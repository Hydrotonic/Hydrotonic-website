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

- Fonts: Source Serif 4 (600) for headings, Inter (400, 500, 600) for everything else.
- Colours come from the CSS variables in `assets/site.css`; light and dark themes must both work.
- Animate only `transform` and `opacity`, never `transition: all`, and keep `prefers-reduced-motion` support.
- Every image has alt text (or `alt=""` if decorative) and width and height attributes.

AI-authored commit messages end with a `Co-Authored-By:` line for the agent.
