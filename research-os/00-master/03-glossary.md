# Glossary — Kamus Istilah & Konvensi UAI AI Research Center

> **ID** MST-03 · **Paket** 00 Master · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Semua: pimpinan, dosen, mahasiswa, reviewer, admin riset
> **Terkait** [MST-00 README](00-readme.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

Dokumen ini adalah **sumber definisi tunggal** untuk seluruh repository. Jika ada dokumen lain yang memakai istilah dengan arti berbeda, dokumen ini yang benar dan dokumen lain yang harus diperbaiki. Tujuannya sederhana: semua dosen, mahasiswa, dan reviewer memakai bahasa yang sama.

---

## 1. Konsep inti

| Istilah | Definisi |
|---|---|
| **Evidence Engineering** | Jiwa mata kuliah dan seluruh sistem: rekayasa bukti. Programmer menghasilkan software, data scientist menghasilkan model, researcher menghasilkan *credible knowledge*, dan credible knowledge membutuhkan bukti yang dirancang, dikumpulkan, diuji, dan dipertanggungjawabkan secara sistematis. |
| **Research thinking** | Alur berpikir: fenomena/masalah nyata → apa yang kita ketahui → apa yang belum diketahui → apa yang kita klaim → bukti apa yang membuat klaim itu dapat dipercaya → desain riset apa yang menghasilkan bukti itu → data/artefak/eksperimen apa yang diperlukan → apa yang bisa membatalkan kesimpulan → bisakah orang lain memeriksa/mereproduksi → *so what?* |
| **Scientific thinker** | North star mahasiswa: orang yang mampu menghasilkan credible evidence dan contribution, serta sulit dibohongi, termasuk oleh AI-nya sendiri. |
| **Amanah epistemik** | Signature UAI. Peneliti memegang amanah untuk tidak mengarang data, memilih bukti yang menguntungkan saja, menutupi hasil negatif, mengubah metrik setelah melihat hasil, mengutip yang tidak dibaca, membiarkan AI mengarang referensi, mengklaim kausalitas dari korelasi, atau melebih-lebihkan kontribusi. Dalam bahasa riset modern: *research integrity*. Dalam bahasa keimanan: kejujuran terhadap kebenaran meskipun kebenaran itu meruntuhkan hipotesis sendiri. |
| **Research Studio** | Positioning Metodologi Penelitian (Metopen): bukan "kuliah tentang penelitian", melainkan studio tempat mahasiswa menjalankan satu *mini research cycle* sehingga proposal TA lahir sebagai konsekuensinya. Komposisi ±30% concepts + 70% studio. |
| **UIRP — UAI Informatics Research Pipeline** | Nama internal keseluruhan sistem: Research Center → dosen → mata kuliah → mahasiswa → problem → dataset → project → Metopen → TA → paper → publikasi/HKI/produk → Research Center lagi. |
| **Research OS** | Repository/kumpulan dokumen yang menjawab **"how do we research?"** (folder `research-os/`). Dibedakan dari **Research Roadmap** yang menjawab **"what should we research?"** dan **Research Backlog** yang menjawab **"what could be researched next?"** |
| **Build → Prove → Contribute** | Arsitektur akademik: mata kuliah teknis **membangun** (Build) research asset; Metopen **membuktikan** (Prove) kualitas bukti; Tugas Akhir **berkontribusi** (Contribute) pengetahuan/artefak. |
| **Discover → Build → Prove → Contribute → Scale** | Research pipeline pada level pusat riset (menambah tahap Discover di awal dan Scale di akhir). |
| **Compounding loop** | Satu mata kuliah → TA lebih baik → mahasiswa lebih capable → riset dosen lebih kuat → publikasi → reputasi prodi → kolaborasi → problem lebih berkualitas → mahasiswa berikutnya mendapat research environment lebih baik. |

## 2. Artefak riset

| Istilah | Definisi |
|---|---|
| **Research Asset** | Hasil kegiatan mata kuliah/riset yang dapat dipakai ulang oleh riset berikutnya: dataset, kode, benchmark, model, prototype, literature map, problem brief, dsb. Prinsip: *research assets should compound*. |
| **Research Pack** | Deliverable akhir Metopen (UAI Informatics Research Pack): Problem Brief, Stakeholder/Impact Statement, Literature Evidence Map, Research Gap, RQ/Hypothesis, Contribution Statement, Research Design, Dataset/Data Plan, Baseline & Metrics, Pilot Experiment, Threats to Validity, Ethics & Privacy, AI Usage Statement, Reproducibility README, Proposal TA, Research Pitch. Spesifikasi lengkap: [MET-04](../04-metopen-research-studio/04-research-pack-specification.md). |
| **Research One-Pager** | Ringkasan satu halaman sebuah riset (problem, why, RQ, method, data, baseline, metric, expected contribution). Template: [TPL-01](../08-templates/01-research-one-pager-template.md). |
| **Research Repository** | Repositori git standar untuk satu riset (`proj-YYYY-topic`): README riset, `docs/` (problem, RQ, literature map, design, ethics, AI-USAGE), `data/`, `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `paper/`, `presentation/`. Template: [TPL-15](../08-templates/15-research-repository-template.md). |
| **Reproducibility package** | Minimum agar pihak lain dapat menjalankan ulang: kode, konfigurasi, seed, environment, langkah eksekusi, dan data/metadata data. |
| **Research Backlog** | Bank masalah (problem bank) Prodi/AI Center: peluang riset di masa depan, bukan kumpulan paper. Disimpan sebagai GitHub Issues + indeks di `research-backlog/`. |
| **Handoff** | Transfer riset antar tahap (Course → Metopen → TA → AI Center) dengan catatan: what exists, missing evidence, next steps, owner. Template: [TPL-14](../08-templates/14-research-handoff-template.md). |

## 3. Tahapan & kematangan

### 3.1 Research Gates (8 gerbang)

Gerbang kualitas yang harus dilewati setiap riset. Satu gate = satu *definition of done* + bukti wajib + reviewer. Definisi lengkap: [OPS-03](../06-execution-os/03-research-gates.md).

| Kode | Nama | Pertanyaan yang dijawab | Label GitHub |
|---|---|---|---|
| **G1** | Endgame Ready | Apa tujuan akhir riset ini (TA, paper, artefak, produk) dan lewat pintu masuk mana? | `gate:G1-endgame` |
| **G2** | Problem Ready | Apakah masalahnya nyata, penting, dan jelas siapa pemangku kepentingannya? | `gate:G2-problem` |
| **G3** | Evidence Ready | Apa yang sudah diketahui menurut literatur (evidence map + synthesis matrix)? | `gate:G3-evidence` |
| **G4** | Question Ready | Apa gap, RQ/hipotesis, dan kontribusi yang selaras dengan bukti? | `gate:G4-question` |
| **G5** | Method Ready | Bagaimana RQ dijawab: desain, data, baseline, metrik, threats to validity? | `gate:G5-method` |
| **G6** | Experiment Ready | Apakah pilot experiment berjalan dan repositorinya reproducible? | `gate:G6-experiment` |
| **G7** | Claim Ready | Apakah klaim didukung hasil, dan ancaman validitas sudah dibahas? | `gate:G7-claim` |
| **G8** | Contribution Ready | Apakah Research Pack lengkap, dipertahankan (defense), dan siap di-handoff? | `gate:G8-contribution` |

Pada board GitHub Projects ditambahkan dua kolom di luar gate: **Idea** (sebelum G2) dan **Published/Released** (setelah G8).

### 3.2 Research maturity (level kematangan)

| Level | Arti |
|---|---|
| **Idea** | Baru masuk backlog; belum divalidasi. |
| **TA Ready** | Outcome minimum Metopen: mahasiswa masuk semester VIII tanpa lagi mencari judul dan metode. Setara lolos G5. |
| **Research Ready** | Outcome target Metopen: mampu menjalankan satu penelitian computing sederhana dengan benar. Setara lolos G6–G7. |
| **Publication Ready** | Outcome aspirasional: hasil layak menjadi paper/dataset/artefak. Setara lolos G8 + manuscript-ready. |
| **Impact Ready** | Hasil menjadi HKI, prototype, bagian riset dosen, atau solusi industri/masyarakat. |

### 3.3 Publication readiness (MET-05)

`TA-ready → manuscript-ready → submission-ready → submitted → accepted → published`.

### 3.4 Release sebagai milestone riset

| Release | Milestone |
|---|---|
| v0.1 | Problem Validated |
| v0.2 | Evidence Ready |
| v0.3 | Research Design |
| v0.5 | Pilot Experiment |
| v0.8 | Manuscript Draft |
| v1.0 | Research Pack |
| v1.1 | Submitted |
| v2.0 | Published |

### 3.5 Entry door (pintu masuk riset)

*Multiple entry points, one pipeline.* Sebuah riset boleh masuk lewat: **Problem** (masalah nyata/stakeholder), **Dataset** (data tersedia), **Faculty Research** (riset dosen), **Course Project** (proyek mata kuliah), **Partner** (industri/pemerintah/masyarakat), **Competition** (lomba). Apa pun pintunya, gate-nya sama.

## 4. Klaster & mode AI

### 4.1 AI Research Clusters (AIR-02)

| Kode | Klaster | Label |
|---|---|---|
| **C1** | AI Models, Data & Knowledge | `cluster:models` |
| **C2** | AI Systems, Software & Security | `cluster:systems` |
| **C3** | Human-Centered & Responsible AI | `cluster:human-ai` |
| **C4** | Applied AI for Human Flourishing | `cluster:applied` |

### 4.2 Peran AI dalam agenda riset

| Istilah | Definisi |
|---|---|
| **AI Core** | Riset yang objeknya AI itu sendiri (model, data, knowledge, algoritma, evaluasi). |
| **AI Enabling** | Riset tentang infrastruktur yang memungkinkan AI: sistem, software engineering, keamanan, data engineering. |
| **AI Application** | Riset yang menerapkan AI ke domain (pendidikan, halal, kesehatan, pangan, pemerintahan, bisnis, dampak sosial). |
| **Responsible AI** | Riset dan praktik AI yang memperhatikan keadilan, privasi, keamanan, transparansi, akuntabilitas, dan nilai kemanusiaan. |

### 4.3 AI Contribution Modes mata kuliah (ARC-03)

| Mode | Arti |
|---|---|
| **F — Foundation** | Mata kuliah mendukung kapabilitas AI/riset (statistik, algoritma, basis data). |
| **E — AI-Enriched** | Mata kuliah memakai kasus/proyek AI. |
| **R — Research-Producing** | Mata kuliah menghasilkan reusable research asset. |

### 4.4 AI Research Competency (AIX-02)

`AI Consumer → AI Collaborator → AI Investigator → AI Governor`. Target Metopen: semua mahasiswa minimal **AI Investigator**, dengan perilaku **AI Governor** (memverifikasi, mendokumentasikan, mempertanggungjawabkan).

### 4.5 AI Research Protocol (AIX-04)

`Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own`. Setiap output AI harus melalui *source verification → reasoning verification → evidence verification → human accountability*. Prinsip: **AI-augmented, human-accountable science**; AI adalah research copilot, bukan epistemic authority.

## 5. Penilaian

| Istilah | Definisi |
|---|---|
| **5E Rubric** | Rubrik Metopen: **End** (kejelasan endgame & problem), **Evidence** (kualitas bukti literatur), **Experiment** (kualitas desain & pilot), **Explanation** (argumentasi claim–evidence–reasoning), **Execution** (disiplin sprint, repositori, gate). Detail: [MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md). |
| **Research Integrity Gate** | Gerbang wajib lulus/gagal (bukan skor): tidak ada fabrikasi, falsifikasi, plagiarisme, sitasi palsu, atau penggunaan AI yang tidak diungkap. Checklist: [TPL-11](../08-templates/11-research-integrity-checklist.md). |
| **Claim–Evidence–Reasoning (CER)** | Struktur argumentasi ilmiah: klaim, bukti pendukung, penalaran yang menghubungkan keduanya. |
| **Threats to validity** | Ancaman terhadap validitas internal, eksternal, konstruk, dan statistik/kesimpulan; wajib ada di setiap Research Pack. |
| **Baseline** | Pembanding paling sederhana yang masuk akal; tanpa baseline, angka metrik tidak bermakna. |
| **Leakage** | Kebocoran informasi dari data uji ke proses pelatihan/pemilihan model yang membuat hasil terlihat lebih baik dari kenyataan. |

## 6. Skema identitas (primary key sistem)

| Jenis | Format | Contoh | Diberikan saat |
|---|---|---|---|
| **Research ID** | `UIAI-YYYY-NNN` | `UIAI-2026-001` | Masalah masuk research backlog; ID mengikuti riset sepanjang lifecycle (Issue → repo → Metopen → TA → dataset → publikasi → HKI) meski judul berubah. |
| **Dataset ID** | `DS-YYYY-NNN` | `DS-2026-001` | Dataset didaftarkan di `datasets-registry/`. |
| **Publication ID** | `PUB-YYYY-NNN` | `PUB-2027-001` | Naskah mulai disiapkan dan dicatat di `publications/`. |
| **Artifact ID** | `ART-YYYY-NNN` | `ART-2026-001` | Software/model/benchmark/prototype dirilis. |
| **Document ID** | `PREFIX-NN` | `STR-01`, `MET-04` | Dokumen Research OS (lihat tabel prefix di bawah). |
| **Task ID** | `OPS-NNN` (3 digit) | `OPS-042` | Microtask dalam Research WBS ([OPS-01](../06-execution-os/01-research-wbs-master.md)). Bedakan dari dokumen `OPS-01`…`OPS-05` (2 digit). |
| **Sprint** | `S0`…`S16` | `S6` | Sprint mingguan Metopen; S0 = onboarding sebelum minggu 1. |

### Prefix dokumen Research OS

| Prefix | Paket | Folder |
|---|---|---|
| `MST` | 00 Master / Executive Navigation | `research-os/00-master/` |
| `STR` | 01 Strategic Foundation | `research-os/01-strategic-foundation/` |
| `ARC` | 02 Academic Architecture | `research-os/02-academic-architecture/` |
| `AIR` | 03 AI Research Ecosystem | `research-os/03-ai-research-ecosystem/` |
| `MET` | 04 Metopen Research Studio | `research-os/04-metopen-research-studio/` |
| `AIX` | 05 AI-Augmented Research & Meta-Thinking | `research-os/05-ai-augmented-research/` |
| `OPS` | 06 Execution Operating System | `research-os/06-execution-os/` |
| `GOV` | 07 Governance & Implementation | `research-os/07-governance/` |
| `TPL` | 08 Templates & Toolkit | `research-os/08-templates/` |

Cara merujuk lintas dokumen: *"Mengikuti Research Gate G5 sebagaimana MET-04 dan OPS-03."*

## 7. Klasifikasi akses

| Kelas | Isi | Contoh |
|---|---|---|
| **PUBLIC** | Framework, kode publik, metadata dataset publik, publikasi, template, materi belajar | `research-os/`, `publications/` |
| **INTERNAL** | Riset yang sedang berjalan, naskah belum terbit, pekerjaan mahasiswa, roadmap internal | repo `proj-*` privat |
| **RESTRICTED** | Data partner rahasia, dataset sensitif, data pribadi, proyek komersial | tidak pernah di GitHub sebagai raw data |

Prinsip: **data mentah yang sensitif tidak pernah otomatis masuk GitHub.** GitHub hanya menyimpan metadata, kode, dan artefak yang aman.

## 8. Istilah institusional

| Istilah | Definisi |
|---|---|
| **Metopen** | Metodologi Penelitian, 2 SKS, semester VII Informatika UAI. |
| **TA** | Tugas Akhir, 4 SKS, semester VIII. |
| **OBE / CPL / CPMK** | Outcome-Based Education; Capaian Pembelajaran Lulusan; Capaian Pembelajaran Mata Kuliah. |
| **RPS** | Rencana Pembelajaran Semester. |
| **PjBL** | Project-Based Learning; **Team-Based Project** adalah variannya. |
| **PP-PTS** | Program pendanaan/penguatan perguruan tinggi swasta; dokumen repo ini dapat menjadi evidence pelaporannya ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)). |
| **BKD** | Beban Kerja Dosen. |
| **HKI** | Hak Kekayaan Intelektual. |
| **LAM-INFOKOM** | Lembaga Akreditasi Mandiri Informatika dan Komputer. |
| **Renstra Penelitian** | Rencana strategis penelitian universitas; topik riset diarahkan selaras dengannya. |

## 9. Tier dokumen

| Tier | Isi | Pembaca wajib |
|---|---|---|
| **Tier 1 — Core Documents** | ±10 dokumen kebijakan/strategi | Pembuat kebijakan (Kaprodi, Dekan, pimpinan) |
| **Tier 2 — Academic Design** | ±15 dokumen desain akademik & mata kuliah | Tim kurikulum, dosen |
| **Tier 3 — Execution Toolkit** | ±30 template & playbook | Mahasiswa, mentor, admin riset |

## 10. Dua view repository

| View | Untuk | Alur |
|---|---|---|
| **View A — Institutional** | Pimpinan | Strategy → Architecture → Governance → Impact (`research-os/`) |
| **View B — Student Execution** | Mahasiswa | This Week → Tasks → Evidence → Gate → Next (`metopen-research-studio/weeks/`) |

Satu backend, dua pengalaman.
