# Week 08 — Design Defense

> **Sprint** S8 · **Gate** G5 Method Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-07-method.md) / [Week berikutnya →](week-09-repository.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Kami menjawabnya dengan ___, data ___, baseline ___, metrik ___, ancaman ___."** — dan kalimat itu sudah diserang red team, lalu bertahan atau direvisi dengan alasan tertulis. Desain riset dari W7 dipertahankan pada **Mid-semester Research Pitch** (7–10 menit) di depan dosen pengampu, mentor, dan red team (peer dari tim lain + dosen lain); setiap serangan dicatat di notulen, diklasifikasi *ubah desain / tambah kontrol / tolak dengan alasan*, dan dokumen desain direvisi. Ethics & Privacy plan dan Experiment Card pilot — dengan *expected result* yang ditulis **sebelum** eksperimen — melengkapi bukti G5 ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W8; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S8). Semua bukti masuk PR `GATE REVIEW: Method Ready`; merge berarti status **TA Ready** dan release `v0.3 Research Design`. Tim juga menjadi red team bagi tim lain: mencari cara desain mereka gagal adalah latihan terbaik untuk menemukan lubang di desain sendiri.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (measurement & evaluation, cara mem-pitch desain, red team thinking), **60 menit studio** (pitch tim + tanya jawab red team terstruktur — jadwal urutan pitch ditentukan dosen; tim yang belum giliran mengerjakan ethics plan dan Experiment Card), **10 menit gate check** (tiap tim menyebut satu serangan yang paling mengubah desainnya). Sprint ini punya slack terbesar dalam semester (15 jam), tetapi jadwal pitch tidak bisa digeser — slack itu buffer untuk mengejar ketertinggalan S3–S7, bukan untuk istirahat ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer).

## Concept (30 menit)

1. **Struktur pitch desain 7–10 menit:** masalah → gap → RQ → desain → bukti yang diharapkan → ancaman. Mengikuti slide 1–4 dan 6 [TPL-13](../../research-os/08-templates/13-research-defense-template.md); slide 5 berisi *rencana* pilot (Experiment Card), bukan hasil. Maksimal 10 slide (+ maksimal 3 slide cadangan untuk tanya-jawab), setiap angka dan klaim menunjuk artefak di repositori ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.16).
2. **Red team thinking:** tugas penonton adalah mencari cara riset ini gagal menjawab RQ. Lima sudut serangan wajib: validitas (4 jenis), leakage, keadilan baseline, data/representativitas, etika. Serangan yang baik spesifik ("split per mahasiswa atau per semester?"), bukan generik ("tambah data").
3. **Menerima kritik adalah sains normal.** Amanah epistemik: menolak kritik red team tanpa alasan adalah pelanggaran integritas ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.9). Tiga respons yang sah untuk setiap serangan: *ubah desain*, *tambah kontrol*, atau *tolak dengan alasan tertulis* — dan ketiganya tercatat.
4. **Measurement & evaluation:** metrik dipilih karena selaras dengan RQ, bukan karena angkanya bagus; baseline harus adil (tuning setara, data identik); error analysis dan *statistical thinking* secukupnya untuk membaca tabel hasil dan menemukan klaim yang tidak didukung — latihan OPS-069 ([MET-06](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3 E3).
5. **Expected result ditulis sebelum eksperimen.** Experiment Card ([TPL-09](../../research-os/08-templates/09-experiment-card.md)) adalah pra-registrasi ringan: hipotesis, baseline, metrik, ambang praktis, *stopping rule*, seed/config, peer reproducer. Bagian pra-registrasi tidak diubah setelah run; bila harus berubah, buat kartu baru dan catat alasannya.
6. **Blocking rule B5:** pilot (OPS-088, W10) tidak boleh dijalankan sebelum PR G5 termerge, dan metrik/baseline harus terkunci dengan tanggal commit sebelum W9 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules). Metrik yang dipilih setelah melihat hasil = mengubah metrik setelah melihat hasil.
7. **Ethics & privacy awal:** jenis data, risiko privasi, persetujuan, anonimisasi, bias, dampak pada stakeholder, kebutuhan izin/komite etik bila ada subjek manusia; nilai privasi kartu dataset (Public/Restricted/Confidential) wajib terisi sebelum G5 ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.5, §4; [SECURITY.md](../../SECURITY.md)).
8. **Kriteria lulus G5:** orang lain dapat menjalankan desain ini tanpa bertanya ke tim. Reviewer mengujinya dengan menjelaskan prosedur eksperimen hanya dari dokumen, lalu menulis bagian mana yang masih harus ditanyakan ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G5; [template PR method-review](../../.github/PULL_REQUEST_TEMPLATE/method-review.md)).
9. **AI sebagai red team sebelum manusia.** Target level minggu ini: *AI Investigator pada Method* — bukti: notulen red team dan log kritik desain, termasuk kritik yang ditolak; self-assessment AI competency kedua dilakukan minggu ini ([AIX-02](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md) §5).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membuka catatan: *"Serangan red team mana yang paling mungkin membuat desain kami gagal menjawab RQ — dan apa yang kami ubah karenanya, atau mengapa kami menolaknya?"*

## Tasks

Semua task Sprint S8 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add pilot experiment card with expected result (OPS-071)`. Task W7 yang belum selesai — terutama OPS-063 (dataset card), OPS-064/065 (baseline & metrik), OPS-067 (Threats v1) — ditulis di atas tabel ini pada salinan tim; PR G5 (OPS-076) tidak dapat dibuka sebelum semuanya ada.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-069 | Ikuti sesi Measurement & Evaluation dan persiapan red team | Latihan evaluasi | 2h | Membuat tabel hasil sintetis untuk latihan (ditandai sebagai latihan) | Mahasiswa menemukan klaim tak didukung secara mandiri |
| OPS-070 | Tulis Ethics & Privacy plan (docs/ethics.md) | docs/ethics.md | 2h | Membantu menyusun checklist risiko; penilaian oleh tim | Dosen memeriksa tidak ada data pribadi yang masuk repo |
| OPS-071 | Isi Experiment Card untuk pilot (TPL-09) | experiments/pilot-01/experiment-card.md + Issue | 1.5h | Mengkritik kelengkapan card | Mentor memeriksa expected result ditulis sebelum eksperimen |
| OPS-072 | Susun slide Mid-semester Research Pitch (7-10 menit) | presentation/midterm-pitch.pdf | 3h | Membantu merapikan alur slide; klaim dan angka dari dokumen tim | Tim memastikan tiap slide bersumber dari artefak repo |
| OPS-073 | Lakukan Red Team Review terhadap desain tim lain | Red team memo untuk tim lain | 2h | Mengusulkan sudut serangan tambahan; tim memilih yang relevan | Dosen memeriksa serangan spesifik, bukan generik |
| OPS-074 | Presentasikan pitch dan terima Red Team Review | Notulen red team | 2h | - | Dosen memverifikasi notulen memuat semua serangan penting |
| OPS-075 | Revisi Research Design berdasarkan red team | Desain revisi | 2h | Membantu menilai konsekuensi tiap perubahan | Mentor memeriksa revisi menjawab serangan valid |
| OPS-076 | Siapkan PR GATE REVIEW: Method Ready (method-review.md) | PR GATE REVIEW: Method Ready | 1.5h | - | Reviewer memeriksa metrik dan baseline sudah ditetapkan sebelum eksperimen |
| OPS-077 | Perbarui AI Usage Log dan jurnal mingguan W8 | AI Usage Log W8 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 16.5h** (jam tim; untuk tim 2 orang bagi dua). Jalur kritis hanya 1.5 jam (PR G5), slack 15 jam — tetapi rantai pitch → revisi → PR bergantung pada jadwal pitch yang ditetapkan dosen ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai tiga task yang saling independen — **OPS-069** di sesi studio, **OPS-070** ethics plan (butuh data plan OPS-062) dan **OPS-071** Experiment Card (butuh baseline OPS-064, metrik OPS-065, design card OPS-066) — dibagi ke anggota berbeda → **OPS-072** slide (butuh 066 + 071) dan **OPS-073** red team untuk tim lain (butuh 069) berjalan paralel → **OPS-074** pitch resmi pada jadwal dosen (butuh 072 + 073) → **OPS-075** revisi desain pada hari yang sama atau esoknya (butuh 074) → **OPS-076** PR G5 setelah 063, 067, 070, 075 ada; **OPS-077** log dan jurnal berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g5-method`, harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| Latihan evaluasi: tabel hasil contoh (bertanda *sintetis/latihan*) + klaim yang tidak didukung beserta alasannya; jurnal W8: **serangan mana yang paling mengubah desain**; entri refleksi self-assessment AI competency #2 | `docs/journal/w08.md` | commit | OPS-069, OPS-077 |
| **Ethics & Privacy plan**: jenis data, risiko privasi + mitigasi, persetujuan/consent, anonimisasi, bias, dampak pada stakeholder, kebutuhan izin/komite etik bila ada subjek manusia (`[isi]` prosedur Prodi), batasan penggunaan AI terhadap data ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.12) | `docs/ethics.md` (ditautkan dari README riset; tidak perlu file `ETHICS.md` terpisah) | commit; risiko privasi dan mitigasi tercantum | OPS-070 |
| **Experiment Card pilot** (judul kartu `EXP-01` sesuai [TPL-09](../../research-os/08-templates/09-experiment-card.md)): seluruh bagian pra-registrasi terisi — RQ, hipotesis + null, baseline, variabel, dataset + split + leakage prevention, metrik + ambang praktis, kontrol, **expected result**, threats, seed/config/env, compute budget, stopping rule, peer reproducer; bagian hasil aktual kosong bertanda "diisi W10" | `experiments/pilot-01/experiment-card.md`; dirujuk dari `experiments/README.md` | commit; Issue `type:experiment` dari form [Experiment](../../.github/ISSUE_TEMPLATE/04-experiment.yml) tertaut ke Research ID | OPS-071 |
| **Slide Mid-semester Research Pitch**: ≤10 slide (+ maksimal 3 slide cadangan) struktur [TPL-13](../../research-os/08-templates/13-research-defense-template.md) (slide 5 = rencana pilot), durasi 7–10 menit, satu slide "pertanyaan yang ingin kami dengar dari red team"; Research ID + gate di slide 1 | `presentation/midterm-pitch.pdf` (+ berkas sumber slide) | commit; durasi latihan dengan timer tercatat di jurnal | OPS-072 |
| **Red team memo untuk tim lain**: minimal 5 serangan (validitas, leakage, baseline, data, etika) masing-masing dengan saran perbaikan, format [TPL-12](../../research-os/08-templates/12-peer-review-template.md) peran *red team* | repo tim lain: Issue atau PR comment; tautannya dicatat di `docs/journal/w08.md` | file review terkirim (URL) | OPS-073 |
| **Notulen red team**: tabel per serangan/pertanyaan — penanya, isi, klasifikasi (*ubah desain / tambah kontrol / tolak + alasan*), tindak lanjut, owner, status | `docs/reviews/midterm-red-team.md` | commit; tabel tindak lanjut berstatus selesai setelah OPS-075 | OPS-074, OPS-075 |
| **Desain revisi**: `docs/research-design.md`, design card ([TPL-08](../../research-os/08-templates/08-research-design-card.md)), Threats to Validity v1 (direvisi), `docs/data-plan.md`, Experiment Card diperbarui sesuai serangan yang diterima; perubahan dicatat di `CHANGELOG.md` bagian `v0.3 Research Design` | `docs/`, `experiments/pilot-01/`, `CHANGELOG.md` | commit revisi (riwayat terlihat di log commit) | OPS-075 |
| **PR `GATE REVIEW: Method Ready — UIAI-YYYY-NNN`** dari `research/g5-method` memakai [template method-review](../../.github/PULL_REQUEST_TEMPLATE/method-review.md); setelah merge: label `gate:G5-method`, `maturity:ta-ready`, release **`v0.3 Research Design`** | PR; GitHub Release | URL PR; release v0.3; README §Current Research Gate | OPS-076 |
| AI Usage Log W8 Stage `Method`: tabel latihan sintetis, checklist risiko etika, kritik Experiment Card, alur slide, sudut serangan red team, latihan pitch adversarial, penilaian konsekuensi revisi — dan keputusan manusia atas tiap output, termasuk kritik yang **ditolak** | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)) | commit | OPS-077 |

Release `v0.3 Research Design` memuat artefak Research Pack 5–9, 11 (v1), dan 12 (awal) ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §7). Setelah PR termerge, README riset: `Current Research Gate: G5 (passed) → G6 (in progress)`, dan Issue **Experiment** untuk pilot dibuka bila belum ada.

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan**, Stage `Method`. Minggu ini AI paling berguna sebagai **penyerang** desain Anda sendiri sebelum manusia menyerangnya ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.5 Challenge; [AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.7 Method).

**Boleh minggu ini**

- Meminta AI membuat tabel hasil eksperimen **sintetis** untuk latihan menemukan klaim tak didukung (OPS-069); tabel ditandai jelas sebagai latihan dan tidak pernah masuk `results/`.
- Meminta AI membantu menyusun checklist risiko privasi/etika untuk jenis data Anda (OPS-070); penilaian risiko, mitigasi, dan keputusan consent dibuat tim; prompt hanya memuat metadata, bukan data.
- Meminta AI mengkritik kelengkapan Experiment Card — "field mana yang masih kabur atau tidak bisa dijalankan orang lain?" (OPS-071); *expected result* dan ambang praktis ditulis tim.
- Meminta AI merapikan alur dan narasi slide pitch (OPS-072); setiap klaim dan angka disalin dari dokumen tim, bukan dari AI.
- Meminta AI mengusulkan sudut serangan tambahan untuk jenis metode/data tim lain (OPS-073); tim memilih yang relevan dan menuliskannya spesifik. Jangan menempelkan dokumen tim lain ke layanan AI eksternal tanpa izin mereka.
- Latihan pitch dengan AI sebagai penanya adversarial memakai 15 pertanyaan penguji [TPL-13](../../research-os/08-templates/13-research-defense-template.md) ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W8) — jawab dengan menunjuk artefak, bukan dengan mengarang hasil.
- Meminta AI membantu menilai konsekuensi tiap perubahan desain (OPS-075) — "jika kontrol X ditambah, apa yang berubah pada data, waktu, dan threats?"; keputusan terima/tolak tetap milik tim dan dicatat.

**Tidak boleh**

- Menjawab pertanyaan red team dengan hasil yang belum ada atau hanya ada di percakapan AI ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W8; [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3). Jawaban jujur: "belum diuji; itu tujuan pilot W10."
- Membiarkan AI memilih atau mengganti metrik, baseline, hipotesis, atau *expected result* — apalagi setelah red team menunjukkan hasil yang mungkin buruk; itu metric switching/HARKing dan melanggar blocking rule B5.
- Memasukkan data mentah, data pribadi mahasiswa/pasien/pengguna, atau dokumen partner ke layanan AI saat menyusun ethics plan atau Experiment Card ([SECURITY.md](../../SECURITY.md)).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-074 (notulen ditulis manusia saat sesi), OPS-076 (PR gate), OPS-077 (log & jurnal).
- Menerima seluruh "red team AI" tanpa entri yang **ditolak** — entri ditolak beserta alasannya adalah bukti Anda menilai, bukan menyalin ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.5).

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Mahasiswa menemukan klaim tak didukung pada tabel latihan secara mandiri dan menjelaskan mengapa (baseline tidak ada, metrik tidak selaras, variansi tidak dilaporkan) | diri sendiri, dicek dosen di sesi studio | OPS-069 |
| Tidak ada data pribadi/sensitif yang masuk repositori (termasuk riwayat git dan slide); risiko privasi punya mitigasi; nilai privasi kartu dataset terisi | dosen pengampu | OPS-070 |
| *Expected result* dan ambang praktis tertulis **sebelum** eksperimen; baseline dan metrik identik dengan yang dikunci W7; peer reproducer ditunjuk | mentor | OPS-071 |
| Tiap slide bersumber dari artefak repositori (path/Issue disebut di catatan slide); tidak ada angka tanpa sumber; durasi latihan 7–10 menit | tim (anggota yang tidak membuat slide memeriksa) | OPS-072 |
| Serangan ke tim lain spesifik pada desain mereka, bukan generik; tiap serangan punya saran perbaikan | dosen pengampu | OPS-073 |
| Notulen memuat semua serangan dan pertanyaan penting, ditulis tanpa defensif; tiap item punya tindak lanjut dan owner | dosen pengampu; peer red team mengonfirmasi item mereka tercatat | OPS-074 |
| Revisi benar-benar menjawab serangan yang valid; serangan yang ditolak punya alasan tertulis; perubahan metrik/baseline (bila ada) tercatat dengan tanggal dan alasan | mentor | OPS-075 |
| Metrik dan baseline sudah ditetapkan sebelum eksperimen; orang lain dapat menjalankan desain tanpa bertanya ke tim; definition of done G5 lengkap; integritas: tidak ada data sensitif di commit, AI tercatat | dosen pengampu + mentor + red team (reviewer PR) | OPS-076 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya, termasuk kritik AI yang ditolak dan alasannya; self-assessment #2 dibahas singkat dengan mentor | diri sendiri; mentor | OPS-077 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W8, "dapat dibuka reviewer" berarti reviewer membaca `docs/research-design.md` + Experiment Card dan mampu menceritakan ulang prosedur eksperimen langkah demi langkah tanpa bertanya ke tim.

## Done When

Minggu ini **menutup gate G5 Method Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] PR `GATE REVIEW: Question Ready` (G4) sudah termerge dan semua task W7 pada critical path (OPS-063, 064, 065, 066, 067) selesai — G5 tidak dapat dibuka sebelum G4 lulus.
- [ ] `docs/journal/w08.md` berisi latihan evaluasi (klaim tak didukung + alasan), refleksi "serangan mana yang paling mengubah desain", dan entri self-assessment AI competency #2.
- [ ] `docs/ethics.md` terisi (jenis data, risiko + mitigasi, consent, anonimisasi, bias, dampak, kebutuhan izin); README riset menunjuk ke sana; nilai privasi kartu dataset terisi; tidak ada data pribadi di repo.
- [ ] `experiments/pilot-01/experiment-card.md` lengkap tanpa field kosong di bagian pra-registrasi; *expected result* dan stopping rule tertulis; Issue `type:experiment` tertaut; commit kartu bertanggal sebelum satu pun run eksperimen.
- [ ] `presentation/midterm-pitch.pdf` ≤10 slide sesuai TPL-13; setiap angka/klaim bersumber dari artefak repo; sudah dilatih minimal 1 kali dengan timer dan durasinya tercatat.
- [ ] Red team memo (≥5 serangan spesifik + saran) terkirim ke repo tim lain; tautannya ada di jurnal.
- [ ] Pitch resmi dilakukan; `docs/reviews/midterm-red-team.md` memuat **setiap** serangan dengan status *ubah desain / tambah kontrol / tolak + alasan*, tindak lanjut, dan owner — tidak ada item tanpa status.
- [ ] Desain direvisi: design card, Threats to Validity v1 (direvisi), data plan, Experiment Card diperbarui; tabel tindak lanjut berstatus selesai; `CHANGELOG.md` mencatat perubahan v0.3; metrik dan baseline final **terkunci dengan tanggal commit**.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Method` untuk setiap penggunaan material, termasuk minimal satu kritik AI yang ditolak dengan alasan; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui.
- [ ] Di gate check, tim menyebut satu serangan yang paling mengubah desain dan menunjukkan baris notulen serta commit revisinya.
- [ ] PR **`GATE REVIEW: Method Ready`** termerge oleh dosen pengampu + mentor + red team; label `gate:G5-method` dan `maturity:ta-ready`; release `v0.3 Research Design` dibuat; README §Current Research Gate diperbarui.

**Ringkasan gate G5** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G5). **Lulus jika** orang lain dapat menjalankan desain ini tanpa bertanya ke tim. **Gagal jika** metrik/baseline belum ditetapkan — eksperimen tidak boleh dimulai sebelum keduanya ada — atau bila ada pelanggaran integritas (data sensitif di commit, metrik diganti setelah melihat hasil, penggunaan AI tidak diungkap), terlepas dari kualitas lainnya. Reviewer: dosen pengampu, mentor, red team (peer + dosen lain). Lolos G5 = status **TA Ready**: mahasiswa masuk semester VIII tanpa lagi mencari judul dan metode ([MST-03](../../research-os/00-master/03-glossary.md) §3.2). Gagal gate bukan hukuman: reviewer menulis apa yang kurang dan bukti apa yang dibutuhkan, tim merevisi, review dibuka ulang. Bila G5 terlambat: kunci baseline trivial dan metrik utama dulu (cukup untuk memulai environment dan data pipeline W9), red team dilakukan asinkron via PR comment, dan PR G5 tetap merge **sebelum** pilot OPS-088 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat).

**Cara membuka PR gate** ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3): (1) pastikan semua bukti di tabel Deliverable ada di branch `research/g5-method`; (2) buka PR berjudul `GATE REVIEW: Method Ready — UIAI-YYYY-NNN` dengan `?template=method-review.md` atau salin isi [template method-review](../../.github/PULL_REQUEST_TEMPLATE/method-review.md); (3) isi seluruh bagian: RQ (dengan rujukan baris matriks), Method (design card), Dataset (Dataset ID, lisensi, privasi, fallback), Baseline, Metrics (prosedur anti-leakage + ambang praktis), Experiment Card, Threats, Ethics & Privacy, bagian *Mid-semester Research Pitch / Red Team Review* (link slide, notulen, perubahan desain), tabel Evidence, dan AI Usage dengan tautan log; (4) tautkan nomor PR G4 dan Issue `type:research-question` serta `type:experiment`; (5) minta review dosen pengampu + mentor + red team, dan minta reviewer menuliskan pertanyaan yang "masih harus ditanyakan ke tim" — jawab dengan memperbaiki dokumen, bukan hanya membalas komentar; (6) setelah merge: label → `gate:G5-method`, maturity → `maturity:ta-ready`, field Mission Control dan README diperbarui, release `v0.3 Research Design`, Issue Experiment untuk pilot dibuka. Komentar review disimpan, tidak dihapus.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) — `experiments/pilot-01/experiment-card.md`; bagian pra-registrasi diisi penuh, hasil aktual menunggu W10.
- [TPL-13 Research Defense Template](../../research-os/08-templates/13-research-defense-template.md) — struktur pitch 7–10 menit (W8: slide 1–4 dan 6 penuh, slide 5 rencana pilot), 15 pertanyaan penguji untuk latihan, checklist teknis H-1.
- [TPL-12 Peer Review Template](../../research-os/08-templates/12-peer-review-template.md) — format red team memo untuk tim lain (peran *red team*) dan format *response letter* untuk membalas serangan di PR.
- [TPL-08 Research Design Card](../../research-os/08-templates/08-research-design-card.md) — direvisi setelah red team; alternatif metode yang ditolak tetap tercantum.
- [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) — butir data & privasi dipakai sebagai kerangka `docs/ethics.md`; ditandatangani penuh baru di W15.
- [TPL-05 Dataset Registry Template](../../research-os/08-templates/05-dataset-registry-template.md) — field License & Privacy kartu dataset harus terisi sebelum PR G5.
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — Stage `Method`; [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — lokasi `presentation/`, `docs/reviews/`, `experiments/`, `CHANGELOG.md`, branch `research/g5-method`.
- Form Issue [Experiment](../../.github/ISSUE_TEMPLATE/04-experiment.yml) dan [template PR method-review](../../.github/PULL_REQUEST_TEMPLATE/method-review.md) untuk `GATE REVIEW: Method Ready`.

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W7 Computing Research Methods Map, §W8 Design Defense · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.7–3.9 Design/Data/Baseline & Metrics, §3.11 Threats, §3.12 Ethics & Privacy, §3.16 Research Pitch · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3 E3 Experiment · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.2 Falsification, §2.5 Dataset & privacy, §2.9 Amanah epistemik, §4 Human subjects, §6 pertanyaan integritas G5.
- [AIX-01 Research Meta-Thinking](../../research-os/05-ai-augmented-research/01-research-meta-thinking.md) §7 Falsification, §9 Causal & statistical reasoning · [AIX-02 AI Research Competency](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md) §5 jalur level (G5 = Investigator pada Method), §6 self-assessment · [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.7 Method · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.5 Challenge, §3 izin/larangan.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S8 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G5 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rule B5, §S8, §Jika satu gate terlambat · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) §3.2 TA Ready, §5 Baseline & Leakage · [SECURITY.md](../../SECURITY.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Defensif — atau sebaliknya, menyerah pada semua serangan.** Tim membantah setiap pertanyaan red team di tempat tanpa mencatatnya, atau menerima semua kritik dan mengubah desain sampai tidak lagi menjawab RQ. Cara menghindari: saat pitch hanya *mencatat dan bertanya balik untuk memperjelas*; klasifikasi dilakukan setelah sesi bersama tim; setiap item berstatus ubah/tambah kontrol/tolak dengan alasan tertulis — entri "tolak dengan alasan" sama berharganya dengan "ubah".
2. **Menjawab dengan hasil yang belum ada.** "Metode kami akan lebih akurat 15%" — angka dari mana? Dari AI, dari paper lain dengan data berbeda, atau dari harapan. Cara menghindari: slide 5 berisi rencana pilot dan *expected result* beserta alasannya; jawaban jujur untuk pertanyaan hasil adalah "belum diuji; itu tujuan pilot W10"; tidak ada angka di slide tanpa path artefak.
3. **Metrik atau baseline "disesuaikan" setelah red team tanpa jejak.** Red team menunjukkan bahwa accuracy menyesatkan pada data tidak seimbang, lalu tim diam-diam mengganti metrik — atau menyimpan dua metrik "untuk dipilih nanti". Cara menghindari: perubahan metrik/baseline yang sah dicatat di notulen dan `CHANGELOG.md` dengan alasan dan tanggal, sebelum W9, dan dikunci di Experiment Card; setelah itu, perubahan hanya lewat kartu baru (TPL-09) — bukan lewat memilih angka terbaik di W11.
4. **Ethics plan formalitas.** "Penelitian ini tidak memiliki isu etika" untuk data mahasiswa/pengguna, field privasi kartu dataset kosong, atau nama/NIM muncul di slide dan contoh Experiment Card. Cara menghindari: tulis siapa subjeknya, risiko nyata (privasi, waktu, bias), mitigasi, dan siapa yang menyetujui; periksa riwayat git dan slide sebelum PR; prompt AI hanya memuat metadata.
5. **Red team memo generik dan slack yang dihabiskan.** Serangan ke tim lain berbunyi "tambah data" atau "pakai deep learning" — tidak membantu mereka dan tidak melatih Anda; sementara 15 jam slack S8 dipakai istirahat padahal dataset card (OPS-063) atau Threats v1 (OPS-067) dari W7 belum ada sehingga PR G5 tidak bisa dibuka. Cara menghindari: setiap serangan menunjuk field spesifik di design/experiment card mereka dan menyebut cara gagal yang konkret (split, confounder, baseline tidak adil, lisensi data); gunakan slack untuk menuntaskan sisa W7 — di S9 tidak ada buffer lagi.
