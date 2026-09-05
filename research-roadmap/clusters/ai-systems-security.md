# C2 — AI Systems, Software & Security

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) · [SECURITY.md](../../SECURITY.md)

| Field | Nilai |
|---|---|
| Kode | **C2** |
| Peran AI | **AI Enabling** — infrastruktur yang memungkinkan AI: sistem, software engineering, keamanan, data engineering |
| Label GitHub | `cluster:systems` |
| Tim GitHub | `@ai-systems` |
| Program terkait | pendukung semua program; paling dekat dengan `program-ai-halal` (traceability) dan `program-responsible-ai` (keamanan & privasi) |
| Kompetensi prodi yang ditumpangi | Software Engineering, IoT (sumber: dokumen diskusi; verifikasi sebelum dokumen formal) |

## 1. Scope

Klaster ini meneliti **bagaimana sistem AI dibangun, diuji, diamankan, dan dioperasikan** sehingga dapat diandalkan di lingkungan nyata dengan sumber daya terbatas. Ini adalah klaster "rekayasa": *software engineering for AI*, *AI for software engineering*, *MLOps*, *keamanan sistem berbasis LLM*, dan *sistem tertanam/IoT* yang memakai model. Klaster ini menjadikan riset klaster lain **dapat dijalankan orang lain** — reproducibility adalah bagian dari scope, bukan tambahan.

| Sub-area | Isi |
|---|---|
| **Systems & MLOps** | pipeline data-model-deploy, monitoring, drift, biaya, model kecil di edge/on-premise |
| **Software engineering for AI / AI for SE** | pengujian sistem ML, kualitas kode berbantuan AI, dokumentasi, reproducibility tooling |
| **Security & reliability** | keamanan aplikasi LLM (prompt injection, kebocoran data), robustness, privasi by design, audit trail |
| **IoT & data engineering** | sensor untuk pangan/lingkungan, pengumpulan data berkualitas, integrasi dengan model |

## 2. Research questions besar 2026–2030

1. Bagaimana **menguji** sistem berbasis ML/LLM secara sistematis (test oracle, metamorphic testing, evaluasi regresi) pada aplikasi kampus dan UMKM?
2. Praktik MLOps minimum apa yang **cukup** bagi organisasi kecil (prodi, UMKM, unit layanan publik) — apa yang benar-benar meningkatkan keandalan?
3. Seberapa rentan aplikasi LLM berbahasa Indonesia (chatbot layanan, RAG kampus) terhadap **prompt injection dan kebocoran data**, dan mitigasi apa yang efektif?
4. Bagaimana **reproducibility** riset ML mahasiswa dapat dijamin secara teknis (environment, seed, konfigurasi) dengan biaya usaha yang rendah?
5. Apakah kode yang dihasilkan/dibantu AI dalam proyek mahasiswa **lebih baik atau lebih buruk** kualitasnya, dan bagaimana mengukurnya secara adil?
6. Arsitektur seperti apa yang memungkinkan **traceability dan audit** (mis. rantai pasok halal, keputusan otomatis layanan publik) tanpa membocorkan data partner?
7. Bagaimana merancang pengumpulan data berbasis **IoT berbiaya rendah** yang menghasilkan data layak riset (kualitas, metadata, privasi)?
8. Model kecil apa yang dapat berjalan **on-premise/edge** dengan kinerja yang cukup untuk kebutuhan domain UAI?

## 3. Example topics (konteks Indonesia/UAI)

1. Pengujian metamorphic untuk chatbot layanan akademik berbahasa Indonesia.
2. Benchmark prompt injection untuk asisten RAG dokumen kampus; evaluasi guardrail.
3. Template reproducibility (environment, seed, `run.sh`) untuk riset Metopen — studi apakah peer dapat mereproduksi hasil ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)).
4. MLOps minimum untuk UMKM: monitoring drift model prediksi permintaan dengan alat gratis.
5. Studi empiris kualitas kode berbantuan AI pada Proyek Perangkat Lunak (mode E).
6. Sistem traceability halal berbasis audit trail: desain, evaluasi keandalan, biaya.
7. Pipeline pengumpulan data sensor rantai dingin pangan dan validasi kualitas data.
8. Deployment model klasifikasi citra halal di perangkat mobile berbiaya rendah: trade-off akurasi–latensi.
9. Privacy-preserving analytics untuk data akademik (agregasi, pseudonimisasi) sebagai infrastruktur riset [C3 × Education](../domains/education.md).
10. Keandalan sistem skrining kesehatan berbasis AI: failure mode, fallback, logging.
11. Studi kasus adopsi praktik SE (versioning data, CI) pada riset mahasiswa: apa yang benar-benar dipakai.

## 4. Related courses

| Mata kuliah | Kontribusi ke C2 | Mode |
|---|---|---|
| Rekayasa Perangkat Lunak (sem. IV) | proses, kualitas, dokumentasi | E/R |
| Pengujian Perangkat Lunak (sem. V) | pengujian sistem ML, test oracle | R |
| Proyek Perangkat Lunak (sem. VI) | sistem end-to-end sebagai research asset | R |
| Basis Data (sem. III) | data engineering, skema | F |
| Struktur Data & Analisis Algoritma (sem. III–IV) | efisiensi, kompleksitas | F |
| AI & Machine Learning (sem. V) | model yang di-deploy | E |
| Kerja Praktik (sem. VI) | masalah sistem nyata dari industri | E (problem discovery; entry door Problem/Partner) |
| Metodologi Penelitian / TA | empirical SE study, benchmarking | R (Prove / Contribute) |

Detail: [research-based-learning/courses/software-engineering](../../research-based-learning/courses/software-engineering/README.md).

## 5. Kebutuhan data dan compute

| Kebutuhan | Isi |
|---|---|
| Data | log sistem (dianonimkan), repositori kode mahasiswa (dengan izin), dataset serangan/prompt (dibuat sendiri), data sensor IoT |
| Compute | server on-premise kecil untuk deployment eksperimen; perangkat edge (single-board computer, ponsel); CI gratis GitHub Actions |
| Alat | container, workflow CI, alat pengujian, alat monitoring open-source; semua terdokumentasi di [AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) |
| Keamanan | eksperimen serangan hanya pada sistem milik sendiri/sandbox; tidak pernah pada sistem produksi tanpa izin tertulis |

## 6. Output yang diharapkan

| Jenis output | Contoh |
|---|---|
| Software / tooling (`ART-*`) | template repo reproducible; harness pengujian LLM; pipeline MLOps ringan |
| Benchmark (`DS-*`/`ART-*`) | suite prompt injection berbahasa Indonesia; dataset log terdokumentasi |
| Paper (`PUB-*`) | empirical SE study, studi kasus, benchmarking sistem |
| Prototype / HKI | sistem traceability; aplikasi edge |
| Research brief | panduan praktik minimum untuk unit kampus/UMKM |

## 7. Entry door yang umum

**Course Project** (Proyek Perangkat Lunak, Pengujian PL) dan **Partner** (masalah sistem dari industri/Kerja Praktik). **Competition** relevan untuk lomba software/IoT — hasil lomba masuk pipeline yang sama dan diuji dengan gate yang sama.

## 8. Keterkaitan program dan klaster lain

- Menyediakan **infrastruktur reproducibility** untuk semua klaster; wajib dipakai sejak G6.
- Menguji **keamanan dan privasi** sistem yang dirancang [C3](responsible-human-ai.md).
- Men-deploy **model** dari [C1](ai-models-data-knowledge.md) untuk aplikasi [C4](applied-ai.md).
- Program: pendukung teknis `program-ai-halal` (traceability) dan `program-responsible-ai` (privasi, keamanan); belum ada program C2 tersendiri sampai 2030.

## 9. Topik yang sengaja tidak kita kejar (2026–2030)

| Tidak dikejar | Alasan (Occam) |
|---|---|
| Desain akselerator hardware/kompiler ML tingkat rendah | di luar kapabilitas dan fasilitas prodi |
| Kriptografi primitif baru | bukan adjacency kepakaran yang ada; pakai pustaka standar |
| Sistem terdistribusi skala data center | tidak ada infrastruktur; masalah UAI berskala kecil–menengah |
| Penetration testing sistem pihak ketiga tanpa izin | melanggar etika dan hukum; hanya sandbox milik sendiri |
| "Membuat aplikasi" tanpa klaim pengetahuan | itu proyek, bukan riset; gagal G1 |

Fokus kami: **sistem AI yang dapat diuji, diamankan, dan dijalankan ulang — pada skala yang benar-benar ada di Indonesia.**
