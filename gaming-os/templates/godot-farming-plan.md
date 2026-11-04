# Pelan projek Godot pixel farming

Templat kerja; salin hanya apabila relevan ke folder dokumen game. Belum diisi bukan keputusan projek. Panduan: [Godot pixel farming](../integrations/godot-pixel-farming.md); rekod platform menggunakan [templat keputusan](platform-decision.md). Jika templat disalin ke game, laraskan pautan relatif ke kanon workspace.

## Sasaran

- Game ID / brief / pemilik state:
- Mod dan skop yang diminta (research / plan / build):
- Bentuk visual (2D top-down / pilihan lain yang memerlukan adapter):
- Platform keluaran / peranti / input:
- Godot CANDIDATE atau SELECTED; versi sebenar / renderer / export dan bukti:
- Sasaran animasi/gameplay dan kriteria penerimaan:
- Identiti asal; mekanik inspirasi; aset/lesen/provider:

## Slice dan visual

- Core loop dan hasil tuaian yang benar-benar diterima pemain:
- Kawasan / alat / benih / tanaman / props minimum:
- Sistem yang ditangguh:
- Saiz tile dan unit / feet anchor / arah / sheet/frame timing / collision footprint:
- Base viewport / filtering / scaling / kamera / Y-sort / UI:
- Handoff aset dan ujian satu import/export sebelum production:

## Pemilikan data dan aturan

| Perkara | Keputusan projek |
|---|---|
| CropDefinition dikongsi vs CropState unik | |
| ID jenis/instance dan cell occupancy | |
| Grid/origin/transform; conversion world↔layer↔cell | |
| Farmable/water/fishable/blocked | |
| Action state, impak, satu commit dan cancellation | |
| Pertumbuhan float; threshold matang; mapping frame | |
| Kekeringan berturutan/terkumpul dan reset kaunter | |
| Mature watering/regrow/harvest input | |
| Inventory penuh dan transaksi hasil | |
| Death/harvest/unload: cell, model, panel, trigger, FX | |
| Urutan daily update, lock, day index, cuaca jika ada | |
| Pause/menu/transition/exit/restart | |
| Save diperlukan? schema/ID/migration/polisi gagal | |
| Material unik/shared; tween dan signal cleanup | |
| Editor tools: readiness, random seed, simpan/undo | |

## Bukti dan sambungan

Semua status awal **NOT RUN**; ganti hanya dengan bukti sebenar.

| Semakan | Status | Fail bukti / peranti / dapatan |
|---|---|---|
| Import/animasi/collision/export | NOT RUN | |
| Loop dari mula hingga hasil dan restart | NOT RUN | |
| Koordinat negatif, exact boundary, transformed parent | NOT RUN | |
| Dua tanaman bebas, float growth, matang/kering | NOT RUN | |
| Harvest sekali/beg penuh/death/replant | NOT RUN | |
| Spam/cancel day transition dan pause | NOT RUN | |
| Save round-trip / invalid save jika dalam skop | NOT RUN | |
| HUD/fokus/material/visual/scaling | NOT RUN | |
| Ulangan lifecycle dan profiling beban sasaran | NOT RUN | |
| Human playtest / peranti fizikal | NOT RUN | |

Risiko dan batas bukti:

Langkah seterusnya dalam skop yang diizinkan:
