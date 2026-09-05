# AI Research Protocol — Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own

> **ID** AIX-04 · **Paket** 05 AI-Augmented Research & Meta-Thinking · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Semua yang memakai AI dalam riset di UAI: mahasiswa Metopen & TA, dosen, mentor, reviewer; wajib dibaca sebelum G1
> **Terkait** [AIX-02 AI Research Competency](02-ai-research-competency-framework.md) · [AIX-03 AI Across Value Stream](03-ai-across-research-value-stream.md) · [AIX-05 AI Tools Reference](05-ai-tools-reference.md) · [MET-07 Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md) · [TPL-11 Research Integrity Checklist](../08-templates/11-research-integrity-checklist.md) · [SECURITY.md](../../SECURITY.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)

## 1. Satu aturan universal

> **AI-augmented, human-accountable science.** AI adalah research copilot, bukan epistemic authority. Setiap output AI yang memengaruhi kesimpulan melewati *source verification → reasoning verification → evidence verification → human accountability*.

Protokol ini menjabarkan aturan itu menjadi delapan langkah yang berlaku untuk **setiap** penggunaan AI yang material dalam riset — dari mencari kata kunci sampai menyunting manuscript:

```
Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own
```

Semangatnya selaras dengan kebijakan publikasi ACM 2026 sebagaimana dirangkum dalam dokumen diskusi: penggunaan AI untuk *membantu penulisan* dibedakan dari AI *di dalam proses penelitian*; bila AI dipakai untuk research design, pemilihan data, eksperimen, coding, simulasi, analisis, testing, validasi, atau pembuatan artefak yang memengaruhi kesimpulan, penggunaannya dijelaskan dalam metode, dan peneliti tetap bertanggung jawab atas hasilnya. *(Verifikasi teks kebijakan terkini sebelum dikutip dalam naskah atau dokumen formal.)*

Kelas ini **bukan** *AI-free Research Methods* — itu tidak realistis. Tetapi juga **bukan** "pakai ChatGPT bikin proposal". Kita tidak mendidik orang yang pandai menghasilkan tulisan akademik; kita mendidik orang yang **sulit dibohongi, termasuk oleh AI-nya sendiri**.

## 2. Delapan langkah

### 2.1 Think — berpikir dulu sebelum bertanya

**Apa.** Sebelum membuka AI, tulis apa yang Anda coba capai, apa yang sudah Anda ketahui, dan apa jawaban yang Anda duga.
**Mengapa.** Tanpa ini, AI mengisi kekosongan dengan jawaban yang terdengar benar dan Anda tidak punya pembanding untuk menilainya. Berpikir dulu menjaga kepemilikan masalah dan memberi Anda alat untuk mendeteksi kesalahan AI.
**Cara praktis.** Tulis 2–3 baris di log sebelum prompt: tujuan, yang diketahui, dugaan. Untuk hal yang bisa dikerjakan sendiri dalam 10 menit (membuka DOI, menghitung rata-rata), kerjakan sendiri.
**Contoh.** Log: "Tujuan: cari baseline standar untuk klasifikasi teks pendek berbahasa Indonesia. Diketahui: TF-IDF + logistic regression lazim; matriks kami baris 3 & 7 memakainya. Dugaan: AI akan menyarankan model transformer; kami butuh baseline *sederhana* dulu."
**Pelanggaran umum.** Membuka AI sebagai langkah pertama untuk setiap pertanyaan; tidak punya dugaan sehingga menerima apa pun.

### 2.2 Ask — bertanya dengan konteks dan batas

**Apa.** Beri AI konteks riset (masalah, data, batasan, artefak terkait) dan minta jenis jawaban yang spesifik (alternatif, kritik, penjelasan), bukan "jawaban final".
**Mengapa.** Kualitas output bergantung pada konteks; tanpa batas, AI mengisi dengan asumsi generik. Meminta *alternatif/kritik* alih-alih *jawaban* menjaga peran AI sebagai copilot.
**Cara praktis.** Tempel Experiment Card/ringkasan matriks (bukan data mentah); nyatakan peran ("bertindak sebagai reviewer skeptis"); minta format yang bisa diverifikasi ("sebutkan sumber yang bisa saya buka" / "sebutkan asumsi").
**Contoh.** Prompt: "Konteks: RQ kami 'apakah fitur aktivitas LMS 4 minggu pertama memprediksi risiko drop-out lebih baik dari IPK semester 1?' Data: 412 mahasiswa, label biner 9% positif. Bertindaklah sebagai reviewer skeptis: sebutkan 8 ancaman validitas, urutkan, dan untuk tiap ancaman usulkan satu pengecekan konkret. Jangan menyarankan model; fokus pada desain." Respons ilustratif: daftar berisi *class imbalance & pilihan metrik*, *leakage dari fitur pasca-minggu-4*, *survivorship (mahasiswa yang sudah cuti)*, *label drift antar angkatan*, dst.
**Pelanggaran umum.** Prompt satu kalimat; memasukkan data pribadi/partner ke prompt; meminta "buatkan bab 2".

### 2.3 Ground — menjangkarkan ke sumber dan artefak

**Apa.** Setiap klaim faktual dari AI harus dijangkarkan ke sumber yang bisa dibuka (paper, dokumentasi, data Anda), dan setiap saran dijangkarkan ke artefak riset Anda (matriks, design card, log eksperimen).
**Mengapa.** AI menghasilkan teks yang plausibel, bukan teks yang benar; tanpa jangkar, Anda tidak bisa membedakan keduanya.
**Cara praktis.** Minta AI menyebut sumber, lalu **buka** sumber itu; bila tidak ada, klaim dibuang. Untuk saran metodologis, tanyakan "baris matriks mana / paper mana yang memakai ini?" dan cek.
**Contoh.** AI menyebut "studi X (2022) menunjukkan aktivitas LMS minggu pertama memprediksi drop-out dengan AUC 0,81". Tindakan: cari judul di Semantic Scholar/Scholar; jika tidak ditemukan → catat "tidak terverifikasi, dibuang"; jika ditemukan → baca bagian hasil, cocokkan angkanya, masukkan ke matriks dengan rujukan halaman.
**Pelanggaran umum.** Menyalin sitasi dari AI; menerima "menurut literatur" tanpa sumber; menjangkarkan ke ringkasan AI, bukan ke paper.

### 2.4 Verify — memverifikasi sumber, penalaran, bukti

**Apa.** Tiga lapis: (1) *source* — ada dan mengatakan itu; (2) *reasoning* — logikanya valid untuk konteks Anda (asumsi uji, kecocokan metode dengan RQ); (3) *evidence* — bukti Anda sendiri mendukungnya (hitung ulang, jalankan ulang).
**Mengapa.** Kesalahan AI terjadi di ketiga lapis: sumber palsu, penalaran yang benar secara umum tetapi salah di konteks Anda, dan angka yang "dihitung" tanpa data.
**Cara praktis.** Kolom *Verification* di AI Usage Log wajib diisi sebelum output dipakai; angka apa pun dari AI dihitung ulang dengan skrip; kode AI dijalankan dengan tes/sanity check; penjelasan statistik dicek asumsinya terhadap data Anda.
**Contoh.** AI menyarankan uji-t berpasangan untuk membandingkan F1 dua model antar 5 fold. Verifikasi penalaran: apakah fold berpasangan? ya. Apakah 5 pengamatan cukup dan distribusinya wajar? diragukan → laporkan mean ± SD dan interval, uji hanya sebagai pelengkap dengan catatan. Verifikasi bukti: hitung dengan `src/analysis.py` (fungsi `compare`), bukan dengan angka yang AI "perkirakan".
**Pelanggaran umum.** Log tanpa kolom verifikasi; "sudah saya cek" tanpa jejak; memverifikasi sumber tetapi tidak penalaran.

### 2.5 Challenge — menantang output dan diri sendiri

**Apa.** Minta AI mencari kelemahan jawabannya sendiri dan kelemahan riset Anda; lalu tantang AI dengan bukti Anda.
**Mengapa.** AI cenderung menyetujui arah pertanyaan (sycophancy). Bila Anda bertanya "apakah desain saya kuat?", ia akan bilang kuat. Bila Anda bertanya "bagaimana desain saya gagal?", ia berguna.
**Cara praktis.** Selalu tambahkan pertanyaan kedua: "apa yang salah dari jawabanmu?"; gunakan AI sebagai red team sebelum W8; catat kritik yang **ditolak** beserta alasannya — entri "ditolak" adalah bukti bahwa Anda menilai, bukan menyalin.
**Contoh.** Setelah AI menyarankan oversampling SMOTE: "Sebutkan 3 cara SMOTE bisa merusak validitas pada data kami (fitur diskrit, n kecil, split sudah ditentukan)." Respons ilustratif menyebut risiko leakage bila oversampling sebelum split dan sampel sintetis tidak realistis untuk fitur diskrit. Keputusan tim: oversampling hanya pada train fold, dibandingkan dengan class weighting; dicatat di Experiment Card.
**Pelanggaran umum.** Hanya bertanya untuk konfirmasi; tidak pernah ada entri "ditolak"; menganggap jawaban lancar = benar.

### 2.6 Reproduce — memastikan hasil bisa diulang tanpa AI

**Apa.** Apa pun yang AI bantu hasilkan (kode, analisis, tabel) harus dapat dijalankan ulang dari repositori oleh orang lain tanpa percakapan AI tersebut.
**Mengapa.** Percakapan AI bukan artefak ilmiah; repositori adalah artefak ilmiah. Hasil yang hanya "pernah muncul di chat" tidak ada.
**Cara praktis.** Kode AI masuk `src/` dengan atribusi di log dan tes; angka masuk `results/` lewat skrip; peer mereproduksi baseline (G6). Untuk analisis: skrip menghasilkan tabel manuscript.
**Contoh.** AI membantu menulis fungsi pembagian data stratified. Tim menambah tes: proporsi label per split ± 1%, tidak ada ID yang muncul di dua split; menjalankan `run.sh`; peer dari tim lain mereproduksi angka baseline dan menulis catatan di `experiments/README.md`.
**Pelanggaran umum.** Hasil dari notebook yang tidak bisa dijalankan ulang; kode AI tanpa tes; "tabel dibuat AI dari log" tanpa skrip.

### 2.7 Disclose — mengungkap secara spesifik

**Apa.** Mencatat penggunaan AI yang material di AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)) saat terjadi, dan merangkumnya di `docs/AI-USAGE.md` (AI Usage Statement; versi final untuk naskah di `paper/AI-USAGE-STATEMENT.md`) dengan membedakan bantuan **penulisan** dan bantuan **proses riset**.
**Mengapa.** Pengungkapan membuat riset dapat diaudit, memenuhi kebijakan venue, dan melindungi Anda: yang diungkap adalah praktik; yang disembunyikan adalah pelanggaran.
**Cara praktis.** Log hanya untuk penggunaan material (yang memengaruhi artefak/kesimpulan), bukan setiap pertanyaan istilah; entri ditulis saat itu juga; statement diperbarui tiap gate.
**Contoh.** Entri log (kolom TPL-10): `#07 · 2026-10-14 · [tool kategori: coding assistant, versi] · Coding · implementasi stratified split · prompt: deskripsi skema (tanpa data) · material output: Ya — fungsi split_stratified() · verifikasi: E — tes proporsi & ID unik lulus (commit a1b2c3) · inclusion: Diubah (seed handling) — src/data.py · PJ: [nama]`.
**Pelanggaran umum.** Log diisi belakangan dari ingatan; statement generik ("kami menggunakan ChatGPT untuk membantu"); AI pada kode/analisis tidak dicatat karena "cuma bantu".

### 2.8 Own — memikul tanggung jawab penuh

**Apa.** Anda bertanggung jawab atas setiap kalimat, angka, dan baris kode dalam riset Anda, apa pun asal-usulnya. "AI yang bilang" bukan pembelaan.
**Mengapa.** Kredibilitas ilmiah melekat pada manusia yang menandatangani; inilah inti amanah epistemik dan alasan AI tidak dapat menjadi penulis.
**Cara praktis.** Uji diri: bisakah Anda menjelaskan bagian ini tanpa membuka AI? Bila tidak, Anda belum memilikinya — pelajari atau buang. Di defense, setiap anggota siap menjelaskan bagian berbantuan AI. TPL-11 ditandatangani dengan pemahaman ini.
**Contoh.** Penguji: "Mengapa memakai F1 kelas minoritas, bukan AUC?" Jawaban yang menunjukkan kepemilikan: "Stakeholder bertindak pada daftar mahasiswa berisiko; yang penting presisi dan recall pada kelas positif pada ambang yang dipakai; AUC tidak menggambarkan itu. Kami mempertimbangkan AUC setelah AI menyarankannya dan melaporkannya sebagai metrik sekunder — lihat tabel 3."
**Pelanggaran umum.** Tidak bisa menjelaskan kode/analisis sendiri; menyalahkan tool; menyerahkan teks yang tidak dipahami.

## 3. Yang diizinkan dan yang dilarang

| Diizinkan (dengan protokol di atas) | Dilarang |
|---|---|
| Eksplorasi terminologi dan konsep bidang | Mengarang atau menyalin referensi dari AI tanpa membuka sumbernya |
| Kandidat keyword/sinonim/string pencarian; tool literature search & deep research untuk **menemukan** | Menulis hasil, tabel, atau angka yang tidak berasal dari run/data tim |
| Pra-baca dan penjelasan paper yang Anda unggah (sesuai lisensi) | Memasukkan data pribadi, data partner, data RESTRICTED, kredensial, atau draft orang lain ke layanan AI |
| Brainstorming hipotesis alternatif dan hipotesis saingan | Menyerahkan teks/kode AI tanpa verifikasi dan tanpa mampu menjelaskannya |
| Kritik/red team desain eksperimen dan threats to validity | Membiarkan AI memilih metrik/baseline/hipotesis setelah melihat hasil (metric switching, HARKing) |
| Coding support, debugging, penjelasan error, penulisan tes | Meng-commit kode AI yang tidak dibaca/diuji |
| Penjelasan statistik dan saran analisis (dihitung ulang oleh tim) | Menggunakan AI untuk menulis review tim lain atau mengunggah draft tim lain |
| Bantuan analisis: kode plotting, pengecekan asumsi, error analysis | Menggunakan AI tanpa mencatatnya ketika penggunaan itu memengaruhi kesimpulan |
| Penyuntingan bahasa, struktur, konsistensi istilah pada draft tim | Menyebut AI sebagai penulis; menyembunyikan penggunaan AI dari venue/penguji |
| Latihan pitch/defense dengan AI sebagai penanya | Menjawab penguji/reviewer dengan hasil yang hanya ada di percakapan AI |

Rincian per tahap riset: [AIX-03](03-ai-across-research-value-stream.md). Kategori tool dan risikonya: [AIX-05](05-ai-tools-reference.md).

## 4. Format AI Usage Statement dan Log

### 4.1 AI Usage Log (per penggunaan material) — [TPL-10](../08-templates/10-ai-usage-log-template.md)

Kolom mengikuti TPL-10 persis agar log dapat diaudit lintas tim:

| Kolom | Isi |
|---|---|
| # | Nomor urut entri (dirujuk dari AI Usage Statement: "log #12–#15") |
| Date | Tanggal penggunaan (ditulis saat itu) |
| Tool (versi) | Kategori + nama tool/versi/model bila diketahui |
| Stage | Tahap riset (Problem · Search · Read · Synthesis · Gap · RQ · Method · Coding · Experiment · Analysis · Writing · Review · Publication) |
| Purpose | Tujuan spesifik |
| Prompt / use | Ringkasan prompt atau cara pakai; **tanpa** data sensitif |
| Material output? | Ya/Tidak — apa yang dihasilkan dan dianggap material |
| Verification | Source / reasoning / evidence — apa yang dicek, hasilnya, tautan commit/file |
| Inclusion in final work | Ya (dipakai utuh) / Diubah (dipakai dengan modifikasi) / Tidak (ditolak — tulis alasannya); lokasi file/section/commit |
| PJ | Penanggung jawab entri (manusia yang memverifikasi) |

Keputusan *dipakai / diubah / ditolak* dicatat di kolom **Inclusion in final work**; entri "Tidak (ditolak)" beserta alasannya adalah bukti bahwa tim menilai (§2.5).

### 4.2 AI Usage Statement (`docs/AI-USAGE.md`; versi final untuk naskah: `paper/AI-USAGE-STATEMENT.md`) — struktur

```
# AI Usage Statement — UIAI-YYYY-NNN

## 1. Ringkasan
Tool (kategori) yang dipakai; tahap riset yang dibantu; siapa yang bertanggung jawab.

## 2. AI dalam proses riset (memengaruhi metode/kesimpulan)
| Tahap | Bantuan AI | Verifikasi | Rujukan log |
Contoh: Method — red team desain — 4 ancaman diadopsi ke Threats v1 — log #12–#15.
Contoh: Coding — fungsi split & evaluasi — tes proporsi/ID lulus, peer reproduksi — log #21–#27.

## 3. AI dalam penulisan (bahasa/struktur)
Bagian mana; jenis bantuan; tidak ada sitasi atau hasil yang berasal dari AI.

## 4. Yang TIDAK dilakukan dengan AI
Hasil, tabel, figur, interpretasi, review untuk tim lain, pemilihan metrik/baseline.

## 5. Data
Tidak ada data mentah/pribadi/partner yang dimasukkan ke layanan AI (atau: pengecualian dan izinnya).

## 6. Pernyataan tanggung jawab
Semua penulis bertanggung jawab penuh atas isi; AI bukan penulis.
```

Statement ini menjadi sumber untuk bagian metode dan pengungkapan AI di proposal/manuscript ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)).

## 5. AI Research Protocol Agreement (ditandatangani di G1)

Teks berikut ditandatangani setiap mahasiswa (dan disalin ke `docs/ai-protocol-agreement.md` di repositori riset) sebagai syarat G1 Endgame Ready.

```
AI RESEARCH PROTOCOL AGREEMENT
UAI AI Research Center — Program Studi Informatika, Universitas Al-Azhar Indonesia

Saya, [nama], NIM [isi], anggota tim riset [Research ID / judul sementara],
menyatakan bahwa dalam seluruh kegiatan riset ini saya akan:

1. THINK   — berpikir dan menuliskan tujuan serta dugaan saya sebelum meminta bantuan AI.
2. ASK     — memberi konteks dan batas yang jelas, dan tidak memasukkan data pribadi,
             data partner, data RESTRICTED, kredensial, atau karya orang lain tanpa izin
             ke layanan AI mana pun.
3. GROUND  — menjangkarkan setiap klaim dari AI ke sumber yang saya buka sendiri dan ke
             artefak riset tim.
4. VERIFY  — memverifikasi sumber, penalaran, dan bukti dari setiap output AI yang
             memengaruhi kesimpulan, dan mencatat verifikasi itu.
5. CHALLENGE — menantang output AI dan riset saya sendiri, serta mencatat saran yang
             saya tolak beserta alasannya.
6. REPRODUCE — memastikan setiap hasil yang dibantu AI dapat dijalankan ulang dari
             repositori tanpa percakapan AI tersebut.
7. DISCLOSE — mencatat penggunaan AI yang material di AI Usage Log saat terjadi dan
             merangkumnya secara jujur di AI-USAGE.md, termasuk dalam bagian metode
             bila memengaruhi kesimpulan.
8. OWN     — bertanggung jawab penuh atas setiap kalimat, angka, dan baris kode dalam
             riset ini, dan mampu menjelaskannya tanpa AI.

Saya memahami bahwa:
- referensi, hasil, atau data yang berasal dari AI dan tidak diverifikasi diperlakukan
  sebagai fabrikasi;
- penggunaan AI yang memengaruhi kesimpulan dan tidak diungkap membuat gate gagal;
- pelanggaran ditangani sesuai MET-07, CODE_OF_CONDUCT.md, dan kebijakan akademik Prodi;
- AI adalah research copilot, bukan epistemic authority; amanah epistemik ada pada saya.

Tanda tangan: ____________________   Tanggal: __________
Dosen pengampu: __________________   Mentor: ___________
```

## 6. Bila protokol dilanggar

| Situasi | Penanganan |
|---|---|
| Kesalahan tidak disengaja terdeteksi sendiri dan dilaporkan (mis. referensi AI lolos ke `.bib`, lalu ditemukan tim) | Perbaiki, catat di log sebagai "ditemukan & dikoreksi"; tidak ada sanksi — ini perilaku Governor |
| Terdeteksi reviewer, tidak disengaja | Gate gagal untuk artefak itu; remediasi dalam satu sprint; catatan di PR |
| Berulang atau disengaja (referensi palsu, hasil AI, AI tidak diungkap) | Diperlakukan sebagai pelanggaran integritas ([MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md) §5) |
| Data sensitif masuk ke layanan AI | Ikuti [SECURITY.md](../../SECURITY.md) §5; laporkan ke dosen/pemilik data |

## 7. Kartu saku

```
Sebelum prompt : tujuan? yang diketahui? dugaan?                (Think)
Saat prompt    : konteks + batas + peran; tanpa data sensitif   (Ask)
Setelah output : sumber bisa dibuka? artefak mana?              (Ground)
               : sumber ✓ penalaran ✓ bukti ✓ — dicatat?        (Verify)
               : "apa yang salah dari jawabanmu?" — ada ditolak? (Challenge)
Sebelum commit : bisa dijalankan ulang tanpa chat?              (Reproduce)
Sebelum gate   : log & AI-USAGE.md mutakhir?                    (Disclose)
Sebelum defense: bisa saya jelaskan tanpa AI?                   (Own)
```
