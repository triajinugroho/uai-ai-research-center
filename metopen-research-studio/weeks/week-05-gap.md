# Week 05 — Gap

> **Sprint** S5 · **Gate** G3 Evidence Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-04-evidence.md) / [Week berikutnya →](week-06-rq.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan kalimat G3 dari [OPS-03](../../research-os/06-execution-os/03-research-gates.md): **"Literatur sudah menunjukkan ___, tetapi bertentangan/kosong pada ___."** Synthesis matrix 15–25 sumber dari W4 dianalisis lintas baris menjadi tiga jenis pola — konsisten, bertentangan, belum diuji — lalu dituangkan sebagai Literature Evidence Map di `docs/literature-map.md`; dari pola itu diturunkan 2–3 kandidat research gap yang masing-masing menunjuk baris matriks, diuji kelayakannya untuk satu semester + TA, dan dipilih satu gap utama plus satu cadangan. Ini minggu penutup G3 Evidence Ready (W3 Search → W4 Evidence → W5 Gap): tim membuka PR `GATE REVIEW: Evidence Ready`, dan merge berarti release `v0.2 Evidence Ready` ([OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S5; [MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W5).

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (dari matriks ke pola, jenis gap, Gap–Claim–Evidence alignment, mengapa "belum ada di UAI" bukan gap), **60 menit studio** (latihan pola pada matriks contoh, lalu mengelompokkan baris matriks tim sendiri per tema dan menandai kontradiksi; 15 menit terakhir tiap tim memaparkan 3 slide peta bukti dan menerima keberatan peer), **10 menit gate check** (tiap tim membacakan satu pola dan baris matriks yang mendukungnya; dosen menguji satu gap secara acak). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md).

## Concept (30 menit)

1. **Matriks dibaca menurun, bukan mendatar.** Ringkasan per paper (membaca satu baris) selesai di W4; sintesis berarti membaca satu kolom lintas baris: metode apa yang berulang, data apa yang dipakai, metrik apa yang lazim, hasil mana yang searah. Pola adalah pernyataan tentang *kumpulan* baris, dan setiap pola harus menunjuk minimal 2 baris ([OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S5).
2. **Tiga jenis pola.** *Konsisten*: apa yang disepakati literatur (beberapa sumber, hasil searah). *Bertentangan*: hasil berlawanan pada masalah serupa — catat dugaan penyebabnya (data, metrik, konteks, ukuran sampel). *Belum diuji*: konteks, data, metode, atau perbandingan yang kosong di semua baris ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3; template PR [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) bagian *Pola yang terlihat dari matriks*).
3. **Jenis gap.** Empiris (hasil belum ada atau bertentangan), metodologis (metode belum dibandingkan atau cacat), kontekstual (konteks/data berbeda *dengan alasan* mengapa hasil bisa berubah), replikasi (temuan belum direplikasi orang lain), artefak/dataset (alat atau data yang dibutuhkan belum ada). Setiap kandidat gap menyebut jenisnya dan baris matriks pendukungnya ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.4).
4. **"Belum ada yang meneliti di UAI/Indonesia" bukan gap** — kecuali ada alasan konteks yang masuk akal mengapa hasil akan berbeda (bahasa, distribusi data, regulasi, infrastruktur) dan alasan itu sendiri didukung baris matriks. Gap naratif adalah kriteria gagal G4 ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G4) dan level *Developing* pada rubrik E2 ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2).
5. **Gap–Claim–Evidence alignment.** Gap yang layak dapat langsung ditulis sebagai klaim yang kelak ingin dibuktikan, dan klaim itu punya jalur ke bukti: baris matriks yang membuat gap ini perlu → klaim yang mengisi gap → bukti apa yang akan dihasilkan. Alignment ini difinalkan di W6 (OPS-051); minggu ini cukup dalam bentuk kandidat.
6. **Gap yang layak ≠ gap yang menarik.** Uji kelayakan: akses data, kompleksitas metode, waktu (sisa semester + TA), kompetensi tim, risiko. Gap yang tidak layak tidak dibuang, tetapi **diparkir** sebagai Issue backlog agar tim lain atau TA berikutnya bisa mengambilnya ([research-backlog](../../research-backlog/README.md)).
7. **Evidence map digambar, bukan hanya ditulis.** Tabel tema × sumber (atau diagram) memperlihatkan di mana sumber menumpuk dan di mana kosong — sel kosong sering adalah kandidat gap; sel penuh dengan hasil berlawanan adalah kontradiksi ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W5).
8. **AI menantang gap, tidak menyatakan gap.** "Apakah ini sudah dijawab di sub-bidang lain?" adalah pertanyaan bagus untuk AI; "belum ada penelitian tentang X" adalah klaim yang AI tidak bisa buktikan. Setiap tantangan AI dijawab dengan pencarian ulang yang tercatat di search log, bukan dengan percaya ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.5).
9. **Kriteria G3 tetap berlaku sampai merge.** Sumber baru yang muncul minggu ini (dari pencarian ulang) melewati jalur yang sama: dibuka DOI/URL-nya, dibaca, masuk matriks dan `references.bib`. Satu referensi tidak terverifikasi = G3 gagal, terlepas dari kualitas pola ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membaca catatan: *"Baris matriks mana yang membuat gap kami ada — dan apa yang harus kami temukan di literatur agar gap itu ternyata tidak ada?"*

## Tasks

Semua task Sprint S5 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add literature map patterns (OPS-043)`. Task W4 yang belum selesai (terutama OPS-039 verifikasi ulang `references.bib` dan OPS-040 kolom `quality`) ditulis di atas tabel ini pada salinan tim — keduanya prasyarat PR G3.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-042 | Ikuti sesi From Literature to Gap | Latihan pola matriks | 2h | Menguji dengan matriks contoh lain | Mahasiswa menjelaskan perbedaan gap naratif vs defensible |
| OPS-043 | Analisis pola matriks: konsisten, bertentangan, belum diuji | Bagian Patterns di docs/literature-map.md | 3h | Membantu mengelompokkan baris dan mengusulkan pola; tim memverifikasi setiap pola ke baris matriks | Dosen memeriksa pola bersumber dari matriks, bukan dari AI |
| OPS-044 | Tulis Literature Evidence Map (docs/literature-map.md) | docs/literature-map.md | 3h | Mengkritik alur argumen dan mendeteksi klaim tanpa sitasi | Tim memastikan tiap kalimat klaim literatur bersitasi terverifikasi |
| OPS-045 | Rumuskan kandidat research gap (2-3) dari pola | Kandidat gap dalam docs/literature-map.md bagian Gap Candidates | 2h | Menantang apakah gap benar-benar belum dijawab literatur; tim memeriksa ulang ke matriks | Dosen menguji satu gap secara acak terhadap matriks |
| OPS-046 | Uji kandidat gap terhadap kelayakan semester + TA | Tabel kelayakan gap | 1.5h | Membantu memperkirakan kompleksitas; keputusan oleh tim | Dosen menilai gap terpilih realistis |
| OPS-047 | Siapkan PR GATE REVIEW: Evidence Ready (evidence-review.md) | PR GATE REVIEW: Evidence Ready | 1.5h | - | Reviewer memeriksa matriks menunjukkan pola dan semua referensi terverifikasi |
| OPS-048 | Presentasikan Literature Evidence Map di studio dan catat umpan balik | Catatan umpan balik studio | 1.5h | Membantu meringkas menjadi 3 slide; isi dari dokumen tim | Dosen memeriksa keberatan utama tercatat |
| OPS-049 | Perbarui AI Usage Log dan jurnal mingguan W5 | AI Usage Log W5 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 15h** (jam tim; untuk tim 2 orang bagi dua). Beban sedang: 11 jam berada pada critical path dengan slack 4 jam ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer) — sprint ini menutup rantai literatur S3–S5, rantai kritis terpanjang pertama di semester.

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-042** di sesi studio dan **OPS-043** langsung setelahnya (matriks OPS-036 dan `references.bib` OPS-039 sudah lengkap dari W4) → **OPS-044** literature map → **OPS-045** kandidat gap (butuh Issue literature-gap OPS-031 dari W3) → **OPS-046** tabel kelayakan → lalu bercabang ke dua anggota berbeda: **OPS-047** PR G3 (butuh juga OPS-026, OPS-039, OPS-040 dari minggu sebelumnya) dan **OPS-048** paparan studio; **OPS-049** berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g3-evidence`, harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Latihan pola pada matriks contoh (tiga jenis pola, masing-masing dengan baris pendukung) + jurnal W5: gap mana yang paling meyakinkan dan mengapa | `docs/journal/w05.md` | commit | OPS-042, OPS-049 |
| **Literature Evidence Map** 2–3 halaman: §Themes (peta tema, tabel tema × sumber atau diagram), §Patterns (konsisten / bertentangan / belum diuji, tiap pola menunjuk ≥2 ID baris matriks), tabel ringkas, §Limitations of the literature; semua sitasi memakai kunci BibTeX yang ada di `references.bib` | `docs/literature-map.md` | commit | OPS-043, OPS-044 |
| §Gap Candidates: 2–3 kandidat gap, masing-masing dengan jenis gap dan baris matriks pendukung; hasil pencarian ulang setelah tantangan AI dicatat di `docs/literature/search-log.csv` | `docs/literature-map.md` §Gap Candidates (bagian dari bukti G3; Research Gap final baru ditetapkan di `docs/research-question.md` pada W6 dan dinilai di G4) | commit | OPS-045 |
| §Feasibility: tabel kelayakan (data · metode · waktu · risiko · kompetensi) per kandidat; keputusan 1 gap utama + 1 cadangan dengan alasan | `docs/literature-map.md` §Feasibility | commit | OPS-046 |
| Issue `type:literature-gap` diperbarui dari "dugaan" menjadi "kandidat": gap statement, jenis, baris matriks; gap yang diparkir dibuka sebagai Issue backlog (form [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml), label `maturity:idea`) dengan tautan ke literature map | Issue di repo pusat; nomor Issue dicatat di literature map | URL Issue | OPS-045, OPS-046 |
| Catatan umpan balik studio: 3 slide (pola, gap, kelayakan), pertanyaan/keberatan dosen dan peer, tindak lanjut dengan penanggung jawab | `docs/reviews/w05-studio-feedback.md`; slide di `presentation/` | commit | OPS-048 |
| **PR `GATE REVIEW: Evidence Ready — UIAI-YYYY-NNN`** dari `research/g3-evidence` memakai [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md); reviewer dosen + peer (+ mentor bila ada); setelah merge: label `gate:G3-evidence`, release `v0.2 Evidence Ready` | PR dan Release di repositori riset | URL PR, URL release | OPS-047 |
| AI Usage Log W5: entri Stage `Synthesis` dan `Gap` — pengelompokan baris, kritik alur argumen, tantangan gap dan hasil pencarian ulangnya, ringkasan slide | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-049 |

README riset diperbarui: `Current Research Gate: G3 (review — W5 Gap)` saat PR dibuka, lalu `G3 passed → G4 (in progress)` setelah merge. Release `v0.2 Evidence Ready` menandai Research Pack berisi artefak 1–4 ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §7).

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan** dengan Stage `Synthesis` atau `Gap`. Minggu ini AI paling berguna sebagai **penantang** — bukan penemu gap. Reviewer G3 membaca log untuk dua hal: sumber dari AI diverifikasi, dan pola/gap berasal dari matriks tim.

**Boleh minggu ini**

- Berlatih dengan **matriks contoh lain** yang dibuat atau dimodifikasi AI untuk menemukan tiga jenis pola sebelum menyentuh matriks tim sendiri (OPS-042).
- Memberi AI **matriks tim sendiri** (bukan meminta ia mencari) untuk membantu mengelompokkan baris per tema dan mengusulkan pola; setiap pola yang dipakai diverifikasi ke ID baris matriks, dan kontradiksi yang disorot AI dicek di paper (OPS-043; [AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.4).
- Meminta AI mengkritik alur argumen literature map dan menandai kalimat klaim yang tidak bersitasi (OPS-044); perbaikan ditulis tim dengan kunci BibTeX yang ada.
- Meminta AI **menantang** kandidat gap — "apakah ini sudah dijawab di sub-bidang lain?", "sub-area apa yang mungkin terlewat?" — lalu menjawab tantangan itu dengan pencarian ulang tercatat di `search-log.csv` (OPS-045; [MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W5).
- Meminta AI membantu memperkirakan kompleksitas metode/data untuk tabel kelayakan (OPS-046); keputusan gap utama dan cadangan tetap oleh tim.
- Meminta AI meringkas `docs/literature-map.md` menjadi 3 slide (OPS-048); isinya dari dokumen tim, angka dan sitasi dicek ulang sebelum dipaparkan.

**Tidak boleh**

- Menerima klaim AI bahwa **"belum ada penelitian tentang X"** sebagai gap — AI tidak dapat membuktikan ketiadaan; gap hanya sah bila menunjuk baris matriks ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.5).
- Memasukkan pola, tema, atau sumber "baru" dari percakapan AI ke literature map tanpa baris matriks dan tanpa melewati jalur Search → Read → verifikasi DOI/URL; satu referensi tak terverifikasi = G3 gagal ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4).
- Membiarkan AI **memilih** gap utama untuk tim, atau menulis §Gap Candidates yang tim tidak bisa jelaskan baris demi baris di gate check.
- Mengunggah PDF berlisensi terbatas atau data stakeholder dari W2 ke layanan AI ([LICENSING.md](../../LICENSING.md), [SECURITY.md](../../SECURITY.md)).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-047 (PR gate — pertanggungjawaban tim) dan OPS-049 (log & jurnal — rekaman proses manusia).

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa dapat menjelaskan perbedaan gap naratif ("belum ada di UAI") vs gap defensible (menunjuk baris matriks dan jenisnya) dengan kata sendiri | diri sendiri, diuji peer pada 10 menit gate check | OPS-042 |
| Setiap pola di §Patterns bersumber dari matriks, bukan dari AI: menunjuk ≥2 ID baris; kontradiksi yang disebut benar-benar ada di paper yang dirujuk | dosen pengampu (spot-check satu pola); tim | OPS-043 |
| Setiap kalimat klaim literatur di literature map bersitasi dengan kunci BibTeX yang ada di `references.bib` dan terverifikasi; tidak ada sitasi ke sumber di luar matriks | tim (anggota yang tidak menulis bagian itu membaca ulang) | OPS-044 |
| Dosen memilih satu kandidat gap secara acak dan menguji: baris matriks yang dirujuk memang mendukung gap; pencarian ulang setelah tantangan AI tercatat | dosen pengampu | OPS-045 |
| Gap terpilih realistis untuk sisa semester + TA: data dapat diakses, metode dalam jangkauan tim, waktu cukup; gap yang diparkir punya Issue backlog | dosen pengampu; mentor bila sudah ada | OPS-046 |
| Reviewer PR memeriksa matriks menunjukkan pola (bukan ringkasan per paper) dan membuka 3–5 DOI/URL acak dari `references.bib` — semua ada dan cocok dengan baris matriks | dosen pengampu + peer reviewer (+ mentor) | OPS-047 |
| Keberatan utama dari paparan studio tercatat beserta tindak lanjut dan penanggung jawabnya | dosen pengampu | OPS-048 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya: tantangan AI mana yang dijawab pencarian ulang, pola usulan AI mana yang ditolak | diri sendiri | OPS-049 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W5, "dapat dibuka reviewer" berarti reviewer bisa memilih satu pola atau gap, membuka ID baris matriks yang dirujuk, dan menemukan sumber yang benar-benar mengatakan itu.

## Done When

Minggu ini **menutup gate G3 Evidence Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] `docs/journal/w05.md` berisi latihan pola matriks contoh dan refleksi: gap mana yang paling meyakinkan dan mengapa.
- [ ] `docs/literature-map.md` §Patterns memuat pola konsisten / bertentangan / belum diuji; **setiap pola menunjuk minimal 2 baris matriks**.
- [ ] `docs/literature-map.md` lengkap (peta tema, pola, tabel ringkas, batasan literatur); semua sitasi memakai kunci yang ada di `references.bib`.
- [ ] §Gap Candidates berisi 2–3 kandidat gap dengan jenis gap dan baris matriks; setiap tantangan AI dijawab pencarian ulang yang tercatat.
- [ ] §Feasibility memuat tabel kelayakan; **satu gap utama + satu cadangan dipilih**; gap lain diparkir sebagai Issue backlog.
- [ ] Issue `type:literature-gap` diperbarui menjadi "kandidat" dengan rujukan baris matriks.
- [ ] `docs/reviews/w05-studio-feedback.md` berisi keberatan dari paparan studio dan tindak lanjutnya.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Synthesis`/`Gap`; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] PR **`GATE REVIEW: Evidence Ready — UIAI-YYYY-NNN`** dibuka dari branch `research/g3-evidence` memakai [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) dengan semua field terisi (search strategy, ringkasan angka, matriks, pola, kandidat gap, evidence, AI usage) dan reviewer diminta: dosen pengampu + peer reviewer (+ mentor bila ada) ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3).
- [ ] PR termerge; label Issue `gate:G3-evidence`; release `v0.2 Evidence Ready` dibuat; README riset `Current Research Gate` diperbarui.

**Lulus jika / Gagal jika** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3): **lulus** jika matriks menunjukkan pola — apa yang konsisten, apa yang bertentangan, apa yang belum diuji — dan keempat butir definition of done G3 terpenuhi (strategi pencarian terdokumentasi; 15–25 sumber primer benar-benar dibaca dalam synthesis matrix; setiap sumber terverifikasi DOI/URL termasuk yang dari AI; `references.bib` terkelola). **Gagal** jika ada **satu saja** referensi yang tidak dapat diverifikasi keberadaannya — terlepas dari kualitas pola — atau ada pelanggaran integritas lain (sumber dikutip tanpa dibaca, AI tidak diungkap). Gagal gate bukan hukuman: reviewer menulis apa yang kurang, tim memperbaiki hanya itu, lalu membuka review ulang. Bila PR G3 belum merge di Jumat, ikuti skenario "G3 terlambat 1 minggu" di [OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat: pangkas ke 15 sumber berkualitas tinggi, PR G3 di W6, RQ W6 ditulis sebagai draft bersyarat dan **tidak** diajukan sebagai PR G4 sampai G3 merge (blocking rule B3).

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — entri Stage `Synthesis` dan `Gap`; catat pola usulan AI yang ditolak dan pencarian ulang yang dilakukan.
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `docs/literature-map.md`, `docs/reviews/`, `presentation/`, aturan release.
- [TPL-04 Research Backlog Template](../../research-os/08-templates/04-research-backlog-template.md) — format kartu masalah untuk gap yang diparkir (status Idea).
- [TPL-01 Research One-Pager Template](../../research-os/08-templates/01-research-one-pager-template.md) — baca bagian Gap/RQ sekarang; diisi di W6 sebagai One-Pager v1.
- Form Issue [Literature Gap](../../.github/ISSUE_TEMPLATE/05-literature-gap.yml) (OPS-045) dan [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml) (gap yang diparkir, OPS-046); template PR [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) (OPS-047).

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W5 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.3 Literature Evidence Map, §3.4 Research Gap, §7 release v0.2 · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2 E2 Evidence · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4 citation integrity.
- [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.4 Synthesis, §3.5 Gap · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 izin/larangan · [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.6 source-grounded synthesis.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S5 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G3–G4 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rules B2–B3, §Jika satu gate terlambat · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) · [Research Backlog](../../research-backlog/README.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Gap naratif.** "Belum ada yang meneliti X di UAI/Indonesia" terasa seperti temuan, padahal hanya pernyataan tentang lokasi. Cara menghindari: setiap gap wajib menyebut jenis (empiris/metodologis/kontekstual/replikasi/artefak) dan ID baris matriks; untuk gap kontekstual, tulis alasan konkret mengapa konteks mengubah hasil — dan alasan itu pun harus punya baris pendukung.
2. **Gap lahir dari percakapan AI, bukan dari matriks.** AI menyebut "belum ada penelitian tentang X" dan tim menyalinnya. Cara menghindari: pakai AI hanya untuk *menantang*; setiap tantangan dijawab dengan pencarian ulang tercatat di `search-log.csv`; kandidat gap yang tidak bisa ditunjuk barisnya dibuang; semuanya dicatat di AI Usage Log.
3. **Sumber baru menyelinap di tahap sintesis.** Pencarian ulang menemukan paper tambahan, langsung disitasi di literature map tanpa dibaca dan tanpa masuk `references.bib` terverifikasi. Cara menghindari: sumber baru mengikuti jalur W3–W4 (verifikasi DOI/URL → baca → baris matriks → `.bib`) sebelum disitasi; satu referensi tak terverifikasi = G3 gagal.
4. **Literature map berbentuk "Penulis A (2023) meneliti..."** — paragraf per paper, bukan pola. Reviewer menandainya level *Developing* dan PR tidak merge. Cara menghindari: tulis dari kolom, bukan dari baris; setiap paragraf §Patterns dimulai dengan pernyataan pola dan diikuti daftar baris pendukung.
5. **Gap terlalu besar — atau sebenarnya sudah dijawab.** Gap "meningkatkan akurasi semua sistem rekomendasi pendidikan" tidak selesai dalam satu TA; gap yang "belum diuji" kadang hanya belum ditemukan karena kata kunci sempit. Cara menghindari: tabel kelayakan (OPS-046) dengan kolom waktu dan data; pencarian ulang dengan sinonim sebelum gap dinyatakan "belum diuji"; gap besar dipecah dan sisanya diparkir ke backlog.
6. **Menulis RQ sebelum G3 merge.** Tergoda langsung merumuskan RQ karena gap sudah terlihat. Cara menghindari: RQ tidak sah sebelum evidence synthesis lolos review (blocking rule B3, [OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md)); minggu ini berhenti di kandidat gap + kelayakan, dan biarkan reviewer G3 menguji gap sebelum ia menjadi pertanyaan.
