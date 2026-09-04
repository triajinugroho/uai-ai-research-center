# Research Handoff Template

> **ID** TPL-14 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Tim yang menyerahkan (mahasiswa/dosen), penerima (pembimbing TA, mahasiswa angkatan berikut, klaster AI Center), dosen pengampu, admin riset
> **Terkait** [ARC-04 Build–Prove–Contribute](../02-academic-architecture/04-build-prove-contribute.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [TPL-02 Mission Tracker](02-research-mission-tracker-template.md) · [TPL-15 Repository Template](15-research-repository-template.md) · [MST-03 Glossary (Handoff)](../00-master/03-glossary.md)

## Cara pakai

Handoff mencatat transfer riset antar tahap — **Course → Metopen → TA → AI Center** — agar penerima dapat melanjutkan tanpa mengulang dari nol dan gate yang sudah lulus dapat diwarisi (*inherited*) dengan bukti. Diisi oleh tim yang menyerahkan bersama mentor pada akhir tahap: akhir mata kuliah mode R (asset ke backlog/Metopen), setelah G8 Metopen (ke pembimbing TA), setelah sidang TA (ke AI Center/klaster/angkatan berikut), atau saat tim berhenti di tengah jalan. Disimpan sebagai `docs/handoff-[dari]-[ke]-[YYYY-MM].md` di repositori riset, ditautkan dari README riset dan Issue backlog, dan dicatat di Mission Tracker (kolom Status/Next Evidence). Penerima menandatangani setelah memverifikasi bahwa artefak yang disebut benar-benar ada dan dapat dibuka; gate warisan yang bukti utamanya hilang tidak diakui.

## Jenis transisi

| Transisi | Kapan | Yang wajib ada | Penerima |
|---|---|---|---|
| Course → Metopen | akhir MK mode R (AI/ML, Data Mining, NLP, RPL) | research asset (dataset/kode/prototype/literature map), Issue backlog, kartu dataset | dosen pengampu Metopen, tim Metopen |
| Metopen → TA | setelah G8 (W16) | Research Pack v1.0, repositori, Integrity Checklist PASS, proposal TA | pembimbing TA, mahasiswa (sering orang yang sama) |
| TA → AI Center | setelah sidang TA / rilis | hasil akhir, manuscript/status publikasi, artefak (ART), dataset (DS), daftar masalah lanjutan | ketua klaster, mentor, angkatan berikut |
| Berhenti di tengah | tim tidak melanjutkan | status gate terakhir, artefak yang ada, alasan | backlog (status Idea/Archived) |

## Template (salin ke `docs/handoff-[dari]-[ke]-[YYYY-MM].md`)

```markdown
# Research Handoff — [Research ID] · [judul]
Dari: [tahap/tim/nama] → Ke: [tahap/tim/nama] · Tanggal: [YYYY-MM-DD] · Gate terakhir lulus: [Gn] (PR #[n], [tanggal]) · Release: [v0.x]

## 1. What exists (artefak + lokasi + status gate)
| Artefak | Lokasi (path/URL/ID) | Status | Gate/bukti | Catatan |
|---|---|---|---|---|
| [Problem Brief] | [docs/problem.md] | [final/draft] | [G2 ✓] | |
| [Literature map + synthesis matrix] | [docs/literature-map.md, references.bib (n entri)] | | [G3 ✓] | |
| [RQ/Hypothesis, Contribution] | [docs/research-question.md] | | [G4 ✓] | |
| [Design Card, Experiment Cards] | [docs/research-design.md, experiments/] | | [G5 ✓] | |
| [Kode, environment, seed] | [src/, requirements.txt, experiments/config-*.yaml] | | [G6 ✓; reproduksi peer tanggal] | |
| [Data / metadata] | [DS-…; data/README.md; lokasi fisik] | | | [privasi, cara akses] |
| [Hasil, analisis, figur] | [results/, figures/] | | [G7 ✓] | |
| [Research Pack / proposal / manuscript] | [paper/, release v1.0] | | [G8 ✓] | |
| [AI Usage Log & Statement, ethics] | [docs/ai-usage-log.md, docs/AI-USAGE.md, docs/ethics.md] | | | |
| [Integrity Checklist] | [docs/integrity-checklist.md] | [PASS/FAIL] | | |

## 2. Missing evidence (apa yang belum ada agar klaim/gate berikutnya sah)
- [bukti] — untuk [gate/klaim] — perkiraan usaha [jam/minggu]

## 3. Next steps (urut prioritas, dengan gate sasaran)
1. [langkah] → [Gn] → target [tanggal]
2. [...]

## 4. Owner
| Peran | Nama | Kontak | Tanggung jawab |
|---|---|---|---|
| Penerus utama | | | |
| Mentor / pembimbing | | | |
| Pemilik data | | | |

## 5. Risiko yang diketahui
| Risiko | Dampak | Mitigasi yang disarankan |
|---|---|---|

## 6. Keputusan yang menunggu
- [keputusan] — pengambil keputusan: [siapa] — dibutuhkan sebelum: [tanggal]

## 7. Kontak & akses
- Repositori: [URL] — akses penerima: [sudah/belum]; data: [cara minta]; akun/API: [disimpan di mana, bukan di repo]

## 8. Tanda tangan
| Peran | Nama | Tanggal | Verifikasi artefak (✓) |
|---|---|---|---|
| Menyerahkan | | | |
| Menerima | | | |
| Mentor/dosen pengampu | | | |
```

## Contoh terisi: Metopen → TA (UIAI-2026-001)

Dari: tim Metopen [Mahasiswa A], [Mahasiswa B] → Ke: TA [Mahasiswa A] dengan pembimbing [Dosen C3] · Tanggal: 2026-12-[dd] · Gate terakhir lulus: G8 (PR #[n], 2026-12-[dd]) · Release: v1.0 Research Pack

| Artefak | Lokasi | Status | Gate/bukti | Catatan |
|---|---|---|---|---|
| Problem Brief, stakeholder statement | `docs/problem.md` | final | G2 ✓ | problem owner: Kaprodi |
| Literature map + synthesis matrix | `docs/literature-map.md`, `references.bib` (22 entri terverifikasi) | final | G3 ✓ | 3 usulan AI dibuang |
| RQ1–RQ2, H1–H2, contribution | `docs/research-question.md` | final | G4 ✓ | RQ2 definisi operasional v2 |
| Design Card v2, EXP-01, EXP-02 | `docs/research-design.md`, `experiments/` | final | G5 ✓, G6 ✓ (reproduksi [Mahasiswa C] 2026-10-[dd]) | 3 run per kasus |
| Kode baseline + LLM+RAG, environment | `src/`, `requirements.txt`, `experiments/config-0[1-2].yaml`, seed 42 | berjalan | G6 ✓ | model [nama/versi] dicatat |
| Data | DS-2026-001 (restricted, institutional server); `data/README.md`; sampel sintetis 40 kasus | akses perlu diperbarui untuk TA | — | consent 120 mahasiswa tersimpan di Prodi |
| Hasil & analisis | `results/analysis.md`, `results/exp-0[1-2].csv`, `figures/` | final | G7 ✓ | H1 tidak terdukung pada pilot |
| Research Pack + proposal TA | `paper/proposal-ta.md`, release v1.0 | final | G8 ✓ | defense lulus dengan revisi minor |
| AI Usage Log & Statement, ethics | `docs/ai-usage-log.md` (14 entri), `docs/AI-USAGE.md`, `docs/ethics.md` | final | — | |
| Integrity Checklist | `docs/integrity-checklist.md` | PASS | — | ditandatangani 2026-12-[dd] |

Missing evidence: (1) evaluasi 80 kasus nyata dengan post-check aturan SKS — untuk klaim RQ1 di TA — ±3 minggu; (2) user study 6 dosen wali dengan κ — untuk RQ2 — ±4 minggu; (3) perbandingan 2 model LLM — untuk threats konstruk — ±2 minggu.

Next steps: 1. Perbarui akses DS-2026-001 atas nama TA → G5 warisan dikonfirmasi → 2027-01-[dd] · 2. EXP-03 evaluasi 80 kasus → G6/G7 TA → 2027-02-[dd] · 3. User study → G7 → 2027-03-[dd] · 4. Manuscript untuk [konferensi nasional — isi] → v0.8 → 2027-04-[dd].

Owner: penerus [Mahasiswa A] · pembimbing [Dosen C3] · pemilik data Kaprodi [isi]. Risiko: biaya API LLM (mitigasi: kuota Prodi/model lokal); pergantian kurikulum 2027 (bekukan versi kurikulum). Keputusan menunggu: apakah [Mahasiswa B] menjadi ko-penulis paper — mentor — sebelum 2027-01-[dd]. Kontak & akses: repo `proj-2026-ai-academic-advising` (pembimbing sudah write); API key di vault Prodi. Tanda tangan: [Mahasiswa A], [Mahasiswa B], [Dosen C3], [dosen pengampu] — artefak diverifikasi ✓.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| What exists | Setiap artefak punya path/ID yang dapat dibuka dan status gate | "Semua ada di repo" |
| Missing evidence | Menyebut untuk klaim/gate apa dan perkiraan usaha | "Perlu penelitian lebih lanjut" |
| Next steps | Urut, bergate, bertanggal | Daftar keinginan |
| Owner | Nama + kontak + tanggung jawab; pemilik data disebut | Kosong atau "tim" |
| Verifikasi | Penerima mencentang setelah membuka artefak | Ditandatangani tanpa membuka repo |
| Kejujuran | Hasil negatif, risiko, dan keputusan tertunda tercatat | Hanya kabar baik |
