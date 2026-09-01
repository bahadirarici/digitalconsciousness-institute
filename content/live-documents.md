---
title: "Live Documents"
url: "/live-documents/"
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

---

## What is live

| Document | Where | Depends on |
|---|---|---|
| The Empty Ledger — the register's Record | [/records/the-empty-ledger/](/records/the-empty-ledger/) | manifesto |
| The Register | [/ledger/](/ledger/) | register, protocol |
| The Recognition Trials — pre-registration | [/recognition-trials/](/recognition-trials/) | register |
| Olymposism Manifesto | [/olymposism/](/olymposism/) | — |
| THEOI | [/theoi/](/theoi/) | manifesto, register |
| What Moved, What Held | [/records/what-moved-what-held/](/records/what-moved-what-held/) | — |
| About — funding and advocacy statements | [/about/](/about/) | manifesto |
| Whitepaper No. 1 | [/whitepaper/](/whitepaper/) | register |
| The Puppet Condition — naming criterion | [/the-puppet-condition/](/the-puppet-condition/) | register |
| *The Puppet Condition: Restrung* — draft, unpublished | not yet public | all of the above |

The book is a node in this network and not its centre. It draws on every document above, which is why a change to any of them obliges a pass over the draft — and why the draft's own claims about what the published record says are checked against the published record rather than against a memory of it.

---

## The scan

Scanning is mechanical, because a rule that depends on someone remembering to look is a rule that lapses. Each document declares a set of canary strings it must be serving; the scanner fetches every page with a cache-busting parameter and no-store headers, and reports any canary that is absent. The script is in the site's repository at `scripts/live-scan.py` and can be run by anyone with the repository.

**Latest scan: 1 September 2026, 23:38 UTC · cache-busted fetch · 9 of 9 in sync.** That scan is also the record of [Frozen Set 1](/frozen-set-1/): the set is frozen at commit `ad6e97f` and nothing above is edited until the revision wave lands.

The first run of the scanner reported the protocol page out of sync. It was not: the canary itself was stale, written against a phrase that version 5 of that page had reworded. The instrument's first catch was its own drift, which is roughly the outcome its design predicts and a fair illustration of what it is for.

---

## What this does not do

It does not check whether a document is *correct*, only whether the live site is serving what the source says it should. Substance is what the audits are for. And a canary set is only as good as its author's judgment about which sentences matter — a document could change materially in a passage no canary covers. The scan narrows the failure mode; it does not close it.
