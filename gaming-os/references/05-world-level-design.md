# 05 - Dunia dan reka level

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Kontrak level

Setiap level mempunyai tujuan latihan/cabaran, spawn, finish, geometry, enemy patterns, pickups, hazard timing, camera bounds dan reset rules. Tulis teach → practice → combine supaya mekanik baharu diperkenal dalam keadaan terkawal. Satu level pendek perlu memberi peluang memahami loop dan mencuba semula.

Mekanik dan art layer ialah dua data berasingan. Platform mestilah permukaan yang boleh dikenal pasti; hiasan tidak berpura-pura solid. Bahaya memberikan telegraph yang mencukupi pada skala peranti sasaran. Coin trail boleh menunjukkan laluan, tetapi tidak boleh mengajak pemain kepada lompatan mustahil tanpa penjelasan.

## Reachability

Ukur jump apex, airtime, jarak mendatar, ladder access dan clearance berdasarkan player contract. Semak spawn → checkpoint/key → gate → exit; jangan cuma memastikan points tidak overlap blocker. Untuk puzzle, semak solution, reset dan pencegahan softlock. Untuk runner/tap-flight, tentukan minimum waktu reaksi dan maksimum perubahan lane/gap antara obstacle.

Tower defense: path mempunyai waypoint, lebar dan border; footprint tower tidak boleh memotong keseluruhan laluan. Validasi turn menggunakan jarak shape/segment, bukan hanya beberapa rectangle kasar. Arena: simpan safe spawn zone dan ring spawn musuh yang tidak muncul atas pemain.

## Output

Level document, object/tile data, camera zones dan debug preview. ASCII tilemap ialah pelan, bukan format engine wajib. Simpan seed/pattern untuk reproduksi procedural bugs. Peta gambar yang cantik tidak membuktikan tahap boleh diselesaikan; buktikan traversal dengan physics sebenar.
