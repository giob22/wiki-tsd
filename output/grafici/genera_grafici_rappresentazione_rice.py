"""Grafici di funzione per la lezione "Complex baseband representation" (Rappresentazione_Rice.pdf).

Nessun grafico riproduce una figura delle slide: sono generati dalle formule del PDF
(eq. (3), (13), (17), (21)) come supporto alla comprensione.
Uso: python genera_grafici_rappresentazione_rice.py  (richiede numpy, matplotlib, pillow)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent

# Stessa palette e stile di genera_grafici_campionamento.py
SURFACE = "#fcfcfb"
INK = "#1f1f1e"
INK_2 = "#5f5e57"
GRID = "#e4e3dc"
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]          # blu (I), arancio (Q), acqua

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


# Esempio comune (t in ms, f in kHz). f_c piccola per rendere visibile la portante:
# nei sistemi reali f_c / B e' molto piu' grande.
FC = 10.0
I_RIGHE = [(1.0, 0.5), (2.0, 0.25)]      # s_c = cos(2pi t) + 0.5 cos(4pi t): righe di modulo 0.5 e 0.25 a +-f
Q_RIGHE = [(1.5, 0.4)]                   # s_s = 0.8 sin(3pi t): righe di modulo 0.4 a +-1.5 kHz


def s_c(t):
    return np.cos(2 * np.pi * 1.0 * t) + 0.5 * np.cos(2 * np.pi * 2.0 * t)


def s_s(t):
    return 0.8 * np.sin(2 * np.pi * 1.5 * t)


def s_p(t):                                                   # eq. (17)
    return np.sqrt(2) * s_c(t) * np.cos(2 * np.pi * FC * t) - np.sqrt(2) * s_s(t) * np.sin(2 * np.pi * FC * t)


# 1. Dal segnale passa-banda all'inviluppo complesso: eq. (3) e (13), p.10 e p.13 del PDF
def catena_spettri(fc=10.0, B=4.0, A=1.0):
    f = np.linspace(-16, 16, 6401)
    a, b = fc - B / 4, fc + 3 * B / 4                         # lobo asimmetrico attorno a f_c (come la slide 11)
    lobo = lambda x: np.where((x >= a) & (x <= b), A * (b - x) / (b - a), 0.0)
    Sp = lobo(f) + lobo(-f)                                   # reale e pari: rispetta S_p(f) = S_p*(-f)
    Spp = np.sqrt(2) * Sp * (f > 0)                           # (3)
    S = np.sqrt(2) * lobo(f + fc)                             # (13): S(f) = S_p^+(f + f_c)
    titoli = [
        r"(a) $S_p(f)$: segnale passa-banda reale; i lobi a $\pm f_c$ sono speculari (simmetria hermitiana)",
        r"(b) $S_p^+(f) = \sqrt{2}\,S_p(f)\,u(f)$: tengo solo $f > 0$ e moltiplico per $\sqrt{2}$  — eq. (3)",
        r"(c) $S(f) = S_p^+(f + f_c)$: sposto il lobo da $f_c$ a 0  — eq. (13)",
    ]
    fig, axs = plt.subplots(3, 1, figsize=(8, 6.8), sharex=True)
    for ax, y, col, tit in zip(axs, [Sp, Spp, S], [INK_2, CAT[0], CAT[1]], titoli):
        ax.fill_between(f, 0, y, color=col, alpha=0.18, lw=0)
        ax.plot(f, y, color=col, lw=2)
        ax.axvline(0, color=INK_2, lw=0.8)
        ax.set_ylim(0, 1.8)
        ax.set_yticks([0, A, np.sqrt(2) * A])
        ax.set_yticklabels(["0", "$A$", r"$\sqrt{2}A$"])
        ax.set_title(tit, loc="left", fontsize=9.5)
    axs[0].text(-fc, 1.2, "stessa informazione\ndel lobo a $+f_c$", ha="center", fontsize=8.5, color=INK_2)
    axs[1].text(-fc, 0.35, "scartato", ha="center", fontsize=8.5, color=INK_2)
    axs[2].text(4.2, 1.0, "non simmetrico attorno a 0:\n$S(f) \\neq S^*(-f)$, quindi $s(t)$ è complesso",
                fontsize=8.5, color=INK)
    axs[2].set_xticks([-fc, 0, fc])
    axs[2].set_xticklabels([r"$-f_c$", "0", r"$f_c$"])
    axs[2].set_xlabel("$f$")
    fig.tight_layout()
    save(fig, "grafico-rice-catena-spettri.png")


# 2. Componenti I/Q lente e portante veloce: eq. (15)-(17), p.14 e p.19 del PDF
def iq_nel_tempo():
    t = np.linspace(0, 2, 8001)                              # ms
    sc, ss = s_c(t), s_s(t)
    amp = np.abs(sc + 1j * ss)                                # |s(t)|
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 5.8), sharex=True, height_ratios=[1, 1.2])
    a1.plot(t, sc, color=CAT[0], label=r"$s_c(t)$ (in fase, I)")
    a1.plot(t, ss, color=CAT[1], label=r"$s_s(t)$ (quadratura, Q)")
    a1.plot(t, amp, color=INK, lw=1.3, ls="--", label=r"$|s(t)| = \sqrt{s_c^2 + s_s^2}$")
    a1.axhline(0, color=INK_2, lw=0.6)
    a1.set_ylim(-1.9, 2.3)
    a1.set_ylabel("banda base")
    a1.set_title("Inviluppo complesso $s = s_c + j s_s$: varia lentamente (righe a 1, 1.5 e 2 kHz)",
                 loc="left", fontsize=9.5)
    a1.legend(loc="upper right", ncol=3, fontsize=8.5)
    a2.plot(t, s_p(t), color=INK_2, lw=0.9, label=r"$s_p(t)$, eq. (17)")
    a2.plot(t, np.sqrt(2) * amp, color=INK, lw=1.3, ls="--", label=r"$\pm\sqrt{2}\,|s(t)|$")
    a2.plot(t, -np.sqrt(2) * amp, color=INK, lw=1.3, ls="--")
    a2.axhline(0, color=INK_2, lw=0.6)
    a2.set_ylim(-3.2, 3.6)
    a2.set_ylabel("passa-banda")
    a2.set_xlabel("$t$ [ms]")
    a2.set_title(r"$s_p(t) = \sqrt{2}\,|s(t)|\cos(2\pi f_c t + \theta(t))$ con $f_c = 10$ kHz: "
                 "portante veloce dentro un inviluppo lento", loc="left", fontsize=9.5)
    a2.legend(loc="upper right", ncol=2, fontsize=8.5)
    fig.tight_layout()
    save(fig, "grafico-rice-iq-tempo.png")


def verifica_righe():
    """Controllo con la FFT dei moduli delle righe usate nell'animazione (finestra di 2 ms = periodo comune)."""
    N = 8000
    t = np.arange(N) * 2.0 / N                                # passo 0.5 kHz in frequenza
    df = 0.5
    for nome, x in [("s_p", s_p(t)), ("sqrt2*s_p*cos", np.sqrt(2) * s_p(t) * np.cos(2 * np.pi * FC * t))]:
        X = np.abs(np.fft.fft(x)) / N
        righe = {f: round(float(X[int(round(f / df))]), 3) for f in (1, 1.5, 2, 8, 8.5, 9, 11, 11.5, 12, 18, 18.5, 19, 21, 21.5, 22)}
        print(" ", nome, {k: v for k, v in righe.items() if v > 1e-6})


# 3. Animazione della downconversion del ramo I: eq. (21), p.17 del PDF
def downconversion_animazione(fps=10, anteprima=None):
    """anteprima = (cartella, [frame, ...]): salva solo quei fotogrammi come PNG, senza la GIF."""
    from matplotlib.animation import FuncAnimation, PillowWriter
    t = np.linspace(0, 2, 8001)
    sp = s_p(t)
    prod = np.sqrt(2) * sp * np.cos(2 * np.pi * FC * t)       # eq. (21)
    amp = np.abs(s_c(t) + 1j * s_s(t))
    fasi = [20, 30, 25, 25, 30]
    testi = [
        ("Passo 1 · Il segnale passa-banda $s_p(t)$",
         "le righe di I (blu) e di Q (arancio) stanno attorno a $\\pm f_c$"),
        ("Passo 2 · Moltiplico per $\\sqrt{2}\\cos(2\\pi f_c t)$",
         "ogni riga si sdoppia in due copie spostate di $\\pm f_c$: una va verso 0, l'altra verso $\\pm 2f_c$"),
        ("Passo 3 · Attorno a 0 le copie di I si sommano, quelle di Q si cancellano",
         "le due copie di Q arrivano con segno opposto: $-2 s_s \\sin\\cos = -s_s \\sin(4\\pi f_c t)$ non ha parte lenta"),
        ("Passo 4 · Filtro passa-basso",
         "taglio tra la banda di $s_c$ (2 kHz) e $2f_c - 2$ kHz: le copie a $\\pm 2f_c$ vengono eliminate"),
        ("Passo 5 · Uscita: la componente in fase $s_c(t)$",
         "coincide con quella di partenza; per $s_s(t)$ si usa lo stesso schema con $-\\sqrt{2}\\sin(2\\pi f_c t)$"),
    ]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.6, 6.6), height_ratios=[1.1, 1])
    fig.subplots_adjust(left=0.08, right=0.98, top=0.80, bottom=0.08, hspace=0.45)
    h1 = fig.text(0.02, 0.962, "", fontsize=12, weight="bold", color=INK)
    h2 = fig.text(0.02, 0.922, "", fontsize=9.5, color=INK_2)

    def fase(k):
        s = 0
        for i, L in enumerate(fasi):
            if k < s + L:
                return i + 1, (k - s) / (L - 1)
            s += L
        return len(fasi), 1.0

    def stems(ax, xs, hs, col, alpha=1.0):
        for x, h in zip(xs, hs):
            if h > 1e-4:
                ax.plot([x, x], [0, h], color=col, lw=2, alpha=alpha, solid_capstyle="butt")
                ax.plot([x], [h], "o", ms=5, color=col, alpha=alpha, mec=SURFACE, mew=1)

    def righe(lista):                                         # righe a +-f con modulo m
        return [(s * f, m) for f, m in lista for s in (1, -1)]

    I, Q = righe(I_RIGHE), righe(Q_RIGHE)

    def draw(k):
        p_i, p = fase(k)
        h1.set_text(testi[p_i - 1][0])
        h2.set_text(testi[p_i - 1][1])
        a1.clear()
        a2.clear()
        # --- tempo
        if p_i == 1:
            a1.plot(t, sp, color=INK_2, lw=0.8, label="$s_p(t)$")
            a1.plot(t, np.sqrt(2) * amp, color=INK, lw=1.2, ls="--", label=r"$\pm\sqrt{2}|s(t)|$")
            a1.plot(t, -np.sqrt(2) * amp, color=INK, lw=1.2, ls="--")
        else:
            al = 1.0 if p_i <= 3 else (1 - 0.8 * p if p_i == 4 else 0.2)
            a1.plot(t, prod, color=INK_2, lw=0.8, alpha=al, label=r"$\sqrt{2}\,s_p(t)\cos(2\pi f_c t)$")
            if p_i == 3:
                a1.plot(t, s_c(t), color=CAT[0], lw=1.6, ls="--", alpha=p, label="parte lenta")
            if p_i >= 4:
                a1.plot(t, s_c(t), color=CAT[0], lw=2.4, alpha=p if p_i == 4 else 1.0, label="uscita del filtro")
            if p_i == 5:
                a1.plot(t, s_c(t), color=INK, lw=1.2, ls=":", label="$s_c(t)$ di partenza")
        a1.axhline(0, color=INK_2, lw=0.6)
        a1.set_xlim(0, 2)
        a1.set_ylim(-3.4, 3.4)
        a1.set_xlabel("$t$ [ms]")
        a1.legend(loc="lower right", ncol=3, fontsize=8.5, bbox_to_anchor=(1.0, 1.0))
        # --- frequenza (moduli delle righe)
        if p_i == 1:
            for fc_ in (FC, -FC):
                stems(a2, [fc_ + x for x, _ in I], [m / np.sqrt(2) for _, m in I], CAT[0])
                stems(a2, [fc_ + x for x, _ in Q], [m / np.sqrt(2) for _, m in Q], CAT[1])
        elif p_i == 2:
            for fc_ in (FC, -FC):
                for dest in (-1, 1):                          # copia spostata di -f_c e di +f_c
                    stems(a2, [fc_ + x + dest * FC * p for x, _ in I], [m / 2 for _, m in I], CAT[0])
                    stems(a2, [fc_ + x + dest * FC * p for x, _ in Q], [m / 2 for _, m in Q], CAT[1])
        else:
            a_far = 1.0 if p_i == 3 else (1 - p if p_i == 4 else 0.0)
            for c in (2 * FC, -2 * FC):
                stems(a2, [c + x for x, _ in I], [m / 2 for _, m in I], CAT[0], alpha=a_far)
                stems(a2, [c + x for x, _ in Q], [m / 2 for _, m in Q], CAT[1], alpha=a_far)
            gI = 0.5 + 0.5 * p if p_i == 3 else 1.0
            stems(a2, [x for x, _ in I], [m * gI for _, m in I], CAT[0])
            if p_i == 3:
                stems(a2, [x for x, _ in Q], [m / 2 * (1 - p) for _, m in Q], CAT[1], alpha=1 - 0.7 * p)
                a2.text(0, 0.72, "Q: copie di segno opposto → si cancellano", ha="center", fontsize=9, color=INK)
        if p_i >= 4:
            a2.add_patch(plt.Rectangle((-5, 0), 10, 0.62, facecolor="#eef4fc", edgecolor=CAT[0], lw=1.4, zorder=0))
            a2.text(0, 0.68, "filtro passa-basso", ha="center", fontsize=9, color=INK)
        a2.set_xlim(-24.5, 24.5)
        a2.set_ylim(0, 0.85)
        a2.set_xticks([-2 * FC, -FC, 0, FC, 2 * FC])
        a2.set_xticklabels([r"$-2f_c$", r"$-f_c$", "0", r"$f_c$", r"$2f_c$"])
        a2.set_yticks([])
        a2.set_xlabel(r"$f$  ($f_c = 10$ kHz)")
        a2.set_ylabel("spettro (moduli)")
        return []

    if anteprima:
        cartella, quali = anteprima
        for k in quali:
            draw(k)
            fig.savefig(f"{cartella}/anteprima-downconversion-{k:03d}.png", dpi=80, bbox_inches=None)
        plt.close(fig)
        return
    ani = FuncAnimation(fig, draw, frames=sum(fasi), blit=False)
    ani.save(OUT / "grafico-rice-downconversion.gif", writer=PillowWriter(fps=fps), dpi=80)
    plt.close(fig)
    print("scritto grafico-rice-downconversion.gif")


if __name__ == "__main__":
    catena_spettri()
    iq_nel_tempo()
    verifica_righe()
    downconversion_animazione()
