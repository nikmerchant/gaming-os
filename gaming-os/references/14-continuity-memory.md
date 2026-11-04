# 14 - Continuity dan memori pembangunan

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Dua tahap state

OS state menyimpan modul, sumber, versi, tooling dan pilihan rentas projek. Game state menyimpan game ID, brief/version, enjin/toolchain, art/asset manifest, rules/balance, level data, build/checkpoint, hasil ujian, isu dan langkah seterusnya. Save-game pemain ialah sistem runtime berbeza dan hanya dibina jika diperlukan.

`MEMORY.md` ialah fakta/pilihan tahan lama. `PROJECT-STATE.md` ialah keadaan terkini. `DECISION-LOG.md` ialah sebab perubahan. `WORKLOG.md` ialah hasil sesi. Manifest mempunyai file/version/hash dan status. Elakkan menduakan naratif panjang di semua fail.

## Checkpoint

Rekod tarikh/zon waktu, mode, tujuan, changes, files, evidence, known issues dan next action yang boleh terus dilakukan. Nyatakan status planned/generated/processed/accepted/implemented/verified secara tepat. `owner_approved` mesti disertai arahan sebenar/tarikh, bukan tekaan daripada silence.

Sebelum sambung, baca state dan semak fail berkaitan. Jika hash/version berbeza, baca perubahan dan kemas kini state. Jangan regenerate aset atau rewrite game yang sudah selesai tanpa sebab. Simpan raw assets dan migration note apabila schema/toolchain berubah.

## Tamat milestone

Kemas kini state dan issue log; simpan decision material; buat ringkasan checkpoint. Jangan letak secrets dalam memori. Pautan sumber panjang boleh dirujuk melalui source ID. Hasil yang belum diuji kekal NOT RUN, dan next step tidak disamarkan sebagai kerja selesai.
