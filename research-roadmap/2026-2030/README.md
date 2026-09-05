# Roadmap 2026–2030 — Lima Tahun, Lima Tahap

> **Status** Draft v0.1 (2026-09) · **Terkait** [Research Roadmap README](../README.md) · [GOV-02 Implementation Roadmap](../../research-os/07-governance/02-implementation-roadmap.md) · [GOV-03 KPI & Measurement](../../research-os/07-governance/03-kpi-and-measurement.md) · [GOV-04 Risk Register](../../research-os/07-governance/04-risk-register.md) · [STR-05 Theory of Change](../../research-os/01-strategic-foundation/05-theory-of-change.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

Roadmap ini menjabarkan **arah riset** per tahun. Ia sejajar dengan dua skema fase yang penomorannya berbeda — fase GitHub di [GOVERNANCE.md §10](../../GOVERNANCE.md) (GitHub Phase 0 Foundation · 1 Research OS · 2 Pilot Metopen · 3 Curriculum Integration · 4 AI Center Launch · 5 Public Research Portal) dan fase akademik di [GOV-02](../../research-os/07-governance/02-implementation-roadmap.md) (GOV-02 Phase 0 Design · 1 Pilot Metopen · 2 Integrate AI/ML · 3 Expand technical courses · 4 AI Research Center integration · 5 Scale cross-faculty); setiap penyebutan nomor fase di dokumen ini menyebut skemanya. Sudut pandang roadmap ini berbeda dari keduanya: GOV-02 menjawab *kapan sistem siap*, roadmap ini menjawab *riset apa yang dikejar ketika sistem itu siap*. Target angka tidak diulang di sini; semuanya merujuk ke [GOV-03](../../research-os/07-governance/03-kpi-and-measurement.md).

## 1. Ringkasan satu tabel

| Tahun | Tahap | Fokus riset | Program yang dibuka | Milestone institusional |
|---|---|---|---|---|
| **2026** | Foundation & Pilot Metopen *(GitHub Phase 0–2 / GOV-02 Phase 0–1)* | Riset skala kecil dari masalah kampus sendiri: **C3 × Education**, **C1 × Education/Government**, **C4 × Halal** | belum ada repo `program-*`; sel matriks dijalankan lewat `proj-2026-*` | Research OS v0.1; angkatan pilot Metopen; Research ID pertama; datasets-registry terisi metadata |
| **2027** | Curriculum Integration & program unggulan *(GitHub Phase 3 / GOV-02 Phase 2–3)* | Mata kuliah mode R menghasilkan research asset; riset TA dari Research Pack angkatan 2026 | `program-ai-education`, `program-responsible-ai` | RPS AI/ML, Data Mining, NLP, Metopen, TA yang terhubung; Faculty Portfolio pertama |
| **2028** | AI Center Launch & cross-faculty *(GitHub Phase 4 / GOV-02 Phase 4)* | Klaster dosen aktif; masalah dari fakultas lain dan partner; C2 mulai dibuka lebar | `program-ai-halal`, `program-ai-health` | Peluncuran resmi pusat riset AI; MoU/kerja sama pertama dengan partner; mid-term review roadmap |
| **2029** | Public Portal & scaling *(GitHub Phase 5 / GOV-02 Phase 5)* | Publikasi dan artefak dari program; dataset UAI yang dapat dibagikan; benchmark berbahasa Indonesia | `program-indonesian-llm` | GitHub menjadi portal publik pusat riset; dashboard otomatis; dataset/benchmark pertama dirilis publik |
| **2030** | Evaluasi & agenda berikutnya *(GitHub Phase 5 / GOV-02 Phase 5, akhir horizon)* | Konsolidasi: replikasi, meta-analisis internal, studi dampak | tidak ada program baru; program yang ada dievaluasi lanjut/ubah/hentikan | End-of-horizon review; roadmap 2031–2035; evidence untuk siklus akreditasi berikutnya |

Urutan pembukaan program disengaja: **pendidikan** dan **responsible AI** lebih dulu karena masalah, data, dan pemangku kepentingannya ada di dalam kampus (risiko akses data rendah, hasil cepat terlihat). **Halal** dan **kesehatan** menyusul setelah ada mitra lintas fakultas dan tata kelola data sensitif teruji. **Indonesian LLM** paling akhir karena membutuhkan compute, korpus, dan kematangan evaluasi yang dibangun oleh program-program sebelumnya.

Tahun pada kolom *Program yang dibuka* adalah **target paling awal** dan hanya berlaku bila syarat §3 terpenuhi. [GOV-02](../../research-os/07-governance/02-implementation-roadmap.md) menempatkan pembuatan repo `program-*` dan target *≥2 repo `program-*` aktif* pada GOV-02 Phase 4 / GitHub Phase 4 (AI Center Launch, semester ganjil 2028/2029); pembukaan dua program unggulan pada 2027 memenuhi target itu lebih awal, dan bila syarat §3 belum terpenuhi pada 2027, pembukaannya bergeser ke 2028 tanpa mengubah urutan.

## 2. Rincian per tahun

### 2026 — Foundation & Pilot Metopen

**Fokus riset.** Masalah yang bisa diakses tanpa perjanjian eksternal: layanan akademik, pembelajaran, dokumen/regulasi kampus, dan produk halal yang datanya publik. Semua riset berskala pilot: satu semester Metopen + satu semester TA.

| Aspek | Isi |
|---|---|
| Sel matriks aktif | C3 × Education (academic advising, AI literacy); C1 × Education/Government (RAG dokumen akademik & regulasi); C4 × Halal (klasifikasi citra produk/label) |
| Program dibuka | — (repo `program-*` belum dibuat; lihat aturan di [README](../README.md) §3.3) |
| Target output | KPI *leading* GOV-03: Research One-Pager, RQ tervalidasi, repositori, pilot experiment untuk angkatan pilot Metopen |
| Milestone institusional | GitHub Phase 0–2 (Foundation, Research OS, Pilot Metopen) = GOV-02 Phase 0–1 (Design, Pilot Metopen) selesai; [BACKLOG.md](../../research-backlog/BACKLOG.md) berisi masalah tervalidasi G2; [REGISTRY.md](../../datasets-registry/REGISTRY.md) berisi kartu dataset pertama; pelatihan dosen reviewer gate |
| Bukti yang dicari | apakah alur Issue → gate → Research Pack berjalan dengan beban dosen yang wajar |

### 2027 — Curriculum Integration & program unggulan

**Fokus riset.** Research asset dari mata kuliah teknis (AI/ML, Data Mining, NLP, RPL) mulai dipakai ulang; TA angkatan pilot menghasilkan hasil pertama yang lolos G7–G8. Dua program unggulan dibuka ketika syarat §3.3 README terpenuhi.

| Aspek | Isi |
|---|---|
| Sel matriks aktif | semua sel 2026 + C3 × Business/Social Impact (keputusan manusia berbantuan AI); C1 × Social Impact (bahasa daerah, low-resource) |
| Program dibuka | `program-ai-education` (AI dalam pendidikan tinggi Indonesia); `program-responsible-ai` (fairness, privasi, explainability, amanah epistemik, AI literacy) |
| Target output | KPI *intermediate* GOV-03: Research Pack, kelanjutan ke TA, riset mahasiswa–dosen bersama; manuscript pertama masuk pipeline [publications](../../publications/README.md) |
| Milestone institusional | mata kuliah bermode R terdokumentasi di [research-based-learning](../../research-based-learning/README.md); Faculty Portfolio di Mission Control terisi; skema penelitian internal dengan ≥2 mahasiswa dimanfaatkan (verifikasi ke LPPM) |
| Bukti yang dicari | apakah research asset mata kuliah benar-benar dipakai riset berikutnya (*research assets should compound*) |

### 2028 — AI Center Launch & cross-faculty

**Fokus riset.** Pusat riset menjadi *matching engine* antara demand (industri, pemerintah, UAI, masyarakat) dan supply (dosen, mahasiswa, mata kuliah, dataset) sebagaimana [AIR-05](../../research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md). Kolaborasi lintas fakultas memakai model **Domain Problem + Data + AI Capability + Evaluation + Impact** ([AIR-04](../../research-os/03-ai-research-ecosystem/04-cross-faculty-ai-model.md)).

| Aspek | Isi |
|---|---|
| Sel matriks aktif | C4 × Health, C4 × Food, C2 × Halal/Government (sistem, keamanan, traceability); C1 × Health (NLP teks kesehatan berbahasa Indonesia) |
| Program dibuka | `program-ai-halal`; `program-ai-health` — keduanya wajib memiliki mitra lintas fakultas/partner dan protokol data sensitif yang lolos review ([SECURITY.md](../../SECURITY.md)) |
| Target output | KPI *lagging* GOV-03 mulai terisi: submission, acceptance, HKI pertama, proposal hibah berbasis Research Pack |
| Milestone institusional | peluncuran resmi AI Research Center; kerja sama pertama dengan fakultas lain dan partner; **mid-term review roadmap** (lanjut/ubah/hentikan sel matriks) |
| Bukti yang dicari | apakah masalah dari luar prodi bisa masuk pipeline yang sama tanpa menurunkan kualitas gate |

### 2029 — Public Portal & scaling

**Fokus riset.** Program yang matang mulai merilis artefak yang dapat dipakai pihak lain: dataset berlisensi jelas, benchmark evaluasi berbahasa Indonesia, model kecil terdokumentasi. Reproducibility menjadi pembeda ([alignment/global.md](../alignment/global.md)).

| Aspek | Isi |
|---|---|
| Sel matriks aktif | C1 × semua domain yang punya korpus (benchmark Indonesia); C2 × Business (MLOps berbiaya rendah); C4 × Government/Social Impact |
| Program dibuka | `program-indonesian-llm` — evaluasi dan adaptasi model bahasa untuk konteks Indonesia/domain UAI, bukan pelatihan foundation model dari nol (lihat [C1](../clusters/ai-models-data-knowledge.md)) |
| Target output | rilis `DS-*` dan `ART-*` publik pertama; publikasi dengan artefak yang dapat direproduksi; KPI lagging GOV-03 |
| Milestone institusional | GitHub Phase 5 (Public Research Portal) / GOV-02 Phase 5 (Scale cross-faculty): portal publik, dashboard otomatis, README organisasi sebagai dashboard; kebijakan compute dan penyimpanan data institusional |
| Bukti yang dicari | apakah artefak UAI dipakai/dikutip pihak luar |

### 2030 — Evaluasi & agenda berikutnya

**Fokus riset.** Tidak ada sel baru. Tahun konsolidasi: replikasi hasil internal, studi dampak program, meta-analisis Research Pack lima angkatan, dan penyusunan roadmap 2031–2035.

| Aspek | Isi |
|---|---|
| Sel matriks aktif | sel yang terbukti hidup; sel yang tidak menghasilkan riset lolos G5 dalam tiga semester dibekukan |
| Program | evaluasi lanjut/ubah/hentikan untuk lima program; tidak ada program baru |
| Target output | laporan dampak lima tahun; seluruh KPI GOV-03 dirangkum sebagai evidence institusional ([GOV-05](../../research-os/07-governance/05-ppts-and-institutional-evidence.md)) |
| Milestone institusional | end-of-horizon review; roadmap baru; evidence untuk siklus akreditasi berikutnya (SK LAM-INFOKOM 2025 berlaku sampai Maret 2030 — sumber: dokumen diskusi; verifikasi sebelum dokumen formal) |
| Bukti yang dicari | apakah compounding loop benar-benar terjadi: apakah mahasiswa angkatan 2030 memulai riset dari posisi lebih baik daripada angkatan 2026 |

## 3. Kapan sebuah program dibuka

Repo `program-<nama>` berisi `README.md`, `roadmap.md`, `problems.md`, `datasets.md`, `projects.md`, `publications.md`, `partners.md` (dokumen sumber). Ia dibuka hanya bila **semua** syarat berikut terpenuhi:

| Syarat | Bukti |
|---|---|
| ≥2 riset `proj-*` pada sel/baris matriks yang sama telah lolos G5 | label `gate:G5-method` di Issue; release `v0.3` |
| Satu dosen `@research-leads` bersedia menjadi penanggung jawab program | tercantum di Faculty Portfolio |
| Sumber masalah/data berkelanjutan | partner, unit UAI, atau dataset publik yang terdaftar di registry |
| Tata kelola data sesuai sensitivitas domain | kartu dataset dengan field Privacy terisi; untuk Health/Halal partner: perjanjian tertulis |
| Disetujui `@directors` pada roadmap review | entri CHANGELOG |

## 4. Asumsi dan risiko ringkas

| Asumsi | Jika tidak terpenuhi | Mitigasi (rujuk [GOV-04](../../research-os/07-governance/04-risk-register.md)) |
|---|---|---|
| Angkatan pilot Metopen 2026 berjalan dengan dosen reviewer yang cukup | 2027 tidak punya Research Pack untuk dilanjutkan | batasi jumlah tim pilot; peer review terstruktur mengurangi beban dosen |
| Data kampus (akademik, dokumen) dapat diakses dengan anonimisasi dan izin | sel C3/C1 × Education tertunda | mulai dari dokumen publik kampus dan data sintetis/agregat; kartu dataset Restricted |
| Ada dosen yang bersedia memimpin program 2027 | program dibuka terlambat | pemetaan dosen ([AIR-03](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md)) sejak 2026; program dapat dipimpin bersama |
| Mitra lintas fakultas/partner tersedia untuk Halal dan Health pada 2028 | program 2028 mundur ke 2029 | pakai data publik dan masalah internal dulu; jangan buka program tanpa mitra |
| Compute dan penyimpanan tersedia untuk 2029 | `program-indonesian-llm` hanya evaluasi, bukan adaptasi model | desain riset yang tidak bergantung GPU besar (evaluasi, data-centric, model kecil) |
| Kualitas riset konsisten saat skala membesar | *publication gaming*, jurnal predator | Research Integrity Gate; venue registry [TPL-06](../../research-os/08-templates/06-publication-venue-registry-template.md) |

## 5. Cara memperbarui dokumen ini

Tabel §1 diperbarui pada roadmap review tahunan; bagian tahun berjalan boleh ditambah subbagian "Realisasi" berisi jumlah riset per sel dan gate tertinggi (dari Mission Control). Jangan mengubah target angka di sini — ubah di GOV-03 dan rujuk.
