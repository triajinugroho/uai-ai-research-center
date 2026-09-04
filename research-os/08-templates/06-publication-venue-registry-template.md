# Publication Venue Registry Template

> **ID** TPL-06 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Pengelola publications, ketua klaster, mentor, mahasiswa dengan endgame paper, Kaprodi
> **Terkait** [publications/README.md](../../publications/README.md) · [MET-05 Publication Backward Design](../04-metopen-research-studio/05-publication-backward-design.md) · [GOV-04 Risk Register](../07-governance/04-risk-register.md) · [ARC-06 Output Taxonomy](../02-academic-architecture/06-research-output-taxonomy.md) · [TPL-02 Mission Tracker](02-research-mission-tracker-template.md)

## Cara pakai

Registry ini adalah daftar venue (jurnal, konferensi, workshop, repositori dataset/artefak) yang **sudah diperiksa** sehingga tim tidak memilih venue predatory atau salah sasaran. Diisi dan ditinjau oleh pengelola publications bersama `@research-leads`, minimal setahun sekali dan setiap ada usulan venue baru lewat Issue **Publication**. Mahasiswa memakainya pada W1 (menetapkan aspirasi endgame) dan W13 (manuscript) untuk backward design ([MET-05](../04-metopen-research-studio/05-publication-backward-design.md)); kolom **Publication Target** di Mission Tracker hanya boleh berisi venue berstatus *whitelist* atau *hati-hati* dengan persetujuan mentor. Disimpan di `publications/VENUES.md` (indeks) dengan catatan pemeriksaan per venue di Issue.

## Nilai kolom

| Kolom | Nilai / cara mengisi |
|---|---|
| Jenis | Journal / Conference / Workshop / Dataset-artifact venue / Preprint server |
| Tingkat | Nasional / Internasional |
| Indexing | [isi apa adanya dari situs resmi/pengindeks: Sinta (peringkat), Scopus (Q), WoS, DOAJ, ACM DL, IEEE Xplore, DBLP, —] |
| Template | tautan template resmi + format (LaTeX/DOCX) + batas halaman |
| Deadline / siklus | tanggal submit berikutnya atau "rolling"; frekuensi terbit |
| Cost | APC / registration fee dalam mata uang asli; "0" bila gratis; siapa yang membayar (Prodi/hibah/mandiri) |
| Publication ethics status | **Whitelist** (terverifikasi aman) / **Hati-hati** (perlu pemeriksaan tambahan atau syarat) / **Predatory** (dilarang) |
| Suitable topics | klaster C1–C4 dan domain yang cocok |
| Kecocokan endgame | TA (laporan/proposal dapat dikonversi) / Paper / Dataset / Artefak |
| Diverifikasi oleh, tanggal | nama + tanggal pemeriksaan; ulang setahun sekali |

## Template tabel (salin ke `publications/VENUES.md`)

```markdown
| Venue | Jenis | Tingkat | Scope | Indexing | Template | Deadline / siklus | Cost | Ethics status | Suitable topics | Kecocokan endgame | Diverifikasi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [nama venue + URL resmi] | [jenis] | [Nasional/Internasional] | [1 kalimat] | [isi] | [link, format, halaman] | [tanggal/siklus] | [APC/fee, pembayar] | [Whitelist/Hati-hati/Predatory] | [C1–C4; domain] | [TA/Paper/Dataset/Artefak] | [nama, YYYY-MM-DD] |
```

Catatan per venue (opsional, satu blok per baris): alasan status, pengalaman tim sebelumnya, waktu review rata-rata, reviewer contact person.

## Checklist mendeteksi predatory venue

Beri tanda pada setiap item yang terpenuhi. **≥ 3 tanda = Predatory** (dilarang); **1–2 tanda = Hati-hati** (perlu keputusan `@research-leads`); **0 tanda + terverifikasi di pengindeks resmi = Whitelist**.

```markdown
- [ ] Undangan submit datang lewat email massal/spam, memuji karya yang tidak relevan
- [ ] Menjanjikan review sangat cepat (hari) dan penerimaan hampir pasti
- [ ] APC/fee tidak transparan atau baru diberitahukan setelah accepted
- [ ] Klaim indexing (Scopus/WoS/Sinta) tidak dapat diverifikasi di situs pengindeks resmi
- [ ] Editorial board tanpa afiliasi jelas, atau nama akademisi dicantumkan tanpa sepengetahuan mereka
- [ ] Scope sangat luas ("all sciences and engineering") tanpa fokus
- [ ] Situs penuh kesalahan bahasa, alamat kantor tidak jelas, DOI tidak resolve
- [ ] Nama meniru venue mapan (typosquatting) atau memakai "International" tanpa peer review nyata
- [ ] Tidak ada kebijakan peer review, retraction, atau publication ethics yang dapat dibaca
- [ ] Artikel terbit tidak melalui proses review yang terlihat (volume ratusan artikel per nomor)
- [ ] Tidak terdaftar/terdaftar negatif pada daftar rujukan resmi yang dipakai Prodi [isi daftar yang disepakati]
```

Prinsip: bila ragu, **jangan submit**. Publikasi di venue predatory tidak dihitung sebagai output ([GOV-04](../07-governance/04-risk-register.md)) dan merusak reputasi mahasiswa, dosen, dan Prodi.

## Contoh terisi (ilustratif; nama venue diisi saat diverifikasi)

| Venue | Jenis | Tingkat | Scope | Indexing | Template | Deadline / siklus | Cost | Ethics status | Suitable topics | Kecocokan endgame | Diverifikasi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Jurnal nasional bidang informatika/AI — isi] | Journal | Nasional | Sistem cerdas, rekayasa perangkat lunak, komputasi terapan | Sinta [peringkat — isi] | [URL template DOCX; 8–12 halaman] | Rolling; 2 nomor/tahun | [Rp — isi]; Prodi | Whitelist | C3, C4; Education, Government | TA, Paper | [isi], 2026-09-[dd] |
| [Konferensi nasional AI in education — isi] | Conference | Nasional | AI dalam pendidikan, learning analytics, HCI | [isi] | [LaTeX 2 kolom; 6 halaman] | [YYYY-MM-DD] | [Rp — isi]; hibah/Prodi | Whitelist | C3; Education | Paper | [isi], 2026-09-[dd] |
| [Repositori dataset terbuka — isi] | Dataset-artifact venue | Internasional | Dataset dengan datasheet dan DOI | DOI, Google Dataset Search | Datasheet for datasets | Rolling | 0 | Whitelist | C1, C3; semua domain | Dataset | [isi], 2026-09-[dd] |
| [Venue yang mengirim undangan spam — isi] | Journal | Internasional | "All areas of computing and engineering" | Klaim Scopus tidak terverifikasi | — | 7 hari | USD [isi] setelah accepted | Predatory | — | — | [isi], 2026-09-[dd] |

Pemakaian pada UIAI-2026-001: Publication Target = baris 2 (konferensi nasional AI in education); backward milestone: manuscript-ready W13 → internal review W14 → submission-ready setelah G8.

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Verifikasi | Indexing dicek langsung di situs pengindeks; tanggal dan nama pemeriksa tercatat | Menyalin klaim dari situs venue |
| Status etika | Ditentukan lewat checklist dengan bukti | "Kelihatannya bagus" |
| Kecocokan | Scope dan topik dipetakan ke klaster/domain; batas halaman dan format tercatat | Daftar nama venue tanpa scope |
| Biaya | Angka + siapa yang membayar | "Terjangkau" |
| Pembaruan | Ditinjau tahunan; venue yang berubah status ditandai | Registry berumur 3 tahun tanpa revisi |
