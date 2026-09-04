#!/usr/bin/env python3
"""build_wbs.py — validasi research-wbs.csv dan render 01-research-wbs-master.md.

Pemakaian (dari root repo):
    python3 tools/build_wbs.py          # validasi + render MD
    python3 tools/build_wbs.py --check  # validasi + bandingkan MD yang ada (CI)

Sumber data: research-os/06-execution-os/research-wbs.csv
Hasil render: research-os/06-execution-os/01-research-wbs-master.md
Hanya memakai pustaka standar Python 3.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "research-os" / "06-execution-os" / "research-wbs.csv"
MD_PATH = ROOT / "research-os" / "06-execution-os" / "01-research-wbs-master.md"

HEADER = [
    "Task ID", "Sprint", "Gate", "Task", "Description", "Input", "Action", "Output",
    "Evidence", "Dependency", "Estimated Effort", "AI Assistance", "Human Validation", "Status",
]

# Tema sprint (S0 onboarding, S1..S16 = minggu 1..16 Metopen)
SPRINT_THEME: "OrderedDict[str, str]" = OrderedDict([
    ("S0", "Onboarding"),
    ("S1", "W1 Endgame"),
    ("S2", "W2 Problem"),
    ("S3", "W3 Search"),
    ("S4", "W4 Evidence"),
    ("S5", "W5 Gap"),
    ("S6", "W6 RQ"),
    ("S7", "W7 Method"),
    ("S8", "W8 Design Defense"),
    ("S9", "W9 Repository"),
    ("S10", "W10 Pilot"),
    ("S11", "W11 Analysis"),
    ("S12", "W12 Contribution"),
    ("S13", "W13 Manuscript"),
    ("S14", "W14 Peer Review"),
    ("S15", "W15 Revision"),
    ("S16", "W16 Defense"),
])

GATE_NAME = {
    "G1": "Endgame Ready", "G2": "Problem Ready", "G3": "Evidence Ready",
    "G4": "Question Ready", "G5": "Method Ready", "G6": "Experiment Ready",
    "G7": "Claim Ready", "G8": "Contribution Ready",
}

# Gate yang seharusnya dikejar tiap sprint (OPS-03 peta gate terhadap semester)
SPRINT_GATE = {
    "S0": "G1", "S1": "G1", "S2": "G2", "S3": "G3", "S4": "G3", "S5": "G3",
    "S6": "G4", "S7": "G5", "S8": "G5", "S9": "G6", "S10": "G6",
    "S11": "G7", "S12": "G7", "S13": "G8", "S14": "G8", "S15": "G8", "S16": "G8",
}

TASK_ID_RE = re.compile(r"^OPS-(\d{3})$")
EFFORT_RE = re.compile(r"^(\d+(?:\.\d+)?)h$")
MIN_PER_SPRINT, MAX_PER_SPRINT = 5, 10
OPTIONAL_DASH = {"Dependency", "AI Assistance"}


class WbsError(Exception):
    pass


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise WbsError(f"CSV tidak ditemukan: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise WbsError("CSV kosong")
        if header != HEADER:
            raise WbsError(
                "Header CSV tidak sesuai.\n  diharapkan: " + ",".join(HEADER)
                + "\n  ditemukan : " + ",".join(header)
            )
        rows = []
        for n, rec in enumerate(reader, start=2):
            if not rec or all(c.strip() == "" for c in rec):
                continue
            if len(rec) != len(HEADER):
                raise WbsError(f"Baris {n}: jumlah kolom {len(rec)}, diharapkan {len(HEADER)}")
            rows.append({k: v.strip() for k, v in zip(HEADER, rec)})
    return rows


def validate(rows: list[dict[str, str]]) -> list[str]:
    """Kembalikan daftar pesan error (kosong = valid)."""
    errors: list[str] = []
    ids: list[str] = []
    for i, r in enumerate(rows, start=1):
        tid = r["Task ID"]
        m = TASK_ID_RE.match(tid)
        if not m:
            errors.append(f"{tid or '(kosong)'}: format Task ID harus OPS-NNN")
            continue
        if int(m.group(1)) != i:
            errors.append(f"{tid}: nomor tidak berurutan (diharapkan OPS-{i:03d})")
        ids.append(tid)

    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        errors.append("Task ID duplikat: " + ", ".join(sorted(dup)))
    id_set = set(ids)

    for r in rows:
        tid = r["Task ID"]
        for col in HEADER:
            val = r[col]
            if val == "":
                errors.append(f"{tid}: kolom '{col}' kosong")
            elif val == "-" and col not in OPTIONAL_DASH:
                errors.append(f"{tid}: kolom '{col}' tidak boleh '-'")
        if r["Sprint"] not in SPRINT_THEME:
            errors.append(f"{tid}: Sprint '{r['Sprint']}' tidak dikenal (S0..S16)")
        if r["Gate"] not in GATE_NAME:
            errors.append(f"{tid}: Gate '{r['Gate']}' tidak dikenal (G1..G8)")
        elif r["Sprint"] in SPRINT_GATE and SPRINT_GATE[r["Sprint"]] != r["Gate"]:
            errors.append(
                f"{tid}: Sprint {r['Sprint']} seharusnya mengejar {SPRINT_GATE[r['Sprint']]}, "
                f"bukan {r['Gate']}"
            )
        if len(r["Task"]) > 70:
            errors.append(f"{tid}: judul Task {len(r['Task'])} karakter (> 70)")
        if not EFFORT_RE.match(r["Estimated Effort"]):
            errors.append(f"{tid}: Estimated Effort '{r['Estimated Effort']}' harus berformat angka + 'h' (mis. 2h)")
        if r["Status"] != "Planned":
            errors.append(f"{tid}: Status '{r['Status']}' (diharapkan 'Planned')")
        dep = r["Dependency"]
        if dep != "-":
            m = TASK_ID_RE.match(tid)
            own = int(m.group(1)) if m else 0
            for d in [x.strip() for x in dep.split(";")]:
                dm = TASK_ID_RE.match(d)
                if not dm:
                    errors.append(f"{tid}: Dependency '{d}' bukan Task ID")
                elif d not in id_set:
                    errors.append(f"{tid}: Dependency '{d}' tidak ada di CSV")
                elif int(dm.group(1)) >= own:
                    errors.append(f"{tid}: Dependency '{d}' harus bernomor lebih kecil")

    per_sprint = Counter(r["Sprint"] for r in rows)
    for s in SPRINT_THEME:
        n = per_sprint.get(s, 0)
        if not MIN_PER_SPRINT <= n <= MAX_PER_SPRINT:
            errors.append(f"Sprint {s}: {n} task (harus {MIN_PER_SPRINT}-{MAX_PER_SPRINT})")
    used_gates = {r["Gate"] for r in rows}
    for g in GATE_NAME:
        if g not in used_gates:
            errors.append(f"Gate {g} tidak dipakai oleh task mana pun")
    # urutan sprint harus monoton (task sprint lebih awal bernomor lebih kecil)
    order = {s: i for i, s in enumerate(SPRINT_THEME)}
    last = -1
    for r in rows:
        if r["Sprint"] in order:
            cur = order[r["Sprint"]]
            if cur < last:
                errors.append(f"{r['Task ID']}: sprint {r['Sprint']} muncul setelah sprint yang lebih akhir")
            last = max(last, cur)
    return errors


def effort_hours(v: str) -> float:
    m = EFFORT_RE.match(v)
    return float(m.group(1)) if m else 0.0


def fmt_h(h: float) -> str:
    return f"{h:g}h"


def esc(s: str) -> str:
    return s.replace("|", "\\|")


def render(rows: list[dict[str, str]]) -> str:
    total_effort = sum(effort_hours(r["Estimated Effort"]) for r in rows)
    by_sprint: "OrderedDict[str, list[dict[str, str]]]" = OrderedDict((s, []) for s in SPRINT_THEME)
    for r in rows:
        by_sprint[r["Sprint"]].append(r)
    per_gate = Counter(r["Gate"] for r in rows)
    effort_gate = Counter()
    for r in rows:
        effort_gate[r["Gate"]] += effort_hours(r["Estimated Effort"])

    L: list[str] = []
    L.append("# Research WBS Master — ±145 Microtasks, 17 Sprint, 8 Gates")
    L.append("")
    L.append("> **ID** OPS-01 · **Paket** 06 Execution Operating System · **Tier** 3 (Execution Toolkit) · **Status** Draft v0.1 (2026-09)")
    L.append("> **Audiens** Mahasiswa, dosen pengampu, mentor")
    L.append("> **Terkait** [OPS-02 Weekly Sprints](02-weekly-sprints.md) · [OPS-03 Research Gates](03-research-gates.md) · [OPS-04 Dependency & Critical Path](04-dependency-and-critical-path.md) · [OPS-05 Student Weekly Playbook](05-student-weekly-playbook.md) · [MET-03 16-Week Blueprint](../04-metopen-research-studio/03-metopen-16-week-blueprint.md)")
    L.append("")
    L.append("> **FILE INI DIRENDER OTOMATIS dari `research-wbs.csv` oleh `tools/build_wbs.py` — jangan diedit manual.** Ubah CSV, lalu jalankan `python3 tools/build_wbs.py`; CI menjalankan `python3 tools/build_wbs.py --check`.")
    L.append("")
    L.append("## Apa ini")
    L.append("")
    L.append("Research WBS (Work Breakdown Structure) memecah satu *mini research cycle* Metopen — dari onboarding sampai release Research Pack v1.0 — menjadi microtask yang cukup kecil untuk dikerjakan dalam beberapa jam dan cukup konkret untuk diperiksa buktinya. Setiap task mengejar satu Research Gate ([OPS-03](03-research-gates.md)), berada dalam satu sprint mingguan ([OPS-02](02-weekly-sprints.md)), dan memiliki ketergantungan eksplisit ([OPS-04](04-dependency-and-critical-path.md)). Mahasiswa tidak membaca file ini secara langsung; mereka memakai halaman mingguan di [OPS-05](05-student-weekly-playbook.md) dan `metopen-research-studio/weeks/`. File ini adalah **backend**-nya.")
    L.append("")
    L.append("Sumber data: `research-wbs.csv` (145 baris, 14 kolom) — dapat dibuka langsung sebagai Google Sheet/Excel untuk tracker kelas ([TPL-02](../08-templates/02-research-mission-tracker-template.md)).")
    L.append("")
    L.append("## 14 kolom")
    L.append("")
    L.append("| Kolom | Arti |")
    L.append("|---|---|")
    L.append("| **Task ID** | `OPS-NNN`, 3 digit, berurutan OPS-001…OPS-145. Dipakai di commit, Issue, halaman mingguan. Bedakan dari ID dokumen `OPS-01`…`OPS-05`. |")
    L.append("| **Sprint** | `S0` onboarding; `S1`…`S16` = minggu 1–16 Metopen. |")
    L.append("| **Gate** | Research Gate yang sedang dikejar task ini (G1–G8). |")
    L.append("| **Task** | Judul singkat imperatif (≤ 70 karakter). |")
    L.append("| **Description** | 1–2 kalimat: apa dan mengapa. |")
    L.append("| **Input** | Dokumen/artefak/template yang dibutuhkan sebelum mulai. |")
    L.append("| **Action** | Langkah konkret, dipisah `;`. |")
    L.append("| **Output** | Artefak yang dihasilkan. |")
    L.append("| **Evidence** | Bukti yang dapat diperiksa reviewer: file, commit, Issue, PR, tabel, release. |")
    L.append("| **Dependency** | Task ID yang harus selesai lebih dulu (dipisah `;`), atau `-`. Selalu merujuk nomor lebih kecil. |")
    L.append("| **Estimated Effort** | Perkiraan jam kerja tim (`2h`). |")
    L.append("| **AI Assistance** | Apa yang boleh dibantu AI pada task ini sesuai [AIX-04](../05-ai-augmented-research/04-ai-research-protocol.md); `-` bila tidak ada. Setiap bantuan dicatat di AI Usage Log ([TPL-10](../08-templates/10-ai-usage-log-template.md)). |")
    L.append("| **Human Validation** | Apa yang wajib diverifikasi manusia (tim, peer, mentor, dosen) sebelum task dianggap selesai. |")
    L.append("| **Status** | `Planned` di master; tracker tim mengubahnya menjadi In Progress / Review / Done. |")
    L.append("")
    L.append("## Ringkasan per sprint")
    L.append("")
    L.append("| Sprint | Minggu / tema | Gate | Jumlah task | Task ID range | Total effort |")
    L.append("|---|---|---|---|---|---|")
    for s, tasks in by_sprint.items():
        if not tasks:
            continue
        gates = sorted({t["Gate"] for t in tasks})
        eff = sum(effort_hours(t["Estimated Effort"]) for t in tasks)
        rng = f"{tasks[0]['Task ID']}–{tasks[-1]['Task ID']}"
        L.append(f"| {s} | {SPRINT_THEME[s]} | {', '.join(gates)} | {len(tasks)} | {rng} | {fmt_h(eff)} |")
    L.append(f"| **Total** | 17 sprint | G1–G8 | **{len(rows)}** | OPS-001–OPS-{len(rows):03d} | **{fmt_h(total_effort)}** |")
    L.append("")
    L.append("---")
    L.append("")
    cols = ["Task ID", "Task", "Description", "Input", "Action", "Output", "Evidence",
            "Dependency", "Effort", "AI Assistance", "Human Validation", "Status"]
    for s, tasks in by_sprint.items():
        if not tasks:
            continue
        gates = sorted({t["Gate"] for t in tasks})
        gate_label = ", ".join(f"Gate {g}" for g in gates) if len(gates) > 1 else f"Gate {gates[0]}"
        L.append(f"## Sprint {s} — {SPRINT_THEME[s]} ({gate_label})")
        L.append("")
        eff = sum(effort_hours(t["Estimated Effort"]) for t in tasks)
        gname = " / ".join(f"{g} {GATE_NAME[g]}" for g in gates)
        L.append(f"{len(tasks)} task · total effort {fmt_h(eff)} · mengejar {gname}.")
        L.append("")
        L.append("| " + " | ".join(cols) + " |")
        L.append("|" + "---|" * len(cols))
        for t in tasks:
            cells = [
                t["Task ID"], t["Task"], t["Description"], t["Input"], t["Action"], t["Output"],
                t["Evidence"], t["Dependency"], t["Estimated Effort"], t["AI Assistance"],
                t["Human Validation"], t["Status"],
            ]
            L.append("| " + " | ".join(esc(c) for c in cells) + " |")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## Statistik")
    L.append("")
    L.append(f"- Total task: **{len(rows)}** (OPS-001–OPS-{len(rows):03d}), 17 sprint (S0–S16).")
    L.append(f"- Total estimated effort: **{fmt_h(total_effort)}** (±{total_effort / 16:.1f} jam per minggu per tim untuk 16 minggu).")
    L.append("")
    L.append("| Gate | Nama | Jumlah task | Total effort |")
    L.append("|---|---|---|---|")
    for g, name in GATE_NAME.items():
        L.append(f"| {g} | {name} | {per_gate.get(g, 0)} | {fmt_h(effort_gate.get(g, 0.0))} |")
    L.append("")
    L.append("Task per sprint: " + ", ".join(f"{s}={len(t)}" for s, t in by_sprint.items() if t) + ".")
    L.append("")
    return "\n".join(L) + "\n"


def stats_line(rows: list[dict[str, str]]) -> str:
    per_sprint = Counter(r["Sprint"] for r in rows)
    per_gate = Counter(r["Gate"] for r in rows)
    total = sum(effort_hours(r["Estimated Effort"]) for r in rows)
    return (
        f"{len(rows)} task, {fmt_h(total)} total; "
        + "sprint: " + " ".join(f"{s}={per_sprint.get(s, 0)}" for s in SPRINT_THEME) + "; "
        + "gate: " + " ".join(f"{g}={per_gate.get(g, 0)}" for g in GATE_NAME)
    )


def main(argv: list[str]) -> int:
    check = "--check" in argv
    try:
        rows = read_rows(CSV_PATH)
        errors = validate(rows)
    except WbsError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    if errors:
        print(f"Validasi research-wbs.csv GAGAL ({len(errors)} masalah):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    md = render(rows)
    if check:
        if not MD_PATH.exists():
            print(f"ERROR: {MD_PATH.relative_to(ROOT)} belum ada; jalankan python3 tools/build_wbs.py", file=sys.stderr)
            return 1
        current = MD_PATH.read_text(encoding="utf-8")
        if current != md:
            cur_lines, new_lines = current.splitlines(), md.splitlines()
            first = next((i for i, (a, b) in enumerate(zip(cur_lines, new_lines), 1) if a != b),
                         min(len(cur_lines), len(new_lines)) + 1)
            print(
                f"ERROR: {MD_PATH.relative_to(ROOT)} tidak sinkron dengan research-wbs.csv "
                f"(perbedaan pertama di baris {first}; {len(cur_lines)} vs {len(new_lines)} baris). "
                "Jalankan python3 tools/build_wbs.py lalu commit hasilnya.",
                file=sys.stderr,
            )
            return 1
        print("OK: research-wbs.csv valid dan 01-research-wbs-master.md sinkron.")
        print(stats_line(rows))
        return 0
    MD_PATH.write_text(md, encoding="utf-8")
    print(f"Rendered {MD_PATH.relative_to(ROOT)} dari {CSV_PATH.relative_to(ROOT)}.")
    print(stats_line(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
