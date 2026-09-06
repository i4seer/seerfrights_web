# Seer Frights website

Static site for **seerfrights.com**.

## Structure

- `/` — home
- `/books/` — all books
- `/books/<title>/` — individual book pages
- `/about/` — series, author, and imprint
- `/other-series/` — Seer Worlds, Seer Frights, and Seer Warns
- `/news/` — series news and updates
- `/404.html` — custom not-found page

## Design

The site uses the same broad modern layout language as Seer Worlds while keeping the Seer Frights identity. As of the September 2026 cover-alignment pass (Phases 1–2 — see `REDESIGN-NOTES.md`), it follows the redesigned book covers: true-black sections separated by thin acid-yellow hairline rules, near-white relief sections, black-field book cards with a chartreuse glow behind each cover, regraded heroes, the yellower Seer Frights green accent, and a three-face type system — `Creepster` (dripping wordmark / heroes / book titles), `Anton` (condensed section headings), Georgia (body).

The footer follows the richer publisher-style structure used on i4Seer, adapted to Seer Frights with Explore, Seer Series, and Seer Press columns.

## Assets

- `images/cover-*.jpg` — approved book covers (1600×2560). These now carry the
  hero art too: the home hero fans all five, and the sub/book heroes are pure
  black with a spotlight and a CSS drip edge (no photographic hero).
- `images/about-scene.webp` — legacy painterly image, still on About and the
  home page, CSS-graded toward the palette pending replacement
- `images/series-worlds.webp`, `images/series-warns.webp` — Other Series artwork
  (cross-brand; the Seer Frights card there uses the Book 1 cover)

No build step is required.
