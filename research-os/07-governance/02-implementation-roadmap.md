# Implementation Roadmap — Enam Fase Menuju 2030

> **ID** GOV-02 · **Paket** 07 Governance & Implementation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, Dekan, kepala AI Research Center, tim kurikulum, admin riset, tim PP-PTS
> **Terkait** [GOV-01 Governance Model](01-governance-model.md) · [GOV-03 KPI](03-kpi-and-measurement.md) · [GOV-04 Risk Register](04-risk-register.md) · [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) · [GOVERNANCE.md §10](../../GOVERNANCE.md) · [MST-01 Executive Summary](../00-master/01-executive-summary.md)

Roadmap ini menerjemahkan theory of change menjadi urutan fase yang dapat dijalankan Prodi tanpa menunggu semua prasyarat sempurna. Prinsipnya: **mulai dari satu kelas, buktikan, lalu perluas.** Durasi bersifat indikatif dan mengikuti kalender akademik; **titik nol adalah semester ganjil 2026/2027**. Setiap fase memiliki *exit criteria* — fase berikutnya dibuka hanya jika kriteria terpenuhi, sama seperti gate pada riset.

---

## 1. Ringkasan fase

| Fase (GOV-02) | Nama | Durasi indikatif | Padanan fase GitHub ([GOVERNANCE.md §10](../../GOVERNANCE.md)) | Owner |
|---|---|---|---|---|
| **Phase 0** | Design | Juli–Agustus 2026 (selesai; repo v0.1.0) | 0 Foundation + 1 Research OS | `@maintainers`, Kaprodi |
| **Phase 1** | Pilot Metopen | Semester ganjil 2026/2027 (September 2026–Januari 2027) | 2 Pilot Metopen | Dosen pengampu Metopen, Kaprodi |
| **Phase 2** | Integrate AI/ML | Semester genap 2026/2027 (persiapan RPS) → semester ganjil 2027/2028 (AI/ML mode R berjalan) | 3 Curriculum Integration (awal) | Koordinator AI/ML, tim kurikulum |
| **Phase 3** | Expand technical courses | Tahun akademik 2027/2028 | 3 Curriculum Integration (penuh) | Tim kurikulum, koordinator MK |
| **Phase 4** | AI Research Center integration | Semester ganjil 2028/2029 (±12 bulan) | 4 AI Center Launch | Kepala AI Research Center |
| **Phase 5** | Scale cross-faculty | 2029–2030 | 5 Public Research Portal | Kepala AI Research Center, pimpinan universitas |

Tahun 2030 dipilih sebagai horizon karena selaras dengan [`research-roadmap/2026-2030/`](../../research-roadmap/2026-2030/README.md) dan masa berlaku akreditasi Prodi hingga Maret 2030 (sumber: dokumen diskusi; verifikasi sebelum dokumen formal).

## 2. Rincian per fase

### Phase 0 — Design (Juli–Agustus 2026, selesai)

| Aspek | Isi |
|---|---|
| **Goal** | Fondasi tersedia: knowledge architecture, tata kelola GitHub, taksonomi, skema ID, 57 dokumen Research OS |
| **Activities** | Menyusun 9 paket dari dokumen diskusi; membuat `.github/` (issue forms, PR templates, labels, workflows); GOVERNANCE, CONTRIBUTING, LICENSING, SECURITY; roadmap 2026–2030; registry kosong dengan template; halaman mingguan W1–W16 |
| **Deliverables** | Repository v0.1.0 ([CHANGELOG](../../CHANGELOG.md)); dokumen Tier 1 status Draft v0.1 |
| **Owner** | `@maintainers`; Kaprodi sebagai sponsor |
| **KPI** | 57 dokumen ada; 0 link rusak (`tools/check_links.py`); WBS 145 task tersinkron |
| **Exit criteria** | Kaprodi membaca [MST-01](../00-master/01-executive-summary.md) dan menjadwalkan rapat keputusan; dosen pengampu Metopen ditetapkan |

### Phase 1 — Pilot Metopen (semester ganjil 2026/2027)

| Aspek | Isi |
|---|---|
| **Goal** | Satu kelas Metopen berjalan penuh sebagai Research Studio dengan 8 gate; 100% tim TA Ready; sistem terbukti dapat dioperasikan |
| **Activities** | Rapat keputusan Prodi (butir 1–8 [MST-01 §6](../00-master/01-executive-summary.md)); S0 onboarding (akun GitHub, repo dari [TPL-15](../08-templates/15-research-repository-template.md), AI Research Protocol agreement); backlog awal ≥ jumlah tim dari dosen/AI Center; matching mentor; sprint S1–S16; red team W8; peer review W14; defense W16; evaluasi semester |
| **Deliverables** | Research Issues, Research One-Pagers, repo `proj-2026-*`, PR gate review, release v0.1–v1.0 per tim, Research Pack v1.0, handoff ke TA, laporan evaluasi pilot |
| **Owner** | Dosen pengampu Metopen (R); Kaprodi (A); admin riset dan AI Center (R untuk backlog/ID/registry) |
| **KPI** ([GOV-03](03-kpi-and-measurement.md) target pilot) | KPI-L-01 100% One-Pager v0 di W2; KPI-L-02 ≥90% RQ tervalidasi di W6; KPI-L-04 ≥70% pilot berjalan di W10; KPI-I-01 ≥80% Research Pack v1.0; KPI-Q-01 ≥90% lolos integrity pertama kali; KPI-L-05 ≥80% gate review dalam SLA |
| **Exit criteria** | ≥80% tim lolos G8; pembimbing TA menerima handoff dan menyatakan Research Pack cukup untuk memulai; evaluasi semester menghasilkan revisi RPS v1.0 dan keputusan lanjut ke Phase 2; tidak ada insiden integritas yang tidak tertangani |

### Phase 2 — Integrate AI/ML (genap 2026/2027 → ganjil 2027/2028)

| Aspek | Isi |
|---|---|
| **Goal** | AI/ML (semester V, 4 SKS) menjadi MK mode **R**: proyeknya menghasilkan research asset yang masuk backlog dan registry, sehingga angkatan berikutnya masuk Metopen dengan asset siap pakai (Build → Prove tersambung) |
| **Activities** | Semester genap 2026/2027: revisi RPS AI/ML mengikuti [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) dan [`courses/ai-ml/`](../../research-based-learning/courses/ai-ml/README.md); definisi `research-artifact.md`; pelatihan koordinator. Semester ganjil 2027/2028: proyek AI/ML memakai Issue `type:problem`/`type:dataset`, baseline & metrik, reproducibility minimum; handoff Course → Metopen; Metopen angkatan kedua berjalan paralel dengan perbaikan dari pilot |
| **Deliverables** | RPS AI/ML v1.0 (mode R); `research-artifact.md` per tim AI/ML; ≥N dataset `DS-2027-*`; backlog terisi dari proyek MK; Metopen angkatan kedua |
| **Owner** | Koordinator AI/ML (R); tim kurikulum (A); admin riset (registry) |
| **KPI** | KPI-I-06 AI/ML mode R aktif; KPI-I-05 ≥30% tim Metopen angkatan kedua memakai asset angkatan sebelumnya/AI-ML; KPI-I-02 ≥70% TA continuation dari pilot |
| **Exit criteria** | Minimal satu siklus penuh AI/ML → Metopen dengan handoff terdokumentasi; TA angkatan pilot berjalan dari Research Pack; KPI pilot bertahan atau naik pada angkatan kedua |

### Phase 3 — Expand technical courses (2027/2028)

| Aspek | Isi |
|---|---|
| **Goal** | MK teknis lain (Data Mining, NLP, RPL/Software Engineering, Basis Data, HCI, Pengujian) ditandai F/E/R dan MK mode E/R mulai menghasilkan asset; pipeline menjadi milik Prodi, bukan satu mata kuliah |
| **Activities** | Workshop dosen berbasis [ARC-02](../02-academic-architecture/02-curriculum-research-map.md) dan [ARC-03](../02-academic-architecture/03-ai-contribution-modes.md); setiap MK mengisi `research-based-learning/courses/<mk>/README.md` + `research-artifact.md`; lecturer playbook dikompilasi; Metopen angkatan ketiga; TA angkatan pilot mencapai Published/Released pertama |
| **Deliverables** | Peta F/E/R seluruh kurikulum; ≥3 MK mode E/R aktif; Lecturer Playbook v1.0; publikasi/artefak pertama dari pipeline |
| **Owner** | Tim kurikulum (A); koordinator MK (R) |
| **KPI** | Jumlah MK mode E/R aktif ≥3; KPI-G-01 ≥2 submission di venue terdaftar; KPI-G-03 ≥1 dataset/artefak publik |
| **Exit criteria** | ≥3 MK menghasilkan asset yang benar-benar dipakai tim Metopen/TA; RPS Metopen dan AI/ML berstatus Adopted v1.0; risk register menunjukkan RSK-05 (faculty resistance) turun ke skor rendah |

### Phase 4 — AI Research Center integration (ganjil 2028/2029, ±12 bulan)

| Aspek | Isi |
|---|---|
| **Goal** | AI Research Center beroperasi sebagai hub: klaster C1–C4 dengan research lead, program riset `program-*`, Faculty Portfolio, problem partner, dan pipeline mahasiswa yang berjalan otomatis setiap semester |
| **Activities** | Menetapkan research leads klaster; membuat repo `program-*` untuk program 5–10 tahun; mengisi [TPL-07](../08-templates/07-faculty-research-map-template.md) seluruh dosen; mengaktifkan marketplace demand–supply ([AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)); mengikat skema penelitian internal ke Research ID mahasiswa; IP review rutin; concept paper AI Research Center dikompilasi dari paket 01+03+07 |
| **Deliverables** | ≥2 repo `program-*` aktif; Faculty Portfolio lengkap; ≥1 problem partner per klaster di backlog; concept paper; laporan evidence tahunan ([GOV-05](05-ppts-and-institutional-evidence.md)) |
| **Owner** | Kepala AI Research Center (A); research leads (R); Kaprodi (C) |
| **KPI** | KPI-I-03 ≥50% riset mahasiswa terikat riset dosen; KPI-G-05 ≥2 hibah dengan mahasiswa pipeline; KPI-G-02 publikasi diterima ≥5/tahun |
| **Exit criteria** | Pusat riset memiliki agenda, orang, backlog, dan evidence yang berjalan tanpa bergantung pada satu dosen; pemisahan penuh peran admin riset dan mentor |

### Phase 5 — Scale cross-faculty (2029–2030)

| Aspek | Isi |
|---|---|
| **Goal** | Model *Domain Problem + Data + AI Capability + Evaluation + Impact* ([AIR-04](../03-ai-research-ecosystem/04-cross-faculty-ai-model.md)) berjalan dengan fakultas lain; GitHub menjadi portofolio publik Pusat Riset AI UAI; evidence akreditasi dan hibah tersedia sebagai ekspor rutin |
| **Activities** | Riset bersama fakultas lain (gizi, pangan, psikologi, hukum, ekonomi, bahasa, komunikasi — sesuai domain roadmap); repo `proj-*` lintas fakultas; otomasi (auto-scaffold repo, auto-update status saat PR gate merge, ringkasan portofolio mingguan); dashboard/website publik; evaluasi roadmap 2026–2030 dan penyusunan roadmap berikutnya |
| **Deliverables** | ≥3 riset lintas fakultas dengan Research ID; portal/dashboard publik; roadmap 2031– draft; paket evidence akreditasi |
| **Owner** | Kepala AI Research Center (A); pimpinan universitas (C); `@maintainers` (otomasi) |
| **KPI** | KPI-G-06 ≥3 riset lintas fakultas/partner aktif; target 2030 pada [GOV-03](03-kpi-and-measurement.md) tercapai; evidence diekspor ≤1 hari kerja saat diminta |
| **Exit criteria** | Roadmap 2026–2030 dievaluasi; loop compounding terbukti (asset angkatan lama dipakai angkatan baru ≥50%); model direplikasi ke prodi/fakultas lain |

## 3. Pemetaan ke fase GitHub

| Fase GitHub ([GOVERNANCE.md §10](../../GOVERNANCE.md)) | Fokus | Fase GOV-02 | Status |
|---|---|---|---|
| 0 Foundation | Organization, `.github`, governance, README, taksonomi, Research ID | Phase 0 | Selesai (v0.1.0) |
| 1 Research OS | 57 dokumen, roadmap, templates, gates | Phase 0 | Selesai (v0.1.0) |
| 2 Pilot Metopen | Research Issues, One-Pagers, repo project, gate reviews | Phase 1 | Semester ganjil 2026/2027 |
| 3 Curriculum Integration | AI/ML dan MK lain menghasilkan research assets | Phase 2 + Phase 3 | 2027–2028 |
| 4 AI Center Launch | Klaster dosen, lintas fakultas, problem partner, repo `program-*` | Phase 4 | 2028/2029 |
| 5 Public Research Portal | Dashboard otomatis, website, portofolio publik | Phase 5 | 2029–2030 |

Perbedaan penomoran disengaja: fase GitHub menghitung pembangunan infrastruktur (0–1) sebagai dua fase; fase GOV-02 menggabungkannya menjadi Phase 0 Design karena bagi Prodi keduanya adalah satu keputusan.

## 4. Quick wins 90 hari pertama (September–November 2026)

Tujuan quick wins: membuat sistem terasa nyata bagi dosen dan mahasiswa sebelum hasil besar terlihat, sekaligus menurunkan risiko faculty resistance (RSK-05) dan overload (RSK-01).

| Minggu | Quick win | Bukti selesai | Owner |
|---|---|---|---|
| 1–2 | Rapat keputusan Prodi atas 9 butir [MST-01 §6](../00-master/01-executive-summary.md); minimal butir 1–3 disetujui | Notulen; status dokumen Tier 1 → Review v0.5 | Kaprodi |
| 1–2 | S0 onboarding: semua mahasiswa Metopen punya akun GitHub, repo dari template, AI Research Protocol ditandatangani | Repo `proj-2026-*` ada untuk setiap tim | Dosen pengampu, admin riset |
| 2–3 | Backlog awal: ≥ jumlah tim Issue `type:problem` dari dosen/AI Center, tertriase klaster/domain | [`research-backlog/BACKLOG.md`](../../research-backlog/BACKLOG.md) terisi | AI Research Center |
| 3–4 | Mentor terpasang untuk setiap tim; faculty research map minimal untuk dosen yang terlibat | Field Faculty Mentor terisi di Mission Control | AI Research Center, Kaprodi |
| 4 | Research ID pertama diberikan (G2 lolos) | Issue berjudul `[UIAI-2026-001] …` | Admin riset |
| 6 | Synthesis matrix pertama dengan semua referensi terverifikasi; G3 lolos untuk mayoritas tim | Release v0.2 pada ≥70% repo | Dosen pengampu |
| 8 | Design Defense / Red Team pertama; dosen lain ikut sebagai red team (sosialisasi lewat praktik) | Notulen red team; G5 lolos | Dosen pengampu, mentor |
| 8–10 | Dataset pertama terdaftar dengan lisensi & privasi jelas | Entri `DS-2026-001` di [`datasets-registry/REGISTRY.md`](../../datasets-registry/REGISTRY.md) | Pengelola registry |
| 10–12 | Pilot experiment pertama direproduksi peer; cerita sukses dibagikan ke rapat Prodi | Release v0.5; catatan reproduksi | Dosen pengampu |
| 12 | Laporan KPI leading pertama (KPI-L-01…L-08) diekspor dari GitHub tanpa form tambahan | Laporan 1 halaman ke Kaprodi | Admin riset |

## 5. Prasyarat lintas fase dan ketergantungan

```
Phase 0 Design ──► Phase 1 Pilot ──► Phase 2 AI/ML ──► Phase 3 MK lain ──► Phase 4 AI Center ──► Phase 5 Lintas fakultas
     │                 │                  │                   │                    │
     │                 │                  │                   │                    └─ butuh: research leads, Faculty Portfolio, IP review rutin
     │                 │                  │                   └─ butuh: RPS AI/ML v1.0 terbukti, Lecturer Playbook
     │                 │                  └─ butuh: hasil pilot, handoff Course→Metopen terdefinisi
     │                 └─ butuh: keputusan Prodi butir 1–3, dosen pengampu, backlog awal, mentor
     └─ butuh: repo v0.1.0, sponsor Kaprodi
```

Fase boleh **tumpang tindih** (Metopen angkatan kedua berjalan saat RPS AI/ML direvisi), tetapi **exit criteria tidak boleh dilewati**. Jika exit criteria Phase 1 tidak tercapai, Phase 1 diulang dengan perbaikan, bukan diteruskan ke Phase 2 — sama seperti gate.

## 6. Tinjauan roadmap

Roadmap ditinjau pada **evaluasi semester** ([GOV-01 §4](01-governance-model.md)) dan **review tahunan**. Perubahan durasi/urutan diajukan lewat PR ke dokumen ini dengan alasan yang merujuk KPI ([GOV-03](03-kpi-and-measurement.md)) atau risiko ([GOV-04](04-risk-register.md)), lalu dicatat di [CHANGELOG.md](../../CHANGELOG.md).
