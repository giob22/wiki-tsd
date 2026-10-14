---
tipo: entità
categoria: algoritmo
---

# Algoritmo di Lloyd-Max

## Cos'è · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=35|35]]

Procedura iterativa che progetta il quantizzatore **ottimo MMSE** per una pdf $f_X$ nota: cerca i livelli di decisione $x_1,\dots,x_{M-1}$ e i livelli di restituzione $q_1,\dots,q_M$ che minimizzano
$$\text{MSE} = \sum_{i=1}^M\int_{R_i}(q_i-x)^2f_X(x)\,dx$$
Il problema non ha soluzione in forma chiusa. L'algoritmo alterna le due condizioni necessarie (derivate in [[quantizzazione-non-uniforme]]):

1. **inizializza** i livelli di decisione (es. quelli uniformi);
2. **centroide**: con le regioni fissate, $q_i = E[x\,|\,x\in R_i]$;
3. **punto medio**: con i livelli fissati, $x_i = (q_i+q_{i+1})/2$;
4. ripeti 2–3 finché l'MSE si assesta su un valore sufficientemente piccolo.

> 🧩 Derivazione mia: ogni passo non aumenta l'MSE, perché ottimizza esattamente rispetto a un sottoinsieme di variabili con le altre fisse. L'MSE è limitato inferiormente da 0, quindi la successione converge. Può però convergere a un minimo **locale**: le condizioni sono solo necessarie.

## Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=32|p. 32]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

È il quantizzatore ottimo per sorgenti stazionarie a pdf nota (es. voce modellata con Laplace). Limiti: serve conoscere la pdf e le prestazioni dipendono dal livello del segnale. Per questo in telefonia si preferisce il [[companding]].

## Concetti correlati

- [[quantizzazione-non-uniforme]], [[media-e-varianza]] (media condizionale), [[companding]]
- [[stazionarieta]] — "sorgente stazionaria" (del primo ordine) vuol dire che la pdf dei campioni non cambia nel tempo

## Fonti · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

- [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-09-28 — collegamento alla stazionarietà; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf_
