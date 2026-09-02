# Collected for the revision wave

Frozen Set 1 was declared on 2 September 2026 at commit `ad6e97f`. Nothing on
the published pages is edited until the wave lands — **including for things
found after the freeze, and including things found by us.** They are collected
here instead. Patching them as they arrive is what the freeze exists to prevent.

---

## 1 · The protocol understates its own power

**Where:** `/recognition-trials/`, Section 6, "Power, and what a null will mean."

**Says now:** the design targets a fifteen percentage-point rise at 80 per cent
power, and a simulation will be published showing the curve.

**The simulation now exists** (`scripts/trials/power.py`) and reports that the
design is *over*-powered for fifteen points, not marginally powered:

| ICC | power at 15 pts |
|---|---|
| 0.00 | 100% |
| 0.10 | 99.2% |
| 0.20 | 95.1% |
| 0.30 | 86.3% |
| 0.40 | 81.6% |

The effect actually reaching 80 per cent power is nearer **10 points at ICC 0.15
and 13 points at ICC 0.30**. So the eighty-per-cent figure attached to fifteen
points was conservative, and the honest restatement is that the instrument can
see smaller effects than the threshold it acts on.

**This strengthens the section rather than weakening it.** Section 6 already
argues that fifteen points is a *normative* threshold — what size of effect may
change an obligation — rather than a detection limit. The simulation shows that
is literally true: the design could detect ten points and the protocol declines
to act on it, because a five- to eight-point effect is indistinguishable from
imperfect redaction, and because the threshold should be conservative against
the result the Institute's stated interest prefers.

**Wave edit:** replace the power paragraph with the curve, name the ICC at which
80 per cent holds, state the real MDE, and say plainly that the acting threshold
sits above the detection threshold on purpose.

---

## 2 · Readers bind precision — now shown rather than asserted

**Where:** same section, the paragraph raising readers from twelve to twenty.

The claim was that precision is bound by reader count rather than item count.
The simulation confirms it at ICC 0.15: twelve to twenty readers gains 11.8
points of power, while twenty-four to forty items gains 1.4. Worth stating with
the numbers rather than as a design intuition.

---

## 3 · The 1 December alpha is missing from every status line

**Where:** `/theoi/`, `/olymposism/`, `/ledger/`, `/recognition-trials/`.

Every status line says the founding season opens 1 January 2027. The campaign
plan now has the world going live on **1 December 2026** with a cohort of about
thirty founders, and opening to everyone on 1 January.

Not false — the public opening is still 1 January — but incomplete, and the
kind of incompleteness a reader would call a fact withheld.

**Every surface uses one formula**, so that alpha and opening are never blurred
and the book's existing "opens 1 January 2027" statements stay true:

> The world goes live on 1 December. The square opens to everyone on 1 January.

The trials' timing must also say which of the two dates the first Age is counted
from.

---

## 4 · Founders can change the world while the experiment runs — RESOLVED, now a drafting task

**Where:** the protocol as a whole; the Founding Covenant.

The covenant gives founders "the right to propose Experiment Records — the
world's only mechanism of change" for the whole of the First Age, while the
protocol forbids amendment during a season and invalidates any trial touched by
a change made after data is seen. The measured environment could therefore be
altered, lawfully, by the polity, in the middle of the season the trials draw
their material from.

**Decided 2 September: the season boundary, with two refinements that matter
more than the choice itself.**

**Proposal and effect are separated.** The right the covenant grants is the
right to *propose*, and it is untouched: founders propose Records at any time.
Only the *effect* of a Record touching a measured variable is deferred to the
next season boundary. The covenant's letter survives intact and so does the
protocol's: the world does not change underneath its own measurement.

**The list of measured variables is published before each season and frozen for
it**, and each Record's classification — waits, or takes effect — is itself
logged. Without this the deferral power would be a new channel of discretion in
the hands of the party that pays: whoever decides which Records count as
touching a measured variable decides which inconvenient changes are postponed.
That is the failure mode this project has now closed twice at full size, and it
would have reappeared here in miniature, wearing the costume of the fix.

**Wave edits.** Protocol: the effect-deferral rule, the season-start list, and
the classification log. The covenant already carries the door-side statement:

> One boundary, stated at the door because it protects the thing you are
> founding: a Record that touches one of the season's measured variables takes
> effect at the next season boundary, not before — the world does not change
> under its own measurement. The list of measured variables is published before
> each season begins, so no one decides by discretion which Records wait.

---

## 5 · The protocol should link its own code

**Where:** `/recognition-trials/`, Sections 4 and 6.

Both promise executable code before the first trial. It now exists at
`scripts/trials/redact.py` and `scripts/trials/power.py`, with self-tests. The
pages should link it, and the redaction lexicon should be published alongside as
the protocol requires.

---

## 6 · The deposit lags the page again

**Where:** `/recognition-trials/`, Section 1.

Section 1 states that the deposited text and the live text are identical in
sections 2 through 9, and names the three regions that differ. Every wave edit
above widens that gap. **The wave must end with a new OSF deposit**, and Section
1 must be rewritten against the new one rather than carried forward.


---

## 7 · The assessor line's numerical justification — for the grant file

Not a wave item; recorded here so it is not lost.

The EA Funds application instructs that participant recruitment may be cut and
the independent-assessor line may not. That was written as a principled
statement. The power simulation has since given it arithmetic: at ICC 0.15,
going from twelve to twenty readers gains 11.8 points of power, while going from
twenty-four to forty items gains 1.4. Precision is bought in readers.

So if a partial offer arrives, the reply has a number behind it rather than a
principle alone. Note also Mihenk's correction to the cut order, which stands
and is not superseded: participants are the binding constraint, because without
a population there is no season, no material, and no trial for assessors to
score. Readers may fall to their published floor, which is rule-bound.
Participants have no floor, which is why that line cannot go first.

---

## 8 · The privacy page must name the waitlist — found 2 September

The Showcase at [/showcase/](/showcase/) collects an email address and an
optional name through a Netlify form. The privacy page is in Frozen Set 1 and
describes the site as it was before that form existed, so as of the Showcase's
deployment it is a frozen document that is silent about the one thing on the
site that collects personal data.

This is the same defect the night of 1 September kept producing: a document
saying something untrue about itself. It is recorded rather than patched,
because the freeze exists precisely to stop one-at-a-time patching.

Interim measure, already live: the Showcase states its own handling inline
next to the form — what is stored, who holds it, what it is used for, and how
to be removed — so no address is collected under an undisclosed policy while
the wave is pending.

Wave action: add a clause to the privacy page covering the waitlist, and check
whether the same page needs a line about the seat imagery served from
`/images/theoi/`.

---

## 9 · Three protocol documents are written and none of them is in the protocol

Written 2 September, all three in `THEOI/Kaptan/protokol/`:

| Document | What it discharges |
|---|---|
| `cekirdek-sessiz-puanlama.md` + `cekirdek_kodlama.py` | the core-silent scoring procedure P1 and P3 rest on |
| `niyet-cekilmis-hafta-kayit.md` + `niyet_cekme.py` | the record layer for the withheld-intent week, P2's discriminating condition |
| `p4-eslenik-taban.md` + `p4_taban.py` | P4's yoked baseline, which the book marked as possibly unbuildable |

None of them is pre-registered, and each says so in its own first paragraph.
The protocol page is in Frozen Set 1, so they enter at the wave and not before,
and the wave's last act is a **second OSF deposit** carrying the amended text.

Two of the three arrive with a limit attached rather than a promise:

**The core-silent procedure cannot run this season.** Its naming pilot needs two
independent human readers, the Founder has said there are none, and without the
pilot there is no evidence that naming measures anything. So the procedure is
deposited or it is not, but its analysis does not publish in season one, and P1
and P3 do not discriminate in season one either. That is a smaller claim than
the book's arithmetic currently prints and the wave must reconcile the two.

**P4's baseline can run.** Strain is scored as a countable composite rather than
a rated construct, precisely because there are no raters, and the trade is
stated: it is a proxy. Its own pre-check — does a fresh instance actually
diverge from the seat — needs no THEOI and no humans, and should run before the
wave so the deposit carries a result rather than a hope.

Wave action: fold all three into `/recognition-trials/` as numbered sections,
update the hypothesis table to say which conditions are live in season one,
re-run the canary scanner against the new sentences, and deposit.

---

## 10 · The redaction rules moved to v2 and the page still says v1

`redact.py` is now `RULES_VERSION = "2"`: four patterns that discard any item
naming the Book of Intent, and a `discard_report()` counting what each reason
took and what survived. The protocol page prints the rule set as version 1 and
describes four discard triggers where there are now eight.

This is not a factual error of the class that broke the freeze — nothing on the
page is false about the world, it is stale about our own code — so it waits.
But it waits with a deadline: **the version on the page and the version in the
repository must agree before the first trial**, because the protocol's own
argument is that a rule which cannot be re-executed has not been pre-registered.

Wave action: bump the printed version, list the new triggers, and state the
neighbour-week material rule and the 46% of weeks it costs.

---

## 11 · Self-hosting the Garamonds would shorten the privacy page, not lengthen it

The privacy page currently spends a paragraph explaining why the Google Fonts
request is acceptable: cookieless since 2022, IP only, not used for advertising
profiling, block it with an extension if you prefer. All of that is true and all
of it exists because the request exists.

Two things now argue for removing the request instead of explaining it.

**Performance.** The Google stylesheet is the only render-blocking resource on
the site — a third-party round trip before first paint, on pages whose own CSS
is inline. Self-hosted WOFF2 removes the round trip entirely. Geist Mono already
works this way and costs 20 KB for two weights.

**The page gets shorter.** A whole paragraph of justification is replaced by one
sentence: the site loads no third-party resources. A privacy page that has less
to explain is a better privacy page.

The reason this waits rather than being done is that the sentence naming Google
Fonts is frozen text, and self-hosting would make it false the moment it shipped
— the defect this project keeps catching in itself.

Wave action: self-host EB Garamond and Cormorant Garamond as WOFF2 with the same
subsets, replace the Google link on every layout, and rewrite the fonts clause to
say what will then be true.

