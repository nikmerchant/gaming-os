# 07 - Kontrak peta runtime

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Pilihan map

Pilih mode: tile, scene, side-scroll, grid, room-chunk atau baked-scene. Selepas itu tentukan visual model, object model, collision model dan engine target. Baked background sesuai untuk plate statik; map interaktif perlu data runtime berasingan.

Layer lazim: ground-only base; props; actors; foreground; collision; zones. Dressed reference menunjukkan sasaran visual. Runtime preview disusun daripada base dan props sebenar supaya elemen tidak berganda. Actors, collectibles, gate dan hazard aktif tidak dibakar ke background.

Compact props boleh dibatch 2x2/3x3/4x4. Platform, jambatan, wall, gate lebar dan objek yang perlu align tepat menggunakan strip/tiles/object tersendiri. Jika prop terpotong pada cell, ubah strategi penghasilan, bukan melonggarkan QC untuk menutup masalah.

## Geometri

Koordinat world mempunyai origin, width/height dan unit jelas. Props menyimpan position, anchor dan layer; collision menyimpan shape berasingan; zones menyimpan trigger/exit/spawn. Visual bbox bukan footprint automatik. Y-sort menggunakan ground anchor; foreground occluder perlu memastikan badan/cue pemain masih boleh dibaca.

Side-scroll menyimpan camera, segment extent, parallax scroll factors, platform IDs, hazard/door/checkpoint dan bounds. Jangan menganggap background image ialah collision source. Tile exports mesti mengikuti format engine/Tiled/LDtk terpilih; contoh JSON Gaming OS memerlukan adapter, bukan terus drop-in ke semua editor.

## Pemeriksaan

Untuk peta ladang Godot, baca bahagian grid/terrain dalam [panduan Godot pixel farming](../integrations/godot-pixel-farming.md). Bezakan cell logik, tanah/siraman, occupancy dan lapisan visual; uji koordinat negatif, sempadan dan transform. Ketiadaan ground tile bukan bukti petak itu air/fishable.

Path aset sah, shape dalam bounds, spawn/exit bebas blocker, tiada duplicate runtime object, dan laluan boleh dimainkan. Debug overlay menunjukkan collision, trigger, anchor dan camera. Perubahan artwork yang mengubah geometry mesti menyemak contract dan traversal semula.
