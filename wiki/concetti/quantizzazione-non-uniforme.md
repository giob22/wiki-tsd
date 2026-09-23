---
tipo: concetto
importanza_esame: alta
prerequisiti: ["quantizzazione-uniforme", "media-e-varianza"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=32", "Campionamento_AD_DA.pdf#page=33", "Campionamento_AD_DA.pdf#page=34", "Campionamento_AD_DA.pdf#page=35", "Campionamento_AD_DA.pdf#page=36"]
---

# Quantizzazione non uniforme e quantizzatore ottimo di Lloyd-Max

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=33]]

Dati $M+1$ **livelli di decisione** $x_0<x_1<\dots<x_{M-1}<x_M$ con $x_0=-\infty$ e $x_M=+\infty$, si ha una partizione dell'asse reale in intervalli $R_i = (x_{i-1},x_i)$, $i=1,\dots,M$:
- **esterni**: $R_1 = ]-\infty,x_1]$ e $R_M = [x_{M-1},+\infty[$;
- **interni**: $R_i$ per $i=2,\dots,M-1$.

Assegnati $M$ **livelli di restituzione** $q_1,\dots,q_M$, la legge di quantizzazione (arbitraria, non uniforme) è
$$Q(x) = q_i \quad \text{se } x\in R_i$$
- regione granulare: $R_g = \bigcup_{i=2}^{M-1}R_i = (x_1,x_{M-1})$;
- regione di sovraccarico: $R_s = R_1\cup R_M$.

![[campionamento-p28-caratteristica-quantizzatore.png]]
*Caratteristica ingresso-uscita $Q(x)$ con regione granulare $\mathcal{R}_g$ e di sovraccarico $\mathcal{R}_s$ — [[Campionamento_AD_DA.pdf#page=28]]. La figura della slide mostra gradini **uniformi**. In un quantizzatore non uniforme la struttura è la stessa (livelli $q_1,\dots,q_M$, regioni esterne che saturano a $q_1$ e $q_M$), ma i gradini hanno larghezze $\Delta_i = x_i - x_{i-1}$ diverse.*

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $f_X(x) = \frac\lambda2 e^{-\lambda\|x\|}$ | pdf di Laplace (ampiezze della voce) | [[Campionamento_AD_DA.pdf#page=32]] |
| $\text{MSE} = E[e^2(n)] = \sum_{i=1}^M\int_{R_i}(q_i-x)^2f_X(x)\,dx$ | errore quadratico medio | [[Campionamento_AD_DA.pdf#page=34]] |
| $q_i = E[x(n)\,\|\,x(n)\in R_i] = \dfrac{\int_{x_{i-1}}^{x_i} x\,f_X(x)\,dx}{\int_{x_{i-1}}^{x_i} f_X(x)\,dx}$ | **condizione del centroide**: baricentro della pdf ristretta a $R_i=(x_{i-1},x_i)$ | [[Campionamento_AD_DA.pdf#page=35]] |
| $x_i = \dfrac{q_i+q_{i+1}}{2}$ | **condizione del punto medio** (minima distanza) | [[Campionamento_AD_DA.pdf#page=35]] |

> 🧩 Derivazione mia — perché quella frazione è una media: il numeratore $\int_{x_{i-1}}^{x_i}x\,f_X(x)\,dx$ pesa ogni valore $x$ per la sua densità di probabilità, come nella somma discreta $\sum_k x_k\,p(x_k)$ di [[media-e-varianza]], ma limitata all'intervallo $R_i$ invece che a tutto l'asse reale. Il denominatore $\int_{x_{i-1}}^{x_i}f_X(x)\,dx = P(x\in R_i)$ è l'area di $f_X$ dentro $R_i$: dividere per questa area **rinormalizza** i pesi, perché $f_X$ ristretta a $R_i$ non è di per sé una pdf valida (non integra a 1 su $R_i$). Il rapporto è quindi la media pesata dei valori di $x$ **condizionata** al fatto che $x$ sia caduto in $R_i$ ([[probabilita-condizionale]]) — cioè il baricentro (centro di massa) della sola fetta di pdf che sta in $R_i$, non di tutta $f_X$.

Simboli: $f_X$ = pdf del segnale, supposto **stazionario del primo ordine** ([[Campionamento_AD_DA.pdf#page=34]]); $e(n) = Q[x(n)]-x(n)$. MSE nell'unità del segnale al quadrato (es. V²).

> 🧮 Formula chiave: le due condizioni di Lloyd-Max.

## Derivazioni

### Derivazione — Condizione del centroide
**Fonte:** [[Campionamento_AD_DA.pdf#page=35]] (risultato dato; «ben noto dalla teoria della stima MMSE»)
> 🧩 Derivazione mia. Fisso le regioni $R_i$ e ottimizzo rispetto a $q_i$, che compare solo nel termine $i$-esimo.
$$
\begin{aligned}
\frac{\partial\,\text{MSE}}{\partial q_i} &= \int_{R_i} 2(q_i-x)f_X(x)\,dx = 0 && \text{derivo sotto il segno di integrale} \\
q_i\int_{R_i}f_X(x)\,dx &= \int_{R_i}x\,f_X(x)\,dx && \text{separo} \\
q_i &= \frac{\int_{R_i}x\,f_X(x)\,dx}{\int_{R_i}f_X(x)\,dx} = \int_{R_i} x\,\frac{f_X(x)}{P(x\in R_i)}\,dx && \text{pdf condizionata a } \{x\in R_i\} \\
&= E[x(n)\,|\,x(n)\in R_i] && \text{media condizionale}
\end{aligned}
$$
È un minimo: $\partial^2\text{MSE}/\partial q_i^2 = 2P(x\in R_i)>0$.
**Interpretazione:** $q_i$ è il **baricentro** della porzione di pdf in $R_i$.

### Derivazione — Condizione del punto medio
**Fonte:** [[Campionamento_AD_DA.pdf#page=35]] (risultato dato)
> 🧩 Derivazione mia. Fisso i $q_i$; $x_i$ è l'estremo superiore di $R_i$ e quello inferiore di $R_{i+1}$.
$$
\begin{aligned}
\text{MSE} &\ni \int_{x_{i-1}}^{x_i}(q_i-x)^2f_X\,dx + \int_{x_i}^{x_{i+1}}(q_{i+1}-x)^2f_X\,dx && \text{termini che dipendono da } x_i \\
\frac{\partial\,\text{MSE}}{\partial x_i} &= (q_i-x_i)^2f_X(x_i) - (q_{i+1}-x_i)^2f_X(x_i) = 0 && \text{regola di Leibniz} \\
(x_i-q_i)^2 &= (q_{i+1}-x_i)^2 && f_X(x_i)>0 \\
x_i - q_i &= q_{i+1}-x_i && q_i<x_i<q_{i+1} \Rightarrow \text{entrambi positivi} \\
x_i &= \frac{q_i+q_{i+1}}{2}
\end{aligned}
$$
**Interpretazione:** ogni $x$ va al livello $q_i$ **più vicino** (regola a minima distanza).

### Caso uniforme come verifica
> 🧩 Sanity check mio: con $f_X$ uniforme su $(-X_{max},X_{max})$ e intervalli uguali, il centroide di ogni $R_i$ è il punto medio e le soglie sono a metà tra livelli adiacenti. Il quantizzatore uniforme soddisfa quindi entrambe le condizioni ed è ottimo, in accordo con [[Campionamento_AD_DA.pdf#page=32]].

## Spiegazione

### Perché non uniforme
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=32]]

- Dal punto di vista teorico la quantizzazione uniforme è ottima **solo** se $x(n)$ è distribuito uniformemente in $(-X_{max},X_{max})$.
- Il segnale vocale ha una pdf **non uniforme**: i valori vicini allo zero sono più probabili di quelli elevati.
- Questo comportamento è ben modellato da una **distribuzione di Laplace**, $f_X(x) = \frac\lambda2e^{-\lambda|x|}$ con $\lambda>0$.
- Intuitivamente, le ampiezze più piccole vanno quantizzate **più finemente**: da qui la **quantizzazione non uniforme**.

![[grafico-laplace-pdf-lambda.png]]
*🧩 Grafico mio (formula di [[Campionamento_AD_DA.pdf#page=32]], script in `output/grafici/`). La pdf di Laplace ha una **cuspide** in 0 e code esponenziali. $\lambda$ regola la larghezza: il picco vale $\lambda/2$ e il valore efficace è $x_{rms} = \sqrt2/\lambda$ (derivazione in [[variabili-aleatorie-notevoli]]). Un parlatore a voce alta ha $\lambda$ piccolo (curva larga), uno a voce bassa ha $\lambda$ grande (curva stretta).*

![[grafico-laplace-gauss-uniforme.png]]
*🧩 Grafico mio: tre pdf con la **stessa potenza** $E[x^2] = 1$. Rispetto a gaussiana e uniforme, la Laplace concentra molta più probabilità vicino a zero e ha code più lunghe. Un quantizzatore uniforme, che spende gli stessi livelli ovunque, "spreca" risoluzione sulle ampiezze grandi (rare) e ne dà poca a quelle piccole (frequenti). È ottimo solo per la pdf uniforme (verde).*

### Algoritmo di Lloyd-Max
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=34]], [[Campionamento_AD_DA.pdf#page=35]]

- Errore di quantizzazione: $e(n) \triangleq x_q(n) - x(n) = Q[x(n)] - x(n)$, con $f_X(x)$ pdf del segnale $x(n)$ supposto **stazionario del primo ordine**. Il suo valor quadratico medio (*mean square error*, MSE) è la funzione da minimizzare ([[Campionamento_AD_DA.pdf#page=34]]).
- Trovare la legge ottima secondo il criterio a **minimo errore quadratico medio** (MMSE) significa determinare gli intervalli $R_1,\dots,R_M$ (cioè i livelli di decisione $x_1,\dots,x_{M-1}$) e i livelli di restituzione $q_1,\dots,q_M$ che minimizzano l'MSE.
- Il problema **non** ha soluzione in forma chiusa. Si ricavano però facilmente **due condizioni necessarie**, fissando un sottoinsieme delle variabili e ottimizzando rispetto all'altro: è il **quantizzatore ottimo di Lloyd-Max** ([[Campionamento_AD_DA.pdf#page=34]]).
- **Regioni fissate**: i livelli ottimi sono i **centroidi** delle regioni di decisione (centroide = media condizionale; risultato ben noto dalla teoria della stima ottima MMSE).
- **Livelli fissati**: le soglie sono i punti medi tra livelli adiacenti, cioè $x(n)$ viene approssimato con il livello $q_i$ più vicino (**regola a minima distanza**).
- L'algoritmo applica **alternativamente** le due condizioni e itera finché l'MSE si assesta su un valore sufficientemente piccolo ([[Campionamento_AD_DA.pdf#page=35]]) → [[algoritmo-lloyd-max]].

![[grafico-lloyd-max-laplace.png]]
*🧩 Grafico mio: risultato dell'algoritmo di Lloyd-Max (le due condizioni di [[Campionamento_AD_DA.pdf#page=35]] iterate fino a convergenza) per $M = 8$ e pdf di Laplace con $x_{rms} = 1$. Livelli $q_i = \pm0.233, \pm0.833, \pm1.672, \pm3.087$; soglie $x_i = 0, \pm0.533, \pm1.253, \pm2.380$; MSE $= 0.0545$, quindi SNR $= 10\log_{10}(1/0.0545) \approx 12.6$ dB. Si vede l'idea della slide: intervalli **stretti** dove la pdf è alta, **larghi** sulle code. Ogni soglia sta a metà fra due livelli; ogni livello è il baricentro della pdf nel suo intervallo, quindi è spostato verso lo zero rispetto al centro dell'intervallo.*

### Limiti del quantizzatore ottimo
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=36]]

1. richiede segnale **stazionario** e **pdf nota**;
2. come l'uniforme, ha prestazioni **fortemente dipendenti dal livello** del segnale.

In telefonia serve una **quantizzazione robusta**, con prestazioni circa indipendenti dal livello, vista la grande variabilità dei parlatori. La soluzione è il [[companding]]: compressione, poi quantizzazione uniforme, e in decodifica espansione.

> 🎯 Esame: derivare le due condizioni (centroide, punto medio), dire perché sono solo *necessarie*, spiegare i limiti che portano al companding.

## Perché importa

Mostra che il quantizzatore va progettato **sulla statistica** della sorgente: con la stessa $M$, mettere intervalli più stretti dove la pdf è più alta riduce l'MSE. Le sue limitazioni ([[Campionamento_AD_DA.pdf#page=36]]) motivano il [[companding]].

## Connessioni

- [[quantizzazione-uniforme]] — caso particolare, ottimo per pdf uniforme.
- [[media-e-varianza]], [[probabilita-totale-e-bayes]] — il centroide è una media condizionale.
- [[algoritmo-lloyd-max]] — procedura iterativa.
- [[companding]] — l'alternativa robusta.
- [[variabili-aleatorie-notevoli]] — pdf di Laplace.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=32]] – [[Campionamento_AD_DA.pdf#page=36]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; aggiunta figura caratteristica p.28; revisione di copertura totale vs PDF (testo + figure)_
