# Week 01 — Endgame

> **Sprint** S1 · **Gate** G1 Endgame Ready · **Status** Draft v0.1 (2026-09) · [← Studio README](../README.md) / [Week berikutnya →](week-02-problem.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan satu kalimat dengan yakin: **"Riset ini menuju ___ lewat pintu ___."** Endgame tertulis di `docs/endgame.md` sebagai *klaim pengetahuan yang ingin dibuktikan*, bukan sekadar aplikasi yang ingin dibuat; entry door dan kandidat mentor dipilih; Issue `type:problem` pertama terbuka dengan Research ID sementara `UIAI-YYYY-TBD`; AI Research Protocol Agreement yang ditandatangani saat onboarding S0 dan AI Usage Log yang sudah berjalan sejak S0 dituntaskan sebagai bukti G1. Semua bukti itu dikumpulkan dalam satu PR `GATE REVIEW: Endgame Ready` yang direview dosen pengampu.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (research thinking, project vs research, entry door), **60 menit studio** (tim menulis endgame dan klaim awal, dosen/mentor berkeliling), **10 menit gate check** (setiap tim melaporkan satu kalimat endgame, blocker, dan rencana sisa sprint). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md): 10 menit sprint planning Senin, 15 menit gate check Jumat.

## Concept (30 menit)

1. **Project ≠ research.** Project menghasilkan artefak yang berjalan; implementation menerapkan yang sudah diketahui; engineering mengoptimalkan; *research* menghasilkan **credible knowledge** — klaim yang dapat diuji dan dipertanggungjawabkan. Judul TA yang berbunyi "Rancang bangun aplikasi X" adalah project sampai ada klaim yang bisa salah.
2. **Alur research thinking sepuluh langkah** ([MET-01](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §4.1): fenomena nyata → apa yang diketahui → apa yang belum → apa yang diklaim → bukti apa yang membuat klaim dipercaya → desain apa yang menghasilkan bukti itu → data/artefak/eksperimen apa → apa yang bisa membatalkan kesimpulan → bisakah orang lain memeriksa → *so what?* Minggu ini Anda baru berada di langkah 1 dan mengintip langkah 4.
3. **Tiga layer outcome** ([STR-02](../../research-os/01-strategic-foundation/02-vision-and-endgame.md) §3): **TA Ready** (minimum, wajib 100%, setara lolos G5), **Research Ready** (target, setara G6–G7), **Publication/Impact Ready** (aspirasi: paper, dataset, artefak, HKI, produk). Endgame ditulis dalam tiga baris ini, bukan satu.
4. **Enam entry door, satu pipeline**: Problem, Dataset, Faculty Research, Course Project, Partner, Competition. Pintu boleh berbeda; gate-nya sama.
5. **Peta semester**: 8 Research Gate ([OPS-03](../../research-os/06-execution-os/03-research-gates.md)) dan 16 artefak Research Pack ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md)). Anda tidak perlu menghafalnya; cukup tahu bahwa setiap minggu mengisi satu potong peta itu.
6. **Endgame lemah vs kuat.** Lemah: "membuat aplikasi rekomendasi mata kuliah". Kuat: "menguji apakah metode M mengungguli baseline B pada konteks K dengan metrik μ" — metode dan metrik boleh masih kosong minggu ini, tetapi bentuk kalimatnya harus sudah berupa klaim.
7. **Klaim awal boleh salah, tetapi harus ada.** Kalimat "Kami ingin membuktikan bahwa ___ pada konteks ___" adalah hipotesis kerja; bagian yang masih asumsi ditandai, bukan disembunyikan. Itulah amanah epistemik sejak hari pertama.
8. **AI adalah copilot, bukan pemilih topik.** Protokol *Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own* ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)) berlaku mulai prompt pertama minggu ini.

**Pertanyaan pemandu** yang harus bisa Anda jawab tanpa membaca catatan di akhir sesi: *"Apa perbedaan antara membuat sesuatu dan membuktikan sesuatu — dan yang mana yang akan tim saya lakukan di TA?"*

## Tasks

Semua task Sprint S1 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add endgame v0 (OPS-008)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-007 | Ikuti sesi Research Mindset dan bedakan proyek vs riset | Refleksi W1 | 2h | Menguji pemahaman lewat contoh tambahan; jawaban akhir ditulis mahasiswa | Mahasiswa menjelaskan ulang perbedaan tanpa membaca catatan |
| OPS-008 | Tetapkan endgame: minimum TA Ready, target Research Ready | Bagian Endgame di docs/endgame.md | 2h | Mengkritik apakah endgame terlalu luas atau terlalu sempit | Dosen memeriksa endgame memuat klaim pengetahuan, bukan sekadar membuat aplikasi |
| OPS-009 | Tulis klaim pengetahuan awal yang ingin dibuktikan | Kalimat klaim awal | 1h | Menawarkan alternatif rumusan klaim; tim memilih dan mengeditnya | Tim menandai bagian klaim yang masih asumsi tanpa bukti |
| OPS-010 | Identifikasi kandidat dosen mentor dan klaster riset | Daftar kandidat mentor + klaster | 1h | - | Dosen pengampu mengonfirmasi kandidat mentor masuk akal |
| OPS-011 | Buka Issue type:problem awal dengan Research ID sementara | Issue type:problem | 1h | Membantu merapikan bahasa Issue; isi substantif dari tim | Tim memastikan problem owner riil dan tidak ada data pribadi |
| OPS-012 | Tulis Research One-Pager v0 bagian identitas dan endgame | docs/one-pager.md v0 (parsial) | 1h | Merapikan format; bukan mengisi konten | Tim memeriksa konsistensi dengan Issue dan endgame |
| OPS-013 | Siapkan PR GATE REVIEW: Endgame Ready | PR GATE REVIEW: Endgame Ready | 1h | - | Dosen pengampu mereview: endgame spesifik dan realistis |
| OPS-014 | Perbarui AI Usage Log dan jurnal mingguan W1 | AI Usage Log W1 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 9.5h** (jam tim; untuk tim 2 orang bagi dua). Sprint ini tergolong ringan — gunakan sisa waktunya untuk membaca backlog dan peta riset dosen, bukan untuk mencuri start ke task minggu depan.

**Urutan yang disarankan** (dari kolom Dependency): mulai dari OPS-007 di sesi studio (prasyaratnya OPS-002 dari S0), lanjut OPS-008 → OPS-009 dan OPS-010 (keduanya hanya butuh OPS-008, boleh paralel) → OPS-011 (butuh OPS-010) → OPS-012 (butuh OPS-011) → OPS-013 (butuh OPS-011, OPS-012, dan repo/log dari S0: OPS-005, OPS-006); OPS-014 berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g1-endgame`, harus ada:

| Artefak | Lokasi di repositori ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §4) | Bentuk bukti | Task |
|---|---|---|---|
| Endgame (minimum / target / aspirasi + bentuk output), **Initial Claim**, **Cluster & Mentor** | `docs/endgame.md` | commit di branch `research/g1-endgame` | OPS-008, OPS-009, OPS-010 |
| Bukti permintaan mentor (tangkapan layar/pesan, tanpa data pribadi berlebih) | tautan atau catatan di `docs/endgame.md` §Cluster & Mentor | commit | OPS-010 |
| Issue Research Problem awal dengan Research ID sementara `UIAI-YYYY-TBD` | Issue `type:problem` di repo pusat (form [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml)); nomor Issue dicantumkan di `README.md` §Current Research Gate | Issue terbuka + commit README | OPS-011 |
| Research One-Pager v0 (bagian identitas & endgame terisi; sisanya `[belum diisi — target vN]`) | `docs/one-pager.md` ([TPL-01](../../research-os/08-templates/01-research-one-pager-template.md)) | commit | OPS-012 |
| AI Research Protocol Agreement tertandatangani | `docs/ai-protocol-agreement.md` ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §5) | commit (ditandatangani di S0, OPS-002) | OPS-002 (S0) → bukti wajib G1 di OPS-013 |
| AI Usage Log W1 + ringkasan AI Usage Statement awal | `docs/AI-USAGE.md` ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)); dimulai di S0 (OPS-006) | commit | OPS-014 |
| Jurnal W1: klasifikasi 5 judul TA (proyek/riset) + refleksi 5 kalimat + apa yang dipelajari/ragu/rencana | `docs/journal/w01.md` | commit | OPS-007, OPS-014 |
| **PR `GATE REVIEW: Endgame Ready`** dengan checklist bukti G1 dan reviewer dosen pengampu | PR dari `research/g1-endgame` ke branch utama repo riset | URL PR terbuka | OPS-013 |

Struktur folder standar (`docs/`, `data/README.md`, `src/`, `notebooks/`, `experiments/`, `results/`, `figures/`, `paper/`, `presentation/`) sudah dibuat saat onboarding S0, pra-W1 (OPS-005); minggu ini cukup dipastikan ada dan README riset memuat judul kerja, tim, dan `Current Research Gate: G1`.

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **saat itu juga**, bukan Jumat.

**Boleh minggu ini**

- Meminta AI memberi contoh judul tambahan untuk latihan klasifikasi proyek vs riset (OPS-007) — jawaban dan refleksi akhir ditulis mahasiswa sendiri.
- Meminta AI mengkritik endgame: terlalu luas untuk satu semester + TA, atau terlalu sempit untuk menjadi klaim pengetahuan (OPS-008).
- Meminta beberapa alternatif rumusan kalimat klaim awal, lalu tim memilih dan mengeditnya (OPS-009).
- Merapikan bahasa Issue (OPS-011) dan format One-Pager (OPS-012) — isi substantif tetap dari tim.
- Eksplorasi istilah bidang dan memetakan sub-area topik kandidat; brainstorming kandidat endgame sebelum dicek ke backlog dan dosen.
- Menjadi "penanya skeptis" saat tim melatih kalimat "Riset ini menuju ___ lewat pintu ___."

**Tidak boleh**

- Meminta AI "memilihkan topik TA" tanpa mengecek [research backlog](../../research-backlog/README.md), [roadmap](../../research-roadmap/README.md), atau riset dosen — keputusan topik adalah milik tim dan mentor.
- Memasukkan data pribadi anggota tim, nama/kontak problem owner, atau data partner ke layanan AI (lihat [SECURITY.md](../../SECURITY.md)).
- Membiarkan AI mengisi substansi endgame, klaim, atau Issue yang tim tidak dapat jelaskan ulang tanpa AI.
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-010 (kandidat mentor), OPS-013 (PR gate), OPS-014 (log dan jurnal) — ketiganya adalah penilaian dan pertanggungjawaban manusia.
- Menyisipkan "referensi" dari AI ke endgame atau Issue; belum ada sumber yang boleh dikutip sebelum diverifikasi di W3.

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa dapat menjelaskan ulang perbedaan project, implementation, engineering, dan research **tanpa membaca catatan** | diri sendiri, diuji oleh peer di 15 menit terakhir studio | OPS-007 |
| Endgame memuat klaim pengetahuan, bukan sekadar "membuat aplikasi X"; realistis untuk 1 semester + TA | dosen pengampu (saat gate check dan review PR) | OPS-008, OPS-013 |
| Bagian klaim yang masih asumsi tanpa bukti **ditandai** eksplisit | tim (setiap anggota membaca ulang `docs/endgame.md`) | OPS-009 |
| Kandidat mentor dan klaster C1–C4 masuk akal terhadap masalah dan peta riset dosen | dosen pengampu | OPS-010 |
| Problem owner di Issue riil (bukan dikarang) dan Issue tidak memuat data pribadi | tim | OPS-011 |
| One-Pager v0 konsisten dengan Issue dan `docs/endgame.md` (judul kerja, tim, entry door, endgame sama persis) | tim; peer dari tim lain membaca 3 menit | OPS-012 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya sendiri (tool, tujuan, verifikasi, dipakai/tidak) | diri sendiri | OPS-014 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint).

## Done When

Minggu ini **menutup gate G1 Endgame Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] Tim (1–3 orang) terbentuk, repositori riset berstruktur standar [TPL-15](../../research-os/08-templates/15-research-repository-template.md), semua anggota punya akses.
- [ ] `docs/endgame.md` memuat **minimum TA Ready / target Research Ready / aspirasi** beserta bentuk output yang dituju.
- [ ] `docs/endgame.md` §Initial Claim berisi kalimat "Kami ingin membuktikan bahwa ___ pada konteks ___" dengan asumsi yang ditandai.
- [ ] Entry door dipilih (Problem / Dataset / Faculty Research / Course Project / Partner / Competition) dan tertulis di endgame serta One-Pager.
- [ ] 1–2 kandidat mentor dan klaster C1–C4 tertulis di `docs/endgame.md` §Cluster & Mentor; pesan permintaan mentor sudah dikirim.
- [ ] Issue `type:problem` terbuka dengan Research ID sementara `UIAI-YYYY-TBD` (ID resmi ditetapkan saat PR G2 di-merge); nomornya tercantum di README riset §Current Research Gate.
- [ ] `docs/one-pager.md` v0: identitas dan endgame terisi; field lain bertanda `[belum diisi — target vN]`, tidak ada yang kosong.
- [ ] `docs/ai-protocol-agreement.md` ditandatangani setiap anggota.
- [ ] `docs/AI-USAGE.md` (AI Usage Log) dan `docs/journal/w01.md` ter-commit.
- [ ] Setiap anggota dapat mengucapkan "Riset ini menuju ___ lewat pintu ___" tanpa membaca.
- [ ] PR **`GATE REVIEW: Endgame Ready`** termerge oleh dosen pengampu; label `gate:G1-endgame` terpasang; README §Current Research Gate diperbarui.

**Ringkasan gate G1** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G1). **Lulus jika** endgame spesifik dan realistis untuk 1 semester + TA, dengan klaim pengetahuan yang ingin dibuktikan. **Gagal jika** endgame hanya "membuat aplikasi X" tanpa klaim pengetahuan — atau bila ada pelanggaran integritas (mis. penggunaan AI yang tidak diungkap), terlepas dari kualitas lainnya. Reviewer: dosen pengampu Metopen. Gagal gate bukan hukuman: reviewer menulis apa yang kurang, tim merevisi, review dibuka ulang.

**Cara membuka PR gate** ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3): (1) pastikan semua bukti di tabel Deliverable ada di branch `research/g1-endgame`; (2) buka PR berjudul `GATE REVIEW: Endgame Ready` — G1 memakai [template PR default](../../.github/PULL_REQUEST_TEMPLATE.md); isi field yang relevan (endgame, entry door, AI usage) dan tulis `[belum ada — target G2/G5]` untuk field RQ, dataset, baseline, metrik; (3) tautkan nomor Issue `type:problem`; (4) minta review dosen pengampu; (5) setelah merge, perbarui label `gate:G1-endgame`, field Mission Control, dan `Current Research Gate` di README. Komentar review disimpan, tidak dihapus — itu bukti proses ilmiah.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — struktur repo, README riset, branch `research/g1-endgame`.
- [TPL-01 Research One-Pager Template](../../research-os/08-templates/01-research-one-pager-template.md) — `docs/one-pager.md` v0 (field 1–6, 19, 20).
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — `docs/AI-USAGE.md` (log + ringkasan statement).
- [TPL-07 Faculty Research Map Template](../../research-os/08-templates/07-faculty-research-map-template.md) — membaca peta riset dosen untuk kandidat mentor.
- Form Issue [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml) dan [template PR default](../../.github/PULL_REQUEST_TEMPLATE.md).

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W1 · [MET-01 Positioning](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §4 research thinking & solution-first vs problem-first · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §E1 End.
- [STR-02 Vision & Endgame](../../research-os/01-strategic-foundation/02-vision-and-endgame.md) §3 empat level outcome.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) · [AIX-02 AI Research Competency](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md) §6 self-assessment awal · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §5 agreement.
- [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) · [AIR-03 Faculty Research Alignment](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md) · [Research Roadmap](../../research-roadmap/README.md) · [Research Backlog](../../research-backlog/README.md).
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S1 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G1 · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md).

**Halaman studio**

- [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Endgame berupa aplikasi, bukan klaim.** "Membuat sistem rekomendasi X" gagal G1. Cara menghindari: tulis dulu kalimat "Kami ingin membuktikan bahwa ___ pada konteks ___"; bila tidak ada kata *membuktikan/menguji/membandingkan*, itu belum riset.
2. **Solution-first sejak hari pertama.** Nama algoritma muncul di endgame atau Issue sebelum masalah dan stakeholder-nya dipahami. Cara menghindari: mundur ke pertanyaan "mengapa X perlu diprediksi/diukur, untuk siapa, keputusan apa yang berubah?" ([MET-01](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §4.2); algoritma boleh muncul di W7.
3. **Aspirasi melampaui kapasitas.** Menulis "publikasi internasional" sebagai target padahal data belum ada. Cara menghindari: minimum TA Ready wajib, target Research Ready, aspirasi boleh kosong — kejujuran tentang batas lebih dihargai reviewer daripada ambisi tanpa rencana bukti.
4. **AI memilihkan topik.** Topik hasil satu prompt tanpa dicek ke backlog, roadmap, atau dosen jarang punya pemilik masalah nyata. Cara menghindari: AI hanya untuk mengkritik dan memperkaya kandidat yang sudah tim temukan; catat di AI Usage Log termasuk saran yang ditolak dan alasannya.
5. **Bukti tinggal di kepala atau di chat.** Endgame "sudah disepakati" tetapi belum di-commit; log AI "nanti diisi Jumat". Cara menghindari: buat file kosong `docs/endgame.md`, `docs/one-pager.md`, `docs/journal/w01.md` pada Senin; setiap commit menyebut Task ID; log diisi pada hari penggunaan.
6. **Data pribadi di Issue atau prompt.** Nama lengkap, NIM, atau kontak problem owner ditulis di Issue publik atau dikirim ke layanan AI. Cara menghindari: sebut peran dan institusi, bukan identitas; simpan kontak di luar repo ([SECURITY.md](../../SECURITY.md)).
