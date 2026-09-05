# AI Research Competency Framework — Consumer → Collaborator → Investigator → Governor

> **ID** AIX-02 · **Paket** 05 AI-Augmented Research & Meta-Thinking · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen pengampu/mentor, reviewer gate, tim kurikulum (untuk RPS mata kuliah mode E/R)
> **Terkait** [AIX-01 Meta-Thinking](01-research-meta-thinking.md) · [AIX-03 AI Across Value Stream](03-ai-across-research-value-stream.md) · [AIX-04 AI Research Protocol](04-ai-research-protocol.md) · [AIX-05 AI Tools Reference](05-ai-tools-reference.md) · [MET-02 Course Outcomes](../04-metopen-research-studio/02-metopen-course-outcomes.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md) · [MST-03 Glossary](../00-master/03-glossary.md)

## 1. Mengapa perlu tangga kompetensi

Semua mahasiswa sudah memakai AI. Pertanyaannya bukan *apakah*, melainkan *pada level apa*. Dua mahasiswa yang sama-sama "memakai ChatGPT untuk literatur" bisa berada di ujung yang berlawanan: satu menyalin referensi yang tidak ada, satu lagi memakai AI untuk menemukan kandidat, membuka setiap DOI, mencatat verifikasinya, dan menolak dua sumber yang ternyata tidak relevan.

Kerangka ini memberi empat level agar perilaku itu **terlihat, dapat dinilai, dan dapat ditingkatkan**:

```
AI Consumer  →  AI Collaborator  →  AI Investigator  →  AI Governor
 memakai         memberi konteks       memakai AI untuk     memverifikasi,
                 & mengiterasi         riset (bukti,        mendokumentasikan,
                                       eksperimen)          mempertanggungjawabkan
```

**Target Metopen (glossary §4.4):** semua mahasiswa minimal **AI Investigator**, dengan perilaku **AI Governor** (memverifikasi, mendokumentasikan, mempertanggungjawabkan). Level ini bukan tentang kecanggihan prompt; ia tentang **hubungan epistemik** antara peneliti dan AI: AI sebagai *research copilot*, bukan *epistemic authority*.

Level bersifat kumulatif: Governor tetap melakukan hal-hal Collaborator; yang berubah adalah siapa yang memegang tanggung jawab atas kebenaran.

## 2. Empat level

### 2.1 Level 1 — AI Consumer

**Deskripsi.** Memakai AI seperti mesin jawab: bertanya, menerima, memakai. Output AI diperlakukan sebagai jawaban, bukan sebagai kandidat.

**Perilaku yang terlihat.** Prompt satu kalimat tanpa konteks; menyalin output ke dokumen; tidak membedakan mana yang diverifikasi; tidak ada log; percaya referensi/angka dari AI; menganggap "AI bilang" sebagai argumen.

**Contoh prompt/praktik.** "Buatkan latar belakang penelitian tentang prediksi kelulusan mahasiswa dengan machine learning." → hasil ditempel ke proposal.

**Kesalahan khas.** Referensi buatan AI masuk `references.bib`; "statistik masalah" tanpa sumber; kode AI di-commit tanpa dibaca; RQ generik yang tidak tertelusur ke literatur.

**Bukti kompetensi (bahwa seseorang berada di level ini).** Tidak ada AI Usage Log atau log diisi belakangan; saat ditanya "dari mana angka ini?", jawabannya "dari AI".

**Kaitan ke rubrik.** Evidence dan Execution paling tinggi *Developing*; risiko gagal Research Integrity Gate (sitasi palsu, AI tidak diungkap).

### 2.2 Level 2 — AI Collaborator

**Deskripsi.** Memperlakukan AI sebagai rekan diskusi: memberi konteks, mengiterasi, membandingkan beberapa jawaban, meminta kritik.

**Perilaku yang terlihat.** Prompt berisi konteks (masalah, data, batasan); meminta beberapa alternatif; menindaklanjuti dengan "mengapa?"; menyunting output secara substansial; mulai membedakan mana ide AI dan mana ide sendiri.

**Contoh prompt/praktik.** "Konteks: kami meneliti prediksi risiko drop-out di prodi Informatika dengan data akademik 6 semester (n≈400). Stakeholder: tim akademik yang memutuskan intervensi di minggu ke-4. Berikan 3 cara membingkai masalah ini secara problem-first, dan untuk masing-masing sebutkan keputusan apa yang berubah." → hasil dibandingkan, satu dipilih dan ditulis ulang.

**Kesalahan khas.** Iterasi panjang tetapi tanpa verifikasi ke sumber luar; nyaman dengan jawaban yang "terdengar benar"; belum memakai AI untuk bagian riset yang sulit (desain, analisis); log tidak konsisten.

**Bukti kompetensi.** Riwayat prompt menunjukkan konteks dan iterasi; draft berbeda jelas dari output AI; AI Usage Log mulai ada tetapi verifikasi belum sistematis.

**Kaitan ke rubrik.** End bisa *Proficient*; Evidence dan Experiment masih rawan *Developing* karena verifikasi belum sistematis.

### 2.3 Level 3 — AI Investigator

**Deskripsi.** Memakai AI sebagai instrumen riset pada tahap-tahap yang bernilai: literature intelligence, red team desain, penjelasan statistik, coding eksperimen, analisis — **dengan verifikasi terhadap sumber, penalaran, dan bukti** untuk setiap output yang memengaruhi kesimpulan.

**Perilaku yang terlihat.** Tahu tahap mana AI membantu dan mana tidak ([AIX-03](03-ai-across-research-value-stream.md)); memakai AI untuk menemukan, lalu membuka sumber asli; meminta AI mencari cara riset bisa gagal; kode AI dibaca, diuji, dan dipahami sebelum di-commit; angka dari AI selalu dihitung ulang; menolak output AI dengan alasan yang tercatat.

**Contoh prompt/praktik.** "Berikut Experiment Card kami (baseline majority class dan logistic regression; metrik F1 kelas minoritas; split stratified 70/15/15 dengan seed 42; fitur dari semester 1–4). Bertindaklah sebagai reviewer yang skeptis: sebutkan 10 cara hasil kami bisa menyesatkan, urutkan dari yang paling mungkin, dan untuk masing-masing usulkan pengecekan konkret." → 4 ancaman diverifikasi relevan, 2 pengecekan masuk microtask, sisanya ditolak dengan alasan di log.

**Kesalahan khas.** Verifikasi dilakukan tetapi tidak didokumentasikan; pengungkapan AI hanya di acknowledgment padahal memengaruhi metode; masih memasukkan potongan data mentah ke prompt.

**Bukti kompetensi.** AI Usage Log menunjukkan pola *Ask → Ground → Verify*; ada entri "ditolak"; sumber dari AI semuanya terverifikasi; kode AI punya tes/sanity check; reviewer tidak menemukan output AI yang tidak diverifikasi.

**Kaitan ke rubrik.** Evidence, Experiment, Explanation dapat *Proficient*–*Exemplary*; Execution *Proficient* bila log konsisten.

### 2.4 Level 4 — AI Governor

**Deskripsi.** Mengatur penggunaan AI dalam riset sebagai sistem: menetapkan aturan (apa yang boleh/tidak, data apa yang tidak masuk), memverifikasi secara sistematis, mendokumentasikan sehingga orang lain bisa mengaudit, dan **mempertanggungjawabkan** semua hasil sebagai miliknya. Di level ini AI Usage Statement bukan formalitas; ia bagian dari metode.

**Perilaku yang terlihat.** AI Usage Log kontemporer dan spesifik; `AI-USAGE.md` membedakan bantuan penulisan dan bantuan proses riset; data sensitif tidak pernah ke AI; memilih tool berdasarkan kriteria ([AIX-05](05-ai-tools-reference.md)); mengajari/mengoreksi anggota tim; menyatakan batas: "bagian ini dibantu AI dan sudah diverifikasi dengan ___"; bisa menjelaskan setiap bagian yang dibantu AI tanpa AI.

**Contoh prompt/praktik.** Sebelum memakai AI untuk analisis: menulis di log "tujuan: cek asumsi uji; input: ringkasan statistik (bukan data mentah); verifikasi: hitung ulang dengan fungsi pemeriksaan asumsi di `src/analysis.py`; keputusan: dipakai/tidak". Setelahnya: entri ditutup dengan hasil verifikasi dan tautan commit.

**Kesalahan khas.** Over-dokumentasi yang membebani tim (solusinya: log hanya untuk penggunaan *material*); terlalu konservatif sehingga tidak memakai AI di tahap yang justru sangat membantu (coding, red team).

**Bukti kompetensi.** Reviewer dapat mengaudit peran AI dari log dan repositori tanpa bertanya ke tim; AI Usage Statement diterima venue/penguji tanpa revisi; mahasiswa mampu mempertahankan bagian yang dibantu AI di defense.

**Kaitan ke rubrik.** Execution *Exemplary*; Research Integrity Gate lulus tanpa catatan.

## 3. Ringkasan empat level

| Aspek | Consumer | Collaborator | Investigator | Governor |
|---|---|---|---|---|
| Hubungan dengan AI | Mesin jawab | Rekan diskusi | Instrumen riset | Sistem yang diatur & diaudit |
| Konteks dalam prompt | Tidak ada | Ada | Ada + artefak riset (card, matriks, log) | Ada + aturan data & verifikasi eksplisit |
| Verifikasi | Tidak | Sesekali, intuitif | Sistematis: sumber → penalaran → bukti | Sistematis + terdokumentasi + dapat diaudit |
| Dokumentasi | Tidak ada | Log tidak konsisten | Log ada, verifikasi tercatat | Log kontemporer + statement dalam metode |
| Siapa bertanggung jawab | "AI bilang" | "Saya sunting" | "Saya verifikasi" | "Saya pertanggungjawabkan" |
| Risiko integritas | Tinggi | Sedang | Rendah | Sangat rendah |
| Status di Metopen | Tidak dapat diterima setelah G1 | Batas bawah S0–W2 | **Minimum lulus** | **Perilaku yang dituntut** |

## 4. Matriks kompetensi × tahap riset

Untuk tiap kelompok tahap value stream ([AIX-03](03-ai-across-research-value-stream.md)), perilaku yang membedakan level:

| Tahap | Consumer | Collaborator | Investigator | Governor |
|---|---|---|---|---|
| Problem | Minta AI "buatkan topik" | Beri konteks, minta 3 framing | Framing diuji ke stakeholder/literatur; yang ditolak dicatat | + aturan: tidak ada klaim masalah tanpa sumber yang bisa dibuka |
| Search & Read | Minta daftar referensi | Minta kata kunci, lalu cari sendiri | AI untuk menemukan; setiap DOI dibuka; ringkasan AI hanya pra-baca | + log verifikasi per sumber; PDF berlisensi tidak diunggah sembarangan |
| Synthesis & Gap | Minta AI menulis related work | Minta AI mengelompokkan tema, lalu sunting | Tema dicocokkan ke baris matriks; AI menantang gap; hasil pencarian ulang dicatat | + gap tidak diterima bila hanya "AI bilang belum ada" |
| RQ & Hypothesis | Pakai RQ dari AI | Iterasi RQ dengan AI | Hipotesis saingan dari AI dipertimbangkan; kriteria penolakan ditulis sendiri | + RQ tertelusur ke matriks, bukan ke percakapan AI |
| Method & Design | Pakai metode "yang disarankan" | Bandingkan alternatif | AI sebagai red team; metrik/baseline ditetapkan dengan justifikasi tim | + deviasi desain setelah hasil diungkap; AI tidak memilih metrik |
| Coding & Experiment | Commit kode AI mentah | Baca & jalankan | Baca, uji, sanity check leakage; log per fungsi material | + tidak ada data mentah/pribadi ke AI; kode AI beratribusi di log |
| Analysis | Terima "interpretasi" AI | Minta penjelasan uji | Semua angka dihitung ulang; asumsi uji dicek | + skrip analisis dapat mereproduksi tabel tanpa AI |
| Writing | Tempel teks AI | Sunting teks AI | Bagian hasil/diskusi ditulis sendiri dari CER; AI hanya bahasa/struktur | + `AI-USAGE.md` sesuai kebijakan venue; bisa menjelaskan tiap bagian tanpa AI |
| Review & Publication | Minta AI menulis review | Minta AI mengkritik draft sendiri | AI reviewer tambahan, diungkap; review tim lain ditulis sendiri | + tidak mengunggah draft orang lain ke AI; kebijakan venue dipatuhi |

## 5. Jalur kenaikan level dalam 16 minggu

| Titik | Harapan level | Bukti |
|---|---|---|
| S0 | Consumer/Collaborator (titik awal jujur) | Self-assessment #1; kuis protokol |
| G1 (W1) | Collaborator, mulai perilaku Governor: agreement ditandatangani, log dimulai | Agreement; entri log pertama |
| G3 (W5) | Investigator pada Search/Read/Synthesis | Semua sumber AI terverifikasi; entri "ditolak" ada |
| G5 (W8) | Investigator pada Method (AI sebagai red team) | Notulen red team; log kritik desain |
| G6 (W10) | Investigator pada Coding/Experiment | Kode AI beratribusi & diuji; tidak ada data ke AI |
| G7 (W12) | Investigator pada Analysis | Angka dihitung ulang; asumsi uji dicek |
| G8 (W16) | **Investigator dengan perilaku Governor** | `AI-USAGE.md` lengkap; self-assessment #3; dapat mempertahankan bagian berbantuan AI di defense |

Self-assessment dilakukan tiga kali (W1, W8, W16) memakai checklist §6 dan dibahas singkat dengan mentor; hasilnya masuk AI Usage Log sebagai entri refleksi. Level bukan nilai; ia diagnosis. Yang dinilai adalah **perilaku yang terbukti di artefak** ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) E5 Execution, CPMK-10).

## 6. Self-assessment checklist

Centang yang **benar-benar Anda lakukan dalam dua minggu terakhir** (bukan yang Anda tahu seharusnya). Hitung per blok.

**Blok A — Consumer (jika sebagian besar ini benar, Anda di level 1)**
```
[ ] Saya pernah memakai referensi dari AI tanpa membuka sumbernya.
[ ] Saya pernah menempel teks AI ke dokumen riset tanpa menyunting substansinya.
[ ] Saya pernah meng-commit kode AI tanpa membacanya sampai selesai.
[ ] Saya tidak punya catatan penggunaan AI untuk minggu ini.
```

**Blok B — Collaborator**
```
[ ] Prompt saya memuat konteks riset (masalah, data, batasan).
[ ] Saya meminta beberapa alternatif dan membandingkannya.
[ ] Saya menyunting output AI secara substansial sebelum memakainya.
[ ] Saya bisa menunjukkan mana ide saya dan mana ide AI.
```

**Blok C — Investigator**
```
[ ] Setiap sumber yang ditemukan lewat AI saya buka dan verifikasi (DOI/URL, isi).
[ ] Saya memakai AI untuk mencari cara riset saya bisa gagal, dan menindaklanjutinya.
[ ] Semua angka/statistik dari AI saya hitung ulang dari data sendiri.
[ ] Kode berbantuan AI saya baca, uji, dan beri sanity check sebelum commit.
[ ] Saya punya entri log berisi output AI yang saya TOLAK beserta alasannya.
[ ] Saya tidak pernah memasukkan data mentah/pribadi/partner ke layanan AI.
```

**Blok D — Governor**
```
[ ] AI Usage Log saya ditulis saat penggunaan, bukan diingat belakangan.
[ ] AI-USAGE.md tim membedakan bantuan penulisan dan bantuan proses riset.
[ ] Saya bisa menjelaskan setiap bagian berbantuan AI tanpa membuka AI.
[ ] Reviewer bisa mengaudit peran AI dari log dan repositori tanpa bertanya ke saya.
[ ] Saya pernah mengoreksi penggunaan AI anggota tim yang tidak sesuai protokol.
[ ] Saya memilih tool berdasarkan kriteria (fungsi, data, verifikasi), bukan kebiasaan.
```

**Interpretasi.** Blok A ada yang tercentang → kembali ke [AIX-04](04-ai-research-protocol.md) dan perbaiki artefak terkait sebelum gate berikutnya. Blok C penuh → Investigator (minimum lulus). Blok C penuh + ≥4 dari Blok D → Investigator dengan perilaku Governor (target).

## 7. Untuk dosen: tanda cepat di review gate

| Tanda di PR/artefak | Kemungkinan level | Tindakan |
|---|---|---|
| Referensi tidak bisa dibuka; angka tanpa sumber | Consumer | Gate gagal (integritas); rujuk AIX-04; remediasi |
| Teks halus tetapi tidak konsisten dengan repositori | Consumer/Collaborator | Minta penjelasan lisan bagian tersebut; cek log |
| Log ada tetapi tanpa kolom verifikasi | Collaborator | Minta lengkapi verifikasi sebelum merge |
| Entri "ditolak" ada; sumber terverifikasi; kode AI diuji | Investigator | Lulus; dorong ke dokumentasi Governor |
| `AI-USAGE.md` dapat diaudit; bagian AI dapat dipertahankan di defense | Governor | Lulus; jadikan contoh anchor untuk kalibrasi rubrik |

Kerangka ini juga dipakai mata kuliah mode E/R ([ARC-03](../02-academic-architecture/03-ai-contribution-modes.md)) dengan target level yang disesuaikan: Collaborator untuk mata kuliah semester 3–4, Investigator untuk semester 5–6, Investigator + Governor untuk Metopen dan TA.
