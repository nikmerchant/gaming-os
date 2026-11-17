# Kad serah build

Salin ke folder permainan selepas setiap build yang diserahkan kepada pemilik. Diadaptasi daripada Claude Code Game Studios 1.3.0 (MIT); lihat [integrasi genre](../integrations/genre-chipsets.md). Isi daripada bukti sebenar; buang baris kosong kecuali baris terakhir.

```text
Build / versi / tarikh:
Cara main: <kawalan>
Buka: <fail, arahan atau peranti>
Semakan kecil: lulus <baris> · gagal <baris> · tidak dinilai <baris> (sebab)
Senarai semak brief: <lulus> daripada <item>
  gagal <id> <item>: missing | broken
  tidak dinilai <id> <item>: <sebab>
Dibaiki: <setiap pembaikan daripada semakan>
Game terdekat: <nama>; berbeza pada <apa>
Tidak seperti dikata: <kata brief yang terlepas>: <sebab>
Masih rosak: <apa>
Belum dibuat: <dijanji tetapi tiada>
Rujukan digunakan: <fail> untuk <apa>
Diteka: <keputusan build yang tiada dalam brief>
Seterusnya: <satu langkah>
Belum dimainkan oleh manusia.
```

Baris terakhir kekal sehingga pemilik atau pemain benar-benar bermain; tiada ujian agent menggantikannya.

## Semakan kecil

Ujian asap, bukan penilaian keseronokan atau kesukaran. Pilih alat mengikut enjin projek.

| Baris | Lulus apabila |
|---|---|
| boots | Build dibuka tanpa crash, ralat konsol/log atau skrin kosong |
| shot | Tangkapan skrin semasa bermain disimpan dan benar-benar dilihat terhadap brief |
| responds | Input kawalan game sendiri mengubah keadaan permainan |
| teks | Teks dalam tetingkap, boleh dibaca dan tidak bertindih |
| alir | Tiada skrin beku, skrin tamat yang memerangkap pemain atau kegagalan tanpa pemulihan |

Satu pusingan pembaikan, kemudian semak sekali lagi. Yang masih gagal ditulis pada “Masih rosak”. Baris yang tidak dapat dijalankan ialah *tidak dinilai* bersama sebab, bukan lulus. Jangan ubah game semata-mata supaya semakan boleh berjalan, dan jangan tala kesukaran melalui skrip.

## Senarai semak brief

Setiap ciri bernombor, ayat minit pertama, ayat cabaran dan baris rupa dalam brief ialah satu item (C1, M1, K1, R1…).

| ID | Item | Status | Bukti | Catatan |
|---|---|---|---|---|
| | | pass / missing / broken / not_assessed | tangkapan skrin atau `fail:baris` | |

`pass` bermaksud “ada dan berfungsi seperti ditulis”, bukan “terasa betul”. Item yang tidak dapat ditunjukkan oleh tangkapan atau kod (bunyi, rasa) ialah `not_assessed` bersama sebab.

## Verdict selepas dimainkan

PROCEED, PIVOT atau KILL oleh pemilik; NOT ASSESSED jika belum dimainkan. Tiga PIVOT pada konsep yang sama memerlukan soalan terus: adakah idea ini betul, atau kos tenggelam?
