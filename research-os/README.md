# Research OS — UAI AI Research Operating System

> **How do we research?** Repository ini adalah *single source of truth* tentang bagaimana UAI melakukan riset: research lifecycle, research gates, protokol AI, etika, template, rubrik, metodologi, dan tata kelola. Dari sini diturunkan dokumen formal Prodi, RPS, concept paper AI Research Center, lecturer playbook, student playbook, dashboard, dan repository template — bukan ditulis ulang dari nol.

Nama internal sistem: **UIRP — UAI Informatics Research Pipeline**. Nama institusional: *UAI Informatics Research-Based Learning & AI Ecosystem*.

## Formula

**UAI Informatics membangun scientific thinkers melalui kurikulum yang menghasilkan reusable research assets; AI menjadi leading thematic umbrella sekaligus cognitive accelerator; Metodologi Penelitian menjadi evidence-quality gate; Tugas Akhir menjadi contribution stage; dan AI Research Center menjadi institutional engine yang menghubungkan seluruh siklus tersebut dengan dosen, roadmap UAI, problem industri/nasional, serta publikasi.**

Semua dokumen di bawah hanyalah implementasi dari formula itu.

## Tujuh layer berpikir → sembilan paket

| Layer | Pertanyaan | Paket |
|---|---|---|
| 1 Why | Mengapa Metopen perlu direposisi? | 01 |
| 2 Endgame | Mahasiswa seperti apa yang ingin dihasilkan? | 01 |
| 3 Academic Architecture | Bagaimana AI/ML → Metopen → TA → publikasi terhubung? | 02 |
| 4 Ecosystem Architecture | Bagaimana MK, dosen, roadmap UAI, pusat riset, industri, prioritas nasional masuk? | 03 |
| 5 Learning & Thinking Architecture | Scientific thinking, meta-thinking, research & AI competency apa yang dilatih? | 04, 05 |
| 6 Execution Architecture | Weekly sprint, gates, tasks, rubrik, tracker, backlog? | 06, 08 |
| 7 Governance & Scale | Siapa melakukan apa, KPI, implementasi, evidence institusional? | 07 |

## Indeks paket

| Paket | Folder | Prefix ID | Tier | Isi |
|---|---|---|---|---|
| 00 Master / Executive Navigation | [`00-master/`](00-master/) | MST | 1 | [README](00-master/00-readme.md) · [Executive Summary](00-master/01-executive-summary.md) · [One-Page Concept](00-master/02-one-page-concept.md) · [Glossary](00-master/03-glossary.md) |
| 01 Strategic Foundation | [`01-strategic-foundation/`](01-strategic-foundation/) | STR | 1 | [Current State & Gaps](01-strategic-foundation/01-current-state-and-gaps.md) · [Vision & Endgame](01-strategic-foundation/02-vision-and-endgame.md) · [Design Principles](01-strategic-foundation/03-design-principles.md) · [Alignment Map](01-strategic-foundation/04-alignment-map.md) · [Theory of Change](01-strategic-foundation/05-theory-of-change.md) |
| 02 Academic Architecture | [`02-academic-architecture/`](02-academic-architecture/) | ARC | 2 | [Capability Spiral](02-academic-architecture/01-research-capability-spiral.md) · [Curriculum Research Map](02-academic-architecture/02-curriculum-research-map.md) · [AI Contribution Modes](02-academic-architecture/03-ai-contribution-modes.md) · [Build–Prove–Contribute](02-academic-architecture/04-build-prove-contribute.md) · [CPL–CPMK–Artifact](02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [Output Taxonomy](02-academic-architecture/06-research-output-taxonomy.md) |
| 03 AI Research Ecosystem | [`03-ai-research-ecosystem/`](03-ai-research-ecosystem/) | AIR | 1–2 | [AI Research Center Concept](03-ai-research-ecosystem/01-ai-research-center-concept.md) · [Clusters](03-ai-research-ecosystem/02-ai-research-clusters.md) · [Faculty Alignment](03-ai-research-ecosystem/03-faculty-research-alignment.md) · [Cross-Faculty Model](03-ai-research-ecosystem/04-cross-faculty-ai-model.md) · [Demand–Supply Marketplace](03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) |
| 04 Metopen Research Studio | [`04-metopen-research-studio/`](04-metopen-research-studio/) | MET | 2 | [Positioning](04-metopen-research-studio/01-metopen-positioning.md) · [Course Outcomes](04-metopen-research-studio/02-metopen-course-outcomes.md) · [16-Week Blueprint](04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [Research Pack](04-metopen-research-studio/04-research-pack-specification.md) · [Publication Backward Design](04-metopen-research-studio/05-publication-backward-design.md) · [5E Rubric](04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [Integrity & Ethics](04-metopen-research-studio/07-research-integrity-and-ethics.md) |
| 05 AI-Augmented Research & Meta-Thinking | [`05-ai-augmented-research/`](05-ai-augmented-research/) | AIX | 2 | [Meta-Thinking](05-ai-augmented-research/01-research-meta-thinking.md) · [AI Competency](05-ai-augmented-research/02-ai-research-competency-framework.md) · [AI Across Value Stream](05-ai-augmented-research/03-ai-across-research-value-stream.md) · [AI Research Protocol](05-ai-augmented-research/04-ai-research-protocol.md) · [AI Tools Reference](05-ai-augmented-research/05-ai-tools-reference.md) |
| 06 Execution Operating System | [`06-execution-os/`](06-execution-os/) | OPS | 3 | [Research WBS](06-execution-os/01-research-wbs-master.md) · [Weekly Sprints](06-execution-os/02-weekly-sprints.md) · [Research Gates](06-execution-os/03-research-gates.md) · [Dependency & Critical Path](06-execution-os/04-dependency-and-critical-path.md) · [Student Weekly Playbook](06-execution-os/05-student-weekly-playbook.md) |
| 07 Governance & Implementation | [`07-governance/`](07-governance/) | GOV | 1 | [Governance Model](07-governance/01-governance-model.md) · [Implementation Roadmap](07-governance/02-implementation-roadmap.md) · [KPI](07-governance/03-kpi-and-measurement.md) · [Risk Register](07-governance/04-risk-register.md) · [PP-PTS Evidence](07-governance/05-ppts-and-institutional-evidence.md) |
| 08 Templates & Toolkit | [`08-templates/`](08-templates/) | TPL | 3 | 15 template executable: one-pager, tracker, leaderboard, backlog, dataset & venue registry, faculty map, design card, experiment card, AI usage log, integrity checklist, peer review, defense, handoff, repository template |

Total 57 dokumen. Tier 1 (17) wajib dibaca pembuat kebijakan; Tier 2 (21) untuk tim kurikulum/dosen; Tier 3 (19) sebagian besar template (hitungan per blok metadata; estimasi awal dokumen sumber ±10/±15/±30).

## Urutan baca yang disarankan

1. **Pimpinan (30 menit):** [One-Page Concept](00-master/02-one-page-concept.md) → [Executive Summary](00-master/01-executive-summary.md) → [Theory of Change](01-strategic-foundation/05-theory-of-change.md) → [Implementation Roadmap](07-governance/02-implementation-roadmap.md) → [KPI](07-governance/03-kpi-and-measurement.md).
2. **Tim kurikulum/dosen:** paket 01 → 02 → 03 → 04 → 05.
3. **Dosen pengampu Metopen:** paket 04 → 06 → 08, lalu [`metopen-research-studio/`](../metopen-research-studio/README.md).
4. **Mahasiswa:** [Student Weekly Playbook](06-execution-os/05-student-weekly-playbook.md) → [`metopen-research-studio/weeks/`](../metopen-research-studio/weeks/) → paket 08 sesuai kebutuhan.

## Urutan pembangunan (dependency)

```
STEP 1 Master thesis (why + endgame + principles)      → 00, 01
STEP 2 Academic architecture + AI ecosystem              → 02, 03
STEP 3 Metopen design (course + pack + assessment)       → 04
STEP 4 Meta-thinking + AI (competency + tools + protocol)→ 05
STEP 5 Execution (145 microtasks, 17 sprints, 8 gates)   → 06
STEP 6 Governance (roles + KPI + implementation)         → 07
STEP 7 Templates (tracker, backlog, leaderboard, …)      → 08
STEP 8 Compile → DOCX formal, RPS, playbooks, dashboard
```

## Artefak turunan

Dari repository ini dapat dikompilasi: (1) Dokumen Formal Prodi *Kerangka Akademik UAI Informatics Research-Based Learning & AI Ecosystem*; (2) Proposal/Concept Paper AI Research Center (paket 01 + 03 + 07); (3) Paket revisi RPS AI/ML, Metopen, TA (paket 02 + 04 + 05); (4) Lecturer Playbook; (5) Student Research Playbook "Dari nol sampai Research Pack"; (6) Research Dashboard/Google Sheet (paket 06 + 08); (7) Research Repository Template. Master-nya tetap di GitHub — tidak ada "RPS versi 5 di Drive tetapi GitHub versi 3".

## Konvensi

Lihat [Glossary (MST-03)](00-master/03-glossary.md) untuk istilah, skema ID, gate, dan tier; [`CLAUDE.md`](../CLAUDE.md) dan [CONTRIBUTING](../CONTRIBUTING.md) untuk konvensi penulisan.

Dokumen asal: [`00-master/source/riset-ai-uai-untuk-negeri.docx`](00-master/source/).
