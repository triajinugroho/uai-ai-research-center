# Research Backlog — What Could Be Researched Next?

> **Status** Draft v0.1 (2026-09) · **Terkait** [MST-03 Glossary](../research-os/00-master/03-glossary.md) · [OPS-03 Research Gates](../research-os/06-execution-os/03-research-gates.md) · [TPL-04 Research Backlog Template](../research-os/08-templates/04-research-backlog-template.md) · [Research Roadmap](../research-roadmap/README.md) · [GOVERNANCE.md](../GOVERNANCE.md) · [CONTRIBUTING.md](../CONTRIBUTING.md)

Backlog adalah **problem bank** Prodi Informatika dan AI Research Center: kumpulan **peluang riset di masa depan**, bukan kumpulan paper, bukan daftar judul TA, dan bukan arsip riset yang sudah selesai. Setiap entri adalah masalah nyata yang layak diteliti tetapi belum (tentu) ada yang mengerjakannya. Sumber utamanya adalah **GitHub Issues** bertipe *Research Problem*; folder ini menyimpan indeks ([BACKLOG.md](BACKLOG.md)) dan kartu masalah ([problems/](problems/)).

Tiga folder, tiga pertanyaan: [research-os](../research-os/README.md) = *how do we research?*, [research-roadmap](../research-roadmap/README.md) = *what should we research?*, backlog = *what could be researched next?*

## 1. Alur: dari ide menjadi riset

```
Issue "Research Problem"  ──►  Triage @maintainers  ──►  Validasi G2 (tingkat masalah)
(form di .github)               (label, klaster, domain)     (nyata? penting? siapa peduli?)
        │                                                             │
        ▼                                                             ▼
Research ID UIAI-YYYY-NNN  ──►  Entri BACKLOG.md + problems/UIAI-YYYY-NNN-slug.md
(resmi saat PR G2 di-merge; sebelumnya UIAI-YYYY-TBD)
        │
        ▼
Tim terbentuk (Metopen / TA / riset dosen)  ──►  repo proj-YYYY-topic  ──►  G1…G8
```

| Langkah | Siapa | Apa yang terjadi | Bukti |
|---|---|---|---|
| 1. Usul | mahasiswa, dosen, partner | Buka Issue dengan form **Research Problem** (`.github/ISSUE_TEMPLATE/`): judul, cluster, domain, problem owner, potential dataset, maturity, related courses, potential output, priority | Issue berlabel `type:problem`, `maturity:idea` |
| 2. Triage | `@maintainers` (+ `@research-leads` klaster) | Cek kelengkapan, tetapkan `cluster:*`, prioritas `P0–P3`, tandai fit roadmap; minta klarifikasi bila perlu | komentar triage di Issue |
| 3. Validasi G2 tingkat masalah | `@maintainers` + 1 dosen klaster | Masalah nyata, penting, ada pemangku kepentingan; *problem-first* bukan *solution-first*; tidak masuk daftar "sengaja tidak dikejar" roadmap | PR **GATE REVIEW: Problem Ready** (G2) di-merge — PR gate dari repo tim ([OPS-021/OPS-022](../research-os/06-execution-os/01-research-wbs-master.md)) atau, untuk masalah yang belum punya tim, PR kartu masalah ke folder ini |
| 4. Research ID | `@maintainers` | Tetapkan ID resmi `UIAI-YYYY-NNN` saat PR G2 di-merge — berurutan per tahun, tidak pernah dipakai ulang; setelah merge, ganti `UIAI-YYYY-TBD` pada judul Issue (dan README riset bila repo sudah ada) menjadi `[UIAI-YYYY-NNN]` | judul Issue, counter di BACKLOG.md |
| 5. Indeks | pengusul/`@maintainers` | Tambah baris di [BACKLOG.md](BACKLOG.md) dan buat `problems/UIAI-YYYY-NNN-slug.md` dari [TPL-04](../research-os/08-templates/04-research-backlog-template.md) via PR | PR merged |
| 6. Eksekusi | tim riset + mentor | Saat ada tim: buat repo `proj-YYYY-topic` dari [TPL-15](../research-os/08-templates/15-research-repository-template.md); Issue menjadi item Mission Control; gate G1–G8 berjalan | label `gate:*`, release |

Sebelum langkah 4, Issue memakai ID sementara `UIAI-YYYY-TBD` ([CONTRIBUTING.md](../CONTRIBUTING.md)). Masalah yang **tidak lolos** validasi tidak dihapus: Issue ditutup dengan alasan (*not planned*) dan dapat dibuka lagi bila ada bukti baru.

## 2. Siapa boleh mengusulkan

| Pengusul | Jalur | Catatan |
|---|---|---|
| **Mahasiswa** | Issue Research Problem; biasanya dari Kerja Praktik, proyek mata kuliah, pengalaman pribadi | Wajib menyebut siapa yang peduli pada masalah ini selain dirinya |
| **Dosen** | Issue Research Problem dengan entry door `Faculty Research`; dapat menandai sub-masalah untuk 2–3 mahasiswa | Terhubung ke skema penelitian internal ([alignment/uai.md](../research-roadmap/alignment/uai.md)) |
| **Partner** (industri, pemerintah, masyarakat) | Issue Research Problem atau lewat pusat riset; entry door `Partner` | Data partner tidak pernah mentah di GitHub ([SECURITY.md](../SECURITY.md)) |
| **AI Center / `@research-leads`** | dari roadmap review, prioritas nasional, hasil riset sebelumnya (*new research backlog*) | Menutup compounding loop |

## 3. Kriteria triage

| Kriteria | Pertanyaan | Nilai |
|---|---|---|
| **Cluster** | Masuk C1/C2/C3/C4 mana (primer, sekunder)? | label `cluster:*` |
| **Domain** | Education / Halal / Health / Food / Government / Business / Social Impact? | field Domain |
| **Data availability** | Ada data? Publik/UAI/partner? Sudah ada kartu di [datasets-registry](../datasets-registry/README.md)? | Ada / Mungkin / Belum |
| **Mentor availability** | Ada dosen yang kepakarannya berdekatan dan bersedia? ([AIR-03](../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md)) | Ada / Kandidat / Belum |
| **Fit roadmap** | Masuk sel matriks aktif tahun ini/berikutnya? ([research-roadmap](../research-roadmap/README.md)) | Tinggi / Sedang / Rendah |
| **Sensitivitas** | Data pribadi/kesehatan/partner? Perlu etik? | Public / Restricted / Confidential |
| **Kelayakan waktu** | Bisa menghasilkan pilot dalam satu semester Metopen + TA? | Ya / Perlu dipecah / Tidak |
| **Problem-first** | Sudah jelas *mengapa* sebelum *pakai algoritma apa*? | Ya / Perlu reframing |

Prioritas: `P0-critical` (memblokir riset lain / permintaan institusi mendesak), `P1-high` (fit roadmap tinggi + data + mentor ada), `P2-medium` (satu dari tiga belum ada), `P3-low` (fit rendah atau data belum ada).

## 4. Label yang dipakai

Sumber tunggal: [`.github/labels.yml`](../.github/labels.yml).

| Kelompok | Label pada Issue backlog |
|---|---|
| Type | `type:problem` (wajib); `type:dataset`, `type:literature-gap` bila Issue turunan dibuat |
| Cluster | `cluster:models` · `cluster:systems` · `cluster:human-ai` · `cluster:applied` |
| Priority | `P0-critical` · `P1-high` · `P2-medium` · `P3-low` |
| Maturity | `maturity:idea` saat masuk; diperbarui mengikuti gate: `maturity:ta-ready` (G5), `maturity:research-ready` (G6–G7), `maturity:publication-ready` (G8+), `maturity:impact-ready` |
| Status | `status:ready` (siap diambil tim) · `status:blocked` (menunggu data/izin/mentor) · `status:review` |
| Gate | `gate:G1-endgame` … `gate:G8-contribution` setelah ada tim |

Domain dan entry door tidak menjadi label; keduanya field di Mission Control dan kolom di BACKLOG.md (topics repo dipakai untuk domain).

## 5. Ritme review backlog

| Kapan | Apa | Siapa |
|---|---|---|
| Setiap minggu (saat semester berjalan) | Triage Issue baru; target ≤7 hari dari Issue dibuka ke komentar triage | `@maintainers` |
| **Awal semester** (sebelum W1 Metopen) | *Backlog grooming*: pastikan ada cukup masalah `status:ready` per klaster untuk tim Metopen; perbarui mentor dan data | `@research-leads`, dosen Metopen |
| **Akhir semester** | Tandai masalah yang diambil tim (link repo), yang selesai (lolos G8), yang mandek; usulkan masalah baru dari hasil riset | `@maintainers`, mentor |
| **Roadmap review tahunan** | Masalah `P3-low` >2 semester tanpa tim dievaluasi: tutup, gabung, atau reframing | `@directors`, `@research-leads` |

## 6. Hubungan ke Mission Control dan leaderboard

- Setiap Issue backlog yang mendapat Research ID menjadi item **UAI AI Research Mission Control** dengan field Research ID, Cluster, Domain, Entry Door, Maturity, Priority, Next Evidence ([GOVERNANCE.md](../GOVERNANCE.md) §9). Kolom **Idea** pada board *Research Pipeline* adalah backlog itu sendiri.
- **Research Leaderboard** ([TPL-03](../research-os/08-templates/03-research-leaderboard-template.md)) menampilkan kemajuan gate per Research ID — mengurutkan **kematangan riset**, bukan orang. Masalah yang belum diambil tim tampil sebagai baris tanpa centang gate.
- Portofolio di [README](../README.md) utama menghitung jumlah *Idea* dari BACKLOG.md.

## 7. Format file `problems/`

Satu file per Research ID: `problems/UIAI-YYYY-NNN-slug.md` (slug kebab-case, English, ≤5 kata). Isi mengikuti [TPL-04](../research-os/08-templates/04-research-backlog-template.md):

| Bagian | Isi |
|---|---|
| Tabel metadata | Research ID, judul, cluster (primer/sekunder), domain, problem owner, potential dataset, research maturity, related courses, potential output, priority, entry door, Issue |
| Problem statement | 3–6 kalimat, *problem-first*, konteks Indonesia/UAI |
| Why it matters / stakeholder | siapa peduli, keputusan apa yang berubah |
| What we know | ringkas; literatur awal diisi saat G3 — jangan mengarang sitasi |
| Candidate RQ | 2–4 RQ awal, boleh direvisi di G4 |
| Possible data & sensitivity | sumber, akses, klasifikasi privasi |
| Candidate mentor | `[isi]` |
| Risks | data, etika, waktu, kompetensi |
| Next evidence | bukti berikutnya yang harus ada agar naik gate |

Contoh: [UIAI-2026-001](problems/UIAI-2026-001-ai-assisted-academic-advising.md), [UIAI-2026-002](problems/UIAI-2026-002-indonesian-rag-evaluation.md), [UIAI-2026-003](problems/UIAI-2026-003-halal-product-image-classification.md) — semuanya **contoh ilustratif** dengan nama orang dan dataset sebagai `[isi]`.

## 8. Yang bukan backlog

- Bukan tempat menyimpan proposal lengkap — itu di repo `proj-*`.
- Bukan daftar keinginan tanpa pemangku kepentingan — masalah tanpa "siapa yang peduli" dikembalikan pada triage.
- Bukan arsip publikasi — itu di [publications](../publications/README.md).
