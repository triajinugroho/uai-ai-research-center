# AI Research Center Concept — Hub, Bukan Satu Lab

> **ID** AIR-01 · **Paket** 03 AI Research Ecosystem · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Rektorat, Dekan, Kaprodi, calon kepala pusat riset, tim PP-PTS, mitra industri/pemerintah, reviewer hibah
> **Terkait** [MST-01 Executive Summary](../00-master/01-executive-summary.md) · [STR-02 Vision & Endgame](../01-strategic-foundation/02-vision-and-endgame.md) · [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) · [AIR-02 AI Research Clusters](02-ai-research-clusters.md) · [AIR-05 Demand–Supply Marketplace](05-research-demand-supply-marketplace.md) · [ARC-04 Build–Prove–Contribute](../02-academic-architecture/04-build-prove-contribute.md) · [GOV-01 Governance Model](../07-governance/01-governance-model.md) · [GOV-02 Implementation Roadmap](../07-governance/02-implementation-roadmap.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

## 1. Posisi: hub yang menghubungkan, bukan lab yang memiliki

UAI AI Research Center **bukan** satu laboratorium dengan beberapa dosen dan komputer. Ia adalah **hub** — *institutional engine* — yang menghubungkan hal-hal yang sudah ada tetapi terfragmentasi: dosen dengan kepakaran masing-masing, mata kuliah yang menghasilkan proyek, mahasiswa yang mencari topik TA, dataset yang tersebar di laptop, masalah nyata dari industri dan masyarakat, roadmap penelitian universitas, dan venue publikasi.

Formula yang mendasari seluruh sistem ([research-os/README](../README.md)):

> UAI Informatics membangun scientific thinkers melalui kurikulum yang menghasilkan reusable research assets; AI menjadi leading thematic umbrella sekaligus cognitive accelerator; Metodologi Penelitian menjadi evidence-quality gate; Tugas Akhir menjadi contribution stage; dan **AI Research Center menjadi institutional engine yang menghubungkan seluruh siklus tersebut dengan dosen, roadmap UAI, problem industri/nasional, serta publikasi.**

Nama internal siklusnya: **UIRP — UAI Informatics Research Pipeline**:

```
Research Center → Dosen → Mata Kuliah → Mahasiswa → Problem → Dataset → Project
      ▲                                                                    │
      │                                                                    ▼
Publikasi / HKI / Produk ◄── Paper ◄── TA ◄── Metopen ◄────────────────────┘
```

Misi riset: *responsible, human-centered, impact-driven AI* — riset yang menghasilkan *credible knowledge* dan artefak yang dapat direproduksi, bermanfaat bagi Indonesia, dan dipertanggungjawabkan secara ilmiah, etis, dan profesional. Signature: **amanah epistemik**.

Mengapa hub, bukan lab:

| Lab tunggal | Hub |
|---|---|
| Riset milik beberapa dosen | Riset milik sistem; dosen mana pun dapat masuk lewat adjacency kepakarannya ([AIR-03](03-faculty-research-alignment.md)) |
| Mahasiswa yang "beruntung" masuk lab | Semua mahasiswa masuk pipeline lewat MK dan Metopen ([ARC-04](../02-academic-architecture/04-build-prove-contribute.md)) |
| Dataset dan kode di laptop anggota lab | Registry, repositori standar, Research ID |
| Berhenti ketika kepala lab pindah | Organisasi berdasarkan sistem, bukan orang (§7) |
| Output: paper anggota lab | Output: paper, dataset, software, model, HKI, prototype, brief ([ARC-06](../02-academic-architecture/06-research-output-taxonomy.md)) |

## 2. Sembilan fungsi hub

Setiap fungsi dijabarkan dalam empat hal: **layanan** (apa yang disediakan), **mekanisme** (bagaimana dijalankan, memakai instrumen yang sudah ada di repo), **output**, dan **KPI** indikatif (angka target ditetapkan di [GOV-03](../07-governance/03-kpi-and-measurement.md)).

### 2.1 Research agenda

| | |
|---|---|
| **Layanan** | Menetapkan *what should we research*: 4 klaster, 7 domain, alignment UAI/Indonesia/global 2026–2030 |
| **Mekanisme** | [research-roadmap](../../research-roadmap/README.md) direview tahunan oleh research lead klaster; setiap masalah backlog wajib menunjuk klaster dan domain; Renstra Penelitian UAI menjadi acuan alignment |
| **Output** | Roadmap 2026–2030, dokumen klaster dan domain, daftar prioritas tahunan |
| **KPI** | % riset aktif yang selaras klaster/domain roadmap; roadmap direview ≥ 1×/tahun |

### 2.2 Faculty collaboration

| | |
|---|---|
| **Layanan** | Memetakan kepakaran dosen ke klaster; membentuk tim lintas dosen dan lintas fakultas; menyediakan mentor untuk riset mahasiswa |
| **Mekanisme** | Faculty Research Map ([AIR-03](03-faculty-research-alignment.md), [TPL-07](../08-templates/07-faculty-research-map-template.md)); tim GitHub per klaster (`@ai-models`, `@ai-systems`, `@responsible-ai`, `@applied-ai`); Faculty Portfolio di Mission Control; model lintas fakultas ([AIR-04](04-cross-faculty-ai-model.md)) |
| **Output** | Peta dosen ↔ klaster ↔ backlog; daftar mentor per klaster; tim riset lintas fakultas |
| **KPI** | % dosen terpetakan; % dosen yang menjadi mentor/reviewer ≥ 1 riset per tahun; jumlah riset lintas fakultas |

### 2.3 Student pipeline

| | |
|---|---|
| **Layanan** | Memastikan setiap mahasiswa masuk pipeline riset lewat MK (Build), Metopen (Prove), dan TA (Contribute), dengan handoff yang tercatat |
| **Mekanisme** | Capability Spiral ([ARC-01](../02-academic-architecture/01-research-capability-spiral.md)); mode F/E/R ([ARC-03](../02-academic-architecture/03-ai-contribution-modes.md)); Metopen 16 minggu dengan 8 gate; handoff [TPL-14](../08-templates/14-research-handoff-template.md); Student Guide |
| **Output** | Research asset MK, Research Pack, TA dengan output, mahasiswa peneliti untuk skema penelitian dosen |
| **KPI** | % mahasiswa Metopen TA Ready; % Research Ready; % TA dimulai dari Research Pack; jumlah mahasiswa dalam riset dosen |

### 2.4 Datasets

| | |
|---|---|
| **Layanan** | Katalog dataset yang dapat diteliti (metadata, akses, lisensi, privasi); tata kelola data; fasilitasi akses ke data institusi dan mitra |
| **Mekanisme** | [datasets-registry](../../datasets-registry/README.md) dengan kartu dataset ([TPL-05](../08-templates/05-dataset-registry-template.md)); Issue `type:dataset`; review data governance sebelum lisensi; data fisik di server/HF/Kaggle/Drive, tidak di GitHub ([SECURITY.md](../../SECURITY.md)) |
| **Output** | Registry `DS-YYYY-NNN`; dataset rilis; perjanjian akses data mitra |
| **KPI** | Jumlah dataset terdaftar; jumlah dataset yang dipakai ≥ 2 riset; 0 insiden data sensitif di repositori |

### 2.5 Compute

| | |
|---|---|
| **Layanan** | Akses komputasi untuk eksperimen (server institusi, cloud credit, GPU bersama) dan panduan efisiensi eksperimen |
| **Mekanisme** | Inventaris compute (`[isi]`); alokasi berdasarkan gate (riset yang lolos G5 berhak antre compute untuk G6); panduan eksperimen kecil dulu (pilot) sebelum skala penuh; pencatatan penggunaan di Experiment Card |
| **Output** | Kuota compute per riset; jadwal; catatan penggunaan |
| **KPI** | % riset G6 yang mendapat compute tepat waktu; utilisasi; biaya per eksperimen |

Compute adalah fungsi yang paling bergantung pada sumber daya universitas; pusat riset bertindak sebagai pengelola akses dan prioritas, bukan pemilik tunggal perangkat.

### 2.6 Industry problem

| | |
|---|---|
| **Layanan** | Pintu masuk masalah nyata dari industri, pemerintah, masyarakat, dan unit internal UAI; pencocokan ke klaster/dosen/MK |
| **Mekanisme** | Issue **Research Problem** (`type:problem`); intake dan klasifikasi ([AIR-05](05-research-demand-supply-marketplace.md)); MoU ringan; Kerja Praktik sebagai sumber Problem Brief; entry door *Partner* |
| **Output** | Research backlog terisi masalah nyata; riset dengan problem owner eksternal; brief untuk mitra |
| **KPI** | Jumlah masalah eksternal masuk backlog; % yang menjadi riset (Research ID); kepuasan mitra terhadap brief |

### 2.7 Publication

| | |
|---|---|
| **Layanan** | Backward design dari venue; venue registry yang menyaring predator; peer review internal; registry publikasi |
| **Mekanisme** | [MET-05](../04-metopen-research-studio/05-publication-backward-design.md); [TPL-06](../08-templates/06-publication-venue-registry-template.md); [TPL-12](../08-templates/12-peer-review-template.md); [publications](../../publications/README.md) dengan kartu `PUB-YYYY-NNN`; Publication Pipeline view di Mission Control |
| **Output** | Manuscript, paper, dataset/artefak rilis; registry publikasi |
| **KPI** | Jumlah submission, acceptance, publikasi (semua jenis output ARC-06); 0 publikasi di venue bermasalah |

### 2.8 Research grants

| | |
|---|---|
| **Layanan** | Mengemas riset yang sudah lolos gate menjadi proposal hibah internal/eksternal; memenuhi persyaratan keterlibatan mahasiswa |
| **Mekanisme** | Faculty Portfolio sebagai bahan proposal; riset yang lolos G5–G8 menjadi *preliminary result*; skema penelitian internal UAI yang mensyaratkan minimal dua mahasiswa aktif dipenuhi dari pipeline Metopen/TA[^1]; alignment Renstra |
| **Output** | Proposal hibah dengan bukti awal; riset mahasiswa terdanai |
| **KPI** | Jumlah proposal yang memakai riset pipeline; jumlah hibah diperoleh; jumlah mahasiswa terdanai |

### 2.9 Dissemination

| | |
|---|---|
| **Layanan** | Menyebarkan hasil ke akademik, mitra, dan publik: research day, poster, brief, portal GitHub publik, website |
| **Mekanisme** | Organization profile README sebagai dashboard publik; Research Day Prodi (poster dan defense terbaik); research brief ke mitra; Phase 5 Public Research Portal ([GOV-02](../07-governance/02-implementation-roadmap.md)) |
| **Output** | Portofolio publik, poster, brief, berita riset |
| **KPI** | Jumlah brief/poster; kunjungan portal; riset yang dikutip/diadopsi mitra |

## 3. Endgame: GitHub sebagai institutional research memory

Bayangkan seseorang — asesor, calon mitra, dosen baru, mahasiswa semester V — membuka GitHub Organization UAI AI Research Center beberapa tahun dari sekarang. Tanpa bertanya kepada siapa pun, ia dapat menjawab:

1. Apa masalah strategis yang sedang diteliti UAI?
2. Siapa penelitinya?
3. Dataset apa yang tersedia?
4. Project apa yang berjalan?
5. Mana yang masih ide?
6. Mana yang sedang eksperimen?
7. Mana yang sudah menjadi TA?
8. Mana yang menghasilkan paper?
9. Mana yang sudah publikasi?
10. Mana yang menghasilkan software/model/HKI?
11. Riset berikutnya dapat melanjutkan dari mana?

Itulah definisi pusat riset yang berhasil: **institutional research memory + collaboration platform + reproducibility infrastructure** — bukan code hosting, dan bukan pula folder Drive yang hanya diketahui pemiliknya. Instrumen yang membuatnya mungkin sudah ada di repo ini: Research ID sebagai primary key, Issue sebagai unit riset, PR sebagai research review, Release sebagai milestone, GitHub Projects sebagai Research Mission Control ([GOVERNANCE.md](../../GOVERNANCE.md)).

## 4. Arsitektur final

```
                          UAI AI RESEARCH CENTER
                                   │
                           GitHub Organization
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
          STRATEGY            RESEARCH OS           EDUCATION
              │                    │                    │
           Roadmap            Methodology         Course Pipeline
              │                    │                    │
              └──────────── RESEARCH BACKLOG ───────────┘
                                   │
                           RESEARCH PROJECT
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                  DATA           CODE         EXPERIMENT
                    └──────────────┼──────────────┘
                                   │
                            RESEARCH GATES
                                   │
                             RESEARCH PACK
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                   TA            PAPER           HKI
                    └──────────────┼──────────────┘
                                   │
                             PUBLICATIONS
                                   │
                                   ▼
                         NEW RESEARCH BACKLOG
```

Tiga cabang atas (Strategy, Research OS, Education) adalah **fungsi hub**; cabang tengah (Research Project → Gates → Pack) adalah **pipeline**; cabang bawah (TA/Paper/HKI → Publications → New Backlog) adalah **compounding loop**. Pusat riset "memiliki" cabang atas dan bawah; cabang tengah dimiliki tim riset masing-masing dengan dosen sebagai owner.

## 5. Hubungan dengan Prodi, fakultas, universitas, dan Renstra

| Pihak | Peran terhadap pusat riset | Yang diterima dari pusat riset |
|---|---|---|
| **Prodi Informatika** | Rumah administratif; menetapkan mode MK, RPS, dan Metopen sebagai gate; Kaprodi anggota `@directors` | Evidence akreditasi (riset mahasiswa, publikasi, dataset, kolaborasi), TA lebih baik, portofolio riset per dosen (BKD) |
| **Fakultas** | Menyediakan akses lintas prodi (Gizi, Teknologi Pangan, Psikologi, Hukum, Ekonomi, Bahasa, Komunikasi, dll.[^2]); mengesahkan MoU ringan internal | Kapabilitas AI untuk masalah domain fakultas; riset lintas fakultas; publikasi bersama ([AIR-04](04-cross-faculty-ai-model.md)) |
| **Universitas (LPPM/unit riset, unit HKI, unit kerja sama)** | Skema penelitian internal, hibah, HKI, MoU eksternal, compute institusi; alignment Renstra Penelitian | Pipeline riset yang siap didanai; keterlibatan mahasiswa yang terdokumentasi; evidence PP-PTS ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)) |
| **Renstra Penelitian UAI** | Acuan arah; topik riset diarahkan selaras dengannya[^1] | Alignment map roadmap ↔ Renstra ([research-roadmap/alignment/uai.md](../../research-roadmap/alignment/uai.md)); pelaporan capaian per tema |
| **Mitra eksternal** | Sumber masalah, data, dan dampak | Brief, prototype, akses talenta, publikasi bersama |

Pusat riset tidak menggantikan LPPM/unit riset universitas; ia adalah **mesin pipeline** di tingkat Prodi/fakultas yang membuat riset lebih mudah didanai, dilaporkan, dan dipublikasikan oleh unit universitas.

## 6. Prinsip: organisasi berdasarkan sistem, bukan orang

Jangan membuat struktur `repo-pak-x` atau `lab-bu-y`. Struktur pusat riset mengikuti tujuh lapis sistem; orang menjadi *owner/contributor* pada lapis itu, bukan struktur utamanya.

| Lapis | Isi | Wujud di GitHub |
|---|---|---|
| **Strategy** | Roadmap, klaster, domain, alignment | `research-roadmap` |
| **Research Infrastructure** | Research OS, template, gate, protokol AI, registry | `research-os`, `datasets-registry`, `.github` |
| **Research Programs** | Tema 5–10 tahun (mis. `program-ai-education`, `program-responsible-ai`) | `program-*` (dibuat ketika isi riil ada) |
| **Research Projects** | Riset 3–12 bulan dengan Research ID | `proj-YYYY-topic` |
| **Education** | MK → pipeline, Metopen studio | `research-based-learning`, `metopen-research-studio` |
| **Outputs** | Publikasi, artefak, dataset rilis | `publications` |
| **Community** | Tim, reviewer, mitra, backlog terbuka | GitHub Teams, `research-backlog` |

Konsekuensinya: ketika dosen pindah, riset tetap ada (Research ID, repositori, handoff); ketika kepala pusat riset berganti, agenda tetap ada (roadmap, backlog); ketika mahasiswa lulus, asset tetap ada (registry, release).

## 7. Model operasi minimum

Peran mengikuti tim GitHub di [GOVERNANCE.md §3](../../GOVERNANCE.md) dan RACI di [GOV-01](../07-governance/01-governance-model.md):

| Peran | Siapa | Tugas inti di hub |
|---|---|---|
| `@directors` | Kepala pusat riset, Kaprodi | Agenda, prioritas, IP review, MoU |
| `@research-leads` | Ketua klaster C1–C4 / program | Validasi backlog klaster, mentor, review roadmap |
| `@faculty` | Dosen | Owner asset MK, mentor, reviewer gate |
| `@reviewers` | Dosen + peer terlatih | Gate review, peer review manuscript |
| `@maintainers` | Pemelihara Research OS | Research ID, registry, template, workflow |
| `@students` | Mahasiswa aktif riset | Menjalankan riset di repositori sendiri |
| Admin/asisten riset | `[isi]` | Triase intake, pencatatan Mission Control, pelaporan |

Ritme minimum: triase backlog mingguan (`@maintainers` + research lead), review roadmap tahunan, Research Day per semester, laporan portofolio per semester ke Prodi/fakultas. Fase implementasi (Foundation → Research OS → Pilot Metopen → Curriculum Integration → AI Center Launch → Public Research Portal) ada di [GOV-02](../07-governance/02-implementation-roadmap.md); pusat riset "diluncurkan" secara formal pada Phase 4, tetapi fungsinya sudah berjalan sejak Phase 2 lewat Metopen.

## 8. Yang bukan AI Research Center

- **Bukan lab tunggal** dengan anggota tetap; keanggotaan mengikuti riset yang berjalan.
- **Bukan sistem kepegawaian**; Faculty Portfolio membantu BKD dan pelaporan, tetapi GitHub tetap research tracking system, bukan alat penilaian kinerja orang.
- **Bukan penerbit atau pabrik paper**; output diakui dalam 13 jenis ([ARC-06](../02-academic-architecture/06-research-output-taxonomy.md)) dan venue bermasalah tidak dihitung.
- **Bukan gudang data**; data sensitif tidak pernah disimpan mentah ([SECURITY.md](../../SECURITY.md)).
- **Bukan pengganti Metopen atau TA**; ia menyediakan masalah, mentor, data, compute, dan jalur output untuk keduanya.

## 9. Dari dokumen ini ke concept paper

Concept paper / proposal pusat riset (Artefak 2 dalam [research-os/README](../README.md)) dapat disusun langsung dari repo:

| Bagian concept paper | Sumber |
|---|---|
| Latar belakang & gap | [STR-01](../01-strategic-foundation/01-current-state-and-gaps.md) |
| Visi, misi, endgame | [STR-02](../01-strategic-foundation/02-vision-and-endgame.md), §1 dokumen ini |
| Konsep hub & fungsi | §2–§4 dokumen ini |
| Agenda riset | [AIR-02](02-ai-research-clusters.md), [research-roadmap](../../research-roadmap/README.md) |
| Sumber daya manusia | [AIR-03](03-faculty-research-alignment.md), [AIR-04](04-cross-faculty-ai-model.md) |
| Model kemitraan | [AIR-05](05-research-demand-supply-marketplace.md) |
| Tata kelola | [GOV-01](../07-governance/01-governance-model.md), [GOVERNANCE.md](../../GOVERNANCE.md) |
| Roadmap implementasi & KPI | [GOV-02](../07-governance/02-implementation-roadmap.md), [GOV-03](../07-governance/03-kpi-and-measurement.md) |
| Risiko | [GOV-04](../07-governance/04-risk-register.md) |
| Theory of change | [STR-05](../01-strategic-foundation/05-theory-of-change.md) |

## 10. Ringkasan

- AI Research Center adalah hub: sembilan fungsi (agenda, kolaborasi dosen, pipeline mahasiswa, dataset, compute, masalah industri, publikasi, hibah, diseminasi), masing-masing dengan layanan, mekanisme, output, KPI.
- Endgame-nya adalah GitHub sebagai institutional research memory yang menjawab sebelas pertanyaan tanpa bertanya kepada siapa pun.
- Organisasi mengikuti sistem (tujuh lapis), bukan orang; riset, agenda, dan asset bertahan melampaui pergantian orang.
- Pusat riset melayani Prodi, fakultas, universitas, dan Renstra — bukan menggantikan mereka.

[^1]: Skema penelitian internal UAI 2026 yang mensyaratkan minimal dua mahasiswa aktif dan arahan keselarasan dengan Renstra Penelitian berasal dari dokumen diskusi *Riset AI UAI untuk Negeri*; verifikasi sebelum dokumen formal.
[^2]: Daftar fakultas/prodi mitra mengikuti dokumen diskusi; nama resmi unit mengikuti struktur organisasi UAI.
