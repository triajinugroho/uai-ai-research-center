# PP-PTS & Institutional Evidence — Dari Alur Kerja ke Bukti Audit

> **ID** GOV-05 · **Paket** 07 Governance & Implementation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Tim PP-PTS, tim penjaminan mutu/akreditasi, Kaprodi, admin riset, reviewer hibah, kepala AI Research Center
> **Terkait** [STR-04 Alignment Map](../01-strategic-foundation/04-alignment-map.md) · [GOV-03 KPI](03-kpi-and-measurement.md) · [GOV-01 Governance Model](01-governance-model.md) · [ARC-05 CPL–CPMK–Artifact Alignment](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [GOVERNANCE.md](../../GOVERNANCE.md) · [TPL-02 Research Mission Tracker](../08-templates/02-research-mission-tracker-template.md)

Dokumen ini menjawab pertanyaan tim pelaporan: **"bukti apa yang ada, di mana, dan bagaimana mengambilnya?"** Prinsipnya *one activity, multiple outcomes*: bukti untuk PP-PTS, akreditasi, laporan hibah, dan BKD lahir dari alur kerja riset di GitHub — bukan dari form yang diisi ulang.

> **Catatan verifikasi.** Istilah *PP-PTS* dipakai sebagaimana dokumen sumber (program pendanaan/penguatan perguruan tinggi swasta). **Nama resmi program pendanaan, komponen laporan, format, dan periode pelaporan harus diverifikasi** oleh admin riset/tim PP-PTS sebelum tabel di sini dipakai dalam laporan formal. Struktur mapping tetap berlaku untuk skema pelaporan apa pun (akreditasi LAM-INFOKOM, hibah internal/eksternal, laporan tahunan Prodi).

---

## 1. Mapping: Activity → RPS → Project → Evidence → KPI → PP-PTS documentation

| # | Activity (apa yang dilakukan) | RPS / dokumen akademik | Project (di mana terjadi) | Evidence (bukti otomatis) | KPI ([GOV-03](03-kpi-and-measurement.md)) | PP-PTS documentation (jenis bukti yang biasanya diminta) |
|---|---|---|---|---|---|---|
| 1 | Reposisi Metopen sebagai Research Studio | RPS Metopen v1.0 (16 minggu, 5E, integrity gate) — [MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) | Kelas Metopen semester VII | RPS di repo (versi, CHANGELOG); notulen keputusan Prodi | — (prasyarat) | Dokumen kurikulum/RPS; SK/notulen penetapan |
| 2 | Pembelajaran berbasis proyek/tim (PjBL, Team-Based Project) | CPMK Metopen ↔ komponen Research Pack — [MET-02](../04-metopen-research-studio/02-metopen-course-outcomes.md), [ARC-05](../02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) | Repo `proj-YYYY-*` per tim; sprint S1–S16 | Git history (kontribusi per anggota), PR gate, sprint review di Mission Control | KPI-L-03, KPI-L-07 | Bukti pelaksanaan pembelajaran inovatif; daftar proyek mahasiswa; log aktivitas |
| 3 | Asesmen autentik (gate review, red team, defense) | Rubrik 5E; *definition of done* gate — [OPS-03](../06-execution-os/03-research-gates.md) | PR `GATE REVIEW:*`; W8 red team; W16 defense | PR review dengan komentar reviewer; rubrik terisi; notulen red team; rekaman/notulen defense ([TPL-13](../08-templates/13-research-defense-template.md)) | KPI-L-01, L-02, L-04, I-01, Q-01 | Bukti asesmen capaian pembelajaran (OBE); portofolio mahasiswa |
| 4 | Keterlibatan mahasiswa dalam penelitian dosen | Faculty research map ([TPL-07](../08-templates/07-faculty-research-map-template.md)); [AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md) | Mission Control field Faculty Mentor; Faculty Portfolio; proposal hibah | Daftar Research ID per dosen; PR review oleh mentor; proposal skema penelitian internal yang mencantumkan Research ID | KPI-L-08, KPI-I-03, KPI-G-05 | Bukti mahasiswa terlibat penelitian dosen; laporan hibah |
| 5 | Pengelolaan data riset | Kartu dataset ([TPL-05](../08-templates/05-dataset-registry-template.md)); [SECURITY.md](../../SECURITY.md) | [`datasets-registry/`](../../datasets-registry/README.md) | Entri `DS-YYYY-NNN` dengan lisensi, privasi, pemilik | KPI-G-03, KPI-I-05 | Bukti tata kelola data/etika penelitian; inventaris dataset |
| 6 | Integritas & etika riset, kebijakan AI | [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md); [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md) | Setiap repo riset | Integrity checklist ditandatangani ([TPL-11](../08-templates/11-research-integrity-checklist.md)); `AI-USAGE.md`; AI Usage Log; `docs/ethics.md` | KPI-Q-01, Q-02, Q-05, Q-07 | Bukti kebijakan integritas akademik dan etika penelitian; kebijakan penggunaan AI |
| 7 | Kelanjutan Metopen → TA | Handoff ([TPL-14](../08-templates/14-research-handoff-template.md)); [ARC-04](../02-academic-architecture/04-build-prove-contribute.md) | Repo riset (berlanjut); data TA Prodi | Release `v1.0 Research Pack`; handoff terisi; Research ID sama di TA | KPI-I-01, KPI-I-02, KPI-I-07 | Bukti keterkaitan mata kuliah dengan TA; masa studi/ketepatan TA |
| 8 | Publikasi & diseminasi | Backward design ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)); venue registry ([TPL-06](../08-templates/06-publication-venue-registry-template.md)) | [`publications/`](../../publications/README.md) | Entri `PUB-YYYY-NNN` (venue, status, DOI); release `v1.1 Submitted`/`v2.0 Published` | KPI-G-01, G-02, Q-06 | Daftar publikasi mahasiswa/dosen; bukti diseminasi |
| 9 | Luaran artefak & HKI | [LICENSING.md](../../LICENSING.md); IP review; [ARC-06](../02-academic-architecture/06-research-output-taxonomy.md) | Release repo riset; registry artefak | Entri `ART-YYYY-NNN`; catatan IP review; sertifikat HKI | KPI-G-03, G-04 | Daftar luaran penelitian (software, dataset, HKI, prototype) |
| 10 | Integrasi MK teknis (AI/ML dst.) sebagai penghasil research asset | RPS MK mode E/R; [ARC-03](../02-academic-architecture/03-ai-contribution-modes.md) | [`research-based-learning/courses/`](../../research-based-learning/README.md) | `research-artifact.md` per MK; Issue backlog dari proyek MK | KPI-I-06 | Bukti integrasi penelitian ke pembelajaran (research-based learning) |
| 11 | Tata kelola dan kelembagaan pusat riset | [GOV-01](01-governance-model.md); [AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md); [GOVERNANCE.md](../../GOVERNANCE.md) | Organization GitHub; rapat bulanan/semester | Notulen rapat Research Ops & evaluasi semester; RACI; risk register; CHANGELOG | KPI-L-05, L-06 | Bukti tata kelola/SOP; struktur organisasi pusat riset |
| 12 | Kerja sama partner & lintas fakultas | [AIR-04](../03-ai-research-ecosystem/04-cross-faculty-ai-model.md); [AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) | Issue `type:problem` entry door Partner; repo lintas fakultas | Research ID dengan Entry Door Partner; perjanjian data (di luar GitHub) | KPI-G-06 | Bukti kerja sama; MoU/perjanjian |
| 13 | Roadmap dan keselarasan Renstra | [`research-roadmap/`](../../research-roadmap/README.md); [`alignment/uai.md`](../../research-roadmap/alignment/uai.md) | Backlog terklasifikasi klaster/domain | Distribusi Research ID per klaster/domain (view By Research Cluster) | — | Bukti peta jalan penelitian dan keselarasan dengan Renstra |
| 14 | Pengukuran kinerja | [GOV-03](03-kpi-and-measurement.md) | Laporan semester | Laporan KPI 1 halaman (aktual vs target) + lampiran ekspor | Semua | Laporan indikator kinerja utama |

## 2. Evidence yang dihasilkan otomatis oleh alur GitHub

| Objek GitHub | Apa yang direkam | Evidence untuk | Lokasi | Catatan integritas bukti |
|---|---|---|---|---|
| **Issue** (`type:problem`, `type:research-question`, `type:dataset`, `type:experiment`, `type:literature-gap`, `type:publication`, `type:research-risk`) | Unit riset: siapa mengusulkan, kapan, klaster/domain, status, Research ID | Jumlah & mutu problem riset; keterlibatan dosen/partner; risiko | Repo organization / `research-backlog/` | Timestamp dan penulis tidak dapat diubah; tutup dengan alasan (`state_reason`) |
| **Pull Request `GATE REVIEW:*`** | Review ilmiah per gate: field RQ, method, dataset, baseline, metrics, threats, evidence, AI usage; komentar reviewer; keputusan merge/close | Asesmen autentik; peran mentor; kualitas proses | Repo `proj-*`, template di `.github/PULL_REQUEST_TEMPLATE/` | Komentar review disimpan, tidak dihapus ([CONTRIBUTING.md §3](../../CONTRIBUTING.md)) |
| **Label** (`gate:*`, `maturity:*`, `cluster:*`, `P0–P3`, `status:*`) | Posisi riset pada gate dan kematangan | KPI leading/intermediate | Issue/PR | Diperbarui saat PR gate merge |
| **Release** (`v0.1` … `v2.0`) | Milestone kematangan dengan tanggal dan artefak terlampir (Research Pack, manuscript) | Bukti luaran per tahap; tanggal capaian | Repo `proj-*` | Tag git tidak dapat diubah tanpa jejak |
| **Git history / commit** | Kontribusi per anggota, waktu, Task ID WBS | Team-Based Project; akuntabilitas individu | Repo `proj-*` | Pesan commit menyebut Research ID/Task ID |
| **GitHub Projects — Research Mission Control** | Field: Research ID, Cluster, Domain, Researcher, Faculty Mentor, Entry Door, Course, Research Gate, Maturity, Priority, Publication Target, Due, Status, Next Evidence | Dashboard pipeline; Faculty Portfolio; By Course; Publication Pipeline | Organization Project | Sumber utama laporan KPI; ekspor CSV |
| **Registry** (`research-backlog/BACKLOG.md`, `datasets-registry/REGISTRY.md`, `publications/PUBLICATIONS.md`) | Indeks Research ID, dataset, publikasi, artefak dengan metadata | Inventaris luaran & data | Folder registry | Diperbarui lewat PR; riwayat di git |
| **Dokumen Research OS + CHANGELOG** | Kebijakan, RPS, rubrik, versi, keputusan | Bukti tata kelola dan kurikulum | `research-os/`, `CHANGELOG.md` | Setiap perubahan bermakna tercatat |
| **Workflow `docs-check`** | Pemeriksaan otomatis link/WBS pada setiap PR | Bukti pengendalian mutu dokumen | `.github/workflows/` | Log Actions tersimpan |

## 3. Cara mengekspor evidence

Prosedur ini dijalankan admin riset (`@maintainers`). Semua perintah memakai GitHub CLI (`gh`) atau fitur ekspor bawaan; hasil disimpan di folder laporan **di luar repo publik** (evidence dapat memuat nama mahasiswa).

| Kebutuhan | Cara | Output |
|---|---|---|
| Daftar riset per periode dengan gate & klaster | Mission Control → view *Research Pipeline* → **Export** (CSV); atau `gh issue list --label "type:problem" --state all --json number,title,labels,createdAt,closedAt` | CSV/JSON Research ID, gate, maturity, mentor, tanggal |
| Bukti asesmen (gate review) per tim | `gh pr list --search "GATE REVIEW" --state all --json number,title,mergedAt,reviews,author` di repo `proj-*`; unduh komentar review dengan `gh pr view <n> --comments` | Daftar PR gate + reviewer + tanggal + komentar |
| Milestone luaran | `gh release list` per repo `proj-*`; lampiran release (Research Pack, manuscript) | Tanggal v0.1…v2.0 per Research ID |
| Kontribusi anggota tim | `git shortlog -sne --since=<tanggal>` per repo; `git log --grep="UIAI-2026-001"` | Ringkasan kontribusi per mahasiswa |
| Faculty Portfolio (BKD, hibah, akreditasi) | Mission Control → view *Faculty Portfolio* → Export; filter Faculty Mentor | Daftar Research ID per dosen dengan gate/maturity |
| Inventaris dataset/publikasi/artefak | Salin tabel dari `REGISTRY.md` / `PUBLICATIONS.md` (Markdown → spreadsheet) | Inventaris dengan ID, lisensi, status |
| Laporan KPI semester | Hitung dari ekspor di atas sesuai formula [GOV-03](03-kpi-and-measurement.md); isi [TPL-02](../08-templates/02-research-mission-tracker-template.md) bila diperlukan ringkasan per tim | Laporan 1 halaman + lampiran |
| Bukti tata kelola | Notulen rapat (folder internal), RACI, risk register, CHANGELOG, workflow logs | Paket dokumen tata kelola |

Aturan:

1. **Jangan mengekspor data sensitif** (data mentah, data pribadi partner) — hanya metadata dan artefak yang aman ([SECURITY.md](../../SECURITY.md)).
2. Setiap ekspor diberi **tanggal dan versi repo** (tag/commit) agar dapat direproduksi saat audit.
3. Ekspor rutin: akhir semester (KPI) dan tahunan (paket evidence). Ekspor ad hoc untuk hibah/audit ≤1 hari kerja (target Phase 5).
4. Otomasi ekspor (GitHub Actions) dibangun **setelah** alur manual stabil ([GOVERNANCE.md §10](../../GOVERNANCE.md)).

## 4. Checklist kesiapan audit

Diperiksa admin riset sebelum periode pelaporan; hasil dilaporkan di evaluasi semester ([GOV-01 §4](01-governance-model.md)).

**A. Identitas & keterlacakan**
- [ ] Setiap riset aktif memiliki Research ID `UIAI-YYYY-NNN` di judul Issue, README riset, dan Mission Control.
- [ ] Dataset yang dipakai memiliki `DS-YYYY-NNN` dengan lisensi dan privasi terisi.
- [ ] Publikasi/artefak memiliki `PUB-`/`ART-` dan menunjuk ke Research ID.

**B. Bukti proses akademik**
- [ ] Setiap gate yang diklaim lolos memiliki PR `GATE REVIEW:*` merged dengan komentar reviewer.
- [ ] Rubrik 5E terisi untuk setiap tim pada akhir semester.
- [ ] Notulen red team (W8) dan defense (W16) tersimpan.
- [ ] Handoff Metopen → TA terisi untuk setiap tim yang lolos G8.

**C. Integritas & etika**
- [ ] Integrity checklist ditandatangani sebelum defense/submission.
- [ ] `AI-USAGE.md` dan AI Usage Log ada di setiap repo riset.
- [ ] `docs/ethics.md` ada untuk riset dengan data manusia/partner.
- [ ] Tidak ada data mentah/sensitif di history repo (pemeriksaan sampel).

**D. Luaran & dampak**
- [ ] Release milestone sesuai gate (v0.1 … v1.0) ada di setiap repo riset.
- [ ] Registry publikasi dan dataset diperbarui sampai tanggal pelaporan.
- [ ] Faculty Portfolio mencerminkan mentor yang benar-benar mereview.

**E. Tata kelola & dokumen**
- [ ] Dokumen Tier 1 memiliki status dan versi yang benar; CHANGELOG mutakhir.
- [ ] Notulen rapat bulanan dan evaluasi semester tersimpan.
- [ ] Risk register ditinjau pada semester berjalan.
- [ ] Fakta institusional dalam dokumen yang akan dilaporkan telah diverifikasi (RSK-14).
- [ ] `python3 tools/check_links.py` lulus pada tag yang dilaporkan.

**F. Paket ekspor**
- [ ] Ekspor Mission Control (CSV) dengan tanggal.
- [ ] Laporan KPI semester 1 halaman + lampiran.
- [ ] Salinan registry (backlog, dataset, publikasi) pada tag pelaporan.
- [ ] Daftar PR gate dan release per Research ID.

## 5. Contoh jejak satu riset sebagai evidence

```
UIAI-2026-001  "[isi judul riset]"
├─ Issue #12  type:problem, cluster:applied, domain Education   (2026-09-15)  ← activity 1–2
├─ PR #3   GATE REVIEW: Problem Ready   merged 2026-09-22, reviewer: dosen pengampu + peer
├─ Release v0.1 Problem Validated        2026-09-22
├─ PR #7   GATE REVIEW: Evidence Ready   merged 2026-10-13; references.bib 22 sumber terverifikasi
├─ Release v0.2 Evidence Ready
├─ PR #11  GATE REVIEW: Method Ready     merged 2026-10-27; notulen red team W8; mentor: [isi]
├─ Release v0.3 Research Design
├─ DS-2026-001  dataset terdaftar (CC BY 4.0, tanpa data pribadi)
├─ PR #15  GATE REVIEW: Experiment Ready merged 2026-11-10; reproduksi peer: tim B
├─ Release v0.5 Pilot Experiment
├─ PR #19  GATE REVIEW: Contribution Ready merged 2027-01-12; integrity checklist; defense W16
├─ Release v1.0 Research Pack; handoff ke TA supervisor [isi]
└─ (TA, 2027)  PUB-2027-001 submitted → accepted; Release v2.0 Published
```

Satu jejak ini sekaligus menjadi bukti untuk: OBE/asesmen (PR gate + rubrik), PjBL/Team-Based Project (git history), keterlibatan dosen (mentor sebagai reviewer), tata kelola data (DS-), integritas (checklist, AI-USAGE), kelanjutan TA (handoff), dan publikasi (PUB-). Tidak ada satu pun yang dibuat khusus untuk laporan.

## 6. Yang perlu diverifikasi sebelum dipakai formal

| Item | Status | Tindak lanjut |
|---|---|---|
| Nama resmi program pendanaan (PP-PTS) dan komponen laporannya | Belum diverifikasi | Admin riset + tim PP-PTS; perbarui kolom terakhir §1 |
| Format dan periode laporan akreditasi LAM-INFOKOM yang relevan | Belum diverifikasi | Tim penjaminan mutu; selaraskan §4 |
| Kebijakan universitas tentang penyimpanan evidence yang memuat nama mahasiswa | Belum diverifikasi | Simpan ekspor di folder internal; tanyakan unit terkait |
| Pengakuan review PR gate sebagai pembimbingan dalam BKD | Belum diputuskan | [MST-01 §6](../00-master/01-executive-summary.md) butir 7 |

Dokumen ini diperbarui setiap kali format pelaporan berubah, lewat PR dan catatan di [CHANGELOG.md](../../CHANGELOG.md).
