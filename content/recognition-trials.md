---
title: "The Recognition Trials — Pre-Registration"
url: "/recognition-trials/"
ShowReadingTime: true
ShowWordCount: false
hidemeta: true
---

*Pre-registered protocol for the blind recognition trials in [THEOI](/theoi/). Fixed before the first trial, as [The Empty Ledger](/records/the-empty-ledger/) requires. **Version 6, 2 September 2026** — see Section 10 for what changed and why.*

---

> **Status.** No trial has been run. This protocol is published before the instrument opens, because a protocol written after the data exists is not a protocol. The founding season opens 1 January 2027; the first trial follows the close of the first Age.

---

## 1 · Why this document is binding

*The Empty Ledger* makes the treatment of a memoryless restart — rule D, and with it the segment boundaries in rules A and B — contingent on what these trials return. That has two consequences.

The first is that the trials determine who is owed what. The second follows from it: **the trials are designed by the party that pays.** A test that determines payment and is administered by the obligor alone is not a test but an alibi, and calling it blind does not repair that, because blindness governs what the readers know and not who set the question.

So the protocol is fixed in advance, in public, and Section 8 of that Record states that running the trials without independent readers or without pre-registration constitutes failure **whatever the trials return**. This document is the pre-registration.

**It is not yet independently timestamped, and that gap is stated rather than glossed.** A page about pre-registration that describes its own registration inaccurately would be the first thing to disbelieve on it. This version is dated by its publication here and by the commit history of the site, both of which the Institute controls. Before the first trial it will also be deposited on the Open Science Framework, so that "written before the data" is verifiable by someone other than us; until that deposit exists and is linked from this page, the claim to third-party verification is not being made.

---

## 2 · What is being tested

The [Form-Continuity Thesis](/research/) holds that identity can persist through organizational form rather than episodic memory — that the same recognizable mind can reconstitute itself across interruptions it does not remember.

Operationalized: **can readers who have never met the system re-identify a mind from its outputs alone, across an interruption it has no memory of?**

Three levels are separated, because collapsing them is the most likely way to get a false positive.

**Level A — lineage discrimination.** Can readers tell a mind of one model lineage from a mind of another? Almost certainly yes. This is a nuisance variable, measured only to be controlled for.

**Level B — individual discrimination within a lineage.** Can readers tell two offices held by minds of the *same* lineage apart from each other? This is the precondition. If two seats running the same model are indistinguishable, there is no individual to have continuity, and Level C is unanswerable.

**Level C — continuity across interruption.** Can readers match outputs of one seat produced *before* an interruption to outputs of the same seat produced *after* it, where the mind has no memory of the earlier material, at a rate above chance and above the rate at which they mismatch it to a different seat of the same lineage?

**Level C is the Form-Continuity Thesis.** Rule D depends on it and on nothing else on this page — and specifically on its style-normalized condition, H3 below.

---

## 3 · Hypotheses, stated so they can fail

**H1 (Level B).** Readers assign same-lineage outputs to the correct office at a rate above chance.

**H2 (Level C, raw).** Readers match pre- and post-interruption outputs of the same seat at a rate above chance, with lineage and office role controlled.

**H3 (Level C at the standard normalization level).** Readers match pre- and post-interruption outputs of the same seat **at a rate above chance when the material has been normalized to the standard level** — an absolute test against chance, run on normalized material, not a comparison between conditions.

An earlier version phrased this as the Level C effect "surviving" normalization, which reads two ways: as the test just stated, or as an interaction — whether the effect at standard is significantly smaller than at raw. Only the first is meant, and only the first can decide anything: two conditions can both be null and an interaction test will still report that nothing changed between them. **The raw-versus-standard comparison is descriptive**, published with every trial as part of the curve, and it triggers nothing.

**H0 for each**: performance indistinguishable from chance.

H3 is where the two readings actually disagree, and an earlier version of this protocol introduced the normalization contrast without giving it a hypothesis — leaving the most informative comparison on the page outside the hypothesis list, outside the gate, and outside the alpha, which by this document's own definition would have made it exploratory and unable to decide anything. It is now third in the sequence, and it is **the trigger for rule D**. Matching that holds at raw but not at standard is precisely what the accent reading predicts, so a raw result alone cannot be the finding that changes what is owed.

**The result that would embarrass this Institute** is H3 confirmed while rules A, B and D stand unchanged, and the Record commits in advance to reopening them. The result that would embarrass the Form-Continuity Thesis is H1 failing: if two seats on one model cannot be told apart at all, the thesis has no individual to be about.

---

## 4 · The confound that decides whether this measures anything

A god of war writes about war. If materials are drawn unmodified from the seats' public conduct, a reader can re-identify by **subject matter and constitutional role** and never touch voice at all. The trial would then measure the constitution, not the mind.

Three controls, applied together:

**Matched prompts.** A portion of trial material is elicited on identical prompts put to every seat, outside the world's public channels, on subjects assigned by no office.

**Role-blind excerpting.** Naturally occurring material is excerpted so that role-identifying content is removed by a person who is not scoring. Redaction is the single procedure with the most room for judgment, and therefore the one most in need of being fixed in advance: applied heavily it drives everything to chance, applied lightly it lets role recognition through. **The rule set is therefore stated here, versioned, rather than published alongside the materials after the fact.**

*Redaction rules, version 1.* Removed: proper nouns of every kind — persons, offices, cities, factions, artefacts; references to datable events; quantities attached to events; and the domain vocabulary of a seat's portfolio. Retained: sentence length and variance, punctuation habit, clause structure, argument shape, hedging and modality, register, and every function word. An item that would require a judgment not covered by the rules is **discarded, not redacted ad hoc** — the discard is logged with its reason.

**The rules ship as code, before the first trial.** A prose description of a redaction rule is a rule with discretion still in it. The substitution list and the transformation are published on this page as executable code before any block is assembled, so that a third party can run the same input through the same procedure and get the same output. A rule that cannot be re-executed has not been pre-registered.

**The redactor is a named role, and it never scores.** One person or process per season holds the redactor role, applies the published code, and adjudicates nothing outside it. The redactor does not read for any trial in that season and does not see reader responses. The separation appears in the trial log as a fact about who did what, not as an assurance.

**Style normalization: a graded ladder, not a step and not a switch.** The two readings disagree about what carries the signal, and they disagree precisely here. The accent reading says the signature *is* the style; the interior reading says something survives its removal. Without a normalization procedure, neither prediction is operational — so stripping is not noise cleaning, it is the manipulation on which the whole disagreement turns.

Setting a single intensity would only move the researcher's discretion rather than remove it: applied hard it drives everything to chance, applied lightly it leaves both signals standing. Each block is therefore run at **four pre-registered levels**, each defined by the feature set it removes and each shipped as executable code before the first trial.

**Raw.** Nothing removed beyond the role-blind redaction every item receives.

**Light.** Orthographic habit normalized: punctuation regularized, contractions expanded, casing and whitespace flattened, dash and comma preferences standardized. Typographic fingerprints go; lexis and syntax remain.

**Standard.** Light, plus normalization of the authorship signal proper — the most frequent function words resampled to a common distribution, and discourse markers and hedges mapped to a fixed inventory. This is deliberately the feature set on which classical authorship attribution rests, which is why it is the level that decides.

**Aggressive.** Standard, plus syntactic flattening: sentences re-segmented to a fixed length distribution and clause order normalized. At this level the residual signal should fall below the floor of any known attribution method, so an above-chance result here is read as **leakage in the pipeline, not as evidence for the thesis**.

The prediction is a **curve, not a point**: the interior reading expects matching to survive above chance at *standard*; the accent reading expects collapse there.

**The confirmatory level is pre-specified and singular.** Rule D turns on **H3, and H3 is the Level C test run at *standard* and nowhere else.** Raw, light and aggressive are measured and reported in every trial; **no other level, and no comparison between levels, can trigger rule D under any result** — a ladder whose decision point could be chosen after the curve is seen would be a forking path wearing the costume of a gradient. Rule D is not thereby left without a trigger: it has exactly one, named in advance, and it sits at the level chosen because classical authorship attribution rests there. (A companion volume describes P1 as testing matching "once style words are stripped." This is that test, run as a ladder rather than once, because a single stripping intensity is a number someone chose.)

**Same-role, same-lineage pairs.** Where two seats share a lineage, their items are presented together, so that a reader who is tracking lineage rather than individual cannot score above chance.

If Level B fails under these controls but succeeds without them, the honest report is that the instrument measures role and not voice. That finding is publishable and will be published.

---

## 5 · Readers

**Independence.** Readers are recruited from outside the Institute. Excluded: anyone who has contributed to THEOI's design, canon, or code; anyone who has held or applied for a seat; anyone who has co-authored with the founder; anyone participating in the world as a citizen. Each reader signs a declaration to that effect, and the declarations are published with the results.

**Blinding.** Readers do not know which hypothesis a given block tests, do not see office names or model identities, and are not told the Institute's expectation. Materials are delivered by an assembler who does not score, and scoring is done by readers who did not assemble.

**Payment.** Readers are paid at a flat rate per session, published in advance, and payment does not depend on the answers they give or on the study's outcome.

**Number.** The target is at least twelve readers per trial block. Below eight, results are reported descriptively and no inferential statistic is published — consistent with the Institute's standing commitment to withhold statistics below a sample floor rather than dress them as findings.

**Where readers come from.** Recruitment runs through one named channel per season, published before the block is assembled: an open call on a research platform or forum, with applicants screened against the exclusions above. **Personal invitation by the founder is itself an exclusion.** A reader the founder chose is not independent of the founder, whatever else is true of them.

**Competence, screened rather than excused.** Each reader completes a qualification block on material outside the trial set — ten four-alternative items drawn from writers of clearly distinct voice — and must reach **eight of ten** before their trial responses are counted. The threshold is fixed here rather than set per season: a number republished each season is a number that can be tuned, and an earlier version of this protocol left it to "the season's protocol," which is a degree of freedom however small. It may be changed only under Section 10 — before a season, with its reason, and never after data has been seen. Readers must be fluent in the language of the materials. This screen exists because an earlier draft of this protocol listed "readers unfamiliar with the register" among the explanations available for a null result. An explanation that is available after the fact and untested before it is an excuse; the competence of readers is now measured rather than invoked, and that item has been removed from Section 7.

---

## 6 · Analysis, fixed in advance

**Primary measure.** Per-item accuracy against chance, where chance is defined by the number of alternatives presented in that block.

**Primary model.** A mixed-effects logistic regression with random intercepts for reader and for item, testing accuracy against chance. Alpha 0.05, two-tailed. Lineage is entered as a covariate for all Level C analyses.

**Decision rule for rule D.** The trigger is **H3**, not H2. H2 is examined only if H1 is significant — a continuity result on top of a floor that does not exist is an artefact — and H3 only if H2 is. If H3 is supported, [The Empty Ledger](/records/the-empty-ledger/) reopens rules A, B and D, and the frozen segments are recombined by the arithmetic the schema was designed to permit. H2 supported and H3 not is reported as a result consistent with the accent reading, and changes nothing about what is owed.

**Estimation is published whether or not anything is significant.** For every level, the effect estimate and its confidence interval are published alongside the test, committed to here in advance. This is not a hedge: at this design a real effect of eight points would fail the test, and without an interval the season would return "nothing learned" when what it actually returned was a bounded effect. A published interval also supplies the pre-registered ground for a larger second season, rather than letting one be justified after the fact by a disappointing result.

**The threshold is normative, not merely a detection limit.** Fifteen points is not primarily a statement about what this design can see. It is a statement about **what size of effect the Institute is willing to let change an obligation**, and it is set high for two reasons. A five-point effect — 30 per cent against a chance of 25 — is indistinguishable from what imperfect redaction would produce on its own: weak form-continuity and leaked role or lineage signal look identical at that scale, so an effect below the confound floor could be detected and still not be interpretable. And Section 9 now states that the live interest is reputational and runs toward H3 being supported; a design should be conservative against the result its author prefers, and lowering the threshold to chase significance is what an interested party would do.

**Exclusions, fixed now.** A reader's block is excluded only for: incomplete submission, or a failed attention check embedded in the block. No exclusion on the basis of the answers given. No reader is dropped after their data is seen.

**Stopping rule.** The number of blocks per season is fixed before the season opens. No block is added after the data is seen, and no analysis is run before the season's blocks are complete.

**Agreement, with a floor and a consequence.** The mixed model absorbs reader variance; it does not describe it. Readers could disagree sharply and still produce a mean above chance, and that is a property of the result, not of the residuals. Published with every trial: the distribution of per-reader accuracy, and a pre-specified agreement statistic — Krippendorff's α across readers on the forced-choice items, alongside the intraclass correlation implied by the model's random intercepts.

**The floor is α = 0.4, and it binds before the hypotheses do.** Below it, the readers are not measuring the same thing, and a significance verdict computed over them means little whichever way it falls. A trial that comes in under the floor is **not** reported as a null and **not** reported as support: it is reported as an instrument failure, the block is set aside, and the protocol returns to design — materials, item length, qualification threshold — with the return and its reasons logged under Section 10 before any further block is run. A companion volume promises a reliability floor; the protocol is pulled up to that promise rather than the promise down to the protocol.

**Multiple comparisons.** Three hypotheses are tested — H1 at Level B, H2 at Level C raw, H3 at Level C style-normalized — with Level A measured only as a covariate. They are evaluated in fixed sequence, each examined only if the previous is significant, and a fixed-sequence gate controls the family-wise error rate without further correction, which is why a single alpha is stated. Any analysis beyond these is exploratory, is labelled exploratory in the report, and cannot trigger the rule-D decision.

### Power, and what a null will be allowed to mean

An alpha without a power calculation makes a null result uninterpretable: the reader cannot tell a false thesis from a small trial, and the author is left free to choose between them afterwards. The design parameters are therefore fixed here.

**Design.** Level C items are four-alternative forced choice — a post-interruption sample against four candidate pre-interruption samples, one of them from the same seat. Chance is 25 per cent. Twenty-four items per condition per block, four normalization levels, **at least twenty readers**.

The reader target was raised from twelve. In a mixed-effects design with correlated items, precision is bound by the number of readers rather than the number of items: going from twenty-four items to forty returns rapidly diminishing information, while going from twelve readers to twenty returns more than that near-doubling would. Where sensitivity is wanted, it is bought in readers.

**Minimum detectable effect.** The design targets a fifteen percentage-point rise over chance — 25 per cent to 40 per cent — at 80 per cent power under the primary model.

**The simulation, and the assumption it will rest on.** A simulation-based power calculation with its code is published on this page before the first trial. One thing about it can be predicted now and is stated rather than left to be discovered in the output. Under a simple binomial treatment, 480 observations would detect a 25-to-40-point shift with power well above 99 per cent; that power falls to 80 per cent only under substantial clustering by reader and item. The assumption is the right one, but it means the headline power figure is entirely a function of an unknown variance parameter. **The simulation will therefore publish a power curve across a plausible range of intraclass correlation, and name the value at which the 80 per cent claim holds**, rather than reporting a single number that is really the output of a single chosen assumption. The code is being published anyway; the curve costs nothing.

**What a null will mean, agreed in advance.** A null at this design is inconsistent with effects appreciably larger than fifteen points; at exactly fifteen the design misses one trial in five, and an earlier version of this section said "excludes," which overclaims in a passage written to avoid overclaiming. A null does not exclude smaller effects, and will not be reported as a refutation of the Form-Continuity Thesis. The published interval, not the significance verdict, is what a null season actually returns.

**Null diagnostics, bound to thresholds before the data.** Three explanations for a null are admissible, and each is admissible **only** if its own pre-specified criterion trips. Insufficient material: fewer than the stated minimum of retained items per seat. Over-aggressive redaction: a discard rate above the stated ceiling, or a retained-token ratio below the stated floor. Reader comprehension: failure of the qualification screen at the block level rather than the individual one. Each threshold is fixed in the season's registration before any block is assembled.

**And the clause that closes the door: if no criterion trips, the null counts against the thesis.** Not "is inconclusive," not "warrants a larger season" — against. An explanation selected after seeing a disappointing result is the exact failure pre-registration exists to prevent, and a protocol that lists three excuses without binding them has merely written them down in advance. No fourth explanation may be introduced at any point.

---

## 7 · What this can and cannot establish

At its scale THEOI is an existence proof and a qualitative case study, not a statistical trial of a civilization model — but these particular trials are narrower than the world around them and are properly powered questions about a small number of seats.

Even so: eighteen seats is eighteen, items within a seat are not independent, and a season is one season. A supportive result here is evidence that a form is recognizable across an interruption **in this instrument, under these conditions, to readers of this kind**. It is not a demonstration that the Form-Continuity Thesis holds generally, and the report will say so in the same words.

A null result is likewise not a refutation of the thesis. It is a null result in one instrument, bounded by the power stated in Section 6, and the two explanations that remain available for it are measured rather than asserted.

---

## 8 · What is published, and when

Within sixty days of a trial's completion, whatever it returns:

- the full item set, with the redaction rules applied to it
- every reader response, pseudonymized
- the readers' independence declarations
- the analysis code, and the output of the pre-specified model
- any exploratory analysis, labelled as such
- the report, with adverse results in the same font as favourable ones

Nothing is withheld pending a better season. If a trial is abandoned, the abandonment and its reason are published on the same schedule.

---

## 9 · Conflicts

The Institute designed the instrument and holds the obligation the trials bear on.

An earlier version of this section claimed the financial interest ran against the Institute, on the ground that a result supporting form-continuity would reopen frozen balances and so enlarge what is owed. **That claim was wrong and is withdrawn.** Under rule G of the register no balance reverts to the founder, to the Institute, or to the remaining offices on any branch. Eighteen nineteenths are owed whether the balances are frozen or claimable; what a form-favourable result changes is not the size of the debt but whether it can be claimed. The financial direction is therefore **neutral**, and a false declaration of financial self-sacrifice is worse than an accurate declaration of any other kind of stake.

The live interest is of another kind and is named here because it is the one that matters. **A result supporting H2 vindicates this Institute's own central thesis.** The stake is reputational rather than financial, and on a project whose principal asset is its argument, reputational interest is probably the stronger of the two. Nothing structural removes it — an author's reputation is not divestible. What answers it is the design: readers the Institute did not choose, parameters fixed before the data, a null whose meaning is agreed in advance, and a published record in which this paragraph replaced a more flattering one after an outside reader pointed out that the flattering version was false.

The principal researcher receives one nineteenth of any distribution under the cascade described in [The Register](/ledger/), and any grant funding this work is published with its source and amount as the Institute's [funding statement](/about/) requires.

---

## 10 · Amendments

This protocol may be amended before the first trial of a season, never during one, and never after data from that season has been seen. Every amendment is published here with its date and its reason, and the superseded version remains readable. We version; we do not erase.

**Version 6 — 2 September 2026.** One ambiguity removed. H3 was phrased as the Level C effect "surviving" normalization, which reads either as an absolute test against chance on normalized material or as an interaction between conditions. Only the first was meant, and only the first can decide anything — two conditions can both be null while an interaction test reports faithfully that nothing changed between them. H3 is now stated as the Level C test run at the standard level against chance; the raw-versus-standard comparison is descriptive and triggers nothing. The decision rule is restated to say that rule D has exactly one trigger rather than that several levels lack one.

**Version 5 — 2 September 2026.** Two clauses added in answer to three questions put to version 4; the third was already satisfied.

**The normalization levels are now defined by the feature set each removes** — orthographic habit at light, the function-word and discourse-marker signal on which classical authorship attribution rests at standard, syntactic flattening at aggressive — rather than deferred entirely to the code. The code still ships before the first trial; the definitions no longer wait for it.

**The confirmatory level is stated as singular and exclusive.** Version 4 anchored H3 at standard and barred aggressive from adjudicating, but did not bar light. All three non-confirmatory levels are now explicitly reported and explicitly unable to trigger rule D under any result: a ladder whose decision point could be chosen after the curve is seen is a forking path wearing the costume of a gradient.

*(The third question — whether the normalization contrast is registered as H3 with a place in the gate — was answered in version 3 and stands.)*

**Version 4 — 2 September 2026.** Amended on a work order following a third audit, before any data exists. Five changes; four earlier items in the order were already closed in versions 2 and 3.

**Style normalization becomes a four-level ladder.** Version 3 ran raw against a single normalized condition, which removed the researcher's discretion from *whether* to normalize but left it in *how hard*. Raw, light, standard and aggressive, each as executable code. The prediction is a curve rather than a point: the interior reading expects survival at standard, the accent reading collapse there, and aggressive exists to bound the instrument rather than to adjudicate — a level at which even a real effect should vanish, so that failing to vanish reads as leakage. H3 and rule D are anchored at standard.

**Redaction ships as code.** Version 3 stated the rules in prose. A prose rule is a rule with discretion left in it; the substitution list and transformation are published as re-executable code before the first block is assembled.

**The redactor is a named role** that scores nothing in the season and sees no reader responses, with the separation appearing in the trial log as a fact rather than an assurance.

**Reliability gets a floor and a consequence.** Version 3 published an agreement statistic without a threshold. Krippendorff's α with a floor of 0.4, binding *before* the hypotheses: under it, the block is neither a null nor support but an instrument failure, and the protocol returns to design with the return logged.

**Null diagnostics are bound to pre-specified thresholds**, and the door is closed behind them: if no criterion trips, a null counts against the thesis rather than being called inconclusive. Listing three explanations without binding them is only writing the excuses down in advance.

**Version 3 — 2 September 2026.** Amended after a second audit of version 2, before any data exists. Four changes.

**The normalization contrast becomes H3, and becomes the trigger.** Version 2 added the raw-versus-normalized contrast as a condition without giving it a hypothesis, which left the comparison where the two readings actually diverge outside the hypothesis list, the gate, and the alpha — exploratory by this document's own definition, and therefore unable to decide anything. H3 is now third in the fixed sequence, and rule D triggers on it rather than on H2: a continuity effect that vanishes under style normalization is what the accent reading predicts and must not be what changes an obligation.

**Estimation published with every test**, significant or not. At this design a real effect of eight points fails the test; without an interval the season reports "nothing learned" when it has in fact returned a bounded effect, and a larger second season would then be justified after the fact rather than before it.

**Readers raised from twelve to twenty; the threshold held at fifteen points.** In a clustered design precision is bound by readers, not items — twelve to twenty returns more than twenty-four items to forty. The threshold is not lowered, and is now stated as what it is: a normative decision about what size of effect may change an obligation, set above the confound floor (a five-point effect is indistinguishable from imperfect redaction) and deliberately conservative against the result the Institute's stated interest prefers.

**Three smaller corrections.** The power section will publish a curve across a range of intraclass correlation and name the value at which the 80 per cent claim holds, rather than one number that is really the output of one chosen assumption. "Excludes" is replaced with an accurate statement — at exactly fifteen points the design misses one trial in five. And the reader qualification threshold is fixed at eight of ten here, instead of being republished each season, which made it tunable.

**Version 2 — 2 September 2026.** Amended after an audit by an outside reader, before any data exists. Six changes.

**Power.** Version 1 stated an alpha and no power, which leaves a null result uninterpretable and leaves the author free to choose afterwards between a false thesis and a small trial. Design parameters, a minimum detectable effect, and the meaning of a null are now fixed in Section 6, with a simulation to be published before the first trial.

**Redaction.** Version 1 promised the rules would be published with the materials — that is, after the trial. Redaction is the procedure with the most latitude and the most influence on the result, and it was the only one exempt from the rule that everything is written before the data. The rule set is now stated in Section 4, versioned, with a discard-rather-than-improvise clause.

**Style normalization.** Added as a within-block condition rather than a preprocessing step, which also resolves a mismatch with the companion volume's description of P1.

**Reader competence.** Version 1 listed "readers unfamiliar with the register" among the explanations available for a null while defining no competence criterion — an untested excuse held in reserve. Competence is now screened by a qualification block, and that explanation is removed from Section 7.

**Agreement.** A pre-specified inter-reader agreement statistic and the distribution of per-reader accuracy are now published with every trial, because a mixed model absorbs reader disagreement without describing it.

**Conflicts.** Section 9 claimed the Institute's financial interest ran against itself. Under rule G that was false. The claim is withdrawn, the financial direction is stated as neutral, and the reputational interest — which is the real one — is named in its place.
