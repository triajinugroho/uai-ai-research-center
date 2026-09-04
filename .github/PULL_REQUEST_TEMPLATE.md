<!--
TEMPLATE DEFAULT — GATE REVIEW
Dipakai untuk G1 Endgame Ready, G4 Question Ready, G7 Claim Ready, dan review lain yang tidak punya template khusus.

Template khusus (tambahkan pada URL "Compare & pull request", atau salin isinya dari .github/PULL_REQUEST_TEMPLATE/):
  ?template=problem-review.md     -> G2 Problem Ready
  ?template=evidence-review.md    -> G3 Evidence Ready
  ?template=method-review.md      -> G5 Method Ready (termasuk Design Defense W8)
  ?template=experiment-review.md  -> G6 Experiment Ready
  ?template=manuscript-review.md  -> G8 Contribution Ready (Research Pack / proposal TA / manuscript)
  ?template=release-review.md     -> Release Review (artefak / dataset / publikasi; tag v0.1-v2.0)

Judul PR yang diharapkan :  GATE REVIEW: <Nama Gate> — <Research ID>
Contoh                   :  GATE REVIEW: Question Ready — UIAI-2026-003
Branch sumber            :  research/gN-<slug>   (mis. research/g4-question)
Definition of done gate  :  research-os/06-execution-os/03-research-gates.md (OPS-03)
Merge = gate lulus. Komentar review adalah bukti proses ilmiah; jangan dihapus.

PR NON-RISET (dokumen / framework / template repo ini): hapus bagian GATE REVIEW dan isi bagian paling bawah.
-->

# GATE REVIEW: <Nama Gate>

| Field | Isi |
|---|---|
| **Research ID** | `UIAI-YYYY-NNN` |
| **Gate yang diajukan** | G_ — <!-- G1 Endgame Ready / G2 Problem Ready / G3 Evidence Ready / G4 Question Ready / G5 Method Ready / G6 Experiment Ready / G7 Claim Ready / G8 Contribution Ready --> |
| **Gate sebelumnya lulus (PR #)** | # |
| **Branch** | `research/gN-<slug>` |
| **Sprint / Minggu Metopen** | S_ / W_ |
| **Tim** | @ |
| **Mentor** | @ |
| **Issue terkait** | # |

## Research Question
<!-- RQ / hipotesis yang sedang dikerjakan. Untuk G1–G3 boleh "belum ditetapkan — tahap evidence". -->

## Method
<!-- Jenis metode dari Computing Research Methods Map (experiment, benchmarking, design science, empirical SE study, ML research, simulation, survey, user study, case study, qualitative) + ringkasan desain. -->

## Dataset
<!-- Dataset ID DS-YYYY-NNN, sumber, ukuran, privasi, lisensi. Tidak ada data mentah di PR ini. -->

## Baseline
<!-- Pembanding paling sederhana yang masuk akal. Tanpa baseline, angka metrik tidak bermakna. -->

## Metrics
<!-- Metrik yang selaras dengan RQ + prosedur evaluasi (split, cross-validation, pencegahan leakage). -->

## Threats to Validity
<!-- Internal / eksternal / konstruk / statistik-kesimpulan. Apa yang bisa membuat kesimpulan salah? -->

## Evidence
<!-- Tautkan bukti wajib gate ini: path file di repo, commit/PR, hasil, figur, notulen. Reviewer harus dapat membuka semuanya. -->

| Bukti wajib (OPS-03) | Link / path | Status |
|---|---|---|
| | | |

## AI Usage
<!-- AI dipakai untuk apa (ide, literatur, kode, analisis, tulisan), bagaimana diverifikasi, siapa yang bertanggung jawab. Link ke AI Usage Log (TPL-10) / AI-USAGE.md. -->
- Ringkasan:
- Link log:

## Definition of Done (OPS-03) — checklist generik
- [ ] Semua butir *definition of done* gate ini pada `research-os/06-execution-os/03-research-gates.md` terpenuhi
- [ ] Semua **bukti wajib** gate ini ada di repositori dan ditautkan pada bagian Evidence
- [ ] Gate sebelumnya sudah lulus (PR merged) atau diwarisi lewat handoff (TPL-14)
- [ ] Research One-Pager (TPL-01) / README riset diperbarui, termasuk bagian *Current Research Gate*
- [ ] Issue terkait diperbarui; label `gate:*` dan field Mission Control diganti setelah merge
- [ ] Release milestone disiapkan bila gate ini memilikinya (v0.1 Problem Validated · v0.2 Evidence Ready · v0.3 Research Design · v0.5 Pilot Experiment · v0.8 Manuscript Draft · v1.0 Research Pack)

## Checklist integritas (Research Integrity Gate — lulus/gagal)
- [ ] Tidak ada fabrikasi/falsifikasi data; hasil negatif dilaporkan
- [ ] Setiap referensi benar-benar dibaca dan terverifikasi ada (DOI/URL), termasuk yang ditemukan lewat AI
- [ ] Tidak ada plagiarisme; kutipan/parafrase disitasi
- [ ] Penggunaan AI yang memengaruhi kesimpulan dicatat di AI Usage Log dan diungkap di `AI-USAGE.md` (AIX-04)
- [ ] Tidak ada data mentah sensitif, data pribadi, atau kredensial di commit (SECURITY.md)
- [ ] Klaim tidak melebihi bukti; tidak ada klaim kausal dari korelasi

## Reviewer yang diminta
- [ ] Dosen pengampu Metopen: @
- [ ] Mentor / dosen pembimbing: @
- [ ] Peer reviewer: @

## Catatan untuk reviewer
<!-- Apa yang paling perlu diperiksa, keputusan yang butuh masukan, keterbatasan yang sudah diketahui. -->

---

## PR non-riset (perubahan dokumen / framework / template repo ini)
<!-- Isi bagian ini saja bila PR bukan gate review. -->

**Ringkasan perubahan**
-

**Checklist**
- [ ] `python3 tools/check_links.py` lulus (0 link/anchor relatif rusak)
- [ ] `python3 tools/build_wbs.py --check` lulus (wajib bila menyentuh `research-wbs.csv` / WBS)
- [ ] Blok metadata dokumen `research-os/` dipertahankan (ID, Paket, Tier, Status, Audiens, Terkait)
- [ ] Istilah/ID mengikuti Glossary (MST-03); label/topics mengikuti `.github/labels.yml` dan GOVERNANCE.md
- [ ] Perubahan tata kelola/lisensi/taksonomi dicatat di `CHANGELOG.md`
