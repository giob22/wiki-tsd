"""Grafici di funzione per la lezione "Campionamento e conversione A/D e D/A".

Nessun grafico riproduce una figura delle slide: sono tutti generati dalle
formule presenti in Campionamento_AD_DA.pdf, come supporto alla comprensione.
Uso: python genera_grafici_campionamento.py  (richiede numpy, scipy, matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.special import erfc

OUT = Path(__file__).parent

# Palette validata (dataviz: categorical light + ordinal blue ramp)
SURFACE = "#fcfcfb"
INK = "#1f1f1e"
INK_2 = "#5f5e57"
GRID = "#e4e3dc"
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]          # blu, arancio, acqua
ORD = ["#86b6ef", "#2a78d6", "#104281"]          # chiaro -> scuro

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


# 1. pdf di Laplace per diversi lambda  (p.32)
def laplace_lambda():
    x = np.linspace(-4, 4, 801)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for lam, c in zip([0.5, 1.0, 2.0], ORD):
        y = lam / 2 * np.exp(-lam * np.abs(x))
        ax.plot(x, y, color=c, label=fr"$\lambda={lam:g}$  ($x_{{rms}}={np.sqrt(2)/lam:.2f}$)")
    ax.set_xlabel("ampiezza $x$")
    ax.set_ylabel("$f_X(x)$")
    ax.set_title(r"pdf di Laplace $f_X(x)=\frac{\lambda}{2}e^{-\lambda|x|}$", loc="left")
    ax.legend(loc="upper right")
    ax.set_ylim(0, 1.05)
    save(fig, "grafico-laplace-pdf-lambda.png")


# 2. Laplace vs Gaussiana vs Uniforme a parita' di potenza (varianza 1)
def laplace_confronto():
    x = np.linspace(-4, 4, 801)
    lap = np.sqrt(2) / 2 * np.exp(-np.sqrt(2) * np.abs(x))
    gau = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
    uni = np.where(np.abs(x) <= np.sqrt(3), 1 / (2 * np.sqrt(3)), 0.0)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(x, lap, color=CAT[0], label="Laplace (voce)")
    ax.plot(x, gau, color=CAT[1], ls="--", label="Gaussiana")
    ax.plot(x, uni, color=CAT[2], ls=":", label="Uniforme")
    ax.annotate("picco in 0:\nampiezze piccole\npiù probabili", xy=(0, 0.707), xytext=(0.9, 0.6),
                color=INK_2, fontsize=9, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    ax.set_xlabel(r"ampiezza $x$ (in unità di $x_{rms}$)")
    ax.set_ylabel("$f_X(x)$")
    ax.set_title("Tre pdf con la stessa potenza ($E[x^2]=1$)", loc="left")
    ax.legend(loc="upper left")
    save(fig, "grafico-laplace-gauss-uniforme.png")


# 3. Quantizzatore di Lloyd-Max per Laplace (varianza 1), M = 8
def lloyd_max_laplace(M=8, iters=500):
    lam = np.sqrt(2)
    f = lambda x: lam / 2 * np.exp(-lam * abs(x))
    q = np.linspace(-2.5, 2.5, M)                      # livelli iniziali
    for _ in range(iters):
        t = np.concatenate(([-np.inf], (q[:-1] + q[1:]) / 2, [np.inf]))   # punto medio
        q_new = np.array([integrate.quad(lambda x: x * f(x), t[i], t[i + 1])[0] /
                          integrate.quad(f, t[i], t[i + 1])[0] for i in range(M)])  # centroide
        if np.max(abs(q_new - q)) < 1e-9:
            q = q_new
            break
        q = q_new
    t = (q[:-1] + q[1:]) / 2
    mse = sum(integrate.quad(lambda x: (q[i] - x) ** 2 * f(x),
                             -np.inf if i == 0 else t[i - 1], np.inf if i == M - 1 else t[i])[0]
              for i in range(M))
    return q, t, mse


def lloyd_max_plot():
    q, t, mse = lloyd_max_laplace()
    x = np.linspace(-6, 6, 1201)
    lam = np.sqrt(2)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(x, lam / 2 * np.exp(-lam * np.abs(x)), color=CAT[0], label="pdf di Laplace ($x_{rms}=1$)")
    for i, ti in enumerate(t):
        ax.axvline(ti, color=INK_2, lw=0.9, ls="--", label="soglie $x_i$ (punti medi)" if i == 0 else None)
    ax.plot(q, np.zeros_like(q), "o", ms=8, color=CAT[1], mec=SURFACE, mew=2, clip_on=False,
            label="livelli $q_i$ (centroidi)")
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 0.75)
    ax.set_xlabel("ampiezza $x$")
    ax.set_ylabel("$f_X(x)$")
    snr = 10 * np.log10(1 / mse)
    ax.set_title(f"Lloyd-Max, M = 8, pdf di Laplace: intervalli stretti al centro, larghi sulle code"
                 f"  (SNR ≈ {snr:.1f} dB)", loc="left", fontsize=9.5)
    ax.legend(loc="upper right", fontsize=9)
    save(fig, "grafico-lloyd-max-laplace.png")
    print("  livelli:", np.round(q, 3), "\n  soglie:", np.round(t, 3), f"\n  MSE={mse:.5f}, SNR={snr:.2f} dB")


# 4. SNR_dB vs b per diversi k_c (legge dei 6 dB/bit, p.30-31)
def snr_vs_bit():
    b = np.arange(1, 17)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    for kc, c in zip([2, 4, 8], ORD):
        snr = 6.02 * b - 20 * np.log10(kc) + 4.77
        ax.plot(b, snr, "o-", color=c, ms=4, label=fr"$k_c={kc}$")
        ax.text(16.3, snr[-1], fr"$k_c={kc}$", color=INK, va="center", fontsize=9)
    ax.axhline(85, color=INK_2, lw=0.9, ls=":")
    ax.text(1.2, 86.5, "obiettivo Es. 7.6: 85 dB", color=INK_2, fontsize=9)
    ax.plot([16], [6.02 * 16 - 12.04 + 4.77], "o", ms=9, color=ORD[1], mec=INK, mew=1.2)
    ax.annotate("b = 16 → 89.1 dB", xy=(16, 89.05), xytext=(11.2, 96), fontsize=9, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    ax.set_xlabel("bit per campione $b$")
    ax.set_ylabel(r"$\mathrm{SNR}_{dB}$")
    ax.set_title(r"$\mathrm{SNR}_{dB}=6.02\,b-[k_c]_{dB}+4.77$: +6 dB per bit", loc="left")
    ax.set_xlim(0.5, 17.8)
    ax.legend(loc="lower right")
    save(fig, "grafico-snr-vs-bit.png")


# 5. Errore di quantizzazione su una sinusoide (b = 3, X_max = 1)
def errore_sinusoide():
    b, Xmax = 3, 1.0
    M = 2 ** b
    D = 2 * Xmax / M
    n = np.arange(0, 64)
    x = 0.9 * np.sin(2 * np.pi * n / 32)
    xq = np.clip((np.floor(x / D) + 0.5) * D, -Xmax + D / 2, Xmax - D / 2)
    e = xq - x
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 4.6), sharex=True, height_ratios=[2, 1])
    a1.plot(n, x, color=CAT[0], label="$x(n)$")
    a1.step(n, xq, where="mid", color=CAT[1], label="$x_q(n)$")
    a1.set_ylabel("ampiezza")
    a1.set_title(f"Quantizzazione uniforme, b = {b} (M = {M}), Δ = {D:g}", loc="left")
    a1.legend(loc="upper right", ncol=2)
    a2.plot(n, e, color=CAT[2], marker="o", ms=3)
    for s in (-D / 2, D / 2):
        a2.axhline(s, color=INK_2, lw=0.9, ls="--")
    a2.text(64.5, D / 2, r"$+\Delta/2$", va="center", fontsize=9)
    a2.text(64.5, -D / 2, r"$-\Delta/2$", va="center", fontsize=9)
    a2.set_ylabel("$e(n)$")
    a2.set_xlabel("$n$")
    save(fig, "grafico-errore-quantizzazione.png")


# 6. Limite di Chebyshev vs probabilita' esatte di sovraccarico (p.29)
def chebyshev():
    kc = np.linspace(1, 6, 300)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.semilogy(kc, 1 / kc**2, color=CAT[0], label=r"Chebyshev $1/k_c^2$ (qualunque pdf)")
    ax.semilogy(kc, np.exp(-np.sqrt(2) * kc), color=CAT[1], ls="--", label=r"Laplace esatta $e^{-\sqrt{2}k_c}$")
    ax.semilogy(kc, erfc(kc / np.sqrt(2)), color=CAT[2], ls=":", label=r"Gaussiana esatta $2Q(k_c)$")
    ax.axvline(4, color=INK_2, lw=0.9)
    ax.text(4.08, 0.2, "four-sigma\nloading", color=INK_2, fontsize=9)
    ax.plot([4], [1 / 16], "o", ms=7, color=CAT[0], mec=SURFACE, mew=2)
    ax.annotate("6.25%", xy=(4, 1 / 16), xytext=(4.5, 0.08), fontsize=9,
                arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    ax.set_xlabel("fattore di carico $k_c = X_{max}/x_{rms}$")
    ax.set_ylabel(r"$P_s = P(|x|>X_{max})$")
    ax.set_title("Probabilità di sovraccarico: limite di Chebyshev e valori esatti", loc="left")
    ax.legend(loc="lower left", fontsize=9)
    save(fig, "grafico-chebyshev-sovraccarico.png")


# 7. |H_r(f)| degli interpolatori (p.17, 23, 24)
def interpolatori():
    u = np.linspace(0, 3, 1201)                        # u = f*T_c = f/f_c
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(u, np.where(u < 0.5, 1.0, 0.0), color=CAT[0], label="ideale  $T_c\\,\\Pi(fT_c)$")
    ax.plot(u, np.abs(np.sinc(u)), color=CAT[1], ls="--", label="ZOH  $T_c|\\mathrm{sinc}(fT_c)|$")
    ax.plot(u, np.sinc(u) ** 2, color=CAT[2], ls=":", label="FOH  $T_c\\,\\mathrm{sinc}^2(fT_c)$")
    for v, lab in [(0.5, "$f_c/2$"), (1, "$f_c$"), (2, "$2f_c$")]:
        ax.axvline(v, color=GRID, lw=1.2, zorder=0)
        ax.text(v, 1.07, lab, ha="center", color=INK_2, fontsize=9)
    ax.set_xlabel("frequenza normalizzata $f\\,T_c = f/f_c$")
    ax.set_ylabel("$|H_r(f)|\\,/\\,T_c$")
    ax.set_ylim(0, 1.13)
    ax.set_title("Risposta in ampiezza dei filtri di ricostruzione", loc="left", pad=16)
    ax.legend(loc="upper right")
    save(fig, "grafico-interpolatori-risposta.png")


# 8. SNR vs livello d'ingresso: uniforme, mu-law, A-law (b = 8, ingresso Laplace, p.39-43)
def snr_vs_livello(b=8, mu=255.0, A=87.6):
    M = 2 ** b
    Xmax = 1.0
    lev = np.linspace(-50, 0, 201)                     # 20 log10(x_rms / X_max)
    sig = Xmax * 10 ** (lev / 20)
    uni = 10 * np.log10(3 * M**2 * sig**2 / Xmax**2)
    # mu-law: 1/F'(x) = ln(1+mu)/mu * (1 + mu|x|/Xmax);  E|x| = sig/sqrt(2) (Laplace)
    Eg = 1 + 2 * mu * (sig / np.sqrt(2)) / Xmax + mu**2 * sig**2 / Xmax**2
    mse_mu = Xmax**2 / (3 * M**2) * (np.log(1 + mu) / mu) ** 2 * Eg
    mul = 10 * np.log10(sig**2 / mse_mu)
    # A-law: 1/F'^2 = (1+lnA)^2 * g,  g = 1/A^2 per |x|<Xmax/A,  x^2/Xmax^2 altrimenti
    a = Xmax / A
    lam = np.sqrt(2) / sig
    p_in = 1 - np.exp(-lam * a)
    tail = np.exp(-lam * a) * (a**2 + 2 * a / lam + 2 / lam**2) / Xmax**2
    mse_A = Xmax**2 / (3 * M**2) * (1 + np.log(A)) ** 2 * (p_in / A**2 + tail)
    alaw = 10 * np.log10(sig**2 / mse_A)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(lev, uni, color=CAT[0], label="uniforme")
    ax.plot(lev, mul, color=CAT[1], ls="--", label=r"legge $\mu$ ($\mu=255$)")
    ax.plot(lev, alaw, color=CAT[2], ls=":", label="legge A (A = 87.6)")
    ax.axhline(6.02 * b - 10.11, color=GRID, lw=1.2, zorder=0)
    ax.text(-49.5, 6.02 * b - 10.11 + 1, r"$6.02b-10.11$", color=INK_2, fontsize=9)
    ax.set_xlabel(r"livello relativo d'ingresso $20\log_{10}(x_{rms}/X_{max})$ [dB]")
    ax.set_ylabel(r"$\mathrm{SNR}_{dB}$")
    ax.set_ylim(0, 60)
    ax.set_title(f"b = {b} bit, ingresso di Laplace (sovraccarico trascurato)", loc="left")
    ax.legend(loc="lower right")
    save(fig, "grafico-snr-vs-livello-companding.png")
    for L in (-40, -20, -12, -4.77):
        i = np.argmin(abs(lev - L))
        print(f"  livello {lev[i]:6.1f} dB: uni {uni[i]:5.1f}  mu {mul[i]:5.1f}  A {alaw[i]:5.1f}")


RED = "#e34948"                                    # rosso della palette: come la sinusoide alias della slide
RAMP4 = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]  # rampa ordinale (intervalli j = 1..4)


# 9. Idea chiave del companding: soglie uniformi su F(x) -> soglie non uniformi su x (p.36, 38, 41)
def companding_soglie(mu=255.0, M=8):
    Xmax = 1.0
    F = lambda x: Xmax * np.log1p(mu * x / Xmax) / np.log1p(mu)        # legge mu, x >= 0
    Finv = lambda y: Xmax / mu * ((1 + mu) ** (y / Xmax) - 1)           # espansore
    D = 2 * Xmax / M
    yj = D * np.arange(M // 2 + 1)                                      # soglie uniformi (asse y)
    xj = Finv(yj)                                                       # soglie equivalenti (asse x)
    Qu = lambda y: np.clip((np.floor(y / D) + 0.5) * D, D / 2, Xmax - D / 2)
    x = np.linspace(0, Xmax, 4001)
    bar = -0.045                                                        # quota delle barre colorate
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.8))

    # (a) compressore: le soglie uniformi su y ricadono su x attraverso la curva
    a1.plot(x, x, color=INK_2, lw=1, ls=":", label=r"$F(x)=x$ (senza compressione)")
    a1.plot(x, F(x), color=CAT[1], label=r"$F(x)$, legge $\mu$ ($\mu=255$)")
    for j in range(1, M // 2 + 1):
        a1.plot([0, xj[j]], [yj[j]] * 2, color=INK_2, lw=0.8, ls="--")
        a1.plot([xj[j]] * 2, [0, yj[j]], color=INK_2, lw=0.8, ls="--")
        a1.plot([bar] * 2, [yj[j - 1], yj[j]], color=RAMP4[j - 1], lw=9, solid_capstyle="butt")
        a1.plot([xj[j - 1], xj[j]], [bar] * 2, color=RAMP4[j - 1], lw=9, solid_capstyle="butt")
    for v in yj[1:-1]:                                                  # separatori tra le barre
        a1.plot([bar - 0.02, bar + 0.02], [v] * 2, color=SURFACE, lw=2)
    for v in xj[1:-1]:
        a1.plot([v] * 2, [bar - 0.02, bar + 0.02], color=SURFACE, lw=2)
    a1.text(0.36, 0.03, "soglie su $y$: 0.25, 0.5, 0.75, 1  (passo $\\Delta$)\n"
                        "soglie su $x$: 0.012, 0.059, 0.247, 1  (×4)",
            fontsize=8.5, color=INK, va="bottom")
    a1.set_xlim(-0.08, 1.03)
    a1.set_ylim(-0.08, 1.05)
    a1.set_xlabel(r"$x\,/\,X_{max}$")
    a1.set_ylabel(r"$y = F(x)\,/\,X_{max}$")
    a1.set_title(r"Compressore: soglie uguali su $y$ → soglie diverse su $x$", loc="left", fontsize=10)
    a1.legend(loc="upper left", bbox_to_anchor=(0.1, 0.93), fontsize=9)

    # (b) catena completa compressore -> quantizzatore uniforme -> espansore
    a2.plot(x, x, color="#c9c8c0", lw=1, ls=":", label=r"$Q(x) = x$")
    a2.plot(x, Qu(x), color=INK_2, lw=1.4, ls="--", label=r"uniforme, $M = 8$")
    a2.plot(x, Finv(Qu(F(x))), color=CAT[1], lw=2, label=r"companding, legge $\mu$, $M = 8$")
    for j in range(1, M // 2 + 1):
        a2.plot([xj[j - 1], xj[j]], [bar] * 2, color=RAMP4[j - 1], lw=9, solid_capstyle="butt")
    for v in xj[1:-1]:
        a2.plot([v] * 2, [bar - 0.02, bar + 0.02], color=SURFACE, lw=2)
    a2.annotate("gradini fitti vicino a 0", xy=(0.04, 0.05), xytext=(0.30, 0.13), fontsize=9,
                color=INK, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    a2.annotate("un solo gradino\nda 0.247 a 1", xy=(0.86, Finv(Qu(F(0.86)))), xytext=(0.76, 0.30),
                fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    a2.set_xlim(-0.08, 1.03)
    a2.set_ylim(-0.08, 1.05)
    a2.set_xlabel(r"$x\,/\,X_{max}$")
    a2.set_ylabel(r"$Q(x)\,/\,X_{max}$")
    a2.set_title(r"Catena completa: $Q(x) = F^{-1}(Q_u(F(x)))$", loc="left", fontsize=10)
    a2.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    save(fig, "grafico-companding-soglie-mu.png")
    print("  soglie x_j:", np.round(xj, 4), "\n  livelli q_j:", np.round(Finv((np.arange(1, M // 2 + 1) - 0.5) * D), 4))


# 10. Frequenza ricostruita in funzione di f0: ripiegamento attorno a fc/2, fc = 2 kHz (p.18)
def aliasing_ripiegamento(fc=2.0):
    f0 = np.linspace(0, 5, 2001)                                        # kHz
    fr = np.abs(f0 - fc * np.round(f0 / fc))                            # replica che cade in [0, fc/2]
    fig, ax = plt.subplots(figsize=(7, 3.9))
    ax.axvspan(0, fc / 2, color="#f0efec", zorder=0)
    ax.text(fc / 4, 1.12, "nessun\naliasing", ha="center", color=INK_2, fontsize=9)
    for v, lab in [(fc / 2, r"$f_c/2$"), (fc, r"$f_c$"), (1.5 * fc, r"$3f_c/2$"), (2 * fc, r"$2f_c$")]:
        ax.axvline(v, color=GRID, lw=1.2, zorder=0)
        ax.text(v, 1.33, lab, ha="center", color=INK_2, fontsize=9)
    ax.plot([0, 1.3], [0, 1.3], color=INK_2, lw=1, ls=":", label=r"ricostruzione corretta ($= f_0$)")
    ax.plot(f0, fr, color=CAT[0], label="frequenza ricostruita")
    ax.axhline(0.5, color=RED, lw=0.9, ls="--", zorder=1)
    ax.plot([2.5, 3.5, 4.5], [0.5] * 3, "o", ms=8, color=INK_2, mec=SURFACE, mew=2, zorder=3)
    ax.plot([1.5], [0.5], "o", ms=10, color=RED, mec=SURFACE, mew=2, zorder=4)
    ax.annotate("esempio della slide:\n1.5 kHz → 0.5 kHz", xy=(1.5, 0.5), xytext=(1.55, 0.72),
                fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=INK_2, lw=0.8))
    ax.text(4.0, 0.68, "anche 2.5, 3.5,\n4.5 kHz → 0.5 kHz", ha="center", fontsize=9, color=INK)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.42)
    ax.set_xlabel(r"frequenza della sinusoide $f_0$ [kHz]")
    ax.set_ylabel("frequenza ricostruita [kHz]")
    ax.set_title(r"$f_c = 2$ kHz: la frequenza ricostruita si ripiega attorno a $f_c/2$", loc="left", pad=18)
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.93), fontsize=9)
    save(fig, "grafico-aliasing-ripiegamento.png")


# 11. Animazione: perche' il ricostruttore restituisce 0.5 kHz, nel tempo e in frequenza (p.12, 15, 17, 18)
def aliasing_animazione(f0=1.5, fc=2.0, fps=10, anteprima=None):
    """anteprima = (cartella, [frame, ...]): salva solo quei fotogrammi come PNG, senza la GIF."""
    from matplotlib.animation import FuncAnimation, PillowWriter
    Tc = 1 / fc                                                         # ms (frequenze in kHz)
    fa = abs(f0 - fc * np.round(f0 / fc))                               # 0.5 kHz
    t = np.linspace(0, 4, 1601)
    tn = np.arange(9) * Tc
    xn = np.cos(2 * np.pi * f0 * tn)
    repl = [r for r in np.arange(-3.5, 3.6, 1.0) if abs(abs(r) - f0) > 1e-9]   # repliche: +-0.5, +-2.5, +-3.5
    fasi = [20, 27, 20, 25, 25, 30]                                     # frame per passo
    testi = [
        ("Passo 1 · Il segnale analogico",
         r"coseno a $f_0 = 1.5$ kHz: nello spettro, due righe a $\pm 1.5$ kHz"),
        (r"Passo 2 · Campionamento a $f_c = 2$ kHz",
         r"un campione ogni $T_c = 0.5$ ms; lo spettro si replica ogni $f_c$: la riga a $-1.5$ kHz, spostata di $+f_c$, cade a $+0.5$ kHz"),
        ("Passo 3 · Restano solo i campioni",
         "tra un campione e l'altro il ricostruttore non sa nulla: vede solo 1, 0, −1, 0, 1, …"),
        ("Passo 4 · I campioni sono ambigui",
         "coseni a 0.5, 1.5, 2.5 kHz, … passano tutti per gli stessi punti"),
        ("Passo 5 · Il filtro di ricostruzione sceglie",
         r"LPF ideale con taglio $f_c/2 = 1$ kHz: passano solo le righe a $\pm 0.5$ kHz"),
        (r"Passo 6 · Uscita: coseno a $f_c - f_0 = 0.5$ kHz",
         r"è l'unico segnale con banda sotto $f_c/2$ che ha quei campioni; il coseno a 1.5 kHz è perso"),
    ]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.6, 6.6), height_ratios=[1.2, 1])
    fig.subplots_adjust(left=0.09, right=0.98, top=0.80, bottom=0.08, hspace=0.42)
    h1 = fig.text(0.02, 0.962, "", fontsize=12, weight="bold", color=INK)
    h2 = fig.text(0.02, 0.922, "", fontsize=9.5, color=INK_2)

    def fase(k):
        s = 0
        for i, L in enumerate(fasi):
            if k < s + L:
                return i + 1, (k - s) / (L - 1)
            s += L
        return len(fasi), 1.0

    def righe(ax, fs, color, alpha=1.0, lw=2):
        for f in fs:
            ax.plot([f, f], [0, 0.5], color=color, lw=lw, alpha=alpha, solid_capstyle="round")
            ax.plot([f], [0.5], "o", ms=8, color=color, alpha=alpha, mec=SURFACE, mew=2)

    def draw(k):
        p_i, p = fase(k)
        h1.set_text(testi[p_i - 1][0])
        h2.set_text(testi[p_i - 1][1])
        a1.clear()
        a2.clear()
        # --- tempo
        a_orig = 1.0 if p_i <= 2 else (1 - 0.85 * p if p_i == 3 else 0.15)
        t_end = 4 * p if p_i == 1 else 4
        m = t <= t_end
        a1.plot(t[m], np.cos(2 * np.pi * f0 * t[m]), color=INK, lw=1.8, alpha=a_orig, label="1.5 kHz (originale)")
        if p_i >= 4:
            q = min(1, 2 * p) if p_i == 4 else 1
            m2 = t <= 4 * q
            a1.plot(t[m2], np.cos(2 * np.pi * fa * t[m2]), color=RED, lw=2.4 if p_i >= 5 else 1.8,
                    ls="-" if p_i >= 5 else "--", label="0.5 kHz")
            if p_i == 4 and p > 0.5 or p_i == 5:
                q3 = min(1, 2 * p - 1) if p_i == 4 else 1
                a3 = 1.0 if p_i == 4 else 1 - 0.9 * p
                m3 = t <= 4 * q3
                a1.plot(t[m3], np.cos(2 * np.pi * (fc + fa) * t[m3]), color=INK_2, lw=1, alpha=a3, label="2.5 kHz")
        if p_i >= 2:
            ns = int(np.ceil(9 * p)) if p_i == 2 else 9
            a1.vlines(tn[:ns], 0, xn[:ns], color=INK, lw=1.2)
            a1.plot(tn[:ns], xn[:ns], "o", ms=9, color=INK, mec=SURFACE, mew=2, zorder=5, label="campioni $x(n)$")
        a1.axhline(0, color=INK_2, lw=0.6)
        a1.set_xlim(-0.1, 4.1)
        a1.set_ylim(-1.35, 1.35)
        a1.set_xticks(np.arange(0, 4.01, 0.5))
        a1.set_xlabel(r"$t$ [ms]   (le tacche sono gli istanti di campionamento $nT_c$)")
        a1.set_ylabel("ampiezza")
        a1.legend(loc="lower right", ncol=4, fontsize=8.5, bbox_to_anchor=(1.0, 1.0))
        # --- frequenza
        righe(a2, [-f0, f0], INK, alpha=1.0 if p_i <= 4 else 0.25)
        if p_i >= 2:
            near = [-fa, fa]
            far = [r for r in repl if abs(abs(r) - fa) > 1e-9]
            show_far = p_i > 2 or p > 0.5
            if p_i <= 4:
                righe(a2, near, INK_2)
                if show_far:
                    righe(a2, far, INK_2, alpha=0.8)
            else:
                righe(a2, near, RED)
                if p_i == 5:
                    righe(a2, far, INK_2, alpha=0.25)
            a2.text(fc / 2, 0.92, r"$+f_c/2$", ha="center", color=INK_2, fontsize=9)
            a2.text(-fc / 2, 0.92, r"$-f_c/2$", ha="center", color=INK_2, fontsize=9)
            if p_i <= 4:
                for v in (-fc / 2, fc / 2):
                    a2.plot([v, v], [0, 0.86], color=INK_2, lw=0.8, ls=":")
                # spostamenti delle due righe: -1.5 + fc = +0.5 e +1.5 - fc = -0.5 (frecce a quote diverse)
                a2.annotate("", xy=(fa, 0.62), xytext=(-f0, 0.62),
                            arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=1.1, shrinkA=0, shrinkB=0))
                a2.annotate("", xy=(-fa, 0.74), xytext=(f0, 0.74),
                            arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=1.1, shrinkA=0, shrinkB=0))
                a2.text(-f0 - 0.08, 0.62, r"$+f_c$", ha="right", va="center", color=INK, fontsize=9)
                a2.text(f0 + 0.08, 0.74, r"$-f_c$", ha="left", va="center", color=INK, fontsize=9)
        if p_i >= 5:
            a2.add_patch(plt.Rectangle((-fc / 2, 0), fc, 0.68, fill=True, facecolor="#eef4fc",
                                       edgecolor=CAT[0], lw=1.6, zorder=0))
            a2.text(0, 0.74, r"$H_r(f)$: passa solo $|f| < f_c/2$", ha="center", color=INK, fontsize=9)
        a2.set_xlim(-4.2, 4.2)
        a2.set_ylim(0, 1.02)
        a2.set_xticks(np.arange(-4, 4.01, 1))
        a2.set_yticks([])
        a2.set_xlabel(r"$f$ [kHz]")
        a2.set_ylabel("spettro (righe)")
        return []

    if anteprima:
        cartella, quali = anteprima
        for k in quali:
            draw(k)
            fig.savefig(f"{cartella}/anteprima-aliasing-{k:03d}.png", dpi=80, bbox_inches=None)
        plt.close(fig)
        return
    ani = FuncAnimation(fig, draw, frames=sum(fasi), blit=False)
    ani.save(OUT / "grafico-aliasing-animazione.gif", writer=PillowWriter(fps=fps), dpi=80)
    plt.close(fig)
    print("scritto grafico-aliasing-animazione.gif")


# 12. Animazione "stroboscopio": 270 gradi per campione equivalgono a -90 gradi per campione (p.18)
def aliasing_stroboscopio(f0=1.5, fc=2.0, fps=14, per_Tc=20, N=8, anteprima=None):
    """anteprima = (cartella, [k, ...]) con k = passo temporale (k / per_Tc campioni): solo PNG, niente GIF."""
    from matplotlib.animation import FuncAnimation, PillowWriter
    Tc = 1 / fc
    fa = fc - f0
    t = np.linspace(0, N * Tc, 1601)
    cc = np.linspace(0, 2 * np.pi, 361)
    seq = []                                                            # pausa sugli istanti di campionamento
    for k in range(N * per_Tc + 1):
        seq += [k] * (5 if k % per_Tc == 0 else 1)
    seq += [N * per_Tc] * 15
    fig = plt.figure(figsize=(10, 5.0))
    a1 = fig.add_axes([0.01, 0.04, 0.36, 0.76])
    a2 = fig.add_axes([0.45, 0.15, 0.53, 0.60])
    h1 = fig.text(0.02, 0.945, "", fontsize=11.5, weight="bold", color=INK)
    h2 = fig.text(0.02, 0.895, "", fontsize=9.5, color=INK_2)

    def draw(k):
        tt = k / per_Tc * Tc
        nmax = k // per_Tc
        su_campione = k % per_Tc == 0
        a1.clear()
        a2.clear()
        a1.set_aspect("equal")
        a1.axis("off")
        a1.plot(np.cos(cc), np.sin(cc), color=GRID, lw=1.2)
        a1.plot([-1.2, 1.2], [0, 0], color=GRID, lw=0.8)
        a1.plot([0, 0], [-1.2, 1.2], color=GRID, lw=0.8)
        pos = {}
        for m in range(nmax + 1):
            pos.setdefault(round(np.degrees(2 * np.pi * f0 * m * Tc)) % 360, []).append(m)
        for ang, ms in pos.items():
            r = np.radians(ang)
            a1.plot(np.cos(r), np.sin(r), "o", ms=10, color=INK, mec=SURFACE, mew=2, zorder=4)
            a1.text(1.42 * np.cos(r), 1.3 * np.sin(r), "n = " + ", ".join(map(str, ms)),
                    ha="center", va="center", fontsize=9, color=INK)
        thb = 2 * np.pi * f0 * tt
        thr = -2 * np.pi * fa * tt
        # rosso sotto e piu' spesso: quando i fasori coincidono resta visibile come bordo
        a1.annotate("", xy=(np.cos(thr), np.sin(thr)), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=3.4, mutation_scale=20))
        a1.annotate("", xy=(np.cos(thb), np.sin(thb)), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=14))
        a1.plot([np.cos(thb)] * 2, [0, np.sin(thb)], color=INK, lw=0.8, ls=":")
        a1.text(0, -1.62, "nero: fasore a 1.5 kHz, gira in senso antiorario\n"
                          "rosso: fasore a 0.5 kHz, gira in senso orario\n"
                          "valore del coseno = proiezione sull'asse orizzontale", ha="center", va="top",
                fontsize=8.5, color=INK)
        a1.set_xlim(-1.75, 1.75)
        a1.set_ylim(-2.25, 1.55)
        m = t <= tt + 1e-12
        a2.plot(t[m], np.cos(2 * np.pi * f0 * t[m]), color=INK, lw=1.8, label="1.5 kHz (originale)")
        a2.plot(t[m], np.cos(2 * np.pi * fa * t[m]), color=RED, lw=1.8, ls="--", label="0.5 kHz (stessi campioni)")
        tn = np.arange(nmax + 1) * Tc
        a2.vlines(tn, 0, np.cos(2 * np.pi * f0 * tn), color=INK, lw=1.2)
        a2.plot(tn, np.cos(2 * np.pi * f0 * tn), "o", ms=9, color=INK, mec=SURFACE, mew=2, zorder=5, label="campioni")
        a2.axhline(0, color=INK_2, lw=0.6)
        a2.set_xlim(-0.05, N * Tc + 0.05)
        a2.set_ylim(-1.3, 1.3)
        a2.set_xticks(np.arange(0, N * Tc + 0.01, Tc))
        a2.set_xlabel(r"$t$ [ms]   (tacche: istanti di campionamento $nT_c$)")
        a2.set_ylabel("valore del coseno")
        a2.legend(loc="lower right", ncol=3, fontsize=8.5, bbox_to_anchor=(1.0, 1.0))
        h1.set_text("Perché si vede 0.5 kHz: l'effetto stroboscopio")
        if su_campione and nmax > 0:
            gb, gr = 270 * nmax, 90 * nmax
            h2.set_text(f"campione n = {nmax}:  nero +{gb}° = {gb // 360} giri + {gb % 360}°   ·   "
                        f"rosso −{gr}° ≡ {(-gr) % 360}°   →   stessa posizione, stesso campione")
        elif nmax == 0 and su_campione:
            h2.set_text("tra due campioni ($T_c = 0.5$ ms) il nero fa 3/4 di giro (+270°), il rosso 1/4 di giro all'indietro (−90°)")
        else:
            h2.set_text(f"t = {tt:.3f} ms: tra i campioni i due fasori sono in posizioni diverse")
        return []

    if anteprima:
        cartella, quali = anteprima
        for k in quali:
            draw(k)
            fig.savefig(f"{cartella}/anteprima-stroboscopio-{k:03d}.png", dpi=80, bbox_inches=None)
        plt.close(fig)
        return
    ani = FuncAnimation(fig, lambda i: draw(seq[i]), frames=len(seq), blit=False)
    ani.save(OUT / "grafico-aliasing-stroboscopio.gif", writer=PillowWriter(fps=fps), dpi=80)
    plt.close(fig)
    print("scritto grafico-aliasing-stroboscopio.gif")


if __name__ == "__main__":
    laplace_lambda()
    laplace_confronto()
    lloyd_max_plot()
    snr_vs_bit()
    errore_sinusoide()
    chebyshev()
    interpolatori()
    snr_vs_livello()
    companding_soglie()
    aliasing_ripiegamento()
    aliasing_animazione()
    aliasing_stroboscopio()
