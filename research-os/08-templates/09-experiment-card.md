# Experiment Card

> **ID** TPL-09 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen/TA, mentor, peer reproducer, reviewer G5–G7
> **Terkait** [OPS-03 G5–G7](../06-execution-os/03-research-gates.md) · [TPL-08 Research Design Card](08-research-design-card.md) · [TPL-10 AI Usage Log](10-ai-usage-log-template.md) · [TPL-15 Repository Template](15-research-repository-template.md) · [MST-03 Glossary §5 (Baseline, Leakage)](../00-master/03-glossary.md)

## Cara pakai

Satu kartu per eksperimen (pilot maupun eksperimen utama), diisi **sebelum** eksperimen dijalankan dan dilengkapi **setelah** hasil ada. Disimpan sebagai `experiments/EXP-NN-<slug>.md` di repositori riset dan dirujuk dari `experiments/README.md`. Kartu pilot pertama adalah bukti wajib G5 Method Ready (bersama Design Card); kartu dengan hasil aktual dan keputusan adalah bukti G6 Experiment Ready; kumpulan kartu menjadi dasar analisis G7 Claim Ready. Bagian *pra-registrasi* (hipotesis, metrik, stopping rule) tidak boleh diubah setelah run; bila berubah, buat kartu baru dan catat alasannya. Eksperimen tidak boleh dimulai bila baseline dan metrik masih kosong.

## Template (salin ke `experiments/EXP-NN-<slug>.md`)

```markdown
# EXP-[NN] — [nama eksperimen] · [Research ID] · [YYYY-MM-DD]

## Pra-registrasi (diisi sebelum run; jangan diubah)
| Bagian | Isi |
|---|---|
| RQ yang dijawab | [RQ1/RQ2] |
| Hypothesis | H: [prediksi yang dapat salah] · Null: [apa yang terjadi bila H salah] |
| Baseline | [pembanding paling sederhana yang masuk akal + cara implementasi] |
| Variables | Independen: [...] · Dependen: [...] · Kontrol: [...] |
| Dataset | [Dataset ID / nama; ukuran] · Split: [train/val/test atau pilot/eval; proporsi; cara membagi] · Leakage prevention: [apa yang dipastikan tidak bocor; pembagian per entitas/waktu; tuning hanya di val] |
| Metric | Utama: [nama + rumus/implementasi] · Sekunder: [...] · Ambang praktis: [ditetapkan sekarang] |
| Controls | [yang dijaga sama antar kondisi: prompt, versi model, hyperparameter, jumlah run] |
| Expected result | [angka/arah yang diharapkan + alasan] |
| Threats | [ancaman spesifik eksperimen ini + mitigasi] |
| Seed / config / environment | Seed: [...] · Config: `experiments/config-[nn].yaml` · Env: `requirements.txt` / `environment.yml` · Hardware: [...] |
| Compute budget | [jam GPU/CPU, biaya API, batas maksimum] |
| Stopping rule | [kapan berhenti: n run selesai / budget habis / hasil di luar rentang X → hentikan dan evaluasi ulang] |
| Peer reproducer | [nama] — target tanggal [YYYY-MM-DD] |

## Hasil aktual (diisi setelah run)
| Bagian | Isi |
|---|---|
| Tanggal run & commit | [YYYY-MM-DD] · `[hash]` |
| Hasil | [tabel metrik per kondisi, mean ± sd/interval, n run] — lihat `results/[file]` |
| Penyimpangan dari rencana | [apa yang berbeda dari pra-registrasi dan mengapa] |
| Error analysis | [pola kesalahan utama, contoh] |
| Reproduksi peer | [berhasil/gagal; angka yang didapat; tanggal] |
| AI assistance | [entri AI Usage Log terkait: #n] |

## Keputusan
[Lanjut ke eksperimen utama / ubah desain (apa) / hentikan (alasan)] — disetujui [mentor], [YYYY-MM-DD]
```

## Contoh terisi

**EXP-01 — Pilot: validitas rekomendasi LLM+RAG vs rule-based · UIAI-2026-001 · 2026-10-[dd]**

| Bagian | Isi |
|---|---|
| RQ yang dijawab | RQ1 |
| Hypothesis | H1: constraint-violation rate LLM+RAG ≤ rule-based pada 40 kasus pilot · Null: LLM+RAG melanggar prasyarat/SKS sama sering atau lebih sering |
| Baseline | Rule-based prerequisite checker + heuristik greedy (isi SKS maksimum dari mata kuliah wajib yang prasyaratnya terpenuhi, lalu elektif urut kode) — `src/baseline/` |
| Variables | Independen: sistem {baseline, LLM+RAG} · Dependen: violation rate, precision@5 · Kontrol: kurikulum v[isi], kasus identik, temperature 0, k = 5 |
| Dataset | 40 kasus advising sintetis (`data/sample-synthetic.csv`, dibuat dari distribusi DS-2026-001 tanpa record asli) · Split: 40 kasus semuanya pilot; 80 kasus nyata disimpan untuk evaluasi dan tidak disentuh · Leakage prevention: dokumen kurikulum masuk RAG, tetapi tidak ada kasus/gold label dalam konteks prompt; prompt tidak di-tune pada kasus pilot yang sama dengan yang dilaporkan |
| Metric | Utama: violation rate = pelanggaran prasyarat/SKS ÷ total rekomendasi (`src/eval/constraints.py`) · Sekunder: precision@5 relevansi elektif vs gold 2 dosen wali · Ambang praktis: selisih ≥ 10 poin persen |
| Controls | Prompt v3 dibekukan; model [nama, versi] dicatat; 3 run per kasus; baseline deterministik 1 run |
| Expected result | Baseline 0 % pelanggaran (by construction) tetapi precision rendah; LLM+RAG ≤ 10 % pelanggaran dengan precision lebih tinggi |
| Threats | LLM menebak kode mata kuliah → validasi terhadap daftar resmi; kasus sintetis terlalu mudah → cek distribusi vs data nyata |
| Seed / config / environment | Seed 42 · `experiments/config-01.yaml` · `requirements.txt` (Python 3.11) · CPU laptop + API LLM |
| Compute budget | ≤ Rp [isi] biaya API; ≤ 4 jam kerja mesin |
| Stopping rule | Berhenti setelah 40 kasus × 3 run; bila > 30 % output tidak dapat diparsing, hentikan dan perbaiki format sebelum melanjutkan |
| Peer reproducer | [Mahasiswa C] — 2026-10-[dd] |

| Hasil aktual | Isi |
|---|---|
| Tanggal run & commit | 2026-10-[dd] · `[hash]` |
| Hasil | Baseline: violation 0,0 %, precision@5 0,31 · LLM+RAG: violation 7,5 % ± 2,1 (3 run), precision@5 0,58 ± 0,04 — `results/exp-01.csv` |
| Penyimpangan dari rencana | 2 kasus dibuang karena kode mata kuliah tidak ada di kurikulum v[isi] (n = 38) |
| Error analysis | Pelanggaran terbanyak: melebihi batas SKS saat IPK rendah (5 dari 9 pelanggaran) |
| Reproduksi peer | Berhasil; violation 7,9 %, precision 0,57; 2026-10-[dd] |
| AI assistance | AI Usage Log #7 (debugging parser), #9 (kritik desain prompt) |

**Keputusan:** lanjut ke EXP-02 (80 kasus nyata) dengan tambahan post-check aturan SKS pada output LLM; H1 belum terdukung (LLM masih melanggar), H2 terindikasi — disetujui [Dosen C3], 2026-10-[dd].

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Pra-registrasi | Hipotesis, metrik, ambang, stopping rule ditulis sebelum run dan tidak berubah | Metrik dipilih setelah melihat hasil |
| Baseline | Sederhana, terimplementasi, angkanya dilaporkan | "Dibandingkan dengan penelitian sebelumnya" tanpa menjalankan |
| Leakage | Cara pencegahan dijelaskan konkret | Tidak disebut |
| Reproducibility | Seed, config, environment, commit, peer reproducer | Hasil hanya di laptop |
| Hasil | Mean ± variasi, n run, penyimpangan dilaporkan | Satu angka terbaik |
| Keputusan | Eksplisit, termasuk hasil negatif | Kartu berhenti di hasil |
