# GOVERNANCE — Tata Kelola GitHub UAI AI Research Center

> Dokumen ini mengatur **bagaimana repository/organization ini dijalankan**: struktur, tim, hak akses, skema identitas, taksonomi, dan Research Mission Control. Tata kelola akademik (peran Kaprodi, RACI, KPI) ada di [`research-os/07-governance/`](research-os/07-governance/01-governance-model.md). Definisi istilah mengikuti [Glossary (MST-03)](research-os/00-master/03-glossary.md).

## 1. Prinsip

1. **Organisasi berdasarkan sistem, bukan orang.** Tidak ada `repo-pak-x` atau `repo-mahasiswa-y`. Struktur mengikuti Strategy → Research Infrastructure → Research Programs → Research Projects → Education → Outputs → Community; orang menjadi owner/contributor.
2. **GitHub adalah research operating system**, bukan sekadar code hosting: *institutional research memory + collaboration platform + reproducibility infrastructure*.
3. **Research ID adalah primary key.** Satu `UIAI-YYYY-NNN` mengikat backlog → Issue → repositori → Metopen → TA → dataset → publikasi → HKI.
4. **Workflow dulu, automation kemudian.** Otomasi (GitHub Actions) baru dibangun setelah alur manual stabil.
5. **Data sensitif tidak pernah masuk GitHub.** Lihat [SECURITY.md](SECURITY.md).

## 2. Peta repository

Saat ini seluruh *launch set* hidup sebagai folder dalam satu repository (monorepo). Setiap folder dirancang agar dapat dipecah menjadi repository terpisah di GitHub Organization `UAI-AI-Research` tanpa penulisan ulang.

| Komponen (calon repo) | Folder saat ini | Fungsi | Akses |
|---|---|---|---|
| `.github` | `.github/` | Front door: profil, issue forms, PR templates, labels, workflows | PUBLIC |
| `research-os` | `research-os/` | *How we research*: framework, gates, protokol AI, etika, template, rubrik | PUBLIC |
| `research-roadmap` | `research-roadmap/` | *What we research*: klaster, domain, alignment | PUBLIC |
| `research-backlog` | `research-backlog/` + Issues | *What could be researched next*: problem bank | PUBLIC (Issue) |
| `datasets-registry` | `datasets-registry/` | Katalog metadata dataset (dataset fisik di server/HF/Kaggle/Drive) | PUBLIC (metadata) |
| `research-based-learning` | `research-based-learning/` | Mata kuliah → research pipeline | PUBLIC |
| `metopen-research-studio` | `metopen-research-studio/` | Halaman mingguan Metopen (View B mahasiswa) | PUBLIC |
| `publications` | `publications/` | Registry metadata publikasi | PUBLIC |
| `program-<nama>` | *(belum dibuat)* | Program riset 5–10 tahun (mis. `program-ai-education`, `program-responsible-ai`) | PUBLIC/INTERNAL |
| `proj-YYYY-<topik>` | *(dibuat per riset)* | Riset individual 3–12 bulan, struktur standar [TPL-15](research-os/08-templates/15-research-repository-template.md) | INTERNAL → PUBLIC saat rilis |

Aturan penamaan project: `proj-2026-ai-student-readiness`, `proj-2026-indonesian-rag-evaluation`, `proj-2027-halal-image-classification`. **Bukan** `final-project-baru-v2-fix`.

## 3. Tim (GitHub Teams)

Berdasarkan peran:

| Team | Anggota | Hak umum |
|---|---|---|
| `@directors` | Kepala pusat riset, Kaprodi | Admin organization |
| `@research-leads` | Ketua klaster/program | Maintain repo program & project klasternya |
| `@faculty` | Dosen | Write pada project yang dimentori; triage backlog |
| `@researchers` | Peneliti/asisten riset | Write pada project |
| `@students` | Mahasiswa aktif riset | Write pada project sendiri; read lainnya |
| `@reviewers` | Reviewer gate/manuscript (dosen + peer terlatih) | Review PR gate |
| `@maintainers` | Pemelihara research-os, templates, workflows | Maintain repo inti |

Berdasarkan klaster: `@ai-models` (C1), `@ai-systems` (C2), `@responsible-ai` (C3), `@applied-ai` (C4). Seseorang dapat berada di beberapa tim sekaligus, misalnya `faculty + ai-systems + reviewers`.

## 4. Model izin (permission)

| Klasifikasi | Isi | Visibilitas repo | Siapa boleh menulis |
|---|---|---|---|
| **PUBLIC** | Framework, kode publik, metadata dataset publik, publikasi, template, materi belajar | Public | `@maintainers` via PR; kontributor via fork/PR |
| **INTERNAL** | Riset berjalan, naskah belum terbit, pekerjaan mahasiswa, roadmap internal | Private/Internal | Tim project + mentor |
| **RESTRICTED** | Data partner rahasia, dataset sensitif, data pribadi, proyek komersial | Tidak di GitHub (hanya metadata) | Sesuai perjanjian partner / komite etik |

Branch `main` pada repo inti dilindungi: perubahan lewat PR + minimal 1 review `@maintainers`.

## 5. Skema identitas

| Jenis | Format | Diberikan oleh | Dicatat di |
|---|---|---|---|
| Research ID | `UIAI-YYYY-NNN` | `@maintainers` saat Issue backlog divalidasi (G2) | `research-backlog/BACKLOG.md`, judul Issue, README riset |
| Dataset ID | `DS-YYYY-NNN` | Pengelola datasets-registry | `datasets-registry/REGISTRY.md` |
| Publication ID | `PUB-YYYY-NNN` | Pengelola publications | `publications/PUBLICATIONS.md` |
| Artifact ID | `ART-YYYY-NNN` | Pengelola publications/AI Center | `publications/PUBLICATIONS.md` (bagian artefak) |

Relasi contoh:

```
UIAI-2026-023
├─ Dataset      DS-2026-014
├─ Artifact     ART-2026-008
└─ Publication  PUB-2027-001
```

Nomor urut `NNN` diberikan berurutan per tahun dan **tidak pernah dipakai ulang**, meskipun riset dibatalkan.

## 6. Taksonomi

### 6.1 Label Issue/PR

Sumber tunggal: [`.github/labels.yml`](.github/labels.yml). Kelompok: `type:*`, `gate:G1…G8`, `cluster:*`, `P0…P3`, `status:*`, `maturity:*`.

### 6.2 Topics repository (controlled vocabulary)

`artificial-intelligence`, `machine-learning`, `nlp`, `computer-vision`, `responsible-ai`, `education`, `halal`, `health`, `food`, `government`, `business`, `social-impact`, `indonesia`, `uai`, `student-research`, `faculty-research`, `dataset`, `publication`, `research-methods`.

Penambahan topic baru diusulkan lewat PR ke dokumen ini.

### 6.3 Branch & release

- Branch riset: `research/g1-endgame`, `research/g2-problem`, … `research/g8-contribution`; branch kerja lain: `feat/…`, `exp/…`, `paper/…`.
- Release = milestone riset: `v0.1` Problem Validated, `v0.2` Evidence Ready, `v0.3` Research Design, `v0.5` Pilot Experiment, `v0.8` Manuscript Draft, `v1.0` Research Pack, `v1.1` Submitted, `v2.0` Published.

## 7. Issue sebagai unit riset

Issue **bukan hanya bug**. Jenis Issue (form di `.github/ISSUE_TEMPLATE/`):

| Jenis | Pertanyaan | Label |
|---|---|---|
| Research Problem | Apa problemnya? | `type:problem` |
| Research Question | Pertanyaan apa yang perlu diuji? | `type:research-question` |
| Dataset | Dataset apa yang tersedia/dibutuhkan? | `type:dataset` |
| Experiment | Eksperimen apa? | `type:experiment` |
| Literature Gap | Gap apa yang teridentifikasi? | `type:literature-gap` |
| Publication | Paper mana yang sedang disiapkan? | `type:publication` |
| Research Risk | Bottleneck-nya apa? | `type:research-risk` |
| Bug | Kesalahan kode/dokumen | `type:bug` |

Dengan ini seluruh proses riset menjadi *searchable* dan *traceable*.

## 8. Pull Request sebagai research review

PR bukan hanya code review. Jenis review: **Problem Review (G2), Evidence Review (G3), Method Review (G5), Experiment Review (G6), Manuscript Review (G8), Release Review**. Template ada di `.github/PULL_REQUEST_TEMPLATE/`. Reviewer: dosen, mentor, peer reviewer. Merge = gate lulus. Detail alur: [CONTRIBUTING.md](CONTRIBUTING.md).

## 9. Research Mission Control (GitHub Projects)

Satu Organization Project bernama **UAI AI Research Mission Control** menjadi master tracker. Item: Research Project / Research Task / Publication.

**Fields**

| Field | Nilai |
|---|---|
| Research ID | `UIAI-2026-023` |
| Title | … |
| Cluster | C1–C4 |
| Domain | Education / Halal / Health / Food / Government / Business / Social Impact |
| Researcher | … |
| Faculty Mentor | … |
| Entry Door | Problem / Dataset / Faculty Research / Course Project / Partner / Competition |
| Course | AI/ML / Data Mining / NLP / RPL / Metopen / TA / — |
| Research Gate | G1–G8 |
| Maturity | Idea / TA Ready / Research Ready / Publication Ready / Impact Ready |
| Priority | P0–P3 |
| Publication Target | venue |
| Due | tanggal |
| Status | Active / Blocked / Review / Done |
| Next Evidence | bukti berikutnya yang harus ada |

**Views**

1. **Research Pipeline** (board): Idea → Problem Ready → Evidence Ready → Question Ready → Method Ready → Experiment Ready → Claim Ready → Contribution Ready → Published/Released. Inilah leaderboard substantif.
2. **By Research Cluster**: C1 AI Models · C2 AI Systems · C3 Human-Centered · C4 Applied.
3. **By Course**: AI/ML · Data Mining · Metopen · TA.
4. **Publication Pipeline**: Research → Writing → Internal Review → Submission Ready → Submitted → Revision → Accepted → Published.
5. **Faculty Portfolio**: riset per dosen pemilik (untuk BKD, pelaporan riset, perencanaan hibah, akreditasi, evaluasi roadmap).

Catatan: GitHub tetap **research tracking system**, bukan sistem kepegawaian. Leaderboard mengurutkan **kematangan riset**, bukan orang ([TPL-03](research-os/08-templates/03-research-leaderboard-template.md)).

## 10. Fase implementasi GitHub

| Fase | Fokus | Output |
|---|---|---|
| **0 — Foundation** | Organization, `.github`, governance, README, taksonomi, Research ID | ✅ repo ini |
| **1 — Research OS** | Seluruh framework masuk `research-os`, roadmap, templates, gates | ✅ repo ini |
| **2 — Pilot Metopen** | Mahasiswa semester VII masuk | Research Issues, One-Pagers, repo project, gate reviews |
| **3 — Curriculum Integration** | AI/ML dan MK lain menghasilkan research assets | folder `research-based-learning/courses/*` terisi artefak riil |
| **4 — AI Center Launch** | Klaster dosen, lintas fakultas, problem partner | repo `program-*`, Faculty Portfolio |
| **5 — Public Research Portal** | GitHub menjadi portofolio publik Pusat Riset AI | dashboard otomatis, website |

Otomasi tahap lanjut (setelah manual stabil): auto-scaffold repo riset baru, auto-update status saat PR gate merge, auto-update registry publikasi, ringkasan portofolio mingguan.

## 11. Perubahan dokumen tata kelola

Perubahan pada GOVERNANCE.md, LICENSING.md, taksonomi label/topics, dan glossary diajukan lewat PR, direview `@maintainers`, dan dicatat di [CHANGELOG.md](CHANGELOG.md).
