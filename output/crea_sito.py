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
    dict(n=1, slug="lezione-1", data="15/09", titolo="Introduzione al corso",
         breve="Il processo di comunicazione, gli elementi di un sistema di comunicazione digitale, rigenerazione e vantaggi del digitale.",
         concetti=["sistema-comunicazione-digitale", "entità/ripetitore-rigenerativo"], fonte="intro-corso", esercizi=[]),
    dict(n=2, slug="lezione-2", data="16/09", titolo="Elementi di teoria della probabilità",
         breve="Spazio di probabilità, probabilità condizionale, Bayes, variabili aleatorie notevoli, gaussiana, media, varianza, coppie, correlazione.",
         concetti=["spazio-di-probabilita", "probabilita-condizionale", "probabilita-totale-e-bayes", "variabile-aleatoria",
                   "variabili-aleatorie-notevoli", "variabile-aleatoria-gaussiana", "funzione-di-variabile-aleatoria", "media-e-varianza",
                   "coppie-di-variabili-aleatorie", "correlazione-e-covarianza"],
         fonte="elementi-teoria-probabilita", esercizi=["calcolo-probabilita-eventi", "cdf-pdf-variabili-notevoli"]),
    dict(n=3, slug="lezione-3", data="22/09", titolo="Campionamento e conversione A/D e D/A",
         breve="Teorema del campionamento, aliasing, interpolazione; quantizzazione uniforme e legge dei 6 dB/bit, Lloyd-Max, companding.",
         concetti=["conversione-ad-da", "teorema-del-campionamento", "interpolazione", "aliasing", "quantizzazione-uniforme",
                   "disuguaglianza-di-chebyshev", "snr-di-quantizzazione", "quantizzazione-non-uniforme", "companding"],
         fonte="campionamento-conversione-ad-da", esercizi=["campionamento-e-aliasing", "dimensionamento-quantizzatore"]),
    dict(n=4, slug="lezione-4", data="25/09", titolo="Rappresentazione complessa in banda base",
         breve="Segnali in banda base e passa-banda, segnale analitico, inviluppo complesso, componenti I/Q, up/down-conversion, filtri.",
         concetti=["modulazione-digitale", "segnali-banda-base-e-passa-banda", "segnale-analitico", "inviluppo-complesso",
                   "upconversion-e-downconversion", "equivalente-banda-base-dei-filtri"],
         fonte="rappresentazione-complessa-banda-base", esercizi=[]),
    dict(n=5, slug="lezione-5", data="29/09", titolo="Laboratorio Matlab: conversione A/D e D/A",
         breve="Lo script AD_conversion.m commentato: spettro, campionamento, interpolazione, quantizzazione, SNR. Non è materia d'esame.",
         concetti=["laboratorio/lab-setup-e-spettro", "laboratorio/lab-campionamento", "laboratorio/lab-interpolazione",
                   "laboratorio/lab-quantizzazione", "laboratorio/lab-snr"],
         fonte="laboratorio-conversione-ad", esercizi=[]),
    dict(n=6, slug="lezione-6", data="05/10", titolo="Processi aleatori",
         breve="Processi stocastici, momenti, stazionarietà, acf, passaggio attraverso filtri LTI, PSD, processo gaussiano, tempo discreto.",
         concetti=["processo-aleatorio", "momenti-di-un-processo", "stazionarieta", "autocorrelazione-processi-wss",
                   "processi-e-sistemi-lti", "densita-spettrale-di-potenza", "processo-gaussiano"],
         fonte="processi-aleatori", esercizi=["calcolo-densita-spettrale"]),
    dict(n=7, slug="lezione-7", data="13/10", titolo="Rappresentazione di Rice per i processi aleatori",
         breve="Inviluppo complesso e componenti in quadratura di un processo passa-banda, loro PSD, rumore in banda.",
         concetti=["processi-passa-banda", "psd-componenti-in-quadratura", "rumore-in-banda-passante"],
         fonte="rappresentazione-processi-passa-banda", esercizi=[]),
    dict(n=8, slug="lezione-8", data="16/10", titolo="Principi di modulazione",
         breve="Modulatore digitale, baud rate, compromesso potenza-banda, spazio dei segnali, modulazione lineare (PAM, PSK, QAM), PSD, FSK.",
         concetti=["principi-di-modulazione", "spazio-dei-segnali", "modulazione-lineare", "modulazione-ortogonale"],
         fonte="principles-of-modulation", esercizi=[]),
    dict(n=9, slug="lezione-9", data="20/10", titolo="Elementi di teoria della rivelazione",
         breve="Test di ipotesi in AWGN, criteri MAP e ML, teorema dell'irrilevanza, filtro adattato, minima distanza e regioni di Voronoi.",
         concetti=["rivelazione-map-ml", "ricevitore-ottimo-awgn"], fonte="elementi-teoria-rivelazione", esercizi=[]),
    dict(n=10, slug="lezione-10", data="28/10", titolo="Prestazioni delle modulazioni binarie e della QPSK",
         breve="Probabilità d'errore di on-off, antipodale e ortogonale, formula con la distanza, QPSK: SER e BER.",
         concetti=["probabilita-errore-binaria", "probabilita-errore-m-aria"], fonte="appunti-lezione-28-ottobre", esercizi=[]),
    dict(n=11, slug="lezione-11", data="02/11", titolo="Union bound e approssimazione dei primi vicini",
         breve="Union bound e pairwise error probability, approssimazione dei primi vicini, 16-QAM, modulazioni ortogonali M-arie.",
         concetti=["probabilita-errore-m-aria"], fonte="appunti-lezione-2-novembre", esercizi=[]),
    dict(n=12, slug="lezione-12", data="03/11", titolo="Parametri globali delle modulazioni e capacità di canale",
         breve="Informazione mutua, capacità e canale AWGN; banda di Shannon, efficienza spettrale e in potenza; frontiera di Shannon; link budget.",
         concetti=["informazione-mutua-e-capacita", "parametri-globali-modulazioni", "limite-di-shannon", "link-budget"],
         fonte="parametri-globali-e-capacita", esercizi=["link-budget-wlan"]),
    dict(n=13, slug="lezione-13", data="09/11", titolo="Stima dei parametri per la sincronizzazione",
         breve="Ritardo e offset dell'oscillatore, timing e portante, stima ML (ampiezza training-based e blind, fase), PLL e Costas loop.",
         concetti=["sincronizzazione", "stima-dei-parametri", "phase-locked-loop"],
         fonte="parameter-estimation-synchronization", esercizi=[]),
    dict(n=14, slug="lezione-14", data="16/11 e 23/11", titolo="Segnalazione su canali a banda limitata",
         breve="Interferenza intersimbolica, criterio di Nyquist, coseno rialzato e filtri RRC, equalizzazione frazionaria, ZF e MMSE, MLSE e algoritmo di Viterbi.",
         concetti=["interferenza-intersimbolica", "criterio-di-nyquist", "equalizzazione", "entità/algoritmo-di-viterbi"],
         fonte="signaling-bandlimited-channels", esercizi=[]),
]
for _c in LEZIONI:
    _c.setdefault("inizio", None)
    _c.setdefault("domande_filtro", None)

# sezioni del corso completo che il sito non mostra (organizzazione del corso, non argomenti): (lezione, inizio del titolo)
ESCLUDI = [(1, "Organizzazione e programma")]

# percorso della prima prova intercorso: (lezione, titolo della sezione da cui partire o None, nota)
INTERCORSO = [
    (3, "Relazione ingresso-uscita del quantizzatore", "dalla quantizzazione uniforme (SNR e legge dei 6 dB/bit) a Lloyd-Max e al companding"),
    (4, None, "tutta la lezione"),
    (6, None, "tutta la lezione"),
    (7, None, "tutta la lezione"),
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
    (6, "Appunti — Sinusoide a fase casuale"): ["realizzazioni"],
    (6, "Slide 13 — Processi stazionari in senso lato"): ["stazionarieta"],
    (6, "Slide 16 — Significato fisico della acf"): ["acf"],
    (6, "Slide 19 — Processi indipendenti"): ["implicazioni"],
    (6, "Slide 28 — PSD e sistemi LTI"): ["lti"],
    (6, "Slide 29–30 — Significato fisico della PSD"): ["psd_filtro"],
    (7, "Slide 8 e appunti"): ["catena_psd"],
    (7, "Slide 9 e appunti"): ["simmetria"],
    (7, "Slide 12–13"): ["rumore"],
    (8, "Slide 4–5 — Esempio di Benedetto-Biglieri"): ["forme_mary"],
    (8, "Slide 10 e appunti — Descrizione nello spazio dei segnali"): ["base_ortonormale"],
    (8, "Slide 13–14 — NRZ e RZ"): ["nrz_rz"],
    (8, "Slide 15 — I/Q e conversione"): ["up_down"],
    (8, "Slide 17–18 — QAM e PAM"): ["costellazioni_lineari"],
    (8, "Slide 20–21 — Occupazione spettrale"): ["psd_sinc2"],
    (8, "Slide 22–23 — Modulazione ortogonale"): ["fsk_ortogonalita"],
    (9, "Dispense p. 4 e appunti — Criterio MAP"): ["onoff_decisione"],
    (9, "Dispense p. 7 e appunti — Correlatore e filtro adattato"): ["ricevitore_correlatori"],
    (9, "Dispense p. 8–10 e appunti — Demodulatore a minima distanza"): ["voronoi"],
    (10, "Segnalazione on-off"): ["onoff_decisione"],
    (10, "Modulazione binaria generica"): ["ber_binarie"],
    (10, "QPSK"): ["qpsk_regioni"],
    (11, "Union bound"): ["union_bound"],
    (11, "Esempio: 16-QAM"): ["qam16_vicini"],
    (12, "Slide 4 — Informazione mutua"): ["canale"],
    (12, "Slide 5 — Informazione mutua ed entropia"): ["entropie"],
    (12, "Slide 9 — Interpretazione della capacità"): ["capacita"],
    (12, "Slide 15–16 — Efficienza in potenza"): ["costellazioni_etap"],
    (12, "Slide 21 — Frontiera di Shannon"): ["piano_shannon"],
    (12, "Slide 31 — Path loss ammissibile"): ["bilancio_wlan"],
    (13, "Slide 3 e appunti — Effetto di ritardo"): ["sync_costellazione"],
    (13, "Slide 4 e appunti — Derivazione del modello (1/4)"): ["downconv_lo"],
    (13, "Slide 8 e appunti — Compiti e fasi"): ["acq_tracking"],
    (13, "Slide 11 e appunti — Il modello dei dati"): ["famiglia_pdf"],
    (13, "Slide 19 e appunti — Blind approach (2/2)"): ["blind_miscela", "tanh_soft"],
    (13, "Slide 24 — La funzione da massimizzare"): ["fase_ml"],
    (13, "Slide 30 e appunti — La struttura del PLL"): ["pll"],
    (13, "Slide 32 e appunti — Il termine d'errore"): ["curva_s"],
    (13, "Slide 33 — Costas loop"): ["costas"],
    (14, "Slide 3 e appunti — Introduzione (2/2)"): ["isi_impulsi"],
    (14, "Slide 6–7 — Effetto dell'ISI"): ["ber_floor"],
    (14, "Slide 9 e appunti — Modello del sistema"): ["sistema_bandlimitato"],
    (14, "Slide 17 — Il criterio nel dominio della frequenza (2/2)"): ["nyquist_repliche"],
    (14, "Slide 18–19 e appunti — Impulso di Nyquist ideale"): ["banda_minima"],
    (14, "Slide 20–21 — Impulso di Nyquist ideale"):["nyquist_bande", "sinc_treno"],
    (14, "Slide 26–27 — Raised cosine"): ["coseno_rialzato"],
    (14, "Slide 28–29 — Raised cosine"): ["rc_impulso"],
    (14, "Slide 30 — Osservazioni"): ["radice_nyquist"],
    (14, "Slide 34–35 — Tipi di equalizzatori"):["equalizzatori"],
    (14, "Slide 38 — Equalizzazione frazionaria (3/5)"): ["fse_geometria"],
    (14, "Slide 53–54 — I passi chiave"): ["traliccio_viterbi"],
    (14, "Slide 56 — Memoria del canale"): ["beta_triangolo"],
}

# didascalie brevi (una riga) che sostituiscono quelle lunghe dei disegni
BREVI = {
    "laplace": "pdf di Laplace (voce) e uniforme.",
    "quantizzatore": "Gradini più stretti vicino a 0.",
    "lloyd_centroide": "Livello al baricentro, soglia a metà tra i livelli.",
    "lloyd_ciclo": "Lloyd-Max alterna centroide e punto medio.",
    "companding_schema": "Compressione, quantizzatore uniforme, espansione.",
    "companding_equivalenza": "Passi uniformi su F(x) = passi non uniformi su x.",
    "leggi": "Leggi µ e A quasi coincidenti.",
    "snr_livello": "Con la legge µ l'SNR non dipende dal livello.",
    "spettri_bb_pb": "Banda base attorno a 0, passa-banda attorno a ±f_c.",
    "catena_spettri": "Tolgo le frequenze negative e traslo in 0.",
    "hilbert": "Hilbert: modulo 1, fase ∓90°.",
    "fasore": "L'inviluppo ruota con la portante.",
    "chi_e_chi": "s_c, s_s in banda base; x_c, x_s passa-banda.",
    "up_down": "Upconversion e downconversion.",
    "realizzazioni": "Fisso ω: un segnale. Fisso t: una variabile aleatoria.",
    "acf": "acf larga = processo lento.",
    "implicazioni": "Indipendenti ⇒ incorrelati; il viceversa solo se gaussiani.",
    "stazionarieta": "SSS ⇒ WSS, non viceversa.",
    "lti": "Media, acf e PSD all'uscita di un filtro LTI.",
    "psd_filtro": "La PSD è potenza per unità di banda.",
    "catena_psd": "PSD dell'inviluppo: un lobo, raddoppiato e traslato.",
    "simmetria": "Spettro simmetrico ⇒ componenti incoerenti.",
    "rumore": "Rumore in banda: N_0/2, inviluppo N_0, componenti N_0/2.",
    "canale": "Canale senza memoria e canale AWGN.",
    "entropie": "L'intersezione è l'informazione mutua.",
    "costellazioni_etap": "OOK, antipodale, ortogonale: distanze a parità di E_b.",
    "piano_shannon": "Frontiera di Shannon e modulazioni a BER 10⁻⁵.",
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
    t = re.sub(r"(?m)^(#{2,6}) (?:Slide \d+(?:[–-]\d+)?(?: e appunti)? — |Dispense p\. \d+(?:[–-]\d+)?(?: e appunti)? — |Appunti — )", r"\1 ", t)
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
        k = m.group(1)
        svg, didascalia = DISEGNI[k]
        breve = BREVI.get(k)
        didascalia = ("🧩 " + breve) if breve else didascalia
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
    for n, titolo in ESCLUDI:
        if n == cfg["n"]:
            blocco = re.sub(rf"(?ms)^### {re.escape(titolo)}.*?(?=^### |^## |\Z)", "", blocco)
    blocco = inserisci_figure(blocco, cfg["n"])
    return titoli_con_pagine(wikilink_testo(blocco, out)).strip()


def concetto_html(nome, out, usati, cartella="concetti"):
    if "/" in nome:
        cartella, nome = nome.split("/", 1)
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
    if not pezzi and not der:
        # pagina senza le sezioni standard (entità, laboratorio): tutto il testo tranne titolo e fonti
        corpo_tutto = re.sub(r"(?m)^# .*\n", "", md)
        corpo_tutto = re.sub(r"(?ms)^## Fonti.*?(?=^## |\Z)", "", corpo_tutto)
        corpo_tutto = re.sub(r"(?ms)^_Aggiornato.*", "", corpo_tutto)
        pezzi.append(demota(corpo_tutto, 2))
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
<p class="crumb"><a href="index.html">Home</a> · <a href="index.html#lezioni">Lezioni</a> · Lezione {cfg['n']} · {cfg["data"]}</p>
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


def _toc(c, out):
    return [re.sub(r'<span class="pag">.*?</span>', "", x).strip() for x in re.findall(r"(?m)^### (.+)$", corpo_lezione(c, CORSO, out))]


def pagina_indice(out):
    """Home: due strade, il percorso della prima prova intercorso oppure le lezioni una per una."""
    card = []
    for c in LEZIONI:
        card.append(f'<a class="card" href="{c["slug"]}.html"><span class="num">Lezione {c["n"]} · {c["data"]}</span>'
                    f'<strong>{html.escape(c["titolo"])}</strong><span class="b">{html.escape(c["breve"])}</span></a>')
    corpo = f"""
<h1>Trasmissione dei Segnali Digitali</h1>
<p class="breve">Appunti di studio del corso (LM Ingegneria Informatica, UNINA): il testo delle slide, le spiegazioni e le dimostrazioni passo-passo, i disegni e le domande da esame.</p>
<div class="cards strade">
<a class="card hero" href="intercorso.html"><span class="num">Percorso</span><strong>Prima prova intercorso</strong><span class="b">Dalla quantizzazione alla rappresentazione di Rice dei processi aleatori: solo gli argomenti della prova, nell'ordine delle lezioni.</span></a>
<a class="card hero" href="#lezioni"><span class="num">Percorso</span><strong>Tutte le lezioni</strong><span class="b">Le lezioni una per una, nell'ordine in cui sono state svolte.</span></a>
<a class="card hero" href="considerazioni.html"><span class="num">Note personali</span><strong>Le mie considerazioni</strong><span class="b">Ragionamenti miei nati durante lo studio, tenuti separati dal materiale delle lezioni.</span></a>
</div>
<h2 class="ps" id="lezioni">Le lezioni</h2>
<div class="cards">{"".join(card)}</div>
<h2 class="ps">Come si legge</h2>
<ul class="legenda">
<li>Ogni lezione ha tre parti: <strong>il corso slide per slide</strong> (con gli appunti presi a lezione), le <strong>spiegazioni e dimostrazioni</strong> passo-passo (a comparsa) e le <strong>domande da esame</strong>.</li>
<li>Le equazioni numerate sono quelle delle slide. I disegni sono costruiti dalle formule delle slide.</li>
<li><span class="chip formula">🧮</span> formula da sapere a memoria · <span class="chip esame">🎯</span> punto da esame · <span class="chip mia">🧩</span> passaggio o disegno ricostruito da me · <span class="chip conn">💡</span> collegamento · <span class="chip avv">⚠️</span> refuso o contraddizione nella slide · <span class="chip dub">❓</span> salto non ricostruito.</li>
<li>Tocca un'immagine per ingrandirla. I pulsanti <strong>A−</strong> e <strong>A+</strong> in alto cambiano la dimensione del testo.</li>
</ul>
"""
    return pagina("Trasmissione dei Segnali Digitali", corpo, "index")


def pagina_intercorso(out):
    card = []
    for n, inizio, nota in INTERCORSO:
        c = next(x for x in LEZIONI if x["n"] == n)
        toc = _toc(c, out)
        if inizio:
            k = next(i for i, x in enumerate(toc) if re.sub(r"<[^>]+>", "", x).startswith(inizio))
            toc = toc[k:]
            href = f'{c["slug"]}.html#{slug(inizio)}'
        else:
            href = f'{c["slug"]}.html'
        li = "".join(f"<li>{html.escape(re.sub(r'<[^>]+>', '', x))}</li>" for x in toc)
        card.append(f'<a class="card" href="{href}"><span class="num">Lezione {c["n"]} · {html.escape(nota)}</span>'
                    f'<strong>{html.escape(c["titolo"])}</strong><span class="b">{html.escape(c["breve"])}</span>'
                    f'<ul>{li}</ul></a>')
    corpo = f"""
<p class="crumb"><a href="index.html">Home</a> · Prima prova intercorso</p>
<h1>Prima prova intercorso</h1>
<p class="breve">Gli argomenti della <strong>prima prova intercorso</strong>: dal quantizzatore uniforme (SNR e legge dei 6 dB/bit) e dalla quantizzazione non uniforme alla rappresentazione di Rice dei processi aleatori. Ogni scheda apre la lezione dal punto giusto.</p>
<div class="cards">{"".join(card)}</div>
<ul class="legenda">
<li>Le Lezioni 1–2 (introduzione e probabilità) e la prima parte della 3 (campionamento e conversione A/D) precedono l'intercorso; della quantizzazione uniforme serve la parte sulla legge dei 6 dB/bit. Il laboratorio Matlab (Lezione 5) non è materia d'esame.</li>
</ul>
"""
    return pagina("Prima prova intercorso · Trasmissione dei Segnali Digitali", corpo, "intercorso")


def pagina_considerazioni(out):
    """Pagina staccata dalle lezioni: i ragionamenti personali salvati durante lo studio (wiki/mie-considerazioni.md)."""
    md = rimuovi_frontmatter((WIKI / "mie-considerazioni.md").read_text(encoding="utf-8"))
    titolo = re.search(r"(?m)^# (.+)$", md).group(1).strip()
    md = re.sub(r"(?m)^# .*\n", "", md)
    md = re.sub(r"(?ms)^_Aggiornato.*", "", md)
    md = re.sub(r"(?m)^Collegamenti:.*\n?", "", md)
    intro, _, resto = md.partition("\n## ")
    resto = "## " + resto if resto else ""
    usati, toc = set(), []
    h = post_html(render_md(wikilink_testo(demota(resto, 1), out)))
    h = con_id(h, usati, toc)
    voci = "".join(f'<li class="l{liv}"><a href="#{i}">{t}</a></li>' for liv, i, t in toc if liv == 3)
    corpo = f"""
<p class="crumb"><a href="index.html">Home</a> · Le mie considerazioni</p>
<h1>{html.escape(titolo)}</h1>
<div class="breve">{post_html(render_md(wikilink_testo(intro.strip(), out)))}</div>
<details class="toc" open><summary>Indice delle considerazioni</summary><ul>{voci}</ul></details>
<section id="considerazioni">
{h}
</section>
"""
    return pagina(f"{titolo} · Trasmissione dei Segnali Digitali", corpo, "considerazioni")


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
.card.hero{border:2px solid var(--a1);background:var(--soft)}
.card.hero strong{font-size:1.25em}
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
      var kx = el.querySelector('.katex');
      if (kx) kx.style.whiteSpace = '';
      // larghezza naturale: se la formula va a capo, somma i pezzi delle righe invece di prendere il riquadro che li contiene
      var rs = el.getClientRects(), wn = 0;
      for (var j = 0; j < rs.length; j++) wn += rs[j].width;
      if (c && c.clientWidth && wn > c.clientWidth - 8) el.classList.add('wide');
      else if (kx) kx.style.whiteSpace = 'nowrap';
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
    (out / "intercorso.html").write_text(pagina_intercorso(out), encoding="utf-8")
    (out / "considerazioni.html").write_text(pagina_considerazioni(out), encoding="utf-8")
    print("scritto index, immagini:", len(COPIATE))
    # pagine aggiuntive tenute fuori dal repository e non collegate dall'indice (facoltative)
    extra = ROOT.parent / "extra_sito.py"
    if extra.exists():
        import importlib.util
        spec = importlib.util.spec_from_file_location("extra_sito", extra)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        (out / f"{mod.SLUG}.html").write_text(mod.pagina_sito(sys.modules[__name__]), encoding="utf-8")
        with open(out / "app.js", "a", encoding="utf-8") as fh:
            fh.write(mod.accesso_js())
        print("scritta la pagina aggiuntiva")


if __name__ == "__main__":
    destinazione = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.gettempdir()) / "sito-tsd"
    costruisci(destinazione)
    print(destinazione)
