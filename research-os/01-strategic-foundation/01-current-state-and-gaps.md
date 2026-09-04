# Current State & Gaps — Posisi Saat Ini, Ideal, dan Sweet Spot

> **ID** STR-01 · **Paket** 01 Strategic Foundation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, tim kurikulum, dosen pengampu Metopen/AI-ML/TA, tim PP-PTS, reviewer internal
> **Terkait** [MST-01 Executive Summary](../00-master/01-executive-summary.md) · [STR-02 Vision & Endgame](02-vision-and-endgame.md) · [STR-03 Design Principles](03-design-principles.md) · [ARC-02 Curriculum Research Map](../02-academic-architecture/02-curriculum-research-map.md) · [MET-01 Metopen Positioning](../04-metopen-research-studio/01-metopen-positioning.md)

Dokumen ini menjawab pertanyaan pertama dari tujuh layer berpikir: **mengapa Metodologi Penelitian dan pipeline riset Prodi perlu direposisi?** Jawabannya disusun dalam tiga bagian: posisi saat ini, tujuh kategori gap, dan peta *current → ideal → sweet spot* yang menjadi dasar seluruh desain paket berikutnya.

> **Catatan transparansi.** Saat analisis dilakukan, struktur kurikulum resmi dan panduan kurikulum UAI ditemukan, tetapi **RPS Metodologi Penelitian Informatika UAI terkini yang dipublikasikan resmi belum ditemukan**. Kolom "current" di seluruh dokumen ini adalah posisi yang *terlihat* dari arsitektur kurikulum publik, bukan klaim bahwa dosen sebelumnya mengajarkannya seperti itu. Semua fakta institusional bersumber dari dokumen diskusi *"Riset AI UAI untuk Negeri"* dan wajib diverifikasi sebelum dipakai dalam dokumen formal.

---

## 1. Current state

### 1.1 Posisi tiga mata kuliah kunci

| Mata kuliah | SKS | Semester | Peran dalam pipeline |
|---|---|---|---|
| AI & Machine Learning | 4 | V | Kandidat utama **Build**: menghasilkan research asset (dataset, baseline, kode) |
| Metodologi Penelitian (Metopen) | 2 | VII | **Prove**: evidence-quality gate; integration layer atas enam semester sebelumnya; launchpad TA |
| Tugas Akhir (TA) | 4 | VIII | **Contribute**: eksekusi penuh dan kontribusi pengetahuan/artefak |

Metopen berada pada posisi yang sangat strategis: bukan mata kuliah pengantar, melainkan seharusnya menjadi *integration layer* atas hampir semua kompetensi enam semester sebelumnya dan *launchpad* menuju TA semester VIII.

### 1.2 Fondasi kurikulum semester 1–8

Sumber: dokumen diskusi; verifikasi sebelum dokumen formal.

| Tahap | Fondasi relevan |
|---|---|
| Semester 1 | Statistika 3 SKS, Kalkulus |
| Semester 2 | Statistika Terapan 3 SKS, Matematika Diskrit |
| Semester 3 | HCI, Struktur Data, Basis Data |
| Semester 4 | Analisis Algoritma, RPL, Data Mining |
| Semester 5 | AI & Machine Learning 4 SKS, Pengujian Perangkat Lunak |
| Semester 6 | Proyek Perangkat Lunak 4 SKS, Kerja Praktik, Etika Profesi |
| Semester 7 | **Metodologi Penelitian 2 SKS** |
| Semester 8 | **Tugas Akhir 4 SKS** |

Kesimpulan yang penting: problem utamanya **bukan** "mahasiswa belum pernah mendapat statistik atau teknologi". Mereka sudah mendapat cukup banyak. Problem yang perlu diselesaikan Metopen adalah: **bisakah mahasiswa mengubah kemampuan teknis tersebut menjadi pengetahuan baru yang evidence-based?** Itu game yang berbeda.

Prodi juga sudah memosisikan kompetensinya pada Software Engineering, Data Science, IoT, dan NLP, dengan visi yang menggabungkan kemampuan intelektual dengan nilai spiritual, moral, dan etika Islami; misinya menyebut optimalisasi riset melalui laboratorium dan kolaborasi eksternal (sumber: dokumen diskusi; verifikasi sebelum dokumen formal).

### 1.3 Komponen ekosistem riset saat ini

| Komponen | Posisi yang terlihat | Bukti yang tersedia di repo |
|---|---|---|
| **Proyek mata kuliah** | Berjalan di AI/ML, Data Mining, RPL, Proyek Perangkat Lunak; hasilnya dinilai lalu berhenti sebagai nilai | Belum ada artefak riil di [`research-based-learning/courses/`](../../research-based-learning/README.md); diisi Phase 3 |
| **Penelitian dosen** | Ada skema penelitian internal UAI 2026 yang mendorong keterlibatan minimal dua mahasiswa aktif dan topik selaras Renstra Penelitian | Peta dosen memakai placeholder `[isi]` di [TPL-07](../08-templates/07-faculty-research-map-template.md) |
| **Publikasi mahasiswa** | Tidak tercatat terstruktur; tidak ada registry | [`publications/`](../../publications/README.md) kosong sampai pilot menghasilkan naskah |
| **Dataset** | Tersebar; tanpa metadata, lisensi, dan pemilik yang jelas | [`datasets-registry/`](../../datasets-registry/README.md) baru berisi template dan contoh |
| **Roadmap riset** | Renstra Penelitian universitas ada; roadmap Prodi/pusat riset AI dirumuskan baru di repo ini | [`research-roadmap/`](../../research-roadmap/README.md) 2026–2030 (draft) |
| **Akreditasi** | UAI berstatus Unggul; Informatika berstatus Baik Sekali per SK LAM-INFOKOM 2025, berlaku hingga Maret 2030 | Sumber: dokumen diskusi; verifikasi sebelum dokumen formal |

Satu mata kuliah tidak akan menaikkan akreditasi. Tetapi Metopen dapat menjadi salah satu *control point* untuk membangun rantai: **mahasiswa → TA → riset dosen → publikasi → dataset/code/artifact → reputasi akademik → evidence akreditasi → kualitas intake mahasiswa → riset lebih baik.**

## 2. Tujuh kategori gap

### GAP-1 Course-project fragmentation
Proyek mata kuliah dirancang untuk menilai kompetensi, bukan untuk diwariskan. Kode ada di laptop mahasiswa, dataset tidak terdaftar, temuan tidak dituliskan sebagai problem brief. Angkatan berikutnya mengulang eksperimen yang sama tanpa tahu hasil sebelumnya. Prinsip yang dilanggar: *research assets should compound* ([STR-03](03-design-principles.md)).

### GAP-2 Metopen–TA fragmentation
Metopen menghasilkan proposal sebagai dokumen; TA dimulai sebagai proses terpisah dengan pembimbing yang sering belum melihat proposal itu. Mahasiswa masuk semester VIII masih mencari judul. Waktu satu semester penuh hilang untuk pekerjaan yang seharusnya selesai di Metopen: problem, evidence map, RQ, desain, dan pilot.

### GAP-3 Faculty–student research fragmentation
Riset dosen dan riset mahasiswa berjalan di dua jalur. Skema penelitian internal mensyaratkan keterlibatan mahasiswa, tetapi tidak ada mekanisme *matching* yang membuat mahasiswa TA-ready tersedia bagi dosen pada waktu yang tepat. Hubungan dosen–mahasiswa "tidak selalu terstruktur", padahal idealnya *research apprenticeship*.

### GAP-4 Dataset fragmentation
Tidak ada katalog. Tidak diketahui dataset apa yang pernah dikumpulkan, siapa pemiliknya, apa lisensinya, apakah mengandung data pribadi. Akibatnya riset baru selalu mulai dari pengumpulan data, dan risiko privasi tidak terkelola.

### GAP-5 Research-roadmap disconnect
Topik TA dan proyek MK dipilih berdasarkan minat sesaat, bukan diarahkan ke roadmap riset Prodi, klaster AI Research Center, Renstra Penelitian UAI, atau prioritas nasional. Hasilnya portofolio yang tersebar dan tidak membangun kedalaman pada tema mana pun.

### GAP-6 Publication downstream thinking
Publikasi dipikirkan setelah TA selesai, bukan dirancang mundur dari venue target sejak awal. Akibatnya naskah tidak pernah ditulis, atau ditulis untuk venue yang tidak tepat, termasuk risiko jurnal predator.

### GAP-7 AI use without systematic research literacy
Mahasiswa sudah memakai GenAI untuk mencari literatur, menulis, dan coding. Tanpa protokol, hasilnya referensi fiktif, klaim tanpa bukti, dan proposal yang "terdengar ilmiah". Kelas *AI-free* tidak realistis; kelas "pakai ChatGPT bikin proposal" tidak dapat dipertanggungjawabkan. Kebijakan publikasi ACM terkini membedakan AI sebagai alat bantu penulisan dari AI di dalam proses riset yang memengaruhi kesimpulan; yang terakhir harus dijelaskan dalam metode, dan peneliti tetap bertanggung jawab (sumber: dokumen diskusi; verifikasi sebelum dokumen formal).

## 3. Matriks Current → Problem → Consequence → Ideal → Intervention

| Gap | Current | Problem | Consequence | Ideal | Intervention di repo ini |
|---|---|---|---|---|---|
| GAP-1 Course project | Proyek MK dinilai lalu berhenti | Tidak ada mekanisme reuse | Setiap angkatan mulai dari nol; tidak ada research asset | MK teknis menghasilkan reusable research asset | Mode F/E/R per MK ([ARC-03](../02-academic-architecture/03-ai-contribution-modes.md)); `research-artifact.md` per MK ([`research-based-learning/`](../../research-based-learning/README.md)); Research ID sejak proyek MK |
| GAP-2 Metopen–TA | Proposal dokumen; TA terpisah | Tidak ada handoff; proposal tidak diuji viabilitasnya | Semester VIII habis untuk mencari judul; TA lemah, solution-first | Proposal Metopen langsung menjadi TA | Research Pack sebagai deliverable ([MET-04](../04-metopen-research-studio/04-research-pack-specification.md)); 8 gate ([OPS-03](../06-execution-os/03-research-gates.md)); handoff ([TPL-14](../08-templates/14-research-handoff-template.md)) |
| GAP-3 Dosen–mahasiswa | Jalur terpisah | Tidak ada matching terstruktur | Skema hibah sulit dipenuhi; mahasiswa tanpa apprenticeship | Lab/faculty research matching | Faculty research map ([AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md), [TPL-07](../08-templates/07-faculty-research-map-template.md)); mentor sebagai reviewer gate ([GOV-01](../07-governance/01-governance-model.md)); entry door *Faculty Research* |
| GAP-4 Dataset | Tersebar di laptop | Tanpa katalog, lisensi, privasi | Riset selalu mulai dari pengumpulan data; risiko privasi | Dataset registry dengan metadata & governance | [`datasets-registry/`](../../datasets-registry/README.md) + [TPL-05](../08-templates/05-dataset-registry-template.md); `DS-YYYY-NNN`; data mentah tidak masuk GitHub |
| GAP-5 Roadmap | Topik berdasarkan minat sesaat | Tidak terhubung roadmap/Renstra/nasional | Portofolio tersebar, tanpa kedalaman | Topik diarahkan ke klaster & domain roadmap | [`research-roadmap/`](../../research-roadmap/README.md) 4 klaster × 7 domain; field Cluster/Domain di Mission Control; G2 mensyaratkan keselarasan klaster |
| GAP-6 Publikasi | Dipikirkan setelah TA | Tanpa backward design; risiko venue predator | Naskah tidak ditulis; publikasi minim | Publication backward design dari venue target | [MET-05](../04-metopen-research-studio/05-publication-backward-design.md); venue registry ([TPL-06](../08-templates/06-publication-venue-registry-template.md)); [`publications/`](../../publications/README.md) |
| GAP-7 AI literacy | AI dipakai tanpa protokol | Tidak ada verifikasi & pengungkapan | Referensi fiktif, klaim kosong, integritas rapuh | AI-augmented, human-accountable science | AI Research Protocol ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)); AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)); integrity gate ([TPL-11](../08-templates/11-research-integrity-checklist.md)) |

## 4. Current vs Ideal vs Sweet Spot (20 dimensi)

Tabel ini adalah inti analisis dan dimuat lengkap sebagaimana dokumen sumber. Kolom **Sweet Spot Informatika UAI** adalah target desain seluruh paket berikutnya.

| Dimensi | Current visible position | Ideal global/frontier | Sweet Spot Informatika UAI |
|---|---|---|---|
| Tujuan | Persiapan penelitian/TA | Melatih independent researcher | **TA-ready novice computer scientist** |
| Fokus | Proposal penelitian | Full research lifecycle | **Problem → Evidence → Method → Pilot → Proposal** |
| Sifat | General research methodology | Specialized disciplinary methods | **Computing-specific research methods** |
| Starting point | "Apa itu penelitian?" | Research problem | **Wicked/problem worth solving** |
| Literatur | Tinjauan pustaka | Critical synthesis / evidence base | **Literature intelligence + evidence map** |
| Research gap | Naratif | Defensible scientific contribution | **Gap–Claim–Evidence alignment** |
| Metode | Quantitative / qualitative | Methodological pluralism | **Experiment, benchmark, design science, case study, survey, user study, ML evaluation** |
| Statistik | Konsep statistik | Rigorous inference | **Enough statistics to prevent bad claims** |
| Coding | Pendukung | Reproducible research software | **Notebook/repository as research artifact** |
| AI | Bisa menjadi shortcut mahasiswa | AI-aware research methodology | **AI as research copilot, not epistemic authority** |
| Evaluasi AI/ML | Accuracy oriented | Multi-dimensional rigorous evaluation | **baseline, metric, benchmark, ablation/error analysis** |
| Validitas | Definisi | Internal/external/construct/statistical validity | **Threats-to-validity wajib** |
| Reproducibility | Opsional | Core scholarly norm | **minimum reproducibility package** |
| Etika | Plagiarisme | Responsible research | **integrity + privacy + human subjects + bias + AI disclosure** |
| Writing | Format proposal | Scientific argumentation | **claim-evidence-reasoning** |
| Output | Proposal | Paper/research artifact | **Research Pack + proposal TA** |
| Assessment | UTS/UAS | Authentic assessment | **milestone portfolio + defense** |
| Hubungan TA | Prasyarat | Embedded research pipeline | **proposal Metopen langsung menjadi TA** |
| Hubungan dosen | Tidak selalu terstruktur | Research apprenticeship | **lab/faculty research matching** |
| Outcome ekosistem | Nilai mata kuliah | Research capacity | **TA → paper/artifact/grant pipeline** |

### 4.1 Mengapa sweet spot sengaja di bawah ideal frontier

Benchmark yang dipakai (sumber: dokumen diskusi; verifikasi sebelum dokumen formal): University of Sydney Research Methods 2026 (literature evaluation, research plan, quality metrics, ethics); Mälardalen (RQ/hipotesis, literature search, analisis kuantitatif–kualitatif, proposal, threats to validity, ethics); University of Houston (experimental design, statistics, membaca dan mereview paper, visualisasi, writing, oral presentation, "CS research in the post-AI world", proyek riset sepanjang semester); Princeton 2026 (causal inference, experiments, regression, benchmark, quasi-experiments, causal ML, LLM labeling); dan BINUS *Research Methodology in Computer Science* 2 SCU (research lifecycle, literature, framework, design, data, ethics, publication, proposal presentation, peer review).

Semuanya tidak bisa dijejalkan ke 2 SKS. Kalau dipaksa: **semua dikenalkan, tidak ada yang dikuasai.** Mahasiswa S1 semester VII tidak membutuhkan advanced causal inference, advanced Bayesian statistics, full systematic review, atau graduate-level epistemology. Mereka membutuhkan **minimum methodological sophistication required to stop producing weak research.** Prinsip Pareto; Occam.

```
RESEARCH PRACTICE / DOING
        ▲
        │                        IDEAL FRONTIER  ●
        │
        │                 SWEET SPOT UAI  ★
        │
        │   CURRENT  ●
        │
        └──────────────────────────────────────────►
      GENERAL METHODS                 COMPUTING-SPECIFIC
        THEORY / KNOWING
```

Sweet spot bergerak ke kanan (computing-specific) dan ke atas (doing), tetapi berhenti sebelum frontier. Satu langkah lebih jauh dari BINUS: bukan sekadar *Research Methodology in Computer Science*, melainkan **Responsible AI-Augmented Evidence Engineering**.

## 5. Dari gap ke desain

| Gap | Dijawab oleh layer | Paket |
|---|---|---|
| GAP-1, GAP-5 | Academic Architecture, Ecosystem | [02](../02-academic-architecture/01-research-capability-spiral.md), [03](../03-ai-research-ecosystem/01-ai-research-center-concept.md) |
| GAP-2, GAP-6 | Metopen Studio, Execution | [04](../04-metopen-research-studio/01-metopen-positioning.md), [06](../06-execution-os/03-research-gates.md) |
| GAP-3 | Ecosystem, Governance | [03](../03-ai-research-ecosystem/03-faculty-research-alignment.md), [07](../07-governance/01-governance-model.md) |
| GAP-4 | Registry & template | [08](../08-templates/05-dataset-registry-template.md), [`datasets-registry/`](../../datasets-registry/README.md) |
| GAP-7 | AI-Augmented Research | [05](../05-ai-augmented-research/04-ai-research-protocol.md) |

Ke mana arah semua ini: [STR-02 Vision & Endgame](02-vision-and-endgame.md). Prinsip yang mengikat desainnya: [STR-03 Design Principles](03-design-principles.md).
