# UIAI-2026-001 — AI-Assisted Academic Advising for Indonesian Universities

> **Status** Draft v0.1 (2026-09) · **contoh ilustratif** · **Terkait** [BACKLOG.md](../BACKLOG.md) · [TPL-04](../../research-os/08-templates/04-research-backlog-template.md) · [Domain Education](../../research-roadmap/domains/education.md) · [C3 Human-Centered & Responsible AI](../../research-roadmap/clusters/responsible-human-ai.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md)

| Field | Nilai |
|---|---|
| **Research ID** | UIAI-2026-001 |
| **Judul** | AI-assisted academic advising for Indonesian universities |
| **Cluster** | C3 Human-Centered & Responsible AI (primer) · C4 Applied AI (sekunder) — label `cluster:human-ai` |
| **Domain** | Education |
| **Problem owner** | `[isi: dosen wali / unit layanan akademik UAI]` |
| **Potential dataset** | [DS-2026-001 Student Learning](../../datasets-registry/datasets/DS-2026-001-student-learning.md) (Restricted; anonimisasi + consent) |
| **Research maturity** | Idea |
| **Related courses** | AI & Machine Learning; Metodologi Penelitian; pendukung: Interaksi Manusia–Komputer, Etika Profesi |
| **Potential output** | TA; paper (computing education / HCI); prototype dashboard dosen wali |
| **Priority** | P1-high |
| **Entry door** | Problem |
| **Issue** | `#[isi]` |

## Problem statement

Dosen wali di perguruan tinggi Indonesia mendampingi puluhan mahasiswa dengan data yang tersebar (nilai, SKS, kehadiran) dan waktu yang terbatas. Mahasiswa berisiko (nilai menurun, beban SKS tidak wajar, keterlambatan studi) sering terdeteksi setelah masalah membesar. Di sisi lain, alat berbasis AI berpotensi memberi peringatan dini dan rekomendasi, tetapi belum diketahui apakah rekomendasi semacam itu **dipercaya, dipakai, dan mengubah tindakan** dosen wali — serta bagaimana menjaganya agar tidak menjadi alat pelabelan mahasiswa.

## Why it matters / stakeholder

| Pemangku kepentingan | Keputusan yang berubah bila riset berhasil |
|---|---|
| Dosen wali | kapan dan kepada siapa melakukan intervensi lebih awal |
| Mahasiswa | menerima dukungan sebelum masalah membesar; hak untuk memahami dan menolak rekomendasi |
| Unit layanan akademik / prodi | alokasi sumber daya pendampingan; kebijakan penggunaan AI dalam advising |

Riset ini juga menjadi contoh sel **C3 × Education** yang diprioritaskan roadmap 2026–2027 karena masalah, data, dan pemangku kepentingan ada di dalam kampus.

## What we know

Ringkasan awal (bukan tinjauan pustaka): sistem early warning dan learning analytics telah banyak dikaji di luar negeri; laporan tentang penerapan di perguruan tinggi Indonesia lebih sedikit; isu explainability dan kepercayaan dosen terhadap rekomendasi otomatis adalah tema yang muncul dalam literatur HCI-AI. **Literatur awal: `[isi saat G3]`** — synthesis matrix 15–25 sumber terverifikasi wajib sebelum RQ dianggap valid.

## Candidate research questions

1. Seberapa akurat model early warning berbasis data akademik semester 1–4 dibanding aturan sederhana (mis. ambang IPK/SKS) yang dipakai dosen wali saat ini?
2. Penjelasan (explanation) seperti apa pada rekomendasi advising yang meningkatkan kepercayaan terkalibrasi dosen wali, diukur lewat user study?
3. Apakah dosen wali mengubah tindakan (frekuensi/jenis intervensi) setelah memakai prototype selama satu semester dibanding semester sebelumnya?

## Possible data & sensitivity

| Data | Sumber | Sensitivitas | Syarat |
|---|---|---|---|
| Rekam akademik teranonimisasi (nilai, SKS, kehadiran) | unit akademik UAI | **Restricted** | pseudonimisasi, kunci di luar repo, izin unit, consent mahasiswa |
| Wawancara/survei dosen wali | dikumpulkan sendiri | Restricted | protokol etik, consent |
| Log penggunaan prototype | dikumpulkan sendiri | Restricted | agregasi |
| Data sintetis untuk pengembangan awal | dibuat tim | Public | dicatat sebagai sintetis |

Aturan: [SECURITY.md](../../SECURITY.md); kartu dataset diisi sebelum G5.

## Candidate mentor

`[isi: dosen dengan kepakaran learning analytics / HCI / ML]` — lihat [AIR-03](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md).

## Risks

| Risiko | Mitigasi |
|---|---|
| Akses data akademik tertunda | mulai dengan data sintetis dan wawancara; pilot pada satu angkatan/prodi |
| Profiling dan diskriminasi mahasiswa | audit fairness per kelompok; sistem hanya pendukung keputusan; mahasiswa dapat melihat dan menolak |
| Dosen wali tidak memakai prototype | libatkan sejak desain (co-design); ukur kegunaan, bukan hanya akurasi |
| Klaim kausal dari korelasi (mis. "intervensi menurunkan risiko") | desain quasi-experiment dengan pembanding; threats to validity eksplisit |
| Bocornya data ke layanan AI eksternal | dilarang; analisis lokal |

## Next evidence

Untuk naik dari Idea ke G2 Problem Ready dengan tim: **Problem Brief** dari wawancara minimal 3 dosen wali + 1 unit akademik, pernyataan pemangku kepentingan, dan konfirmasi jalur akses data (siapa memberi izin, dalam bentuk apa).
