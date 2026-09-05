# C4 — Applied AI for Human Flourishing

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [AIR-04 Cross-Faculty AI Model](../../research-os/03-ai-research-ecosystem/04-cross-faculty-ai-model.md) · [AIR-05 Demand–Supply Marketplace](../../research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) · [Domains](../domains/education.md)

| Field | Nilai |
|---|---|
| Kode | **C4** |
| Peran AI | **AI Application** — menerapkan AI ke domain: pendidikan, halal, kesehatan, pangan, pemerintahan, bisnis, dampak sosial |
| Label GitHub | `cluster:applied` |
| Tim GitHub | `@applied-ai` |
| Program terkait | `program-ai-education` (2027), `program-ai-halal` (2028), `program-ai-health` (2028) |
| Model kolaborasi | **Domain Problem + Data + AI Capability + Evaluation + Impact** ([AIR-04](../../research-os/03-ai-research-ecosystem/04-cross-faculty-ai-model.md)) |

## 1. Scope

Klaster ini meneliti **apakah dan bagaimana AI benar-benar membantu manusia** di tujuh domain roadmap. Kata kuncinya adalah *human flourishing*: manfaat yang dapat diukur bagi mahasiswa, konsumen, pasien, petani/pelaku pangan, warga, pelaku usaha, dan komunitas — bukan sekadar akurasi model. Setiap riset C4 wajib memiliki **pemangku kepentingan yang dapat disebut**, **keputusan yang berubah** bila riset berhasil, dan **evaluasi dampak**, bukan hanya evaluasi model.

C4 adalah klaster dengan jumlah riset terbanyak, karena pintu masuk **Problem** dan **Partner** hampir selalu jatuh ke sini. Ia bergantung pada tiga klaster lain: model dan data dari [C1](ai-models-data-knowledge.md), sistem dari [C2](ai-systems-security.md), dan penilaian etika/manusia dari [C3](responsible-human-ai.md).

## 2. Research questions besar 2026–2030

1. Pada masalah domain apa di Indonesia AI memberi **peningkatan yang praktis bermakna** dibanding baseline sederhana (aturan, statistik, praktik manusia saat ini) — dan pada masalah apa tidak?
2. Bagaimana **mengukur dampak** penerapan AI di lapangan (kampus, UMKM, layanan publik) dengan desain yang cukup kuat (quasi-experiment, pilot terkontrol) dalam batas TA?
3. Faktor apa yang menentukan **adopsi** sistem AI oleh pemangku kepentingan non-teknis di Indonesia, dan bagaimana desain riset dapat mengantisipasinya?
4. Bagaimana **data domain berskala kecil** (kampus, satu UMKM, satu puskesmas) tetap dapat menghasilkan bukti yang valid — metode apa yang cocok?
5. Apakah solusi AI yang dikembangkan untuk satu konteks (mis. satu kampus) **dapat ditransfer** ke konteks lain, dan apa yang membuatnya gagal?
6. Bagaimana kebutuhan khas masyarakat Muslim Indonesia (halal, zakat/wakaf, pendidikan Islam) dapat dilayani AI dengan **standar bukti yang sama** ketatnya dengan domain lain?
7. Bagaimana model kolaborasi lintas fakultas dan partner (**Domain Problem + Data + AI Capability + Evaluation + Impact**) dijalankan tanpa menurunkan kualitas gate?

## 3. Example topics (konteks Indonesia/UAI)

1. Early warning kesulitan belajar mahasiswa dari data akademik teranonimisasi: seberapa akurat dan seberapa berguna bagi dosen wali ([education](../domains/education.md)).
2. Klasifikasi citra produk/label halal untuk membantu konsumen dan pengawas (lihat [UIAI-2026-003](../../research-backlog/problems/UIAI-2026-003-halal-product-image-classification.md)).
3. Skrining dini risiko kesehatan berbasis kuesioner + model sederhana untuk layanan kesehatan kampus/komunitas ([health](../domains/health.md)).
4. Prediksi kualitas dan susut pangan dari data sensor/citra untuk pelaku pangan kecil ([food](../domains/food.md)).
5. Klasifikasi dan prioritisasi pengaduan warga untuk unit layanan publik ([government](../domains/government.md)).
6. Prediksi permintaan dan rekomendasi stok untuk UMKM dengan data transaksi kecil ([business](../domains/business.md)).
7. Analitik penyaluran zakat/wakaf/filantropi untuk lembaga sosial ([social-impact](../domains/social-impact.md)).
8. Asisten belajar berbasis RAG untuk satu mata kuliah: eksperimen terkontrol terhadap hasil belajar.
9. Deteksi anomali konsumsi energi/air di kampus untuk keberlanjutan.
10. Rekomendasi jalur karier/mata kuliah pilihan berbasis data alumni teranonimisasi.
11. Chatbot layanan mahasiswa: evaluasi kegunaan nyata vs baseline FAQ statis.
12. Estimasi kebutuhan gizi dari citra makanan untuk program gizi komunitas (lintas fakultas Gizi/Teknologi Pangan — verifikasi mitra).

## 4. Related courses

| Mata kuliah | Kontribusi ke C4 | Mode |
|---|---|---|
| AI & Machine Learning (sem. V) | model terapan + baseline | E/R |
| Data Mining (sem. IV) | eksplorasi data domain, feature | E/R |
| NLP | aplikasi teks domain | R |
| Proyek Perangkat Lunak (sem. VI) | prototype sistem domain | R |
| Kerja Praktik (sem. VI) | masalah nyata dari industri/instansi | E (problem discovery; entry door Problem/Partner) |
| Interaksi Manusia–Komputer | evaluasi pengguna domain | E |
| Metodologi Penelitian / TA | design science, case study, quasi-experiment | R (Prove / Contribute) |

Detail: [research-based-learning](../../research-based-learning/README.md).

## 5. Kebutuhan data dan compute

| Kebutuhan | Isi |
|---|---|
| Data | hampir selalu **data partner atau data internal** → sensitivitas tinggi; kartu dataset dengan Privacy `Restricted/Confidential`; perjanjian tertulis untuk data partner; data publik (produk halal, statistik pemerintah, korpus) untuk memulai |
| Compute | rendah–menengah; sebagian besar model tabular/klasik; citra dan NLP memakai model pra-latih dari [C1](ai-models-data-knowledge.md) |
| Akses lapangan | waktu pemangku kepentingan untuk wawancara, uji coba, evaluasi dampak — sering menjadi bottleneck utama, catat sebagai Research Risk |
| Etika | penilaian dampak manusia dari [C3](responsible-human-ai.md) sebelum deployment apa pun |

## 6. Output yang diharapkan

| Jenis output | Contoh |
|---|---|
| Prototype / produk / HKI | sistem klasifikasi halal; dashboard dosen wali; alat prediksi UMKM |
| Paper (`PUB-*`) | studi kasus, design science, evaluasi lapangan, replikasi lintas konteks |
| Dataset (`DS-*`) | dataset domain berlisensi jelas bila aman dibuka (mis. citra produk publik) |
| Research brief | rekomendasi untuk unit kampus, instansi, partner |
| Competition project | hasil lomba yang diuji dengan gate yang sama |

## 7. Entry door yang umum

**Problem** dan **Partner** — dan **Competition**. Karena pintu ini rawan *solution-first*, G2 diperketat: masalah harus diformulasikan sebelum algoritma ("mengapa X perlu diprediksi?" sebelum "pakai Random Forest"; lihat [OPS-03](../../research-os/06-execution-os/03-research-gates.md)).

## 8. Keterkaitan program dan klaster lain

- **Konsumen** kapabilitas C1 (model, korpus), C2 (deployment, keandalan), C3 (etika, user study).
- **Pemasok** masalah dan data nyata kembali ke tiga klaster lain — inilah loop *problem lebih berkualitas → mahasiswa berikutnya mendapat research environment lebih baik*.
- Program: `program-ai-education`, `program-ai-halal`, `program-ai-health` adalah program C4; domain Food, Government, Business, Social Impact dijalankan sebagai `proj-*` sampai memenuhi syarat program.

## 9. Topik yang sengaja tidak kita kejar (2026–2030)

| Tidak dikejar | Alasan (Occam) |
|---|---|
| Aplikasi tanpa pemangku kepentingan yang dapat dihubungi | tidak bisa lolos G2 dan tidak bisa dievaluasi dampaknya |
| Aplikasi yang membutuhkan data partner tanpa perjanjian tertulis | risiko privasi/hukum; bertentangan dengan [SECURITY.md](../../SECURITY.md) |
| Sistem klinis berisiko tinggi yang menggantikan keputusan tenaga kesehatan | di luar kompetensi, regulasi, dan etika; kami mendukung keputusan, bukan menggantikan |
| Membangun "super-app" lintas domain | terlalu luas untuk TA; fokus satu keputusan, satu pemangku kepentingan |
| Mengulang aplikasi yang sudah matang di pasar tanpa pertanyaan baru | tidak ada gap; gagal G4 |
| Skoring kredit/sosial yang berpotensi diskriminatif tanpa audit fairness | bertentangan dengan Responsible AI |

Fokus kami: **satu masalah nyata, satu pemangku kepentingan, satu keputusan yang berubah, dengan bukti yang dapat diperiksa.**
