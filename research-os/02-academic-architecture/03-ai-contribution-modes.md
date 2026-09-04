# AI Contribution Modes — Tiga Mode Kontribusi Mata Kuliah: F / E / R

> **ID** ARC-03 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen pengampu, koordinator mata kuliah, tim kurikulum, Kaprodi
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [ARC-02 Curriculum Research Map](02-curriculum-research-map.md) · [ARC-04 Build–Prove–Contribute](04-build-prove-contribute.md) · [ARC-05 CPL–CPMK–Artifact](05-cpl-cpmk-artifact-alignment.md) · [ARC-06 Research Output Taxonomy](06-research-output-taxonomy.md) · [TPL-14 Research Handoff](../08-templates/14-research-handoff-template.md) · [Faculty Guide](../../research-based-learning/faculty-guide/README.md)

## 1. Satu kalimat yang harus dipahami semua dosen

**Tidak semua mata kuliah harus melakukan riset. Setiap mata kuliah cukup ditandai satu huruf — F, E, atau R — dan memenuhi kewajiban minimum mode itu.**

Tanpa pembagian ini, dua hal buruk terjadi. Pertama, dosen mata kuliah fondasi merasa dipaksa "membuat riset" dari materi yang memang bukan riset, lalu menolak seluruh sistem. Kedua, mata kuliah yang sebenarnya sudah menghasilkan artefak riset (AI/ML, Proyek PL) tidak pernah mencatat dan mewariskan artefak itu karena tidak ada kewajiban yang jelas. Mode F/E/R membuat beban proporsional: kecil untuk sebagian besar MK, jelas untuk sedikit MK yang memang menjadi mesin pipeline.

## 2. Definisi tiga mode

| Mode | Nama | Definisi | Peran dalam pipeline | Contoh MK (default) |
|---|---|---|---|---|
| **F** | **Foundation** | Mata kuliah yang **mendukung kapabilitas** AI dan riset (statistik, matematika, algoritma, basis data) tanpa perlu memakai kasus AI atau menghasilkan artefak riset | Menanam *evidence reasoning*, *formal reasoning*, *baseline thinking* (Year 1–2 spiral) | Statistika, Kalkulus, Statistika Terapan, Matematika Diskrit, Struktur Data |
| **E** | **AI-Enriched** | Mata kuliah yang **memakai kasus atau proyek AI** sebagai bahan belajar, dengan sedikit lapisan riset (baseline, metrik, AI disclosure), tanpa kewajiban menghasilkan research asset terdaftar | Menghubungkan kompetensi teknis dengan cara berpikir riset; menyiapkan calon asset | HCI, RPL, Pengujian PL, Kerja Praktik, Etika Profesi, Basis Data (bila naik) |
| **R** | **Research-Producing** | Mata kuliah yang **menghasilkan reusable research asset** yang terdaftar dan di-handoff (dataset card, Experiment Card + repositori, benchmark, prototype terevaluasi, Research Pack) | Mesin pipeline Build → Prove → Contribute | AI & Machine Learning, Metodologi Penelitian, Tugas Akhir; kandidat: Data Mining, Proyek PL, NLP |

Tiga hal yang perlu ditegaskan:

1. Mode adalah **label kontribusi**, bukan peringkat mutu. MK bermode F tidak "lebih rendah" dari MK bermode R; ia hanya memberi kontribusi berbeda.
2. Mode melekat pada **mata kuliah pada semester tertentu**, bukan pada dosen. Mode dapat berubah antar semester.
3. Satu MK hanya punya **satu mode** pada satu waktu. Bila dosen ragu antara E dan R, pilih E dulu; naik ke R ketika kewajiban minimum R sudah realistis.

## 3. Kriteria masuk mode

| Kriteria | F Foundation | E AI-Enriched | R Research-Producing |
|---|---|---|---|
| Ada kasus/proyek AI dalam RPS? | Tidak wajib | **Ya**, minimal satu kasus atau satu proyek | Ya |
| Ada proyek/tugas yang menghasilkan artefak (kode/data/laporan eksperimen/prototype)? | Tidak wajib | Ya, tetapi artefak boleh berhenti di kelas | **Ya, dan artefak wajib reusable** |
| Dosen bersedia menjadi owner asset atau mentor awal? | Tidak | Tidak wajib | **Ya** (atau menunjuk dosen mitra) |
| Ada jalur handoff yang jelas (ke Metopen, backlog, registry, atau riset dosen)? | Tidak | Tidak wajib | **Ya** |
| Beban tambahan pada dosen | ≈ 0 (mengarahkan tugas yang ada) | Kecil (1 kasus AI + rubrik ditambah 2–3 kriteria) | Sedang (registrasi asset + handoff + review) |

Mata kuliah yang memenuhi kriteria R tetapi tidak siap memenuhi kewajibannya sebaiknya **ditandai E** dulu. Lebih baik satu MK R yang benar-benar menghasilkan asset daripada lima MK R yang hanya label.

## 4. Kewajiban minimum per mode

### 4.1 Mode F — Foundation

1. **Mengidentifikasi** dalam RPS satu–dua kompetensi riset yang ditopang MK ini (memakai tabel [ARC-01 §7](01-research-capability-spiral.md)), misalnya "evidence reasoning: membedakan korelasi dan kausalitas".
2. **Satu tugas** yang memakai data/kasus nyata (boleh publik atau anonim) dan menuntut mahasiswa menuliskan *apa yang boleh dan tidak boleh disimpulkan*.
3. Bila ada tugas komputasi: hasil dapat **dijalankan ulang** (notebook/skrip + data + langkah). Tidak perlu repositori formal.
4. Tidak ada kewajiban AI, registrasi, atau handoff.

### 4.2 Mode E — AI-Enriched

Semua kewajiban F, ditambah:

1. **Minimal satu kasus atau proyek AI** yang relevan dengan MK (contoh di [ARC-02 §3](02-curriculum-research-map.md)).
2. Rubrik proyek memuat minimal tiga kriteria riset: **baseline/pembanding**, **metrik dan cara mengukur**, **keterbatasan/threats to validity** (versi ringan).
3. **AI Usage Statement** ringkas pada setiap tugas yang boleh memakai AI generatif (siapa memakai apa untuk apa, diverifikasi bagaimana), mengikuti [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md).
4. Dosen **menandai** artefak terbaik kelas (1–3 per semester) sebagai *kandidat* research asset dan memberi tahu koordinator Metopen — tanpa kewajiban registrasi formal.

### 4.3 Mode R — Research-Producing

Semua kewajiban E, ditambah:

1. **Research asset terdaftar.** Setiap tim/mahasiswa menghasilkan minimal satu asset dari [ARC-06](06-research-output-taxonomy.md) yang **dicatat** di tempat yang sesuai: dataset → kartu di `datasets-registry/` ([TPL-05](../08-templates/05-dataset-registry-template.md)); masalah → Issue `type:problem` di research backlog ([TPL-04](../08-templates/04-research-backlog-template.md)); eksperimen/kode → repositori dari [TPL-15](../08-templates/15-research-repository-template.md) dengan Experiment Card ([TPL-09](../08-templates/09-experiment-card.md)); prototype/model → Issue `type:artifact`.
2. **Reproducibility minimum.** Repositori memuat README cara menjalankan, environment, seed, dan data/metadata; minimal satu kali direproduksi oleh peer.
3. **Baseline dan metrik ditetapkan sebelum eksperimen** dan tercatat (embrio G5 Method Ready).
4. **AI Usage Log** ([TPL-10](../08-templates/10-ai-usage-log-template.md)) untuk setiap tim, dinilai sebagai bagian rubrik.
5. **Handoff** ([TPL-14](../08-templates/14-research-handoff-template.md)) pada akhir semester untuk setiap asset yang layak dilanjutkan: *what exists, missing evidence, next steps, owner*. Tujuan handoff: Metopen, riset dosen, backlog, atau AI Research Center.
6. **Lisensi** dinyatakan mengikuti [LICENSING.md](../../LICENSING.md) (kode Apache-2.0, dokumen CC BY 4.0, dataset lewat review).
7. **Owner dosen** untuk setiap asset yang di-handoff (boleh dosen pengampu atau dosen mitra dari klaster terkait).
8. Dosen melaporkan ringkasan asset semester itu ke `research-based-learning/courses/<mk>/research-artifact.md`.

Untuk Metopen dan TA, kewajiban R diperluas oleh paket 04 (Research Pack, 8 gate, defense).

## 5. Contoh penetapan mode

| Mata kuliah | Mode disarankan | Alasan singkat |
|---|---|---|
| Statistika, Kalkulus, Matematika Diskrit, Struktur Data | F | Fondasi; tugas yang ada cukup diarahkan ke evidence/formal reasoning |
| Statistika Terapan | F (→E bila memakai dataset dari paper AI) | Replikasi analisis sudah cukup; kasus AI opsional |
| Basis Data | F (→E) | Dataset card v0 adalah kontribusi kecil tapi bernilai; naik ke E bila dipakai untuk data AI |
| HCI | E | User study pada sistem AI adalah kasus alami; asset boleh berhenti di kelas |
| Analisis Algoritma | F (→E) | Benchmark empiris; E bila objeknya algoritma ML |
| RPL | E | Repositori research-grade untuk proyek AI; kandidat R bila membangun tooling riset dosen |
| Data Mining | E (→R) | Laporan eksperimen dengan baseline; R bila dataset card dan repositori diregistrasi |
| AI & Machine Learning | **R** | Pintu masuk utama pipeline; Experiment Card + repo + handoff wajib |
| Pengujian Perangkat Lunak | E | Menguji sistem ML dari AI/ML; asset = test suite |
| Proyek Perangkat Lunak | E (→R) | Prototype AI terevaluasi; R bila prototype diregistrasi sebagai artefak dan di-handoff |
| Kerja Praktik | E | Problem Brief → backlog (registrasi ringan, bukan asset penuh) |
| Etika Profesi | F (→E) | Kajian etika kasus AI; E bila terhubung ke proyek tim lain |
| Metodologi Penelitian, Tugas Akhir | **R** | Prove dan Contribute |
| NLP, Keamanan, IoT (peminatan) | E (→R) | Bergantung kesiapan dosen dan ketersediaan data |

Daftar ini adalah usulan awal; keputusan resmi diambil dalam workshop dosen ([ARC-02 §6](02-curriculum-research-map.md)) dan dicatat di `research-based-learning/courses/`.

## 6. Decision tree untuk dosen

```
Mulai: mata kuliah saya
│
├─ Apakah ada (atau bisa ada tanpa menambah beban) kasus/proyek AI dalam MK ini?
│    ├─ Tidak ──────────────────────────────────────────────► MODE F
│    │        (kewajiban: identifikasi kompetensi riset + 1 tugas
│    │         "apa yang boleh/tidak boleh disimpulkan")
│    └─ Ya
│        │
│        ├─ Apakah proyek menghasilkan artefak (kode/data/eksperimen/prototype)
│        │  yang MASUK AKAL dipakai ulang di luar kelas?
│        │    ├─ Tidak ──────────────────────────────────────► MODE E
│        │    └─ Ya
│        │        │
│        │        ├─ Apakah saya (atau dosen mitra) bersedia menjadi owner
│        │        │  asset & mengisi handoff di akhir semester?
│        │        │    ├─ Tidak ──────────────────────────────► MODE E
│        │        │    │        (tandai artefak terbaik sebagai kandidat)
│        │        │    └─ Ya
│        │        │        │
│        │        │        ├─ Apakah ada jalur handoff yang jelas
│        │        │        │  (Metopen / backlog / registry / riset dosen)?
│        │        │        │    ├─ Tidak ─────────────────────► MODE E
│        │        │        │    │        (bangun jalurnya dulu bersama koordinator Metopen)
│        │        │        │    └─ Ya ────────────────────────► MODE R
│        │        │        │
```

Pertanyaan pengaman sebelum memilih R: *"Kalau semester depan saya tidak mengampu MK ini, apakah asset yang dihasilkan masih bisa ditemukan dan dilanjutkan orang lain?"* Kalau jawabannya tidak, itu belum R.

## 7. Dampak ke RPS dan penilaian

| Komponen RPS | Mode F | Mode E | Mode R |
|---|---|---|---|
| **CPMK** | Tambahkan/pertajam 1 CPMK bernuansa evidence reasoning (kata kerja: menafsirkan, membandingkan, membuktikan) | + 1 CPMK tentang evaluasi/klaim berbasis bukti pada kasus AI | + 1 CPMK tentang menghasilkan artefak riset reproducible dan mendokumentasikan penggunaan AI |
| **Materi** | Tidak berubah; satu pertemuan memakai contoh data nyata | 1–2 pertemuan memakai kasus AI | 2–3 pertemuan: baseline/metrik/leakage, reproducibility, AI Research Protocol |
| **Aktivitas** | Tugas data nyata + notebook | Proyek/kasus AI | Proyek mini-research dengan Experiment Card |
| **Assessment** | Rubrik tugas + kriteria "batas kesimpulan" | Rubrik proyek + 3 kriteria riset + AI Usage Statement | Rubrik proyek + kriteria reproducibility + AI Usage Log + handoff terisi; disarankan mengadopsi dimensi 5E ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)) versi ringan |
| **Bobot penilaian yang disarankan untuk komponen riset** | ≤ 10% | 15–25% | 30–50% (proyek) |
| **Bukti untuk akreditasi/PP-PTS** | RPS + contoh tugas | RPS + rubrik + contoh proyek | RPS + rubrik + asset terdaftar + handoff + registry ([GOV-05](../07-governance/05-ppts-and-institutional-evidence.md)) |
| **Integritas** | Aturan plagiarisme standar | + AI disclosure | + AI Usage Log; pelanggaran integritas = gagal komponen proyek |

Cara mengerjakan revisinya secara konkret ada di [ARC-05](05-cpl-cpmk-artifact-alignment.md).

## 8. Prosedur penetapan dan peninjauan mode

1. **Usulan**: dosen pengampu mengusulkan mode memakai decision tree; koordinator MK menyetujui.
2. **Pengesahan**: Kaprodi mengesahkan daftar mode per semester (biasanya dalam workshop dosen atau rapat kurikulum).
3. **Pencatatan**: mode, asset, klaster, owner ditulis di `research-based-learning/courses/<mk>/README.md`; ringkasan lintas MK di [research-based-learning/README.md](../../research-based-learning/README.md).
4. **Peninjauan**: setiap akhir semester, MK mode R melaporkan jumlah asset terdaftar dan handoff; MK yang dua semester berturut-turut tidak menghasilkan asset diturunkan ke E (tanpa sanksi); MK E yang konsisten menghasilkan kandidat asset ditawari naik ke R.
5. **Dukungan**: pusat riset menyediakan template, contoh, dan dosen mitra untuk MK yang naik ke R ([AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md)).

## 9. Kesalahan umum dan cara menghindarinya

| Kesalahan | Akibat | Cara menghindari |
|---|---|---|
| Menandai semua MK sebagai R agar "terlihat riset" | Asset palsu, handoff kosong, dosen kelelahan | Terapkan pertanyaan pengaman §6; batasi R pada 3–6 MK di awal |
| Mode E tanpa baseline/metrik dalam rubrik | Proyek AI tetap solution-first ("accuracy 93%, selesai") | Tiga kriteria riset wajib di rubrik E |
| Asset R dihasilkan tetapi tidak dicatat | Tidak ada yang tahu asset itu ada; Metopen mulai dari nol | Registrasi adalah kewajiban, bukan opsi; koordinator Metopen memeriksa tiap akhir semester |
| Handoff tanpa owner dosen | Asset yatim; mahasiswa lulus, asset hilang | Field *owner* wajib terisi dosen |
| Menganggap F "tidak penting" | Metopen harus mengajar ulang statistik dasar | Kewajiban F kecil tapi wajib; indikatornya dipantau ([ARC-01 §3](01-research-capability-spiral.md)) |

## 10. Ringkasan

- **F** menopang, **E** memperkaya, **R** menghasilkan. Satu huruf per MK per semester.
- Kewajiban F hampir nol; E kecil; R jelas: asset terdaftar, reproducible, baseline/metrik lebih dulu, AI Usage Log, handoff dengan owner.
- Pilih E bila ragu; naik ke R ketika jalur handoff dan owner sudah ada.
- Mode dicatat di `research-based-learning/courses/` dan ditinjau tiap semester.
