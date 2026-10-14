---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria"]
fonti_pdf: ["Probabilità.pdf#page=28", "Probabilità.pdf#page=29", "Probabilità.pdf#page=30"]
---

# Media statistica, momenti e varianza

## Definizione · [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=29|29]]

- **Media statistica** (valore atteso) di una v.a. $X$ con pdf $f(x)$: $E(X) \triangleq \int_{-\infty}^{+\infty}x\,f(x)\,dx$.
- **Momento $n$-esimo**: $\mu_n = E(X^n) \triangleq \int x^n f(x)\,dx$. Per $n=2$ si ha il **valor quadratico medio** $E(X^2)$.
- **Varianza**: $\text{Var}(X) = \sigma_X^2 \triangleq E[(X-E(X))^2]$.
- **Deviazione standard**: $\sigma_X \triangleq \sqrt{\text{Var}(X)}$.

Unità: $E(X)$ e $\sigma_X$ hanno l'unità di $X$ (es. V); $E(X^2)$ e $\text{Var}(X)$ il suo quadrato (es. V², che su 1 Ω è una potenza in W).

## Formule · [[Probabilità.pdf#page=28|p. 28]]–[[Probabilità.pdf#page=30|30]]

> 🧮 Formula chiave — **Teorema fondamentale della media**:
> $$E[g(X)] = \int_{-\infty}^{+\infty} g(x)\,f(x)\,dx \qquad \text{(discreto: } \textstyle\sum_i p(x_i)g(x_i))$$

> 🧮 Formula chiave:
> $$\text{Var}(X) = E(X^2) - E^2(X)$$

**Proprietà della media**, con $a,b$ costanti reali e $g,h$ funzioni reali:
1. Linearità: $E[a\,g(X)+b\,h(X)] = a\,E[g(X)]+b\,E[h(X)]$; in particolare $E(aX+b) = aE(X)+b$
2. $g(x)\ge0\ \forall x \Rightarrow E[g(X)]\ge0$
3. $g_1\ge g_2\ \forall x \Rightarrow E[g_1(X)]\ge E[g_2(X)]$
4. $a\le g(x)\le b\ \forall x \Rightarrow a\le E[g(X)]\le b$

**Proprietà della varianza**:
- $\text{Var}(aX+b) = a^2\,\text{Var}(X)$: non dipende da $b$ (invarianza per traslazione); $\sigma_Y = |a|\sigma_X$
- v.a. **centrata** $Y = X-\mu_X$: $E(Y)=0$, $\text{Var}(Y) = \text{Var}(X)$

## Derivazioni

### Derivazione — $\text{Var}(X) = E(X^2)-E^2(X)$ · [[Probabilità.pdf#page=29|p. 29]]
$$
\begin{aligned}
\text{Var}(X) &= E[(X-\mu)^2], \quad \mu \triangleq E(X) && \text{def.} \\
&= E[X^2 - 2\mu X + \mu^2] && \text{sviluppo il quadrato} \\
&= E(X^2) - 2\mu E(X) + \mu^2 && \text{linearità; } \mu \text{ costante} \\
&= E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2 && E(X)=\mu
\end{aligned}
$$
**Sanity check:** $\text{Var}\ge0 \Rightarrow E(X^2)\ge E^2(X)$, cioè la potenza totale è almeno quella della componente continua.

### Derivazione — $\text{Var}(aX+b) = a^2\text{Var}(X)$ · [[Probabilità.pdf#page=30|p. 30]]
$$
\begin{aligned}
E(aX+b) &= a\mu + b && \text{linearità} \\
\text{Var}(aX+b) &= E[(aX + b - a\mu - b)^2] && \text{def.} \\
&= E[a^2(X-\mu)^2] = a^2\,\text{Var}(X) && b \text{ si cancella}
\end{aligned}
$$

### Derivazione — Linearità della media
Dal teorema fondamentale: $\int[a g(x)+b h(x)]f(x)dx = a\int g f + b\int h f$ (linearità dell'integrale). Le proprietà 2–4 seguono da $f\ge0$ (monotonia dell'integrale) e da $\int f = 1$ (per la 4).

### Derivazione — Media e varianza della Gaussiana
Vedi [[variabile-aleatoria-gaussiana]] (derivazione $E(X)=\mu$, $\text{Var}(X)=\sigma^2$).

## Spiegazione · Probabilità [[Probabilità.pdf#page=23|p. 23]] · Campionamento [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- La media è il **baricentro** della pdf, la deviazione standard ne misura la **larghezza**.
- Il teorema fondamentale della media è molto comodo: per calcolare $E[g(X)]$ basta $f_X$ e non serve ricavare la pdf di $Y=g(X)$ ([[funzione-di-variabile-aleatoria]]).
- Lettura "elettrica" (🧩 mia; nelle slide appare in p. 29 come $x_{rms} = \sqrt{P_x}$): per un segnale modellato come v.a., $E(X)$ è la componente continua, $E(X^2)$ la potenza (valor quadratico medio) e, per una v.a. a media nulla, $\sigma_X = x_{rms}$ è il valore efficace.

> 🎯 Esame: il valor quadratico medio dell'errore di quantizzazione $E[e^2] = \Delta^2/12$ è una varianza di un'uniforme a media nulla ([[snr-di-quantizzazione]]).

Momenti delle v.a. notevoli: tabella in [[variabili-aleatorie-notevoli]].

## Perché importa

Potenza di segnale, potenza di rumore e SNR sono tutti momenti del secondo ordine. L'MSE che Lloyd-Max minimizza ([[quantizzazione-non-uniforme]]) è un valor quadratico medio; il centroide $E[x|x\in R_i]$ è una media condizionale.

## Connessioni

- [[correlazione-e-covarianza]] — estende media e varianza alle coppie di v.a.
- [[disuguaglianza-di-chebyshev]] — usa media e varianza per limitare le code della pdf.
- [[snr-di-quantizzazione]] — $P_x = E[x^2]$, $P_e = E[e^2]$.

## Fonti · [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=30|p. 30]]

- [[elementi-teoria-probabilita]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
