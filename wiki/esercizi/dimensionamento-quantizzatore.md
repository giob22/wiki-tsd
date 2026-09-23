---
tipo: esercizio
argomento: "Dimensionamento di un quantizzatore (bit, SNR, fattore di carico) e bit rate"
difficoltà: media
---

# Dimensionamento di un quantizzatore e bit rate

## Metodo

1. **Fissare $k_c$** in base alla probabilità di sovraccarico ammessa: $P_s\le1/k_c^2$, cioè $k_c\ge1/\sqrt{P_s}$ ([[disuguaglianza-di-chebyshev]]). Default: $k_c = 4$ (four-sigma loading).
2. **Calcolare $[k_c]_{dB} = 20\log_{10}k_c$** (rapporto di ampiezze, quindi $20\log$).
3. **Invertire la legge dei 6 dB/bit** ([[snr-di-quantizzazione]]):
   $$b\ge\frac{\text{SNR}_{dB}+[k_c]_{dB}-4.77}{6.02}$$
   e arrotondare **per eccesso** all'intero.
4. **Verificare**: ricalcolare l'SNR con il $b$ scelto, e anche con $b-1$ per controllare che non basti.
5. **Bit rate**: $R_b = b\cdot f_c$ per canale; per $n_{ch}$ canali, $R_{tot} = n_{ch}\,b\,f_c$.
6. **Memoria**: bit $= R_{tot}\cdot T$; poi byte (÷8), kB (÷1000), MB (÷1000) secondo ISO/IEC ([[Campionamento_AD_DA.pdf#page=31]]).
7. Con companding: $\text{SNR}_{dB}\approx6.02b+\alpha$, con $\alpha = -9.99$ (A-law) o $-10.11$ (µ-law) ([[companding]]).

## Formule usate

- $\Delta = 2X_{max}/M$, $M = 2^b$ — [[quantizzazione-uniforme]] ([[Campionamento_AD_DA.pdf#page=26]], [[Campionamento_AD_DA.pdf#page=27]])
- $P_s\le1/k_c^2$ — [[disuguaglianza-di-chebyshev]] ([[Campionamento_AD_DA.pdf#page=29]])
- $\text{SNR}_{dB} = 6.02b-[k_c]_{dB}+4.77$ — [[snr-di-quantizzazione]] ([[Campionamento_AD_DA.pdf#page=30]])
- $\text{SNR}_{dB}\approx6.02b+\alpha$ — [[companding]] ([[Campionamento_AD_DA.pdf#page=43]])

## Casi svolti

### Caso 1 — Four-sigma loading
**Traccia** ([[Campionamento_AD_DA.pdf#page=29]]): $k_c = 4$. Probabilità di sovraccarico massima?
$$P_s\le\frac{1}{k_c^2} = \frac{1}{16} = 0.0625 = 6.25\%$$
**Sanity check:** per un segnale gaussiano il valore vero è $2Q(4)\approx6.3\cdot10^{-5}$ ([[variabile-aleatoria-gaussiana]]); Chebyshev è molto conservativo.

### Caso 2 — Esempio 7.6: quantizzatore audio a 85 dB
**Traccia** ([[Campionamento_AD_DA.pdf#page=31]]): si vuole $\text{SNR}_{dB} = 85$ dB con $k_c = 4$. Quanti bit? Bit rate per audio stereo a $f_c = 44.1$ kHz? Memoria per 1 minuto?

**Dati:** $\text{SNR}_{dB} = 85$ dB, $k_c = 4$, $f_c = 44.1$ kHz, 2 canali, $T = 60$ s.

**Passo 1 — numero di bit** (la slide dà solo «$b = 16$»):
$$
\begin{aligned}
[k_c]_{dB} &= 20\log_{10}4 = 20\times0.60206 = 12.04\,\text{dB} && \text{fattore di carico in dB} \\
6.02\,b - 12.04 + 4.77 &\ge 85 && \text{legge dei 6 dB/bit} \\
6.02\,b &\ge 85 + 12.04 - 4.77 = 92.27 && \text{isolo } b \\
b &\ge 92.27/6.02 = 15.33 && \\
b &= 16 && \text{arrotondo per eccesso}
\end{aligned}
$$
**Verifica:**
- $b = 16$: $6.02\times16-7.27 = 96.32-7.27 = 89.05$ dB ≥ 85 ✓;
- $b = 15$: $90.30-7.27 = 83.03$ dB < 85 ✗.

**Passo 2 — bit rate per canale:**
$$R_b = b\cdot f_c = 16\,\text{bit/campione}\times44\,100\,\text{campioni/s} = 705\,600\,\text{bit/s} = 705.6\,\text{kbit/s}$$

**Passo 3 — memoria per 1 minuto stereo:**
$$
\begin{aligned}
N_{bit} &= n_{ch}\times T\times f_c\times b = 2\times60\times44\,100\times16 && \text{canali} \times \text{s} \times \text{campioni/s} \times \text{bit/campione} \\
&= 2\times60 = 120;\quad 120\times44\,100 = 5\,292\,000;\quad 5\,292\,000\times16 = 84\,672\,000\,\text{bit} \\
&= 84\,672\,000/8 = 10\,584\,000\,\text{byte} && 1\,\text{byte} = 8\,\text{bit} \\
&= 10\,584\,\text{kB}\approx10.6\,\text{MB} && 1\,\text{kB} = 1000\,\text{byte},\ 1\,\text{MB} = 1000\,\text{kB}
\end{aligned}
$$
**Risultato:** $b = 16$ bit; 705.6 kbit/s per canale; ≈ 10.6 MB/minuto (tutti ✓ con la slide).
**Sanity check** (🧩 mio): bit rate stereo totale $= 2\times705.6 = 1411.2$ kbit/s, e $1411.2\,\text{kbit/s}\times60\,\text{s} = 84\,672$ kbit ✓. È circa 10× i 128 kbit/s di un MP3 ([[Intro.pdf#page=15]]), in accordo con la stima «around ten times higher» per l'audio professionale.

### Caso 3 — Costanti $\alpha$ del companding
**Traccia** ([[Campionamento_AD_DA.pdf#page=43]]): verificare $\alpha = -9.99$ dB (A-law, $A=87.6$), $-10.11$ dB (µ-law, $\mu=255$), $-7.3$ dB (uniforme, $k_c=4$).
$$
\begin{aligned}
\text{A-law: } \alpha &= 4.77-20\log_{10}(1+\ln87.6) = 4.77-20\log_{10}(1+4.473) && \ln87.6 = 4.4728 \\
&= 4.77-20\log_{10}5.473 = 4.77-20\times0.7382 = 4.77-14.76 = -9.99\,\text{dB} \\
\mu\text{-law: } \alpha &= 4.77-20\log_{10}\ln256 = 4.77-20\log_{10}5.545 && \ln256 = 8\ln2 = 5.5452 \\
&= 4.77-20\times0.7439 = 4.77-14.88 = -10.11\,\text{dB} \\
\text{uniforme: } \alpha &= 4.77-20\log_{10}4 = 4.77-12.04 = -7.27\approx-7.3\,\text{dB}
\end{aligned}
$$
**Risultato:** tutti ✓.

## Trappole

- **$[k_c]_{dB}$ usa $20\log_{10}$**, non $10\log_{10}$: $k_c$ è un rapporto di ampiezze.
- **Arrotondare $b$ per eccesso**: 15.33 → 16, non 15.
- La legge dei 6 dB/bit ignora il **sovraccarico**: se $k_c$ è piccolo, l'SNR reale è peggiore.
- **Stereo** = 2 canali; «per canale» vs «totale».
- **Unità di memoria**: le slide usano i fattori ISO/IEC decimali (1 kB = 1000 byte), non 1024 ([[Campionamento_AD_DA.pdf#page=31]]).
- Le costanti $\alpha$ del companding valgono con il segnale che impegna **tutta la dinamica**.

_Aggiornato: 2026-09-23 — revisione di copertura: rimosso caso inventato (voce PCM 8 bit)_
