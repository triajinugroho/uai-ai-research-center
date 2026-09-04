# UAI AI Research Center

**Universitas Al-Azhar Indonesia AI Research Center** · Program Studi Informatika
*Human-Centered, Responsible and Impact-Driven Artificial Intelligence Research.*
**Advancing AI for Knowledge, Humanity and Impact.**

> Repository ini bukan tempat menyimpan source code. Ia adalah **research operating system** — *institutional research memory + collaboration platform + reproducibility infrastructure* — yang menghubungkan:
>
> **Research Center → Dosen → Mata Kuliah → Mahasiswa → Problem → Dataset → Project → Metopen → TA → Paper → Publikasi / HKI / Produk → Research Center lagi.**

Status: **v0.1.0 — Phase 0 Foundation + Phase 1 Research OS** (lihat [CHANGELOG](CHANGELOG.md)). Dokumen bahasa Indonesia dengan istilah teknis dalam English.

---

## Who We Are

Pusat riset AI Informatika UAI yang menjadikan kurikulum sebagai penghasil *reusable research assets*, AI sebagai payung tematik sekaligus *cognitive accelerator*, Metodologi Penelitian sebagai *evidence-quality gate*, Tugas Akhir sebagai *contribution stage*, dan pusat riset sebagai *institutional engine* yang menghubungkan seluruh siklus itu dengan dosen, roadmap UAI, problem industri/nasional, dan publikasi. Signature kami: **amanah epistemik** — mencari kebenaran, bukan membela hipotesis.

## Research Mission

Responsible, human-centered, impact-driven AI: riset yang menghasilkan *credible knowledge* dan artefak yang dapat direproduksi, bermanfaat bagi Indonesia, dan dipertanggungjawabkan secara ilmiah, etis, dan profesional.

## Research Clusters

| Kode | Klaster | Contoh arah |
|---|---|---|
| C1 | **AI Models, Data & Knowledge** | Indonesian NLP, representasi pengetahuan, evaluasi model, data-centric AI |
| C2 | **AI Systems, Software & Security** | MLOps, rekayasa perangkat lunak untuk AI, keamanan & keandalan sistem AI |
| C3 | **Human-Centered & Responsible AI** | HCI untuk AI, fairness, privasi, explainability, AI dalam pendidikan |
| C4 | **Applied AI for Human Flourishing** | Pendidikan, halal, kesehatan, pangan, pemerintahan, bisnis, dampak sosial |

Detail: [Research Roadmap](research-roadmap/README.md) · [AIR-02 AI Research Clusters](research-os/03-ai-research-ecosystem/02-ai-research-clusters.md).

## Research Pipeline

**Discover → Build → Prove → Contribute → Scale**

Setiap riset melewati **8 Research Gates**: G1 Endgame · G2 Problem · G3 Evidence · G4 Question · G5 Method · G6 Experiment · G7 Claim · G8 Contribution ([OPS-03](research-os/06-execution-os/03-research-gates.md)). Issue adalah unit riset, Pull Request adalah *research review*, Release adalah milestone kematangan riset, dan GitHub Projects adalah **Research Mission Control** ([GOVERNANCE](GOVERNANCE.md)).

## Current Portfolio

| Pipeline | Jumlah |
|---|---|
| Idea (backlog) | lihat [research-backlog/BACKLOG.md](research-backlog/BACKLOG.md) |
| Problem Ready → Contribution Ready | 0 — pilot Metopen dimulai Phase 2 |
| Published / Released | 0 |

Angka akan diperbarui manual setiap sprint; otomasi via GitHub Actions menyusul setelah alur stabil.

## Peta Repository

Repository ini adalah **monorepo** yang meniru *launch set* GitHub Organization (7 repo inti + studio Metopen). Setiap folder dapat dipecah menjadi repository terpisah tanpa penulisan ulang.

| Folder | Menjawab | Mulai dari |
|---|---|---|
| [`research-os/`](research-os/README.md) | **How do we research?** — framework, gates, protokol AI, etika, rubrik, 15 template | [Executive Summary](research-os/00-master/01-executive-summary.md) · [One-Page Concept](research-os/00-master/02-one-page-concept.md) · [Glossary](research-os/00-master/03-glossary.md) |
| [`research-roadmap/`](research-roadmap/README.md) | **What should we research?** — 4 klaster, 7 domain, alignment UAI/Indonesia/global 2026–2030 | [Roadmap 2026–2030](research-roadmap/2026-2030/README.md) |
| [`research-backlog/`](research-backlog/README.md) | **What could be researched next?** — problem bank (Issues + indeks) | [BACKLOG.md](research-backlog/BACKLOG.md) |
| [`datasets-registry/`](datasets-registry/README.md) | Katalog metadata dataset (data fisik di luar GitHub) | [REGISTRY.md](datasets-registry/REGISTRY.md) |
| [`research-based-learning/`](research-based-learning/README.md) | Mata kuliah → research pipeline (mode F/E/R), panduan dosen & mahasiswa | [Student Guide](research-based-learning/student-guide/README.md) · [Faculty Guide](research-based-learning/faculty-guide/README.md) |
| [`metopen-research-studio/`](metopen-research-studio/README.md) | Metodologi Penelitian sebagai Research Studio — halaman mingguan W1–W16 untuk mahasiswa | [Week 01](metopen-research-studio/weeks/week-01-endgame.md) |
| [`publications/`](publications/README.md) | Registry metadata publikasi & artefak | [PUBLICATIONS.md](publications/PUBLICATIONS.md) |
| [`.github/`](.github/) | Issue forms, PR templates (gate review), label taxonomy, workflows | [labels.yml](.github/labels.yml) |
| [`tools/`](tools/) | `check_links.py`, `build_wbs.py` | — |

Repo `program-<nama>` (program riset 5–10 tahun) dan `proj-YYYY-<topik>` (riset 3–12 bulan) dibuat **hanya ketika isi riilnya ada**, memakai [template repositori riset](research-os/08-templates/15-research-repository-template.md).

## Dua cara membaca

| View | Untuk | Jalur |
|---|---|---|
| **A — Institutional** | Kaprodi, Dekan, pimpinan, tim PP-PTS, reviewer | Strategy → Architecture → Governance → Impact: [`research-os/01`](research-os/01-strategic-foundation/) → [`02`](research-os/02-academic-architecture/) → [`03`](research-os/03-ai-research-ecosystem/) → [`07`](research-os/07-governance/) |
| **B — Student Execution** | Mahasiswa | This Week → Tasks → Evidence → Gate → Next: [`metopen-research-studio/weeks/`](metopen-research-studio/weeks/) + [Student Weekly Playbook](research-os/06-execution-os/05-student-weekly-playbook.md) |

## For Students

1. Baca [Student Guide](research-based-learning/student-guide/README.md) dan [AI Research Protocol](research-os/05-ai-augmented-research/04-ai-research-protocol.md).
2. Pilih atau usulkan masalah lewat Issue **Research Problem** ([backlog](research-backlog/README.md)).
3. Buat repositori riset dari [template](research-os/08-templates/15-research-repository-template.md), lalu ikuti [Week 01](metopen-research-studio/weeks/week-01-endgame.md).

## For Researchers (Dosen)

1. Baca [Faculty Guide](research-based-learning/faculty-guide/README.md) dan [Faculty Research Alignment](research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md).
2. Tandai mata kuliah Anda dengan mode **F / E / R** ([ARC-03](research-os/02-academic-architecture/03-ai-contribution-modes.md)).
3. Daftarkan masalah/dataset ke backlog dan registry; jadilah mentor/reviewer gate.

## For Partners

Industri, pemerintah, dan masyarakat dapat mengajukan masalah lewat Issue **Research Problem** atau menghubungi pusat riset. Model kolaborasi: **Domain Problem + Data + AI Capability + Evaluation + Impact** ([AIR-04](research-os/03-ai-research-ecosystem/04-cross-faculty-ai-model.md), [AIR-05](research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)). Data partner tidak pernah disimpan mentah di GitHub ([SECURITY](SECURITY.md)).

## Tata kelola & lisensi

[GOVERNANCE](GOVERNANCE.md) · [CONTRIBUTING](CONTRIBUTING.md) · [CODE OF CONDUCT](CODE_OF_CONDUCT.md) · [SECURITY](SECURITY.md) · [LICENSING](LICENSING.md) · [CITATION](CITATION.cff)

Kode: [Apache-2.0](LICENSE). Dokumen & materi: [CC BY 4.0](LICENSE-DOCS). Dataset: case-by-case. Aset ber-HKI: restricted sampai IP review.

## Asal dokumen

Seluruh desain diturunkan dari dokumen diskusi *"Riset AI UAI untuk Negeri"* ([`research-os/00-master/source/`](research-os/00-master/source/)). Fakta institusional di dalamnya (akreditasi, struktur kurikulum, benchmark kampus lain) perlu diverifikasi ulang sebelum dipakai dalam dokumen formal.

Maintainer: [@triajinugroho](https://github.com/triajinugroho) — Program Studi Informatika, Universitas Al-Azhar Indonesia.
