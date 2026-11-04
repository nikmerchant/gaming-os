# 06 - Arah seni, sprite dan animasi

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Art contract

Rekod kamera, perspektif, gaya pixel/pixel-inspired/HD, palet, lighting, skala actor, outline, texture density dan readability pada saiz runtime. Gunakan master/anchor yang mengekalkan identiti dan scale, kemudian satu sheet bagi setiap action supaya drift mudah diperiksa. Wide slash, projectile, impact dan dust menjadi FX tersendiri apabila perlu.

## Pipeline aset

Codex boleh menghasilkan aset melalui Imagegen sendiri apabila sesuai dan tersedia. Gunakan [pipeline Imagegen Codex](../integrations/codex-imagegen-assets.md) untuk concept art, sprite, latar, ikon dan calon tekstur. Provider khusus dalam brief kekal dihormati. Output bitmap 3D-look/reference bukan mesh/rig; assets 3D perlu pipeline model/rig/animasi berasingan. Built-in dipilih melalui skill imagegen sesi; jangan andaikan nama model atau meminta API key bagi tool built-in.

Spec → katalog provider/model → generation → raw → processing → preview/QC → accepted runtime. Raw dipelihara; fail processed mempunyai hash dan sejarah. Manifest menyimpan ID, penggunaan, image path, source path, frame rect/duration, origin, ukuran, collision reference, provider/model dan status.

Native alpha dipilih jika tool menyokong dan hasilnya bersih. Jika chroma diperlukan, warna background tidak boleh sama dengan warna watak; process edge/despill tanpa merosakkan FX. Jangan menganggap gambar checkerboard mempunyai transparency sebenar.

Grounded sprite berkongsi feet line dan standing-equivalent scale. Fit-to-bbox setiap pose boleh menjadikan watak berubah saiz apabila membongkok; scale profile perlu diuji merentas aksi. Jump/fall memerlukan root motion/offset yang disengajakan. Pixel art perlu resampling yang sesuai; kaedah seperti LANCZOS boleh melembutkan pixel dan mesti diperiksa.

## QC

Bagi 2D pixel farming Godot, [panduan khusus](../integrations/godot-pixel-farming.md) menghubungkan filtering/scaling, feet anchor, arah/action sprite, discrete animation, terrain dan frame tanaman dengan runtime. Sheet cantik perlu diuji pada saiz/kamera sebenar; jumlah frame artwork tidak menentukan aturan matang secara automatik.

Tiada frame kosong tidak sengaja, anggota terpotong, grid salah, pink halo, identiti berubah atau scale/anchor drift yang tidak dijelaskan. Alpha/timing/loop diperiksa dalam preview, bukan satu still sahaja. Ukuran drift ialah toleransi projek, bukan angka universal. Manifest membezakan accepted_by_agent dan approved_by_owner.
