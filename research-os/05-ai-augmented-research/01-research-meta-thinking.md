# Research Meta-Thinking — Sepuluh Meta-Skill Peneliti Computing

> **ID** AIX-01 · **Paket** 05 AI-Augmented Research & Meta-Thinking · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen & TA, dosen pengampu/mentor studio, dosen mata kuliah mode R, siapa pun yang memakai AI dalam riset
> **Terkait** [AIX-02 AI Research Competency](02-ai-research-competency-framework.md) · [AIX-03 AI Across Value Stream](03-ai-across-research-value-stream.md) · [AIX-04 AI Research Protocol](04-ai-research-protocol.md) · [MET-01 Metopen Positioning](../04-metopen-research-studio/01-metopen-positioning.md) · [MET-03 16-Week Blueprint](../04-metopen-research-studio/03-metopen-16-week-blueprint.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)

## 1. Mengapa meta-thinking

GenAI membuat *eksekusi* murah: kode, ringkasan, draft, tabel, bahkan "hipotesis" bisa diminta dalam hitungan detik. Yang menjadi langka adalah **berpikir tentang berpikir**: tahu masalah apa yang layak dipecahkan, tahu klaim apa yang sedang dibuat, tahu bukti apa yang cukup, tahu kapan diri sendiri (atau AI) sedang menipu diri.

Metopen memilih sepuluh meta-skill yang, bila tidak dimiliki, membuat riset lemah — apa pun tool-nya. Sepuluh ini bukan teori kognisi; ia adalah **alat kerja** yang dilatih di blok konsep (30%) dan dipakai di studio (70%) ([MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)).

| # | Meta-skill | Pertanyaan inti | Minggu utama Metopen | Dimensi 5E |
|---|---|---|---|---|
| 1 | Problem framing | Apa masalah sebenarnya, untuk siapa? | W1–W2 | End |
| 2 | Decomposition | Bagian mana yang bisa dijawab dulu? | W2, W6, W7 | End, Execution |
| 3 | Abstraction | Pola umum apa di balik kasus ini? | W4–W5, W7 | Evidence |
| 4 | First principles | Apa yang benar-benar kita ketahui, bukan asumsi? | W2, W7 | End, Experiment |
| 5 | Hypothesis | Apa yang kita klaim, dan bagaimana bisa salah? | W6 | End |
| 6 | Falsification | Bukti apa yang akan membatalkan klaim? | W6–W8, W12 | Experiment, Explanation |
| 7 | Evidence literacy | Seberapa kuat bukti ini, dan mengapa? | W3–W5, W11 | Evidence |
| 8 | Causal & statistical reasoning | Apakah ini sebab, atau kebetulan? | W7, W11 | Experiment, Explanation |
| 9 | Systems thinking | Bagaimana bagian-bagian saling memengaruhi? | W2, W7, W12 | End, Explanation |
| 10 | Metacognition | Apa yang saya tidak tahu, dan apa yang membuat saya yakin? | setiap minggu | Execution |

Format tiap skill: **Definition → Research Use → Student Mistake → Exercise → AI Role.** Setiap *Exercise* dirancang 15–30 menit, dapat dipakai langsung di blok konsep/studio, menghasilkan artefak kecil yang masuk ke repositori.

---

## 2. Problem framing

**Definition.** Kemampuan menyatakan masalah sebagai kesenjangan antara keadaan sekarang dan keadaan yang diinginkan, dari sudut pandang orang yang mengalaminya — sebelum memikirkan solusi.

**Research Use.** Menentukan Problem Brief dan Stakeholder/Impact Statement (G2). Framing yang benar menentukan literatur apa yang dicari, metrik apa yang bermakna, dan apakah hasil riset akan mengubah keputusan siapa pun.

**Student Mistake.** Memulai dari solusi ("pakai Random Forest untuk memprediksi X"); memilih masalah karena datanya tersedia, bukan karena masalahnya penting; masalah terlalu luas ("pendidikan Indonesia") atau tanpa pemilik.

**Exercise — Rantai Mengapa (20 menit).** (1) Tulis kalimat riset Anda saat ini. (2) Tanyakan "mengapa itu penting?" lima kali berturut-turut; tulis setiap jawaban. (3) Pada tiap level, tulis siapa yang peduli dan keputusan apa yang berubah. (4) Pilih level yang paling konkret sekaligus paling bermakna; tulis ulang masalah tanpa menyebut metode. (5) Uji ke satu orang dari tim lain: bisakah ia mengulang masalah dalam dua kalimat? Output: draft `docs/problem.md` §1.

**AI Role.** *Membantu:* mengajukan sudut pandang stakeholder yang terlewat; menantang apakah kalimat masih solution-first; mengusulkan reframing alternatif untuk dibandingkan. *Jebakan:* AI cenderung membuat masalah terdengar penting dengan bahasa generik dan "statistik" tanpa sumber; AI tidak tahu konteks UAI/Indonesia kecuali Anda memberinya; framing dari AI tidak punya pemilik. Verifikasi dengan stakeholder nyata atau dokumen yang bisa dibuka.

## 3. Decomposition

**Definition.** Memecah masalah besar menjadi sub-masalah yang masing-masing dapat dijawab, diurutkan, dan diuji secara terpisah.

**Research Use.** Mengubah masalah menjadi satu RQ utama dan RQ pendukung yang terbatas (G4); memecah desain menjadi pilot yang layak dalam 2 minggu (G5–G6); menyusun microtask sprint ([OPS-02](../06-execution-os/02-weekly-sprints.md)).

**Student Mistake.** RQ yang sebenarnya lima RQ; pilot yang mencoba menjawab semuanya; tidak tahu bagian mana yang blocking (mis. akses data) sehingga baru ketahuan di W10.

**Exercise — Pohon Pertanyaan (25 menit).** (1) Tulis RQ besar di akar. (2) Turunkan 3–6 sub-pertanyaan yang, bila semuanya terjawab, menjawab akar. (3) Untuk setiap sub-pertanyaan tandai: bukti apa yang menjawabnya, data/artefak apa yang dibutuhkan, berapa lama, apa dependensinya. (4) Lingkari satu sub-pertanyaan yang paling murah dan paling informatif: itu pilot Anda. (5) Tandai dependensi blocking dan masukkan ke Issue. Output: `docs/research-question.md` §Decomposition + daftar Issue.

**AI Role.** *Membantu:* menghasilkan kandidat dekomposisi cepat; mengecek apakah sub-pertanyaan lengkap (MECE) dan mengurutkan dependensi. *Jebakan:* dekomposisi AI cenderung simetris dan "rapi" tetapi tidak tahu mana yang murah/mahal di konteks Anda; ia tidak tahu data Anda belum ada. Pilih dan urutkan sendiri berdasarkan ketersediaan nyata.

## 4. Abstraction

**Definition.** Melihat pola umum di balik kasus-kasus spesifik, dan sebaliknya menurunkan kasus spesifik dari pola umum, dengan sadar apa yang dibuang.

**Research Use.** Mengelompokkan 20 paper ke 4–5 tema dalam synthesis matrix (G3); memetakan masalah lokal ke kelas masalah computing yang sudah punya metode (klasifikasi, ranking, deteksi anomali, rekomendasi, optimasi); memilih metode dari Computing Research Methods Map berdasarkan kelas masalah, bukan tren.

**Student Mistake.** Meringkas paper satu per satu tanpa tema; menganggap masalahnya unik sehingga tidak mencari literatur pada kelas masalah yang sama; atau sebaliknya, abstraksi terlalu tinggi sehingga konteks yang mengubah hasil hilang.

**Exercise — Dua Arah (20 menit).** (1) Ambil 8 baris synthesis matrix. (2) Naik: kelompokkan ke 3 tema dan beri nama tema dengan kata benda abstrak (bukan nama metode). (3) Turun: untuk masalah Anda, tulis "ini adalah kasus dari kelas masalah ___ dengan kekhasan ___ (data, bahasa, skala, konteks)". (4) Tulis apa yang hilang ketika Anda mengabstraksi — itu kandidat ancaman validitas eksternal. Output: tema di `docs/literature-map.md` + kalimat kelas masalah di `docs/research-design.md`.

**AI Role.** *Membantu:* mengusulkan tema/taksonomi awal; menamai kelas masalah dan metode standar untuknya. *Jebakan:* AI mengabstraksi dengan lancar tetapi tidak tahu kekhasan konteks Anda; taksonomi dari AI terasa meyakinkan meski tidak sesuai isi paper. Cocokkan tiap tema dengan baris matriks yang benar-benar Anda baca.

## 5. First principles

**Definition.** Membangun penalaran dari hal-hal yang benar-benar diketahui (definisi, pengukuran, hasil yang terverifikasi), bukan dari analogi, kebiasaan, atau "semua orang memakai ini".

**Research Use.** Memilih baseline paling sederhana ("apa prediktor paling naif?"); menetapkan metrik dari apa yang sebenarnya dibutuhkan stakeholder, bukan dari yang lazim; mempertanyakan asumsi data ("apakah label ini benar-benar mengukur konstruk?").

**Student Mistake.** Memakai metrik/arsitektur karena paper populer memakainya; menganggap "state-of-the-art" otomatis relevan; tidak pernah menjalankan baseline naif sehingga tidak tahu apakah model belajar apa pun.

**Exercise — Daftar Asumsi (15 menit).** (1) Tulis 10 asumsi yang membuat riset Anda bekerja (data representatif, label benar, metrik selaras tujuan, baseline adil, split tidak bocor, dst.). (2) Untuk tiap asumsi tandai: **diketahui** (ada bukti), **diasumsikan** (masuk akal, belum dicek), **tidak tahu**. (3) Untuk yang "diasumsikan/tidak tahu", tulis cara termurah mengeceknya. (4) Pilih dua untuk dicek minggu ini. Output: tabel asumsi di `docs/research-design.md` §Assumptions; dua microtask baru.

**AI Role.** *Membantu:* menjelaskan definisi metrik/metode dari dasar; membantu menurunkan konsekuensi logis dari asumsi. *Jebakan:* AI adalah mesin analogi — ia menjawab dengan "yang lazim", persis lawan first principles; penjelasannya terdengar fundamental meski hanya rangkuman kebiasaan. Minta AI menunjukkan dari mana sebuah "keharusan" berasal, lalu cek sumbernya.

## 6. Hypothesis

**Definition.** Merumuskan dugaan yang spesifik, berarah, dan dapat diuji tentang hubungan antar hal, beserta kondisi yang akan membuat dugaan itu salah.

**Research Use.** RQ/Hypothesis (G4) dan Experiment Card (G5): variabel, arah, ambang yang berarti secara praktis, kriteria penolakan. Hipotesis yang baik menentukan desain; desain tanpa hipotesis menghasilkan angka tanpa makna.

**Student Mistake.** Hipotesis yang tidak bisa salah ("metode M dapat diterapkan untuk X"); hipotesis diubah setelah hasil terlihat (HARKing); tidak ada ambang praktis sehingga perbedaan 0,3% dianggap "lebih baik".

**Exercise — Tiga Hipotesis (20 menit).** (1) Tulis hipotesis utama dalam format: "Pada data D, [intervensi/metode] akan [arah] [metrik] dibanding [baseline] sebesar minimal [Δ], karena [mekanisme]". (2) Tulis hipotesis nol dan satu hipotesis saingan (penjelasan lain untuk hasil yang sama). (3) Tulis apa yang akan Anda lihat bila hipotesis salah. (4) Tulis Δ dan alasannya dari sudut stakeholder. Output: bagian Hypothesis di `docs/research-question.md` dan TPL-09.

**AI Role.** *Membantu:* brainstorming hipotesis alternatif/saingan; memeriksa apakah hipotesis Anda benar-benar bisa salah; menyarankan mekanisme yang perlu dicek di literatur. *Jebakan:* AI menghasilkan hipotesis yang "terdengar ilmiah" tetapi tidak tertelusur ke gap Anda; AI tidak tahu Δ yang berarti bagi stakeholder Anda. Setiap hipotesis harus menunjuk baris matriks dan stakeholder.

## 7. Falsification

**Definition.** Secara aktif mencari bukti yang akan membatalkan klaim sendiri, dan merancang pengujian agar klaim punya kesempatan nyata untuk gagal.

**Research Use.** Threats to Validity (G5, G7); desain kontrol dan baseline yang adil; red team W8; sanity check "hasil terlalu bagus" (leakage); pelaporan hasil negatif. Ini inti amanah epistemik: bersedia dibuktikan salah.

**Student Mistake.** Mencari literatur/hasil yang mendukung saja; menjalankan banyak seed dan melaporkan yang terbaik; menganggap threats to validity sebagai formalitas yang disalin dari buku; menolak kritik red team sebagai "tidak paham konteks".

**Exercise — Pre-mortem (25 menit).** (1) Bayangkan W16: riset Anda dinyatakan gagal/klaimnya salah. (2) Setiap anggota menulis 5 alasan paling mungkin (leakage, data tidak representatif, baseline lemah, metrik salah, bug, confounder, ukuran sampel). (3) Gabungkan, kelompokkan ke 4 jenis validitas. (4) Untuk 3 alasan teratas, rancang pengecekan konkret yang bisa dilakukan sebelum G6. (5) Masukkan ke Threats v1 dengan mitigasi. Output: `docs/research-design.md` §Threats + microtask pengecekan.

**AI Role.** *Membantu:* sangat baik sebagai red team — "berikan 10 cara eksperimen ini bisa menyesatkan"; menyebut ancaman validitas khas untuk jenis metode Anda. *Jebakan:* daftar AI generik dan panjang; ia tidak tahu ancaman yang spesifik pada data/kode Anda; ia juga akan dengan senang hati "meyakinkan" Anda bahwa desain Anda kuat bila Anda bertanya begitu. Tanyakan cara gagal, bukan konfirmasi.

## 8. Evidence literacy

**Definition.** Menilai kekuatan bukti: jenis sumber, desain yang menghasilkannya, ukuran dan representativitas data, konsistensi antar sumber, dan apakah klaim melebihi datanya.

**Research Use.** Kolom "kualitas bukti" dan "keterbatasan" di synthesis matrix (G3); memutuskan sumber mana yang layak menjadi dasar gap; menimbang hasil pilot sendiri (G7) dengan standar yang sama.

**Student Mistake.** Menyamakan blog, preprint, dan paper ter-review; percaya angka dari abstrak; menganggap paper "terkenal" pasti benar; membaca ringkasan AI sebagai membaca paper; memberi bobot sama pada studi 30 sampel dan 30.000 sampel.

**Exercise — Piramida Bukti Lokal (20 menit).** (1) Ambil 6 sumber dari matriks Anda. (2) Untuk masing-masing tulis: jenis (jurnal/konferensi/preprint/laporan/blog), desain (experiment/benchmark/survey/...), ukuran & asal data, apakah ada baseline, apakah kode/data tersedia, apakah hasil direplikasi orang lain. (3) Beri skor kekuatan 1–5 dan alasan satu kalimat. (4) Tandai klaim mana dalam gap Anda yang hanya ditopang sumber berskor ≤2. Output: kolom kualitas di `docs/literature/synthesis-matrix.csv`; revisi bagian Gap Candidates di `docs/literature-map.md`.

**AI Role.** *Membantu:* menjelaskan desain studi yang tidak dikenal; mengekstrak struktur paper sebagai pra-baca; membantu membandingkan metodologi dua paper. *Jebakan:* AI tidak bisa memverifikasi bahwa paper ada atau mengatakan yang ia klaim; ringkasan AI menghaluskan keterbatasan; AI tidak tahu reputasi venue secara andal. Setiap penilaian bukti harus berdasarkan PDF yang Anda buka.

## 9. Causal & statistical reasoning

**Definition.** Membedakan korelasi dari sebab-akibat; memahami variabilitas, ketidakpastian, dan ukuran sampel; tahu kapan perbedaan angka berarti sesuatu dan kapan tidak.

**Research Use.** Desain kontrol dan confounder (G5); pelaporan mean ± deviasi antar seed/fold, interval, uji sederhana bila tepat, effect size (G7); membatasi klaim ("berkorelasi", bukan "menyebabkan"); memilih metrik untuk data tidak seimbang. Standar Metopen: *enough statistics to prevent bad claims* — bukan statistik lanjutan.

**Student Mistake.** Klaim kausal dari data observasional; satu run tanpa variansi; "signifikan" tanpa effect size; accuracy pada data 95:5; membandingkan model dengan baseline yang dievaluasi pada split berbeda; menganggap perbedaan 0,5% sebagai kemajuan tanpa tahu variansinya.

**Exercise — Dua Penjelasan (20 menit).** (1) Ambil satu hasil pilot atau satu klaim dari paper di matriks ("A meningkatkan B"). (2) Tulis dua penjelasan non-kausal yang bisa menghasilkan pola yang sama (confounder, seleksi, kebetulan, leakage, reverse causation). (3) Tulis data/desain apa yang bisa membedakan penjelasan itu. (4) Hitung, dari log Anda, variansi antar seed untuk satu metrik; tulis apakah perbedaan vs baseline lebih besar dari variansi itu. Output: paragraf di `results/analysis.md` §Uncertainty + revisi klaim di CER table.

**AI Role.** *Membantu:* menjelaskan uji/interval/effect size dalam bahasa sederhana; menyarankan analisis yang tepat untuk desain Anda; membantu menulis kode analisis. *Jebakan:* AI dapat "menghitung" angka yang tidak pernah dihitung; ia mengonfirmasi interpretasi yang Anda inginkan; ia sering menyarankan uji yang asumsinya tidak terpenuhi. Semua angka dihitung ulang dari data Anda; asumsi uji dicek.

## 10. Systems thinking

**Definition.** Melihat masalah sebagai sistem: komponen, hubungan, umpan balik, batas, dan konsekuensi tak langsung — termasuk bagaimana intervensi mengubah perilaku sistem.

**Research Use.** Stakeholder/Impact Statement (G2): siapa yang terpengaruh bila prediksi tersedia, insentif apa yang berubah; desain (G5): di mana bias masuk sepanjang pipeline data → model → keputusan; "so what" (G7): dampak di luar metrik. Juga untuk melihat riset sendiri sebagai bagian pipeline Course → Metopen → TA → AI Center.

**Student Mistake.** Mengoptimasi satu metrik tanpa melihat efek samping (mis. model prediksi risiko mahasiswa yang justru menstigma); menganggap data statis padahal perilaku berubah setelah sistem dipakai; batas sistem tidak dinyatakan sehingga klaim generalisasi berlebihan.

**Exercise — Peta Sistem (25 menit).** (1) Gambar komponen: sumber data → pengumpulan → label → model → keputusan → orang yang terdampak → data berikutnya. (2) Tandai di mana bias/leakage/insentif masuk pada tiap panah. (3) Tulis satu umpan balik (bagaimana keputusan mengubah data masa depan). (4) Nyatakan batas sistem yang Anda teliti dan apa yang sengaja di luar batas. (5) Turunkan satu ancaman validitas eksternal dan satu isu etika. Output: bagian Scope di `docs/research-design.md` + figur peta sistem di `figures/` (mis. `figures/system-map.png`; file tambahan di luar struktur minimum TPL-15).

**AI Role.** *Membantu:* memperluas peta dengan komponen/stakeholder yang terlewat; menanyakan konsekuensi orde kedua. *Jebakan:* AI menghasilkan peta sistem yang lengkap secara generik tetapi tidak tahu sistem nyata Anda (siapa sebenarnya membuat keputusan di kampus/partner); peta yang terlalu besar melumpuhkan. Batasi ke apa yang bisa Anda verifikasi dengan stakeholder.

## 11. Metacognition

**Definition.** Kesadaran atas proses berpikir sendiri: apa yang saya tahu, apa yang saya asumsikan, seberapa yakin saya dan mengapa, kapan saya sedang bias, dan kapan saya perlu berhenti dan memeriksa.

**Research Use.** AI Usage Log yang jujur (apa yang saya verifikasi, apa yang tidak); gate check mingguan ("blocker saya apa"); merevisi kontribusi turun bila bukti lemah; menyadari kapan sedang mencari konfirmasi; memilih kapan bertanya ke AI vs ke mentor vs ke data.

**Student Mistake.** Yakin karena "sudah baca banyak" padahal hanya ringkasan; tidak sadar sedang HARKing; mengira memahami kode AI karena berjalan; menunda menyatakan "saya tidak tahu" sampai defense.

**Exercise — Kalibrasi Keyakinan (15 menit, ulangi tiap gate).** (1) Tulis 5 klaim yang Anda pegang tentang riset Anda saat ini (tentang data, literatur, metode, hasil). (2) Beri tingkat keyakinan 50–100% pada masing-masing. (3) Tulis satu bukti yang mendasari keyakinan itu; bila tidak ada, turunkan keyakinan. (4) Simpan; di gate berikutnya buka lagi dan tandai mana yang ternyata salah. (5) Catat pola: pada jenis klaim apa Anda cenderung terlalu yakin? Output: bagian Kalibrasi Keyakinan di jurnal mingguan `docs/journal/wNN.md` dan entri refleksi di AI Usage Log.

**AI Role.** *Membantu:* sebagai cermin — "tanyakan kepada saya 5 pertanyaan yang akan mengungkap apa yang belum saya pahami tentang desain ini"; membantu menyusun refleksi. *Jebakan:* AI sangat baik dalam membuat Anda merasa paham (penjelasan lancar ≠ pemahaman); kemudahan mendapat jawaban menurunkan kebiasaan memeriksa. Uji pemahaman dengan menjelaskan kembali tanpa AI, atau dengan menjalankan/menghitung sendiri.

---

## 12. Cara memakai di studio

| Situasi | Skill yang dipanggil | Latihan |
|---|---|---|
| Tim datang dengan "kami mau pakai metode M" | 1 Problem framing, 4 First principles | Rantai Mengapa, Daftar Asumsi |
| Matriks literatur berupa ringkasan per paper | 3 Abstraction, 7 Evidence literacy | Dua Arah, Piramida Bukti |
| RQ terlalu besar | 2 Decomposition, 5 Hypothesis | Pohon Pertanyaan, Tiga Hipotesis |
| Menjelang Design Defense W8 | 6 Falsification, 9 Systems | Pre-mortem, Peta Sistem |
| Hasil pilot "terlalu bagus" | 6 Falsification, 8 Causal/statistical | Dua Penjelasan |
| Klaim di draft melebihi bukti | 8, 10 Metacognition | Dua Penjelasan, Kalibrasi Keyakinan |
| Setiap gate check | 10 Metacognition | Kalibrasi Keyakinan |

Dosen memilih **satu latihan per blok konsep** sesuai minggu; hasil latihan masuk repositori sehingga menjadi bukti Execution di rubrik ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)). Hubungan skill ini dengan level kompetensi AI ada di [AIX-02](02-ai-research-competency-framework.md); posisi AI pada tiap tahap riset ada di [AIX-03](03-ai-across-research-value-stream.md).

## 13. Self-check singkat mahasiswa

```
[ ] Saya bisa menyatakan masalah tanpa menyebut metode.               (1)
[ ] Saya tahu sub-pertanyaan mana yang pilot dan mana yang TA.         (2)
[ ] Saya tahu kelas masalah computing dari masalah saya.               (3)
[ ] Saya tahu asumsi mana yang sudah dicek dan mana yang belum.        (4)
[ ] Hipotesis saya punya arah, ambang, dan kriteria penolakan.         (5)
[ ] Saya sudah menulis tiga cara riset saya bisa gagal.                (6)
[ ] Saya bisa menyebut sumber terlemah dalam gap saya.                 (7)
[ ] Saya tahu variansi antar seed metrik utama saya.                   (8)
[ ] Saya tahu siapa yang terdampak bila sistem saya dipakai.           (9)
[ ] Saya tahu klaim mana yang saya pegang tanpa bukti kuat.            (10)
```
