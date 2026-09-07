# Content sources and remaining details

The site was populated from Jiho Kim's two-page CV on September 7, 2026. The PDF was read without modification.

## Source records

- `static/files/cv.pdf`: Education, experience, teaching, honors, project contributions, publication status, and repository links.
- `data/profile.toml`: Existing UW email, Google Scholar profile, GitHub profile, ORCID identifier, and location.
- `static/images/profile_square.png`: Existing portrait. The broken `.svg` reference was corrected.
- [Divided attention preprint](https://arxiv.org/abs/2608.10320): Full author names, preprint links, and forthcoming TVCG venue.
- [Chart explanation paper](https://pages.cs.wisc.edu/~yeaseulkim/assets/papers/2023_explanation.pdf): Full author names, DOI, and equal contribution notation.
- [Chart question-answering paper](https://arjun010.github.io/assets/papers/blv-qa-chi23.pdf): Full author names, DOI, and paper link.

The PDF metadata title is `cv-260820-JihoKim.docx`. The website labels the CV version August 2026.

## Editorial choices

- The role is **PhD Student in Computer Sciences**, matching the CV. Candidacy status was not inferred.
- The anticipated PhD completion date remains **May 2027**.
- The VIS paper appears once under journal articles. Its preprint identifies TVCG as the forthcoming venue.
- The Publications page combines journal and conference papers in one peer-reviewed list. Preprint and manuscript sections are omitted.
- The two unfinished manuscripts remain as detail pages linked from their projects. No publication years or venues were invented.
- Comparison axis alignment remains a project but is no longer selected work on the home page.
- The CV navigation item downloads the original PDF directly. The separate CV page was removed.
- The Contact page displays the email with `[at]` and `[dot]`. Shared email links lead to this page instead of exposing mailto addresses.
- Short research summaries are paraphrases, not verbatim published abstracts. The interface labels them **Research summary**.
- Missing project results, software stacks, dates, images, and resource links are omitted.
- Motivation and career-interest prose synthesizes the CV's research areas and the stated purpose of this website. Review its wording before publishing.
- Personal interests, an advisor name, a formal dissertation title, academic service, and mentorship claims were not invented.
- The CV's telephone number remains in the PDF. It was not added to the website's contact page.

## Details to confirm

- **Final site URL:** `baseURL` still uses `https://example.org/`. Set the real URL and change `params.noIndex` to `false` before publishing.
- **Email:** The existing UW email is retained as `kim999@wisc.edu`. The CV uses `captainhoji@gmail.com`. Confirm your preferred public address.
- **LinkedIn:** The original profile file contained `https://www.linkedin.com/captainhoji`. The CV's LinkedIn annotation points to an email address. The uncertain link is hidden until you provide the public profile URL.
- **Dissertation:** Add the approved dissertation title and advisor if you want these displayed.
- **Manuscript authors:** The accessible-sampling entry preserves `Y. Zhao` and `X. Zhu` from the CV. Expand these names if desired.
- **TVCG citation:** Add the final publication year, volume, pages, and journal DOI when available. The current year follows the CV's IEEE VIS 2026 entry.
- **Project details:** Add approved figures, dated milestones, quantitative results, and missing code or data links when available.

No changes have been deployed to a remote website.
