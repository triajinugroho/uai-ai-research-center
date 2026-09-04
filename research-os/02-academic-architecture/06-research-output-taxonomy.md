# Research Output Taxonomy — Jenis Output Riset dan Kriteria Minimumnya

> **ID** ARC-06 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa, pembimbing TA, dosen pengampu MK mode R, pengelola registry (`publications/`, `datasets-registry/`), tim KPI
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [ARC-04 Build–Prove–Contribute](04-build-prove-contribute.md) · [MET-05 Publication Backward Design](../04-metopen-research-studio/05-publication-backward-design.md) · [TPL-05 Dataset Registry](../08-templates/05-dataset-registry-template.md) · [TPL-06 Publication Venue Registry](../08-templates/06-publication-venue-registry-template.md) · [LICENSING.md](../../LICENSING.md) · [publications/](../../publications/README.md) · [datasets-registry/](../../datasets-registry/README.md)

## 1. Outcome riset bukan hanya "jurnal"

Kalau satu-satunya output yang dihitung adalah artikel jurnal, tiga hal buruk terjadi: mahasiswa dan dosen terdorong ke venue yang mudah (termasuk predator), riset yang menghasilkan dataset atau software bernilai tidak dihargai, dan hasil negatif yang jujur tidak punya tempat. Di computing, *paper bukan satu-satunya produk penelitian*: dataset, source code, model, konfigurasi, benchmark, prompt, seed, notebook, log eksperimen — semuanya adalah output ilmiah yang dapat direview dan dipakai ulang.

Taksonomi ini menetapkan **tiga belas jenis output** yang diakui pusat riset, masing-masing dengan kriteria minimum, skema ID, tempat registrasi, lisensi default, dan level maturity yang biasanya menghasilkannya. Prinsipnya: **publication oriented, not publication obsessed** — setiap riset menuju output yang bisa diperiksa orang lain, dan jurnal hanyalah salah satunya.

## 2. Ringkasan tiga belas jenis

| # | Jenis | ID | Registrasi | Lisensi default | Maturity yang biasanya menghasilkan |
|---|---|---|---|---|---|
| 1 | Proposal (TA/penelitian) | Research ID | Repositori riset (`paper/` atau `docs/`) + release `v1.0` | CC BY 4.0 (dokumen) / INTERNAL bila belum siap | TA Ready → Research Ready |
| 2 | Manuscript | `PUB-YYYY-NNN` (status Draft) | `publications/` | Hak cipta penulis; INTERNAL sampai submitted | Research Ready → Publication Ready |
| 3 | Journal article | `PUB-YYYY-NNN` | `publications/` (metadata, DOI) | Mengikuti publisher; preprint bila diizinkan | Publication Ready |
| 4 | Conference paper | `PUB-YYYY-NNN` | `publications/` | Mengikuti publisher | Publication Ready |
| 5 | Dataset | `DS-YYYY-NNN` | `datasets-registry/` (metadata saja) | **Tidak ada default** — data governance review | Research Ready → Impact Ready |
| 6 | Benchmark | `ART-YYYY-NNN` (+ `DS-` bila memuat data) | `publications/` bagian artefak + `datasets-registry/` | Kode Apache-2.0; data lewat review | Research Ready → Publication Ready |
| 7 | Software / tools riset | `ART-YYYY-NNN` | `publications/` bagian artefak; repositori public | Apache-2.0 | Research Ready → Impact Ready |
| 8 | Model | `ART-YYYY-NNN` | `publications/` bagian artefak; weights di HF/server | Research-only license atau tidak dirilis; kode Apache-2.0 | Research Ready → Publication Ready |
| 9 | HKI | `ART-YYYY-NNN` + nomor HKI | `publications/` bagian artefak | Restricted sampai IP review | Impact Ready |
| 10 | Prototype | `ART-YYYY-NNN` | `publications/` bagian artefak | Apache-2.0 atau restricted (bila komersial) | Research Ready → Impact Ready |
| 11 | Research brief | Research ID (dokumen) | Repositori riset `docs/`; opsional `research-roadmap/domains/` | CC BY 4.0 | TA Ready ke atas |
| 12 | Poster | Research ID (dokumen) | Repositori riset `presentation/` | CC BY 4.0 | Research Ready |
| 13 | Competition project | Research ID + `ART-` bila ada artefak | Issue entry door *Competition*; `publications/` bagian artefak | Mengikuti aturan lomba; kode Apache-2.0 bila boleh | Idea → Research Ready |

Aturan ID: satu riset punya satu **Research ID** (`UIAI-YYYY-NNN`); output-nya mendapat ID sendiri (`PUB-`, `DS-`, `ART-`) yang selalu menunjuk balik ke Research ID ([GOVERNANCE.md §5](../../GOVERNANCE.md)). Dokumen turunan (proposal, brief, poster) tidak mendapat ID sendiri; ia dicatat sebagai file dalam repositori riset.

## 3. Rincian per jenis

### 3.1 Proposal

- **Definisi.** Dokumen formal rencana riset: Proposal TA (dari Research Pack) atau proposal penelitian dosen/hibah yang memuat riset mahasiswa.
- **Kriteria minimum.** Semua komponen Research Pack sampai Research Design terisi; RQ dapat ditelusuri ke synthesis matrix; baseline dan metrik ditetapkan; threats to validity awal; ethics & privacy; AI Usage Statement. Setara lolos G5, idealnya G8.
- **Contoh.** Proposal TA `UIAI-2026-017` "Stabilitas lintas angkatan model deteksi dini mahasiswa berisiko" (lihat skenario [ARC-04 §10](04-build-prove-contribute.md)).

### 3.2 Manuscript

- **Definisi.** Naskah ilmiah yang sedang disiapkan untuk venue tertentu; belum submitted.
- **Kriteria minimum.** Mengikuti [MET-05](../04-metopen-research-studio/05-publication-backward-design.md): venue target dipilih dari registry ([TPL-06](../08-templates/06-publication-venue-registry-template.md)) dengan status etika publikasi jelas; struktur IMRaD atau format venue; setiap klaim menunjuk tabel/figur; threats to validity; AI disclosure sesuai kebijakan venue; lolos peer review internal ([TPL-12](../08-templates/12-peer-review-template.md)).
- **Status.** Draft → manuscript-ready → submission-ready → submitted → accepted → published; dicatat pada kartu publikasi.
- **Contoh.** `PUB-2027-003` draft untuk venue AI dalam pendidikan, status submission-ready.

### 3.3 Journal article

- **Definisi.** Manuscript yang diterima/terbit di jurnal ilmiah.
- **Kriteria minimum.** Jurnal terindeks/terakreditasi dan **bukan predator** (diperiksa lewat venue registry); DOI; afiliasi UAI; mahasiswa sebagai penulis bila memenuhi kriteria kontribusi; kode/data pendukung tersedia sesuai lisensi; PDF publisher **tidak** disimpan di repo kecuali diizinkan.
- **Contoh.** Artikel hasil TA `UIAI-2026-017`, terbit 2027, dicatat `PUB-2027-003` status published dengan tautan ke `DS-2026-004` dan `ART-2027-002`.

### 3.4 Conference paper

- **Definisi.** Paper yang diterima di konferensi/seminar ilmiah (termasuk workshop) dengan proses review.
- **Kriteria minimum.** Sama dengan journal article; ditambah presentasi (slide/poster disimpan di `presentation/`). Konferensi tanpa review tidak dihitung sebagai conference paper (dicatat sebagai *dissemination* biasa).
- **Contoh.** Paper 6 halaman hasil pilot Metopen di seminar nasional informatika; `PUB-2027-001`.

### 3.5 Dataset

- **Definisi.** Kumpulan data yang dikumpulkan/dianotasi/dikurasi riset dan dapat dipakai riset lain.
- **Kriteria minimum.** Kartu dataset lengkap ([TPL-05](../08-templates/05-dataset-registry-template.md)): sumber, owner, ukuran, modality, kualitas, privasi (Public/Restricted/Confidential), lisensi, potensi RQ; pedoman anotasi bila ada anotasi; data fisik di server institusi/HF/Kaggle/Drive, **bukan** di GitHub; review data governance sebelum lisensi ditetapkan; consent/izin bila data manusia ([SECURITY.md](../../SECURITY.md)).
- **Lisensi.** Tidak ada default. Dibuat UAI dan aman dibuka → CC BY 4.0 atau CC0; mengandung data pribadi/partner → tidak ada lisensi publik, hanya metadata.
- **Contoh.** `DS-2026-004` log aktivitas LMS anonim (Restricted; metadata publik); `DS-2026-002` katalog produk halal (contoh dari dokumen sumber); `DS-2026-003` korpus teks Bahasa Indonesia untuk satu tugas klasifikasi.

### 3.6 Benchmark

- **Definisi.** Paket evaluasi standar: tugas, data uji, metrik, protokol, dan baseline, agar metode berbeda dapat dibandingkan secara adil.
- **Kriteria minimum.** Protokol evaluasi tertulis (split, metrik, larangan leakage); minimal dua baseline dengan angka tereproduksi; skrip evaluasi; lisensi kode dan data terpisah; versi (semver) karena benchmark berevolusi.
- **Contoh.** Benchmark kecil klasifikasi teks layanan akademik Bahasa Indonesia: 3 baseline, skrip evaluasi, `ART-2027-005` + `DS-2027-001`.

### 3.7 Software / tools riset

- **Definisi.** Perangkat lunak yang dapat dipakai ulang: library, pipeline, tool anotasi, skrip eksperimen yang dikemas.
- **Kriteria minimum.** Repositori public dengan README, instalasi, contoh pakai, tes dasar, `CITATION.cff`, lisensi Apache-2.0; release bertag; tidak memuat data sensitif atau kredensial; IP review singkat sebelum rilis bila berpotensi komersial ([LICENSING.md §6](../../LICENSING.md)).
- **Contoh.** Pipeline pra-pemrosesan log LMS + fitur mingguan, `ART-2027-002`.

### 3.8 Model

- **Definisi.** Model terlatih (weights) beserta kartu model.
- **Kriteria minimum.** Model card: data latih (ID dataset), prosedur, metrik pada benchmark/baseline, keterbatasan, penggunaan yang tidak disarankan, bias yang diketahui; kode pelatihan dan evaluasi reproducible; weights disimpan di HF/server, bukan git; weights dari data sensitif **tidak** dirilis tanpa review.
- **Lisensi.** Kode Apache-2.0; weights research-only atau tidak dirilis; dinyatakan per komponen di README riset.
- **Contoh.** Model klasifikasi teks Bahasa Indonesia untuk tiket layanan, `ART-2027-006`, weights research-only.

### 3.9 HKI

- **Definisi.** Hak Kekayaan Intelektual yang didaftarkan (hak cipta program komputer, paten, desain) atas output riset.
- **Kriteria minimum.** IP review bersama `@directors`; dokumen pendaftaran lewat unit HKI universitas; artefak yang didaftarkan tetap punya `ART-` dan Research ID; lisensi publik ditahan sampai keputusan; nomor HKI dicatat di kartu artefak.
- **Contoh.** Hak cipta program komputer atas prototype sistem rekomendasi produk halal, `ART-2027-009`, status restricted.

### 3.10 Prototype

- **Definisi.** Sistem yang berfungsi (bukan produksi) yang menunjukkan kelayakan solusi AI untuk domain nyata; sering hasil Proyek Perangkat Lunak atau TA design-science.
- **Kriteria minimum.** Dapat dijalankan mengikuti README; evaluasi dengan pengguna atau skenario (bukan hanya "berjalan"); keterbatasan dinyatakan; AI Usage Statement; data demo tidak sensitif; lisensi ditetapkan (Apache-2.0 atau restricted).
- **Contoh.** Prototype asisten konsultasi akademik berbasis RAG dengan evaluasi 8 pengguna, `ART-2026-003`.

### 3.11 Research brief

- **Definisi.** Ringkasan 1–2 halaman hasil riset untuk pengambil keputusan (Prodi, fakultas, mitra, pemerintah) — bahasa non-teknis, rekomendasi, keterbatasan.
- **Kriteria minimum.** Menyebut Research ID; klaim tidak melebihi bukti; menyebut keterbatasan dan langkah lanjut; disetujui pembimbing/mentor; CC BY 4.0.
- **Contoh.** Brief untuk bagian akademik tentang deteksi dini mahasiswa berisiko: apa yang berhasil, apa yang belum, apa yang diperlukan untuk uji coba.

### 3.12 Poster

- **Definisi.** Presentasi visual satu halaman untuk seminar/pameran riset/hari riset Prodi.
- **Kriteria minimum.** Problem, RQ, metode, hasil dengan baseline terlihat, threats to validity, kontribusi, Research ID, QR ke repositori; disimpan di `presentation/`.
- **Contoh.** Poster hasil pilot Metopen pada Research Day Prodi.

### 3.13 Competition project

- **Definisi.** Proyek yang diikutsertakan dalam lomba (data science, hackathon, karya ilmiah, inovasi) yang masuk pipeline lewat entry door *Competition*.
- **Kriteria minimum.** Diregistrasi sebagai Issue dengan Research ID; repositori standar; hasil lomba dicatat; bila menghasilkan artefak → `ART-`; bila ingin naik ke TA/paper harus melewati gate seperti riset lain (lomba tidak menggantikan G3–G5).
- **Contoh.** Proyek hackathon "chatbot layanan halal" yang kemudian menjadi masalah backlog `UIAI-2026-021`.

## 4. Matriks jenis output × maturity

| Jenis | Idea | TA Ready | Research Ready | Publication Ready | Impact Ready |
|---|---|---|---|---|---|
| Proposal | | **●** | ● | | |
| Research brief | | ● | ● | ● | ● |
| Poster | | | **●** | ● | |
| Manuscript | | | ● | **●** | |
| Conference paper | | | | **●** | |
| Journal article | | | | **●** | ● |
| Dataset | | | ● | ● | **●** |
| Benchmark | | | ● | **●** | |
| Software/tools | | | ● | ● | **●** |
| Model | | | ● | **●** | |
| Prototype | | | ● | | **●** |
| HKI | | | | | **●** |
| Competition project | ● | ● | ● | | |

● = lazim; **●** = paling khas. Matriks ini membantu menetapkan endgame di G1: mahasiswa yang menargetkan *Impact Ready* harus tahu bahwa outputnya dataset/software/prototype/HKI, bukan hanya laporan.

## 5. Hubungan dengan release milestone

| Release | Output yang biasanya lahir |
|---|---|
| v0.3 Research Design | Proposal (draft), Research brief awal |
| v0.5 Pilot Experiment | Poster, dataset card v0, repositori eksperimen |
| v0.8 Manuscript Draft | Manuscript |
| v1.0 Research Pack | Proposal TA final, Research Pack |
| v1.1 Submitted | Manuscript submitted; dataset/artefak siap rilis |
| v2.0 Published | Journal/conference paper, dataset rilis, software/model rilis, HKI |

## 6. Aturan penghitungan untuk KPI

1. **Satu riset boleh menghasilkan banyak output**; setiap output dihitung sekali pada jenisnya.
2. **Jangan hitung ganda**: manuscript yang menjadi journal article dihitung sebagai journal article (kartu `PUB-` sama, status berubah), bukan dua output.
3. **Dataset dan software dihitung setara paper** dalam KPI output ([GOV-03](../07-governance/03-kpi-and-measurement.md)) agar tidak ada insentif mengejar jurnal saja.
4. Output tanpa registrasi (tidak ada `PUB-`/`DS-`/`ART-` atau file di repositori riset) **tidak dihitung**.
5. Publikasi di venue yang ditandai bermasalah pada venue registry tidak dihitung dan dicatat sebagai risiko ([GOV-04](../07-governance/04-risk-register.md)).

## 7. Ringkasan

- Tiga belas jenis output diakui; jurnal hanya satu di antaranya.
- Setiap output punya kriteria minimum, ID (`PUB-`/`DS-`/`ART-` atau file dalam repositori riset), tempat registrasi, dan lisensi default sesuai [LICENSING.md](../../LICENSING.md).
- Dataset tidak punya lisensi default dan tidak pernah disimpan mentah di GitHub; HKI dan aset komersial restricted sampai IP review.
- Endgame di G1 dipilih dari taksonomi ini; KPI menghitung semua jenis, bukan hanya jurnal.
