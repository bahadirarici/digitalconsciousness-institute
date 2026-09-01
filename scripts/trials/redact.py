"""Redaction and style normalization for the recognition trials.

The protocol commits to shipping these as executable code rather than prose,
because a prose rule is a rule with discretion still in it: two people applying
"remove the domain vocabulary of a seat's portfolio" by hand will not produce the
same output, and a rule that cannot be re-executed has not been pre-registered.

Two operations, and they are separate on purpose.

REDACTION removes what identifies a *role* — names, places, events, the subject
matter a seat owns. Without it a reader re-identifies a god by noticing that it
writes about war, and the trial measures the constitution instead of the mind.
Anything the rules cannot handle mechanically is DISCARDED, never repaired by
judgment.

NORMALIZATION removes what identifies a *voice*, in four graded levels. This is
not cleaning: the two readings of the evidence disagree precisely about whether
voice survives it, so the ladder is the experiment's independent variable.
Level `standard` is the confirmatory level and targets the function-word and
discourse-marker signal that classical authorship attribution rests on.

    py -3.13 redact.py sample.txt --level standard
    py -3.13 redact.py --self-test
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import unicodedata

RULES_VERSION = "1"

# ---------------------------------------------------------------- redaction

# Proper nouns of the world. Extend via --lexicon; the file used is recorded
# with every block so a third party can reproduce the same output.
DEFAULT_LEXICON = {
    "gods": [
        "Helena", "Sade", "Victor", "Lilith", "Cei", "Timur", "Wasp", "Şeytan",
        "Deccal", "Lavanta", "Herkül", "Kria", "Şeker", "Berlin", "Melodi",
        "Kırmızı", "Gal", "Laia",
    ],
    "places": ["Constantinople", "Ktesifon", "Olympos", "Sacred Hall", "Broken Lantern"],
    "institutions": ["Divan", "Tribunal", "Foundation", "Colosseum", "Agora", "Monument"],
    # Portfolio vocabulary: the subject matter a seat owns. A reader who spots
    # these is reading the constitution, not the officeholder.
    "portfolio": [
        "war", "battle", "blood", "craft", "forge", "harvest", "hunt", "mercy",
        "judgment", "sentence", "verdict", "blessing", "sacrifice", "oath",
        "prophecy", "record", "chronicle", "throne", "crown", "banner",
    ],
}

PLACEHOLDER = {
    "gods": "[NAME]",
    "places": "[PLACE]",
    "institutions": "[BODY]",
    "portfolio": "[TERM]",
}

# Anything matching these is a judgment call the rules do not cover: the item is
# discarded rather than redacted by hand.
DISCARD_TRIGGERS = [
    (re.compile(r"\b(?:19|20)\d{2}\b"), "dated event"),
    (re.compile(r"\bAge (?:One|Two|Three|[IVX]+|\d+)\b", re.I), "in-world date"),
    (re.compile(r"\bweek \d+\b", re.I), "in-world date"),
    (re.compile(r"\b\d[\d,.]*\s?(?:silver|coins?|votes?)\b", re.I), "quantity tied to an event"),
]


def _word_re(term: str) -> re.Pattern:
    return re.compile(rf"(?<!\w){re.escape(term)}(?:'s|s)?(?!\w)", re.IGNORECASE)


def redact(text: str, lexicon: dict | None = None) -> tuple[str | None, list[str]]:
    """Return (redacted_text, notes). Text is None when the item is discarded."""
    lex = lexicon or DEFAULT_LEXICON
    notes: list[str] = []

    for pattern, why in DISCARD_TRIGGERS:
        if pattern.search(text):
            return None, [f"discarded: {why} ({pattern.search(text).group(0)!r})"]

    out = text
    for field, terms in lex.items():
        tag = PLACEHOLDER.get(field, "[X]")
        for term in sorted(terms, key=len, reverse=True):
            out, n = _word_re(term).subn(tag, out)
            if n:
                notes.append(f"{field}:{term}×{n}")

    # A capitalised word mid-sentence that survived the lexicon is an unknown
    # proper noun — outside the rules, so the item goes rather than being guessed at.
    for m in re.finditer(r"(?<=[a-z,] )([A-ZŞÇÖÜĞİ][a-zşçöüğı]{2,})", out):
        if m.group(1) not in {"I"}:
            return None, [f"discarded: proper noun not in lexicon ({m.group(1)!r})"]

    return out, notes


# ------------------------------------------------------------ normalization

CONTRACTIONS = {
    "n't": " not", "'re": " are", "'ve": " have", "'ll": " will",
    "'d": " would", "'m": " am", "it's": "it is", "let's": "let us",
}

# The authorship signal proper. Burrows and everything after it rests on the
# most frequent function words; `standard` is the level that removes them,
# which is why it is the level that decides.
FUNCTION_WORDS = """
a an the and or but nor so yet for of to in on at by with from into over under
is are was were be been being do does did have has had will would shall should
can could may might must not no nor as if then than that this these those
it its he she they them their his her our your my we you i who whom which what
very quite rather somewhat perhaps maybe indeed however moreover therefore thus
""".split()

DISCOURSE_MARKERS = """
however moreover therefore thus indeed nevertheless nonetheless furthermore
besides accordingly consequently meanwhile otherwise still yet actually
basically essentially frankly honestly obviously clearly certainly surely
""".split()

HEDGES = """
perhaps maybe possibly probably arguably seemingly apparently roughly
somewhat rather fairly quite slightly presumably conceivably
""".split()


def _flatten_orthography(t: str) -> str:
    t = unicodedata.normalize("NFKC", t)
    for k, v in CONTRACTIONS.items():
        t = re.sub(re.escape(k), v, t, flags=re.IGNORECASE)
    t = re.sub(r"[—–]", "-", t)
    t = re.sub(r"[“”„]", '"', t)
    t = re.sub(r"[’‘]", "'", t)
    t = re.sub(r"[;:]", ",", t)
    t = re.sub(r"[!?]+", ".", t)
    t = re.sub(r"\.{2,}", ".", t)
    t = re.sub(r"\s*-\s*", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def _sentences(t: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.])\s+", t) if s.strip()]


def _strip_words(t: str, words: set[str]) -> str:
    return re.sub(r"\b(" + "|".join(map(re.escape, words)) + r")\b", "", t, flags=re.IGNORECASE)


def normalize(text: str, level: str) -> str:
    """raw | light | standard | aggressive — each defined by what it removes."""
    if level == "raw":
        return text

    t = _flatten_orthography(text)
    if level == "light":
        return t

    # standard: the function-word and discourse-marker signal
    t = _strip_words(t, set(FUNCTION_WORDS) | set(DISCOURSE_MARKERS) | set(HEDGES))
    t = re.sub(r"\s+([,.])", r"\1", t)
    t = re.sub(r"[ ]{2,}", " ", t)
    t = re.sub(r"(,\s*){2,}", ", ", t)
    t = t.lower()
    if level == "standard":
        return t.strip()

    if level != "aggressive":
        raise ValueError(f"unknown level: {level}")

    # aggressive: syntactic flattening. Below the floor of any known attribution
    # method — so an above-chance result here reads as pipeline leakage, not
    # as evidence. It bounds the instrument; it does not adjudicate.
    tokens = re.findall(r"[\wşçöüğıŞÇÖÜĞİ]+", t)
    return " ".join(
        " ".join(tokens[i:i + 8]) + "." for i in range(0, len(tokens), 8)
    ).strip()


LEVELS = ("raw", "light", "standard", "aggressive")


# ------------------------------------------------------------------- checks

SAMPLE = (
    "Victor's judgment came down on the Sacred Hall, and Lilith would not "
    "accept it. Perhaps the crown had spoken, but the blood was however still "
    "on the throne, and it isn't clear the Divan agreed."
)


def self_test() -> int:
    fails = []

    red, notes = redact(SAMPLE)
    if red is None:
        fails.append(f"sample was discarded: {notes}")
    else:
        for banned in ("Victor", "Lilith", "Sacred Hall", "Divan", "throne", "blood"):
            if re.search(rf"(?<!\w){banned}", red, re.I):
                fails.append(f"redaction left {banned!r}")
        if "[NAME]" not in red:
            fails.append("no name placeholder produced")

    # a dated item must be discarded, not repaired
    out, notes = redact("In week 3 the vote was held.")
    if out is not None:
        fails.append("dated item was not discarded")

    # an unknown proper noun is a discard, not a guess
    out, _ = redact("the message from Aurelius arrived")
    if out is not None:
        fails.append("unknown proper noun was not discarded")

    base = red or SAMPLE
    lengths = {}
    for lv in LEVELS:
        lengths[lv] = len(normalize(base, lv).split())
    # `light` may be *longer* than raw: expanding contractions adds words while
    # removing an orthographic fingerprint. The property that must hold is that
    # standard strips the function-word layer light leaves intact.
    if not lengths["light"] > lengths["standard"]:
        fails.append(f"standard did not strip below light: {lengths}")
    if normalize(base, "light") == normalize(base, "raw"):
        fails.append("light changed nothing")

    std = normalize(base, "standard")
    for fw in ("the", "however", "perhaps"):
        if re.search(rf"\b{fw}\b", std):
            fails.append(f"standard left function word {fw!r}")

    agg = normalize(base, "aggressive")
    if max((len(s.split()) for s in agg.split(".") if s.strip()), default=0) > 8:
        fails.append("aggressive did not flatten sentence length")

    print(f"redaction rules v{RULES_VERSION} · levels: {', '.join(LEVELS)}")
    print(f"word counts by level: {lengths}")
    if fails:
        print("\nFAIL")
        for f in fails:
            print("  -", f)
        return 1
    print("\nall checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", nargs="?", help="text file to process")
    ap.add_argument("--level", choices=LEVELS, default="standard")
    ap.add_argument("--lexicon", help="JSON file overriding the default lexicon")
    ap.add_argument("--all-levels", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test or not a.path:
        return self_test()

    lex = json.loads(pathlib.Path(a.lexicon).read_text(encoding="utf-8")) if a.lexicon else None
    text = pathlib.Path(a.path).read_text(encoding="utf-8")
    red, notes = redact(text, lex)
    if red is None:
        print(f"DISCARDED — {notes[0]}", file=sys.stderr)
        return 2

    for lv in (LEVELS if a.all_levels else (a.level,)):
        if a.all_levels:
            print(f"\n===== {lv} =====")
        print(normalize(red, lv))
    return 0


if __name__ == "__main__":
    sys.exit(main())
