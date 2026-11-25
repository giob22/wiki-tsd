"""Grafici della pagina wiki/mie-considerazioni.md (ragionamenti personali, non delle slide).

  grafico-cons-verosimiglianza-media.png  il ricevuto y è fisso; ogni ipotesi H_k è una gaussiana centrata
                                          in s_k (stessa varianza); la verosimiglianza f(y|H_k) è l'altezza
                                          della campana nel punto y. H_0 (solo rumore, media 0) è il
                                          denominatore comune del rapporto Lambda_k = f(y|H_k)/f(y|H_0).

Caso reale monodimensionale: s_1 = -1, s_2 = +1, sigma = 0.5, y = 0.7.

Uso: python genera_grafici_considerazioni.py  (richiede numpy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO = "#2a78d6", "#eb6834"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": False, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})

SIGMA, Y = 0.5, 0.7
IPOTESI = [  # (media, colore, stile, etichetta)
    (-1.0, BLU, "-", r"$H_1$: trasmesso $s_1=-1$"),
    (0.0, INK_2, "--", r"$H_0$: solo rumore, media 0"),
    (1.0, ARANCIO, "-", r"$H_2$: trasmesso $s_2=+1$"),
]


def gauss(x, m):
    return np.exp(-(x - m) ** 2 / (2 * SIGMA ** 2)) / np.sqrt(2 * np.pi * SIGMA ** 2)


def verosimiglianza_media():
    x = np.linspace(-3, 3, 1201)
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    alt = {}
    for m, c, ls, lab in IPOTESI:
        ax.plot(x, gauss(x, m), color=c, ls=ls, lw=2 if ls == "-" else 1.6, label=lab)
        ax.plot([m, m], [0, gauss(m, m)], color=c, lw=0.8, ls=":")
        ax.text(m, -0.07, {-1.0: "$s_1$", 0.0: "0", 1.0: "$s_2$"}[m], color=c, ha="center", va="top", fontsize=10)
        alt[m] = gauss(Y, m)
        ax.plot(Y, alt[m], "o", color=c, ms=6, zorder=5)
    # il ricevuto: una sola verticale, uguale per tutte le ipotesi
    ax.axvline(Y, color=INK, lw=1.4)
    ax.text(Y - 0.06, 0.97, "$y$ ricevuto (fisso)", color=INK, fontsize=10, va="top", ha="right")
    # altezze nel punto y
    ax.annotate(rf"$f(y\mid H_2)={alt[1.0]:.2f}$", xy=(Y, alt[1.0]), xytext=(1.55, 0.70), color=ARANCIO, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=ARANCIO, lw=1))
    ax.annotate(rf"$f(y\mid H_0)={alt[0.0]:.2f}$", xy=(Y, alt[0.0]), xytext=(1.55, 0.44), color=INK_2, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=INK_2, lw=1))
    ax.annotate(rf"$f(y\mid H_1)\approx{alt[-1.0]:.3f}$", xy=(Y, alt[-1.0]), xytext=(1.55, 0.18), color=BLU, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=BLU, lw=1))
    # rapporti di verosimiglianza
    l2, l1 = alt[1.0] / alt[0.0], alt[-1.0] / alt[0.0]
    fig.text(0.5, 0.06,
             rf"$\Lambda_2=f(y\mid H_2)\,/\,f(y\mid H_0)\approx{l2:.1f}$      "
             rf"$\Lambda_1=f(y\mid H_1)\,/\,f(y\mid H_0)\approx{l1:.3f}$" "\n"
             r"$H_0$ non è un candidato: è lo stesso denominatore per tutti.  Si decide $H_2$, la media più vicina a $y$.",
             fontsize=10, ha="center", va="top", linespacing=1.7)
    # distanze tra y e le medie candidate
    for m, c, dy in ((1.0, ARANCIO, -0.16), (-1.0, BLU, -0.23)):
        ax.annotate("", xy=(m, dy), xytext=(Y, dy), arrowprops=dict(arrowstyle="<->", color=c, lw=1.1),
                    annotation_clip=False)
        ax.text((m + Y) / 2, dy - 0.015, f"{abs(Y - m):.1f}", color=c, ha="center", va="top", fontsize=9)
    ax.set_xlim(-3, 3), ax.set_ylim(-0.3, 1.0)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.spines["bottom"].set_position(("data", 0))
    ax.set_xticks([])
    ax.spines["left"].set_bounds(0, 0.9)
    ax.text(3.0, 0.02, "valore del ricevuto", color=INK_2, fontsize=9, ha="right", va="bottom")
    ax.text(-1.85, -0.20, "distanza di $y$\ndalle medie", color=INK_2, fontsize=9, ha="right", va="center")
    ax.set_ylabel(r"densità $f(y\mid H_k)$")
    ax.yaxis.set_label_coords(-0.06, 0.6)
    ax.set_title("Il ricevuto $y$ è fisso: cambia solo la media della gaussiana, cioè l'ipotesi")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0), fontsize=9)
    fig.savefig(OUT / "grafico-cons-verosimiglianza-media.png")
    plt.close(fig)
    return l1, l2


if __name__ == "__main__":
    l1, l2 = verosimiglianza_media()
    # verifica: il rapporto coincide con exp[(1/sigma^2)(y s - s^2/2)] (caso reale)
    for s, l in ((1.0, l2), (-1.0, l1)):
        assert np.isclose(l, np.exp((Y * s - s ** 2 / 2) / SIGMA ** 2))
    print("ok", round(l1, 4), round(l2, 3))
