# Domain — Government (Pemerintahan & Layanan Publik)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C1 AI Models, Data & Knowledge](../clusters/ai-models-data-knowledge.md) · [C2 AI Systems, Software & Security](../clusters/ai-systems-security.md) · [C3 Human-Centered & Responsible AI](../clusters/responsible-human-ai.md) · [alignment/indonesia.md](../alignment/indonesia.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `government` |
| Program | belum ada program tersendiri sampai 2030; dijalankan sebagai `proj-*`; topik regulasi/RAG berbagi dengan `program-ai-education` (dokumen kampus) |
| Klaster utama | C1 (RAG regulasi, klasifikasi pengaduan), C2 (keamanan chatbot layanan publik), C3 (fairness, transparansi), C4 (analisis kebijakan) |
| Prioritas roadmap | sel **C1 × Government** dibuka 2026 lewat dokumen/regulasi kampus (proxy layanan publik); mitra instansi 2028+ |

## 1. Mengapa domain ini untuk UAI

Layanan publik di Indonesia sedang bertransformasi digital dan membutuhkan bukti tentang apa yang bekerja — terutama untuk **teks berbahasa Indonesia** (regulasi, pengaduan, formulir). UAI berada di Jakarta, dekat dengan instansi pusat dan daerah, dan kampus sendiri adalah "pemerintahan kecil": memiliki regulasi, prosedur, pengaduan, dan layanan. Masalah kampus menjadi **proxy berisiko rendah** untuk masalah layanan publik, sehingga metode dapat dimatangkan sebelum bekerja dengan instansi.

> **Catatan verifikasi.** Dokumen ini tidak mengutip regulasi atau program pemerintah tertentu. Petakan ke dokumen kebijakan resmi terkini saat roadmap review. Mitra instansi: `[isi]`; ketersediaan Fakultas Hukum/Ekonomi UAI sebagai mitra: `[isi]`.

## 2. Problem space (masalah nyata)

1. **Regulasi dan prosedur** sulit dicari dan dipahami warga/pegawai; pertanyaan berulang membebani layanan.
2. **Pengaduan publik** dalam bahasa Indonesia campur daerah harus diklasifikasikan dan diprioritaskan manual.
3. Chatbot layanan publik rentan **memberi informasi salah** dan terhadap prompt injection.
4. Keputusan otomatis (penyaringan bantuan, antrean) berisiko **tidak adil** dan tidak transparan.
5. Dokumen kebijakan panjang jarang dianalisis secara sistematis (peringkasan, ekstraksi kewajiban).
6. Data layanan publik terbuka jarang dimanfaatkan karena kualitasnya beragam.
7. Pegawai kekurangan literasi AI untuk mengawasi sistem yang mereka pakai.
8. Layanan kampus (surat, izin, pengaduan mahasiswa) menghadapi masalah serupa dalam skala kecil.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| Unit layanan/administrasi kampus | pemilik masalah proxy, pengguna awal |
| Instansi pemerintah daerah/pusat, unit layanan publik | mitra masalah dan data (2028+, perjanjian) |
| Pegawai layanan publik | partisipan user study, evaluator |
| Warga/mahasiswa sebagai pengguna layanan | partisipan |
| Fakultas Hukum, Ekonomi, Komunikasi di UAI | pakar regulasi, kebijakan, komunikasi publik (verifikasi) |
| Organisasi masyarakat sipil yang mengawasi layanan publik | mitra evaluasi transparansi |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Teks regulasi/peraturan publik | Public | cek sumber resmi; versi dan tanggal dicatat |
| Dokumen dan prosedur kampus | Internal/Public | izin unit; hindari data pribadi di dalam dokumen |
| Pengaduan publik | **Restricted** | berisi data pribadi; anonimisasi; perjanjian |
| Data layanan publik terbuka (statistik) | Public | catat kualitas dan keterbatasan |
| Log chatbot layanan | Restricted | agregasi |
| Survei pegawai/warga | Restricted | consent |

## 5. Contoh research questions

- Seberapa akurat dan seberapa sering "halusinasi" jawaban RAG atas regulasi kampus berbahasa Indonesia dibanding pencarian kata kunci, dinilai pakar? (C1) — lihat [UIAI-2026-002](../../research-backlog/problems/UIAI-2026-002-indonesian-rag-evaluation.md).
- Model klasifikasi pengaduan mana yang cukup baik untuk teks berbahasa Indonesia campur daerah, dan bagaimana kinerjanya per daerah/kelompok? (C1 + C3)
- Seberapa rentan chatbot layanan publik berbahasa Indonesia terhadap prompt injection, dan guardrail mana yang efektif tanpa merusak kegunaan? (C2)
- Penjelasan apa yang diperlukan pegawai untuk mengawasi keputusan prioritisasi otomatis, dan apakah penjelasan itu mengubah keputusan mereka? (C3)
- Apakah peringkasan otomatis dokumen kebijakan mempertahankan kewajiban hukum yang penting, diukur dengan protokol anotasi pakar? (C1 + C4)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Benchmark RAG regulasi berbahasa Indonesia (`DS-*`) | standar evaluasi asisten layanan publik |
| Suite keamanan chatbot layanan publik (`ART-*`) | sistem lebih aman sebelum deployment |
| Prototype klasifikasi/prioritisasi pengaduan | respon layanan lebih cepat |
| Paper (NLP, security, HCI, e-government) | posisi UAI di riset layanan publik digital |
| Research brief untuk instansi | rekomendasi adopsi berbasis bukti |

## 7. Risiko etika dan privasi khas domain

- **Keadilan**: sistem prioritisasi dapat merugikan kelompok tertentu; audit fairness dan manusia sebagai pengambil keputusan.
- **Data pengaduan** memuat identitas dan keluhan sensitif; Restricted, anonimisasi ketat.
- **Kesalahan informasi hukum** dapat merugikan warga; sistem harus mengutip sumber dan versi regulasi.
- **Kepentingan politik**: hindari riset yang dapat disalahgunakan untuk surveillance atau propaganda; nilai risiko di G2.
- **Ketergantungan** pada layanan AI eksternal untuk data publik sensitif — dilarang tanpa perjanjian.

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| NLP | korpus regulasi; pipeline RAG; klasifikasi pengaduan |
| AI & Machine Learning | baseline klasifikasi teks |
| Pengujian Perangkat Lunak | harness pengujian keamanan chatbot |
| Rekayasa Perangkat Lunak | analisis kebutuhan layanan publik |
| Interaksi Manusia–Komputer | user study pegawai/warga |
| Etika Profesi | analisis fairness dan transparansi keputusan otomatis |
