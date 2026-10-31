"""Export current SEERFRIGHTS artwork and refresh content-versioned local URLs.

Run from any directory: python scripts/sync_frights_artwork.py
Requires Pillow and fonttools. Does not change source artwork or listings.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

from PIL import Image, ImageDraw, ImageOps
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def slugify(title):
    title = title.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", title).strip("-")


def export(source, book_numbers=None):
    images = ROOT / "images"
    images.mkdir(exist_ok=True)
    books = sorted(source.glob("book[0-9][0-9]"))
    previous = {}
    if book_numbers is not None:
        if not book_numbers.issubset({int(book.name[4:]) for book in books}):
            raise ValueError('Unknown source book number')
        previous = {b['number']: b for b in json.loads((ROOT / 'data/frights-artwork.json').read_text(encoding='utf-8'))['books']}
    # Validate the whole source set before replacing the website exports.
    for book in books:
        if book_numbers is not None and int(book.name[4:]) not in book_numbers:
            continue
        for name in ("cover-front.png", "cover-front.jpg", "background-cold-light-master.png"):
            if not (book / "images-print" / name).is_file():
                raise FileNotFoundError(book / "images-print" / name)
    records = []
    for book in books:
        if book_numbers is not None and int(book.name[4:]) not in book_numbers:
            records.append(previous[int(book.name[4:])])
            continue
        title = re.search(r'^title:\s*"(.+)"', (book / "metadata.yaml").read_text(encoding="utf-8-sig"), re.M)[1]
        slug = slugify(title)
        original = book / "images-print" / "cover-front.png"
        cover = Image.open(original).convert("RGB")
        jpeg = images / f"cover-{slug}-front.jpg"
        webp = images / f"cover-{slug}-front-web.webp"
        shutil.copyfile(book / "images-print" / "cover-front.jpg", jpeg)
        cover.resize((900, 1440), Image.Resampling.LANCZOS).save(webp, quality=88, method=6)
        master = book / "images-print" / "background-cold-light-master.png"
        art = Image.open(master).convert("RGB")
        landscape = ImageOps.fit(art, (1600, 900), Image.Resampling.LANCZOS, centering=(0.6, 0.58))
        artwork = images / f"art-{slug}.webp"
        landscape.save(artwork, quality=87, method=6)
        thumbnail = images / f"art-{slug}-thumb.webp"
        ImageOps.fit(art, (480, 300), Image.Resampling.LANCZOS, centering=(0.75, 0.58)).save(thumbnail, quality=85, method=6)
        if book.name == "book01":
            hero = ImageOps.fit(art, (1920, 1080), Image.Resampling.LANCZOS, centering=(0.6, 0.58))
            hero.save(images / "seer-frights-series-hero.webp", quality=90, method=6)
            hero.save(images / "seer-frights-series-hero.jpg", quality=92, optimize=True)
            hero.save(ROOT / "assets/seer-collections/seer-frights-20261022.webp", quality=90, method=6)
        record = {
            "number": int(book.name[4:]), "title": title, "slug": slug,
            "source": f"{book.name}/images-print/cover-front.png",
            "source_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
            "source_art": f"{book.name}/images-print/background-cold-light-master.png",
            "source_art_sha256": hashlib.sha256(master.read_bytes()).hexdigest(),
            "jpeg": f"/images/{jpeg.name}?v={digest(jpeg)}",
            "webp": f"/images/{webp.name}?v={digest(webp)}",
            "artwork": f"/images/{artwork.name}?v={digest(artwork)}",
            "thumbnail": f"/images/{thumbnail.name}?v={digest(thumbnail)}",
        }
        records.append(record)
        print(f"Synced book {record['number']:02}: {title}")
    if book_numbers is not None:
        (ROOT / "data/frights-artwork.json").write_text(json.dumps({"source": "SEERFRIGHTS", "books": records}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return records
    for name in ("author", "logo"):
        image = Image.open(source / "assets" / f"{name}.png").convert("RGB")
        image.thumbnail((900, 900), Image.Resampling.LANCZOS)
        image.save(images / f"{name}.webp", quality=90, method=6)
    fonts = ROOT / "assets/fonts"
    fonts.mkdir(exist_ok=True)
    for name in ("AlegreyaSC-Black", "Charter-Regular", "Charter-Italic"):
        font = TTFont(source / "fonts" / f"{name}.ttf")
        options = subset.Options()
        options.flavor = "woff"
        worker = subset.Subsetter(options=options)
        worker.populate(unicodes=list(range(0x100)) + list(range(0x2010, 0x2028)) + list(range(0x2190, 0x219A)))
        worker.subset(font)
        font.flavor = "woff"
        font.save(fonts / f"{name}.woff")
    for license_name in ("AlegreyaSC-OFL.txt", "Charter-LICENSE.txt"):
        shutil.copyfile(source / "fonts" / license_name, fonts / license_name)
    (ROOT / "data/frights-artwork.json").write_text(json.dumps({"source": "SEERFRIGHTS", "books": records}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    icon = Image.new("RGB", (64, 64), "#071014")
    ImageDraw.Draw(icon).polygon([(18,13),(48,13),(48,21),(27,21),(27,31),(44,31),(44,39),(27,39),(27,54),(18,54)], fill="#6dded8")
    for size in (16,32):
        icon.resize((size,size),Image.Resampling.LANCZOS).save(ROOT / f"favicon-{size}x{size}.png")
    icon.save(ROOT / "favicon.ico", sizes=[(16,16),(32,32),(48,48),(64,64)])
    return records


def refresh_versions():
    manifest = ROOT / "data/frights-artwork.json"
    if manifest.is_file():
        books = json.loads(manifest.read_text(encoding="utf-8"))["books"]
        css_path = ROOT / "style.css"
        css = css_path.read_text(encoding="utf-8")
        css = re.sub(r'\n/\* Synced book artwork \*/[\s\S]*$', '', css)
        css += '\n/* Synced book artwork */\n'
        css += '\n'.join(f'.book-{book["number"]}{{ --book-art:url("{book["artwork"]}") }}' for book in books)
        css += '\n.book-detail-page .book-title-band{background-image:linear-gradient(90deg,rgba(7,16,20,.97),rgba(7,16,20,.8)),var(--book-art);background-position:center,70% 55%}\n'
        css_path.write_text(css, encoding="utf-8")
    # Refresh HTML, CSS and JSON including Open Graph and structured-data images.
    pattern = re.compile(r'(?P<path>/(?:images|assets)/[^\s\"\'<>?()]+\.(?:webp|jpg|png|woff2|woff)|/style\.css|/site\.js|/favicon\.svg|/site\.webmanifest)(?:\?v=[a-zA-Z0-9-]+)?')
    # CSS must be finalized before its hash is inserted into HTML.
    for file in [ROOT / "style.css", *ROOT.rglob("*.html")]:
        content = file.read_text(encoding="utf-8")
        if file.suffix == ".html":
            content = content.replace('name="theme-color" content="#0a0a0b"', 'name="theme-color" content="#071014"')
            if 'rel="preload" as="font"' not in content:
                content = content.replace('<link rel="stylesheet" href="/style.css', '<link rel="preload" as="font" href="/assets/fonts/AlegreyaSC-Black.woff" type="font/woff" crossorigin>\n<link rel="stylesheet" href="/style.css')
        def version(match):
            local = ROOT / match["path"].lstrip("/")
            return f'{match["path"]}?v={digest(local)}' if local.is_file() else match[0]
        updated = pattern.sub(version, content)
        if updated != file.read_text(encoding="utf-8"):
            file.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT.parent / "SEERFRIGHTS")
    parser.add_argument("--versions-only", action="store_true")
    parser.add_argument("--book", type=int, action="append", help="Refresh only this book number; repeat to select more than one")
    args = parser.parse_args()
    if args.book and args.versions_only:parser.error('--book cannot be combined with --versions-only')
    if not args.versions_only:
        export(args.source, set(args.book) if args.book else None)
    refresh_versions()
