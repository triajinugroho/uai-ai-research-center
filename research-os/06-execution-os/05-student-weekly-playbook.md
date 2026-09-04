# Student Weekly Playbook — Satu Halaman per Minggu

> **ID** OPS-05 · **Paket** 06 Execution Operating System · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen (utama), asisten studio, mentor
> **Terkait** [OPS-02 Weekly Sprints](02-weekly-sprints.md) · [OPS-03 Research Gates](03-research-gates.md) · [OPS-04 Dependency & Critical Path](04-dependency-and-critical-path.md) · [OPS-01 Research WBS](01-research-wbs-master.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [TPL-10 AI Usage Log](../08-templates/10-ai-usage-log-template.md)

## Untuk siapa dokumen ini

Untuk Anda, mahasiswa Metopen. Di belakang layar ada 145 microtask, 17 sprint, 8 gate, dan peta ketergantungan. Anda **tidak perlu** membacanya. Yang Anda perlukan hanya **satu halaman per minggu** dengan enam bagian tetap. Backend kompleks, frontend ringan.

Halaman mingguan resmi ada di [`metopen-research-studio/weeks/`](../../metopen-research-studio/weeks/) (`week-01-endgame.md` … `week-16-defense.md`). Dokumen ini menjelaskan formatnya, cara memakainya, dan memberi satu contoh terisi lengkap.

## Format halaman mingguan

Setiap halaman minggu memakai enam bagian ini, dalam urutan ini, tanpa tambahan:

```
# Week NN — <Tema>            (Sprint SNN · mengejar Gate GN)

## This Week
Satu kalimat: outcome minggu ini. Bukan daftar kegiatan.

## Tasks
7–10 baby steps, masing-masing dengan Task ID dari WBS, judul, dan effort.
Tandai [ ] belum, [~] sedang, [x] selesai.

## Deliverable
Apa yang harus ada di repositori pada hari Jumat (file/PR/Issue).

## AI Assist
AI boleh dipakai untuk apa minggu ini — dan untuk apa TIDAK.

## Human Check
Apa yang wajib diverifikasi manusia (Anda, peer, mentor, dosen).

## Done When
Definisi selesai yang bisa dicek ya/tidak.
```

Isi tiap bagian diambil dari kolom WBS: *Tasks* ← `Task ID`, `Task`, `Estimated Effort`; *Deliverable* ← `Output` + `Evidence`; *AI Assist* ← `AI Assistance`; *Human Check* ← `Human Validation`; *Done When* ← *Definition of done* sprint di [OPS-02](02-weekly-sprints.md).

## Cara memakai: 10 menit Senin, 15 menit Jumat

**Senin (awal sesi studio, 10 menit — sprint planning)**

1. Buka halaman minggu ini. Baca *This Week* keras-keras dalam tim.
2. Lihat *Tasks*. Tandai task yang **sudah boleh dimulai** (semua dependency-nya selesai minggu lalu). Biasanya task sesi studio dan 1–2 task produksi.
3. Bagi task antar anggota. Tulis nama di samping task. Satu orang maksimal 2 task berjalan bersamaan.
4. Cek *Deliverable*: file apa yang harus ada Jumat. Buat file kosongnya sekarang bila belum ada.
5. Baca *AI Assist* dan *Human Check* sekali. Ini kontrak minggu ini.

**Selama minggu**

- Kerjakan task; setiap commit menyebut Task ID: `Add search strategy v1 (OPS-026)`.
- Setiap kali memakai AI untuk sesuatu yang memengaruhi pekerjaan, catat di `docs/AI-USAGE.md` **saat itu juga**, bukan Jumat.
- Task selesai hanya jika bukti (Evidence) ada di repositori dan *Human Check*-nya sudah dilakukan.

**Jumat (15 menit — gate check)**

1. Buka *Done When*. Jawab ya/tidak per butir. Jujur.
2. Bila minggu ini minggu gate: pastikan PR `GATE REVIEW: …` sudah dibuka dan reviewer diminta.
3. Tulis jurnal mingguan (`docs/journal/wNN.md`): apa yang dipelajari, apa yang masih ragu, apa yang dibawa ke minggu depan.
4. Task yang belum selesai **dibawa**, bukan dihapus. Tulis di halaman minggu depan bagian *Tasks* paling atas.

## Aturan sprint

| Aturan | Isi | Mengapa |
|---|---|---|
| **WIP limit** | Maksimal 2 task *sedang dikerjakan* per orang; maksimal 4 per tim. | Task riset yang setengah jadi tidak menghasilkan bukti. Selesaikan, baru mulai yang lain. |
| **Definisi done** | Task selesai = Output ada di repo + Evidence dapat dibuka reviewer + Human Check dilakukan + AI Usage Log tercatat. | "Sudah dikerjakan di laptop" bukan selesai. Bukti yang tidak dapat diperiksa sama dengan tidak ada. |
| **Urutan tidak boleh dilompati** | Jangan mengerjakan task minggu depan bila task gate minggu ini belum selesai. RQ tidak sah sebelum evidence synthesis; eksperimen tidak boleh dijalankan sebelum baseline dan metrik terkunci. | Gate berurutan ([OPS-03](03-research-gates.md)). Melompat menghasilkan pekerjaan yang harus diulang. |
| **Metrik dikunci** | Setelah W7, metrik dan baseline tidak diubah setelah melihat hasil. Bila harus berubah, catat alasan dan tanggalnya. | Mengubah metrik setelah melihat hasil adalah pelanggaran amanah epistemik. |
| **AI sebagai copilot** | Ikuti *Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own* ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)). AI tidak pernah menghasilkan referensi, angka hasil, atau keputusan. | Anda yang bertanggung jawab, bukan AI. Referensi hasil AI yang tidak diverifikasi = gate gagal. |
| **Jika terlambat** | Prioritaskan: (1) task critical path, (2) task PR gate, (3) AI Usage Log. Beri tahu dosen di Senin berikutnya, bukan di minggu gate. Lihat skenario pemulihan di [OPS-04](04-dependency-and-critical-path.md#jika-satu-gate-terlambat). | Terlambat satu minggu bisa dipulihkan; terlambat diam-diam tiga minggu tidak. |
| **Jika gagal gate** | Baca komentar reviewer, perbaiki hanya yang diminta, buka review ulang. Gagal gate adalah bagian normal proses. | Reviewer wajib menuliskan apa yang kurang; itu peta perbaikan Anda. |

## Contoh terisi: Week 06 — RQ

Contoh di bawah memakai Task ID nyata dari [OPS-01](01-research-wbs-master.md) sprint S6. Halaman resminya: [`week-06-rq.md`](../../metopen-research-studio/weeks/week-06-rq.md).

```
# Week 06 — RQ                      (Sprint S6 · mengejar Gate G4 Question Ready)

## This Week
Kami memiliki 1–3 RQ yang dapat difalsifikasi, masing-masing ditelusuri ke
baris tertentu di synthesis matrix, dan pernyataan kontribusi yang tidak
melebihi apa yang RQ dapat buktikan.

## Tasks
[ ] OPS-050  Ikuti sesi RQ, Claim & Contribution ............................. 2h    (semua)
[ ] OPS-051  Tulis Research Gap final dengan Gap-Claim-Evidence alignment ..... 2h    (Rani)
[ ] OPS-052  Rumuskan 1-3 RQ dan/atau hipotesis yang dapat difalsifikasi ...... 2h    (semua)
[ ] OPS-053  Tulis Contribution Statement ..................................... 1.5h  (Fajar)
[ ] OPS-054  Uji RQ dengan checklist keterjawaban dan falsifiabilitas ......... 1.5h  (Rani)
[ ] OPS-055  Perbarui Research One-Pager ke v1 ................................ 1h    (Fajar)
[ ] OPS-056  Buka Issue type:research-question ................................ 0.5h  (Fajar)
[ ] OPS-057  Siapkan PR GATE REVIEW: Question Ready ........................... 1h    (Rani)
[ ] OPS-058  Perbarui AI Usage Log dan jurnal mingguan W6 ..................... 0.5h  (semua)
Boleh dimulai Senin: OPS-050, OPS-051 (PR G3 sudah merge minggu lalu).
Total ±12 jam tim.

## Deliverable
- docs/research-question.md  → bagian Gap (tabel Gap | Evidence | Claim), RQ,
  Contribution, RQ Check
- docs/one-pager.md v1 (tag one-pager-v1)
- Issue type:research-question tertaut ke Research ID
- PR "GATE REVIEW: Question Ready" dari branch research/g4-question

## AI Assist
Boleh: mengusulkan variasi rumusan RQ dan menguji apakah RQ dapat dijawab;
berperan sebagai reviewer skeptis (OPS-054); mengkritik konsistensi gap ↔ klaim
(OPS-051); meringkas ke One-Pager (OPS-055) — lalu tim mengedit.
Tidak boleh: memilih RQ untuk tim; menambah "bukti literatur" yang tidak ada
di synthesis matrix; menulis Contribution Statement yang tidak kami pahami.
Semua dicatat di docs/AI-USAGE.md.

## Human Check
- Tiap RQ menunjuk gap DAN baris matriks tertentu (dosen + mentor, OPS-057).
- Untuk tiap RQ kami menulis hasil yang akan MEMBATALKANNYA (OPS-054).
- Kontribusi tidak melebihi apa yang RQ dapat buktikan (OPS-053).
- RQ di Issue identik dengan RQ di dokumen (OPS-056).
- Setiap anggota memverifikasi entri AI Usage Log miliknya (OPS-058).

## Done When
[ ] PR GATE REVIEW: Question Ready termerge (label gate:G4-question).
[ ] research-question.md berisi tabel alignment, 1–3 RQ, contribution, RQ check.
[ ] Issue literature-gap ditutup dengan tautan ke gap final.
[ ] One-Pager v1 ter-tag; tidak mendahului metode/data (masih tentatif).
[ ] Jurnal W6 ditulis: apa yang berubah dari klaim awal W1 ke RQ sekarang.
```

Perhatikan tiga hal dari contoh itu: *This Week* satu kalimat outcome; *Tasks* memakai Task ID sehingga commit, Issue, dan review saling merujuk; *Done When* dapat dijawab ya/tidak oleh orang lain.

## Ringkasan 16 minggu dalam satu tabel

Baris di bawah hanyalah *This Week* tiap minggu; rinciannya ada di halaman minggu masing-masing dan [OPS-02](02-weekly-sprints.md).

| Minggu | Sprint | Gate | This Week (outcome) |
|---|---|---|---|
| W0 | S0 | G1 | Akun, tim, repositori, AI Usage Log siap. |
| W1 Endgame | S1 | G1 | Endgame dan klaim awal tertulis; PR G1. |
| W2 Problem | S2 | G2 | Problem Brief problem-first dengan bukti stakeholder; Research ID resmi. |
| W3 Search | S3 | G3 | Search strategy dijalankan; semua referensi terverifikasi. |
| W4 Evidence | S4 | G3 | 15–25 sumber dibaca dan diekstrak ke synthesis matrix. |
| W5 Gap | S5 | G3 | Pola matriks dan gap yang layak; PR G3. |
| W6 RQ | S6 | G4 | RQ yang dapat difalsifikasi + contribution; PR G4. |
| W7 Method | S7 | G5 | Desain, data plan, baseline, metrik terkunci, design card. |
| W8 Design Defense | S8 | G5 | Pitch + red team; desain direvisi; PR G5. |
| W9 Repository | S9 | G6 | Repositori dapat dijalankan satu perintah dengan seed. |
| W10 Pilot | S10 | G6 | Pilot berjalan; peer mereproduksi baseline; PR G6. |
| W11 Analysis | S11 | G7 | Hasil penuh dengan ketidakpastian, error analysis, figur jujur. |
| W12 Contribution | S12 | G7 | Tabel CER, threats v1, contribution tidak melebihi bukti; PR G7. |
| W13 Manuscript | S13 | G8 | Proposal/manuscript dari artefak; release v0.8. |
| W14 Peer Review | S14 | G8 | Memberi dan menerima review; tabel tanggapan. |
| W15 Revision | S15 | G8 | Revisi tuntas; integrity checklist ditandatangani; rehearsal. |
| W16 Defense | S16 | G8 | Defense, handoff, release v1.0 Research Pack. |

## Tiga pertanyaan sebelum menutup laptop setiap minggu

1. **Apa buktinya?** Bila jawabannya "ada di kepala saya" atau "ada di chat AI", belum selesai.
2. **Apa yang bisa membuat ini salah?** Bila tidak ada jawaban, Anda belum berpikir sebagai peneliti minggu ini.
3. **Bisakah orang lain memeriksanya?** Bila tidak, commit, catat, dan tautkan sekarang.

Itulah research thinking sebagai kebiasaan mingguan — dan amanah epistemik dalam bentuk paling sederhana: mencari kebenaran, bukan membela hipotesis.
