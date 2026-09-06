# Seer Frights redesign

## Review findings

The original site had strong series identity and good book-cover assets, but the presentation was much darker and denser than Seer Worlds. The biggest design differences were:

- nearly every section used a dark background, which reduced visual hierarchy
- the home page relied on a layered hero system with separate background, book-stack, and logo images
- typography leaned heavily on novelty/display fonts
- book information was presented in long alternating blocks instead of the cleaner cover-first grids used on Seer Worlds
- the mobile navigation was a wrapped list rather than the compact menu pattern used on Seer Worlds
- the hero art was extremely dark, especially on interior pages

## Redesign direction implemented

1. **Use Seer Worlds as the layout language, not as a color copy.**
   - full-bleed hero
   - transparent navigation over the hero
   - cream/paper content areas alternating with deep atmospheric bands
   - modern rounded cards and generous spacing
   - cover-first book showcase

2. **Keep Seer Frights visually distinct.**
   - deep green/black night palette
   - acid-green accent
   - small purple secondary accent
   - spooky-fun imagery rather than blue/gold fantasy imagery

3. **Modernize the home page.**
   - one clear visual hero and two primary CTAs
   - a parchment-style introduction strip similar to Seer Worlds
   - a five-cover series showcase
   - shorter, clearer series-positioning sections

4. **Modernize Books and About.**
   - Books uses large cover cards on a light paper background
   - About uses a readable editorial layout with a supporting image and facts panel
   - the author/imprint content is separated into clean dark cards

5. **Modernize every individual book page.**
   - cinematic title hero
   - sticky large cover on desktop
   - clean specification card
   - wider readable synopsis column
   - consistent buy/all-books CTAs
   - related-book cover strip at the bottom

6. **Improve imagery and performance.**
   - replaced the old layered hero setup with web-optimized professional artwork
   - added dedicated `hero-home.webp`, `hero-sub.webp`, and `about-scene.webp`
   - retained the approved 1600×2560 book covers unchanged

7. **Improve responsive behavior and accessibility.**
   - skip link
   - semantic navigation
   - mobile Menu button with `aria-expanded`
   - responsive grids and book-detail layout
   - no external font dependency

## One content question

The source About page says **“Book 1 coming soon”**, while the Books page and individual book pages say the books are **“Available now.”** The redesign preserves the About-page wording rather than silently changing source content. If that status is outdated, it should be changed to the wording you prefer.


## September 2026 — cover-alignment redesign, Phase 1

The book covers were redesigned into a new look: true-black backgrounds, one
spotlit object per book, a dripping acid-yellow "SEER FRIGHTS" wordmark, and a
thin "— BOOK N —" rule. The site's cream-paper / painterly-swamp language no
longer matched. Phase 1 realigns color and texture only (no new art, no new
fonts, no markup changes beyond meta tags):

- **Palette retuned to the covers.** Grounds moved from deep swamp-green to true
  black (`--night-deep:#000`); the accent green moved yellower
  (`#a6e93c → #d8f23c`) to match the wordmark; warm paper tones replaced with a
  near-white (`#faf9f5`); added a `--brass` object-light accent and a `--glow`
  token.
- **Dropped the parchment treatment.** Removed the torn-paper `clip-path` edges
  and the paper-speckle `radial-gradient` textures. `.parchment` and every dark
  band are now flat black separated by thin chartreuse hairline rules
  (`.rule-divider` echoes the cover's BOOK-N rule).
- **Cards rebuilt for black covers.** Book tiles, news cards, related strip, and
  the home `.split-art` no longer sit covers on a warm mat — they use a
  near-black field with a soft chartreuse glow behind the cover.
- **Heroes regraded.** Home / sub / book / 404 hero photos are crushed toward
  black with a single warm key light instead of the old blue-green wash.
- **Legacy painterly art** (`about-scene.webp`) is desaturated and dimmed via CSS
  as a stopgap — it should be replaced with cover-aligned art in a later phase.
- `theme-color` → `#000000` on every page; home `og:image` → the Book 1 cover.

## September 2026 — cover-alignment redesign, Phase 2 (typography)

A three-face horror-paperback type system, matching how the covers set type
(dripping title face + clean supporting text):

- **Display — `Creepster`** (Google Fonts, dripping horror caps). Used only for
  the wordmark, hero H1s, book-title heroes, the `BOOK N` card labels, and the
  `— THE BOOKS —` rule. This is the closest free match to the covers' hand-drawn
  lettering; the exact cover font isn't licensed for web, so a true wordmark SVG
  is still a later item.
- **Headings — `Anton`** (Google Fonts, heavy condensed). All section H2s, card
  and feature titles, set uppercase — the horror-paperback subhead voice,
  replacing the plain-serif headings that read as generic.
- **Body — Georgia**, unchanged.
- **Wordmark fixed to one line.** `SEER FRIGHTS` was stacked `SEER` / `FRIGHTS`
  in the header and footer, which the locked cover spec forbids; both halves are
  now one baseline-aligned line in the display face.
- **Cover title color adopted.** Home hero wordmark → acid green (`--green`, the
  series-mark color); book-title heroes → `--title-yellow #E6C91E` (the exact
  locked cover title hex).
- Fonts are `preconnect`ed and requested in one stylesheet call per page.

Mobile note: headless screenshots couldn't reliably emulate a phone viewport, so
the small-screen type scale (sane `clamp` floors + `body{overflow-x:hidden}` as a
backstop) is coded but wants a real-device check.

## September 2026 — cover-alignment redesign, Phase 4 (per-book accent + last of the legacy art)

- **Per-book "object light."** Each book page's `<body>` gets a `book-1`…`book-5`
  class that sets `--accent` (an unquoted `r,g,b` triple) to the color glowing
  off that cover's object: `77,184,230` cyan (Book 1 lantern), `201,138,60` warm
  wood (Book 2 tag), `138,143,150` ash (Book 3 skin), `224,169,46` gold (Book 4
  card), `185,138,78` brass (Book 5 key). It drives the book-hero's secondary
  spotlight pool and the large cover's outer glow — nothing else. The brand
  green/yellow are untouched, so the differentiation is atmospheric, not a
  five-theme system.
- **`about-scene.webp` retired.** The painterly swamp is gone from both places it
  lived: the home "grown-ups" section now shows a two-cover pair (`.cover-duo`)
  and the About sidebar a three-cover fan (`.cover-trio`), both on a lit surface
  with a chartreuse glow — same treatment as the book cards. The CSS grading
  hack from Phase 1 is removed.
- `images/` now holds only the five covers plus the two cross-brand Other Series
  images. Every Seer Frights image on the site is a book cover.

Still not done: a true hand-drawn wordmark SVG (Creepster is a close stand-in).

## September 2026 — cover-alignment redesign, Phase 3 (heroes + motifs)

The heroes were the last piece still speaking the old painterly-swamp language.
Rebuilt in CSS with the covers as the only art:

- **Home hero = the cover wall.** The painterly `hero-home.webp` is gone; the
  hero is now flat black with one top-center pool of light and the five covers
  fanned like a shelf caught in that light, wordmark and copy alongside. "The
  hero is the most characteristic thing in the subject's world" — that's the five
  covers.
- **Sub-hero and book-hero** dropped `hero-sub.webp` for flat black + a spotlight
  glow + the drip edge. Book heroes glow and drip in the cover title yellow
  (`--title-yellow`); everything else in acid green.
- **Drip motif.** A reusable `--drip` SVG mask (solid bar + irregular hanging
  teardrops, echoing the wet cover lettering) sits at the bottom edge of every
  dark hero, doubling as the transition into the light sections.
- **Spotlight motif.** Every dark hero carries a single radial pool of light
  (green from the top, a warm brass secondary) — the way every cover object is
  lit.
- **404** rebuilt to match (black + spotlight, green Creepster headline).
- **Favicon** recolored to the new palette (`#000` ground, `#d8f23c` slime).
- **Other Series** — the Seer Frights card now uses the Book 1 cover instead of
  the retired swamp photo.
- `hero-home.webp` and `hero-sub.webp` deleted (unreferenced, ~850 KB).

## August 2026 navigation / content update

- Added `/other-series/` in the Seer Worlds-style card layout, themed for Seer Frights.
- Added `/news/` with a featured series update and supporting book/news cards.
- Added Other Series and News to the top navigation on every page.
- Rebuilt the footer using the multi-column i4Seer publisher pattern, with Seer Frights styling.
- Added optimized Seer Worlds and Seer Warns artwork for the Other Series page.
- Preserved the latest home-hero alignment update.
