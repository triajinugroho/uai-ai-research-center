# Research Integrity & Ethics — Amanah Epistemik dalam Riset Computing

> **ID** MET-07 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen pengampu, mentor, reviewer gate, pengelola datasets-registry, komite etik (bila ada)
> **Terkait** [MET-06 5E Rubric](06-assessment-and-5e-rubric.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md) · [TPL-11 Research Integrity Checklist](../08-templates/11-research-integrity-checklist.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · [SECURITY.md](../../SECURITY.md) · [LICENSING.md](../../LICENSING.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md)

## 1. Mengapa integritas adalah gate, bukan bab

Riset menghasilkan *credible knowledge*. Kata kuncinya *credible*: pengetahuan yang boleh dipercaya orang lain tanpa harus mengulang seluruh pekerjaan. Kredibilitas itu runtuh bukan hanya oleh kebohongan besar, tetapi oleh kebiasaan kecil: satu seed yang dipilih karena hasilnya bagus, satu metrik yang diganti setelah hasil terlihat, satu referensi yang "pasti ada" tetapi tidak pernah dibuka.

Karena itu di UAI integritas adalah **Research Integrity Gate** — lulus/gagal di setiap gate ([MET-06](06-assessment-and-5e-rubric.md) §4), bukan satu bab "etika penelitian" di akhir semester. Landasannya adalah **amanah epistemik**: peneliti memegang amanah untuk tidak mengarang data, memilih bukti yang menguntungkan saja, menutupi hasil negatif, mengubah metrik setelah melihat hasil, mengutip yang tidak dibaca, membiarkan AI mengarang referensi, mengklaim kausalitas dari korelasi, atau melebih-lebihkan kontribusi. Dalam bahasa riset modern: *research integrity*. Dalam bahasa keimanan: kejujuran terhadap kebenaran meskipun kebenaran itu meruntuhkan hipotesis sendiri.

Dokumen ini membahas sembilan topik dengan format tetap: **definisi → contoh pelanggaran dalam riset computing/ML → cara mencegah → cara mendeteksi → konsekuensi.**

## 2. Sembilan topik

### 2.1 Fabrication (fabrikasi)

| | |
|---|---|
| **Definisi** | Mengarang data, hasil, atau catatan yang tidak pernah ada. |
| **Contoh di computing/ML** | Menulis angka akurasi di tabel tanpa run yang menghasilkannya; mengisi baris synthesis matrix dari "ingatan" atau ringkasan AI tanpa membaca paper; mengarang jumlah responden survei; membuat log eksperimen setelah deadline dari perkiraan; menampilkan figur "ilustratif" sebagai hasil. |
| **Cara mencegah** | Setiap angka di `results/` berasal dari run yang tercatat (config + seed + log); tabel di manuscript dihasilkan skrip dari `results/`, bukan diketik manual; baris matriks berisi rujukan halaman/tabel paper. |
| **Cara mendeteksi** | Reviewer meminta run ulang satu angka acak; membandingkan tabel manuscript dengan `results/`; spot-check baris matriks terhadap PDF; memeriksa timestamp commit vs klaim jadwal. |
| **Konsekuensi** | Gate gagal; pelanggaran kode etik berat; nilai E untuk pelanggar; artefak dicabut dari registry bila sudah dirilis. |

### 2.2 Falsification (falsifikasi)

| | |
|---|---|
| **Definisi** | Memanipulasi data, prosedur, atau hasil sehingga penelitian tidak lagi merepresentasikan apa yang sebenarnya terjadi. |
| **Contoh di computing/ML** | **Leakage yang disembunyikan** (fitur target bocor ke train, split dibuat setelah normalisasi/oversampling seluruh data) dan tetap dilaporkan sebagai hasil valid; **metric switching** — mengganti metrik utama setelah melihat mana yang bagus tanpa mengungkapkannya; **seed cherry-picking** — menjalankan 20 seed dan melaporkan satu yang terbaik seolah hasil tunggal; membuang data uji yang "aneh" agar hasil rapi; tuning hyperparameter pada test set; mengubah hipotesis setelah hasil (HARKing) tanpa pengungkapan; memotong sumbu figur agar perbedaan tampak besar. |
| **Cara mencegah** | Baseline dan metrik ditetapkan di G5 sebelum eksperimen (pre-registration ringan lewat Experiment Card); split disimpan sebagai file/seed dan dibuat sebelum pra-pemrosesan; semua seed dilaporkan dengan mean ± deviasi; sanity check "hasil terlalu bagus"; perubahan metrik/hipotesis dicatat sebagai *deviation* di `results/analysis.md`. |
| **Cara mendeteksi** | Bandingkan metrik di Experiment Card (G5) dengan metrik di analisis (G7); periksa urutan split vs pra-pemrosesan dalam kode; hitung ulang dari log semua seed; periksa apakah test set pernah dipakai untuk memilih model. |
| **Konsekuensi** | Gate G6/G7 gagal; klaim harus ditarik; pelanggaran disengaja = pelanggaran kode etik berat. |

### 2.3 Plagiarism (plagiarisme)

| | |
|---|---|
| **Definisi** | Mengambil gagasan, teks, kode, data, atau figur orang lain tanpa atribusi yang benar, termasuk *self-plagiarism* (memakai ulang karya sendiri tanpa pengungkapan). |
| **Contoh di computing/ML** | Menyalin paragraf related work dari paper lain dengan mengganti beberapa kata; menyalin kode repositori orang lain tanpa lisensi/atribusi; memakai figur arsitektur dari paper lain tanpa izin/sitasi; mengirim proposal Metopen yang sama sebagai laporan mata kuliah lain tanpa pengungkapan; menyerahkan teks AI yang meniru sumber tertentu. |
| **Cara mencegah** | Menulis dari synthesis matrix dengan kata sendiri; mengutip langsung dengan tanda kutip dan halaman; setiap kode pihak ketiga disertai lisensi dan atribusi di README/header; figur pihak ketiga hanya bila lisensi mengizinkan; pengungkapan reuse karya sendiri. |
| **Cara mendeteksi** | Pemeriksa kemiripan teks (bila tersedia di Prodi); pencarian frasa; pemeriksaan lisensi kode; reviewer membandingkan related work dengan sumber yang dikutip. |
| **Konsekuensi** | Sesuai kebijakan akademik Prodi (`[isi]`); gate gagal; plagiarisme berat = kode etik berat. |

### 2.4 Citation integrity (integritas sitasi)

| | |
|---|---|
| **Definisi** | Setiap sitasi harus merujuk sumber yang benar-benar ada, benar-benar dibaca, dan benar-benar mengatakan apa yang dikutip. |
| **Contoh di computing/ML** | Referensi buatan AI (judul dan penulis masuk akal, DOI tidak ada); mengutip abstrak untuk klaim yang tidak ada di badan paper; mengutip paper tanpa membacanya karena "semua orang mengutip itu"; mengubah makna klaim sumber; sitasi ke blog untuk klaim empiris; menambah sitasi agar daftar pustaka panjang. |
| **Cara mencegah** | Semua sumber masuk `references.bib` hanya setelah DOI/URL dibuka; catatan "dibaca oleh siapa, bagian mana" di matriks; sumber dari AI wajib diverifikasi dan dicatat di AI Usage Log; sitasi hanya untuk klaim yang bisa ditunjuk halamannya. |
| **Cara mendeteksi** | Reviewer membuka 3–5 DOI acak; mencocokkan klaim di teks dengan bagian paper; mengecek apakah setiap entri `.bib` muncul di matriks. |
| **Konsekuensi** | **Satu** referensi yang tidak dapat diverifikasi keberadaannya = G3 gagal (OPS-03); referensi buatan AI yang lolos ke proposal = pelanggaran integritas. |

### 2.5 Dataset & privacy (data dan privasi)

| | |
|---|---|
| **Definisi** | Data dikumpulkan, disimpan, dipakai, dan dibagikan sesuai hak pemilik, persetujuan subjek, lisensi, dan klasifikasi keamanan ([SECURITY.md](../../SECURITY.md)). |
| **Contoh di computing/ML** | Meng-commit data mahasiswa (NIM, nilai) ke GitHub; memakai dataset Kaggle dengan lisensi yang melarang penggunaan tertentu; scraping data pribadi tanpa dasar; memasukkan data pasien/pengguna ke layanan AI eksternal lewat prompt; menerbitkan model yang dilatih pada data partner tanpa izin; membagikan dataset "anonim" yang masih bisa di-reidentifikasi. |
| **Cara mencegah** | Data plan (G5) menyebut sumber, lisensi, privasi, consent; data mentah sensitif di luar git (`.gitignore`, server institusi); kartu dataset dengan field License & Privacy diisi sebelum G5; anonimisasi/pseudonimisasi sebelum analisis, kunci pemetaan di luar repositori; prompt AI tidak memuat data pribadi/partner; lisensi output diputuskan lewat review ([LICENSING.md](../../LICENSING.md)). |
| **Cara mendeteksi** | Pemeriksaan riwayat git untuk file data/kredensial; review kartu dataset; pertanyaan reviewer "dari mana consent-nya?"; audit prompt di AI Usage Log. |
| **Konsekuensi** | Gate gagal; kebocoran ditangani sesuai SECURITY.md §5 (tulis ulang riwayat, rotasi kredensial, laporan ke pemilik data); pelanggaran berat = kode etik. |

### 2.6 Bias (bias dan keadilan)

| | |
|---|---|
| **Definisi** | Kecenderungan sistematis dalam data, desain, analisis, atau interpretasi yang membuat hasil menyimpang dari kebenaran atau merugikan kelompok tertentu. |
| **Contoh di computing/ML** | Data latih hanya dari satu kampus/kelompok lalu diklaim berlaku umum; label dibuat satu annotator tanpa pengukuran kesepakatan; confirmation bias — hanya mencari literatur yang mendukung; survivorship bias pada data yang tersisa; model yang akurasinya tinggi secara agregat tetapi buruk untuk subkelompok, tanpa dilaporkan; memilih baseline yang sengaja lemah. |
| **Cara mencegah** | Representativitas dibahas di Data Plan; evaluasi per subkelompok bila relevan; kriteria inklusi literatur ditetapkan sebelum pencarian; baseline yang masuk akal; threats to validity eksternal/konstruk ditulis jujur; red team W8 mencari bias. |
| **Cara mendeteksi** | Reviewer memeriksa populasi vs sampel; meminta metrik per subkelompok; membandingkan strategi pencarian dengan hasil matriks. |
| **Konsekuensi** | Bias yang tidak diungkap = klaim melebihi bukti → G7 gagal; bias yang diungkap dengan mitigasi = riset yang jujur. |

### 2.7 Reproducibility (reproduksibilitas)

| | |
|---|---|
| **Definisi** | Orang lain dapat menjalankan ulang pekerjaan dengan kode, konfigurasi, seed, environment, langkah, dan data/metadata yang disediakan, dan mendapatkan hasil yang konsisten. |
| **Contoh pelanggaran** | Hasil hanya ada di laptop; dependensi tidak dipin; notebook dijalankan tidak berurutan; seed tidak dicatat; pra-pemrosesan manual di spreadsheet tanpa skrip; "kode akan tersedia" tetapi tidak pernah; hasil manuscript berbeda dari yang dihasilkan repositori. |
| **Cara mencegah** | Reproducibility package minimum sejak W9; `run.sh`/Makefile; `requirements.txt`/`environment.yml`; seed tetap; skrip menghasilkan tabel/figur; peer reproduction sebagai syarat G6. |
| **Cara mendeteksi** | Peer/mentor menjalankan `run.sh` di mesin lain (G6); reproducibility check T−4 sebelum submit ([MET-05](05-publication-backward-design.md)). |
| **Konsekuensi** | G6 gagal bila peer tidak bisa mereproduksi baseline; bukan pelanggaran etik kecuali disertai klaim palsu ("telah direproduksi" padahal tidak). |

### 2.8 AI usage (penggunaan AI)

| | |
|---|---|
| **Definisi** | AI adalah *research copilot*, bukan *epistemic authority*: setiap output AI melewati verifikasi sumber, penalaran, dan bukti, diungkap, dan menjadi tanggung jawab manusia ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)). |
| **Contoh pelanggaran** | Referensi buatan AI; hasil/tabel "diperkirakan" AI; bagian hasil/diskusi ditulis AI tanpa verifikasi terhadap data; kode AI di-commit tanpa dibaca/diuji lalu menghasilkan leakage; AI dipakai memilih metrik setelah hasil; data pribadi dimasukkan ke prompt; penggunaan AI yang memengaruhi kesimpulan tidak diungkap; AI Usage Log diisi dari ingatan. |
| **Cara mencegah** | Protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own; AI Usage Log kontemporer ([TPL-10](../08-templates/10-ai-usage-log-template.md)); AI Usage Statement membedakan bantuan penulisan dan bantuan proses riset; daftar izin/larangan AIX-04. |
| **Cara mendeteksi** | Reviewer membandingkan log dengan artefak (kode, teks, referensi); meminta mahasiswa menjelaskan bagian yang dibantu AI; verifikasi sumber; pola teks yang tidak konsisten dengan repositori. |
| **Konsekuensi** | AI tidak diungkap padahal memengaruhi kesimpulan = gate gagal; referensi/hasil buatan AI = fabrikasi. |

### 2.9 Amanah epistemik (integritas sebagai worldview)

| | |
|---|---|
| **Definisi** | Sikap dasar peneliti: mencari apa yang benar berdasarkan bukti, bukan membela hipotesis; bersedia dibuktikan salah; melaporkan apa adanya. |
| **Contoh pelanggaran** | Menutupi hasil negatif; mengubah kontribusi agar terdengar "novel"; menolak kritik red team tanpa alasan; menekan anggota tim/peer untuk "membuat hasil terlihat bagus"; menulis "penelitian ini tidak memiliki keterbatasan". |
| **Cara mencegah** | Hasil negatif dinilai sama dengan hasil positif di rubrik ([MET-06](06-assessment-and-5e-rubric.md)); threats to validity wajib; red team dan peer review sebagai budaya; kontribusi direvisi turun bila bukti lemah; dosen memodelkan sikap "saya tidak tahu" dan "saya keliru". |
| **Cara mendeteksi** | Perbandingan klaim G4 vs G7 (apakah direvisi jujur); keberadaan hasil negatif di `results/`; cara tim menanggapi review. |
| **Konsekuensi** | Tidak ada sanksi formal untuk "kurang rendah hati", tetapi klaim yang melebihi bukti membuat G7/G8 gagal; tekanan terhadap reviewer/peer = pelanggaran kode etik. |

## 3. Kebijakan AI dalam riset

Kebijakan AI UAI mengikuti **semangat kebijakan ACM 2026** sebagaimana dirangkum dalam dokumen diskusi (verifikasi teks kebijakan terkini sebelum dikutip dalam dokumen formal atau naskah):

1. **Dua jenis penggunaan dibedakan.** (a) AI untuk membantu **penulisan** (bahasa, struktur, penyuntingan) dan (b) AI di dalam **proses penelitian** (research design, pemilihan data, eksperimen, coding, simulasi, analisis, testing, validasi, pembuatan artefak).
2. **Penggunaan jenis (b) yang memengaruhi kesimpulan wajib dijelaskan dalam bagian metode** — bukan hanya di acknowledgment — termasuk tool, tujuan, dan cara verifikasinya.
3. **Peneliti tetap bertanggung jawab penuh** atas semua hasil, termasuk yang dihasilkan dengan bantuan AI. AI tidak menjadi penulis dan tidak dapat "disalahkan".
4. **Data sensitif tidak masuk ke layanan AI eksternal** ([SECURITY.md](../../SECURITY.md) §4).
5. **Venue menentukan format pengungkapan**; `AI-USAGE.md` adalah sumber untuk mengisinya.

Operasionalisasi (daftar yang diizinkan/dilarang, format statement dan log, agreement yang ditandatangani di G1) ada di [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md) dan [TPL-10](../08-templates/10-ai-usage-log-template.md).

## 4. Human subjects dan persetujuan

Riset yang melibatkan manusia — survei, wawancara, user study, data perilaku pengguna, data mahasiswa, data kesehatan — memerlukan:

| Ketentuan | Minimum di Metopen/TA |
|---|---|
| Penilaian risiko | `docs/ethics.md` menjelaskan siapa subjeknya, risiko (privasi, waktu, psikologis), dan mitigasi |
| Persetujuan (informed consent) | Penjelasan tujuan, apa yang dikumpulkan, cara penyimpanan, hak menolak/mundur tanpa konsekuensi, kontak peneliti; consent tercatat (form/tangkapan layar/log) dan disimpan **di luar** repositori publik |
| Izin institusi / komite etik | Bila Prodi/Universitas memiliki komite etik atau prosedur izin (`[isi]`), izin diperoleh sebelum pengumpulan data; bila tidak ada, dosen pembimbing menyetujui tertulis di `docs/ethics.md` |
| Kelompok rentan & data sensitif | Anak-anak, pasien, data kesehatan/keuangan/keagamaan memerlukan pertimbangan tambahan dan tidak boleh dikumpulkan tanpa izin formal |
| Data mahasiswa UAI | Sering menjadi sumber data termudah — dan paling berisiko; perlu izin unit pemilik data, anonimisasi, dan pernyataan tujuan yang jelas; tidak boleh ada tekanan akademik untuk berpartisipasi |
| Anonimisasi | Sebelum analisis; kunci pemetaan di luar repositori; laporan tidak memuat data yang bisa mengidentifikasi orang |
| Penyimpanan & masa simpan | Ditulis di kartu dataset; dihapus/diarsipkan sesuai perjanjian |
| Pelaporan | Bagian Ethics di proposal/manuscript merangkum semua hal di atas |

Nilai privasi pada kartu dataset (`Public / Restricted / Confidential`) harus terisi **sebelum G5 Method Ready**.

## 5. Prosedur penanganan dugaan pelanggaran

| Langkah | Siapa | Apa |
|---|---|---|
| 1 Deteksi | Reviewer/peer/dosen/mahasiswa | Menandai dugaan di PR gate (komentar privat bila sensitif) atau melapor ke dosen pengampu; tidak menuduh di forum terbuka |
| 2 Klarifikasi | Dosen pengampu + tim | Tim diminta menunjukkan bukti (log, run, sumber); banyak kasus adalah kesalahan tidak disengaja |
| 3 Klasifikasi | Dosen pengampu (+ mentor) | **Ringan** (sitasi keliru, log kurang, README tidak lengkap) → perbaiki dalam satu sprint, dicatat. **Sedang** (metric switching tanpa pengungkapan, data sensitif ter-commit tanpa niat buruk) → gate gagal, remediasi, catatan resmi. **Berat** (fabrikasi, falsifikasi disengaja, plagiarisme berat, referensi AI disengaja, tekanan pada reviewer) → kode etik |
| 4 Keputusan | Dosen pengampu; kasus berat ke Kaprodi/komisi Prodi (`[isi]`) | Sesuai [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) dan kebijakan akademik |
| 5 Pencatatan | Dosen pengampu | Catatan di Issue privat `type:research-risk`; artefak yang tercemar diperbaiki/ditarik; registry diperbarui bila sudah dirilis |
| 6 Pembelajaran | Semua | Kasus (dianonimkan) menjadi bahan studio berikutnya |

Prinsip: **niat dan pengungkapan** membedakan kesalahan dari pelanggaran. Tim yang menemukan leakage sendiri dan melaporkannya sedang melakukan riset yang baik.

## 6. Sebelum setiap gate: pertanyaan integritas

| Gate | Pertanyaan yang harus dijawab "ya" dengan bukti |
|---|---|
| G1 | Agreement AI Research Protocol ditandatangani? AI Usage Log dimulai? |
| G2 | Statistik/klaim masalah punya sumber yang bisa dibuka? |
| G3 | Semua referensi terverifikasi ada dan dibaca? Sumber dari AI dicatat? |
| G4 | RQ tidak diubah diam-diam dari gap? |
| G5 | Metrik & baseline ditetapkan sebelum eksperimen? Data plan: lisensi, privasi, consent? Tidak ada data sensitif di git? |
| G6 | Semua seed/run dicatat? Split dibuat sebelum pra-pemrosesan? Kode AI dibaca & diuji? |
| G7 | Semua run dilaporkan (bukan yang terbaik)? Hasil negatif ada? Klaim tidak kausal dari korelasi? Perubahan metrik/hipotesis diungkap? |
| G8 | TPL-11 ditandatangani? `AI-USAGE.md` konsisten dengan naskah? Semua sitasi di `references.bib`? Tidak ada plagiarisme/self-plagiarism? |

Checklist lengkap: [TPL-11](../08-templates/11-research-integrity-checklist.md). Log AI: [TPL-10](../08-templates/10-ai-usage-log-template.md). Kebijakan data: [SECURITY.md](../../SECURITY.md). Kode etik komunitas: [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md).

## 7. Satu kalimat

Orientasi peneliti UAI bukan "bagaimana penelitian saya terlihat bagus?", melainkan **"apa yang sebenarnya benar berdasarkan bukti yang Allah izinkan saya temukan?"** — dan setiap gate adalah kesempatan membuktikan bahwa kalimat itu bukan slogan.
