---
tipo: concetto
importanza_esame: alta
prerequisiti: ["stazionarieta", "momenti-di-un-processo", "correlazione-e-covarianza"]
fonti_pdf: ["random_processes.pdf#page=19", "random_processes.pdf#page=20", "random_processes.pdf#page=21"]
---

# Autocorrelazione dei processi WSS

## Definizione · [[random_processes.pdf#page=17|p. 17]], [[random_processes.pdf#page=19|p. 19]]

Per un processo WSS ([[stazionarieta]]) l'autocorrelazione dipende solo dalla distanza tra i due campioni, e si scrive in funzione del **ritardo** (*lag*) $\tau$:
$$R_{XX}(\tau) \triangleq E[X(t)\,X(t - \tau)], \qquad \forall\,\tau \in \mathbb{R} \tag{7}$$
detta **lag-acf**. $\tau$ è la distanza temporale tra i campioni negli istanti $t_1 = t$ e $t_2 = t_1 - \tau$.

**Autocorrelazione normalizzata:**
$$\rho_{XX}(\tau) \triangleq \frac{R_{XX}(\tau)}{R_{XX}(0)} \tag{8}$$
con valori confinati in $[-1, 1]$, cioè $|\rho_{XX}(\tau)| \le 1$.

> 🧩 Coerenza con la notazione a due istanti: con $t_1 = t$ e $t_2 = t - \tau$ si ha $\tau = t_1 - t_2$, quindi la (7) è la $R_{XX}(t_1 - t_2)$ della stazionarietà del secondo ordine.

## Formule · [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=20|20]]

| Formula | Significato |
|---|---|
| $R_{XX}(\tau) = E[X(t)X(t-\tau)]$ | lag-acf, eq. (7) |
| $R_{XX}(0) = E[X^2(t)]$ | proprietà 1: valore quadratico medio |
| $R_{XX}(-\tau) = R_{XX}(\tau)$ | proprietà 2: funzione pari |
| $\|R_{XX}(\tau)\| \le R_{XX}(0)$ | proprietà 3: massimo in modulo in $\tau = 0$ |
| $\rho_{XX}(\tau) = R_{XX}(\tau)/R_{XX}(0)$, $\ \|\rho_{XX}\| \le 1$ | normalizzata, eq. (8) |
| $\|R_{XX}(\tau)\| <$ valore prescritto per $\tau > \tau_{dec}$ | tempo di decorrelazione |

Simboli: $\tau$ = ritardo [s]; $R_{XX}$ nell'unità del segnale al quadrato (es. V²); $\rho_{XX}$ adimensionale; $\tau_{dec}$ = tempo di decorrelazione [s].

> 🧮 Formula chiave: $R_{XX}(0) = E[X^2]$, $\ R_{XX}(-\tau) = R_{XX}(\tau)$, $\ |R_{XX}(\tau)| \le R_{XX}(0)$.

## Derivazioni

### Derivazione — Proprietà 1: $R_{XX}(0) = E[X^2(t)]$ · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** «ponendo $\tau = 0$ nella (7)».
$$R_{XX}(0) = E[X(t)\,X(t - 0)] = E[X^2(t)]$$
È il **valore quadratico medio**, lo stesso per ogni $t$ perché il processo è WSS. In [[densita-spettrale-di-potenza]] è la **potenza** del processo.

### Derivazione — Proprietà 2: $R_{XX}$ è pari · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
R_{XX}(-\tau) &= E[X(t)\,X(t + \tau)] && \text{(7) con ritardo } -\tau \\
&= E[X(t' - \tau)\,X(t')] && t' = t + \tau \text{: per un processo WSS il risultato non dipende dall'istante scelto} \\
&= E[X(t')\,X(t' - \tau)] = R_{XX}(\tau) && \text{il prodotto commuta}
\end{aligned}
$$
**In parole:** "il campione di adesso con quello di $\tau$ secondi fa" e "il campione di adesso con quello fra $\tau$ secondi" sono la stessa coppia vista dall'altro lato.

### Derivazione — Proprietà 3: $|R_{XX}(\tau)| \le R_{XX}(0)$ · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Due dimostrazioni mie

**Con la disuguaglianza di Schwarz** ([[correlazione-e-covarianza]]):
$$
|R_{XX}(\tau)| = |E[X(t)X(t-\tau)]| \le \sqrt{E[X^2(t)]\,E[X^2(t-\tau)]} = \sqrt{R_{XX}(0)\,R_{XX}(0)} = R_{XX}(0)
$$
L'ultima uguaglianza usa la WSS: il valore quadratico medio è lo stesso in $t$ e in $t - \tau$.

**Con un quadrato non negativo:**
$$
\begin{aligned}
0 &\le E\big[\big(X(t) \pm X(t - \tau)\big)^2\big] && \text{valore atteso di un quadrato} \\
&= E[X^2(t)] \pm 2E[X(t)X(t-\tau)] + E[X^2(t-\tau)] && \text{sviluppo} \\
&= 2R_{XX}(0) \pm 2R_{XX}(\tau) && \text{proprietà 1 e (7)} \\
\Rightarrow\ -R_{XX}(0) &\le R_{XX}(\tau) \le R_{XX}(0) && \text{segno } + \text{ e segno } -
\end{aligned}
$$

### Derivazione — $|\rho_{XX}(\tau)| \le 1$ · [[random_processes.pdf#page=19|p. 19]]
Si divide la proprietà 3 per $R_{XX}(0) > 0$: $|\rho_{XX}(\tau)| = |R_{XX}(\tau)|/R_{XX}(0) \le 1$.
> 🧩 Se il processo ha **media nulla**, $\rho_{XX}(\tau)$ è proprio il **coefficiente di correlazione** tra i campioni $X(t)$ e $X(t-\tau)$ ([[correlazione-e-covarianza]]): $\text{Cov} = R_{XX}(\tau)$ e $\sigma^2 = R_{XX}(0)$ per entrambi.

### Derivazione — Tempo di decorrelazione dell'esempio esponenziale · [[random_processes.pdf#page=20|p. 20]]
**Fonte:** definizione di p. 20
> 🧩 Calcolo mio per il processo dei grafici, $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$ con $R_{XX}(0) = 1$ e soglia $0.1\,R_{XX}(0)$.

$$
\begin{aligned}
e^{-\tau_{dec}/\tau_c} &= 0.1 && |R_{XX}| \text{ scende sotto la soglia per } \tau > \tau_{dec} \\
\tau_{dec} &= \tau_c\ln 10 \approx 2.30\,\tau_c && \text{logaritmo di entrambi i membri}
\end{aligned}
$$
**Numeri:** $\tau_c = 2 \Rightarrow \tau_{dec} \approx 4.61$; $\tau_c = 0.1 \Rightarrow \tau_{dec} \approx 0.23$ (valori segnati nel grafico sotto).
**Sanity check:** $\tau_{dec}$ è proporzionale a $\tau_c$. Un processo con correlazione che si esaurisce 20 volte più in fretta ha un tempo di decorrelazione 20 volte più corto ✓. Il valore dipende dalla soglia scelta, che la slide lascia libera.

## Spiegazione

### Significato fisico (slide 15–16) · [[random_processes.pdf#page=19|p. 19]]–[[random_processes.pdf#page=21|21]], [[random_processes.pdf#page=32|p. 32]]

- $R_{XX}(\tau)$ descrive quanto sono **legati tra loro** due campioni presi a $\tau$ secondi di distanza.
- Più il processo **cambia rapidamente** nel tempo, più rapidamente $R_{XX}(\tau)$ scende dal massimo $R_{XX}(0)$ al crescere di $\tau$.
- Questo comportamento si riassume nel **tempo di decorrelazione** $\tau_{dec}$: per $\tau > \tau_{dec}$ il modulo di $R_{XX}(\tau)$ resta sotto un valore prescritto.

![[random-processes-p21-autocorrelazione-lento-veloce.png]]
*autocorrelazione di un processo che fluttua lentamente (curva larga, che scende piano) e di uno che fluttua rapidamente (curva stretta attorno a $\tau = 0$). Entrambe hanno il massimo in $\tau = 0$ e sono pari.*

![[grafico-rp-lento-veloce.png]]
*🧩 Grafico mio (definizioni di p. 19, p. 20 e Wiener-Khinchin di p. 32). Due processi gaussiani WSS con la stessa potenza $R_{XX}(0) = 1$: lento ($\tau_c = 2$) e veloce ($\tau_c = 0.1$).*
- *In alto una realizzazione di ciascuno: il veloce cambia molto di più da un istante all'altro.*
- *Al centro le autocorrelazioni $e^{-|\tau|/\tau_c}$: quella del veloce crolla subito ($\tau_{dec} \approx 0.23$), quella del lento dopo molto ($\tau_{dec} \approx 4.61$).*
- *In basso le PSD, trasformate delle autocorrelazioni: il lento concentra la potenza vicino a $f = 0$, il veloce la spalma su una banda larga. L'area è la stessa, 1.*

### Come si costruisce $R_{XX}(\tau)$ (animazione) · [[random_processes.pdf#page=19|p. 19]]
![[grafico-rp-autocorrelazione.gif]]
*🧩 Animazione mia della (7), con 600 realizzazioni del processo esponenziale ($\tau_c = 1$).*
- *In alto: si fissa $t = 6$ e si prende il campione a $t - \tau$, con $\tau$ che cresce da 0 a 4.*
- *In basso a sinistra: le 600 coppie $(X(t), X(t-\tau))$. Per $\tau = 0$ stanno sulla bisettrice; al crescere di $\tau$ la nuvola si allarga fino a diventare circolare, cioè i campioni non si "somigliano" più.*
- *In basso a destra: la media del prodotto su tutte le realizzazioni è la stima di $R_{XX}(\tau)$, che segue la curva teorica $e^{-\tau/\tau_c}$.*

*È la definizione (7) letta nel senso del [[processo-aleatorio|primo punto di vista]]: il valore atteso è una media **sull'insieme delle realizzazioni**, a istanti fissati.*

> 🎯 Esame: definire la lag-acf; dimostrare le tre proprietà (valore in 0, parità, massimo in 0); definire l'autocorrelazione normalizzata; spiegare il legame tra velocità di variazione del processo, larghezza di $R_{XX}$ e tempo di decorrelazione.

## Perché importa

Dice quanto "memoria" ha un processo: per quanto tempo il suo valore attuale dà informazione su quello futuro. Attraverso la trasformata di Fourier diventa la densità spettrale di potenza ([[densita-spettrale-di-potenza]]): un'autocorrelazione stretta corrisponde a uno spettro largo, e viceversa.

## Connessioni

- [[stazionarieta]] — la WSS permette di scrivere $R_{XX}$ in funzione del solo $\tau$.
- [[momenti-di-un-processo]] — la definizione generale $R_{XX}(t_1, t_2)$.
- [[correlazione-e-covarianza]] — Schwarz per la proprietà 3; $\rho_{XX}$ come coefficiente di correlazione.
- [[densita-spettrale-di-potenza]] — Wiener-Khinchin: $S_{XX} = \mathcal{F}[R_{XX}]$.
- [[processi-e-sistemi-lti]] — come si trasforma $R_{XX}$ attraverso un filtro.

## Fonti · [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=21|p. 21]]

- [[processi-aleatori]]

_Aggiornato: 2026-09-28 — creazione da ingest random_processes.pdf_
