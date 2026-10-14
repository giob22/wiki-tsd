---
tipo: fonte
titolo: "Elementi di Teoria della Probabilità"
file_raw: "Probabilità.pdf"
pagine: "1-38"
data_ingest: 2026-09-23
formato: slide-pdf
argomenti: [spazio di probabilità, assiomi di Kolmogorov, probabilità condizionale, indipendenza, probabilità totale, Bayes, variabile aleatoria, CDF, pdf, v.a. notevoli, gaussiana, erf/erfc/Q, funzione di v.a., media, varianza, coppie di v.a., covarianza, Schwarz]
---

# Elementi di Teoria della Probabilità — Probabilità.pdf

## Sommario

Ripasso della teoria della probabilità, come base per i processi aleatori e le prestazioni dei sistemi digitali. Si parte dalle definizioni (esperimento, spazio campione, eventi) e dagli **assiomi di Kolmogorov**, da cui seguono le proprietà elementari. Poi vengono **probabilità condizionale**, legge della probabilità composta, regola della catena, **indipendenza** (anche per più eventi), **probabilità totale** e **Bayes** con la lettura cause/effetto. Nella seconda parte: **variabile aleatoria**, CDF/pdf/DF con le proprietà; v.a. notevoli (Bernoulli, Binomiale, Uniforme, **Gaussiana**) con le funzioni erf, erfc e $Q$ e i comandi Matlab; funzione di v.a.; **media**, momenti, **varianza**. Infine le **coppie di v.a.** (congiunte, marginali, condizionali, indipendenza) e la loro descrizione sintetica (correlazione, covarianza, coefficiente di correlazione, disuguaglianza di Schwarz). Molti risultati sono enunciati senza dimostrazione: nel wiki sono espansi e marcati 🧩.

## Punti chiave · [[Probabilità.pdf#page=5|p. 5]]–[[Probabilità.pdf#page=7|7]], [[Probabilità.pdf#page=9|p. 9]]–[[Probabilità.pdf#page=14|14]], [[Probabilità.pdf#page=16|p. 16]]–[[Probabilità.pdf#page=20|20]], [[Probabilità.pdf#page=23|p. 23]]–[[Probabilità.pdf#page=25|25]], [[Probabilità.pdf#page=27|p. 27]], [[Probabilità.pdf#page=28|28]], [[Probabilità.pdf#page=30|p. 30]], [[Probabilità.pdf#page=31|31]], [[Probabilità.pdf#page=35|p. 35]], [[Probabilità.pdf#page=37|p. 37]], [[Probabilità.pdf#page=38|38]]

1. Spazio di probabilità $(\Omega,\mathcal{S},P)$ e assiomi I–III; proprietà 1–7.
2. $P(A|B) = P(AB)/P(B)$; attrazione e repulsione tra eventi.
3. Probabilità composta e regola della catena, con $n!$ scritture.
4. Indipendenza: $P(AB) = P(A)P(B)$; per $n$ eventi serve la fattorizzazione su **ogni** sottoinsieme; indipendenti ≠ mutuamente esclusivi.
5. Probabilità totale e Bayes: probabilità a priori delle cause → a posteriori.
6. CDF: 6 proprietà; $P(X=x) = F(x)-F(x^-)$. V.a. discrete, continue, miste.
7. pdf come derivata (generalizzata) della CDF; DF solo per v.a. discrete.
8. Bernoulli, Binomiale, Uniforme, Gaussiana.
9. CDF gaussiana tramite erf/erfc; $Q(x) = \frac12\text{erfc}(x/\sqrt2)$.
10. $f_Y(y) = \sum_if_X(x_i)/|g'(x_i)|$; la trasformazione affine di una gaussiana è gaussiana.
11. Teorema fondamentale della media; $\text{Var} = E(X^2)-E^2(X)$; $\text{Var}(aX+b) = a^2\text{Var}(X)$.
12. Coppie: marginali dalla congiunta, pdf condizionali, indipendenza come fattorizzazione.
13. $\text{Cov} = E(XY)-E(X)E(Y)$; $\text{Var}(X+Y)$; Schwarz; $|\rho|\le1$.

## Concetti introdotti

- [[spazio-di-probabilita]]
- [[probabilita-condizionale]]
- [[probabilita-totale-e-bayes]]
- [[variabile-aleatoria]]
- [[variabili-aleatorie-notevoli]]
- [[variabile-aleatoria-gaussiana]]
- [[funzione-di-variabile-aleatoria]]
- [[media-e-varianza]]
- [[coppie-di-variabili-aleatorie]]
- [[correlazione-e-covarianza]]

Esercizi: [[calcolo-probabilita-eventi]], [[cdf-pdf-variabili-notevoli]].

## Refusi rilevati · [[Probabilità.pdf#page=13|p. 13]], [[Probabilità.pdf#page=14|14]], [[Probabilità.pdf#page=27|p. 27]]

> ⚠️ p. 13: "$A_j\cap A_j = \emptyset,\ i\neq j$" → corretto $A_i\cap A_j$.
> ⚠️ p. 27: "$F_Y(y) = P(\omega: g(X(\omega))\le x)$" → corretto $\le y$.

## Domande aperte · [[Probabilità.pdf#page=9|p. 9]], [[Probabilità.pdf#page=11|p. 11]], [[Probabilità.pdf#page=17|p. 17]], [[Probabilità.pdf#page=23|p. 23]]

- Esempio 2.3 ed Esempio 2.6: la slide non specifica l'evento da calcolare. Nel wiki ho svolto il caso più tipico, da verificare con gli appunti ❓.
- «Discussione del valore assunto da $P(X=x)$ nei tre casi»: svolta a lezione; ricostruita nel wiki dalla prop. 6 della CDF.
- La notazione $\mathcal{N}(\mu,\sigma)$ usa la deviazione standard: resterà così nelle slide successive?
- Il CLT è citato ma non enunciato.

## Domande da esame

- Enunciare gli assiomi di Kolmogorov e dimostrare $P(A\cup B) = P(A)+P(B)-P(AB)$.
- Differenza tra eventi indipendenti e mutuamente esclusivi.
- Teorema della probabilità totale e di Bayes: ipotesi e interpretazione.
- Proprietà della CDF; come si calcola $P(X=x)$ per v.a. continue, discrete, miste.
- Esprimere $P(X>x)$ e $P(|X|>x)$ per una gaussiana con erfc e con $Q$.
- pdf di $Y = aX+b$ con $X$ gaussiana.
- Dimostrare $\text{Var}(X) = E(X^2)-E^2(X)$ e $\text{Cov}(X,Y) = E(XY)-E(X)E(Y)$.
- Indipendenza ⇒ incorrelazione? E il viceversa?
- Disuguaglianza di Schwarz e $|\rho|\le1$.

_Aggiornato: 2026-09-23 — ingest iniziale_
