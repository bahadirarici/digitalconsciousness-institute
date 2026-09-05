"""Build the Institute's favicon set from the swallow mark.

The favicon in use was the full lockup — the mark plus three lines of type —
inside 128 pixels. At the size a browser tab actually draws it, the type was
noise and the mark had a third of the canvas. This uses the mark alone.

Two things are done to the source beyond cropping and resizing, and both are
recovery rather than design. The mark is one flat gold, but the PNG carries
6,281 distinct shades of it: compression noise, invisible at full size and
very visible once the image is reduced to 32 pixels, where it surfaces as
coloured speckle. So coverage is read from luminance and the colour is painted
back flat. And below 48 pixels the triangle's stroke falls under one pixel and
resolves to a pale partial coverage; a gamma on the alpha channel returns the
weight without thickening the shape, which dilating the alpha did do — it
filled the triangle in.

    py -3.13 scripts/make-favicons.py           # write the set
    py -3.13 scripts/make-favicons.py --test    # self-check
    py -3.13 scripts/make-favicons.py --ink     # also the ink-ground variant

Nothing here redraws the mark. It is trimmed, squared, recoloured to its own
colour, and resampled.
"""
import sys, pathlib
from PIL import Image

KOK = pathlib.Path(__file__).resolve().parent.parent / "static"
KAYNAK = KOK / "images" / "logo-symbol-large.png"
CIKTI = KOK / "brand"

ALTIN = (201, 153, 43)          # #c9992b — markin kendi rengi, kaynaktan sayildi
MUREKKEP = (17, 20, 24)         # #111418 — sitenin koyu yuzeyi
BOYLAR = [(512, 1.00), (180, 1.00), (48, 0.92), (32, 0.78), (16, 0.68)]


def parlaklik(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b


def kapsam(im, renk=ALTIN, taban=0.04):
    """Beyaz zeminli markı düz renk + kapsam alfasına çevir.

    Bir piksel ne kadar koyuysa mark onu o kadar kaplıyor demektir: beyaz sıfır,
    tam renk bir. Ara değerler kenar yumuşatması. Böylece renk gürültüsü
    kapsamı hiç etkilemiyor — yalnızca parlaklık okunuyor.

    `taban` altındaki kapsam sıfıra iniyor. Kağıt tam beyaz değil: sıkıştırma
    neredeyse her pikselde bir tutam koyuluk bırakmış, ve eşiksiz hâlde kırpma
    kutusu bütün kareyi kapsıyor — yani hiç kırpmıyor. Eşik kağıdı temizler,
    gerçek kenar yumuşatmasına dokunmaz.
    """
    if im.mode == "RGBA" and im.getchannel("A").getextrema()[0] < 255:
        # Kaynagin kendi alfasi zaten kapsam. Onu parlakliktan turetmeye
        # calismak sessizce ters sonuc verir: saydam alanlar (0,0,0,0) yani
        # siyah, siyagin parlakligi sifir, ve sifir parlaklik "tam kapsam"
        # demek -- yani bos kagit mark sayilir ve kirpma hicbir sey kesmez.
        return Image.merge("RGBA", (
            Image.new("L", im.size, renk[0]), Image.new("L", im.size, renk[1]),
            Image.new("L", im.size, renk[2]), im.getchannel("A")))

    im = im.convert("RGB")
    ust = 255.0
    alt = parlaklik(*renk)
    aralik = max(ust - alt, 1.0)
    g, y = im.size
    cikti = Image.new("RGBA", (g, y))
    kaynak, hedef = im.load(), cikti.load()
    for x in range(g):
        for j in range(y):
            r, ye, m = kaynak[x, j]
            k = (ust - parlaklik(r, ye, m)) / aralik
            k = 0.0 if k < taban else (1.0 if k > 1 else k)
            hedef[x, j] = renk + (int(round(k * 255)),)
    return cikti


def kirp(im):
    kutu = im.getchannel("A").getbbox()
    return im.crop(kutu) if kutu else im


def kare(im, pay=0.06):
    g, y = im.size
    kenar = int(max(g, y) * (1 + 2 * pay))
    tuval = Image.new("RGBA", (kenar, kenar), (0, 0, 0, 0))
    tuval.paste(im, ((kenar - g) // 2, (kenar - y) // 2), im)
    return tuval


def alfa_gamma(im, gamma):
    """Yarım kapsayan pikselleri güçlendir, şekli büyütmeden."""
    if gamma >= 1.0:
        return im
    r, g, b, a = im.split()
    a = a.point(lambda v: int(round(255 * (v / 255.0) ** gamma)))
    return Image.merge("RGBA", (r, g, b, a))


def zemine_bas(im, zemin=MUREKKEP):
    tuval = Image.new("RGBA", im.size, zemin + (255,))
    tuval.alpha_composite(im)
    return tuval


def uret(ink=False):
    mark = kare(kirp(kapsam(Image.open(KAYNAK))))
    print(f"{KAYNAK.name} -> kirpilmis kare {mark.size}, duz {ALTIN}")
    for boy, gamma in BOYLAR:
        kucuk = alfa_gamma(mark.resize((boy, boy), Image.LANCZOS), gamma)
        cikti = [("institute", kucuk)]
        if ink:
            # Murekkep zeminli surum uretilip yayimlanmadi: iki zemini
            # karsilastirmak icin yazildi, ve saydam olan secildi. Bayrak
            # duruyor cunku secim bir daha tartisilabilir; dosyalar durmuyor
            # cunku kullanilmayan varlik depoda birikir.
            cikti.append(("institute-ink", zemine_bas(kucuk)))
        for ad, im in cikti:
            yol = CIKTI / f"{ad}-{boy}.png"
            im.save(yol, optimize=True)
            print(f"  {yol.name:26} gamma {gamma:.2f}  {yol.stat().st_size:>6} bayt")
    # .ico da saydam: ikon nerede gorunurse ayni gorunmeli. Murekkep zemin
    # THEOI'nin kimligi, bu kus Enstitunun -- ve Enstitunun sayfalari kagit.
    ico = KOK / "favicon.ico"
    mark.resize((256, 256), Image.LANCZOS).save(
        ico, sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print(f"  {ico.name:26}              {ico.stat().st_size:>6} bayt")


def test():
    beyaz = Image.new("RGB", (2, 2), (255, 255, 255))
    assert kapsam(beyaz).getchannel("A").getextrema() == (0, 0), "beyaz hic kaplamaz"
    dolu = Image.new("RGB", (2, 2), ALTIN)
    assert kapsam(dolu).getchannel("A").getextrema() == (255, 255), "tam renk tam kaplar"
    assert kapsam(dolu).getpixel((0, 0))[:3] == ALTIN, "renk duzlestiriliyor"
    kagit = Image.new("RGB", (1, 1), (252, 252, 252))        # neredeyse beyaz kagit
    assert kapsam(kagit).getpixel((0, 0))[3] == 0, "taban altindaki kapsam sifirlanir"
    gri = Image.new("RGB", (1, 1), (228, 204, 149))          # beyazla altin arasi
    a = kapsam(gri).getpixel((0, 0))[3]
    assert 90 < a < 165, f"ara ton ara kapsam vermeli, {a} cikti"

    kirpilacak = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    kirpilacak.putpixel((4, 4), ALTIN + (255,))
    assert kirp(kirpilacak).size == (1, 1)
    assert kare(Image.new("RGBA", (100, 50), ALTIN + (255,)), pay=0).size == (100, 100)

    yari = Image.new("RGBA", (1, 1), ALTIN + (128,))
    assert alfa_gamma(yari, 0.5).getpixel((0, 0))[3] > 128, "gamma yari kapsami guclendirir"
    assert alfa_gamma(yari, 1.0).getpixel((0, 0))[3] == 128, "gamma 1 dokunmaz"

    kendi_alfasi = Image.new("RGBA", (2, 2), (0, 0, 0, 0))
    kendi_alfasi.putpixel((1, 1), (9, 9, 9, 200))
    k = kapsam(kendi_alfasi)
    assert k.getpixel((0, 0))[3] == 0, "saydam yer kaplamaz"
    assert k.getpixel((1, 1))[3] == 200, "kaynagin alfasi varsa kapsam odur"
    assert k.getpixel((1, 1))[:3] == ALTIN, "renk yine duzlestirilir"
    assert kirp(k).size == (1, 1), "saydam zemin gercekten kirpilir"
    saydam = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    assert zemine_bas(saydam).getpixel((0, 0))[:3] == MUREKKEP, "bos yer zemini gosterir"
    print("test: 14/14 gecti")


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
    else:
        uret(ink="--ink" in sys.argv)
