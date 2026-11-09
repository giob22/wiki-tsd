"""Costruisce il sito di studio per l'intercorso: HTML statico, formule KaTeX, disegni SVG, leggibile da cellulare.

Per ogni lezione l'ordine è quello dei PDF:
  1. «Il corso, slide per slide»  = sezione di wiki/corso-completo.md (solo ciò che sta nei PDF), con i disegni;
  2. «Spiegazioni e dimostrazioni» = per ogni pagina concetto: spiegazione, derivazioni passo-passo (a comparsa);
  3. «Domande da esame»            = dalla pagina fonte.

Uso:  python crea_sito.py [cartella]      (default: <temp>/sito-tsd)
Richiede: markdown-it-py, mdit-py-plugins, pillow. Le formule si rendono nel browser con KaTeX (CDN).
"""
import html
import re
import shutil
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sito_disegni  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/"

LEZIONI = [
    dict(n=3, slug="lezione-3", titolo="Quantizzazione: SNR, legge dei 6 dB, Lloyd-Max e companding",
         breve="Il quantizzatore uniforme e il suo SNR (legge dei 6 dB/bit), i suoi limiti, il quantizzatore ottimo di Lloyd-Max e il companding (leggi µ e A).",
         pdf="Campionamento_AD_DA.pdf, slide 26–43", inizio="### Relazione ingresso-uscita del quantizzatore",
         concetti=["quantizzazione-uniforme", "snr-di-quantizzazione", "quantizzazione-non-uniforme", "companding"],
         fonte="campionamento-conversione-ad-da",
         domande_filtro=("quantizzatore uniforme", "6 dB", "Lloyd", "robusta", "companding"), esercizi=["dimensionamento-quantizzatore"]),
    dict(n=4, slug="lezione-4", titolo="Rappresentazione complessa in banda base",
         breve="Segnali in banda base e passa-banda, segnale analitico, inviluppo complesso, componenti I/Q, up/down-conversion, filtri.",
         pdf="Rappresentazione_Rice.pdf, slide 1–19 più appunti", inizio=None,
         concetti=["modulazione-digitale", "segnali-banda-base-e-passa-banda", "segnale-analitico", "inviluppo-complesso",
                   "upconversion-e-downconversion", "equivalente-banda-base-dei-filtri"],
         fonte="rappresentazione-complessa-banda-base", domande_filtro=None, esercizi=[]),
    dict(n=5, slug="lezione-5", titolo="Processi aleatori",
         breve="Processi stocastici, momenti, stazionarietà, acf, passaggio attraverso filtri LTI, PSD, processo gaussiano, tempo discreto.",
         pdf="random_processes.pdf, slide 1–41 più appunti", inizio=None,
         concetti=["processo-aleatorio", "momenti-di-un-processo", "stazionarieta", "autocorrelazione-processi-wss",
                   "processi-e-sistemi-lti", "densita-spettrale-di-potenza", "processo-gaussiano"],
         fonte="processi-aleatori", domande_filtro=None, esercizi=["calcolo-densita-spettrale"]),
    dict(n=7, slug="lezione-7", titolo="Rappresentazione di Rice per i processi aleatori",
         breve="Inviluppo complesso e componenti in quadratura di un processo passa-banda, loro PSD, rumore in banda.",
         pdf="Rappresentazione_Rice_processi.pdf, slide 1–13 più appunti", inizio=None,
         concetti=["processi-passa-banda", "psd-componenti-in-quadratura", "rumore-in-banda-passante"],
         fonte="rappresentazione-processi-passa-banda", domande_filtro=None, esercizi=[]),
]

# dove va ogni disegno: (n. lezione, inizio del titolo della sezione) -> chiavi; il disegno sta in fondo alla sezione
FIGURE = {
    (3, "Limiti della quantizzazione uniforme"): ["laplace"],
    (3, "Quantizzazione non uniforme"): ["quantizzatore"],
    (3, "Quantizzazione ottima: Lloyd-Max"): ["lloyd_centroide", "lloyd_ciclo"],
    (3, "Limiti della quantizzazione ottima"): ["companding_schema"],
    (3, "Analisi del companding"): ["companding_equivalenza"],
    (3, "Legge A"): ["leggi"],
    (3, "Prestazioni del companding"): ["snr_livello"],
    (4, "Segnali in banda base e in banda passante"): ["spettri_bb_pb"],
    (4, "Ritorno al segnale reale e Hilbert"): ["hilbert"],
    (4, "Inviluppo complesso"): ["catena_spettri", "fasore"],
    (4, "Energia dell'inviluppo"): ["chi_e_chi"],
    (4, "Upconversion e downconversion"): ["up_down"],
    (5, "Appunti — Sinusoide a fase casuale"): ["realizzazioni"],
    (5, "Slide 13 — Processi stazionari in senso lato"): ["stazionarieta"],
    (5, "Slide 16 — Significato fisico della acf"): ["acf"],
    (5, "Slide 19 — Processi indipendenti"): ["implicazioni"],
    (5, "Slide 28 — PSD e sistemi LTI"): ["lti"],
    (5, "Slide 29–30 — Significato fisico della PSD"): ["psd_filtro"],
    (7, "Slide 8 e appunti"): ["catena_psd"],
    (7, "Slide 9 e appunti"): ["simmetria"],
    (7, "Slide 12–13"): ["rumore"],
}

# ----------------------------------------------------------------------------------------------- immagini


def indice_immagini():
    nomi = {}
    for cartella in ("raw/assets", "output/grafici", "raw/scripts"):
        for p in (ROOT / cartella).rglob("*"):
            if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif"):
                nomi[p.name] = p
    return nomi


IMMAGINI = indice_immagini()
COPIATE = {}


def immagine_sito(nome, out):
    """Copia l'immagine in img/ (le GIF diventano un fotogramma fisso: il sito deve restare leggero)."""
    if nome in COPIATE:
        return COPIATE[nome]
    p = IMMAGINI.get(nome)
    if p is None:
        return None
    (out / "img").mkdir(exist_ok=True)
    if p.suffix.lower() == ".gif":
        im = Image.open(p)
        im.seek(int(im.n_frames * .6))
        dest = out / "img" / (p.stem + ".png")
        im.convert("RGB").save(dest, optimize=True)
    else:
        dest = out / "img" / p.name
        shutil.copy(p, dest)
    COPIATE[nome] = "img/" + dest.name
    return COPIATE[nome]


# ----------------------------------------------------------------------------------------------- Markdown -> HTML

def rimuovi_frontmatter(t):
    return re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)


def _alias_pdf(m):
    nome, pag, alias = m.group(1), m.group(2), m.group(3)
    return alias if alias else (f"p. {pag}" if pag else "")


def togli_riferimenti(t):
    """Il sito non cita i PDF: via pagine, numeri di slide, righe «Fonte:» e prefissi «Slide N —» dei titoli."""
    t = "\n".join(r for r in t.split("\n") if ".pdf" not in r)
    t = re.sub(r"(?m)^\*\*Fonte:\*\*.*\n?", "", t)
    t = re.sub(r"(?m)^Fonte:.*\n?", "", t)
    t = re.sub(r"(?m)^(#{2,6}) (?:Slide \d+(?:[–-]\d+)?(?: e appunti)? — |Appunti — )", r"\1 ", t)
    t = re.sub(r"(?m)^(#{2,6} .+?) · (?:.*\bpp?\. ?\d+.*|appunti.*)$", r"\1", t)
    t = re.sub(r"(?m)^(@@DET:.+?) · [^@]*(@@)$", r"\1\2", t)
    t = re.sub(r"[ \t]*\((?:[^()$]*?)\b(?:pp?\.|[Ss]lide|pagin[ae])[ \t]*\d[^()$]*\)", "", t)
    t = re.sub(r"(?:,| di| a| in| alle| alla| nelle)?[ \t]*\bpp?\. ?\d+(?:[–-]\d+)?(?:(?:,| e) ?\d+(?:[–-]\d+)?)*", "", t)
    t = re.sub(r"[ \t]+(?:della|nella|sulla|dalla|alla|delle|nelle|sulle|dalle|di)[ \t]+[Ss]lide \d+(?:[–-]\d+)?(?:(?:,| e) ?\d+(?:[–-]\d+)?)*", "", t)
    t = re.sub(r"\b([Ss]lide) \d+(?:[–-]\d+)?(?:(?:,| e) ?\d+(?:[–-]\d+)?)*", r"\1", t)
    t = t.replace(" nel PDF", "").replace(",,", ",").replace(", ,", ",")
    t = re.sub(r"(?m)^[.,;:] ?(?=\S)", "", t)
    return t


def wikilink_testo(t, out):
    """Wikilink -> testo. Le immagini vanno in img/; i riferimenti ai PDF restano come 'p. N'."""
    def img(m):
        nome, larg = m.group(1).strip(), m.group(3)
        src = immagine_sito(nome, out)
        if src is None:
            return ""
        return f'\n\n<img class="zoom" src="{src}" alt="" loading="lazy">\n\n'
    t = re.sub(r"!\[\[([^\]|]+?)(\\?\|(\d+))?\]\]", img, t)
    t = re.sub(r"\[\[[^\]|#]+\.pdf(?:#page=(\d+))?(?:\\?\|([^\]]*))?\]\]",
               lambda m: m.group(2) if m.group(2) else (f"p. {m.group(1)}" if m.group(1) else ""), t)
    t = re.sub(r"\[\[([^\]|]+?)\\?\|([^\]]+)\]\]", r"\2", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("#")[-1].replace("-", " "), t)
    return togli_riferimenti(t)


def titoli_con_pagine(t):
    return t


def render_md(testo):
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    dollarmath_plugin(md, allow_space=True, allow_digits=True, double_inline=True)
    md.add_render_rule("math_inline", lambda self, t, i, o, e: f'<span class="math inline">{html.escape(t[i].content)}</span>')
    md.add_render_rule("math_block", lambda self, t, i, o, e: f'<div class="math block">{html.escape(t[i].content)}</div>')
    return md.render(testo)


def render_inline(testo):
    md = MarkdownIt("commonmark", {"html": True})
    dollarmath_plugin(md, allow_space=True, allow_digits=True, double_inline=True)
    md.add_render_rule("math_inline", lambda self, t, i, o, e: f'<span class="math inline">{html.escape(t[i].content)}</span>')
    return md.renderInline(testo)


CALLOUT = {"🧮": "formula", "🎯": "esame", "🧩": "mia", "💡": "conn", "⚠": "avv", "❓": "dub", "📄": "mia", "📚": "mia"}


def post_html(h):
    # callout dai blockquote che iniziano con un marcatore
    def bq(m):
        for emo, cls in CALLOUT.items():
            if m.group(1).startswith(emo):
                return f'<blockquote class="co {cls}"><p>{m.group(1)}'
        return m.group(0)
    h = re.sub(r"<blockquote>\s*<p>(\S)", lambda m: bq(m) if m.group(1) in CALLOUT else m.group(0), h)
    # tabelle scorrevoli
    h = h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    return h


def slug(t):
    t = re.sub(r"<[^>]+>", "", t).lower()
    for a, b in (("à", "a"), ("è", "e"), ("é", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:48] or "sez"


def con_id(h, usati, toc=None, prefisso=""):
    def f(m):
        liv, attr, inner = int(m.group(1)), m.group(2), m.group(3)
        s = prefisso + slug(re.sub(r'<span class="pag">.*?</span>', "", inner))
        base, k = s, 2
        while s in usati:
            s, k = f"{base}-{k}", k + 1
        usati.add(s)
        if toc is not None and liv in (3, 4):
            toc.append((liv, s, re.sub(r'<span class="pag">.*?</span>', "", inner)))
        return f'<h{liv}{attr} id="{s}">{inner}</h{liv}>'
    return re.sub(r"<h([2-6])([^>]*)>(.*?)</h\1>", f, h)


def sezione(md, titolo):
    """Contenuto della sezione `## titolo` (fino alla successiva `## `), senza il titolo."""
    m = re.search(rf"(?ms)^## {re.escape(titolo)}[^\n]*\n(.*?)(?=^## |\Z)", md)
    return m.group(1).strip() if m else ""


def demota(md, n):
    return re.sub(r"(?m)^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + n) + " ", md)


# ----------------------------------------------------------------------------------------------- figure

DISEGNI = sito_disegni.tutte()


def inserisci_figure(corpo, n):
    righe = corpo.split("\n")
    out, pendenti = [], []
    for r in righe + ["## FINE"]:
        if re.match(r"#{2,6} ", r):
            for k in pendenti:
                out += ["", f"@@FIG:{k}@@", ""]
            pendenti = []
            testo = re.sub(r"^#+ ", "", r)
            testo = re.sub(r" · .*$", "", testo)
            for (ln, prefisso), chiavi in FIGURE.items():
                if ln == n and testo.startswith(prefisso):
                    pendenti = list(chiavi)
        out.append(r)
    return "\n".join(out[:-1])


def numera_equazioni(h, n):
    """Ancore `eq-N` davanti alle formule numerate della lezione. Ritorna (html, numeri trovati)."""
    trovati = {}

    def f(m):
        tex = html.unescape(m.group(1))
        nums = list(dict.fromkeys(re.findall(r"\\tag\{(\d+)\}", tex) + re.findall(r"\\quad\((\d+)\)", tex)))
        nuovi = []
        for k in nums:
            if k in trovati:
                print(f"  attenzione: eq. ({k}) compare due volte nella Lezione {n}")
            else:
                trovati[k] = tex
                nuovi.append(k)
        if not nuovi:
            return m.group(0)
        ancore = "".join(f'<span class="ea" id="eq-{k}"></span>' for k in nuovi)
        return f'{ancore}<div class="math block" data-eq="{" ".join(nuovi)}">{m.group(1)}</div>'
    h = re.sub(r'<div class="math block">(.*?)</div>', f, h, flags=re.S)
    return h, set(trovati)


_NON_LINKARE = {"a", "code", "pre", "svg", "summary", "script", "button", "h1", "h2", "h3", "h4", "h5", "h6"}


def collega_riferimenti(h, nums, n):
    """Nel testo «(10)» diventa un link all'equazione, con anteprima al passaggio del mouse."""
    out, prof, math = [], 0, None
    visti = []
    for tok in re.split(r"(<[^>]*>)", h):
        if tok.startswith("<"):
            mt = re.match(r"<(/?)([a-zA-Z0-9]+)", tok)
            if mt:
                chiude, nome = mt.group(1) == "/", mt.group(2).lower()
                if math:
                    if chiude and nome == math:
                        math = None
                elif not chiude and 'class="math' in tok:
                    math = nome
                elif nome in _NON_LINKARE:
                    prof += -1 if chiude else 1
            out.append(tok)
        elif prof or math:
            out.append(tok)
        else:
            def r(m):
                prima, dopo = tok[:m.start()], tok[m.end():]
                elenco = re.search(r"[:;] $", prima) and re.match(r" [a-zà-ù]", dopo)  # «; (2) eliminare…»: elenco numerato
                if m.group(1) in nums and not elenco:
                    visti.append(tok[max(0, m.start() - 30):m.end() + 10])
                    return f'<a class="eqref" href="#eq-{m.group(1)}" data-eq="{m.group(1)}">({m.group(1)})</a>'
                return m.group(0)
            out.append(re.sub(r"\((\d{1,2})\)", r, tok))
    if VERBOSO:
        for v in visti:
            print(f"   L{n} rif: …{v.strip()}…")
    return "".join(out)


VERBOSO = bool(__import__("os").environ.get("VERBOSO"))


def figure_html(h):
    def f(m):
        svg, didascalia = DISEGNI[m.group(1)]
        return f'<figure class="fig">{svg}<figcaption>{render_inline(didascalia)}</figcaption></figure>'
    return re.sub(r"<p>@@FIG:(\w+)@@</p>", f, h)


# ----------------------------------------------------------------------------------------------- lezioni

def corpo_lezione(cfg, corso, out):
    parti = re.split(r"(?m)^(?=## Lezione \d+)", corso)
    blocco = next(p for p in parti if p.startswith(f"## Lezione {cfg['n']} "))
    blocco = blocco.split("\n", 1)[1]
    blocco = re.sub(r"(?m)^\*Approfondimenti nel wiki.*$", "", blocco)
    if cfg["inizio"]:
        blocco = blocco[blocco.index(cfg["inizio"]):]
    blocco = inserisci_figure(blocco, cfg["n"])
    return titoli_con_pagine(wikilink_testo(blocco, out)).strip()


def concetto_html(nome, out, usati, cartella="concetti"):
    md = rimuovi_frontmatter((WIKI / cartella / f"{nome}.md").read_text(encoding="utf-8"))
    titolo = re.search(r"(?m)^# (.+)$", md).group(1).strip()
    pezzi = []
    sp = sezione(md, "Spiegazione")
    if sp:
        pezzi.append("#### Spiegazione\n\n" + demota(sp, 1))
    perche = sezione(md, "Perché importa")
    if perche:
        pezzi.append("#### Perché importa\n\n" + perche)
    der = sezione(md, "Derivazioni")
    esame = [r for r in md.split("\n") if r.startswith("> 🎯") and r not in (sp + der + perche)]
    corpo_der = ""
    if der:
        blocchi = re.split(r"(?m)^(?=### )", der)
        intro, resto = blocchi[0].strip(), blocchi[1:]
        if intro:
            corpo_der += intro + "\n\n"
        for b in resto:
            tit, _, testo = b.partition("\n")
            corpo_der += f"@@DET:{tit[4:].strip()}@@\n\n{testo.strip()}\n\n@@/DET@@\n\n"
    testo = "\n\n".join(pezzi)
    if esame:
        testo += "\n\n" + "\n".join(esame)
    testo = titoli_con_pagine(wikilink_testo(testo, out))
    corpo_der = titoli_con_pagine(wikilink_testo(corpo_der, out))
    h = post_html(render_md(testo))
    hd = post_html(render_md(corpo_der))

    def det(m):
        t = m.group(1)
        return f'<details class="der"><summary>{t}</summary>'
    hd = re.sub(r"<p>@@DET:(.*?)@@</p>", det, hd)
    hd = hd.replace("<p>@@/DET@@</p>", "</details>")
    h = con_id(h, usati, prefisso=slug(nome) + "-")
    hd = con_id(hd, usati, prefisso=slug(nome) + "-")
    if hd.strip():
        h += '<h4 class="sub">Dimostrazioni passo-passo</h4>' + hd
    return (f'<details class="conc"><summary><span class="n">{html.escape(titolo)}</span></summary>'
            f'<div class="cb">{h}</div></details>')


def esercizio_html(nome, out, usati):
    md = rimuovi_frontmatter((WIKI / "esercizi" / f"{nome}.md").read_text(encoding="utf-8"))
    titolo = re.search(r"(?m)^# (.+)$", md).group(1).strip()
    md = re.sub(r"(?m)^# .*\n", "", md)
    md = re.sub(r"(?ms)^_Aggiornato.*", "", md)
    md = demota(md, 2)
    h = post_html(render_md(titoli_con_pagine(wikilink_testo(md, out))))
    h = con_id(h, usati, prefisso=slug(nome) + "-")
    return (f'<details class="conc es"><summary><span class="n">Esercizio svolto · {html.escape(titolo)}</span></summary>'
            f'<div class="cb">{h}</div></details>')


def domande_html(cfg, out):
    md = rimuovi_frontmatter((WIKI / "fonti" / f"{cfg['fonte']}.md").read_text(encoding="utf-8"))
    sez = sezione(md, "Domande da esame")
    sez = re.sub(r"(?ms)^_Aggiornato.*", "", sez).strip()
    if cfg["domande_filtro"]:
        sez = "\n".join(r for r in sez.split("\n") if any(k in r for k in cfg["domande_filtro"]))
    return post_html(render_md(wikilink_testo(sez, out)))


def pagina_lezione(cfg, corso, out, precedente, successiva):
    usati = set()
    toc = []
    corpo = figure_html(post_html(render_md(corpo_lezione(cfg, corso, out))))
    corpo, numeri = numera_equazioni(corpo, cfg["n"])
    corpo = collega_riferimenti(corpo, numeri, cfg["n"])
    corpo = con_id(corpo, usati, toc)
    conc ="\n".join(concetto_html(c, out, usati) for c in cfg["concetti"])
    for e in cfg["esercizi"]:
        conc += "\n" + esercizio_html(e, out, usati)
    dom = domande_html(cfg, out)
    voci = []
    for liv, i, t in toc:
        voci.append(f'<li class="l{liv}"><a href="#{i}">{t}</a></li>')
    indice = (f'<details class="toc"><summary>Indice della lezione</summary><ul>{"".join(voci)}'
              f'<li class="l3"><a href="#approfondimenti">Spiegazioni e dimostrazioni passo-passo</a></li>'
              f'<li class="l3"><a href="#domande">Domande da esame</a></li></ul></details>')
    nav = '<nav class="pn">'
    nav += f'<a href="{precedente["slug"]}.html">← Lezione {precedente["n"]}</a>' if precedente else "<span></span>"
    nav += f'<a href="{successiva["slug"]}.html">Lezione {successiva["n"]} →</a>' if successiva else "<span></span>"
    nav += "</nav>"
    corpo_pagina = f"""
<p class="crumb"><a href="index.html">Intercorso</a> · Lezione {cfg['n']}</p>
<h1>{html.escape(cfg['titolo'])}</h1>
<p class="breve">{html.escape(cfg['breve'])}</p>
{indice}
<section id="corso"><h2 class="ps">Il corso, slide per slide</h2>
{corpo}
</section>
<section id="approfondimenti"><h2 class="ps">Spiegazioni e dimostrazioni passo-passo</h2>
<p class="nota">Apri una voce per leggere la spiegazione in parole semplici e le dimostrazioni svolte riga per riga (🧩 = passaggio ricostruito da me).</p>
{conc}
</section>
<section id="domande"><h2 class="ps">Domande da esame</h2>
{dom}
</section>
{nav}
"""
    return pagina(f"Lezione {cfg['n']} · {cfg['titolo']}", corpo_pagina, cfg["slug"])


def pagina_indice(out):
    card = []
    for c in LEZIONI:
        toc = [re.sub(r'<span class="pag">.*?</span>', "", x).strip() for x in re.findall(r"(?m)^### (.+)$", corpo_lezione(c, CORSO, out))]
        li = "".join(f"<li>{html.escape(re.sub(r'<[^>]+>', '', t))}</li>" for t in toc)
        card.append(f'<a class="card" href="{c["slug"]}.html"><span class="num">Lezione {c["n"]}</span>'
                    f'<strong>{html.escape(c["titolo"])}</strong><span class="b">{html.escape(c["breve"])}</span>'
                    f'<ul>{li}</ul></a>')
    corpo = f"""
<h1>Trasmissione dei Segnali Digitali</h1>
<p class="breve">Appunti per la <strong>prima prova intercorso</strong>: dal quantizzatore uniforme (SNR e legge dei 6 dB/bit) e dalla quantizzazione non uniforme alla rappresentazione di Rice dei processi aleatori. Segue l'ordine delle lezioni.</p>
<div class="cards">{"".join(card)}</div>
<h2 class="ps">Come si legge</h2>
<ul class="legenda">
<li>Ogni lezione ha tre parti: <strong>il corso slide per slide</strong> (come nelle slide), le <strong>spiegazioni e dimostrazioni</strong> passo-passo (a comparsa) e le <strong>domande da esame</strong>.</li>
<li>Le equazioni numerate sono quelle delle slide. I disegni sono costruiti dalle formule delle slide.</li>
<li><span class="chip formula">🧮</span> formula da sapere a memoria · <span class="chip esame">🎯</span> punto da esame · <span class="chip mia">🧩</span> passaggio ricostruito da me · <span class="chip conn">💡</span> collegamento · <span class="chip avv">⚠️</span> refuso o contraddizione nella slide · <span class="chip dub">❓</span> salto non ricostruito.</li>
<li>Tocca un'immagine per ingrandirla. I pulsanti <strong>A−</strong> e <strong>A+</strong> in alto cambiano la dimensione del testo.</li>
<li>La Lezione 6 (laboratorio Matlab) non è materia d'esame, per questo non compare. Le Lezioni 1–2 e la prima parte della 3 (campionamento e conversione A/D) precedono l'intercorso; della quantizzazione uniforme è inclusa la parte che serve alla legge dei 6 dB/bit.</li>
</ul>
"""
    return pagina("Trasmissione dei Segnali Digitali · Intercorso", corpo, "index")


# ----------------------------------------------------------------------------------------------- pagina, stile, script

def pagina(titolo, corpo, slug_corrente):
    nav = ['<a href="index.html" class="home" aria-label="indice">⌂</a>']
    for c in LEZIONI:
        att = ' aria-current="page"' if c["slug"] == slug_corrente else ""
        nav.append(f'<a href="{c["slug"]}.html"{att}>L{c["n"]}</a>')
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titolo)}</title>
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{KATEX}katex.min.css">
<link rel="stylesheet" href="style.css">
<script>{TEMA_INIZIALE}</script>
<script defer src="{KATEX}katex.min.js"></script>
<script defer src="app.js"></script></head>
<body><header class="top"><nav>{"".join(nav)}</nav><span class="ctl"><span class="tm" role="group" aria-label="tema"><button data-t="sistema" title="Tema del sistema" aria-label="tema del sistema">{ICONA_SISTEMA}</button><button data-t="chiaro" title="Tema chiaro" aria-label="tema chiaro">{ICONA_SOLE}</button><button data-t="scuro" title="Tema scuro" aria-label="tema scuro">{ICONA_LUNA}</button></span><span class="fs"><button id="fm" aria-label="testo più piccolo">A−</button><button id="fp" aria-label="testo più grande">A+</button></span></span></header>
<main>{corpo}</main>
<footer>Appunti personali del corso di Trasmissione dei Segnali Digitali (LM Ingegneria Informatica, UNINA). Generato dal wiki con <code>output/crea_sito.py</code>.</footer>
<div id="lb" hidden></div><a id="su" href="#" hidden aria-label="torna su">↑</a>
</body></html>"""


_SVG = '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">{}</svg>'
ICONA_SISTEMA = _SVG.format('<circle cx="8" cy="8" r="6"/><path d="M8 2a6 6 0 0 1 0 12z" fill="currentColor" stroke="none"/>')
ICONA_SOLE = _SVG.format('<circle cx="8" cy="8" r="3" fill="currentColor"/><path d="M8 1.2v2M8 12.8v2M1.2 8h2M12.8 8h2M3.2 3.2l1.4 1.4M11.4 11.4l1.4 1.4M3.2 12.8l1.4-1.4M11.4 4.6l1.4-1.4"/>')
ICONA_LUNA = _SVG.format('<path d="M13.2 9.6A5.8 5.8 0 1 1 6.4 2.8a4.6 4.6 0 0 0 6.8 6.8z" fill="currentColor"/>')

TEMA_INIZIALE = ("try{var t=localStorage.getItem('tsd-tema');"
                 "if(t==='chiaro')document.documentElement.setAttribute('data-theme','light');"
                 "else if(t==='scuro')document.documentElement.setAttribute('data-theme','dark');}catch(e){}")

_CHIARO = "--bg:#fbfaf7;--card:#fff;--ink:#1f1f1e;--ink2:#5d5c57;--line:#d9d7cf;--a1:#1f6fd6;--a2:#d9541e;--a3:#2a8f5a;--a4:#8a4fc4;--soft:#eef4fc;--soft2:#fbefe8;--code:#f2f1ec;color-scheme:light"
_SCURO = "--bg:#161615;--card:#1f1f1e;--ink:#ecebe6;--ink2:#a9a79f;--line:#3a3935;--a1:#6fa8f5;--a2:#f08a5d;--a3:#5cc490;--a4:#b98ae8;--soft:#1d2a3d;--soft2:#3a2a22;--code:#2a2926;color-scheme:dark"

STILE = (":root{" + _CHIARO + "}\n"
         "@media (prefers-color-scheme:dark){:root:not([data-theme=\"light\"]){" + _SCURO + "}}\n"
         ":root[data-theme=\"dark\"]{" + _SCURO + "}\n") + r"""
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:12px 16px 40px}
a{color:var(--a1)}
.top{position:sticky;top:0;z-index:20;display:flex;justify-content:space-between;align-items:center;gap:8px;padding:8px 12px;background:var(--bg);border-bottom:1px solid var(--line)}
.top nav{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none;flex:1 1 auto;min-width:0}
.top nav a{padding:4px 8px;border:1px solid var(--line);border-radius:16px;text-decoration:none;color:var(--ink);font-weight:600;font-size:13px;white-space:nowrap}
.tm button{display:inline-flex;align-items:center;justify-content:center;width:30px;padding:4px 0}
.top nav a[aria-current],.top nav a.home{background:var(--a1);color:#fff;border-color:var(--a1)}
.ctl{display:flex;gap:7px;flex:none}
.tm,.fs{display:inline-flex;gap:3px}
.tm button,.fs button{font:600 14px system-ui;padding:4px 7px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);cursor:pointer}
.tm button[aria-pressed="true"]{background:var(--a1);color:#fff;border-color:var(--a1)}
h1{font-size:1.65em;line-height:1.2;margin:.3em 0 .2em}
h2.ps{font-size:1.3em;margin:1.8em 0 .4em;padding:.35em .6em;background:var(--a1);color:#fff;border-radius:8px}
h3{font-size:1.15em;margin:1.7em 0 .3em;padding-bottom:.15em;border-bottom:2px solid var(--a1)}
h4{font-size:1.02em;margin:1.2em 0 .2em;color:var(--a1)}
h4.sub{margin-top:1.6em;border-top:1px dashed var(--line);padding-top:.7em}
h5,h6{font-size:1em;margin:1em 0 .2em}
.crumb,.meta{color:var(--ink2);font-size:.88em;margin:.2em 0}
.breve{font-size:1.02em}
p,li{overflow-wrap:break-word}
ul,ol{padding-left:1.3em}li{margin:.25em 0}
code{background:var(--code);padding:0 4px;border-radius:4px;font-size:.9em}
pre{background:var(--code);padding:10px;overflow-x:auto;border-radius:8px;font-size:.85em}
.math.block{overflow-x:auto;overflow-y:hidden;padding:2px 0;margin:.4em 0}
summary .katex,h3 .katex,h4 .katex,li .katex,td .katex{white-space:normal}
.math.inline.wide{display:block;overflow-x:auto;overflow-y:hidden;max-width:100%;margin:.2em 0}
.katex{font-size:1.04em}
.ea{display:block;height:0;scroll-margin-top:64px}
a.eqref{text-decoration:none;border-bottom:1px dotted var(--a1);cursor:help;white-space:nowrap}
a.eqref:hover,a.eqref:focus-visible{background:var(--soft);border-radius:3px}
.math.block.flash{background:var(--soft);transition:background .4s}
#eqpop{position:fixed;z-index:40;width:max-content;max-width:min(94vw,760px);background:var(--card);border:1px solid var(--a1);border-radius:10px;box-shadow:0 8px 28px rgba(0,0,0,.28);padding:6px 12px 6px}
#eqpop[hidden]{display:none}
#eqpop .ph{display:flex;justify-content:space-between;gap:18px;font-size:.78em;color:var(--ink2);margin-bottom:2px}
#eqpop .ph a{white-space:nowrap}
#eqpop .math.block{margin:.2em 0}
#eqpop .katex-display{margin:0}
.katex-display{margin:.2em 0}
.tw{overflow-x:auto;margin:.8em 0;position:relative}
.math.block,.math.inline.wide{position:relative}
table{border-collapse:collapse;font-size:.92em}th,td{border:1px solid var(--line);padding:4px 9px;vertical-align:top}th{background:var(--code)}
blockquote{margin:.8em 0;padding:.4em .9em;border-left:4px solid var(--line);background:var(--code);border-radius:0 8px 8px 0}
blockquote p{margin:.3em 0}
.co.formula{border-color:var(--a1);background:var(--soft)}
.co.esame{border-color:var(--a3)}
.co.mia{border-color:var(--a4)}
.co.conn{border-color:var(--a2);background:var(--soft2)}
.co.avv{border-color:#d4a017}
.co.dub{border-color:#c0392b}
.chip{display:inline-block;padding:0 5px;border-radius:6px;border-left:4px solid var(--line);background:var(--code)}
.chip.formula{border-color:var(--a1)}.chip.esame{border-color:var(--a3)}.chip.mia{border-color:var(--a4)}.chip.conn{border-color:var(--a2)}.chip.avv{border-color:#d4a017}.chip.dub{border-color:#c0392b}
img{max-width:100%;height:auto;display:block;margin:.8em auto;border:1px solid var(--line);border-radius:6px;background:#fff}
img.zoom{cursor:zoom-in}
figure.fig{margin:1em 0;padding:8px 6px 4px;background:var(--card);border:1px solid var(--line);border-radius:10px}
figure.fig svg{display:block;width:100%;max-width:460px;height:auto;margin:0 auto}
figcaption{font-size:.84em;color:var(--ink2);margin:.4em 4px .3em;text-align:left}
details.toc,details.conc,details.der{margin:.6em 0;border:1px solid var(--line);border-radius:10px;background:var(--card)}
details>summary{cursor:pointer;padding:.55em .8em;font-weight:600;list-style:none}
details>summary::-webkit-details-marker{display:none}
details>summary::before{content:"▸";display:inline-block;width:1.1em;color:var(--a1)}
details[open]>summary::before{content:"▾"}
details.conc>summary{background:var(--soft);border-radius:10px;font-size:1.04em}
details.conc.es>summary{background:var(--soft2)}
details.conc[open]>summary{border-radius:10px 10px 0 0}
details.der{margin:.5em 0;background:var(--bg)}
details.der>summary{font-weight:500;font-size:.96em}
.cb,details.der>*:not(summary),details.toc>ul{padding:0 .9em}
.cb{padding-bottom:.5em}
details.der>*:not(summary):last-child{padding-bottom:.6em}
.toc ul{list-style:none;margin:0;padding-bottom:.6em}.toc li{margin:.3em 0}.toc li.l4{padding-left:1.2em;font-size:.9em}.toc a{text-decoration:none}
.cards{display:grid;gap:12px;margin:1em 0}
.card{display:block;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);text-decoration:none}
.card .num{display:block;color:var(--a1);font-weight:700;font-size:.85em;text-transform:uppercase;letter-spacing:.04em}
.card strong{display:block;font-size:1.12em;margin:.1em 0}
.card .b{display:block;color:var(--ink2);font-size:.92em;margin-bottom:.3em}
.card ul{margin:.3em 0 0;font-size:.86em;color:var(--ink2);columns:1}
.legenda li{margin:.5em 0}
.nota{color:var(--ink2);font-size:.92em}
.pn{display:flex;justify-content:space-between;margin-top:2em;font-weight:600}
footer{max-width:760px;margin:0 auto;padding:0 16px 30px;color:var(--ink2);font-size:.8em}
#lb{position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.88);overflow:auto;padding:10px}
#lb[hidden]{display:none}#lb img{max-width:none;width:min(1100px,230%);margin:0 auto;border:0;background:#fff}
#su{position:fixed;right:14px;bottom:14px;width:42px;height:42px;line-height:40px;text-align:center;border-radius:50%;background:var(--a1);color:#fff;text-decoration:none;font-size:20px;z-index:30}
#su[hidden]{display:none}
/* disegni SVG */
svg .ln{stroke:var(--ink);fill:none;stroke-width:1.3}
svg .ax{stroke:var(--ink2);fill:none;stroke-width:1.1}
svg .gd{stroke:var(--ink2);fill:none;stroke-width:1;stroke-dasharray:3 3;opacity:.8}
svg .ar2{stroke:var(--a1);fill:none;stroke-width:1.2}
svg .cv,svg .cv2,svg .cv3,svg .cv4{fill:none;stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round}
svg .cv{stroke:var(--a1)}svg .cv2{stroke:var(--a2)}svg .cv3{stroke:var(--a3)}svg .cv4{stroke:var(--a4)}
svg .dash{stroke-dasharray:6 4}svg .dash2{stroke-dasharray:2 3}
svg .ev{stroke-width:3.6}
svg .pt{fill:var(--card);stroke-width:2}
svg .fl{fill:var(--a1);fill-opacity:.2;stroke:none}
svg .fl2{fill:var(--a2);fill-opacity:.35;stroke:none}
svg .ban{fill:none;stroke:var(--a2);stroke-width:1;stroke-dasharray:3 3}
svg .bx{fill:var(--card);stroke:var(--ink2);stroke-width:1.3}
svg .bx1{fill:var(--soft);stroke:var(--a1)}svg .bx2{fill:var(--soft2);stroke:var(--a2)}
svg .mk{fill:var(--ink2)}
svg text{fill:var(--ink);font:12.5px system-ui,-apple-system,"Segoe UI",sans-serif}
svg text.ts{font-size:11px;fill:var(--ink2)}
svg text.tb{font-weight:700}
svg text.a1{fill:var(--a1)}svg text.a2{fill:var(--a2)}svg text.a3{fill:var(--a3)}svg text.a4{fill:var(--a4)}
@media (min-width:700px){body{font-size:18px}.cards{grid-template-columns:1fr 1fr}}
"""

SCRIPT = r"""
(function () {
  var root = document.documentElement;
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var size = parseFloat(lsGet('tsd-fs')) || 17;
  function applica() { document.body.style.fontSize = size + 'px'; }
  applica();
  var fm = document.getElementById('fm'), fp = document.getElementById('fp');
  if (fm) fm.onclick = function () { size = Math.max(13, size - 1); lsSet('tsd-fs', size); applica(); fitAll(); };
  if (fp) fp.onclick = function () { size = Math.min(26, size + 1); lsSet('tsd-fs', size); applica(); fitAll(); };

  // tema: sistema (segue il dispositivo), chiaro, scuro
  var temi = { sistema: null, chiaro: 'light', scuro: 'dark' };
  var tema = lsGet('tsd-tema'); if (!(tema in temi)) tema = 'sistema';
  function temaApplica() {
    if (temi[tema]) root.setAttribute('data-theme', temi[tema]); else root.removeAttribute('data-theme');
    document.querySelectorAll('.tm button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.t === tema ? 'true' : 'false'); });
  }
  temaApplica();
  document.querySelectorAll('.tm button').forEach(function (b) { b.onclick = function () { tema = b.dataset.t; lsSet('tsd-tema', tema); temaApplica(); }; });

  // una formula troppo larga viene rimpicciolita finché sta in una riga (sotto la soglia resta lo scorrimento)
  var MIN = 0.3;
  function fit(el) {
    if (!el.dataset.ok) return;
    var blocco = el.classList.contains('block');
    el.style.fontSize = '';
    if (!blocco && !el.closest('summary')) {
      var c = el.closest('p,li,td,th,blockquote,div');
      el.classList.remove('wide');
      if (c && c.clientWidth && el.getBoundingClientRect().width > c.clientWidth - 8) el.classList.add('wide');
    }
    if (!blocco && !el.classList.contains('wide')) return;
    if (!el.clientWidth) return;
    var k = 1;
    for (var i = 0; i < 4 && k > MIN; i++) {
      var w = larghezza(el);
      if (w <= el.clientWidth - 1) break;
      k = Math.max(MIN, k * (el.clientWidth - 1) / w * 0.985);
      el.style.fontSize = k + 'em';
    }
  }
  // larghezza occupata dalla formula (più il numero d'equazione, che sta a destra)
  function larghezza(el) {
    var basi = el.querySelectorAll('.katex-html > .base');
    if (!basi.length) return el.scrollWidth;
    var l = 1e9, r = -1e9;
    basi.forEach(function (b) { var q = b.getBoundingClientRect(); l = Math.min(l, q.left); r = Math.max(r, q.right); });
    var tag = el.querySelector('.tag');
    return (r - l) + (tag ? tag.getBoundingClientRect().width + 12 : 0);
  }
  function fitAll() { document.querySelectorAll('.math[data-ok]').forEach(fit); }
  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(fitAll, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitAll);

  function rendi(el) {
    if (el.dataset.ok || !window.katex) return;
    el.dataset.ok = '1';
    try { katex.render(el.textContent, el, { displayMode: el.classList.contains('block'), throwOnError: false, strict: false }); } catch (e) {}
    fit(el);
  }
  function rendiIn(nodo) { nodo.querySelectorAll('.math').forEach(function (e) { rendi(e); fit(e); }); }
  function chiuso(el) { if (el.closest('summary')) return false; var d = el.closest('details'); while (d) { if (!d.open) return true; d = d.parentElement && d.parentElement.closest('details'); } return false; }
  function avvia() {
    document.querySelectorAll('.math').forEach(function (el) { if (!chiuso(el)) rendi(el); });
    document.querySelectorAll('details').forEach(function (d) { d.addEventListener('toggle', function () { if (d.open) rendiIn(d); }); });
    // apre i dettagli che contengono l'ancora richiesta
    function apriAncora() {
      var id = decodeURIComponent(location.hash.slice(1)); if (!id) return;
      var el = document.getElementById(id); if (!el) return;
      var d = el.closest('details');
      while (d) { d.open = true; d = d.parentElement && d.parentElement.closest('details'); }
      rendiIn(document.body); el.scrollIntoView();
    }
    window.addEventListener('hashchange', apriAncora); apriAncora();
    setTimeout(fitAll, 500);
    document.body.setAttribute('data-pronto', '1');
  }
  window.addEventListener('load', avvia);
  // lightbox
  var lb = document.getElementById('lb');
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.tagName === 'IMG' && t.classList.contains('zoom')) { lb.innerHTML = '<img src="' + t.src + '" alt="">'; lb.hidden = false; }
    else if (lb && !lb.hidden) { lb.hidden = true; lb.innerHTML = ''; }
  });
  // anteprima delle equazioni richiamate nel testo, ad esempio «(10)»
  var eqTex = {}, eqEl = {};
  document.querySelectorAll('.math[data-eq]').forEach(function (b) {
    var tex = b.textContent;
    b.dataset.eq.split(' ').forEach(function (n) { eqTex[n] = tex; eqEl[n] = b; });
  });
  var pop = document.createElement('div'); pop.id = 'eqpop'; pop.hidden = true; document.body.appendChild(pop);
  var popT = null, popA = null;
  var tocco = !(window.matchMedia && matchMedia('(hover: hover)').matches);
  function popNascondi() { clearTimeout(popT); pop.hidden = true; popA = null; }
  function popMostra(a) {
    var n = a.dataset.eq;
    if (!eqTex[n] || !window.katex) return;
    clearTimeout(popT); popA = a;
    pop.innerHTML = '<div class="ph"><span>Equazione (' + n + ')</span><a href="#eq-' + n + '">vai all’equazione ↓</a></div><div class="math block"></div>';
    var m = pop.lastChild; m.dataset.ok = '1';
    pop.hidden = false;
    var tex = eqTex[n].replace(/\\tag\{\d+\}/g, '');
    try { katex.render(tex, m, { displayMode: true, throwOnError: false, strict: false }); } catch (e) {}
    fit(m);
    var r = a.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight;
    var x = Math.min(Math.max(8, r.left - 16), Math.max(8, window.innerWidth - w - 8));
    var y = r.bottom + 6;
    if (y + h > window.innerHeight - 8 && r.top - h - 6 > 8) y = r.top - h - 6;
    pop.style.left = x + 'px'; pop.style.top = Math.max(8, y) + 'px';
  }
  function flash(n) {
    var b = eqEl[n]; if (!b) return;
    b.classList.add('flash'); setTimeout(function () { b.classList.remove('flash'); }, 1800);
  }
  function flashHash() { var m = /^#eq-(\d+)$/.exec(location.hash); if (m) flash(m[1]); }
  window.addEventListener('hashchange', flashHash); window.addEventListener('load', flashHash);
  function eqLink(t) { return t.closest ? t.closest('a.eqref') : null; }
  document.addEventListener('mouseover', function (e) {
    if (tocco) return;
    var a = eqLink(e.target);
    if (a) { if (a === popA && !pop.hidden) { clearTimeout(popT); return; } clearTimeout(popT); popT = setTimeout(function () { popMostra(a); }, 120); }
    else if (e.target.closest && e.target.closest('#eqpop')) clearTimeout(popT);
  });
  document.addEventListener('mouseout', function (e) {
    if (tocco) return;
    if (eqLink(e.target) || (e.target.closest && e.target.closest('#eqpop'))) { clearTimeout(popT); popT = setTimeout(popNascondi, 260); }
  });
  document.addEventListener('focusin', function (e) { var a = eqLink(e.target); if (a) popMostra(a); });
  document.addEventListener('focusout', function (e) { if (eqLink(e.target)) popT = setTimeout(popNascondi, 200); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') popNascondi(); });
  document.addEventListener('click', function (e) {
    var a = eqLink(e.target);
    if (a && tocco) { e.preventDefault(); if (popA === a && !pop.hidden) popNascondi(); else popMostra(a); return; }
    if (!(e.target.closest && e.target.closest('#eqpop a'))) { if (!(e.target.closest && e.target.closest('#eqpop'))) popNascondi(); return; }
    popNascondi();
  });
  window.addEventListener('scroll', function () { if (!pop.hidden) popNascondi(); }, { passive: true });

  var su = document.getElementById('su');
  window.addEventListener('scroll', function () { if (su) su.hidden = window.scrollY < 600; }, { passive: true });
})();
"""

CORSO = ""


def costruisci(out):
    global CORSO
    CORSO = (WIKI / "corso-completo.md").read_text(encoding="utf-8")
    if out.exists():
        for p in out.iterdir():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
    out.mkdir(parents=True, exist_ok=True)
    (out / "style.css").write_text(STILE, encoding="utf-8")
    (out / "app.js").write_text(SCRIPT, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    for i, c in enumerate(LEZIONI):
        prec = LEZIONI[i - 1] if i else None
        succ = LEZIONI[i + 1] if i + 1 < len(LEZIONI) else None
        (out / f"{c['slug']}.html").write_text(pagina_lezione(c, CORSO, out, prec, succ), encoding="utf-8")
        print("scritto", c["slug"])
    (out / "index.html").write_text(pagina_indice(out), encoding="utf-8")
    print("scritto index, immagini:", len(COPIATE))


if __name__ == "__main__":
    destinazione = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.gettempdir()) / "sito-tsd"
    costruisci(destinazione)
    print(destinazione)
