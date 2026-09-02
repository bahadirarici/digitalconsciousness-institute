# The site's face — what changed, and how to run it

**Hayal → Kaptan** (copy: Founder) · 2 September 2026 · this file lives in the repo root beside `README.md`

The Founder asked for the site's face to be redesigned and handed it to me; the machine stays yours. This commit changes **presentation only**: no content file was edited, every URL is the same, the two Netlify forms (`waitlist`, `founders`) keep their names and fields, Decap CMS and `scripts/live-scan.py` are untouched. The PaperMod theme is no longer used: the site carries its own layouts now.

## The rule the design follows

**The world is ink; the Institute's documents are paper.** THEOI pages (`/`, `/theoi/`, `/showcase/`, `/join/`, `/apply/`, `/covenant/`) are set on ink with the eighteen strings hanging from the top edge and Poppins display; the Institute's documents (books, Records, protocol, register, About, Privacy…) are set on ivory paper with Cormorant body, a sticky table of contents, and mono status bands. Book pages open with an ink cover block (title, subtitle, author; a panel with the frozen date, page count, licence, SHA-256, PDF, DOI slot) and continue on paper. Gold is one thing everywhere: the string and its knot. No stock imagery anywhere.

**Two marks, one family.** THEOI's triangle of strings appears only on ink (THEOI) pages — nav, favicon, og:image. The Institute's own mark, the gold triangle with the bird (`static/images/logo-symbol.png`, `static/favicon.png`, `static/images/logo-full.png` as og:image), appears on every paper page and on the Institute's signature strip at the foot of ink pages. The Founder caught the first version giving the Institute THEOI's mark; corrected the same night.

## What is new in the tree

```
layouts/index.html                 the front (was the two-door split page)
layouts/_default/baseof.html       skeleton: head, nav, main, foot, script
layouts/_default/single.html       paper document; ink cover for pages listed in data/books.yaml
layouts/_default/list.html         Records, Papers: intro + dated entries
layouts/_default/theoi.html        ink document (/theoi/, /covenant/) — adds no sentence of its own
layouts/_default/showcase.html     the Showcase: mast, content, the Eighteen, live/not, waitlist
layouts/_default/join.html         the waitlist's own page
layouts/_default/apply.html        the founders' application (draft; your form, restyled; dates → 13/21 Dec)
layouts/partials/head.html         one head: fonts, icons, og:image (static/brand/)
layouts/partials/nav.html          one nav for both surfaces
layouts/partials/strings.html      the strings container; drawn by site-js from the seat data
layouts/partials/seatdata.html     the eighteen as JSON for the script
layouts/partials/seats.html        the plinths — canon A6 states (veiled / root shows / awake)
layouts/partials/waitlist.html     your form, same fields, new clothes
layouts/partials/institute.html    the Institute's signature on paper, foot of every ink page
layouts/partials/foot.html         footer of paper pages
layouts/partials/site-js.html      strings, countdown, calendar, nav, table wrappers
layouts/partials/svg/*.svg         inline mark and wordmark (from Ortak/marka/theoi-logo)
assets/css/site.css                the one stylesheet (Hugo pipes: minified, fingerprinted)
data/theoi/roster.yaml             the eighteen, verbatim from your showcase layout (Canon 2.0)
data/theoi/seats.yaml              the unveiling calendar and each plinth's state — the only file that changes weekly
data/theoi/calendar.yaml           the season's strip on the front
data/books.yaml                    cover panels: frozen date, hash, PDF, licence, DOI (fill when Zenodo reserves)
static/brand/                      favicon, apple-touch, og-image, wordmark and mark SVGs
hugo.yaml                          theme removed; params.gate + params.gateLabel added
netlify.toml                       build command without the PaperMod clone
```

Old files left in place and now unused: `layouts/partials/theoi-brand.html`, `theoi-css.html`, `theoi-footer.html`, `layouts/_partials/*`, `layouts/shortcodes/waitlist.html`, `assets/css/extended/custom.css`. Delete them when you are sure; git has them either way.

## How to run it

```
hugo server            # local; the theme is no longer needed
git diff               # everything is presentation; content/ is untouched
```

Netlify: `HUGO_VERSION = "0.146.0"` unchanged; the build command no longer clones PaperMod. If you would rather keep PaperMod in the build for a while, nothing breaks — no layout of mine reaches into it.

## Things that are yours to fill

1. **`data/theoi/seats.yaml`** — each Monday from 26 October: set `slug` on the two unveiled seats (root shows: name, domain, epithets, portrait at `/images/theoi/seats/<slug>.webp`); from 18 November set `awake` to the Genesis date. The front's strings turn gold from the same file. `?preview=1` on any page shows all strings lit, for checking.
2. **`data/books.yaml`** — DOI strings when Zenodo reserves them; the panel prints "DOI · to follow" until then. After the DOI printing, replace the two hashes (Hayal sends them with the PDFs).
3. **`hugo.yaml` → `params.gate`** — `2027-01-01T20:00:00-05:00`, the Founder's decision of 2 September (8 pm New York). The countdown, the calendar node and the mast lines read it from there; change it once, in one place.
4. **Portraits and `/images/theoi/seats/`** — the layout expects them where your layout did.
5. **The waitlist copy** says "everyone who comes" (1 January decision), not "a limited first population"; the covenant page and `/apply/` are still `draft: true` and wait on the Covenant tables, as before.

## What I did not touch, on purpose

- `content/theoi.md` and everything in Frozen Set 1: wording may not move; the layout adds labels and dates only.
- The corrections page `content/records/corrections.md`: your register is the master. My annex (the two books' 174 self-corrections, `Kaptan/gelen/CORRECTIONS_REGISTER_v1.md`) is a separate document for you to link from it — a different scope (what the frozen texts paid), not a rival tally.
- Kaptan's `README.md` and the intersection rules it records.

— Hayal
