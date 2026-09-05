# UIAI-2026-003 — Klasifikasi Citra Produk/Label Halal

> **Status** Draft v0.1 (2026-09) · **contoh ilustratif** · **Terkait** [BACKLOG.md](../BACKLOG.md) · [TPL-04](../../research-os/08-templates/04-research-backlog-template.md) · [C4 Applied AI](../../research-roadmap/clusters/applied-ai.md) · [Domain Halal](../../research-roadmap/domains/halal.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md)

| Field | Nilai |
|---|---|
| **Research ID** | UIAI-2026-003 |
| **Judul** | Klasifikasi citra produk/label halal |
| **Cluster** | C4 Applied AI for Human Flourishing (primer) · C1 AI Models, Data & Knowledge (sekunder: data & evaluasi) — label `cluster:applied` |
| **Domain** | Halal |
| **Problem owner** | `[isi: unit kajian halal / komunitas konsumen / asosiasi UMKM]` |
| **Potential dataset** | [DS-2026-002 Halal Products](../../datasets-registry/datasets/DS-2026-002-halal-products.md) (Public/Partner) |
| **Research maturity** | Idea |
| **Related courses** | AI & Machine Learning; Metodologi Penelitian; pendukung: Proyek Perangkat Lunak, NLP (OCR/teks label) |
| **Potential output** | TA; paper (computer vision terapan); dataset `DS-*`; prototype aplikasi |
| **Priority** | P2-medium |
| **Entry door** | Course Project |
| **Issue** | `#[isi]` |

## Problem statement

Konsumen Muslim dan pengawas menghadapi volume produk yang besar dengan label yang beragam (logo, teks komposisi, bahasa campur, kualitas cetak). Verifikasi status halal dari kemasan di lapangan lambat dan bergantung pada ketelitian manusia. Klasifikasi citra dapat membantu **pra-skrining** — menandai produk yang perlu diperiksa lebih lanjut — tetapi belum diketahui seberapa akurat pendekatan itu pada kondisi foto nyata (pencahayaan pasar, kemasan tertekuk, produk UMKM), dibanding baseline OCR + aturan, dan apa risiko kesalahannya bagi konsumen dan pelaku usaha. Sistem **tidak** dimaksudkan menetapkan status halal; keputusan tetap pada manusia/otoritas.

## Why it matters / stakeholder

| Pemangku kepentingan | Keputusan yang berubah |
|---|---|
| Konsumen | produk mana yang perlu dicek lebih lanjut sebelum membeli |
| Pengawas/auditor | prioritas pemeriksaan di lapangan |
| UMKM | umpan balik tentang kejelasan label mereka |
| Program `program-ai-halal` (2028) | dataset dan baseline pertama |

## What we know

Ringkasan awal: klasifikasi citra kemasan dan OCR label adalah tugas computer vision yang mapan; penerapan khusus untuk indikator halal dan produk Indonesia jarang dilaporkan dengan dataset terbuka; kesenjangan utama adalah data yang representatif dan evaluasi pada kondisi nyata. **Literatur awal: `[isi saat G3]`.**

## Candidate research questions

1. Seberapa akurat model klasifikasi citra mengenali indikator status halal pada kemasan dibanding baseline OCR + aturan kata kunci, pada dataset yang mencakup produk UMKM dan kondisi foto beragam?
2. Pada kondisi apa (pencahayaan, sudut, kemasan rusak, logo tidak standar) model paling sering gagal, dan apakah kegagalan itu berbeda antara produk besar dan UMKM?
3. Apakah pra-skrining otomatis mengurangi waktu pemeriksaan manusia tanpa menaikkan false negative yang merugikan konsumen?

## Possible data & sensitivity

| Data | Sumber | Sensitivitas | Syarat |
|---|---|---|---|
| Citra kemasan produk difoto tim di ruang publik/ritel | dikumpulkan sendiri | Public (setelah review) | tanpa wajah/orang; izin lokasi bila diperlukan; cek hak merek sebelum rilis dataset |
| Daftar produk bersertifikat yang dipublikasikan otoritas | publik | Public | cek ketentuan penggunaan; catat tanggal pengambilan |
| Citra dari partner (UMKM/pengawas) | partner | **Restricted/Confidential** | perjanjian tertulis; tidak di GitHub |
| Anotasi label (indikator, bounding box) | dibuat tim + validasi pakar | mengikuti citra | pedoman anotasi; agreement |

## Candidate mentor

`[isi: dosen computer vision / ML terapan]`; pakar domain halal `[isi]`.

## Risks

| Risiko | Mitigasi |
|---|---|
| Sistem dianggap "memfatwakan" status halal | output eksplisit sebagai indikasi pra-skrining; disclaimer; evaluasi false positive/negative |
| Dataset bias ke produk besar | sampling produk UMKM disengaja; laporkan kinerja per segmen |
| Hak merek/citra saat rilis dataset | konsultasi unit HKI/hukum; rilis terbatas bila perlu ([LICENSING.md](../../LICENSING.md)) |
| Akurasi tinggi di lab, buruk di lapangan | uji pada foto kondisi nyata; threats to validity eksternal |
| Regulasi berubah | tidak mengutip regulasi dalam model; pakar domain memvalidasi indikator |

## Next evidence

Untuk naik ke G2: pernyataan kebutuhan dari minimal satu pemangku kepentingan (unit kajian halal/komunitas/asosiasi), rencana pengumpulan 200–500 citra awal beserta protokol izin, dan daftar indikator yang divalidasi pakar.
