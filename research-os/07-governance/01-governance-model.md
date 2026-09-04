# Governance Model — Peran, RACI, dan Ritme

> **ID** GOV-01 · **Paket** 07 Governance & Implementation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, kepala AI Research Center, tim kurikulum, koordinator MK, dosen, mentor, admin riset; mahasiswa (bagian peran & ritme)
> **Terkait** [GOVERNANCE.md](../../GOVERNANCE.md) · [GOV-02 Implementation Roadmap](02-implementation-roadmap.md) · [GOV-03 KPI](03-kpi-and-measurement.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [STR-03 Design Principles](../01-strategic-foundation/03-design-principles.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md)

[GOVERNANCE.md](../../GOVERNANCE.md) di root mengatur **tata kelola GitHub** (repo, team, akses, label, Mission Control). Dokumen ini mengatur **tata kelola akademik**: siapa memegang peran apa, siapa bertanggung jawab atas aktivitas apa (RACI), forum apa yang berjalan dengan ritme apa, dan bagaimana peran akademik dipetakan ke GitHub Teams. Keduanya saling melengkapi; jika bertentangan, definisi istilah mengikuti [MST-03](../00-master/03-glossary.md).

Prinsip yang mengikat: **organisasi berdasarkan sistem, bukan orang** — peran melekat pada fungsi, seseorang boleh memegang beberapa peran, dan pergantian orang tidak mengubah alur.

---

## 1. Peran dan tanggung jawab

| Peran | Siapa | Tanggung jawab utama | Bukan tanggung jawabnya |
|---|---|---|---|
| **Kaprodi** | Ketua Program Studi Informatika | Menetapkan kebijakan (positioning Metopen, Research Pack sebagai proposal TA, AI policy, pengakuan beban mentor); menyetujui dokumen Tier 1; memimpin evaluasi semester; pemilik akhir KPI dan risk register | Mereview gate riset satu per satu |
| **Curriculum team** (tim kurikulum) | Dosen yang ditugaskan Prodi | Merevisi RPS AI/ML, Metopen, TA mengikuti paket 02/04/05; memetakan CPL–CPMK–artefak ([ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md)); menandai mode F/E/R MK; memvalidasi rubrik 5E | Mengoperasikan repository harian |
| **AI Research Center** | Kepala pusat riset + research leads klaster C1–C4 | Memelihara roadmap dan backlog; memvalidasi problem (triage) dan memberi Research ID bersama maintainer; matching mentor–tim; mengelola program `program-*`, Faculty Portfolio, hubungan partner, IP review, publikasi/hibah | Menilai mata kuliah |
| **MK coordinator** (koordinator mata kuliah) | Koordinator AI/ML, Data Mining, NLP, RPL, dsb. | Memastikan MK mode E/R menghasilkan research asset (`research-artifact.md`, Issue backlog, dataset terdaftar); handoff Course → Metopen | Membimbing riset sampai G8 |
| **Lecturer** (dosen pengampu Metopen) | Pengampu Metopen semester berjalan | Menjalankan studio 16 minggu; reviewer utama G1–G3 dan G5–G8; memimpin sprint review mingguan, red team W8, defense W16; menilai rubrik 5E; memutuskan integrity gate | Menjadi mentor substantif semua tim |
| **Research mentor** (dosen mentor riset) | Dosen dari klaster yang cocok (≤5 tim per mentor) | Reviewer G4–G8; menjaga keselarasan dengan riset dosen/klaster; membuka pintu skema penelitian internal; calon pembimbing TA | Mengerjakan eksperimen mahasiswa |
| **TA supervisor** (pembimbing TA) | Dosen pembimbing semester VIII | Menerima handoff G8; melanjutkan gate G6–G8 dengan data penuh; mengarahkan ke Published/Released; mencatat kelanjutan Research ID | Meminta topik baru jika Research Pack valid |
| **Student** (mahasiswa / tim riset) | Tim 1–3 mahasiswa Metopen/TA | Menjalankan sprint; membuka PR gate; menulis AI Usage Log; peer review dan peer reproduction untuk tim lain; menandatangani integrity checklist; memiliki (owns) setiap klaim | Menunggu instruksi untuk memulai gate berikutnya |
| **Admin / research assistant** (admin riset, asisten riset; `@maintainers`) | Staf/asisten yang ditunjuk | Memelihara repo inti, template, label, workflow; memberi Research ID; mengelola registry dataset/publikasi; menjalankan ekspor evidence dan laporan KPI; menjaga SLA review; verifikasi fakta institusional | Mengambil keputusan akademik |

Catatan: satu orang dapat memegang beberapa peran (dosen pengampu Metopen yang juga mentor dan research lead klaster). Yang dilarang hanya **self-review**: reviewer sebuah gate tidak boleh anggota tim yang direview.

## 2. RACI matrix

R = Responsible (mengerjakan) · A = Accountable (memutuskan/bertanggung jawab akhir, tepat satu per baris) · C = Consulted · I = Informed.

Kolom: **KP** Kaprodi · **CT** Curriculum team · **AC** AI Research Center · **MC** MK coordinator · **LC** Lecturer Metopen · **RM** Research mentor · **TS** TA supervisor · **ST** Student · **AD** Admin/research assistant.

| # | Aktivitas | KP | CT | AC | MC | LC | RM | TS | ST | AD |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Menetapkan kebijakan & RPS Metopen (positioning, Research Pack, 5E, AI policy) | A | R | C | C | C | I | I | I | I |
| 2 | Menandai mode F/E/R dan research asset MK teknis | I | A | C | R | I | I | I | I | I |
| 3 | Validasi backlog (triage Issue `type:problem`, keselarasan klaster/domain) | I | I | A | C | R | C | I | R | C |
| 4 | Pemberian Research ID `UIAI-YYYY-NNN` saat lolos G2 | I | I | C | I | C | I | I | I | A/R |
| 5 | Matching mentor–tim (faculty research matching) | C | I | A | I | R | C | I | I | R |
| 6 | Gate review G1–G3 (Endgame, Problem, Evidence) | I | I | I | I | A/R | C | I | R | I |
| 7 | Gate review G4 (Question) | I | I | I | I | A | R | I | R | I |
| 8 | Red team review W8 / gate review G5 (Method) | I | I | C | I | A | R | I | R | I |
| 9 | Gate review G6–G7 (Experiment, Claim) termasuk peer reproduction | I | I | I | I | A | R | I | R | I |
| 10 | Research Defense W16 / gate review G8 (Contribution) | I | I | C | I | A | R | C | R | I |
| 11 | Handoff Metopen → TA (dan Course → Metopen, TA → AI Center) | I | I | C | R | R | C | A | R | I |
| 12 | Registrasi dataset (`DS-`), lisensi & privasi | I | I | A | C | I | C | I | R | R |
| 13 | Registrasi publikasi (`PUB-`), pemilihan venue, submission | I | I | A | I | C | R | R | R | R |
| 14 | IP review & penetapan lisensi artefak (`ART-`) / HKI | C | I | A | I | I | R | R | C | R |
| 15 | Pelaporan KPI semester & ekspor evidence (PP-PTS, akreditasi, hibah) | A | C | R | C | R | I | I | I | R |
| 16 | Review risk register & penanganan insiden integritas | A | C | R | I | R | C | C | I | R |
| 17 | Pemeliharaan research-os, template, label, workflow (PR ke `main`) | C | C | C | I | C | I | I | I | A/R |
| 18 | Pembaruan Mission Control (field gate, maturity, status) | I | I | C | I | C | I | I | R | A |

Aturan penerapan:

1. Setiap baris memiliki tepat satu **A**. Jika dua peran ingin sama-sama memutuskan, eskalasi ke Kaprodi.
2. **R** untuk mahasiswa berarti mahasiswa mengerjakan dan membuka PR; **A** pada dosen berarti dosen memutuskan lulus/gagal dengan alasan tertulis (aturan 4 di [OPS-03](../06-execution-os/03-research-gates.md)).
3. Integritas riset: siapa pun (termasuk mahasiswa) wajib melaporkan dugaan pelanggaran; penanganan mengikuti baris 16 dan [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md).

## 3. Alur keputusan (siapa memutuskan apa)

| Jenis keputusan | Pemutus | Mekanisme | Dicatat di |
|---|---|---|---|
| Kebijakan Prodi (Tier 1 v1.0, AI policy, pengakuan beban) | Kaprodi | Rapat Prodi; PR ke dokumen Tier 1 | CHANGELOG, notulen Prodi |
| Lulus/gagal gate | Reviewer A pada baris RACI | Merge/close PR `GATE REVIEW:*` dengan komentar | PR, label `gate:*`, Mission Control |
| Research ID, dataset ID, publication ID | Admin riset / pengelola registry | Sesuai [GOVERNANCE.md §5](../../GOVERNANCE.md) | Registry, judul Issue |
| Lisensi artefak / HKI | AI Research Center bersama `@directors` | IP review singkat ([LICENSING.md §6](../../LICENSING.md)) | README riset, registry |
| Perubahan template/glossary | `@maintainers` | PR + review | CHANGELOG |
| Insiden integritas | Kaprodi (A), dosen pengampu + AI Center (R) | Prosedur [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md) | Catatan internal (bukan repo publik) |

## 4. Forum dan ritme

| Forum | Frekuensi | Peserta | Agenda tetap | Output |
|---|---|---|---|---|
| **Sprint review mingguan** | Setiap minggu W1–W16 (dalam jam studio) | Dosen pengampu, semua tim; mentor bila hadir | Per tim ≤10 menit: deliverable sprint, blocker, AI Usage Log, next sprint | Status Mission Control diperbarui; Issue `type:research-risk` untuk blocker |
| **Gate review** | Asinkron, saat PR `GATE REVIEW:*` dibuka; SLA 5 hari kerja | Reviewer sesuai RACI (dosen, mentor, peer) | Periksa terhadap *definition of done*; tulis apa yang kurang & bukti apa yang dibutuhkan | Merge (lulus) atau request changes (revisi) |
| **Design Defense / Red Team** | Sekali, W8 | Dosen pengampu, mentor, dosen lain, peer | Pitch 7–10 menit + serangan terhadap desain, baseline, metrik, validitas | Notulen red team; keputusan G5 |
| **Research Defense** | Sekali, W16 | Dosen pengampu, mentor, penguji | Pertanggungjawaban Research Pack | Keputusan G8; handoff ditandatangani |
| **Rapat bulanan Research Ops** | Bulanan | Kaprodi, dosen pengampu, AI Research Center, admin riset, koordinator MK terkait | Pipeline (board Research Pipeline), item blocked, SLA review, risiko baru, kebutuhan mentor | Notulen; tindakan di Issue |
| **Evaluasi semester** | Akhir semester | Kaprodi, tim kurikulum, AI Research Center, dosen pengampu, admin riset | KPI vs target, lessons learned, revisi RPS/template, keputusan scale-up fase berikutnya ([GOV-02](02-implementation-roadmap.md)) | Laporan KPI; PR revisi dokumen; CHANGELOG |
| **Review tahunan roadmap & evidence** | Tahunan | Kaprodi, kepala AI Research Center, tim PP-PTS/akreditasi | Roadmap 2026–2030, Faculty Portfolio, ekspor evidence ([GOV-05](05-ppts-and-institutional-evidence.md)), risk register | Roadmap diperbarui; paket evidence |

SLA yang dipegang: gate review ≤5 hari kerja; jawaban blocker mahasiswa ≤2 hari kerja pada sprint review berikutnya; Research ID diberikan ≤2 hari kerja setelah G2 merge.

## 5. Hubungan dengan GitHub Teams

Peran akademik di dokumen ini dipetakan ke tim GitHub di [GOVERNANCE.md §3](../../GOVERNANCE.md). Satu orang bisa masuk beberapa tim.

| Peran akademik | GitHub Team | Hak yang menyertai |
|---|---|---|
| Kaprodi, kepala AI Research Center | `@directors` | Admin organization; persetujuan IP review |
| Research leads klaster (AI Research Center) | `@research-leads` + `@ai-models`/`@ai-systems`/`@responsible-ai`/`@applied-ai` | Maintain repo program & project klasternya; triage backlog |
| Curriculum team, MK coordinator, lecturer, research mentor, TA supervisor | `@faculty` (+ tim klaster) | Write pada project yang dimentori; triage backlog |
| Reviewer gate (dosen, mentor, peer terlatih) | `@reviewers` | Review PR gate; wajib untuk merge PR `GATE REVIEW:*` |
| Student | `@students` | Write pada project sendiri; read lainnya |
| Research assistant / peneliti | `@researchers` | Write pada project |
| Admin riset / maintainer | `@maintainers` | Maintain repo inti; memberi Research ID; merge ke `main` |

Aturan branch dan PR (`research/gN-*`, `GATE REVIEW:`, merge = lulus) mengikuti [CONTRIBUTING.md](../../CONTRIBUTING.md). Field Mission Control (Research Gate, Maturity, Faculty Mentor, Status, Next Evidence) adalah sumber data utama forum di §4 dan KPI di [GOV-03](03-kpi-and-measurement.md).

## 6. Onboarding peran

| Peran | Yang harus dibaca | Yang harus bisa dilakukan sebelum semester |
|---|---|---|
| Lecturer Metopen | Paket 04, 06, 08; [`metopen-research-studio/`](../../metopen-research-studio/README.md) | Membuka/mereview PR gate; mengisi rubrik 5E; memimpin red team |
| Research mentor | [OPS-03](../06-execution-os/03-research-gates.md), [MET-04](../04-metopen-research-studio/04-research-pack-specification.md), [TPL-14](../08-templates/14-research-handoff-template.md), [AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md) | Mereview G4–G8; mengisi faculty research map |
| MK coordinator | [ARC-03](../02-academic-architecture/03-ai-contribution-modes.md), [ARC-04](../02-academic-architecture/04-build-prove-contribute.md), [`research-based-learning/faculty-guide/`](../../research-based-learning/faculty-guide/README.md) | Menghasilkan `research-artifact.md` dan Issue backlog dari proyek MK |
| Student | [OPS-05](../06-execution-os/05-student-weekly-playbook.md), [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md), [`student-guide/`](../../research-based-learning/student-guide/README.md) | Membuat repo dari [TPL-15](../08-templates/15-research-repository-template.md); membuka Issue dan PR; mengisi AI Usage Log |
| Admin riset | [GOVERNANCE.md](../../GOVERNANCE.md), [CONTRIBUTING.md](../../CONTRIBUTING.md), [GOV-05](05-ppts-and-institutional-evidence.md), template registry paket 08 | Memberi ID; mengekspor evidence; menjalankan `tools/check_links.py` |

Fase pemberlakuan peran-peran ini mengikuti [GOV-02 Implementation Roadmap](02-implementation-roadmap.md): pada pilot, peran mentor dan admin riset boleh dirangkap; pemisahan penuh terjadi pada Phase 4.
