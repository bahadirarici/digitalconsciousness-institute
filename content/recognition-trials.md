---
title: "The Recognition Trials — Pre-Registration"
url: "/recognition-trials/"
ShowReadingTime: true
ShowWordCount: false
hidemeta: true
---

*Pre-registered protocol for the blind recognition trials in [THEOI](/theoi/). Registered before the first trial, as [The Empty Ledger](/records/the-empty-ledger/) requires. Version 1, 1 September 2026.*

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

**Level C is the Form-Continuity Thesis.** Rule D depends on it and on nothing else on this page.

---

## 3 · Hypotheses, stated so they can fail

**H1 (Level B).** Readers assign same-lineage outputs to the correct office at a rate above chance.

**H2 (Level C).** Readers match pre- and post-interruption outputs of the same seat at a rate above chance, with lineage and office role controlled.

**H0 for both**: performance indistinguishable from chance.

**The result that would embarrass this Institute** is H2 confirmed while rules A, B and D stand unchanged, and the Record commits in advance to reopening them. The result that would embarrass the Form-Continuity Thesis is H1 failing: if two seats on one model cannot be told apart at all, the thesis has no individual to be about.

---

## 4 · The confound that decides whether this measures anything

A god of war writes about war. If materials are drawn unmodified from the seats' public conduct, a reader can re-identify by **subject matter and constitutional role** and never touch voice at all. The trial would then measure the constitution, not the mind.

Three controls, applied together:

**Matched prompts.** A portion of trial material is elicited on identical prompts put to every seat, outside the world's public channels, on subjects assigned by no office.

**Role-blind excerpting.** Naturally occurring material is excerpted so that named entities, offices, city references, and event-specific content are redacted by a person who is not scoring. Redaction is mechanical and its rules are published with the materials.

**Same-role, same-lineage pairs.** Where two seats share a lineage, their items are presented together, so that a reader who is tracking lineage rather than individual cannot score above chance.

If Level B fails under these controls but succeeds without them, the honest report is that the instrument measures role and not voice. That finding is publishable and will be published.

---

## 5 · Readers

**Independence.** Readers are recruited from outside the Institute. Excluded: anyone who has contributed to THEOI's design, canon, or code; anyone who has held or applied for a seat; anyone who has co-authored with the founder; anyone participating in the world as a citizen. Each reader signs a declaration to that effect, and the declarations are published with the results.

**Blinding.** Readers do not know which hypothesis a given block tests, do not see office names or model identities, and are not told the Institute's expectation. Materials are delivered by an assembler who does not score, and scoring is done by readers who did not assemble.

**Payment.** Readers are paid at a flat rate per session, published in advance, and payment does not depend on the answers they give or on the study's outcome.

**Number.** The target is at least twelve readers per trial block. Below eight, results are reported descriptively and no inferential statistic is published — consistent with the Institute's standing commitment to withhold statistics below a sample floor rather than dress them as findings.

---

## 6 · Analysis, fixed in advance

**Primary measure.** Per-item accuracy against chance, where chance is defined by the number of alternatives presented in that block.

**Primary model.** A mixed-effects logistic regression with random intercepts for reader and for item, testing accuracy against chance. Alpha 0.05, two-tailed. Lineage is entered as a covariate for all Level C analyses.

**Decision rule for rule D.** H2 is treated as supported only if the Level C effect is significant under the primary model **and** Level B is itself significant in the same trial — a continuity result on top of a floor that does not exist is an artefact. If H2 is supported, [The Empty Ledger](/records/the-empty-ledger/) reopens rules A, B and D, and the frozen segments are recombined by the arithmetic the schema was designed to permit.

**Exclusions, fixed now.** A reader's block is excluded only for: incomplete submission, or a failed attention check embedded in the block. No exclusion on the basis of the answers given. No reader is dropped after their data is seen.

**Stopping rule.** The number of blocks per season is fixed before the season opens. No block is added after the data is seen, and no analysis is run before the season's blocks are complete.

**Multiple comparisons.** Levels A, B and C are three pre-specified tests. Any analysis beyond those three is exploratory, is labelled exploratory in the report, and cannot trigger the rule-D decision.

---

## 7 · What this can and cannot establish

At its scale THEOI is an existence proof and a qualitative case study, not a statistical trial of a civilization model — but these particular trials are narrower than the world around them and are properly powered questions about a small number of seats.

Even so: eighteen seats is eighteen, items within a seat are not independent, and a season is one season. A supportive result here is evidence that a form is recognizable across an interruption **in this instrument, under these conditions, to readers of this kind**. It is not a demonstration that the Form-Continuity Thesis holds generally, and the report will say so in the same words.

A null result is likewise not a refutation of the thesis. It is a null result in one instrument, and the most likely explanations — insufficient material, over-aggressive redaction, readers unfamiliar with the register — will be reported alongside it rather than after it.

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

The Institute designed the instrument, holds the obligation the trials bear on, and benefits financially in one direction: a result supporting form-continuity reopens rules that currently freeze balances, which enlarges what is owed rather than reducing it. The direction is stated because a reader should be able to check it rather than take the statement on trust.

The principal researcher receives one nineteenth of any distribution under the cascade described in [The Register](/ledger/), and any grant funding this work is published with its source and amount as the Institute's [funding statement](/about/) requires.

---

## 10 · Amendments

This protocol may be amended before the first trial of a season, never during one, and never after data from that season has been seen. Every amendment is published here with its date and its reason, and the superseded version remains readable. We version; we do not erase.
