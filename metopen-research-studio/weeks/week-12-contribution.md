# Week 12 — Contribution

> **Sprint** S12 · **Gate** G7 Claim Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-11-analysis.md) / [Week berikutnya →](week-13-manuscript.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Bukti mendukung klaim ___ dan tidak mendukung ___."** Setiap RQ dijawab dengan struktur **Claim–Evidence–Reasoning (CER)** yang menunjuk tabel/figur tertentu; Threats to Validity diperbarui ke **v2** berdasarkan apa yang benar-benar terjadi; Contribution Statement direvisi agar tidak melebihi bukti; Limitations & Future Work ditulis jujur; Research One-Pager naik ke v2 (hasil dan klaim) ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W12; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S12). Semua bukti masuk PR `GATE REVIEW: Claim Ready`; merge berarti **G7 lulus** dan riset berstatus **Research Ready**.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (CER, batas klaim kausal vs korelasional, generalisasi ke populasi mana, hasil negatif sebagai hasil, "so what?" bagi stakeholder), **60 menit studio** (menyusun tabel CER per RQ, lalu meminta peer menantang tiap klaim; tim yang cepat lanjut ke Threats v2), **10 menit gate check** (tiap tim membacakan satu klaim dan menyebut tabel/figur yang mendukungnya; klaim tanpa rujukan dicoret di tempat). Sprint ini ringan secara jam (12 jam) tetapi padat keputusan — kualitas review PR G7 lebih penting daripada kecepatan.

## Concept (30 menit)

- **Claim–Evidence–Reasoning.** Klaim (apa yang kami nyatakan), bukti (tabel/figur mana, angka berapa), penalaran (mengapa bukti itu cukup untuk klaim itu — dan apa yang tidak dicakupnya).
- **Batas klaim.** Kausal hanya jika desain memungkinkannya (kontrol, randomisasi, atau argumen identifikasi); selain itu tulis "berasosiasi dengan", bukan "menyebabkan".
- **Generalisasi.** Ke populasi/dataset/kondisi mana hasil berlaku? Sampel Anda merepresentasikan apa? Ini sumber utama threats validitas eksternal.
- **Hasil negatif adalah hasil.** "Metode X tidak lebih baik dari baseline pada kondisi Y" adalah klaim sah dan berguna.
- **Contribution Statement yang jujur.** Jenis kontribusi (empiris, artefak, metode, dataset, replikasi, studi kasus) dan besarnya — tidak lebih dari yang dibuktikan.
- **Threats to Validity v2.** Versi v1 ditulis sebelum eksperimen (G5); v2 ditulis setelah hasil: ancaman mana yang terbukti, mana yang baru muncul, mitigasi mana yang gagal, dan dampaknya pada tiap klaim.
- **"So what?"** Keputusan apa yang berubah bagi stakeholder bila klaim ini benar? Jika tidak ada, kontribusinya perlu dirumuskan ulang.

**Pertanyaan pemandu:** *Klaim mana di analisis Anda yang akan Anda pertahankan di depan reviewer paling skeptis — dan mana yang harus Anda lepaskan?*

## Tasks

Semua task Sprint S12 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add CER table for RQ1-RQ2 (UIAI-2026-001, OPS-106)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-105 | Ikuti sesi Scientific Argumentation (Claim-Evidence-Reasoning) | Latihan CER | 2h | Memberi contoh klaim untuk dinilai | Mahasiswa menilai klaim secara mandiri |
| OPS-106 | Susun tabel Claim-Evidence-Reasoning untuk setiap RQ | results/analysis.md bagian CER Table | 2.5h | Berperan sebagai reviewer yang menantang setiap klaim | Dosen + mentor memeriksa tidak ada klaim kausal dari korelasi |
| OPS-107 | Perbarui Threats to Validity berdasarkan hasil aktual | Threats to Validity v2 | 2h | Mengusulkan ancaman yang terlewat | Tim memastikan tiap ancaman dikaitkan dengan klaim yang terdampak |
| OPS-108 | Revisi Contribution Statement agar tidak melebihi bukti | Contribution Statement v2 | 1h | Mengkritik kontribusi yang berlebihan | Mentor memeriksa kontribusi tidak melebihi bukti |
| OPS-109 | Tulis bagian Limitations dan Future Work | results/analysis.md bagian Limitations & Future Work | 1.5h | Membantu merapikan; isi dari tim | Tim memastikan keterbatasan tidak disembunyikan |
| OPS-110 | Perbarui Research One-Pager ke v2 (hasil dan klaim) | docs/one-pager.md v2 | 1h | Meringkas; tim memverifikasi angka | Tim memeriksa setiap angka di One-Pager cocok dengan summary.csv |
| OPS-111 | Siapkan PR GATE REVIEW: Claim Ready | PR GATE REVIEW: Claim Ready | 1.5h | - | Reviewer memeriksa setiap klaim menunjuk tabel/figur tertentu |
| OPS-112 | Perbarui AI Usage Log dan jurnal mingguan W12 | AI Usage Log W12 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 12h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: OPS-105 (sesi) → OPS-106 (tabel CER) adalah pintu semua task lain; OPS-107 (Threats v2) dan OPS-108 (Contribution v2) menyusul, lalu OPS-109 dan OPS-110; OPS-111 (PR G7) hanya dibuka setelah OPS-100, OPS-104, OPS-106–108, dan OPS-110 selesai ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules).

## Deliverable

| Artefak | Lokasi di repositori riset | Bukti |
|---|---|---|
| Tabel Claim–Evidence–Reasoning per RQ | `results/analysis.md` §CER Table | commit; setiap baris menunjuk tabel/figur |
| Threats to Validity v2 | `results/analysis.md` §Threats (v2), dengan kolom perubahan dari v1 di `docs/research-design.md` | commit |
| Contribution Statement v2 | `docs/research-question.md` §Contribution (revisi) | commit |
| Limitations & Future Work | `results/analysis.md` §Limitations & Future Work | commit; tiap future work terkait keterbatasan tertentu |
| Research One-Pager v2 | `docs/one-pager.md` (tag `one-pager-v2`) | commit + tag |
| PR Gate Review G7 | PR `GATE REVIEW: Claim Ready` dari branch `research/g7-claim` | URL PR; label `gate:G7-claim` setelah merge |
| AI Usage Log + jurnal | `docs/AI-USAGE.md`, `docs/journal/w12.md` | commit |

Komponen Research Pack yang tuntas minggu ini: Contribution Statement, Threats to Validity (v2), bagian hasil Pilot/Main Experiment ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md)).

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Memberi contoh klaim untuk dinilai sebagai latihan CER (OPS-105).
- Berperan sebagai reviewer yang menantang setiap klaim: "bukti mana yang mendukung ini?" (OPS-106).
- Mengusulkan ancaman validitas yang mungkin terlewat (OPS-107).
- Mengkritik Contribution Statement yang berlebihan (OPS-108).
- Membantu merapikan bahasa Limitations & Future Work dan One-Pager v2; isi dan angka dari tim (OPS-109, OPS-110).

Tidak boleh:

- Memakai kalimat klaim buatan AI yang tidak didukung tabel/figur tim.
- Membiarkan AI "menyimpulkan" hasil; penalaran di kolom Reasoning harus milik tim.
- Menghapus atau melembutkan keterbatasan atas saran AI agar "terlihat lebih kuat".
- Menyerahkan PR G7 tanpa mencatat bantuan AI yang memengaruhi klaim di AI Usage Log.

## Human Check

- **Tim**: tiap ancaman v2 dikaitkan dengan klaim yang terdampak (OPS-107); keterbatasan tidak disembunyikan (OPS-109); setiap angka di One-Pager cocok dengan `results/main/summary.csv` (OPS-110).
- **Mentor**: kontribusi tidak melebihi bukti (OPS-108).
- **Dosen + mentor**: tidak ada klaim kausal dari korelasi; tidak ada *improvement* tanpa baseline (OPS-106).
- **Reviewer PR**: setiap klaim menunjuk tabel/figur tertentu (OPS-111).
- **Setiap anggota**: entri AI Usage Log miliknya sendiri (OPS-112).

## Done When

Minggu ini **menutup G7 Claim Ready** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G7).

- [ ] Tabel CER lengkap untuk setiap RQ; setiap klaim menunjuk tabel/figur tertentu.
- [ ] Threats to Validity v2 ditulis berdasarkan hasil aktual, dengan kolom perubahan dari v1.
- [ ] Contribution Statement v2 dan Limitations & Future Work tidak melebihi bukti; hasil negatif dilaporkan.
- [ ] Research One-Pager v2 memuat hasil dan klaim; tag `one-pager-v2` dibuat.
- [ ] PR `GATE REVIEW: Claim Ready` dibuka dari `research/g7-claim` memakai [template default](../../.github/PULL_REQUEST_TEMPLATE.md), direview dosen + mentor, dan **di-merge**; label Issue diperbarui ke `gate:G7-claim`; Mission Control diperbarui (Maturity: Research Ready).
- [ ] AI Usage Log dan `docs/journal/w12.md` diperbarui oleh setiap anggota.

**Lulus jika** setiap klaim menunjuk ke tabel/figur tertentu. **Gagal jika** ada klaim kausal dari korelasi atau *improvement* tanpa baseline. Gagal bukan hukuman: reviewer menuliskan bukti apa yang kurang, tim merevisi dan membuka review ulang ([CONTRIBUTING](../../CONTRIBUTING.md) §3).

## Templates & rujukan

- Template: [TPL-01 Research One-Pager](../../research-os/08-templates/01-research-one-pager-template.md) (v2), [TPL-08 Research Design Card](../../research-os/08-templates/08-research-design-card.md) (bagian threats), [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md), [PR template default](../../.github/PULL_REQUEST_TEMPLATE.md).
- Konsep: [MET-03 §W12](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md), [MET-06 Rubrik 5E — Explanation](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md), [AIX-01 Meta-Thinking — falsification](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md), [OPS-02 §S12](../../research-os/06-execution-os/02-weekly-sprints.md), [OPS-03 G7](../../research-os/06-execution-os/03-research-gates.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).

## Jebakan minggu ini

1. **Kontribusi melebihi bukti.** "Kami membuktikan metode X unggul" dari satu dataset dan tiga seed. Batasi klaim pada kondisi yang diuji.
2. **Threats tidak diperbarui.** Menyalin threats v1 apa adanya. v2 harus menyebut ancaman yang terbukti terjadi dan yang baru muncul dari data.
3. **Menyembunyikan hasil negatif.** RQ yang jawabannya "tidak" tetap masuk tabel CER dengan bukti yang sama kuatnya.
4. **Reasoning yang hanya mengulang klaim.** Kolom Reasoning harus menjelaskan *mengapa* bukti itu cukup dan apa yang tidak dicakupnya — bukan parafrase klaim.
5. **Membuka PR G7 sebelum figur dan arsip siap.** Reviewer tidak bisa memeriksa klaim tanpa OPS-100 (figur) dan OPS-104 (arsip run) selesai.
