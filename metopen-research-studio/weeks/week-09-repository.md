# Week 09 — Repository

> **Sprint** S9 · **Gate** G6 Experiment Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-08-design-defense.md) / [Week berikutnya →](week-10-pilot.md)

## This Week

Pada akhir minggu ini repositori riset Anda berubah dari kumpulan dokumen menjadi **reproducibility package**: environment terkunci versi, seed dan konfigurasi terpusat, pipeline data dengan split anti-leakage, baseline dan metode yang membaca metrik terkunci G5, serta **satu perintah** (`run.sh`/Makefile) yang menjalankan semuanya dan menulis log + hasil ke `results/` — sementara data mentah tetap di luar GitHub ([OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S9; [MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W9). Ini minggu pembuka G6 (W9 Repository → W10 Pilot): pilot end-to-end, reproduksi peer, dan PR `GATE REVIEW: Experiment Ready` menyusul di W10. Kalimat G6 dari [OPS-03](../../research-os/06-execution-os/03-research-gates.md) — **"Pilot kami berjalan; orang lain sudah mereproduksinya."** — baru bisa diucapkan minggu depan; minggu ini tugasnya membuat kalimat itu *mungkin*.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (reproducibility package, data governance, struktur `experiments/` dan logging, git hygiene), **60 menit studio** (latihan mereproduksi notebook contoh dari environment bersih dan mencatat kegagalannya, lalu tim memulai OPS-079 environment + seed di repo sendiri), **10 menit gate check** (tiap tim menunjukkan `.gitignore`, `requirements.txt`/`environment.yml`, dan `config.yaml` dengan seed; dosen menguji apakah metrik di config identik dengan yang dikunci di `docs/research-design.md`). Ini sprint terberat semester (24 jam tim, kerapuhan tinggi) — mulai OPS-079/080 di hari pertama, bukan setelah sesi berikutnya ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md).

## Concept (30 menit)

1. **Repositori riset adalah artefak yang dapat diperiksa, bukan tempat menyimpan kode.** Research Pack hidup di repositori dan dirilis sebagai `v1.0` ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §1); README-nya adalah README riset, bukan README software ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)). Orang yang datang tiga tahun kemudian harus mengerti masalah, klaim, status, dan cara menjalankan.
2. **Reproducibility package minimum** = kode + konfigurasi + seed + environment + langkah eksekusi + data/metadata data ([MST-03](../../research-os/00-master/03-glossary.md) §2). Hilang satu, orang lain tidak bisa menjalankan ulang. Metopen menargetkan minimum ini; artifact badging formal ala ACM adalah norma komunitas yang dituju, bukan syarat semester ([MET-01](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §7.2).
3. **Environment dipin, seed dicatat, config terpusat.** `requirements.txt`/`environment.yml` dengan versi terkunci; `set_seed()` dipanggil di satu tempat; seed, split, dan hyperparameter hidup di `experiments/pilot-01/config.yaml`, bukan di badan kode. "Berjalan di laptop saya" bukan reproducibility ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.7).
4. **Data governance: GitHub menyimpan metadata, bukan data.** Data mentah sensitif tidak pernah masuk git ([SECURITY.md](../../SECURITY.md) §3); `data/README.md` memuat Dataset ID, sumber, skema, split, dan daftar apa yang *tidak* ada di repo; `.gitignore` mengecualikan `data/raw/`, kredensial, `.env`. Lisensi per komponen (kode Apache-2.0, dokumen CC BY 4.0, dataset sesuai kartu) mengikuti [LICENSING.md](../../LICENSING.md).
5. **Leakage dicegah di kode, bukan di niat.** Urutan wajib: *split dulu dengan seed, lalu pra-pemrosesan hanya pada train*; tidak ada duplikat lintas split; tidak ada fitur yang membocorkan target; tuning hanya di validation. Tes sederhana "tidak ada overlap train/test" adalah bagian dari `src/data.py`, bukan pemeriksaan manual ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.9).
6. **Metrik dan baseline sudah terkunci; kode hanya mengimplementasikannya.** `src/evaluate.py` membaca metrik yang ditetapkan di G5 (`docs/research-design.md` §Metrics & Evaluation); bila implementasi memaksa perubahan, catat alasan dan tanggal, jangan diam-diam ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint; blocking rule B5 di [OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md)).
7. **Struktur `experiments/` dan logging.** Satu folder per eksperimen (`experiments/pilot-01/`: experiment card dari W8, `config.yaml`, `logs/`); hasil ke `results/pilot-01/` sebagai JSON/CSV bermeta *timestamp, seed, git hash*; figur ke `figures/`. Hasil yang tidak menyebut commit asalnya tidak bisa ditelusuri ([TPL-09](../../research-os/08-templates/09-experiment-card.md)).
8. **Notebook untuk eksplorasi, `src/` untuk kebenaran.** Notebook dijalankan "Restart & run all" sebelum commit, output dibersihkan dari data pribadi, dan logika inti dipindah ke modul yang bisa diuji ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.8).
9. **Git hygiene sebagai jejak ilmiah.** Commit kecil dengan pesan bermakna yang menyebut Task ID; kerja di branch `research/g6-experiment`; PR internal `exp/pilot-01` direview anggota lain sebelum merge ([TPL-15](../../research-os/08-templates/15-research-repository-template.md) §Konvensi; [CONTRIBUTING.md](../../CONTRIBUTING.md) §5).
10. **Kode berbantuan AI adalah kode Anda.** Coding support adalah penggunaan AI paling matang, tetapi kode AI yang *berjalan* belum tentu *benar* — leakage sering datang dari kode "yang berhasil". Semua kode AI dibaca, diuji, diberi sanity check, dan dicatat per modul di AI Usage Log ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.8).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi: *"Kalau laptop saya hilang malam ini, bisakah anggota tim lain meng-clone repositori, menginstal environment, dan menghasilkan angka baseline yang sama dengan satu perintah — tanpa bertanya kepada saya, dan tanpa menemukan satu pun baris data mentah di riwayat git?"*

## Tasks

Semua task Sprint S9 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add data pipeline with leakage test (OPS-080)`. Task W8 yang belum selesai — terutama OPS-076 PR `GATE REVIEW: Method Ready` dan OPS-071 Experiment Card — ditulis di atas tabel ini pada salinan tim: OPS-079 membutuhkan experiment card, dan pilot W10 (OPS-088) tidak boleh dijalankan sebelum PR G5 termerge (blocking rule B5).

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-078 | Ikuti sesi Data, Experiments & Reproducibility | Catatan reproduksi latihan | 2h | Membantu mendiagnosis error environment | Mahasiswa menjalankan sendiri di environment bersih |
| OPS-079 | Siapkan environment dan seed (requirements/environment, config) | File environment + config | 2h | Membantu menulis boilerplate config dan set_seed; diuji tim | Tim menguji instalasi dari nol berhasil |
| OPS-080 | Bangun pipeline data: loading, cleaning, split anti-leakage | src/data.py + data/README.md | 4h | Membantu menulis kode dan tes; hasil tes dijalankan tim | Tim memverifikasi tidak ada overlap train/test dan tidak ada data pribadi di repo |
| OPS-081 | Implementasikan baseline dan evaluasi metrik terkunci | Kode baseline + hasil awal | 4h | Membantu menulis kode dan debugging; angka dijalankan dan diperiksa tim | Tim memeriksa metrik di kode identik dengan metrik terkunci |
| OPS-082 | Implementasikan metode utama / artefak yang diuji | src/method.py | 6h | Membantu implementasi dan debugging sesuai AI Research Protocol; setiap potongan dicatat di AI Usage Log | Tim membaca dan memahami setiap fungsi yang dibantu AI |
| OPS-083 | Buat skrip run.sh/Makefile dan logging eksperimen | run.sh/Makefile + logging | 2h | Membantu menulis skrip; diuji tim | Tim memastikan hasil memuat git hash dan seed |
| OPS-084 | Tulis experiments/README.md (reproducibility README v0) | experiments/README.md v0 | 1.5h | Merapikan format README | Anggota lain mengikuti README tanpa bertanya |
| OPS-085 | Perbarui AI Usage Log untuk kode yang dibantu AI dan jurnal W9 | AI Usage Log W9 + jurnal | 1h | - | Setiap anggota memverifikasi entri log miliknya |
| OPS-086 | Lakukan code review internal dan checklist kualitas kode | PR internal termerge | 1.5h | Membantu menjelaskan potongan kode saat review | Reviewer manusia menyetujui PR |

**Total effort: 24h** (jam tim; untuk tim 2 orang bagi dua; mahasiswa yang bekerja sendiri perlu memakai akhir pekan). Ini sprint dengan jam terbesar dan kerapuhan tinggi: 17 jam berada pada critical path, slack hanya 7 jam ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer) — tidak ada buffer lagi setelah S8.

**Urutan yang disarankan** (dari kolom Dependency): Senin **OPS-078** di sesi studio lalu langsung **OPS-079** (butuh experiment card OPS-071 dari W8) → **OPS-080** pipeline data; setelah itu pecah ke dua anggota berbeda: **OPS-081** baseline + evaluasi (butuh baseline OPS-064 dan metrik terkunci OPS-065 dari W7) *paralel* dengan **OPS-082** metode utama; keduanya bertemu di **OPS-083** run.sh + logging → **OPS-084** README v0 → **OPS-086** code review internal; **OPS-085** berjalan sepanjang minggu setiap kali ada kode berbantuan AI dan ditutup Jumat bersama jurnal.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g6-experiment` (dibuat dari `main` setelah PR G5 merge; PR G6 sendiri dibuka di W10), harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Catatan reproduksi latihan: notebook contoh dijalankan dari environment bersih, kegagalan yang ditemui dan penyebabnya + jurnal W9 | `docs/journal/w09.md` | commit | OPS-078, OPS-085 |
| **Environment terkunci versi** + **config pilot** dengan seed, split, hyperparameter + fungsi `set_seed` | `requirements.txt` atau `environment.yml` (root); `experiments/pilot-01/config.yaml`; `src/utils.py` (atau modul setara) | commit; seed tercantum di config; instalasi dari nol berhasil | OPS-079 |
| **Pipeline data**: load → clean → split dengan seed; tes "tidak ada overlap train/test"; `data/README.md` berisi Dataset ID (`DS-YYYY-NNN` dari W7), sumber, akses, privasi, skema, split, sampel sintetis ≤100 baris, dan daftar yang *tidak* ada di repo | `src/data.py`; `data/README.md`; `.gitignore` (`data/raw/`, `*.key`, `.env`) | commit; tes anti-leakage lulus; tidak ada data mentah di riwayat git ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.8) | OPS-080 |
| **Baseline** (trivial + literatur, sesuai `docs/research-design.md` §Baseline) dan **fungsi evaluasi** yang membaca metrik terkunci G5; hasil baseline awal pada subset | `src/baseline.py`; `src/evaluate.py`; `results/pilot-01/baseline.json` (seed, tanggal, git hash) | commit; angka baseline ada di `results/`, bukan di chat/notebook | OPS-081 |
| **Metode utama / artefak yang diuji**, berjalan dari config dan seed, lulus smoke test pada sampel kecil | `src/method.py` (atau modul artefak) | commit; smoke test tercatat di log | OPS-082 |
| **Satu perintah** menjalankan pipeline penuh; log per run; hasil JSON/CSV dengan timestamp, seed, git hash | `run.sh` atau `Makefile` (root); `experiments/pilot-01/logs/`; `results/pilot-01/` | commit; menjalankan perintah menghasilkan `results/` dan `logs/` | OPS-083 |
| **Reproducibility README v0**: langkah 1-2-3 instalasi, cara mendapatkan data (atau metadata bila restricted), perintah run, output yang diharapkan, waktu berjalan, keterbatasan; tabel eksperimen (`EXP-01` pilot → RQ, status, config, kartu) | `experiments/README.md`; bagian *Reproducibility* di `README.md` riset | commit; anggota lain mengikuti tanpa bertanya ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.14) | OPS-084 |
| AI Usage Log W9: entri Stage `Coding` per modul — tujuan, bagian yang dipakai utuh vs diadaptasi, cara verifikasi (tes/pembacaan), file + commit | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit; entri merujuk file/commit | OPS-085 |
| **PR internal** `exp/pilot-01` → `research/g6-experiment` dengan checklist kualitas kode (keterbacaan, seed, tanpa hardcode path, tanpa data pribadi, tes lulus) dan komentar reviewer | PR di repositori riset | URL PR internal termerge dengan komentar review | OPS-086 |

README riset diperbarui: `Current Research Gate: G5 passed → G6 (in progress — W9 Repository)`. Tata letak `experiments/pilot-01/` (experiment card, `config.yaml`, `logs/`) dan `results/pilot-01/` mengikuti pohon kanonik TPL-15; eksperimen utama W11 memakai `experiments/main/` dan `results/main/`. Belum ada hasil pilot penuh, figur, atau catatan reproduksi peer minggu ini — semuanya W10.

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan** dengan Stage `Coding`. Minggu ini AI paling berguna sebagai **pair programmer dan diagnostik error**; reviewer G6 membaca log untuk satu hal utama: apakah setiap modul berbantuan AI dibaca, diuji, dan dapat dijelaskan anggota yang meng-commit-nya ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.8; contoh baris #7 di TPL-10 adalah polanya).

**Boleh minggu ini**

- Meminta AI mendiagnosis error environment dan konflik versi saat latihan reproduksi dan saat instalasi dari nol (OPS-078, OPS-079); tim yang menjalankan ulang di environment bersih.
- Meminta AI menulis boilerplate `config.yaml`, fungsi `set_seed`, dan kerangka `run.sh`/Makefile (OPS-079, OPS-083); semuanya diuji tim sebelum commit.
- Meminta AI membantu menulis `src/data.py` beserta tes anti-leakage (OPS-080) — dengan **skema dan sampel sintetis**, bukan data asli; tes dijalankan tim dan hasilnya dicatat.
- Meminta AI membantu menulis dan men-debug `src/baseline.py`, `src/evaluate.py`, dan `src/method.py` (OPS-081, OPS-082); angka dijalankan dan diperiksa tim; setiap potongan dicatat di log dengan tanda "utuh" atau "diadaptasi".
- Meminta AI menulis unit test/sanity check tambahan (proporsi split, ID unik, tidak ada fitur target) — kategori yang [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 sebut "penulisan tes".
- Meminta AI merapikan format `experiments/README.md` (OPS-084); isi langkah dan output yang diharapkan berasal dari apa yang benar-benar dijalankan tim.
- Meminta AI menjelaskan potongan kode rekan saat code review (OPS-086) agar reviewer memahami sebelum menyetujui — bukan agar reviewer melewatkan pembacaan.

**Tidak boleh**

- Memasukkan **data mentah, data pribadi, data partner, atau data RESTRICTED** ke prompt — termasuk "hanya 10 baris untuk contoh"; pakai skema tanpa nilai atau sampel sintetis ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §4; [SECURITY.md](../../SECURITY.md)).
- Meng-commit kode AI yang tidak dibaca dan diuji; anggota yang tidak bisa menjelaskan fungsi yang di-commit-nya adalah red flag reviewer ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3; [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.8).
- Membiarkan AI "menyesuaikan" metrik, baseline, atau split saat implementasi karena "lebih mudah dihitung" — metrik dan baseline terkunci di G5; perubahan hanya dengan alasan tertulis dan tanggal.
- Menerima angka baseline "perkiraan" dari AI atau membiarkan AI menulis apa pun ke `results/`; hasil hanya sah dari run tercatat (config, seed, log, git hash) ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.9).
- Memakai AI pada OPS-085 (log & jurnal): WBS menandainya tanpa bantuan AI — log adalah rekaman verifikasi manusia, diisi saat itu juga, bukan dari ingatan hari Jumat.

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Notebook contoh benar-benar dijalankan sendiri di environment bersih; kegagalan dicatat apa adanya, bukan disalin dari peserta lain | diri sendiri, dicek dosen pada 10 menit gate check | OPS-078 |
| Instalasi dari nol berhasil: `git clone` → instal environment → import modul, di mesin/venv yang belum pernah dipakai | tim (anggota yang tidak menyiapkan environment) | OPS-079 |
| Tidak ada overlap train/test (tes lulus); tidak ada data pribadi atau data mentah di working tree **maupun riwayat git**; `.gitignore` aktif | tim; mentor mengecek riwayat git saat berkunjung | OPS-080 |
| Metrik di `src/evaluate.py` identik (nama, rumus, agregasi) dengan metrik terkunci di `docs/research-design.md` §Metrics & Evaluation; baseline yang diimplementasi sama dengan §Baseline | tim; dosen pengampu memeriksa diff saat gate check | OPS-081 |
| Setiap fungsi berbantuan AI di `src/method.py` dibaca dan dipahami: anggota bisa menjelaskan apa yang dilakukannya tanpa membuka chat | tim (anggota yang meng-commit, diuji reviewer PR internal) | OPS-082 |
| Menjalankan satu perintah menghasilkan `results/` dan `logs/`; file hasil memuat git hash, seed, timestamp | tim | OPS-083 |
| Anggota lain mengikuti `experiments/README.md` dari clone bersih tanpa bertanya; langkah yang membingungkan dicatat untuk diperbaiki (latihan sebelum peer reproducer W10) | anggota tim yang tidak menulis README | OPS-084 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya: modul, utuh/diadaptasi, cara verifikasi, commit | diri sendiri | OPS-085 |
| Checklist kualitas kode terpenuhi: keterbacaan, seed, tanpa hardcode path absolut, tanpa data pribadi, tes lulus; reviewer manusia menyetujui PR internal | peer dalam tim (reviewer bukan penulis kode); mentor menjalankan `run.sh` di mesin lain bila sempat ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W9) | OPS-086 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W9, "dapat dibuka reviewer" berarti: yang menulis kode direproduksi oleh yang tidak menulisnya — Human Check silang, bukan sendiri-sendiri ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Pelajaran).

## Done When

Minggu ini **belum menutup gate**; G6 Experiment Ready ditutup di W10 setelah pilot dan reproduksi peer. Jawab ya/tidak per butir pada Jumat:

- [ ] `docs/journal/w09.md` berisi catatan reproduksi latihan (kegagalan + penyebab) dan refleksi: bagian repositori mana yang paling rapuh bila orang lain menjalankannya.
- [ ] `requirements.txt`/`environment.yml` dengan versi terkunci; instalasi dari nol berhasil di mesin/venv anggota lain.
- [ ] `experiments/pilot-01/config.yaml` memuat seed, split, hyperparameter; `set_seed` dipanggil di satu tempat.
- [ ] `src/data.py` berjalan; tes anti-leakage lulus; `data/README.md` lengkap (Dataset ID, sumber, akses, privasi, skema, split, sampel sintetis, daftar yang tidak ada di repo).
- [ ] `.gitignore` mengecualikan `data/raw/`, kredensial, `.env`; **tidak ada data mentah/pribadi di riwayat git** (diperiksa, bukan diasumsikan).
- [ ] `src/baseline.py` + `src/evaluate.py` berjalan pada subset; `results/pilot-01/baseline.json` memuat seed, tanggal, git hash; metrik identik dengan yang terkunci di G5.
- [ ] `src/method.py` berjalan dari config dan seed; smoke test pada sampel kecil lulus.
- [ ] `bash run.sh` (atau `make pilot`) menjalankan pipeline penuh dan menulis `results/pilot-01/` + `experiments/pilot-01/logs/`.
- [ ] `experiments/README.md` v0 diikuti anggota lain dari clone bersih tanpa bertanya; bagian *Reproducibility* README riset terisi.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Coding` per modul berbantuan AI dengan tanda utuh/diadaptasi dan cara verifikasi; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] PR internal `exp/pilot-01` termerge ke `research/g6-experiment` dengan komentar review dan checklist kualitas kode terpenuhi.
- [ ] README riset menunjukkan `G6 (in progress)`; branch `research/g6-experiment` ada; **metrik dan baseline tidak berubah** dari G5 (bila berubah, alasan dan tanggal tercatat).

**Progres menuju gate.** Butir-butir di atas adalah setengah pertama definition of done G6 ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G6): repositori berisi `src/`, `notebooks/`, `experiments/` dengan konfigurasi, seed, environment, dan README cara menjalankan. Setengah kedua dikerjakan di W10: pilot end-to-end pada subset (baseline + minimal satu pembanding, OPS-088), tabel hasil dan figur awal, sanity check dan uji leakage (label-shuffle harus jatuh ke chance, OPS-090), reproduksi peer dari tim lain (OPS-091) dan perbaikan README berdasarkan kendalanya (OPS-092), lalu PR **`GATE REVIEW: Experiment Ready — UIAI-YYYY-NNN`** dari branch `research/g6-experiment` memakai [experiment-review.md](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md) (OPS-094; [CONTRIBUTING.md](../../CONTRIBUTING.md) §3), disusul release `v0.5 Pilot Experiment`. Ingat kriterianya sejak sekarang: **lulus** jika peer dapat mereproduksi angka baseline dari repositori; **gagal** jika hasil hanya ada di laptop anggota tim. Bila W9 tertinggal, turunkan skala — subset lebih kecil, 3 seed — dan prioritaskan reproducibility README daripada hasil bagus; jangan pernah melewati reproduksi peer ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat). Jadwalkan peer reproducer dari tim lain **minggu ini**, karena jam orang lain tidak bisa dipercepat.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — struktur folder, konvensi branch/commit, isi minimal `data/README.md` dan `experiments/README.md`, bagian *Reproducibility* README riset, kriteria good vs weak (OPS-079, OPS-080, OPS-084, OPS-086).
- [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) — kartu pilot dari W8 adalah sumber seed/config/split/metrik yang diimplementasikan minggu ini; bagian pra-registrasi tidak diubah (OPS-079, OPS-081, OPS-082).
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — entri Stage `Coding`; contoh baris #7 "debugging parser" adalah pola yang dipakai minggu ini (OPS-085).
- [TPL-05 Dataset Registry Template](../../research-os/08-templates/05-dataset-registry-template.md) — Dataset ID dari W7 dicantumkan di `data/README.md`; aturan "GitHub = catalog, bukan storage" ([datasets-registry](../../datasets-registry/README.md) §4).
- [TPL-08 Research Design Card](../../research-os/08-templates/08-research-design-card.md) — rujukan untuk memastikan kode mengimplementasikan desain yang lolos G5, bukan desain baru; template PR [experiment-review.md](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md) untuk W10.

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W9 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.8 Data Plan, §3.9 Baseline & Metrics, §3.10 Pilot Experiment, §3.14 Reproducibility README, §4 Struktur repositori · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3 E3 Experiment, §3.5 E5 Execution · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5 Dataset & privacy, §2.7 Reproducibility, §2.8 AI usage · [MET-01 Positioning](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §7.2.
- [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.8 Coding, §3.9 Experiment · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.6 Reproduce, §3 · [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.7 Coding, §2.8 Notebooks & compute, §4 Kebijakan data.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S9 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G6 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rules B5–B6, §Slack dan buffer · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) §2 Reproducibility package, §5 Leakage · [SECURITY.md](../../SECURITY.md) · [LICENSING.md](../../LICENSING.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Notebook dengan path absolut laptop, dijalankan tidak berurutan.** Hasilnya "berjalan di mesin saya" dan gagal di mesin peer — level *Developing* pada rubrik E3/E5 ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3, §3.5). Cara menghindari: path relatif dari config; logika inti di `src/`; "Restart & run all" sebelum commit; anggota lain mengikuti README dari clone bersih sebelum Jumat.
2. **Leakage lewat kode "yang berhasil".** Normalisasi/imputasi/seleksi fitur sebelum split, duplikat lintas split, atau kolom yang diturunkan dari target membuat baseline tampak hebat dan pilot W10 "terlalu bagus". Cara menghindari: `src/data.py` memaksa urutan *split dulu → pra-pemrosesan pada train*; tes overlap dan tes "tidak ada fitur target" adalah bagian dari kode; label-shuffle sanity check direncanakan sekarang untuk W10 ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.7).
3. **Data mentah, kredensial, atau output notebook berisi data pribadi ikut ter-commit.** Sekali masuk riwayat git, penghapusan butuh penulisan ulang riwayat dan laporan ke pemilik data ([SECURITY.md](../../SECURITY.md) §5; [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5). Cara menghindari: `.gitignore` sebelum file data pertama disentuh; `git status` sebelum setiap commit; output notebook dibersihkan; sampel di repo hanya sintetis ≤100 baris.
4. **Metrik "menyesuaikan diri" saat implementasi.** Metrik yang dikunci di G5 diam-diam berubah menjadi yang tersedia di pustaka, atau baseline literatur diganti yang lebih lemah karena lebih mudah — metric switching dalam bentuk halus. Cara menghindari: `src/evaluate.py` membaca nama metrik dari config yang menyalin `docs/research-design.md` §Metrics & Evaluation; reviewer PR internal membandingkan keduanya; setiap perubahan dicatat dengan alasan dan tanggal.
5. **Kode AI di-commit karena "sudah jalan".** Anggota tidak bisa menjelaskan fungsi yang di-commit-nya; log AI Usage kosong padahal setengah `src/` dibantu AI; leakage bersembunyi di kode yang tidak dibaca ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.8). Cara menghindari: aturan tim "tidak bisa menjelaskan = tidak di-commit"; entri log per modul ditulis saat kode dibuat; reviewer PR internal meminta penulis menjelaskan satu fungsi acak.
6. **Mengejar angka bagus alih-alih pipeline yang benar.** Menghabiskan enam jam OPS-082 untuk tuning hyperparameter sebelum `run.sh` ada berarti pilot W10 dan reproduksi peer tidak punya dasar. Cara menghindari: target minggu ini adalah *satu perintah, hasil apa pun, dapat diulang* — tuning bukan bagian dari sprint ini; hasil buruk yang reproducible lebih berharga daripada hasil bagus yang hanya ada di laptop.
