"""Grafici per upconversion e downconversion (Rappresentazione_Rice.pdf, slide 14, eq. (17) e (21)).

Nessun grafico riproduce una figura delle slide: sono generati dalle formule del PDF.
  1. upconversion nel tempo: s_c e s_s moltiplicati per le portanti, somma = s_p (eq. (17));
  2. downconversion nel tempo: i due rami, con il termine a 2 f_c che il passa-basso toglie (eq. (21));
  3. upconversion e downconversion in frequenza, con un lobo asimmetrico (come la slide 11);
  4. dove mettere la frequenza di taglio del passa-basso: W <= f_LP <= 2 f_c - W.
Esempio nel tempo: f_c = 10 kHz, s_c = cos(2 pi 1 kHz t) + 0.5 cos(2 pi 2 kHz t), s_s = 0.8 sin(2 pi 1.5 kHz t)
(stesso esempio di genera_grafici_rappresentazione_rice.py). Tempi in ms, frequenze in kHz.
Uso: python genera_grafici_upconversion.py  (richiede numpy, matplotlib)
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
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 1.6, "font.size": 10, "legend.frameon": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

FC = 10.0
R2 = np.sqrt(2)
sc = lambda t: np.cos(2 * np.pi * 1.0 * t) + 0.5 * np.cos(2 * np.pi * 2.0 * t)
ss = lambda t: 0.8 * np.sin(2 * np.pi * 1.5 * t)
carr_c = lambda t: R2 * np.cos(2 * np.pi * FC * t)
carr_s = lambda t: -R2 * np.sin(2 * np.pi * FC * t)
sp = lambda t: sc(t) * carr_c(t) + ss(t) * carr_s(t)          # eq. (17)

T_MOSTRA = 2.0                                              # ms mostrati (un periodo di s_c e s_s)
t = np.linspace(0, T_MOSTRA, 4000)


def save(fig, name):
    fig.savefig(OUT / name)
    plt.close(fig)
    print("scritto", name)


# ---------------------------------------------------------------- 1. upconversion nel tempo
def upconversion_tempo():
    fig, ax = plt.subplots(3, 1, figsize=(9, 8.2), sharex=True)
    a = ax[0]
    a.plot(t, sc(t), color=BLU, lw=2.2, label=r"$s_c(t)$ (ingresso del ramo I)")
    a.plot(t, sc(t) * carr_c(t), color=BLU, lw=0.8, alpha=0.8, label=r"$\sqrt{2}\,s_c(t)\cos(2\pi f_c t)$")
    a.set(title=r"Ramo I: $s_c$ moltiplicato per la portante $\sqrt{2}\cos(2\pi f_c t)$", ylabel="ampiezza")
    a.legend(loc="upper right", fontsize=8, ncol=2)
    a = ax[1]
    a.plot(t, ss(t), color=ARANCIO, lw=2.2, label=r"$s_s(t)$ (ingresso del ramo Q)")
    a.plot(t, ss(t) * carr_s(t), color=ARANCIO, lw=0.8, alpha=0.8, label=r"$-\sqrt{2}\,s_s(t)\sin(2\pi f_c t)$")
    a.set(title=r"Ramo Q: $s_s$ moltiplicato per $-\sqrt{2}\sin(2\pi f_c t)$", ylabel="ampiezza")
    a.legend(loc="upper right", fontsize=8, ncol=2)
    a = ax[2]
    env = R2 * np.sqrt(sc(t) ** 2 + ss(t) ** 2)
    a.plot(t, sp(t), color=INK, lw=0.9, label=r"$s_p(t)$ = somma dei due rami, eq. (17)")
    a.plot(t, env, color=ROSSO, lw=1.6, ls="--", label=r"$\pm\sqrt{2}\,|s(t)|$ (inviluppo)")
    a.plot(t, -env, color=ROSSO, lw=1.6, ls="--")
    a.set(title=r"Somma: segnale passa-banda $s_p(t)$ con portante a $f_c = 10$ kHz",
          xlabel="t [ms]", ylabel="ampiezza")
    a.legend(loc="upper right", fontsize=8, ncol=2)
    for a in ax:
        a.set_ylim(a.get_ylim()[0], a.get_ylim()[1] * 1.3)
    fig.suptitle("Upconversion nel tempo: dalla banda base alla portante", fontsize=12, y=0.995)
    fig.tight_layout()
    save(fig, "grafico-rice-upconversion-tempo.png")


# ---------------------------------------------------------------- 2. downconversion nel tempo
def lpf_ideale(x, dt, taglio):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), dt)
    X[f > taglio] = 0
    return np.fft.irfft(X, len(x))


def downconversion_tempo():
    # finestra periodica di 8 ms (4 periodi): il filtro nel dominio della frequenza è esatto
    tt = np.arange(0, 8.0, 0.0005)
    dt = tt[1] - tt[0]
    ramo_i = R2 * sp(tt) * np.cos(2 * np.pi * FC * tt)
    ramo_q = -R2 * sp(tt) * np.sin(2 * np.pi * FC * tt)
    out_i, out_q = lpf_ideale(ramo_i, dt, 5.0), lpf_ideale(ramo_q, dt, 5.0)
    assert np.abs(out_i - sc(tt)).max() < 1e-6 and np.abs(out_q - ss(tt)).max() < 1e-6
    m = tt < T_MOSTRA
    x = tt[m]
    fig, ax = plt.subplots(3, 2, figsize=(11, 8.4), sharex=True, sharey="row")
    for c, (nome, prod, lento, out, col, car) in enumerate([
            ("ramo I", ramo_i, sc(tt), out_i, BLU, r"$\sqrt{2}\,\cos(2\pi f_c t)$"),
            ("ramo Q", ramo_q, ss(tt), out_q, ARANCIO, r"$-\sqrt{2}\,\sin(2\pi f_c t)$")]):
        a = ax[0, c]
        a.plot(x, sp(x), color=INK, lw=0.8)
        a.set(title=f"{nome}: ingresso $s_p(t)$", ylabel="ampiezza" if c == 0 else "")
        a = ax[1, c]
        a.plot(x, prod[m], color=col, lw=1.0, label=r"$s_p(t)\cdot$" + car)
        a.plot(x, lento[m], color=ROSSO, lw=2.2, ls="--", label=r"parte lenta: $s_c$" if c == 0 else r"parte lenta: $s_s$")
        a.set(title="dopo il moltiplicatore: parte lenta + termini a $2f_c$ = 20 kHz")
        a.legend(loc="upper right", fontsize=8)
        a = ax[2, c]
        a.plot(x, lento[m], color=INK_2, lw=3.2, alpha=0.5, label="componente originale")
        a.plot(x, out[m], color=col, lw=1.8, label="uscita del passa-basso (5 kHz)")
        a.set(title="dopo il passa-basso: i termini a $2f_c$ sono tagliati", xlabel="t [ms]",
              ylabel="ampiezza" if c == 0 else "")
        a.legend(loc="upper right", fontsize=8)
    for c in range(2):
        for r in (1, 2):
            ax[r, c].set_ylim(ax[r, c].get_ylim()[0], ax[r, c].get_ylim()[1] * 1.3)
    fig.suptitle("Downconversion nel tempo: moltiplicazione per la portante e passa-basso, eq. (21)", fontsize=12, y=0.995)
    fig.tight_layout()
    save(fig, "grafico-rice-downconversion-tempo.png")


# ---------------------------------------------------------------- 3. upconversion e downconversion in frequenza
def lobo(f, centro=0.5, semi=1.5, h=1.0):
    return h * np.clip(1 - np.abs(f - centro) / semi, 0, None)


def up_down_frequenza():
    fc, lpf = 6.0, 4.0
    f = np.linspace(-16, 16, 6000)
    S = lambda x: lobo(x)                                    # S(f) reale, asimmetrico: supporto [-1, 2] kHz
    quad = [
        (S(f), BLU, r"$S(f)$: inviluppo complesso in banda base", [(0.5, 1.0, "1")], False),
        ((S(f - fc) + S(-f - fc)) / R2, ARANCIO,
         r"Upconversion: $S_p(f) = [S(f-f_c) + S^{*}(-f-f_c)]/\sqrt{2}$ (eq. (14))", [(fc + 0.5, 0.71, r"$S(f-f_c)/\sqrt{2}$")], False),
        ((S(f - 2 * fc) + S(-f - 2 * fc) + S(f) + S(-f)) / 2, ROSSO,
         r"Downconversion, dopo il moltiplicatore $\sqrt{2}\cos(2\pi f_c t)$: una copia in banda base e due a $\pm 2f_c$",
         [(0.0, 0.67, r"$[S(f)+S^{*}(-f)]/2$"), (2 * fc + 0.5, 0.5, r"$S(f-2f_c)/2$")], True),
        ((S(f) + S(-f)) / 2, BLU, r"Dopo il passa-basso: resta $[S(f) + S^{*}(-f)]/2$ = spettro di $s_c(t)$", [(0.0, 0.67, "")], False),
    ]
    fig, ax = plt.subplots(4, 1, figsize=(9.5, 9), sharex=True)
    for a, (y, col, tit, note, lp) in zip(ax, quad):
        a.fill_between(f, y, color=col, alpha=0.3, lw=0)
        a.plot(f, y, color=col)
        a.axvline(0, color=INK_2, lw=0.8)
        a.set(title=tit, ylim=(-0.05, 1.3), yticks=[])
        a.title.set_fontsize(9.5)
        for x0, h, txt in note:
            a.text(x0, h + 0.07, txt, ha="center", fontsize=9, color=col)
        if lp:
            a.add_patch(plt.Rectangle((-lpf, -0.05), 2 * lpf, 1.2, fill=False, ec=INK, ls="--", lw=1.2))
            a.text(0, 1.2, "passa-basso", ha="center", fontsize=8.5, color=INK)
    ax[1].text(-fc - 0.5, 0.78, r"$S^{*}(-f-f_c)/\sqrt{2}$", ha="center", fontsize=9, color=ARANCIO)
    ax[2].text(-2 * fc - 0.5, 0.57, r"$S^{*}(-f-2f_c)/2$", ha="center", fontsize=9, color=ROSSO)
    ax[3].set_xlabel("f [kHz]")
    for a in ax:
        for c in (-fc, fc):
            a.axvline(c, color=GRID, lw=1, ls=":")
    fig.suptitle(r"Upconversion e downconversion in frequenza ($f_c = 6$ kHz, $S(f)$ reale e asimmetrico, solo per disegnare)",
                 fontsize=11, y=0.995)
    fig.tight_layout()
    save(fig, "grafico-rice-up-down-frequenza.png")


# ---------------------------------------------------------------- 4. dove mettere la frequenza di taglio del passa-basso
def requisito_passabasso():
    """Spettro dopo il moltiplicatore: banda utile |f| < W, copie a +-2 f_c, e il taglio f_LP del filtro."""
    W = 2.0                                                  # kHz, banda di s_c e s_s (come nell'esempio nel tempo)
    f = np.linspace(-27, 27, 6000)
    forma = lambda x: np.clip(2.2 * (1 - np.abs(x) / W), 0, 1)       # lobo trapezoidale di semi-larghezza W
    base = forma(f)
    copie = 0.75 * (forma(f - 2 * FC) + forma(f + 2 * FC))
    casi = [
        (5.0, "(a) $f_{LP} = 5$ kHz: dentro l'intervallo ammesso", "banda utile intera, copie a $\\pm 2f_c$ tagliate", ACQUA),
        (1.0, "(b) $f_{LP} = 1$ kHz $< W$: troppo basso", "il filtro taglia parte della banda utile", ROSSO),
        (19.0, "(c) $f_{LP} = 19$ kHz $> 2f_c - W = 18$ kHz: troppo alto", "il filtro lascia passare l'inizio delle copie a $\\pm 2f_c$", ROSSO),
    ]
    fig, ax = plt.subplots(3, 1, figsize=(9.5, 8.4), sharex=True)
    for a, (flp, tit, nota, col) in zip(ax, casi):
        a.fill_between(f, base, color=BLU, alpha=0.30, lw=0)
        a.fill_between(f, copie, color=ARANCIO, alpha=0.30, lw=0)
        a.plot(f, base, color=BLU, lw=1.6)
        a.plot(f, copie, color=ARANCIO, lw=1.6)
        a.add_patch(plt.Rectangle((-flp, -0.04), 2 * flp, 1.32, fill=False, ec=INK, ls="--", lw=1.3))
        a.text(0, 1.33, "passa-basso", ha="center", fontsize=8.5)
        # parti perse o lasciate passare
        if flp < W:
            persa = np.where(np.abs(f) > flp, base, 0)
            a.fill_between(f, persa, color=ROSSO, alpha=0.75, lw=0, hatch="///", ec=ROSSO)
        if flp > 2 * FC - W:
            passa = np.where(np.abs(f) < flp, copie, 0)
            a.fill_between(f, passa, color=ROSSO, alpha=0.75, lw=0, hatch="///", ec=ROSSO)
        a.axvline(0, color=INK_2, lw=0.8)
        a.set(ylim=(-0.05, 1.5), yticks=[], title=tit + " — " + nota)
        a.title.set_fontsize(9.5)
    # intervallo ammesso per f_LP, e quote di riferimento sul primo pannello
    a = ax[0]
    for x, et in ((W, "$W$"), (2 * FC - W, "$2f_c - W$"), (-W, "$-W$"), (-(2 * FC - W), "$-(2f_c - W)$")):
        a.plot([x, x], [-0.04, 0.0], color=INK, lw=1)
        a.text(x, -0.22, et, ha="center", fontsize=8.5)
    for x, et in ((FC, ""), (-FC, "")):
        pass
    a.annotate("", xy=(W, 1.12), xytext=(2 * FC - W, 1.12), arrowprops=dict(arrowstyle="<->", color=ACQUA, lw=1.8))
    a.text(14, 1.17, r"$f_{LP}$ ammesso: $W \leq f_{LP} \leq 2f_c - W$", ha="center", fontsize=9, color=ACQUA)
    a.text(0, 0.45, "banda utile\n$|f| < W$", ha="center", fontsize=8.5, color=BLU)
    a.text(2 * FC, 0.62, "copia a $+2f_c$", ha="center", fontsize=8.5, color=ARANCIO)
    a.text(-2 * FC, 0.62, "copia a $-2f_c$", ha="center", fontsize=8.5, color=ARANCIO)
    ax[2].set_xlabel("f [kHz]")
    ax[2].set_xticks(range(-24, 25, 4))
    fig.suptitle(r"Dove mettere il passa-basso dopo il moltiplicatore ($f_c = 10$ kHz, $W = 2$ kHz)", fontsize=11.5, y=0.995)
    fig.tight_layout()
    save(fig, "grafico-rice-requisito-passabasso.png")



if __name__ == "__main__":
    upconversion_tempo()
    downconversion_tempo()
    up_down_frequenza()
    requisito_passabasso()
