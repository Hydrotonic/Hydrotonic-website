#!/usr/bin/env python3
"""Static checks for hydrotonic.org. Standard library only.

Run:  python scripts/check_site.py     Exit 0 = pass, 1 = failures.
Guards the house rules in AGENTS.md: no em dashes, no buzzwords, no street
address, socials upfront, CSP on every page, noopener, complete translations.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ["index.html", "about.html", "faq.html", "privacy.html", "404.html"]
failures = []

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def visible(s):
    s = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", s)

pages = {p: read(p) for p in PAGES}
js = read("assets/site.js")

for p, s in pages.items():
    text = visible(s)
    if "—" in text: failures.append(f"{p}: em dash in copy")
    for w in ["delve", "unlock", "unleash", "elevate", "transform", "synergy", "game-chang", "skyrocket"]:
        if w in text.lower(): failures.append(f"{p}: buzzword '{w}'")
    for leak in ["Raj Mahal", "1213", "Shahwaliullah", "Vaibhav", "590010", "google.com/maps"]:
        if leak in s: failures.append(f"{p}: street address detail '{leak}' published")
    if 'http-equiv="Content-Security-Policy"' not in s: failures.append(f"{p}: missing CSP meta")
    if len(re.findall(r"<h1\b", s)) != 1: failures.append(f"{p}: expected exactly one <h1>")
    if re.search(r"\son[a-z]+\s*=", s, re.I): failures.append(f"{p}: inline event handler")
    inline = re.findall(r'<script(?![^>]*\b(?:src|type="application/ld\+json"))[^>]*>\s*\S', s)
    if inline: failures.append(f"{p}: inline executable script")
    top = s.split("<header", 1)[0]
    if "instagram.com/hydrotonic.in" not in top or "linkedin.com/company/hydrotonic" not in top:
        failures.append(f"{p}: Instagram and LinkedIn must be in the top bar")
    for a in re.findall(r"<a\b[^>]*>", s):
        if 'target="_blank"' in a and "noopener" not in a: failures.append(f"{p}: target=_blank without noopener")
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    for anchor in re.findall(r'href="#([^"]+)"', s):
        if anchor not in ids: failures.append(f"{p}: anchor #{anchor} has no target")

if "—" in js: failures.append("assets/site.js: em dash in translations")

# Every data-i18n key used on a page has a Kannada and a Hindi entry.
keys = set()
for s in pages.values(): keys |= set(re.findall(r'data-i18n="([^"]+)"', s))
for lang in ["kn", "hi"]:
    block = re.search(lang + r":\s*\{(.*?)\n  \}", js, re.S)
    have = set(re.findall(r"(\w+):\s*'", block.group(1))) if block else set()
    missing = sorted(keys - have)
    if missing: failures.append(f"assets/site.js: {lang} missing {missing}")

# Cache-busters must match across pages.
versions = set()
for s in pages.values(): versions |= set(re.findall(r"assets/(?:site\.css|site\.js|theme\.js)\?v=(\d+)", s))
if len(versions) != 1: failures.append(f"asset ?v= numbers differ across pages: {sorted(versions)}")

if read("CNAME").strip() != "hydrotonic.org": failures.append("CNAME changed")

if failures:
    print("\n".join(f"FAIL  {f}" for f in failures))
    sys.exit(1)
print("All checks passed.")
