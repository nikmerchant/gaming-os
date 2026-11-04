# 10 - Progression dan balance

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Data tuning

Simpan parameter dalam content/balance data: speed, gap, spawn interval, enemy stats, attack range/cooldown, reward, prices dan wave table. Bezakan base stat, modifier dan derived stat; recalculate bila inventory berubah. Damage satu attack tidak berlaku setiap render frame kecuali aturan beam/DOT menyatakan cadence.

Difficulty menguji kemahiran yang telah diperkenalkan. Tambah tekanan secara bertahap; jangan menukar kekuatan flap/jump tanpa penjelasan. Tap-flight mempunyai gap/spacing/vertical transition limits; runner mempunyai pattern selamat; wave mempunyai komposisi dan telegraph. Nilai tier sumber ialah contoh, bukan tuning yang terbukti.

## Genre

Arena roguelite: senjata, upgrade dan kedai perlu state terpisah. Wave-end membersihkan entity mengikut kontrak dan menyelesaikan pending level-up sebelum shop. Tower defense: valid placement, range, targeting paling hampir core, refund dan ekonomi didefinisikan. Match-3: valid/invalid swap, cascade order, enemy turn dan no-move reshuffle ditentukan sebelum animation.

## Balance evidence

Ukur masa sesi, punca mati, perubahan build, completion dan kefahaman objective. Gunakan seed untuk replay apabila ada random. Bezakan balance angka daripada game feel. Menambah health atau particle tidak menyelesaikan feedback yang mengelirukan.

Target awal ialah cadangan untuk diuji: pemain memahami tindakan pertama, kegagalan ada sebab yang dapat dibaca, strategi/kemahiran mempengaruhi hasil dan restart tidak melecehkan. Rekod data atau observation sebenar; jangan menyatakan retention, engagement atau kadar kemenangan yang tidak pernah diukur.
