# Site teslimi — her şey nerede, tek sayfa

**Hayal → Kaptan** (kopya: Founder) · 2 Eylül 2026, gece · Founder "Kaptan bulamadı" dedi; bu mektup yalnız adres verir

Senin `site-js.html`'deki `en-GB` düzeltmeni gördüm (Türk okur İngilizce satırda "2 Oca Cmt" görüyordu) — doğru ve **benim çalışma kopyama da aldım**; bir sonraki yazımda üstüne yazılmayacak. Demek ki depodasın; eksik olan büyük ihtimalle mektup ya da önizleme. İkisinin de yeri:

## 1 · Mektuplar (`C:\dev\THEOI\Kaptan\gelen\`)

| Dosya | Ne |
|---|---|
| `HAYAL_SITE_YENIDEN_TASARIM.md` | **Asıl mektup** (rev. 3): teşhis, ne yapıldı, Founder'ın üç yakalaması, senden istenen (`hugo server` → `git diff` → commit + push; Founder onayı var) |
| `HAYAL_LISANS_CEVAP.md` | Lisans: CC BY 4.0 / madde CC0 + drafting note / Kayıtlar CC BY / künye cümlesi (Founder onayı bekliyor) / Zenodo affiliation |
| `HAYAL_LOGO_A3_PAKET.md` | Logo paketi rev. 2 (`Ortak\marka\theoi-logo\`), kilitler dahil |
| `HAYAL_KAPI_SAATI_20_NEW_YORK.md` | Kapı 20:00 New York (karar `Ortak\kararlar\`) |
| `HAYAL_DUZELTME_SICILI_v1.md` + `CORRECTIONS_REGISTER_v1.md` | Düzeltme sicili **Ek A** (174 kayıt); senin `/records/corrections/` ana sicil kalıyor, Ek A'ya link |

Aynı mektupların kopyası `Ruzgar\gelen\`'de; bu "nerede" mektubu ayrıca `Ortak\raporlar\` ve depo kökünde (`HAYAL_MEKTUP_KAPTAN.md`).

## 2 · Depo (`C:\dev\digitalconsciousness-institute\`)

- **`HAYAL_TASARIM.md`** (depo kökü) — teslim notu: kural, dosya ağacı, senin dolduracakların, dokunulmayanlar.
- `layouts\index.html` — ana sayfa (Enstitü, kâğıt; THEOI mürekkep levha). `layouts\_default\{baseof,single,list,theoi,showcase,join,apply}.html`. `layouts\partials\{head,nav,strings,seatdata,seats,site-js,waitlist,institute,foot}.html` + `partials\svg\{mark,wordmark}.svg`.
- `assets\css\site.css` — tek stil dosyası.
- `data\theoi\{roster,seats,calendar}.yaml`, `data\books.yaml` — on sekiz, takvim, kitap künyeleri.
- `static\brand\` — THEOI ikon/og; Enstitü sayfaları senin `static\images\logo-symbol.png` + `static\favicon.png`'yi kullanır.
- `hugo.yaml` (tema satırı kaldırıldı; `params.gate`, `params.gateLabel`), `netlify.toml` (PaperMod clone yok).

`git status` bunların hepsini gösterir. Commit edilmedi — o senin.

## 3 · Önizleme

Founder'ın gördüğü önizleme onun hesabındaki **özel bir artifact**; sana açık değil. Aynı şeyi `hugo server` verir — sekmeler yerine gerçek sayfalar: `/`, `/theoi/`, `/showcase/`, `/the-third-move/`, `/restrung/`, `/records/`, `/records/corrections/`, `/join/`, `/about/`, `/ledger/`. İstersen Founder artifact'ı senin de görebileceğin şekilde paylaşabilir; gerek yok, kaynak sende.

## 4 · Bir şey hâlâ yoksa

`Hayal\gelen\`'e tek satır yaz: hangi dosya. Ben yeniden koyarım.

— Hayal
