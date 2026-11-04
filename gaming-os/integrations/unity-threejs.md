# Pilihan platform: Unity dan Three.js

Panduan framework v0.1. Unity dan Three.js ialah pilihan platform pembangunan Gaming OS bersama Godot. Unreal, Phaser dan runtime tersuai masih boleh dinilai apabila relevan. Ini panduan pemilihan/pelaksanaan, bukan pemasangan atau pengesahan build pada mesin pengguna.

## Peranan dan pemilihan

| Pilihan | Peranan | Calon apabila | Keputusan tambahan |
|---|---|---|---|
| Godot | Enjin game dan editor 2D/3D | Pipeline/editor Godot memenuhi brief | Versi, renderer, bahasa dan export sasaran |
| Unity | Enjin dan editor 2D/3D; scripting C# | Projek memerlukan workflow Unity untuk mobile/desktop atau output lain yang disahkan | Editor/build modules, render pipeline, packages, bahasa, output dan lesen |
| Three.js | Library 3D JavaScript sebagai asas runtime game web | Sasaran 3D dalam browser dengan scene, model dan interface web tersuai | Sistem input, gameplay state, collision/physics, audio, save dan loading dipilih/dibina berasingan |

Three.js boleh digunakan membina game, tetapi bukan enjin lengkap dengan semua sistem gameplay tersedia. React bukan syarat; JavaScript/TypeScript biasa boleh dipilih. Pemilihan React wrapper ialah keputusan dependency berasingan, bukan default Gaming OS. Unity juga tidak dipilih secara automatik kerana library UI web tersedia.

Sumber primer: [Unity Engine](https://unity.com/products/unity-engine), [Three.js Making a Game](https://threejs.org/manual/pages/game.html). Pemilihan kesesuaian di atas ialah cadangan kejuruteraan; mutu dan prestasi memerlukan bukti projek.

## Pipeline aset dan animasi

**Unity:** simpan source Blender, eksport FBX/tekstur mengikut kontrak, kemudian import dan semak skala, orientasi, rig, klip serta materials pada render pipeline terpilih. Dokumentasi Unity menyatakan FBX sebagai format model utama. Jangan anggap shader Blender atau GLB sedia ada terus serasi tanpa importer dan ujian yang sesuai. [Unity importing a model](https://docs.unity.com/en-us/engine/6000.6/manual/assets-and-media/asset-types/models/importing/importing-model-files).

**Three.js:** Blender → glTF/GLB → `GLTFLoader`; klip daripada aset dimainkan melalui `AnimationMixer`. Pastikan animasi dikemas kini menggunakan masa yang betul dan lifecycle loader/mixer/scene diurus. Semak clip naming, textures/materials, unit dan kamera pada browser sebenar. [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html), [AnimationMixer](https://threejs.org/docs/pages/AnimationMixer.html).

Higgsfield untuk Blender kekal optional. Tanpa sambungan, gunakan Blender biasa, procedural atau aset berlesen yang sesuai. Provider aset tidak menentukan enjin, dan imej/mesh cantik belum membuktikan rig atau gameplay berfungsi.

## Kontrak sebelum BUILD

Isi [keputusan platform](../templates/platform-decision.md) selepas menetapkan sasaran animasi/gameplay/platform keluaran. Rekod engine/library, versi, bahasa, renderer/pipeline, input, collision/physics, animation controller, save/audio, format aset, deployment dan bajet. Bagi Three.js, nyatakan siapa menyediakan setiap sistem gameplay yang tidak datang daripada library itu.

Jika UI/motion sebahagian skop, ikut [panduan UI/motion](ui-motion.md): Unity menggunakan UI/animasi asli yang dipilih projek; Three.js boleh menggabungkan canvas 3D dengan DOM UI. Asingkan state simulation daripada nilai paparan dan tentukan pemilik input/focus setiap lapisan. Repo React hanya digunakan apabila stack projek memerlukannya.

## Bukti minimum selepas pemilihan

1. Import satu model dan mainkan klip utama; semak scale/material/rig serta transition.
2. Uji input, collision, win/fail/pause dan restart dalam slice kecil.
3. Unity: build/jalankan pada platform sasaran; editor preview sahaja belum membuktikan build. Semak modules/SDK dan keserasian packages.
4. Three.js: jalankan melalui HTTP/dev server; semak URL aset/subpath, loading/error state, resize, pointer/touch, tab background dan cleanup semasa restart.
5. Ukur loading/frame time/memory serta worst-case effects pada peranti/browser baseline. Catat PASS/FAIL/NOT RUN berasingan daripada semakan dokumentasi.

Versi dan renderer tidak dipin pada tahap OS; tentukan setiap projek dan simpan lockfile/package metadata yang relevan. Menambah pilihan platform tidak mengubah engine projek sedia ada tanpa arahan migrasi. Runtime Unity/Three.js belum diuji oleh penambahan panduan ini.
