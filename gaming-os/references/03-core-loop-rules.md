# 03 - Core loop, aturan dan state

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Kontrak aturan

Tulis loop sebagai tindakan → cabaran/keputusan → hasil → feedback → tindakan berikutnya. Bezakan loop saat-ke-saat daripada meta loop. Match-3 mempunyai swap/match/resolve dan turn monster; arena mempunyai dodge/auto-attack/pickup dan wave/upgrade/shop. Jangan menggabungkan keduanya tanpa tujuan.

Aturan perlu menentukan trigger, prasyarat, perubahan state, feedback dan reset. Contoh pickup: overlap dengan item aktif → tandakan consumed → tambah skor sekali → keluarkan collider → kemas kini HUD. Damage: overlap bahaya dan cooldown tamat → kurangkan health sekali → invulnerability sementara → feedback. HUD membaca state; ia tidak menyimpan angka gameplay berasingan.

## State machine

Nyatakan loading, title, playing, paused, won, lost dan restarting. Tambah level-complete, upgrade-choice atau shop hanya apabila genre memerlukan. Tulis transition dan siapa memilikinya. Saat pause, simulation/timer/combat berhenti mengikut kontrak; UI tetap boleh digunakan. Restart menghapus entity, projectile, pending timer dan listener sesi lama lalu mencipta state baharu.

Keadaan awal mesti sah: spawn bebas collision, input released, timer tepat, skor sifar dan objective dapat dicapai. Win/fail berlaku sekali walaupun banyak event masuk pada frame sama; tentukan priority jika keduanya berlaku serentak.

## Bukti siap

Sesi boleh dimulakan, dimainkan, dimenangi/digagalkan dan direstart tanpa refresh. Peraturan yang belum dilaksanakan ditandakan planned. Jangan label decorative HUD seperti minimap sebagai fungsi sebenar. Uji collect-once, damage cadence, pause time dan reset data.
