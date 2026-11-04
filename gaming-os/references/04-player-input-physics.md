# 04 - Player, input dan physics

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Action map

Input fizikal diterjemah kepada tindakan: move, jump/flap, attack, interact, pause dan restart. Keyboard, pointer dan touch berkongsi action tersebut. Bezakan pressed, held dan released supaya jump tidak berulang kerana key repeat. Simpan pointer ID setiap touch; clear input pada pointercancel/blur. Satu jari bergerak dan jari lain menyerang perlu dapat berfungsi serentak apabila genre memerlukannya.

## Kontrak gerakan

Rekod unit world px, saat, kelajuan px/s, acceleration px/s², gravity, impulse, drag dan had kelajuan. Gunakan masa simulation, bukan bilangan frame. Kaedah timestep serta clamp/catch-up perlu jelas supaya resume tab tidak melompat jauh. Pada fixed timestep, rekod dt dan had langkah setiap render.

Platformer: simpan previous position, grounded, horizontal/vertical velocity; resolve collision mengikut arah pergerakan. One-way platform perlu syarat datang dari atas, bukan sekadar overlap. Coyote time/jump buffer ialah pilihan rasa, bukan wajib. Bagi gravity malar, tinggi lompatan anggaran `h = v²/(2g)`; lompatan 1.5x tinggi memerlukan impulse `sqrt(1.5)` kali, bukan 1.5 kali. Semak semula dengan collision dan airtime sebenar.

Tap-flight: flap impulse dan gravity konsisten; difficulty mengubah obstacle/world, bukan input secara mengejut. Top-down: normalize diagonal jika kelajuan seragam diminta.

## Semakan

Uji input desktop/touch, release, simultaneous buttons, 30/60/120 Hz, ceiling/side/landing, high-speed tunnel, pause/resume dan orientation. Hitbox collision berasingan daripada transparent canvas sprite; FX tidak membesarkan hitbox.
