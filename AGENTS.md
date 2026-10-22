# Hydrotonic website: rules for every contributor and AI agent

Claude Code, Codex and people follow the same rules here. Modelled on the rules in `Aatif_Junaid-Website`.

## How the site works

- Plain HTML, CSS and vanilla JavaScript. No build step, no framework, no npm.
- `index.html` (home), `privacy.html` (Privacy Notice), `404.html`. Shared styles in `assets/site.css`, behaviour in `assets/site.js`, pre-paint theme in `assets/theme.js`.
- Hosted on GitHub Pages from `main` at https://hydrotonic.org. Never delete `CNAME`; GitHub created it and the custom domain depends on it.
- When `site.css`, `site.js` or `theme.js` changes, bump the `?v=` number on every page so browsers fetch the new file.

## Before every push

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
- Third-party embeds that set cookies (Instagram) load only after the visitor clicks.
- Keep the Content Security Policy meta tag on every page. No inline JavaScript or `on...=` handlers; JSON-LD is the only inline script. Add a new external domain to the CSP only when a feature needs it.
- Every `target="_blank"` link has `rel="noopener"`.
- Never commit passwords, tokens or the brother's private details.

## Design

- Visual reference: verdantrobotics.com (aesthetic only; never copy its assets, copy or code). Calm dark teal and near-black surfaces, one green accent (`#4db748`), gradient headline text, small tag labels above headings, pill buttons.
- Mobile first: about 4 in 5 visitors use a phone. Design and review at 375px before desktop. Swipeable rails on phones, a full-screen `<dialog>` menu, and every tap target at least 44px.
- Font: Montserrat (400, 500, 600) only.
- Dark is the default theme; light is opt-in through the theme button. Colours come from the CSS variables in `assets/site.css`, and both themes must work.
- Photos must match what Hydrotonic sells: hydroponics and protected growing (towers, channels, net pots, roots, nurseries) lead. India and farmers appear as people and context (a portrait, a nursery), never as open-field cultivation, which would contradict the vertical-growing message. Never place a stock portrait next to the founder's name. Prefer Hydrotonic's own photos; Unsplash is the fallback and is credited in the footer.
- Animate only `transform` and `opacity`, never `transition: all`, and keep `prefers-reduced-motion` support. The one exception is the tower line drawing in "Tower highlights", which sets `stroke-dashoffset` from scroll position.
- Every image has alt text (or `alt=""` if decorative) and width and height attributes.

AI-authored commit messages end with a `Co-Authored-By:` line for the agent.
