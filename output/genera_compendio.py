"""Genera wiki/corso-completo.md: tutto il corso in un unico file, lezione per lezione.

L'ordine viene da wiki/lezioni.md: per ogni "## Lezione N — titolo" si prendono, nell'ordine,
le pagine dei punti numerati ("1. [[pagina]] — ...") e poi esercizi ed entità collegate
("Esercizi collegati: [[...]]", "Entità collegate: [[...]]").
Ogni pagina viene copiata senza intestazione YAML e senza la riga "_Aggiornato", con i titoli abbassati
di due livelli (# -> ###, ## -> ####, ...). Il file è generato: non modificarlo a mano, ma modificare
le pagine e rilanciare lo script.
Uso: python genera_compendio.py
"""
import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT = WIKI / "corso-completo.md"

pagine = {p.stem: p for p in WIKI.rglob("*.md")}


def corpo(nome, shift=2):
    testo = pagine[nome].read_text(encoding="utf-8")
    if testo.startswith("---"):
        testo = testo.split("\n---", 1)[1].split("\n", 1)[1]
    righe, out, in_code = testo.split("\n"), [], False
    for l in righe:
        if l.strip().startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^_Aggiornato:", l):
            continue
        m = re.match(r"^(#{1,6})(\s.*)$", l)
        if m and not in_code:
            livello = min(len(m.group(1)) + shift, 6)
            l = "#" * livello + m.group(2)
            if len(m.group(1)) == 1:
                l += f" · [[{nome}|pagina]]"
        out.append(l)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def lezioni():
    testo = (WIKI / "lezioni.md").read_text(encoding="utf-8")
    blocchi = re.split(r"(?m)^## ", testo)[1:]
    for b in blocchi:
        titolo = b.split("\n", 1)[0].strip()
        voci = re.findall(r"(?m)^\d+\.\s+\[\[([^\]|#]+)", b)
        esercizi = []
        for etichetta in ("Esercizi collegati", "Entità collegate"):
            m = re.search(rf"(?m)^{etichetta}:(.*)$", b)
            if m:
                esercizi += re.findall(r"\[\[([^\]|#]+)", m.group(1))
        yield titolo, voci, esercizi


def main():
    parti = [
        "# Corso completo — Trasmissione dei Segnali Digitali",
        "",
        "> Tutto il wiki in un unico file, lezione per lezione e argomento per argomento, nell'ordine di [[lezioni]]. "
        f"**File generato** da `output/genera_compendio.py` il {datetime.date.today():%Y-%m-%d}: non modificarlo a mano, "
        "modifica le pagine e rilancia lo script. Ogni argomento rimanda alla sua pagina con il link «pagina».",
        "",
        "## Indice",
        "",
    ]
    struttura = list(lezioni())
    for titolo, voci, esercizi in struttura:
        parti.append(f"- [[#{titolo}]]")
    for titolo, voci, esercizi in struttura:
        parti += ["", "---", "", f"## {titolo}", ""]
        visti = []
        for nome in voci + esercizi:
            if nome in visti or nome not in pagine:
                continue
            visti.append(nome)
            parti += [corpo(nome), ""]
    OUT.write_text("\n".join(parti).rstrip() + "\n", encoding="utf-8", newline="\n")
    print("scritto", OUT.name, "-", sum(len(v) + len(e) for _, v, e in struttura), "voci,",
          len(OUT.read_text(encoding="utf-8")) // 1024, "KB")


if __name__ == "__main__":
    main()
