# Data Mining — Course Research Guide

**Status** Draft v0.1 (2026-09) · GitHub Phase 3 Curriculum Integration (GOV-02 Phase 3 Expand technical courses) — artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [ARC-01 Capability Spiral](../../../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-02 Curriculum Research Map](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-05 CPL–CPMK–Artifact](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [AI/ML](../ai-ml/README.md) · [Assessment](../../assessment/README.md)

## 1. Identitas mata kuliah

| Field | Nilai |
|---|---|
| Nama | Data Mining |
| Semester | IV |
| SKS | [isi] |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **R — Research-Producing** (boleh dijalankan sebagai E pada semester pertama integrasi) |
| Tahun spiral ([ARC-01](../../../research-os/02-academic-architecture/01-research-capability-spiral.md)) | Year 2 — Build & Compare |
| Entry door yang dibuka | **Dataset** |
| Klaster utama | C1 AI Models, Data & Knowledge (data-centric AI) |
| Klaster sekunder | C4 Applied AI (bila dataset berdomain: pendidikan, halal, kesehatan, dst.) |
| Field **Course** di Mission Control | `Data Mining` |
| Pengampu | [isi] |

*Semester dari tabel kurikulum dokumen diskusi; SKS tidak disebut di sana. Verifikasi sebelum dokumen formal.*

## 2. Mengapa mode R

Data Mining adalah mata kuliah pertama tempat mahasiswa memegang **dataset nyata secara utuh**: membersihkan, memisahkan, memodelkan, dan mengukur. Di titik inilah kebiasaan paling merusak riset lahir atau dicegah: leakage, metrik tanpa baseline, dan "accuracy 93%" tanpa error analysis. Karena itu asset yang diminta dari MK ini bukan model, melainkan **pengetahuan tentang dataset**: *evidence map dataset* dan *error analysis* yang dapat dipakai ulang oleh AI/ML, NLP, Metopen, dan riset dosen.

Mode R dipilih karena artefaknya (dataset card, evidence map dataset, laporan leakage) langsung menjadi entri `datasets-registry/` — research memory yang paling murah dan paling sering dipakai ulang. Bila kelas belum siap, pengampu boleh menjalankannya sebagai mode E satu semester dengan artefak wajib dikurangi menjadi dataset card + laporan baseline.

## 3. Peran dalam research value chain

[ARC-02](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) menempatkan Data Mining pada **data infrastructure → evaluation & leakage awareness**. Kompetensi Year 2 yang menjadi tanggung jawab MK ini (ARC-01 §4):

- **Baseline thinking**: setiap model dibandingkan dengan pembanding paling sederhana (majority class, rata-rata, aturan tunggal).
- **Pengukuran yang benar**: train/test split, cross-validation, prosedur yang dapat diulang.
- **Data infrastructure**: kualitas data, provenance, dataset card.
- **Evaluation & leakage awareness**: mengenali dan mencegah kebocoran informasi dari data uji.

Yang tidak diminta: hipotesis riset formal atau literature map. Cukup satu pertanyaan analitis per proyek dan kejujuran tentang apa yang ditunjukkan data.

## 4. CPMK riset yang ditambahkan

Kerangka [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md).

| # | CPMK riset (tambahan) | Learning activity | Assessment | Research artifact | Evidence |
|---|---|---|---|---|---|
| R1 | Mahasiswa mampu mendokumentasikan provenance, kualitas, lisensi, dan privasi sebuah dataset dalam dataset card | Studio dataset card (minggu 3–4) | Checklist dataset card | Dataset card v0 ([TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md)) | Kartu terverifikasi pengelola registry |
| R2 | Mahasiswa mampu menyusun *evidence map dataset*: apa yang diketahui tentang dataset ini (sumber, hasil terdahulu, bias, batasan) dan risiko leakage-nya | Audit data (minggu 5–7) | Rubrik §6 (metrik & evaluasi) | Evidence map dataset (`docs/dataset-evidence-map.md`) | Tabel bukti + daftar risiko leakage dengan mitigasi |
| R3 | Mahasiswa mampu menjalankan baseline dan satu metode pembanding dengan prosedur evaluasi yang benar dan dapat diulang | Eksperimen (minggu 8–10) | Rubrik §6 (baseline, reproducibility) | Laporan eksperimen + notebook | Angka baseline direproduksi peer |
| R4 | Mahasiswa mampu melakukan error analysis dan menyatakan klaim yang tidak melebihi bukti, dengan pengungkapan penggunaan AI | Sesi error analysis (minggu 11–13) | Rubrik §6 (AI disclosure); laporan | Error analysis report + AI Usage Log ([TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md)) | Kasus gagal dikelompokkan; klaim dibatasi |

## 5. Project guide — proyek berorientasi riset

### 5.1 Bentuk proyek

| Aspek | Ketentuan |
|---|---|
| Tema | **Satu dataset, satu pertanyaan analitis.** Dataset dari [`datasets-registry/REGISTRY.md`](../../../datasets-registry/REGISTRY.md), dataset publik berlisensi jelas, atau data terbuka domain Indonesia. Pertanyaan ditulis dalam bentuk "apakah X dapat diprediksi/dikelompokkan dari Y, dan seberapa jauh dibanding baseline?" |
| Tim | 2–3 mahasiswa; setiap anggota bertanggung jawab atas satu bagian dataset card. |
| Data | Tidak ada data pribadi mentah; data yang mengandung identitas harus dianonimkan sebelum masuk repo ([SECURITY.md](../../../SECURITY.md)). |
| Repositori | Repo kelas per tim dengan struktur minimum `data/README.md`, `notebooks/`, `results/`, `docs/`; boleh memakai [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) penuh bila tim berniat lanjut. |
| AI | AI boleh membantu EDA, kode, dan penjelasan metrik; setiap kode bantuan AI diuji; log di AI Usage Log ([AIX-04](../../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)). |
| Endgame yang diminta | Minimal: dataset card terdaftar. Target: evidence map dataset dipakai kelas AI/ML atau NLP semester berikutnya. |

### 5.2 Timeline satu semester (16 minggu, 5 milestone)

| Milestone | Minggu | Pertanyaan yang dijawab | Deliverable | Gate embrio |
|---|---|---|---|---|
| **M1 Dataset & Pertanyaan** | 4 | Dataset apa, dari mana, boleh dipakai untuk apa, pertanyaan analitis apa? | **Dataset card v0**, pertanyaan analitis 1 paragraf, repo tim | G2 (awal), G5 (data plan) |
| **M2 Audit Data** | 7 | Apa yang sudah diketahui tentang dataset ini; di mana bias dan risiko leakage-nya? | **Evidence map dataset** (provenance, hasil terdahulu bila ada, distribusi, missing, duplikasi, fitur bocor), rencana split | G3 (versi data), G5 |
| **M3 Baseline** | 10 | Berapa angka pembanding paling sederhana, dengan prosedur apa? | Baseline + 1 metode pembanding, cross-validation/split yang benar, tabel hasil di `results/` | G6 |
| **M4 Error Analysis** | 13 | Di mana model gagal dan mengapa; apa yang tidak boleh disimpulkan? | **Error analysis report**, threats awal (representativitas, leakage), **peer reproduction** angka baseline | G6, G7 |
| **M5 Registry & Handoff** | 15–16 | Apa yang bisa dipakai ulang orang lain? | Dataset card final ke registry, ringkasan 1 halaman, AI Usage Statement, [handoff](../../../research-os/08-templates/14-research-handoff-template.md) bila lanjut | Handoff |

### 5.3 Hubungan ke backlog dan datasets-registry

- Prioritas *reuse before create*: kelas mulai dari dataset yang sudah ada di registry dan **memperkaya kartunya** (menambah evidence map, risiko leakage, baseline yang direproduksi). Ini kontribusi riil sekalipun datasetnya lama.
- Dataset baru yang lolos verifikasi mendapat `DS-YYYY-NNN`. Evidence map dataset dilampirkan pada kartu sebagai bagian *possible research questions* dan *known limitations*.
- Pertanyaan analitis yang ternyata menarik diajukan sebagai Issue *Research Problem* ke [`research-backlog/`](../../../research-backlog/README.md) dengan label `cluster:models`/`cluster:applied` dan catatan *related courses: Data Mining*.

## 6. Rubrik ringkas research-quality

Research Integrity gate (lulus/gagal) berlaku di atas rubrik. Rubrik lintas MK dan kalibrasi: [Assessment](../../assessment/README.md).

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality |
|---|---|---|---|---|
| **Baseline** | Tidak ada pembanding | Baseline ada tetapi ditetapkan setelah melihat hasil | Baseline sederhana ditetapkan sebelum eksperimen; alasan ditulis | Baseline + pembanding; hasil baseline direproduksi peer; perbedaan dibahas secara praktis |
| **Metrik & evaluasi (termasuk leakage)** | Split tidak dijelaskan; metrik tunggal tanpa alasan | Split ada; leakage tidak diperiksa | Split/CV benar; leakage diperiksa dan dicatat; metrik selaras pertanyaan | Evidence map dataset memuat risiko leakage + mitigasi; variansi antar fold; metrik pelengkap bila kelas tidak seimbang |
| **Reproducibility** | Notebook tidak berjalan ulang | Berjalan di laptop tim dengan intervensi manual | README, environment, seed; tim sendiri menjalankan ulang | Peer mereproduksi baseline tanpa bertanya |
| **AI disclosure & integritas** | Tidak ada log | Log tidak lengkap | Log lengkap; kode AI diuji | Log memuat verifikasi; keterbatasan dataset dinyatakan jujur; klaim tidak melebihi bukti |

## 7. Template yang dipakai

| Kebutuhan | Template |
|---|---|
| Dataset card | [TPL-05 Dataset Registry Template](../../../research-os/08-templates/05-dataset-registry-template.md) |
| Log AI | [TPL-10 AI Usage Log](../../../research-os/08-templates/10-ai-usage-log-template.md) |
| Repositori (opsional penuh) | [TPL-15 Research Repository Template](../../../research-os/08-templates/15-research-repository-template.md) |
| Eksperimen (opsional, tim yang lanjut) | [TPL-09 Experiment Card](../../../research-os/08-templates/09-experiment-card.md) |
| Ringkasan (opsional) | [TPL-01 Research One-Pager](../../../research-os/08-templates/01-research-one-pager-template.md) |
| Handoff | [TPL-14 Research Handoff](../../../research-os/08-templates/14-research-handoff-template.md) |
| Integritas | [TPL-11 Research Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md) |

## 8. Catatan RPS

`RPS.md` akan ditambahkan oleh pengampu; kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Perubahan minimum pada RPS: satu proyek dataset menggantikan tugas-tugas kecil terpisah (*one activity, multiple outcomes*), CPMK R1–R4 ditambahkan, milestone §5.2 menjadi komponen penilaian proyek.

## 9. Pengampu

| Peran | Nama |
|---|---|
| Pengampu | [isi] |
| Pengelola datasets-registry yang menjadi mitra kelas | [isi] |
