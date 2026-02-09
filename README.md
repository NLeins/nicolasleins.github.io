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
