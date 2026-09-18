# Project notes: Moyle Plumbing & Gasfitting, emergency plumber Gold Coast site

Static site for GitHub Pages. Base URL: https://peteinoz.github.io/emergency-plumber-gold-coast/
This file is build facts only. It is excluded from sitemap.xml.

## Current state (updated 2026-09-18)

**Status: blocked on network access. No pages, copy or images have been produced yet.**

The session's egress policy refuses every host the brief needs (section 3 says stop rather than
fall back to placeholders, so the build stopped here):

| Host | Needed for | Result |
| --- | --- | --- |
| www.moyleplumbing.com.au | SOURCE pages, sitemap.xml, hours check | 403 from egress proxy (curl and WebFetch) |
| images.squarespace-cdn.com | logo, favicon, all business photos | 403 |
| i.imgur.com | inner-page photos | 403 |
| i.ytimg.com / img.youtube.com | thumbnail for the click-to-load video facade | 403 |

Only github.com is reachable.

### Built so far (network-independent groundwork)

- `css/style.css` (about 13 KB): mobile-first layout, brand colours, header with click-to-call,
  CSS-only dropdown nav on desktop, sticky mobile call bar, hero, cards, FAQ `<details>`,
  breadcrumbs, map and video-facade boxes, footer, focus states, print styles.
- `js/main.js` (about 1.2 KB, deferred): mobile nav toggle and YouTube facade only. Without JS the
  nav renders expanded and the video shows a `<noscript>` link.
- `tools/build.py`: stamps the shared header, hero, FAQs, related links, footer and JSON-LD into every
  page from `tools/content/*.py`, writes `/slug/index.html`, `404.html` (with `<base>` and noindex)
  and `sitemap.xml`. Schema per page kind: Plumber (all), WebSite (home), BreadcrumbList (inner),
  Service (service and suburb pages), FAQPage (pages with FAQs), BlogPosting (posts).
- `tools/qa.py`: all ten section-13 checks plus hours-claim, mobile-number and PO Box guards, image
  alt/size attributes, meta completeness, word-count guide, JSON-LD banned properties.
- `tools/fetch_source.py` and `tools/slugmap.py`: SOURCE research helper (sitemap listing, page text
  for the originality check, image manifest). Output folders are gitignored so no SOURCE text ever
  enters the repo.
- `.nojekyll`, `.gitignore`, this file.

Build and QA were smoke-tested in a scratch folder with two throwaway pages and generated
placeholder images; none of that was committed.

### Not yet done

Everything that depends on the SOURCE or its images: reading the SOURCE pages, confirming the sitemap
and blog inventory, checking the emergency page for stated hours, downloading and converting images,
writing all page copy, building, QA, originality check, Lighthouse pass.

## Questions for Pete (answer in one reply; the build then runs without stopping)

1. **Network.** Please allow www.moyleplumbing.com.au, images.squarespace-cdn.com, i.imgur.com and
   i.ytimg.com in this environment's network policy, then re-run. If the policy can't change, the
   alternative is to paste the SOURCE page text and sitemap into the conversation and attach the
   image files (logo, footer logo, favicon, business photos) to the repo on a branch I can read.
2. **Images without network.** If only the SOURCE pages can be opened but not the image CDN, do you
   want the build to go ahead with the pages and leave image slots to fill later, or wait for the
   assets? The brief forbids placeholders, so the default is to wait.

Hours: already answered. Only hours the SOURCE itself states will be used; no 24/7 claim otherwise.

## Assumptions made (say if any is wrong)

- The footer shows the email address under the NAP block alongside the QBCC licence and ABN.
- BlogPosting `datePublished` will be the date each article is published on this site, not the SOURCE
  post date, because the articles are new pieces.
- The `blog` index page is kept only if the SOURCE /blog page resolves; otherwise dropped, per brief.
- Pages deploy from the root of `main`; work is committed on `claude/eager-thompson-uemfso` and needs
  merging to `main` before Pages is enabled.

## Page inventory and slug map (new slug <- SOURCE path)

Planned count: 53 nav pages + blog posts (3 known, to be confirmed from the SOURCE sitemap) = 56 so
far. Final count to be recorded after the sitemap is read.

Core (7): `/` <- /, `contact-us`, `about-us`, `environmental-green-plumbers`, `products-and-brands`,
`handy-hints-blog`, `blog` (kept only if it resolves on the SOURCE).

Services (23): `all-services-available`, `general-plumbing-maintenance` <-
/general-domestic-maintenance-emergency-plumbing-and-gas-fitting, `blocked-drains`, `hot-water`,
`hot-water-tempering-valves` <- /hot-water-system/tempering-valves, `emergency-plumbing`,
`commercial-plumbing`, `dishwasher-installations`, `gas-fitting` <- /gas, `leak-repairs`,
`prepurchase-plumbing-inspection`, `pumps`, `real-estate-property-manager`, `toilets`, `burst-pipe`,
`water-filter-installation`, `bathroom-modifications`, `suburbs-serviced`, `leaking-shower-repairs` <-
/shower-renovations, `bathroom-renovations` <- /bath-rennovations, `insinkerator`, `bbq-gas-bottle`,
`water-compliancy`.

Service areas (23, slugs unchanged): `blocked-drains-coomera`, `plumber-coomera`,
`plumber-eight-mile-plains`, `plumber-hope-island`, `plumber-pimpama`, `plumber-loganholme`,
`plumber-ormeau`, `plumber-rochedale-south`, `plumber-mount-cotton`, `emergency-plumber-beenleigh`,
`plumber-beenleigh`, `emergency-plumbers-helensvale`, `plumber-helensvale`,
`plumbing-services-alberton`, `plumber-shailer-park`, `blocked-drains-ormeau`,
`hot-water-repairs-brisbane-southside`, `hot-water-springwood`, `hot-water-system-logan`,
`hot-water-systems-brisbane-southside`, `hot-water-gold-coast`, `plumber-redland-bay`,
`yarrabilba-plumber`.

Blog posts (flat slugs): `frequently-asked-questions`, `helpful-tips-for-plumbing-emergencies`,
`electrolysis-in-copper-pipe`, plus any others in the SOURCE sitemap under /handy-hints-blog/ or /blog/.

Excluded: /testimonials/*, /search, cart, account and system URLs, the nav folders /services,
/service-areas and /about-us-1.

The same map lives in `tools/slugmap.py` and drives the fetch helper and originality check.

## How to build

```
python3 tools/build.py     # renders every page, 404.html and sitemap.xml
python3 tools/qa.py        # section-13 checks; exit code 1 on any failure
```

Content modules go in `tools/content/<slug>.py` (schema documented at the top of `tools/build.py`).
Body copy uses `{rel}` for the path prefix, `{map}` for the Google Maps embed (home and contact only)
and `{video}` for the YouTube facade. The committed HTML is the deliverable; the tools folder is
just how it is produced.

## Launch checklist

1. Merge the branch into `main`.
2. GitHub: Settings -> Pages -> Deploy from a branch -> `main`, folder `/ (root)`. `.nojekyll` is in place.
3. Confirm https://peteinoz.github.io/emergency-plumber-gold-coast/ loads and that a bad URL shows 404.html.
4. Google Search Console: add a URL-prefix property for the base URL above and verify it (HTML tag or
   file upload into the repo root).
5. Submit https://peteinoz.github.io/emergency-plumber-gold-coast/sitemap.xml in Search Console.
6. Spot-check the Plumber, FAQPage and BreadcrumbList schema in the Rich Results test.
7. Run Lighthouse on mobile for the home page and one service, suburb and blog page.

## Change log

- 2026-09-18: Repo scaffolded (CSS, JS, build and QA tooling, slug map, fetch helper, .nojekyll,
  .gitignore, project.md). Network to SOURCE and image hosts blocked; stopped for access.
