# Keputusan platform permainan

- Game ID / brief / tarikh / penulis keputusan:
- Status keputusan: UNDECIDED / CANDIDATE / SELECTED / REVISIT:
- Arahan/pilihan pemilik yang menjadi asas:

## Sasaran dahulu

- 2D / 2.5D / 3D; kamera dan perspektif:
- Genre / tindakan utama / model physics dan collision:
- Platform keluaran (browser/native/OS), peranti baseline dan input:
- Rujukan visual/animasi; unsur yang hendak dicapai:
- Animasi: frame-by-frame / skeletal 2D / rig 3D; klip, transition dan interruption:
- Root motion / in-place / IK / facial / cutscene jika perlu:
- Acceptance gameplay: respons input, timing aksi, hitbox, state dan restart:
- Acceptance visual: skala, peralihan, readability, deformasi dan lighting:
- Bajet fps/frame time, loading, memory dan saiz build; cadangan vs ukuran:

## Calon dan keperluan wajib

Nilai Godot, Unity atau Three.js mengikut sasaran; calon lain juga dibenarkan. Rujuk [panduan Unity/Three.js](../integrations/unity-threejs.md). Jika Three.js dipilih, isi pemilik/dependency untuk input, collision/physics, gameplay state, audio/save dan UI; ia tidak dibekalkan sebagai satu enjin lengkap.

| Calon enjin | Export sasaran | Animasi/physics wajib | Pipeline aset | Alat/perkakasan | Kos/lesen | Alasan pilih/tolak; sumber |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Setiap sel: PASS / FAIL / UNKNOWN dengan asas. Ini semakan keperluan dokumentasi; jangan gunakan PASS untuk ujian runtime yang belum dibuat. Calon gagal keperluan wajib tidak boleh dipilih hanya kerana markah pilihan lain.

## Toolchain terpilih

- Enjin utama / versi sasaran / renderer / bahasa atau visual scripting:
- Sistem tambahan jika runtime library (contohnya Three.js) / versi / alasan / status ujian:
- Alat model/sprite/rig/animasi/texture/audio dan versi:
- Pemasangan/kebolehlaksanaan pada mesin: VERIFIED / UNKNOWN; bukti:
- Format source → export → import; plugin/importer jika ada:
- Unit/axes, pivot/origin, skeleton, clip naming dan materials:
- Kontrak aset/scene yang digunakan; penyesuaian 3D jika perlu:
- Sebab memenuhi sasaran; kompromi yang diterima:
- Alternatif dan keadaan yang membenarkan pertukaran:
- Lesen/kos disemak pada tarikh; perkara terbuka:

## Bukti selepas pemilihan

| Ujian slice teknikal | Acceptance | NOT RUN / PASS / FAIL | Build/peranti/log |
|---|---|---|---|
| Import satu aset dan animasi | | NOT RUN | |
| Kawalan + collision + feedback | | NOT RUN | |
| Transition/interruption/loop | | NOT RUN | |
| Export dan jalankan pada sasaran | | NOT RUN | |
| Prestasi dan restart | | NOT RUN | |

- Ketidakpastian/blocker; next action:
- Pemilihan direkod sebelum build pada:
- Pipeline boleh diperluas kepada aset final: BELUM TERBUKTI / TERBUKTI; asas:
- Review/approval pemilik hanya jika diminta: status dan bukti sebenar:
