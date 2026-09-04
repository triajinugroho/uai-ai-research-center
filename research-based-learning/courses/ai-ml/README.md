# AI & Machine Learning — Course Research Guide

**Status** Draft v0.1 (2026-09) · Phase 3 Curriculum Integration — artefak riil menyusul
**Terkait** [Hub Research-Based Learning](../../README.md) · [research-artifact.md](research-artifact.md) · [ARC-01 Capability Spiral](../../../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-02 Curriculum Research Map](../../../research-os/02-academic-architecture/02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-04 Build–Prove–Contribute](../../../research-os/02-academic-architecture/04-build-prove-contribute.md) · [ARC-05 CPL–CPMK–Artifact](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [Assessment](../../assessment/README.md) · [Faculty Guide](../../faculty-guide/README.md)

## 1. Identitas mata kuliah

| Field | Nilai |
|---|---|
| Nama | AI & Machine Learning |
| Semester | V |
| SKS | 4 |
| Mode ([ARC-03](../../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) | **R — Research-Producing** |
| Tahun spiral ([ARC-01](../../../research-os/02-academic-architecture/01-research-capability-spiral.md)) | Year 3 — Experiment & Evaluate |
| Entry door yang dibuka | **Course Project** (pintu masuk utama riset mahasiswa ke pipeline) |
| Klaster utama | C1 AI Models, Data & Knowledge |
| Klaster sekunder | C4 Applied AI for Human Flourishing (bila proyek berdomain), C3 Human-Centered & Responsible AI (evaluasi fairness/robustness) |
| Field **Course** di Mission Control | `AI/ML` |
| Pengampu | [isi] |
| Asisten/mentor riset | [isi] |

*Semester dan SKS dari tabel kurikulum dokumen diskusi; verifikasi sebelum dokumen formal.*

## 2. Mengapa mode R

AI/ML adalah mata kuliah teknis terbesar (4 SKS) sebelum Metopen dan berada tepat di tahun spiral *Experiment & Evaluate*. Tiga alasan ia ditetapkan sebagai mode R, bukan sekadar E:

1. **Proyeknya sudah berbentuk eksperimen.** Setiap proyek AI/ML memiliki data, model, dan angka. Yang kurang hanyalah disiplin: baseline sebelum model, metrik sebelum hasil, seed dan split yang dicatat, error analysis setelah angka. Menambahkan disiplin itu tidak menambah beban, tetapi mengubah proyek menjadi *research asset*.
2. **Ia menjadi bahan baku Metopen.** Dokumen sumber menempatkan alur **AI/ML → Metopen → TA** sebagai peluang utama. Mahasiswa yang masuk Metopen dengan Experiment Card dan repo reproducible memulai W1 dari posisi berbeda dengan yang masuk dengan "ide judul".
3. **Ia mengisi registry.** Dataset card dan baseline dari kelas ini adalah entri pertama `datasets-registry/` dan kandidat backlog yang paling realistis.

Konsekuensi mode R: research asset di [research-artifact.md](research-artifact.md) yang bertanda **wajib** menjadi bagian penilaian, dan minimal satu artefak per tim tercatat di registry/backlog/handoff pada akhir semester.

## 3. Peran dalam research value chain

Menurut [ARC-02](../../../research-os/02-academic-architecture/02-curriculum-research-map.md), AI/ML adalah **AI Core** dalam value chain: tempat mahasiswa pertama kali merancang eksperimen ML dengan hipotesis, variabel, kontrol, baseline, metrik yang selaras tujuan, ablation/error analysis, dan variansi antar seed. Kompetensi yang ia tumbuhkan (ARC-01 §5):

- Experimental design untuk ML.
- Evaluasi multi-dimensi: bukan hanya accuracy — robustness, fairness awal, biaya, kegunaan.
- Reproducibility: repo eksperimen yang dapat dijalankan orang lain.
- AI Investigator: memakai AI untuk mengkritik desain eksperimen dan membangkitkan hipotesis alternatif, dengan verifikasi.

Yang **tidak** diminta dari AI/ML: literature synthesis matrix, RQ formal, threats to validity lengkap. Itu pekerjaan Metopen (Prove). AI/ML membangun (Build).

## 4. CPMK riset yang ditambahkan

Kerangka [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md): CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence. Empat CPMK riset di bawah **ditambahkan** pada CPMK teknis yang sudah ada, bukan menggantikannya.

| # | CPMK riset (tambahan) | Learning activity | Assessment | Research artifact | Evidence |
|---|---|---|---|---|---|
| R1 | Mahasiswa mampu merancang eksperimen ML dengan hipotesis, baseline, dan metrik yang ditetapkan **sebelum** eksperimen dijalankan | Studio Experiment Card (minggu 5–6) | Rubrik research-quality §7 (kriteria baseline, metrik) | Experiment Card ([TPL-09](../../../research-os/08-templates/09-experiment-card.md)) | Commit Experiment Card bertanggal sebelum commit hasil |
| R2 | Mahasiswa mampu mendokumentasikan data yang dipakai (sumber, lisensi, privasi, split, leakage risk) dalam dataset card | Studio dataset card (minggu 3–4) | Checklist dataset card | Dataset card v0 ([TPL-05](../../../research-os/08-templates/05-dataset-registry-template.md)) | Kartu masuk `datasets-registry/` atau ditolak dengan alasan tercatat |
| R3 | Mahasiswa mampu menghasilkan eksperimen yang direproduksi tim lain dari repositori (kode, seed, environment, README) | Peer reproduction (minggu 12–13) | Kriteria reproducibility §7 | Notebook/repo reproducible ([TPL-15](../../../research-os/08-templates/15-research-repository-template.md)) | Catatan reproduksi peer di `experiments/README.md` |
| R4 | Mahasiswa mampu menganalisis error dan melaporkan klaim yang tidak melebihi bukti, termasuk mengungkap penggunaan AI | Sesi error analysis + AI disclosure (minggu 11, 14) | Kriteria AI disclosure §7; laporan akhir | Research One-Pager v0 ([TPL-01](../../../research-os/08-templates/01-research-one-pager-template.md)) + AI Usage Log ([TPL-10](../../../research-os/08-templates/10-ai-usage-log-template.md)) | One-pager memuat baseline, metrik, hasil, keterbatasan; log AI terisi |

## 5. Project guide — proyek berorientasi riset

### 5.1 Bentuk proyek

| Aspek | Ketentuan |
|---|---|
| Tema | Dipilih dari [`research-backlog/BACKLOG.md`](../../../research-backlog/BACKLOG.md) (Issue `type:problem` berlabel `cluster:models` atau `cluster:applied`), dari dataset di [`datasets-registry/REGISTRY.md`](../../../datasets-registry/REGISTRY.md), atau dari masalah nyata yang diusulkan tim dan disetujui pengampu. Tema yang berangkat dari "saya ingin memakai algoritma X" dikembalikan untuk ditulis ulang *problem-first*. |
| Tim | 2–3 mahasiswa. Peran bergilir: data owner, experiment owner, reproducibility owner. |
| Data | Dataset publik berlisensi jelas, dataset registry, atau data yang sudah dianonimkan. Data pribadi/partner **tidak** masuk repo ([SECURITY.md](../../../SECURITY.md)). |
| Repositori | Dibuat dari [TPL-15](../../../research-os/08-templates/15-research-repository-template.md) sejak minggu 2; nama `proj-YYYY-<topik>` bila diproyeksikan lanjut ke Metopen, atau repo kelas bila belum. |
| AI | Mengikuti [AI Research Protocol (AIX-04)](../../../research-os/05-ai-augmented-research/04-ai-research-protocol.md); AI Usage Log wajib sejak minggu 1. |
| Endgame yang diminta | Minimal: research asset terdaftar. Target: handoff ke Metopen. Aspirasi: kandidat backlog `UIAI-` dengan dataset `DS-`. |

### 5.2 Timeline satu semester (16 minggu, 5 milestone)

| Milestone | Minggu | Pertanyaan yang dijawab | Deliverable | Gate embrio |
|---|---|---|---|---|
| **M1 Problem & Data** | 3 | Masalah apa, siapa yang peduli, data apa, boleh dipakai atau tidak? | Problem statement 1 halaman (problem-first), **dataset card v0**, repo dari TPL-15, AI Usage Log dimulai | G2, G5 (data plan) |
| **M2 Baseline** | 6 | Pembanding paling sederhana apa, metrik apa, split bagaimana? | **Experiment Card** (hipotesis, baseline, variabel, metrik, kontrol, threats awal) + **baseline experiment** berjalan end-to-end | G5 |
| **M3 Method & Comparison** | 10 | Apakah metode yang diusulkan mengungguli baseline pada metrik yang ditetapkan, dengan variansi antar seed? | Hasil ≥ 1 metode pembanding + baseline, ≥ 3 seed/fold, tabel hasil di `results/` | G6 |
| **M4 Reproduce & Analyze** | 13 | Bisakah tim lain mereproduksi angka baseline; di mana model gagal? | **Peer reproduction** oleh tim lain (catatan di `experiments/README.md`), **error analysis** (confusion/kasus gagal/slice), threats to validity awal | G6, G7 |
| **M5 One-Pager & Handoff** | 15–16 | Apa klaim yang layak, apa yang belum terbukti, dilanjutkan oleh siapa? | **Research One-Pager v0**, presentasi 7 menit, AI Usage Statement, [handoff TPL-14](../../../research-os/08-templates/14-research-handoff-template.md) untuk tim yang lanjut | G7 (klaim), handoff |

Minggu 1–2 dipakai untuk pembentukan tim, pembacaan protokol AI, dan pemilihan tema dari backlog. Milestone dinilai lewat *milestone portfolio* (lihat [Assessment](../../assessment/README.md)); tidak ada UTS/UAS hafalan untuk komponen proyek.

### 5.3 Hubungan ke backlog dan datasets-registry

- **Masuk:** tema diambil dari backlog/registry (*reuse before create*). Bila tim membuat tema baru, tim membuka Issue *Research Problem* pada minggu 3 sehingga masalahnya tercatat sekalipun proyek berhenti di akhir semester.
- **Keluar:** dataset card v0 diserahkan ke pengelola `datasets-registry/` (ID `DS-YYYY-NNN` diberikan bila lolos verifikasi metadata); Research One-Pager v0 dilampirkan ke Issue backlog; tim yang lanjut ke Metopen membawa Research ID sementara (format sementara sesuai [CONTRIBUTING.md §2](../../../CONTRIBUTING.md)) yang diresmikan menjadi `UIAI-YYYY-NNN` saat lolos G2 di Metopen.

## 6. Rubrik ringkas research-quality

Rubrik ini menilai komponen proyek (bobot ditentukan pengampu dalam RPS). Rubrik lengkap dan kalibrasi antar dosen: [Assessment §4](../../assessment/README.md). **Research Integrity gate** berlaku lulus/gagal di atas rubrik ini: fabrikasi angka, sitasi palsu, atau AI yang tidak diungkap membuat proyek gagal terlepas dari skor.

| Kriteria | 1 — Belum | 2 — Dasar | 3 — Baik | 4 — Research-quality |
|---|---|---|---|---|
| **Baseline** | Tidak ada baseline; model dibandingkan dengan dirinya sendiri | Baseline ada tetapi dipilih setelah hasil, atau tidak masuk akal (terlalu lemah) | Baseline sederhana yang masuk akal, ditetapkan sebelum eksperimen | Baseline + ≥ 1 pembanding kuat; alasan pemilihan ditulis; hasil baseline direproduksi peer |
| **Metrik & evaluasi** | Hanya accuracy tanpa alasan; split tidak dijelaskan | Metrik disebut; split ada tetapi leakage tidak diperiksa | Metrik selaras tujuan; split/CV benar; leakage diperiksa | Metrik multi-dimensi (kinerja + robustness/fairness/biaya bila relevan); variansi antar seed; signifikansi praktis dibahas |
| **Reproducibility** | Hasil hanya ada di laptop anggota | Kode ada, tetapi environment/seed/langkah tidak lengkap | README, environment, seed, skrip; tim sendiri bisa menjalankan ulang | Peer dari tim lain mereproduksi angka baseline tanpa bertanya; log eksperimen tersimpan |
| **AI disclosure & integritas** | Tidak ada AI Usage Log, atau log tidak mencerminkan pekerjaan | Log ada tetapi verifikasi tidak dicatat | Log lengkap; kode bantuan AI diuji; AI Usage Statement di laporan | Log menunjukkan verifikasi sumber/penalaran/bukti; kekeliruan AI yang ditemukan dicatat; klaim tidak melebihi bukti |

Tim yang mencapai level 4 pada ≥ 3 kriteria direkomendasikan untuk handoff ke Metopen dengan catatan pengampu.

## 7. Template yang dipakai

| Kebutuhan | Template |
|---|---|
| Kartu dataset | [TPL-05 Dataset Registry Template](../../../research-os/08-templates/05-dataset-registry-template.md) |
| Rancangan eksperimen | [TPL-09 Experiment Card](../../../research-os/08-templates/09-experiment-card.md) |
| Repositori | [TPL-15 Research Repository Template](../../../research-os/08-templates/15-research-repository-template.md) |
| Log AI | [TPL-10 AI Usage Log](../../../research-os/08-templates/10-ai-usage-log-template.md) |
| Ringkasan riset | [TPL-01 Research One-Pager](../../../research-os/08-templates/01-research-one-pager-template.md) |
| Handoff | [TPL-14 Research Handoff](../../../research-os/08-templates/14-research-handoff-template.md) |
| Integritas (akhir semester) | [TPL-11 Research Integrity Checklist](../../../research-os/08-templates/11-research-integrity-checklist.md) |
| Rancangan riset (opsional, tim yang lanjut) | [TPL-08 Research Design Card](../../../research-os/08-templates/08-research-design-card.md) |

Salinan template yang disesuaikan untuk kelas dapat diletakkan di `templates/` dalam folder ini.

## 8. Catatan RPS

`RPS.md` akan ditambahkan oleh pengampu; kerangka revisi lihat [ARC-05](../../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md). Prinsip revisi: CPMK teknis tetap; empat CPMK riset §4 ditambahkan; komponen proyek dinilai dengan milestone portfolio §5.2 dan rubrik §6; AI Usage Log menjadi lampiran wajib laporan.

## 9. Pengampu

| Peran | Nama |
|---|---|
| Pengampu | [isi] |
| Pengampu pendamping / asisten | [isi] |
| Mentor riset dari klaster C1 | [isi] |
