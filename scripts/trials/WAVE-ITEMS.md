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
