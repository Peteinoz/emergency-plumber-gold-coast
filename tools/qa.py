#!/usr/bin/env python3
"""QA checks from the build brief (section 13). Run after tools/build.py.

    python3 tools/qa.py            # exit 1 on any failure

SOURCE originality (check 9) needs plain-text copies of the SOURCE pages in
tools/source_text/<source-slug>.txt (kept out of the repo; see project.md).
It is skipped with a warning when that folder is absent.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://peteinoz.github.io/emergency-plumber-gold-coast/"
MAIN = "https://www.moyleplumbing.com.au/"
TARGET = "emergency plumber repair near me"
NAP = ["Moyle Plumbing &amp; Gasfitting", "8 Belair Drive, Yatala QLD 4207", "(07) 3807 7327"]
SOURCE_TEXT = ROOT / "tools" / "source_text"

sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

failures = []
warnings = []


def fail(msg):
    failures.append(msg)


def warn(msg):
    warnings.append(msg)


class Doc(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.links = []          # (href, in_main, in_sentence, context)
        self.assets = []         # src/href of images, css, js, icons
        self.h1 = []
        self.title = ""
        self.meta = {}
        self.canonical = ""
        self.ld = []
        self.text_main = []
        self.text_all = []
        self._cur = None
        self._in_ld = False
        self._in_title = False
        self._details_q = []
        self._in_summary = False
        self._in_footer = False
        self.footer_text = []
        self.faq_visible = []
        self._skip_depth = None

    def in_main(self):
        return "main" in self.stack

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append(tag)
        cls = a.get("class", "")
        if self._skip_depth is None and any(c in cls.split() for c in ("cta-row", "breadcrumbs", "related", "call-bar", "hero-panel", "faq-heading")):
            self._skip_depth = len(self.stack)
        if tag == "a" and a.get("href"):
            ctx = "".join(self.text_all[-3:])[-200:]
            self.links.append({"href": a["href"], "in_main": self.in_main(), "rel": a.get("rel", ""),
                               "in_nav": "nav" in self.stack, "in_footer": "footer" in self.stack,
                               "in_header": "header" in self.stack, "tag_ctx": list(self.stack[-4:]), "before": ctx})
        if tag == "img":
            self.assets.append(("img", a.get("src", "")))
            if "alt" not in a:
                fail(f"img without alt: {a.get('src')}")
            if not a.get("width") or not a.get("height"):
                fail(f"img without width/height: {a.get('src')}")
        if tag == "link" and a.get("rel") in ("stylesheet", "icon"):
            self.assets.append((a["rel"], a.get("href", "")))
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href", "")
        if tag == "script":
            if a.get("src"):
                self.assets.append(("script", a["src"]))
            if a.get("type") == "application/ld+json":
                self._in_ld = True
                self._cur = []
        if tag == "iframe":
            self.assets.append(("iframe", a.get("src", "")))
        if tag == "meta" and (a.get("name") or a.get("property")):
            self.meta[a.get("name") or a.get("property")] = a.get("content", "")
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._cur_h1 = []
        if tag == "summary":
            self._in_summary = True
            self._cur_summary = []

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self.ld.append("".join(self._cur))
            self._in_ld = False
            self._cur = None
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self.h1.append("".join(self._cur_h1).strip())
        if tag == "summary":
            self._in_summary = False
            self.faq_visible.append("".join(self._cur_summary).strip())
        while self.stack and self.stack[-1] != tag:
            self.stack.pop()
        if self.stack:
            self.stack.pop()
        if self._skip_depth is not None and len(self.stack) < self._skip_depth:
            self._skip_depth = None

    def handle_data(self, data):
        if self._in_ld:
            self._cur.append(data)
            return
        if self._in_title:
            self.title += data
        if "h1" in self.stack:
            self._cur_h1.append(data)
        if self._in_summary:
            self._cur_summary.append(data)
        self.text_all.append(data)
        if self.in_main() and self._skip_depth is None:
            self.text_main.append(data)
        if "footer" in self.stack:
            self.footer_text.append(data)


def parse(path):
    d = Doc()
    d.feed(path.read_text(encoding="utf-8"))
    return d


def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def shingles(text, n=6):
    w = words(text)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


ALLOWED_SHINGLE_PARTS = ["moyle plumbing", "8 belair drive", "yatala qld 4207", "07 3807 7327", "1077154", "77 105 255 534",
                         "plumbing gasfitting", "plumbing and gasfitting", "moyleplumbing com au",
                         "northern gold coast", "gold coast beenleigh logan", "beenleigh logan and brisbane"]


def main():
    pages = build.load_pages()
    slugs = {p["slug"] for p in pages}
    html_files = {}
    for p in pages:
        f = ROOT / "index.html" if p["slug"] == "" else ROOT / p["slug"] / "index.html"
        if not f.exists():
            fail(f"missing file for slug '{p['slug']}'")
        else:
            html_files[p["slug"]] = f
    # 1. page count and stray folders
    stray = [d.name for d in ROOT.iterdir() if d.is_dir() and (d / "index.html").exists() and d.name not in slugs]
    if stray:
        fail(f"folders with index.html not in inventory: {stray}")
    print(f"pages in content: {len(pages)}; html files: {len(html_files)}")

    titles, descs, h1s = {}, {}, {}
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8") if (ROOT / "sitemap.xml").exists() else ""
    sitemap_locs = set(re.findall(r"<loc>(.*?)</loc>", sitemap))
    page_text = {}

    for slug, f in html_files.items():
        d = parse(f)
        raw = f.read_text(encoding="utf-8")
        rel = "" if slug == "" else "../"
        label = f"/{slug}/" if slug else "/"

        # 2. NAP in footer
        footer_html = raw[raw.find("<footer"):raw.find("</footer>")]
        for line in NAP:
            if line not in footer_html:
                fail(f"{label}: NAP line missing from footer: {line}")
        if "tel:+61738077327" not in footer_html:
            fail(f"{label}: footer phone not linked to tel:+61738077327")
        for bad in ["PO Box", "0417", "04"]:
            pass
        if re.search(r"\b04\d{2}\s?\d{3}\s?\d{3}\b", raw):
            fail(f"{label}: a mobile number appears on the page")
        if re.search(r"\bPO Box\b", raw, re.I):
            fail(f"{label}: a PO Box appears on the page")

        # 3. exactly one contextual main-site link inside <main>
        main_links = [l for l in d.links if l["href"] == MAIN]
        domain_links = [l for l in d.links if "moyleplumbing.com.au" in l["href"] and not l["href"].startswith("mailto:")]
        if len(main_links) != 1:
            fail(f"{label}: expected 1 link to {MAIN}, found {len(main_links)}")
        else:
            l = main_links[0]
            if not l["in_main"] or l["in_nav"] or l["in_header"] or l["in_footer"]:
                fail(f"{label}: main-site link is not inside <main> body copy")
            if "nofollow" in l["rel"] or "sponsored" in l["rel"]:
                fail(f"{label}: main-site link carries rel={l['rel']}")
            if "p" not in l["tag_ctx"] and "li" not in l["tag_ctx"]:
                fail(f"{label}: main-site link is not inside a sentence (context {l['tag_ctx']})")
            if "button" in l["tag_ctx"] or any(c.startswith("btn") for c in l["tag_ctx"]):
                fail(f"{label}: main-site link looks like a button")
        if len(domain_links) != len(main_links):
            fail(f"{label}: extra links to moyleplumbing.com.au: {[l['href'] for l in domain_links if l['href'] != MAIN]}")
        if raw.count("moyleplumbing.com.au") - raw.count("admin@moyleplumbing.com.au") - 2 > 1:
            # 2 = JSON-LD sameAs + the one link
            warn(f"{label}: moyleplumbing.com.au appears more than expected in the markup")

        # home link in body copy
        body_home = [l for l in d.links if l["href"] == rel and l["in_main"] and not l["in_nav"]
                     and ("p" in l["tag_ctx"] or "li" in l["tag_ctx"])]
        if slug != "" and not body_home:
            fail(f"{label}: no link to home inside body copy")

        # 4. absolute/leading-slash paths and remote assets
        if re.search(r'(href|src)="/', raw):
            fail(f"{label}: leading-slash path found")
        for kind, src in d.assets:
            if kind == "iframe":
                if not src.startswith("https://www.google.com/maps"):
                    fail(f"{label}: unexpected iframe {src}")
                continue
            if src.startswith(("http://", "https://", "//")):
                fail(f"{label}: remote asset {src}")
            target = (f.parent / src).resolve()
            if not target.exists():
                fail(f"{label}: asset not found: {src}")
        if "@import" in raw or "fonts.googleapis" in raw:
            fail(f"{label}: external font or import")
        # BASE URL only in head/JSON-LD
        body_part = raw[raw.find("<body"):]
        body_no_ld = re.sub(r"<script type=\"application/ld\+json\">.*?</script>", "", body_part, flags=re.S)
        if BASE in body_no_ld and slug != "404":
            fail(f"{label}: BASE URL used in body markup")

        # 5. internal links resolve
        for l in d.links:
            h = l["href"]
            if h.startswith(("tel:", "mailto:", "#", "http://", "https://")):
                continue
            path = h.split("#")[0]
            target = (f.parent / path).resolve()
            if path.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                fail(f"{label}: broken internal link {h}")
            if not path.endswith("/") and not path.endswith(".html") and "." not in path.split("/")[-1]:
                fail(f"{label}: internal link without trailing slash: {h}")

        # 6. unique title/description/h1
        t = d.title.strip()
        desc = d.meta.get("description", "")
        if not t or len(t) > 60:
            fail(f"{label}: title missing or over 60 chars ({len(t)}): {t}")
        if not desc or len(desc) > 155:
            fail(f"{label}: meta description missing or over 155 chars ({len(desc)})")
        if not re.search(r"\b(call|ring|phone)\b", desc, re.I):
            fail(f"{label}: meta description has no prompt to call")
        if len(d.h1) != 1:
            fail(f"{label}: expected 1 H1, found {len(d.h1)}")
        for store, val, name in ((titles, t, "title"), (descs, desc, "description"), (h1s, d.h1[0] if d.h1 else "", "h1")):
            if val in store:
                fail(f"{label}: duplicate {name} shared with {store[val]}")
            store[val] = label
        for key in ("og:title", "og:description", "og:url", "og:type", "og:image", "twitter:card", "viewport"):
            if key not in d.meta:
                fail(f"{label}: missing meta {key}")

        # 7. JSON-LD parses; FAQ matches visible
        for block in d.ld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                fail(f"{label}: JSON-LD parse error: {e}")
                continue
            graph = data.get("@graph", [data])
            for node in graph:
                if node.get("@type") == "FAQPage":
                    schema_qs = [q["name"] for q in node["mainEntity"]]
                    if schema_qs != d.faq_visible:
                        fail(f"{label}: FAQ schema questions differ from visible FAQs")
                    schema_as = [q["acceptedAnswer"]["text"] for q in node["mainEntity"]]
                    page_faq = next(p for p in pages if p["slug"] == slug).get("faqs", [])
                    for (q, a), sa in zip(page_faq, schema_as):
                        if build.strip_tags(a) != sa:
                            fail(f"{label}: FAQ answer text differs from schema for '{q}'")
                if node.get("@type") == "Plumber":
                    addr = node["address"]
                    if (addr["streetAddress"], addr["addressLocality"], addr["addressRegion"], addr["postalCode"]) != ("8 Belair Drive", "Yatala", "QLD", "4207"):
                        fail(f"{label}: JSON-LD address does not match NAP")
                    if node.get("telephone") != "+61738077327":
                        fail(f"{label}: JSON-LD telephone mismatch")
                    for banned in ("geo", "aggregateRating", "review", "openingHours", "openingHoursSpecification"):
                        if banned in node:
                            fail(f"{label}: JSON-LD contains banned property {banned}")
            if slug != "":
                if not any(n.get("@type") == "BreadcrumbList" for n in graph):
                    fail(f"{label}: missing BreadcrumbList")
            else:
                if not any(n.get("@type") == "WebSite" for n in graph):
                    fail(f"{label}: home missing WebSite schema")
        if d.faq_visible and not any('"FAQPage"' in b for b in d.ld):
            fail(f"{label}: visible FAQs but no FAQPage schema")

        # 8. canonical, og:url, sitemap agree
        expected = BASE if slug == "" else f"{BASE}{slug}/"
        if d.canonical != expected:
            fail(f"{label}: canonical {d.canonical} != {expected}")
        if d.meta.get("og:url") != expected:
            fail(f"{label}: og:url mismatch")
        if expected not in sitemap_locs:
            fail(f"{label}: missing from sitemap.xml")

        # 10. target phrase only in home title/H1
        in_title_h1 = TARGET in (t + " " + " ".join(d.h1)).lower()
        if slug == "" and not in_title_h1:
            fail("home: target phrase missing from title/H1")
        if slug != "" and in_title_h1:
            fail(f"{label}: target phrase appears in title or H1 (only home may use it)")
        if slug == "":
            body_text = " ".join(d.text_main)
            first100 = " ".join(words(body_text)[:100])
            if TARGET not in first100:
                fail("home: target phrase not in first 100 words of main copy")
            if TARGET not in desc.lower():
                fail("home: target phrase not in meta description")
            if TARGET not in raw[raw.find("<h2"):].lower() or not re.search(r"<h2[^>]*>[^<]*" + re.escape(TARGET), raw, re.I):
                fail("home: target phrase not in an H2")
            if not re.search(r'alt="[^"]*' + re.escape(TARGET), raw, re.I):
                fail("home: target phrase not in an image alt")
            if raw.lower().count(TARGET) > 8:
                warn(f"home: target phrase appears {raw.lower().count(TARGET)} times; check for stuffing")

        # hours claims
        if re.search(r"\b24\s*/\s*7\b|24 hours|24-hour|around the clock", raw, re.I):
            fail(f"{label}: 24/7 or hours claim present (not confirmed by SOURCE)")

        page_text[slug] = " ".join(d.text_main)
        wc = len(words(page_text[slug]))
        page_obj = next(p for p in pages if p["slug"] == slug)
        limits = {"home": (1200, 1600), "service": (700, 1100), "suburb": (600, 900), "hub": (400, 700), "post": (800, 1200)}
        lo, hi = limits.get(page_obj["kind"], (150, 1600))
        if wc < lo or wc > hi:
            warn(f"{label}: {wc} words (guide {lo}-{hi})")

    # sitemap entries all point at real pages
    for loc in sitemap_locs:
        s = loc[len(BASE):].rstrip("/")
        if s not in html_files:
            fail(f"sitemap entry has no page: {loc}")

    # 9. originality between pages of this site
    def clean(sh):
        return {s for s in sh if not any(a in s for a in ALLOWED_SHINGLE_PARTS)}
    sh = {s: clean(shingles(t)) for s, t in page_text.items()}
    # strip shingles that come from the shared shell (hero CTA labels etc) by removing ones present in >3 pages
    common = {}
    for s, set_ in sh.items():
        for g in set_:
            common[g] = common.get(g, 0) + 1
    shell = {g for g, c in common.items() if c > 3}
    if shell:
        warn(f"{len(shell)} six-word shingles repeat on more than 3 pages (shared shell or repeated copy); sample: {sorted(shell)[:5]}")
    keys = sorted(sh)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            overlap = (sh[a] & sh[b]) - shell
            if overlap:
                fail(f"duplicate copy between /{a}/ and /{b}/: {sorted(overlap)[:3]}")
    if SOURCE_TEXT.exists():
        src_map = {}
        for p in pages:
            src = p.get("source")
            if src:
                src_map[p["slug"]] = src
        for slug, src in src_map.items():
            sf = SOURCE_TEXT / (src.strip("/").replace("/", "__") or "home")
            sf = sf.with_suffix(".txt")
            if not sf.exists():
                warn(f"no SOURCE text for /{slug}/ ({src})")
                continue
            overlap = clean(shingles(sf.read_text(encoding="utf-8"))) & sh.get(slug, set())
            if overlap:
                fail(f"/{slug}/ shares copy with SOURCE {src}: {sorted(overlap)[:3]}")
    else:
        warn("tools/source_text/ absent: SOURCE originality check skipped")

    # 404
    nf = ROOT / "404.html"
    if not nf.exists():
        fail("404.html missing")
    else:
        t404 = nf.read_text(encoding="utf-8")
        if f'<base href="{BASE}">' not in t404 or "noindex" not in t404:
            fail("404.html needs the base tag and noindex")
    if not (ROOT / ".nojekyll").exists():
        fail(".nojekyll missing")
    css = (ROOT / "css" / "style.css").stat().st_size
    js = (ROOT / "js" / "main.js").stat().st_size
    if css > 40 * 1024:
        warn(f"style.css is {css} bytes (target under 40 KB)")
    if js > 5 * 1024:
        warn(f"main.js is {js} bytes (target under 5 KB)")

    for w in warnings:
        print("WARN:", w)
    for f_ in failures:
        print("FAIL:", f_)
    print(f"{len(failures)} failures, {len(warnings)} warnings")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
