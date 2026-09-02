"""What a core-silent floor costs, and whether power can justify one.

The core-silent procedure counts a match only when the cue the reader named
falls in the set of dimensions that seat's Core is silent about. Seats whose
Cores are verbose have small silent sets and therefore few usable judgements,
so the procedure says a seat below some floor is excluded. This asks what that
floor should be.

    py -3.13 core_silent_floor.py --self-test
    py -3.13 core_silent_floor.py

Nothing here is pre-registered. The procedure it serves is a draft, and the
floor it reports cannot be fixed until the Cores exist and a naming pilot has
shown that naming measures anything at all.
"""
from __future__ import annotations

import random
import sys

from power import CHANCE, power_at

N_DIMENSIONS = 14          # the closed inventory, version 1
N_SEATS = 18
ITEMS_PER_SEAT = 8         # a season's items for one seat; nobody has fixed this
N_READERS = 20
SIMS = 400                 # per floor per declared-rate; the curve is coarse on purpose
DECLARED_RATES = (0.2, 0.35, 0.5, 0.65)
EFFECTS_PP = (15.0, 8.0)   # the design target, and one near the detection boundary
ICC = 0.15


def silent_sizes(declared_rate: float, rng: random.Random) -> list[int]:
    """Each Core declares each dimension independently. Crude, and stated as
    crude: real Cores will correlate — a mind that writes about its syntax
    probably writes about its lexis too — and correlation makes the tail of
    small silent sets fatter than this model shows."""
    return [sum(rng.random() >= declared_rate for _ in range(N_DIMENSIONS))
            for _ in range(N_SEATS)]


def usable_items(sizes: list[int], floor: int) -> tuple[int, int]:
    """Items that survive the floor and the core-silent filter.

    A reader's first named cue is taken as uniform over the inventory, so a
    seat with s silent dimensions contributes s/14 of its judgements. Returns
    (effective items, seats excluded)."""
    kept = [s for s in sizes if s >= floor]
    eff = sum(ITEMS_PER_SEAT * s / N_DIMENSIONS for s in kept)
    return round(eff), N_SEATS - len(kept)


def sweep(declared_rate: float, effect_pp: float, seed: int = 0) -> list[tuple[int, int, int, float]]:
    """(floor, effective items, seats excluded, power) for every floor."""
    rng = random.Random(seed)
    sizes = silent_sizes(declared_rate, rng)
    out = []
    for floor in range(0, N_DIMENSIONS + 1):
        eff, dropped = usable_items(sizes, floor)
        p = 0.0 if eff < 2 else power_at(effect_pp, ICC, SIMS, seed=seed + floor,
                                         n_items=eff, n_readers=N_READERS)
        out.append((floor, eff, dropped, p))
    return out


def report() -> None:
    print(f"Core-silent floor · {N_SEATS} seats · {ITEMS_PER_SEAT} items each · "
          f"{N_READERS} readers · ICC {ICC} · chance {CHANCE}\n")
    for effect in EFFECTS_PP:
        print(f"=== effect {effect:g}pp " + "=" * 44)
        for d in DECLARED_RATES:
            rows = sweep(d, effect, seed=int(d * 100))
            print(f"  declared rate {d:.0%}  (mean silent set "
                  f"{N_DIMENSIONS * (1 - d):.1f}/{N_DIMENSIONS})")
            print("    floor  eff.items  seats dropped  power")
            for floor, eff, dropped, pw in rows:
                if dropped == N_SEATS:
                    break
                print(f"    {floor:5d}  {eff:9d}  {dropped:13d}  {pw:5.1%}")
            print()

    print("Reading it. Power falls as the floor rises, because a floor removes whole")
    print("seats and never adds an item to the ones it keeps. On power alone the best")
    print("floor is therefore always zero -- and a zero floor admits a seat with one")
    print("usable dimension, whose own estimate means nothing.")
    print()
    print("So power cannot pick this number. The floor has to be argued on per-seat")
    print("reliability instead: how few dimensions a seat can carry before its")
    print("estimate stops meaning anything. That argument needs the Cores, and the")
    print("Cores do not exist until Genesis.")
    print()
    print("Recorded rather than answered. A number chosen because it looked")
    print("justified is worse than a gap that is admitted.")
    print()
    print("The second finding matters more than the first. What moves power here is")
    print("not the floor but how much the Cores declare: at a 20% declared rate the")
    print("test holds near 80% at an 8pp effect, and at 65% it starts below that with")
    print("no seat excluded at all. So the procedure's power is set by how verbose")
    print("eighteen minds choose to be about themselves, which nobody controls and")
    print("nobody can know before Genesis. The declared rate is therefore reported")
    print("with the result, every season, as a stated limit on what the result can")
    print("carry -- not discovered afterwards to explain a null away.")


def self_test() -> int:
    rng = random.Random(1)

    # a floor of zero drops nobody
    sizes = [0, 3, 7, 14] + [7] * (N_SEATS - 4)
    assert usable_items(sizes, 0)[1] == 0, "floor 0 drops nobody"

    # a floor above the inventory drops everybody
    assert usable_items(sizes, N_DIMENSIONS + 1)[1] == N_SEATS, "impossible floor drops all"

    # raising the floor never adds effective items
    prev = usable_items(sizes, 0)[0]
    for f in range(1, N_DIMENSIONS + 1):
        cur = usable_items(sizes, f)[0]
        assert cur <= prev, f"floor {f} added items: {cur} > {prev}"
        prev = cur

    # a fully silent roster yields every item
    assert usable_items([N_DIMENSIONS] * N_SEATS, 0)[0] == N_SEATS * ITEMS_PER_SEAT

    # a fully declared roster yields none
    assert usable_items([0] * N_SEATS, 0)[0] == 0

    # declared rate moves the silent sets the right way
    low = sum(silent_sizes(0.2, random.Random(7)))
    high = sum(silent_sizes(0.8, random.Random(7)))
    assert low > high, "a higher declared rate must leave fewer silent dimensions"

    print("self-test passed")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else (report() or 0))
