# Research Integrity Checklist

> **ID** TPL-11 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa, pembimbing/mentor, dosen pengampu, penguji defense, reviewer manuscript
> **Terkait** [MET-07 Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [MET-06 5E Rubric](../04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [OPS-03 G8](../06-execution-os/03-research-gates.md) · [TPL-10 AI Usage Log](10-ai-usage-log-template.md) · [TPL-15 Repository Template](15-research-repository-template.md) · [MST-03 Glossary (Amanah epistemik)](../00-master/03-glossary.md)

## Cara pakai

Checklist ini adalah **Research Integrity Gate**: lulus/gagal, bukan skor. Diisi oleh mahasiswa (ketua tim) dan ditandatangani bersama pembimbing/mentor **sebelum** Research Defense (W16, G8) dan sebelum setiap submission manuscript/rilis artefak; disimpan sebagai `docs/integrity-checklist.md` di repositori riset dan dilampirkan pada PR `GATE REVIEW: Contribution Ready`. Setiap item harus ✓ dengan bukti yang dapat dibuka (file, commit, tautan), atau `N/A` dengan alasan. Satu item saja yang gagal (fabrikasi, sitasi palsu, AI tidak diungkap, plagiarisme) membuat gate gagal terlepas dari kualitas riset lainnya, sesuai amanah epistemik ([MST-03](../00-master/03-glossary.md)). Dosen pengampu memakai hasilnya sebagai prasyarat penilaian 5E ([MET-06](../04-metopen-research-studio/06-assessment-and-5e-rubric.md)).

## Template (salin ke `docs/integrity-checklist.md`)

```markdown
# Research Integrity Checklist — [Research ID] · [judul] · [YYYY-MM-DD]
Tahap: [Defense G8 / Submission ke [venue] / Rilis artefak [ART-…]]

## A. Data
- [ ] A1 Tidak ada data yang dibuat-buat, diubah, atau dihapus untuk memperbaiki hasil — Bukti: [data/README.md, log akses, commit]
- [ ] A2 Provenance jelas: asal, tanggal, versi, cara pengumpulan, Dataset ID — Bukti: [DS-…, data/README.md]
- [ ] A3 Data yang dibuang/outlier dilaporkan dengan alasan yang ditetapkan sebelum analisis — Bukti: [results/analysis.md §]

## B. Analisis
- [ ] B1 Tidak ada metric switching: metrik & ambang sama dengan pra-registrasi Experiment Card — Bukti: [experiments/pilot-01/experiment-card.md §Pra-registrasi]
- [ ] B2 Tidak ada seed/run cherry-picking: semua run dilaporkan (mean ± variasi, n) — Bukti: [results/…]
- [ ] B3 Tidak ada leakage: split per entitas/waktu, tuning hanya di validation, test disentuh sekali — Bukti: [src/data.py, src/evaluate.py, experiments/pilot-01/experiment-card.md]
- [ ] B4 Baseline dijalankan dan dilaporkan pada kondisi yang sama — Bukti: [results/…]

## C. Sitasi
- [ ] C1 Semua referensi benar-benar dibaca (minimal bagian yang dikutip) — Bukti: [synthesis matrix, catatan bacaan]
- [ ] C2 Setiap referensi terverifikasi ada (DOI/URL dibuka) — Bukti: [references.bib, kolom verified]
- [ ] C3 Kutipan/parafrase menunjuk sumber yang tepat; tidak ada sitasi sekunder disamarkan sebagai primer — Bukti: [manuscript]

## D. Plagiarisme
- [ ] D1 Similarity check dijalankan pada dokumen final; hasil ≤ ambang Prodi [isi] dan bagian tinggi dijelaskan — Bukti: [laporan similarity, tanggal, %]
- [ ] D2 Tidak ada self-plagiarism dari tugas/laporan lain tanpa sitasi — Bukti: [pernyataan]

## E. AI
- [ ] E1 AI Usage Log lengkap sejak onboarding S0 (pra-W1) dan dicatat hari yang sama — Bukti: [docs/AI-USAGE.md §Log, n entri]
- [ ] E2 AI Usage Statement ada di docs/AI-USAGE.md, paper/AI-USAGE-STATEMENT.md, README, dan manuscript; konsisten dengan log — Bukti: [tautan]
- [ ] E3 Tidak ada referensi, data, angka hasil, atau figur yang dihasilkan AI tanpa verifikasi — Bukti: [log kolom verification; referensi dibuang: n]
- [ ] E4 Tidak ada data sensitif yang diberikan ke tool AI eksternal — Bukti: [log; pernyataan]

## F. Etika & privasi
- [ ] F1 Consent diperoleh untuk data manusia/partisipan; formulir tersimpan di luar GitHub — Bukti: [docs/ethics.md, lokasi formulir]
- [ ] F2 Anonimisasi/pseudonimisasi dilakukan sebelum data dipakai; tidak ada data pribadi di repo — Bukti: [skrip anonimisasi, audit repo]
- [ ] F3 Persetujuan komite etik/pemilik data diperoleh bila disyaratkan — Bukti: [nomor surat / N/A + alasan]
- [ ] F4 Lisensi data dan artefak sesuai LICENSING.md — Bukti: [README tabel lisensi]

## G. Reproducibility
- [ ] G1 README riset memuat cara menjalankan ulang (langkah, perintah) — Bukti: [README §Reproducibility]
- [ ] G2 Environment terkunci (requirements.txt/environment.yml), seed dan config tersimpan — Bukti: [file]
- [ ] G3 Minimal satu reproduksi oleh peer berhasil dan dicatat — Bukti: [docs/reviews/reproduction-pilot-01.md; experiments/pilot-01/experiment-card.md §Reproduksi peer]

## H. Authorship & kontribusi
- [ ] H1 Semua penulis memberi kontribusi substantif dan menyetujui versi final; tidak ada guest/ghost author — Bukti: [CITATION.cff, pernyataan kontribusi]
- [ ] H2 Kontribusi tiap anggota tim dan mentor dinyatakan — Bukti: [README §Researchers]

## I. Klaim
- [ ] I1 Setiap klaim menunjuk tabel/figur tertentu (Claim–Evidence–Reasoning) — Bukti: [results/analysis.md tabel CER]
- [ ] I2 Tidak ada klaim kausal dari korelasi; tidak ada generalisasi melampaui sampel — Bukti: [threats to validity]
- [ ] I3 Contribution statement tidak melebihi bukti — Bukti: [manuscript §Contribution]

## J. Hasil negatif
- [ ] J1 Hasil negatif/tidak sesuai hipotesis dilaporkan, bukan disembunyikan — Bukti: [results/…]
- [ ] J2 Penyimpangan dari rencana (pra-registrasi) dicatat dengan alasan — Bukti: [experiments/pilot-01/experiment-card.md §Penyimpangan dari rencana; results/analysis.md]

## Keputusan
Jumlah item: [n] · ✓: [n] · N/A (beralasan): [n] · Gagal: [n]
Hasil: [ ] PASS — semua item ✓/N/A   [ ] FAIL — item gagal: [kode item]; tindakan: [apa, sampai kapan]

## Tanda tangan
| Peran | Nama | Tanda tangan / akun GitHub | Tanggal |
|---|---|---|---|
| Mahasiswa (ketua tim) | | | |
| Anggota tim | | | |
| Pembimbing / mentor | | | |
| Dosen pengampu (untuk G8) | | | |

Pernyataan: "Kami menyatakan bahwa isi checklist ini benar; kami memahami bahwa pelanggaran integritas membuat gate gagal dan dapat berakibat sanksi akademik sesuai peraturan yang berlaku."
```

## Aturan pass/fail

| Kondisi | Keputusan |
|---|---|
| Semua item ✓ atau N/A dengan alasan yang diterima pembimbing | PASS |
| Ada item tanpa bukti yang dapat dibuka | Belum dapat diputuskan — lengkapi bukti, ulangi |
| Ada satu item gagal pada A, C2, D1, E1–E3, atau F1–F2 | FAIL — gate gagal; tidak dapat defense/submission sampai diperbaiki dan diverifikasi ulang |
| Item gagal pada bagian lain | FAIL — revisi dalam ≤ 1 minggu, review ulang oleh pembimbing |

## Contoh terisi (cuplikan)

UIAI-2026-001 · Tahap: Defense G8 · 2026-12-[dd]

- [x] B1 Tidak ada metric switching — Bukti: `experiments/pilot-01/experiment-card.md`, `experiments/main/README.md`: metrik violation rate & precision@5, ambang 10 poin persen, sama dengan pra-registrasi.
- [x] B2 Semua run dilaporkan — Bukti: `results/main/summary.csv`, 80 kasus × 3 run, mean ± sd di `results/analysis.md` Tabel 2.
- [x] C2 Referensi terverifikasi — Bukti: `references.bib` 22 entri, kolom `verified=2026-10-[dd]`; 3 usulan AI dibuang (AI Usage Log #6).
- [x] E4 Tidak ada data sensitif ke tool AI — Bukti: log #7 memakai fungsi tanpa data; sampel sintetis untuk #9.
- [x] F2 Anonimisasi — Bukti: `src/data.py` (fungsi anonymize), audit repo 2026-11-[dd] oleh [Mahasiswa C]: 0 kolom identitas.
- [ ] N/A F3 Persetujuan komite etik — alasan: data internal Prodi dengan consent dan anonimisasi; pemilik data (Kaprodi) menyetujui lewat surat [nomor — isi]; diterima pembimbing.
- [x] J1 Hasil negatif dilaporkan — Bukti: H1 tidak terdukung pada pilot (LLM+RAG masih melanggar 7,5 %), dibahas di `results/analysis.md` §4.

Keputusan: 30 item · ✓ 29 · N/A 1 · Gagal 0 → **PASS**. Ditandatangani [Mahasiswa A], [Mahasiswa B], [Dosen C3], [dosen pengampu], 2026-12-[dd].

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Bukti | Setiap ✓ menunjuk file/commit/tautan yang dapat dibuka | ✓ tanpa bukti |
| N/A | Alasan tertulis dan disetujui pembimbing | N/A untuk menghindari item sulit |
| Waktu | Diisi bertahap sejak G6, difinalkan sebelum defense | Diisi satu malam sebelum defense |
| Kejujuran | Hasil negatif dan penyimpangan tercatat | Semua "sempurna" tanpa catatan |
| Tanda tangan | Mahasiswa dan pembimbing menandatangani versi yang sama | Hanya mahasiswa |
