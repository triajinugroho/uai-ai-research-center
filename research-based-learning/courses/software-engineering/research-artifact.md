# Rekayasa Perangkat Lunak — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — artefak riil menyusul
**Terkait** [README RPL](README.md) · [Hub Research-Based Learning](../../README.md) · [ARC-06 Research Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [LICENSING.md](../../../LICENSING.md) · [publications](../../../publications/README.md)

Asset rumpun RPL adalah **research-grade software + testing evidence + artifact README**. Kolom "MK" menandai MK mana dalam rumpun yang bertanggung jawab; pengampu boleh menggeser sesuai RPS.

## 1. Tabel artefak

| Artefak | MK | Wajib / Opsional | Format & lokasi | Template | ID yang diberikan | Kriteria kualitas | Diserahkan ke | Gate (embrio) |
|---|---|---|---|---|---|---|---|---|
| **Problem/requirement brief** | RPL, Proyek PL | Wajib | `docs/problem.md` + `docs/requirements.md`; menunjuk Issue backlog atau stakeholder | — | `UIAI-YYYY-TBD` bila lanjut ke riset | Problem-first; keputusan yang berubah; survei alternatif yang sudah ada (reuse before create) | Repo tim; Issue backlog | G2 |
| **Research-grade software** | Semua | Wajib | Repo: `src/`, `tests/`, `docs/`, `README.md`, `LICENSE` (Apache-2.0), `CITATION.cff`, `CHANGELOG.md`; environment/`Dockerfile` bila perlu | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) atau repo software standar | `ART-YYYY-NNN` bila dirilis lewat release review | Peer menjalankan mengikuti README tanpa bertanya; tes otomatis lulus; dependensi dan lisensinya tercatat | Repo tim (INTERNAL → PUBLIC saat rilis) | G6 (embrio) |
| **Artifact README** | Semua | Wajib | `README.md` dengan bagian: tujuan, klaim yang didukung, instalasi, cara menjalankan, cara mereproduksi hasil evaluasi, struktur, lisensi, sitasi, AI Usage Statement | Kerangka di `templates/` folder MK | — | *Documented, complete, executable/reusable*; hasil evaluasi yang diklaim dapat direproduksi dari README | Repo tim; dilampirkan ke release review | G6, Release review |
| **Testing evidence** | Pengujian PL (utama), RPL | Wajib | `tests/` + `docs/testing-evidence.md`: cakupan, jenis tes (unit/integration/metamorphic/regression model), hasil, kasus gagal yang diperbaiki | [TPL-09](../../../research-os/08-templates/09-experiment-card.md) untuk protokol evaluasi sistem ML | — | Kasus non-deterministik ditangani (seed, toleransi); regression pada model terdokumentasi; hasil tes tersimpan | Repo tim | G6–G7 |
| **Laporan evaluasi pengguna** | Proyek PL (utama), HCI-terkait | Wajib untuk Proyek PL | `docs/user-evaluation.md`: protokol, instrumen, consent, jumlah partisipan, hasil, keterbatasan | — | — | Consent terdokumentasi; data partisipan dianonimkan; klaim kegunaan dibatasi bukti | Repo tim; `docs/ethics.md` | G7 |
| **AI Usage Log + Statement** | Semua | Wajib | `AI-USAGE.md` | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | Kode bantuan AI diuji; verifikasi dicatat; statement di README | Repo tim | Integrity check |
| **Release artefak** | Proyek PL, RPL (bila matang) | Opsional | GitHub Release berversi + PR `release-review.md`; IP review singkat bila berpotensi HKI | PR template `release-review.md` | `ART-YYYY-NNN` (pengelola publications/AI Center) | Lisensi ditetapkan; changelog; sitasi; tidak ada data sensitif; tidak ada dependensi berlisensi tak kompatibel | `publications/` (bagian artefak) | Release review |
| **Issue Artifact / Research Problem** | Semua | Opsional (wajib bila tema baru) | Issue `type:artifact` atau `type:problem` + `cluster:systems` | Form di `.github/ISSUE_TEMPLATE/` | `UIAI-YYYY-NNN` di G2 (Metopen) | Kebutuhan tooling riset yang jelas pemiliknya | `research-backlog/` | G2 |
| **Handoff** | Semua | Opsional (wajib bila lanjut) | `docs/handoff.md` | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | What exists, missing evidence (mis. evaluasi pengguna belum ada), next steps, owner | Metopen / AI Center / riset dosen; Mission Control field Course = `RPL` | Handoff |

## 2. Definition of done artefak wajib

- [ ] Requirement brief menunjuk Issue backlog atau stakeholder yang dapat dihubungi; alternatif yang sudah ada disurvei.
- [ ] Repo dengan `LICENSE`, `CITATION.cff`, `CHANGELOG.md`; tes otomatis lulus.
- [ ] Peer dari tim lain menjalankan software mengikuti README tanpa bertanya; catatan peer run di `docs/`.
- [ ] Testing evidence terdokumentasi (Pengujian PL: termasuk metamorphic/regression pada model) **atau** evaluasi pengguna dengan consent (Proyek PL).
- [ ] Artifact README memuat cara mereproduksi hasil evaluasi + AI Usage Statement.
- [ ] `AI-USAGE.md` terisi; [TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md) ditandatangani; lisensi dependensi diperiksa.

## 3. Contoh baris terisi (ilustrasi)

| Artefak | Lokasi | ID | Catatan |
|---|---|---|---|
| Evaluation harness untuk benchmark NLP kelas [isi] | `proj-YYYY-[topik]/src/evaluate/` | `ART-YYYY-NNN` (setelah release review) | Dipakai ulang oleh 2 tim Metopen; lisensi Apache-2.0 |
| Testing evidence model klasifikasi [isi] | `docs/testing-evidence.md` | — | 12 kasus metamorphic; 2 regresi ditemukan & diperbaiki |
| Handoff ke AI Center | `docs/handoff.md` | — | Missing evidence: evaluasi pengguna hanya 5 partisipan |

## 4. Ke mana artefak mengalir

```
Rumpun RPL (sem. IV–VI)
├─ software + artifact README ─► publications/ (ART-YYYY-NNN) bila dirilis; dipakai riset lain (reuse)
├─ testing evidence ───────────► bukti G6–G7 riset yang memakai software ini
├─ requirement brief / Issue ──► research-backlog/ (type:artifact / type:problem)
├─ prototype + evaluasi ───────► Metopen (entry door Course Project) atau AI Center (entry door Partner)
└─ handoff ────────────────────► Mission Control field Course = RPL
```
