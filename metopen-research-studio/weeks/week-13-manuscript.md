# Week 13 — Manuscript

> **Sprint** S13 · **Gate** G8 Contribution Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-12-contribution.md) / [Week berikutnya →](week-14-peer-review.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Proposal TA kami tersusun dari artefak yang sudah ada, bukan dari nol."** Proposal TA (atau manuscript bila endgame-nya paper) ditulis dengan memetakan komponen Research Pack ke bagian dokumen: Pendahuluan dan Tinjauan Pustaka dari Problem Brief dan Literature Evidence Map, Metode dari Research Design Card dan Data Plan, Hasil dan Pembahasan dari `results/analysis.md` dan tabel CER, Rencana TA untuk semester VIII. AI Usage Statement ditulis dari AI Usage Log, indeks Research Pack dirakit, dan semuanya dirilis sebagai **v0.8 Manuscript Draft** ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W13; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S13). G8 *dimulai* minggu ini dan ditutup di Week 16.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (scientific argumentation & writing, struktur IMRaD untuk computing dan pemetaannya ke proposal TA, citation integrity, batas AI dalam penulisan), **60 menit studio** (membuat outline dari artefak, lalu menulis Pendahuluan; tim yang cepat lanjut ke Metode), **10 menit gate check** (tiap tim menunjukkan outline-nya dan menyebut komponen Research Pack mana yang belum punya "rumah" di proposal). Sprint ini padat jam (19.5 jam) karena empat bagian tulisan (OPS-114–117) hanya bisa dimulai setelah outline (OPS-113) — bagi bagian antar anggota, tetapi satu orang tetap membaca seluruh draft untuk konsistensi.

## Concept (30 menit)

- **Menulis dari artefak, bukan dari nol.** Setiap bagian proposal punya sumber di repositori: tidak ada kalimat hasil yang tidak berasal dari `results/analysis.md`.
- **IMRaD untuk computing** dan pemetaannya ke proposal TA: Pendahuluan (problem, why, gap, RQ, kontribusi), Tinjauan Pustaka (evidence map, bukan ringkasan satu per satu), Metode (desain, data, baseline, metrik, prosedur, threats v1), Hasil pilot/utama (tabel, figur, CER), Pembahasan (batas klaim, threats v2, limitations), Rencana TA ([MET-05](../../research-os/04-metopen-research-studio/05-publication-backward-design.md)).
- **Citation integrity.** Semua sitasi ada di `references.bib` yang terverifikasi (DOI/URL) dan benar-benar dibaca; sitasi yang tidak dapat diverifikasi dihapus.
- **Backward design dari venue.** Bila endgame paper, format dan panjang mengikuti venue target di registry; bila TA, mengikuti format proposal Prodi.
- **AI dalam penulisan.** Penyuntingan bahasa dan struktur diperbolehkan dan diungkap; hasil, klaim, dan sitasi tidak boleh berasal dari AI (kebijakan ACM sebagaimana dirangkum di [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md); verifikasi teks terkini).
- **Reproducibility README** adalah bagian dari naskah: pembaca harus bisa menjalankan ulang angka di tabel dari repositori.
- **Release v0.8** menandai draft lengkap yang siap direview peer di Week 14.

**Pertanyaan pemandu:** *Bagian mana dari proposal Anda yang tidak bisa Anda telusuri ke satu file di repositori?*

## Tasks

Semua task Sprint S13 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Draft method section from design card (UIAI-2026-001, OPS-115)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-113 | Ikuti sesi Scientific Writing dan struktur proposal/manuscript | Outline proposal/manuscript | 2h | Membantu menyusun outline dari artefak yang ada | Dosen memeriksa outline mencakup semua komponen Research Pack |
| OPS-114 | Tulis Pendahuluan dan Tinjauan Pustaka dari artefak G2-G3 | Bagian 1-2 proposal | 4h | Membantu memperbaiki alur kalimat; tidak menghasilkan sitasi; setiap bantuan dicatat | Tim memeriksa tiap sitasi dibaca dan terverifikasi |
| OPS-115 | Tulis Metode dari Research Design Card dan Data Plan | Bagian Metode | 3h | Membantu merapikan; isi dari dokumen tim | Mentor memeriksa metode cukup rinci untuk direplikasi |
| OPS-116 | Tulis Hasil dan Pembahasan dari analysis.md dan tabel CER | Bagian Hasil & Pembahasan | 4h | Membantu alur kalimat; angka dan klaim dari CER table | Dosen memeriksa tidak ada klaim baru yang tidak ada di CER table |
| OPS-117 | Tulis Rencana TA (timeline semester VIII) dan target output | Bagian Rencana TA | 2h | Membantu menyusun timeline; keputusan oleh tim | Mentor memeriksa rencana realistis untuk 1 semester |
| OPS-118 | Tulis AI Usage Statement dari AI Usage Log | AI Usage Statement | 1.5h | - | Dosen membandingkan statement dengan log secara acak |
| OPS-119 | Rakit draft Research Pack v0.8 dan periksa kelengkapan MET-04 | docs/research-pack.md (indeks) | 1.5h | - | Dosen memeriksa indeks terhadap MET-04 |
| OPS-120 | Buat release v0.8 Manuscript Draft | Release v0.8 | 1h | - | Tim memeriksa PDF identik dengan sumber markdown |
| OPS-121 | Perbarui AI Usage Log dan jurnal mingguan W13 | AI Usage Log W13 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 19.5h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: OPS-113 (outline) dahulu; OPS-114, OPS-115, OPS-116, dan OPS-117 dapat ditulis paralel oleh anggota berbeda; OPS-118 (AI Usage Statement) kapan saja setelah log W12; OPS-119 (indeks Research Pack) menunggu semua bagian; OPS-120 (release v0.8) paling akhir ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

## Deliverable

| Artefak | Lokasi di repositori riset | Bukti |
|---|---|---|
| Outline proposal/manuscript | `paper/outline.md` | commit; setiap bagian menunjuk artefak sumber |
| Draft proposal/manuscript v0.8 | `paper/proposal.md` + `paper/proposal-v0.8.pdf` | commit; PDF identik dengan sumber markdown |
| AI Usage Statement (untuk naskah) | `paper/AI-USAGE-STATEMENT.md` (ringkasan dari `docs/AI-USAGE.md`) | commit |
| Indeks Research Pack | `docs/research-pack.md` (16 komponen [MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) → lokasi file) | commit; tidak ada komponen kosong tanpa rencana |
| Release | `v0.8 Manuscript Draft` | halaman release di GitHub |
| AI Usage Log + jurnal | `docs/AI-USAGE.md`, `docs/journal/w13.md` | commit |

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Membantu menyusun outline dari artefak yang ada (OPS-113).
- Memperbaiki alur kalimat dan tata bahasa Pendahuluan/Tinjauan Pustaka; tidak menghasilkan sitasi; setiap bantuan dicatat (OPS-114).
- Merapikan bagian Metode; isinya dari dokumen tim (OPS-115).
- Membantu alur kalimat Hasil & Pembahasan; angka dan klaim dari tabel CER (OPS-116).
- Membantu menyusun timeline Rencana TA; keputusan oleh tim (OPS-117).
- Memeriksa konsistensi istilah antar bagian.

Tidak boleh:

- Menulis bagian Hasil atau Pembahasan dari AI; menambah klaim yang tidak ada di tabel CER.
- Menambah sitasi yang tidak ada di `references.bib` terverifikasi — referensi buatan AI adalah pelanggaran integritas ([TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md)).
- Membuat AI Usage Statement dengan AI tanpa membandingkannya dengan log.
- Memasukkan data pribadi atau data partner ke layanan AI saat menyunting ([SECURITY](../../SECURITY.md)).

## Human Check

- **Dosen**: outline mencakup semua komponen Research Pack (OPS-113); tidak ada klaim baru di luar tabel CER (OPS-116); statement dibandingkan dengan log secara acak (OPS-118); indeks diperiksa terhadap MET-04 (OPS-119); satu bagian dibaca dan setiap sitasinya dicek ada di `references.bib`.
- **Mentor**: metode cukup rinci untuk direplikasi (OPS-115); rencana TA realistis untuk satu semester (OPS-117).
- **Tim**: tiap sitasi dibaca dan terverifikasi (OPS-114); PDF identik dengan sumber markdown (OPS-120).
- **Setiap anggota**: entri AI Usage Log miliknya sendiri (OPS-121).

## Done When

Minggu ini belum menutup gate; G8 Contribution Ready ditutup di [Week 16](week-16-defense.md). Sprint selesai bila:

- [ ] `paper/outline.md` memetakan setiap bagian ke artefak sumber di repositori.
- [ ] Draft v0.8 lengkap: Pendahuluan, Tinjauan Pustaka, Metode, Hasil & Pembahasan, Rencana TA — tanpa sitasi di luar `references.bib` dan tanpa klaim di luar tabel CER.
- [ ] `paper/AI-USAGE-STATEMENT.md` konsisten dengan `docs/AI-USAGE.md`.
- [ ] `docs/research-pack.md` mengindeks 16 komponen; komponen yang belum ada punya rencana penyelesaian (Week 15).
- [ ] Release `v0.8 Manuscript Draft` dibuat; PDF identik dengan sumber markdown.
- [ ] AI Usage Log dan `docs/journal/w13.md` diperbarui oleh setiap anggota.

## Templates & rujukan

- Template: [TPL-10 AI Usage Log & Statement](../../research-os/08-templates/10-ai-usage-log-template.md), [TPL-06 Publication Venue Registry](../../research-os/08-templates/06-publication-venue-registry-template.md), [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) (mulai dibaca), [TPL-15 Research Repository](../../research-os/08-templates/15-research-repository-template.md).
- Konsep: [MET-03 §W13](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md), [MET-05 Publication Backward Design](../../research-os/04-metopen-research-studio/05-publication-backward-design.md), [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md), [AIX-03 AI Across Value Stream — Writing](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md), [OPS-02 §S13](../../research-os/06-execution-os/02-weekly-sprints.md), [OPS-03 G8](../../research-os/06-execution-os/03-research-gates.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).

## Jebakan minggu ini

1. **Menulis sebelum klaim siap.** Menulis Pembahasan sebelum PR G7 merge menghasilkan naskah yang harus dibongkar. Tunggu tabel CER final.
2. **Sitasi yang tidak ada di `references.bib`.** Menambah referensi "dari ingatan" atau dari AI. Setiap sitasi harus terverifikasi dan sudah dibaca.
3. **AI menulis hasil.** Kalimat hasil/pembahasan dari AI hampir selalu menambah klaim halus yang tidak ada di data. Tulis sendiri, minta AI hanya merapikan.
4. **Tinjauan pustaka sebagai daftar ringkasan.** Gunakan pola dari synthesis matrix (konsisten, bertentangan, belum diuji), bukan satu paragraf per paper.
5. **Rencana TA yang tidak realistis.** Satu semester bimbingan; tulis milestone per bulan dan gate yang akan dilewati, bukan daftar keinginan.
