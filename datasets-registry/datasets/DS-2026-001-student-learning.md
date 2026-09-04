# DS-2026-001 — Student Learning Records (teranonimisasi)

> **Status** contoh ilustratif — belum ada data riil · Draft v0.1 (2026-09) · **Terkait** [REGISTRY.md](../REGISTRY.md) · [Registry README](../README.md) · [TPL-05](../../research-os/08-templates/05-dataset-registry-template.md) · [SECURITY.md](../../SECURITY.md) · [UIAI-2026-001](../../research-backlog/problems/UIAI-2026-001-ai-assisted-academic-advising.md) · [Domain Education](../../research-roadmap/domains/education.md)

## Kartu dataset

| Field | Nilai |
|---|---|
| **Dataset ID** | DS-2026-001 |
| **Name** | Student Learning Records (anonymized) |
| **Domain** | Education |
| **Source** | UAI (unit layanan akademik) |
| **Owner** | `[isi: unit pengelola data akademik UAI; penanggung jawab]` |
| **Size** | `[isi: jumlah mahasiswa, semester, jumlah baris]` |
| **Modality** | Tabular (nilai per mata kuliah, SKS, IPK/IPS, kehadiran agregat, jalur masuk terkategori) |
| **License** | No public license (Restricted) |
| **Privacy** | **Restricted** — data pribadi mahasiswa; hanya versi pseudonim/agregat yang boleh dianalisis |
| **Potential Task** | Prediction (early warning risiko akademik), classification, clustering pola belajar, fairness audit |
| **Related Projects** | [UIAI-2026-001](../../research-backlog/problems/UIAI-2026-001-ai-assisted-academic-advising.md) |
| **Quality Notes** | `[isi setelah data diterima]` — periksa: kelengkapan kehadiran per mata kuliah, perubahan kurikulum antar angkatan, mahasiswa pindah/cuti, ketidakseimbangan kelas berisiko |
| **Access** | Permintaan tertulis ke Owner dengan Research ID, protokol etik, dan daftar field yang dibutuhkan; disetujui Owner + pengelola registry; akses per orang, berjangka |
| **Possible Research Questions** | (1) Seberapa akurat prediksi risiko keterlambatan studi dari data semester 1–4 dibanding aturan ambang sederhana? (2) Apakah model berkinerja berbeda antar kelompok (jalur masuk, angkatan)? (3) Pola beban SKS seperti apa yang berasosiasi dengan penurunan IPS? |
| **Physical Location** | Institutional server UAI `[isi]`; **tidak** di GitHub, Drive pribadi, atau layanan AI eksternal |
| **Review Date** | `[isi: tanggal review privasi/etik]` |
| **Status** | contoh ilustratif — belum ada data riil |

## Catatan anonimisasi dan consent

1. **Pseudonimisasi**: NIM dan nama diganti ID acak oleh Owner sebelum data diserahkan; tabel pemetaan disimpan Owner, tidak pernah diberikan ke tim riset.
2. **Minimisasi**: hanya field yang dibutuhkan RQ; tanpa alamat, kontak, atau catatan bebas.
3. **Agregasi/k-anonymity**: kelompok kecil (mis. jalur masuk dengan <5 mahasiswa) digabung agar tidak dapat diidentifikasi ulang.
4. **Consent**: mekanisme persetujuan mahasiswa `[isi: opt-in/opt-out sesuai kebijakan kampus]`; consent dapat ditarik; didokumentasikan di `docs/ethics.md` riset.
5. **Izin institusi/komite etik**: `[isi]` — wajib sebelum G5 Method Ready.
6. **Penggunaan**: hanya untuk riset yang tercantum di Related Projects; penggunaan baru memerlukan permintaan baru.
7. **Retensi**: data dihapus dari lingkungan analisis setelah riset selesai `[isi: jangka waktu]`; hasil agregat/model boleh disimpan setelah review kebocoran informasi.
8. **Larangan**: tidak ada data ini dalam prompt ke layanan AI eksternal; tidak ada output notebook yang menampilkan baris individual di repo.

## Sensitivitas dan risiko

| Risiko | Mitigasi |
|---|---|
| Re-identifikasi dari kombinasi field | agregasi; uji re-identifikasi sebelum analisis |
| Profiling/diskriminasi mahasiswa | audit fairness wajib; hasil dipakai sebagai pendukung keputusan manusia |
| Bocor lewat repo/notebook | `.gitignore` `data/raw/`, `data/private/`; review PR memeriksa output |
| Perubahan kurikulum membuat data tidak sebanding | catat versi kurikulum per angkatan di Quality Notes |
