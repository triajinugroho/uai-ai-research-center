# Research Demand–Supply Marketplace — AI Research Center sebagai Matching Engine

> **ID** AIR-05 · **Paket** 03 AI Research Ecosystem · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kepala pusat riset, `@maintainers`, research lead klaster, admin riset, mitra industri/pemerintah/masyarakat, unit kerja sama, dosen pengampu MK mode R
> **Terkait** [AIR-01 AI Research Center Concept](01-ai-research-center-concept.md) · [AIR-02 AI Research Clusters](02-ai-research-clusters.md) · [AIR-03 Faculty Research Alignment](03-faculty-research-alignment.md) · [AIR-04 Cross-Faculty AI Model](04-cross-faculty-ai-model.md) · [ARC-04 Build–Prove–Contribute](../02-academic-architecture/04-build-prove-contribute.md) · [TPL-04 Research Backlog](../08-templates/04-research-backlog-template.md) · [TPL-02 Research Mission Tracker](../08-templates/02-research-mission-tracker-template.md) · [Research Backlog](../../research-backlog/README.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

## 1. Ide dasar

Ada dua sisi yang selama ini tidak pernah bertemu secara sistematis. Di satu sisi ada **permintaan**: industri dengan masalah yang tidak sempat dipecahkan, pemerintah dengan data yang tidak sempat dianalisis, unit-unit UAI dengan pertanyaan yang tidak sempat dijawab, masyarakat dengan kebutuhan yang tidak sempat didengar, dan prioritas nasional yang membutuhkan riset lokal. Di sisi lain ada **pasokan**: dosen dengan kepakaran, mahasiswa yang setiap semester harus mengerjakan proyek dan TA, mata kuliah yang membutuhkan kasus nyata, laboratorium, dataset, dan alat.

Tanpa mekanisme pencocokan, kedua sisi saling mengarang: mahasiswa mengarang masalah untuk TA, mitra mengarang solusi tanpa bukti. **AI Research Center adalah matching engine** — ia menerima permintaan, mengklasifikasikannya, mencocokkannya dengan pasokan, memberinya Research ID, dan mendorongnya ke pipeline gate. Marketplace ini bukan platform baru; ia adalah **cara memakai research backlog, Mission Control, dan registry** yang sudah ada.

## 2. Sisi permintaan (demand)

| Sumber permintaan | Bentuk permintaan | Contoh | Pintu masuk | Yang dibutuhkan dari mereka |
|---|---|---|---|---|
| **Industry** | Masalah operasional/produk yang butuh bukti, bukan hanya prototipe; data yang belum dianalisis | Verifikasi informasi produk, prediksi permintaan UMKM, pengujian sistem berbasis LLM | Issue *Research Problem* (entry door *Partner*), KP | Problem owner, akses data dengan perjanjian, waktu untuk evaluasi |
| **Government** | Analisis data layanan publik, kebijakan berbasis bukti, alat bantu regulasi | Analisis aduan layanan, asisten regulasi | Issue, undangan pusat riset, MoU | Data publik/anonim, validator domain |
| **UAI (unit internal)** | Pertanyaan institusional: akademik, layanan mahasiswa, halal, perpustakaan, TI | Deteksi dini mahasiswa berisiko, chatbot layanan, analitik pembelajaran | Issue (entry door *Problem*), permintaan pimpinan | Data institusi dengan tata kelola, keputusan yang akan berubah |
| **Society** | Kebutuhan komunitas, lembaga sosial, sekolah, masjid, UMKM binaan | Pemetaan kebutuhan komunitas, literasi AI, alat verifikasi konten | Issue via dosen pengabdian, KP | Akses lapangan, partisipan, evaluasi manfaat |
| **National priorities** | Arah riset nasional dan Renstra UAI: kedaulatan data/bahasa, halal, kesehatan, pendidikan, ekonomi digital | Benchmark NLP Bahasa Indonesia, ontologi halal | Roadmap ([research-roadmap/alignment/indonesia.md](../../research-roadmap/alignment/indonesia.md)) | Diterjemahkan menjadi masalah konkret oleh research lead |

Permintaan yang **tidak** diterima: pesanan pengembangan software tanpa pertanyaan pengetahuan (diarahkan ke KP/Proyek PL biasa), permintaan data pribadi tanpa dasar, dan masalah yang solusinya sudah ditetapkan ("buatkan model X").

## 3. Sisi pasokan (supply)

| Sumber pasokan | Kapasitas | Batasan | Registry |
|---|---|---|---|
| **Dosen** | Kepakaran, mentor, reviewer, owner riset, penulis proposal hibah | Waktu; adjacency ke AI berbeda-beda | Faculty Research Map ([AIR-03](03-faculty-research-alignment.md), [TPL-07](../08-templates/07-faculty-research-map-template.md)) |
| **Mahasiswa** | Tim proyek MK (sem. III–VI), Metopen (sem. VII), TA (sem. VIII); tenaga riset untuk skema internal | Satu semester per tahap; kompetensi sesuai spiral ([ARC-01](../02-academic-architecture/01-research-capability-spiral.md)) | Mission Control (Researcher), Student Guide |
| **Courses** | Menu proyek untuk MK mode R/E: AI/ML, Data Mining, Proyek PL, RPL, HCI, NLP; Metopen; TA | Mengikuti kalender akademik; ukuran masalah harus muat satu semester | [ARC-02](../02-academic-architecture/02-curriculum-research-map.md), `research-based-learning/courses/` |
| **Labs / compute** | Laboratorium Prodi, server, cloud credit, GPU bersama | Kuota; prioritas berdasarkan gate | Inventaris compute (`[isi]`), [AIR-01 §2.5](01-ai-research-center-concept.md) |
| **Datasets** | Dataset terdaftar: pembelajaran, halal, NLP Indonesia, sensor, dll. | Privasi, lisensi, akses | [datasets-registry](../../datasets-registry/README.md) |
| **Tools** | Research OS: template, gate, protokol AI, katalog alat AI | Butuh pelatihan awal | [research-os](../README.md), [AIX-05](../05-ai-augmented-research/05-ai-tools-reference.md) |

## 4. Tabel demand × supply

Sel menunjukkan bentuk pencocokan yang paling lazim; ● = pencocokan utama, ○ = pendukung.

| Demand ↓ / Supply → | Dosen | Mahasiswa | Courses | Labs/compute | Datasets | Tools |
|---|---|---|---|---|---|---|
| **Industry** | ● mentor + owner; proposal bersama | ● TA, Metopen, KP | ○ Proyek PL, AI/ML sebagai pilot | ○ | ○ data mitra (restricted) | ○ |
| **Government** | ● owner + validator domain (lintas fakultas) | ● TA, Metopen | ○ Data Mining, NLP | ○ | ● data publik/anonim → registry | ○ |
| **UAI internal** | ● owner; unit sebagai problem owner | ● proyek MK → Metopen → TA | ● AI/ML, HCI, Proyek PL | ● compute institusi | ● data institusi (restricted) | ● |
| **Society** | ● dosen pengabdian + mentor | ● KP, Proyek PL, TA | ○ Proyek PL, Etika Profesi | ○ | ○ data survei/komunitas | ○ |
| **National priorities** | ● research lead menerjemahkan; owner | ● Metopen, TA, NLP | ● NLP, AI/ML | ● | ● benchmark/korpus → registry | ● |

Cara membaca: masalah industri paling sering dicocokkan dengan dosen sebagai mentor/owner dan mahasiswa TA/Metopen; masalah internal UAI adalah yang paling mudah dicocokkan ke semua sisi pasokan karena data dan stakeholder ada di dalam.

## 5. Proses matching

```
 1 INTAKE ──► 2 KLASIFIKASI ──► 3 PENCOCOKAN ──► 4 RESEARCH ID ──► 5 PIPELINE ──► 6 KEMBALI KE MARKETPLACE
 Issue           klaster/domain      dosen/MK/           G2 Problem         G3–G8             output, brief,
 type:problem    maturity/prioritas  mahasiswa/data      Ready              gate              backlog baru
```

**Langkah 1 — Intake.** Permintaan masuk sebagai Issue *Research Problem* (form `.github/ISSUE_TEMPLATE/`), langsung oleh pengusul atau dibantu admin riset. Field wajib: masalah, stakeholder/problem owner, domain, data yang mungkin, output yang diharapkan, batas waktu jika ada. Label awal: `type:problem`, `maturity:idea`.

**Langkah 2 — Klasifikasi (triase mingguan `@maintainers` + research lead).** Tetapkan klaster primer/sekunder ([AIR-02 §8](02-ai-research-clusters.md)), domain, prioritas P0–P3, dan kelayakan: apakah ada pertanyaan pengetahuan (bukan pesanan software), apakah data realistis, apakah ukurannya muat pipeline (satu semester Metopen + satu semester TA, atau proyek MK). Masalah yang belum layak diberi komentar apa yang kurang dan tetap di backlog sebagai *Idea*.

**Langkah 3 — Pencocokan.** Research lead klaster mencocokkan masalah dengan: (a) dosen dari Faculty Research Map yang *Possible Research*-nya berdekatan → calon mentor/owner; (b) MK mode R/E yang semester berikutnya bisa memakainya sebagai menu proyek → field *Course*; (c) mahasiswa Metopen/TA yang mencari topik → lewat menu masalah W1–W2; (d) dataset di registry yang relevan; (e) fakultas mitra bila lintas disiplin ([AIR-04](04-cross-faculty-ai-model.md)). Hasil: Issue diperbarui dengan *Faculty Mentor*, *Course*, *Entry Door*, dan ditandai `status:ready`.

**Langkah 4 — Research ID.** Ketika tim terbentuk dan lolos **G2 Problem Ready**, `@maintainers` memberi `UIAI-YYYY-NNN`; Issue, repositori, dan Mission Control diperbarui. Sebelum itu dipakai ID sementara sesuai konvensi [CONTRIBUTING.md §2](../../CONTRIBUTING.md).

**Langkah 5 — Pipeline.** Riset berjalan lewat G3–G8 ([OPS-03](../06-execution-os/03-research-gates.md)); pusat riset memantau lewat Mission Control, menyediakan compute/data/reviewer, dan menjaga komunikasi dengan problem owner (minimal di G5 dan G8).

**Langkah 6 — Kembali ke marketplace.** Output terdaftar ([ARC-06](../02-academic-architecture/06-research-output-taxonomy.md)); problem owner menerima research brief; *next steps* dari handoff menjadi Issue baru; masalah yang selesai ditutup dengan tautan ke output. Loop tertutup.

## 6. Artefak marketplace

| Artefak | Fungsi dalam marketplace | Lokasi | Template |
|---|---|---|---|
| **Research Backlog** | Katalog permintaan (problem bank): apa yang bisa diteliti, statusnya, siapa problem owner | GitHub Issues + indeks `research-backlog/BACKLOG.md` | [TPL-04](../08-templates/04-research-backlog-template.md) |
| **Research Mission Control** | Papan pencocokan dan pemantauan: field Cluster, Domain, Researcher, Faculty Mentor, Entry Door, Course, Gate, Maturity, Priority, Next Evidence; view Pipeline, By Cluster, By Course, Publication, Faculty Portfolio | GitHub Projects | [TPL-02](../08-templates/02-research-mission-tracker-template.md) |
| **Faculty Research Map** | Katalog pasokan dosen | `research-based-learning/faculty-guide/` (internal) | [TPL-07](../08-templates/07-faculty-research-map-template.md) |
| **Datasets Registry** | Katalog pasokan data | `datasets-registry/REGISTRY.md` | [TPL-05](../08-templates/05-dataset-registry-template.md) |
| **Publications Registry** | Katalog output yang kembali ke marketplace | `publications/PUBLICATIONS.md` | [publications/_template](../../publications/_template/publication-card.md) |
| **Research Leaderboard** | Kematangan riset (bukan orang) untuk melihat pasokan yang siap dipindahkan ke tahap berikut | Dari Mission Control | [TPL-03](../08-templates/03-research-leaderboard-template.md) |
| **Research Brief** | Pengembalian nilai ke sisi permintaan | Repositori riset `docs/` | [ARC-06 §3.11](../02-academic-architecture/06-research-output-taxonomy.md) |

## 7. SLA sederhana

Angka di bawah adalah komitmen layanan awal (Phase 2–4); disesuaikan setelah volume diketahui.

| Layanan | Komitmen | Penanggung jawab |
|---|---|---|
| Konfirmasi penerimaan Issue permintaan | ≤ 5 hari kerja | Admin riset / `@maintainers` |
| Klasifikasi & keputusan kelayakan | ≤ 2 minggu (triase mingguan) | `@maintainers` + research lead |
| Pencocokan ke calon mentor/MK | ≤ 4 minggu setelah layak; atau dijadwalkan ke semester berikutnya dengan tanggal jelas | Research lead klaster |
| Kabar ke problem owner | Saat diterima, saat dicocokkan, saat G2, G5, G8; minimal satu kali per semester bila menunggu | Mentor / admin riset |
| Research brief untuk problem owner | ≤ 4 minggu setelah G8 (Metopen) atau sidang TA | Tim riset + mentor |
| Permintaan yang tidak dapat dicocokkan | Diberi tahu dalam ≤ 1 semester beserta alasannya; tetap di backlog bila layak | Research lead |
| Data mitra | Kartu dataset dibuat ≤ 2 minggu setelah perjanjian; data mentah tidak pernah ke GitHub | Pengelola registry |

## 8. Aturan prioritas

1. **P0** — masalah yang memblokir riset lain atau permintaan pimpinan dengan tenggat institusional.
2. **P1** — ada problem owner aktif + data realistis + selaras roadmap/Renstra + ada calon mentor.
3. **P2** — layak tetapi belum ada salah satu dari: data, mentor, atau mahasiswa.
4. **P3** — ide yang perlu dimatangkan.

Di antara prioritas sama, dahulukan masalah yang: memakai dataset yang sudah terdaftar (*reuse before create*), lintas fakultas dengan komponen lengkap ([AIR-04 §2](04-cross-faculty-ai-model.md)), atau melanjutkan riset yang sudah punya handoff.

## 9. Contoh alur: satu masalah industri hingga TA dan paper

**Permintaan.** Sebuah UMKM pangan binaan (lewat unit kerja sama UAI) mengeluh: pra-audit halal memakan waktu karena harus memeriksa satu per satu bahan pada label produk pemasok. Mereka bertanya, "Bisakah AI membantu?"

**Intake (bulan 1).** Admin riset membantu membuat Issue *Research Problem*: "Pemeriksaan awal status bahan pada label produk pemasok untuk pra-audit halal UMKM". Domain Halal; stakeholder: pemilik UMKM dan auditor internal; data yang mungkin: foto label produk, daftar bahan kritis (publik), katalog produk (contoh registry: *halal products*); output diharapkan: alat bantu + bukti seberapa bisa dipercaya. Entry door *Partner*; `maturity:idea`.

**Klasifikasi (triase minggu berikutnya).** Ada pertanyaan pengetahuan ("seberapa akurat dan di mana gagalnya ekstraksi bahan dari label lokal, dan apakah membantu auditor?"), bukan sekadar pesanan software. Klaster primer C4 (Applied/Halal), sekunder C1 (ekstraksi informasi, penalaran bahan). Prioritas P1: problem owner aktif, data realistis, selaras domain roadmap.

**Pencocokan (bulan 2).** Research lead C4 mencocokkan: dosen Informatika dengan *Possible Research* "ekstraksi informasi dari dokumen Bahasa Indonesia" sebagai mentor; dosen Teknologi Pangan sebagai validator domain (model lima komponen); MK **AI & Machine Learning** semester V sebagai Build — masalah masuk menu proyek; dataset kandidat `DS-2026-002` (katalog produk halal) tersedia di registry. Nota kesepakatan satu halaman disahkan; data foto label diklasifikasikan *Restricted* (dapat memuat identitas pemasok), disimpan di server institusi.

**Build (semester V).** Tim AI/ML membuat Experiment Card: tugas ekstraksi daftar bahan dari foto label; baseline OCR + pencocokan kata kunci; metrik presisi/recall per bahan kritis; split per pemasok untuk mencegah leakage. Hasil: baseline sudah cukup baik untuk bahan umum, gagal pada bahan turunan dan label rusak. Handoff #1 terisi.

**Prove (semester VII, Metopen).** Satu mahasiswa melanjutkan; G2 Problem Ready → **`UIAI-2026-021`**. Evidence map 20 sumber tentang ekstraksi informasi label dan sistem verifikasi halal; gap: hampir tidak ada evaluasi pada label produk lokal dan pada bahan turunan. RQ: "Seberapa akurat pipeline ekstraksi+penalaran bahan pada label produk UMKM Indonesia dibanding pemeriksaan manual, dan pada kelas bahan apa ia gagal?" G5 dengan reviewer C4 dan C1; validasi domain oleh dosen Teknologi Pangan; pilot pada 200 label; G8 dengan Research Pack dan proposal TA.

**Contribute (semester VIII, TA).** Eksperimen penuh, studi kecil dengan dua auditor internal UMKM (apakah waktu pra-audit berkurang, kesalahan apa yang tetap lolos). Output: laporan TA; prototype `ART-2027-004` (kode Apache-2.0; data restricted); manuscript `PUB-2027-006` untuk seminar/jurnal bidang sistem informasi/halal dengan penulis mahasiswa, mentor Informatika, dosen Teknologi Pangan; research brief untuk UMKM dan unit kerja sama.

**Kembali ke marketplace.** Brief diserahkan ≤ 4 minggu setelah sidang. Handoff #3: next steps — ontologi bahan turunan, uji pada UMKM lain; dua Issue baru dibuka (`type:research-question`, `type:dataset`) dan menjadi menu proyek angkatan berikutnya; riset lanjutan diusulkan ke skema penelitian internal dengan dua mahasiswa baru. Research ID `UIAI-2026-021` tetap menjadi jangkar semua tautan.

Durasi total dari intake ke paper: sekitar 2–2,5 tahun kalender, tetapi problem owner mendapat nilai lebih awal: hasil Build (semester V) sudah memberi tahu bahan mana yang bisa dipercaya sistem.

## 10. Metrik marketplace

| Metrik | Mengukur | Sumber |
|---|---|---|
| Jumlah permintaan masuk per sumber (industry/government/UAI/society/national) | Kesehatan sisi permintaan | Issues `type:problem` |
| % permintaan diklasifikasi dalam SLA | Responsivitas | Tanggal Issue |
| % permintaan yang dicocokkan (mendapat mentor/MK) dalam 1 semester | Kapasitas pencocokan | Field Mission Control |
| % masalah yang mencapai G2 (Research ID) | Kualitas intake | Label gate |
| % riset yang memakai dataset terdaftar | *Reuse before create* | Field dataset |
| Jumlah research brief dikembalikan ke problem owner | Nilai balik ke permintaan | `docs/` repositori |
| Jumlah Issue baru yang lahir dari handoff #3 | Compounding loop | Issue tertaut |
| Kepuasan problem owner (survei singkat di G8) | Kualitas hubungan | Survei |

Metrik ini masuk ke [GOV-03](../07-governance/03-kpi-and-measurement.md) sebagai bagian KPI pusat riset.

## 11. Ringkasan

- Demand: industry, government, UAI, society, national priorities. Supply: dosen, mahasiswa, courses, labs/compute, datasets, tools.
- Pusat riset mencocokkan keduanya lewat enam langkah: intake → klasifikasi → pencocokan → Research ID → pipeline → kembali ke marketplace.
- Artefaknya sudah ada: Research Backlog, Mission Control, Faculty Research Map, registry dataset dan publikasi, research brief.
- SLA sederhana menjaga kepercayaan sisi permintaan; aturan prioritas menjaga kapasitas sisi pasokan.
- Satu masalah industri dapat menjadi proyek AI/ML, Research Pack, TA, prototype, paper, dan dua masalah baru — dengan satu Research ID.
