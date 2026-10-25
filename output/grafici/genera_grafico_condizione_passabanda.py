"""Grafico: perché un segnale passa-banda richiede f_c > B (Rappresentazione_Rice.pdf, p. 4, eq. (2)).

Quattro spettri con la stessa banda B e portante sempre più bassa:
  (a) f_c = 2B   -> condizione rispettata: i lobi in ±f_c sono lontani dall'origine;
  (b) f_c = B    -> soglia della slide: fascia libera [-B/2, B/2] attorno a 0;
  (c) f_c = B/2  -> caso limite: i lobi si toccano in f = 0;
  (d) f_c = B/4  -> i lobi si sovrappongono e contengono f = 0: non è più un segnale passa-banda.
Uso: python genera_grafico_condizione_passabanda.py  (richiede numpy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ACQUA, ROSSO = "#2a78d6", "#eb6834", "#1baf7a", "#e34948"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": False, "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})

B = 1.0


def lobo(f, centro):
    """Lobo trapezoidale di larghezza B centrato in 'centro' (forma qualsiasi: conta solo il supporto)."""
    u = np.abs(f - centro) / (B / 2)
    return np.clip(1.4 * (1 - u), 0, 1) * (u <= 1)


casi = [
    (2 * B, BLU, r"(a) $f_c = 2B$: $f_c > B$ rispettata", "lobi lontani, $f = 0$ escluso"),
    (B, ACQUA, r"(b) $f_c = B$: soglia della slide", "attorno a $f = 0$ resta libera una fascia larga $B$"),
    (B / 2, ARANCIO, r"(c) $f_c = B/2$: caso limite", "i lobi si toccano in $f = 0$"),
    (B / 4, ROSSO, r"(d) $f_c = B/4$: non è più passa-banda", "lobi sovrapposti attorno a $f = 0$"),
]

fig, ax = plt.subplots(4, 1, figsize=(9, 8.6), sharex=True)
f = np.linspace(-3, 3, 4000)
for a, (fc, col, titolo, nota) in zip(ax, casi):
    pos, neg = lobo(f, fc), lobo(f, -fc)
    a.fill_between(f, pos, color=col, alpha=0.30, lw=0)
    a.fill_between(f, neg, color=col, alpha=0.30, lw=0)
    a.plot(f, pos, color=col)
    a.plot(f, neg, color=col)
    if fc > B / 2:
        a.plot(f, np.zeros_like(f), color=INK_2, lw=0.8)
    else:
        a.plot(f, pos + neg, color=INK, lw=1.2, ls="--", label="somma dei due lobi")
        a.legend(loc="upper right", fontsize=8)
    a.axvline(0, color=INK_2, lw=0.8)
    for c in (fc, -fc):
        a.plot([c, c], [-0.04, 0.04], color=INK, lw=1)
    a.text(fc, -0.17, r"$f_c$", ha="center", fontsize=9)
    a.text(-fc, -0.17, r"$-f_c$", ha="center", fontsize=9)
    # bordo inferiore del lobo positivo
    lo = fc - B / 2
    a.annotate("", xy=(fc - B / 2, 1.12), xytext=(fc + B / 2, 1.12),
               arrowprops=dict(arrowstyle="<->", color=INK_2, lw=1))
    a.text(fc, 1.17, r"$B$", ha="center", fontsize=9, color=INK_2)
    a.plot([lo, lo], [0, 1.05], color=col, lw=1, ls=":")
    a.text(lo + 0.04 if lo >= 0 else lo - 0.04, 0.55, rf"$f_c - B/2 = {lo:.2g}B$", fontsize=9, color=col,
           ha="left" if lo >= 0 else "right")
    a.set(ylim=(-0.25, max(1.35, (pos + neg).max() + 0.1)), yticks=[], title=f"{titolo} — {nota}")
    a.title.set_fontsize(10)
ax[-1].set_xlabel(r"$f\ /\ B$")
fig.suptitle(r"Perché si chiede $f_c > B$: il bordo inferiore del lobo positivo è $f_c - B/2$", fontsize=11, y=0.995)
fig.tight_layout()
fig.savefig(OUT / "grafico-rice-condizione-passabanda.png")
print("scritto grafico-rice-condizione-passabanda.png")
