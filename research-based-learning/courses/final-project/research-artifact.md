# Tugas Akhir — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · Mengikuti angkatan pertama Metopen Studio — artefak riil menyusul
**Terkait** [README TA](README.md) · [Metopen research-artifact](../research-methods/research-artifact.md) · [MET-04 Research Pack](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-05 Publication Backward Design](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md) · [ARC-06 Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [publications](../../../publications/README.md)

Asset TA adalah **Research Pack lengkap + manuscript + artefak/ART + handoff ke AI Center**. Komponen Pack yang sudah lolos gate di Metopen **diperbarui**, bukan dibuat ulang. Path bertanda † (`docs/ta-plan.md`, `paper/laporan-ta.*`, `paper/manuscript.*`, `docs/venue.md`) adalah perluasan fase TA di luar struktur minimum [TPL-15](../../../research-os/08-templates/15-research-repository-template.md): laporan TA dan manuscript adalah kelanjutan `paper/proposal.md` Metopen; venue boleh dicatat di `paper/outline.md` §Venue.

## 1. Tabel artefak

| Artefak | Wajib / Opsional | Format & lokasi (repo `proj-YYYY-topik`) | Template | ID yang diberikan | Kriteria kualitas | Diserahkan ke | Gate |
|---|---|---|---|---|---|---|---|
| **Rencana TA dari handoff** | Wajib | `docs/ta-plan.md`†: missing evidence → task; jadwal; Experiment Card diperbarui | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) (masukan), [TPL-09](../../../research-os/08-templates/09-experiment-card.md) | mewarisi `UIAI-YYYY-NNN` | Setiap *missing evidence* Metopen punya task dan minggu target | Pembimbing; Mission Control (Course = `TA`) | Intake |
| **Research Pack lengkap (v1.0 TA)** | Wajib | Semua komponen [MET-04](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md) diperbarui di `docs/`, `data/`, `results/`, `paper/` | paket 08 | — | Tidak ada komponen kosong; literature map ≤ 6 bulan; threats final; AI Usage Statement final | Repo; release `v1.0` | G8 |
| **Eksperimen penuh + reproducibility package** | Wajib | `src/`, `experiments/` (+README, konfigurasi, seed), `results/`, `figures/`, environment; data penuh atau kartu ke lokasi eksternal | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) | — | Semua kondisi desain dijalankan; ≥ 3 seed/fold; pembimbing/peer mereproduksi baseline dan hasil utama | Repo; PR `GATE REVIEW: Experiment Ready` | G6 |
| **Analisis + CER + threats final** | Wajib | `results/analysis.md`, tabel CER per RQ, figur final | — | — | Klaim menunjuk tabel/figur; ketidakpastian & signifikansi praktis; hasil negatif dilaporkan; tidak ada klaim kausal dari korelasi | Repo; PR `GATE REVIEW: Claim Ready` | G7 |
| **Laporan TA** | Wajib | `paper/laporan-ta.*`† sesuai format Prodi + lampiran (reproducibility README, AI Usage Statement, Integrity Checklist) | format Prodi; struktur bab mengikuti Research Pack | — | Lulus sidang; konsisten dengan repo (angka di laporan = angka di `results/`) | Prodi; repo | G8 |
| **Manuscript** | Opsional (wajib bila endgame Publication Ready) | `paper/manuscript.*`† sesuai template venue; `docs/venue.md`† | [MET-05](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md), [TPL-06](../../../research-os/08-templates/06-publication-venue-registry-template.md), [TPL-12](../../../research-os/08-templates/12-peer-review-template.md) | `PUB-YYYY-NNN` (pengelola publications) | Lolos peer review internal (PR `manuscript-review.md`); venue beretika; status `manuscript-ready` → `submission-ready` | `publications/` | G8; PR manuscript review |
| **Dataset (rilis)** | Opsional | Kartu di `datasets-registry/datasets/`; data di lokasi sesuai review privasi/lisensi | [TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md) | `DS-YYYY-NNN` (bila belum ada) | Lisensi diputuskan lewat review ([LICENSING.md](../../../LICENSING.md)); tidak ada data sensitif mentah | `datasets-registry/` | G8; review registry |
| **Artefak: software / model / benchmark / prototype** | Opsional (wajib bila endgame Impact Ready) | Release berversi + artifact README + `CITATION.cff` + lisensi; model weights di luar GitHub dengan kartu model | PR `release-review.md`; kerangka artifact README ([RPL](../software-engineering/research-artifact.md)) | `ART-YYYY-NNN` (pengelola publications/AI Center) | Documented, complete, executable/reusable; IP review bila berpotensi HKI | `publications/` (artefak); unit HKI bila perlu | Release review |
| **Sidang TA sebagai Research Defense** | Wajib | `presentation/defense-final.pdf` (diperbarui untuk sidang TA) + notulen di `docs/reviews/defense-minutes.md` | [TPL-13](../../../research-os/08-templates/13-research-defense-template.md) | — | Problem, evidence, method, results, claim, limitations, integritas dipertahankan | Prodi; repo | G8 |
| **Research Integrity Checklist (final)** | Wajib | `docs/integrity-checklist.md` ditandatangani mahasiswa + pembimbing | [TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md) | — | Semua butir lulus; sitasi 100% terverifikasi; AI disclosure lengkap | Pembimbing; koordinator TA | G8 (lulus/gagal) |
| **AI Usage Log (kumulatif sejak Metopen)** | Wajib | `docs/AI-USAGE.md` (kumulatif) + `paper/AI-USAGE-STATEMENT.md` | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | Kontinu Metopen → TA; setiap penggunaan yang memengaruhi kesimpulan terverifikasi | Repo; lampiran laporan | Setiap gate |
| **Handoff ke AI Research Center** | Wajib | `docs/handoff.md` (versi akhir): what exists, missing evidence, next steps, owner berikutnya | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | Pertanyaan lanjutan tercatat sebagai Issue baru; owner berikutnya disebut (dosen klaster/mahasiswa/partner) | AI Center (dosen klaster); Mission Control (Maturity diperbarui) | Setelah sidang |
| **Issue lanjutan (Research Problem / Literature Gap)** | Opsional (disarankan) | Issue `type:problem` / `type:literature-gap` merujuk `UIAI-YYYY-NNN` induk | Form `.github/ISSUE_TEMPLATE/` | `UIAI-YYYY-NNN` baru saat divalidasi | Berangkat dari *missing evidence*/threats yang belum terjawab | `research-backlog/` | (Idea) |

## 2. Definition of done (akhir TA)

- [ ] Laporan TA lulus sidang; angka di laporan identik dengan `results/`.
- [ ] Release `v1.0 Research Pack` (TA) dengan semua komponen terisi; PR G6, G7, G8 merged.
- [ ] Reproducibility package direproduksi pembimbing/peer (catatan di `experiments/README.md`).
- [ ] Integrity Checklist final ditandatangani; `docs/AI-USAGE.md` kumulatif.
- [ ] Untuk endgame ≥ Publication Ready: `PUB-`/`DS-`/`ART-` terdaftar dengan status; release `v1.1 Submitted` bila sudah dikirim.
- [ ] `docs/handoff.md` ke AI Center terisi; Mission Control: Course `TA`, Maturity diperbarui, Next Evidence = langkah owner berikutnya.

## 3. Contoh baris terisi (ilustrasi)

| Artefak | Lokasi | ID | Status |
|---|---|---|---|
| Manuscript "[isi judul]" untuk venue [isi] | `proj-YYYY-[topik]/paper/manuscript.tex` | `PUB-YYYY-NNN` | `submission-ready`; peer review internal 2 reviewer |
| Benchmark harness + model weights | Release `v1.0`; weights di server institusi + `docs/model-card.md` | `ART-YYYY-NNN` | Apache-2.0 (kode); weights research-only |
| Handoff ke AI Center | `docs/handoff.md` | — | Missing evidence: validitas eksternal pada domain [isi]; owner berikutnya: dosen klaster C4 [isi] |

## 4. Ke mana artefak mengalir

```
TA (sem. VIII)
├─ laporan TA + Pack v1.0 ──────► Prodi (kelulusan); Mission Control (Maturity ≥ Research Ready)
├─ manuscript ──────────────────► publications/ (PUB-) → submitted → accepted → published (v1.1 → v2.0)
├─ dataset ─────────────────────► datasets-registry/ (DS-)
├─ software/model/prototype ────► publications/ (ART-); IP review → HKI bila relevan
├─ handoff ─────────────────────► AI Research Center: riset dosen, program-*, partner
└─ Issue lanjutan ──────────────► research-backlog/ → mahasiswa angkatan berikutnya (compounding loop)
```
