# UIAI-2026-002 — Evaluasi RAG Berbahasa Indonesia untuk Dokumen Akademik & Regulasi Kampus

> **Status** Draft v0.1 (2026-09) · **contoh ilustratif** · **Terkait** [BACKLOG.md](../BACKLOG.md) · [TPL-04](../../research-os/08-templates/04-research-backlog-template.md) · [C1 AI Models, Data & Knowledge](../../research-roadmap/clusters/ai-models-data-knowledge.md) · [Domain Education](../../research-roadmap/domains/education.md) · [Domain Government](../../research-roadmap/domains/government.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md)

| Field | Nilai |
|---|---|
| **Research ID** | UIAI-2026-002 |
| **Judul** | Evaluasi RAG berbahasa Indonesia untuk dokumen akademik & regulasi kampus |
| **Cluster** | C1 AI Models, Data & Knowledge (primer) · C2 AI Systems, Software & Security (sekunder: keandalan/keamanan) — label `cluster:models` |
| **Domain** | Education (dokumen akademik) / Government (regulasi; kampus sebagai proxy layanan publik) |
| **Problem owner** | `[isi: unit layanan akademik / bagian hukum-regulasi kampus]` |
| **Potential dataset** | [DS-2026-003 Indonesian NLP](../../datasets-registry/datasets/DS-2026-003-indonesian-nlp.md) (korpus publik) + dokumen kampus publik `[isi]` |
| **Research maturity** | Idea |
| **Related courses** | NLP; AI & Machine Learning; Metodologi Penelitian; pendukung: Pengujian Perangkat Lunak |
| **Potential output** | TA; paper (NLP/IR evaluation); benchmark `DS-*`; pipeline evaluasi `ART-*` |
| **Priority** | P1-high |
| **Entry door** | Dataset |
| **Issue** | `#[isi]` |

## Problem statement

Unit layanan kampus menerima pertanyaan berulang tentang prosedur, panduan, dan regulasi yang tersebar di banyak dokumen berbahasa Indonesia. Asisten tanya-jawab berbasis RAG tampak menjanjikan, tetapi **belum ada cara yang disepakati untuk mengevaluasi** seberapa benar jawabannya untuk dokumen berbahasa Indonesia di domain akademik/regulasi: metrik apa, benchmark apa, protokol anotasi apa, dan jenis kesalahan apa (halusinasi, salah rujukan versi, jawaban parsial) yang paling sering muncul. Tanpa evaluasi itu, deployment di kampus — apalagi di layanan publik — tidak dapat dipertanggungjawabkan.

## Why it matters / stakeholder

| Pemangku kepentingan | Keputusan yang berubah |
|---|---|
| Unit layanan akademik/regulasi | apakah dan bagaimana asisten RAG boleh dipakai; konfigurasi mana yang cukup baik |
| Mahasiswa/pegawai pengguna | mendapat jawaban yang mengutip sumber dan versi dokumen |
| Peneliti C1/C4 lain | memakai benchmark dan protokol yang sama (research asset yang compound) |
| Instansi layanan publik (2028+) | dasar evaluasi sebelum adopsi |

## What we know

Ringkasan awal: evaluasi RAG umumnya membedakan kualitas retrieval dan kualitas generasi; benchmark yang tersedia didominasi bahasa Inggris dan domain umum; evaluasi berbasis LLM-as-judge dipakai luas tetapi validitasnya untuk bahasa Indonesia belum jelas. **Literatur awal: `[isi saat G3]`.**

## Candidate research questions

1. Bagaimana kinerja beberapa konfigurasi RAG (chunking, embedding, retriever) pada tanya-jawab dokumen akademik/regulasi berbahasa Indonesia dibanding baseline pencarian kata kunci (BM25) dan model tanpa retrieval?
2. Seberapa sering jawaban mengandung halusinasi atau rujukan versi dokumen yang salah, dinilai anotator manusia, dan apakah penilaian otomatis (LLM-as-judge) sejalan dengan penilaian manusia?
3. Protokol anotasi seperti apa yang menghasilkan agreement antar-anotator yang memadai untuk benchmark ini?

## Possible data & sensitivity

| Data | Sumber | Sensitivitas | Syarat |
|---|---|---|---|
| Dokumen akademik & regulasi kampus yang **sudah publik** | situs/unit UAI | Public | cek status publikasi; catat versi dan tanggal |
| Dokumen internal | unit UAI | Internal | izin; tidak dirilis sebagai bagian benchmark |
| Pasangan pertanyaan–jawaban yang dianotasi | dibuat tim + anotator | Public (bila dokumen sumber publik) | pedoman anotasi; agreement dicatat |
| Korpus publik bahasa Indonesia | `[isi: nama korpus publik yang dipilih]` | Public | cek lisensi |
| Pertanyaan riil pengguna (log) | unit layanan | Restricted | anonimisasi; hanya bila diizinkan |

## Candidate mentor

`[isi: dosen NLP / information retrieval]`.

## Risks

| Risiko | Mitigasi |
|---|---|
| Biaya API model eksternal | pakai model terbuka kecil sebagai baseline; batasi ukuran evaluasi |
| Dokumen berubah versi selama riset | bekukan snapshot korpus dengan tanggal; catat di kartu dataset |
| Anotasi tidak konsisten | pedoman tertulis, pelatihan anotator, ukur agreement, adjudikasi |
| Data pribadi dalam dokumen/log | saring sebelum masuk korpus; log hanya teranonimisasi |
| Leakage antara data pengembangan dan uji | pisahkan sejak awal; catat di Experiment Card |

## Next evidence

Untuk naik ke G2: konfirmasi daftar dokumen publik yang boleh dipakai (`[isi]`), pernyataan kebutuhan dari unit layanan, dan estimasi jumlah pertanyaan riil per bulan sebagai bukti masalah nyata.
