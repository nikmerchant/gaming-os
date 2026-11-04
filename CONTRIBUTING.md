# Menyumbang kepada Gaming OS

Sumbangan boleh memperbaiki workflow, templat, kejelasan panduan, adapter enjin atau pengesahan. Buka issue untuk masalah yang dapat diterangkan, atau pull request untuk perubahan fokus dengan sebab dan bukti yang sesuai.

- Kekalkan satu kanon dalam `gaming-os/`; wrapper alat hanya menunjuk kepadanya.
- Terangkan trigger, hasil yang diingini dan batas. Elakkan menjadikan pilihan satu projek sebagai aturan semua game.
- Gunakan sumber primer bagi fakta API/alat yang berubah. Catat versi/peranti apabila menjalankan ujian sebenar.
- Jangan sertakan game persendirian, rancangan cerita, memori sesi, screenshot pengguna, token, transkrip atau bahan kursus berbayar. Contoh baharu mestilah generik dan mempunyai hak penggunaan yang sesuai.
- Pisahkan bukti struktur, runtime, visual dan human playtest. Fail panduan tidak membuktikan integrasi berfungsi dalam semua enjin.

Jalankan:

```sh
python tools/validate_public.py
python -m unittest discover -s tests
```

Selepas menyemak kandungan perubahan, kemas kini hash fail yang sudah disenaraikan:

```sh
python tools/validate_public.py --refresh
```

Untuk fail framework baharu, tambahkan path relatif yang tepat dalam `PUBLIC-FILES.json` dahulu, kemudian refresh dan semak diff. Jangan menukar senarai fail menjadi semua isi folder; senarai eksplisit membantu menjaga sempadan penerbitan. Fail di luar senarai akan menyebabkan validasi gagal.

Dengan menyumbang, pastikan anda mempunyai hak untuk memberikan sumbangan di bawah lesen MIT repo ini. Lesen pihak ketiga, termasuk media, tidak digantikan oleh MIT framework.
