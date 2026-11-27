---
tipo: concetto
importanza_esame: alta
prerequisiti: ["ofdm", "teorema-del-campionamento", "conversione-ad-da"]
fonti_pdf: ["ofdm_goldsmith_slides.pdf#page=33", "ofdm_goldsmith_slides.pdf#page=34", "ofdm_goldsmith_slides.pdf#page=35", "ofdm_goldsmith_slides.pdf#page=46", "ofdm_goldsmith_slides.pdf#page=47"]
---

# Realizzazione numerica dell'OFDM: IFFT e FFT

## Definizione · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=34|34]], [[ofdm_goldsmith_slides.pdf#page=46|46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]

Campionando il blocco utile OFDM a passo $T_c=T_u/N$ si ottiene esattamente la **IDFT** degli $N$ simboli: il banco di $N$ modulatori a tempo continuo diventa una **IFFT** in trasmissione, e il banco di $N$ correlatori diventa una **FFT** in ricezione. FFT e IFFT sono algoritmi veloci per calcolare DFT e IDFT, non trasformate diverse ([[fft]]).

- **Trasmettitore** (slide 41): bit → S/P → mapping QAM/PSK (alcune posizioni possono essere riservate a toni nulli o piloti) → IFFT su $N$ punti ($N$ campioni) → aggiunta del prefisso ciclico ($P=N+L_{cp}$ campioni) → P/S → DAC → $x(t)$, poi filtraggio e upconversion.
- **Ricevitore** (slide 42): $r(t)$ → ADC → S/P ($P$ campioni per blocco) → allineamento della finestra FFT e rimozione del CP ($P\to N$) → FFT su $N$ punti → equalizzazione a una presa per sottoportante (con stima di $H[k]$) → decisione e P/S → bit.

## Formule · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=34|34]], [[ofdm_goldsmith_slides.pdf#page=35|35]]

| Formula | Significato |
|---|---|
| $T_c=T_u/N$, $f_s=1/T_c=N/T_u$ | passo e frequenza di campionamento |
| $x_n[q]=\frac{1}{\sqrt N}\sum_{i=0}^{N-1}a_i[n]e^{j2\pi iq/N}=\text{IDFT}\{a_i[n]\}[q]$ | campioni del blocco utile, $q=0,\dots,N-1$ |
| $[\mathbf F_N]_{k,q}=\frac{1}{\sqrt N}e^{-j2\pi kq/N}$, $\mathbf F_N\mathbf F_N^H=\mathbf I_N$ | matrice DFT unitaria |
| $\mathbf x_n=\mathbf F_N^H\mathbf a_n$ (IDFT), $\mathbf a_n=\mathbf F_N\mathbf x_n$ (DFT) | forma matriciale |
| $\sum_q\lvert x_n[q]\rvert^2=\sum_i\lvert a_i[n]\rvert^2$ | Parseval: l'energia si conserva |
| $A[\ell]=x_n[q]$, $\ell=nN+q$ | serializzazione dei blocchi (senza CP) |
| $x(t)=\sum_\ell A[\ell]\,p_{DAC}(t-\ell T_c)$ | ricostruzione con la risposta impulsiva del DAC |

Simboli: $\mathbf a_n=[a_0[n],\dots,a_{N-1}[n]]^T$ simboli in frequenza; $\mathbf x_n=[x_n[0],\dots,x_n[N-1]]^T$ campioni nel tempo; $p_{DAC}(t)$ risposta impulsiva dello stadio di conversione D/A e ricostruzione.

> 🧮 Formula chiave: $\mathbf x_n=\mathbf F_N^H\mathbf a_n$ in trasmissione, $\mathbf a_n=\mathbf F_N\mathbf x_n$ in ricezione; costo $O(N\log N)$.

## Derivazioni

### Derivazione — Il campionamento uniforme fa comparire la IDFT · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]]

**Fonte:** slide 28, "dopo un aggiustamento di guadagno costante". **Si parte da:** $f_n(t)=\frac{1}{\sqrt{T_u}}\sum_ia_i[n]e^{j2\pi it/T_u}$, $0\le t<T_u$ ([[prefisso-ciclico]]).

$$
\begin{aligned}
f_n(qT_c)&=\frac{1}{\sqrt{T_u}}\sum_{i=0}^{N-1}a_i[n]\,e^{j2\pi iqT_c/T_u} && u=qT_c,\ q=0,\dots,N-1\\
&=\frac{1}{\sqrt{T_u}}\sum_{i=0}^{N-1}a_i[n]\,e^{j2\pi iq/N} && T_c/T_u=1/N\\
&=\sqrt{\frac{N}{T_u}}\cdot\underbrace{\frac{1}{\sqrt N}\sum_{i=0}^{N-1}a_i[n]\,e^{j2\pi iq/N}}_{x_n[q]} && \text{moltiplico e divido per }\sqrt N\\
&=\frac{1}{\sqrt{T_c}}\,x_n[q] && \sqrt{N/T_u}=1/\sqrt{T_c}
\end{aligned}
$$

Il guadagno costante $1/\sqrt{T_c}$ tra $f_n(qT_c)$ e $x_n[q]$ lo assorbe il guadagno analogico del trasmettitore. La normalizzazione $1/\sqrt N$ rende DFT e IDFT unitarie.

**Sanity check:** $f_s=N/T_u$ è proprio la larghezza (circa $N\Delta f$) dello spettro del blocco, la somma di sinc² di [[ofdm]]: si campiona alla frequenza di Nyquist di un segnale complesso che occupa circa $N/T_u$.
**Ipotesi:** campionamento sincrono con l'inizio del blocco utile. La IFFT calcola la IDFT in $O(N\log N)$ operazioni invece di $N$ oscillatori separati.

### Derivazione — DFT unitaria, inversa e Parseval · [[ofdm_goldsmith_slides.pdf#page=34|p. 34]]

**Fonte:** slide 29, risultati dati. **Si parte da:** $[\mathbf F_N]_{k,q}=\frac{1}{\sqrt N}e^{-j2\pi kq/N}$.

$$
\begin{aligned}
[\mathbf F_N\mathbf F_N^H]_{k,k'}&=\sum_{q=0}^{N-1}\frac{1}{\sqrt N}e^{-j2\pi kq/N}\cdot\frac{1}{\sqrt N}e^{+j2\pi k'q/N} && (\mathbf F^H)_{q,k'}=\overline{\mathbf F_{k',q}}\\
&=\frac1N\sum_{q=0}^{N-1}\big(e^{-j2\pi(k-k')/N}\big)^q && \text{serie geometrica di ragione } z\\
&=\begin{cases}1, & k=k'\ (z=1,\ N\text{ termini uguali a }1)\\[2pt]\dfrac1N\,\dfrac{1-z^N}{1-z}=0, & k\neq k'\ (z^N=e^{-j2\pi(k-k')}=1)\end{cases} && \text{somma geometrica}\\
\mathbf F_N\mathbf x_n&=\mathbf F_N\mathbf F_N^H\mathbf a_n=\mathbf a_n && \text{la DFT inverte la IDFT}\\
\lVert\mathbf x_n\rVert^2&=\mathbf a_n^H\mathbf F_N\mathbf F_N^H\mathbf a_n=\lVert\mathbf a_n\rVert^2 && \text{Parseval}
\end{aligned}
$$

**Sanity check:** è la versione discreta dell'ortonormalità delle sottoportanti: le righe di $\mathbf F_N$ sono le sottoportanti campionate, e sono ortonormali.

### Derivazione — Serializzazione dell'uscita IFFT · [[ofdm_goldsmith_slides.pdf#page=35|p. 35]]

**Fonte:** slide 30. La IFFT produce blocchi $x_n[0],\dots,x_n[N-1]$; senza prefisso il flusso seriale è $A[\ell]=x_n[q]$ con $\ell=nN+q$, $0\le q<N$: è l'inverso della decomposizione polifase degli appunti di p. 4 ($d(mN+i)=d_i(m)$). Per esempio $\ell=2N+5$ è il campione $q=5$ del blocco $n=2$. Il DAC ricostruisce $x(t)=\sum_\ell A[\ell]p_{DAC}(t-\ell T_c)$: IFFT, serializzazione e ricostruzione sono la controparte numerica del banco di modulatori a tempo continuo. Con il CP ogni blocco contiene invece $P=N+L_{cp}$ campioni e l'indicizzazione seriale cambia di conseguenza (🧩 per esempio $\ell=nP+L_{cp}+q$ con $q=-L_{cp},\dots,N-1$, così il blocco $n$ comincia dal suo prefisso in $\ell=nP$).

## Spiegazione · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=46|46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]

- **Cosa cambia rispetto al banco analogico.** Il banco di $N$ oscillatori a frequenze $i/T_u$, che dovevano essere precisissimi (appunti di p. 14), è sostituito da un calcolo: la IFFT genera direttamente i campioni della somma delle sottoportanti. In ricezione la FFT calcola in un colpo solo le $N$ proiezioni $r_i[n]$ dei correlatori.
- **Dove sta il prefisso.** Nel trasmettitore il CP si aggiunge **dopo** la IFFT (si copiano campioni nel tempo); nel ricevitore si toglie **prima** della FFT. La FFT lavora sempre su $N$ campioni, il canale vede $P=N+L_{cp}$ campioni.
- **Cosa fa il ricevitore dopo la FFT.** Ottiene $Y_n[k]$ su ogni sottoportante, stima $H[k]$, equalizza gli $N$ canali scalari e decide ([[equalizzazione-ofdm]]).

> 🎯 Esame: disegnare lo schema a blocchi di trasmettitore e ricevitore OFDM in banda base, con IFFT/FFT, aggiunta/rimozione del CP, P/S e DAC/ADC; spiegare perché campionando a $T_c=T_u/N$ compare la IDFT.

## Perché importa · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=14|14]]

È la ragione per cui l'OFDM è diventato pratico: la FFT costa $O(N\log N)$ ed è precisa per costruzione, mentre un banco analogico di oscillatori a spaziatura esatta era irrealizzabile (appunti di p. 14).

## Connessioni

- [[ofdm]] — gli impulsi $\phi_i(t)$ campionati sono le righe della matrice DFT.
- [[prefisso-ciclico]] — il CP rende circolare la convoluzione, e la DFT diagonalizza la convoluzione circolare.
- [[teorema-del-campionamento]] e [[conversione-ad-da]] — campionamento a $N/T_u$ e ricostruzione con $p_{DAC}(t)$.
- [[fft]] — l'algoritmo.

> 📚 Approfondimento (non d'esame): [[multiportante-ofdm-dmt-gelli]] — la stessa costruzione con IDFT normalizzata $1/N$, convertitori A/D e D/A ideali e il calcolo della varianza del rumore dopo la DFT.

## Fonti · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]]–[[ofdm_goldsmith_slides.pdf#page=35|35]], [[ofdm_goldsmith_slides.pdf#page=46|46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]

- [[signaling-ofdm]] — Lezione 15, slide 28–30, 41–42.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15, ofdm_goldsmith_slides.pdf)_
