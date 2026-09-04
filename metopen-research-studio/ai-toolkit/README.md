# AI Toolkit — Memakai AI dalam Riset Tanpa Dibohongi Olehnya

> **Status** Draft v0.1 (2026-09) · Panduan praktis mahasiswa; protokol lengkap di [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md), katalog tool di [AIX-05 AI Tools Reference](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md), tangga kompetensi di [AIX-02](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md)
> **Terkait** [Studio README](../README.md) · [AIX-03 AI Across Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) · [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md) · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [SECURITY.md](../../SECURITY.md)

Kelas ini **bukan** *AI-free Research Methods* dan **bukan** "pakai ChatGPT bikin proposal". Satu aturan: **AI-augmented, human-accountable science.** AI adalah research copilot, bukan epistemic authority. Setiap output AI yang memengaruhi kesimpulan melewati *source verification → reasoning verification → evidence verification → human accountability*. Kita tidak mendidik orang yang pandai menghasilkan tulisan akademik; kita mendidik orang yang **sulit dibohongi — termasuk oleh AI-nya sendiri**.

## 1. Protokol delapan langkah

```
Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own
```

| Langkah | Yang Anda lakukan | Tanda dilanggar |
|---|---|---|
| **Think** | Tulis 2–3 baris sebelum prompt: tujuan, yang sudah diketahui, dugaan jawaban. Hal yang bisa dikerjakan sendiri dalam 10 menit (membuka DOI, menghitung rata-rata) dikerjakan sendiri | AI adalah langkah pertama untuk setiap pertanyaan; tidak punya dugaan sehingga menerima apa pun |
| **Ask** | Beri konteks riset (masalah, data, batasan, artefak — bukan data mentah), nyatakan peran ("reviewer skeptis"), minta alternatif/kritik yang bisa diverifikasi, bukan "jawaban final" | Prompt satu kalimat; "buatkan bab 2"; data pribadi di prompt |
| **Ground** | Setiap klaim faktual AI dijangkarkan ke sumber yang Anda **buka**; setiap saran ke artefak Anda (matriks, design card, log). Sumber tidak ditemukan → klaim dibuang | Menyalin sitasi dari AI; "menurut literatur" tanpa sumber |
| **Verify** | Tiga lapis: *source* (ada dan mengatakan itu), *reasoning* (valid untuk konteks Anda), *evidence* (hitung/jalankan ulang sendiri). Tulis **apa yang dicek**, bukan "sudah diverifikasi" | Log tanpa kolom verifikasi; angka AI dipakai tanpa dihitung ulang |
| **Challenge** | Selalu tanya "apa yang salah dari jawabanmu?"; pakai AI sebagai red team; catat kritik yang **ditolak** beserta alasan | Hanya bertanya untuk konfirmasi; tidak pernah ada entri "ditolak" |
| **Reproduce** | Apa pun yang AI bantu (kode, analisis, tabel) dapat dijalankan ulang dari repositori oleh orang lain tanpa percakapan AI; kode AI diberi tes | Hasil hanya ada di notebook/chat; kode AI tanpa tes |
| **Disclose** | Catat penggunaan material di AI Usage Log **saat terjadi**; rangkum di `docs/AI-USAGE.md`, bedakan bantuan penulisan vs proses riset | Log diisi belakangan; statement generik "kami menggunakan ChatGPT untuk membantu" |
| **Own** | Anda bertanggung jawab atas setiap kalimat, angka, dan baris kode. Uji diri: bisa dijelaskan tanpa membuka AI? Bila tidak, pelajari atau buang | "AI yang bilang"; tidak bisa menjelaskan kode/analisis sendiri di defense |


## 2. Minggu demi minggu: AI boleh untuk apa, apa yang wajib diverifikasi, tool kategori apa ([AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md); red flags per tahap di [AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md))

| Minggu | AI boleh untuk | Wajib diverifikasi manusia | Tool kategori (AIX-05) |
|---|---|---|---|
| W1 Endgame | Eksplorasi istilah bidang, memetakan sub-area topik, brainstorming kandidat endgame | Kandidat dicek ke backlog/roadmap/dosen; endgame ditulis tim; tidak ada data anggota tim ke AI | General reasoning |
| W2 Problem | Tiga framing problem-first, stakeholder yang terlewat, rantai "mengapa" | Konfirmasi ke stakeholder nyata; tidak ada statistik masalah tanpa sumber; kalimat masalah ditulis ulang tim | General reasoning |
| W3 Search | Kata kunci, sinonim lintas bahasa, string pencarian, kandidat sumber | **AI boleh menemukan, tidak pernah mengutip**: setiap DOI/URL dibuka sebelum masuk `references.bib`; sumber via AI dicatat di log | Deep research, Literature search, Citation intelligence, Reference management |
| W4 Evidence | Orientasi/pra-baca paper yang Anda unggah (sesuai lisensi), tanya-jawab atas dokumen | Bagian metode, hasil, keterbatasan dibaca sendiri; baris matriks merujuk halaman/tabel; peer cross-check 2 baris | Source-grounded synthesis, Reference management |
| W5 Gap | Mengelompokkan tema dari **matriks Anda**; menantang gap ("sudah dijawab di sub-bidang lain?") | Tiap tema menunjuk baris matriks; pencarian ulang tercatat; gap tidak diterima bila hanya "AI bilang belum ada" | General reasoning, Source-grounded synthesis |
| W6 RQ | Variasi rumusan RQ, hipotesis saingan, uji keterjawaban/falsifiabilitas | RQ tertelusur ke matriks, bukan ke percakapan AI; kriteria penolakan ditulis tim; AI tidak memilih RQ | General reasoning |
| W7 Method | Red team desain, penjelasan jenis metode, ancaman validitas, saran kontrol | Metrik/baseline dijustifikasi tim **tanpa** AI; setiap kritik diklasifikasi terima/ubah/tolak dengan alasan | General reasoning |
| W8 Design Defense | Latihan pitch (AI sebagai penanya), antisipasi pertanyaan red team | Jawaban merujuk artefak di repositori; revisi desain dicatat di riwayat Design Card | General reasoning |
| W9 Repository | Coding support, tes, debugging, environment, skrip `run.sh` | Baca seluruh kode; tes/sanity check (split sebelum pra-pemrosesan, ID unik, tidak ada fitur target); log per fungsi material; **tidak ada data mentah/pribadi ke AI** | Coding, Notebooks & compute |
| W10 Pilot | Diagnosis run gagal, usulan pengecekan leakage/distribusi | Hasil hanya sah dari run tercatat (config, seed, log); peer mereproduksi baseline | Coding, Notebooks & compute |
| W11 Analysis | Penjelasan uji & asumsinya, kode plotting, ide error analysis | **Tim menghitung**: semua angka dari skrip di repositori; asumsi uji dicek pada data Anda; interpretasi ditulis tim | Statistics, Coding |
| W12 Contribution | Kritik tabel CER, "so what", klaim terkuat yang tidak boleh dibuat | Klaim menunjuk tabel/figur; kontribusi tidak melebihi bukti; hasil negatif ditulis | General reasoning |
| W13 Manuscript | Bahasa, struktur, konsistensi istilah, umpan balik alur | Hasil/diskusi ditulis tim dari CER; sitasi hanya dari `references.bib`; diungkap di `AI-USAGE.md` | Writing |
| W14 Peer Review | Memeriksa draft **sendiri** dengan checklist TPL-12; menyusun response letter | Review untuk tim lain ditulis sendiri; **draft tim lain tidak diunggah** ke layanan AI | Peer review support |
| W15 Revision | Konsistensi revisi, pengecekan format | Angka yang berubah berasal dari run baru ter-commit; Integrity Checklist diisi manusia | Writing |
| W16 Defense | Latihan menjawab 15 pertanyaan penguji (TPL-13) | Tiap anggota bisa menjelaskan bagian berbantuan AI tanpa AI | General reasoning |

## 3. Larangan

| Dilarang | Mengapa | Akibat |
|---|---|---|
| Memasukkan data pribadi (NIM, nilai, transkrip), data partner, data RESTRICTED, kredensial, atau draft/karya orang lain ke layanan AI | Kebocoran tidak bisa ditarik; melanggar consent dan [SECURITY.md](../../SECURITY.md) | Gate gagal; penanganan sesuai SECURITY.md §5; laporkan ke dosen/pemilik data |
| Referensi buatan AI yang tidak dibuka; angka hasil, tabel, figur, atau data "diperkirakan" AI | Diperlakukan sebagai **fabrikasi** ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)) | Satu referensi tak terverifikasi = G3 gagal; hasil buatan AI = pelanggaran integritas berat |
| Menyerahkan teks/kode AI tanpa verifikasi dan tanpa mampu menjelaskannya | Anda yang menandatangani, bukan AI | Gate gagal; di defense dinilai tidak memiliki riset sendiri |
| Membiarkan AI memilih metrik/baseline/hipotesis setelah melihat hasil | Metric switching / HARKing | G6/G7 gagal; klaim ditarik |
| Meng-commit kode AI yang tidak dibaca/diuji | Kode yang "jalan" sering bocor (leakage) | G6 gagal bila peer tidak bisa mereproduksi atau leakage ditemukan |
| Menulis review tim lain dengan AI; mengunggah draft orang lain | Kerahasiaan dan tanggung jawab reviewer | Komponen Peer Review 0; pelanggaran kode etik |
| Tidak mencatat penggunaan AI yang memengaruhi kesimpulan; menyebut AI sebagai penulis | Yang diungkap adalah praktik; yang disembunyikan adalah pelanggaran | Gate gagal terlepas dari kualitas |

Aturan praktis data: sebelum menempel apa pun ke prompt, tanyakan "kalau teks ini bocor ke publik, apakah ada yang dirugikan?" Jika ya, jangan. PUBLIC boleh; INTERNAL hanya ke layanan dengan kebijakan tidak-melatih/tidak-menyimpan atau model lokal, seizin tim; RESTRICTED **tidak pernah** — pakai skema/ringkasan statistik tanpa nilai atau sampel sintetis ([AIX-05 §4](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md)).

## 4. Mengisi AI Usage Log dan AI Usage Statement (TPL-10)

**Log** (`docs/ai-usage-log.md`, dimulai saat agreement ditandatangani di S0/W1): satu baris per penggunaan **material** — output AI yang masuk (utuh/diubah) ke kode, data, analisis, teks, atau keputusan desain. Tidak wajib untuk pemeriksaan ejaan atau terjemahan istilah tunggal.

| Kolom | Isi yang benar |
|---|---|
| Date · Tool (versi) · Stage | Tanggal penggunaan (hari yang sama); kategori + nama/versi bila diketahui; stage `Problem · Search · Read · Synthesis · Gap · RQ · Method · Coding · Experiment · Analysis · Writing · Review · Publication` |
| Purpose · Prompt / use | Tujuan satu frasa; inti prompt 1–2 baris **tanpa data sensitif** |
| Material output? | Ya/Tidak |
| Verification | `S: … · R: … · E: …` — apa yang dicek dan hasilnya (mis. "3 dari 4 referensi tidak ditemukan → dibuang"; "unit test 12 kasus lulus, commit a1b2c3") |
| Inclusion in final work | Ya / Diubah / Tidak — dengan lokasi konkret (file/section/commit) |
| PJ | Nama anggota yang bertanggung jawab |

Reviewer memeriksa log pada G3 (verifikasi sumber), G6 (kode berbantuan AI), dan G8 (statement lengkap). Log dinilai dari **kejujuran dan kualitas verifikasi**, bukan dari banyak-sedikitnya AI dipakai; entri "ditolak" adalah bukti Anda menilai, bukan menyalin. Contoh tiga entri terisi ada di [examples §(d)](../examples/README.md).

**Statement** (`docs/AI-USAGE.md`, dirakit W13 dari log, difinalkan W16; struktur lengkap di [AIX-04 §4.2](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)): (1) ringkasan tool dan tahap; (2) **AI dalam proses riset** — tahap, bantuan, verifikasi, rujukan nomor log; (3) **AI dalam penulisan** — bagian mana, jenis bantuan; (4) yang TIDAK dilakukan dengan AI (hasil, tabel, figur, interpretasi, review tim lain, pemilihan metrik/baseline); (5) data — tidak ada data pribadi/partner ke layanan AI; (6) pernyataan tanggung jawab — AI bukan penulis. Statement ini menjadi sumber bagian metode dan pengungkapan AI di proposal/manuscript; penggunaan yang memengaruhi kesimpulan dijelaskan di Methods, bukan hanya di catatan kaki.

## 5. AI Research Protocol Agreement (ditandatangani di G1)

Teks lengkap ada di [AIX-04 §5](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md); salin ke `docs/ai-protocol-agreement.md`, isi nama/NIM, tanda tangani bersama dosen pengampu dan mentor. Intinya:

```
Saya, [nama], NIM [isi], anggota tim riset [Research ID / judul sementara], menyatakan bahwa
dalam seluruh kegiatan riset ini saya akan: THINK sebelum bertanya; ASK dengan konteks dan tanpa
data pribadi/partner/RESTRICTED/kredensial/karya orang lain; GROUND setiap klaim AI ke sumber
yang saya buka sendiri; VERIFY sumber, penalaran, dan bukti, lalu mencatatnya; CHALLENGE output AI
dan riset saya sendiri, termasuk mencatat saran yang saya tolak; REPRODUCE setiap hasil berbantuan
AI dari repositori tanpa percakapan AI; DISCLOSE penggunaan AI yang material di AI Usage Log saat
terjadi dan di AI-USAGE.md; OWN setiap kalimat, angka, dan baris kode, dan mampu menjelaskannya
tanpa AI.

Saya memahami bahwa referensi, hasil, atau data dari AI yang tidak diverifikasi diperlakukan
sebagai fabrikasi; penggunaan AI yang memengaruhi kesimpulan dan tidak diungkap membuat gate
gagal; AI adalah research copilot, bukan epistemic authority; amanah epistemik ada pada saya.

Tanda tangan: ______________  Tanggal: ________  Dosen pengampu: ______________  Mentor: ________
```

## 6. Level kompetensi yang dituju

```
AI Consumer  →  AI Collaborator  →  AI Investigator  →  AI Governor
 memakai         memberi konteks       memakai AI untuk     memverifikasi,
                 & mengiterasi         riset (bukti,        mendokumentasikan,
                                       eksperimen)          mempertanggungjawabkan
```

Target Metopen: semua mahasiswa minimal **AI Investigator** (verifikasi sistematis sumber → penalaran → bukti; sumber via AI semuanya terverifikasi; kode AI diuji; ada entri "ditolak"), dengan perilaku **AI Governor** (log kontemporer dan dapat diaudit; `AI-USAGE.md` membedakan penulisan vs proses riset; data sensitif tidak pernah ke AI; bisa mempertahankan bagian berbantuan AI di defense). Consumer tidak dapat diterima setelah G1; Collaborator adalah batas bawah S0–W2.

| Titik | Harapan level | Bukti di artefak |
|---|---|---|
| G1 (W1) | Collaborator, mulai perilaku Governor | Agreement; entri log pertama; self-assessment #1 |
| G3 (W5) | Investigator pada Search/Read/Synthesis | Semua sumber via AI terverifikasi; entri "ditolak" ada |
| G5 (W8) | Investigator pada Method | Notulen red team; log kritik desain terima/tolak; self-assessment #2 |
| G6 (W10) | Investigator pada Coding/Experiment | Kode AI beratribusi & diuji; tidak ada data ke AI |
| G7 (W12) | Investigator pada Analysis | Angka dihitung ulang skrip; asumsi uji dicek |
| G8 (W16) | **Investigator dengan perilaku Governor** | `AI-USAGE.md` lengkap; self-assessment #3; bagian berbantuan AI dipertahankan di defense |

Self-assessment (checklist [AIX-02 §6](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md)) dilakukan di W1, W8, W16 dan dicatat di log sebagai entri refleksi. Level bukan nilai; ia diagnosis. Yang dinilai adalah perilaku yang terbukti di artefak (E5 Execution, [rubrics](../rubrics/README.md)). Tidak ada tool yang diwajibkan; semua kategori punya opsi gratis yang memadai, dan usulan tool baru mengikuti prosedur [AIX-05 §6](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md).
