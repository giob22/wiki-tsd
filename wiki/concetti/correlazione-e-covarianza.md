---
tipo: concetto
importanza_esame: alta
prerequisiti: ["coppie-di-variabili-aleatorie", "media-e-varianza"]
fonti_pdf: ["Probabilità.pdf#page=36", "Probabilità.pdf#page=37", "Probabilità.pdf#page=38"]
---

# Correlazione, covarianza e coefficiente di correlazione

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=37]]

Per una coppia $(X,Y)$ con pdf congiunta $f_{XY}$, medie $\mu_X,\mu_Y$ e deviazioni standard $\sigma_X,\sigma_Y$:

| Grandezza | Definizione |
|---|---|
| **Correlazione** | $\text{Corr}(X,Y) \triangleq E(XY) = \iint xy\,f_{XY}(x,y)\,dx\,dy$ |
| **Covarianza** | $\text{Cov}(X,Y) \triangleq E[(X-\mu_X)(Y-\mu_Y)]$ |
| **Coefficiente di correlazione** | $\rho_{XY} \triangleq \dfrac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y}$ (adimensionale) |

Correlazione e covarianza possono avere segno qualsiasi. Casi particolari: $\text{Corr}(X,X) = E(X^2)$ e $\text{Cov}(X,X) = \text{Var}(X)$.

Terminologia usata in [[Probabilità.pdf#page=38]]:
- $X,Y$ **ortogonali** se $E(XY) = 0$;
- $X,Y$ **incorrelate** se $\text{Cov}(X,Y) = 0$.

## Formule

**Teorema fondamentale della media per coppie** ([[Probabilità.pdf#page=36]]): $E[g(X,Y)] = \iint g(x,y)f_{XY}(x,y)\,dx\,dy$ (per il caso discreto: $\sum_{i,j}g(x_i,y_j)p_{XY}(x_i,y_j)$). La media è lineare: $E(a_1X+a_2Y) = a_1E(X)+a_2E(Y)$.

**Proprietà** ([[Probabilità.pdf#page=38]]):
1. $\text{Cov}(X,Y) = E(XY) - E(X)E(Y)$ — relazione fondamentale
2. $E[(X+Y)^2] = E(X^2)+E(Y^2)+2E(XY)$; se $X,Y$ sono ortogonali, $E[(X+Y)^2] = E(X^2)+E(Y^2)$
3. $\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y)+2\,\text{Cov}(X,Y)$; se sono incorrelate, le varianze si sommano.
   In generale: $\text{Var}\left(\sum_i c_iX_i\right) = \sum_i c_i^2\text{Var}(X_i) + \sum_i\sum_{j\neq i}c_ic_j\text{Cov}(X_i,X_j)$
4. $|E(XY)| \le \sqrt{E(X^2)}\sqrt{E(Y^2)}$ — Schwarz; uguaglianza se e solo se $Y = a^*X$ in media quadratica
5. $|\text{Cov}(X,Y)| \le \sigma_X\sigma_Y$ — Schwarz; uguaglianza se e solo se $Y = a^*X+b^*$ in media quadratica
6. $|\rho_{XY}|\le 1$

> 🧮 Formula chiave: proprietà 1 e 3.

## Derivazioni

> 🧩 Derivazione mia: le slide enunciano le proprietà senza passaggi.

### Derivazione — Proprietà 1
$$
\begin{aligned}
\text{Cov}(X,Y) &= E[XY - \mu_YX - \mu_XY + \mu_X\mu_Y] && \text{sviluppo il prodotto} \\
&= E(XY) - \mu_Y\mu_X - \mu_X\mu_Y + \mu_X\mu_Y && \text{linearità} \\
&= E(XY) - E(X)E(Y)
\end{aligned}
$$

### Derivazione — Proprietà 2 e 3
$$
\begin{aligned}
E[(X+Y)^2] &= E[X^2+2XY+Y^2] = E(X^2)+E(Y^2)+2E(XY) && \text{linearità} \\
\text{Var}(X+Y) &= E\big[\big((X-\mu_X)+(Y-\mu_Y)\big)^2\big] && \mu_{X+Y} = \mu_X+\mu_Y \\
&= \text{Var}(X)+\text{Var}(Y)+2\text{Cov}(X,Y) && \text{prop. 2 sulle v.a. centrate}
\end{aligned}
$$
Caso generale: $\text{Var}(\sum_ic_iX_i) = E[(\sum_ic_i(X_i-\mu_i))^2] = \sum_i\sum_jc_ic_j\text{Cov}(X_i,X_j)$. Separando i termini $i=j$, dove $\text{Cov}(X_i,X_i) = \text{Var}(X_i)$, si ottiene la formula della slide.

### Derivazione — Disuguaglianza di Schwarz (prop. 4)
$$
\begin{aligned}
0 &\le E[(Y-aX)^2] \quad \forall a\in\mathbb{R} && \text{media di una quantità} \ge 0 \\
&= E(Y^2) - 2a\,E(XY) + a^2E(X^2) && \text{polinomio di 2° grado in } a \\
\Rightarrow \Delta &= 4E^2(XY) - 4E(X^2)E(Y^2) \le 0 && \text{mai negativo} \Rightarrow \text{discriminante} \le 0 \\
\Rightarrow |E(XY)| &\le \sqrt{E(X^2)E(Y^2)}
\end{aligned}
$$
L'uguaglianza vale se e solo se $\Delta = 0$, cioè esiste $a^*$ con $E[(Y-a^*X)^2] = 0$: $Y = a^*X$ in media quadratica.
**Prop. 5:** applico la 4 alle v.a. centrate $X-\mu_X$ e $Y-\mu_Y$. **Prop. 6:** divido la 5 per $\sigma_X\sigma_Y$.

### Derivazione — Indipendenti ⇒ incorrelate
> 🧩 Derivazione mia (non esplicitata nelle slide, ma segue da [[Probabilità.pdf#page=35]] e [[Probabilità.pdf#page=36]])
$$
E(XY) = \iint xy\,f_X(x)f_Y(y)\,dx\,dy = \int xf_X\,dx\int yf_Y\,dy = E(X)E(Y) \Rightarrow \text{Cov} = 0
$$
Il **viceversa è falso** in generale. Controesempio (🧩 mio): $X\sim\mathcal{U}(-1,1)$ e $Y=X^2$ sono incorrelate, perché $E(XY) = E(X^3) = 0 = E(X)E(Y)$, ma $Y$ è funzione deterministica di $X$.

## Spiegazione

- **Ortogonale ≠ incorrelato**: i due concetti coincidono se almeno una delle v.a. ha media nulla (per la prop. 1).
- $\rho_{XY}$ misura la **dipendenza lineare**: $|\rho|=1$ se e solo se $Y$ è una funzione affine di $X$ in media quadratica (prop. 5); $\rho=0$ significa nessuna dipendenza *lineare*, ma può esserci dipendenza non lineare.
- La prop. 3 serve a sommare potenze di rumore: segnale e rumore incorrelati → le potenze si sommano.

> 🎯 Esame: indipendenza ⇒ incorrelazione ma non viceversa; ortogonalità vs incorrelazione; dimostrazione di Schwarz.

## Perché importa

L'ipotesi "errore di quantizzazione incorrelato col segnale" (modello additivo $x_q = x + e$, [[Campionamento_AD_DA.pdf#page=28]]) serve a dire che la potenza di $x_q$ è $P_x + P_e$. La funzione di autocorrelazione dei processi aleatori estende $\text{Corr}(X,Y)$ a due campioni dello stesso processo.

> 🧩 Derivazione mia: il collegamento con il modello del quantizzatore è una mia lettura. La slide 28 introduce il modello a sommatore senza parlare di correlazione.

## Connessioni

- [[media-e-varianza]] — per $X=Y$ le definizioni si riducono a valor quadratico medio e varianza.
- [[coppie-di-variabili-aleatorie]] — i momenti misti sono calcolati dalla pdf congiunta.
- [[variabili-aleatorie-notevoli]] — la varianza della binomiale ($npq$) usa la prop. 3 generalizzata.
- [[momenti-di-un-processo]] — autocorrelazione e autocovarianza di un processo sono correlazione e covarianza di due suoi campioni; incoerenza e incorrelazione tra processi ricalcano ortogonalità e incorrelazione tra v.a.
- [[autocorrelazione-processi-wss]] — la disuguaglianza di Schwarz dà $|R_{XX}(\tau)| \le R_{XX}(0)$.

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=36]] – [[Probabilità.pdf#page=38]]

_Aggiornato: 2026-09-28 — collegamenti ai processi aleatori; 2026-09-23 — creazione da ingest Probabilità.pdf_
