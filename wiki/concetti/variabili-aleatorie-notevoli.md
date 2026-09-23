---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria"]
fonti_pdf: ["Probabilità.pdf#page=20", "Probabilità.pdf#page=21", "Probabilità.pdf#page=22", "Probabilità.pdf#page=23"]
---

# Variabili aleatorie notevoli: Bernoulli, Binomiale, Uniforme (e Laplace)

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=20]] – [[Probabilità.pdf#page=23]], [[Campionamento_AD_DA.pdf#page=32]]

| V.a. | Tipo | Parametri | Valori | Uso tipico |
|---|---|---|---|---|
| **Bernoulli** $X\sim\text{Bern}(p)$ | discreta | $p\in[0,1]$, $q=1-p$ | $\{0,1\}$ | successo/insuccesso; simile all'indicatrice di un evento ([[Probabilità.pdf#page=20]]) |
| **Binomiale** $X\sim\mathcal{B}(n,p)$ | discreta | $n\in\mathbb{N}$, $p$ | $\{0,1,\dots,n\}$ | numero di successi in $n$ prove ripetute ([[Probabilità.pdf#page=21]]) |
| **Uniforme** $X\sim\mathcal{U}(a,b)$ | continua | $a<b$ | $(a,b)$ | nessuna preferenza fra i valori di un intervallo limitato ([[Probabilità.pdf#page=22]]) |
| **Gaussiana** $X\sim\mathcal{N}(\mu,\sigma)$ | continua | $\mu$, $\sigma>0$ | $\mathbb{R}$ | somma di molti contributi indipendenti → pagina dedicata [[variabile-aleatoria-gaussiana]] |
| **Laplace** | continua | $\lambda>0$ | $\mathbb{R}$ | ampiezze del segnale vocale ([[Campionamento_AD_DA.pdf#page=32]]) |

## Formule

| V.a. | DF / pdf | CDF | Pagina |
|---|---|---|---|
| Bernoulli | $p(0)=q,\ p(1)=p$ | derivata sotto | [[Probabilità.pdf#page=20]] |
| Binomiale | $p(k) = \binom{n}{k}p^k q^{n-k}$ | derivata sotto | [[Probabilità.pdf#page=21]] |
| Uniforme | $f(x)=\frac{1}{b-a}$ per $x\in(a,b)$, 0 altrove | $F(x) = 0,\ \frac{x-a}{b-a},\ 1$ per $x<a$, $a\le x<b$, $x\ge b$ | [[Probabilità.pdf#page=22]] |
| Laplace | $f_X(x) = \frac{\lambda}{2}e^{-\lambda\|x\|}$ | — | [[Campionamento_AD_DA.pdf#page=32]] |

Unità: $f$ in $[X]^{-1}$; per la Laplace $\lambda$ ha unità $[X]^{-1}$ (es. 1/V).

**Momenti** (🧩 Derivazione mia; le slide sulla probabilità non li calcolano, ma servono: la varianza dell'uniforme dà $\Delta^2/12$ in [[snr-di-quantizzazione]]):

| V.a. | $E(X)$ | $\text{Var}(X)$ |
|---|---|---|
| Bern($p$) | $p$ | $pq$ |
| $\mathcal{B}(n,p)$ | $np$ | $npq$ |
| $\mathcal{U}(a,b)$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Laplace($\lambda$) | $0$ | $\frac{2}{\lambda^2}$ |

## Derivazioni

Le CDF e pdf di Bernoulli e Binomiale sono esercizi lasciati al lettore nelle slide («Calcolare CDF e pdf», [[Probabilità.pdf#page=20]], [[Probabilità.pdf#page=21]]). Svolgimento completo in [[cdf-pdf-variabili-notevoli]]; qui i risultati:

$$
\begin{aligned}
\text{Bern:}\quad F(x) &= q\,u(x) + p\,u(x-1), & f(x) &= q\,\delta(x) + p\,\delta(x-1) \\
\text{Bin:}\quad F(x) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k}\,u(x-k), & f(x) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k}\,\delta(x-k)
\end{aligned}
$$

### Derivazione — Normalizzazione della Binomiale
**Fonte:** [[Probabilità.pdf#page=21]] (suggerisce di usare la potenza del binomio)
$$
\begin{aligned}
\sum_{k=0}^n p(k) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k} && \text{DF binomiale} \\
&= (p+q)^n && \text{sviluppo di Newton del binomio} \\
&= 1^n = 1 && p+q=1
\end{aligned}
$$

### Derivazione — Da dove viene la DF binomiale
> 🧩 Derivazione mia (la slide dà la formula senza giustificarla)

Faccio $n$ prove di Bernoulli **indipendenti**, ognuna con successo di probabilità $p$. Una sequenza *specifica* con $k$ successi e $n-k$ insuccessi ha probabilità $p^kq^{n-k}$, per l'indipendenza ([[probabilita-condizionale]]). Le sequenze con esattamente $k$ successi sono $\binom{n}{k}$ e sono eventi disgiunti; sommando si ottiene $p(k) = \binom nk p^kq^{n-k}$.

**Caso particolare** $n=1$: $p(0) = \binom10 q = q$ e $p(1) = \binom11 p = p$, cioè la Bernoulli ([[Probabilità.pdf#page=21]]).

### Derivazione — CDF dell'Uniforme
**Fonte:** [[Probabilità.pdf#page=22]] («si ottiene per integrazione»)
$$
\begin{aligned}
x<a:&\quad F(x) = \int_{-\infty}^x 0\,dy = 0 \\
a\le x<b:&\quad F(x) = \int_a^x \frac{1}{b-a}\,dy = \frac{x-a}{b-a} && \text{pdf costante in }(a,b) \\
x\ge b:&\quad F(x) = \int_a^b \frac{1}{b-a}\,dy = 1
\end{aligned}
$$
**Sanity check:** $F$ è continua in $a$ (vale 0) e in $b$ (vale 1), come deve per una v.a. continua.

### Derivazione — Media e varianza dell'Uniforme
> 🧩 Derivazione mia
$$
\begin{aligned}
E(X) &= \int_a^b \frac{x}{b-a}\,dx = \frac{b^2-a^2}{2(b-a)} = \frac{a+b}{2} && b^2-a^2=(b-a)(b+a) \\
E(X^2) &= \int_a^b \frac{x^2}{b-a}\,dx = \frac{b^3-a^3}{3(b-a)} = \frac{a^2+ab+b^2}{3} && b^3-a^3=(b-a)(a^2+ab+b^2) \\
\text{Var}(X) &= E(X^2) - E^2(X) && [[media-e-varianza]] \\
&= \frac{4(a^2+ab+b^2) - 3(a+b)^2}{12} && \text{denominatore comune} \\
&= \frac{a^2 - 2ab + b^2}{12} = \frac{(b-a)^2}{12}
\end{aligned}
$$
**Caso d'uso:** $a=-\Delta/2$, $b=\Delta/2$ → $\text{Var} = \Delta^2/12$, cioè la potenza del rumore di quantizzazione ([[Campionamento_AD_DA.pdf#page=30]]).

### Derivazione — Media e varianza di Bernoulli e Binomiale
> 🧩 Derivazione mia
$$
\begin{aligned}
\text{Bern:}\ E(X) &= 0\cdot q + 1\cdot p = p, \quad E(X^2) = p, \quad \text{Var} = p - p^2 = pq \\
\text{Bin:}\ X &= \textstyle\sum_{i=1}^n X_i,\ X_i \sim \text{Bern}(p) \text{ indip.} && \text{conteggio dei successi} \\
E(X) &= \textstyle\sum_i E(X_i) = np && \text{linearità} \\
\text{Var}(X) &= \textstyle\sum_i \text{Var}(X_i) = npq && X_i \text{ incorrelate, } [[correlazione-e-covarianza]]
\end{aligned}
$$

### Derivazione — Normalizzazione e varianza della Laplace
> 🧩 Derivazione mia
$$
\begin{aligned}
\int_{-\infty}^{\infty}\tfrac{\lambda}{2}e^{-\lambda|x|}dx &= 2\cdot\tfrac{\lambda}{2}\int_0^\infty e^{-\lambda x}dx = \lambda\cdot\tfrac1\lambda = 1 && \text{pdf pari} \\
E(X) &= 0 && \text{pdf pari} \\
E(X^2) &= 2\cdot\tfrac\lambda2\int_0^\infty x^2e^{-\lambda x}dx = \lambda\cdot\tfrac{2}{\lambda^3} = \tfrac{2}{\lambda^2} && \textstyle\int_0^\infty x^2e^{-\lambda x}dx = 2/\lambda^3
\end{aligned}
$$
Quindi $x_{rms} = \sqrt2/\lambda$: più $\lambda$ è grande, più la pdf è concentrata intorno allo zero.

![[grafico-laplace-pdf-lambda.png]]
*🧩 Grafico mio (formula di [[Campionamento_AD_DA.pdf#page=32]]): cuspide in 0 alta $\lambda/2$, code esponenziali; larghezza $\propto 1/\lambda$. Confronto con gaussiana e uniforme a pari potenza in [[quantizzazione-non-uniforme]].*

## Spiegazione

![[probabilita-p22-uniforme.png]]

- **Esempio uniforme** ([[Probabilità.pdf#page=22]]): un bus arriva a caso tra le 10:00 e le 10:15, quindi $X\sim\mathcal{U}(0,900)$ s (15 min × 60 s/min = 900 s). Per esempio $P(X\le 300\,\text{s}) = 300/900 = 1/3$ (🧩 mio).
- La Bernoulli è simile alla v.a. **indicatrice** di un evento $A$: vale 1 se $\omega\in A$, 0 altrimenti, con $p = P(A)$ ([[Probabilità.pdf#page=20]]).
- **Laplace e voce** ([[Campionamento_AD_DA.pdf#page=32]]): i valori vicini allo zero sono i più probabili, e per questo la quantizzazione uniforme non è ottima per la voce → [[quantizzazione-non-uniforme]].

## Perché importa

- Bernoulli/Binomiale: il numero di bit errati in un blocco di $n$ bit, con errori indipendenti di probabilità $p$, è Binomiale.
  > 🧩 Derivazione mia: applicazione naturale, non nelle slide.
- Uniforme: è il modello dell'errore di quantizzazione ([[snr-di-quantizzazione]]).
- Laplace: è il modello delle ampiezze della voce ([[companding]]).

## Connessioni

- [[variabile-aleatoria]] — definizioni di CDF, pdf, DF.
- [[variabile-aleatoria-gaussiana]] — la quarta v.a. notevole.
- [[media-e-varianza]] — i momenti in tabella.
- [[disuguaglianza-di-chebyshev]] — usata sul fattore di carico, vale per qualunque pdf.

## Fonti

- [[elementi-teoria-probabilita]], [[campionamento-conversione-ad-da]]
- [[Probabilità.pdf#page=20]] – [[Probabilità.pdf#page=23]], [[Campionamento_AD_DA.pdf#page=32]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf e Campionamento_AD_DA.pdf_
