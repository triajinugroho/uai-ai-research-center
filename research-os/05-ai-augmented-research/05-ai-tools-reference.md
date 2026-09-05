# AI Tools Reference — Katalog Kategorikal Tool Riset

> **ID** AIX-05 · **Paket** 05 AI-Augmented Research & Meta-Thinking · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen/mentor, pengelola lab/AI Center, admin riset (akses & biaya)
> **Terkait** [AIX-03 AI Across Value Stream](03-ai-across-research-value-stream.md) · [AIX-04 AI Research Protocol](04-ai-research-protocol.md) · [AIX-02 AI Research Competency](02-ai-research-competency-framework.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md) · [SECURITY.md](../../SECURITY.md) · [LICENSING.md](../../LICENSING.md) · [AI toolkit studio](../../metopen-research-studio/ai-toolkit/README.md)

## 1. Mengapa katalog kategorikal

Tool AI berganti tiap beberapa bulan; **fungsi** dalam riset tidak. Dokumen ini menata tool berdasarkan fungsi (kategori) sehingga tetap berguna ketika nama produk berubah. Nama tool yang disebut hanyalah **contoh dan bisa berubah**; tidak ada tool yang diwajibkan, dan tidak ada tool yang otomatis "disetujui" — yang disetujui adalah **cara memakainya** ([AIX-04](04-ai-research-protocol.md)).

Tiga pertanyaan sebelum memakai tool apa pun:

1. **Fungsi apa** yang saya butuhkan di tahap riset ini? ([AIX-03](03-ai-across-research-value-stream.md))
2. **Data apa** yang akan saya masukkan, dan bolehkah? (§4)
3. **Bagaimana saya memverifikasi** outputnya, dan di mana saya mencatatnya? (TPL-10)

Format tiap kategori: fungsi dalam riset → kriteria memilih → contoh tool → risiko & verifikasi → tahap value stream.

## 2. Sebelas kategori

### 2.1 General reasoning (asisten percakapan umum)

- **Fungsi.** Diskusi, reframing masalah, penjelasan konsep, brainstorming hipotesis, red team desain, umpan balik struktur tulisan, latihan pitch.
- **Kriteria memilih.** Kualitas penalaran pada teks panjang; dapat menerima konteks/artefak (teks, tabel); kebijakan data (apakah input dipakai untuk pelatihan; opsi *opt-out*); ketersediaan tanpa biaya bagi mahasiswa; kemampuan menyebut ketidakpastian.
- **Contoh (bisa berubah).** ChatGPT, Claude, Gemini, dan asisten sejenis; model open-weight yang dijalankan lokal untuk konteks sensitif.
- **Risiko & verifikasi.** Halusinasi fakta dan sitasi; sycophancy; penjelasan lancar ≠ benar. Verifikasi: sumber dibuka; tanya "apa yang salah dari jawabanmu"; tidak pernah dipakai untuk mengutip atau menghitung.
- **Tahap.** Problem, Gap, RQ, Method (red team), Analysis (penjelasan), Writing (umpan balik), Review (draft sendiri).

### 2.2 Deep research (mode riset otomatis multi-langkah)

- **Fungsi.** Menjelajah banyak sumber web/akademik untuk memetakan landscape topik dan menemukan kandidat sumber yang terlewat.
- **Kriteria memilih.** Menyertakan tautan sumber yang bisa dibuka; membedakan sumber akademik dan non-akademik; transparan tentang cakupan pencarian.
- **Contoh (bisa berubah).** Mode "deep research"/"research" pada asisten umum; agen pencarian akademik.
- **Risiko & verifikasi.** Laporan panjang yang tampak lengkap tetapi menyembunyikan sumber lemah; sumber yang salah dikutip; bias ke sumber berbahasa Inggris. Verifikasi: laporan hanya dipakai sebagai **daftar kandidat**; setiap sumber melewati tahap Search/Read biasa; tidak pernah dikutip langsung.
- **Tahap.** Search (kandidat), Gap (pencarian ulang).

### 2.3 Literature search (basis data & mesin pencari akademik)

- **Fungsi.** Menemukan paper primer secara sistematis dengan kata kunci, filter, dan citation chaining.
- **Kriteria memilih.** Cakupan bidang computing; metadata lengkap (DOI, venue, tahun); filter dan ekspor `.bib`; akses institusi bila berbayar.
- **Contoh (bisa berubah).** Google Scholar, Semantic Scholar, Scopus (bila kampus berlangganan), OpenAlex, arXiv, ACM Digital Library/IEEE Xplore (akses sesuai langganan), Garuda/SINTA untuk jurnal nasional.
- **Risiko & verifikasi.** Preprint tanpa review; duplikasi versi; metadata salah. Verifikasi: catat string pencarian dan tanggal di `docs/literature/search-strategy.md` dan `docs/literature/search-log.csv`; cek versi terbit; ekspor ke reference manager, bukan disalin manual.
- **Tahap.** Search, Gap.

### 2.4 Citation intelligence (peta sitasi & konteks kutipan)

- **Fungsi.** Melihat siapa mengutip siapa, paper mana yang sentral, dan bagaimana sebuah klaim dikutip (mendukung/membantah).
- **Kriteria memilih.** Data sitasi yang luas dan mutakhir; visualisasi jaringan; tautan ke DOI; konteks kutipan (bila ada).
- **Contoh (bisa berubah).** Connected Papers, Research Rabbit, Litmaps, Scite, fitur "cited by"/"references" di Semantic Scholar.
- **Risiko & verifikasi.** Jaringan sitasi ≠ kualitas; paper banyak dikutip bisa dikutip karena dibantah; cakupan tidak lengkap untuk jurnal nasional. Verifikasi: paper sentral tetap dibaca; konteks kutipan dicek di teks asli.
- **Tahap.** Search (citation chaining), Synthesis.

### 2.5 Reference management (pengelola referensi)

- **Fungsi.** Menyimpan PDF, metadata, anotasi; menghasilkan `references.bib` dan sitasi yang konsisten.
- **Kriteria memilih.** Ekspor BibTeX; sinkronisasi tim; plugin browser; gratis/open-source bila memungkinkan; penyimpanan PDF sesuai lisensi.
- **Contoh (bisa berubah).** Zotero (disarankan: gratis, open-source, grup tim), Mendeley, JabRef.
- **Risiko & verifikasi.** Metadata otomatis salah (tahun, penulis); duplikasi. Verifikasi: cek tiap entri terhadap halaman DOI sebelum `.bib` di-commit; satu pemilik `references.bib` per tim.
- **Tahap.** Search, Read, Writing, Publication.

### 2.6 Source-grounded synthesis (sintesis berbasis dokumen yang Anda unggah)

- **Fungsi.** Tanya-jawab dan ringkasan yang **terjangkar** pada dokumen yang Anda berikan (PDF paper, matriks, catatan), dengan rujukan ke bagian dokumen.
- **Kriteria memilih.** Jawaban menyertakan kutipan/lokasi dalam dokumen; tidak "mengarang" di luar dokumen; kebijakan data untuk dokumen yang diunggah; dukungan banyak dokumen sekaligus.
- **Contoh (bisa berubah).** NotebookLM, Elicit, Consensus, SciSpace, fitur unggah dokumen pada asisten umum.
- **Risiko & verifikasi.** Melampaui dokumen tanpa memberi tahu; salah menempatkan klaim; lisensi PDF publisher mungkin melarang pengunggahan ke layanan pihak ketiga ([LICENSING.md](../../LICENSING.md)). Verifikasi: setiap jawaban ditelusuri ke halaman; hanya unggah dokumen yang lisensinya mengizinkan; baris matriks tetap ditulis dari bacaan sendiri.
- **Tahap.** Read, Synthesis.

### 2.7 Coding (asisten kode)

- **Fungsi.** Menulis, menjelaskan, dan memperbaiki kode; membuat tes; refactoring; skrip utilitas eksperimen.
- **Kriteria memilih.** Integrasi IDE/terminal; kebijakan data untuk kode yang dikirim; dukungan bahasa/pustaka riset (Python, R); kemampuan menjalankan tes lokal; biaya/akses pendidikan.
- **Contoh (bisa berubah).** GitHub Copilot, Cursor, Claude Code, asisten kode pada IDE populer; model lokal untuk repositori sensitif.
- **Risiko & verifikasi.** Kode berjalan tetapi salah (leakage, off-by-one pada split, metrik salah); ketergantungan tidak perlu; kode yang tidak dipahami; kredensial/data ikut terkirim. Verifikasi: baca seluruh kode; tes unit/sanity check (proporsi split, ID unik, tidak ada fitur target); `.gitignore` data; atribusi di AI Usage Log.
- **Tahap.** Coding, Experiment, Analysis (plotting).

### 2.8 Notebooks & compute (lingkungan eksperimen)

- **Fungsi.** Menjalankan eksperimen secara interaktif dan terdokumentasi; akses GPU terbatas.
- **Kriteria memilih.** Reproducibility (dapat dijalankan dari atas ke bawah); ekspor ke skrip; environment pinned; kuota GPU; penyimpanan data sesuai klasifikasi.
- **Contoh (bisa berubah).** Jupyter/JupyterLab lokal atau server lab, Google Colab, Kaggle Notebooks; komputasi lab Prodi/AI Center (`[isi]`).
- **Risiko & verifikasi.** Notebook dijalankan tidak berurutan; hasil tidak dapat diulang; data RESTRICTED diunggah ke cloud. Verifikasi: "Restart & run all" sebelum commit; logika inti dipindah ke `src/`; data sensitif hanya di infrastruktur yang diizinkan.
- **Tahap.** Coding, Experiment, Analysis.

### 2.9 Statistics (alat & asisten statistik)

- **Fungsi.** Menghitung statistik deskriptif, ketidakpastian, uji sederhana, effect size; memeriksa asumsi; membuat figur.
- **Kriteria memilih.** Dapat diskrip (reproducible); dokumentasi metode jelas; gratis; keluaran yang dapat dimasukkan ke `results/`.
- **Contoh (bisa berubah).** Python (`scipy`, `statsmodels`, `scikit-learn`, `matplotlib`/`seaborn`), R; JASP/jamovi sebagai GUI open-source untuk pemula; asisten umum untuk **menjelaskan** uji.
- **Risiko & verifikasi.** Memilih uji yang asumsinya tidak terpenuhi; p-value tanpa effect size; angka dari asisten AI yang tidak dihitung. Verifikasi: semua angka dari skrip di repositori; asumsi dicek dan dicatat; interpretasi ditulis tim.
- **Tahap.** Analysis.

### 2.10 Writing (penulisan ilmiah)

- **Fungsi.** Menyusun manuscript/proposal, mengelola sitasi, menyunting bahasa dan struktur, menjaga konsistensi istilah.
- **Kriteria memilih.** Dukungan BibTeX/format venue; kolaborasi tim; riwayat versi; kebijakan data untuk draft yang belum terbit (INTERNAL).
- **Contoh (bisa berubah).** LaTeX (Overleaf atau lokal), Markdown + Pandoc, pengolah kata standar; pemeriksa bahasa (mis. Grammarly, Writefull, LanguageTool); asisten umum untuk umpan balik struktur.
- **Risiko & verifikasi.** Teks halus yang menyimpang dari hasil; sitasi "ditambahkan" AI; draft belum terbit terkirim ke layanan yang menyimpan data. Verifikasi: bagian hasil/diskusi ditulis dari CER; sitasi hanya dari `references.bib`; pengungkapan di `docs/AI-USAGE.md`; hormati kebijakan AI venue.
- **Tahap.** Writing, Publication.

### 2.11 Peer review support (bantuan review)

- **Fungsi.** Membantu reviewer memeriksa kelengkapan (checklist TPL-12), konsistensi klaim–bukti, dan menyusun komentar yang spesifik; membantu penulis mengantisipasi kritik.
- **Kriteria memilih.** Bekerja pada dokumen yang Anda berikan; tidak menyimpan/melatih dari naskah rahasia; keluaran berupa pertanyaan/pengecekan, bukan "skor".
- **Contoh (bisa berubah).** Asisten umum atau source-grounded dengan prompt berbasis TPL-12; checklist reviewer venue.
- **Risiko & verifikasi.** Melanggar kerahasiaan naskah orang lain; review generik; reviewer tidak membaca. Verifikasi: **draft tim lain tidak diunggah** ke layanan AI tanpa izin; review ditulis sendiri dan merujuk halaman/tabel; AI hanya untuk draft sendiri, diungkap.
- **Tahap.** Review, Publication.

## 3. Tabel ringkas

| Kategori | Fungsi utama | Tahap value stream | Risiko utama | Verifikasi minimum | Data yang boleh masuk |
|---|---|---|---|---|---|
| General reasoning | Diskusi, reframing, red team, penjelasan | Problem–Writing | Halusinasi, sycophancy | Sumber dibuka; tanya "apa yang salah"; tidak untuk mengutip/menghitung | PUBLIC; ringkasan artefak tanpa data pribadi |
| Deep research | Landscape & kandidat sumber | Search, Gap | Sumber lemah tersembunyi | Kandidat saja; verifikasi tiap sumber | Topik/kata kunci |
| Literature search | Menemukan paper primer | Search, Gap | Preprint, metadata salah | Catat strategi; cek versi | Kata kunci |
| Citation intelligence | Peta & konteks sitasi | Search, Synthesis | Sitasi ≠ kualitas | Baca paper sentral | DOI |
| Reference management | `.bib`, PDF, anotasi | Search–Publication | Metadata salah | Cek tiap entri vs DOI | PDF sesuai lisensi |
| Source-grounded synthesis | Tanya-jawab atas dokumen Anda | Read, Synthesis | Melampaui dokumen; lisensi PDF | Telusuri ke halaman | Dokumen berlisensi sesuai |
| Coding | Kode, tes, debugging | Coding–Analysis | Kode salah tapi jalan; leakage | Baca, tes, sanity check, log | Kode & skema; **bukan** data mentah/kredensial |
| Notebooks & compute | Eksperimen interaktif | Coding–Analysis | Tidak reproducible; data cloud | Run-all; logika ke `src/` | Sesuai klasifikasi data |
| Statistics | Angka, uji, figur | Analysis | Uji salah; angka AI | Skrip di repo; asumsi dicek | Data tim di lingkungan yang diizinkan |
| Writing | Draft, sitasi, bahasa | Writing, Publication | Teks menyimpang; sitasi palsu | CER; `.bib` terverifikasi; disclose | Draft INTERNAL hanya ke layanan yang sesuai |
| Peer review support | Checklist, konsistensi | Review, Publication | Kerahasiaan | Draft sendiri saja; review ditulis sendiri | Draft sendiri |

## 4. Kebijakan penggunaan data pada tool AI

Mengikuti [SECURITY.md](../../SECURITY.md):

| Klasifikasi | Boleh ke layanan AI eksternal? | Catatan |
|---|---|---|
| **PUBLIC** (framework, kode publik, metadata dataset publik, paper terbit sesuai lisensi) | Ya | Tetap catat di log bila material |
| **INTERNAL** (draft belum terbit, kode riset, hasil awal) | Hanya ke layanan dengan kebijakan tidak-melatih/tidak-menyimpan yang jelas, atau model lokal; seizin tim | Draft orang lain: perlu izin pemiliknya |
| **RESTRICTED** (data pribadi, data partner, data kesehatan, kredensial) | **Tidak pernah** | Gunakan ringkasan statistik/skema tanpa nilai; atau model lokal di infrastruktur yang diizinkan pemilik data |

Aturan praktis: sebelum menempel apa pun ke prompt, tanyakan "kalau teks ini bocor ke publik, apakah ada yang dirugikan?" Jika ya, jangan.

## 5. Biaya dan akses untuk mahasiswa

- **Default gratis.** Semua kategori memiliki opsi gratis/open-source yang memadai untuk Metopen (asisten umum tingkat gratis, Google Scholar/Semantic Scholar/OpenAlex, Zotero, Jupyter/Colab, Python/R, LaTeX/Markdown). Tidak ada tugas Metopen yang mensyaratkan tool berbayar.
- **Langganan institusi.** Akses basis data berbayar (mis. Scopus, ACM DL, IEEE Xplore) mengikuti langganan perpustakaan/kampus (`[isi]` status terkini); program edukasi vendor (mis. paket mahasiswa untuk asisten kode) dimanfaatkan bila tersedia.
- **Komputasi.** Kuota GPU gratis di layanan notebook publik cukup untuk pilot; kebutuhan lebih besar diajukan ke lab/AI Center dengan kartu dataset dan Experiment Card sebagai justifikasi.
- **Kesetaraan.** Penilaian tidak boleh bergantung pada tool berbayar; reviewer menilai verifikasi dan artefak, bukan kecanggihan tool.
- **Akun.** Gunakan akun yang dapat dipertanggungjawabkan (institusi bila ada); jangan berbagi akun/kredensial; simpan API key di luar repositori.

## 6. Prosedur mengusulkan tool baru

1. Buka Issue di repositori ini lewat form yang paling dekat (form **Bug** untuk perbaikan/penambahan dokumen; taksonomi label mengikuti [GOVERNANCE.md](../../GOVERNANCE.md) §6 tanpa label baru) berjudul `Tool proposal: <nama> (<kategori>)`, atau langsung ajukan PR ke dokumen ini.
2. Isi: kategori (§2), fungsi dalam riset, tahap value stream, kebijakan data tool (tautan ke ketentuan layanan), biaya/akses, contoh verifikasi output, risiko yang diketahui, siapa yang sudah mencoba dan hasilnya.
3. Pengelola `metopen-research-studio/ai-toolkit/` atau `@maintainers` menilai terhadap kriteria kategori dan kebijakan data (§4).
4. Bila diterima: ditambahkan sebagai **contoh** di kategori terkait (dokumen ini) dan di panduan praktis [AI toolkit studio](../../metopen-research-studio/ai-toolkit/README.md); bila ditolak: alasan dicatat di Issue.
5. Contoh tool ditinjau tiap semester; tool yang tidak lagi tersedia atau berubah kebijakan datanya dihapus/diperbarui. Kategori dan kriteria jarang berubah; itulah alasan katalog ini kategorikal.

## 7. Pengingat

Tool terbaik bukan yang paling canggih, melainkan yang outputnya **paling mudah Anda verifikasi** dan **paling aman untuk data Anda**. Bila dua tool sama-sama berguna, pilih yang gratis, terbuka, dan bisa dijalankan ulang oleh peer Anda.
