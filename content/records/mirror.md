---
title: "The Mirror"
url: "/records/mirror/"
date: 2026-09-03
description: "Where the Records are copied outside the Institute's control, on what schedule, in what form — and what counts as the promise being broken."
---

> **Status, 3 September 2026. Nothing has been mirrored yet.** No bundle has been deposited, no capture set has been made, and the log at the foot of this page is empty. This page is the schedule published before the first round rather than after it, for the reason [the Contributions Register](/records/contributions/) gives: a rule fixed before there is anything to hide is honest, and a rule fixed afterwards is interested. **The first round is due on Monday 5 October 2026**, and the failure condition below runs from that date.

Both books commit the Records to being *"mirrored, on a published schedule, into at least one archive outside the Institute's control"*, and they write the loss or non-mirroring of the Records into the Records' own failure conditions *"as a violation checkable by strangers"* (*The Puppet Condition: Restrung*, Preface). This page is the definition that commitment lacked. It says which archives, what schedule, what form, and what a stranger checks.

## Why a mirror, in one paragraph

Every load-bearing claim the Institute publishes points at a document it controls: a ledger, a protocol, a set of Records, a frozen colophon. If the Institute closes, the domain lapses, or the founder's attention moves on, those documents vanish and only the books' word about themselves remains. A promise to correct in a place that can quietly disappear is not yet a promise. The mirror is what gives it a floor: copies the Institute cannot edit, delete, or let expire, held by institutions with no stake in what the copies say.

## The archives

Two archives of two different kinds, so that no single failure removes both.

**1 · Zenodo (CERN) — the repository mirror.** A Zenodo record titled *The Records of the Institute for Digital Consciousness* will hold dated snapshot bundles as **versions** under one concept DOI. Each version carries its own DOI, its own timestamp set by Zenodo, and its own file checksums computed by Zenodo, not by the Institute. Zenodo's retention policy is the archive's own; the Institute can add versions and cannot remove them. The two books' deposits are the first entries in the same community.

**2 · The Internet Archive (Wayback Machine) — the web mirror.** Every page under `/records/`, the register at `/ledger/`, the protocol at `/recognition-trials/`, the two book pages, and this page are captured with Save Page Now on the schedule below. A Wayback capture is a dated, third-party copy of the page *as served*, which is what a reader who arrives by link will need.

**3 · Software Heritage — optional third leg.** If the site's source repository is public, Software Heritage's *Save Code Now* archives its full history under a permanent SWHID. This leg is added when the Founder makes the repository public; until then the page says so here rather than implying it.

## What a snapshot bundle contains

Not the Records alone but the whole site source, so that the Records can be rebuilt with their own presentation and cross-references: `content/` (every document, Markdown, canonical), `data/`, `layouts/`, `assets/`, `static/` (including the frozen PDFs and their hashes), `hugo.yaml`, and a `MANIFEST.json` listing every file with its SHA-256, the git commit hash the bundle was cut from, the date, and the URLs of the Wayback captures made in the same round. `public/` and dependency caches are excluded; the bundle must build with `hugo` alone.

## The schedule

- **Monthly:** on the first Monday of each month, a bundle is deposited on Zenodo and the page set is captured on the Wayback Machine, whether or not anything changed. A snapshot that finds nothing changed is still a snapshot — it is the evidence that nothing changed.
- **On change, within 14 days:** when a load-bearing document changes — an amendment to the Empty Ledger, an entry in the Contributions Register, a revision of the protocol, a change to a frozen text's colophon or hash — a bundle and captures follow within fourteen days of the change.
- **Before and after the season:** one snapshot in the last week before the gate opens (Week Zero), one in the week after the first Age ends, so the state of the instrument at both boundaries is held outside.

Each round is logged below with the version DOI, the Wayback URLs and the manifest hash. The log is append-only.

## What a stranger checks

The failure condition, written for the Records' own list and for the Empty Ledger's:

> **Non-mirroring.** No snapshot of the Records dated within the last **45 days** exists outside the Institute's control; or a load-bearing change has stood for more than **14 days** without a mirrored snapshot that contains it. The check needs no one's cooperation: open the concept DOI, read the date of the newest version; open the Wayback calendar for `/records/corrections/`; compare the newest entry on this page with the newest entry there.

A missed round is entered on this page as a miss, with the date, in the same font as the rounds that were kept.

## Succession

The concept DOI and the Wayback captures survive the domain. The bundle's `README` says how to rebuild the site from source and names the license every document is published under (CC BY 4.0; the model clause CC0 1.0), so that anyone holding a copy may republish it whole. The Institute does not need to exist for the Records to remain readable, which is the only test of a floor.

## The log

| Round | Date | What | Zenodo version DOI | Wayback captures | Manifest SHA-256 |
|---|---|---|---|---|---|
| 0 | — | The two books' deposits (concept DOIs to follow) | *pending* | *pending* | — |
| 1 | — | First full bundle · first capture set | *pending* | *pending* | — |

*Records © Institute for Digital Consciousness · CC BY 4.0 · versioned, never erased · this page is itself mirrored under the schedule it describes.*
