#!/usr/bin/env python3
"""Check generated HTML and internal links without third-party dependencies."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Document(HTMLParser):
    """Collect only the HTML fields needed for the site checks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.errors = []
        self.meta = {}
        self.canonical = ""
        self.h1_count = 0
        self.lang = ""
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"Duplicate ID: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.in_title = True
        if tag == "img" and "alt" not in attrs:
            self.errors.append("Image is missing an alt attribute")
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property", ""))] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href", "")
        # Some tools share the site's host but live outside this Hugo build.
        check_target = attrs.get("data-external") != "true"
        for key in ("href", "src", "poster"):
            if key in attrs:
                self.references.append((attrs[key], check_target))
        if tag == "object" and attrs.get("data"):
            self.references.append((attrs["data"], True))
        for candidate in attrs.get("srcset", "").split(","):
            if candidate.strip():
                self.references.append((candidate.strip().split()[0], True))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title += text


def check_site(root, base_url):
    """Resolve generated links as a browser would, including Pages subpaths."""
    root = root.resolve()
    base_url = base_url.rstrip("/") + "/"
    base = urlsplit(base_url)
    documents = {}
    failures = []
    checked = 0
    for path in sorted(root.rglob("*.html")):
        document = Document()
        document.feed(path.read_text(encoding="utf-8"))
        documents[path] = document
        errors = document.errors
        if document.h1_count != 1:
            errors.append(f"Expected one h1, found {document.h1_count}")
        if not document.lang or not document.title.strip():
            errors.append("Missing page language or title")
        for field in ("description", "viewport", "og:title", "og:description", "og:url", "og:type"):
            if not document.meta.get(field):
                errors.append(f"Missing metadata: {field}")
        if not document.canonical:
            errors.append("Missing canonical URL")
        if document.meta.get("og:url") != document.canonical:
            errors.append("Open Graph URL does not match the canonical URL")
        failures.extend(f"{path.relative_to(root)}: {error}" for error in errors)

    def resolve(reference, source_url, source_name):
        nonlocal checked
        target_url = urlsplit(urljoin(source_url, reference))
        if target_url.scheme not in ("http", "https") or target_url.netloc != base.netloc:
            return
        checked += 1
        target_path = unquote(target_url.path)
        if not target_path.startswith(base.path):
            failures.append(f"{source_name}: link escapes the site subpath: {reference}")
            return
        relative_path = target_path[len(base.path):]
        target = (root / relative_path).resolve()
        if not target.is_relative_to(root):
            failures.append(f"{source_name}: link escapes the build directory: {reference}")
            return
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            failures.append(f"{source_name}: missing target: {reference}")
            return
        if target_url.fragment and target in documents:
            fragment = unquote(target_url.fragment)
            if fragment not in documents[target].ids:
                failures.append(f"{source_name}: missing fragment: {reference}")

    for path, document in documents.items():
        relative = path.relative_to(root).as_posix()
        route = relative[:-10] if relative.endswith("index.html") else relative
        source_url = urljoin(base_url, route)
        expected_canonical = source_url
        if document.canonical != expected_canonical:
            failures.append(f"{relative}: canonical URL should be {expected_canonical}")
        for reference, check_target in document.references:
            if check_target:
                resolve(reference, source_url, relative)

    # Sitemap and robots URLs must use the same deployment prefix as the HTML.
    sitemap = root / "sitemap.xml"
    if sitemap.exists():
        try:
            for location in ET.parse(sitemap).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                resolve(location.text or "", base_url, "sitemap.xml")
        except ET.ParseError as error:
            failures.append(f"Invalid sitemap XML: {error}")
    else:
        failures.append("Missing sitemap.xml")
    robots = root / "robots.txt"
    if not robots.exists() or f"Sitemap: {base_url}sitemap.xml" not in robots.read_text():
        failures.append("robots.txt is missing the correct sitemap URL")
    if not documents:
        failures.append("No generated HTML files found")
    if failures:
        print("Site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Passed: {len(documents)} HTML pages, {checked} internal references, metadata, sitemap, and robots.txt.")
    print("External destinations are not checked.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?", default=Path("public"))
    parser.add_argument("--base-url", default="https://example.org/")
    args = parser.parse_args()
    sys.exit(check_site(args.directory, args.base_url))
