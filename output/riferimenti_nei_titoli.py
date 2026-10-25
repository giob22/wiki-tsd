"""Sposta i riferimenti ai PDF ([[file.pdf#page=N]]) dal corpo del testo ai titoli di sezione.

Per ogni pagina del wiki (esclusi lezioni.md e log.md):
- ogni riferimento a un PDF viene tolto dal corpo e aggiunto al titolo (#, ##, ###, ...) della sezione
  in cui si trova, in forma compatta: "### Titolo · [[file.pdf#page=3|p. 3]], [[...|p. 5]]";
- le righe che servivano solo a citare la fonte ("> 📄 Fonte: ...") spariscono;
- le colonne "Pagina" delle tabelle spariscono (se la pagina è la prima colonna resta come testo "p. N");
- i riferimenti che fanno parte di una frase ("gli appunti di [[...#page=24]]") diventano testo semplice "p. 24";
- i link a titoli ([[pagina#Titolo]]) diventano link alla pagina, perché cambiando i titoli si romperebbero.
Uso: python riferimenti_nei_titoli.py           prova: scrive i diff in una cartella temporanea
     python riferimenti_nei_titoli.py --scrivi  applica le modifiche
"""
import difflib
import pathlib
import re
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ESCLUSI = {"lezioni.md", "log.md", "corso-completo.md"}
CORTO = {"Intro.pdf": "Intro", "Probabilità.pdf": "Probabilità", "Campionamento_AD_DA.pdf": "Campionamento",
         "Rappresentazione_Rice.pdf": "Rice", "random_processes.pdf": "Processi"}

LINK = re.compile(r"(?<!!)\[\[([^\[\]|#]+?\.pdf)(?:#page=(\d+))?(?:\|[^\[\]]*)?\]\]")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
T = r"\x00\d+\x01"                      # segnaposto numerato di un riferimento

QUAL = (r"(?:slide\s*\d+(?:\s*[–-]\s*\d+)?"
        r"|appunti(?:\s+a\s+mano)?|note?\s+a\s+mano|nota|pagina\s+di\s+appunti(?:\s+prima\s+della\s+slide\s*\d+)?"
        r"|con\s+(?:le\s+)?(?:note|nota|annotazioni)(?:\s+a\s+mano)?|tutte\s+con\s+annotazioni\s+a\s+mano"
        r"|figura|esempio|tabella|testo|risultato\s+dato|coppia\s+data|dato\s+come\s+modello|p\.\s*\d+)")
SEP = r"(?:\s*(?:,|;|–|-|\+|\be\b)\s*)"
QGROUP = rf"(?:\s*\(\s*{QUAL}(?:{SEP}{QUAL})*\s*\))"
BLOCCO = rf"{T}{QGROUP}?(?:{SEP}{T}{QGROUP}?)*"


def ripulisci(line):
    """Toglie i segnaposto con il loro contorno; quelli dentro una frase restano (diventeranno 'p. N')."""
    # parentesi che contengono solo citazioni e qualificatori
    line = re.sub(rf"\s*\(\s*(?:(?:{QUAL}|vedi|→)\s*[,:]?\s*)*{BLOCCO}(?:{SEP}{QUAL})*\s*\)", "", line)
    # "📄 Fonte: <citazioni>: spiegazione" -> "📄 Fonte: spiegazione" solo se dopo c'è ":" (la citazione introduce il testo)
    line = re.sub(rf"(📄 Fonte:|\*\*Fonte:\*\*)\s*{BLOCCO}(?:{SEP}{QUAL})*\s*:\s*", r"\1 ", line)
    # didascalie che iniziano con la citazione: "*[[..]] (slide 17). Testo*"
    line = re.sub(rf"^(\s*(?:-\s*)?\*)\s*{BLOCCO}\s*[.:,]?\s*", r"\1", line)
    # "Appunti a mano, [[..]]." in coda di didascalia, "Appunti a mano, [[..]]: testo"
    line = re.sub(rf",\s*{BLOCCO}(?=\s*\.?\*\s*$|\s*:)", "", line)
    # "... — [[..]]." / "... — [[..]]*" in coda: pura citazione
    line = re.sub(rf"\s*—\s*{BLOCCO}(?:{SEP}{QUAL})*\s*(?=\.?\*?\s*$)", "", line)
    # "(testo, [[..]])" -> "(testo)"   e   "([[..]], slide 13; testo)" / "([[..]], vedi X)" -> "(testo)"
    line = re.sub(rf"\s*[,;]\s*{BLOCCO}(?:{SEP}{QUAL})*\s*(?=\))", "", line)
    line = re.sub(rf"\(\s*{BLOCCO}(?:{SEP}{QUAL})*\s*[,;]\s*", "(", line)
    # "📄 Fonte: [[..]] — testo" -> "📄 Testo"
    line = re.sub(rf"📄 Fonte:\s*{BLOCCO}(?:{SEP}{QUAL})*\s*—\s*(\w)", lambda m: "📄 " + m.group(1).upper(), line)
    return line


def da_cancellare(line, work):
    t = re.sub(r"📄|Fonte:?|\*\*Fonte:\*\*|🧩|[>\-*_:.,;()\s]", "", line)
    if t == "":
        return True
    # righe di sola citazione (Fonte, o voce di elenco fatta solo di citazioni): tolti segnaposto e parentesi non resta testo
    if re.match(rf"\s*(>\s*📄 Fonte:|\*\*Fonte:\*\*|-\s+\**{T})", work):
        resto = re.sub(r"\([^()]*\)", "", re.sub(T, "", work))
        resto = re.sub(rf"📄|Fonte:?|\*\*Fonte:\*\*|{QUAL}|\b(?:e|vedi|anche)\b|[>\-*_:.,;–\s]", "", resto)
        return resto == ""
    return False


def sistema(s):
    s = re.sub(r"\(\s*[,;]?\s*\)", "", s)
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"([,;:])\s*([,;.])", r"\2", s)
    s = re.sub(r"(\S)  +", r"\1 ", s)
    s = re.sub(r"\*\*Fonte:\*\*\s*$", "", s)
    return s.rstrip()


def celle_di(riga):
    """Celle di una riga di tabella: separa sui '|' non preceduti da '\\' (in $|x|$ si scrive '\\|')."""
    s = riga.strip()
    s = s[1:] if s.startswith("|") else s
    s = s[:-1] if s.endswith("|") and not s.endswith("\\|") else s
    return re.split(r"(?<!\\)\|", s)


def comprimi(pagine):
    out = []
    for p in sorted(set(pagine)):
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def etichetta(refs):
    per_file = {}
    for f, n in refs:
        per_file.setdefault(f, [])
        if n:
            per_file[f].append(n)
    multipli = len(per_file) > 1
    parti = []
    for f, pp in per_file.items():
        if not pp:
            parti.append(f"[[{f}|{CORTO.get(f, f)}]]")
            continue
        pezzi = []
        for a, b in comprimi(pp):
            if a == b:
                pezzi.append(f"[[{f}#page={a}|p. {a}]]")
            elif b == a + 1:
                pezzi.append(f"[[{f}#page={a}|p. {a}]], [[{f}#page={b}|{b}]]")
            else:
                pezzi.append(f"[[{f}#page={a}|p. {a}]]–[[{f}#page={b}|{b}]]")
        parti.append((CORTO.get(f, f) + " " if multipli else "") + ", ".join(pezzi))
    return " · ".join(parti)


def ancore(testo):
    def sub(m):
        pag, tit, alias = m.group(1), m.group(2), m.group(3)
        if pag.endswith(".pdf") or tit.startswith("page="):
            return m.group(0)
        if pag:
            return f"[[{pag}|{alias[1:]}]]" if alias else f"[[{pag}]] (sezione «{tit}»)"
        return alias[1:] if alias else f"«{tit}» (in questa pagina)"
    return re.sub(r"\[\[([^\[\]|#]*)#([^\[\]|]+)(\|[^\[\]]*)?\]\]", sub, testo)


def trasforma(testo):
    righe = ancore(testo).split("\n")
    out, refs_sez = [], {}
    titolo = None
    in_code = in_math = False
    in_yaml = righe[0].strip() == "---"
    drop = None
    for i, line in enumerate(righe):
        if in_yaml:
            out.append(line)
            in_yaml = not (i > 0 and line.strip() == "---")
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        if not in_math and HEAD.match(line):
            out.append(line)
            titolo = len(out) - 1
            continue
        if line.strip() == "$$" or (line.strip().startswith("$$") and line.strip().count("$$") == 1):
            in_math = not in_math

        refs = []

        def tok(m):
            refs.append((m.group(1), int(m.group(2)) if m.group(2) else None))
            return f"\x00{len(refs) - 1}\x01"
        work = LINK.sub(tok, line)
        refs_sez.setdefault(titolo, []).extend(refs)

        def testo_p(m):
            f, n = refs[int(m.group(0)[1:-1])]
            return f"p. {n}" if n else ""

        if line.lstrip().startswith("|"):
            celle = [c.strip() for c in celle_di(line)]
            if drop is None and celle and re.fullmatch(r"Pagin[ae].*", celle[-1]) and len(celle) > 1:
                drop = len(celle) - 1
            if drop is None and not refs:
                out.append(line)
                continue
            cw = [c.strip() for c in celle_di(work)]
            if drop is not None and len(cw) > drop:
                del cw[drop]
            cw = [sistema(re.sub(T, testo_p, ripulisci(c))) for c in cw]
            out.append("| " + " | ".join(cw) + " |")
            continue
        drop = None
        if not refs:
            out.append(line)
            continue
        nuova = sistema(re.sub(T, testo_p, ripulisci(work)))
        if da_cancellare(nuova, work):
            continue
        if re.fullmatch(r"\s*(?:-\s*)?\*\s*\*?\s*", nuova):
            continue
        out.append(nuova)

    # separatori delle tabelle: tante colonne quante l'intestazione
    for k, l in enumerate(out):
        if re.fullmatch(r"\|(\s*:?-+:?\s*\|)+", l.strip()) and k > 0 and out[k - 1].lstrip().startswith("|"):
            ncol = len(celle_di(out[k - 1]))
            out[k] = "|" + "---|" * ncol
    for idx, refs in refs_sez.items():
        if idx is None or not refs:
            continue
        out[idx] = out[idx].rstrip() + " · " + etichetta(refs)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def main():
    scrivi = "--scrivi" in sys.argv
    tmp = pathlib.Path(tempfile.gettempdir()) / "rif-titoli"
    tmp.mkdir(exist_ok=True)
    prima = dopo = senza_titolo = 0
    for p in sorted(WIKI.rglob("*.md")):
        if p.name in ESCLUSI or p.parent.name == "corso":   # capitoli generati dal compendio
            continue
        s = p.read_text(encoding="utf-8")
        n = trasforma(s)
        prima += len(LINK.findall(s))
        dopo += sum(len(LINK.findall(l)) for l in n.split("\n") if not HEAD.match(l))
        if n != s:
            (tmp / (p.stem + ".diff")).write_text(
                "\n".join(difflib.unified_diff(s.split("\n"), n.split("\n"), lineterm="", n=0)), encoding="utf-8")
            if scrivi:
                p.write_text(n, encoding="utf-8", newline="\n")
    print("riferimenti prima:", prima, "| rimasti nel corpo:", dopo, "| diff in", tmp)


if __name__ == "__main__":
    main()
