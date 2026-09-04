# Publication Backward Design — Dari Target Venue ke Milestone Mundur

> **ID** MET-05 · **Paket** 04 Metopen Research Studio · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa TA dengan endgame paper/artefak, dosen pembimbing & mentor, pengelola `publications/`, ketua klaster
> **Terkait** [MET-04 Research Pack](04-research-pack-specification.md) · [MET-07 Integrity & Ethics](07-research-integrity-and-ethics.md) · [ARC-06 Research Output Taxonomy](../02-academic-architecture/06-research-output-taxonomy.md) · [TPL-06 Publication Venue Registry](../08-templates/06-publication-venue-registry-template.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [Registry publikasi](../../publications/README.md) · [GOV-04 Risk Register](../07-governance/04-risk-register.md)

## 1. Publication oriented, not publication obsessed

Publikasi adalah **konsekuensi** riset yang baik, bukan tujuan yang membenarkan segala cara. Prinsip kerja dokumen ini:

1. **Backward design.** Bila endgame sebuah riset adalah paper, tentukan venue lebih dulu, lalu turunkan milestone mundur dari deadline. Tanpa itu, manuscript "akan ditulis nanti" — dan nanti tidak pernah datang.
2. **Tidak semua TA harus menjadi paper.** Layer aspirasional ([MET-02](02-metopen-course-outcomes.md) §3) berlaku untuk tim terbaik. TA yang jujur dan reproducible tanpa paper lebih berharga daripada paper di venue predator.
3. **Kematangan diukur dengan gate, bukan dengan jumlah submit.** Riset masuk jalur publikasi hanya setelah G7 Claim Ready; manuscript adalah cara mengomunikasikan klaim yang sudah didukung bukti, bukan cara mencari klaim.
4. **Publication gaming adalah risiko institusional** ([GOV-04](../07-governance/04-risk-register.md)): salami slicing, venue predator, penulis tanpa kontribusi, dan submit ganda dilarang.

## 2. Tahapan kesiapan publikasi

Rantai resmi (glossary §3.3): `TA-ready → manuscript-ready → submission-ready → submitted → accepted → published`.

| Tahap | Definisi | Bukti yang harus ada | Release / status | Siapa memutuskan |
|---|---|---|---|---|
| **TA-ready** | Research Pack cukup matang untuk dieksekusi sebagai TA; belum tentu ada hasil lengkap | Research Pack v1.0 dengan artefak wajib Metopen; G5 lulus (minimum) | v1.0 Research Pack; `maturity:ta-ready` | Dosen pengampu Metopen |
| **Manuscript-ready** | Ada klaim yang didukung bukti, ditulis dalam struktur IMRaD lengkap, dengan threats dan AI disclosure; belum disesuaikan ke venue tertentu | G7 lulus; `paper/` berisi draft lengkap; semua figur/tabel dapat direproduksi dari `results/`; CER table | v0.8 Manuscript Draft → `publications/` entri dibuat, **PUB ID** diberikan | Pembimbing/mentor + peer review internal (TPL-12) |
| **Submission-ready** | Manuscript diformat ke template venue, memenuhi panjang/anonimisasi/etika venue, lolos integrity checklist, semua penulis menyetujui | Venue dipilih dari registry (TPL-06); checklist submission (§8) lengkap; TPL-11 ditandatangani; response internal review selesai; artefak/dataset punya DOI/URL bila disyaratkan | Mission Control: *Submission Ready* | Pembimbing (corresponding author) |
| **Submitted** | Naskah dikirim ke venue | Bukti submit (ID/email); status di registry | v1.1 Submitted; `type:publication` Issue diperbarui | — |
| **Accepted** | Venue menerima (setelah revisi bila ada) | Surat penerimaan; camera-ready; revisi tercatat | Mission Control: *Accepted* | — |
| **Published** | Terbit dengan DOI/URL resmi | DOI; metadata lengkap di `publications/PUBLICATIONS.md`; artefak dirilis sesuai lisensi | v2.0 Published; kolom *Published/Released* | Pengelola `publications/` |

Dua tahap yang sering dilewati dan menyebabkan penolakan: **manuscript-ready** (menulis sebelum klaim jelas) dan **submission-ready** (submit tanpa mengecek scope/format/etika venue).

## 3. Memilih venue

Venue dipilih dari **Publication Venue Registry** ([TPL-06](../08-templates/06-publication-venue-registry-template.md)) yang dikelola klaster; venue baru diusulkan lewat PR ke registry sebelum dipakai.

### 3.1 Kriteria

| Kriteria | Pertanyaan | Tanda baik | Tanda buruk |
|---|---|---|---|
| Scope | Apakah RQ dan jenis kontribusi cocok dengan call/aims? | Paper serupa pernah terbit di sana; kontribusi jenis kita (empiris/artefak/dataset) diterima | "Semua topik komputer" |
| Indexing & reputasi | Terindeks di mana; siapa editor/PC; sponsor komunitas ilmiah (mis. ACM/IEEE/asosiasi nasional) | Editorial board jelas dan dapat diverifikasi; proses review dijelaskan | Janji terbit dalam hitungan hari; email undangan massal |
| Template & panjang | Format apa; berapa halaman; anonimisasi? | Template resmi tersedia | Tidak ada template atau panduan penulis |
| Deadline & siklus | Kapan deadline; berapa lama review; kapan terbit? | Jadwal terbuka, konsisten dengan jadwal TA | Deadline "terus diperpanjang" |
| Biaya | APC/registrasi berapa; ada waiver? | Biaya transparan dan sebanding; ada skema bantuan | Biaya diminta di awal sebelum review |
| Etika publikasi | Kebijakan AI, data, conflict of interest, retraksi jelas? | Kebijakan etika dipublikasikan | Tidak ada kebijakan etika |
| Kecocokan level | Untuk mahasiswa S1: venue nasional bereputasi, workshop/track mahasiswa, konferensi regional, jurnal terakreditasi nasional | Menerima kontribusi empiris/replikasi/dataset skala kecil | Menuntut hasil skala besar yang tidak mungkin dalam TA |

### 3.2 Menghindari venue predator

Tanda-tanda venue predator: undangan tidak diminta, review sangat cepat, biaya diminta sebelum review, scope terlalu luas, nama meniru venue terkenal, editorial board tidak dapat diverifikasi, klaim indeks yang tidak bisa dicek. **Aturan:** venue yang tidak ada di registry dengan status etika terverifikasi tidak boleh menjadi target submit riset UAI. Bila ragu, tanyakan ke ketua klaster dan pengelola `publications/`.

### 3.3 Jenis output sesuai taksonomi

Bukan hanya paper. Sesuai [ARC-06](../02-academic-architecture/06-research-output-taxonomy.md), output yang dicatat: paper (konferensi/jurnal/workshop), dataset (`DS-`), artefak software/model/benchmark (`ART-`), HKI, prototype, laporan kebijakan/industri. Backward design berlaku untuk semuanya: dataset punya "venue" berupa repositori data dengan DOI; artefak punya rilis dengan lisensi dan dokumentasi.

## 4. Jadwal mundur dari deadline

Gunakan deadline venue sebagai T0 dan hitung mundur. Angka minggu adalah default; sesuaikan dengan kalender TA.

| Waktu | Milestone | Bukti | Tahap |
|---|---|---|---|
| T−16 minggu | G7 Claim Ready: hasil utama dan CER table final | PR G7 merged; `results/analysis.md` | manuscript-ready dimulai |
| T−12 minggu | Draft lengkap IMRaD v0.8 (semua bagian, figur, tabel, threats, AI disclosure) | release v0.8; entri `publications/` + PUB ID | manuscript-ready |
| T−10 minggu | Internal peer review (TPL-12) oleh ≥1 peer dan ≥1 dosen di luar tim | review tersimpan di `paper/reviews/` | |
| T−8 minggu | Revisi mayor; eksperimen tambahan bila reviewer meminta (harus tercatat sebagai run baru, bukan angka baru) | response letter internal | |
| T−6 minggu | Pemilihan venue final dari registry; pemetaan ke template; cek panjang & anonimisasi | venue di Issue `type:publication` | submission-ready dimulai |
| T−4 minggu | Reproducibility check oleh peer: figur/tabel utama dihasilkan ulang dari repositori | catatan reproduksi | |
| T−3 minggu | Research Integrity Checklist (TPL-11) untuk manuscript; cek sitasi terhadap `references.bib`; cek kebijakan AI venue | TPL-11 ditandatangani semua penulis | |
| T−2 minggu | Persetujuan semua penulis; pembimbing menyetujui sebagai corresponding author; artefak/dataset diberi DOI/URL bila disyaratkan | persetujuan tercatat di Issue | submission-ready |
| T−1 minggu | Proofread akhir; metadata (judul, abstrak, kata kunci, afiliasi "Universitas Al-Azhar Indonesia") | final PDF di `paper/submitted/` | |
| T0 | Submit | bukti submit; release v1.1 | submitted |
| T+review | Tanggapi review venue; setiap perubahan hasil dijalankan ulang dan dicatat | response letter di `paper/` | revision |
| Accepted | Camera-ready; rilis artefak; perbarui registry | release v2.0; `publications/PUBLICATIONS.md` | accepted → published |

Bila T−16 jatuh sebelum G7 tercapai, venue itu **bukan** target realistis untuk siklus ini; pilih venue dengan deadline berikutnya. Mengejar deadline dengan hasil setengah jadi adalah sumber utama klaim buruk.

## 5. Struktur manuscript IMRaD untuk computing

Manuscript ditulis **dari Research Pack**, bukan dari nol. Pemetaan:

| Bagian | Isi | Ditarik dari artefak |
|---|---|---|
| Title & Abstract | Masalah, metode, hasil utama, kontribusi, dalam ±200 kata; tidak ada klaim yang tidak ada di badan paper | Contribution Statement, CER table |
| 1 Introduction | Fenomena/masalah; mengapa penting; gap singkat; RQ; ringkasan kontribusi (bullet) | Problem Brief, Research Gap, RQ, Contribution |
| 2 Related Work / Background | Sintesis literatur berdasarkan tema (bukan daftar); apa yang konsisten/bertentangan; posisi riset ini | Literature Evidence Map, synthesis matrix |
| 3 Method / Approach | Desain; data (sumber, ukuran, split, lisensi, privasi); baseline; metrik; prosedur; implementasi; penggunaan AI dalam proses riset bila memengaruhi kesimpulan | Research Design, Data Plan, Baseline & Metrics, AI Usage Statement |
| 4 Experimental Setup | Environment, seed, hyperparameter, protokol evaluasi; tautan repositori | Reproducibility README, Experiment Card |
| 5 Results | Tabel/figur vs baseline dengan variansi; error analysis; hasil negatif | `results/analysis.md`, `figures/` |
| 6 Discussion | Claim–Evidence–Reasoning per RQ; implikasi bagi stakeholder ("so what"); perbandingan dengan literatur | CER table, Stakeholder/Impact |
| 7 Threats to Validity | Internal, eksternal, konstruk, statistik; mitigasi; sisa risiko | Threats v2 |
| 8 Conclusion & Future Work | Klaim final sebatas bukti; langkah berikutnya | Contribution (revisi), Handoff |
| Ethics / Data Availability / AI Disclosure | Pernyataan etika, ketersediaan data & kode, penggunaan AI (mengikuti kebijakan venue) | `docs/ethics.md`, `AI-USAGE.md` |
| References | Hanya sumber yang dibaca dan terverifikasi | `references.bib` |

Untuk **proposal TA**, struktur yang sama dipakai dengan bagian 5–6 diganti "Hasil Pilot" dan ditambah "Rencana & Jadwal TA". Bagian 7 (threats) tetap wajib. Format resmi Prodi mengikat (`[isi]`); pemetaan ini memastikan isinya konsisten dengan repositori.

## 6. Authorship policy

Kebijakan penulis mengikuti prinsip kontribusi nyata dan [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) (tidak mengklaim pekerjaan orang lain; tidak memasukkan nama tanpa kontribusi; tidak menghapus kontributor nyata).

| Ketentuan | Isi |
|---|---|
| Kriteria penulis | Kontribusi substansial pada minimal satu dari: konsepsi/desain, data, eksperimen/analisis, penulisan; **dan** menyetujui versi final; **dan** bertanggung jawab atas bagian yang dikerjakan |
| Mahasiswa sebagai first author | Bila mahasiswa mengerjakan bagian terbesar riset (biasanya pada TA yang menjadi paper), mahasiswa **first author**; pembimbing corresponding author. Ini default, bukan pengecualian |
| Urutan penulis | Berdasarkan besar kontribusi; disepakati tertulis sebelum submission-ready (dicatat di Issue `type:publication`) |
| Kontribusi tanpa authorship | Penyedia data, reviewer internal, bantuan teknis kecil → *Acknowledgments* |
| Bukti kontribusi | Riwayat git, Issue/PR, AI Usage Log, notulen; sengketa diselesaikan oleh ketua klaster |
| AI | AI bukan penulis dan tidak dicantumkan sebagai penulis; penggunaannya diungkap sesuai kebijakan venue |
| Afiliasi | "Program Studi Informatika, Universitas Al-Azhar Indonesia" (+ AI Research Center bila sudah resmi) |

## 7. Hubungan ke registry `publications/` dan PUB ID

1. Saat manuscript-ready, pengelola `publications/` memberi **Publication ID** `PUB-YYYY-NNN` dan membuat kartu dari `publications/_template/publication-card.md`, terhubung ke Research ID `UIAI-YYYY-NNN` (dan `DS-`/`ART-` terkait).
2. Status dicatat di `publications/PUBLICATIONS.md` dan di view *Publication Pipeline* Mission Control: Research → Writing → Internal Review → Submission Ready → Submitted → Revision → Accepted → Published ([GOVERNANCE.md](../../GOVERNANCE.md) §9).
3. Registry menyimpan **metadata** (judul, penulis, venue, status, DOI, tautan repositori, lisensi), bukan PDF publisher ([LICENSING.md](../../LICENSING.md)).
4. Setiap perubahan status (submitted/accepted/published) diperbarui bersama release riset (v1.1, v2.0) dan label Issue `type:publication`.
5. Publikasi yang terbit menjadi evidence institusional ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)) dan input KPI lagging ([GOV-03](../07-governance/03-kpi-and-measurement.md)).

## 8. Checklist submission-ready

```
[ ] Venue ada di registry TPL-06 dengan status etika terverifikasi; scope cocok
[ ] Manuscript mengikuti template venue (panjang, anonimisasi, format referensi)
[ ] Semua figur/tabel dapat direproduksi dari repositori (peer check tercatat)
[ ] Threats to Validity ada dan spesifik
[ ] AI disclosure sesuai kebijakan venue; AI-USAGE.md konsisten dengan naskah
[ ] Semua sitasi ada di references.bib dan pernah dibaca; tidak ada sitasi buatan AI
[ ] Data: lisensi & privasi sesuai; data sensitif tidak dibagikan; pernyataan ketersediaan data benar
[ ] Tidak ada submit ganda ke venue lain; tidak ada salami slicing dari riset yang sama
[ ] Semua penulis menyetujui urutan dan versi final; kontribusi tercatat
[ ] TPL-11 Research Integrity Checklist ditandatangani semua penulis
[ ] Issue type:publication dan Mission Control diperbarui ke Submission Ready
```

## 9. Contoh jalur TA → paper (ilustratif)

Tim `[isi]` dengan Research ID `UIAI-2026-0NN`, endgame *paper di venue nasional bereputasi* dengan deadline pertengahan semester VIII:

| Kapan | Apa |
|---|---|
| Metopen W12 | G7 lulus untuk pilot; klaim awal terbatas pada subset |
| Metopen W16 | Research Pack v1.0; handoff mencatat "missing evidence: eksperimen penuh pada data lengkap, ≥5 seed" |
| TA minggu 1–6 | Eksperimen penuh; `results/` diperbarui; CER direvisi |
| TA minggu 7 (T−12) | Draft v0.8; PUB ID diberikan |
| TA minggu 9 (T−10) | Internal review oleh peer & dosen klaster |
| TA minggu 13 (T−6) | Venue final; format |
| TA minggu 16 (T−3) | TPL-11; reproducibility check |
| TA minggu 19 (T0) | Submit; v1.1 |
| Sidang TA | Laporan TA memuat naskah yang disubmit sebagai lampiran; status *submitted* |

Bila hasil eksperimen penuh **tidak** mendukung klaim, jalur yang benar adalah melaporkannya sebagai hasil negatif dalam TA (dan, bila layak, sebagai paper replikasi/negative result), bukan mengubah metrik atau memilih seed terbaik ([MET-07](07-research-integrity-and-ethics.md)).

## 10. Ringkasan satu kalimat per tahap

| Tahap | Kalimat yang harus bisa diucapkan tim |
|---|---|
| TA-ready | "Kami tahu masalah, bukti, RQ, dan metodenya; TA tinggal mengeksekusi." |
| Manuscript-ready | "Klaim kami didukung tabel ini dan dibatasi oleh ancaman ini; naskah lengkap sudah ada." |
| Submission-ready | "Venue ini cocok dan etis; naskah sudah sesuai template; semua penulis dan checklist integritas setuju." |
| Submitted | "Naskah terkirim; kami siap menjalankan ulang apa pun yang diminta reviewer." |
| Accepted / Published | "Hasil ini bisa diperiksa siapa pun lewat DOI dan repositori." |
