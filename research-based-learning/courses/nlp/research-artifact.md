# NLP — Research Artifact Specification

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — artefak riil menyusul
**Terkait** [README NLP](README.md) · [Hub Research-Based Learning](../../README.md) · [datasets-registry](../../../datasets-registry/README.md) · [ARC-06 Research Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [LICENSING.md](../../../LICENSING.md)

Asset utama MK/topik NLP adalah **korpus/anotasi kecil + benchmark**. Korpus fisik yang sensitif disimpan di luar GitHub; repo menyimpan kartu, guideline, skrip, dan hasil ([SECURITY.md](../../../SECURITY.md)).

## 1. Tabel artefak

| Artefak | Wajib / Opsional | Format & lokasi | Template | ID yang diberikan | Kriteria kualitas | Diserahkan ke | Gate (embrio) |
|---|---|---|---|---|---|---|---|
| **Annotation guideline** | Wajib | Markdown, `docs/annotation-guideline.md` (definisi label, contoh positif/negatif, kasus batas, prosedur adjudikasi, versi) | — (kerangka di `templates/` folder MK) | — | Anotator baru mencapai agreement serupa hanya dengan membaca guideline; setiap revisi berversi dengan alasan | Bersama dataset card ke registry | G5 (construct validity) |
| **Laporan agreement & adjudication** | Wajib | `docs/agreement.md`: nilai agreement per label, matriks ketidaksepakatan, keputusan adjudikasi | — | — | Ukuran agreement yang sesuai (mis. Cohen's/Fleiss' κ) dilaporkan dengan n; ketidaksepakatan sistematis dianalisis, bukan hanya di-rata-rata | Bersama dataset card | G5 |
| **Korpus v0 + split** | Wajib | `data/` (bila publik & aman) atau lokasi eksternal + `data/README.md`; format terbuka (JSONL/CSV/CoNLL); split train/dev/test tanpa duplikasi lintas split | [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) (struktur `data/`) | `DS-YYYY-NNN` (pengelola registry setelah review lisensi & privasi) | Provenance, izin, anonimisasi entitas, statistik korpus, lisensi ditetapkan lewat review ([LICENSING.md §4](../../../LICENSING.md)) | `datasets-registry/` (metadata + lokasi) | G5 (data plan) |
| **Dataset card** | Wajib | `data/README.md` + salinan `datasets-registry/datasets/` | [TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md) | mengikuti `DS-` korpus | Semua field terisi termasuk *known baselines* dan *known limitations* (bias bahasa/dialek/domain) | `datasets-registry/` | G5 |
| **Experiment Card + benchmark** | Wajib | `docs/experiment-card.md`; skrip evaluasi tetap di `src/evaluate.py`; hasil di `results/benchmark.md` | [TPL-09](../../../research-os/08-templates/09-experiment-card.md) | — | Baseline + 1 model; metrik sesuai tugas dengan alasan; ≥ 3 seed; skrip evaluasi tidak berubah setelah hasil pertama; angka baseline direproduksi peer | Repo tim; angka baseline dicatat di dataset card | G6 |
| **Error analysis linguistik** | Wajib | `results/analysis.md` + contoh kasus gagal (dianonimkan) | — | — | Kasus gagal dikelompokkan per fenomena bahasa (ejaan, singkatan, campur kode, dialek, ambiguitas label); klaim dibatasi | Repo tim; ringkasan ke one-pager | G7 |
| **AI Usage Log** | Wajib | `AI-USAGE.md`; bagian khusus *pra-anotasi AI* (jumlah label AI, % dikoreksi manusia) | [TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md) | — | AI tidak dihitung sebagai anotator; setiap label AI diverifikasi; tingkat koreksi dilaporkan | Repo tim | Integrity check |
| **Research One-Pager v0** | Opsional (wajib bila lanjut) | `docs/one-pager.md` | [TPL-01](../../../research-os/08-templates/01-research-one-pager-template.md) | `UIAI-YYYY-TBD` | Problem-first; baseline dan metrik tercantum | Issue backlog; handoff ke Metopen | G2, G7 |
| **Evaluation harness / tool anotasi** | Opsional | `src/` teruji + README | — | `ART-YYYY-NNN` bila dirilis | Dapat dipakai pada korpus lain; teruji; lisensi Apache-2.0 | `publications/` (artefak) | Release review |
| **Handoff** | Opsional (wajib bila lanjut) | `docs/handoff.md` | [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) | — | What exists, missing evidence (mis. ukuran korpus, agreement label tertentu), next steps, owner | Koordinator Metopen / dosen klaster C1; Mission Control field Course = `NLP` | Handoff |

## 2. Definition of done artefak wajib

- [ ] Guideline v2 (setelah pilot) berversi; laporan agreement dengan n dan analisis ketidaksepakatan.
- [ ] Korpus v0 dengan split bebas duplikasi; entitas pribadi dianonimkan; lokasi & lisensi diputuskan lewat review registry.
- [ ] Dataset card diverifikasi; *known baselines* diisi dari benchmark tim.
- [ ] Experiment Card ber-commit sebelum hasil; benchmark ≥ 3 seed; baseline direproduksi peer.
- [ ] Error analysis linguistik dengan contoh yang dianonimkan.
- [ ] `AI-USAGE.md` memuat bagian pra-anotasi AI; [TPL-11](../../../research-os/08-templates/11-research-integrity-checklist.md) ditandatangani.

## 3. Contoh baris terisi (ilustrasi)

| Artefak | Lokasi | ID | Catatan |
|---|---|---|---|
| Korpus "[isi] — teks layanan publik berbahasa Indonesia, tugas NER" | server institusi; kartu di `datasets-registry/datasets/ds-YYYY-NNN-[slug].md` | `DS-YYYY-NNN` | Privasi `Restricted` (entitas dianonimkan; teks mentah tidak di GitHub) |
| Benchmark baseline CRF vs [model] | `proj-YYYY-[topik]/results/benchmark.md` | — | F1 per kelas, 3 seed; direproduksi tim [isi] |
| Handoff | `docs/handoff.md` | — | Missing evidence: agreement label `[isi]` < ambang; perlu 1 anotator tambahan |

## 4. Ke mana artefak mengalir

```
NLP
├─ korpus + guideline + dataset card ──► datasets-registry/ (DS-YYYY-NNN) ──► Metopen/TA bidang NLP, riset dosen C1
├─ benchmark (skrip + baseline) ───────► dicatat di dataset card sebagai known baseline
├─ one-pager + Issue ──────────────────► research-backlog/
├─ harness / tool anotasi ─────────────► publications/ (ART-) bila dirilis
└─ handoff ────────────────────────────► Metopen W1–W2 atau dosen klaster C1
```
