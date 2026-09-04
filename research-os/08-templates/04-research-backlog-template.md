# Research Backlog Template

> **ID** TPL-04 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Dosen (problem owner, mentor), admin riset, `@maintainers`, mahasiswa yang mencari masalah riset, partner
> **Terkait** [research-backlog/README.md](../../research-backlog/README.md) · [BACKLOG.md](../../research-backlog/BACKLOG.md) · [CONTRIBUTING.md §2](../../CONTRIBUTING.md) · [AIR-05 Demand–Supply Marketplace](../03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) · [AIR-02 Clusters](../03-ai-research-ecosystem/02-ai-research-clusters.md) · [TPL-07 Faculty Research Map](07-faculty-research-map-template.md)

## Cara pakai

Backlog adalah **problem bank** Prodi/AI Center: daftar peluang riset yang layak dikerjakan berikutnya, bukan kumpulan paper. Setiap masalah masuk lewat Issue **Research Problem** (form di `.github/ISSUE_TEMPLATE/`), ditriase oleh `@faculty`/`@maintainers`, lalu dicatat sebagai satu entri di `research-backlog/problems/` dan satu baris di indeks `research-backlog/BACKLOG.md`. Mahasiswa memilih masalah dari sini pada W1 (G1 Endgame Ready); masalah mendapat Research ID resmi ketika tim yang mengambilnya lolos G2 Problem Ready. Dosen mengisi backlog dari riset sendiri, mata kuliah mode R, partner, atau roadmap; partner mengisi lewat Issue yang sama. Entri diperbarui saat status berubah dan ditinjau tiap awal semester.

## Format entri (salin ke `research-backlog/problems/<slug>.md`)

```markdown
# [Judul masalah — kalimat masalah, bukan nama solusi]

| Field | Isi |
|---|---|
| Research ID | [— sebelum G2 / UIAI-YYYY-NNN setelah G2] |
| Issue | #[n] |
| Cluster | [C1 / C2 / C3 / C4] |
| Domain | [Education / Halal / Health / Food / Government / Business / Social Impact] |
| Problem owner | [nama/unit yang punya masalah dan akan memakai hasilnya] |
| Potential dataset | [nama + Dataset ID bila terdaftar / "perlu dikumpulkan" / "belum ada"] |
| Research maturity | [Idea / TA Ready / Research Ready / Publication Ready / Impact Ready] |
| Related courses | [AI/ML, Data Mining, NLP, RPL, Metopen, TA, …] |
| Potential output | [TA / paper / dataset / benchmark / software / model / HKI / prototype / research brief] |
| Priority | [P0 / P1 / P2 / P3] |
| Source / entry door | [Problem / Dataset / Faculty Research / Course Project / Partner / Competition] — [asal konkret] |
| Status backlog | [Idea / Claimed / Active / Done / Archived] |
| Notes | [batasan, risiko, kontak, tautan] |

## Masalah (3–5 kalimat)
[fenomena nyata, siapa yang terdampak, mengapa penting sekarang; problem-first, bukan solution-first]

## Pertanyaan awal yang mungkin
- [RQ kandidat 1] · [RQ kandidat 2]

## Bukti awal
- [sumber terverifikasi 1] · [sumber 2]
```

## Tabel indeks (`research-backlog/BACKLOG.md`)

```markdown
| Research ID | Judul | Cluster | Domain | Problem owner | Dataset | Maturity | Courses | Output | Priority | Entry door | Status | Issue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [—/UIAI-YYYY-NNN] | [judul] | [C] | [domain] | [owner] | [DS-… / —] | [maturity] | [courses] | [output] | [P] | [door] | [status] | #[n] |
```

Urutan baris: Priority (P0 dulu), lalu Maturity, lalu tanggal Issue. Baris `Archived` dipindah ke bagian bawah.

## Alur: Issue → backlog → Research ID

```
Issue "Research Problem" (siapa pun)        label: type:problem, maturity:idea
        │  triase ≤ 1 minggu oleh @faculty/@maintainers
        ▼
Masuk backlog   → entri problems/<slug>.md + baris BACKLOG.md   status: Idea
        │  tim mahasiswa/dosen mengambil (assign di Issue)        status: Claimed
        ▼
G1 Endgame Ready → repo proj-YYYY-topic dibuat                   label: gate:G1-endgame
        │
        ▼
G2 Problem Ready lulus → @maintainers memberi UIAI-YYYY-NNN       status: Active
   • judul Issue diubah `[UIAI-YYYY-NNN] Judul`
   • kolom Research ID di BACKLOG.md dan entri diisi
   • baris ditambahkan ke Mission Tracker (TPL-02)
        │
        ▼
G8 / Published → status: Done (tautan ke Research Pack / PUB / DS / ART)
```

Definisi prioritas: **P0** memblokir riset lain atau ada tenggat partner/hibah; **P1** selaras roadmap dan ada data + owner; **P2** menarik, data/owner belum pasti; **P3** ide jangka panjang. Nomor Research ID berurutan per tahun dan tidak pernah dipakai ulang, termasuk untuk masalah yang dibatalkan.

## Contoh terisi

| Field | Isi |
|---|---|
| Research ID | UIAI-2026-001 |
| Issue | #[n] |
| Cluster | C3 Human-Centered & Responsible AI |
| Domain | Education |
| Problem owner | Kaprodi Informatika / koordinator dosen wali [isi] |
| Potential dataset | Dokumen kurikulum (public); transkrip anonim (UAI, restricted) — DS-2026-001 |
| Research maturity | TA Ready (per 2026-10, lolos G5) |
| Related courses | AI/ML, NLP, Metopen, TA |
| Potential output | TA, paper konferensi nasional, dataset kasus advising, prototype |
| Priority | P1 |
| Source / entry door | Problem — keluhan dosen wali tentang beban konsultasi dan pelanggaran prasyarat |
| Status backlog | Active |
| Notes | Butuh consent mahasiswa dan anonimisasi sebelum data dipakai; mentor [Dosen C3]; hasil pilot dapat menjadi masalah lanjutan untuk angkatan berikutnya |

Masalah: Dosen wali menangani puluhan mahasiswa dengan waktu konsultasi terbatas; mahasiswa memilih mata kuliah dengan informasi tidak lengkap sehingga terjadi pelanggaran prasyarat dan keterlambatan lulus. Asisten advising berbasis LLM menjanjikan bantuan, tetapi belum ada bukti terkontrol pada kurikulum Indonesia. Pertanyaan awal: apakah asisten LLM+RAG menghasilkan rencana studi yang valid dan berguna dibanding aturan sederhana? Bukti awal: [sumber terverifikasi 1], [sumber 2].

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Rumusan | Kalimat masalah dengan pemilik dan dampak | "Implementasi CNN untuk X" |
| Problem owner | Orang/unit nyata yang akan memakai hasil | "Masyarakat umum" |
| Dataset | Disebut sumber, akses, privasi, atau jujur "belum ada" | "Dataset dari Kaggle" tanpa nama |
| Prioritas | Mengikuti definisi P0–P3 | Semua P1 |
| Status | Berubah mengikuti kejadian di Issue/PR | Entri tidak pernah diperbarui setelah dibuat |
| Kelengkapan indeks | Setiap entri punya baris di BACKLOG.md dan Issue | Entri di Drive tanpa Issue |
