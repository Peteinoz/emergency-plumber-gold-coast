# Project notes: Moyle Plumbing & Gasfitting, emergency plumber Gold Coast site

Static site for GitHub Pages. Base URL: https://peteinoz.github.io/emergency-plumber-gold-coast/
This file is build facts only. It is excluded from sitemap.xml.

## Current state (updated 2026-09-18)

**Status: built. 56 pages plus 404.html and sitemap.xml, QA passing with zero failures.**

Built as a no-SOURCE site on Pete's instruction after the network policy blocked the SOURCE and its
image hosts. All copy is written from the fact sheet in the brief and general plumbing knowledge. No
hours, prices, guarantees, awards, reviews or response-time claims beyond the brief's facts.

### Images: what happened

Pete reported uploading photos to `/images` on this branch, but no image files existed on any branch
or in the GitHub API listing when the build ran. The site therefore has **no photographs**:

- Header and footer logo: an inline SVG wordmark in brand colours (in `tools/build.py`, `WORDMARK_SVG`).
- `images/moyle-plumbing-gasfitting-logo.png`: generated wordmark PNG, used only for JSON-LD `logo`.
- `images/og/moyle-plumbing-gold-coast.jpg`: generated 1200x630 brand card with the NAP, used as the
  og:image on every page and as JSON-LD `image`.
- `images/moyle-plumbing-gasfitting-yatala-card.webp`: 640x336 version of the card, shown on the
  home page in the Find us section (it carries the one image alt with the target phrase).
- `images/favicon.ico` and `images/apple-touch-icon.png`: generated drop icon.
- Every page hero uses a CSS facts panel instead of a photo. No placeholders, no broken image tags.

**To add real photos later:** drop them in `images/`, resize to displayed size, convert to WebP, then
set `hero=dict(src=..., alt=..., w=..., h=...)` on the relevant page in `tools/content/`, replace
`WORDMARK_SVG` with an `<img>` of the real logo if wanted, regenerate the og image from a real photo,
and rerun `python3 tools/build.py && python3 tools/qa.py`.

### Verification done

- `tools/qa.py`: 0 failures. Checks: page count and files; NAP in every footer; exactly one contextual
  main-site link per page inside `<main>` in a sentence; no leading-slash or remote assets; every
  internal link and asset resolves; unique titles, descriptions and H1s; JSON-LD parses and FAQ
  schema matches visible FAQs; canonical, og:url and sitemap agree; target phrase only in the home
  title and H1; no 24/7 or hours claims; no mobile number or PO Box; 6-word shingle overlap between
  pages is zero (place names, NAP and brand exempt as the brief allows).
- Playwright screenshots at 390px and 1280px: no console errors, nav toggle works, sticky call bar on
  mobile, layout intact.
- Lighthouse 12 mobile (local server): home, blocked-drains, plumber-coomera, contact-us,
  hot-water-system-logan and electrolysis-in-copper-pipe all 100 performance, 100 accessibility,
  100 best practices, 100 SEO after two fixes (link contrast token darkened; the `js` class is now
  added by an inline one-liner in the head so the collapsed nav does not cause layout shift).
- The Google Maps iframe and the youtube facade: the map embed is present on home and contact
  (lazy-loaded); the video facade was skipped per instruction.

### Decisions and assumptions

- `blog` kept as a second index (by topic) because the SOURCE could not be checked for a 404. Drop
  it by deleting `tools/content/blog.py` and rebuilding if the SOURCE /blog does not resolve.
- Blog post `datePublished` is this site's publish date (2026-09-18), not the SOURCE post date.
- Footer shows email under the NAP block with the QBCC licence and ABN.
- Hero facts panel text is treated as shell (excluded from the copy-overlap check) like the header
  and footer.
- Suburb facts are limited to what is generally known: housing era, estate versus acreage, canal
  ground, tank and septic country. No drive times or distances are stated as numbers.
- Home-page link anchors are unique on every page and all emergency-related; main-site anchors are
  split roughly 60% brand, 20% naked URL, 20% partial-match, each partial-match phrase used once.

## Page inventory: 56 pages

Core (7): `/`, `contact-us`, `about-us`, `environmental-green-plumbers`, `products-and-brands`,
`handy-hints-blog`, `blog`.

Services (23): `all-services-available`, `general-plumbing-maintenance`, `blocked-drains`, `hot-water`,
`hot-water-tempering-valves`, `emergency-plumbing`, `commercial-plumbing`, `dishwasher-installations`,
`gas-fitting`, `leak-repairs`, `prepurchase-plumbing-inspection`, `pumps`,
`real-estate-property-manager`, `toilets`, `burst-pipe`, `water-filter-installation`,
`bathroom-modifications`, `suburbs-serviced`, `leaking-shower-repairs`, `bathroom-renovations`,
`insinkerator`, `bbq-gas-bottle`, `water-compliancy`.

Service areas (23): `blocked-drains-coomera`, `plumber-coomera`, `plumber-eight-mile-plains`,
`plumber-hope-island`, `plumber-pimpama`, `plumber-loganholme`, `plumber-ormeau`,
`plumber-rochedale-south`, `plumber-mount-cotton`, `emergency-plumber-beenleigh`, `plumber-beenleigh`,
`emergency-plumbers-helensvale`, `plumber-helensvale`, `plumbing-services-alberton`,
`plumber-shailer-park`, `blocked-drains-ormeau`, `hot-water-repairs-brisbane-southside`,
`hot-water-springwood`, `hot-water-system-logan`, `hot-water-systems-brisbane-southside`,
`hot-water-gold-coast`, `plumber-redland-bay`, `yarrabilba-plumber`.

Blog posts (3): `frequently-asked-questions`, `helpful-tips-for-plumbing-emergencies`,
`electrolysis-in-copper-pipe`. Any further posts in the SOURCE sitemap are unknown (sitemap unreachable).

### SOURCE-to-new slug map

Slugs are unchanged except: `general-plumbing-maintenance` <-
/general-domestic-maintenance-emergency-plumbing-and-gas-fitting; `hot-water-tempering-valves` <-
/hot-water-system/tempering-valves; `gas-fitting` <- /gas; `leaking-shower-repairs` <-
/shower-renovations; `bathroom-renovations` <- /bath-rennovations; blog posts flattened from
/handy-hints-blog/<slug> to /<slug>. The same map is in `tools/slugmap.py`.

Excluded: /testimonials/*, /search, cart, account and system URLs, the nav folders /services,
/service-areas and /about-us-1.

## Repo layout

- `index.html`, `<slug>/index.html` (56 pages), `404.html`, `sitemap.xml`, `.nojekyll`
- `css/style.css` (about 13 KB), `js/main.js` (under 1 KB, deferred, nav toggle only)
- `images/`: generated brand assets listed above
- `tools/build.py`: shell renderer, JSON-LD, sitemap and 404 generation
- `tools/content/*.py`: one module per page plus `_common.py` helpers
- `tools/qa.py`: section-13 checks; `tools/fetch_source.py` and `tools/slugmap.py`: SOURCE research
  helpers for when network access exists (output folders gitignored)

## How to build

```
python3 tools/build.py     # renders every page, 404.html and sitemap.xml
python3 tools/qa.py        # exit code 1 on any failure
```

Body copy uses `{rel}` for the path prefix and `{map}` for the Google Maps embed. The committed HTML
is the deliverable; the tools folder is how it is produced.

## Launch checklist

1. Merge `claude/eager-thompson-uemfso` into `main`.
2. GitHub: Settings -> Pages -> Deploy from a branch -> `main`, folder `/ (root)`. `.nojekyll` is in place.
3. Confirm https://peteinoz.github.io/emergency-plumber-gold-coast/ loads and a bad URL shows 404.html.
4. Google Search Console: add a URL-prefix property for the base URL and verify it (HTML tag in the
   head via `tools/build.py`, or an HTML file in the repo root).
5. Submit https://peteinoz.github.io/emergency-plumber-gold-coast/sitemap.xml in Search Console.
6. Spot-check Plumber, FAQPage, BreadcrumbList and BlogPosting schema in the Rich Results test.
7. When real photos and the logo are available, add them as described above and rebuild.

## Change log

- 2026-09-18: Repo scaffolded (CSS, JS, build and QA tooling, slug map, fetch helper, .nojekyll,
  .gitignore, project.md). Network to SOURCE and image hosts blocked; stopped for access.
- 2026-09-18: No-SOURCE build. 56 content modules written; generated brand assets; hero facts panels;
  inline SVG wordmark; video facade removed. Five rounds of copy rewrites to reach zero six-word
  overlap between pages; all meta descriptions trimmed to 155 characters; 32 short pages extended.
  Contrast and layout-shift fixes from Lighthouse. QA at zero failures.
