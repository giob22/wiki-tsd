---
tipo: esercizio
argomento: "dimensionamento di un sistema OFDM: spaziatura, prefisso ciclico, efficienza, bit rate, banda"
difficoltà: bassa
---

# Dimensionamento di un sistema OFDM

## Metodo · [[ofdm_goldsmith_slides.pdf#page=11|p. 11]], [[ofdm_goldsmith_slides.pdf#page=48|48]]–[[ofdm_goldsmith_slides.pdf#page=51|51]]

Si applica quando si danno il passo di campionamento (o la banda), il numero di punti della IFFT e la memoria del canale, e si chiedono i tempi del simbolo OFDM, la lunghezza del prefisso, l'efficienza e il bit rate. È una catena di definizioni:

1. **Campionamento**: $T_c=1/B$ se si dà la banda $B$ del canale.
2. **Tempo utile e spaziatura**: $T_u=NT_c$, $\Delta f=1/T_u=B/N$.
3. **Prefisso**: scegliere $L_{cp}$ con $T_g=L_{cp}T_c\ge T_h$ (memoria del canale), cioè $L_{cp}\ge\lceil T_h/T_c\rceil$.
4. **Durata del simbolo OFDM**: $T=T_u+T_g$, $P=N+L_{cp}$ campioni.
5. **Efficienza**: $\eta_{cp}=N/(N+L_{cp})=T_u/T$.
6. **Bit rate lordo**: $R_b=N_d\log_2M/T$ con $N_d$ portanti dati; netto: moltiplicare per il tasso del codice.

## Formule usate

- [[ofdm]] — $\Delta f=1/T_u$; banda con sottocanali sovrapposti.
- [[prefisso-ciclico]] — $T_g\ge T_h$, $\eta_{cp}=N/(N+L_{cp})$, $R_b=\frac{N_d\log_2M}{T_u}\cdot\frac{N}{N+L_{cp}}$.
- [[limiti-dell-ofdm]] — offset normalizzato $\epsilon_f=\delta f/\Delta f$, PAPR massimo $N$.

## Casi svolti

### Caso 1 — Scelta del prefisso (Goldsmith, esempio 12.4) · [[ofdm_goldsmith_slides.pdf#page=49|p. 49]]

**Traccia:** canale campionato con $T_c=1\ \mu$s e memoria massima $5\ \mu$s; $N=128$, $L_{cp}=8$; tutti i 128 toni in 16-QAM non codificata. Calcolare $T_u$, $T_g$, $T$, $\eta_{cp}$ e il bit rate lordo.

**Svolgimento:**

$$
\begin{aligned}
T_u&=NT_c=128\cdot1\ \mu\text{s}=128\ \mu\text{s} && \text{passo 2}\\
T_g&=L_{cp}T_c=8\ \mu\text{s}>5\ \mu\text{s} && \text{passo 3: il CP copre la memoria}\\
T&=T_u+T_g=136\ \mu\text{s} && \text{passo 4}\\
\eta_{cp}&=\frac{128}{136}\approx0.941 && \text{passo 5}\\
R_b&=\frac{128\cdot\log_216}{136\ \mu\text{s}}=\frac{512\ \text{bit}}{1.36\cdot10^{-4}\ \text{s}}\approx3.76\ \text{Mbit/s} && \text{passo 6}
\end{aligned}
$$

**Risultato:** $T=136\ \mu$s, $\eta_{cp}\approx94.1\%$, $R_b\approx3.76$ Mbit/s.
**Verifica:** basterebbe $L_{cp}=5$; con 8 si ha margine. Con $\Delta f=1/128\ \mu\text{s}\approx7.8$ kHz.

### Caso 2 — IEEE 802.11a · [[ofdm_goldsmith_slides.pdf#page=51|p. 51]], [[ofdm_goldsmith_slides.pdf#page=52|52]]

**Traccia:** canale da 20 MHz, $N=64$, $L_{cp}=16$, 48 portanti dati. Calcolare tempi, frazione di prefisso e bit rate non codificati.

**Svolgimento:**

$$
\begin{aligned}
T_c&=1/(20\ \text{MHz})=0.05\ \mu\text{s},\qquad \Delta f=20\ \text{MHz}/64=312.5\ \text{kHz} && \text{passi 1–2}\\
T_u&=64\cdot0.05\ \mu\text{s}=3.2\ \mu\text{s},\qquad T_g=16\cdot0.05\ \mu\text{s}=0.8\ \mu\text{s} && \text{passi 2–3}\\
T&=4\ \mu\text{s},\qquad L_{cp}/P=16/80=20\%,\qquad \eta_{cp}=64/80=80\% && \text{passi 4–5}\\
R_b&=\frac{48\log_2M}{4\ \mu\text{s}}=12\log_2M\ \text{Mbit/s} && \text{passo 6}
\end{aligned}
$$

**Risultato:** 12, 24, 48, 72 Mbit/s per BPSK, QPSK, 16-QAM, 64-QAM; con codice di tasso 1/2 in BPSK, 6 Mbit/s.
**Verifica:** $T_u=1/\Delta f$ ✓; il canale deve avere memoria $\le0.8\ \mu$s.

### Caso 3 — Overhead del CP al variare di $N$ · [[ofdm_goldsmith_slides.pdf#page=58|p. 58]]

**Traccia:** $T_c$ fisso, $L_{cp}=8$; confrontare $N=16,64,128$.

**Svolgimento:** frazione di CP $=L_{cp}/(N+L_{cp})$: $8/24=33.3\%$, $8/72=11.1\%$, $8/136=5.9\%$; spaziatura $1/(NT_c)$: $1/(16T_c)$, $1/(64T_c)$, $1/(128T_c)$.
**Risultato:** $N$ grande ⇒ overhead piccolo ma $\Delta f$ piccolo, quindi a parità di $\delta f$ l'offset normalizzato $\epsilon_f=\delta f\,NT_c$ cresce (8 volte da 16 a 128) e cresce il PAPR possibile ($10\log_{10}N$: 12 dB, 18 dB, 21 dB).

### Caso 4 — Banda con e senza sovrapposizione (Goldsmith, esempi 12.2–12.3) · [[ofdm_goldsmith_slides.pdf#page=22|p. 22]]

**Traccia:** $N=128$ sottocanali, $T_u=0.2$ ms, coseno rialzato con $\beta=1$, margine $\varepsilon=0.1$. Confrontare la banda FDM con quella a sottocanali sovrapposti.

**Svolgimento:**

$$
\begin{aligned}
B_{FDM}&\simeq\frac{N(1+\beta+\varepsilon)}{T_u}=\frac{128\cdot2.1}{2\cdot10^{-4}\ \text{s}}=1.344\ \text{MHz} && \text{bande separate}\\
B_{overlap}&\simeq\frac{N+\beta+\varepsilon}{T_u}=\frac{129.1}{2\cdot10^{-4}\ \text{s}}\approx0.646\ \text{MHz} && \text{portanti a }1/T_u
\end{aligned}
$$

**Risultato:** la sovrapposizione riduce la banda a circa il 48%.

### Caso 5 — Nullo spettrale di un canale a due prese · [[ofdm_goldsmith_slides.pdf#page=43|p. 43]]

**Traccia:** $h[0]=h[1]=1$, $N=16$. Quali sottoportanti sono perse?

**Svolgimento:** $\lvert H[k]\rvert^2=4\cos^2(\pi k/16)$ ([[equalizzazione-ofdm]]) si annulla per $\pi k/16=\pi/2$, cioè $k=8$.
**Risultato:** il tono 8 è perso: nessun equalizzatore lo recupera; servono codifica e interleaving o non usarlo per i dati.

## Trappole

- $T_u$ **non** è la durata del simbolo OFDM trasmesso: con il prefisso è $T=T_u+T_g$. Il bit rate si divide per $T$, la spaziatura è $1/T_u$.
- Il CP si dimensiona sulla **memoria del canale** ($T_h$), non come percentuale fissa del simbolo.
- Il bit rate lordo usa le **portanti dati** ($N_d$), non tutte le $N$ posizioni della IFFT (in 802.11a 48 su 64).
- Rate lordo ≠ rate netto: va moltiplicato per il tasso del codice.
- La DFT del canale $H[k]$ è non unitaria (senza $1/\sqrt N$), mentre quella dei simboli è unitaria.

_Aggiornato: 2026-11-27 — creazione (Lezione 15: esempi numerici delle slide 17, 38, 44, 46–47, 53)_
