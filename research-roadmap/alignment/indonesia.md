# Alignment — Indonesia (Prioritas Nasional yang Relevan)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [STR-04 Alignment Map](../../research-os/01-strategic-foundation/04-alignment-map.md) · [AIR-05 Demand–Supply Marketplace](../../research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md) · [alignment/uai.md](uai.md) · [alignment/global.md](global.md)

Dokumen ini memetakan arah roadmap ke **prioritas nasional Indonesia secara generik**. Ia sengaja **tidak mengutip regulasi, nomor peraturan, nama program, atau target angka pemerintah**, karena hal-hal itu berubah dan harus dipetakan ke dokumen kebijakan resmi terkini pada setiap roadmap review. Yang tetap adalah arah besarnya: Indonesia membutuhkan AI yang bekerja dalam bahasa dan konteksnya sendiri, dibuat oleh talenta lokal, dan memberi manfaat pada layanan publik, ekonomi rakyat, kesehatan, pendidikan, dan industri halal.

> **Catatan.** Petakan setiap baris di bawah ke dokumen kebijakan resmi terkini (strategi AI nasional, rencana pembangunan, kebijakan sektoral, peta jalan halal, kebijakan data pribadi) dan catat rujukannya di kolom terakhir saat roadmap review. `[isi: rujukan resmi]`.

## 1. Prioritas nasional → implikasi untuk roadmap UAI → klaster/domain

| Prioritas nasional (generik) | Implikasi untuk roadmap 2026–2030 | Klaster/domain terkait | Rujukan resmi |
|---|---|---|---|
| **Transformasi digital** layanan publik dan ekonomi | Riset tentang apa yang benar-benar bekerja saat AI diterapkan di layanan publik dan usaha kecil; evaluasi lapangan, bukan hanya prototype | C4, C2; [government](../domains/government.md), [business](../domains/business.md) | `[isi]` |
| **Talenta digital / AI** | Pipeline Metopen → TA → riset dosen sebagai mesin talenta; AI literacy dan AI Research Competency sebagai objek riset sendiri | C3; [education](../domains/education.md) | `[isi]` |
| **Bahasa Indonesia dan bahasa daerah** dalam teknologi | Korpus, benchmark, dan evaluasi model untuk bahasa Indonesia dan daerah (low-resource) sebagai kontribusi ilmiah utama C1; `program-indonesian-llm` 2029 | C1; [social-impact](../domains/social-impact.md), semua domain berteks | `[isi]` |
| **Industri dan jaminan produk halal** | Verifikasi, ekstraksi informasi, knowledge graph, traceability; `program-ai-halal` 2028 | C4, C1, C2; [halal](../domains/halal.md) | `[isi]` |
| **Kesehatan** masyarakat dan layanan primer | Skrining dini, NLP teks kesehatan berbahasa Indonesia, keamanan chatbot kesehatan; `program-ai-health` 2028 dengan tata kelola data ketat | C4, C1, C3; [health](../domains/health.md) | `[isi]` |
| **Pendidikan** bermutu dan merata | AI dalam pendidikan tinggi (advising, asisten belajar, integritas), pendidikan kelompok marginal | C3, C4; [education](../domains/education.md), [social-impact](../domains/social-impact.md) | `[isi]` |
| **Layanan publik** yang responsif dan adil | RAG regulasi, klasifikasi pengaduan, fairness keputusan otomatis, keamanan sistem | C1, C2, C3; [government](../domains/government.md) | `[isi]` |
| **UMKM dan ekonomi rakyat** (termasuk ekonomi syariah) | Alat berbiaya rendah, MLOps minimum, akses pembiayaan yang adil | C4, C2, C3; [business](../domains/business.md) | `[isi]` |
| **Ketahanan pangan** dan pengurangan susut | Sensor/IoT, citra, prediksi susut untuk pelaku pangan kecil | C4, C2; [food](../domains/food.md) | `[isi]` |
| **Perlindungan data pribadi** dan AI yang bertanggung jawab | Klasifikasi PUBLIC/INTERNAL/RESTRICTED, kartu dataset, protokol etik; riset privasi dan fairness dalam konteks lokal | C3, C2; [SECURITY.md](../../SECURITY.md) | `[isi]` |
| **Inklusi**: disabilitas, daerah tertinggal, kelompok rentan | Aksesibilitas AI berbahasa Indonesia; sistem low-resource; co-design komunitas | C3, C4; [social-impact](../domains/social-impact.md) | `[isi]` |
| **Kebencanaan dan lingkungan** | Triase informasi bencana, analitik lingkungan kampus/kota | C1, C2, C4; [social-impact](../domains/social-impact.md) | `[isi]` |

## 2. Cara membaca tabel

- **Kolom implikasi** menyatakan apa yang roadmap lakukan *karena* prioritas itu, bukan klaim bahwa UAI menjalankan program pemerintah.
- **Satu riset boleh menyentuh beberapa baris**; catat baris utama di Research One-Pager bagian *why it matters* untuk memudahkan pelaporan hibah dan alignment.
- Bila prioritas nasional berubah, ubah kolom implikasi lewat PR pada roadmap review; jangan mengubah sel matriks secara diam-diam.

## 3. Dari prioritas ke pasar riset (demand side)

Dalam model demand–supply ([AIR-05](../../research-os/03-ai-research-ecosystem/05-research-demand-supply-marketplace.md)), prioritas nasional adalah salah satu sumber **demand** bersama industri, pemerintah, UAI, dan masyarakat. Roadmap menerjemahkannya menjadi sel matriks; backlog menampung masalah konkret; klaster menyediakan supply (dosen, mahasiswa, mata kuliah, dataset). Prioritas nasional yang tidak memiliki satu pun masalah konkret di backlog selama dua semester ditandai sebagai *demand tanpa supply* dan dibahas pada roadmap review.

## 4. Bagaimana riset mahasiswa mengutip prioritas nasional dengan jujur

Amanah epistemik berlaku juga di sini. Dalam Problem Brief dan proposal:

1. Sebutkan prioritas secara **spesifik dan terverifikasi** (dokumen, tahun) — bukan "sesuai program pemerintah" tanpa rujukan.
2. Jelaskan **keputusan siapa yang berubah** bila riset berhasil; prioritas nasional bukan pengganti pemangku kepentingan nyata.
3. Jangan mengklaim dampak nasional dari pilot satu kampus; batasi klaim sesuai bukti (G7).
4. Rujukan yang ditemukan lewat AI wajib diverifikasi keberadaannya ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)).

## 5. Daftar verifikasi pada roadmap review

- [ ] Setiap baris tabel §1 memiliki rujukan resmi terkini di kolom terakhir.
- [ ] Baris yang tidak lagi relevan dihapus atau ditandai; baris baru ditambah dengan implikasi yang jelas.
- [ ] Setiap sel matriks aktif memiliki minimal satu baris prioritas nasional dan satu tema Renstra ([uai.md](uai.md)).
