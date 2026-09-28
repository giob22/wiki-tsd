---
tipo: concetto
importanza_esame: media
prerequisiti: ["variabile-aleatoria", "probabilita-condizionale"]
fonti_pdf: ["Probabilità.pdf#page=31", "Probabilità.pdf#page=32", "Probabilità.pdf#page=33", "Probabilità.pdf#page=34", "Probabilità.pdf#page=35"]
---

# Coppie di variabili aleatorie

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=31]]

Una **coppia di v.a.** è formata da due funzioni definite sullo stesso $\Omega$:
$$(X,Y): \omega\in\Omega \to (X(\omega), Y(\omega)) \in \mathbb{R}\times\mathbb{R}$$
Le CDF marginali $F_X$ e $F_Y$ descrivono le singole v.a. ma **non** la loro relazione. Per quella servono le funzioni congiunte.

![[probabilita-p31-coppia-va.png]]

## Formule

| Grandezza | Definizione | Pagina |
|---|---|---|
| CDF congiunta | $F_{XY}(x,y) \triangleq P(X\le x, Y\le y)$ | [[Probabilità.pdf#page=31]] |
| pdf congiunta | $f_{XY}(x,y) \triangleq \dfrac{\partial^2 F_{XY}(x,y)}{\partial x\,\partial y}$ | [[Probabilità.pdf#page=31]] |
| pdf condizionale | $f_X(x\|y) \triangleq \dfrac{f_{XY}(x,y)}{f_Y(y)}$, $\quad f_Y(y\|x) \triangleq \dfrac{f_{XY}(x,y)}{f_X(x)}$ | [[Probabilità.pdf#page=34]] |
| indipendenza | $f_{XY}(x,y) = f_X(x)\,f_Y(y)$ | [[Probabilità.pdf#page=35]] |

Unità: $f_{XY}$ ha dimensione $[X]^{-1}[Y]^{-1}$.

**Proprietà di base** ([[Probabilità.pdf#page=32]]):
1. $F_X(x) = F_{XY}(x,+\infty)$ — CDF marginale di $X$
2. $F_Y(y) = F_{XY}(+\infty,y)$
3. $f_X(x) = \int_{-\infty}^{+\infty} f_{XY}(x,y)\,dy$ — pdf marginale
4. $f_Y(y) = \int_{-\infty}^{+\infty} f_{XY}(x,y)\,dx$
5. $\iint f_{XY}\,dx\,dy = 1$
6. $P((X,Y)\in A) = \iint_A f_{XY}(x,y)\,dx\,dy$
7. $F_{XY}(x,y) = \int_{-\infty}^x\int_{-\infty}^y f_{XY}(u,v)\,du\,dv$

**Proprietà della CDF congiunta** ([[Probabilità.pdf#page=33]]):
1. $F(-\infty,y) = F(x,-\infty) = 0$, $F(+\infty,+\infty) = 1$
2. $P(x_1<X\le x_2, Y\le y) = F(x_2,y) - F(x_1,y)$ (analoga in $y$)
3. $P(x_1<X\le x_2,\ y_1<Y\le y_2) = F(x_2,y_2) - F(x_1,y_2) - F(x_2,y_1) + F(x_1,y_1)$
   — regola mnemonica: "+" per le coppie concordi ($x_1y_1$, $x_2y_2$), "−" per le discordi.

## Derivazioni

> 🧩 Derivazione mia: le slide riassumono le proprietà senza dimostrarle.

### Derivazione — CDF marginale (prop. 1)
$\{Y\le+\infty\} = \Omega$, quindi $F_{XY}(x,+\infty) = P(\{X\le x\}\cap\Omega) = P(X\le x) = F_X(x)$.

### Derivazione — pdf marginale (prop. 3)
$$
\begin{aligned}
F_X(x) &= F_{XY}(x,+\infty) = \int_{-\infty}^{x}\left[\int_{-\infty}^{+\infty} f_{XY}(u,v)\,dv\right]du && \text{prop. 1 + prop. 7} \\
f_X(x) &= \frac{dF_X}{dx} = \int_{-\infty}^{+\infty} f_{XY}(x,v)\,dv && \text{teorema fondamentale del calcolo}
\end{aligned}
$$

### Derivazione — Probabilità di un rettangolo (prop. 3 della CDF)
$$
\begin{aligned}
P(x_1<X\le x_2,\ y_1<Y\le y_2) &= P(x_1<X\le x_2, Y\le y_2) - P(x_1<X\le x_2, Y\le y_1) && \{Y\le y_2\} = \{Y\le y_1\}\cup\{y_1<Y\le y_2\} \\
&= [F(x_2,y_2)-F(x_1,y_2)] - [F(x_2,y_1)-F(x_1,y_1)] && \text{prop. 2 applicata due volte}
\end{aligned}
$$

### Derivazione — Normalizzazione delle pdf condizionali
**Fonte:** [[Probabilità.pdf#page=34]]
$$
\int_{-\infty}^{+\infty} f_X(x|y)\,dx = \frac{1}{f_Y(y)}\int f_{XY}(x,y)\,dx = \frac{f_Y(y)}{f_Y(y)} = 1 \qquad \text{(prop. 4 delle marginali)}
$$

### Derivazione — Indipendenza ⇒ condizionale = marginale
**Fonte:** [[Probabilità.pdf#page=35]]
$$f_X(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)} = \frac{f_X(x)f_Y(y)}{f_Y(y)} = f_X(x)$$
Analogamente $f_Y(y|x) = f_Y(y)$.

## Spiegazione

- **Pdf condizionale** ([[Probabilità.pdf#page=34]]): dice come cambia la distribuzione di $Y$ quando si fissa $\{X=x\}$. Esempio della slide: il peso $Y$ di una persona di cui si conosce l'altezza $X$. È l'analogo per densità di $P(A|B)$ ([[probabilita-condizionale]]).
- **Indipendenza** ([[Probabilità.pdf#page=35]]): la fattorizzazione si può scrivere in modo equivalente con la CDF congiunta ($F_{XY} = F_XF_Y$) o con la DF congiunta per v.a. discrete.
- Dalla congiunta si ricavano sempre le marginali. Il viceversa vale **solo** se c'è indipendenza.

> 🎯 Esame: marginali dalla congiunta, definizione di pdf condizionale, differenza tra indipendenza e incorrelazione (vedi [[correlazione-e-covarianza]]).

## Perché importa

Segnale e rumore, oppure due campioni successivi dello stesso segnale, sono coppie di v.a. La loro relazione statistica (indipendenza, correlazione) è la base dei **processi aleatori**, argomento del corso ([[Intro.pdf#page=3]]).

## Connessioni

- [[correlazione-e-covarianza]] — descrizione sintetica (momenti misti) della coppia.
- [[probabilita-totale-e-bayes]] — Bayes per densità: $f_X(x|y) = f_Y(y|x)f_X(x)/f_Y(y)$ (🧩 mio, combinando le due definizioni di [[Probabilità.pdf#page=34]]).
- [[media-e-varianza]] — il teorema fondamentale della media si estende alle coppie.
- [[processo-aleatorio]] — due campioni di un processo sono una coppia di v.a.; le marginali danno la coerenza delle distribuzioni di ordine $k$.

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=31]] – [[Probabilità.pdf#page=35]]

_Aggiornato: 2026-09-28 — collegamento al processo aleatorio; 2026-09-23 — creazione da ingest Probabilità.pdf_
