# 08 - Runtime dan seni bina enjin

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Pemilihan stack

Sebelum membina apa sahaja game, tetapkan sasaran gameplay, kaedah animasi, dimensi/kamera dan platform keluaran. Ikut [workflow pemilihan](../workflows/platform-selection.md) dan rekod [keputusan platform](../templates/platform-decision.md). Tiada engine default. Bezakan enjin/runtime (Godot, Unity, Three.js, Unreal, Phaser atau runtime tersuai), alat aset/rig/animasi (contohnya Blender) dan platform keluaran (contohnya Windows/browser/Android).

Godot menjadi calon bagi 2D/3D berasaskan editor; Unreal bagi keperluan animasi watak 3D yang kompleks; Unity apabila workflow/ekosistemnya memenuhi projek; Phaser bagi 2D web; Canvas modular bagi skop kecil yang bersebab. Ini cadangan bersyarat, bukan penarafan mutu. Kekalkan stack sedia ada apabila memenuhi brief. Semak dokumentasi rasmi enjin terpilih serta pipeline import/export yang diperlukan.

Unity dan Three.js ialah pilihan platform yang tersedia dalam panduan. Ikut [panduan pelaksanaan](../integrations/unity-threejs.md): Unity enjin/editor dengan C#; Three.js library 3D untuk asas runtime web, dengan input/game state/collision/physics dan sistem lain dipilih/dibina mengikut brief. Tiada dakwaan Three.js menyediakan semua sistem enjin lengkap atau bahawa kedua-dua toolchain sudah diuji.

Sahkan satu handoff aset, animasi, input/collision dan export dalam slice teknikal selepas pemilihan. Enjin sahaja tidak menjamin animasi atau gameplay. Kontrak sprite/peta v0.1 bukan kontrak mesh/rig/material 3D; tentukan adapter dan kontrak projek sebenar sebelum production. TypeScript atau Node/Vite tidak diwajibkan semua game.

Sahkan versi/compatibility semasa dan simpan lockfile apabila menggunakan package manager. Jangan menyalin versi daripada contoh lama sebagai fakta keserasian. Runtime permainan tidak perlu memanggil API generation selepas aset dihantar melainkan brief meminta feature itu.

## Pemisahan sistem

Untuk projek pertanian/kehidupan 2D pixel art yang menggunakan Godot, ikut [panduan khusus](../integrations/godot-pixel-farming.md): pemilikan grid, definisi/state tanaman, action commit, daily transaction, UI pemerhati dan lifecycle. Panduan memautkan API rasmi; ia belum starter project atau bukti runtime. Pelan dan kes QA dalam [templat](../templates/godot-farming-plan.md).

Bootstrap hanya initialize. Game/session memiliki state dan lifecycle. Input menghasilkan actions. Player/enemy/weapon mengubah simulation. Level/content menyimpan data. Asset loader memiliki path/metadata. Renderer menggambar, HUD membaca state, audio/FX mendengar events. Elakkan UI dan simulation menyimpan health/score berasingan.

Simulation dan render dipisahkan. Atur update order secara jelas: actions → movement → collision/combat → consumed objects → state transition → HUD/render. Fast-speed mode mengubah semua simulation clocks yang relevan secara konsisten; UI input tidak perlu dipercepat.

## Runtime reliability

Untuk interface/motion, ikut [panduan integrasi](../integrations/ui-motion.md). Pilih satu pemilik setiap animasi/property; state simulation ialah sumber benar. Game native menggunakan UI/Tween/AnimationPlayer enjin, output React menggunakan primitive dan dependencies serasi. Bersihkan scoped animations/timers/listeners/RAF ketika exit/reset/unmount. Lenis hanya untuk scroll halaman yang memerlukannya, bukan camera/input game.

Assets dimuat sekali; missing asset mempunyai error bermakna. Projectile/effects mempunyai lifetime dan disposal; pooling dipilih apabila profiling menunjukkan keperluan. Restart tidak menduakan listener/timer. Jalankan modular web game melalui local HTTP server; ES modules/fetch boleh gagal melalui file://. Run report merekod command, port sebenar, URL dan build mode.
