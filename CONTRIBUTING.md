# CONTRIBUTING — Cara Berkontribusi

Repository ini memakai GitHub sebagai **research operating system**. Kontribusi bukan hanya kode: masalah riset, pertanyaan, dataset, eksperimen, naskah, dan review ilmiah semuanya lewat Issue dan Pull Request. Ikuti definisi di [Glossary](research-os/00-master/03-glossary.md) dan tata kelola di [GOVERNANCE.md](GOVERNANCE.md).

## 1. Tiga jalur kontribusi

| Anda ingin… | Lakukan |
|---|---|
| Mengusulkan **masalah riset** baru | Buka Issue **Research Problem** → masuk `research-backlog` |
| Memulai/menjalankan **riset** | Ikuti alur gate di bawah (branch `research/gN-*`, PR gate review) |
| Memperbaiki **framework/template/dokumen** | Fork/branch `docs/<topik>`, PR ke `main`, review `@maintainers` |

## 2. Issue adalah unit riset

Pilih form yang sesuai di **New Issue**:

- **Research Problem** — masalah apa yang layak diteliti (cluster, domain, problem owner, potential dataset, maturity, related courses, potential output, priority).
- **Research Question** — RQ/hipotesis yang perlu diuji, terkait Research ID.
- **Dataset** — dataset tersedia/dibutuhkan; nanti dicatat di `datasets-registry/`.
- **Experiment** — eksperimen/pilot yang akan dijalankan (hipotesis, baseline, metrik).
- **Literature Gap** — gap dari evidence map.
- **Publication** — naskah yang disiapkan (venue, status).
- **Research Risk** — bottleneck.
- **Bug** — kesalahan pada kode/dokumen/template.

Selalu cantumkan **Research ID** (`UIAI-YYYY-NNN`) di judul bila sudah ada: `[UIAI-2026-001] Judul`. Riset baru mendapat ID resmi saat lolos G2 (Problem Ready); sebelum itu pakai `UIAI-YYYY-TBD`.

## 3. Alur riset lewat gate

```
Issue (type:problem) ──G1──G2──> repo proj-YYYY-topic ──G3──G4──G5──> pilot ──G6──G7──> Research Pack ──G8──> TA / paper / artefak
```

1. **Buat repositori riset** dari [template repositori riset (TPL-15)](research-os/08-templates/15-research-repository-template.md): `README.md` riset, `docs/`, `data/README.md`, `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `paper/`, `presentation/`, `CITATION.cff`, `LICENSE`, `CHANGELOG.md`.
2. **Bekerja di branch gate**: `research/g2-problem`, `research/g3-evidence`, `research/g4-question`, `research/g5-method`, `research/g6-experiment`, `research/g7-claim`, `research/g8-contribution`.
3. **Buka PR `GATE REVIEW: <Nama Gate>`** memakai template yang sesuai (pilih lewat `?template=` atau salin dari `.github/PULL_REQUEST_TEMPLATE/`):
   - `problem-review.md` (G2), `evidence-review.md` (G3), `method-review.md` (G5), `experiment-review.md` (G6), `manuscript-review.md` (G8), `release-review.md` (rilis artefak/publikasi). G1, G4, G7 memakai template default.
   - Isi seluruh field: RQ, method, dataset, baseline, metrics, threats to validity, evidence, AI usage.
4. **Reviewer** (dosen, mentor, peer) memeriksa terhadap *definition of done* di [OPS-03 Research Gates](research-os/06-execution-os/03-research-gates.md). Komentar review = bukti proses ilmiah; simpan, jangan hapus.
5. **Merge = gate lulus.** Perbarui label `gate:*`, field Mission Control, dan bagian *Current Research Gate* di README riset. Buat **Release** sesuai milestone (`v0.1` … `v2.0`).
6. **Handoff** saat berpindah tahap (Course → Metopen → TA → AI Center) memakai [TPL-14](research-os/08-templates/14-research-handoff-template.md).

Riset tidak lahir sekali jadi; ia direvisi berdasarkan review. PR yang ditolak adalah bagian normal dari proses.

## 4. Aturan integritas (wajib)

- Tidak ada fabrikasi/falsifikasi data, tidak ada plagiarisme, tidak ada sitasi yang tidak dibaca atau tidak dapat diverifikasi.
- Setiap penggunaan AI yang memengaruhi kesimpulan (desain, pemilihan data, kode, analisis, penulisan) dicatat di **AI Usage Log** ([TPL-10](research-os/08-templates/10-ai-usage-log-template.md)) dan diungkap di `docs/AI-USAGE.md`; ikuti [AI Research Protocol (AIX-04)](research-os/05-ai-augmented-research/04-ai-research-protocol.md).
- Data pribadi/sensitif tidak pernah di-commit ([SECURITY.md](SECURITY.md)). Dataset didaftarkan sebagai **metadata** di `datasets-registry/`.
- Sebelum defense/submission, isi [Research Integrity Checklist (TPL-11)](research-os/08-templates/11-research-integrity-checklist.md).

## 5. Konvensi teknis

- **Commit**: kalimat imperatif singkat, sebutkan Research ID/Task ID bila relevan: `Add synthesis matrix v1 (UIAI-2026-003, OPS-031)`.
- **Markdown**: heading berjenjang, tabel untuk data terstruktur, link relatif.
- **Kode**: sertakan `requirements.txt`/`environment.yml`, seed tetap, skrip `run.sh`/`Makefile` untuk mereproduksi hasil.
- **Lisensi**: ikuti [LICENSING.md](LICENSING.md) — Apache-2.0 untuk kode, CC BY 4.0 untuk dokumen; dataset dan aset ber-HKI diputuskan lewat review.
- **Dokumen research-os**: pertahankan blok metadata (ID, paket, tier, status, audiens, terkait). Ubah `research-wbs.csv` lalu jalankan `python3 tools/build_wbs.py` dan `python3 tools/sync_weeks.py` (tabel task halaman mingguan studio juga dirender dari CSV); jangan mengedit `01-research-wbs-master.md` langsung.

## 6. Sebelum membuka PR ke `main` repo ini

```bash
python3 tools/check_links.py
python3 tools/build_wbs.py --check
python3 tools/sync_weeks.py --check
```

Ketiganya harus lulus. Workflow `docs-check` menjalankan hal yang sama di CI.

## 7. Pertanyaan

Buka Issue dengan label `question`-nya pada form yang paling dekat, atau hubungi `@maintainers`. Untuk bergabung sebagai mahasiswa peneliti, baca [Student Guide](research-based-learning/student-guide/README.md); untuk dosen, [Faculty Guide](research-based-learning/faculty-guide/README.md).
