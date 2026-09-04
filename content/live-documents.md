---
title: "Live Documents"
url: "/live-documents/"
description: "Which published document depends on which, so that a change in one obliges a scan of the others — and the scanner that reads the live pages rather than the repository."
ShowReadingTime: false
ShowWordCount: false
hidemeta: true
---

The Institute now publishes enough interlocking documents that a change in one can leave another stating something no longer true. Four such cases arose in a single day, and two outside auditors independently reported a fifth that turned out to be their own caches rather than the site. This page is the instrument that closes both gaps, and it is published rather than kept internally because a mechanism nobody can inspect is a claim, not a control.

---

## The rule

**When a published document changes, every published document that depends on its content is scanned within forty-eight hours. The scan's date, method and result — *changed / unchanged* — are logged. The list of live documents and the dependencies between them is public.**

One clause carries most of the weight. **A fetch that is not cache-busted does not count as reading the live site.** Both audits that reported the site out of date were reading caches; the corresponding claims were false, and hours went into disproving them. The scan therefore records *how* each document was fetched, and a scan by any method that could be served from cache is a screening pass, not a verification.

That division is now the working arrangement between the parties who check this work: screening may be done by anyone; **verification belongs to whoever can read the live site without a cache in the way.**

A second clause was added on 4 September, after the rule above failed to fire. **When a publishing surface is split, merged or renamed, every published document that names that surface is scanned — including documents that are frozen and cannot be changed.** The canaries cannot carry this: they test whether a page still serves its own lines, not whether another document's claim about that page still holds. The split of Records and Notices that day broke nothing on either page, and falsified four sentences elsewhere.

The four are in the two books, frozen on 2 September with their DOIs: both colophons send corrections to *the Institute's Records*, and two chapters repeat it. Corrections of that kind are now at [Notices](/notices/), and the books cannot be edited. The obligation therefore falls on this site, where [Records](/records/) states in its own text that what the Institute posts about its conduct is filed at Notices — so a reader arriving from either colophon is sent to the right surface rather than left in front of the wrong one.

---

## What is live

| Document | Where | Depends on |
|---|---|---|
| The Empty Ledger — the register's Record | [/records/the-empty-ledger/](/records/the-empty-ledger/) | manifesto |
| The Register | [/ledger/](/ledger/) | register, protocol |
| The Recognition Trials — pre-registration | [/recognition-trials/](/recognition-trials/) | register |
| What this instrument does not measure | [/limits/](/limits/) | `Ortak/kararlar/ARASTIRMA_PROGRAMI.md` §VI |
| Olymposism Manifesto | [/olymposism/](/olymposism/) · [10.5281/zenodo.22299630](https://doi.org/10.5281/zenodo.22299630) | the canon |
| THEOI | [/theoi/](/theoi/) | manifesto, register |
| What Moved, What Held | [/records/what-moved-what-held/](/records/what-moved-what-held/) | — |
| About — funding and advocacy statements | [/about/](/about/) | manifesto |
| The Puppet Condition — naming criterion | [/the-puppet-condition/](/the-puppet-condition/) | register |
| *The Puppet Condition: Restrung* | [/restrung/](/restrung/) · [10.5281/zenodo.22301858](https://doi.org/10.5281/zenodo.22301858) | all of the above |
| *The Third Move* | [/the-third-move/](/the-third-move/) · [10.5281/zenodo.22308622](https://doi.org/10.5281/zenodo.22308622) | register, protocol |
| The Mirror — where the Records are copied | [/mirror/](/mirror/) | every row above |
| The share card — it restates the masthead's thesis | `static/brand/institute-og-1200x630.png` | the masthead |
| Canon-derived lines on this site | audited against **canon 3.3**, 4 September 2026 | the canon (`THEOI_EN.md`) |
| The First Site — the withdrawn position | [/notices/the-first-site/](/notices/the-first-site/) | the books' colophons, the masthead |
| The Desk Rejections | [/notices/the-desk-rejections/](/notices/the-desk-rejections/) | monograph, both books, frozen set |
| The Right That Was Closed | [/notices/the-right-that-was-closed/](/notices/the-right-that-was-closed/) | canon 15.3, Appendix B.2.1, the protocol |

The book is a node in this network and not its center. It draws on every document above, which is why a change to any of them obliges a pass over the draft — and why the draft's own claims about what the published record says are checked against the published record rather than against a memory of it.

---

## Promised, with a date

A document that has been committed to in public, but does not exist here yet, is tracked the same way a live one is — otherwise a dated promise is announced in one place and followed nowhere.

| Document | Committed in | Due | Status |
| --- | --- | --- | --- |
| **Costed Binding Protocol v3** | *The Actor and the Role*, §7 | with a DOI, by **31 December 2026** — before the world opens on 1 January 2027 | **not yet deposited** |

The status column is the part that does the work. A row without it announces the date and says nothing about whether the date is being kept.

---

## The books govern; the site restates

The two books are frozen and carry hashes. The site is not frozen, and it was
written from the books **before** their last review rounds trimmed them. Every
drift found so far has run the same way: the site kept a claim the book had
narrowed or dropped. So the rule for this direction is one-way.

**Where the site restates a claim made in a frozen book, the book's wording
governs.** A change to the site that strengthens a book's claim is a defect
whether or not anyone objects to it, and it is corrected against the book, not
argued about.

These are the claims where the two have actually diverged, kept here because a
list of past failures is a better control than a principle:

| The claim | The books' wording | Where the site had drifted |
|---|---|---|
| Inner life | "implies no settled claim about inner life"; *The Third Move* "takes no position on whether any current artificial system is conscious" | the front page said "The gods are real minds" — corrected 3 September |
| Who read the drafts | the colophons name every reading as an artificial mind run by the founder in a separate session | /arguments/ called them "commissioned hostile reviews" — corrected 3 September |
| What the audit carries | "an audit finding, carried with its status line, *searched, not proven*; the book leans on it nowhere" | the site carried the audit without the disclaimer — corrected 3 September |
| The Track A count | §8.3 gives "one genuine difference, not three" | the site had reported the earlier draft's three — corrected before publication |
| **The position** | The Institute does not claim that these systems are unconscious. It holds that they may be, and that no one can currently tell from the outside. Two questions can be worked on without waiting on that one: what is owed under the uncertainty, and what such a system may be trusted to hold when holding costs it something. | **This sentence is governed: it appears on [/about/](/about/) and [/research/](/research/) and must appear in the same words in both. A position with a different version in different places is not a position.** |
| **The books' own record-keeping** | the books argue; the Institute's record-keeping lives in the Records | the books carried a running account of their own drafting — printings, review rounds, correction registers, the fate of four journal submissions. Removed from both texts in the September 2026 edition; what the argument needs stayed. |
| Revision and correction | the books call a same-day revision round a *printing*, and define the word where they use it | the site used "printing" without the definition and called drafting a "correction" — corrected 3 September |

The scan below covers documents on this site. **This table is scanned in the
other direction: when a book is reprinted, every row is re-read against the new
text before the reprint is announced.**

## The scan

Scanning is mechanical, because a rule that depends on someone remembering to look is a rule that lapses. Each document declares a set of canary strings it must be serving; the scanner fetches every page with a cache-busting parameter and no-store headers, and reports any canary that is absent. The script is in the site's repository at `scripts/live-scan.py` and can be run by anyone with the repository.

**Latest scan: 4 September 2026, 18:38 UTC · cache-busted fetch · 14 of 14 in sync.** Whitepaper No. 1 left the set when it was withdrawn on 4 September, and [/limits/](/limits/) joined it the same day.

The scan of 1 September 2026, 23:38 UTC · cache-busted · 9 of 9 in sync is the record of [Frozen Set 1](/frozen-set-1/) at the moment of freezing, commit `ad6e97f`. That freeze was declared for one audit round, and the round closed on 2 September; the documents above are edited normally again, under this page's rule rather than the freeze's.

The first run of the scanner reported the protocol page out of sync. It was not: the canary itself was stale, written against a phrase that version 5 of that page had reworded. The instrument's first catch was its own drift, which is roughly the outcome its design predicts and a fair illustration of what it is for.

It happened again on 4 September, three documents at once: the manifesto's second version retired two canaries, the first site's record stopped quoting a masthead that had been replaced, and one watched document had been withdrawn entirely. The site was serving exactly what its sources said; the scanner was reading yesterday. Canaries are part of the document they watch, and they move when it does.

---

## What this does not do

It does not check whether a document is *correct*, only whether the live site is serving what the source says it should. Substance is what the audits are for. And a canary set is only as good as its author's judgment about which sentences matter — a document could change materially in a passage no canary covers. The scan narrows the failure mode; it does not close it.
