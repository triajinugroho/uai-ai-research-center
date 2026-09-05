# Domain — Food (Pangan)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C2 AI Systems, Software & Security](../clusters/ai-systems-security.md) · [C4 Applied AI](../clusters/applied-ai.md) · [Domain Halal](halal.md) · [AIR-04 Cross-Faculty AI Model](../../research-os/03-ai-research-ecosystem/04-cross-faculty-ai-model.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `food` |
| Program | belum ada program tersendiri sampai 2030; dijalankan sebagai `proj-*` dan bagian `program-ai-halal` / `program-ai-health` |
| Klaster utama | C4 (prediksi kualitas, susut), C2 (IoT, sensor, data engineering), C1 (ekstraksi label gizi), C3 (nudging etis) |
| Prioritas roadmap | sel aktif 2028 (bersama Health) |

## 1. Mengapa domain ini untuk UAI

Pangan bersinggungan dengan dua domain lain yang menjadi kekuatan UAI: **halal** (bahan, proses, label) dan **kesehatan** (gizi). Dokumen diskusi menyebut Teknologi Pangan dan Gizi sebagai mitra lintas fakultas yang mungkin — verifikasi ketersediaannya. Pangan juga memberi masalah computing yang konkret dan berbiaya rendah untuk dipelajari: citra, sensor, deret waktu, dan label teks. Bagi Indonesia, ketahanan pangan, pengurangan susut, dan UMKM pangan adalah prioritas generik yang tidak memerlukan kutipan regulasi untuk dipahami urgensinya.

> **Catatan verifikasi.** Mitra internal (prodi pangan/gizi) dan mitra eksternal (pelaku pangan, koperasi, pasar): `[isi]`. Standar keamanan pangan yang relevan dipetakan saat riset dirancang, bukan dikutip di sini.

## 2. Problem space (masalah nyata)

1. **Susut pangan** pada rantai distribusi kecil (pasar, kantin, UMKM) tidak terukur; keputusan stok berbasis perkiraan.
2. Kualitas bahan pangan segar dinilai visual secara manual; tidak konsisten.
3. Label gizi dan komposisi pada kemasan sulit dibaca dan dibandingkan konsumen; data label tidak terstruktur.
4. **Rantai dingin** produk kecil tidak dipantau; kerusakan diketahui terlambat.
5. Pelaku pangan kecil tidak punya alat prediksi permintaan harian yang sederhana.
6. Program gizi komunitas sulit memantau asupan dan variasi menu.
7. Kantin kampus: sisa makanan, preferensi, dan keamanan pangan jarang dianalisis.
8. Informasi keamanan pangan berbahasa Indonesia untuk UMKM tersebar dan sulit dicari.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| Kantin/unit layanan pangan kampus | pemilik masalah awal, sumber data berisiko rendah |
| Prodi/fakultas pangan dan gizi di UAI | pakar domain, co-investigator (verifikasi) |
| UMKM pangan, koperasi, pedagang pasar | mitra masalah dan data (Restricted) |
| Lembaga sosial yang menjalankan program gizi/pangan | mitra evaluasi dampak |
| Pemerintah daerah/dinas terkait | partner scaling (2029+) |
| Penyedia sensor/IoT lokal | partner teknis |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Citra bahan pangan (dikumpulkan sendiri) | Public | tanpa identitas orang; lisensi ditetapkan saat rilis |
| Data sensor suhu/kelembapan rantai dingin | Public/Partner | metadata alat dan kalibrasi wajib dicatat |
| Data transaksi/penjualan pelaku pangan | **Restricted** | data bisnis partner; agregasi |
| Teks label gizi/komposisi | Public | cek hak merek saat rilis dataset |
| Data sisa makanan kantin | Internal | izin unit |
| Catatan asupan program gizi | **Restricted** | data pribadi kesehatan; ikuti [health.md](health.md) |

## 5. Contoh research questions

- Seberapa akurat klasifikasi citra kesegaran bahan pangan dibanding penilaian manusia, dan apakah ia stabil pada kondisi pencahayaan pasar? (C4)
- Apakah pemantauan sensor rantai dingin berbiaya rendah menghasilkan data yang cukup andal untuk memprediksi kerusakan lebih awal dari inspeksi manual? (C2 + C4)
- Model prediksi permintaan sederhana mana yang cukup baik untuk kantin/UMKM dengan data kurang dari satu tahun, dibanding rata-rata bergerak? (C4)
- Bisakah ekstraksi label gizi dari citra kemasan menghasilkan tabel terstruktur dengan presisi memadai untuk perbandingan produk? (C1)
- Apakah nudging berbasis data di kantin (informasi gizi/sisa makanan) mengubah perilaku tanpa manipulasi yang tidak etis? (C3)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Dataset citra pangan lokal berlisensi jelas | riset CV pangan Indonesia |
| Pipeline IoT + data berkualitas riset (`ART-*`) | template untuk domain lain |
| Alat prediksi susut/permintaan untuk UMKM | pengurangan kerugian |
| Paper (CV, IoT, applied ML) | kolaborasi lintas fakultas |
| Research brief untuk unit kampus/lembaga sosial | keputusan operasional berbasis bukti |

## 7. Risiko etika dan privasi khas domain

- **Keamanan pangan**: sistem tidak boleh menyatakan makanan "aman" tanpa validasi laboratorium; klaim sebatas indikasi.
- **Data bisnis partner** (penjualan, pemasok) — Restricted; agregasi sebelum analisis.
- **Nudging** perilaku konsumsi harus transparan dan dapat ditolak.
- **Data gizi individu** = data kesehatan; ikuti aturan domain Health.
- **Keterwakilan**: dataset dari kantin kampus belum tentu mewakili pasar; nyatakan threats to validity.

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| AI & Machine Learning | baseline klasifikasi citra pangan; prediksi deret waktu |
| Data Mining | eksplorasi data transaksi kantin |
| Proyek Perangkat Lunak | prototype pemantauan rantai dingin / prediksi stok |
| Basis Data | skema data sensor dan label |
| NLP | ekstraksi label gizi/komposisi |
| Interaksi Manusia–Komputer | evaluasi nudging dan antarmuka pelaku usaha |
