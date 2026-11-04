# Pemilihan platform sebelum membina game

Digunakan dalam PLAN dan sebagai prasyarat BUILD. Baca modul [08](../references/08-runtime-engine-architecture.md), isi [keputusan platform](../templates/platform-decision.md), dan hubungkan ke brief serta state permainan.

## Urutan

Pilihan platform yang disediakan termasuk **Godot, Unity dan Three.js**. Gunakan [panduan Unity/Three.js](../integrations/unity-threejs.md) untuk membanding enjin editor dengan asas runtime 3D web; Three.js memerlukan pemilihan sistem gameplay tambahan. Unreal/Phaser/runtime lain masih calon apabila brief memerlukannya.

1. Tetapkan bentuk permainan (2D/2.5D/3D), kamera, sasaran keluaran/peranti dan tindakan utama. Dapatkan rujukan mutu animasi serta gameplay, kemudian tulis acceptance yang boleh diperiksa.
2. Bezakan enjin/runtime, alat penghasilan aset/animasi dan platform keluaran. Jangan pilih engine kerana satu prompt contoh menggunakannya.
3. Semak dokumentasi rasmi semasa untuk keperluan wajib. Banding calon relevan; rekod keupayaan alat/perkakasan sebenar sebagai VERIFIED atau UNKNOWN, bukan andaian pemasangan.
4. Rekod satu engine terpilih, versi sasaran, alat aset, format handoff, alasan, kos/batas dan alternatif bersyarat. Jika fakta penting belum tersedia, kekalkan keputusan sebagai CANDIDATE dan teruskan penyelidikan/pelan yang tidak bergantung padanya.
5. Hanya mula membina game setelah status SELECTED direkod. Ini keputusan teknikal dalam kebenaran kerja sedia ada, bukan permintaan approval baharu secara automatik. Jika pengguna hanya meminta kajian atau pelan, tamatkan pada deliverable itu.
6. Dalam skop pembangunan yang diizinkan, uji import/export dan slice teknikal selepas pemilihan: satu aset, animasi, kawalan, collision dan build sasaran. Rekod NOT RUN/PASS/FAIL dengan log/peranti. Jangan memperbanyak aset final sebelum pipeline yang diperlukan terbukti.

## Kriteria keputusan

Bagi simulasi pertanian/kehidupan pixel art 2D, gunakan [panduan Godot pixel farming](../integrations/godot-pixel-farming.md) sebagai calon pipeline dan [pelan khusus](../templates/godot-farming-plan.md) selepas keperluan dikenal pasti. Transkrip tutorial bukan alasan memilih Godot secara automatik; banding sasaran, toolchain dan handoff sebenar seperti langkah di atas.

Selepas output/enjin dipilih, gunakan [integrasi UI/motion](../integrations/ui-motion.md) jika interface atau animasi persembahan sebahagian skop. Pemilihan repo UI tidak mendahului atau menggantikan pemilihan engine; catat runtime native vs web, dependency/import, budget dan terms dalam kontrak berkaitan.

Tapis dahulu sasaran export, jenis animasi, physics/input, keserasian pipeline, ketersediaan alat/perkakasan dan bajet/lesen. Kemudian banding masa iterasi, tooling level, kemahiran pasukan, profiling dan penyelenggaraan. Sokongan teori tidak sama dengan bukti projek.

Gameplay interaktif dan animasi perlu diperiksa bersama: timing aksi, interruption, blending/frames, hitbox dan camera feedback. Enjin sahaja tidak menjamin hasil. Jika platform keluaran, dimensi atau mutu sasaran berubah, semak keputusan semula sebelum meneruskan kerja yang bergantung padanya.

Untuk projek sedia ada, semak dan rekod stack sedia ada; jangan migrasi tanpa sebab yang berpunca daripada keperluan. Kontrak sprite/atlas dan peta 2D v0.1 digunakan hanya jika sesuai. Projek 3D perlu spesifikasi mesh, rig, materials, unit/axes, clip dan scene tersendiri.
