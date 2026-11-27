"""Grafici delle pagine di approfondimento (wiki/approfondimenti/, materiale non d'esame).

  grafico-gelli-water-filling.png   water filling delle note di Gelli (eq. 118-121): profilo n_i = Gamma sigma_i^2/|H_i|^2
                                    di 8 sottoportanti, livello dell'acqua K, energie E_i = max(K - n_i, 0) e bit b_i

Esempio: canale a due prese h = [1, 0.6], N = 8 (|H_i|^2 = 1.36 + 1.2 cos(2 pi i/8)), Gamma sigma^2 = 0.25, energia totale E = 2.
Uso: python genera_grafici_approfondimenti.py  (richiede numpy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ROSSO = "#2a78d6", "#eb6834", "#e34948"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": False, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})


def water_filling(n, E):
    """K e E_i della (119): si toglie la sottoportante peggiore finché tutte le attive hanno E_i >= 0."""
    attive = np.ones(len(n), bool)
    while True:
        K = (E + n[attive].sum()) / attive.sum()          # (120) ristretta alle attive
        Ei = np.where(attive, K - n, 0.0)
        if (Ei >= -1e-12).all():
            return K, np.maximum(Ei, 0)
        attive &= Ei > 0


def grafico(N=8, alfa=0.6, gs2=0.25, E=2.0):
    i = np.arange(N)
    H2 = abs(1 + alfa * np.exp(-2j * np.pi * i / N)) ** 2
    n = gs2 / H2
    K, Ei = water_filling(n, E)
    bi = np.log2(1 + Ei / n)                                # (112)/(116) con E_i |H_i|^2/(Gamma sigma^2) = E_i/n_i
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    ax.bar(i, n, width=0.92, color="#d9d6cc", edgecolor=INK_2, label=r"fondo $\Gamma\sigma_i^2/|H_i|^2$")
    ax.bar(i, Ei, bottom=n, width=0.92, color=BLU, alpha=.55, label=r"acqua = energia $\mathcal{E}_i$")
    ax.axhline(K, color=BLU, lw=1.6, ls="--")
    ax.text(-0.45, K - 0.03, f"livello K = {K:.2f}", color=BLU, ha="left", va="top", fontsize=9)
    for k in i:
        ax.text(k, max(K, n[k]) + 0.10, f"{bi[k]:.1f} bit" if Ei[k] > 0 else "0 bit\n(spenta)", ha="center", va="bottom",
                fontsize=8.5, color=ROSSO if Ei[k] == 0 else INK)
    ax.set_xticks(i), ax.set_xlabel("sottoportante $i$")
    ax.set_ylabel("energia (unità arbitrarie)")
    ax.set_ylim(0, max(n.max(), K) * 1.35)
    ax.set_title("Water filling: si versa l'energia E sul profilo del canale")
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(OUT / "grafico-gelli-water-filling.png")
    plt.close(fig)
    return K, Ei, bi, n


if __name__ == "__main__":
    K, Ei, bi, n = grafico()
    assert np.isclose(Ei.sum(), 2.0)                       # vincolo (117)
    assert np.allclose((Ei + n)[Ei > 0], K)                # (118) sulle attive
    assert (n[Ei == 0] >= K - 1e-12).all()                 # le spente hanno il fondo sopra il livello
    print("ok K =", round(K, 3), "bit totali =", round(bi.sum(), 2), "spente:", list(np.where(Ei == 0)[0]))
