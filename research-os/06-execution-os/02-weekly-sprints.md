# Weekly Sprints — 145 Microtasks dalam 17 Sprint

> **ID** OPS-02 · **Paket** 06 Execution Operating System · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa, dosen pengampu, mentor, asisten studio
> **Terkait** [OPS-01 Research WBS](01-research-wbs-master.md) · [OPS-03 Research Gates](03-research-gates.md) · [OPS-04 Dependency & Critical Path](04-dependency-and-critical-path.md) · [OPS-05 Student Weekly Playbook](05-student-weekly-playbook.md) · [MET-03 16-Week Blueprint](../04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)

## Mengapa mahasiswa tidak melihat 145 task sekaligus

Research WBS ([OPS-01](01-research-wbs-master.md)) berisi 145 microtask. Kalau seluruhnya diperlihatkan pada minggu pertama, yang terjadi bukan kejelasan, melainkan kelumpuhan: mahasiswa membaca task W13 "tulis manuscript" pada saat mereka belum tahu masalahnya apa. Karena itu WBS **dipotong menjadi 17 sprint** — satu sprint onboarding (S0) dan enam belas sprint mingguan (S1–S16) yang mengikuti blueprint Metopen. Setiap sprint hanya berisi **5–10 task (umumnya 7–10)**, semuanya mengejar satu Research Gate, dan semuanya selesai dalam satu minggu.

Prinsipnya sama dengan *production line*: mahasiswa tidak "belajar membuat proposal" selama satu semester; mereka menjalankan satu mini research cycle sprint demi sprint, dan proposal TA lahir sebagai konsekuensinya. Backend-nya (WBS, dependency, gate) kompleks; frontend-nya (halaman mingguan) ringan.

Aturan pembagian:

1. Satu sprint = satu minggu kalender = satu halaman di `metopen-research-studio/weeks/`.
2. Satu sprint hanya mengejar **satu gate**. Gate G3 (Evidence) mendapat tiga sprint (S3–S5); G8 (Contribution) mendapat empat sprint (S13–S16) karena bobot penulisan, review, revisi, dan defense.
3. Setiap sprint S1–S15 memiliki satu task **sesi studio** (konsep ±30%) — S0 onboarding dan S16 defense tidak —, beberapa task **produksi artefak** (studio ±70%), satu task **AI Usage Log + jurnal**, dan — pada sprint gate — satu task **PR GATE REVIEW**.
4. Task tidak boleh dipindah ke sprint lebih awal bila dependency-nya belum ada ([OPS-04](04-dependency-and-critical-path.md)); boleh mundur satu sprint dengan konsekuensi yang dijelaskan di bagian *Jika terlambat*.

## Peta 17 sprint → 8 gate

```
 S0        S1        S2        S3   S4   S5        S6        S7   S8        S9   S10       S11  S12       S13  S14  S15  S16
 Onboard   Endgame   Problem   Search Evid Gap     RQ        Method Design  Repo Pilot     Anal Contrib   Manu Peer Rev  Def
 ┌──┐      ┌──┐      ┌──┐      ┌──┬──┬──┐          ┌──┐      ┌──┬──┐        ┌──┬──┐        ┌──┬──┐        ┌──┬──┬──┬──┐
 │6 │      │8 │      │9 │      │9 │9 │8 │          │9 │      │10│9 │        │9 │9 │        │9 │8 │        │9 │8 │7 │9 │
 └─┬┘      └─┬┘      └─┬┘      └──┴──┴─┬┘          └─┬┘      └──┴─┬┘        └──┴─┬┘        └──┴─┬┘        └──┴──┴──┴─┬┘
   └────┬────┘         │               │             │           │              │              │                      │
     ▼ G1 Endgame    ▼ G2 Problem    ▼ G3 Evidence ▼ G4 Question ▼ G5 Method  ▼ G6 Experiment ▼ G7 Claim      ▼ G8 Contribution
       Ready           Ready  v0.1     Ready  v0.2    Ready         Ready v0.3   Ready  v0.5     Ready           Ready  v0.8 → v1.0
```

Angka dalam kotak = jumlah task per sprint (total 145). Release milestone (`v0.1`, `v0.2`, `v0.3`, `v0.5`, `v0.8`, `v1.0`) mengikuti [OPS-03](03-research-gates.md).

## Ritme setiap sprint

| Kapan | Apa | Durasi |
|---|---|---|
| Awal sesi studio (Senin) | **Sprint planning**: buka halaman minggu, baca *This Week*, bagi task antar anggota, tandai task yang sudah punya semua dependency | 10 menit |
| Sesi studio | Task sesi (konsep) + mulai task produksi | 100 menit |
| Selama minggu | Kerjakan task produksi; commit dengan Task ID; catat AI Usage Log | sesuai effort |
| Akhir minggu (Jumat) | **Gate check**: cek *Done When*; pada sprint gate, buka/merge PR GATE REVIEW; tulis jurnal mingguan | 15 menit |

Beban jam pada tabel di bawah adalah **total jam tim** (1–3 orang) menurut kolom *Estimated Effort* WBS. Untuk tim 2 orang, bagi dua; untuk mahasiswa yang bekerja sendiri, sprint terberat (S4, S9, S11) perlu dibagi ke akhir pekan atau task non-kritis digeser sesuai [OPS-04](04-dependency-and-critical-path.md).

---

## S0 — Onboarding (Gate G1) · 6 task · 8h

**Sprint goal:** Semua prasyarat teknis dan tim siap sehingga W1 langsung bekerja pada riset, bukan pada akun.

| Task ID | Task |
|---|---|
| OPS-001 | Buat akun GitHub dan gabung organisasi riset |
| OPS-002 | Baca Student Weekly Playbook dan AI Research Protocol |
| OPS-003 | Bentuk tim riset 1-3 orang dan tetapkan peran |
| OPS-004 | Pilih entry door dan kandidat masalah awal |
| OPS-005 | Buat repositori riset dari template TPL-15 |
| OPS-006 | Mulai AI Usage Log dan catat penggunaan pertama |

**Deliverable:** repositori riset dari [TPL-15](../08-templates/15-research-repository-template.md), `docs/team.md`, `docs/AI-USAGE.md`, agreement AI Research Protocol.
**Definition of done:** semua anggota punya akun dan akses; repo berstruktur standar; AI Usage Log berisi minimal 1 entri; entry door dipilih.

## S1 — W1 Endgame (Gate G1) · 8 task · 9.5h

**Sprint goal:** Tim dapat mengucapkan "riset ini menuju ___ lewat pintu ___" dan menuliskannya sebagai klaim pengetahuan, bukan sekadar aplikasi.

| Task ID | Task |
|---|---|
| OPS-007 | Ikuti sesi Research Mindset dan bedakan proyek vs riset |
| OPS-008 | Tetapkan endgame: minimum TA Ready, target Research Ready |
| OPS-009 | Tulis klaim pengetahuan awal yang ingin dibuktikan |
| OPS-010 | Identifikasi kandidat dosen mentor dan klaster riset |
| OPS-011 | Buka Issue type:problem awal dengan Research ID sementara |
| OPS-012 | Tulis Research One-Pager v0 bagian identitas dan endgame |
| OPS-013 | Siapkan PR GATE REVIEW: Endgame Ready |
| OPS-014 | Perbarui AI Usage Log dan jurnal mingguan W1 |

**Deliverable:** `docs/endgame.md`, Issue `type:problem`, One-Pager v0 (parsial), PR `GATE REVIEW: Endgame Ready`.
**Definition of done:** PR G1 dibuka, direview dosen pengampu, dan di-merge (merge = G1 lulus); endgame memuat minimum/target/aspirasi dan klaim awal; kandidat mentor teridentifikasi.

## S2 — W2 Problem (Gate G2) · 9 task · 14h

**Sprint goal:** Masalah dinyatakan problem-first dengan bukti dari stakeholder nyata, dan Research ID resmi diberikan.

| Task ID | Task |
|---|---|
| OPS-015 | Ikuti sesi Problem Discovery dan latihan problem-first |
| OPS-016 | Wawancara atau observasi stakeholder masalah |
| OPS-017 | Tulis Problem Brief |
| OPS-018 | Tulis Stakeholder & Impact Statement |
| OPS-019 | Selaraskan masalah dengan klaster dan domain roadmap |
| OPS-020 | Lengkapi Research One-Pager v0 |
| OPS-021 | Perbarui Issue backlog dan ajukan permohonan Research ID resmi |
| OPS-022 | Siapkan PR GATE REVIEW: Problem Ready (problem-review.md) |
| OPS-023 | Perbarui AI Usage Log dan jurnal mingguan W2 |

**Deliverable:** `docs/problem.md` (Problem Brief + Stakeholder & Impact), One-Pager v0, Research ID `UIAI-YYYY-NNN` (ditetapkan @maintainers saat PR G2 di-merge), release `v0.1 Problem Validated`.
**Definition of done:** PR G2 termerge oleh dosen + 1 peer; orang di luar tim dapat menjelaskan ulang masalah dalam dua kalimat; tidak ada nama algoritma di Problem Brief.

## S3 — W3 Search (Gate G3) · 9 task · 16.5h

**Sprint goal:** Strategi pencarian terdokumentasi dan dijalankan; setiap kandidat sumber terverifikasi ada.

| Task ID | Task |
|---|---|
| OPS-024 | Ikuti sesi Evidence Discovery dan kualitas sumber |
| OPS-025 | Susun daftar kata kunci dan sinonim dari Problem Brief |
| OPS-026 | Tulis search strategy: basis data, kriteria inklusi/eksklusi |
| OPS-027 | Jalankan pencarian dan catat log pencarian |
| OPS-028 | Lakukan screening judul/abstrak menjadi 30-40 kandidat |
| OPS-029 | Lakukan citation chaining pada 3-5 sumber kunci |
| OPS-030 | Verifikasi tiap referensi (DOI/URL) dan buat references.bib |
| OPS-031 | Buka Issue type:literature-gap awal (hipotesis gap) |
| OPS-032 | Perbarui AI Usage Log dan jurnal mingguan W3 |

**Deliverable:** `docs/literature/search-strategy.md`, `search-log.csv`, `screening.csv`, `references.bib` terverifikasi, Issue `type:literature-gap` (dugaan).
**Definition of done:** minimal 8 query tercatat; 30–40 kandidat lolos screening dengan alasan; 100% DOI/URL dibuka manual; entri AI Usage Log verifikasi sumber ada.

## S4 — W4 Evidence (Gate G3) · 9 task · 22h

**Sprint goal:** 15–25 sumber primer benar-benar dibaca dan diekstrak ke synthesis matrix dengan penilaian kualitas.

| Task ID | Task |
|---|---|
| OPS-033 | Ikuti sesi membaca kritis dan synthesis matrix |
| OPS-034 | Rancang kolom synthesis matrix |
| OPS-035 | Baca dan ekstrak 8-12 sumber prioritas ke matriks |
| OPS-036 | Baca dan ekstrak 8-12 sumber berikutnya ke matriks |
| OPS-037 | Catat metrik, baseline, dan dataset yang lazim di literatur |
| OPS-038 | Jalankan pencarian pelengkap untuk sumber yang belum tercakup |
| OPS-039 | Verifikasi ulang seluruh entri references.bib |
| OPS-040 | Nilai kualitas tiap sumber (venue, peer review, tahun, sitasi) |
| OPS-041 | Perbarui AI Usage Log dan jurnal mingguan W4 |

**Deliverable:** `docs/literature/synthesis-matrix.csv` (15–25 baris), `common-metrics-baselines.md`, `verification.md`.
**Definition of done:** setiap baris matriks berkolom `verified=yes` dan `quality`; dua anggota memeriksa silang references.bib; daftar metrik/baseline/dataset siap dipakai di W7. Ini sprint terberat pertama — bagi bacaan sejak Senin.

## S5 — W5 Gap (Gate G3) · 8 task · 15h

**Sprint goal:** Matriks menunjukkan pola (konsisten / bertentangan / belum diuji) dan gap kandidat lolos uji kelayakan; G3 lulus.

| Task ID | Task |
|---|---|
| OPS-042 | Ikuti sesi From Literature to Gap |
| OPS-043 | Analisis pola matriks: konsisten, bertentangan, belum diuji |
| OPS-044 | Tulis Literature Evidence Map (docs/literature-map.md) |
| OPS-045 | Rumuskan kandidat research gap (2-3) dari pola |
| OPS-046 | Uji kandidat gap terhadap kelayakan semester + TA |
| OPS-047 | Siapkan PR GATE REVIEW: Evidence Ready (evidence-review.md) |
| OPS-048 | Presentasikan Literature Evidence Map di studio dan catat umpan balik |
| OPS-049 | Perbarui AI Usage Log dan jurnal mingguan W5 |

**Deliverable:** `docs/literature-map.md` (pola + kandidat gap + kelayakan), release `v0.2 Evidence Ready`, catatan umpan balik studio.
**Definition of done:** PR G3 termerge; setiap pola menunjuk minimal 2 baris matriks; satu gap utama + satu cadangan dipilih; gap lain diparkir ke backlog.

## S6 — W6 RQ (Gate G4) · 9 task · 12h

**Sprint goal:** RQ/hipotesis yang dapat difalsifikasi diturunkan langsung dari gap dan matriks; contribution statement tidak melebihi apa yang RQ dapat buktikan.

| Task ID | Task |
|---|---|
| OPS-050 | Ikuti sesi RQ, Claim & Contribution |
| OPS-051 | Tulis Research Gap final dengan Gap-Claim-Evidence alignment |
| OPS-052 | Rumuskan 1-3 RQ dan/atau hipotesis yang dapat difalsifikasi |
| OPS-053 | Tulis Contribution Statement |
| OPS-054 | Uji RQ dengan checklist keterjawaban dan falsifiabilitas |
| OPS-055 | Perbarui Research One-Pager ke v1 (problem-gap-RQ-contribution) |
| OPS-056 | Buka Issue type:research-question |
| OPS-057 | Siapkan PR GATE REVIEW: Question Ready |
| OPS-058 | Perbarui AI Usage Log dan jurnal mingguan W6 |

**Deliverable:** `docs/research-question.md` (gap final, RQ, contribution, RQ check), One-Pager v1, Issue `type:research-question`.
**Definition of done:** PR G4 termerge oleh dosen + mentor; setiap RQ ditelusuri ke baris matriks; hasil yang akan membatalkan tiap RQ tertulis. Sprint ini ringan secara jam tetapi berat secara berpikir — jangan diisi task lain.

## S7 — W7 Method (Gate G5) · 10 task · 17h

**Sprint goal:** Desain riset lengkap: metode, variabel, data plan, baseline, metrik terkunci, design card, threats awal — sebelum satu baris kode eksperimen ditulis.

| Task ID | Task |
|---|---|
| OPS-059 | Ikuti sesi Computing Research Methods Map dan validitas |
| OPS-060 | Pilih jenis metode dari Methods Map untuk tiap RQ |
| OPS-061 | Definisikan variabel, konstruk, kontrol, dan sampling |
| OPS-062 | Tulis Dataset/Data Plan: sumber, akses, lisensi, privasi, ukuran |
| OPS-063 | Daftarkan dataset ke datasets-registry (dataset card) |
| OPS-064 | Tetapkan baseline paling sederhana dan alasannya |
| OPS-065 | Pilih metrik yang selaras dengan RQ dan prosedur evaluasi anti-leakage |
| OPS-066 | Isi Research Design Card (TPL-08) |
| OPS-067 | Tulis Threats to Validity awal (4 jenis validitas) |
| OPS-068 | Perbarui AI Usage Log dan jurnal mingguan W7 |

**Deliverable:** `docs/research-design.md`, `docs/data-plan.md`, `docs/design-card.md` ([TPL-08](../08-templates/08-research-design-card.md)), dataset card di `datasets-registry/` ([TPL-05](../08-templates/05-dataset-registry-template.md)), threats v1 (`docs/research-design.md` §Threats).
**Definition of done:** metrik dan baseline **terkunci dengan tanggal commit** sebelum W9; design card tanpa field kosong; dataset card diajukan.

## S8 — W8 Design Defense (Gate G5) · 9 task · 16.5h

**Sprint goal:** Desain dipertahankan pada Mid-semester Research Pitch dan diserang red team; revisi dilakukan; G5 lulus.

| Task ID | Task |
|---|---|
| OPS-069 | Ikuti sesi Measurement & Evaluation dan persiapan red team |
| OPS-070 | Tulis Ethics & Privacy plan (docs/ethics.md) |
| OPS-071 | Isi Experiment Card untuk pilot (TPL-09) |
| OPS-072 | Susun slide Mid-semester Research Pitch (7-10 menit) |
| OPS-073 | Lakukan Red Team Review terhadap desain tim lain |
| OPS-074 | Presentasikan pitch dan terima Red Team Review |
| OPS-075 | Revisi Research Design berdasarkan red team |
| OPS-076 | Siapkan PR GATE REVIEW: Method Ready (method-review.md) |
| OPS-077 | Perbarui AI Usage Log dan jurnal mingguan W8 |

**Deliverable:** `docs/ethics.md`, `experiments/pilot-01/experiment-card.md` ([TPL-09](../08-templates/09-experiment-card.md)), `presentation/midterm-pitch.pdf`, `docs/reviews/midterm-red-team.md`, release `v0.3 Research Design`.
**Definition of done:** PR G5 termerge; setiap serangan red team berstatus diterima/ditolak dengan alasan; expected result pilot tertulis sebelum eksperimen. Lolos G5 = status **TA Ready**.

## S9 — W9 Repository (Gate G6) · 9 task · 24h

**Sprint goal:** Repositori menjadi reproducibility package: environment, seed, pipeline data anti-leakage, baseline, metode, satu perintah untuk menjalankan semuanya.

| Task ID | Task |
|---|---|
| OPS-078 | Ikuti sesi Data, Experiments & Reproducibility |
| OPS-079 | Siapkan environment dan seed (requirements/environment, config) |
| OPS-080 | Bangun pipeline data: loading, cleaning, split anti-leakage |
| OPS-081 | Implementasikan baseline dan evaluasi metrik terkunci |
| OPS-082 | Implementasikan metode utama / artefak yang diuji |
| OPS-083 | Buat skrip run.sh/Makefile dan logging eksperimen |
| OPS-084 | Tulis experiments/README.md (reproducibility README v0) |
| OPS-085 | Perbarui AI Usage Log untuk kode yang dibantu AI dan jurnal W9 |
| OPS-086 | Lakukan code review internal dan checklist kualitas kode |

**Deliverable:** `requirements.txt`/`environment.yml`, `experiments/pilot-01/config.yaml`, `src/data.py`, `src/baseline.py`, `src/evaluate.py`, `src/method.py`, `run.sh`, `experiments/README.md` v0.
**Definition of done:** instalasi dari nol berhasil; tes anti-leakage lulus; tidak ada data mentah/pribadi di repo; setiap potongan kode berbantuan AI tercatat di AI Usage Log. Sprint terberat — mulai OPS-079/080 di hari pertama.

## S10 — W10 Pilot (Gate G6) · 9 task · 16h

**Sprint goal:** Pilot berjalan end-to-end dengan baseline dan minimal satu pembanding; peer mereproduksi angka baseline hanya dari repo.

| Task ID | Task |
|---|---|
| OPS-087 | Ikuti sesi Pilot Study / Minimum Viable Experiment |
| OPS-088 | Jalankan pilot end-to-end: baseline + minimal satu metode pembanding |
| OPS-089 | Buat tabel hasil pilot dan figur awal |
| OPS-090 | Lakukan sanity check dan uji leakage pada hasil pilot |
| OPS-091 | Minta peer mereproduksi hasil baseline dari repositori |
| OPS-092 | Perbaiki reproducibility README dan kode berdasarkan kendala peer |
| OPS-093 | Perbarui Experiment Card dengan hasil aktual dan catatan pilot |
| OPS-094 | Siapkan PR GATE REVIEW: Experiment Ready (experiment-review.md) |
| OPS-095 | Perbarui AI Usage Log dan jurnal mingguan W10 |

**Deliverable:** `results/pilot-01/` (hasil per seed, `summary.md`, `sanity-check.md`), `figures/pilot-01/`, `docs/reviews/reproduction-pilot-01.md`, release `v0.5 Pilot Experiment`.
**Definition of done:** PR G6 termerge oleh dosen + peer reproducer; label-shuffle jatuh ke chance; angka peer cocok dalam toleransi; keputusan lanjut/ubah tercatat di experiment card.

## S11 — W11 Analysis (Gate G7) · 9 task · 22.5h

**Sprint goal:** Eksperimen skala penuh dijalankan dan dianalisis jujur: ketidakpastian, error analysis, figur dengan baseline terlihat, perbandingan apple-to-apple dengan literatur.

| Task ID | Task |
|---|---|
| OPS-096 | Ikuti sesi Analyzing & Visualizing Evidence |
| OPS-097 | Jalankan eksperimen utama pada skala penuh sesuai desain |
| OPS-098 | Hitung ringkasan statistik dan ketidakpastian antar seed/fold |
| OPS-099 | Lakukan error analysis pada kasus gagal |
| OPS-100 | Buat visualisasi bukti yang jujur (figur final) |
| OPS-101 | Bandingkan hasil dengan literatur di synthesis matrix |
| OPS-102 | Tulis draft results/analysis.md |
| OPS-103 | Perbarui AI Usage Log dan jurnal mingguan W11 |
| OPS-104 | Arsipkan hasil, log, dan konfigurasi eksperimen utama |

**Deliverable:** `results/main/summary.csv`, `results/analysis.md` v0, `figures/main/`, `experiments/main/README.md`.
**Definition of done:** metrik dan prosedur identik dengan yang dikunci di G5; setiap angka ditelusuri ke run (seed, git hash); hasil negatif dilaporkan.

## S12 — W12 Contribution (Gate G7) · 8 task · 12h

**Sprint goal:** Setiap RQ dijawab dengan Claim–Evidence–Reasoning yang menunjuk tabel/figur; threats dan contribution direvisi agar tidak melebihi bukti; G7 lulus.

| Task ID | Task |
|---|---|
| OPS-105 | Ikuti sesi Scientific Argumentation (Claim-Evidence-Reasoning) |
| OPS-106 | Susun tabel Claim-Evidence-Reasoning untuk setiap RQ |
| OPS-107 | Perbarui Threats to Validity berdasarkan hasil aktual |
| OPS-108 | Revisi Contribution Statement agar tidak melebihi bukti |
| OPS-109 | Tulis bagian Limitations dan Future Work |
| OPS-110 | Perbarui Research One-Pager ke v2 (hasil dan klaim) |
| OPS-111 | Siapkan PR GATE REVIEW: Claim Ready |
| OPS-112 | Perbarui AI Usage Log dan jurnal mingguan W12 |

**Deliverable:** tabel CER di `results/analysis.md`, threats v2 (`results/analysis.md` §Threats), contribution v2, Limitations & Future Work, One-Pager v2.
**Definition of done:** PR G7 termerge oleh dosen + mentor; tidak ada klaim kausal dari korelasi; tidak ada improvement tanpa baseline. Lolos G7 = status **Research Ready**.

## S13 — W13 Manuscript (Gate G8) · 9 task · 19.5h

**Sprint goal:** Proposal TA (atau manuscript) ditulis dari artefak yang sudah ada — bukan dari nol — dan dirilis sebagai v0.8.

| Task ID | Task |
|---|---|
| OPS-113 | Ikuti sesi Scientific Writing dan struktur proposal/manuscript |
| OPS-114 | Tulis Pendahuluan dan Tinjauan Pustaka dari artefak G2-G3 |
| OPS-115 | Tulis Metode dari Research Design Card dan Data Plan |
| OPS-116 | Tulis Hasil dan Pembahasan dari analysis.md dan tabel CER |
| OPS-117 | Tulis Rencana TA (timeline semester VIII) dan target output |
| OPS-118 | Tulis AI Usage Statement dari AI Usage Log |
| OPS-119 | Rakit draft Research Pack v0.8 dan periksa kelengkapan MET-04 |
| OPS-120 | Buat release v0.8 Manuscript Draft |
| OPS-121 | Perbarui AI Usage Log dan jurnal mingguan W13 |

**Deliverable:** `paper/proposal.md` (+ PDF), `paper/AI-USAGE-STATEMENT.md`, `docs/research-pack.md` (indeks 16 komponen [MET-04](../04-metopen-research-studio/04-research-pack-specification.md)), release `v0.8 Manuscript Draft`.
**Definition of done:** tidak ada sitasi di luar `references.bib`; tidak ada klaim di luar tabel CER; indeks Research Pack tanpa komponen kosong tanpa rencana.

## S14 — W14 Peer Review (Gate G8) · 8 task · 15h

**Sprint goal:** Tim menjadi reviewer bagi tim lain dan menerima review untuk drafnya sendiri; semua komentar masuk tabel tanggapan.

| Task ID | Task |
|---|---|
| OPS-122 | Ikuti sesi Peer Review: mahasiswa menjadi reviewer |
| OPS-123 | Tulis peer review untuk draft tim lain (memberi) |
| OPS-124 | Terima peer review dan buat tabel tanggapan (response to reviewers) |
| OPS-125 | Verifikasi ulang seluruh sitasi dan angka di draft |
| OPS-126 | Perbaiki reproducibility README final dan uji dari environment bersih |
| OPS-127 | Siapkan draft slide Research Defense (TPL-13) |
| OPS-128 | Buka PR GATE REVIEW: Contribution Ready (manuscript-review.md) draft |
| OPS-129 | Perbarui AI Usage Log dan jurnal mingguan W14 |

**Deliverable:** peer review terkirim ([TPL-12](../08-templates/12-peer-review-template.md)), `paper/response-to-reviewers.md`, `paper/verification-checklist.md`, `experiments/README.md` final, `presentation/defense-draft.pdf`, PR G8 terbuka.
**Definition of done:** minimal 5 komentar spesifik diberikan ke tim lain; semua komentar yang diterima terklasifikasi mayor/minor; reproduksi final dijalankan oleh anggota yang tidak menulis kode.

## S15 — W15 Revision (Gate G8) · 7 task · 14h

**Sprint goal:** Revisi tuntas tanpa menambah klaim di luar bukti; Research Integrity Checklist ditandatangani; tim siap defense.

| Task ID | Task |
|---|---|
| OPS-130 | Ikuti sesi Revision & Defense Preparation |
| OPS-131 | Revisi proposal/manuscript sesuai tabel tanggapan |
| OPS-132 | Sinkronkan seluruh Research Pack dengan revisi |
| OPS-133 | Isi Research Integrity Checklist (TPL-11) dan tandatangani |
| OPS-134 | Latihan defense (rehearsal) dengan timer dan mock penguji |
| OPS-135 | Finalkan slide defense dan lembar ringkas untuk penguji |
| OPS-136 | Perbarui AI Usage Log dan jurnal mingguan W15 |

**Deliverable:** proposal v0.9 (revisi pasca peer review, `paper/proposal.md`), Research Pack tersinkron, `docs/integrity-checklist.md` ([TPL-11](../08-templates/11-research-integrity-checklist.md)) tertandatangani, `presentation/defense-final.pdf`, catatan rehearsal.
**Definition of done:** tabel tanggapan berstatus selesai dan dikonfirmasi reviewer; setiap butir checklist merujuk bukti; rehearsal minimal 2 kali dengan timer. **Defense tidak boleh dijadwalkan sebelum checklist ditandatangani.**

## S16 — W16 Defense (Gate G8) · 9 task · 12.5h

**Sprint goal:** Riset dipertanggungjawabkan secara oral, diwariskan lewat handoff, dan dirilis sebagai Research Pack v1.0.

| Task ID | Task |
|---|---|
| OPS-137 | Presentasikan Research Defense (7-10 menit) dan tanya jawab |
| OPS-138 | Lakukan revisi pasca-defense |
| OPS-139 | Finalkan AI Usage Statement dan AI-USAGE.md |
| OPS-140 | Isi Research Handoff (TPL-14) ke TA/mentor/AI Center |
| OPS-141 | Perbarui registry: Issue, dataset card, dan publikasi bila ada |
| OPS-142 | Lengkapi CITATION.cff, LICENSE, CHANGELOG, dan README riset |
| OPS-143 | Merge PR GATE REVIEW: Contribution Ready |
| OPS-144 | Buat release v1.0 Research Pack |
| OPS-145 | Tulis refleksi akhir semester dan rencana semester VIII |

**Deliverable:** `docs/reviews/defense-minutes.md`, `docs/handoff.md` ([TPL-14](../08-templates/14-research-handoff-template.md)), registry diperbarui, proposal v1.0 (`paper/proposal-v1.0.pdf`), PR G8 termerge, release `v1.0 Research Pack`, refleksi akhir.
**Definition of done:** dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol; release v1.0 memuat seluruh komponen MET-04; Issue menunjukkan gate G8.

---

## Rekap beban per sprint

| Sprint | Tema | Gate | Task | Jam tim | Catatan beban |
|---|---|---|---|---|---|
| S0 | Onboarding | G1 | 6 | 8 | ringan; selesaikan sebelum W1 |
| S1 | W1 Endgame | G1 | 8 | 9.5 | ringan |
| S2 | W2 Problem | G2 | 9 | 14 | sedang; wawancara butuh janji temu lebih awal |
| S3 | W3 Search | G3 | 9 | 16.5 | sedang; hampir semua berantai (lihat OPS-04) |
| S4 | W4 Evidence | G3 | 9 | 22 | **berat**; bacaan dibagi antar anggota |
| S5 | W5 Gap | G3 | 8 | 15 | sedang; PR G3 |
| S6 | W6 RQ | G4 | 9 | 12 | ringan secara jam, berat secara berpikir |
| S7 | W7 Method | G5 | 10 | 17 | sedang |
| S8 | W8 Design Defense | G5 | 9 | 16.5 | sedang; jadwal pitch ditentukan dosen |
| S9 | W9 Repository | G6 | 9 | 24 | **berat**; sprint coding |
| S10 | W10 Pilot | G6 | 9 | 16 | sedang; butuh peer reproducer dari tim lain |
| S11 | W11 Analysis | G7 | 9 | 22.5 | **berat**; eksperimen penuh + analisis |
| S12 | W12 Contribution | G7 | 8 | 12 | ringan |
| S13 | W13 Manuscript | G8 | 9 | 19.5 | sedang-berat; menulis dari artefak |
| S14 | W14 Peer Review | G8 | 8 | 15 | sedang; banyak task paralel |
| S15 | W15 Revision | G8 | 7 | 14 | sedang |
| S16 | W16 Defense | G8 | 9 | 12.5 | ringan setelah defense |
| **Total** | | | **145** | **266** | ±16.6 jam tim per minggu |

## Jika terlambat

Sprint yang tertinggal tidak "dihapus"; task yang belum selesai dibawa ke sprint berikutnya, tetapi **gate tetap berurutan**. Prioritas saat tertinggal: (1) task pada critical path ([OPS-04](04-dependency-and-critical-path.md)), (2) task PR GATE REVIEW, (3) task AI Usage Log — ketiganya tidak boleh dilewati. Task sesi studio yang terlewat diganti dengan membaca materi minggu tersebut. Skenario pemulihan per gate ada di [OPS-04 bagian *Jika satu gate terlambat*](04-dependency-and-critical-path.md#jika-satu-gate-terlambat).

## Cara memakai dokumen ini

- **Dosen pengampu**: dokumen ini adalah rencana semester; sinkron dengan [MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md). Ubah komposisi task lewat `research-wbs.csv`, lalu render ulang ([OPS-01](01-research-wbs-master.md)); daftar Task ID di dokumen ini harus diperbarui mengikuti CSV.
- **Mahasiswa**: jangan baca semua sprint sekaligus. Buka halaman minggu berjalan di `../../metopen-research-studio/weeks/` dan ikuti format [OPS-05](05-student-weekly-playbook.md).
- **Mentor**: cukup lihat *Sprint goal* dan *Definition of done* sprint berjalan, lalu periksa bukti di repositori tim.
