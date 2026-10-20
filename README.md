# Academic Website

Personal website built with Jekyll and hosted on GitHub Pages.

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`

## Updating Publications

Export your Zotero collection using **BibLaTeX** to `Personal Publications biblatex.bib`, keeping the existing citation keys, then run:

```bash
python3 update_publications.py
python3 -B -m unittest discover -s tests -v
```

This regenerates `publications.md` and the homepage's `_includes/featured_publication.html`. Update only this active export; `Personal Publications.bib` is retained as a legacy reference and is not merged into the website's input.

BibLaTeX preserves Zotero's **Conference Name** as `eventtitle`, journal names as `journaltitle`, and publication dates as `date`. The site uses Proceedings Title (`booktitle`) when available, otherwise Conference Name. Year-only dates stay year-only; access dates are never used as publication dates.

The repo-local update workflow is documented in `.agents/skills/update-publications/SKILL.md` (`/skill:update-publications` in Pi after `/reload`).

### Mapping Images to New Publications

To show a thumbnail next to a new publication:
1. Add an optimized WebP image to `assets/images/` (square or rectangular is fine; aim for ≤300 KB).
2. Add a mapping in `update_publications.py` under `IMAGE_MAPPINGS` using the BibLaTeX cite key:
   - Example: `'leins_investigating_2026': 'SA-in-robotics.webp'`
3. Run `python3 update_publications.py` to regenerate both publication outputs.

## Deployment

Push to GitHub and enable GitHub Pages in repository settings:
- Settings > Pages
- Source: "Deploy from branch"
- Branch: `main`, folder: `/ (root)`

## Customization

Edit the following files to add your content:
- `_config.yml` - Site title, email, social links
- `index.md` - Home/About page
- `bio.md` - Extended biography
- `Personal Publications biblatex.bib` - Your active Zotero publication export (BibLaTeX format)

## Adding Blog Posts

Create new files in `_posts/` with format: `YYYY-MM-DD-title.md`

Example:
```markdown
---
layout: post
title: "Your Post Title"
date: 2025-01-29
categories: research
---

Your content here...
```
