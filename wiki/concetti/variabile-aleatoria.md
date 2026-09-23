---
tipo: concetto
importanza_esame: alta
prerequisiti: ["spazio-di-probabilita"]
fonti_pdf: ["Probabilità.pdf#page=15", "Probabilità.pdf#page=16", "Probabilità.pdf#page=17", "Probabilità.pdf#page=18", "Probabilità.pdf#page=19"]
---

# Variabile aleatoria: CDF, pdf, DF

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=15]]

Una **variabile aleatoria** (v.a.) è una funzione definita sullo spazio campione a valori nei reali estesi:
$$X: \omega \in \Omega \to X(\omega) \in \overline{\mathbb{R}} = \mathbb{R}\cup\{-\infty,+\infty\}$$
Serve a descrivere in forma numerica i risultati di un esperimento aleatorio, con $\Omega$ discreto o continuo e legge $P(\cdot)$.

![[probabilita-p15-variabile-aleatoria.png]]

## Formule

| Funzione | Definizione | Pagina |
|---|---|---|
| **CDF** (funzione di distribuzione cumulativa) | $F_X(x) \triangleq P(X \le x),\ \forall x\in\mathbb{R}$ | [[Probabilità.pdf#page=16]] |
| **pdf** (densità di probabilità) | $f_X(x) \triangleq \dfrac{d}{dx}F_X(x)$ (derivata generalizzata) | [[Probabilità.pdf#page=18]] |
| **DF / pmf** (distribuzione / "massa" di probabilità) | $p_X(x) \triangleq P(X = x)$ | [[Probabilità.pdf#page=19]] |

$F_X$ e $p_X$ sono adimensionali. $f_X$ ha le dimensioni di $[X]^{-1}$ (es. 1/V se $X$ è una tensione), perché $f_X(x)\,dx$ è una probabilità.

**Proprietà della CDF** ([[Probabilità.pdf#page=16]]):
1. $F(+\infty) = 1$, $F(-\infty) = 0$
2. monotona crescente (non strettamente): $x_1 < x_2 \Rightarrow F(x_1)\le F(x_2)$
3. $P(X>x) = 1-F(x)$ (CDF complementare o *funzione di affidabilità*)
4. continua da destra: $F(x^+) = F(x)$
5. $P(x_1 < X \le x_2) = F(x_2) - F(x_1)$
6. $P(X = x) = F(x) - F(x^-)$

**Proprietà della pdf** ([[Probabilità.pdf#page=18]]):
1. $f(x)\ge0$
2. $F(x) = \int_{-\infty}^{x} f(y)\,dy$
3. $\int_{-\infty}^{+\infty} f(x)\,dx = 1$
4. $P(x_1<X\le x_2) = \int_{x_1}^{x_2} f(x)\,dx$ (attenzione a eventuali impulsi in $x_1$ o $x_2$)
5. $P(x\le X\le x+\Delta x)\approx f(x)\Delta x \Rightarrow f(x) = \lim_{\Delta x\to0}\dfrac{P(x\le X\le x+\Delta x)}{\Delta x}$

**Proprietà della DF** ([[Probabilità.pdf#page=19]]): $p(x)\ge0$; $F(x) = \sum_{u\le x}p(u)$; $\sum_u p(u) = 1$; $P(x_1<X\le x_2) = \sum_{x_1<u\le x_2}p(u)$.

## Derivazioni

> 🧩 Derivazione mia: le slide elencano le proprietà senza dimostrarle.

### Derivazione — Proprietà 5 della CDF
$$
\begin{aligned}
\{X\le x_2\} &= \{X\le x_1\} \cup \{x_1 < X \le x_2\} && x_1<x_2,\ \text{unione disgiunta} \\
F(x_2) &= F(x_1) + P(x_1<X\le x_2) && \text{additività} \\
\Rightarrow P(x_1<X\le x_2) &= F(x_2) - F(x_1)
\end{aligned}
$$
La proprietà 2 segue subito: $F(x_2)-F(x_1)$ è una probabilità, quindi $\ge 0$.

### Derivazione — Proprietà 3 della CDF
$\{X>x\}$ è il complementare di $\{X\le x\}$, quindi $P(X>x) = 1 - P(X\le x) = 1 - F(x)$ (proprietà 3 di [[spazio-di-probabilita]]).

### Derivazione — Proprietà 6 della CDF
$$
\begin{aligned}
P(X = x) &= \lim_{\varepsilon\to0^+} P(x-\varepsilon < X \le x) && \{X=x\} = \textstyle\bigcap_\varepsilon \{x-\varepsilon<X\le x\} \\
&= \lim_{\varepsilon\to0^+} [F(x) - F(x-\varepsilon)] && \text{prop. 5} \\
&= F(x) - F(x^-)
\end{aligned}
$$
Quindi $P(X=x)$ è l'**ampiezza del salto** della CDF in $x$.

### Derivazione — Proprietà 5 della pdf
$$
\begin{aligned}
P(x < X\le x+\Delta x) &= F(x+\Delta x) - F(x) && \text{prop. 5 CDF} \\
&= F'(x)\,\Delta x + o(\Delta x) && \text{Taylor al 1° ordine} \\
&\approx f(x)\,\Delta x && f = F'
\end{aligned}
$$
**Ipotesi:** $F$ derivabile in $x$, cioè nessun impulso della pdf in $x$.

### Derivazione — Proprietà 3 della pdf
Dalla 2 e da $F(+\infty)=1$: $\int_{-\infty}^{+\infty}f = F(+\infty) = 1$.

## Spiegazione

### Tipi di v.a. e valore di $P(X=x)$
> 📄 Fonte: [[Probabilità.pdf#page=17]] («Discussione del valore assunto da $P(X=x)$ nei tre casi», lasciata alla lezione)

| Tipo | CDF | pdf | $P(X=x)$ |
|---|---|---|---|
| **Discreta** | costante a tratti: $F(x) = \sum_i p_i\,u(x-x_i)$ | $f(x) = \sum_i p_i\,\delta(x-x_i)$ ([[Probabilità.pdf#page=18]]) | $p_i$ se $x=x_i$, 0 altrove |
| **Continua** | continua | senza impulsi | $0$ per ogni $x$ |
| **Mista** | discontinua ma non costante a tratti | parte continua + impulsi | $\neq 0$ solo nei punti di salto |

Simboli: $u(\cdot)$ = gradino unitario, $\delta(\cdot)$ = impulso di Dirac, $p_i = P(X=x_i)$.

> 🧩 Derivazione mia (la colonna $P(X=x)$): discende direttamente dalla prop. 6. Se $F$ è continua in $x$ il salto è nullo. Per una v.a. continua anche l'evento "$X$ vale esattamente $x$" ha probabilità zero, pur non essendo impossibile.

La DF "ha senso solo per v.a. discrete" e va calcolata solo nei punti $x=x_i$, altrove è nulla ([[Probabilità.pdf#page=19]]).

### Esempio di v.a. mista
> 🧩 Derivazione mia (esempio non nelle slide): l'uscita di un [[quantizzazione-uniforme|quantizzatore]] con saturazione applicata a un ingresso gaussiano. È discreta; se invece si satura *senza* quantizzare, $Y = \min(X, X_{max})$ ha una parte continua più un impulso di area $P(X\ge X_{max})$ in $X_{max}$, quindi è mista.

## Perché importa

Campioni di segnale, rumore ed errore di quantizzazione sono tutti modellati come v.a. Il modello $e(n)\sim\mathcal{U}(-\Delta/2,\Delta/2)$ è una pdf ([[snr-di-quantizzazione]]); la probabilità di sovraccarico è una CDF complementare ([[quantizzazione-uniforme]]).

## Connessioni

- [[variabili-aleatorie-notevoli]] — CDF/pdf/DF di Bernoulli, Binomiale, Uniforme.
- [[variabile-aleatoria-gaussiana]] — la CDF non ha forma chiusa, quindi servono erf/erfc/Q.
- [[funzione-di-variabile-aleatoria]] — pdf di $Y=g(X)$.
- [[media-e-varianza]] — descrizione sintetica della pdf.

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=15]] – [[Probabilità.pdf#page=19]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
