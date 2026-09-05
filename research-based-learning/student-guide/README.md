# Student Guide — Dari Nol sampai Research Pack

**Status** Draft v0.1 (2026-09)
**Terkait** [Hub Research-Based Learning](../README.md) · [Metopen Research Studio — Week 01](../../metopen-research-studio/weeks/week-01-endgame.md) · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md)

Ini versi ringkas *Student Research Playbook*. Baca sekali sebelum mulai (±20 menit), lalu bekerja dari halaman mingguan di [`metopen-research-studio/weeks/`](../../metopen-research-studio/README.md). Panduan ini berlaku untuk Metopen dan TA, dan sebagian besar juga untuk proyek AI/ML, Data Mining, NLP, dan RPL.

## 1. Apa yang berbeda: research thinking, bukan solution-first

Pola yang sering terjadi:

> "Saya ingin menggunakan Random Forest untuk memprediksi X."

Itu *solution-first*: algoritma dipilih sebelum masalah dipahami. Di sini Anda diminta mundur dulu:

```
Mengapa X perlu diprediksi? → siapa stakeholder-nya? → keputusan apa yang berubah jika prediksi tersedia?
→ apa yang sudah diketahui? → baseline paling sederhana apa? → metrik apa? → apakah data mewakili populasi?
→ bagaimana leakage dicegah? → apakah perbaikannya berarti secara praktis? → apa yang bisa membuat kesimpulan salah?
```

Barulah algoritma muncul — sebagai jawaban, bukan titik awal. Perubahan yang dituju:

| Tahap | Kalimat Anda |
|---|---|
| 1 | "Saya membuat sesuatu." |
| 2 | "Saya membuat klaim yang dapat diuji." |
| 3 | "Saya punya bukti yang cukup kuat untuk mempertanggungjawabkan klaim itu." |

Sepuluh pertanyaan research thinking ([MST-03](../../research-os/00-master/03-glossary.md)): fenomena/masalah nyata → apa yang kita ketahui → apa yang belum → apa yang kita klaim → bukti apa yang membuatnya dipercaya → desain apa yang menghasilkan bukti itu → data/artefak/eksperimen apa → apa yang bisa membatalkan kesimpulan → bisakah orang lain mereproduksi → *so what?*

Yang membedakan Anda di akhir semester bukan seberapa canggih modelnya, tetapi apakah Anda **sulit dibohongi — termasuk oleh AI Anda sendiri**.

## 2. Peta: 8 gate dan 16 minggu

Riset Anda melewati delapan gerbang. Setiap gerbang punya *definition of done*, bukti wajib, dan reviewer ([OPS-03](../../research-os/06-execution-os/03-research-gates.md)). Satu kalimat yang harus bisa Anda ucapkan di tiap gate:

| Gate | Minggu | Kalimat | Release |
|---|---|---|---|
| **G1 Endgame Ready** | W1 | "Riset ini menuju ___ lewat pintu ___." | — |
| **G2 Problem Ready** | W2 | "Masalahnya adalah ___, penting bagi ___ karena ___." | v0.1 Problem Validated |
| **G3 Evidence Ready** | W3–W5 | "Literatur sudah menunjukkan ___, tetapi bertentangan/kosong pada ___." | v0.2 Evidence Ready |
| **G4 Question Ready** | W6 | "Maka kami bertanya ___ dan akan berkontribusi ___." | — |
| **G5 Method Ready** | W7–W8 | "Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___." | v0.3 Research Design |
| **G6 Experiment Ready** | W9–W10 | "Pilot kami berjalan; orang lain sudah mereproduksinya." | v0.5 Pilot Experiment |
| **G7 Claim Ready** | W11–W12 | "Bukti mendukung klaim ___ dan tidak mendukung ___." | — |
| **G8 Contribution Ready** | W13–W16 | "Research Pack lengkap; TA/paper dapat dimulai dari sini." | v0.8 → v1.0 Research Pack |

Minggu: W1 Endgame · W2 Problem · W3 Search · W4 Evidence · W5 Gap · W6 RQ · W7 Method · W8 Design Defense · W9 Repository · W10 Pilot · W11 Analysis · W12 Contribution · W13 Manuscript · W14 Peer Review · W15 Revision · W16 Defense. Sprint S0 (onboarding) berlangsung sebelum W1.

Tiga level hasil: **TA Ready** (lolos G5 — minimum semua orang), **Research Ready** (G6–G7 — target), **Publication Ready** (G8 + manuscript — aspirasi).

## 3. Cara memulai (5 langkah, sebelum W1)

1. **Baca dan tanda tangani AI Research Protocol** ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)): *Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*. Mulai AI Usage Log ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) hari ini.
2. **Pilih masalah dari backlog** ([`research-backlog/BACKLOG.md`](../../research-backlog/BACKLOG.md)) atau bawa artefak MK sebelumnya (Experiment Card AI/ML, dataset card, korpus NLP, software RPL, problem brief KP). Kalau masalah Anda baru, buka Issue **Research Problem**. Pintu masuk boleh apa saja — Problem, Dataset, Faculty Research, Course Project, Partner, Competition — gate-nya sama.
3. **Bentuk tim 1–3 orang** dan sepakati peran bergilir: data owner, experiment owner, reproducibility owner. Identifikasi kandidat dosen mentor dari peta dosen ([AIR-03](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md)).
4. **Buat repositori riset dari [TPL-15](../../research-os/08-templates/15-research-repository-template.md)**: `README.md`, `docs/` (termasuk `docs/AI-USAGE.md`), `data/README.md`, `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `paper/`, `presentation/`, `references.bib`, `LICENSE`, `CITATION.cff`. Nama: `proj-YYYY-<topik>`.
5. **Buka [Week 01 — Endgame](../../metopen-research-studio/weeks/week-01-endgame.md)** dan kerjakan task-nya. Jangan membaca semua 16 minggu sekaligus; satu minggu, satu halaman.

## 4. Ritme mingguan (Student Weekly Playbook)

Backend sistem ini besar (±145 microtask, 17 sprint), tetapi Anda hanya perlu melihat **satu halaman per minggu** dengan enam bagian ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md)):

| Bagian | Isinya | Kebiasaan yang diminta |
|---|---|---|
| **This Week** | Outcome minggu ini | Baca Senin pagi; tulis di Issue sprint |
| **Tasks** | 5–10 task (umumnya 7–10) sebagai baby steps (Task ID `OPS-NNN`) | Kerjakan berurutan; commit per task |
| **Deliverable** | Yang dikumpulkan | Selalu dalam repo, bukan chat |
| **AI Assist** | AI boleh dipakai untuk apa minggu ini | Catat setiap penggunaan di AI Usage Log |
| **Human Check** | Yang wajib Anda verifikasi sendiri | Sumber, penalaran, bukti |
| **Done When** | Definisi selesai | Jangan lanjut minggu berikut sebelum ini terpenuhi |

Ritme yang terbukti: **3 sesi kerja tim per minggu** (2 jam), **1 sesi 20 menit dengan dosen/mentor** (bawa: gate saat ini, bukti minggu ini, blocker, bukti berikutnya), dan **1 commit per sesi**. Saat merasa gate siap, buka PR `GATE REVIEW: <nama gate>` dari branch `research/gN-<slug>` ([CONTRIBUTING.md](../../CONTRIBUTING.md)).

## 5. Aturan AI: boleh dan tidak

Kelas ini bukan *AI-free* dan bukan "pakai ChatGPT bikin proposal". Prinsipnya **AI-augmented, human-accountable science**: AI adalah research copilot, bukan epistemic authority.

| Boleh (dengan log & verifikasi) | Tidak boleh |
|---|---|
| Eksplorasi terminologi dan kandidat kata kunci pencarian | Memasukkan referensi dari AI tanpa memverifikasi DOI/URL dan membacanya |
| Coding support & debugging — kode diuji sebelum dipakai | Memakai kode AI tanpa pengujian, atau tanpa dicatat |
| Brainstorming hipotesis alternatif; mengkritik desain eksperimen Anda | Meminta AI "menulis proposal/hasil" lalu mengumpulkannya |
| Menjelaskan konsep statistik — verifikasi ke buku/notebook | Membiarkan AI menginterpretasi hasil tanpa Anda memeriksa angkanya |
| Membantu analisis dan visualisasi — angka dari data Anda | Memasukkan data pribadi/partner ke layanan AI eksternal ([SECURITY.md](../../SECURITY.md)) |
| Pra-anotasi label (NLP) — setiap label diverifikasi manusia | Menghitung AI sebagai anotator |
| Menyunting bahasa — diungkap di AI Usage Statement | Menyembunyikan penggunaan AI yang memengaruhi kesimpulan |

Setiap output AI melewati **source verification → reasoning verification → evidence verification → human accountability**. Target kompetensi: minimal **AI Investigator** dengan perilaku **AI Governor** (memverifikasi, mendokumentasikan, mempertanggungjawabkan) ([AIX-02](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md)). Katalog alat per kategori: [AIX-05](../../research-os/05-ai-augmented-research/05-ai-tools-reference.md).

## 6. Integritas dan amanah epistemik

Signature UAI: **amanah epistemik**. Anda memegang amanah untuk **tidak**:

- mengarang atau mengubah data;
- memilih bukti yang menguntungkan saja atau menutupi hasil negatif;
- mengubah metrik setelah melihat hasil;
- mengutip yang tidak dibaca, atau membiarkan AI mengarang referensi;
- mengklaim kausalitas dari korelasi;
- melebih-lebihkan kontribusi;
- menyalin kode/tulisan tanpa atribusi.

Dalam bahasa riset modern: *research integrity*. Dalam bahasa keimanan: kejujuran terhadap kebenaran meskipun kebenaran itu meruntuhkan hipotesis sendiri. Orientasinya bukan "bagaimana penelitian saya terlihat bagus?", melainkan "apa yang sebenarnya benar berdasarkan bukti yang Allah izinkan saya temukan?"

Operasionalnya: **Research Integrity gate** di setiap gate — lulus/gagal, bukan skor. Satu pelanggaran membuat gate gagal terlepas dari kualitas lain. Sebelum defense/submission Anda mengisi [Research Integrity Checklist (TPL-11)](../../research-os/08-templates/11-research-integrity-checklist.md). Model yang kalah dari baseline dan dilaporkan jujur adalah hasil yang sah; model yang "menang" karena leakage adalah pelanggaran.

## 7. Apa yang dinilai: 5E

Tidak ada UTS/UAS hafalan untuk komponen studio. Yang dinilai adalah **milestone portfolio + defense** dengan rubrik **5E** ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)):

| E | Menilai | Bukti utama |
|---|---|---|
| **End** | Kejelasan endgame & problem | `docs/endgame.md`, Problem Brief, One-Pager |
| **Evidence** | Kualitas bukti literatur | Synthesis matrix 15–25 sumber terverifikasi, Research Gap |
| **Experiment** | Kualitas desain & pilot | Design Card, Experiment Card, baseline & metrik, pilot yang direproduksi |
| **Explanation** | Argumentasi claim–evidence–reasoning | `results/analysis.md`, threats to validity, proposal/manuscript, defense |
| **Execution** | Disiplin sprint, repositori, gate, peer review | Commit history, PR gate, AI Usage Log, review yang Anda tulis untuk tim lain |

Di MK teknis (AI/ML, Data Mining, NLP, RPL) empat kriteria yang sama dipakai dalam bentuk ringkas: **baseline, metrik & evaluasi, reproducibility, AI disclosure** ([Assessment](../assessment/README.md)).

## 8. Cara meminta review dan mentor

| Kebutuhan | Cara |
|---|---|
| Review gate | PR `GATE REVIEW: <gate>` memakai template di `.github/PULL_REQUEST_TEMPLATE/`; isi semua field (RQ, method, dataset, baseline, metrics, threats, evidence, AI usage); beri label `status:review` |
| Pertanyaan cepat ke dosen | Komentar di Issue sprint dengan format: *gate saat ini · yang sudah ada · yang macet · keputusan yang dibutuhkan* |
| Mentor dari klaster | Lihat peta dosen ([AIR-03](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md)); ajukan lewat pengampu di G1; nama mentor masuk field *Faculty Mentor* Mission Control |
| Peer review | W14: Anda mereview tim lain dengan [TPL-12](../../research-os/08-templates/12-peer-review-template.md) — problem, evidence, RQ, method, results, claim, limitations |
| Peer reproduction | Minta tim lain menjalankan baseline Anda dari README tanpa bertanya; catat hasilnya di `experiments/README.md` (bukti G6) |

Review yang menolak PR bukan kegagalan; itu bagian normal riset. Baca *apa yang kurang* dan *bukti apa yang dibutuhkan*, revisi, buka review ulang.

## 9. Jalur setelah Metopen

| Jalur | Syarat | Yang terjadi |
|---|---|---|
| **TA** (semester VIII) | Research Pack lolos G5 (TA Ready) + handoff | Pembimbing memulai dari Pack Anda; TA = G6–G8 skala penuh ([final-project](../courses/final-project/README.md)) |
| **Paper** | Research Ready + manuscript-ready | Pipeline `submission-ready → submitted → accepted → published` di [`publications/`](../../publications/README.md) ([MET-05](../../research-os/04-metopen-research-studio/05-publication-backward-design.md)) |
| **Artefak / dataset** | Software/model/korpus layak rilis | Release review → `ART-`/`DS-`; lisensi & IP review ([LICENSING.md](../../LICENSING.md)) |
| **AI Research Center** | Handoff dengan *missing evidence* | Riset masuk program/riset dosen; Anda dapat menjadi asisten riset atau anggota tim skema penelitian |
| **Kompetisi / produk / HKI** | Impact Ready | Dicatat di Mission Control; HKI lewat unit terkait |

Apa pun jalurnya, tinggalkan handoff ([TPL-14](../../research-os/08-templates/14-research-handoff-template.md)). Riset tanpa handoff hilang bersama nilai.

## 10. FAQ mahasiswa

**1. Saya belum punya ide judul. Apakah itu masalah?**
Tidak — justru bagus. Judul lahir di W6 (RQ) sebagai konsekuensi masalah dan bukti. Mulailah dari backlog atau artefak MK sebelumnya.

**2. Bolehkah saya melanjutkan proyek AI/ML atau KP saya?**
Sangat disarankan. Bawa Experiment Card/problem brief-nya dan minta pengampu MK asal mengisi handoff. Anda mewarisi gate embrio yang sudah dilatih.

**3. Berapa banyak paper yang harus dibaca?**
15–25 sumber primer yang **benar-benar dibaca** dan dipetakan dalam synthesis matrix — bukan 50 abstrak. Satu referensi yang tidak bisa diverifikasi membuat G3 gagal.

**4. Model saya kalah dari baseline. Apakah saya gagal?**
Tidak. Laporkan jujur dengan error analysis dan threats to validity. Hasil negatif yang dijelaskan dengan baik lolos G7; hasil "menang" tanpa baseline tidak.

**5. Apa bedanya "TA Ready" dan "Research Ready"?**
TA Ready = lolos G5: desain, data plan, baseline, metrik siap; Anda tidak lagi mencari judul di semester VIII. Research Ready = lolos G6–G7: pilot berjalan, direproduksi, dianalisis.

**6. Saya bekerja sendiri. Bagaimana peer reproduction?**
Minta anggota tim lain di kelas; pengampu menjadwalkannya di W10 dan W12–13. Tim 1 orang tetap wajib direproduksi orang lain.

**7. AI membantu saya menulis kode; harus dicatat?**
Ya, di AI Usage Log: tool, tanggal, tujuan, output material, verifikasi (diuji atau tidak), dimasukkan atau tidak. Kode yang tidak diuji tidak boleh masuk `src/`.

**8. Data saya dari partner/instansi. Boleh di-push?**
Tidak. Simpan di luar GitHub; commit hanya kartu metadata (`data/README.md`) dan kode. Prompt ke AI eksternal juga tidak boleh memuat data pribadi/partner.

**9. Berapa lama Research Defense?**
7–10 menit dengan struktur [TPL-13](../../research-os/08-templates/13-research-defense-template.md); penguji bertanya tentang problem, evidence, method, results, claim, limitations — bukan hafalan.

**10. Apa yang terjadi kalau saya gagal satu gate?**
Reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan; Anda merevisi dan membuka review ulang. Gate berurutan, jadi selesaikan yang gagal sebelum lanjut. Gagal gate bukan hukuman; itu cara sistem mencegah Anda menghabiskan semester pada eksperimen yang tidak menjawab apa pun.

## 11. Checklist "saya siap mulai"

- [ ] Saya sudah membaca AI Research Protocol dan menandatanganinya; `docs/AI-USAGE.md` sudah ada di repo saya.
- [ ] Saya sudah membaca [Glossary](../../research-os/00-master/03-glossary.md) bagian gate, maturity, dan skema ID.
- [ ] Saya punya masalah (dari backlog/artefak MK/dosen/partner) dan bisa menjelaskannya dalam dua kalimat *tanpa menyebut algoritma*.
- [ ] Tim 1–3 orang terbentuk; peran bergilir disepakati; akun GitHub semua anggota aktif.
- [ ] Repositori `proj-YYYY-<topik>` dibuat dari TPL-15 dengan struktur lengkap; `LICENSE` dan `CITATION.cff` ada.
- [ ] Saya tahu endgame saya: minimum TA Ready, target Research Ready, aspirasi (bila ada).
- [ ] Saya tahu kandidat mentor dan cara meminta review (PR `GATE REVIEW`).
- [ ] Saya sudah membuka [Week 01 — Endgame](../../metopen-research-studio/weeks/week-01-endgame.md) dan tahu *Done When* minggu ini.
- [ ] Saya paham: data sensitif tidak pernah masuk GitHub; setiap referensi harus terverifikasi; setiap penggunaan AI dicatat.
