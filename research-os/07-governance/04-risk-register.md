# Risk Register — Risiko, Sinyal Dini, Mitigasi

> **ID** GOV-04 · **Paket** 07 Governance & Implementation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, kepala AI Research Center, dosen pengampu Metopen, tim kurikulum, admin riset, reviewer hibah
> **Terkait** [GOV-01 Governance Model](01-governance-model.md) · [GOV-03 KPI](03-kpi-and-measurement.md) · [STR-05 Theory of Change](../01-strategic-foundation/05-theory-of-change.md) · [MET-07 Research Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [SECURITY.md](../../SECURITY.md)

Register ini mencatat risiko yang dapat memutus rantai sebab-akibat di [STR-05](../01-strategic-foundation/05-theory-of-change.md). Setiap risiko memiliki ID tetap (`RSK-NN`, tidak dipakai ulang), skor, sinyal dini yang sebagian besar berupa KPI di [GOV-03](03-kpi-and-measurement.md), mitigasi (mencegah), contingency (jika terjadi), dan pemilik. Risiko riset per proyek (bottleneck teknis satu tim) **tidak** dicatat di sini, melainkan sebagai Issue `type:research-risk` di repo riset masing-masing.

---

## 1. Skala penilaian

| Skor | Likelihood (L) | Impact (I) |
|---|---|---|
| 1 | Sangat jarang (<10% per semester) | Gangguan kecil, terserap tanpa perubahan rencana |
| 2 | Jarang (10–30%) | Satu tim/aktivitas terhambat |
| 3 | Mungkin (30–50%) | Beberapa tim/satu fase terhambat; KPI meleset |
| 4 | Sering (50–75%) | Satu fase gagal exit criteria; reputasi Prodi terancam |
| 5 | Hampir pasti (>75%) | Pipeline berhenti; integritas/kepercayaan institusi rusak |

**Skor risiko = L × I.** Kategori: 1–6 rendah (pantau), 8–12 sedang (mitigasi aktif), 15–25 tinggi (mitigasi + contingency siap, dilaporkan ke Kaprodi setiap bulan).

## 2. Register

| ID | Risiko | Deskripsi | L | I | Skor | Early warning signal | Mitigasi | Contingency | Owner |
|---|---|---|---|---|---|---|---|---|---|
| **RSK-01** | Overload mahasiswa & dosen | 2 SKS tidak cukup untuk 16 minggu studio + 8 gate; dosen pengampu kewalahan mereview semua PR; mahasiswa mengerjakan MK lain bersamaan | 4 | 4 | **16** | KPI-L-05 <70%; sprint dengan >30% task tertunda; mahasiswa melewatkan sprint review; PR gate menumpuk >5 hari | Sprint 7–10 task saja; sweet spot bukan frontier (15–25 sumber, pilot pada subset data); review asinkron via PR; peer review & peer reproduction mengurangi beban dosen; asisten riset membantu triase; S0 onboarding memangkas friksi teknis | Kurangi cakupan pilot (subset lebih kecil, baseline saja); geser G6 ke W11; tambah reviewer dari `@reviewers`; untuk semester berikutnya usulkan pengakuan beban dosen | Dosen pengampu; Kaprodi |
| **RSK-02** | Fake AI research | Mahasiswa memakai GenAI menghasilkan referensi fiktif, literature review tanpa membaca, kode yang tidak dipahami, atau klaim yang "terdengar ilmiah"; kepercayaan pada Research Pack runtuh | 4 | 5 | **20** | KPI-Q-02 <95% pada audit sampel W5; AI Usage Log kosong (KPI-L-07 rendah); mahasiswa tidak dapat menjelaskan kode/klaimnya saat sprint review; referensi tanpa DOI/URL | Protokol AIX-04 wajib sejak S0; G3 gagal jika satu referensi tak terverifikasi; AI Usage Log tiap sprint; pertanyaan lisan acak "jelaskan baris ini" di sprint review; integrity check pada setiap gate; target kompetensi AI Investigator/Governor | Gate dibatalkan dan diulang dari G3; kasus terkonfirmasi ditangani prosedur [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md); audit seluruh referensi tim terkait; pelatihan ulang protokol untuk kelas | Dosen pengampu; Kaprodi (insiden) |
| **RSK-03** | Predatory journal | Tekanan publikasi mendorong submission ke jurnal/konferensi predator; publikasi tercatat tetapi merusak reputasi | 3 | 4 | **12** | Usulan venue tidak ada di venue registry; biaya publikasi diminta sebelum review; waktu review <2 minggu; KPI-Q-06 >0 | Venue registry non-predator ([TPL-06](../08-templates/06-publication-venue-registry-template.md)) wajib pada backward design ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)); KPI-G hanya menghitung venue terdaftar; mentor menyetujui venue sebelum submission | Tarik naskah bila belum terbit; jika terbit, tidak dihitung dalam KPI dan dicatat sebagai lesson learned; perbarui registry dengan daftar hitam | AI Research Center; mentor |
| **RSK-04** | Plagiarism | Salin-tempel teks/kode/ide tanpa atribusi, termasuk self-plagiarism dari proyek MK sebelumnya dan parafrase AI tanpa sumber | 3 | 5 | **15** | Kemiripan tinggi pada pemeriksaan sampel; kalimat tanpa sitasi pada klaim faktual; kode tanpa atribusi lisensi | Integrity checklist [TPL-11](../08-templates/11-research-integrity-checklist.md) sebelum defense/submission; pemeriksaan kemiripan pada W13 manuscript; ajarkan atribusi kode/lisensi ([LICENSING.md](../../LICENSING.md)); reuse asset dicatat eksplisit (bukan disembunyikan) | Prosedur [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md); gate G8 gagal; sanksi akademik sesuai aturan universitas; naskah tidak di-submit | Dosen pengampu; Kaprodi |
| **RSK-05** | Faculty resistance | Dosen menolak format studio, review via PR, atau penandaan F/E/R karena dianggap beban tambahan tanpa pengakuan | 3 | 4 | **12** | Mentor tidak merespons PR >5 hari; MK enggan menandai mode; komentar "ini bukan tugas saya" di rapat; KPI-L-08 <100% | Mode F/E/R (tidak semua MK riset besar); pengakuan beban mentor ([MST-01 §6](../00-master/01-executive-summary.md) butir 7); pilot satu kelas dulu; quick wins 90 hari ([GOV-02 §4](02-implementation-roadmap.md)); dosen lain dilibatkan sebagai red team W8 (sosialisasi lewat praktik); Faculty Portfolio memberi manfaat langsung (BKD, hibah) | Pilot berjalan dengan dosen yang bersedia saja; Phase 3 ditunda sampai exit criteria Phase 2; Kaprodi memfasilitasi dialog beban kerja | Kaprodi; tim kurikulum |
| **RSK-06** | Fragmentation kembali | Setelah pilot, riset kembali tersebar: repo di akun pribadi, dataset di laptop, proposal di Drive, ID tidak dipakai | 3 | 4 | **12** | KPI-L-06 <80%; Research ID tidak muncul di judul Issue/proposal TA; dataset baru tanpa `DS-`; RPS versi Drive berbeda dari GitHub | Research ID sebagai primary key sejak G2; satu Mission Control; handoff wajib; registry sebagai syarat gate (G5 Data Plan); master dokumen di GitHub; admin riset memantau bulanan | Audit dan migrasi repo/dataset ke organization; Research ID diberikan retroaktif; reminder di evaluasi semester | Admin riset (`@maintainers`) |
| **RSK-07** | Administrative burden | Tuntutan laporan PP-PTS/akreditasi/BKD berubah menjadi form paralel yang menyalin ulang data GitHub | 3 | 3 | **9** | Permintaan "isi form ini" yang datanya sudah ada di Issue/PR; dosen menghabiskan >2 jam/bulan untuk laporan manual | Prinsip P1; ekspor evidence dari GitHub ([GOV-05 §3](05-ppts-and-institutional-evidence.md)); laporan KPI satu halaman; otomasi ekspor setelah alur stabil | Admin riset menyusun laporan dari ekspor, bukan meminta dosen mengisi ulang; usulkan format laporan ke unit terkait | Admin riset; Kaprodi |
| **RSK-08** | Publication gaming | KPI publikasi dikejar lewat salami slicing, honorary authorship, atau memaksa semua mahasiswa submit | 2 | 4 | **8** | Beberapa `PUB-` dari satu Research ID dengan kontribusi tumpang tindih; daftar penulis tidak sesuai kontribusi di git; KPI-G-01 naik tajam tanpa KPI-I-04 | P7 *publication oriented, not obsessed*; KPI-G hanya menghitung acceptance di venue terdaftar; authorship mengikuti kontribusi tercatat; Publication Ready bukan syarat lulus; anti-gaming di [GOV-03 §6](03-kpi-and-measurement.md) | Naskah ditinjau ulang oleh AI Center sebelum submission; KPI direvisi bila memicu gaming | AI Research Center; Kaprodi |
| **RSK-09** | Research quality inconsistency | Standar gate berbeda antar reviewer/mentor/kelas; Research Pack angkatan A jauh lebih lemah dari angkatan B | 3 | 3 | **9** | Variansi skor 5E antar reviewer tinggi pada tim sebanding; keluhan mahasiswa "reviewer X lebih keras"; TA supervisor menolak Research Pack yang lolos G8 | *Definition of done* eksplisit ([OPS-03](../06-execution-os/03-research-gates.md)); rubrik 5E dengan deskriptor ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)); kalibrasi reviewer di awal semester (menilai 2 contoh bersama); audit sampel PR gate per semester; contoh Research Pack di [`metopen-research-studio/examples/`](../../metopen-research-studio/examples/README.md) | Review ulang tim yang terdampak oleh reviewer kedua; revisi deskriptor rubrik | Dosen pengampu; tim kurikulum |
| **RSK-10** | Data privacy & data sensitif | Data pribadi/partner/kesehatan masuk GitHub atau dipakai tanpa consent/perjanjian; pelanggaran hukum dan etika | 2 | 5 | **10** | File data mentah di commit; dataset tanpa field Privacy/License di registry; riset human subjects tanpa `docs/ethics.md` | [SECURITY.md](../../SECURITY.md): data mentah tidak pernah ke GitHub; registry hanya metadata; Ethics & Privacy wajib di G5; kartu dataset dengan consent/lisensi; `.gitignore` data di [TPL-15](../08-templates/15-research-repository-template.md); pemeriksaan pada PR gate | Hapus data dari history (force-push oleh maintainer), rotasi akses, laporkan ke pemilik data/komite etik; riset dihentikan sampai perjanjian jelas | Pengelola registry; AI Research Center; `@maintainers` |
| **RSK-11** | Tool obsolescence | AI tools, platform, atau fitur GitHub berubah/hilang; materi dan protokol menjadi usang | 3 | 2 | **6** | Tool di contoh [AIX-05](../05-ai-augmented-research/05-ai-tools-reference.md) tidak tersedia; workflow gagal; mahasiswa memakai tool di luar daftar tanpa protokol | Katalog tool **kategorikal** (kategori tetap, contoh tool berganti); protokol AIX-04 agnostik tool; otomasi hanya setelah alur manual stabil; tinjau AIX-05 tiap semester | Ganti contoh tool lewat PR; protokol dan gate tidak berubah | Admin riset; dosen pengampu |
| **RSK-12** | Mentor capacity | Jumlah dosen yang mampu/bersedia menjadi mentor lebih sedikit dari jumlah tim; rasio >5 tim per mentor; review G4–G8 menjadi bottleneck | 4 | 4 | **16** | KPI-L-08 <100% di W2; mentor dengan >5 tim; PR G4/G5 menunggu >5 hari; mentor tidak hadir red team | Faculty research map untuk menemukan adjacency AI dari kepakaran existing ([AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md)); mentor lintas klaster; peer review & red team mengurangi beban; asisten riset sebagai co-reviewer; pengakuan beban; pada pilot dosen pengampu boleh merangkap mentor | Batasi jumlah tim per semester sesuai kapasitas mentor; mentor eksternal (alumni, partner) sebagai reviewer tambahan lewat `@reviewers`; gate G4 direview dosen pengampu saja | AI Research Center; Kaprodi |
| **RSK-13** | Ketergantungan pada satu orang | Sistem bergantung pada satu dosen penggagas/pengampu; jika berhalangan, pipeline berhenti | 3 | 4 | **12** | Semua PR gate direview satu orang; tidak ada `@maintainers` kedua; dokumen hanya dipahami satu orang | Organisasi berdasarkan sistem bukan orang; minimal 2 `@maintainers`; onboarding peran ([GOV-01 §6](01-governance-model.md)); Lecturer Playbook di Phase 3; dokumentasi lengkap di GitHub | Kaprodi menunjuk pengganti; playbook dan Research OS menjadi pegangan | Kaprodi |
| **RSK-14** | Fakta institusional tidak terverifikasi | Dokumen formal mengutip akreditasi, kurikulum, skema penelitian, atau benchmark dari dokumen diskusi yang ternyata tidak akurat | 3 | 3 | **9** | Dokumen Tier 1 dikompilasi ke DOCX tanpa catatan verifikasi; angka berbeda dengan dokumen resmi | Setiap fakta institusional diberi label "verifikasi sebelum dokumen formal"; butir 9 [MST-01 §6](../00-master/01-executive-summary.md); admin riset memverifikasi sebelum kompilasi | Koreksi lewat PR + CHANGELOG; tarik dokumen formal yang keliru | Admin riset |

## 3. Peta panas (ringkasan)

| Kategori | Risiko |
|---|---|
| **Tinggi (15–25)** | RSK-02 Fake AI research (20), RSK-01 Overload (16), RSK-12 Mentor capacity (16), RSK-04 Plagiarism (15) |
| **Sedang (8–12)** | RSK-03 Predatory journal (12), RSK-05 Faculty resistance (12), RSK-06 Fragmentation (12), RSK-13 Ketergantungan satu orang (12), RSK-10 Data privacy (10), RSK-07 Administrative burden (9), RSK-09 Quality inconsistency (9), RSK-14 Fakta tak terverifikasi (9), RSK-08 Publication gaming (8) |
| **Rendah (1–6)** | RSK-11 Tool obsolescence (6) |

Empat risiko tinggi memiliki benang merah: **kapasitas manusia** (RSK-01, RSK-12) dan **integritas di era GenAI** (RSK-02, RSK-04). Itulah sebabnya desain memilih sweet spot di bawah frontier dan menempatkan integritas sebagai gate lulus/gagal, bukan skor.

## 3.1 Risiko yang paling akut per fase

Setiap fase [GOV-02](02-implementation-roadmap.md) mengaktifkan risiko yang berbeda; owner fase memantau baris yang relevan lebih ketat.

| Fase | Risiko paling akut | Mengapa | Pengaman utama pada fase itu |
|---|---|---|---|
| Phase 1 Pilot Metopen | RSK-01, RSK-02, RSK-12, RSK-09 | Semua serba pertama: beban belum terukur, protokol AI baru dikenal, mentor terbatas, reviewer belum terkalibrasi | S0 onboarding; kalibrasi reviewer; dosen pengampu merangkap mentor; audit referensi W5 |
| Phase 2 Integrate AI/ML | RSK-05, RSK-06, RSK-04 | MK lain masuk; asset mulai dipakai ulang tanpa atribusi; ID mudah terlewat | Mode R yang jelas; handoff Course → Metopen; pencatatan reuse eksplisit |
| Phase 3 Expand technical courses | RSK-05, RSK-09, RSK-13 | Lebih banyak dosen dengan pemahaman berbeda; ketergantungan pada penggagas | Lecturer Playbook; workshop; `@maintainers` kedua |
| Phase 4 AI Research Center | RSK-10, RSK-03, RSK-08, RSK-12 | Data partner masuk; tekanan publikasi/hibah naik; kebutuhan mentor melonjak | Perjanjian data; venue registry; IP review; research leads klaster |
| Phase 5 Scale cross-faculty | RSK-10, RSK-07, RSK-11, RSK-14 | Data lintas fakultas lebih sensitif; laporan publik; otomasi bergantung tool; dokumen formal dikutip luas | SECURITY.md lintas fakultas; ekspor otomatis; katalog kategorikal; verifikasi fakta |

## 3.2 Dashboard risiko untuk rapat bulanan

Admin riset mengisi tabel ini sebelum rapat Research Ops ([GOV-01 §4](01-governance-model.md)); hanya risiko sedang/tinggi dan risiko dengan sinyal aktif yang dibahas.

| ID | Skor saat ini | Sinyal aktif bulan ini? (ya/tidak + bukti) | Tren (naik/tetap/turun) | Tindakan bulan lalu | Tindakan bulan ini | Owner hadir? |
|---|---|---|---|---|---|---|
| RSK-01 | 16 | [isi] | [isi] | [isi] | [isi] | [isi] |
| RSK-02 | 20 | [isi] | [isi] | [isi] | [isi] | [isi] |
| RSK-12 | 16 | [isi] | [isi] | [isi] | [isi] | [isi] |
| RSK-04 | 15 | [isi] | [isi] | [isi] | [isi] | [isi] |
| … | | | | | | |

Contoh terisi (pilot, bulan ke-2): `RSK-12 | 16 | ya — 2 mentor memegang 7 tim, PR G4 tim C menunggu 8 hari | naik | matching mentor | tambah 1 reviewer dari @reviewers untuk G4; batasi 5 tim/mentor mulai angkatan berikutnya | ya`.

## 4. Proses review risiko

| Langkah | Kapan | Siapa | Apa yang dilakukan |
|---|---|---|---|
| 1. Pantau sinyal dini | Mingguan (sprint review) dan bulanan (Research Ops) | Dosen pengampu; admin riset | Periksa early warning signal, terutama KPI-L-05, L-07, L-08, Q-02; catat blocker sebagai Issue `type:research-risk` |
| 2. Nilai ulang skor | Bulanan | Admin riset (R), Kaprodi (A) | Perbarui L dan I berdasarkan kejadian nyata; risiko tinggi dilaporkan di rapat bulanan |
| 3. Tambah risiko baru | Kapan saja | Siapa pun lewat PR ke dokumen ini | ID baru berurutan (`RSK-15`, …), deskripsi, L/I, sinyal, mitigasi, contingency, owner |
| 4. Aktifkan contingency | Saat sinyal dini terpenuhi | Owner risiko | Jalankan contingency; catat di notulen; buka Issue tindak lanjut |
| 5. Evaluasi semester | Akhir semester | Kaprodi, tim kurikulum, AI Center | Tinjau seluruh register; tutup risiko yang tidak relevan (status *retired*, ID tidak dipakai ulang); perbarui mitigasi; catat di CHANGELOG |
| 6. Review tahunan | Tahunan | Kaprodi, kepala AI Research Center | Selaraskan dengan roadmap ([GOV-02](02-implementation-roadmap.md)) dan target 2030; lampirkan sebagai evidence tata kelola ([GOV-05](05-ppts-and-institutional-evidence.md)) |

Insiden integritas (RSK-02, RSK-04, RSK-10) **tidak** didiskusikan di repo publik; register ini hanya mencatat jumlah dan status penanganan (KPI-Q-05). Prosedur penanganan mengikuti [MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md).

## 5. Hubungan dengan risiko per riset

| Level | Tempat pencatatan | Contoh |
|---|---|---|
| Institusional (dokumen ini) | `RSK-NN` di register | Mentor capacity; predatory journal |
| Per riset | Issue `type:research-risk` di repo riset + Mission Control (Status: Blocked) | Dataset partner belum diberikan; baseline tidak dapat direproduksi |
| Per gate | Bagian Threats to Validity di Research Pack | Leakage; sampel tidak representatif |

Risiko per riset yang muncul berulang di ≥3 tim dinaikkan menjadi kandidat risiko institusional lewat PR ke dokumen ini.
