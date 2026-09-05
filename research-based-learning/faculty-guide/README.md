# Faculty Guide — Lecturer Playbook Ringkas

**Status** Draft v0.1 (2026-09)
**Terkait** [Hub Research-Based Learning](../README.md) · [Assessment](../assessment/README.md) · [Student Guide](../student-guide/README.md) · [ARC-01 Research Capability Spiral](../../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-03 AI Contribution Modes](../../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-05 CPL–CPMK–Artifact](../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [AIR-03 Faculty Research Alignment](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md) · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) · [GOV-01 Governance Model](../../research-os/07-governance/01-governance-model.md) · [GOVERNANCE.md](../../GOVERNANCE.md)

Panduan ini adalah versi ringkas *Lecturer Playbook* (artefak turunan #4 dalam [research-os/README](../../research-os/README.md)). Ia untuk **semua dosen** Prodi Informatika — bukan hanya pengampu Metopen — dan dapat dibaca dalam 20 menit. Versi panjang dikompilasi dari paket 02, 04, 05, 06 bila diperlukan.

Kalimat yang perlu dipegang: *yang diminta dari mata kuliah Anda bukan riset besar, melainkan satu lapisan tipis berpikir riset pada aktivitas yang sudah ada* — **one activity, multiple outcomes**.

## 1. Research capability spiral: di mana mata kuliah Anda berada

[ARC-01](../../research-os/02-academic-architecture/01-research-capability-spiral.md) menempatkan kompetensi riset yang sama — mengamati, bertanya, membandingkan, membuktikan, mempertanggungjawabkan — berulang setiap tahun dengan taruhan yang makin besar.

| Tahun | Tema | Mata kuliah | Pertanyaan yang harus bisa dijawab mahasiswa | Yang diminta dari dosen |
|---|---|---|---|---|
| Y1 | Observe & Reason | Statistika, Kalkulus, Statistika Terapan, Matematika Diskrit | "Apa yang ditunjukkan data ini, dan apa yang *tidak* boleh saya simpulkan?" | Satu tugas dengan bagian "apa yang tidak boleh disimpulkan"; notebook yang bisa dijalankan ulang |
| Y2 | Build & Compare | HCI, Struktur Data, Basis Data, Analisis Algoritma, RPL, Data Mining | "Saya membangun sesuatu — dibanding apa, diukur dengan apa, pada data apa?" | Setiap proyek menyebut baseline & metrik; dataset card v0; README reproducibility |
| Y3 | Experiment & Evaluate | AI/ML, Pengujian PL, Proyek PL, Kerja Praktik, Etika Profesi | "Apakah klaim saya bertahan terhadap baseline, error analysis, threats to validity, pengguna nyata?" | Experiment Card sebelum eksperimen; peer reproduction; problem brief dari KP; AI Usage Log dinilai |
| Y4 | Prove & Contribute | Metopen, TA | "Bukti apa yang membuat klaim saya layak dipercaya, dan siapa yang bisa memeriksanya?" | 8 gate formal; Research Pack; defense; handoff |

Temukan MK Anda di tabel [hub §4](../README.md), lalu ambil 1–3 sel di [ARC-01 §7](../../research-os/02-academic-architecture/01-research-capability-spiral.md) sebagai tanggung jawab MK Anda. Itu saja titik mulainya.

## 2. Memilih mode F / E / R

[ARC-03](../../research-os/02-academic-architecture/03-ai-contribution-modes.md) memberi tiga mode agar tidak semua MK dipaksa melakukan riset.

| Pertanyaan | Ya → | Contoh |
|---|---|---|
| Apakah MK Anda membangun kemampuan dasar (statistik, algoritma, data, penalaran) yang dipakai riset, tanpa proyek AI? | **F — Foundation** | Statistika, Matematika Diskrit, Struktur Data, Analisis Algoritma |
| Apakah MK Anda memakai kasus/proyek AI atau masalah riset nyata sebagai bahan, tetapi artefaknya tidak dimaksudkan dipakai ulang? | **E — AI-Enriched** | HCI (user study sistem AI), Pengujian PL (testing model), Etika Profesi (kasus AI), Kerja Praktik |
| Apakah MK Anda menghasilkan artefak yang **dicatat dan dipakai ulang** riset lain (dataset card, experiment card, korpus, software terdaftar, Research Pack)? | **R — Research-Producing** | AI/ML, Data Mining, NLP, Metopen, TA; RPL/Proyek PL bila artefak terdaftar |

Tiga aturan praktis:

1. **Mode boleh naik bertahap** (E → R). Semester pertama integrasi, jalankan E dengan satu artefak wajib; semester berikutnya naikkan ke R.
2. **Mode R menuntut konsekuensi**: artefak wajib di `courses/<mk>/research-artifact.md` masuk penilaian, dan minimal satu artefak per tim tercatat di registry/backlog/handoff.
3. **Mode F bukan mode rendah.** Tanpa evidence reasoning Y1 dan baseline thinking Y2, Metopen harus mengajar semuanya dalam 2 SKS.

Catat keputusan di tabel [hub §4](../README.md) lewat PR.

## 3. Mendesain proyek MK agar menghasilkan research asset

Enam keputusan desain yang mengubah "tugas besar" menjadi research asset tanpa menambah beban:

| # | Keputusan | Cara termurah melakukannya |
|---|---|---|
| 1 | **Tema problem-first, dari backlog/registry** | Buka [`research-backlog/BACKLOG.md`](../../research-backlog/BACKLOG.md) dan [`datasets-registry/REGISTRY.md`](../../datasets-registry/REGISTRY.md); pilih 3–5 tema yang cocok MK Anda; larang "saya ingin memakai algoritma X" sebagai kalimat pembuka (*reuse before create*) |
| 2 | **Baseline & metrik sebelum hasil** | Milestone tengah = Experiment Card ([TPL-09](../../research-os/08-templates/09-experiment-card.md)) ber-commit sebelum hasil pertama; ini satu-satunya cara mencegah metrik dipilih setelah melihat angka |
| 3 | **Repositori sejak minggu 2** | Struktur [TPL-15](../../research-os/08-templates/15-research-repository-template.md) (boleh minimum); hasil yang hanya ada di laptop tidak dinilai |
| 4 | **Satu artefak yang dicatat** | Dataset card ([TPL-05](../../research-os/08-templates/05-dataset-registry-template.md)) atau Issue *Research Problem*; 30 menit kerja tim, seumur hidup di research memory Prodi |
| 5 | **Milestone portfolio, bukan UTS/UAS hafalan untuk komponen proyek** | 4–5 milestone dengan deliverable jelas (contoh di setiap `courses/<mk>/README.md` §5); presentasi 7 menit di akhir |
| 6 | **AI Usage Log sejak minggu 1** | [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md); ringan di Y1–Y2, dinilai di Y3–Y4 |

Kerangka formal untuk menuliskannya ke RPS: [ARC-05](../../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) — CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence. Contoh CPMK riset per MK ada di setiap `courses/<mk>/README.md` §4.

## 4. Menilai: rubrik dan integritas

Standar lintas MK ada di [Assessment](../assessment/README.md). Ringkasnya:

- **MK teknis mode E/R** memakai rubrik research-quality 4 level pada empat kriteria: **baseline, metrik & evaluasi, reproducibility, AI disclosure & integritas**. Level 3 = "baik untuk kelas"; level 4 = "layak dipakai riset lain".
- **Metopen dan TA** memakai **5E** ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)): End, Evidence, Experiment, Explanation, Execution.
- **Research Integrity gate** berlaku di semua MK sebagai lulus/gagal, bukan skor: fabrikasi, falsifikasi, plagiarisme, sitasi palsu, AI tidak diungkap → gagal, terlepas dari kualitas lain ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- **Tim vs individu**: gunakan git log (kontribusi commit), AI Usage Log per orang, dan peran bergilir yang dicatat di README; jangan menilai tim dari satu presenter.

Yang perlu dihindari: menilai "keindahan" laporan lebih dari kejujuran hasilnya. Hasil negatif yang dilaporkan jujur dengan baseline dan threats to validity bernilai lebih tinggi daripada accuracy 97% tanpa pembanding.

## 5. Mentoring dan review gate

### 5.1 Ritme: 20 menit per tim per minggu

Format tetap agar 20 menit cukup (untuk MK teknis, cukup dua mingguan):

| Menit | Agenda | Pertanyaan dosen |
|---|---|---|
| 0–3 | Status | "Gate/milestone mana sekarang? Apa yang selesai minggu ini — tunjukkan komitnya." |
| 3–10 | Bukti | "Apa bukti yang dihasilkan? Baseline-nya apa? Angkanya dibanding apa?" |
| 10–15 | Blocker | "Apa yang menghambat? Keputusan apa yang butuh saya?" |
| 15–18 | Next evidence | "Bukti apa yang harus ada minggu depan agar milestone berikutnya lulus?" |
| 18–20 | Catat | Tulis 3 baris di Issue/PR: status, blocker, next evidence — ini bukti proses ilmiah |

Bagian yang paling sering dilewatkan dan paling berharga: **next evidence**. Mahasiswa yang tahu bukti apa yang dicari minggu depan tidak akan tersesat.

### 5.2 Cara menulis review gate yang baik

Review gate ditulis di PR `GATE REVIEW: <gate>` ([CONTRIBUTING.md §3](../../CONTRIBUTING.md)); merge = lulus. Reviewer memeriksa terhadap *definition of done* di [OPS-03](../../research-os/06-execution-os/03-research-gates.md), bukan terhadap selera.

| Lakukan | Hindari |
|---|---|
| Mulai dari pertanyaan gate: "Apakah orang di luar tim bisa mengulang masalah ini dalam dua kalimat?" (G2) | "Kurang mendalam", "perbaiki lagi" tanpa menyebut apa |
| Sebut **bukti yang kurang**, bukan hanya kekurangan: "Belum ada baseline; tambahkan majority-class baseline di `results/pilot-01/summary.md` (+ `baseline.json`)" | Meminta perubahan metode sebelum baseline & metrik disepakati |
| Pisahkan **blocking** (gagal gate) dari **saran** (boleh nanti) | Menggabungkan 15 komentar tanpa prioritas |
| Cek integritas dulu: sitasi terverifikasi? AI Usage Log ada? data sensitif tidak di repo? | Menilai tulisan rapi sebagai bukti kualitas |
| Tulis keputusan eksplisit: "Lulus G5" / "Belum: 2 blocker di atas" | Membiarkan PR menggantung tanpa keputusan |
| Simpan komentar; jangan hapus setelah revisi | Memberi review lisan tanpa jejak |

Kalimat pembuka yang berguna: *"Klaim ini menunjuk ke bukti apa?"*, *"Apa yang bisa membuat kesimpulan ini salah?"*, *"Siapa selain kalian yang sudah menjalankan ini?"*

Gagal gate bukan hukuman; reviewer wajib menulis *apa yang kurang* dan *bukti apa yang dibutuhkan* (aturan 4, OPS-03).

## 6. Research handoff

Setiap kali riset berpindah tahap (Course → Metopen → TA → AI Center), isi [TPL-14](../../research-os/08-templates/14-research-handoff-template.md): **what exists, missing evidence, next steps, owner**. Peta handoff antar MK ada di [hub §7](../README.md).

Tanggung jawab dosen pengirim: menandatangani handoff hanya bila *missing evidence* terisi jujur. Tanggung jawab dosen penerima: memulai dari handoff, bukan dari nol. Handoff tanpa penerima yang disebut namanya belum selesai.

## 7. Mendaftarkan problem dan dataset

| Yang Anda punya | Lakukan | Hasil |
|---|---|---|
| Masalah riset (dari riset Anda, partner, KP, atau kelas) | Buka Issue **Research Problem** ([`research-backlog/`](../../research-backlog/README.md)): cluster, domain, problem owner, potential dataset, maturity, related courses, potential output, priority | Masuk problem bank; `UIAI-YYYY-NNN` saat divalidasi G2; mahasiswa dapat memilihnya |
| Dataset (milik Anda, publik, partner) | Isi kartu dataset [TPL-05](../../research-os/08-templates/05-dataset-registry-template.md) di [`datasets-registry/`](../../datasets-registry/README.md) — **metadata saja**; privasi & lisensi diisi | `DS-YYYY-NNN`; dataset dapat dipakai kelas dan Metopen |
| Kebutuhan tooling | Issue **Artifact** (`type:artifact`) | Kandidat proyek RPL/Proyek PL |
| Kepakaran Anda | Isi baris Anda di peta dosen ([AIR-03](../../research-os/03-ai-research-ecosystem/03-faculty-research-alignment.md), [TPL-07](../../research-os/08-templates/07-faculty-research-map-template.md)) | Mahasiswa dan Mission Control dapat mencocokkan mentor |

Prinsip: bukan mengubah semua dosen menjadi AI researcher, tetapi menemukan *adjacency* AI dari kepakaran yang sudah ada.

## 8. Peran di Research Mission Control

Mission Control ([GOVERNANCE.md §9](../../GOVERNANCE.md)) adalah GitHub Project yang melacak semua riset. Peran dosen:

| Peran | Yang dilakukan di Mission Control |
|---|---|
| Pengampu MK mode R | Memastikan tim yang lanjut punya item dengan field **Course** = MK Anda dan **Entry Door** = Course Project |
| Mentor / pembimbing | Mengisi field **Faculty Mentor**, memperbarui **Research Gate** saat PR gate merge, menulis **Next Evidence** |
| Reviewer (`@reviewers`) | Mengambil PR `GATE REVIEW` yang berstatus `status:review` sesuai klaster |
| Ketua klaster (`@research-leads`) | Membaca view *By Research Cluster* dan *Faculty Portfolio* untuk perencanaan hibah/BKD |

Leaderboard mengurutkan **kematangan riset**, bukan orang ([TPL-03](../../research-os/08-templates/03-research-leaderboard-template.md)). Field yang paling berguna untuk dosen: *Research Gate*, *Maturity*, *Next Evidence*.

## 9. Kaitan BKD dan skema penelitian internal

Dokumen diskusi mencatat bahwa skema penelitian internal UAI mendorong keterlibatan mahasiswa — pada call yang ditemukan, minimal **dua mahasiswa aktif** dilibatkan — dan mengarahkan topik agar terkait Renstra Penelitian universitas. *(Catatan verifikasi: rujuk panduan skema penelitian internal dan aturan BKD terkini sebelum dipakai dalam pengajuan; angka dan syarat dapat berubah per tahun.)*

Implikasi praktis untuk dosen:

| Peluang | Bagaimana pipeline ini membantu |
|---|---|
| Proposal penelitian internal | Research Pack Metopen yang selaras riset Anda = bahan proposal siap pakai; tim mahasiswa sudah terbentuk (syarat ≥ 2 mahasiswa terpenuhi secara alami) |
| BKD penelitian & pembimbingan | Mission Control view *Faculty Portfolio* + PR review yang tersimpan = bukti pembimbingan dan review yang terdokumentasi |
| Publikasi bersama mahasiswa | Pipeline `manuscript-ready → submission-ready → submitted → accepted → published` di [`publications/`](../../publications/README.md) dengan `PUB-` |
| Pelaporan PP-PTS / akreditasi | Artefak kelas → CPMK → bukti terpetakan ([GOV-05](../../research-os/07-governance/05-ppts-and-institutional-evidence.md)) |

GitHub tetap *research tracking system*, bukan sistem kepegawaian; angka BKD tetap dihitung lewat mekanisme resmi.

## 10. FAQ dosen

**1. Mata kuliah saya teoretis (Matematika Diskrit). Apa hubungannya dengan riset?**
Mode F. Yang diminta hanya satu: mahasiswa menulis bukti/counterexample untuk satu klaim dan menyadari bahwa klaim bisa salah — embrio *falsification*. Tidak ada dataset, tidak ada eksperimen.

**2. Apakah saya wajib membimbing riset atau memakai GitHub?**
Tidak. Mode F/E tidak mewajibkan GitHub. Mode R mewajibkan artefak tercatat, dan cara termudahnya adalah repo kelas + kartu dataset. Pembimbingan riset hanya untuk dosen yang menjadi mentor/pembimbing.

**3. Berapa waktu tambahan yang realistis?**
Desain awal: satu sesi workshop + 2–3 jam. Per semester: review milestone (yang menggantikan koreksi tugas lama, bukan menambahnya) dan 20 menit/tim/minggu (dua mingguan untuk MK teknis).

**4. Bagaimana kalau mahasiswa memakai AI untuk seluruh tugas?**
Itu terjadi bila yang dinilai adalah dokumen. Nilailah bukti: Experiment Card sebelum hasil, peer reproduction, AI Usage Log dengan verifikasi, presentasi 7 menit dengan pertanyaan "angka ini dibanding apa?". Protokol lengkap di [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md).

**5. Data kelas saya mengandung data mahasiswa/partner. Boleh masuk repo?**
Tidak. Hanya kartu metadata yang masuk `datasets-registry/`; data fisik di server institusi/Drive dengan anonimisasi ([SECURITY.md](../../SECURITY.md)). Nilai privasi kartu harus terisi sebelum data dipakai.

**6. Proyek kelas saya tidak selesai di akhir semester. Apakah sia-sia?**
Tidak, bila artefaknya tercatat: dataset card, Issue backlog, dan handoff dengan *missing evidence*. Angkatan berikutnya atau tim Metopen melanjutkannya — itulah *research assets should compound*.

**7. Bagaimana kalau hasil eksperimen mahasiswa buruk (model kalah dari baseline)?**
Itu hasil yang sah dan sering lebih berharga. Nilai kejujuran laporan, error analysis, dan threats to validity. Menyembunyikan hasil negatif adalah pelanggaran amanah epistemik.

**8. Siapa yang memberi Research ID, Dataset ID, dan Artifact ID?**
`UIAI-` oleh `@maintainers` saat Issue lolos G2; `DS-` oleh pengelola datasets-registry; `ART-`/`PUB-` oleh pengelola publications/AI Center ([GOVERNANCE.md §5](../../GOVERNANCE.md)). Dosen tidak perlu menomori sendiri.

## 11. Checklist semester dosen

**Sebelum semester**
- [ ] Mode MK ditetapkan (F/E/R) dan tercatat di [hub §4](../README.md).
- [ ] 1–3 sel ARC-01 §7 dipilih; CPMK riset ditulis dengan kerangka ARC-05 (contoh di `courses/<mk>/README.md` §4).
- [ ] 3–5 tema dari backlog/registry disiapkan; Issue *Research Problem* dibuka bila tema baru.
- [ ] Milestone (4–5) dan rubrik research-quality dimasukkan ke RPS; `research-artifact.md` MK diperbarui bila ada folder.
- [ ] Template yang dipakai (TPL-05/09/10/15) disalin ke materi kelas.

**Selama semester**
- [ ] Tim membuat repo di minggu 2; AI Usage Log dimulai.
- [ ] Experiment Card / dataset card ber-commit sebelum hasil (cek tanggal).
- [ ] Bimbingan 20 menit dengan format §5.1; catatan 3 baris tersimpan di Issue/PR.
- [ ] Peer reproduction dijadwalkan (minggu 12–13).
- [ ] Integritas diperiksa di setiap milestone (sitasi, data sensitif, AI disclosure).

**Akhir semester**
- [ ] Artefak wajib per tim dinilai dengan rubrik; Integrity Checklist ditandatangani tim.
- [ ] Dataset card diserahkan ke registry; Issue backlog diperbarui.
- [ ] Handoff [TPL-14](../../research-os/08-templates/14-research-handoff-template.md) untuk tim yang lanjut ke Metopen/AI Center; penerima disebut namanya.
- [ ] Baris status MK di [hub §5](../README.md) diperbarui; ringkasan artefak dikirim ke koordinator komponen (bukti OBE/akreditasi).
- [ ] Satu paragraf refleksi: apa yang diubah semester depan (mode naik? milestone digeser?).
