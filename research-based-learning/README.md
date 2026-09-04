# Research-Based Learning — Mata Kuliah → Research Pipeline

**Status** Draft v0.1 (2026-09) · Fase implementasi: **Phase 3 Curriculum Integration** (artefak riil menyusul)
**Terkait** [ARC-01 Research Capability Spiral](../research-os/02-academic-architecture/01-research-capability-spiral.md) · [ARC-02 Curriculum Research Map](../research-os/02-academic-architecture/02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](../research-os/02-academic-architecture/03-ai-contribution-modes.md) · [ARC-04 Build–Prove–Contribute](../research-os/02-academic-architecture/04-build-prove-contribute.md) · [ARC-05 CPL–CPMK–Artifact Alignment](../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md) · [MST-03 Glossary](../research-os/00-master/03-glossary.md) · [GOVERNANCE.md](../GOVERNANCE.md)

## 1. Fungsi komponen ini

`research-based-learning/` adalah **hub yang menghubungkan pendidikan ke research center**. Ia menjawab satu pertanyaan praktis yang tidak dijawab oleh `research-os/`: *mata kuliah saya harus melakukan apa, menghasilkan apa, dan menyerahkannya ke mana?*

Posisinya dalam UIRP (UAI Informatics Research Pipeline):

```
Research Center → Dosen → [ MATA KULIAH ] → Mahasiswa → Problem → Dataset → Project → Metopen → TA → Paper → Research Center lagi
                            ▲ komponen ini
```

Yang ada di sini:

| Isi | Untuk siapa | Menjawab |
|---|---|---|
| Tabel mode **F / E / R** semua mata kuliah relevan (§4) | Tim kurikulum, Kaprodi | MK mana yang mendukung, memakai, dan menghasilkan riset? |
| `courses/<mk>/` — README + `research-artifact.md` per MK (§5) | Dosen pengampu | Proyek seperti apa, rubrik apa, artefak apa, diserahkan ke mana? |
| [`faculty-guide/`](faculty-guide/README.md) — Lecturer Playbook ringkas | Dosen | Bagaimana mendesain, menilai, memberi review, dan handoff? |
| [`student-guide/`](student-guide/README.md) — "Dari nol sampai Research Pack" | Mahasiswa | Bagaimana memulai dan apa yang dinilai? |
| [`assessment/`](assessment/README.md) — asesmen lintas MK | Dosen, tim OBE/akreditasi | Rubrik apa yang dipakai semua MK dan bukti apa yang dihasilkan? |

Yang **tidak** ada di sini: framework dan definisi (itu di [`research-os/`](../research-os/README.md)), halaman mingguan Metopen (itu di [`metopen-research-studio/`](../metopen-research-studio/README.md)), dan kode/data proyek mahasiswa (itu di repo `proj-YYYY-topik` masing-masing).

## 2. Prinsip: setiap mata kuliah tidak perlu repo sendiri

Dokumen sumber tegas: **setiap mata kuliah tidak perlu punya repo sendiri, kecuali memang banyak artefak.** Lebih baik satu folder per MK di dalam komponen ini:

```
research-based-learning/courses/ai-ml/
├── README.md              ← identitas MK, mode, CPMK riset, project guide, rubrik ringkas
├── research-artifact.md   ← spesifikasi research asset yang wajib/opsional dihasilkan
├── RPS.md                 ← (ditambahkan pengampu; kerangka revisi lihat ARC-05)
├── project-guide.md       ← (opsional bila project guide di README sudah tidak cukup)
├── rubric.md              ← (opsional; rubrik lengkap bila perlu dipisah)
└── templates/             ← (opsional; salinan template yang disesuaikan untuk MK)
```

Repo terpisah (`course-<nama>` atau `proj-YYYY-topik`) dibuat **hanya** bila MK sudah *mature* atau *coding-heavy*: artefaknya bukan lagi dokumen tetapi kode, data, dan eksperimen yang terus berkembang. Kriteria pemecahan ada di [GOVERNANCE.md §2](../GOVERNANCE.md). Sampai saat itu, folder di sini adalah alamat resmi MK.

Dua prinsip desain dari [STR-03](../research-os/01-strategic-foundation/03-design-principles.md) yang paling menentukan komponen ini:

- **One activity, multiple outcomes.** Satu proyek MK menghasilkan nilai mata kuliah, research asset, kandidat entri backlog/registry, dan bahan Metopen sekaligus. Tidak ada tugas tambahan; yang ada adalah lapisan tipis berpikir riset pada aktivitas yang sudah ada.
- **Research assets should compound.** Artefak semester ini menjadi titik mulai semester berikutnya, bukan hilang bersama nilai.

## 3. Struktur folder

```
research-based-learning/
├── README.md                      ← halaman ini
├── courses/
│   ├── ai-ml/                     ← AI & Machine Learning (sem. V, 4 SKS) — pintu masuk utama
│   ├── research-methods/          ← Metodologi Penelitian (sem. VII, 2 SKS) — Prove
│   ├── data-mining/               ← Data Mining (sem. IV)
│   ├── nlp/                       ← Mata kuliah/topik pilihan bidang NLP
│   ├── software-engineering/      ← RPL (sem. IV) + rumpun Pengujian PL & Proyek PL
│   └── final-project/             ← Tugas Akhir (sem. VIII, 4 SKS) — Contribute
├── faculty-guide/README.md        ← Lecturer Playbook ringkas
├── student-guide/README.md        ← Student Research Playbook ringkas
└── assessment/README.md           ← asesmen lintas MK
```

Nama folder mengikuti nilai field **Course** pada Research Mission Control ([GOVERNANCE.md §9](../GOVERNANCE.md)): `AI/ML · Data Mining · NLP · RPL · Metopen · TA`. Dengan begitu satu riset dapat ditelusuri dari folder MK → Issue → Mission Control tanpa pemetaan tambahan.

## 4. Peta mata kuliah → research pipeline

Mode mengikuti [ARC-03](../research-os/02-academic-architecture/03-ai-contribution-modes.md): **F — Foundation** (mendukung kapabilitas AI/riset), **E — AI-Enriched** (memakai kasus/proyek AI), **R — Research-Producing** (menghasilkan reusable research asset). Mode di bawah adalah **usulan awal** berdasarkan [ARC-01](../research-os/02-academic-architecture/01-research-capability-spiral.md); mode final ditetapkan pengampu bersama tim kurikulum lewat langkah §7. Semester dan SKS berasal dari tabel kurikulum dalam dokumen diskusi *Riset AI UAI untuk Negeri*; SKS yang tidak disebut di sana ditulis `[isi]`.[^1]

| Mata kuliah | Sem. | SKS | Mode | Tahun spiral | Research asset yang dihasilkan | Folder di `courses/` |
|---|---|---|---|---|---|---|
| Statistika | I | 3 | F | Y1 Observe & Reason | Notebook analisis data kecil yang dapat dijalankan ulang; paragraf Claim–Evidence–Reasoning | — |
| Statistika Terapan | II | 3 | F | Y1 | Laporan analisis (deskriptif + 1 uji inferensial) dengan bagian "apa yang tidak boleh disimpulkan" | — |
| Matematika Diskrit | II | [isi] | F | Y1 | Catatan bukti/counterexample satu klaim (embrio falsification) | — |
| HCI | III | [isi] | E | Y2 Build & Compare | Protokol + hasil user study kecil; instrumen; catatan etika partisipan | — |
| Struktur Data | III | [isi] | F | Y2 | Benchmark harness kecil + laporan perbandingan | — |
| Basis Data | III | [isi] | F | Y2 | Skema + data dictionary + **dataset card v0** (kandidat `datasets-registry/`) | — |
| Analisis Algoritma | IV | [isi] | F | Y2 | Benchmark + laporan perbandingan dengan prosedur pengukuran berulang | — |
| Rekayasa Perangkat Lunak (RPL) | IV | [isi] | E → R | Y2 | Repositori proyek dengan README reproducibility, test suite; kandidat research-grade software | [`software-engineering/`](courses/software-engineering/README.md) |
| Data Mining | IV | [isi] | R | Y2 | Evidence map dataset, laporan eksperimen dengan baseline + pemeriksaan leakage + error analysis; dataset card | [`data-mining/`](courses/data-mining/README.md) |
| AI & Machine Learning | V | 4 | **R** | Y3 Experiment & Evaluate | Dataset card, baseline experiment, Experiment Card, notebook reproducible, Research One-Pager v0 — **pintu masuk utama** (entry door *Course Project*) | [`ai-ml/`](courses/ai-ml/README.md) |
| Pengujian Perangkat Lunak | V | [isi] | E | Y3 | Test suite/protokol evaluasi untuk sistem ML (testing evidence) | (memakai [`software-engineering/`](courses/software-engineering/README.md)) |
| Proyek Perangkat Lunak | VI | 4 | E → R | Y3 | Prototype + laporan evaluasi pengguna + AI Usage Statement; kandidat artefak `ART-` | (memakai [`software-engineering/`](courses/software-engineering/README.md)) |
| Kerja Praktik | VI | [isi] | E | Y3 | **Problem Brief** dari masalah nyata tempat KP → Issue `type:problem` (entry door *Partner*) | — |
| Etika Profesi | VI | [isi] | E | Y3 | Kajian etika & privasi satu kasus AI → embrio `docs/ethics.md` | — |
| Mata kuliah/topik pilihan bidang **NLP** | [isi] | [isi] | R | Y3 | Korpus/anotasi kecil + benchmark baseline; dataset card | [`nlp/`](courses/nlp/README.md) |
| Metodologi Penelitian (Metopen) | VII | 2 | **R** | Y4 Prove & Contribute | **Research Pack** + Proposal TA + release `v1.0` | [`research-methods/`](courses/research-methods/README.md) |
| Tugas Akhir (TA) | VIII | 4 | **R** | Y4 | Research Pack lengkap + manuscript + artefak/ART + handoff ke AI Center | [`final-project/`](courses/final-project/README.md) |

Catatan:

- Prodi memosisikan kompetensinya pada Software Engineering, Data Science, IoT, dan NLP (dokumen diskusi). Bidang NLP belum tampak sebagai satu nama MK dalam tabel kurikulum yang dikutip, karena itu ditulis sebagai *mata kuliah/topik pilihan bidang NLP*; pengampu mengisi nama resmi, semester, dan SKS-nya.
- MK tanpa folder tetap menghasilkan artefak; artefaknya dicatat langsung di `datasets-registry/` (dataset card), `research-backlog/` (problem brief), atau repo proyek mahasiswa. Folder baru dibuat bila MK naik ke mode R (§7 langkah 3).
- Kalkulus (sem. I) mendukung fondasi tetapi tidak dipetakan artefak riset.

## 5. Status folder

| Folder | Isi saat ini | Status |
|---|---|---|
| [`courses/ai-ml/`](courses/ai-ml/README.md) | README (identitas, CPMK riset, project guide, rubrik) + [`research-artifact.md`](courses/ai-ml/research-artifact.md) | Phase 3 Curriculum Integration — desain siap; RPS dan artefak riil menyusul |
| [`courses/research-methods/`](courses/research-methods/README.md) | README + [`research-artifact.md`](courses/research-methods/research-artifact.md); desain penuh di `research-os/04` dan halaman mingguan di `metopen-research-studio/` | Phase 2 Pilot Metopen (semester VII pertama) — artefak riil menyusul |
| [`courses/data-mining/`](courses/data-mining/README.md) | README + [`research-artifact.md`](courses/data-mining/research-artifact.md) | Phase 3 — artefak riil menyusul |
| [`courses/nlp/`](courses/nlp/README.md) | README + [`research-artifact.md`](courses/nlp/research-artifact.md) | Phase 3 — nama MK resmi, semester, SKS `[isi]`; artefak riil menyusul |
| [`courses/software-engineering/`](courses/software-engineering/README.md) | README + [`research-artifact.md`](courses/software-engineering/research-artifact.md) | Phase 3 — artefak riil menyusul |
| [`courses/final-project/`](courses/final-project/README.md) | README + [`research-artifact.md`](courses/final-project/research-artifact.md) | Mengikuti angkatan pertama Metopen Studio; artefak riil menyusul |
| [`faculty-guide/`](faculty-guide/README.md) | Lecturer Playbook ringkas | Draft v0.1 |
| [`student-guide/`](student-guide/README.md) | Student Research Playbook ringkas | Draft v0.1 |
| [`assessment/`](assessment/README.md) | Asesmen lintas MK | Draft v0.1 |

"Artefak riil" berarti: dataset card yang benar-benar terdaftar, Issue backlog dari proyek MK, Experiment Card dari tim nyata, dan handoff yang benar-benar terjadi. Status ini diperbarui tiap akhir semester oleh koordinator komponen.

## 6. Alur Build → Prove → Contribute

Arsitektur akademik [ARC-04](../research-os/02-academic-architecture/04-build-prove-contribute.md): mata kuliah teknis **membangun** research asset, Metopen **membuktikan** kualitas buktinya, TA **berkontribusi** pengetahuan/artefak.

```
BUILD (sem. I–VI)                    PROVE (sem. VII)                CONTRIBUTE (sem. VIII →)
Statistika · Basis Data · Data Mining   Metopen Research Studio          Tugas Akhir
RPL · AI/ML · Pengujian PL · Proyek PL  16 minggu · 8 gate (G1–G8)       G6–G8 penuh · manuscript
KP · Etika · NLP                        Research Pack v1.0               paper / dataset / ART / HKI
        │                                      │                                 │
        ▼                                      ▼                                 ▼
 dataset card, baseline, experiment card,  proposal TA yang lolos G5–G8     PUB-/DS-/ART-YYYY-NNN
 problem brief, prototype, test evidence   (TA Ready → Research Ready)     handoff ke AI Research Center
        └──────────────── satu Research ID UIAI-YYYY-NNN mengikuti riset sepanjang alur ────────────────┘
```

Tiga konsekuensi praktis:

1. **Metopen tidak mulai dari nol.** W1–W2 Metopen diawali dengan inventarisasi artefak Build: Experiment Card AI/ML, dataset card Data Mining/Basis Data, problem brief KP. Entry door *Course Project* adalah jalur yang diutamakan.
2. **TA tidak mengulang Metopen.** TA dimulai dari Research Pack (minimal G5 lulus); pembimbing membaca handoff, bukan mendengar ide baru.
3. **Gate di MK teknis bersifat embrio.** Reviewer formal baru di Metopen dan TA. Di MK Build, gate dipakai sebagai *bahasa* rubrik (misalnya "baseline dan metrik ditetapkan sebelum eksperimen" = embrio G5), bukan sebagai PR review resmi — kecuali pengampu memilih memakainya.

## 7. Handoff antar mata kuliah

Setiap perpindahan memakai [TPL-14 Research Handoff](../research-os/08-templates/14-research-handoff-template.md): *what exists, missing evidence, next steps, owner*. Handoff disimpan di repo proyek (`docs/handoff.md`) dan dirujuk dari Issue backlog.

| Dari | Ke | Yang diserahkan | Kapan | Yang menandatangani |
|---|---|---|---|---|
| Basis Data / Data Mining | `datasets-registry/` → AI/ML, NLP | Dataset card v0, skema, catatan kualitas & leakage | Akhir semester III/IV | Pengampu + pengelola registry |
| Kerja Praktik | `research-backlog/` → Metopen | Problem Brief (Issue `type:problem`), kontak stakeholder, batasan data | Akhir KP | Mahasiswa + pembimbing KP |
| AI/ML | Metopen (W1–W2) | Experiment Card, repo reproducible, Research One-Pager v0, AI Usage Log | Akhir semester V, atau saat mahasiswa mendaftar Metopen | Pengampu AI/ML + mahasiswa |
| RPL / Pengujian PL / Proyek PL | Metopen atau AI Center | Research-grade software, test evidence, artifact README, laporan evaluasi pengguna | Akhir semester | Pengampu + mahasiswa |
| NLP | `datasets-registry/` → Metopen / riset dosen | Korpus + guideline anotasi + benchmark baseline | Akhir semester | Pengampu + pengelola registry |
| Metopen | TA | **Research Pack v1.0** + Proposal TA + handoff G8 | W16 | Pengampu Metopen + calon pembimbing TA |
| TA | AI Research Center / `publications/` | Manuscript, artefak, dataset, handoff "apa yang belum terbukti" | Setelah sidang | Pembimbing + mahasiswa + pengelola publications |

Aturan: handoff yang tidak menyebut *missing evidence* ditolak. Riset yang diwariskan tanpa daftar bukti yang belum ada akan diulang dari nol oleh penerima.

## 8. Cara dosen mendaftarkan mata kuliahnya

Lima langkah; total waktu yang wajar: satu sesi workshop kurikulum + 2–3 jam kerja mandiri.

1. **Tentukan mode F / E / R.** Pakai kriteria [ARC-03](../research-os/02-academic-architecture/03-ai-contribution-modes.md): apakah MK Anda *mendukung* (F), *memakai kasus AI* (E), atau *menghasilkan asset yang dipakai ulang* (R)? Mode boleh naik bertahap (E → R) dan tidak harus R. Catat keputusan di tabel §4 lewat PR.
2. **Pilih 1–3 sel di tabel kompetensi × tahun** [ARC-01 §7](../research-os/02-academic-architecture/01-research-capability-spiral.md) yang menjadi tanggung jawab MK Anda, lalu tulis sebagai **CPMK riset tambahan** dengan kerangka [ARC-05](../research-os/02-academic-architecture/05-cpl-cpmk-artifact-alignment.md): CPL → CPMK → Learning Activity → Assessment → Research Artifact → Evidence.
3. **Tetapkan research asset + template.** Bila MK sudah punya folder di `courses/`, revisi `research-artifact.md`-nya. Bila belum dan mode Anda R, ajukan folder baru lewat PR (`README.md` + `research-artifact.md` mengikuti pola folder yang ada). Mode F/E tanpa folder cukup menunjuk registry/backlog sebagai tujuan artefak.
4. **Sambungkan ke backlog dan registry.** Daftarkan problem yang akan dipakai kelas ke [`research-backlog/`](../research-backlog/README.md) (Issue *Research Problem*) dan dataset ke [`datasets-registry/`](../datasets-registry/README.md) (metadata saja). Minta pengelola menetapkan nilai field **Course** di Mission Control untuk Issue yang lahir dari kelas Anda.
5. **Tutup semester dengan handoff dan status.** Isi [TPL-14](../research-os/08-templates/14-research-handoff-template.md) untuk tim yang layak dilanjutkan, perbarui baris MK Anda di §5, dan serahkan ringkasan artefak ke koordinator komponen untuk bukti OBE/akreditasi ([GOV-05](../research-os/07-governance/05-ppts-and-institutional-evidence.md)).

Panduan yang lebih rinci untuk setiap langkah ada di [Faculty Guide](faculty-guide/README.md).

## 9. Siapa memelihara komponen ini

| Peran | Tanggung jawab |
|---|---|
| Koordinator komponen (tim kurikulum / koordinator Metopen) | Memperbarui tabel §4 dan status §5; menyetujui folder MK baru |
| Pengampu MK | README, `research-artifact.md`, `RPS.md` folder MK-nya; handoff akhir semester |
| Pengelola registry/backlog | Memberi ID `DS-`/`UIAI-`; memverifikasi metadata dari kelas |
| `@maintainers` | Review PR ke komponen ini; menjaga link dan konsistensi istilah dengan [MST-03](../research-os/00-master/03-glossary.md) |

Perubahan diajukan lewat PR ke branch `docs/<topik>` ([CONTRIBUTING.md](../CONTRIBUTING.md)).

[^1]: Struktur kurikulum, semester, dan SKS dikutip dari tabel kurikulum dalam dokumen diskusi *Riset AI UAI untuk Negeri* (`research-os/00-master/source/`). Verifikasi terhadap dokumen kurikulum resmi Prodi sebelum dipakai dalam dokumen formal.
