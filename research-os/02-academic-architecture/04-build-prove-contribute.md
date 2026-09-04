# Build → Prove → Contribute — Koneksi Utama Technical Courses, Metopen, dan Tugas Akhir

> **ID** ARC-04 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu MK teknis (terutama AI/ML), dosen pengampu Metopen, pembimbing TA, koordinator TA, pusat riset
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [ARC-01 Capability Spiral](01-research-capability-spiral.md) · [ARC-03 AI Contribution Modes](03-ai-contribution-modes.md) · [ARC-06 Research Output Taxonomy](06-research-output-taxonomy.md) · [MET-01 Metopen Positioning](../04-metopen-research-studio/01-metopen-positioning.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [TPL-14 Research Handoff](../08-templates/14-research-handoff-template.md) · [AIR-01 AI Research Center Concept](../03-ai-research-ecosystem/01-ai-research-center-concept.md)

## 1. Arsitektur dalam satu baris

**Technical Courses = BUILD. Metopen = PROVE. TA = CONTRIBUTE.**

Mata kuliah teknis **membangun** research asset (kode, data, eksperimen, prototype). Metopen **membuktikan** kualitas buktinya (masalah nyata, evidence map, RQ, desain, pilot, validitas). Tugas Akhir **berkontribusi** — menjawab RQ dan mewariskan hasil sebagai pengetahuan atau artefak. Pada level pusat riset, rantai ini diperluas dua tahap: **Discover** sebelum Build (dari mana masalah datang) dan **Scale** setelah Contribute (ke mana hasil pergi).

Tanpa arsitektur ini, tiga hal terjadi berulang setiap tahun: proyek AI/ML semester V hilang setelah nilai keluar; mahasiswa masuk semester VII masih mencari judul; TA dimulai dari nol tanpa bukti bahwa masalahnya nyata. Arsitektur ini bukan menambah pekerjaan; ia **menyambung** pekerjaan yang sudah ada.

## 2. Diagram alur

```
 DISCOVER            BUILD                 PROVE                  CONTRIBUTE            SCALE
 (AI Center,         (Technical Courses:   (Metopen sem. VII,     (TA sem. VIII,        (AI Center:
  KP, mitra,          AI/ML sem. V, Data    16 minggu,             4 SKS)                program-*,
  dosen, backlog)     Mining, Proyek PL,    8 gates)                                     paper, HKI,
                      RPL, HCI, NLP)                                                     produk, mitra)
 ┌──────────────┐    ┌──────────────┐      ┌──────────────┐       ┌──────────────┐      ┌──────────────┐
 │ Problem Brief│    │ Research     │      │ Research Pack│       │ TA + output  │      │ Publikasi    │
 │ Dataset card │───►│ Asset:       │─────►│ + Proposal TA│──────►│ dari         │─────►│ Dataset rilis│
 │ Issue backlog│    │ Experiment   │      │ + repo v1.0  │       │ taksonomi    │      │ Artefak/HKI  │
 │ Research ID  │    │ Card + repo  │      │ (G1 → G8)    │       │ (paper, DS,  │      │ Riset dosen  │
 │ (sementara)  │    │ + dataset    │      │              │       │ ART, HKI)    │      │ Backlog baru │
 └──────────────┘    └──────────────┘      └──────────────┘       └──────────────┘      └──────────────┘
        │                   │                     │                       │                     │
        ▼                   ▼                     ▼                       ▼                     ▼
   entry door          HANDOFF #1            HANDOFF #2               HANDOFF #3           Research ID
   dipilih             Course → Metopen      Metopen → TA             TA → AI Center       tetap sama
                       (TPL-14)              (TPL-14 + G8)            (TPL-14)             sepanjang alur
```

Prinsip yang mengikat semuanya: **satu Research ID `UIAI-YYYY-NNN`** mengikuti riset dari backlog hingga publikasi, meski judul, tim, dan pembimbing berubah ([GOVERNANCE.md §5](../../GOVERNANCE.md)).

## 3. Ringkasan lima tahap

| Tahap | Pemilik | Pertanyaan | Input | Output wajib | Gate |
|---|---|---|---|---|---|
| **Discover** | AI Research Center, dosen, mahasiswa KP, mitra | Masalah apa yang layak diteliti? | Roadmap, Renstra, masalah mitra, KP, riset dosen, dataset | Issue `type:problem`, Problem Brief v0, kandidat dataset | Sebelum G1 (kolom *Idea*) |
| **Build** | Dosen pengampu MK teknis (mode R/E) | Bisakah kita membangun sesuatu yang bisa diuji? | Problem/dataset dari Discover atau kasus MK | Research asset: Experiment Card + repositori + dataset card; handoff | Embrio G5–G6 (tidak formal) |
| **Prove** | Dosen pengampu Metopen + mentor | Apakah klaimnya layak dipercaya? | Asset hasil Build (atau entry door lain) | Research Pack, Proposal TA, release v1.0, handoff | **G1–G8 formal** |
| **Contribute** | Pembimbing TA + mahasiswa | Apa kontribusinya dan siapa yang bisa memeriksanya? | Research Pack | Laporan TA + minimal satu output taksonomi; handoff | G6–G8 diperbarui untuk skala TA; release v1.1/v2.0 bila publikasi |
| **Scale** | AI Research Center, research lead klaster | Ke mana hasil ini pergi dan riset apa yang lahir darinya? | TA + output + handoff | Publikasi/dataset/artefak terdaftar, program riset, backlog baru | *Published/Released* |

## 4. BUILD — Technical Courses

**Tujuan.** Mengubah proyek mata kuliah dari "tugas yang selesai saat nilai keluar" menjadi **research asset** yang dapat dilanjutkan orang lain. Build tidak menuntut riset lengkap; ia menuntut artefak yang *bisa diuji*.

**Mata kuliah utama.** AI & Machine Learning (sem. V, mode R) sebagai pintu utama; Data Mining (sem. IV), Proyek Perangkat Lunak (sem. VI), RPL (sem. IV), HCI (sem. III), NLP/peminatan sebagai pintu tambahan (mode E→R). Peran masing-masing di [ARC-02](02-curriculum-research-map.md).

**Input.** Salah satu dari: (a) masalah dari research backlog yang sudah punya Research ID sementara; (b) dataset dari `datasets-registry/`; (c) sub-masalah riset dosen; (d) kasus yang dirancang dosen pengampu. Prinsip *reuse before create*: dosen pengampu memeriksa backlog dan registry sebelum membuat kasus baru.

**Output wajib (mode R).**

| Artefak | Spesifikasi | Template |
|---|---|---|
| Experiment Card | Hipotesis, baseline, variabel, dataset, metrik, kontrol, hasil, threats | [TPL-09](../08-templates/09-experiment-card.md) |
| Repositori eksperimen | Struktur standar; README cara menjalankan; environment; seed; direproduksi peer minimal sekali | [TPL-15](../08-templates/15-research-repository-template.md) |
| Dataset card (bila memakai/membuat data baru) | Sumber, lisensi, privasi, ukuran, modality, potensi RQ | [TPL-05](../08-templates/05-dataset-registry-template.md) |
| AI Usage Log | Alat, tujuan, output material, verifikasi | [TPL-10](../08-templates/10-ai-usage-log-template.md) |
| Handoff #1 | Untuk asset yang layak dilanjutkan | [TPL-14](../08-templates/14-research-handoff-template.md) |

**Kriteria handoff Course → Metopen (Handoff #1).** Asset layak di-handoff bila:

1. Masalahnya dapat dijelaskan dalam dua kalimat oleh orang di luar tim (embrio G2).
2. Baseline dan metrik ditetapkan **sebelum** eksperimen dan tercatat di Experiment Card.
3. Repositori dapat dijalankan ulang oleh peer (angka baseline tereproduksi).
4. Ada minimal satu hasil — termasuk hasil negatif — dan satu daftar "apa yang belum diketahui".
5. AI Usage Log terisi.
6. Ada dosen owner yang bersedia menjadi mentor awal atau merujuk ke dosen lain.

Asset yang memenuhi 1–3 saja tetap boleh di-handoff dengan catatan *missing evidence*; itulah gunanya kolom tersebut.

**Gate relevan.** Build melatih G5 Method dan G6 Experiment dalam bentuk embrio; belum ada review formal. Bila MK memakai PR review internal kelas, template `experiment-review.md` dapat dipakai sebagai latihan.

**Pemilik.** Dosen pengampu MK (mode R) sebagai owner proses; mahasiswa sebagai owner artefak; koordinator Metopen sebagai penerima daftar handoff di akhir semester.

## 5. PROVE — Metodologi Penelitian

**Tujuan.** Membuktikan bahwa masalahnya nyata, buktinya dipetakan, pertanyaannya tepat, metodenya valid, pilotnya viable, dan klaimnya tidak melebihi bukti. Metopen adalah **evidence-quality gate** — Research Studio, bukan kuliah tentang penelitian ([MET-01](../04-metopen-research-studio/01-metopen-positioning.md)).

**Input.** Prioritas pertama: asset dari Build lewat Handoff #1 (entry door *Course Project*). Pintu lain tetap terbuka: Problem, Dataset, Faculty Research, Partner, Competition. Apa pun pintunya, gate-nya sama.

**Output wajib.**

| Artefak | Isi | Sumber spesifikasi |
|---|---|---|
| Research Pack | Problem Brief, Stakeholder/Impact, Literature Evidence Map, Gap, RQ/Hypothesis, Contribution Statement, Research Design, Data Plan, Baseline & Metrics, Pilot Experiment, Threats to Validity, Ethics & Privacy, AI Usage Statement, Reproducibility README, Proposal TA, Research Pitch | [MET-04](../04-metopen-research-studio/04-research-pack-specification.md) |
| Repositori riset `proj-YYYY-topic` | Release `v1.0 Research Pack` | [TPL-15](../08-templates/15-research-repository-template.md) |
| Research Integrity Checklist | Ditandatangani | [TPL-11](../08-templates/11-research-integrity-checklist.md) |
| Handoff #2 Metopen → TA | What exists, missing evidence, next steps, owner (pembimbing TA) | [TPL-14](../08-templates/14-research-handoff-template.md) |

**Kriteria handoff Metopen → TA (Handoff #2).** Sama dengan lulus **G8 Contribution Ready**: Research Pack lengkap, peer review dan defense lulus, integritas lulus, dan *"dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol"* ([OPS-03](../06-execution-os/03-research-gates.md)). Level maturity minimum untuk lanjut ke TA: **TA Ready** (lolos G5); target **Research Ready** (lolos G6–G7).

**Gate relevan.** Seluruh G1–G8 formal, dipetakan ke W1–W16 dan S1–S16. Review lewat PR `GATE REVIEW`.

**Pemilik.** Dosen pengampu Metopen (owner proses dan reviewer utama), mentor dosen (dari klaster), peer reviewer, red team pada W8.

## 6. CONTRIBUTE — Tugas Akhir

**Tujuan.** Menjawab RQ dengan bukti yang cukup dan **mewariskan** hasilnya: TA bukan hanya laporan, tetapi kontribusi pengetahuan atau artefak yang bisa diperiksa dan dilanjutkan.

**Input.** Research Pack + Handoff #2. Pembimbing TA idealnya adalah mentor Metopen atau dosen dari klaster yang sama; bila berbeda, handoff adalah dokumen serah-terima resmi.

**Output wajib.**

| Endgame (ditetapkan di G1) | Output minimum TA |
|---|---|
| TA Ready | Laporan TA + repositori final (reproducible) + handoff #3 |
| Research Ready | Di atas + Experiment lengkap (bukan pilot) + analisis G7 penuh |
| Publication Ready | Di atas + manuscript (`PUB-YYYY-NNN`, status manuscript-ready/submission-ready) atau dataset rilis (`DS-`) atau artefak rilis (`ART-`) |
| Impact Ready | Di atas + HKI/prototype/adopsi mitra/bagian riset dosen |

Jenis output mengikuti [ARC-06](06-research-output-taxonomy.md); pipeline publikasi mengikuti [MET-05](../04-metopen-research-studio/05-publication-backward-design.md).

**Kriteria handoff TA → AI Research Center (Handoff #3).**

1. Repositori final berisi kode, konfigurasi, seed, environment, hasil, figur, dan `AI-USAGE.md`; lisensi per komponen dinyatakan.
2. Semua output terdaftar: publikasi di `publications/`, dataset di `datasets-registry/`, artefak di `publications/` (bagian artefak).
3. Bagian *missing evidence* dan *next steps* diisi untuk riset lanjutan; minimal satu Issue `type:problem` atau `type:research-question` baru dibuka di backlog dari hasil TA.
4. Owner lanjutan disebut: dosen pembimbing, research lead klaster, atau program riset.
5. Data sensitif tidak ada di repositori ([SECURITY.md](../../SECURITY.md)).

**Gate relevan.** G6 Experiment dan G7 Claim diperbarui pada skala TA (eksperimen penuh, bukan pilot); G8 Contribution Ready diperiksa ulang pada sidang TA. Release `v1.1 Submitted` dan `v2.0 Published` bila endgame publikasi.

**Pemilik.** Pembimbing TA (owner proses), mahasiswa (owner artefak), penguji sidang (reviewer G7–G8), pengelola registry (registrasi output).

## 7. DISCOVER — sebelum Build (perluasan pusat riset)

Build hanya sebaik masalah yang masuk. Discover adalah fungsi pusat riset untuk memastikan mata kuliah dan mahasiswa tidak mengarang masalah.

**Sumber masalah.** Roadmap 2026–2030 ([research-roadmap](../../research-roadmap/README.md)), Renstra Penelitian UAI, masalah mitra industri/pemerintah/masyarakat ([AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)), riset dosen ([AIR-03](../03-ai-research-ecosystem/03-faculty-research-alignment.md)), Problem Brief dari Kerja Praktik, dataset yang tersedia, dan handoff #3 dari TA sebelumnya.

**Output.** Issue `type:problem` di research backlog dengan metadata (cluster, domain, problem owner, potential dataset, maturity, related courses, potential output, priority); Research ID sementara (format ID sementara mengikuti [CONTRIBUTING.md §2](../../CONTRIBUTING.md)) yang menjadi resmi saat lolos G2.

**Pemilik.** AI Research Center (`@maintainers` untuk triase, research lead klaster untuk validasi), dosen pengusul, mahasiswa KP.

**Kaitan ke Build.** Dosen pengampu MK mode R memilih 3–10 masalah dari backlog setiap semester sebagai menu proyek; masalah yang dipilih ditandai `status:ready` dan dikaitkan ke MK di Mission Control (field *Course*).

## 8. SCALE — setelah Contribute (perluasan pusat riset)

Contribute menghasilkan satu TA. Scale membuat satu TA menjadi bagian dari sesuatu yang lebih besar.

**Bentuk Scale.**

| Jalur | Mekanisme | Registrasi |
|---|---|---|
| Publikasi | manuscript-ready → submission-ready → submitted → accepted → published ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)) | `PUB-YYYY-NNN` di `publications/` |
| Dataset rilis | Data governance review → lisensi → rilis di HF/Kaggle/server | `DS-YYYY-NNN` di `datasets-registry/` |
| Artefak/software/model | IP review singkat → lisensi → release | `ART-YYYY-NNN` |
| HKI | Pendaftaran lewat unit HKI universitas | Dicatat di publications (bagian artefak) |
| Riset dosen / hibah | TA menjadi bagian proposal penelitian internal (skema yang mensyaratkan minimal 2 mahasiswa) atau eksternal | Faculty Portfolio di Mission Control |
| Program riset | Beberapa riset dengan tema sama menjadi `program-<nama>` (5–10 tahun) | Repo `program-*` |
| Backlog baru | *Next steps* dari handoff #3 menjadi Issue baru | Research ID baru, terhubung ke ID lama |

**Pemilik.** AI Research Center, research lead klaster, pengelola registry, dosen pembimbing.

**Kaitan ke Discover.** Scale menutup loop: backlog baru dari TA menjadi input Discover untuk angkatan berikutnya. Inilah *compounding loop*.

## 9. Kriteria handoff umum (ringkasan TPL-14)

Setiap handoff — #1 Course → Metopen, #2 Metopen → TA, #3 TA → AI Center — mengisi empat field wajib yang sama:

| Field | Isi | Contoh (Handoff #1) |
|---|---|---|
| **What exists** | Artefak apa yang ada, di mana, versi apa, gate/maturity terakhir | "Repo `proj-2026-lms-risk` commit abc123; Experiment Card v1; baseline logistic regression F1 0.61 tereproduksi peer" |
| **Missing evidence** | Bukti apa yang belum ada untuk naik ke gate berikutnya | "Belum ada evidence map; dataset hanya 1 semester; belum ada threats to validity" |
| **Next steps** | 3–5 langkah konkret berikutnya | "Literature search W3; minta data 2 semester tambahan ke pengelola; tetapkan baseline kedua" |
| **Owner** | Siapa yang bertanggung jawab setelah handoff (dosen + mahasiswa) | "[isi] (dosen mentor, C3); tim: [isi]" |

Ditambah: Research ID, entry door, klaster, lisensi/privasi data, dan AI Usage Log terakhir. Handoff disimpan di repositori riset (`docs/handoff-<tahap>.md`) dan ditautkan dari Issue.

## 10. Skenario naratif: satu riset dari proyek AI/ML semester V hingga TA

**Research ID:** `UIAI-2026-017` · **Klaster primer:** C3 Human-Centered & Responsible AI · **Sekunder:** C4 Applied AI (domain Education) · **Entry door:** Course Project. Nama orang dan dataset di bawah adalah ilustrasi.

**Discover (sebelum semester V).** Bagian akademik Prodi menyampaikan ke pusat riset bahwa mahasiswa yang tertinggal sering baru terdeteksi setelah UTS. Seorang dosen membuka Issue `type:problem` "Deteksi dini mahasiswa berisiko tertinggal dari aktivitas LMS" — cluster `human-ai`, domain Education, potential dataset: log LMS anonim (kandidat `DS-2026-004`), related course AI/ML + Metopen, priority P1. Research ID masih sementara — nomor resmi baru diberikan saat G2.

**Build (semester V, AI & ML, mode R).** Tim tiga mahasiswa memilih masalah itu dari menu proyek. Mereka mengisi Experiment Card: hipotesis "fitur aktivitas minggu 1–6 memprediksi risiko dengan lebih baik daripada baseline IPK semester lalu"; baseline logistic regression pada IPK; metrik F1 kelas minoritas dan AUROC; split per angkatan untuk mencegah leakage. Repositori dibuat dari TPL-15; peer dari tim lain mereproduksi angka baseline. Hasil: gradient boosting sedikit lebih baik dari baseline pada satu angkatan, tidak pada angkatan lain. Mereka menuliskannya jujur, termasuk hasil negatif, dan mencatat penggunaan AI untuk debugging dan brainstorming fitur. Di akhir semester dosen pengampu mengisi **Handoff #1**: what exists (repo, card, baseline tereproduksi), missing evidence (evidence map, data lintas angkatan, fairness antar kelompok, threats to validity), next steps, owner (dosen C3).

**Prove (semester VII, Metopen).** Satu anggota tim melanjutkan. W1 G1: endgame minimum TA Ready, target Research Ready, aspirasi paper di venue AI dalam pendidikan; entry door Course Project. W2 G2: Problem Brief dan stakeholder statement (dosen wali, bagian akademik; keputusan yang berubah: intervensi minggu ke-7); Research ID resmi **`UIAI-2026-017`**. W3–W5 G3: synthesis matrix 18 sumber tentang early-warning system di pendidikan tinggi — polanya: banyak yang melaporkan akurasi tinggi, sedikit yang menguji lintas angkatan atau fairness. W6 G4: gap tepat di situ; RQ1 "Seberapa stabil kinerja model lintas angkatan?", RQ2 "Apakah kesalahan model terdistribusi merata antar kelompok mahasiswa?"; kontribusi empiris + replikasi. W7–W8 G5: Research Design Card (ML research + evaluasi fairness), Data Plan (dua angkatan tambahan, anonimisasi, consent institusi, privasi *Restricted*), baseline dan metrik tetap, threats to validity; dipertahankan di red team W8. W9–W10 G6: repositori dirapikan, pilot pada dua angkatan, direproduksi peer. W11–W12 G7: hasil pilot — kinerja turun pada angkatan baru; error analysis menunjukkan fitur tertentu tidak stabil. Klaim dibatasi. W13–W16 G8: manuscript draft, peer review, revisi, defense; release `v1.0 Research Pack`; **Handoff #2** ke pembimbing TA (dosen yang sama, C3).

**Contribute (semester VIII, TA).** Eksperimen penuh pada tiga angkatan, analisis fairness, dan satu studi kecil dengan dosen wali (HCI: apakah output model dapat ditindaklanjuti). Laporan TA menjawab RQ1–RQ2 dengan klaim terbatas bukti. Output: manuscript `PUB-2027-003` (submission-ready), dataset card `DS-2026-004` diperbarui (data tetap *Restricted*, hanya metadata publik), repositori `ART-2027-002` (kode Apache-2.0). **Handoff #3**: next steps — validasi prospektif satu semester, uji intervensi; Issue baru `type:research-question` dibuka.

**Scale.** Pusat riset memasukkan `UIAI-2026-017` ke Faculty Portfolio dosen pembimbing; riset lanjutannya menjadi bagian proposal skema penelitian internal dengan dua mahasiswa baru; masalah "uji intervensi" masuk menu proyek AI/ML angkatan berikutnya. Research ID tetap sama; riset lanjutan mendapat ID baru yang tertaut.

Yang membuat skenario ini bekerja bukan kepintaran mahasiswa, tetapi tiga handoff yang terisi, satu Research ID, dan gate yang tidak dilompati.

## 11. Anti-pola yang dicegah

| Tanpa arsitektur ini | Dengan arsitektur ini |
|---|---|
| Proyek AI/ML berakhir di laptop mahasiswa | Experiment Card + repo + handoff #1 |
| Mahasiswa masuk Metopen mencari judul dari nol | Menu masalah dari backlog dan asset Build |
| Proposal TA ditulis dua minggu sebelum sidang proposal | Research Pack lahir dari mini research cycle |
| TA berganti pembimbing, riwayat hilang | Research ID + handoff #2 |
| TA selesai, tidak ada yang tahu apa hasilnya | Registry output + handoff #3 + backlog baru |

## 12. Ringkasan

- Build (MK teknis) menghasilkan asset yang bisa diuji; Prove (Metopen) membuktikan kualitas bukti lewat G1–G8; Contribute (TA) menjawab RQ dan mewariskan output.
- Discover memastikan masalah nyata masuk; Scale memastikan hasil tidak berhenti di laporan.
- Tiga handoff memakai satu template ([TPL-14](../08-templates/14-research-handoff-template.md)); satu Research ID mengikat semuanya.
- Kriteria handoff bukan formalitas: ia adalah *definition of done* antar tahap.
