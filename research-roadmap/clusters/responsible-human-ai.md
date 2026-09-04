# C3 — Human-Centered & Responsible AI

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [MET-07 Research Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) · [alignment/uai.md](../alignment/uai.md)

| Field | Nilai |
|---|---|
| Kode | **C3** |
| Peran AI | **Responsible AI** — keadilan, privasi, keamanan, transparansi, akuntabilitas, nilai kemanusiaan; ditambah **human-centered**: bagaimana manusia memakai, memahami, dan mempercayai AI |
| Label GitHub | `cluster:human-ai` |
| Tim GitHub | `@responsible-ai` |
| Program terkait | `program-responsible-ai` (2027), `program-ai-education` (2027) |
| Signature UAI | **amanah epistemik** — kejujuran terhadap kebenaran meskipun meruntuhkan hipotesis sendiri |

## 1. Scope

Klaster ini meneliti **hubungan manusia dan AI**: bagaimana orang berinteraksi dengan sistem AI, bagaimana sistem itu dapat dijelaskan, adil, menjaga privasi, dan bagaimana institusi (kampus, layanan publik, usaha kecil) mengelola AI secara bertanggung jawab. Di UAI, klaster ini juga menjadi rumah bagi riset tentang **etika AI dari sudut nilai Islam** yang dikerjakan secara empiris, bukan normatif semata — misalnya bagaimana konsep amanah, kejujuran, dan kemaslahatan diterjemahkan menjadi kriteria evaluasi sistem.

| Sub-area | Isi |
|---|---|
| **HCI untuk AI** | desain interaksi, user study, evaluasi manusia terhadap keluaran AI, kepercayaan (trust) yang terkalibrasi |
| **Fairness, privacy, explainability** | pengukuran bias pada data/model Indonesia, privasi by design, penjelasan yang berguna bagi pengguna non-teknis |
| **AI dalam pendidikan** | AI literacy, academic advising, integritas akademik di era GenAI, asesmen yang jujur |
| **Tata kelola & etika** | kebijakan penggunaan AI di institusi, AI usage disclosure, etika AI berbasis nilai Islam yang dapat diukur |

## 2. Research questions besar 2026–2030

1. Bagaimana **mahasiswa dan dosen Indonesia** benar-benar memakai GenAI dalam belajar dan riset, dan apa hubungannya dengan kualitas bukti yang mereka hasilkan?
2. Desain interaksi seperti apa yang membuat pengguna **mempercayai AI secukupnya** — tidak terlalu percaya, tidak menolak — pada asisten akademik dan layanan publik?
3. Bias apa yang muncul pada model/data berbahasa Indonesia terhadap kelompok tertentu (daerah, gender, status sosial), dan **metrik fairness** mana yang bermakna dalam konteks lokal?
4. Penjelasan (explanation) seperti apa yang **benar-benar membantu** dosen wali, tenaga kesehatan, atau pelaku UMKM mengambil keputusan, diukur lewat user study?
5. Bagaimana **AI literacy** dapat diukur dan ditingkatkan pada mahasiswa, dan apakah peningkatan itu mengubah perilaku verifikasi mereka?
6. Bagaimana **privasi data mahasiswa/pengguna** dijaga saat sistem AI dipakai di kampus, dan apa trade-off-nya terhadap kegunaan?
7. Bagaimana nilai-nilai Islami (amanah, kejujuran, kemaslahatan, keadilan) dapat **dioperasionalkan** menjadi kriteria evaluasi sistem AI yang dapat diuji, dan apakah kriteria itu berbeda hasilnya dari kerangka responsible AI umum?
8. Apakah protokol **AI-augmented, human-accountable science** ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)) mengubah kualitas riset mahasiswa — ini riset tentang sistem kita sendiri.

## 3. Example topics (konteks Indonesia/UAI)

1. AI-assisted academic advising untuk perguruan tinggi Indonesia: kebutuhan, desain, evaluasi bersama dosen wali (lihat [UIAI-2026-001](../../research-backlog/problems/UIAI-2026-001-ai-assisted-academic-advising.md)).
2. Survei dan studi perilaku penggunaan GenAI mahasiswa Informatika UAI dalam tugas dan riset.
3. Instrumen pengukuran AI literacy berbahasa Indonesia dan validasinya.
4. User study explainability pada sistem early warning kesulitan belajar: penjelasan mana yang dipakai dosen wali.
5. Audit fairness model prediksi (mis. kelulusan tepat waktu) terhadap kelompok asal daerah/jalur masuk — dengan data teranonimisasi.
6. Kepercayaan konsumen Muslim terhadap verifikasi halal berbantuan AI: eksperimen terkontrol.
7. Kerangka evaluasi "amanah epistemik" untuk asisten riset AI: uji apakah asisten mengarang referensi, dan bagaimana pengguna mendeteksinya.
8. Kebijakan penggunaan AI di mata kuliah: studi kasus penerapan AI Usage Statement dan dampaknya terhadap integritas.
9. Aksesibilitas antarmuka AI berbahasa Indonesia bagi pengguna disabilitas.
10. Persepsi pegawai layanan publik terhadap keputusan berbantuan AI: transparansi dan akuntabilitas.
11. Studi replikasi temuan HCI-AI dari luar negeri pada konteks Indonesia: apakah hasilnya bertahan?

## 4. Related courses

| Mata kuliah | Kontribusi ke C3 | Mode |
|---|---|---|
| Interaksi Manusia–Komputer (sem. III) | user study, evaluasi manusia | E/R |
| Etika Profesi (sem. VI) | tata kelola, integritas, etika AI | E |
| AI & Machine Learning (sem. V) | fairness, explainability sebagai evaluasi tambahan | E |
| Statistika & Statistika Terapan | desain survei/eksperimen, inferensi | F |
| Metodologi Penelitian (sem. VII) | user study, survey, case study, qualitative methods; AI protocol | Prove |
| Tugas Akhir | kontribusi empiris | Contribute |

Lintas fakultas: Psikologi (pengukuran, perilaku), Hukum (privasi, regulasi), Komunikasi (persepsi), studi Islam (etika) — sumber: dokumen diskusi; verifikasi ketersediaan mitra sebelum dokumen formal.

## 5. Kebutuhan data dan compute

| Kebutuhan | Isi |
|---|---|
| Data | data survei/wawancara/observasi yang dikumpulkan sendiri dengan **consent**; data akademik agregat/teranonimisasi (`Restricted`, lihat [DS-2026-001](../../datasets-registry/datasets/DS-2026-001-student-learning.md)); log interaksi dengan izin |
| Etika | protokol etik untuk subjek manusia wajib sebelum G5 ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)); komite etik kampus bila ada — `[isi: prosedur etik UAI]` |
| Compute | rendah; kebutuhan utama adalah instrumen, partisipan, dan analisis statistik |
| Alat | alat survei, alat analisis kualitatif, pustaka fairness/XAI open-source |

## 6. Output yang diharapkan

| Jenis output | Contoh |
|---|---|
| Paper (`PUB-*`) | user study, survei, audit fairness, studi kasus kebijakan |
| Instrumen / benchmark (`ART-*`/`DS-*`) | kuesioner AI literacy tervalidasi; suite audit bias berbahasa Indonesia |
| Research brief / kebijakan | rekomendasi kebijakan AI untuk prodi/universitas; pedoman AI usage |
| Prototype | antarmuka advising dengan penjelasan; dashboard dosen wali |
| Kontribusi ke sistem sendiri | revisi protokol AI, rubrik, kebijakan integritas ([research-os](../../research-os/README.md)) |

## 7. Entry door yang umum

**Problem** (masalah nyata dari unit kampus, dosen wali, layanan mahasiswa) dan **Faculty Research** (riset dosen tentang pembelajaran/etika). Entry door **Course Project** dari HCI dan Etika Profesi juga umum.

## 8. Keterkaitan program dan klaster lain

- Memakai temuan bias/halusinasi dari [C1](ai-models-data-knowledge.md) sebagai objek studi manusia.
- Menetapkan **syarat privasi dan keamanan** yang diimplementasikan [C2](ai-systems-security.md).
- Menjadi **gate etika** bagi seluruh aplikasi [C4](applied-ai.md): tidak ada aplikasi domain tanpa penilaian dampak manusia.
- Program: `program-responsible-ai` adalah muara klaster; `program-ai-education` berbagi topik advising dan AI literacy.

## 9. Topik yang sengaja tidak kita kejar (2026–2030)

| Tidak dikejar | Alasan (Occam) |
|---|---|
| Spekulasi filosofis tentang AGI/kesadaran mesin tanpa data empiris | tidak menghasilkan bukti yang dapat diuji; gagal G4 |
| Lobi kebijakan atau advokasi tanpa riset | bukan riset; output kebijakan harus berbasis studi |
| Studi persepsi generik "apakah orang suka AI" tanpa keputusan yang berubah | gagal G2: tidak jelas keputusan siapa yang berubah |
| Kerangka etika normatif baru tanpa operasionalisasi | kami mengukur, bukan hanya merumuskan |
| Penelitian pada subjek manusia tanpa consent/protokol etik | melanggar amanah epistemik dan [SECURITY.md](../../SECURITY.md) |

Fokus kami: **AI yang dapat dipercaya secukupnya, dijelaskan seperlunya, dan dipertanggungjawabkan sepenuhnya oleh manusia.**
