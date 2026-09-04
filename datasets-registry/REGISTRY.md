# REGISTRY — Indeks Dataset

> **Status** Draft v0.1 (2026-09) · **Terkait** [Registry README](README.md) · [TPL-05 Dataset Registry Template](../research-os/08-templates/05-dataset-registry-template.md) · [SECURITY.md](../SECURITY.md) · [LICENSING.md](../LICENSING.md) · [BACKLOG.md](../research-backlog/BACKLOG.md)

Indeks semua dataset yang memiliki Dataset ID. Data fisik **tidak** ada di repo ini; kolom *Source* dan kartu menunjukkan lokasinya. Tiga baris pertama adalah **contoh ilustratif**; ganti saat kartu riil pertama masuk.

## Counter

| Tahun | Dataset ID berikutnya |
|---|---|
| 2026 | **DS-2026-004** |

## Indeks

| Dataset ID | Name | Domain | Source | Modality | Size | License | Privacy | Owner | Related Projects | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [DS-2026-001](datasets/DS-2026-001-student-learning.md) | Student Learning Records (teranonimisasi) *(contoh ilustratif)* | Education | UAI | Tabular | `[isi]` | no public license | **Restricted** | `[isi]` | UIAI-2026-001 | contoh ilustratif — belum ada data riil |
| [DS-2026-002](datasets/DS-2026-002-halal-products.md) | Halal Product Packaging Images *(contoh ilustratif)* | Halal | UAI / Partner | Image (+ teks label) | `[isi]` | CC BY 4.0 (bagian publik, setelah review) | Public / Partner (Restricted) | `[isi]` | UIAI-2026-003 | contoh ilustratif — belum ada data riil |
| [DS-2026-003](datasets/DS-2026-003-indonesian-nlp.md) | Indonesian Text Corpus (publik) *(contoh ilustratif)* | General / Education / Government | Public | Text | `[isi]` | `[isi: lisensi korpus asli]` | Public | `[isi]` | UIAI-2026-002 | contoh ilustratif — belum ada data riil |
| `[DS-YYYY-NNN]` | `[nama]` | `[domain]` | `[Public/UAI/Partner]` | `[modalitas]` | `[isi]` | `[isi]` | `[Public/Restricted/Confidential]` | `[isi]` | `[UIAI-…]` | `[draft/active/deprecated]` |

## Penjelasan kolom

| Kolom | Nilai |
|---|---|
| **Dataset ID** | `DS-YYYY-NNN`, link ke kartu |
| **Name** | nama singkat, English |
| **Domain** | Education · Halal · Health · Food · Government · Business · Social Impact · General |
| **Source** | Public · UAI · Partner (boleh gabungan) |
| **Modality** | Text · Image · Tabular · Audio · Time series · Multimodal |
| **Size** | record/citra/token + ukuran file; `[isi]` bila belum dikumpulkan |
| **License** | lisensi asli (dataset pihak ketiga) atau lisensi yang ditetapkan setelah review; "no public license" untuk Restricted/Confidential |
| **Privacy** | Public · Restricted · Confidential ([SECURITY.md](../SECURITY.md)) |
| **Owner** | pemilik/pengelola data; nama riil → `[isi]` |
| **Related Projects** | Research ID yang memakai/menghasilkan |
| **Status** | draft (Issue dibuka) · active (kartu lengkap, review selesai) · deprecated (tidak dipakai/lokasi hilang) · contoh ilustratif |

## Ringkasan (diperbarui tiap akhir semester)

| Privacy | Jumlah kartu |
|---|---|
| Public | 1 *(contoh)* |
| Restricted | 1 *(contoh)* |
| Public/Partner | 1 *(contoh)* |
| Confidential | 0 |

Belum ada dataset riil terdaftar.
