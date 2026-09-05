# Vision & Endgame — Begin with the End in Mind

> **ID** STR-02 · **Paket** 01 Strategic Foundation · **Tier** 1 (Core) · **Status** Draft v0.1 (2026-09)
> **Audiens** Kaprodi, tim kurikulum, dosen pengampu, mentor riset, pimpinan universitas
> **Terkait** [STR-01 Current State & Gaps](01-current-state-and-gaps.md) · [STR-03 Design Principles](03-design-principles.md) · [STR-05 Theory of Change](05-theory-of-change.md) · [MET-02 Metopen Course Outcomes](../04-metopen-research-studio/02-metopen-course-outcomes.md) · [ARC-06 Research Output Taxonomy](../02-academic-architecture/06-research-output-taxonomy.md)

Dokumen ini menjawab layer kedua: **mahasiswa seperti apa yang ingin dihasilkan, dan institusi seperti apa yang terbentuk sebagai akibatnya?** Semua desain di paket 02–08 harus dapat ditelusuri balik ke endgame yang dituliskan di sini.

---

## 1. Begin with the end in mind

Kita tidak mendesain mata kuliah lalu berharap ada hasilnya. Kita menetapkan hasil akhir, lalu bekerja mundur: lulusan seperti apa → kemampuan apa → bukti apa yang menunjukkan kemampuan itu → aktivitas apa yang menghasilkan bukti itu → minggu ke berapa dan gate mana. Itu sebabnya Metopen dimulai dengan G1 *Endgame Ready* pada minggu pertama: mahasiswa harus menyatakan riset ini mau menjadi apa sebelum mengerjakan apa pun.

Endgame ditetapkan pada dua level: **mahasiswa** (north star personal) dan **institusi** (compounding loop).

## 2. North star mahasiswa: scientific thinker

> **Scientific thinker**: orang yang mampu menghasilkan *credible evidence* dan *contribution*, serta sulit dibohongi — termasuk oleh AI-nya sendiri ([MST-03](../00-master/03-glossary.md)).

Epistemologi mahasiswa berubah dalam tiga langkah:

| Dari | Ke | Lalu ke |
|---|---|---|
| "Saya membuat sesuatu." | "Saya membuat klaim yang dapat diuji." | "Saya memiliki bukti yang cukup kuat untuk mempertanggungjawabkan klaim tersebut." |

Yang dilatih bukan hafalan jenis penelitian, melainkan alur *research thinking*: fenomena/masalah nyata → apa yang kita ketahui → apa yang belum → apa yang kita klaim → bukti apa yang membuat klaim itu dapat dipercaya → desain riset apa yang menghasilkan bukti itu → data/artefak/eksperimen apa yang diperlukan → apa yang bisa membatalkan kesimpulan → bisakah orang lain memeriksa/mereproduksi → *so what?*

## 3. Empat level outcome

Empat level ini adalah *maturity* riset sekaligus level capaian mahasiswa. Keempatnya dipetakan ke gate ([OPS-03](../06-execution-os/03-research-gates.md)) dan label `maturity:*` di GitHub.

### 3.1 TA Ready — minimum (wajib 100%)

| Aspek | Isi |
|---|---|
| Definisi | Mahasiswa masuk semester VIII **tanpa lagi mencari judul dan metode**. Problem, evidence map, gap, RQ, desain, data plan, baseline, dan metrik sudah tervalidasi. |
| Setara gate | Lolos **G5 Method Ready** (termasuk Design Defense W8) |
| Indikator | Research One-Pager v1 disetujui; Research Design Card lengkap; dataset teridentifikasi dan aksesnya jelas; pembimbing TA dapat memulai bimbingan dari dokumen, bukan dari percakapan "mau meneliti apa?" |
| Contoh output | Proposal TA yang diturunkan dari Research Pack; Issue `type:research-question` tertutup lolos; release `v0.3 Research Design` |
| Bukti gagal | Mahasiswa mengganti topik di semester VIII karena desainnya tidak viable |

### 3.2 Research Ready — target

| Aspek | Isi |
|---|---|
| Definisi | Mahasiswa **mampu menjalankan satu penelitian computing sederhana secara benar**: eksperimen berjalan, direproduksi orang lain, klaim tidak melebihi bukti. |
| Setara gate | Lolos **G6 Experiment Ready** dan **G7 Claim Ready** |
| Indikator | Pilot experiment end-to-end pada subset data dengan baseline; peer berhasil mereproduksi angka baseline; tabel Claim–Evidence–Reasoning untuk setiap RQ; threats to validity diperbarui berdasarkan hasil nyata; hasil negatif dilaporkan |
| Contoh output | Release `v0.5 Pilot Experiment`; `results/analysis.md`; repository dengan seed, environment, dan README eksekusi |
| Bukti gagal | Hasil hanya ada di laptop anggota tim; klaim kausal dari korelasi; improvement tanpa baseline |

### 3.3 Publication Ready — aspirasional

| Aspek | Isi |
|---|---|
| Definisi | Hasil **layak menjadi paper, dataset, atau artefak** yang dapat direview pihak luar. |
| Setara gate | Lolos **G8 Contribution Ready** + status *manuscript-ready* ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)) |
| Indikator | Research Pack v1.0 lengkap; manuscript draft mengikuti format venue target dari venue registry non-predator; peer review internal lolos; AI Usage Statement dan integrity checklist ditandatangani |
| Contoh output | Release `v0.8 Manuscript Draft` → `v1.0 Research Pack`; entri `PUB-YYYY-NNN` di [`publications/`](../../publications/README.md); dataset dengan `DS-YYYY-NNN` |
| Bukti gagal | Naskah ditargetkan ke venue yang tidak lolos venue registry; klaim di abstrak tidak didukung tabel |

### 3.4 Impact Ready — aspirasional lanjutan

| Aspek | Isi |
|---|---|
| Definisi | Hasil menjadi **HKI, prototype, bagian riset dosen, atau solusi industri/masyarakat**. |
| Setara gate | Setelah G8; kolom *Published/Released* di Mission Control |
| Indikator | Artefak dirilis (`ART-YYYY-NNN`) dengan lisensi jelas setelah IP review; diadopsi stakeholder yang disebut di Problem Brief; menjadi bagian proposal hibah dosen atau program klaster |
| Contoh output | Release `v2.0 Published`; HKI terdaftar; prototype dipakai partner; Research ID muncul di Faculty Portfolio dosen |
| Bukti gagal | "Impact" hanya berupa klaim di kesimpulan tanpa stakeholder yang benar-benar memakai |

Target distribusi per angkatan disepakati di [GOV-03](../07-governance/03-kpi-and-measurement.md): 100% TA Ready adalah syarat lulus; Research Ready target mayoritas; Publication/Impact Ready untuk tim terbaik.

## 4. Backward reasoning dari lulusan ideal

Lima tahun setelah lulus, tidak penting apakah alumni masih ingat perbedaan penelitian deskriptif dan korelasional. Yang penting: ketika mereka menjadi **AI engineer, software engineer, product manager, entrepreneur, researcher, consultant, atau decision maker**, mereka otomatis bertanya:

1. **Apa problem sebenarnya?**
2. **Apa yang kita ketahui vs hanya kita asumsikan?**
3. **Apa evidence-nya?**
4. **Apa baseline-nya?**
5. **Bagaimana kita mengujinya?**
6. **Apa biasnya?**
7. **Apa yang bisa membuat kesimpulan ini salah?**
8. **Bisakah orang lain memverifikasinya?**

Dari delapan pertanyaan itu, mundur ke kemampuan yang harus terbentuk, lalu ke tempat kemampuan itu dilatih:

| Pertanyaan alumni | Kemampuan | Dilatih di | Bukti di Research Pack |
|---|---|---|---|
| Apa problem sebenarnya? | Problem framing, stakeholder analysis | W2 Problem, G2 | Problem Brief, Stakeholder/Impact Statement |
| Apa yang kita ketahui vs asumsi? | Literature intelligence, synthesis | W3–W5, G3 | Literature Evidence Map, synthesis matrix |
| Apa evidence-nya? | Evidence literacy, CER | W11–W12, G7 | Tabel Claim–Evidence–Reasoning |
| Apa baseline-nya? | Measurement & evaluation design | W7, G5 | Baseline & Metrics |
| Bagaimana kita mengujinya? | Research design, experiment | W7–W10, G5–G6 | Research Design, Pilot Experiment |
| Apa biasnya? | Validity & ethics reasoning | W7, W12, G5, G7 | Threats to Validity, Ethics & Privacy |
| Apa yang bisa membuat kesimpulan salah? | Falsification, red teaming | W8 Design Defense, W14 Peer Review | Notulen red team, peer review |
| Bisakah orang lain memverifikasi? | Reproducibility, disclosure | W9 Repository, G6, G8 | Reproducibility README, AI Usage Statement |

Peran per profesi (mengapa endgame ini relevan bagi yang tidak menjadi akademisi):

| Profesi | Pertanyaan yang paling menyelamatkan | Tanpa research thinking |
|---|---|---|
| AI engineer | Apa baseline-nya? Bagaimana leakage dicegah? | Model "akurasi 93%" yang gagal di produksi |
| Software engineer | Apa evidence bahwa perubahan ini memperbaiki? | Optimasi berdasarkan anggapan |
| Product manager | Apa problem sebenarnya, untuk siapa? | Fitur yang tidak dipakai |
| Entrepreneur | Apa yang kita asumsikan? Bagaimana mengujinya murah? | Membangun sebelum memvalidasi |
| Consultant / decision maker | Apa yang bisa membuat rekomendasi ini salah? | Keputusan berbasis klaim yang terdengar meyakinkan |
| Researcher | Semua delapan | Riset lemah, tidak dapat direproduksi |

## 5. Research method sebagai operating system berpikir

Metodologi penelitian dalam desain ini bukan *content* yang dihafal, melainkan *operating system* yang menjalankan cara berpikir apa pun di atasnya. Implikasinya:

- Metopen tidak mengajarkan "jenis-jenis penelitian" sebagai bab; ia mengajarkan **satu siklus** yang dijalankan sendiri oleh mahasiswa, dengan konsep dimasukkan tepat saat dibutuhkan (*just-in-time*), sekitar 30% dari waktu.
- Setiap konsep diuji lewat artefak: mahasiswa tidak "memahami threats to validity", mahasiswa **menulis** threats to validity risetnya sendiri dan mempertahankannya di depan red team.
- AI dipakai sebagai *cognitive accelerator* di dalam OS ini, bukan sebagai OS pengganti: protokol Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)) adalah *kernel*-nya.
- Sepuluh meta-skill (problem framing, decomposition, abstraction, first principles, hypothesis, falsification, evidence literacy, causal/statistical reasoning, systems thinking, metacognition) adalah *system call* yang dipanggil berulang sepanjang 16 minggu ([AIX-01](../05-ai-augmented-research/01-research-meta-thinking.md)).

Positioning final Metopen sebagai konsekuensinya: *research studio yang melatih mahasiswa mengubah masalah nyata menjadi pertanyaan ilmiah, membangun argumentasi berbasis literatur, merancang metode dan eksperimen yang valid, menggunakan AI secara bertanggung jawab, menghasilkan evidence dan artefak yang reproducible, serta mempertanggungjawabkan temuannya secara ilmiah, etis, dan profesional sebagai fondasi Tugas Akhir dan karya penelitian berikutnya* ([MET-01](../04-metopen-research-studio/01-metopen-positioning.md)).

## 6. Endgame institusional: compounding barokah loop

Pada level institusi, endgame-nya bukan "nilai Metopen membaik", melainkan terbentuknya siklus yang menguat sendiri:

```
 satu mata kuliah (Metopen sebagai Research Studio)
        │
        ▼
 TA lebih baik ──► mahasiswa lebih capable ──► riset dosen lebih kuat
        ▲                                              │
        │                                              ▼
 mahasiswa berikutnya                             publikasi, artefak, HKI
 mendapat research                                     │
 environment lebih baik                                ▼
        ▲                                        reputasi prodi
        │                                              │
 problem lebih berkualitas ◄── kolaborasi & partner ◄──┘
```

Setiap putaran meninggalkan **research asset** di repository (dataset terdaftar, kode, benchmark, problem brief, literature map) sehingga angkatan berikutnya tidak memulai dari nol. Inilah arti *compounding*: nilainya bertambah karena diwariskan, bukan karena diulang. Disebut *barokah* karena hasil yang jujur — yang diperoleh dengan amanah epistemik — adalah hasil yang layak diwariskan.

Indikator bahwa loop mulai berputar (rincian di [GOV-03](../07-governance/03-kpi-and-measurement.md)):

| Putaran | Tanda |
|---|---|
| 1 (pilot) | 100% tim Metopen TA Ready; Research Pack v1.0 dipakai pembimbing TA |
| 2 | Riset TA melanjutkan Research Pack tanpa ganti topik; dosen mengambil mahasiswa TA-ready ke skema penelitian internal |
| 3 | Dataset dan kode angkatan sebelumnya dipakai ulang oleh tim baru; backlog berisi problem dari partner |
| 4+ | Publikasi mahasiswa–dosen rutin; Faculty Portfolio menjadi evidence akreditasi dan hibah; AI Research Center menjadi hub lintas fakultas |

Arah ini kompatibel dengan visi Prodi yang menyebut problem solving, agent of change, riset melalui laboratorium, kolaborasi eksternal, dan landasan spiritual-moral-etika Islami (sumber: dokumen diskusi; verifikasi sebelum dokumen formal).

## 7. Yang bukan endgame

Untuk mencegah salah sasaran, berikut yang **bukan** ukuran keberhasilan:

- Jumlah proposal yang dikumpulkan tepat waktu (itu deadline, bukan gate).
- Jumlah publikasi tanpa memandang venue (lihat *publication oriented, not publication obsessed* di [STR-03](03-design-principles.md)).
- Jumlah Issue atau commit (aktivitas ≠ kematangan riset).
- Nilai rata-rata Metopen (nilai adalah konsekuensi rubrik 5E, bukan tujuan).
- Semua mahasiswa menjadi peneliti (endgame-nya scientific thinker di profesi apa pun).

Prinsip yang menjaga endgame ini tetap pada jalurnya: [STR-03 Design Principles](03-design-principles.md). Rantai sebab-akibat lengkapnya: [STR-05 Theory of Change](05-theory-of-change.md).
