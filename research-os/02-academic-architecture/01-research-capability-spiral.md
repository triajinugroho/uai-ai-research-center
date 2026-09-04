# Research Capability Spiral — Model Empat Tahun Pertumbuhan Kapabilitas Riset

> **ID** ARC-01 · **Paket** 02 Academic Architecture · **Tier** 2 (Academic Design) · **Status** Draft v0.1 (2026-09)
> **Audiens** Tim kurikulum, Kaprodi, dosen pengampu seluruh mata kuliah, dosen pembimbing TA, koordinator Metopen
> **Terkait** [MST-03 Glossary](../00-master/03-glossary.md) · [STR-02 Vision & Endgame](../01-strategic-foundation/02-vision-and-endgame.md) · [ARC-02 Curriculum Research Map](02-curriculum-research-map.md) · [ARC-03 AI Contribution Modes](03-ai-contribution-modes.md) · [ARC-04 Build–Prove–Contribute](04-build-prove-contribute.md) · [AIX-01 Research Meta-Thinking](../05-ai-augmented-research/01-research-meta-thinking.md) · [AIX-02 AI Research Competency](../05-ai-augmented-research/02-ai-research-competency-framework.md) · [OPS-03 Research Gates](../06-execution-os/03-research-gates.md)

## 1. Mengapa spiral, bukan tangga

Metodologi Penelitian di semester VII hanya 2 SKS. Kalau research thinking baru diperkenalkan di sana, dua SKS itu harus mengajarkan segalanya sekaligus: bertanya, mencari bukti, merancang eksperimen, menulis, dan mempertanggungjawabkan. Hasilnya seperti yang diperingatkan dokumen sumber: *semua dikenalkan, tidak ada yang dikuasai.*

Kenyataannya, mahasiswa Informatika UAI sudah membawa modal yang cukup. Sejak semester I mereka belajar Statistika dan Kalkulus; semester II Statistika Terapan dan Matematika Diskrit; semester III HCI, Struktur Data, Basis Data; semester IV Analisis Algoritma, RPL, Data Mining; semester V AI & Machine Learning dan Pengujian Perangkat Lunak; semester VI Proyek Perangkat Lunak, Kerja Praktik, Etika Profesi. Metopen adalah **integration layer** atas semua itu, dan TA adalah **contribution stage**-nya.[^1]

Masalahnya, kompetensi itu tumbuh sebagai *kemampuan teknis* — bukan sebagai *kemampuan menghasilkan pengetahuan yang evidence-based*. Research Capability Spiral menutup jarak itu tanpa menambah SKS dan tanpa mengubah semua mata kuliah menjadi kelas riset. Ide dasarnya:

- Kompetensi riset yang sama — **mengamati, bertanya, membandingkan, membuktikan, mempertanggungjawabkan** — muncul berulang setiap tahun, pada tingkat kesulitan dan tanggung jawab yang lebih tinggi. Itulah sebabnya bentuknya *spiral*, bukan tangga: mahasiswa tidak "lulus" dari evidence reasoning di tahun pertama; mereka kembali ke sana di tahun ke-4 dengan taruhan yang lebih besar.
- Setiap tahun punya satu **tema kognitif** yang sederhana untuk dikomunikasikan ke dosen dan mahasiswa.
- Setiap putaran menghasilkan **artefak** yang dapat dipakai ulang oleh putaran berikutnya (prinsip *research assets should compound*).
- Setiap putaran menaikkan satu tingkat **AI research competency** ([AIX-02](../05-ai-augmented-research/02-ai-research-competency-framework.md)): AI Consumer → AI Collaborator → AI Investigator → AI Governor.

```
                       Year 4  PROVE & CONTRIBUTE
                    ┌──────────────────────────────┐
                    │ Metopen (Prove) · TA (Contribute)
                    │ Research Pack · Proposal TA · Paper/Artefak
                Year 3  EXPERIMENT & EVALUATE      │
             ┌───────────────────────────────┐     │
             │ AI/ML · Pengujian PL · Proyek PL     │
             │ Kerja Praktik · Etika Profesi        │
         Year 2  BUILD & COMPARE                    │
      ┌─────────────────────────────────┐           │
      │ HCI · Struktur Data · Basis Data │           │
      │ Analisis Algoritma · RPL · Data Mining       │
  Year 1  OBSERVE & REASON                          │
┌──────────────────────────────┐                    │
│ Statistika · Kalkulus        │                    │
│ Statistika Terapan · Mat. Diskrit                 │
└──────────────────────────────┴────────────────────┘
   kompetensi yang sama, tanggung jawab makin besar ──►
```

## 2. Ringkasan empat putaran

| Tahun | Tema | Pertanyaan inti yang harus bisa dijawab mahasiswa | Kompetensi riset yang ditumbuhkan | Level AI competency (target akhir tahun) | Gate yang "dilatih" (belum formal) |
|---|---|---|---|---|---|
| **Year 1** | Observe & Reason | "Apa yang sebenarnya ditunjukkan data ini, dan apa yang *tidak* boleh saya simpulkan?" | Evidence reasoning, statistical thinking, formal reasoning | **AI Consumer** yang sadar batas (tahu AI bisa salah) | G2 Problem (embrio), G3 Evidence (membaca) |
| **Year 2** | Build & Compare | "Saya membangun sesuatu — dibanding apa, diukur dengan apa, pada data apa?" | Baseline thinking, data infrastructure, benchmark, human evaluation, research-grade engineering | **AI Collaborator** (memberi konteks, mengiterasi, memeriksa hasil) | G5 Method (embrio), G6 Experiment (embrio) |
| **Year 3** | Experiment & Evaluate | "Apakah klaim saya bertahan terhadap baseline, error analysis, threats to validity, dan pengguna nyata?" | Experimental design, ML evaluation, testing AI systems, ethics & privacy, problem discovery | **AI Investigator** (memakai AI untuk riset dengan verifikasi) | G5 Method, G6 Experiment, G7 Claim (dalam konteks MK) |
| **Year 4** | Prove & Contribute | "Bukti apa yang membuat klaim saya layak dipercaya, dan siapa yang bisa memeriksanya?" | Full mini research cycle, scientific argumentation, reproducibility, defense, contribution | **AI Investigator** dengan perilaku **AI Governor** (verifikasi, dokumentasi, akuntabilitas) | G1–G8 formal |

Kata kunci untuk sosialisasi ke dosen: **Year 1 belajar membaca bukti, Year 2 belajar membandingkan, Year 3 belajar menguji, Year 4 belajar membuktikan dan berkontribusi.**

## 3. Year 1 — Observe & Reason

**Mata kuliah pendukung:** Statistika (3 SKS, sem. I), Kalkulus (sem. I), Statistika Terapan (3 SKS, sem. II), Matematika Diskrit (sem. II).

**Kompetensi riset yang ditumbuhkan**

- Membaca tabel, grafik, dan ringkasan statistik dengan benar: apa yang ditunjukkan, apa yang tidak ditunjukkan.
- Membedakan korelasi dan kausalitas; mengenali confounder sederhana; memahami variabilitas dan ketidakpastian.
- Memahami bahwa setiap angka membutuhkan pembanding (embrio *baseline thinking*).
- Penalaran formal: definisi, asumsi, bukti sederhana, counterexample — fondasi *falsification*.
- Menulis satu paragraf **Claim–Evidence–Reasoning** dari data kecil.

**Artefak yang dihasilkan**

- Laporan analisis data kecil (deskriptif + satu uji inferensial) dengan bagian "apa yang tidak boleh disimpulkan".
- Notebook analisis yang dapat dijalankan ulang (embrio reproducibility; cukup seed, data, dan langkah).
- Catatan bukti/counterexample untuk satu klaim matematis.

**Meta-skill utama** ([AIX-01](../05-ai-augmented-research/01-research-meta-thinking.md)): *evidence literacy*, *causal/statistical reasoning*, *first principles*, *falsification* (versi awal).

**Level AI competency:** AI Consumer yang sadar batas. Mahasiswa boleh memakai AI untuk menjelaskan konsep statistik, tetapi tugas menuntut mereka memverifikasi penjelasan itu terhadap buku/notebook dan menemukan minimal satu kekeliruan AI selama semester.

**Indikator akhir Year 1**

| Indikator | Cara mengukur |
|---|---|
| Mahasiswa dapat menjelaskan mengapa sebuah korelasi tidak membuktikan sebab-akibat pada satu kasus nyata | Soal kasus dalam UTS/UAS Statistika Terapan |
| Mahasiswa dapat menyebut minimal dua hal yang tidak boleh disimpulkan dari tabel hasil | Rubrik laporan analisis |
| Notebook analisis dapat dijalankan ulang oleh teman sekelas | Peer check sederhana di kelas |
| Mahasiswa dapat menuliskan satu paragraf CER yang benar | Rubrik tugas |

## 4. Year 2 — Build & Compare

**Mata kuliah pendukung:** HCI, Struktur Data, Basis Data (sem. III); Analisis Algoritma, RPL, Data Mining (sem. IV).

**Kompetensi riset yang ditumbuhkan**

- **Baseline thinking**: setiap artefak yang dibangun dibandingkan dengan alternatif paling sederhana yang masuk akal.
- **Pengukuran yang benar**: mengukur waktu/akurasi/kegunaan dengan prosedur yang bisa diulang (Struktur Data, Analisis Algoritma, Data Mining).
- **Data infrastructure**: merancang skema, data dictionary, dan kartu dataset; memahami kualitas dan provenance data (Basis Data, Data Mining).
- **Human evaluation**: menyusun protokol user study sederhana, instrumen, dan etika partisipan (HCI).
- **Research-grade engineering**: repositori terstruktur, pengujian, dokumentasi cara menjalankan (RPL).
- **Evaluation & leakage awareness**: train/test split, cross-validation, kebocoran data (Data Mining).

**Artefak yang dihasilkan**

- Benchmark harness kecil + laporan perbandingan (Struktur Data / Analisis Algoritma).
- Skema data + dataset card v0 untuk satu data nyata yang sudah dianonimkan (Basis Data) — kandidat entri `datasets-registry/`.
- Protokol dan hasil user study kecil (HCI).
- Repositori proyek dengan README reproducibility (RPL).
- Laporan eksperimen Data Mining dengan baseline, metrik yang dijelaskan, dan pemeriksaan leakage.

**Meta-skill utama:** *decomposition*, *abstraction*, *hypothesis* (awal), *evidence literacy* lanjut, *systems thinking* (awal).

**Level AI competency:** AI Collaborator. Mahasiswa memberi konteks yang cukup kepada AI (data, tujuan, batasan), mengiterasi, dan memeriksa output; setiap kode yang dibantu AI harus diuji. Mulai dikenalkan AI Usage Log ringan ([TPL-10](../08-templates/10-ai-usage-log-template.md)).

**Indikator akhir Year 2**

| Indikator | Cara mengukur |
|---|---|
| Setiap proyek MK menyebut baseline dan metrik secara eksplisit | Checklist rubrik proyek |
| Mahasiswa dapat menjelaskan satu cara leakage terjadi dan mencegahnya | Soal/tugas Data Mining |
| Minimal satu dataset card v0 dihasilkan per kelas Basis Data/Data Mining | Hitung entri kandidat registry |
| Repositori proyek RPL dapat dijalankan orang lain mengikuti README | Peer reproduction |

## 5. Year 3 — Experiment & Evaluate

**Mata kuliah pendukung:** AI & Machine Learning (4 SKS, sem. V), Pengujian Perangkat Lunak (sem. V); Proyek Perangkat Lunak (4 SKS, sem. VI), Kerja Praktik (sem. VI), Etika Profesi (sem. VI).

Ini putaran paling menentukan karena proyek AI/ML semester V adalah **pintu masuk utama** riset mahasiswa ke pipeline (entry door *Course Project*, lihat [ARC-04](04-build-prove-contribute.md)).

**Kompetensi riset yang ditumbuhkan**

- **Experimental design untuk ML**: hipotesis, variabel, kontrol, baseline, metrik selaras tujuan, ablation/error analysis, variansi antar seed (AI/ML).
- **Evaluasi multi-dimensi**: bukan hanya accuracy — robustness, fairness awal, biaya, kegunaan (AI/ML, Pengujian PL).
- **Testing AI systems**: pengujian sistem berbasis ML/LLM, metamorphic testing, regression pada model (Pengujian PL).
- **Prototype engineering dengan evaluasi**: membangun prototype AI untuk domain nyata dan mengevaluasinya dengan pengguna (Proyek PL).
- **Problem discovery**: menulis problem brief dari masalah nyata tempat Kerja Praktik — calon entri research backlog (entry door *Partner*).
- **Responsible research**: privasi, consent, bias, AI disclosure, amanah epistemik (Etika Profesi).

**Artefak yang dihasilkan**

- **Experiment Card** ([TPL-09](../08-templates/09-experiment-card.md)) + repositori eksperimen reproducible + laporan hasil dengan error analysis (AI/ML) — research asset yang wajib didaftarkan bila MK bermode R ([ARC-03](03-ai-contribution-modes.md)).
- Test suite/protokol evaluasi untuk sistem ML (Pengujian PL).
- Prototype + laporan evaluasi pengguna + AI Usage Statement (Proyek PL).
- Problem Brief dari Kerja Praktik → Issue `type:problem` di research backlog.
- Kajian etika & privasi satu kasus AI (Etika Profesi) → embrio `docs/ethics.md`.

**Meta-skill utama:** *hypothesis*, *falsification*, *causal/statistical reasoning* lanjut, *systems thinking*, *problem framing* (dari KP).

**Level AI competency:** AI Investigator. Mahasiswa memakai AI untuk mengkritik desain eksperimen, membangkitkan hipotesis alternatif, dan membantu analisis — dengan verifikasi sumber, penalaran, dan bukti. AI Usage Log menjadi bagian penilaian proyek AI/ML.

**Indikator akhir Year 3**

| Indikator | Cara mengukur |
|---|---|
| ≥ 1 Experiment Card per tim AI/ML, dengan baseline dan metrik ditetapkan sebelum eksperimen | Rubrik proyek AI/ML |
| Peer dapat mereproduksi angka baseline dari repositori tim | Peer reproduction (embrio G6) |
| ≥ 1 problem brief per mahasiswa KP masuk backlog | Hitung Issue `type:problem` |
| Laporan proyek memuat threats to validity dan AI Usage Statement | Checklist |
| Persentase proyek AI/ML yang di-handoff ke Metopen ([TPL-14](../08-templates/14-research-handoff-template.md)) | Registry handoff |

## 6. Year 4 — Prove & Contribute

**Mata kuliah pendukung:** Metodologi Penelitian (2 SKS, sem. VII), Tugas Akhir (4 SKS, sem. VIII).

**Kompetensi riset yang ditumbuhkan**

- Menjalankan **satu mini research cycle penuh** dalam 16 minggu: Endgame → Problem → Search → Evidence → Gap → RQ → Method → Design Defense → Repository → Pilot → Analysis → Contribution → Manuscript → Peer Review → Revision → Defense ([MET-03](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)).
- **Literature intelligence**: synthesis matrix, Gap–Claim–Evidence alignment, bukan ringkasan paper satu per satu.
- **Research design & validity** dengan Computing Research Methods Map; threats to validity wajib.
- **Reproducible research**: repositori riset sebagai artefak yang dapat diperiksa ([TPL-15](../08-templates/15-research-repository-template.md)).
- **Scientific argumentation & defense**: manuscript, peer review sebagai reviewer, research pitch 7–10 menit.
- **Contribution**: TA yang menjawab RQ dengan bukti; output tambahan sesuai [ARC-06](06-research-output-taxonomy.md) (paper, dataset, artefak, HKI, prototype).

**Artefak yang dihasilkan**

- **Research Pack** ([MET-04](../04-metopen-research-studio/04-research-pack-specification.md)) + Proposal TA + release `v1.0 Research Pack` (Metopen).
- Laporan TA + repositori final + minimal satu output dari taksonomi selain laporan TA untuk endgame di atas *TA Ready* (TA).
- Handoff ke AI Research Center: apa yang ada, bukti yang belum ada, langkah berikut, owner ([TPL-14](../08-templates/14-research-handoff-template.md)).

**Meta-skill utama:** seluruh sepuluh meta-skill AIX-01, dengan penekanan pada *metacognition* (mahasiswa menilai sendiri kualitas buktinya) dan *falsification*.

**Level AI competency:** minimal AI Investigator untuk semua mahasiswa; perilaku AI Governor diwajibkan lewat AI Research Protocol ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)): Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own.

**Indikator akhir Year 4**

| Indikator | Cara mengukur |
|---|---|
| 100% mahasiswa lulus Metopen berstatus **TA Ready** (lolos G5) | Mission Control / leaderboard |
| ≥ target % **Research Ready** (lolos G6–G7) | Mission Control |
| % TA yang dimulai dari Research Pack tanpa mengulang dari nol | Survei pembimbing TA + handoff |
| % TA menghasilkan output selain laporan (paper/dataset/artefak/HKI) | `publications/`, `datasets-registry/` |
| 0 pelanggaran Research Integrity Gate | Checklist [TPL-11](../08-templates/11-research-integrity-checklist.md) |

Target angka per tahun ditetapkan di [GOV-03](../07-governance/03-kpi-and-measurement.md).

## 7. Tabel pemetaan kompetensi × tahun

Setiap baris adalah satu kompetensi riset; setiap kolom menunjukkan bentuknya pada tahun tersebut. Kompetensi tidak "selesai" — ia naik tingkat.

| Kompetensi riset | Year 1 Observe & Reason | Year 2 Build & Compare | Year 3 Experiment & Evaluate | Year 4 Prove & Contribute |
|---|---|---|---|---|
| **Problem framing** | Mengenali fenomena di balik data | Merumuskan masalah yang diselesaikan artefak | Menulis problem brief dari KP/proyek; stakeholder & keputusan | Problem Brief + impact statement yang lolos G2 |
| **Evidence literacy** | Membaca tabel/grafik; korelasi ≠ kausalitas | Membaca dokumentasi & paper teknis untuk memilih pendekatan | Membaca paper ML/SE kritis: baseline, metrik, keterbatasan | Synthesis matrix 15–25 sumber; Gap–Claim–Evidence (G3–G4) |
| **Statistical & causal reasoning** | Uji hipotesis dasar, variabilitas | Perbandingan kinerja dengan pengulangan | Variansi antar seed, signifikansi praktis, confounder | *Enough statistics to prevent bad claims*; analisis G7 |
| **Data handling & infrastructure** | Membersihkan data kecil | Skema, data dictionary, dataset card v0 | Data plan, privasi, provenance, split yang benar | Dataset/Data Plan G5; registrasi `DS-YYYY-NNN` bila baru |
| **Building & comparing (baseline thinking)** | Angka butuh pembanding | Baseline eksplisit pada setiap proyek | Baseline + metode pembanding + ablation | Baseline & Metrics dalam Research Design (G5) |
| **Experimental design & evaluation** | Mengamati eksperimen orang lain | Mengukur dengan prosedur berulang | Experiment Card; error analysis; evaluasi multi-dimensi | Pilot experiment (G6) dan analisis (G7) |
| **Validity & reproducibility** | Notebook bisa dijalankan ulang | README reproducibility pada repo proyek | Threats to validity awal; peer reproduction | Reproducibility package; threats to validity wajib (G5–G7) |
| **Scientific argumentation & writing** | Satu paragraf CER | Laporan perbandingan yang jujur | Laporan eksperimen dengan klaim terbatas bukti | Manuscript/Proposal TA; CER per RQ (G7–G8) |
| **Research integrity & ethics (amanah epistemik)** | Tidak mengarang angka; sitasi jujur | Tidak menyalin kode tanpa atribusi; lisensi | Privasi, consent, bias, AI disclosure (Etika Profesi) | Research Integrity Gate lulus/gagal; Ethics & Privacy dalam Pack |
| **AI-augmented research competency** | AI Consumer sadar batas | AI Collaborator; AI Usage Log ringan | AI Investigator; AI Usage Log dinilai | AI Investigator + perilaku AI Governor; AI Usage Statement |
| **Collaboration & review** | Peer check notebook | Code review antar tim | Red team ringan pada desain eksperimen | Peer review formal ([TPL-12](../08-templates/12-peer-review-template.md)); Design Defense W8 |
| **Contribution & dissemination** | — | Artefak dipakai ulang tim lain di kelas | Research asset terdaftar + handoff | TA + paper/dataset/artefak/HKI; handoff ke AI Center |

## 8. Bagaimana spiral ini dipakai

1. **Tim kurikulum** memakai tabel §7 sebagai kerangka saat merevisi RPS: setiap MK mengambil satu–tiga sel yang menjadi tanggung jawabnya dan menuliskannya sebagai CPMK + artefak ([ARC-05](05-cpl-cpmk-artifact-alignment.md)).
2. **Dosen pengampu** menandai mode MK-nya (F/E/R) dengan [ARC-03](03-ai-contribution-modes.md); mode F cukup memperkuat sel Year 1–2, mode R wajib menghasilkan artefak yang tercatat.
3. **Koordinator Metopen** memakai indikator Year 3 untuk mengetahui kesiapan angkatan yang masuk: berapa Experiment Card, berapa problem brief, berapa handoff.
4. **Pembimbing TA** memakai indikator Year 4 dan handoff Metopen sebagai titik mulai bimbingan.
5. **Pusat riset** membaca spiral sebagai *student pipeline* ([AIR-01](../03-ai-research-ecosystem/01-ai-research-center-concept.md)): artefak Year 2–3 mengisi backlog dan registry; Year 4 mengisi Mission Control.

Yang **tidak** diminta oleh spiral ini: menambah SKS, mengubah nama mata kuliah, atau mewajibkan semua dosen membimbing riset. Yang diminta hanyalah satu lapisan tipis berpikir riset pada aktivitas yang sudah ada — *one activity, multiple outcomes*.

## 9. Risiko dan batasan

| Risiko | Mitigasi |
|---|---|
| Dosen Year 1–2 merasa "ini bukan urusan riset" | Framing: Year 1–2 hanya *evidence reasoning* dan *baseline thinking*, bukan riset; contoh tugas siap pakai di [ARC-02](02-curriculum-research-map.md) |
| Artefak Year 2–3 tidak pernah dipakai ulang | Registrasi ringan (dataset card, Issue backlog); Metopen W1–W2 memulai dari artefak yang sudah ada |
| Spiral hanya ada di dokumen, tidak di RPS | Workshop dosen 1 hari ([ARC-02 §6](02-curriculum-research-map.md)) menghasilkan revisi minimal 1 CPMK per MK |
| Level AI competency dipaksakan tanpa alat | [AIX-05](../05-ai-augmented-research/05-ai-tools-reference.md) dan AI Usage Log yang sangat ringan di Year 1–2 |

[^1]: Struktur kurikulum dan SKS berasal dari dokumen diskusi *Riset AI UAI untuk Negeri* (tabel kurikulum semester I–VIII); verifikasi terhadap dokumen kurikulum resmi Prodi sebelum dipakai dalam dokumen formal.
