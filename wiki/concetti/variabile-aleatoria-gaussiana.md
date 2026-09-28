---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria", "media-e-varianza"]
fonti_pdf: ["Probabilità.pdf#page=23", "Probabilità.pdf#page=24", "Probabilità.pdf#page=25", "Probabilità.pdf#page=26"]
---

# Variabile aleatoria Gaussiana e funzioni erf, erfc, Q

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=23]]

$X \sim \mathcal{N}(\mu,\sigma)$ (normale) è una v.a. continua con pdf a campana
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad x\in\mathbb{R}$$
- $\mu\in\mathbb{R}$: "baricentro" della pdf, cioè la media $E(X)$ ([[Probabilità.pdf#page=28]]);
- $\sigma>0$: "larghezza" della pdf, cioè la deviazione standard, con $\sigma^2 = \text{Var}(X)$ ([[Probabilità.pdf#page=29]]).

Descrive fenomeni che sono la somma di un gran numero di contributi indipendenti: **teorema centrale del limite** (CLT) — [[Probabilità.pdf#page=23]].

> ⚠️ Notazione: le slide scrivono $\mathcal{N}(\mu,\sigma)$ con la **deviazione standard** come secondo parametro. Molti testi usano $\mathcal{N}(\mu,\sigma^2)$. Nel wiki seguo la notazione delle slide.

![[probabilita-p23-gaussiana.png]]

## Formule

> 📄 Fonte: [[Probabilità.pdf#page=24]], [[Probabilità.pdf#page=25]]

**Funzioni integrali** (argomento adimensionale):
$$
\text{erf}(x) \triangleq \frac{2}{\sqrt\pi}\int_0^x e^{-t^2}dt, \qquad
\text{erfc}(x) \triangleq \frac{2}{\sqrt\pi}\int_x^{+\infty} e^{-t^2}dt = 1-\text{erf}(x)
$$
$$
Q(x) \triangleq \frac{1}{\sqrt{2\pi}}\int_x^{+\infty}e^{-t^2/2}dt \equiv \frac12\,\text{erfc}\!\left(\frac{x}{\sqrt2}\right)
$$

> 🧮 Formula chiave — CDF gaussiana ([[Probabilità.pdf#page=24]]):
> $$F(x) = \frac12\left[1+\text{erf}\left(\frac{x-\mu}{\sqrt2\,\sigma}\right)\right] = 1 - \frac12\,\text{erfc}\left(\frac{x-\mu}{\sqrt2\,\sigma}\right)$$

**Probabilità notevoli** ([[Probabilità.pdf#page=25]]), con $x \ge 0$ nelle ultime due:

| Evento | Espressione |
|---|---|
| $P(X<x)$ | $\frac12\left[1+\text{erf}\frac{x-\mu}{\sqrt2\sigma}\right] = \frac12\,\text{erfc}\frac{\mu-x}{\sqrt2\sigma}$ |
| $P(X>x)$ | $\frac12\,\text{erfc}\frac{x-\mu}{\sqrt2\sigma}$ |
| $P(\|X\|<x)$ | $\frac12\left[\text{erf}\frac{x-\mu}{\sqrt2\sigma} + \text{erf}\frac{x+\mu}{\sqrt2\sigma}\right]$ |
| $P(\|X\|>x)$ | $\frac12\left[\text{erfc}\frac{x-\mu}{\sqrt2\sigma} + \text{erfc}\frac{x+\mu}{\sqrt2\sigma}\right]$ |

> 🧮 Formula chiave (🧩 mia, conseguenza diretta): $P(X>x) = Q\!\left(\frac{x-\mu}{\sigma}\right)$.

## Derivazioni

### Derivazione — Normalizzazione della pdf
**Fonte:** [[Probabilità.pdf#page=23]] (suggerisce l'integrale notevole $\int_{-\infty}^{+\infty}e^{-x^2}dx = \sqrt\pi$)
$$
\begin{aligned}
\int_{-\infty}^{+\infty} \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx
&= \frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{+\infty} e^{-t^2}\sqrt2\,\sigma\,dt && t = \tfrac{x-\mu}{\sqrt2\sigma},\ dx = \sqrt2\sigma\,dt \\
&= \frac{1}{\sqrt\pi}\int_{-\infty}^{+\infty}e^{-t^2}dt && \text{semplifico } \sqrt2\sigma \\
&= \frac{1}{\sqrt\pi}\sqrt\pi = 1 && \text{integrale notevole}
\end{aligned}
$$

### Derivazione — CDF in termini di erf
**Fonte:** [[Probabilità.pdf#page=24]] (risultato dato)
$$
\begin{aligned}
F(x) &= \frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^x e^{-(t-\mu)^2/(2\sigma^2)}dt && \text{def. CDF} \\
&= \frac{1}{\sqrt\pi}\int_{-\infty}^{z} e^{-u^2}du, \quad z \triangleq \tfrac{x-\mu}{\sqrt2\sigma} && u = \tfrac{t-\mu}{\sqrt2\sigma} \\
&= \frac{1}{\sqrt\pi}\left[\int_{-\infty}^0 e^{-u^2}du + \int_0^z e^{-u^2}du\right] && \text{spezzo in } 0 \\
&= \frac{1}{\sqrt\pi}\left[\frac{\sqrt\pi}{2} + \frac{\sqrt\pi}{2}\text{erf}(z)\right] && \text{metà dell'integrale notevole; def. erf} \\
&= \frac12[1+\text{erf}(z)] = 1 - \frac12\text{erfc}(z) && \text{erf} = 1-\text{erfc}
\end{aligned}
$$
La formula vale anche per $z<0$: in quel caso $\int_0^z = -\int_z^0$ e $\text{erf}(z)<0$.

### Derivazione — Le quattro probabilità notevoli
**Fonte:** [[Probabilità.pdf#page=25]] («si dimostra facilmente»)
> 🧩 Derivazione mia. Uso due proprietà: $\text{erf}$ è **dispari** ($\text{erf}(-z) = -\text{erf}(z)$, perché l'integrando è pari), e quindi $1+\text{erf}(z) = 1-\text{erf}(-z) = \text{erfc}(-z)$.

$$
\begin{aligned}
P(X<x) &= F(x) = \tfrac12[1+\text{erf}(z)] = \tfrac12\text{erfc}(-z) = \tfrac12\text{erfc}\tfrac{\mu-x}{\sqrt2\sigma} && \text{v.a. continua: } P(X=x)=0 \\
P(X>x) &= 1-F(x) = \tfrac12\text{erfc}(z) && \text{prop. 3 CDF} \\
P(|X|<x) &= F(x) - F(-x) && x\ge0 \\
&= \tfrac12\left[\text{erf}\tfrac{x-\mu}{\sqrt2\sigma} - \text{erf}\tfrac{-x-\mu}{\sqrt2\sigma}\right] && \text{sostituisco la CDF} \\
&= \tfrac12\left[\text{erf}\tfrac{x-\mu}{\sqrt2\sigma} + \text{erf}\tfrac{x+\mu}{\sqrt2\sigma}\right] && \text{erf dispari} \\
P(|X|>x) &= 1 - P(|X|<x) = \tfrac12\left[(1-\text{erf}\tfrac{x-\mu}{\sqrt2\sigma}) + (1-\text{erf}\tfrac{x+\mu}{\sqrt2\sigma})\right] && 1 = \tfrac12+\tfrac12 \\
&= \tfrac12\left[\text{erfc}\tfrac{x-\mu}{\sqrt2\sigma} + \text{erfc}\tfrac{x+\mu}{\sqrt2\sigma}\right]
\end{aligned}
$$
**Sanity check:** con $\mu=0$, $P(|X|>x) = \text{erfc}(x/(\sqrt2\sigma)) = 2Q(x/\sigma)$, due code uguali per simmetria.

### Derivazione — $Q(x) = \frac12\text{erfc}(x/\sqrt2)$
**Fonte:** [[Probabilità.pdf#page=25]] (identità data)
$$
\begin{aligned}
Q(x) &= \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt && \text{def.} \\
&= \frac{1}{\sqrt{2\pi}}\int_{x/\sqrt2}^{\infty}e^{-u^2}\sqrt2\,du && t = \sqrt2 u \\
&= \frac12\cdot\frac{2}{\sqrt\pi}\int_{x/\sqrt2}^\infty e^{-u^2}du = \frac12\text{erfc}\left(\frac{x}{\sqrt2}\right) && \text{def. erfc}
\end{aligned}
$$
Quindi $P(X>x) = \frac12\text{erfc}\frac{x-\mu}{\sqrt2\sigma} = Q\left(\frac{x-\mu}{\sigma}\right)$: $Q$ è la coda della gaussiana **standard** $\mathcal{N}(0,1)$.

### Derivazione — $E(X)=\mu$ e $\text{Var}(X)=\sigma^2$
**Fonte:** [[Probabilità.pdf#page=28]], [[Probabilità.pdf#page=29]] («si prova che»)
> 🧩 Derivazione mia
$$
\begin{aligned}
E(X) &= \int x f(x)dx = \mu\underbrace{\int f(x)dx}_{=1} + \underbrace{\int (x-\mu) f(x)dx}_{=0} && x = \mu + (x-\mu);\ \text{integrando dispari intorno a } \mu \\
&= \mu \\
\text{Var}(X) &= \int (x-\mu)^2 f(x)dx = \frac{\sigma^2}{\sqrt{2\pi}}\int_{-\infty}^{\infty} t^2 e^{-t^2/2}dt && t=(x-\mu)/\sigma \\
&= \frac{\sigma^2}{\sqrt{2\pi}}\left( \left[-t e^{-t^2/2}\right]_{-\infty}^{\infty} + \int e^{-t^2/2}dt \right) && \text{per parti: } t\cdot t e^{-t^2/2} \\
&= \frac{\sigma^2}{\sqrt{2\pi}}(0 + \sqrt{2\pi}) = \sigma^2 && \int e^{-t^2/2}dt=\sqrt{2\pi}
\end{aligned}
$$

## Spiegazione

- La CDF **non ha forma chiusa** ([[Probabilità.pdf#page=24]]): per questo si introducono funzioni tabulate/numeriche.
- In **Matlab** ([[Probabilità.pdf#page=26]]): `erf`, `erfc`, `qfunc`. Codice per la CDF di $\mathcal{N}(0,1)$:
  ```matlab
  x = -3:0.1:3;
  y = (1/2)*(1+erf(x/sqrt(2)));
  plot(x,y)
  grid on
  title('CDF of normal distribution with µ = 0 and σ = 1')
  xlabel('x')
  ylabel('CDF')
  ```
  Qui $\mu=0$, $\sigma=1$, quindi $z = x/\sqrt2$.
- Una **trasformazione affine** di una gaussiana è ancora gaussiana ([[Probabilità.pdf#page=27]]) → [[funzione-di-variabile-aleatoria]].

> 🎯 Esame: saper passare da erf/erfc/Q in entrambi i sensi e scrivere $P(X>x)$, $P(|X|>x)$ per una gaussiana non standard. Nel corso la probabilità d'errore dei sistemi digitali si scriverà con $Q(\cdot)$.

**Valori di riferimento** — 📚 Fonte esterna (tabelle standard della Q, non nelle slide): $Q(1)\approx 0.159$, $Q(2)\approx 0.0228$, $Q(3)\approx 1.35\cdot10^{-3}$, $Q(4)\approx 3.17\cdot10^{-5}$.

> 💡 Connessione: con il *four-sigma loading* ([[quantizzazione-uniforme]]), se il segnale fosse gaussiano la probabilità di sovraccarico sarebbe $P(|X|>4\sigma) = 2Q(4) \approx 6.3\cdot10^{-5}$ (🧩 mio). È molto meno del limite di Chebyshev (6.25%), che vale per qualunque pdf ed è quindi pessimistico.

## Perché importa

Il rumore termico è somma di moltissimi contributi indipendenti (moto degli elettroni, [[Intro.pdf#page=18]]), quindi per il CLT è gaussiano. La funzione $Q$ sarà lo strumento standard per le probabilità d'errore.

## Connessioni

- [[variabile-aleatoria]] — definizione di CDF/pdf.
- [[media-e-varianza]] — interpretazione di $\mu$ e $\sigma$.
- [[funzione-di-variabile-aleatoria]] — $aX+b$ resta gaussiana.
- [[disuguaglianza-di-chebyshev]] — limite generico contro calcolo esatto con la Q.
- [[processo-gaussiano]] — la versione a $n$ variabili (gaussiana multivariata); per $n = 1$ si ritrova questa pdf.

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=23]] – [[Probabilità.pdf#page=26]]

_Aggiornato: 2026-09-28 — collegamento al processo gaussiano; 2026-09-23 — creazione da ingest Probabilità.pdf_
