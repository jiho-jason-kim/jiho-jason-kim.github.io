# Jiho Kim’s academic website

Personal academic website for Jiho Kim, a PhD student in Computer Sciences at the University of Wisconsin–Madison.

The site presents research, publications, projects, teaching, and contact information. The CV link downloads the current PDF.

Built with Hugo and custom templates. Content uses Markdown files. The site uses system fonts and requires no JavaScript.

## Run locally

Install Hugo 0.153.4 or later. On macOS:

```sh
brew install hugo
```

From the repository directory, start the development server:

```sh
hugo server -D
```

Open [localhost:1313](http://localhost:1313/). Changes appear when you save a file.

## Update content

- **Pages, publications, and projects:** `content/`
- **Profile and contact details:** `data/profile.toml`
- **CV:** `static/files/cv.pdf`
- **Profile photo:** `static/images/profile_square.png`
- **Navigation and site settings:** `hugo.toml`
- **Styles:** `assets/css/main.css`

See the [maintenance guide](docs/MAINTENANCE.md) for content examples, checks, and deployment details.

## Publish with GitHub Pages

1. Set `baseURL` in `hugo.toml` to your public site address. Set `params.noIndex` to `false` when ready.
2. In GitHub, select **Settings → Pages → Source → GitHub Actions**.
3. Push changes to `main`. The included workflow builds, checks, and deploys the site.

## Acknowledgment

This website was made with help from GPT-6 Astra.
