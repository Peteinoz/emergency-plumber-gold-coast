"""Helpers shared by content modules. Strings keep the literal {rel} token for build.py."""
MAIN = "https://www.moyleplumbing.com.au/"


def L(slug, text):
    """Internal link to /slug/ (relative)."""
    return f'<a href="{{rel}}{slug}/">{text}</a>'


def H(text):
    """Link to the home page."""
    return f'<a href="{{rel}}">{text}</a>'


def M(text):
    """The one contextual link to the main site."""
    return f'<a href="{MAIN}">{text}</a>'


PHONE = '<a href="tel:+61738077327">(07) 3807 7327</a>'
MAILTO = '<a href="mailto:admin@moyleplumbing.com.au">admin@moyleplumbing.com.au</a>'


def sec(inner, cls="section wrap prose"):
    return f'<section class="{cls}">{inner}</section>\n'


def soft(inner):
    return f'<section class="section-soft"><div class="wrap prose">{inner}</div></section>\n'


def navy(inner):
    return f'<section class="section-navy"><div class="wrap prose">{inner}</div></section>\n'


def callout(inner, warn=False):
    return f'<div class="callout{" warn" if warn else ""}">{inner}</div>'


def cards(items, cols=None):
    """items: list of (slug, heading, text)."""
    cls = "cards" + (f" cols-{cols}" if cols else "")
    out = "".join(f'<li class="card"><h3>{L(s, h)}</h3><p>{t}</p></li>' for s, h, t in items)
    return f'<ul class="{cls}">{out}</ul>'
