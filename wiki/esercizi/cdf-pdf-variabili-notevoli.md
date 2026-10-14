---
tipo: esercizio
argomento: "Calcolo di CDF, pdf, momenti di v.a. e di funzioni di v.a."
difficoltà: media
---

# CDF e pdf di variabili aleatorie notevoli e trasformate

## Metodo

**V.a. discreta** con DF $p(x_i) = p_i$ ([[variabile-aleatoria]]):
1. CDF: somma di gradini, $F(x) = \sum_ip_i\,u(x-x_i)$, costante a tratti con salti di ampiezza $p_i$ in $x_i$;
2. pdf: derivata generalizzata, $f(x) = \sum_ip_i\,\delta(x-x_i)$;
3. verifica: $\sum_ip_i = 1$.

**V.a. continua** con pdf $f$:
1. CDF: $F(x) = \int_{-\infty}^xf$, **spezzando** l'integrale nei tratti in cui $f$ cambia espressione;
2. verifica: $F(-\infty)=0$, $F(+\infty)=1$, $F$ continua.

**Funzione di v.a.** $Y=g(X)$ ([[funzione-di-variabile-aleatoria]]):
1. radici $x_i(y)$ di $g(x)=y$;
2. $f_Y(y) = \sum_if_X(x_i)/|g'(x_i)|$;
3. controllo con media e varianza ($E(aX+b) = aE(X)+b$, $\text{Var}(aX+b) = a^2\text{Var}(X)$).

## Formule usate · [[Probabilità.pdf#page=16|p. 16]], [[Probabilità.pdf#page=18|p. 18]]–[[Probabilità.pdf#page=20|20]], [[Probabilità.pdf#page=22|p. 22]], [[Probabilità.pdf#page=24|p. 24]], [[Probabilità.pdf#page=27|p. 27]]

- Definizioni di CDF, pdf, DF → [[variabile-aleatoria]]
- DF Bernoulli e Binomiale, pdf Uniforme → [[variabili-aleatorie-notevoli]]
- $f_Y = \sum f_X(x_i)/|g'(x_i)|$ → [[funzione-di-variabile-aleatoria]]
- CDF gaussiana con erf → [[variabile-aleatoria-gaussiana]]

## Casi svolti

### Caso 1 — CDF e pdf della Bernoulli · [[Probabilità.pdf#page=20|p. 20]]
**Traccia**: $X\sim\text{Bern}(p)$, «Calcolare CDF e pdf».
> 🧩 Derivazione mia (esercizio lasciato al lettore)
$$
\begin{aligned}
F(x) = P(X\le x) &= \begin{cases}0 & x<0 && \text{nessun valore} \le x\\ q & 0\le x<1 && \text{solo } X=0\\ q+p = 1 & x\ge1 && \text{entrambi}\end{cases} \\
&= q\,u(x) + p\,u(x-1) && \text{forma compatta con gradini} \\
f(x) = \frac{dF}{dx} &= q\,\delta(x) + p\,\delta(x-1) && \frac{d}{dx}u(x-x_0) = \delta(x-x_0)
\end{aligned}
$$
**Sanity check:** salto $q$ in 0 e $p$ in 1, che sommano a 1 ✓; $F$ continua da destra ✓ (con $u(0) = 1$).

### Caso 2 — CDF e pdf della Binomiale · [[Probabilità.pdf#page=21|p. 21]]
**Traccia**: $X\sim\mathcal{B}(n,p)$, «Calcolare CDF e pdf»; verificare la normalizzazione.
> 🧩 Derivazione mia
$$
\begin{aligned}
F(x) &= \sum_{k\le x}p(k) = \sum_{k=0}^{\lfloor x\rfloor}\tbinom nkp^kq^{n-k} \quad (0\le x<n) && \text{prop. 2 della DF} \\
&= \sum_{k=0}^n\tbinom nkp^kq^{n-k}\,u(x-k) && \text{forma con gradini, valida } \forall x \\
f(x) &= \sum_{k=0}^n\tbinom nkp^kq^{n-k}\,\delta(x-k) \\
\sum_{k=0}^np(k) &= (p+q)^n = 1 && \text{binomio di Newton}
\end{aligned}
$$
**Esempio numerico** (🧩 mio): $n = 3$, $p = 0.5$: $p(k) = \binom3k/8 = 1/8, 3/8, 3/8, 1/8$ per $k = 0,1,2,3$. CDF: $1/8$, $1/2$, $7/8$, $1$ ✓.

### Caso 3 — CDF dell'Uniforme ed esempio del bus · [[Probabilità.pdf#page=22|p. 22]]
**Traccia**: $X\sim\mathcal{U}(a,b)$, ricavare la CDF per integrazione; bus tra le 10:00 e le 10:15.
**Svolgimento:** derivazione completa in [[variabili-aleatorie-notevoli]]:
$$F(x) = 0\ (x<a),\quad\frac{x-a}{b-a}\ (a\le x<b),\quad1\ (x\ge b)$$
**Numeri:** 15 min × 60 s/min = 900 s, quindi $X\sim\mathcal{U}(0,900\,\text{s})$ ✓. Probabilità di attendere al più 5 min (🧩): $F(300\,\text{s}) = 300/900 = 0.333$.

### Caso 4 — $Y = aX+b$ con $X$ gaussiana standard · [[Probabilità.pdf#page=27|p. 27]]
**Traccia**: $X\sim\mathcal{N}(0,1)$, calcolare la pdf di $Y = aX+b$.
**Svolgimento:** vedi [[funzione-di-variabile-aleatoria]] (derivazione passo-passo).
**Risultato:** $f_Y(y) = \frac{1}{\sqrt{2\pi a^2}}e^{-(y-b)^2/(2a^2)}$, cioè $Y\sim\mathcal{N}(b,|a|)$.

### Caso 5 — CDF gaussiana standard in Matlab · [[Probabilità.pdf#page=26|p. 26]]
**Traccia**: rappresentare la CDF di $\mathcal{N}(0,1)$.
**Svolgimento:** con $\mu=0$, $\sigma=1$ la formula $F(x) = \frac12[1+\text{erf}(\frac{x-\mu}{\sqrt2\sigma})]$ diventa `y = (1/2)*(1+erf(x/sqrt(2)))`.
**Sanity check** (🧩 mio): $F(0) = \frac12(1+0) = 0.5$, per simmetria ✓; $F(3)\approx1-Q(3)\approx0.99865$.

## Trappole · [[Probabilità.pdf#page=18|p. 18]]

- **Estremi di integrazione** nella CDF di pdf definite a tratti: per $x\ge b$ l'integrale si ferma a $b$, non a $x$.
- **Impulsi** negli estremi: $P(x_1<X\le x_2) = \int_{x_1}^{x_2}f$ vale solo se si gestiscono gli eventuali impulsi in $x_1$ e $x_2$.
- Nella formula di $f_Y$ il modulo $|g'|$ è necessario: senza, per $a<0$ la pdf verrebbe negativa.
- La notazione $\mathcal{N}(\mu,\sigma)$ delle slide usa $\sigma$, **non** $\sigma^2$.
- Per le v.a. discrete la pdf esiste solo in senso generalizzato (con le $\delta$).

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
