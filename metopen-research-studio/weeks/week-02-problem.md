# Week 02 — Problem

> **Sprint** S2 · **Gate** G2 Problem Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-01-endgame.md) / [Week berikutnya →](week-03-search.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Masalahnya adalah ___, penting bagi ___ karena ___"** — dan orang di luar tim dapat mengulanginya dalam dua kalimat tanpa menyebut satu pun nama algoritma. Masalah dinyatakan *problem-first* di `docs/problem.md` (Problem Brief + Stakeholder & Impact Statement) dengan bukti dari stakeholder nyata, dipetakan ke klaster C1–C4 dan domain roadmap, diringkas ke Research One-Pager v0, lalu dikumpulkan dalam PR `GATE REVIEW: Problem Ready`. Bila lulus, `@maintainers` memberi Research ID resmi `UIAI-YYYY-NNN` dan release `v0.1 Problem Validated` dibuat — inilah primary key yang mengikuti riset Anda sampai TA dan publikasi.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (solution-first vs problem-first, problem worth solving, stakeholder & impact), **60 menit studio** (latihan mundur dari solusi ke masalah, menulis Problem Brief, peer test dua kalimat lintas tim), **10 menit gate check** (tiap tim membacakan kalimat masalahnya; tim lain mengulang dalam dua kalimat). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md); sprint goal dari [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S2.

## Concept (30 menit)

1. **Solution-first adalah pola TA yang paling sering gagal G2.** "Saya ingin menggunakan Random Forest untuk memprediksi X" memilih algoritma sebelum masalahnya dipahami ([MET-01](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §4.2). Minggu ini Anda dipaksa mundur; algoritma boleh muncul lagi di W7 — sebagai jawaban atas pertanyaan, bukan titik awal.
2. **Rantai "mengapa" lima level.** Mengapa X perlu diprediksi/diukur? → siapa stakeholder-nya? → keputusan apa yang berubah jika hasilnya tersedia? → bagaimana stakeholder menanganinya sekarang (baseline lapangan)? → apa yang belum bisa dijawab cara itu? Pilih level yang paling konkret sekaligus paling bermakna ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §2).
3. **Problem framing** = kesenjangan antara keadaan sekarang dan keadaan yang diinginkan, dari sudut pandang orang yang mengalaminya. Framing menentukan literatur apa yang dicari (W3), metrik apa yang bermakna (W7), dan apakah hasil riset akan mengubah keputusan siapa pun.
4. **Problem worth solving** memenuhi empat syarat: nyata (ada pemiliknya), penting sekarang (ada alasan waktunya), ada pemangku kepentingan yang bisa disebut perannya, dan ada konteks Indonesia/UAI/domain. Tulis juga apa yang terjadi bila masalah dibiarkan.
5. **Evidence of need harus bersumber.** Kutipan wawancara (peran + tanggal), angka dari dokumen resmi yang bisa dibuka, atau konfirmasi dosen pemilik masalah. "Statistik masalah" tanpa sumber — apalagi dari AI — adalah kelemahan umum Problem Brief ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.1).
6. **Stakeholder & Impact Statement** menjawab tiga hal: siapa (primer/sekunder), keputusan apa yang berubah bila riset berhasil, dan siapa yang dirugikan bila hasilnya salah. Contoh baik: "Tim akademik Prodi memakai prediksi ini untuk memutuskan intervensi di minggu ke-4." Contoh lemah: "Bermanfaat bagi masyarakat luas."
7. **Klaster ≠ domain.** Klaster primer (C1–C4) = *apa yang baru bila riset berhasil* (model/data, sistem/keamanan, manusia/nilai, dampak domain); domain roadmap (Education, Halal, Health, Food, Government, Business, Social Impact) = mitra dan dataset. Satu klaster primer wajib, maksimal satu sekunder ([AIR-02](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) §8–9).
8. **Uji dua kalimat** adalah kriteria lulus G2: reviewer di luar tim menulis ulang masalah (kalimat 1) dan mengapa penting untuk siapa (kalimat 2) tanpa bertanya ke tim.
9. **Research ID resmi lahir di gate ini.** Sebelum G2 lulus Anda memakai `UIAI-YYYY-…` (ID sementara); setelah merge, `@maintainers` memberi `UIAI-YYYY-NNN` yang mengikat Issue → repo → Metopen → TA → dataset → publikasi ([GOVERNANCE.md](../../GOVERNANCE.md) §skema identitas).
10. **Etika mulai dari wawancara pertama.** Izin sebelum mencatat, sebut peran bukan nama, kontak dan rekaman disimpan di luar repositori ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §4, [SECURITY.md](../../SECURITY.md)).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membaca catatan: *"Mengapa masalah ini perlu diselesaikan, siapa yang peduli, dan keputusan apa yang berubah bila riset kami berhasil — tanpa menyebut satu pun nama metode?"*

## Tasks

Semua task Sprint S2 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add problem brief v0 (OPS-017)`. Task yang belum selesai dari W1 ditulis di atas tabel ini pada salinan tim.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-015 | Ikuti sesi Problem Discovery dan latihan problem-first | Latihan problem-first | 2h | Memberi contoh judul solution-first untuk dilatih; jawaban ditulis mahasiswa | Mahasiswa menjelaskan mengapa versi problem-first lebih baik |
| OPS-016 | Wawancara atau observasi stakeholder masalah | Catatan stakeholder | 3h | Membantu menyusun daftar pertanyaan wawancara; tidak menggantikan wawancara | Tim memastikan catatan berasal dari sumber nyata dan izin diperoleh |
| OPS-017 | Tulis Problem Brief | docs/problem.md | 3h | Mengkritik struktur dan kejelasan; menantang apakah masalah nyata | Dosen dan peer memeriksa masalah dapat dijelaskan ulang dalam 2 kalimat |
| OPS-018 | Tulis Stakeholder & Impact Statement | Bagian Stakeholder & Impact di docs/problem.md | 1.5h | Menawarkan stakeholder yang mungkin terlewat; tim memverifikasi relevansinya | Tim memastikan tiap stakeholder nyata, bukan hipotetis |
| OPS-019 | Selaraskan masalah dengan klaster dan domain roadmap | Bagian Alignment di docs/problem.md | 1h | - | Dosen mengonfirmasi klaster dan domain |
| OPS-020 | Lengkapi Research One-Pager v0 | docs/one-pager.md v0 | 1h | Meringkas problem brief menjadi 3 kalimat; tim mengedit | Tim memeriksa One-Pager tidak mendahului bukti literatur |
| OPS-021 | Perbarui Issue backlog dan ajukan permohonan Research ID resmi | Issue diperbarui; permohonan Research ID tercatat | 0.5h | - | @maintainers menetapkan ID saat G2 merge; tim memeriksa konsistensi ID di semua file |
| OPS-022 | Siapkan PR GATE REVIEW: Problem Ready (problem-review.md) | PR GATE REVIEW: Problem Ready | 1.5h | - | Dosen + peer memeriksa masalah problem-first dan dapat dijelaskan ulang |
| OPS-023 | Perbarui AI Usage Log dan jurnal mingguan W2 | AI Usage Log W2 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 14h** (jam tim; untuk tim 2 orang bagi dua). Sprint ini tergolong sedang; yang paling mahal bukan jamnya, melainkan **jadwal orang lain** — janji wawancara (OPS-016) seharusnya sudah dibuat di W1 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §S2).

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-015** di sesi studio dan **OPS-016** (keduanya hanya bergantung pada task S1) → **OPS-017** Problem Brief (butuh PR G1 termerge, latihan, dan catatan stakeholder; ini task dengan dependen terbanyak di seluruh WBS, kerjakan dulu) → **OPS-018** dan **OPS-019** paralel → **OPS-020** One-Pager v0 → **OPS-021** perbarui Issue → **OPS-022** PR G2 (butuh 017–021); **OPS-023** berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g2-problem`, harus ada:

| Artefak | Lokasi di repositori ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §4) | Bentuk bukti | Task |
|---|---|---|---|
| **Problem Brief** 1–2 halaman: fenomena/masalah nyata, konteks Indonesia/UAI, mengapa penting sekarang, apa yang terjadi bila dibiarkan, batasan — **tanpa nama metode** | `docs/problem.md` §Problem Brief | commit di `research/g2-problem` | OPS-017 |
| **Evidence of Need**: kutipan/angka dari wawancara, observasi, atau dokumen resmi, dengan sumber (peran narasumber, tanggal; tanpa data pribadi) | `docs/problem.md` §Evidence of Need | commit | OPS-016 |
| **Stakeholder & Impact Statement**: tabel peran · kepentingan · keputusan yang berubah · risiko bila salah (minimal 2 stakeholder) + paragraf dampak | `docs/problem.md` §Stakeholder & Impact | commit | OPS-018 |
| **Alignment**: klaster primer C1–C4 (+ sekunder bila ada), domain roadmap, 3 kalimat alasan | `docs/problem.md` §Alignment; label `cluster:*` pada Issue | commit + label Issue | OPS-019 |
| Research One-Pager v0: field Problem & why, Stakeholder, Expected contribution (tentatif) terisi; RQ/Method/Data/Baseline bertanda `[belum diisi — target G3–G5]` | `docs/one-pager.md` ([TPL-01](../../research-os/08-templates/01-research-one-pager-template.md)) | commit dengan tag `one-pager-v0` | OPS-020 |
| Issue `type:problem` diperbarui (tautan `docs/problem.md`, cluster, domain, owner, maturity, priority) dan permintaan Research ID ke `@maintainers` | Issue di repo pusat (form [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml)); setelah ID diberikan, ganti `UIAI-YYYY-…` (ID sementara) di judul Issue, README riset, dan One-Pager | komentar Issue + commit | OPS-021 |
| Latihan problem-first (judul solution-first → versi problem-first dengan 5 pertanyaan mundur) + jurnal W2: bukti apa yang paling meyakinkan bahwa masalah nyata | `docs/journal/w02.md` | commit | OPS-015, OPS-023 |
| AI Usage Log W2 (termasuk saran AI yang ditolak dan alasannya) | `docs/ai-usage-log.md`, ringkasan di `docs/AI-USAGE.md` ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-023 |
| **PR `GATE REVIEW: Problem Ready`** memakai template [problem-review.md](../../.github/PULL_REQUEST_TEMPLATE/problem-review.md), reviewer dosen pengampu + 1 peer | PR dari `research/g2-problem` ke branch utama repo riset | URL PR; setelah merge: label `gate:G2-problem`, release `v0.1 Problem Validated` | OPS-022 |

README riset diperbarui: `Current Research Gate: G2 (in review)` pada Senin, `G2 passed` setelah merge, dan Research ID resmi menggantikan `UIAI-YYYY-…` (ID sementara). Release `v0.1 Problem Validated` berisi artefak Research Pack #1–#2 ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §7).

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan**, bukan Jumat. Minggu ini AI paling berguna sebagai **kritikus**, bukan penulis.

**Boleh minggu ini**

- Meminta AI memberi contoh judul TA solution-first tambahan untuk dilatih ditulis ulang menjadi problem-first (OPS-015) — jawaban dan rantai "mengapa" ditulis mahasiswa.
- Meminta AI membantu menyusun 5–7 pertanyaan wawancara terbuka dan mengkritik pertanyaan yang menggiring (OPS-016) — wawancaranya tetap dilakukan manusia dengan izin narasumber.
- Meminta AI mengkritik struktur dan kejelasan Problem Brief, dan menantang: "apakah masalah ini nyata? bagian mana yang masih solution-first?" (OPS-017).
- Meminta AI menawarkan stakeholder yang mungkin terlewat (primer/sekunder, siapa yang dirugikan bila salah), lalu tim memverifikasi relevansinya ke sumber nyata (OPS-018).
- Meminta AI meringkas Problem Brief menjadi 3 kalimat untuk One-Pager (OPS-020), lalu tim mengedit sampai setiap kata bisa dipertanggungjawabkan.
- Berperan sebagai "orang luar" dalam latihan uji dua kalimat sebelum peer test sungguhan.

**Tidak boleh**

- Mengambil "statistik masalah", kutipan, atau referensi dari AI tanpa sumber yang bisa dibuka; Evidence of Need hanya boleh berisi apa yang tim saksikan atau baca sendiri.
- Menulis Problem Brief atau Stakeholder Statement seluruhnya oleh AI — framing dari AI tidak punya pemilik, dan gate gagal bila tim tidak bisa menjelaskannya tanpa AI.
- Mengarang stakeholder atau menerima stakeholder usulan AI yang tidak diverifikasi ke orang/dokumen nyata.
- Memasukkan transkrip wawancara, nama/kontak narasumber, data mahasiswa, atau data partner ke layanan AI ([SECURITY.md](../../SECURITY.md)).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-019 (keselarasan klaster/domain), OPS-021 (Issue & Research ID), OPS-022 (PR gate), OPS-023 (log & jurnal) — keempatnya adalah penilaian dan pertanggungjawaban manusia.

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa dapat menjelaskan mengapa versi problem-first lebih baik daripada judul solution-first asalnya, tanpa membaca catatan | diri sendiri, diuji peer di 10 menit gate check | OPS-015 |
| Catatan stakeholder berasal dari sumber nyata (peran, tanggal), izin diperoleh sebelum dicatat, tidak ada data pribadi di repositori | tim (dua anggota membaca ulang sebelum commit) | OPS-016 |
| Masalah dapat dijelaskan ulang dalam dua kalimat oleh orang di luar tim; tidak ada nama metode di bagian masalah | peer dari tim lain (peer test di studio), lalu dosen pengampu + peer reviewer di PR | OPS-017, OPS-022 |
| Setiap stakeholder di tabel nyata (bisa ditunjuk perannya), bukan hipotetis; keputusan yang berubah konkret | tim; mentor bila sudah ada | OPS-018 |
| Klaster primer dan domain sesuai dengan *apa yang baru bila riset berhasil*, bukan sekadar topik | dosen pengampu (konfirmasi saat gate check) | OPS-019 |
| One-Pager v0 tidak mendahului bukti: RQ/Method/Data/Baseline masih bertanda menunggu G3–G5; isi Problem & Stakeholder identik dengan `docs/problem.md` | tim; peer membaca 3 menit | OPS-020 |
| Research ID resmi diberikan dan konsisten di judul Issue, README riset, One-Pager, dan `docs/problem.md` | `@maintainers` memberi ID; tim memeriksa konsistensi | OPS-021 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya (tool, tujuan, verifikasi, dipakai/ditolak) | diri sendiri | OPS-023 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint).

## Done When

Minggu ini **menutup gate G2 Problem Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] PR `GATE REVIEW: Endgame Ready` (G1) sudah termerge — G2 tidak dapat dibuka sebelum G1 lulus.
- [ ] `docs/problem.md` §Problem Brief: fenomena nyata, konteks Indonesia/UAI, mengapa penting sekarang, apa yang terjadi bila dibiarkan, batasan; **kalimat pertama menyebut masalah, bukan metode**; tidak ada nama algoritma di seluruh bagian masalah.
- [ ] `docs/problem.md` §Evidence of Need memuat minimal satu bukti bersumber (wawancara/observasi/dokumen resmi) dengan peran narasumber dan tanggal, tanpa data pribadi.
- [ ] `docs/problem.md` §Stakeholder & Impact: tabel minimal 2 stakeholder dengan keputusan yang berubah dan risiko bila salah; paragraf dampak ditulis.
- [ ] `docs/problem.md` §Alignment: satu klaster primer C1–C4, domain roadmap, 3 kalimat alasan; label `cluster:*` terpasang di Issue.
- [ ] `docs/one-pager.md` v0 ter-tag `one-pager-v0`; field 7–8 terisi, field RQ/Method/Data/Baseline bertanda `[belum diisi — target G3–G5]`, tidak ada field kosong.
- [ ] Issue `type:problem` diperbarui dan `@maintainers` diminta memberi Research ID; setelah diberikan, `UIAI-YYYY-…` (ID sementara) diganti di semua file.
- [ ] `docs/journal/w02.md` berisi latihan problem-first dan jawaban "bukti apa yang paling meyakinkan bahwa masalah ini nyata"; `docs/ai-usage-log.md` mutakhir.
- [ ] Peer dari tim lain berhasil mengulang masalah dan mengapa penting dalam dua kalimat tanpa bertanya.
- [ ] PR **`GATE REVIEW: Problem Ready`** termerge oleh dosen pengampu + 1 peer reviewer; label `gate:G2-problem`; release `v0.1 Problem Validated` dibuat; README §Current Research Gate diperbarui.

**Ringkasan gate G2** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G2). **Lulus jika** orang di luar tim dapat menjelaskan ulang masalah dan mengapa penting dalam dua kalimat. **Gagal jika** masalah hanya justifikasi untuk algoritma yang sudah dipilih — atau bila ada pelanggaran integritas (stakeholder/angka dikarang, penggunaan AI tidak diungkap), terlepas dari kualitas lainnya. Reviewer: dosen pengampu + 1 peer reviewer. Gagal gate bukan hukuman: reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan, tim merevisi, review dibuka ulang.

**Cara membuka PR gate** ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3): (1) pastikan semua bukti di tabel Deliverable ada di branch `research/g2-problem`; (2) buka PR berjudul `GATE REVIEW: Problem Ready — UIAI-YYYY-… (ID sementara)` memakai template [problem-review.md](../../.github/PULL_REQUEST_TEMPLATE/problem-review.md) (tambahkan `?template=problem-review.md` pada URL *Compare & pull request* atau salin isinya); (3) isi ringkasan Problem Brief, tabel stakeholder, bagian *Uji problem-first* (baseline lapangan, apa yang belum terjawab), tabel Evidence, dan AI Usage; (4) tautkan nomor PR G1 dan nomor Issue `type:problem`; (5) minta review dosen pengampu + 1 peer, dan minta reviewer mengisi bagian *uji dua kalimat*; (6) setelah merge: `@maintainers` memberi Research ID, label → `gate:G2-problem`, buat release `v0.1 Problem Validated`. Komentar review disimpan, tidak dihapus.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-01 Research One-Pager Template](../../research-os/08-templates/01-research-one-pager-template.md) — `docs/one-pager.md` v0 (field 7 Problem & why, 8 Stakeholder, 12 Contribution draft, 19 Next evidence, 20 Gate).
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — `docs/ai-usage-log.md` dan `docs/AI-USAGE.md`.
- [TPL-04 Research Backlog Template](../../research-os/08-templates/04-research-backlog-template.md) — bentuk kartu masalah `problems/UIAI-YYYY-NNN-slug.md` yang dibuat setelah Research ID diberikan.
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `docs/problem.md`, branch `research/g2-problem`.
- Form Issue [Research Problem](../../.github/ISSUE_TEMPLATE/01-research-problem.yml) dan template PR [problem-review.md](../../.github/PULL_REQUEST_TEMPLATE/problem-review.md).

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W2 · [MET-01 Positioning](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) §4.2 solution-first vs problem-first · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.1–3.2 Problem Brief & Stakeholder/Impact · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.1 E1 End · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §4 human subjects.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §2 problem framing (latihan Rantai Mengapa) · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 izin/larangan.
- [AIR-02 AI Research Clusters](../../research-os/03-ai-research-ecosystem/02-ai-research-clusters.md) §8–9 · [Research Roadmap](../../research-roadmap/README.md) — [klaster](../../research-roadmap/clusters/ai-models-data-knowledge.md) dan [domain](../../research-roadmap/domains/education.md) · [Research Backlog](../../research-backlog/README.md) §1 alur Research ID · [GOVERNANCE.md](../../GOVERNANCE.md).
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S2 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G2 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §S2 dan skenario "G2 terlambat 1 minggu" · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Solution-first yang tersembunyi.** Paragraf pertama sudah "problem", tetapi paragraf kedua berbunyi "oleh karena itu digunakan metode M". Cara menghindari: cari setiap nama algoritma/model/framework di `docs/problem.md` dan hapus; jika masalahnya runtuh tanpa nama itu, masalahnya belum ada — ulangi rantai "mengapa".
2. **Statistik masalah tanpa sumber.** "70% mahasiswa terlambat lulus" tanpa dokumen yang bisa dibuka, atau angka yang dihasilkan AI. Cara menghindari: setiap angka di Problem Brief menunjuk dokumen resmi, wawancara (peran + tanggal), atau dihapus; referensi ilmiah menunggu verifikasi di W3.
3. **Stakeholder dikarang atau terlalu umum.** "Bermanfaat bagi masyarakat luas" tidak lolos uji dua kalimat karena tidak ada keputusan yang berubah. Cara menghindari: untuk tiap baris tabel stakeholder tulis peran spesifik dan satu keputusan konkret; bila tidak bisa menunjuk orang/unit nyata, hapus barisnya.
4. **Masalah terlalu luas atau tanpa pemilik.** "Pendidikan Indonesia" bukan masalah yang bisa dijawab dalam satu semester + TA. Cara menghindari: pilih level rantai "mengapa" yang paling konkret sekaligus bermakna; tulis batasan (populasi, konteks, jangka waktu) secara eksplisit.
5. **Wawancara ditunda, atau narasumber masuk repositori.** Menunggu jadwal stakeholder membuat OPS-017 mundur dan seluruh S2 ikut mundur; sebaliknya, transkrip lengkap dengan nama dan kontak di-commit ke repo publik. Cara menghindari: bila wawancara tak kunjung terjadwal, pakai telaah dokumen resmi + satu wawancara singkat daring ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) skenario G2 terlambat); simpan hanya kutipan, peran, dan tanggal di repo, sisanya di luar ([SECURITY.md](../../SECURITY.md)).
6. **One-Pager mendahului bukti.** Tergoda mengisi RQ, metode, dan dataset sekarang karena "sudah tahu mau apa". Cara menghindari: biarkan field itu bertanda `[belum diisi — target G3–G5]`; RQ yang ditulis sebelum synthesis matrix tidak dianggap valid ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G4).
