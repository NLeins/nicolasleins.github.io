# Website design polish plan

## Working agreement

- Work one pass at a time. Stop for review after each pass.
- Ask Nicolas for preferences before starting the next pass or choosing a new design direction.
- Do not start the next pass until the current one is approved.
- Refine the existing site, not its information architecture or content.
- Use user-confirmed personal dates. Confirm previously hidden personal metadata before introducing it visibly; do not infer dates from related roles.
- Keep Jekyll, Minima, Liquid, SCSS, and the Python publication generator.
- Keep existing URLs and the Home / Bio / Publications / Blog navigation.
- Never manually edit generated publication files; change the generator when needed.
- This plan is excluded from the published Jekyll site.

## Confirmed preferences

- Visual impact: subtle refinement, not a noticeably different design.
- Colors: retain the existing navy/blue palette; deeper shades are acceptable for contrast.
- Typography: keep system fonts; no external font service.
- Save decisions and progress here so work can resume in a later session.
- Pass 1 was reviewed and approved: “looks good.”
- Pass 2 portrait: faint blue glow plus a static centered ring, not a node illustration. Nicolas requested a concentric ring after reviewing the initial offset version.
- Pass 2 hero: add “Researcher · Zuse Institute Berlin,” refine spacing and headline sizing, and preserve all existing text.
- Pass 2 featured publication: thin blue accent plus a soft background tint.
- Pass 2 was approved after centering the portrait ring: “great.”
- Pass 3a publications: make cards more compact; add subtle metadata-supported type labels; keep year headings only, without jump links.
- Pass 3a was reviewed and approved: “looks good.”
- Pass 3b biography: date labels and separators only, without dots or a vertical timeline; small “Current” labels on the Ph.D. and current research role. Retain white cards and the existing two columns.
- User-confirmed dates: Ph.D. since 2025; ZIB researcher since 2025; WBI research assistant 2022–2025. Corrected in `_data/person.yml` after biography review.
- Pass 3b was approved after those date corrections: “biography is good.”
- Pass 3c blog: editorial listing, not cards; centered article reading column of roughly 70 characters, refined spacing, and lightly framed figures. Preserve all post text and dates.
- Pass 3c was approved: “nice.”
- Pass 3d footer: keep the centered arrangement and white background, with one fine divider, less excess spacing, and softer icon styling. Keep the existing social/legal links and add no visible content.
- Pass 3d was approved: “looks good.” Nicolas requested committing the approved changes before final validation or optional portrait optimization.

## Pass 1 — Shared foundation

**Status:** Approved by Nicolas. Sass and focused source checks passed. Full Jekyll build and browser checks remain unverified.

Scope:
- Consolidate color, spacing, border-radius, shadow, and transition values in `assets/main.scss`.
- Keep the white background, existing layout, and basic type scale.
- Refine heading weight, line height, and readable mobile text.
- Give cards softer shadows and consistent borders; remove misleading hover movement from static panels.
- Standardize primary/secondary buttons and their hover/visited states.
- Use a deeper shade of blue for readable links and white-label buttons.
- Add visible focus styles and reduced-motion support for shared transitions.
- Consolidate duplicate publication image/title rules without redesigning publication cards.
- Replace only the homepage secondary button's inline styling with a shared class.

Files:
- `assets/main.scss`
- `index.md` (secondary button class only)
- `_config.yml` (exclude this internal plan from publishing)
- `DESIGN-POLISH-PLAN.md`

Not included: hero decoration, new homepage content, active navigation indicator, publication badges or year links, biography timelines, blog redesign, new fonts, or new dependencies in the project.

Review checklist:
- Does the deeper blue still feel right?
- Are the calmer cards and heading weights an improvement?
- Do primary/secondary buttons look balanced?
- Does the site still feel like the same website on desktop and mobile?

## Pass 2 — Homepage preview

**Status:** Approved by Nicolas after centering the portrait ring. Sass and focused template checks passed; full Jekyll build and browser checks remain unverified.

Agreed scope:
- Preserve text-left / portrait-right arrangement and the existing stacked mobile layout.
- Add a static faint blue glow and centered ring around the portrait using decorative CSS pseudo-elements.
- Add the affiliation label above the greeting, refine spacing, and gently scale the headline without rewriting existing text.
- Style the existing featured-publication include through a homepage-only section, with a thin blue accent and soft tint. Leave generated markup and ordinary publication cards untouched.
- Replace homepage section/action inline spacing with named classes.
- Add an active-page navigation indicator, including a Blog section indicator on blog posts.
- Label navigation and retain Minima's checkbox menu while making its mobile toggle keyboard-reachable.

Files: `index.md`, `assets/main.scss`, `_includes/header.html`, and this plan. No publication regeneration is needed because neither the generator nor its inputs/outputs changed.

Review the portrait detail, hero sizing, featured-card emphasis, and current-page indicator before starting any remaining-page work.

## Pass 3 — Remaining pages

**Status:** All four individually reviewed page-polish steps are approved.

### Pass 3a — Publications

**Status:** Approved by Nicolas: “looks good.”

Agreed scope and implementation:
- Compact cards with 16px padding/gaps, 128px thumbnail panels (112px on phones), and tighter metadata spacing. Preserve full figures using `object-fit: contain`, and keep all existing titles/authors/dates/links.
- Put subtle paper-type labels alongside venue/date metadata rather than adding a separate row. Label arXiv preprints, conference proceedings, and journal articles only when metadata supports it. Leave the software repository unlabeled. Recognize the ICIS Proceedings entry as a conference paper despite its BibTeX `article` type.
- Retain year headings with a quiet separator line. No year-jump navigation or filtering.
- Use matching Cite/link controls without pipe separators, with mobile-sized touch targets.
- Use a real button for copying BibTeX, per-card live success/error feedback, a busy state that preserves focus, legacy clipboard fallback, and safe repeated-click handling.
- Keep all compact styles scoped to the publications page so the approved homepage feature is unchanged.
- Generate markup through `update_publications.py` and regenerate `publications.md`. Keep citation JavaScript in `assets/publications.js`, loaded only by the publications page.
- Add standard-library regression tests in `tests/test_update_publications.py`; exclude `tests/` from the published site.

Files: `update_publications.py`, generated `publications.md`, `assets/main.scss`, new `assets/publications.js`, new `tests/test_update_publications.py`, `_config.yml` (test-directory exclusion), and this plan.

### Pass 3b — Biography

**Status:** Approved by Nicolas after correcting the personal dates below. Sass and focused template checks passed.

Agreed scope and implementation:
- Keep the existing two-column biography layout, introduction, research interests, and contact cards unchanged.
- Refine only education and professional-experience records using date-first rows, existing titles/institutions/descriptions, and fine horizontal separators. No timeline rail, dots, animation, or tinted entry backgrounds.
- Add small outlined “Current” labels based on existing status metadata, not inferred from job/degree titles.
- Show the current Ph.D. as “Since 2025,” based on the user's correction, avoiding a redundant “Currently / Current” pair. Correct the ZIB researcher start to 2025 and WBI research assistant range to 2022–2025; retain the other completion years and position date ranges.
- Preserve all supervisor details and links.
- Replace touched inline styles with nine scoped biography rules. Use semantic ordered lists without visible numbering, retaining list semantics for assistive technology.

Files: `bio.md`, `assets/main.scss`, `_data/person.yml` (user-requested date corrections), and this plan. No other personal data was changed.

### Pass 3c — Blog

**Status:** Approved by Nicolas: “nice.” Sass and focused template checks passed.

Agreed scope and implementation:
- Replace the plain blog list with an editorial listing: date, linked title, a short excerpt derived from the existing post, and a reading link. Use fine separators instead of card boxes.
- Show up to 45 words of existing excerpt text, stripping HTML and preserving encoded characters without double escaping. Skip empty excerpts and provide a quiet empty-list state.
- Keep post order, dates, titles, and URLs unchanged. No new posts, rewritten prose, reading-time estimates, or fabricated metadata.
- Center individual articles in a `70ch` maximum-width reading column. Refine title/paragraph/heading spacing and lightly frame images without cropping them. Support existing figure captions when present, without inventing new ones.
- Add only a scoped article class to the post layout; preserve content insertion, author/date markup, structured metadata, and optional comments behavior.
- Keep all new styles scoped to `.blog-index` or `.blog-article`, leaving approved pages unchanged.

Files: `blog.md`, `_layouts/post.html`, `assets/main.scss`, and this plan. `_posts/`, personal data, navigation, and footer are unchanged in this pass.

### Pass 3d — Footer

**Status:** Approved by Nicolas: “looks good.” Sass and focused template checks passed.

Agreed scope and implementation:
- Preserve the centered social-icons/legal-links arrangement and white footer background.
- Use a single fine top divider; remove the redundant inner border and excess inner margin/padding. Set outer footer padding to 24px and tighten the gap between icons and legal links.
- Keep 44px social controls, with pale neutral surfaces, subtle borders, and existing blue hover feedback. Allow icons to wrap on narrow screens.
- Give social/legal groups descriptive navigation labels and icon links explicit accessible names. Hide decorative SVGs and the legal separator from assistive technology. Include static new-tab safety attributes.
- Preserve all existing link destinations, icon paths, legal text, profile visibility conditions, and the existing external-link script. No copyright, dates, new links, or other visible content was added.

Files: `_includes/footer.html`, `assets/main.scss`, and this plan. All other page sources remain unchanged in this pass.

Generated publication markup changes must go through `update_publications.py`, followed by regeneration.

## Pass 4 — Final validation

**Status:** Pending. Nicolas requested committing the approved changes instead of answering the validation-tooling/portrait questions. Full Jekyll build, real-browser checks, and optional portrait optimization have not been authorized or completed. Focused checks from earlier passes are recorded below.

- Build Jekyll with the existing locked dependencies.
- Check desktop, tablet, and mobile rendering, especially navigation and long publication titles.
- Check keyboard navigation, focus, color contrast, and reduced motion.
- Check citation copying, links, image loading, and generated publication output where changed.
- Consider resizing/re-encoding the oversized portrait after confirming image preferences.

## Validation log

### Pass 1 checks

- Sass compiled successfully using Dart Sass 1.77.8 against the locked Minima 2.5.1 theme. The downloaded theme gem matched its lockfile checksum. Validation dependencies and compiled CSS were kept outside the repository.
- Shared link/button contrast: 6.15:1 on white; shared link text on the pale action surface: 5.88:1. Shared muted/subtle text on white also passed 4.5:1. This is not a full site-wide contrast audit; untouched inline styles remain for later passes.
- Focus and reduced-motion styles are present in compiled CSS.
- Duplicate base publication image/title rules were consolidated, and static-card hover movement is absent.
- Verified the secondary button uses its shared class and the plan is excluded from publishing.
- `git diff --check` passed.
- Publication output, featured-publication include, generator, BibTeX, and personal data were unchanged.
- Full Jekyll build unavailable: this environment has no Ruby/Bundler installation. No browser rendering checks were performed. Existing `_site/` output was not regenerated.
- For visual review in an environment with the project's Ruby dependencies installed, run `bundle exec jekyll serve` and review the freshly built pages rather than the old `_site/` files.

### Pass 2 checks

- Sass compiled against the same locked Minima 2.5.1 theme using Dart Sass 1.77.8.
- LiquidJS rendered the changed header for 14 route/base-URL combinations: Home, Bio, Publications, Blog, a blog article, Legal Notice, and Privacy Policy, with and without `/preview` as a base URL. Exactly the intended navigation item was marked; unrelated pages had none.
- The homepage template rendered with its real featured-publication include. Existing introduction text, primary/secondary actions, section labels, and base-URL links were checked.
- Verified compiled styles contain the static glow/ring, homepage-scoped feature treatment, active-navigation indicator, and keyboard-focusable mobile toggle treatment. No animation was introduced.
- `git diff --check` passed.
- Publication output, featured include, generator, BibTeX, personal data, Bio/Blog sources, and article layout remain unchanged.
- Validation packages, generated CSS, and test renderings were kept in a temporary directory, outside the repository. No new project dependencies were added.
- LiquidJS template checks are supplemental, not proof of a full Ruby/Jekyll build. Ruby/Bundler and a browser are unavailable here, so no full build or browser visual checks were performed. Existing `_site/` output was not regenerated.

### Pass 3a checks

- Eight standard-library Python regression tests passed: supported paper labels (including ICIS proceedings and unknown types), exact BibTeX preservation, meaningful image attributes, balanced markup with/without images, HTML escaping, year ordering, and homepage-feature isolation.
- Eight temporary jsdom scenarios passed: modern clipboard success, missing/denied/throwing clipboard APIs, legacy success/failure, textarea cleanup, focus preservation, per-card live feedback, busy-state click guards, repeated-copy timer handling, independent cards, and ignoring controls outside the list.
- `node --check assets/publications.js` and `git diff --check` passed.
- Sass compiled using Dart Sass 1.77.8 against locked Minima 2.5.1.
- Regeneration was checked for idempotence. The homepage featured include remains byte-for-byte unchanged.
- DOM simulation is not a real-browser clipboard/layout test. Full Jekyll build and browser visual checks remain unavailable in this environment. Temporary DOM-test dependencies and compiled CSS were kept outside the repository; no new project dependencies were added.
- Run persistent Python checks with `python3 -B -m unittest discover -s tests -v`. Regenerate with `python3 update_publications.py` in environments without the `python` alias.

### Pass 3b checks

- Sass compiled against locked Minima 2.5.1 using Dart Sass 1.77.8. Comparing compiled before/after CSS verified that only nine biography-scoped rules were added; all existing compiled rules were unchanged.
- LiquidJS/jsdom checks covered the actual biography render plus completed-current entries, a current education entry without a start year, special-character escaping, and empty lists.
- Verified all education/experience entries remain in their original order, exactly the intended entries receive “Current,” and all existing links and supervisor details remain intact.
- Verified introduction, research interests, contact cards, section headings, and the two-column markup remain identical to their pre-pass renderings.
- Existing eight Python publication regression tests and `git diff --check` passed.
- Full Ruby/Jekyll and real-browser visual checks remain unverified. Validation output and supplemental checks were kept outside the repository, with no new project dependencies.

### Pass 3c checks

- Sass compiled against locked Minima 2.5.1 using Dart Sass 1.77.8. Comparing compiled before/after CSS verified that only 19 blog-scoped rules were added; all existing compiled rules were unchanged.
- Seven LiquidJS/jsdom scenarios passed: actual post listing with and without a base URL, post ordering, absent excerpts, empty list, escaped titles/entities, article content insertion, author fallback, dates, and structured metadata.
- Verified the original post source is byte-for-byte unchanged and the post-layout source differs only by its new scoped class. Article HTML is inserted unchanged in template checks.
- Re-ran biography checks and confirmed the corrected dates remain Ph.D. 2025, ZIB 2025, and WBI 2022–2025.
- Existing eight Python publication regression tests and `git diff --check` passed.
- Full Ruby/Jekyll and real-browser visual checks remain unverified. Supplemental validation files and generated CSS stayed outside the repository; no project dependencies were added.

### Pass 3d checks

- Sass compiled against locked Minima 2.5.1 using Dart Sass 1.77.8. Comparing compiled before/after CSS verified all non-footer styles were unchanged.
- Eight LiquidJS/jsdom footer contexts passed: root/base-URL links, each omitted profile, no profiles, and missing credentials. Checked preserved destinations/icon paths/legal text, navigation labels, accessible link names, hidden decorative SVGs, and static new-tab safety attributes.
- DOM computed-style checks confirmed centered content, white background, 24px outer padding, 44px social controls, and no redundant inner divider/margin/padding. These simulated checks do not establish real-browser layout, hover, or keyboard behavior.
- Existing external-link script is byte-for-byte unchanged.
- Re-ran blog template checks, the eight Python publication regression tests, and `git diff --check`; all passed.
- Full Ruby/Jekyll and real-browser visual checks remain unverified. Supplemental validation files and generated CSS stayed outside the repository; no project dependencies were added.

All design passes (1, 2, 3a–3d) are approved. The approved changes are ready to commit at Nicolas's request. Final validation remains pending; ask for tooling preferences before starting it. Portrait optimization is optional, remains unapproved, and has not been performed.
