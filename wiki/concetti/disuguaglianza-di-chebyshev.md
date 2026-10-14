---
tipo: concetto
importanza_esame: media
prerequisiti: ["media-e-varianza"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=29"]
---

# Disuguaglianza di Chebyshev

## Definizione · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

> 📚 Fonte esterna: enunciato standard di qualunque testo di probabilità (es. Papoulis, *Probability, Random Variables and Stochastic Processes*, cap. 5).

Per ogni v.a. $X$ con media $\mu$ e deviazione standard $\sigma$ finite, e per ogni $k>0$:
$$P(|X-\mu|\ge k\sigma) \le \frac{1}{k^2}$$
Il limite vale **per qualunque pdf**: non richiede ipotesi sulla distribuzione oltre all'esistenza della varianza.

## Formule · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

Applicazione del corso: $x(n)$ è assimilato a una v.a. a media nulla con $\sigma = x_{rms}$; $X_{max}$ è la soglia di sovraccarico; $k_c = X_{max}/x_{rms}$ è il fattore di carico:
$$P_s = P(|x(n)|>X_{max}) \le \frac{1}{k_c^2}$$

## Derivazioni

### Derivazione — Disuguaglianza di Chebyshev · [[Probabilità.pdf#page=28|p. 28]]
> 🧩 Derivazione mia (dimostrazione standard tramite il teorema fondamentale della media)
$$
\begin{aligned}
\sigma^2 &= \int_{-\infty}^{+\infty}(x-\mu)^2f(x)\,dx && \text{def. varianza} \\
&\ge \int_{|x-\mu|\ge k\sigma}(x-\mu)^2f(x)\,dx && \text{tolgo un integrando} \ge 0 \\
&\ge \int_{|x-\mu|\ge k\sigma}k^2\sigma^2f(x)\,dx && \text{lì } (x-\mu)^2\ge k^2\sigma^2 \\
&= k^2\sigma^2\,P(|X-\mu|\ge k\sigma) && \text{prop. 6 della pdf} \\
\Rightarrow P(|X-\mu|\ge k\sigma) &\le \frac{1}{k^2} && \text{divido per } k^2\sigma^2>0
\end{aligned}
$$

### Derivazione — Probabilità di sovraccarico · [[Campionamento_AD_DA.pdf#page=29|p. 29]]
$$
\begin{aligned}
\mu &= 0,\ \sigma = x_{rms} && \text{ipotesi della slide} \\
k\sigma = X_{max} &\Rightarrow k = X_{max}/x_{rms} = k_c && \text{def. fattore di carico} \\
P(|x(n)|>X_{max}) &\le P(|x(n)|\ge X_{max}) \le \frac{1}{k_c^2} && \{>\} \subseteq \{\ge\};\ \text{Chebyshev}
\end{aligned}
$$
**Numeri:** $k_c=4$ (*four-sigma loading*) → $P_s\le 1/16 = 0.0625 = 6.25\%$.
**Sanity check:** per un segnale gaussiano la probabilità vera sarebbe $2Q(4)\approx6.3\cdot10^{-5}$ ([[variabile-aleatoria-gaussiana]]), molto sotto il limite. Chebyshev è quindi un maggiorante **conservativo**.
**Ipotesi:** media nulla; varianza finita; il segnale campionato è trattato come una v.a. (quindi statistiche costanti nel tempo).

### Derivazione — Probabilità esatta di sovraccarico per Laplace · [[Campionamento_AD_DA.pdf#page=32|p. 32]]
> 🧩 Derivazione mia (serve al confronto nel grafico; pdf di Laplace da p. 32)
$$
\begin{aligned}
P(|X|>a) &= 2\int_a^\infty\tfrac\lambda2e^{-\lambda x}dx = e^{-\lambda a} && \text{pdf pari} \\
x_{rms} &= \sqrt2/\lambda \Rightarrow \lambda = \sqrt2/x_{rms} && [[variabili-aleatorie-notevoli]] \\
a = X_{max} = k_cx_{rms} &\Rightarrow P_s = e^{-\sqrt2\,k_c} && \text{sostituisco}
\end{aligned}
$$
**Numeri:** $k_c = 4$ → $P_s = e^{-5.657} \approx 3.5\cdot10^{-3}$ (0.35%), contro il limite di 6.25%.

## Spiegazione

La disuguaglianza usa **solo** i primi due momenti, per questo è debole ma universale. Se si conosce la pdf (gaussiana, Laplace...) si calcola il valore esatto, molto più piccolo.

![[grafico-chebyshev-sovraccarico.png]]
*🧩 Grafico mio (scala logaritmica). Il limite di Chebyshev $1/k_c^2$ decresce solo come potenza. Le probabilità vere decrescono esponenzialmente: Laplace come $e^{-\sqrt2k_c}$, gaussiana ancora più in fretta, come $2Q(k_c)$. Al four-sigma loading il limite vale 6.25%, mentre per una voce di Laplace il valore esatto è circa 0.35%. La Laplace ha code più pesanti della gaussiana, quindi per la voce il sovraccarico è più probabile che per un segnale gaussiano con la stessa potenza.*

> 🎯 Esame: sapere da dove viene $P_s \le 1/k_c^2$ e perché con $k_c=4$ si ha $6.25\%$.

## Perché importa

È il criterio usato per scegliere $X_{max}$ di un quantizzatore: trade-off tra sovraccarico e rumore granulare ([[quantizzazione-uniforme]], [[snr-di-quantizzazione]]).

## Connessioni

- [[media-e-varianza]] — la dimostrazione è un'applicazione del teorema fondamentale della media.
- [[quantizzazione-uniforme]] — fattore di carico e probabilità di sovraccarico.
- [[variabile-aleatoria-gaussiana]] — confronto limite/valore esatto.

## Fonti · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf_
