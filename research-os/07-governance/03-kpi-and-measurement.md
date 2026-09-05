# KPI & Measurement — Mengukur Kematangan Riset, Bukan Aktivitas

> **ID** GOV-03 · **Paket** 07 Governance & Implementation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, kepala AI Research Center, dosen pengampu Metopen, admin riset, tim PP-PTS/akreditasi, reviewer hibah
> **Terkait** [GOV-02 Implementation Roadmap](02-implementation-roadmap.md) · [GOV-04 Risk Register](04-risk-register.md) · [GOV-05 PP-PTS Evidence](05-ppts-and-institutional-evidence.md) · [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [TPL-03 Research Leaderboard](../08-templates/03-research-leaderboard-template.md)

KPI di sini mengukur **kematangan riset dan kualitas bukti**, bukan jumlah aktivitas. Semua data diambil dari yang sudah ada di alur kerja — Issue, PR gate, release, Mission Control, registry — sehingga pengukuran tidak menambah pekerjaan (prinsip P1). Target angka bersifat **usulan** dan disepakati Prodi pada evaluasi Phase 1; target 2030 mengikuti horizon [`research-roadmap/2026-2030/`](../../research-roadmap/2026-2030/README.md).

Kode KPI: `KPI-L-NN` leading, `KPI-I-NN` intermediate, `KPI-G-NN` lagging, `KPI-Q-NN` kualitas & integritas.

---

## 1. Leading indicators (dalam semester; memprediksi hasil)

| ID | KPI | Definisi | Formula | Sumber data | Frekuensi | Target pilot | Target 2030 | Pemilik |
|---|---|---|---|---|---|---|---|---|
| KPI-L-01 | % Research One-Pager | Tim yang One-Pager v0-nya disetujui pada G2 (W2) | tim dengan One-Pager v0 disetujui ÷ total tim | PR `GATE REVIEW: Problem Ready` merged; [TPL-01](../08-templates/01-research-one-pager-template.md) | W2, W6 | 100% | 100% | Dosen pengampu |
| KPI-L-02 | % validated RQ | Tim yang RQ-nya lolos G4 pada W6 (ditelusuri ke synthesis matrix) | tim lolos G4 pada/ sebelum W6 ÷ total tim | Label `gate:G4-question`; Issue `type:research-question` | W6 | ≥90% | ≥95% | Dosen pengampu, mentor |
| KPI-L-03 | % repositories | Tim dengan repo standar [TPL-15](../08-templates/15-research-repository-template.md) aktif (≥1 commit/minggu) dan reproducibility package di W9 | repo memenuhi struktur + commit rutin ÷ total tim | Repo `proj-*`; git log | W1, W9 | 100% | 100% | Admin riset |
| KPI-L-04 | % pilot experiments | Tim yang pilot experiment-nya lolos G6 pada W10 (berjalan end-to-end, direproduksi peer) | tim lolos G6 ÷ total tim | Label `gate:G6-experiment`; release v0.5 | W10 | ≥70% | ≥90% | Dosen pengampu |
| KPI-L-05 | % gate review dalam SLA | PR `GATE REVIEW:*` yang mendapat keputusan ≤5 hari kerja | PR gate diputuskan dalam SLA ÷ total PR gate | Timestamp PR (opened → merged/closed) | Bulanan | ≥80% | ≥95% | Admin riset |
| KPI-L-06 | % evidence completeness | Research ID dengan jejak lengkap: Issue + PR gate untuk gate yang diklaim + release milestone | Research ID lengkap ÷ total Research ID aktif | Mission Control + repo | Bulanan | ≥90% | 100% | Admin riset |
| KPI-L-07 | % AI Usage Log terisi | Tim yang AI Usage Log-nya diperbarui setiap sprint (S1–S16) | sprint dengan log terisi ÷ (jumlah tim × jumlah sprint) | [TPL-10](../08-templates/10-ai-usage-log-template.md) di repo; sprint review | Mingguan | ≥85% | ≥95% | Dosen pengampu |
| KPI-L-08 | % mentor terpasang | Tim dengan dosen mentor tercatat di Mission Control pada W2 | tim dengan Faculty Mentor terisi ÷ total tim | Field Faculty Mentor | W2 | 100% | 100% | AI Research Center |

## 2. Intermediate indicators (akhir semester sampai satu tahun)

| ID | KPI | Definisi | Formula | Sumber data | Frekuensi | Target pilot | Target 2030 | Pemilik |
|---|---|---|---|---|---|---|---|---|
| KPI-I-01 | Research Packs (TA Ready & lengkap) | Tim yang merilis `v1.0 Research Pack` (lolos G8) pada akhir Metopen; sekaligus 100% TA Ready (lolos G5) sebagai syarat lulus | tim dengan release v1.0 ÷ total tim; tim lolos G5 ÷ total tim | Release; label `gate:G8-contribution` | Akhir semester | ≥80% v1.0; 100% G5 | ≥95% v1.0; 100% G5 | Dosen pengampu |
| KPI-I-02 | TA continuation | Mahasiswa yang TA-nya melanjutkan Research ID Metopen tanpa ganti topik/metode | TA dengan Research ID sama ÷ mahasiswa Metopen yang mengambil TA | Handoff [TPL-14](../08-templates/14-research-handoff-template.md); data TA Prodi; Mission Control | Semester berikutnya | ≥70% | ≥90% | Koordinator TA |
| KPI-I-03 | Student–faculty research | Riset mahasiswa yang terikat riset dosen (mentor aktif mereview ≥3 gate, atau masuk skema penelitian internal) | riset terikat dosen ÷ total riset mahasiswa | Faculty Portfolio; PR review; proposal hibah | Semester | ≥40% | ≥60% | AI Research Center |
| KPI-I-04 | % Research Ready | Tim yang lolos G7 (klaim didukung bukti, pilot direproduksi) | tim lolos G7 ÷ total tim | Label `gate:G7-claim` | Akhir semester | ≥50% | ≥75% | Dosen pengampu |
| KPI-I-05 | Research asset reuse | Riset baru yang memakai ≥1 asset terdaftar dari riset sebelumnya (dataset, kode, literature map) | riset dengan reuse tercatat di One-Pager/README ÷ total riset baru | Entry door Dataset/Course Project; README riset; registry | Semester | ≥20% (angkatan 2) | ≥50% | Admin riset |
| KPI-I-06 | MK mode R aktif | Mata kuliah yang menghasilkan `research-artifact.md` dan/atau Issue backlog pada semester berjalan | jumlah MK mode E/R dengan artefak nyata | [`research-based-learning/courses/`](../../research-based-learning/README.md) | Semester | 1 (AI/ML, Phase 2) | ≥5 | Tim kurikulum |
| KPI-I-07 | Handoff completeness | Handoff antar tahap yang terisi lengkap (what exists, missing evidence, next steps, owner) | handoff lengkap ÷ total perpindahan tahap | [TPL-14](../08-templates/14-research-handoff-template.md) | Semester | ≥80% | 100% | Dosen pengampu, TA supervisor |

## 3. Lagging indicators (satu tahun ke atas; dampak)

| ID | KPI | Definisi | Formula | Sumber data | Frekuensi | Target pilot (angkatan 1, diukur 2027–2028) | Target 2030 (per tahun) | Pemilik |
|---|---|---|---|---|---|---|---|---|
| KPI-G-01 | Submissions | Naskah dikirim ke venue yang terdaftar di venue registry (non-predator) | jumlah entri `PUB-` berstatus submitted | [`publications/`](../../publications/README.md); [TPL-06](../08-templates/06-publication-venue-registry-template.md) | Tahunan | ≥2 | ≥10 | AI Research Center |
| KPI-G-02 | Acceptances / publications | Naskah diterima/terbit di venue terdaftar | jumlah `PUB-` berstatus accepted/published | [`publications/PUBLICATIONS.md`](../../publications/PUBLICATIONS.md) | Tahunan | ≥1 | ≥6 | AI Research Center |
| KPI-G-03 | Dataset & artefak dirilis | Dataset `DS-` publik dengan lisensi jelas dan artefak `ART-` dirilis | jumlah DS-/ART- publik | [`datasets-registry/REGISTRY.md`](../../datasets-registry/REGISTRY.md); publications | Tahunan | ≥1 | ≥5 | Pengelola registry |
| KPI-G-04 | HKI | Kekayaan intelektual terdaftar dari riset pipeline (setelah IP review) | jumlah HKI dengan Research ID | Registry; catatan IP review | Tahunan | 0–1 | ≥2 | AI Research Center |
| KPI-G-05 | Grants | Hibah/skema penelitian (internal/eksternal) yang melibatkan mahasiswa pipeline dengan Research ID | jumlah hibah yang mencantumkan Research ID mahasiswa | Faculty Portfolio; proposal hibah | Tahunan | ≥1 | ≥4 | Kepala AI Research Center |
| KPI-G-06 | Cross-faculty / partner research | Riset aktif lintas fakultas atau dengan partner (industri/pemerintah/masyarakat) | jumlah Research ID dengan entry door Partner atau domain lintas fakultas | Mission Control | Tahunan | 0–1 | ≥3 | Kepala AI Research Center |
| KPI-G-07 | Competitions | Prestasi kompetisi yang berasal dari riset pipeline (Research ID tercatat) | jumlah prestasi dengan Research ID | Registry publikasi/artefak | Tahunan | ≥1 | ≥3 | Dosen pengampu, AI Center |

## 4. KPI kualitas & integritas

KPI ini menjaga agar angka di §1–§3 tidak dicapai dengan menurunkan standar.

| ID | KPI | Definisi | Formula | Sumber data | Frekuensi | Target pilot | Target 2030 | Pemilik |
|---|---|---|---|---|---|---|---|---|
| KPI-Q-01 | % lolos integrity gate pertama kali | Riset yang lolos Research Integrity check pada setiap gate tanpa perlu revisi integritas | gate lolos integritas pada percobaan pertama ÷ total gate review | PR gate review; [TPL-11](../08-templates/11-research-integrity-checklist.md) | Semester | ≥90% | ≥97% | Dosen pengampu |
| KPI-Q-02 | % referensi terverifikasi | Referensi pada synthesis matrix yang terbukti ada (DOI/URL valid) dan benar-benar dibaca — diaudit sampel acak ≥10 referensi per tim | referensi valid ÷ referensi sampel | `references.bib`; audit dosen/peer di G3 | W5, akhir semester | ≥98% | 100% | Dosen pengampu |
| KPI-Q-03 | % pilot direproduksi peer pertama kali | Pilot yang angka baseline-nya berhasil direproduksi peer pada percobaan pertama | reproduksi berhasil pertama kali ÷ total pilot | Catatan reproduksi peer di G6 | W10 | ≥60% | ≥85% | Dosen pengampu |
| KPI-Q-04 | % klaim dengan baseline & threats to validity | Klaim di G7/Research Pack yang menunjuk tabel/figur, memiliki baseline, dan dibahas ancaman validitasnya | klaim memenuhi tiga syarat ÷ total klaim (audit sampel) | `results/analysis.md`; tabel CER | Akhir semester | ≥85% | ≥95% | Mentor |
| KPI-Q-05 | Insiden integritas terkonfirmasi | Pelanggaran integritas yang terkonfirmasi (fabrikasi, plagiarisme, sitasi palsu, AI tidak diungkap) | jumlah kasus; % ditangani sesuai prosedur | Catatan internal ([MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md)) | Semester | 0 (semua kasus ditangani) | 0 | Kaprodi |
| KPI-Q-06 | Venue quality | Naskah yang dikirim ke venue **tidak** terdaftar/predator | jumlah kasus | Venue registry | Tahunan | 0 | 0 | AI Research Center |
| KPI-Q-07 | % AI Investigator | Mahasiswa yang mencapai level kompetensi AI Investigator dengan perilaku Governor ([AIX-02](../05-ai-augmented-research/02-ai-research-competency-framework.md)) | mahasiswa memenuhi rubrik kompetensi ÷ total | Rubrik 5E dimensi Evidence/Execution; AI Usage Log | Akhir semester | ≥70% | ≥90% | Dosen pengampu |

## 5. Cara pengukuran

1. **Sumber tunggal = GitHub.** Leading dan intermediate diambil dari label `gate:*`, PR `GATE REVIEW:*`, release, dan field Mission Control (Research Gate, Maturity, Faculty Mentor, Entry Door, Status). Lagging dari registry `publications/` dan `datasets-registry/`. Prosedur ekspor ada di [GOV-05 §3](05-ppts-and-institutional-evidence.md).
2. **Ritme.** Mingguan: KPI-L-07 di sprint review. Bulanan: KPI-L-05, L-06 di rapat Research Ops. Akhir semester: semua leading/intermediate/kualitas. Tahunan: lagging.
3. **Denominator jelas.** "Total tim" = tim yang terdaftar di S0; mahasiswa yang mengundurkan diri dicatat terpisah, bukan dihapus dari denominator.
4. **Audit sampel.** KPI-Q-02 dan Q-04 diukur dari sampel acak yang diambil dosen/peer, bukan self-report.
5. **Leaderboard** ([TPL-03](../08-templates/03-research-leaderboard-template.md)) mengurutkan **kematangan riset** (gate/maturity), bukan orang; ia adalah tampilan KPI-L/I, bukan KPI tersendiri.
6. **Laporan.** Satu halaman per semester ke Kaprodi (tabel §1–§4 dengan aktual vs target), dilampirkan pada evaluasi semester ([GOV-01 §4](01-governance-model.md)) dan menjadi lampiran evidence ([GOV-05](05-ppts-and-institutional-evidence.md)).

## 6. Peringatan anti-gaming

Setiap KPI dapat dicapai dengan cara yang salah. Aturan berikut mengikat.

| Cara gaming yang mungkin | Mengapa merusak | Pengaman |
|---|---|---|
| Meluluskan gate agar KPI-L naik | Gate menjadi formalitas; TA tetap lemah | Reviewer wajib menulis alasan; audit sampel PR gate oleh Kaprodi/AI Center tiap semester; KPI-Q-01/Q-03 mengoreksi |
| Menghitung submission ke jurnal predator/berbayar tanpa review | Reputasi rusak; melanggar P7 | KPI-G hanya menghitung venue terdaftar; KPI-Q-06 target 0 |
| Memecah satu riset menjadi banyak naskah (salami slicing) | Kontribusi menipis | Satu Research ID → publikasi dicatat per kontribusi; reviewer manuscript menilai kebaruan |
| Memaksa semua mahasiswa submit paper | Overload; naskah buruk; gaming | Publication Ready adalah aspirasi, bukan syarat lulus; tidak ada KPI "% mahasiswa submit" |
| Menghitung jumlah Issue/commit sebagai produktivitas | Aktivitas ≠ kematangan | Tidak ada KPI berbasis jumlah Issue/commit; leaderboard berbasis gate |
| Menurunkan standar integritas agar KPI-Q-01 tinggi | Integritas hancur | Integrity check punya kriteria eksplisit ([TPL-11](../08-templates/11-research-integrity-checklist.md)); satu pelanggaran = gagal |
| Menaikkan target 2030 tanpa kapasitas mentor | Overload mentor; kualitas turun | Target 2030 ditinjau tahunan bersama risk register (RSK-01, RSK-12) |
| Menjadikan leaderboard alat ranking mahasiswa/dosen | GitHub menjadi sistem kepegawaian | Leaderboard mengurutkan riset, bukan orang ([GOVERNANCE.md §9](../../GOVERNANCE.md)) |

Prinsip umumnya: **ketika target dan kualitas bertentangan, kualitas menang, dan targetnya yang direvisi** — dicatat sebagai keputusan pada evaluasi semester.

## 6.1 Contoh laporan KPI semester (format satu halaman)

Format ini diisi admin riset dari ekspor GitHub ([GOV-05 §3](05-ppts-and-institutional-evidence.md)) dan dibahas pada evaluasi semester. Angka di bawah hanya ilustrasi format, bukan data riil.

```
LAPORAN KPI — Metopen Research Studio
Semester: ganjil 2026/2027 (pilot)      Tim terdaftar (S0): 12      Tag repo: v0.2.0
Tanggal ekspor: [isi]                    Disusun: admin riset         Disetujui: Kaprodi

LEADING                          Aktual     Target pilot   Status   Catatan
KPI-L-01 One-Pager v0 (W2)       12/12=100%   100%          hijau
KPI-L-02 RQ tervalidasi (W6)     10/12= 83%   ≥90%          kuning   2 tim mengulang G3 (referensi tak terverifikasi)
KPI-L-04 Pilot lolos G6 (W10)     9/12= 75%   ≥70%          hijau
KPI-L-05 Gate review dalam SLA   41/52= 79%   ≥80%          kuning   bottleneck G4–G5 pada 2 mentor (RSK-12)
KPI-L-07 AI Usage Log per sprint  88%         ≥85%          hijau
KPI-L-08 Mentor terpasang (W2)   12/12=100%   100%          hijau

INTERMEDIATE                     Aktual     Target pilot   Status
KPI-I-01 Research Pack v1.0      10/12= 83%   ≥80%          hijau    100% lolos G5 (TA Ready)
KPI-I-04 Research Ready (G7)      7/12= 58%   ≥50%          hijau
KPI-I-07 Handoff lengkap         10/10=100%   ≥80%          hijau

KUALITAS & INTEGRITAS            Aktual     Target pilot   Status
KPI-Q-01 Integrity lolos pertama 49/52= 94%   ≥90%          hijau
KPI-Q-02 Referensi terverifikasi 117/120=98%  ≥98%          hijau    audit sampel W5 + akhir semester
KPI-Q-03 Reproduksi peer pertama  6/9 = 67%   ≥60%          hijau
KPI-Q-05 Insiden integritas       0           0             hijau

KEPUTUSAN EVALUASI SEMESTER
1. Tambah 1 reviewer @reviewers untuk G4–G5; batas 5 tim per mentor (RSK-12).
2. Audit referensi dimajukan ke W4 untuk mencegah pengulangan G3.
3. Lanjut ke Phase 2 (exit criteria Phase 1 terpenuhi: ≥80% G8, handoff diterima TA supervisor).
```

Status: hijau = mencapai target; kuning = meleset ≤15% dari target; merah = meleset >15% atau KPI-Q-05/Q-06 >0. Setiap status kuning/merah wajib disertai catatan dan rujukan risiko ([GOV-04](04-risk-register.md)).

## 7. Hubungan dengan dokumen lain

- Rantai sebab-akibat yang dijelaskan KPI ini: [STR-05](../01-strategic-foundation/05-theory-of-change.md).
- Target per fase: [GOV-02](02-implementation-roadmap.md).
- Risiko yang dipantau bersama KPI: [GOV-04](04-risk-register.md) (early warning signal banyak yang berupa KPI di dokumen ini).
- Cara KPI menjadi evidence PP-PTS/akreditasi: [GOV-05](05-ppts-and-institutional-evidence.md).
- Tracker per tim dan leaderboard: [TPL-02](../08-templates/02-research-mission-tracker-template.md), [TPL-03](../08-templates/03-research-leaderboard-template.md).
