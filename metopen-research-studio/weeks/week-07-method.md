# Week 07 — Method

> **Sprint** S7 · **Gate** G5 Method Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-06-rq.md) / [Week berikutnya →](week-08-design-defense.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan draft kalimat G5 dari [OPS-03](../../research-os/06-execution-os/03-research-gates.md): **"Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___."** RQ yang lolos G4 di W6 dipasangkan dengan jenis metode dari Computing Research Methods Map (beserta alternatif yang ditolak), lalu diturunkan menjadi variabel/konstruk dengan definisi operasional, kontrol, sampling, Dataset/Data Plan dengan kartu dataset, baseline paling sederhana, dan metrik yang **terkunci dengan tanggal commit** — semuanya dirangkum dalam Research Design Card dan ditutup dengan Threats to Validity v0, **sebelum satu baris kode eksperimen ditulis** ([OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S7; [MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W7). Ini minggu pembuka G5 (W7 Method → W8 Design Defense): Ethics & Privacy, Experiment Card, pitch, red team, dan PR `GATE REVIEW: Method Ready` menyusul di W8.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (Methods Map — kapan dipakai, bukti apa yang dihasilkan, ancaman khasnya; variabel, kontrol, confounder; baseline & metrik; leakage; empat validitas), **60 menit studio** (latihan mencocokkan 5 RQ contoh dengan jenis metode dan ancaman validitasnya, lalu tim mengisi tabel pemilihan metode untuk RQ-nya sendiri dan mulai mendefinisikan variabel), **10 menit gate check** (tiap tim membacakan draft kalimat G5; dosen menguji apakah baseline dan metrik sudah disebut dengan nama, bukan "akan ditentukan"). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md).

## Concept (30 menit)

1. **Metode dipilih karena mampu menghasilkan bukti yang RQ butuhkan — bukan karena familiar.** Methods Map menyediakan sepuluh jenis: experiment, benchmarking, design science, empirical SE study, ML research, simulation, survey, user study, case study, qualitative; masing-masing punya pertanyaan yang cocok, bukti yang dihasilkan, dan ancaman khas (misalnya ML research: leakage, seed cherry-picking, metric switching). Tulis alternatif yang ditolak beserta alasannya ([TPL-08](../../research-os/08-templates/08-research-design-card.md); [MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.7).
2. **Metode menunggu RQ** (blocking rule B4, [OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md)): OPS-060 baru boleh dimulai setelah PR G4 termerge. Kalau urutannya dibalik, metode menjadi jawaban yang mencari pertanyaan.
3. **Variabel harus bisa diukur orang lain.** Setiap variabel/konstruk punya definisi operasional ("akurasi" tanpa cara hitung bukan definisi); kontrol dan confounder disebut; unit analisis dan strategi sampling ditetapkan. Uji utamanya: orang lain dapat menjalankan desain ini tanpa bertanya ke tim ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G5).
4. **Tanpa baseline, angka metrik tidak bermakna** ([MST-03](../../research-os/00-master/03-glossary.md) §5). Minimal satu baseline trivial (majority class, rata-rata, heuristik) dan satu baseline literatur dengan sitasi dari `references.bib`; baseline harus cukup sederhana *dan* adil terhadap metode yang diuji.
5. **Metrik dikunci sebelum hasil terlihat.** Metrik utama dan sekunder dipilih karena selaras dengan RQ, dengan ambang "berarti secara praktis" yang ditetapkan sekarang. Setelah W7, metrik dan baseline tidak diubah setelah melihat hasil; bila terpaksa, catat alasan dan tanggalnya ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Metric switching adalah pelanggaran amanah epistemik.
6. **Leakage dicegah oleh prosedur, bukan niat.** Kebocoran informasi dari data uji ke pelatihan/pemilihan model membuat hasil tampak lebih baik dari kenyataan ([MST-03](../../research-os/00-master/03-glossary.md) §5). Prosedur evaluasi menyebut split/CV, seed, jumlah run, dan daftar sumber leakage (pra-pemrosesan sebelum split, duplikat lintas split, tuning pada data uji) beserta pencegahannya ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.9).
7. **Data plan adalah bagian dari desain, bukan lampiran.** Sumber, cara akses, lisensi, kelas privasi (Public / Restricted / Confidential), ukuran, representativitas terhadap populasi, rencana split, dan rencana cadangan bila akses gagal. Kartu dataset ([TPL-05](../../research-os/08-templates/05-dataset-registry-template.md)) adalah metadata: data mentah tidak pernah masuk GitHub ([datasets-registry](../../datasets-registry/README.md); [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5).
8. **Empat threats to validity, ditulis spesifik untuk riset ini.** Internal, eksternal, konstruk, statistik/kesimpulan — masing-masing dengan dampak dan mitigasi, atau dinyatakan diterima dengan alasan. "Label dibuat oleh satu annotator" adalah ancaman; "keterbatasan waktu" bukan ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.11; [AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §7 Falsification).
9. **AI adalah red team desain, bukan pemilih metrik.** Meminta AI mencari confounder yang terlewat atau menyerang desain adalah penggunaan paling bernilai minggu ini; tetapi bila tim tidak bisa menjustifikasi metrik/baseline tanpa AI, tim belum siap G5 ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.7).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membaca catatan: *"Kalau orang lain diberi `docs/research-design.md` kami tanpa boleh bertanya, bisakah mereka menjalankan desain ini — dan angka pada metrik mana yang akan membuktikan RQ kami salah?"*

## Tasks

Semua task Sprint S7 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Lock primary metric and evaluation protocol (OPS-065)`. Task W6 yang belum selesai — terutama OPS-057 PR `GATE REVIEW: Question Ready` — ditulis di atas tabel ini pada salinan tim: sesi OPS-059 tetap diikuti, tetapi OPS-060 dan seluruh rantai di bawahnya menunggu PR G4 termerge (blocking rule B4).

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-059 | Ikuti sesi Computing Research Methods Map dan validitas | Latihan metode-validitas | 2h | Menjelaskan perbedaan jenis metode dengan contoh | Mahasiswa memilih metode untuk RQ contoh dengan alasan |
| OPS-060 | Pilih jenis metode dari Methods Map untuk tiap RQ | Tabel pemilihan metode | 2h | Menawarkan alternatif metode dan kelemahannya; keputusan oleh tim | Mentor memeriksa metode mampu menjawab RQ |
| OPS-061 | Definisikan variabel, konstruk, kontrol, dan sampling | Bagian Variables & Controls di docs/research-design.md | 2h | Mengusulkan confounder yang mungkin terlewat | Tim memverifikasi definisi operasional dapat diukur |
| OPS-062 | Tulis Dataset/Data Plan: sumber, akses, lisensi, privasi, ukuran | docs/data-plan.md | 2.5h | Membantu menelusuri lisensi dataset; tim memverifikasi ke sumber asli | Tim memastikan data boleh dipakai dan tidak memuat data pribadi tanpa izin |
| OPS-063 | Daftarkan dataset ke datasets-registry (dataset card) | Dataset card + Issue type:dataset | 1.5h | Membantu merapikan metadata; nilai lisensi/privasi diverifikasi tim | Pengelola registry memeriksa privasi dan lisensi |
| OPS-064 | Tetapkan baseline paling sederhana dan alasannya | Bagian Baseline di docs/research-design.md | 1.5h | Mengusulkan baseline sederhana; tim memilih | Mentor memeriksa baseline cukup sederhana dan adil |
| OPS-065 | Pilih metrik yang selaras dengan RQ dan prosedur evaluasi anti-leakage | Bagian Metrics & Evaluation di docs/research-design.md | 2h | Menjelaskan sifat metrik dan skenario leakage; tim memutuskan | Dosen memeriksa metrik selaras RQ dan prosedur mencegah leakage |
| OPS-066 | Isi Research Design Card (TPL-08) | docs/design-card.md | 1.5h | Merapikan bahasa; isi dari dokumen tim | Mentor memeriksa orang lain dapat menjalankan desain tanpa bertanya |
| OPS-067 | Tulis Threats to Validity awal (4 jenis validitas) | docs/research-design.md bagian Threats to Validity v0 | 1.5h | Berperan sebagai red team mengusulkan ancaman; tim menilai relevansi | Tim memastikan tiap ancaman punya mitigasi atau dinyatakan diterima |
| OPS-068 | Perbarui AI Usage Log dan jurnal mingguan W7 | AI Usage Log W7 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 17h** (jam tim; untuk tim 2 orang bagi dua). Beban sedang dengan kerapuhan rendah: 8 jam pada critical path, slack 9 jam ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer) — tetapi dua task di sini, OPS-064 dan OPS-065, mengunci seluruh sprint kode S9 (blocking rule B5), sehingga keduanya tidak boleh digeser ke W8.

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-059** di sesi studio, lalu **OPS-060** begitu PR G4 termerge → bercabang ke dua jalur paralel yang dikerjakan anggota berbeda: jalur **data** **OPS-061** → **OPS-062** (butuh `common-metrics-baselines.md` OPS-037 dari W4) → **OPS-063**, dan jalur **evaluasi** **OPS-064** (juga butuh OPS-037) → **OPS-065**; kedua jalur bertemu di **OPS-066** design card → **OPS-067** threats v0; **OPS-068** berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch baru `research/g5-method` (dibuat dari `main` setelah PR G4 merge; PR G5 sendiri dibuka di W8), harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Latihan metode–validitas: 5 RQ contoh, masing-masing dengan jenis metode, alasan, dan ancaman validitas khas + jurnal W7: keputusan desain mana yang paling berisiko dan mengapa | `docs/journal/w07.md` | commit | OPS-059, OPS-068 |
| **Research Design** §Method Selection: tabel RQ \| bukti yang dibutuhkan \| jenis metode \| alternatif ditolak + alasan; §Variables & Controls: variabel/konstruk dengan definisi operasional, kontrol, confounder yang diwaspadai, unit analisis, sampling | `docs/research-design.md` | commit; tiap variabel punya definisi operasional | OPS-060, OPS-061 |
| **Dataset/Data Plan**: sumber, cara akses, lisensi, kelas privasi, ukuran, representativitas, rencana split train/val/test atau sampel, batasan, rencana cadangan; URL dan lisensi sumber tercantum; `data/README.md` menunjuk ke sini | `docs/data-plan.md` (dirujuk dari `docs/research-design.md` §Data, sesuai [MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.8) | commit; **tidak ada data mentah di git** | OPS-062 |
| **Dataset card** ([TPL-05](../../research-os/08-templates/05-dataset-registry-template.md)): dataset, domain, URL/source, owner, license, size, modality, quality, privacy, possible RQs; Issue `type:dataset` lewat form [Dataset](../../.github/ISSUE_TEMPLATE/03-dataset.yml); PR ke `datasets-registry/datasets/` + baris di [REGISTRY.md](../../datasets-registry/REGISTRY.md) | repo pusat `datasets-registry/datasets/DS-YYYY-NNN-<slug>.md`; nomor Issue dan URL PR dicatat di data plan | URL Issue, URL PR; Dataset ID `DS-YYYY-NNN` diberikan pengelola registry | OPS-063 |
| §Baseline: ≥1 baseline trivial (mayoritas/rata-rata/heuristik) + ≥1 baseline literatur dengan sitasi dari `references.bib`, alasan, dan cara implementasi | `docs/research-design.md` §Baseline | commit | OPS-064 |
| §Metrics & Evaluation: metrik utama + sekunder dan alasan keselarasan dengan RQ; ambang "berarti secara praktis"; prosedur split/CV, seed, jumlah run; daftar sumber leakage dan pencegahannya; **baris "Metrik terkunci pada YYYY-MM-DD, commit <hash>"** | `docs/research-design.md` §Metrics & Evaluation (disalin ke `experiments/config/` di W9) | commit bertanggal sebelum eksperimen | OPS-065 |
| **Research Design Card** ([TPL-08](../../research-os/08-templates/08-research-design-card.md)): satu halaman — metode, variabel, data, baseline, metrik, prosedur, threats awal — tanpa field kosong, tiap baris tertaut ke bagian rinci (bila tim memilih satu file seperti saran TPL-08, jadikan kartu bagian pertama `research-design.md`; jangan dua salinan berbeda isi) | `docs/design-card.md` | commit; tidak ada field kosong | OPS-066 |
| §Threats to Validity v0: tabel Threat \| Jenis \| Dampak \| Mitigasi \| Status, minimal 2 ancaman per jenis (internal, eksternal, konstruk, statistik/kesimpulan); kritik AI yang diterima/ditolak tercatat | `docs/research-design.md` §Threats to Validity | commit | OPS-067 |
| AI Usage Log W7: entri Stage `Method` — penjelasan metode, alternatif yang ditawarkan AI, confounder usulan, penelusuran lisensi, red team threats — beserta klasifikasi terima/ubah/tolak | `docs/ai-usage-log.md`, ringkasan di `docs/AI-USAGE.md` ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-068 |

README riset diperbarui: `Current Research Gate: G4 passed → G5 (in progress — W7 Method)`. Research One-Pager ([TPL-01](../../research-os/08-templates/01-research-one-pager-template.md)) bagian Method/Data/Baseline/Metric boleh mulai diisi dari design card, tetapi versi resminya (v2) baru di W12. Tidak ada file di `src/` atau `experiments/` yang berisi kode eksperimen minggu ini.

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan** dengan Stage `Method`. Minggu ini AI paling berguna sebagai **penjelas dan red team desain**; keputusan metode, baseline, dan metrik tetap milik tim, dengan justifikasi yang bisa tim ucapkan tanpa membuka chat. Reviewer G5 membaca log untuk satu hal utama: apakah setiap kritik AI diklasifikasi terima/ubah desain/tolak dengan alasan ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.7).

**Boleh minggu ini**

- Meminta AI menjelaskan perbedaan jenis metode dengan contoh, dan berlatih mencocokkan RQ contoh dengan metode sebelum menyentuh RQ tim sendiri (OPS-059).
- Meminta AI menawarkan alternatif metode beserta kelemahannya (OPS-060) dan mengusulkan baseline sederhana (OPS-064); tim yang memilih dan menulis alasannya — alternatif yang ditolak ikut dicatat.
- Meminta AI mengusulkan confounder yang mungkin terlewat (OPS-061) dan berperan sebagai red team yang menyerang desain untuk tabel threats (OPS-067); tim menilai relevansi tiap usulan.
- Meminta AI membantu menelusuri lisensi dataset dan merapikan metadata kartu dataset (OPS-062, OPS-063); nilai lisensi dan privasi diverifikasi tim ke halaman sumber asli, bukan ke jawaban AI.
- Meminta AI menjelaskan sifat metrik (apa yang diukur, kapan menyesatkan, misalnya accuracy pada kelas tidak seimbang) dan skenario leakage untuk jenis data tim (OPS-065); tim memutuskan metrik dan prosedurnya ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.9).
- Meminta AI merapikan bahasa design card (OPS-066); isinya dari dokumen tim, tanpa menambah keputusan baru.

**Tidak boleh**

- Membiarkan AI **memilih** metrik atau baseline tanpa justifikasi yang dipahami tim; "disarankan AI" bukan alasan, dan metrik yang dipilih AI setelah melihat hasil adalah metric switching ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3; [MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W7).
- Memasukkan **data mentah**, data pribadi, data partner, atau sampel dataset Restricted/Confidential ke layanan AI — termasuk saat meminta bantuan menilai representativitas ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5; [SECURITY.md](../../SECURITY.md)).
- Menyalin daftar threats generik dari AI ke `research-design.md` tanpa mengklasifikasi tiap usulan; log yang tidak memuat satu pun kritik yang ditolak adalah red flag bahwa tim tidak menilai.
- Menerima lisensi atau ketentuan dataset "menurut AI" tanpa membuka halaman lisensi sumber asli; kartu dataset yang salah lisensi gagal di review pengelola registry ([LICENSING.md](../../LICENSING.md)).
- Memakai AI pada OPS-068 (log & jurnal): WBS menandainya tanpa bantuan AI — jurnal adalah rekaman penilaian manusia.

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa dapat memilih metode untuk 5 RQ contoh dengan alasan yang menyebut bukti yang dibutuhkan, bukan "biasa dipakai" | diri sendiri, diuji peer pada 10 menit gate check | OPS-059 |
| Metode yang dipilih mampu menjawab RQ; alternatif yang ditolak masuk akal | mentor | OPS-060 |
| Setiap definisi operasional dapat diukur: ada cara hitung/instrumen, bukan sekadar nama variabel | tim (anggota yang tidak menulis bagian itu membaca ulang) | OPS-061 |
| Data boleh dipakai (lisensi, izin, syarat redistribusi) dan tidak memuat data pribadi tanpa izin; tidak ada data mentah di git | tim | OPS-062 |
| Kolom Privacy dan License kartu dataset benar; kelas privasi sesuai [datasets-registry](../../datasets-registry/README.md) §4 | pengelola registry (review PR), komite etik bila data manusia | OPS-063 |
| Baseline cukup sederhana *dan* adil: tidak dilemahkan agar metode tampak unggul | mentor | OPS-064 |
| Metrik selaras dengan RQ; prosedur evaluasi (split/CV, seed, jumlah run) mencegah leakage; metrik terkunci dengan tanggal **sebelum tim menyentuh kode eksperimen** | dosen pengampu | OPS-065 |
| Orang lain dapat menjalankan desain dari design card tanpa bertanya ke tim; tidak ada field kosong | mentor | OPS-066 |
| Setiap ancaman punya mitigasi, atau dinyatakan diterima dengan alasan; minimal 2 per jenis | tim | OPS-067 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya: kritik AI mana yang diterima, diubah, ditolak | diri sendiri | OPS-068 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W7, "dapat dibuka reviewer" berarti mentor bisa membaca `docs/design-card.md` sendirian dan menuliskan langkah 1 → n yang akan ia jalankan tanpa menghubungi tim.

## Done When

Minggu ini **belum menutup gate**; G5 Method Ready ditutup di W8 setelah pitch dan red team. Jawab ya/tidak per butir pada Jumat:

- [ ] `docs/journal/w07.md` berisi latihan 5 RQ contoh (metode + alasan + ancaman khas) dan refleksi: keputusan desain mana yang paling berisiko.
- [ ] `docs/research-design.md` §Method Selection: setiap RQ punya jenis metode, bukti yang dibutuhkan, dan alternatif yang ditolak beserta alasan.
- [ ] §Variables & Controls: setiap variabel/konstruk punya definisi operasional; confounder, unit analisis, dan sampling tertulis.
- [ ] `docs/data-plan.md` lengkap (sumber, akses, lisensi, privasi, ukuran, representativitas, split, batasan, rencana cadangan); URL dan lisensi tercantum; tidak ada data mentah di riwayat git.
- [ ] Issue `type:dataset` dibuka dan PR kartu dataset ke `datasets-registry/` diajukan; Dataset ID menunggu pengelola.
- [ ] §Baseline memuat ≥1 baseline trivial + ≥1 baseline literatur dengan sitasi yang ada di `references.bib`.
- [ ] §Metrics & Evaluation memuat metrik utama/sekunder + alasan, ambang praktis, prosedur split/CV/seed/jumlah run, daftar sumber leakage; **metrik dan baseline terkunci dengan tanggal dan hash commit**.
- [ ] `docs/design-card.md` tanpa field kosong dan tertaut ke bagian rinci.
- [ ] §Threats to Validity v0: tabel Threat \| Jenis \| Dampak \| Mitigasi \| Status dengan ≥2 ancaman per jenis.
- [ ] `docs/ai-usage-log.md` memuat entri Stage `Method` dengan klasifikasi terima/ubah/tolak; tiap anggota sudah memverifikasi entrinya; `docs/AI-USAGE.md` diperbarui.
- [ ] Branch `research/g5-method` ada; README riset menunjukkan `G5 (in progress)`; **belum ada kode eksperimen** di `src/` atau `experiments/`.

**Progres menuju gate.** Butir-butir di atas adalah setengah pertama definition of done G5 ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G5): Research Design Card, Dataset/Data Plan, Baseline & Metrics, dan Threats awal. Setengah kedua dikerjakan di W8: Ethics & Privacy (`docs/ethics.md`, OPS-070), Experiment Card pilot ([TPL-09](../../research-os/08-templates/09-experiment-card.md), OPS-071), slide pitch, red team, revisi desain, lalu PR **`GATE REVIEW: Method Ready — UIAI-YYYY-NNN`** dari branch `research/g5-method` memakai [method-review.md](../../.github/PULL_REQUEST_TEMPLATE/method-review.md) (OPS-076; [CONTRIBUTING.md](../../CONTRIBUTING.md) §3). Ingat kriterianya sejak sekarang: **lulus** jika orang lain dapat menjalankan desain ini tanpa bertanya ke tim; **gagal** jika metrik/baseline belum ditetapkan — eksperimen tidak boleh dimulai sebelum keduanya ada. Bila W7 tertinggal, gunakan slack S8 (15 jam) untuk mengejar, tetapi kunci baseline trivial dan metrik utama (OPS-064/065) lebih dulu — itulah satu-satunya yang boleh membuka OPS-079/080 di W9 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat).

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-08 Research Design Card](../../research-os/08-templates/08-research-design-card.md) — Methods Map, tabel kartu, contoh terisi, kriteria good vs weak (OPS-060, OPS-061, OPS-066, OPS-067).
- [TPL-05 Dataset Registry Template](../../research-os/08-templates/05-dataset-registry-template.md) — kartu dataset dan aturan "GitHub = catalog, bukan storage" (OPS-062, OPS-063); form Issue [Dataset](../../.github/ISSUE_TEMPLATE/03-dataset.yml); indeks [REGISTRY.md](../../datasets-registry/REGISTRY.md).
- [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) — baca bagian pra-registrasi sekarang; baseline dan metrik yang dikunci minggu ini akan disalin ke sana di W8 (OPS-071).
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — entri Stage `Method`; contoh baris #9 "red-team desain eksperimen" adalah pola yang dipakai minggu ini.
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `docs/research-design.md`, `docs/data-plan.md`, `data/README.md`, aturan `.gitignore` data.
- [TPL-01 Research One-Pager Template](../../research-os/08-templates/01-research-one-pager-template.md) — bagian Method/Data/Baseline/Metric; template PR [method-review.md](../../.github/PULL_REQUEST_TEMPLATE/method-review.md) untuk W8.

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W7 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.7 Research Design, §3.8 Data Plan, §3.9 Baseline & Metrics, §3.11 Threats · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3 E3 Experiment · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5 Dataset & privacy.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §7 Falsification, §9 Causal & statistical reasoning · [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.7 Method · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 · [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md) §2.9 Statistics.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S7 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G5 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rules B4–B5, §Slack dan buffer · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) §5 Baseline, Leakage, Threats · [datasets-registry](../../datasets-registry/README.md) · [LICENSING.md](../../LICENSING.md) · [SECURITY.md](../../SECURITY.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Metode dipilih karena familiar, bukan karena RQ.** "Kami pakai Random Forest karena sudah pernah" atau "metode kuantitatif" tanpa prosedur adalah level *Beginning* pada rubrik E3 ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3). Cara menghindari: kolom "bukti yang dibutuhkan RQ" diisi lebih dulu, baru kolom metode; alternatif yang ditolak wajib ditulis dengan alasan.
2. **Metrik ditunda "sampai lihat data" — atau dipilih AI.** Ini benih metric switching: memilih metrik yang kebetulan bagus setelah hasil terlihat. Cara menghindari: metrik utama, ambang praktis, dan prosedur evaluasi dikunci minggu ini dengan tanggal dan hash commit; setiap perubahan setelahnya dicatat beserta alasannya; justifikasi harus bisa diucapkan tim tanpa membuka chat AI.
3. **Tidak ada baseline trivial, atau hanya accuracy pada data tidak seimbang.** Angka 92% tanpa pembanding tidak bermakna; accuracy pada kelas 90:10 hampir selalu menyesatkan. Cara menghindari: baseline mayoritas/rata-rata/heuristik selalu ada di samping baseline literatur; metrik yang peka pada ketidakseimbangan dipertimbangkan dan alasannya ditulis ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.9).
4. **Leakage lewat pra-pemrosesan dan split yang dibuat setelah melihat data.** Normalisasi/imputasi/seleksi fitur pada seluruh data sebelum split, duplikat lintas split, atau tuning pada data uji membuat hasil pilot "terlalu bagus". Cara menghindari: prosedur menyebut urutan *split dulu, lalu pra-pemrosesan pada train*; daftar sumber leakage dan pencegahannya ada di §Metrics & Evaluation; label-shuffle sanity check direncanakan sejak sekarang untuk W10.
5. **Data plan "dari Kaggle" — dan data mentah ikut ter-commit.** Tanpa lisensi, ukuran, representativitas, dan rencana cadangan, data plan gagal review; data pribadi di riwayat git adalah pelanggaran integritas yang butuh penulisan ulang riwayat ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5). Cara menghindari: kartu dataset diisi lengkap sebelum data disentuh; `.gitignore` untuk `data/raw/` dipasang hari ini; kelas privasi ditetapkan sebelum satu pun sampel dibuka di notebook.
6. **Menulis kode eksperimen minggu ini karena "desain sudah jelas".** Blocking rule B5 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md)): kode baseline/evaluasi menunggu metrik terkunci, pilot menunggu PR G5 merge. Cara menghindari: energi lebih dipakai untuk threats v0 dan red team AI, bukan `src/`; kalau tetap ingin menyiapkan sesuatu, cukup `requirements.txt` kosong dan struktur folder dari TPL-15.
