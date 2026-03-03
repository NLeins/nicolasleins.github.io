# Academic Website

Personal website built with Jekyll and hosted on GitHub Pages.

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`

## Updating Publications

When you add new entries to `Personal Publications.bib`, run:

```bash
python update_publications.py
```

This will regenerate `publications.md` with your latest publications.

### Mapping Images to New Publications

To show a thumbnail next to a new publication:
1. Add an optimized WebP image to `assets/images/` (square or rectangular is fine; aim for ≤300 KB).
2. Add a mapping in `update_publications.py` under `IMAGE_MAPPINGS` using the BibTeX cite key:
   - Example: `'leins_investigating_2026': 'SA-in-robotics.webp'`
3. Run `python update_publications.py` to regenerate `publications.md`.

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
- `Personal Publications.bib` - Your publications (BibTeX format)

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
