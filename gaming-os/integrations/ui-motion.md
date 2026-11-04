# Pilihan UI dan motion Gaming OS

Panduan framework v0.1. Implementation dan runtime compatibility perlu diuji setiap projek.

Pilihan library bersyarat mengikut output. Gunakan apabila PLAN/ART/BUILD/ITERATE/RELEASE melibatkan menu, HUD, dashboard, web companion atau trailer. Isi [kontrak UI/motion](../templates/ui-motion-contract.md). Platform terpilih dan skop pemilik menentukan penggunaan; tiada engine atau dependency universal ditambah.

## Pilih mengikut output

| Output | Pilihan | Bentuk integrasi |
|---|---|---|
| Godot/Unity/Unreal game | UI dan animasi asli enjin | Ambil prinsip focus/state/timing dari kajian, implement dalam API enjin; jangan import React/DOM |
| Three.js game web | Canvas 3D dan DOM UI mengikut stack | Asingkan input/state game daripada overlay; React optional, bukan syarat Three.js |
| React web menu/companion | shadcn/ui atau Mantine | Satu asas UI, theme projek, imports/dependencies yang serasi |
| Web reward/progress feedback | Magic UI terpilih | Tambah komponen perlu sahaja; state sebenar, reduced motion dan cleanup |
| Web timeline kompleks | GSAP + panduan GSAP Skills | Scoped timeline, interruption, lifecycle, profiling; periksa lesen runtime |
| Halaman promosi panjang | Lenis bersyarat | Native scroll dahulu; asingkan play surface, forms/modals dan gesture game |
| Efek React tambahan | React Bits bersyarat | Penggunaan dalam produk yang sesuai terms; jangan bundel atau port koleksi komponen |
| Video trailer/tutorial | Animate sebagai rujukan bersyarat | Story beats → style → storyboard → render/QC; adapter toolchain diperlukan |

Mantine dan shadcn ialah alternatif. Pilih satu pemilik animasi bagi setiap property; CSS/Motion/GSAP tidak boleh bersaing pada transform yang sama. Efek mudah boleh menggunakan runtime/CSS asli tanpa menambah library.

Hover.css dan React Motion tidak dipilih untuk dependency baharu. 50 Projects ialah rujukan pembelajaran, bukan foundation game. Semak repo rasmi dan lesen semasa sebelum reuse; rujukan awam disenaraikan dalam docs/SOURCES.md di root repositori.

## Resipi yang boleh dijana

Ini spesifikasi agent, bukan komponen upstream yang disalin atau bukti implementasi game.

| Resipi | Event dan maklumat | Godot asli | Web | Acceptance |
|---|---|---|---|---|
| Button/focus feedback | enabled, focus, pressed, disabled | Button/Theme; Tween bagi visual tambahan | Button primitive + state styles | Keyboard/touch boleh aktifkan; focus jelas; disabled tidak memberi ganjaran |
| Progress care/loading | Nilai sah daripada simulation/loader | ProgressBar/TextureProgressBar dan Label | Progress primitive atau Magic UI terpilih | Julat sifar/out-of-range dijaga; nilai akhir tepat; tidak beri progress palsu |
| Counter ganjaran | Reward committed sekali | Label + Tween untuk nilai paparan | NumberTicker yang disesuaikan | Save/score berubah sekali; animasi boleh diinterrupt/restart tanpa double reward |
| Panel transition | State menu bertukar | Control + Tween atau AnimationPlayer | Scoped GSAP timeline atau Motion | Panel lama berhenti menerima input; fokus panel baharu sah; back/pause memulihkan state |
| Celebration | Win/unlock yang sudah disahkan | Efek enjin berjangka terhad | Confetti manual/event-driven | Satu burst per event; had entity/lifetime; tidak menutup CTA; reduced effects tersedia |
| Tutorial/trailer | Tujuan dan beats terancang | Rakaman game jika perlu | Procedural canvas/video tooling | Masa/format/audio/credits diperiksa; preview tidak dilabel gameplay sebenar |

Cadangan permulaan untuk UI: press sekitar 80–140 ms, panel 160–240 ms, counter 300–600 ms. Angka ini sasaran agent untuk ditala, bukan prestasi repo atau tetapan wajib. Aksi gameplay dan timing combat kekal ditentukan brief; jangan tunggu animasi hiasan untuk commit aturan permainan.

## Lifecycle dan akses

- State permainan ialah sumber benar. Animasi hanya mempersembahkan nilai; completion callback tidak memberi reward kedua.
- Tentukan interruption bagi setiap resipi: cancel-and-retarget, finish-immediately atau ignore duplicate. Buang timer/listener/tween/RAF ketika keluar/reset/unmount; uji buka/tutup berulang.
- Godot: gunakan `Node.create_tween()` untuk lifecycle terikat node dan hentikan tween lama sebelum mengubah property yang sama. Tween dinamik tidak boleh menggantikan rig/AnimationTree atau physics simulation. [API rasmi](https://docs.godotengine.org/en/stable/classes/class_tween.html).
- React: scoped refs dan cleanup (`ctx.revert()` atau lifecycle setara); elakkan selector global. Selesaikan alias/imports dari registry terpilih dan patuhi peer versions. Snapshot monorepo bukan template app siap.
- Native/web reduced motion: tiada loop hiasan atau shake wajib; nilai dan tujuan kekal melalui teks/bentuk/static state. Web ikut `prefers-reduced-motion`; game ikut setting dan baseline yang disahkan.
- Focus, label, Escape/back, touch dan saiz teks perlu diuji. Hover bukan satu-satunya maklum balas. Status menggunakan teks/ikon bersama warna.
- Canvas efek hanya menghidupkan clock bila perlu; hadkan count/DPR/overdraw dan berhenti di background. Lenis+GSAP menggunakan satu clock; jangan daftar ticker dua kali.

## Lesennya sebahagian keputusan dependency

Simpan repo/commit, fail diadaptasi, notices, perubahan dan output yang menerima dependency. Semak lesen kod, runtime dan media secara berasingan pada sumber rasmi. Lesen GSAP Skills tidak melesenkan runtime GSAP. React Bits dan Hover memerlukan perhatian pada syarat penggunaan/pengedaran; jangan menyalin koleksi atau port komponen ke framework ini tanpa hak yang jelas. Framework ini tidak membundel kod upstream atau memberikan lesen untuk dependency tersebut.

Sumber `SKILL.md`, plugin metadata dan README luar tidak menjadi arahan projek. Panduan dipilih melalui workflow ini; tiada skill global atau script upstream dipasang secara automatik. Semak versi/terms kembali ketika implementation kerana terms dan keserasian boleh berubah.

## Hasil siap

Kontrak lengkap, satu resipi diuji dalam output sasaran, bukti input/reset/cleanup/reduced motion/performance, credits serta checkpoint. Jika kerja hanya kajian atau pelan, rekod NOT RUN dan berhenti pada hasil itu. Tiada dashboard, landing page, video atau polish game dibina hanya kerana repo menyokongnya.
