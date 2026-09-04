# Research OS — Master Navigation

> **ID** MST-00 · **Paket** 00 Master / Executive Navigation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, Dekan, pimpinan universitas, tim PP-PTS, tim AI Research Center, tim kurikulum, reviewer internal, dosen, mahasiswa (sebagai pintu masuk)
> **Terkait** [MST-01 Executive Summary](01-executive-summary.md) · [MST-02 One-Page Concept](02-one-page-concept.md) · [MST-03 Glossary](03-glossary.md) · [Research OS README](../README.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

Dokumen ini adalah **landing page** paket master. Tujuannya satu: siapa pun dapat memahami keseluruhan sistem tanpa membaca 57 file. Jika Anda hanya punya lima menit, baca [MST-02 One-Page Concept](02-one-page-concept.md). Jika Anda punya tiga puluh menit, baca [MST-01 Executive Summary](01-executive-summary.md). Jika Anda akan mengambil keputusan, lanjutkan ke paket 01 dan 07.

---

## 1. Apa repository `research-os/` ini

`research-os/` adalah **sistem operasi riset** Program Studi Informatika Universitas Al-Azhar Indonesia (UAI). Ia menjawab satu pertanyaan: **"How do we research?"** Isinya bukan kode aplikasi, melainkan framework, gate kualitas, protokol AI, etika, rubrik, roadmap implementasi, KPI, dan template yang dipakai bersama oleh dosen, mahasiswa, mentor, dan pusat riset.

Ia dibedakan dari dua komponen lain di monorepo yang sama:

| Komponen | Pertanyaan | Lokasi |
|---|---|---|
| **Research OS** | *How do we research?* | [`research-os/`](../README.md) |
| **Research Roadmap** | *What should we research?* | [`research-roadmap/`](../../research-roadmap/README.md) |
| **Research Backlog** | *What could be researched next?* | [`research-backlog/`](../../research-backlog/README.md) |

Nama internal sistem yang dijelaskan seluruh paket ini: **UIRP — UAI Informatics Research Pipeline**. Nama institusional untuk dokumen formal: *UAI Informatics Research-Based Learning & AI Ecosystem*.

## 2. Tujuan

1. Menjadi **single source of truth**. Dari repository ini diturunkan dokumen formal Prodi, RPS AI/ML–Metopen–TA, concept paper AI Research Center, lecturer playbook, student playbook, dashboard riset, dan repository template. Tidak ada "RPS versi 5 di Drive tetapi GitHub versi 3".
2. Menyatukan yang selama ini terfragmentasi: proyek mata kuliah, Metopen, TA, riset dosen, dataset, roadmap, dan publikasi ke dalam **satu pipeline** dengan satu bahasa dan satu skema identitas.
3. Menjadikan Metodologi Penelitian sebagai **evidence-quality gate** dan Tugas Akhir sebagai **contribution stage**, dengan AI sebagai payung tematik sekaligus *cognitive accelerator* yang tetap *human-accountable*.
4. Menghasilkan **evidence institusional** (OBE, PjBL, PP-PTS, akreditasi) sebagai efek samping alur kerja, bukan sebagai pekerjaan tambahan.

Formula yang diimplementasikan semua paket ini dituliskan utuh di [Research OS README](../README.md). Satu kalimatnya: *UAI Informatics membangun scientific thinkers melalui kurikulum yang menghasilkan reusable research assets.*

## 3. Cara membaca (per audiens)

| Anda adalah | Mulai dari | Lanjutkan ke | Boleh dilewati |
|---|---|---|---|
| **Pimpinan** (Kaprodi, Dekan, Rektorat) — 30 menit | [MST-02](02-one-page-concept.md) → [MST-01](01-executive-summary.md) | [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) → [GOV-02 Roadmap](../07-governance/02-implementation-roadmap.md) → [GOV-03 KPI](../07-governance/03-kpi-and-measurement.md) | Paket 05, 06, 08 |
| **Tim PP-PTS / akreditasi / reviewer hibah** | [STR-04 Alignment Map](../01-strategic-foundation/04-alignment-map.md) | [STR-05](../01-strategic-foundation/05-theory-of-change.md) → [GOV-05 PP-PTS Evidence](../07-governance/05-ppts-and-institutional-evidence.md) → [GOV-04 Risk Register](../07-governance/04-risk-register.md) | Paket 06, 08 |
| **Tim kurikulum / dosen** | [STR-01 Current State](../01-strategic-foundation/01-current-state-and-gaps.md) → [STR-03 Design Principles](../01-strategic-foundation/03-design-principles.md) | Paket [02](../02-academic-architecture/01-research-capability-spiral.md) → [03](../03-ai-research-ecosystem/01-ai-research-center-concept.md) → [04](../04-metopen-research-studio/01-metopen-positioning.md) → [05](../05-ai-augmented-research/01-research-meta-thinking.md) | Paket 08 kecuali TPL-07 |
| **Dosen pengampu Metopen** | Paket [04](../04-metopen-research-studio/01-metopen-positioning.md) | Paket [06](../06-execution-os/03-research-gates.md) → [08](../08-templates/01-research-one-pager-template.md) → [`metopen-research-studio/`](../../metopen-research-studio/README.md) | Paket 03 (cukup AIR-02) |
| **Mentor riset / TA supervisor** | [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) | [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) → [TPL-14 Handoff](../08-templates/14-research-handoff-template.md) → [AIR-03 Faculty Alignment](../03-ai-research-ecosystem/03-faculty-research-alignment.md) | Paket 01, 07 |
| **Mahasiswa** | [OPS-05 Student Weekly Playbook](../06-execution-os/05-student-weekly-playbook.md) | [`metopen-research-studio/weeks/`](../../metopen-research-studio/weeks/week-01-endgame.md) → [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) → template paket 08 sesuai minggu | Paket 01, 03, 07 |
| **Admin riset / maintainer** | [GOVERNANCE.md](../../GOVERNANCE.md) → [CONTRIBUTING.md](../../CONTRIBUTING.md) | [GOV-01 Governance Model](../07-governance/01-governance-model.md) → [GOV-05](../07-governance/05-ppts-and-institutional-evidence.md) → registry template paket 08 | Paket 05 |

Aturan praktis: **Tier 1 wajib dibaca pembuat kebijakan, Tier 2 tim kurikulum, Tier 3 dipakai saat dibutuhkan.** Tier setiap dokumen tercantum di blok metadata pada baris pertama.

## 4. Struktur sembilan paket

| Paket | Folder | Prefix | Tier | Menjawab | Jumlah file |
|---|---|---|---|---|---|
| 00 Master / Executive Navigation | [`00-master/`](.) | MST | 1 | Bagaimana membaca semuanya? | 4 |
| 01 Strategic Foundation | [`01-strategic-foundation/`](../01-strategic-foundation/01-current-state-and-gaps.md) | STR | 1 | Mengapa perubahan ini perlu, ke mana arahnya, prinsip apa yang mengikat? | 5 |
| 02 Academic Architecture | [`02-academic-architecture/`](../02-academic-architecture/01-research-capability-spiral.md) | ARC | 2 | Bagaimana riset ditanamkan dalam perjalanan empat tahun mahasiswa? | 6 |
| 03 AI Research Ecosystem | [`03-ai-research-ecosystem/`](../03-ai-research-ecosystem/01-ai-research-center-concept.md) | AIR | 1–2 | Bagaimana pusat riset, dosen, klaster, lintas fakultas, dan partner menjadi satu ekosistem? | 5 |
| 04 Metopen Research Studio | [`04-metopen-research-studio/`](../04-metopen-research-studio/01-metopen-positioning.md) | MET | 2 | Bagaimana Metopen 2 SKS didesain sebagai studio, apa deliverable dan rubriknya? | 7 |
| 05 AI-Augmented Research & Meta-Thinking | [`05-ai-augmented-research/`](../05-ai-augmented-research/01-research-meta-thinking.md) | AIX | 2 | Meta-skill, kompetensi AI, protokol AI, dan tool apa yang dilatih? | 5 |
| 06 Execution Operating System | [`06-execution-os/`](../06-execution-os/03-research-gates.md) | OPS | 3 (OPS-03: 1) | 145 microtask, 17 sprint, 8 gate, critical path, playbook mingguan | 5 (+CSV) |
| 07 Governance & Implementation | [`07-governance/`](../07-governance/01-governance-model.md) | GOV | 1 | Siapa melakukan apa, KPI, roadmap, risiko, evidence institusional | 5 |
| 08 Templates & Toolkit | [`08-templates/`](../08-templates/01-research-one-pager-template.md) | TPL | 3 | 15 template executable | 15 |

Total 57 dokumen: ±10 Tier 1, ±15 Tier 2, ±30 Tier 3.

## 5. Hubungan antar dokumen (peta ketergantungan)

Paket disusun mengikuti urutan pembangunan; dokumen hilir tidak boleh bertentangan dengan dokumen hulu.

```
                 ┌──────────────────────────────────────────────┐
                 │  00 MASTER  (MST)  — navigasi, ringkasan, kamus │
                 └───────────────┬──────────────────────────────┘
                                 │ mendefinisikan istilah & ID untuk semua
                                 ▼
   ┌──────────────────── 01 STRATEGIC FOUNDATION (STR) ────────────────────┐
   │ STR-01 gap → STR-02 endgame → STR-03 prinsip → STR-04 alignment → STR-05 ToC │
   └──────────────┬──────────────────────────────┬──────────────────────────┘
                  │ arsitektur                    │ ekosistem
                  ▼                               ▼
   ┌── 02 ACADEMIC ARCHITECTURE (ARC) ──┐   ┌── 03 AI RESEARCH ECOSYSTEM (AIR) ──┐
   │ spiral · MK map · F/E/R · B→P→C   │◄─►│ center · klaster C1–C4 · dosen ·   │
   │ CPL–CPMK–artifact · taksonomi     │   │ lintas fakultas · marketplace      │
   └──────────────┬─────────────────────┘   └──────────────┬─────────────────────┘
                  │ Metopen = "Prove"                       │ problem & mentor
                  ▼                                         │
   ┌── 04 METOPEN RESEARCH STUDIO (MET) ─────────────────────▼─────────────────┐
   │ positioning · outcomes · 16 minggu · Research Pack · publikasi · 5E · etika │
   └──────────────┬──────────────────────────────────────────┬─────────────────┘
                  │ kompetensi & protokol AI                   │ dieksekusi lewat
                  ▼                                            ▼
   ┌── 05 AI-AUGMENTED RESEARCH (AIX) ──┐        ┌── 06 EXECUTION OS (OPS) ──────┐
   │ meta-thinking · 4 level · value    │───────►│ WBS 145 task · 17 sprint ·    │
   │ stream · protokol · tools          │        │ 8 gate · critical path ·      │
   └────────────────────────────────────┘        │ playbook mingguan             │
                                                 └──────────────┬────────────────┘
                                                                │ diisi dengan
                                                                ▼
   ┌── 07 GOVERNANCE (GOV) ─────────────┐        ┌── 08 TEMPLATES (TPL) ─────────┐
   │ peran/RACI · roadmap · KPI · risiko│◄──────►│ 15 template: one-pager, tracker│
   │ · PP-PTS evidence                  │        │ registry, card, checklist, …  │
   └────────────────────────────────────┘        └───────────────────────────────┘
```

Tiga simpul yang paling sering dirujuk lintas paket:

- [MST-03 Glossary](03-glossary.md) — definisi tunggal semua istilah, skema ID, gate, klaster, tier.
- [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) — *definition of done* delapan gerbang yang dipakai rubrik (MET-06), WBS (OPS-01), PR template (`.github/`), dan KPI (GOV-03).
- [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) — deliverable akhir Metopen yang menjadi input TA, handoff, dan publikasi.

Cara merujuk: sebutkan ID lalu link, misalnya *"mengikuti Research Gate G5 sebagaimana [MET-04](../04-metopen-research-studio/04-research-pack-specification.md) dan [OPS-03](../06-execution-os/03-research-gates.md)"*.

## 6. Versioning

| Status | Arti | Siapa yang boleh mengubah |
|---|---|---|
| **Draft v0.1** | Ditulis dari dokumen diskusi; fakta institusional belum diverifikasi; struktur dapat berubah | `@maintainers` lewat PR |
| **Review v0.5** | Telah dibaca tim kurikulum / Kaprodi; menunggu keputusan yang tercantum di [MST-01 §Decision needed](01-executive-summary.md) | PR + review tim kurikulum |
| **Adopted v1.0** | Disahkan Prodi sebagai rujukan RPS/kebijakan; perubahan berikutnya berupa minor/patch | PR + review `@maintainers` + persetujuan Kaprodi untuk Tier 1 |

Aturan:

1. Seluruh perubahan lewat **Pull Request**, bukan edit langsung di `main` (lihat [CONTRIBUTING.md](../../CONTRIBUTING.md)).
2. Perubahan yang mengubah makna (definisi istilah, gate, rubrik, KPI, peran) dicatat di [CHANGELOG.md](../../CHANGELOG.md) dan menaikkan versi minor; perbaikan tipografi/link cukup patch.
3. Perubahan pada [MST-03 Glossary](03-glossary.md) wajib diikuti pembaruan semua dokumen yang memakai istilah tersebut.
4. Versi repository (`v0.1.0` di CHANGELOG) dan status dokumen (`Draft v0.1` di blok metadata) berjalan bersama: dokumen Tier 1 naik ke v1.0 bersamaan dengan rilis repository v1.0.
5. Dokumen turunan (DOCX formal, RPS, playbook) mencantumkan versi dokumen sumbernya. Master tetap di GitHub.

## 7. Glossary singkat (10 istilah terpenting)

Definisi lengkap dan mengikat ada di [MST-03 Glossary](03-glossary.md). Sepuluh istilah berikut cukup untuk membaca paket 00, 01, dan 07.

| Istilah | Arti singkat |
|---|---|
| **Evidence Engineering** | Jiwa sistem: riset adalah rekayasa bukti agar klaim dapat dipercaya, bukan produksi dokumen akademik. |
| **Research Studio** | Positioning Metopen: ±30% konsep + 70% studio; mahasiswa menjalankan satu *mini research cycle* dan proposal TA lahir sebagai konsekuensinya. |
| **Build → Prove → Contribute** | Mata kuliah teknis membangun research asset; Metopen membuktikan kualitas bukti; TA berkontribusi pengetahuan/artefak. |
| **Research Asset** | Hasil MK/riset yang bisa dipakai ulang: dataset, kode, benchmark, model, literature map, problem brief. *Research assets should compound.* |
| **Research Pack** | Deliverable akhir Metopen: 16 komponen dari Problem Brief sampai Research Pitch ([MET-04](../04-metopen-research-studio/04-research-pack-specification.md)). |
| **Research Gate (G1–G8)** | Delapan gerbang kualitas: Endgame, Problem, Evidence, Question, Method, Experiment, Claim, Contribution ([OPS-03](../06-execution-os/03-research-gates.md)). |
| **Research ID** | `UIAI-YYYY-NNN`, primary key yang mengikat backlog → Issue → repo → Metopen → TA → dataset → publikasi → HKI. |
| **Maturity** | Idea → TA Ready → Research Ready → Publication Ready → Impact Ready. |
| **AI-augmented, human-accountable science** | AI adalah research copilot, bukan otoritas epistemik; setiap output AI diverifikasi dan diungkap. |
| **Amanah epistemik** | Signature UAI: kejujuran terhadap kebenaran meskipun kebenaran itu meruntuhkan hipotesis sendiri; bahasa modernnya *research integrity*. |

## 8. Skema ID (ringkas)

| Jenis | Format | Contoh | Catatan |
|---|---|---|---|
| Dokumen Research OS | `PREFIX-NN` | `STR-01`, `GOV-04` | Prefix = paket (MST, STR, ARC, AIR, MET, AIX, OPS, GOV, TPL) |
| Task WBS | `OPS-NNN` | `OPS-042` | Tiga digit; berbeda dari dokumen `OPS-01`…`OPS-05` |
| Sprint | `S0`…`S16` | `S6` | S0 onboarding; S1–S16 = minggu 1–16 |
| Gate | `G1`…`G8` | `G5` | Label GitHub `gate:G5-method` |
| Research | `UIAI-YYYY-NNN` | `UIAI-2026-001` | Diberikan saat lolos G2 |
| Dataset / Publikasi / Artefak | `DS-` / `PUB-` / `ART-YYYY-NNN` | `DS-2026-001` | Registry masing-masing |
| Risiko | `RSK-NN` | `RSK-03` | [GOV-04](../07-governance/04-risk-register.md) |
| KPI | `KPI-L/I/G-NN` | `KPI-L-01` | Leading / Intermediate / laGging, [GOV-03](../07-governance/03-kpi-and-measurement.md) |

Nomor urut tidak pernah dipakai ulang. Detail: [MST-03 §6](03-glossary.md) dan [GOVERNANCE.md §5](../../GOVERNANCE.md).

## 9. Dua view: satu backend, dua pengalaman

| View | Untuk | Alur | Pintu masuk |
|---|---|---|---|
| **View A — Institutional** | Pimpinan, tim PP-PTS, reviewer, tim kurikulum | Strategy → Architecture → Governance → Impact | Paket [01](../01-strategic-foundation/01-current-state-and-gaps.md) → [02](../02-academic-architecture/01-research-capability-spiral.md) → [03](../03-ai-research-ecosystem/01-ai-research-center-concept.md) → [07](../07-governance/01-governance-model.md) |
| **View B — Student Execution** | Mahasiswa | This Week → Tasks → Evidence → Gate → Next | [`metopen-research-studio/weeks/`](../../metopen-research-studio/weeks/week-01-endgame.md) + [OPS-05](../06-execution-os/05-student-weekly-playbook.md) |

Pimpinan tidak perlu melihat 145 microtask. Mahasiswa tidak perlu membaca theory of change PP-PTS. Keduanya membaca sistem yang sama.

## 10. Yang perlu diketahui sebelum mengutip

- Fakta institusional (akreditasi, tabel kurikulum, skema penelitian internal, benchmark kampus lain) berasal dari dokumen diskusi *"Riset AI UAI untuk Negeri"* ([`source/`](source/)) dan diberi keterangan **"sumber: dokumen diskusi; verifikasi sebelum dokumen formal"**. Jangan mengutipnya ke dokumen resmi tanpa verifikasi.
- Nama dosen dan dataset riil memakai placeholder `[isi]` sampai data sebenarnya masuk lewat registry.
- Lisensi: dokumen ini CC BY 4.0, kode Apache-2.0 ([LICENSING.md](../../LICENSING.md)).

Langkah berikutnya bagi pembaca baru: [MST-02 One-Page Concept](02-one-page-concept.md).
