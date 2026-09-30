"""Grafici di funzione per la lezione "Stochastic processes" (random_processes.pdf).

Nessun grafico riproduce una figura delle slide: sono generati dalle definizioni del PDF
(realizzazioni, autocorrelazione (7), PSD e Wiener-Khinchin (p.27), pdf gaussiana (33)-(34))
come supporto alla comprensione.

Processo d'esempio: gaussiano, media nulla, WSS, con autocorrelazione R(tau) = exp(-|tau|/tau_c)
e quindi PSD S(f) = 2 tau_c / (1 + (2 pi f tau_c)^2). Le realizzazioni si generano in modo esatto
con la ricorsione x[n] = a x[n-1] + sqrt(1 - a^2) w[n], a = exp(-dt/tau_c), w[n] gaussiani indipendenti.
Uso: python genera_grafici_random_processes.py  (richiede numpy, matplotlib, pillow)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

OUT = Path(__file__).parent

# Stessa palette e stile degli altri script
SURFACE = "#fcfcfb"
INK = "#1f1f1e"
INK_2 = "#5f5e57"
GRID = "#e4e3dc"
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]          # blu, arancio, acqua
BLU = LinearSegmentedColormap.from_list("blu", ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.edgecolor": INK_2, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})


def save(fig, name):
    fig.savefig(OUT / name)
    plt.close(fig)
    print("scritto", name)


def realizzazioni(n_real, n_camp, dt, tau_c, seed=0):
    """n_real realizzazioni del processo gaussiano WSS con R(tau) = exp(-|tau|/tau_c), varianza 1."""
    rng = np.random.default_rng(seed)
    a = np.exp(-dt / tau_c)
    x = np.empty((n_real, n_camp))
    x[:, 0] = rng.standard_normal(n_real)                    # partenza gia' stazionaria
    w = rng.standard_normal((n_real, n_camp))
    for n in range(1, n_camp):
        x[:, n] = a * x[:, n - 1] + np.sqrt(1 - a**2) * w[:, n]
    return x


R = lambda tau, tau_c: np.exp(-np.abs(tau) / tau_c)
S = lambda f, tau_c: 2 * tau_c / (1 + (2 * np.pi * f * tau_c) ** 2)


# 1. Le due facce del processo: realizzazioni e variabile aleatoria a t0 (p.3-4)
def realizzazioni_e_va(tau_c=0.5, t0=6.0):
    dt = 0.01
    t = np.arange(0, 10, dt)
    x = realizzazioni(5000, t.size, dt, tau_c, seed=1)
    i0 = int(round(t0 / dt))
    fig = plt.figure(figsize=(10, 5.4))
    gs = fig.add_gridspec(5, 2, width_ratios=[2.3, 1], hspace=0.15, wspace=0.18)
    for r in range(5):
        ax = fig.add_subplot(gs[r, 0])
        ax.plot(t, x[r], color=INK_2, lw=1)
        ax.axvline(t0, color=CAT[1], lw=1, ls="--")
        ax.plot([t0], [x[r, i0]], "o", ms=8, color=CAT[1], mec=SURFACE, mew=2, zorder=5)
        ax.set_ylim(-3.2, 3.2)
        ax.set_yticks([])
        ax.set_ylabel(f"$x_{r + 1}(t)$", rotation=0, labelpad=16, va="center")
        if r < 4:
            ax.set_xticklabels([])
        else:
            ax.set_xlabel("$t$")
        if r == 0:
            ax.set_title("Realizzazioni: una forma d'onda per ogni esito $\\omega_i$", loc="left", fontsize=9.5)
            ax.text(t0 + 0.1, 2.3, "$t_0$", color=CAT[1], fontsize=10)
    ax = fig.add_subplot(gs[:, 1])
    v = np.linspace(-4, 4, 400)
    ax.hist(x[:, i0], bins=50, range=(-4, 4), density=True, orientation="horizontal",
            color=CAT[0], alpha=0.35, edgecolor=SURFACE, lw=0.5, label="istogramma di $X(t_0)$\n(5000 realizzazioni)")
    ax.plot(np.exp(-v**2 / 2) / np.sqrt(2 * np.pi), v, color=INK, lw=1.6, label="pdf gaussiana\n$\\mu = 0$, $\\sigma^2 = 1$")
    ax.set_ylim(-3.2, 3.2)
    ax.set_xlabel("$f_{X(t_0)}(x)$")
    ax.set_ylabel("$x$")
    ax.set_title("Fissato $t_0$: una variabile aleatoria", loc="left", fontsize=9.5)
    ax.legend(loc="upper right", fontsize=8.5)
    save(fig, "grafico-rp-realizzazioni.png")


# 2. Processo lento contro veloce: realizzazioni, autocorrelazione, PSD (p.15-16, p.27)
def lento_vs_veloce(tc_lento=2.0, tc_veloce=0.1, soglia=0.1):
    dt = 0.01
    t = np.arange(0, 10, dt)
    xl = realizzazioni(1, t.size, dt, tc_lento, seed=3)[0]
    xv = realizzazioni(1, t.size, dt, tc_veloce, seed=4)[0]
    tau = np.linspace(-6, 6, 1201)
    f = np.linspace(-2.5, 2.5, 1001)
    fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(8, 8.2), height_ratios=[1.2, 1, 1])
    a1.plot(t, xl + 3, color=CAT[0], lw=1.4, label=rf"lento ($\tau_c = {tc_lento:g}$)")
    a1.plot(t, xv - 3, color=CAT[1], lw=1.0, label=rf"veloce ($\tau_c = {tc_veloce:g}$)")
    a1.set_yticks([])
    a1.set_xlabel("$t$")
    a1.set_title("Una realizzazione di ciascun processo (stessa potenza $R(0) = 1$)", loc="left", fontsize=9.5)
    a1.legend(loc="center", bbox_to_anchor=(0.5, 0.5), ncol=2, fontsize=8.5)
    for tc, c, nome in [(tc_lento, CAT[0], "lento"), (tc_veloce, CAT[1], "veloce")]:
        a2.plot(tau, R(tau, tc), color=c, label=nome)
        td = tc * np.log(1 / soglia)                           # |R| < soglia per tau > td
        a2.plot([td], [soglia], "o", ms=8, color=c, mec=SURFACE, mew=2, zorder=5)
        a2.annotate(rf"$\tau_{{dec}} \approx {td:.2f}$", xy=(td, soglia), xytext=(td + 0.25, soglia + 0.28),
                    fontsize=8.5, color=INK, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
        a3.plot(f, S(f, tc), color=c, label=nome)
    a2.axhline(soglia, color=INK_2, lw=0.9, ls="--")
    a2.text(-5.9, soglia + 0.04, f"valore prescritto ({soglia:g} R(0))", fontsize=8.5, color=INK_2)
    a2.set_xlabel(r"$\tau$")
    a2.set_ylabel(r"$R_{XX}(\tau)$")
    a2.set_title(r"Autocorrelazione $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$: più il processo è veloce, prima decade",
                 loc="left", fontsize=9.5)
    a3.set_xlabel("$f$")
    a3.set_ylabel(r"$S_{XX}(f)$")
    a3.set_title(r"PSD $S_{XX}(f) = \dfrac{2\tau_c}{1 + (2\pi f \tau_c)^2}$ (trasformata di $R_{XX}$): stessa area, "
                 "forme opposte", loc="left", fontsize=9.5)
    a3.legend(loc="upper right", fontsize=8.5)
    fig.tight_layout()
    save(fig, "grafico-rp-lento-veloce.png")


# 3. Animazione: come si costruisce R(tau) mediando sulle realizzazioni (p.8, p.14-15)
def autocorrelazione_animazione(tau_c=1.0, t_fisso=6.0, fps=10, anteprima=None):
    """anteprima = (cartella, [frame, ...]): salva solo quei fotogrammi come PNG, senza la GIF."""
    from matplotlib.animation import FuncAnimation, PillowWriter
    dt = 0.02
    t = np.arange(0, 8, dt)
    x = realizzazioni(600, t.size, dt, tau_c, seed=7)
    i_t = int(round(t_fisso / dt))
    taus = np.round(np.arange(0, 4.01, 0.1), 2)
    seq = [0] * 12 + [k for k in range(len(taus)) for _ in range(2)] + [len(taus) - 1] * 15
    stime = [float(np.mean(x[:, i_t] * x[:, i_t - int(round(tt / dt))])) for tt in taus]
    fig = plt.figure(figsize=(9, 6.4))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.25], hspace=0.42, wspace=0.28,
                          left=0.07, right=0.98, top=0.83, bottom=0.08)
    a1 = fig.add_subplot(gs[0, :])
    a2 = fig.add_subplot(gs[1, 0])
    a3 = fig.add_subplot(gs[1, 1])
    fig.text(0.02, 0.955, r"Autocorrelazione: quanto si somigliano due campioni distanti $\tau$",
             fontsize=12, weight="bold", color=INK)
    fig.text(0.02, 0.915, r"$R_{XX}(\tau) = E[X(t)\,X(t-\tau)]$: media, su tutte le realizzazioni, del prodotto dei due campioni",
             fontsize=9.5, color=INK_2)

    def draw(k):
        tau = taus[k]
        i_s = i_t - int(round(tau / dt))
        a1.clear(); a2.clear(); a3.clear()
        for r, c in zip(range(4), [INK_2, INK_2, INK_2, INK_2]):
            a1.plot(t, x[r], color=c, lw=0.9, alpha=0.8)
        for tt, col, lab in [(t_fisso, CAT[1], "$t$"), (t_fisso - tau, CAT[0], r"$t-\tau$")]:
            a1.axvline(tt, color=col, lw=1.2, ls="--")
            a1.text(tt + 0.05, 2.9, lab, color=col, fontsize=10)
        a1.plot([t_fisso] * 4, x[:4, i_t], "o", ms=7, color=CAT[1], mec=SURFACE, mew=1.5, zorder=5)
        a1.plot([t_fisso - tau] * 4, x[:4, i_s], "o", ms=7, color=CAT[0], mec=SURFACE, mew=1.5, zorder=5)
        a1.set_xlim(0, 8)
        a1.set_ylim(-3.3, 3.5)
        a1.set_yticks([])
        a1.set_xlabel("$t$")
        a1.set_title(rf"4 delle 600 realizzazioni; $\tau = {tau:.1f}$", loc="left", fontsize=9.5)
        a2.plot(x[:, i_t], x[:, i_s], "o", ms=3.5, color=CAT[0], alpha=0.45, mec="none")
        a2.set_xlim(-3.5, 3.5)
        a2.set_ylim(-3.5, 3.5)
        a2.set_aspect("equal")
        a2.set_xlabel("$X(t)$")
        a2.set_ylabel(r"$X(t-\tau)$")
        a2.set_title(rf"coppie di campioni, media del prodotto = {stime[k]:.2f}", loc="left", fontsize=9.5)
        tt_ = np.linspace(0, 4, 300)
        a3.plot(tt_, R(tt_, tau_c), color=GRID, lw=3, label=r"teorica $e^{-\tau/\tau_c}$")
        a3.plot(taus[:k + 1], stime[:k + 1], "o-", ms=5, lw=1.2, color=CAT[1], mec=SURFACE, mew=1, label="stima dalle realizzazioni")
        a3.set_xlim(0, 4)
        a3.set_ylim(-0.2, 1.1)
        a3.set_xlabel(r"$\tau$")
        a3.set_ylabel(r"$R_{XX}(\tau)$")
        a3.set_title("la curva si costruisce punto per punto", loc="left", fontsize=9.5)
        a3.legend(loc="upper right", fontsize=8.5)
        return []

    if anteprima:
        cartella, quali = anteprima
        for k in quali:
            draw(seq[k])
            fig.savefig(f"{cartella}/anteprima-acf-{k:03d}.png", dpi=80, bbox_inches=None)
        plt.close(fig)
        return
    ani = FuncAnimation(fig, lambda i: draw(seq[i]), frames=len(seq), blit=False)
    ani.save(OUT / "grafico-rp-autocorrelazione.gif", writer=PillowWriter(fps=fps), dpi=80)
    plt.close(fig)
    print("scritto grafico-rp-autocorrelazione.gif")


# 4. Due campioni di un processo gaussiano: incorrelati = indipendenti (p.37, p.39)
def gaussiana_bivariata(rho=0.8, n=400):
    v = np.linspace(-3.5, 3.5, 301)
    X1, X2 = np.meshgrid(v, v)
    rng = np.random.default_rng(11)
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.9))
    for ax, r in zip(axs, [0.0, rho]):
        det = 1 - r**2                                        # Sigma = [[1, r], [r, 1]]
        q = (X1**2 - 2 * r * X1 * X2 + X2**2) / det           # (x - mu)^T Sigma^-1 (x - mu)
        pdf = np.exp(-q / 2) / (2 * np.pi * np.sqrt(det))     # eq. (33) con n = 2
        livelli = np.linspace(0.01, pdf.max(), 8)              # sotto 0.01 niente riempimento: sfondo chiaro
        ax.contourf(X1, X2, pdf, levels=livelli, cmap=BLU, alpha=0.9, extend="max")
        ax.contour(X1, X2, pdf, levels=livelli, colors=SURFACE, linewidths=0.6)
        c = rng.multivariate_normal([0, 0], [[1, r], [r, 1]], size=n)
        ax.plot(c[:, 0], c[:, 1], "o", ms=2.5, color=INK, alpha=0.35, mec="none")
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-3.5, 3.5)
        ax.set_aspect("equal")
        ax.set_xlabel("$x_1$  (valore di $X(t_1)$)")
        ax.set_ylabel("$x_2$  (valore di $X(t_2)$)")
    axs[0].set_title(r"$\rho = 0$: $f(x_1, x_2) = f(x_1)\,f(x_2)$, cerchi" + "\nincorrelati e quindi indipendenti, eq. (34)",
                     loc="left", fontsize=9.5)
    axs[1].set_title(rf"$\rho = {rho:g}$: ellissi inclinate" + "\ni due campioni tendono ad avere lo stesso segno",
                     loc="left", fontsize=9.5)
    fig.suptitle("pdf congiunta di due campioni di un processo gaussiano (media nulla, varianza 1), eq. (33)",
                 x=0.02, ha="left", fontsize=10.5)
    fig.tight_layout()
    save(fig, "grafico-rp-gaussiana-bivariata.png")


if __name__ == "__main__":
    realizzazioni_e_va()
    lento_vs_veloce()
    gaussiana_bivariata()
    autocorrelazione_animazione()
