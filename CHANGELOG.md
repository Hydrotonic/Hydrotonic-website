# Changelog

All notable changes to hydrotonic.org. Newest first.

## 2026-10-22: Story homepage, About and FAQ pages, olive palette

- Homepage rebuilt as a short story in three chapters: 01 who we are, 02 the tower (scroll animation) and how we install it, 03 what we sell. The install steps now follow the tower instead of sitting in a separate "How it works" section, and the separate Services grid is gone.
- New `about.html`: the company story, stats, the Instagram gallery and a founder section for Mohammed Daanish Mulla (UAS Dharwad, RAWE fieldwork, NSS 2024-25 special camp, founding Hydrotonic).
- New `faq.html` with all seven questions; the homepage links to it from Contact.
- Palette shifted from grey to olive green in both dark and light modes.
- Icons moved to one shared `assets/icons.svg`; the homepage no longer loads anything from Instagram.

## 2026-10-22: Pull-request workflow

- Added the "Site checks" GitHub Action, which runs `scripts/check_site.py` on every pull request and push to `main`.
- `AGENTS.md` now requires all changes to go through an approved pull request.

## 2026-10-22: Mobile-first redesign inspired by Verdant Robotics

- New look modelled on verdantrobotics.com: Montserrat throughout, near-black and deep teal surfaces with one green accent, gradient headline text, tag labels and pill buttons. Dark is now the default theme.
- Transparent header over the hero that turns solid on scroll; a full-screen menu on phones with language, theme, WhatsApp, Instagram and LinkedIn.
- Full-height hero with an aerial photo of Indian farmland and three highlights that become a swipeable rail on phones. Products also swipe on phones.
- New "Tower highlights" section: a line drawing of a hydroponic tower draws itself, its modules slide together, water fills and plants sprout as you scroll, with four captions (the Hydrotonic take on Verdant's scroll-driven hardware animation).
- Photos now match the hydroponic message instead of open-field farming: hydroponic lettuce channels in a polyhouse (hero), a net pot with roots hanging free (About), a grower with seedling trays in a shade-net nursery (Contact), and a close-up portrait of an Indian farmer in the "Made for India's growers" band.
- New full-width statement band with a parallax photo, and a "How it works" timeline that fills as you scroll.
- Fixed the enquiry form overflowing on phones.

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
