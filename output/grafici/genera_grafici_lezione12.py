"""Grafici della Lezione 12 (parametri globali e capacità).

  grafico-l12-ber-limite-shannon.png  probabilità d'errore sul bit della segnalazione ortogonale M-aria
                                      coerente in funzione di Eb/N0, per M crescente: le curve si
                                      avvicinano alla verticale di Shannon ln2 = -1.59 dB
                                      (ricostruzione dello schizzo negli appunti di Confronto new.pdf p. 23)

Formula usata (segnalazione ortogonale coerente, M segnali equiprobabili di energia Es = Eb log2 M):
  uscite dei correlatori normalizzate a varianza 1: quello giusto ha media sqrt(2 Es/N0), gli altri M-1 media 0;
  P_c = int phi(y - sqrt(2 Es/N0)) Phi(y)^(M-1) dy,   P_e = 1 - P_c,   P_b = M / (2 (M-1)) * P_e.
Per M = 2 si ritrova P_b = Q(sqrt(Eb/N0)).

Uso: python genera_grafici_lezione12.py  (richiede numpy, scipy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import log_ndtr
from scipy.stats import norm

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ACQUA, ROSSO, VIOLA = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#7c5cc4"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": True, "grid.color": GRID, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})


def pb_ortogonale(ebn0_db, k):
    """P_b della segnalazione ortogonale coerente con M = 2**k segnali."""
    M = 2 ** k
    y = np.linspace(-12, 40, 20001)
    dy = y[1] - y[0]
    out = []
    for g in 10 ** (np.asarray(ebn0_db) / 10):
        mu = np.sqrt(2 * k * g)                       # sqrt(2 Es/N0), Es = k Eb
        # 1 - Phi(y)^(M-1), calcolato con log per non perdere precisione quando è piccolo
        uno_meno = -np.expm1((M - 1) * log_ndtr(y))
        pe = np.sum(norm.pdf(y - mu) * uno_meno) * dy
        out.append(M / (2 * (M - 1)) * pe)
    return np.array(out)


def ber_limite_shannon():
    lim = 10 * np.log10(np.log(2))                    # -1.59 dB
    x = np.linspace(-3, 14, 300)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.axvspan(-3, lim, color=ROSSO, alpha=0.08, lw=0)
    ax.text(-2.3, 2e-5, "impossibile", color=ROSSO, fontsize=9, rotation=90, va="center", ha="center")
    curve = [(1, BLU), (2, ACQUA), (4, ARANCIO), (6, VIOLA), (10, INK_2), (16, INK)]
    for k, c in curve:
        pb = pb_ortogonale(x, k)
        ax.semilogy(x, pb, color=c, label=f"$M = {2 ** k}$" if k < 10 else f"$M = 2^{{{k}}}$")
    # limite M -> infinito: P_b = 1/2 sotto ln 2, 0 sopra (gradino sulla verticale di Shannon)
    ax.plot([-3, lim, lim], [0.5, 0.5, 1e-7], color=ROSSO, lw=2.2, ls="--", label=r"$M\to\infty$")
    ax.text(lim + 0.2, 2e-3, "limite di\nShannon\n−1.59 dB\n= ln 2", color=ROSSO, fontsize=9, va="center")
    ax.annotate("M cresce", xy=(5.2, 1e-5), xytext=(10.2, 1e-5), color=INK_2, fontsize=9, va="center",
                arrowprops=dict(arrowstyle="->", color=INK_2, lw=1.2))
    ax.set_xlim(-3, 14), ax.set_ylim(1e-7, 0.8)
    ax.set_xlabel("$E_b/N_0$  [dB]")
    ax.set_ylabel("probabilità d'errore sul bit  $P_b(e)$")
    ax.set_title("Segnalazione ortogonale coerente: al crescere di M le curve si avvicinano a −1.59 dB")
    ax.legend(loc="lower left", bbox_to_anchor=(0.16, 0.0), fontsize=9)
    fig.savefig(OUT / "grafico-l12-ber-limite-shannon.png")
    plt.close(fig)


if __name__ == "__main__":
    # verifica: per M = 2 deve valere P_b = Q(sqrt(Eb/N0))
    g = np.array([0.0, 6.0, 10.0])
    assert np.allclose(pb_ortogonale(g, 1), norm.sf(np.sqrt(10 ** (g / 10))), rtol=1e-4)
    ber_limite_shannon()
    print("ok")
