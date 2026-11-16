---
tipo: concetto
importanza_esame: alta
prerequisiti: ["ricevitore-ottimo-awgn", "variabile-aleatoria-gaussiana"]
fonti_pdf: ["Lezione 10-28.pdf#page=1", "Lezione 10-28.pdf#page=2", "Lezione 10-28.pdf#page=3"]
---

# Probabilità d'errore delle modulazioni binarie

## Definizione · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=3|3]]

Per due segnali $s_1(t)$, $s_2(t)$ equiprobabili in AWGN, con ricevitore ML (a minima distanza), la probabilità d'errore dipende solo dalla **distanza** $d=\lVert s_1-s_2\rVert$ tra i due punti della costellazione:

$$P(e)=\frac12\,\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)$$

Ne derivano i casi on-off, antipodale e ortogonale, e il caso generale con coefficiente di correlazione $\rho$. La $P(e)$ non cambia per traslazioni e rotazioni della costellazione, mentre l'energia media sì: è minima con baricentro nell'origine.

## Formule · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=3|3]]

| Modulazione | $d$ | $P(e)$ |
|---|---|---|
| on-off ($0$, $\sqrt{E_s}$) | $\sqrt{E_s}$ | $\frac12\text{erfc}\big(\frac12\sqrt{E_s/N_0}\big)$ |
| antipodale ($\pm\sqrt{E_s}$) | $2\sqrt{E_s}$ | $\frac12\text{erfc}\big(\sqrt{E_s/N_0}\big)$ |
| ortogonale | $\sqrt{2E_s}$ | $\frac12\text{erfc}\big(\sqrt{E_s/(2N_0)}\big)$ |
| equienergetica con correlazione $\rho$ | $\sqrt{2E_s(1-\rho)}$ | $\frac12\text{erfc}\big(\sqrt{E_s(1-\rho)/(2N_0)}\big)$ |

> 🧮 Formula chiave: $P(e)=\frac12\text{erfc}\big(\frac{d}{2\sqrt{N_0}}\big)$, $d^2=E_{s_1}+E_{s_2}-2\rho\sqrt{E_{s_1}E_{s_2}}$.

Simboli: $E_s$ [J] energia del segnale (per l'on-off, energia di $s_1$); $N_0/2$ [W/Hz] PSD del rumore; $\rho=\frac{\langle s_1,s_2\rangle}{\lVert s_1\rVert\lVert s_2\rVert}$ coefficiente di correlazione; $\text{erfc}(x)=\frac{2}{\sqrt\pi}\int_x^\infty e^{-u^2}du$.

## Derivazioni

### Derivazione — On-off · [[Lezione 10-28.pdf#page=1|p. 1]]
**Fonte:** appunti del 28/10, p. 1.
**Si parte da:** $\lambda(r)=\frac{2\sqrt{E_s}}{N_0}r-\frac{E_s}{N_0}\gtrless0$ (ML, [[rivelazione-map-ml]]).

$$
\begin{aligned}
\frac{2\sqrt{E_s}}{N_0}r-\frac{E_s}{N_0}\gtrless0&\iff r\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \frac{\sqrt{E_s}}{2} && \text{soglia a metà strada, non dipende da } N_0\\
P(e\mid H_0)&=P\Big(n>\frac{\sqrt{E_s}}{2}\Big)=\int_{\sqrt{E_s}/2}^{\infty}\frac{1}{\sqrt{\pi N_0}}e^{-x^2/N_0}dx && n\sim\mathcal N(0,\tfrac{N_0}{2})\\
&\overset{u=x/\sqrt{N_0}}{=}\frac{1}{\sqrt\pi}\int_{\frac12\sqrt{E_s/N_0}}^{\infty}e^{-u^2}du=\frac12\text{erfc}\Big(\frac12\sqrt{\frac{E_s}{N_0}}\Big) && \text{definizione di erfc}\\
P(e\mid H_1)&=P\Big(\sqrt{E_s}+n<\frac{\sqrt{E_s}}{2}\Big)=P\Big(n<-\frac{\sqrt{E_s}}{2}\Big)=P(e\mid H_0) && \text{simmetria della gaussiana}\\
P(e)&=\tfrac12P(e\mid H_0)+\tfrac12P(e\mid H_1)=\frac12\text{erfc}\Big(\frac12\sqrt{\frac{E_s}{N_0}}\Big)
\end{aligned}
$$

Gli appunti ottengono $P(e\mid H_1)$ con $\text{erfc}(-x)=2-\text{erfc}(x)$; il risultato è lo stesso perché le regioni di decisione sono **congruenti**.

### Derivazione — Antipodale · [[Lezione 10-28.pdf#page=2|p. 2]]
**Fonte:** appunti p. 2.

$$
\begin{aligned}
\lambda_1\gtrless\lambda_2&\iff\sqrt{E_s}\,r\gtrless-\sqrt{E_s}\,r\iff r\ \underset{H_2}{\overset{H_1}{\gtrless}}\ 0 && \text{segnali equienergetici: } \tfrac12E_s \text{ si toglie}\\
P(e)=P(e\mid H_2)&=P(-\sqrt{E_s}+n>0)=P(n>\sqrt{E_s})=\frac12\text{erfc}\Big(\sqrt{\frac{E_s}{N_0}}\Big) && \text{stesso cambio di variabile}
\end{aligned}
$$

### Derivazione — Formula generale in funzione della distanza · [[Lezione 10-28.pdf#page=2|p. 2]], [[Lezione 10-28.pdf#page=3|3]]
**Fonte:** appunti p. 2 («si può dimostrare che») e p. 3.

> 🧩 Derivazione mia del passaggio «si può dimostrare». Si sceglie un asse lungo il segmento $\mathbf s_1\mathbf s_2$: per l'invarianza per rotazioni e traslazioni il problema diventa quello di due punti a distanza $d$ su una retta, con soglia nel punto medio. Il rumore proiettato su quell'asse è $\mathcal N(0,N_0/2)$, quindi:

$$
\begin{aligned}
P(e)&=P\Big(n>\frac d2\Big)=\frac12\text{erfc}\Big(\frac{d/2}{\sqrt{N_0}}\Big)=\frac12\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big) && \text{come nell'on-off con } \tfrac{\sqrt{E_s}}{2}\to\tfrac d2\\
d^2&=\int_0^{T_b}(s_1-s_2)^2dt=E_{s_1}+E_{s_2}-2\int_0^{T_b}s_1s_2\,dt && \text{sviluppo del quadrato}\\
&=E_{s_1}+E_{s_2}-2\rho\sqrt{E_{s_1}E_{s_2}} && \textstyle\int s_1s_2=\rho\sqrt{E_{s_1}E_{s_2}}\\
E_{s_1}=E_{s_2}=E_s:\quad P(e)&=\frac12\text{erfc}\Big(\sqrt{\frac{2E_s(1-\rho)}{4N_0}}\Big)=\frac12\text{erfc}\Big(\sqrt{\frac{E_s(1-\rho)}{2N_0}}\Big)
\end{aligned}
$$

**Verifica:** $\rho=-1$ ridà l'antipodale, $\rho=0$ l'ortogonale; l'on-off ($E_{s_1}=0$) dà $d=\sqrt{E_s}$ e la formula iniziale.
**Ipotesi:** AWGN, simboli equiprobabili, ricevitore ML.

### Derivazione — Energia minima con baricentro nell'origine · [[Lezione 10-28.pdf#page=2|p. 2]]
**Fonte:** appunti p. 2 («$E_s$ è minima se $\sum_i\mathbf s_i=0$»).

> 🧩 Derivazione mia. Traslo tutta la costellazione di $\mathbf c$ (la $P(e)$ non cambia):

$$
E(\mathbf c)=\frac1M\sum_i\lVert\mathbf s_i-\mathbf c\rVert^2=\frac1M\sum_i\lVert\mathbf s_i\rVert^2-2\mathbf c^T\bar{\mathbf s}+\lVert\mathbf c\rVert^2,\qquad\bar{\mathbf s}=\frac1M\sum_i\mathbf s_i
$$

è una parabola in $\mathbf c$ con minimo in $\mathbf c=\bar{\mathbf s}$: conviene spostare il baricentro nell'origine. Esempio: l'on-off è un'antipodale spostata, con la stessa $d$ ma energia media maggiore.

## Spiegazione · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=3|3]]

Con il ricevitore ML in AWGN tutto si riduce a geometria: il ricevitore sbaglia quando il rumore, proiettato lungo la retta che unisce i due punti, supera metà della distanza. Per questo conta solo $d$, e $P(e)$ è la coda di una gaussiana oltre $d/2$.

- A parità di energia per simbolo $E_s$, l'**antipodale** mette i punti il più lontano possibile ($d=2\sqrt{E_s}$, $\rho=-1$): sfrutta meglio l'energia. L'**ortogonale** ha $d=\sqrt{2E_s}$ (3 dB peggio), l'**on-off** $d=\sqrt{E_s}$ rispetto alla sua energia di picco.
- Il contrasto di energia $\sqrt{E_s/N_0}$ è l'argomento della erfc: la $P(e)$ scende molto rapidamente al crescere di $E_s/N_0$.
- Regioni **congruenti** (stessa forma e dimensione) danno la stessa probabilità d'errore condizionata: basta calcolarne una.
- La $P(e)$ è invariante per rotazioni e traslazioni, l'energia no: le costellazioni pratiche sono centrate nell'origine.
- **Monte Carlo**: per stimare con una simulazione una probabilità $p$ servono circa $100/p$ prove (per $p\approx10^{-4}$, un milione).

> 🎯 Esame: derivare $P(e)$ per on-off e antipodale passo passo, la formula $\frac12\text{erfc}(d/2\sqrt{N_0})$ e il caso con $\rho$; confronto tra on-off, ortogonale e antipodale; invarianza e energia minima.

## Perché importa

Sono i mattoni di tutte le prestazioni del corso: la QPSK si calcola con due antipodali indipendenti, lo union bound somma probabilità d'errore binarie tra coppie di punti ([[probabilita-errore-m-aria]]), e l'efficienza in potenza $\eta_P=d_{min}^2/(4E_b)$ di [[parametri-globali-modulazioni]] è proprio il confronto tra queste distanze.

## Connessioni

- [[ricevitore-ottimo-awgn]] — la soglia a metà distanza.
- [[variabile-aleatoria-gaussiana]] — la coda della gaussiana e la erfc.
- [[probabilita-errore-m-aria]] — QPSK, union bound, primi vicini.
- [[parametri-globali-modulazioni]] — gli stessi esempi OOK, antipodale, ortogonale con $\eta_P$.

## Fonti · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=3|3]]

[[appunti-lezione-28-ottobre]] — Lezione 10-28.pdf.

_Aggiornato: 2026-11-16 — creazione da ingest Lezione 10-28.pdf_
