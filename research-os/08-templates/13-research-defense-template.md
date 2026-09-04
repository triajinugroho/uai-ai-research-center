# Research Defense Template

> **ID** TPL-13 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa (tim presenter), penguji/red team, dosen pengampu, mentor, peer audience
> **Terkait** [OPS-03 G5 & G8](../06-execution-os/03-research-gates.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [MET-04 Research Pack (Research Pitch)](../04-metopen-research-studio/04-research-pack-specification.md) · [TPL-11 Integrity Checklist](11-research-integrity-checklist.md) · [TPL-12 Peer Review](12-peer-review-template.md) · [TPL-14 Handoff](14-research-handoff-template.md) · [Week 16 Defense](../../metopen-research-studio/weeks/week-16-defense.md)

## Cara pakai

Dipakai dua kali: **W8 Design Defense / Red Team Review** (bukti G5; slide 1–4 dan 6 penuh, slide 5 berisi rencana pilot) dan **W16 Research Defense** (bukti G8; semua slide penuh). Tim menyiapkan 7–10 slide sesuai struktur di bawah, menyimpannya di `presentation/` repositori riset, dan berlatih sampai durasi 7–10 menit; tanya jawab 10–15 menit. Penguji (dosen pengampu + mentor + 1 dosen/peer red team) menilai dengan rubrik singkat di bawah dan menuliskan notulen di PR gate. Defense hanya dapat dijadwalkan bila Integrity Checklist ([TPL-11](11-research-integrity-checklist.md)) sudah ditandatangani; lulus defense ditindaklanjuti dengan handoff ([TPL-14](14-research-handoff-template.md)).

## Struktur pitch (7–10 menit, ±9 menit total)

| # | Slide | Durasi | Isi wajib | Sumber di Research Pack |
|---|---|---|---|---|
| 1 | Problem & why it matters | 1 mnt | Fenomena nyata, siapa terdampak, keputusan yang berubah; Research ID + endgame di sudut slide | Problem Brief, Stakeholder statement |
| 2 | What we know & gap | 1,5 mnt | 3 temuan literatur dengan sitasi; pola konsisten/bertentangan/kosong; gap dalam 1 kalimat yang menunjuk matriks | Literature Evidence Map, Research Gap |
| 3 | RQ & contribution | 1 mnt | RQ (maks 2) + hipotesis yang dapat salah; jenis kontribusi | RQ/Hypothesis, Contribution Statement |
| 4 | Method / design | 2 mnt | Jenis metode, unit analisis, variabel, data (Dataset ID, privasi), baseline, metrik, prosedur 1 diagram | Research Design, Data Plan, Baseline & Metrics |
| 5 | Pilot evidence | 2 mnt | Tabel/figur hasil dengan baseline terlihat, variasi antar run, error analysis 1 contoh; hasil negatif disebut; W8: rencana pilot + Experiment Card | Pilot Experiment, Results |
| 6 | Threats & ethics | 1 mnt | 4 threats + mitigasi; consent/anonimisasi; AI Usage Statement 2 kalimat | Threats to Validity, Ethics & Privacy, AI Usage |
| 7 | Next steps / handoff | 0,5 mnt | Apa yang ada, apa yang kurang, langkah TA/paper berikutnya, owner | Reproducibility README, Proposal TA, Handoff |

Boleh ditambah maksimal 2 slide cadangan (backup) untuk tanya jawab: detail data, detail konfigurasi. Slide judul tidak dihitung.

## 15 pertanyaan penguji yang wajib siap dijawab

| # | Pertanyaan | Bukti jawaban ada di |
|---|---|---|
| 1 | Siapa yang peduli pada masalah ini dan keputusan apa yang berubah bila riset berhasil? | Problem Brief |
| 2 | Apa tiga hal yang sudah diketahui literatur, dan di mana literatur bertentangan? | Synthesis matrix |
| 3 | Tunjukkan baris matriks yang menjadi asal gap Anda. | Literature map |
| 4 | Apa yang akan membuat hipotesis Anda salah? | RQ/Hypothesis, Experiment Card |
| 5 | Mengapa metode ini, bukan metode lain dari Methods Map? | Design Card |
| 6 | Apa baseline Anda, dan mengapa itu pembanding yang adil? | Baseline & Metrics |
| 7 | Bagaimana metrik dipilih, dan apakah ditetapkan sebelum melihat data? | Experiment Card pra-registrasi |
| 8 | Bagaimana Anda mencegah leakage? | Experiment Card, src/ |
| 9 | Dari mana data berasal, siapa pemiliknya, dan bagaimana privasi dijaga? | Dataset card, docs/ethics.md |
| 10 | Apakah sampel/dataset merepresentasikan populasi klaim Anda? | Threats eksternal |
| 11 | Apakah perbedaan hasil secara praktis berarti, bukan hanya secara angka? | Analysis, ambang praktis |
| 12 | Apa hasil negatif atau kejutan yang Anda temukan? | Results, EXP cards |
| 13 | Apa yang dilakukan AI dalam riset ini dan bagaimana Anda memverifikasinya? | AI Usage Log & Statement |
| 14 | Bisakah saya mereproduksi angka baseline Anda sekarang dari repositori? | README Reproducibility, peer reproduction |
| 15 | Apa klaim terkuat yang **tidak** boleh Anda buat dari bukti ini? | CER table, Contribution statement |

Latihan: tiap anggota tim menjawab semua 15 pertanyaan dalam ≤ 45 detik per pertanyaan; jawaban selalu menunjuk artefak.

## Rubrik penilaian defense (singkat, selaras 5E)

| Kriteria (5E) | 4 — Kuat | 3 — Memadai | 2 — Lemah | 1 — Tidak ada |
|---|---|---|---|---|
| End — problem & endgame | Orang luar bisa mengulang masalah dan endgame dalam 2 kalimat | Jelas tetapi dampak samar | Solution-first | Tidak jelas |
| Evidence — literatur & gap | Gap ditelusuri ke matriks; sumber terverifikasi | Gap masuk akal, matriks tipis | Gap naratif | Tidak ada |
| Experiment — desain & pilot | Baseline, metrik, kontrol, leakage jelas; pilot direproduksi | Desain jelas, pilot sebagian | Metrik/baseline kabur | Tidak ada pilot |
| Explanation — klaim & threats | CER eksplisit; klaim tidak melebihi bukti; hasil negatif dibahas | Klaim didukung, threats umum | Klaim melebihi bukti | Tidak ada klaim |
| Execution — pitch, repo, integritas | Tepat waktu, artefak ditunjuk langsung, checklist integritas PASS | Sedikit melebihi waktu | Slide tanpa artefak | Integritas gagal → defense gagal |

Keputusan: **Lulus** (rata-rata ≥ 3, tidak ada kriteria 1, integritas PASS) · **Lulus dengan revisi** (rata-rata ≥ 2,5; revisi ≤ 1 minggu) · **Ulang** (ada kriteria 1 atau integritas gagal). Notulen: 3 kekuatan, 3 perbaikan, keputusan, penandatangan.

## Checklist teknis (H-1 dan hari H)

```markdown
- [ ] Slide ≤ 10 (+2 cadangan), tersimpan di presentation/ dan PDF cadangan di Drive kelas
- [ ] Research ID, gate, tanggal, nama tim di slide 1; nomor slide di semua halaman
- [ ] Setiap angka di slide punya sumber (tabel/figur di results/); baseline selalu terlihat di grafik
- [ ] Figur terbaca dari 5 meter (font ≥ 18 pt, tanpa tabel 12 kolom)
- [ ] Sitasi di slide 2 dapat dibuka (DOI/URL disiapkan di slide cadangan)
- [ ] Demo/notebook (bila ada) dijalankan ulang pagi hari H dari repositori bersih
- [ ] Repositori dapat diakses penguji; README Current Research Gate diperbarui
- [ ] Integrity Checklist ditandatangani; AI Usage Statement dicetak/dibuka
- [ ] Pembagian peran presenter dan penjawab pertanyaan ditetapkan; stopwatch disiapkan
- [ ] Latihan penuh ≥ 2 kali dengan waktu; latihan tanya jawab 15 pertanyaan
- [ ] Peralatan: laptop + charger, adaptor HDMI, file offline, koneksi cadangan
```

## Contoh terisi (rencana slide W16, UIAI-2026-001)

| # | Slide | Isi ringkas |
|---|---|---|
| 1 | Problem & why | Dosen wali menangani puluhan mahasiswa; pelanggaran prasyarat dan keterlambatan lulus; stakeholder: mahasiswa, dosen wali, Kaprodi. UIAI-2026-001 · endgame: TA + paper nasional |
| 2 | What we know & gap | 3 temuan (rekomendasi mata kuliah, asisten LLM di konteks Barat, kepercayaan pada saran AI); gap: belum ada evaluasi terkontrol LLM+RAG vs rule-based pada kurikulum Indonesia (M-07, M-12, M-19) |
| 3 | RQ & contribution | RQ1 validitas constraint, RQ2 penilaian dosen wali; H1/H2 dapat salah; kontribusi empiris + artefak (benchmark 40 kasus, prototipe) |
| 4 | Method | Design science + benchmarking + user study kecil; baseline rule-based; metrik violation rate, precision@5, Likert; diagram prosedur 7 langkah; DS-2026-001 restricted |
| 5 | Pilot evidence | Tabel EXP-01/EXP-02: baseline 0 % vs LLM+RAG 7,5 % ± 2,1 pelanggaran; precision 0,31 vs 0,58 ± 0,04; error analysis: batas SKS saat IPK rendah; H1 tidak terdukung, H2 terindikasi |
| 6 | Threats & ethics | Gold label subjektif (2 penilai, κ), 1 prodi, definisi relevansi, n kecil (interval); consent + anonimisasi; AI untuk coding/kritik desain, log 14 entri |
| 7 | Next steps | Ada: repo reproducible, pilot, proposal TA; kurang: evaluasi 80 kasus nyata dengan post-check SKS, user study 6 dosen wali; owner: [Mahasiswa A] (TA), mentor [Dosen C3] |

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Alur | Problem → bukti → RQ → metode → hasil → threats → next, tiap slide 1 pesan | Slide latar belakang 4 halaman, hasil 1 halaman |
| Bukti | Setiap klaim menunjuk tabel/figur; baseline terlihat | Angka tanpa pembanding |
| Kejujuran | Hasil negatif dan keterbatasan disebut sendiri sebelum ditanya | Keterbatasan baru muncul saat ditanya |
| Waktu | 7–10 menit; tanya jawab ≤ 45 detik per jawaban | 15 menit, tanya jawab bertele-tele |
| Tanya jawab | Jawaban menunjuk artefak ("lihat EXP-02 tabel 2") | "Menurut kami…" tanpa bukti |
