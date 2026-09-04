# Dependency & Critical Path — Mana yang Paralel, Mana yang Blocking

> **ID** OPS-04 · **Paket** 06 Execution Operating System · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)
> **Audiens** Mahasiswa (lead tim), dosen pengampu, mentor, asisten studio
> **Terkait** [OPS-01 Research WBS](01-research-wbs-master.md) · [OPS-02 Weekly Sprints](02-weekly-sprints.md) · [OPS-03 Research Gates](03-research-gates.md) · [OPS-05 Student Weekly Playbook](05-student-weekly-playbook.md) · [MET-04 Research Pack](../04-metopen-research-studio/04-research-pack-specification.md) · [GOV-04 Risk Register](../07-governance/04-risk-register.md)

## Mengapa dokumen ini ada

Research WBS ([OPS-01](01-research-wbs-master.md)) memiliki kolom **Dependency**. Kolom itu bukan hiasan: ia menyandikan aturan epistemik riset ke dalam urutan kerja. *RQ tidak boleh dianggap validated sebelum evidence synthesis. Experiment tidak boleh jalan sebelum metric dan baseline defined.* Kalau urutan ini dilanggar, hasilnya bukan riset yang lebih cepat, melainkan riset yang harus diulang.

Dokumen ini menurunkan tiga hal dari kolom Dependency: (1) **critical path** — rangkaian task terpanjang dari S0 ke S16 yang menentukan durasi minimum semester; (2) **blocking rules** — task yang mengunci task lain; (3) **task paralel** — apa yang bisa dikerjakan bersamaan oleh anggota tim yang berbeda. Semua angka di sini dihitung langsung dari `research-wbs.csv` dengan skrip di bagian akhir; bila CSV berubah, jalankan ulang skrip dan perbarui dokumen ini.

## Critical path: 70 task, 154 jam

Critical path dihitung sebagai jalur terpanjang (menurut *Estimated Effort*) dalam graf ketergantungan. Dari 145 task, **70 task (154 dari 266 jam)** berada di jalur kritis. Artinya: kalau satu task di jalur ini terlambat satu hari, seluruh semester bergeser satu hari — kecuali slack sprint berikutnya menyerapnya.

```
S0  OPS-001 akun ─ OPS-002 baca playbook & protokol AI
      │
S1  OPS-007 sesi mindset ─ OPS-008 endgame ─ OPS-010 mentor/klaster ─ OPS-011 Issue problem
      │
S2  OPS-016 wawancara stakeholder ─ OPS-017 PROBLEM BRIEF ─ OPS-018 stakeholder ─ OPS-020 one-pager v0
      ─ OPS-021 Research ID ─ OPS-022 PR G2 ══════════════════════════════════════ ▶ G2 Problem Ready
      │
S3  OPS-026 SEARCH STRATEGY ─ OPS-027 pencarian ─ OPS-028 screening ─ OPS-029 chaining ─ OPS-030 verifikasi DOI
      │
S4  OPS-035 baca 8-12 ─ OPS-036 baca 8-12 lagi ─ OPS-038 pencarian pelengkap ─ OPS-039 verifikasi ulang .bib
      │
S5  OPS-043 POLA MATRIKS ─ OPS-044 literature map ─ OPS-045 kandidat gap ─ OPS-046 kelayakan
      ─ OPS-047 PR G3 ══════════════════════════════════════════════════════════ ▶ G3 Evidence Ready
      │
S6  OPS-051 gap final ─ OPS-052 RQ ─ OPS-053 contribution ─ OPS-054 uji RQ ─ OPS-055 one-pager v1
      ─ OPS-057 PR G4 ══════════════════════════════════════════════════════════ ▶ G4 Question Ready
      │
S7  OPS-060 pilih metode ─ OPS-061 variabel ─ OPS-062 DATA PLAN ─ OPS-066 design card
      │                                   (OPS-064 baseline ─ OPS-065 METRIK terkunci: paralel, tetapi mengunci S9)
S8  OPS-071 experiment card              (OPS-074 pitch ─ OPS-075 revisi ─ OPS-076 PR G5 ▶ G5 Method Ready: mengunci OPS-088)
      │
S9  OPS-079 environment+seed ─ OPS-080 pipeline data ─ OPS-082 METODE ─ OPS-083 run.sh ─ OPS-084 README ─ OPS-086 code review
      │
S10 OPS-088 PILOT ─ OPS-091 REPRODUKSI PEER ─ OPS-092 perbaiki README ─ OPS-094 PR G6 ═══ ▶ G6 Experiment Ready
      │
S11 OPS-097 EKSPERIMEN PENUH ─ OPS-098 statistik ─ OPS-099 error analysis ─ OPS-100 figur jujur ─ OPS-102 analysis.md
      │
S12 OPS-106 TABEL CER ─ OPS-107 threats v1 ─ OPS-108 contribution v2 ─ OPS-110 one-pager v2
      ─ OPS-111 PR G7 ══════════════════════════════════════════════════════════ ▶ G7 Claim Ready
      │
S13 OPS-116 hasil & pembahasan ─ OPS-119 rakit Research Pack ─ OPS-120 release v0.8
      │
S14 OPS-125 verifikasi sitasi & angka
      │
S15 OPS-131 REVISI ─ OPS-132 sinkron pack ─ OPS-133 INTEGRITY CHECKLIST
      │
S16 OPS-137 DEFENSE ─ OPS-138 revisi pasca-defense ─ OPS-140 HANDOFF ─ OPS-143 merge PR G8 ─ OPS-144 RELEASE v1.0
      ─ OPS-145 refleksi ══════════════════════════════════════════════════════ ▶ G8 Contribution Ready
```

Huruf kapital menandai **simpul kunci** — task dengan out-degree tinggi atau yang mewakili aturan epistemik. Dua hal yang perlu dibaca dari diagram:

- Jalur kritis melewati **empat PR gate** (G2, G3, G4, G7) dan berakhir pada PR G8. PR G5 dan G6 tidak berada pada jalur terpanjang menurut jam, tetapi keduanya adalah *blocking rule* (tabel berikut) — pilot (OPS-088) tidak boleh dijalankan sebelum PR G5 termerge, dan eksperimen penuh (OPS-097) tidak sebelum PR G6.
- Rantai terpanjang berada di **S3–S5** (literatur, 38.5 jam kritis) dan **S9–S11** (kode–pilot–eksperimen, 43 jam kritis). Dua blok inilah yang menentukan apakah semester selesai tepat waktu.

## Blocking rules

Aturan di bawah adalah *dependency* yang mewakili prinsip riset, bukan sekadar urutan administratif. Reviewer gate memeriksa aturan ini; melanggarnya berarti gate gagal ([OPS-03](03-research-gates.md)).

| # | Aturan | Task yang mengunci | Task yang dikunci | Mengapa |
|---|---|---|---|---|
| B1 | **Masalah dulu, solusi kemudian.** Problem Brief tidak menyebut algoritma; RQ dan metode menunggu G2. | OPS-013 (PR G1) → OPS-017; OPS-022 (PR G2) → OPS-026 | search strategy, semua task G3 | Pencarian literatur yang dilakukan sebelum masalah jelas menghasilkan daftar paper tentang *algoritma*, bukan tentang *masalah*. |
| B2 | **Setiap referensi diverifikasi sebelum dipakai.** | OPS-030, OPS-039 | OPS-035/036 (ekstraksi), OPS-043 (pola), OPS-047 (PR G3) | Satu referensi yang tidak dapat diverifikasi = G3 gagal. Sumber hasil AI diverifikasi sebelum masuk matriks. |
| B3 | **RQ tidak validated sebelum evidence synthesis.** | OPS-047 (PR G3) → OPS-051; OPS-046 → OPS-051 | gap final, RQ (OPS-052), contribution (OPS-053), PR G4 | RQ yang lahir sebelum matriks selesai hanyalah preferensi; ia tidak dapat ditelusuri ke baris matriks. |
| B4 | **Metode menunggu RQ.** | OPS-057 (PR G4) → OPS-060 | pemilihan metode, variabel, data plan, design card | Metode dipilih karena mampu menjawab RQ, bukan sebaliknya. |
| B5 | **Experiment tidak jalan sebelum metric dan baseline defined.** | OPS-064 (baseline), OPS-065 (metrik terkunci) → OPS-071, OPS-081; OPS-076 (PR G5) → OPS-088 | experiment card, kode baseline/evaluasi, pilot | Metrik yang dipilih setelah melihat hasil = mengubah metrik setelah melihat hasil (pelanggaran amanah epistemik). |
| B6 | **Reproduksi oleh peer sebelum G6.** | OPS-091 → OPS-092 → OPS-094 | PR G6, eksperimen penuh (OPS-097) | Hasil yang hanya ada di laptop anggota tim bukan bukti. |
| B7 | **Eksperimen penuh menunggu pilot lulus.** | OPS-093 (keputusan pilot), OPS-094 (PR G6) → OPS-097 | seluruh S11 | Menjalankan skala penuh pada desain yang belum terbukti viabel membuang jam paling mahal di semester. |
| B8 | **Klaim menunjuk bukti; threats diperbarui setelah hasil.** | OPS-102 → OPS-106 (CER) → OPS-107 (threats v1) → OPS-108 (contribution v2) | PR G7 | Threats to validity yang ditulis sebelum eksperimen (v0) belum tahu apa yang benar-benar terjadi. |
| B9 | **Manuscript tidak sebelum Claim Ready.** | OPS-111 (PR G7) → OPS-116, OPS-119 | Hasil & Pembahasan, Research Pack v0.8, release v0.8 | Menulis pembahasan sebelum klaim lolos review menghasilkan naskah yang membela hipotesis, bukan melaporkan bukti. |
| B10 | **Defense tidak sebelum integrity checklist dan AI usage statement.** | OPS-118 (AI Usage Statement), OPS-125 (verifikasi sitasi/angka), OPS-133 (integrity checklist) → OPS-137 | defense, merge PR G8, release v1.0 | Research Integrity Gate bersifat lulus/gagal; ia diperiksa *sebelum* penguji mendengar pitch. |
| B11 | **Release v1.0 hanya setelah handoff dan merge G8.** | OPS-140 (handoff), OPS-143 (merge PR G8) → OPS-144 | release v1.0 | Research Pack tanpa handoff tidak dapat diwariskan ke TA/mentor/AI Center. |

Aturan "lunak" yang juga tercermin di CSV: AI Usage Log diperbarui **setiap sprint** (OPS-006 → 014 → 023 → … → 139) sehingga AI Usage Statement (OPS-118) tidak dapat ditulis dari ingatan; dan One-Pager berjalan v0 → v1 → v2 (OPS-012/020 → 055 → 110) mengikuti gate, bukan ditulis sekali di akhir.

## Task yang bisa paralel per sprint

Task **paralel** = task yang semua dependency-nya sudah selesai di sprint sebelumnya, sehingga dapat dimulai hari pertama oleh anggota berbeda. Task **berantai** = harus menunggu task lain dalam sprint yang sama. Data dari skrip di bawah.

| Sprint | Boleh dimulai Senin (paralel) | Berantai dalam sprint | Pola kerja yang disarankan |
|---|---|---|---|
| S0 | OPS-001 | 002 → 003 → 004 → 005 → 006 | Satu orang bisa menyelesaikan semuanya dalam sehari; jangan tunggu W1. |
| S1 | OPS-007 | 008 → 009/010 → 011 → 012 → 013; 014 | Setelah OPS-008, pecah: satu orang OPS-009, satu orang OPS-010. |
| S2 | OPS-015, OPS-016 | 017 → 018/019 → 020 → 021 → 022; 023 | Janji wawancara (016) dibuat di W1. OPS-018 dan OPS-019 paralel setelah Problem Brief. |
| S3 | OPS-024 | 025 → 026 → 027 → 028 → 029 → 030; 031; 032 | Hampir sepenuhnya berantai — sprint dengan slack terkecil kedua. Bagi *query* antar anggota di OPS-027. |
| S4 | OPS-033 | 034 → 035 → 036/037 → 038 → 039; 040; 041 | OPS-035 dan OPS-036 dibagi per anggota (paralel dalam task); OPS-037 dan OPS-040 dapat dikerjakan orang ketiga. |
| S5 | OPS-042, OPS-043 | 044 → 045 → 046 → 047/048; 049 | OPS-043 dimulai Senin karena matriks sudah lengkap. |
| S6 | OPS-050, OPS-051 | 052 → 053/056 → 054 → 055 → 057; 058 | Berpikir bersama pada OPS-052; setelah itu paralel. |
| S7 | OPS-059 | 060 → 061 → 062 → 063; 060 → 064 → 065; 061/062/064/065 → 066 → 067; 068 | Dua jalur paralel: **data** (061 → 062 → 063) dan **evaluasi** (064 → 065). Bertemu di design card (066). |
| S8 | OPS-069, OPS-070, OPS-071 | 072 → 074 → 075 → 076; 073 → 074; 077 | Slack terbesar (15 jam). OPS-070 (ethics) dan OPS-073 (red team tim lain) benar-benar independen. |
| S9 | OPS-078 | 079 → 080 → 081/082 → 083 → 084 → 086; 085 | Setelah OPS-080, pecah: satu orang baseline (081), satu orang metode (082). |
| S10 | OPS-087, OPS-088 | 088 → 089/090/091 → 092/093 → 094; 095 | Setelah pilot berjalan, tiga task (089, 090, 091) paralel; 091 dikerjakan **peer**, bukan tim. |
| S11 | OPS-096, OPS-097 | 097 → 098 → 099/101/104 → 100 → 102; 103 | Eksperimen penuh (097) dimulai Senin karena PR G6 sudah merge; sambil menunggu run, kerjakan 096 dan siapkan 101. |
| S12 | OPS-105 | 106 → 107 → 108 → 109/110 → 111; 112 | Berantai; tetapi tiap task pendek. |
| S13 | OPS-113, OPS-118 | 114/115/116/117 → 119 → 120; 121 | Empat bagian tulisan (114–117) paralel per anggota; slack 13 jam. |
| S14 | OPS-122, OPS-124, OPS-125, OPS-126, OPS-127 | 123; 124 → 128; 129 | Sprint paling paralel: lima task bisa dimulai Senin. |
| S15 | OPS-130, OPS-131 | 131 → 132 → 133; 130 → 134 → 135; 136 | Dua jalur: **naskah** (131 → 132 → 133) dan **defense** (134 → 135). |
| S16 | OPS-137 | 138 → 139/140/141/142 → 143 → 144 → 145 | Setelah revisi pasca-defense, empat task administrasi paralel. |

## Slack dan buffer

Slack sprint = total jam sprint − jam task kritis di sprint itu. Slack besar berarti banyak pekerjaan paralel yang *tidak* menahan semester; slack kecil berarti sprint rapuh.

| Sprint | Jam total | Jam kritis | Slack | Kerapuhan |
|---|---|---|---|---|
| S0 | 8 | 3 | 5 | rendah |
| S1 | 9.5 | 6 | 3.5 | rendah |
| S2 | 14 | 10.5 | 3.5 | sedang — bergantung jadwal stakeholder |
| S3 | 16.5 | 12 | 4.5 | **tinggi** — rantai 5 task berurutan |
| S4 | 22 | 15.5 | 6.5 | **tinggi** — jam terbesar kedua |
| S5 | 15 | 11 | 4 | sedang |
| S6 | 12 | 9 | 3 | sedang — jam kecil, tetapi menunggu review G3 |
| S7 | 17 | 8 | 9 | rendah |
| S8 | 16.5 | 1.5 | 15 | rendah — tetapi jadwal pitch tidak bisa digeser |
| S9 | 24 | 17 | 7 | **tinggi** — jam terbesar, rantai kode |
| S10 | 16 | 9 | 7 | sedang — bergantung ketersediaan peer reproducer |
| S11 | 22.5 | 17 | 5.5 | **tinggi** — waktu komputasi eksperimen penuh |
| S12 | 12 | 8 | 4 | sedang |
| S13 | 19.5 | 6.5 | 13 | rendah |
| S14 | 15 | 2 | 13 | rendah — bergantung tim lain mengirim review |
| S15 | 14 | 8.5 | 5.5 | sedang |
| S16 | 12.5 | 9.5 | 3 | sedang — jadwal defense tetap |

Buffer yang sengaja disediakan dalam desain:

1. **S8 (slack 15 jam)** adalah buffer untuk S3–S7. Tim yang tertinggal di literatur atau desain memakai S8 untuk mengejar, sambil tetap mengikuti pitch.
2. **S13–S14 (slack 13 + 13 jam)** adalah buffer untuk S9–S12. Menulis dari artefak yang sudah ada memang lebih cepat daripada yang dibayangkan mahasiswa; jam itu bisa dipakai untuk mengulang eksperimen yang belum stabil.
3. **Waktu komputasi** di S11 (OPS-097) tidak dihitung sebagai jam kerja. Jalankan run panjang pada Senin malam agar Selasa sudah ada hasil.
4. Task **AI Usage Log + jurnal** (0.5–1 jam/sprint) tidak pernah menjadi buffer. Ia tetap dikerjakan meski sprint tertinggal.

## Jika satu gate terlambat

Gate berurutan, jadi keterlambatan tidak dapat "dilewati". Skenario pemulihan di bawah dirancang agar tim tetap lolos G8 pada W16 tanpa mengorbankan integritas.

| Gate terlambat | Gejala | Pemulihan | Yang tidak boleh dilakukan |
|---|---|---|---|
| **G2 (S2) terlambat 1 minggu** | Stakeholder belum bisa diwawancara; Problem Brief masih solution-first. | Ganti wawancara dengan telaah dokumen resmi + 1 wawancara singkat daring; kerjakan OPS-025 (kata kunci) dari draft Problem Brief; PR G2 dan search strategy (OPS-026) selesai di S3; pakai slack S3–S4 dengan membagi bacaan ke 3 orang. | Memulai pencarian literatur dengan kata kunci algoritma. |
| **G3 (S5) terlambat 1 minggu** | Matriks < 15 sumber; masih ada DOI tak terverifikasi. | Kurangi ke 15 sumber berkualitas tinggi (OPS-040 menjadi kriteria pemangkasan); PR G3 di S6; RQ (OPS-052) ditulis sebagai *draft bersyarat* tetapi **tidak** diajukan sebagai PR G4 sampai G3 merge; S7 dan S8 digabung (slack 24 jam). | Membuka PR G4 sebelum G3 merge; menambah sumber tanpa membaca. |
| **G3 terlambat 2 minggu** | Sama, lebih parah. | Dosen mengaktifkan opsi *gap cadangan* yang lebih sempit (OPS-046); pilot (S10) disusutkan menjadi baseline + 1 pembanding pada subset kecil; tulis manuscript sebagai **proposal TA** saja (tanpa manuscript paper). | Mengklaim gap yang tidak ditelusuri ke matriks. |
| **G5 (S8) terlambat** | Metrik/baseline belum terkunci saat W9; red team belum dilakukan. | Kunci baseline trivial dan metrik utama dulu (OPS-064/065) — cukup untuk memulai OPS-079/080 (environment, data pipeline) yang tidak membutuhkan metode; red team dilakukan asinkron via PR comment; PR G5 merge sebelum OPS-088. | Menjalankan pilot dengan metrik "sementara". |
| **G6 (S10) terlambat** | Pilot gagal berjalan atau peer tidak bisa mereproduksi. | Turunkan skala: subset lebih kecil, 3 seed; prioritaskan reproducibility README daripada hasil bagus; peer reproducer dari asisten studio bila tim lain sibuk; eksperimen penuh (OPS-097) dipangkas ke kondisi minimum yang menjawab RQ utama saja. | Melaporkan hasil pilot yang hanya ada di laptop; melewati OPS-091. |
| **G7 (S12) terlambat** | Hasil belum stabil; CER belum menunjuk figur. | Terima hasil apa adanya — termasuk **hasil negatif** — dan tulis CER dengan confidence rendah; threats v1 menjadi bagian terkuat naskah; S13 memakai slack 13 jam untuk menulis. Riset dengan hasil negatif yang jujur tetap lolos G7. | Mengubah metrik, membuang seed yang buruk, atau memperhalus figur. |
| **G8 (S16) terancam** | Revisi belum selesai; checklist belum ditandatangani. | Prioritas mutlak: OPS-125 (verifikasi sitasi/angka) → OPS-133 (integrity) → OPS-137 (defense). Handoff (OPS-140) boleh diisi *setelah* defense dengan bagian *missing evidence* yang jujur; release v1.0 boleh mundur ke minggu ujian. | Defense tanpa checklist; release v1.0 dengan komponen kosong. |

Aturan umum pemulihan: **kurangi skala, jangan kurangi integritas.** Ruang lingkup RQ boleh menyempit, jumlah sumber boleh turun ke batas minimum, eksperimen boleh mengecil — tetapi verifikasi referensi, metrik terkunci, reproduksi peer, dan AI disclosure tidak pernah dipangkas.

## Pelajaran project & research management untuk mahasiswa

1. **Dependency adalah argumen, bukan birokrasi.** Setiap panah di WBS menjawab "mengapa ini harus lebih dulu?". Kalau Anda tidak bisa menjawabnya, Anda belum memahami risetnya.
2. **Critical path memberi tahu di mana harus khawatir.** Dari 145 task, hanya 70 yang menentukan tanggal selesai. Task lain penting untuk kualitas, tetapi tidak untuk jadwal. Ketika waktu sempit, lihat kolom *Jam kritis*, bukan daftar task.
3. **Paralel bukan berarti sendiri-sendiri.** Task paralel dibagi antar anggota, tetapi *Human Check*-nya tetap silang: yang membaca sumber diperiksa oleh yang tidak membacanya; yang menulis kode direproduksi oleh yang tidak menulisnya.
4. **Slack itu untuk dipakai, bukan dihabiskan.** S8 dan S13–S14 longgar karena S3–S5 dan S9–S11 sempit. Tim yang menghabiskan S8 untuk "istirahat" akan menemukan tidak ada buffer lagi di S9.
5. **Gate yang gagal lebih murah daripada gate yang dilompati.** PR yang ditolak di G4 menghabiskan satu minggu; RQ yang salah dan baru ketahuan di G7 menghabiskan sepuluh minggu.
6. **Jam yang paling mahal adalah jam komputasi dan jam orang lain.** Wawancara stakeholder (S2), peer reproducer (S10), reviewer (S14), dan penguji (S16) tidak bisa dipercepat oleh Anda; jadwalkan mereka lebih awal daripada yang terasa perlu.
7. **Setiap skenario pemulihan menyusutkan ruang lingkup, bukan kejujuran.** Itulah bedanya manajemen riset dengan manajemen proyek biasa: deliverable boleh mengecil, klaim boleh menyempit, tetapi bukti tidak boleh dipoles.

## Skrip: menghitung critical path dari CSV

Skrip berikut hanya memakai pustaka standar Python 3. Jalankan dari root repo. Ia menghitung jalur terpanjang menurut *Estimated Effort*, task yang boleh dimulai di awal sprint, dan slack per sprint — semua angka pada dokumen ini berasal darinya.

```python
#!/usr/bin/env python3
"""Critical path Research WBS dari research-os/06-execution-os/research-wbs.csv."""
import csv
from collections import OrderedDict

rows = list(csv.DictReader(open("research-os/06-execution-os/research-wbs.csv", encoding="utf-8")))
ids = [r["Task ID"] for r in rows]
eff = {r["Task ID"]: float(r["Estimated Effort"].rstrip("h")) for r in rows}
deps = {r["Task ID"]: [] if r["Dependency"] == "-" else r["Dependency"].split(";") for r in rows}
sprint = {r["Task ID"]: r["Sprint"] for r in rows}
order = {f"S{i}": i for i in range(17)}

# Jalur terpanjang (DAG; CSV menjamin dependency selalu bernomor lebih kecil)
best, prev = {}, {}
for t in ids:
    cands = [(best[d], d) for d in deps[t]]
    best[t] = (max(cands)[0] if cands else 0.0) + eff[t]
    prev[t] = max(cands)[1] if cands else None
end = max(ids, key=best.get)
path, cur = [], end
while cur:
    path.append(cur)
    cur = prev[cur]
path.reverse()
cp = set(path)
print(f"Critical path: {len(path)} task, {best[end]:g} jam dari {sum(eff.values()):g} jam")
print(" -> ".join(path))

# Paralel-start vs berantai, dan slack per sprint
by = OrderedDict()
for t in ids:
    by.setdefault(sprint[t], []).append(t)
for s, ts in by.items():
    start = [t for t in ts if all(order[sprint[d]] < order[s] for d in deps[t])]
    total = sum(eff[t] for t in ts)
    crit = sum(eff[t] for t in ts if t in cp)
    print(f"{s}: total={total:g}h kritis={crit:g}h slack={total-crit:g}h "
          f"mulai-Senin={start} kritis={[t for t in ts if t in cp]}")
```

Hasil aktual (dijalankan pada `research-wbs.csv` Draft v0.1, 145 task, 266 jam):

```
Critical path: 70 task, 154 jam dari 266 jam
OPS-001 -> OPS-002 -> OPS-007 -> OPS-008 -> OPS-010 -> OPS-011 -> OPS-016 -> OPS-017 -> OPS-018
-> OPS-020 -> OPS-021 -> OPS-022 -> OPS-026 -> OPS-027 -> OPS-028 -> OPS-029 -> OPS-030 -> OPS-035
-> OPS-036 -> OPS-038 -> OPS-039 -> OPS-043 -> OPS-044 -> OPS-045 -> OPS-046 -> OPS-047 -> OPS-051
-> OPS-052 -> OPS-053 -> OPS-054 -> OPS-055 -> OPS-057 -> OPS-060 -> OPS-061 -> OPS-062 -> OPS-066
-> OPS-071 -> OPS-079 -> OPS-080 -> OPS-082 -> OPS-083 -> OPS-084 -> OPS-086 -> OPS-088 -> OPS-091
-> OPS-092 -> OPS-094 -> OPS-097 -> OPS-098 -> OPS-099 -> OPS-100 -> OPS-102 -> OPS-106 -> OPS-107
-> OPS-108 -> OPS-110 -> OPS-111 -> OPS-116 -> OPS-119 -> OPS-120 -> OPS-125 -> OPS-131 -> OPS-132
-> OPS-133 -> OPS-137 -> OPS-138 -> OPS-140 -> OPS-143 -> OPS-144 -> OPS-145
S0:  total=8h    kritis=3h    slack=5h    mulai-Senin=[OPS-001]
S1:  total=9.5h  kritis=6h    slack=3.5h  mulai-Senin=[OPS-007]
S2:  total=14h   kritis=10.5h slack=3.5h  mulai-Senin=[OPS-015, OPS-016]
S3:  total=16.5h kritis=12h   slack=4.5h  mulai-Senin=[OPS-024]
S4:  total=22h   kritis=15.5h slack=6.5h  mulai-Senin=[OPS-033]
S5:  total=15h   kritis=11h   slack=4h    mulai-Senin=[OPS-042, OPS-043]
S6:  total=12h   kritis=9h    slack=3h    mulai-Senin=[OPS-050, OPS-051]
S7:  total=17h   kritis=8h    slack=9h    mulai-Senin=[OPS-059]
S8:  total=16.5h kritis=1.5h  slack=15h   mulai-Senin=[OPS-069, OPS-070, OPS-071]
S9:  total=24h   kritis=17h   slack=7h    mulai-Senin=[OPS-078]
S10: total=16h   kritis=9h    slack=7h    mulai-Senin=[OPS-087, OPS-088]
S11: total=22.5h kritis=17h   slack=5.5h  mulai-Senin=[OPS-096, OPS-097]
S12: total=12h   kritis=8h    slack=4h    mulai-Senin=[OPS-105]
S13: total=19.5h kritis=6.5h  slack=13h   mulai-Senin=[OPS-113, OPS-118]
S14: total=15h   kritis=2h    slack=13h   mulai-Senin=[OPS-122, OPS-124, OPS-125, OPS-126, OPS-127]
S15: total=14h   kritis=8.5h  slack=5.5h  mulai-Senin=[OPS-130, OPS-131]
S16: total=12.5h kritis=9.5h  slack=3h    mulai-Senin=[OPS-137]
```

Task paling banyak mengunci task lain (out-degree): OPS-017 Problem Brief (6), OPS-106 tabel CER (5), OPS-113 sesi writing (5), lalu OPS-011, OPS-036, OPS-044, OPS-052, OPS-064, OPS-066, OPS-088, OPS-098, OPS-107 (masing-masing 4). Inilah task yang, bila terlambat, menahan paling banyak pekerjaan lain — dan karena itu wajib dibagi ke anggota yang paling andal.

Catatan: pemodelan ini memakai jam kerja tim sebagai bobot dan mengabaikan waktu tunggu eksternal (review dosen, jadwal stakeholder, waktu komputasi). Dalam praktik, waktu tunggu itulah yang paling sering menggeser jadwal; karena itu setiap PR gate diminta review pada hari yang sama saat dibuka.
