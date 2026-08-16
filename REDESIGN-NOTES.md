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


## August 2026 navigation / content update

- Added `/other-series/` in the Seer Worlds-style card layout, themed for Seer Frights.
- Added `/news/` with a featured series update and supporting book/news cards.
- Added Other Series and News to the top navigation on every page.
- Rebuilt the footer using the multi-column i4Seer publisher pattern, with Seer Frights styling.
- Added optimized Seer Worlds and Seer Warns artwork for the Other Series page.
- Preserved the latest home-hero alignment update.
