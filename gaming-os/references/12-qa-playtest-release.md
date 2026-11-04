# 12 - QA, playtest dan release

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Lapisan bukti

Structural checks memeriksa path/schema/bounds. Unit/system tests memeriksa peraturan. Browser smoke test memeriksa flow dan errors. Visual review memeriksa alpha/alignment/readability. Human playtest memeriksa kefahaman, rasa, fairness dan keseronokan. Catat tiap lapisan sebagai PASS/FAIL/NOT RUN beserta bukti sebenar.

QA minimum: load/title/start, actions, collision, pickup once, damage cooldown, timer/pause, objective, win/fail dan restart. Uji repeat restart, tab background, resize, input release dan missing assets. Pilih tambahan genre: beam loop/softlock, match-3 dead board/cascades, shop locks/price, tower footprint sepanjang route, procedural pattern fairness.

## Isu dan pembaikan

Issue report merekod build, device, expected/actual, langkah repro, evidence dan severity. Prioriti: blocker → input/collision → rules/state → clarity/balance → visual polish. Fix hanya sistem perlu; ulang ujian relevan dan sesi ringkas lengkap. Jangan rewrite semua projek untuk satu corner bug.

Playtest report menyatakan siapa/berapa orang, task, observation dan limitation. Jika agent sendiri menguji, tulis agent playthrough. Jangan reka feedback pemain atau metrik.

## Release gate

Untuk UI/motion gunakan [kontrak](../templates/ui-motion-contract.md) serta [panduan integrasi](../integrations/ui-motion.md). Uji interrupt/back/pause, focus dan touch, repeated open/close/reset, nilai julat sifar/out-of-range, reduced motion dan worst-case effects. Semak notis sumber/dependency yang benar-benar dihantar; snapshot sumber pihak ketiga dikecualikan daripada bundle awam secara default. Snapshot/hash checks tidak membuktikan keserasian React, prestasi atau runtime game.

Deliver build, command/URL, controls, assets/credits, known issues dan platform matrix. Case-sensitive paths dan subpath deployment diperiksa. Tapis bahan sumber dan ekstrak persendirian daripada output awam. Production label memerlukan evidence untuk sasaran yang dinyatakan; package validator sahaja tidak cukup. Deployment dilakukan apabila skop pemilik meliputinya.
