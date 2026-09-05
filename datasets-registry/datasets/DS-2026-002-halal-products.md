# DS-2026-002 — Halal Product Packaging Images

> **Status** contoh ilustratif — belum ada data riil · Draft v0.1 (2026-09) · **Terkait** [REGISTRY.md](../REGISTRY.md) · [Registry README](../README.md) · [TPL-05](../../research-os/08-templates/05-dataset-registry-template.md) · [LICENSING.md](../../LICENSING.md) · [UIAI-2026-003](../../research-backlog/problems/UIAI-2026-003-halal-product-image-classification.md) · [Domain Halal](../../research-roadmap/domains/halal.md)

## Kartu dataset

| Field | Nilai |
|---|---|
| **Dataset ID** | DS-2026-002 |
| **Name** | Halal Product Packaging Images (with label annotations) |
| **Domain** | Halal |
| **Source** | UAI (dikumpulkan tim riset di ruang publik/ritel) + Partner (citra dari UMKM/pengawas, bila ada perjanjian) |
| **Owner** | `[isi: dosen/unit penanggung jawab; partner untuk bagian Partner]` |
| **Size** | `[isi: jumlah citra; target awal 200–500, target program 5.000+]` |
| **Modality** | Image (foto kemasan) + Text (transkripsi label/komposisi hasil OCR & koreksi manual) + anotasi (indikator halal, bounding box logo/teks) |
| **License** | Bagian publik: **CC BY 4.0** setelah review hak merek dan IP review; bagian Partner: no public license |
| **Privacy** | **Public** (bagian UAI, tanpa orang/wajah/identitas) / **Restricted** (bagian Partner) |
| **Potential Task** | Image classification, object detection (logo/label), OCR + information extraction (komposisi bahan), robustness evaluation (kondisi foto) |
| **Related Projects** | [UIAI-2026-003](../../research-backlog/problems/UIAI-2026-003-halal-product-image-classification.md); calon: knowledge graph bahan (C1) |
| **Quality Notes** | `[isi setelah pengumpulan]` — catat: distribusi kategori produk (besar vs UMKM), kondisi pencahayaan/sudut, duplikasi produk yang sama, kualitas OCR, agreement antar-anotator, versi pedoman anotasi |
| **Access** | Bagian publik: unduh dari `[isi: Hugging Face/Kaggle org UAI]` setelah rilis; sebelum rilis: minta ke Owner dengan Research ID. Bagian Partner: hanya lewat perjanjian |
| **Possible Research Questions** | (1) Seberapa akurat klasifikasi indikator halal dibanding OCR + aturan? (2) Kondisi foto apa yang paling menurunkan kinerja? (3) Bisakah ekstraksi komposisi bahan dari citra label dipetakan ke basis pengetahuan bahan dengan presisi memadai? |
| **Physical Location** | Sebelum rilis: institutional storage UAI `[isi]`; setelah rilis: `[isi: Hugging Face/Kaggle]`; bagian Partner: server institusi/lingkungan mitra |
| **Review Date** | `[isi]` |
| **Status** | contoh ilustratif — belum ada data riil |

## Protokol pengumpulan (ringkas)

1. Foto diambil tim di ritel/pasar dengan izin pengelola lokasi bila diperlukan; **tanpa wajah, orang, atau identitas** pihak lain.
2. Setiap citra diberi metadata: kategori produk, sumber lokasi (kategori, bukan alamat), kondisi pencahayaan, perangkat.
3. Anotasi mengikuti pedoman tertulis; indikator divalidasi pakar domain `[isi]`; agreement antar-anotator dilaporkan.
4. Sampling produk UMKM disengaja agar dataset tidak bias ke produk besar.
5. Sebelum rilis publik: **IP review** singkat (hak merek/citra produk) bersama `@directors` dan unit HKI/hukum ([LICENSING.md](../../LICENSING.md) §6); bila diperlukan, rilis terbatas untuk riset.

## Sensitivitas dan risiko

| Risiko | Mitigasi |
|---|---|
| Hak merek pada citra kemasan | konsultasi unit HKI; lisensi/rilis terbatas bila perlu |
| Data partner (resep/proses) ikut terfoto | bagian Partner dipisah, Restricted; tidak pernah di GitHub |
| Sistem dianggap menetapkan status halal | dataset dan model diberi disclaimer: indikasi pra-skrining, bukan keputusan |
| Bias kategori/kondisi | laporkan distribusi; evaluasi per segmen |
