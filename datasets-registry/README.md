# Datasets Registry — Katalog & Tata Kelola Dataset (bukan penyimpanan)

> **Status** Draft v0.1 (2026-09) · **Terkait** [MST-03 Glossary](../research-os/00-master/03-glossary.md) · [TPL-05 Dataset Registry Template](../research-os/08-templates/05-dataset-registry-template.md) · [SECURITY.md](../SECURITY.md) · [LICENSING.md](../LICENSING.md) · [MET-07 Research Integrity & Ethics](../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [Research Backlog](../research-backlog/README.md)

Folder ini adalah **catalog and governance layer** untuk semua dataset yang dipakai riset UAI AI Research Center. Ia menyimpan **metadata** (kartu dataset), **bukan data**. Dataset fisik hidup di luar GitHub. Prinsip dari [SECURITY.md](../SECURITY.md): *data mentah yang sensitif tidak pernah otomatis masuk GitHub; GitHub hanya menyimpan metadata, kode, dan artefak yang aman.*

## 1. Mengapa registry, bukan menyimpan dataset di Git

| Alasan | Penjelasan |
|---|---|
| **Ukuran** | Dataset besar (citra, korpus, log) tidak cocok di Git; riwayat repo membengkak dan tidak dapat dibersihkan dengan mudah |
| **Privasi** | Data mahasiswa, kesehatan, partner, dan data pribadi tidak boleh berada di repo publik maupun privat tanpa kontrol akses yang tepat |
| **Lisensi** | Banyak dataset memiliki syarat redistribusi; menyalinnya ke GitHub dapat melanggar syarat itu |
| **Traceability** | Yang dibutuhkan riset adalah *tahu dataset apa yang ada, siapa pemiliknya, boleh dipakai untuk apa, dan di mana* — itu metadata |
| **Reuse** | Kartu dataset membuat research asset dapat ditemukan oleh riset berikutnya (*research assets should compound*) |

## 2. Lokasi fisik yang diperbolehkan

| Lokasi | Cocok untuk | Catatan |
|---|---|---|
| **Institutional server / storage UAI** | data Restricted/Confidential, data partner | kontrol akses oleh pengelola; `[isi: nama server/unit pengelola]` |
| **Hugging Face (dataset hub)** | dataset publik berlisensi jelas, korpus, benchmark | pakai organisasi UAI; kartu dataset di HF menyalin field dari sini |
| **Kaggle** | dataset publik, kompetisi internal | cek lisensi platform |
| **Google Drive / cloud storage institusional** | data Internal selama riset berjalan | tautan hanya di kartu; akses per orang; bukan untuk data Confidential tanpa enkripsi/izin |
| **Cloud object storage** | data besar, pipeline | biaya dan akses dikelola pengelola registry |
| **Lingkungan mitra** (analisis di tempat) | data klinis/partner yang tidak boleh dipindahkan | riset dijalankan di sisi mitra; hanya hasil agregat keluar |

Yang **tidak** diperbolehkan: data mentah di repo GitHub mana pun (termasuk `proj-*` privat), data pribadi di notebook output/log, data partner di prompt layanan AI eksternal.

## 3. Alur pendaftaran

```
Issue "Dataset" (type:dataset)  ──►  Review privasi & lisensi  ──►  Dataset ID DS-YYYY-NNN
                                      (pengelola registry;              │
                                       komite etik bila data manusia)    ▼
                                                        Kartu datasets/DS-YYYY-NNN-slug.md
                                                        + baris di REGISTRY.md (PR)
```

| Langkah | Siapa | Isi |
|---|---|---|
| 1. Issue Dataset | pengusul (mahasiswa/dosen/partner via pusat riset) | nama, sumber, pemilik, modalitas, ukuran perkiraan, lisensi yang diketahui, privasi yang diperkirakan, Research ID terkait |
| 2. Review privasi & lisensi | pengelola registry (`@maintainers`/pengelola yang ditunjuk) + komite etik untuk data manusia | ikuti decision tree dataset di [LICENSING.md](../LICENSING.md): ownership → privacy → consent → partner agreement → lisensi; tetapkan kelas `Public / Restricted / Confidential` |
| 3. Dataset ID | pengelola registry | `DS-YYYY-NNN` berurutan per tahun, tidak dipakai ulang |
| 4. Kartu + indeks | pengusul | buat `datasets/DS-YYYY-NNN-slug.md` dari [TPL-05](../research-os/08-templates/05-dataset-registry-template.md); tambah baris di [REGISTRY.md](REGISTRY.md); PR direview pengelola |
| 5. Pemakaian | tim riset | rujuk Dataset ID di Research One-Pager, Data Plan (`docs/data-plan.md`, G5), README riset, dan kartu publikasi |

Kartu wajib ada **sebelum G5 Method Ready** untuk setiap dataset yang dipakai riset ([OPS-03](../research-os/06-execution-os/03-research-gates.md)); field Privacy harus terisi ([SECURITY.md](../SECURITY.md) §4).

## 4. Aturan privasi dan lisensi

| Kelas privasi | Arti | Yang boleh di GitHub |
|---|---|---|
| **Public** | dapat dibagikan terbuka; tidak ada data pribadi; lisensi jelas | kartu + tautan unduh; sampel kecil bila lisensi mengizinkan |
| **Restricted** | data pribadi/mahasiswa/pengguna yang telah dianonimisasi/pseudonimisasi; atau data partner dengan akses terbatas | kartu saja; akses lewat pengelola; consent dan izin didokumentasikan di `docs/ethics.md` riset |
| **Confidential** | data klinis, data proses/bisnis partner rahasia, data komersial | kartu dengan deskripsi umum saja; lokasi hanya "lingkungan mitra/server institusi"; perjanjian tertulis |

Lisensi mengikuti [LICENSING.md](../LICENSING.md): dataset **tidak punya lisensi default**; dataset buatan UAI yang aman dibuka → CC BY 4.0 atau CC0; dataset dengan data pribadi/partner → **tidak ada lisensi publik**. Untuk dataset pihak ketiga, catat lisensi aslinya dan syarat redistribusi; jangan mengunggah ulang bila dilarang.

Praktik wajib untuk data manusia ([SECURITY.md](../SECURITY.md) §4, [MET-07](../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)): anonimisasi sebelum analisis, kunci pemetaan di luar repo, consent dan izin institusi terdokumentasi, prompt AI eksternal tanpa data pribadi.

## 5. Field kartu dataset

| Field | Isi |
|---|---|
| Dataset ID | `DS-YYYY-NNN` |
| Name | nama singkat |
| Domain | Education / Halal / Health / Food / Government / Business / Social Impact / General |
| Source | Public / UAI / Partner (+ URL/sumber) |
| Owner | pemilik/pengelola data `[isi]` |
| Size | jumlah record/citra/token, ukuran file `[isi]` |
| Modality | Text / Image / Tabular / Audio / Time series / Multimodal |
| License | lisensi asli atau lisensi yang ditetapkan; "no public license" bila Restricted/Confidential |
| Privacy | Public / Restricted / Confidential |
| Potential Task | classification, prediction, RAG, IE, QA, dst. |
| Related Projects | Research ID `UIAI-YYYY-NNN` yang memakai |
| Quality Notes | kelengkapan, bias, duplikasi, keterwakilan, versi |
| Access | cara meminta akses; siapa menyetujui |
| Possible Research Questions | 2–4 RQ yang mungkin |
| Physical Location | server/HF/Kaggle/Drive/cloud/mitra |
| Review Date | tanggal review privasi/lisensi terakhir |
| Status | draft / active / deprecated; "contoh ilustratif" untuk kartu contoh |

## 6. Ritme review

| Kapan | Apa | Siapa |
|---|---|---|
| Saat Issue Dataset masuk | review privasi & lisensi ≤14 hari | pengelola registry (+ komite etik) |
| Setiap akhir semester | cek kartu aktif: lokasi masih valid, Related Projects diperbarui, dataset yang tidak dipakai ditandai `deprecated` | pengelola registry |
| Sebelum rilis publik dataset (`DS-*` menjadi terbuka) | IP review singkat dengan `@directors`; cek ulang consent, hak merek, lisensi | pengelola + `@directors` |
| Roadmap review tahunan | dataset apa yang dibutuhkan sel matriks aktif tetapi belum ada → Issue Dataset "dibutuhkan" | `@research-leads` |

## 7. Hubungan ke Research ID

Dataset ID adalah simpul kedua dalam knowledge graph sederhana (`UIAI → DS / ART / PUB`, lihat [GOVERNANCE.md](../GOVERNANCE.md) §5). Aturan:

- Setiap kartu mencantumkan Research ID yang memakainya; setiap README riset mencantumkan Dataset ID yang dipakai.
- Dataset yang **dihasilkan** riset (bukan hanya dipakai) didaftarkan sebagai kartu baru dengan Source = UAI dan Related Projects = Research ID penghasilnya; ia juga dapat dicatat sebagai artefak di [publications](../publications/README.md) bila dirilis.
- Kartu publikasi ([publications](../publications/README.md)) merujuk Dataset ID agar klaim paper dapat ditelusuri ke data.

## 8. Contoh kartu

[DS-2026-001 Student Learning](datasets/DS-2026-001-student-learning.md) (Restricted) · [DS-2026-002 Halal Products](datasets/DS-2026-002-halal-products.md) (Public/Partner) · [DS-2026-003 Indonesian NLP](datasets/DS-2026-003-indonesian-nlp.md) (Public). Ketiganya **contoh ilustratif** — belum ada data riil; nama korpus, pemilik, dan ukuran ditulis `[isi]`.
