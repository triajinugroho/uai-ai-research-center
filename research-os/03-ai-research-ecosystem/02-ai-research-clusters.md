# AI Research Clusters — Empat Klaster Riset AI UAI

> **ID** AIR-02 · **Paket** 03 AI Research Ecosystem · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Pimpinan, research lead klaster, dosen, mahasiswa yang memilih topik, pengelola backlog dan Mission Control
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [AIR-01 AI Research Center Concept](01-ai-research-center-concept.md) · [AIR-03 Faculty Research Alignment](03-faculty-research-alignment.md) · [AIR-04 Cross-Faculty AI Model](04-cross-faculty-ai-model.md) · [ARC-02 Curriculum Research Map](../02-academic-architecture/02-curriculum-research-map.md) · [Research Roadmap](../../research-roadmap/README.md) · [.github/labels.yml](../../.github/labels.yml)

## 1. Mengapa empat klaster

Klaster adalah cara pusat riset mengelompokkan riset agar **dosen tahu di mana ia masuk, mahasiswa tahu ke mana bertanya, dan pimpinan tahu apa yang dikerjakan**. Empat klaster dipilih karena mencerminkan empat pertanyaan berbeda tentang AI: *apa* AI-nya (model, data, pengetahuan), *bagaimana* AI dibangun dan diamankan (sistem, software, keamanan), *untuk siapa dan dengan nilai apa* AI dibuat (manusia, tanggung jawab), dan *untuk masalah apa* AI diterapkan (domain kemaslahatan manusia).

Klaster bukan unit organisasi dengan anggota tetap. Ia adalah **label** pada riset, tim GitHub, dan lensa pada roadmap. Satu dosen dapat berada di dua klaster; satu riset punya satu klaster primer dan boleh satu sekunder (§8).

| Kode | Klaster | Pertanyaan inti | Label GitHub | Tim GitHub |
|---|---|---|---|---|
| **C1** | AI Models, Data & Knowledge | Bagaimana membangun dan mengevaluasi model, data, dan representasi pengetahuan yang lebih baik — terutama untuk konteks Indonesia? | `cluster:models` | `@ai-models` |
| **C2** | AI Systems, Software & Security | Bagaimana merekayasa, menguji, mengoperasikan, dan mengamankan sistem AI? | `cluster:systems` | `@ai-systems` |
| **C3** | Human-Centered & Responsible AI | Bagaimana AI dirancang, dievaluasi, dan diatur agar berguna, adil, transparan, dan aman bagi manusia? | `cluster:human-ai` | `@responsible-ai` |
| **C4** | Applied AI for Human Flourishing | Bagaimana AI menyelesaikan masalah nyata di pendidikan, halal, kesehatan, pangan, pemerintahan, bisnis, dan dampak sosial? | `cluster:applied` | `@applied-ai` |

## 2. Lensa lintas klaster: AI Core / AI Enabling / AI Application / Responsible AI

Empat istilah di [Glossary §4.2](../00-master/03-glossary.md) adalah **lensa peran AI dalam sebuah riset**, bukan klaster tandingan. Setiap riset dapat dilihat lewat satu atau lebih lensa:

| Lensa | Objek riset | Klaster yang paling sering memakainya |
|---|---|---|
| **AI Core** | AI itu sendiri: model, data, knowledge, algoritma, evaluasi | C1 |
| **AI Enabling** | Infrastruktur yang memungkinkan AI: sistem, software engineering, keamanan, data engineering | C2 |
| **AI Application** | Penerapan AI ke domain | C4 (dan C3 bila domainnya interaksi manusia) |
| **Responsible AI** | Keadilan, privasi, keamanan, transparansi, akuntabilitas, nilai kemanusiaan | C3 — tetapi **wajib menjadi lensa setiap riset** di semua klaster |

Matriks klaster × lensa (● = fokus utama, ○ = lazim hadir):

| | AI Core | AI Enabling | AI Application | Responsible AI |
|---|---|---|---|---|
| C1 Models, Data & Knowledge | ● | ○ | ○ | ○ |
| C2 Systems, Software & Security | ○ | ● | ○ | ○ |
| C3 Human-Centered & Responsible AI | ○ | ○ | ○ | ● |
| C4 Applied AI | ○ | ○ | ● | ○ |

Aturan praktis: klaster ditentukan oleh **kontribusi utama** riset (apa yang baru), bukan oleh domain atau alat. Riset "model klasifikasi teks Bahasa Indonesia untuk keluhan layanan kesehatan" yang kontribusinya adalah *benchmark dan model* masuk C1 (sekunder C4); bila kontribusinya adalah *dampak pada alur layanan* masuk C4 (sekunder C1).

## 3. C1 — AI Models, Data & Knowledge

**Scope.** Riset yang objeknya AI itu sendiri: model machine learning/deep learning, data-centric AI, representasi pengetahuan, NLP (khususnya Bahasa Indonesia dan bahasa daerah), computer vision, evaluasi dan benchmark model, efisiensi model, retrieval-augmented generation, dan metode evaluasi LLM.

**Example topics (konteks Indonesia/UAI).**

1. Benchmark kecil NLP Bahasa Indonesia untuk tugas layanan akademik (klasifikasi tiket, ekstraksi entitas).
2. Evaluasi RAG untuk dokumen regulasi/akademik Bahasa Indonesia: seberapa sering jawaban tidak berdasar sumber (grounding).
3. Data-centric AI: pengaruh kualitas anotasi terhadap kinerja model pada korpus kecil.
4. Stabilitas kinerja model prediksi mahasiswa berisiko lintas angkatan (replikasi dan generalisasi).
5. Representasi pengetahuan produk halal (ontologi bahan, sertifikasi) untuk penalaran otomatis.
6. Klasifikasi citra produk/label kemasan untuk verifikasi informasi halal.
7. Model ringan (efisien) untuk perangkat terbatas dalam konteks IoT kampus.
8. Evaluasi bias bahasa pada LLM multibahasa untuk Bahasa Indonesia.

**Related courses.** AI & Machine Learning (R), Data Mining (E→R), NLP (R), Statistika Terapan (F), Basis Data (F→E), Analisis Algoritma (F→E).

**Possible faculty.** `[isi]` — kriteria: kepakaran machine learning, NLP, computer vision, data mining, statistika/matematika terapan, atau basis data/knowledge engineering; dosen dengan latar matematika/statistika masuk lewat evaluasi dan inferensi ([AIR-03](03-faculty-research-alignment.md)).

**Possible datasets (jenis).** Korpus teks Bahasa Indonesia (layanan, regulasi, media) dengan anotasi; data pembelajaran mahasiswa anonim (contoh sumber: *student learning*); katalog produk halal (contoh sumber: *halal products*); korpus NLP Indonesia (contoh sumber: *Indonesian NLP*); citra produk/label; dataset publik yang direplikasi.

**Outputs.** Benchmark, dataset dengan pedoman anotasi, model dengan model card, paper empiris/replikasi, software evaluasi.

**Contoh Research ID hipotetis.** `UIAI-2026-003` "Benchmark klasifikasi tiket layanan akademik Bahasa Indonesia" (primer C1, sekunder C4/Education); `UIAI-2026-011` "Grounding evaluation RAG dokumen akademik" (primer C1, sekunder C2).

## 4. C2 — AI Systems, Software & Security

**Scope.** Riset tentang infrastruktur yang memungkinkan AI: rekayasa perangkat lunak untuk sistem AI (SE4AI) dan AI untuk rekayasa perangkat lunak (AI4SE), MLOps, pengujian sistem ML/LLM, keandalan, kinerja dan biaya, keamanan sistem AI (adversarial, prompt injection, kebocoran data), privasi teknis, data engineering, dan sistem IoT/edge AI.

**Example topics.**

1. Metamorphic dan robustness testing untuk model klasifikasi teks/gambar hasil kelas AI/ML.
2. Threat model dan evaluasi ketahanan sistem berbasis LLM di lingkungan kampus (prompt injection, kebocoran data pribadi).
3. Pipeline reproducible untuk eksperimen ML mahasiswa: apa yang paling sering merusak reproducibility?
4. Pengaruh alat coding berbasis AI terhadap kualitas kode dan pengujian pada proyek RPL (empirical SE study).
5. MLOps ringan untuk institusi kecil: monitoring drift model prediksi akademik.
6. Arsitektur edge AI untuk sensor kampus (energi, kehadiran) dengan batasan daya.
7. Keamanan dan privasi pada integrasi chatbot layanan dengan data mahasiswa.
8. Benchmark biaya–kinerja inferensi LLM lokal vs API untuk kasus institusi.

**Related courses.** RPL (E), Pengujian Perangkat Lunak (E), Proyek Perangkat Lunak (E→R), Struktur Data (F), Analisis Algoritma (F→E), Keamanan (E→R), IoT (E), Basis Data (F→E).

**Possible faculty.** `[isi]` — kriteria: kepakaran rekayasa perangkat lunak, pengujian, jaringan/keamanan, sistem terdistribusi, basis data/data engineering, IoT/embedded; dosen jaringan masuk lewat keamanan sistem AI, dosen basis data lewat data engineering.

**Possible datasets (jenis).** Repositori kode proyek mahasiswa (anonim) untuk empirical SE; log sistem/aplikasi; data sensor IoT; kumpulan prompt/serangan untuk pengujian; hasil benchmark inferensi.

**Outputs.** Software/tools (test harness, pipeline), benchmark sistem, paper empirical SE, prototype sistem, laporan keamanan.

**Contoh Research ID hipotetis.** `UIAI-2026-008` "Ketahanan chatbot layanan akademik terhadap prompt injection" (primer C2, sekunder C3); `UIAI-2026-014` "Reproducibility eksperimen ML mahasiswa: studi empiris" (primer C2, sekunder C3/Education).

## 5. C3 — Human-Centered & Responsible AI

**Scope.** Riset tentang manusia dan nilai dalam AI: HCI untuk sistem AI, evaluasi pengguna, explainability, fairness, privasi, transparansi, akuntabilitas, AI dalam pendidikan (pedagogi, penilaian, integritas akademik), literasi AI, etika AI dalam perspektif nilai keislaman dan kemanusiaan, serta tata kelola AI institusional.

**Example topics.**

1. Bagaimana mahasiswa memakai GenAI dalam tugas akademik dan dampaknya pada kualitas argumentasi (studi empiris + AI Usage Log).
2. Evaluasi fairness model deteksi dini mahasiswa berisiko antar kelompok mahasiswa.
3. Explainability untuk dosen wali: penjelasan model seperti apa yang dapat ditindaklanjuti?
4. User study chatbot konsultasi akademik: kepercayaan, kesalahan, dan perilaku verifikasi pengguna.
5. Kerangka amanah epistemik sebagai instrumen penilaian integritas riset berbantuan AI.
6. Privasi dan consent pada penggunaan data LMS untuk analitik pembelajaran.
7. Literasi AI dan verifikasi: intervensi apa yang membuat mahasiswa lebih sulit dibohongi AI?
8. Tata kelola AI di perguruan tinggi: kebijakan disclosure dan efeknya.
9. Desain antarmuka yang mendorong verifikasi sumber pada asisten riset berbasis LLM.

**Related courses.** HCI (E), Etika Profesi (F→E), Metodologi Penelitian (R), Statistika/Statistika Terapan (F), Proyek Perangkat Lunak (E→R).

**Possible faculty.** `[isi]` — kriteria: kepakaran HCI, pendidikan/teknologi pembelajaran, etika profesi, psikologi (lintas fakultas), hukum/kebijakan (lintas fakultas), statistika untuk studi manusia.

**Possible datasets (jenis).** Data pembelajaran mahasiswa anonim (LMS, nilai, kehadiran) dengan consent; AI Usage Log Metopen (anonim, agregat); transkrip interaksi pengguna–chatbot (anonim); survei dan wawancara; hasil user study.

**Outputs.** Paper empiris/user study, instrumen dan protokol evaluasi, kebijakan/brief institusional, dataset interaksi (restricted), prototype antarmuka.

**Contoh Research ID hipotetis.** `UIAI-2026-017` "Stabilitas dan fairness deteksi dini mahasiswa berisiko" (primer C3, sekunder C4/Education; lihat [ARC-04 §10](../02-academic-architecture/04-build-prove-contribute.md)); `UIAI-2026-019` "Perilaku verifikasi mahasiswa terhadap output AI dalam Metopen" (primer C3).

## 6. C4 — Applied AI for Human Flourishing

**Scope.** Riset yang menerapkan AI untuk masalah nyata pada tujuh domain roadmap — **Education, Halal, Health, Food, Government, Business, Social Impact** — dengan kontribusi utama pada *dampak dan evaluasi dalam domain*. Klaster ini adalah rumah utama kolaborasi lintas fakultas ([AIR-04](04-cross-faculty-ai-model.md)) dan masalah mitra ([AIR-05](05-research-demand-supply-marketplace.md)).

**Example topics.**

1. Sistem rekomendasi/verifikasi informasi halal untuk konsumen dan UMKM (Halal, dengan Teknologi Pangan/Hukum).
2. Estimasi asupan gizi dari citra makanan lokal dan evaluasinya dengan ahli gizi (Health/Food, dengan Gizi).
3. Deteksi dini mahasiswa berisiko dan uji intervensi bersama bagian akademik (Education).
4. Analisis sentimen dan topik aduan layanan publik Bahasa Indonesia untuk pemerintah daerah (Government, dengan Komunikasi).
5. Asisten dokumen hukum/regulasi berbasis RAG untuk UMKM dan evaluasi kebergunaannya (Business/Government, dengan Hukum/Ekonomi).
6. Prediksi permintaan dan pengurangan limbah pangan pada kantin/dapur institusi (Food/Business).
7. AI untuk pembelajaran bahasa (Arab/Inggris) dengan evaluasi pedagogis (Education, dengan Bahasa).
8. Deteksi kesejahteraan psikologis dari data self-report dengan tata kelola privasi ketat (Health, dengan Psikologi).
9. Pemetaan kebutuhan sosial komunitas dari data terbuka untuk program pengabdian (Social Impact).

**Related courses.** Proyek Perangkat Lunak (E→R), Kerja Praktik (E, problem discovery), Data Mining (E→R), AI & Machine Learning (R), Tugas Akhir (R), HCI (E).

**Possible faculty.** `[isi]` — Informatika sebagai penyedia kapabilitas AI + dosen domain dari fakultas mitra sebagai problem owner dan evaluator; kriteria: kepakaran domain dengan masalah nyata dan akses data.

**Possible datasets (jenis).** Katalog produk halal dan bahan (contoh sumber: *halal products*); data gizi/menu; data layanan publik/aduan (anonim); data UMKM; data pembelajaran (contoh sumber: *student learning*); data terbuka pemerintah; data survei komunitas.

**Outputs.** Prototype terevaluasi, research brief untuk mitra, paper aplikasi, dataset domain (sering restricted), HKI, adopsi mitra.

**Contoh Research ID hipotetis.** `UIAI-2026-021` "Asisten verifikasi informasi halal untuk UMKM" (primer C4/Halal, sekunder C1); `UIAI-2026-025` "Estimasi porsi makanan lokal dari citra dengan evaluasi ahli gizi" (primer C4/Health, sekunder C1).

## 7. Ringkasan lintas klaster

| | C1 Models, Data & Knowledge | C2 Systems, Software & Security | C3 Human-Centered & Responsible | C4 Applied AI |
|---|---|---|---|---|
| Kontribusi khas | Model, data, benchmark, evaluasi | Tools, pipeline, pengujian, keamanan | Bukti tentang manusia & nilai; instrumen; kebijakan | Dampak domain; prototype; brief |
| Metode dominan | ML research, benchmarking, replikasi | Empirical SE, experiment, design science | User study, survey, experiment, qualitative | Design science, case study, field evaluation |
| MK sumber utama | AI/ML, NLP, Data Mining | RPL, Pengujian PL, Proyek PL, Keamanan | HCI, Etika Profesi, Metopen | Proyek PL, KP, TA |
| Mitra khas | Komunitas NLP Indonesia, penyedia data | Unit TI kampus, industri software | Bagian akademik, psikologi, hukum | Fakultas mitra, pemerintah, UMKM |
| Output khas | Benchmark, dataset, model | Software, benchmark sistem | Paper empiris, brief kebijakan | Prototype, brief, HKI |

## 8. Aturan penetapan klaster primer dan sekunder

1. **Satu klaster primer wajib** untuk setiap Issue `type:problem` dan setiap riset ber-Research ID; label `cluster:*` dan field *Cluster* di Mission Control memakai klaster primer.
2. **Klaster primer = kontribusi utama.** Tanyakan: "Kalau riset ini berhasil, apa yang baru — model/data (C1), sistem/keamanan (C2), pemahaman tentang manusia/nilai (C3), atau dampak domain (C4)?"
3. **Maksimal satu klaster sekunder**, dicatat di Research One-Pager dan README riset (bukan label kedua) agar board tidak ganda.
4. **Domain ≠ klaster.** Semua riset punya domain (Education, Halal, …) di field *Domain*; riset C1–C3 pun punya domain. Domain menentukan mitra dan dataset; klaster menentukan metode dan reviewer.
5. **Responsible AI adalah lensa wajib**, bukan alasan memasukkan semua riset ke C3. Riset masuk C3 hanya bila kontribusi utamanya tentang manusia/nilai.
6. **Penetapan** oleh pengusul saat membuat Issue; **validasi** oleh research lead klaster saat triase; perubahan klaster dicatat di Issue.
7. **Riset lintas klaster** (mis. benchmark C1 yang lahir dari kebutuhan C4) mendapat reviewer dari kedua klaster pada G5 dan G7.

## 9. Klaster × domain roadmap

| Domain | C1 | C2 | C3 | C4 | Contoh masalah |
|---|---|---|---|---|---|
| Education | ● | ○ | ● | ● | Deteksi dini, GenAI dalam tugas, chatbot akademik |
| Halal | ● | ○ | ○ | ● | Verifikasi informasi halal, ontologi bahan |
| Health | ● | ○ | ● | ● | Estimasi gizi dari citra, kesejahteraan psikologis |
| Food | ○ | ● | ○ | ● | Limbah pangan, rantai pasok |
| Government | ● | ● | ● | ● | Aduan layanan publik, asisten regulasi |
| Business | ○ | ● | ○ | ● | UMKM, prediksi permintaan |
| Social Impact | ○ | ○ | ● | ● | Pemetaan kebutuhan komunitas |

Dokumen domain ada di [research-roadmap/domains/](../../research-roadmap/domains/education.md); dokumen klaster di [research-roadmap/clusters/](../../research-roadmap/clusters/ai-models-data-knowledge.md).

## 10. Tata kelola klaster

- Setiap klaster punya **satu research lead** (`@research-leads`) — dosen dengan kepakaran terdekat; ditinjau tahunan.
- Research lead: memvalidasi backlog klaster, menyediakan/menunjuk mentor dan reviewer gate, mengusulkan prioritas tahunan, melaporkan portofolio klaster per semester (view *By Research Cluster* di Mission Control).
- Klaster tidak punya anggaran atau anggota tetap; sumber daya mengikuti riset yang lolos gate.
- Klaster baru atau perubahan scope diajukan lewat PR ke dokumen ini dan [GOVERNANCE.md](../../GOVERNANCE.md) (label/tim) serta dicatat di CHANGELOG.

## 11. Ringkasan

- Empat klaster menjawab empat pertanyaan: apa AI-nya (C1), bagaimana dibangun dan diamankan (C2), untuk siapa dan dengan nilai apa (C3), untuk masalah apa (C4).
- AI Core / Enabling / Application / Responsible AI adalah lensa, bukan klaster; Responsible AI wajib pada semua riset.
- Satu klaster primer per riset ditentukan oleh kontribusi utama; domain dicatat terpisah.
- Klaster adalah label dan tim, bukan unit dengan anggota tetap; research lead memvalidasi dan memfasilitasi.
