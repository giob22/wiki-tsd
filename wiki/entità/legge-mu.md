---
tipo: entità
categoria: algoritmo
---

# Legge µ (µ-law)

## Cos'è

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=41]]

Legge di compressione per il [[companding]]:
$$F(x) = X_{max}\frac{\ln(1+\mu|x|/X_{max})}{\ln(1+\mu)}\,\text{sgn}(x),\qquad |x|\le X_{max}$$
- $\mu$ (adimensionale) regola il grado di compressione; valore usato: $\mu = 255$;
- $\mu = 0$: $F(x) = x$, cioè quantizzazione uniforme;
- usata in Stati Uniti, Canada e Giappone; approssimazione a 7 segmenti in [[g711]].

![[campionamento-p41-mu-law.png]]

## Come si usa nel corso

È un'approssimazione della legge logaritmica ideale che vale $0$ in $x=0$: il termine "$1+$" evita $\ln0 = -\infty$. Prestazioni ([[Campionamento_AD_DA.pdf#page=43]]):
$$\text{SNR}_{dB}\approx6.02\,b+4.77-20\log_{10}\ln(1+\mu)\overset{\mu=255}{=}6.02\,b-10.11$$
La derivazione di $\alpha$, i controlli ($F(X_{max}) = X_{max}$, limite $\mu\to0$) e l'approssimazione usata ($\mu|x|/X_{max}\gg1$) sono in [[companding]].

## Concetti correlati

- [[companding]], [[legge-a]], [[g711]], [[snr-di-quantizzazione]]

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=41]], [[Campionamento_AD_DA.pdf#page=43]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf_
