# Log penghasilan aset

- Game / art contract / tarikh:
- Provider/catalog semasa dan parameter disahkan:
- Laluan tool: Codex built-in image_gen / provider lain yang dipilih / CLI/API jika diminta:
- Jenis hasil: concept/reference / bitmap runtime candidate / input pipeline 3D:
- Skop batch / bajet atau had yang ditetapkan:

| Asset ID | Prompt / reference | Model ID | Job ID | Raw path / hash | Processing | Output | QC | Fallback dan sebab |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Status processing/QC direkod berasingan daripada approval pemilik. Simpan prompt dan reference yang digunakan; jangan simpan secrets. Failed/pending job bukan output siap. Retry/fallback ikut skop, tool dan kos sebenar; catat setiap perubahan model. Semak preview sebelum runtime acceptance.

Untuk built-in Codex gunakan [panduan Imagegen](../integrations/codex-imagegen-assets.md). Jika model/job ID tidak dipulangkan, rekod null/tidak dilaporkan, bukan tekaan. Salin output projek ke workspace, rekod path/hash sebenar dan bezakan gambar reference daripada model 3D atau asset runtime yang telah diuji.
