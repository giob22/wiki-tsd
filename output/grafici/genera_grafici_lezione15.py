"""Grafici della Lezione 15 (OFDM, ofdm_goldsmith_slides.pdf).

  grafico-l15-psd-ofdm.png      PSD ideale dell'OFDM, S(f) = Es * sum_i sinc^2(Tu f - i) (slide 16), N = 8:
                                le sinc^2 delle sottoportanti si sovrappongono e la somma è quasi piatta su N/Tu
  grafico-l15-ici-cfo.png       offset di frequenza normalizzato eps = df/Delta_f (slide 51-52): potenza utile
                                |C_0(eps)|^2 e potenza di ICI sum_{m!=0} |C_m(eps)|^2 = 1 - |C_0(eps)|^2, N = 64
  grafico-l15-papr-ccdf.png     PAPR di un blocco OFDM con simboli QPSK casuali (slide 49-50, 53): probabilità che
                                il PAPR superi una soglia, per N = 16, 64, 256 (IFFT sovracampionata x4)
  grafico-l15-due-ortogonalita.png  le due ortogonalità della biortogonalità (slide 8-9, appunti p. 13-14): nel tempo
                                finestre disgiunte (delta_{n-m}), in frequenza periodi interi in T_u (delta_{k-i});
                                matrice dei prodotti scalari calcolata numericamente = identità

Uso: python genera_grafici_lezione15.py  (richiede numpy, matplotlib)
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


def _rc(f, beta=0.35):
    """Spettro a coseno rialzato (frequenza in unità di 1/T): forma schematica di una sottobanda FDM."""
    a = abs(f)
    return np.where(a <= (1 - beta) / 2, 1.0,
                    np.where(a <= (1 + beta) / 2, np.cos(np.pi / (2 * beta) * (a - (1 - beta) / 2)) ** 2, 0.0))


def _rc_t(t, beta=0.35):
    """Impulso complessivo a coseno rialzato nel tempo (t in unità di T): p(0) = 1, p(mT) = 0 per m != 0."""
    den = 1 - (2 * beta * t) ** 2
    den = np.where(abs(den) < 1e-8, 1e-8, den)
    return np.sinc(t) * np.cos(np.pi * beta * t) / den


def ricevitore_fdm(N=4, i1=1, sigma=0.3, seme=7):
    """Ricevitore FDM della slide 5 ridisegnato con il flusso del segnale lungo i blocchi (esempio QPSK, ramo i = 1)."""
    rng = np.random.default_rng(seme)
    fig = plt.figure(figsize=(13.2, 8.6))
    gs = fig.add_gridspec(2, 6, height_ratios=[1.3, 1], hspace=0.22, wspace=0.42, width_ratios=[1, 1, 1, 1.15, 1.05, 1.5])
    ax = fig.add_subplot(gs[0, :])
    ax.set_xlim(0, 100), ax.set_ylim(3, 43), ax.axis("off")

    def blocco(x, w, y, testo, c=INK_2, fc=SURFACE, fs=8.6):
        ax.add_patch(FancyBboxPatch((x, y - 2.2), w, 4.4, boxstyle="round,pad=0,rounding_size=0.6", fc=fc, ec=c, lw=1.2))
        ax.text(x + w / 2, y, testo, ha="center", va="center", fontsize=fs)

    def fr(x0, y0, x1, y1, c=INK_2):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=9, color=c, lw=1.1))

    # colonne dei blocchi: x iniziale e larghezza
    X = dict(bpf=(7, 10), mix=(21, 9), mf=(34, 9.5), cam=(47, 8), dec=(59, 8), dem=(71, 8))
    righe = [(36, 0, "$i=0$"), (24, i1, f"$i={i1}$"), (8, N - 1, "$i=N-1$")]
    ax.text(2.2, 22, "$y(t)=x(t)+w(t)$", rotation=90, ha="center", va="center", fontsize=9.5)
    ax.plot([4, 4], [8, 36], color=INK_2, lw=1.1)
    ax.add_patch(FancyArrowPatch((2.9, 22), (4, 22), arrowstyle="-", color=INK_2, lw=1.1))
    for y, i, nome in righe:
        hl = i == i1
        c = RAMI_FDM[i % len(RAMI_FDM)]
        ec = c if hl else INK_2
        fc = tuple(0.12 * u + 0.88 * v for u, v in zip(matplotlib.colors.to_rgb(c), matplotlib.colors.to_rgb(SURFACE))) if hl else SURFACE
        sub = nome.strip("$").replace("i=", "")
        fi = f"f_{{{sub}}}"
        fr(4, y, X["bpf"][0], y)
        blocco(*X["bpf"], y, f"passa-banda\nintorno a ${fi}$", ec, fc)
        blocco(*X["mix"], y, f"$\\times\\, e^{{-j2\\pi {fi} t}}$", ec, fc)
        blocco(*X["mf"], y, "filtro adattato\n$g(-t)$", ec, fc)
        blocco(*X["cam"], y, "campiona\n$t=mT$", ec, fc)
        blocco(*X["dec"], y, "decisore", ec, fc)
        blocco(*X["dem"], y, "demapper", ec, fc)
        chiavi = list(X)
        for a, b in zip(chiavi, chiavi[1:]):
            fr(X[a][0] + X[a][1], y, X[b][0], y)
        fr(X["dem"][0] + X["dem"][1], y, 84, 22 + (y - 22) * 0.45)
        ax.text(1.0 + X["bpf"][0] - 1, y + 3.0, nome, fontsize=9, color=c if hl else INK)
        # contorno del blocco «demodulator» della slide
        ax.add_patch(Rectangle((X["mix"][0] - 1.3, y - 3.4), X["dem"][0] + X["dem"][1] - X["mix"][0] + 2.6, 6.8,
                               fill=False, ec=INK_2, lw=0.9, ls=(0, (4, 3))))
    ax.text(X["mix"][0] - 1.1, 40.2, "«demodulator» della slide 5 (demodula e decide)", fontsize=8.5, color=INK_2)
    ax.text(X["bpf"][0] + 5, 16.5, "⋮", fontsize=14, ha="center", va="center", color=INK_2)
    ax.text(50, 16.5, "⋮", fontsize=14, ha="center", va="center", color=INK_2)
    # P/S e uscita
    ax.add_patch(FancyBboxPatch((84, 6), 6.5, 32, boxstyle="round,pad=0,rounding_size=0.6", fc=SURFACE, ec=INK_2, lw=1.2))
    ax.text(87.25, 22, "P/S", ha="center", va="center", fontsize=11)
    fr(90.5, 22, 96, 22)
    ax.text(97, 22, "$\\hat d[\\ell]$", va="center", fontsize=11)
    # segnali sul ramo evidenziato, numerati come i pannelli sotto
    y = 24
    seg = [((4.6, X["bpf"][0]), "①", "$y(t)$"),
           ((X["bpf"][0] + X["bpf"][1], X["mix"][0]), "②", f"$y_{i1}(t)$"),
           ((X["mix"][0] + X["mix"][1], X["mf"][0]), "③", f"$v_{i1}(t)$"),
           ((X["mf"][0] + X["mf"][1], X["cam"][0]), "④", f"$z_{i1}(t)$"),
           ((X["cam"][0] + X["cam"][1], X["dec"][0]), "⑤", f"$r_{i1}[m]$"),
           ((X["dec"][0] + X["dec"][1], X["dem"][0]), "⑥", f"$\\hat a_{i1}[m]$"),
           ((X["dem"][0] + X["dem"][1], 84), "", f"$\\hat d_{i1}(m)$")]
    for (x0, x1), num, lab in seg:
        xm = (x0 + x1) / 2
        ax.text(xm, y - 3.8, f"{num} {lab}".strip(), ha="center", va="top", fontsize=9.5, color=BLU)
    ax.set_title(f"Ricevitore FDM convenzionale: come si trasforma il segnale lungo un ramo (esempio: N = {N}, QPSK, ramo i = {i1})",
                 fontsize=11.5, loc="left", weight="bold")

    # ---- pannelli: il segnale del ramo i1 nei punti ①–⑥
    f = np.linspace(-4.2, 4.2, 3000)                                    # frequenza in unità di 1/T
    centri = (np.arange(N) - (N - 1) / 2) * 1.8                         # sottobande separate da guardie
    rumore = 0.07
    p = [fig.add_subplot(gs[1, k]) for k in range(6)]
    for i, c0 in enumerate(centri):
        p[0].fill_between(f, _rc(f - c0) + rumore, rumore, color=chiaro_fdm(RAMI_FDM[i]), lw=0)
        p[0].plot(f, _rc(f - c0) + rumore, color=RAMI_FDM[i], lw=1.3)
    p[0].axhline(rumore, color=INK_2, lw=.8, ls=":")
    p[0].set_title("① $|Y(f)|^2$: tutti i rami\n+ rumore", fontsize=9)
    p[0].set_xticks(centri), p[0].set_xticklabels([f"$f_{i}$" for i in range(N)], fontsize=8)
    filtro = (abs(f - centri[i1]) <= 0.75)
    band = _rc(f - centri[i1]) * filtro + rumore * filtro
    p[1].fill_between(f, band, color=chiaro_fdm(RAMI_FDM[i1]), lw=0)
    p[1].plot(f, band, color=RAMI_FDM[i1], lw=1.3)
    p[1].plot(f, 1.15 * filtro, color=INK_2, lw=.9, ls="--")
    p[1].set_title(f"② dopo il passa-banda:\nresta solo la banda di $f_{i1}$", fontsize=9)
    p[1].set_xticks(centri), p[1].set_xticklabels([f"$f_{i}$" for i in range(N)], fontsize=8)
    band0 = np.interp(f + centri[i1], f, band, left=0, right=0)
    p[2].fill_between(f, band0, color=chiaro_fdm(RAMI_FDM[i1]), lw=0)
    p[2].plot(f, band0, color=RAMI_FDM[i1], lw=1.3)
    p[2].set_title("③ dopo il mixer:\nriportato in banda base", fontsize=9)
    p[2].set_xticks([0]), p[2].set_xticklabels(["0"], fontsize=8)
    for g in p[:3]:
        g.set_xlim(-4.2, 4.2), g.set_ylim(0, 1.3), g.set_yticks([]), g.set_xlabel("$f$", fontsize=8, labelpad=1)
    # ④ uscita del filtro adattato e campioni: z(mT) = a[m] + w[m] (impulso complessivo di Nyquist)
    M = 10
    a = (rng.choice([-1, 1], M) + 1j * rng.choice([-1, 1], M))
    w = sigma * (rng.standard_normal(M) + 1j * rng.standard_normal(M))
    r = a + w
    t = np.linspace(-0.5, M - 0.5, 2000)
    z = sum(r[m] * _rc_t(t - m) for m in range(M))
    p[3].plot(t, z.real, color=RAMI_FDM[i1], lw=1.3)
    p[3].plot(np.arange(M), r.real, "o", color=INK, ms=3.5)
    p[3].axhline(0, color=INK_2, lw=.7)
    p[3].set_title("④ filtro adattato (parte reale)\ne campioni in $t=mT$", fontsize=9)
    p[3].set_xticks([0, 3, 6, 9]), p[3].set_xticklabels(["0", "$3T$", "$6T$", "$9T$"], fontsize=8)
    p[3].set_yticks([-1, 0, 1]), p[3].tick_params(labelsize=8)
    # ⑤ statistiche di decisione: simbolo + rumore, nuvole attorno ai punti QPSK
    nuv = rng.choice([-1, 1], (400, 2)) @ np.array([1, 1j]) + sigma * (rng.standard_normal(400) + 1j * rng.standard_normal(400))
    p[4].plot(nuv.real, nuv.imag, ".", color=chiaro_fdm(RAMI_FDM[i1], .55), ms=3)
    p[4].plot(r.real, r.imag, ".", color=RAMI_FDM[i1], ms=5)
    p[4].plot([1, 1, -1, -1], [1, -1, 1, -1], "x", color=INK, ms=7, mew=2)
    p[4].axhline(0, color=INK_2, lw=.8), p[4].axvline(0, color=INK_2, lw=.8)
    p[4].set_title(f"⑤ $r_{i1}[m]=a_{i1}[m]+w_{i1}[m]$\nsimbolo + rumore", fontsize=9)
    p[4].set_aspect("equal"), p[4].set_xlim(-2.2, 2.2), p[4].set_ylim(-2.2, 2.2)
    p[4].set_xticks([-1, 1]), p[4].set_yticks([-1, 1]), p[4].tick_params(labelsize=8)
    # ⑥ decisione (quadrante) e demapping Gray: bit b0 dal segno della parte reale, b1 dall'immaginaria
    ah = np.sign(r.real) + 1j * np.sign(r.imag)
    p[5].axis("off")
    p[5].set_title("⑥ decisione e demapper\n(primi 4 simboli)", fontsize=9)
    cols = ["$m$", f"$r_{i1}[m]$", f"$\\hat a_{i1}[m]$", f"$\\hat d_{i1}(m)$"]
    xs = [0.04, 0.34, 0.68, 0.93]
    for x, c in zip(xs, cols):
        p[5].text(x, 0.92, c, fontsize=9, ha="center", va="center", transform=p[5].transAxes, color=INK_2)
    p[5].plot([0, 1], [0.84, 0.84], color=GRID, lw=1, transform=p[5].transAxes)
    for m in range(4):
        yy = 0.74 - m * 0.13
        vals = [f"{m}", f"{r[m].real:+.1f}{r[m].imag:+.1f}j", f"{int(ah[m].real):+d}{int(ah[m].imag):+d}j",
                f"{int(ah[m].real < 0)}{int(ah[m].imag < 0)}"]
        for j, (x, v) in enumerate(zip(xs, vals)):
            p[5].text(x, yy, v, fontsize=9, ha="center", va="center", transform=p[5].transAxes,
                      color=ROSSO if (j == 2 and ah[m] != a[m]) else (BLU if j == 3 else INK))
    p[5].text(0.0, 0.16, "decisore: il quadrante di $r$\ndemapper (Gray): bit $0$ se la\ncomponente è $>0$, $1$ se è $<0$",
              fontsize=8, transform=p[5].transAxes, color=INK_2, va="top")
    fig.savefig(OUT / "grafico-l15-ricevitore-fdm-flusso.png")
    plt.close(fig)
    return int((ah != a).sum()), M


RAMI_FDM = [BLU, ARANCIO, ACQUA, VIOLA]


def chiaro_fdm(c, a=0.3):
    r = matplotlib.colors.to_rgb(c)
    s = matplotlib.colors.to_rgb(SURFACE)
    return tuple(a * x + (1 - a) * y for x, y in zip(r, s))


def due_ortogonalita(N=4, blocchi=3, k=3, i=1, n=1, campioni=2000):
    """Le due ortogonalità della biortogonalità (slide 8-9, appunti p. 13-14), con T_u = 1 e
    phi_k(t - n T_u) = R_Tu(t - n T_u) exp(j 2 pi k (t - n T_u) / T_u).
    In alto il tempo (delta_{n-m}), in basso la frequenza (delta_{k-i}), a destra la matrice dei prodotti scalari."""
    dt = 1 / campioni
    t = np.arange(0, blocchi, dt)

    def phi(kk, nn):
        finestra = ((t >= nn) & (t < nn + 1)).astype(float)
        return finestra * np.exp(2j * np.pi * kk * (t - nn))

    # matrice di Gram: righe e colonne ordinate per (blocco, sottoportante)
    base = np.array([phi(kk, nn) for nn in range(blocchi) for kk in range(N)])
    G = base @ base.conj().T * dt

    fig = plt.figure(figsize=(13.6, 7.6))
    gs = fig.add_gridspec(2, 3, width_ratios=[1.25, 1.25, 1.15], hspace=0.85, wspace=0.42)
    col = {"k": BLU, "i": ARANCIO}

    def assi(ax, x0, x1, ylim):
        ax.set_xlim(x0, x1), ax.set_ylim(*ylim)
        ax.grid(False), ax.axhline(0, color=INK_2, lw=0.8)
        for b in range(blocchi + 1):
            ax.axvline(b, color=GRID, lw=1, ls="--", zorder=0)
        ax.set_xlabel(r"$t/T_u$")

    # ---- ① tempo: stessa sottoportante, blocchi diversi
    m = n + 1
    rit = lambda q: "T_u" if q == 1 else f"{q}T_u"
    a1 = fig.add_subplot(gs[0, 0])
    assi(a1, 0, blocchi, (-1.6, 1.9))
    a1.plot(t, phi(i, n).real, color=col["k"])
    a1.plot(t, phi(i, m).real, color=col["i"])
    a1.text(n + 0.5, 1.12, rf"Re $\phi_{i}(t-{rit(n)})$", ha="center", color=col["k"], fontsize=9)
    a1.text(m + 0.5, 1.12, rf"Re $\phi_{i}(t-{rit(m)})$", ha="center", color=col["i"], fontsize=9)
    for b in range(blocchi):
        a1.text(b + 0.5, 1.62, f"blocco {b}", ha="center", color=INK_2, fontsize=8.5)
    a1.set_title("Le due forme d'onda: stessa sottoportante,\nblocchi diversi", fontsize=10)

    a2 = fig.add_subplot(gs[0, 1])
    assi(a2, 0, blocchi, (-1.6, 1.9))
    a2.axvspan(n, n + 1, color=chiaro_fdm(col["k"], 0.18), lw=0)
    a2.axvspan(m, m + 1, color=chiaro_fdm(col["i"], 0.18), lw=0)
    prod_t = phi(i, n) * phi(i, m).conj()
    a2.plot(t, prod_t.real, color=ROSSO, lw=2.6)
    a2.text(n + 0.5, 1.0, "qui c'è solo\nil blocco $n$", ha="center", color=col["k"], fontsize=8.5)
    a2.text(m + 0.5, 1.0, "qui c'è solo\nil blocco $m$", ha="center", color=col["i"], fontsize=8.5)
    a2.text(1.5, -1.05, r"prodotto $\phi_i(t-nT_u)\,\phi_i^\ast(t-mT_u)\equiv 0$", ha="center", color=ROSSO, fontsize=9)
    a2.set_title("Il prodotto è nullo ovunque: le finestre\nnon si sovrappongono", fontsize=10)
    a2.text(1.5, -2.95, r"$\Rightarrow\ \langle\cdot,\cdot\rangle=0$ per $n\neq m$, anche se $k=i$:  niente ISI",
            ha="center", color=INK, fontsize=9.5, transform=a2.transData)

    # ---- ② frequenza: stesso blocco, sottoportanti diverse
    b1 = fig.add_subplot(gs[1, 0])
    assi(b1, n - 0.15, n + 1.15, (-1.6, 1.9))
    b1.plot(t, phi(k, n).real, color=col["k"], label=rf"Re $\phi_{k}(t-{rit(n)})$  ($k={k}$: {k} periodi)")
    b1.plot(t, phi(i, n).real, color=col["i"], label=rf"Re $\phi_{i}(t-{rit(n)})$  ($i={i}$: {i} periodo)")
    b1.legend(loc="lower center", bbox_to_anchor=(0.5, -0.5), ncol=1, fontsize=8.5)
    b1.set_title("Le due forme d'onda: stesso blocco,\nsottoportanti diverse (sovrapposte)", fontsize=10)

    b2 = fig.add_subplot(gs[1, 1])
    assi(b2, n - 0.15, n + 1.15, (-1.6, 1.9))
    prod_f = (phi(k, n) * phi(i, n).conj()).real
    dentro = (t >= n) & (t < n + 1)
    b2.fill_between(t, 0, prod_f, where=dentro & (prod_f > 0), color=chiaro_fdm(BLU, 0.45), lw=0)
    b2.fill_between(t, 0, prod_f, where=dentro & (prod_f < 0), color=chiaro_fdm(ROSSO, 0.45), lw=0)
    b2.plot(t, prod_f, color=INK, lw=1.8)
    b2.plot([n, n + 1], [1, 1], color=INK_2, lw=1.3, ls="--")
    b2.text(n + 0.5, 1.12, r"per $k=i$: $|\phi_i|^2=1/T_u$, area 1 (energia unitaria)",
            ha="center", color=INK_2, fontsize=8.3)
    b2.set_title(rf"Re$[\phi_k\phi_i^\ast]=\cos(2\pi(k-i)t/T_u)/T_u$: $k-i={k-i}$" + "\nperiodi interi, aree + e − uguali",
                 fontsize=10)
    b2.text(n + 0.5, -2.95, r"$\Rightarrow\ \int_{T_u}\phi_k\phi_i^\ast\,dt=0$ per $k\neq i$:  niente ICI",
            ha="center", color=INK, fontsize=9.5)

    fig.text(0.02, a1.get_position().y1 + 0.085, r"①  Ortogonalità nel tempo, fattore $\delta_{n-m}$", fontsize=12.5, weight="bold", color=INK)
    fig.text(0.02, b1.get_position().y1 + 0.085, r"②  Ortogonalità in frequenza, fattore $\delta_{k-i}$", fontsize=12.5, weight="bold", color=INK)

    # ---- ③ matrice dei prodotti scalari
    c = fig.add_subplot(gs[:, 2])
    c.grid(False)
    c.imshow(np.abs(G), cmap="Greys", vmin=0, vmax=1.25)
    L = N * blocchi
    for b in range(1, blocchi):
        c.axhline(b * N - 0.5, color=INK_2, lw=1.2), c.axvline(b * N - 0.5, color=INK_2, lw=1.2)
    for b in range(blocchi):                                     # blocchi diagonali: stesso n, qui agisce delta_{k-i}
        c.add_patch(Rectangle((b * N - 0.5, b * N - 0.5), N, N, fill=False, ec=BLU, lw=2.2))
    for r in range(L):
        for s in range(L):
            c.text(s, r, f"{abs(G[r, s]):.0f}", ha="center", va="center", fontsize=6.8,
                   color=SURFACE if r == s else (BLU if r // N == s // N else ARANCIO))
    etichette = [f"{kk}" for nn in range(blocchi) for kk in range(N)]
    c.set_xticks(range(L), etichette, fontsize=7), c.set_yticks(range(L), etichette, fontsize=7)
    for b in range(blocchi):
        c.text(b * N + (N - 1) / 2, -1.1, f"$m={b}$", ha="center", fontsize=9)
        c.text(-1.9, b * N + (N - 1) / 2, f"$n={b}$", va="center", ha="right", fontsize=9)
    c.set_xlabel(r"sottoportante $i$ (raggruppate per blocco $m$)", fontsize=9)
    c.set_ylabel(r"sottoportante $k$ (raggruppate per blocco $n$)", fontsize=9, labelpad=36)
    c.set_title(r"③  Le due insieme: $|\langle\phi_k(t-nT_u),\phi_i(t-mT_u)\rangle|$" + "\n"
                f"calcolati numericamente, N = {N}, {blocchi} blocchi", fontsize=10, pad=30)
    c.text((L - 1) / 2, L + 1.3,
           "diagonale: 1 (energia unitaria)\n"
           "zeri blu, dentro i riquadri: stesso blocco, k ≠ i → δ$_{k-i}$ (no ICI)\n"
           "zeri arancioni, fuori dai riquadri: blocchi diversi → δ$_{n-m}$ (no ISI)\n"
           "risultato: matrice identità = biortogonalità",
           ha="center", va="top", fontsize=8.8, color=INK)
    for sp in c.spines.values():
        sp.set_visible(False)

    fig.savefig(OUT / "grafico-l15-due-ortogonalita.png")
    plt.close(fig)
    return G


if __name__ == "__main__":
    G = due_ortogonalita()
    assert np.allclose(G, np.eye(len(G)), atol=1e-9), np.abs(G - np.eye(len(G))).max()   # biortogonalità
    errori, simboli = ricevitore_fdm()
    print("ricevitore FDM:", errori, "errori su", simboli)
    centro = psd_ofdm()
    assert 0.9 < centro < 1.1, centro                      # la somma delle sinc^2 è circa 1 dentro la banda
    utile, ici = ici_cfo()
    assert np.allclose(utile + ici, 1)                     # Parseval: la potenza si ripartisce, non si perde
    assert np.isclose(utile[0], 1) and np.isclose(ici[0], 0)
    papr_ccdf()
    print("ok", round(float(centro), 3), "eps=0.1 ->", round(float(10*np.log10(utile[80]/ici[80])), 1), "dB")
