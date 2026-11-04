# Pelan dan keputusan QA

- Game / build / tarikh:
- Enjin / peranti / OS / browser:
- Command / URL / seed / test mode:
- Pelaksana dan jenis bukti:

## Matriks

| ID | Senario | Expected | Automatic/manual/human | Hasil PASS/FAIL/NOT RUN | Bukti |
|---|---|---|---|---|---|
| Q01 | Load → title → start | Aset dimuat, objective dan controls jelas | | NOT RUN | |
| Q02 | Input pressed/held/released | Action tidak double/stuck | | NOT RUN | |
| Q03 | Collision sisi/atas/bawah | Tiada snap/tunnel/softlock | | NOT RUN | |
| Q04 | Pickup sama berulang | Reward diberi sekali | | NOT RUN | |
| Q05 | Damage berterusan | Cadence dan cooldown ikut rules | | NOT RUN | |
| Q06 | Pause/background/resume | Tiada simulation jump/timer salah | | NOT RUN | |
| Q07 | Win dan fail | Transition jelas dan berlaku sekali | | NOT RUN | |
| Q08 | Restart tiga kali | Semua sesi reset, listener tidak duplicate | | NOT RUN | |
| Q09 | Touch serentak/resize | Kawalan, pointer mapping dan UI kekal sah | | NOT RUN | |
| Q10 | Worst-case entities/FX | Budget diukur pada peranti sasaran | | NOT RUN | |
| Q11 | Runtime asset review | Alpha, anchor, timing dan readability sah | | NOT RUN | |
| Q12 | Release path/README | Build boleh dijalankan dengan arahan | | NOT RUN | |

Tambah kes genre: tower route footprint; beam loop; match-3 no moves; shop duplicate/lock; procedural fairness. NOT APPLICABLE mesti mempunyai sebab. Unit tests yang lulus bukan bukti human playtest.

## Keputusan milestone

Blockers; isu kecil; apa yang benar-benar lulus; limitation; tahap release yang boleh didakwa; next action.
