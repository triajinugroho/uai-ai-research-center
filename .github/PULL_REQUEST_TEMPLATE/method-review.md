<!--
METHOD REVIEW — G5 Method Ready (termasuk Mid-semester Research Pitch / Red Team Review, W8)
Cara pakai: buka PR dari branch research/g5-method, tambahkan ?template=method-review.md pada URL
"Compare & pull request" (atau salin isi file ini ke deskripsi PR).
Judul PR : GATE REVIEW: Method Ready — UIAI-YYYY-NNN
Definition of done : research-os/06-execution-os/03-research-gates.md bagian G5 (OPS-03)
Minggu/Sprint : W7–W8 / S7–S8 · Release milestone setelah merge : v0.3 Research Design
Reviewer : dosen pengampu, mentor, red team (peer + dosen lain). Merge = gate lulus.
Eksperimen TIDAK boleh dimulai sebelum metrik dan baseline ditetapkan.
-->

# GATE REVIEW: Method Ready — `UIAI-YYYY-NNN`

| Field | Isi |
|---|---|
| **Research ID** | `UIAI-YYYY-NNN` |
| **Gate** | G5 Method Ready |
| **G4 Question Ready lulus (PR #)** | # |
| **Branch** | `research/g5-method` |
| **Tim / Mentor** | @ / @ |
| **Issue Research Question / Experiment terkait** | # / # |

## Research Question
<!-- Salin RQ/hipotesis yang lolos G4, masing-masing dengan rujukan baris synthesis matrix. -->

## Method — Research Design Card (TPL-08)
| Unsur | Isi |
|---|---|
| Jenis metode (experiment / benchmarking / design science / empirical SE study / ML research / simulation / survey / user study / case study / qualitative) | |
| Variabel / konstruk | |
| Kontrol | |
| Sampling / unit analisis | |
| Prosedur ringkas (langkah 1 → n) | |
| Link Research Design Card | |

## Dataset — Data Plan
| Unsur | Isi |
|---|---|
| Dataset ID (DS-YYYY-NNN) / status registry | |
| Sumber & akses | |
| Lisensi | |
| Privasi (Public / Restricted / Confidential) | |
| Ukuran & representativitas terhadap populasi | |
| Rencana bila data tidak tersedia (fallback) | |

## Baseline
<!-- Baseline paling sederhana yang masuk akal + minimal satu pembanding. Mengapa baseline ini adil? -->

## Metrics
| Metrik | Selaras dengan RQ mana | Prosedur evaluasi (split / CV / pencegahan leakage) | Ambang "berarti secara praktis" |
|---|---|---|---|
| | | | |

## Experiment Card untuk pilot (TPL-09)
- Link Experiment Card:
- Subset data untuk pilot:
- Seed / config / environment:

## Threats to Validity (awal)
| Jenis | Ancaman | Rencana mitigasi |
|---|---|---|
| Internal | | |
| Eksternal | | |
| Konstruk | | |
| Statistik / kesimpulan | | |

## Ethics & Privacy (awal, MET-07)
<!-- Data manusia? consent? komite etik? anonimisasi? prompt ke AI eksternal tidak memuat data pribadi/partner. Versi lengkap di docs/ethics.md. -->

## Mid-semester Research Pitch / Red Team Review (W8)
| Unsur | Link / isi |
|---|---|
| Slide pitch | |
| Notulen red team (keberatan utama + tanggapan) | |
| Perubahan desain akibat red team | |

## Evidence
| Bukti wajib G5 (OPS-03) | Link / path | Status |
|---|---|---|
| `docs/research-design.md` | | |
| Research Design Card (TPL-08) | | |
| Experiment Card (TPL-09) | | |
| `docs/ethics.md` | | |
| Slide pitch | | |
| Notulen red team | | |
| Kartu dataset di `datasets-registry/` (bila dataset baru) | | |

## AI Usage
- AI dipakai untuk (mengkritik desain, alternatif hipotesis, penjelasan statistik, …):
- Bagaimana keluaran AI diverifikasi:
- Link AI Usage Log (TPL-10):

## Definition of Done — G5 Method Ready (OPS-03)
- [ ] **Research Design Card** (TPL-08): jenis metode, variabel/konstruk, kontrol, sampling
- [ ] **Dataset/Data Plan**: sumber, akses, lisensi, privasi, ukuran, representativitas; dicatat di datasets-registry bila baru
- [ ] **Baseline & Metrics**: baseline paling sederhana, metrik selaras RQ, prosedur evaluasi yang mencegah leakage
- [ ] **Experiment Card** (TPL-09) untuk pilot
- [ ] **Threats to Validity** awal (internal, eksternal, konstruk, statistik)
- [ ] **Ethics & Privacy** awal (MET-07); privasi dataset terisi sebelum gate ini
- [ ] Dipertahankan pada **Mid-semester Research Pitch / Red Team Review** (W8)

## Checklist integritas
- [ ] Metrik ditetapkan **sebelum** melihat hasil (tidak akan diganti setelah eksperimen)
- [ ] Tidak ada data mentah/pribadi/kredensial di commit
- [ ] Penggunaan AI dicatat di AI Usage Log

## Untuk reviewer — uji "bisa dijalankan orang lain"
<!-- Reviewer mencoba menjelaskan prosedur eksperimen dari dokumen saja. Bagian mana yang masih harus ditanyakan ke tim? -->
- Pertanyaan yang masih harus ditanyakan ke tim:

**Lulus jika** orang lain dapat menjalankan desain ini tanpa bertanya ke tim.
**Gagal jika** metrik/baseline belum ditetapkan.

## Reviewer yang diminta
- [ ] Dosen pengampu Metopen: @
- [ ] Mentor: @
- [ ] Red team (peer + dosen lain): @ @

## Setelah merge
- [ ] Label Issue → `gate:G5-method`; maturity → `maturity:ta-ready`; field Mission Control diperbarui
- [ ] Release `v0.3 Research Design`
- [ ] Buka Issue **Experiment** untuk pilot (G6)

## Catatan untuk reviewer
