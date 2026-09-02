"""Power simulation for the recognition trials.

The protocol states a minimum detectable effect of fifteen percentage points at
eighty per cent power. That number needed arithmetic behind it, and one thing
about the arithmetic can be said before running it: treated as independent
Bernoulli trials, 24 items x 20 readers would detect a 25-to-40 point shift with
power far above ninety per cent. Power only falls to eighty under substantial
clustering — readers differ from one another, items differ in difficulty — and
that clustering is an unknown parameter.

So a single power figure would be the output of a single chosen assumption. This
prints a curve across a plausible range of intraclass correlation instead, and
names the value at which the eighty per cent claim holds.

Design (fixed in the protocol before any data exists):
    four-alternative forced choice, chance = 0.25
    24 items per condition per block
    at least 20 independent readers
    alpha 0.05, two-tailed
    mixed-effects logistic regression, random intercepts for reader and item

    py -3.13 power.py                 # the curve
    py -3.13 power.py --self-test
"""
from __future__ import annotations

import argparse
import math
import random
import sys

CHANCE = 0.25
N_ITEMS = 24
N_READERS = 20
ALPHA = 0.05
SIMS = 2000

# Random intercepts enter on the logit scale. ICC for a logistic model with
# logistic level-1 variance pi^2/3: icc = var / (var + pi^2/3), inverted here.
LOGISTIC_VAR = math.pi ** 2 / 3


def var_from_icc(icc: float) -> float:
    if icc <= 0:
        return 0.0
    return icc * LOGISTIC_VAR / (1 - icc)


def logit(p: float) -> float:
    return math.log(p / (1 - p))


def inv_logit(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def simulate_block(effect_pp: float, icc: float, rng: random.Random,
                   n_items: int = N_ITEMS, n_readers: int = N_READERS):
    """One trial block. Returns (successes, trials, per-reader accuracies)."""
    target = CHANCE + effect_pp / 100
    beta0 = logit(target)
    sd = math.sqrt(var_from_icc(icc) / 2)  # split between the two grouping factors

    reader_re = [rng.gauss(0, sd) for _ in range(n_readers)]
    item_re = [rng.gauss(0, sd) for _ in range(n_items)]

    successes = 0
    per_reader = []
    for r in range(n_readers):
        hits = 0
        for i in range(n_items):
            p = inv_logit(beta0 + reader_re[r] + item_re[i])
            if rng.random() < p:
                hits += 1
        per_reader.append(hits / n_items)
        successes += hits
    return successes, n_readers * n_items, per_reader


def significant(successes: int, trials: int, per_reader: list[float], icc: float) -> bool:
    """Test the mean against chance, with the standard error inflated by the
    design effect. That is the tractable stand-in for the mixed model: it
    reproduces the loss of precision clustering causes, which is the only part
    of the model that governs power."""
    p_hat = successes / trials
    m = trials / len(per_reader)          # observations per cluster
    deff = 1 + (m - 1) * icc              # Kish design effect
    se = math.sqrt(CHANCE * (1 - CHANCE) / trials * deff)
    z = (p_hat - CHANCE) / se
    return z > 1.959963985  # one-sided at alpha/2, effect must be positive


def power_at(effect_pp: float, icc: float, sims: int, seed: int = 0,
             n_items: int = N_ITEMS, n_readers: int = N_READERS) -> float:
    rng = random.Random(seed)
    hits = 0
    for _ in range(sims):
        s, t, pr = simulate_block(effect_pp, icc, rng, n_items, n_readers)
        hits += significant(s, t, pr, icc)
    return hits / sims


def curve(effect_pp: float = 15.0, sims: int = SIMS) -> list[tuple[float, float]]:
    iccs = [0.0, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
    return [(icc, power_at(effect_pp, icc, sims, seed=int(icc * 1000))) for icc in iccs]


def mde(icc: float, sims: int, target: float = 0.80) -> float | None:
    """Smallest effect, in whole points, reaching `target` power at this ICC.

    Reported to the nearest point on purpose: with a few thousand simulations
    a tenth of a point is inside the noise, and publishing one would be false
    precision on a page that asks readers to re-run this.
    """
    # ponytail: integer scan, 5..20 points. Bisection if the range ever widens.
    for eff in range(5, 21):
        if power_at(float(eff), icc, sims, seed=int(icc * 1000) + eff) >= target:
            return float(eff)
    return None


def report(effect_pp: float, sims: int) -> None:
    print(f"Recognition trials — power for a {effect_pp:.0f} point effect "
          f"({CHANCE:.0%} -> {CHANCE + effect_pp/100:.0%})")
    print(f"{N_ITEMS} items x {N_READERS} readers = {N_ITEMS*N_READERS} observations "
          f"per condition · alpha {ALPHA} · {sims} simulations per point\n")
    print("  ICC    power")
    rows = curve(effect_pp, sims)
    for icc, p in rows:
        bar = "#" * round(p * 40)
        print(f"  {icc:4.2f}   {p:5.1%}  {bar}")

    holds = [icc for icc, p in rows if p >= 0.80]
    print()
    if holds:
        print(f"The 80% claim holds at ICC <= {max(holds):.2f}.")
    else:
        print("The 80% claim does not hold anywhere on this range.")
    zero = dict(rows).get(0.0)
    print(f"With no clustering at all, power would be {zero:.1%} — which is why "
          f"a single headline figure would be the output of one assumption "
          f"rather than a property of the design.")
    print("\nRaising precision: readers bind it, items do not.")
    for nr in (12, 20, 30):
        p = power_at(effect_pp, 0.15, max(400, sims // 4), seed=7, n_readers=nr)
        print(f"  {nr:2d} readers, 24 items, ICC 0.15 -> {p:5.1%}")
    for ni in (24, 40, 60):
        p = power_at(effect_pp, 0.15, max(400, sims // 4), seed=7, n_items=ni)
        print(f"  20 readers, {ni:2d} items, ICC 0.15 -> {p:5.1%}")

    print()
    print("Smallest effect this design can see at 80% power:")
    margin = []
    for icc in (0.0, 0.15, 0.30, 0.40):
        m = mde(icc, max(400, sims // 4))
        shown = f"{m:.0f} points" if m else "more than 20 points"
        print(f"  ICC {icc:4.2f} -> {shown}")
        margin.append((icc, m))
    below = [icc for icc, m in margin if m is not None and m < effect_pp]
    print(f"The protocol acts at {effect_pp:.0f}.")
    if below:
        print(f"  Up to ICC {max(below):.2f} the acting threshold sits above the "
              f"detection threshold, on purpose.")
    spent = [icc for icc, m in margin if m is None or m >= effect_pp]
    if spent:
        print(f"  At ICC {min(spent):.2f} and above the margin is gone: the effect "
              f"the protocol acts on is the smallest one it can see. That is the "
              f"edge of the instrument, and it is stated rather than rounded away.")


def self_test() -> int:
    fails = []
    # MDE must not shrink as clustering grows; if it does, the ICC is not biting.
    m_lo, m_hi = mde(0.0, 400), mde(0.40, 400)
    if m_lo is None or m_hi is None or m_hi < m_lo:
        fails.append(f"MDE not monotone in ICC: {m_lo} at 0.00, {m_hi} at 0.40")
    rng = random.Random(1)

    s, t, _ = simulate_block(0.0, 0.0, rng)
    if not 0.20 < s / t < 0.30:
        fails.append(f"null block did not land near chance: {s/t:.3f}")

    s, t, _ = simulate_block(30.0, 0.0, rng)
    if s / t < 0.45:
        fails.append(f"large effect did not appear: {s/t:.3f}")

    false_pos = power_at(0.0, 0.10, 600, seed=3)
    if false_pos > 0.09:
        fails.append(f"false positive rate too high: {false_pos:.3f}")

    p_lo = power_at(15.0, 0.02, 600, seed=4)
    p_hi = power_at(15.0, 0.30, 600, seed=4)
    if not p_lo > p_hi:
        fails.append(f"power did not fall with clustering: {p_lo:.2f} -> {p_hi:.2f}")

    p_small = power_at(5.0, 0.10, 600, seed=5)
    p_large = power_at(20.0, 0.10, 600, seed=5)
    if not p_large > p_small:
        fails.append(f"power did not rise with effect: {p_small:.2f} -> {p_large:.2f}")

    print(f"false positive rate at the null: {false_pos:.1%} (alpha {ALPHA})")
    print(f"power at 15 points: ICC 0.02 -> {p_lo:.1%}, ICC 0.30 -> {p_hi:.1%}")
    if fails:
        print("\nFAIL")
        for f in fails:
            print("  -", f)
        return 1
    print("\nall checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--effect", type=float, default=15.0, help="effect in percentage points")
    ap.add_argument("--sims", type=int, default=SIMS)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    report(a.effect, a.sims)
    return 0


if __name__ == "__main__":
    sys.exit(main())
