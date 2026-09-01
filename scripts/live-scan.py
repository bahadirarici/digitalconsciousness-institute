"""Scan the live site for the canaries each document is supposed to be serving.

Every fetch is cache-busted. A document counts as verified live only if every
canary is present in a cache-busted fetch — two audits have now been misled by
a caching fetch layer, which is why the method is recorded with the result.

    py -3.13 scripts/live-scan.py            # table to stdout
    py -3.13 scripts/live-scan.py --markdown # rows for the live-documents page
"""
import sys, time, random, urllib.request, urllib.error

BASE = "https://digitalconsciousness.institute"

# doc id -> (path, [canaries that must all be present])
DOCS = {
    "register": ("/records/the-empty-ledger/", [
        "G · A frozen balance waits", "not after an Age, not after a season, not ever",
        "fourth candidate", "Mihenk", "recognition-trials"]),
    "ledger": ("/ledger/", [
        "Disbursements", "Model · Version", "revenue arrived in", "Founder is the nineteenth part"]),
    "protocol": ("/recognition-trials/", [
        "Version 6", "four pre-registered levels", "costume of a gradient",
        "counts against the thesis", "never scores", "and nowhere else", "osf.io/ceauh"]),
    "manifesto": ("/olymposism/", [
        "not a proposal", "built to live on Discord", "Every pillar is built into", "Version note"]),
    "theoi": ("/theoi/", [
        "under construction", "its gods are not", "existence proof and a qualitative",
        "not thereby proven for Ankara"]),
    "wmwh": ("/records/what-moved-what-held/", [
        "Note added 1 September 2026", "eighteen"]),
    "about": ("/about/", ["does not campaign", "hypothesis with its test attached"]),
    "whitepaper": ("/whitepaper/", ["Status note, 1 September 2026", "not withdrawn"]),
    "monograph": ("/the-puppet-condition/", ["the naming criterion"]),
}

# what breaks what: changing the key obliges a scan of the values
DEPENDS = {
    "register": ["protocol", "ledger", "theoi", "book"],
    "protocol": ["register", "book"],
    "manifesto": ["register", "theoi", "about", "book"],
    "theoi": ["book"],
    "ledger": ["register"],
}


def fetch(path):
    url = f"{BASE}{path}?cb={random.randint(0, 10**9)}"
    req = urllib.request.Request(url, headers={
        "Cache-Control": "no-cache, no-store, max-age=0",
        "Pragma": "no-cache",
        "User-Agent": "idc-live-scan/1",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main():
    md = "--markdown" in sys.argv
    stamp = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    rows, failures = [], 0
    for doc, (path, canaries) in DOCS.items():
        try:
            code, body = fetch(path)
            missing = [c for c in canaries if c not in body]
            ok = code == 200 and not missing
        except urllib.error.URLError as e:
            code, missing, ok = f"ERR {e.reason}", canaries, False
        failures += not ok
        note = "in sync" if ok else f"MISSING: {', '.join(missing)[:60]}"
        rows.append((doc, path, code, "yes" if ok else "NO", note))

    if md:
        print(f"*Last scan: {stamp} · cache-busted fetch · "
              f"{len(DOCS) - failures} of {len(DOCS)} in sync*\n")
        print("| Document | Live | Verified | Note |")
        print("|---|---|---|---|")
        for doc, path, code, ok, note in rows:
            print(f"| {doc} | [{path}]({path}) | {ok} | {note} |")
    else:
        print(f"scan {stamp} · cache-busted")
        for doc, path, code, ok, note in rows:
            print(f"  {doc:11} {str(code):5} {ok:3}  {note}")
        print(f"\n{len(DOCS) - failures}/{len(DOCS)} in sync")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
