# Metopen Course Outcomes — CPMK, Tiga Layer Outcome, dan Peta Gate

> **ID** MET-02 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu Metopen, tim kurikulum/OBE Prodi, penyusun RPS, reviewer gate, mahasiswa
> **Terkait** [MET-01 Positioning](01-metopen-positioning.md) · [MET-03 16-Week Blueprint](03-metopen-16-week-blueprint.md) · [MET-04 Research Pack](04-research-pack-specification.md) · [MET-06 5E Rubric](06-assessment-and-5e-rubric.md) · [ARC-05 CPL–CPMK–Artifact Alignment](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [MST-03 Glossary](../00-master/03-glossary.md)

## 1. Prinsip penyusunan CPMK

CPMK Metopen bukan daftar topik yang "dibahas", melainkan **kemampuan yang dibuktikan dengan artefak**. Setiap CPMK memiliki empat pengikat:

1. **Kata kerja terukur** — mahasiswa *merumuskan*, *memetakan*, *merancang*, *menjalankan*, *mempertahankan*; bukan *memahami* atau *mengetahui*.
2. **Artefak Research Pack** — bukti bahwa kemampuan itu ada ([MET-04](04-research-pack-specification.md)).
3. **Gate** — titik ketika artefak direview lulus/gagal ([OPS-03](../06-execution-os/03-research-gates.md)).
4. **Bobot** — porsi dalam nilai akhir, dioperasionalkan lewat rubrik 5E ([MET-06](06-assessment-and-5e-rubric.md)).

Rantai lengkapnya mengikuti [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md): **CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence.**

## 2. Prasyarat yang sudah dimiliki mahasiswa

Metopen tidak mengulang materi. Ia memakai kompetensi enam semester sebelumnya sebagai bahan baku.

| Semester | Mata kuliah (dokumen diskusi; verifikasi ke kurikulum resmi) | Dipakai di Metopen untuk |
|---|---|---|
| 1 | Statistika, Kalkulus | Membaca metrik, distribusi, variansi; statistical thinking di W11 |
| 2 | Statistika Terapan, Matematika Diskrit | Uji sederhana, interval, sampling; logika hipotesis/falsifikasi |
| 3 | HCI, Struktur Data, Basis Data | User study & survey design (W7); data plan & skema data (W9) |
| 4 | Analisis Algoritma, RPL, Data Mining | Benchmarking & kompleksitas; empirical SE; pipeline data & evaluasi |
| 5 | AI & Machine Learning, Pengujian Perangkat Lunak | Baseline, metrik, leakage, error analysis (W7, W10–W11); pengujian sebagai bukti |
| 6 | Proyek Perangkat Lunak, Kerja Praktik, Etika Profesi | Kerja tim & git (S0, W9); problem dari dunia nyata (W2); etika & integritas (W1, W7) |

Asumsi kerja: mahasiswa yang masuk Metopen sudah bisa menulis kode, mengolah data, melatih model sederhana, dan bekerja dalam tim. Yang belum mereka miliki adalah **disiplin bukti**. Bila asumsi ini tidak terpenuhi untuk sebagian mahasiswa, Sprint S0 (onboarding) memberi jalur penyegaran, bukan minggu tambahan.

## 3. Tiga layer outcome

| Layer | Nama | Definisi | Bukti | Setara gate | Target populasi |
|---|---|---|---|---|---|
| Minimum | **TA Ready** | Mahasiswa masuk semester VIII dengan masalah, bukti literatur, RQ, dan desain metode yang sudah direview; tidak lagi mencari judul dan metode | Research Pack dengan artefak wajib Metopen lengkap; proposal TA draft; G5 lulus | G5 | 100% mahasiswa |
| Target | **Research Ready** | Mahasiswa mampu menjalankan satu penelitian computing sederhana secara benar: pilot berjalan, direproduksi peer, klaim tidak melebihi bukti | Pilot Experiment + Reproducibility README + CER table; G7 lulus | G6–G7 | Mayoritas tim |
| Aspirational | **Publication / Impact Ready** | Hasil layak dilanjutkan menjadi paper, dataset, open-source artifact, HKI, prototype, bagian riset dosen, atau solusi industri/masyarakat | Research Pack v1.0 + manuscript draft v0.8 + handoff ke mentor/AI Center | G8 + manuscript-ready ([MET-05](05-publication-backward-design.md)) | Tim terbaik |

Layer tidak menggantikan nilai. Nilai huruf mengikuti [MET-06](06-assessment-and-5e-rubric.md); layer adalah **status kematangan riset** (`maturity:*`) yang dicatat di Mission Control dan mengikuti riset ke TA.

## 4. Tiga belas CPMK

Format tiap CPMK: rumusan capaian → indikator → artefak Research Pack → minggu/gate → bobot. Kode `CPMK-NN` bersifat internal dokumen ini; pemetaan ke kode CPMK resmi RPS diisi oleh penyusun RPS (`[isi]`).

### CPMK-01 Problem Formulation

**Capaian:** Mahasiswa mampu **merumuskan** masalah riset secara problem-first dari fenomena nyata, lengkap dengan stakeholder, konteks, dan konsekuensi keputusan.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Masalah dinyatakan tanpa menyebut solusi/algoritma di kalimat pertama | Problem Brief | W2 / G2 | 8% |
| Stakeholder dan keputusan yang berubah dinyatakan eksplisit | Stakeholder/Impact Statement | W2 / G2 | |
| Endgame (TA/paper/artefak) dan entry door ditetapkan | `docs/endgame.md`, One-Pager v0 | W1 / G1 | |
| Orang luar dapat menjelaskan ulang masalah dalam dua kalimat | Uji peer di studio | W2 | |

### CPMK-02 Evidence Discovery

**Capaian:** Mahasiswa mampu **menemukan** literatur primer yang relevan dengan strategi pencarian terdokumentasi dan memverifikasi keberadaan setiap sumber.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Strategi pencarian ditulis: kata kunci, basis data, citation chaining, kriteria inklusi/eksklusi | `docs/search-strategy.md` | W3 / G3 | 6% |
| 15–25 sumber primer terverifikasi (DOI/URL) | `references.bib` | W3–W4 / G3 | |
| Sumber temuan AI dicatat dan diverifikasi | AI Usage Log | W3 / G3 | |

### CPMK-03 Synthesis

**Capaian:** Mahasiswa mampu **menyintesis** literatur ke dalam synthesis matrix yang memperlihatkan pola, konsistensi, dan pertentangan — bukan ringkasan satu per satu.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Matriks berisi kolom problem, metode, data, metrik, hasil, keterbatasan, relevansi | `literature/synthesis-matrix.csv` | W4–W5 / G3 | 8% |
| Bagian "pola" menyebut apa yang konsisten, bertentangan, belum diuji | Literature Evidence Map | W5 / G3 | |
| Setiap baris matriks dapat dicocokkan dengan isi paper (bukan abstrak AI) | Spot-check reviewer | W5 / G3 | |

### CPMK-04 Research Gap

**Capaian:** Mahasiswa mampu **menurunkan** research gap yang dapat ditelusuri ke baris synthesis matrix (Gap–Claim–Evidence alignment).

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Gap merujuk baris/sumber tertentu, bukan naratif "belum ada di UAI" | Research Gap | W5 / G3→G4 | 6% |
| Jenis gap dinyatakan (empiris, metodologis, kontekstual, replikasi, artefak) | Research Gap | W5 | |

### CPMK-05 Research Question

**Capaian:** Mahasiswa mampu **merumuskan** research question yang spesifik, dapat dijawab dalam batas semester + TA, dan selaras dengan gap.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| RQ menyebut konstruk, konteks, dan pembanding | RQ/Hypothesis | W6 / G4 | 6% |
| Setiap RQ dapat ditelusuri ke gap | `docs/research-question.md` | W6 / G4 | |
| Contribution Statement menyebut jenis kontribusi | Contribution Statement | W6 / G4 | |

### CPMK-06 Hypothesis

**Capaian:** Mahasiswa mampu **menyusun** hipotesis yang dapat difalsifikasi beserta kondisi yang akan membuatnya salah.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Hipotesis punya arah, variabel, dan kriteria penolakan | RQ/Hypothesis, Experiment Card | W6–W7 / G4–G5 | 4% |
| "Apa yang akan kami lihat jika hipotesis salah" ditulis | Experiment Card | W7 / G5 | |

### CPMK-07 Methods

**Capaian:** Mahasiswa mampu **memilih dan merancang** metode dari Computing Research Methods Map beserta data plan, baseline, dan metrik yang selaras dengan RQ.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Jenis metode dipilih dengan alasan dan alternatif yang ditolak | Research Design (TPL-08) | W7–W8 / G5 | 12% |
| Baseline paling sederhana dan metrik selaras RQ ditetapkan sebelum eksperimen | Baseline & Metrics | W7 / G5 | |
| Data plan menyebut sumber, akses, lisensi, privasi, representativitas | Dataset/Data Plan | W7 / G5 | |
| Desain dipertahankan di Design Defense dan direvisi | Notulen red team | W8 / G5 | |

### CPMK-08 Experiment

**Capaian:** Mahasiswa mampu **menjalankan** pilot experiment end-to-end dalam repositori yang dapat direproduksi orang lain.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Repositori berisi kode, konfigurasi, seed, environment, README run | Reproducibility README, `experiments/` | W9 / G6 | 12% |
| Pilot berjalan pada subset data: baseline + ≥1 pembanding | Pilot Experiment | W10 / G6 | |
| Peer berhasil mereproduksi angka baseline | Catatan reproduksi | W10 / G6 | |

### CPMK-09 Validity

**Capaian:** Mahasiswa mampu **mengidentifikasi dan menangani** threats to validity (internal, eksternal, konstruk, statistik) sebelum dan sesudah eksperimen.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Threats awal ditulis di desain, termasuk leakage dan bias data | Threats to Validity v1 | W7 / G5 | 8% |
| Threats diperbarui berdasarkan apa yang terjadi di pilot | Threats to Validity v2 | W12 / G7 | |
| Klaim dibatasi sesuai threats | CER table | W12 / G7 | |

### CPMK-10 AI-Assisted Research

**Capaian:** Mahasiswa mampu **menggunakan** AI sebagai research copilot sesuai protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own, pada level minimal **AI Investigator** dengan perilaku **AI Governor**.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| AI Usage Log terisi konsisten: tool, tujuan, output, verifikasi, dipakai/tidak | AI Usage Log (TPL-10) | S0–W16 / setiap gate | 6% |
| Tidak ada referensi/hasil buatan AI yang lolos verifikasi | Spot-check reviewer | setiap gate | |
| AI Usage Statement menjelaskan peran AI dalam metode | AI Usage Statement | W13–W15 / G8 | |
| Self-assessment level kompetensi ([AIX-02](../05-ai-augmented-research/02-ai-research-competency-framework.md)) | Checklist | W1, W8, W16 | |

### CPMK-11 Research Integrity

**Capaian:** Mahasiswa **menunjukkan** amanah epistemik: tidak ada fabrikasi, falsifikasi, plagiarisme, sitasi palsu, penyembunyian hasil negatif, atau AI yang tidak diungkap.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Lolos Research Integrity check pada setiap gate | Review gate | G1–G8 | **Gate lulus/gagal, bukan skor** |
| Research Integrity Checklist ditandatangani | TPL-11 | W15 / G8 | |
| Ethics & Privacy terisi; data sensitif tidak di-commit | `docs/ethics.md`, `ETHICS.md` | W7, W9 / G5–G6 | |

Kegagalan integritas membatalkan gate terlepas dari kualitas lain ([MET-07](07-research-integrity-and-ethics.md), [MET-06](06-assessment-and-5e-rubric.md)).

### CPMK-12 Scientific Writing

**Capaian:** Mahasiswa mampu **menulis** proposal TA (atau manuscript) dengan struktur claim–evidence–reasoning, sitasi yang benar, dan pengungkapan AI.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Proposal mengikuti struktur IMRaD/proposal computing ([MET-05](05-publication-backward-design.md)) | Proposal TA | W13 / G8 | 12% |
| Setiap klaim menunjuk tabel/figur/sumber | Proposal, CER table | W13–W15 / G8 | |
| Revisi menanggapi peer review secara terdokumentasi | Response to reviewers | W15 / G8 | |
| Menulis review untuk tim lain (TPL-12) | Peer review | W14 | |

### CPMK-13 Research Defense

**Capaian:** Mahasiswa mampu **mempertahankan** desain (W8) dan temuan (W16) secara lisan dengan merujuk bukti, dan mengakui batas klaim.

| Indikator | Artefak | Minggu / Gate | Bobot |
|---|---|---|---|
| Mid-semester pitch menjawab pertanyaan red team dengan bukti/desain | Slide pitch, notulen | W8 / G5 | 12% |
| Defense 7–10 menit mengikuti TPL-13; jawaban merujuk figur/tabel | Research Pitch, rekaman/notulen | W16 / G8 | |
| Mengakui keterbatasan tanpa diminta | Penilaian penguji | W16 / G8 | |

### Rekapitulasi bobot

| CPMK | Nama | Bobot | Dimensi 5E utama |
|---|---|---|---|
| 01 | Problem Formulation | 8% | End |
| 02 | Evidence Discovery | 6% | Evidence |
| 03 | Synthesis | 8% | Evidence |
| 04 | Research Gap | 6% | Evidence |
| 05 | Research Question | 6% | End |
| 06 | Hypothesis | 4% | End / Experiment |
| 07 | Methods | 12% | Experiment |
| 08 | Experiment | 12% | Experiment / Execution |
| 09 | Validity | 8% | Explanation |
| 10 | AI-Assisted Research | 6% | Execution |
| 11 | Research Integrity | gate | (mandatory pass) |
| 12 | Scientific Writing | 12% | Explanation |
| 13 | Research Defense | 12% | Explanation / End |
| | **Total** | **100%** | |

Cara bobot ini diturunkan menjadi komponen nilai (milestone portfolio, defense, peer review, partisipasi sprint) ada di [MET-06](06-assessment-and-5e-rubric.md).

## 5. Peta CPMK × 16 minggu × gate

`●` = minggu utama (artefak dinilai), `○` = minggu pendukung (dilatih/direvisi).

| CPMK | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 | W13 | W14 | W15 | W16 | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 Problem | ● | ● | | | | ○ | | ○ | | | | | ○ | | | | G1, G2 |
| 02 Discovery | | ○ | ● | ○ | | | | | | | | | | | | | G3 |
| 03 Synthesis | | | ○ | ● | ● | | | | | | | | | | | | G3 |
| 04 Gap | | | | ○ | ● | ○ | | | | | | | | | | | G3, G4 |
| 05 RQ | | | | | ○ | ● | ○ | ○ | | | | ○ | | | | | G4 |
| 06 Hypothesis | | | | | | ● | ● | | | | | | | | | | G4, G5 |
| 07 Methods | | | | | | | ● | ● | ○ | | | | | | | | G5 |
| 08 Experiment | | | | | | | | | ● | ● | ○ | | | | | | G6 |
| 09 Validity | | | | | | | ● | ○ | | ○ | ○ | ● | | | | | G5, G7 |
| 10 AI-Assisted | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● | ○ | semua |
| 11 Integrity | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ | ● | ● | semua (pass/fail) |
| 12 Writing | | | | | | | | | | | ○ | ○ | ● | ● | ● | | G8 |
| 13 Defense | | | | | | | | ● | | | | | | | ○ | ● | G5, G8 |
| **Gate minggu** | G1 | G2 | G3 | G3 | G3 | G4 | G5 | G5 | G6 | G6 | G7 | G7 | G8 | G8 | G8 | G8 | |

Ketentuan turunan:

- Tidak ada minggu tanpa CPMK yang dinilai; tidak ada CPMK tanpa minggu utama.
- Gate adalah titik penilaian CPMK; nilai CPMK diberikan saat PR `GATE REVIEW` di-merge, bukan saat "tugas dikumpulkan".
- CPMK-10 dan CPMK-11 bersifat lintas minggu; buktinya adalah AI Usage Log dan integrity check di setiap gate.

## 6. Hubungan ke CPL

Pemetaan ke kode CPL resmi Prodi Informatika UAI diisi oleh tim kurikulum (`[isi]`); dokumen ini hanya menetapkan **kategori CPL generik** yang didukung, mengikuti kerangka [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md).

| Kategori CPL generik | Kode CPL Prodi | CPMK pendukung | Bukti (artefak) |
|---|---|---|---|
| Sikap: integritas akademik, tanggung jawab, etika profesi dan nilai Islami | `[isi]` | 11, 10, 13 | TPL-11, AI Usage Statement, `docs/ethics.md` |
| Pengetahuan: konsep dan metode riset computing (experiment, benchmark, design science, empirical SE, ML evaluation) | `[isi]` | 07, 08, 09 | Research Design, Pilot Experiment, Threats to Validity |
| Keterampilan umum: berpikir kritis, komunikasi ilmiah lisan dan tulisan, kerja tim | `[isi]` | 03, 12, 13 | Synthesis matrix, Proposal TA, Research Pitch |
| Keterampilan umum: pembelajaran mandiri dan pemanfaatan teknologi digital secara bertanggung jawab | `[isi]` | 02, 10 | Search strategy, AI Usage Log |
| Keterampilan khusus: merumuskan masalah dan pertanyaan riset di bidang Informatika | `[isi]` | 01, 04, 05, 06 | Problem Brief, Research Gap, RQ/Hypothesis |
| Keterampilan khusus: membangun artefak komputasi yang dapat diuji dan direproduksi | `[isi]` | 08 | Research Repository, Reproducibility README |

Evidence CPL untuk akreditasi/OBE dapat diambil langsung dari Research Pack dan riwayat PR gate ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)), tanpa membuat portofolio terpisah.

## 7. Cara memakai dokumen ini

| Pengguna | Gunakan untuk |
|---|---|
| Penyusun RPS | Salin CPMK-01…13 ke format RPS; isi kode CPL; ambil minggu dari §5 dan aktivitas dari [MET-03](03-metopen-16-week-blueprint.md) |
| Dosen pengampu | Tentukan apa yang dinilai di tiap gate; pakai rubrik [MET-06](06-assessment-and-5e-rubric.md) |
| Mahasiswa | Ketahui bukti apa yang harus ada di tiap minggu; self-check terhadap indikator |
| Reviewer gate | Cek indikator CPMK yang terkait gate saat menilai PR |
| Tim akreditasi | Tarik rantai CPL → CPMK → artefak → bukti dari repositori riset |

Perubahan CPMK diusulkan lewat PR ke dokumen ini dan harus diikuti pembaruan [MET-03](03-metopen-16-week-blueprint.md), [MET-04](04-research-pack-specification.md), dan [MET-06](06-assessment-and-5e-rubric.md) agar rantai bukti tetap utuh.
