# Metopen Research Studio — Metodologi Penelitian Informatika UAI

> **Status** Draft v0.1 (2026-09) · **View B — Student Execution** · satu backend [Research OS](../research-os/README.md), satu frontend ringan untuk mahasiswa
> **Audiens** Mahasiswa semester VII Informatika UAI (utama), asisten studio, mentor, dosen pengampu
> **Terkait** [MET-01 Positioning](../research-os/04-metopen-research-studio/01-metopen-positioning.md) · [MET-03 16-Week Blueprint](../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [MET-04 Research Pack](../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [OPS-02 Weekly Sprints](../research-os/06-execution-os/02-weekly-sprints.md) · [OPS-03 Research Gates](../research-os/06-execution-os/03-research-gates.md) · [OPS-05 Student Weekly Playbook](../research-os/06-execution-os/05-student-weekly-playbook.md) · [Student Guide](../research-based-learning/student-guide/README.md)

## 1. Apa studio ini

Metodologi Penelitian di Informatika UAI **bukan "kuliah tentang penelitian"**. Ia adalah studio tempat setiap tim menjalankan **satu mini research cycle** — Problem → Evidence Map → Gap → RQ → Research Design → Pilot → Validity → Reproducible Artifact → Proposal TA — sehingga proposal TA lahir sebagai konsekuensinya, bukan sebagai tugas akhir semester.

Folder ini adalah **View B (Student Execution)**: apa yang Anda lihat setiap minggu.

```
This Week  →  Tasks  →  Evidence  →  Gate  →  Next
```

Di belakang layar ada 145 microtask, 17 sprint, 8 gate, dan peta ketergantungan ([`research-os/06-execution-os/`](../research-os/06-execution-os/03-research-gates.md)). Anda **tidak perlu** membacanya. Cukup buka halaman minggu berjalan di [`weeks/`](weeks/week-01-endgame.md), kerjakan task-nya, taruh buktinya di repositori, lewati gate-nya, lanjut ke minggu berikutnya. *Backend kompleks, frontend ringan* — satu backend, dua pengalaman ([MST-03 §10](../research-os/00-master/03-glossary.md)).

| View | Untuk | Alur | Tempat |
|---|---|---|---|
| A — Institutional | Pimpinan, tim kurikulum, dosen | Strategy → Architecture → Governance → Impact | [`research-os/`](../research-os/README.md) |
| **B — Student Execution** | **Mahasiswa** | **This Week → Tasks → Evidence → Gate → Next** | **folder ini** |

## 2. Identitas mata kuliah

| Aspek | Ketentuan |
|---|---|
| Nama formal (kurikulum, RPS, transkrip) | **Metodologi Penelitian**, 2 SKS, semester VII, Program Studi Informatika UAI |
| Positioning internal | **AI-Augmented Research Methods & Evidence Engineering for Informatics** ([MET-01](../research-os/04-metopen-research-studio/01-metopen-positioning.md)) |
| Bentuk | Research Studio: ±30% concepts + ±70% studio; sesi 100 menit per minggu |
| Deliverable | UAI Informatics Research Pack (16 artefak) + Proposal TA ([MET-04](../research-os/04-metopen-research-studio/04-research-pack-specification.md)) |
| Jiwa | Evidence Engineering — merekayasa bukti yang dirancang, dikumpulkan, diuji, dan dipertanggungjawabkan |
| Signature UAI | Amanah epistemik: jujur pada kebenaran meski meruntuhkan hipotesis sendiri |
| Posisi dalam pipeline | Mata kuliah teknis **Build** → Metopen **Prove** → Tugas Akhir **Contribute** |

## 3. North star

> **100% mahasiswa selesai Metopen sudah TA-ready; mahasiswa terbaik research/publication-ready.**

| Layer | Nama | Arti | Setara gate |
|---|---|---|---|
| Minimum | **TA Ready** | Masuk semester VIII tanpa lagi mencari judul dan metode | G5 |
| Target | **Research Ready** | Mampu menjalankan satu penelitian computing sederhana dengan benar | G6–G7 |
| Aspirasional | **Publication / Impact Ready** | Hasil layak menjadi paper, dataset, artefak open-source, HKI, prototype, atau bagian riset dosen | G8 + manuscript-ready |

Yang membedakan Anda di akhir semester bukan seberapa canggih modelnya, melainkan apakah Anda **sulit dibohongi — termasuk oleh AI Anda sendiri**.

## 4. Bentuk sesi: 30% konsep, 70% studio, 100 menit

| Menit | Blok | Isi |
|---|---|---|
| 0–30 | **Concept** | Satu konsep inti minggu itu; satu contoh baik, satu contoh lemah |
| 30–90 | **Studio** | Tim mengerjakan microtask sprint; dosen/mentor berkeliling; peer critique 15 menit terakhir |
| 90–100 | **Gate check** | Tiap tim melapor satu kalimat status, blocker, dan rencana sisa sprint |

Sisa pekerjaan sprint (±16 jam tim per minggu, lihat [OPS-02](../research-os/06-execution-os/02-weekly-sprints.md)) dikerjakan di luar kelas mengikuti halaman mingguan.

## 5. Peta 16 minggu

Sprint S0 (onboarding, sebelum W1) tidak punya halaman mingguan: akun GitHub, tim 1–3 orang, repositori dari TPL-15, `docs/team.md`, AI Usage Log entri pertama — rinciannya di [OPS-02 §S0](../research-os/06-execution-os/02-weekly-sprints.md).

| Week | Tema | Sprint | Gate | Deliverable utama | Halaman |
|---|---|---|---|---|---|
| W1 | Endgame | S1 | G1 | `docs/endgame.md`, Issue `type:problem`, One-Pager v0 (parsial), PR G1 | [week-01-endgame.md](weeks/week-01-endgame.md) |
| W2 | Problem | S2 | G2 | `docs/problem.md` (Problem Brief + Stakeholder/Impact), One-Pager v0, Research ID resmi, release v0.1 | [week-02-problem.md](weeks/week-02-problem.md) |
| W3 | Search | S3 | G3 | Search strategy, search log, screening, `references.bib` terverifikasi | [week-03-search.md](weeks/week-03-search.md) |
| W4 | Evidence | S4 | G3 | Synthesis matrix 15–25 sumber, daftar metrik/baseline lazim | [week-04-evidence.md](weeks/week-04-evidence.md) |
| W5 | Gap | S5 | G3 | `docs/literature-map.md` (pola + kandidat gap), PR G3, release v0.2 | [week-05-gap.md](weeks/week-05-gap.md) |
| W6 | RQ | S6 | G4 | `docs/research-question.md` (gap final, RQ, contribution), One-Pager v1, PR G4 | [week-06-rq.md](weeks/week-06-rq.md) |
| W7 | Method | S7 | G5 | Research Design Card, Data Plan, baseline & metrik terkunci, dataset card, Threats to Validity v1 | [week-07-method.md](weeks/week-07-method.md) |
| W8 | Design Defense | S8 | G5 | `docs/ethics.md`, Experiment Card pilot, pitch, notulen red team, PR G5, release v0.3 | [week-08-design-defense.md](weeks/week-08-design-defense.md) |
| W9 | Repository | S9 | G6 | Environment + seed, `src/`, `run.sh`, `experiments/README.md` v0 | [week-09-repository.md](weeks/week-09-repository.md) |
| W10 | Pilot | S10 | G6 | Hasil pilot di `results/`, catatan reproduksi peer, PR G6, release v0.5 | [week-10-pilot.md](weeks/week-10-pilot.md) |
| W11 | Analysis | S11 | G7 | `results/analysis.md` v0, figur jujur, ketidakpastian antar seed | [week-11-analysis.md](weeks/week-11-analysis.md) |
| W12 | Contribution | S12 | G7 | Tabel CER, Threats to Validity v2, Contribution Statement v2, One-Pager v2, PR G7 | [week-12-contribution.md](weeks/week-12-contribution.md) |
| W13 | Manuscript | S13 | G8 | Proposal TA / manuscript draft, AI Usage Statement, indeks Research Pack, release v0.8 | [week-13-manuscript.md](weeks/week-13-manuscript.md) |
| W14 | Peer Review | S14 | G8 | 2 review untuk tim lain, response to reviewers, PR G8 dibuka | [week-14-peer-review.md](weeks/week-14-peer-review.md) |
| W15 | Revision | S15 | G8 | Proposal v0.9, Research Integrity Checklist ditandatangani, rehearsal | [week-15-revision.md](weeks/week-15-revision.md) |
| W16 | Defense | S16 | G8 | Research Defense, handoff, PR G8 merge, release v1.0 Research Pack | [week-16-defense.md](weeks/week-16-defense.md) |

Sprint terberat: S4 (bacaan), S9 (coding), S11 (eksperimen penuh + analisis). Mulai task kritisnya di hari pertama.

## 6. Delapan gate

Gate menjawab *apakah sesuatu layak dilanjutkan*, bukan *kapan dikumpulkan*. Gate berurutan; direview lewat PR `GATE REVIEW: <Nama Gate>`; merge = lulus. Versi mahasiswa lengkap (bukti wajib, reviewer, PR template, alur 6 langkah) ada di [research-gates/README.md](research-gates/README.md); definisi resmi di [OPS-03](../research-os/06-execution-os/03-research-gates.md).

| Gate | Minggu | Satu kalimat yang harus bisa diucapkan tim |
|---|---|---|
| G1 Endgame Ready | W1 | "Riset ini menuju ___ lewat pintu ___." |
| G2 Problem Ready | W2 | "Masalahnya adalah ___, penting bagi ___ karena ___." |
| G3 Evidence Ready | W3–W5 | "Literatur sudah menunjukkan ___, tetapi bertentangan/kosong pada ___." |
| G4 Question Ready | W6 | "Maka kami bertanya ___ dan akan berkontribusi ___." |
| G5 Method Ready | W7–W8 | "Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___." |
| G6 Experiment Ready | W9–W10 | "Pilot kami berjalan; orang lain sudah mereproduksinya." |
| G7 Claim Ready | W11–W12 | "Bukti mendukung klaim ___ dan tidak mendukung ___." |
| G8 Contribution Ready | W13–W16 | "Research Pack lengkap; TA/paper dapat dimulai dari sini." |

## 7. Cara memakai halaman mingguan

Setiap halaman di `weeks/` memakai enam bagian tetap ([OPS-05](../research-os/06-execution-os/05-student-weekly-playbook.md)): **This Week** (satu kalimat outcome) · **Tasks** (5–10 task — umumnya 7–10 — dengan Task ID `OPS-NNN` dan effort) · **Deliverable** (apa yang harus ada di repositori hari Jumat) · **AI Assist** (AI boleh untuk apa, tidak boleh untuk apa) · **Human Check** (apa yang wajib diverifikasi manusia) · **Done When** (ya/tidak).

**Senin, 10 menit (sprint planning)**
1. Buka halaman minggu ini; baca *This Week* keras-keras dalam tim.
2. Tandai task yang sudah boleh dimulai (dependency-nya selesai minggu lalu); bagi antar anggota — maksimal 2 task berjalan per orang.
3. Lihat *Deliverable*; buat file kosongnya sekarang bila belum ada.
4. Baca *AI Assist* dan *Human Check* sekali: itu kontrak minggu ini.

**Selama minggu**: setiap commit menyebut Task ID (`Add search strategy v1 (OPS-026)`); setiap pemakaian AI yang material dicatat di AI Usage Log `docs/AI-USAGE.md` **saat itu juga**; task selesai hanya bila bukti ada di repositori dan Human Check sudah dilakukan.

**Jumat, 15 menit (gate check)**
1. Buka *Done When*; jawab ya/tidak per butir. Jujur.
2. Pada minggu gate: pastikan PR `GATE REVIEW: …` sudah dibuka dan reviewer diminta.
3. Tulis jurnal mingguan `docs/journal/wNN.md`: apa yang dipelajari, apa yang masih ragu, apa yang dibawa ke minggu depan.
4. Task yang belum selesai **dibawa** ke minggu depan, bukan dihapus.

Tiga pertanyaan sebelum menutup laptop: *Apa buktinya? Apa yang bisa membuat ini salah? Bisakah orang lain memeriksanya?*

## 8. Research Pack: deliverable akhir

Research Pack adalah 16 artefak yang hidup di repositori riset dan dirilis sebagai `v1.0 Research Pack` — bukan `Proposal.pdf` tunggal ([MET-04](../research-os/04-metopen-research-studio/04-research-pack-specification.md)). Sifat wajib: **traceable** (RQ → gap → baris matriks; klaim → tabel), **inspectable** (orang luar bisa memeriksa), **honest** (hasil negatif dan penggunaan AI ditulis apa adanya).

| # | Artefak | Gate | # | Artefak | Gate |
|---|---|---|---|---|---|
| 1 | Problem Brief | G2 | 9 | Baseline & Metrics | G5 |
| 2 | Stakeholder / Impact Statement | G2 | 10 | Pilot Experiment | G6, G7 |
| 3 | Literature Evidence Map | G3 | 11 | Threats to Validity | G5, G7 |
| 4 | Research Gap | G3→G4 | 12 | Ethics & Privacy | G5, G8 |
| 5 | RQ / Hypothesis | G4 | 13 | AI Usage Statement | setiap gate, final G8 |
| 6 | Contribution Statement | G4, revisi G7 | 14 | Reproducibility README | G6, G8 |
| 7 | Research Design | G5 | 15 | Proposal TA | G8 |
| 8 | Dataset / Data Plan | G5 | 16 | Research Pitch | G5 (W8), G8 (W16) |

Release mengikuti gate: v0.1 Problem Validated → v0.2 Evidence Ready → v0.3 Research Design → v0.5 Pilot Experiment → v0.8 Manuscript Draft → **v1.0 Research Pack**. Setelah G8, Research Pack diwariskan ke TA lewat handoff (TPL-14): *what exists, missing evidence, next steps, owner*.

## 9. Penilaian: 5E + Research Integrity Gate

Tidak ada UTS/UAS tertulis. Nilai datang dari **artefak yang lolos gate** ([MET-06](../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md); versi mahasiswa di [rubrics/README.md](rubrics/README.md)).

| Komponen | Bobot | Isi |
|---|---|---|
| A. Milestone Portfolio (Research Pack) — rubrik 5E | 60% | End 10% · Evidence 15% · Experiment 15% · Explanation 10% · Execution 10% |
| B. Research Defense (W16) | 15% | Presentasi tim + tanya-jawab individu |
| C. Peer Review sebagai reviewer (W14) | 10% | Kualitas 2 review: spesifik, berbasis bukti, dapat ditindaklanjuti |
| D. Partisipasi Sprint (S0–S16) | 15% | Deliverable tepat waktu, gate check, AI Usage Log konsisten, kontribusi terlihat di git |
| **Research Integrity Gate** | **prasyarat** | Lulus/gagal di setiap gate: tidak ada fabrikasi, sitasi palsu, plagiarisme, AI tak diungkap |

**Proficient di semua E = TA Ready; Exemplary = jalur Research/Publication Ready.** Integritas bukan komponen nilai; ia syarat nilai.

## 10. Aturan AI

Kelas ini bukan *AI-free* dan bukan "pakai ChatGPT bikin proposal". Aturannya satu: **AI-augmented, human-accountable science** — AI adalah research copilot, bukan epistemic authority. Setiap penggunaan AI yang material mengikuti protokol ([AIX-04](../research-os/05-ai-augmented-research/04-ai-research-protocol.md); versi praktis di [ai-toolkit/README.md](ai-toolkit/README.md)):

```
Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own
```

Tiga larangan mutlak: (1) data pribadi/partner/RESTRICTED masuk ke layanan AI; (2) referensi, angka hasil, atau data yang dihasilkan AI tanpa verifikasi — diperlakukan sebagai fabrikasi; (3) teks/kode AI yang tidak diverifikasi dan tidak bisa Anda jelaskan. Penggunaan yang material dicatat di AI Usage Log (TPL-10) saat terjadi; penggunaan yang memengaruhi kesimpulan dan tidak diungkap membuat gate gagal. Target kompetensi: **AI Investigator dengan perilaku AI Governor** ([AIX-02](../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md)).

## 11. Cara memulai (5 langkah, Sprint S0)

1. **Baca protokol AI dan tanda tangani agreement.** Baca [AIX-04](../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (teks agreement di §5) dan [OPS-05](../research-os/06-execution-os/05-student-weekly-playbook.md); simpan agreement sebagai `docs/ai-protocol-agreement.md`.
2. **Pilih problem.** Telusuri [research backlog](../research-backlog/README.md) (bank masalah dengan Research ID), riset dosen, dataset di [datasets-registry](../datasets-registry/README.md), atau proyek mata kuliah Anda. Semua pintu masuk melewati gate yang sama.
3. **Bentuk tim 1–3 orang** (disarankan 2) dengan peran eksplisit: lead, data/experiment owner, documentation/reviewer owner. Tulis di `docs/team.md`.
4. **Buat repositori riset dari [TPL-15](../research-os/08-templates/15-research-repository-template.md)** (`proj-YYYY-topik`, visibilitas awal private): README riset, `docs/`, `data/README.md`, `src/`, `experiments/`, `results/`, `paper/`, `presentation/` (pohon lengkap di TPL-15). Mulai AI Usage Log `docs/AI-USAGE.md` dengan entri pertama (OPS-005/OPS-006, masih di S0 — pra-W1).
5. **Buka [Week 01 — Endgame](weeks/week-01-endgame.md)** pada Senin pertama dan ikuti ritme Senin 10 menit / Jumat 15 menit.

## 12. Struktur folder studio

```
metopen-research-studio/
├── README.md                 # halaman ini
├── weeks/                    # 16 halaman mingguan (This Week / Tasks / Deliverable / AI Assist / Human Check / Done When)
│   ├── week-01-endgame.md … week-16-defense.md
├── research-gates/README.md  # 8 gate versi mahasiswa: kalimat, bukti, reviewer, PR template, alur review
├── templates/README.md       # indeks 15 template TPL-01…TPL-15: dipakai minggu berapa, gate apa, disimpan di mana
├── rubrics/README.md         # rubrik 5E versi mahasiswa, integrity gate, skema nilai, remedial
├── examples/README.md        # contoh terisi riset ilustratif UIAI-2026-001
└── ai-toolkit/README.md      # protokol AI praktis, tabel minggu → AI boleh/verifikasi/tool, log & statement
```

Sumber tunggal desain tetap di [`research-os/04-metopen-research-studio/`](../research-os/04-metopen-research-studio/01-metopen-positioning.md) (MET-01…MET-07) dan [`research-os/06-execution-os/`](../research-os/06-execution-os/02-weekly-sprints.md) (OPS-01…OPS-05); folder ini tidak menduplikasinya, hanya menyajikannya per minggu.

## 13. Peran

| Peran | Yang dilakukan setiap minggu | Yang diputuskan |
|---|---|---|
| **Tim mahasiswa** (1–3) | Menjalankan task sprint, menaruh bukti di repositori, membuka PR gate, mencatat AI Usage Log, menulis jurnal | Isi riset: endgame, masalah, RQ, desain, klaim |
| **Dosen pengampu** | Concept 30 menit, berkeliling di studio, gate check; mereview semua PR gate | **Lulus/gagal gate**; nilai akhir; penyempitan ruang lingkup bila terlambat |
| **Mentor** (dosen klaster) | Menjawab "baris matriks mana yang membuat RQ ini perlu?", mengecek desain dan klaim; reviewer G4, G5, G7, G8 | Rekomendasi lulus; arah TA setelah handoff |
| **Peer / `@reviewers`** | Peer test dua kalimat (W2), cross-check matriks (W4), red team (W8), reproduksi baseline (W10), peer review manuscript (W14) memakai TPL-12 | Rekomendasi saja; komentar wajib berisi *apa yang kurang* dan *bukti apa yang dibutuhkan* |
| **Admin riset** | Memperbarui Mission Control dan leaderboard setiap Jumat setelah PR merge | — |

Kontribusi yang tidak terlihat di git, Issue, log, atau notulen dianggap tidak ada — itu bagian dari pelajaran *inspectable research*.

## 14. Tautan lanjut

- Panduan mahasiswa lengkap (berlaku juga untuk TA dan proyek mata kuliah): [research-based-learning/student-guide](../research-based-learning/student-guide/README.md)
- Halaman mata kuliah dalam pipeline research-based learning: [courses/research-methods](../research-based-learning/courses/research-methods/README.md)
- Desain akademik Metopen (View A): [research-os/04-metopen-research-studio](../research-os/04-metopen-research-studio/01-metopen-positioning.md) — MET-01 positioning, MET-02 CPMK, MET-03 blueprint, MET-04 Research Pack, MET-05 publication backward design, MET-06 rubrik, MET-07 integritas & etika
- Cara membuka Issue dan PR gate: [CONTRIBUTING.md](../CONTRIBUTING.md) · kamus istilah: [MST-03 Glossary](../research-os/00-master/03-glossary.md)
