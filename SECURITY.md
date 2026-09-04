# SECURITY — Keamanan Data, Privasi, dan Pelaporan

## 1. Prinsip utama

**Data mentah yang sensitif tidak pernah otomatis masuk GitHub.** Repository hanya menyimpan metadata, kode, dan artefak yang aman untuk dibagikan pada tingkat aksesnya.

## 2. Klasifikasi

| Kelas | Contoh | Boleh di GitHub? |
|---|---|---|
| **PUBLIC** | Framework, template, kode open-source, metadata dataset publik, sitasi publikasi | Ya, repo public |
| **INTERNAL** | Riset berjalan, naskah belum terbit, pekerjaan mahasiswa, roadmap internal | Ya, repo private/internal |
| **RESTRICTED** | Data partner rahasia, dataset sensitif, data pribadi (mahasiswa, pasien, pengguna), data kesehatan, proyek komersial | **Tidak.** Hanya kartu metadata di `datasets-registry/` |

## 3. Yang dilarang di-commit

- Data pribadi (nama, NIM, email, nomor telepon, alamat, identitas) dalam bentuk mentah, termasuk di notebook output dan log.
- Kredensial: API key, token, password, file `.env`, kunci SSH, kredensial cloud.
- Dataset partner atau dataset dengan perjanjian akses terbatas.
- PDF publisher yang haknya tidak mengizinkan redistribusi (lihat [LICENSING.md](LICENSING.md)).
- Model weights hasil pelatihan pada data sensitif tanpa review.

Gunakan `.gitignore` (`data/raw/`, `data/private/`, format model) dan simpan data fisik di server institusi, Hugging Face, Kaggle, Drive, atau cloud sesuai kartu dataset.

## 4. Praktik wajib untuk riset dengan data manusia

- Anonimisasi/pseudonimisasi sebelum analisis; simpan kunci pemetaan di luar repository.
- Persetujuan (consent) dan izin institusi/komite etik didokumentasikan di `docs/ethics.md`.
- Nilai privasi pada kartu dataset (`Public / Restricted / Confidential`) harus diisi sebelum G5 Method Ready.
- Prompt ke layanan AI eksternal **tidak boleh** memuat data pribadi atau data partner.

## 5. Jika ada kebocoran

1. Jangan hanya menghapus file di commit berikutnya; riwayat git tetap menyimpannya. Hubungi `@maintainers` untuk menulis ulang riwayat dan mencabut kredensial.
2. Rotasi semua kredensial yang terekspos.
3. Laporkan kepada pemilik data/partner sesuai perjanjian.
4. Catat insiden di Issue **Research Risk** (private) dan di risk register riset.

## 6. Melaporkan kerentanan atau insiden

Kirim laporan secara privat kepada `@directors`/`@maintainers` (gunakan fitur *Report a vulnerability* GitHub bila diaktifkan, atau kontak resmi pusat riset). Jangan membuka Issue publik untuk kerentanan yang belum ditangani. Kami akan mengonfirmasi penerimaan dan menindaklanjuti sesegera mungkin.

## 7. Cakupan

Kebijakan ini berlaku untuk semua repository di bawah UAI AI Research Center, termasuk repo riset `proj-*` dan `program-*`.
