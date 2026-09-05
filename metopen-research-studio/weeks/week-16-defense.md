# Week 16 — Defense

> **Sprint** S16 · **Gate** G8 Contribution Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-15-revision.md) / Setelah semester: [Handoff (TPL-14)](../../research-os/08-templates/14-research-handoff-template.md) · [Tugas Akhir](../../research-based-learning/courses/final-project/README.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Research Pack lengkap; TA/paper dapat dimulai dari sini."** Riset dipertanggungjawabkan secara oral dalam **Research Defense 7–10 menit** plus tanya-jawab di hadapan dosen, mentor, dan penguji; revisi pasca-defense dikerjakan; AI Usage Statement difinalkan; handoff ke TA/mentor/AI Center diisi ([TPL-14](../../research-os/08-templates/14-research-handoff-template.md)); registry (Issue, kartu dataset, publikasi bila ada) dan metadata repositori dilengkapi; PR `GATE REVIEW: Contribution Ready` **di-merge**; release **v1.0 Research Pack** dibuat; dan tim menulis refleksi akhir semester serta rencana semester VIII ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W16; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S16). Merge PR G8 berarti **G8 lulus**; status kematangan ditetapkan: TA Ready, Research Ready, atau Publication Ready.

Sesi 100 menit minggu ini adalah sesi defense: **10 menit pembukaan** (aturan, urutan, rubrik), lalu **tiap tim 7–10 menit presentasi + 10 menit tanya-jawab** (dinilai dengan [Rubrik 5E](../rubrics/README.md) dan rubrik defense [TPL-13](../../research-os/08-templates/13-research-defense-template.md)), ditutup **10 menit** pengumuman catatan wajib. Defense hanya boleh berlangsung bila checklist integritas sudah ditandatangani di Week 15 (OPS-137 bergantung pada OPS-133).

## Concept (30 menit)

- **Struktur defense** ([TPL-13](../../research-os/08-templates/13-research-defense-template.md)): masalah & why (1 menit) → apa yang diketahui & gap (1.5) → RQ & kontribusi (1) → desain (2) → bukti pilot/utama (2) → threats & etika (1) → rencana TA/handoff (0.5).
- **Menjawab dengan bukti.** Setiap jawaban menunjuk tabel, figur, atau file di repositori; "menurut kami" tanpa bukti bukan jawaban.
- **Mengakui batas tanpa diminta.** Threats v2 dan limitations disampaikan sendiri; penguji menghargai kejujuran lebih daripada kesan sempurna.
- **Handoff.** *What exists* (artefak + lokasi + status gate), *missing evidence*, *next steps*, *owner* — agar dosen pembimbing TA dapat memulai tanpa mengulang dari nol.
- **Release v1.0** adalah snapshot Research Pack yang lengkap dan dapat disitasi (CITATION.cff, lisensi per komponen sesuai [LICENSING](../../LICENSING.md)).
- **Refleksi.** Apa yang berubah dari "saya membuat sesuatu" menjadi "saya punya bukti untuk klaim saya"; rencana semester VIII.

**Pertanyaan pemandu:** *Jika penguji hanya boleh membuka satu file di repositori Anda untuk menguji klaim utama, file mana yang Anda tunjuk?*

## Tasks

Semua task Sprint S16 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add research handoff to TA supervisor (UIAI-2026-001, OPS-140)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-137 | Presentasikan Research Defense (7-10 menit) dan tanya jawab | Defense terlaksana | 2h | - | Penguji menilai dengan 5E Rubric; integrity checklist wajib sudah ditandatangani sebelum defense |
| OPS-138 | Lakukan revisi pasca-defense | Proposal final | 3h | Membantu memperbaiki kalimat; tidak menambah klaim | Dosen mengonfirmasi catatan wajib terpenuhi |
| OPS-139 | Finalkan AI Usage Statement dan AI-USAGE.md | AI Usage Statement final | 1h | - | Dosen membandingkan statement dan log |
| OPS-140 | Isi Research Handoff (TPL-14) ke TA/mentor/AI Center | docs/handoff.md | 1.5h | Membantu merangkum artefak; isi diverifikasi tim | Mentor mengonfirmasi handoff cukup untuk memulai bimbingan TA |
| OPS-141 | Perbarui registry: Issue, dataset card, dan publikasi bila ada | Registry diperbarui | 1h | - | Pengelola registry memeriksa entri |
| OPS-142 | Lengkapi CITATION.cff, LICENSE, CHANGELOG, dan README riset | Metadata repo lengkap | 1h | Membantu format CITATION.cff | Tim memeriksa lisensi sesuai kebijakan |
| OPS-143 | Merge PR GATE REVIEW: Contribution Ready | PR G8 termerge | 1h | - | Dosen pengampu menyetujui merge = gate lulus |
| OPS-144 | Buat release v1.0 Research Pack | Release v1.0 | 1h | - | Dosen memeriksa release memuat semua komponen |
| OPS-145 | Tulis refleksi akhir semester dan rencana semester VIII | Refleksi akhir | 1h | - | Dosen membaca dan memberi umpan balik akhir |

**Total effort: 12.5h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: OPS-137 (defense) membuka semua task lain; OPS-138 (revisi pasca-defense) segera setelahnya, lalu OPS-139, OPS-140, OPS-141, dan OPS-142 dapat paralel; OPS-143 (merge PR G8) hanya setelah checklist, defense, statement final, handoff, dan metadata lengkap; OPS-144 (release v1.0) setelah merge; OPS-145 (refleksi) menutup semester ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules).

## Deliverable

| Artefak | Lokasi di repositori riset | Bukti |
|---|---|---|
| Defense terlaksana + notulen | `docs/reviews/defense-minutes.md` | notulen: pertanyaan, jawaban, catatan wajib penguji |
| Proposal final (revisi pasca-defense) | `paper/proposal.md`, `paper/proposal-v1.0.pdf` | commit; catatan wajib penguji terpenuhi |
| AI Usage Statement final | `paper/AI-USAGE-STATEMENT.md`, log lengkap di `docs/AI-USAGE.md` | commit; dosen membandingkan statement dan log |
| Research Handoff | `docs/handoff.md` ([TPL-14](../../research-os/08-templates/14-research-handoff-template.md)) | commit; konfirmasi penerimaan dari mentor/pembimbing TA |
| Registry diperbarui | Issue riset (label `gate:G8-contribution`), [datasets-registry](../../datasets-registry/README.md), [publications](../../publications/README.md) bila ada | pengelola registry memeriksa entri |
| Metadata repositori | `CITATION.cff`, `LICENSE`, `LICENSE-DOCS`, `CHANGELOG.md`, README riset (Research Status, Current Research Gate) | commit |
| PR Gate Review G8 | PR `GATE REVIEW: Contribution Ready` **termerge** | URL PR; label diperbarui |
| Release | `v1.0 Research Pack` | halaman release memuat semua komponen [MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) |
| Refleksi akhir + rencana semester VIII | `docs/journal/w16-reflection.md` | commit; umpan balik dosen |

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Latihan tanya-jawab sebelum defense (dari Week 15).
- Memperbaiki kalimat pada revisi pasca-defense — tanpa menambah klaim (OPS-138).
- Membantu merangkum artefak untuk handoff; isi diverifikasi tim (OPS-140).
- Membantu format `CITATION.cff` (OPS-142).
- Membantu menyusun kerangka refleksi; isi pengalaman dari tim.

Tidak boleh:

- Menampilkan di defense hasil, figur, atau angka yang tidak ada di repositori.
- Membiarkan AI menjawab pertanyaan penguji secara langsung (perangkat AI tidak dipakai selama defense).
- Menulis AI Usage Statement final yang berbeda dari log.
- Mengisi handoff dengan klaim status gate yang belum benar-benar dilewati.

## Human Check

- **Penguji**: menilai dengan Rubrik 5E; checklist integritas wajib sudah ditandatangani sebelum defense (OPS-137).
- **Dosen**: catatan wajib pasca-defense terpenuhi (OPS-138); statement dan log dibandingkan (OPS-139); merge PR G8 = gate lulus (OPS-143); release memuat semua komponen (OPS-144); umpan balik refleksi (OPS-145).
- **Mentor**: handoff cukup untuk memulai bimbingan TA (OPS-140).
- **Pengelola registry**: entri Issue/dataset/publikasi diperiksa (OPS-141).
- **Tim**: lisensi per komponen sesuai kebijakan (OPS-142).

## Done When

Minggu ini **menutup G8 Contribution Ready** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G8) — gate terakhir Metopen.

- [ ] Defense 7–10 menit + tanya-jawab terlaksana; notulen di `docs/reviews/defense-minutes.md`.
- [ ] Revisi pasca-defense selesai; catatan wajib penguji terpenuhi dan dikonfirmasi dosen.
- [ ] AI Usage Statement final konsisten dengan log; Research Integrity Checklist tetap berlaku (tidak ada perubahan yang melanggarnya).
- [ ] `docs/handoff.md` terisi (what exists, missing evidence, next steps, owner) dan diterima mentor/pembimbing TA.
- [ ] Registry diperbarui: Issue berlabel `gate:G8-contribution`, kartu dataset dan entri publikasi/artefak bila ada; Mission Control diperbarui (Maturity: TA Ready / Research Ready / Publication Ready).
- [ ] `CITATION.cff`, lisensi per komponen, `CHANGELOG.md`, dan README riset lengkap.
- [ ] PR `GATE REVIEW: Contribution Ready` (template [manuscript-review.md](../../.github/PULL_REQUEST_TEMPLATE/manuscript-review.md), branch `research/g8-contribution`) **di-merge** oleh dosen pengampu.
- [ ] Release `v1.0 Research Pack` dibuat dan memuat seluruh komponen MET-04.
- [ ] `docs/journal/w16-reflection.md` ditulis; rencana semester VIII disepakati dengan calon pembimbing TA.

**Lulus jika** dosen pembimbing TA dapat memulai bimbingan dari Research Pack tanpa mengulang dari nol. **Gagal jika** ada komponen Research Pack yang kosong atau integritas tidak lolos. Gagal berarti revisi terjadwal dan review ulang, bukan akhir ([CONTRIBUTING](../../CONTRIBUTING.md) §3).

## Templates & rujukan

- Template: [TPL-13 Research Defense](../../research-os/08-templates/13-research-defense-template.md), [TPL-14 Research Handoff](../../research-os/08-templates/14-research-handoff-template.md), [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md), [TPL-15 Research Repository](../../research-os/08-templates/15-research-repository-template.md) (README riset & lisensi per komponen), [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md), [PR manuscript-review](../../.github/PULL_REQUEST_TEMPLATE/manuscript-review.md).
- Konsep: [MET-03 §W16](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md), [MET-05 Publication Backward Design](../../research-os/04-metopen-research-studio/05-publication-backward-design.md) (jalur setelah Metopen), [MET-06 Rubrik 5E](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md), [ARC-04 Build → Prove → Contribute](../../research-os/02-academic-architecture/04-build-prove-contribute.md) (handoff ke TA), [OPS-02 §S16](../../research-os/06-execution-os/02-weekly-sprints.md), [LICENSING](../../LICENSING.md), [GOVERNANCE §6.3 release](../../GOVERNANCE.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).
- Setelah semester: [Tugas Akhir — research-based-learning](../../research-based-learning/courses/final-project/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Pitch yang "menjual", bukan mempertanggungjawabkan.** Defense bukan presentasi produk; penguji menilai bukti, batas klaim, dan kejujuran, bukan antusiasme.
2. **Klaim melebihi bukti di panggung.** Di bawah tekanan, klaim sering membesar. Bawa tabel CER; jawab dari sana.
3. **Handoff kosong atau terlalu optimistis.** "Semua sudah selesai" tidak membantu pembimbing TA. Tulis *missing evidence* sejujur threats v2.
4. **Merge PR G8 sebelum syaratnya lengkap.** OPS-143 menunggu checklist, defense, statement final, handoff, dan metadata; merge dini membuat release v1.0 tidak lengkap.
5. **Melewatkan refleksi.** Refleksi dan rencana semester VIII adalah jembatan ke TA — tanpa itu, semester VIII dimulai dari mencari-cari lagi.
