# Publications — Registry Metadata Publikasi & Artefak (bukan arsip PDF)

> **Status** Draft v0.1 (2026-09) · **Terkait** [MST-03 Glossary](../research-os/00-master/03-glossary.md) · [MET-05 Publication Backward Design](../research-os/04-metopen-research-studio/05-publication-backward-design.md) · [TPL-06 Publication Venue Registry](../research-os/08-templates/06-publication-venue-registry-template.md) · [TPL-11 Research Integrity Checklist](../research-os/08-templates/11-research-integrity-checklist.md) · [LICENSING.md](../LICENSING.md) · [GOVERNANCE.md](../GOVERNANCE.md)

Folder ini adalah **database metadata karya ilmiah** UAI AI Research Center: paper, dataset paper, artefak (software/model/benchmark/prototype), dan HKI. Ia membuat hubungan **project → evidence → manuscript → publication** tetap dapat ditelusuri. Ia **bukan** tempat menyimpan PDF penerbit.

## 1. Fungsi

| Fungsi | Cara |
|---|---|
| Institutional memory | setiap karya tercatat dengan `PUB-YYYY-NNN`/`ART-YYYY-NNN` dan terhubung ke Research ID |
| Traceability | kartu publikasi menunjuk ke dataset (`DS-*`), artefak (`ART-*`), kode, dan Research Pack yang menjadi buktinya |
| Pipeline publikasi | status Draft → Submitted → Under Review → Accepted → Published tampak di satu tabel dan di view *Publication Pipeline* Mission Control |
| Pelaporan | bahan BKD, akreditasi, PP-PTS, dan Faculty Portfolio ([GOV-05](../research-os/07-governance/05-ppts-and-institutional-evidence.md)) |
| Integritas | AI Usage Statement, checklist integritas, dan status etika venue tercatat bersama karya |

## 2. Aturan

1. **Metadata, DOI, sitasi** — yang disimpan adalah metadata lengkap, DOI/URL resmi, dan sitasi (BibTeX di kartu). Ini selalu aman.
2. **PDF penerbit tidak disimpan** di repo ini maupun repo `proj-*`, kecuali lisensi penerbit secara eksplisit mengizinkan (mis. open access CC BY — tetap cukup tautkan DOI).
3. **Preprint hanya jika hak mengizinkan** — cek kebijakan penerbit/venue sebelum mengunggah ke server preprint; catat tautan preprint di kartu, bukan filenya.
4. **Lisensi naskah mengikuti penerbit** ([LICENSING.md](../LICENSING.md)); kartu mencatat status hak cipta.
5. **Venue harus ada di venue registry** ([TPL-06](../research-os/08-templates/06-publication-venue-registry-template.md)) dengan status etika publikasi yang jelas — tidak ada submission ke venue yang tidak dikenal/predator.
6. **AI Usage Statement** wajib di setiap kartu, mengikuti [AIX-04](../research-os/05-ai-augmented-research/04-ai-research-protocol.md) dan kebijakan venue.
7. **Research Integrity Checklist** ([TPL-11](../research-os/08-templates/11-research-integrity-checklist.md)) ditandatangani sebelum status *Submitted*.
8. Penulis mahasiswa dan dosen dicantumkan dengan kontribusi **CRediT** ringkas; urutan penulis disepakati sebelum submission.

## 3. Alur PUB ID

```
Issue "Publication" (type:publication)  ──►  PUB-YYYY-NNN  ──►  baris di PUBLICATIONS.md
        (venue, target, Research ID)         (pengelola publications)        │
                                                                             ▼
                                              kartu YYYY/PUB-YYYY-NNN-slug.md dari _template/publication-card.md
```

| Langkah | Siapa | Kapan |
|---|---|---|
| Buka Issue **Publication** dengan Research ID, venue target, jenis kontribusi, penulis | tim riset | saat naskah mulai disiapkan (*manuscript-ready*, biasanya setelah G8 atau saat G7 untuk endgame paper) |
| Beri `PUB-YYYY-NNN` (tahun = tahun Issue dibuka; tidak dipakai ulang) | pengelola publications (`@maintainers`) | ≤7 hari |
| Tambah baris di [PUBLICATIONS.md](PUBLICATIONS.md) + kartu di folder tahun | tim riset via PR | bersamaan |
| Perbarui status setiap perubahan (submitted, review, accepted, published, DOI) | tim riset | ≤7 hari setelah perubahan |
| Setelah *Published*: lengkapi DOI, sitasi, lisensi, tautan artefak/dataset; Research ID naik ke **Published/Released** | tim + pengelola | ≤14 hari |

Sebelum PUB ID diberikan, naskah cukup dilacak sebagai release `v0.8 Manuscript Draft` di repo riset.

## 4. Status pipeline

| Status | Arti | Bukti |
|---|---|---|
| **Draft** | naskah ditulis; manuscript-ready → submission-ready ([MET-05](../research-os/04-metopen-research-studio/05-publication-backward-design.md)) | Issue Publication, kartu |
| **Submitted** | dikirim ke venue; checklist integritas lengkap | tanggal submission; release `v1.1 Submitted` |
| **Under Review** | menunggu/merevisi berdasarkan review | ringkasan komentar reviewer di kartu |
| **Accepted** | diterima; menunggu terbit | surat/notifikasi (tidak diunggah; cukup tanggal) |
| **Published** | terbit; DOI ada | DOI; release `v2.0 Published` |
| **Rejected / Withdrawn** | ditolak/ditarik; kartu tetap ada, dicatat venue berikutnya | catatan di kartu |

Kematangan riset padanannya: *Publication Ready* saat Draft/Submitted; *Impact Ready* bila karya berubah menjadi HKI/prototype/solusi.

## 5. Knowledge graph sederhana

Satu Research ID mengikat semua keluaran (dokumen sumber):

```
UIAI-2026-023
│
├─ Dataset      DS-2026-014
│
├─ Artifact     ART-2026-008
│
└─ Publication  PUB-2027-001
```

Aturan tautan:

- Kartu publikasi wajib menyebut **Research Project** (`UIAI-*`), **Dataset** (`DS-*` atau "none"), **Artifact** (`ART-*` atau "none"), dan **Code** (repo/commit/release).
- Kartu dataset ([datasets-registry](../datasets-registry/README.md)) dan README riset menyebut balik `PUB-*` setelah terbit.
- Dengan itu setiap klaim dalam paper dapat ditelusuri ke data, kode, dan eksperimen — *inspectable research artifact*, bukan sekadar dokumen akademik.

## 6. Artefak (ART ID) juga dicatat di sini

Artefak — software, model, benchmark, prototype — mendapat `ART-YYYY-NNN` dari pengelola publications/AI Center ([GOVERNANCE.md](../GOVERNANCE.md) §5) dan dicatat pada **tabel artefak** di [PUBLICATIONS.md](PUBLICATIONS.md). Syarat rilis:

| Syarat | Rujukan |
|---|---|
| Reproducibility package: kode, konfigurasi, seed, environment, langkah eksekusi, metadata data | [MST-03](../research-os/00-master/03-glossary.md), [TPL-15](../research-os/08-templates/15-research-repository-template.md) |
| Lisensi per komponen dinyatakan (code / docs / dataset / model weights) | [LICENSING.md](../LICENSING.md) §5 |
| IP review singkat bersama `@directors` bila ada potensi HKI/komersialisasi | [LICENSING.md](../LICENSING.md) §6 |
| Release Review PR (`.github/PULL_REQUEST_TEMPLATE/`) lulus | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Kriteria *documented, complete, executable/reusable* (semangat artifact badging ACM — sumber: dokumen diskusi) | [alignment/global.md](../research-roadmap/alignment/global.md) |

Artefak yang menyertai paper dirujuk dari kartu publikasi; artefak mandiri (tanpa paper) tetap mendapat ART ID.

## 7. Hubungan ke MET-05 dan TPL-06

- [MET-05 Publication Backward Design](../research-os/04-metopen-research-studio/05-publication-backward-design.md): target venue dipilih **backward** dari jenis kontribusi; milestone TA-ready → manuscript-ready → submission-ready → submitted → accepted → published. Registry ini adalah tempat milestone itu dicatat.
- [TPL-06 Publication Venue Registry](../research-os/08-templates/06-publication-venue-registry-template.md): daftar venue (scope, indexing, template, deadline, biaya, status etika, topik cocok). Tabel venue yang aktif dipelihara di bagian **Venue Registry** pada [PUBLICATIONS.md](PUBLICATIONS.md); kartu publikasi merujuk venue dari tabel itu, dan venue baru ditambahkan lewat PR sebelum submission.

## 8. Struktur folder dan ritme update

```
publications/
├── README.md                    ← halaman ini
├── PUBLICATIONS.md              ← indeks publikasi + tabel artefak + counter
├── _template/publication-card.md
├── 2026/README.md               ← satu file per publikasi: PUB-2026-NNN-slug.md
├── 2027/ … (dibuat saat ada PUB ID tahun itu)
```

| Ritme | Apa |
|---|---|
| Setiap perubahan status | perbarui kartu + baris indeks (≤7 hari) |
| Akhir sprint | pengelola cek konsistensi indeks vs kartu vs Mission Control |
| Akhir semester | ringkasan jumlah per status dan per klaster untuk [README](../README.md) utama dan Faculty Portfolio |
| Roadmap review tahunan | evaluasi venue (TPL-06), proporsi karya dengan artefak/dataset terbuka |

Otomasi pembaruan registry dari Issue/Release menyusul setelah alur manual stabil ([GOVERNANCE.md](../GOVERNANCE.md) §10).
