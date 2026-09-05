# Design Principles — Konstitusi Sistem

> **ID** STR-03 · **Paket** 01 Strategic Foundation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Semua pengambil keputusan desain: Kaprodi, tim kurikulum, dosen pengampu, AI Research Center, maintainer repo
> **Terkait** [STR-01 Current State & Gaps](01-current-state-and-gaps.md) · [STR-02 Vision & Endgame](02-vision-and-endgame.md) · [ARC-04 Build–Prove–Contribute](../02-academic-architecture/04-build-prove-contribute.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [GOV-01 Governance Model](../07-governance/01-governance-model.md)

Dokumen ini adalah **konstitusi** UAI Informatics Research Pipeline. Setiap dokumen, template, rubrik, kebijakan, dan keputusan operasional di repository ini harus konsisten dengan sepuluh prinsip di bawah. Jika suatu usulan melanggar salah satu prinsip, usulan itu yang direvisi, bukan prinsipnya — kecuali lewat amendemen resmi (§12).

Untuk setiap prinsip: pernyataan, arti, implikasi desain (yang kita lakukan / tidak lakukan), contoh penerapan di repo ini, dan anti-pattern yang harus dikenali.

---

## P1 — One activity, multiple outcomes

**Pernyataan.** Satu aktivitas mahasiswa atau dosen harus menghasilkan beberapa hasil sekaligus: nilai mata kuliah, research asset, evidence OBE/PjBL, bahan TA, kandidat publikasi, dan evidence PP-PTS/akreditasi.

**Arti.** Beban dosen dan mahasiswa terbatas; institusi tidak boleh meminta pekerjaan terpisah untuk setiap tuntutan administratif. Evidence institusional harus menjadi **efek samping** alur kerja riset, bukan pekerjaan tambahan.

**Implikasi desain.**
- Kita lakukan: merancang setiap deliverable agar sekaligus menjadi artefak asesmen, artefak riset, dan evidence pelaporan; menyimpan semuanya di satu tempat (GitHub) dengan satu Research ID.
- Kita tidak lakukan: membuat form laporan terpisah untuk PP-PTS, akreditasi, dan BKD yang menyalin ulang informasi yang sudah ada di Issue/PR/release.

**Contoh di repo.** PR `GATE REVIEW: Method Ready` adalah sekaligus penilaian rubrik 5E (MET-06), bukti CPMK (ARC-05), notulen review ilmiah, dan evidence PjBL untuk [GOV-05](../07-governance/05-ppts-and-institutional-evidence.md).

**Anti-pattern.** "Kumpulkan proposal ke dosen, upload lagi ke LMS, isi lagi form monitoring, lalu buat lagi laporan PP-PTS." Empat pekerjaan untuk satu informasi.

## P2 — Reuse before create

**Pernyataan.** Sebelum membuat dataset, kode, literature map, atau problem baru, periksa dulu apa yang sudah ada di registry, backlog, dan repository angkatan sebelumnya.

**Arti.** Riset yang selalu mulai dari nol tidak pernah menjadi dalam. Institusi menjadi lebih pintar hanya jika hasil sebelumnya dipakai ulang.

**Implikasi desain.**
- Kita lakukan: mewajibkan pencarian di [`datasets-registry/`](../../datasets-registry/README.md), [`research-backlog/`](../../research-backlog/README.md), dan [`publications/`](../../publications/README.md) pada G1–G2; menyediakan handoff ([TPL-14](../08-templates/14-research-handoff-template.md)) agar riset lanjutan mewarisi gate.
- Kita tidak lakukan: menilai lebih tinggi riset yang "membuat dataset sendiri" jika dataset serupa sudah ada dan cukup.

**Contoh di repo.** Entry door *Dataset* dan *Faculty Research* di Mission Control; riset lanjutan boleh melewati gate yang sudah diwarisi dari handoff (aturan 1 di [OPS-03](../06-execution-os/03-research-gates.md)).

**Anti-pattern.** Lima TA berturut-turut mengumpulkan ulang dataset sentimen yang sama karena tidak ada yang tahu dataset itu pernah ada.

## P3 — Build → Prove → Contribute

**Pernyataan.** Mata kuliah teknis **membangun** research asset; Metopen **membuktikan** kualitas bukti; TA **berkontribusi** pengetahuan/artefak. Tiga tahap, satu pipeline.

**Arti.** Setiap mata kuliah punya peran yang jelas dan terbatas. Tidak semua MK harus melakukan penelitian besar; Metopen tidak harus mengajarkan coding; TA tidak harus mulai dari pencarian judul.

**Implikasi desain.**
- Kita lakukan: menandai setiap MK dengan mode F/E/R ([ARC-03](../02-academic-architecture/03-ai-contribution-modes.md)); menetapkan kriteria handoff antar tahap ([ARC-04](../02-academic-architecture/04-build-prove-contribute.md)); menjadikan Research Pack sebagai kontrak antara Metopen dan TA.
- Kita tidak lakukan: mengubah AI/ML menjadi kelas metodologi, atau mengubah Metopen menjadi kelas pemrograman.

**Contoh di repo.** Struktur [`research-based-learning/courses/`](../../research-based-learning/README.md) (Build) → [`metopen-research-studio/`](../../metopen-research-studio/README.md) (Prove) → `final-project` (Contribute), dengan Research ID yang sama mengalir di ketiganya.

**Anti-pattern.** Proyek AI/ML yang dinilai sebagai "penelitian" padahal tidak ada RQ; atau Metopen yang meminta mahasiswa "membuat sistem" alih-alih membuktikan klaim.

## P4 — Scientific thinking over academic formatting

**Pernyataan.** Yang dinilai adalah kualitas berpikir ilmiah (problem, evidence, claim, validity), bukan kepatuhan format dokumen.

**Arti.** Proposal yang rapi tetapi tanpa baseline lebih buruk daripada catatan sederhana dengan RQ yang tervalidasi dan pilot yang berjalan. Format diperlukan hanya pada tahap akhir (Proposal TA, manuscript) dan itu pun mengikuti venue/institusi, bukan diajarkan sebagai inti.

**Implikasi desain.**
- Kita lakukan: rubrik 5E menilai End, Evidence, Experiment, Explanation, Execution ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)); gate menanyakan "bisakah orang lain menjalankan desain ini?" bukan "apakah margin sudah benar?".
- Kita tidak lakukan: memberi bobot nilai untuk tata letak, jumlah halaman, atau jumlah referensi.

**Contoh di repo.** Kriteria lulus G5: *"orang lain dapat menjalankan desain ini tanpa bertanya ke tim"*; kriteria gagal G2: *"masalah hanya justifikasi untuk algoritma yang sudah dipilih"*.

**Anti-pattern.** Minggu penuh membahas format sitasi sementara mahasiswa belum bisa menyebut baseline risetnya.

## P5 — AI augments, human owns

**Pernyataan.** AI boleh dipakai di setiap tahap riset sebagai *research copilot*, tetapi manusia memverifikasi, mendokumentasikan, mengungkap, dan mempertanggungjawabkan setiap keputusan. AI bukan otoritas epistemik.

**Arti.** Kelas *AI-free* tidak realistis; kelas "pakai ChatGPT bikin proposal" tidak dapat dipertanggungjawabkan. Sweet spot-nya: **AI-augmented, human-accountable science**, selaras dengan kebijakan publikasi yang mewajibkan pengungkapan AI yang memengaruhi kesimpulan.

**Implikasi desain.**
- Kita lakukan: protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)); AI Usage Log wajib ([TPL-10](../08-templates/10-ai-usage-log-template.md)); AI Usage Statement di Research Pack; target kompetensi minimal *AI Investigator* dengan perilaku *AI Governor* ([AIX-02](../05-ai-augmented-research/02-ai-research-competency-framework.md)).
- Kita tidak lakukan: melarang AI; atau sebaliknya menerima output AI tanpa verifikasi sumber, penalaran, dan bukti.

**Contoh di repo.** G3 gagal jika ada satu referensi yang tidak dapat diverifikasi, termasuk yang ditemukan lewat AI; setiap gate memiliki Research Integrity check.

**Anti-pattern.** Literature review berisi 20 referensi yang tidak pernah dibuka; kode eksperimen yang tidak dipahami penulisnya sendiri.

## P6 — Evidence before claim

**Pernyataan.** Tidak ada klaim tanpa bukti yang ditunjuk secara spesifik; tidak ada RQ sebelum evidence synthesis; tidak ada eksperimen sebelum baseline dan metrik ditetapkan.

**Arti.** Urutan gate bukan birokrasi; ia mencegah riset yang menghasilkan angka yang tidak menjawab apa pun. Ini juga inti amanah epistemik: mencari kebenaran, bukan membela hipotesis.

**Implikasi desain.**
- Kita lakukan: gate berurutan ([OPS-03](../06-execution-os/03-research-gates.md)); dependency eksplisit di [OPS-04](../06-execution-os/04-dependency-and-critical-path.md); struktur Claim–Evidence–Reasoning wajib di G7; hasil negatif wajib dilaporkan.
- Kita tidak lakukan: membiarkan tim "lompat ke eksperimen dulu, literatur belakangan"; atau mengubah metrik setelah melihat hasil.

**Contoh di repo.** *"RQ tidak boleh dianggap validated sebelum evidence synthesis."* *"Experiment tidak jalan sebelum metric dan baseline defined."* Keduanya adalah aturan blocking di WBS.

**Anti-pattern.** "Akurasi 93%" tanpa baseline, tanpa pembanding, tanpa threats to validity.

## P7 — Publication oriented, not publication obsessed

**Pernyataan.** Riset dirancang mundur dari venue target agar kualitasnya layak publikasi, tetapi publikasi bukan kewajiban semua mahasiswa dan bukan ukuran tunggal keberhasilan.

**Arti.** Backward design meningkatkan kualitas (format, baseline, reproducibility) bahkan bagi riset yang berakhir sebagai TA. Obsesi publikasi memicu jurnal predator, *salami slicing*, dan gaming.

**Implikasi desain.**
- Kita lakukan: publication backward design ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)); venue registry dengan kriteria non-predator ([TPL-06](../08-templates/06-publication-venue-registry-template.md)); level outcome TA Ready sebagai syarat lulus, Publication Ready sebagai aspirasi.
- Kita tidak lakukan: menjadikan "submit paper" sebagai syarat kelulusan Metopen; menghitung publikasi di venue yang tidak lolos registry sebagai KPI.

**Contoh di repo.** KPI lagging menghitung *acceptance* di venue terdaftar, bukan *submission* semata ([GOV-03](../07-governance/03-kpi-and-measurement.md)); risiko `predatory journal` dan `publication gaming` ada di [GOV-04](../07-governance/04-risk-register.md).

**Anti-pattern.** Sepuluh naskah dikirim ke jurnal berbayar tanpa review agar "KPI publikasi" tercapai.

## P8 — Multiple entry points, one pipeline

**Pernyataan.** Riset boleh masuk lewat Problem, Dataset, Faculty Research, Course Project, Partner, atau Competition. Apa pun pintunya, gate, template, dan Research ID-nya sama.

**Arti.** Mahasiswa dan dosen punya konteks berbeda; sistem harus menerima semuanya tanpa menurunkan standar bukti.

**Implikasi desain.**
- Kita lakukan: field *Entry Door* di Mission Control; Issue *Research Problem* sebagai pintu universal ([CONTRIBUTING.md](../../CONTRIBUTING.md)); marketplace demand–supply di [AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md).
- Kita tidak lakukan: membuat alur terpisah untuk "riset dosen", "riset lomba", dan "riset TA" dengan standar berbeda.

**Contoh di repo.** Riset dari lomba tetap harus lolos G2 (problem nyata) dan G5 (baseline & metrik) sebelum diakui sebagai riset, bukan sekadar produk.

**Anti-pattern.** Riset partner yang langsung "dianggap lolos" semua gate karena datanya menarik.

## P9 — Backend detailed, frontend simple

**Pernyataan.** Sistem boleh sangat rinci di belakang (145 microtask, 17 sprint, 8 gate, 15 template), tetapi yang dilihat mahasiswa setiap minggu harus sederhana: This Week → Tasks → Deliverable → AI Assist → Human Check → Done When.

**Arti.** Kompleksitas adalah tanggung jawab desainer, bukan beban pengguna. Pimpinan tidak perlu melihat microtask; mahasiswa tidak perlu membaca theory of change.

**Implikasi desain.**
- Kita lakukan: dua view (A Institutional, B Student Execution — [MST-00 §9](../00-master/00-readme.md)); halaman mingguan [`metopen-research-studio/weeks/`](../../metopen-research-studio/weeks/week-01-endgame.md) yang hanya menampilkan 5–10 task per sprint (umumnya 7–10); tier dokumen.
- Kita tidak lakukan: memberi mahasiswa file WBS 145 baris pada minggu pertama; atau memaksa pimpinan membaca template.

**Contoh di repo.** [OPS-05 Student Weekly Playbook](../06-execution-os/05-student-weekly-playbook.md) adalah *frontend*; [OPS-01 Research WBS](../06-execution-os/01-research-wbs-master.md) adalah *backend*.

**Anti-pattern.** Dashboard dengan 30 kolom yang tidak pernah dibuka mahasiswa.

## P10 — Research assets should compound

**Pernyataan.** Setiap riset harus meninggalkan sesuatu yang dapat dipakai riset berikutnya: dataset terdaftar, kode reproducible, literature map, problem brief, benchmark, atau handoff.

**Arti.** Inilah mekanisme compounding loop ([STR-02 §6](02-vision-and-endgame.md)). Riset yang tidak meninggalkan asset adalah riset yang harus diulang.

**Implikasi desain.**
- Kita lakukan: mewajibkan reproducibility package di G6; registry dataset/publikasi/artefak; handoff di G8; lisensi yang memungkinkan reuse ([LICENSING.md](../../LICENSING.md)); repository standar ([TPL-15](../08-templates/15-research-repository-template.md)).
- Kita tidak lakukan: menerima Research Pack yang komponennya hanya ada di laptop; menutup repo riset tanpa handoff.

**Contoh di repo.** Kriteria lulus G8: *"dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol."*

**Anti-pattern.** Proposal.pdf yang menjadi satu-satunya jejak riset setelah mahasiswa lulus.

---

## 11. Cara memakai prinsip saat ada konflik keputusan

Prinsip kadang saling menarik. Gunakan urutan berikut.

### 11.1 Prosedur

1. **Tuliskan keputusannya** dalam satu kalimat dan sebutkan prinsip mana yang mendukung dan mana yang tertekan.
2. **Cek integritas dulu.** Jika salah satu opsi melanggar Research Integrity (fabrikasi, sitasi palsu, AI tidak diungkap, data sensitif ke GitHub), opsi itu gugur tanpa diskusi. Integritas berada di atas semua prinsip.
3. **Cek endgame.** Opsi mana yang lebih mendekatkan mahasiswa ke TA Ready/Research Ready ([STR-02](02-vision-and-endgame.md))? Prinsip adalah alat; endgame adalah tujuan.
4. **Terapkan urutan prioritas** di §11.2.
5. **Catat keputusan** sebagai *decision record* singkat di PR/Issue terkait (konteks, opsi, prinsip yang menang, alasan), agar keputusan berikutnya konsisten.

### 11.2 Urutan prioritas saat bentrok

| Prioritas | Prinsip | Alasan |
|---|---|---|
| 1 | P5 AI augments, human owns · P6 Evidence before claim | Menjaga kredibilitas pengetahuan; tanpa ini sistem tidak layak disebut riset |
| 2 | P3 Build → Prove → Contribute · P8 Multiple entry points, one pipeline | Menjaga integritas arsitektur; kalau dilanggar, pipeline pecah menjadi jalur-jalur |
| 3 | P4 Scientific thinking over formatting · P10 Assets compound | Menjaga nilai jangka panjang |
| 4 | P1 One activity, multiple outcomes · P2 Reuse before create · P9 Backend detailed, frontend simple | Menjaga efisiensi dan keberlanjutan |
| 5 | P7 Publication oriented, not obsessed | Pengarah, bukan pembatas |

### 11.3 Contoh konflik yang sudah diputuskan

| Konflik | Prinsip yang bentrok | Keputusan | Alasan |
|---|---|---|---|
| Mahasiswa ingin memakai dataset partner yang sangat menarik tetapi belum ada perjanjian privasi | P8 (terima entry door Partner) vs integritas/privasi | Riset boleh masuk backlog, tetapi G5 tidak lolos sampai Data Plan dan Ethics jelas; data mentah tidak masuk GitHub | Integritas di atas prinsip |
| Waktu 2 SKS tidak cukup untuk literature review yang "lengkap" | P6 (evidence dulu) vs P9 (sederhana) | 15–25 sumber primer dalam synthesis matrix, bukan systematic review penuh | Sweet spot: cukup bukti untuk mencegah klaim buruk |
| Dosen ingin menambah laporan mingguan terpisah untuk monitoring | P1 (satu aktivitas) vs kebutuhan monitoring | Monitoring memakai Mission Control dan PR gate yang sudah ada; tidak ada form baru | P1 menang; kebutuhan dipenuhi tanpa pekerjaan tambahan |
| Tim ingin langsung eksperimen karena kode sudah ada dari AI/ML | P2 (reuse) vs P6 (evidence dulu) | Kode boleh dipakai (reuse), tetapi eksperimen "resmi" menunggu baseline & metrik di G5; kode lama dicatat sebagai research asset | Keduanya dipenuhi dengan urutan yang benar |
| Kaprodi ingin KPI "jumlah submission" | P7 vs tekanan institusional | KPI menghitung acceptance di venue terdaftar; submission dicatat sebagai leading indicator saja | Mencegah gaming |
| Mahasiswa ingin AI menulis bagian related work | P5 vs efisiensi | Boleh untuk draft struktur, dengan setiap kalimat klaim ditelusuri ke sumber yang dibaca dan dicatat di AI Usage Log | Human owns |

## 12. Amendemen prinsip

Prinsip dapat diubah hanya lewat PR ke dokumen ini yang (a) menjelaskan konflik nyata yang tidak terselesaikan oleh §11, (b) direview `@maintainers` dan tim kurikulum, (c) disetujui Kaprodi, dan (d) dicatat di [CHANGELOG.md](../../CHANGELOG.md) dengan versi minor baru. Perubahan prinsip wajib diikuti audit dokumen yang merujuknya.

Prinsip-prinsip ini diturunkan langsung dari gap di [STR-01](01-current-state-and-gaps.md) dan endgame di [STR-02](02-vision-and-endgame.md); alignment institusionalnya ada di [STR-04](04-alignment-map.md).
