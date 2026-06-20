# Seer Frights — Hero Art Brief

Brief for the artist creating the homepage hero banner. Read the **Deliverables** and
**Hard constraints** sections carefully — they exist so the art drops cleanly into a
real, fast, responsive website instead of fighting it.

---

## The concept

A professional **series brand** hero banner for a 1990s-style kids' horror book series,
**SEER FRIGHTS**. Fun-scary, not gory. Colorful, glossy, playful-spooky.

The scene lives in the **right two-thirds**:

- A dramatic **3D display of two middle-grade paperbacks**:
  - **_Don't Go Into the Swamp_** in front
  - A second **scarecrow-themed book** partly behind it
- Above the books, a **slime-dripping SEER FRIGHTS logo** with a **glowing cartoon
  eyeball emblem**.
- Atmosphere blending **swamp + cornfield at night**: blue-black night fog, toxic-green
  slime highlights, cold cyan moonlight, fireflies, twisted cypress trees, hanging moss,
  corn-stalk silhouettes, and **faint hidden glowing eyes** in the darkness.

The **left third** stays dark, quiet, and low-detail — that is where the website's
headline and buttons go (added in code, not painted).

> **Do not** deliver a single full-width book cover. This should read as a *series brand
> landing page*, not a one-book product shot.

---

## Hard constraints (please follow exactly)

1. **No baked-in text.** Do **not** paint the headline, tagline, or buttons into the
   image. The words "You should be scared," the body copy, and the buttons are live HTML
   layered on top in code. Leaving a literal text-shaped hole will not line up across
   screen sizes.

2. **Left third = dark & low-detail.** White/cream headline text sits over the left side.
   Keep that area low-contrast and uncluttered so the text stays readable without a heavy
   overlay. Push all the busy detail (eyes, fireflies, moss, slime) to the **right and the
   outer edges**.

3. **Safe zone.** Compose the **logo + book stack** cluster within the **centered 60%**
   of the frame. Nothing critical (logo, book titles, eyeball) should sit near the outer
   edges — phones crop the sides and top aggressively.

4. **Aspect ratio 16:9**, not 2:1. The extra vertical room lets mobile crops survive
   without chopping the books or logo.

5. **No gore, no realistic violence, no clutter.** Cartoon-spooky only.

---

## Deliverables

Please provide all three as **separate files**. Delivering the logo and books as
transparent PNGs with **real alpha channels** is the single most useful thing — it lets us scale them crisply on
retina screens and animate the float/drip independently.

| # | File | Format | Size | Notes |
|---|------|--------|------|-------|
| 1 | **Atmosphere / background** | Lossless **PNG** | **2560 × 1440** (16:9) | The full swamp+cornfield night scene. **No logo, no books, no text.** Left third dark. |
| 2 | **Logo lockup** | **PNG-24 with real alpha transparency** | ~1600 px wide | Slime-dripping SEER FRIGHTS wordmark + glowing eyeball emblem. Isolated on a transparent canvas. Do not paint a checkerboard/white/gray background; the PNG must have an alpha channel. |
| 3 | **Book stack** | **PNG-24 with real alpha transparency** | ~1400 px wide | The two-book 3D stack (Swamp front, scarecrow behind). Isolated on a transparent canvas. Do not paint a checkerboard/white/gray background; the PNG must have an alpha channel. |

Optional but nice: a flattened **preview composite** (all three combined) so we can sanity-check the intended look.
### Transparency requirement for logo + book stack

For deliverables #2 and #3, “transparent PNG” means a true PNG alpha channel.
Do **not** paint or export a white, gray, checkerboard, or paper-colored background.
The image viewer may show a checkerboard behind the art, but that checkerboard must
be the viewer UI, not pixels in the file. Please verify before delivery: the PNG should
open as RGBA / PNG-24 with alpha, not RGB / opaque.


### Color targets (match the existing brand)

| Name | Hex | Use |
|------|-----|-----|
| Slime green | `#7cff3f` | The drip, highlights, glow |
| Deep slime | `#4faf1f` | Slime shadow/depth |
| Swamp night | `#07100b` | Darkest background |
| Bog green-black | `#0d1f12` | Mid background |
| Bone cream | `#f3ecd6` | (text color — leave room for it on the left) |
| Blood red | `#ff3b30` | Sparse danger accents only |
| Purple | `#9b5cff` | Secondary glow / eyebrow accents |

---

## Why these constraints (short version)

- **Separate transparent layers** → sharp on retina, independently animatable, logo
  swappable later without a re-render.
- **16:9 + safe zone** → one master image survives desktop *and* phone crops; no separate
  mobile painting needed.
- **Dark left third, no painted text** → the real HTML headline stays crisp and readable
  at every size, and copy can change without new art.
- **Lossless PNG master** → we compress to WebP/AVIF (~150–300 KB) for a fast first paint
  without double-compression artifacts.

---

## Where it lands in code

The site layers them like this (back to front):

1. Background atmosphere (`hero-bg.webp`) — full-bleed, with a left-side scrim for text.
2. Book stack (`hero-books.png`) — right side, gentle float animation.
3. Logo lockup (`hero-logo.png`) — above the books, subtle drip/glow.
4. **Live HTML** headline + tagline + buttons — left third.

The placeholder layers are already stubbed in `index.html` / `style.css`, so the art drops
straight in with no redesign.
