# Research Gates — Delapan Gerbang, Versi Mahasiswa

> **Status** Draft v0.1 (2026-09) · Versi ringkas untuk tim mahasiswa; definisi resmi (definition of done lengkap, kriteria lulus/gagal) ada di [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md)
> **Terkait** [Studio README](../README.md) · [MST-03 Glossary §3](../../research-os/00-master/03-glossary.md) · [CONTRIBUTING.md §3](../../CONTRIBUTING.md) · [TPL-12 Peer Review](../../research-os/08-templates/12-peer-review-template.md) · [rubrics](../rubrics/README.md)

Deadline menjawab *kapan* sesuatu dikumpulkan. Gate menjawab *apakah sesuatu layak dilanjutkan*. Delapan gate ini berurutan: G(n+1) tidak dibuka sebelum G(n) lulus. Setiap gate direview lewat Pull Request `GATE REVIEW: <Nama Gate> — UIAI-YYYY-NNN` dari branch `research/gN-<slug>`; **merge = lulus**. Satu pelanggaran integritas (fabrikasi, sitasi palsu, AI tidak diungkap) membuat gate gagal terlepas dari kualitas lainnya.

## 1. Tabel delapan gate

| Gate | Minggu · Sprint | Satu kalimat yang harus bisa diucapkan tim | Bukti wajib (ringkas) | Reviewer | PR template | Release |
|---|---|---|---|---|---|---|
| **G1 Endgame Ready** | W1 · S1 | "Riset ini menuju ___ lewat pintu ___." | `docs/endgame.md` (minimum TA Ready / target Research Ready / aspirasi), repositori dari TPL-15, Issue `type:problem` dengan ID sementara `UIAI-YYYY-TBD`, agreement AI Research Protocol, AI Usage Log `docs/AI-USAGE.md` (dimulai saat onboarding S0, pra-W1) | Dosen pengampu | [default](../../.github/PULL_REQUEST_TEMPLATE.md) | — |
| **G2 Problem Ready** | W2 · S2 | "Masalahnya adalah ___, penting bagi ___ karena ___." | `docs/problem.md` (Problem Brief problem-first + Stakeholder & Impact), One-Pager v0, Issue backlog diperbarui + permohonan Research ID; ID resmi `UIAI-YYYY-NNN` ditetapkan `@maintainers` saat PR di-merge (lalu judul Issue dan README riset diperbarui) | Dosen + 1 peer | [problem-review.md](../../.github/PULL_REQUEST_TEMPLATE/problem-review.md) | v0.1 Problem Validated |
| **G3 Evidence Ready** | W3–W5 · S3–S5 | "Literatur sudah menunjukkan ___, tetapi bertentangan/kosong pada ___." | Search strategy, synthesis matrix 15–25 sumber primer yang dibaca, `docs/literature-map.md` (pola + gap kandidat), `references.bib` 100% DOI/URL terverifikasi, AI Usage Log verifikasi sumber | Dosen + peer; mentor bila ada | [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) | v0.2 Evidence Ready |
| **G4 Question Ready** | W6 · S6 | "Maka kami bertanya ___ dan akan berkontribusi ___." | `docs/research-question.md` (gap final dengan Gap–Claim–Evidence alignment, 1–3 RQ/hipotesis falsifiable, Contribution Statement), One-Pager v1, Issue `type:research-question` | Dosen + mentor | [default](../../.github/PULL_REQUEST_TEMPLATE.md) | — |
| **G5 Method Ready** | W7–W8 · S7–S8 | "Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___." | `docs/research-design.md` + Design Card `docs/design-card.md` (TPL-08), Data Plan `docs/data-plan.md` + dataset card, baseline & metrik terkunci, Experiment Card pilot `experiments/pilot-01/experiment-card.md` (TPL-09), Threats to Validity v1, `docs/ethics.md`, slide pitch W8 (7–10 menit), notulen red team `docs/reviews/midterm-red-team.md` | Dosen, mentor, red team (peer + dosen lain) | [method-review.md](../../.github/PULL_REQUEST_TEMPLATE/method-review.md) | v0.3 Research Design |
| **G6 Experiment Ready** | W9–W10 · S9–S10 | "Pilot kami berjalan; orang lain sudah mereproduksinya." | `src/`, `experiments/` (config, seed, environment), `run.sh`, `experiments/README.md`, hasil pilot di `results/` (baseline + ≥1 pembanding), catatan reproduksi peer, AI Usage Log kode berbantuan AI | Dosen + peer reproducer | [experiment-review.md](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md) | v0.5 Pilot Experiment |
| **G7 Claim Ready** | W11–W12 · S11–S12 | "Bukti mendukung klaim ___ dan tidak mendukung ___." | `results/analysis.md` (hasil vs baseline, variansi antar seed, error analysis), figur final jujur, tabel Claim–Evidence–Reasoning per RQ, Threats to Validity v2 (pasca-hasil, di `results/analysis.md`), Contribution Statement v2, One-Pager v2 | Dosen + mentor | [default](../../.github/PULL_REQUEST_TEMPLATE.md) | — |
| **G8 Contribution Ready** | W13–W16 · S13–S16 | "Research Pack lengkap; TA/paper dapat dimulai dari sini." | Research Pack 16 artefak (MET-04), proposal TA / manuscript, AI Usage Statement, peer review + response, Research Integrity Checklist (TPL-11) ditandatangani, defense 7–10 menit + notulen, handoff (TPL-14) | Dosen, mentor, penguji defense; peer reviewer manuscript | [manuscript-review.md](../../.github/PULL_REQUEST_TEMPLATE/manuscript-review.md) | v0.8 Manuscript Draft → v1.0 Research Pack |

Setelah G8, rilis artefak/dataset/publikasi (v1.1 Submitted, v2.0 Published) memakai [release-review.md](../../.github/PULL_REQUEST_TEMPLATE/release-review.md). Status kematangan yang diperoleh: lolos **G5 = TA Ready**, lolos **G6–G7 = Research Ready**, lolos **G8 + manuscript-ready = Publication Ready**.

## 2. Alur PR gate review: enam langkah

1. **Cek *Done When* dulu.** Buka halaman minggu gate di [`weeks/`](../weeks/week-01-endgame.md) dan jawab setiap butir *Done When* ya/tidak. Semua bukti wajib harus **ada di repositori** (file, commit, Issue), bukan di laptop atau di percakapan AI. Bandingkan dengan definition of done gate di [OPS-03](../../research-os/06-execution-os/03-research-gates.md).
2. **Bekerja di branch gate.** `research/g2-problem`, `research/g3-evidence`, `research/g4-question`, `research/g5-method`, `research/g6-experiment`, `research/g7-claim`, `research/g8-contribution` (G1: `research/g1-endgame`). Setiap commit menyebut Task ID dan Research ID: `Add synthesis matrix v1 (UIAI-2026-001, OPS-035)`.
3. **Buka PR** berjudul `GATE REVIEW: <Nama Gate> — UIAI-YYYY-NNN` (untuk G1 dan G2 pakai ID sementara `UIAI-YYYY-TBD`; ID resmi ditetapkan saat PR G2 di-merge) memakai template sesuai tabel (tambahkan `?template=<nama>.md` pada URL *Compare & pull request*, atau salin isinya dari `.github/PULL_REQUEST_TEMPLATE/`). Isi **semua** field: RQ, method, dataset, baseline, metrics, threats to validity, evidence (tabel bukti wajib dengan path/link), AI usage. Field yang belum relevan ditulis "belum ditetapkan — tahap evidence", bukan dikosongkan.
4. **Minta reviewer** sesuai gate: dosen pengampu selalu; peer/`@reviewers` untuk G2, G3, G6 (reproducer), G8; mentor untuk G4, G5, G7, G8; red team untuk G5. Peer dan mentor mengisi [TPL-12](../../research-os/08-templates/12-peer-review-template.md): skor per dimensi **plus** komentar *apa yang kurang* dan *bukti apa yang dibutuhkan*. Bagian integritas dicentang reviewer di setiap gate.
5. **Tanggapi review.** Tulis *response letter* di PR: terima / ubah / tolak dengan alasan untuk setiap komentar. Perbaiki hanya yang diminta; angka yang berubah harus berasal dari run baru yang ter-commit. Komentar review tidak pernah dihapus — ia bukti proses ilmiah. Minta review ulang.
6. **Merge = gate lulus.** Setelah merge: perbarui label Issue `gate:GN-…`, field Research Gate di Mission Control, bagian *Current Research Gate* di README riset; buat release sesuai milestone (`v0.1` … `v1.0`); tutup Issue yang selesai; buka halaman minggu berikutnya.

## 2a. Checklist sebelum meminta review

Jawab semuanya "ya" sebelum menekan *Request review*:

- [ ] Judul PR `GATE REVIEW: <Nama Gate> — UIAI-YYYY-NNN` (G1–G2: `UIAI-YYYY-TBD`); branch `research/gN-<slug>`; PR gate sebelumnya sudah merge dan nomornya dicantumkan.
- [ ] Tabel *Evidence* di PR berisi **setiap** bukti wajib gate ini dengan path/link yang bisa dibuka reviewer.
- [ ] Angka apa pun di PR berasal dari `results/` yang ter-commit (config + seed + log), bukan diketik dari ingatan atau dari AI.
- [ ] Setiap referensi yang disebut ada di `references.bib` dan DOI/URL-nya sudah dibuka oleh anggota tim.
- [ ] AI Usage Log `docs/AI-USAGE.md` mutakhir sampai hari ini; bagian *AI Usage* di PR merujuk nomor entri log.
- [ ] Tidak ada data mentah, data pribadi, atau kredensial di riwayat git ([SECURITY.md](../../SECURITY.md)).
- [ ] Setiap anggota tim bisa menjelaskan setiap bagian PR tanpa membuka AI.
- [ ] Kalimat gate (§1) bisa diucapkan dengan semua "___" terisi dan masing-masing menunjuk file di repositori.

## 2b. Apa yang dicari reviewer di tiap gate

| Gate | Pertanyaan pertama reviewer | Tanda cepat gagal |
|---|---|---|
| G1 | "Klaim pengetahuan apa yang mau dibuktikan, bukan aplikasi apa yang mau dibuat?" | Endgame hanya "membuat aplikasi X" |
| G2 | "Bisakah saya mengulang masalah dan siapa yang peduli dalam dua kalimat?" | Nama algoritma muncul di paragraf pertama Problem Brief |
| G3 | "Buka tiga DOI acak; apakah baris matriksnya cocok dengan paper?" | Satu referensi tidak bisa dibuka; matriks berupa ringkasan per paper |
| G4 | "Baris matriks mana yang membuat RQ ini perlu, dan hasil apa yang membatalkannya?" | Gap "belum ada yang meneliti di UAI"; RQ tidak bisa salah |
| G5 | "Bisakah orang lain menjalankan desain ini tanpa bertanya ke tim?" | Metrik/baseline belum ditetapkan; threats generik |
| G6 | "Bisakah peer mereproduksi angka baseline sekarang dari repositori?" | Hasil hanya di laptop; tidak ada seed/config |
| G7 | "Klaim ini menunjuk tabel/figur mana, dan apa yang tidak boleh diklaim?" | Klaim kausal dari korelasi; improvement tanpa baseline |
| G8 | "Bisakah pembimbing TA mulai dari Research Pack ini tanpa mengulang dari nol?" | Komponen Research Pack kosong; checklist integritas belum ditandatangani |

## 3. Jika gagal gate

Gagal gate **bukan hukuman** dan bukan hal langka. Yang terjadi:

| Situasi | Yang dilakukan |
|---|---|
| Reviewer menandai *Developing* / meminta revisi | Reviewer wajib menuliskan *apa yang kurang* dan *bukti apa yang dibutuhkan*. Itu peta perbaikan Anda: perbaiki hanya itu, lalu buka review ulang. Maksimal dua review ulang per gate; lebih dari itu dosen memutuskan apakah ruang lingkup riset dikecilkan. |
| Bukti belum ada di repositori | PR tidak dapat direview. Commit dulu, tautkan, baru minta review. |
| Pelanggaran integritas (referensi tidak bisa dibuka, angka tanpa run, AI tidak diungkap, data pribadi di repo) | Gate gagal terlepas dari level 5E. Kesalahan tidak disengaja diperbaiki dalam satu sprint dan dicatat (di AI Usage Log sebagai "ditemukan & dikoreksi"); pelanggaran disengaja ditangani sesuai [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) dan [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md). |
| Terlambat satu sprint | Task dibawa ke minggu berikutnya; gate tetap berurutan. Prioritas: (1) task critical path, (2) task PR gate, (3) AI Usage Log. Beri tahu dosen di Senin berikutnya, bukan di minggu gate ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md)). |
| Batas keras terlewat | G5 paling lambat W9, G6 paling lambat W11, G8 di W16. Tim yang belum G5 pada W9 mendapat konsultasi wajib dan penyempitan ruang lingkup. |

Nilai 5E dinilai pada **versi yang lulus** (kualitas), tanpa potongan; keterlambatan tercatat di E5 Execution dan komponen Partisipasi Sprint ([rubrics](../rubrics/README.md)). RQ tidak dianggap sah sebelum G3 lulus; eksperimen tidak boleh dimulai sebelum baseline dan metrik terkunci di G5.

## 4. Pengingat satu baris

Bukti yang tidak dapat diperiksa reviewer sama dengan tidak ada. Sebelum membuka PR gate, tanyakan pada diri sendiri kalimat gate di tabel §1 — bila ada bagian "___" yang belum bisa Anda isi dengan menunjuk file di repositori, Anda belum siap.
