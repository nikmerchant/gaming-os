# Brief permainan

Salin ke folder permainan. Tetapkan sasaran dan keputusan platform sebelum membina apa sahaja game; aset final mengikuti pipeline yang telah diuji.

- Game ID / working title asal:
- Versi / tarikh / pemilik:
- Mod kerja dan hasil yang diminta:
- Audience / umur / bahasa:
- Peranti baseline / orientation / cara input:
- Platform keluaran / 2D, 2.5D atau 3D / kamera:
- Rujukan mutu gameplay dan animasi / kaedah animasi / transition utama:
- Player fantasy satu ayat:
- Design pillars (2-3):
- Core loop tindakan → keputusan → hasil → feedback:
- Objektif, syarat menang, gagal dan restart:
- Session length sasaran (belum terukur):
- Minimum vertical slice:
- Feature ditangguh dan sebab:
- Reference dan unsur mekanik yang dikaji:
- Identiti/nama/watak/dunia/UI/audio asal:

## Kata pemilik dan skop slice

Isi melalui [satu pusingan soalan](../integrations/genre-chipsets.md) apabila idea masih terbuka. Nilai yang diambil daripada lalai genre ditanda *sementara*.

- Kata pemilik (seperti ditaip; jangan tulis semula):
- Elak (setiap penolakan pemilik; mendahului semua sumber lain):
- Genre dipadankan / genre yang memimpin setiap sistem jika mashup:
- Ciri slice bernombor (C1, C2…; boleh disemak satu demi satu):
- Minit pertama (ayat yang boleh diperhatikan):
- Cabaran (bila kesukaran pertama tiba; kos kalah):
- Rupa dan rujukan (kamera, gaya; game terdekat dan beza kita):
- Ditangguh, bersama langkah yang akan membinanya:
- Diteka oleh agent (belum disahkan pemilik):

## Kontrak sistem

| Sistem | Aturan / data | Feedback | Reset / acceptance |
|---|---|---|---|
| Player / input | | | |
| World / collision | | | |
| Enemy / hazard | | | |
| Reward / score | | | |
| State / objective | | | |

## Seni dan aset

Kamera, perspektif, gaya, palet, lighting, skala runtime, animation, anchor dan density. Senarai aset minimum beserta tujuan, format, ukuran, alpha, provider pilihan dan status. Manifest ialah rekod fail sebenar; brief belum bukti generation.

## Teknik dan keputusan

- Enjin/toolchain terpilih serta alasan:
- Fail [keputusan platform](platform-decision.md) / status SELECTED sebelum build:
- Alat aset/rig/animasi / format export-import / bukti handoff:
- Versi disahkan / lockfile:
- Timestep, unit, collision model, viewport dan resize:
- Audio/mute/reduced effects:
- Bajet generation/loading/performance (cadangan vs hasil ukuran):
- Gate review jika memang diminta dan bukti kebenaran sedia ada:

## Acceptance dan langkah

Senario mesti lulus; peranti/browser; metode automatic/manual/human; risiko utama; open decisions; milestone pertama dan next action. Jangan tulis PASS sebelum diuji. Selepas build, isi [kad serah](handover-card.md) terhadap ciri bernombor di atas.
