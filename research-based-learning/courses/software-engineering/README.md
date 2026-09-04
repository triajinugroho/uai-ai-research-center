# Rekayasa Perangkat Lunak (Rumpun RPL · Pengujian PL · Proyek PL) — Course Research Guide

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [ARC-01 Capability Spiral](../../../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-02 Curriculum Research Map](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-05 CPL–CPMK–Artifact](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [AIR-02 AI Research Clusters](../../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [Assessment](../../assessment/README.md)

## 1. Identitas mata kuliah

Folder ini menampung **rumpun rekayasa perangkat lunak**: satu MK jangkar dan dua MK lanjutan yang memakai pola artefak yang sama. Nilai field **Course** di Mission Control untuk ketiganya: `RPL`.

| Field | MK jangkar | MK lanjutan 1 | MK lanjutan 2 |
|---|---|---|---|
| Nama | Rekayasa Perangkat Lunak (RPL) | Pengujian Perangkat Lunak | Proyek Perangkat Lunak |
| Semester | IV | V | VI |
| SKS | [isi] | [isi] | 4 |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **E → R** (E pada semester pertama integrasi; R bila proyek menghasilkan research-grade software terdaftar) | **E** | **E → R** |
| Tahun spiral | Year 2 — Build & Compare | Year 3 — Experiment & Evaluate | Year 3 |
| Entry door yang dibuka | Course Project | Course Project | Course Project / Partner |
| Klaster utama | C2 AI Systems, Software & Security | C2 | C2 / C4 (prototype berdomain) |
| Pengampu | [isi] | [isi] | [isi] |

*Semester dan SKS dari tabel kurikulum dokumen diskusi (Proyek PL 4 SKS; SKS RPL dan Pengujian PL tidak disebut). Verifikasi sebelum dokumen formal.*

## 2. Mengapa mode E → R

Dokumen sumber menempatkan Software Engineering pada value chain sebagai **research-grade software engineering**: kemampuan membuat software yang dapat diperiksa, diuji, dan dipakai ulang orang lain. Di computing, software adalah produk riset yang sah — bersama dataset, benchmark, dan model — dan komunitas ilmiah (mis. praktik *artifact review & badging* ACM yang dirangkum dokumen diskusi) menghargai artefak yang *documented, complete, executable/reusable*.

Rumpun ini tidak diminta melakukan riset. Ia diminta menghasilkan **software yang layak menjadi bagian riset**: evaluation harness, pipeline data, tool anotasi, prototype AI untuk domain nyata — lengkap dengan **testing evidence** dan **artifact README**. Karena itu mode awalnya E (memakai kasus AI/riset sebagai objek proyek), dan naik ke R ketika artefaknya terdaftar sebagai `ART-` atau dipakai riset lain.

Pembagian peran dalam rumpun:

| MK | Fokus research-grade | Artefak utama |
|---|---|---|
| RPL (sem. IV) | Repositori terstruktur, requirement dari problem nyata, dokumentasi cara menjalankan, pengujian dasar | Research-grade software v0 + artifact README |
| Pengujian PL (sem. V) | Testing evidence untuk sistem ML/LLM: unit/integration, metamorphic testing, regression pada model, evaluasi robustness | Test suite + protokol evaluasi + laporan bukti pengujian |
| Proyek PL (sem. VI) | Prototype AI untuk domain nyata + evaluasi pengguna + AI Usage Statement | Prototype + laporan evaluasi pengguna; kandidat `ART-` |

## 3. Peran dalam research value chain

[ARC-02](../../../research-os/02-academic-architecture/02-curriculum-research-map.md): Software Engineering → *research-grade software engineering*; Security/Testing → *AI safety/security & testing AI systems*. Kompetensi ARC-01 yang menjadi tanggung jawab rumpun ini:

- **Research-grade engineering** (Year 2): repositori terstruktur, pengujian, dokumentasi cara menjalankan; peer dapat menjalankan mengikuti README.
- **Testing AI systems** (Year 3): pengujian sistem berbasis ML/LLM, metamorphic testing, regression pada model.
- **Prototype engineering dengan evaluasi** (Year 3): membangun prototype AI untuk domain nyata dan mengevaluasinya dengan pengguna.
- **Contribution & dissemination**: artefak dipakai ulang tim lain; lisensi ditetapkan ([LICENSING.md](../../../LICENSING.md)).

## 4. CPMK riset yang ditambahkan

Kerangka [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). R1–R2 untuk RPL; R3 untuk Pengujian PL; R4 untuk Proyek PL (pengampu menyesuaikan).

| # | CPMK riset (tambahan) | Learning activity | Assessment | Research artifact | Evidence |
|---|---|---|---|---|---|
| R1 | Mahasiswa mampu menurunkan requirement dari problem riset/stakeholder nyata (bukan fitur yang dibayangkan) dan menuliskannya problem-first | Studio requirement dari backlog (minggu 2–3) | Rubrik §6; review requirement | Problem/requirement brief | Requirement menunjuk Issue backlog atau stakeholder |
| R2 | Mahasiswa mampu menghasilkan software yang dapat dijalankan orang lain mengikuti README, dengan pengujian otomatis | Peer run + code review (minggu 9–10, 13) | Rubrik §6 (reproducibility) | Research-grade software + artifact README | Peer menjalankan tanpa bertanya; CI/tes lulus |
| R3 | Mahasiswa mampu merancang dan mendokumentasikan bukti pengujian untuk sistem berbasis ML/LLM (termasuk kasus non-deterministik) | Studio testing evidence | Rubrik §6 (metrik & evaluasi) | Test suite + protokol evaluasi + laporan | Laporan memuat cakupan, kasus metamorphic/regression, hasil |
| R4 | Mahasiswa mampu mengevaluasi prototype dengan pengguna nyata secara etis dan mengungkap penggunaan AI dalam pengembangan | Evaluasi pengguna (minggu 12–14) | Rubrik §6 (AI disclosure, baseline) | Laporan evaluasi pengguna + AI Usage Statement | Protokol, consent, hasil, keterbatasan |

## 5. Project guide — proyek berorientasi riset

### 5.1 Bentuk proyek

| Aspek | Ketentuan |
|---|---|
| Tema | **Software untuk riset atau software AI yang dievaluasi.** Sumber: Issue `type:problem`/`type:artifact` di [`research-backlog/BACKLOG.md`](../../../research-backlog/BACKLOG.md) (label `cluster:systems` diutamakan), kebutuhan tooling riset dosen (harness evaluasi, pipeline data, tool anotasi untuk [NLP](../nlp/README.md), dashboard eksperimen), atau prototype AI domain (C4). Proyek "aplikasi CRUD tanpa pemilik masalah" tidak diterima. |
| Tim | 3–5 mahasiswa (RPL/Proyek PL); 2–3 (Pengujian PL). Peran: product/problem owner, engineering lead, test/evidence owner, reproducibility owner. |
| Data | Bila software memproses data, data mengikuti kartu di [`datasets-registry/REGISTRY.md`](../../../datasets-registry/REGISTRY.md); tidak ada data pribadi/partner mentah di repo ([SECURITY.md](../../../SECURITY.md)). |
| Repositori | Dari [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) bila artefak riset, atau repo software standar dengan `README`, `tests/`, `docs/`, `LICENSE` (Apache-2.0), `CITATION.cff`. |
| AI | Kode bantuan AI wajib diuji; AI Usage Log sejak minggu 1 ([AIX-04](../../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)). |
| Endgame | Minimal: repo yang dapat dijalankan peer + artifact README. Target: dipakai satu riset/kelas lain. Aspirasi: rilis `ART-YYYY-NNN` lewat release review. |

### 5.2 Timeline satu semester (16 minggu, 5 milestone)

| Milestone | Minggu | Pertanyaan yang dijawab | Deliverable | Gate embrio |
|---|---|---|---|---|
| **M1 Problem & Requirement** | 3 | Masalah siapa, keputusan apa yang berubah, apa yang sudah ada (reuse before create)? | Problem/requirement brief menunjuk Issue backlog/stakeholder; survei tool yang sudah ada; repo dibuat | G2 |
| **M2 Arsitektur & Skeleton** | 6 | Bagaimana software ini akan diperiksa dan diuji orang lain? | Arsitektur, repo skeleton, pipeline tes awal, rencana testing evidence, lisensi ditetapkan | G5 (rencana evaluasi) |
| **M3 MVP + Tests** | 10 | Apakah fungsi inti berjalan dan teruji? | MVP, test suite berjalan otomatis, **peer run** mengikuti README | G6 (embrio) |
| **M4 Evidence** | 13 | Apa buktinya software ini benar/berguna? | **Testing evidence** (Pengujian PL: metamorphic/regression pada model) atau **evaluasi pengguna** (Proyek PL); perbandingan dengan alternatif/baseline sederhana; **artifact README** | G6–G7 |
| **M5 Release & Handoff** | 15–16 | Siapa yang bisa memakainya besok tanpa kita? | Release kandidat `ART-` (versi, changelog, lisensi, sitasi), AI Usage Statement, presentasi 7 menit, [handoff](../../../research-os/08-templates/14-research-handoff-template.md) | Release review, handoff |

### 5.3 Hubungan ke backlog dan datasets-registry

- Requirement selalu menunjuk ke Issue backlog atau stakeholder yang dapat dihubungi; bila tim menemukan masalah baru, tim membuka Issue *Research Problem* (atau Issue *Artifact* `type:artifact` bila kebutuhannya tooling).
- Software yang memproses dataset registry mencatat `DS-` yang dipakai di README; skrip kualitas data atau harness evaluasi yang dipakai ulang lintas kelas diajukan sebagai `ART-` ke pengelola `publications/`.
- Prototype domain (Proyek PL) yang berasal dari masalah Kerja Praktik/partner dicatat dengan entry door *Partner*.

## 6. Rubrik ringkas research-quality

Research Integrity gate berlaku lulus/gagal (termasuk atribusi kode pihak ketiga dan lisensi). Rubrik lintas MK: [Assessment](../../assessment/README.md).

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality |
|---|---|---|---|---|
| **Baseline / pembanding** | Tidak ada perbandingan dengan alternatif yang sudah ada | Alternatif disebut tanpa data | Dibandingkan dengan alternatif/baseline sederhana pada kriteria yang jelas (fungsi, kinerja, kegunaan) | Perbandingan terukur; alasan memilih membangun sendiri (bukan reuse) ditulis dan meyakinkan |
| **Metrik & evaluasi (testing evidence)** | Tidak ada tes otomatis | Tes ada, cakupan tidak diketahui | Test suite otomatis; cakupan dilaporkan; kasus non-deterministik (ML/LLM) ditangani | Metamorphic/regression testing pada model; evaluasi pengguna dengan protokol dan consent; keterbatasan dibahas |
| **Reproducibility (artifact README)** | Tidak bisa dijalankan orang lain | Bisa dijalankan dengan bantuan tim | README: instalasi, cara menjalankan, contoh, environment; peer menjalankan tanpa bertanya | Artifact README lengkap (documented, complete, executable/reusable), versi & changelog, `CITATION.cff`, lisensi; peer mereproduksi hasil evaluasi |
| **AI disclosure & integritas** | Tidak ada log; kode pihak ketiga tanpa atribusi | Log tidak lengkap | Log lengkap; kode AI diuji; lisensi dependensi diperiksa | Log memuat verifikasi; AI Usage Statement di README; tidak ada klaim melebihi bukti pengujian |

## 7. Template yang dipakai

| Kebutuhan | Template |
|---|---|
| Repositori riset | [TPL-15 Research Repository Template](../../../research-os/08-templates/15-research-repository-template.md) |
| Log AI | [TPL-10 AI Usage Log](../../../research-os/08-templates/10-ai-usage-log-template.md) |
| Evaluasi (Pengujian PL / Proyek PL) | [TPL-09 Experiment Card](../../../research-os/08-templates/09-experiment-card.md) (dipakai untuk protokol evaluasi) |
| Handoff | [TPL-14 Research Handoff](../../../research-os/08-templates/14-research-handoff-template.md) |
| Integritas | [TPL-11 Research Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md) |
| Ringkasan (bila lanjut ke riset) | [TPL-01 Research One-Pager](../../../research-os/08-templates/01-research-one-pager-template.md) |
| Rilis artefak | PR template `release-review.md` di `.github/PULL_REQUEST_TEMPLATE/` |

Kerangka *artifact README* (tujuan, klaim yang didukung, instalasi, cara menjalankan, cara mereproduksi hasil, struktur, lisensi, sitasi) dapat disimpan di `templates/` folder ini.

## 8. Catatan RPS

`RPS.md` akan ditambahkan oleh pengampu masing-masing MK (RPL, Pengujian PL, Proyek PL); kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Satu folder ini boleh memuat tiga RPS (`RPS-rpl.md`, `RPS-pengujian.md`, `RPS-proyek.md`).

## 9. Pengampu

| MK | Pengampu |
|---|---|
| RPL | [isi] |
| Pengujian Perangkat Lunak | [isi] |
| Proyek Perangkat Lunak | [isi] |
| Dosen klaster C2 mitra rumpun | [isi] |
