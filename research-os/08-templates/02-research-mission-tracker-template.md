# Research Mission Tracker Template

> **ID** TPL-02 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Admin riset, dosen pengampu Metopen, ketua klaster, Kaprodi; mahasiswa (membaca baris timnya sendiri)
> **Terkait** [GOVERNANCE.md §9 Mission Control](../../GOVERNANCE.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [OPS-02 Weekly Sprints](../06-execution-os/02-weekly-sprints.md) · [GOV-03 KPI](../07-governance/03-kpi-and-measurement.md) · [TPL-03 Leaderboard](03-research-leaderboard-template.md) · [TPL-01 One-Pager](01-research-one-pager-template.md)

## Cara pakai

Tracker ini melacak **semua tim** dalam satu tabel: satu baris per Research ID, dari Idea sampai Published/Released. Sumber kebenarannya adalah GitHub Projects **UAI AI Research Mission Control** (Organization Project); Google Sheet hanya cermin untuk pihak yang tidak memakai GitHub, dengan kolom yang persis sama. Diperbarui oleh admin riset atau dosen pengampu setiap akhir sprint (Jumat) setelah PR `GATE REVIEW` di-merge, dan oleh tim saat mengubah **Next Evidence**. Field **Research Gate**, **Maturity**, dan **Status** dipakai oleh semua gate G1–G8, oleh leaderboard ([TPL-03](03-research-leaderboard-template.md)), dan oleh KPI leading ([GOV-03](../07-governance/03-kpi-and-measurement.md)). Jangan membuat tracker kedua: satu Research ID, satu baris, satu tempat.

## Nilai yang diizinkan

| Field | Nilai |
|---|---|
| Cluster | C1 / C2 / C3 / C4 |
| Domain | Education / Halal / Health / Food / Government / Business / Social Impact |
| Entry Door | Problem / Dataset / Faculty Research / Course Project / Partner / Competition |
| Course | AI/ML / Data Mining / NLP / RPL / Metopen / TA / — |
| Research Gate | G1 / G2 / G3 / G4 / G5 / G6 / G7 / G8 (gate yang **sedang dikerjakan**; gate terakhir yang lulus ada di kolom tanggal) |
| Maturity | Idea / TA Ready / Research Ready / Publication Ready / Impact Ready |
| Priority | P0 / P1 / P2 / P3 (sesuai label `P0-critical` … `P3-low`) |
| Status | Active / Blocked / Review / Done |
| Sprint | S0 … S16 (opsional, field Iteration) |

## Template tabel (salin ke Sheet atau ekspor CSV)

```markdown
| Research ID | Title | Cluster | Domain | Researcher | Faculty Mentor | Entry Door | Course | Research Gate | Maturity | Priority | Publication Target | Due | Status | Next Evidence | Repo / Issue | Sprint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [UIAI-YYYY-NNN] | [judul] | [C1–C4] | [domain] | [nama] | [nama] | [entry door] | [course] | [G1–G8] | [maturity] | [P0–P3] | [venue / —] | [YYYY-MM-DD] | [status] | [bukti berikutnya] | [link] | [S0–S16] |
```

Kolom tambahan **tanggal lolos gate** (satu kolom per gate; isi tanggal merge PR, kosong bila belum):

```markdown
| Research ID | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | Release terakhir | PR gate terakhir |
|---|---|---|---|---|---|---|---|---|---|---|
| [UIAI-YYYY-NNN] | [YYYY-MM-DD] | | | | | | | | [v0.x] | [#n] |
```

## Petunjuk GitHub Projects

1. **Buat** Organization Project → nama `UAI AI Research Mission Control`, layout Table. Item = Issue `type:problem` (satu per Research ID), Issue `type:publication`, dan Draft Item untuk task tanpa Issue.
2. **Custom fields**: `Research ID` (Text), `Cluster`/`Domain`/`Entry Door`/`Course`/`Research Gate`/`Maturity`/`Priority`/`Status` (Single select dengan nilai di tabel di atas), `Faculty Mentor` dan `Researcher` (Text), `Publication Target` (Text), `Due` (Date), `Next Evidence` (Text), `Sprint` (Iteration, 1 minggu, mulai S0), `G1`…`G8 passed` (Date).
3. **Views** (sesuai [GOVERNANCE.md §9](../../GOVERNANCE.md)):

| View | Layout | Group / kolom | Filter | Pemakai utama |
|---|---|---|---|---|
| 1 Research Pipeline | Board | kolom = Idea → Problem Ready → … → Contribution Ready → Published/Released (dari `Research Gate` + `Maturity`) | semua item riset | semua; inilah leaderboard substantif |
| 2 By Research Cluster | Board | group by `Cluster` | `Status != Done` | ketua klaster |
| 3 By Course | Table | group by `Course` | `Course` is AI/ML, Data Mining, Metopen, TA | dosen pengampu |
| 4 Publication Pipeline | Board | kolom = Research → Writing → Internal Review → Submission Ready → Submitted → Revision → Accepted → Published | `type:publication` | pengelola publications |
| 5 Faculty Portfolio | Table | group by `Faculty Mentor`, sort `Research Gate` | semua | dosen (BKD, hibah), Kaprodi (akreditasi) |

4. **Sinkronisasi label**: setiap perubahan `Research Gate` harus diikuti label `gate:Gn-*` pada Issue dan bagian *Current Research Gate* di README riset. Otomasi menyusul setelah alur manual stabil.
5. **Ekspor**: Projects → `...` → Export CSV setiap akhir bulan; simpan ke Sheet cermin untuk laporan Prodi.

## Petunjuk Google Sheet (cermin)

- Tab `Tracker`: kolom persis seperti template; baris = Research ID. Data validation untuk kolom Single select memakai tab `Lookup`.
- Tab `Gate Log`: `Research ID | Gate | Tanggal lolos | PR | Reviewer | Catatan` — satu baris per kejadian lolos gate; kolom G1–G8 di `Tracker` diisi dari sini.
- Tab `Lookup`: daftar nilai yang diizinkan (salin tabel di atas).
- Aturan: Sheet **tidak** diedit langsung untuk perubahan status; ubah di GitHub Projects, lalu cerminkan. Bila GitHub belum dipakai suatu angkatan, Sheet boleh menjadi sumber sementara, tetapi kolomnya tetap sama agar migrasi tanpa penulisan ulang.

## Contoh terisi

| Research ID | Title | Cluster | Domain | Researcher | Faculty Mentor | Entry Door | Course | Research Gate | Maturity | Priority | Publication Target | Due | Status | Next Evidence | Repo / Issue | Sprint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UIAI-2026-001 | AI-assisted academic advising for Indonesian universities | C3 | Education | [Mahasiswa A], [Mahasiswa B] | [Dosen C3] | Problem | Metopen | G5 | TA Ready (target Research Ready) | P1 | [konferensi nasional AI in education — isi] | 2026-10-[dd] | Review | Experiment Card pilot 40 kasus + notulen red team W8 | proj-2026-ai-academic-advising · #[n] | S8 |

| Research ID | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | Release terakhir | PR gate terakhir |
|---|---|---|---|---|---|---|---|---|---|---|
| UIAI-2026-001 | 2026-09-[dd] | 2026-09-[dd] | 2026-10-[dd] | 2026-10-[dd] | | | | | v0.2 Evidence Ready | #[n] GATE REVIEW: Question Ready |

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Kelengkapan | Setiap baris punya Research Gate, Status, Next Evidence yang konkret dan bertanggal | Next Evidence berisi "lanjut riset" |
| Kesegaran | Diperbarui tiap akhir sprint; tanggal gate = tanggal merge PR | Status berubah tanpa PR; tanggal diisi dari ingatan |
| Satu sumber | GitHub Projects = sumber; Sheet = cermin | Tiga versi tracker berbeda di Drive, WhatsApp, GitHub |
| Nilai terkontrol | Semua kolom memakai nilai yang diizinkan (dropdown) | "Hampir G5", "high-ish" |
| Privasi | Tidak ada data mahasiswa selain nama/akun GitHub; tidak ada nilai akademik | Kolom IPK, nomor telepon |
