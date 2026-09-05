# PUBLICATIONS — Indeks Publikasi & Artefak

> **Status** Draft v0.1 (2026-09) · **Terkait** [Publications README](README.md) · [Kartu template](_template/publication-card.md) · [2026/](2026/README.md) · [MET-05 Publication Backward Design](../research-os/04-metopen-research-studio/05-publication-backward-design.md) · [REGISTRY.md](../datasets-registry/REGISTRY.md) · [BACKLOG.md](../research-backlog/BACKLOG.md)

Indeks metadata semua publikasi dan artefak. Sumber kebenaran status adalah kartu di folder tahun dan Issue **Publication**; tabel ini diperbarui lewat PR ≤7 hari setelah status berubah. Belum ada publikasi riil; baris berlabel *contoh* hanya menunjukkan format.

## Counter

| Jenis | ID berikutnya |
|---|---|
| Publication | **PUB-2026-001** |
| Artifact | **ART-2026-001** |

Nomor berurutan per tahun, tidak pernah dipakai ulang (termasuk untuk naskah yang ditarik). Baris contoh di bawah **tidak** mengonsumsi nomor.

## 1. Publikasi

| PUB ID | Title | Authors | Research Project | Venue | Status | DOI | Artifact | Dataset | Code |
|---|---|---|---|---|---|---|---|---|---|
| *contoh* PUB-2026-000 | Evaluating Indonesian RAG on University Regulation Documents *(contoh ilustratif)* | `[isi: mahasiswa]`, `[isi: dosen]` | [UIAI-2026-002](../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md) | `[isi: venue dari TPL-06]` | Draft | — | *contoh* ART-2026-000 | [DS-2026-003](../datasets-registry/datasets/DS-2026-003-indonesian-nlp.md) | `proj-2026-indonesian-rag-evaluation` @ `[tag]` |
| `[PUB-YYYY-NNN]` | `[judul]` | `[penulis]` | `[UIAI-YYYY-NNN]` | `[venue]` | `[Draft/Internal Review/Submission Ready/Submitted/Under Review/Revision/Accepted/Published/Rejected-Withdrawn]` | `[DOI]` | `[ART-… / none]` | `[DS-… / none]` | `[repo@tag]` |

### Penjelasan kolom

| Kolom | Isi |
|---|---|
| **PUB ID** | `PUB-YYYY-NNN`, link ke kartu `YYYY/PUB-YYYY-NNN-slug.md` |
| **Title** | judul naskah (boleh berubah; ID tidak) |
| **Authors** | urutan penulis sesuai naskah; nama riil → `[isi]` sampai submission |
| **Research Project** | Research ID; link ke kartu backlog/README riset |
| **Venue** | nama venue dari venue registry ([TPL-06](../research-os/08-templates/06-publication-venue-registry-template.md)) |
| **Status** | Draft · Internal Review · Submission Ready · Submitted · Under Review · Revision · Accepted · Published · Rejected/Withdrawn (sama dengan form Issue *Publication*; kematangan naskah MET-05: manuscript-ready = Draft/Internal Review, submission-ready = Submission Ready) |
| **DOI** | DOI/URL resmi setelah terbit; "—" sebelum itu |
| **Artifact** | `ART-YYYY-NNN` atau "none" |
| **Dataset** | `DS-YYYY-NNN` atau "none" |
| **Code** | repo + tag/commit yang mereproduksi hasil |

## 2. Artefak

| ART ID | Name | Type | Research ID | License | Location | Status |
|---|---|---|---|---|---|---|
| *contoh* ART-2026-000 | Indonesian RAG evaluation harness *(contoh ilustratif)* | software (benchmark tooling) | UIAI-2026-002 | Apache-2.0 (code) · CC BY 4.0 (docs) | `proj-2026-indonesian-rag-evaluation` release `[tag]` | draft |
| `[ART-YYYY-NNN]` | `[nama]` | `[software/model/benchmark/prototype]` | `[UIAI-YYYY-NNN]` | `[lisensi per komponen]` | `[repo/release/HF/server]` | `[draft/released/deprecated/restricted]` |

### Penjelasan kolom

| Kolom | Isi |
|---|---|
| **Type** | software · model · benchmark · prototype |
| **License** | per komponen sesuai [LICENSING.md](../LICENSING.md) §5; "restricted" bila menunggu IP review |
| **Location** | release repo, Hugging Face, server institusi; model weights sensitif tidak dirilis publik tanpa review |
| **Status** | draft (belum rilis) · released (Release Review lulus) · restricted (IP review) · deprecated |

## 3. Venue Registry

Daftar venue yang **boleh** menjadi target submission. Tidak ada submission ke venue yang tidak ada di tabel ini; venue baru diusulkan lewat PR yang mengisi semua kolom (termasuk status etika) memakai format [TPL-06 Publication Venue Registry Template](../research-os/08-templates/06-publication-venue-registry-template.md). Kolom *Publication ethics status* mengikuti tiga nilai: **whitelist** (terverifikasi bereputasi), **hati-hati** (perlu pemeriksaan tambahan sebelum submit), **predatory** (dilarang). Kartu publikasi ([_template/publication-card.md](_template/publication-card.md)) hanya boleh merujuk venue berstatus whitelist atau hati-hati yang sudah diperiksa `@maintainers`.

| Venue | Scope | Indexing | Template | Deadline | Cost | Publication ethics status | Suitable topics | Tingkat | Kecocokan endgame (TA/paper/dataset) |
|---|---|---|---|---|---|---|---|---|---|
| `[isi: nama jurnal nasional terakreditasi]` | `[isi: cakupan, mis. informatika/AI terapan]` | `[isi: SINTA/DOAJ/…]` | `[isi: URL template]` | `[isi: rolling / tanggal]` | `[isi: APC / gratis]` | `[whitelist / hati-hati / predatory]` | `[isi: C1–C4 / domain]` | `[nasional / internasional]` | `[TA / paper / dataset]` |
| `[isi: nama konferensi internasional]` | `[isi]` | `[isi: Scopus/IEEE Xplore/ACM DL/…]` | `[isi]` | `[isi: tanggal call for papers]` | `[isi: registrasi]` | `[whitelist / hati-hati / predatory]` | `[isi]` | `[internasional]` | `[paper / dataset]` |

### Penjelasan kolom

| Kolom | Isi |
|---|---|
| **Scope** | bidang yang diterima venue; cocokkan dengan klaster/domain riset |
| **Indexing** | basis indeks (SINTA, DOAJ, Scopus, IEEE Xplore, ACM DL, dst.) — sebutkan apa adanya, jangan mengklaim indeks yang tidak dapat diverifikasi |
| **Template** | tautan template naskah resmi venue |
| **Deadline** | tanggal call/rolling; perbarui tiap tahun |
| **Cost** | biaya publikasi/registrasi; sumber dana dicatat di Issue Publication |
| **Publication ethics status** | whitelist / hati-hati / predatory — hasil pemeriksaan `@maintainers` (kebijakan review, transparansi biaya, editorial board, indeks yang dapat diverifikasi) |
| **Suitable topics** | klaster/domain roadmap yang cocok |
| **Tingkat** | nasional / internasional |
| **Kecocokan endgame** | untuk endgame apa venue ini realistis: TA (laporan/skripsi → artikel), paper (kontribusi empiris/artefak), dataset (dataset/benchmark paper) — mengikuti backward design [MET-05](../research-os/04-metopen-research-studio/05-publication-backward-design.md) |

Review tabel ini pada roadmap review tahunan; hapus venue yang statusnya berubah menjadi predatory dan catat di [CHANGELOG.md](../CHANGELOG.md).

## 4. Ringkasan (diperbarui tiap akhir semester)

| Status | Jumlah |
|---|---|
| Draft | 0 |
| Internal Review | 0 |
| Submission Ready | 0 |
| Submitted | 0 |
| Under Review | 0 |
| Revision | 0 |
| Accepted | 0 |
| Published | 0 |
| Rejected/Withdrawn | 0 |
| Artefak released | 0 |

Baris contoh tidak dihitung.
