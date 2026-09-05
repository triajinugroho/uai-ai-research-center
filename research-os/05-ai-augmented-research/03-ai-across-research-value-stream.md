# AI Across the Research Value Stream — Peran AI di Tiga Belas Tahap Riset

> **ID** AIX-03 · **Paket** 05 AI-Augmented Research & Meta-Thinking · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen pengampu/mentor, reviewer gate, dosen mata kuliah mode E/R
> **Terkait** [AIX-01 Meta-Thinking](01-research-meta-thinking.md) · [AIX-02 AI Research Competency](02-ai-research-competency-framework.md) · [AIX-04 AI Research Protocol](04-ai-research-protocol.md) · [AIX-05 AI Tools Reference](05-ai-tools-reference.md) · [MET-03 16-Week Blueprint](../04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md)

## 1. Prinsip

1. **AI as copilot, not epistemic authority.** AI mempercepat pencarian, penulisan kode, kritik, dan penjelasan; AI **tidak** menentukan apa yang benar. Kebenaran ditentukan oleh sumber yang bisa dibuka, penalaran yang bisa diikuti, dan bukti yang bisa direproduksi.
2. **Rantai verifikasi universal:** setiap output AI yang memengaruhi kesimpulan melewati **source verification → reasoning verification → evidence verification → human accountability** ([AIX-04](04-ai-research-protocol.md)).
3. **Peran AI berbeda per tahap.** Di tahap *Search* AI sangat membantu dan risikonya terkendali (verifikasi DOI); di tahap *Analysis* AI berguna untuk menjelaskan tetapi berbahaya untuk "menghitung"; di tahap *Writing* AI boleh menyunting bahasa tetapi tidak boleh menulis hasil.
4. **Manusia memegang tugas yang menentukan.** Kolom *Human Task* di tabel adalah pekerjaan yang tidak boleh didelegasikan; kolom *AI Role* adalah bantuan yang boleh diterima dengan verifikasi di kolom *Verification*.

Kategori tool dijelaskan di [AIX-05](05-ai-tools-reference.md); meta-skill di [AIX-01](01-research-meta-thinking.md); artefak di [MET-04](../04-metopen-research-studio/04-research-pack-specification.md).

## 2. Tabel besar: tiga belas tahap

| Stage | Human Task | Meta Skill | AI Role | Tools (kategori — contoh, bisa berubah) | Verification | Artifact |
|---|---|---|---|---|---|---|
| **1 Problem** (W1–W2, G1–G2) | Memilih masalah yang layak; bicara dengan stakeholder; menulis problem-first; menetapkan endgame | Problem framing, Systems thinking | Mengusulkan reframing alternatif; menantang solution-first; memetakan stakeholder kandidat; menjelaskan istilah domain | General reasoning (chat assistant umum) | Stakeholder nyata/dosen pemilik masalah mengonfirmasi; setiap klaim masalah punya sumber yang bisa dibuka; framing ditulis ulang oleh tim | `docs/endgame.md`, Problem Brief, Stakeholder/Impact |
| **2 Search** (W3, G3) | Menyusun strategi pencarian; memilih basis data; screening; memutuskan inklusi/eksklusi | Evidence literacy, Decomposition | Kandidat kata kunci/sinonim; string pencarian; menemukan kandidat paper; citation chaining terbantu | Literature search (Google Scholar, Semantic Scholar, Scopus, OpenAlex); Deep research (mode riset pada asisten umum); Citation intelligence (peta sitasi) | **Setiap** sumber dibuka: DOI/URL ada, judul-penulis-tahun cocok; sumber temuan AI ditandai di log | `docs/literature/search-strategy.md`, `docs/literature/search-log.csv`, `docs/literature/screening.csv` (kandidat), `references.bib` awal |
| **3 Read** (W4, G3) | Membaca paper primer; mengekstrak klaim vs bukti; menilai kualitas | Evidence literacy, Abstraction | Pra-baca: struktur paper, istilah, ringkasan bagian; menjawab pertanyaan tentang teks yang **Anda** unggah (bila lisensi mengizinkan) | Source-grounded synthesis (asisten berbasis dokumen yang Anda unggah); Reference management (Zotero/Mendeley/JabRef untuk PDF & anotasi) | Baris matriks berisi rujukan halaman/tabel; peer cross-check 2 baris terhadap PDF; ringkasan AI tidak pernah menggantikan membaca bagian metode & hasil | Synthesis matrix baris per sumber |
| **4 Synthesis** (W4–W5, G3) | Mengelompokkan ke tema; menemukan pola konsisten/bertentangan/belum diuji; menulis evidence map | Abstraction, Evidence literacy | Mengusulkan taksonomi tema; menyorot kontradiksi antar baris matriks yang Anda berikan; menyusun draft tabel tema × sumber | Source-grounded synthesis; General reasoning | Tiap tema dicocokkan ke baris matriks yang benar-benar dibaca; kontradiksi dicek di paper asli; tidak ada sumber baru masuk tanpa verifikasi | Literature Evidence Map |
| **5 Gap** (W5, G3→G4) | Menurunkan gap dari matriks; memilih jenis gap; menilai apakah gap layak diisi | Falsification, First principles | Menantang gap ("sub-area apa yang mungkin terlewat?"); mengusulkan pencarian tambahan | General reasoning; Literature search (pencarian ulang) | Klaim "belum ada" dibuktikan dengan pencarian ulang yang tercatat; gap merujuk baris matriks, bukan percakapan AI | Gap Candidates di `docs/literature-map.md` → Research Gap di `docs/research-question.md`, Issue `type:literature-gap` |
| **6 RQ** (W6, G4) | Merumuskan RQ/hipotesis; menetapkan batas & Δ praktis; menulis kontribusi | Hypothesis, Decomposition | Brainstorming hipotesis saingan; memeriksa apakah RQ bisa salah; mengusulkan dekomposisi | General reasoning | RQ tertelusur ke gap & matriks; kriteria penolakan ditulis tim; hipotesis saingan dari AI dicek relevansinya | RQ/Hypothesis, Contribution Statement |
| **7 Method** (W7–W8, G5) | Memilih metode dari Methods Map; mendesain kontrol/sampling; menetapkan baseline & metrik; menulis threats | Falsification, Causal reasoning, First principles | Red team desain; menjelaskan metode/metrik; menyebut ancaman validitas khas; mengusulkan baseline standar untuk dibandingkan | General reasoning; Statistics (asisten statistik/penjelas uji) | Metrik & baseline dipilih dengan justifikasi tim sebelum eksperimen; kritik AI diklasifikasi terima/tolak dengan alasan; red team manusia W8 | Research Design (TPL-08), Experiment Card (TPL-09), Threats v1 |
| **8 Coding** (W9, G6) | Menyusun repositori; implementasi pipeline & baseline; data governance | Decomposition, Metacognition | Coding support; debugging; skrip utilitas; penjelasan error; refactoring; menulis tes | Coding (asisten kode di IDE/terminal); Notebooks (Jupyter/Colab) | Semua kode AI dibaca, dijalankan, diuji; sanity check leakage/split; tidak ada data mentah/pribadi ke AI; atribusi di log | `src/`, `experiments/`, README, kartu dataset |
| **9 Experiment** (W10, G6) | Menjalankan pilot; mencatat seed/config/log; mengelola hasil | Falsification, Metacognition | Diagnosis kegagalan run; saran sanity check; penjelasan perilaku model | Coding; Notebooks; experiment tracking sederhana | Hasil berasal dari run tercatat; semua seed dilaporkan; peer mereproduksi baseline | Pilot results di `results/`, catatan reproduksi |
| **10 Analysis** (W11–W12, G7) | Membandingkan ke baseline; error analysis; ketidakpastian; CER; membatasi klaim | Causal & statistical reasoning, Falsification | Menjelaskan uji/interval/effect size; menyarankan analisis; membantu kode plotting; menantang klaim yang melebihi bukti | Statistics (Python/R + asisten penjelas; JASP/jamovi sebagai contoh GUI); General reasoning | **Semua angka dihitung ulang** dari data oleh skrip tim; asumsi uji dicek; figur dicek terhadap data; AI tidak menginterpretasi tanpa data | `results/analysis.md`, CER table, Threats v2, figur |
| **11 Writing** (W13, G8) | Menulis proposal/manuscript dari Research Pack; argumentasi CER; sitasi | Metacognition, Abstraction | Penyuntingan bahasa; umpan balik struktur; konsistensi istilah; pengecekan bahwa tiap klaim menunjuk bukti | Writing (editor LaTeX/Markdown, pemeriksa bahasa; asisten umum untuk umpan balik) | Bagian hasil/diskusi ditulis tim; sitasi hanya dari `references.bib` terverifikasi; `docs/AI-USAGE.md` diperbarui; teks AI tidak dipakai tanpa verifikasi isi | Proposal TA / manuscript v0.8 (`paper/proposal.md`), `docs/AI-USAGE.md` + `paper/AI-USAGE-STATEMENT.md`, Reproducibility README (`experiments/README.md`) |
| **12 Review** (W14–W15, G8) | Mereview tim lain (TPL-12); menanggapi review; revisi | Evidence literacy, Metacognition | Reviewer tambahan untuk draft **sendiri**; bantu menyusun response letter; cek konsistensi revisi | Peer review support (asisten umum dengan checklist TPL-12) | Review untuk tim lain ditulis sendiri; draft tim lain tidak diunggah ke AI tanpa izin; perubahan angka = run baru tercatat | Review terkirim, response letter (`paper/response-to-reviewers.md`), proposal v0.9 (revisi pasca peer review), TPL-11 |
| **13 Publication** (pasca-G8; [MET-05](../04-metopen-research-studio/05-publication-backward-design.md)) | Memilih venue; format; authorship; submit; rilis artefak | Systems thinking, Metacognition | Cek kesesuaian template/panjang; ringkasan kebijakan venue (diverifikasi); draft cover letter untuk disunting | Writing; Reference management; General reasoning | Venue ada di registry TPL-06; kebijakan AI venue dibaca dari sumber resmi; semua penulis menyetujui; TPL-11 | Submission package, entri `publications/`, release v1.1/v2.0 |

## 3. Penjelasan per tahap dan red flags

### 3.1 Problem
AI berguna sebagai lawan diskusi yang tak lelah: minta ia menantang framing, menyebut stakeholder yang terlewat, dan mengusulkan tiga cara membingkai masalah. Tetapi AI tidak mengenal stakeholder Anda, tidak tahu data apa yang tersedia di UAI, dan gemar membuat masalah terdengar penting dengan angka tanpa sumber. Hasil akhirnya harus ditulis ulang oleh tim dan dikonfirmasi ke orang nyata.
**Red flags:** kalimat masalah berisi statistik tanpa sumber; masalah dan "urgensinya" persis seperti output AI generik; endgame "membuat aplikasi"; tim tidak bisa menyebut satu orang yang peduli.

### 3.2 Search
Ini tahap di mana AI paling produktif: kata kunci, sinonim lintas bahasa, string pencarian, dan tool deep research untuk menemukan kandidat yang terlewat oleh pencarian manual. Risikonya juga paling terkenal: referensi yang tidak ada. Aturan tunggal: **AI boleh menemukan, tidak pernah mengutip.** Setiap kandidat dibuka dan dicocokkan sebelum masuk `references.bib`.
**Red flags:** entri `.bib` tanpa DOI/URL; judul yang "terlalu pas"; penulis terkenal dengan judul yang tidak ada di profil mereka; log tidak mencatat sumber mana yang datang lewat AI.

### 3.3 Read
AI dapat mengurangi waktu orientasi (struktur paper, istilah, apa yang diklaim) dan menjawab pertanyaan tentang dokumen yang Anda unggah. Yang tidak boleh terjadi: ringkasan AI menggantikan membaca bagian metode, hasil, dan keterbatasan — karena di sanalah kualitas bukti terlihat. Perhatikan lisensi PDF sebelum mengunggah ke layanan eksternal.
**Red flags:** baris matriks tanpa rujukan halaman/tabel; keterbatasan paper "tidak ada"; anggota tim tidak bisa menjawab "baseline paper ini apa?".

### 3.4 Synthesis
Mengelompokkan 20 paper ke tema adalah pekerjaan abstraksi yang AI bantu dengan cepat, terutama jika Anda memberinya matriks Anda sendiri (bukan meminta ia "mencari"). Verifikasinya sederhana: setiap tema harus bisa ditunjuk ke baris yang Anda baca; kontradiksi yang disorot AI dicek di paper.
**Red flags:** tema yang tidak punya baris matriks; "related work" berbentuk paragraf per paper; sumber baru muncul di tahap ini tanpa lewat tahap Search/Read.

### 3.5 Gap
AI bagus untuk *menantang* gap ("apakah ini sudah dijawab di sub-bidang lain?"), buruk untuk *menyatakan* gap ("belum ada penelitian tentang X" adalah klaim yang AI tidak bisa buktikan). Tanggapi tantangan AI dengan pencarian ulang yang tercatat.
**Red flags:** gap naratif "belum ada di UAI/Indonesia"; gap yang muncul dari percakapan AI tanpa baris matriks; tidak ada pencarian ulang setelah AI menyebut sub-area.

### 3.6 RQ
AI berguna untuk menghasilkan hipotesis saingan dan memeriksa apakah RQ bisa salah. Δ yang berarti dan batas RQ tetap keputusan tim berdasarkan stakeholder dan waktu semester.
**Red flags:** RQ generik ("bagaimana penerapan..."); tidak ada kriteria penolakan; RQ berubah setelah hasil tanpa catatan.

### 3.7 Method
Gunakan AI sebagai red team desain — ini salah satu penggunaan paling bernilai. Namun AI tidak boleh **memilihkan** metrik/baseline: jika tim tidak bisa menjustifikasi pilihan tanpa AI, tim belum siap G5. Semua kritik AI diklasifikasi (terima/ubah desain/tolak dengan alasan) dan dicatat.
**Red flags:** metrik/baseline "disarankan AI" tanpa alasan tim; threats to validity generik; tidak ada kritik yang ditolak (tanda tim tidak menilai).

### 3.8 Coding
Coding support adalah penggunaan AI yang paling matang, tetapi kode AI yang berjalan bukan berarti benar: leakage sering datang dari kode "yang berhasil". Semua kode AI dibaca, diuji, dan diberi sanity check (split sebelum pra-pemrosesan, tidak ada fitur target). Data mentah/pribadi tidak pernah masuk prompt.
**Red flags:** commit besar tanpa penjelasan; tidak ada tes/sanity check; potongan data asli di riwayat prompt; anggota tidak bisa menjelaskan fungsi yang di-commit.

### 3.9 Experiment
AI membantu mendiagnosis run yang gagal dan mengusulkan pengecekan; ia tidak menghasilkan hasil. Hasil hanya sah bila berasal dari run tercatat (config, seed, log) dan peer dapat mereproduksinya.
**Red flags:** hasil "terlalu bagus" tanpa investigasi; hanya satu seed; hasil di tabel tidak ada di `results/`; run gagal tidak dicatat.

### 3.10 Analysis
Tahap paling berbahaya: AI menjelaskan statistik dengan lancar dan sering **mengarang angka** atau menyarankan uji yang asumsinya tidak terpenuhi. Prinsip: AI boleh menjelaskan dan menyarankan; **tim menghitung**. Setiap angka dalam `results/analysis.md` dihasilkan skrip dari data.
**Red flags:** angka yang tidak bisa dihasilkan ulang oleh skrip; "signifikan" tanpa effect size/variansi; interpretasi AI disalin ke diskusi; klaim kausal dari data observasional.

### 3.11 Writing
AI menyunting bahasa dan struktur dengan baik dan boleh dipakai — dengan pengungkapan. Bagian hasil dan diskusi ditulis tim dari CER table karena hanya tim yang tahu apa yang bukti dukung. Sitasi hanya dari `references.bib` yang sudah terverifikasi; AI tidak boleh "menambahkan referensi yang relevan".
**Red flags:** kalimat halus tetapi tidak konsisten dengan repositori; sitasi baru di tahap menulis; `docs/AI-USAGE.md` menyebut "membantu" tanpa rincian; anggota tidak bisa menjelaskan paragraf tertentu.

### 3.12 Review
Sebagai reviewer, Anda bertanggung jawab atas review Anda: AI boleh membantu Anda memeriksa draft **sendiri** atau menyusun response letter, tetapi review untuk tim lain ditulis sendiri dan draft orang lain tidak diunggah ke layanan AI tanpa izin (kerahasiaan). Revisi yang mengubah angka harus berupa run baru.
**Red flags:** review generik yang bisa berlaku untuk paper mana pun; response letter yang "menerima semua" tanpa perubahan; angka berubah di revisi tanpa commit eksperimen.

### 3.13 Publication
AI membantu memeriksa kesesuaian format dan meringkas kebijakan venue — yang kemudian dibaca dari sumber resminya. Pemilihan venue, authorship, dan pengungkapan AI mengikuti [MET-05](../04-metopen-research-studio/05-publication-backward-design.md) dan kebijakan venue.
**Red flags:** venue tidak ada di registry; ringkasan kebijakan venue dari AI tidak dicek; cover letter menjanjikan hal yang tidak ada di naskah; AI disebut sebagai penulis.

## 4. Rantai verifikasi dalam praktik

| Lapis | Pertanyaan | Contoh tindakan | Dicatat di |
|---|---|---|---|
| Source verification | Apakah sumber yang dirujuk AI benar-benar ada dan mengatakan itu? | Buka DOI; cocokkan kutipan dengan halaman | AI Usage Log kolom Verification; matriks |
| Reasoning verification | Apakah penalaran AI valid untuk konteks saya? | Cek asumsi uji; cek apakah saran metode cocok dengan RQ | Log; `docs/research-design.md` |
| Evidence verification | Apakah bukti saya sendiri mendukung apa yang AI/kami klaim? | Hitung ulang; jalankan ulang; bandingkan dengan `results/` | Log; `results/analysis.md` |
| Human accountability | Bisakah saya mempertahankan ini tanpa AI? | Jelaskan ke peer; tulis di `docs/AI-USAGE.md`; tanda tangani TPL-11 | `docs/AI-USAGE.md`, TPL-11, defense |

## 5. Ringkasan satu baris per tahap

| Tahap | AI boleh | AI tidak boleh |
|---|---|---|
| Problem | Menantang framing | Mengarang urgensi/statistik |
| Search | Menemukan kandidat | Mengutip |
| Read | Pra-baca | Menggantikan membaca metode & hasil |
| Synthesis | Mengusulkan tema dari matriks Anda | Menambah sumber tak terverifikasi |
| Gap | Menantang gap | Menyatakan "belum ada" |
| RQ | Hipotesis saingan | Menentukan Δ/batas |
| Method | Red team | Memilihkan metrik/baseline |
| Coding | Menulis/menjelaskan kode | Menerima data mentah; lolos tanpa tes |
| Experiment | Diagnosis run | Menghasilkan hasil |
| Analysis | Menjelaskan & menyarankan | Menghitung/menginterpretasi tanpa data |
| Writing | Bahasa & struktur | Menulis hasil/diskusi; menambah sitasi |
| Review | Reviewer tambahan untuk draft sendiri | Mereview tim lain untuk Anda |
| Publication | Cek format | Menjadi penulis; menggantikan pembacaan kebijakan |

## 6. Contoh penerapan: satu riset melintasi tiga belas tahap (ilustratif)

Tim `[isi]`, Research ID `UIAI-2026-0NN`, entry door *Faculty Research*, masalah: deteksi dini mahasiswa berisiko drop-out dari aktivitas LMS empat minggu pertama.

| Tahap | Yang dilakukan tim | Yang dilakukan AI | Verifikasi & catatan log |
|---|---|---|---|
| Problem | Wawancara singkat tim akademik: keputusan yang berubah = intervensi minggu ke-4 | Diminta 3 reframing problem-first; menyorot bahwa "prediksi" bukan tujuan, "intervensi tepat waktu" tujuannya | Reframing #2 dipakai setelah dikonfirmasi ke dosen pemilik masalah; #1 dan #3 ditolak (log #01) |
| Search | String pencarian di Scholar & Semantic Scholar; citation chaining dari 3 paper kunci | Kandidat kata kunci lintas bahasa ("early warning", "learning analytics", "at-risk") dan 12 kandidat paper dari mode deep research | 9 dari 12 kandidat ditemukan dan relevan; 3 tidak ditemukan → dibuang (log #02–#04) |
| Read | 18 paper dibaca; matriks diisi dengan rujukan halaman | Pra-baca struktur 6 paper yang paling sulit | Peer cross-check 2 baris; satu koreksi angka AUC (log #05) |
| Synthesis | 4 tema: fitur aktivitas, fitur akademik, ketidakseimbangan kelas, generalisasi lintas institusi | Diminta menyusun tabel tema × sumber dari matriks yang diberikan; menyorot kontradiksi pada tema 4 | Kontradiksi dicek di 3 paper; benar (log #06) |
| Gap | Gap kontekstual + metodologis: baseline sederhana jarang dilaporkan; data institusi Indonesia minim | AI menantang: "apakah sudah ada studi di Indonesia?" | Pencarian ulang dengan kata kunci Indonesia: 2 studi ditemukan, dimasukkan ke matriks; gap dipersempit (log #07) |
| RQ | "Apakah fitur aktivitas LMS 4 minggu pertama meningkatkan F1 kelas berisiko ≥0,05 dibanding baseline IPK semester 1?" | Hipotesis saingan: efek berasal dari mahasiswa cuti (survivorship) | Kriteria penolakan ditulis tim; hipotesis saingan masuk Threats (log #08) |
| Method | Benchmarking + experiment; baseline majority & logistic regression IPK; metrik F1 kelas positif; split stratified per angkatan | Red team desain: 8 ancaman; menyarankan AUC sebagai metrik | 4 ancaman diadopsi; AUC dijadikan metrik sekunder dengan justifikasi; SMOTE ditolak (log #09–#12) |
| Coding | Repositori TPL-15; `run.sh`; tes split | Fungsi split stratified dan evaluasi; penjelasan error pandas | Tes proporsi & ID unik lulus; tidak ada data ke AI (skema saja) (log #13–#18) |
| Experiment | Pilot pada 1 angkatan, 5 seed | Diagnosis run gagal (memory) | Peer dari tim lain mereproduksi baseline (selisih F1 <0,01) (log #19) |
| Analysis | Mean ± SD antar seed; error analysis pada false negative | Penjelasan interval bootstrap; kode plotting | Semua angka dari `src/analysis.py`; asumsi uji dicek; interpretasi ditulis tim (log #20–#23) |
| Writing | Proposal TA dari Research Pack | Penyuntingan bahasa bab 1–2; umpan balik struktur | Bagian hasil ditulis tim; sitasi hanya dari `.bib`; `docs/AI-USAGE.md` diperbarui (log #24–#26) |
| Review | Menulis 2 review untuk tim lain; menerima 2 review | Reviewer tambahan untuk draft sendiri | Draft tim lain tidak diunggah; response letter ditulis tim (log #27) |
| Publication | Endgame TA; aspirasi paper venue nasional setelah eksperimen penuh | — (belum) | Handoff mencatat "missing evidence: eksperimen 3 angkatan" |

Hasilnya: 27 entri log, 7 di antaranya berisi keputusan **ditolak** — tanda tim menilai, bukan menyalin. Reviewer G8 dapat mengaudit peran AI tanpa bertanya ke tim.

## 7. Cara memakai tabel ini di studio

| Pengguna | Gunakan untuk |
|---|---|
| Mahasiswa | Sebelum memakai AI di suatu tahap, baca baris tahap itu: apa tugas manusia, apa peran AI, verifikasi apa yang wajib; salin kolom *Verification* ke kolom verifikasi di AI Usage Log |
| Dosen (blok konsep) | Tampilkan satu baris tabel di minggu terkait ([MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)); bahas satu red flag dengan contoh nyata (dianonimkan) dari semester sebelumnya |
| Mentor (studio) | Saat tim menunjukkan output AI, tanyakan tiga hal: "sumbernya?", "kamu hitung/jalankan ulang?", "dicatat di mana?" |
| Reviewer gate | Cocokkan log tim dengan kolom *Verification* tahap yang direview; red flags §3 menjadi daftar periksa cepat |
| Tim kurikulum | Untuk mata kuliah mode E/R, ambil subset tahap (mis. Coding–Experiment–Analysis untuk AI/ML) dan sesuaikan level target ([AIX-02](02-ai-research-competency-framework.md) §7) |

Tabel ini sengaja **tidak** menyebut nama tool spesifik selain sebagai contoh; ketika tool berganti, kolom *Human Task*, *Verification*, dan *Artifact* tetap berlaku. Itulah bagian yang harus dikuasai mahasiswa.
