# Research Leaderboard Template

> **ID** TPL-03 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Admin riset, dosen pengampu Metopen, ketua klaster, mahasiswa, pimpinan (versi publik)
> **Terkait** [TPL-02 Mission Tracker](02-research-mission-tracker-template.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [GOVERNANCE.md §9](../../GOVERNANCE.md) · [MST-03 Glossary §3](../00-master/03-glossary.md) · [GOV-03 KPI](../07-governance/03-kpi-and-measurement.md)

## Cara pakai

Leaderboard menampilkan **kematangan riset** per proyek berdasarkan gate yang telah dilewati, bukan peringkat orang. Diturunkan dari Mission Tracker ([TPL-02](02-research-mission-tracker-template.md)) oleh admin riset atau dosen pengampu setiap akhir sprint (mingguan), lalu dipasang di `research-backlog/BACKLOG.md` (bagian status) atau README organisasi/kelas. Kolom tabel sengaja mengikuti gate G2–G8; G1 Endgame Ready tidak ditampilkan karena menjadi prasyarat masuk tabel. Versi publik hanya memuat Research ID, judul, klaster, dan status gate; versi internal menambah nama tim, blocker, dan catatan reviewer. Dipakai di W8 (Design Defense) dan W16 (Defense) sebagai gambaran kelas, dan oleh [GOV-03](../07-governance/03-kpi-and-measurement.md) untuk KPI leading.

## Legenda status per kolom

| Simbol | Arti | Sumber di GitHub |
|---|---|---|
| ✓ | Gate lulus | PR `GATE REVIEW` di-merge; label `gate:Gn-*` maju |
| Active | Gate sedang dikerjakan pada sprint ini | branch `research/gN-*` ada; PR belum dibuka |
| Review | Menunggu review gate | PR `GATE REVIEW` terbuka; label `status:review` |
| Draft | Artefak gate sudah ada sebagai draft, belum diajukan review (mis. manuscript draft untuk G8) | commit di branch, tanpa PR |
| — | Belum dimulai | tidak ada branch/PR |
| ↺ | Gate ditolak, sedang revisi (hanya di versi internal) | PR ditutup dengan komentar "apa yang kurang & bukti yang dibutuhkan" |

Pemetaan kolom → gate: Problem = G2 · Evidence = G3 · RQ = G4 · Method = G5 · Experiment = G6 · Claim = G7 · Contribution = G8.

## Template — versi publik

```markdown
## Research Leaderboard — [nama kelas / angkatan / klaster] · diperbarui [YYYY-MM-DD] (Sprint [Sn])

| Project | Title | Cluster | Problem | Evidence | RQ | Method | Experiment | Claim | Contribution |
|---|---|---|---|---|---|---|---|---|---|
| [UIAI-YYYY-NNN] | [judul singkat] | [C1–C4] | [✓/Active/Review/Draft/—] | | | | | | |

Ringkasan: [n] proyek · Problem Ready [n] · Evidence Ready [n] · Question Ready [n] · Method Ready [n] · Experiment Ready [n] · Claim Ready [n] · Contribution Ready [n] · Published/Released [n]
```

## Template — versi internal

```markdown
| Project | Tim | Mentor | Problem | Evidence | RQ | Method | Experiment | Claim | Contribution | Blocker | Catatan reviewer terakhir | Next Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [UIAI-YYYY-NNN] | [nama] | [nama] | | | | | | | | [—/deskripsi] | [1 kalimat] | [bukti + tanggal] |
```

## Aturan

1. **Yang diranking adalah kematangan riset, bukan orang.** Tidak ada kolom nilai, IPK, atau "mahasiswa terbaik". Urutan baris: jumlah gate lulus (menurun), lalu Research ID.
2. Status hanya berubah karena **kejadian di GitHub** (PR dibuka/merge/ditutup). Tidak ada "✓ karena sudah dipresentasikan".
3. Gate berurutan: kolom di kanan tidak boleh ✓ jika kolom di kirinya belum ✓, kecuali riset warisan handoff ([TPL-14](14-research-handoff-template.md)) yang mewarisi gate — tandai dengan catatan `inherited`.
4. Gate yang ditolak bukan hukuman: di versi publik tampil sebagai Active; di versi internal ↺ dengan catatan reviewer.
5. Riset yang berhenti dipindahkan ke bagian **Archived** dengan alasan satu baris; nomor Research ID tidak dipakai ulang.
6. Versi publik tidak memuat nama mahasiswa; versi internal hanya untuk dosen pengampu, mentor, dan tim yang bersangkutan.

## Cara update mingguan (±15 menit, akhir sprint)

1. Buka View 1 *Research Pipeline* di Mission Control; catat PR `GATE REVIEW` yang di-merge/dibuka/ditutup minggu ini.
2. Perbarui label `gate:*` dan `status:*` pada Issue yang berubah.
3. Perbarui kolom Research Gate, Status, Next Evidence, dan tanggal gate di tracker ([TPL-02](02-research-mission-tracker-template.md)).
4. Salin ke tabel leaderboard (publik + internal); hitung baris ringkasan.
5. Commit dengan pesan `Update leaderboard Sn (YYYY-MM-DD)`; umumkan di kanal kelas beserta tiga hal: siapa lolos gate, siapa Review, blocker apa yang perlu bantuan dosen.

## Contoh terisi (versi publik)

| Project | Title | Cluster | Problem | Evidence | RQ | Method | Experiment | Claim | Contribution |
|---|---|---|---|---|---|---|---|---|---|
| UIAI-2026-001 | AI-assisted academic advising for Indonesian universities | C3 | ✓ | ✓ | ✓ | Review | — | — | — |
| UIAI-2026-[NNN] | [isi] | [C1] | ✓ | ✓ | Active | — | — | — | — |
| UIAI-2026-[NNN] | [isi] | [C4] | ✓ | Draft | — | — | — | — | — |

Ringkasan: 3 proyek · Problem Ready 3 · Evidence Ready 2 · Question Ready 1 · Method Ready 0 · Experiment Ready 0 · Claim Ready 0 · Contribution Ready 0 · Published/Released 0

Contoh baris internal untuk UIAI-2026-001: Blocker `—` · Catatan reviewer terakhir: "RQ2 perlu definisi operasional 'relevansi elektif' sebelum G5" · Next Evidence: Experiment Card pilot 40 kasus + notulen red team, W8.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Keterlacakan | Setiap ✓ dapat ditelusuri ke PR yang di-merge | Status diisi dari kesan dosen |
| Bahasa | Kolom = gate; status = simbol legenda | Kolom "progress %" tanpa definisi |
| Etos | Leaderboard memicu diskusi "bukti apa yang kurang" | Leaderboard dipakai untuk mempermalukan tim |
| Ritme | Diperbarui setiap sprint dengan tanggal | Terakhir diperbarui dua bulan lalu |
| Pemisahan versi | Publik tanpa nama; internal dengan blocker | Nama dan nilai mahasiswa tampil di README publik |
