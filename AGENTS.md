# Hydrotonic website: rules for every contributor and AI agent

Claude Code, Codex and people follow the same rules here. Modelled on the rules in `Aatif_Junaid-Website`.

## How the site works

- Plain HTML, CSS and vanilla JavaScript. No build step, no framework, no npm.
- `index.html` (home), `about.html` (company and founder), `faq.html`, `privacy.html` (Privacy Notice), `404.html`. Shared styles in `assets/site.css`, behaviour in `assets/site.js`, pre-paint theme in `assets/theme.js`, icons in `assets/icons.svg`.
- Hosted on GitHub Pages from `main` at https://hydrotonic.org. Never delete `CNAME`; GitHub created it and the custom domain depends on it.
- When `site.css`, `site.js` or `theme.js` changes, bump the `?v=` number on every page so browsers fetch the new file. Asset paths start with `/` so they work from every page.

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
- Every visible string has a `data-i18n` key with Kannada (`kn`) and Hindi (`hi`) entries in `assets/site.js`. Translations need a native speaker's review.

## Privacy and compliance

- Never publish the full street address, building name or a map pin. Location is "Belagavi, Karnataka" only.
- Instagram and LinkedIn stay labelled in the top bar of every page.
- The enquiry form keeps its required consent checkbox and the link to the Privacy Notice. If data handling changes (new form tool, analytics, cookies), update `privacy.html` first.
- The site loads no third-party embeds. If one is ever added and it sets cookies (for example Instagram), it must load only after the visitor clicks, and `privacy.html` must say so.
- Keep the Content Security Policy meta tag on every page. No inline JavaScript or `on...=` handlers; JSON-LD is the only inline script. Add a new external domain to the CSP only when a feature needs it.
- Every `target="_blank"` link has `rel="noopener"`.
- Never commit passwords, tokens or the brother's private details.

## Design

- Visual reference: verdantrobotics.com (aesthetic only; never copy its assets, copy or code). Calm olive-green surfaces, one green accent (`#7cc457` in dark mode, `#4a8a2a` in light), gradient headline text, small tag labels above headings, pill buttons.
- Mobile first: about 4 in 5 visitors use a phone. Design and review at 375px before desktop. Swipeable rails on phones, a full-screen `<dialog>` menu, and every tap target at least 44px.
- Font: Montserrat (400, 500, 600) only.
- The homepage tells one story in three short chapters: 01 who we are, 02 the tower and how we install it, 03 what we sell. Keep it short; longer content belongs on About or FAQ.
- Palette is olive green, not grey. Dark is the default theme; light is opt-in through the theme button. Colours come from the CSS variables in `assets/site.css`, and both themes must work.
- Use Hydrotonic's own photos first (in `img/`). The founder does not want his tower design copied: prefer close-ups of plants, roots and net pots, and lush towers where leaves hide the build. Wide shots that show the full plumbing or frame layout may only appear blurred behind text. The one exception, at the owner's request, is the About hero: the covered farm with the towers in focus. Never use photos or video that show other people's faces without their consent.
- The homepage hero is one clean stock photo of leafy greens growing hydroponically (the owner's choice: his own terrace shots read as cluttered). Keep it uncluttered and free of other companies' logos. Other stock tower photos are cropped to leaves only (no bases, plumbing, frames, roofs or logos).
- Logo files live in `img/`: `logo-mark-light.png` and `logo-mark-navy.png` (mark only, header), `logo-light.png` and `logo-navy.png` (mark with HYDROTONIC below), `favicon.png`. Use the light version on dark surfaces and the navy version on light ones. `logo.jpg` is the original banner crop used by the owner's GitHub profile README; keep it.
- Wherever the founder's B.Sc. (Hons.) is mentioned, show the UAS Dharwad emblem (`img/uas-dharwad.png`) as a stamp or badge, never on top of his photo. It marks where he studied, not an endorsement of Hydrotonic, so never word it as one.
- Photos must match what Hydrotonic sells: hydroponics and protected growing (towers, channels, net pots, roots, nurseries) lead. India and farmers appear as people and context (a portrait, a nursery), never as open-field cultivation, which would contradict the vertical-growing message. Never place a stock portrait next to the founder's name. Prefer Hydrotonic's own photos; Unsplash is the fallback and is credited in the footer.
- Photo treatment: a sharp, softly glowing centre, blurred edges and a light vignette (`about-wide.jpg`, `greens-wide.jpg`). Never darken the whole frame; the overlay only darkens where text sits.
- Animate only `transform` and `opacity`, never `transition: all`, and keep `prefers-reduced-motion` support. The one exception is the tower line drawing in "Tower highlights", which sets `stroke-dashoffset` from scroll position.
- Every image has alt text (or `alt=""` if decorative) and width and height attributes.

AI-authored commit messages end with a `Co-Authored-By:` line for the agent.
