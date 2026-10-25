"""Crea i PDF delle lezioni di wiki/corso-completo.md.

Ogni lezione del corso è una sezione "## Lezione N — titolo". Lo script prende le lezioni indicate, converte il Markdown
in HTML (formule con KaTeX, immagini incorporate) e lo stampa in PDF con Chrome senza interfaccia.

Uso:  python crea_pdf.py            -> PDF delle lezioni 5 e 6
      python crea_pdf.py 3 4        -> PDF delle lezioni 3 e 4
      python crea_pdf.py tutte      -> un PDF per ogni lezione
      python crea_pdf.py --tutto    -> un unico PDF con tutto il corso
Richiede: markdown-it-py, mdit-py-plugins, pillow, Chrome (o Edge) e una connessione per scaricare KaTeX.
I PDF vanno in output/pdf/. Nei PDF i link diventano testo; le animazioni (GIF) diventano un fotogramma.
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SORGENTE = ROOT / "wiki" / "corso-completo.md"
OUT = ROOT / "output" / "pdf"
CHROME = next((p for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                           r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                           r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") if Path(p).exists()), None)

STILE = """
@page { size: A4; margin: 18mm 17mm 20mm 17mm; @bottom-center { content: counter(page); font: 9pt sans-serif; color: #666; } }
body { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 10.4pt; line-height: 1.45; color: #1f1f1e; }
h1 { font-size: 22pt; margin: 0 0 4mm; border-bottom: 2px solid #2a78d6; padding-bottom: 2mm; }
h2 { font-size: 15pt; margin: 9mm 0 3mm; color: #1c5cab; break-after: avoid; }
h3 { font-size: 12.5pt; margin: 6mm 0 2mm; color: #1f1f1e; border-bottom: 1px solid #ddd; break-after: avoid; }
h4 { font-size: 11pt; margin: 4mm 0 1.5mm; color: #333; break-after: avoid; }
p { margin: 1.6mm 0; } ul, ol { margin: 1mm 0 2mm; padding-left: 6mm; } li { margin: 0.6mm 0; }
blockquote { margin: 2mm 0; padding: 1.5mm 4mm; border-left: 3px solid #eb6834; background: #faf4ef; break-inside: avoid; }
table { border-collapse: collapse; margin: 2.5mm 0; font-size: 9.6pt; break-inside: avoid; }
th, td { border: 1px solid #c9c8c0; padding: 1mm 2.4mm; vertical-align: top; } th { background: #f0efe9; }
img { max-width: 100%; height: auto; display: block; margin: 2.5mm auto; break-inside: avoid; }
em.did, p > em:only-child { font-size: 9.2pt; color: #555; }
.math.block { margin: 2mm 0; overflow-x: hidden; break-inside: avoid; }
code { font-size: 9.2pt; background: #f2f1ec; padding: 0 1mm; }
hr { border: 0; border-top: 1px solid #ddd; margin: 5mm 0; }
.copertina { margin-bottom: 6mm; color: #555; font-size: 10pt; }
"""

PAGINA = """<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{titolo}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<style>{stile}</style></head><body>{corpo}
<script>
window.addEventListener('load', function () {{
  document.querySelectorAll('.math').forEach(function (el) {{
    var blocco = el.classList.contains('block');
    try {{ katex.render(el.textContent, el, {{displayMode: blocco, throwOnError: false, strict: false}}); }} catch (e) {{}}
  }});
  document.body.setAttribute('data-pronto', '1');
}});
</script></body></html>"""


def indice_immagini():
    nomi = {}
    for cartella in ("raw/assets", "output/grafici", "raw/scripts"):
        for p in (ROOT / cartella).rglob("*"):
            if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif"):
                nomi[p.name] = p
    return nomi


IMMAGINI = indice_immagini()


def fotogramma(gif, tmp):
    """Un fotogramma rappresentativo (circa 60% dell'animazione) al posto della GIF."""
    im = Image.open(gif)
    im.seek(int(im.n_frames * 0.6))
    out = tmp / (gif.stem + ".png")
    im.convert("RGB").save(out)
    return out


def converti_wikilink(testo, tmp):
    def immagine(m):
        nome, larg = m.group(1), m.group(3)
        p = IMMAGINI.get(nome)
        if p is None:
            return f"*(immagine mancante: {nome})*"
        if p.suffix.lower() == ".gif":
            p = fotogramma(p, tmp)
        w = f' width="{larg}"' if larg else ""
        return f'\n\n<img src="{p.as_uri()}"{w}>\n\n'      # paragrafo a sé: la didascalia che segue resta Markdown
    testo = re.sub(r"!\[\[([^\]|]+?)(\|(\d+))?\]\]", immagine, testo)
    # riferimenti ai PDF: restano come testo, con l'alias
    testo = re.sub(r"\[\[[^\]|#]+\.pdf(?:#page=\d+)?\|([^\]]*)\]\]", r"\1", testo)
    testo = re.sub(r"\[\[([^\]|#]+)\.pdf#page=(\d+)\]\]", r"p. \2", testo)
    testo = re.sub(r"\[\[[^\]|#]+\.pdf\]\]", "", testo)
    testo = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", testo)
    testo = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("#")[-1], testo)
    return testo


def lezioni_del_corso(testo):
    parti = re.split(r"(?m)^(?=## Lezione \d+)", testo)
    return {int(re.match(r"## Lezione (\d+)", p).group(1)): p for p in parti if p.startswith("## Lezione")}


def slug(t):
    t = t.lower()
    for a, b in (("à", "a"), ("è", "e"), ("é", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u"), ("—", " ")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def md_a_html(md_testo):
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    dollarmath_plugin(md, allow_space=True, allow_digits=True, double_inline=True)
    md.add_render_rule("math_inline", lambda self, t, i, o, e: f'<span class="math inline">{html.escape(t[i].content)}</span>')
    md.add_render_rule("math_block", lambda self, t, i, o, e: f'<div class="math block">{html.escape(t[i].content)}</div>')
    return md.render(md_testo)


def stampa_pdf(corpo_html, titolo, destinazione):
    if CHROME is None:
        raise SystemExit("Chrome o Edge non trovati")
    with tempfile.TemporaryDirectory(prefix="pdf") as d:
        pagina = Path(d) / "p.html"
        pagina.write_text(PAGINA.format(titolo=html.escape(titolo), stile=STILE, corpo=corpo_html), encoding="utf-8")
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
               "--virtual-time-budget=60000", f"--print-to-pdf={destinazione}", pagina.as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=300)


def costruisci(numeri, testo_corso, unico=False):
    lez = lezioni_del_corso(testo_corso)
    tmp = Path(tempfile.mkdtemp(prefix="gif"))
    if unico:
        corpo = "# Trasmissione dei Segnali Digitali — corso completo\n\n" + "\n\n".join(lez[n] for n in sorted(lez))
        stampa_pdf(md_a_html(converti_wikilink(corpo, tmp)), "Corso completo", OUT / "corso-completo.pdf")
        print("scritto", OUT / "corso-completo.pdf")
        return
    for n in numeri:
        blocco = lez[n]
        titolo = blocco.split("\n", 1)[0][3:].strip()
        corpo = re.sub(r"(?m)^#(#+ )", r"\1", blocco)     # ogni titolo sale di un livello: la lezione diventa h1
        stampa_pdf(md_a_html(converti_wikilink(corpo, tmp)), titolo, OUT / f"lezione-{n}-{slug(titolo.split('—', 1)[-1])}.pdf")
        print("scritto", OUT / f"lezione-{n}-{slug(titolo.split('—', 1)[-1])}.pdf")


if __name__ == "__main__":
    args = sys.argv[1:]
    testo = SORGENTE.read_text(encoding="utf-8")
    if args == ["--tutto"]:
        costruisci([], testo, unico=True)
    elif args == ["tutte"]:
        costruisci(sorted(lezioni_del_corso(testo)), testo)
    else:
        costruisci([int(a) for a in args] or [5, 6], testo)
