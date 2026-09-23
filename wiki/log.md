# Log — Trasmissione dei Segnali Digitali

Formato entry: `## [YYYY-MM-DD] <operazione> | <dettaglio>`
Filtra ultimi 10: `grep "^## " wiki/log.md | tail -10`

---

## [2026-09-23] setup | Wiki tsd inizializzato (struttura vuota, nessuna fonte)

## [2026-09-23] ingest | Introduzione al corso (Intro.pdf) | pagine coperte: 1-21
- fonte: [[intro-corso]]; concetti: [[sistema-comunicazione-digitale]]; entità: [[ripetitore-rigenerativo]]
- 3 figure in raw/assets/

## [2026-09-23] ingest | Elementi di Teoria della Probabilità (Probabilità.pdf) | pagine coperte: 1-38
- fonte: [[elementi-teoria-probabilita]]; 10 concetti; esercizi: [[calcolo-probabilita-eventi]], [[cdf-pdf-variabili-notevoli]]
- refusi segnalati: p.13-14 ($A_j\cap A_j$), p.27 ($\le x$); Es. 2.3 e 2.6 senza evento specificato (❓)

## [2026-09-23] ingest | Campionamento e conversione A/D e D/A (Campionamento_AD_DA.pdf) | pagine coperte: 1-43
- fonte: [[campionamento-conversione-ad-da]]; 9 concetti (incl. [[disuguaglianza-di-chebyshev]]); entità: [[g711]], [[legge-mu]], [[legge-a]], [[algoritmo-lloyd-max]]
- esercizi: [[campionamento-e-aliasing]], [[dimensionamento-quantizzatore]]; derivati 6 dB/bit, α µ/A-law, Lloyd-Max
- refuso: p.24 "First-Order Hold (ZOH)"

## [2026-09-23] setup | nome corso corretto in "Trasmissione dei Segnali Digitali"; temi principali compilati in CLAUDE.md; creato [[lezioni]] (3 lezioni, 1 PDF ciascuna)

## [2026-09-23] revisione | Campionamento_AD_DA.pdf | copertura totale pp. 1-43 (testo + figure)
- aggiunti contenuti mancanti: p.2 (trasformazione inversa, circuito d'esempio), p.3 (catena A/D-DSP-D/A), p.4 (dettagli vantaggi), p.7-11 e p.14-15 (figure + unità, sistema campionatore, problema fondamentale), p.12 (replicazione non univoca), p.17 (sinc a banda limitata + figura), p.19 (due ipotesi ideali), p.20-21 (pannelli figure, schema antialiasing), p.23-25 e p.27-28 (figure, esempio livelli), p.30 e p.34-36 (testo completo, schema compander), p.38 e p.40-43 (figure e conclusione legge logaritmica)
- rimossi: dati esterni G.711 (8 kHz/8 bit), esercizi inventati (voce PCM, scelta f_r), anticipazioni (modulazione, decisione a minima distanza), terminologia "mid-rise"
- nuovo refuso segnalato: p.36 figura "decoder" → encoder
- regola di copertura totale aggiunta a CLAUDE.md (INGEST passo 11)

## [2026-09-23] grafici | Campionamento_AD_DA.pdf | 8 grafici di funzione in output/grafici/
- inseriti in [[quantizzazione-non-uniforme]] (Laplace ×2, Lloyd-Max), [[variabili-aleatorie-notevoli]], [[snr-di-quantizzazione]] (SNR vs b, errore), [[disuguaglianza-di-chebyshev]] (+ derivazione P_s Laplace), [[interpolazione]] (|H_r|), [[companding]] (SNR vs livello µ/A/uniforme + derivazione)
- verifiche: µ 38.0 dB, A 38.2 dB, uniforme k_c=4 40.9 dB coincidono con p.43
