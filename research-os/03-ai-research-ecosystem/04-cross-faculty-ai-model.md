# Cross-Faculty AI Model — Domain Problem + Data + AI Capability + Evaluation + Impact

> **ID** AIR-04 · **Paket** 03 AI Research Ecosystem · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kepala pusat riset, Dekan, Kaprodi dan dosen fakultas/prodi mitra (Gizi, Teknologi Pangan, Psikologi, Hukum, Ekonomi, Bahasa, Komunikasi, dll.), dosen Informatika, unit kerja sama
> **Terkait** [AIR-01 AI Research Center Concept](01-ai-research-center-concept.md) · [AIR-02 AI Research Clusters](02-ai-research-clusters.md) · [AIR-03 Faculty Research Alignment](03-faculty-research-alignment.md) · [AIR-05 Demand–Supply Marketplace](05-research-demand-supply-marketplace.md) · [ARC-06 Research Output Taxonomy](../02-academic-architecture/06-research-output-taxonomy.md) · [MET-07 Research Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [SECURITY.md](../../SECURITY.md) · [LICENSING.md](../../LICENSING.md)

## 1. Mengapa lintas fakultas

Masalah yang paling layak diteliti dengan AI jarang berada di dalam Informatika. Ia ada di klinik gizi, dapur produksi pangan, ruang konseling, kantor hukum, UMKM, kelas bahasa, dan ruang redaksi. Informatika membawa **kapabilitas AI**; fakultas lain membawa **masalah, data, cara mengevaluasi, dan dampak**. Tanpa fakultas lain, riset AI Informatika berisiko menjadi latihan algoritma pada dataset publik. Tanpa Informatika, fakultas lain berisiko memakai AI sebagai kotak hitam tanpa evaluasi.

Klaster utama kolaborasi ini adalah **C4 Applied AI for Human Flourishing**, dengan C3 (manusia dan nilai) dan C1 (data dan model) sebagai sekunder. Domain roadmap: Education, Halal, Health, Food, Government, Business, Social Impact.

## 2. Model lima komponen

Setiap riset lintas fakultas harus bisa mengisi lima komponen berikut **sebelum** lolos G2 Problem Ready. Komponen yang kosong adalah tanda kolaborasi belum siap.

```
 DOMAIN PROBLEM  +  DATA  +  AI CAPABILITY  +  EVALUATION  +  IMPACT
 (fakultas mitra)  (mitra/     (Informatika)     (mitra +        (mitra +
                    bersama)                      Informatika)    pusat riset)
```

| Komponen | Pertanyaan | Isi minimum | Pemilik utama | Pemilik pendukung |
|---|---|---|---|---|
| **Domain Problem** | Masalah nyata apa, siapa yang peduli, keputusan apa yang berubah bila terjawab? | Problem Brief dalam bahasa domain; stakeholder; ukuran keberhasilan menurut domain (bukan metrik ML) | Dosen/unit fakultas mitra (*problem owner*) | Informatika membantu menerjemahkan ke pertanyaan yang dapat diuji |
| **Data** | Data apa yang ada atau bisa dikumpulkan, siapa pemiliknya, apa batas privasinya? | Kartu dataset ([TPL-05](../08-templates/05-dataset-registry-template.md)): sumber, ukuran, modality, privasi, consent, lisensi; data fisik di luar GitHub | Fakultas mitra (*data owner*) atau bersama | Informatika: skema, anonimisasi, pipeline; pusat riset: data governance review |
| **AI Capability** | Pendekatan AI apa yang masuk akal, dengan baseline apa? | Research Design Card ([TPL-08](../08-templates/08-research-design-card.md)); baseline paling sederhana (sering aturan/regresi/praktik manual saat ini); metrik teknis | Dosen/mahasiswa Informatika | Mitra memverifikasi asumsi domain |
| **Evaluation** | Bagaimana kita tahu ini benar-benar bekerja — secara teknis dan secara domain? | Dua lapis: metrik teknis (Informatika) + validasi domain (ahli/pengguna mitra: uji dengan ahli gizi, panel hukum, pengguna layanan); threats to validity dari kedua sisi | Bersama; validasi domain dipimpin mitra | Reviewer gate dari dua klaster |
| **Impact** | Apa yang berubah bila berhasil, dan bagaimana kita mengukurnya? | Impact statement; jalur adopsi (prototype, brief, kebijakan, produk); indikator dampak domain | Mitra (dampak) + pusat riset (jalur Scale) | Informatika: artefak yang dapat dipelihara |

Prinsip pembagian pemilik: **yang paling memahami komponen itu yang memilikinya**. Informatika tidak memiliki masalah gizi; ahli gizi tidak memiliki baseline model. Kolaborasi gagal ketika satu pihak mencoba memiliki semuanya.

## 3. Contoh per fakultas/prodi

Nama fakultas/prodi mengikuti dokumen sumber; nama resmi unit dan ketersediaan data mengikuti struktur UAI (`[isi]`). Semua contoh adalah ilustrasi arah, bukan riset yang sudah disepakati.

| Fakultas/Prodi mitra | Domain problem | Data yang mungkin | AI capability | Evaluation | Impact | Klaster (primer/sekunder) · Domain |
|---|---|---|---|---|---|---|
| **Gizi** | Estimasi asupan gizi dari foto makanan lokal Indonesia tidak akurat dengan aplikasi global | Citra makanan lokal dengan label porsi/gizi oleh ahli; tabel komposisi pangan | Klasifikasi/estimasi porsi dari citra; baseline: lookup manual + rata-rata porsi | Metrik error estimasi vs penilaian ahli gizi; uji pada menu nyata; bias jenis makanan | Alat bantu konseling gizi; dataset citra makanan lokal | C4/C1 · Health, Food |
| **Teknologi Pangan** | Verifikasi status bahan dan proses halal pada produk UMKM memakan waktu | Katalog produk & bahan (contoh sumber: *halal products*), daftar bahan kritis, dokumen sertifikasi | Ekstraksi informasi dari label; penalaran berbasis ontologi bahan; RAG regulasi halal | Presisi/recall ekstraksi; validasi auditor halal; kasus tepi (bahan turunan) | Asisten pra-audit UMKM; ontologi bahan halal terbuka | C4/C1 · Halal, Food |
| **Psikologi** | Deteksi dini kebutuhan dukungan kesejahteraan mahasiswa dari self-report rutin | Kuesioner self-report (anonim, consent), data layanan konseling agregat | Model risiko sederhana; NLP pada teks bebas; baseline: skor kuesioner standar | Validitas terhadap instrumen psikologi; fairness antar kelompok; false positive cost | Prioritas layanan konseling; kebijakan privasi data mahasiswa | C3/C4 · Health, Education |
| **Hukum** | UMKM dan masyarakat kesulitan memahami regulasi (perizinan, halal, ketenagakerjaan) | Korpus regulasi publik; FAQ layanan hukum; pertanyaan pengguna (anonim) | Asisten tanya-jawab berbasis RAG dengan sitasi pasal; baseline: pencarian kata kunci | Grounding (jawaban bersumber), akurasi hukum oleh panel dosen hukum, uji kebergunaan | Klinik hukum berbantuan AI; brief kebijakan | C4/C1 · Government, Business |
| **Ekonomi / Bisnis** | UMKM binaan tidak punya prediksi permintaan dan pengelolaan stok | Data transaksi UMKM (anonim, perjanjian), harga, musim | Peramalan sederhana; baseline: rata-rata bergerak; segmentasi pelanggan | Error peramalan vs praktik saat ini; dampak pada stok/limbah dalam uji lapangan | Dashboard UMKM; modul pendampingan | C4/C2 · Business |
| **Bahasa (Arab/Inggris/Indonesia)** | Umpan balik menulis/berbicara bahasa asing lambat dan tidak konsisten | Tulisan mahasiswa (consent), rekaman ujaran, rubrik penilaian dosen | Penilaian otomatis berbantuan LLM dengan rubrik; baseline: rubrik manual satu penilai | Kesepakatan dengan penilai manusia (inter-rater), bias terhadap dialek/kesalahan tertentu, efek pedagogis | Alat umpan balik formatif; korpus pembelajar | C4/C3 · Education |
| **Komunikasi** | Analisis opini publik dan aduan layanan di media sosial/kanal resmi memakan waktu manual | Teks publik (media sosial, kanal aduan) sesuai ketentuan platform; koding manual sebagai label | Klasifikasi topik/sentimen Bahasa Indonesia; baseline: leksikon | Kesepakatan dengan koder manusia; validitas konstruk "sentimen"; drift topik | Laporan berkala untuk pemerintah daerah/organisasi; brief | C4/C1 · Government, Social Impact |
| **Pendidikan / unit akademik UAI** | Mahasiswa berisiko tertinggal terdeteksi terlambat | Log LMS, kehadiran, nilai (anonim; contoh sumber: *student learning*) | Prediksi risiko; baseline: IPK semester lalu | Stabilitas lintas angkatan, fairness, uji intervensi dengan dosen wali | Intervensi minggu ke-7; kebijakan analitik pembelajaran | C3/C4 · Education |
| **Dakwah / studi Islam (bila ada)** | Verifikasi kutipan dan sumber dalam konten keagamaan digital | Korpus teks rujukan yang sah, kutipan beredar (publik) | Pencocokan kutipan, deteksi atribusi salah; RAG berbasis sumber sah | Akurasi atribusi oleh ahli; batas kemampuan sistem dinyatakan jelas | Alat bantu verifikasi untuk pendidik/lembaga | C1/C4 · Social Impact |

Setiap baris dapat langsung menjadi Issue `type:problem` dengan problem owner dari fakultas mitra dan calon mentor dari Informatika.

## 4. Mekanisme kolaborasi

### 4.1 Pintu masuk

| Pintu | Siapa | Bagaimana |
|---|---|---|
| **Issue Research Problem** | Dosen/unit fakultas mitra (dibantu admin riset bila belum terbiasa GitHub) | Mengisi form *Research Problem*: domain, masalah, stakeholder, data yang mungkin, output yang diharapkan; ditandai entry door *Partner* atau *Faculty Research* |
| **Kerja Praktik / magang** | Mahasiswa Informatika di unit fakultas lain | Problem Brief dari KP masuk backlog |
| **Undangan pusat riset** | `@directors`, research lead C4 | Sesi 60 menit per fakultas: memaparkan model lima komponen, mengumpulkan 3–5 masalah kandidat |
| **Proposal hibah bersama** | Dosen dua fakultas | Riset yang sudah punya Research ID dan lolos G5 menjadi *preliminary result* |

Setelah masuk, alur sama dengan riset lain: klasifikasi → pencocokan → Research ID saat G2 → pipeline gate ([AIR-05](05-research-demand-supply-marketplace.md)).

### 4.2 MoU ringan

Kolaborasi internal antar fakultas tidak selalu memerlukan MoU formal universitas; cukup **nota kesepakatan riset satu halaman** yang disahkan pimpinan kedua unit dan disimpan di `docs/agreement.md` (INTERNAL) repositori riset. Isinya:

1. Research ID, judul kerja, klaster/domain.
2. Problem owner (mitra), AI capability owner (Informatika), mahasiswa yang terlibat.
3. Data: pemilik, klasifikasi (PUBLIC/INTERNAL/RESTRICTED), akses, anonimisasi, consent, masa simpan, siapa yang menghapus.
4. Output yang diharapkan dan jalur Scale (prototype, brief, paper, HKI) beserta pemilik masing-masing.
5. Authorship dan atribusi (§4.3).
6. Lisensi per komponen ([LICENSING.md §5](../../LICENSING.md)).
7. Durasi, titik review (G5 dan G8), dan cara mengakhiri.

MoU formal universitas diperlukan bila melibatkan pihak eksternal, data pasien/klien, potensi komersialisasi, atau pendanaan.

### 4.3 Pembagian authorship

Mengikuti prinsip kontribusi substansial (ide/desain, data, analisis, penulisan, tanggung jawab akhir) dan disepakati **di awal** (dalam nota kesepakatan), ditinjau di G7:

- Problem owner yang merumuskan masalah, menyediakan data, dan memvalidasi domain **adalah** penulis, bukan sekadar ucapan terima kasih.
- Mahasiswa yang menjalankan riset adalah penulis (sering penulis pertama pada paper hasil TA).
- Dosen Informatika yang merancang metode dan mengawasi eksperimen adalah penulis.
- Penyedia data tanpa kontribusi intelektual lain → *acknowledgement* + sitasi dataset (`DS-YYYY-NNN`).
- Urutan penulis ditetapkan berdasarkan kontribusi, dicatat di `paper/AUTHORSHIP.md`; perselisihan diputuskan `@directors`.
- Kontribusi AI diungkap sesuai kebijakan venue; AI bukan penulis.

### 4.4 Data governance

Mengikuti [SECURITY.md](../../SECURITY.md) tanpa pengecualian:

- Data mentah mitra **tidak pernah** masuk GitHub; hanya kartu metadata di `datasets-registry/`.
- Klasifikasi privasi (Public/Restricted/Confidential) diisi sebelum G5; data manusia memerlukan consent dan izin komite etik/institusi yang didokumentasikan di `docs/ethics.md` ([MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- Anonimisasi/pseudonimisasi sebelum analisis; kunci pemetaan disimpan di unit pemilik data, bukan di tim riset.
- Prompt ke layanan AI eksternal tidak memuat data pribadi/mitra.
- Lisensi dataset ditetapkan setelah review pengelola registry; dataset dengan data pribadi tidak mendapat lisensi publik.
- Model yang dilatih pada data sensitif tidak dirilis tanpa review.

## 5. Alur kolaborasi

```
 Fakultas mitra                 Pusat riset (hub)                    Informatika
 ──────────────                 ─────────────────                    ───────────
 Masalah domain ──► Issue type:problem ──► klasifikasi klaster/domain ──► calon mentor & MK
                                   │                                          │
 Data owner ◄──── nota kesepakatan 1 halaman (5 komponen, data, authorship) ─┘
                                   │
                         G2 Problem Ready → Research ID
                                   │
 validasi domain ◄──── G5 Method Ready (reviewer dua klaster) ────► baseline & metrik
                                   │
 uji lapangan/ahli ◄── G6–G7 Experiment & Claim ─────────────────► repositori reproducible
                                   │
 brief/prototype ◄──── G8 Contribution Ready + handoff ─────────► paper/dataset/ART
                                   │
                         Scale: adopsi, hibah, program-*, backlog baru
```

## 6. Kegagalan umum kolaborasi lintas disiplin dan cara menghindarinya

| Kegagalan | Gejala | Cara menghindari |
|---|---|---|
| **Solution-first dari Informatika** | "Kami punya model X, ada data apa?" | Komponen *Domain Problem* diisi mitra dulu; G2 menolak masalah yang hanya justifikasi algoritma |
| **Data dijanjikan, tidak pernah datang** | Riset macet di G5 menunggu data | Kartu dataset dan akses diverifikasi sebelum G2 disetujui; pilot memakai subset/sintetis; batas waktu data dalam nota |
| **Evaluasi hanya metrik ML** | Accuracy tinggi, ahli domain tidak percaya | Lapis evaluasi domain wajib (§2); reviewer G5/G7 dari kedua klaster |
| **Bahasa berbeda** | "Recall" vs "sensitivitas", "fitur" vs "variabel" | Glossary riset 1 halaman per proyek di `docs/`; problem brief ditulis dalam bahasa domain |
| **Authorship diperdebatkan di akhir** | Konflik saat submit | Disepakati di nota kesepakatan; ditinjau di G7 |
| **Mahasiswa menjadi satu-satunya jembatan** | Dua dosen tidak pernah bertemu; mahasiswa lulus, kolaborasi selesai | Dua dosen hadir di Design Defense (W8) dan defense; handoff #3 menyebut owner dari kedua sisi |
| **Privasi dianggap urusan belakangan** | Data pribadi muncul di notebook | Klasifikasi privasi sebelum G5; checklist integritas; `.gitignore` data |
| **Ekspektasi produk jadi** | Mitra berharap sistem produksi dari satu TA | Nota kesepakatan menyebut output riset (prototype terevaluasi, brief), bukan produk; jalur Scale terpisah |
| **Tidak ada dampak terukur** | Riset selesai, tidak ada yang berubah | Komponen *Impact* dengan indikator domain dan jalur adopsi disepakati di awal; brief wajib untuk mitra |

## 7. Checklist kickoff kolaborasi

- [ ] Lima komponen terisi dengan pemilik yang jelas.
- [ ] Issue `type:problem` dibuat; klaster primer/sekunder dan domain ditetapkan.
- [ ] Nota kesepakatan satu halaman disahkan kedua unit; MoU formal bila diperlukan.
- [ ] Kartu dataset dibuat; klasifikasi privasi, consent, dan akses jelas; tidak ada data mentah di GitHub.
- [ ] Baseline domain (praktik saat ini) dan baseline teknis ditetapkan.
- [ ] Reviewer dari dua klaster ditunjuk untuk G5 dan G7.
- [ ] Authorship dan lisensi per komponen disepakati.
- [ ] Jalur Scale (brief/prototype/paper/HKI) dan indikator dampak disepakati.
- [ ] Mahasiswa dan mentor dari kedua sisi tercatat di Mission Control.

## 8. Ringkasan

- Kolaborasi lintas fakultas = Domain Problem (mitra) + Data (mitra/bersama) + AI Capability (Informatika) + Evaluation (bersama, validasi domain dipimpin mitra) + Impact (mitra + pusat riset).
- Pintu masuk lewat Issue, KP, undangan pusat riset, atau proposal bersama; nota kesepakatan satu halaman cukup untuk kolaborasi internal.
- Authorship disepakati di awal; data governance mengikuti SECURITY.md tanpa pengecualian.
- Kegagalan umum dicegah oleh gate: G2 menolak solution-first, G5 menuntut data dan evaluasi domain, G7 menuntut klaim yang dipercaya ahli domain.
