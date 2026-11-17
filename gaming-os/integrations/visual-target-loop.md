# Gelung sasaran visual

WORKING v0.1; 17 November 2026. Diadaptasi daripada skill Cook oleh Leon Lin (MIT, commit `b23cac6f`); lihat [repo asal](https://github.com/Leonxlnx/cook). Gunakan dalam ART, ASSET dan ITERATE apabila rupa game (scene, model, UI, animasi, trailer) mesti setanding rujukan. Ia kaedah pilihan, bukan gate, dan tidak memilih enjin atau provider.

## Prinsip

1. **Rujukan membawa rupa, brief pendek.** Kumpul rujukan pemilik (imej, tangkapan skrin, video) dalam folder game, bernombor R01… dan V01…. Gambar menyampaikan cahaya, warna, komposisi dan ketumpatan yang perkataan tidak dapat. Rujukan ialah aras mutu minimum; ambil daripada banyak rujukan, jangan salin satu unsur 1:1. Identiti, watak dan aset tetap asli.
2. **Sasaran dahulu.** Sebelum build penuh, hasilkan sasaran murah untuk dipilih pemilik: mockup, konsep atau dua hingga tiga arah bersebelahan. Menukar sasaran lebih murah daripada menukar build.
3. **Bar bernombor setiap dimensi.** Komposisi, cahaya, warna, bahan, ketumpatan butiran (dekat dan jauh) dan gerakan masing-masing ada nombor, supaya dimensi terlemah tidak terlindung. Nombor tinggi memberitahu agent bahawa kerja belum siap sebaik sahaja ia berfungsi.
4. **Kalibrasi oleh pemilik.** Model menilai diri terlalu tinggi. Apabila pemilik memberi anggaran (“ini 60–70%”), rekod beza sebagai offset dan tolak daripada skor seterusnya.
5. **Pengkritik konteks segar.** Pembina ialah hakim paling lemah. Skor diberi oleh sub-agent atau sesi baharu yang hanya menerima imej sebelah-menyebelah dan rubrik, tanpa kod, sejarah atau skor pembina; sekurang-kurangnya dua, ambil median. Model lain sebagai hakim membantu: dalam projek ini Codex boleh menilai kerja Claude Code atau sebaliknya sebagai kerja baca sahaja. Tanpa itu, tanda “self-scored”.
6. **Diukur lawan dianggar.** Nombor daripada arahan (delta saturasi/kecerahan per rantau, frame time) dilabel *diukur*; skor pengkritik dilabel *dianggar*. Jangan lapor semakan yang tidak dijalankan.
7. **Bingkai tetap.** Satu preset kamera/viewport bagi setiap shot supaya setiap pusingan dirender pada bingkai dan nisbah yang sama dengan rujukan.
8. **Kedalaman sebelum keluasan; statik sebelum gerakan.** Jadikan satu shot, model atau skrin benar-benar baik sebelum memperbanyak. Betulkan reka bentuk statik dahulu, kemudian animasi; rujukan video dianalisis bingkai demi bingkai kepada senarai kesan dan tempo.
9. **Maklum balas khusus.** Kata pemilik direkod tepat dan didahulukan daripada pengkritik; setiap item ditutup hanya dengan still atau klip yang membuktikannya. Jika pemilik rasa ada yang tidak kena tetapi sukar menamakannya, terangkan dengan bahasa mudah bagaimana bahagian itu dibina.

## Satu pusingan

Fokus (maklum balas pemilik dahulu, kemudian dimensi terlemah) → baiki secara mendalam → render still pada preset → imej sebelah-menyebelah (rujukan kiri, hasil kanan) → ukur yang boleh diukur → skor pengkritik segar → catat dalam [lejar pusingan](../templates/visual-rounds.md) → hantar still dan nota ringkas kepada pemilik. Build mesti kekal boleh dijalankan pada akhir setiap pusingan; jika skor jatuh, baiki atau kembali ke pusingan terbaik.

Berhenti apabila bar dicapai mengikut median terkalibrasi, atau had masa/penggunaan yang ditetapkan pemilik tiba; laporkan terus apa yang masih di bawah bar.

## Penyesuaian Gaming OS

- **Masa dan penggunaan ditetapkan pemilik.** Tiada lantai lapan jam atau sasaran menghabiskan tetingkap penggunaan. Tanpa had yang dinyatakan, jalankan satu pusingan dan lapor. Generation berkredit kekal mengikut izin dan had projek.
- **Soalan masih dibenarkan** apabila keputusan memang milik pemilik; checkpoint dan arahan berhenti dihormati.
- **Tiada peraturan “sifar aset luar”.** Pipeline aset projek (Blender, Imagegen Codex, Higgsfield optional) kekal; provenance dan lesen direkod.
- **Skor bukan kelulusan.** Median pengkritik ialah `accepted_by_agent` paling tinggi; `approved_by_owner` hanya daripada pemilik, dan still bukan bukti runtime atau playtest.
- **Senarai elak** rupa generik ditulis dalam baris Elak brief setiap game, bukan senarai universal.
- Skrip `side-by-side.mjs` dan semakan warna dalam repo asal ialah rujukan; framework ini tidak memasangnya. Pilih alat mengikut enjin dan sahkan dalam persekitaran sebenar.

Kaedah ini belum diuji pada game Gaming OS.
