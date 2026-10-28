# Changelog

All notable changes to hydrotonic.org. Newest first.

## 2026-10-28: Logo without the tile

- The light box behind the logo is gone. The transparent navy mark sits straight on the page; on dark surfaces a faint light halo keeps the towers readable, and in light mode it is plain.

## 2026-10-27: Visual pass

- Logo back to its banner colours (navy towers, green leaves, blue water) on a small light tile in the header, menu and footer, in both themes.
- Phones: a second header row with About and FAQ first, the section links, and the language and theme controls, so none of them hide in the menu. It folds away on scroll.
- Tower animation: rounded header pipe with a highlight, lettuce heads instead of flat leaves, small roots inside the tubes, and a pump and filter in the reservoir with labels (translated). Heads now fill in across the towers in a fixed random order rather than bottom to top.
- Products: the Inputs card is a line drawing of a net pot with cocopeat, a pump and nutrient bottles A and B; the Microgreens card pairs a microgreens tray with edible flowers (Unsplash).
- The farmer band is about a third shorter.
- About gallery: three new farm photos (lettuce head, spinach bunch, spinach with roots); the small tomato seedling photo is retired as a near duplicate.
- Email is now hydrotonic.org@gmail.com everywhere, including the enquiry form and structured data. Facebook added to the menu, contact panel, footer and structured data.

## 2026-10-23: The Tower

- The menu link now reads "The Tower", capitalised as the product's name, in the header, the phone menu and the footer.

## 2026-10-23: Mobile pass

- Lighter pages: the header logo was downloading about 350 KB (both colour versions, at desktop poster size) for a 46px mark; it is now 8 KB, and the version only used in light mode loads only when needed. The footer logo went from 195 KB to 25 KB and the UAS emblem from 224 KB to 29 KB, with no visible difference. The phone hero photo is 242 KB instead of 318 KB and is fetched first; the farmer and contact photos load phone-sized versions on phones.
- Smoother scrolling: the tower animation does no work outside its section and only updates what changed inside it (about 30% less work per frame); the hero's slow drift pauses once it is off screen; on touch screens the fixed header is solid instead of a live blur, which is costly on mid-range phones.
- No more jump: on FAQ, Privacy and 404 the content jumped 69px when the header turned fixed while scrolling. It now keeps its space.
- Touch: every link and button is at least 44x44px (contact links were 26px tall, footer links 42px); hover lifts no longer stick after a tap, and buttons and cards give a small press response instead; the background no longer scrolls behind the open menu; the product row does not trigger the browser's back-swipe.
- Safe areas: the header, menu, footer and floating WhatsApp button keep clear of notches and the iPhone home bar.
- The floating WhatsApp button now steps aside over the enquiry form and the About page buttons, where it used to cover "Send enquiry".
- Native touches: the address bar follows the light or dark theme, and the site has a home-screen icon and web app manifest for "Add to Home Screen".
- Every tower leaf now reaches full size at the end of the animation (the top ones stopped at 98.7%).

## 2026-10-23: One contact row for products

- The four product cards no longer each carry an "Enquire on WhatsApp" link; they show just the photo and the name.
- One row under the cards offers "Enquire on WhatsApp" (opens WhatsApp with a short product message) and "Call" (+91 74833 06330), in the same pill styles as the other button pairs.
- Translations: the WhatsApp label lost its arrow, and "Call" is added in Kannada, Hindi and Marathi.

## 2026-10-23: Founder strip as a bridge

- The founder teaser on the homepage is no longer a boxed card. It is a quiet strip: his photo with "Meet the founder" (now jumping straight to the founder section on About), a thin divider, then three short lines: Founded in Belagavi by, his name, and his degree. It stacks and centres on phones.
- The farmer photo above now fades into the strip and the contact photo below rises out of it, with no seam in either theme. The UAS emblem is no longer shown in this strip.
- Translations: the one long sentence is split into the three lines in Kannada, Hindi and Marathi.

## 2026-10-23: Design polish

- The language menu and the form's "Interested in" list now open as a rounded panel in the site's colours, with readable options and a green tick on the current choice. Before, the options were dark text on a dark square list. Browsers without the new styling keep their own list, now with readable colours.
- Larger logo in the header and menu (46px on desktop, 34px on phones) so the towers, water and leaves read; the header still fits from 320 to 1440px in all four languages.
- One primary button style: Get a quote, Send enquiry and the Back buttons on the 404 and Privacy pages are now the same solid green. The 404 and Privacy buttons had no style before.
- Palette fixes: the hero's WhatsApp pill and the video play button used a stray grey-blue; the menu's WhatsApp button used WhatsApp green. All now use the site palette (the floating WhatsApp button keeps WhatsApp green).
- Privacy and 404 pages: language and theme stay in the header on phones (those pages have no menu), and their short footer no longer has an empty band above it.

## 2026-10-23: Cleaner header

- Removed the strip above the header (phone, email, location, Instagram, LinkedIn). Instagram and LinkedIn are still linked in the menu, the contact section and the footer; the Privacy and 404 footers now link them too.
- Header in sentence case: the name now reads "Hydrotonic" instead of all capitals.
- Header and menu links run sections first (The tower, Products, Contact), then a thin divider, then other pages (About, FAQ) marked with a small arrow.
- "Get a quote" is now a filled green button on its own at the far right, on phones too. The phone header was tightened so the name, menu and button always fit (checked from 320 to 1440px in all four languages); the Kannada label is now the shorter "ದರ ಕೇಳಿ".
- The tower drawing now finishes one screen early and holds, complete, for one more screen of scrolling before the page moves on. (This was meant to ship with the less-text update but missed the merge.)
- Asset version numbers are bumped properly again, now including the icon sprite, so returning visitors get the new files.

## 2026-10-23: Marathi, and a full language pass

- Added Marathi (मराठी) to the language menu on every page, with every string translated. The site check now requires Kannada, Hindi and Marathi for every key.
- Reviewed the Kannada and Hindi text: the university is now named the same way everywhere, "Fresh Produce" reads as fresh greens and vegetables in Kannada, and headings match the English punctuation.
- The founder's name on About and the footer photo credits are now translated. The FAQ footer no longer credits photos it does not have.
- Kannada and Devanagari now render in Noto Sans Kannada and Noto Sans Devanagari, matched to Montserrat, on every phone instead of whatever font the phone has. Buttons, the language menu and form fields use the same font stack. These languages get taller line spacing so vowel signs and conjuncts never touch.
- The translation file is rewritten one string per line, in page order, so a native speaker can review it.
- On phones the "Get a quote" button is hidden in the top bar; it was colliding with the Hydrotonic name (in English too, and more in Kannada). The floating WhatsApp button, the hero and the menu still offer contact.

## 2026-10-23: Less text, readable photos, setup diagram

- Text on photos (homepage hero, the farmer band, contact, About hero and the About band) is now solid white with a soft shadow, over a dark overlay behind the text. In light mode the contact and band overlays no longer fade to the pale page colour under the heading.
- Removed the template look: no eyebrow tags, no "01 · 02 · 03" section labels or product number badges, no gradient headings, no numbers in the mobile menu.
- Cut the subtext: pillar descriptions, product descriptions, section leads, the swipe hint and the band sentence are gone. The tower steps are now one short line each that narrates the animation.
- "And we set it up for you" is now a four-step icon diagram in the same line style as the tower: tell us about your space, we design it, we bring it and set it up, grow with our support.
- Removed translation entries that no page uses anymore.

## 2026-10-23: Tower illustration redrawn after Hydrotonic's own towers

- The "02 · The tower" animation now shows three single-tube towers on one reservoir pipe, like the logo and the founder's builds, instead of stacked boxes with an outside pipe.
- As you scroll: the towers draw in, the reservoir fills, the pump in the base lifts water up the centre of the middle tower and across the top pipe into the side towers, water trickles back down inside, and leaves grow from cups on the left, front and right of each tower.
- A sun in the top corner, with a soft glow, shows the plants growing toward the light. Water is blue and the sun yellow, in this illustration only.
- The "Recirculating water" step now says the pump sits in the reservoir and lifts water up the centre of the tower (English, Kannada and Hindi).

## 2026-10-23: Sharper link preview

- The link-preview banner is now 2400x1260 (`img/og-banner.jpg`, 232 KB), rebuilt from the 1280x730 original with edge sharpening so the wordmark, tagline and product icons stay crisp. It has a new filename so apps fetch it again.

## 2026-10-23: Link preview image

- Pasting hydrotonic.org (home, About or FAQ) into WhatsApp, LinkedIn, Facebook or X now shows the Hydrotonic brand banner (`img/og-share.jpg`, 1200x630, 75 KB). It replaces the three different preview images.

## 2026-10-23: Brighter About hero, greens band, closer founder portrait

- About hero: the dark treatment is gone. The towers now sit in a bright, softly glowing centre with blurred edges and a light vignette, and the overlay only darkens behind the heading and the top bar.
- The About page ends on a new photo band of lettuce growing on vertical towers, cropped to leaves only (no tower bases, roof or logos) with soft, blurred edges.
- Founder portrait zoomed in to head and shoulders, and the UAS stamp removed from it. On the homepage teaser the UAS badge now sits under his photo instead of on it.
- About footer credit reads "Most photos by Hydrotonic".

## 2026-10-23: New logo, hero and UAS stamp

- New logo cut out from the brand banner: the towers, water and leaves without the background, in a light version for dark surfaces and a navy version for light ones. The header shows the mark beside the name; the footer shows the full logo with HYDROTONIC below. New favicon from the same mark.
- Hero is now one clean Unsplash photo of lettuce growing in a vertical hydroponic system, replacing the terrace photo.
- Contact section brings back the grower holding a seedling tray in a shade-net nursery.
- The University of Agricultural Sciences, Dharwad emblem now appears as a stamp wherever the founder's B.Sc. (Hons.) is mentioned: the Education card and portrait on About, the B.Sc. stat, the homepage pillar and the founder teaser.
- About hero keeps the covered tower farm photo but blurs, desaturates and vignettes everything around the towers.
- Removed four images no page used anymore.

## 2026-10-23: Merge rule

- Pull requests no longer need an approval; Aatif or the owner can merge once the Site checks job passes. Direct pushes, deletions and force pushes to `main` stay blocked.
- AGENTS.md updated to match, with the olive palette and the no-embeds rule corrected.

## 2026-10-23: Hydrotonic's own photos and the founder portrait

- Replaced the stock photos with Hydrotonic's own: rooftop and covered tower farms (hero and About, softened so the build layout is not readable), coriander towers, lettuce, spinach, tomato and coriander in net pots, and roots. One Unsplash photo remains (the farmer portrait in the homepage band).
- Added a founder portrait to the About page and the homepage teaser: a BiRefNet portrait cutout with edge colour cleanup on a plain olive gradient, an olive tone with soft highlights, a soft rim light on hair and shoulders, and a light under-eye retouch. Tone only; his features are unchanged.
- The About page gallery now shows Hydrotonic's own photos instead of Instagram embeds, so the site no longer loads anything from Instagram. The Privacy Notice is updated to match.
- The RAWE entry on the About page now describes the farmer awareness charts and demonstration models prepared in Shirahatti taluk, Gadag district.
- Removed the old business-card product crops.

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
