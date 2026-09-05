# DS-2026-003 — Indonesian Text Corpus (publik)

> **Status** contoh ilustratif — belum ada data riil · Draft v0.1 (2026-09) · **Terkait** [REGISTRY.md](../REGISTRY.md) · [Registry README](../README.md) · [TPL-05](../../research-os/08-templates/05-dataset-registry-template.md) · [LICENSING.md](../../LICENSING.md) · [UIAI-2026-002](../../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md) · [C1 AI Models, Data & Knowledge](../../research-roadmap/clusters/ai-models-data-knowledge.md)

## Kartu dataset

| Field | Nilai |
|---|---|
| **Dataset ID** | DS-2026-003 |
| **Name** | Indonesian Text Corpus — `[isi: nama korpus publik yang dipilih]` |
| **Domain** | General (bahasa Indonesia); dipakai untuk Education dan Government (dokumen akademik/regulasi) |
| **Source** | Public — `[isi: URL/sumber resmi korpus]` |
| **Owner** | Penerbit korpus asli `[isi]`; pengelola salinan lokal di UAI `[isi]` |
| **Size** | `[isi: jumlah dokumen/kalimat/token; ukuran file]` |
| **Modality** | Text (bahasa Indonesia; sebagian mungkin campur bahasa daerah/Inggris) |
| **License** | `[isi: lisensi korpus asli — salin persis dari sumber]`; cek apakah redistribusi/turunan diizinkan sebelum mengunggah ulang atau merilis benchmark turunan |
| **Privacy** | **Public** — namun periksa apakah korpus memuat data pribadi (nama, kontak) dari sumber web; saring sebelum dipakai |
| **Potential Task** | Language modeling/adaptasi, retrieval & RAG evaluation, text classification, QA, information extraction, benchmark construction |
| **Related Projects** | [UIAI-2026-002](../../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md); calon: klasifikasi pengaduan (Government), korpus edukasi kesehatan (Health) |
| **Quality Notes** | `[isi setelah eksplorasi]` — catat: domain/genre dominan, duplikasi, kualitas tokenisasi, proporsi bahasa campur, tanggal pengambilan (snapshot), versi korpus |
| **Access** | Unduh langsung dari sumber sesuai lisensi; salinan lokal (snapshot berversi) di `[isi: institutional storage/HF org UAI]` agar eksperimen reproducible |
| **Possible Research Questions** | (1) Bagaimana kinerja retriever/embedding untuk dokumen berbahasa Indonesia domain akademik dibanding domain umum? (2) Seberapa besar pengaruh kualitas/duplikasi korpus terhadap evaluasi RAG? (3) Apakah model kecil yang diadaptasi pada korpus ini cukup untuk klasifikasi teks layanan kampus? |
| **Physical Location** | Sumber asli (publik) + snapshot berversi di `[isi]`; tidak di GitHub |
| **Review Date** | `[isi]` |
| **Status** | contoh ilustratif — belum ada data riil |

## Catatan penggunaan korpus publik

1. **Jangan mengunggah ulang** korpus ke GitHub/HF tanpa memastikan lisensi mengizinkan redistribusi; cukup catat sumber dan versi.
2. **Snapshot berversi**: simpan hash/tanggal unduhan di Experiment Card agar hasil dapat direproduksi meski sumber berubah.
3. **Benchmark turunan** (mis. pasangan pertanyaan–jawaban dari dokumen kampus) didaftarkan sebagai kartu baru dengan Source = UAI dan lisensi ditetapkan setelah review.
4. **Data pribadi** yang mungkin terkandung dalam korpus web disaring; jangan memakai bagian yang memuat identitas untuk contoh di paper.
5. **Leakage**: pastikan data evaluasi tidak tumpang tindih dengan data adaptasi/latih; catat di Experiment Card ([TPL-09](../../research-os/08-templates/09-experiment-card.md)).

## Sensitivitas dan risiko

| Risiko | Mitigasi |
|---|---|
| Lisensi tidak mengizinkan turunan | pilih korpus lain; catat keputusan di Issue Dataset |
| Korpus berubah/hilang dari sumber | snapshot berversi di storage institusi |
| Bias domain (mis. berita dominan) | laporkan distribusi; tambah dokumen domain UAI sebagai kartu terpisah |
| Data pribadi dari web | penyaringan; tidak ditampilkan dalam output |
