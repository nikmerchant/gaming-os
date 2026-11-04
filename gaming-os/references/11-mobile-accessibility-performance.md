# 11 - Mobile, aksesibiliti dan prestasi

Versi: v0.1. Panduan framework; kesesuaian dan bukti runtime ditentukan setiap projek.

## Kontrak peranti

Tetapkan orientation, logical viewport, scaling/letterbox, CSS size dan backing resolution. Input screen diterjemah kepada world dengan offset/scale yang sama. Resize tidak mengubah simulation geometry secara tidak sengaja. Semak safe area, browser chrome dan canvas pada telefon sebenar.

Touch ialah kawalan utama apabila peranti sasaran mobile. Rancang tap, drag/swipe, joystick atau buttons mengikut genre; tangan tidak boleh menutup bahaya utama. Bezakan tap daripada drag, kendali pointercancel, blur dan multitouch. Jangan mengunci scroll seluruh halaman jika hanya play surface perlu `touch-action` khusus.

## Akses

Controls dan restart boleh dikenal pasti, font dapat dibaca, state menggunakan bentuk/teks bersama warna, pause/mute tersedia dan shake/flashing boleh dikurangkan. Sasaran awal hit area control 44 CSS px boleh digunakan sebagai design target projek, bukan bukti compliance rasmi. Bincang satu tangan/remapping apabila audience memerlukan.

## Bajet prestasi

[Integrasi UI/motion](../integrations/ui-motion.md) memerlukan focus/keyboard/touch, fallback reduced motion dan profiling pada sasaran. Berhentikan clock dekoratif apabila idle/background; hadkan count/lifetime/DPR dan overdraw. Hover bukan satu-satunya maklum balas. Jika menggunakan Lenis/scroll effects bagi web, asingkan play surface/modals/forms dan semak gesture; default native scroll kekal apabila smoothing tidak perlu.

Cadangan awal: target 60 fps pada peranti baseline dan reduced-effects mode sekurang-kurangnya 30 fps; kedua-duanya belum dibuktikan. Rekod model telefon, OS/browser, build, frame-time, load time, memory trend dan senario maksimum entity/FX. Baseline dan loading budget dipilih selepas ukuran pilot, bukan jaminan universal.

Kurangkan overdraw, cache static layers, hadkan DPR/texture mengikut keperluan dan buang objects selesai. Profile sebelum optimization besar. Emulation desktop membantu QA layout; ia tidak menggantikan Safari/Chrome serta prestasi GPU/bateri telefon sebenar.
