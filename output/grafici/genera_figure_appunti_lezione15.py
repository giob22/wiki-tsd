"""Ridisegni puliti dei disegni a mano negli appunti della Lezione 15 (ofdm_goldsmith_slides.pdf).

Ogni figura rifà un disegno degli appunti (stesso contenuto, resa più leggibile), senza aggiungere argomenti nuovi.

  grafico-l15-appunti-p4-polifase.png       p. 4  — S/P come decomposizione polifase, d(mN+i) = d_i(m), N = 4:
                                              l'uscita parte quando il blocco è completo e ogni simbolo dura T_u = N T_b
  grafico-l15-appunti-p9-rallentare.png     p. 9  — perché rallentare aiuta: simboli lunghi T_u = N T_b invece di T_b
                                              ⇒ spettro N volte più stretto
  grafico-l15-appunti-p10-canale-piatto.png p. 10 — segnale a portante singola più largo della banda in cui il canale è
                                              circa costante; con tante sottoportanti strette il canale su ognuna è piatto
  grafico-l15-appunti-p13-isi-ici.png       p. 13 — chi disturba il simbolo a_i[m]: blocchi diversi (ISI) e rami diversi
                                              dello stesso blocco (ICI); condizione delta_{k-i} delta_{n-m}
  grafico-l15-appunti-p14-ortogonalita.png  p. 14 — il calcolo dell'ortogonalità: finestre disgiunte per n != m; per
                                              n = m un numero intero di periodi in T_u dà integrale nullo, una piccola
                                              variazione di frequenza no (ICI)

Uso: python genera_figure_appunti_lezione15.py  (richiede numpy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ACQUA, ROSSO, VIOLA = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#7c5cc4"
RAMI = [BLU, ARANCIO, ACQUA, VIOLA]
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": False, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})


def chiaro(c, a=0.22):
    """Colore c mescolato col fondo: riempimento tenue delle caselle."""
    r, g, b = matplotlib.colors.to_rgb(c)
    s = matplotlib.colors.to_rgb(SURFACE)
    return tuple(a * x + (1 - a) * y for x, y in zip((r, g, b), s))


def freccia(ax, a, b, colore=INK_2, stile="-|>", **kw):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=stile, mutation_scale=10, color=colore, lw=1.1, **kw))


def quota(ax, x0, x1, y, testo, colore=INK):
    freccia(ax, (x0, y), (x1, y), colore, "<|-|>")
    ax.text((x0 + x1) / 2, y + 0.12, testo, ha="center", va="bottom", color=colore, fontsize=9.5)


# ------------------------------------------------------------------------------------------------ p. 4
def polifase(N=4, blocchi=3):
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.set_xlim(-3.6, N * (blocchi + 1) + 0.6), ax.set_ylim(-7.4, 2.2), ax.axis("off")
    h = 0.78
    # ingresso seriale: un simbolo ogni T_b, colore = ramo di destinazione i = l mod N
    for l in range(N * blocchi):
        c = RAMI[l % N]
        ax.add_patch(Rectangle((l, 0), 1, h, fc=chiaro(c), ec=c, lw=1))
        ax.text(l + .5, h / 2, f"$d({l})$", ha="center", va="center", fontsize=8.5)
    ax.text(-0.3, h / 2, "ingresso seriale\n$R_b=1/T_b$", ha="right", va="center", fontsize=9.5)
    quota(ax, 0, 1, h + 0.15, "$T_b$")
    # uscite: il ramo i riceve d(mN+i); il simbolo m esce quando il blocco m è completo e dura T_u = N T_b
    ys = [-1.9 - 1.25 * i for i in range(N)]
    for i, y in enumerate(ys):
        c = RAMI[i]
        nome = f"ramo $i={i}$" if i < N - 1 else f"ramo $i=N-1={i}$"
        ax.text(-0.3, y + h / 2, nome, ha="right", va="center", color=c, fontsize=9.5)
        for m in range(blocchi):
            x0 = N * (m + 1)
            ax.add_patch(Rectangle((x0, y), N, h, fc=chiaro(c), ec=c, lw=1))
            ax.text(x0 + N / 2, y + h / 2, f"$d_{i}({m})=d({m * N + i})$", ha="center", va="center", fontsize=9)
        # da dove arriva il simbolo del blocco 0
        freccia(ax, (i + .5, -0.02), (N + 0.15, y + h), c, "-|>", ls=(0, (3, 2)), alpha=.75)
    ax.text(N * (blocchi + 1) + 0.4, ys[0] + h / 2, "rate $R_b/N$", ha="left", va="center", fontsize=9.5)
    # blocco completo: l'uscita parte a t = N T_b
    ax.plot([N, N], [ys[-1] - 0.3, h + 0.05], color=ROSSO, lw=1, ls=":")
    ax.text(N + 0.1, ys[-1] - 0.55, "blocco 0 completo:\nescono i primi $N$ simboli", color=ROSSO, fontsize=8.5, va="top")
    quota(ax, 2 * N, 3 * N, ys[-1] - 0.75, "$T_u=NT_b$")
    # asse dei tempi
    yt = -7.0
    freccia(ax, (0, yt), (N * (blocchi + 1) + 0.5, yt), INK_2)
    for m in range(blocchi + 2):
        ax.plot([N * m] * 2, [yt - .08, yt + .08], color=INK_2, lw=1)
        ax.text(N * m, yt - 0.18, ["0", "$T_u$", "$2T_u$", "$3T_u$", "$4T_u$"][m], ha="center", va="top", fontsize=9)
    ax.text(N * (blocchi + 1) + 0.55, yt, "$t$", va="center")
    ax.text(-3.5, 1.95, r"Convertitore S/P = decomposizione polifase:  $d(mN+i)=d_i(m)$,  $N=4$",
            fontsize=11, va="top", weight="bold")
    fig.savefig(OUT / "grafico-l15-appunti-p4-polifase.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------ p. 9
def rallentare(N=4, simboli=16, seme=3):
    rng = np.random.default_rng(seme)
    fig, ax = plt.subplots(2, 2, figsize=(9.4, 4.8), gridspec_kw=dict(width_ratios=[1.25, 1]))
    t = np.linspace(0, simboli, 4000)                                   # tempo in unità di T_b
    d = rng.choice([-1, 1], simboli)
    a = rng.choice([-1, 1], simboli // N)
    serie = d[np.minimum(t.astype(int), simboli - 1)]
    ramo = a[np.minimum((t / N).astype(int), simboli // N - 1)]
    for r, (y, c, tit) in enumerate([(serie, BLU, "flusso seriale: un simbolo ogni $T_b$ (rate $R_b$)"),
                                    (ramo, ARANCIO, f"un ramo dopo lo S/P: un simbolo ogni $T_u=NT_b$ (rate $R_b/N$), $N={N}$")]):
        g = ax[r, 0]
        g.plot(t, y, color=c, lw=1.8)
        g.set_ylim(-1.6, 1.6), g.set_yticks([-1, 1]), g.set_xlim(0, simboli)
        g.set_xticks(range(0, simboli + 1, N if r else 2))
        g.set_title(tit, fontsize=9.5, loc="left")
        g.grid(True, color=GRID)
    ax[1, 0].set_xticklabels([f"{k // N}$T_u$" if k else "0" for k in range(0, simboli + 1, N)])
    ax[0, 0].set_xticklabels([f"{k}$T_b$" if k else "0" for k in range(0, simboli + 1, 2)], fontsize=8)
    ax[1, 0].set_xlabel("$t$")
    f = np.linspace(-3, 3, 3000)                                        # frequenza normalizzata f T_b
    for r, (T, c, testo) in enumerate([(1, BLU, "lobo principale largo $2/T_b$"),
                                      (N, ARANCIO, f"$2/T_u=2/(NT_b)$: {N} volte più stretto")]):
        g = ax[r, 1]
        g.fill_between(f, np.sinc(f * T) ** 2, color=chiaro(c, .35))
        g.plot(f, np.sinc(f * T) ** 2, color=c, lw=1.6)
        g.set_xlim(-3, 3), g.set_ylim(0, 1.25), g.set_yticks([])
        g.set_xticks([-2, -1, 0, 1, 2]), g.set_xticklabels(["$-2/T_b$", "$-1/T_b$", "0", "$1/T_b$", "$2/T_b$"], fontsize=8)
        g.text(0, 1.08, testo, ha="center", fontsize=9, color=c)
        g.grid(True, color=GRID)
    ax[0, 1].set_title("spettro di un simbolo (normalizzato)", fontsize=9.5)
    ax[1, 1].set_xlabel("$f$")
    fig.suptitle("Rallentare il sistema: simboli $N$ volte più lunghi ⇒ banda $N$ volte più stretta ⇒ meno ISI",
                 fontsize=11, weight="bold", x=0.02, ha="left")
    fig.tight_layout()
    fig.savefig(OUT / "grafico-l15-appunti-p9-rallentare.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------ p. 10
def canale_piatto(N=16):
    f = np.linspace(-1.35, 1.35, 4000)                                  # frequenza normalizzata alla banda del segnale
    H = abs(1 + 0.7 * np.exp(-2j * np.pi * 1.5 * f)) / 1.7              # canale selettivo (esempio a due cammini)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.6, 5.6), sharex=True)
    # portante singola: uno spettro largo che attraversa massimi e minimi del canale
    S = np.sinc(f / 1.0) ** 2 * (abs(f) <= 1)
    a1.fill_between(f, S, color=chiaro(BLU, .3))
    a1.plot(f, S, color=BLU, lw=1.8, label="spettro del segnale (portante singola)")
    a1.plot(f, H, color=ROSSO, lw=2, label="$|H(f)|$ del canale")
    quota(a1, -0.12, 0.12, 1.05, "banda in cui il canale\nè circa costante", ROSSO)
    a1.set_title("Prima: il segnale è più largo della banda del canale ⇒ il canale lo distorce ⇒ ISI",
                 fontsize=10, loc="left")
    # multiportante: N sottoportanti strette, distanziate 2/N
    fk = -1 + (np.arange(N) + 0.5) * 2 / N
    k0 = 7
    for k, c in enumerate(fk):
        lobo = np.sinc((f - c) * N / 2) ** 2 * (abs(f - c) <= 2 / N)
        a2.plot(f, 0.8 * lobo, color=ACQUA if k != k0 else INK, lw=1.2 if k != k0 else 2)
    a2.plot(f, H, color=ROSSO, lw=2)
    # sulla sottoportante evidenziata il canale vale quasi una costante
    sel = abs(f - fk[k0]) <= 1 / N
    a2.fill_between(f[sel], 0, H[sel], color=chiaro(ROSSO, .35))
    a2.annotate("su una sottoportante il canale\nè approssimabile piatto",
                xy=(fk[k0], H[np.argmin(abs(f - fk[k0]))]), xytext=(0.22, 1.13), fontsize=9,
                arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=1), ha="left")
    a2.set_title("Multiportante: tante sottoportanti strette ⇒ banda del singolo ramo minore ⇒ più robustezza all'ISI",
                 fontsize=10, loc="left")
    a2.plot([], [], color=ACQUA, lw=1.2, label=f"sottoportanti ($N={N}$)")
    a2.plot([], [], color=ROSSO, lw=2, label="$|H(f)|$ del canale")
    for g in (a1, a2):
        g.set_ylim(0, 1.4), g.set_yticks([]), g.grid(True, color=GRID)
        g.legend(fontsize=8.5, loc="upper left")
    a2.set_xticks([-1, 0, 1]), a2.set_xticklabels(["$-B$", "0", "$B$"]), a2.set_xlabel("$f$")
    fig.tight_layout()
    fig.savefig(OUT / "grafico-l15-appunti-p10-canale-piatto.png")
    plt.close(fig)
    return float(np.ptp(H[sel])), float(np.ptp(H[abs(f) <= 1]))


# ------------------------------------------------------------------------------------------------ p. 13
def isi_ici(N=4, blocchi=3, i0=1, m0=1):
    fig, ax = plt.subplots(figsize=(9.0, 4.6))
    ax.set_xlim(-2.2, blocchi + 4.6), ax.set_ylim(-0.9, N + 0.9), ax.axis("off")
    for n in range(blocchi):
        for k in range(N):
            y = N - 1 - k
            if (k, n) == (i0, m0):
                fc, ec, lw = chiaro(ROSSO, .4), ROSSO, 2.2
            elif n != m0:
                fc, ec, lw = chiaro(ARANCIO, .28), ARANCIO, 1
            else:
                fc, ec, lw = chiaro(BLU, .28), BLU, 1
            ax.add_patch(FancyBboxPatch((n + .06, y + .08), .88, .84, boxstyle="round,pad=0,rounding_size=.08",
                                        fc=fc, ec=ec, lw=lw))
            ax.text(n + .5, y + .5, f"$a_{k}[{n}]$", ha="center", va="center", fontsize=10)
    for k in range(N):
        ax.text(-0.15, N - 1 - k + .5, f"ramo $k={k}$" if k < N - 1 else f"ramo $k=N-1$", ha="right", va="center", fontsize=9.5)
    for n in range(blocchi):
        ax.text(n + .5, N + 0.15, f"$n={n}$", ha="center", va="bottom", fontsize=9.5)
    ax.text(-0.15, N + 0.15, "blocco", ha="right", va="bottom", fontsize=9.5)
    ax.text(m0 + .5, -0.25, "stesso blocco\n$n=m$", ha="center", va="top", fontsize=8.5, color=BLU)
    ax.text(blocchi / 2, N + 0.62, "scorre il tempo →", ha="center", fontsize=8.5, color=INK_2)
    # legenda e condizione
    x = blocchi + 0.45
    righe = [(ROSSO, f"$a_{i0}[{m0}]$: il simbolo che voglio ricavare ($i={i0}$, $m={m0}$)"),
             (ARANCIO, "ISI: simboli di altri blocchi, $n\\neq m$\n(anche dello stesso ramo, cioè dello stesso stream)"),
             (BLU, "ICI: stesso blocco, altri rami, $n=m$, $k\\neq i$")]
    for j, (c, t) in enumerate(righe):
        y = N - 0.3 - j * 1.0
        ax.add_patch(Rectangle((x, y - .18), .32, .36, fc=chiaro(c, .4), ec=c, lw=1.2))
        ax.text(x + .45, y, t, va="center", fontsize=9)
    ax.text(x, 0.55, "Per eliminarle entrambe:", fontsize=9.5, weight="bold")
    ax.text(x, 0.05, r"$\langle\phi_k(t-nT_u),\phi_i(t-mT_u)\rangle=\delta_{k-i}\,\delta_{n-m}$", fontsize=11)
    ax.text(x, -0.5, "$n=m$: ortogonalità temporale     $k=i$: ortogonalità fra gli impulsi", fontsize=8.5, color=INK_2)
    fig.savefig(OUT / "grafico-l15-appunti-p13-isi-ici.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------ p. 14
def ortogonalita(dk=2, dnu=2.25):
    fig, ax = plt.subplots(1, 3, figsize=(11.2, 3.5), gridspec_kw=dict(width_ratios=[1, 1.15, 1.15]))
    # (a) blocchi diversi: le finestre rettangolari non si sovrappongono
    g = ax[0]
    for m, c in [(1, BLU), (2, ARANCIO)]:
        g.add_patch(Rectangle((m, 0), 1, 1, fc=chiaro(c, .35), ec=c, lw=1.6))
    g.text(1.5, 1.08, "$R_T(t-mT_u)$", ha="center", color=BLU, fontsize=9.5)
    g.text(2.5, 1.08, "$R_T(t-nT_u)$", ha="center", color=ARANCIO, fontsize=9.5)
    g.set_xlim(0, 3.4), g.set_ylim(0, 1.5), g.set_yticks([])
    g.set_xticks([1, 2, 3]), g.set_xticklabels(["$mT_u$", "$(m+1)T_u$\n$=nT_u$", "$(n+1)T_u$"], fontsize=8.5)
    g.set_title("$n\\neq m$: finestre disgiunte\n⇒ prodotto nullo ⇒ niente ISI", fontsize=10)
    g.set_xlabel("$t$")
    # (b) stesso blocco, k - i intero: periodi interi in T_u, aree positive e negative si compensano
    t = np.linspace(0, 1, 2000)                                         # t / T_u
    for g, nu, tit in [(ax[1], dk, f"$n=m$, $k-i={dk}$: periodi interi in $T_u$"),
                       (ax[2], dnu, f"frequenza spostata: $(f_k-f_i)T_u={dnu}$")]:
        y = np.cos(2 * np.pi * nu * t)
        g.fill_between(t, y, where=y >= 0, color=chiaro(BLU, .45), interpolate=True)
        g.fill_between(t, y, where=y < 0, color=chiaro(ROSSO, .45), interpolate=True)
        g.plot(t, y, color=INK, lw=1.4, label="parte reale")
        g.plot(t, np.sin(2 * np.pi * nu * t), color=INK_2, lw=1, ls="--", label="parte immaginaria")
        g.axhline(0, color=INK_2, lw=.8)
        I = np.exp(1j * np.pi * nu) * np.sinc(nu)                       # <phi_k, phi_i> = e^{j pi nu Tu} sinc(nu Tu)
        g.text(0.5, -1.55, f"$|\\langle\\phi_k,\\phi_i\\rangle|={abs(I):.2f}$" + ("  ⇒ ortogonali" if abs(I) < 1e-9 else "  ⇒ ICI"),
               ha="center", fontsize=10, color=ACQUA if abs(I) < 1e-9 else ROSSO, weight="bold")
        g.set_xlim(0, 1), g.set_ylim(-1.8, 1.45), g.set_yticks([-1, 0, 1])
        g.set_xticks([0, .5, 1]), g.set_xticklabels(["$mT_u$", "", "$(m+1)T_u$"], fontsize=8.5)
        g.set_title(tit, fontsize=10)
        g.set_xlabel("$t$")
    ax[1].legend(fontsize=8, loc="upper right", ncol=2)
    fig.suptitle(r"Integranda $e^{j2\pi (k-i)t/T_u}$: l'integrale su $T_u$ si annulla solo se $(f_k-f_i)T_u$ è un intero non nullo",
                 fontsize=10.5, x=0.02, ha="left", weight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "grafico-l15-appunti-p14-ortogonalita.png")
    plt.close(fig)
    return abs(np.sinc(dk)), abs(np.sinc(dnu))


if __name__ == "__main__":
    polifase()
    rallentare()
    var_sotto, var_tutto = canale_piatto()
    assert var_sotto < 0.2 * var_tutto, (var_sotto, var_tutto)         # sulla sottoportante il canale varia poco
    isi_ici()
    zero, residuo = ortogonalita()
    assert zero < 1e-12 and 0.05 < residuo < 0.2, (zero, residuo)
    print("ok", round(var_sotto / var_tutto, 3), round(float(residuo), 3))
