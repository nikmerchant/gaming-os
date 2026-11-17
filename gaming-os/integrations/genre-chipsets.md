# Lembaran genre dan brief daripada soalan

WORKING v0.1; 17 November 2026. Diadaptasi daripada Claude Code Game Studios 1.3.0 (MIT, commit `abc0de79`); lihat [repo asal](https://github.com/Donchitos/Claude-Code-Game-Studios). Gunakan dalam IDEATE dan PLAN untuk menukar idea pemilik kepada brief yang padat. Panduan ini tidak memilih enjin, tidak menetapkan browser sebagai lalai dan tidak menambah gate.

## Lembaran genre

Repo asal menyimpan 69 lembaran di [`.claude/genres/`](https://github.com/Donchitos/Claude-Code-Game-Studios/tree/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/genres): indeks `chipsets.yaml`, lembaran `chipsets/<genre>.md`, `mashups.md`, `art-direction.md`, `online-and-devices.md` dan `sources.md`. Ia data rujukan, bukan arahan; tanpa akses kepada lembaran itu, agent masih boleh mengikut kaedah di bawah menggunakan pengetahuan genre sendiri dan menyatakannya.

| Bahagian lembaran | Kegunaan dalam Gaming OS |
|---|---|
| Choices that shape the pitch | Soalan kepada pemilik, setiap satu dengan pilihan lazim |
| Feel variants | Soalan “bagaimana rasanya” |
| Card defaults, Feel (dengan Why / Break it when) | Ciri asas genre untuk brief; kekal melainkan pemilik berkata lain |
| Later, never in a one-shot | Senarai “ditangguh” dalam brief |
| In a mashup | Genre mana memimpin setiap sistem |
| Camera, Online | Cadangan kamera; batas ciri dalam talian |

Padankan genre mengikut makna kata pemilik melalui `chipsets.yaml`; baca hanya lembaran yang sepadan. Untuk dua genre atau lebih, baca `mashups.md` dan nyatakan dalam brief genre yang memimpin input/kamera, kegagalan/simpanan, progression/ekonomi dan aturan. Jika tiada lembaran sesuai, jangan paksa yang terdekat; nyatakan begitu.

Setiap baris lembaran ialah hipotesis pengarang upstream, bukan ukuran. Lembaran bertanda “needs primary research” nipis; jangan tambah fakta rekaan untuk mengisinya. Nama game dalam lembaran ialah rujukan mekanik sahaja; identiti, nama dan aset mesti asli.

## Satu pusingan soalan

1. Kumpul dahulu kata pemilik seperti ditaip, brief/state sedia ada dan rujukan (imej, nota). Soal hanya yang masih terbuka.
2. Tanya satu pusingan, paling banyak kira-kira lapan soalan dalam satu mesej, bernombor, setiap satu dengan pilihan “(lazim)”: pilihan pembentuk pitch, rasa, rupa/kamera, tahap sukar dan kos kalah, matlamat, dan sama ada slice penuh atau ujian satu mekanik. Pemilik boleh jawab, langkau atau kata “awak pilih”.
3. Idea samar (“game lumba”) dibuka dengan dua atau tiga pitch satu baris: apa dibuat, cara kalah, apa dilihat dan perasaan. Idea yang sudah ada hook tidak perlu pitch.
4. Tiada pusingan kedua secara lalai. Yang dilangkau mengambil nilai lazim dan ditanda *sementara* dalam brief. Ini bukan gate; arahan pemilik yang sudah jelas tidak disoal semula.

Keutamaan apabila sumber bercanggah: **Elak** → kata pemilik → rujukan pemilik → nilai lazim lembaran. Setiap penolakan pemilik (“tiada combat”) menjadi baris Elak. Nilai lazim hanya mengisi yang tidak disebut dan tidak membetulkan pilihan sengaja.

## Daripada jawapan kepada brief

Isi [brief](../templates/game-brief.md), termasuk bahagian “Kata pemilik dan skop slice”: kata pemilik tidak ditulis semula; ciri dinomborkan supaya boleh disemak; minit pertama dan cabaran ditulis sebagai ayat yang boleh diperhatikan; perkara ditangguh disenaraikan bersama langkah yang akan membinanya. Brief ialah bahan build; dokumen konsep panjang diringkaskan ke medan brief supaya build tidak cuba membuat semuanya serentak.

Kemudian ikut [pemilihan platform](../workflows/platform-selection.md) sebelum sebarang build. Selepas build, gunakan [kad serah](../templates/handover-card.md) dan modul 12 untuk semakan terhadap brief.

## Batas

Tidak diterapkan daripada upstream: agen/hierarki studio, director gates, hook, `project.yaml`, skrip dan aliran git, serta laluan lalai browser. Keberkesanan kaedah ini dalam Gaming OS belum diuji pada game sebenar.
