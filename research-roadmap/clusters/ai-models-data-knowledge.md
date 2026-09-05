# C1 — AI Models, Data & Knowledge

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) · [Datasets Registry](../../datasets-registry/README.md)

| Field | Nilai |
|---|---|
| Kode | **C1** |
| Peran AI | **AI Core** — objek risetnya AI itu sendiri: model, data, pengetahuan, evaluasi |
| Label GitHub | `cluster:models` |
| Tim GitHub | `@ai-models` |
| Program terkait | `program-indonesian-llm` (2029), `program-ai-education` (2027) |
| Kompetensi prodi yang ditumpangi | Data Science, NLP (sumber: dokumen diskusi; verifikasi sebelum dokumen formal) |

## 1. Scope

Klaster ini meneliti **bagaimana model, data, dan representasi pengetahuan dibangun dan dievaluasi** — dengan penekanan pada konteks Indonesia yang sering *low-resource*: bahasa Indonesia dan bahasa daerah, dokumen berbahasa campur, domain khusus (akademik, regulasi, halal, kesehatan). Fokusnya bukan mengejar model terbesar, tetapi **data-centric AI**, **evaluasi yang jujur**, dan **pengetahuan terstruktur** yang membuat model kecil bekerja baik untuk masalah nyata.

Tiga sub-area:

| Sub-area | Isi |
|---|---|
| **Models** | adaptasi/fine-tuning model bahasa dan visi untuk bahasa/domain Indonesia; model kecil dan efisien; retrieval-augmented generation (RAG) |
| **Data** | pembuatan dan kurasi dataset berbahasa Indonesia; anotasi; kualitas data; data sintetis dan risikonya; dokumentasi dataset (datasheet/kartu) |
| **Knowledge** | knowledge graph, ontologi domain (halal, akademik, regulasi), ekstraksi informasi, penalaran berbasis pengetahuan |

## 2. Research questions besar 2026–2030

1. Seberapa jauh model bahasa yang tersedia saat ini dapat diandalkan untuk **dokumen berbahasa Indonesia di domain khusus** (akademik, regulasi, halal), dan pada jenis kesalahan apa mereka gagal?
2. Bagaimana **mengevaluasi sistem RAG berbahasa Indonesia** secara reproducible — metrik, benchmark, dan protokol anotasi apa yang valid untuk konteks kita?
3. Apakah **pendekatan data-centric** (kurasi, pembersihan, augmentasi terkontrol) memberi peningkatan yang setara atau lebih besar daripada mengganti model, pada dataset skala kampus?
4. Bagaimana membangun **korpus dan benchmark** bahasa Indonesia/daerah yang etis (consent, lisensi) dan dapat dibagikan?
5. Representasi pengetahuan apa (ontologi, knowledge graph) yang paling berguna untuk **verifikasi klaim** di domain halal dan regulasi, dan bagaimana mengukurnya?
6. Kapan **model kecil** yang dilatih/diadaptasi lokal cukup baik dibanding layanan model besar, dengan mempertimbangkan biaya, privasi, dan latensi?
7. Bagaimana mendeteksi dan mengukur **halusinasi dan bias** pada keluaran model untuk bahasa Indonesia, sehingga hasilnya dapat dipakai klaster C3?
8. Metode anotasi berbantuan LLM apa yang **cukup andal** untuk dipakai membangun dataset, dan bagaimana memvalidasinya terhadap anotasi manusia?

## 3. Example topics (konteks Indonesia/UAI)

1. Evaluasi RAG untuk tanya-jawab dokumen akademik dan regulasi kampus berbahasa Indonesia (lihat [UIAI-2026-002](../../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md)).
2. Benchmark pemahaman bacaan/QA berbahasa Indonesia untuk domain pendidikan tinggi.
3. Ekstraksi informasi komposisi bahan dari label produk pangan untuk mendukung verifikasi halal.
4. Knowledge graph bahan dan proses halal dari sumber publik.
5. Klasifikasi dan peringkasan pengaduan/aspirasi publik berbahasa Indonesia campur daerah.
6. Perbandingan strategi chunking dan embedding untuk dokumen berbahasa Indonesia.
7. Deteksi halusinasi pada jawaban model untuk pertanyaan faktual seputar regulasi.
8. Data-centric AI: pengaruh kualitas label terhadap kinerja model pada dataset kampus.
9. Korpus bahasa daerah kecil (mis. dari komunitas) dan evaluasi transfer lintas bahasa.
10. Anotasi berbantuan LLM untuk teks edukasi kesehatan berbahasa Indonesia, divalidasi terhadap anotator manusia.
11. Model kecil untuk klasifikasi intent layanan mahasiswa yang dapat dijalankan on-premise.
12. Datasheet/kartu dataset untuk seluruh dataset UAI: apakah dokumentasi meningkatkan reuse?

## 4. Related courses

| Mata kuliah | Kontribusi ke C1 | Mode ([ARC-03](../../research-os/02-academic-architecture/03-ai-contribution-modes.md)) |
|---|---|---|
| AI & Machine Learning (sem. V) | model, evaluasi, baseline | E/R |
| Data Mining (sem. IV) | preprocessing, feature, kualitas data | E/R |
| NLP | korpus, tokenisasi, model bahasa, RAG | R |
| Basis Data (sem. III) | skema data, knowledge graph | F |
| Statistika & Statistika Terapan (sem. I–II) | inferensi, ketidakpastian evaluasi | F |
| Metodologi Penelitian (sem. VII) | desain evaluasi, threats to validity | R (Prove) |
| Tugas Akhir (sem. VIII) | kontribusi | R (Contribute) |

Detail per mata kuliah: [research-based-learning/courses](../../research-based-learning/README.md).

## 5. Kebutuhan data dan compute

| Kebutuhan | 2026–2027 | 2028–2030 |
|---|---|---|
| Data | dokumen publik kampus, korpus publik berbahasa Indonesia (`[isi: nama korpus yang dipilih]`, lihat [DS-2026-003](../../datasets-registry/datasets/DS-2026-003-indonesian-nlp.md)), anotasi kecil oleh mahasiswa | korpus domain (halal, kesehatan) dari mitra; benchmark buatan UAI |
| Compute | laptop/Colab/GPU bersama tingkat kecil; API model eksternal untuk baseline (tanpa data pribadi, lihat [SECURITY.md](../../SECURITY.md)) | GPU institusional untuk fine-tuning model kecil–menengah; penyimpanan korpus |
| Anotasi | pedoman anotasi + agreement antar-anotator dicatat | platform anotasi; anotator terlatih lintas fakultas (bahasa, hukum) |

Aturan: data mentah tidak masuk GitHub; hanya kartu di [datasets-registry](../../datasets-registry/README.md).

## 6. Output yang diharapkan

| Jenis output ([ARC-06](../../research-os/02-academic-architecture/06-research-output-taxonomy.md)) | Contoh |
|---|---|
| Dataset / benchmark (`DS-*`) | benchmark QA dokumen akademik berbahasa Indonesia; korpus bahasa daerah kecil |
| Model / software (`ART-*`) | model klasifikasi kecil on-premise; pipeline evaluasi RAG |
| Paper (`PUB-*`) | studi evaluasi, dataset paper, replikasi |
| Research brief | rekomendasi "model mana cukup" untuk unit kampus |
| TA | evaluasi terkontrol satu komponen (retriever, embedding, anotasi) |

## 7. Entry door yang umum

**Dataset** (data tersedia → apa yang bisa diuji) dan **Course Project** (proyek NLP/AI-ML yang menghasilkan research asset). Entry door **Faculty Research** relevan bila dosen sudah memiliki korpus. Apa pun pintunya, gate-nya sama ([OPS-03](../../research-os/06-execution-os/03-research-gates.md)).

## 8. Keterkaitan program dan klaster lain

- Memasok **metrik dan temuan bias/halusinasi** ke [C3](responsible-human-ai.md).
- Memasok **model dan korpus** ke [C4](applied-ai.md) untuk domain tertentu.
- Bergantung pada [C2](ai-systems-security.md) untuk deployment dan reliabilitas.
- Program: `program-indonesian-llm` adalah muara klaster ini; `program-ai-education` memakai RAG dokumen akademik.

## 9. Topik yang sengaja tidak kita kejar (2026–2030)

| Tidak dikejar | Alasan (Occam) |
|---|---|
| Pelatihan foundation model bahasa Indonesia dari nol pada skala frontier | compute dan data di luar jangkauan; kontribusi lebih besar lewat evaluasi, adaptasi, dan data |
| Mengejar peringkat leaderboard benchmark berbahasa Inggris umum | tidak menjawab masalah pemangku kepentingan Indonesia/UAI |
| Arsitektur model baru tanpa masalah domain | risiko "solution-first"; gagal G2 |
| Web-scale crawling tanpa kejelasan lisensi/consent | bertentangan dengan [LICENSING.md](../../LICENSING.md) dan amanah epistemik |
| Riset yang hanya membandingkan accuracy tanpa baseline dan error analysis | gagal G5/G7 |

Fokus kami: **model yang cukup, data yang jujur, evaluasi yang dapat direproduksi.**
