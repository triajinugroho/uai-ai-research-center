# Assessment & 5E Rubric — Penilaian Metopen sebagai Milestone Portfolio

> **ID** MET-06 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu Metopen, mentor, reviewer gate (`@reviewers`), peer reviewer, mahasiswa, tim OBE Prodi
> **Terkait** [MET-02 Course Outcomes](02-metopen-course-outcomes.md) · [MET-04 Research Pack](04-research-pack-specification.md) · [MET-07 Integrity & Ethics](07-research-integrity-and-ethics.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [TPL-11 Research Integrity Checklist](../08-templates/11-research-integrity-checklist.md) · [TPL-12 Peer Review](../08-templates/12-peer-review-template.md) · [TPL-13 Research Defense](../08-templates/13-research-defense-template.md) · [MST-03 Glossary](../00-master/03-glossary.md)

## 1. Filosofi penilaian

Metopen menilai **apa yang mahasiswa hasilkan dan pertanggungjawabkan**, bukan apa yang mereka hafal. Tidak ada UTS/UAS berbentuk ujian tertulis tentang definisi penelitian. Yang ada:

1. **Milestone portfolio** — Research Pack dinilai bertahap di setiap gate lewat PR `GATE REVIEW`, dengan rubrik 5E.
2. **Research Defense** — pertanggungjawaban oral di W16 (dan Design Defense W8 sebagai bagian gate G5).
3. **Peer review** — mahasiswa dinilai juga sebagai *reviewer*, bukan hanya sebagai penulis.
4. **Partisipasi sprint** — disiplin mingguan: deliverable sprint, gate check, AI Usage Log.
5. **Research Integrity Gate** — lulus/gagal, bukan skor.

Konsekuensi desain: nilai tidak bisa "dikejar di akhir semester". Tim yang tidak lolos G3 di W5 tidak bisa menutupnya dengan proposal yang bagus di W15, karena proposal tanpa evidence map tidak akan lolos G8.

## 2. Skema nilai akhir

| Komponen | Bobot | Dinilai lewat | Kapan | Satuan |
|---|---|---|---|---|
| **A. Milestone Portfolio (Research Pack)** | **60%** | Rubrik 5E pada PR gate G1–G8 | Berjalan (W1–W16) | Tim, dimodulasi individu (§7) |
| — End | 10% | G1, G2, G4 | W1, W2, W6 | |
| — Evidence | 15% | G3, G4 | W3–W6 | |
| — Experiment | 15% | G5, G6 | W7–W10 | |
| — Explanation | 10% | G7, G8 (dokumen) | W11–W15 | |
| — Execution | 10% | Semua gate (repositori, reproducibility, disiplin gate) | W1–W16 | |
| **B. Research Defense** | **15%** | TPL-13; rubrik 5E terfokus End + Explanation | W16 | Individu (tanya-jawab) + tim (presentasi) |
| **C. Peer Review sebagai reviewer** | **10%** | Kualitas 2 review (TPL-12): spesifik, berbasis bukti, dapat ditindaklanjuti | W14 | Individu |
| **D. Partisipasi Sprint** | **15%** | Deliverable sprint tepat waktu, gate check hadir & bermakna, AI Usage Log konsisten, kontribusi terlihat di git/Issue | S0–S16 | Individu |
| **Research Integrity Gate** | **prasyarat** | Integrity check setiap gate + TPL-11 di G8 | Setiap gate | Lulus/gagal |
| **Total** | **100%** | | | |

Konversi ke nilai huruf mengikuti ketentuan Prodi (`[isi]`). Level rubrik dikonversi ke persentase komponen: Exemplary = 100%, Proficient = 85%, Developing = 70%, Beginning = 55%, tidak ada = 0%.

### 2.1 Rekonsiliasi dengan CPMK

| Komponen | CPMK yang dibuktikan ([MET-02](02-metopen-course-outcomes.md)) |
|---|---|
| A — End | 01 Problem, 05 RQ, 06 Hypothesis |
| A — Evidence | 02 Discovery, 03 Synthesis, 04 Gap |
| A — Experiment | 07 Methods, 08 Experiment, 06 Hypothesis (kriteria penolakan) |
| A — Explanation | 09 Validity, 12 Writing |
| A — Execution | 08 Experiment (reproducibility), 10 AI-Assisted |
| B — Defense | 13 Defense, 01, 09 |
| C — Peer Review | 12 Writing (sebagai reviewer), 03 Synthesis |
| D — Partisipasi | 10 AI-Assisted, disiplin semua CPMK |
| Integrity Gate | 11 Research Integrity |

## 3. Rubrik 5E

Empat level: **Exemplary (4) · Proficient (3) · Developing (2) · Beginning (1)**. Proficient adalah standar "TA Ready". Exemplary adalah standar "Research/Publication Ready". Developing berarti gate belum lulus dan perlu revisi; Beginning berarti artefak belum ada secara substantif.

### 3.1 E1 — End (kejelasan endgame & problem)

**Bobot** 10% · **Artefak** `docs/endgame.md`, Problem Brief, Stakeholder/Impact, RQ/Hypothesis, Contribution Statement · **Gate/minggu** G1 (W1), G2 (W2), G4 (W6)

| Level | Kriteria konkret |
|---|---|
| Exemplary | Endgame spesifik (TA + aspirasi paper/artefak realistis) dan entry door jelas; masalah problem-first dengan stakeholder nyata dan keputusan yang berubah dinyatakan; RQ spesifik, terbatas, dapat difalsifikasi, tertelusur ke gap; kontribusi disebut jenisnya dan sepadan dengan rencana bukti; orang luar mengulang masalah dalam dua kalimat tanpa kesulitan |
| Proficient | Endgame dan entry door jelas; masalah problem-first dengan stakeholder disebut; RQ spesifik dan tertelusur ke gap; kontribusi disebut jenisnya; sedikit kelonggaran pada batas RQ |
| Developing | Endgame masih "membuat aplikasi X"; masalah sebagian solution-first; RQ terlalu luas atau tidak bisa salah; kontribusi generik ("menerapkan M di konteks baru") |
| Beginning | Belum ada endgame/problem brief yang substantif; RQ berupa judul; tidak ada stakeholder |

### 3.2 E2 — Evidence (kualitas bukti literatur)

**Bobot** 15% · **Artefak** search strategy, synthesis matrix, Literature Evidence Map, `references.bib`, Research Gap · **Gate/minggu** G3 (W3–W5), G4 (W6)

| Level | Kriteria konkret |
|---|---|
| Exemplary | Strategi pencarian terdokumentasi dan direplikasi reviewer; ≥20 sumber primer relevan dan benar-benar dibaca; matriks memperlihatkan pola (konsisten/bertentangan/belum diuji) dan kualitas bukti tiap sumber; gap merujuk baris spesifik dan jenis gap jelas; semua sumber terverifikasi; sumber dari AI dicatat dan diverifikasi |
| Proficient | Strategi tertulis; 15–25 sumber terverifikasi; matriks lengkap 7 kolom; pola dinyatakan; gap tertelusur ke matriks; spot-check reviewer cocok dengan paper |
| Developing | <15 sumber atau sebagian sekunder; matriks berupa ringkasan per paper tanpa pola; gap naratif; ≥1 baris matriks tidak cocok dengan paper saat spot-check |
| Beginning | Daftar pustaka tanpa matriks; sumber tidak terverifikasi; tidak ada strategi pencarian |

*Catatan:* satu referensi yang tidak dapat diverifikasi keberadaannya membuat **gate G3 gagal** terlepas dari level (aturan integritas), bukan sekadar menurunkan level.

### 3.3 E3 — Experiment (kualitas desain & pilot)

**Bobot** 15% · **Artefak** Research Design Card, Data Plan, Baseline & Metrics, Experiment Card, Pilot Experiment, catatan reproduksi peer · **Gate/minggu** G5 (W7–W8), G6 (W9–W10)

| Level | Kriteria konkret |
|---|---|
| Exemplary | Metode dipilih dari Methods Map dengan alternatif yang ditolak; variabel/kontrol/sampling eksplisit; baseline dan metrik ditetapkan sebelum eksperimen dengan justifikasi; protokol evaluasi mencegah leakage; data plan mencakup lisensi/privasi/representativitas; pilot berjalan dengan ≥3 seed, baseline + pembanding, direproduksi peer tanpa bantuan tim; red team W8 dijawab dengan perubahan desain yang tercatat |
| Proficient | Desain lengkap dan bisa dijalankan orang lain; baseline & metrik ada sebelum eksperimen; pilot end-to-end pada subset dengan baseline + 1 pembanding; direproduksi peer (boleh dengan sedikit bantuan); threats v1 ada |
| Developing | Baseline atau metrik ditetapkan setelah melihat hasil; pilot berjalan hanya di satu mesin; data plan tanpa lisensi/privasi; kontrol tidak jelas |
| Beginning | Tidak ada baseline; pilot tidak berjalan; desain berupa "metode kuantitatif" tanpa prosedur |

### 3.4 E4 — Explanation (argumentasi claim–evidence–reasoning)

**Bobot** 10% (portfolio) + fokus Defense · **Artefak** `results/analysis.md`, CER table, Threats v2, Contribution revisi, Proposal TA, figur · **Gate/minggu** G7 (W11–W12), G8 (W13–W15)

| Level | Kriteria konkret |
|---|---|
| Exemplary | Setiap klaim menunjuk tabel/figur tertentu dengan ketidakpastian; error analysis menjelaskan di mana dan mengapa metode gagal; hasil negatif dilaporkan dan dimaknai; threats v2 spesifik dengan mitigasi dan sisa risiko; kontribusi direvisi turun bila bukti lemah; proposal konsisten penuh dengan repositori; visualisasi jujur; "so what" bagi stakeholder jelas |
| Proficient | CER per RQ ada; klaim tidak melebihi bukti; threats v2 ada; proposal mengikuti struktur dan konsisten dengan `results/`; figur menampilkan baseline |
| Developing | Klaim sebagian tidak menunjuk bukti; klaim kausal dari korelasi; threats tidak diperbarui; hasil negatif disembunyikan atau tidak dibahas; figur menyesatkan (skala, cherry-picking) |
| Beginning | Tidak ada analisis; proposal tidak sesuai dengan repositori; klaim tanpa bukti |

### 3.5 E5 — Execution (disiplin sprint, repositori, gate)

**Bobot** 10% (portfolio) + komponen D · **Artefak** repositori, Reproducibility README, AI Usage Log, riwayat PR gate, release · **Gate/minggu** semua

| Level | Kriteria konkret |
|---|---|
| Exemplary | Repositori mengikuti TPL-15 penuh; README membuat peer menjalankan tanpa bertanya; environment/seed/config terkelola; commit kecil bermakna dengan Research/Task ID; semua gate lewat PR tepat waktu atau dengan revisi cepat; release sesuai milestone; AI Usage Log lengkap, kontemporer, dan spesifik; label & Mission Control selalu mutakhir |
| Proficient | Struktur standar; README cukup untuk reproduksi dengan sedikit bantuan; PR gate lengkap; AI Usage Log ada dan konsisten; release dibuat |
| Developing | Struktur tidak lengkap; hasil di luar repositori; PR gate terlambat >1 sprint tanpa komunikasi; AI Usage Log diisi belakangan/tidak spesifik |
| Beginning | Repositori nyaris kosong; tidak ada PR gate; tidak ada AI Usage Log |

## 4. Research Integrity Gate (lulus/gagal)

Integritas **tidak diberi skor** karena skor menyiratkan "sedikit fabrikasi masih dapat nilai". Ketentuannya:

| Aspek | Ketentuan |
|---|---|
| Kapan diperiksa | Setiap PR gate (reviewer mencentang bagian integritas), dan TPL-11 di G8 |
| Yang membuat gagal | Fabrikasi/falsifikasi data atau hasil; plagiarisme; sitasi tidak ada/tidak dibaca; AI tidak diungkap padahal memengaruhi kesimpulan; data pribadi/sensitif di-commit; metric switching/seed cherry-picking yang disembunyikan; hasil negatif disembunyikan ([MET-07](07-research-integrity-and-ethics.md)) |
| Akibat pada gate | Gate gagal terlepas dari level 5E; PR tidak di-merge |
| Akibat pada nilai | Nilai komponen A untuk gate itu ditangguhkan sampai remediasi; pelanggaran berat (fabrikasi, plagiarisme berat) ditangani sebagai pelanggaran kode etik ([CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)) dan kebijakan akademik Prodi (`[isi]`), dapat berujung nilai E |
| Remediasi | Kesalahan tidak disengaja (sitasi keliru, log AI kurang) diperbaiki dalam satu sprint dan dicatat; pelanggaran disengaja tidak dapat "diperbaiki" dengan mengganti artefak |
| Prinsip | Amanah epistemik: kejujuran terhadap kebenaran meskipun meruntuhkan hipotesis sendiri |

## 5. Remedial dan revisi

1. **Gate gagal bukan hukuman.** Reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan (OPS-03 aturan 4). Tim merevisi dan membuka review ulang.
2. **Batas revisi:** maksimal dua review ulang per gate dalam semester; lebih dari itu, dosen memutuskan apakah ruang lingkup riset harus dikecilkan.
3. **Nilai setelah revisi:** level 5E dinilai pada versi yang lulus (kualitas), tanpa potongan; keterlambatan tercatat di E5 Execution dan komponen D, sehingga revisi tidak "gratis" tetapi tidak menghukum kualitas akhir.
4. **Batas waktu keras:** G5 harus lulus paling lambat W9; G6 paling lambat W11; G8 di W16. Tim yang tidak mencapai G5 pada W9 mendapat sesi konsultasi wajib dan penyempitan ruang lingkup.
5. **Remedial akhir semester:** hanya untuk komponen B (defense ulang) dan artefak G8 yang belum lengkap, dalam jendela yang ditetapkan Prodi (`[isi]`); tidak ada remedial berupa "tugas tambahan" di luar Research Pack.

## 6. Penilaian tim vs individu

| Komponen | Unit | Cara memodulasi individu |
|---|---|---|
| A Portfolio | Tim | Nilai tim × faktor kontribusi individu (0,8–1,1) dari: riwayat git (commit/PR bermakna, bukan jumlah baris), Issue/PR yang ditangani, AI Usage Log pribadi, peer contribution rating di W8 dan W16, observasi studio. Selisih >0,2 antar anggota harus disertai bukti tertulis |
| B Defense | Tim + individu | Presentasi dinilai tim; tanya-jawab dinilai per orang (setiap anggota wajib menjawab minimal satu pertanyaan penguji) |
| C Peer Review | Individu | Setiap mahasiswa menulis review sendiri |
| D Partisipasi | Individu | Kehadiran & kualitas gate check, deliverable sprint pribadi, log AI |
| Integrity | Individu & tim | Pelanggaran individu ditangani per orang; artefak tim yang tercemar tetap harus diperbaiki tim |

Kontribusi yang tidak terlihat di git, Issue, log, atau notulen dianggap tidak ada — ini bagian dari pelajaran *inspectable research*.

## 7. Kalibrasi antar penilai

1. **Anchor samples.** Sebelum semester, dosen dan reviewer menilai bersama 2–3 contoh artefak (satu Exemplary, satu Developing) per E untuk menyamakan persepsi; hasilnya disimpan di `metopen-research-studio/rubrics/` sebagai acuan.
2. **Double-marking.** Minimal 20% PR gate dinilai dua penilai; selisih ≥1 level didiskusikan sampai sepakat, dan alasan dicatat di PR.
3. **Peer reviewer terlatih.** Mahasiswa `@reviewers` memakai TPL-12 dan hanya memberi rekomendasi; keputusan lulus/gagal oleh dosen.
4. **Konsistensi lintas gate.** Reviewer yang sama mengikuti satu tim dari G3 sampai G7 bila memungkinkan, agar konteks tidak hilang.
5. **Audit akhir.** Di W16, dosen memeriksa distribusi level per E; bila satu E menumpuk di Exemplary tanpa artefak yang menjustifikasi, rubrik dan penilaian ditinjau.
6. **Transparansi.** Rubrik ini dibagikan ke mahasiswa di S0; tidak ada kriteria tersembunyi.

## 8. Contoh penilaian satu tim (ilustratif)

Tim `[isi]`, Research ID `UIAI-2026-0NN`, 2 anggota (A dan B), endgame TA + aspirasi paper.

**A. Portfolio (60%)**

| E | Level tim | Persentase | Bobot | Skor |
|---|---|---|---|---|
| End | Proficient (masalah kuat; RQ pendukung agak luas) | 85% | 10 | 8,5 |
| Evidence | Exemplary (22 sumber, matriks berpola, gap ke baris 4/9/12) | 100% | 15 | 15,0 |
| Experiment | Proficient (baseline + 1 pembanding, 3 seed, direproduksi peer dengan sedikit bantuan) | 85% | 15 | 12,75 |
| Explanation | Developing → direvisi ke Proficient di G7 ulang (klaim awal melebihi bukti, diperbaiki) | 85% | 10 | 8,5 |
| Execution | Proficient (README baik; PR G6 terlambat 1 sprint dengan komunikasi) | 85% | 10 | 8,5 |
| **Subtotal tim** | | | **60** | **53,25** |

Faktor kontribusi: A = 1,0 (memimpin eksperimen & analisis, log AI lengkap); B = 0,9 (menulis literatur & proposal, kontribusi kode lebih kecil, log AI kurang spesifik di S9–S10). A: 53,25; B: 47,9.

**B. Defense (15%)**: presentasi tim Proficient (85% × 10 = 8,5); tanya-jawab A Exemplary (100% × 5 = 5,0), B Proficient (85% × 5 = 4,25). A: 13,5; B: 12,75.

**C. Peer review (10%)**: A Proficient (8,5); B Exemplary (10,0) — review B sangat spesifik dan berbasis bukti.

**D. Partisipasi (15%)**: A 14,0; B 12,5 (dua deliverable sprint terlambat).

**Integrity gate**: lulus di semua gate; TPL-11 ditandatangani.

| Mahasiswa | A | B | C | D | Total |
|---|---|---|---|---|---|
| A | 53,25 | 13,5 | 8,5 | 14,0 | **89,25** |
| B | 47,9 | 12,75 | 10,0 | 12,5 | **83,15** |

Status kematangan tim: **Research Ready** (G7 lulus, pilot direproduksi); handoff mencatat eksperimen penuh sebagai *missing evidence* untuk TA.

## 9. Ringkasan untuk mahasiswa

- Nilai datang dari **artefak yang lolos gate**, bukan dari ujian.
- **Proficient di semua E = TA Ready.** Exemplary = jalur Research/Publication Ready.
- Integritas bukan komponen nilai; ia **syarat** nilai.
- Revisi diperbolehkan dan normal; keterlambatan tercatat di Execution.
- Kontribusi yang tidak terlihat di repositori dianggap tidak ada.
