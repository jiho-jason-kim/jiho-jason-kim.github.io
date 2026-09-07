# Jiho Kim's academic website

This is the detailed maintenance guide. See the [public README](../README.md) for a short overview.

This website was made with help from GPT-6 Astra.

A Hugo website for Jiho Kim's academic and industry applications. The content follows the August 2026 CV and verified publication records.

The site includes Home, Research, Publications, Projects, Teaching, About, and Contact. The CV tab downloads the PDF directly.

It has no theme dependency, JavaScript, external fonts, analytics, or package manager requirements.

## Requirements and local development

Use **Hugo 0.153.4 or later**. The workflow pins Hugo 0.153.4, which is the version used for verification. Standard Hugo is sufficient. Hugo Extended also works.

Install Hugo on macOS with Homebrew:

```sh
brew install hugo
hugo version
```

For other systems, use the [official Hugo installation instructions](https://gohugo.io/installation/).

Run these commands from the repository directory:

```sh
hugo server -D
```

Visit [http://localhost:1313/](http://localhost:1313/). Hugo rebuilds when you save content. The `-D` option includes drafts during development. Press `Ctrl+C` to stop the server.

Build the production files:

```sh
hugo --gc --minify --panicOnWarning
```

Hugo writes the generated site to `public/`. Do not commit that directory. No Go, Node.js, or Sass installation is required.

## Maintain the content

1. **`data/profile.toml`**: Update contact details, profile links, portrait, and CV date.
2. **`hugo.toml`**: Set the final `baseURL` and update search metadata when needed.
3. **`content/_index.md`**: Update the introduction, biography, and research interests.
4. **`content/`**: Maintain page content and individual publication and project entries.
5. **`static/files/cv.pdf`**: Replace this file when a newer CV is available.

The source contains five publication entries and eleven project entries from the CV. The Publications page combines the three peer-reviewed papers in one list.

Preprints and manuscripts in preparation are excluded from that list. Manuscript detail pages remain available through their related projects.

See `CONTENT_NOTES.md` for source records and details that still need confirmation. Empty resource and profile URLs are hidden.

`params.sampleMode` is now `false`. New archetypes still begin as drafts with sample labels to prevent accidental publication of unfinished entries.

`params.noIndex` remains `true` until the final site address is configured. Set it to `false` before publishing the finished site. This setting controls search indexing, not access.

## Repository structure

```text
.github/workflows/hugo.yml    Build, check, and deploy with GitHub Actions
archetypes/                  Templates for new Markdown content
assets/css/main.css          Organized stylesheet and design tokens
content/                    Pages, publications, and projects
data/profile.toml            Shared personal details and profile links
CONTENT_NOTES.md              Content sources and remaining details
data/publication_categories.toml  Publication groups and their order
hugo.toml                    Hugo settings, SEO defaults, and navigation
layouts/                     Custom Hugo layouts
layouts/_partials/           Reusable header, footer, and components
layouts/_shortcodes/         CV download links for Markdown content
layouts/publications/        Publication list and detail templates
layouts/projects/            Project list and detail templates
scripts/check_site.py        Internal link and metadata checks
static/favicon.svg           Replaceable initials favicon
static/images/               Jiho Kim's portrait
static/files/cv.pdf           Current CV supplied by Jiho Kim
```

Hugo uses `_partials` for reusable templates. This repository uses the template structure introduced in Hugo 0.146.0.

## Add a publication

Create a Markdown file from the publication archetype:

```sh
hugo new content publications/my-paper.md
```

Edit the front matter at the beginning of the new file:

```yaml
---
title: "Your publication title"
description: "A concise description for readers and search engines."
date: 2026-09-01
year: 2026
category: journal
work_type: Journal article
authors: ["Your Name", "Coauthor Name"]
venue: "Your journal or conference"
abstract: "Your complete abstract."
doi: ""
pdf: ""
code: ""
data: ""
project: ""
citation: |
  Paste your BibTeX citation here.
featured: false
featured_order: 4
sample: false
draft: false
---
```

Choose `journal`, `conference`, `preprint`, or `working-paper` for `category`. The build rejects unknown categories. Only `journal` and `conference` entries appear on the Publications page.

Use the actual publication year. `date` controls Hugo's publication scheduling. A future date stays unpublished until that date unless you use `hugo server -F`.

The DOI field accepts either a DOI identifier or a complete DOI URL. Other resource fields accept an HTTPS URL or a site-relative path. For example, place a PDF in `static/files/my-paper.pdf` and set `pdf: "files/my-paper.pdf"`.

Use `project: "/projects/my-project/"` to connect a publication to a project. Leave unavailable resource fields empty. The template hides those links.

The list displays authors, venue, year, resource links, abstract, and citation. Native disclosure controls expand the abstract and citation. Each publication also has its own detail page.

The current entries use paraphrased research summaries, labeled with `abstract_label: "Research summary"`. For the published abstract, replace the text and use `abstract_label: Abstract`.

Use `author_note` for contribution notes and `preprint` for a preprint URL. Leave `year` and `date` absent for undated manuscripts in preparation.

Add optional notes below the front matter. Use Markdown headings for the overview, contribution, and limitations. **No template edits are required.**

## Add a project

```sh
hugo new content projects/my-project.md
```

Edit the generated front matter and Markdown sections. Each project supports:

- Title, description, year, status, and your role.
- Methods and technologies as YAML lists.
- `github`, `paper`, and `demo` resource links.
- `image`, `image_alt`, and `image_caption` fields.
- Markdown sections for the research problem, contribution, methods, results, and technologies.

Place project images in `static/images/`. Set `image: "images/my-project.webp"` and provide a useful `image_alt` description. Use a 16:9 image where practical. An empty image field removes the image.

Set `sample: false` and `draft: false` when the content is ready. **No template edits are required.**

Use `weight` to order projects. Lower values appear first. Omit dates, status, and technologies when they are not documented.

## Choose selected work

Set `featured: true` on publication or project entries. Set `featured_order` to control their order. The home page shows the first five featured entries. Keep three to five entries selected.

## Update the profile photo

1. Place your portrait at `static/images/profile.webp` or use another supported image format.
2. Set `photo = 'images/profile.webp'` in `data/profile.toml`.
3. Set `photoAlt` to a short description, such as `Portrait of Your Name`.
4. Update `photoCaption`, or set it to an empty string.
5. Remove the previous portrait when it is no longer used.

Use a square portrait of at least 414 × 414 pixels. Compress it before adding it. CSS displays a smaller circular crop and preserves the original image file.

The current portrait is `static/images/profile_square.png`. The favicon uses Jiho Kim's initials. Update `static/favicon.svg` to change it.

## Update the CV

Replace `static/files/cv.pdf` with your accessible, text-based PDF. Keep the filename to preserve existing links. If you change the filename, update `cv` in `data/profile.toml`.

Update `cvUpdated` in `data/profile.toml` for your maintenance records.

The CV navigation item and home button download the PDF directly. There is no separate CV page.

Use `{{< cv-link >}}` in Markdown to insert a CV download link. Set custom text with `{{< cv-link text="Download curriculum vitae" >}}`.

## Change navigation

Edit the `[[menus.main]]` entries in `hugo.toml`. Page entries use `name`, `pageRef`, and `weight`. Lower weights appear first.

The CV entry uses `params = { download = true }` and reads its file path from `data/profile.toml`. The same menu supplies desktop and mobile navigation.

To add a page:

```sh
hugo new content new-page.md
```

Write the page, set `draft: false`, then add its menu entry. For links inside Markdown, use Hugo references:

```markdown
[Research]({{< relref "/research" >}})
[My project]({{< relref "/projects/my-project" >}})
```

These references work on both account Pages sites and repository subpaths. Hugo also detects missing reference targets during builds.

## Design and accessibility

Edit the variables at the start of `assets/css/main.css` to change colors and fonts. The remaining CSS has labeled sections for shared components, pages, responsive layouts, and print.

The site uses system fonts, semantic landmarks, one main heading per page, visible focus states, image descriptions, and a skip link. Native HTML controls provide mobile navigation and publication disclosures. No JavaScript is shipped in production. Hugo adds its own live-reload script during development.

Dark mode is omitted to keep the stylesheet small. Navigation collapses below 900 pixels. The main content uses one column on narrow screens.

## Email display

Maintain the email in `data/profile.toml`. The Contact page converts it to `name [at] domain [dot] edu` during the build.

Generated HTML contains no raw email address or mailto link. Email links lead to the Contact page. This discourages simple address harvesting without JavaScript.

The downloadable CV retains its original contact details.

## SEO and search indexing

Shared templates provide page titles, descriptions, canonical URLs, Open Graph metadata, and Twitter card metadata. Each Markdown `description` overrides the default in `hugo.toml`.

Hugo generates `sitemap.xml`. The custom `robots.txt` points to that sitemap. Crawling stays enabled so search engines can read `noindex` metadata during setup.

To add a social preview image, place it in `static/images/` and set `params.socialImage` in `hugo.toml`. Use your own image. No image is required for the existing text metadata.

## Verify changes

Python 3.9 or later is required for the optional checker. GitHub's runner includes Python.

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py public --base-url https://example.org/
```

Use your configured `baseURL` in the check command. Test repository subpaths with:

```sh
hugo --gc --minify --panicOnWarning --baseURL https://example.org/academic/ --destination /tmp/academic-check
python3 scripts/check_site.py /tmp/academic-check --base-url https://example.org/academic/
```

The checker verifies internal pages, assets, fragments, headings, metadata, sitemap entries, and the robots sitemap URL. It does not check external destinations or verify publication claims.

Also review the home, publication, project, and contact pages at desktop and mobile widths. Test the menu, keyboard focus, disclosure controls, and PDF download after content changes.

## Deploy with GitHub Pages

The workflow follows the [official Hugo GitHub Pages deployment model](https://gohugo.io/host-and-deploy/host-on-github-pages/). It builds on pushes and pull requests. Only the `main` branch can deploy.

1. Create a GitHub repository. Use `USERNAME.github.io` for an account site, or another repository name for a project site.
2. Review `CONTENT_NOTES.md`, set `baseURL`, and set `params.noIndex = false` in `hugo.toml`.
3. In the repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Commit the source files and push them to `main`.
5. Open **Actions → Build and deploy Hugo** to monitor the build and deployment.
6. Open the URL from the completed deployment.

Typical URLs are:

```text
Account site: https://USERNAME.github.io/
Project site: https://USERNAME.github.io/REPOSITORY/
```

For a new local repository, replace the uppercase values before running:

```sh
git init -b main
git add .
git commit -m "Create academic website"
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

The workflow uses the Pages-provided URL during builds. This preserves repository subpaths and configured custom domains. It verifies the Hugo archive checksum, builds the site, checks internal links, uploads the output, and deploys it.

No personal access token or deployment branch is required. GitHub supplies a scoped token to the workflow. Pull requests run the build and checks without publishing.

For a custom domain, configure it in **Settings → Pages** and set `baseURL` to the same HTTPS URL. For a different default branch, update the workflow branch filters and deployment condition.

Publishing requires your GitHub repository and Pages settings. This project does not create a remote repository or publish automatically from your computer.
