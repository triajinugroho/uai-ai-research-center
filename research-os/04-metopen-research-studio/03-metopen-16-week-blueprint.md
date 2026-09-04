# Metopen 16-Week Blueprint — Satu Semester sebagai Research Production Line

> **ID** MET-03 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu Metopen, asisten/mentor studio, mahasiswa semester VII, penyusun RPS
> **Terkait** [MET-01 Positioning](01-metopen-positioning.md) · [MET-02 Course Outcomes](02-metopen-course-outcomes.md) · [MET-04 Research Pack](04-research-pack-specification.md) · [MET-06 5E Rubric](06-assessment-and-5e-rubric.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [OPS-01 Research WBS](../06-execution-os/01-research-wbs-master.md) · [OPS-02 Weekly Sprints](../06-execution-os/02-weekly-sprints.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [OPS-05 Student Weekly Playbook](../06-execution-os/05-student-weekly-playbook.md) · [Studio mahasiswa](../../metopen-research-studio/README.md)

## 1. Bentuk semester

Mahasiswa tidak "belajar membuat proposal" selama satu semester. Mereka menjalankan **satu mini research cycle**, dan proposal TA lahir sebagai konsekuensinya. Enam belas minggu adalah satu production line: Problem → Evidence Map → Gap → RQ → Research Design → Pilot → Validity → Reproducible Artifact → Proposal TA.

### 1.1 Komposisi 30/70

| Porsi | Isi | Bentuk |
|---|---|---|
| ±30% concepts | Materi inti yang tanpanya mahasiswa menghasilkan riset lemah (prinsip Pareto, [MET-01](01-metopen-positioning.md) §5) | Mini-lecture, contoh kasus, demonstrasi |
| ±70% research studio | Tim mengerjakan risetnya sendiri dengan mentor keliling, peer critique, gate check | Studio, review, pitch, red team, defense |

### 1.2 Struktur satu sesi 2 SKS (100 menit)

| Menit | Blok | Isi |
|---|---|---|
| 0–30 | **Concept** | Materi inti minggu itu; satu konsep, satu contoh baik, satu contoh lemah |
| 30–90 | **Studio** | Tim mengerjakan microtask sprint; dosen/mentor berkeliling; peer critique terstruktur di 15 menit terakhir |
| 90–100 | **Gate check** | Setiap tim melaporkan status satu kalimat ("Riset ini menuju ___ lewat pintu ___"), blocker, dan rencana sisa sprint; dosen mencatat di tracker |

Pekerjaan di luar kelas mengikuti sprint mingguan [OPS-02](../06-execution-os/02-weekly-sprints.md): 7–10 microtask per sprint, terlihat oleh mahasiswa lewat [OPS-05](../06-execution-os/05-student-weekly-playbook.md) dan halaman mingguan di `metopen-research-studio/weeks/`.

### 1.3 Tabel ringkasan

| Sprint | Minggu | Tema | Konsep inti (30%) | Deliverable utama | Gate | Release |
|---|---|---|---|---|---|---|
| S0 | pra-W1 | Onboarding | Cara kerja studio, GitHub, protokol AI | Akun, repo latihan, kuis protokol | — | — |
| S1 | W1 | Endgame | Research thinking; project vs research; entry door | `docs/endgame.md`, repo riset, agreement | G1 | — |
| S2 | W2 | Problem | Problem-first; stakeholder; problem worth solving | Problem Brief, One-Pager v0 | G2 | v0.1 |
| S3 | W3 | Search | Landscape literatur; basis data; citation chaining; kualitas sumber | Search strategy, `references.bib` awal | G3 (mulai) | — |
| S4 | W4 | Evidence | Membaca paper strategis; synthesis matrix | Synthesis matrix v1 | G3 | — |
| S5 | W5 | Gap | Dari matriks ke pola; jenis gap; Gap–Claim–Evidence | Literature Evidence Map, Research Gap | G3 (lulus) | v0.2 |
| S6 | W6 | RQ | Anatomi RQ; hipotesis falsifiable; jenis kontribusi | RQ/Hypothesis, Contribution Statement | G4 | — |
| S7 | W7 | Method | Computing Research Methods Map; desain; metrik & baseline; validity | Research Design Card, Data Plan, Baseline & Metrics | G5 (mulai) | — |
| S8 | W8 | Design Defense | Pitching desain; red team thinking | Pitch, notulen red team, desain revisi | G5 (lulus) | v0.3 |
| S9 | W9 | Repository | Reproducibility package; data governance | Repo eksperimen siap, dataset card | G6 (mulai) | — |
| S10 | W10 | Pilot | Minimum viable experiment; seed & sanity check | Pilot results, catatan reproduksi peer | G6 (lulus) | v0.5 |
| S11 | W11 | Analysis | Error analysis; ketidakpastian; visualisasi jujur | `results/analysis.md` draft, figur | G7 (mulai) | — |
| S12 | W12 | Contribution | Claim–Evidence–Reasoning; hasil negatif; "so what" | CER table, Threats v2, Contribution revisi | G7 (lulus) | — |
| S13 | W13 | Manuscript | IMRaD computing; struktur proposal; sitasi; AI dalam penulisan | Proposal TA / manuscript draft | G8 (mulai) | v0.8 |
| S14 | W14 | Peer Review | Etika reviewer; TPL-12 | 2 review ditulis, review diterima | G8 | — |
| S15 | W15 | Revision | Response to reviewers; integrity checklist; handoff | Proposal v1.0 draft, TPL-11, TPL-14 | G8 | — |
| S16 | W16 | Defense | Research defense | Defense, Research Pack v1.0, handoff | G8 (lulus) | v1.0 |

### 1.4 Konvensi bagian per minggu

Setiap minggu di bawah memuat: **Objective · Concept (30%) · Activity (70%) · AI use · Microtasks · Deliverable · Gate · Human check**. Microtask ditulis ringkas; nomor Task ID resmi tidak diulang di sini agar tidak menyimpang dari sumber tunggal WBS — lihat [OPS-01](../06-execution-os/01-research-wbs-master.md) pada sprint yang sesuai. Aturan AI per minggu adalah turunan dari [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md); daftar izin/larangan lengkap ada di sana.

---

## Sprint S0 — Onboarding (sebelum W1)

**Objective.** Semua mahasiswa masuk W1 dengan alat, akun, dan pemahaman aturan main yang sama.

**Isi.** Membaca [Student Guide](../../research-based-learning/student-guide/README.md), [OPS-05](../06-execution-os/05-student-weekly-playbook.md), dan [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md); membuat akun GitHub; latihan branch/PR pada repo latihan; instalasi Python/notebook environment dan reference manager; kuis singkat protokol AI dan integritas (lulus ≥80%, boleh diulang); mengisi preferensi klaster/domain dan kandidat entry door; penyegaran opsional statistik dasar dan git untuk yang membutuhkan.

**Deliverable.** Akun GitHub aktif di team `@students`, PR latihan merged, kuis lulus, form preferensi terisi. Task ID resmi: lihat OPS-01 Sprint S0.

---

## W1 — Endgame

**Objective.** Setiap tim tahu risetnya mau menjadi apa, untuk siapa, dan masuk lewat pintu mana; repositori riset berdiri; protokol AI disepakati.

**Concept (30%).** Perbedaan *project*, *implementation*, *engineering*, dan *research*. Alur research thinking sepuluh langkah ([MET-01](01-metopen-positioning.md) §4). Tiga layer outcome (TA Ready / Research Ready / Publication Ready). Enam entry door. Peta 8 gate dan 16 artefak Research Pack sebagai "peta semester". Contoh endgame lemah ("membuat aplikasi X") vs kuat ("menguji apakah X mengungguli baseline B pada konteks K").

**Activity (70%).** Pembentukan tim 1–3 orang (disarankan 2). Memilih entry door dari kandidat backlog/riset dosen/dataset/proyek MK. Menulis `docs/endgame.md`. Membuat repositori dari [TPL-15](../08-templates/15-research-repository-template.md). Membuka Issue `type:problem` awal. Menandatangani **AI Research Protocol Agreement** dan memulai AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)). Self-assessment awal level AI competency ([AIX-02](../05-ai-augmented-research/02-ai-research-competency-framework.md)).

**AI use.** Boleh: eksplorasi istilah bidang, memetakan sub-area topik, brainstorming kandidat endgame. Tidak boleh: meminta AI "memilihkan topik TA" tanpa mengecek backlog/dosen; memasukkan data pribadi anggota tim ke layanan AI.

**Microtasks.** (1) Bentuk tim dan bagi peran awal; (2) telusuri ≥3 kandidat problem dari backlog/roadmap; (3) pilih entry door dan kandidat mentor; (4) buat repo dari template dan isi README riset minimal; (5) tulis `docs/endgame.md`; (6) tanda tangani agreement, buat AI Usage Log; (7) buka Issue `type:problem`. Task ID resmi: lihat OPS-01 Sprint S1.

**Deliverable.** `docs/endgame.md`, repositori standar, Issue awal, agreement, AI Usage Log entri pertama.

**Gate.** G1 Endgame Ready. **Human check.** Dosen memastikan endgame memuat klaim pengetahuan yang ingin dibuktikan, bukan hanya artefak yang ingin dibuat.

## W2 — Problem

**Objective.** Masalah diformulasikan problem-first, dengan stakeholder dan keputusan yang berubah; Research ID resmi diberikan.

**Concept (30%).** Solution-first vs problem-first (rantai "Mengapa X perlu diprediksi?"). Problem worth solving: nyata, penting sekarang, ada pemangku kepentingan, ada konteks Indonesia/UAI. Stakeholder & impact statement. Keselarasan dengan klaster C1–C4 dan domain roadmap. Uji dua kalimat: orang luar bisa mengulang masalahnya.

**Activity (70%).** Menulis Problem Brief (`docs/problem.md`) dan Stakeholder/Impact Statement. Wawancara singkat/konfirmasi ke stakeholder atau dosen pemilik masalah bila memungkinkan. Menyusun Research One-Pager v0 ([TPL-01](../08-templates/01-research-one-pager-template.md)). Peer test dua kalimat lintas tim. Membuka PR `GATE REVIEW: Problem Ready`.

**AI use.** Boleh: meminta AI mengkritik apakah problem statement masih solution-first; brainstorming kandidat stakeholder yang kemudian diverifikasi. Tidak boleh: mengambil "statistik masalah" dari AI tanpa sumber yang bisa dibuka; menulis Problem Brief seluruhnya oleh AI.

**Microtasks.** (1) Tulis rantai "mengapa" hingga lima level; (2) identifikasi stakeholder dan keputusan yang berubah; (3) tulis Problem Brief; (4) petakan ke klaster dan domain; (5) isi One-Pager v0; (6) peer test dua kalimat dan perbaiki; (7) buka PR G2. Task ID resmi: lihat OPS-01 Sprint S2.

**Deliverable.** `docs/problem.md`, One-Pager v0, PR G2, Research ID `UIAI-YYYY-NNN`, release v0.1 Problem Validated.

**Gate.** G2 Problem Ready. **Human check.** Reviewer luar tim mengulang masalah dalam dua kalimat tanpa menyebut algoritma.

## W3 — Search

**Objective.** Strategi pencarian literatur terdokumentasi dan 40–60 kandidat sumber tersaring menjadi 15–25 sumber primer terverifikasi.

**Concept (30%).** Landscape literatur computing: jurnal, konferensi, preprint, thesis, grey literature — dan cara menimbang kualitasnya. Basis data: Google Scholar, Scopus, Semantic Scholar, dan sejenisnya. Backward/forward citation chaining. Kriteria inklusi/eksklusi. Reference management dan `references.bib`. AI untuk *literature intelligence*: berguna untuk menemukan, tidak pernah dipercaya untuk mengutip.

**Activity (70%).** Menyusun `docs/search-strategy.md` (kata kunci, sinonim, string pencarian, basis data, kriteria). Menjalankan pencarian dan citation chaining. Screening judul/abstrak. Memverifikasi keberadaan setiap sumber (DOI/URL dibuka). Menyiapkan reference manager dan `references.bib`.

**AI use.** Boleh: kandidat kata kunci dan sinonim; tool deep research/literature search untuk menemukan kandidat; ringkasan abstrak sebagai pra-screening. Tidak boleh: memasukkan referensi dari AI tanpa membuka sumber aslinya; menganggap "ringkasan AI" sebagai telah membaca paper.

**Microtasks.** (1) Tulis kata kunci dan string pencarian; (2) tentukan basis data dan kriteria inklusi/eksklusi; (3) jalankan pencarian, catat jumlah hasil; (4) citation chaining dari 3–5 paper kunci; (5) screening ke 15–25 sumber; (6) verifikasi DOI/URL setiap sumber, catat di AI Usage Log bila lewat AI; (7) isi `references.bib`. Task ID resmi: lihat OPS-01 Sprint S3.

**Deliverable.** `docs/search-strategy.md`, daftar kandidat tersaring, `references.bib` awal.

**Gate.** G3 Evidence Ready (mulai). **Human check.** Dosen spot-check 3 sumber acak: ada, relevan, dan kriteria pencarian benar-benar dipakai.

## W4 — Evidence

**Objective.** Sumber primer dibaca secara nyata dan dituangkan dalam synthesis matrix.

**Concept (30%).** Membaca paper computing secara strategis: abstract → figures/tables → method → limitations → introduction terakhir. Membedakan klaim dari bukti. Kolom synthesis matrix: problem, metode, data, metrik, hasil, keterbatasan, relevansi. Critical appraisal: apakah baseline ada, apakah data representatif, apakah hasilnya direproduksi orang lain.

**Activity (70%).** Membagi sumber antar anggota; membaca dan mengisi `literature/synthesis-matrix.csv`; menandai pertentangan dan konsistensi awal; mencatat kualitas bukti tiap sumber. Peer cross-check: anggota lain memeriksa 2 baris matriks terhadap PDF.

**AI use.** Boleh: menjelaskan istilah/teknik yang belum dikenal; membantu mengekstrak struktur paper sebagai pra-baca. Tidak boleh: mengisi baris matriks dari output AI tanpa membuka bagian paper yang dirujuk; memasukkan PDF berlisensi terbatas ke layanan AI yang melanggar ketentuan.

**Microtasks.** (1) Bagi sumber antar anggota; (2) baca dan isi matriks 8–12 sumber pertama; (3) baca dan isi sisanya; (4) tandai kualitas bukti tiap sumber; (5) peer cross-check 2 baris; (6) catat pertentangan awal; (7) perbarui `references.bib`. Task ID resmi: lihat OPS-01 Sprint S4.

**Deliverable.** Synthesis matrix v1 (15–25 baris), catatan pertentangan.

**Gate.** G3 (berlanjut). **Human check.** Reviewer memilih satu baris dan meminta mahasiswa menunjukkan halaman/tabel di paper yang mendukungnya.

## W5 — Gap

**Objective.** Literature Evidence Map final dan Research Gap yang dapat ditelusuri ke baris matriks; G3 lulus.

**Concept (30%).** Dari matriks ke pola: apa yang konsisten, apa yang bertentangan, apa yang belum diuji. Jenis gap: empiris, metodologis, kontekstual, replikasi, artefak/dataset. Gap–Claim–Evidence alignment. Mengapa "belum ada yang meneliti di UAI/Indonesia" bukan gap kecuali ada alasan konteks yang mengubah hasil. Menggambar evidence map (tabel tema × sumber atau diagram).

**Activity (70%).** Menulis `docs/literature-map.md` (narasi pola + tabel/diagram). Menulis Research Gap dengan rujukan baris. Membuka Issue `type:literature-gap`. PR `GATE REVIEW: Evidence Ready`. Release v0.2.

**AI use.** Boleh: meminta AI menantang gap ("apa sub-area yang mungkin terlewat?") lalu memverifikasi lewat pencarian ulang. Tidak boleh: menerima klaim AI bahwa "belum ada penelitian tentang X".

**Microtasks.** (1) Kelompokkan baris matriks ke tema; (2) tulis pola konsisten/bertentangan/belum diuji; (3) gambar evidence map; (4) tulis gap dengan rujukan baris; (5) tantang gap via AI dan pencarian ulang; (6) buka Issue gap; (7) buka PR G3 dan buat release v0.2. Task ID resmi: lihat OPS-01 Sprint S5.

**Deliverable.** Literature Evidence Map, Research Gap, `references.bib` final, PR G3.

**Gate.** G3 Evidence Ready (lulus). **Human check.** Gagal bila satu saja referensi tidak dapat diverifikasi keberadaannya.

## W6 — RQ

**Objective.** RQ dan/atau hipotesis yang spesifik, dapat difalsifikasi, dan terjangkau dalam semester + TA; kontribusi dinyatakan.

**Concept (30%).** Anatomi RQ: konstruk, konteks, pembanding, batas. Hipotesis yang bisa salah: arah, variabel, kriteria penolakan. Jenis kontribusi: empiris, artefak, metode, dataset, replikasi, studi kasus. Scoping: satu RQ utama, maksimal dua RQ pendukung. RQ tidak valid sebelum G3 selesai.

**Activity (70%).** Menulis `docs/research-question.md` (RQ, hipotesis, kontribusi). Menelusuri setiap RQ ke gap dan baris matriks. Research One-Pager v1. Issue `type:research-question`. PR `GATE REVIEW: Question Ready`.

**AI use.** Boleh: brainstorming hipotesis alternatif; meminta AI mencari cara hipotesis bisa salah. Tidak boleh: memakai RQ buatan AI yang tidak bisa ditelusuri ke matriks.

**Microtasks.** (1) Tulis 3 kandidat RQ; (2) pilih satu, uji spesifik/answerable/bounded; (3) tulis hipotesis dan kriteria penolakan; (4) tulis Contribution Statement; (5) tautkan RQ ke gap dan baris matriks; (6) perbarui One-Pager v1; (7) buka Issue RQ dan PR G4. Task ID resmi: lihat OPS-01 Sprint S6.

**Deliverable.** RQ/Hypothesis, Contribution Statement, One-Pager v1, PR G4.

**Gate.** G4 Question Ready. **Human check.** Mentor menanyakan "baris mana di matriks yang membuat RQ ini perlu?" untuk setiap RQ.

## W7 — Method

**Objective.** Desain riset, data plan, baseline & metrik, threats to validity awal, dan ethics awal tersusun.

**Concept (30%).** **Computing Research Methods Map** — untuk tiap metode: kapan dipakai, bukti apa yang dihasilkan, ancaman khasnya:

| Metode | Kapan | Bukti | Ancaman khas |
|---|---|---|---|
| Controlled experiment | Menguji efek intervensi/algoritma | Perbandingan terkontrol | Confounder, leakage |
| Benchmarking | Membandingkan metode pada dataset/tugas standar | Tabel metrik vs baseline | Data uji tidak representatif, tuning tidak adil |
| Design science | Membangun & mengevaluasi artefak | Artefak + evaluasi | Evaluasi hanya oleh pembuat |
| Empirical SE study | Mempelajari praktik/artefak perangkat lunak | Data proyek/repositori, pengukuran | Bias seleksi proyek |
| ML research | Model, data, evaluasi | Metrik, ablation, error analysis | Leakage, seed cherry-picking, metric switching |
| Simulation | Sistem yang mahal/berbahaya diuji langsung | Hasil simulasi dengan parameter | Model simulasi tidak valid |
| Survey | Persepsi/praktik populasi | Data kuesioner | Sampling, instrumen tidak valid |
| User study | Interaksi manusia–sistem | Pengukuran tugas, kualitatif | Ukuran sampel kecil, efek pembelajaran |
| Case study | Fenomena dalam konteks nyata | Deskripsi kaya, triangulasi | Generalisasi terbatas |
| Qualitative | Makna, alasan, proses | Wawancara, coding tematik | Reflexivity, reliabilitas coding |

Lalu: variabel, konstruk, kontrol, sampling, confounder, bias. Measurement & evaluation: metric selection selaras RQ, baseline paling sederhana, benchmark, protokol evaluasi yang mencegah leakage. Empat threats to validity. Ethics & privacy awal.

**Activity (70%).** Mengisi Research Design Card ([TPL-08](../08-templates/08-research-design-card.md)), Dataset/Data Plan (dan kartu dataset di `datasets-registry/` bila baru, [TPL-05](../08-templates/05-dataset-registry-template.md)), Baseline & Metrics, Experiment Card draft ([TPL-09](../08-templates/09-experiment-card.md)), Threats v1, `docs/ethics.md` awal. Menyiapkan slide pitch W8.

**AI use.** Boleh: meminta AI mengkritik desain ("apa confounder yang belum dikontrol?"); penjelasan metrik/statistik. Tidak boleh: membiarkan AI memilih metrik/baseline tanpa justifikasi yang dipahami tim; memasukkan data mentah ke AI.

**Microtasks.** (1) Pilih metode dari map dan tulis alternatif yang ditolak; (2) definisikan variabel/konstruk/kontrol/sampling; (3) tulis data plan dan kartu dataset; (4) tetapkan baseline dan metrik; (5) isi Experiment Card draft; (6) tulis Threats v1 dan ethics awal; (7) susun slide pitch; (8) minta AI red-team desain dan catat di log. Task ID resmi: lihat OPS-01 Sprint S7.

**Deliverable.** `docs/research-design.md` draft, design card, data plan, baseline & metrics, experiment card, threats v1, `docs/ethics.md`, slide.

**Gate.** G5 Method Ready (mulai). **Human check.** Dosen memastikan baseline dan metrik sudah ada sebelum tim menyentuh kode eksperimen.

## W8 — Design Defense

**Objective.** Desain dipertahankan di Mid-semester Research Pitch / Red Team Review dan direvisi; G5 lulus.

**Concept (30%).** Cara mem-pitch desain riset dalam 5–7 menit: masalah → gap → RQ → desain → bukti yang diharapkan → ancaman. Red team thinking: tugas penonton adalah mencari cara riset ini gagal. Menerima kritik sebagai bagian normal sains (amanah epistemik).

**Activity (70%).** Setiap tim pitch; red team (peer dari tim lain + dosen/mentor lain) mengajukan pertanyaan terstruktur (metrik? baseline? leakage? representativitas? etika?). Notulen red team. Revisi desain di studio. PR `GATE REVIEW: Method Ready`. Release v0.3. Self-assessment AI competency kedua.

**AI use.** Boleh: latihan pitch dengan AI sebagai penanya adversarial. Tidak boleh: menjawab pertanyaan red team dengan hasil yang belum ada.

**Microtasks.** (1) Latihan pitch dengan AI/peer; (2) pitch resmi; (3) catat semua pertanyaan red team; (4) klasifikasikan kritik: ubah desain / tambah kontrol / tolak dengan alasan; (5) revisi design card, threats, experiment card; (6) buka PR G5 dan release v0.3. Task ID resmi: lihat OPS-01 Sprint S8.

**Deliverable.** Slide pitch, notulen red team, desain revisi, PR G5.

**Gate.** G5 Method Ready (lulus). **Human check.** Orang lain dapat menjalankan desain ini tanpa bertanya ke tim; metrik dan baseline final.

## W9 — Repository

**Objective.** Repositori eksperimen siap dijalankan: kode, konfigurasi, seed, environment, README, dan data governance beres.

**Concept (30%).** Research repository sebagai artefak yang dapat diperiksa. Reproducibility package minimum. Data governance: data mentah sensitif tidak masuk GitHub ([SECURITY.md](../../SECURITY.md)), kartu dataset, lisensi per komponen ([LICENSING.md](../../LICENSING.md)). Struktur `experiments/` dan logging. Git hygiene: commit kecil, pesan bermakna, branch `research/g6-experiment`.

**Activity (70%).** Menyiapkan `src/`, `notebooks/`, `experiments/config`, `requirements.txt`/`environment.yml`, `run.sh`, `data/README.md`, `.gitignore`. Memuat data (subset) dan sanity check. Menulis stub baseline. Kode berbantuan AI direview dan diuji, dicatat di log.

**AI use.** Boleh: coding support, debugging, penjelasan error, membuat skrip utilitas. Tidak boleh: memasukkan data pribadi/partner ke AI; meng-commit kode AI yang tidak dibaca dan diuji.

**Microtasks.** (1) Susun struktur repo dan `.gitignore`; (2) tulis environment dan `run.sh`; (3) tulis `data/README.md` dan kartu dataset; (4) muat subset data dan sanity check (distribusi label, duplikasi, leakage awal); (5) implementasi baseline; (6) tulis `experiments/README.md`; (7) log semua bantuan AI pada kode. Task ID resmi: lihat OPS-01 Sprint S9.

**Deliverable.** Repositori siap eksperimen, kartu dataset (`DS-YYYY-NNN` bila baru), baseline berjalan.

**Gate.** G6 Experiment Ready (mulai). **Human check.** Mentor menjalankan `run.sh` di mesin lain; data sensitif tidak ada di riwayat git.

## W10 — Pilot

**Objective.** Minimum viable experiment berjalan end-to-end pada subset data dan direproduksi peer; G6 lulus.

**Concept (30%).** Pilot vs eksperimen penuh: tujuan pilot adalah membuktikan desain viable, bukan mengejar angka. Seed, variansi antar run, sanity check hasil (apakah baseline masuk akal, apakah akurasi "terlalu bagus" menandakan leakage). Logging eksperimen dan penyimpanan hasil di `results/`.

**Activity (70%).** Menjalankan baseline + minimal satu pembanding pada subset; mengulang dengan ≥3 seed bila relevan; menyimpan log dan hasil; peer dari tim lain mereproduksi angka baseline dari repositori dan menulis catatan; PR `GATE REVIEW: Experiment Ready`; release v0.5.

**AI use.** Boleh: debugging, interpretasi pesan error, saran sanity check. Tidak boleh: "memperbaiki" hasil dengan angka dari AI; menyembunyikan run yang gagal.

**Microtasks.** (1) Jalankan baseline dengan seed tetap; (2) jalankan pembanding; (3) ulangi dengan beberapa seed; (4) simpan log/hasil/figur awal; (5) sanity check leakage & distribusi; (6) minta peer mereproduksi dan catat; (7) buka PR G6, release v0.5. Task ID resmi: lihat OPS-01 Sprint S10.

**Deliverable.** Pilot results di `results/`, figur awal, catatan reproduksi peer, PR G6.

**Gate.** G6 Experiment Ready (lulus). **Human check.** Peer dapat mereproduksi angka baseline; hasil tidak hanya ada di laptop anggota tim.

## W11 — Analysis

**Objective.** Hasil pilot dianalisis dan divisualisasikan secara jujur, dengan ketidakpastian dan error analysis.

**Concept (30%).** Analyzing and visualizing evidence: perbandingan terhadap baseline, error analysis (di mana metode gagal dan mengapa), ketidakpastian (variansi antar seed/fold, interval bila relevan), uji statistik sederhana bila tepat, effect size dan practical significance. Visualisasi jujur: skala sumbu, baseline terlihat, tidak cherry-picking run.

**Activity (70%).** Notebook analisis; figur di `figures/`; `results/analysis.md` draft; catatan threats yang muncul dari data. Peer memeriksa satu figur: apakah bisa menyesatkan.

**AI use.** Boleh: penjelasan uji statistik, saran analisis, bantuan kode plotting. Tidak boleh: angka/tabel dari AI yang tidak dihitung sendiri; membiarkan AI "menginterpretasi" hasil tanpa memeriksa datanya.

**Microtasks.** (1) Tabel hasil vs baseline dengan variansi; (2) error analysis kualitatif pada contoh gagal; (3) uji/interval bila relevan; (4) buat 2–4 figur utama; (5) tulis `results/analysis.md` draft; (6) catat threats baru; (7) peer check figur. Task ID resmi: lihat OPS-01 Sprint S11.

**Deliverable.** `results/analysis.md` draft, figur, notebook analisis.

**Gate.** G7 Claim Ready (mulai). **Human check.** Dosen memeriksa satu figur terhadap data mentahnya.

## W12 — Contribution

**Objective.** Klaim ditetapkan sebatas bukti dengan struktur Claim–Evidence–Reasoning; G7 lulus.

**Concept (30%).** CER: klaim, bukti (tabel/figur), penalaran yang menghubungkan. Batas klaim: kausal vs korelasional, generalisasi ke populasi mana. Hasil negatif adalah hasil. Merevisi Contribution Statement agar tidak melebihi bukti. "So what?" bagi stakeholder.

**Activity (70%).** Menyusun CER table per RQ; memperbarui Threats v2; merevisi Contribution Statement; PR `GATE REVIEW: Claim Ready`.

**AI use.** Boleh: meminta AI menantang apakah klaim melebihi bukti. Tidak boleh: memakai kalimat klaim AI yang tidak didukung tabel/figur tim.

**Microtasks.** (1) Tulis CER per RQ; (2) tandai klaim yang tidak boleh dibuat; (3) perbarui Threats v2; (4) revisi Contribution Statement; (5) tulis "so what" untuk stakeholder; (6) buka PR G7. Task ID resmi: lihat OPS-01 Sprint S12.

**Deliverable.** CER table, Threats v2, Contribution Statement revisi, PR G7.

**Gate.** G7 Claim Ready (lulus). **Human check.** Setiap klaim menunjuk tabel/figur; tidak ada klaim kausal dari korelasi.

## W13 — Manuscript

**Objective.** Proposal TA (atau manuscript bila endgame paper) tersusun dari Research Pack; AI Usage Statement dan Reproducibility README ditulis.

**Concept (30%).** Scientific argumentation and writing: menulis dari artefak, bukan dari nol. Struktur IMRaD untuk computing dan pemetaannya ke proposal TA ([MET-05](05-publication-backward-design.md)). Citation integrity. AI dalam penulisan: penyuntingan bahasa dan struktur diperbolehkan dan diungkap; hasil dan klaim tidak.

**Activity (70%).** Menulis draft proposal/manuscript di `paper/`; `AI-USAGE.md`; Reproducibility README; release v0.8 Manuscript Draft.

**AI use.** Boleh: penyuntingan bahasa, umpan balik struktur, pengecekan konsistensi istilah; semuanya dicatat. Tidak boleh: menulis bagian hasil/diskusi dari AI; menambah sitasi yang tidak ada di `references.bib` yang terverifikasi.

**Microtasks.** (1) Petakan artefak Research Pack ke bagian proposal; (2) tulis Introduction & Related Work dari Problem Brief dan Evidence Map; (3) tulis Method dari design card; (4) tulis Pilot Results & Threats; (5) tulis `AI-USAGE.md`; (6) tulis Reproducibility README; (7) release v0.8. Task ID resmi: lihat OPS-01 Sprint S13.

**Deliverable.** Proposal/manuscript draft v0.8, `AI-USAGE.md`, Reproducibility README.

**Gate.** G8 Contribution Ready (mulai). **Human check.** Dosen membaca satu bagian dan memeriksa setiap sitasi ada di `references.bib`.

## W14 — Peer Review

**Objective.** Setiap mahasiswa menjadi reviewer untuk dua tim lain dan menerima review untuk timnya.

**Concept (30%).** Bagaimana peer review bekerja di computing. Etika reviewer: kerahasiaan, kritik pada gagasan, spesifik dan dapat ditindaklanjuti, menyebut bukti. Struktur [TPL-12](../08-templates/12-peer-review-template.md): problem, evidence, RQ, method, results, claim, limitations.

**Activity (70%).** Review silang terstruktur (double-blind bila memungkinkan); diskusi kalibrasi review di studio; tim membaca review yang diterima dan menyusun daftar tanggapan.

**AI use.** Boleh: memakai AI sebagai reviewer tambahan untuk draft tim sendiri, diungkap di log. Tidak boleh: membuat AI menulis review untuk tim lain; memasukkan draft tim lain ke layanan AI tanpa izin.

**Microtasks.** (1) Baca dua proposal tim lain; (2) tulis review dengan TPL-12; (3) kalibrasi di studio; (4) kirim review; (5) baca review yang diterima; (6) susun daftar tanggapan awal. Task ID resmi: lihat OPS-01 Sprint S14.

**Deliverable.** Dua review terkirim, review diterima, daftar tanggapan.

**Gate.** G8 (berlanjut). **Human check.** Dosen menilai kualitas review sebagai reviewer (CPMK-12), bukan hanya draft yang direview.

## W15 — Revision

**Objective.** Proposal direvisi berdasarkan review; Research Pack dilengkapi; integritas dan handoff disiapkan.

**Concept (30%).** Response to reviewers: terima/ubah/tolak dengan alasan. Disiplin revisi. Research Integrity Checklist ([TPL-11](../08-templates/11-research-integrity-checklist.md)). Handoff ke TA/mentor/AI Center ([TPL-14](../08-templates/14-research-handoff-template.md)).

**Activity (70%).** Revisi proposal; surat tanggapan; melengkapi seluruh artefak Research Pack wajib ([MET-04](04-research-pack-specification.md) §5); menandatangani TPL-11; menyusun handoff; finalisasi AI Usage Statement; latihan defense.

**AI use.** Boleh: pemeriksaan konsistensi dan bahasa, diungkap. Tidak boleh: mengubah angka hasil pada tahap revisi tanpa menjalankan ulang eksperimen dan mencatatnya.

**Microtasks.** (1) Klasifikasikan komentar reviewer; (2) revisi proposal; (3) tulis response letter; (4) lengkapi artefak Research Pack yang kurang; (5) isi dan tandatangani TPL-11; (6) tulis handoff; (7) latihan defense. Task ID resmi: lihat OPS-01 Sprint S15.

**Deliverable.** Proposal v1.0 draft, response letter, TPL-11, handoff draft.

**Gate.** G8 (berlanjut). **Human check.** Dosen memeriksa checklist integritas terhadap repositori (bukan hanya tanda tangan).

## W16 — Defense

**Objective.** Research Defense 7–10 menit; Research Pack v1.0 dirilis; handoff ke TA.

**Concept (30%).** Struktur defense ([TPL-13](../08-templates/13-research-defense-template.md)): masalah → bukti → RQ → desain → pilot → klaim & batasnya → rencana TA. Menjawab dengan bukti, mengakui batas tanpa diminta.

**Activity (70%).** Defense di hadapan dosen, mentor, penguji; release v1.0 Research Pack; PR `GATE REVIEW: Contribution Ready` merged; handoff final; self-assessment AI competency akhir; refleksi.

**AI use.** Boleh: latihan tanya-jawab. Tidak boleh: menampilkan hasil yang tidak ada di repositori.

**Microtasks.** (1) Finalisasi slide defense; (2) defense; (3) catat pertanyaan dan jawaban; (4) perbaikan minor pasca defense; (5) release v1.0; (6) merge PR G8; (7) handoff final dan perbarui Mission Control. Task ID resmi: lihat OPS-01 Sprint S16.

**Deliverable.** Research Pack v1.0, rekaman/notulen defense, handoff, status maturity (TA Ready / Research Ready / Publication Ready).

**Gate.** G8 Contribution Ready (lulus). **Human check.** Dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol.

---

## 3. Catatan implementasi

- **Kalender kampus.** Bila semester efektif kurang dari 16 pertemuan, gabungkan W14–W15 (peer review + revisi) sebagai satu sprint dua minggu di luar kelas; jangan memotong W7–W8 atau W10.
- **Tim yang tertinggal.** Gate berurutan; tim yang gagal G3 di W5 masih boleh mulai W6 secara paralel hanya untuk latihan, tetapi RQ tidak dianggap valid sebelum G3 lulus ([OPS-04](../06-execution-os/04-dependency-and-critical-path.md)).
- **Beban dosen.** Review gate dibagi dengan mentor dan peer reviewer terlatih (`@reviewers`); dosen pengampu memutuskan lulus/gagal.
- **Halaman mingguan mahasiswa.** Versi ringan setiap minggu (This Week / Tasks / Deliverable / AI Assist / Human Check / Done When) ada di `metopen-research-studio/weeks/` mulai dari [Week 01](../../metopen-research-studio/weeks/week-01-endgame.md) sampai [Week 16](../../metopen-research-studio/weeks/week-16-defense.md); dokumen ini adalah backend-nya.
