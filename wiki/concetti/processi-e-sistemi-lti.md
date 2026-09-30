---
tipo: concetto
importanza_esame: alta
prerequisiti: ["autocorrelazione-processi-wss", "momenti-di-un-processo"]
fonti_pdf: ["random_processes.pdf#page=26", "random_processes.pdf#page=27", "random_processes.pdf#page=28", "random_processes.pdf#page=29", "random_processes.pdf#page=30", "random_processes.pdf#page=31", "random_processes.pdf#page=33"]
---

# Processi aleatori attraverso sistemi LTI

## Definizione

> 📄 Fonte: [[random_processes.pdf#page=26]]

Un processo $X(t)$ entra in un **filtro LTI deterministico** con risposta impulsiva $h(t)$; l'uscita $Y(t)$ è un altro processo aleatorio, dato dall'integrale di convoluzione:
$$Y(t) = \int_{-\infty}^{+\infty} h(\tau_1)\,X(t - \tau_1)\,d\tau_1$$
- In generale è **difficile** trovare la distribuzione di $Y(t)$, anche conoscendo quella di $X(t)$.
- In molti casi basta calcolare **media e autocorrelazione** di $Y(t)$ a partire da quelle di $X(t)$, supponendo $X(t)$ **WSS**.

Risultati principali (ingresso WSS):
$$\mu_Y = \mu_X\,H(0) \qquad R_{YY}(\tau) = R_{XX}(\tau) * h(\tau) * h(-\tau) \qquad S_{YY}(f) = S_{XX}(f)\,|H(f)|^2$$

![[random-processes-p26-filtro-lti.png]]
*[[random_processes.pdf#page=26]]: $X(t)$ → filtro con risposta impulsiva $h(t)$ → $Y(t)$.*

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $\mu_Y(t) = E\big[\int h(\tau_1)X(t - \tau_1)\,d\tau_1\big]$ | media dell'uscita, eq. (14) | [[random_processes.pdf#page=27]] |
| $\mu_Y(t) = \int h(\tau_1)\,\mu_X(t - \tau_1)\,d\tau_1 = \mu_X(t) * h(t)$ | eq. (15) | [[random_processes.pdf#page=27]] |
| $\mu_Y = \mu_X\int h(\tau_1)\,d\tau_1 = \mu_X H(0)$ | ingresso WSS, eq. (16) | [[random_processes.pdf#page=28]] |
| $R_{Y_1Y_2}(t_1, t_2) = \iint h_1(\tau_1)h_2(\tau_2)\,R_{X_1X_2}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1 d\tau_2$ | mutua correlazione delle uscite, eq. (17)–(18) | [[random_processes.pdf#page=29]] |
| $R_{Y_1Y_2}(\tau) = \iint h_1(\tau_1)h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_1 d\tau_2$ | ingressi congiuntamente WSS, eq. (19) | [[random_processes.pdf#page=30]] |
| $R_{Y_1Y_2}(\tau) = R_{X_1X_2}(\tau) * h_1(\tau) * h_2(-\tau) = R_{X_1X_2}(\tau) * r_{h_1h_2}(\tau)$ | eq. (20) | [[random_processes.pdf#page=30]] |
| $R_{YY}(\tau) = R_{XX}(\tau) * h(\tau) * h(-\tau) = R_{XX}(\tau) * r_{hh}(\tau)$ | autocorrelazione dell'uscita | [[random_processes.pdf#page=31]] |
| $R_{YX}(\tau) = R_{XX}(\tau) * h(\tau)$, $\ R_{XY}(\tau) = R_{XX}(\tau) * h(-\tau)$ | mutue correlazioni ingresso-uscita | [[random_processes.pdf#page=31]] |
| $S_{YY}(f) = S_{XX}(f)\,\|H(f)\|^2$ | PSD dell'uscita, eq. (22) | [[random_processes.pdf#page=33]] |

Simboli:
- $h(t)$ = risposta impulsiva [1/s]; $H(f) = \int h(t)e^{-j2\pi ft}dt$ = risposta in frequenza (adimensionale); $H(0)$ = risposta a frequenza zero;
- $r_{h_1h_2}(\tau) = h_1(\tau) * h_2(-\tau) = \int h_1(s)\,h_2(s - \tau)\,ds$ = mutua correlazione **deterministica** delle due risposte impulsive (🧩 la slide la usa senza definirla), e $r_{hh}$ l'autocorrelazione deterministica di $h$;
- $S_{XX}$, $S_{YY}$ = densità spettrali di potenza ([[densita-spettrale-di-potenza]]).

> 🧮 Formula chiave: $\mu_Y = \mu_X H(0)$ e $S_{YY}(f) = S_{XX}(f)\,|H(f)|^2$.

## Derivazioni

### Derivazione — Media dell'uscita, eq. (15) e (16)
**Fonte:** [[random_processes.pdf#page=27]], [[random_processes.pdf#page=28]]
$$
\begin{aligned}
\mu_Y(t) &= E\Big[\int h(\tau_1)\,X(t - \tau_1)\,d\tau_1\Big] && \text{definizione, eq. (14)} \\
&= \int h(\tau_1)\,E[X(t - \tau_1)]\,d\tau_1 && \text{scambio } E \text{ e integrale: } E[X(t)] \text{ finita, filtro stabile} \\
&= \int h(\tau_1)\,\mu_X(t - \tau_1)\,d\tau_1 = \mu_X(t) * h(t) && \text{definizione di convoluzione, eq. (15)} \\
&= \mu_X\int h(\tau_1)\,d\tau_1 && \text{ingresso WSS: } \mu_X(t) \equiv \mu_X \\
&= \mu_X\,H(0) && H(0) = \textstyle\int h(t)\,e^{-j2\pi\cdot 0\cdot t}dt = \int h(t)\,dt \quad \text{(16)}
\end{aligned}
$$
**Lettura:** la media è la componente "continua" (a frequenza zero) del processo, e il filtro la moltiplica per il suo guadagno a frequenza zero.

### Derivazione — Mutua correlazione delle uscite, eq. (17)–(18)
**Fonte:** [[random_processes.pdf#page=29]]

Due sistemi LTI: $X_1 \to h_1 \to Y_1$ e $X_2 \to h_2 \to Y_2$.
![[random-processes-p29-due-sistemi-lti.png]]
*[[random_processes.pdf#page=29]]: $x_1(\cdot) \to h_1(\cdot) \to y_1(\cdot)$ e $x_2(\cdot) \to h_2(\cdot) \to y_2(\cdot)$.*

$$
\begin{aligned}
R_{Y_1Y_2}(t_1, t_2) &= E\Big[\int h_1(\tau_1)X_1(t_1 - \tau_1)\,d\tau_1\int h_2(\tau_2)X_2(t_2 - \tau_2)\,d\tau_2\Big] && \text{uscite come convoluzioni, eq. (17)} \\
&= \iint h_1(\tau_1)\,h_2(\tau_2)\,E[X_1(t_1 - \tau_1)X_2(t_2 - \tau_2)]\,d\tau_1 d\tau_2 && \text{prodotto di integrali = integrale doppio; scambio } E \\
&= \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(t_1 - \tau_1,\ t_2 - \tau_2)\,d\tau_1 d\tau_2 && \text{definizione di mutua correlazione, eq. (18)}
\end{aligned}
$$

### Derivazione — Ingressi congiuntamente WSS, eq. (19)–(20)
**Fonte:** [[random_processes.pdf#page=30]]: il passaggio dalla (19) alla (20) è dato senza calcoli.
$$
\begin{aligned}
(t_1 - \tau_1) - (t_2 - \tau_2) &= \tau - \tau_1 + \tau_2 && \tau = t_1 - t_2;\ \text{per ingressi congiuntamente WSS conta solo la differenza} \\
R_{Y_1Y_2}(\tau) &= \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_1 d\tau_2 && \text{eq. (19)}
\end{aligned}
$$
> 🧩 Passaggi miei dalla (19) alla (20), con $\tilde h_2(\tau) = h_2(-\tau)$:

$$
\begin{aligned}
\int h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_2 &= \int \tilde h_2(u)\,R_{X_1X_2}\big((\tau - \tau_1) - u\big)\,du && u = -\tau_2 \\
&= \big[R_{X_1X_2} * \tilde h_2\big](\tau - \tau_1) && \text{definizione di convoluzione} \\
R_{Y_1Y_2}(\tau) &= \int h_1(\tau_1)\,\big[R_{X_1X_2} * \tilde h_2\big](\tau - \tau_1)\,d\tau_1 && \text{integrale esterno} \\
&= R_{X_1X_2}(\tau) * h_2(-\tau) * h_1(\tau) = R_{X_1X_2}(\tau) * r_{h_1h_2}(\tau) && \text{la convoluzione è commutativa e associativa}
\end{aligned}
$$
Il risultato dipende **solo dal ritardo** $\tau$.

**LTI conserva l'incoerenza** ([[random_processes.pdf#page=30]]): se gli ingressi sono incoerenti, $R_{X_1X_2} \equiv 0$, allora $R_{Y_1Y_2} = 0 * r_{h_1h_2} \equiv 0$ e anche le uscite sono incoerenti.

### Derivazione — Autocorrelazione dell'uscita e mutue correlazioni ingresso-uscita
**Fonte:** [[random_processes.pdf#page=31]]
$$
\begin{aligned}
R_{YY}(t_1, t_2) &= \iint h(\tau_1)\,h(\tau_2)\,R_{XX}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1 d\tau_2 && \text{(18) con } h_1 = h_2 = h,\ X_1 = X_2 = X \\
R_{YY}(\tau) &= R_{XX}(\tau) * h(\tau) * h(-\tau) = R_{XX}(\tau) * r_{hh}(\tau) && \text{(20) con ingresso WSS}
\end{aligned}
$$
Per le mutue correlazioni ingresso-uscita si usa la (20), facendo passare uno dei due rami per un filtro "identità" $\delta(t)$:
$$
\begin{aligned}
R_{YX}(\tau) &= R_{XX}(\tau) * h(\tau) * \delta(-\tau) = R_{XX}(\tau) * h(\tau) && Y_1 = Y,\ Y_2 = X,\ h_1 = h,\ h_2 = \delta \\
R_{XY}(\tau) &= R_{XX}(\tau) * \delta(\tau) * h(-\tau) = R_{XX}(\tau) * h(-\tau) && Y_1 = X,\ Y_2 = Y,\ h_1 = \delta,\ h_2 = h
\end{aligned}
$$
**Sanity check** (🧩): la simmetria $R_{XY}(\tau) = R_{YX}(-\tau)$ di [[momenti-di-un-processo]] vale. Infatti $R_{YX}(-\tau) = [R_{XX} * h](-\tau) = [R_{XX}(-\cdot) * h(-\cdot)](\tau) = R_{XX}(\tau) * h(-\tau)$, perché $R_{XX}$ è pari ✓.

### Derivazione — Ingresso WSS ⇒ uscita WSS
**Fonte:** [[random_processes.pdf#page=31]]: «se l'ingresso di un sistema LTI stabile è WSS, anche l'uscita è WSS».
> 🧩 Derivazione mia: le due condizioni della WSS ([[stazionarieta]]).

- **Media costante:** $\mu_Y = \mu_X H(0)$, eq. (16), non dipende da $t$.
- **Autocorrelazione funzione del solo ritardo:** $R_{YY}(\tau) = R_{XX}(\tau) * r_{hh}(\tau)$ dipende solo da $\tau$.

### Derivazione — PSD dell'uscita, eq. (22)
**Fonte:** [[random_processes.pdf#page=33]]: dalla relazione di Wiener-Khinchin e da $R_{YY} = R_{XX} * h(\tau) * h(-\tau)$.
$$
\begin{aligned}
S_{YY}(f) &= \mathcal{F}\big[R_{XX}(\tau) * h(\tau) * h(-\tau)\big] && \text{Wiener-Khinchin: } S_{YY} = \mathcal{F}[R_{YY}] \\
&= S_{XX}(f)\,H(f)\,H(-f) && \text{convoluzioni} \to \text{prodotti; riflessione: } h(-\tau) \to H(-f) \\
&= S_{XX}(f)\,H(f)\,H^*(f) = S_{XX}(f)\,|H(f)|^2 && h \text{ reale: } H(-f) = H^*(f) \text{ (simmetria hermitiana)}
\end{aligned}
$$
**In parole** ([[random_processes.pdf#page=33]]): la PSD dell'uscita è la PSD dell'ingresso moltiplicata per il **modulo quadro** della risposta in frequenza. La fase del filtro non conta.
**Potenza in uscita** (🧩): $P_Y = R_{YY}(0) = \int S_{XX}(f)\,|H(f)|^2\,df$, per la (21) di [[densita-spettrale-di-potenza]].
**Sanity check** (🧩): se $\mu_X \neq 0$, $R_{XX}$ contiene la costante $\mu_X^2$ e quindi $S_{XX}$ la riga $\mu_X^2\,\delta(f)$. Nella (22) la riga diventa $\mu_X^2|H(0)|^2\delta(f)$, cioè una media in uscita $|\mu_Y| = |\mu_X H(0)|$, in accordo con la (16) ✓.

## Spiegazione

> 🧩 Il quadro (lettura mia):
> - Un filtro deterministico non rende "più aleatorio" il processo: lo rimodella. La media viene moltiplicata per $H(0)$; lo spettro di potenza per $|H(f)|^2$, quindi il filtro esalta o attenua le componenti di potenza alle varie frequenze.
> - Nel tempo, l'autocorrelazione dell'uscita è quella d'ingresso "spalmata" da $r_{hh}$. Un filtro passa-basso stretto ha $h$ lunga, quindi $r_{hh}$ larga, quindi un'uscita più lenta: il tempo di decorrelazione aumenta ([[autocorrelazione-processi-wss]]).
> - Non si conosce invece la distribuzione di $Y$, salvo per un ingresso gaussiano: in quel caso l'uscita resta gaussiana ([[processo-gaussiano]]).

> 🎯 Esame: ricavare $\mu_Y = \mu_X H(0)$ con le ipotesi per scambiare media e integrale; ricavare la (18) e la (20); dire perché ingresso WSS dà uscita WSS; ricavare $S_{YY} = S_{XX}|H|^2$.

## Perché importa

Ogni blocco lineare di un sistema di comunicazione (filtri di trasmissione e ricezione, canale LTI) agisce su segnali e rumori aleatori. Queste formule dicono come cambiano media, correlazione e spettro di potenza, cioè le quantità che determinano il rapporto segnale-rumore.

## Connessioni

- [[autocorrelazione-processi-wss]] — $R_{XX}(\tau)$ in ingresso e $R_{YY}(\tau)$ in uscita.
- [[densita-spettrale-di-potenza]] — la (22) e il suo significato fisico (filtro a banda stretta).
- [[momenti-di-un-processo]] — mutue correlazioni e loro simmetria.
- [[stazionarieta]] — WSS in ingresso ⇒ WSS in uscita.
- [[processo-gaussiano]] — un processo gaussiano attraverso un filtro stabile resta gaussiano.
- [[equivalente-banda-base-dei-filtri]] — gli stessi filtri LTI, descritti in banda base.

## Fonti

- [[processi-aleatori]]
- [[random_processes.pdf#page=26]] – [[random_processes.pdf#page=31]], [[random_processes.pdf#page=33]]

_Aggiornato: 2026-09-28 — creazione da ingest random_processes.pdf_
