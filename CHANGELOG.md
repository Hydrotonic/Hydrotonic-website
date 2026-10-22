# Changelog

All notable changes to hydrotonic.org. Newest first.

## 2026-10-22: House rules, privacy and compliance

Applied the rules from Aatif's own website repository.

- Removed the full street address, building name and Google Maps link everywhere, including structured data. Location now reads "Belagavi, Karnataka".
- Added labelled Instagram and LinkedIn links to the top bar of every page.
- Switched to a more professional type pairing: Source Serif 4 for headings, Inter for body text.
- Added `privacy.html`, a Privacy Notice written for India's Digital Personal Data Protection Act, 2023, and linked it from the footer and the form.
- Added a required consent checkbox to the enquiry form.
- Instagram posts in the gallery now load only after the visitor clicks "Show Instagram posts", because Instagram sets cookies.
- Added a Content Security Policy to every page and moved all JavaScript into `assets/site.js` and `assets/theme.js`. CSS moved to `assets/site.css`.
- Added a canonical link, Open Graph and Twitter card tags, a skip link, `404.html`, `robots.txt` and `sitemap.xml`.
- Raised mobile tap targets to at least 44px, added image dimensions, and limited animation to transform and opacity.
- Added `AGENTS.md`, `CLAUDE.md`, this changelog and `scripts/check_site.py`.

## 2026-10-22: Redesign with dark mode

- Full redesign using the AgriCulture template as a reference only: top bar, full-width hero with fading photos, stats strip, numbered product cards, "Why Hydrotonic" section, services grid, "How it works" steps, FAQ and a full footer.
- Added a light and dark theme toggle that follows the visitor's device setting by default.
- Hero and About photos are Unsplash placeholders until Hydrotonic supplies its own.

## 2026-10-22: Enquiry form, gallery, FAQ and languages

- Added an enquiry form delivered by FormSubmit to hydrotonichydroponics@gmail.com (activated the same day).
- Added WhatsApp enquiry links on each product, an Instagram gallery, a 7-question FAQ, and a Kannada and Hindi language switch.

## 2026-10-22: First version

- Single-page site with products, services, about and contact sections, built from the business card, Instagram and LinkedIn.
- Published on GitHub Pages at hydrotonic.org with HTTPS enforced.
