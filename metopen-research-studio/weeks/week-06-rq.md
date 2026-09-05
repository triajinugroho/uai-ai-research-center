# Week 06 — RQ

> **Sprint** S6 · **Gate** G4 Question Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-05-gap.md) / [Week berikutnya →](week-07-method.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Maka kami bertanya ___ dan akan berkontribusi ___."** RQ dan/atau hipotesis (1–3 buah) yang spesifik, dapat difalsifikasi, dan terjangkau dalam semester + TA ditulis di `docs/research-question.md`; setiap RQ ditelusuri ke gap final dan ke baris tertentu di synthesis matrix; Contribution Statement menyebut jenis kontribusi dan tidak melebihi apa yang RQ dapat buktikan ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W6; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S6). Semua bukti dikumpulkan dalam PR `GATE REVIEW: Question Ready` yang direview dosen pengampu + mentor. Sprint ini ringan secara jam (12 jam tim) tetapi berat secara berpikir — jangan diisi task lain, dan ingat RQ tidak sah sebelum PR G3 termerge.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (anatomi RQ, hipotesis yang bisa salah, jenis kontribusi, scoping), **60 menit studio** (tim menulis tabel Gap–Evidence–Claim dan draft RQ; mentor berkeliling menanyakan "baris mana di matriks yang membuat RQ ini perlu?"), **10 menit gate check** (tiap tim membacakan satu RQ beserta hasil yang akan membatalkannya). Ritme Senin–Jumat mengikuti [OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md), yang memakai minggu ini sebagai contoh terisi.

## Concept (30 menit)

1. **RQ tidak valid sebelum G3 selesai.** RQ yang lahir sebelum matriks lengkap hanyalah preferensi; ia tidak dapat ditelusuri ke baris matriks. Karena itu OPS-051 baru boleh dimulai setelah PR `GATE REVIEW: Evidence Ready` termerge — blocking rule B3 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules; [OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G4).
2. **Gap–Claim–Evidence alignment.** Gap final ditulis sebagai satu tabel: *Gap* (apa yang belum diketahui/bertentangan/belum diuji) | *Evidence* (nomor baris matriks + sumber) | *Claim* (apa yang ingin diuji). Klaim awal dari `docs/endgame.md` (W1) direvisi agar sesuai bukti, bukan sebaliknya ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.4).
3. **Anatomi RQ:** konstruk (apa yang diukur), konteks (data/populasi/lingkungan), pembanding (baseline B), batas (apa yang tidak dijawab). Kuat: *"Apakah pada data D, metode M mengungguli baseline B pada metrik μ ≥ Δ?"* Lemah: *"Bagaimana penerapan M untuk X?"* ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.5).
4. **Hipotesis yang bisa salah** menyebut arah, variabel, pembanding, dan **kriteria penolakan**; Δ yang berarti secara praktis ditentukan dari sudut stakeholder, bukan dari AI. Tulis juga hipotesis nol dan satu hipotesis saingan ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §6).
5. **Falsifikasi sebagai kebiasaan:** untuk tiap RQ tuliskan *hasil apa yang akan membatalkannya* sebelum satu pun data dilihat. RQ yang tidak punya jawaban "salah" bukan RQ riset ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §7).
6. **Scoping:** satu RQ utama, maksimal dua RQ pendukung; harus terjawab dalam batas semester Metopen + TA dengan data yang lazim di literatur (`docs/literature/common-metrics-baselines.md`, W4).
7. **Jenis kontribusi computing:** empiris, artefak, metode, dataset, replikasi, studi kasus ([ARC-06](../../research-os/02-academic-architecture/06-research-output-taxonomy.md) §2). Kontribusi dinyatakan sebagai *"bermakna karena ___"* untuk stakeholder dan literatur; kata "pertama di Indonesia" atau "novel framework" tanpa bukti dilarang ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.6).
8. **Kontribusi ≤ bukti yang mungkin dihasilkan.** Versi G4 adalah janji yang sepadan dengan RQ; ia akan direvisi lagi setelah pilot di G7. Klaim yang melebihi RQ menurunkan E1 ke *Developing* ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.1).
9. **RQ tidak diubah diam-diam.** Setiap perubahan rumusan setelah minggu ini dicatat dengan alasan dan tanggal; mengubah RQ setelah melihat hasil adalah HARKing — pertanyaan integritas G4 ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §6).
10. **Metode menunggu RQ**, bukan sebaliknya (blocking rule B4). One-Pager v1 boleh memuat draft metode/data/baseline, tetapi ditandai tentatif sampai G5.

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membuka catatan: *"Untuk setiap RQ kami — baris mana di synthesis matrix yang membuatnya perlu, dan hasil apa yang akan membuatnya salah?"*

## Tasks

Semua task Sprint S6 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add RQ1-RQ2 with falsifying results (OPS-052)`. Task W5 yang belum selesai — terutama OPS-047 PR G3 — ditulis di atas tabel ini pada salinan tim; selama PR G3 belum termerge, OPS-051 dan seterusnya hanya boleh dikerjakan sebagai *draft bersyarat*.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-050 | Ikuti sesi RQ, Claim & Contribution | Latihan RQ | 2h | Memberi contoh RQ lemah untuk diperbaiki | Mahasiswa menjelaskan mengapa RQ hasil perbaikan lebih dapat dijawab |
| OPS-051 | Tulis Research Gap final dengan Gap-Claim-Evidence alignment | docs/research-question.md bagian Gap | 2h | Menantang konsistensi antara gap dan klaim | Dosen memeriksa gap ditelusuri ke baris matriks tertentu |
| OPS-052 | Rumuskan 1-3 RQ dan/atau hipotesis yang dapat difalsifikasi | RQ/hipotesis dalam docs/research-question.md | 2h | Mengusulkan variasi rumusan RQ dan menguji keterjawaban; tim memilih | Dosen dan mentor memeriksa RQ spesifik dan dapat dijawab |
| OPS-053 | Tulis Contribution Statement | docs/research-question.md bagian Contribution | 1.5h | Mengkritik kontribusi yang melebihi RQ | Tim memastikan kontribusi tidak melebihi apa yang RQ dapat buktikan |
| OPS-054 | Uji RQ dengan checklist keterjawaban dan falsifiabilitas | Checklist RQ terisi | 1.5h | Berperan sebagai reviewer skeptis terhadap RQ | Tim menuliskan hasil yang akan membatalkan tiap RQ |
| OPS-055 | Perbarui Research One-Pager ke v1 (problem-gap-RQ-contribution) | docs/one-pager.md v1 | 1h | Meringkas; tim mengedit dan memverifikasi | Tim memeriksa v1 konsisten dengan research-question.md |
| OPS-056 | Buka Issue type:research-question | Issue type:research-question | 0.5h | - | Tim memeriksa RQ di Issue identik dengan dokumen |
| OPS-057 | Siapkan PR GATE REVIEW: Question Ready | PR GATE REVIEW: Question Ready | 1h | - | Dosen + mentor memeriksa tiap RQ ditelusuri ke matriks |
| OPS-058 | Perbarui AI Usage Log dan jurnal mingguan W6 | AI Usage Log W6 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 12h** (jam tim; untuk tim 2 orang bagi dua). Jalur kritis 9 jam, slack 3 jam — kecil, dan sprint ini menunggu review G3 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer).

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai **OPS-050** di sesi studio dan **OPS-051** tabel Gap–Evidence–Claim (butuh gap terpilih OPS-046 dan PR G3 OPS-047 termerge) → **OPS-052** RQ dikerjakan *bersama seluruh tim*, bukan dibagi → **OPS-053** kontribusi → setelah 052 dan 053 selesai, **OPS-054** uji RQ dan **OPS-056** Issue RQ berjalan paralel oleh orang berbeda → **OPS-055** One-Pager v1 (butuh 054 dan One-Pager v0 dari W2) → **OPS-057** PR G4 setelah 051, 054, 055, 056 ada; **OPS-058** log dan jurnal berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g4-question`, harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Latihan sesi: 3 RQ lemah → RQ terukur + jenis kontribusi tiap contoh; jurnal W6: **apa yang berubah dari klaim awal W1 ke RQ sekarang** | `docs/journal/w06.md` | commit | OPS-050, OPS-058 |
| **§Gap** — tabel `Gap \| Evidence (baris matriks + sumber) \| Claim`; klaim awal `docs/endgame.md` direvisi; jenis gap disebut; ini Research Gap final yang dinilai di G4 (kandidatnya ada di `docs/literature-map.md` §Gap Candidates dari W5) | `docs/research-question.md` §Gap | commit; Issue `type:literature-gap` ditutup dengan tautan ke gap final | OPS-051 |
| **§RQ / Hypothesis** — 1 RQ utama + maks 2 pendukung; tiap RQ: konstruk, konteks, pembanding, batas, jawaban yang mungkin, **hasil yang membatalkan**, tautan gap + nomor baris matriks; hipotesis ditandai (arah, variabel, kriteria penolakan) | `docs/research-question.md` §RQ | commit | OPS-052 |
| **§Contribution** — jenis kontribusi + satu paragraf "kontribusi ini bermakna karena ___"; konsisten dengan RQ dan endgame | `docs/research-question.md` §Contribution | commit | OPS-053 |
| **§RQ Check** — checklist per RQ: data yang ada, metrik kandidat, hasil pembatal, waktu; RQ yang gagal direvisi dan perubahannya tercatat | `docs/research-question.md` §RQ Check | commit (riwayat revisi terlihat di log commit) | OPS-054 |
| **Research One-Pager v1**: field 9–12 (What we know, Gap, RQ, Contribution) wajib; Why diperbarui; field 13–16 (Method/Data/Baseline/Metrics) draft bertanda `tentatif — menunggu G5` | `docs/one-pager.md` | commit dengan tag `one-pager-v1` | OPS-055 |
| **Issue `type:research-question`** dari form [Research Question](../../.github/ISSUE_TEMPLATE/02-research-question.yml): RQ, hipotesis, baris matriks, kontribusi, jenis kontribusi; tertaut ke Issue `type:problem` dan `type:literature-gap` | GitHub Issue `[UIAI-YYYY-NNN] RQ: …` | nomor Issue dicatat di README riset dan One-Pager | OPS-056 |
| **PR `GATE REVIEW: Question Ready — UIAI-YYYY-NNN`** dari `research/g4-question` memakai template default | PR; label `gate:G4-question` setelah merge | URL PR; README §Current Research Gate | OPS-057 |
| AI Usage Log W6 dengan Stage `Gap`/`RQ`: contoh RQ lemah, tantangan konsistensi gap–klaim, variasi RQ, kritik kontribusi, reviewer skeptis, ringkasan One-Pager — dan keputusan manusia atas tiap output | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-058 |

G4 tidak memiliki release milestone ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §Peta gate); rilis berikutnya `v0.3 Research Design` dibuat di W8. Setelah PR termerge, README riset: `Current Research Gate: G4 (passed) → G5 (in progress)`.

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan**, Stage `Gap` atau `RQ`. Minggu ini AI paling berguna sebagai **lawan debat**, bukan sebagai penulis RQ: ia bagus untuk menantang, buruk untuk memutuskan ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.5–3.6).

**Boleh minggu ini**

- Meminta AI memberi contoh RQ lemah untuk diperbaiki sebagai latihan (OPS-050); perbaikannya ditulis dan dijelaskan sendiri.
- Meminta AI menantang konsistensi gap ↔ klaim: "apakah gap ini sudah dijawab di sub-bidang lain?" (OPS-051) — tanggapi dengan pencarian ulang yang dicatat, bukan dengan menerima jawabannya.
- Meminta AI mengusulkan variasi rumusan RQ dan menguji keterjawabannya (OPS-052); **tim yang memilih**, dan setiap RQ terpilih tetap harus menunjuk baris matriks.
- Brainstorming hipotesis alternatif dan hipotesis saingan, lalu meminta AI mencari cara hipotesis Anda bisa salah ([AIX-01](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §6–7) — tanyakan cara gagal, bukan konfirmasi.
- Meminta AI mengkritik Contribution Statement yang melebihi RQ (OPS-053) dan berperan sebagai reviewer skeptis saat mengisi RQ Check (OPS-054); kritik diklasifikasi terima/ubah/tolak dengan alasan di log.
- Meminta AI meringkas `research-question.md` ke format One-Pager (OPS-055); tim mengedit dan memverifikasi setiap field terhadap dokumen sumber.

**Tidak boleh**

- Memakai RQ atau gap buatan AI yang tidak dapat ditelusuri ke baris synthesis matrix ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W6) — "belum ada penelitian tentang X" adalah klaim yang AI tidak bisa buktikan.
- Membiarkan AI **memilihkan** RQ, hipotesis, atau Δ yang berarti; batas RQ dan ambang praktis adalah keputusan tim berdasarkan stakeholder dan waktu semester ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3).
- Menambahkan "bukti literatur" atau sumber baru lewat AI ke tabel alignment; sumber baru hanya masuk lewat pencarian tercatat dengan DOI/URL dibuka — satu referensi tidak terverifikasi membatalkan gate.
- Menyerahkan Contribution Statement hasil AI yang tim tidak mampu jelaskan, atau frasa "pertama di Indonesia"/"novel" tanpa baris matriks yang mendukung.
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-056 (Issue RQ), OPS-057 (PR gate), OPS-058 (log & jurnal); dan tidak memasukkan data stakeholder/pribadi ke prompt ([SECURITY.md](../../SECURITY.md)).

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa menjelaskan mengapa RQ hasil perbaikan lebih dapat dijawab daripada versi lemahnya | diri sendiri, diuji dosen di sesi studio | OPS-050 |
| Gap final ditelusuri ke baris matriks tertentu (nomor baris + sumber terverifikasi), bukan gap naratif | dosen pengampu | OPS-051 |
| Tiap RQ spesifik (konstruk, konteks, pembanding, batas) dan dapat dijawab dalam semester + TA; mentor menanyakan "baris mana di matriks yang membuat RQ ini perlu?" | dosen pengampu + mentor | OPS-052 |
| Kontribusi tidak melebihi apa yang RQ dapat buktikan; jenis kontribusi disebut; konsisten dengan endgame W1 | tim (dibaca ulang oleh anggota yang tidak menulisnya) | OPS-053 |
| Untuk tiap RQ tertulis **hasil yang akan membatalkannya**, data dan metrik kandidat ada, waktu masuk akal | tim; mentor bila tersedia | OPS-054 |
| One-Pager v1 konsisten kata demi kata dengan `research-question.md`; field 13–16 bertanda tentatif | tim | OPS-055 |
| RQ di Issue identik dengan RQ di dokumen; tautan ke Issue problem dan literature-gap ada | tim | OPS-056 |
| Tiap RQ ditelusuri ke matriks; definition of done G4 terpenuhi; integritas: RQ tidak diubah diam-diam dari gap | dosen pengampu + mentor (reviewer PR) | OPS-057 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya, khususnya RQ/hipotesis yang berasal dari saran AI dan keputusan manusia atasnya | diri sendiri | OPS-058 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W6, "dapat dibuka reviewer" berarti reviewer memilih satu RQ, membuka nomor baris matriks yang disebut, dan menemukan bahwa baris itu memang menunjukkan gap tersebut.

## Done When

Minggu ini **menutup gate G4 Question Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] PR `GATE REVIEW: Evidence Ready` (G3) sudah termerge — G4 tidak dapat dibuka sebelum G3 lulus (blocking rule B3).
- [ ] `docs/journal/w06.md` berisi latihan 3 RQ lemah → terukur dan refleksi "apa yang berubah dari klaim awal W1 ke RQ sekarang".
- [ ] `docs/research-question.md` §Gap memuat tabel Gap | Evidence | Claim; setiap baris Evidence menyebut nomor baris matriks dan sumber; Issue `type:literature-gap` ditutup dengan tautan ke gap final.
- [ ] §RQ berisi 1 RQ utama + maks 2 pendukung; tiap RQ menunjuk gap **dan** baris matriks; hipotesis (bila ada) menyebut arah, variabel, pembanding, kriteria penolakan.
- [ ] Untuk **setiap** RQ tertulis hasil yang akan membatalkannya, dan §RQ Check terisi (data, metrik kandidat, hasil pembatal, waktu); RQ yang direvisi tercatat di commit.
- [ ] §Contribution menyebut jenis kontribusi dan alasan bermakna; tidak ada frasa "pertama"/"novel" tanpa bukti; tidak melebihi RQ.
- [ ] `docs/one-pager.md` v1 ter-tag `one-pager-v1`; field 9–12 terisi dari matriks dan `research-question.md`; field 13–16 bertanda `tentatif — menunggu G5`; tidak ada field kosong.
- [ ] Issue `type:research-question` terbuka dengan Research ID, tertaut ke Issue problem dan literature-gap; nomornya tercatat di README riset dan One-Pager.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Gap`/`RQ` untuk setiap penggunaan material; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] Di gate check, tim membacakan satu RQ dan hasil pembatalnya, lalu menunjukkan baris matriksnya tanpa membuka catatan lain.
- [ ] PR **`GATE REVIEW: Question Ready`** termerge oleh dosen pengampu + mentor; label `gate:G4-question`; README §Current Research Gate diperbarui.

**Ringkasan gate G4** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G4). **Lulus jika** setiap RQ dapat ditelusuri ke baris tertentu di synthesis matrix. **Gagal jika** gap hanya naratif ("belum ada yang meneliti di UAI") — atau bila ada pelanggaran integritas (RQ diubah diam-diam dari gap, sumber pendukung tidak terverifikasi, penggunaan AI tidak diungkap), terlepas dari kualitas lainnya. Reviewer: dosen pengampu + mentor. Gagal gate bukan hukuman: reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan, tim merevisi, review dibuka ulang; PR yang ditolak di G4 menghabiskan satu minggu, RQ yang salah dan baru ketahuan di G7 menghabiskan sepuluh minggu ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Pelajaran).

**Cara membuka PR gate** ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3): (1) pastikan semua bukti di tabel Deliverable ada di branch `research/g4-question`; (2) buka PR berjudul `GATE REVIEW: Question Ready — UIAI-YYYY-NNN` memakai [template default](../../.github/PULL_REQUEST_TEMPLATE.md) (G4 tidak punya template khusus); (3) isi bagian *Research Question* dengan RQ/hipotesis final, bagian *Method/Dataset/Baseline/Metrics/Threats* dengan draft tentatif yang ditandai "menunggu G5", tabel *Evidence* dengan path `docs/research-question.md`, `docs/one-pager.md` (tag `one-pager-v1`), dan nomor Issue RQ, serta bagian *AI Usage* dengan tautan log; (4) tautkan nomor PR G3 dan Issue `type:problem`, `type:literature-gap`, `type:research-question`; (5) minta review dosen pengampu + mentor, dan minta mentor menuliskan untuk tiap RQ "baris mana di matriks yang membuatnya perlu"; (6) setelah merge: label → `gate:G4-question`, field Mission Control dan README diperbarui; tidak ada release untuk G4. Komentar review disimpan, tidak dihapus. Bila PR G3 belum termerge pada Senin, tulis RQ sebagai draft bersyarat dan **jangan** buka PR G4 sampai G3 lulus ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat).

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-01 Research One-Pager Template](../../research-os/08-templates/01-research-one-pager-template.md) — `docs/one-pager.md` v1 (field 9 What we know, 10 Gap, 11 RQ/hipotesis, 12 Contribution wajib; 13–16 draft; 19 Next evidence; 20 Gate).
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — `docs/AI-USAGE.md` (Stage `Gap`/`RQ`).
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `docs/research-question.md`, `docs/journal/`, branch `research/g4-question`.
- [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) — format hipotesis (arah, variabel, Δ, kriteria penolakan) yang akan dipakai ulang di W8; menulisnya sekarang membuat pilot nanti punya *expected result*.
- [TPL-04 Research Backlog Template](../../research-os/08-templates/04-research-backlog-template.md) — gap cadangan yang tidak dipakai diparkir sebagai kartu masalah backlog, bukan dibuang.
- Form Issue [Research Question](../../.github/ISSUE_TEMPLATE/02-research-question.yml) dan [template PR default](../../.github/PULL_REQUEST_TEMPLATE.md) untuk `GATE REVIEW: Question Ready`.

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W6 · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.4 Research Gap, §3.5 RQ/Hypothesis, §3.6 Contribution Statement · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.1 E1 End · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §6 pertanyaan integritas G4 · [ARC-06 Research Output Taxonomy](../../research-os/02-academic-architecture/06-research-output-taxonomy.md) §2 jenis output.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §6 Hypothesis (latihan *Tiga Hipotesis*), §7 Falsification · [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.5 Gap, §3.6 RQ · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3 izin/larangan.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S6 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G4 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rule B3–B4, §S6 · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Contoh terisi Week 06 · [MST-03 Glossary](../../research-os/00-master/03-glossary.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **RQ lahir sebelum matriks, atau RQ = keinginan.** Tim sudah "tahu" RQ-nya sejak W1 dan matriks dipakai untuk membenarkannya; saat reviewer menanyakan baris matriks, jawabannya "secara umum literatur belum..." — gap naratif, G4 gagal. Cara menghindari: mulai OPS-051 dari matriks (baris mana konsisten/bertentangan/belum diuji), baru turunkan klaim; bila tidak ada baris yang membuat RQ perlu, itu bukan gap; bandingkan RQ akhir dengan klaim awal W1 di jurnal dan tulis apa yang berubah.
2. **RQ yang tidak bisa salah.** "Bagaimana penerapan M untuk X?" atau "Apakah M dapat digunakan untuk Y?" selalu terjawab "ya"; tidak ada eksperimen yang bisa membantahnya, sehingga W7–W12 menghasilkan angka tanpa makna. Cara menghindari: pakai anatomi konstruk–konteks–pembanding–batas; tulis hasil pembatal di §RQ Check sebelum Jumat; minta AI mencari cara hipotesis gagal, bukan alasan hipotesis benar.
3. **Terlalu banyak RQ atau gap terlalu besar untuk satu TA.** Empat RQ, tiga dataset, dua domain — tidak satu pun terjawab dalam semester + TA. Cara menghindari: satu RQ utama, maksimal dua pendukung; uji tiap RQ terhadap data yang benar-benar ada di `common-metrics-baselines.md` dan waktu yang tersisa; RQ sisanya diparkir ke backlog.
4. **Kontribusi melebihi RQ.** "Novel framework", "pertama di Indonesia", atau "menerapkan M di konteks baru" tanpa alasan mengapa konteks mengubah hasil. Cara menghindari: pilih satu jenis kontribusi dari enam, tulis "bermakna karena ___" untuk stakeholder yang disebut di W2, dan biarkan anggota yang tidak menulisnya membaca ulang dengan pertanyaan "bukti apa yang mungkin kita hasilkan untuk klaim ini?"
5. **Mendahului G5 dan RQ berubah diam-diam.** One-Pager v1 mengunci metode, data, dan baseline sebelum desain dipikirkan, lalu RQ disesuaikan ke metode favorit — solution-first kembali lewat pintu belakang; atau RQ direvisi tanpa jejak setelah data dilihat (HARKing). Cara menghindari: field 13–16 bertanda tentatif; metode dipilih di W7 karena mampu menjawab RQ (blocking rule B4); setiap perubahan RQ setelah W6 dicatat dengan alasan dan tanggal di `research-question.md` dan commit.
