# Curriculum Research Map — Menempatkan Setiap Mata Kuliah pada Research Value Chain

> **ID** ARC-02 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu semua mata kuliah, tim kurikulum, Kaprodi, fasilitator workshop dosen
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [ARC-01 Capability Spiral](01-research-capability-spiral.md) · [ARC-03 AI Contribution Modes](03-ai-contribution-modes.md) · [ARC-04 Build–Prove–Contribute](04-build-prove-contribute.md) · [ARC-05 CPL–CPMK–Artifact](05-cpl-cpmk-artifact-alignment.md) · [AIR-02 AI Research Clusters](../03-ai-research-ecosystem/02-ai-research-clusters.md) · [Research-Based Learning](../../research-based-learning/README.md)

## 1. Tujuan dokumen

Dokumen ini menjawab satu pertanyaan yang akan ditanyakan setiap dosen ketika mendengar "kurikulum berbasis riset": **"Lalu mata kuliah saya di mana?"**

Jawabannya: setiap mata kuliah sudah berada pada suatu titik di **research value chain** — rantai nilai yang mengubah masalah nyata menjadi pengetahuan yang kredibel. Statistika bukan "mata kuliah dasar yang tidak ada hubungannya dengan riset"; ia adalah *evidence reasoning*. Basis Data adalah *data infrastructure*. RPL adalah *research-grade software engineering*. HCI adalah *human evaluation*. Tidak ada mata kuliah yang berada di luar rantai; yang berbeda hanya perannya dan seberapa jauh ia diminta menghasilkan research asset (mode F/E/R, [ARC-03](03-ai-contribution-modes.md)).

Dokumen ini dirancang sebagai **bahan workshop dosen satu hari** (§6). Hasil workshop dimasukkan ke `research-based-learning/courses/<mk>/README.md` dan `research-artifact.md`.

## 2. Research value chain

```
 DISCOVER ─────────── BUILD ────────────────────────────── PROVE ──── CONTRIBUTE
 ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐ ┌───────────┐
 │ Problem &  │ │ Evidence   │ │ Data       │ │ Computation│ │ Research-  │ │ Evidence │ │ Contribu- │
 │ Stakeholder│→│ Reasoning  │→│ Infra-     │→│ & AI Core  │→│ grade Eng. │→│ Quality  │→│ tion &    │
 │ Discovery  │ │ (statistik,│ │ structure  │ │ (algoritma,│ │ + Human &  │ │ Gate     │ │ Dissemi-  │
 │ (KP, mitra)│ │ formal)    │ │ (DB, data  │ │ ML, NLP)   │ │ Safety Eval│ │ (Metopen)│ │ nation(TA)│
 └────────────┘ └────────────┘ │ mining)    │ └────────────┘ └────────────┘ └──────────┘ └───────────┘
                               └────────────┘
 Lensa lintas rantai: Responsible AI & Research Integrity (Etika Profesi) · AI-augmented research (semua MK)
```

Peran pada rantai (research value chain role) yang dipakai dalam tabel:

| Role | Arti | Pertanyaan yang dijawab mata kuliah |
|---|---|---|
| **Evidence reasoning** | Kemampuan membaca, mengukur, dan menyimpulkan dari data dengan benar | "Apa yang boleh disimpulkan dari angka ini?" |
| **Formal reasoning** | Definisi, bukti, counterexample, model abstrak | "Apakah klaim ini benar secara logis, dan apa yang membatalkannya?" |
| **Data infrastructure** | Skema, kualitas, provenance, kartu dataset, pipeline data | "Dari mana bukti berasal dan bisakah dipercaya?" |
| **Computation & benchmarking** | Mengukur kinerja algoritma/struktur dengan prosedur berulang | "Lebih baik dibanding apa, diukur bagaimana?" |
| **Research-grade software engineering** | Repositori, pengujian, CI, dokumentasi, reproducibility | "Bisakah orang lain menjalankan ulang?" |
| **Human evaluation** | User study, instrumen, etika partisipan | "Apakah berguna bagi manusia nyata?" |
| **AI Core** | Model, data, knowledge, evaluasi model | "Apakah model ini benar-benar lebih baik dan mengapa?" |
| **Experimentation & evaluation** | Desain eksperimen, baseline, metrik, leakage, error analysis | "Apakah eksperimennya valid?" |
| **AI safety/security & testing** | Menguji, menyerang, dan mengamankan sistem AI | "Kapan sistem ini gagal atau disalahgunakan?" |
| **Problem discovery** | Problem brief dari dunia nyata | "Masalah apa yang layak diteliti?" |
| **Responsible AI & integrity** | Privasi, bias, consent, AI disclosure, amanah epistemik | "Apakah ini boleh dan jujur?" |
| **Evidence quality gate (Prove)** | Integrasi semua di atas dalam satu mini research cycle | "Apakah klaim ini layak dipercaya?" |
| **Contribution (Contribute)** | Menjawab RQ dan mewariskan hasil | "Apa kontribusinya dan siapa yang melanjutkan?" |

## 3. Peta mata kuliah × research value chain

Kolom **Mode** menunjukkan mode default yang disarankan dan mode yang mungkin dicapai (`F→E` berarti default Foundation, dapat naik ke AI-Enriched). Kolom **Klaster** merujuk [AIR-02](../03-ai-research-ecosystem/02-ai-research-clusters.md). Kurikulum semester I–VIII mengikuti dokumen sumber.[^1]

| Mata kuliah | Sem. | Research value chain role | Research asset yang bisa dihasilkan | Mode | Klaster | Contoh project berorientasi riset |
|---|---|---|---|---|---|---|
| Statistika | I | Evidence reasoning | Laporan analisis data kecil dengan bagian "yang tidak boleh disimpulkan"; notebook yang dapat dijalankan ulang | F | C1, C3 | Analisis data survei kebiasaan belajar (anonim): deskripsi, satu uji hipotesis, interpretasi jujur tentang batas kesimpulan |
| Kalkulus | I | Formal reasoning (fondasi model) | Catatan turunan & visualisasi konvergensi | F | C1 | "Mengapa gradient descent bekerja": turunan fungsi loss sederhana dan grafik konvergensi pada data mainan |
| Statistika Terapan | II | Evidence reasoning (inferensi, regresi, desain eksperimen) | Notebook replikasi analisis; laporan CER | F→E | C1, C3 | Replikasi analisis dari satu dataset publik yang dipakai paper; bandingkan hasil dan jelaskan perbedaan |
| Matematika Diskrit | II | Formal reasoning (graf, logika, bukti) | Model graf + bukti/counterexample | F | C1, C2 | Memodelkan prasyarat mata kuliah sebagai graf; membuktikan sifat jalur terpanjang; kaitkan ke perencanaan studi |
| HCI | III | Human evaluation | Protokol user study, instrumen, hasil evaluasi, consent form | E | C3 | Usability study kecil (5–8 partisipan) pada prototipe chatbot layanan akademik; laporkan temuan + threats to validity |
| Struktur Data | III | Computation & benchmarking | Benchmark harness + laporan perbandingan | F | C2 | Membandingkan struktur data pada beban kerja nyata (log aplikasi) dengan pengukuran berulang dan variansi |
| Basis Data | III | Data infrastructure | Skema, data dictionary, dataset card v0 (kandidat `DS-YYYY-NNN`) | F→E | C1, C2 | Merancang skema dan dataset card untuk data pembelajaran (anonim) yang siap dipakai Data Mining semester berikutnya |
| Analisis Algoritma | IV | Computation & benchmarking (empirical algorithmics) | Eksperimen kinerja algoritma + notebook | F→E | C2 | Menguji apakah analisis asimtotik terlihat pada data nyata; laporkan kapan tidak terlihat dan mengapa |
| RPL | IV | Research-grade software engineering | Repositori terstruktur, test suite, README reproducibility, CI sederhana | E | C2 | Membangun pipeline data/eksperimen yang teruji untuk riset dosen atau tim AI/ML; deliverable = repo yang bisa dijalankan orang lain |
| Data Mining | IV | Experimentation & evaluation | Laporan eksperimen dengan baseline, metrik, pemeriksaan leakage; dataset card | E→R | C1, C4 | "Prediksi X" dengan baseline paling sederhana, cross-validation yang benar, error analysis, dan pernyataan keterbatasan |
| AI & Machine Learning | V | AI Core + experimentation | Experiment Card, repositori eksperimen reproducible, model/benchmark kecil, AI Usage Log | R | C1 (C2–C4 sesuai domain) | Mini-research: RQ kecil, baseline vs metode, ablation, variansi antar seed; hasil di-handoff ke Metopen (entry door *Course Project*) |
| Pengujian Perangkat Lunak | V | AI safety/security & testing | Test suite dan protokol evaluasi sistem ML; laporan kegagalan | E | C2 | Metamorphic/robustness testing pada model dari kelas AI/ML; dokumentasikan kelas kegagalan |
| Proyek Perangkat Lunak | VI | Research-grade engineering + human evaluation (prototype) | Prototype AI untuk domain + evaluasi pengguna + AI Usage Statement | E→R | C2, C4 | Prototype AI untuk domain UAI (pendidikan, halal) dengan evaluasi pengguna dan repositori standar |
| Kerja Praktik | VI | Problem discovery | Problem Brief → Issue `type:problem` di research backlog | E | C4 | Setiap mahasiswa KP membawa pulang satu masalah nyata yang layak diteliti, dengan stakeholder dan data yang mungkin (entry door *Partner*) |
| Etika Profesi | VI | Responsible AI & research integrity | Kajian etika & privasi kasus AI; embrio `docs/ethics.md`; pernyataan amanah epistemik | F→E | C3 | Analisis satu kasus AI nyata: privasi, bias, consent, AI disclosure; rekomendasi untuk proyek tim sendiri |
| Metodologi Penelitian | VII | Evidence quality gate (Prove) | Research Pack, Proposal TA, repositori riset, release v1.0 | R | Semua | Mini research cycle 16 minggu ([MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)) |
| Tugas Akhir | VIII | Contribution (Contribute) | Laporan TA + paper/dataset/artefak/HKI/prototype ([ARC-06](06-research-output-taxonomy.md)) | R | Semua | Menjawab RQ dari Research Pack; handoff ke AI Research Center |
| NLP (peminatan; nama & semester: [isi sesuai kurikulum]) | [isi] | AI Core (Indonesian NLP) | Korpus/anotasi kecil, benchmark, model baseline | R | C1 | Membangun benchmark kecil Bahasa Indonesia untuk satu tugas (mis. klasifikasi teks layanan) dengan pedoman anotasi |
| Keamanan Sistem/Jaringan (peminatan; [isi]) | [isi] | AI safety/security | Threat model sistem AI, evaluasi adversarial, laporan | E→R | C2 | Threat model dan uji ketahanan satu sistem berbasis LLM (prompt injection, data leakage) |
| IoT (peminatan; [isi]) | [isi] | Data infrastructure & edge AI | Dataset sensor terdeskripsi, prototype edge inference | E | C2, C4 | Pengumpulan data sensor dengan kartu dataset dan evaluasi model ringan di perangkat |

Catatan: Prodi memosisikan kompetensinya pada Software Engineering, Data Science, IoT, dan NLP (dokumen sumber); baris peminatan di atas mengikuti positioning itu dan harus disesuaikan dengan nama MK dan semester resmi.

## 4. Penjelasan per kelompok

### 4.1 Fondasi kuantitatif & formal (Statistika, Kalkulus, Statistika Terapan, Matematika Diskrit)

Peran: **evidence reasoning** dan **formal reasoning**. Tidak diminta menghasilkan riset; diminta menanamkan tiga kebiasaan: angka membutuhkan pembanding, korelasi bukan sebab-akibat, dan klaim membutuhkan bukti yang bisa diperiksa. Perubahan minimal pada RPS: satu tugas berbasis data nyata (anonim) dengan bagian wajib "apa yang tidak boleh disimpulkan", dan notebook yang bisa dijalankan ulang. Inilah *enough statistics to prevent bad claims* yang dibutuhkan Metopen — ditanam di Year 1, bukan diajarkan ulang di semester VII.

### 4.2 Data & sistem (Struktur Data, Basis Data, Analisis Algoritma)

Peran: **data infrastructure** dan **computation & benchmarking**. Research asset paling bernilai dari kelompok ini adalah *dataset card* (Basis Data) dan *benchmark harness* (Struktur Data, Analisis Algoritma). Dataset card v0 dari Basis Data semester III dapat langsung dipakai Data Mining semester IV dan AI/ML semester V — contoh nyata *reuse before create*.

### 4.3 Rekayasa perangkat lunak (RPL, Pengujian PL, Proyek PL)

Peran: **research-grade software engineering** dan **AI safety/security & testing**. Riset computing menghasilkan kode, dan kode riset yang tidak teruji menghasilkan klaim yang tidak bisa dipercaya. RPL menanamkan repositori standar dan README reproducibility; Pengujian PL menguji sistem ML yang dibangun di AI/ML; Proyek PL membangun prototype untuk domain nyata dengan evaluasi pengguna. Tiga MK ini adalah calon utama mode E→R untuk klaster C2.

### 4.4 Manusia & etika (HCI, Etika Profesi)

Peran: **human evaluation** dan **responsible AI & integrity**. HCI menyediakan metode evaluasi yang sering hilang pada TA berbasis ML: apakah sistemnya berguna bagi manusia. Etika Profesi menanamkan amanah epistemik sebelum mahasiswa masuk Metopen: privasi, consent, bias, AI disclosure. Keduanya adalah rumah alami klaster C3.

### 4.5 AI Core dan eksperimentasi (Data Mining, AI & ML, NLP)

Peran: **AI Core** dan **experimentation & evaluation**. AI/ML semester V adalah MK dengan mode **R** paling penting: proyeknya adalah pintu masuk utama riset mahasiswa (*Course Project*). Kewajiban minimumnya: Experiment Card, baseline dan metrik ditetapkan sebelum eksperimen, repositori yang direproduksi peer, AI Usage Log, dan handoff ke Metopen ([TPL-14](../08-templates/14-research-handoff-template.md)). Data Mining semester IV adalah latihan pendahulunya.

### 4.6 Penemuan masalah (Kerja Praktik)

Peran: **problem discovery**. Kerja Praktik adalah sumber masalah nyata terbesar yang selama ini terbuang. Kewajiban minimum: satu Problem Brief per mahasiswa yang diajukan sebagai Issue `type:problem` ke [research backlog](../../research-backlog/README.md). Tidak semua akan diteliti; yang penting bank masalahnya terisi (lihat [AIR-05](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)).

### 4.7 Integrasi & kontribusi (Metopen, TA)

Peran: **Prove** dan **Contribute**. Detail di [ARC-04](04-build-prove-contribute.md) dan paket 04.

## 5. Cara dosen memakai peta ini

1. Temukan baris mata kuliah Anda. Bila tidak ada, tambahkan barisnya dengan peran dari tabel §2.
2. Pilih **satu** research asset dari kolom "Research asset yang bisa dihasilkan" yang paling dekat dengan tugas/proyek yang sudah ada di RPS. Jangan menambah tugas baru bila tugas lama bisa diarahkan.
3. Tetapkan mode F/E/R memakai decision tree [ARC-03](03-ai-contribution-modes.md).
4. Tulis satu CPMK dan satu assessment yang mengikat asset tersebut memakai kerangka [ARC-05](05-cpl-cpmk-artifact-alignment.md).
5. Bila mode R: tentukan ke mana asset diregistrasikan (backlog, `datasets-registry/`, atau handoff ke Metopen) dan siapa owner-nya.
6. Catat hasilnya di `research-based-learning/courses/<mk>/README.md` (mode, asset, klaster, contoh proyek) dan `research-artifact.md` (spesifikasi asset).

## 6. Agenda workshop dosen satu hari

**Tujuan:** setiap dosen pulang dengan (a) baris peta MK-nya terisi, (b) mode F/E/R ditetapkan, (c) satu CPMK + assessment + artefak direvisi, (d) komitmen registrasi asset bila mode R.

**Peserta:** seluruh dosen pengampu Prodi Informatika; fasilitator: koordinator Metopen + tim kurikulum; pengambil keputusan: Kaprodi.

**Pra-workshop (dikirim H-7):** [MST-02 One-Page Concept](../00-master/02-one-page-concept.md), [ARC-01](01-research-capability-spiral.md), dokumen ini, RPS MK masing-masing.

| Waktu | Sesi | Isi | Output sesi |
|---|---|---|---|
| 08.30–09.00 | Pembukaan | Kaprodi: formula UIRP, mengapa sekarang, keputusan yang diharapkan hari ini | Kesepahaman tujuan |
| 09.00–10.00 | Sesi 1 — Research value chain & capability spiral | Presentasi ARC-01 + ARC-02; contoh Statistika → evidence reasoning, RPL → research-grade SE | Setiap dosen menandai posisi MK-nya pada rantai |
| 10.00–10.45 | Sesi 2 — Mode F/E/R | Decision tree ARC-03; latihan cepat: tiap dosen memutuskan mode MK-nya dan menuliskan alasannya | Daftar sementara mode per MK |
| 10.45–11.00 | Rehat | | |
| 11.00–12.00 | Sesi 3 — Kerja kelompok per klaster (C1–C4) | Kelompok mengisi baris peta untuk MK anggotanya: role, asset, contoh proyek; fasilitator per kelompok | Baris peta terisi untuk semua MK yang hadir |
| 12.00–13.00 | Ishoma | | |
| 13.00–14.00 | Sesi 4 — CPL → CPMK → Artifact → Evidence | Kerangka ARC-05; tiap dosen merevisi satu CPMK dan satu assessment agar mengikat research asset | Satu baris ARC-05 terisi per MK |
| 14.00–14.45 | Sesi 5 — Research asset, handoff, taksonomi output | ARC-04, ARC-06, TPL-14: bagaimana asset mengalir ke Metopen/backlog/registry; siapa owner | Rencana registrasi asset untuk MK mode R |
| 14.45–15.00 | Rehat | | |
| 15.00–15.45 | Sesi 6 — Gallery walk & komitmen | Setiap kelompok memaparkan 2 baris terbaik; dosen lain memberi satu masukan; pengisian folder `research-based-learning/courses/` dimulai | Draft README per MK |
| 15.45–16.00 | Penutupan | Kaprodi: keputusan (mode per MK disahkan sementara), tindak lanjut, tenggat penyerahan RPS revisi | Notulen keputusan + daftar tindak lanjut |

**Pasca-workshop (≤ 3 minggu):** tim kurikulum mengonsolidasikan peta final ke dokumen ini (PR `docs/curriculum-map`), dosen menyerahkan RPS revisi, koordinator Metopen memperbarui daftar MK sumber handoff.

**Aturan main workshop:** tidak ada MK yang dipaksa menjadi mode R; tidak ada tugas baru bila tugas lama bisa diarahkan; setiap keputusan mode dapat ditinjau ulang setiap semester.

## 7. Ringkasan

- Semua mata kuliah berada di research value chain; yang berbeda perannya, bukan keberadaannya.
- Research asset paling bernilai dari semester I–VI: notebook yang bisa dijalankan ulang, dataset card, benchmark harness, repositori reproducible, protokol user study, Experiment Card, dan Problem Brief.
- AI/ML (R), Data Mining (E→R), Proyek PL (E→R), dan Kerja Praktik (problem discovery) adalah sumber utama pipeline menuju Metopen dan TA.
- Peta ini hidup: diperbarui lewat workshop tahunan dan PR ke dokumen ini.

[^1]: Tabel kurikulum semester I–VIII dan positioning kompetensi Prodi berasal dari dokumen diskusi *Riset AI UAI untuk Negeri*; verifikasi terhadap dokumen kurikulum resmi sebelum dipakai dalam dokumen formal.
