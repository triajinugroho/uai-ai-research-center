# Templates — Indeks 15 Template Research OS untuk Mahasiswa

> **Status** Draft v0.1 (2026-09) · Indeks saja; isi template tidak diduplikasi di sini — buka file sumbernya di [`research-os/08-templates/`](../../research-os/08-templates/01-research-one-pager-template.md)
> **Terkait** [Studio README](../README.md) · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [TPL-15 Research Repository](../../research-os/08-templates/15-research-repository-template.md) · [research-gates](../research-gates/README.md)

Setiap template berisi: cara pakai, template siap salin, contoh terisi, dan kriteria kualitas (good vs weak). Salin bagian *Template* ke lokasi yang disebut di kolom **Disimpan di** (struktur repositori riset sesuai [MET-04 §4](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) dan TPL-15), isi bertahap mengikuti minggu, dan tautkan dari PR gate. Field yang belum wajib ditulis `[belum diisi — target vN]`, bukan dikosongkan.

## Tabel indeks

| Template | ID | Dipakai minggu | Gate | Disimpan di |
|---|---|---|---|---|
| [Research One-Pager](../../research-os/08-templates/01-research-one-pager-template.md) | TPL-01 | W1 (identitas + endgame, v0 parsial), W2 (v0), W6 (v1), W12 (v2: hasil & klaim) | G2 (v0), G4 (v1), G7 (v2) | `docs/one-pager.md` di repositori riset; ditautkan dari Issue backlog dan README riset |
| [Research Mission Tracker](../../research-os/08-templates/02-research-mission-tracker-template.md) | TPL-02 | Setiap Jumat setelah PR gate merge (diisi admin riset/dosen; tim mengisi *Next Evidence*) | Semua gate | GitHub Projects **Mission Control** (organisasi) + cermin Google Sheet; bukan di repositori riset |
| [Research Leaderboard](../../research-os/08-templates/03-research-leaderboard-template.md) | TPL-03 | Mingguan oleh admin/dosen; dilihat kelas di W8 dan W16 | G2–G8 (status per kolom) | `research-backlog/BACKLOG.md` bagian status atau README kelas/organisasi |
| [Research Backlog](../../research-os/08-templates/04-research-backlog-template.md) | TPL-04 | S0 (memilih masalah, pra-W1), W2 (Research ID resmi ditetapkan saat PR G2 di-merge) | G1–G2 | Issue **Research Problem** + `research-backlog/problems/UIAI-YYYY-NNN-<slug>.md` |
| [Dataset Registry](../../research-os/08-templates/05-dataset-registry-template.md) | TPL-05 | W7 (Data Plan); diperbarui bila akses/lisensi berubah, W16 | G5 (wajib sebelum lulus) | `datasets-registry/datasets/ds-YYYY-NNN-<slug>.md` (metadata saja) + `data/README.md` di repositori riset |
| [Publication Venue Registry](../../research-os/08-templates/06-publication-venue-registry-template.md) | TPL-06 | W1 (aspirasi endgame), W13 (backward design manuscript) | G1, G8 | `publications/PUBLICATIONS.md` bagian Venue Registry (dikelola pengelola publications); tim hanya membaca |
| [Faculty Research Map](../../research-os/08-templates/07-faculty-research-map-template.md) | TPL-07 | W1 (mencari kandidat mentor per klaster) | G1 | Lampiran AIR-03 di `research-os/03-ai-research-ecosystem/` (diisi dosen); tim hanya membaca |
| [Research Design Card](../../research-os/08-templates/08-research-design-card.md) | TPL-08 | W7 (v1), W8 (v2 setelah red team); diperbarui W10, W12 bila desain berubah | G5; revisi G6, G7 | `docs/design-card.md` (kartu satu halaman) yang menunjuk rincian di `docs/research-design.md` dan `docs/data-plan.md` |
| [Experiment Card](../../research-os/08-templates/09-experiment-card.md) | TPL-09 | W8 (pra-registrasi pilot), W10 (hasil aktual + keputusan), W11 (eksperimen utama) | G5, G6, G7 | `experiments/pilot-01/experiment-card.md` + `experiments/pilot-01/config.yaml` (eksperimen utama W11: `experiments/main/`); dirujuk dari `experiments/README.md` |
| [AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md) | TPL-10 | S0 (entri pertama, pra-W1) sampai W16; statement dirakit W13, final W16 | Diperiksa setiap gate (G3 sumber, G6 kode, G8 statement) | `docs/AI-USAGE.md` (log + ringkasan AI Usage Statement); statement final untuk naskah di `paper/AI-USAGE-STATEMENT.md` |
| [Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) | TPL-11 | Diisi bertahap sejak W10; ditandatangani W15 sebelum defense; ulang sebelum submission | G8 (prasyarat defense) | `docs/integrity-checklist.md`; dilampirkan pada PR `GATE REVIEW: Contribution Ready` |
| [Peer Review](../../research-os/08-templates/12-peer-review-template.md) | TPL-12 | W8 (red team), W14 (review manuscript tim lain, 2 review per mahasiswa); dipakai reviewer di setiap PR gate | G2–G8 | Komentar PR gate tim yang direview, atau file di `docs/reviews/` repositori tim yang direview (mis. `docs/reviews/midterm-red-team.md`, W8); response letter di komentar balasan (W14: `paper/response-to-reviewers.md`) |
| [Research Defense](../../research-os/08-templates/13-research-defense-template.md) | TPL-13 | W8 (Design Defense: slide 1–4 dan 6 penuh, slide 5 rencana pilot), W14 (draft), W15 (final + rehearsal), W16 (defense) | G5, G8 | `presentation/midterm-pitch.pdf`, `presentation/defense-final.pdf` (7–10 menit, ≤10 slide + maksimal 3 slide cadangan), notulen di `docs/reviews/` |
| [Research Handoff](../../research-os/08-templates/14-research-handoff-template.md) | TPL-14 | W16 (Metopen → TA); juga bila tim berhenti di tengah | G8 | `docs/handoff.md`; ditautkan dari README riset dan Issue backlog |
| [Research Repository](../../research-os/08-templates/15-research-repository-template.md) | TPL-15 | S0 (membuat repo, pra-W1), W9 (`src/`, `experiments/`, environment), W16 (CITATION.cff, CHANGELOG, README final) | G1, G6, G8 | Repositori riset `proj-YYYY-<topik>` itu sendiri: struktur folder + README riset standar |

## Urutan pemakaian dalam satu semester

```
S0     TPL-15 repo → TPL-04 pilih masalah → TPL-10 log dimulai (onboarding, pra-W1)
W1     TPL-07 cari mentor → TPL-06 cek venue aspirasi → TPL-01 v0 (identitas)         → G1
W2     TPL-01 v0 lengkap                                                   → G2
W3–W5  (synthesis matrix, kolom di MET-03 W4) + TPL-10 verifikasi sumber   → G3
W6     TPL-01 v1                                                           → G4
W7–W8  TPL-08 design card → TPL-05 dataset card → TPL-09 pilot pra-registrasi → TPL-13 pitch W8 → TPL-12 red team → G5
W9–W10 TPL-15 (src/experiments/env) → TPL-09 hasil aktual → TPL-12 catatan reproduksi peer → G6
W11–W12 TPL-09 eksperimen utama → TPL-01 v2 → G7
W13–W16 TPL-10 statement → TPL-12 review manuscript → TPL-11 checklist → TPL-13 defense → TPL-14 handoff → TPL-02/03 diperbarui → G8
```

## Pertanyaan yang sering muncul

| Pertanyaan | Jawaban |
|---|---|
| Template synthesis matrix tidak ada di daftar? | Benar; kolom matriks (problem, metode, data, metrik, hasil, keterbatasan, relevansi, verified, quality) ditetapkan di [MET-03 W4](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) dan disimpan sebagai `docs/literature/synthesis-matrix.csv`. Cuplikan terisi ada di [examples](../examples/README.md). |
| Boleh mengubah kolom template? | Boleh menambah kolom; jangan menghapus kolom wajib (reviewer memakainya). Catat perubahan di header artefak. |
| Template mana yang harus ada sebelum eksperimen pertama? | TPL-08 (design card), TPL-05 (dataset card), TPL-09 (pra-registrasi pilot) — eksperimen tidak boleh dimulai bila baseline dan metrik masih kosong. |
| Template mana yang tidak diisi mahasiswa? | TPL-02, TPL-03, TPL-06, TPL-07 diisi admin riset/dosen/pengelola; mahasiswa membaca dan memperbarui field *Next Evidence* saja. |
| Format proposal TA memakai template mana? | Format resmi Prodi (`[isi]`); pemetaan artefak Research Pack → bagian proposal ada di [MET-05](../../research-os/04-metopen-research-studio/05-publication-backward-design.md). |

## Aturan singkat

1. **Satu sumber, satu lokasi.** Jangan menyalin isi template ke folder studio atau ke dokumen lain; salin hanya ke repositori riset Anda pada path di kolom *Disimpan di*.
2. **Versi terlihat di git.** Header artefak memuat versi, tanggal, gate; file tidak ditimpa tanpa jejak commit.
3. **Bagian pra-registrasi tidak diubah** (Experiment Card): bila desain berubah setelah run, buat kartu baru dan catat alasan.
4. **Metadata, bukan data.** TPL-05 dan `data/README.md` hanya berisi metadata; data mentah sensitif tidak pernah masuk GitHub ([SECURITY.md](../../SECURITY.md)).
5. **Placeholder eksplisit.** Nama dosen, dataset riil, dan nomor surat ditulis `[isi]` sampai diverifikasi; referensi ditulis lengkap hanya setelah DOI/URL dibuka.

Contoh terisi untuk TPL-01, TPL-08, TPL-10, synthesis matrix, dan PR gate ada di [examples](../examples/README.md); kaitan template dengan 16 artefak Research Pack ada di [MET-04 §2](../../research-os/04-metopen-research-studio/04-research-pack-specification.md).
