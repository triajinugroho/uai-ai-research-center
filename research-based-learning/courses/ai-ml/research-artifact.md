# AI & Machine Learning — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · GitHub Phase 3 Curriculum Integration (GOV-02 Phase 2 Integrate AI/ML) — artefak riil menyusul
**Terkait** [README AI/ML](README.md) · [Hub Research-Based Learning](../../README.md) · [ARC-06 Research Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [MST-03 Glossary](../../../research-os/00-master/03-glossary.md)

Dokumen ini menetapkan **research asset** yang dihasilkan mata kuliah AI & Machine Learning (mode R). Research asset adalah hasil kegiatan MK yang dapat dipakai ulang oleh riset berikutnya ([MST-03 §2](../../../research-os/00-master/03-glossary.md)). Artefak bertanda **wajib** adalah bagian penilaian; artefak **opsional** menambah rekomendasi handoff.

## 1. Tabel artefak

| Artefak | Wajib / Opsional | Format & lokasi | Template | ID yang diberikan | Kriteria kualitas | Diserahkan ke | Gate (embrio) |
|---|---|---|---|---|---|---|---|
| **Dataset card v0** | Wajib | Markdown, `data/README.md` di repo tim + salinan ke `datasets-registry/datasets/` bila lolos verifikasi | [TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md) | `DS-YYYY-NNN` (oleh pengelola registry, bila dataset baru dan metadata lengkap) | Sumber, owner, lisensi, ukuran, modalitas, privasi (`Public/Restricted/Confidential`), split, risiko leakage, possible research questions terisi; tidak ada data mentah sensitif | `datasets-registry/` (metadata) | G5 (data plan) |
| **Baseline experiment** | Wajib | Kode + config di `experiments/pilot-01/`, hasil di `results/pilot-01/baseline.json` + `results/pilot-01/summary.md` | — (mengikuti struktur [TPL-15](../../../research-os/08-templates/15-research-repository-template.md)) | — | Baseline paling sederhana yang masuk akal; ditetapkan sebelum model utama; ≥ 3 seed/fold; angka direproduksi peer | Repo tim; dirujuk dari Experiment Card | G6 |
| **Experiment Card** | Wajib | Markdown, `experiments/pilot-01/experiment-card.md` | [TPL-09](../../../research-os/08-templates/09-experiment-card.md) | — (mengikuti Research ID bila ada) | Hipotesis, baseline, variabel, dataset, metrik, kontrol, expected result, threats awal — semua terisi **sebelum** hasil ada (dibuktikan tanggal commit) | Repo tim; dilampirkan ke handoff | G5 |
| **Reproducible notebook / repo** | Wajib | Repo dari TPL-15: `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `requirements.txt`/`environment.yml`, `experiments/README.md` | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) | — | Peer dari tim lain mereproduksi angka baseline tanpa bertanya; seed dan konfigurasi tercatat; catatan reproduksi peer tersimpan | Repo tim (INTERNAL → PUBLIC bila dirilis) | G6 |
| **Error analysis** | Wajib | `results/analysis.md` + figur di `figures/` | — | — | Kasus gagal dikelompokkan; perbandingan terhadap baseline; variansi dilaporkan; klaim dibatasi bukti; hasil negatif tidak disembunyikan | Repo tim; diringkas di one-pager | G7 |
| **Research One-Pager v0** | Wajib | Markdown 1 halaman, `docs/one-pager.md` | [TPL-01](../../../research-os/08-templates/01-research-one-pager-template.md) | ID sementara per [CONTRIBUTING.md §2](../../../CONTRIBUTING.md); `UIAI-YYYY-NNN` resmi saat lolos G2 di Metopen | Problem, why, RQ awal, method, data, baseline, metric, expected contribution, keterbatasan; ditulis problem-first | Dilampirkan ke Issue backlog; handoff ke Metopen | G2 (awal), G7 (klaim) |
| **AI Usage Log + AI Usage Statement** | Wajib | `docs/AI-USAGE.md`; log tabel per penggunaan (kolom TPL-10) | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | Tool, tanggal, tujuan, output material, verifikasi, dimasukkan/tidak ke hasil akhir; kekeliruan AI yang ditemukan dicatat | Repo tim; lampiran laporan | Integrity check setiap milestone |
| **Issue Research Problem** | Opsional (wajib bila tema baru) | Issue GitHub `type:problem` + `cluster:*` | Form *Research Problem* di `.github/ISSUE_TEMPLATE/` | `UIAI-YYYY-NNN` saat lolos G2 | Problem-first; stakeholder jelas; potential dataset dan related courses terisi | `research-backlog/` | G2 |
| **Model / artefak terlatih** | Opsional | Weights di luar GitHub (server institusi/HF) + kartu model di `docs/model-card.md` (file tambahan di luar struktur minimum TPL-15) | — | `ART-YYYY-NNN` bila dirilis lewat release review | Kartu model: data latih, metrik, keterbatasan, lisensi; IP review bila berpotensi HKI ([LICENSING.md](../../../LICENSING.md)) | `publications/` (bagian artefak) | Release review |
| **Handoff ke Metopen** | Opsional (wajib bagi tim yang lanjut) | `docs/handoff.md` | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | What exists, missing evidence, next steps, owner; ditandatangani pengampu | Koordinator Metopen; Mission Control field Course = `AI/ML` | Handoff |

## 2. Definition of done artefak wajib (akhir semester)

- [ ] Dataset card v0 lengkap; keputusan pengelola registry (diterima dengan `DS-` / ditolak dengan alasan) tercatat.
- [ ] Experiment Card ber-commit sebelum commit hasil pertama.
- [ ] Baseline dan ≥ 1 metode pembanding dijalankan dengan ≥ 3 seed/fold; tabel hasil di `results/`.
- [ ] Peer reproduction oleh tim lain berhasil untuk angka baseline; catatan di `experiments/README.md`.
- [ ] Error analysis + threats to validity awal di `results/analysis.md`.
- [ ] Research One-Pager v0 dilampirkan ke Issue backlog (Issue baru atau Issue yang dipakai).
- [ ] `docs/AI-USAGE.md` terisi; Research Integrity Checklist ([TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md)) ditandatangani tim.
- [ ] Tidak ada data pribadi/partner mentah di repo ([SECURITY.md](../../../SECURITY.md)).

## 3. Contoh baris terisi (ilustrasi, bukan data riil)

| Artefak | Lokasi | ID | Status |
|---|---|---|---|
| Dataset card v0 "[isi nama dataset]" | `datasets-registry/datasets/ds-YYYY-NNN-[slug].md` | `DS-YYYY-NNN` | Diterima pengelola registry, privasi `Public` |
| Experiment Card "baseline logistic regression vs [metode]" | `proj-YYYY-[topik]/experiments/pilot-01/experiment-card.md` | ID sementara | Commit 2 minggu sebelum hasil |
| Handoff ke Metopen | `proj-YYYY-[topik]/docs/handoff.md` | — | Missing evidence: threats to validity eksternal, literature map |

## 4. Ke mana artefak mengalir

```
AI/ML (sem. V)
├─ dataset card ──────────► datasets-registry/  (DS-YYYY-NNN)
├─ one-pager + Issue ─────► research-backlog/   (ID sementara → UIAI-YYYY-NNN di G2 Metopen)
├─ experiment card + repo ► Metopen W1–W2 (entry door Course Project) ─► TA
├─ model/artefak ─────────► publications/ (ART-YYYY-NNN) bila dirilis
└─ semua ─────────────────► Mission Control (field Course = AI/ML) untuk tim yang lanjut
```

Artefak yang tidak lanjut ke Metopen tetap bernilai: dataset card dan Issue backlog adalah *research memory* Prodi yang dapat diambil angkatan berikutnya (*research assets should compound*).
