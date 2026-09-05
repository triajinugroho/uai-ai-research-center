# Domain — Halal

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C1 AI Models, Data & Knowledge](../clusters/ai-models-data-knowledge.md) · [C2 AI Systems, Software & Security](../clusters/ai-systems-security.md) · [C4 Applied AI](../clusters/applied-ai.md) · [alignment/indonesia.md](../alignment/indonesia.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `halal` |
| Program | `program-ai-halal` (dibuka 2028, setelah ada mitra) |
| Klaster utama | C4 (klasifikasi, verifikasi), C1 (ekstraksi informasi, knowledge graph), C2 (traceability); C3 untuk kepercayaan konsumen |
| Prioritas roadmap | sel **C4 × Halal** dibuka 2026 dengan data publik; program 2028 |

## 1. Mengapa domain ini untuk UAI

Halal adalah domain tempat identitas UAI sebagai kampus Islam bertemu dengan kebutuhan nyata masyarakat Indonesia: konsumen ingin tahu status produk, pelaku usaha kecil kesulitan memenuhi persyaratan, dan pengawas kewalahan dengan volume produk. Domain ini juga kaya masalah computing: citra label, teks komposisi bahan, pengetahuan tentang bahan dan proses, serta rantai pasok yang perlu ditelusuri. Untuk UAI, halal adalah **domain pembeda**: sedikit pusat riset AI yang menggarapnya dengan standar bukti yang ketat.

> **Catatan verifikasi.** Regulasi, otoritas sertifikasi, dan skema halal Indonesia berubah; dokumen ini sengaja tidak mengutip nomor regulasi. Petakan ke dokumen kebijakan resmi terkini saat roadmap review dan sebelum menjalin mitra. Ketersediaan mitra internal (mis. unit kajian halal UAI, fakultas terkait): `[isi]`.

## 2. Problem space (masalah nyata)

1. Konsumen kesulitan memverifikasi status halal produk dari **label/kemasan** di lapangan, terutama produk impor atau UMKM.
2. Daftar **komposisi bahan** pada label ditulis beragam (istilah, bahasa campur, singkatan); pemetaan ke status bahan memerlukan pengetahuan pakar.
3. **UMKM pangan** tidak memahami persyaratan dokumen dan proses; biaya konsultasi tinggi.
4. Pengawas/auditor menghadapi volume produk besar; **prioritisasi pemeriksaan** dilakukan manual.
5. Informasi halal tersebar di berbagai sumber; tidak ada **basis pengetahuan** terstruktur yang dapat dipakai sistem.
6. **Traceability** rantai pasok (bahan → proses → produk) sulit diaudit; data partner sensitif.
7. Klaim halal palsu/menyesatkan di pemasaran daring sulit dideteksi.
8. Edukasi halal bagi konsumen muda kurang menarik dan tidak personal.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| Konsumen Muslim (mahasiswa UAI sebagai kelompok awal) | pengguna, partisipan user study |
| UMKM pangan/kosmetik | pemilik masalah, sumber data proses (Restricted) |
| Lembaga/unit kajian halal di kampus | pakar domain, validasi label |
| Otoritas/lembaga sertifikasi dan auditor halal | pemilik masalah prioritisasi (2028+, via perjanjian) |
| Asosiasi UMKM, pemerintah daerah | partner scaling |
| Fakultas lain: Teknologi Pangan, Gizi, Hukum, Ekonomi | kolaborasi lintas fakultas (verifikasi ketersediaan) |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Citra kemasan/label produk yang difoto di ruang publik oleh tim sendiri | Public/Partner | hindari wajah/orang; cek hak merek untuk publikasi dataset; lihat [DS-2026-002](../../datasets-registry/datasets/DS-2026-002-halal-products.md) |
| Daftar produk bersertifikat yang dipublikasikan otoritas | Public | cek ketentuan penggunaan data |
| Basis pengetahuan bahan (sumber publik, literatur) | Public | kurasi pakar |
| Data proses produksi UMKM/partner | **Confidential** | tidak pernah di GitHub; hanya kartu metadata |
| Data audit/sertifikasi | Confidential | perjanjian tertulis |
| Survei kepercayaan konsumen | Restricted | consent |

## 5. Contoh research questions

- Seberapa akurat klasifikasi citra label/produk mengenali indikator status halal dibanding baseline OCR + aturan, dan pada kondisi foto apa ia gagal? (C4) — lihat [UIAI-2026-003](../../research-backlog/problems/UIAI-2026-003-halal-product-image-classification.md).
- Apakah ekstraksi komposisi bahan dari teks label berbahasa campur dapat dipetakan ke knowledge graph bahan dengan presisi yang memadai untuk pra-skrining? (C1)
- Fitur apa yang paling memprediksi kebutuhan pemeriksaan lanjutan pada produk UMKM, dan apakah prioritisasi otomatis lebih efisien daripada urutan pendaftaran? (C4, data partner)
- Bagaimana konsumen Muslim muda menyikapi verifikasi berbantuan AI — apakah kepercayaan mereka terkalibrasi dengan akurasi sistem? (C3)
- Arsitektur audit trail seperti apa yang memenuhi kebutuhan traceability tanpa membuka data proses partner? (C2)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Dataset citra label produk berlisensi jelas (`DS-*`) | fondasi riset halal-AI di Indonesia |
| Knowledge graph bahan halal (`ART-*`) | pra-skrining lebih cepat bagi UMKM/pengawas |
| Prototype aplikasi verifikasi konsumen | edukasi dan perlindungan konsumen |
| Paper (computer vision, IE, HCI) | posisi UAI di riset halal-AI |
| Research brief untuk otoritas/asosiasi | masukan kebijakan berbasis bukti |

## 7. Risiko etika dan privasi khas domain

- **Klaim keagamaan oleh sistem**: sistem tidak boleh "memfatwakan" status halal; output adalah *indikasi* untuk manusia/otoritas. Sertakan disclaimer dan evaluasi false positive/negative secara eksplisit.
- **Merugikan UMKM** bila sistem salah melabeli produk; evaluasi dampak dan mekanisme koreksi wajib.
- **Data partner rahasia** (resep, proses) — Confidential; perjanjian sebelum akses.
- **Hak merek/citra produk** saat merilis dataset; konsultasi unit HKI/hukum ([LICENSING.md](../../LICENSING.md)).
- **Bias dataset** terhadap produk besar/terkenal; sampling produk UMKM harus disengaja.

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| AI & Machine Learning | baseline klasifikasi citra label; pipeline OCR |
| NLP | ekstraksi komposisi bahan; normalisasi istilah |
| Data Mining | eksplorasi daftar produk bersertifikat |
| Basis Data | skema knowledge graph bahan |
| Proyek Perangkat Lunak / Pengujian PL | prototype aplikasi verifikasi + pengujian |
| Interaksi Manusia–Komputer | user study kepercayaan konsumen |
| Etika Profesi | analisis batas klaim sistem terhadap otoritas |
