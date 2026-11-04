# 09 - Feedback, audio dan VFX

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Event feedback

Setiap kesan menjawab tindakan atau perubahan state: jump/landing, collect, hit, damage, upgrade, wave/level complete dan fail/win. Pilih timing, duration, intensity, layer dan reduced-motion alternative. Kesan yang mengaburkan obstacle atau attack telegraph gagal walaupun nampak mewah.

Pisahkan hero animation, weapon/projectile dan impact. Spray cone, electric chain dan melee arc perlu memberi maklumat bentuk serangan masing-masing; jangan menggunakan bola generik bagi semua weapon. Damage flash, health pulse dan hit sound menyampaikan satu event, bukan damage tambahan.

## UI dan audio

Gunakan [integrasi UI/motion](../integrations/ui-motion.md) dan [kontrak](../templates/ui-motion-contract.md) untuk button/focus, progress, counter, panel dan celebration. Magic UI/GSAP/shadcn/Mantine ialah pilihan output web; untuk enjin asli terjemah prinsip kepada API enjin sendiri. Nilai/reward committed berasingan daripada nilai paparan animasi; jangan memberi ganjaran melalui completion callback kedua. Tentukan interruption dan reduced-motion feedback sebelum menambah efek.

Gunakan teks/nombor dinamik dalam DOM/engine UI. Imej AI boleh memberi icon/panel texture; jangan rasterize skor, harga atau instruction yang berubah. Tunjukkan controls, objective, pause/restart dan state dengan hierarchy yang jelas. Health dan enemy identity tidak bergantung kepada warna sahaja.

Audio asal boleh disintesis ringan atau dijana melalui tool yang tersedia. Simpan sumber dan credit; tiada soundtrack/SFX francais disalin. Browser audio dimulakan melalui gesture dan mempunyai mute/volume. Bunyi tidak menjadi satu-satunya petunjuk penting.

## Polish order dan bukti

Perbaiki respons input, collision, damage/reward clarity dan camera dahulu. Kemudian tambah animation/FX/audio secara terukur. Tetapkan max effect lifetime/count serta intensity; cuba telefon dengan effect-heavy scene. UI preview dalam art document belum membuktikan text legibility semasa bermain. Simpan before/after apabila menilai shake, trails atau particles.
