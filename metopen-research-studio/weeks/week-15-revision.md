# Week 15 — Revision

> **Sprint** S15 · **Gate** G8 Contribution Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-14-peer-review.md) / [Week berikutnya →](week-16-defense.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Setiap komentar reviewer sudah dijawab, setiap butir checklist integritas punya bukti, dan kami siap defense."** Proposal direvisi sesuai tabel tanggapan menjadi **v0.9** tanpa menambah klaim di luar bukti; seluruh Research Pack disinkronkan dengan revisi; Research Integrity Checklist ([TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md)) diisi dan ditandatangani mahasiswa dan pembimbing; slide defense difinalkan dan dilatih dengan timer serta mock penguji ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W15; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S15). Aturan keras sprint ini: **defense tidak boleh dijadwalkan sebelum checklist integritas ditandatangani.**

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (response to reviewers: terima/ubah/tolak dengan alasan; disiplin revisi; anatomi checklist integritas; struktur defense 7–10 menit), **60 menit studio** (revisi bagian mayor, lalu latihan tanya-jawab dengan mock penguji dari tim lain), **10 menit gate check** (tiap tim menunjukkan satu butir checklist integritas beserta bukti yang mendukungnya). Beban 14 jam dengan satu task besar (OPS-131, revisi 5 jam) yang memblokir sinkronisasi dan checklist — mulai revisi pada hari pertama.

## Concept (30 menit)

- **Response to reviewers.** Untuk tiap komentar: kutip komentar, keputusan (terima / ubah sebagian / tolak), alasan, dan lokasi perubahan di naskah. Reviewer mengonfirmasi tanggapan memadai.
- **Disiplin revisi.** Revisi tidak boleh menambah klaim, sitasi, atau angka baru tanpa bukti; bila reviewer meminta eksperimen tambahan yang tidak mungkin dalam sisa waktu, tulis sebagai keterbatasan dan rencana TA.
- **Sinkronisasi Research Pack.** Angka dan klaim harus identik di One-Pager, `results/analysis.md`, proposal, dan slide — satu sumber, banyak tampilan.
- **Research Integrity Checklist.** Data (tanpa fabrikasi, provenance jelas), analisis (tanpa metric switching, leakage, cherry-picking seed), sitasi (semua dibaca dan terverifikasi), plagiarisme (similarity check), AI (log lengkap, statement, tanpa referensi/hasil buatan AI), etika/privasi, reproducibility, authorship, klaim tidak melebihi bukti, hasil negatif dilaporkan. Pass/fail — satu pelanggaran = gate gagal.
- **Amanah epistemik.** Menandatangani checklist adalah pernyataan kejujuran terhadap bukti, bukan formalitas ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md)).
- **Persiapan defense.** Struktur [TPL-13](../../research-os/08-templates/13-research-defense-template.md), 15 pertanyaan penguji yang wajib siap dijawab, rehearsal dengan timer minimal dua kali.

**Pertanyaan pemandu:** *Butir checklist integritas mana yang paling sulit Anda buktikan — dan apa artinya bagi klaim Anda?*

## Tasks

Semua task Sprint S15 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Revise proposal per reviewer table (UIAI-2026-001, OPS-131)`.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-130 | Ikuti sesi Revision & Defense Preparation | Latihan tanya jawab | 1.5h | Berperan sebagai penguji memberi pertanyaan latihan | Mahasiswa menjawab dengan merujuk artefak |
| OPS-131 | Revisi proposal/manuscript sesuai tabel tanggapan | Proposal v0.9 | 5h | Membantu memperbaiki kalimat; tidak menambah klaim atau sitasi | Reviewer mengonfirmasi tanggapan memadai |
| OPS-132 | Sinkronkan seluruh Research Pack dengan revisi | Research Pack tersinkron | 2h | Membantu mendeteksi inkonsistensi antar dokumen | Tim memeriksa angka dan klaim identik di semua dokumen |
| OPS-133 | Isi Research Integrity Checklist (TPL-11) dan tandatangani | docs/integrity-checklist.md tertandatangani | 1.5h | - | Dosen memverifikasi butir secara acak; satu pelanggaran = gate gagal |
| OPS-134 | Latihan defense (rehearsal) dengan timer dan mock penguji | Catatan rehearsal | 2h | Berperan sebagai penguji tambahan | Mentor/peer menilai kesiapan |
| OPS-135 | Finalkan slide defense dan lembar ringkas untuk penguji | presentation/defense-final.pdf | 1.5h | Membantu merapikan | Tim memeriksa konsistensi slide dengan proposal v0.9 |
| OPS-136 | Perbarui AI Usage Log dan jurnal mingguan W15 | AI Usage Log W15 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 14h** (jam tim; untuk tim 2 orang bagi dua). Urutan yang disarankan: OPS-131 (revisi) segera setelah sesi karena OPS-132 (sinkronisasi) dan OPS-133 (checklist) menunggunya; OPS-130 (latihan tanya-jawab) dan OPS-134 (rehearsal) dapat dijadwalkan paralel oleh anggota yang tidak sedang merevisi; OPS-135 (slide final) setelah rehearsal; OPS-136 (log/jurnal) di akhir ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules).

## Deliverable

| Artefak | Lokasi di repositori riset | Bukti |
|---|---|---|
| Proposal/manuscript v0.9 (revisi pasca peer review) | `paper/proposal.md` | commit; tabel tanggapan berstatus selesai dan dikonfirmasi reviewer |
| Research Pack tersinkron | semua komponen di `docs/research-pack.md` | commit; angka & klaim identik di semua dokumen |
| Research Integrity Checklist tertandatangani | `docs/integrity-checklist.md` ([TPL-11](../../research-os/08-templates/11-research-integrity-checklist.md)) | commit; tiap butir merujuk bukti; tanda tangan mahasiswa + pembimbing |
| Catatan rehearsal defense | `docs/reviews/defense-rehearsal.md` | commit; minimal 2 rehearsal dengan timer |
| Slide defense final + lembar ringkas penguji | `presentation/defense-final.pdf` | commit; konsisten dengan proposal v0.9 |
| AI Usage Log + jurnal | `docs/AI-USAGE.md`, `docs/journal/w15.md` | commit |

## AI Assist

Boleh (catat di [AI Usage Log — TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md), ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md)):

- Berperan sebagai penguji yang memberi pertanyaan latihan; jawaban tetap merujuk artefak tim (OPS-130, OPS-134).
- Memperbaiki kalimat saat revisi — tanpa menambah klaim atau sitasi (OPS-131).
- Mendeteksi inkonsistensi angka/istilah antar dokumen Research Pack (OPS-132).
- Merapikan slide dan lembar ringkas (OPS-135).
- Memeriksa bahasa dan konsistensi; diungkap di log.

Tidak boleh:

- Mengubah angka hasil pada tahap revisi tanpa menjalankan ulang eksperimen dan mencatatnya di log eksperimen.
- Menandatangani checklist integritas yang butirnya "diperiksa" AI, bukan oleh tim dengan bukti.
- Menyusun AI Usage Statement final tanpa mencocokkannya dengan log baris per baris.
- Menggunakan AI untuk menulis jawaban defense yang tidak Anda pahami — penguji akan menggali.

## Human Check

- **Reviewer (peer)**: mengonfirmasi tanggapan atas komentarnya memadai (OPS-131).
- **Tim**: angka dan klaim identik di semua dokumen (OPS-132); slide konsisten dengan proposal v0.9 (OPS-135).
- **Dosen**: memverifikasi butir checklist secara acak terhadap repositori (bukan hanya tanda tangan); satu pelanggaran = gate gagal (OPS-133).
- **Mentor/peer**: menilai kesiapan pada rehearsal (OPS-134); mahasiswa menjawab dengan merujuk artefak (OPS-130).
- **Setiap anggota**: entri AI Usage Log miliknya sendiri (OPS-136).

## Done When

Minggu ini belum menutup gate; G8 Contribution Ready ditutup di [Week 16](week-16-defense.md). Sprint selesai bila:

- [ ] Proposal v0.9: setiap baris `paper/response-to-reviewers.md` berstatus selesai dengan lokasi perubahan, dan reviewer mengonfirmasi.
- [ ] Research Pack tersinkron: tidak ada angka/klaim yang berbeda antara One-Pager v2, `results/analysis.md`, proposal, dan slide.
- [ ] `docs/integrity-checklist.md` terisi penuh, setiap butir merujuk bukti, ditandatangani mahasiswa dan pembimbing.
- [ ] Rehearsal defense minimal 2 kali dengan timer dan mock penguji; catatan di `docs/reviews/defense-rehearsal.md`.
- [ ] `presentation/defense-final.pdf` dan lembar ringkas penguji siap.
- [ ] Jadwal defense ditetapkan **hanya setelah** checklist integritas ditandatangani.
- [ ] AI Usage Log dan `docs/journal/w15.md` diperbarui oleh setiap anggota.

## Templates & rujukan

- Template: [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md), [TPL-12 Peer Review — response letter](../../research-os/08-templates/12-peer-review-template.md), [TPL-13 Research Defense](../../research-os/08-templates/13-research-defense-template.md), [TPL-14 Research Handoff](../../research-os/08-templates/14-research-handoff-template.md) (mulai disiapkan), [TPL-10 AI Usage Log](../../research-os/08-templates/10-ai-usage-log-template.md).
- Konsep: [MET-03 §W15](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md), [MET-04 Research Pack §5](../../research-os/04-metopen-research-studio/04-research-pack-specification.md), [MET-06 Rubrik 5E & Integrity Gate](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md), [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md), [AIX-02 AI Governor](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md), [OPS-02 §S15](../../research-os/06-execution-os/02-weekly-sprints.md), [CODE OF CONDUCT §4](../../CODE_OF_CONDUCT.md).
- Studio: [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrik 5E](../rubrics/README.md) · [Templates](../templates/README.md) · [Beranda studio](../README.md).

## Jebakan minggu ini

1. **Menutupi hasil negatif saat revisi.** Reviewer mempertanyakan hasil yang lemah, lalu tim "menghilangkannya". Hasil lemah tetap dilaporkan; yang direvisi adalah klaimnya.
2. **Menandatangani checklist tanpa bukti.** Setiap butir harus menunjuk file/commit; dosen memeriksa secara acak dan satu pelanggaran menggagalkan gate.
3. **AI Usage Statement tidak lengkap.** Statement yang lebih "bersih" daripada log adalah pelanggaran disclosure; cocokkan baris per baris.
4. **Revisi yang menambah klaim.** Menjawab reviewer dengan klaim baru tanpa bukti baru. Jawab dengan keterbatasan dan rencana TA.
5. **Rehearsal hanya sekali, tanpa timer.** Defense 7–10 menit yang molor memotong sesi tanya-jawab — bagian yang justru dinilai.
