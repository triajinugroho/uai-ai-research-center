# Domain — Education (Pendidikan Tinggi)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C3 Human-Centered & Responsible AI](../clusters/responsible-human-ai.md) · [C4 Applied AI](../clusters/applied-ai.md) · [alignment/uai.md](../alignment/uai.md) · [research-based-learning](../../research-based-learning/README.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `education` |
| Program | `program-ai-education` (dibuka 2027) |
| Klaster utama | C3, C4; pendukung C1 (RAG dokumen akademik), C2 (keandalan & privasi sistem kampus) |
| Prioritas roadmap | **Tertinggi 2026–2027** — masalah, data, dan pemangku kepentingan ada di dalam kampus |

## 1. Mengapa domain ini untuk UAI

UAI adalah kampus tempat riset ini sendiri berlangsung: mahasiswa, dosen wali, unit layanan akademik, dan mata kuliah adalah pemangku kepentingan yang dapat ditemui setiap hari. Ini membuat pendidikan menjadi domain dengan **jarak terpendek antara masalah, data, dan evaluasi**. Selain itu, seluruh sistem UIRP (Metopen sebagai Research Studio, Build → Prove → Contribute) adalah intervensi pendidikan yang layak diteliti — riset tentang sistem kita sendiri adalah bagian dari domain ini.

Sebagai kampus Islam di Jakarta, UAI juga punya pertanyaan khas: bagaimana AI dipakai dalam pembelajaran yang menjunjung integritas (amanah epistemik), dan bagaimana pendidikan Islam terintegrasi memanfaatkan AI secara bertanggung jawab.

> **Catatan verifikasi.** Struktur kurikulum dan status akreditasi yang dirujuk dokumen ini berasal dari dokumen diskusi; verifikasi ke Prodi/LAM-INFOKOM sebelum dokumen formal. Akses ke data akademik memerlukan izin unit terkait — `[isi: unit pengelola data akademik UAI]`.

## 2. Problem space (masalah nyata)

1. **Academic advising** dosen wali bersifat reaktif; mahasiswa berisiko (nilai, kehadiran, beban SKS) sering terdeteksi terlambat.
2. Mahasiswa memakai GenAI untuk tugas dan riset tanpa **literasi verifikasi**; dosen tidak punya cara adil untuk menilai.
3. Dokumen akademik dan regulasi kampus (panduan, SK, prosedur) sulit dicari; pertanyaan berulang membebani staf.
4. **Proposal TA** sering *solution-first*; kualitas bukti rendah; Metopen dan TA terfragmentasi.
5. Research asset mata kuliah (dataset, kode, prototype) hilang setelah semester berakhir.
6. Asesmen berbasis proyek sulit dinilai konsisten antar dosen; rubrik jarang divalidasi.
7. Materi ajar berbahasa Indonesia yang terstruktur untuk asisten belajar (RAG) belum tersedia.
8. Mahasiswa dengan kebutuhan khusus (disabilitas, latar belakang bahasa) kurang terlayani oleh alat digital kampus.
9. Alumni tracing dan kesesuaian kurikulum–pekerjaan dianalisis manual dan jarang.
10. Dosen kekurangan waktu untuk mentoring riset; beban review tidak terdistribusi.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran dalam riset |
|---|---|
| Dosen wali, dosen pengampu, koordinator TA | pemilik masalah, evaluator kegunaan |
| Unit layanan akademik / bagian kemahasiswaan | pemilik data, pengguna sistem |
| Mahasiswa (subjek sekaligus co-researcher) | partisipan user study, pengusul masalah |
| Unit penjaminan mutu / tim akreditasi | pengguna evidence |
| Prodi/fakultas lain di UAI (Psikologi, Pendidikan Islam) | mitra pengukuran perilaku dan pedagogi |
| Perguruan tinggi lain di Indonesia | replikasi lintas kampus (2028+) |
| Penyedia LMS / edtech lokal | partner data/deployment (2028+) |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Rekam akademik (nilai, SKS, kehadiran) | **Restricted** — data pribadi mahasiswa | wajib anonimisasi/pseudonimisasi, consent, izin unit; lihat [DS-2026-001](../../datasets-registry/datasets/DS-2026-001-student-learning.md) |
| Log LMS/interaksi asisten belajar | Restricted | agregasi; kunci pemetaan di luar repo |
| Dokumen akademik & regulasi kampus publik | Public/Internal | cek status publikasi dokumen sebelum dipakai |
| Survei/wawancara AI literacy | Restricted (dikumpulkan sendiri) | protokol etik, consent |
| Research Pack & artefak riset mahasiswa | Internal → Public saat rilis | izin mahasiswa untuk dijadikan objek studi |
| Data alumni | Restricted | melalui unit alumni |

Aturan umum: [SECURITY.md](../../SECURITY.md); data mentah tidak pernah masuk GitHub.

## 5. Contoh research questions

- Seberapa akurat model early warning berbasis data akademik semester 1–4 memprediksi risiko keterlambatan studi, dan apakah dosen wali mengubah tindakan setelah melihatnya? (C4 + C3)
- Penjelasan seperti apa pada rekomendasi advising yang meningkatkan kepercayaan terkalibrasi dosen wali? (C3)
- Apakah asisten RAG dokumen kampus mengurangi pertanyaan berulang ke staf dibanding FAQ statis, dan berapa tingkat jawaban salahnya? (C1 + C4)
- Apakah protokol AI Research Protocol mengubah proporsi referensi terverifikasi dalam proposal mahasiswa dibanding angkatan sebelumnya? (C3, riset tentang sistem sendiri)
- Bagaimana rubrik 5E berkorelasi dengan kelanjutan riset ke TA dan publikasi? (C3/C4)

## 6. Output dan dampak

| Output | Dampak yang diharapkan |
|---|---|
| Dashboard/prototype advising dengan penjelasan | intervensi dosen wali lebih awal |
| Instrumen AI literacy tervalidasi | kebijakan AI prodi berbasis data |
| Asisten RAG dokumen kampus + benchmark evaluasi | layanan akademik lebih cepat; benchmark dipakai kampus lain |
| Paper pendidikan tinggi/computing education | reputasi prodi; evidence akreditasi ([GOV-05](../../research-os/07-governance/05-ppts-and-institutional-evidence.md)) |
| Research asset mata kuliah yang terdokumentasi | compounding loop antar angkatan |

## 7. Risiko etika dan privasi khas domain

- **Profiling mahasiswa**: prediksi risiko dapat melabeli dan mendiskriminasi; wajib audit fairness dan penggunaan sebagai *pendukung* keputusan manusia.
- **Consent yang tidak setara**: mahasiswa berada pada relasi kuasa dengan dosen; consent harus sukarela dan dapat ditarik.
- **Surveillance**: log interaksi berlebihan; batasi pada tujuan riset yang disetujui.
- **Integritas asesmen**: alat deteksi AI berpotensi salah menuduh; jangan dipakai sebagai bukti tunggal.
- **Kebocoran data pribadi** ke layanan AI eksternal lewat prompt — dilarang ([SECURITY.md](../../SECURITY.md)).

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| AI & Machine Learning | model baseline prediksi risiko pada data sintetis/teranonimisasi |
| Data Mining | eksplorasi pola data akademik agregat |
| NLP | korpus dokumen kampus, pipeline RAG |
| Interaksi Manusia–Komputer | user study antarmuka advising/asisten belajar |
| Proyek Perangkat Lunak | prototype sistem advising/asisten |
| Etika Profesi | kebijakan penggunaan AI, studi kasus integritas |
| Metodologi Penelitian | Research Pack yang menjadi objek studi sistem sendiri |
