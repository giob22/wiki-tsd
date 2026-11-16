"""Grafici delle Lezioni 13 (stima e sincronizzazione) e 14 (canali a banda limitata).

  grafico-l13-verosimiglianza-blind.png  miscela (7) e log-verosimiglianza blind vs training, con la soluzione tanh
  grafico-l13-curva-s-pll.png             termine d'errore del PLL (15) in funzione di theta_hat - theta
  grafico-l14-coseno-rialzato.png         spettro a coseno rialzato e impulso per alpha = 0, 0.5, 1
  grafico-l14-errore-timing.png           ISI di caso peggiore con errore di timing: sinc (diverge) e coseno rialzato
Uso: python genera_grafici_lezioni13_14.py  (richiede numpy, matplotlib)
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
    "axes.grid": True, "grid.color": GRID, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})


def gauss(x, m, s2):
    return np.exp(-(x - m) ** 2 / (2 * s2)) / np.sqrt(2 * np.pi * s2)


# ---------------------------------------------------------------- L13: verosimiglianza blind
def verosimiglianza_blind():
    rng = np.random.default_rng(7)
    A, s2, K = 1.0, 0.25, 200
    b = rng.choice([-1, 1], K)
    y = A * b + rng.normal(0, np.sqrt(s2), K)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.6))
    x = np.linspace(-3, 3, 600)
    a1.plot(x, 0.5 * gauss(x, -A, s2) + 0.5 * gauss(x, A, s2), color=BLU, label="miscela (7)")
    a1.plot(x, 0.5 * gauss(x, A, s2), color=ARANCIO, lw=1.2, ls="--", label="½ · gaussiana in +A")
    a1.plot(x, 0.5 * gauss(x, -A, s2), color=ACQUA, lw=1.2, ls="--", label="½ · gaussiana in −A")
    a1.set_xlabel("y(k)"), a1.set_title("pdf di y(k) senza conoscere b(k)  (A = 1, σ² = 0.25)")
    a1.legend(fontsize=8)
    Ag = np.linspace(0.01, 2, 400)
    ll_b = [np.sum(np.log(0.5 * gauss(y, -a, s2) + 0.5 * gauss(y, a, s2))) for a in Ag]
    ll_t = [np.sum(np.log(gauss(y, a * b, s2))) for a in Ag]
    a2.plot(Ag, ll_b - np.max(ll_b), color=BLU, label="blind (7)")
    a2.plot(Ag, ll_t - np.max(ll_t), color=ARANCIO, label="training (simboli noti)")
    Ah = 0.5
    for _ in range(100):  # punto fisso dell'equazione trascendente
        Ah = np.mean(y * np.tanh(Ah * y / s2))
    At = np.mean(y * b)
    a2.axvline(Ah, color=BLU, lw=1, ls=":"), a2.axvline(At, color=ARANCIO, lw=1, ls=":")
    a2.set_ylim(-60, 3), a2.set_xlabel("A di prova"), a2.set_ylabel("log-verosimiglianza (max = 0)")
    a2.set_title(f"K = {K}: Â blind = {Ah:.3f}, Â training = {At:.3f}")
    a2.legend(fontsize=8, loc="lower center")
    fig.savefig(OUT / "grafico-l13-verosimiglianza-blind.png")
    plt.close(fig)


# ---------------------------------------------------------------- L13: curva a S del PLL
def curva_s_pll():
    e = np.linspace(-np.pi, np.pi, 400)
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.plot(e, 0.5 * np.sin(e), color=BLU)
    ax.axhline(0, color=INK_2, lw=.8), ax.axvline(0, color=INK_2, lw=.8)
    ax.annotate("stima troppo grande:\nθ̂ diminuisce", (1.2, .47), fontsize=8, color=INK_2)
    ax.annotate("stima troppo piccola:\nθ̂ aumenta", (-3.0, -.2), fontsize=8, color=INK_2)
    ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], ["−π", "−π/2", "0", "π/2", "π"])
    ax.set_xlabel("θ̂ₖ − θₖ₊₁"), ax.set_ylabel("integrale / T₀")
    ax.set_title("Termine d'errore (15): (T₀/2)·sin(θ̂ₖ − θₖ₊₁)")
    fig.savefig(OUT / "grafico-l13-curva-s-pll.png")
    plt.close(fig)


# ---------------------------------------------------------------- L14: coseno rialzato
def P_rc(f, a, T=1.0):
    f = np.abs(f)
    out = np.zeros_like(f)
    f1, f2 = (1 - a) / (2 * T), (1 + a) / (2 * T)
    out[f <= f1] = T
    m = (f > f1) & (f < f2)
    if a > 0:
        out[m] = T / 2 * (1 - np.sin((f[m] - 1 / (2 * T)) * np.pi * T / a))
    return out


def p_rc(t, a, T=1.0):
    den = 1 - (2 * a * t / T) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.sinc(t / T) * np.cos(np.pi * a * t / T) / den
    sing = np.isclose(den, 0)
    r[sing] = np.pi / 4 * np.sinc(1 / (2 * a)) if a > 0 else 0  # limite per t = ±T/(2α)
    return r


def coseno_rialzato():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.6))
    f = np.linspace(-1.2, 1.2, 1200)
    t = np.linspace(-4, 4, 1601)
    for a, c in ((0, BLU), (0.5, ARANCIO), (1, ACQUA)):
        a1.plot(f, P_rc(f, a), color=c, label=f"α = {a}")
        a2.plot(t, p_rc(t, a), color=c, label=f"α = {a}")
    a1.set_xlabel("f·T"), a1.set_ylabel("P(f)/T"), a1.set_title("Spettro: banda (1+α)/(2T)")
    a1.legend(fontsize=8)
    a2.axhline(0, color=INK_2, lw=.8)
    a2.set_xticks(range(-4, 5)), a2.set_xlabel("t/T"), a2.set_title("Impulso: zeri in t = kT, code più corte con α")
    a2.legend(fontsize=8)
    fig.savefig(OUT / "grafico-l14-coseno-rialzato.png")
    plt.close(fig)


def errore_timing():
    dt = 0.1  # errore di timing pari al 10% di T
    N = np.arange(1, 2001)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for a, c, nome in ((0, BLU, "sinc (α = 0)"), (0.5, ARANCIO, "coseno rialzato α = 0.5")):
        n = np.concatenate([-N[::-1], N]).astype(float)
        termini = np.abs(p_rc(dt - n, a))
        # caso peggiore: s(n) = ±1 con il segno che somma tutti i contributi
        cum = [np.sum(termini[np.abs(n) <= k]) for k in N]
        ax.plot(N, cum, color=c, label=nome)
    ax.set_xscale("log"), ax.set_xlabel("simboli interferenti considerati per lato")
    ax.set_ylabel("ISI di caso peggiore")
    ax.set_title("Errore di timing Δt = 0.1 T")
    ax.legend(fontsize=8)
    fig.savefig(OUT / "grafico-l14-errore-timing.png")
    plt.close(fig)


if __name__ == "__main__":
    verosimiglianza_blind()
    curva_s_pll()
    coseno_rialzato()
    errore_timing()
    print("ok")
