---
tipo: concetto
importanza_esame: alta
prerequisiti: ["processo-aleatorio", "media-e-varianza", "correlazione-e-covarianza"]
fonti_pdf: ["random_processes.pdf#page=4", "random_processes.pdf#page=5", "random_processes.pdf#page=12", "random_processes.pdf#page=13", "random_processes.pdf#page=14", "random_processes.pdf#page=22", "random_processes.pdf#page=23", "random_processes.pdf#page=24", "random_processes.pdf#page=25", "random_processes.pdf#page=45", "random_processes.pdf#page=46"]
---

# Momenti di un processo aleatorio: media, correlazioni, covarianze

## Definizione · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]]

La **caratterizzazione statistica parziale** di un processo reale $X(t)$ usa i momenti del primo e del secondo ordine, invece di tutte le distribuzioni ([[processo-aleatorio]]):
- **media**: il valore atteso del campione all'istante $t$;
- **funzione di autocorrelazione** (*acf*): il valore atteso del prodotto di due campioni, agli istanti $t_1$ e $t_2$;
- **funzione di autocovarianza**: lo stesso, dopo aver tolto le medie.

Con due processi $X(t)$ e $Y(t)$ si definiscono allo stesso modo la **mutua correlazione** e la **mutua covarianza**.

## Formule · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

| Formula | Significato |
|---|---|
| $\mu_X(t) = E[X(t)] = \int_{-\infty}^{+\infty} x\,f_{X(t)}(x)\,dx$ | media, eq. (3): usa la pdf del **primo** ordine |
| $R_{XX}(t_1, t_2) = E[X(t_1)X(t_2)] = \iint x_1 x_2\,f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_1dx_2$ | autocorrelazione, eq. (4): usa la pdf del **secondo** ordine |
| $C_{XX}(t_1, t_2) = E\{[X(t_1) - \mu_X(t_1)][X(t_2) - \mu_X(t_2)]\} = R_{XX}(t_1, t_2) - \mu_X(t_1)\mu_X(t_2)$ | autocovarianza, eq. (5) |
| $R_{XY}(t, \tau) = E[X(t)\,Y(t - \tau)]$, $\ R_{YX}(t, \tau) = E[Y(t)\,X(t - \tau)]$ | mutue correlazioni, eq. (9) |
| $R_{XY}(\tau) = R_{YX}(-\tau)$ | simmetria (processi congiuntamente WSS) |
| $C_{XY}(t, \tau) = E\{[X(t) - \mu_X(t)][Y(t-\tau) - \mu_Y(t-\tau)]\}$ | mutua covarianza, eq. (10); la (11) è $C_{YX}$ |
| $\mu_Z(t) = \mu_X(t) + j\mu_Y(t)$ | media di un processo complesso, eq. (12) |
| $R_{ZZ}(t_1, t_2) = E[Z(t_1)Z^\ast (t_2)]$ | autocorrelazione di un processo complesso, eq. (13) |
| $\mu_X(n)$, $R_{XY}(n, k) = E[X(n)Y(k)]$, $C_{XY}(n,k) = R_{XY}(n,k) - \mu_X(n)\mu_Y(k)$ | versioni a tempo discreto, eq. (35)–(37) |

Simboli: $E[\cdot]$ = valore atteso; $f_{X(t)}$ = pdf del primo ordine, $f_{X(t_1),X(t_2)}$ = pdf del secondo ordine; $\tau$ = ritardo (*lag*) [s]; $Z^\ast$ = coniugato. Unità: $\mu$ come il segnale (es. V); $R$ e $C$ come il segnale al quadrato (es. V², cioè W su 1 Ω).

## Derivazioni

### Derivazione — Eq. (5): autocovarianza da media e autocorrelazione · [[random_processes.pdf#page=14|p. 14]]
**Fonte:** se si conoscono media e autocorrelazione, si ricava l'autocovarianza.
> 🧩 Passaggi miei. Scrivo $X_1 = X(t_1)$, $X_2 = X(t_2)$, $\mu_1 = \mu_X(t_1)$, $\mu_2 = \mu_X(t_2)$.

$$
\begin{aligned}
C_{XX}(t_1, t_2) &= E[(X_1 - \mu_1)(X_2 - \mu_2)] && \text{definizione} \\
&= E[X_1X_2] - \mu_2E[X_1] - \mu_1E[X_2] + \mu_1\mu_2 && \text{sviluppo e linearità di } E \text{ (} \mu_i \text{ sono costanti)} \\
&= R_{XX}(t_1, t_2) - \mu_1\mu_2 - \mu_1\mu_2 + \mu_1\mu_2 && E[X_i] = \mu_i \\
&= R_{XX}(t_1, t_2) - \mu_X(t_1)\,\mu_X(t_2)
\end{aligned}
$$
È la stessa relazione $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$ di [[correlazione-e-covarianza]], applicata a due campioni dello stesso processo. Allo stesso modo si ottiene la (37) a tempo discreto.

### Derivazione — Simmetria delle mutue correlazioni: $R_{XY}(\tau) = R_{YX}(-\tau)$ · [[random_processes.pdf#page=22|p. 22]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
R_{YX}(t', -\tau) &= E[Y(t')\,X(t' + \tau)] && \text{definizione (9) con ritardo } -\tau \\
&= E[Y(t - \tau)\,X(t)] && \text{scelgo } t' = t - \tau \\
&= E[X(t)\,Y(t - \tau)] = R_{XY}(t, \tau) && \text{il prodotto commuta}
\end{aligned}
$$
Per processi **congiuntamente WSS** nessuna delle due dipende da $t$, quindi $R_{XY}(\tau) = R_{YX}(-\tau)$.
**Perché $R_{XY}$ non è pari:** scambiare $\tau$ con $-\tau$ equivale a scambiare i ruoli di $X$ e $Y$, e in generale le due funzioni sono diverse. Per lo stesso motivo non c'è garanzia di un massimo in $\tau = 0$: il massimo sta dove i due processi "si somigliano di più", che può essere un ritardo diverso da zero.

### Derivazione — Mutua covarianza: casi particolari · [[random_processes.pdf#page=23|p. 23]]
> 🧩 Passaggi miei, con lo stesso sviluppo della (5):

$$
C_{XY}(t, \tau) = R_{XY}(t, \tau) - \mu_X(t)\,\mu_Y(t - \tau)
$$
- **media nulla** ($\mu_X = \mu_Y = 0$ per ogni $t$): $C_{XY}(t, \tau) = R_{XY}(t, \tau)$, e allo stesso modo $C_{YX} = R_{YX}$;
- **congiuntamente WSS**: le medie sono costanti e $R_{XY}$ dipende solo da $\tau$, quindi $C_{XY}(t, \tau) = R_{XY}(\tau) - \mu_X\mu_Y = C_{XY}(\tau)$.

### Derivazione — Indipendenti ⇒ incorrelati; con media nulla, incoerenti ⇔ incorrelati · [[random_processes.pdf#page=24|p. 24]]
**Fonte:** «si può dimostrare».
> 🧩 Derivazione mia (stesso argomento di [[correlazione-e-covarianza]] per due v.a.)

$$
\begin{aligned}
R_{XY}(\tau) &= E[X(t)\,Y(t - \tau)] = E[X(t)]\,E[Y(t - \tau)] = \mu_X\,\mu_Y && \text{indipendenza: il valore atteso del prodotto si fattorizza} \\
C_{XY}(\tau) &= R_{XY}(\tau) - \mu_X\mu_Y = 0 && \text{quindi incorrelati}
\end{aligned}
$$
Con $\mu_X = \mu_Y = 0$ vale $C_{XY} = R_{XY}$: $R_{XY} \equiv 0$ (incoerenti) se e solo se $C_{XY} \equiv 0$ (incorrelati).
Il viceversa, incorrelati ⇒ indipendenti, in generale **non** vale: vale per i processi gaussiani ([[processo-gaussiano]]).

### Derivazione — Momenti dell'esempio della slide 2 · [[random_processes.pdf#page=2|p. 2]]
> 🧩 Calcolo mio: la slide definisce il processo ma non ne calcola i momenti.

$$
\begin{aligned}
\mu_X(t) &= A\cdot q + (-A)\cdot p = A(1 - 2p) && 0 < t < T:\ X(t) = A \text{ con prob. } q,\ -A \text{ con prob. } p \\
\mu_X(t) &= 0 && \text{fuori da } (0, T):\ X(t) = 0 \\
R_{XX}(t_1, t_2) &= E[X(t_1)X(t_2)] = A^2 && t_1, t_2 \in (0, T):\ \text{stesso } \omega, \text{ stesso segno: il prodotto è sempre } A^2 \\
C_{XX}(t_1, t_2) &= A^2 - A^2(1 - 2p)^2 = 4p(1 - p)\,A^2 = 4pq\,A^2 && \text{eq. (5); } 1 - (1 - 2p)^2 = 4p - 4p^2
\end{aligned}
$$
Fuori da $(0, T)^2$ autocorrelazione e covarianza sono nulle.
**Sanity check:**
- con $p = 0$ o $p = 1$ il segnale è deterministico e $C_{XX} = 0$ ✓;
- con $p = 1/2$ la media è nulla e $C_{XX} = R_{XX} = A^2$ ✓.

**Lettura:** la media dipende da $t$ (vale $A(1 - 2p)$ dentro il rettangolo e 0 fuori), quindi il processo **non è stazionario** ([[stazionarieta]]). In generale $\mu_X(t)$ è funzione di $t$ e $R_{XX}$, $C_{XX}$ lo sono di $t_1$ e $t_2$ separatamente, come dicono le slide 7–9.

### Derivazione — Momenti della sinusoide a fase casuale degli appunti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]], [[random_processes.pdf#page=12|p. 12]], [[random_processes.pdf#page=13|13]]
**Fonte:** appunti a mano di p. 4 e p. 5: $X(t) = A\cos(2\pi f_0 t + \Theta)$, con $A$, $f_0$ deterministiche e $\Theta \sim \mathcal{U}(0, 2\pi)$ (vedi [[processo-aleatorio]]).
> 🧩 Calcolo mio: gli appunti definiscono il processo ma non ne calcolano i momenti. Applico le definizioni (3) e (4). L'unica v.a. è $\Theta$, quindi i valori attesi sono integrali su $\vartheta$ pesati con $f_\Theta(\vartheta) = \frac{1}{2\pi}$ in $[0, 2\pi]$.

**Media:**
$$
\begin{aligned}
\mu_X(t) &= E[A\cos(2\pi f_0 t + \Theta)] = \int_0^{2\pi} A\cos(2\pi f_0 t + \vartheta)\,\frac{1}{2\pi}\,d\vartheta && \text{valore atteso di una funzione di } \Theta \\
&= \frac{A}{2\pi}\Big[\sin(2\pi f_0 t + \vartheta)\Big]_0^{2\pi} && \text{primitiva di } \cos \text{ in } \vartheta \text{ (} t \text{ è fisso)} \\
&= \frac{A}{2\pi}\big[\sin(2\pi f_0 t + 2\pi) - \sin(2\pi f_0 t)\big] = 0 && \sin \text{ ha periodo } 2\pi
\end{aligned}
$$

**Autocorrelazione**, con $t_1 = t$ e $t_2 = t - \tau$ come nella convenzione del ritardo:
$$
\begin{aligned}
R_{XX}(t_1, t_2) &= A^2\,E\big[\cos(2\pi f_0 t_1 + \Theta)\cos(2\pi f_0 t_2 + \Theta)\big] && \text{definizione (4); } A \text{ è deterministica} \\
&= \frac{A^2}{2}\,E\big[\cos(2\pi f_0 (t_1 - t_2)) + \cos(2\pi f_0 (t_1 + t_2) + 2\Theta)\big] && \cos a\cos b = \tfrac12[\cos(a - b) + \cos(a + b)] \\
&= \frac{A^2}{2}\cos(2\pi f_0 (t_1 - t_2)) + \frac{A^2}{2}\,E\big[\cos(2\pi f_0 (t_1 + t_2) + 2\Theta)\big] && \text{il primo termine non contiene } \Theta \\
&= \frac{A^2}{2}\cos(2\pi f_0 (t_1 - t_2)) && \text{il secondo valore atteso è nullo (sotto)} \\
&= \frac{A^2}{2}\cos(2\pi f_0 \tau) && t_1 - t_2 = \tau
\end{aligned}
$$
Il valore atteso che si annulla: con $\varphi = 2\pi f_0(t_1 + t_2)$,
$$E[\cos(\varphi + 2\Theta)] = \frac{1}{2\pi}\int_0^{2\pi}\cos(\varphi + 2\vartheta)\,d\vartheta = \frac{1}{2\pi}\Big[\frac{\sin(\varphi + 2\vartheta)}{2}\Big]_0^{2\pi} = \frac{\sin(\varphi + 4\pi) - \sin\varphi}{4\pi} = 0$$
Il coseno fa due periodi interi in $\vartheta \in [0, 2\pi]$ e la sua media è zero.

**Risultato:** $\mu_X = 0$ e $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$. Poiché la media è nulla, anche $C_{XX}(\tau) = R_{XX}(\tau)$, eq. (5).
**Sanity check:**
- $R_{XX}(0) = \frac{A^2}{2} = E[X^2(t)]$: è la potenza media di una sinusoide di ampiezza $A$, come nel caso deterministico ✓;
- $R_{XX}$ è pari e $|R_{XX}(\tau)| \le R_{XX}(0)$, come vogliono le proprietà di [[autocorrelazione-processi-wss]] ✓.

**Ipotesi:** fase **uniforme su un intero periodo**. È lei che fa sparire la dipendenza da $t$. Se $\Theta$ fosse, per esempio, uniforme solo in $(0, \pi)$, la stessa integrazione darebbe
$$\mu_X(t) = \frac{A}{\pi}\big[\sin(2\pi f_0 t + \pi) - \sin(2\pi f_0 t)\big] = -\frac{2A}{\pi}\sin(2\pi f_0 t)$$
che dipende da $t$: il processo non sarebbe più WSS.

**Lettura:** la media non dipende da $t$ e l'autocorrelazione dipende solo da $\tau = t_1 - t_2$. Il processo è quindi **WSS** ([[stazionarieta]]), all'opposto del rettangolo della slide 2. Ogni realizzazione è un coseno deterministico. È l'incertezza sulla fase, uguale per tutte le fasi, a rendere la statistica indipendente dall'origine dei tempi.

## Spiegazione

### Media, autocorrelazione, autocovarianza (slide 7–9) · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]]

- La **media** di $X(t)$ è il valore atteso della v.a. ottenuta campionando il processo in $t$. Usa solo la pdf del **primo ordine** $f_{X(t)}$ e in generale è una funzione di $t$.
- L'**autocorrelazione** è il valore atteso del prodotto di due v.a., $X(t_1)$ e $X(t_2)$. Usa la pdf del **secondo ordine** e in generale dipende da $t_1$ e $t_2$ separatamente.
- L'**autocovarianza** è l'autocorrelazione dei processi "centrati" (media sottratta). Conoscendo media e autocorrelazione si ottiene con la (5).

> 💡 Connessione: per $t_1 = t_2 = t$ si ritrovano grandezze note di [[media-e-varianza]]. $R_{XX}(t, t) = E[X^2(t)]$ è il valore quadratico medio, e $C_{XX}(t, t) = \text{Var}[X(t)]$ la varianza del campione in $t$.

### Mutue correlazioni e covarianze (slide 17–18) · [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]]

- Con due processi reali $X(t)$ e $Y(t)$, di autocorrelazioni $R_{XX}(t, \tau)$ e $R_{YY}(t, \tau)$, si definiscono le **mutue correlazioni** con ritardo, eq. (9). Dipendono dall'**ordine** dei due processi.
- $X(t)$ e $Y(t)$ sono **congiuntamente WSS** se ciascuno è WSS ([[stazionarieta]]) e in più $R_{XY}(t, \tau) \equiv R_{XY}(\tau)$.
- In generale la mutua correlazione **non è pari** in $\tau$, a differenza dell'autocorrelazione, e **non ha il massimo nell'origine**. Rispetta però $R_{XY}(\tau) = R_{YX}(-\tau)$.
- Le **mutue covarianze** (10)–(11) dipendono anch'esse dall'ordine; con media nulla coincidono con le mutue correlazioni; per processi congiuntamente WSS dipendono solo da $\tau$.

### Indipendenti, incoerenti, incorrelati (slide 19) · [[random_processes.pdf#page=24|p. 24]]

| Proprietà | Definizione |
|---|---|
| **indipendenti** | gli insiemi $\{X(t_1), \dots, X(t_k)\}$ e $\{Y(t'_1), \dots, Y(t'_j)\}$ sono indipendenti per ogni $k, j \in \mathbb{N}$ e ogni scelta degli istanti |
| **incoerenti** | $R_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$ |
| **incorrelati** | $C_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$ |

- Indipendenti ⇒ incorrelati.
- Se $\mu_X = \mu_Y = 0$, incoerenza e incorrelazione coincidono.

> 🧩 L'ordine di forza: *indipendenza* riguarda tutte le distribuzioni congiunte, *incorrelazione* solo i momenti del secondo ordine. È la stessa gerarchia tra v.a. di [[correlazione-e-covarianza]]. "Incoerenti" corrisponde a "ortogonali" per due v.a. ($E[XY] = 0$).

### Processi complessi (slide 20) · [[random_processes.pdf#page=25|p. 25]]

- $Z(t) = X(t) + jY(t)$. La caratterizzazione completa di $Z$ richiede quella **congiunta** di parte reale e immaginaria.
- Caratterizzazione parziale: media (12) e autocorrelazione (13), con il **coniugato** sul secondo fattore. Si può scrivere come funzione di $(t_1, t_2)$ o di $(t, \tau)$: $R_{ZZ}(t, \tau) = E[Z(t)Z^\ast (t - \tau)]$.
- A rigore servirebbe anche un altro momento del secondo ordine, la **autocorrelazione coniugata** $R_{ZZ^\ast}(t_1, t_2) = E[Z(t_1)Z(t_2)]$, senza coniugato. Per la maggior parte dei processi però è nulla.

> 🧩 Perché il coniugato (osservazione mia): con $t_1 = t_2 = t$ si ottiene $E[Z(t)Z^\ast (t)] = E[|Z(t)|^2] \ge 0$, un numero reale che è la potenza istantanea media. Senza coniugato si otterrebbe $E[Z^2(t)]$, che in generale è complesso e non misura la potenza. È lo stesso motivo del coniugato nel prodotto scalare $\langle u, v\rangle = \int u v^\ast$ di [[inviluppo-complesso]].

### Tempo discreto (slide 40–41) · [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

$$
\mu_X(n) \triangleq E[X(n)] = \int x\,f_{X(n)}(x)\,dx \tag{35}
$$
$$
R_{XY}(n, k) \triangleq E[X(n)Y(k)] = \iint x\,y\,f_{X(n),Y(k)}(x, y)\,dx\,dy \tag{36}
$$
$$
C_{XY}(n, k) \triangleq E\{[X(n) - \mu_X(n)][Y(k) - \mu_Y(k)]\} = R_{XY}(n, k) - \mu_X(n)\mu_Y(k) \tag{37}
$$
Con $X(n) \equiv Y(n)$ nella (36) e nella (37) si ottengono autocorrelazione e autocovarianza a tempo discreto.

> ⚠️ Refuso della slide: nella (36) la pdf è scritta $f_{X(n),Y(k)}(x, x)$; deve essere $(x, y)$.

> 🎯 Esame: definire media, autocorrelazione e autocovarianza e ricavare la (5); mutue correlazioni e loro simmetria; differenza tra processi indipendenti, incoerenti e incorrelati; perché nell'autocorrelazione di un processo complesso c'è il coniugato.

## Perché importa

Media e autocorrelazione sono le grandezze con cui si lavora in pratica. Si propagano con formule semplici attraverso i filtri ([[processi-e-sistemi-lti]]); dall'autocorrelazione si ottiene la densità spettrale di potenza ([[densita-spettrale-di-potenza]]); per un processo gaussiano bastano da sole a dare la caratterizzazione completa ([[processo-gaussiano]]).

## Connessioni

- [[processo-aleatorio]] — la caratterizzazione parziale sostituisce quella completa.
- [[media-e-varianza]], [[correlazione-e-covarianza]] — gli stessi momenti per una o due v.a.; qui applicati ai campioni del processo.
- [[stazionarieta]] — WSS: media costante e autocorrelazione dipendente solo da $\tau$. La sinusoide a fase casuale degli appunti è WSS, il rettangolo della slide 2 no.
- [[autocorrelazione-processi-wss]] — proprietà dell'autocorrelazione nel caso WSS.
- [[inviluppo-complesso]] — processi complessi in banda base, coniugato nel prodotto scalare.

## Fonti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]], [[random_processes.pdf#page=12|p. 12]], [[random_processes.pdf#page=14|p. 14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

- [[processi-aleatori]]

_Aggiornato: 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-09-28 — re-ingest del PDF con appunti: momenti della sinusoide a fase casuale (p.4–5), processo WSS a confronto con il rettangolo. Prima, nello stesso giorno: creazione da ingest random_processes.pdf_
