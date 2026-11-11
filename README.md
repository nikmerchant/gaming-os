# Gaming OS

Build by [CaknaAI team](https://caknaai.com/)

**A reusable, file-based workflow for designing, building and improving original games with AI coding assistants.**

Gaming OS menghubungkan idea, pemilihan enjin, gameplay, aset, pembangunan, QA dan memori projek. Dokumentasi utama menggunakan **Bahasa Melayu**, dengan istilah teknikal dikekalkan. Ia sebuah framework kerja; bukan sistem operasi komputer, game engine atau koleksi game siap.

## Kandungan

- **12 mod kerja:** RESEARCH, IDEATE, PLAN, ART, ASSET, BUILD, PLAYTEST, DIAGNOSE, ITERATE, RELEASE, CONTINUE dan EDUCATE.
- **14 modul** untuk identiti asal, core loop, input/physics, dunia, art/animasi, peta, seni bina, feedback, progression, mobile, QA, pembelajaran dan kesinambungan.
- Templat brief, keputusan platform, state/checkpoint, aset/peta, QA/playtest dan kontrak UI/motion.
- Panduan Godot pixel farming, Unity/Three.js, UI/motion dan aset bitmap melalui Codex Imagegen apabila tersedia.
- Arahan bersama untuk Codex dan Claude Code, satu kanon framework dan memori pengguna yang disimpan secara persendirian.

Godot, Unity, Three.js, Unreal, Phaser atau runtime lain dipilih mengikut sasaran gameplay, animasi dan platform keluaran. Blender ialah alat aset/rig/animasi, bukan pengganti keputusan enjin. Tiada enjin atau provider aset diwajibkan. Higgsfield optional.

## Mula menggunakan

1. Clone atau muat turun repositori ini ke folder baharu:

   ```sh
   git clone https://github.com/nikmerchant/gaming-os.git
   cd gaming-os
   ```

2. Untuk memori kerja tempatan, jalankan dengan Python 3.10 atau lebih baharu:

   ```sh
   python tools/init_workspace.py
   ```

   Ini mencipta fail kosong berstruktur dalam `workspace/`, yang diabaikan Git. Ia tidak mencipta game, memilih enjin, memasang alat atau menyalin rekod projek orang lain. Python hanya diperlukan untuk helper dan validator, bukan untuk membaca framework.

3. Buka folder ini dalam alat pilihan dan minta:

   > Guna Gaming OS dalam mod PLAN untuk game asal saya. Tetapkan sasaran gameplay, animasi dan platform keluaran; bandingkan enjin yang relevan, kemudian sediakan brief dan satu slice kecil. Simpan keputusan dalam workspace persendirian. Hasil sesi ini pelan sahaja.

4. Baca [pintu masuk](gaming-os/SKILL.md), [router](gaming-os/workflows/router.md) dan modul relevan. Apabila bersedia membina, minta BUILD untuk skop yang jelas. Pemilihan enjin mendahului pembangunan; uji pipeline kecil sebelum memperbanyak aset final.

**Codex:** gunakan `AGENTS.md` dan fail kanon `gaming-os/` dalam folder projek. Tiada skill global atau MCP dipasang oleh repo ini.

**Claude Code:** `CLAUDE.md` mengimport `AGENTS.md`; wrapper projek `.claude/skills/gaming-os/SKILL.md` merujuk kanon sama. Ketersediaan penemuan skill dan alat bergantung pada versi/sesi. Memori kekal pada fail workspace sendiri, bukan salinan kanon berasingan.

Alat lain juga boleh membaca Markdown secara terus. Plugin, image generation, editor dan SDK perlu tersedia serta dikonfigurasi sendiri; repo ini tidak membekalkan akses akaun atau kredit. Hanya satu alat menyunting fail workspace yang sama pada satu masa.

## Pilih panduan

| Keperluan | Pintu masuk |
|---|---|
| Idea, pelan, build atau sambung | [Router 12 mod](gaming-os/workflows/router.md) |
| Pilih enjin dan alat aset | [Pemilihan platform](gaming-os/workflows/platform-selection.md) |
| Simulasi pertanian pixel art 2D | [Godot pixel farming](gaming-os/integrations/godot-pixel-farming.md) |
| Unity atau 3D web | [Unity/Three.js](gaming-os/integrations/unity-threejs.md) |
| Menu/HUD dan motion | [UI/motion](gaming-os/integrations/ui-motion.md) |
| Bitmap/reference Imagegen | [Aset Codex Imagegen](gaming-os/integrations/codex-imagegen-assets.md) |
| Brief, kontrak dan bukti | [Templat](gaming-os/templates/) |

## Privasi dan skop repo

Repo ini hanya membekalkan framework, templat generik dan alat pemeriksaan. **Tiada game persendirian, aset game, save pemain, cerita/rancangan game, transkrip, corpus berbayar, sejarah perbualan, rekod kerja peribadi atau kredensial disertakan.**

Simpan game dan bahan sensitif dalam repo/folder berasingan atau lokasi yang diabaikan Git. Jangan menerbitkan folder kerja peribadi secara keseluruhan. `.gitignore` sahaja tidak mengeluarkan fail yang sudah pernah di-commit; ikuti [panduan penerbitan](docs/PUBLICATION.md).

## Pemeriksaan

```sh
python tools/validate_public.py
python -m unittest discover -s tests
```

Validator memeriksa senarai fail awam, hash, pautan tempatan, beberapa corak sensitif dan contoh kontrak. Ia tidak membuktikan game menyeronokkan, integrasi enjin telah diuji atau semua kebocoran maklumat dapat dikesan. Semakan kandungan manusia tetap diperlukan sebelum menambah fail baharu.

Framework ini versi awal. Panduan teknikal perlu dipadankan dengan versi alat sebenar. Bezakan ujian automatik, pemeriksaan visual dan human playtest; jangan melabel prompt atau concept art sebagai aset runtime siap.

## Sumbangan dan lesen

Lihat [CONTRIBUTING](CONTRIBUTING.md) untuk perubahan framework. Jangan sertakan projek pengguna atau bahan berlesen pihak ketiga dalam sumbangan.

[MIT License](LICENSE) meliputi kandungan asal framework ini. Enjin, library, plugin, fon, media dan aset luar kekal di bawah lesen masing-masing; lihat [sumber primer](docs/SOURCES.md). MIT tidak menukar hak kandungan pihak ketiga menjadi milik repo ini.
