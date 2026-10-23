# Hydrotonic website: rules for every contributor and AI agent

Claude Code, Codex and people follow the same rules here. Modelled on the rules in `Aatif_Junaid-Website`.

## How the site works

- Plain HTML, CSS and vanilla JavaScript. No build step, no framework, no npm.
- `index.html` (home), `about.html` (company and founder), `faq.html`, `privacy.html` (Privacy Notice), `404.html`. Shared styles in `assets/site.css`, behaviour in `assets/site.js`, pre-paint theme in `assets/theme.js`, icons in `assets/icons.svg`.
- Hosted on GitHub Pages from `main` at https://hydrotonic.org. Never delete `CNAME`; GitHub created it and the custom domain depends on it.
- When `site.css`, `site.js` or `theme.js` changes, bump the `?v=` number on every page (including the `icons.svg` references) so browsers fetch the new file. Asset paths start with `/` so they work from every page.

## Changes go through pull requests

- `main` is protected. Never push to it directly: work on a branch and open a pull request. No approval is required (the ruleset sets required approvals to 0), so Aatif or the owner can merge once the "Site checks" job passes. Deletions and force pushes to `main` stay blocked.
- The "Site checks" GitHub Action (`.github/workflows/site-checks.yml`) runs `scripts/check_site.py` on every pull request and must pass. Keep its actions pinned to full commit SHAs and its permissions read-only.

## Before every pull request

1. Run `python scripts/check_site.py` and fix every failure.
2. Check the page in a browser near 1440px and 375px wide, in light and dark mode: no console errors, no horizontal scroll, every control at least 44px tall on mobile.
3. Add a dated entry to `CHANGELOG.md`.

## Copy rules

- No em dashes anywhere, including the Kannada and Hindi translations in `assets/site.js`.
- No empty buzzwords (delve, unlock, elevate, transform, synergy, game-changing, and similar).
- Every claim must be true and sourced from Hydrotonic's own card, Instagram or LinkedIn, or confirmed by the owner. No invented testimonials, prices or numbers.
- Every visible string has a `data-i18n` key with Kannada (`kn`), Hindi (`hi`) and Marathi (`mr`) entries in `assets/site.js`, one key per line in page order. Translations need a native speaker's review.
- In translations, keep WhatsApp, Instagram, UAS, RAWE and NSS as written in Hindi and Marathi; Kannada uses the transliterated app names. Write the brand in each script (ಹೈಡ್ರೋಟೋನಿಕ್, हाइड्रोटोनिक, हायड्रोटॉनिक) and the city as the official Belagavi (ಬೆಳಗಾವಿ, बेलगावी, बेळगावी). Name the university as "University of Agricultural Sciences, Dharwad" in full, the same way in every language.
- Kannada and Devanagari use Noto Sans Kannada and Noto Sans Devanagari (loaded with Montserrat; the browser fetches them only when those scripts are on screen). Those languages get taller line heights and no negative letter spacing; check that new strings fit at 360px.

## Privacy and compliance

- Never publish the full street address, building name or a map pin. Location is "Belagavi, Karnataka" only.
- Instagram and LinkedIn stay linked on every page (menu, contact section and footer). There is no top bar above the header; the owner removed it on 2026-10-23 for a cleaner look.
- The enquiry form keeps its required consent checkbox and the link to the Privacy Notice. If data handling changes (new form tool, analytics, cookies), update `privacy.html` first.
- The site loads no third-party embeds. If one is ever added and it sets cookies (for example Instagram), it must load only after the visitor clicks, and `privacy.html` must say so.
- Keep the Content Security Policy meta tag on every page. No inline JavaScript or `on...=` handlers; JSON-LD is the only inline script. Add a new external domain to the CSP only when a feature needs it.
- Every `target="_blank"` link has `rel="noopener"`.
- Never commit passwords, tokens or the brother's private details.

## Design

- Visual reference: verdantrobotics.com (aesthetic only; never copy its assets, copy or code). Calm olive-green surfaces, one green accent (`#7cc457` in dark mode, `#4a8a2a` in light), solid headings (no gradient text), pill buttons.
- Header: sentence case throughout (the name reads "Hydrotonic"). Links to sections of the homepage come first, then a thin divider, then links to other pages (About, FAQ) with a small arrow icon. "Get a quote" is the only filled button and sits at the far right, on phones too.
- Buttons: one filled primary style, `btn-brand` (green, from the `--cta` token), for the main action: Get a quote, Send enquiry, Back to the homepage. WhatsApp buttons in the page use the light pill (`btn-light`); secondary actions use outlines (`btn-outline` on photos, `btn-line` on surfaces). Only the floating WhatsApp button uses WhatsApp's own green. Use palette colours only; no stray greys or blues.
- Dropdowns (the language menu and form selects) open as a rounded panel in the site's colours via `appearance: base-select` where supported; elsewhere options must still be readable (surface background, strong text). The header logo mark is 46px tall on desktop and 34px on phones.
- Mobile first: about 4 in 5 visitors use a phone. Design and review at 375px before desktop. Swipeable rails on phones, a full-screen `<dialog>` menu, and every tap target at least 44px.
- Font: Montserrat (400, 500, 600) only.
- The homepage tells one story in order: who we are, the tower and how we install it, what we sell. Keep it short; longer content belongs on About or FAQ.
- Less is more, and it must not look template-made: no eyebrow tags above headings, no numbered sections or badges (01, 02...), and no subtext under every card or step. One heading per section, at most one short line under it, and let photos, icons and diagrams carry the message.
- Text on photos must stay readable in both themes: solid white with a soft shadow, over a dark overlay that sits behind the text itself. Never let an overlay fade into the page background where text sits.
- Palette is olive green, not grey. Dark is the default theme; light is opt-in through the theme button. Colours come from the CSS variables in `assets/site.css`, and both themes must work.
- Use Hydrotonic's own photos first (in `img/`). The founder does not want his tower design copied: prefer close-ups of plants, roots and net pots, and lush towers where leaves hide the build. Wide shots that show the full plumbing or frame layout may only appear blurred behind text. The one exception, at the owner's request, is the About hero: the covered farm with the towers in focus. Never use photos or video that show other people's faces without their consent.
- The homepage hero is one clean stock photo of leafy greens growing hydroponically (the owner's choice: his own terrace shots read as cluttered). Keep it uncluttered and free of other companies' logos. Other stock tower photos are cropped to leaves only (no bases, plumbing, frames, roofs or logos).
- Logo files live in `img/`: `logo-mark-light.png` and `logo-mark-navy.png` (mark only, header), `logo-light.png` and `logo-navy.png` (mark with HYDROTONIC below), `favicon.png`. Use the light version on dark surfaces and the navy version on light ones. `logo.jpg` is the original banner crop used by the owner's GitHub profile README; keep it. `og-banner.jpg` (the full brand banner, 2400x1260, kept under 300 KB for WhatsApp) is the link-preview image on every page; if it changes, give it a new filename so WhatsApp and others fetch it again.
- Wherever the founder's B.Sc. (Hons.) is mentioned, show the UAS Dharwad emblem (`img/uas-dharwad.png`) as a stamp or badge, never on top of his photo. It marks where he studied, not an endorsement of Hydrotonic, so never word it as one.
- Photos must match what Hydrotonic sells: hydroponics and protected growing (towers, channels, net pots, roots, nurseries) lead. India and farmers appear as people and context (a portrait, a nursery), never as open-field cultivation, which would contradict the vertical-growing message. Never place a stock portrait next to the founder's name. Prefer Hydrotonic's own photos; Unsplash is the fallback and is credited in the footer.
- Photo treatment: a sharp, softly glowing centre, blurred edges and a light vignette (`about-wide.jpg`, `greens-wide.jpg`). Never darken the whole frame; the overlay only darkens where text sits.
- Animate only `transform` and `opacity`, never `transition: all`, and keep `prefers-reduced-motion` support. The one exception is the tower illustration in "02 · The tower", which sets `stroke-dashoffset` from scroll position for its line drawing and water.
- The tower illustration shows Hydrotonic's real design, as in the logo and the owner's builds: three single-tube towers (the middle one tallest) with net-pot cups in several columns, caps and a header pipe on top, and one reservoir pipe at the base. The pump sits in the reservoir and lifts water up the centre of the middle tower, over to the side towers, and it trickles back down inside. Never draw stacked boxes or an outside riser pipe. The drawing completes one screen before the section unpins, so the last screen of scroll shows the finished tower with nothing changing; keep that hold if you change the section height. It is the only place that uses blue for water and yellow for the sun (`--water`, `--sun`, scoped to `.tower-art`). The SVG comes from `scripts/gen_tower.py`; change the script and paste its output rather than editing coordinates by hand.
- Every image has alt text (or `alt=""` if decorative) and width and height attributes.

AI-authored commit messages end with a `Co-Authored-By:` line for the agent.
