"""Grafici per la lezione di laboratorio del 28/09 (raw/scripts/09_28_2006/AD_conversion.m).

Lo script replica in Python, passo per passo, AD_conversion.m (stessi parametri, stessi arrotondamenti,
stessa convoluzione e stesso taglio), poi disegna cosa succede dentro ogni macroblocco:
setup e spettro, campionamento, interpolazione, quantizzazione, SNR.
Uso: python genera_grafici_laboratorio_ad.py  (richiede numpy, matplotlib, pillow)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = Path(__file__).parent

SURFACE = "#fcfcfb"
INK = "#1f1f1e"
INK_2 = "#5f5e57"
GRID = "#e4e3dc"
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]          # blu, arancio, acqua
RED = "#e34948"

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


# ---------------------------------------------------------------- replica di AD_conversion.m
def grid(accuracy=10_000, t_i=-30.0, t_f=30.0):
    dt = (t_f - t_i) / accuracy
    return t_i + dt * np.arange(accuracy), dt              # t_i:dt:t_f-dt


def signal(t, dt, flag=1):
    if flag == 1:                                           # trapezio, righe 21-35
        ts_i = round(-2 / dt) * dt
        ts_f = ts_i + round(4 / dt) * dt
        ts_l = round(-1 / dt) * dt
        ts_r = ts_l + round(2 / dt) * dt
        e = dt / 2
        s = np.zeros_like(t)
        m1 = (t >= ts_i - e) & (t <= ts_l + e)
        m2 = (t > ts_l + e) & (t <= ts_r + e)
        m3 = (t > ts_r + e) & (t < ts_f - e)
        s[m1], s[m2], s[m3] = t[m1] + 2, 1, -t[m3] + 2
        return s, 1.0
    f0 = 4                                                  # somma di sinusoidi, righe 44-48
    s = 5*np.sin(2*np.pi*f0*t + np.pi/5) + 3*np.sin(2*np.pi*(f0/3)*t + np.pi/8) \
        + 2*np.sin(2*np.pi*(f0/10)*t - np.pi/3)
    return s, 4.0


def spectrum(s, dt):
    return np.linspace(-0.5, 0.5, len(s)) / dt, dt * np.fft.fftshift(np.fft.fft(s))


def sample(t, s, dt, W, fs=None):
    fs = 2 * W if fs is None else fs
    Ts = round((1 / fs) / dt) * dt                          # Ts multiplo di dt
    high = np.abs(t / Ts - np.round(t / Ts)) < 1e-8
    return s * high, np.flatnonzero(high), Ts


def interp_filter(C, Ts, dt, N_lobi=25):
    k = round(Ts / dt)
    if C == 1:
        th = np.arange(0, k + 1) * dt
        return th, np.ones_like(th)
    if C == 2:
        th = np.arange(-k, k + 1) * dt
        return th, 1 - np.abs(th / Ts)
    th = np.arange(-N_lobi * k, N_lobi * k + 1) * dt
    return th, np.sinc(th / Ts)


def interpolate(x, h):
    y = np.convolve(x, h)                                   # lunghezza N + L - 1
    a = (len(h) - 1) // 2
    return y, y[a:a + len(x)]


def quantize(s_samp, idx, bits):
    s_min, s_max = s_samp.min(), s_samp.max()
    Delta = (s_max - s_min) / 2**bits
    n = int(np.floor((s_max - s_min - Delta / 2) / Delta + 1e-10)) + 1
    cbook = s_min + Delta / 2 + Delta * np.arange(n)
    s_q = np.zeros_like(s_samp)
    for k in idx:
        s_q[k] = cbook[np.argmin(np.abs(cbook - s_samp[k]))]
    return s_q, cbook, Delta


def snr_db(s, s_hat):
    return 10 * np.log10(np.mean(s**2) / np.mean((s - s_hat)**2))


t, dt = grid()
N = len(t)
s, W = signal(t, dt, 1)
s_samp, idx, Ts = sample(t, s, dt, W)
fs = 1 / Ts
nz = idx[s_samp[idx] != 0]
S_true = lambda f: 3 * np.sinc(3 * f) * np.sinc(f)       # trapezio = rect(t/3) * rect(t)


# ---------------------------------------------------------------- 0. setup e spettro
def fig_setup():
    f, S = spectrum(s, dt)
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.6))
    m = (t > -1.06) & (t < -0.94)
    ax[0].plot(t[m], s[m], "o", ms=4, color=CAT[0])
    ax[0].set(title="Zoom sullo spigolo in t = -1:\ngriglia con passo dt = 6 ms",
              xlabel="t [s]", ylabel="s(t)")
    m = np.abs(f) < 3
    ax[1].plot(f[m], np.abs(S[m]), color=CAT[0], label="|dt·FFT(s)|  (codice)")
    ax[1].plot(f[m], np.abs(S_true(f[m])), "--", color=CAT[1], lw=1.5, label="3|sinc(3f)·sinc(f)|  (esatta)")
    for x in (-W, W):
        ax[1].axvline(x, color=INK_2, lw=1, ls=":")
    ax[1].text(W + 0.05, 2.4, "W = 1 Hz", color=INK_2)
    ax[1].set(title="Spettro: la FFT approssima\nla trasformata continua", xlabel="f [Hz]", ylabel="|S(f)|")
    ax[1].legend(loc="upper right", fontsize=8)
    m = (f > 0) & (f < 20)
    ax[2].plot(f[m], 20 * np.log10(np.abs(S[m]) / 3 + 1e-12), color=CAT[0])
    ax[2].axvline(W, color=INK_2, lw=1, ls=":")
    ax[2].set(title="Stesso spettro in dB: non si annulla mai\n(segnale limitato nel tempo)", xlabel="f [Hz]",
              ylabel="20log10(|S|/S(0)) [dB]", ylim=(-90, 5))
    save(fig, "grafico-lab-setup-spettro.png")


# ---------------------------------------------------------------- 1. campionamento
def fig_campionamento():
    fig, ax = plt.subplots(2, 1, figsize=(10, 6.2))
    m = np.abs(t) < 3
    ax[0].plot(t[m], s[m], color=INK_2, lw=1.5, label="s(t)")
    ax[0].stem(t[idx][np.abs(t[idx]) < 3], s_samp[idx][np.abs(t[idx]) < 3], linefmt=CAT[0], markerfmt="o",
               basefmt=" ", label=f"campioni s(nTs), Ts = {Ts:.3f} s")
    ax[0].set(title="Campionamento: s_samp = s · high (zero ovunque tranne negli istanti nTs)", xlabel="t [s]")
    ax[0].legend(loc="upper right", fontsize=8)
    f, Xs = spectrum(s_samp, dt)
    Xs = Xs / dt * Ts                                        # Ts·somma: pari a sum_k S(f - k fs)
    m = np.abs(f) < 5
    ax[1].plot(f[m], np.abs(Xs[m]), color=CAT[0], label="|Ts·DTFT dei campioni| = |somma delle repliche|")
    for k, c in ((0, CAT[1]), (1, CAT[2]), (-1, CAT[2])):
        ax[1].plot(f[m], np.abs(S_true(f[m] - k * fs)), "--", lw=1.2, color=c,
                   label="replica centrale S(f)" if k == 0 else ("repliche S(f ∓ fs)" if k == 1 else None))
    ax[1].axvspan(-fs / 2, fs / 2, color=CAT[0], alpha=0.06)
    ax[1].text(fs / 2 + 0.05, 2.5, f"fs/2 = {fs/2:.3f} Hz", color=INK_2)
    ax[1].set(title=f"Spettro del segnale campionato: repliche ogni fs = {fs:.3f} Hz\n"
                    "le code delle repliche entrano in |f| < fs/2 (aliasing piccolo: lo 0.05% dell'energia sta oltre W)",
              xlabel="f [Hz]")
    ax[1].legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    save(fig, "grafico-lab-campionamento-spettro.png")


# ---------------------------------------------------------------- 2. interpolazione
def fig_durata_convoluzione():
    th, h = interp_filter(3, Ts, dt)
    y, y_tr = interpolate(s_samp, h)
    t_conv = t[0] + th[0] + dt * np.arange(len(y))           # righe 199-202 del codice
    wrong = y[:N]                                            # taglio sbagliato: prime N
    fig, ax = plt.subplots(3, 1, figsize=(11, 7.6))
    ax[0].stem(t[nz], s_samp[nz], linefmt=CAT[0], markerfmt="o", basefmt=" ")
    ax[0].plot([t[0], t[-1]], [0, 0], color=CAT[0], lw=4, alpha=0.35, label=f"asse di s_samp: {N} punti, [-30, 30) s")
    ax[0].plot(th, h * 0.8 - 1.2, color=CAT[1], lw=1.2, label=f"h(t) = sinc(t/Ts), {len(h)} punti, [{th[0]:.2f}, {th[-1]:.2f}] s")
    ax[0].set(xlim=(-45, 45), yticks=[], title="Ingressi della convoluzione (h spostato in basso per leggibilità)")
    ax[0].legend(loc="upper left", fontsize=8)
    ax[1].plot(t_conv, y, color=CAT[0], lw=1.5)
    ax[1].axvspan(t_conv[0], t[0], color=RED, alpha=0.12)
    ax[1].axvspan(t[-1], t_conv[-1], color=RED, alpha=0.12)
    ax[1].text(-41, 0.6, "tagliato", color=RED)
    ax[1].text(33, 0.6, "tagliato", color=RED)
    ax[1].set(xlim=(-45, 45), title=f"Uscita completa di conv: {len(y)} = N + L - 1 punti, "
                                    f"da {t_conv[0]:.2f} a {t_conv[-1]:.2f} s (durate sommate)")
    ax[2].plot(t, s, color=INK_2, lw=1.2, label="s(t) originale")
    ax[2].plot(t, y_tr, color=CAT[0], lw=1.8, label="taglio del codice: da (L-1)/2 per N punti")
    ax[2].plot(t, wrong, color=RED, lw=1.5, ls="--", label=f"taglio sbagliato: prime N (ritardo {-th[0]:.2f} s)")
    ax[2].set(xlim=(-5, 16), xlabel="t [s]", title="Perché si taglia proprio lì: tornare sull'asse t di s(t)")
    ax[2].legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    save(fig, "grafico-lab-durata-convoluzione.png")


def fig_interpolatori():
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.6), sharey=True)
    m = np.abs(t) < 3
    for a, (C, nome) in zip(ax, ((1, "C = 1: rettangolo (ZOH)\nlinee verticali = punti sommati due volte"), (2, "C = 2: triangolo (lineare)"),
                                 (3, "C = 3: sinc, 25 lobi per lato"))):
        th, h = interp_filter(C, Ts, dt)
        _, y = interpolate(s_samp, h)
        a.plot(t[m], s[m], color=INK_2, lw=1.2, label="s(t)")
        a.plot(t[m], y[m], color=CAT[0], label=f"ricostruito, SNR = {snr_db(s, y):.1f} dB")
        a.plot(t[nz], s_samp[nz], "o", color=CAT[1], ms=4)
        if C == 1:
            hc = np.ones(round(Ts / dt))                     # 0:dt:Ts-dt, nessun punto in comune
            yc = np.convolve(s_samp, hc)[:N]                 # allineamento causale: th(1) = 0
            a.plot(t[m], yc[m], color=CAT[2], lw=1.2, ls="--",
                   label=f"ZOH corretto e causale, SNR = {snr_db(s, yc):.1f} dB")
        a.set(title=nome, xlabel="t [s]")
        a.legend(loc="lower center", fontsize=7)
    fig.tight_layout()
    save(fig, "grafico-lab-interpolatori.png")


def gif_interpolazione():
    """Ogni campione aggiunge una copia di h centrata in nTs e scalata del suo valore."""
    m = np.abs(t) < 3.2
    tt = t[m]
    filt = [(2, "lineare (triangolo)"), (3, "Shannon (sinc)")]
    copies = {}
    for C, _ in filt:
        th, h = interp_filter(C, Ts, dt)
        copies[C] = [s_samp[k] * np.interp(tt - t[k], th, h, left=0, right=0) for k in nz]
    fig, ax = plt.subplots(2, 1, figsize=(8, 5.6), sharex=True)

    def draw(i):
        for a, (C, nome) in zip(ax, filt):
            a.clear()
            a.plot(tt, s[m], color=INK_2, lw=1, ls=":", label="s(t)")
            for j in range(i):
                a.plot(tt, copies[C][j], color=CAT[2], lw=0.9, alpha=0.7)
            a.plot(tt, np.sum(copies[C][:i], axis=0) if i else 0 * tt, color=CAT[0], lw=2,
                   label="somma = conv(s_samp, h)")
            if i:
                a.stem(t[nz[:i]], s_samp[nz[:i]], linefmt=CAT[1], markerfmt="o", basefmt=" ")
            a.set(ylim=(-0.25, 1.15), title=f"Interpolazione {nome}: {i} campioni su {len(nz)}")
            a.legend(loc="upper right", fontsize=7)
        ax[1].set_xlabel("t [s]")
        fig.tight_layout()

    anim = FuncAnimation(fig, draw, frames=list(range(len(nz) + 1)) + [len(nz)] * 3, interval=700)
    anim.save(OUT / "grafico-lab-interpolazione.gif", writer=PillowWriter(fps=1.4))
    plt.close(fig)
    print("scritto grafico-lab-interpolazione.gif")


# ---------------------------------------------------------------- 3. quantizzazione
def fig_quantizzazione():
    s_q, cbook, Delta = quantize(s_samp, idx, 4)
    th, h = interp_filter(2, Ts, dt)
    _, sq_r = interpolate(s_q, h)
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.8))
    x = np.linspace(-0.02, 1.02, 2000)
    q = cbook[np.argmin(np.abs(cbook[None, :] - x[:, None]), axis=1)]
    ax[0].plot(x, q, color=CAT[0], lw=1.5, label="Q(x): 16 livelli al centro delle celle")
    ax[0].plot(x, x, color=INK_2, lw=0.8, ls=":")
    for v in sorted(set(np.round(s_samp[idx], 3))):
        ax[0].plot(v, cbook[np.argmin(np.abs(cbook - v))], "o", color=CAT[1], ms=6)
    ax[0].set(title=f"Caratteristica: Δ = 1/16 = {Delta:.4f}\nnessun livello in 0: lo 0 va a Δ/2", xlabel="campione", ylabel="livello")
    ax[0].legend(loc="upper left", fontsize=7)
    e = s_q[idx] - s_samp[idx]
    ax[1].vlines(t[idx], 0, e, color=CAT[1], lw=0.6)
    ax[1].plot(t[idx], e, "o", color=CAT[1], ms=3)
    ax[1].axhline(Delta / 2, color=RED, lw=1, ls="--")
    ax[1].axhline(-Delta / 2, color=RED, lw=1, ls="--")
    ax[1].set(title="Errore e(n) = s_q - s sui 121 campioni:\nquasi tutti valgono esattamente +Δ/2", xlabel="nTs [s]")
    m = np.abs(t) < 6
    ax[2].plot(t[m], s[m], color=INK_2, lw=1.2, label="s(t)")
    ax[2].plot(t[m], sq_r[m], color=CAT[0], label="ricostruito dopo la quantizzazione")
    ax[2].set(title="Il 'pavimento' a Δ/2 = 0.031 fuori dal trapezio", xlabel="t [s]")
    ax[2].legend(loc="upper right", fontsize=7)
    fig.tight_layout()
    save(fig, "grafico-lab-quantizzazione.png")


# ---------------------------------------------------------------- 4. SNR
def fig_snr():
    bits = np.arange(1, 13)
    tot, camp = [], []
    for b in bits:
        s_q, _, _ = quantize(s_samp, idx, b)
        _, y = interpolate(s_q, interp_filter(2, Ts, dt)[1])
        tot.append(snr_db(s, y))
        camp.append(snr_db(s_samp[idx], s_q[idx]))
    floor_lin = snr_db(s, interpolate(s_samp, interp_filter(2, Ts, dt)[1])[1])
    floor_sinc = snr_db(s, interpolate(s_samp, interp_filter(3, Ts, dt)[1])[1])
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.plot(bits, tot, "o-", color=CAT[0], label="SNR_q del codice (s contro ricostruito), lineare")
    ax.plot(bits, camp, "s--", color=CAT[1], lw=1.5, ms=4, label="SNR sui soli campioni (solo quantizzazione)")
    ax.plot(bits, camp[0] + 6.02 * (bits - 1), ":", color=INK_2, lw=1.2, label="pendenza 6.02 dB/bit")
    model = [10 * np.log10(np.mean(s**2) / ((1 / 2**b)**2 / 12)) for b in bits]
    ax.plot(bits, model, "--", color=INK, lw=1, label="modello P_e = Δ²/12 (4.77 dB più ottimista)")
    ax.axhline(floor_lin, color=CAT[2], lw=1.2, ls="-.", label=f"senza quantizzazione, lineare: {floor_lin:.1f} dB")
    ax.axhline(floor_sinc, color=RED, lw=1.2, ls="-.", label=f"senza quantizzazione, sinc: {floor_sinc:.1f} dB")
    ax.annotate("4 bit: 16.7 dB\n(valore stampato dal codice)", (4, tot[3]), (5.2, 6), fontsize=8,
                arrowprops=dict(arrowstyle="->", color=INK_2))
    ax.set(xlabel="bit per campione b", ylabel="SNR [dB]",
           title="Esempio 1: +6 dB per bit finché domina la quantizzazione,\npoi il limite è l'errore di interpolazione")
    ax.legend(loc="upper left", fontsize=7.5)
    save(fig, "grafico-lab-snr-vs-bit.png")


# ---------------------------------------------------------------- esempio 2 (flag = 2)
def fig_esempio2():
    s2, W2 = signal(t, dt, 2)
    fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    m = np.abs(t) < 3
    for a, fsr in zip(ax, (None, 16)):
        ss, ii, T2 = sample(t, s2, dt, W2, fsr)
        _, y = interpolate(ss, interp_filter(3, T2, dt)[1])
        a.plot(t[m], s2[m], color=INK_2, lw=1.2, label="s(t)")
        a.plot(t[m], y[m], color=CAT[0], lw=1.6, label=f"ricostruito con la sinc, SNR = {snr_db(s2, y):.1f} dB")
        mm = np.abs(t[ii]) < 3
        a.plot(t[ii][mm], ss[ii][mm], "o", color=CAT[1], ms=3.5)
        tag = "fs = 2W come nel codice" if fsr is None else "fs = 16 Hz richiesti"
        a.set(title=f"Esempio 2, {tag}: Ts = {T2:.3f} s, fs = {1/T2:.2f} Hz", ylim=(-11, 11))
        a.legend(loc="upper right", fontsize=8)
    ax[1].set_xlabel("t [s]")
    fig.tight_layout()
    save(fig, "grafico-lab-esempio2.png")


if __name__ == "__main__":
    fig_setup()
    fig_campionamento()
    fig_durata_convoluzione()
    fig_interpolatori()
    gif_interpolazione()
    fig_quantizzazione()
    fig_snr()
    fig_esempio2()
