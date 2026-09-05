# Week 14 — Peer Review

> **Sprint** S14 · **Gate** G8 Contribution Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-13-manuscript.md) / [Week berikutnya →](week-15-revision.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Kami sudah mereview riset orang lain dengan bukti, dan menerima review atas riset kami tanpa membela diri."** Setiap mahasiswa menjadi reviewer untuk draft tim lain memakai [TPL-12](../../research-os/08-templates/12-peer-review-template.md), menerima review untuk timnya sendiri, dan mengubah semua komentar menjadi tabel tanggapan (*response to reviewers*). Di sela itu tim memverifikasi ulang seluruh sitasi dan angka di draft, menguji reproducibility README dari environment bersih, menyusun draft slide defense, dan **membuka** PR `GATE REVIEW: Contribution Ready` sebagai draft agar dosen mulai mereview ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W14; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S14). G8 belum ditutup — merge terjadi di Week 16.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (bagaimana peer review bekerja di computing, etika reviewer, struktur TPL-12, cara membaca review sebagai data bukan serangan), **60 menit studio** (latihan kalibrasi: semua menilai satu draft yang sama lalu membandingkan skor; kemudian mulai menulis review untuk tim yang ditugaskan), **10 menit gate check** (tiap reviewer menyebut satu komentar paling penting yang akan ia tulis dan bukti yang mendasarinya). Review dilakukan *double-blind* bila memungkinkan; draft tim lain **tidak boleh** dimasukkan ke layanan AI tanpa izin.

## Concept (30 menit)

- **Peer review adalah bagian dari sains**, bukan formalitas: riset direvisi berdasarkan review, tidak lahir sekali jadi.
- **Etika reviewer.** Kerahasiaan draft; kritik pada gagasan dan bukti, bukan orang; komentar spesifik dan dapat ditindaklanjuti; setiap penilaian menyebut bukti (halaman/tabel/figur).
- **Struktur TPL-12.** Problem, evidence, RQ, method, results, claim, limitations — tiap aspek diberi skor dan komentar "apa yang kurang dan bukti apa yang dibutuhkan", ditutup rekomendasi (accept / minor / major / reject).
- **Kalibrasi.** Dua reviewer yang membaca draft yang sama seharusnya sampai pada skor yang mirip; perbedaan besar dibahas di studio agar standar kelas sama.
- **Menerima review.** Klasifikasikan komentar mayor/minor; keputusan terima/ubah/tolak selalu dengan alasan — menolak komentar boleh, mengabaikannya tidak.
- **Verifikasi ulang draft.** Angka di naskah dicocokkan ke `results/main/summary.csv`, sitasi ke `references.bib`; dua anggota memeriksa silang.
- **Reproduksi dari environment bersih.** Anggota yang tidak menulis kode menjalankan README; jika gagal, README-nya yang salah.

**Pertanyaan pemandu:** *Komentar apa yang paling tidak ingin Anda terima tentang draft Anda — dan mengapa Anda belum memperbaikinya sendiri?*

## Tasks

Semua task Sprint S14 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add response-to-reviewers table (UIAI-2026-001, OPS-124)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-122 | Ikuti sesi Peer Review: mahasiswa menjadi reviewer | Latihan kalibrasi review | 2h | Menjelaskan kriteria rubrik dengan contoh | Dosen memeriksa kalibrasi skor |
| OPS-123 | Tulis peer review untuk draft tim lain (memberi) | Peer review terkirim | 3h | Membantu memeriksa konsistensi angka dalam draft; penilaian oleh manusia | Dosen memeriksa review spesifik dan sopan |
| OPS-124 | Terima peer review dan buat tabel tanggapan (response to reviewers) | paper/response-to-reviewers.md | 1.5h | Membantu mengelompokkan komentar | Tim memutuskan sendiri terima/tolak dengan alasan |
| OPS-125 | Verifikasi ulang seluruh sitasi dan angka di draft | Checklist verifikasi draft | 2h | Membantu mencocokkan angka secara otomatis; hasil diperiksa manusia | Dua anggota memeriksa silang |
| OPS-126 | Perbaiki reproducibility README final dan uji dari environment bersih | experiments/README.md final | 2h | Membantu memperjelas instruksi | Anggota yang tidak menulis kode menjalankan uji |
| OPS-127 | Siapkan draft slide Research Defense (TPL-13) | presentation/defense-draft.pdf | 3h | Membantu merapikan alur slide; angka dari artefak tim | Tim memastikan tiap slide bersumber dari repo |
| OPS-128 | Buka PR GATE REVIEW: Contribution Ready (manuscript-review.md) draft | PR GATE REVIEW: Contribution Ready (open) | 1h | - | Dosen mulai review terhadap definition of done G8 |
| OPS-129 | Perbarui AI Usage Log dan jurnal mingguan W14 | AI Usage Log W14 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 15h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: OPS-122 (kalibrasi) → OPS-123 (menulis review) pada paruh pertama minggu agar tim lain menerima review tepat waktu; OPS-124 (tabel tanggapan) dan OPS-125 (verifikasi angka/sitasi) begitu review masuk; OPS-126 (reproduksi bersih) dan OPS-127 (slide draft) dapat paralel; OPS-128 (PR G8 draft) paling akhir setelah OPS-124 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

## Deliverable

| Artefak | Lokasi | Bukti |
|---|---|---|
| Peer review untuk tim lain (memberi) | Formulir [TPL-12](../../research-os/08-templates/12-peer-review-template.md) di PR tim lain atau kanal review kelas | review terkirim; minimal 5 komentar spesifik |
| Tabel tanggapan (response to reviewers) | `paper/response-to-reviewers.md` | commit; setiap komentar terklasifikasi mayor/minor dengan keputusan terima/ubah/tolak |
| Checklist verifikasi angka & sitasi | `paper/verification-checklist.md` | commit; diperiksa silang dua anggota |
| Reproducibility README final | `experiments/README.md` | commit; catatan uji dari environment bersih di `docs/reviews/` |
| Draft slide defense | `presentation/defense-draft.pdf` | commit |
| PR Gate Review G8 (draft) | PR `GATE REVIEW: Contribution Ready` dari branch `research/g8-contribution`, template [manuscript-review.md](../../.github/PULL_REQUEST_TEMPLATE/manuscript-review.md) | URL PR (status draft) |
| AI Usage Log + jurnal | `docs/AI-USAGE.md`, `docs/journal/w14.md` | commit |

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Menjelaskan kriteria rubrik review dengan contoh saat kalibrasi (OPS-122).
- Membantu memeriksa konsistensi angka dalam draft *tim sendiri*; penilaian tetap oleh manusia (OPS-123, OPS-125).
- Membantu mengelompokkan komentar reviewer yang diterima (OPS-124).
- Memperjelas instruksi reproducibility README (OPS-126).
- Merapikan alur slide; angka dari artefak tim (OPS-127).
- Menjadi "reviewer tambahan" untuk draft tim sendiri, diungkap di log.

Tidak boleh:

- Membuat AI menulis review untuk tim lain — review adalah penilaian Anda, dan kualitasnya dinilai (CPMK peer review).
- Memasukkan draft tim lain ke layanan AI tanpa izin tertulis penulisnya (kerahasiaan reviewer).
- Menyerahkan tabel tanggapan yang keputusannya dibuat AI; terima/ubah/tolak diputuskan tim dengan alasan.
- Mengubah angka hasil di draft "agar cocok" tanpa menjalankan ulang eksperimen.

## Human Check

- **Dosen**: kalibrasi skor antar reviewer (OPS-122); review spesifik dan sopan (OPS-123); mulai review PR G8 terhadap definition of done ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G8) (OPS-128).
- **Tim**: keputusan terima/tolak komentar dibuat sendiri dengan alasan (OPS-124); dua anggota memeriksa silang angka dan sitasi (OPS-125); tiap slide bersumber dari repositori (OPS-127).
- **Anggota yang tidak menulis kode**: menjalankan uji reproduksi dari environment bersih (OPS-126).
- **Setiap anggota**: entri AI Usage Log miliknya sendiri (OPS-129).

## Done When

Minggu ini belum menutup gate; G8 Contribution Ready ditutup di [Week 16](week-16-defense.md). Sprint selesai bila:

- [ ] Review untuk tim lain terkirim dengan TPL-12: minimal 5 komentar spesifik, masing-masing menyebut bukti, ditutup rekomendasi.
- [ ] Semua komentar yang diterima masuk `paper/response-to-reviewers.md`, terklasifikasi mayor/minor, dengan keputusan dan alasan.
- [ ] `paper/verification-checklist.md`: setiap angka cocok dengan `results/main/summary.csv`, setiap sitasi ada di `references.bib`.
- [ ] Reproduksi final dari environment bersih berhasil oleh anggota yang tidak menulis kode; `experiments/README.md` final.
- [ ] `presentation/defense-draft.pdf` ada; tiap slide bersumber dari artefak repositori.
- [ ] PR `GATE REVIEW: Contribution Ready` dibuka sebagai draft dari `research/g8-contribution` dengan template manuscript-review.
- [ ] AI Usage Log dan `docs/journal/w14.md` diperbarui oleh setiap anggota.

## Templates & rujukan

- Template: [TPL-12 Peer Review](../../research-os/08-templates/12-peer-review-template.md), [TPL-13 Research Defense](../../research-os/08-templates/13-research-defense-template.md), [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md), [PR manuscript-review](../../.github/PULL_REQUEST_TEMPLATE/manuscript-review.md).
- Konsep: [MET-03 §W14](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-05 Publication Backward Design](../../research-os/04-metopen-research-studio/05-publication-backward-design.md), [MET-06 Rubrik 5E](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) (komponen peer review), [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md), [AIX-03 AI Across Value Stream — Review](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md), [OPS-02 §S14](../../research-os/06-execution-os/02-weekly-sprints.md), [CODE OF CONDUCT](../../CODE_OF_CONDUCT.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).

## Jebakan minggu ini

1. **Review yang tidak spesifik.** "Metodenya kurang kuat" tidak bisa ditindaklanjuti. Tulis: bagian mana, apa yang kurang, bukti apa yang dibutuhkan.
2. **Defensif terhadap kritik.** Menolak semua komentar mayor tanpa alasan. Komentar boleh ditolak, tetapi dengan argumen dan bukti — dan reviewer harus dikonfirmasi.
3. **Plagiarisme saat merevisi.** Menyalin kalimat dari paper lain "agar terdengar akademik". Parafrase dengan sitasi, atau kutip dengan tanda kutip.
4. **Membocorkan draft orang lain.** Memasukkan draft tim lain ke AI atau membahasnya di luar studio melanggar kerahasiaan reviewer.
5. **Menunda review sampai akhir minggu.** Tim lain butuh waktu merevisi di Week 15; kirim review pada paruh pertama minggu.
