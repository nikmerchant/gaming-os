# Router Gaming OS

Pilih mod daripada **hasil yang diminta**, bukan nama permainan dalam reference. Jika pengguna meminta idea sahaja, tamatkan dengan idea; jika meminta build dan skop jelas, teruskan sampai build serta ujian yang relevan.

| Mod | Kegunaan | Modul minimum | Hasil utama |
|---|---|---|---|
| RESEARCH | Kaji sumber/mekanik/tool | 01, 02, 14 | Sintesis, sumber dan batas bukti |
| IDEATE | Cipta/pilih konsep | 01, 02, 03 | Konsep asal, loop, risiko, pilot |
| PLAN | Rancang permainan dan pilih platform builder | 01, 03, 04, 05, 08, 11, 14 | Sasaran, keputusan enjin/alat aset, brief, level, QA |
| ART | Tetapkan arah seni | 02, 06, 07, 09 | Art contract, anchor dan spesifikasi |
| ASSET | Jana/proses aset | 06; 07 jika peta; 09 jika audio/FX | Fail sebenar, provenance, manifest, QC |
| BUILD | Bina prototaip | 03, 04, 05, 08, 11, 12, 14 | Gameplay runnable dan bukti ujian |
| PLAYTEST | Nilai bermain/balance | 03, 10, 11, 12 | Protokol, dapatan sebenar dan tindakan |
| DIAGNOSE | Cari punca bug/feel | 08, 12, 14 + modul sistem terkesan | Repro, punca dan fix terkawal |
| ITERATE | Tingkatkan hasil | 09, 10, 12, 14 + modul berubah | Perubahan fokus, regression dan state |
| RELEASE | Sediakan pakej akhir | 08, 11, 12, 14 | Build, README, credit, limitation |
| CONTINUE | Sambung checkpoint | 14 dahulu; kemudian mod aktif | State dipulih dan tindakan diteruskan |
| EDUCATE | Reka pembelajaran melalui game | 02, 03, 11, 13 | Learning brief dan reka assessment |

## Modul

| ID | Fail | Peranan |
|---|---|---|
| 01 | [Game architecture](../references/01-game-architecture.md) | Pipeline dan skop |
| 02 | [Idea dan identiti](../references/02-idea-originality.md) | Konsep dan originaliti |
| 03 | [Core loop](../references/03-core-loop-rules.md) | Aturan dan state |
| 04 | [Player dan input](../references/04-player-input-physics.md) | Kawalan dan physics |
| 05 | [Level](../references/05-world-level-design.md) | Dunia dan difficulty layout |
| 06 | [Sprite](../references/06-art-sprite-pipeline.md) | Aset dan animasi |
| 07 | [Peta](../references/07-map-runtime-contract.md) | Layer, props dan collision |
| 08 | [Runtime](../references/08-runtime-engine-architecture.md) | Enjin dan kod |
| 09 | [Feedback](../references/09-feedback-audio-vfx.md) | UI, audio dan VFX |
| 10 | [Progression](../references/10-progression-balance.md) | Skor, wave, ekonomi dan tuning |
| 11 | [Mobile](../references/11-mobile-accessibility-performance.md) | Telefon, akses dan prestasi |
| 12 | [QA](../references/12-qa-playtest-release.md) | Ujian dan release |
| 13 | [Pendidikan](../references/13-learning-game-design.md) | Objektif pembelajaran pilihan |
| 14 | [Continuity](../references/14-continuity-memory.md) | Memori dan checkpoint |

ID di atas merujuk modul Gaming OS. Apabila dua mod diperlukan, buat turutan yang berasaskan kebergantungan; contohnya PLAN → ASSET → BUILD. Gate projek hanya terpakai jika diminta atau sudah direkod sebagai pilihan pemilik.

Permintaan memilih Godot/Unreal/Blender atau platform builder menggunakan RESEARCH → PLAN dan [workflow pemilihan platform](platform-selection.md). Sebelum apa sahaja BUILD, keputusan platform mesti direkod; ini termasuk prototaip mekanik. Pengesahan pipeline dibuat selepas pemilihan, sebelum memperbanyak aset final. Tiada 2D/browser/Canvas default yang menggantikan keputusan tersebut.

Permintaan Unity atau Three.js turut menggunakan RESEARCH dan PLAN → BUILD apabila pembangunan diizinkan. Baca [panduan Unity/Three.js](../integrations/unity-threejs.md) bersama modul 08; pilih output dan pipeline terlebih dahulu, kemudian semak sistem gameplay yang perlu ditambah bagi Three.js. Godot/Unreal/Phaser kekal pilihan mengikut projek.

## Routing Godot pixel farming

Permintaan panduan game pertanian/kehidupan pixel art ala Stardew menggunakan RESEARCH dan PLAN dengan [panduan Godot pixel farming](../integrations/godot-pixel-farming.md) dan [templat pelan](../templates/godot-farming-plan.md). Untuk BUILD yang sudah diizinkan dan Godot sudah dipilih, ambil bahagian input/animasi/grid/crops/day cycle/UI/QA yang relevan bersama modul03/04/06/07/08/12/14. ART/ASSET menggunakan kontrak visual dan pipeline aset biasa. DIAGNOSE/ITERATE membaca bahagian sistem yang berubah sahaja.

Transkrip ialah rujukan teknikal 2D; contoh angka, aset kursus dan promosi premium tidak menjadi canon atau ciri wajib. Pixel art 3D memerlukan keputusan/pipeline sendiri. Panduan tidak memilih enjin atau menyambung mana-mana game secara automatik.

## Routing UI, motion dan repo

Untuk permintaan aset melalui Imagegen Codex, gunakan ART/ASSET dengan [pipeline Imagegen](../integrations/codex-imagegen-assets.md), modul06 dan kontrak aset projek. Mod07 diperlukan bagi latar/peta; model 3D tetap mengikuti pipeline mesh/rig projek. Planning sahaja tidak mengaktifkan generation. Pilihan alat ini tidak menyambung game yang sedang dihentikan.

Untuk UI/menu/HUD atau animasi interface, muatkan [integrasi UI/motion](../integrations/ui-motion.md) selepas keputusan platform. PLAN menetapkan [kontrak](../templates/ui-motion-contract.md); ART menetapkan states/style/timing; BUILD dan ITERATE melaksanakan serta menguji resipi yang relevan; RELEASE menyemak dependency/notices dan output. Modul 08/09/11/12 menghubungkan implementation, feedback, akses/prestasi dan QA.

Kajian repo menggunakan RESEARCH → PLAN, bukan arahan membina dashboard atau menukar engine game. Video promosi yang diminta menggunakan ART/ASSET/RELEASE serta skill media yang sesuai; Animate ialah rujukan bersyarat dan memerlukan toolchain disahkan. Game enjin asli menggunakan UI/animation API enjin; repo React/DOM hanya dipilih untuk output web yang sesuai. Semak sumber primer dan lesen dependency yang benar-benar digunakan.
