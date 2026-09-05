# Examples — Contoh Terisi Riset Ilustratif UIAI-2026-001

> **Status** Draft v0.1 (2026-09) · **Contoh ilustratif; data `[isi]`.** Semua angka, nama, dan sumber di halaman ini adalah ilustrasi untuk menunjukkan *bentuk* artefak yang lolos gate, bukan hasil riset nyata. Sitasi ditulis sebagai placeholder dan **wajib diganti setelah DOI/URL diverifikasi**.
> **Terkait** [Studio README](../README.md) · [templates](../templates/README.md) · [Kartu masalah UIAI-2026-001](../../research-backlog/problems/UIAI-2026-001-ai-assisted-academic-advising.md) · [DS-2026-001 Student Learning](../../datasets-registry/datasets/DS-2026-001-student-learning.md) · [TPL-01](../../research-os/08-templates/01-research-one-pager-template.md) · [TPL-08](../../research-os/08-templates/08-research-design-card.md) · [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) · [method-review.md](../../.github/PULL_REQUEST_TEMPLATE/method-review.md)

Riset ilustratif yang dipakai di seluruh repositori: **UIAI-2026-001 — AI-assisted academic advising for Indonesian universities**, klaster **C3 Human-Centered & Responsible AI** (sekunder C4), domain **Education**, entry door **Problem**. Contoh yang sama dipakai di `research-os/08-templates/` dan `research-backlog/problems/`, sehingga Anda bisa melihat satu riset yang sama bergerak dari kartu backlog (Idea) → One-Pager v1 (G4) → Design Card (G5) → PR gate.

## (a) Research One-Pager v1 — format TPL-01, bukti G4 Question Ready (W6)

`docs/one-pager.md` — v1 · 2026-10-[dd]. Field yang belum wajib pada v1 ditulis `[belum diisi — target v2]`.

| Field | Isi |
|---|---|
| Research ID | UIAI-2026-001 |
| Judul kerja | AI-assisted academic advising for Indonesian universities |
| Tim | [Mahasiswa A] (@[isi]), [Mahasiswa B] (@[isi]) |
| Mentor | [Dosen C3] — C3 Human-Centered & Responsible AI · Domain: Education |
| Entry door | Problem (problem owner: Kaprodi / dosen wali — `[isi]`) |
| Endgame | Minimum: TA Ready · Target: Research Ready · Aspirasi: paper konferensi nasional + dataset anonim rencana studi |
| Problem & why it matters | Dosen wali menangani puluhan mahasiswa dengan waktu konsultasi terbatas; mahasiswa memilih mata kuliah dengan informasi tidak lengkap sehingga terjadi pelanggaran prasyarat dan keterlambatan lulus. Asisten advising berbasis LLM menjanjikan bantuan, tetapi belum ada bukti terkontrol pada kurikulum Indonesia (OBE, prasyarat, paket semester). |
| Stakeholder | Mahasiswa, dosen wali, Kaprodi — keputusan yang berubah bila riset berhasil: rencana studi per semester dan alokasi waktu konsultasi dosen wali |
| What we know | 1. Sistem rekomendasi mata kuliah berbasis riwayat akademik meningkatkan akurasi prediksi nilai, tetapi jarang mengevaluasi validitas prasyarat ([Penulis, Tahun — isi setelah verifikasi DOI]; matriks M-03, M-07). 2. Asisten LLM untuk advising diuji terutama di universitas Amerika/Eropa dengan kurikulum fleksibel ([Penulis, Tahun — isi setelah verifikasi DOI]; M-12). 3. Kepercayaan pengguna terhadap saran AI akademik bergantung pada penjelasan dan kemampuan verifikasi ([Penulis, Tahun — isi setelah verifikasi DOI]; M-19). |
| Gap | Belum ada evaluasi terkontrol LLM+RAG vs baseline rule-based pada constraint kurikulum Indonesia (prasyarat, SKS, paket semester), dan belum ada pengukuran gabungan validitas rekomendasi + persepsi dosen wali — baris M-07, M-12, M-19 synthesis matrix. Jenis gap: empiris + kontekstual. |
| RQ / hipotesis | RQ1: Apakah rekomendasi rencana studi dari asisten LLM+RAG memenuhi aturan prasyarat/SKS lebih baik daripada baseline rule-based? · RQ2: Bagaimana dosen wali menilai relevansi elektif dan kegunaan asisten? · H1: tingkat pelanggaran constraint LLM+RAG ≤ rule-based (ditolak bila LLM+RAG melanggar lebih sering) · H2: skor relevansi elektif LLM+RAG > rule-based menurut dosen wali (ditolak bila median skor tidak lebih tinggi) |
| Contribution | Empiris + artefak: bukti terkontrol pertama pada konteks kurikulum Informatika UAI; benchmark 40 kasus advising sintetis; prototipe open-source — bermakna karena dosen wali dan Kaprodi memutuskan apakah asisten layak diuji coba nyata |
| Method | Draft: design science (artefak asisten) + benchmarking offline + user study kecil dosen wali — dikunci di W7 ([TPL-08](../../research-os/08-templates/08-research-design-card.md)) |
| Data | Draft: dokumen kurikulum (Public); transkrip anonim (Restricted, consent) — kandidat DS-2026-001; 40 kasus sintetis untuk pilot |
| Baseline | Draft: rule-based prerequisite checker + heuristik greedy per semester |
| Metrics | Draft: constraint-violation rate; precision@5 relevansi elektif vs gold dosen wali; skor kegunaan Likert 1–5 — dikunci di W7 |
| Threats to validity | [belum diisi — target v2] |
| Ethics / AI note | Data mahasiswa dianonimkan, consent tertulis, tidak masuk GitHub; AI dipakai untuk kata kunci pencarian, pra-baca paper, dan kritik rumusan RQ — log `docs/AI-USAGE.md` entri #1–#9 |
| Next evidence | Research Design Card v1 + Data Plan + dataset card — W7, 2026-10-[dd] |
| Gate saat ini | G4 Question Ready — Review — PR #[n] |

Mengapa ini lolos G4: setiap RQ menunjuk baris matriks tertentu; tiap hipotesis punya kondisi penolakan; kontribusi tidak melebihi apa yang RQ dapat buktikan; method/data/baseline/metrics masih *draft* dan diberi tanda — tidak mendahului G5.

## (b) Research Design Card — format TPL-08, bukti G5 Method Ready (W7–W8)

`docs/design-card.md` — v2 · 2026-10-[dd] (setelah red team W8); rincian tiap bagian di `docs/research-design.md`, data plan di `docs/data-plan.md`.

| Bagian | Isi |
|---|---|
| RQ / hipotesis | RQ1 dan RQ2 seperti One-Pager v1 · H1: violation rate LLM+RAG ≤ rule-based · H2: skor relevansi LLM+RAG > rule-based |
| Jenis metode | Utama: design science (artefak asisten advising) dengan evaluasi benchmarking offline · Pendukung: user study kecil dengan dosen wali · Alasan: RQ1 butuh pembanding terkontrol pada kasus tetap; RQ2 butuh penilaian manusia · Ditolak: survey mahasiswa saja (tidak menjawab validitas constraint) |
| Unit analisis | RQ1: satu kasus advising (profil mahasiswa anonim + semester target) · RQ2: satu penilaian dosen wali per kasus |
| Variabel independen | Sistem: {rule-based baseline, LLM+RAG}; model LLM dan versi ditetapkan tetap `[isi]` |
| Variabel dependen | Constraint-violation rate (pelanggaran prasyarat/SKS per rencana); precision@5 relevansi elektif vs gold; skor kegunaan Likert 1–5 |
| Variabel kontrol | Kurikulum versi sama; kasus sama untuk kedua sistem; prompt tetap; temperature 0; jumlah rekomendasi = 5 |
| Sampling / dataset | 40 kasus advising sintetis (pilot) + 80 kasus dari DS-2026-001 (evaluasi); stratifikasi semester 3/5/7; split pilot/evaluasi ditetapkan sebelum run; gold label oleh 2 dosen wali `[isi]` |
| Prosedur | 1. Bekukan kurikulum & aturan → 2. Bangun baseline → 3. Bangun LLM+RAG → 4. Jalankan kedua sistem pada kasus → 5. Hitung metrik otomatis → 6. Dosen wali menilai 20 kasus acak (blind terhadap sistem) → 7. Analisis |
| Instrumen | Skrip evaluasi `src/eval/`; lembar penilaian dosen wali (Likert + komentar); protokol wawancara singkat 10 menit |
| Analisis | RQ1: bandingkan proporsi pelanggaran dengan interval kepercayaan bootstrap · RQ2: median skor + agreement antar penilai (Cohen's κ) · Ambang praktis: selisih ≥ 10 poin persen dianggap berarti — ditetapkan sebelum data dilihat |
| Threats — internal | Gold label subjektif → 2 penilai + κ; urutan penilaian → diacak |
| Threats — eksternal | Satu prodi, satu kurikulum → klaim dibatasi ke konteks serupa; kasus sintetis → validasi dengan 80 kasus nyata |
| Threats — konstruk | "Relevansi elektif" ≠ "keputusan terbaik" → definisi operasional + triangulasi wawancara |
| Threats — statistik/kesimpulan | n kecil; LLM nondeterministik → 3 run per kasus, laporkan variansi dan interval |
| Etika | Transkrip Restricted: consent tertulis, anonimisasi sebelum akses, kunci di luar repo; dosen wali sebagai partisipan diberi informed consent; tidak ada keputusan akademik nyata diambil dari sistem; lihat `docs/ethics.md` |
| Reproducibility plan | `experiments/pilot-01/config.yaml`, seed 42, `requirements.txt`, `run.sh`; model & versi dicatat; kasus sintetis dirilis; reproduksi oleh peer [Mahasiswa C] pada W10 |
| Riwayat perubahan | v1 2026-10-[dd] draft W7 · v2 2026-10-[dd] setelah red team: tambah 3 run per kasus, definisi operasional relevansi, alternatif metode yang ditolak |

## (c) Cuplikan synthesis matrix — 5 dari 15–25 baris, `docs/literature/synthesis-matrix.csv` (G3)

Kolom mengikuti [MET-03 W4](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md). Sumber ditulis placeholder; kolom *Verified* diisi tanggal DOI/URL dibuka, *Quality* diisi setelah OPS-040.

| ID | Sumber | Problem | Metode | Data | Metrik | Hasil (ringkas) | Keterbatasan | Relevansi | Verified | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| M-03 | [Penulis, Tahun — isi setelah verifikasi DOI] | Rekomendasi mata kuliah dari riwayat akademik | Collaborative filtering / matrix factorization | Nilai mahasiswa satu universitas, n `[isi]` | RMSE prediksi nilai; precision@k | Prediksi nilai cukup akurat; prasyarat tidak dievaluasi | Satu institusi; tidak ada evaluasi constraint | Tinggi — pembanding untuk baseline | `[isi]` | `[isi]` |
| M-07 | [Penulis, Tahun — isi setelah verifikasi DOI] | Penyusunan rencana studi yang memenuhi prasyarat | Rule-based / constraint satisfaction | Kurikulum + transkrip, n `[isi]` | Violation rate; waktu penyusunan | Aturan terpenuhi; relevansi elektif rendah | Tidak ada studi pengguna | Tinggi — asal baseline rule-based (RQ1) | `[isi]` | `[isi]` |
| M-12 | [Penulis, Tahun — isi setelah verifikasi DOI] | Asisten advising berbasis LLM | LLM + RAG atas katalog mata kuliah | Kurikulum fleksibel universitas AS/Eropa | Akurasi jawaban; kepuasan pengguna | Jawaban relevan; halusinasi prasyarat dilaporkan | Kurikulum fleksibel, bukan paket semester; tanpa baseline rule-based | Tinggi — gap kontekstual (RQ1) | `[isi]` | `[isi]` |
| M-15 | [Penulis, Tahun — isi setelah verifikasi DOI] | Early warning mahasiswa berisiko | Klasifikasi risiko (learning analytics) | LMS + data akademik, n `[isi]` | AUC; F1 | Fitur awal semester prediktif | Tidak menyentuh rekomendasi rencana studi | Sedang — konteks stakeholder dosen wali | `[isi]` | `[isi]` |
| M-19 | [Penulis, Tahun — isi setelah verifikasi DOI] | Kepercayaan pada saran AI akademik | User study | Mahasiswa/dosen, n `[isi]` | Skor trust (Likert); keberhasilan tugas | Penjelasan meningkatkan kepercayaan terkalibrasi | n kecil; satu institusi | Tinggi — instrumen RQ2 | `[isi]` | `[isi]` |

Pola yang dibaca dari matriks penuh (ilustratif): **konsisten** — rekomendasi berbasis riwayat akademik akurat untuk nilai (M-03 dkk.); **bertentangan** — LLM relevan tetapi rawan halusinasi prasyarat (M-12) vs rule-based patuh tetapi tidak relevan (M-07); **belum diuji** — LLM+RAG vs rule-based pada kurikulum berpaket semester dengan penilaian dosen wali (M-07, M-12, M-19). Gap dan RQ pada (a) diturunkan dari ketiga baris terakhir ini.

## (d) Tiga entri AI Usage Log — format TPL-10, `docs/AI-USAGE.md`

| # | Date | Tool (versi) | Stage | Purpose | Prompt / use (ringkas) | Material output? | Verification (S / R / E) | Inclusion in final work | PJ |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 2026-09-[dd] | [LLM chat, model `[isi]`] | Search | Usulan referensi tambahan | "Sebutkan paper tentang LLM advising di Indonesia" | Tidak | S: 3 dari 4 referensi tidak ditemukan di Scholar/DOI → **dibuang**; 1 ditemukan dan dibaca penuh · R: — · E: — | Tidak (3 dibuang); 1 masuk `references.bib` sebagai M-12 setelah dibaca | [Mahasiswa A] |
| 7 | 2026-10-[dd] | [coding assistant `[isi]`] | Coding | Debugging parser output LLM | Tempel pesan error + fungsi parser (tanpa data mahasiswa; contoh input sintetis) | Ya | S: — · R: patch dibaca baris per baris; satu perubahan yang tidak perlu ditolak · E: unit test 12 kasus lulus (`tests/test_parse.py`) | Diubah — `src/eval/parse.py` commit `[hash]` | [Mahasiswa B] |
| 9 | 2026-10-[dd] | [LLM chat, model `[isi]`] | Method | Red team desain eksperimen sebelum W8 | "Bertindaklah sebagai reviewer skeptis: apa kelemahan desain berikut …" (Design Card v1 tanpa data) | Ya | S: — · R: 5 kritik dinilai tim; 2 diterima (nondeterminisme LLM → 3 run per kasus; gold label subjektif → 2 penilai + κ), 3 ditolak dengan alasan (mis. "tambah model kedua" — di luar ruang lingkup semester) · E: dicek terhadap baris M-12, M-19 | Diubah — Design Card v2 bagian Threats; notulen `docs/reviews/midterm-red-team.md` | [Mahasiswa A] |

Yang membuat log ini *Governor-grade*: ditulis pada hari yang sama; kolom verifikasi menyebut **apa yang dicek dan hasilnya** (bukan "sudah diverifikasi"); ada entri **ditolak** dengan alasan; tidak ada data mahasiswa di prompt; lokasi inclusion konkret (file/commit). Ringkasan AI Usage Statement di bagian atas `docs/AI-USAGE.md` diperbarui tiap gate; statement final untuk naskah dirakit di W13 ke `paper/AI-USAGE-STATEMENT.md`.

## (e) Contoh teks PR "GATE REVIEW: Method Ready" (singkat)

Template lengkap: [method-review.md](../../.github/PULL_REQUEST_TEMPLATE/method-review.md). Di bawah ini versi terisi ringkas — di PR sungguhan setiap bagian ditautkan ke file.

```markdown
# GATE REVIEW: Method Ready — `UIAI-2026-001`

| Field | Isi |
|---|---|
| Research ID | UIAI-2026-001 |
| Gate | G5 Method Ready |
| G4 Question Ready lulus (PR #) | #[n] (merged 2026-10-[dd]) |
| Branch | research/g5-method |
| Sprint / Minggu | S8 / W8 |
| Tim / Mentor | @[isi], @[isi] / @[isi] |
| Issue Research Question / Experiment | #[n] / #[n] |

## Research Question
RQ1 (M-07, M-12): apakah LLM+RAG memenuhi prasyarat/SKS lebih baik dari rule-based? — H1: violation rate LLM+RAG ≤ rule-based.
RQ2 (M-19): bagaimana dosen wali menilai relevansi elektif dan kegunaan? — H2: skor relevansi LLM+RAG > rule-based.

## Method — Research Design Card (TPL-08)
Design science + benchmarking offline (utama), user study kecil dosen wali (pendukung). Unit: kasus advising / penilaian dosen wali.
Kontrol: kurikulum sama, kasus sama, prompt tetap, temperature 0, top-5. Prosedur 7 langkah → docs/design-card.md v2 (rincian: docs/research-design.md).

## Dataset — Data Plan (docs/data-plan.md)
Kurikulum (Public). DS-2026-001 transkrip anonim (Restricted; consent; kartu dataset diajukan, PR datasets-registry #[n]).
40 kasus sintetis untuk pilot (Public, dirilis). Fallback bila akses transkrip tertunda: evaluasi pada kasus sintetis + wawancara dosen wali.

## Baseline
Rule-based prerequisite checker + heuristik greedy per semester — adil karena memakai aturan yang sama dengan yang dipakai dosen wali hari ini.

## Metrics
| Metrik | RQ | Prosedur evaluasi | Ambang praktis |
|---|---|---|---|
| Constraint-violation rate | RQ1 | split pilot/eval ditetapkan sebelum run; 3 run per kasus; bootstrap CI | selisih ≥ 10 poin persen |
| precision@5 relevansi elektif | RQ2 | gold label 2 dosen wali, κ dilaporkan | selisih ≥ 10 poin persen |
| Kegunaan (Likert 1–5) | RQ2 | 20 kasus acak, blind terhadap sistem | median ≥ 4 |

## Experiment Card pilot (TPL-09)
experiments/pilot-01/experiment-card.md (EXP-01) · subset: 40 kasus sintetis · seed 42 · experiments/pilot-01/config.yaml · requirements.txt

## Threats to Validity (v1, pra-eksperimen)
Internal: gold label subjektif → 2 penilai + κ · Eksternal: satu prodi → klaim dibatasi · Konstruk: relevansi ≠ keputusan terbaik → definisi operasional · Statistik: n kecil, LLM nondeterministik → 3 run, interval.

## Ethics & Privacy (awal)
Transkrip anonim, consent tertulis, kunci di luar repo; dosen wali informed consent; tidak ada data mahasiswa ke layanan AI (log #7, #9). Lengkap: docs/ethics.md.

## Mid-semester Research Pitch / Red Team (W8)
Slide: presentation/midterm-pitch.pdf · Notulen: docs/reviews/midterm-red-team.md (7 keberatan: 4 diterima, 2 ditolak dengan alasan, 1 ditunda ke TA)
Perubahan desain: 3 run per kasus; definisi operasional relevansi; alternatif metode yang ditolak dicatat.

## Evidence
| Bukti wajib G5 (OPS-03) | Link / path | Status |
|---|---|---|
| docs/design-card.md (Design Card v2) + docs/research-design.md | [link] | ada |
| Data Plan + dataset card DS-2026-001 | docs/data-plan.md; datasets-registry PR #[n] | diajukan |
| experiments/pilot-01/experiment-card.md | [link] | pra-registrasi terisi |
| docs/ethics.md | [link] | ada |
| Slide pitch + notulen red team | presentation/, docs/reviews/ | ada |

## AI Usage
docs/AI-USAGE.md entri #1–#12; red team AI (#9): 2 dari 5 kritik diterima; tidak ada referensi AI tanpa verifikasi (#6: 3 dibuang).

## Integritas
- [x] Metrik dan baseline ditetapkan sebelum eksperimen (EXP-01 pra-registrasi)
- [x] Tidak ada data mentah/pribadi di PR ini
- [x] Semua referensi yang disebut ada di references.bib dan sudah dibuka
```

Merge PR ini berarti G5 lulus → release `v0.3 Research Design` → status **TA Ready** → lanjut [Week 09 — Repository](../weeks/week-09-repository.md).
