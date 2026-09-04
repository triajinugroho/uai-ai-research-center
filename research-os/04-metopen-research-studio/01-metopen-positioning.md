# Metopen Positioning — Dari "Methodology Course" ke Research Evidence Studio

> **ID** MET-01 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu Metopen, tim kurikulum Prodi Informatika, Kaprodi, dosen pembimbing TA, mahasiswa semester VII
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [STR-01 Current State & Gaps](../01-strategic-foundation/01-current-state-and-gaps.md) · [STR-02 Vision & Endgame](../01-strategic-foundation/02-vision-and-endgame.md) · [ARC-04 Build–Prove–Contribute](../02-academic-architecture/04-build-prove-contribute.md) · [MET-02 Course Outcomes](02-metopen-course-outcomes.md) · [MET-03 16-Week Blueprint](03-metopen-16-week-blueprint.md) · [MET-04 Research Pack](04-research-pack-specification.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md)

## 1. Satu kalimat

Jangan mengampu Metodologi Penelitian sebagai "kuliah tentang penelitian". Jadikan ia **Research Evidence Studio** yang mengubah mahasiswa semester VII menjadi *novice computer scientist* yang mampu menghasilkan klaim, bukti, eksperimen, artefak, dan proposal TA yang dapat dipertanggungjawabkan.

| Aspek | Ketentuan |
|---|---|
| Nama formal (kurikulum, RPS, transkrip) | **Metodologi Penelitian**, 2 SKS, semester VII, Program Studi Informatika UAI |
| Positioning internal | **AI-Augmented Research Methods & Evidence Engineering for Informatics** |
| Versi sederhana | **Research Methods for Informatics: From Problem to Evidence** |
| Bentuk | Research Studio: ±30% concepts + 70% studio ([MET-03](03-metopen-16-week-blueprint.md)) |
| Deliverable | UAI Informatics Research Pack + Proposal TA ([MET-04](04-research-pack-specification.md)) |
| Jiwa | Evidence Engineering |
| Signature UAI | Amanah epistemik |

Nama formal tidak diubah. Yang diubah adalah **apa yang terjadi di dalam kelas** dan **apa yang keluar dari kelas**.

## 2. Posisi strategis: integration layer enam semester dan launchpad TA

Ketika struktur kurikulum Informatika UAI dibaca sebagai satu arsitektur, Metopen berada pada posisi yang tidak biasa untuk mata kuliah 2 SKS.

| Tahap | Fondasi relevan yang sudah dimiliki mahasiswa |
|---|---|
| Semester 1 | Statistika 3 SKS, Kalkulus |
| Semester 2 | Statistika Terapan 3 SKS, Matematika Diskrit |
| Semester 3 | HCI, Struktur Data, Basis Data |
| Semester 4 | Analisis Algoritma, RPL, Data Mining |
| Semester 5 | AI & Machine Learning 4 SKS, Pengujian Perangkat Lunak |
| Semester 6 | Proyek Perangkat Lunak 4 SKS, Kerja Praktik, Etika Profesi |
| Semester 7 | **Metodologi Penelitian 2 SKS** |
| Semester 8 | **Tugas Akhir 4 SKS** |

*Sumber: dokumen diskusi "Riset AI UAI untuk Negeri"; struktur kurikulum perlu diverifikasi terhadap dokumen kurikulum resmi Prodi sebelum dipakai dalam dokumen formal.*

Dua implikasi:

1. **Metopen bukan mata kuliah pengantar.** Mahasiswa sudah punya dua mata kuliah statistika, data mining, AI/ML, RPL, pengujian, dan satu proyek perangkat lunak 4 SKS. Metopen tidak perlu mengajarkan "apa itu variabel" atau "apa itu regresi". Ia adalah **integration layer** yang mengikat semua kompetensi itu ke satu tujuan: menghasilkan pengetahuan yang dapat dipercaya.
2. **Metopen adalah launchpad TA.** Ia mata kuliah terakhir sebelum Tugas Akhir. Bila mahasiswa keluar dari Metopen masih mencari judul dan metode, satu semester TA habis untuk pekerjaan yang seharusnya sudah selesai. Bila mahasiswa keluar dari Metopen dengan Research Pack, TA dimulai dari G5 Method Ready, bukan dari nol.

Dalam arsitektur akademik [ARC-04](../02-academic-architecture/04-build-prove-contribute.md): mata kuliah teknis **Build**, Metopen **Prove**, TA **Contribute**. Metopen adalah *evidence-quality gate* dari seluruh pipeline.

## 3. Problem yang diselesaikan Metopen

Problem utamanya bukan "mahasiswa belum pernah mendapat statistik atau teknologi". Justru mereka sudah mendapat cukup banyak. Problem yang perlu diselesaikan adalah:

> **Bisakah mahasiswa mengubah kemampuan teknis tersebut menjadi pengetahuan baru yang evidence-based?**

Itu permainan yang berbeda. Membuat model dengan akurasi 93% adalah kemampuan teknis. Mengetahui apakah 93% itu berarti sesuatu — dibanding baseline apa, pada data yang merepresentasikan siapa, dengan kebocoran apa yang sudah dicegah, dan apa yang bisa membuat angka itu salah — adalah kemampuan riset. Metopen melatih yang kedua.

Gejala yang ingin dihilangkan:

| Gejala pada TA/proyek | Akar masalah | Yang dilatih Metopen |
|---|---|---|
| Judul dipilih dari algoritma, bukan dari masalah | *Solution-first thinking* | Problem formulation (W2) |
| Tinjauan pustaka = ringkasan paper satu per satu | Tidak ada synthesis | Literature Evidence Map & synthesis matrix (W3–W5) |
| "Belum ada yang meneliti di UAI" sebagai gap | Gap naratif, bukan gap bukti | Gap–Claim–Evidence alignment (W5–W6) |
| Akurasi tanpa baseline | Tidak ada pembanding | Baseline & metrics (W7) |
| Hasil tidak bisa dijalankan ulang | Repositori tidak ada | Reproducibility package (W9–W10) |
| Klaim melebihi bukti | Tidak ada threats to validity | Claim–Evidence–Reasoning (W11–W12) |
| Referensi dari AI yang tidak ada | AI sebagai epistemic authority | AI Research Protocol (semua minggu) |

## 4. Evidence Engineering sebagai jiwa mata kuliah

Kalau harus dipilih satu konsep yang menjadi jiwa Metopen, konsep itu adalah **Evidence Engineering**.

Programmer menghasilkan software. Data scientist menghasilkan model. Researcher menghasilkan *credible knowledge*. Dan credible knowledge membutuhkan **rekayasa bukti**: bukti yang dirancang, dikumpulkan, diuji, dan dipertanggungjawabkan secara sistematis.

Mahasiswa harus memahami bahwa penelitian bukan:

> baca banyak jurnal → bikin judul → pakai algoritma → accuracy 93% → selesai.

Melainkan alur *research thinking* sepuluh langkah berikut.

### 4.1 Alur research thinking

| # | Pertanyaan | Artefak Research Pack yang menjawabnya | Gate |
|---|---|---|---|
| 1 | **Real-world phenomenon / problem** — apa fenomena atau masalah nyatanya? | Problem Brief, Stakeholder/Impact Statement | G2 |
| 2 | **What do we know?** — apa yang sudah diketahui dunia? | Literature Evidence Map | G3 |
| 3 | **What don't we know?** — apa yang belum diketahui? | Research Gap | G4 |
| 4 | **What exactly are we claiming?** — apa persisnya yang kita klaim? | RQ / Hypothesis, Contribution Statement | G4 |
| 5 | **What evidence would make that claim believable?** — bukti apa yang membuat klaim itu layak dipercaya? | Baseline & Metrics | G5 |
| 6 | **What research design can generate that evidence?** — desain riset apa yang menghasilkan bukti itu? | Research Design | G5 |
| 7 | **What data / artifact / experiment is required?** — data, artefak, eksperimen apa yang diperlukan? | Dataset/Data Plan, Pilot Experiment | G5–G6 |
| 8 | **What can invalidate our conclusion?** — apa yang bisa membatalkan kesimpulan? | Threats to Validity | G5, G7 |
| 9 | **Can someone else inspect/reproduce it?** — bisakah orang lain memeriksa/mereproduksi? | Reproducibility README, AI Usage Statement | G6, G8 |
| 10 | **So what?** — lalu apa artinya? | Contribution Statement (revisi), Research Pitch | G7–G8 |

Sepuluh pertanyaan ini adalah tulang punggung 16 minggu ([MET-03](03-metopen-16-week-blueprint.md)), 8 gate ([OPS-03](../06-execution-os/03-research-gates.md)), dan 16 artefak Research Pack ([MET-04](04-research-pack-specification.md)). Tidak ada konsep yang diajarkan di Metopen yang tidak menjawab salah satu dari sepuluh pertanyaan ini.

### 4.2 Solution-first vs problem-first

Pola TA Informatika yang sering terjadi:

> "Saya ingin menggunakan Random Forest untuk memprediksi X."

Ini *solution-first*. Algoritma dipilih sebelum masalahnya dipahami. Metopen memaksa mahasiswa mundur:

```
Mengapa X perlu diprediksi?
  → siapa stakeholder-nya?
  → keputusan apa yang berubah jika prediksi tersedia?
  → apa state-of-the-art saat ini?
  → baseline paling sederhana apa?
  → apa kelemahannya?
  → mengapa Random Forest?
  → dibanding apa?
  → metric apa?
  → apakah dataset merepresentasikan population?
  → bagaimana leakage dicegah?
  → apakah improvement secara praktis berarti?
  → apa threats to validity-nya?
```

Barulah algoritma muncul — sebagai jawaban atas pertanyaan, bukan sebagai titik awal.

| | Solution-first (lemah) | Problem-first (yang dilatih) |
|---|---|---|
| Kalimat pembuka | "Saya pakai metode M untuk X" | "Stakeholder S menghadapi masalah X; keputusan D berubah bila ..." |
| Literatur | Mencari paper yang memakai M | Memetakan apa yang diketahui tentang X dan bagaimana X diukur |
| Gap | "Belum ada yang memakai M untuk X di Indonesia" | "Bukti tentang X pada konteks K bertentangan/kosong pada dimensi Z" |
| Baseline | Tidak ada, atau metode M dibanding dirinya sendiri | Pembanding paling sederhana yang masuk akal |
| Klaim | "M lebih baik" | "Pada data D dengan metrik μ, M mengungguli baseline B sebesar Δ; berlaku untuk ...; tidak berlaku untuk ..." |
| Reviewer G2 | Gagal: masalah hanya justifikasi algoritma | Lulus: orang luar bisa mengulang masalahnya dalam dua kalimat |

Perubahan epistemologi yang dituju:

1. **"Saya membuat sesuatu."** → mahasiswa engineering.
2. **"Saya membuat klaim yang dapat diuji."** → mahasiswa mulai berpikir ilmiah.
3. **"Saya memiliki bukti yang cukup kuat untuk mempertanggungjawabkan klaim tersebut."** → scientific thinker.

## 5. Mengapa tidak mengejar "ideal universitas top" secara mentah

Benchmark mata kuliah research methods di beberapa universitas (sebagaimana dirangkum dalam dokumen diskusi; verifikasi silabus terkini sebelum dikutip dalam dokumen formal):

| Universitas | Cakupan yang dilaporkan |
|---|---|
| University of Sydney (Research Methods 2026) | Menemukan dan mengevaluasi literatur, menulis literature review, research plan, quality metrics, research ethics |
| Mälardalen University | Research question/hypothesis, literature search, analisis kuantitatif dan kualitatif, proposal design, threats to validity, ethics |
| University of Houston | Experimental design, statistics, membaca dan mereview paper, data processing, visualization, writing, oral presentation, "Computer Science research in the post-AI world"; proyek riset sepanjang semester |
| Princeton (2026) | Empirical CS melalui causal inference, experiments, regression, benchmark, quasi-experiments, causal ML, labeling dengan LLM |
| BINUS (Research Methodology in Computer Science, 2 SCU) | Scientific research lifecycle, literature/citation, theoretical framework, research design, data handling, analysis/visualization, ethics, scientific publication, proposal presentation, peer review, tren CS |

Tiga kesimpulan dari benchmark itu:

1. **Arah globalnya jelas**: computing-specific, project-based, mencakup validity, ethics, reproducibility, dan AI-aware research. Metopen UAI harus berada di arah yang sama.
2. **Semuanya tidak bisa dijejalkan ke 2 SKS.** Kalau dipaksa, hasilnya: *semua dikenalkan, tidak ada yang dikuasai*.
3. **BINUS membuktikan 2 SKS tidak harus generik.** Tetapi UAI didorong satu langkah lebih jauh: bukan sekadar *Research Methodology in Computer Science*, melainkan **Responsible AI-Augmented Evidence Engineering**.

### 5.1 Prinsip Pareto

Mahasiswa S1 semester VII **tidak** membutuhkan advanced causal inference, advanced Bayesian statistics, full systematic review, graduate-level epistemology, atau sophisticated econometrics.

Mereka membutuhkan:

> **minimum methodological sophistication required to stop producing weak research.**

Occam. Setiap topik yang masuk ke Metopen harus lolos uji: *apakah tanpa topik ini mahasiswa akan menghasilkan riset yang lemah?* Kalau jawabannya tidak, topik itu masuk ke bahan bacaan opsional, bukan ke 16 minggu.

| Masuk kurikulum inti (Pareto 20%) | Bahan opsional / TA lanjutan |
|---|---|
| Baseline, metrik, leakage, error analysis | Causal inference lanjutan, quasi-experiment |
| Threats to validity (4 jenis) | Meta-analysis, full systematic review protokol PRISMA |
| Synthesis matrix | Bibliometrics lanjutan |
| Statistical thinking secukupnya (variansi antar seed/fold, interval, uji sederhana) | Bayesian statistics, econometrics |
| Reproducibility package minimum | Artifact badging formal |
| AI Research Protocol | Filsafat ilmu tingkat pascasarjana |

## 6. Posisi visual: dua sumbu

Bayangkan dua sumbu. Horizontal: *Generic Research Methods → Computing-Specific Research Methods*. Vertikal: *Theory/Knowing → Research Practice/Doing*.

```
RESEARCH PRACTICE / DOING
        ↑
        |
        |                       IDEAL FRONTIER
        |                            ●
        |
        |                  SWEET SPOT UAI
        |                       ★
        |
        |  CURRENT
        |    ●
        |
        ----------------------------------------------------→
        GENERAL METHODS                  COMPUTING-SPECIFIC
        |
        |
   THEORY / KNOWING
```

Sweet spot sengaja diletakkan **sedikit di bawah ideal frontier** pada sumbu vertikal dan **jauh ke kanan** pada sumbu horizontal. Artinya: sangat computing-specific, sangat praktik, tetapi tidak mengejar kecanggihan metodologis yang tidak bisa dikuasai dalam 2 SKS.

Catatan transparansi dari dokumen diskusi: RPS Metopen Informatika UAI terkini belum ditemukan dipublikasikan resmi, sehingga posisi "current" dibaca dari arsitektur kurikulum publik, bukan klaim tentang cara dosen sebelumnya mengajar. Rincian *current vs ideal vs sweet spot* per dimensi ada di [STR-01](../01-strategic-foundation/01-current-state-and-gaps.md).

### 6.1 Ringkasan sweet spot per dimensi

| Dimensi | Sweet spot Informatika UAI |
|---|---|
| Tujuan | TA-ready novice computer scientist |
| Fokus | Problem → Evidence → Method → Pilot → Proposal |
| Starting point | Masalah yang layak dipecahkan, bukan "apa itu penelitian?" |
| Literatur | Literature intelligence + evidence map |
| Research gap | Gap–Claim–Evidence alignment |
| Metode | Experiment, benchmark, design science, case study, survey, user study, ML evaluation |
| Statistik | Cukup untuk mencegah klaim buruk |
| Coding | Notebook/repository sebagai research artifact |
| AI | AI as research copilot, not epistemic authority |
| Evaluasi AI/ML | Baseline, metric, benchmark, ablation/error analysis |
| Validitas | Threats to validity wajib |
| Reproducibility | Minimum reproducibility package |
| Etika | Integrity + privacy + human subjects + bias + AI disclosure |
| Writing | Claim–evidence–reasoning |
| Output | Research Pack + proposal TA |
| Assessment | Milestone portfolio + defense |
| Hubungan TA | Proposal Metopen langsung menjadi TA |
| Hubungan dosen | Lab/faculty research matching |

## 7. Dua pembeda: GenAI dan reproducibility

### 7.1 Apa yang berubah karena GenAI

Panduan kurikulum CS2023 (ACM/IEEE-CS/AAAI) mencerminkan makin sentralnya AI dalam Computer Science, memperkuat probability/statistics, dan bergeser menuju kurikulum berorientasi kompetensi. Praktik publikasi ACM pada 2026 juga membedakan AI untuk membantu penulisan dari AI yang digunakan di dalam proses penelitian; bila AI memengaruhi desain, data, eksperimen, kode, analisis, atau artefak yang memengaruhi kesimpulan, penggunaannya perlu dijelaskan dalam metode dan peneliti tetap bertanggung jawab. *(Sebagaimana dirangkum dalam dokumen diskusi; verifikasi teks kebijakan terkini sebelum dikutip.)*

Implikasinya: Metopen **bukan** *AI-free Research Methods* (tidak realistis), dan **bukan** "pakai ChatGPT bikin proposal". Sweet spot-nya:

> **AI-augmented, human-accountable science.**

Mahasiswa boleh memakai AI untuk eksplorasi terminologi, kandidat keyword, coding support, debugging, brainstorming hipotesis alternatif, kritik desain eksperimen, penjelasan statistik, dan bantuan analisis. Tetapi setiap output harus melalui **source verification → reasoning verification → evidence verification → human accountability** ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)). Dengan begitu kita tidak mendidik orang yang pandai menghasilkan tulisan akademik; kita mendidik orang yang **sulit dibohongi — termasuk oleh AI-nya sendiri**.

### 7.2 Reproducibility sebagai pembeda kedua

Di computing, paper bukan satu-satunya produk penelitian. Ada dataset, source code, model, configuration, benchmark, prompt, random seed, notebook, experiment logs, environment, visualization, dan scripts. Maka mahasiswa tidak hanya menyerahkan `Proposal.pdf`, tetapi **Research Repository** ([TPL-15](../08-templates/15-research-repository-template.md)). Tidak harus semua lengkap di Metopen, tetapi mindset-nya dibangun: dari *academic document* menjadi *inspectable research artifact*.

## 8. Layer Al Azhar: amanah epistemik, bukan tempelan

Nilai Islam masuk ke Metopen bukan sebagai satu pertemuan "Etika Penelitian dalam Islam", melainkan sebagai worldview yang bekerja setiap minggu: **amanah epistemik**.

Seorang peneliti memegang amanah untuk tidak mengarang data, memilih bukti yang menguntungkan saja, menutupi hasil negatif, mengubah metrik setelah melihat hasil, mengutip yang tidak dibaca, membiarkan AI mengarang referensi, mengklaim kausalitas dari korelasi, atau melebih-lebihkan kontribusi. Dalam bahasa riset modern: *research integrity*. Dalam bahasa keimanan: kejujuran terhadap kebenaran meskipun kebenaran itu meruntuhkan hipotesis sendiri.

Orientasi berubah dari "bagaimana penelitian saya terlihat bagus?" menjadi "apa yang sebenarnya benar berdasarkan bukti yang Allah izinkan saya temukan?" Secara akademik rigorous, secara spiritual meaningful. Operasionalisasinya: Research Integrity Gate yang bersifat lulus/gagal di setiap gate ([MET-06](06-assessment-and-5e-rubric.md), [MET-07](07-research-integrity-and-ethics.md)), bukan satu bab di akhir semester.

## 9. Positioning final

> **Metodologi Penelitian Informatika adalah research studio yang melatih mahasiswa mengubah masalah nyata menjadi pertanyaan ilmiah, membangun argumentasi berbasis literatur, merancang metode dan eksperimen yang valid, menggunakan AI secara bertanggung jawab, menghasilkan evidence dan artefak yang reproducible, serta mempertanggungjawabkan temuannya secara ilmiah, etis, dan profesional sebagai fondasi Tugas Akhir dan karya penelitian berikutnya.**

Setiap frasa dalam definisi itu memiliki minggu, artefak, dan gate-nya:

| Frasa | Minggu | Artefak | Gate |
|---|---|---|---|
| mengubah masalah nyata menjadi pertanyaan ilmiah | W2, W6 | Problem Brief, RQ/Hypothesis | G2, G4 |
| membangun argumentasi berbasis literatur | W3–W5 | Literature Evidence Map, Research Gap | G3 |
| merancang metode dan eksperimen yang valid | W7–W8 | Research Design, Baseline & Metrics, Threats to Validity | G5 |
| menggunakan AI secara bertanggung jawab | semua | AI Usage Statement, AI Usage Log | setiap gate |
| menghasilkan evidence dan artefak yang reproducible | W9–W11 | Pilot Experiment, Reproducibility README | G6, G7 |
| mempertanggungjawabkan temuannya | W12–W16 | Contribution Statement, Proposal TA, Research Pitch | G7, G8 |

## 10. Expected learner transformation

### 10.1 Tiga tahap epistemologis

| Tahap | Kalimat mahasiswa | Ciri | Kira-kira tercapai |
|---|---|---|---|
| 1 | "Saya membuat sesuatu." | Bangga pada artefak; belum ada klaim | Masuk Metopen (W1) |
| 2 | "Saya membuat klaim yang dapat diuji." | Punya RQ, hipotesis yang bisa salah, baseline, metrik | G4–G5 (W6–W8) |
| 3 | "Saya punya bukti yang cukup kuat untuk mempertanggungjawabkan klaim itu." | Pilot berjalan, threats to validity ditulis jujur, klaim tidak melebihi bukti | G7–G8 (W12–W16) |

### 10.2 Tiga layer outcome

| Layer | Nama | Arti | Setara gate |
|---|---|---|---|
| Minimum | **TA Ready** | Tidak masuk semester VIII masih mencari judul dan metode | G5 |
| Target | **Research Ready** | Mampu menjalankan satu penelitian computing sederhana secara benar | G6–G7 |
| Aspirational | **Publication / Impact Ready** | TA terbaik menjadi paper, dataset, open-source artifact, HKI, prototype, bagian riset dosen, atau solusi industri/masyarakat | G8 + manuscript-ready |

North star: **100% mahasiswa selesai Metopen sudah TA-ready; mahasiswa terbaik research/publication-ready.** Rincian per CPMK di [MET-02](02-metopen-course-outcomes.md).

### 10.3 Endgame jangka panjang: research method sebagai operating system berpikir

Lima tahun setelah lulus, tidak penting apakah mahasiswa masih ingat perbedaan penelitian deskriptif dan korelasional. Yang penting: ketika mereka menjadi AI engineer, software engineer, product manager, entrepreneur, researcher, consultant, atau decision maker, mereka otomatis bertanya:

- Apa problem sebenarnya?
- Apa yang kita ketahui vs hanya kita asumsikan?
- Apa evidence-nya?
- Apa baseline-nya?
- Bagaimana kita mengujinya?
- Apa bias-nya?
- Apa yang bisa membuat kesimpulan ini salah?
- Bisakah orang lain memverifikasinya?

Itulah research method sebagai operating system berpikir — bahkan bagi mahasiswa yang tidak pernah menjadi akademisi.

## 11. Compounding loop

Metopen tidak berdiri sendiri. Ia adalah *control point* dan *talent funnel* penelitian dosen:

> satu mata kuliah → TA lebih baik → mahasiswa lebih capable → riset dosen lebih kuat → publikasi → reputasi prodi → kolaborasi → problem lebih berkualitas → mahasiswa berikutnya mendapat research environment yang lebih baik.

Skema penelitian internal UAI yang mendorong keterlibatan mahasiswa dan mengarahkan topik ke Renstra Penelitian universitas (sebagaimana disebut dalam dokumen diskusi; verifikasi panduan skema terkini) membuat loop ini punya pintu masuk nyata: problem dari riset dosen masuk sebagai *Faculty Research entry door* ([AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md)), dan Research Pack terbaik kembali ke dosen sebagai bahan proposal, dataset, atau paper.

## 12. Power move

Jangan ajarkan mahasiswa cara "membuat penelitian terlihat ilmiah". Ajarkan mereka cara **membedakan klaim yang dipercaya karena terdengar meyakinkan dengan klaim yang layak dipercaya karena memiliki bukti**. Semua dokumen paket 04 hanyalah implementasi dari kalimat ini.
