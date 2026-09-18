#!/usr/bin/env python3
"""Fetch the SOURCE site for research only. Nothing it saves is committed.

    python3 tools/fetch_source.py sitemap      # print every URL in the SOURCE sitemap
    python3 tools/fetch_source.py pages        # save plain text of each mapped SOURCE page
                                               #   to tools/source_text/<path>.txt (gitignored)
    python3 tools/fetch_source.py images       # write tools/source_images/manifest.json
                                               #   listing image URLs per SOURCE page

The text files feed the originality check in tools/qa.py (6-word shingles).
"""
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = "https://www.moyleplumbing.com.au"
sys.path.insert(0, str(ROOT / "tools"))
from slugmap import SLUG_MAP  # noqa: E402


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site research)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.images = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self._skip += 1
        if tag == "img":
            for k in ("src", "data-src", "data-image"):
                if a.get(k):
                    self.images.append({"url": a[k], "alt": a.get("alt", "")})
                    break

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sitemap"
    if cmd == "sitemap":
        xml = get(SOURCE + "/sitemap.xml").decode("utf-8", "replace")
        for loc in re.findall(r"<loc>(.*?)</loc>", xml):
            print(loc)
        return
    out_text = ROOT / "tools" / "source_text"
    out_html = ROOT / "tools" / "source_html"
    out_img = ROOT / "tools" / "source_images"
    manifest = {}
    for new_slug, src_path in SLUG_MAP.items():
        url = SOURCE + src_path
        try:
            raw = get(url).decode("utf-8", "replace")
        except Exception as e:
            print(f"FAILED {url}: {e}")
            continue
        p = Text()
        p.feed(raw)
        name = (src_path.strip("/").replace("/", "__") or "home")
        if cmd == "pages":
            out_text.mkdir(exist_ok=True)
            out_html.mkdir(exist_ok=True)
            (out_html / f"{name}.html").write_text(raw, encoding="utf-8")
            text = re.sub(r"\s+", " ", " ".join(p.parts))
            (out_text / f"{name}.txt").write_text(text, encoding="utf-8")
            print(f"saved {name}.txt ({len(text.split())} words)")
        if cmd == "images":
            manifest[new_slug] = [i for i in p.images if "shutterstock" not in i["url"].lower()]
            print(f"{new_slug}: {len(manifest[new_slug])} images")
    if cmd == "images":
        out_img.mkdir(exist_ok=True)
        (out_img / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
