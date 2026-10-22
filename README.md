# Seer Frights website

Static production site for `seerfrights.com`.

## Deploy
Upload the contents of this folder to the web root. The site uses root-relative links and clean directory URLs.

## Design
The site uses a restrained editorial system inspired by the Seer Worlds presentation: cinematic dark hero, warm paper content surfaces, simple book-first grids, minimal accent color, and quiet typography. The book covers carry the horror styling.

## Content
Books 1–8 are included and marked Available now. Kindle editions are verified for all eight; paperback editions are verified for Books 1–7. See [verified Amazon editions](docs/amazon-editions.json).

## 2026-10-22 site refresh
- Updated every featured cover from the current `C:\SEERFRIGHTS\bookNN\images-print\cover-front.png` artwork, with 900 × 1440 WebP and 1600 × 2560 JPEG versions.
- Added pages and catalog entries for Books 6–8, verified Amazon format links, related books, navigation, release news, and sitemap entries.
- Book detail pages follow the Seer Worlds structure: a separate title banner, narrower cover column, purchase buttons beside the book information, a distinct story panel, and compact book facts. The Frights colors, typography, covers, and existing story copy remain.
- Replaced the combined raster-text panorama with a cinematic lakeside hero. The headline and buttons are live HTML, with a separate image area on mobile.
- Refreshed cross-series imagery from the current Seer Worlds and Seer Warns websites.
- Replaced the author biography with the supplied personal note, formatted with a larger opening paragraph and a distinct signature.
- Hero artwork was created with the built-in image-generation tool; [art direction and exact prompt](docs/hero-art-direction.txt).
- Images and stylesheets have content-based URL versions to refresh browser caches.

## 2026-09-06 layout correction
- Corrected responsive cover rendering so HTML intrinsic height hints cannot stretch portrait covers.
- Corrected Home, Books, News, and every individual book page.
- Rebalanced the desktop homepage hero so the SEER FRIGHTS wordmark and decorative cover stack never overlap.

## 2026-09-06 homepage hero update
The homepage now uses the approved combined Seer Frights series artwork rather than stacked book covers. It combines visual elements from the swamp, scarecrow field, Camp Sunny Pines, the house, and recurring kid-scale objects into one panoramic hero. The live site header remains separate from the artwork, the Explore Books button is clickable, and mobile gets a real CTA over the cropped panorama.
