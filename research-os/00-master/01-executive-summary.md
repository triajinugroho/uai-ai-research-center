# Executive Summary — UAI Informatics Research Pipeline (UIRP)

> **ID** MST-01 · **Paket** 00 Master / Executive Navigation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, Dekan, pimpinan universitas, tim PP-PTS, kepala AI Research Center, rapat pimpinan Prodi
> **Terkait** [MST-00 README](00-readme.md) · [MST-02 One-Page Concept](02-one-page-concept.md) · [STR-01 Current State & Gaps](../01-strategic-foundation/01-current-state-and-gaps.md) · [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) · [GOV-02 Implementation Roadmap](../07-governance/02-implementation-roadmap.md)

Dokumen ini adalah bahan rapat pimpinan: 2–4 halaman, dibaca dalam 15 menit, diakhiri daftar keputusan yang perlu disepakati Prodi. Rincian teknis ada di paket 01–08; dokumen ini sengaja tidak mengulangnya.

---

## 1. Problem

Program Studi Informatika UAI sudah memiliki modal yang cukup: statistika di semester I–II, basis data dan HCI di semester III, algoritma, RPL, dan data mining di semester IV, AI & Machine Learning 4 SKS di semester V, proyek perangkat lunak dan kerja praktik di semester VI, Metodologi Penelitian 2 SKS di semester VII, dan Tugas Akhir 4 SKS di semester VIII (*sumber: dokumen diskusi; verifikasi sebelum dokumen formal*). Masalahnya bukan kekurangan materi. Masalahnya adalah **fragmentasi**: kemampuan teknis tidak berubah menjadi pengetahuan baru yang *evidence-based*.

Enam fragmentasi yang terlihat:

| # | Fragmentasi | Gejala |
|---|---|---|
| 1 | **Course project fragmented** | Proyek AI/ML, Data Mining, RPL selesai sebagai nilai mata kuliah; kode, data, dan temuannya tidak dipakai ulang oleh siapa pun. |
| 2 | **Metopen–TA fragmented** | Metopen menghasilkan proposal di atas kertas; mahasiswa masuk semester VIII masih mencari judul dan metode. |
| 3 | **Faculty–student research fragmented** | Riset dosen dan riset mahasiswa berjalan di jalur terpisah; mahasiswa jarang menjadi bagian riset dosen secara terstruktur. |
| 4 | **Dataset fragmented** | Dataset tersebar di laptop pribadi, tidak terkatalog, tidak diketahui lisensinya, tidak bisa diwariskan. |
| 5 | **Roadmap disconnect** | Topik TA dan proyek MK tidak terhubung ke roadmap riset Prodi/Renstra Penelitian UAI. |
| 6 | **AI use without research literacy** | Mahasiswa sudah memakai GenAI, tetapi tanpa protokol verifikasi; risiko referensi fiktif, klaim tanpa bukti, dan proposal yang "terdengar ilmiah". |

Akibat gabungannya: TA berkualitas rendah dengan pola *solution-first* ("saya ingin memakai Random Forest untuk memprediksi X"), publikasi mahasiswa minim, dan setiap angkatan memulai dari nol. Analisis lengkap: [STR-01](../01-strategic-foundation/01-current-state-and-gaps.md).

## 2. Opportunity

Tiga peluang terbuka pada saat yang sama.

1. **Posisi kurikulum sudah tepat.** AI/ML (semester V) → Metopen (semester VII) → TA (semester VIII) adalah urutan alami *Build → Prove → Contribute*. Metopen berada pada posisi *integration layer* atas enam semester kompetensi dan *launchpad* menuju TA. Tidak perlu mengubah struktur kurikulum untuk memulai.
2. **Skema penelitian internal UAI 2026 mendorong keterlibatan mahasiswa.** Pada call yang ditemukan, minimal dua mahasiswa aktif UAI dilibatkan, dan topik diarahkan selaras Renstra Penelitian universitas (*sumber: dokumen diskusi; verifikasi sebelum dokumen formal*). Metopen dapat menjadi **talent funnel** penelitian dosen.
3. **Status akreditasi memberi alasan institusional.** UAI berstatus Unggul; Informatika berstatus Baik Sekali berdasarkan SK LAM-INFOKOM 2025 yang berlaku sampai Maret 2030 (*sumber: dokumen diskusi; verifikasi sebelum dokumen formal*). Satu mata kuliah tidak menaikkan akreditasi, tetapi pipeline mahasiswa → TA → riset dosen → publikasi → artefak → reputasi → evidence akreditasi adalah *compounding loop* yang dapat dimulai dari satu titik kendali.

## 3. Solution: UAI Informatics Research Pipeline (UIRP)

UIRP adalah satu pipeline yang menghubungkan **Research Center → dosen → mata kuliah → mahasiswa → problem → dataset → project → Metopen → TA → paper → publikasi/HKI/produk → Research Center lagi**.

Perubahan intinya ada pada Metopen: dari "kuliah tentang penelitian" menjadi **Research Studio** (±30% konsep + 70% studio) dengan positioning internal *AI-Augmented Research Methods & Evidence Engineering for Informatics*. Mahasiswa tidak belajar membuat proposal selama satu semester; mereka menjalankan satu *mini research cycle*, dan proposal TA lahir sebagai konsekuensinya.

Deliverable akhirnya bukan `Proposal.pdf`, melainkan **UAI Informatics Research Pack** — 16 komponen dari Problem Brief, Literature Evidence Map, Research Gap, RQ, Research Design, Data Plan, Baseline & Metrics, Pilot Experiment, Threats to Validity, Ethics & Privacy, AI Usage Statement, Reproducibility README, hingga Proposal TA dan Research Pitch ([MET-04](../04-metopen-research-studio/04-research-pack-specification.md)).

North star: **100% mahasiswa selesai Metopen sudah TA-ready; mahasiswa terbaik research/publication-ready.**

## 4. Architecture

```
        BUILD                    PROVE                     CONTRIBUTE
  Mata kuliah teknis   ──►   Metopen (Research Studio) ──►   Tugas Akhir
  AI/ML, Data Mining,        16 minggu · 17 sprint ·         eksekusi penuh dari
  NLP, RPL, dsb.             145 microtask · 8 gate          Research Pack
  menghasilkan               menghasilkan                    menghasilkan
  RESEARCH ASSET             RESEARCH PACK                   PAPER / DATASET /
  (dataset, kode,            (v1.0 release)                  ARTEFAK / HKI / PRODUK
  benchmark, problem brief)
```

Tiga mekanisme yang membuat arsitektur ini berjalan:

- **Delapan Research Gates** ([OPS-03](../06-execution-os/03-research-gates.md)): G1 Endgame Ready → G2 Problem Ready → G3 Evidence Ready → G4 Question Ready → G5 Method Ready → G6 Experiment Ready → G7 Claim Ready → G8 Contribution Ready. Setiap gate memiliki *definition of done*, bukti wajib, reviewer, dan kriteria lulus/gagal. Gate direview lewat Pull Request; merge = lulus.
- **Research Pack sebagai satu-satunya deliverable** yang menjadi input langsung pembimbing TA, tanpa mengulang dari nol.
- **GitHub sebagai research operating system**: Issue adalah unit riset, PR adalah review ilmiah, Release adalah milestone kematangan, GitHub Projects adalah Research Mission Control, dan `UIAI-YYYY-NNN` adalah primary key yang mengikat semuanya ([GOVERNANCE.md](../../GOVERNANCE.md)).

Dua pembeda yang membuat desain ini khas UAI: **AI-augmented, human-accountable science** (setiap output AI melalui source → reasoning → evidence verification → human accountability; [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)) dan **reproducibility** (repository, bukan dokumen, sebagai artefak riset). Signature nilainya: **amanah epistemik** — mencari kebenaran, bukan membela hipotesis.

## 5. Institutional leverage

Satu alur kerja menghasilkan evidence untuk banyak keperluan sekaligus (*one activity, multiple outcomes*):

| Tuntutan institusional | Apa yang UIRP hasilkan secara otomatis |
|---|---|
| **OBE / CPL / CPMK** | Setiap gate = asesmen autentik dengan artefak terukur; rubrik 5E (End, Evidence, Experiment, Explanation, Execution) memetakan CPMK → artefak → evidence ([ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md), [MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)). |
| **PjBL / Team-Based Project** | Tim 1–3 mahasiswa, sprint mingguan, deliverable per sprint, peer review, defense. |
| **PP-PTS** | Mapping Activity → RPS → Project → Evidence → KPI → dokumentasi; evidence diekspor dari Issue, PR, release, registry ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)). |
| **AI Research Center** | Backlog masalah, klaster C1–C4, dataset registry, dan Faculty Portfolio memberi pusat riset pipeline mahasiswa yang siap pakai ([AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md)). |
| **Penelitian dosen** | Mahasiswa TA-ready adalah kandidat "minimal dua mahasiswa" untuk skema penelitian internal; riset dosen menjadi entry door riset mahasiswa ([AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md)). |
| **Publikasi & HKI** | Publication backward design dari TA-ready → manuscript-ready → submission-ready → submitted → accepted → published ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)); registry `publications/`. |

Compounding loop: **satu mata kuliah → TA lebih baik → mahasiswa lebih capable → riset dosen lebih kuat → publikasi → reputasi prodi → kolaborasi → problem lebih berkualitas → mahasiswa berikutnya mendapat research environment lebih baik.** Diagram sebab-akibatnya ada di [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md).

## 6. Decision needed

Berikut keputusan konkret yang perlu disepakati Prodi agar pilot dapat berjalan. Setiap butir dapat diputuskan terpisah; butir 1–3 adalah prasyarat minimum.

| # | Keputusan | Opsi yang diusulkan | Dokumen rujukan | Pemilik keputusan |
|---|---|---|---|---|
| 1 | **Positioning Metopen** sebagai Research Studio (±30% konsep + 70% studio) dengan nama formal tetap Metodologi Penelitian 2 SKS | Setujui positioning; RPS direvisi mengikuti 16-week blueprint | [MET-01](../04-metopen-research-studio/01-metopen-positioning.md), [MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md) | Kaprodi + tim kurikulum |
| 2 | **Research Pack sebagai deliverable resmi** Metopen sekaligus dokumen proposal TA yang diakui | Research Pack v1.0 menggantikan proposal terpisah; pembimbing TA memulai dari Research Pack | [MET-04](../04-metopen-research-studio/04-research-pack-specification.md), [ARC-04](../02-academic-architecture/04-build-prove-contribute.md) | Kaprodi + koordinator TA |
| 3 | **Gate & rubrik 5E** sebagai instrumen penilaian; Research Integrity sebagai gate lulus/gagal, bukan skor | Adopsi 8 gate + rubrik 5E + integrity gate | [OPS-03](../06-execution-os/03-research-gates.md), [MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) | Tim kurikulum |
| 4 | **AI policy** Prodi untuk riset mahasiswa: AI diperbolehkan dengan protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own dan AI Usage Log wajib | Adopsi AIX-04 sebagai kebijakan Prodi; selaras kebijakan publikasi ACM | [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md), [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md) | Kaprodi |
| 5 | **Repositori riset** GitHub sebagai wadah resmi (Issue, PR gate review, Mission Control, registry) dengan kebijakan data sensitif tidak pernah masuk GitHub | Adopsi GOVERNANCE.md + SECURITY.md; tunjuk `@maintainers` | [GOVERNANCE.md](../../GOVERNANCE.md), [GOV-01](../07-governance/01-governance-model.md) | Kaprodi + AI Research Center |
| 6 | **Research ID** `UIAI-YYYY-NNN` sebagai primary key yang dipakai di Metopen, TA, dataset, publikasi, dan pelaporan | Adopsi skema ID; ID diberikan saat lolos G2 | [MST-03 §6](03-glossary.md), [GOVERNANCE.md §5](../../GOVERNANCE.md) | Admin riset / `@maintainers` |
| 7 | **Peran mentor riset** (dosen) dan pengakuan bebannya (BKD/penugasan) | Setiap tim Metopen memiliki 1 dosen mentor; mentor = reviewer gate G4–G8; diakui sebagai pembimbingan/penelitian | [GOV-01](../07-governance/01-governance-model.md), [AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md) | Kaprodi + Dekan |
| 8 | **Pilot pada semester ganjil 2026/2027** untuk kelas Metopen (GitHub Phase 2 — Pilot Metopen; GOV-02 Phase 1) dengan KPI pilot yang disepakati | Jalankan pilot satu kelas; evaluasi akhir semester; keputusan scale-up untuk AI/ML pada semester berikutnya | [GOV-02](../07-governance/02-implementation-roadmap.md), [GOV-03](../07-governance/03-kpi-and-measurement.md) | Kaprodi |
| 9 | **Verifikasi fakta institusional** (akreditasi, skema penelitian internal, tabel kurikulum) sebelum dokumen ini dikompilasi menjadi dokumen formal | Tugaskan admin riset memverifikasi dan mencatat sumber resmi | [MST-00 §10](00-readme.md) | Admin riset |

Yang **tidak** diminta: penambahan SKS, perubahan struktur kurikulum, pengadaan sistem informasi baru, atau kewajiban publikasi bagi semua mahasiswa. Semua berjalan di atas mata kuliah yang sudah ada dan GitHub yang gratis untuk institusi pendidikan.

## 7. Ringkasan satu paragraf

Informatika UAI sudah memiliki fondasi statistik, data, AI/ML, dan rekayasa perangkat lunak yang cukup; yang belum ada adalah pipeline yang mengubah kemampuan teknis itu menjadi pengetahuan baru yang *evidence-based*. UIRP menjawabnya dengan memposisikan Metodologi Penelitian sebagai Research Studio yang menghasilkan Research Pack melalui delapan Research Gates, sehingga 100% mahasiswa masuk TA dalam keadaan TA-ready dan yang terbaik siap publikasi; mata kuliah teknis menjadi penghasil research asset, TA menjadi tahap kontribusi, dan AI Research Center menjadi mesin institusional yang menghubungkan seluruh siklus dengan dosen, roadmap UAI, problem nasional, dan publikasi. Semua ini berjalan di atas kurikulum yang ada, memakai GitHub sebagai research operating system, menghasilkan evidence OBE/PjBL/PP-PTS secara otomatis, dan berpegang pada satu signature: **amanah epistemik — AI-augmented, human-accountable science.** Yang dibutuhkan dari Prodi adalah sembilan keputusan di atas, dengan pilot dimulai pada semester ganjil 2026/2027.
