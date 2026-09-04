# Peer Review Template

> **ID** TPL-12 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Peer reviewer (mahasiswa), dosen reviewer, mentor, penulis (tim riset), dosen pengampu
> **Terkait** [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [CONTRIBUTING.md §3](../../CONTRIBUTING.md) · [TPL-11 Integrity Checklist](11-research-integrity-checklist.md) · [TPL-13 Defense](13-research-defense-template.md) · [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md)

## Cara pakai

Dipakai setiap kali sebuah artefak riset direview: PR `GATE REVIEW` (G2–G8), red team W8, dan peer review manuscript W14 (setiap mahasiswa mereview minimal satu Research Pack tim lain). Reviewer mengisi template ini sebagai komentar PR atau file `reviews/review-[gate]-[reviewer].md`; komentar tidak dihapus karena menjadi bukti proses ilmiah. Setiap dimensi diberi skor **dan** komentar wajib dua bagian: *apa yang kurang* dan *bukti apa yang dibutuhkan* — skor tanpa komentar tidak diterima. Penulis membalas dengan **response letter** (bagian akhir template) sebelum review ulang; PR di-merge hanya bila rekomendasi *Accept* atau *Minor* yang sudah ditindaklanjuti.

## Skala

| Skor | Arti |
|---|---|
| 4 | Kuat: lengkap, didukung bukti, dapat diperiksa; tidak ada perbaikan penting |
| 3 | Memadai: memenuhi definition of done gate; perbaikan kecil |
| 2 | Lemah: ada, tetapi bukti tidak cukup atau tidak konsisten; perbaikan besar |
| 1 | Tidak ada / tidak dapat diterima |

Dimensi yang tidak relevan untuk gate tersebut (mis. *Results* pada G2) ditulis `—`.

## Template review (salin ke komentar PR)

```markdown
# Review — [Research ID] · [artefak: One-Pager v1 / Design Card / Research Pack / Manuscript] · Gate [Gn]
Reviewer: [nama/akun] · Peran: [peer / dosen / mentor / red team] · Tanggal: [YYYY-MM-DD] · Versi/commit: [hash]

## Penilaian
| Dimensi | Skor (1–4) | Apa yang kurang | Bukti apa yang dibutuhkan |
|---|---|---|---|
| Problem (nyata, penting, stakeholder jelas) | | | |
| Evidence (synthesis matrix, sumber terverifikasi, pola terlihat) | | | |
| RQ (dapat ditelusuri ke gap; dapat dijawab; hipotesis dapat difalsifikasi) | | | |
| Method (desain, data, baseline, metrik, kontrol; dapat dijalankan orang lain) | | | |
| Results (pilot berjalan, reproducible, dilaporkan jujur termasuk variasi) | | | |
| Claim (CER eksplisit; tidak melebihi bukti; tidak kausal dari korelasi) | | | |
| Limitations (threats to validity 4 jenis + mitigasi; hasil negatif dibahas) | | | |

## Integritas (wajib dicek)
- [ ] Referensi yang saya cek acak ([n] buah) semuanya ada dan sesuai isi
- [ ] AI Usage Log ada dan sesuai dengan artefak
- [ ] Tidak ada indikasi leakage / metric switching / data tanpa provenance
Temuan integritas (bila ada): [...] → langsung dilaporkan ke dosen pengampu

## Rekomendasi
[ ] Accept — gate lulus, merge
[ ] Minor revision — merge setelah perbaikan kecil berikut: [...]
[ ] Major revision — bukti penting belum ada; review ulang setelah: [...]
[ ] Reject (untuk gate ini) — kembali ke gate [Gn-1] karena: [...]

## Ringkasan untuk penulis
Tiga kekuatan: 1. [...] 2. [...] 3. [...]
Tiga perbaikan utama (urut prioritas): 1. [...] 2. [...] 3. [...]
Satu pertanyaan terbesar yang harus bisa dijawab di defense: [...]
Estimasi usaha revisi: [jam/hari]
```

## Etika reviewer

1. Review artefak, bukan orang; tulis dengan nada yang ingin Anda terima.
2. Konflik kepentingan (satu tim, kerabat, kompetisi langsung) → tolak menjadi reviewer.
3. Kerahasiaan: isi artefak yang direview tidak dibagikan di luar proses; data restricted tidak diunduh.
4. Baca seluruh artefak; cek minimal 3 referensi secara acak; jalankan kode bila review G6.
5. Tidak menilai berdasarkan apakah hipotesis "menarik"; nilai berdasarkan bukti dan kejelasan.
6. AI boleh dipakai reviewer untuk memahami istilah, bukan untuk menghasilkan penilaian; catat di AI Usage Log reviewer sendiri; jangan mengunggah artefak INTERNAL ke tool eksternal.
7. Temuan integritas dilaporkan ke dosen pengampu, bukan dibahas publik.

## Template response letter (penulis, salin ke komentar PR balasan)

```markdown
# Response to Review — [Research ID] · Gate [Gn] · [YYYY-MM-DD] · versi baru: [hash]
| # | Komentar reviewer (ringkas) | Tanggapan (setuju / setuju sebagian / tidak setuju + alasan) | Perubahan (file/section/commit) atau alasan tidak diubah |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
Ringkasan perubahan: [3–5 baris]. Hal yang sengaja tidak diubah dan alasannya: [...].
```

Aturan: setiap komentar dijawab satu per satu; "tidak setuju" harus disertai bukti/argumen, bukan penolakan; perubahan menunjuk commit.

## Contoh terisi (cuplikan review G4, One-Pager v1 UIAI-2026-001)

| Dimensi | Skor | Apa yang kurang | Bukti apa yang dibutuhkan |
|---|---|---|---|
| Problem | 4 | — | — |
| Evidence | 3 | Matriks 18 sumber, tetapi kolom "keterbatasan" kosong pada 6 baris | Isi keterbatasan tiap sumber; tandai sumber yang bertentangan (M-07 vs M-12) |
| RQ | 3 | RQ2 "kegunaan" belum didefinisikan operasional; H2 belum dapat difalsifikasi | Definisi operasional relevansi elektif (gold dari siapa, skala apa) dan arah H2 yang dapat salah |
| Method | — | (belum wajib di G4) | — |
| Results | — | — | — |
| Claim | 3 | Contribution "pertama di Indonesia" tidak dapat dibuktikan dari matriks | Ubah menjadi "belum ditemukan dalam pencarian [basis data, tanggal]" atau hapus |
| Limitations | 2 | Belum ada threats awal | Minimal ancaman eksternal (1 prodi) dan konstruk (relevansi) |

Integritas: 3 referensi dicek (M-03, M-11, M-15) — semua ada dan sesuai; AI Usage Log 6 entri, konsisten. Rekomendasi: **Minor revision**. Ringkasan: kekuatan — problem sangat jelas, matriks rapi, RQ1 tajam; perbaikan — definisi operasional RQ2, klaim "pertama", threats awal; pertanyaan terbesar — "Apa bedanya hasil Anda dengan sistem prasyarat otomatis yang sudah ada di SIAKAD?"; usaha revisi ±1 hari.

Cuplikan response letter: `| 2 | RQ2 belum operasional | Setuju | Ditambah definisi: relevansi = skor 1–5 dari 2 dosen wali terhadap 5 elektif teratas; H2 ditulis ulang — docs/research-question.md §2, commit [hash] |`

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Komentar | Menyebut yang kurang **dan** bukti yang dibutuhkan, spesifik ke baris/section | "Perlu diperbaiki" |
| Skor | Konsisten dengan komentar dan definition of done gate | Skor 4 dengan daftar kekurangan panjang |
| Integritas | Referensi dicek acak; hasil disebut | Kotak dicentang tanpa memeriksa |
| Rekomendasi | Jelas apa syarat merge | "Bagus, lanjutkan" |
| Response letter | Setiap komentar dijawab dengan commit | Balasan "sudah diperbaiki semua" |
