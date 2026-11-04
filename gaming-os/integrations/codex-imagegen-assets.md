# Penghasilan aset game melalui Imagegen Codex

Panduan framework v0.1; ketersediaan alat berbeza mengikut sesi dan penyedia. Gunakan Imagegen terbina dalam Codex untuk menghasilkan aset game bitmap apabila sesuai dan alat tersedia. Baca skill `imagegen` yang tersedia dalam sesi sebelum generation/edit sebenar. Higgsfield dan provider lain kekal pilihan mengikut akses, brief serta arahan khusus pemilik.

## Pilih hasil yang betul

| Hasil | Penggunaan Imagegen | Pemeriksaan sebelum runtime |
|---|---|---|
| Concept art watak/dunia/props | Arah visual dan rujukan aset | Identiti, siluet, kamera, palet, skala dan kegunaan jelas |
| Sprite, props dan ilustrasi 2D | Bitmap/cutout dengan alpha apabila perlu | Dimensions, alpha sebenar, anchor, collision berasingan dan readability |
| Latar/panorama/layer peta | Artwork mengikut kamera dan aspect brief | Seam/layer/parallax dan ruang gameplay; gambar tidak menentukan collision |
| Ikon atau panel berilustrasi | Bitmap untuk item/portrait/panel art | Saiz runtime, contrast dan state; teks/skor/harga dinamik kekal UI enjin |
| Tekstur permukaan | Calon texture/albedo mengikut kontrak | Tile/seam, UV, lighting terbakar dan material dalam enjin; bukan PBR lengkap secara automatik |
| Sprite animation | Kandidat pose/frame atau sheet mengikut kontrak | Konsistensi bentuk/skala, grid, timing dan loop; jangan anggap terus production-ready |
| Aset 3D | Reference/turnaround atau imej untuk pipeline model | Imej bukan mesh/GLB/FBX, rig atau klip; proses model/rig/animasi dan import tetap diperlukan |

Untuk vector/icon system sedia ada, bentuk mudah atau sumber native yang boleh diedit, pilih workflow asal apabila lebih sesuai. Imagegen tidak diwajibkan bagi setiap asset atau menggantikan Blender, engine UI dan kod.

## Workflow ART → ASSET

1. Semak brief, platform dan kontrak aset. Rekod ID, tujuan runtime, gaya/palet, kamera, dimensi sasaran, alpha, anchor/frame dan batas bajet/skop. Tentukan sama ada preview, reference atau aset yang akan digunakan game.
2. Pilih built-in Imagegen untuk bitmap yang sesuai apabila provider khusus belum ditetapkan. Ikut pilihan provider/reference sedia ada; jangan menukar aset Higgsfield yang diminta secara khusus atau menjana semula aset completed tanpa sebab.
3. Tulis prompt beserta peranan setiap reference. Nyatakan subject, gaya, framing, lighting, background/alpha dan unsur yang mesti kekal. Pemeriksaan/ejaan teks serta konsistensi watak tidak dianggap terjamin.
4. Gunakan tool built-in sebenar. Untuk cutout, minta background transparent dan parameter transparency apabila disediakan tool; checkerboard yang dilukis bukan alpha. Built-in tidak memerlukan `OPENAI_API_KEY`. CLI/API fallback hanya apabila dipilih pemilik; jangan menukar laluan/provider secara senyap jika built-in gagal atau tiada.
5. Inspect output sebenar. Untuk edit imej tempatan, paparkan/inspect dahulu mengikut skill/tool sesi. Kekalkan asal dan hasilkan versi baharu apabila replacement tidak diminta. Banyak aset berlainan memerlukan prompt/call berasingan; jangan serahkan collage sebagai fail runtime yang sudah dipisahkan.
6. Simpan raw dan kandidat projek dalam folder permainan, contohnya `assets/raw/codex-imagegen/` dan `assets/candidates/`. Salin output sebenar dari lokasi yang dipulangkan alat ke workspace; jangan biarkan game bergantung pada folder generation peribadi Codex. Jangan reka nama/path fail sebelum output wujud.
7. Lengkapkan [generation log](../templates/generation-log.md) dan [manifest](../templates/asset-manifest.example.json): provider/tool, prompt/reference, output path/hash, dimensi, processing dan QC. Jika tool tidak memulangkan model/job ID, kekalkan null dan jelaskan tidak dilaporkan; jangan menyamakannya dengan model Higgsfield bernama serupa.
8. Semak raw → processed/candidate → runtime sebagai status berasingan. Uji import, alpha/material, frame/anchor, visual serta performance pada platform sebenar sebelum runtime acceptance. `accepted_by_agent` berbeza daripada `approved_by_owner`.

Untuk 3D tanpa sambungan Higgsfield, imej rujukan masih boleh digunakan dalam pemodelan/rigging Blender biasa atau pipeline lain yang dipilih. Jika provider/model 3D tambahan memerlukan akses/kos, ikut skop sebenar; pilihan Imagegen tidak memberi akses kepada provider lain atau meluaskan bajet yang dipersetujui.

## Bukti dan batas

Nyatakan aset sebenar, prompt dan kaedah generation serta path projek. Jika hanya pelan/panduan diminta, hasil ialah spesifikasi dan status NOT RUN. Jika tool tidak tersedia, simpan spesifikasi/limitation dan teruskan kerja bebas yang boleh dibuat. Jangan dakwa generation, rig, animasi, approval, import atau ujian runtime hanya kerana prompt atau gambar konsep tersedia.
