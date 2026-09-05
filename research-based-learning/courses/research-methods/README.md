# Metodologi Penelitian (Metopen) — Course Research Guide

**Status** Draft v0.1 (2026-09) · GitHub Phase 2 / GOV-02 Phase 1 (Pilot Metopen) — artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [Metopen Research Studio (View B mahasiswa)](../../../metopen-research-studio/README.md) · [MET-01 Positioning](../../../research-os/04-metopen-research-studio/01-metopen-positioning.md) · [MET-02 Course Outcomes](../../../research-os/04-metopen-research-studio/02-metopen-course-outcomes.md) · [MET-03 16-Week Blueprint](../../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [MET-04 Research Pack](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-06 5E Rubric](../../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [Final Project (TA)](../final-project/README.md)

## 1. Di mana desain Metopen berada

Folder ini **bukan** tempat desain Metopen. Desainnya sudah lengkap di dua tempat, dan halaman ini hanya menghubungkan keduanya ke pipeline mata kuliah:

| Kebutuhan | Tempat | Isi |
|---|---|---|
| Desain akademik (View A: dosen, tim kurikulum) | [`research-os/04-metopen-research-studio/`](../../../research-os/04-metopen-research-studio/01-metopen-positioning.md) | MET-01 positioning, MET-02 CPMK, MET-03 blueprint 16 minggu, MET-04 spesifikasi Research Pack, MET-05 publication backward design, MET-06 5E rubric, MET-07 integrity & ethics |
| Eksekusi mingguan (View B: mahasiswa) | [`metopen-research-studio/`](../../../metopen-research-studio/README.md) | `weeks/week-01-endgame.md` … `week-16-defense.md`, research-gates, templates, rubrics, examples, AI toolkit |
| Task & sprint | [`research-os/06-execution-os/`](../../../research-os/06-execution-os/03-research-gates.md) | OPS-01 WBS ±145 microtask, OPS-02 17 sprint (S0–S16), OPS-03 8 gate, OPS-04 critical path, OPS-05 Student Weekly Playbook |

Jangan menduplikasi blueprint ke sini. Bila ada yang perlu diubah pada minggu, gate, atau rubrik, ubah di sumbernya dan halaman ini cukup dirujuk ulang.

## 2. Identitas mata kuliah

| Field | Nilai |
|---|---|
| Nama formal | Metodologi Penelitian |
| Semester | VII |
| SKS | 2 |
| Positioning internal | AI-Augmented Research Methods & Evidence Engineering for Informatics ([MET-01](../../../research-os/04-metopen-research-studio/01-metopen-positioning.md)) |
| Bentuk | Research Studio: ±30% concepts + 70% studio |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **R — Research-Producing** |
| Tahap ([ARC-04](../../../research-os/02-academic-architecture/04-build-prove-contribute.md)) | **PROVE** — evidence-quality gate seluruh pipeline |
| Tahun spiral ([ARC-01](../../../research-os/02-academic-architecture/01-research-capability-spiral.md)) | Year 4 — Prove & Contribute |
| Entry door yang diterima | Semua enam: Problem, Dataset, Faculty Research, Course Project (diutamakan), Partner, Competition |
| Klaster | Semua (C1–C4); tim memilih satu klaster utama di G2 |
| Field **Course** di Mission Control | `Metopen` |
| Pengampu / koordinator | [isi] |

*Semester dan SKS dari tabel kurikulum dokumen diskusi; verifikasi sebelum dokumen formal.*

## 3. Mengapa mode R dan mengapa "Prove"

Metopen adalah satu-satunya mata kuliah yang **memproduksi Research Pack** — deliverable yang secara definisi adalah research asset: Problem Brief, Literature Evidence Map, RQ, Research Design, Data Plan, Baseline & Metrics, Pilot Experiment, Threats to Validity, Ethics, AI Usage Statement, Reproducibility README, Proposal TA, Research Pitch ([MET-04](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md)).

Ia disebut **Prove** karena tugasnya bukan membangun sesuatu yang baru (itu sudah dilakukan MK teknis), melainkan **membuktikan bahwa bukti yang ada cukup** untuk mendukung klaim: baseline sudah ada? metrik selaras RQ? pilot berjalan? orang lain bisa mereproduksi? Apa yang bisa membatalkan kesimpulan? Delapan gate G1–G8 ([OPS-03](../../../research-os/06-execution-os/03-research-gates.md)) adalah operasionalisasi "prove" itu.

## 4. Peran dalam research value chain

Menurut [ARC-02](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) dan [MET-01 §2](../../../research-os/04-metopen-research-studio/01-metopen-positioning.md), Metopen adalah **integration layer** enam semester dan **launchpad TA**. Dalam pipeline komponen ini:

- **Masuk (W1–W2):** inventarisasi artefak Build — Experiment Card & repo dari [AI/ML](../ai-ml/README.md), dataset card dari [Data Mining](../data-mining/README.md)/Basis Data, korpus dari [NLP](../nlp/README.md), software dari [RPL](../software-engineering/README.md), problem brief dari Kerja Praktik. Tim yang membawa handoff [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) mewarisi gate embrio yang sudah dilatih.
- **Keluar (W16):** Research Pack v1.0 + Proposal TA + handoff G8 ke [TA](../final-project/README.md); artefak terdaftar (`UIAI-`, `DS-` bila ada); Mission Control diperbarui.

## 5. CPMK riset

CPMK lengkap ada di [MET-02](../../../research-os/04-metopen-research-studio/02-metopen-course-outcomes.md). Untuk keperluan pemetaan lintas MK ([ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md)), empat CPMK payung yang dipakai komponen ini:

| # | CPMK payung | Gate yang membuktikan | Artefak Research Pack | Kriteria 5E |
|---|---|---|---|---|
| M1 | Mahasiswa mampu mengubah masalah nyata menjadi RQ yang selaras dengan bukti literatur (Gap–Claim–Evidence alignment) | G2, G3, G4 | Problem Brief, Literature Evidence Map, Research Gap, RQ/Hypothesis, Contribution Statement | End, Evidence |
| M2 | Mahasiswa mampu merancang metode, data, baseline, metrik, dan threats to validity yang dapat dijalankan orang lain | G5 | Research Design, Dataset/Data Plan, Baseline & Metrics, Threats to Validity, Ethics & Privacy | Experiment |
| M3 | Mahasiswa mampu menjalankan pilot experiment yang reproducible dan menganalisis hasil dengan klaim yang tidak melebihi bukti | G6, G7 | Pilot Experiment, Reproducibility README, analisis CER | Experiment, Explanation |
| M4 | Mahasiswa mampu mempertanggungjawabkan riset secara tertulis dan lisan, jujur tentang penggunaan AI dan integritas (amanah epistemik) | G8 + Integrity gate | Proposal TA, Research Pitch, AI Usage Statement, Research Integrity Checklist | Explanation, Execution |

## 6. Project guide — studio satu semester

Proyek Metopen **adalah** mata kuliahnya: satu *mini research cycle* per tim, 16 minggu, delapan gate. Rincian mingguan ada di [MET-03](../../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) dan halaman [Week 01–16](../../../metopen-research-studio/README.md). Ringkasannya sebagai lima milestone yang selaras dengan release ([OPS-03](../../../research-os/06-execution-os/03-research-gates.md), tabel peta gate):

| Milestone | Minggu (sprint) | Gate | Release | Deliverable inti |
|---|---|---|---|---|
| **M1 Endgame & Problem** | W1–W2 (S1–S2) | G1, G2 | v0.1 Problem Validated | Tim + repo dari [TPL-15](../../../research-os/08-templates/15-research-repository-template.md), `docs/endgame.md`, Problem Brief, One-Pager v0, Research ID `UIAI-YYYY-NNN` |
| **M2 Evidence & Question** | W3–W6 (S3–S6) | G3, G4 | v0.2 Evidence Ready | Synthesis matrix 15–25 sumber terverifikasi, `references.bib`, Research Gap, RQ, Contribution Statement |
| **M3 Method & Design Defense** | W7–W8 (S7–S8) | G5 | v0.3 Research Design | Research Design Card, Data Plan, Baseline & Metrics, Experiment Card, threats awal, ethics; **Mid-semester Research Pitch / Red Team Review** |
| **M4 Repository, Pilot & Analysis** | W9–W12 (S9–S12) | G6, G7 | v0.5 Pilot Experiment | Repo reproducible, pilot end-to-end, peer reproduction, `results/analysis.md`, CER per RQ, threats diperbarui |
| **M5 Manuscript, Review & Defense** | W13–W16 (S13–S16) | G8 | v0.8 Manuscript Draft → v1.0 Research Pack | Proposal TA/manuscript, peer review sebagai reviewer, revisi, Research Defense 7–10 menit, Integrity Checklist, handoff ke TA |

| Aspek | Ketentuan |
|---|---|
| Tim | 1–3 mahasiswa (G1) |
| Tema | Dari backlog/registry/artefak MK sebelumnya/riset dosen/partner/lomba — *multiple entry points, one pipeline* |
| Hubungan ke backlog & registry | Research ID diberikan saat lolos G2 ([GOVERNANCE.md §5](../../../GOVERNANCE.md)); dataset baru didaftarkan sebelum G5; Issue backlog menjadi rekam jejak riset |
| Ritme | Sprint mingguan 7–10 task ([OPS-02](../../../research-os/06-execution-os/02-weekly-sprints.md)); review gate lewat PR `GATE REVIEW: <gate>` ([CONTRIBUTING.md](../../../CONTRIBUTING.md)) |
| Endgame minimum | **TA Ready** (lolos G5) untuk 100% mahasiswa; target **Research Ready** (G6–G7); aspirasi **Publication Ready** |

## 7. Rubrik

Standar penilaian Metopen adalah **5E Rubric** ([MET-06](../../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)): End, Evidence, Experiment, Explanation, Execution — ditambah **Research Integrity gate** lulus/gagal. Bobot dan deskriptor level ada di MET-06; asesmen lintas MK di [Assessment](../../assessment/README.md).

Untuk konsistensi dengan MK teknis, empat kriteria research-quality di bawah adalah **irisan** 5E yang juga dipakai MK mode E/R (versi ringkas; 5E yang berlaku untuk nilai akhir):

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality | Bagian 5E |
|---|---|---|---|---|---|
| **Baseline** | Tidak ada | Ada setelah hasil | Ditetapkan di G5 sebelum pilot | Baseline + pembanding; direproduksi peer di G6 | Experiment |
| **Metrik & evaluasi** | Tidak selaras RQ | Selaras tetapi leakage tidak diperiksa | Selaras RQ, prosedur mencegah leakage | Ketidakpastian (seed/fold/interval) dan signifikansi praktis dibahas di G7 | Experiment, Explanation |
| **Reproducibility** | Hasil di laptop | Kode tanpa environment/seed | Repo TPL-15 lengkap; tim menjalankan ulang | Peer mereproduksi angka baseline; Reproducibility README di Pack | Execution |
| **AI disclosure & integritas** | Tidak ada log | Log tanpa verifikasi | Log lengkap; AI Usage Statement | Protokol AIX-04 terlihat di log; sumber dari AI semua terverifikasi; Integrity Checklist lulus | Semua (gate) |

## 8. Template yang dipakai

Metopen memakai **seluruh** paket 08. Urutan pemakaian per gate:

| Gate | Template |
|---|---|
| G1 | [TPL-15 Repository](../../../research-os/08-templates/15-research-repository-template.md), [TPL-10 AI Usage Log](../../../research-os/08-templates/10-ai-usage-log-template.md) |
| G2 | [TPL-01 One-Pager](../../../research-os/08-templates/01-research-one-pager-template.md), [TPL-04 Backlog](../../../research-os/08-templates/04-research-backlog-template.md) |
| G3–G4 | synthesis matrix (bagian [MET-04](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md)), [TPL-06 Venue Registry](../../../research-os/08-templates/06-publication-venue-registry-template.md) (backward design) |
| G5 | [TPL-08 Research Design Card](../../../research-os/08-templates/08-research-design-card.md), [TPL-09 Experiment Card](../../../research-os/08-templates/09-experiment-card.md), [TPL-05 Dataset Registry](../../../research-os/08-templates/05-dataset-registry-template.md) |
| G6–G7 | struktur `experiments/`, `results/` dari TPL-15 |
| G8 | [TPL-12 Peer Review](../../../research-os/08-templates/12-peer-review-template.md), [TPL-13 Research Defense](../../../research-os/08-templates/13-research-defense-template.md), [TPL-11 Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md), [TPL-14 Handoff](../../../research-os/08-templates/14-research-handoff-template.md) |
| Pemantauan dosen | [TPL-02 Mission Tracker](../../../research-os/08-templates/02-research-mission-tracker-template.md), [TPL-03 Leaderboard](../../../research-os/08-templates/03-research-leaderboard-template.md) |

## 9. Catatan RPS

`RPS.md` akan ditambahkan oleh pengampu; kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Bahan RPS diambil langsung dari MET-02 (CPMK), MET-03 (pertemuan mingguan), MET-04 (deliverable), MET-06 (penilaian), MET-07 (integritas) — *dikompilasi, bukan ditulis ulang* (lihat "Artefak turunan" di [research-os/README](../../../research-os/README.md)).

## 10. Pengampu

| Peran | Nama |
|---|---|
| Pengampu / koordinator Metopen | [isi] |
| Mentor riset per klaster (C1–C4) | [isi] |
| Red team reviewer W8 (dosen lain) | [isi] |
