# CPL → CPMK → Artifact → Evidence — Kerangka Penyelarasan untuk Revisi RPS

> **ID** ARC-05 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu yang merevisi RPS, tim kurikulum, koordinator MK, tim penjaminan mutu, tim PP-PTS
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [ARC-02 Curriculum Research Map](02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](03-ai-contribution-modes.md) · [ARC-06 Research Output Taxonomy](06-research-output-taxonomy.md) · [MET-02 Metopen Course Outcomes](../04-metopen-research-studio/02-metopen-course-outcomes.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [STR-04 Alignment Map](../01-strategic-foundation/04-alignment-map.md) · [GOV-05 PP-PTS Evidence](../07-governance/05-ppts-and-institutional-evidence.md)

## 1. Rantai enam tautan

Outcome-Based Education (OBE) menuntut setiap mata kuliah menunjukkan bahwa **capaian** benar-benar **dicapai** dan **dibuktikan**. Dalam praktik, rantai itu sering putus di tengah: CPL ditulis, CPMK ditulis, tetapi assessment-nya ujian tulis yang tidak menghasilkan apa pun yang bisa diperiksa orang lain. Kerangka ini menambah dua tautan yang membuat rantai itu bisa diaudit: **Research Artifact** dan **Evidence**.

```
 CPL ──► CPMK ──► Learning Activity ──► Assessment ──► Research Artifact ──► Evidence
 (lulusan   (MK bisa    (mahasiswa      (dinilai       (benda nyata yang     (jejak yang bisa
  bisa apa)  apa)        melakukan apa)  dengan apa)    dihasilkan)           diaudit: repo,
                                                                              Issue, PR, registry)
```

| Tautan | Definisi | Pertanyaan pemandu | Sumber |
|---|---|---|---|
| **CPL** | Capaian Pembelajaran Lulusan — kompetensi lulusan Prodi | "Lulusan Informatika UAI harus bisa apa?" | Dokumen kurikulum Prodi (`[isi]`) |
| **CPMK** | Capaian Pembelajaran Mata Kuliah — kontribusi MK ini terhadap CPL | "Setelah MK ini, mahasiswa bisa apa yang sebelumnya tidak bisa?" | RPS; untuk Metopen: [MET-02](../04-metopen-research-studio/02-metopen-course-outcomes.md) |
| **Learning Activity** | Aktivitas yang membuat CPMK terjadi | "Mahasiswa *melakukan* apa, pada minggu ke berapa?" | RPS; untuk Metopen: W1–W16 ([MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)) |
| **Assessment** | Cara menilai bahwa CPMK tercapai | "Dinilai dengan instrumen apa, rubrik apa, bobot berapa?" | Rubrik MK; untuk Metopen: 5E + Research Integrity Gate ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)) |
| **Research Artifact** | Benda nyata yang dihasilkan aktivitas dan dinilai assessment | "Apa yang tersisa setelah semester berakhir dan bisa dipakai orang lain?" | [ARC-06](06-research-output-taxonomy.md), paket 08 |
| **Evidence** | Jejak terverifikasi bahwa artefak ada dan memenuhi kriteria | "Kalau auditor/asesor bertanya, kita tunjukkan apa?" | Repositori, Issue, PR gate review, release, registry, AI Usage Log |

Aturan emas: **setiap CPMK harus berujung pada minimal satu artefak dan satu evidence yang dapat ditunjukkan tanpa bertanya kepada mahasiswa.** CPMK yang tidak punya artefak biasanya CPMK yang tidak benar-benar dinilai.

## 2. Mengapa Research Artifact dan Evidence dipisah

- **Artifact** adalah hasil kerja: Experiment Card, synthesis matrix, repositori, manuscript.
- **Evidence** adalah bukti bahwa artifact itu ada, milik siapa, kapan dibuat, dan lolos review apa: URL commit, PR `GATE REVIEW` yang di-merge, release `v1.0`, entri registry, AI Usage Log.

Pemisahan ini yang membuat kerangka berguna untuk tiga audiens sekaligus: dosen (menilai artifact), tim mutu/akreditasi (mengaudit evidence), dan pusat riset (memakai ulang artifact). Untuk pelaporan PP-PTS, kolom Evidence langsung menjadi lampiran ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)).

## 3. Cara memakai kerangka ini untuk revisi RPS

Kerjakan **satu CPMK dalam satu baris**. Jangan merevisi seluruh RPS sekaligus; mulai dari satu–tiga CPMK yang paling dekat dengan proyek yang sudah ada.

1. **Salin CPL** yang relevan dari dokumen kurikulum Prodi ke kolom CPL. Bila belum tersedia, tulis `CPL-x: [isi sesuai dokumen kurikulum Prodi]` — jangan mengarang CPL.
2. **Tulis/pertajam CPMK** dengan kata kerja yang menghasilkan benda: *merumuskan, memetakan, merancang, menjalankan, menganalisis, mempertahankan, mendokumentasikan*. Hindari *memahami, mengetahui* — tidak ada artifact-nya.
3. **Tentukan learning activity** yang sudah ada di RPS (atau arahkan tugas yang ada); sebut minggunya.
4. **Tentukan assessment**: instrumen, rubrik, bobot. Untuk MK mode E/R, masukkan minimal tiga kriteria riset ([ARC-03 §4](03-ai-contribution-modes.md)); untuk Metopen, pakai dimensi 5E.
5. **Tentukan research artifact** dari taksonomi [ARC-06](06-research-output-taxonomy.md) atau template paket 08.
6. **Tentukan evidence**: di mana artifact itu bisa ditemukan dan diverifikasi (path repositori, jenis Issue/PR, registry, release).
7. **Periksa rantai**: bila ada sel kosong, baris itu belum selesai. Bila artifact tidak pernah dipakai ulang siapa pun, pertimbangkan apakah CPMK-nya perlu.
8. Simpan baris ke `research-based-learning/courses/<mk>/research-artifact.md`; RPS resmi diturunkan dari sana.

## 4. Contoh terisi — Metodologi Penelitian (mode R)

CPMK konseptual mengikuti dokumen sumber dan [MET-02](../04-metopen-research-studio/02-metopen-course-outcomes.md). CPL ditulis generik karena CPL resmi tidak ada dalam dokumen sumber.

| # | CPL | CPMK | Learning Activity (minggu) | Assessment | Research Artifact | Evidence |
|---|---|---|---|---|---|---|
| 1 | CPL-x: [isi] | **Problem formulation** — merumuskan masalah nyata secara problem-first, lengkap dengan stakeholder dan dampak keputusan | W1 Endgame, W2 Problem: studio problem discovery, wawancara stakeholder ringan | 5E **End**; peer check "dua kalimat" | Problem Brief + Stakeholder/Impact Statement; Research One-Pager v0 ([TPL-01](../08-templates/01-research-one-pager-template.md)) | `docs/endgame.md`, `docs/problem.md`; PR `GATE REVIEW: Endgame Ready` (G1) dan `GATE REVIEW: Problem Ready` (G2) merged; Issue `type:problem` dengan Research ID |
| 2 | CPL-x: [isi] | **Evidence discovery** — merancang dan menjalankan strategi pencarian literatur (basis data, kata kunci, citation chaining, kriteria inklusi) | W3 Search: lab pencarian; AI untuk kandidat keyword dengan verifikasi | 5E **Evidence** (strategi) | Search log + kriteria inklusi/eksklusi; `references.bib` awal | `docs/literature/search-strategy.md` + `docs/literature/search-log.csv`; AI Usage Log entri pencarian |
| 3 | CPL-x: [isi] | **Synthesis** — menyintesis 15–25 sumber primer dalam synthesis matrix, bukan ringkasan satu per satu | W4 Evidence: studio synthesis matrix | 5E **Evidence** (kualitas matriks) | Literature Evidence Map + synthesis matrix (tabel/CSV) | PR `GATE REVIEW: Evidence Ready` (G3) merged; semua DOI terverifikasi |
| 4 | CPL-x: [isi] | **Gap** — menurunkan research gap langsung dari synthesis matrix (Gap–Claim–Evidence alignment) | W5 Gap: studio gap analysis | 5E **Evidence**/**End** | Research Gap statement yang menunjuk baris matriks | Gap Candidates di `docs/literature-map.md` (W5, bukti G3) → Research Gap final di `docs/research-question.md` (W6, dinilai G4); Issue `type:literature-gap` |
| 5 | CPL-x: [isi] | **RQ** — merumuskan RQ spesifik yang dapat dijawab dalam batas semester + TA | W6 RQ: studio RQ + Contribution Statement | 5E **End** | RQ + Contribution Statement; One-Pager v1 | PR `GATE REVIEW: Question Ready` (G4) merged; Issue `type:research-question` |
| 6 | CPL-x: [isi] | **Hypothesis** — menyatakan hipotesis yang dapat difalsifikasi beserta apa yang akan membantahnya | W6 RQ (lanjutan) | 5E **End** | Hypothesis + kondisi falsifikasi dalam One-Pager | `docs/research-question.md` bagian hipotesis |
| 7 | CPL-x: [isi] | **Methods** — memilih metode dari Computing Research Methods Map dan menjustifikasinya | W7 Method: studio design card | 5E **Experiment** (desain) | Research Design Card ([TPL-08](../08-templates/08-research-design-card.md)); Data Plan; Baseline & Metrics | `docs/research-design.md`, `docs/design-card.md`, `docs/data-plan.md`; PR `GATE REVIEW: Method Ready` (G5) merged; kartu dataset bila data baru (`datasets-registry/`) |
| 8 | CPL-x: [isi] | **Experiment** — merancang dan menjalankan pilot/minimum viable experiment yang reproducible | W9 Repository, W10 Pilot | 5E **Experiment** (pilot) + **Execution** | Experiment Card ([TPL-09](../08-templates/09-experiment-card.md)); repositori dengan `src/`, `experiments/`, `results/` | PR `GATE REVIEW: Experiment Ready` (G6) merged; catatan reproduksi peer; release `v0.5` |
| 9 | CPL-x: [isi] | **Validity** — mengidentifikasi threats to validity (internal, eksternal, konstruk, statistik) dan membatasi klaim sesuai bukti | W8 Design Defense (awal), W11 Analysis, W12 Contribution | 5E **Explanation** | Threats to Validity section; tabel Claim–Evidence–Reasoning | `results/analysis.md`; PR `GATE REVIEW: Claim Ready` (G7) merged; notulen red team W8 |
| 10 | CPL-x: [isi] | **AI-assisted research** — memakai AI sebagai research copilot sesuai protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own | Lintas minggu; sesi khusus W3, W9 | 5E **Execution**; kriteria disclosure | AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)); AI Usage Statement | `docs/AI-USAGE.md`; log dengan verifikasi per entri |
| 11 | CPL-x: [isi] | **Research integrity** — menjalankan riset dengan amanah epistemik: tanpa fabrikasi, falsifikasi, plagiarisme, sitasi palsu, AI tak diungkap | Lintas minggu; sesi etika & privasi W7 | **Research Integrity Gate** (lulus/gagal, bukan skor) | Ethics & Privacy section; Research Integrity Checklist ([TPL-11](../08-templates/11-research-integrity-checklist.md)) | `docs/ethics.md`; checklist ditandatangani sebelum defense |
| 12 | CPL-x: [isi] | **Writing** — menulis argumentasi ilmiah claim–evidence–reasoning dalam manuscript/proposal dan merevisinya berdasarkan peer review | W13 Manuscript, W14 Peer Review, W15 Revision | 5E **Explanation**; peer review ([TPL-12](../08-templates/12-peer-review-template.md)) | Proposal TA / manuscript draft; review yang ditulis mahasiswa untuk tim lain | `paper/proposal.md`; PR review comments; release `v0.8 Manuscript Draft` |
| 13 | CPL-x: [isi] | **Defense** — mempertahankan riset secara oral 7–10 menit dan menjawab kritik dengan merujuk bukti | W16 Defense | 5E semua dimensi; penguji | Research Pitch ([TPL-13](../08-templates/13-research-defense-template.md)); Research Pack lengkap | Rekaman/notulen defense; PR `GATE REVIEW: Contribution Ready` (G8) merged; release `v1.0 Research Pack`; handoff ([TPL-14](../08-templates/14-research-handoff-template.md)) |

Pengamatan: 13 CPMK → 8 PR gate review + 3 release + 1 checklist + 1 log. Semua evidence adalah objek GitHub yang bisa dihitung; itulah yang membuat KPI [GOV-03](../07-governance/03-kpi-and-measurement.md) dapat dihitung tanpa survei.

## 5. Contoh terisi — AI & Machine Learning (semester V, mode R)

Contoh untuk MK teknis: CPMK teknis yang sudah ada tetap; yang ditambahkan adalah lapisan riset pada proyek.

| # | CPL | CPMK | Learning Activity | Assessment | Research Artifact | Evidence |
|---|---|---|---|---|---|---|
| 1 | CPL-x: [isi] | Merumuskan pertanyaan kecil yang dapat diuji dari masalah backlog/dataset, bukan dari algoritma yang ingin dipakai | Pertemuan proyek 1: memilih masalah dari menu backlog; menulis "mengapa X perlu diprediksi" | Rubrik proyek — kriteria *problem-first* | Problem statement 1 halaman dalam repositori | `docs/problem.md`; tautan ke Issue backlog |
| 2 | CPL-x: [isi] | Menetapkan baseline paling sederhana dan metrik yang selaras tujuan **sebelum** melatih model | Pertemuan proyek 2: Experiment Card | Rubrik — kriteria *baseline & metrik ditetapkan lebih dulu* | Experiment Card v0 | Commit card sebelum commit model pertama (urutan commit adalah bukti) |
| 3 | CPL-x: [isi] | Menjalankan eksperimen dengan split yang mencegah leakage dan melaporkan variansi antar seed | Lab eksperimen | Rubrik — kriteria *leakage & variansi* | Skrip eksperimen + hasil per seed | `experiments/`, `results/`; README cara menjalankan |
| 4 | CPL-x: [isi] | Melakukan error analysis dan membatasi klaim sesuai bukti, termasuk melaporkan hasil negatif | Pertemuan analisis | Rubrik — *Explanation* ringan | Laporan hasil dengan CER + keterbatasan | `results/analysis.md` |
| 5 | CPL-x: [isi] | Membangun repositori yang dapat direproduksi peer | Lab reproducibility; peer swap | Peer reproduction (lulus/gagal) | Repositori dari [TPL-15](../08-templates/15-research-repository-template.md) | Catatan reproduksi peer di Issue/PR |
| 6 | CPL-x: [isi] | Mendokumentasikan penggunaan AI untuk kode/analisis secara jujur | Lintas minggu | Kriteria disclosure | AI Usage Log | `docs/AI-USAGE.md` |
| 7 | CPL-x: [isi] | Menyerahkan asset untuk dilanjutkan (handoff) | Pertemuan akhir | Kriteria handoff terisi | Handoff #1 ([TPL-14](../08-templates/14-research-handoff-template.md)) | `docs/handoff.md` (bagian Course → Metopen); daftar handoff di koordinator Metopen |

Untuk MK mode E, cukup baris 1, 2, 4, 6; untuk mode F, cukup satu–dua baris bernuansa evidence reasoning seperti contoh berikut.

## 5b. Contoh terisi — Statistika Terapan (semester II, mode F)

| # | CPL | CPMK | Learning Activity | Assessment | Research Artifact | Evidence |
|---|---|---|---|---|---|---|
| 1 | CPL-x: [isi] | Menafsirkan hasil analisis inferensial pada data nyata dan menyatakan secara eksplisit apa yang tidak boleh disimpulkan (korelasi ≠ kausalitas, generalisasi terbatas sampel) | Tugas analisis dataset publik/anonim (minggu 10–12) | Rubrik laporan: kriteria "batas kesimpulan" berbobot ≥ 20% | Laporan analisis + notebook yang dapat dijalankan ulang | Notebook dijalankan ulang oleh teman sekelas (peer check tercatat di laporan) |
| 2 | CPL-x: [isi] | Mereplikasi satu analisis dari paper/data terbuka dan menjelaskan perbedaan hasil | Tugas replikasi berpasangan (minggu 13–14) | Rubrik: kejujuran melaporkan perbedaan; bukan "hasil sama" | Notebook replikasi + catatan perbedaan | Repositori/folder tugas dengan data, kode, dan seed |

Dua baris ini tidak menambah materi Statistika Terapan; keduanya hanya mengarahkan tugas yang sudah ada agar menghasilkan kebiasaan Year 1 spiral ([ARC-01 §3](01-research-capability-spiral.md)).

## 6. Aturan kualitas baris

| Periksa | Lulus bila |
|---|---|
| Kata kerja CPMK | Menghasilkan benda yang bisa dinilai (bukan "memahami") |
| Aktivitas | Ada minggunya dan sudah/akan ada di RPS |
| Assessment | Ada instrumen, rubrik, bobot; untuk R ada Research Integrity check |
| Artifact | Ada di taksonomi/template; bisa dipakai ulang di luar kelas (untuk R) |
| Evidence | Bisa ditunjukkan tanpa bertanya ke mahasiswa; idealnya objek GitHub (commit, PR, release, Issue, registry) |
| Data | Tidak ada data sensitif dalam evidence publik ([SECURITY.md](../../SECURITY.md)) |
| Beban | Tidak menambah tugas baru bila tugas lama bisa diarahkan |

## 7. Hubungan dengan 5E dan Research Gates

Untuk Metopen, kolom Assessment memakai dimensi 5E dan kolom Evidence memakai gate: **End** ↔ G1–G2, **Evidence** ↔ G3–G4, **Experiment** ↔ G5–G6, **Explanation** ↔ G7, **Execution** ↔ disiplin sprint dan repositori lintas gate, **Research Integrity** ↔ gate lulus/gagal di setiap PR. Ini berarti nilai Metopen dapat direkonstruksi dari Mission Control dan riwayat PR — tidak ada penilaian yang tidak punya jejak.

Untuk MK lain, gate tidak formal, tetapi kolom Evidence tetap menunjuk pada objek yang bisa diperiksa (commit, catatan reproduksi, dataset card, Issue backlog).

## 8. Template kosong

Salin tabel di bawah ke `research-based-learning/courses/<mk>/research-artifact.md`. Satu baris per CPMK. Isi semua kolom; baris dengan sel kosong belum selesai.

**Mata kuliah:** [isi] · **Semester:** [isi] · **Mode (ARC-03):** F / E / R · **Klaster terkait (AIR-02):** C1 / C2 / C3 / C4 · **Dosen pengampu:** [isi] · **Versi RPS:** [isi]

| # | CPL | CPMK (kata kerja menghasilkan benda) | Learning Activity (minggu) | Assessment (instrumen, rubrik, bobot) | Research Artifact (ARC-06 / TPL) | Evidence (path/Issue/PR/release/registry) |
|---|---|---|---|---|---|---|
| 1 | CPL-x: [isi sesuai dokumen kurikulum Prodi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 2 | CPL-x: [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 3 | CPL-x: [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |

**Checklist sebelum menyerahkan:**

- [ ] Setiap CPMK punya minimal satu artifact dan satu evidence.
- [ ] Untuk mode E/R: rubrik memuat baseline/pembanding, metrik, keterbatasan.
- [ ] Untuk mode R: ada kriteria reproducibility, AI Usage Log, dan handoff.
- [ ] Evidence tidak memuat data sensitif.
- [ ] Baris disimpan di `research-based-learning/courses/<mk>/research-artifact.md` dan RPS diturunkan darinya.

## 9. Catatan

- CPL resmi Prodi tidak ada dalam dokumen sumber; semua `CPL-x` di dokumen ini adalah placeholder dan wajib diisi dari dokumen kurikulum Prodi sebelum RPS disahkan.
- Kerangka ini kompatibel dengan PjBL/Team-Based Project: *learning activity* adalah proyek tim, *artifact* adalah keluaran proyek, *evidence* adalah jejak repositori tim ([STR-04](../01-strategic-foundation/04-alignment-map.md)).
