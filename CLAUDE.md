# CLAUDE.md — Panduan untuk sesi Claude Code di repo ini

Repo ini adalah **UAI AI Research Center** — *research operating system* Pusat Riset AI Program Studi Informatika, Universitas Al-Azhar Indonesia. Isinya hampir seluruhnya Markdown (framework, template, registry), bukan kode aplikasi.

## Sumber kebenaran

- Dokumen asal desain: `research-os/00-master/source/riset-ai-uai-untuk-negeri.docx` (transkrip diskusi desain; jangan diubah).
- Kamus istilah, skema ID, gate, klaster: `research-os/00-master/03-glossary.md` — **selalu ikuti definisi di sini**.
- Definisi 8 Research Gates: `research-os/06-execution-os/03-research-gates.md`.
- Konvensi kontribusi (Issue = unit riset, PR = gate review, branch `research/gN-*`): `CONTRIBUTING.md`.
- Tata kelola, tim, akses, taksonomi label/topics: `GOVERNANCE.md`; kebijakan lisensi: `LICENSING.md`.

## Struktur (monorepo yang meniru launch set 7 repo Organization)

| Folder | Menjawab | Catatan |
|---|---|---|
| `research-os/` | *How do we research?* | 9 paket `00-master` … `08-templates`, 57 dokumen ber-ID |
| `research-roadmap/` | *What should we research?* | klaster, domain, alignment 2026–2030 |
| `research-backlog/` | *What could be researched next?* | problem bank; sumber utama Issues |
| `datasets-registry/` | katalog metadata dataset | **tidak pernah** menyimpan data mentah |
| `research-based-learning/` | mata kuliah → research pipeline | mode F/E/R per mata kuliah |
| `metopen-research-studio/` | View B mahasiswa Metopen | `weeks/week-01…16.md` merujuk Task ID WBS |
| `publications/` | registry metadata publikasi | tanpa PDF publisher |
| `.github/` | issue forms, PR templates, labels, workflows | |
| `tools/` | `check_links.py`, `build_wbs.py` | |

Repo `program-*` dan `proj-YYYY-topic` **tidak** dibuat di sini; konvensinya ada di README dan `research-os/08-templates/15-research-repository-template.md`.

## Konvensi penulisan

- Bahasa: **Bahasa Indonesia** untuk narasi; istilah teknis, nama file, label, ID dalam **English**.
- Nama folder/file: kebab-case dengan prefix nomor (`01-current-state-and-gaps.md`).
- Setiap dokumen `research-os/` diawali blok metadata blockquote: `**ID**`, `**Paket**`, `**Tier**`, `**Status**`, `**Audiens**`, `**Terkait**` (link relatif + ID).
- ID dokumen: `MST/STR/ARC/AIR/MET/AIX/OPS/GOV/TPL-NN`. ID task WBS: `OPS-NNN` (3 digit). Research ID: `UIAI-YYYY-NNN`; dataset `DS-`, publikasi `PUB-`, artefak `ART-`.
- Gate: G1 Endgame, G2 Problem, G3 Evidence, G4 Question, G5 Method, G6 Experiment, G7 Claim, G8 Contribution. Label `gate:G5-method` dst.
- Semua link internal **relatif**; jangan memakai URL absolut ke repo ini.
- Fakta institusional (akreditasi, kurikulum, benchmark kampus lain) berasal dari dokumen asal dan diberi catatan "verifikasi sebelum dokumen formal"; jangan menambah klaim baru. Data riil dosen/dataset memakai placeholder `[isi]`.
- Template harus *executable* (tabel/checklist/field), bukan narasi panjang.
- WBS: `research-os/06-execution-os/research-wbs.csv` adalah sumber; `01-research-wbs-master.md` dirender oleh `python3 tools/build_wbs.py`. Ubah CSV, lalu render ulang; jangan mengedit MD hasil render secara manual.

## Verifikasi sebelum commit

```bash
python3 tools/check_links.py            # 0 link/anchor relatif rusak
python3 tools/build_wbs.py --check      # MD sinkron dengan CSV, ID task unik, 8 gate terpakai
python3 -c "import yaml,glob;[yaml.safe_load(open(f)) for f in glob.glob('.github/**/*.yml',recursive=True)]"
```

## Yang jangan dilakukan

- Jangan memasukkan data mentah, data pribadi, atau PDF publisher ke repo.
- Jangan membuat label/topics di luar taksonomi `.github/labels.yml` dan `GOVERNANCE.md` tanpa memperbarui keduanya.
- Jangan mengubah definisi di glossary secara diam-diam; perubahan istilah harus diikuti pembaruan semua dokumen yang memakainya.
