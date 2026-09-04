<!--
EVIDENCE REVIEW — G3 Evidence Ready
Cara pakai: buka PR dari branch research/g3-evidence, tambahkan ?template=evidence-review.md pada URL
"Compare & pull request" (atau salin isi file ini ke deskripsi PR).
Judul PR : GATE REVIEW: Evidence Ready — UIAI-YYYY-NNN
Definition of done : research-os/06-execution-os/03-research-gates.md bagian G3 (OPS-03)
Minggu/Sprint : W3–W5 / S3–S5 · Release milestone setelah merge : v0.2 Evidence Ready
Reviewer : dosen pengampu + peer reviewer; mentor bila sudah ada. Merge = gate lulus.
Satu referensi yang tidak dapat diverifikasi = gate gagal.
-->

# GATE REVIEW: Evidence Ready — `UIAI-YYYY-NNN`

| Field | Isi |
|---|---|
| **Research ID** | `UIAI-YYYY-NNN` |
| **Gate** | G3 Evidence Ready |
| **G2 Problem Ready lulus (PR #)** | # |
| **Branch** | `research/g3-evidence` |
| **Tim / Mentor** | @ / @ |
| **Issue Literature Gap terkait** | # |

## Strategi pencarian (search strategy)
| Unsur | Isi |
|---|---|
| Kata kunci & kombinasi | |
| Basis data (Google Scholar / Scopus / Semantic Scholar / lainnya) | |
| Citation chaining (backward/forward) | |
| Kriteria inklusi / eksklusi | |
| Kriteria kualitas sumber (peer-reviewed, venue, tahun, primer/sekunder) | |
| Rentang tahun | |

## Literature Evidence Map — ringkasan angka
| Ukuran | Nilai |
|---|---|
| Kandidat sumber ditemukan | |
| Sumber primer relevan yang **benar-benar dibaca** (target 15–25) | |
| Sumber yang ditemukan lewat AI | |
| Sumber yang **tidak dapat diverifikasi** (harus 0) | |

## Synthesis matrix
<!-- Link ke docs/literature-map.md + matriks (tabel/CSV). Kolom minimum: problem, metode, data, metrik, hasil, keterbatasan, relevansi. -->
- Link matriks:
- Kolom yang dipakai:

## Pola yang terlihat dari matriks
<!-- Inilah inti G3: matriks harus menunjukkan pola, bukan ringkasan paper satu per satu. -->
- **Konsisten** (apa yang disepakati literatur):
- **Bertentangan** (hasil yang saling berlawanan, dan dugaan penyebabnya):
- **Belum diuji** (konteks, data, metode, perbandingan yang kosong):

## Kandidat gap (untuk G4)
<!-- Rujuk baris matriks. Belum harus final. -->

## Evidence
| Bukti wajib G3 (OPS-03) | Link / path | Status |
|---|---|---|
| `docs/literature-map.md` | | |
| Synthesis matrix (tabel/CSV) | | |
| `references.bib` terkelola | | |
| AI Usage Log menunjukkan verifikasi sumber | | |

## AI Usage
- AI dipakai untuk (kandidat keyword, literature intelligence, ringkasan awal, …):
- Cara verifikasi sumber dari AI (DOI/URL dibuka, abstrak dibaca, dicocokkan dengan versi publisher):
- Link AI Usage Log (TPL-10):

## Definition of Done — G3 Evidence Ready (OPS-03)
- [ ] Strategi pencarian terdokumentasi (kata kunci, basis data, citation chaining, inklusi/eksklusi, kualitas sumber)
- [ ] **Literature Evidence Map**: minimal 15–25 sumber primer relevan yang benar-benar dibaca
- [ ] Sumber dipetakan dalam **synthesis matrix** (problem, metode, data, metrik, hasil, keterbatasan, relevansi), bukan ringkasan satu per satu
- [ ] Setiap sumber terverifikasi ada (DOI/URL), termasuk sumber yang ditemukan lewat AI
- [ ] `references.bib` terkelola dan konsisten dengan matriks
- [ ] Matriks menunjukkan pola: konsisten / bertentangan / belum diuji

## Checklist integritas
- [ ] Tidak ada sumber yang dikutip tanpa dibaca
- [ ] Tidak ada referensi hasil karangan AI (semua dicek ke DOI/URL asli)
- [ ] Kutipan/parafrase ditandai sumbernya (tidak ada plagiarisme)

## Untuk reviewer — uji sampel referensi
<!-- Reviewer memilih acak 3–5 entri references.bib, membuka DOI/URL, dan mencocokkan dengan baris matriks. -->
| Entri yang diuji | DOI/URL dibuka? | Sesuai isi matriks? | Catatan |
|---|---|---|---|
| | | | |

**Lulus jika** matriks menunjukkan pola (apa yang konsisten, bertentangan, belum diuji).
**Gagal jika** ada satu saja referensi yang tidak dapat diverifikasi keberadaannya.

## Reviewer yang diminta
- [ ] Dosen pengampu Metopen: @
- [ ] Peer reviewer: @
- [ ] Mentor (bila sudah ada): @

## Setelah merge
- [ ] Label Issue → `gate:G3-evidence`; field Mission Control diperbarui
- [ ] Release `v0.2 Evidence Ready`
- [ ] Buka Issue **Literature Gap** untuk setiap gap yang akan dibawa ke G4

## Catatan untuk reviewer
