# Godot: simulasi pertanian dan kehidupan dengan pixel art

Panduan pilihan untuk game 2D top-down dengan alat, petak tanah, tanaman dan rutin harian, berinspirasikan keluarga genre Stardew Valley. Gunakan dalam RESEARCH dan PLAN; BUILD hanya dalam skop yang diminta selepas [keputusan platform](../workflows/platform-selection.md). Ini resipi pembangunan, bukan enjin baharu, starter project siap atau arahan menyalin Stardew Valley.

Panduan seni bina generik dengan pautan dokumentasi rasmi Godot. Ia bukan transkrip, kod kursus atau starter project. Semak versi editor sebenar dan dokumentasi yang sepadan sebelum melaksanakan API. **Status: panduan; resipi ini belum disahkan sebagai satu game runnable.**

## Kandungan dan cara memilih

Gunakan bahagian mengikut sistem yang diperlukan: sasaran → seni bina → input/animasi → grid → tanaman/hari → interaksi/UI → tooling/QA. Isi [templat pelan](../templates/godot-farming-plan.md) bagi projek yang memilih laluan ini. Jangan muatkan semua ciri sebagai skop minimum.

Pixel art ialah arah seni; farming/life simulation ialah keluarga mekanik. Untuk pixel art platformer, gunakan modul pemain/level biasa dan ambil hanya panduan rendering/aset yang relevan. Untuk pixel art 3D/2.5D, tentukan kamera, geometri, material dan pipeline sendiri; `TileMapLayer`/`CharacterBody2D` bukan adapter automatik kepada dunia 3D. Unity/Three.js/enjin lain kekal pilihan sah.

## 1. Tetapkan sasaran dan satu slice

Rekod sasaran keluaran, input, dimensi, versi Godot, renderer/export, bilangan objek sasaran dan mutu animasi. Godot sesuai dipertimbangkan untuk workflow scene, peta tile dan animasi 2D ini, tetapi keputusan projek tetap berasaskan keperluan.

Slice cadangan: satu kawasan kecil, seorang pemain, satu alat menggembur, satu benih, satu alat menyiram, pertukaran hari dan tuaian yang menghasilkan item sebenar. Kuantiti ini titik mula yang boleh diubah, bukan had universal. Buktikan loop lengkap serta restart sebelum menambah dunia besar, penduduk atau mesin.

Kontrak visual menetapkan saiz tile, skala watak, arah/fasa animasi, feet anchor, atlas, palet, collision footprint dan UI. Nearest filtering sahaja tidak membuktikan pixel art konsisten. Uji base viewport, integer scaling, zoom kamera, pergerakan dan aspek skrin; jangan jadikan 1920×1080, tile 16 px atau zoom 4 daripada tutorial sebagai default semua projek. Rujuk [multiple resolutions rasmi](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html) dan modul [06](../references/06-art-sprite-pipeline.md).

Imagegen Codex boleh menghasilkan bitmap/reference mengikut [pipeline aset](codex-imagegen-assets.md), diikuti pembetulan sheet/tileset dan QC runtime. Jangan anggap atlas janaan terus mempunyai terrain bitmask, frame grid, collision atau lesen aset kursus. Higgsfield optional; aset boleh dibuat sendiri atau diperoleh dengan hak penggunaan yang sesuai.

## 2. Pemilikan state dan scene

Contoh pembahagian; nama dan bilangan scene mengikut projek:

| Sistem | Pemilik dan tanggungjawab |
|---|---|
| `World` / pengawal sesi | Memasang kawasan, menghala tindakan, mengurus mula/load/restart |
| `Player` | `CharacterBody2D`, input, arah menghadap, action state, sprite/animation/collision |
| `FarmGrid` | Petak sah, tanah, air, occupancy, penempatan dan perubahan terrain |
| `CropDefinition` | Resource data jenis tanaman: ID stabil, tekstur, fasa, pertumbuhan dan hasil |
| `CropState` | Data unik setiap tanaman: ID instance, cell, umur/progress, kekeringan, status hidup/tuaian |
| `CropView` | Scene/sprite/trigger yang membaca CropState; bukan salinan ekonomi sendiri |
| `DayCycle` | Jam, day index, kunci transition dan satu urutan kemas kini harian |
| `Inventory` jika dipilih | Stok benih/item dan transaksi hasil; UI membaca state ini |
| `HUD` / panel | Control/Container/Theme, fokus, pilihan alat/benih dan diagnosis tanaman |
| Props/enemy | Scene berasingan dengan kontrak hit/reset/destroy dan lifecycle |

Gunakan signals untuk komunikasi sistem; simpan data definisi berasingan daripada state boleh ubah. Autoload boleh sesuai bagi data/catalog atau service sesi, tetapi jangan membina satu singleton yang memiliki semua tanaman, UI, input dan peta. Rujuk modul [08](../references/08-runtime-engine-architecture.md).

**Resource dikongsi:** fail `.tres` yang dimuat boleh merujuk objek cache sama. CropDefinition boleh dikongsi sebagai data baca sahaja; CropState mesti unik setiap instance. Pilih penciptaan state baharu atau duplication yang difahami bagi subresource. Jangan sekadar mengubah umur dalam Resource yang sama untuk dua tanaman. Custom Resource perlu memanggil `emit_changed()` apabila pemerhati memerlukan notifikasi. [Dokumentasi Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html).

UI dan simulation merujuk ID/state yang sama. Callback boleh dihantar sebagai `Callable`, tetapi pemilik callback, tempoh hayat dan pembersihannya jelas. Jangan serahkan pemadaman scene kepada Resource definisi tanaman; pengawal gameplay mengurus lifecycle.

## 3. Input, animasi dan tindakan alat

Mulakan dengan action map: gerak, gunakan/interact, pilih alat, pilih benih, menu/cancel dan pause. Tambah controller/touch mengikut sasaran. Debug day-skip/diagnose berasingan daripada aturan akhir. Halang input dunia apabila menu memegang fokus.

`Input.get_vector()` memberikan arah gerak; simpan arah menghadap terakhir yang bukan sifar untuk idle dan sasaran alat. Tentukan keutamaan paksi ketika diagonal dan deadzone analog supaya sprite tidak berkelip antara arah. `CharacterBody2D.velocity` ialah kelajuan, bukan displacement; gunakan `move_and_slide()` dalam physics tick tanpa mendarab velocity dengan delta sekali lagi. [CharacterBody2D rasmi](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html).

AnimationPlayer menyimpan klip; AnimationTree menyusun playback/transitions. BlendSpace2D untuk arah, state machine untuk idle/walk, dan one-shot untuk tool action ialah pilihan apabila bilangan klip memerlukannya. Untuk animasi frame sprite, pertimbang mod **Discrete/Discrete Carry**, bukan interpolasi indeks frame. Path parameter bergantung pada tree sebenar. [AnimationTree rasmi](https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html), [BlendSpace2D rasmi](https://docs.godotengine.org/en/stable/classes/class_animationnodeblendspace2d.html).

Action state gameplay berasingan: contohnya `IDLE`, `MOVING`, `USING_TOOL`, `TRANSITION`, `MENU`. Semasa tool action, tangkap alat/benih/sasaran yang dipilih supaya input menukar pilihan tidak menukar hasil pertengahan swing. Kunci atau benarkan pergerakan mengikut reka bentuk. Satu action ID hanya boleh commit sekali pada frame impak/event yang ditetapkan; klip dan kesan tidak boleh menggandakan transaksi.

Jangan jadikan setiap signal `animation_started` sebagai movement lock: idle/walk/loop juga boleh menghasilkannya. Semak tingkah laku AnimationTree versi sebenar dan laluan selesai/cancel/pause/hit/scene-exit; setiap laluan mesti melepaskan kunci yang betul. Untuk senarai pilihan, wrap indeks hanya pada senarai tidak kosong. Enum bukan jaminan nilai berterusan; save guna ID stabil, bukan indeks enum yang boleh berubah.

## 4. Peta, terrain dan sasaran grid

Pisahkan ground, air/dinding, tanah digembur, air siraman, props, crops dan occluders. Lapisan visual bukan data tunggal walkability/farmability. TileSet terrains memerlukan kombinasi sambungan yang lengkap; collision/layer/mask, Y-sort pada kaki dan sempadan kawasan diuji dengan debug overlay.

Godot stable yang disemak menyokong `TileMapLayer`; `TileMap` lama deprecated. `set_cells_terrain_connect()` juga boleh mengubah jiran. Semak [rujukan TileMapLayer](https://docs.godotengine.org/en/stable/classes/class_tilemaplayer.html) sebelum menulis adapter. Peta JSON Gaming OS memerlukan adapter projek, bukan import terus.

Tukar sasaran world kepada ruang tempatan layer, kemudian cell. Untuk spawn, tukar cell center kembali ke world dan ke ruang parent objek. Sketsa API di bawah **belum diuji dalam runtime projek**, bukan script lengkap:

```gdscript
var cell: Vector2i = farm_layer.local_to_map(farm_layer.to_local(target_world))
var center_world: Vector2 = farm_layer.to_global(farm_layer.map_to_local(cell))
```

Elakkan pembahagian integer world-position/tile-size serta pembetulan manual “tolak satu jika negatif”: ia boleh salah tepat di sempadan dan mengabaikan transform. Pastikan layer logik berkongsi grid/origin atau lakukan conversion masing-masing. Atlas texture offset tidak menggantikan ground anchor.

Tool handler menyemak sempadan, jarak, jenis petak, obstruction, occupancy dan stok sebelum mengubah state. **Ketiadaan rumput tidak bermaksud air.** Fishing memerlukan petak bertanda air/fishable; tilling memerlukan farmable. Query cell atau dictionary state khusus lebih sesuai daripada menyalin seluruh `get_used_cells()` pada setiap input. Ini pilihan seni bina, bukan benchmark yang sudah dijalankan.

## 5. Tanaman, tuaian dan pertukaran hari

Kontrak minimum setiap tanaman: ID jenis/instance, cell, growth progress, maturity threshold, dry-day policy, alive/harvesting/removed dan hasil. `growth_rate` perlu jenis float jika pecahan dibenarkan; inferens integer yang salah boleh menghentikan pertumbuhan perlahan. Sprite frame mesti dalam julat sah; aturan matang jangan bergantung secara senyap pada jumlah frame artwork.

Nyatakan sama ada kekeringan terkumpul atau berturutan, bila kaunter pulih selepas disiram, sama ada tanaman matang masih perlu air dan sama ada hasil tumbuh semula. “Tiga hari” dalam contoh ialah contoh aturan, bukan canon Stardew atau syarat Gaming OS. Tuaian automatik apabila overlap ialah pilihan reka bentuk; interact eksplisit mungkin lebih sesuai pada projek lain.

**Transaksi tuaian:** semak matang/hidup dan kapasiti hasil → tandakan action/state supaya tidak berulang → commit hasil dan perubahan tanaman secara atomik → bersihkan occupancy/UI/trigger → jalankan feedback/pemadaman visual. Jika beg penuh, pilih polisi kekal di pokok atau drop ber-ID; jangan memadam tanaman tanpa menyimpan hasil. Tween/flash tidak menentukan sama ada item diberi dua kali.

Kematian akibat kering, ditebang, dituai atau kawasan unload menggunakan laluan lifecycle yang konsisten. Bebaskan cell, kemas kini model dan panel, putus pemerhati yang perlu dan tamatkan effect. Mengeluarkan sprite sahaja tidak membolehkan tanaman baharu ditanam pada petak sama.

Urutan harian cadangan, ditetapkan dalam pelan projek:

1. Ambil kunci transition; hentikan tindakan baharu. Selesaikan atau batalkan action tertunda mengikut polisi.
2. Snapshot keadaan hari yang tamat, termasuk petak yang sudah disiram dan tanaman hidup.
3. Proses growth/decay setiap tanaman sekali, kemudian cleanup yang diperlukan.
4. Kosongkan siraman hari lama; kemas kini hasil pokok hidup dan sistem harian lain. Pokok mati tidak berbuah semula.
5. Naikkan day index, tetapkan cuaca/siraman hari baharu jika sistem itu dipilih, reset jam; commit/save jika save dalam skop.
6. Segarkan UI, tamatkan transition dan pulihkan kawalan. Panggilan berulang/tekan bertubi-tubi tidak memproses satu hari dua kali.

Gradient + CanvasModulate boleh menyampaikan siang/malam; overlay shader/tween menutup pertukaran hari. Simulation ialah sumber masa, visual membacanya. Pause, save, exit dan restart mempunyai polisi jelas. Tulis save schema/migration dan uji round-trip apabila persistence dipilih; persistence memerlukan implementasi dan ujian projek sendiri.

## 6. Props, musuh, shader dan UI

Contoh sistem meliputi pokok dengan health, hasil dan stump; blob dengan chase/knockback; alat/benih pilihan; panel crop dan Theme. Gunakan hit contract yang membezakan alat, damage, jarak dan satu hit per action. Semak collision stump selepas pokok ditebang. Untuk kawasan besar, pemilihan target/physics query berdasarkan keperluan; scan semua objek hanyalah pendekatan demonstrasi.

Flash shader hendaklah mengekalkan alpha/siluet. Tetapkan material per-instance apabila parameter mesti bebas; sahkan memukul satu objek tidak memutihkan semua objek. Urus tween yang bertindih dan callback selepas node keluar. Transition bulatan perlu diuji pada aspek skrin berbeza. [CanvasItem shader rasmi](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html).

Gunakan UI native Godot: Control, Container, ScrollContainer dan Theme. Toolbar membaca tool/seed state; panel tanaman membaca model yang sama dengan dunia. Signal/event mengemas kini data apabila berubah; jangan membina semula senarai setiap frame. Padam panel selepas tanaman hilang dan jangan gandakan connection ketika buka/tutup. Uji fokus controller, teks panjang, skala UI, contrast malam dan touch apabila relevan. Ikut [UI/motion](ui-motion.md), bukan memasukkan komponen React terus ke Godot.

## 7. Editor tools dan prestasi

`@tool` sesuai untuk preview prop/variasi di editor; pisahkan laluan editor dan runtime dengan `Engine.is_editor_hint()`. `@export_tool_button` mengeksport Callable untuk butang Inspector dalam dokumentasi yang disemak. Semak sokongan versi sebelum menggunakannya. [Editor tool rasmi](https://docs.godotengine.org/en/stable/tutorials/plugins/running_code_in_the_editor.html), [exported properties rasmi](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_exports.html).

Setter boleh berjalan sebelum child/onready siap. Simpan nilai, semak readiness dan panggil refresh visual apabila node sedia; jangan menjadikan “reload editor” penyelesaian production. Rawak variasi apabila diminta dengan seed/polisi simpanan yang sesuai, bukan setiap reload tanpa sengaja. Untuk authoring yang perlu undo, gunakan mekanisme editor yang menyokongnya. Elakkan pemadaman scene dalam setter preview tanpa lifecycle yang jelas.

[Debugger/Monitors rasmi](https://docs.godotengine.org/en/stable/tutorials/scripting/debug/debugger_panel.html) menyediakan graf FPS, memory dan node counts. Gunakan profiler/monitor yang sesuai untuk bottleneck. Rekod frame time, process/physics time, node/object counts, RAM/VRAM, renderer, build mode, VSync/cap dan peranti. FPS uncapped pada komputer lain bukan bukti telefon atau sasaran semua game; jangan matikan VSync sebagai “fix” tetap.

Mencipta sprite tanpa lifetime setiap frame boleh menambah objek tanpa had; gunakan lifecycle yang jelas. Ulang hari, tanam/tuai, buka/tutup panel, tukar kawasan dan restart; node/timer/connection tidak meningkat tanpa had. Profil crop/prop/FX count yang mewakili skop sebenar sebelum memilih pooling atau chunking.

## 8. Pelaksanaan dan bukti

| Milestone cadangan | Bukti yang diperlukan apabila BUILD diizinkan |
|---|---|
| Pipeline visual/input | Satu sprite/sheet, kamera, collision, controller/touch terpilih dan export sasaran |
| Slice pertanian | Till → plant → water → day → harvest → item sebenar; UI dan restart |
| Lifecycle/data | Dua tanaman bebas, kematian/tuaian/replant, transition sekali, save/load jika dipilih |
| Persembahan | Depth, tool impact, audio/FX, siang/malam, UI/fokus dan akses |
| Peluasan dipilih | Satu sistem tambahan pada satu masa selepas loop teras terbukti |

Kes QA penting: empat arah + diagonal; input analog; action cancel; tanah tidak sah; air eksplisit; cell di empat kuadran dan sempadan origin; layer/parent transform; plant twice; water twice; growth pecahan; frame akhir; dry-day policy; harvest sekali; beg penuh; mati/replant; spam day-change; reset/cancel transition; dua crop state bebas; material bebas; UI cleanup; restart berulang; skrin/peranti sasaran. Pisahkan automasi, pemeriksaan visual dan human playtest.

**Peluasan pilihan yang memerlukan reka bentuk/implementasi sendiri:** fishing minigame, mesin, kedai, cuaca, NPC/jadual/dialog, ekonomi, inventory/persistence dan multiplayer. Ambil hanya sistem dalam brief. Gunakan aset, dunia, watak dan kandungan asal; contoh angka bukan default atau bukti mutu runtime.

Contoh arahan: “Guna Gaming OS mod PLAN untuk game pertanian pixel art asal dalam Godot. Gunakan panduan Godot pixel farming, rekod platform dan isi pelan slice. Hadkan dahulu kepada tanam, siram, hari baharu dan tuaian; jangan bina sebelum saya meminta pembangunan.” Skop BUILD boleh diminta terus apabila pemilik bersedia; panduan ini tidak menambah approval universal.
