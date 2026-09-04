# Publication Card — Template Kartu Publikasi

> **Status** Draft v0.1 (2026-09) · **Terkait** [Publications README](../README.md) · [PUBLICATIONS.md](../PUBLICATIONS.md) · [MET-05 Publication Backward Design](../../research-os/04-metopen-research-studio/05-publication-backward-design.md) · [TPL-06 Venue Registry](../../research-os/08-templates/06-publication-venue-registry-template.md) · [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md) · [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md)

Salin bagian **A** ke `publications/YYYY/PUB-YYYY-NNN-slug.md`, ganti judul H1 dengan `PUB-YYYY-NNN — Judul`, dan isi semua field. Bagian **B** adalah contoh terisi (ilustratif) sebagai acuan tingkat kelengkapan. Jangan menyimpan PDF penerbit; cukup metadata, DOI, sitasi, dan tautan.

---

## A. Template

### Metadata inti

| Field | Isi |
|---|---|
| **PUB ID** | `PUB-YYYY-NNN` |
| **Title** | `[judul naskah]` |
| **Authors** | `[Nama 1 (afiliasi)]`, `[Nama 2 (afiliasi)]`, … — urutan sesuai naskah |
| **CRediT (ringkas)** | `[Nama 1]`: conceptualization, methodology, software, investigation, writing – original draft · `[Nama 2]`: supervision, validation, writing – review & editing · … |
| **Research Project** | `UIAI-YYYY-NNN` — link ke kartu backlog / README riset |
| **Venue** | `[nama venue]` (`[jurnal/konferensi/workshop]`, `[indexing]`) — harus ada di venue registry [TPL-06](../../research-os/08-templates/06-publication-venue-registry-template.md) |
| **Status** | Draft / Submitted / Under Review / Accepted / Published / Rejected-Withdrawn |
| **DOI** | `[DOI atau —]` |
| **Artifact** | `ART-YYYY-NNN` / none |
| **Dataset** | `DS-YYYY-NNN` / none |
| **Code** | `[repo]` @ `[tag/commit]` |

### Isi

| Field | Isi |
|---|---|
| **Abstract** | `[150–250 kata; klaim tidak melebihi bukti]` |
| **Keywords** | `[3–6 kata kunci]` |
| **Contribution type** | empiris / artefak / metode / dataset / replikasi / studi kasus ([ARC-06](../../research-os/02-academic-architecture/06-research-output-taxonomy.md)) |
| **Cluster / Domain** | `[C1–C4]` / `[domain]` |

### Timeline

| Milestone | Tanggal |
|---|---|
| Manuscript-ready | `[YYYY-MM-DD]` |
| Submission-ready (checklist integritas lengkap) | `[YYYY-MM-DD]` |
| Submitted | `[YYYY-MM-DD]` |
| Review received | `[YYYY-MM-DD]` |
| Revision submitted | `[YYYY-MM-DD]` |
| Accepted | `[YYYY-MM-DD]` |
| Published | `[YYYY-MM-DD]` |

### Review dan revisi

| Field | Isi |
|---|---|
| **Reviewer comments summary** | `[ringkasan poin utama reviewer; tanpa menyalin teks review secara utuh bila kebijakan venue melarang]` |
| **Response summary** | `[apa yang diubah; apa yang dipertahankan dan mengapa]` |
| **Hasil negatif yang dilaporkan** | `[ya/tidak; bagian mana]` |

### Hak dan akses

| Field | Isi |
|---|---|
| **License / copyright** | `[publisher copyright / CC BY 4.0 (OA) / …]` |
| **Preprint link** | `[URL atau "tidak diizinkan oleh kebijakan venue"]` |
| **Publisher PDF di repo?** | tidak (aturan [Publications README](../README.md) §2) |
| **Citation (BibTeX)** | `[isi setelah terbit]` |

### Integritas

| Field | Isi |
|---|---|
| **AI Usage Statement (singkat)** | `[AI dipakai untuk apa (mis. brainstorming keyword, debugging kode, penyuntingan bahasa); apa yang TIDAK dipakai AI; semua keluaran diverifikasi manusia; log lengkap di AI-USAGE.md repo riset]` |
| **Integrity checklist done** | `[ya — tanggal, ditandatangani oleh]` ([TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md)) |
| **Ethics / privacy** | `[protokol etik/consent bila ada data manusia; Dataset ID dengan Privacy-nya]` |
| **Conflict of interest** | `[none / jelaskan]` |

---

## B. Contoh terisi (ilustratif — bukan publikasi riil)

### PUB-2026-000 — Evaluating Retrieval-Augmented Generation on Indonesian University Regulation Documents

| Field | Isi |
|---|---|
| **PUB ID** | PUB-2026-000 *(contoh; nomor 000 tidak pernah diberikan)* |
| **Title** | Evaluating Retrieval-Augmented Generation on Indonesian University Regulation Documents |
| **Authors** | `[isi: mahasiswa]` (UAI), `[isi: dosen pembimbing]` (UAI) |
| **CRediT (ringkas)** | mahasiswa: conceptualization, methodology, software, investigation, data curation, writing – original draft · dosen: supervision, methodology, validation, writing – review & editing |
| **Research Project** | [UIAI-2026-002](../../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md) |
| **Venue** | `[isi: konferensi nasional/internasional NLP-IR dari venue registry]` |
| **Status** | Draft |
| **DOI** | — |
| **Artifact** | ART-2026-000 *(contoh)* — evaluation harness |
| **Dataset** | [DS-2026-003](../../datasets-registry/datasets/DS-2026-003-indonesian-nlp.md) + benchmark QA turunan `[DS-… setelah didaftarkan]` |
| **Code** | `proj-2026-indonesian-rag-evaluation` @ `v0.8` |
| **Abstract** | Kami mengevaluasi tiga konfigurasi RAG terhadap baseline BM25 dan model tanpa retrieval pada `[N]` pasangan pertanyaan–jawaban dari dokumen regulasi kampus berbahasa Indonesia yang dianotasi `[k]` anotator (agreement `[κ]`). Hasil menunjukkan `[ringkasan temuan; termasuk jenis kesalahan dominan]`. Penilaian LLM-as-judge `[sejalan/tidak sejalan]` dengan penilaian manusia pada `[aspek]`. Kami merilis benchmark dan harness evaluasi. *(contoh ilustratif; angka diisi dari hasil riil)* |
| **Keywords** | retrieval-augmented generation; Indonesian NLP; evaluation; university regulation; benchmark |
| **Contribution type** | empiris + dataset/benchmark |
| **Cluster / Domain** | C1 / Education, Government |
| **Timeline** | manuscript-ready `[isi]` · submission-ready `[isi]` · submitted — · accepted — · published — |
| **Reviewer comments summary** | belum ada (Draft) |
| **Response summary** | — |
| **Hasil negatif yang dilaporkan** | ya — konfigurasi `[X]` tidak mengalahkan BM25 pada pertanyaan prosedural |
| **License / copyright** | mengikuti venue; benchmark turunan direncanakan CC BY 4.0 setelah review; kode Apache-2.0 |
| **Preprint link** | `[isi bila kebijakan venue mengizinkan]` |
| **Publisher PDF di repo?** | tidak |
| **Citation (BibTeX)** | `[isi setelah terbit]` |
| **AI Usage Statement (singkat)** | Asisten AI dipakai untuk eksplorasi kata kunci pencarian literatur, bantuan debugging skrip evaluasi, dan penyuntingan bahasa Inggris. Tidak dipakai untuk menghasilkan data, anotasi acuan, atau menulis analisis hasil. Semua referensi diverifikasi keberadaannya; log lengkap di `docs/AI-USAGE.md` repo riset. |
| **Integrity checklist done** | `[isi: tanggal; ditandatangani mahasiswa + dosen]` — wajib sebelum Submitted |
| **Ethics / privacy** | dokumen sumber publik; log pengguna tidak dipakai; DS-2026-003 Privacy = Public |
| **Conflict of interest** | none |
