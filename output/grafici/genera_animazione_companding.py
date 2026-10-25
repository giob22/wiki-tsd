"""Animazione del companding con la legge µ (Campionamento_AD_DA.pdf, p. 36-43).

Al variare di µ (da quasi 0, cioè quasi uniforme, fino a 255 dello standard G.711):
- in alto a sinistra: la legge di compressione F(x); le soglie uniformi sull'asse compresso y
  (righe orizzontali) diventano, attraverso F^{-1}, soglie non uniformi sull'asse x (righe verticali);
- in alto a destra: la caratteristica complessiva Q(x) = F^{-1}(Q_u(F(x))), confrontata con l'uniforme;
- in basso: SNR in funzione del livello del segnale (Laplace), con b = 8 bit: al crescere di µ la curva
  si appiattisce (quantizzazione robusta) a prezzo di qualche dB a pieno carico.
Per leggibilità la figura in alto usa M = 16 livelli; l'SNR usa b = 8 bit (M = 256).
Uso: python genera_animazione_companding.py  (richiede numpy, matplotlib, pillow)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ACQUA, ROSSO = "#2a78d6", "#eb6834", "#1baf7a", "#e34948"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 100,
})

XMAX = 1.0
M_FIG = 16
B_SNR = 8


def F(x, mu):
    return np.sign(x) * XMAX * np.log1p(mu * np.abs(x) / XMAX) / np.log1p(mu)


def Finv(y, mu):
    return np.sign(y) * XMAX / mu * np.expm1(np.abs(y) / XMAX * np.log1p(mu))


def Qu(y, M):
    D = 2 * XMAX / M
    return np.clip(np.floor(y / D) * D + D / 2, -XMAX + D / 2, XMAX - D / 2)


def Q(x, mu, M):
    return Finv(Qu(F(np.clip(x, -XMAX, XMAX), mu), M), mu)


rng = np.random.default_rng(0)
base = rng.laplace(0, 1 / np.sqrt(2), 40_000)          # Laplace con x_rms = 1
livelli_db = np.linspace(-50, 0, 26)                   # x_rms / X_max in dB


def snr_curve(mu, M):
    out = []
    for L in livelli_db:
        x = base * XMAX * 10 ** (L / 20)
        e = Q(x, mu, M) - x
        out.append(10 * np.log10(np.mean(x**2) / np.mean(e**2)))
    return np.array(out)


mus = np.concatenate([np.geomspace(0.05, 255, 44), np.full(10, 255.0)])
snr_unif = snr_curve(1e-6, 2**B_SNR)
snr_255 = snr_curve(255, 2**B_SNR)


def main():
    fig = plt.figure(figsize=(11, 8))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1], hspace=0.38, wspace=0.25)
    ax_f, ax_q, ax_s = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])
    xx = np.linspace(-1, 1, 3000)
    D = 2 * XMAX / M_FIG
    y_soglie = -XMAX + D * np.arange(1, M_FIG)

    def frame(k):
        mu = mus[k]
        for a in (ax_f, ax_q, ax_s):
            a.clear()
        # 1) legge di compressione e soglie
        x_soglie = Finv(y_soglie, mu)
        for ys, xs in zip(y_soglie, x_soglie):
            ax_f.plot([-1, xs], [ys, ys], color=ACQUA, lw=0.7, alpha=0.8)
            ax_f.plot([xs, xs], [ys, -1], color=ARANCIO, lw=0.7, alpha=0.8)
        ax_f.plot(xx, F(xx, mu), color=BLU, lw=2.4)
        ax_f.plot(xx, xx, color=INK_2, lw=0.8, ls=":")
        ax_f.set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r"ingresso $x / X_{max}$", ylabel=r"compresso $y = F(x)$",
                 title=rf"Compressore µ-law, $\mu = {mu:.3g}$: celle uguali su $y$ (verde)" "\n"
                       r"diventano celle diverse su $x$ (arancio)")
        # 2) caratteristica complessiva
        ax_q.plot(xx, Qu(xx, M_FIG), color=INK_2, lw=1.2, ls="--", label="uniforme (senza companding)")
        ax_q.plot(xx, Q(xx, mu, M_FIG), color=BLU, lw=2, label=r"$F^{-1}(Q_u(F(x)))$")
        ax_q.plot(xx, xx, color=INK_2, lw=0.6, ls=":")
        ax_q.set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r"$x / X_{max}$", ylabel=r"$Q(x) / X_{max}$",
                 title=f"Quantizzatore complessivo, M = {M_FIG} livelli:\ngradini fitti vicino a 0, larghi ai bordi")
        ax_q.legend(loc="upper left", fontsize=8)
        # 3) SNR in funzione del livello
        s = snr_curve(mu, 2**B_SNR)
        ax_s.plot(livelli_db, snr_unif, color=INK_2, lw=1.2, ls="--", label="uniforme")
        ax_s.plot(livelli_db, snr_255, color=ACQUA, lw=1, ls=":", label="µ = 255 (G.711)")
        ax_s.plot(livelli_db, s, color=ROSSO, lw=2.4, label=rf"µ = {mu:.3g}")
        ax_s.axvline(-12.04, color=INK_2, lw=0.8, ls="-.")
        ax_s.text(-11.6, 50, r"$k_c = 4$", color=INK_2, fontsize=9)
        ax_s.text(-7.5, 40, "sovraccarico", color=INK_2, fontsize=9)
        ax_s.set(xlim=(-50, 0), ylim=(0, 55), xlabel=r"livello del segnale $20\log_{10}(x_{rms}/X_{max})$ [dB]",
                 ylabel="SNR [dB]",
                 title=f"SNR con b = {B_SNR} bit, segnale di Laplace: più µ cresce, più l'SNR diventa indipendente dal livello")
        ax_s.legend(loc="lower right", fontsize=9)

    anim = FuncAnimation(fig, frame, frames=len(mus), interval=150)
    anim.save(OUT / "grafico-companding-animazione.gif", writer=PillowWriter(fps=7))
    plt.close(fig)
    print("scritto grafico-companding-animazione.gif")


if __name__ == "__main__":
    main()
