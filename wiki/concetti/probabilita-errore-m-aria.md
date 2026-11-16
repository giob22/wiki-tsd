---
tipo: concetto
importanza_esame: alta
prerequisiti: ["probabilita-errore-binaria", "modulazione-lineare", "ricevitore-ottimo-awgn"]
fonti_pdf: ["Lezione 10-28.pdf#page=3", "Lezione 10-28.pdf#page=4", "Lezione 11-2.pdf#page=2", "Lezione 11-2.pdf#page=3"]
---

# Probabilità d'errore delle modulazioni M-arie

## Definizione · [[Lezione 10-28.pdf#page=4|p. 4]] · 11-2 [[Lezione 11-2.pdf#page=2|p. 2]]

Per $M>2$ la probabilità d'errore sul simbolo (SER) si calcola esattamente solo in casi semplici, come la QPSK, passando per la **probabilità di corretta decisione**. In generale si usano lo **union bound**, che maggiora $P(e)$ con la somma delle probabilità d'errore tra coppie di punti, e l'**approssimazione dei primi vicini**, che tiene solo i punti a distanza minima. Con il mapping di Gray, ad alto SNR, $\text{BER}\approx\text{SER}/\log_2M$.

## Formule · [[Lezione 10-28.pdf#page=4|p. 4]] · 11-2 [[Lezione 11-2.pdf#page=2|p. 2]]

| Formula | Significato |
|---|---|
| $P(e)=1-P(c)$, $P(c)=\frac1M\sum_kP(c\mid H_k)$ | via della corretta decisione |
| $P(e)_{QPSK}=\text{erfc}\sqrt{\frac{E_s}{2N_0}}-\frac14\text{erfc}^2\sqrt{\frac{E_s}{2N_0}}\simeq\text{erfc}\sqrt{\frac{E_b}{N_0}}$ | SER della QPSK |
| $\text{BER}=\frac{\text{SER}}{\log_2M}$ | con mapping di Gray, alto SNR |
| $P(e)\le\frac{1}{2M}\sum_k\sum_{i\neq k}\text{erfc}\frac{d_{ik}}{2\sqrt{N_0}}$ | union bound |
| $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\frac{d_{min}}{2\sqrt{N_0}}$ | primi vicini |
| $P(e)_{16QAM}\approx\frac32\text{erfc}\sqrt{\frac25\frac{E_b}{N_0}}$ | 16-QAM |
| $P(e)_{ort}\le\frac{M-1}{2}\text{erfc}\sqrt{\frac{E_b\log_2M}{2N_0}}$ | $M$ segnali ortogonali |

> 🧮 Formula chiave: union bound e $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\big(\frac{d_{min}}{2\sqrt{N_0}}\big)$.

Simboli: $d_{ik}=\lVert\mathbf s_i-\mathbf s_k\rVert$; $d_{min}$ distanza minima; $\bar N_{d_{min}}$ numero medio di vicini a distanza minima; $E_s=E_b\log_2M$ [J].

## Derivazioni

### Derivazione — SER della QPSK · [[Lezione 10-28.pdf#page=3|p. 3]], [[Lezione 10-28.pdf#page=4|4]]
**Fonte:** appunti del 28/10, p. 3–4.

$$
\begin{aligned}
P(c)&=P(c\mid H_1) && \text{regioni congruenti (quadranti)}\\
&=P\Big(n_1>-\frac{A\sqrt T}{2},\ n_2>-\frac{A\sqrt T}{2}\Big)=\Big[P\Big(n_1>-\frac{A\sqrt T}{2}\Big)\Big]^2 && \mathbf s_1=\big(\tfrac{A\sqrt T}{2},\tfrac{A\sqrt T}{2}\big)\text{, } n_1,n_2 \text{ indipendenti}\\
&=(1-p)^2,\qquad p=\frac12\text{erfc}\Big(\frac A2\sqrt{\frac{T}{N_0}}\Big) && \text{coda della gaussiana}\\
P(e)&=1-(1-p)^2=2p-p^2
\end{aligned}
$$

Con $E_s=\lVert\mathbf s_i\rVert^2=\frac{A^2T}{4}+\frac{A^2T}{4}=\frac{A^2T}{2}$: $\frac A2\sqrt{\frac{T}{N_0}}=\sqrt{\frac{A^2T}{4N_0}}=\sqrt{\frac{E_s}{2N_0}}$, quindi

$$
P(e)=\text{erfc}\Big(\sqrt{\frac{E_s}{2N_0}}\Big)-\frac14\text{erfc}^2\Big(\sqrt{\frac{E_s}{2N_0}}\Big)\simeq\text{erfc}\Big(\sqrt{\frac{E_b}{N_0}}\Big)\qquad(E_s=2E_b,\ \text{alto SNR})
$$

È il doppio della $P(e)$ dell'antipodale; ma ogni simbolo porta 2 bit e, con Gray, un errore di simbolo è quasi sempre un solo bit sbagliato: $\text{BER}=\frac{\text{SER}}{2}=\frac12\text{erfc}\sqrt{E_b/N_0}$, **uguale all'antipodale**.

### Derivazione — Union bound · [[Lezione 11-2.pdf#page=2|p. 2]]
**Fonte:** appunti del 2/11.

$$
\begin{aligned}
P(e\mid H_k)&=P\Big(\bigcup_{i\neq k}\{\lambda_i(\mathbf r)>\lambda_k(\mathbf r)\}\ \Big|\ H_k\Big) && \text{errore se un altro } \lambda_i \text{ supera } \lambda_k\\
&\le\sum_{i\neq k}P\big(\lambda_i>\lambda_k\mid H_k\big) && P(A\cup B)\le P(A)+P(B)\\
&=\sum_{i\neq k}\frac12\text{erfc}\Big(\frac{d_{ik}}{2\sqrt{N_0}}\Big) && \text{ogni termine è una PEP binaria}\\
P(e)&=\frac1M\sum_kP(e\mid H_k)\le\frac{1}{2M}\sum_k\sum_{i\neq k}\text{erfc}\Big(\frac{d_{ik}}{2\sqrt{N_0}}\Big)
\end{aligned}
$$

### Derivazione — 16-QAM con i primi vicini · [[Lezione 11-2.pdf#page=2|p. 2]]
**Fonte:** appunti del 2/11.

$$
\begin{aligned}
\bar N_{d_{min}}&=\frac{1}{16}(4\cdot4+8\cdot3+4\cdot2)=\frac{48}{16}=3 && \text{4 interni, 8 di bordo, 4 d'angolo}\\
E_s&=\frac{1}{16}\Big(4\cdot\frac{d^2}{2}+8\cdot\frac{5d^2}{2}+4\cdot\frac{9d^2}{2}\Big)=\frac{40}{16}d^2=\frac52d^2 && \text{punti in } (\pm\tfrac d2,\pm\tfrac d2),(\pm\tfrac d2,\pm\tfrac{3d}{2}),\dots\\
\frac52d^2&=4E_b\ \Rightarrow\ d^2=\frac85E_b && E_s=E_b\log_216\\
P(e)&\approx\frac32\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)=\frac32\text{erfc}\Big(\sqrt{\frac{d^2}{4N_0}}\Big)=\frac32\text{erfc}\Big(\sqrt{\frac25\frac{E_b}{N_0}}\Big)
\end{aligned}
$$

**Verifica:** $\frac25=0.4$ è proprio l'$\eta_P$ della 16-QAM in [[parametri-globali-modulazioni]].

### Derivazione — $M$ segnali ortogonali · [[Lezione 11-2.pdf#page=2|p. 2]]
**Fonte:** appunti del 2/11 (esempio con $M=3$).

$$
\begin{aligned}
d_{ik}&=d\ \ \forall i\neq k && \text{tutti alla stessa distanza}\\
P(e)&\le\frac{1}{2M}\cdot M(M-1)\,\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)=\frac{M-1}{2}\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big) && M(M-1) \text{ coppie ordinate}\\
E_s&=\frac{d^2}{2}\ \Rightarrow\ d=\sqrt{2E_s}=\sqrt{2E_b\log_2M} && \lVert\mathbf s_i\rVert=\tfrac{d}{\sqrt2}\\
P(e)&\le\frac{M-1}{2}\text{erfc}\Big(\sqrt{\frac{E_b\log_2M}{2N_0}}\Big)
\end{aligned}
$$

A $E_b$ fisso, aumentando $M$ l'argomento cresce come $\sqrt{\log_2M}$ e la erfc scende più in fretta di quanto cresca $M-1$: $P(e)$ diminuisce. A $E_s$ fisso, invece, $P(e)$ aumenta con $M$.

## Spiegazione · 10-28 [[Lezione 10-28.pdf#page=4|p. 4]] · 11-2 [[Lezione 11-2.pdf#page=2|p. 2]], [[Lezione 11-2.pdf#page=3|3]]

Con più di due simboli le regioni di decisione hanno forme complicate e l'integrale della gaussiana su di esse raramente si calcola in forma chiusa.

- **QPSK**: le regioni sono quadranti, e le due coordinate del rumore sono indipendenti. Indovinare il simbolo vuol dire indovinare due bit antipodali indipendenti: $P(c)=(1-p)^2$.
- **Union bound**: un errore avviene se il ricevuto è più vicino ad **almeno un** altro punto. La probabilità dell'unione è al più la somma delle probabilità: ogni termine è un problema binario tra due punti (pairwise error probability). Si ottiene un **maggiorante**.
- **Primi vicini**: ad alto SNR i termini con distanza maggiore sono trascurabili rispetto a quelli a $d_{min}$ (la erfc decresce come una gaussiana). Resta $\frac{\bar N_{d_{min}}}{2}\text{erfc}\frac{d_{min}}{2\sqrt{N_0}}$. A basso SNR l'approssimazione è poco affidabile, perché anche i punti più lontani contribuiscono.
- **SER e BER**: con il mapping di Gray i vicini differiscono per un bit, quindi un errore di simbolo è quasi sempre un solo bit sbagliato su $\log_2M$.

> 🎯 Esame: SER della QPSK via corretta decisione e confronto BER con l'antipodale, union bound con la PEP, approssimazione dei primi vicini, esempio 16-QAM ($\bar N=3$, $d^2=\frac85E_b$), ortogonali con $M$.

## Perché importa

Sono le formule con cui si confrontano le modulazioni: l'approssimazione dei primi vicini è la (5) della lezione sui parametri globali, e da essa nascono l'efficienza in potenza e il piano di Shannon ([[parametri-globali-modulazioni]], [[limite-di-shannon]]).

## Connessioni

- [[probabilita-errore-binaria]] — ogni PEP è un caso binario.
- [[modulazione-lineare]] — costellazioni PSK e QAM e mapping di Gray.
- [[modulazione-ortogonale]] — distanze uguali tra tutti i segnali.
- [[parametri-globali-modulazioni]] — (5)–(6) e $\eta_P$.

## Fonti · 10-28 [[Lezione 10-28.pdf#page=3|p. 3]], [[Lezione 10-28.pdf#page=4|4]] · 11-2 [[Lezione 11-2.pdf#page=2|p. 2]], [[Lezione 11-2.pdf#page=3|3]]

[[appunti-lezione-28-ottobre]], [[appunti-lezione-2-novembre]].

_Aggiornato: 2026-11-16 — creazione da ingest Lezione 10-28.pdf e Lezione 11-2.pdf_
