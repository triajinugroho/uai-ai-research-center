#!/usr/bin/env python3
"""
check_links.py — Pemeriksa link & anchor relatif untuk seluruh file Markdown repository.

Dipakai oleh CONTRIBUTING.md §6, CLAUDE.md, dan workflow .github/workflows/docs-check.yml.
Hanya memakai pustaka standar Python 3.

Yang diperiksa
- Link inline  [teks](target)  dan gambar  ![alt](target)
- Definisi reference-style  [label]: target   (definisi footnote [^n]: diabaikan)
- Link di dalam code fence (``` / ~~~), inline code (`...`), dan komentar HTML diabaikan.
- Target eksternal (http://, https://, mailto:, tel:, skema lain, //host) diabaikan.
- Target relatif: query (?...) dan anchor (#...) dibuang, di-URL-decode, diresolve relatif
  terhadap direktori file (atau terhadap root bila diawali "/"); harus ada sebagai file/direktori.
- Target .md dengan #anchor, dan #anchor ke file sendiri: anchor dicocokkan dengan slug heading
  ala GitHub — lowercase; hapus karakter selain huruf/angka/underscore/spasi/hyphen (unicode aware);
  spasi → hyphen; heading duplikat diberi akhiran -1, -2, ...  Atribut id="..."/name="..." pada
  tag HTML juga diterima sebagai anchor.

Keluaran: satu baris "file:baris: target → alasan" per link rusak, lalu ringkasan jumlah file
dan link yang diperiksa. Exit code 1 bila ada link rusak, 0 bila bersih.

Penggunaan
    python3 tools/check_links.py                 # root = direktori induk dari tools/
    python3 tools/check_links.py --root PATH     # root lain
"""

import argparse
import os
import re
import sys
from urllib.parse import unquote

SKIP_DIRS = {".git", "node_modules"}
MD_EXT = (".md", ".markdown")

SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")  # http:, https:, mailto:, tel:, ...
FENCE_OPEN_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
ATX_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")
REF_DEF_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(?:<([^>]*)>|(\S+))")
HTML_ANCHOR_RE = re.compile(r"""<[A-Za-z][^>]*\s(?:id|name)\s*=\s*["']([^"']+)["']""")
INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)*?\1")
LINK_START_RE = re.compile(r"!?\[((?:[^\[\]\\]|\\.|\[[^\]]*\])*)\]\(")


# ---------------------------------------------------------------------------
# Pembersihan teks
# ---------------------------------------------------------------------------
def strip_html_comments(line, in_comment):
    """Buang isi komentar HTML pada satu baris; kembalikan (baris_bersih, status_komentar)."""
    out = []
    i = 0
    n = len(line)
    while i < n:
        if in_comment:
            j = line.find("-->", i)
            if j == -1:
                return "".join(out), True
            i = j + 3
            in_comment = False
        else:
            j = line.find("<!--", i)
            if j == -1:
                out.append(line[i:])
                break
            out.append(line[i:j])
            i = j + 4
            in_comment = True
    return "".join(out), in_comment


def iter_inline_links(line):
    """Hasilkan target dari setiap [teks](target) / ![alt](target) pada satu baris."""
    pos = 0
    n = len(line)
    while True:
        m = LINK_START_RE.search(line, pos)
        if not m:
            return
        i = m.end()
        while i < n and line[i] in " \t":
            i += 1
        if i < n and line[i] == "<":
            j = line.find(">", i + 1)
            if j == -1:
                pos = m.end()
                continue
            dest = line[i + 1:j]
            end = j + 1
        else:
            depth = 0
            j = i
            while j < n:
                c = line[j]
                if c == "\\":
                    j += 2
                    continue
                if c == "(":
                    depth += 1
                elif c == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif c in " \t" and depth == 0:
                    break
                j += 1
            dest = line[i:j]
            end = j
        yield dest
        pos = max(end, m.end())


# ---------------------------------------------------------------------------
# Slug heading ala GitHub
# ---------------------------------------------------------------------------
def slugify(text):
    t = text.strip()
    t = re.sub(r"<[^>]+>", "", t)                       # tag HTML
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)    # [teks](url) -> teks
    t = t.replace("`", "").replace("*", "")             # inline code & emphasis
    t = t.lower()
    t = re.sub(r"[^\w\- ]", "", t)                      # \w = huruf/angka/underscore (unicode)
    return t.replace(" ", "-")


def build_anchor_set(headings, explicit_anchors):
    anchors = set(explicit_anchors)
    seen = {}
    for h in headings:
        base = slugify(h)
        if base in seen:
            seen[base] += 1
            slug = f"{base}-{seen[base]}"
        else:
            seen[base] = 0
            slug = base
        anchors.add(slug)
    return anchors


# ---------------------------------------------------------------------------
# Pemindaian file
# ---------------------------------------------------------------------------
def scan_markdown(path):
    """Kembalikan (links[(baris, target)], headings[teks], explicit_anchors{set})."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    links, headings, anchors = [], [], set()
    in_fence = None
    in_comment = False
    for lineno, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip("\r")
        if in_fence:
            ch, length = in_fence
            if re.match(r"^\s{0,3}%s{%d,}\s*$" % (re.escape(ch), length), line):
                in_fence = None
            continue
        if not in_comment:
            fm = FENCE_OPEN_RE.match(line)
            if fm:
                in_fence = (fm.group(1)[0], len(fm.group(1)))
                continue
        line, in_comment = strip_html_comments(line, in_comment)
        if not line.strip():
            continue
        hm = ATX_HEADING_RE.match(line)
        if hm:
            headings.append(hm.group(1))
        for a in HTML_ANCHOR_RE.findall(line):
            anchors.add(a)
        line = INLINE_CODE_RE.sub(" ", line)
        rm = REF_DEF_RE.match(line)
        if rm and not rm.group(1).startswith("^"):
            links.append((lineno, rm.group(2) if rm.group(2) is not None else rm.group(3)))
            continue
        for dest in iter_inline_links(line):
            links.append((lineno, dest))
    return links, headings, anchors


def collect_markdown_files(root):
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if fn.lower().endswith(MD_EXT):
                result.append(os.path.join(dirpath, fn))
    return result


# ---------------------------------------------------------------------------
# Pemeriksaan
# ---------------------------------------------------------------------------
def check(root):
    root = os.path.abspath(root)
    md_files = collect_markdown_files(root)
    anchor_cache = {}
    scanned = {}

    def anchors_for(path):
        path = os.path.abspath(path)
        if path not in anchor_cache:
            if path in scanned:
                _, headings, explicit = scanned[path]
            else:
                _, headings, explicit = scan_markdown(path)
            anchor_cache[path] = build_anchor_set(headings, explicit)
        return anchor_cache[path]

    broken = []
    n_links = 0
    n_external = 0

    for path in md_files:
        links, headings, explicit = scan_markdown(path)
        scanned[os.path.abspath(path)] = (links, headings, explicit)
        rel_file = os.path.relpath(path, root)
        for lineno, raw_target in links:
            target = raw_target.strip()
            if SCHEME_RE.match(target) or target.startswith("//"):
                n_external += 1
                continue
            n_links += 1
            if target == "":
                broken.append((rel_file, lineno, raw_target, "target kosong"))
                continue
            path_part, _, frag = target.partition("#")
            path_part = unquote(path_part.split("?", 1)[0])
            frag = unquote(frag)

            if path_part == "":
                if frag and frag not in anchors_for(path):
                    broken.append((rel_file, lineno, target,
                                   f"anchor '#{frag}' tidak ditemukan di file ini"))
                continue

            if path_part.startswith("/"):
                resolved = os.path.normpath(os.path.join(root, path_part.lstrip("/")))
            else:
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), path_part))

            if not os.path.exists(resolved):
                broken.append((rel_file, lineno, target,
                               f"file/direktori tidak ada: {os.path.relpath(resolved, root)}"))
                continue
            if frag and os.path.isfile(resolved) and resolved.lower().endswith(MD_EXT):
                if frag not in anchors_for(resolved):
                    broken.append((rel_file, lineno, target,
                                   f"anchor '#{frag}' tidak ditemukan di {os.path.relpath(resolved, root)}"))

    broken.sort(key=lambda b: (b[0], b[1]))
    for rel_file, lineno, target, reason in broken:
        print(f"{rel_file}:{lineno}: {target} → {reason}")
    if broken:
        print()
    print(f"Diperiksa: {len(md_files)} file Markdown, {n_links} link/anchor relatif "
          f"({n_external} link eksternal dilewati). Rusak: {len(broken)}.")
    return 1 if broken else 0


def main(argv=None):
    default_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser = argparse.ArgumentParser(
        description="Periksa link & anchor relatif pada semua file Markdown (exit 1 bila ada yang rusak).")
    parser.add_argument("--root", default=default_root,
                        help="direktori root repository (default: direktori induk dari tools/)")
    args = parser.parse_args(argv)
    if not os.path.isdir(args.root):
        print(f"Root tidak ditemukan: {args.root}", file=sys.stderr)
        return 2
    return check(args.root)


if __name__ == "__main__":
    sys.exit(main())
