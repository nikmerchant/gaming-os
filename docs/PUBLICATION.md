# Memisahkan framework awam dan kerja persendirian

Gunakan repo ini untuk modul, workflow, integrasi panduan, templat kosong dan helper. Simpan pembangunan game dalam folder/repo berasingan. Untuk nota tempatan, helper boleh mencipta `workspace/`, yang diabaikan Git.

## Sebelum menerbitkan

1. Mulakan daripada salinan framework yang bersih, bukan root folder kerja yang mengandungi game dan memori.
2. Semak semua fail dan sejarah commit. Jangan menyalin `.git` daripada workspace persendirian.
3. Pastikan hanya fail yang disengajakan ada dalam `PUBLIC-FILES.json`; jalankan validator dan ujian.
4. Jika menggunakan Git, semak `git ls-files`, `git status` dan diff sebelum push. `.gitignore` tidak mengeluarkan fail yang sudah dijejak.
5. Semak kredensial, path komputer, nama/kandungan projek persendirian, save pemain, aset, log, build dan hak penggunaan. Corak automatik hanya bantuan, bukan jaminan lengkap.
6. Muat naik hanya pokok fail awam yang disemak. Jangan menggunakan wildcard upload pada keseluruhan workspace persendirian.

Fail yang sudah diterbitkan boleh kekal dalam sejarah Git, cache atau salinan orang lain walaupun dipadam kemudian. Jika kredensial terdedah, batalkan/ganti kredensial dan urus sejarah yang berkaitan; jangan menganggap penghapusan fail terkini sudah memulihkan kerahsiaan.

## Pemeriksaan framework

Validator mengesahkan allowlist, hash, pautan tempatan, contoh kontrak dan beberapa corak sensitif. `.git` dikecualikan daripada pemeriksaan fail working tree supaya checkout boleh digunakan. Sejarah Git tetap perlu diperiksa secara berasingan apabila ada sejarah sebelum ini.

Refresh manifest hanya selepas semakan. Ia tidak memberi izin menerbitkan fail pengguna dan tidak menghalalkan bahan pihak ketiga. Permintaan membina atau menyimpan game tidak dengan sendirinya memberi izin menerbitkan game tersebut.
