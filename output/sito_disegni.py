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


def tutte():
    f = {k[4:]: v for k, v in globals().items() if k.startswith("fig_")}
    return {k: fn() for k, fn in f.items()}
