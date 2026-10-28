# hydrotonic.org

The website of Hydrotonic, a hydroponic tower systems business in Belagavi, Karnataka. Plain HTML, CSS and JavaScript, hosted on GitHub Pages at https://hydrotonic.org.

## Working on it

- Rules for every contributor and AI agent are in `AGENTS.md`. Read it first.
- Preview locally: `python -m http.server 8417` in this folder, then open http://127.0.0.1:8417/.
- Before a pull request: `python scripts/check_site.py`, and check the page at about 1440px and 375px in both themes.
- Every change goes through a pull request; the "Site checks" action must pass before it can merge.
- `CHANGELOG.md` lists what changed and when.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `faq.html`, `privacy.html`, `404.html` | The five pages |
| `assets/site.css`, `assets/site.js`, `assets/theme.js`, `assets/icons.svg` | Styles, behaviour and translations, pre-paint theme, icon sprite |
| `img/` | Photos, logos and icons |
| `scripts/check_site.py` | The checks the action runs |
| `scripts/gen_tower.py` | Generates the tower illustration SVG in `index.html` |
| `CNAME`, `sitemap.xml`, `robots.txt`, `manifest.webmanifest` | Hosting and discovery files |
