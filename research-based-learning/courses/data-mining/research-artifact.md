# Data Mining — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — artefak riil menyusul
**Terkait** [README Data Mining](README.md) · [Hub Research-Based Learning](../../README.md) · [datasets-registry](../../../datasets-registry/README.md) · [ARC-06 Research Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md)

Asset utama Data Mining adalah **pengetahuan tentang dataset** — evidence map dataset dan error analysis — bukan model. Artefak **wajib** menjadi bagian penilaian; **opsional** memperkuat rekomendasi handoff.

## 1. Tabel artefak

| Artefak | Wajib / Opsional | Format & lokasi | Template | ID yang diberikan | Kriteria kualitas | Diserahkan ke | Gate (embrio) |
|---|---|---|---|---|---|---|---|
| **Dataset card v0 → final** | Wajib | Markdown, `data/README.md` di repo tim; salinan ke `datasets-registry/datasets/` bila lolos verifikasi | [TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md) | `DS-YYYY-NNN` (pengelola registry; dataset lama cukup diperkaya, ID tetap) | Sumber, owner, lisensi, ukuran, modalitas, privasi, kualitas, possible research questions, known limitations; tidak ada data mentah sensitif | `datasets-registry/` | G5 (data plan) |
| **Evidence map dataset** | Wajib | `docs/dataset-evidence-map.md`: tabel (aspek · apa yang diketahui · sumber/bukti · implikasi) + daftar risiko leakage & mitigasi | — (tabel bebas; contoh di §3) | — | Provenance jelas; hasil terdahulu pada dataset ini (bila ada) dicantumkan dengan sumber yang bisa diverifikasi; distribusi kelas, missing, duplikasi, fitur bocor diperiksa dengan bukti (figur/tabel) | Dilampirkan pada dataset card (bagian limitations) | G3 (bukti tentang data), G5 |
| **Laporan baseline & pembanding** | Wajib | `results/baseline.md` + notebook di `notebooks/` | — | — | Baseline sederhana + 1 metode; split/CV benar; ≥ 3 fold/seed; angka baseline direproduksi peer | Repo tim | G6 |
| **Error analysis report** | Wajib | `results/analysis.md` + figur | — | — | Kasus gagal dikelompokkan (slice/kelas/fitur); perbandingan ke baseline; "apa yang tidak boleh disimpulkan" ditulis eksplisit | Repo tim; ringkasan ke dataset card | G7 |
| **Notebook reproducible** | Wajib | `notebooks/` + `requirements.txt`, seed, README langkah | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) (struktur minimum) | — | Peer menjalankan ulang tanpa bertanya | Repo tim | G6 |
| **AI Usage Log** | Wajib | `AI-USAGE.md` | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | Tool, tujuan, output material, verifikasi, dimasukkan/tidak | Repo tim; lampiran laporan | Integrity check |
| **Issue Research Problem** | Opsional | Issue `type:problem` + `type:dataset` bila perlu | Form di `.github/ISSUE_TEMPLATE/` | `UIAI-YYYY-NNN` saat lolos G2 (di Metopen) | Pertanyaan analitis yang layak menjadi riset; related courses: Data Mining | `research-backlog/` | G2 |
| **Data quality script** | Opsional | `src/quality_checks.py` (duplikasi, missing, leakage sederhana) | — | `ART-YYYY-NNN` bila dirilis dan dipakai ulang lintas kelas | Berjalan pada dataset lain dengan konfigurasi minimal; teruji | `publications/` (artefak) bila dirilis | Release review |
| **Handoff** | Opsional (wajib bila lanjut ke AI/ML/NLP/Metopen) | `docs/handoff.md` | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | What exists, missing evidence, next steps, owner | Pengampu MK penerima; pengelola registry | Handoff |

## 2. Definition of done artefak wajib

- [ ] Dataset card diverifikasi pengelola registry (diterima/diperkaya/ditolak dengan alasan tercatat).
- [ ] Evidence map dataset memuat ≥ 5 aspek dengan bukti dan ≥ 2 risiko leakage dengan mitigasi.
- [ ] Baseline + 1 pembanding, ≥ 3 fold/seed, angka baseline direproduksi tim lain.
- [ ] Error analysis memuat bagian "apa yang tidak boleh disimpulkan".
- [ ] `AI-USAGE.md` terisi; [TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md) ditandatangani.
- [ ] Tidak ada data pribadi mentah di repo.

## 3. Contoh evidence map dataset (ilustrasi)

| Aspek | Apa yang diketahui | Bukti/sumber | Implikasi untuk eksperimen |
|---|---|---|---|
| Provenance | Dikumpulkan [isi] tahun [isi], lisensi [isi] | Kartu dataset `DS-YYYY-NNN` | Boleh dipakai untuk riset akademik |
| Distribusi kelas | Kelas minoritas 8% | `figures/class-dist.png` | Accuracy menyesatkan; pakai F1/PR-AUC + baseline majority |
| Fitur bocor | Kolom `[isi]` diisi setelah label diketahui | Analisis korelasi + dokumentasi sumber | Kolom dibuang sebelum split |
| Duplikasi | 3% baris duplikat lintas split | `src/quality_checks.py` | Dedup sebelum split |
| Hasil terdahulu | [isi] melaporkan F1 0,xx dengan metode [isi] | DOI/URL terverifikasi | Menjadi pembanding eksternal, bukan baseline internal |

## 4. Ke mana artefak mengalir

```
Data Mining (sem. IV)
├─ dataset card + evidence map ──► datasets-registry/ (DS-YYYY-NNN)  ──► AI/ML (sem. V), NLP, Metopen, riset dosen
├─ pertanyaan analitis ──────────► research-backlog/ (Issue type:problem)
├─ data quality script ──────────► publications/ (ART-) bila dirilis
└─ handoff ──────────────────────► pengampu MK penerima; Mission Control field Course = Data Mining
```
