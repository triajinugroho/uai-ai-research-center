# Research Pack Specification — UAI Informatics Research Pack

> **ID** MET-04 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen pengampu, mentor, reviewer gate, dosen pembimbing TA
> **Terkait** [MET-03 16-Week Blueprint](03-metopen-16-week-blueprint.md) · [MET-06 5E Rubric](06-assessment-and-5e-rubric.md) · [MET-07 Integrity & Ethics](07-research-integrity-and-ethics.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [TPL-15 Research Repository Template](../08-templates/15-research-repository-template.md) · [TPL-14 Handoff](../08-templates/14-research-handoff-template.md) · [MST-03 Glossary](../00-master/03-glossary.md)

## 1. Apa itu Research Pack

**UAI Informatics Research Pack** adalah deliverable akhir Metopen: kumpulan 16 artefak yang, bila lengkap, membuat dosen pembimbing TA dapat memulai bimbingan tanpa mengulang dari nol, dan membuat orang lain dapat memeriksa serta mereproduksi apa yang sudah dikerjakan.

North star-nya bukan "mahasiswa memperoleh nilai Metopen", melainkan: **pada akhir semester, mahasiswa memiliki research project yang cukup matang untuk langsung dieksekusi sebagai TA.**

Research Pack bukan dokumen tunggal. Ia **hidup di repositori riset** ([TPL-15](../08-templates/15-research-repository-template.md)) dan dirilis sebagai `v1.0 Research Pack`. Ini lompatan dari *academic document* (`Proposal.pdf`) menjadi *inspectable research artifact*.

Tiga sifat wajib:

1. **Traceable** — setiap artefak menunjuk ke artefak sebelumnya (RQ ke gap, gap ke baris matriks, klaim ke tabel).
2. **Inspectable** — orang luar dapat membuka repositori dan memeriksa setiap klaim.
3. **Honest** — hasil negatif, keterbatasan, dan penggunaan AI ditulis apa adanya.

## 2. Enam belas artefak — ringkasan

| # | Artefak | Fungsi (satu kalimat) | Lokasi di repositori | Template | Gate dinilai |
|---|---|---|---|---|---|
| 1 | Problem Brief | Mengapa masalah penting | `docs/problem.md` | [TPL-01](../08-templates/01-research-one-pager-template.md) | G2 |
| 2 | Stakeholder / Impact Statement | Untuk siapa riset berguna | `docs/problem.md` §Stakeholder | TPL-01 | G2 |
| 3 | Literature Evidence Map | Apa yang sudah diketahui | `docs/literature-map.md`, `docs/literature/synthesis-matrix.csv` (+ `search-strategy.md`, `verification.md` di `docs/literature/`), `references.bib` | — | G3 |
| 4 | Research Gap | Apa yang belum diketahui | `docs/literature-map.md` §Gap Candidates (G3) → `docs/research-question.md` §Research Gap (G4) | — | G3 (kandidat) → G4 (final, dinilai) |
| 5 | RQ / Hypothesis | Apa yang diuji | `docs/research-question.md` | TPL-01 | G4 |
| 6 | Contribution Statement | Kebaruan/kontribusi | `docs/research-question.md` §Contribution | TPL-01 | G4, revisi G7 |
| 7 | Research Design | Bagaimana menjawab RQ | `docs/research-design.md` + `docs/design-card.md` (TPL-08) | [TPL-08](../08-templates/08-research-design-card.md) | G5 |
| 8 | Dataset / Data Plan | Dari mana evidence berasal | `docs/data-plan.md` (+ ringkasan §Data di `docs/research-design.md`), `data/README.md`, kartu dataset | [TPL-05](../08-templates/05-dataset-registry-template.md) | G5 |
| 9 | Baseline & Metrics | Dibanding apa dan dinilai bagaimana | `docs/research-design.md` §Evaluation, `experiments/pilot-01/experiment-card.md` + `config.yaml` (dan `experiments/main/`) | [TPL-09](../08-templates/09-experiment-card.md) | G5 |
| 10 | Pilot Experiment | Apakah desain viable | `experiments/pilot-01/`, `results/pilot-01/`, `results/analysis.md`, `figures/pilot-01/` | TPL-09 | G6, G7 |
| 11 | Threats to Validity | Apa yang bisa membuat kesimpulan salah | `docs/research-design.md` §Threats (v1), `results/analysis.md` §Threats (v2) | TPL-08 | G5, G7 |
| 12 | Ethics & Privacy | Batas moral/profesional | `docs/ethics.md` (penunjuk `ETHICS.md` di root opsional) | [TPL-11](../08-templates/11-research-integrity-checklist.md) | G5, G8 |
| 13 | AI Usage Statement | AI digunakan untuk apa | `docs/AI-USAGE.md` (log TPL-10 + statement ringkas); statement final `paper/AI-USAGE-STATEMENT.md` | [TPL-10](../08-templates/10-ai-usage-log-template.md) | setiap gate, final G8 |
| 14 | Reproducibility README | Bagaimana direplikasi | `README.md`, `experiments/README.md` | TPL-15 | G6, G8 |
| 15 | Proposal TA | Dokumen formal | `paper/proposal.md` (+ `paper/proposal-v0.8.pdf`, `paper/proposal-v1.0.pdf`) atau manuscript | [MET-05](05-publication-backward-design.md) | G8 |
| 16 | Research Pitch | Pertanggungjawaban oral | `presentation/midterm-pitch.pdf` (W8), `presentation/defense-final.pdf` (W16); notulen di `docs/reviews/midterm-red-team.md`, `docs/reviews/defense-minutes.md` | [TPL-13](../08-templates/13-research-defense-template.md) | G5 (W8), G8 (W16) |

## 3. Spesifikasi per artefak

Format tiap artefak: fungsi → isi minimum → format/lokasi → template → gate → kriteria kualitas (good vs weak) → kesalahan umum.

### 3.1 Problem Brief

- **Fungsi.** Menjelaskan mengapa masalah ini penting, sekarang, di konteks ini.
- **Isi minimum.** Fenomena/masalah nyata; konteks Indonesia/UAI/domain; mengapa penting sekarang; apa yang terjadi bila tidak diteliti; keselarasan klaster (C1–C4) dan domain roadmap; Research ID.
- **Format/lokasi.** `docs/problem.md`, 1–2 halaman; ringkasan di Research One-Pager (`docs/one-pager.md`, v0 di G2 → v1 di G4 → v2 di G7).
- **Template.** TPL-01 (bagian Problem & Why).
- **Gate.** G2 Problem Ready.
- **Good vs weak.** Good: kalimat pertama menyebut masalah, bukan metode; orang luar bisa mengulangnya dalam dua kalimat. Weak: "Penelitian ini menggunakan algoritma M untuk ..." pada paragraf pertama; masalah hanya justifikasi algoritma.
- **Kesalahan umum.** Statistik masalah tanpa sumber; masalah terlalu luas ("pendidikan Indonesia"); masalah tidak punya pemilik.

### 3.2 Stakeholder / Impact Statement

- **Fungsi.** Menyatakan untuk siapa riset berguna dan keputusan apa yang berubah.
- **Isi minimum.** Daftar stakeholder (primer/sekunder); keputusan/tindakan yang berubah bila riset berhasil; ukuran dampak yang masuk akal; bukti bahwa stakeholder itu nyata (wawancara singkat, dokumen, dosen pemilik masalah).
- **Format/lokasi.** Bagian dalam `docs/problem.md`.
- **Template.** TPL-01.
- **Gate.** G2.
- **Good vs weak.** Good: "Tim akademik Prodi memakai prediksi ini untuk memutuskan intervensi di minggu ke-4". Weak: "Bermanfaat bagi masyarakat luas".
- **Kesalahan umum.** Stakeholder dikarang; dampak dilebih-lebihkan; tidak ada keputusan yang berubah.

### 3.3 Literature Evidence Map

- **Fungsi.** Menunjukkan apa yang sudah diketahui dunia, sebagai sintesis — bukan ringkasan per paper.
- **Isi minimum.** Strategi pencarian (`docs/literature/search-strategy.md`); synthesis matrix 15–25 sumber primer dengan kolom problem, metode, data, metrik, hasil, keterbatasan, relevansi; narasi pola: konsisten, bertentangan, belum diuji; `references.bib` terverifikasi (DOI/URL).
- **Format/lokasi.** `docs/literature-map.md` (narasi + tabel tema × sumber + Gap Candidates), `docs/literature/synthesis-matrix.csv`, `docs/literature/verification.md` (bukti verifikasi tiap referensi), `references.bib`.
- **Template.** Kolom matriks di [MET-03](03-metopen-16-week-blueprint.md) W4.
- **Gate.** G3 Evidence Ready.
- **Good vs weak.** Good: matriks memperlihatkan pola; setiap baris bisa dicocokkan dengan halaman paper. Weak: daftar paragraf "Penulis A (2023) meneliti ..."; sumber dari AI yang tidak dibuka.
- **Kesalahan umum.** Referensi tidak terverifikasi; hanya abstrak yang dibaca; sumber sekunder (blog) diperlakukan sebagai primer; tidak ada kriteria inklusi.

### 3.4 Research Gap

- **Fungsi.** Menyatakan apa yang belum diketahui, dengan bukti dari matriks.
- **Isi minimum.** Pernyataan gap; jenis gap (empiris/metodologis/kontekstual/replikasi/artefak); rujukan baris matriks yang mendukung; alasan mengapa gap ini layak diisi.
- **Format/lokasi.** Bagian Gap Candidates di `docs/literature-map.md` (G3) dan bagian Research Gap di `docs/research-question.md` (G4); Issue `type:literature-gap`.
- **Template.** —
- **Gate.** G3 — Gap Candidates (bagian `docs/literature-map.md`); G4 Question Ready — Research Gap final dinilai bersama RQ (`docs/research-question.md`).
- **Good vs weak.** Good: "Baris 4, 9, 12 menunjukkan hasil bertentangan pada data bahasa Indonesia; tidak ada yang mengontrol X". Weak: "Belum ada yang meneliti di UAI".
- **Kesalahan umum.** Gap naratif; gap terlalu besar untuk satu TA; gap yang sebenarnya sudah dijawab tetapi terlewat pencarian.

### 3.5 RQ / Hypothesis

- **Fungsi.** Menyatakan persis apa yang diuji.
- **Isi minimum.** Satu RQ utama (maksimal dua pendukung) dengan konstruk, konteks, pembanding, batas; hipotesis yang dapat difalsifikasi (arah, variabel, kriteria penolakan); tautan RQ → gap → baris matriks.
- **Format/lokasi.** `docs/research-question.md`; Issue `type:research-question`.
- **Template.** TPL-01 (bagian RQ).
- **Gate.** G4 Question Ready.
- **Good vs weak.** Good: "Apakah pada data D, metode M mengungguli baseline B pada metrik μ ≥ Δ?" Weak: "Bagaimana penerapan M untuk X?"
- **Kesalahan umum.** RQ yang tidak bisa salah; terlalu banyak RQ; RQ berubah diam-diam setelah hasil terlihat.

### 3.6 Contribution Statement

- **Fungsi.** Menyatakan kebaruan/kontribusi dan mengapa bermakna.
- **Isi minimum.** Jenis kontribusi (empiris, artefak, metode, dataset, replikasi, studi kasus); kalimat kontribusi; pihak yang diuntungkan; versi awal (G4) dan versi revisi setelah bukti (G7).
- **Format/lokasi.** Bagian dalam `docs/research-question.md`; direvisi di `results/analysis.md`.
- **Template.** TPL-01.
- **Gate.** G4, revisi G7.
- **Good vs weak.** Good: kontribusi sepadan dengan bukti; menyebut batas. Weak: "novel framework" tanpa bukti; kontribusi hanya "menerapkan M di konteks baru" tanpa alasan konteks mengubah hasil.
- **Kesalahan umum.** Melebih-lebihkan; tidak direvisi setelah pilot.

### 3.7 Research Design

- **Fungsi.** Menjelaskan bagaimana RQ dijawab sehingga orang lain bisa menjalankannya.
- **Isi minimum.** Jenis metode dari Computing Research Methods Map dan alternatif yang ditolak; variabel/konstruk; kontrol; sampling; prosedur; alat; rencana analisis.
- **Format/lokasi.** `docs/research-design.md` + Research Design Card di `docs/design-card.md`.
- **Template.** TPL-08.
- **Gate.** G5 Method Ready (dipertahankan di W8).
- **Good vs weak.** Good: orang lain bisa menjalankan tanpa bertanya. Weak: "Penelitian ini menggunakan metode kuantitatif" tanpa prosedur.
- **Kesalahan umum.** Metode dipilih karena familiar, bukan karena RQ; tidak ada kontrol; prosedur tidak bisa diulang.

### 3.8 Dataset / Data Plan

- **Fungsi.** Menjelaskan dari mana bukti berasal dan apakah boleh dipakai.
- **Isi minimum.** Sumber; cara akses; lisensi; privasi (Public/Restricted/Confidential); ukuran; representativitas terhadap populasi; pra-pemrosesan; split train/val/test dan pencegahan leakage; `DS-YYYY-NNN` bila didaftarkan.
- **Format/lokasi.** `docs/data-plan.md` (+ ringkasan §Data di `docs/research-design.md`); `data/README.md`; kartu dataset di `datasets-registry/`.
- **Template.** TPL-05.
- **Gate.** G5.
- **Good vs weak.** Good: representativitas dibahas jujur; data sensitif tidak ada di git. Weak: "Dataset diambil dari Kaggle" tanpa lisensi, ukuran, atau representativitas.
- **Kesalahan umum.** Data mentah di-commit; split dibuat setelah melihat data; tidak ada rencana bila akses data gagal.

### 3.9 Baseline & Metrics

- **Fungsi.** Menetapkan pembanding dan cara menilai sebelum eksperimen dimulai.
- **Isi minimum.** Baseline paling sederhana yang masuk akal (majority class, heuristik, metode standar); metrik utama dan sekunder yang selaras dengan RQ; protokol evaluasi (split, cross-validation, seed); ambang "berarti secara praktis".
- **Format/lokasi.** Bagian Evaluation di `docs/research-design.md`; konfigurasi di `experiments/pilot-01/config.yaml`; kartu di `experiments/pilot-01/experiment-card.md`.
- **Template.** TPL-09.
- **Gate.** G5 — eksperimen tidak boleh dimulai sebelum ini ada.
- **Good vs weak.** Good: metrik ditetapkan sebelum hasil; baseline dijalankan lebih dulu. Weak: metrik dipilih setelah melihat mana yang bagus (metric switching).
- **Kesalahan umum.** Tidak ada baseline; hanya accuracy pada data tidak seimbang; leakage lewat pra-pemrosesan sebelum split.

### 3.10 Pilot Experiment

- **Fungsi.** Membuktikan desain viable dan pipeline berjalan end-to-end.
- **Isi minimum.** Kode eksperimen; konfigurasi; seed; log; hasil baseline + ≥1 pembanding pada subset; figur awal; catatan reproduksi oleh peer; `results/analysis.md` dengan tabel hasil, variansi, error analysis, dan CER table.
- **Format/lokasi.** `experiments/pilot-01/` (experiment-card.md, config.yaml, logs/), `results/pilot-01/` + `results/analysis.md`, `figures/pilot-01/`, `notebooks/`.
- **Template.** TPL-09.
- **Gate.** G6 Experiment Ready (berjalan & direproduksi), G7 Claim Ready (dianalisis).
- **Good vs weak.** Good: angka bisa direproduksi peer dari repositori; run gagal tetap dicatat. Weak: hasil hanya di laptop; satu seed yang paling bagus.
- **Kesalahan umum.** Pilot dijadikan eksperimen penuh (terlalu ambisius); hasil "terlalu bagus" tidak dicurigai leakage.

### 3.11 Threats to Validity

- **Fungsi.** Menyatakan apa yang bisa membuat kesimpulan salah.
- **Isi minimum.** Empat jenis: internal, eksternal, konstruk, statistik/kesimpulan; untuk tiap ancaman: deskripsi, mitigasi, sisa risiko; v1 di desain, v2 setelah pilot.
- **Format/lokasi.** `docs/research-design.md` §Threats (v1); `results/analysis.md` §Threats (v2).
- **Template.** TPL-08.
- **Gate.** G5, G7.
- **Good vs weak.** Good: ancaman spesifik pada riset ini ("label dibuat oleh satu annotator"). Weak: daftar generik yang disalin dari buku.
- **Kesalahan umum.** Ditulis sekali dan tidak diperbarui; ancaman disebut tanpa mitigasi; klaim tetap besar meski ancaman besar.

### 3.12 Ethics & Privacy

- **Fungsi.** Menyatakan batas moral/profesional riset.
- **Isi minimum.** Apakah melibatkan manusia/data pribadi; persetujuan dan izin (komite etik bila ada); anonimisasi; penyimpanan data; bias dan dampak; kepatuhan [SECURITY.md](../../SECURITY.md); pernyataan tidak ada pelanggaran integritas.
- **Format/lokasi.** `docs/ethics.md` (penunjuk `ETHICS.md` di root opsional).
- **Template.** TPL-11 (checklist), [MET-07](07-research-integrity-and-ethics.md).
- **Gate.** G5 (awal), G8 (final).
- **Good vs weak.** Good: menjelaskan risiko nyata dan mitigasi. Weak: "Penelitian ini tidak memiliki isu etika" untuk data mahasiswa.
- **Kesalahan umum.** Data manusia tanpa consent; prompt AI berisi data pribadi; lisensi dataset tidak dicek.

### 3.13 AI Usage Statement

- **Fungsi.** Menyatakan AI digunakan untuk apa, dan bahwa manusia bertanggung jawab.
- **Isi minimum.** `docs/AI-USAGE.md`: tool, tahap riset yang dibantu, jenis bantuan (penulisan vs proses riset), cara verifikasi, apa yang ditolak; log rinci per penggunaan yang material (TPL-10): tool, tanggal, tujuan, prompt/penggunaan, output material, verifikasi, dipakai/tidak.
- **Format/lokasi.** `docs/AI-USAGE.md` (log TPL-10 + statement ringkas, diperbarui tiap minggu/gate); statement final untuk naskah di `paper/AI-USAGE-STATEMENT.md` dan ringkasannya di README riset §AI Usage.
- **Template.** TPL-10; format statement di [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md).
- **Gate.** Diperiksa di setiap gate; final di G8.
- **Good vs weak.** Good: spesifik, membedakan bantuan penulisan dan bantuan proses riset. Weak: "Kami menggunakan ChatGPT untuk membantu" atau tidak ada sama sekali.
- **Kesalahan umum.** Log diisi belakangan dari ingatan; penggunaan pada kode tidak dicatat.

### 3.14 Reproducibility README

- **Fungsi.** Membuat orang lain bisa menjalankan ulang.
- **Isi minimum.** Cara instalasi environment; cara mendapatkan data (atau metadata bila restricted); perintah menjalankan baseline dan eksperimen; seed; versi; struktur folder; hasil yang diharapkan; lisensi per komponen; Current Research Gate.
- **Format/lokasi.** `README.md` (root riset), `experiments/README.md`.
- **Template.** TPL-15.
- **Gate.** G6, G8.
- **Good vs weak.** Good: peer berhasil menjalankan tanpa bertanya. Weak: "Jalankan notebook" tanpa environment.
- **Kesalahan umum.** Path absolut; dependensi tidak dipin; data step dilewati.

### 3.15 Proposal TA

- **Fungsi.** Dokumen formal untuk pendaftaran TA (atau manuscript bila endgame paper).
- **Isi minimum.** Judul; latar belakang (dari Problem Brief); tinjauan pustaka (dari Evidence Map); gap & RQ; kontribusi; metode & desain; data; evaluasi (baseline, metrik); hasil pilot; threats; etika; jadwal TA; referensi terverifikasi; AI usage statement.
- **Format/lokasi.** `paper/proposal.md` (sumber) + `paper/proposal-v0.8.pdf` (v0.8 draft, W13) → v0.9 revisi pasca peer review (W15) → `paper/proposal-v1.0.pdf` (v1.0 final, W16), sesuai format Prodi; struktur IMRaD computing di [MET-05](05-publication-backward-design.md).
- **Template.** Format resmi Prodi (`[isi]`); pemetaan artefak → bagian di MET-05.
- **Gate.** G8.
- **Good vs weak.** Good: setiap bagian ditarik dari artefak yang sudah direview. Weak: ditulis dari nol di minggu terakhir, tidak konsisten dengan repositori.
- **Kesalahan umum.** Sitasi tidak ada di `references.bib`; hasil pilot tidak sama dengan `results/`.

### 3.16 Research Pitch

- **Fungsi.** Pertanggungjawaban oral: desain (W8) dan temuan (W16).
- **Isi minimum.** Slide 7–10 menit; notulen pertanyaan & jawaban; daftar revisi yang dijanjikan.
- **Format/lokasi.** `presentation/midterm-pitch.pdf` (W8), `presentation/defense-draft.pdf`, `presentation/defense-final.pdf` (W16); notulen di `docs/reviews/midterm-red-team.md` dan `docs/reviews/defense-minutes.md`; rekaman bila ada.
- **Template.** TPL-13.
- **Gate.** G5 (Design Defense), G8 (Research Defense).
- **Good vs weak.** Good: jawaban merujuk figur/tabel; mengakui batas tanpa diminta. Weak: membaca slide; menjawab dengan hasil yang tidak ada di repositori.
- **Kesalahan umum.** Terlalu banyak slide teori; tidak ada slide threats.

## 4. Struktur repositori minimum

Dokumen sumber menetapkan *mindset* "Research Repository minimal": `README.md`, `research-question.md`, `literature/`, `data/`, `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `references.bib`, `AI-USAGE.md`, `ETHICS.md` — *tidak harus semua lengkap di Metopen, tetapi mindset-nya sudah dibangun*. Daftar itu dikutip sebagai mindset; **penempatan kanonik: lihat [TPL-15](../08-templates/15-research-repository-template.md)**. Ringkasan pohon kanoniknya:

```
proj-YYYY-topic/
├── README.md                      # Reproducibility README + Current Research Gate + lisensi per komponen (TPL-15)
├── CITATION.cff · LICENSE · LICENSE-DOCS · CHANGELOG.md · requirements.txt|environment.yml · run.sh
├── references.bib                 # semua sitasi terverifikasi (DOI/URL)
├── docs/
│   ├── team.md · endgame.md · ai-protocol-agreement.md     # G1
│   ├── AI-USAGE.md                # AI Usage Log (TPL-10) + statement ringkas; diperbarui tiap minggu/gate
│   ├── problem.md                 # Problem Brief + Stakeholder/Impact (G2)
│   ├── one-pager.md               # Research One-Pager v0 (G2) → v1 (G4) → v2 (G7)
│   ├── literature/                # search-strategy.md, search-log.csv, screening.csv, synthesis-matrix.csv, verification.md, common-metrics-baselines.md (G3)
│   ├── literature-map.md          # Literature Evidence Map + Gap Candidates (G3)
│   ├── research-question.md       # Research Gap final + RQ/Hypothesis + Contribution (G4)
│   ├── research-design.md         # Research Design + Baseline & Metrics + Threats v1 (G5)
│   ├── design-card.md · data-plan.md · ethics.md           # Design Card TPL-08, Data Plan, Ethics & Privacy (G5)
│   ├── journal/ · reviews/        # jurnal mingguan w01…w16-reflection; notulen review (w05-studio-feedback, midterm-red-team, reproduction-pilot-01, defense-rehearsal, defense-minutes)
│   └── research-pack.md · integrity-checklist.md · handoff.md   # G8: indeks 16 artefak → lokasi file, TPL-11, TPL-14
├── data/README.md                 # metadata & cara akses saja; data mentah sensitif TIDAK di repo
├── src/ · notebooks/
├── experiments/                   # README.md (cara menjalankan ulang), pilot-01/ (experiment-card.md, config.yaml, logs/), main/
├── results/                       # pilot-01/, main/, analysis.md (tabel hasil, error analysis, CER, Threats v2 — G7)
├── figures/                       # pilot-01/, main/
├── paper/                         # outline.md, proposal.md, proposal-v0.8.pdf, proposal-v1.0.pdf, AI-USAGE-STATEMENT.md, response-to-reviewers.md, verification-checklist.md (G8)
└── presentation/                  # midterm-pitch.pdf (W8), defense-draft.pdf, defense-final.pdf (W16)
```

Pohon lengkap (beserta skrip pembuat folder): [TPL-15](../08-templates/15-research-repository-template.md). `research-question.md` dan `ETHICS.md` di root dari daftar sumber boleh dibuat sebagai penunjuk opsional ke `docs/research-question.md` dan `docs/ethics.md`.

Aturan: **tidak harus semua lengkap di Metopen, tetapi mindset-nya dibangun.** Folder boleh kosong dengan `README.md` yang menyatakan "belum ada; akan diisi di TA", tetapi tidak boleh hilang.

## 5. Wajib vs opsional: Metopen vs TA

| # | Artefak | Metopen (v1.0 Research Pack) | TA (akhir semester VIII) |
|---|---|---|---|
| 1 | Problem Brief | **Wajib** final | Wajib (revisi minor) |
| 2 | Stakeholder/Impact | **Wajib** final | Wajib |
| 3 | Literature Evidence Map | **Wajib** 15–25 sumber | Wajib, diperluas |
| 4 | Research Gap | **Wajib** | Wajib |
| 5 | RQ/Hypothesis | **Wajib** | Wajib (boleh direvisi dengan pencatatan) |
| 6 | Contribution Statement | **Wajib** v-awal + revisi pasca-pilot | Wajib final |
| 7 | Research Design | **Wajib** (lolos G5) | Wajib final |
| 8 | Dataset/Data Plan | **Wajib** rencana + kartu dataset; data penuh opsional | Wajib data penuh |
| 9 | Baseline & Metrics | **Wajib** ditetapkan & baseline dijalankan | Wajib |
| 10 | Pilot Experiment | **Wajib** pilot pada subset + reproduksi peer; eksperimen penuh opsional | Eksperimen penuh wajib |
| 11 | Threats to Validity | **Wajib** v1 & v2 | Wajib final |
| 12 | Ethics & Privacy | **Wajib** | Wajib (+ izin formal bila human subjects) |
| 13 | AI Usage Statement | **Wajib** + log | Wajib + log lanjutan |
| 14 | Reproducibility README | **Wajib** minimum (env, run, seed) | Wajib lengkap (artifact-ready) |
| 15 | Proposal TA | **Wajib** | Digantikan laporan TA / manuscript |
| 16 | Research Pitch | **Wajib** W8 & W16 | Sidang TA |
| — | Full results & analysis | Opsional (bila pilot sudah kuat) | Wajib |
| — | Manuscript untuk venue | Opsional (aspirational) | Opsional → [MET-05](05-publication-backward-design.md) |
| — | Artefak rilis (`ART-`), dataset rilis (`DS-`) | Opsional | Didorong |

## 6. Checklist kelengkapan (dipakai saat G8 dan handoff)

```
[ ] 1  Problem Brief ada, problem-first, Research ID tercantum
[ ] 2  Stakeholder & keputusan yang berubah eksplisit
[ ] 3  Synthesis matrix ≥15 sumber, semua DOI/URL terverifikasi, references.bib rapi
[ ] 4  Gap merujuk baris matriks
[ ] 5  RQ/H spesifik, tertelusur ke gap; kriteria penolakan hipotesis ada
[ ] 6  Contribution Statement direvisi setelah pilot; tidak melebihi bukti
[ ] 7  Research Design Card lengkap; alternatif metode yang ditolak disebut
[ ] 8  Data plan: sumber, lisensi, privasi, split; kartu dataset bila baru; tidak ada data mentah sensitif di git
[ ] 9  Baseline & metrik ditetapkan sebelum eksperimen; protokol evaluasi mencegah leakage
[ ] 10 Pilot berjalan; hasil di results/; direproduksi peer (catatan ada)
[ ] 11 Threats v1 dan v2, dengan mitigasi
[ ] 12 docs/ethics.md terisi; consent/izin bila human subjects
[ ] 13 docs/AI-USAGE.md (log + statement) dan paper/AI-USAGE-STATEMENT.md lengkap; tidak ada referensi/hasil buatan AI
[ ] 14 README: env, run, seed, hasil yang diharapkan, Current Research Gate, lisensi
[ ] 15 Proposal TA konsisten dengan repositori; semua sitasi ada di references.bib
[ ] 16 Slide W8 & W16 di presentation/ (midterm-pitch.pdf, defense-final.pdf); notulen di docs/reviews/ (midterm-red-team.md, defense-minutes.md)
[ ] —  Research Integrity Checklist (TPL-11) ditandatangani
[ ] —  Handoff (TPL-14) terisi; release v1.0 dibuat; label gate & Mission Control diperbarui
```

## 7. Versi dan rilis

| Release | Isi Research Pack pada titik itu |
|---|---|
| v0.1 Problem Validated | Artefak 1–2 |
| v0.2 Evidence Ready | + 3–4 |
| v0.3 Research Design | + 5–9, 11 (v1), 12 (awal) |
| v0.5 Pilot Experiment | + 10 (pilot), 14 (minimum) |
| v0.8 Manuscript Draft | + 15 draft (`paper/proposal-v0.8.pdf`, W13), 13 |
| **v1.0 Research Pack** | 1–16 lengkap sesuai §5 kolom Metopen; proposal v1.0 (`paper/proposal-v1.0.pdf`, W16) setelah revisi v0.9 pasca peer review (W15) |
| v1.1 Submitted / v2.0 Published | Jalur publikasi ([MET-05](05-publication-backward-design.md)) |

Research Pack yang lolos G8 diwariskan ke TA lewat [TPL-14](../08-templates/14-research-handoff-template.md): *what exists, missing evidence, next steps, owner*. Dosen pembimbing TA mulai dari sana, bukan dari judul kosong.
