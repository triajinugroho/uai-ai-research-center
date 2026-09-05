# Alignment — Global (Arah Riset Computing Dunia yang Kami Ikuti)

> **Status** Draft v0.1 (2026-09) · **Terkait** [Roadmap README](../README.md) · [STR-01 Current State & Gaps](../../research-os/01-strategic-foundation/01-current-state-and-gaps.md) · [MET-01 Metopen Positioning](../../research-os/04-metopen-research-studio/01-metopen-positioning.md) · [AIX-04 AI Research Protocol](../../research-os/05-ai-augmented-research/04-ai-research-protocol.md) · [MET-07 Research Integrity & Ethics](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) · [alignment/uai.md](uai.md)

Dokumen ini memetakan arah global yang menjadi rujukan roadmap. Semua butir berasal dari dokumen diskusi *"Riset AI UAI untuk Negeri"* (benchmark kurikulum dan kebijakan yang dicek pada 2026). **Sumber: dokumen diskusi; verifikasi ke dokumen asli (kurikulum, kebijakan penerbit, standar) sebelum dokumen formal.** Prinsipnya: kami mengikuti arah, bukan menjiplak — sweet spot UAI sengaja ditempatkan sedikit di bawah *ideal frontier* (Occam: *minimum methodological sophistication required to stop producing weak research*).

## 1. Arah global → implikasi untuk roadmap UAI → klaster/domain

| Arah global (menurut dokumen sumber) | Implikasi untuk roadmap 2026–2030 | Klaster/domain terkait | Verifikasi |
|---|---|---|---|
| **Responsible AI**: keadilan, privasi, keamanan, transparansi, akuntabilitas sebagai norma riset dan produk | C3 menjadi gate etika bagi semua aplikasi; `program-responsible-ai` dibuka 2027 (lebih awal dari program domain); audit fairness dan explainability dalam konteks Indonesia sebagai kontribusi | C3; semua domain | `[isi: kerangka responsible AI yang dirujuk]` |
| **Reproducibility & artifact badging (ACM)**: artifact review untuk artefak yang *documented, complete, executable/reusable* dan hasil yang dapat direproduksi pihak lain | Research Repository sebagai artefak yang dapat diperiksa; G6 mewajibkan reproduksi oleh peer; `ART-*` dirilis dengan reproducibility package; 2029 target artefak publik pertama | C2 (infrastruktur), semua klaster | `[isi: kebijakan artifact badging ACM versi terkini]` |
| **CS2023 (ACM/IEEE-CS/AAAI)**: AI semakin sentral, probability/statistics diperkuat, society–ethics–profession terintegrasi, kurikulum *competency-oriented* | AI sebagai payung tematik seluruh riset; statistika sebagai fondasi evaluasi ("enough statistics to prevent bad claims"); kompetensi riset (AI Investigator/Governor) sebagai outcome yang diukur | Semua; [research-based-learning](../../research-based-learning/README.md) | `[isi: rujukan CS2023]` |
| **AI-augmented, human-accountable science**: kebijakan penerbit (ACM 2026 menurut sumber) membedakan AI untuk membantu penulisan dari AI dalam proses riset; penggunaan yang memengaruhi kesimpulan harus dijelaskan dan peneliti tetap bertanggung jawab | AI Usage Statement wajib di setiap Research Pack dan kartu publikasi; AI Research Protocol; riset tentang efektivitas protokol ini sendiri (C3) | C3; [publications](../../publications/README.md) | `[isi: kebijakan penerbit terkini]` |
| **Open science**: data, kode, preprint, lisensi terbuka dengan atribusi | Apache-2.0 untuk kode, CC BY 4.0 untuk dokumen, dataset case-by-case ([LICENSING.md](../../LICENSING.md)); registry dataset dan publikasi publik; preprint bila hak mengizinkan | Semua; [datasets-registry](../../datasets-registry/README.md) | `[isi]` |
| **Research methods courses pasca-GenAI** (benchmark Sydney, Mälardalen, Houston, Princeton, BINUS menurut sumber): literature evaluation, research plan, threats to validity, ethics, experimental design, "CS research in the post-AI world", empirical CS dengan causal reasoning dan benchmark | Metopen sebagai Research Studio (Evidence Engineering); roadmap mengandalkan Research Pack sebagai unit input riset; tidak mengejar advanced causal inference/Bayesian pada S1 | [MET-01](../../research-os/04-metopen-research-studio/01-metopen-positioning.md); semua klaster | `[isi: silabus yang dirujuk + tahun]` |
| **Data-centric AI dan evaluasi yang jujur** (baseline, benchmark, ablation/error analysis, multi-dimensional evaluation) | C1 fokus pada data dan evaluasi, bukan model terbesar; G5 mewajibkan baseline dan metrik sebelum eksperimen | C1, C4 | `[isi]` |
| **Low-resource languages dan AI untuk konteks lokal** sebagai kontribusi yang diakui komunitas global | Korpus/benchmark bahasa Indonesia dan daerah sebagai jalur publikasi internasional yang realistis bagi UAI | C1; [social-impact](../domains/social-impact.md) | `[isi]` |
| **Research integrity** di era GenAI: fabrikasi, sitasi palsu, publication gaming, jurnal predator | Research Integrity Gate lulus/gagal; venue registry [TPL-06](../../research-os/08-templates/06-publication-venue-registry-template.md) dengan status etika publikasi; amanah epistemik | Semua; [MET-07](../../research-os/04-metopen-research-studio/07-research-integrity-and-ethics.md) | `[isi]` |

## 2. Apa yang sengaja tidak kami ikuti secara mentah

Dokumen sumber menegaskan: *"Jangan mengejar ideal universitas top secara mentah."* Untuk roadmap ini artinya:

| Arah global | Mengapa tidak dikejar penuh 2026–2030 |
|---|---|
| Foundation model skala frontier | compute dan data di luar jangkauan; kontribusi lewat evaluasi, adaptasi, korpus |
| Advanced causal inference, Bayesian, econometrics pada level S1 | melampaui kebutuhan; cukup *statistical thinking* untuk mencegah klaim buruk |
| Full systematic review sebagai syarat setiap riset | evidence map + synthesis matrix 15–25 sumber sudah memadai untuk G3 |
| Mengejar venue paling bergengsi sebagai target utama | *publication oriented, not publication obsessed*; venue dipilih backward dari kontribusi ([MET-05](../../research-os/04-metopen-research-studio/05-publication-backward-design.md)) |

## 3. Bagaimana arah global masuk ke praktik harian

1. **Setiap Research Pack** memuat Threats to Validity, Ethics & Privacy, AI Usage Statement, Reproducibility README — ini adalah arah global yang dijadikan *definition of done* ([MET-04](../../research-os/04-metopen-research-studio/04-research-pack-specification.md)).
2. **Setiap artefak** (`ART-*`) dinilai terhadap kriteria *documented, complete, executable/reusable* sebelum rilis.
3. **Setiap publikasi** (`PUB-*`) mencatat AI Usage Statement, lisensi, dan tautan artefak/dataset/kode ([publications](../../publications/README.md)).
4. **Setiap roadmap review** memeriksa apakah arah global berubah (kebijakan penerbit, kurikulum acuan, norma reproducibility) dan memperbarui tabel §1.

## 4. Daftar verifikasi sebelum dokumen formal

- [ ] Rujukan CS2023 dicek ke dokumen asli (tahun, penerbit).
- [ ] Kebijakan AI penerbit (ACM dan penerbit lain yang menjadi target) dicek versi terkininya.
- [ ] Kebijakan artifact badging ACM dicek versi terkininya.
- [ ] Benchmark mata kuliah research methods (Sydney, Mälardalen, Houston, Princeton, BINUS) dicek ke silabus resmi tahun berjalan; hapus yang tidak dapat diverifikasi.
- [ ] Kerangka responsible AI yang dirujuk disebut secara eksplisit.
