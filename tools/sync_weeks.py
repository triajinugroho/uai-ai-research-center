#!/usr/bin/env python3
"""Sinkronkan tabel "## Tasks" pada halaman mingguan Metopen dengan research-wbs.csv.

Sumber kebenaran task adalah research-os/06-execution-os/research-wbs.csv. Halaman
metopen-research-studio/weeks/week-NN-*.md memuat tabel task Sprint S<NN>; skrip ini
merender ulang tabel itu (kolom Task ID | Task | Output | Effort | AI Assist | Human Check)
dan baris "Total effort" dari CSV, tanpa menyentuh bagian lain halaman.

Pemakaian (dari root repo):
    python3 tools/sync_weeks.py            # tulis ulang tabel yang berbeda
    python3 tools/sync_weeks.py --check    # hanya periksa; exit 1 bila ada yang tidak sinkron
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "research-os" / "06-execution-os" / "research-wbs.csv"
WEEKS = ROOT / "metopen-research-studio" / "weeks"
HEADER = "| Task ID | Task | Output | Effort | AI Assist | Human Check |"
SEP = "|---|---|---|---|---|---|"


def esc(s: str) -> str:
    return s.replace("|", "\\|").strip()


def load_tasks():
    by_sprint = {}
    with CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            by_sprint.setdefault(row["Sprint"], []).append(row)
    return by_sprint


def render_table(rows):
    lines = [HEADER, SEP]
    total = 0
    for r in sorted(rows, key=lambda r: r["Task ID"]):
        eff = r["Estimated Effort"].strip()
        m = re.match(r"(\d+(?:\.\d+)?)h", eff)
        if m:
            total += float(m.group(1))
        lines.append(
            "| {} | {} | {} | {} | {} | {} |".format(
                r["Task ID"], esc(r["Task"]), esc(r["Output"]), esc(eff),
                esc(r["AI Assistance"]), esc(r["Human Validation"]),
            )
        )
    total_s = str(int(total)) if total == int(total) else str(total)
    lines.append("")
    lines.append(f"**Total effort: {total_s}h**")
    return "\n".join(lines), total_s


def sync_file(path: Path, rows, check: bool):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Tasks\s*\n(.*?)(?=^## )", text, flags=re.S | re.M)
    if not m:
        return f"{path.name}: bagian '## Tasks' tidak ditemukan", False
    section = m.group(1)
    # Tabel = blok baris yang diawali '|' ; baris Total effort = baris yang memuat 'Total effort'
    tbl = re.search(r"((?:^\|.*\n?)+)", section, flags=re.M)
    tot = re.search(r"^.*Total effort.*$", section, flags=re.M)
    if not tbl or not tot:
        return f"{path.name}: tabel atau baris 'Total effort' tidak ditemukan", False
    new_table, _ = render_table(rows)
    new_tbl_part, new_tot_line = new_table.split("\n\n", 1)
    new_section = section[: tbl.start(1)] + new_tbl_part + "\n" + section[tbl.end(1):]
    # Ganti hanya token "**Total effort: Xh**"; komentar setelahnya dipertahankan.
    new_section = re.sub(r"\*\*Total effort:\s*[\d.,]+\s*h\*\*", new_tot_line, new_section, count=1)
    if new_section == section:
        return f"{path.name}: sinkron", True
    if check:
        return f"{path.name}: TIDAK sinkron dengan CSV", False
    text = text[: m.start(1)] + new_section + text[m.end(1):]
    path.write_text(text, encoding="utf-8")
    return f"{path.name}: diperbarui", True


def main():
    check = "--check" in sys.argv
    by_sprint = load_tasks()
    ok = True
    files = sorted(WEEKS.glob("week-*.md"))
    if not files:
        print("Tidak ada halaman mingguan.")
        sys.exit(1)
    for path in files:
        n = int(re.match(r"week-(\d\d)", path.name).group(1))
        rows = by_sprint.get(f"S{n}", [])
        if not rows:
            print(f"{path.name}: tidak ada task Sprint S{n} di CSV")
            ok = False
            continue
        msg, good = sync_file(path, rows, check)
        print(msg)
        ok = ok and good
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
