# Index — Trasmissione dei Segnali Digitali

## Overview
- [[overview]] — panoramica del corso, programma, copertura
- [[lezioni]] — elenco lezioni con gli argomenti in ordine di PDF

## Concetti

**Sistema di comunicazione**
- [[sistema-comunicazione-digitale]] — elementi, schema a blocchi, vantaggi del digitale, separazione (alta)

**Probabilità**
- [[spazio-di-probabilita]] — assiomi di Kolmogorov, proprietà elementari (media)
- [[probabilita-condizionale]] — condizionale, probabilità composta, catena, indipendenza (alta)
- [[probabilita-totale-e-bayes]] — probabilità totale, Bayes (alta)
- [[variabile-aleatoria]] — CDF, pdf, DF; v.a. discrete/continue/miste (alta)
- [[variabili-aleatorie-notevoli]] — Bernoulli, Binomiale, Uniforme, Laplace (alta)
- [[variabile-aleatoria-gaussiana]] — pdf gaussiana, erf, erfc, Q (alta)
- [[funzione-di-variabile-aleatoria]] — $f_Y = \sum f_X/|g'|$ (media)
- [[media-e-varianza]] — teorema fondamentale, momenti, varianza (alta)
- [[coppie-di-variabili-aleatorie]] — congiunte, marginali, condizionali (media)
- [[correlazione-e-covarianza]] — Corr, Cov, ρ, Schwarz (alta)
- [[disuguaglianza-di-chebyshev]] — limite sulle code; sovraccarico (media)

**Conversione A/D e D/A**
- [[conversione-ad-da]] — campionamento + quantizzazione; interpolazione (media)
- [[teorema-del-campionamento]] — Shannon, Nyquist, ricostruzione (alta)
- [[aliasing]] — frequenza alias, antialiasing (alta)
- [[interpolazione]] — serie di Shannon, ZOH, FOH (alta)
- [[quantizzazione-uniforme]] — Δ, M, regioni, fattore di carico (alta)
- [[snr-di-quantizzazione]] — legge dei 6 dB/bit (alta)
- [[quantizzazione-non-uniforme]] — Lloyd-Max: centroide e punto medio (alta)
- [[companding]] — legge logaritmica, µ/A-law, prestazioni (alta)

## Entità
- [[ripetitore-rigenerativo]] — dispositivo
- [[g711]] — standard ITU-T PCM voce
- [[legge-mu]] — algoritmo di compressione (µ = 255)
- [[legge-a]] — algoritmo di compressione (A = 87.6)
- [[algoritmo-lloyd-max]] — quantizzatore ottimo MMSE

## Fonti
- [[intro-corso]] — Intro.pdf, pp. 1–21
- [[elementi-teoria-probabilita]] — Probabilità.pdf, pp. 1–38
- [[campionamento-conversione-ad-da]] — Campionamento_AD_DA.pdf, pp. 1–43

## Esercizi
- [[calcolo-probabilita-eventi]] — eventi, condizionale, indipendenza (bassa)
- [[cdf-pdf-variabili-notevoli]] — CDF/pdf di v.a. notevoli e trasformate (media)
- [[campionamento-e-aliasing]] — Nyquist, alias, numero di campioni (bassa)
- [[dimensionamento-quantizzatore]] — bit, SNR, $k_c$, bit rate, companding (media)

## Esame
_nessun materiale ancora — lancia `prepara esame`_

## Asset
Figure in `raw/assets/`: 3 da Intro, 7 da Probabilità, 29 da Campionamento (nome `file-pN-descrizione.png`).
Grafici di funzione generati (🧩) in `output/grafici/` — script `genera_grafici_campionamento.py`: pdf di Laplace, Laplace/gauss/uniforme, Lloyd-Max M=8, SNR vs bit, errore di quantizzazione, Chebyshev vs esatto, $|H_r(f)|$ interpolatori, SNR vs livello (uniforme/µ/A).
