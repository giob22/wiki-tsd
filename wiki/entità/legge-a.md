---
tipo: entità
categoria: algoritmo
---

# Legge A (A-law)

## Cos'è

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=42]]

Legge di compressione per il [[companding]], definita a tratti:
$$
F(x) = \begin{cases}
X_{max}\dfrac{A|x|/X_{max}}{1+\ln A}\,\text{sgn}(x) & 0\le|x|\le X_{max}/A \quad\text{(tratto lineare)}\\[2mm]
X_{max}\dfrac{1+\ln(A|x|/X_{max})}{1+\ln A}\,\text{sgn}(x) & X_{max}/A\le|x|\le X_{max}\quad\text{(tratto logaritmico)}
\end{cases}
$$
- $A$ (adimensionale) regola il grado di compressione; valore usato: $A = 87.6$;
- $A = 1$: $F(x) = x$, cioè quantizzazione uniforme;
- usata in Europa e nei collegamenti internazionali; approssimazione a 7 segmenti in [[g711]].

![[campionamento-p42-a-law.png]]

## Come si usa nel corso

Il tratto lineare vicino a zero risolve il problema $\ln0 = -\infty$ della legge logaritmica ideale. Prestazioni ([[Campionamento_AD_DA.pdf#page=43]]):
$$\text{SNR}_{dB}\approx6.02\,b+4.77-20\log_{10}(1+\ln A)\overset{A=87.6}{=}6.02\,b-9.99$$
Derivazione di $\alpha$ e verifiche (continuità in $X_{max}/A$, caso $A=1$) in [[companding]].

> 🧩 Derivazione mia: con $A=87.6$ la soglia lineare/logaritmica è a $X_{max}/87.6\approx0.0114\,X_{max}$, cioè circa $-38.9$ dB sotto il fondo scala ($20\log_{10}87.6 = 38.85$).

## Concetti correlati

- [[companding]], [[legge-mu]], [[g711]], [[snr-di-quantizzazione]]

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=42]], [[Campionamento_AD_DA.pdf#page=43]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf_
