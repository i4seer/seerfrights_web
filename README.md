# Seer Frights website

Static production site for `seerfrights.com`.

## Deploy
Upload the contents of this folder to the web root. The site uses root-relative links and clean directory URLs.

## Design
The site follows the current Cold Light covers for Books 1–6: near-black blue surfaces, lantern cyan (`#6dded8`), aged cream (`#f5ebd1`), restrained brass, and the same Alegreya SC Black title font and Charter reading font used in the books. All fonts are local, with licenses in `assets/fonts/`.

## Content
Books 1–8 are included and marked Available now. Kindle editions are verified for all eight; paperback editions are verified for Books 1–7. See [verified Amazon editions](docs/amazon-editions.json).

## 2026-10-26 artwork and theme refresh

- Synced all 20 current front covers and text-free illustrations from `C:\SEERFRIGHTS`, including the website’s eight listed books. Source JPEGs are copied exactly; 900 × 1440 WebP covers, landscape artwork, and lightweight thumbnails are exported for the web.
- Replaced the older photographic hero with Book 1’s actual engraved swamp illustration. A six-image strip introduces the places and objects on the first six covers.
- Applied the cover typography and palette to every page, including the catalog, book details, About, News, other collections, navigation, buttons, browser colors, and favicons. Book banners use their own updated artwork.
- Preserved existing book listings, availability, story copy, and verified purchase links.
- Added `data/frights-artwork.json` with source fingerprints and a repeatable sync: `python scripts/sync_frights_artwork.py`. Requires Pillow and fonttools. Use `--source` to specify a different source folder or `--versions-only` after editing site styles or markup.
- All artwork, fonts, CSS, metadata images, and shared collection images use content-based cache versions.

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
