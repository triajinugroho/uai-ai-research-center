# Research Roadmap — What Should We Research? (2026–2030)

> **Status** Draft v0.1 (2026-09) · **Terkait** [MST-03 Glossary](../research-os/00-master/03-glossary.md) · [AIR-01 AI Research Center Concept](../research-os/03-ai-research-ecosystem/01-ai-research-center-concept.md) · [AIR-02 AI Research Clusters](../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [STR-04 Alignment Map](../research-os/01-strategic-foundation/04-alignment-map.md) · [GOV-02 Implementation Roadmap](../research-os/07-governance/02-implementation-roadmap.md) · [Research Backlog](../research-backlog/README.md)

Folder ini adalah **strategic research brain** UAI AI Research Center. Ia menjawab satu pertanyaan: **apa yang seharusnya kita teliti** dalam lima tahun ke depan, dan mengapa. Ia tidak menjelaskan *bagaimana* meneliti (itu tugas `research-os/`) dan tidak menampung *ide riset satu per satu* (itu tugas `research-backlog/`).

## 1. Tiga folder, tiga pertanyaan

| Folder | Pertanyaan | Isi | Horizon | Siapa yang mengubah |
|---|---|---|---|---|
| [`research-os/`](../research-os/README.md) | **How do we research?** | framework, gates, protokol AI, etika, rubrik, template | stabil; direvisi per versi | `@maintainers` via PR |
| `research-roadmap/` (folder ini) | **What should we research?** | klaster, domain, alignment, tahapan 2026–2030 | 5 tahun; review tahunan | `@directors` + `@research-leads` |
| [`research-backlog/`](../research-backlog/README.md) | **What could be researched next?** | problem bank: Issue + indeks `BACKLOG.md` | bergulir; review per semester | siapa saja mengusulkan, `@maintainers` triage |

Hubungan ketiganya: roadmap menetapkan **arah**, backlog menampung **peluang** yang dinilai terhadap arah itu, research-os menjamin **kualitas bukti** ketika peluang dijalankan. Sebuah masalah yang bagus tetapi di luar roadmap tidak otomatis ditolak; ia diberi prioritas lebih rendah atau menjadi masukan untuk review roadmap berikutnya.

## 2. Struktur folder

```
research-roadmap/
├── README.md                      ← halaman ini: cara memakai roadmap, matriks klaster × domain
├── 2026-2030/README.md            ← roadmap lima tahun per tahap
├── clusters/                      ← 4 klaster riset AI (sumbu "kapabilitas")
│   ├── ai-models-data-knowledge.md   C1
│   ├── ai-systems-security.md        C2
│   ├── responsible-human-ai.md       C3
│   └── applied-ai.md                 C4
├── domains/                       ← 7 domain penerapan (sumbu "masalah")
│   ├── education.md · halal.md · health.md · food.md
│   └── government.md · business.md · social-impact.md
└── alignment/                     ← mengapa arah ini: UAI, Indonesia, global
    ├── uai.md · indonesia.md · global.md
```

Dua sumbu itu disengaja. **Klaster** menjawab "kapabilitas AI apa yang kita bangun" (AI Core, AI Enabling, Responsible AI). **Domain** menjawab "masalah siapa yang kita selesaikan" (AI Application). Setiap riset berada di satu sel matriks klaster × domain; riset lintas sel dicatat dengan klaster primer dan sekunder, mengikuti field **Cluster** dan **Domain** di Mission Control ([GOVERNANCE.md](../GOVERNANCE.md)).

## 3. Cara roadmap dipakai

### 3.1 Memilih masalah (mahasiswa, dosen)

1. Baca [2026-2030/README.md](2026-2030/README.md) untuk tahu fokus tahun berjalan.
2. Pilih satu **domain** yang Anda punya akses ke masalah/datanya, lalu satu **klaster** yang sesuai kapabilitas Anda.
3. Cek bagian *problem space* dan *contoh RQ* di file domain; cek bagian *research questions besar* di file klaster.
4. Cek bagian **"topik yang sengaja tidak kita kejar"** di file klaster; kalau ide Anda ada di sana, cari sudut lain.
5. Ajukan lewat Issue **Research Problem** ke [backlog](../research-backlog/README.md). Sebutkan sel matriks (mis. `C3 × Education`).

### 3.2 Menilai backlog (triage `@maintainers`, `@research-leads`)

Kriteria **fit roadmap** pada triage backlog dinilai dari tiga hal: (a) masuk salah satu sel matriks, (b) sejalan dengan fokus tahun berjalan atau tahun berikutnya, (c) tidak masuk daftar "sengaja tidak dikejar". Fit tinggi menaikkan prioritas (`P1-high`); fit rendah bukan alasan menolak, melainkan alasan menunda (`P3-low`) atau meminta reframing.

### 3.3 Menentukan program (`@directors`)

Repo `program-<nama>` (5–10 tahun) dibuka **hanya** ketika satu sel/baris matriks sudah memiliki: minimal 2 riset `proj-*` yang lolos G5, satu dosen penanggung jawab, dan satu sumber masalah/data yang berkelanjutan (partner, unit UAI, atau dataset publik). Urutan pembukaan program ada di [2026-2030/README.md](2026-2030/README.md).

### 3.4 Menyusun mata kuliah mode R

Dosen pengampu mata kuliah bermode **R — Research-Producing** ([ARC-03](../research-os/02-academic-architecture/03-ai-contribution-modes.md)) memilih tema proyek semester dari sel matriks yang sedang aktif, sehingga research asset mata kuliah langsung dapat dipakai riset berikutnya ([research-based-learning](../research-based-learning/README.md)).

## 4. Matriks 4 klaster × 7 domain (ringkasan)

Setiap sel berisi contoh arah, bukan daftar tertutup. Detail di file klaster dan domain masing-masing.

| Klaster ↓ / Domain → | [Education](domains/education.md) | [Halal](domains/halal.md) | [Health](domains/health.md) | [Food](domains/food.md) | [Government](domains/government.md) | [Business](domains/business.md) | [Social Impact](domains/social-impact.md) |
|---|---|---|---|---|---|---|---|
| **C1** [AI Models, Data & Knowledge](clusters/ai-models-data-knowledge.md) | RAG dokumen akademik & regulasi kampus; korpus materi ajar | knowledge graph komposisi bahan & sertifikasi | NLP teks klinis/edukasi kesehatan berbahasa Indonesia | ekstraksi informasi label pangan & gizi | RAG regulasi; klasifikasi pengaduan publik | NLP ulasan & percakapan pelanggan UMKM | korpus bahasa daerah; low-resource NLP |
| **C2** [AI Systems, Software & Security](clusters/ai-systems-security.md) | keandalan & MLOps sistem AI kampus | sistem traceability & audit trail | privasi, keandalan sistem skrining | IoT rantai pangan & sensor kualitas | keamanan chatbot layanan publik (prompt injection) | MLOps berbiaya rendah untuk UMKM | sistem informasi bencana low-resource |
| **C3** [Human-Centered & Responsible AI](clusters/responsible-human-ai.md) | AI literacy; academic advising; asesmen yang jujur | kepercayaan konsumen pada verifikasi berbasis AI | explainability untuk tenaga kesehatan | nudging konsumsi yang etis | fairness & transparansi keputusan otomatis | keputusan pelaku usaha berbantuan AI | inklusi, aksesibilitas, disabilitas |
| **C4** [Applied AI for Human Flourishing](clusters/applied-ai.md) | early warning kesulitan belajar | klasifikasi citra produk/label halal | skrining dini & prediksi risiko | prediksi kualitas & susut pangan | analisis kebijakan & pengaduan | prediksi permintaan & kredit mikro | filantropi (zakat/wakaf), komunitas, lingkungan |

Warna prioritas 2026–2027 (lihat roadmap): sel **C3 × Education**, **C1 × Education/Government**, **C4 × Halal** dibuka lebih dulu karena masalah dan datanya paling dekat dengan kampus.

## 5. Ritme review tahunan

| Kapan | Apa | Siapa | Output |
|---|---|---|---|
| Setiap Juli–Agustus (sebelum semester ganjil) | **Roadmap review**: apa yang berubah di UAI, Indonesia, global; sel mana yang hidup/mati; program apa yang siap dibuka | `@directors` memimpin; `@research-leads` per klaster mengusulkan; masukan dari `@faculty` dan backlog | PR ke folder ini + entri di [CHANGELOG.md](../CHANGELOG.md) |
| Setiap akhir semester | **Portfolio check**: jumlah riset per sel matriks (dari Mission Control view *By Research Cluster*), gate tertinggi yang dicapai | `@research-leads` | tabel ringkas di [2026-2030/README.md](2026-2030/README.md) |
| 2028 (tengah horizon) | **Mid-term review**: apakah program unggulan layak dilanjutkan | `@directors`, Kaprodi, pimpinan fakultas | keputusan lanjut/ubah/hentikan program |
| 2030 | **End-of-horizon review** → roadmap 2031–2035 | `@directors` | dokumen roadmap baru |

Prinsip review: **evidence before claim** juga berlaku untuk roadmap. Sel matriks yang tiga semester berturut-turut tidak menghasilkan riset yang lolos G5 dipertimbangkan untuk dibekukan.

## 6. Hubungan ke Renstra Penelitian UAI dan prioritas nasional

Dokumen sumber menyebut bahwa UAI mengarahkan topik penelitian agar terkait dengan **Renstra Penelitian universitas**, dan bahwa skema penelitian internal 2026 mendorong keterlibatan mahasiswa (minimal dua mahasiswa aktif pada call yang ditemukan). Roadmap ini dirancang agar setiap sel matriks dapat dipetakan ke tema Renstra tersebut; pemetaannya ada di [alignment/uai.md](alignment/uai.md).

> **Catatan verifikasi.** Rujukan Renstra Penelitian UAI periode berjalan: `[isi: nomor dokumen, periode, tema prioritas]`. Sebelum roadmap ini dipakai dalam dokumen formal, tim harus memverifikasi tema Renstra dan skema penelitian internal terkini langsung ke LPPM/unit penelitian UAI. Sumber: dokumen diskusi; verifikasi sebelum dokumen formal.

Prioritas nasional (transformasi digital, talenta digital, bahasa Indonesia dan daerah, halal, kesehatan, pendidikan, layanan publik, UMKM) dipetakan secara generik di [alignment/indonesia.md](alignment/indonesia.md); arah global (responsible AI, reproducibility, CS2023, open science) di [alignment/global.md](alignment/global.md). Roadmap tidak mengutip nomor regulasi tertentu; pemetaan ke dokumen kebijakan resmi dilakukan saat roadmap review.

## 7. Apa yang bukan tugas roadmap

- Roadmap **bukan** daftar judul TA. Judul lahir dari backlog dan Metopen, bukan dari sini.
- Roadmap **bukan** janji publikasi. Target output ada di [GOV-03 KPI](../research-os/07-governance/03-kpi-and-measurement.md).
- Roadmap **bukan** peta dosen. Pemetaan dosen ↔ klaster ada di [AIR-03](../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md) dan [TPL-07](../research-os/08-templates/07-faculty-research-map-template.md).
- Roadmap **tidak** menyimpan data. Dataset dicatat di [datasets-registry](../datasets-registry/README.md).

Prinsip Occam berlaku: lebih baik empat sel matriks yang hidup daripada dua puluh delapan sel yang hanya tertulis.
