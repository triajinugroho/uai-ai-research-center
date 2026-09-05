# AI Usage Log Template

> **ID** TPL-10 · **Paket** 08 Templates & Toolkit · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa peneliti, dosen/peneliti, mentor, reviewer gate, komite integritas
> **Terkait** [AIX-04 AI Research Protocol](../05-ai-augmented-research/04-ai-research-protocol.md) · [AIX-03 AI Across Value Stream](../05-ai-augmented-research/03-ai-across-research-value-stream.md) · [AIX-02 AI Competency](../05-ai-augmented-research/02-ai-research-competency-framework.md) · [MET-07 Integrity & Ethics](../04-metopen-research-studio/07-research-integrity-and-ethics.md) · [TPL-11 Integrity Checklist](11-research-integrity-checklist.md) · [SECURITY.md](../../SECURITY.md)

## Cara pakai

Log ini mencatat **setiap penggunaan AI yang memengaruhi riset** — desain, pencarian literatur, pemilihan data, kode, eksperimen, analisis, penulisan — sejak onboarding Sprint S0 (pra-W1; dibuat bersamaan dengan repositori riset dan penandatanganan AI Research Protocol agreement, OPS-002/OPS-006, dituntaskan di W1 untuk G1) sampai submission. Diisi oleh anggota tim yang memakai AI, pada hari yang sama, sebagai `docs/AI-USAGE.md` (bagian Log; atau CSV pendamping dengan kolom sama) di repositori riset. Di bagian atas file yang sama disusun **AI Usage Statement** ringkas dari log; versi final untuk naskah ditulis di `paper/AI-USAGE-STATEMENT.md` (OPS-118, difinalkan OPS-139) dan menjadi bagian Research Pack, bagian *AI Usage Disclosure* README riset, dan pernyataan di manuscript. Reviewer memeriksa log pada G3 (verifikasi sumber), G6 (kode berbantuan AI), dan G8 (statement lengkap); log yang tidak lengkap membuat Research Integrity Gate gagal ([TPL-11](11-research-integrity-checklist.md)). Prinsip: AI-augmented, human-accountable — AI adalah research copilot, bukan epistemic authority.

## Aturan

1. **Catat yang material.** Wajib dicatat: setiap output AI yang masuk (utuh/diubah) ke kode, data, analisis, teks, atau keputusan desain. Tidak wajib: pemeriksaan ejaan, terjemahan istilah tunggal.
2. **Tiga verifikasi** sebelum output dipakai ([AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md)): *source* (sumber benar-benar ada: DOI/URL dibuka), *reasoning* (langkah penalaran dicek manusia), *evidence* (klaim dicocokkan dengan data/paper asli). Tulis apa yang dicek, bukan sekadar "sudah diverifikasi".
3. **Tidak ada data sensitif ke tool AI eksternal**: data pribadi, transkrip mahasiswa, data partner, kredensial. Pakai sampel sintetis atau data teranonimisasi yang statusnya Public ([SECURITY.md](../../SECURITY.md)).
4. **Referensi dari AI** dianggap tidak ada sampai diverifikasi; referensi yang tidak dapat diverifikasi dibuang dan dicatat sebagai `dibuang`.
5. **Penanggung jawab manusia** selalu disebut; tanggung jawab atas hasil tidak berpindah ke tool.
6. Log tidak dinilai dari banyaknya AI dipakai, melainkan dari kejujuran dan kualitas verifikasi.

Stage value stream (kolom *Stage*): `Problem · Search · Read · Synthesis · Gap · RQ · Method · Coding · Experiment · Analysis · Writing · Review · Publication`.

## Template log (salin ke `docs/AI-USAGE.md` §Log)

```markdown
| # | Date | Tool (versi) | Stage | Purpose | Prompt / use (ringkas) | Material output? | Verification (source / reasoning / evidence — apa yang dicek) | Inclusion in final work | PJ |
|---|---|---|---|---|---|---|---|---|---|
| [n] | [YYYY-MM-DD] | [nama tool, versi/model] | [stage] | [tujuan 1 frasa] | [inti prompt / cara pakai, 1–2 baris; tanpa data sensitif] | [Ya/Tidak] | [S: … · R: … · E: …] | [Ya / Tidak / Diubah — lokasi (file/section/commit)] | [nama] |
```

Kolom **Inclusion**: *Ya* = dipakai utuh; *Diubah* = dipakai setelah diedit/dikoreksi; *Tidak* = hanya eksplorasi/dibuang.

## Template AI Usage Statement (bagian atas `docs/AI-USAGE.md`; versi final di `paper/AI-USAGE-STATEMENT.md` dan manuscript)

```markdown
## AI Usage Statement — [Research ID] · [YYYY-MM-DD]

Tool yang digunakan: [nama, versi/model].
AI digunakan untuk: [stage + tujuan, mis. eksplorasi kata kunci pencarian (Search), debugging skrip evaluasi (Coding), kritik desain eksperimen (Method), perbaikan bahasa (Writing)].
AI tidak digunakan untuk: [mis. menghasilkan data, menulis hasil, memilih metrik, menghasilkan referensi tanpa verifikasi].
Verifikasi: setiap output AI diperiksa oleh [nama] melalui verifikasi sumber, penalaran, dan bukti; [n] referensi yang diusulkan AI dibuang karena tidak dapat diverifikasi.
Data: tidak ada data pribadi/sensitif yang diberikan ke tool AI; [sampel sintetis/anonim] digunakan bila diperlukan.
Tanggung jawab: seluruh klaim, kode, analisis, dan teks menjadi tanggung jawab penulis.
Log lengkap: `docs/AI-USAGE.md` §Log ([n] entri).
```

Untuk manuscript, ringkas menjadi 3–5 kalimat di bagian Methods/Acknowledgements sesuai kebijakan venue; penggunaan AI dalam proses riset (desain, data, kode, analisis) dijelaskan di Methods, bukan hanya di catatan kaki.

## Contoh terisi

| # | Date | Tool (versi) | Stage | Purpose | Prompt / use (ringkas) | Material output? | Verification | Inclusion in final work | PJ |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 2026-09-[dd] | [LLM chat, model isi] | Search | Kandidat kata kunci & sinonim | "Berikan istilah pencarian untuk academic advising + LLM + recommender di konteks universitas" | Tidak | S: tidak relevan · R: daftar dicek terhadap istilah di 3 paper awal · E: 4 dari 9 istilah menghasilkan hit relevan di Scopus | Diubah — `docs/literature-map.md` §strategi pencarian | [Mahasiswa A] |
| 5 | 2026-09-[dd] | [LLM chat] | Read | Ringkasan awal 2 paper | Unggah PDF paper open-access, minta ringkasan metode & hasil | Ya | S: paper dibaca penuh oleh PJ · R: ringkasan salah pada ukuran sampel, dikoreksi · E: angka dicocokkan dengan tabel paper | Diubah — synthesis matrix baris M-07 | [Mahasiswa B] |
| 6 | 2026-09-[dd] | [LLM chat] | Search | Usulan referensi tambahan | "Sebutkan paper tentang LLM advising di Indonesia" | Tidak | S: 3 dari 4 referensi tidak ditemukan di Scholar/DOI → dibuang; 1 terverifikasi | Tidak (3 dibuang); 1 masuk `references.bib` setelah dibaca | [Mahasiswa A] |
| 7 | 2026-10-[dd] | [coding assistant] | Coding | Debugging parser output LLM | Tempel pesan error + fungsi parser (tanpa data mahasiswa) | Ya | R: patch dibaca baris per baris · E: unit test 12 kasus lulus | Diubah — `src/evaluate.py` (fungsi parser) commit `[hash]` | [Mahasiswa B] |
| 9 | 2026-10-[dd] | [LLM chat] | Method | Red-team desain eksperimen | "Apa kelemahan desain berikut: …" (Design Card v1 tanpa data) | Ya | R: 5 kritik dinilai; 2 diterima (nondeterminisme LLM, gold label subjektif) | Diubah — Design Card v2 threats | [Mahasiswa A] |
| 12 | 2026-11-[dd] | [LLM chat] | Writing | Perbaikan bahasa Inggris abstrak | Tempel draf abstrak, minta koreksi tata bahasa tanpa mengubah isi | Ya | R: dibandingkan kalimat per kalimat; klaim tidak berubah | Diubah — `paper/proposal.md` §Abstract | [Mahasiswa B] |

## Kriteria kualitas

| Aspek | Good | Weak |
|---|---|---|
| Kelengkapan | Semua output material tercatat, termasuk yang dibuang | Hanya penggunaan "yang aman" dicatat |
| Verifikasi | Menyebut apa yang dicek dan hasilnya (mis. 3 referensi dibuang) | "Sudah diverifikasi" |
| Inclusion | Lokasi konkret (file/section/commit) | "Dipakai sebagian" |
| Privasi | Prompt bebas data sensitif; disebut cara menghindarinya | Transkrip mahasiswa ditempel ke chat |
| Statement | Konsisten dengan log; menyebut yang tidak dipakai AI | Statement generik tanpa log |
| Ketepatan waktu | Dicatat hari yang sama | Direkonstruksi menjelang defense |
