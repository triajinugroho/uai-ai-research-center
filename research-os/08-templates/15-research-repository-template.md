# Research Repository Template

> **ID** TPL-15 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa peneliti, dosen/peneliti, mentor, `@maintainers`, peer reproducer
> **Terkait** [GOVERNANCE.md §2, §6.3](../../GOVERNANCE.md) · [CONTRIBUTING.md §3, §5](../../CONTRIBUTING.md) · [LICENSING.md §5–6](../../LICENSING.md) · [SECURITY.md](../../SECURITY.md) · [OPS-03 G1 & G6](../06-execution-os/03-research-gates.md) · [TPL-05 Dataset Registry](05-dataset-registry-template.md) · [TPL-09 Experiment Card](09-experiment-card.md) · [TPL-10 AI Usage Log](10-ai-usage-log-template.md)

## Cara pakai

Setiap riset yang benar-benar dijalankan mendapat satu repositori `proj-YYYY-<topik>` dengan struktur standar ini, dibuat pada W1 sebagai bagian G1 Endgame Ready (jalankan skrip di bagian akhir), lalu diisi bertahap mengikuti gate. Repositori adalah **inspectable research artifact**, bukan sekadar tempat kode: README-nya adalah README riset, bukan README software. Visibilitas awal INTERNAL (private) dan menjadi PUBLIC saat rilis artefak/publikasi setelah IP review ([LICENSING.md](../../LICENSING.md)). Reviewer G6 memeriksa bahwa `src/`, `experiments/`, environment, dan README cara menjalankan ada dan peer dapat mereproduksi angka baseline; data mentah sensitif tidak pernah di-commit ([SECURITY.md](../../SECURITY.md)).

## Konvensi

| Hal | Aturan | Contoh |
|---|---|---|
| Nama repo | `proj-YYYY-<topik-kebab-case>`, tahun = tahun Research ID | `proj-2026-ai-academic-advising`; bukan `final-project-baru-v2-fix` |
| Branch gate | `research/g1-endgame` … `research/g8-contribution`; kerja lain `feat/…`, `exp/…`, `paper/…` | `research/g5-method` |
| PR | `GATE REVIEW: <Nama Gate>` memakai template `.github/PULL_REQUEST_TEMPLATE/`; merge = gate lulus | `GATE REVIEW: Method Ready` |
| Release | `v0.1` Problem Validated · `v0.2` Evidence Ready · `v0.3` Research Design · `v0.5` Pilot Experiment · `v0.8` Manuscript Draft · `v1.0` Research Pack · `v1.1` Submitted · `v2.0` Published | tag `v0.5` setelah G6 |
| Commit | imperatif singkat + Research ID/Task ID | `Add EXP-01 pilot results (UIAI-2026-001, OPS-078)` |
| Topics | dari controlled vocabulary GOVERNANCE §6.2 | `student-research`, `education`, `responsible-ai` |
| Lisensi | `LICENSE` Apache-2.0 (kode), `LICENSE-DOCS` CC BY 4.0 (dokumen); dataset & model per tabel lisensi README | — |

## Struktur repositori

```
proj-YYYY-topic/
├── README.md                 # README riset (blok di bawah)
├── CITATION.cff              # cara mengutip repo
├── LICENSE                   # Apache-2.0 (kode)
├── LICENSE-DOCS              # CC BY 4.0 (dokumen)
├── CHANGELOG.md              # per release v0.1 … v2.0
├── requirements.txt          # atau environment.yml
├── run.sh                    # reproduksi end-to-end
├── references.bib
├── docs/
│   ├── problem.md            # G2
│   ├── research-question.md  # G4
│   ├── literature-map.md     # G3 (+ synthesis-matrix.csv)
│   ├── research-design.md    # G5 (TPL-08)
│   ├── ethics.md             # G5
│   ├── AI-USAGE.md           # statement (TPL-10)
│   ├── ai-usage-log.md
│   ├── one-pager.md          # TPL-01
│   ├── integrity-checklist.md# TPL-11
│   └── handoff-*.md          # TPL-14
├── data/
│   └── README.md             # metadata saja, bukan data
├── src/                      # kode sumber (baseline, metode, evaluasi)
├── notebooks/                # eksplorasi; hasil final dipindah ke src/
├── experiments/              # EXP-NN-*.md (TPL-09), config-*.yaml, README.md
├── results/                  # csv/json hasil, analysis.md
├── figures/                  # figur final (+ skrip pembuatnya)
├── paper/                    # proposal TA / manuscript
└── presentation/             # slide pitch W8/W16 (TPL-13)
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
[jenis metode + 1 kalimat desain; lihat docs/research-design.md]

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
Seed: [n] · Config: `experiments/config-*.yaml` · Hardware: [isi] · Waktu: [isi]
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
| Preprocessing | skrip `src/data/…`, urutan langkah, versi hasil |
| Split | train/val/test atau pilot/eval; cara membagi; file daftar ID split |
| Sampel | `data/sample-synthetic.csv` (≤ 100 baris, tanpa data pribadi) |
| Yang TIDAK ada di repo | data mentah, data pribadi, kredensial (`.gitignore`: data/raw/, *.key, .env) |
```

## Isi minimal `experiments/README.md`

```markdown
# Experiments — [Research ID]
| ID | Nama | RQ | Status | Config | Hasil | Kartu |
|---|---|---|---|---|---|---|
| EXP-01 | [pilot …] | RQ1 | [selesai/berjalan] | config-01.yaml | results/exp-01.csv | EXP-01-….md |
Cara menjalankan satu eksperimen: `python -m src.run --config experiments/config-01.yaml --seed 42`
Konvensi: satu kartu (TPL-09) per eksperimen; pra-registrasi tidak diubah setelah run; hasil ke results/, figur ke figures/.
```

## Skrip cepat membuat struktur

```bash
# ganti nilai di baris pertama, lalu jalankan di folder kerja
REPO=proj-2026-ai-academic-advising; RID=UIAI-2026-001; TITLE="AI-assisted academic advising for Indonesian universities"
mkdir -p "$REPO"/{docs,data,src,notebooks,experiments,results,figures,paper,presentation} && cd "$REPO" && git init -q
printf '# %s\n\n## Research ID\n%s\n' "$TITLE" "$RID" > README.md
for f in problem research-question literature-map research-design ethics AI-USAGE ai-usage-log one-pager; do printf '# %s — %s\n' "$f" "$RID" > "docs/$f.md"; done
printf '# Data — %s\n(metadata saja; data mentah tidak di-commit)\n' "$RID" > data/README.md
printf '# Experiments — %s\n' "$RID" > experiments/README.md
printf 'data/raw/\n*.key\n.env\n__pycache__/\n.ipynb_checkpoints/\n' > .gitignore
printf '# Changelog\n\n## v0.1 Problem Validated — [YYYY-MM-DD]\n' > CHANGELOG.md
printf 'cff-version: 1.2.0\nmessage: "Cite this research repository."\ntitle: "%s"\nauthors:\n  - family-names: "[isi]"\n    given-names: "[isi]"\n    affiliation: "Universitas Al-Azhar Indonesia"\nidentifiers:\n  - type: other\n    value: "%s"\nlicense: Apache-2.0\n' "$TITLE" "$RID" > CITATION.cff
touch requirements.txt references.bib run.sh && chmod +x run.sh
# salin LICENSE (Apache-2.0) dan LICENSE-DOCS (CC BY 4.0) dari repo uai-ai-research-center, lalu:
git add -A && git commit -qm "Scaffold research repository ($RID)" && git checkout -qb research/g1-endgame
```

## Contoh terisi (cuplikan README `proj-2026-ai-academic-advising`)

**Research ID** UIAI-2026-001 · Issue #[n] · Cluster C3 · Domain Education · Entry door Problem. **Problem** Dosen wali menangani puluhan mahasiswa dengan waktu terbatas; pelanggaran prasyarat dan keterlambatan lulus. **Research Question** RQ1 validitas rekomendasi LLM+RAG vs rule-based; RQ2 penilaian dosen wali. **Dataset** DS-2026-001 (UAI, restricted, 120 transkrip anonim) + 40 kasus sintetis di `data/sample-synthetic.csv`. **Baseline** rule-based prerequisite checker (`src/baseline/`). **Evaluation Metrics** constraint-violation rate, precision@5, Likert; ambang 10 poin persen. **Research Status** TA Ready — v1.0 (2026-12-[dd]). **Current Research Gate** G8 – Contribution Ready — lulus 2026-12-[dd]. **Researchers** [Mahasiswa A] (@[isi]) — lead; [Mahasiswa B] — eksperimen; mentor [Dosen C3]. **Related Course** Metopen semester VII → TA. **Publications** belum ada (target [konferensi nasional — isi]). **Reproducibility** `bash run.sh`, seed 42, Python 3.11; reproduksi peer [Mahasiswa C] 2026-10-[dd] (violation 7,9 %). **AI Usage Disclosure** AI dipakai untuk kata kunci pencarian, debugging parser, kritik desain, koreksi bahasa; tidak untuk data/hasil/referensi tanpa verifikasi; 3 referensi usulan AI dibuang; log 14 entri. **License** Code Apache-2.0 · Docs CC-BY-4.0 · Dataset restricted (DS-2026-001) · Model weights not released · Paper —.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| README | Orang yang datang tiga tahun kemudian mengerti masalah, klaim, status, cara menjalankan | README berisi cara install saja |
| Data | `data/README.md` lengkap; data mentah tidak di-commit; sampel sintetis kecil | CSV transkrip mahasiswa di repo |
| Reproducibility | `run.sh` + environment + seed + config; reproduksi peer tercatat | Notebook dengan path absolut laptop |
| Gate & release | Branch/PR/release mengikuti konvensi; Current Research Gate diperbarui | Semua kerja di `main` tanpa PR |
| Lisensi | Tabel per komponen terisi | Tanpa LICENSE |
| Kebersihan | Notebook eksplorasi dipisah dari `src/`; figur punya skrip | Hasil final hanya di notebook |
