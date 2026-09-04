# Alignment Map — Keselarasan Institusional

> **ID** STR-04 · **Paket** 01 Strategic Foundation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, tim kurikulum, tim PP-PTS, tim penjaminan mutu/akreditasi, kepala AI Research Center, reviewer hibah
> **Terkait** [STR-03 Design Principles](03-design-principles.md) · [STR-05 Theory of Change](05-theory-of-change.md) · [ARC-05 CPL–CPMK–Artifact Alignment](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [GOV-05 PP-PTS & Institutional Evidence](../07-governance/05-ppts-and-institutional-evidence.md) · [AIR-01 AI Research Center Concept](../03-ai-research-ecosystem/01-ai-research-center-concept.md)

Dokumen ini khusus membahas **alignment institusional**: bagaimana UAI Informatics Research Pipeline (UIRP) memenuhi tuntutan kerangka yang sudah ada — OBE, CPL, PjBL, Team-Based Project, PP-PTS, roadmap/Renstra penelitian UAI, program AI Research Center, Tugas Akhir, dan publikasi. Pembahasan teknis (rubrik, gate, template) ada di paket lain dan tidak diulang; di sini cukup dirujuk.

Pesan utamanya satu: **UIRP tidak menambah kerangka baru di atas kerangka yang ada. Ia adalah cara menjalankan kerangka yang ada sehingga evidence-nya lahir dari satu alur kerja** (prinsip P1 *one activity, multiple outcomes*).

---

## 1. Tabel ringkas

| Kerangka | Tuntutan inti | Bagaimana UIRP memenuhinya | Evidence yang dihasilkan | Dokumen rujukan |
|---|---|---|---|---|
| **OBE** | Pembelajaran dirancang mundur dari capaian; capaian diukur dengan asesmen autentik | Endgame ditetapkan di G1; setiap gate = capaian terukur dengan *definition of done*; rubrik 5E | PR gate review, rubrik terisi, Research Pack, release milestone | [MET-02](../04-metopen-research-studio/02-metopen-course-outcomes.md), [MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md), [OPS-03](../06-execution-os/03-research-gates.md) |
| **CPL / CPMK** | Setiap CPMK dapat ditelusuri ke CPL dan ke bukti capaian mahasiswa | Kerangka CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence; setiap komponen Research Pack dipetakan ke CPMK | Matriks CPL–CPMK–artefak; artefak per mahasiswa/tim di repo riset | [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md), [MET-04](../04-metopen-research-studio/04-research-pack-specification.md) |
| **PjBL** | Pembelajaran berbasis proyek nyata dengan produk akhir yang bermakna | Metopen = studio (±30% konsep + 70% studio); satu *mini research cycle* per tim; produk = Research Pack | Sprint log, deliverable mingguan, Research Pack v1.0 | [MET-01](../04-metopen-research-studio/01-metopen-positioning.md), [MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md), [OPS-02](../06-execution-os/02-weekly-sprints.md) |
| **Team-Based Project** | Kerja tim dengan peran, kolaborasi, dan akuntabilitas individu | Tim 1–3 mahasiswa; peran tercatat di README riset; kontribusi terlihat di commit/PR; peer review W14 | Git history, PR review, peer review form, defense | [TPL-15](../08-templates/15-research-repository-template.md), [TPL-12](../08-templates/12-peer-review-template.md), [TPL-13](../08-templates/13-research-defense-template.md) |
| **PP-PTS** | Bukti kegiatan, luaran, dan indikator kinerja yang terdokumentasi dan dapat diaudit | Mapping Activity → RPS → Project → Evidence → KPI → dokumentasi; evidence diekspor dari GitHub | Issue, PR, release, registry, Mission Control export, KPI report | [GOV-05](../07-governance/05-ppts-and-institutional-evidence.md), [GOV-03](../07-governance/03-kpi-and-measurement.md) |
| **Roadmap / Renstra Penelitian UAI** | Topik riset selaras arah strategis universitas | 4 klaster × 7 domain × 3 lapis alignment (UAI, Indonesia, global); G2 mensyaratkan keselarasan klaster/domain; field Cluster & Domain di Mission Control | Backlog terklasifikasi; portofolio per klaster/domain | [`research-roadmap/`](../../research-roadmap/README.md), [AIR-02](../03-ai-research-ecosystem/02-ai-research-clusters.md), [`alignment/uai.md`](../../research-roadmap/alignment/uai.md) |
| **Program AI Research Center** | Agenda riset, kolaborasi dosen, pipeline mahasiswa, dataset, publikasi, hibah, diseminasi | Pusat riset sebagai hub dan *matching engine*; backlog, registry, Faculty Portfolio, klaster; Metopen sebagai talent funnel | Faculty Portfolio, backlog, dataset registry, program repo `program-*` | [AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md), [AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md), [AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) |
| **Tugas Akhir** | Proposal yang layak, pembimbingan efektif, hasil yang dapat dipertanggungjawabkan | Research Pack = proposal TA; handoff formal; pembimbing mulai dari G8; TA melanjutkan gate yang sama sampai Published/Released | Research Pack v1.0, handoff form, repo riset yang berlanjut | [ARC-04](../02-academic-architecture/04-build-prove-contribute.md), [TPL-14](../08-templates/14-research-handoff-template.md), [`courses/final-project`](../../research-based-learning/courses/final-project/README.md) |
| **Publikasi** | Luaran ilmiah bermutu di venue kredibel, dengan integritas dan pengungkapan AI | Backward design dari venue; venue registry non-predator; integrity checklist; AI Usage Statement; registry `PUB-` | Entri publications, manuscript di repo, checklist ditandatangani | [MET-05](../04-metopen-research-studio/05-publication-backward-design.md), [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md), [`publications/`](../../publications/README.md) |

## 2. Narasi per kerangka

### 2.1 OBE (Outcome-Based Education)

OBE menuntut desain mundur dari capaian dan asesmen yang membuktikan capaian itu, bukan menguji hafalan. UIRP sudah OBE secara struktural: seluruh semester Metopen dimulai dengan **G1 Endgame Ready** (mahasiswa menyatakan riset ini mau menjadi apa), dan setiap gate berikutnya adalah capaian dengan *definition of done*, bukti wajib, reviewer, dan kriteria lulus/gagal. Rubrik 5E menilai dimensi berpikir ilmiah (End, Evidence, Experiment, Explanation, Execution), sedangkan Research Integrity menjadi gate lulus/gagal. Nilai akhir adalah konsekuensi portofolio milestone + defense, sesuai *authentic assessment* pada tabel sweet spot ([STR-01 §4](01-current-state-and-gaps.md)).

### 2.2 CPL dan CPMK

Jembatan ke revisi RPS adalah kerangka **CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence** ([ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md)). CPMK konseptual Metopen (problem formulation, evidence discovery, synthesis, gap, RQ, hypothesis, methods, experiment, validity, AI-assisted research, research integrity, writing, defense — [MET-02](../04-metopen-research-studio/02-metopen-course-outcomes.md)) masing-masing dipetakan ke komponen Research Pack, sehingga bukti capaian CPMK adalah artefak riil, bukan nilai ujian. Kerangka yang sama dipakai AI/ML dan MK teknis lain ketika mereka menandai diri sebagai mode E atau R.

### 2.3 PjBL dan Team-Based Project

Metopen sebagai Research Studio adalah PjBL dalam bentuk paling ketat: proyek nyata (problem dengan stakeholder), proses terstruktur (17 sprint), produk bermakna (Research Pack yang dipakai TA), dan refleksi (peer review, defense). Team-Based Project terpenuhi lewat tim 1–3 orang dengan akuntabilitas individu yang terlihat di git history dan PR — sesuatu yang sulit dibuktikan pada proyek berbasis dokumen. Sprint review mingguan ([GOV-01 §4](../07-governance/01-governance-model.md)) adalah mekanisme monitoring PjBL tanpa form tambahan.

### 2.4 PP-PTS

Program pendanaan/penguatan perguruan tinggi swasta menuntut bukti kegiatan, luaran, dan indikator kinerja yang dapat diaudit. UIRP memenuhi ini dengan prinsip *one activity, multiple outcomes*: Issue, PR gate, release, dan registry adalah evidence yang lahir otomatis dari alur riset. Mapping lengkap **Activity → RPS → Project → Evidence → KPI → PP-PTS documentation**, cara ekspor, dan checklist audit ada di [GOV-05](../07-governance/05-ppts-and-institutional-evidence.md). Catatan: nama program pendanaan dan format laporan resmi perlu diverifikasi; dokumen ini memakai istilah PP-PTS sebagaimana dokumen sumber.

### 2.5 Roadmap dan Renstra Penelitian UAI

Skema penelitian internal UAI mengarahkan topik agar terkait Renstra Penelitian universitas (sumber: dokumen diskusi; verifikasi sebelum dokumen formal). UIRP menerjemahkannya menjadi struktur yang dapat dioperasikan: [`research-roadmap/`](../../research-roadmap/README.md) 2026–2030 dengan empat klaster (C1 Models, C2 Systems, C3 Human-AI, C4 Applied), tujuh domain (education, halal, health, food, government, business, social-impact), dan tiga lapis alignment (UAI, Indonesia, global). G2 Problem Ready mensyaratkan setiap riset menunjuk klaster dan domainnya, sehingga portofolio Prodi terbentuk mengikuti roadmap, bukan minat sesaat (menjawab GAP-5).

### 2.6 Program AI Research Center

Pusat riset diposisikan sebagai **hub**, bukan satu lab: research agenda, faculty collaboration, student pipeline, datasets, compute, industry problem, publication, research grants, dissemination ([AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md)). UIRP memberi pusat riset tiga hal yang biasanya tidak dimiliki pusat riset baru: **pipeline mahasiswa** yang TA-ready setiap semester, **backlog masalah** yang tervalidasi, dan **registry** dataset/publikasi. Sebaliknya, pusat riset memberi Metopen problem berkualitas, mentor, dan klaster. Faculty Portfolio di Mission Control melayani BKD, pelaporan riset, perencanaan hibah, akreditasi, dan evaluasi roadmap — dengan catatan GitHub tetap *research tracking system*, bukan sistem kepegawaian ([GOVERNANCE.md §9](../../GOVERNANCE.md)).

### 2.7 Tugas Akhir

Alignment terpenting secara akademik: **proposal Metopen langsung menjadi TA**. Research Pack v1.0 adalah proposal TA; handoff ([TPL-14](../08-templates/14-research-handoff-template.md)) mencatat *what exists, missing evidence, next steps, owner*; pembimbing TA memulai dari G8, bukan dari nol. Selama TA, riset melanjutkan gate yang sama (G6–G7 dengan data penuh, lalu Published/Released), sehingga sistem penilaian, template, dan repository tidak berganti antar semester. Keputusan formal yang diperlukan tercantum di [MST-01 §6](../00-master/01-executive-summary.md) butir 2.

### 2.8 Publikasi

Publikasi diperlakukan sebagai *orientation*, bukan *obsession* (P7). Backward design dari venue target menaikkan kualitas semua riset; venue registry mencegah jurnal predator; integrity checklist dan AI Usage Statement memenuhi kebijakan publikasi modern yang mewajibkan pengungkapan AI dalam proses riset. Registry `PUB-YYYY-NNN` di [`publications/`](../../publications/README.md) menyimpan metadata (bukan PDF publisher) sehingga rekam jejak Prodi tersusun otomatis.

## 3. Peta alignment terhadap gate

Tabel ini menunjukkan pada gate mana setiap kerangka mendapatkan evidence utamanya, agar tim penjaminan mutu tahu kapan harus melihat.

| Gate | OBE/CPMK | PjBL/TBP | PP-PTS | Roadmap | AI Center | TA | Publikasi |
|---|---|---|---|---|---|---|---|
| G1 Endgame | ● | ● | | | | ● | |
| G2 Problem | ● | ● | ● | ● | ● | | |
| G3 Evidence | ● | ● | | | | | ● |
| G4 Question | ● | ● | | ● | | ● | |
| G5 Method | ● | ● | ● | | ● | ● | ● |
| G6 Experiment | ● | ● | ● | | ● | ● | |
| G7 Claim | ● | ● | | | | ● | ● |
| G8 Contribution | ● | ● | ● | ● | ● | ● | ● |

## 4. Yang belum selaras dan perlu keputusan

| Isu | Status | Tindak lanjut |
|---|---|---|
| Pengakuan Research Pack sebagai proposal TA resmi | Belum diputuskan | [MST-01 §6](../00-master/01-executive-summary.md) butir 2 |
| Pengakuan beban mentor riset dalam BKD/penugasan | Belum diputuskan | [MST-01 §6](../00-master/01-executive-summary.md) butir 7; [GOV-01](../07-governance/01-governance-model.md) |
| Nama resmi program pendanaan dan format laporan | Perlu verifikasi | [GOV-05 §6](../07-governance/05-ppts-and-institutional-evidence.md) |
| Kesesuaian CPL resmi Prodi dengan CPMK konseptual MET-02 | Perlu pemetaan oleh tim kurikulum | [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) |
| Kebijakan AI universitas (jika ada) vs AIX-04 | Perlu pengecekan | [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md) |

Rantai sebab-akibat yang menjelaskan mengapa alignment ini menghasilkan dampak: [STR-05 Theory of Change](05-theory-of-change.md).
