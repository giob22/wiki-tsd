---
tipo: entità
categoria: algoritmo
---

# Legge µ (µ-law)

## Cos'è · [[Campionamento_AD_DA.pdf#page=41|p. 41]]

Legge di compressione per il [[companding]]:
$$F(x) = X_{max}\frac{\ln(1+\mu|x|/X_{max})}{\ln(1+\mu)}\,\text{sgn}(x),\qquad |x|\le X_{max}$$
- $\mu$ (adimensionale) regola il grado di compressione; valore usato: $\mu = 255$;
- $\mu = 0$: $F(x) = x$, cioè quantizzazione uniforme;
- usata in Stati Uniti, Canada e Giappone; approssimazione a 7 segmenti in [[g711]].

![[campionamento-p41-mu-law.png]]

## Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=43|p. 43]]

È un'approssimazione della legge logaritmica ideale che vale $0$ in $x=0$: il termine "$1+$" evita $\ln0 = -\infty$. Prestazioni:
$$\text{SNR}_{dB}\approx6.02\,b+4.77-20\log_{10}\ln(1+\mu)\overset{\mu=255}{=}6.02\,b-10.11$$
La derivazione di $\alpha$, i controlli ($F(X_{max}) = X_{max}$, limite $\mu\to0$) e l'approssimazione usata ($\mu|x|/X_{max}\gg1$) sono in [[companding]].

Come ogni legge di compressione, trasforma il quantizzatore uniforme in un quantizzatore non uniforme sull'asse $x$ ([[companding]] (sezione «Idea chiave del companding»)). Le soglie equivalenti sono $x_j = \frac{X_{max}}{\mu}\big[(1+\mu)^{2j/M}-1\big]$. Con $\mu = 255$ e $M = 8$ valgono $0.0118$, $0.0588$, $0.247$ e $1$ (in unità di $X_{max}$): ogni intervallo è 4 volte più largo del precedente (🧩 derivazione in [[companding]] (sezione «Derivazione — Esempio µ-law, soglie e livelli equivalenti»)).

## Concetti correlati

- [[companding]], [[legge-a]], [[g711]], [[snr-di-quantizzazione]]

## Fonti · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-09-24 — soglie equivalenti sull'asse $x$ e link all'idea chiave del companding; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf_
