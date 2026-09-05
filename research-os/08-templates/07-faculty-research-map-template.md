# Faculty Research Map Template

> **ID** TPL-07 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, kepala pusat riset, ketua klaster, dosen, admin riset; mahasiswa (versi ringkas untuk memilih mentor)
> **Terkait** [AIR-03 Faculty Research Alignment](../03-ai-research-ecosystem/03-faculty-research-alignment.md) · [AIR-02 Clusters](../03-ai-research-ecosystem/02-ai-research-clusters.md) · [ARC-03 AI Contribution Modes](../02-academic-architecture/03-ai-contribution-modes.md) · [TPL-04 Backlog](04-research-backlog-template.md) · [GOVERNANCE.md §9 View 5](../../GOVERNANCE.md) · [GOV-01 Governance Model](../07-governance/01-governance-model.md)

## Cara pakai

Peta ini menghubungkan **dosen ↔ klaster ↔ research backlog** agar setiap masalah di backlog punya calon mentor dan setiap dosen punya jalur riset AI yang jelas, tanpa memaksa semua dosen menjadi "peneliti AI". Diisi oleh setiap dosen (baris sendiri) pada workshop dosen awal semester, dikonsolidasi oleh admin riset/ketua klaster, dan disimpan di `research-os/03-ai-research-ecosystem/` sebagai lampiran AIR-03 atau di dokumen internal Prodi (versi dengan kapasitas dan skema hibah bersifat INTERNAL). Dipakai pada W1 (G1: identifikasi kandidat mentor), saat triase backlog (menetapkan calon mentor), dan untuk View 5 *Faculty Portfolio* di Mission Control. Ditinjau tiap semester; nama dosen riil memakai placeholder `[isi]` di dokumen publik.

## Kolom

| Kolom | Cara mengisi |
|---|---|
| Dosen | nama + akun GitHub + tim klaster (`@ai-models`, `@ai-systems`, `@responsible-ai`, `@applied-ai`) |
| Existing Expertise | bidang riset/keahlian saat ini (2–4 kata kunci), termasuk yang non-AI |
| AI Relation | AI Core / AI Enabling / AI Application / Responsible AI ([MST-03 §4.2](../00-master/03-glossary.md)); boleh lebih dari satu |
| Primary Cluster | C1 / C2 / C3 / C4 |
| Secondary Cluster | C1–C4 atau — |
| Possible Research | 1–3 arah riset konkret yang bisa dimentori 1–2 tahun ke depan |
| Backlog IDs | Research ID / Issue backlog yang dimiliki atau dimentori |
| Kapasitas mentoring | jumlah tim Metopen/TA per semester yang sanggup dimentori (angka), dan sisa kapasitas |
| Skema penelitian internal | skema hibah/penelitian internal UAI yang diikuti atau direncanakan [isi; verifikasi ke LPPM], tahun, dan apakah melibatkan mahasiswa |
| Mata kuliah & mode | mata kuliah yang diampu + mode F/E/R ([ARC-03](../02-academic-architecture/03-ai-contribution-modes.md)) |

## Template tabel

```markdown
| Dosen | Existing Expertise | AI Relation | Primary Cluster | Secondary Cluster | Possible Research | Backlog IDs | Kapasitas mentoring (tim/semester; sisa) | Skema penelitian internal | Mata kuliah & mode |
|---|---|---|---|---|---|---|---|---|---|
| [nama (@github)] | [kata kunci] | [Core/Enabling/Application/Responsible] | [C] | [C/—] | 1. [...] 2. [...] | [UIAI-…; #n] | [n; sisa n] | [skema, tahun, mahasiswa terlibat y/n] | [MK — F/E/R] |
```

Ringkasan klaster (diisi admin riset setelah konsolidasi):

```markdown
| Cluster | Jumlah dosen (primary) | Jumlah dosen (secondary) | Total kapasitas mentoring | Backlog aktif | Backlog tanpa mentor |
|---|---|---|---|---|---|
| C1 | | | | | |
| C2 | | | | | |
| C3 | | | | | |
| C4 | | | | | |
```

## Aturan

1. Setiap dosen punya **satu** Primary Cluster; Secondary opsional. Dosen non-AI tetap masuk peta lewat AI Relation *Enabling* atau *Application* (mis. basis data → data infrastructure; HCI → human evaluation; keamanan → AI safety/security).
2. Kapasitas mentoring default 2–3 tim per semester; angka nyata ditetapkan dosen sendiri dan dihormati saat penugasan.
3. Masalah backlog dengan `Backlog tanpa mentor` > 0 dibahas di rapat klaster; bila tidak ada mentor dalam 1 semester, prioritas diturunkan.
4. Peta bukan penilaian kinerja; ia alat pencocokan (matching) dan perencanaan hibah/BKD. Data BKD tetap di sistem kepegawaian.
5. Versi publik hanya memuat klaster, expertise, dan arah riset; kapasitas dan skema hibah hanya di versi internal.

## Contoh terisi (ilustratif)

| Dosen | Existing Expertise | AI Relation | Primary Cluster | Secondary Cluster | Possible Research | Backlog IDs | Kapasitas mentoring | Skema penelitian internal | Mata kuliah & mode |
|---|---|---|---|---|---|---|---|---|---|
| [Dosen C3] (@[isi]) | HCI, sistem informasi akademik, evaluasi pengguna | AI Application, Responsible AI | C3 | C4 | 1. AI-assisted academic advising dan kepercayaan pengguna 2. Explainable recommendation untuk keputusan akademik 3. Evaluasi human-AI pada layanan kampus | UIAI-2026-001; #[n] | 3; sisa 2 | [skema penelitian internal UAI 2026 — isi; verifikasi]; melibatkan 2 mahasiswa: ya | HCI — E; Metopen — R |
| [Dosen C1] (@[isi]) | NLP bahasa Indonesia, information retrieval | AI Core | C1 | C3 | 1. Evaluasi RAG berbahasa Indonesia untuk dokumen kurikulum/regulasi 2. Benchmark QA domain pendidikan | #[n] | 2; sisa 1 | [isi] | NLP — R; AI/ML — E |
| [Dosen C2] (@[isi]) | Rekayasa perangkat lunak, pengujian | AI Enabling | C2 | — | 1. Pengujian sistem berbasis LLM 2. MLOps untuk prototipe riset mahasiswa | — | 2; sisa 2 | — | RPL — E; Pengujian PL — F |

Baris ringkasan (contoh): C3 · primary 1 · secondary 2 · kapasitas 3 · backlog aktif 1 · tanpa mentor 0.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Possible Research | Arah konkret yang bisa menjadi Issue backlog dalam 1 semester | "AI untuk berbagai bidang" |
| AI Relation | Dosen non-AI dipetakan jujur sebagai Enabling/Application | Semua dosen ditulis "AI Core" |
| Kapasitas | Angka yang ditetapkan dosen sendiri dan diperbarui tiap semester | Kosong atau angka tak terbatas |
| Keterkaitan backlog | Setiap Backlog ID di peta ada di BACKLOG.md dan sebaliknya | Backlog tanpa mentor tidak terlihat |
| Privasi | Versi publik tanpa kapasitas/hibah | Data hibah dan beban dosen di README publik |
