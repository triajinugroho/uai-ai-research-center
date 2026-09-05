# Research One-Pager Template

> **ID** TPL-01 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen/TA, dosen pengampu, mentor, reviewer gate, admin riset
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [TPL-02 Mission Tracker](02-research-mission-tracker-template.md) · [TPL-08 Research Design Card](08-research-design-card.md) · [TPL-15 Repository Template](15-research-repository-template.md)

## Cara pakai

Satu halaman yang merangkum seluruh riset: siapa pun yang membacanya dalam tiga menit harus bisa menjelaskan ulang masalah, klaim, dan cara membuktikannya. Diisi oleh tim mahasiswa (1–3 orang), disimpan di repositori riset sebagai `docs/one-pager.md`, dan ditautkan dari Issue backlog serta README riset. Dibuat bertahap: **v0** pada W2 sebagai bukti wajib G2 Problem Ready (identitas/endgame dirintis di W1, OPS-012; dilengkapi OPS-020), **v1** pada W6 untuk G4 Question Ready (OPS-055; field Method/Data/Baseline/Metrics/Threats diisi dari Design Card setelah G5 lulus, W7–W8, tanpa mengganti nomor versi, dan dibawa ke pitch W8), **v2** pada W12 untuk G7 Claim Ready memuat hasil, klaim, dan keterbatasan (OPS-110), dibawa ke Research Defense W16 (G8). Reviewer memakai halaman ini sebagai pintu masuk PR `GATE REVIEW`; admin riset menyalin baris **Gate saat ini** dan **Next evidence** ke Mission Control ([TPL-02](02-research-mission-tracker-template.md)). Batas: ±400 kata di luar tabel; rincian pindah ke `docs/`.

## Field wajib per versi

| # | Field | v0 (G2, W2) | v1 (G4, W6; diperbarui setelah G5) | v2 (G7, W12) |
|---|---|---|---|---|
| 1 | Research ID | sementara `UIAI-YYYY-TBD` → resmi saat PR G2 di-merge | wajib | wajib |
| 2 | Judul kerja | wajib | wajib (boleh berubah) | wajib |
| 3 | Tim | wajib | wajib | wajib |
| 4 | Mentor | kandidat | wajib | wajib |
| 5 | Entry door | wajib | wajib | wajib |
| 6 | Endgame (minimum / target / aspirasi) | wajib | wajib | wajib |
| 7 | Problem & why it matters | wajib | wajib | wajib |
| 8 | Stakeholder & keputusan yang berubah | wajib | wajib | wajib |
| 9 | What we know (3 poin + sitasi) | ≥1 poin, sumber terverifikasi | 3 poin dari synthesis matrix | 3 poin |
| 10 | Gap | `[menunggu G3–G4]` | wajib, ditelusuri ke matriks | wajib |
| 11 | RQ / hipotesis | `[menunggu G3–G4]` | wajib | wajib |
| 12 | Contribution | expected contribution tentatif (OPS-020); final `[menunggu G4]` | wajib (jenis + mengapa bermakna) | wajib (direvisi agar tidak melebihi bukti) |
| 13 | Method | `[menunggu G5]` | tentatif; setelah G5 lulus: wajib (rujuk TPL-08 / TPL-05) | wajib (yang aktual) |
| 14 | Data | `[menunggu G5]` | tentatif; setelah G5 lulus: wajib (rujuk TPL-08 / TPL-05) | wajib (yang aktual) |
| 15 | Baseline | `[menunggu G5]` | tentatif; setelah G5 lulus: wajib (rujuk TPL-08 / TPL-05) | wajib (yang aktual) |
| 16 | Metrics | `[menunggu G5]` | tentatif; setelah G5 lulus: wajib (rujuk TPL-08 / TPL-05) | wajib (yang aktual) |
| 17 | Threats to validity | — | setelah G5 lulus: wajib (4 jenis, Threats v1 di docs/research-design.md) | wajib (Threats v2 pasca-hasil, results/analysis.md) |
| 18 | Results (angka utama ± variasi, rujuk results/main/summary.csv) | — | — | wajib |
| 19 | Claim (CER ringkas per RQ, rujuk tabel CER results/analysis.md) | — | — | wajib; hasil negatif dilaporkan |
| 20 | Limitations (batas generalisasi + future work) | — | — | wajib |
| 21 | Ethics / AI note | AI Usage Log dimulai | wajib ringkas | wajib |
| 22 | Next evidence | wajib | wajib | wajib |
| 23 | Gate saat ini | wajib | wajib | wajib |

Aturan: field yang belum wajib ditulis `[menunggu Gn — target vN]` (mis. `[menunggu G3–G5 — target v1]`), bukan dikosongkan; field wajib yang kosong = gate tidak dapat direview.

## Template (salin ke `docs/one-pager.md`)

```markdown
# Research One-Pager — [Research ID] · v[0/1/2] · [YYYY-MM-DD]

| Field | Isi |
|---|---|
| Research ID | [UIAI-YYYY-TBD sampai PR G2 di-merge → UIAI-YYYY-NNN] |
| Judul kerja | [judul; boleh berubah sampai G4] |
| Tim | [nama 1 (@github)], [nama 2], [nama 3] |
| Mentor | [nama dosen] — [klaster C1–C4] |
| Entry door | [Problem / Dataset / Faculty Research / Course Project / Partner / Competition] |
| Endgame | Minimum: TA Ready · Target: Research Ready · Aspirasi: [paper/dataset/artefak/HKI/produk atau —] |
| Problem & why it matters | [2–3 kalimat: fenomena nyata, konteks Indonesia/UAI, mengapa penting sekarang] |
| Stakeholder | [siapa] — keputusan yang berubah bila riset berhasil: [apa] |
| What we know | 1. [temuan] ([Penulis, Tahun, DOI]) 2. [temuan] ([…]) 3. [temuan] ([…]) |
| Gap | [apa yang belum diketahui / bertentangan / belum diuji — rujuk baris synthesis matrix] |
| RQ / hipotesis | RQ1: [...] · RQ2: [...] · H1: [dapat difalsifikasi] |
| Contribution | [empiris / artefak / metode / dataset / replikasi / studi kasus] — [mengapa bermakna] |
| Method | [jenis dari Computing Research Methods Map] — [1 kalimat desain] |
| Data | [sumber, ukuran, akses, privasi; Dataset ID bila ada] |
| Baseline | [pembanding paling sederhana yang masuk akal] |
| Metrics | [metrik selaras RQ + prosedur evaluasi anti-leakage] |
| Threats to validity | Internal: [...] · Eksternal: [...] · Konstruk: [...] · Statistik: [...] |
| Results | [v0–v1: menunggu G7 — target v2 · v2: angka utama ± variasi per RQ, rujuk results/main/summary.csv] |
| Claim | [v0–v1: menunggu G7 — target v2 · v2: CER ringkas per RQ, rujuk tabel CER results/analysis.md; hasil negatif dilaporkan] |
| Limitations | [v0–v1: menunggu G7 — target v2 · v2: batas generalisasi + future work] |
| Ethics / AI note | [consent/anonimisasi/persetujuan etik; AI dipakai untuk apa; log di docs/AI-USAGE.md] |
| Next evidence | [bukti konkret berikutnya + tanggal] |
| Gate saat ini | [G1–G8] — [Lulus / Review / Active] — PR #[n] |
```

## Contoh terisi (v1 diperbarui untuk G5, W8; field hasil menunggu v2)

| Field | Isi |
|---|---|
| Research ID | UIAI-2026-001 |
| Judul kerja | AI-assisted academic advising for Indonesian universities |
| Tim | [Mahasiswa A] (@[isi]), [Mahasiswa B] (@[isi]) |
| Mentor | [Dosen C3] — C3 Human-Centered & Responsible AI · Domain: Education |
| Entry door | Problem (problem owner: Kaprodi/dosen wali) |
| Endgame | Minimum: TA Ready · Target: Research Ready · Aspirasi: paper konferensi nasional + dataset anonim rencana studi |
| Problem & why it matters | Dosen wali menangani puluhan mahasiswa dengan waktu konsultasi terbatas; mahasiswa memilih mata kuliah dengan informasi tidak lengkap sehingga terjadi pelanggaran prasyarat dan keterlambatan lulus. Asisten advising berbasis LLM menjanjikan bantuan, tetapi belum ada bukti terkontrol pada kurikulum Indonesia (OBE, prasyarat, paket semester). |
| Stakeholder | Mahasiswa, dosen wali, Kaprodi — keputusan yang berubah: rencana studi per semester dan alokasi waktu konsultasi |
| What we know | 1. Sistem rekomendasi mata kuliah berbasis riwayat akademik meningkatkan akurasi prediksi nilai, tetapi jarang mengevaluasi validitas prasyarat ([Penulis, Tahun, DOI: isi]). 2. Asisten LLM untuk advising diuji terutama di konteks universitas Amerika/Eropa dengan kurikulum fleksibel ([isi]). 3. Kepercayaan pengguna terhadap saran AI akademik bergantung pada penjelasan dan kemampuan verifikasi ([isi]). |
| Gap | Belum ada evaluasi terkontrol LLM+RAG vs baseline rule-based pada constraint kurikulum Indonesia, dan belum ada pengukuran gabungan validitas rekomendasi + persepsi dosen wali (baris M-07, M-12, M-19 synthesis matrix). |
| RQ / hipotesis | RQ1: Apakah rekomendasi rencana studi dari asisten LLM+RAG memenuhi aturan prasyarat/SKS lebih baik daripada baseline rule-based? · RQ2: Bagaimana dosen wali menilai relevansi elektif dan kegunaan asisten? · H1: tingkat pelanggaran constraint LLM+RAG ≤ rule-based; H2: skor relevansi elektif LLM+RAG > rule-based menurut penilaian dosen wali. |
| Contribution | Empiris + artefak: bukti terkontrol pertama pada konteks kurikulum Informatika UAI, benchmark 40 kasus advising, prototipe open-source. |
| Method | Design science + benchmarking offline + user study kecil (mixed) — lihat [TPL-08](08-research-design-card.md) |
| Data | Dokumen kurikulum (public); transkrip anonim 120 mahasiswa (UAI, restricted, consent) — DS-2026-001; 40 kasus advising sintetis untuk pilot |
| Baseline | Rule-based prerequisite checker + heuristik greedy per semester |
| Metrics | Constraint-violation rate; precision@5 relevansi elektif vs gold dosen wali; skor kegunaan (Likert 5) — split kasus pilot/evaluasi ditetapkan sebelum run |
| Threats to validity | Internal: gold label subjektif → 2 dosen wali + agreement. Eksternal: 1 prodi → klaim dibatasi. Konstruk: "relevansi" ≠ "kebenaran" → definisi operasional. Statistik: n kecil → laporkan interval, bukan hanya rata-rata. |
| Results | [menunggu G7 — target v2] |
| Claim | [menunggu G7 — target v2] |
| Limitations | [menunggu G7 — target v2] |
| Ethics / AI note | Data mahasiswa dianonimkan, consent tertulis, tidak masuk GitHub; AI dipakai untuk coding support dan kritik desain, dicatat di `docs/AI-USAGE.md` |
| Next evidence | Experiment Card pilot 40 kasus + notulen red team W8 — [YYYY-MM-DD] |
| Gate saat ini | G5 Method Ready — Review — PR #[n] |

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Problem | Orang luar dapat mengulang masalah dan siapa yang peduli dalam dua kalimat | Masalah hanya justifikasi algoritma yang sudah dipilih |
| What we know | Tiga temuan dengan sitasi terverifikasi (DOI/URL), berasal dari synthesis matrix | Daftar judul paper tanpa temuan; sitasi dari AI yang belum dicek |
| Gap → RQ | Setiap RQ menunjuk baris matriks; hipotesis dapat difalsifikasi | "Belum ada yang meneliti di UAI" |
| Method–baseline–metric | Ketiganya konsisten dengan RQ; baseline paling sederhana disebut | Metrik dipilih sebelum RQ jelas; tanpa baseline |
| Threats | Empat jenis, masing-masing dengan mitigasi | "Keterbatasan waktu dan data" |
| Panjang | Satu halaman; rincian di `docs/` | Tiga halaman narasi |
| Versi | Header memuat versi, tanggal, gate; perubahan terlihat di git | File ditimpa tanpa jejak |
