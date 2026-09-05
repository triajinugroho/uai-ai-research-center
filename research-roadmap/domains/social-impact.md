# Domain — Social Impact (Dampak Sosial, Komunitas & Lingkungan)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [Roadmap 2026–2030](../2026-2030/README.md) · [C1 AI Models, Data & Knowledge](../clusters/ai-models-data-knowledge.md) · [C3 Human-Centered & Responsible AI](../clusters/responsible-human-ai.md) · [C4 Applied AI](../clusters/applied-ai.md) · [alignment/uai.md](../alignment/uai.md)

| Field | Nilai |
|---|---|
| Topic GitHub | `social-impact` |
| Program | belum ada program tersendiri sampai 2030; topik bahasa daerah masuk `program-indonesian-llm` (2029); topik inklusi masuk `program-responsible-ai` |
| Klaster utama | C4 (filantropi, komunitas, lingkungan), C1 (bahasa daerah, low-resource NLP), C3 (inklusi, aksesibilitas), C2 (sistem low-resource untuk bencana) |
| Prioritas roadmap | sel C3/C1 × Social Impact 2027; C4 × Social Impact 2029 |

## 1. Mengapa domain ini untuk UAI

Misi prodi menyebut lulusan sebagai **agent of change** dan landasan spiritual-moral-etika Islami (sumber: dokumen diskusi; verifikasi). Domain ini adalah tempat misi itu diuji secara empiris: apakah AI yang kami buat memberi manfaat bagi komunitas yang paling membutuhkan — lembaga filantropi Islam (zakat, wakaf, sedekah), komunitas penutur bahasa daerah, penyandang disabilitas, korban bencana, dan lingkungan hidup. Domain ini juga menyediakan **masalah low-resource** yang justru menjadi kontribusi ilmiah bernilai: data kecil, bahasa minoritas, infrastruktur terbatas.

> **Catatan verifikasi.** Lembaga filantropi/komunitas mitra: `[isi]`. Prioritas nasional terkait (bahasa daerah, inklusi, bencana, lingkungan) dipetakan ke dokumen kebijakan resmi terkini saat roadmap review.

## 2. Problem space (masalah nyata)

1. Lembaga **zakat/wakaf/filantropi** menyalurkan bantuan dengan data penerima yang tersebar; prioritisasi dan pelaporan dampak lemah.
2. **Bahasa daerah** Indonesia sangat kurang terwakili dalam data dan model; layanan digital tidak menjangkau penuturnya.
3. **Aksesibilitas** layanan digital bagi penyandang disabilitas (netra, rungu) berbahasa Indonesia terbatas.
4. Informasi **bencana** dan tanggap darurat perlu diproses cepat dari teks/media sosial berbahasa Indonesia campur.
5. Komunitas dan lembaga sosial kekurangan kapasitas **analitik** untuk mengevaluasi program mereka.
6. **Misinformasi** yang menyasar komunitas keagamaan sulit diidentifikasi tanpa konteks budaya.
7. Data **lingkungan** lokal (sampah, air, energi kampus) tidak dianalisis; keberlanjutan kampus tanpa evidence.
8. Pendidikan bagi kelompok marginal (anak putus sekolah, pesantren kecil) kurang terlayani alat digital.
9. Relawan dan komunitas menghasilkan data (survei, foto, laporan) yang tidak terstruktur dan hilang.

## 3. Pemangku kepentingan dan calon partner

| Jenis | Peran |
|---|---|
| Lembaga amil zakat, nazir wakaf, yayasan sosial | pemilik masalah, data penerima (Confidential) |
| Komunitas penutur bahasa daerah, lembaga budaya | mitra korpus (consent komunitas) |
| Organisasi penyandang disabilitas | co-designer, evaluator aksesibilitas |
| Lembaga kemanusiaan/tanggap bencana | mitra sistem low-resource |
| Unit pengabdian masyarakat UAI, organisasi mahasiswa | jembatan ke komunitas |
| Fakultas Bahasa, Komunikasi, Psikologi, Hukum di UAI | mitra lintas fakultas (verifikasi) |
| Pengelola fasilitas/lingkungan kampus | pemilik data lingkungan internal |

## 4. Data yang mungkin dan sensitivitasnya

| Data | Sensitivitas | Catatan |
|---|---|---|
| Data penerima bantuan | **Confidential** | kelompok rentan; tidak pernah di GitHub; agregasi ketat |
| Korpus bahasa daerah dari komunitas | Public setelah consent komunitas | lisensi disepakati dengan komunitas; atribusi |
| Teks media sosial publik tentang bencana | Public (teks) | hapus identitas; cek ketentuan platform |
| Rekaman/uji aksesibilitas dengan penyandang disabilitas | **Restricted** | consent, protokol etik |
| Data lingkungan kampus (sensor, meteran) | Internal | izin unit |
| Laporan program lembaga sosial | Restricted | perjanjian |

## 5. Contoh research questions

- Bagaimana kinerja model bahasa pada bahasa daerah tertentu dengan data sangat kecil, dan strategi transfer mana yang paling efektif? (C1)
- Apakah prioritisasi penyaluran bantuan berbasis data meningkatkan ketepatan sasaran dibanding praktik lembaga saat ini, tanpa mendiskriminasi kelompok tertentu? (C4 + C3)
- Antarmuka AI berbahasa Indonesia seperti apa yang benar-benar dapat diakses pengguna tunanetra, diukur lewat user study bersama mereka? (C3)
- Seberapa cepat dan akurat klasifikasi laporan bencana dari teks campur daerah dibanding triase manual relawan? (C1 + C2)
- Apakah dashboard analitik sederhana mengubah keputusan program lembaga sosial kecil, diukur enam bulan setelah adopsi? (C4, studi kasus)

## 6. Output dan dampak

| Output | Dampak |
|---|---|
| Korpus/benchmark bahasa daerah (`DS-*`) dengan lisensi komunitas | representasi bahasa minoritas dalam AI |
| Alat analitik/prioritisasi untuk lembaga filantropi | penyaluran lebih tepat, pelaporan dampak |
| Pedoman aksesibilitas AI berbahasa Indonesia (`ART-*`/brief) | layanan digital inklusif |
| Sistem triase laporan bencana low-resource | respons lebih cepat |
| Paper (low-resource NLP, ICTD, HCI, AI for social good) | posisi UAI: AI for human flourishing |

## 7. Risiko etika dan privasi khas domain

- **Kelompok rentan**: kesalahan sistem berdampak besar pada orang yang paling tidak berdaya; evaluasi harm dan mekanisme banding wajib.
- **Ekstraktivisme data**: mengambil korpus dari komunitas tanpa manfaat balik; sepakati kepemilikan dan lisensi bersama komunitas.
- **Stigma dan pelabelan** penerima bantuan; agregasi, tanpa skor individu yang dipublikasikan.
- **Paternalisme**: solusi tanpa co-design dengan komunitas; libatkan sejak G2.
- **Misinformasi**: sistem deteksi dapat menjadi alat sensor; batasi pada dukungan verifikasi manusia.

## 8. Mata kuliah yang bisa menyumbang research asset

| Mata kuliah | Research asset |
|---|---|
| NLP | korpus bahasa daerah; klasifikasi teks bencana |
| AI & Machine Learning | baseline low-resource; evaluasi transfer |
| Interaksi Manusia–Komputer | user study aksesibilitas; co-design komunitas |
| Proyek Perangkat Lunak | prototype dashboard lembaga sosial |
| Data Mining | analisis data lingkungan kampus |
| Etika Profesi | analisis dampak pada kelompok rentan |
| Kerja Praktik / pengabdian masyarakat | entry door Problem/Partner dari komunitas |
