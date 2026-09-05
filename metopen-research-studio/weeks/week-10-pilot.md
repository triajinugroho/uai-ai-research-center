# Week 10 — Pilot

> **Sprint** S10 · **Gate** G6 Experiment Ready · **Status** Draft v0.1 (2026-09) · [← Week sebelumnya](week-09-repository.md) / [Week berikutnya →](week-11-analysis.md)

## This Week

Pada akhir minggu ini tim Anda dapat mengucapkan: **"Pilot kami berjalan; orang lain sudah mereproduksinya."** Minimum viable experiment dijalankan end-to-end pada subset data dengan seed tetap — baseline plus minimal satu metode pembanding, minimal 3 seed — hasil per run disimpan di `results/pilot-01/`, dirangkum menjadi tabel dan figur awal, lalu diperiksa dengan sanity check dan uji leakage; setelah itu **peer dari tim lain mereproduksi angka baseline hanya dari repositori** tanpa bertanya ke tim ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W10; [OPS-02](../../research-os/06-execution-os/02-weekly-sprints.md) §S10). Tujuan pilot adalah membuktikan desain *viable*, bukan mengejar angka terbaik; keputusan *lanjut / ubah desain / ubah skala* dicatat di Experiment Card dan disetujui mentor. Semua bukti masuk PR `GATE REVIEW: Experiment Ready`; merge berarti G6 lulus dan release `v0.5 Pilot Experiment`.

Sesi studio 100 menit dibagi tiga: **30 menit konsep** (pilot vs eksperimen penuh, seed dan variansi antar run, sanity check hasil, logging ke `results/`), **60 menit studio** (menulis kriteria keberhasilan pilot, lalu memulai run pertama dengan seed tetap; tim yang run-nya masih berjalan menyusun checklist sanity check dan menghubungi peer reproducer), **10 menit gate check** (tiap tim menyebut angka baseline pertamanya dan satu hal yang akan membuat mereka curiga pada angka itu). Sprint ini sedang secara jam (16 jam, slack 7 jam) tetapi rapuh pada satu titik: ketersediaan peer reproducer dari tim lain — minta kesediaan mereka hari Senin, bukan Kamis ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Slack dan buffer).

## Concept (30 menit)

1. **Pilot ≠ eksperimen penuh.** Pilot menjawab "apakah desain ini bisa dijalankan dan menghasilkan angka yang masuk akal?", bukan "berapa angka terbaik?". Subset data, baseline + satu pembanding, beberapa seed — cukup untuk melihat pipeline bekerja dan variansinya terbaca ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.10). Pilot yang terlalu ambisius menghabiskan jam S11.
2. **Kriteria keberhasilan ditulis sebelum run.** Sebelum satu run pun dimulai, tim menulis apa yang dianggap pilot "berhasil" (pipeline selesai end-to-end, baseline di rentang yang diharapkan Experiment Card, variansi antar seed terbaca) dan "gagal" (crash, metrik tidak terhitung, hasil mustahil) — bagian *Success Criteria* di Experiment Card ([TPL-09](../../research-os/08-templates/09-experiment-card.md)); *expected result* dari W8 tidak diubah.
3. **Seed dan variansi antar run.** Satu angka dari satu seed bukan hasil; hasil adalah mean ± std dari n seed. Perbedaan baseline vs pembanding yang lebih kecil daripada variansi antar seed belum berarti apa-apa — itu bahan W11, bukan klaim W10.
4. **Sanity check: curigai hasil yang terlalu bagus.** Baseline harus masuk akal (majority class ≈ proporsi kelas mayoritas); hasil pada label yang diacak harus jatuh ke *chance*; tidak ada overlap entitas antara train dan test; metrik dihitung ulang manual pada sampel kecil. Akurasi mendekati sempurna hampir selalu berarti leakage, bukan terobosan ([MST-03](../../research-os/00-master/03-glossary.md) §5 Leakage; [AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.9).
5. **Logging dan `results/`.** Setiap run menghasilkan file dengan seed, git hash, timestamp, config, waktu, dan resource. Setiap angka di tabel/figur harus dapat ditelusuri ke file run tertentu; run yang gagal tetap dicatat, tidak dihapus.
6. **Reproduksi peer adalah definisi G6** (blocking rule B6). Peer dari tim lain menjalankan baseline dari environment bersih hanya dengan `experiments/README.md`; toleransi selisih ditetapkan sebelum peer mulai; setiap kendala peer adalah bug README, bukan kesalahan peer ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G6; [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.7).
7. **Keputusan pilot: lanjut / ubah desain / ubah skala.** Hasil aktual vs expected, penyimpangan, dan keputusan diisi di Experiment Card dan disetujui mentor. Blocking rule B7: eksperimen penuh (OPS-097, W11) tidak dimulai sebelum keputusan ini dan PR G6 termerge ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Blocking rules).
8. **Metrik dan baseline tetap yang dikunci di G5.** Bila hasil pilot memaksa perubahan (misalnya metrik tidak terhitung pada data nyata), buat kartu eksperimen baru, catat alasan dan tanggal, minta persetujuan mentor — jangan mengganti diam-diam ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint).
9. **AI pada eksperimen: mendiagnosis, bukan menghasilkan.** Target level minggu ini *AI Investigator pada Coding/Experiment*: kode berbantuan AI beratribusi dan diuji, tidak ada data ke AI, tidak ada angka dari AI ([AIX-02](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md) §5; [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.6 Reproduce).

**Pertanyaan pemandu** yang harus bisa Anda jawab di akhir sesi tanpa membuka catatan: *"Baseline kami memberi ___ ± ___ pada ___ seed; apa yang membuat kami yakin angka itu bukan hasil leakage — dan sudahkah orang di luar tim mendapat angka yang sama hanya dari repositori kami?"*

## Tasks

Semua task Sprint S10 dari Research WBS ([OPS-01](../../research-os/06-execution-os/01-research-wbs-master.md)); tandai `[ ]` belum, `[~]` sedang, `[x]` selesai pada salinan tim Anda. Setiap commit menyebut Task ID, misalnya `Add pilot-01 results for 3 seeds (OPS-088)`. Task W9 yang belum selesai — terutama OPS-083 (`run.sh` + logging), OPS-084 (`experiments/README.md` v0), OPS-086 (code review internal) — ditulis di atas tabel ini pada salinan tim; pilot (OPS-088) tidak boleh dijalankan sebelum PR G5 termerge dan kode baseline/metode/evaluasi ter-commit.

| Task ID | Task | Output | Effort | AI Assist | Human Check |
|---|---|---|---|---|---|
| OPS-087 | Ikuti sesi Pilot Study / Minimum Viable Experiment | Kriteria keberhasilan pilot | 1.5h | - | Mentor memeriksa kriteria ditulis sebelum menjalankan pilot |
| OPS-088 | Jalankan pilot end-to-end: baseline + minimal satu metode pembanding | Hasil pilot | 4h | Membantu mendiagnosis error saat berjalan | Tim memeriksa hasil berasal dari kode yang ter-commit |
| OPS-089 | Buat tabel hasil pilot dan figur awal | Tabel + figur pilot | 2h | Membantu kode plotting; tim memeriksa skala dan label | Tim memastikan baseline terlihat dan sumbu tidak menyesatkan |
| OPS-090 | Lakukan sanity check dan uji leakage pada hasil pilot | Catatan sanity check | 2h | Mengusulkan pemeriksaan tambahan | Tim menuliskan bukti tiap pemeriksaan lulus atau gagal |
| OPS-091 | Minta peer mereproduksi hasil baseline dari repositori | Catatan reproduksi peer | 2h | - | Peer reproducer mengonfirmasi angka baseline cocok dalam toleransi |
| OPS-092 | Perbaiki reproducibility README dan kode berdasarkan kendala peer | experiments/README.md v1 | 1.5h | Membantu memperjelas instruksi | Peer mengonfirmasi reproduksi berhasil setelah perbaikan |
| OPS-093 | Perbarui Experiment Card dengan hasil aktual dan catatan pilot | Experiment card terisi penuh | 1h | - | Mentor memeriksa keputusan lanjut/ubah masuk akal |
| OPS-094 | Siapkan PR GATE REVIEW: Experiment Ready (experiment-review.md) | PR GATE REVIEW: Experiment Ready | 1.5h | - | Reviewer memeriksa peer dapat mereproduksi angka baseline dari repositori |
| OPS-095 | Perbarui AI Usage Log dan jurnal mingguan W10 | AI Usage Log W10 + jurnal | 0.5h | - | Setiap anggota memverifikasi entri log miliknya |

**Total effort: 16h** (jam tim; untuk tim 2 orang bagi dua). Jalur kritis 9 jam — rantai 088 → 091 → 092 → 094 — sehingga waktu tunggu peer reproducer adalah risiko jadwal terbesar minggu ini ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Task yang bisa paralel).

**Urutan yang disarankan** (dari kolom Dependency): Senin mulai dua task yang sudah punya semua dependency dari W8–W9 — **OPS-087** di sesi studio (butuh Experiment Card OPS-071 dan sesi OPS-078) dan **OPS-088** run pilot dengan seed tetap (butuh PR G5 OPS-076, kode 081/082/083, code review 086) → begitu hasil ada, tiga task berjalan paralel oleh orang berbeda: **OPS-089** tabel/figur, **OPS-090** sanity check, dan **OPS-091** yang dikerjakan **peer**, bukan tim (butuh 085 + 088) → **OPS-092** perbaiki README dari kendala peer (butuh 091) dan **OPS-093** isi hasil aktual + keputusan (butuh 089 + 090) → **OPS-094** PR G6 setelah 085, 089, 091, 092, 093 selesai; **OPS-095** log dan jurnal berjalan sepanjang minggu dan ditutup Jumat.

## Deliverable

Hari Jumat, di repositori riset `proj-YYYY-topic` ([TPL-15](../../research-os/08-templates/15-research-repository-template.md)) pada branch `research/g6-experiment`, harus ada:

| Artefak | Lokasi di repositori | Bentuk bukti | Task |
|---|---|---|---|
| **Kriteria keberhasilan pilot**: apa yang dianggap "berhasil" dan "gagal", dengan rujukan ke *expected result* W8; ditulis sebelum run pertama | `experiments/pilot-01/experiment-card.md` bagian *Success Criteria* | commit bertanggal sebelum file run pertama | OPS-087 |
| **Hasil pilot per run**: baseline + minimal satu pembanding, minimal 3 seed, subset data yang sama; tiap file memuat seed, git hash, timestamp, config, waktu, dan resource; run gagal tetap disimpan | `results/pilot-01/*.json` (+ log di `experiments/pilot-01/logs/`) | commit; angka dapat ditelusuri ke `run.sh` dan `experiments/pilot-01/config.yaml` | OPS-088 |
| **Tabel hasil dan figur awal**: mean ± std antar seed per sistem; 1–2 figur dengan baseline terlihat, sumbu berskala jujur, label lengkap; dihasilkan skrip, bukan disusun manual | `results/pilot-01/summary.md`, `figures/pilot-01/*.png`; skrip `src/report.py` atau `notebooks/pilot-results.ipynb` (output dibersihkan) | commit; tiap angka di summary sama dengan file run | OPS-089 |
| **Catatan sanity check**: hasil label shuffle (harus ke *chance*), cek overlap entitas antar split, perhitungan manual metrik pada sampel kecil, kewajaran baseline, pemeriksaan tambahan yang dipilih tim — masing-masing berstatus lulus/gagal dengan bukti | `results/pilot-01/sanity-check.md` | commit | OPS-090 |
| **Catatan reproduksi peer**: peer dari tim lain (nama, tanggal, commit yang direproduksi, environment), perintah yang dijalankan, angka baseline yang diperoleh vs angka tim, selisih terhadap toleransi, kendala; ditandatangani peer | `docs/reviews/reproduction-pilot-01.md` | commit oleh peer atau PR comment dari akun peer | OPS-091 |
| **Reproducibility README v1**: langkah yang hilang, versi, path, dan waktu eksekusi diperbaiki sesuai kendala peer; tabel eksperimen sesuai [TPL-15](../../research-os/08-templates/15-research-repository-template.md) §experiments/README | `experiments/README.md`, `run.sh`, `requirements.txt`/`environment.yml` | commit perbaikan; catatan peer berstatus *berhasil* setelah perbaikan | OPS-092 |
| **Experiment Card terisi penuh** ([TPL-09](../../research-os/08-templates/09-experiment-card.md)): *Hasil aktual* (tanggal run, commit, tabel, penyimpangan, error analysis awal, reproduksi peer, entri AI Usage Log) dan *Keputusan* (lanjut / ubah desain / ubah skala) disetujui mentor; bagian pra-registrasi tidak berubah | `experiments/pilot-01/experiment-card.md`; `CHANGELOG.md` bagian `v0.5` | commit kartu; Issue `type:experiment` ([form Experiment](../../.github/ISSUE_TEMPLATE/04-experiment.yml)) diperbarui dengan hasil dan keputusan | OPS-093 |
| **PR `GATE REVIEW: Experiment Ready — UIAI-YYYY-NNN`** dari `research/g6-experiment` memakai [template experiment-review](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md); setelah merge: label `gate:G6-experiment`, release **`v0.5 Pilot Experiment`** | PR; GitHub Release | URL PR; release v0.5; README §Current Research Gate | OPS-094 |
| AI Usage Log W10 Stage `Experiment`/`Coding`: diagnosis error, kode plotting, usulan sanity check, penjelasan instruksi README — dan keputusan manusia atas tiap output; jurnal W10: **apa yang mengejutkan dari hasil pilot** | `docs/AI-USAGE.md` — log + ringkasan statement ([TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md)); `docs/journal/w10.md` | commit | OPS-095 |

Release `v0.5 Pilot Experiment` menambahkan artefak Research Pack 10 (pilot) dan 14 (Reproducibility README minimum) ke v0.3 ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §7). Setelah PR termerge, README riset: `Current Research Gate: G6 (passed) → G7 (in progress)`; data mentah, data pribadi, kredensial, dan output notebook yang memuat data tetap tidak ada di repositori ([SECURITY.md](../../SECURITY.md)).

## AI Assist

Ikuti [AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) (*Think → Ask → Ground → Verify → Challenge → Reproduce → Disclose → Own*) dan catat setiap penggunaan yang material di AI Usage Log [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) **pada hari penggunaan**, Stage `Experiment` (atau `Coding` untuk perubahan kode). Minggu ini AI berguna sebagai **teknisi diagnosis**: membaca traceback, mengusulkan pemeriksaan, merapikan skrip — tidak pernah sebagai sumber angka ([AIX-03](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.9 Experiment).

**Boleh minggu ini**

- Meminta AI membantu mendiagnosis error saat pilot berjalan — pesan error, traceback, log — dengan konteks kode dan config, tanpa data (OPS-088); perbaikan dibaca, diuji, di-commit dengan atribusi di log.
- Meminta AI membantu kode plotting dan tabel ringkasan (OPS-089); tim memeriksa skala sumbu, label, baseline terlihat, dan mencocokkan tiap angka dengan file run.
- Meminta AI mengusulkan pemeriksaan sanity tambahan untuk jenis data/metode Anda — "bagaimana leakage bisa terjadi pada pipeline ini?" (OPS-090); tim menjalankan pemeriksaannya sendiri dan menulis buktinya.
- Meminta AI memperjelas kalimat instruksi di `experiments/README.md` yang membuat peer tersandung (OPS-092); langkahnya tetap diuji ulang oleh peer, bukan oleh AI.
- Meminta AI menjelaskan mengapa variansi antar seed besar atau mengapa baseline memberi angka tertentu — sebagai hipotesis untuk diperiksa, bukan sebagai interpretasi yang disalin ke kartu.
- Meminta AI menantang kesimpulan Anda sendiri: "apa yang salah dari klaim bahwa pilot ini berhasil?" ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.5 Challenge); catat kritik yang ditolak beserta alasannya.

**Tidak boleh**

- "Memperbaiki" hasil dengan angka dari AI, mengisi sel tabel yang run-nya gagal, atau membiarkan AI menyusun `summary.md` dari ingatan percakapan — setiap angka harus berasal dari file di `results/pilot-01/` ([MET-03](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W10).
- Menyembunyikan run yang gagal atau seed yang buruk, apa pun sarannya; run gagal dicatat di experiment card sebagai penyimpangan.
- Memasukkan data mentah, data pribadi, output notebook berisi data, atau kredensial ke layanan AI saat debugging ([SECURITY.md](../../SECURITY.md); [TPL-10](../../research-os/08-templates/10-ai-usage-log-template.md) aturan 3).
- Memakai AI pada task yang menurut WBS tanpa bantuan AI: OPS-087 (kriteria keberhasilan ditulis tim), OPS-091 (peer mereproduksi sendiri — bukan dibantu chat AI tim), OPS-093 (keputusan pilot), OPS-094 (PR gate), OPS-095 (log & jurnal).
- Mengganti metrik atau baseline karena AI menyarankan metrik "yang lebih cocok" setelah hasil terlihat — itu metric switching ([AIX-04](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §3).

## Human Check

| Apa yang diverifikasi | Siapa | Task |
|---|---|---|
| Kriteria keberhasilan pilot ditulis dan ter-commit **sebelum** run pertama; konsisten dengan *expected result* W8 | mentor | OPS-087 |
| Setiap file hasil berasal dari kode yang ter-commit (git hash di file = commit di repo); config, seed, dan subset data identik antar sistem; run gagal tercatat | tim (anggota yang tidak menjalankan run memeriksa) | OPS-088 |
| Baseline terlihat di setiap figur; sumbu tidak dipotong atau diskalakan menyesatkan; angka di `summary.md` sama dengan file run; mean ± std, bukan angka terbaik | tim; satu peer memeriksa satu figur | OPS-089 |
| Tiap pemeriksaan sanity berstatus lulus/gagal dengan bukti tertulis; label shuffle jatuh ke *chance*; tidak ada overlap entitas antar split; metrik cocok dengan hitungan manual | tim; dosen membaca `sanity-check.md` saat review PR | OPS-090 |
| Angka baseline peer cocok dengan angka tim dalam toleransi yang ditetapkan sebelumnya; peer bekerja dari environment bersih tanpa bertanya ke tim; kendala dicatat apa adanya | peer reproducer dari tim lain (atau asisten studio bila tim lain sibuk) | OPS-091 |
| Setelah perbaikan README/skrip, reproduksi diulang dan berhasil; catatan peer berstatus *berhasil* | peer reproducer | OPS-092 |
| Keputusan lanjut / ubah desain / ubah skala masuk akal terhadap hasil dan sanity check; pra-registrasi tidak berubah; penyimpangan dijelaskan | mentor | OPS-093 |
| Definition of done G6 lengkap: `src/`, `notebooks/`, `experiments/` + config/seed/env/README; pilot end-to-end; hasil di `results/` dan `figures/`; reproduksi peer tercatat; metrik & baseline tidak berubah dari G5; integritas: tidak ada data sensitif di commit, kode AI diungkap | dosen pengampu + peer reproducer (reviewer PR) | OPS-094 |
| Setiap anggota memverifikasi entri AI Usage Log miliknya, termasuk kode berbantuan AI yang di-commit minggu ini; jurnal ditulis jujur tentang yang mengejutkan | diri sendiri; mentor membaca jurnal | OPS-095 |

Prinsip: task selesai hanya jika Output ada di repo, Evidence dapat dibuka reviewer, Human Check sudah dilakukan, dan AI Usage Log tercatat ([OPS-05](../../research-os/06-execution-os/05-student-weekly-playbook.md) §Aturan sprint). Untuk W10, "dapat dibuka reviewer" berarti reviewer meng-clone repositori, menjalankan `run.sh` sesuai README, dan mendapat angka baseline yang sama — hasil di laptop anggota tim tidak dihitung.

## Done When

Minggu ini **menutup gate G6 Experiment Ready**. Jawab ya/tidak per butir pada Jumat:

- [ ] PR `GATE REVIEW: Method Ready` (G5) sudah termerge dan kode W9 (OPS-081, 082, 083, 084, 086) ter-commit sebelum run pilot pertama — pilot tidak dijalankan dengan metrik "sementara".
- [ ] `experiments/pilot-01/experiment-card.md` memuat *Success Criteria* dengan tanggal commit lebih awal daripada file hasil pertama di `results/pilot-01/`.
- [ ] `results/pilot-01/` berisi hasil baseline + minimal satu pembanding pada minimal 3 seed; tiap file memuat seed, git hash, timestamp; run gagal ikut tersimpan.
- [ ] `results/pilot-01/summary.md` (mean ± std) dan `figures/pilot-01/` dihasilkan skrip; baseline terlihat di setiap figur; tiap angka cocok dengan file run.
- [ ] `results/pilot-01/sanity-check.md` lengkap: label shuffle jatuh ke *chance*, tidak ada overlap split, metrik cocok dengan hitungan manual, baseline wajar — setiap butir berstatus lulus/gagal dengan bukti.
- [ ] `docs/reviews/reproduction-pilot-01.md` ditandatangani peer dari tim lain; angka baseline cocok dalam toleransi; kendala peer sudah diperbaiki di `experiments/README.md` v1 dan reproduksi ulang berstatus *berhasil*.
- [ ] Experiment Card: *Hasil aktual*, *Penyimpangan*, *Reproduksi peer*, dan *Keputusan* (lanjut / ubah desain / ubah skala) terisi dan disetujui mentor; pra-registrasi tidak berubah; Issue `type:experiment` diperbarui.
- [ ] Metrik dan baseline identik dengan yang dikunci di G5; bila ada perubahan, kartu baru + alasan + tanggal + persetujuan mentor tercatat di `CHANGELOG.md`.
- [ ] `docs/AI-USAGE.md` memuat entri Stage `Experiment`/`Coding` untuk setiap penggunaan material minggu ini; tiap anggota sudah memverifikasi entrinya; ringkasan AI Usage Statement di bagian atas file diperbarui; `docs/journal/w10.md` ditulis.
- [ ] Di gate check, tim menyebut angka baseline ± std, menunjuk file run-nya, dan menyebut satu pemeriksaan sanity yang paling meyakinkan mereka.
- [ ] PR **`GATE REVIEW: Experiment Ready`** termerge oleh dosen pengampu + peer reproducer; label `gate:G6-experiment`; release `v0.5 Pilot Experiment` dibuat; README §Current Research Gate diperbarui.

**Ringkasan gate G6** ([OPS-03](../../research-os/06-execution-os/03-research-gates.md) §G6). **Lulus jika** peer dapat mereproduksi angka baseline dari repositori. **Gagal jika** hasil hanya ada di laptop anggota tim — atau bila ada pelanggaran integritas (data sensitif di commit, run gagal disembunyikan, metrik diganti setelah melihat hasil, kode berbantuan AI tidak diungkap), terlepas dari kualitas lainnya. Reviewer: dosen pengampu + peer reproducer. Hasil pilot yang **buruk** tidak membuat gate gagal; yang membuat gagal adalah hasil yang tidak dapat direproduksi atau tidak jujur — pilot dengan keputusan "ubah desain" yang tercatat tetap lolos G6. Bila G6 terlambat: turunkan skala (subset lebih kecil, 3 seed), prioritaskan reproducibility README daripada hasil bagus, minta asisten studio menjadi peer reproducer bila tim lain sibuk, dan pangkas eksperimen penuh W11 ke kondisi minimum yang menjawab RQ utama — jangan pernah melewati OPS-091 ([OPS-04](../../research-os/06-execution-os/04-dependency-and-critical-path.md) §Jika satu gate terlambat).

**Cara membuka PR gate** ([CONTRIBUTING.md](../../CONTRIBUTING.md) §3): (1) pastikan semua bukti di tabel Deliverable ada di branch `research/g6-experiment`; (2) buka PR berjudul `GATE REVIEW: Experiment Ready — UIAI-YYYY-NNN` dengan `?template=experiment-review.md` atau salin isi [template experiment-review](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md); (3) isi seluruh bagian: RQ, Method (sesuai Design Card G5), Dataset & split (subset pilot, pencegahan leakage), Baseline & metode pembanding (config/seed), Metrics & hasil pilot (mean ± std, baseline terlihat), Threats yang diperbarui dari pengalaman pilot, tabel Struktur repositori & reproducibility, Catatan reproduksi peer, tabel Evidence, AI Usage dengan bagian kode yang dibantu AI dan cara memverifikasinya; (4) tautkan nomor PR G5 dan Issue `type:experiment`; (5) minta review dosen pengampu + peer reproducer, dan minta peer mengisi bagian *Untuk reviewer — peer reproducer* (perintah yang dijalankan, angka yang diperoleh, langkah README yang tidak jelas) — jawab kendala dengan memperbaiki README, bukan hanya membalas komentar; (6) setelah merge: label → `gate:G6-experiment`, field Mission Control dan README diperbarui, release `v0.5 Pilot Experiment`, Issue Experiment diperbarui dengan keputusan. Komentar review disimpan, tidak dihapus.

## Templates & rujukan

**Template yang dipakai minggu ini**

- [TPL-09 Experiment Card](../../research-os/08-templates/09-experiment-card.md) — bagian *Hasil aktual* dan *Keputusan* diisi minggu ini; pra-registrasi dari W8 tidak diubah; contoh terisi menunjukkan format hasil mean ± sd dan catatan reproduksi peer.
- [TPL-15 Research Repository Template](../../research-os/08-templates/15-research-repository-template.md) — isi minimal `experiments/README.md` (tabel eksperimen, perintah menjalankan, konvensi hasil/figur), lokasi `results/`, `figures/`, `docs/reviews/`, branch `research/g6-experiment`.
- [TPL-10 AI Usage Log Template](../../research-os/08-templates/10-ai-usage-log-template.md) — Stage `Experiment` dan `Coding`; aturan tidak ada data sensitif ke tool AI.
- [TPL-12 Peer Review Template](../../research-os/08-templates/12-peer-review-template.md) — format catatan peer reproducer bila tim ingin struktur yang seragam dengan review lain.
- [TPL-11 Research Integrity Checklist](../../research-os/08-templates/11-research-integrity-checklist.md) — butir reproducibility dan data dipakai sebagai pemeriksaan diri sebelum PR; ditandatangani penuh di W15.
- Form Issue [Experiment](../../.github/ISSUE_TEMPLATE/04-experiment.yml) dan [template PR experiment-review](../../.github/PULL_REQUEST_TEMPLATE/experiment-review.md) untuk `GATE REVIEW: Experiment Ready`.

**Dokumen konsep**

- [MET-03 16-Week Blueprint](../../research-os/04-metopen-research-studio/03-metopen-16-week-blueprint.md) §W9 Repository, §W10 Pilot, §W11 Analysis · [MET-04 Research Pack](../../research-os/04-metopen-research-studio/04-research-pack-specification.md) §3.9 Baseline & Metrics, §3.10 Pilot Experiment, §3.14 Reproducibility README, §7 release v0.5 · [MET-06 5E Rubric](../../research-os/04-metopen-research-studio/06-assessment-and-5e-rubric.md) §3.3 E3 Experiment · [MET-07 Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.1 Fabrication, §2.2 Falsification, §2.7 Reproducibility, §6 pertanyaan integritas G6.
- [AIX-02 AI Research Competency](../../research-os/05-ai-augmented-research/02-ai-research-competency-framework.md) §5 (G6 = Investigator pada Coding/Experiment) · [AIX-03 AI Across Research Value Stream](../../research-os/05-ai-augmented-research/03-ai-across-research-value-stream.md) §3.8 Coding, §3.9 Experiment · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) §2.6 Reproduce, §2.7 Disclose, §3 izin/larangan.
- [OPS-02 Weekly Sprints](../../research-os/06-execution-os/02-weekly-sprints.md) §S10 · [OPS-03 Research Gates](../../research-os/06-execution-os/03-research-gates.md) §G6 · [OPS-04 Dependency & Critical Path](../../research-os/06-execution-os/04-dependency-and-critical-path.md) blocking rules B5–B7, §S10, §Jika satu gate terlambat · [OPS-05 Student Weekly Playbook](../../research-os/06-execution-os/05-student-weekly-playbook.md) · [MST-03 Glossary](../../research-os/00-master/03-glossary.md) §2 Reproducibility package, §3.4 release v0.5, §5 Baseline & Leakage · [SECURITY.md](../../SECURITY.md).

**Halaman studio**

- [Studio README](../README.md) · [Research Gates](../research-gates/README.md) · [AI Toolkit](../ai-toolkit/README.md) · [Rubrics](../rubrics/README.md) · [Templates](../templates/README.md) · [Examples](../examples/README.md) · [Student Guide](../../research-based-learning/student-guide/README.md).

## Jebakan minggu ini

1. **Pilot dijadikan eksperimen penuh.** Tim menjalankan seluruh dataset, lima metode, dan tuning hyperparameter di W10 "supaya W11 ringan" — run tidak selesai, tidak ada waktu untuk sanity check dan reproduksi peer, PR G6 tidak terbuka. Cara menghindari: subset data, baseline + satu pembanding, 3 seed; kriteria keberhasilan pilot adalah *pipeline berjalan dan angka masuk akal*, bukan angka bagus; skala penuh menunggu keputusan pilot dan PR G6 (blocking rule B7).
2. **Hasil "terlalu bagus" dirayakan, bukan dicurigai.** Akurasi 99% pada data yang di literatur mentok di 80% hampir pasti leakage: pra-pemrosesan sebelum split, entitas yang sama di train dan test, fitur yang merupakan target terselubung. Cara menghindari: jalankan label shuffle (harus jatuh ke *chance*), cek overlap entitas, hitung metrik manual pada sampel kecil, bandingkan dengan rentang di `common-metrics-baselines.md` W4; tulis semua di `sanity-check.md` sebelum siapa pun menyebut angka itu di luar tim.
3. **Satu seed terbaik, run gagal dihapus.** Tabel berisi satu angka per sistem, seed yang "jelek" tidak dilaporkan, dan run yang crash dihapus dari `results/`. Ini falsifikasi ([MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) §2.2). Cara menghindari: laporkan mean ± std dari semua seed yang direncanakan; run gagal tetap tersimpan dan dicatat sebagai penyimpangan di Experiment Card; skrip yang membuat `summary.md` membaca semua file run, bukan file pilihan.
4. **Reproduksi peer yang "dibantu".** Peer adalah anggota tim sendiri, atau peer dari tim lain dipandu lewat chat langkah demi langkah, atau menjalankan di laptop tim yang environment-nya sudah jadi — lalu catatan menyatakan "berhasil". Cara menghindari: peer dari tim lain, environment bersih, hanya README; setiap pertanyaan peer dicatat sebagai kendala dan dijawab dengan memperbaiki README (OPS-092), lalu peer mengulang; toleransi selisih ditetapkan sebelum peer mulai.
5. **Angka di tabel tidak sama dengan angka di `results/`.** `summary.md` diketik manual dari ingatan, figur dibuat dari run lama, atau notebook dijalankan tidak berurutan sehingga angka di PR tidak dapat ditelusuri ke file mana pun. Cara menghindari: satu skrip (`src/report.py`) menghasilkan tabel dan figur dari file run; tiap file run memuat git hash; reviewer mencocokkan satu angka acak di PR dengan file run-nya — lakukan pemeriksaan itu sendiri sebelum reviewer melakukannya.
