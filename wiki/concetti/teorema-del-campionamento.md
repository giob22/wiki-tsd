---
tipo: concetto
importanza_esame: alta
prerequisiti: ["conversione-ad-da"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=8", "Campionamento_AD_DA.pdf#page=11", "Campionamento_AD_DA.pdf#page=12", "Campionamento_AD_DA.pdf#page=13", "Campionamento_AD_DA.pdf#page=14", "Campionamento_AD_DA.pdf#page=15", "Campionamento_AD_DA.pdf#page=16"]
---

# Teorema del campionamento (teorema di Shannon)

## Definizione · [[Campionamento_AD_DA.pdf#page=7|p. 7]], [[Campionamento_AD_DA.pdf#page=8|8]], [[Campionamento_AD_DA.pdf#page=14|p. 14]]

**Campionamento uniforme**: campionare un segnale a tempo continuo $x_a(t)$ significa estrarne i valori in istanti discreti di tempo, generalmente equispaziati di $T_c$ (**periodo di campionamento**).

![[campionamento-p7-campionamento-uniforme.png]]
*(a) Segnale TC $x_a(t)$ con i valori $x_a(nT_c)$ negli istanti $nT_c$; (b) segnale TD $x(n)$, sequenza indicizzata da $n$ intero*

**Relazione ingresso-uscita del campionatore**: la descrizione matematica è semplice,
$$x(n) = x_a(nT_c)$$
- $T_c$ = **periodo di campionamento**, in secondi (s) o sottomultipli;
- $f_c = 1/T_c$ = **frequenza di campionamento**, in Hertz (Hz) o multipli, a volte in campioni/s;
- il blocco che esegue l'operazione si chiama **sistema campionatore**: ingresso $x_a(t)$, uscita $x(n)$, comandato da $T_c$.

**Problema fondamentale**: scegliere in modo appropriato $f_c = 1/T_c$ per un dato segnale $x_a(t)$.

![[campionamento-p8-campionatore.png]]

![[campionamento-p14-teorema-shannon.png]]
*Spettro $X_a(f)$ di un segnale a banda rigorosamente limitata: nullo fuori da $[-f_m, f_m]$ (disegnato triangolare, di altezza 1)*

> 🧮 Formula chiave — **Teorema del campionamento**
> **Ipotesi:** $x_a(t)$ a banda **rigorosamente limitata** con banda monolatera $B_x = f_m$; $f_c = 1/T_c \ge 2f_m$; $x(n) = x_a(nT_c)$.
> **Tesi:** $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n)$.
> La minima frequenza di campionamento $f_{c,\min} = 2f_m$ è la **frequenza di Nyquist** di $x_a(t)$.

## Formule · [[Campionamento_AD_DA.pdf#page=11|p. 11]]–[[Campionamento_AD_DA.pdf#page=13|13]], [[Campionamento_AD_DA.pdf#page=15|p. 15]]

| Formula | Significato |
|---|---|
| $x_\delta(t) = x_a(t)\sum_n\delta(t-nT_c) = \sum_n x_a(nT_c)\,\delta(t-nT_c)$ | segnale campionato idealmente |
| $\sum_n\delta(t-nT_c) \xleftrightarrow{FT} \frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)$ | trasformata del pettine di delta |
| $X_\delta(f) = \frac{1}{T_c}\sum_{k=-\infty}^{+\infty}X_a\left(f-\frac{k}{T_c}\right)$ | spettro periodico, periodo $f_c$ |
| $f_c \ge 2f_m$ | condizione di Nyquist |
| $H_r(f) = T_c\,\Pi\left(\frac{f}{2f_r}\right)$, $f_m\le f_r\le f_c-f_m$ | filtro di ricostruzione (LPF ideale) |

Simboli: $\delta(\cdot)$ = impulso di Dirac; $\Pi(x)$ = rettangolo unitario (1 per $|x|<1/2$); $X_a(f)$ = trasformata di Fourier di $x_a(t)$; $f_r$ = frequenza di taglio del filtro [Hz].

## Derivazioni

### Derivazione — Forma del segnale campionato idealmente · [[Campionamento_AD_DA.pdf#page=11|p. 11]]
$$
\begin{aligned}
x_\delta(t) &= x_a(t)\sum_n\delta(t-nT_c) && \text{1° stadio: prodotto per il pettine} \\
&= \sum_n x_a(t)\,\delta(t-nT_c) && \text{linearità} \\
&= \sum_n x_a(nT_c)\,\delta(t-nT_c) && \text{proprietà del campionamento della } \delta:\ g(t)\delta(t-t_0) = g(t_0)\delta(t-t_0)
\end{aligned}
$$

### Derivazione — Trasformata del pettine di delta · [[Campionamento_AD_DA.pdf#page=12|p. 12]]
> 🧩 Derivazione mia (richiamo di teoria dei segnali)
$$
\begin{aligned}
\textstyle\sum_n\delta(t-nT_c) &= \textstyle\sum_k c_k\,e^{j2\pi k t/T_c} && \text{segnale periodico di periodo } T_c \Rightarrow \text{serie di Fourier} \\
c_k &= \frac{1}{T_c}\int_{-T_c/2}^{T_c/2}\delta(t)\,e^{-j2\pi kt/T_c}dt = \frac{1}{T_c} && \text{nel periodo c'è solo } \delta(t) \\
\textstyle\sum_n\delta(t-nT_c) &= \frac{1}{T_c}\textstyle\sum_k e^{j2\pi kf_ct} \xleftrightarrow{FT} \frac{1}{T_c}\textstyle\sum_k\delta(f-kf_c) && e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)
\end{aligned}
$$

### Derivazione — Spettro del segnale campionato · [[Campionamento_AD_DA.pdf#page=12|p. 12]]
$$
\begin{aligned}
X_\delta(f) &= X_a(f) * \left[\frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)\right] && \text{prodotto nel tempo} \leftrightarrow \text{convoluzione in frequenza} \\
&= \frac{1}{T_c}\sum_k X_a(f)*\delta(f-kf_c) && \text{linearità} \\
&= \frac{1}{T_c}\sum_k X_a(f-kf_c) && X*\delta(f-f_0) = X(f-f_0)
\end{aligned}
$$
Il risultato è la **replicazione** di $X_a(f)$ con passo $f_c = 1/T_c$ e ampiezza scalata di $1/T_c$: uno spettro **periodico** di periodo $f_c$.

Conseguenze tratte dalla slide:
- l'invertibilità del campionamento equivale a stabilire **quando $X_a(f)$ si può ottenere univocamente dalla sua replicazione** con passo $f_c$;
- in generale la relazione tra "generatore" e replicazione **non è univoca**: generatori diversi possono dare la stessa replicazione;
- per questo si **assume** che $x_a(t)$ sia a **banda rigorosamente limitata**, con banda monolatera $B_x = f_m$, e si studia il problema **graficamente** al variare di $f_c$ (i tre casi qui sotto).

### Derivazione — Condizione $f_c\ge2f_m$ · [[Campionamento_AD_DA.pdf#page=13|p. 13]]
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
*I tre casi: (a) $f_c>2f_m$, repliche separate da una banda di guardia $f_c-2f_m$; (b) $f_c=2f_m$, repliche che si toccano in $f_c/2$; (c) $f_c<2f_m$, repliche sovrapposte ([[aliasing]]).*

### Derivazione — Caso limite: un coseno campionato esattamente a $f_c = 2f_0$ · [[Campionamento_AD_DA.pdf#page=13|p. 13]], [[Campionamento_AD_DA.pdf#page=14|14]], [[Campionamento_AD_DA.pdf#page=17|p. 17]]
> 🧩 Esempio e derivazione miei: approfondiscono il caso (b) della figura sopra, $f_c = 2f_m$, che il teorema ammette con il "$\ge$".

**Domanda:** $x(t) = \cos(2\pi f_0 t + \varphi)$, per esempio con $f_0 = \pi$ Hz, campionato alla frequenza di Nyquist $f_c = 2f_0 = 2\pi$ Hz, cioè $T_c = \frac{1}{2f_0}$. Si perde informazione? L'interpolazione ideale restituisce $x(t)$?

**I campioni:**
$$
\begin{aligned}
x(n) &= \cos\Big(2\pi f_0\,\frac{n}{2f_0} + \varphi\Big) && t = nT_c = \frac{n}{2f_0} \\
&= \cos(\pi n + \varphi) && \text{il coseno fa mezzo periodo tra un campione e l'altro} \\
&= \cos(\pi n)\cos\varphi - \sin(\pi n)\sin\varphi && \text{formula di addizione} \\
&= (-1)^n\cos\varphi && \cos(\pi n) = (-1)^n,\ \sin(\pi n) = 0
\end{aligned}
$$
La parte in $\sin\varphi$ sparisce: i campioni cadono sempre dove il seno vale zero. Dai campioni si legge **solo** $\cos\varphi$, non $\varphi$.

**La ricostruzione ideale** (serie di Shannon) con questi campioni dà:
$$x_r(t) = \sum_n (-1)^n\cos\varphi\ \text{sinc}\Big(\frac{t - nT_c}{T_c}\Big) = \cos\varphi\,\cos(2\pi f_0 t)$$
Il secondo passaggio usa l'identità $\sum_n (-1)^n\,\text{sinc}(x - n) = \cos(\pi x)$, verificata numericamente (scarto $< 10^{-4}$).

**Cosa succede al variare della fase:**
- **$\varphi = 0$** (coseno "puro"): i campioni cadono sui picchi, $\pm 1$, e $x_r(t) = \cos(2\pi f_0 t) = x(t)$. **Ricostruzione perfetta**, ma per una coincidenza di fase.
- **$\varphi = 45°$:** $x_r(t) = 0.71\cos(2\pi f_0 t)$. Ampiezza sbagliata e fase persa: il ricostruito è un coseno con fase 0, non $45°$.
- **$\varphi = 90°$**, cioè $x(t) = -\sin(2\pi f_0 t)$: tutti i campioni valgono 0 e $x_r(t) = 0$. **Il segnale sparisce del tutto.**

**Il perché in frequenza.** $x(t)$ ha due righe: $\frac{1}{2}e^{j\varphi}$ in $+f_0$ e $\frac{1}{2}e^{-j\varphi}$ in $-f_0$. Campionando, lo spettro si replica ogni $f_c = 2f_0$. La replica della riga in $-f_0$ finisce in $-f_0 + f_c = +f_0$: **esattamente sopra** la riga in $+f_0$. Le repliche "si toccano" proprio dove sta il segnale, e le due righe si sommano:
$$\tfrac{1}{2}e^{j\varphi} + \tfrac{1}{2}e^{-j\varphi} = \cos\varphi$$
Resta un numero reale: la fase è persa. È una forma di aliasing al bordo della banda.

![[grafico-nyquist-limite-coseno.gif]]
*🧩 Animazione mia (script `output/grafici/genera_grafici_nyquist_limite.py`): $f_0 = \pi$ Hz, $f_c = 2\pi$ Hz, fase $\varphi$ che va da $0°$ a $180°$.*
- *In alto: il segnale (grigio), i campioni (arancio) e il ricostruito ideale (blu). A $0°$ coincidono; a $90°$ i campioni sono tutti nulli e il ricostruito è piatto; a $180°$ il ricostruito torna intero perché $\cos\varphi = -1$ e il segnale è $-\cos(2\pi f_0 t)$.*
- *In basso a sinistra: i due fasori in $f_c/2$ (blu $\frac12 e^{j\varphi}$, verde $\frac12 e^{-j\varphi}$) e la loro somma (rosso), sempre sull'asse reale.*
- *In basso a destra: l'ampiezza ricostruita $\cos\varphi$ contro quella vera, 1.*

**Conclusione:**
- campionando un coseno esattamente a $2f_0$ **si perde informazione**: la fase, e con lei l'ampiezza apparente;
- l'interpolazione ideale restituisce il segnale di partenza **solo se** $\varphi = 0$ o $\varphi = \pi$, cioè se i campioni cadono sui picchi;
- per una sinusoide (o qualunque riga spettrale) proprio a $f_m$ serve $f_c > 2f_m$ **strettamente**.

Il "$\ge$" del teorema resta valido per segnali con spettro **continuo**: lì il punto $f = f_m$ ha energia nulla, e la sovrapposizione in un solo punto non conta. Diventa un problema solo quando c'è una riga, cioè una delta, proprio sul bordo. In pratica il caso limite si evita comunque sovracampionando (sezione «Effetti pratici» sotto).

**Ipotesi:** campionamento ideale e interpolatore ideale a durata infinita; nessun rumore.

### Derivazione — Ricostruzione perfetta con LPF ideale · [[Campionamento_AD_DA.pdf#page=15|p. 15]]
$$
\begin{aligned}
X_r(f) &= H_r(f)\,X_\delta(f) = T_c\,\Pi\!\left(\tfrac{f}{2f_r}\right)\cdot\frac{1}{T_c}\sum_k X_a(f-kf_c) && \text{filtraggio LTI} \\
&= \Pi\!\left(\tfrac{f}{2f_r}\right)\sum_kX_a(f-kf_c) && T_c \text{ compensa } 1/T_c \\
&= X_a(f) && \text{se } f_r\ge f_m \text{ (passa la replica 0) e } f_r\le f_c-f_m \text{ (blocca la replica } \pm1)
\end{aligned}
$$
L'intervallo $[f_m,\,f_c-f_m]$ non è vuoto solo se $f_c\ge2f_m$. Scelta comune: $f_r = f_c/2$, il centro dell'intervallo.

![[campionamento-p15-filtro-ricostruzione.png]]
*Ricostruzione del segnale TC: (a) $X_\delta(f)$, repliche di altezza $1/T_c$ centrate in $0, \pm f_c, \dots$; (b) $H_r(f)$, rettangolo di altezza $T_c$ tra $-f_c/2$ e $f_c/2$; (c) $X_r(f) = X_a(f)$, la sola replica centrale riportata ad altezza 1.*
**Sanity check:** con $f_c = 2f_m$ l'intervallo si riduce al punto $f_r = f_m = f_c/2$ e il filtro deve essere perfettamente ideale.
**Ipotesi:** banda rigorosamente limitata; campionamento e filtro ideali (vedi [[aliasing]] e [[interpolazione]] per i casi reali).

## Spiegazione

### Intuizione · [[Campionamento_AD_DA.pdf#page=9|p. 9]], [[Campionamento_AD_DA.pdf#page=10|10]]

**Scelta di $f_c$**: è fondamentale per avere una buona rappresentazione del segnale e per poterlo ricostruire dai campioni a tempo discreto.
- $T_c$ **troppo grande** per un segnale che varia rapidamente (larga banda): i campioni non seguono le oscillazioni.
- $T_c$ **adeguato** per un segnale che varia lentamente (banda stretta): i campioni descrivono bene l'andamento.
- Quindi $f_c = 1/T_c$ va scelta **proporzionale alla rapidità di variazione** del segnale nel tempo, o equivalentemente alla sua **banda** in frequenza. È l'osservazione intuitiva alla base del teorema del campionamento.

![[campionamento-p9-scelta-fc.png]]

**Invertibilità del campionamento**: dai campioni $x(n)$ si può ricostruire il segnale TC originale $x_a(t)$?
- A prima vista **no**: esistono **infiniti** segnali TC che hanno gli stessi campioni $x(n)$ (es. $x_{a1}(t)$ e $x_{a2}(t)$ in figura), quindi servono condizioni aggiuntive.
- Con **ulteriori assunzioni** su $x_a(t)$ e una **scelta opportuna** di $f_c = 1/T_c$, $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n) = x_a(nT_c)$.
- Questo risultato fondamentale è la tesi del **teorema del campionamento**, o **teorema di Shannon**.

![[campionamento-p10-invertibilita.png]]

### Modello a due stadi · [[Campionamento_AD_DA.pdf#page=11|p. 11]]

Per dimostrare il teorema conviene schematizzare il campionamento in **due stadi**:
1. $x_a(t)$ viene moltiplicato per un **pettine di delta** $\Delta_{T_c}(t)$ di periodo $T_c$, e si ottiene $x_\delta(t)$ (ancora TC);
2. da $x_\delta(t)$ si estraggono i campioni $x(n) = x(nT_c)$: nello schema è il blocco "convertitore $\delta/n$", che trasforma il treno di impulsi nella sequenza.

È un modello utile per lo studio matematico, **senza alcun riscontro pratico**. Il segnale TC $x_\delta(t)$ si chiama **campionamento ideale**. Studiare l'invertibilità del campionamento equivale a studiare quella del **primo stadio**, perché il secondo è solo un cambio di rappresentazione.

![[campionamento-p11-campionamento-ideale.png]]
*Schema a due stadi e segnale $x_\delta(t)$: impulsi negli istanti $nT_c$, con aree pari ai campioni (inviluppo tratteggiato = $x_a(t)$)*

### Effetti pratici · [[Campionamento_AD_DA.pdf#page=16|p. 16]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]

$f_c$ cresce **linearmente** con la banda:

| Segnale | $f_m$ | $f_c \ge 2f_m$ |
|---|---|---|
| Voce | 4 kHz | 8 kHz |
| Audio | 20 kHz | 40 kHz |
| Video | 5 MHz | 10 MHz |

Al crescere di $f_c$ crescono il **costo dell'hardware** (campionatore) e il **numero di campioni** generati (ingombro di memoria).

**Esempio**: 1 minuto di audio mono campionato a $f_c = 44.1$ kHz corrisponde a $60\times44\,100 = 2\,646\,000$ campioni. Il valore **raddoppia** per un segnale stereo (canali L e R). Svolgimento in [[campionamento-e-aliasing]].

**Sovracampionamento** (*oversampling*): campionare con $f_c$ maggiore della frequenza di Nyquist. Non conviene per complessità e costo, ma può essere vantaggioso contro alcuni problemi pratici. Per esempio riduce l'aliasing dei segnali a banda non rigorosamente limitata (vedi [[aliasing]]).

> 🎯 Esame: enunciato completo con ipotesi e tesi; dimostrazione grafica/spettrale; ruolo del guadagno $T_c$ del filtro; perché $f_r\in[f_m, f_c-f_m]$.

## Perché importa · [[Campionamento_AD_DA.pdf#page=31|p. 31]]

Stabilisce quanti campioni al secondo servono per rappresentare un segnale senza perdite. Insieme al numero di bit per campione ([[quantizzazione-uniforme]]) fissa il bit rate prodotto dalla conversione A/D.

## Connessioni · Intro [[Intro.pdf#page=15|p. 15]] · Rice [[Rappresentazione_Rice.pdf#page=9|p. 9]]

- [[lab-campionamento]] — 🧪 laboratorio (non d'esame): campionamento simulato, repliche dello spettro e un caso in cui l'arrotondamento porta $f_s$ sotto $2W$.
- [[aliasing]] — cosa succede quando le ipotesi cadono.
- [[interpolazione]] — la ricostruzione $x_r(t)$ nel dominio del tempo (serie di Shannon).
- [[conversione-ad-da]] — il campionamento è la prima metà della conversione A/D.
- [[sistema-comunicazione-digitale]] — il campionamento è il primo passo della conversione A/D svolta dal codificatore di sorgente.
- [[inviluppo-complesso]] — un segnale passa-banda va campionato a $f_c \ge 2 f_{max}$ (qui $f_{max}$ è la sua frequenza massima), il suo inviluppo complesso a una frequenza molto più bassa; il confronto è ricavato in quella pagina. Attenzione alla notazione: qui $f_c$ è la frequenza di campionamento, là è la portante.

## Fonti · [[Campionamento_AD_DA.pdf#page=7|p. 7]], [[Campionamento_AD_DA.pdf#page=16|p. 16]]

- [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-10-12 — caso limite $f_c = 2f_0$ per un coseno, con derivazione e animazione; 2026-09-30 — collegamento al laboratorio Matlab; 2026-09-25 — collegamento con l'inviluppo complesso; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
