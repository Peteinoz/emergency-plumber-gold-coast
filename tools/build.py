#!/usr/bin/env python3
"""Stamp the shared shell into every page and write finished HTML.

Usage:  python3 tools/build.py            (writes every page, 404.html, sitemap.xml)

Content lives in tools/content/*.py. Each module defines a dict named `page`:

    page = dict(
        slug="blocked-drains",        # "" for the home page; one level deep only
        kind="service",               # home | core | hub | service | suburb | post
        title="...",                  # <= 60 chars, unique
        description="...",            # <= 155 chars, unique, ends with a prompt to call
        h1="...",
        eyebrow="Blocked drains",     # optional short label above the H1
        intro="<p>40-60 word answer-first intro</p>",
        hero=dict(src="images/x.webp", alt="...", w=900, h=600),   # optional
        og_image="images/og/x.jpg",   # 1200x630 local crop, path relative to repo root
        body="<section class=\"section\">...</section>",  # use {rel} for the path prefix
        faqs=[("Question?", "<p>Answer html</p>"), ...],   # 3-5 per page
        related=[("blocked-drains", "Blocked drain plumber"), ...],  # slugs, "" = home
        breadcrumb=[("all-services-available", "Services")],        # parent chain
        service=dict(name="Blocked drain clearing", type="Plumber", area="Gold Coast"),  # service/suburb pages
        post=dict(published="2026-09-18", modified="2026-09-18", image="images/x.webp"),  # blog posts
        lastmod="2026-09-18",
        noindex=False,
    )

The body copy must contain exactly one contextual link to the main site and
exactly one link back to home (`{rel}`); tools/qa.py checks both.
"""
import html
import importlib.util
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "tools" / "content"
BASE = "https://peteinoz.github.io/emergency-plumber-gold-coast/"
MAIN_SITE = "https://www.moyleplumbing.com.au/"

NAME = "Moyle Plumbing & Gasfitting"
STREET = "8 Belair Drive"
LOCALITY = "Yatala"
REGION = "QLD"
POSTCODE = "4207"
PHONE_DISPLAY = "(07) 3807 7327"
PHONE_TEL = "+61738077327"
EMAIL = "admin@moyleplumbing.com.au"
QBCC = "1077154"
ABN = "77 105 255 534"
LOGO = "images/moyle-plumbing-gasfitting-logo.png"
DEFAULT_OG = "images/og/moyle-plumbing-gold-coast.jpg"
FAVICON = "images/favicon.ico"
MAP_EMBED = "https://www.google.com/maps?q=8+Belair+Drive+Yatala+QLD+4207&output=embed"

SAME_AS = [
    MAIN_SITE,
    "https://www.facebook.com/moyleplumbing.gasfitting/",
    "https://www.instagram.com/moyle_plumbing/",
    "https://twitter.com/moyleplumbing",
    "https://www.linkedin.com/company/moyle-plumbing-&-gasfitting",
    "https://www.yelp.com.au/biz/moyle-plumbing-and-gasfitting-yatala-2",
    "https://www.youtube.com/user/Cheryl63100",
]
AREA_SERVED = [
    "Gold Coast", "Northern Gold Coast", "Yatala", "Beenleigh", "Logan",
    "Brisbane Southside", "Coomera", "Helensvale", "Hope Island", "Pimpama", "Ormeau",
]

# Header nav: hubs carry the full lists, so keep this short.
NAV_SERVICES = [
    ("emergency-plumbing", "Emergency plumbing"),
    ("blocked-drains", "Blocked drains"),
    ("hot-water", "Hot water"),
    ("burst-pipe", "Burst pipes"),
    ("leak-repairs", "Leak detection"),
    ("gas-fitting", "Gas fitting"),
    ("toilets", "Toilets"),
    ("all-services-available", "All services"),
]
NAV_AREAS = [
    ("plumber-coomera", "Coomera"),
    ("plumber-helensvale", "Helensvale"),
    ("plumber-hope-island", "Hope Island"),
    ("plumber-pimpama", "Pimpama"),
    ("plumber-ormeau", "Ormeau"),
    ("plumber-beenleigh", "Beenleigh"),
    ("suburbs-serviced", "All suburbs"),
]
FOOTER_SERVICES = [
    ("emergency-plumbing", "Emergency plumbing"),
    ("blocked-drains", "Blocked drains"),
    ("hot-water", "Hot water systems"),
    ("burst-pipe", "Burst pipe repair"),
    ("gas-fitting", "Gas fitting"),
    ("leak-repairs", "Leak repairs"),
    ("all-services-available", "All services"),
]
FOOTER_COMPANY = [
    ("about-us", "About us"),
    ("suburbs-serviced", "Suburbs serviced"),
    ("handy-hints-blog", "Handy hints"),
    ("contact-us", "Contact"),
    ("environmental-green-plumbers", "Green plumbing"),
    ("products-and-brands", "Products and brands"),
]

PHONE_SVG = ('<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>')
MENU_SVG = ('<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>')
WORDMARK_SVG = (
    '<svg class="wordmark" viewBox="0 0 300 64" role="img" aria-label="Moyle Plumbing &amp; Gasfitting">'
    '<path fill="#009be4" d="M24 4 8 30a17 17 0 1 0 32 0z"/>'
    '<text x="52" y="30" font-family="system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-weight="800" font-size="27" fill="currentColor">Moyle Plumbing</text>'
    '<text x="53" y="54" font-family="system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-weight="700" font-size="16" letter-spacing="2" fill="#009be4">&amp; GASFITTING</text>'
    '</svg>')
PLAY_SVG = ('<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-2 14.5v-9l7 4.5z"/></svg>')


def esc(s):
    return html.escape(s, quote=True)


def href(rel, slug):
    return rel if slug == "" else f"{rel}{slug}/"


def url(slug):
    return BASE if slug == "" else f"{BASE}{slug}/"


def nav_list(rel, items):
    return "".join(f'<li><a href="{href(rel, s)}">{esc(t)}</a></li>' for s, t in items)


def header(rel):
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{rel}" aria-label="{esc(NAME)} home">{WORDMARK_SVG}</a>
    <button class="nav-btn" type="button" aria-expanded="false" aria-controls="site-nav">{MENU_SVG} Menu</button>
    <a class="btn btn-primary header-call" href="tel:{PHONE_TEL}">{PHONE_SVG}{PHONE_DISPLAY}</a>
    <nav id="site-nav" class="site-nav" aria-label="Main">
      <ul>
        <li><a href="{rel}">Home</a></li>
        <li><a href="{href(rel, "all-services-available")}">Services</a>
          <ul class="sub">{nav_list(rel, NAV_SERVICES)}</ul></li>
        <li><a href="{href(rel, "suburbs-serviced")}">Service Areas</a>
          <ul class="sub">{nav_list(rel, NAV_AREAS)}</ul></li>
        <li><a href="{href(rel, "handy-hints-blog")}">Handy Hints</a></li>
        <li><a href="{href(rel, "about-us")}">About</a></li>
        <li><a href="{href(rel, "contact-us")}">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
'''


def footer(rel):
    year = date.today().year
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-logo">{WORDMARK_SVG}</div>
      <address>{esc(NAME)}<br>{STREET}, {LOCALITY} {REGION} {POSTCODE}<br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></address>
      <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>QBCC licence {QBCC}<br>ABN {ABN}</p>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{nav_list(rel, FOOTER_SERVICES)}</ul>
    </div>
    <div>
      <h2>Company</h2>
      <ul>{nav_list(rel, FOOTER_COMPANY)}</ul>
    </div>
  </div>
  <div class="wrap legal"><p>&copy; {year} {esc(NAME)}. Licensed plumbers and gasfitters based in Yatala, serving the northern Gold Coast, Beenleigh, Logan and Brisbane's southside.</p></div>
</footer>
<div class="call-bar"><a href="tel:{PHONE_TEL}">{PHONE_SVG}Call {PHONE_DISPLAY}</a></div>
'''


def breadcrumbs(rel, page):
    if page["slug"] == "":
        return ""
    chain = [("", "Home")] + list(page.get("breadcrumb", [])) + [(page["slug"], page.get("crumb", page["h1"]))]
    items = []
    for i, (slug, label) in enumerate(chain):
        if i == len(chain) - 1:
            items.append(f'<li aria-current="page">{esc(label)}</li>')
        else:
            items.append(f'<li><a href="{href(rel, slug)}">{esc(label)}</a></li>')
    return f'<nav class="breadcrumbs wrap" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>\n'


DEFAULT_CHIPS = {
    "home": ["Family owned and run since 1983", "Based at Yatala, northern Gold Coast", "Licensed and insured plumbers and gasfitters", "Price agreed before work starts"],
    "service": ["Licensed and insured", "Upfront set pricing", "Work area left clean", "Family business since 1983"],
    "suburb": ["Yatala-based, local to you", "Same-day aim for genuine emergencies", "QBCC licence 1077154", "Price known before work starts"],
    "hub": ["Domestic, commercial and real estate work", "Licensed plumbers and gasfitters", "Serving the northern Gold Coast, Logan and Brisbane southside"],
    "post": ["Written by a licensed plumbing trade", "Practical steps, no sales pitch", "Call if it cannot wait"],
    "core": ["Family owned and operated", "Trading since 1983", "Licensed and insured", "QBCC licence 1077154"],
}


def hero(rel, page):
    img = ""
    h = page.get("hero")
    if h:
        img = (f'<img src="{rel}{h["src"]}" alt="{esc(h["alt"])}" width="{h["w"]}" height="{h["h"]}" '
               f'fetchpriority="high" decoding="async">')
    else:
        chips = page.get("chips") or DEFAULT_CHIPS.get(page.get("kind", "core"), DEFAULT_CHIPS["core"])
        items = "".join(f"<li>{esc(c)}</li>" for c in chips)
        img = f'<div class="hero-panel" aria-label="Key facts"><ul class="checks">{items}</ul></div>'
    eyebrow = f'<span class="eyebrow">{esc(page["eyebrow"])}</span>' if page.get("eyebrow") else ""
    intro = page["intro"].replace("{rel}", rel)
    return f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      {eyebrow}
      <h1>{esc(page["h1"])}</h1>
      {intro}
      <div class="cta-row">
        <a class="btn btn-primary" href="tel:{PHONE_TEL}">{PHONE_SVG}Call {PHONE_DISPLAY}</a>
        <a class="btn btn-outline" href="mailto:{EMAIL}">Email {EMAIL}</a>
      </div>
    </div>
    {img}
  </div>
</section>
'''


def faqs_html(page, rel):
    faqs = page.get("faqs") or []
    if not faqs:
        return ""
    items = "".join(
        f'<details><summary>{esc(q)}</summary><div class="answer">{a.replace("{rel}", rel)}</div></details>' for q, a in faqs
    )
    return f'<section class="section faqs wrap"><h2 class="faq-heading">{esc(page.get("faq_heading", "Frequently asked questions"))}</h2>{items}</section>\n'


def related_html(rel, page):
    rel_links = page.get("related") or []
    if not rel_links:
        return ""
    items = nav_list(rel, rel_links)
    return f'<section class="section related wrap"><h2>{esc(page.get("related_heading", "Related pages"))}</h2><ul class="link-grid">{items}</ul></section>\n'


def map_html():
    return (f'<div class="map"><iframe src="{MAP_EMBED}" loading="lazy" title="Map showing {esc(NAME)} at {STREET}, {LOCALITY}" '
            f'referrerpolicy="no-referrer-when-downgrade"></iframe></div>')


def video_facade(rel, video_id, thumb, title):
    return (f'<div class="video" data-video-id="{esc(video_id)}" data-video-title="{esc(title)}">'
            f'<img src="{rel}{thumb["src"]}" alt="{esc(thumb["alt"])}" width="{thumb["w"]}" height="{thumb["h"]}" loading="lazy">'
            f'<button class="video-btn" type="button" aria-label="Play video: {esc(title)}">{PLAY_SVG}<span>Play video</span></button></div>'
            f'<p class="video-fallback"><noscript>Enable JavaScript to play the video here, or watch it on '
            f'<a href="https://www.youtube-nocookie.com/embed/{esc(video_id)}">YouTube</a>.</noscript></p>')


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def business_node():
    return {
        "@type": "Plumber",
        "@id": BASE + "#business",
        "name": NAME,
        "url": BASE,
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "logo": BASE + LOGO,
        "image": BASE + DEFAULT_OG,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": LOCALITY,
            "addressRegion": REGION,
            "postalCode": POSTCODE,
            "addressCountry": "AU",
        },
        "areaServed": [{"@type": "Place", "name": a} for a in AREA_SERVED],
        "sameAs": SAME_AS,
    }


def json_ld(page):
    graph = [business_node()]
    slug = page["slug"]
    if slug == "":
        graph.append({
            "@type": "WebSite",
            "@id": BASE + "#website",
            "url": BASE,
            "name": NAME,
            "publisher": {"@id": BASE + "#business"},
            "inLanguage": "en-AU",
        })
    else:
        chain = [("", "Home")] + list(page.get("breadcrumb", [])) + [(slug, page.get("crumb", page["h1"]))]
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": label, "item": url(s)}
                for i, (s, label) in enumerate(chain)
            ],
        })
    svc = page.get("service")
    if svc:
        node = {
            "@type": "Service",
            "name": svc["name"],
            "serviceType": svc.get("type", svc["name"]),
            "provider": {"@id": BASE + "#business"},
            "areaServed": {"@type": "Place", "name": svc.get("area", "Gold Coast")},
            "url": url(slug),
        }
        if svc.get("description"):
            node["description"] = svc["description"]
        graph.append(node)
    if page.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in page["faqs"]
            ],
        })
    post = page.get("post")
    if post:
        graph.append({
            "@type": "BlogPosting",
            "headline": page["h1"],
            "description": page["description"],
            "url": url(slug),
            "mainEntityOfPage": url(slug),
            "datePublished": post["published"],
            "dateModified": post.get("modified", post["published"]),
            "image": BASE + post.get("image", page.get("og_image", DEFAULT_OG)),
            "author": {"@id": BASE + "#business"},
            "publisher": {"@id": BASE + "#business"},
            "inLanguage": "en-AU",
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def render(page, rel=None, base_tag=False):
    slug = page["slug"]
    if rel is None:
        rel = "" if slug == "" else "../"
    canonical = url(slug)
    og_image = BASE + page.get("og_image", DEFAULT_OG)
    og_type = "article" if page.get("post") else "website"
    robots = '<meta name="robots" content="noindex, nofollow">\n' if page.get("noindex") else ""
    base = f'<base href="{BASE}">\n' if base_tag else ""
    canon = "" if page.get("noindex") else f'<link rel="canonical" href="{canonical}">\n'
    body = page["body"].replace("{rel}", rel)
    if "{map}" in body:
        body = body.replace("{map}", map_html())
    ld = json_ld(page)
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="zCM2Hs8gUAZDjbd2SdaIh0PQSo5cY-tW3ou9S0zFXtc">
<meta name="msvalidate.01" content="B1D866BAAB10788C4CF54CD6B53EEB99">
{base}<title>{esc(page["title"])}</title>
<meta name="description" content="{esc(page["description"])}">
{robots}{canon}<meta property="og:title" content="{esc(page["title"])}">
<meta property="og:description" content="{esc(page["description"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c1836">
<link rel="icon" href="{rel}{FAVICON}" sizes="any">
<link rel="apple-touch-icon" href="{rel}images/apple-touch-icon.png">
<link rel="stylesheet" href="{rel}css/style.css">
<script>document.documentElement.classList.add('js')</script>
<script src="{rel}js/main.js" defer></script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(rel)}<main id="main">
{breadcrumbs(rel, page)}{hero(rel, page)}{body}
{faqs_html(page, rel)}{related_html(rel, page)}</main>
{footer(rel)}</body>
</html>
'''


def load_pages():
    pages = []
    if str(CONTENT) not in sys.path:
        sys.path.insert(0, str(CONTENT))
    for f in sorted(CONTENT.glob("*.py")):
        if f.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        page = getattr(mod, "page")
        page.setdefault("lastmod", date.today().isoformat())
        pages.append(page)
    return pages


def sitemap(pages):
    entries = []
    for p in sorted(pages, key=lambda p: (p["slug"] != "", p["slug"])):
        if p.get("noindex"):
            continue
        entries.append(f"  <url>\n    <loc>{url(p['slug'])}</loc>\n    <lastmod>{p['lastmod']}</lastmod>\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + "\n</urlset>\n")


def image_size(path):
    try:
        from PIL import Image
        with Image.open(ROOT / path) as im:
            return im.size
    except Exception:
        return (180, 60)


def main():
    pages = load_pages()
    slugs = set()
    for p in pages:
        assert p["slug"] not in slugs, f"duplicate slug {p['slug']}"
        slugs.add(p["slug"])
        out = ROOT / "index.html" if p["slug"] == "" else ROOT / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        html_text = render(p)
        out.write_text(html_text, encoding="utf-8")
    # 404: served at any depth, so it uses a <base> tag and noindex.
    nf = {
        "slug": "404",
        "kind": "core",
        "title": "Page not found | Moyle Plumbing & Gasfitting",
        "description": "That page isn't here. Head back to the home page or call Moyle Plumbing & Gasfitting on (07) 3807 7327.",
        "h1": "That page isn't here",
        "intro": "<p>The link you followed may be old, or the address may have a typo in it. Use the menu above, head back to the <a href=\"{rel}\">home page</a>, or ring us if you need a plumber now.</p>",
        "body": "<section class=\"section wrap prose\"><h2>Popular pages</h2><ul class=\"link-grid\">" + nav_list("{rel}", NAV_SERVICES + [(s, t) for s, t in NAV_AREAS if s != "suburbs-serviced"] + [("suburbs-serviced", "All suburbs"), ("contact-us", "Contact us")]) + "</ul></section>",
        "noindex": True,
    }
    nf_html = render(nf, rel="", base_tag=True)
    (ROOT / "404.html").write_text(nf_html, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(pages), encoding="utf-8")
    print(f"built {len(pages)} pages + 404.html + sitemap.xml")


if __name__ == "__main__":
    main()
