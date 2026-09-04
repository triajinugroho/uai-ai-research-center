# Natural Language Processing (Mata Kuliah/Topik Pilihan Bidang NLP) — Course Research Guide

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — nama MK resmi, semester, SKS `[isi]`; artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [ARC-01 Capability Spiral](../../../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-02 Curriculum Research Map](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-05 CPL–CPMK–Artifact](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [AIR-02 AI Research Clusters](../../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [Assessment](../../assessment/README.md)

## 1. Identitas mata kuliah

| Field | Nilai |
|---|---|
| Nama resmi | [isi] — mata kuliah/topik pilihan bidang NLP Prodi Informatika |
| Semester | [isi] |
| SKS | [isi] |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **R — Research-Producing** |
| Tahun spiral ([ARC-01](../../../research-os/02-academic-architecture/01-research-capability-spiral.md)) | Year 3 — Experiment & Evaluate (atau Year 2 bila ditempatkan lebih awal) |
| Entry door yang dibuka | **Dataset** (korpus) dan **Course Project** |
| Klaster utama | C1 AI Models, Data & Knowledge — Indonesian NLP |
| Klaster sekunder | C4 Applied AI (teks domain: pendidikan, halal, kesehatan, pemerintahan); C3 Responsible AI (bias bahasa, privasi teks) |
| Field **Course** di Mission Control | `NLP` |
| Pengampu | [isi] |

Prodi Informatika UAI memosisikan kompetensinya pada Software Engineering, Data Science, IoT, dan **NLP** (dokumen diskusi). Nama mata kuliah yang membawa bidang ini belum tampak pada tabel kurikulum yang dikutip; folder ini menampung MK/topik pilihan mana pun yang mengampu bidang NLP. Pengampu mengisi identitas resminya.

## 2. Mengapa mode R

NLP Indonesia adalah wilayah di mana **data adalah kontribusi**. Korpus kecil yang dianotasi dengan guideline jelas, agreement yang dilaporkan jujur, dan benchmark baseline yang dapat direproduksi bernilai lebih tinggi bagi klaster C1 daripada satu model lagi di atas dataset publik. Karena itu MK ini ditetapkan mode R dengan asset **korpus/anotasi kecil + benchmark**.

Tiga alasan tambahan:

1. Korpus berbahasa Indonesia dan bahasa daerah untuk domain UAI (pendidikan, halal, pemerintahan) langka; setiap kelas dapat menambah satu.
2. Anotasi memaksa mahasiswa berhadapan dengan *construct validity* secara konkret: apa yang sebenarnya diukur label ini?
3. Benchmark baseline adalah pembanding wajib bagi Metopen/TA berikutnya di bidang NLP — *research assets should compound*.

## 3. Peran dalam research value chain

[ARC-02](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) menempatkan NLP sebagai **AI Core**. Kompetensi riset yang menjadi tanggung jawab MK ini:

- **Data creation & annotation**: guideline anotasi, pilot annotation, inter-annotator agreement, adjudication.
- **Benchmarking**: baseline sederhana (mis. lexicon/TF-IDF + linear) sebelum model besar; metrik yang tepat untuk tugas (F1 per kelas, exact match, BLEU/ROUGE bila relevan) dengan alasan.
- **Ethics & privacy teks**: consent, anonimisasi entitas, bias bahasa dan dialek.
- **Reproducibility**: korpus berversi, skrip evaluasi tetap, seed.

## 4. CPMK riset yang ditambahkan

Kerangka [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md).

| # | CPMK riset (tambahan) | Learning activity | Assessment | Research artifact | Evidence |
|---|---|---|---|---|---|
| R1 | Mahasiswa mampu merancang guideline anotasi yang dapat diikuti orang lain dan mengukur inter-annotator agreement | Studio anotasi (minggu 4–6) | Rubrik §6 (metrik: agreement dilaporkan) | Annotation guideline + laporan agreement | Nilai agreement (mis. Cohen's κ) + kasus ketidaksepakatan yang diadjudikasi |
| R2 | Mahasiswa mampu membangun korpus kecil dengan dokumentasi provenance, lisensi, privasi, dan pembagian split yang tidak bocor | Pengumpulan & kurasi (minggu 3–9) | Checklist dataset card | Korpus v0 + dataset card ([TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md)) | Kartu diverifikasi registry |
| R3 | Mahasiswa mampu menetapkan baseline dan metrik sebelum eksperimen dan menghasilkan benchmark yang dapat direproduksi | Studio benchmark (minggu 10–12) | Rubrik §6 (baseline, reproducibility) | Experiment Card ([TPL-09](../../../research-os/08-templates/09-experiment-card.md)) + benchmark script | Peer mereproduksi angka baseline |
| R4 | Mahasiswa mampu melaporkan error analysis linguistik dan mengungkap penggunaan AI (termasuk AI untuk pra-anotasi) | Sesi analisis (minggu 13–14) | Rubrik §6 (AI disclosure) | Error analysis + AI Usage Log ([TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md)) | Log memuat verifikasi pra-anotasi AI oleh manusia |

## 5. Project guide — proyek berorientasi riset

### 5.1 Bentuk proyek

| Aspek | Ketentuan |
|---|---|
| Tema | Satu tugas NLP pada teks berbahasa Indonesia/daerah dalam domain roadmap (mis. klasifikasi, NER, ekstraksi, QA sederhana, ringkasan). Sumber tema: [`research-backlog/BACKLOG.md`](../../../research-backlog/BACKLOG.md) (label `cluster:models`), kebutuhan riset dosen klaster C1, atau korpus yang sudah ada di [`datasets-registry/REGISTRY.md`](../../../datasets-registry/REGISTRY.md) yang perlu diperluas. |
| Tim | 3 mahasiswa (minimal 2 anotator independen + 1 adjudicator bergilir). |
| Ukuran korpus | Kecil tetapi jujur: cukup untuk agreement yang bermakna dan split train/dev/test (pengampu menetapkan angka minimum per tugas). |
| Data & etika | Teks publik atau dengan izin; entitas pribadi dianonimkan; tidak ada teks partner/rahasia di repo ([SECURITY.md](../../../SECURITY.md)); lisensi korpus diputuskan lewat review registry ([LICENSING.md](../../../LICENSING.md)). |
| Repositori | Dari [TPL-15](../../../research-os/08-templates/15-research-repository-template.md); korpus berversi di `data/` (atau di luar repo bila sensitif, dengan kartu di `data/README.md`). |
| AI | AI boleh dipakai untuk pra-anotasi/kandidat label **hanya** bila setiap label diverifikasi manusia dan dicatat; AI tidak menjadi anotator yang dihitung dalam agreement ([AIX-04](../../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)). |
| Endgame | Minimal: korpus + kartu terdaftar. Target: benchmark dipakai Metopen/TA berikutnya. Aspirasi: rilis dataset (`DS-`) + artefak evaluasi (`ART-`). |

### 5.2 Timeline satu semester (16 minggu, 5 milestone)

| Milestone | Minggu | Pertanyaan yang dijawab | Deliverable | Gate embrio |
|---|---|---|---|---|
| **M1 Tugas & Sumber** | 3 | Tugas NLP apa, untuk siapa, teks dari mana, boleh dipakai atau tidak? | Task brief 1 halaman, sumber teks + izin/lisensi, rencana anonimisasi, repo | G2, G5 (data plan) |
| **M2 Guideline & Pilot Anotasi** | 6 | Apakah label yang kita definisikan dapat disepakati orang lain? | **Annotation guideline v1**, pilot 50–100 item oleh 2 anotator, **agreement** + adjudication log, guideline v2 | G5 (construct) |
| **M3 Korpus v0** | 9 | Apakah korpus cukup, bersih, dan terdokumentasi? | Korpus v0 + split; **dataset card v0**; statistik korpus | G5 |
| **M4 Benchmark** | 12 | Berapa angka baseline dan satu pembanding, dengan skrip evaluasi tetap? | **Experiment Card**, baseline + 1 model, skrip evaluasi, ≥ 3 seed, **peer reproduction** | G6 |
| **M5 Analisis & Rilis** | 15–16 | Di mana model gagal secara linguistik; apa yang boleh diklaim; siapa yang melanjutkan? | Error analysis, Research One-Pager v0, dataset card final ke registry, AI Usage Statement, [handoff](../../../research-os/08-templates/14-research-handoff-template.md) | G7, handoff |

### 5.3 Hubungan ke backlog dan datasets-registry

- Korpus yang lolos verifikasi mendapat `DS-YYYY-NNN`; guideline anotasi disimpan bersama kartu sebagai bagian *quality*.
- Benchmark (skrip + angka baseline) dicatat pada kartu dataset sebagai *known baselines* agar riset berikutnya tidak mengulang.
- Tugas NLP yang menarik untuk riset lebih lanjut diajukan sebagai Issue *Research Problem* dengan *related courses: NLP* dan *potential dataset: DS-…*.

## 6. Rubrik ringkas research-quality

Research Integrity gate berlaku lulus/gagal. Rubrik lintas MK: [Assessment](../../assessment/README.md).

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality |
|---|---|---|---|---|
| **Baseline** | Langsung model besar tanpa pembanding | Baseline ada tetapi setelah hasil | Baseline sederhana ditetapkan sebelum eksperimen | Baseline + pembanding; angka baseline direproduksi peer; perbandingan ke hasil terdahulu (bila ada) dengan sumber terverifikasi |
| **Metrik & evaluasi (termasuk agreement)** | Metrik tidak sesuai tugas; agreement tidak dilaporkan | Metrik sesuai; agreement dilaporkan tanpa adjudikasi | Metrik per kelas; agreement + adjudication log; split tidak bocor (tidak ada dokumen sama lintas split) | Analisis per slice (panjang teks, dialek, domain); keterbatasan label dibahas; variansi antar seed |
| **Reproducibility** | Korpus/skrip tidak tersedia | Korpus ada, skrip evaluasi berubah-ubah | Korpus berversi, skrip evaluasi tetap, seed, README | Peer mereproduksi baseline; guideline dapat diikuti anotator baru dengan agreement serupa |
| **AI disclosure & integritas** | Pra-anotasi AI tidak diungkap | Diungkap tanpa verifikasi | Setiap label AI diverifikasi manusia dan dicatat | Log memuat tingkat koreksi terhadap AI; bias yang ditemukan dilaporkan; klaim dibatasi |

## 7. Template yang dipakai

| Kebutuhan | Template |
|---|---|
| Dataset card korpus | [TPL-05 Dataset Registry Template](../../../research-os/08-templates/05-dataset-registry-template.md) |
| Benchmark | [TPL-09 Experiment Card](../../../research-os/08-templates/09-experiment-card.md) |
| Repositori | [TPL-15 Research Repository Template](../../../research-os/08-templates/15-research-repository-template.md) |
| Log AI | [TPL-10 AI Usage Log](../../../research-os/08-templates/10-ai-usage-log-template.md) |
| Ringkasan | [TPL-01 Research One-Pager](../../../research-os/08-templates/01-research-one-pager-template.md) |
| Handoff | [TPL-14 Research Handoff](../../../research-os/08-templates/14-research-handoff-template.md) |
| Integritas | [TPL-11 Research Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md) |

Annotation guideline belum memiliki template di paket 08; pengampu dapat menaruh kerangka guideline di `templates/` folder ini.

## 8. Catatan RPS

`RPS.md` akan ditambahkan oleh pengampu; kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Bila bidang NLP diampu sebagai topik di dalam MK lain (mis. bagian AI/ML lanjutan), pengampu cukup mengambil milestone M2 dan M4 sebagai komponen proyek dan mencatat artefaknya di folder ini.

## 9. Pengampu

| Peran | Nama |
|---|---|
| Pengampu | [isi] |
| Dosen klaster C1 (Indonesian NLP) yang menjadi mitra kelas | [isi] |
