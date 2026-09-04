# Assessment — Asesmen Lintas Mata Kuliah

**Status** Draft v0.1 (2026-09)
**Terkait** [Hub Research-Based Learning](../README.md) · [Faculty Guide](../faculty-guide/README.md) · [Student Guide](../student-guide/README.md) · [MET-06 Assessment & 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [MET-07 Research Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [ARC-05 CPL–CPMK–Artifact Alignment](../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) · [GOV-05 PP-PTS & Institutional Evidence](../../research-os/07-governance/05-ppts-and-institutional-evidence.md) · [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md)

Dokumen ini menetapkan **standar asesmen yang sama** untuk semua mata kuliah dalam pipeline, agar nilai "baik" di Data Mining, AI/ML, Metopen, dan TA berarti hal yang sama: *bukti yang dapat dipercaya*. Rubrik per MK ada di masing-masing `courses/<mk>/README.md`; dokumen ini adalah induknya.

## 1. Prinsip: authentic assessment

Dokumen sumber menempatkan asesmen pada sweet spot **milestone portfolio + defense**, bukan UTS/UAS hafalan. Alasannya sederhana: yang ingin dibentuk adalah *scientific thinker*, dan kemampuan itu hanya terlihat ketika mahasiswa benar-benar membuat klaim, mengumpulkan bukti, dan mempertahankannya.

| Prinsip | Artinya dalam praktik |
|---|---|
| **Nilai bukti, bukan dokumen** | Yang dinilai adalah artefak yang dapat diperiksa (repo, Experiment Card, hasil reproduksi, log), bukan kerapian laporan |
| **Milestone, bukan ujian tunggal** | 4–5 milestone per semester dengan deliverable jelas; setiap milestone punya *definition of done* |
| **Defense, bukan hafalan** | Presentasi 7–10 menit + tanya jawab: "angka ini dibanding apa?", "apa yang bisa membuatnya salah?", "siapa yang sudah mereproduksi?" |
| **Prosesnya terlihat** | Commit history, PR review, AI Usage Log adalah bagian penilaian; hasil yang muncul tiba-tiba di minggu terakhir tanpa jejak tidak dapat dinilai |
| **Integritas adalah gate, bukan bobot** | Pelanggaran integritas = gagal, terlepas dari skor lain |
| **Kejujuran dihargai** | Hasil negatif dengan error analysis dan threats to validity dapat mencapai level tertinggi |

Komponen non-proyek (kuis konsep, tugas kecil) tetap boleh ada sesuai RPS; dokumen ini mengatur **komponen proyek/riset**.

## 2. Rubrik 5E sebagai standar

Rubrik induk seluruh pipeline adalah **5E** ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)) — dipakai penuh di Metopen dan TA, dan menjadi rujukan bagi rubrik ringkas MK teknis.

| E | Pertanyaan | Bukti yang diperiksa | Gate yang terkait |
|---|---|---|---|
| **End** | Apakah endgame dan masalahnya jelas, nyata, dan penting bagi seseorang? | `docs/endgame.md`, Problem Brief, Stakeholder/Impact, One-Pager | G1, G2 |
| **Evidence** | Apakah bukti literatur cukup, terverifikasi, dan disintesis (bukan diringkas satu per satu)? | Synthesis matrix, `references.bib`, Research Gap | G3, G4 |
| **Experiment** | Apakah desain, data, baseline, metrik, dan pilot layak dan reproducible? | Design Card, Experiment Card, Data Plan, pilot, catatan reproduksi peer | G5, G6 |
| **Explanation** | Apakah klaim didukung bukti dan penalaran, dengan threats to validity yang jujur? | `results/analysis.md`, CER, proposal/manuscript, defense | G7, G8 |
| **Execution** | Apakah sprint, repositori, gate, dan peer review dijalankan dengan disiplin? | Commit history, PR gate, sprint Issue, AI Usage Log, review yang ditulis | Semua |

Deskriptor level dan bobot ada di MET-06. Dokumen ini tidak menggandakannya.

## 3. Rubrik research-quality untuk mata kuliah teknis (mode E/R)

Untuk AI/ML, Data Mining, NLP, dan rumpun RPL, 5E diringkas menjadi **empat kriteria** yang merupakan irisan *Experiment* + *Explanation* + *Execution*. Ini rubrik kanonik; versi per MK di `courses/<mk>/README.md` §6 hanya menyesuaikan contoh.

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik (standar kelas) | 4 — Research-quality (layak dipakai riset lain) |
|---|---|---|---|---|
| **Baseline** | Tidak ada pembanding; artefak dibandingkan dengan dirinya sendiri | Baseline ada tetapi dipilih setelah hasil atau terlalu lemah | Baseline paling sederhana yang masuk akal, **ditetapkan sebelum eksperimen** (bukti: tanggal commit), alasan ditulis | Baseline + pembanding kuat/alternatif yang ada; angka baseline **direproduksi peer**; perbedaan dibahas secara praktis |
| **Metrik & evaluasi** | Metrik tunggal tanpa alasan; split/prosedur tidak dijelaskan | Metrik disebut; prosedur ada tetapi leakage/validitas tidak diperiksa | Metrik selaras tujuan; split/CV/protokol benar; leakage diperiksa; ≥ 3 seed/fold bila stokastik | Evaluasi multi-dimensi (kinerja + robustness/fairness/biaya/kegunaan bila relevan); ketidakpastian dilaporkan; signifikansi praktis dan threats to validity dibahas jujur |
| **Reproducibility** | Hasil hanya di laptop anggota | Kode ada; environment/seed/langkah tidak lengkap | README, environment, seed, skrip; tim sendiri menjalankan ulang dari nol | **Peer dari tim lain mereproduksi** tanpa bertanya; log eksperimen tersimpan; artefak berversi dengan lisensi & sitasi |
| **AI disclosure & integritas** | Tidak ada AI Usage Log, atau log tidak mencerminkan pekerjaan; sitasi/kode tanpa atribusi | Log ada tetapi verifikasi tidak dicatat | Log lengkap (tool, tujuan, output, verifikasi, dimasukkan/tidak); kode AI diuji; AI Usage Statement di laporan | Log menunjukkan protokol AIX-04 (verifikasi sumber/penalaran/bukti); kekeliruan AI yang ditemukan dicatat; semua referensi terverifikasi; klaim tidak melebihi bukti |

Konversi ke nilai diserahkan ke RPS. Rekomendasi: level 3 pada semua kriteria = batas "B"; level 4 pada ≥ 3 kriteria = rekomendasi handoff ke Metopen/AI Center. Kriteria **AI disclosure & integritas** di bawah level 2 memicu pemeriksaan Research Integrity gate (§4).

Mode F tidak memakai rubrik ini penuh; cukup satu kriteria yang relevan (mis. "notebook dapat dijalankan ulang" atau "bagian *apa yang tidak boleh disimpulkan* ada").

## 4. Research Integrity gate lintas mata kuliah

Berlaku di **semua** MK pipeline sebagai **lulus/gagal**, diperiksa di setiap milestone/gate ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md); [OPS-03](../../research-os/06-execution-os/03-research-gates.md) aturan 3).

| Pelanggaran | Contoh di MK teknis | Konsekuensi |
|---|---|---|
| Fabrikasi / falsifikasi | Angka hasil tidak dapat direproduksi dari kode & data yang diserahkan; log eksperimen diedit | Gagal komponen proyek; dilaporkan sesuai aturan akademik Prodi |
| Plagiarisme / kode tanpa atribusi | Menyalin repo lain tanpa lisensi/atribusi | Gagal komponen; revisi dengan atribusi bila diizinkan pengampu |
| Sitasi palsu / tidak dibaca | Referensi dari AI yang tidak ada; DOI tidak cocok | Gagal gate/milestone terkait sampai semua sitasi terverifikasi |
| AI tidak diungkap | Kode/tulisan/analisis berbantuan AI tanpa entri di AI Usage Log | Gagal milestone; pengulangan dengan log lengkap |
| Pelanggaran privasi/data | Data pribadi/partner di-commit; prompt AI berisi data sensitif | Gagal milestone; insiden ditangani sesuai [SECURITY.md](../../SECURITY.md) |
| Leakage yang disembunyikan / metrik diubah setelah hasil | Test set masuk pelatihan; metrik diganti agar "menang" | Gagal kriteria integritas; laporan harus ditulis ulang jujur |

Prosedur: pengampu mencatat temuan di PR/Issue (bukan lisan), memberi kesempatan klarifikasi, lalu memutuskan. Sebelum defense/submission, mahasiswa mengisi [TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md). Nilai UAI-nya: **amanah epistemik** — kejujuran terhadap kebenaran meskipun meruntuhkan hipotesis sendiri.

## 5. Penilaian tim vs individu

Proyek dikerjakan tim (1–3 di Metopen/TA; 2–5 di MK teknis), tetapi nilai adalah individu. Sumber bukti kontribusi individu:

| Sumber | Yang dilihat | Catatan |
|---|---|---|
| **Git log** | Distribusi commit per anggota per milestone; jenis kontribusi (kode, dokumen, eksperimen); PR yang dibuka/direview | Commit kecil rutin lebih bermakna daripada satu commit besar di akhir; hindari menilai jumlah baris |
| **AI Usage Log per orang** | Siapa memakai AI untuk apa, dan bagaimana memverifikasinya | Log kosong pada anggota yang jelas memakai AI = masalah integritas, bukan sekadar administrasi |
| **Peran bergilir** | Data owner / experiment owner / reproducibility owner dicatat di README per milestone | Setiap anggota harus pernah memegang reproducibility owner |
| **Defense / presentasi** | Pertanyaan diarahkan ke anggota yang dipilih penguji, bukan presenter tetap | Ketidakmampuan menjelaskan bagian yang diklaim dikerjakan = penyesuaian nilai individu |
| **Peer review yang ditulis** | Kualitas review untuk tim lain ([TPL-12](../../research-os/08-templates/12-peer-review-template.md)) | Komponen Execution individual |
| **Peer assessment ringan** | Formulir singkat kontribusi anggota (opsional) | Sebagai pelengkap, bukan penentu utama |

Rumus yang disarankan: nilai tim (artefak, rubrik §3/5E) × faktor kontribusi individu (0,8–1,1) berdasarkan bukti di atas, dengan Integrity gate individual.

## 6. Kalibrasi antar dosen

Agar level 3 di satu kelas sama dengan level 3 di kelas lain:

1. **Sesi kalibrasi awal semester (60 menit)**: dosen pipeline menilai bersama 2–3 artefak contoh (dari `metopen-research-studio/examples/` atau semester sebelumnya) dengan rubrik §3, membandingkan skor, dan menyepakati *anchor* per level.
2. **Anchor tertulis**: satu contoh nyata per level per kriteria disimpan di folder MK (`rubric.md` atau `templates/`) setelah artefak riil ada.
3. **Double-marking sampel**: 10% artefak milestone akhir dinilai dua dosen; selisih > 1 level dibahas.
4. **Review gate lintas dosen**: reviewer PR gate di Metopen/TA berasal dari dosen lain/klaster lain (red team W8), sehingga standar tidak bergantung pada satu orang.
5. **Refleksi akhir semester**: distribusi level per kriteria per MK dilaporkan ke koordinator komponen; kriteria yang hampir semua tim mendapat level 4 atau level 1 ditinjau ulang deskriptornya.

## 7. Bukti untuk OBE dan akreditasi

Setiap artefak yang dinilai adalah **evidence** dalam rantai [ARC-05](../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md): CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence. Pemetaan ke pelaporan institusional (PP-PTS, akreditasi) ada di [GOV-05](../../research-os/07-governance/05-ppts-and-institutional-evidence.md): *Activity → RPS → Project → Evidence → KPI → dokumentasi*.

Yang perlu disimpan koordinator komponen tiap semester (tanpa menyalin pekerjaan mahasiswa yang INTERNAL):

- Daftar artefak per MK dengan tautan repo/registry/Issue dan level rubrik (tabel §8 sebagai format).
- Jumlah dataset card terdaftar, Issue backlog dari kelas, Experiment Card, handoff, PR gate merged — ini leading indicator [GOV-03](../../research-os/07-governance/03-kpi-and-measurement.md).
- Rekap Integrity gate (jumlah pemeriksaan, jumlah temuan, tindak lanjut).
- Notulen kalibrasi (§6).

## 8. Pemetaan artefak → CPMK → bukti

Tabel ini menghubungkan artefak setiap MK ke CPMK riset (nomor mengacu `courses/<mk>/README.md` §4 atau §7) dan bukti yang dapat diaudit.

| MK | Artefak | CPMK riset | Kriteria rubrik / 5E | Bukti yang diaudit | Lokasi bukti |
|---|---|---|---|---|---|
| AI/ML | Dataset card v0 | R2 | Metrik & evaluasi (data plan) | Keputusan pengelola registry | `datasets-registry/` |
| AI/ML | Experiment Card + baseline experiment | R1 | Baseline; Metrik | Tanggal commit card < tanggal hasil; tabel baseline | repo tim `docs/`, `results/` |
| AI/ML | Repo reproducible + peer reproduction | R3 | Reproducibility | Catatan reproduksi peer | `experiments/README.md` |
| AI/ML | Error analysis + One-Pager v0 + AI Usage Log | R4 | AI disclosure; Explanation | Analisis, one-pager, `AI-USAGE.md` | repo tim; Issue backlog |
| Data Mining | Dataset card + evidence map dataset | R1, R2 | Metrik & evaluasi (leakage) | Kartu diverifikasi; ≥ 2 risiko leakage + mitigasi | `datasets-registry/`; `docs/dataset-evidence-map.md` |
| Data Mining | Baseline + pembanding; error analysis | R3, R4 | Baseline; Reproducibility; AI disclosure | Peer reproduction; `results/analysis.md` | repo tim |
| NLP | Annotation guideline + agreement | R1 | Metrik & evaluasi (construct) | Nilai agreement + adjudication log | `docs/annotation-guideline.md`, `docs/agreement.md` |
| NLP | Korpus + dataset card; benchmark | R2, R3 | Reproducibility; Baseline | `DS-` terdaftar; skrip evaluasi tetap; peer reproduction | `datasets-registry/`; `results/benchmark.md` |
| NLP | Error analysis linguistik + AI Usage Log (pra-anotasi) | R4 | AI disclosure | Tingkat koreksi manusia atas label AI | `AI-USAGE.md` |
| RPL / Pengujian PL / Proyek PL | Requirement brief; research-grade software + artifact README | R1, R2 | Baseline (alternatif); Reproducibility | Issue backlog dirujuk; peer run tanpa bertanya | repo tim; `research-backlog/` |
| RPL / Pengujian PL / Proyek PL | Testing evidence; evaluasi pengguna; AI Usage Statement | R3, R4 | Metrik & evaluasi; AI disclosure | `docs/testing-evidence.md`; `docs/user-evaluation.md` + consent | repo tim |
| Metopen | Problem Brief, Evidence Map, RQ, Contribution | M1 | End; Evidence | PR G2–G4 merged; `UIAI-` diberikan | repo `proj-*`; Mission Control |
| Metopen | Design Card, Data Plan, Baseline & Metrics, Threats, Ethics; Design Defense | M2 | Experiment | PR G5 merged; notulen red team | repo; release v0.3 |
| Metopen | Pilot + reproducibility; analysis + CER | M3 | Experiment; Explanation | PR G6–G7 merged; catatan reproduksi | repo; release v0.5 |
| Metopen | Proposal TA, defense, Integrity Checklist, AI Usage Statement, handoff | M4 | Explanation; Execution; Integrity gate | PR G8 merged; release v1.0; checklist ditandatangani | repo; Mission Control (Maturity) |
| TA | Eksperimen penuh + package | T1 | Experiment; Reproducibility | PR G6 merged; reproduksi pembimbing/peer | repo |
| TA | Analysis + CER + threats final | T2 | Explanation | PR G7 merged | `results/analysis.md` |
| TA | Laporan TA + manuscript/dataset/artefak | T3 | Contribution (ARC-06) | Sidang lulus; `PUB-`/`DS-`/`ART-` terdaftar | Prodi; `publications/`; `datasets-registry/` |
| TA | Sidang sebagai defense; Integrity Checklist; handoff ke AI Center | T4 | Execution; Integrity gate | Notulen sidang; checklist; `docs/handoff.md` | repo; Mission Control |

Tabel ini diperbarui bersama `research-artifact.md` tiap MK. Bila sebuah artefak tidak punya baris di sini, ia belum menjadi bukti OBE — tambahkan atau hapus artefaknya.
