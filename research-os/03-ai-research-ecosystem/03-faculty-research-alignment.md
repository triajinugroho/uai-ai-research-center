# Faculty Research Alignment — Menemukan Adjacency AI dari Kepakaran Dosen yang Ada

> **ID** AIR-03 · **Paket** 03 AI Research Ecosystem · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, kepala pusat riset, research lead klaster, seluruh dosen Prodi Informatika, admin riset
> **Terkait** [AIR-01 AI Research Center Concept](01-ai-research-center-concept.md) · [AIR-02 AI Research Clusters](02-ai-research-clusters.md) · [AIR-04 Cross-Faculty AI Model](04-cross-faculty-ai-model.md) · [ARC-02 Curriculum Research Map](../02-academic-architecture/02-curriculum-research-map.md) · [TPL-07 Faculty Research Map Template](../08-templates/07-faculty-research-map-template.md) · [GOV-01 Governance Model](../07-governance/01-governance-model.md) · [Faculty Guide](../../research-based-learning/faculty-guide/README.md)

## 1. Prinsip

**Bukan mengubah semua dosen menjadi AI researcher, tetapi menemukan adjacency AI dari kepakaran yang sudah ada.**

Dosen jaringan tidak perlu menjadi ahli deep learning; ia bisa meneliti keamanan sistem AI. Dosen basis data tidak perlu melatih model; ia bisa meneliti data engineering dan kualitas data untuk AI. Dosen HCI sudah berada di jantung Human-Centered AI. Dosen matematika/statistika adalah orang yang paling dibutuhkan untuk evaluasi dan inferensi yang benar. AI adalah *thematic umbrella* — payung, bukan pengganti kepakaran.

Tiga alasan pendekatan ini lebih sehat daripada "semua ke AI":

1. **Riset yang baik lahir dari kepakaran yang dalam**, bukan dari topik yang sedang populer.
2. **Beban dosen realistis**: adjacency menambah satu sudut pandang, bukan satu bidang baru.
3. **Klaster C2, C3, C4 justru membutuhkan** dosen non-ML: sistem, keamanan, HCI, etika, domain.

Hasil pemetaan dipakai untuk: mentor dan reviewer gate per klaster, menu masalah untuk MK mode R, proposal skema penelitian internal, Faculty Portfolio di Mission Control, dan perencanaan BKD.

## 2. Template pemetaan

Format resmi dan versi yang dapat diisi ada di [TPL-07](../08-templates/07-faculty-research-map-template.md); tabel di bawah adalah bentuk ringkasnya. Lima baris contoh memakai **nama peran generik**, bukan nama orang; baris riil ditulis dengan placeholder `[isi]` sampai diisi dari wawancara.

| Dosen | Existing Expertise | AI Relation | Primary Cluster | Secondary Cluster | Possible Research |
|---|---|---|---|---|---|
| *Contoh: Dosen jaringan & keamanan* | Jaringan komputer, keamanan sistem, forensik | AI Enabling — keamanan sistem AI; deteksi anomali jaringan dengan ML | C2 | C3 | Threat model dan uji ketahanan chatbot layanan akademik terhadap prompt injection dan kebocoran data; deteksi anomali trafik kampus dengan baseline sederhana |
| *Contoh: Dosen basis data & data engineering* | Perancangan basis data, data warehouse, kualitas data | AI Enabling — data infrastructure untuk AI; data-centric AI | C2 | C1 | Pengaruh kualitas data dan skema terhadap kinerja model prediksi akademik; pipeline data reproducible untuk datasets-registry |
| *Contoh: Dosen rekayasa perangkat lunak* | Proses pengembangan, pengujian, arsitektur | AI Enabling — SE4AI & AI4SE | C2 | C3 | Studi empiris pengaruh alat coding AI pada kualitas kode proyek mahasiswa; metamorphic testing sistem ML |
| *Contoh: Dosen HCI / multimedia* | Desain interaksi, evaluasi kegunaan, multimedia | Responsible AI / AI Application — human evaluation sistem AI | C3 | C4 | User study kepercayaan dan perilaku verifikasi pada asisten akademik berbasis LLM; desain antarmuka yang mendorong verifikasi sumber |
| *Contoh: Dosen matematika / statistika* | Statistika inferensial, optimasi, pemodelan | AI Core — evaluasi, inferensi, ketidakpastian model | C1 | C3 | Stabilitas dan ketidakpastian kinerja model lintas angkatan; metode evaluasi yang mencegah klaim buruk pada TA berbasis ML |
| `[isi nama dosen]` | `[isi]` | `[isi]` | `[isi C1–C4]` | `[isi / —]` | `[isi 1–3 arah riset]` |
| `[isi]` | `[isi]` | `[isi]` | `[isi]` | `[isi]` | `[isi]` |

Definisi kolom:

| Kolom | Isi |
|---|---|
| **Existing Expertise** | Bidang riset/mengajar dosen saat ini, apa adanya — termasuk yang tidak berhubungan dengan AI |
| **AI Relation** | Lensa hubungan dengan AI ([AIR-02 §2](02-ai-research-clusters.md)): AI Core / AI Enabling / AI Application / Responsible AI, plus satu frasa penjelas |
| **Primary Cluster** | Klaster tempat kontribusi utama dosen paling mungkin (C1–C4) |
| **Secondary Cluster** | Klaster kedua bila ada; boleh kosong |
| **Possible Research** | 1–3 arah riset konkret yang bisa dimulai dalam 12 bulan dengan mahasiswa; bukan judul final |

## 3. Prosedur pemetaan

**Langkah 1 — Persiapan (admin riset, 1 minggu).** Kumpulkan data yang sudah ada: mata kuliah yang diampu, publikasi 5 tahun terakhir, TA yang dibimbing, proyek/hibah. Isi kolom *Existing Expertise* sebagai draft.

**Langkah 2 — Wawancara 30 menit (research lead atau kepala pusat riset dengan tiap dosen).** Bukan evaluasi; percakapan. Pertanyaan pemandu:

1. Apa yang paling Anda kuasai dan paling Anda nikmati untuk diteliti atau diajarkan?
2. Masalah nyata apa (di kampus, industri, masyarakat) yang sering Anda temui dan menurut Anda belum terjawab?
3. Data apa yang pernah Anda pegang atau bisa Anda akses?
4. Kalau ada satu hal di bidang Anda yang berubah karena AI, apa itu?
5. Riset apa yang ingin Anda kerjakan bila ada dua mahasiswa yang membantu selama satu tahun?
6. Peran mana yang nyaman bagi Anda tahun ini: owner riset, mentor, reviewer gate, atau penyedia masalah/data?

Pewawancara mengisi *AI Relation*, klaster, dan *Possible Research* **bersama** dosen di akhir wawancara; jangan diisi sendiri setelahnya.

**Langkah 3 — Form.** Dosen memeriksa dan melengkapi barisnya lewat form [TPL-07](../08-templates/07-faculty-research-map-template.md) (peran yang bersedia diambil, kapasitas mahasiswa per tahun, MK yang diampu dan mode F/E/R-nya).

**Langkah 4 — Validasi (research lead klaster, 1 minggu).** Periksa: apakah klaster primer sesuai kontribusi utama; apakah *Possible Research* cukup konkret untuk menjadi Issue `type:problem`; apakah ada tumpang tindih yang bisa menjadi kolaborasi.

**Langkah 5 — Publikasi & tindak lanjut.** Peta disahkan Kaprodi, disimpan di `research-based-learning/faculty-guide/` (versi internal bila memuat data pribadi) dan diringkas di Faculty Portfolio. Setiap *Possible Research* yang disetujui dosen dibuka sebagai Issue backlog dengan dosen sebagai problem owner.

**Langkah 6 — Pemutakhiran.** Setiap tahun (bersamaan dengan review roadmap) atau ketika dosen baru bergabung.

Waktu total untuk 15–20 dosen: sekitar 4–6 minggu kalender, 30 menit per dosen ditambah satu sesi validasi per klaster.

## 4. Contoh adjacency untuk kepakaran umum

| Kepakaran existing | Adjacency AI yang alami | Klaster | Contoh riset awal dengan mahasiswa | MK yang bisa menjadi Build |
|---|---|---|---|---|
| **Jaringan komputer** | Keamanan sistem AI; deteksi anomali/intrusi berbasis ML; jaringan untuk inferensi edge | C2 (sekunder C3) | Evaluasi ketahanan layanan LLM kampus; baseline deteksi anomali trafik dengan metrik yang jujur | Keamanan, IoT, Pengujian PL |
| **Basis data** | Data engineering untuk AI; kualitas data; skema dan kartu dataset; knowledge graph | C2 / C1 | Dampak kualitas anotasi/data terhadap model; pembangunan datasets-registry Prodi | Basis Data, Data Mining |
| **Rekayasa perangkat lunak** | SE4AI (menguji, memelihara sistem ML), AI4SE (alat coding AI), reproducibility | C2 (sekunder C3) | Studi empiris alat coding AI di kelas RPL; pipeline reproducible untuk eksperimen mahasiswa | RPL, Pengujian PL, Proyek PL |
| **HCI / multimedia** | Human-centered AI; evaluasi pengguna; explainability; desain yang mendorong verifikasi | C3 (sekunder C4) | User study chatbot akademik; explainability untuk dosen wali | HCI, Proyek PL |
| **Keamanan informasi** | AI safety/security; privasi teknis; adversarial ML; tata kelola data | C2 (sekunder C3) | Threat model sistem AI kampus; privasi pada analitik pembelajaran | Keamanan, Etika Profesi |
| **Matematika / statistika** | Evaluasi model, inferensi, ketidakpastian, desain eksperimen, causal thinking | C1 (sekunder C3) | Stabilitas model lintas angkatan; "enough statistics" untuk TA ML | Statistika, Statistika Terapan, AI/ML |
| **Algoritma / komputasi** | Efisiensi model, benchmarking empiris, optimasi | C1 / C2 | Benchmark biaya–kinerja inferensi lokal vs API | Analisis Algoritma, Struktur Data |
| **Sistem informasi / manajemen** | AI Application di bisnis/pemerintahan; adopsi teknologi; evaluasi dampak | C4 (sekunder C3) | Asisten regulasi untuk UMKM dan evaluasi kebergunaannya | Proyek PL, KP |
| **IoT / embedded** | Edge AI, sensing sebagai data infrastructure | C2 (sekunder C4) | Dataset sensor kampus dengan kartu dataset; model ringan di perangkat | IoT, Proyek PL |
| **Pendidikan / pedagogi (bila ada)** | AI dalam pendidikan; integritas akademik; literasi AI | C3 (sekunder C4) | Perilaku verifikasi mahasiswa terhadap AI di Metopen | Metopen, Etika Profesi |

Pola umumnya: kepakaran *infrastruktur* → C2; kepakaran *manusia/nilai* → C3; kepakaran *kuantitatif* → C1 (evaluasi); kepakaran *domain* → C4. Hampir tidak ada kepakaran Informatika yang tidak punya adjacency.

## 5. Kaitan dengan BKD dan skema penelitian internal

- **BKD.** Setiap riset ber-Research ID dengan dosen sebagai owner/mentor tercatat di Faculty Portfolio (view Mission Control) — bukti kegiatan penelitian dan pembimbingan yang dapat ditarik per semester tanpa mengisi ulang formulir dari nol. GitHub tetap research tracking system, bukan sistem kepegawaian ([GOVERNANCE.md §9](../../GOVERNANCE.md)); angka BKD resmi tetap diproses unit universitas.
- **Skema penelitian internal UAI.** Beberapa skema mensyaratkan atau mendorong keterlibatan mahasiswa — pada call yang ditemukan, minimal dua mahasiswa aktif — dan mengarahkan topik selaras Renstra Penelitian.[^1] Pipeline ini memenuhi keduanya secara alami: *Possible Research* dosen menjadi masalah backlog → dikerjakan mahasiswa di MK mode R/Metopen/TA → hasil gate menjadi *preliminary result* proposal → dua mahasiswa Metopen/TA menjadi anggota tim. Dosen tidak perlu mencari mahasiswa dadakan menjelang tenggat proposal.
- **Publikasi bersama.** Riset mahasiswa yang lolos G7–G8 di bawah mentor menghasilkan manuscript dengan dosen sebagai penulis sesuai kontribusi (aturan authorship di [AIR-04 §5](04-cross-faculty-ai-model.md) berlaku juga untuk dosen–mahasiswa).

## 6. Peran yang dapat diambil dosen

Tidak semua dosen harus menjadi owner riset. Peta ini mencatat peran yang **dipilih** dosen tahun itu:

| Peran | Komitmen | Cocok untuk |
|---|---|---|
| **Problem/data provider** | Mengajukan masalah atau data ke backlog/registry; tidak membimbing | Dosen dengan akses masalah/data tetapi waktu terbatas |
| **Reviewer gate** | Mereview 3–6 PR gate per semester di klasternya | Semua dosen; latihan terbaik untuk memahami sistem |
| **Mentor** | Mendampingi 1–3 tim Metopen/TA dari G4 hingga G8 | Dosen dengan kepakaran dekat pada topik |
| **Owner riset** | Memimpin riset ber-Research ID dengan mahasiswa; menuju paper/hibah | Dosen yang siap menjadikan riset bagian BKD/hibah |
| **Research lead klaster** | Memvalidasi backlog, mengatur mentor/reviewer, melapor per semester | Satu dosen per klaster |

Peran dapat berubah tiap semester; yang penting tercatat.

## 7. Kesalahan umum

| Kesalahan | Cara menghindari |
|---|---|
| Mengisi peta dari CV tanpa wawancara | Wawancara 30 menit wajib; kolom *AI Relation* dan *Possible Research* diisi bersama dosen |
| Memaksa semua dosen ke C1 | Ingat: C2–C4 membutuhkan dosen non-ML; klaster ditentukan kontribusi, bukan gengsi |
| *Possible Research* terlalu umum ("AI untuk pendidikan") | Uji: bisakah menjadi Issue `type:problem` dengan stakeholder, data yang mungkin, dan MK terkait? |
| Peta dibuat sekali lalu usang | Pemutakhiran tahunan; perubahan lewat PR ke TPL-07 versi terisi |
| Peta menjadi alat penilaian dosen | Peta adalah alat pencocokan; tidak ada peringkat dosen ([TPL-03](../08-templates/03-research-leaderboard-template.md) mengurutkan riset, bukan orang) |

## 8. Ringkasan

- Cari adjacency, bukan konversi: setiap kepakaran Informatika punya pintu masuk ke salah satu klaster.
- Enam kolom, satu wawancara 30 menit per dosen, validasi research lead, pemutakhiran tahunan.
- Hasilnya langsung dipakai: mentor/reviewer per klaster, menu masalah MK mode R, tim untuk skema penelitian internal (minimal dua mahasiswa), Faculty Portfolio untuk BKD.
- Format isian resmi: [TPL-07 Faculty Research Map Template](../08-templates/07-faculty-research-map-template.md).

[^1]: Persyaratan skema penelitian internal UAI 2026 (minimal dua mahasiswa aktif; keselarasan dengan Renstra Penelitian) berasal dari dokumen diskusi *Riset AI UAI untuk Negeri*; verifikasi terhadap panduan resmi sebelum dipakai dalam dokumen formal.
