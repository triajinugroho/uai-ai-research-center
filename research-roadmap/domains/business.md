# Domain — Business (Bisnis & UMKM)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C2 AI Systems, Software & Security](../clusters/ai-systems-security.md) · [C3 Human-Centered & Responsible AI](../clusters/responsible-human-ai.md) · [C4 Applied AI](../clusters/applied-ai.md) · [AIR-05 Demand–Supply Marketplace](../../research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `business` |
| Program | belum ada program tersendiri sampai 2030; dijalankan sebagai `proj-*`, sering lewat entry door Partner/Kerja Praktik |
| Klaster utama | C4 (prediksi, rekomendasi), C2 (MLOps berbiaya rendah), C3 (keputusan manusia berbantuan AI), C1 (NLP ulasan/percakapan) |
| Prioritas roadmap | sel C3 × Business 2027; C2 × Business 2029 |

## 1. Mengapa domain ini untuk UAI

UMKM adalah tulang punggung ekonomi Indonesia dan prioritas nasional yang generik; mereka juga menjadi sumber masalah nyata yang **mudah diakses** mahasiswa lewat Kerja Praktik, keluarga, dan komunitas. UAI memiliki fakultas ekonomi/bisnis (sumber: dokumen diskusi — verifikasi) untuk kolaborasi lintas fakultas, dan komunitas kampus Islam memberi akses ke ekosistem ekonomi syariah, koperasi, dan filantropi. Domain ini melatih hal yang sering hilang di riset mahasiswa: **apakah model sederhana yang murah sudah cukup**, dan apakah pelaku usaha benar-benar memakai hasilnya.

> **Catatan verifikasi.** Mitra fakultas ekonomi/bisnis dan asosiasi UMKM: `[isi]`. Data transaksi partner selalu Restricted.

## 2. Problem space (masalah nyata)

1. UMKM mengambil keputusan **stok dan harga** tanpa data; alat prediksi yang ada terlalu mahal/kompleks.
2. **Ulasan dan percakapan pelanggan** berbahasa Indonesia informal tidak dianalisis; keluhan terlambat ditangani.
3. **Akses pembiayaan** UMKM terhambat penilaian risiko yang tidak transparan; skoring berpotensi diskriminatif.
4. Pelaku usaha tidak tahu **kapan mempercayai** rekomendasi AI; adopsi rendah atau kepercayaan buta.
5. Praktik **MLOps** di perusahaan kecil tidak ada; model yang dibuat mahasiswa cepat usang.
6. Data usaha kecil berskala kecil dan berantakan; metode standar gagal.
7. Ekonomi syariah/koperasi membutuhkan analitik yang sesuai prinsip (transparansi, tanpa riba) tetapi jarang diteliti dengan AI.
8. Lulusan Informatika menjadi wirausaha tanpa **evidence-based product decision**.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| UMKM (pangan, ritel, jasa) termasuk usaha keluarga mahasiswa | pemilik masalah, sumber data (Restricted) |
| Koperasi, lembaga keuangan mikro, lembaga keuangan syariah | mitra masalah pembiayaan (perjanjian ketat) |
| Asosiasi UMKM, inkubator bisnis kampus | partner scaling dan rekrutmen partisipan |
| Fakultas ekonomi/bisnis di UAI | pakar domain, co-investigator (verifikasi) |
| Tempat Kerja Praktik mahasiswa (industri) | entry door Partner |
| Platform marketplace/POS lokal | partner data (2029+) |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Transaksi/penjualan UMKM | **Restricted** | data bisnis; agregasi; perjanjian tertulis |
| Ulasan publik produk/usaha | Public (teks) | hindari identitas pengulas saat rilis; cek ketentuan platform |
| Data pembiayaan/kredit | **Confidential** | hanya lewat mitra; audit fairness wajib |
| Survei pelaku usaha | Restricted | consent |
| Data marketplace agregat/publik | Public | catat keterbatasan |
| Data usaha sintetis | Public | untuk pengembangan metode |

## 5. Contoh research questions

- Pada data penjualan UMKM kurang dari 12 bulan, apakah model prediksi permintaan sederhana mengalahkan rata-rata bergerak secara praktis bermakna, dan pada kategori produk apa tidak? (C4)
- Bagaimana model bahasa menganalisis sentimen/keluhan ulasan berbahasa Indonesia informal dibanding anotasi manusia, dan apakah hasilnya mengubah tindakan pemilik usaha? (C1 + C3)
- Praktik MLOps minimum apa (monitoring, retraining) yang benar-benar dipakai UMKM setelah enam bulan, dan mengapa? (C2, studi kasus)
- Apakah penjelasan sederhana pada rekomendasi stok meningkatkan kepercayaan terkalibrasi pelaku usaha dibanding rekomendasi tanpa penjelasan? (C3, eksperimen)
- Bisakah skoring pembiayaan mikro dirancang adil terhadap kelompok usaha tertentu, dan apa trade-off akurasinya? (C3 + C4, data mitra)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Alat prediksi/rekomendasi berbiaya rendah (`ART-*`) | keputusan UMKM berbasis data |
| Dataset ulasan berbahasa Indonesia berlisensi jelas (`DS-*`) | riset NLP bisnis lokal |
| Paper (applied ML, IS, HCI, empirical SE) | posisi UAI di riset UMKM digital |
| Studi kasus adopsi | panduan bagi inkubator/asosiasi |
| Research brief ekonomi syariah + AI | kontribusi khas UAI |

## 7. Risiko etika dan privasi khas domain

- **Diskriminasi** dalam skoring kredit/pembiayaan; audit fairness dan manusia sebagai pengambil keputusan.
- **Data bisnis rahasia** partner; kebocoran merusak kepercayaan — Restricted/Confidential.
- **Manipulasi konsumen** lewat rekomendasi/harga dinamis; batas etika ditetapkan di G2.
- **Overclaiming manfaat** ekonomi dari pilot kecil; klaim sebatas bukti dan threats to validity.
- **Konflik kepentingan** bila usaha milik keluarga mahasiswa; ungkapkan di Research Pack.

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| Data Mining | eksplorasi transaksi; segmentasi |
| AI & Machine Learning | baseline prediksi permintaan; skoring dengan audit fairness |
| NLP | analisis ulasan/percakapan pelanggan |
| Rekayasa Perangkat Lunak / Proyek PL | prototype alat UMKM; praktik MLOps ringan |
| Kerja Praktik | masalah dan data dari industri (entry door Partner) |
| Interaksi Manusia–Komputer | user study pelaku usaha |
