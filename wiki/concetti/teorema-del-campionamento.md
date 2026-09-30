---
tipo: concetto
importanza_esame: alta
prerequisiti: ["conversione-ad-da"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=8", "Campionamento_AD_DA.pdf#page=11", "Campionamento_AD_DA.pdf#page=12", "Campionamento_AD_DA.pdf#page=13", "Campionamento_AD_DA.pdf#page=14", "Campionamento_AD_DA.pdf#page=15", "Campionamento_AD_DA.pdf#page=16"]
---

# Teorema del campionamento (teorema di Shannon)

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=8]], [[Campionamento_AD_DA.pdf#page=14]]

**Campionamento uniforme** ([[Campionamento_AD_DA.pdf#page=7]]): campionare un segnale a tempo continuo $x_a(t)$ significa estrarne i valori in istanti discreti di tempo, generalmente equispaziati di $T_c$ (**periodo di campionamento**).

![[campionamento-p7-campionamento-uniforme.png]]
*(a) Segnale TC $x_a(t)$ con i valori $x_a(nT_c)$ negli istanti $nT_c$; (b) segnale TD $x(n)$, sequenza indicizzata da $n$ intero — [[Campionamento_AD_DA.pdf#page=7]]*

**Relazione ingresso-uscita del campionatore** ([[Campionamento_AD_DA.pdf#page=8]]): la descrizione matematica è semplice,
$$x(n) = x_a(nT_c)$$
- $T_c$ = **periodo di campionamento**, in secondi (s) o sottomultipli;
- $f_c = 1/T_c$ = **frequenza di campionamento**, in Hertz (Hz) o multipli, a volte in campioni/s;
- il blocco che esegue l'operazione si chiama **sistema campionatore**: ingresso $x_a(t)$, uscita $x(n)$, comandato da $T_c$.

**Problema fondamentale** ([[Campionamento_AD_DA.pdf#page=8]]): scegliere in modo appropriato $f_c = 1/T_c$ per un dato segnale $x_a(t)$.

![[campionamento-p8-campionatore.png]]

![[campionamento-p14-teorema-shannon.png]]
*Spettro $X_a(f)$ di un segnale a banda rigorosamente limitata: nullo fuori da $[-f_m, f_m]$ (disegnato triangolare, di altezza 1) — [[Campionamento_AD_DA.pdf#page=14]]*

> 🧮 Formula chiave — **Teorema del campionamento** ([[Campionamento_AD_DA.pdf#page=14]])
> **Ipotesi:** $x_a(t)$ a banda **rigorosamente limitata** con banda monolatera $B_x = f_m$; $f_c = 1/T_c \ge 2f_m$; $x(n) = x_a(nT_c)$.
> **Tesi:** $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n)$.
> La minima frequenza di campionamento $f_{c,\min} = 2f_m$ è la **frequenza di Nyquist** di $x_a(t)$.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $x_\delta(t) = x_a(t)\sum_n\delta(t-nT_c) = \sum_n x_a(nT_c)\,\delta(t-nT_c)$ | segnale campionato idealmente | [[Campionamento_AD_DA.pdf#page=11]] |
| $\sum_n\delta(t-nT_c) \xleftrightarrow{FT} \frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)$ | trasformata del pettine di delta | [[Campionamento_AD_DA.pdf#page=12]] |
| $X_\delta(f) = \frac{1}{T_c}\sum_{k=-\infty}^{+\infty}X_a\left(f-\frac{k}{T_c}\right)$ | spettro periodico, periodo $f_c$ | [[Campionamento_AD_DA.pdf#page=12]] |
| $f_c \ge 2f_m$ | condizione di Nyquist | [[Campionamento_AD_DA.pdf#page=13]] |
| $H_r(f) = T_c\,\Pi\left(\frac{f}{2f_r}\right)$, $f_m\le f_r\le f_c-f_m$ | filtro di ricostruzione (LPF ideale) | [[Campionamento_AD_DA.pdf#page=15]] |

Simboli: $\delta(\cdot)$ = impulso di Dirac; $\Pi(x)$ = rettangolo unitario (1 per $|x|<1/2$); $X_a(f)$ = trasformata di Fourier di $x_a(t)$; $f_r$ = frequenza di taglio del filtro [Hz].

## Derivazioni

### Derivazione — Forma del segnale campionato idealmente
**Fonte:** [[Campionamento_AD_DA.pdf#page=11]]
$$
\begin{aligned}
x_\delta(t) &= x_a(t)\sum_n\delta(t-nT_c) && \text{1° stadio: prodotto per il pettine} \\
&= \sum_n x_a(t)\,\delta(t-nT_c) && \text{linearità} \\
&= \sum_n x_a(nT_c)\,\delta(t-nT_c) && \text{proprietà del campionamento della } \delta:\ g(t)\delta(t-t_0) = g(t_0)\delta(t-t_0)
\end{aligned}
$$

### Derivazione — Trasformata del pettine di delta
**Fonte:** [[Campionamento_AD_DA.pdf#page=12]] («ricordiamo...», dato per noto)
> 🧩 Derivazione mia (richiamo di teoria dei segnali)
$$
\begin{aligned}
\textstyle\sum_n\delta(t-nT_c) &= \textstyle\sum_k c_k\,e^{j2\pi k t/T_c} && \text{segnale periodico di periodo } T_c \Rightarrow \text{serie di Fourier} \\
c_k &= \frac{1}{T_c}\int_{-T_c/2}^{T_c/2}\delta(t)\,e^{-j2\pi kt/T_c}dt = \frac{1}{T_c} && \text{nel periodo c'è solo } \delta(t) \\
\textstyle\sum_n\delta(t-nT_c) &= \frac{1}{T_c}\textstyle\sum_k e^{j2\pi kf_ct} \xleftrightarrow{FT} \frac{1}{T_c}\textstyle\sum_k\delta(f-kf_c) && e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)
\end{aligned}
$$

### Derivazione — Spettro del segnale campionato
**Fonte:** [[Campionamento_AD_DA.pdf#page=12]]
$$
\begin{aligned}
X_\delta(f) &= X_a(f) * \left[\frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)\right] && \text{prodotto nel tempo} \leftrightarrow \text{convoluzione in frequenza} \\
&= \frac{1}{T_c}\sum_k X_a(f)*\delta(f-kf_c) && \text{linearità} \\
&= \frac{1}{T_c}\sum_k X_a(f-kf_c) && X*\delta(f-f_0) = X(f-f_0)
\end{aligned}
$$
Il risultato è la **replicazione** di $X_a(f)$ con passo $f_c = 1/T_c$ e ampiezza scalata di $1/T_c$: uno spettro **periodico** di periodo $f_c$ ([[Campionamento_AD_DA.pdf#page=12]]).

Conseguenze tratte dalla slide ([[Campionamento_AD_DA.pdf#page=12]]):
- l'invertibilità del campionamento equivale a stabilire **quando $X_a(f)$ si può ottenere univocamente dalla sua replicazione** con passo $f_c$;
- in generale la relazione tra "generatore" e replicazione **non è univoca**: generatori diversi possono dare la stessa replicazione;
- per questo si **assume** che $x_a(t)$ sia a **banda rigorosamente limitata**, con banda monolatera $B_x = f_m$, e si studia il problema **graficamente** al variare di $f_c$ (i tre casi qui sotto).

### Derivazione — Condizione $f_c\ge2f_m$
**Fonte:** [[Campionamento_AD_DA.pdf#page=13]] (mostrata solo graficamente)
> 🧩 Derivazione mia (traduzione algebrica della figura)
$$
\begin{aligned}
\text{supp}\,X_a &= [-f_m, f_m] && \text{banda rigorosamente limitata} \\
\text{supp}\,X_a(f-kf_c) &= [kf_c - f_m,\ kf_c+f_m] && \text{replica } k \\
\text{no sovrapposizione tra replica 0 e 1} &\iff f_m \le f_c - f_m && \text{estremo destro di 0} \le \text{estremo sinistro di 1} \\
&\iff f_c \ge 2f_m
\end{aligned}
$$
Per simmetria e periodicità basta controllare repliche adiacenti.

![[campionamento-p13-tre-casi-campionamento.png]]
*I tre casi ([[Campionamento_AD_DA.pdf#page=13]]): (a) $f_c>2f_m$, repliche separate da una banda di guardia $f_c-2f_m$; (b) $f_c=2f_m$, repliche che si toccano in $f_c/2$; (c) $f_c<2f_m$, repliche sovrapposte ([[aliasing]]).*

### Derivazione — Ricostruzione perfetta con LPF ideale
**Fonte:** [[Campionamento_AD_DA.pdf#page=15]]
$$
\begin{aligned}
X_r(f) &= H_r(f)\,X_\delta(f) = T_c\,\Pi\!\left(\tfrac{f}{2f_r}\right)\cdot\frac{1}{T_c}\sum_k X_a(f-kf_c) && \text{filtraggio LTI} \\
&= \Pi\!\left(\tfrac{f}{2f_r}\right)\sum_kX_a(f-kf_c) && T_c \text{ compensa } 1/T_c \\
&= X_a(f) && \text{se } f_r\ge f_m \text{ (passa la replica 0) e } f_r\le f_c-f_m \text{ (blocca la replica } \pm1)
\end{aligned}
$$
L'intervallo $[f_m,\,f_c-f_m]$ non è vuoto solo se $f_c\ge2f_m$. Scelta comune: $f_r = f_c/2$, il centro dell'intervallo ([[Campionamento_AD_DA.pdf#page=15]]).

![[campionamento-p15-filtro-ricostruzione.png]]
*Ricostruzione del segnale TC ([[Campionamento_AD_DA.pdf#page=15]]): (a) $X_\delta(f)$, repliche di altezza $1/T_c$ centrate in $0, \pm f_c, \dots$; (b) $H_r(f)$, rettangolo di altezza $T_c$ tra $-f_c/2$ e $f_c/2$; (c) $X_r(f) = X_a(f)$, la sola replica centrale riportata ad altezza 1.*
**Sanity check:** con $f_c = 2f_m$ l'intervallo si riduce al punto $f_r = f_m = f_c/2$ e il filtro deve essere perfettamente ideale.
**Ipotesi:** banda rigorosamente limitata; campionamento e filtro ideali (vedi [[aliasing]] e [[interpolazione]] per i casi reali).

## Spiegazione

### Intuizione
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=9]], [[Campionamento_AD_DA.pdf#page=10]]

**Scelta di $f_c$** ([[Campionamento_AD_DA.pdf#page=9]]): è fondamentale per avere una buona rappresentazione del segnale e per poterlo ricostruire dai campioni a tempo discreto.
- $T_c$ **troppo grande** per un segnale che varia rapidamente (larga banda): i campioni non seguono le oscillazioni.
- $T_c$ **adeguato** per un segnale che varia lentamente (banda stretta): i campioni descrivono bene l'andamento.
- Quindi $f_c = 1/T_c$ va scelta **proporzionale alla rapidità di variazione** del segnale nel tempo, o equivalentemente alla sua **banda** in frequenza. È l'osservazione intuitiva alla base del teorema del campionamento.

![[campionamento-p9-scelta-fc.png]]

**Invertibilità del campionamento** ([[Campionamento_AD_DA.pdf#page=10]]): dai campioni $x(n)$ si può ricostruire il segnale TC originale $x_a(t)$?
- A prima vista **no**: esistono **infiniti** segnali TC che hanno gli stessi campioni $x(n)$ (es. $x_{a1}(t)$ e $x_{a2}(t)$ in figura), quindi servono condizioni aggiuntive.
- Con **ulteriori assunzioni** su $x_a(t)$ e una **scelta opportuna** di $f_c = 1/T_c$, $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n) = x_a(nT_c)$.
- Questo risultato fondamentale è la tesi del **teorema del campionamento**, o **teorema di Shannon**.

![[campionamento-p10-invertibilita.png]]

### Modello a due stadi
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=11]]

Per dimostrare il teorema conviene schematizzare il campionamento in **due stadi**:
1. $x_a(t)$ viene moltiplicato per un **pettine di delta** $\Delta_{T_c}(t)$ di periodo $T_c$, e si ottiene $x_\delta(t)$ (ancora TC);
2. da $x_\delta(t)$ si estraggono i campioni $x(n) = x(nT_c)$: nello schema è il blocco "convertitore $\delta/n$", che trasforma il treno di impulsi nella sequenza.

È un modello utile per lo studio matematico, **senza alcun riscontro pratico**. Il segnale TC $x_\delta(t)$ si chiama **campionamento ideale**. Studiare l'invertibilità del campionamento equivale a studiare quella del **primo stadio**, perché il secondo è solo un cambio di rappresentazione.

![[campionamento-p11-campionamento-ideale.png]]
*Schema a due stadi e segnale $x_\delta(t)$: impulsi negli istanti $nT_c$, con aree pari ai campioni (inviluppo tratteggiato = $x_a(t)$) — [[Campionamento_AD_DA.pdf#page=11]]*

### Effetti pratici
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=16]]

$f_c$ cresce **linearmente** con la banda:

| Segnale | $f_m$ | $f_c \ge 2f_m$ |
|---|---|---|
| Voce | 4 kHz | 8 kHz |
| Audio | 20 kHz | 40 kHz |
| Video | 5 MHz | 10 MHz |

Al crescere di $f_c$ crescono il **costo dell'hardware** (campionatore) e il **numero di campioni** generati (ingombro di memoria).

**Esempio** ([[Campionamento_AD_DA.pdf#page=16]]): 1 minuto di audio mono campionato a $f_c = 44.1$ kHz corrisponde a $60\times44\,100 = 2\,646\,000$ campioni. Il valore **raddoppia** per un segnale stereo (canali L e R). Svolgimento in [[campionamento-e-aliasing]].

**Sovracampionamento** (*oversampling*): campionare con $f_c$ maggiore della frequenza di Nyquist. Non conviene per complessità e costo, ma può essere vantaggioso contro alcuni problemi pratici ([[Campionamento_AD_DA.pdf#page=16]]). Per esempio riduce l'aliasing dei segnali a banda non rigorosamente limitata ([[Campionamento_AD_DA.pdf#page=21]], vedi [[aliasing]]).

> 🎯 Esame: enunciato completo con ipotesi e tesi; dimostrazione grafica/spettrale; ruolo del guadagno $T_c$ del filtro; perché $f_r\in[f_m, f_c-f_m]$.

## Perché importa

Stabilisce quanti campioni al secondo servono per rappresentare un segnale senza perdite. Insieme al numero di bit per campione ([[quantizzazione-uniforme]]) fissa il bit rate prodotto dalla conversione A/D ([[Campionamento_AD_DA.pdf#page=31]]).

## Connessioni

- [[lab-campionamento]] — 🧪 laboratorio (non d'esame): campionamento simulato, repliche dello spettro e un caso in cui l'arrotondamento porta $f_s$ sotto $2W$.
- [[aliasing]] — cosa succede quando le ipotesi cadono.
- [[interpolazione]] — la ricostruzione $x_r(t)$ nel dominio del tempo (serie di Shannon).
- [[conversione-ad-da]] — il campionamento è la prima metà della conversione A/D.
- [[sistema-comunicazione-digitale]] — il campionamento è il primo passo della conversione A/D svolta dal codificatore di sorgente ([[Intro.pdf#page=15]]).
- [[inviluppo-complesso]] — un segnale passa-banda va campionato a $f_c \ge 2 f_{max}$ (qui $f_{max}$ è la sua frequenza massima), il suo inviluppo complesso a una frequenza molto più bassa ([[Rappresentazione_Rice.pdf#page=9]]); il confronto è ricavato in quella pagina. Attenzione alla notazione: qui $f_c$ è la frequenza di campionamento, là è la portante.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=7]] – [[Campionamento_AD_DA.pdf#page=16]]

_Aggiornato: 2026-09-30 — collegamento al laboratorio Matlab; 2026-09-25 — collegamento con l'inviluppo complesso; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
