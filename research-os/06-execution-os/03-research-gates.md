# Research Gates — Delapan Gerbang Kualitas Riset

> **ID** OPS-03 · **Paket** 06 Execution Operating System · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa, dosen pengampu, mentor riset, reviewer, TA supervisor
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [OPS-01 Research WBS](01-research-wbs-master.md) · [OPS-02 Weekly Sprints](02-weekly-sprints.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md)

## Mengapa gate, bukan sekadar deadline

Deadline menjawab *kapan* sesuatu dikumpulkan. Gate menjawab *apakah sesuatu layak dilanjutkan*. Riset yang lolos ke tahap eksperimen tanpa RQ yang tervalidasi akan menghasilkan angka yang tidak menjawab apa pun. Karena itu setiap riset di UAI AI Research Center melewati delapan gerbang berurutan, masing-masing dengan **definition of done**, **bukti wajib**, **reviewer**, dan **kriteria lulus/gagal** yang eksplisit.

Aturan umum:

1. Gate bersifat **berurutan**. G(n+1) tidak dapat dibuka sebelum G(n) lulus. Pengecualian hanya untuk riset lanjutan yang mewarisi gate dari handoff ([TPL-14](../08-templates/14-research-handoff-template.md)).
2. Gate direview lewat **Pull Request** bertajuk `GATE REVIEW: <nama gate>` dari branch `research/gN-<slug>` (lihat [CONTRIBUTING.md](../../CONTRIBUTING.md)). Merge = lulus.
3. Setiap gate memiliki **Research Integrity check**: satu saja pelanggaran integritas (fabrikasi, sitasi palsu, AI tidak diungkap) membuat gate gagal terlepas dari kualitas lainnya.
4. Gagal gate bukan hukuman. Reviewer wajib menuliskan *apa yang kurang* dan *bukti apa yang dibutuhkan*; tim merevisi dan membuka review ulang.
5. Status gate direkam di label Issue (`gate:G5-method`), field **Research Gate** di Mission Control, dan bagian **Current Research Gate** di README riset.

## Peta gate terhadap semester Metopen

| Gate | Minggu Metopen | Sprint | Release milestone |
|---|---|---|---|
| G1 Endgame Ready | W1 | S1 | — |
| G2 Problem Ready | W2 | S2 | v0.1 Problem Validated |
| G3 Evidence Ready | W3–W5 | S3–S5 | v0.2 Evidence Ready |
| G4 Question Ready | W6 | S6 | — |
| G5 Method Ready | W7–W8 (Design Defense) | S7–S8 | v0.3 Research Design |
| G6 Experiment Ready | W9–W10 | S9–S10 | v0.5 Pilot Experiment |
| G7 Claim Ready | W11–W12 | S11–S12 | — |
| G8 Contribution Ready | W13–W16 (Defense) | S13–S16 | v0.8 Manuscript Draft → v1.0 Research Pack |

Rincian task per gate ada di [OPS-01](01-research-wbs-master.md); urutan ketergantungan di [OPS-04](04-dependency-and-critical-path.md).

---

## G1 — Endgame Ready

**Pertanyaan:** Riset ini mau menjadi apa, untuk siapa, dan masuk lewat pintu mana?

**Definition of done**
- Tim (1–3 mahasiswa) terbentuk, akun GitHub dan repositori riset dibuat dari [TPL-15](../08-templates/15-research-repository-template.md).
- Endgame dinyatakan eksplisit: minimum **TA Ready**, target **Research Ready**, aspirasi (paper/dataset/artefak/HKI/produk) bila ada.
- Entry door dipilih (Problem / Dataset / Faculty Research / Course Project / Partner / Competition) dan kandidat dosen mentor diidentifikasi.
- Mahasiswa menandatangani **AI Research Protocol agreement** ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)) dan memulai AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)).

**Bukti wajib:** `docs/endgame.md` (atau bagian Endgame di Research One-Pager), repositori dengan struktur standar, Issue `type:problem` awal dengan Research ID sementara.

**Reviewer:** dosen pengampu Metopen.

**Lulus jika:** endgame spesifik dan realistis untuk 1 semester + TA; **gagal jika** endgame hanya "membuat aplikasi X" tanpa klaim pengetahuan yang ingin dibuktikan.

## G2 — Problem Ready

**Pertanyaan:** Apakah masalahnya nyata, penting, dan jelas siapa yang peduli?

**Definition of done**
- **Problem Brief**: fenomena/masalah nyata, konteks Indonesia/UAI, mengapa penting sekarang.
- **Stakeholder & impact statement**: siapa pemangku kepentingan, keputusan apa yang berubah bila riset berhasil.
- Masalah diformulasikan *problem-first*, bukan *solution-first* ("mengapa X perlu diprediksi?" sebelum "pakai Random Forest").
- Masalah selaras dengan salah satu klaster ([AIR-02](../03-ai-research-ecosystem/02-ai-research-clusters.md)) dan domain roadmap.

**Bukti wajib:** `docs/problem.md`, Research One-Pager v0 ([TPL-01](../08-templates/01-research-one-pager-template.md)), Issue backlog diperbarui, Research ID `UIAI-YYYY-NNN` resmi diberikan.

**Reviewer:** dosen pengampu + 1 peer reviewer.

**Lulus jika:** orang di luar tim dapat menjelaskan ulang masalah dan mengapa penting dalam dua kalimat; **gagal jika** masalah hanya justifikasi untuk algoritma yang sudah dipilih.

## G3 — Evidence Ready

**Pertanyaan:** Apa yang sudah diketahui dunia tentang masalah ini?

**Definition of done**
- Strategi pencarian terdokumentasi (kata kunci, basis data: Google Scholar/Scopus/Semantic Scholar, citation chaining, kriteria inklusi/eksklusi, kualitas sumber).
- **Literature Evidence Map**: minimal 15–25 sumber primer yang relevan dan benar-benar dibaca, dipetakan dalam **synthesis matrix** (bukan ringkasan satu per satu): problem, metode, data, metrik, hasil, keterbatasan, relevansi.
- Setiap sumber terverifikasi ada (DOI/URL), termasuk sumber yang ditemukan lewat AI.
- `references.bib` terkelola.

**Bukti wajib:** `docs/literature-map.md` + synthesis matrix (tabel/CSV), `references.bib`, AI Usage Log menunjukkan verifikasi sumber.

**Reviewer:** dosen pengampu + peer reviewer; mentor bila sudah ada.

**Lulus jika:** matriks menunjukkan pola (apa yang konsisten, apa yang bertentangan, apa yang belum diuji); **gagal jika** ada satu saja referensi yang tidak dapat diverifikasi keberadaannya.

## G4 — Question Ready

**Pertanyaan:** Apa yang belum diketahui, apa yang kita klaim, dan apa kontribusinya?

**Definition of done**
- **Research Gap** diturunkan langsung dari synthesis matrix (Gap–Claim–Evidence alignment).
- **RQ** (dan/atau hipotesis yang dapat difalsifikasi) yang spesifik, dapat dijawab dalam batas semester + TA.
- **Contribution Statement**: jenis kontribusi (empiris, artefak, metode, dataset, replikasi, studi kasus) dan mengapa bermakna.
- RQ tidak boleh dianggap valid sebelum evidence synthesis (G3) selesai.

**Bukti wajib:** `docs/research-question.md`, Research One-Pager v1, Issue `type:research-question`.

**Reviewer:** dosen pengampu + mentor.

**Lulus jika:** setiap RQ dapat ditelusuri ke baris tertentu di synthesis matrix; **gagal jika** gap hanya naratif ("belum ada yang meneliti di UAI").

## G5 — Method Ready

**Pertanyaan:** Bagaimana persisnya RQ akan dijawab, dan apa yang bisa membuat jawabannya salah?

**Definition of done**
- **Research Design Card** ([TPL-08](../08-templates/08-research-design-card.md)): jenis metode dari Computing Research Methods Map (experiment, benchmarking, design science, empirical SE study, ML research, simulation, survey, user study, case study, qualitative), variabel/konstruk, kontrol, sampling.
- **Dataset/Data Plan**: sumber, akses, lisensi, privasi, ukuran, representativitas; dicatat di datasets-registry bila baru.
- **Baseline & Metrics**: baseline paling sederhana, metrik yang selaras dengan RQ, prosedur evaluasi yang mencegah leakage.
- **Experiment Card** ([TPL-09](../08-templates/09-experiment-card.md)) untuk pilot.
- **Threats to Validity** awal (internal, eksternal, konstruk, statistik).
- **Ethics & Privacy** awal ([MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- Dipertahankan pada **Mid-semester Research Pitch / Red Team Review** (W8).

**Bukti wajib:** `docs/research-design.md`, design card, experiment card, `docs/ethics.md`, slide pitch, notulen red team.

**Reviewer:** dosen pengampu, mentor, red team (peer + dosen lain).

**Lulus jika:** orang lain dapat menjalankan desain ini tanpa bertanya ke tim; **gagal jika** metrik/baseline belum ditetapkan (eksperimen tidak boleh dimulai sebelum keduanya ada).

## G6 — Experiment Ready

**Pertanyaan:** Apakah desainnya viable dalam praktik, dan bisakah orang lain menjalankannya?

**Definition of done**
- Repositori berisi `src/`, `notebooks/`, `experiments/` dengan konfigurasi, seed, environment (`requirements.txt`/`environment.yml`), dan README cara menjalankan.
- **Pilot study / minimum viable experiment** dijalankan end-to-end pada subset data: baseline + minimal satu metode pembanding.
- Log eksperimen dan hasil awal tersimpan di `results/`; figur di `figures/`.
- Reproduksi oleh anggota lain/peer berhasil (minimal satu kali).

**Bukti wajib:** commit eksperimen, `experiments/README.md`, hasil pilot, catatan reproduksi peer, AI Usage Log untuk kode yang dibantu AI.

**Reviewer:** dosen pengampu + mentor + peer reproducer.

**Lulus jika:** peer dapat mereproduksi angka baseline dari repositori; **gagal jika** hasil hanya ada di laptop anggota tim.

## G7 — Claim Ready

**Pertanyaan:** Apa yang boleh kita klaim berdasarkan bukti ini, dan apa yang tidak?

**Definition of done**
- Analisis hasil: error analysis, perbandingan terhadap baseline, ketidakpastian (variansi antar seed/fold, interval bila relevan), *statistical thinking* secukupnya untuk mencegah klaim buruk.
- Visualisasi bukti yang jujur (skala, baseline terlihat, tidak cherry-picking).
- **Claim–Evidence–Reasoning** eksplisit untuk setiap RQ; hasil negatif dilaporkan.
- **Threats to Validity** diperbarui berdasarkan apa yang benar-benar terjadi.
- Contribution statement direvisi agar tidak melebihi bukti.

**Bukti wajib:** `results/analysis.md`, figur final, tabel CER, bagian threats to validity.

**Reviewer:** dosen pengampu + mentor.

**Lulus jika:** setiap klaim menunjuk ke tabel/figur tertentu; **gagal jika** ada klaim kausal dari korelasi atau improvement tanpa baseline.

## G8 — Contribution Ready

**Pertanyaan:** Apakah riset ini siap dipertanggungjawabkan dan diwariskan?

**Definition of done**
- **Research Pack** lengkap sesuai [MET-04](../04-metopen-research-studio/04-research-pack-specification.md), termasuk Proposal TA formal (atau manuscript bila endgame paper), AI Usage Statement, Reproducibility README, Ethics & Privacy.
- Lolos **peer review** ([TPL-12](../08-templates/12-peer-review-template.md)) dan revisi.
- **Research Defense** 7–10 menit ([TPL-13](../08-templates/13-research-defense-template.md)) lulus.
- **Research Integrity Checklist** ([TPL-11](../08-templates/11-research-integrity-checklist.md)) ditandatangani.
- **Handoff** ke TA/mentor/AI Center terisi ([TPL-14](../08-templates/14-research-handoff-template.md)); release `v1.0 Research Pack` dibuat.

**Bukti wajib:** release v1.0, dokumen proposal/manuscript, rekaman/notulen defense, checklist integritas, handoff.

**Reviewer:** dosen pengampu, mentor, penguji defense; peer reviewer untuk manuscript.

**Lulus jika:** dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol; **gagal jika** ada komponen Research Pack yang kosong atau integritas tidak lolos.

---

## Setelah G8

Riset yang lolos G8 masuk kolom **Published/Released** ketika menghasilkan publikasi (`PUB-YYYY-NNN`), dataset (`DS-YYYY-NNN`), artefak (`ART-YYYY-NNN`), atau HKI. Pipeline publikasi (manuscript-ready → submission-ready → submitted → accepted → published) dikelola di [MET-05](../04-metopen-research-studio/05-publication-backward-design.md) dan `publications/`.

## Ringkasan satu baris per gate

| Gate | Satu kalimat yang harus bisa diucapkan tim |
|---|---|
| G1 | "Riset ini menuju ___ lewat pintu ___." |
| G2 | "Masalahnya adalah ___, penting bagi ___ karena ___." |
| G3 | "Literatur sudah menunjukkan ___, tetapi bertentangan/kosong pada ___." |
| G4 | "Maka kami bertanya ___ dan akan berkontribusi ___." |
| G5 | "Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___." |
| G6 | "Pilot kami berjalan; orang lain sudah mereproduksinya." |
| G7 | "Bukti mendukung klaim ___ dan tidak mendukung ___." |
| G8 | "Research Pack lengkap; TA/paper dapat dimulai dari sini." |
