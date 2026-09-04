# Dataset Registry Template

> **ID** TPL-05 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Pengelola datasets-registry, dosen pemilik data, mahasiswa peneliti, komite etik/data governance, partner
> **Terkait** [datasets-registry/README.md](../../datasets-registry/README.md) · [REGISTRY.md](../../datasets-registry/REGISTRY.md) · [SECURITY.md](../../SECURITY.md) · [LICENSING.md §4](../../LICENSING.md) · [MET-07 Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [OPS-03 G5](../06-execution-os/03-research-gates.md)

## Cara pakai

Satu **kartu dataset** per dataset, disimpan sebagai `datasets-registry/datasets/ds-YYYY-NNN-<slug>.md`, dengan satu baris di indeks `datasets-registry/REGISTRY.md`. Diisi oleh pemilik data (dosen, tim riset, atau partner lewat Issue **Dataset**) dan disetujui pengelola registry; Dataset ID `DS-YYYY-NNN` diberikan saat kartu disetujui. Wajib ada sebelum G5 Method Ready untuk setiap dataset yang dipakai riset (Dataset/Data Plan), dan diperbarui saat lisensi, akses, atau lokasi berubah. Kartu ini adalah **metadata**: data fisik tidak pernah masuk GitHub. Reviewer G5 memeriksa kolom License, Privacy, dan Access sebelum menyetujui desain.

## Aturan: GitHub = catalog & governance layer, bukan storage

1. Repository hanya menyimpan kartu (metadata), skema kolom, contoh sintetis kecil (≤ 100 baris, tanpa data pribadi), dan skrip akses.
2. Data fisik berada di salah satu: institutional server UAI, Hugging Face, Kaggle, Google Drive institusi, cloud storage, atau server partner — dicatat di kolom **Lokasi fisik** beserta cara akses.
3. Privacy `Restricted` dan `Confidential`: tidak ada sampel mentah di GitHub; hanya skema + statistik agregat. Lihat [SECURITY.md](../../SECURITY.md).
4. Lisensi dataset tidak pernah default; ikuti decision tree [LICENSING.md §4](../../LICENSING.md) (ownership → privacy → consent → partner agreement → lisensi).
5. Dataset yang memuat data manusia memerlukan catatan consent/anonimisasi dan, bila ada, persetujuan komite etik ([MET-07](../04-metopen-research-studio/07-research-integrity-and-ethics.md)).
6. Setiap kartu ditinjau ulang minimal setahun sekali atau saat proyek terkait berganti fase (kolom **Tanggal review**).

## Template kartu (salin ke `datasets-registry/datasets/ds-YYYY-NNN-<slug>.md`)

```markdown
# [Nama dataset]

| Field | Isi |
|---|---|
| Dataset ID | [DS-YYYY-NNN] |
| Name | [nama resmi + versi] |
| Domain | [Education / Halal / Health / Food / Government / Business / Social Impact / lintas] |
| Source | [Public / UAI / Partner] — [asal konkret, URL bila publik] |
| Owner | [nama/unit + kontak] |
| Size | [jumlah record/berkas, ukuran GB, rentang waktu] |
| Modality | [Text / Image / Tabular / Audio / Video / Time series / Graph / Multimodal] |
| License | [CC BY 4.0 / CC0 / research-only / lisensi partner / belum ditetapkan — alasan] |
| Privacy | [Public / Restricted / Confidential] — [jenis data pribadi bila ada; anonimisasi; consent] |
| Potential task | [classification / prediction / regression / RAG / retrieval / NER / recommendation / clustering / benchmarking / …] |
| Related projects | [UIAI-YYYY-NNN, …] |
| Quality notes | [kelengkapan, label noise, ketidakseimbangan kelas, bias sampling, duplikasi, versi] |
| Access | [cara minta akses, siapa menyetujui, SLA, persyaratan (NDA/etik)] |
| Possible research questions | 1. [...] 2. [...] |
| Lokasi fisik | [institutional server / Hugging Face / Kaggle / Drive / cloud / server partner] — [path/URL/ID] |
| Skema / dokumentasi | [link ke data/README.md proyek atau datasheet] |
| Tanggal review | [YYYY-MM-DD] — reviewer [nama] |
```

## Tabel indeks (`datasets-registry/REGISTRY.md`)

```markdown
| Dataset ID | Name | Domain | Source | Modality | Size | License | Privacy | Potential task | Related projects | Lokasi fisik | Review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [DS-YYYY-NNN] | [nama] | [domain] | [Public/UAI/Partner] | [modality] | [size] | [license] | [Public/Restricted/Confidential] | [task] | [UIAI-…] | [lokasi] | [YYYY-MM-DD] |
```

## Contoh terisi

| Field | Isi |
|---|---|
| Dataset ID | DS-2026-001 |
| Name | UAI Informatics Anonymized Transcript & Course-Plan Dataset (pilot v0.1) |
| Domain | Education |
| Source | UAI — BAAK/Prodi Informatika, ekspor SIAKAD [isi] |
| Owner | [Kaprodi Informatika / dosen penanggung jawab data — isi] |
| Size | 120 mahasiswa × ±40 baris mata kuliah (≈4.800 record), 2 MB CSV, angkatan [isi] |
| Modality | Tabular (+ dokumen kurikulum PDF/teks sebagai konteks RAG) |
| License | Belum ditetapkan — data pribadi mahasiswa; rencana: rilis versi sintetis CC BY 4.0 setelah review etik |
| Privacy | Restricted — NIM dan nama dihapus, ID acak, tanggal lahir dibuang; consent tertulis dari mahasiswa yang datanya dipakai |
| Potential task | Recommendation (rencana studi), constraint checking, RAG evaluation, prediction (risiko keterlambatan) |
| Related projects | UIAI-2026-001 |
| Quality notes | Nilai mata kuliah konversi kurikulum lama → baru belum seragam; 7 % baris tanpa kode mata kuliah; distribusi angkatan tidak seimbang |
| Access | Ajukan Issue `type:dataset` menyebut Research ID + tujuan; disetujui owner + pengelola registry ≤ 5 hari kerja; wajib menandatangani pernyataan penggunaan data |
| Possible research questions | 1. Seberapa valid rekomendasi rencana studi berbasis LLM+RAG terhadap aturan prasyarat/SKS? 2. Fitur apa yang paling memprediksi keterlambatan lulus? |
| Lokasi fisik | Institutional server UAI `[path]` (akses VPN); sampel sintetis 50 baris di repo proyek `data/sample-synthetic.csv` |
| Skema / dokumentasi | `proj-2026-ai-academic-advising/data/README.md` |
| Tanggal review | 2026-09-[dd] — reviewer [isi] |

Baris indeks: `DS-2026-001 | UAI Informatics Anonymized Transcript & Course-Plan Dataset | Education | UAI | Tabular | 4.800 record | belum ditetapkan | Restricted | recommendation, RAG eval | UIAI-2026-001 | institutional server | 2026-09-[dd]`

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Privasi | Jenis data pribadi, cara anonimisasi, dan consent disebut eksplisit | "Data aman" |
| Lisensi | Keputusan lisensi + alasan, atau "belum ditetapkan" + rencana | CC0 otomatis pada data mahasiswa |
| Quality notes | Menyebut noise, ketidakseimbangan, versi | "Data bersih" |
| Lokasi | Path/URL + cara akses + penyetuju | "Ada di laptop [nama]" |
| Keterkaitan | Related projects terisi dan sinkron dengan One-Pager | Dataset dipakai riset tetapi tidak terdaftar |
| Pemisahan | Hanya metadata di GitHub | CSV mentah di-commit |
