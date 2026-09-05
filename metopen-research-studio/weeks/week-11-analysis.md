# Week 11 — Analysis

> **Sprint** S11 · **Gate** G7 Claim Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-10-pilot.md) / [Week berikutnya →](week-12-contribution.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Eksperimen utama sudah dijalankan pada skala penuh, dan kami tahu di mana metode kami gagal."** Pilot yang lolos G6 dijalankan ulang sesuai desain yang dikunci di G5 (metrik dan prosedur tidak boleh berubah), hasilnya dirangkum dengan ketidakpastian antar seed/fold, dianalisis lewat error analysis pada kasus gagal, divisualisasikan secara jujur, dan dibandingkan *apple-to-apple* dengan angka literatur di synthesis matrix ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W11; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S11). Minggu ini G7 *dimulai*, belum ditutup: klaim resmi baru disusun di Week 12.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (perbandingan terhadap baseline, error analysis, ketidakpastian, effect size dan practical significance, visualisasi jujur), **60 menit studio** (menyusun tabel hasil vs baseline dengan variansi, lalu memilih 5–10 contoh gagal untuk error analysis; tim yang run utamanya masih berjalan mengerjakan latihan figur menyesatkan), **10 menit gate check** (tiap tim menunjukkan satu figur dan menyebut satu cara figur itu bisa menyesatkan pembaca). Ini sprint terberat kedua secara jam (22.5 jam) karena run skala penuh (OPS-097, 6 jam) memblokir hampir semua task lain — mulai run pada hari pertama sprint ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer).

## Concept (30 menit)

- **Baseline selalu terlihat.** Angka metode tanpa baseline di tabel/figur yang sama tidak bermakna; selisih terhadap baseline adalah hasil, bukan angka absolutnya.
- **Ketidakpastian adalah bagian dari hasil.** Laporkan rata-rata ± simpangan (atau interval) antar seed/fold, bukan hanya run terbaik; jika hanya satu run, katakan begitu.
- **Error analysis.** Kelompokkan kasus gagal (jenis input, kelas, panjang, sumber data) dan cari pola — di situlah "mengapa" ditemukan, bukan di angka agregat.
- **Uji statistik sederhana bila tepat.** Uji dan interval hanya bila asumsinya masuk akal; effect size dan *practical significance* sering lebih penting daripada p-value.
- **Visualisasi jujur.** Sumbu mulai dari nol bila bermakna, skala konsisten antar panel, baseline tergambar, tidak memilih run terbaik (cherry-picking), caption menyebut n dan seed.
- **Apple-to-apple.** Angka literatur hanya dibandingkan bila dataset, split, metrik, dan protokolnya sama; jika tidak, nyatakan "tidak sebanding" alih-alih memaksakan.
- **Hasil negatif adalah hasil.** Metode yang tidak mengalahkan baseline tetap dilaporkan; menyembunyikannya adalah pelanggaran amanah epistemik ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- **Setiap angka bisa ditelusuri** ke run tertentu: seed, konfigurasi, git hash, file log.

**Pertanyaan pemandu:** *Jika seseorang hanya melihat satu figur utama Anda, kesimpulan apa yang akan ia tarik — dan apakah datanya benar-benar mendukung kesimpulan itu?*

## Tasks

Semua task Sprint S11 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add main experiment summary with seed variance (UIAI-2026-001, OPS-098)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-096 | Ikuti sesi Analyzing & Visualizing Evidence | Latihan visualisasi | 2h | Membuat contoh figur menyesatkan untuk latihan (ditandai latihan) | Mahasiswa memperbaiki figur secara mandiri |
| OPS-097 | Jalankan eksperimen utama pada skala penuh sesuai desain | Hasil eksperimen utama | 6h | Membantu mendiagnosis error; tidak mengubah metrik atau prosedur | Tim memastikan metrik dan prosedur identik dengan yang dikunci di G5 |
| OPS-098 | Hitung ringkasan statistik dan ketidakpastian antar seed/fold | results/main/summary.csv | 3h | Menjelaskan pilihan uji statistik dan asumsinya; tim memilih dan memverifikasi | Dosen memeriksa ketidakpastian dilaporkan, bukan hanya angka terbaik |
| OPS-099 | Lakukan error analysis pada kasus gagal | results/analysis.md bagian Error Analysis | 3h | Membantu mengelompokkan kesalahan; label akhir oleh manusia | Tim memeriksa contoh kesalahan tidak memuat data pribadi |
| OPS-100 | Buat visualisasi bukti yang jujur (figur final) | figures/main/*.png + caption | 2h | Membantu kode plotting; tim memeriksa kejujuran visual | Peer memeriksa figur tidak menyesatkan |
| OPS-101 | Bandingkan hasil dengan literatur di synthesis matrix | results/analysis.md bagian Comparison with Literature | 2h | Membantu menyusun tabel; angka literatur diverifikasi ke matriks | Tim memastikan perbandingan apple-to-apple atau dinyatakan tidak sebanding |
| OPS-102 | Tulis draft results/analysis.md | results/analysis.md v0 | 3h | Mengkritik kejelasan dan mendeteksi klaim tanpa rujukan tabel | Dosen memeriksa hasil negatif dilaporkan |
| OPS-103 | Perbarui AI Usage Log dan jurnal mingguan W11 | AI Usage Log W11 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |
| OPS-104 | Arsipkan hasil, log, dan konfigurasi eksperimen utama | experiments/main/README.md | 1h | - | Tim memeriksa tautan tabel ke run lengkap |

**Total effort: 22.5h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: mulai OPS-097 (run skala penuh) segera setelah sesi, karena OPS-098 → OPS-099/OPS-100/OPS-101 → OPS-102 semuanya menunggu hasilnya; OPS-096 (latihan) dan OPS-103 (log/jurnal) dapat dikerjakan sambil menunggu run; OPS-104 (arsip) dilakukan begitu OPS-098 selesai ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

## Deliverable

| Artefak | Lokasi di repositori riset | Bukti |
|---|---|---|
| Hasil eksperimen utama (semua run, seed, konfigurasi, log) | `experiments/main/`, `results/main/*.json`, `experiments/main/README.md` | commit + tautan dari tabel ringkasan ke run |
| Ringkasan statistik & ketidakpastian | `results/main/summary.csv` | commit; kolom mean/std (atau interval) per metrik |
| Error analysis pada kasus gagal | `results/analysis.md` §Error Analysis | commit; contoh tidak memuat data pribadi |
| Figur final + caption | `figures/main/*.png` (+ skrip pembuatnya di `src/report.py`) | commit; peer check tercatat |
| Perbandingan dengan literatur | `results/analysis.md` §Comparison with Literature | commit; setiap angka literatur menunjuk baris synthesis matrix |
| Draft analisis | `results/analysis.md` v0 | commit |
| AI Usage Log + jurnal | `docs/AI-USAGE.md`, `docs/journal/w11.md` | commit |

Struktur lengkap repositori riset: [TPL-15](../../research-os/08-templates/15-research-repository-template.md); komponen Research Pack yang mulai terisi minggu ini: Pilot Experiment → hasil, Threats to Validity (catatan awal v2) ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md)).

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Membuat contoh figur yang menyesatkan untuk latihan, dengan tanda "latihan" (OPS-096).
- Membantu mendiagnosis error saat run skala penuh — tanpa mengubah metrik atau prosedur (OPS-097).
- Menjelaskan pilihan uji statistik dan asumsinya; tim yang memilih dan memverifikasi (OPS-098).
- Membantu mengelompokkan kesalahan pada error analysis; label akhir tetap oleh manusia (OPS-099).
- Membantu kode plotting; kejujuran visual diperiksa tim (OPS-100).
- Membantu menyusun tabel perbandingan; angka literatur diverifikasi ke synthesis matrix (OPS-101).
- Mengkritik kejelasan draft analisis dan mendeteksi klaim tanpa rujukan tabel (OPS-102).

Tidak boleh:

- Menerima angka, tabel, atau "hasil" dari AI yang tidak dihitung dari run tim sendiri.
- Membiarkan AI "menginterpretasi" hasil tanpa tim memeriksa datanya langsung.
- Mengubah metrik, split, atau prosedur di tengah eksperimen atas saran AI (itu *metric switching* — lihat [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- Memasukkan contoh kasus gagal yang memuat data pribadi ke layanan AI ([SECURITY](../../SECURITY.md)).

## Human Check

- **Tim**: metrik dan prosedur identik dengan yang dikunci di G5 (OPS-097); setiap angka di tabel menunjuk run lengkap (OPS-104); perbandingan literatur apple-to-apple atau dinyatakan tidak sebanding (OPS-101); contoh kesalahan bebas data pribadi (OPS-099).
- **Peer**: satu figur utama diperiksa — bisakah menyesatkan? (OPS-100).
- **Dosen**: ketidakpastian dilaporkan, bukan hanya angka terbaik (OPS-098); hasil negatif dilaporkan (OPS-102); satu figur dicek terhadap data mentahnya.
- **Setiap anggota**: entri AI Usage Log miliknya sendiri (OPS-103).

## Done When

Minggu ini belum menutup gate; G7 Claim Ready ditutup di [Week 12](week-12-contribution.md). Sprint selesai bila:

- [ ] Eksperimen utama selesai pada skala penuh dengan metrik dan prosedur yang sama seperti G5, minimal 3 seed/fold.
- [ ] `results/main/summary.csv` memuat ketidakpastian (std/interval) per metrik, dan setiap baris tertelusur ke run (seed, git hash).
- [ ] `results/analysis.md` v0 memuat Error Analysis dan Comparison with Literature; hasil negatif ikut dilaporkan.
- [ ] 2–4 figur final di `figures/main/` lolos peer check "tidak menyesatkan", masing-masing dengan caption yang menyebut n dan seed.
- [ ] `experiments/main/README.md` menjelaskan cara mereproduksi setiap angka di tabel.
- [ ] Threats to Validity baru yang muncul dari data dicatat sebagai bahan v2 (dituntaskan Week 12).
- [ ] AI Usage Log dan `docs/journal/w11.md` diperbarui oleh setiap anggota.

## Templates & rujukan

- Template: [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) (bagian hasil aktual), [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md), [TPL-15 Research Repository](../../research-os/08-templates/15-research-repository-template.md).
- Konsep: [MET-03 §W11](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md), [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md), [AIX-01 Meta-Thinking — evidence literacy & causal/statistical reasoning](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md), [AIX-03 AI Across Value Stream — Analysis](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md), [OPS-02 §S11](../../research-os/06-execution-os/02-weekly-sprints.md), [OPS-03 G7](../../research-os/06-execution-os/03-research-gates.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).

## Jebakan minggu ini

1. **Mengklaim kausalitas dari korelasi.** "Fitur X menyebabkan akurasi naik" hanya dari perbandingan dua konfigurasi. Tulis apa yang teramati, bukan mekanisme yang belum diuji.
2. **Cherry-picking seed atau run.** Melaporkan run terbaik sebagai "hasil". Laporkan semua run dan ketidakpastiannya; jika satu run berbeda jauh, itu bahan error analysis.
3. **Visualisasi menyesatkan.** Sumbu dipotong, baseline dihilangkan, skala berbeda antar panel. Uji setiap figur dengan pertanyaan pemandu di atas.
4. **Mengubah metrik setelah melihat hasil.** Ini *metric switching*; metrik dikunci di G5. Bila memang perlu metrik tambahan, laporkan keduanya dan jelaskan alasannya.
5. **Mengabaikan hasil negatif.** Metode yang kalah dari baseline tetap dilaporkan — justru itu bukti yang paling jarang dan paling berguna bagi riset berikutnya.
