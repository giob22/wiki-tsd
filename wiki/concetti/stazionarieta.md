---
tipo: concetto
importanza_esame: alta
prerequisiti: ["processo-aleatorio", "momenti-di-un-processo"]
fonti_pdf: ["random_processes.pdf#page=4", "random_processes.pdf#page=15", "random_processes.pdf#page=16", "random_processes.pdf#page=17", "random_processes.pdf#page=18"]
---

# Stazionarietà dei processi aleatori

## Definizione · [[random_processes.pdf#page=15|p. 15]]–[[random_processes.pdf#page=18|18]]

In generale la caratterizzazione statistica di un processo $X(t)$ **cambia nel tempo**. Se le sue proprietà statistiche non dipendono, entro certi limiti, dalla scelta dell'**origine dei tempi**, il processo si dice **stazionario** in qualche senso. Ci sono diverse forme di stazionarietà.

Il confronto che le definisce:
- si considera il processo iniziato a $t = -\infty$ e lo si campiona negli istanti $t_1, \dots, t_k$, con CDF congiunta di ordine $k$ $F_{X(t_1),\dots,X(t_k)}$;
- si spostano tutti gli istanti della stessa quantità $\tau$ (traslazione nel tempo): $X(t_1 + \tau), \dots, X(t_k + \tau)$, con CDF $F_{X(t_1+\tau),\dots,X(t_k+\tau)}$.

$X(t)$ è **stazionario di ordine $k$** se
$$F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1,\dots,x_k) = F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \tag{6}$$
per ogni traslazione $\tau$ e ogni scelta di $t_1, \dots, t_k$.

| Tipo | Condizione |
|---|---|
| **in senso stretto** (SSS, *strict-sense*) | la (6) vale per **ogni** $k \in \mathbb{N}$: la forma più forte |
| **del primo ordine** | la (6) vale per $k = 1$ |
| **del secondo ordine** | la (6) vale per $k = 2$ |
| **in senso lato** (WSS, *wide-sense*, o *debolmente stazionario*) | media costante e autocorrelazione che dipende solo dalla differenza tra i due istanti |

Spesso bastano forme più deboli della stazionarietà in senso stretto.

## Formule · [[random_processes.pdf#page=16|p. 16]]–[[random_processes.pdf#page=18|18]]

| Formula | Significato |
|---|---|
| $F_{X(t)}(x) = F_{X(t+\tau)}(x) = F_{X(0)}(x)$ | primo ordine: la distribuzione non dipende da $t$ |
| $\mu_X(t) = \int x\,f_{X(0)}(x)\,dx \equiv \mu_X$ | primo ordine: media costante |
| $F_{X(t_1),X(t_2)}(x_1, x_2) = F_{X(t_1-t_2),X(0)}(x_1, x_2)$ | secondo ordine: dipende solo da $t_1 - t_2$ |
| $R_{XX}(t_1, t_2) \equiv R_{XX}(t_1 - t_2)$ | secondo ordine: autocorrelazione in funzione della differenza |
| SSS ⇒ WSS |  |

Simboli: $\tau$ = traslazione temporale [s]; $F$ = CDF congiunte ([[processo-aleatorio]]); $\mu_X$ = media; $R_{XX}$ = autocorrelazione ([[momenti-di-un-processo]]).

## Derivazioni

### Derivazione — Primo ordine: distribuzione e media non dipendono da $t$ · [[random_processes.pdf#page=16|p. 16]]
**Fonte:** «ponendo $\tau = -t$ risulta…».
> 🧩 Passaggi esplicitati da me

$$
\begin{aligned}
F_{X(t_1+\tau)}(x) &= F_{X(t_1)}(x) \quad \forall\,\tau, t_1 && \text{(6) con } k = 1 \\
F_{X(t)}(x) &= F_{X(t - t)}(x) = F_{X(0)}(x) && t_1 = t,\ \tau = -t \\
f_{X(t)}(x) &= f_{X(0)}(x) && \text{derivo in } x \\
\mu_X(t) &= \int x\,f_{X(t)}(x)\,dx = \int x\,f_{X(0)}(x)\,dx \equiv \mu_X && \text{la media non dipende da } t
\end{aligned}
$$
Si può confrontare ogni istante con l'istante 0: se tutti hanno la stessa distribuzione di $X(0)$, hanno tutti la stessa distribuzione.

### Derivazione — Secondo ordine: conta solo la distanza tra gli istanti · [[random_processes.pdf#page=17|p. 17]]
**Fonte:** «ponendo $\tau = -t_2$ risulta…».
$$
\begin{aligned}
F_{X(t_1),X(t_2)}(x_1, x_2) &= F_{X(t_1+\tau),X(t_2+\tau)}(x_1, x_2) && \text{(6) con } k = 2 \\
&= F_{X(t_1-t_2),X(0)}(x_1, x_2) && \tau = -t_2 \\
R_{XX}(t_1, t_2) &= \iint x_1x_2\,f_{X(t_1-t_2),X(0)}(x_1, x_2)\,dx_1dx_2 \equiv R_{XX}(t_1 - t_2) && \text{la (4) con la pdf traslata}
\end{aligned}
$$
La distribuzione del secondo ordine dipende solo dalla **differenza** $t_1 - t_2$, non dagli istanti particolari in cui si campiona. Di conseguenza anche l'autocorrelazione.

### Derivazione — Stazionario di ordine $k$ ⇒ stazionario di ordine $k-1$ · [[random_processes.pdf#page=17|p. 17]]
**Fonte:** affermato senza dimostrazione.
> 🧩 Derivazione mia, con la coerenza delle distribuzioni di [[processo-aleatorio]].

$$
\begin{aligned}
F_{X(t_1+\tau),\dots,X(t_{k-1}+\tau)}(x_1,\dots,x_{k-1}) &= F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1,\dots,x_{k-1}, +\infty) && \text{marginale} \\
&= F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_{k-1}, +\infty) && \text{(6) di ordine } k \\
&= F_{X(t_1),\dots,X(t_{k-1})}(x_1,\dots,x_{k-1}) && \text{marginale}
\end{aligned}
$$
È la (6) di ordine $k-1$; ripetendo si scende a $k-2$, e così via. Il viceversa in generale **non** vale: l'invarianza delle marginali non dice nulla su come i campioni dipendono tra loro.

### Derivazione — SSS ⇒ WSS · [[random_processes.pdf#page=18|p. 18]], [[random_processes.pdf#page=44|p. 44]]
**Fonte:** affermato senza dimostrazione.
> 🧩 Derivazione mia

- SSS vuol dire che la (6) vale per ogni $k$, in particolare per $k = 1$ e $k = 2$.
- Per $k = 1$, la media è costante: prima condizione WSS.
- Per $k = 2$, l'autocorrelazione dipende solo da $t_1 - t_2$: seconda condizione WSS.

**Ipotesi:** media e autocorrelazione devono esistere, cioè momenti di secondo ordine finiti.
**Il viceversa** in generale non vale: WSS impone condizioni solo su due momenti, non su tutte le distribuzioni. Fa eccezione il processo gaussiano, per cui WSS ⇒ SSS ([[processo-gaussiano]]).

## Spiegazione

### Come leggere la definizione · [[random_processes.pdf#page=4|p. 4]]
> 🧩 Spiegazione mia

- "Stazionario" vuol dire che **non si può capire che ore sono** guardando la statistica del processo. Un blocco di campioni preso adesso e lo stesso blocco preso fra un'ora hanno la stessa distribuzione.
- La stazionarietà riguarda la **statistica**, non le realizzazioni: le forme d'onda cambiano nel tempo anche quando il processo è stazionario (grafico delle realizzazioni in [[processo-aleatorio]]).
- **Esempio non stazionario:** il rettangolo di segno casuale della slide 2 ha media $A(1-2p)$ dentro $(0, T)$ e 0 fuori ([[momenti-di-un-processo]]): la media dipende da $t$.
- **Esempio stazionario:** il processo gaussiano con $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$ dei grafici ([[autocorrelazione-processi-wss]]) è WSS e, essendo gaussiano, anche SSS.
- **Esempio WSS dagli appunti:** la sinusoide a fase casuale $A\cos(2\pi f_0 t + \Theta)$, $\Theta \sim \mathcal{U}(0, 2\pi)$, ha media nulla e $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$: calcolo in [[momenti-di-un-processo]]. Ogni realizzazione è un coseno deterministico, ma la statistica non dipende da $t$.

### Scala delle stazionarietà · Processi [[random_processes.pdf#page=16|p. 16]], [[random_processes.pdf#page=18|p. 18]] · Campionamento [[Campionamento_AD_DA.pdf#page=34|p. 34]]

$$\text{SSS} \ \Rightarrow\ \dots \ \Rightarrow\ \text{ordine } 2 \ \Rightarrow\ \text{ordine } 1$$
$$\text{ordine } 2 \ \Rightarrow\ \text{WSS} \quad (\text{se esistono i momenti})$$

La WSS è la forma di stazionarietà usata nel resto della lezione: [[autocorrelazione-processi-wss]], [[densita-spettrale-di-potenza]], [[processi-e-sistemi-lti]].

> 💡 Connessione: il quantizzatore di Lloyd-Max suppone il segnale **stazionario del primo ordine** ([[quantizzazione-non-uniforme]]). Vuol dire che tutti i campioni $x(n)$ hanno la stessa pdf $f_X$, e quindi un solo quantizzatore progettato su $f_X$ va bene in ogni istante.

> 🎯 Esame: definire la stazionarietà di ordine $k$, SSS, del primo e del secondo ordine, WSS; ricavare che al primo ordine la media è costante e al secondo l'autocorrelazione dipende da $t_1 - t_2$; mostrare SSS ⇒ WSS e perché non vale il viceversa.

## Perché importa

Senza stazionarietà media e autocorrelazione sono funzioni di uno o due istanti, difficili da maneggiare. Con la WSS l'autocorrelazione diventa funzione del solo ritardo $\tau$, e si può farne la trasformata di Fourier: la densità spettrale di potenza ([[densita-spettrale-di-potenza]]).

## Connessioni

- [[processo-aleatorio]] — le distribuzioni congiunte di cui si chiede l'invarianza.
- [[momenti-di-un-processo]] — media e autocorrelazione nella definizione di WSS.
- [[autocorrelazione-processi-wss]] — proprietà dell'autocorrelazione quando il processo è WSS.
- [[processo-gaussiano]] — WSS ⇒ SSS.
- [[quantizzazione-non-uniforme]] — ipotesi di stazionarietà del primo ordine in Lloyd-Max.

## Fonti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=15|p. 15]], [[random_processes.pdf#page=18|p. 18]]

- [[processi-aleatori]]

_Aggiornato: 2026-09-28 — re-ingest: esempio WSS della sinusoide a fase casuale dagli appunti. Prima, nello stesso giorno: creazione da ingest random_processes.pdf_
