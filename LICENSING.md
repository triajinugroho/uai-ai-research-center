# LICENSING — Kebijakan Lisensi UAI AI Research Center

Tanpa lisensi, repository public sekalipun **tidak** memberi orang lain hak untuk menyalin, memodifikasi, atau memakai ulang karya. Karena pusat riset menghasilkan jenis aset yang berbeda (kode, dokumen, dataset, model, naskah), kami **tidak memakai satu lisensi untuk semua**.

## 1. Kebijakan default organization

| Jenis aset | Lisensi default | File |
|---|---|---|
| **Software / kode / tools riset** | **Apache License 2.0** | [`LICENSE`](LICENSE) |
| **Dokumentasi, framework, template, handbook, RPS supplement, materi ajar** | **CC BY 4.0** | [`LICENSE-DOCS`](LICENSE-DOCS) |
| **Open educational resources yang ingin tetap terbuka** | CC BY-SA 4.0 (opsional, per repo) | — |
| **Dataset** | **Tidak ada default** — wajib data governance review | kartu dataset |
| **Naskah/paper** | Mengikuti kebijakan publisher/hak cipta | — |
| **Riset rahasia / partner** | Tidak ada lisensi publik | repo private |
| **Potensi HKI / komersialisasi** | Restricted sampai IP review selesai | repo private |

Repository ini sendiri: kode di `tools/` dan skrip lain → Apache-2.0; seluruh Markdown, template, dan materi → CC BY 4.0. Atribusi: *"UAI AI Research Center, Universitas Al-Azhar Indonesia"* + penulis (lihat [CITATION.cff](CITATION.cff)).

## 2. Mengapa pilihan ini

- **Apache-2.0, bukan MIT**: sama permisifnya, tetapi memuat *patent grant* eksplisit; relevan bila suatu hari ada algoritma, tooling, atau komponen AI bernilai komersial.
- **Apache-2.0, bukan GPL**: GPL mewajibkan turunan tetap open; untuk pusat riset yang ingin banyak kolaborasi industri, itu sering menjadi gesekan. Apache lebih *frictionless*. GPL-3.0 tetap boleh dipilih per repo bila filosofi "turunan harus tetap open" memang diinginkan.
- **CC BY untuk dokumen**: tujuan knowledge output universitas adalah dipakai, dikutip, diajarkan ulang, dan menyebar, dengan atribusi kembali ke UAI dan penulis. Cocok dengan tujuan amal jariyah ilmu sekaligus reputasi akademik.
- **Dataset case-by-case**: dataset bisa mengandung data mahasiswa, kesehatan, partner, atau pribadi. Jangan otomatis CC0.

## 3. Ringkasan lisensi yang relevan

| Lisensi | Orang lain boleh apa? | Wajib apa? | Cocok untuk |
|---|---|---|---|
| MIT | Pakai, modifikasi, distribusi, komersial | Cantumkan copyright & lisensi | Kode, tools, starter repo |
| Apache 2.0 | Seperti MIT, termasuk komersial | Atribusi + ketentuan paten | Software/AI system yang lebih serius |
| GPL v3 | Pakai, modifikasi, distribusi | Turunan yang didistribusikan tetap GPL | Open-source yang ingin dijaga tetap open |
| AGPL v3 | Seperti GPL, termasuk penggunaan via server/web | Source modifikasi layanan network harus dibuka | SaaS/open AI service tertentu |
| BSD 2/3-Clause | Sangat permisif | Atribusi | Software akademik |
| MPL 2.0 | Modifikasi dan komersial | File yang dimodifikasi tetap open | Kompromi open vs commercial |
| CC BY 4.0 | Copy, adaptasi, komersial | Atribusi | Dokumen, modul, materi ilmiah |
| CC BY-SA 4.0 | Copy, adaptasi, komersial | Atribusi + turunan lisensi sama | Open educational resources |
| CC BY-NC 4.0 | Copy/adaptasi non-komersial | Atribusi, tidak komersial | Materi yang ingin dibatasi bisnis |
| CC BY-ND 4.0 | Copy/distribusi | Atribusi, tidak boleh modifikasi | Dokumen final tertentu |
| CC0 | Hampir bebas tanpa syarat | Minimal | Metadata/data tertentu |
| No License / All Rights Reserved | Praktis hanya melihat | Harus minta izin | Dokumen internal/IP sensitif |

Ingat: **public repo ≠ open source** (public tanpa lisensi = hak reuse sangat terbatas) dan **open source ≠ bebas aturan** (Apache, MIT, GPL semuanya punya kewajiban).

## 4. Decision tree

```
Apakah aset berupa software?
├─ Ya → Ingin reuse industri mudah?  → Apache-2.0
│       Turunan harus tetap open?    → GPL-3.0
└─ Tidak
   ├─ Dokumen / modul / template / materi ajar? → CC-BY-4.0 (CC-BY-SA-4.0 bila ingin tetap terbuka)
   ├─ Dataset? → Cek ownership → cek privacy → cek consent → cek partner agreement → baru tentukan lisensi
   │            (dibuat UAI & aman dibuka: CC-BY-4.0 / CC0; mengandung data pribadi/partner: TIDAK ada lisensi publik)
   ├─ Naskah / paper? → ikuti publisher; simpan metadata, DOI, sitasi; preprint hanya jika diizinkan
   └─ Berpotensi HKI / patent / komersialisasi? → JANGAN public-license sebelum IP review
```

## 5. Proyek AI punya beberapa lapis hak

Satu project dapat memiliki lisensi berbeda per komponen. Nyatakan semuanya di README riset:

```
Code:           Apache-2.0
Documentation:  CC-BY-4.0
Dataset:        CC-BY-4.0  (atau: restricted — lihat DS-2026-014)
Model weights:  Research-only license (atau: not released)
Paper:          Publisher copyright (DOI: …)
```

## 6. Prosedur

1. Saat membuat repo riset dari template, salin `LICENSE` (Apache-2.0) dan `LICENSE-DOCS` (CC BY 4.0), lalu isi tabel lisensi per komponen di README.
2. Dataset baru: isi kartu dataset di `datasets-registry/` termasuk field **License** dan **Privacy**; lisensi ditetapkan setelah review pengelola registry (dan komite etik bila ada data manusia).
3. Sebelum rilis artefak/model (`ART-YYYY-NNN`) atau publikasi, lakukan **IP review** singkat bersama `@directors`: apakah ada potensi HKI/komersialisasi? Jika ya, tahan lisensi publik.
4. Perubahan kebijakan ini lewat PR ke dokumen ini dan dicatat di [CHANGELOG.md](CHANGELOG.md).

*Catatan: dokumen ini adalah kebijakan internal, bukan nasihat hukum. Untuk kasus kompleks (partner, paten, data lintas negara), konsultasikan dengan unit HKI/hukum universitas.*
