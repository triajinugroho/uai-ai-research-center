<!--
RELEASE REVIEW — rilis artefak / dataset / publikasi / Research Pack (tag v0.1–v2.0)
Cara pakai: buka PR yang menyiapkan rilis (CHANGELOG, CITATION, README lisensi, registry), tambahkan
?template=release-review.md pada URL "Compare & pull request" (atau salin isi file ini ke deskripsi PR).
Judul PR : RELEASE REVIEW: <tag> <milestone> — <Research ID>   contoh: RELEASE REVIEW: v1.0 Research Pack — UIAI-2026-003
Kebijakan : LICENSING.md (lisensi per komponen, IP review), SECURITY.md (tidak ada data sensitif),
            GOVERNANCE.md §6.3 (release = milestone riset), CHANGELOG.md, CITATION.cff.
Reviewer : @maintainers / pengelola registry; @directors untuk IP review bila ada potensi HKI/komersialisasi.
Merge = rilis boleh dibuat (tag + GitHub Release).
-->

# RELEASE REVIEW: `vX.Y <milestone>` — `UIAI-YYYY-NNN`

| Field | Isi |
|---|---|
| **Research ID** | `UIAI-YYYY-NNN` |
| **Release tag** | v0.1 Problem Validated / v0.2 Evidence Ready / v0.3 Research Design / v0.5 Pilot Experiment / v0.8 Manuscript Draft / v1.0 Research Pack / v1.1 Submitted / v2.0 Published |
| **Gate yang mendasari (PR #)** | # |
| **Jenis yang dirilis** | Research Pack / Artifact `ART-YYYY-NNN` / Dataset `DS-YYYY-NNN` (metadata) / Publication `PUB-YYYY-NNN` / kombinasi |
| **Repositori** | `proj-YYYY-<topik>` |
| **Visibilitas setelah rilis** | INTERNAL → PUBLIC / tetap INTERNAL |

## Apa yang dirilis
<!-- Ringkasan isi rilis, commit/tag yang akan dibuat, dan apa yang TIDAK dirilis (mis. model weights, data mentah). -->

## Lisensi per komponen (LICENSING.md §5)
| Komponen | Lisensi | File / catatan |
|---|---|---|
| Code | Apache-2.0 / GPL-3.0 / — | `LICENSE` |
| Documentation | CC-BY-4.0 / CC-BY-SA-4.0 | `LICENSE-DOCS` |
| Dataset | CC-BY-4.0 / CC0 / restricted / tidak dirilis | kartu `DS-YYYY-NNN`, hasil data governance review |
| Model weights | research-only / not released | |
| Paper | publisher copyright (DOI) / preprint bila diizinkan | |
| Prototype / lainnya | | |

## IP review (LICENSING.md §6)
- [ ] Tidak ada potensi HKI/komersialisasi → boleh lisensi publik
- [ ] Ada potensi HKI/komersialisasi → **IP review** bersama `@directors` selesai; keputusan:
- Catatan IP review (tanggal, peserta, keputusan):

## Tidak ada data sensitif (SECURITY.md)
- [ ] Tidak ada data mentah RESTRICTED/Confidential, data pribadi (nama, NIM, email, dsb.), atau data partner di repositori **termasuk riwayat git**
- [ ] Output notebook dan log dibersihkan dari data pribadi
- [ ] Tidak ada kredensial (API key, token, `.env`, kunci) — hasil pemindaian:
- [ ] `.gitignore` mencakup `data/raw/`, `data/private/`, format model
- [ ] Model weights hasil pelatihan pada data sensitif tidak dirilis tanpa review

## Metadata rilis
- [ ] `CITATION.cff` diperbarui (judul, penulis, versi, tanggal, DOI/permalink bila ada)
- [ ] `CHANGELOG.md` memuat entri rilis ini (tag, tanggal, apa yang berubah)
- [ ] README riset: tabel lisensi per komponen, bagian *Current Research Gate*, cara sitasi
- [ ] `AI-USAGE.md` / AI Usage Statement tersedia
- [ ] Reproducibility README (kode, konfigurasi, seed, environment, langkah eksekusi, metadata data)

## Pembaruan registry (setelah merge)
| Registry | Entri | Status |
|---|---|---|
| `datasets-registry/REGISTRY.md` | DS-YYYY-NNN | |
| `publications/PUBLICATIONS.md` (publikasi / artefak) | PUB-YYYY-NNN / ART-YYYY-NNN | |
| `research-backlog/BACKLOG.md` (maturity) | UIAI-YYYY-NNN | |
| Mission Control (Status, Maturity, Publication Target) | | |

## Evidence
| Bukti | Link / path |
|---|---|
| PR gate yang mendasari rilis | # |
| Draft catatan rilis (release notes) | |
| Hasil pemindaian kredensial / data pribadi | |
| Notulen IP review (bila ada) | |

## Checklist integritas
- [ ] Klaim di release notes/README tidak melebihi bukti yang lolos G7/G8
- [ ] Atribusi lengkap: penulis, mentor, partner, dataset pihak ketiga, lisensi pustaka yang dipakai
- [ ] Penggunaan AI diungkap

## Reviewer yang diminta
- [ ] `@maintainers` / pengelola registry: @
- [ ] `@directors` (IP review, bila relevan): @
- [ ] Mentor: @

## Setelah merge
- [ ] Buat tag + GitHub Release `vX.Y` dengan release notes
- [ ] Perbarui registry sesuai tabel di atas; kolom **Published/Released** di Mission Control
- [ ] Bila visibilitas berubah ke PUBLIC: cek ulang seluruh riwayat git sebelum mengubah visibilitas

## Catatan untuk reviewer
