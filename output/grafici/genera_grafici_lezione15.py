"""Grafici della Lezione 15 (OFDM, ofdm_goldsmith_slides.pdf).

  grafico-l15-psd-ofdm.png      PSD ideale dell'OFDM, S(f) = Es * sum_i sinc^2(Tu f - i) (slide 16), N = 8:
                                le sinc^2 delle sottoportanti si sovrappongono e la somma è quasi piatta su N/Tu
  grafico-l15-ici-cfo.png       offset di frequenza normalizzato eps = df/Delta_f (slide 51-52): potenza utile
                                |C_0(eps)|^2 e potenza di ICI sum_{m!=0} |C_m(eps)|^2 = 1 - |C_0(eps)|^2, N = 64
  grafico-l15-papr-ccdf.png     PAPR di un blocco OFDM con simboli QPSK casuali (slide 49-50, 53): probabilità che
                                il PAPR superi una soglia, per N = 16, 64, 256 (IFFT sovracampionata x4)

Uso: python genera_grafici_lezione15.py  (richiede numpy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#1f1f1e", "#5f5e57", "#e4e3dc"
BLU, ARANCIO, ACQUA, ROSSO, VIOLA = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#7c5cc4"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": INK_2,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.grid": True, "grid.color": GRID, "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2, "font.size": 10, "legend.frameon": False, "figure.dpi": 150, "savefig.bbox": "tight",
})


def psd_ofdm(N=8):
    x = np.linspace(-3, N + 2, 3000)                  # f Tu
    comp = np.array([np.sinc(x - i) ** 2 for i in range(N)])
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    for i in range(N):
        ax.plot(x, comp[i], color=[BLU, ARANCIO][i % 2], lw=1, ls="--", alpha=.8)
    ax.plot(x, comp.sum(0), color=INK, lw=2.2, label=r"$S_{xx}(f)/E_s=\sum_i \mathrm{sinc}^2(T_u f-i)$")
    ax.plot([], [], color=BLU, lw=1, ls="--", label="singole sottoportanti")
    ax.annotate("", xy=(-0.5, 1.22), xytext=(N - 0.5, 1.22), arrowprops=dict(arrowstyle="<->", color=ROSSO, lw=1.2))
    ax.text((N - 1) / 2, 1.26, r"circa $N/T_u$", color=ROSSO, ha="center", va="bottom")
    ax.set_xlabel(r"$f\,T_u$  (frequenza normalizzata alla spaziatura $\Delta f=1/T_u$)")
    ax.set_ylabel(r"PSD$/E_s$")
    ax.set_ylim(0, 1.45), ax.set_xlim(-3, N + 2)
    ax.set_xticks(range(-2, N + 2))
    ax.set_title(f"PSD dell'OFDM ideale, N = {N}: lobi sovrapposti, somma quasi piatta")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, fontsize=9)
    fig.savefig(OUT / "grafico-l15-psd-ofdm.png")
    plt.close(fig)
    return comp.sum(0)[np.argmin(abs(x - (N - 1) / 2))]


def C(m, eps, N):
    q = np.arange(N)
    return np.exp(1j * 2 * np.pi * (np.asarray(eps)[..., None] - m) * q / N).mean(-1)


def ici_cfo(N=64):
    eps = np.linspace(0, 0.5, 400)
    utile = abs(C(0, eps, N)) ** 2
    ici = sum(abs(C(m, eps, N)) ** 2 for m in range(1, N))      # m = k - i != 0 (mod N)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
    a1.plot(eps, utile, color=BLU, label=r"utile $|C_0(\epsilon_f)|^2$")
    a1.plot(eps, ici, color=ROSSO, label=r"ICI $\sum_{m\neq0}|C_m(\epsilon_f)|^2$")
    a1.set_xlabel(r"$\epsilon_f=\delta f/\Delta f$"), a1.set_ylabel("frazione della potenza")
    a1.set_title("Dove va la potenza della sottoportante")
    a1.legend(fontsize=9)
    sir = 10 * np.log10(utile[1:] / ici[1:])
    a2.plot(eps[1:], sir, color=VIOLA)
    a2.set_xlabel(r"$\epsilon_f=\delta f/\Delta f$"), a2.set_ylabel("utile / ICI  [dB]")
    a2.set_ylim(0, 40)
    a2.set_title(f"Rapporto segnale/ICI (N = {N}, canale piatto)")
    fig.tight_layout()
    fig.savefig(OUT / "grafico-l15-ici-cfo.png")
    plt.close(fig)
    return utile, ici


def papr_ccdf(Ns=(16, 64, 256), blocchi=20000, sovra=4, seme=1):
    rng = np.random.default_rng(seme)
    soglie = np.linspace(2, 13, 200)
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    for N, c in zip(Ns, (BLU, ACQUA, ARANCIO)):
        a = (rng.choice([-1, 1], (blocchi, N)) + 1j * rng.choice([-1, 1], (blocchi, N))) / np.sqrt(2)
        # IFFT sovracampionata: zeri al centro dello spettro per approssimare il segnale a tempo continuo
        A = np.zeros((blocchi, N * sovra), complex)
        A[:, :N // 2], A[:, -N // 2:] = a[:, :N // 2], a[:, N // 2:]
        x = np.fft.ifft(A, axis=1)
        p = abs(x) ** 2
        papr = 10 * np.log10(p.max(1) / p.mean(1))
        ax.semilogy(soglie, [(papr > s).mean() for s in soglie], color=c, label=f"N = {N}  (massimo teorico {10*np.log10(N):.0f} dB)")
    ax.set_ylim(1e-4, 1.2), ax.set_xlim(2, 13)
    ax.set_xlabel("soglia  PAPR$_0$  [dB]"), ax.set_ylabel(r"$P(\mathrm{PAPR}>\mathrm{PAPR}_0)$")
    ax.set_title("PAPR di un blocco OFDM con QPSK casuale: cresce con N")
    ax.legend(fontsize=9, loc="lower left")
    fig.savefig(OUT / "grafico-l15-papr-ccdf.png")
    plt.close(fig)


if __name__ == "__main__":
    centro = psd_ofdm()
    assert 0.9 < centro < 1.1, centro                      # la somma delle sinc^2 è circa 1 dentro la banda
    utile, ici = ici_cfo()
    assert np.allclose(utile + ici, 1)                     # Parseval: la potenza si ripartisce, non si perde
    assert np.isclose(utile[0], 1) and np.isclose(ici[0], 0)
    papr_ccdf()
    print("ok", round(float(centro), 3), "eps=0.1 ->", round(float(10*np.log10(utile[80]/ici[80])), 1), "dB")
