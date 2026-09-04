# Research Design Card

> **ID** TPL-08 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa Metopen/TA, mentor, dosen pengampu, red team W8, reviewer G5
> **Terkait** [OPS-03 G5 Method Ready](../06-execution-os/03-research-gates.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [MET-07 Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [TPL-09 Experiment Card](09-experiment-card.md) · [TPL-05 Dataset Registry](05-dataset-registry-template.md) · [TPL-01 One-Pager](01-research-one-pager-template.md)

## Cara pakai

Satu halaman metodologi yang menjawab: *bagaimana persisnya RQ dijawab, dan apa yang bisa membuat jawabannya salah?* Diisi tim pada W7 (setelah G4 lulus), disimpan sebagai `docs/research-design.md` di repositori riset, dan dipertahankan pada Design Defense / Red Team Review W8. Menjadi bukti wajib G5 Method Ready bersama Experiment Card ([TPL-09](09-experiment-card.md)) dan `docs/ethics.md`. Kartu ini diperbarui setelah pilot (G6) dan setelah analisis (G7) bila desain berubah; setiap perubahan dicatat di bagian riwayat. Uji utamanya: orang lain dapat menjalankan desain ini tanpa bertanya ke tim.

## Computing Research Methods Map (pilih satu utama, boleh satu pendukung)

| Metode | Cocok untuk pertanyaan | Bukti yang dihasilkan | Pembanding khas |
|---|---|---|---|
| Experiment (controlled) | "Apakah X menyebabkan/meningkatkan Y?" | efek terukur dengan kontrol | kondisi kontrol / baseline |
| Benchmarking | "Seberapa baik metode A vs B pada tugas T?" | tabel metrik pada dataset/benchmark tetap | baseline sederhana + SOTA yang direproduksi |
| Design science | "Artefak seperti apa yang menyelesaikan masalah P, dan seberapa baik?" | artefak + evaluasi terhadap kriteria | artefak/proses yang ada |
| Empirical SE study | "Bagaimana praktik/alat X memengaruhi kualitas/proses perangkat lunak?" | data proyek, repositori, pengembang | praktik saat ini |
| ML research | "Apakah model/fitur/data baru meningkatkan kinerja secara sah?" | metrik + ablation + error analysis | baseline, ablation |
| Simulation | "Bagaimana sistem berperilaku pada kondisi yang sulit diuji nyata?" | hasil simulasi + sensitivitas | skenario dasar |
| Survey | "Apa yang dipikirkan/dilakukan populasi P?" | respons terukur dari sampel | — (deskriptif) atau kelompok |
| User study | "Bagaimana manusia berinteraksi dengan/menilai sistem S?" | tugas, waktu, kesalahan, persepsi | sistem/alur pembanding |
| Case study | "Bagaimana dan mengapa X terjadi dalam konteks nyata C?" | deskripsi mendalam, triangulasi | — |
| Qualitative | "Apa makna/pola di balik pengalaman P?" | tema dari wawancara/observasi | — |

## Template (salin ke `docs/research-design.md`)

```markdown
# Research Design Card — [Research ID] · v[n] · [YYYY-MM-DD]

| Bagian | Isi |
|---|---|
| RQ / hipotesis | RQ1: [...] · RQ2: [...] · H1: [...] (dapat difalsifikasi) |
| Jenis metode | Utama: [dari Methods Map] · Pendukung: [...] · Alasan: [mengapa metode ini menghasilkan bukti yang dibutuhkan RQ] |
| Unit analisis | [apa yang diukur: model/run, dokumen, pengguna, tim, proyek, kasus] |
| Variabel / konstruk — independen | [yang dimanipulasi/dibandingkan] |
| Variabel / konstruk — dependen | [yang diukur; definisi operasional] |
| Variabel kontrol / confounder | [yang dijaga tetap atau dicatat] |
| Sampling / dataset | [populasi, cara memilih, ukuran, representativitas; Dataset ID; split] |
| Prosedur | 1. [...] 2. [...] 3. [...] (urutan yang dapat diulang orang lain) |
| Instrumen | [kuesioner, protokol wawancara, skrip evaluasi, benchmark, konfigurasi] |
| Analisis | [statistik/kualitatif; uji apa, ambang apa, ditetapkan sebelum data dilihat] |
| Validitas & threats — internal | [ancaman] → [mitigasi] |
| Validitas & threats — eksternal | [ancaman] → [mitigasi] |
| Validitas & threats — konstruk | [ancaman] → [mitigasi] |
| Validitas & threats — statistik/kesimpulan | [ancaman] → [mitigasi] |
| Etika | [data manusia? consent, anonimisasi, risiko, persetujuan etik; lihat docs/ethics.md] |
| Reproducibility plan | [kode, config, seed, environment, data/metadata, langkah eksekusi, siapa mereproduksi] |
| Riwayat perubahan | v1 [tanggal] [ringkas] · v2 [...] |
```

## Contoh terisi

| Bagian | Isi |
|---|---|
| RQ / hipotesis | RQ1: Apakah rekomendasi rencana studi dari asisten LLM+RAG memenuhi aturan prasyarat/SKS lebih baik daripada baseline rule-based? · RQ2: Bagaimana dosen wali menilai relevansi elektif dan kegunaan asisten? · H1: violation rate LLM+RAG ≤ rule-based · H2: skor relevansi LLM+RAG > rule-based |
| Jenis metode | Utama: design science (artefak asisten advising) dengan evaluasi benchmarking offline · Pendukung: user study kecil dengan dosen wali · Alasan: RQ1 butuh pembanding terkontrol pada kasus tetap; RQ2 butuh penilaian manusia |
| Unit analisis | RQ1: satu kasus advising (profil mahasiswa anonim + semester target) · RQ2: satu penilaian dosen wali per kasus |
| Variabel independen | Sistem: {rule-based baseline, LLM+RAG}; model LLM dan versi ditetapkan tetap |
| Variabel dependen | Constraint-violation rate (pelanggaran prasyarat/SKS per rencana); precision@5 relevansi elektif vs gold; skor kegunaan Likert 1–5 |
| Variabel kontrol | Kurikulum versi sama, kasus sama untuk kedua sistem, prompt tetap, temperature 0, jumlah rekomendasi = 5 |
| Sampling / dataset | 40 kasus advising sintetis (pilot) + 80 kasus dari DS-2026-001 (evaluasi); stratifikasi semester 3/5/7; split pilot/evaluasi ditetapkan sebelum run; gold label oleh 2 dosen wali |
| Prosedur | 1. Bekukan kurikulum & aturan → 2. Bangun baseline → 3. Bangun LLM+RAG → 4. Jalankan kedua sistem pada kasus → 5. Hitung metrik otomatis → 6. Dosen wali menilai 20 kasus acak (blind terhadap sistem) → 7. Analisis |
| Instrumen | Skrip evaluasi `src/eval/`; lembar penilaian dosen wali (Likert + komentar); protokol wawancara singkat 10 menit |
| Analisis | RQ1: bandingkan proporsi pelanggaran dengan interval kepercayaan bootstrap; RQ2: median skor + agreement antar penilai (Cohen's κ); ambang praktis: selisih ≥ 10 poin persen dianggap berarti — ditetapkan sebelum data |
| Threats — internal | Gold label subjektif → 2 penilai + κ; urutan penilaian → acak |
| Threats — eksternal | Satu prodi, satu kurikulum → klaim dibatasi ke konteks serupa; kasus sintetis → validasi dengan 80 kasus nyata |
| Threats — konstruk | "Relevansi elektif" ≠ "keputusan terbaik" → definisi operasional + triangulasi wawancara |
| Threats — statistik | n kecil; LLM nondeterministik → 3 run per kasus, laporkan variansi dan interval |
| Etika | Data transkrip restricted, consent tertulis, anonimisasi sebelum akses; dosen wali sebagai partisipan diberi informed consent; tidak ada keputusan akademik nyata diambil dari sistem |
| Reproducibility plan | `experiments/config.yaml`, seed 42, `requirements.txt`, skrip `run.sh`, model & versi dicatat, kasus sintetis dirilis; reproduksi oleh peer [Mahasiswa C] pada W10 |
| Riwayat perubahan | v1 2026-10-[dd] draft W7 · v2 2026-10-[dd] setelah red team: tambah 3 run per kasus, definisi operasional relevansi |

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Kecocokan metode–RQ | Alasan pemilihan metode menyebut bukti yang dibutuhkan RQ | Metode dipilih karena "biasa dipakai" |
| Variabel | Definisi operasional terukur; kontrol disebut | "Akurasi" tanpa cara hitung |
| Prosedur | Orang lain dapat menjalankan tanpa bertanya | "Dilakukan eksperimen" |
| Analisis | Uji/ambang ditetapkan sebelum data dilihat | Metrik dipilih setelah melihat hasil |
| Threats | Empat jenis, masing-masing ancaman + mitigasi | Daftar keterbatasan umum |
| Etika & data | Merujuk Dataset ID, consent, privasi | Tidak menyebut asal data |
