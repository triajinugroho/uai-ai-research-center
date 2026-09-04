<!--
EXPERIMENT REVIEW — G6 Experiment Ready
Cara pakai: buka PR dari branch research/g6-experiment, tambahkan ?template=experiment-review.md pada URL
"Compare & pull request" (atau salin isi file ini ke deskripsi PR).
Judul PR : GATE REVIEW: Experiment Ready — UIAI-YYYY-NNN
Definition of done : research-os/06-execution-os/03-research-gates.md bagian G6 (OPS-03)
Minggu/Sprint : W9–W10 / S9–S10 · Release milestone setelah merge : v0.5 Pilot Experiment
Reviewer : dosen pengampu + peer reproducer. Merge = gate lulus.
Hasil yang hanya ada di laptop anggota tim = gate gagal.
-->

# GATE REVIEW: Experiment Ready — `UIAI-YYYY-NNN`

| Field | Isi |
|---|---|
| **Research ID** | `UIAI-YYYY-NNN` |
| **Gate** | G6 Experiment Ready |
| **G5 Method Ready lulus (PR #)** | # |
| **Branch** | `research/g6-experiment` |
| **Tim / Mentor** | @ / @ |
| **Issue Experiment terkait** | # |

## Research Question
<!-- RQ/hipotesis yang diuji pilot ini. -->

## Method (ringkas, sesuai Design Card yang lolos G5)

## Dataset & split
| Unsur | Isi |
|---|---|
| Dataset ID | |
| Subset pilot (ukuran, cara memilih) | |
| Split train/val/test atau CV | |
| Pencegahan leakage | |

## Baseline & metode pembanding
| Sistem | Deskripsi | Konfigurasi / seed |
|---|---|---|
| Baseline | | |
| Metode 1 | | |

## Metrics & hasil pilot
<!-- Angka mentah + variansi antar seed/fold bila ada. Baseline harus terlihat. Ini pilot: tujuannya membuktikan desain viable, bukan klaim final. -->
| Sistem | Metrik utama | Metrik sekunder | Seed / n run |
|---|---|---|---|
| Baseline | | | |
| Metode 1 | | | |

## Threats to Validity (diperbarui dari pengalaman pilot)

## Struktur repositori & reproducibility
| Unsur | Path | Status |
|---|---|---|
| `src/` | | |
| `notebooks/` (output dibersihkan dari data pribadi) | | |
| `experiments/` (config, seed) | | |
| `experiments/README.md` (cara menjalankan) | | |
| `requirements.txt` / `environment.yml` | | |
| `run.sh` / `Makefile` | | |
| `results/` (log & hasil awal) | | |
| `figures/` | | |

## Catatan reproduksi oleh peer
<!-- Minimal satu reproduksi oleh anggota lain / peer di mesin berbeda. -->
| Reproducer | Tanggal | Commit yang direproduksi | Angka baseline cocok? (selisih) | Masalah yang ditemui |
|---|---|---|---|---|
| @ | | | | |

## Evidence
| Bukti wajib G6 (OPS-03) | Link / path | Status |
|---|---|---|
| Commit eksperimen | | |
| `experiments/README.md` | | |
| Hasil pilot (`results/`) | | |
| Catatan reproduksi peer | | |
| AI Usage Log untuk kode yang dibantu AI | | |

## AI Usage
- Bagian kode yang dibantu AI (file/fungsi) dan cara memverifikasinya (tes, pembacaan ulang, pembanding manual):
- Link AI Usage Log (TPL-10) / `AI-USAGE.md`:

## Definition of Done — G6 Experiment Ready (OPS-03)
- [ ] Repositori berisi `src/`, `notebooks/`, `experiments/` dengan konfigurasi, seed, environment, dan README cara menjalankan
- [ ] **Pilot / minimum viable experiment** berjalan end-to-end pada subset data: baseline + minimal satu metode pembanding
- [ ] Log eksperimen dan hasil awal tersimpan di `results/`; figur di `figures/`
- [ ] Reproduksi oleh anggota lain / peer berhasil (minimal satu kali) dan dicatat
- [ ] Metrik & baseline **tidak berubah** dari yang ditetapkan di G5 (bila berubah, jelaskan mengapa dan minta persetujuan mentor)

## Checklist integritas
- [ ] Tidak ada data mentah sensitif, data pribadi, kredensial, atau output notebook yang bocor di commit
- [ ] Hasil dilaporkan apa adanya, termasuk yang tidak sesuai harapan
- [ ] Kode yang dibantu AI diungkap di AI Usage Log

## Untuk reviewer — peer reproducer
<!-- Peer reproducer menjalankan ulang baseline dari repositori mengikuti README, tanpa bertanya ke tim. -->
- Perintah yang dijalankan:
- Angka yang diperoleh vs angka di PR:
- Langkah README yang tidak jelas:

**Lulus jika** peer dapat mereproduksi angka baseline dari repositori.
**Gagal jika** hasil hanya ada di laptop anggota tim.

## Reviewer yang diminta
- [ ] Dosen pengampu Metopen: @
- [ ] Peer reproducer: @

## Setelah merge
- [ ] Label Issue → `gate:G6-experiment`; maturity → `maturity:research-ready` (setelah G7); field Mission Control diperbarui
- [ ] Release `v0.5 Pilot Experiment`

## Catatan untuk reviewer
