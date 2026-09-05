# Rubrics — Rubrik 5E dan Skema Nilai, Versi Mahasiswa

> **Status** Draft v0.1 (2026-09) · Versi ringkas; rubrik lengkap empat level per E, kalibrasi antar penilai, dan contoh perhitungan ada di [MET-06 Assessment & 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md)
> **Terkait** [Studio README](../README.md) · [research-gates](../research-gates/README.md) · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [TPL-11 Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) · [TPL-13 Research Defense](../../research-os/08-templates/13-research-defense-template.md)

Metopen menilai **apa yang Anda hasilkan dan pertanggungjawabkan**, bukan apa yang Anda hafal. Tidak ada UTS/UAS tertulis. Nilai tidak bisa "dikejar di akhir semester": tim yang tidak lolos G3 di W5 tidak bisa menutupnya dengan proposal bagus di W15, karena proposal tanpa evidence map tidak lolos G8. Rubrik ini dibagikan sejak S0; tidak ada kriteria tersembunyi.

## 1. Rubrik 5E

Empat level: **Exemplary (4) · Proficient (3) · Developing (2) · Beginning (1)**. Proficient = standar **TA Ready**. Exemplary = standar **Research/Publication Ready**. Developing = gate belum lulus, revisi. Beginning = artefak belum ada secara substantif. Konversi: Exemplary 100% · Proficient 85% · Developing 70% · Beginning 55% · tidak ada 0% dari bobot komponen.

| E | Apa yang dinilai | Bobot | Artefak yang dinilai | Minggu / gate penilaian |
|---|---|---|---|---|
| **E1 End** | Kejelasan endgame & problem: endgame spesifik, masalah problem-first dengan stakeholder nyata, RQ tertelusur ke gap, kontribusi sepadan dengan rencana bukti | 10% | `docs/endgame.md`, Problem Brief, Stakeholder/Impact, RQ/Hypothesis, Contribution Statement | W1 (G1), W2 (G2), W6 (G4) |
| **E2 Evidence** | Kualitas bukti literatur: strategi pencarian, synthesis matrix berpola, sumber terverifikasi, gap merujuk baris matriks | 15% | Search strategy, synthesis matrix, Literature Evidence Map, `references.bib`, Research Gap | W3–W5 (G3), W6 (G4) |
| **E3 Experiment** | Kualitas desain & pilot: metode cocok RQ, baseline & metrik sebelum eksperimen, anti-leakage, data plan berlisensi/privasi, pilot direproduksi peer | 15% | Research Design Card, Data Plan, Baseline & Metrics, Experiment Card, hasil pilot, catatan reproduksi peer | W7–W8 (G5), W9–W10 (G6) |
| **E4 Explanation** | Argumentasi Claim–Evidence–Reasoning: klaim menunjuk tabel/figur, ketidakpastian dilaporkan, hasil negatif dibahas, threats diperbarui, proposal konsisten dengan repositori | 10% (+ fokus Defense) | `results/analysis.md`, tabel CER, Threats v2, Contribution revisi, Proposal TA, figur | W11–W12 (G7), W13–W15 (G8) |
| **E5 Execution** | Disiplin sprint, repositori, gate: struktur TPL-15, Reproducibility README, commit dengan Task ID, PR gate tepat waktu, release, AI Usage Log kontemporer | 10% (+ komponen D) | Repositori, README, AI Usage Log, riwayat PR gate, release | Semua minggu / semua gate |

### Contoh Exemplary vs Beginning, satu baris per E

| E | Exemplary | Beginning |
|---|---|---|
| End | "Tim akademik memakai prediksi ini untuk memutuskan intervensi di minggu ke-4" — orang luar mengulang masalah dalam dua kalimat; RQ bisa salah dan menunjuk baris matriks | Endgame "membuat aplikasi X"; RQ berupa judul; tidak ada stakeholder |
| Evidence | ≥20 sumber primer dibaca; matriks memperlihatkan konsisten/bertentangan/belum diuji; gap "baris 4, 9, 12 bertentangan pada data Indonesia"; semua DOI dibuka | Daftar pustaka tanpa matriks; sumber tidak terverifikasi; tidak ada strategi pencarian |
| Experiment | Metode dipilih dengan alternatif yang ditolak; baseline & metrik ditetapkan sebelum run; ≥3 seed; peer mereproduksi tanpa bantuan tim; red team dijawab dengan perubahan tercatat | Tidak ada baseline; pilot tidak berjalan; desain berupa "metode kuantitatif" tanpa prosedur |
| Explanation | Setiap klaim menunjuk tabel/figur dengan ketidakpastian; error analysis menjelaskan mengapa metode gagal; kontribusi direvisi turun bila bukti lemah | Tidak ada analisis; proposal tidak sesuai repositori; klaim tanpa bukti |
| Execution | Peer menjalankan `run.sh` tanpa bertanya; commit kecil bermakna dengan Task ID; semua gate lewat PR tepat waktu; log AI spesifik dan kontemporer | Repositori nyaris kosong; tidak ada PR gate; tidak ada AI Usage Log |

Catatan: satu referensi yang tidak dapat diverifikasi membuat **G3 gagal** terlepas dari level — itu aturan integritas, bukan penurunan level.

## 2. Research Integrity Gate (lulus/gagal)

Integritas **tidak diberi skor** karena skor menyiratkan "sedikit fabrikasi masih dapat nilai". Ia adalah **syarat** nilai ([MET-06 §4](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md), [TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md)).

| Aspek | Ketentuan |
|---|---|
| Kapan diperiksa | Setiap PR gate (reviewer mencentang bagian integritas) dan Research Integrity Checklist TPL-11 di G8 sebelum defense |
| Yang membuat gagal | Fabrikasi/falsifikasi data atau hasil; plagiarisme; sitasi tidak ada/tidak dibaca; AI tidak diungkap padahal memengaruhi kesimpulan; data pribadi/sensitif di-commit; metric switching atau seed cherry-picking yang disembunyikan; hasil negatif disembunyikan |
| Akibat pada gate | Gate gagal terlepas dari level 5E; PR tidak di-merge; defense tidak dapat dijadwalkan sebelum checklist PASS |
| Akibat pada nilai | Nilai komponen A untuk gate itu ditangguhkan sampai remediasi; pelanggaran berat (fabrikasi, plagiarisme berat) ditangani sebagai pelanggaran kode etik ([CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)) dan kebijakan akademik Prodi (`[isi]`), dapat berujung nilai E |
| Remediasi | Kesalahan tidak disengaja (sitasi keliru, log AI kurang) diperbaiki dalam satu sprint dan dicatat; pelanggaran disengaja tidak dapat "diperbaiki" dengan mengganti artefak |
| Prinsip | Amanah epistemik: kejujuran terhadap kebenaran meskipun meruntuhkan hipotesis sendiri |

Checklist TPL-11 memuat item A–J (data, analisis, sitasi, plagiarisme, AI, etika & privasi, reproducibility, authorship, klaim, hasil negatif); setiap ✓ harus menunjuk bukti yang dapat dibuka. Satu item gagal pada A, C2, D1, E1–E3, atau F1–F2 = FAIL.

## 3. Skema nilai akhir

| Komponen | Bobot | Dinilai lewat | Kapan | Satuan |
|---|---|---|---|---|
| **A. Milestone Portfolio (Research Pack)** | **60%** | Rubrik 5E pada PR gate G1–G8: End 10 · Evidence 15 · Experiment 15 · Explanation 10 · Execution 10 | W1–W16 | Tim, dimodulasi individu |
| **B. Research Defense** | **15%** | TPL-13; rubrik 5E terfokus End + Explanation | W16 | Tim (presentasi) + individu (tanya-jawab) |
| **C. Peer Review sebagai reviewer** | **10%** | Kualitas 2 review TPL-12: spesifik, berbasis bukti, dapat ditindaklanjuti | W14 | Individu |
| **D. Partisipasi Sprint** | **15%** | Deliverable sprint tepat waktu, gate check hadir & bermakna, AI Usage Log konsisten, kontribusi terlihat di git/Issue | S0–S16 | Individu |
| **Research Integrity Gate** | **prasyarat** | Integrity check setiap gate + TPL-11 di G8 | Setiap gate | Lulus/gagal |
| **Total** | **100%** | | | |

Konversi ke nilai huruf mengikuti ketentuan Prodi (`[isi]`). Defense: keputusan **Lulus** (rata-rata ≥ 3, tidak ada kriteria 1, integritas PASS), **Lulus dengan revisi** (rata-rata ≥ 2,5; revisi ≤ 1 minggu), atau **Ulang** ([TPL-13](../../research-os/08-templates/13-research-defense-template.md)).

## 4. Penilaian tim vs individu

| Komponen | Unit | Cara memodulasi individu |
|---|---|---|
| A Portfolio | Tim | Nilai tim × faktor kontribusi individu (0,8–1,1) dari riwayat git (commit/PR bermakna, bukan jumlah baris), Issue/PR yang ditangani, AI Usage Log pribadi, peer contribution rating di W8 dan W16, observasi studio; selisih >0,2 antar anggota harus disertai bukti tertulis |
| B Defense | Tim + individu | Presentasi dinilai tim; tanya-jawab per orang — setiap anggota wajib menjawab minimal satu pertanyaan penguji |
| C Peer Review | Individu | Setiap mahasiswa menulis review sendiri; AI tidak dipakai untuk mereview tim lain |
| D Partisipasi | Individu | Kehadiran & kualitas gate check, deliverable sprint pribadi, log AI |
| Integrity | Individu & tim | Pelanggaran individu ditangani per orang; artefak tim yang tercemar tetap harus diperbaiki tim |

Kontribusi yang tidak terlihat di git, Issue, log, atau notulen dianggap tidak ada.

## 5. Remedial dan revisi

1. **Gate gagal bukan hukuman.** Reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan; tim merevisi dan membuka review ulang ([research-gates §3](../research-gates/README.md)).
2. **Batas revisi:** maksimal dua review ulang per gate; lebih dari itu dosen memutuskan penyempitan ruang lingkup.
3. **Nilai setelah revisi:** level 5E dinilai pada versi yang lulus, tanpa potongan; keterlambatan tercatat di E5 Execution dan komponen D — revisi tidak "gratis", tetapi tidak menghukum kualitas akhir.
4. **Batas waktu keras:** G5 paling lambat W9; G6 paling lambat W11; G8 di W16. Belum G5 pada W9 → konsultasi wajib + penyempitan ruang lingkup.
5. **Remedial akhir semester:** hanya untuk komponen B (defense ulang) dan artefak G8 yang belum lengkap, dalam jendela yang ditetapkan Prodi (`[isi]`); tidak ada remedial berupa "tugas tambahan" di luar Research Pack.

## 6. Ringkasan untuk mahasiswa

- Nilai datang dari **artefak yang lolos gate**, bukan dari ujian.
- **Proficient di semua E = TA Ready.** Exemplary = jalur Research/Publication Ready.
- Integritas bukan komponen nilai; ia **syarat** nilai.
- Revisi diperbolehkan dan normal; keterlambatan tercatat di Execution.
- Hasil negatif yang dilaporkan jujur dinilai sama dengan hasil positif; klaim yang melebihi bukti diturunkan levelnya.
- Anchor samples (contoh Exemplary/Developing per E) untuk kalibrasi penilai disimpan di folder ini oleh dosen sebelum semester dimulai; contoh artefak terisi ada di [examples](../examples/README.md).
