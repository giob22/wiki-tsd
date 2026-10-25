"""Controllo di integrità di wiki/corso-completo.md.

Verifica: link interni e ancore, file e pagine dei PDF citati, immagini esistenti, formule ($ spaiati, spazi ai bordi,
`*` dentro le formule in linea, `|` nelle tabelle), riferimenti ai PDF fuori dai titoli, pagine dei PDF non citate.
Uso: python controlla_corso.py
"""
import pathlib
import re

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "wiki" / "corso-completo.md"
nomi_wiki = {p.stem for p in (ROOT / "wiki").rglob("*.md")}
file_noti = {p.name: p for d in ("raw", "output", "wiki") for p in (ROOT / d).rglob("*") if p.is_file()}

INLINE = re.compile(r"(?<![\\$])\$(?!\$)([^$]+?)(?<!\\)\$(?!\$)")
DOLLARO = re.compile(r"(?<!\\)(?<!\$)\$(?!\$)")

testo = SRC.read_text(encoding="utf-8")
righe = testo.split("\n")
titoli = {re.sub(r"^#+\s*", "", r).strip() for r in righe if re.match(r"^#{1,6} ", r)}
problemi = []
citate = {}

in_codice = in_math = False
for i, r in enumerate(righe, 1):
    if r.strip().startswith("```"):
        in_codice = not in_codice
        continue
    if in_codice:
        continue
    titolo = bool(re.match(r"^#{1,6} ", r))
    if titolo:
        # intervalli «p. a–b»: contano anche le pagine intermedie
        for m in re.finditer(r"\[\[([^\]|#]+\.pdf)#page=(\d+)[^\]]*\]\]–\[\[[^\]|#]+\.pdf#page=(\d+)", r):
            citate.setdefault(m.group(1), set()).update(range(int(m.group(2)), int(m.group(3)) + 1))
    for m in re.finditer(r"!?\[\[([^\]]+)\]\]", r):
        base, _, frag = m.group(1).split("|")[0].partition("#")
        if not base:
            if frag not in titoli:
                problemi.append((i, "ancora mancante", frag))
        elif base.lower().endswith(".pdf"):
            pag = re.match(r"page=(\d+)", frag)
            if base not in file_noti:
                problemi.append((i, "PDF mancante", base))
            elif pag:
                n = int(pag.group(1))
                with pymupdf.open(file_noti[base]) as d:
                    if n > len(d):
                        problemi.append((i, "pagina oltre la fine", f"{base}#{n}"))
                citate.setdefault(base, set()).add(n)
                if not titolo:
                    problemi.append((i, "riferimento PDF fuori dal titolo", m.group(0)))
        elif "." in base and not base.endswith(".md"):
            if base not in file_noti:
                problemi.append((i, "immagine/file mancante", base))
        elif base not in nomi_wiki:
            problemi.append((i, "pagina wiki mancante", base))
    if r.strip() == "$$":
        in_math = not in_math
        continue
    if in_math or r.strip().startswith("$$"):
        continue
    for mm in INLINE.finditer(r):
        f = mm.group(1)
        if f != f.strip():
            problemi.append((i, "spazio al bordo del $", f[:30]))
        if "*" in f:
            problemi.append((i, "* dentro formula in linea", f[:30]))
        if r.lstrip().startswith("|") and "|" in f:
            problemi.append((i, "| dentro formula in tabella", f[:30]))
    if len(DOLLARO.findall(r)) % 2:
        problemi.append((i, "$ spaiato", r[:50]))
if in_math:
    problemi.append((0, "$$ non chiuso", ""))

print(f"{len(righe)} righe, {len(titoli)} titoli")
for base, pagine in sorted(citate.items()):
    with pymupdf.open(file_noti[base]) as d:
        tot = len(d)
    mancanti = sorted(set(range(1, tot + 1)) - pagine)
    print(f"{base}: {len(pagine)}/{tot} pagine citate nei titoli; non citate: {mancanti}")
if problemi:
    print(f"\n{len(problemi)} problemi:")
    for p in problemi:
        print("  riga", *p)
else:
    print("\nNessun problema.")
