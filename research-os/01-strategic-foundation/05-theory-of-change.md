# Theory of Change — Dari Input ke Dampak

> **ID** STR-05 · **Paket** 01 Strategic Foundation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Pimpinan universitas, reviewer hibah, tim PP-PTS, kepala AI Research Center, Kaprodi
> **Terkait** [STR-02 Vision & Endgame](02-vision-and-endgame.md) · [STR-04 Alignment Map](04-alignment-map.md) · [GOV-03 KPI & Measurement](../07-governance/03-kpi-and-measurement.md) · [GOV-04 Risk Register](../07-governance/04-risk-register.md) · [GOV-02 Implementation Roadmap](../07-governance/02-implementation-roadmap.md)

Dokumen ini menjelaskan **rantai sebab-akibat** yang membuat UAI Informatics Research Pipeline (UIRP) menghasilkan dampak: apa yang dimasukkan, apa yang dilakukan, apa yang dihasilkan langsung, apa yang berubah pada mahasiswa dan dosen, dan apa dampak institusionalnya. Ditulis dalam format yang lazim dipakai reviewer hibah: Input → Activities → Output → Outcome → Impact, disertai asumsi dan risiko.

---

## 1. Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│ INPUT                                                                │
│ Dosen (pengampu, mentor, pembimbing TA, klaster C1–C4)               │
│ + Mata Kuliah (AI/ML sem V, Metopen sem VII, TA sem VIII, MK F/E/R)  │
│ + AI Infrastructure (GitHub sebagai research OS, AI tools, compute)  │
│ + Dataset (datasets-registry, data partner ber-governance)           │
│ + Problem (backlog dari stakeholder, roadmap, prioritas nasional)    │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ ACTIVITIES                                                           │
│ PjBL di MK teknis (Build)                                            │
│ + Research Studio Metopen: 17 sprint, 145 microtask, 8 gate (Prove)  │
│ + Mentoring: dosen mentor, red team W8, peer review W14, defense W16 │
│ + AI Research Protocol: Think→Ask→Ground→Verify→Challenge→           │
│   Reproduce→Disclose→Own                                             │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ OUTPUT                                                               │
│ Research Assets (dataset terdaftar, kode reproducible, benchmark,    │
│   literature map, problem brief)                                     │
│ + Research Packs v1.0 (16 komponen; proposal TA + pitch)             │
│ + Evidence otomatis (Issue, PR gate review, release, registry)       │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ OUTCOME                                                              │
│ Better TA (100% TA Ready; mayoritas Research Ready)                  │
│ + Research Participation (mahasiswa dalam riset dosen; mentor aktif) │
│ + Manuscripts (manuscript-ready → submitted di venue kredibel)       │
│ + Scientific thinkers (kompetensi AI Investigator/Governor)          │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ IMPACT                                                               │
│ Stronger Research Culture (amanah epistemik sebagai norma)           │
│ + Publication & artefak (PUB-, DS-, ART-, HKI) yang bertambah        │
│ + AI Research Center sebagai hub lintas fakultas & partner           │
│ + Evidence akreditasi/PP-PTS + reputasi + intake lebih baik          │
│   → compounding loop: problem lebih baik untuk angkatan berikutnya   │
└──────────────────────────────────────────────────────────────────────┘
```

## 2. Tabel rinci per tahap

Kode KPI merujuk ke [GOV-03](../07-governance/03-kpi-and-measurement.md). Pemilik merujuk ke peran di [GOV-01](../07-governance/01-governance-model.md).

### 2.1 Input

| Komponen | Indikator kesiapan | Sumber data | Pemilik |
|---|---|---|---|
| Dosen | Dosen pengampu Metopen ditetapkan; ≥1 mentor per tim; peta dosen–klaster terisi ([TPL-07](../08-templates/07-faculty-research-map-template.md)) | Faculty research map; penugasan Prodi | Kaprodi, AI Research Center |
| Mata kuliah | RPS Metopen mengikuti blueprint 16 minggu; AI/ML ditandai mode R (Phase 2) | RPS; `research-based-learning/courses/*/README.md` | Tim kurikulum, koordinator MK |
| AI infrastructure | GitHub Organization/repo aktif; Mission Control dibuat; AI tools terdaftar di [AIX-05](../05-ai-augmented-research/05-ai-tools-reference.md) | GOVERNANCE.md, Projects | Admin riset / `@maintainers` |
| Dataset | ≥N dataset terkatalog dengan lisensi & privasi jelas | [`datasets-registry/REGISTRY.md`](../../datasets-registry/REGISTRY.md) | Pengelola registry |
| Problem | Backlog berisi problem tervalidasi cukup untuk semua tim | [`research-backlog/BACKLOG.md`](../../research-backlog/BACKLOG.md), Issues `type:problem` | AI Research Center, dosen |

### 2.2 Activities

| Aktivitas | Indikator pelaksanaan | Sumber data | Pemilik |
|---|---|---|---|
| PjBL di MK teknis (Build) | MK mode E/R menghasilkan `research-artifact.md` dan/atau Issue backlog | `research-based-learning/courses/*` | Koordinator MK |
| Research Studio Metopen (Prove) | Sprint S0–S16 berjalan; PR gate dibuka sesuai jadwal W1–W16 | Mission Control, PR `GATE REVIEW:*` | Dosen pengampu Metopen |
| Mentoring | Mentor mereview G4–G8; red team W8 terlaksana; peer review W14; defense W16 | PR review, notulen red team, [TPL-12](../08-templates/12-peer-review-template.md), [TPL-13](../08-templates/13-research-defense-template.md) | Mentor, dosen pengampu |
| AI Research Protocol | AI Usage Log terisi tiap sprint; verifikasi sumber tercatat | [TPL-10](../08-templates/10-ai-usage-log-template.md), `AI-USAGE.md` | Mahasiswa; diaudit dosen |

### 2.3 Output

| Output | Indikator | Sumber data | KPI | Pemilik |
|---|---|---|---|---|
| Research Assets | Dataset `DS-`, kode dengan reproducibility package, literature map, problem brief per tim | Registry, repo riset, release v0.2–v0.5 | KPI-L-03, KPI-L-04, KPI-I-05 | Tim riset, pengelola registry |
| Research Packs | Release `v1.0 Research Pack` per tim; 16 komponen lengkap | Release, [MET-04](../04-metopen-research-studio/04-research-pack-specification.md) checklist | KPI-I-01 | Tim riset, dosen pengampu |
| Evidence otomatis | Issue/PR/release per Research ID dapat diekspor | GitHub export ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)) | KPI-L-06 | Admin riset |

### 2.4 Outcome

| Outcome | Indikator | Sumber data | KPI | Pemilik |
|---|---|---|---|---|
| Better TA | % tim lolos G5 (TA Ready) = 100%; % lolos G7 (Research Ready); % TA melanjutkan Research Pack tanpa ganti topik | Mission Control, handoff, data TA Prodi | KPI-I-01, KPI-I-02 | Dosen pengampu, koordinator TA |
| Research Participation | % riset mahasiswa dengan mentor aktif; jumlah mahasiswa masuk skema penelitian dosen | Faculty Portfolio, proposal hibah | KPI-I-03 | AI Research Center |
| Manuscripts | Jumlah manuscript-ready dan submitted di venue terdaftar | [`publications/`](../../publications/README.md), venue registry | KPI-G-01 | Mentor, tim riset |
| Scientific thinkers | % mahasiswa mencapai level AI Investigator; skor 5E dimensi Evidence & Explanation | Rubrik 5E, AI Usage Log | KPI-Q-01..04 | Dosen pengampu |

### 2.5 Impact

| Impact | Indikator | Sumber data | KPI | Pemilik |
|---|---|---|---|---|
| Stronger research culture | % riset lolos integrity gate pertama kali; peer reproduksi rutin; mahasiswa menjadi reviewer | Integrity checklist, PR review | KPI-Q-01, KPI-Q-03 | Kaprodi |
| Publication & artefak | Publikasi diterima, dataset/artefak dirilis, HKI | Registry `PUB-`/`DS-`/`ART-` | KPI-G-02..04 | AI Research Center |
| AI Research Center sebagai hub | Program `program-*` aktif; riset lintas fakultas; problem partner di backlog | Repo program, backlog, Mission Control | KPI-G-05..06 | Kepala AI Research Center |
| Evidence institusional & reputasi | Evidence PP-PTS/akreditasi diekspor tanpa pekerjaan tambahan; hibah dengan mahasiswa | [GOV-05](../07-governance/05-ppts-and-institutional-evidence.md) export, data hibah | KPI-G-05 | Kaprodi, tim PP-PTS |

## 3. Logika sebab-akibat (mengapa tahap berikutnya terjadi)

| Dari → Ke | Mekanisme | Bukti bahwa mekanisme bekerja |
|---|---|---|
| Input → Activities | Kurikulum sudah menempatkan AI/ML–Metopen–TA berurutan; tidak perlu perubahan struktur untuk mulai | RPS Metopen direvisi tanpa penambahan SKS |
| Activities → Output | Gate memaksa artefak lahir pada minggu tertentu; sprint kecil (7–10 task) membuat pekerjaan selesai | PR gate merge sesuai jadwal; release milestone terbentuk |
| Output → Outcome | Research Pack menjadi proposal TA; pembimbing tidak mengulang dari nol; mentor sudah mengenal riset sejak G4 | TA melanjutkan Research ID yang sama; waktu TA berkurang |
| Outcome → Impact | Mahasiswa TA-ready memenuhi syarat "minimal dua mahasiswa" skema penelitian internal; publikasi menambah reputasi; evidence lahir otomatis | Proposal hibah dosen mencantumkan Research ID mahasiswa; export evidence dipakai laporan |
| Impact → Input (loop) | Reputasi dan kolaborasi mendatangkan problem/partner lebih baik; asset diwariskan | Backlog angkatan berikutnya berisi problem partner dan dataset terdaftar |

## 4. Assumptions

Theory of change ini hanya berlaku jika asumsi berikut terpenuhi. Setiap asumsi memiliki cara memeriksanya.

| # | Asumsi | Cara memverifikasi | Jika tidak terpenuhi |
|---|---|---|---|
| A1 | Prodi menyetujui Research Pack sebagai deliverable resmi Metopen dan proposal TA yang diakui | Keputusan tertulis ([MST-01 §6](../00-master/01-executive-summary.md) butir 2) | Outcome "Better TA" tidak terjadi; Metopen kembali menjadi kelas proposal |
| A2 | Dosen pengampu Metopen bersedia menjalankan format studio (70%) dan mereview PR gate | Kesediaan dinyatakan sebelum semester; pelatihan singkat | Gate menjadi formalitas; kualitas bukti tidak naik |
| A3 | Tersedia mentor dosen untuk setiap tim (rasio ≤5 tim per mentor) dan bebannya diakui | Faculty research map; keputusan BKD/penugasan | Bottleneck review; mentor capacity risk ([GOV-04](../07-governance/04-risk-register.md) RSK-12) |
| A4 | Mahasiswa semester VII memiliki fondasi teknis dari AI/ML, Data Mining, RPL untuk menjalankan pilot experiment | Nilai/portofolio MK prasyarat; sprint S0 onboarding | Pilot tidak terlaksana; outcome berhenti di TA Ready |
| A5 | Backlog berisi problem tervalidasi yang cukup untuk semua tim pada awal semester | Jumlah Issue `type:problem` lolos triage ≥ jumlah tim | Tim memilih problem *solution-first*; G2 gagal massal |
| A6 | Akses GitHub, AI tools, dan compute dasar tersedia bagi semua mahasiswa | Uji akses di S0 | Fragmentasi kembali ke laptop pribadi |
| A7 | Kebijakan AI Prodi mengizinkan AI dengan protokol pengungkapan (bukan melarang total) | Keputusan kebijakan ([MST-01 §6](../00-master/01-executive-summary.md) butir 4) | Mahasiswa memakai AI secara diam-diam; integritas rapuh |
| A8 | Pembimbing TA bersedia memulai dari Research Pack/handoff, bukan meminta topik baru | Sosialisasi ke pembimbing; handoff wajib | TA continuation rendah; investasi Metopen hilang |
| A9 | Skema penelitian internal UAI tetap mendorong keterlibatan mahasiswa dan keselarasan Renstra | Verifikasi call terbaru setiap tahun | Insentif dosen untuk mentoring melemah |
| A10 | Data sensitif dapat dikelola di luar GitHub tanpa menghambat riset | SECURITY.md dijalankan; registry metadata cukup | Riset partner tertahan atau privasi bocor |

## 5. Risks (ringkas)

Register lengkap dengan skor, early warning, dan contingency ada di [GOV-04](../07-governance/04-risk-register.md). Di sini hanya risiko yang paling langsung mengancam rantai sebab-akibat.

| Risiko (ID GOV-04) | Tahap yang terancam | Mitigasi ringkas |
|---|---|---|
| RSK-01 Overload mahasiswa/dosen dalam 2 SKS | Activities → Output | Sprint 7–10 task; sweet spot bukan frontier; reuse asset; review asinkron via PR |
| RSK-02 Fake AI research (referensi fiktif, klaim kosong) | Output → Outcome | Protokol AIX-04; G3 gagal jika satu referensi tak terverifikasi; AI Usage Log; integrity gate |
| RSK-03 Predatory journal | Outcome → Impact | Venue registry non-predator; KPI hanya menghitung venue terdaftar |
| RSK-05 Faculty resistance | Input → Activities | Mode F/E/R (tidak semua MK riset besar); pengakuan beban; quick wins; pilot satu kelas |
| RSK-06 Fragmentation kembali | Output, loop | Research ID sebagai primary key; satu repo/registry; handoff wajib |
| RSK-07 Administrative burden | Activities | Evidence otomatis dari GitHub; tidak ada form paralel (P1) |
| RSK-08 Publication gaming | Impact | P7; anti-gaming di GOV-03; audit sampel |
| RSK-12 Mentor capacity | Activities → Output | Rasio tim/mentor; peer review dan red team mengurangi beban; asisten riset |

## 6. Cara memakai dokumen ini

- **Reviewer hibah / pimpinan:** baca §1 dan §3 untuk logika; §4 untuk asumsi yang perlu dukungan kebijakan; [GOV-03](../07-governance/03-kpi-and-measurement.md) untuk target angka.
- **Tim PP-PTS:** tiap baris Output/Outcome/Impact menunjuk sumber data yang dapat diekspor ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)).
- **Kaprodi:** asumsi A1, A3, A7, A8 adalah keputusan yang berada di tangan Prodi; tanpa itu rantai terputus pada tahap Outcome.
- **Evaluasi semester:** periksa apakah setiap panah di §3 benar-benar terjadi; jika tidak, perbaiki mekanismenya, bukan targetnya.

Roadmap fase untuk mewujudkan rantai ini: [GOV-02](../07-governance/02-implementation-roadmap.md).
