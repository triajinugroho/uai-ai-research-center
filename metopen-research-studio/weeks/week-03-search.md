# Week 03 — Search

> **Sprint** S3 · **Gate** G3 Evidence Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-02-problem.md) / [Week berikutnya →](week-04-evidence.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Kami mencari dengan kata kunci ___ di basis data ___ dengan kriteria ___, dan setiap kandidat sumber yang kami simpan benar-benar ada."** Strategi pencarian terdokumentasi di `docs/literature/search-strategy.md`, dijalankan dan dicatat di `search-log.csv` (minimal 8 query di minimal 2 basis data), disaring menjadi 30–40 kandidat di `screening.csv`, diperluas lewat citation chaining dari 3–5 sumber kunci, dan setiap DOI/URL dibuka manual sebelum masuk `references.bib`. Ini minggu pertama dari tiga minggu G3 Evidence Ready (W3 Search → W4 Evidence → W5 Gap): PR gate baru dibuka di W5, tetapi satu referensi yang tidak dapat diverifikasi minggu ini sudah cukup untuk menggagalkannya nanti ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3).

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (landscape literatur computing, basis data, citation chaining, kualitas sumber, AI sebagai *literature intelligence*), **60 menit studio** (mencoba tiga basis data dengan satu kata kunci yang sama, menyusun tabel kata kunci, mulai menulis search strategy), **10 menit gate check** (tiap tim membacakan kriteria inklusi/eksklusinya; dosen menguji apakah tim lain bisa mengulang pencariannya). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md); sprint goal dari [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S3.

## Concept (30 menit)

1. **Literatur computing tidak seragam.** Jurnal, konferensi (di computing sering setara atau lebih selektif daripada jurnal), preprint (arXiv — belum direview), thesis, dan grey literature (laporan, dokumentasi, blog) punya bobot bukti berbeda. Sumber sekunder boleh memandu pencarian, tetapi hanya **sumber primer** yang masuk synthesis matrix ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.3).
2. **Kualitas sumber dinilai, bukan diasumsikan.** Kriteria: peer-reviewed atau tidak, venue, tahun, primer/sekunder, apakah ada baseline dan data yang jelas. Jumlah sitasi bukan ukuran kualitas — paper bisa banyak dikutip karena dibantah ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.4).
3. **Kata kunci diturunkan dari Problem Brief, bukan dari algoritma.** Ekstrak 3–5 konsep inti masalah, buat sinonim dan istilah teknis dalam bahasa Inggris dan Indonesia, lalu susun kombinasi boolean. Pencarian yang dimulai dari nama metode menghasilkan daftar paper tentang *algoritma*, bukan tentang *masalah* ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rule B1).
4. **Basis data saling melengkapi.** Google Scholar luas tetapi berisik; Semantic Scholar kuat untuk cited-by dan metadata; Scopus (bila kampus berlangganan) lebih terkurasi; Garuda/SINTA untuk jurnal nasional; OpenAlex/arXiv/ACM DL/IEEE Xplore sesuai akses. Minimal dua basis data, dengan alasan pemilihan tertulis.
5. **Search strategy adalah prosedur yang bisa diulang.** Orang lain harus bisa menjalankan query yang sama, pada basis data yang sama, dengan kriteria inklusi/eksklusi yang sama, dan sampai pada kandidat yang kira-kira sama. Karena itu dicatat: string pencarian, basis data, tanggal, jumlah hasil, rentang tahun, bahasa, kriteria — bukan "kami mencari di Google".
6. **Screening judul/abstrak** menyaring hasil pencarian (biasanya 40–60 atau lebih) menjadi 30–40 kandidat, masing-masing dengan keputusan *include/exclude* **dan alasannya** berdasarkan kriteria yang sudah ditulis. Membaca abstrak bukan membaca paper; pembacaan penuh 15–25 sumber terjadi di W4.
7. **Citation chaining** menutup lubang pencarian kata kunci: *backward* (daftar referensi paper kunci) dan *forward* (siapa yang mengutipnya) dari 3–5 sumber paling sentral. Kandidat yang masuk lewat jalur ini ditandai `sumber=chaining` di log.
8. **Reference manager dan `references.bib`.** Zotero (atau setara) menyimpan PDF, metadata, dan mengekspor BibTeX. Metadata otomatis sering salah (tahun, penulis, versi preprint vs terbit) — setiap entri dicek ke halaman DOI sebelum `.bib` di-commit; satu pemilik `references.bib` per tim ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.5).
9. **AI untuk *literature intelligence*: berguna untuk menemukan, tidak pernah dipercaya untuk mengutip.** Referensi dari AI dianggap **tidak ada** sampai DOI/URL-nya dibuka dan judul-penulis-tahun cocok; yang tidak ditemukan dibuang dan dicatat sebagai `dibuang` di AI Usage Log ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3, [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membaca catatan: *"Bagaimana orang lain dapat mengulang pencarian kami dan sampai pada kandidat sumber yang sama — dan bagaimana kami tahu setiap sumber itu benar-benar ada dan layak dipercaya?"*

## Tasks

Semua task Sprint S3 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add search strategy v1 (OPS-026)`. Task yang belum selesai dari W2 (terutama PR G2 bila belum termerge) ditulis di atas tabel ini pada salinan tim.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-024 | Ikuti sesi Evidence Discovery dan kualitas sumber | Catatan perbandingan basis data | 2h | Menjelaskan fitur basis data; bukan sumber daftar referensi | Mahasiswa menyebutkan kriteria kualitas sumber dengan kata sendiri |
| OPS-025 | Susun daftar kata kunci dan sinonim dari Problem Brief | Tabel kata kunci | 1.5h | Mengusulkan sinonim dan istilah teknis; tim memverifikasi lewat hasil pencarian nyata | Tim menguji tiap kata kunci menghasilkan artikel relevan |
| OPS-026 | Tulis search strategy: basis data, kriteria inklusi/eksklusi | docs/literature/search-strategy.md | 2h | Mengkritik kriteria inklusi/eksklusi yang ambigu | Dosen memeriksa strategi dapat diulang orang lain |
| OPS-027 | Jalankan pencarian dan catat log pencarian | Log pencarian | 3h | - | Tim memeriksa log lengkap dan dapat diulang |
| OPS-028 | Lakukan screening judul/abstrak menjadi 30-40 kandidat | Daftar screening | 3h | Membantu membaca abstrak cepat dan mengelompokkan; keputusan include/exclude oleh manusia | Tim memeriksa sampel 5 keputusan exclude tidak salah buang |
| OPS-029 | Lakukan citation chaining pada 3-5 sumber kunci | Kandidat tambahan dari chaining | 2h | Merangkum kandidat dari daftar cited-by; tim memutuskan | Tim memastikan sumber kunci benar-benar sentral |
| OPS-030 | Verifikasi tiap referensi (DOI/URL) dan buat references.bib | references.bib terverifikasi | 2h | Membantu memformat BibTeX; tidak boleh dipakai untuk menghasilkan referensi | Tiap referensi dibuka manual oleh anggota tim; satu referensi palsu = gate gagal |
| OPS-031 | Buka Issue type:literature-gap awal (hipotesis gap) | Issue type:literature-gap | 0.5h | - | Tim menandai gap sebagai dugaan, bukan temuan |
| OPS-032 | Perbarui AI Usage Log dan jurnal mingguan W3 | AI Usage Log W3 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 16.5h** (jam tim; untuk tim 2 orang bagi dua). Sprint ini tergolong sedang secara jam, tetapi **hampir sepenuhnya berantai** — slack terkecil kedua di semester ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel); satu task yang tertunda menggeser semua task setelahnya.

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-024** di sesi studio (hanya bergantung pada Problem Brief W2) → **OPS-025** tabel kata kunci → **OPS-026** search strategy (butuh PR G2 termerge, OPS-022) → **OPS-027** jalankan pencarian — bagi *query* antar anggota, ini satu-satunya titik paralel → **OPS-028** screening → **OPS-029** chaining → **OPS-030** verifikasi dan `references.bib` (butuh 028 dan 029); **OPS-031** Issue literature-gap dapat dibuka begitu screening selesai (butuh Research ID resmi dari OPS-021); **OPS-032** berjalan sepanjang minggu dan ditutup Jumat setelah OPS-030.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g3-evidence` (dipakai sampai PR G3 di W5), harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Catatan perbandingan 3 basis data dengan satu kata kunci yang sama (jumlah hasil, kualitas metadata, fitur cited-by) + jurnal W3: apa yang paling mengejutkan dari hasil pencarian | `docs/journal/w03.md` | commit di `research/g3-evidence` | OPS-024, OPS-032 |
| **Search strategy**: §Keywords (3–5 konsep inti, sinonim EN/ID, kombinasi boolean), basis data dan alasannya, rentang tahun, bahasa, kriteria inklusi/eksklusi, kriteria kualitas sumber, cara mencatat hasil, **tanggal pencarian**, nomor Issue literature-gap | `docs/literature/search-strategy.md` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) | commit | OPS-025, OPS-026, OPS-031 |
| **Log pencarian**: kolom query · basis data · tanggal · jumlah hasil · jumlah diambil · sumber (`keyword`/`chaining`); minimal 8 query di minimal 2 basis data; entri `sumber=chaining` dari 3–5 sumber kunci | `docs/literature/search-log.csv` | commit | OPS-027, OPS-029 |
| **Daftar screening**: satu baris per kandidat dengan judul, penulis, tahun, venue, DOI/URL, keputusan include/exclude, alasan (merujuk kriteria), kolom `verified=yes/no`; 30–40 kandidat berstatus include | `docs/literature/screening.csv` | commit | OPS-028, OPS-030 |
| **`references.bib` terverifikasi**: hanya entri yang DOI/URL-nya dibuka manual dan cocok; diekspor dari reference manager; entri yang dibuang tidak masuk | `references.bib` (root repositori riset) | commit | OPS-030 |
| Issue `type:literature-gap` berisi 1–3 **dugaan** gap berstatus "belum diverifikasi", tertaut ke Research ID; akan diuji terhadap synthesis matrix di W5 | Issue di repo pusat (form [Literature Gap](../../.github/ISSUE_TEMPLATE/05-literature-gap.yml)); nomor Issue dicatat di `search-strategy.md` | URL Issue + commit | OPS-031 |
| AI Usage Log W3: entri untuk usulan kata kunci, pra-screening abstrak, format BibTeX, dan **verifikasi sumber** — termasuk referensi usulan AI yang dibuang dan alasannya | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-030, OPS-032 |

README riset diperbarui: `Current Research Gate: G3 (in progress — W3 Search)`. Tidak ada PR gate dan tidak ada release minggu ini; artefak di atas menjadi bagian *Strategi pencarian* dan *Evidence* pada PR `GATE REVIEW: Evidence Ready` di W5 ([evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md)).

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan** dengan Stage `Search`. Minggu ini AI paling berguna untuk **menemukan**; reviewer G3 akan membaca log ini secara khusus untuk melihat bagaimana sumber dari AI diverifikasi.

**Boleh minggu ini**

- Meminta AI menjelaskan fitur basis data (filter, ekspor `.bib`, cited-by, operator boolean) sebelum mencobanya sendiri (OPS-024) — bukan meminta daftar referensi.
- Meminta AI mengusulkan sinonim, istilah teknis, dan variasi lintas bahasa untuk tiap konsep inti (OPS-025); tiap kata kunci diuji pada basis data nyata dan hanya yang menghasilkan artikel relevan yang dipertahankan.
- Meminta AI mengkritik kriteria inklusi/eksklusi yang ambigu ("relevan" itu apa? rentang tahun kenapa?) sebelum strategi di-commit (OPS-026).
- Memakai tool literature search / deep research / citation intelligence ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.2–2.4) untuk **menemukan kandidat**, dengan setiap kandidat ditandai asal-usulnya di log dan diverifikasi DOI/URL-nya.
- Meminta AI membaca abstrak secara cepat dan mengelompokkan kandidat berdasarkan tema sebagai pra-screening (OPS-028); keputusan include/exclude dan alasannya ditulis manusia.
- Meminta AI merangkum daftar cited-by dari sumber kunci untuk memilih mana yang layak diperiksa (OPS-029); tim yang memutuskan dan membuka sumbernya.
- Meminta AI membantu memformat atau merapikan entri BibTeX yang sudah terverifikasi (OPS-030).

**Tidak boleh**

- Meminta AI "menghasilkan referensi" atau memasukkan referensi usulan AI ke `screening.csv`/`references.bib` tanpa membuka DOI/URL asli; satu referensi palsu = G3 gagal, dan referensi buatan AI yang lolos ke proposal = fabrikasi ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4, §2.8).
- Menganggap ringkasan AI atas sebuah paper sebagai "sudah membaca" — screening W3 hanya judul/abstrak, dan pembacaan penuh W4 dilakukan manusia.
- Mengunggah PDF berlisensi terbatas ke layanan AI, atau memasukkan kutipan wawancara/data stakeholder dari W2 ke prompt ([LICENSING.md](../../LICENSING.md), [SECURITY.md](../../SECURITY.md)).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-027 (menjalankan dan mencatat pencarian), OPS-031 (Issue literature-gap), OPS-032 (log & jurnal) — ketiganya adalah rekaman proses dan pertanggungjawaban manusia.
- Membiarkan AI merumuskan "gap" dari daftar kandidat: gap yang sah hanya lahir dari synthesis matrix di W5, bukan dari daftar judul.

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa dapat menyebutkan kriteria kualitas sumber (peer review, venue, tahun, primer/sekunder, ada baseline/data) dengan kata sendiri, tanpa membaca catatan | diri sendiri, diuji peer di 10 menit gate check | OPS-024 |
| Setiap kata kunci di tabel menghasilkan minimal satu artikel relevan pada basis data nyata; kata kunci yang hanya menghasilkan paper tentang algoritma dibuang | tim (dua anggota mencoba query secara independen) | OPS-025 |
| Search strategy dapat diulang orang lain: basis data, string, rentang tahun, bahasa, kriteria, dan tanggal tertulis; tim lain di studio mencoba satu query dan mendapat hasil serupa | dosen pengampu (spot-check di gate check); peer dari tim lain | OPS-026 |
| Log pencarian lengkap dan dapat diulang: setiap baris punya query, basis data, tanggal, jumlah hasil; minimal 8 query, minimal 2 basis data | tim | OPS-027 |
| Sampel 5 keputusan *exclude* dibaca ulang oleh anggota yang tidak memutuskannya: tidak ada sumber relevan yang salah buang; setiap alasan merujuk kriteria tertulis | tim (peer internal) | OPS-028 |
| 3–5 sumber kunci yang dipakai chaining benar-benar sentral (muncul berulang, dikutip kandidat lain), bukan sekadar yang pertama ditemukan | tim; mentor bila sudah ada | OPS-029 |
| **Setiap** referensi dibuka manual oleh anggota tim: DOI/URL mengarah ke artikel yang benar, judul-penulis-tahun cocok, versi terbit dibedakan dari preprint; kolom `verified=yes` hanya untuk yang lolos; dosen membuka 3 sumber acak: ada, relevan, kriteria pencarian benar-benar dipakai | tim (dua anggota memeriksa silang); dosen pengampu | OPS-030 |
| Dugaan gap di Issue ditandai sebagai **dugaan**, bukan temuan; tidak ada kalimat "belum ada yang meneliti" tanpa rujukan ke hasil screening | tim | OPS-031 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya, khususnya entri verifikasi sumber (berapa usulan AI, berapa ditemukan, berapa dibuang) | diri sendiri | OPS-032 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W3, "dapat dibuka reviewer" berarti reviewer bisa memilih baris acak di `screening.csv`, mengklik DOI/URL-nya, dan mendapatkan artikel yang sama.

## Done When

Minggu ini **belum menutup gate** — G3 Evidence Ready berlangsung W3–W5 dan PR-nya dibuka di W5. Jawab ya/tidak per butir pada Jumat:

- [ ] PR `GATE REVIEW: Problem Ready` (G2) sudah termerge dan Research ID resmi `UIAI-YYYY-NNN` ada — search strategy (OPS-026) tidak ditulis sebelum itu (blocking rule B1).
- [ ] Branch `research/g3-evidence` dibuat dari branch utama; folder `docs/literature/` ada.
- [ ] `docs/journal/w03.md` berisi perbandingan 3 basis data dengan satu kata kunci yang sama dan refleksi minggu ini.
- [ ] `docs/literature/search-strategy.md` lengkap: §Keywords, basis data + alasan, rentang tahun, bahasa, kriteria inklusi/eksklusi, kriteria kualitas sumber, cara mencatat, tanggal pencarian, nomor Issue literature-gap; tidak ada nama algoritma sebagai kata kunci utama.
- [ ] `docs/literature/search-log.csv` berisi minimal 8 query pada minimal 2 basis data, plus entri `sumber=chaining` dari 3–5 sumber kunci.
- [ ] `docs/literature/screening.csv` berisi 30–40 kandidat *include* dengan alasan; setiap *exclude* punya alasan; sampel 5 exclude sudah dicek ulang.
- [ ] `references.bib` hanya berisi entri `verified=yes`; 100% DOI/URL dibuka manual; entri yang dibuang tercatat di AI Usage Log atau kolom alasan screening.
- [ ] Issue `type:literature-gap` terbuka dengan 1–3 dugaan gap berstatus "belum diverifikasi", tertaut ke Research ID, nomornya dicatat di search strategy.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Search` untuk kata kunci, pra-screening, dan verifikasi sumber (termasuk yang dibuang); tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] Dosen membuka 3 sumber acak dari `screening.csv` di gate check: semuanya ada, relevan, dan konsisten dengan kriteria.
- [ ] README riset: `Current Research Gate: G3 (in progress — W3 Search)`.

**Progres menuju G3** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G3). Dari empat butir definition of done G3, minggu ini menuntaskan *strategi pencarian terdokumentasi* dan *setiap sumber terverifikasi (DOI/URL)*, serta memulai *`references.bib` terkelola*; W4 menambahkan *synthesis matrix* 15–25 sumber yang benar-benar dibaca, W5 menambahkan pola (konsisten/bertentangan/belum diuji) dan kandidat gap, lalu tim membuka PR **`GATE REVIEW: Evidence Ready`** dari `research/g3-evidence` memakai [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3; task OPS-047). Ingat kriteria gagalnya sejak sekarang: **satu saja referensi yang tidak dapat diverifikasi keberadaannya = G3 gagal**, terlepas dari kualitas matriks. Bila PR G2 belum termerge di Senin, ikuti skenario "G2 terlambat 1 minggu" di [OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat: kerjakan OPS-025 dari draft Problem Brief, jangan mulai pencarian dengan kata kunci algoritma.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — `docs/AI-USAGE.md` (contoh terisi baris Stage `Search`: usulan kata kunci, referensi AI yang dibuang).
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `references.bib`, `docs/`, branch `research/g3-evidence`.
- [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) — butir integritas sitasi yang akan ditandatangani di W15; baca sekarang agar tahu apa yang diperiksa.
- Form Issue [Literature Gap](../../.github/ISSUE_TEMPLATE/05-literature-gap.yml) (OPS-031) dan template PR [evidence-review.md](../../.github/PULL_REQUEST_TEMPLATE/evidence-review.md) (dipakai W5; bagian *Strategi pencarian* bisa diisi dari minggu ini).

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W3 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.3 Literature Evidence Map, §4 struktur repositori · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.2 E2 Evidence · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.4 citation integrity, §2.8 AI usage.
- [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) tahap 2 Search · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 izin/larangan · [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.2–2.5 deep research, literature search, citation intelligence, reference management; §4 kebijakan data.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S3 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G3 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rules B1–B2, §S3 · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) · [SECURITY.md](../../SECURITY.md) · [LICENSING.md](../../LICENSING.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Referensi dari AI yang tidak dibuka.** Judul dan penulis terdengar masuk akal, DOI tidak ada. Satu saja yang lolos ke `references.bib` = G3 gagal, dan bila sampai ke proposal = fabrikasi. Cara menghindari: setiap usulan AI masuk log dengan status `dibuang`/`terverifikasi`; tidak ada entri `.bib` tanpa kolom `verified=yes` di `screening.csv`; dua anggota memeriksa silang sebelum commit.
2. **Mencari algoritma, bukan masalah.** Kata kunci utama "random forest", "LSTM", "chatbot" menghasilkan tumpukan paper tentang metode yang tidak menjawab apa yang sudah diketahui tentang *masalah* tim. Cara menghindari: tabel kata kunci diturunkan dari 3–5 konsep inti Problem Brief; nama metode paling banyak menjadi kata kunci pelengkap, bukan pusat query ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) B1).
3. **Pencarian yang tidak bisa diulang.** "Kami cari di Google Scholar" tanpa string, tanggal, dan jumlah hasil. Reviewer tidak bisa mereplikasi, dan tim sendiri tidak tahu query mana yang perlu dilengkapi di W4 (OPS-038). Cara menghindari: isi `search-log.csv` **saat** mencari, bukan Jumat; satu baris per query per basis data.
4. **Abstrak dianggap paper; blog dianggap sumber primer.** Screening W3 memang hanya judul/abstrak, tetapi keputusan *include* bukan berarti paper sudah dibaca; dan sumber sekunder (blog, dokumentasi, ringkasan AI) tidak boleh masuk hitungan 15–25 sumber primer. Cara menghindari: kolom `jenis` (jurnal/konferensi/preprint/thesis/grey) di `screening.csv`; sumber sekunder hanya sebagai jalan menuju sumber primernya.
5. **Jumlah sitasi dan metadata otomatis dipercaya begitu saja.** Paper "paling banyak dikutip" belum tentu terbaik, dan reference manager sering salah tahun atau mengambil versi preprint. Cara menghindari: kualitas dinilai dari venue, peer review, dan kejelasan baseline/data (OPS-040 di W4); setiap entri `.bib` dicocokkan ke halaman DOI; versi terbit diutamakan atas preprint.
6. **Gap "ditemukan" terlalu dini.** Setelah screening, tergoda menulis "belum ada yang meneliti X" sebagai temuan. Cara menghindari: Issue literature-gap W3 hanya berisi **dugaan** berstatus "belum diverifikasi"; gap yang sah baru lahir dari synthesis matrix di W5 dan harus menunjuk baris matriks ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G4).
