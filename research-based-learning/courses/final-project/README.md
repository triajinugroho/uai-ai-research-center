# Tugas Akhir (TA) — Course Research Guide

**Status** Draft v0.1 (2026-09) · Mengikuti angkatan pertama Metopen Studio — artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [Metopen](../research-methods/README.md) · [ARC-04 Build–Prove–Contribute](../../../research-os/02-academic-architecture/04-build-prove-contribute.md) · [ARC-06 Research Output Taxonomy](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md) · [MET-04 Research Pack](../../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-05 Publication Backward Design](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md) · [OPS-03 Research Gates](../../../research-os/06-execution-os/03-research-gates.md) · [AIR-01 AI Research Center Concept](../../../research-os/03-ai-research-ecosystem/01-ai-research-center-concept.md) · [Assessment](../../assessment/README.md)

## 1. Identitas mata kuliah

| Field | Nilai |
|---|---|
| Nama | Tugas Akhir |
| Semester | VIII |
| SKS | 4 |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **R — Research-Producing** |
| Tahap ([ARC-04](../../../research-os/02-academic-architecture/04-build-prove-contribute.md)) | **CONTRIBUTE** — contribution stage |
| Tahun spiral ([ARC-01](../../../research-os/02-academic-architecture/01-research-capability-spiral.md)) | Year 4 — Prove & Contribute |
| Prasyarat yang diasumsikan | Research Pack Metopen dengan status minimal **TA Ready** (G5 lulus) |
| Klaster | Mengikuti Research ID yang diwarisi dari Metopen |
| Field **Course** di Mission Control | `TA` |
| Koordinator TA | [isi] |

*Semester dan SKS dari tabel kurikulum dokumen diskusi; verifikasi sebelum dokumen formal.*

## 2. Mengapa mode R dan mengapa "Contribute"

TA adalah tempat riset mahasiswa **berkontribusi**: menjawab RQ dengan bukti yang cukup, lalu mewariskan sesuatu — pengetahuan (manuscript), artefak (software/model/benchmark), data (dataset), atau HKI/prototype ([ARC-06](../../../research-os/02-academic-architecture/06-research-output-taxonomy.md)). Endgame minimum TA adalah laporan TA yang lulus sidang; endgame yang didorong komponen ini adalah **minimal satu output dari taksonomi selain laporan TA** untuk riset di atas *TA Ready*.

Perbedaan mendasar dengan pola TA yang sering terjadi: TA **tidak dimulai dari judul**. Ia dimulai dari Research Pack yang sudah lolos gate. Satu semester TA dipakai untuk eksperimen penuh, analisis, dan kontribusi — bukan untuk mencari metode.

## 3. Kriteria TA-ready (yang diterima pembimbing)

Mahasiswa dinyatakan **TA Ready** ketika Research Pack Metopen-nya lolos **G5 Method Ready** ([OPS-03](../../../research-os/06-execution-os/03-research-gates.md); [MST-03 §3.2](../../../research-os/00-master/03-glossary.md)). Pembimbing memeriksa Research Pack terhadap daftar berikut pada pertemuan pertama:

| Komponen Research Pack | Harus ada untuk TA Ready | Kondisi ideal (Research Ready) |
|---|---|---|
| Endgame + Research ID `UIAI-YYYY-NNN` | Ya | + kandidat venue (MET-05) |
| Problem Brief + Stakeholder/Impact | Ya | + kontak stakeholder aktif |
| Literature Evidence Map (synthesis matrix 15–25 sumber terverifikasi) | Ya | + diperbarui ≤ 6 bulan |
| Research Gap + RQ/Hypothesis + Contribution Statement | Ya | + RQ sekunder untuk TA |
| Research Design Card + Data Plan + Baseline & Metrics + Threats to Validity + Ethics | Ya (G5) | + Experiment Card yang sudah dijalankan |
| Pilot Experiment + Reproducibility README | Tidak wajib (G6) | Ya, direproduksi peer |
| Analisis + CER | Tidak wajib (G7) | Ya |
| Proposal TA + Research Pitch + Integrity Checklist + AI Usage Statement | Ya (G8 Metopen) | Ya |
| Handoff [TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) berisi *missing evidence* | Ya | Ya |

Bila salah satu komponen "harus ada" kosong, mahasiswa **belum TA Ready**: pembimbing dan koordinator TA mengembalikan ke gate yang gagal (bukan memulai judul baru). Riset yang masuk TA bukan dari Metopen (mis. pindahan, entry door Faculty Research langsung) harus menjalani G1–G5 dahulu dengan pembimbing sebagai reviewer.

## 4. Handoff dari Metopen

Handoff adalah dokumen pertama yang dibaca pembimbing. Isinya (TPL-14): **what exists** (komponen Pack + gate yang lulus + release), **missing evidence** (apa yang belum terbukti — biasanya eksperimen penuh, validitas eksternal, ukuran data), **next steps** (rencana G6–G8 TA), **owner** (mahasiswa, pembimbing, mentor klaster). Aturan: *dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol* — itulah kriteria lulus G8 Metopen.

Pemasangan pembimbing mengikuti kandidat mentor yang diidentifikasi sejak G1 dan pemetaan dosen ↔ klaster ([AIR-03](../../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md)); Mission Control field Course berubah `Metopen` → `TA`, field Faculty Mentor diisi.

## 5. Alur TA: G6 → G7 → G8 → publikasi

TA memakai gate yang sama dengan Metopen, tetapi pada skala penuh dan dengan reviewer tambahan (pembimbing, penguji). Riset yang sudah lolos G6/G7 di Metopen tidak mengulang gate itu; ia **memperluas** eksperimen dan membuka review ulang hanya bila desain berubah.

| Milestone | Minggu | Gate | Yang berbeda dari Metopen | Deliverable | Release |
|---|---|---|---|---|---|
| **M1 Intake & Plan** | 1–2 | (handoff) | Pembimbing membaca Pack; *missing evidence* menjadi rencana kerja; Experiment Card diperbarui untuk eksperimen penuh | Rencana TA 1 halaman; jadwal bimbingan; Issue `type:experiment` | — |
| **M2 Full Experiment** | 3–7 | **G6** | Data penuh (bukan subset), semua kondisi/ablation yang direncanakan, ≥ 3 seed/fold; peer/pembimbing mereproduksi baseline | `experiments/`, `results/`, log; PR `GATE REVIEW: Experiment Ready` | v0.5 (bila belum) |
| **M3 Analysis & Claim** | 8–10 | **G7** | Error analysis mendalam, ketidakpastian, signifikansi praktis, threats to validity final; klaim per RQ | `results/analysis.md`, figur final, tabel CER; PR `GATE REVIEW: Claim Ready` | — |
| **M4 Manuscript & Pack** | 11–13 | **G8** | Laporan TA + (bila endgame paper) manuscript sesuai venue target; Research Pack diperbarui; Integrity Checklist; peer review internal | `paper/`, Pack v1.0 (TA), PR `GATE REVIEW: Contribution Ready` | v0.8 → v1.0 |
| **M5 Sidang & Rilis** | 14–16 | G8 + publikasi | Sidang TA sebagai Research Defense ([TPL-13](../../../research-os/08-templates/13-research-defense-template.md)); rilis artefak/dataset; submission bila submission-ready; handoff ke AI Center | Sidang lulus; `PUB-`/`DS-`/`ART-` terdaftar; `docs/handoff.md` | v1.1 Submitted (bila ada) → v2.0 Published |

Pipeline publikasi setelah sidang (`manuscript-ready → submission-ready → submitted → accepted → published`) dikelola lewat [MET-05](../../../research-os/04-metopen-research-studio/05-publication-backward-design.md) dan [`publications/`](../../../publications/README.md). Venue dipilih dari registry venue ([TPL-06](../../../research-os/08-templates/06-publication-venue-registry-template.md)); hindari venue yang tidak jelas etika publikasinya ([GOV-04](../../../research-os/07-governance/04-risk-register.md), risiko *predatory journal*).

## 6. Peran pembimbing (dan penguji)

| Peran | Tanggung jawab dalam alur gate |
|---|---|
| **Pembimbing utama** | Membaca handoff & Pack di minggu 1; menyetujui rencana; reviewer PR G6–G8; menjaga klaim tidak melebihi bukti; memutuskan endgame publikasi bersama mahasiswa; menandatangani Integrity Checklist; mengisi handoff ke AI Center |
| **Pembimbing pendamping / mentor klaster** | Review metode & analisis; menghubungkan ke riset dosen/klaster; peer reproducer bila perlu |
| **Penguji sidang** | Menguji sebagai *research defense*: problem, evidence, method, results, claim, limitations, integritas ([TPL-13](../../../research-os/08-templates/13-research-defense-template.md)); bukan menguji hafalan |
| **Koordinator TA** | Memastikan intake hanya dari Research Pack TA Ready; memantau Mission Control view *By Course = TA*; mengumpulkan bukti untuk OBE/akreditasi |

Ritme yang disarankan: bimbingan 20 menit/mahasiswa/minggu dengan format tetap — *gate saat ini, bukti yang dihasilkan minggu ini, blocker, bukti berikutnya* (lihat [Faculty Guide §6](../../faculty-guide/README.md)). Komentar review disimpan di PR sebagai bukti proses ilmiah.

## 7. CPMK riset

TA mewarisi CPMK payung Metopen ([research-methods](../research-methods/README.md) §5) pada skala penuh. Yang khas TA ([ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md)):

| # | CPMK riset TA | Gate | Artefak | Evidence |
|---|---|---|---|---|
| T1 | Mahasiswa mampu menjalankan eksperimen penuh yang reproducible sesuai desain yang telah dipertahankan | G6 | Repositori final + reproducibility package | Reproduksi oleh pembimbing/peer |
| T2 | Mahasiswa mampu menarik kesimpulan yang dibatasi bukti, dengan threats to validity dan hasil negatif dilaporkan | G7 | `results/analysis.md`, CER | Setiap klaim menunjuk tabel/figur |
| T3 | Mahasiswa mampu menghasilkan kontribusi yang dapat diwariskan: laporan TA + minimal satu output taksonomi (untuk endgame di atas TA Ready) | G8 | Laporan TA, manuscript/dataset/artefak | `PUB-`/`DS-`/`ART-` terdaftar |
| T4 | Mahasiswa mampu mempertanggungjawabkan riset secara lisan dan etis (amanah epistemik), termasuk AI disclosure | G8 | Sidang, Integrity Checklist, AI Usage Statement | Sidang lulus; checklist ditandatangani |

## 8. Target output: proposal → manuscript → artefak

| Endgame (ditetapkan di G1 Metopen, ditinjau di M1 TA) | Output minimum TA | Output tambahan | Registry |
|---|---|---|---|
| TA Ready | Laporan TA lulus sidang + repo reproducible | — | Mission Control |
| Research Ready | + eksperimen penuh & analisis yang direproduksi | Research brief / poster | Mission Control |
| Publication Ready | + manuscript submission-ready | Conference/journal paper; dataset; benchmark | `publications/` (`PUB-`), `datasets-registry/` (`DS-`) |
| Impact Ready | + artefak dirilis / prototype / HKI / bagian riset dosen | Software, model, prototype, HKI, competition project | `publications/` (`ART-`), IP review ([LICENSING.md](../../../LICENSING.md)) |

## 9. Hubungan ke AI Research Center

TA adalah ujung *student pipeline* pusat riset ([AIR-01](../../../research-os/03-ai-research-ecosystem/01-ai-research-center-concept.md)). Tiga hubungan konkret:

1. **Handoff ke AI Center** setelah sidang ([TPL-14](../../../research-os/08-templates/14-research-handoff-template.md)): apa yang terbukti, apa yang belum, langkah berikut, owner berikutnya (dosen klaster, mahasiswa angkatan berikutnya, atau partner). TA yang selesai tanpa handoff adalah research memory yang hilang.
2. **Masuk ke riset dosen & skema penelitian internal**: TA yang selaras riset dosen menjadi bagian proposal/paper dosen (skema penelitian internal UAI mendorong keterlibatan mahasiswa — lihat catatan verifikasi di [Faculty Guide §10](../../faculty-guide/README.md)).
3. **Kembali ke backlog**: pertanyaan lanjutan yang muncul dari TA dicatat sebagai Issue *Research Problem* / *Literature Gap* baru — *new research backlog* dalam compounding loop.

## 10. Rubrik ringkas

Nilai TA mengikuti aturan Prodi; komponen ini menetapkan **standar kualitas riset** yang diperiksa pembimbing/penguji, memakai 5E ([MET-06](../../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)) + Research Integrity gate. Ringkas (4 level, irisan dengan MK lain):

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality |
|---|---|---|---|---|
| **Baseline & pembanding** | Tidak ada | Ada, lemah/dipilih belakangan | Baseline + pembanding dari desain G5 | + ablation; perbandingan dengan hasil terdahulu yang terverifikasi |
| **Metrik & evaluasi** | Metrik tunggal tanpa alasan | Selaras RQ, ketidakpastian tidak dilaporkan | Selaras RQ; variansi seed/fold; leakage dicegah | + signifikansi praktis, evaluasi multi-dimensi, threats final jujur |
| **Reproducibility** | Hasil di laptop | Kode tanpa environment | Package lengkap; pembimbing menjalankan ulang | + peer eksternal mereproduksi; artefak dirilis dengan lisensi & sitasi |
| **AI disclosure & integritas** | Tidak ada log | Log tidak lengkap | Log lengkap; statement di laporan; checklist lulus | + protokol AIX-04 terlihat konsisten sejak Metopen; sitasi 100% terverifikasi |

## 11. Template yang dipakai

Seluruh paket 08 seperti Metopen (lihat [research-methods §8](../research-methods/README.md)), dengan penekanan pada [TPL-13 Defense](../../../research-os/08-templates/13-research-defense-template.md), [TPL-11 Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md), [TPL-14 Handoff](../../../research-os/08-templates/14-research-handoff-template.md), [TPL-06 Venue Registry](../../../research-os/08-templates/06-publication-venue-registry-template.md), dan PR template `manuscript-review.md` / `release-review.md`.

## 12. Catatan RPS / pedoman TA

`RPS.md` (atau suplemen pedoman TA) akan ditambahkan oleh koordinator TA; kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Perubahan minimum: syarat intake = Research Pack TA Ready; sidang = research defense; lampiran wajib = reproducibility package, AI Usage Statement, Integrity Checklist, handoff.

## 13. Pengampu

| Peran | Nama |
|---|---|
| Koordinator TA | [isi] |
| Pembimbing (per klaster) | [isi] |
| Penguji terlatih research defense | [isi] |
