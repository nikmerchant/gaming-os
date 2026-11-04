# 01 - Seni bina Gaming OS

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Kontrak

Gaming OS mempunyai tiga lapisan: sumber penyelidikan, panduan operasi dan projek permainan. Sumber menunjukkan kemungkinan; modul membantu membuat keputusan; projek menyimpan pilihan sebenar. Pisahkan memori OS daripada state setiap game.

Pipeline standard: sasaran gameplay/animasi/platform keluaran → brief dan aturan → keputusan enjin/alat aset → slice pengesahan pipeline → art contract/aset minimum → prototaip lengkap → QA/playtest → polish → release/checkpoint. Ikut [pemilihan platform](../workflows/platform-selection.md) sebelum build, termasuk prototaip mekanik. Pilih kerja yang mengurangkan ketidakpastian terbesar. Image-first boleh menetapkan arah konsep; aset runtime final mengikuti toolchain yang dipilih dan diuji.

Skop minimum perlu menyatakan tindakan utama, cabaran, reward, win/fail dan restart. Satu vertical slice menyambungkan semua sistem yang diperlukan dalam satu level/arena; ia bukan semua kandungan akhir.

## Input dan output

Input: niat pemilik, audience, peranti, genre, reference, tool tersedia dan had skop. Output: brief, dependency map, milestone dan acceptance criteria. Soalan yang belum terjawab direkod sebagai open decision, bukan diisi sebagai fakta.

Tiga milestone bukti: **planned** mempunyai kontrak; **implemented** mempunyai fail runnable; **verified** mempunyai hasil ujian yang relevan. Label production ready memerlukan sasaran platform, playtest dan release gate projek yang benar-benar dipenuhi.

## Pemeriksaan

Pastikan projek boleh menjawab: siapa bermain, apa tindakan mereka, bagaimana mendapat feedback, apa menamatkan sesi dan bagaimana mencuba semula. Jangan menambah backend, multiplayer, kedai atau crafting kerana ia muncul dalam genre lain. Semak ketidakpadanan antara pelan, aset dan gameplay pada setiap milestone.
