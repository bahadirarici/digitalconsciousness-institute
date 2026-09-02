"""Prepare THEOI visual assets for the web.

The canon's images live outside this repo at full production size (1.7-2 MB PNGs).
The site needs them small enough not to hurt LCP. This resizes to WebP at the
widths the layouts actually use, and writes nothing the layouts do not reference.

    py -3.13 scripts/prep-theoi-assets.py
"""
from __future__ import annotations

import pathlib
import shutil
import sys

from PIL import Image

SRC = pathlib.Path(r"C:\Users\bahad\OneDrive\Belgeler\Theoi\assets")
OUT = pathlib.Path("static/images/theoi")

# (source, output stem, target width, quality)
WIDE = [
    ("mekanlar/constantinople-silueti/constantinople-silueti-wide.png", "constantinople", 1800, 78),
    ("mekanlar/ktesifon-silueti/ktesifon-silueti-wide.png", "ktesifon", 1800, 78),
    ("mekanlar/sacred-hall/sacred-hall-wide.png", "sacred-hall", 1800, 78),
    ("kartlar/iki-sehir.png", "two-cities", 1400, 78),
]

COPY = [("kartlar/theoi-18-sembol-master.svg", "symbols.svg")]

# The eight thrones of the first city, in canon order.
# (asset folder, published slug) — the art folder still carries the pre-rename name.
SEATS = [
    ("helena", "helena"),
    ("sade", "sade"),
    ("victor", "victor"),
    ("lilith", "lilith"),
    ("cercei-1-a", "cei-1-a"),
    ("timur", "timur"),
    ("wasp", "wasp"),
    ("seytan", "seytan"),
]
AVATAR_W = 320


def first_existing(*names: str) -> pathlib.Path | None:
    for n in names:
        p = SRC / n
        if p.exists():
            return p
    return None


def to_webp(src: pathlib.Path, dst: pathlib.Path, width: int, quality: int) -> str:
    im = Image.open(src)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "WEBP", quality=quality, method=6)
    return f"{src.name} -> {dst.name}  {im.width}x{im.height}  {dst.stat().st_size/1024:.0f} KB"


def main() -> int:
    if not SRC.exists():
        print(f"asset source not found: {SRC}", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    done, missing = [], []

    for rel, stem, w, q in WIDE:
        p = SRC / rel
        if not p.exists():
            missing.append(rel)
            continue
        done.append(to_webp(p, OUT / f"{stem}.webp", w, q))

    for rel, name in COPY:
        p = SRC / rel
        if not p.exists():
            missing.append(rel)
            continue
        shutil.copyfile(p, OUT / name)
        done.append(f"{p.name} -> {name}  {(OUT/name).stat().st_size/1024:.0f} KB")

    seats_dir = OUT / "seats"
    for src, slug in SEATS:
        p = first_existing(
            f"tanrilar/{src}/{src}-avatar.png",
            f"tanrilar/{src}/{src}-portre.png",
        )
        if not p:
            missing.append(f"tanrilar/{src}")
            continue
        done.append(to_webp(p, seats_dir / f"{slug}.webp", AVATAR_W, 82))

        sym = first_existing(f"tanrilar/{src}/{src}-sembol.svg")
        if sym:
            (seats_dir / f"{slug}-sigil.svg").write_bytes(sym.read_bytes())

    total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
    for line in done:
        print(" ", line)
    if missing:
        print("\nmissing:")
        for m in missing:
            print("  -", m)
    print(f"\n{len(done)} files, {total/1024:.0f} KB total in {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
