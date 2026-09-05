# Research Repository Template

> **ID** TPL-15 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa peneliti, dosen/peneliti, mentor, `@maintainers`, peer reproducer
> **Terkait** [GOVERNANCE.md §2, §6.3](../../GOVERNANCE.md) · [CONTRIBUTING.md §3, §5](../../CONTRIBUTING.md) · [LICENSING.md §5–6](../../LICENSING.md) · [SECURITY.md](../../SECURITY.md) · [OPS-03 G1 & G6](../06-execution-os/03-research-gates.md) · [TPL-05 Dataset Registry](05-dataset-registry-template.md) · [TPL-09 Experiment Card](09-experiment-card.md) · [TPL-10 AI Usage Log](10-ai-usage-log-template.md)

## Cara pakai

Setiap riset yang benar-benar dijalankan mendapat satu repositori `proj-YYYY-<topik>` dengan struktur standar ini, dibuat saat onboarding S0 (pra-W1, OPS-005) sebagai bagian G1 Endgame Ready yang dituntaskan di W1 (jalankan skrip di bagian akhir), lalu diisi bertahap mengikuti gate. Repositori adalah **inspectable research artifact**, bukan sekadar tempat kode: README-nya adalah README riset, bukan README software. Visibilitas awal INTERNAL (private) dan menjadi PUBLIC saat rilis artefak/publikasi setelah IP review ([LICENSING.md](../../LICENSING.md)). Reviewer G6 memeriksa bahwa `src/`, `experiments/`, environment, dan README cara menjalankan ada dan peer dapat mereproduksi angka baseline; data mentah sensitif tidak pernah di-commit ([SECURITY.md](../../SECURITY.md)).

## Konvensi

| Hal | Aturan | Contoh |
|---|---|---|
| Nama repo | `proj-YYYY-<topik-kebab-case>`, tahun = tahun Research ID | `proj-2026-ai-academic-advising`; bukan `final-project-baru-v2-fix` |
| Branch gate | `research/g1-endgame` … `research/g8-contribution`; kerja lain `feat/…`, `exp/…`, `paper/…`, `docs/…` | `research/g5-method` |
| PR | `GATE REVIEW: <Nama Gate>` memakai template `.github/PULL_REQUEST_TEMPLATE/`; merge = gate lulus | `GATE REVIEW: Method Ready` |
| Release | `v0.1` Problem Validated · `v0.2` Evidence Ready · `v0.3` Research Design · `v0.5` Pilot Experiment · `v0.8` Manuscript Draft · `v1.0` Research Pack · `v1.1` Submitted · `v2.0` Published | tag `v0.5` setelah G6 |
| Commit | imperatif singkat + Research ID/Task ID | `Add pilot-01 results (UIAI-2026-001, OPS-088)` |
| Topics | dari controlled vocabulary GOVERNANCE §6.2 | `student-research`, `education`, `responsible-ai` |
| Lisensi | `LICENSE` Apache-2.0 (kode), `LICENSE-DOCS` CC BY 4.0 (dokumen); dataset & model per tabel lisensi README | — |

## Struktur repositori

Pohon ini adalah tata letak **kanonik** yang dirujuk seluruh task WBS ([OPS-01](../06-execution-os/01-research-wbs-master.md)); dokumen lain (MET-04, OPS-03, template, PR template) memakai path yang sama. Komentar per baris menyebut gate yang menghasilkan/menilai file itu.

```
proj-YYYY-topic/
├── README.md                      # README riset (blok di bawah): Research ID, status, Current Research Gate, lisensi per komponen, reproducibility
├── CITATION.cff                   # cara mengutip repo
├── LICENSE                        # Apache-2.0 (kode)
├── LICENSE-DOCS                   # CC BY 4.0 (dokumen)
├── CHANGELOG.md                   # per release v0.1 … v2.0
├── requirements.txt               # atau environment.yml (versi terkunci)
├── run.sh                         # reproduksi end-to-end
├── references.bib                 # semua sitasi terverifikasi (DOI/URL)
├── docs/
│   ├── team.md                    # G1: anggota, peran, mentor
│   ├── endgame.md                 # G1: endgame, entry door, aspirasi
│   ├── ai-protocol-agreement.md   # G1: AI Research Protocol Agreement (AIX-04)
│   ├── AI-USAGE.md                # AI Usage Log (TPL-10) + ringkasan AI Usage Statement; diperbarui tiap minggu/gate
│   ├── problem.md                 # G2: Problem Brief + Stakeholder/Impact Statement
│   ├── one-pager.md               # Research One-Pager (TPL-01) v0 (G2) → v1 (G4) → v2 (G7/G8)
│   ├── literature/
│   │   ├── search-strategy.md     # G3: kata kunci, basis data, kriteria inklusi/eksklusi
│   │   ├── search-log.csv         # G3: log pencarian
│   │   ├── screening.csv          # G3: hasil penyaringan
│   │   ├── synthesis-matrix.csv   # G3: matriks sintesis (problem, metode, data, metrik, hasil, keterbatasan, relevansi)
│   │   ├── verification.md        # G3: bukti verifikasi tiap referensi (DOI/URL)
│   │   └── common-metrics-baselines.md  # G3/G5: metrik & baseline yang lazim di literatur
│   ├── literature-map.md          # G3: Literature Evidence Map (narasi + pola + Gap Candidates + Feasibility)
│   ├── research-question.md       # G4: Research Gap final, RQ/hipotesis, Contribution Statement
│   ├── research-design.md         # G5: Research Design (jenis metode, variabel, prosedur, evaluasi, Threats v1)
│   ├── design-card.md             # G5: Research Design Card (TPL-08)
│   ├── data-plan.md               # G5: Dataset/Data Plan (sumber, akses, lisensi, privasi, split, leakage prevention) + link kartu DS
│   ├── ethics.md                  # G5: Ethics & Privacy (consent, anonimisasi, komite etik)
│   ├── journal/                   # jurnal mingguan (Execution): w01.md … w15.md, w16-reflection.md
│   ├── reviews/                   # notulen review: w05-studio-feedback.md, midterm-red-team.md, reproduction-pilot-01.md, defense-rehearsal.md, defense-minutes.md
│   ├── research-pack.md           # G8: indeks Research Pack (16 artefak MET-04 → lokasi file)
│   ├── integrity-checklist.md     # G8: Research Integrity Checklist (TPL-11) tertandatangani
│   └── handoff.md                 # G8: Research Handoff (TPL-14)
├── data/
│   └── README.md                  # metadata & cara akses saja; data mentah sensitif TIDAK di repo (SECURITY.md)
├── src/                           # data.py, baseline.py, method.py, evaluate.py, analysis.py, report.py
├── notebooks/                     # eksplorasi (pilot-results.ipynb); hasil final dipindah ke src/
├── experiments/
│   ├── README.md                  # G6: cara menjalankan ulang semua eksperimen (Reproducibility README)
│   ├── pilot-01/                  # G5/G6: experiment-card.md (TPL-09), config.yaml, logs/
│   └── main/                      # G6/G7: README.md, experiment-card.md, config.yaml, logs/
├── results/
│   ├── pilot-01/                  # G6: baseline.json, summary.md, sanity-check.md
│   ├── main/                      # G7: summary.csv, *.json
│   └── analysis.md                # G7: tabel hasil, error analysis, CER table, Threats v2
├── figures/
│   ├── pilot-01/                  # G6: figur pilot (baseline selalu terlihat; skrip di src/report.py)
│   └── main/                      # G7: figur final
├── paper/                         # G8: outline.md, proposal.md (Proposal TA / manuscript), proposal-v0.8.pdf, proposal-v1.0.pdf, AI-USAGE-STATEMENT.md, response-to-reviewers.md, verification-checklist.md
└── presentation/                  # G5/G8: midterm-pitch.pdf (W8, TPL-13), defense-draft.pdf, defense-final.pdf (W16)
```

## README riset standar (salin ke `README.md`)

```markdown
# [Research Title]

## Research ID
[UIAI-YYYY-NNN] · Issue #[n] · Cluster [C1–C4] · Domain [isi] · Entry door [isi]

## Problem
[2–3 kalimat: fenomena nyata, konteks, siapa terdampak]

## Why It Matters
[stakeholder; keputusan yang berubah bila riset berhasil]

## Research Question
RQ1 [...]
RQ2 [...]

## Hypothesis
H1 [dapat difalsifikasi] · H2 [...]

## Dataset
[Dataset ID, nama, sumber, ukuran, privasi, cara akses; lihat data/README.md]

## Baseline
[pembanding paling sederhana + lokasi kode]

## Method
[jenis metode + 1 kalimat desain; lihat docs/research-design.md dan docs/design-card.md]

## Evaluation Metrics
[metrik utama & sekunder, ambang praktis, prosedur anti-leakage]

## Research Status
[Idea / TA Ready / Research Ready / Publication Ready / Impact Ready] — release [v0.x] ([tanggal])

## Current Research Gate
[Gn – Nama Gate] — [Active / Review PR #n / Lulus tanggal]

## Expected Contribution
[jenis: empiris / artefak / metode / dataset / replikasi / studi kasus — mengapa bermakna]

## Researchers
[nama (@github) — peran]; mentor [nama]

## Related Course
[AI/ML / Data Mining / NLP / RPL / Metopen / TA] — semester [isi]

## Related Research Program
[program-<nama> / klaster / skema penelitian — atau —]

## Publications
[PUB-YYYY-NNN — venue — status] atau "belum ada"

## Reproducibility
1. `git clone [URL] && cd [repo]`
2. `pip install -r requirements.txt` (Python [versi])
3. Minta akses data sesuai data/README.md; letakkan di `data/raw/` (tidak di-commit)
4. `bash run.sh` → menjalankan baseline + metode, menulis `results/`
Seed: [n] · Config: `experiments/pilot-01/config.yaml` (dan `experiments/main/`) · Hardware: [isi] · Waktu: [isi]
Reproduksi terakhir oleh peer: [nama, tanggal, hasil]

## AI Usage Disclosure
[3–5 kalimat dari docs/AI-USAGE.md: tool, untuk apa, tidak untuk apa, verifikasi, tanggung jawab]

## License
| Komponen | Lisensi |
|---|---|
| Code | Apache-2.0 |
| Documentation | CC-BY-4.0 |
| Dataset | [CC-BY-4.0 / restricted — lihat DS-YYYY-NNN / not released] |
| Model weights | [research-only / not released / —] |
| Paper | [publisher copyright (DOI) / preprint / —] |
```

## Isi minimal `data/README.md` (metadata, bukan data)

```markdown
# Data — [Research ID]
| Field | Isi |
|---|---|
| Dataset ID & kartu | [DS-YYYY-NNN] — datasets-registry |
| Sumber & pemilik | [isi] |
| Lokasi fisik & cara akses | [server/HF/Kaggle/Drive/cloud; siapa menyetujui] |
| Privasi & lisensi | [Public/Restricted/Confidential; lisensi] |
| Skema | kolom, tipe, satuan, nilai kosong |
| Preprocessing | skrip `src/data.py`, urutan langkah, versi hasil |
| Split | train/val/test atau pilot/eval; cara membagi; file daftar ID split |
| Sampel (opsional) | `data/sample-synthetic.csv` (≤ 100 baris, tanpa data pribadi) |
| Yang TIDAK ada di repo | selain README ini dan sampel sintetis opsional, tidak ada data lain: data mentah, data pribadi, kredensial (`.gitignore`: data/raw/, *.key, .env) |
```

## Isi minimal `experiments/README.md`

```markdown
# Experiments — [Research ID]
| Run | Nama | RQ | Status | Config | Hasil | Kartu |
|---|---|---|---|---|---|---|
| pilot-01 | [pilot …] | RQ1 | [selesai/berjalan] | experiments/pilot-01/config.yaml | results/pilot-01/summary.md | experiments/pilot-01/experiment-card.md |
| main | [eksperimen utama …] | RQ1–RQ2 | [rencana] | experiments/main/config.yaml | results/main/summary.csv | experiments/main/experiment-card.md |
Cara menjalankan satu eksperimen: `bash run.sh --config experiments/pilot-01/config.yaml --seed 42`
Konvensi: satu kartu (TPL-09) per run; pra-registrasi tidak diubah setelah run; hasil ke results/<run>/, figur ke figures/<run>/.
```

## Skrip cepat membuat struktur

```bash
# ganti nilai di baris pertama, lalu jalankan di folder kerja (S0 onboarding, OPS-005); membuat seluruh struktur kanonik di atas
REPO=proj-2026-ai-academic-advising; RID=UIAI-2026-001; TITLE="AI-assisted academic advising for Indonesian universities"
mkdir -p "$REPO"/{docs/literature,docs/journal,docs/reviews,data,src,notebooks,experiments/pilot-01/logs,experiments/main/logs,results/pilot-01,results/main,figures/pilot-01,figures/main,paper,presentation} && cd "$REPO" && git init -q
printf '# %s\n\n## Research ID\n%s\n' "$TITLE" "$RID" > README.md
for f in team endgame ai-protocol-agreement AI-USAGE problem one-pager literature-map research-question research-design design-card data-plan ethics research-pack integrity-checklist handoff; do printf '# %s — %s\n' "$f" "$RID" > "docs/$f.md"; done
for f in search-strategy verification common-metrics-baselines; do printf '# %s — %s\n' "$f" "$RID" > "docs/literature/$f.md"; done; touch docs/literature/{search-log,screening,synthesis-matrix}.csv
for w in $(seq -w 1 15); do printf '# Journal W%s — %s\n' "$w" "$RID" > "docs/journal/w$w.md"; done; printf '# Reflection W16 — %s\n' "$RID" > docs/journal/w16-reflection.md
printf '# Data — %s\n(metadata saja; data mentah tidak di-commit)\n' "$RID" > data/README.md
printf '# Experiments — %s\n' "$RID" > experiments/README.md; printf '# Experiment Card — pilot-01 — %s\n' "$RID" > experiments/pilot-01/experiment-card.md; printf 'seed: 42\n' > experiments/pilot-01/config.yaml; printf '# Main experiment — %s\n' "$RID" > experiments/main/README.md
for f in data baseline method evaluate analysis report; do printf '"""%s — %s"""\n' "$f" "$RID" > "src/$f.py"; done
printf '# Analysis — %s\n' "$RID" > results/analysis.md
for f in outline proposal AI-USAGE-STATEMENT response-to-reviewers verification-checklist; do printf '# %s — %s\n' "$f" "$RID" > "paper/$f.md"; done
touch docs/reviews/.gitkeep experiments/pilot-01/logs/.gitkeep experiments/main/logs/.gitkeep results/pilot-01/.gitkeep results/main/.gitkeep figures/pilot-01/.gitkeep figures/main/.gitkeep notebooks/.gitkeep presentation/.gitkeep
printf 'data/raw/\n*.key\n.env\n__pycache__/\n.ipynb_checkpoints/\n' > .gitignore
printf '# Changelog\n\n## v0.1 Problem Validated — [YYYY-MM-DD]\n' > CHANGELOG.md
printf 'cff-version: 1.2.0\nmessage: "Cite this research repository."\ntitle: "%s"\nauthors:\n  - family-names: "[isi]"\n    given-names: "[isi]"\n    affiliation: "Universitas Al-Azhar Indonesia"\nidentifiers:\n  - type: other\n    value: "%s"\nlicense: Apache-2.0\n' "$TITLE" "$RID" > CITATION.cff
touch requirements.txt references.bib run.sh && chmod +x run.sh
# salin LICENSE (Apache-2.0) dan LICENSE-DOCS (CC BY 4.0) dari repo uai-ai-research-center, lalu:
git add -A && git commit -qm "Scaffold research repository ($RID)" && git checkout -qb research/g1-endgame
```

## Contoh terisi (cuplikan README `proj-2026-ai-academic-advising`)

**Research ID** UIAI-2026-001 · Issue #[n] · Cluster C3 · Domain Education · Entry door Problem. **Problem** Dosen wali menangani puluhan mahasiswa dengan waktu terbatas; pelanggaran prasyarat dan keterlambatan lulus. **Research Question** RQ1 validitas rekomendasi LLM+RAG vs rule-based; RQ2 penilaian dosen wali. **Dataset** DS-2026-001 (UAI, restricted, 120 transkrip anonim) + 40 kasus sintetis di `data/sample-synthetic.csv`. **Baseline** rule-based prerequisite checker (`src/baseline.py`). **Evaluation Metrics** constraint-violation rate, precision@5, Likert; ambang 10 poin persen. **Research Status** TA Ready — v1.0 (2026-12-[dd]). **Current Research Gate** G8 – Contribution Ready — lulus 2026-12-[dd]. **Researchers** [Mahasiswa A] (@[isi]) — lead; [Mahasiswa B] — eksperimen; mentor [Dosen C3]. **Related Course** Metopen semester VII → TA. **Publications** belum ada (target [konferensi nasional — isi]). **Reproducibility** `bash run.sh`, seed 42, Python 3.11; reproduksi peer [Mahasiswa C] 2026-10-[dd] (violation 7,9 %). **AI Usage Disclosure** AI dipakai untuk kata kunci pencarian, debugging parser, kritik desain, koreksi bahasa; tidak untuk data/hasil/referensi tanpa verifikasi; 3 referensi usulan AI dibuang; log 14 entri. **License** Code Apache-2.0 · Docs CC-BY-4.0 · Dataset restricted (DS-2026-001) · Model weights not released · Paper —.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| README | Orang yang datang tiga tahun kemudian mengerti masalah, klaim, status, cara menjalankan | README berisi cara install saja |
| Data | `data/README.md` lengkap; data mentah tidak di-commit; sampel sintetis kecil | CSV transkrip mahasiswa di repo |
| Reproducibility | `run.sh` + environment + seed + config; reproduksi peer tercatat | Notebook dengan path absolut laptop |
| Gate & release | Branch/PR/release mengikuti konvensi; Current Research Gate diperbarui | Semua kerja di `main` tanpa PR |
| Lisensi | Tabel per komponen terisi | Tanpa LICENSE |
| Kebersihan | Notebook eksplorasi dipisah dari `src/`; figur punya skrip | Hasil final hanya di notebook |
