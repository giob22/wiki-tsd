"""Disegni SVG del sito di studio: piccoli (viewBox largo 400), con colori presi dal CSS del sito (tema chiaro/scuro).

Ogni funzione `fig_*` restituisce (svg, didascalia). `tutte()` li raccoglie per chiave.
Le didascalie iniziano con 🧩: i disegni sono miei, costruiti dalle formule delle slide.
"""
import html
import math

import numpy as np

_n = [0]


def _fmt(s):
    """Testo con pedici e apici: x_i, x_{i-1}, f^{2}."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in "_^" and i + 1 < len(s):
            if s[i + 1] == "{":
                j = s.index("}", i)
                tok, i = s[i + 2:j], j + 1
            else:
                tok, i = s[i + 1], i + 2
            dy = 3 if c == "_" else -4
            out.append(f'<tspan dy="{dy}" font-size="0.72em">{html.escape(tok)}</tspan><tspan dy="{-dy}">​</tspan>')
        else:
            out.append(html.escape(c))
            i += 1
    return "".join(out)


class Svg:
    def __init__(self, w, h, titolo):
        _n[0] += 1
        self.i, self.w, self.h, self.titolo, self.e = _n[0], w, h, titolo, []

    def line(self, x1, y1, x2, y2, c="ln", ar=False, ar0=False):
        m = f' marker-end="url(#a{self.i})"' if ar else ""
        m += f' marker-start="url(#a{self.i})"' if ar0 else ""
        self.e.append(f'<line class="{c}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{m}/>')

    def poly(self, pts, c="cv", close=False, ar=False):
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + (" Z" if close else "")
        m = f' marker-end="url(#a{self.i})"' if ar else ""
        self.e.append(f'<path class="{c}" d="{d}"{m}/>')

    def rect(self, x, y, w, h, c="bx", rx=4):
        self.e.append(f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"/>')

    def circ(self, x, y, r, c="bx"):
        self.e.append(f'<circle class="{c}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>')

    def t(self, x, y, s, c="tx", a="middle"):
        self.e.append(f'<text class="{c}" x="{x:.1f}" y="{y:.1f}" text-anchor="{a}">{_fmt(s)}</text>')

    def t2(self, x, y, righe, c="tx", a="middle", dy=14):
        for k, r in enumerate(righe):
            self.t(x, y + k * dy, r, c, a)

    def mult(self, x, y, r=9):
        self.circ(x, y, r)
        self.line(x - r * .55, y - r * .55, x + r * .55, y + r * .55, "ln")
        self.line(x - r * .55, y + r * .55, x + r * .55, y - r * .55, "ln")

    def somma(self, x, y, r=9, segno=("+", "+")):
        self.circ(x, y, r)
        self.t(x, y + 4, "Σ", "ts")

    def render(self):
        defs = (f'<defs><marker id="a{self.i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path class="mk" d="M0 0L10 5L0 10z"/></marker></defs>')
        return (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.titolo)}" '
                f'xmlns="http://www.w3.org/2000/svg">{defs}{"".join(self.e)}</svg>')


def lobo(s, cx, y0, hw, h, forma="tri", c="cv", fill="fl"):
    if forma == "tri":
        pts = [(cx - hw, y0), (cx, y0 - h), (cx + hw, y0)]
    elif forma == "ris":      # triangolo asimmetrico: picco a destra
        pts = [(cx - hw, y0), (cx + hw * .8, y0 - h), (cx + hw, y0)]
    else:
        pts = [(cx - hw, y0), (cx - hw, y0 - h), (cx + hw, y0 - h), (cx + hw, y0)]
    if fill:
        s.poly(pts, fill, True)
    s.poly(pts, c)


def asse_f(s, x0, x1, y, etichetta="f", alto=None, cx=None):
    s.line(x0, y, x1, y, "ax", ar=True)
    s.t(x1 + 2, y + 15, etichetta, "ts", "end")
    if alto and cx is not None:
        s.line(cx, y + 3, cx, y - alto, "ax", ar=True)


# --------------------------------------------------------------------------------------------- Lezione 3

def fig_laplace():
    s = Svg(400, 175, "pdf di Laplace e pdf uniforme")
    cx, y0, kx, ky = 200, 140, 42, 200
    xs = np.linspace(-4.2, 4.2, 169)
    pts = [(cx + kx * x, y0 - ky * .5 * math.exp(-abs(x))) for x in xs]
    s.poly([(cx - kx * 4.2, y0)] + pts + [(cx + kx * 4.2, y0)], "fl", True)
    s.line(cx - kx * 4.4, y0, cx + kx * 4.4, y0, "ax", ar=True)
    s.line(cx, y0 + 4, cx, y0 - 112, "ax", ar=True)
    s.poly(pts, "cv")
    u = ky / 6
    s.poly([(cx - 3 * kx, y0), (cx - 3 * kx, y0 - u), (cx + 3 * kx, y0 - u), (cx + 3 * kx, y0)], "cv2 dash")
    s.t(cx + 8, y0 - 112, "f_X(x)", "ts", "start")
    s.t(cx + kx * 4.4 + 4, y0 + 15, "x", "ts", "end")
    s.t(cx - 3 * kx, y0 + 15, "−X_{max}", "ts")
    s.t(cx + 3 * kx, y0 + 15, "X_{max}", "ts")
    s.t(cx + 38, y0 - 88, "Laplace (voce)", "tx a1", "start")
    s.t(cx + 3 * kx - 2, y0 - u - 6, "uniforme", "tx a2", "end")
    s.t(cx + 38, y0 - 70, "vicino a 0 la pdf è alta", "ts", "start")
    return s.render(), "🧩 La pdf di Laplace ($\\lambda=1$) concentra la probabilità vicino allo zero; la pdf uniforme (tratteggiata) è il caso in cui il quantizzatore uniforme è ottimo."


def fig_quantizzatore():
    s = Svg(400, 262, "caratteristica di un quantizzatore non uniforme")
    ox, oy, k = 200, 125, 45
    x = [-1.65, -.78, -.22, .22, .78, 1.65]
    q = [-2.2, -1.1, -.45, 0, .45, 1.1, 2.2]
    X = lambda v: ox + k * v
    Y = lambda v: oy - k * v
    s.line(X(-3.1), oy, X(3.15), oy, "ax", ar=True)
    s.line(ox, Y(-2.65), ox, Y(2.65), "ax", ar=True)
    s.line(X(-2.6), Y(-2.6), X(2.6), Y(2.6), "gd")
    pts = [(X(-3), Y(q[0]))]
    for i in range(6):
        pts += [(X(x[i]), Y(q[i])), (X(x[i]), Y(q[i + 1]))]
    pts.append((X(3), Y(q[6])))
    s.poly(pts, "cv")
    for i in range(6):
        y_end = oy
        s.line(X(x[i]), Y(q[i] if x[i] > 0 else q[i + 1]), X(x[i]), y_end, "gd")
        s.line(X(x[i]), oy - 3, X(x[i]), oy + 3, "ln")
    pos = [(-2.3, q[0]), (-1.2, q[1]), (-.5, q[2]), (0, q[3]), (.5, q[4]), (1.2, q[5]), (2.3, q[6])]
    for i, (px, qv) in enumerate(pos):
        s.t(X(px) + (0 if i != 3 else 16), (Y(qv) - 5 if qv > 0 else Y(qv) + 14) if i != 3 else oy + 16, f"q_{i + 1}", "ts a1")
    for i, xv in enumerate(x):
        s.t(X(xv) + (-3 if i == 2 else 3 if i == 3 else 0), oy + (15 if xv < 0 else -7), f"x_{i + 1}", "ts")
    s.t(X(3.15), oy + 14, "x", "ts", "end")
    s.t(ox + 6, Y(2.65) + 8, "Q(x)", "ts", "start")
    yb = 246
    for a, b, tx in ((-3.0, x[0], "R_s"), (x[0], x[5], "regione granulare R_g"), (x[5], 3.0, "R_s")):
        s.line(X(a) + 2, yb - 8, X(a) + 2, yb - 3, "ax")
        s.line(X(a) + 2, yb - 3, X(b) - 2, yb - 3, "ax")
        s.line(X(b) - 2, yb - 8, X(b) - 2, yb - 3, "ax")
        s.t((X(a) + X(b)) / 2, yb + 9, tx, "ts")
    return s.render(), "🧩 Quantizzatore con $M=7$ livelli: $Q(x)=q_i$ se $x\\in R_i=(x_{i-1},x_i)$. Gli scalini sono più stretti vicino a 0. Le due regioni esterne ($R_1$, $R_7$) sono di sovraccarico $R_s$; quelle interne formano la regione granulare $R_g$. I livelli sono scelti qui a metà tra i $q$ adiacenti."


def fig_lloyd_centroide():
    s = Svg(400, 178, "centroide e punto medio di una regione di decisione")
    x0, k, y0, ky = 30, 80, 144, 112
    f = lambda t: math.exp(-t)
    a, b = .6, 2.1
    xs = np.linspace(0, 4.3, 120)
    curve = [(x0 + k * t, y0 - ky * f(t)) for t in xs]
    reg = [(x0 + k * a, y0)] + [(x0 + k * t, y0 - ky * f(t)) for t in np.linspace(a, b, 40)] + [(x0 + k * b, y0)]
    s.poly(reg, "fl", True)
    s.line(x0 - 6, y0, x0 + k * 4.5, y0, "ax", ar=True)
    s.line(x0, y0 + 3, x0, y0 - 128, "ax", ar=True)
    s.poly(curve, "cv")
    tt = np.linspace(a, b, 2000)
    qc = float(np.sum(tt * np.exp(-tt)) / np.sum(np.exp(-tt)))
    m = (a + b) / 2
    s.line(x0 + k * a, y0, x0 + k * a, y0 - ky * f(a), "ln")
    s.line(x0 + k * b, y0, x0 + k * b, y0 - ky * f(b), "ln")
    s.line(x0 + k * m, y0, x0 + k * m, y0 - 80, "gd")
    s.line(x0 + k * qc, y0, x0 + k * qc, y0 - 80, "cv2")
    s.t(x0 + k * a, y0 + 15, "x_{i−1}", "ts")
    s.t(x0 + k * b, y0 + 15, "x_i", "ts")
    s.t(x0 + k * qc - 4, y0 - 86, "q_i", "tx a2", "end")
    s.t(x0 + k * qc - 4, y0 - 100, "centroide", "ts a2", "end")
    s.t(x0 + k * m + 4, y0 - 84, "punto medio", "ts", "start")
    s.t(x0 + 6, 14, "f_X(x)", "ts", "start")
    s.t(x0 + k * 4.5, y0 + 15, "x", "ts", "end")
    s.t(x0 + k * 3.0, 90, "area di R_i", "ts a1", "middle")
    return s.render(), "🧩 Su $R_i=(x_{i-1},x_i)$ il livello ottimo $q_i$ è il baricentro della pdf (centroide), spostato verso la parte dove la pdf è più alta; la soglia ottima è il punto medio tra due livelli."


def fig_lloyd_ciclo():
    s = Svg(400, 262, "ciclo dell'algoritmo di Lloyd-Max")
    s.rect(70, 8, 270, 34)
    s.t(205, 29, "Inizializza i livelli di decisione x_i", "tx")
    s.rect(70, 72, 270, 52, "bx bx1")
    s.t2(205, 93, ["① x_i fissati: q_i = E[x | x ∈ R_i]", "(centroide)"], "tx", dy=17)
    s.rect(70, 150, 270, 52, "bx bx2")
    s.t2(205, 171, ["② q_i fissati: x_i = (q_i + q_{i+1}) / 2", "(punto medio)"], "tx", dy=17)
    s.rect(70, 224, 270, 32)
    s.t(205, 245, "MSE assestato?", "tx")
    s.line(205, 42, 205, 72, "ln", ar=True)
    s.line(205, 124, 205, 150, "ln", ar=True)
    s.line(205, 202, 205, 224, "ln", ar=True)
    s.poly([(70, 240), (30, 240), (30, 98), (70, 98)], "ln", ar=True)
    s.t(22, 172, "no", "ts", "end")
    s.line(340, 240, 380, 240, "ln", ar=True)
    s.t(360, 232, "sì", "ts")
    s.t(366, 256, "fine", "ts")
    return s.render(), "🧩 Lloyd-Max applica a turno le due condizioni necessarie finché l'MSE non si assesta. Ogni passo non aumenta l'MSE, ma si può arrivare a un minimo locale."


def fig_companding_schema():
    s = Svg(400, 170, "schema del companding")
    s.t(24, 43, "x(n)", "tx", "middle")
    s.line(42, 38, 66, 38, "ln", ar=True)
    s.rect(66, 18, 104, 40, "bx bx1")
    s.t2(118, 35, ["Compressore", "F(x)"], dy=15)
    s.line(170, 38, 218, 38, "ln", ar=True)
    s.rect(218, 18, 104, 40)
    s.t2(270, 35, ["Codificatore", "uniforme n bit"], dy=15)
    s.poly([(270, 58), (270, 90), (118, 90), (118, 112)], "ln", ar=True)
    s.t(194, 84, "n bit (canale)", "ts")
    s.rect(66, 112, 104, 40)
    s.t2(118, 129, ["Decodificatore", "uniforme n bit"], dy=15)
    s.line(170, 132, 218, 132, "ln", ar=True)
    s.rect(218, 112, 104, 40, "bx bx2")
    s.t2(270, 129, ["Espansore", "F⁻¹(x)"], dy=15)
    s.line(322, 132, 350, 132, "ln", ar=True)
    s.t(372, 136, "x̂(n)", "tx")
    return s.render(), "🧩 Companding: legge di compressione $F$, quantizzazione uniforme a $n$ bit, e in decodifica la legge simmetrica $F^{-1}$ (espansione). Nella figura originale il secondo blocco è chiamato «decoder» per un refuso: è il codificatore."


def fig_companding_equivalenza():
    s = Svg(400, 232, "compressione e livelli non uniformi")
    ox, oy, W, H = 60, 192, 290, 150
    mu = 20.0
    F = lambda v: math.log(1 + mu * v) / math.log(1 + mu)
    Finv = lambda y: (math.exp(y * math.log(1 + mu)) - 1) / mu
    s.line(ox - 4, oy, ox + W + 14, oy, "ax", ar=True)
    s.line(ox, oy + 3, ox, oy - H - 14, "ax", ar=True)
    s.poly([(ox + W * v, oy - H * F(v)) for v in np.linspace(0, 1, 80)], "cv")
    n = 6
    for k in range(1, n):
        y = k / n
        xv = Finv(y)
        s.line(ox, oy - H * y, ox + W * xv, oy - H * y, "gd")
        s.line(ox + W * xv, oy - H * y, ox + W * xv, oy, "gd")
        s.line(ox + W * xv, oy - 3, ox + W * xv, oy + 3, "ln")
    s.line(ox, oy - H, ox + W, oy - H, "gd")
    s.line(ox + W, oy - H, ox + W, oy, "gd")
    s.t(ox + W, oy + 15, "X_{max}", "ts")
    s.t(ox - 6, oy - H + 4, "X_{max}", "ts", "end")
    s.t(ox + W + 14, oy - 6, "x", "ts", "end")
    s.t(ox + 6, oy - H - 6, "F(x)", "ts", "start")
    s.t(ox - 6, oy - H * (1.5 / n) + 4, "Δ", "tx a1", "end")
    xi0, xi1 = Finv(4 / n), Finv(5 / n)
    s.t(ox + W * (xi0 + xi1) / 2, oy + 28, "Δ_i grande", "ts a2")
    s.t(ox + W * Finv(1 / n) / 2 + 2, oy + 28, "Δ_i piccolo", "ts a2")
    s.t(ox + 8, oy - H * .5 + 4, "livelli uniformi", "ts", "start")
    return s.render(), "🧩 Livelli equispaziati ($\\Delta$) sull'asse di $F(x)$ corrispondono a livelli non uniformi sull'asse di $x$: fitti vicino a 0 ($\\Delta_i$ piccolo), radi per ampiezze grandi. Curva logaritmica con $\\mu=20$ per renderla visibile."


def fig_leggi():
    s = Svg(400, 232, "leggi di compressione mu e A")
    ox, oy, L = 46, 204, 180
    s.line(ox - 4, oy, ox + L + 12, oy, "ax", ar=True)
    s.line(ox, oy + 3, ox, oy - L - 12, "ax", ar=True)
    s.line(ox + L, oy - L, ox + L, oy, "gd")
    s.line(ox, oy - L, ox + L, oy - L, "gd")
    s.line(ox, oy, ox + L, oy - L, "cv3 dash")
    mu, A = 255.0, 87.6
    s.poly([(ox + L * v, oy - L * math.log(1 + mu * v) / math.log(1 + mu)) for v in np.linspace(0, 1, 120)], "cv")

    def a_law(v):
        return A * v / (1 + math.log(A)) if v <= 1 / A else (1 + math.log(A * v)) / (1 + math.log(A))
    s.poly([(ox + L * v, oy - L * a_law(v)) for v in np.linspace(0, 1, 200)], "cv2 dash2")
    s.t(ox + L, oy + 15, "1", "ts")
    s.t(ox - 6, oy - L + 4, "1", "ts", "end")
    s.t(ox - 6, oy + 4, "0", "ts", "end")
    s.t(ox + L + 12, oy + 15, "|x|/X_{max}", "ts", "end")
    s.t(ox + 6, oy - L - 8, "F(x)/X_{max}", "ts", "start")
    lx = 250
    s.line(lx, 60, lx + 26, 60, "cv")
    s.t(lx + 32, 64, "legge µ, µ = 255", "ts", "start")
    s.line(lx, 84, lx + 26, 84, "cv2 dash2")
    s.t(lx + 32, 88, "legge A, A = 87.6", "ts", "start")
    s.line(lx, 108, lx + 26, 108, "cv3 dash")
    s.t2(lx + 32, 112, ["µ = 0, A = 1:", "uniforme F(x) = x"], "ts", "start", dy=13)
    return s.render(), "🧩 Le due leggi (parte $x\\ge0$) comprimono molto vicino a 0 e poco in alto; le curve quasi coincidono. Con $\\mu=0$ o $A=1$ si torna alla diagonale, cioè al quantizzatore uniforme."


def fig_snr_livello():
    s = Svg(400, 250, "SNR in funzione del livello del segnale")
    ox, oy, W, H = 52, 214, 320, 180      # livello -60..-12 dB; SNR -10..50 dB
    lv = lambda L: ox + W * (L + 60) / 48
    sn = lambda v: oy - H * (v + 10) / 60
    s.line(ox - 4, oy, ox + W + 8, oy, "ax", ar=True)
    s.line(ox, oy + 3, ox, oy - H - 12, "ax", ar=True)
    b, M, mu = 8, 256, 255.0
    liv = np.linspace(-60, -12, 100)
    uni = [6.02 * b + 4.77 + L for L in liv]
    comp = []
    for L in liv:
        r = 10 ** (L / 20)
        den = (math.log(1 + mu) / mu) ** 2 * (1 + 2 * mu * r / math.sqrt(2) + (mu * r) ** 2)
        comp.append(10 * math.log10(3 * M * M * r * r / den))
    s.poly([(lv(L), sn(v)) for L, v in zip(liv, uni)], "cv2")
    s.poly([(lv(L), sn(v)) for L, v in zip(liv, comp)], "cv")
    for v in (0, 20, 40):
        s.line(ox, sn(v), ox + W, sn(v), "gd")
        s.t(ox - 6, sn(v) + 4, f"{v}", "ts", "end")
    for L in (-60, -48, -36, -24, -12):
        s.line(lv(L), oy - 3, lv(L), oy + 3, "ln")
        s.t(lv(L), oy + 15, f"{L}", "ts")
    s.t(ox + W + 8, oy + 28, "livello rms del segnale [dB rispetto a X_{max}]", "ts", "end")
    s.t(ox + 4, oy - H - 6, "SNR [dB]", "ts", "start")
    s.t(lv(-52), sn(30), "µ-law (µ = 255)", "tx a1", "start")
    s.t(lv(-52), sn(-3), "uniforme", "tx a2", "start")
    return s.render(), "🧩 SNR con $b=8$ bit e pdf di Laplace (ad alta risoluzione, sovraccarico trascurato): per il quantizzatore uniforme l'SNR cala di 1 dB per ogni dB di livello perso; con la legge $\\mu=255$ resta circa costante (≈38 dB, cioè $6.02\\,b-10.11$). Curve calcolate da me con la formula di $\\text{MSE}$."


# --------------------------------------------------------------------------------------------- Lezione 4

def fig_spettri_bb_pb():
    s = Svg(400, 250, "spettri in banda base e in banda passante")
    cx = 200
    y1, y2 = 84, 196
    s.t(10, 16, "banda base", "tx tb", "start")
    asse_f(s, 20, 388, y1, "f", 66, cx)
    lobo(s, cx, y1, 46, 52)
    s.t(cx + 8, y1 - 62, "|S(f)|", "ts", "start")
    s.t(cx, y1 + 15, "0", "ts")
    s.line(cx - 46, y1 + 27, cx + 46, y1 + 27, "ar2", ar=True, ar0=True)
    s.t(cx + 56, y1 + 31, "banda ≈ B", "ts a1", "start")
    s.t(10, 128, "banda passante", "tx tb", "start")
    asse_f(s, 20, 388, y2, "f", 66, cx)
    for sg in (-1, 1):
        lobo(s, cx + sg * 112, y2, 40, 52)
    s.t(cx + 8, y2 - 62, "|S_p(f)|", "ts", "start")
    s.t(cx - 112, y2 + 15, "−f_c", "ts")
    s.t(cx + 112, y2 + 15, "f_c", "ts")
    s.line(cx + 72, y2 + 27, cx + 152, y2 + 27, "ar2", ar=True, ar0=True)
    s.t(cx + 112, y2 + 42, "B", "ts a1")
    return s.render(), "🧩 Segnale in banda base: spettro concentrato attorno a $f=0$. Segnale passa-banda reale: due lobi in $\\pm f_c$, uno immagine hermitiana dell'altro ($S_p(-f)=S_p^\\ast(f)$), con $B\\ll f_c$."


def _catena(titolo, fattore, etichette, altezza_b):
    s = Svg(400, 304, titolo)
    cx, fc, hw = 200, 100, 30
    ys = (96, 194, 292)
    h0 = 34
    for y in ys:
        asse_f(s, 20, 392, y, "f", 74, cx)
    for sg in (-1, 1):
        lobo(s, cx + sg * fc, ys[0], hw, h0)
    lobo(s, cx + fc, ys[1], hw, altezza_b)
    lobo(s, cx, ys[2], hw, altezza_b)
    for y, e in zip(ys, etichette):
        s.t(10, y - 80, e, "tx a1", "start")
    s.t(cx - fc, ys[0] + 15, "−f_c", "ts")
    s.t(cx + fc, ys[0] + 15, "f_c", "ts")
    s.t(cx + fc, ys[1] + 15, "f_c", "ts")
    s.t(cx, ys[2] + 15, "0", "ts")
    s.line(340, ys[0] + 18, 340, ys[1] - 58, "ln", ar=True)
    s.t(346, (ys[0] + ys[1]) / 2 - 10, fattore, "ts a2", "start")
    s.line(340, ys[1] + 18, 340, ys[2] - 58, "ln", ar=True)
    s.t(346, (ys[1] + ys[2]) / 2 - 10, "trasla di", "ts a2", "start")
    s.t(346, (ys[1] + ys[2]) / 2 + 2, "−f_c", "ts a2", "start")
    return s


def fig_catena_spettri():
    s = _catena("dallo spettro passa-banda all'inviluppo", "× √2 · u(f)", ["S_p(f)", "S_p⁺(f) = √2 S_p(f) u(f)", "S(f) = S_p⁺(f + f_c)"], 48)
    return s.render(), "🧩 Dal segnale reale all'inviluppo complesso: si tengono solo le frequenze positive (filtro $\\sqrt2\\,u(f)$, il $\\sqrt2$ conserva l'energia) e si trasla il lobo nell'origine. L'inviluppo in generale ha spettro asimmetrico, quindi è complesso."


def fig_hilbert():
    s = Svg(400, 138, "risposta in frequenza del filtro di Hilbert")
    for cx, tit in ((100, "|H(f)| = 1"), (300, "fase di H(f)")):
        s.line(cx - 84, 72, cx + 84, 72, "ax", ar=True)
        s.line(cx, 118, cx, 24, "ax", ar=True)
        s.t(cx, 14, tit, "tx tb")
        s.t(cx + 88, 88, "f", "ts", "end")
    s.line(16, 44, 100, 44, "cv")
    s.line(100, 44, 184, 44, "cv")
    s.circ(100, 44, 3, "bx")
    s.t(180, 38, "1", "ts", "end")
    s.line(216, 44, 300, 44, "cv2")
    s.line(300, 100, 384, 100, "cv2")
    s.line(300, 44, 300, 100, "gd")
    s.t(310, 40, "+90° (f < 0)", "ts a2", "start")
    s.t(236, 114, "−90° (f > 0)", "ts a2", "start")
    return s.render(), "🧩 Il filtro di Hilbert $H(f)=-j\\,\\text{sgn}(f)$ ha modulo 1 e sfasa di $-90°$ le frequenze positive e di $+90°$ le negative: non cambia le ampiezze, solo le fasi."


def fig_fasore():
    s = Svg(400, 238, "inviluppo complesso e rotazione della portante")
    ox, oy = 70, 190
    s.line(ox - 10, oy, 380, oy, "ax", ar=True)
    s.line(ox, oy + 10, ox, 12, "ax", ar=True)
    s.t(380, oy + 15, "I = Re", "ts", "end")
    s.t(ox + 6, 14, "Q = Im", "ts", "start")
    sc, ss = 120, 70
    s.line(ox, oy, ox + sc, oy - ss, "cv", ar=True)
    s.line(ox + sc, oy - ss, ox + sc, oy, "gd")
    s.line(ox, oy - ss, ox + sc, oy - ss, "gd")
    s.t(ox + sc / 2, oy + 15, "s_c", "ts a1")
    s.t(ox - 8, oy - ss / 2, "s_s", "ts a1", "end")
    s.t(ox + sc + 10, oy - ss + 4, "s = s_c + j s_s", "tx a1", "start")
    al = math.radians(38)
    rx = sc * math.cos(al) - ss * math.sin(al)
    ry = sc * math.sin(al) + ss * math.cos(al)
    s.line(ox, oy, ox + rx, oy - ry, "cv2 dash", ar=True)
    s.line(ox + rx, oy - ry, ox + rx, oy, "gd")
    s.t(ox + rx + 8, oy - ry - 4, "s e^{jα}", "tx a2", "start")
    r = 46
    th = math.atan2(ss, sc)
    s.poly([(ox + r * math.cos(th), oy - r * math.sin(th)), (ox + r * math.cos(th + al), oy - r * math.sin(th + al))], "ax")
    s.t(ox + 66 * math.cos(th + al / 2) - 6, oy - 66 * math.sin(th + al / 2) + 4, "α", "tx a2")
    s.t(380, 34, "α = 2π f_c t", "ts a2", "end")
    s.t(ox + rx - 6, oy + 31, "proiezione: Re{s e^{jα}} = s_p/√2", "ts a2", "start")
    return s.render(), "🧩 Nel piano complesso $s=s_c+js_s$ ruota con la portante: $s\\,e^{j2\\pi f_ct}$. La proiezione sull'asse reale, moltiplicata per $\\sqrt2$, è il segnale passa-banda $s_p(t)=\\sqrt2\\,s_c\\cos\\alpha-\\sqrt2\\,s_s\\sin\\alpha$."


def fig_chi_e_chi():
    s = Svg(400, 300, "chi è chi nell'upconverter: s_c, s_s, x_c, x_s, s_p")
    s.t(48, 14, "banda base", "ts tb")
    s.t(265, 14, "banda passante", "ts tb")
    yi, yq, ys = 80, 212, 146   # ramo I, ramo Q, sommatore
    for y, nome, col, car, c, fl, sp in ((yi, "I", "a1", "√2 cos(2πf_ct)", "cv", "fl", "c"),
                                         (yq, "Q", "a2", "−√2 sin(2πf_ct)", "cv2", "fl2", "s")):
        up = y == yi
        s.t(46, y - 9, f"s_{sp}(t)", f"tx tb {col}")
        s.line(8, y, 102, y, "ln", ar=True)
        s.mult(112, y)
        ycar = y - 30
        s.t(112, ycar, car, "ts")
        s.line(112, ycar + 4, 112, y - 10, "ln", ar=True)
        s.t(190, y - 9, f"x_{sp}(t)" if up else f"−x_s(t)", f"tx tb {col}")
        # spettri sotto i fili: base y+40
        yb = y + 42
        s.line(14, yb, 82, yb, "ax", ar=True)
        lobo(s, 48, yb, 20, 24, "tri", c, fl)
        s.t(48, yb + 15, f"S_{sp}(f)", f"ts {col}")
        s.line(130, yb, 252, yb, "ax", ar=True)
        for cx in (145, 235):
            lobo(s, cx, yb, 18, 24, "tri", c, fl)
        s.t(145, yb + 15, "−f_c", "ts")
        s.t(235, yb + 15, "f_c", "ts")
        s.t(190, yb + 15, f"X_{sp}(f)", f"ts {col}")
    s.poly([(121, yi), (262, yi), (262, ys - 9)], "cv", ar=True)
    s.poly([(121, yq), (262, yq), (262, ys + 9)], "cv2", ar=True)
    s.circ(262, ys, 9)
    s.t(262, ys + 4, "+", "ts")
    s.line(271, ys, 392, ys, "ln", ar=True)
    s.t(332, ys - 9, "s_p = x_c − x_s", "tx tb a3")
    yb = ys + 50
    s.line(278, yb, 392, yb, "ax", ar=True)
    for cx in (303, 367):
        lobo(s, cx, yb, 18, 24, "tri", "cv3", None)
    s.t(335, yb + 15, "S_p(f)", "ts a3")
    s.t(8, 288, "I = in fase (coseno)  ·  Q = in quadratura (seno)", "ts", "start")
    return s.render(), ("🧩 **Chi è chi.** $s_c$, $s_s$ (minuscole, a sinistra) sono le componenti reali dell'inviluppo, in banda base: ciò che esce dal modulatore. "
                        "$x_c=\\sqrt2\\,s_c\\cos(2\\pi f_ct)$ e $x_s=\\sqrt2\\,s_s\\sin(2\\pi f_ct)$ sono le stesse informazioni dopo il moltiplicatore: due forme d'onda passa-banda ortogonali (18), con lo spettro replicato in $\\pm f_c$ e scalato per $1/\\sqrt2$. "
                        "Il sommatore le ricompone in $s_p=x_c-x_s$ (17). Il pedice $c$ indica il ramo del coseno (I), il pedice $s$ il ramo del seno (Q); $S_c$, $X_c$ sono le trasformate di $s_c$, $x_c$.")


def fig_up_down():
    s = Svg(400, 332, "upconversion e downconversion")
    s.t(10, 16, "Upconversion (trasmissione)", "tx tb", "start")
    s.t(18, 69, "s_c", "tx a1")
    s.line(32, 64, 84, 64, "ln", ar=True)
    s.mult(94, 64)
    s.t(94, 42, "√2 cos(2πf_ct)", "ts")
    s.line(94, 46, 94, 54, "ln", ar=True)
    s.t(18, 121, "s_s", "tx a1")
    s.line(32, 116, 84, 116, "ln", ar=True)
    s.mult(94, 116)
    s.t(94, 148, "−√2 sin(2πf_ct)", "ts")
    s.line(94, 136, 94, 126, "ln", ar=True)
    s.poly([(104, 64), (200, 64), (200, 81)], "ln", ar=True)
    s.poly([(104, 116), (200, 116), (200, 99)], "ln", ar=True)
    s.circ(200, 90, 9)
    s.t(200, 94, "+", "ts")
    s.line(209, 90, 268, 90, "ln", ar=True)
    s.t(300, 94, "s_p(t)", "tx a2")
    s.t(10, 184, "Downconversion (ricezione)", "tx tb", "start")
    s.t(18, 266, "s_p(t)", "tx a2", "start")
    s.line(56, 262, 68, 262, "ln")
    s.line(68, 232, 68, 292, "ln")
    s.line(68, 232, 148, 232, "ln", ar=True)
    s.line(68, 292, 148, 292, "ln", ar=True)
    s.mult(158, 232)
    s.mult(158, 292)
    s.t(158, 210, "√2 cos(2πf_ct)", "ts")
    s.line(158, 214, 158, 222, "ln", ar=True)
    s.t(158, 322, "−√2 sin(2πf_ct)", "ts")
    s.line(158, 312, 158, 302, "ln", ar=True)
    s.line(168, 232, 214, 232, "ln", ar=True)
    s.line(168, 292, 214, 292, "ln", ar=True)
    s.rect(214, 217, 62, 30, "bx bx1")
    s.t(245, 236, "passa-basso", "ts")
    s.rect(214, 277, 62, 30, "bx bx1")
    s.t(245, 296, "passa-basso", "ts")
    s.line(276, 232, 326, 232, "ln", ar=True)
    s.line(276, 292, 326, 292, "ln", ar=True)
    s.t(350, 236, "s_c(t)", "tx a1")
    s.t(350, 296, "s_s(t)", "tx a1")
    return s.render(), "🧩 Upconversion: $s_c$ per $\\sqrt2\\cos$, $s_s$ per $-\\sqrt2\\sin$, somma (eq. 17). Downconversion: si moltiplica per gli stessi segnali e il passa-basso elimina i termini a $2f_c$ (eq. 21). Il taglio del filtro deve stare tra $W$ e $2f_c-W$."


# --------------------------------------------------------------------------------------------- Lezione 5

def fig_realizzazioni():
    s = Svg(400, 238, "realizzazioni di un processo aleatorio")
    ox, oy, W, A = 40, 118, 330, 46
    s.line(ox - 4, oy, ox + W + 8, oy, "ax", ar=True)
    s.line(ox, oy + 62, ox, oy - 70, "ax", ar=True)
    th = [.4, 1.75, 3.0, 4.3]
    cl = ["cv", "cv2", "cv3", "cv4"]
    t1 = .42
    for k, (p, c) in enumerate(zip(th, cl)):
        pts = [(ox + W * t / 2, oy - A * math.cos(2 * math.pi * t + p)) for t in np.linspace(0, 2, 160)]
        s.poly(pts, c + (" ev" if k == 0 else ""))
    xv = ox + W * t1 / 2
    s.line(xv, oy + 64, xv, oy - 68, "gd")
    for p, c in zip(th, cl):
        s.circ(xv, oy - A * math.cos(2 * math.pi * t1 + p), 3.5, "pt " + c)
    s.t(xv, oy + 78, "t_1", "ts")
    s.t(ox + W + 8, oy + 15, "t", "ts", "end")
    s.t(ox + 6, oy - 72, "X(t; ω)", "ts", "start")
    for k, c in enumerate(cl):
        s.t(ox + W - 4 - 34 * (3 - k), 14, f"ω_{k + 1}", "ts " + {"cv": "a1", "cv2": "a2", "cv3": "a3", "cv4": "a4"}[c], "end")
    s.t(ox, 208, "t = t_1 fisso: i 4 punti sono valori di una variabile aleatoria", "ts", "start")
    s.t(ox, 226, "ω fisso (es. ω_1, curva spessa): una funzione del tempo", "ts", "start")
    return s.render(), "🧩 Processo $X(t;\\omega)=\\cos(2\\pi t+\\Theta)$ con fase casuale: ogni $\\omega_k$ è una forma d'onda (una **realizzazione**); fissando $t_1$ i valori sulla verticale sono i campioni di una variabile aleatoria."


def _liscia(n, sigma, seed):
    r = np.random.RandomState(seed).randn(n + 8 * sigma)
    k = np.exp(-0.5 * (np.arange(-4 * sigma, 4 * sigma + 1) / sigma) ** 2)
    y = np.convolve(r, k, mode="valid")[:n]
    return y / (np.std(y) + 1e-9)


def fig_acf():
    s = Svg(400, 236, "acf di un processo lento e di uno veloce")
    for riga, (sg, tit, seed) in enumerate(((12, "processo lento", 3), (2, "processo veloce", 5))):
        yc = 66 + riga * 104
        s.t(8, yc - 46, tit, "tx tb", "start")
        y = _liscia(200, sg, seed)
        s.line(10, yc, 200, yc, "ax", ar=True)
        s.poly([(10 + 190 * i / 199, yc - 20 * v) for i, v in enumerate(y)], "cv")
        s.t(198, yc + 14, "t", "ts", "end")
        ox = 300
        s.line(ox - 60, yc + 22, ox + 82, yc + 22, "ax", ar=True)
        s.line(ox, yc + 26, ox, yc - 40, "ax", ar=True)
        tc = 2 * sg * 1.0
        pts = [(ox + 1.45 * u, yc + 22 - 56 * math.exp(-(u / (2 * sg)) ** 2 / 1.0 / 1)) for u in np.linspace(-40, 40, 160)]
        s.poly(pts, "cv2")
        s.t(ox + 82, yc + 36, "τ", "ts", "end")
        s.t(ox + 6, yc - 40, "R_X(τ)", "ts", "start")
    return s.render(), "🧩 Più la acf è larga, più il processo varia lentamente: campioni vicini sono correlati a lungo. Una acf stretta indica un processo che cambia rapidamente (tempo di decorrelazione breve)."


def fig_implicazioni():
    s = Svg(400, 196, "indipendenti, incorrelati, incoerenti")
    s.rect(10, 20, 124, 40, "bx bx1")
    s.t2(72, 37, ["Indipendenti", "(tutti i campioni)"], dy=14)
    s.rect(200, 20, 150, 40)
    s.t2(275, 37, ["Incorrelati", "C_{XY}(τ) = 0 ∀τ"], dy=14)
    s.line(134, 40, 200, 40, "ln", ar=True)
    s.t(167, 32, "⇒", "tx")
    s.rect(200, 120, 150, 40)
    s.t2(275, 137, ["Incoerenti", "R_{XY}(τ) = 0 ∀τ"], dy=14)
    s.line(275, 62, 275, 118, "ln", ar=True, ar0=True)
    s.t(281, 94, "se μ_X = μ_Y = 0", "ts a2", "start")
    s.poly([(200, 52), (170, 52), (170, 118), (134, 118), (72, 118), (72, 62)], "gd", ar=True)
    s.t2(110, 172, ["solo per processi", "gaussiani (congiunti)"], "ts a2", "middle", dy=12)
    return s.render(), "🧩 Indipendenti ⇒ incorrelati (sempre). Con medie nulle incorrelazione e incoerenza coincidono. Il verso opposto, incorrelati ⇒ indipendenti, vale per i processi gaussiani."


def fig_stazionarieta():
    s = Svg(400, 152, "tipi di stazionarietà")
    s.rect(10, 52, 104, 46, "bx bx1")
    s.t2(62, 70, ["SSS", "(ogni ordine k)"], dy=14)
    s.rect(160, 12, 104, 40)
    s.t2(212, 28, ["ordine k", "poi k−1, …, 1"], dy=14)
    s.line(114, 66, 160, 38, "ln", ar=True)
    s.rect(160, 98, 230, 44, "bx bx2")
    s.t2(275, 116, ["WSS (senso lato)", "media costante + acf(τ)"], dy=14)
    s.line(114, 84, 160, 112, "ln", ar=True)
    s.t(300, 36, "il viceversa non vale", "ts a2", "start")
    return s.render(), "🧩 La stazionarietà stretta (SSS) implica quella di ogni ordine e quella in senso lato (WSS: media costante e acf che dipende solo dal ritardo). Non vale il viceversa."


def fig_lti():
    s = Svg(400, 206, "processo attraverso un filtro LTI")
    s.t(22, 40, "X(t)", "tx a1")
    s.line(40, 36, 120, 36, "ln", ar=True)
    s.rect(120, 14, 160, 44, "bx bx1")
    s.t2(200, 32, ["filtro LTI", "h(t) ⟷ H(f)"], dy=14)
    s.line(280, 36, 360, 36, "ln", ar=True)
    s.t(380, 40, "Y(t)", "tx a2")
    rows = [("media", "μ_Y = μ_X · H(0)"), ("autocorrelazione", "R_{YY}(τ) = R_{XX}(τ) ∗ h(τ) ∗ h(−τ)"), ("PSD", "S_{YY}(f) = S_{XX}(f) · |H(f)|²"), ("WSS", "ingresso WSS ⇒ uscita WSS")]
    for i, (a, b) in enumerate(rows):
        y = 100 + i * 32
        s.t(14, y, a, "ts", "start")
        s.t(130, y, b, "tx", "start")
    return s.render(), "🧩 Un filtro LTI deterministico non cambia la natura del processo: riscala la media per $H(0)$, la PSD per $\\lvert H(f)\\rvert^2$ e «sfuma» la acf con $r_{hh}=h(\\tau)\\ast h(-\\tau)$."


def fig_psd_filtro():
    s = Svg(400, 196, "significato fisico della PSD")
    cx, y0, f0, hw = 200, 150, 70, 14
    g = lambda f: 100 * math.exp(-(f / 95) ** 2)
    fs = np.linspace(-175, 175, 140)
    s.poly([(cx + f, y0 - g(f)) for f in fs], "cv")
    for sg in (-1, 1):
        a, b = sg * f0 - hw, sg * f0 + hw
        pts = [(cx + a, y0)] + [(cx + f, y0 - g(f)) for f in np.linspace(a, b, 12)] + [(cx + b, y0)]
        s.poly(pts, "fl2", True)
        s.rect(cx + a, y0 - 118, 2 * hw, 118, "ban", 0)
    asse_f(s, 16, 392, y0, "f", 112, cx)
    s.t(cx + 8, y0 - 116, "S_{XX}(f)", "ts", "start")
    s.t(cx + f0, y0 + 15, "f_0", "ts")
    s.t(cx - f0, y0 + 15, "−f_0", "ts")
    s.line(cx + f0 - hw, y0 + 24, cx + f0 + hw, y0 + 24, "ar2", ar=True, ar0=True)
    s.t(cx + f0, y0 + 38, "Δf", "ts a2")
    s.t(392, 28, "filtro ideale |H| = 1 nelle", "ts", "end")
    s.t(392, 42, "due bande strette", "ts", "end")
    s.t(392, 60, "ΔP ≈ 2 Δf · S_{XX}(f_0)", "tx a2", "end")
    return s.render(), "🧩 Se un filtro ideale a banda stretta lascia passare solo due finestre larghe $\\Delta f$ attorno a $\\pm f_0$, la potenza in uscita è l'area della PSD in quelle finestre: $S_{XX}(f_0)$ è la potenza per unità di frequenza."


# --------------------------------------------------------------------------------------------- Lezione 7

def fig_catena_psd():
    s = _catena("dalla PSD passa-banda alla PSD dell'inviluppo", "× 2 · u(f)",
                ["(a) PSD del processo passa-banda: S(f)", "(b) processo analitico: 2 S(f) u(f)", "(c) inviluppo: S_{xx}(f) = 2 S(f+f_c) u(f+f_c)"], 68)
    return s.render(), "🧩 Costruzione della (14): si prende la PSD del processo reale, si eliminano le frequenze negative (filtro $\\sqrt2\\,u(f)$, quindi $\\lvert H\\rvert^2=2\\,u(f)$) e si trasla di $-f_c$. Per un processo il quadrato del filtro raddoppia l'altezza."


def fig_simmetria():
    s = Svg(400, 172, "PSD dell'inviluppo simmetrica e non simmetrica")
    for cx, tit, forma in ((100, "PSD simmetrica attorno a f_c", "tri"), (300, "PSD non simmetrica", "ris")):
        s.t(cx, 16, tit, "tx tb")
        asse_f(s, cx - 90, cx + 90, 120, "f", 80, cx)
        lobo(s, cx, 120, 50, 62, forma)
        s.t(cx, 135, "0", "ts")
    s.t2(100, 154, ["S_{xx} pari  ⇒  R_{xx} reale", "⇒ x_c, x_s incoerenti"], "ts a1", dy=12)
    s.t2(300, 154, ["S_{xx} non pari ⇒ R_{xx} complessa", "⇒ x_c, x_s correlate (τ ≠ 0)"], "ts a2", dy=12)
    return s.render(), "🧩 Lo spettro dell'inviluppo è pari solo se quello passa-banda è simmetrico attorno alla portante. In quel caso $R_{x_cx_s}\\equiv0$ e $S_{xx}=2S_{x_cx_c}$."


def fig_rumore():
    s = Svg(400, 296, "rumore in banda passante")
    cx, fc, hw = 200, 100, 36
    ys = (92, 190, 280)
    for y in ys:
        asse_f(s, 20, 392, y, "f", 60, cx)
    for sg in (-1, 1):
        lobo(s, cx + sg * fc, ys[0], hw, 34, "rect")
    lobo(s, cx, ys[1], hw, 52, "rect")
    lobo(s, cx, ys[2], hw, 34, "rect")
    s.t(10, ys[0] - 68, "(a) rumore passa-banda w_p", "tx a1", "start")
    s.t(10, ys[1] - 68, "(b) inviluppo w = w_c + j w_s", "tx a1", "start")
    s.t(10, ys[2] - 56, "(c) componenti w_c e w_s (stessa PSD)", "tx a1", "start")
    s.t(cx + fc + hw + 4, ys[0] - 22, "N_0/2", "ts a2", "start")
    s.t(cx + hw + 4, ys[1] - 34, "N_0", "ts a2", "start")
    s.t(cx + hw + 4, ys[2] - 20, "N_0/2", "ts a2", "start")
    s.t(cx - fc, ys[0] + 15, "−f_c", "ts")
    s.t(cx + fc, ys[0] + 15, "f_c", "ts")
    s.line(cx - hw, ys[1] + 18, cx + hw, ys[1] + 18, "ar2", ar=True, ar0=True)
    s.t(cx, ys[1] + 32, "W", "ts a2")
    s.t(cx, ys[2] + 15, "0", "ts")
    return s.render(), "🧩 Rumore con PSD $N_0/2$ in una banda $W$ attorno a $\\pm f_c$: l'inviluppo ha PSD $N_0$ (si tiene un solo lobo e si raddoppia) e ciascuna componente $N_0/2$. La potenza si conserva: $2W\\cdot N_0/2=N_0W$."


# --------------------------------------------------------------------------------------------- Lezione 8

def fig_canale():
    s = Svg(400, 176, "canale senza memoria e canale AWGN")
    s.t(10, 16, "canale senza memoria", "tx tb", "start")
    s.t(30, 60, "X", "tx a1")
    s.line(42, 56, 140, 56, "ln", ar=True)
    s.rect(140, 34, 120, 44, "bx bx1")
    s.t2(200, 52, ["canale", "p(y | x)"], dy=15)
    s.line(260, 56, 358, 56, "ln", ar=True)
    s.t(372, 60, "Y", "tx a2")
    s.t(10, 112, "canale AWGN", "tx tb", "start")
    s.t(34, 150, "x[i]", "tx a1")
    s.line(56, 146, 191, 146, "ln", ar=True)
    s.circ(200, 146, 9)
    s.t(200, 150, "+", "ts")
    s.t(200, 116, "n[i] gaussiano bianco", "ts")
    s.line(200, 121, 200, 137, "ln", ar=True)
    s.line(209, 146, 344, 146, "ln", ar=True)
    s.t(370, 150, "y[i]", "tx a2")
    return s.render(), "🧩 Il canale è descritto dalla probabilità dell'uscita dato l'ingresso, $p(y\\mid x)$. Nel canale AWGN l'uscita è l'ingresso più un rumore gaussiano bianco indipendente: $y[i]=x[i]+n[i]$."


def fig_entropie():
    s = Svg(400, 226, "entropie e informazione mutua")
    for cx, c, f in ((165, "cv", "fl"), (235, "cv2", "fl2")):
        s.circ(cx, 100, 78, f)
        s.circ(cx, 100, 78, c)
    s.t(110, 16, "H(X)", "tx tb a1")
    s.t(290, 16, "H(Y)", "tx tb a2")
    s.t(122, 104, "H(X|Y)", "tx")
    s.t(200, 104, "I(X;Y)", "tx tb")
    s.t(278, 104, "H(Y|X)", "tx")
    s.t(14, 200, "incertezza residua", "ts a1", "start")
    s.t(14, 214, "su X, visto Y", "ts a1", "start")
    s.t(200, 200, "informazione", "ts")
    s.t(200, 214, "trasportata", "ts")
    s.t(386, 200, "incertezza su Y", "ts a2", "end")
    s.t(386, 214, "dovuta al rumore", "ts a2", "end")
    return s.render(), "🧩 Ogni cerchio è l'incertezza di una variabile. L'intersezione è l'informazione mutua: $I(X;Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)$. Con variabili indipendenti i cerchi non si toccano ($I=0$); con un canale perfetto coincidono."


def fig_capacita():
    s = Svg(400, 220, "capacità AWGN in funzione di SNR e di banda")
    # (a) C/W in funzione di gamma in dB
    ox, oy, W, H = 34, 176, 150, 140
    s.line(ox - 4, oy, ox + W + 10, oy, "ax", ar=True)
    s.line(ox, oy + 3, ox, oy - H - 10, "ax", ar=True)
    gx = lambda g: ox + W * (g + 10) / 40
    cy = lambda c: oy - H * c / 10
    pts = [(gx(g), cy(math.log2(1 + 10 ** (g / 10)))) for g in np.linspace(-10, 30, 120)]
    s.poly(pts, "cv")
    for g in (-10, 0, 10, 20, 30):
        s.line(gx(g), oy - 3, gx(g), oy + 3, "ln")
        s.t(gx(g), oy + 15, str(g), "ts")
    for c in (5, 10):
        s.line(ox - 3, cy(c), ox + 3, cy(c), "ln")
        s.t(ox - 6, cy(c) + 4, str(c), "ts", "end")
    s.t(ox + W + 10, oy + 30, "γ [dB]", "ts", "end")
    s.t(ox + 6, oy - H - 8, "C/W [bit/s/Hz]", "ts", "start")
    s.t(ox + W / 2, 14, "(a) log in γ", "tx tb a1")
    # (b) C in funzione di W a P/N0 fisso
    ox2 = 232
    s.line(ox2 - 4, oy, ox2 + W + 10, oy, "ax", ar=True)
    s.line(ox2, oy + 3, ox2, oy - H - 10, "ax", ar=True)
    wx = lambda w: ox2 + W * w / 6
    ky = lambda c: oy - H * c / 1.6
    pts = [(wx(w), ky(w * math.log2(1 + 1 / w))) for w in np.linspace(0.01, 6, 150)]
    s.poly(pts, "cv2")
    s.line(ox2, ky(1 / math.log(2)), ox2 + W, ky(1 / math.log(2)), "gd")
    s.t(ox2 + W, ky(1 / math.log(2)) - 6, "1.44 P/N_0", "ts a2", "end")
    s.t(ox2 + W + 10, oy + 30, "W  [unità P/N_0]", "ts", "end")
    s.t(ox2 + 6, oy - H - 8, "C", "ts", "start")
    s.t(ox2 + W / 2, 14, "(b) satura in W", "tx tb a2")
    return s.render(), "🧩 (a) A banda fissa la capacità cresce solo come il logaritmo dell'SNR: a SNR alto +3 dB danno +1 bit/s/Hz. (b) A potenza fissa, allargare la banda fa crescere la capacità quasi linearmente all'inizio, ma il rumore raccolto cresce con $W$ e la capacità satura a $\\frac{P}{N_0}\\log_2e\\approx1.44\\,P/N_0$."


def fig_costellazioni_etap():
    s = Svg(400, 190, "OOK, antipodale e ortogonale binaria")
    k = 30
    # OOK
    y = 96
    s.t(64, 18, "OOK", "tx tb")
    s.line(16, y, 120, y, "ax", ar=True)
    for x, lab in ((36, "0"), (36 + 2 * k, "A")):
        s.circ(x, y, 5, "pt cv")
        s.t(x, y + 18, lab, "ts")
    s.line(36, y - 16, 36 + 2 * k, y - 16, "ar2", ar=True, ar0=True)
    s.t(36 + k, y - 22, "d = A", "ts a1")
    s.t(64, 160, "η_P = 1/2", "tx a2")
    # antipodale
    cx = 200
    s.t(cx, 18, "antipodale", "tx tb")
    s.line(cx - 60, y, cx + 60, y, "ax", ar=True)
    s.line(cx, y - 6, cx, y + 6, "ln")
    for x, lab in ((cx - 2 * k, "−A"), (cx + 2 * k, "A")):
        s.circ(x, y, 5, "pt cv")
        s.t(x, y + 18, lab, "ts")
    s.line(cx - 2 * k, y - 16, cx + 2 * k, y - 16, "ar2", ar=True, ar0=True)
    s.t(cx, y - 22, "d = 2A", "ts a1")
    s.t(cx, 160, "η_P = 1", "tx a2")
    # ortogonale
    ox, oy = 300, 130
    s.t(336, 18, "ortogonale", "tx tb")
    s.line(ox - 6, oy, ox + 84, oy, "ax", ar=True)
    s.line(ox, oy + 6, ox, oy - 90, "ax", ar=True)
    s.circ(ox + 2 * k, oy, 5, "pt cv")
    s.circ(ox, oy - 2 * k, 5, "pt cv")
    s.line(ox + 2 * k, oy, ox, oy - 2 * k, "gd")
    s.t(ox + 2 * k, oy + 16, "(A,0)", "ts")
    s.t(ox - 4, oy - 2 * k + 4, "(0,A)", "ts", "end")
    s.t(ox + k + 6, oy - k - 4, "d = √2 A", "ts a1", "start")
    s.t(336, 160, "η_P = 1/2", "tx a2")
    s.t(200, 184, "η_P = d²_min / (4 E_b): a parità di E_b, l'antipodale separa di più", "ts")
    return s.render(), "🧩 Le tre costellazioni binarie della slide 16. L'antipodale ha $d_{min}^2=4E_b$, le altre due solo $2E_b$: per la stessa probabilità d'errore richiedono circa 3 dB in più di $E_b/N_0$."


def _ebn0_per_ber(famiglia, M, ber=1e-5):
    """E_b/N_0 [dB] per la BER data con l'approssimazione (6) e codifica di Gray (dove serve)."""
    k = math.log2(M)
    if famiglia == "PSK":
        eta, nv = k * math.sin(math.pi / M) ** 2, (1 if M == 2 else 2)
        f = lambda g: nv / 2 * math.erfc(math.sqrt(eta * g)) / k
    elif famiglia == "QAM":
        eta, nv = 3 * k / (2 * (M - 1)), 4 * (1 - 1 / math.sqrt(M))
        f = lambda g: nv / 2 * math.erfc(math.sqrt(eta * g)) / k
    else:  # ortogonale coerente
        eta = k / 2
        f = lambda g: (M - 1) / 2 * math.erfc(math.sqrt(eta * g)) * (M / 2) / (M - 1)
    lo, hi = -5.0, 40.0
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(10 ** (m / 10)) > ber else (lo, m)
    return lo


def fig_piano_shannon():
    s = Svg(400, 290, "frontiera di Shannon e modulazioni")
    ox, oy, W, H = 44, 248, 330, 222
    x = lambda db: ox + W * (db + 2) / 22          # E_b/N_0 da -2 a 20 dB
    y = lambda eta: oy - H * (math.log2(eta) + 3) / 7  # eta_B da 1/8 a 16
    curva = [(10 * math.log10((2 ** e - 1) / e), e) for e in np.geomspace(1 / 8, 16, 120)]
    zona = [(x(-2), y(1 / 8))] + [(x(db), y(e)) for db, e in curva if db <= 20] + [(x(20), y(16)), (x(-2), y(16))]
    s.poly(zona, "fl2", True)
    s.poly([(x(db), y(e)) for db, e in curva if db <= 20], "cv2")
    s.line(ox - 4, oy, ox + W + 8, oy, "ax", ar=True)
    s.line(x(0), oy + 3, x(0), oy - H - 8, "gd")
    s.line(ox, oy + 3, ox, oy - H - 10, "ax", ar=True)
    s.line(x(-1.59), oy, x(-1.59), y(1 / 8), "gd")
    s.line(ox, y(1), ox + W, y(1), "gd")
    for db in (0, 5, 10, 15, 20):
        s.line(x(db), oy - 3, x(db), oy + 3, "ln")
        s.t(x(db), oy + 15, str(db), "ts")
    for e, lab in ((1 / 8, "1/8"), (1 / 2, "1/2"), (1, "1"), (2, "2"), (4, "4"), (8, "8"), (16, "16")):
        s.line(ox - 3, y(e), ox + 3, y(e), "ln")
        s.t(ox - 6, y(e) + 4, lab, "ts", "end")
    s.t(ox + W + 8, oy + 30, "E_b/N_0 [dB]", "ts", "end")
    s.t(ox + 6, 14, "η_B [bit/s/Hz]", "ts", "start")
    s.t(x(-1.2), y(1 / 8) - 30, "−1.59 dB", "ts a2", "start")
    s.t(x(1.5), y(10), "impossibile", "tx a2", "start")
    s.t(x(1.2), y(1) - 6, "limitata in banda ↑", "ts", "start")
    s.t(x(1.2), y(1) + 14, "limitata in potenza ↓", "ts", "start")
    serie = (("PSK", (2, 4, 8, 16), "cv", lambda M: math.log2(M)),
             ("QAM", (16, 64), "cv3", lambda M: math.log2(M)),
             ("ORT", (2, 4, 8, 16), "cv4", lambda M: 2 * math.log2(M) / M))
    for fam, Ms, cl, etab in serie:
        pts = [(x(_ebn0_per_ber(fam, M)), y(etab(M))) for M in Ms]
        s.poly(pts, cl + " dash")
        for (px, py), M in zip(pts, Ms):
            s.circ(px, py, 3.6, "pt " + cl)
            if fam == "ORT":
                s.t(px + 2, py + 15, str(M), "ts", "middle")
            else:
                s.t(px - 6, py - 5, str(M), "ts", "end")
    lx, ly = x(13.2), y(1 / 2) - 10
    for i, (nome, cl) in enumerate((("M-PSK", "cv"), ("M-QAM", "cv3"), ("M-FSK ortogonale", "cv4"))):
        s.line(lx, ly + i * 16, lx + 18, ly + i * 16, cl)
        s.t(lx + 24, ly + i * 16 + 4, nome, "ts", "start")
    return s.render(), ("🧩 Frontiera $E_b/N_0=(2^{\\eta_B}-1)/\\eta_B$ (curva arancione): a sinistra la regione impossibile, che per $\\eta_B\\to0$ tende a $-1.59$ dB. "
                        "I punti sono le modulazioni a BER $=10^{-5}$, calcolati da me con l'approssimazione (6) e codifica di Gray: PSK e QAM salgono e vanno a destra al crescere di $M$, le ortogonali scendono e vanno a sinistra. "
                        "Stesso significato della figura della slide 23.")


def fig_bilancio_wlan():
    s = Svg(400, 300, "bilancio di potenza dell'esempio WLAN")
    oy0, H = 24, 236
    lv = lambda dbm: oy0 + H * (25 - dbm) / 125     # da +25 a -100 dBm
    ax = 46
    s.line(ax, lv(-100) + 4, ax, lv(25) - 10, "ax", ar=True)
    for d in (20, 0, -20, -40, -60, -80, -100):
        s.line(ax - 3, lv(d), ax + 3, lv(d), "ln")
        s.t(ax - 6, lv(d) + 4, str(d), "ts", "end")
    s.t(ax + 4, 12, "dBm", "ts", "start")
    passi = [(20, "P_{tx}", "20"), (22, "+G_{tx}", "22"), (-65, "−L_{path}", "−65"), (-63, "+G_{rx}", "−63")]
    xs = [62, 104, 146, 188]
    prev = None
    for (val, nome, num), x0 in zip(passi, xs):
        if prev is not None:
            s.line(x0, lv(prev), x0, lv(val), "cv dash")
        s.line(x0, lv(val), x0 + 34, lv(val), "cv ev")
        s.t(x0 + 17, lv(val) - 6, num, "ts a1")
        s.t(x0 + 17, lv(-100) + 22, nome, "ts a1")
        prev = val
    s.t(138, lv(-22), "−87 dB", "ts a1", "end")
    s.t(138, lv(-22) + 13, "di propagazione", "ts a1", "end")
    s.line(ax, lv(-95), 392, lv(-95), "gd")
    s.t(392, lv(-95) + 14, "rumore P_n = −95", "ts", "end")
    s.line(ax, lv(-83), 392, lv(-83), "cv2")
    s.t(392, lv(-83) - 5, "sensibilità −83", "ts a2", "end")
    s.line(222, lv(-63), 300, lv(-63), "gd")
    s.line(276, lv(-95), 276, lv(-83), "ar2", ar=True, ar0=True)
    s.t(282, lv(-89) + 4, "SNR_{req} 12 dB", "ts", "start")
    s.line(250, lv(-83), 250, lv(-63), "ar2", ar=True, ar0=True)
    s.t(256, lv(-73) + 4, "margine 20 dB", "ts", "start")
    return s.render(), ("🧩 Bilancio dell'esempio in dBm: 20 dBm trasmessi, +2 dB d'antenna, −87 dB di propagazione, +2 dB d'antenna: arrivano −63 dBm. "
                        "Il ricevitore ha un rumore di −95 dBm e per la BER richiesta servono 12 dB sopra il rumore (sensibilità −83 dBm); i 20 dB restanti sono il margine.")


# --------------------------------------------------------------------------------------------- Lezioni 8–11

def _gonna(s, x0, x1, y0, h, fn, cl="cv", n=160):
    xs = np.linspace(x0, x1, n)
    s.poly([(x, y0 - h * fn(x)) for x in xs], cl)


def fig_forme_mary():
    s = Svg(400, 372, "stessa sequenza di bit con M = 2, 4, 8")
    bits = "100101111000"
    x0, w = 74, 314 / 12
    righe = ((2, 1, {"1": 1, "0": -1}, 1, 58, 30), (4, 2, {"10": 3, "11": 1, "01": -1, "00": -3}, 3, 158, 40),
             (8, 3, {"111": 7, "101": 5, "100": 3, "110": 1, "010": -1, "011": -3, "001": -5, "000": -7}, 7, 286, 56))
    for M, h, mappa, amax, yc, hh in righe:
        k = hh / amax
        s.line(x0 - 4, yc, 392, yc, "ax", ar=True)
        s.line(x0, yc + hh + 6, x0, yc - hh - 10, "ax", ar=True)
        for v in range(-amax, amax + 1, 2):
            s.line(x0 - 3, yc - k * v, x0 + 3, yc - k * v, "ax")
            s.t(x0 - 6, yc - k * v + 4, f"{v}".replace("-", "−"), "ts", "end")
        s.t(8, yc + 4, f"M={M}", "tx tb a1", "start")
        pts = []
        for i in range(0, 12, h):
            v = mappa[bits[i:i + h]]
            xa, xb = x0 + i * w, x0 + (i + h) * w
            pts += [(xa, yc - k * v), (xb, yc - k * v)]
            s.line(xb, yc - 3, xb, yc + 3, "gd")
        s.poly(pts, "cv")
        s.t(x0 + h * w / 2 + 6, yc + hh + 16, f"T = {h}T_b", "ts a2")
    for i, b in enumerate(bits):
        s.t(x0 + (i + .5) * w, 14, b, "ts")
    return s.render(), ("🧩 Più bit per simbolo: simboli più lunghi, livelli più vicini. "
                        "In ordinata i livelli PAM $a_i=(2i-1-M)\\frac d2$ con $d=2$, cioè $\\pm1,\\pm3,\\dots,\\pm(M-1)$.")


def fig_nrz_rz():
    s = Svg(400, 200, "segnali NRZ e RZ")
    bits = [1, 0, 1, 1, 0, 0, 1]
    x0, w = 50, 46
    for r, (nome, frac) in enumerate((("NRZ", 1.0), ("RZ", 0.5))):
        yc = 58 + r * 92
        s.line(x0 - 4, yc, 392, yc, "ax", ar=True)
        s.t(10, yc + 4, nome, "tx tb a1", "start")
        pts = []
        for i, b in enumerate(bits):
            v = -1 if b else 1
            xa = x0 + i * w
            pts += [(xa, yc), (xa, yc - 30 * v), (xa + frac * w, yc - 30 * v), (xa + frac * w, yc)]
            if r == 0:
                s.t(xa + w / 2, 14, str(b), "ts")
        s.poly(pts, "cv")
        s.t(x0 - 8, yc - 26, "A", "ts", "end")
        s.t(x0 - 8, yc + 34, "−A", "ts", "end")
    return s.render(), "🧩 NRZ tiene il livello per tutto il simbolo, RZ per metà."


def _punto(s, x, y, lab=None, dy=-8, cl="cv"):
    s.circ(x, y, 4, "pt " + cl)
    if lab:
        s.t(x, y + dy, lab, "ts")


def fig_costellazioni_lineari():
    s = Svg(400, 330, "costellazioni PAM, QPSK, 8-PSK, 16-QAM")
    # PAM-4
    y = 46
    s.t(10, 18, "4-PAM", "tx tb a1", "start")
    s.line(30, y, 380, y, "ax", ar=True)
    for v, lab in ((-3, "00"), (-1, "10"), (1, "11"), (3, "01")):
        _punto(s, 205 + v * 40, y, lab, -10)
        s.t(205 + v * 40, y + 16, str(v), "ts")
    # QPSK
    cx, cy, R = 100, 170, 50
    s.t(10, 96, "QPSK (Gray)", "tx tb a1", "start")
    s.line(cx - 70, cy, cx + 70, cy, "ax")
    s.line(cx, cy + 70, cx, cy - 70, "ax")
    s.circ(cx, cy, R, "gd")
    for a, lab in ((45, "00"), (135, "01"), (225, "11"), (315, "10")):
        x, yy = cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a))
        _punto(s, x, yy)
        s.t(cx + (R + 16) * math.cos(math.radians(a)), cy - (R + 16) * math.sin(math.radians(a)) + 4, lab, "ts")
    # 8-PSK
    cx = 300
    s.t(220, 96, "8-PSK", "tx tb a1", "start")
    s.line(cx - 70, cy, cx + 70, cy, "ax")
    s.line(cx, cy + 70, cx, cy - 70, "ax")
    s.circ(cx, cy, R, "gd")
    for i in range(8):
        a = math.radians(45 * i)
        _punto(s, cx + R * math.cos(a), cy - R * math.sin(a))
    # 16-QAM
    cx, cy = 205, 290
    s.t(10, 262, "16-QAM", "tx tb a1", "start")
    s.line(cx - 70, cy, cx + 70, cy, "ax")
    s.line(cx, cy + 38, cx, cy - 38, "ax")
    for i in (-3, -1, 1, 3):
        for j in (-3, -1, 1, 3):
            _punto(s, cx + 16 * i, cy - 11 * j)
    return s.render(), "🧩 Costellazioni: PAM su una retta, PSK su un cerchio, QAM su una griglia."


def fig_psd_sinc2():
    s = Svg(400, 190, "PSD per impulso rettangolare")
    ox, oy, kx, ky = 200, 160, 50, 130
    s.line(20, oy, 390, oy, "ax", ar=True)
    s.line(ox, oy + 4, ox, oy - ky - 12, "ax", ar=True)
    f = lambda x: 1.0 if abs(x) < 1e-9 else (math.sin(math.pi * x) / (math.pi * x)) ** 2
    pts = [(ox + kx * x, oy - ky * f(x)) for x in np.linspace(-3.5, 3.5, 400)]
    s.poly([(ox - kx * 1, oy)] + [(ox + kx * x, oy - ky * f(x)) for x in np.linspace(-1, 1, 120)] + [(ox + kx * 1, oy)], "fl", True)
    s.poly(pts, "cv")
    for k in (-3, -2, -1, 1, 2, 3):
        s.t(ox + kx * k, oy + 15, f"{k}/T", "ts")
    s.t(390, oy + 15, "f", "ts", "end")
    s.t(ox + 8, oy - ky - 8, "S_{ss}(f) ∝ sinc²(fT)", "ts", "start")
    return s.render(), "🧩 Il lobo principale è largo 2/T: simboli più lunghi, banda più stretta."


def fig_base_ortonormale():
    s = Svg(400, 220, "vettore nello spazio dei segnali")
    ox, oy = 120, 190
    s.line(ox - 10, oy, 380, oy, "ax", ar=True)
    s.line(ox, oy + 10, ox, 14, "ax", ar=True)
    s.t(380, oy + 15, "ψ_1(t)", "ts", "end")
    s.t(ox + 6, 18, "ψ_2(t)", "ts", "start")
    px, py = 200, 120
    s.line(ox, oy, ox + px, oy - py, "cv", ar=True)
    s.line(ox + px, oy - py, ox + px, oy, "gd")
    s.line(ox, oy - py, ox + px, oy - py, "gd")
    s.t(ox + px / 2, oy + 16, "s_i(1) = ⟨s_i, ψ_1⟩", "ts a1")
    s.t(ox - 6, oy - py + 4, "s_i(2)", "ts a1", "end")
    s.t(ox + px + 8, oy - py, "s_i = [s_i(1), s_i(2)]", "tx a1", "start")
    s.t(ox + px / 2 - 30, oy - py / 2 - 10, "‖s_i‖² = E_i", "ts a2", "end")
    return s.render(), "🧩 Ogni forma d'onda è un punto: le coordinate sono le proiezioni sulla base."


def fig_fsk_ortogonalita():
    s = Svg(400, 210, "prodotto scalare tra due toni in funzione della spaziatura")
    ox, oy, kx, ky = 40, 120, 160, 80
    s.line(ox - 4, oy, 392, oy, "ax", ar=True)
    s.line(ox, oy + 70, ox, oy - ky - 12, "ax", ar=True)
    coer = lambda x: 1.0 if x == 0 else math.sin(2 * math.pi * x) / (2 * math.pi * x)
    nonc = lambda x: 1.0 if x == 0 else abs(math.sin(math.pi * x) / (math.pi * x))
    xs = np.linspace(0, 2.15, 300)
    s.poly([(ox + kx * x, oy - ky * coer(x)) for x in xs], "cv")
    s.poly([(ox + kx * x, oy - ky * nonc(x)) for x in xs], "cv2 dash")
    for x, lab in ((0.5, "1/(2T)"), (1, "1/T"), (1.5, "3/(2T)"), (2, "2/T")):
        s.line(ox + kx * x, oy - 3, ox + kx * x, oy + 3, "ln")
        s.t(ox + kx * x, oy + 16, lab, "ts")
    s.circ(ox + kx * .5, oy, 4, "pt cv")
    s.circ(ox + kx * 1, oy, 4, "pt cv2")
    s.t(392, oy + 32, "Δf", "ts", "end")
    s.t(250, 30, "coerente", "ts a1", "start")
    s.t(250, 46, "non coerente (modulo)", "ts a2", "start")
    s.line(222, 26, 244, 26, "cv")
    s.line(222, 42, 244, 42, "cv2 dash")
    return s.render(), "🧩 Primo zero a 1/(2T) se la fase è nota, a 1/T se non lo è."


def fig_onoff_decisione():
    s = Svg(400, 200, "decisione on-off con soglia a metà")
    ox, oy, k, H = 90, 160, 60, 110
    g = lambda x, m: math.exp(-((x - m) ** 2) / 0.5)
    s.line(20, oy, 392, oy, "ax", ar=True)
    xs = np.linspace(-1.2, 4.0, 300)
    soglia = 1.25
    s.poly([(ox + k * soglia, oy)] + [(ox + k * x, oy - H * g(x, 0)) for x in np.linspace(soglia, 2.6, 60)] + [(ox + k * 2.6, oy)], "fl", True)
    s.poly([(ox + k * -0.2, oy)] + [(ox + k * x, oy - H * g(x, 2.5)) for x in np.linspace(-0.2, soglia, 60)] + [(ox + k * soglia, oy)], "fl2", True)
    s.poly([(ox + k * x, oy - H * g(x, 0)) for x in xs], "cv")
    s.poly([(ox + k * x, oy - H * g(x, 2.5)) for x in xs], "cv2")
    s.line(ox + k * soglia, oy + 4, ox + k * soglia, oy - H - 6, "gd")
    s.t(ox, oy + 15, "0", "ts")
    s.t(ox + k * 2.5, oy + 15, "√E_s", "ts")
    s.t(ox + k * soglia, oy + 15, "√E_s/2", "ts a2")
    s.t(ox - 10, oy - H - 4, "H_0", "tx a1", "end")
    s.t(ox + k * 2.5 + 12, oy - H - 4, "H_1", "tx a2", "start")
    s.t(392, oy + 30, "r", "ts", "end")
    return s.render(), "🧩 Le code oltre la soglia sono la probabilità d'errore."


def fig_ricevitore_correlatori():
    s = Svg(400, 210, "ricevitore ottimo a correlatori")
    s.t(18, 108, "r(t)", "tx a1")
    s.line(36, 104, 56, 104, "ln")
    s.line(56, 40, 56, 170, "ln")
    for i, (y, lab) in enumerate(((40, "1"), (104, "2"), (170, "M"))):
        s.line(56, y, 80, y, "ln", ar=True)
        s.mult(90, y)
        s.t(90, y - 16, f"s_{lab}(t)", "ts")
        s.line(99, y, 120, y, "ln", ar=True)
        s.rect(120, y - 14, 60, 28, "bx bx1")
        s.t(150, y + 4, "∫_0^T dt", "ts")
        s.line(180, y, 206, y, "ln", ar=True)
        s.circ(215, y, 9)
        s.t(215, y + 4, "+", "ts")
        s.t(215, y - 14, f"−E_{lab}/2", "ts a2")
        s.line(224, y, 290, y, "ln", ar=True)
        s.t(258, y - 6, f"λ_{lab}", "ts a1")
    s.t(150, 140, "⋮", "tx")
    s.rect(290, 26, 50, 158, "bx bx2")
    s.t(315, 108, "MAX", "tx tb")
    s.line(340, 104, 386, 104, "ln", ar=True)
    s.t(364, 96, "m̂", "tx")
    return s.render(), "🧩 Banco di correlatori; ogni ramo può essere un filtro adattato s_k(T−t) campionato in T."


def fig_voronoi():
    s = Svg(400, 260, "regioni di Voronoi")
    P = [(120, 150), (260, 80), (300, 200), (170, 50)]
    W, H = 400, 260
    import itertools
    for (a, b) in itertools.combinations(range(len(P)), 2):
        # confine: punti equidistanti da a e b e non più vicini a un terzo
        seg = []
        (xa, ya), (xb, yb) = P[a], P[b]
        mx, my = (xa + xb) / 2, (ya + yb) / 2
        dx, dy = -(yb - ya), xb - xa
        n = math.hypot(dx, dy)
        dx, dy = dx / n, dy / n
        for t in np.linspace(-400, 400, 1601):
            x, y = mx + t * dx, my + t * dy
            if not (0 <= x <= W and 0 <= y <= H):
                continue
            da = (x - xa) ** 2 + (y - ya) ** 2
            if all(da <= (x - P[c][0]) ** 2 + (y - P[c][1]) ** 2 + 1e-6 for c in range(len(P)) if c not in (a, b)):
                seg.append((x, y))
        if len(seg) > 1:
            s.line(seg[0][0], seg[0][1], seg[-1][0], seg[-1][1], "ln")
    for i, (x, y) in enumerate(P):
        s.circ(x, y, 5, "pt cv")
        s.t(x + 10, y - 8, f"s_{i + 1}", "tx a1", "start")
    return s.render(), "🧩 Ogni regione contiene i punti più vicini al suo segnale."


def _Q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def fig_ber_binarie():
    s = Svg(400, 250, "probabilità d'errore di antipodale e ortogonale")
    ox, oy, W, H = 50, 220, 330, 200
    x = lambda db: ox + W * db / 14
    y = lambda p: oy - H * (-math.log10(p)) / 7
    s.line(ox - 4, oy, ox + W + 8, oy, "ax", ar=True)
    s.line(ox, oy + 4, ox, oy - H - 10, "ax", ar=True)
    for e in range(1, 8):
        s.line(ox, y(10 ** -e), ox + W, y(10 ** -e), "gd")
        s.t(ox - 6, y(10 ** -e) + 4, f"10^{{−{e}}}", "ts", "end")
    for db in (0, 4, 8, 12):
        s.t(x(db), oy + 15, str(db), "ts")
    dbs = np.linspace(0, 14, 200)
    for fn, cl in ((lambda g: 0.5 * math.erfc(math.sqrt(g)), "cv"), (lambda g: 0.5 * math.erfc(math.sqrt(g / 2)), "cv2")):
        pts = [(x(d), y(fn(10 ** (d / 10)))) for d in dbs if fn(10 ** (d / 10)) > 1e-7]
        s.poly(pts, cl)
    s.t(x(4.2), y(1e-5), "antipodale", "ts a1", "end")
    s.t(x(12.7), y(1e-4), "ortogonale, on-off", "ts a2", "start")
    s.t(ox + W + 8, oy + 30, "E_b/N_0 [dB]", "ts", "end")
    s.t(ox + 6, 14, "P(e)", "ts", "start")
    return s.render(), "🧩 A parità di E_b l'antipodale guadagna 3 dB."


def fig_qpsk_regioni():
    s = Svg(400, 230, "regioni di decisione della QPSK")
    cx, cy, R = 200, 116, 70
    s.rect(cx, cy - 104, 170, 104, "fl", 0)
    s.line(cx - 180, cy, cx + 180, cy, "ax", ar=True)
    s.line(cx, cy + 104, cx, cy - 106, "ax", ar=True)
    for a, lab in ((45, "s_1 · 00"), (135, "s_2 · 01"), (225, "s_3 · 11"), (315, "s_4 · 10")):
        xx, yy = cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a))
        s.circ(xx, yy, 5, "pt cv")
        s.t(xx + (14 if math.cos(math.radians(a)) > 0 else -14), yy + 4, lab, "ts", "start" if math.cos(math.radians(a)) > 0 else "end")
    s.t(cx + 160, cy - 86, "Z_1", "tx tb a1", "end")
    s.t(cx + 176, cy + 15, "z_1", "ts", "end")
    s.t(cx + 6, cy - 98, "z_2", "ts", "start")
    return s.render(), "🧩 Si decide dai segni di z_1 e z_2: le regioni sono i quadranti."


def fig_union_bound():
    s = Svg(400, 230, "union bound")
    k, a, b = (200, 140), (110, 70), (300, 80)
    def semipiano(p, q, cl):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = q[0] - p[0], q[1] - p[1]
        n = math.hypot(dx, dy)
        ux, uy = dx / n, dy / n
        tx, ty = -uy, ux
        L = 400
        pts = [(mx + tx * L, my + ty * L), (mx - tx * L, my - ty * L), (mx - tx * L + ux * L, my - ty * L + uy * L), (mx + tx * L + ux * L, my + ty * L + uy * L)]
        s.poly(pts, cl, True)
        s.line(mx + tx * 200, my + ty * 200, mx - tx * 200, my - ty * 200, "gd")
    semipiano(k, a, "fl")
    semipiano(k, b, "fl2")
    for p, lab, cl in ((k, "s_k", "cv"), (a, "s_i", "cv"), (b, "s_j", "cv2")):
        s.circ(p[0], p[1], 5, "pt " + cl)
        s.t(p[0] + 8, p[1] + 16, lab, "tx a1", "start")
    s.t(200, 20, "zona contata due volte", "ts a2")
    return s.render(), "🧩 La somma delle due PEP conta due volte la zona sovrapposta: maggiorante."


def fig_qam16_vicini():
    s = Svg(400, 230, "vicini a distanza minima nella 16-QAM")
    cx, cy, d = 200, 112, 44
    for i in (-3, -1, 1, 3):
        for j in (-3, -1, 1, 3):
            nv = (2 if abs(i) == 3 else 3) if abs(i) == 3 or abs(j) == 3 else 4
            if abs(i) == 3 and abs(j) == 3:
                nv = 2
            elif abs(i) == 3 or abs(j) == 3:
                nv = 3
            cl = {2: "cv2", 3: "cv3", 4: "cv"}[nv]
            x, y = cx + i * d / 2, cy - j * d / 2
            s.circ(x, y, 6, "pt " + cl)
            s.t(x + 11, y - 6, str(nv), "ts", "start")
    s.line(cx + d / 2, cy + d * 1.9, cx + 3 * d / 2, cy + d * 1.9, "ar2", ar=True, ar0=True)
    s.t(cx + d, cy + d * 1.9 + 14, "d", "ts a2")
    s.t(20, 30, "4 interni × 4", "ts a1", "start")
    s.t(20, 46, "8 di bordo × 3", "ts a3", "start")
    s.t(20, 62, "4 d'angolo × 2", "ts a2", "start")
    s.t(20, 86, "N̄ = 48/16 = 3", "tx", "start")
    return s.render(), "🧩 Numero di vicini a distanza d per ogni punto."


# --------------------------------------------------------------------------------------------- Lezione 13

def fig_sync_costellazione():
    s = Svg(400, 220, "costellazione scalata e ruotata dal canale e dall'offset")
    cx, cy, R = 200, 112, 62
    s.line(cx - 170, cy, cx + 170, cy, "ax", ar=True)
    s.line(cx, cy + 100, cx, cy - 102, "ax", ar=True)
    th = math.radians(28)
    for a in (45, 135, 225, 315):
        r = math.radians(a)
        s.circ(cx + R * math.cos(r), cy - R * math.sin(r), 5, "pt cv")
        x2, y2 = cx + 1.25 * R * math.cos(r + th), cy - 1.25 * R * math.sin(r + th)
        s.circ(x2, y2, 5, "pt cv2")
    r = math.radians(45)
    pts = [(cx + 0.55 * R * math.cos(r + u), cy - 0.55 * R * math.sin(r + u)) for u in np.linspace(0, th, 20)]
    s.poly(pts, "ar2", ar=True)
    s.t(cx + 0.9 * R * math.cos(r + th / 2) + 4, cy - 0.62 * R * math.sin(r + th / 2) - 2, "θ", "ts a2", "start")
    pts = [(cx + 1.55 * R * math.cos(math.radians(a)), cy - 1.55 * R * math.sin(math.radians(a))) for a in np.linspace(80, 120, 20)]
    s.poly(pts, "ar2", ar=True)
    s.t(cx - 30, cy - 1.62 * R - 4, "2πΔf t", "ts a2", "end")
    s.t(20, 24, "● trasmessa", "ts a1", "start")
    s.t(20, 40, "● ricevuta: × A, ruotata", "ts a2", "start")
    return s.render(), "🧩 A scala, θ ruota, Δf fa girare la costellazione nel tempo."


def fig_downconv_lo():
    s = Svg(400, 170, "down-conversion con LO a f_c − Δf")
    s.t(26, 89, "y_p(t)", "tx a1")
    s.line(50, 85, 70, 85, "ln")
    s.line(70, 40, 70, 130, "ln")
    for y, lo, out in ((40, "√2 cos ω_{LO}t", "y_I(t)"), (130, "−√2 sin ω_{LO}t", "y_Q(t)")):
        s.line(70, y, 120, y, "ln", ar=True)
        s.mult(130, y)
        s.t(130, y + (26 if y > 85 else -16), lo, "ts a2")
        s.line(139, y, 190, y, "ln", ar=True)
        s.rect(190, y - 14, 60, 28, "bx bx1")
        s.t(220, y + 4, "LPF", "ts")
        s.line(250, y, 330, y, "ln", ar=True)
        s.t(345, y + 4, out, "tx", "start")
    s.t(220, 92, "ω_{LO} = 2π(f_c − Δf)", "ts")
    return s.render(), "🧩 Ogni ramo dà una miscela di v_I e v_Q ruotata di 2πΔf t."


def fig_acq_tracking():
    s = Svg(400, 120, "acquisizione e tracking")
    y = 60
    s.rect(20, y - 18, 100, 36, "bx bx1")
    s.t(70, y + 4, "preambolo", "ts")
    s.rect(120, y - 18, 260, 36, "bx")
    s.t(250, y + 4, "dati", "ts")
    s.line(20, y + 30, 120, y + 30, "ar2", ar=True, ar0=True)
    s.t(70, y + 46, "acquisizione (training)", "ts a1")
    s.line(120, y + 30, 380, y + 30, "ar2", ar=True, ar0=True)
    s.t(250, y + 46, "tracking: decision-directed o blind", "ts a2")
    s.t(200, 22, "nei sistemi a pacchetto il tracking spesso non serve", "ts")
    return s.render(), "🧩 Stima iniziale con i simboli noti, poi aggiornamento continuo."


def fig_famiglia_pdf():
    s = Svg(400, 160, "famiglia di pdf parametrizzata da θ")
    oy, k, H = 130, 40, 90
    s.line(20, oy, 390, oy, "ax", ar=True)
    s.line(200, oy + 4, 200, 20, "gd")
    s.t(200, oy + 15, "0", "ts")
    for m, cl, lab in ((-2.6, "cv", "θ_1"), (0.4, "cv2", "θ_2"), (3.0, "cv3", "θ_3")):
        xs = np.linspace(m - 2.2, m + 2.2, 80)
        s.poly([(200 + k * x, oy - H * math.exp(-(x - m) ** 2 / 0.6)) for x in xs], cl)
        s.t(200 + k * m, oy + 15, lab, "ts")
    s.line(200 + k * -2.2, oy + 2, 200 + k * -2.2, oy - 70, "ar2", ar=True)
    s.t(200 + k * -2.2 - 4, oy - 76, "y(0) osservato", "ts a2", "end")
    return s.render(), "🧩 Con y(0) < 0 la pdf più verosimile è quella di θ_1."


def fig_blind_miscela():
    s = Svg(400, 170, "verosimiglianza blind: miscela di due gaussiane")
    oy, k, H = 140, 55, 100
    s.line(20, oy, 390, oy, "ax", ar=True)
    xs = np.linspace(-3.3, 3.3, 300)
    g = lambda x, m: math.exp(-(x - m) ** 2 / 0.5)
    s.poly([(200 + k * x, oy - H * 0.5 * g(x, -1.5)) for x in xs], "cv3")
    s.poly([(200 + k * x, oy - H * 0.5 * g(x, 1.5)) for x in xs], "cv2")
    s.poly([(200 + k * x, oy - H * (0.5 * g(x, -1.5) + 0.5 * g(x, 1.5))) for x in xs], "cv")
    s.t(200 - 1.5 * k, oy + 15, "−A", "ts")
    s.t(200 + 1.5 * k, oy + 15, "+A", "ts")
    s.t(390, oy + 15, "y(k)", "ts", "end")
    s.t(200 - 1.5 * k, oy - H * 0.5 - 8, "b = −1, peso ½", "ts a3")
    s.t(200 + 1.5 * k, oy - H * 0.5 - 8, "b = +1, peso ½", "ts a2")
    return s.render(), "🧩 Senza conoscere b(k), y(k) segue la somma pesata delle due gaussiane."


def fig_tanh_soft():
    s = Svg(400, 170, "decisione soffice tanh e decisione dura")
    ox, oy, kx, ky = 200, 85, 45, 55
    s.line(30, oy, 380, oy, "ax", ar=True)
    s.line(ox, 160, ox, 12, "ax", ar=True)
    xs = np.linspace(-3.6, 3.6, 200)
    s.poly([(ox + kx * x, oy - ky * math.tanh(x)) for x in xs], "cv")
    s.poly([(ox + kx * -3.6, oy + ky), (ox, oy + ky), (ox, oy - ky), (ox + kx * 3.6, oy - ky)], "cv2")
    s.t(ox - 6, oy - ky + 4, "+1", "ts", "end")
    s.t(ox + 6, oy + ky + 4, "−1", "ts", "start")
    s.t(380, oy + 15, "A y/σ²", "ts", "end")
    s.t(36, 22, "tanh: blind (soffice)", "ts a1", "start")
    s.t(36, 38, "sgn: decision-directed", "ts a2", "start")
    return s.render(), "🧩 tanh(Ay/σ²) prende il posto del simbolo b(k): a SNR alto diventa il segno."


def fig_fase_ml():
    s = Svg(400, 210, "stima ML della fase come argomento della correlazione")
    ox, oy = 150, 170
    s.line(30, oy, 380, oy, "ax", ar=True)
    s.line(ox, 200, ox, 14, "ax", ar=True)
    phi = math.radians(38)
    L = 170
    s.line(ox, oy, ox + L * math.cos(phi), oy - L * math.sin(phi), "ar2", ar=True)
    s.t(ox + L * math.cos(phi) + 6, oy - L * math.sin(phi), "Z = ⟨y, s⟩", "tx a2", "start")
    s.line(ox + L * math.cos(phi), oy - L * math.sin(phi), ox + L * math.cos(phi), oy, "gd")
    s.line(ox + L * math.cos(phi), oy - L * math.sin(phi), ox, oy - L * math.sin(phi), "gd")
    s.t(ox + L * math.cos(phi), oy + 15, "Z_c", "ts")
    s.t(ox - 6, oy - L * math.sin(phi) + 4, "Z_s", "ts", "end")
    pts = [(ox + 40 * math.cos(u), oy - 40 * math.sin(u)) for u in np.linspace(0, phi, 20)]
    s.poly(pts, "cv")
    s.t(ox + 50, oy - 12, "φ = θ̂", "ts a1", "start")
    return s.render(), "🧩 θ̂ = φ = tan⁻¹(Z_s/Z_c): massimizza |Z| cos(φ − θ)."


def fig_pll():
    s = Svg(400, 180, "phase-locked loop")
    s.t(30, 50, "y_p(t)", "tx a1")
    s.line(55, 46, 140, 46, "ln", ar=True)
    s.mult(150, 46)
    s.line(159, 46, 210, 46, "ln", ar=True)
    s.rect(210, 30, 90, 32, "bx bx1")
    s.t(255, 50, "loop filter", "ts")
    s.t(255, 22, "∫ dt", "ts a2")
    s.line(300, 46, 350, 46, "ln")
    s.line(350, 46, 350, 140, "ln", ar=True)
    s.rect(210, 122, 140, 36, "bx bx2")
    s.t(280, 144, "VCO: dθ̂/dt = γ c(t)", "ts")
    s.line(210, 140, 150, 140, "ln")
    s.line(150, 140, 150, 57, "ln", ar=True)
    s.t(146, 104, "−sin(2πf_c t + θ̂)", "ts a2", "end")
    s.t(358, 96, "c(t)", "ts", "start")
    return s.render(), "🧩 Il prodotto misura l'errore di fase, il filtro lo integra, il VCO corregge."


def fig_curva_s():
    s = Svg(400, 170, "termine d'errore del PLL")
    ox, oy, kx, ky = 200, 85, 50, 60
    s.line(30, oy, 380, oy, "ax", ar=True)
    s.line(ox, 160, ox, 12, "ax", ar=True)
    xs = np.linspace(-math.pi, math.pi, 200)
    s.poly([(ox + kx * x, oy - ky * math.sin(x)) for x in xs], "cv")
    s.circ(ox, oy, 5, "pt cv2")
    s.t(ox + kx * math.pi, oy + 15, "π", "ts")
    s.t(ox - kx * math.pi, oy + 15, "−π", "ts")
    s.t(380, oy - 8, "θ̂ − θ", "ts", "end")
    s.t(ox + 8, oy + 18, "aggancio", "ts a2", "start")
    s.t(ox + kx * 1.6, oy - ky - 6, "θ̂ scende", "ts a1")
    s.t(ox - kx * 1.6, oy + ky + 14, "θ̂ sale", "ts a1")
    return s.render(), "🧩 (T₀/2) sin(θ̂ − θ): segno e modulo dell'errore."


def fig_costas():
    s = Svg(400, 200, "Costas loop")
    s.t(22, 104, "r(t)", "tx a1")
    s.line(40, 100, 70, 100, "ln")
    s.line(70, 36, 70, 164, "ln")
    for y, lo, e in ((36, "cos", "e_1"), (164, "−sin", "e_2")):
        s.line(70, y, 110, y, "ln", ar=True)
        s.mult(120, y)
        s.line(129, y, 180, y, "ln", ar=True)
        s.rect(180, y - 13, 50, 26, "bx bx1")
        s.t(205, y + 4, "LPF", "ts")
        s.line(230, y, 330, y, "ln")
        s.t(280, y - 6, e, "ts a1")
        s.line(330, y, 330, 100 + (-9 if y < 100 else 9), "ln", ar=True)
    s.mult(330, 100)
    s.line(321, 100, 280, 100, "ln", ar=True)
    s.rect(230, 88, 50, 24, "bx bx1")
    s.t(255, 104, "loop", "ts")
    s.line(230, 100, 190, 100, "ln", ar=True)
    s.rect(140, 88, 50, 24, "bx bx2")
    s.t(165, 104, "VCO", "ts")
    s.line(140, 100, 120, 100, "ln")
    s.line(120, 100, 120, 47, "ln", ar=True)
    s.line(120, 100, 120, 153, "ln", ar=True)
    s.t(126, 76, "π/2 sul ramo Q", "ts a2", "start")
    s.t(330, 126, "e = e_1 e_2", "ts", "start")
    return s.render(), "🧩 Il prodotto e_1 e_2 ∝ m² sin 2Δ non dipende dal segno dei simboli."


# --------------------------------------------------------------------------------------------- Lezione 14

def fig_isi_impulsi():
    s = Svg(400, 180, "impulsi che si sovrappongono: interferenza intersimbolica")
    oy, k, H = 110, 52, 70
    s.line(15, oy, 392, oy, "ax", ar=True)
    simboli = [1, -1, 1, 1]
    cl = ["cv", "cv2", "cv3", "cv"]
    ts = np.linspace(-1.6, 7.4, 400)
    for n, (a, c) in enumerate(zip(simboli, cl)):
        sp = lambda t: a * math.exp(-((t - n - 0.35) ** 2) / 0.55)  # impulso allargato dal canale
        s.poly([(40 + k * t, oy - H * sp(t)) for t in ts], c)
    tot = lambda t: sum(a * math.exp(-((t - n - 0.35) ** 2) / 0.55) for n, a in enumerate(simboli))
    for n in range(4):
        x = 40 + k * (n + 0.35)
        s.line(x, oy + 30, x, oy - H - 10, "gd")
        s.circ(x, oy - H * tot(n + 0.35), 4, "pt cv2")
    s.t(40 + k * 1.35, oy + 44, "istanti di campionamento", "ts")
    return s.render(), "🧩 Le code dei vicini si sommano al campione del simbolo che si decide."


def fig_ber_floor():
    s = Svg(400, 230, "perdita di SNR e BER floor")
    ox, oy, W, H = 50, 200, 330, 180
    x = lambda db: ox + W * db / 16
    y = lambda p: oy - H * (-math.log10(p)) / 6
    s.line(ox - 4, oy, ox + W + 8, oy, "ax", ar=True)
    s.line(ox, oy + 4, ox, oy - H - 10, "ax", ar=True)
    for e in range(1, 7):
        s.line(ox, y(10 ** -e), ox + W, y(10 ** -e), "gd")
        s.t(ox - 6, y(10 ** -e) + 4, f"10^{{−{e}}}", "ts", "end")
    dbs = np.linspace(0, 16, 300)
    ber = lambda d: 0.5 * math.erfc(math.sqrt(10 ** (d / 10)))
    s.poly([(x(d), y(ber(d))) for d in dbs if ber(d) > 1e-6], "cv")
    s.poly([(x(d), y(ber(d - 2))) for d in dbs if d >= 2 and ber(d - 2) > 1e-6], "cv2")
    s.poly([(x(d), y(ber(d - 1) + 3e-4)) for d in dbs if d >= 1], "cv3")
    for db in (0, 4, 8, 12, 16):
        s.t(x(db), oy + 15, str(db), "ts")
    s.t(ox + W + 8, oy + 30, "E_b/N_0 [dB]", "ts", "end")
    s.t(x(9.8), y(2e-6), "teorica", "ts a1", "start")
    s.t(x(12.2), y(2e-5), "perdita di SNR", "ts a2", "start")
    s.t(x(15.8), y(3e-4) - 8, "BER floor (ISI)", "ts a3", "end")
    return s.render(), "🧩 La perdita di SNR sposta la curva; l'ISI la ferma su un pavimento."


def fig_sistema_bandlimitato():
    s = Svg(400, 130, "modello del sistema su canale a banda limitata")
    y = 60
    blocchi = [(30, "g(t)"), (110, "h(t)"), (220, "c(t)")]
    s.t(14, y + 4, "s(n)", "ts a1", "middle")
    s.line(26, y, 40, y, "ln", ar=True)
    for x0, lab in blocchi:
        s.rect(x0 + 10, y - 16, 56, 32, "bx bx1")
        s.t(x0 + 38, y + 4, lab, "ts")
    s.line(96, y, 120, y, "ln", ar=True)
    s.line(176, y, 191, y, "ln", ar=True)
    s.circ(200, y, 9)
    s.t(200, y + 4, "+", "ts")
    s.line(200, y + 36, 200, y + 9, "ln", ar=True)
    s.t(200, y + 50, "rumore", "ts")
    s.line(209, y, 230, y, "ln", ar=True)
    s.line(286, y, 300, y, "ln")
    s.line(300, y, 318, y - 10, "ln")
    s.t(312, y - 18, "kT", "ts a2")
    s.line(320, y, 336, y, "ln", ar=True)
    s.rect(336, y - 16, 56, 32, "bx bx2")
    s.t(364, y + 4, "decisore", "ts")
    s.t(150, 22, "p(t) = g ∗ h ∗ c", "tx a1")
    return s.render(), "🧩 L'impulso che conta è la cascata dei tre filtri."


def _rc(f, a, T=1.0):
    f = abs(f)
    f1, f2 = (1 - a) / (2 * T), (1 + a) / (2 * T)
    if f <= f1:
        return T
    if f >= f2:
        return 0.0
    return T / 2 * (1 - math.sin((f - 1 / (2 * T)) * math.pi * T / a))


def fig_nyquist_repliche():
    s = Svg(400, 170, "repliche dello spettro che sommano a T")
    oy, k, H = 130, 110, 80
    s.line(15, oy, 392, oy, "ax", ar=True)
    fs = np.linspace(-1.7, 1.7, 400)
    for m, cl in ((-1, "cv3"), (0, "cv"), (1, "cv2")):
        s.poly([(200 + k * f, oy - H * _rc(f - m, 0.5)) for f in fs], cl)
    s.line(200 + k * -1.7, oy - H, 200 + k * 1.7, oy - H, "gd")
    s.t(390, oy - H - 6, "somma = T", "ts a1", "end")
    for f, lab in ((-1, "−1/T"), (0, "0"), (1, "1/T"), (0.5, "1/2T")):
        s.t(200 + k * f, oy + 15, lab, "ts")
    return s.render(), "🧩 Coseno rialzato: ogni replica riempie ciò che la vicina lascia."


def fig_nyquist_bande():
    s = Svg(400, 300, "banda passante, banda monolatera e bilatera dell'impulso di Nyquist ideale")
    cx, k = 200, 90
    oy1, H = 100, 56
    s.t(10, 14, "spettro: passa-basso ideale", "tx tb", "start")
    s.line(20, oy1, 388, oy1, "ax", ar=True)
    s.t(386, oy1 + 15, "f", "ts", "end")
    pts = [(cx - k, oy1), (cx - k, oy1 - H), (cx + k, oy1 - H), (cx + k, oy1)]
    s.poly(pts, "fl", True)
    s.poly([(20, oy1)] + pts + [(380, oy1)], "cv")
    s.t(cx, oy1 - H - 8, "|P(f)|", "ts a1")
    s.t(cx, oy1 - H / 2 + 4, "banda passante", "ts a1")
    s.t(cx - k - 6, oy1 - H + 4, "1/(2W_N) = T", "ts", "end")
    for x, lab in ((cx - k, "−W_N"), (cx, "0"), (cx + k, "W_N")):
        s.line(x, oy1 - 3, x, oy1 + 3, "ax")
        s.t(x, oy1 + 15, lab, "ts")
    s.line(cx, oy1 + 28, cx + k, oy1 + 28, "ar2", ar=True, ar0=True)
    s.t(cx - 8, oy1 + 32, "monolatera: W_N = R_s/2", "ts a1", "end")
    s.line(cx - k, oy1 + 46, cx + k, oy1 + 46, "ar2", ar=True, ar0=True)
    s.t(cx, oy1 + 62, "bilatera: 2W_N = 1/T = R_s", "ts a1")

    oy2, H2, kt = 262, 56, 36
    s.t(10, 186, "impulso: p(t) = sinc(t/T)", "tx tb", "start")
    s.line(20, oy2, 388, oy2, "ax", ar=True)
    s.t(386, oy2 + 17, "t", "ts", "end")
    ts = np.linspace(-5, 5, 500)
    s.poly([(cx + kt * t, oy2 - H2 * float(np.sinc(t))) for t in ts], "cv2")
    s.t(cx + 8, oy2 - H2 - 2, "1", "ts", "start")
    for n in range(-4, 5):
        if n:
            s.line(cx + kt * n, oy2 - 3, cx + kt * n, oy2 + 3, "ax")
    for n, lab in ((-2, "−2T"), (-1, "−T"), (1, "T"), (2, "2T")):
        s.t(cx + kt * n, oy2 + 18, lab, "ts")
    s.t(388, 200, "zeri ogni T = 1/(2W_N)", "ts a2", "end")
    return s.render(), ("🧩 «Banda passante» qui è l'intervallo di frequenze che il filtro lascia passare, $\\lvert f\\rvert<W_N$, "
                        "dove $\\lvert P(f)\\rvert=1/(2W_N)=T$: non c'entra il segnale passa-banda. "
                        "La banda monolatera conta solo le frequenze positive, $W_N=R_s/2$; la bilatera anche le negative, $2W_N=R_s$. "
                        "Più la banda è stretta, più la sinc è larga: i suoi zeri cadono ogni $T=1/(2W_N)$.")


def fig_sinc_treno():
    s = Svg(400, 180, "treno di sinc per la sequenza 1011010")
    oy, k, H = 95, 46, 55
    bits = [1, 0, 1, 1, 0, 1, 0]
    s.line(15, oy, 392, oy, "ax", ar=True)
    ts = np.linspace(-1.2, 7.2, 500)
    tot = lambda t: sum((2 * b - 1) * float(np.sinc(t - n)) for n, b in enumerate(bits))
    for n, b in enumerate(bits):
        s.poly([(40 + k * t, oy - H * (2 * b - 1) * float(np.sinc(t - n))) for t in ts], "cv3")
    s.poly([(40 + k * t, oy - H * tot(t)) for t in ts], "cv")
    for n, b in enumerate(bits):
        s.circ(40 + k * n, oy - H * (2 * b - 1), 4, "pt cv2")
        s.t(40 + k * n, 168, str(b), "ts a2")
    return s.render(), "🧩 Negli istanti kT pesa solo il proprio impulso: ISI nulla."


def fig_coseno_rialzato():
    s = Svg(400, 170, "spettro a coseno rialzato")
    oy, k, H = 135, 150, 95
    s.line(15, oy, 392, oy, "ax", ar=True)
    fs = np.linspace(-1.2, 1.2, 400)
    for a, cl in ((0.0, "cv"), (0.5, "cv2"), (1.0, "cv3")):
        if a == 0:
            pts = [(200 + k * -1.2, oy), (200 + k * -0.5, oy), (200 + k * -0.5, oy - H), (200 + k * 0.5, oy - H), (200 + k * 0.5, oy), (200 + k * 1.2, oy)]
        else:
            pts = [(200 + k * f, oy - H * _rc(f, a)) for f in fs]
        s.poly(pts, cl)
    for f, lab in ((-1, "−1/T"), (-0.5, "−1/2T"), (0.5, "1/2T"), (1, "1/T")):
        s.t(200 + k * f, oy + 15, lab, "ts")
    s.t(24, 22, "α = 0", "ts a1", "start")
    s.t(24, 38, "α = 0.5", "ts a2", "start")
    s.t(24, 54, "α = 1", "ts a3", "start")
    return s.render(), "🧩 Banda (1 + α)/(2T); tutte valgono T/2 in 1/(2T)."


def fig_rc_impulso():
    s = Svg(400, 170, "impulso a coseno rialzato")
    oy, k, H = 120, 40, 95
    s.line(15, oy, 392, oy, "ax", ar=True)
    ts = np.linspace(-4.5, 4.5, 500)

    def p(t, a):
        den = 1 - (2 * a * t) ** 2
        if abs(den) < 1e-6:
            return math.pi / 4 * float(np.sinc(1 / (2 * a)))
        return float(np.sinc(t)) * math.cos(math.pi * a * t) / den

    for a, cl in ((0.0, "cv"), (0.5, "cv2"), (1.0, "cv3")):
        s.poly([(200 + k * t, oy - H * p(t, a)) for t in ts], cl)
    for n in range(-4, 5):
        s.line(200 + k * n, oy + 4, 200 + k * n, oy - 4, "ax")
        if n:
            s.t(200 + k * n, oy + 16, f"{n}T", "ts")
    return s.render(), "🧩 Stessi zeri in kT; con α grande le code quasi spariscono."


def fig_equalizzatori():
    s = Svg(400, 170, "tipi di equalizzatori")
    s.rect(150, 10, 100, 26, "bx bx2")
    s.t(200, 28, "equalizzatori", "ts tb")
    for x, lab in ((100, "lineari"), (300, "non lineari")):
        s.line(200, 36, x, 60, "ln", ar=True)
        s.rect(x - 50, 60, 100, 26, "bx bx1")
        s.t(x, 78, lab, "ts")
    for x, lab in ((60, "ZF"), (140, "MMSE")):
        s.line(100, 86, x, 110, "ln", ar=True)
        s.rect(x - 32, 110, 64, 26, "bx")
        s.t(x, 128, lab, "ts")
    for x, lab in ((255, "DFE"), (345, "MLSE")):
        s.line(300, 86, x, 110, "ln", ar=True)
        s.rect(x - 32, 110, 64, 26, "bx")
        s.t(x, 128, lab, "ts")
    s.t(100, 156, "semplici, amplificano il rumore", "ts a2")
    s.t(300, 156, "DFE: propagazione errori · MLSE: ottima", "ts a2")
    return s.render(), "🧩 Dal più semplice all'ottimo."


def fig_traliccio_viterbi():
    s = Svg(400, 200, "traliccio a due stati e sopravvissuti di Viterbi")
    X = [50, 150, 250, 350]
    Y = {"A": 60, "B": 150}
    rami = [(0, "A", "A", 1), (0, "A", "B", 3),
            (1, "A", "A", 2), (1, "A", "B", 1), (1, "B", "A", 1), (1, "B", "B", 3),
            (2, "A", "A", 3), (2, "B", "A", 1)]
    sopr = {(0, "A", "A"), (1, "A", "B"), (2, "B", "A"), (0, "A", "B"), (1, "A", "A")}
    finale = {(0, "A", "A"), (1, "A", "B"), (2, "B", "A")}
    for k, a, b, m in rami:
        cl = "cv" if (k, a, b) in finale else ("cv2" if (k, a, b) in sopr else "gd")
        x1, y1, x2, y2 = X[k], Y[a], X[k + 1], Y[b]
        s.line(x1, y1, x2, y2, cl)
        s.t((x1 + x2) / 2 + (0 if a == b else 8), (y1 + y2) / 2 - 5, str(m), "ts")
    G = {(0, "A"): 0, (1, "A"): 1, (1, "B"): 3, (2, "A"): 3, (2, "B"): 2, (3, "A"): 3}
    for (k, st), g in G.items():
        s.circ(X[k], Y[st], 6, "pt cv")
        s.t(X[k], Y[st] + 22, f"Γ={g}", "ts a1")
    s.t(20, Y["A"] + 4, "A", "tx", "end")
    s.t(20, Y["B"] + 4, "B", "tx", "end")
    for k in range(4):
        s.t(X[k], 22, f"k={k}", "ts")
    return s.render(), "🧩 Esempio del wiki: in blu il cammino minimo A→A→B→A, metrica 3."


def tutte():
    f = {k[4:]: v for k, v in globals().items() if k.startswith("fig_")}
    return {k: fn() for k, fn in f.items()}
