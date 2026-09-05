# Domain — Health (Kesehatan)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C1 AI Models, Data & Knowledge](../clusters/ai-models-data-knowledge.md) · [C3 Human-Centered & Responsible AI](../clusters/responsible-human-ai.md) · [C4 Applied AI](../clusters/applied-ai.md) · [SECURITY.md](../../SECURITY.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `health` |
| Program | `program-ai-health` (dibuka 2028, wajib mitra dan protokol data sensitif) |
| Klaster utama | C4 (skrining, prediksi risiko), C1 (NLP teks kesehatan berbahasa Indonesia), C3 (explainability, kepercayaan tenaga kesehatan), C2 (keandalan, privasi) |
| Prioritas roadmap | dibuka penuh 2028; 2026–2027 hanya data publik/sintetis dan masalah kesehatan kampus |

## 1. Mengapa domain ini untuk UAI

Kesehatan adalah prioritas nasional dan kebutuhan komunitas kampus (layanan kesehatan mahasiswa, kesehatan mental, gizi). UAI memiliki fakultas/prodi yang bersinggungan dengan kesehatan (mis. Gizi; sumber: dokumen diskusi — verifikasi) sehingga kolaborasi lintas fakultas **Domain Problem + Data + AI Capability + Evaluation + Impact** dapat dijalankan di dalam kampus sebelum ke mitra eksternal. Domain ini juga menuntut standar etika dan privasi tertinggi — tempat yang tepat untuk membuktikan bahwa tata kelola data UAI ([SECURITY.md](../../SECURITY.md)) berfungsi.

Posisi kami tegas: AI **mendukung** keputusan tenaga kesehatan, tidak menggantikannya.

> **Catatan verifikasi.** Regulasi data kesehatan dan persyaratan etik penelitian kesehatan tidak dikutip di sini; petakan ke ketentuan resmi terkini. Komite etik yang dipakai: `[isi: komite etik UAI/mitra]`. Mitra layanan kesehatan: `[isi]`.

## 2. Problem space (masalah nyata)

1. Layanan kesehatan kampus/komunitas kekurangan alat **skrining dini** sederhana (risiko gizi, kesehatan mental, penyakit tidak menular) yang sesuai konteks Indonesia.
2. Informasi kesehatan berbahasa Indonesia di internet banyak yang **tidak akurat**; pengguna sulit memverifikasi.
3. Catatan layanan kesehatan primer sering berupa **teks bebas berbahasa Indonesia** yang tidak terstruktur.
4. Tenaga kesehatan skeptis terhadap rekomendasi AI yang **tidak dapat dijelaskan**.
5. Program gizi komunitas kesulitan mengestimasi asupan dari laporan sederhana (foto, catatan).
6. Kesehatan mental mahasiswa: deteksi kebutuhan dukungan dini tanpa stigma dan tanpa surveillance.
7. Edukasi kesehatan personal (chatbot) berisiko memberi nasihat salah; belum ada evaluasi berbahasa Indonesia yang ketat.
8. Data kesehatan tersebar dan sensitif; riset sulit dimulai tanpa protokol yang jelas.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| Unit layanan kesehatan kampus, konselor mahasiswa | pemilik masalah, pengguna |
| Prodi/fakultas kesehatan dan gizi di UAI | pakar domain, co-investigator (verifikasi) |
| Fasilitas kesehatan primer (puskesmas/klinik) | mitra data dan evaluasi (2028+, perjanjian) |
| Organisasi kesehatan komunitas / lembaga sosial | mitra program gizi/edukasi |
| Tenaga kesehatan (dokter, perawat, ahli gizi) | evaluator explainability, partisipan user study |
| Mahasiswa dan masyarakat sekitar kampus | partisipan (consent ketat) |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Data klinis/rekam medis | **Confidential** | tidak pernah di GitHub; hanya dengan perjanjian dan etik; analisis di lingkungan mitra bila memungkinkan |
| Kuesioner skrining yang dikumpulkan sendiri | **Restricted** | consent, anonimisasi, protokol etik |
| Data kesehatan mental | **Confidential** | risiko tertinggi; hanya dengan konselor profesional sebagai co-investigator |
| Dataset kesehatan publik (survei nasional agregat, dataset terbuka) | Public | cek lisensi; cocok untuk 2026–2027 |
| Teks edukasi kesehatan publik berbahasa Indonesia | Public | untuk korpus NLP dan evaluasi chatbot |
| Citra makanan (dikumpulkan sendiri) | Restricted/Public tergantung isi | hindari identitas orang |
| Data sintetis | Public | untuk pengembangan metode sebelum akses data riil |

## 5. Contoh research questions

- Apakah model skrining sederhana dari kuesioner + data antropometri memiliki akurasi setara instrumen standar pada populasi mahasiswa, dan apakah ia lebih cepat? (C4)
- Bagaimana kinerja model bahasa dalam menjawab pertanyaan kesehatan umum berbahasa Indonesia dibanding sumber resmi, dan jenis kesalahan apa yang berbahaya? (C1 + C3)
- Penjelasan seperti apa yang membuat ahli gizi menerima/menolak rekomendasi sistem, diukur lewat user study? (C3)
- Seberapa akurat estimasi porsi/gizi dari citra makanan Indonesia dibanding catatan manual, untuk kebutuhan program komunitas (bukan klinis)? (C4, lintas fakultas)
- Arsitektur privasi seperti apa (agregasi, pseudonimisasi, analisis di sisi mitra) yang memungkinkan riset tanpa memindahkan data klinis? (C2)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Alat skrining dini terverifikasi untuk layanan kampus/komunitas | deteksi lebih awal, rujukan tepat |
| Benchmark evaluasi jawaban kesehatan berbahasa Indonesia (`DS-*`) | standar keamanan chatbot kesehatan lokal |
| Protokol tata kelola data kesehatan untuk riset mahasiswa | template dipakai program lain |
| Paper (health informatics, NLP, HCI) | kolaborasi lintas fakultas terbukti |
| Research brief untuk mitra layanan kesehatan | keputusan program berbasis bukti |

## 7. Risiko etika dan privasi khas domain

- **Bahaya klinis**: rekomendasi salah dapat merugikan; sistem hanya pendukung, evaluasi *harm* eksplisit, tenaga kesehatan selalu di loop.
- **Data paling sensitif**: kebocoran = kerugian tak terpulihkan; ikuti [SECURITY.md](../../SECURITY.md), prompt ke AI eksternal tidak boleh memuat data pasien.
- **Stigma** kesehatan mental; desain tanpa pelabelan individu, fokus dukungan.
- **Bias populasi**: dataset publik luar negeri tidak mewakili Indonesia; validasi lokal wajib.
- **Overclaiming**: klaim "mendeteksi penyakit" dari data survei adalah pelanggaran amanah epistemik; klaim harus sebatas bukti (G7).

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| AI & Machine Learning | baseline skrining pada dataset publik/sintetis |
| NLP | korpus edukasi kesehatan; evaluasi QA kesehatan |
| Data Mining | eksplorasi survei kesehatan publik agregat |
| Interaksi Manusia–Komputer | user study explainability dengan tenaga kesehatan |
| Pengujian Perangkat Lunak | pengujian keandalan sistem skrining |
| Etika Profesi | analisis protokol etik dan privasi |
| Metodologi Penelitian | Research Pack dengan Ethics & Privacy yang lengkap sebagai contoh terbaik |
