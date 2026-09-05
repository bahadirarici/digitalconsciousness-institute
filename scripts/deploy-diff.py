"""Does pushing this actually change the site?

Every push builds, and a build costs the same whether it changes a hundred
pages or none. On 5 September a push landed here that changed seventeen source
files and produced a byte-identical site — the date was moved into a parameter,
which was worth doing and cost a whole build to publish nothing.

This builds what is deployed (origin/main) and what is about to be, and says
which pages differ. Nothing differing is not a reason to abandon the work; it
is a reason to let it ride along with the next push that does change something.

    py -3.13 scripts/deploy-diff.py          # what a push would change
    py -3.13 scripts/deploy-diff.py --test   # self-check

Exit 0 when the output differs, 1 when it does not — so it can gate a push.
"""
import sys, subprocess, tempfile, pathlib, hashlib, shutil, os

KOK = pathlib.Path(__file__).resolve().parent.parent


def hugo_yolu():
    """Hugo PATH'te degil; WinGet paketinden bulunuyor."""
    if shutil.which("hugo"):
        return "hugo"
    for p in pathlib.Path(os.environ.get("LOCALAPPDATA", "")).glob(
            "Microsoft/WinGet/Packages/Hugo.Hugo.Extended_*/hugo.exe"):
        return str(p)
    raise SystemExit("hugo bulunamadi")


def parmakizi(kok):
    """Uretilen her dosyanin yolu -> icerigin ozeti."""
    kok = pathlib.Path(kok)
    cikti = {}
    for p in sorted(kok.rglob("*")):
        if p.is_file():
            cikti[str(p.relative_to(kok)).replace("\\", "/")] = \
                hashlib.sha256(p.read_bytes()).hexdigest()
    return cikti


def fark(once, sonra):
    """(eklenen, silinen, degisen) — yol listeleri."""
    a, b = set(once), set(sonra)
    return (sorted(b - a), sorted(a - b),
            sorted(y for y in a & b if once[y] != sonra[y]))


def kur(ref, hedef):
    """Bir ref'i gecici bir calisma agacina cikarip derle."""
    agac = tempfile.mkdtemp(prefix="dd-agac-")
    subprocess.run(["git", "worktree", "add", "--detach", agac, ref],
                   cwd=KOK, check=True, capture_output=True)
    try:
        subprocess.run([hugo_yolu(), "--gc", "--minify", "-s", agac, "-d", hedef],
                       check=True, capture_output=True)
        return parmakizi(hedef)
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", agac],
                       cwd=KOK, capture_output=True)


def main():
    yayinda = subprocess.run(["git", "rev-parse", "origin/main"], cwd=KOK,
                             capture_output=True, text=True).stdout.strip()
    burada = subprocess.run(["git", "rev-parse", "HEAD"], cwd=KOK,
                            capture_output=True, text=True).stdout.strip()
    if yayinda == burada:
        print("HEAD zaten origin/main — pushlanacak bir sey yok")
        return 1

    gecici = tempfile.mkdtemp(prefix="dd-cikti-")
    try:
        once = kur(yayinda, os.path.join(gecici, "once"))
        sonra = kur(burada, os.path.join(gecici, "sonra"))
    finally:
        shutil.rmtree(gecici, ignore_errors=True)

    eklenen, silinen, degisen = fark(once, sonra)
    n = subprocess.run(["git", "rev-list", "--count", f"{yayinda}..{burada}"],
                       cwd=KOK, capture_output=True, text=True).stdout.strip()
    print(f"yayinda {yayinda[:7]}  ->  burada {burada[:7]}   ({n} commit)")
    print(f"uretilen dosya: {len(once)} -> {len(sonra)}\n")

    if not (eklenen or silinen or degisen):
        print("  CIKTI BIREBIR AYNI — bu push bir derleme yakar, hicbir sayfa degismez")
        print("  bir sonraki degisiklikle birlikte gitsin")
        return 1

    for ad, liste in (("eklenen", eklenen), ("silinen", silinen), ("degisen", degisen)):
        if liste:
            print(f"  {ad} ({len(liste)}):")
            for y in liste[:20]:
                print(f"    {y}")
            if len(liste) > 20:
                print(f"    … {len(liste)-20} tane daha")
    return 0


def test():
    assert fark({}, {}) == ([], [], [])
    assert fark({"a": "1"}, {"a": "1"}) == ([], [], [])
    assert fark({"a": "1"}, {"a": "2"}) == ([], [], ["a"])
    assert fark({}, {"b": "1"}) == (["b"], [], [])
    assert fark({"c": "1"}, {}) == ([], ["c"], [])
    e, s, d = fark({"a": "1", "c": "1"}, {"a": "2", "b": "1"})
    assert (e, s, d) == (["b"], ["c"], ["a"]), (e, s, d)

    gec = tempfile.mkdtemp(prefix="dd-test-")
    try:
        (pathlib.Path(gec) / "alt").mkdir()
        (pathlib.Path(gec) / "alt" / "x.html").write_bytes(b"merhaba")
        pi = parmakizi(gec)
        assert list(pi) == ["alt/x.html"], pi
        assert pi["alt/x.html"] == hashlib.sha256(b"merhaba").hexdigest()
    finally:
        shutil.rmtree(gec, ignore_errors=True)
    print("test: 8/8 gecti")
    return 0


if __name__ == "__main__":
    sys.exit(test() if "--test" in sys.argv else main())
