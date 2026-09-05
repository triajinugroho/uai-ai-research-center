# Metodologi Penelitian — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · GitHub Phase 2 / GOV-02 Phase 1 (Pilot Metopen) — artefak riil menyusul
**Terkait** [README Metopen](README.md) · [MET-04 Research Pack Specification](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [GOVERNANCE.md](../../../GOVERNANCE.md) · [Final Project (TA)](../final-project/research-artifact.md)

Asset Metopen adalah **UAI Informatics Research Pack** — spesifikasi lengkap di [MET-04](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md). Tabel di bawah tidak mengulang spesifikasi; ia menetapkan **status wajib/opsional, lokasi, ID, tujuan penyerahan, dan gate** setiap komponen agar konsisten dengan MK lain di komponen ini.

## 1. Tabel artefak

| Artefak (komponen Research Pack) | Wajib / Opsional | Format & lokasi (repo `proj-YYYY-topik`) | Template | ID yang diberikan | Kriteria kualitas (ringkas; detail di MET-04/OPS-03) | Diserahkan ke | Gate |
|---|---|---|---|---|---|---|---|
| **Endgame statement** | Wajib | `docs/endgame.md` | bagian TPL-01 | — | Endgame spesifik (TA Ready / Research Ready / aspirasi), entry door, kandidat mentor | Repo; Mission Control | G1 |
| **Problem Brief + Stakeholder/Impact Statement** | Wajib | `docs/problem.md` | [TPL-01](../../../research-os/08-templates/01-research-one-pager-template.md) (v0) | **`UIAI-YYYY-NNN`** resmi saat lolos G2 | Problem-first; orang luar bisa mengulang masalah dalam dua kalimat; klaster & domain dipilih | `research-backlog/` (Issue diperbarui); Mission Control | G2 |
| **Literature Evidence Map + synthesis matrix + `references.bib`** | Wajib | `docs/literature-map.md`, `docs/literature/synthesis-matrix.csv` (+ `search-strategy.md`, `verification.md` di `docs/literature/`), `references.bib` | bagian MET-04 | — | 15–25 sumber primer dibaca & terverifikasi (DOI/URL); pola konsisten/bertentangan/kosong terlihat | Repo | G3 |
| **Research Gap, RQ/Hypothesis, Contribution Statement** | Wajib | `docs/research-question.md`; One-Pager v1 | [TPL-01](../../../research-os/08-templates/01-research-one-pager-template.md) | — | Setiap RQ dapat ditelusuri ke baris synthesis matrix | Repo; Issue `type:research-question` | G4 |
| **Research Design Card** | Wajib | `docs/research-design.md` + `docs/design-card.md` | [TPL-08](../../../research-os/08-templates/08-research-design-card.md) | — | Jenis metode dari Computing Research Methods Map; variabel, kontrol, sampling; orang lain bisa menjalankan tanpa bertanya | Repo | G5 |
| **Dataset/Data Plan (+ dataset card bila data baru)** | Wajib | `docs/data-plan.md`; `data/README.md`; kartu ke `datasets-registry/` | [TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md) | `DS-YYYY-NNN` bila dataset baru | Sumber, akses, lisensi, privasi diisi sebelum G5 ([SECURITY.md](../../../SECURITY.md)) | `datasets-registry/` | G5 |
| **Baseline & Metrics + Experiment Card** | Wajib | `docs/research-design.md` §Baseline & Metrics; `experiments/pilot-01/experiment-card.md` | [TPL-09](../../../research-os/08-templates/09-experiment-card.md) | — | Baseline sederhana, metrik selaras RQ, prosedur mencegah leakage; ditetapkan sebelum pilot | Repo | G5 |
| **Threats to Validity (awal → diperbarui)** | Wajib | v1 di `docs/research-design.md` §Threats (G5) → v2 di `results/analysis.md` §Threats (G7) | — | — | Internal, eksternal, konstruk, statistik; diperbarui setelah pilot | Repo | G5, G7 |
| **Ethics & Privacy** | Wajib | `docs/ethics.md` | [MET-07](../../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) | — | Consent, anonimisasi, bias, batas penggunaan AI | Repo | G5 |
| **Design Defense (pitch + notulen red team)** | Wajib | `presentation/w08-pitch.pdf`, `docs/red-team-notes.md` | [TPL-13](../../../research-os/08-templates/13-research-defense-template.md) (versi mid) | — | Kritik red team dicatat dan dijawab | Repo | G5 |
| **Pilot Experiment + Reproducibility package** | Wajib | `src/`, `notebooks/`, `experiments/` (+README), `results/`, `figures/`, environment, seed | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) | — | Pilot end-to-end (baseline + ≥ 1 pembanding); peer mereproduksi angka baseline | Repo; release v0.5 | G6 |
| **Analysis + Claim–Evidence–Reasoning** | Wajib | `results/analysis.md`, figur final | — | — | Setiap klaim menunjuk tabel/figur; hasil negatif dilaporkan; tidak ada klaim kausal dari korelasi | Repo | G7 |
| **AI Usage Log + AI Usage Statement** | Wajib | `AI-USAGE.md` | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | Semua penggunaan AI yang memengaruhi kesimpulan tercatat & terverifikasi | Repo; lampiran Pack | Setiap gate (integrity) |
| **Proposal TA (atau manuscript bila endgame paper)** | Wajib | `paper/proposal-ta.md` / `paper/manuscript.md` | struktur MET-04; [MET-05](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md) untuk paper | `PUB-YYYY-NNN` bila naskah didaftarkan di `publications/` | Lolos peer review [TPL-12](../../../research-os/08-templates/12-peer-review-template.md) + revisi | Pembimbing TA; `publications/` bila paper | G8 |
| **Research Pitch / Defense** | Wajib | `presentation/defense.pdf` + rekaman/notulen | [TPL-13](../../../research-os/08-templates/13-research-defense-template.md) | — | 7–10 menit; lulus penguji | Repo | G8 |
| **Research Integrity Checklist** | Wajib | `docs/integrity-checklist.md` ditandatangani | [TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md) | — | Semua butir lulus | Repo; pengampu | G8 (gate lulus/gagal) |
| **Handoff ke TA / mentor / AI Center** | Wajib | `docs/handoff.md` | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | What exists, missing evidence, next steps, owner (calon pembimbing) | [TA](../final-project/README.md); Mission Control (Course = `Metopen` → `TA`) | G8 |
| **Release `v1.0 Research Pack`** | Wajib | GitHub Release | — | — | Semua komponen di atas ada; tidak ada yang kosong | Mission Control (Maturity ≥ TA Ready) | G8 |
| **Peer review yang ditulis mahasiswa (sebagai reviewer)** | Wajib (bagian Execution) | PR review pada repo tim lain (W14) | [TPL-12](../../../research-os/08-templates/12-peer-review-template.md) | — | Menilai problem, evidence, RQ, method, results, claim, limitations; konstruktif | Repo tim yang direview | G8 |
| **Artefak / model / benchmark** | Opsional | sesuai [ARC-06](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) | — | `ART-YYYY-NNN` bila dirilis | Release review; lisensi; IP review bila perlu | `publications/` | Release review |

## 2. Definition of done (akhir semester)

Sama dengan *definition of done* G8 di [OPS-03](../../../research-os/06-execution-os/03-research-gates.md): Research Pack lengkap, peer review lulus, defense lulus, Integrity Checklist ditandatangani, handoff terisi, release v1.0 dibuat. Ditambah, untuk komponen ini:

- [ ] Mission Control: field Course `Metopen`, Maturity minimal **TA Ready**, Next Evidence terisi untuk TA.
- [ ] Bila dataset baru: `DS-` terdaftar. Bila naskah: `PUB-` terdaftar dengan status `manuscript-ready`.
- [ ] Artefak Build yang dipakai (dari AI/ML, Data Mining, NLP, RPL) dirujuk di README riset sebagai *provenance*.

## 3. Tingkat kematangan keluaran

| Keluaran Metopen | Gate lulus | Maturity | Yang diterima TA |
|---|---|---|---|
| Minimum | G5 | **TA Ready** | Proposal dengan desain, data plan, baseline & metrik; pilot belum tentu ada |
| Target | G6–G7 | **Research Ready** | Pilot berjalan & direproduksi; analisis awal; TA langsung memperluas eksperimen |
| Aspirasi | G8 + manuscript-ready | **Publication Ready** | Manuscript draft; TA menjadi eksperimen penuh + submission ([MET-05](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md)) |

## 4. Ke mana artefak mengalir

```
Metopen (sem. VII)
├─ Research Pack v1.0 + Proposal TA + handoff ─► TA (sem. VIII): mulai dari G6, bukan dari nol
├─ Research ID UIAI-YYYY-NNN ──────────────────► research-backlog/ (Issue divalidasi), Mission Control
├─ dataset card ───────────────────────────────► datasets-registry/ (DS-)
├─ manuscript (bila endgame paper) ────────────► publications/ (PUB-, status manuscript-ready)
└─ Research Pack yang tidak dilanjutkan mahasiswa ─► AI Center / riset dosen lewat handoff (what exists, missing evidence)
```
