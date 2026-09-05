# Week 04 — Evidence

> **Sprint** S4 · **Gate** G3 Evidence Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-03-search.md) / [Week berikutnya →](week-05-gap.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Kami sudah membaca ___ sumber primer secara penuh; setiap baris synthesis matrix kami dapat ditunjukkan halaman, tabel, atau figurnya di paper asli."** Sumber primer 15–25 buah benar-benar dibaca — bukan abstraknya, bukan ringkasan AI-nya — dan diekstrak ke `docs/literature/synthesis-matrix.csv` dengan kolom `verified` dan `quality`; metrik, baseline, dan dataset yang lazim di literatur dicatat agar desain riset di W7 sebanding dengan literatur; `references.bib` diverifikasi ulang oleh dua anggota berbeda. Ini minggu kedua dari tiga minggu G3 Evidence Ready (W3 Search → W4 Evidence → W5 Gap): PR gate baru dibuka di W5, tetapi pola yang akan dicari di W5 hanya bisa muncul bila matriks minggu ini diisi dari bacaan nyata ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3). Ini **sprint terberat pertama** semester (22 jam tim) — bagi bacaan sejak Senin ([OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S4).

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (membaca paper computing secara strategis, klaim vs bukti, kolom synthesis matrix, critical appraisal), **60 menit studio** (membaca satu paper bersama dan mengisi baris matriks contoh, menyepakati kolom matriks tim, membagi sumber antar anggota), **10 menit gate check** (dosen memilih satu baris matriks contoh dan meminta mahasiswa menunjukkan halaman/tabel yang mendukungnya). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md); sprint goal dari [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S4.

## Concept (30 menit)

1. **Membaca paper computing secara strategis**, bukan dari halaman satu: abstract → figures/tables → method → limitations → introduction terakhir. Tabel dan figur menunjukkan apa yang *benar-benar diukur*; introduction adalah argumen penjualan penulis. Urutan ini membuat 15–25 paper terbaca dalam satu minggu tanpa menjadi ringkasan abstrak ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W4).
2. **Klaim ≠ bukti.** Setiap paper mengklaim sesuatu; tugas tim adalah menemukan tabel/figur yang menopangnya. Kolom *hasil utama* di matriks diisi angka + kondisi (dataset, split, baseline pembanding, metrik), bukan kata sifat penulis ("signifikan", "state-of-the-art").
3. **Matriks lebih kuat daripada ringkasan satu per satu.** Baris = sumber, kolom = dimensi yang sama untuk semua sumber; pola (konsisten / bertentangan / belum diuji) hanya terlihat bila semua baris diukur dengan kolom yang sama. Paragraf "Penulis A (2023) meneliti ..." tidak pernah memperlihatkan pola ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.3).
4. **Kolom matriks disepakati sebelum membaca**: sumber, tahun, problem, metode, data, metrik, hasil utama, keterbatasan, relevansi, catatan verifikasi (halaman/tabel) — ditambah kolom `verified`, `quality`, dan kolom khusus masalah tim (misalnya konteks Indonesia, ukuran data). Skala relevansi dan kualitas didefinisikan tertulis; setelah disepakati, kolom tidak diubah diam-diam di tengah minggu.
5. **Critical appraisal** untuk setiap sumber: apakah ada baseline, apakah data representatif dan berapa ukurannya, apakah kode/data tersedia, apakah hasilnya pernah direproduksi orang lain, apakah klaim melebihi datanya. Ini *evidence literacy* ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §8) — standar yang sama akan Anda pakai untuk menilai hasil pilot sendiri di W11–W12.
6. **Kualitas sumber dinilai, bukan dihitung dari sitasi.** Venue, peer review, tahun, dan jumlah sitasi masing-masing hanya satu sinyal; paper bisa banyak dikutip karena dibantah. Sumber non-peer-reviewed (preprint, laporan) boleh ada di matriks tetapi perannya dibatasi sebagai bukti pendukung, dan itu ditulis di kolom `quality` (OPS-040; [MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2).
7. **Metrik, baseline, dan dataset yang lazim** diekstrak sekarang, bukan di W7: agar baseline dan metrik yang tim kunci nanti sebanding dengan literatur, dan agar perbandingan di W11 *apple-to-apple* (dataset dan protokol yang sama), bukan angka yang dicomot dari abstrak.
8. **Cakupan yang bolong ditutup dengan pencarian pelengkap** yang dicatat di `search-log.csv` — bukan strategi baru. Setelah 8–12 sumber pertama biasanya terlihat tema yang minim sumber (konteks Indonesia, sumber terbaru, dataset tertentu); itulah yang dicari di OPS-038.
9. **Membaca adalah tindakan manusia.** AI boleh menjelaskan istilah dan membantu menemukan bagian metode/hasil dalam PDF yang lisensinya mengizinkan; baris matriks ditulis dari bacaan sendiri dengan nomor halaman. Anggota lain memeriksa acak 2 baris terhadap PDF — inilah *spot-check* yang juga akan dilakukan reviewer G3 ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membaca catatan: *"Untuk baris mana pun di matriks kami, dapatkah saya menunjukkan halaman, tabel, atau figur yang mendukungnya — dan dapatkah saya membedakan apa yang penulis klaim dari apa yang datanya tunjukkan?"*

## Tasks

Semua task Sprint S4 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add synthesis matrix rows 1-10 (OPS-035)`. Task yang belum selesai dari W3 (terutama OPS-030 verifikasi `references.bib`) ditulis di atas tabel ini pada salinan tim — OPS-035 tidak boleh dimulai sebelum OPS-030 selesai.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-033 | Ikuti sesi membaca kritis dan synthesis matrix | Baris matriks latihan | 2h | Menjelaskan istilah teknis dalam paper; tidak meringkas paper menggantikan bacaan | Mahasiswa mengisi baris matriks dari bacaannya sendiri |
| OPS-034 | Rancang kolom synthesis matrix | docs/literature/synthesis-matrix.csv (kosong berstruktur) | 1h | - | Dosen memeriksa kolom cukup untuk menemukan pola |
| OPS-035 | Baca dan ekstrak 8-12 sumber prioritas ke matriks | Matriks terisi 8-12 baris | 6h | Membantu menemukan bagian metode/hasil dalam PDF; ekstraksi akhir ditulis manusia | Anggota lain memeriksa acak 2 baris terhadap paper aslinya |
| OPS-036 | Baca dan ekstrak 8-12 sumber berikutnya ke matriks | Matriks terisi 15-25 baris | 6h | Membantu menemukan bagian metode/hasil dalam PDF; ekstraksi akhir ditulis manusia | Anggota lain memeriksa acak 2 baris terhadap paper aslinya |
| OPS-037 | Catat metrik, baseline, dan dataset yang lazim di literatur | docs/literature/common-metrics-baselines.md | 1.5h | Membantu mengelompokkan metrik; tim memverifikasi ke matriks | Tim memastikan tiap entri merujuk sumber yang dibaca |
| OPS-038 | Jalankan pencarian pelengkap untuk sumber yang belum tercakup | Sumber pelengkap terverifikasi | 2h | Mengusulkan query pelengkap; tim menjalankannya | Tiap sumber baru dibuka manual dan diverifikasi |
| OPS-039 | Verifikasi ulang seluruh entri references.bib | references.bib bersih | 1.5h | - | Dua anggota berbeda memeriksa silang; satu entri tidak valid = gate gagal |
| OPS-040 | Nilai kualitas tiap sumber (venue, peer review, tahun, sitasi) | Kolom quality di synthesis matrix | 1.5h | Membantu menelusuri indeksasi venue; penilaian akhir oleh tim | Dosen memeriksa sampel penilaian kualitas |
| OPS-041 | Perbarui AI Usage Log dan jurnal mingguan W4 | AI Usage Log W4 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 22h** (jam tim; untuk tim 2 orang bagi dua). Ini jam terbesar kedua di semester dengan jalur kritis 15,5 jam dan slack 6,5 jam ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer); yang membuatnya bisa selesai bukan lembur Jumat, melainkan **membagi 15–25 sumber per anggota pada hari Senin**.

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-033** di sesi studio (hanya bergantung pada sesi W3) → **OPS-034** sepakati kolom pada hari yang sama → **OPS-035** 8–12 sumber prioritas (butuh `references.bib` W3, OPS-030) — dibagi per anggota, ini titik paralel terbesar → setelah 035: **OPS-036** sisa sumber dan **OPS-037** metrik/baseline/dataset berjalan paralel (orang ketiga bisa mengambil 037) → **OPS-038** pencarian pelengkap (butuh 036) → **OPS-039** verifikasi ulang `.bib` (butuh 037 dan 038, dikerjakan dua orang berbeda); **OPS-040** kolom `quality` dapat dikerjakan siapa pun begitu 036 selesai; **OPS-041** berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g3-evidence` (dipakai sejak W3 sampai PR G3 di W5), harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Baris matriks latihan dari paper yang dibaca bersama di studio + jurnal W4: **pola apa yang mulai terlihat** (konsisten/bertentangan) dan sumber mana yang ternyata tidak relevan | `docs/journal/w04.md` | commit di `research/g3-evidence` | OPS-033, OPS-041 |
| **Synthesis matrix** v1: header disepakati (sumber, tahun, problem, metode, data, metrik, hasil utama, keterbatasan, relevansi, catatan verifikasi/halaman, `verified`, `quality`, kolom khusus masalah tim); **15–25 baris** sumber primer yang dibaca penuh; setiap baris `verified=yes`; skala relevansi/kualitas didefinisikan di baris komentar atau `docs/literature/README.md` | `docs/literature/synthesis-matrix.csv` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) | commit header (OPS-034) lalu commit bertahap per 3–5 baris | OPS-034, OPS-035, OPS-036, OPS-040 |
| **Common metrics, baselines & datasets**: tabel metrik (frekuensi pemakaian di matriks), baseline umum, dataset publik + lisensi + ukuran; tanda ✓ pada yang mungkin dipakai tim; setiap entri merujuk nomor baris matriks | `docs/literature/common-metrics-baselines.md` | commit | OPS-037 |
| Pencarian pelengkap: baris baru di log (query, basis data, tanggal, jumlah hasil, `sumber=pelengkap`), kandidat baru di screening dengan alasan, entri `.bib` baru hanya setelah DOI/URL dibuka, baris matriks baru bila dibaca | `docs/literature/search-log.csv`, `docs/literature/screening.csv`, `references.bib` | commit | OPS-038 |
| **`references.bib` bersih** + **tabel verifikasi**: satu baris per entri `.bib` — DOI/URL dibuka (ya/tidak), judul-penulis-tahun cocok, versi terbit vs preprint, asal (keyword/chaining/AI/pelengkap), pemeriksa 1, pemeriksa 2, keputusan; jumlah entri valid = jumlah baris matriks + kandidat W3 yang sengaja belum dibaca (ditandai) | `references.bib` (root repositori riset), `docs/literature/verification.md` | commit | OPS-039 |
| AI Usage Log W4 dengan Stage `Read`/`Synthesis`: penjelasan istilah, pra-baca PDF (tool, lisensi PDF dicek), pengelompokan metrik, query pelengkap, penelusuran indeksasi venue — dan apa yang ditolak | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-041 |

README riset diperbarui: `Current Research Gate: G3 (in progress — W4 Evidence)`. Tidak ada PR gate dan tidak ada release minggu ini; matriks dan tabel verifikasi menjadi bagian *Literature Evidence Map — ringkasan angka* dan *Synthesis matrix* pada PR `GATE REVIEW: Evidence Ready` di W5 ([evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md)).

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan**, Stage `Read` atau `Synthesis`. Minggu ini AI paling berguna sebagai **pra-baca dan kamus**, bukan sebagai pembaca; reviewer G3 akan mencocokkan baris matriks dengan paper, bukan dengan ringkasan AI.

**Boleh minggu ini**

- Meminta AI menjelaskan istilah, teknik, atau desain studi yang belum dikenal saat membaca (OPS-033, OPS-035, OPS-036) — lalu kembali ke paper untuk melihat bagaimana istilah itu dipakai di sana.
- Memakai tool *source-grounded synthesis* ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.6) untuk menemukan bagian metode/hasil/keterbatasan dalam PDF **yang lisensinya mengizinkan unggah**, sebagai pra-baca; ekstraksi akhir ke matriks ditulis manusia dengan nomor halaman (OPS-035, OPS-036).
- Meminta AI membantu mengelompokkan metrik ke keluarga (klasifikasi, ranking, regresi, kualitas teks, dsb.) dan menyarankan kolom tabel (OPS-037); setiap entri diverifikasi ke baris matriks dan sumber yang dibaca.
- Meminta AI mengusulkan query pelengkap untuk tema yang minim sumber (OPS-038); tim yang menjalankannya di basis data nyata dan mencatatnya di `search-log.csv`.
- Meminta AI membantu menelusuri indeksasi venue (Scopus/SINTA/CORE/DBLP) sebagai titik awal (OPS-040); penilaian `quality` diputuskan tim setelah membuka halaman venue.
- Setelah baris matriks ditulis sendiri, meminta AI menantang: "keterbatasan apa yang tidak disebut penulis? apakah baseline-nya adil?" — sebagai latihan critical appraisal, dicatat sebagai *Challenge* di log.

**Tidak boleh**

- Mengisi baris matriks dari output AI tanpa membuka bagian paper yang dirujuk; ringkasan AI **bukan** membaca, dan baris yang tidak cocok dengan paper saat spot-check menurunkan E2 ke *Developing* ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2).
- Mengunggah PDF berlisensi terbatas (publisher) ke layanan AI pihak ketiga ([LICENSING.md](../../LICENSING.md), [AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.6, §4); pakai versi open access/author's copy, atau baca tanpa AI.
- Menerima "penilaian kualitas venue" atau angka sitasi dari AI tanpa membuka halaman venue/indeks — AI tidak tahu reputasi venue secara andal ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §8).
- Membiarkan AI menambahkan sumber ke matriks atau `references.bib`; sumber baru hanya masuk lewat OPS-038 dengan DOI/URL dibuka manual — satu entri tidak valid = G3 gagal ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-034 (merancang kolom — keputusan tim tentang apa yang penting untuk masalahnya), OPS-039 (verifikasi ulang `.bib`), OPS-041 (log & jurnal).

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Baris matriks latihan diisi dari bacaan sendiri atas paper yang dibaca bersama; mahasiswa dapat menunjuk halaman/tabel yang mendukung tiap sel | diri sendiri, diuji dosen di 10 menit gate check | OPS-033 |
| Kolom matriks cukup untuk menemukan pola di W5 (minimal problem, metode, data, metrik, hasil, keterbatasan, relevansi + `verified`, `quality`, halaman) dan skala relevansi/kualitas terdefinisi | dosen pengampu (saat studio, sebelum baris pertama diisi) | OPS-034 |
| Anggota lain memilih acak 2 baris per pembaca dan mencocokkannya dengan paper asli: hasil utama, data, dan keterbatasan sesuai; halaman tercantum; ketidakcocokan dicatat dan baris diperbaiki | tim (cross-check silang antar pembaca); mentor bila sudah ada | OPS-035, OPS-036 |
| Setiap entri metrik/baseline/dataset merujuk nomor baris matriks dan sumber yang benar-benar dibaca; lisensi dataset publik tercatat | tim | OPS-037 |
| Tiap sumber pelengkap dibuka manual: DOI/URL benar, judul-penulis-tahun cocok, lolos kriteria inklusi W3; tercatat di log dan screening | tim (anggota yang tidak mengusulkan query) | OPS-038 |
| **Seluruh** `references.bib` diperiksa silang oleh **dua anggota berbeda**: DOI valid, penulis/tahun cocok, tidak ada entri halusinasi; sumber asal AI ditandai dan hasil pemeriksaannya ada di AI Usage Log; satu entri tidak valid = G3 gagal | tim (dua pemeriksa); dosen membuka 3 entri acak | OPS-039 |
| Sampel penilaian `quality`: alasan masuk akal (venue, peer review, tahun, sitasi), sumber non-peer-reviewed ditandai sebagai pendukung | dosen pengampu | OPS-040 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya, khususnya pra-baca PDF (tool, lisensi) dan apa yang ditolak | diri sendiri | OPS-041 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W4, "dapat dibuka reviewer" berarti reviewer memilih baris acak di matriks, membuka PDF-nya, dan menemukan halaman/tabel yang disebut baris itu.

## Done When

Minggu ini **belum menutup gate** — G3 Evidence Ready berlangsung W3–W5 dan PR-nya dibuka di W5. Jawab ya/tidak per butir pada Jumat:

- [ ] Deliverable W3 lengkap sebelum ekstraksi dimulai: `search-strategy.md`, `search-log.csv`, `screening.csv`, dan `references.bib` terverifikasi (OPS-030) — blocking rule B2 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules).
- [ ] `docs/journal/w04.md` berisi baris matriks latihan dari sesi studio dan refleksi "pola apa yang mulai terlihat".
- [ ] `docs/literature/synthesis-matrix.csv` memiliki header yang disepakati dan diperiksa dosen (OPS-034) sebelum baris pertama diisi; skala relevansi dan kualitas terdefinisi.
- [ ] Matriks berisi **minimal 15 baris** (target 15–25) sumber primer yang dibaca penuh; setiap baris `verified=yes`, kolom hasil utama berisi angka + kondisi, kolom catatan verifikasi menyebut halaman/tabel; sumber yang ternyata tidak relevan dicatat beserta alasannya.
- [ ] Cross-check selesai: anggota lain memeriksa acak 2 baris per pembaca terhadap PDF; ketidakcocokan diperbaiki dan dicatat di jurnal.
- [ ] `docs/literature/common-metrics-baselines.md` berisi tabel metrik (frekuensi), baseline umum, dataset publik + lisensi; setiap entri merujuk baris matriks.
- [ ] Pencarian pelengkap tercatat di `search-log.csv`; sumber baru masuk `screening.csv` dan `references.bib` hanya setelah DOI/URL dibuka.
- [ ] `docs/literature/verification.md` memuat satu baris per entri `.bib` dengan dua pemeriksa berbeda; **0 entri tidak valid**; entri asal AI ditandai dan hasil pemeriksaannya ada di AI Usage Log.
- [ ] Kolom `quality` terisi untuk **semua** baris dengan alasan; sumber non-peer-reviewed ditandai sebagai bukti pendukung; dosen sudah memeriksa sampel.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Read`/`Synthesis` untuk setiap penggunaan material minggu ini; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] Di gate check, dosen memilih satu baris matriks dan mahasiswa menunjukkan halaman/tabel pendukungnya tanpa membuka catatan lain.
- [ ] README riset: `Current Research Gate: G3 (in progress — W4 Evidence)`.

**Progres menuju G3** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3). Dari empat butir definition of done G3, W3 menuntaskan *strategi pencarian terdokumentasi*; minggu ini menuntaskan *Literature Evidence Map: 15–25 sumber primer yang benar-benar dibaca dalam synthesis matrix* dan mengunci *setiap sumber terverifikasi* serta *`references.bib` terkelola* lewat verifikasi ulang dua orang; W5 menambahkan narasi pola (konsisten/bertentangan/belum diuji) di `docs/literature-map.md` dan kandidat gap, lalu tim membuka PR **`GATE REVIEW: Evidence Ready`** dari `research/g3-evidence` memakai [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3; task OPS-047). Kriteria lulusnya: *matriks menunjukkan pola*; kriteria gagalnya: *satu saja referensi yang tidak dapat diverifikasi keberadaannya* — keduanya ditentukan oleh kualitas baris yang Anda tulis minggu ini. Bila `references.bib` W3 belum tuntas pada Senin, selesaikan OPS-030 lebih dulu dan pakai slack 6,5 jam S4 dengan membagi bacaan ke tiga orang ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — `docs/AI-USAGE.md` (Stage `Read`/`Synthesis`).
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `references.bib`, `docs/literature/` (synthesis matrix, verification), `docs/literature-map.md`, branch `research/g3-evidence`.
- [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) — butir integritas sitasi ("dibaca oleh siapa, bagian mana") yang ditandatangani di W15; kolom catatan verifikasi matriks adalah buktinya.
- [TPL-05 Dataset Registry Template](../../research-os/08-templates/05-dataset-registry-template.md) — field lisensi/akses/ukuran yang perlu dicatat untuk dataset publik yang ditemukan di literatur (OPS-037), dipakai saat mendaftarkan dataset di W7.
- Template PR [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) (dipakai W5; bagian *Literature Evidence Map — ringkasan angka* dan *Synthesis matrix* bisa diisi dari minggu ini) dan form Issue [Literature Gap](../../.github/ISSUE_TEMPLATE/05-literature-gap.yml) (dugaan gap W3 diperbarui bila matriks mulai membantahnya).

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W4 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.3 Literature Evidence Map, §4 struktur repositori · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2 E2 Evidence · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4 citation integrity, §2.8 AI usage.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §8 evidence literacy (latihan *Piramida Bukti Lokal*) · [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.3 Read, §3.4 Synthesis · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 izin/larangan · [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.6 source-grounded synthesis, §4 kebijakan data.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S4 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G3 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rule B2, §S4 · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) · [LICENSING.md](../../LICENSING.md) · [SECURITY.md](../../SECURITY.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Ringkasan AI dianggap membaca.** Baris matriks rapi, tetapi tidak ada nomor halaman, dan saat dosen membuka PDF, angkanya tidak ada di tabel mana pun — E2 langsung *Developing* dan kepercayaan reviewer hilang untuk baris lainnya. Cara menghindari: kolom catatan verifikasi (halaman/tabel) wajib untuk setiap baris; AI hanya untuk istilah dan menemukan bagian; cross-check 2 baris per pembaca oleh anggota lain sebelum Jumat.
2. **Matriks berubah menjadi ringkasan per paper.** Kolom *hasil utama* berisi "metode yang diusulkan mengungguli baseline" — kalimat abstrak, bukan bukti — sehingga di W5 tidak ada pola yang bisa dibandingkan. Cara menghindari: hasil utama = metrik + angka + dataset + baseline pembanding; keterbatasan diisi dari bagian *limitations* **dan** pengamatan Anda sendiri (baseline lemah? data kecil? tidak direproduksi?).
3. **Kolom tidak disepakati, atau tiap anggota mengisi dengan gaya sendiri.** Satu orang menulis "relevan", yang lain "3", yang lain kosong; skala kualitas berbeda-beda; kolom ditambah di tengah minggu tanpa mengisi ulang baris lama. Cara menghindari: OPS-034 selesai Senin dan diperiksa dosen; definisi skala tertulis; satu pemilik file matriks yang menggabungkan kontribusi anggota.
4. **Bacaan dikerjakan serial oleh satu orang, atau ditumpuk ke Kamis.** Dua belas jam ekstraksi (OPS-035 + OPS-036) tidak muat di satu malam; hasilnya baris dangkal dari abstrak. Cara menghindari: bagi sumber per anggota Senin, jadwalkan dua sesi baca tetap, dan adakan sinkronisasi 15 menit di tengah minggu untuk menandai pertentangan awal ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §S4).
5. **Metadata dan kualitas dipercaya begitu saja.** `.bib` dari reference manager memuat tahun preprint alih-alih versi terbit; paper "paling banyak dikutip" otomatis dianggap terbaik; angka hasil disalin tanpa dataset dan protokolnya sehingga W11 membandingkan apel dengan jeruk. Cara menghindari: OPS-039 dua pemeriksa berbeda mencocokkan tiap entri ke halaman DOI; `quality` dinilai dari venue, peer review, tahun — sitasi hanya satu sinyal; OPS-037 selalu mencatat metrik bersama dataset dan protokol evaluasinya.
