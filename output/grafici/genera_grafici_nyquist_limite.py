"""Animazione: coseno campionato esattamente a f_c = 2 f_0 (caso limite del teorema del campionamento).

x(t) = cos(2 pi f0 t + phi), f0 = pi Hz, campionato a fc = 2 f0 (Tc = 1/(2 pi) s).
I campioni valgono cos(pi n + phi) = (-1)^n cos(phi): la fase non si vede più, conta solo cos(phi).
L'interpolazione ideale (serie di Shannon) restituisce cos(phi) cos(2 pi f0 t), non x(t).
In frequenza: la riga in +f0 (peso e^{j phi}/2) e la replica della riga in -f0 (peso e^{-j phi}/2)
cadono nello stesso punto fc/2 = f0 e si sommano: e^{j phi}/2 + e^{-j phi}/2 = cos(phi).
Uso: python genera_grafici_nyquist_limite.py  (richiede numpy, matplotlib, pillow)
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
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 110,
})

f0 = np.pi                      # Hz
fc = 2 * f0                     # frequenza di Nyquist: esattamente il doppio
Tc = 1 / fc
t = np.linspace(0, 2.5, 1500)
n = np.arange(0, int(2.5 / Tc) + 1)
fasi = np.concatenate([np.linspace(0, np.pi, 60), np.full(8, np.pi)])


def disegna():
    fig = plt.figure(figsize=(10, 7.2))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1], hspace=0.45, wspace=0.3)
    ax_t = fig.add_subplot(gs[0, :])
    ax_f = fig.add_subplot(gs[1, 0])
    ax_a = fig.add_subplot(gs[1, 1])

    def frame(k):
        phi = fasi[k]
        for a in (ax_t, ax_f, ax_a):
            a.clear()
        # tempo
        x = np.cos(2 * np.pi * f0 * t + phi)
        xs = np.cos(2 * np.pi * f0 * n * Tc + phi)
        xr = np.cos(phi) * np.cos(2 * np.pi * f0 * t)        # serie di Shannon sui campioni
        ax_t.plot(t, x, color=INK_2, lw=1.4, label=r"segnale $x(t) = \cos(2\pi f_0 t + \varphi)$")
        ax_t.plot(t, xr, color=BLU, lw=2.2, label=r"ricostruito: $\cos\varphi\,\cos(2\pi f_0 t)$")
        ax_t.vlines(n * Tc, 0, xs, color=ARANCIO, lw=1.2)
        ax_t.plot(n * Tc, xs, "o", color=ARANCIO, ms=5, label=r"campioni $(-1)^n\cos\varphi$")
        ax_t.set(xlim=(0, 2.5), ylim=(-1.25, 1.6), xlabel="t [s]",
                 title=rf"$f_0 = \pi$ Hz campionato a $f_c = 2f_0 = 2\pi$ Hz  ·  "
                       rf"$\varphi = {np.degrees(phi):.0f}°$,  $\cos\varphi = {np.cos(phi):+.2f}$")
        ax_t.legend(loc="upper right", fontsize=8, ncol=3)
        # fasori in f = f0
        ax_f.set_aspect("equal")
        ax_f.axhline(0, color=INK_2, lw=0.8)
        ax_f.axvline(0, color=INK_2, lw=0.8)
        th = np.linspace(0, 2 * np.pi, 200)
        ax_f.plot(0.5 * np.cos(th), 0.5 * np.sin(th), color=GRID, lw=1)
        p1 = 0.5 * np.exp(1j * phi)
        p2 = 0.5 * np.exp(-1j * phi)
        kw = dict(angles="xy", scale_units="xy", scale=1, width=0.012)
        ax_f.quiver(0, 0, p1.real, p1.imag, color=BLU, **kw)
        ax_f.quiver(p1.real, p1.imag, p2.real, p2.imag, color=ACQUA, **kw)
        ax_f.quiver(0, 0, np.cos(phi), 0, color=ROSSO, width=0.02, angles="xy", scale_units="xy", scale=1)
        ax_f.text(-1.05, 0.85, r"$\frac{1}{2}e^{j\varphi}$: riga in $+f_0$", color=BLU, fontsize=9)
        ax_f.text(-1.05, 0.68, r"$\frac{1}{2}e^{-j\varphi}$: replica di $-f_0$", color=ACQUA, fontsize=9)
        ax_f.text(-1.05, -1.0, r"somma $= \cos\varphi$ (reale)", color=ROSSO, fontsize=9)
        ax_f.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), title=r"In $f = f_c/2 = f_0$ le due righe si sommano")
        # ampiezza ricostruita
        ff = np.linspace(0, np.pi, 200)
        ax_a.plot(np.degrees(ff), np.ones_like(ff), color=INK_2, lw=1.2, ls="--", label="ampiezza vera")
        ax_a.plot(np.degrees(ff), np.cos(ff), color=BLU, label=r"ricostruita: $\cos\varphi$")
        ax_a.plot(np.degrees(phi), np.cos(phi), "o", color=ROSSO, ms=8)
        ax_a.set(xlim=(0, 180), ylim=(-1.15, 1.25), xlabel=r"fase $\varphi$ [°]", xticks=[0, 45, 90, 135, 180],
                 title="Ampiezza della ricostruzione")
        ax_a.legend(loc="lower left", fontsize=8)

    anim = FuncAnimation(fig, frame, frames=len(fasi), interval=120)
    anim.save(OUT / "grafico-nyquist-limite-coseno.gif", writer=PillowWriter(fps=8))
    plt.close(fig)
    print("scritto grafico-nyquist-limite-coseno.gif")


if __name__ == "__main__":
    disegna()
