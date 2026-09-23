# Overview — Trasmissione dei Segnali Digitali

Corso della LM in Ingegneria Informatica, Università di Napoli Federico II, a.a. 2026-27, docente Donatella Darsena ([[Intro.pdf#page=1]]). Testo: U. Madhow, *Fundamentals of Digital Communication*, Cambridge 2008. Esame: colloquio orale ([[Intro.pdf#page=2]]).

> ⚠️ Nome del corso: il wiki era stato inizializzato come "Trasmissione dei **Sistemi** Digitali". Le slide dicono "Trasmissione dei **segnali** digitali" ([[Intro.pdf#page=1]]). Nome corretto il 2026-09-23.

**Temi principali** (programma, [[Intro.pdf#page=3]]):
1. Rappresentazione complessa in banda base dei segnali
2. Processi aleatori
3. Modulazione digitale dei segnali
4. Stima dei parametri e sincronizzazione
5. Comunicazione digitale su canali selettivi in frequenza
6. Elementi di teoria dell'informazione e codifica di canale

Elenco lezioni → [[lezioni]]

## Argomenti coperti nel wiki

| Area | Pagine | Stato |
|---|---|---|
| Quadro generale del sistema digitale | [[sistema-comunicazione-digitale]], [[ripetitore-rigenerativo]] | qualitativo |
| Probabilità (prerequisito per i processi aleatori) | [[spazio-di-probabilita]], [[probabilita-condizionale]], [[probabilita-totale-e-bayes]], [[variabile-aleatoria]], [[variabili-aleatorie-notevoli]], [[variabile-aleatoria-gaussiana]], [[funzione-di-variabile-aleatoria]], [[media-e-varianza]], [[coppie-di-variabili-aleatorie]], [[correlazione-e-covarianza]], [[disuguaglianza-di-chebyshev]] | completo per la fonte |
| Conversione A/D e D/A (codifica di sorgente) | [[conversione-ad-da]], [[teorema-del-campionamento]], [[aliasing]], [[interpolazione]], [[quantizzazione-uniforme]], [[snr-di-quantizzazione]], [[quantizzazione-non-uniforme]], [[companding]] | completo per la fonte |

Filo logico finora: il sistema digitale ([[sistema-comunicazione-digitale]]) comincia con la conversione A/D della sorgente ([[conversione-ad-da]]), che ne fissa il bit rate $b\cdot f_c$ ([[dimensionamento-quantizzatore]]). La natura statistica del canale e del rumore richiede la teoria della probabilità, già usata nella quantizzazione ([[disuguaglianza-di-chebyshev]], $\Delta^2/12$).

## Argomenti mancanti / da ingerire

Nessuno dei sei temi principali ha ancora una fonte dedicata:
- rappresentazione complessa in banda base — TODO
- processi aleatori (base probabilistica pronta) — TODO
- modulazione digitale — TODO
- stima dei parametri e sincronizzazione — TODO
- canali selettivi in frequenza / equalizzazione — TODO
- teoria dell'informazione e codifica di canale — TODO
- rumore termico: solo qualitativo ([[Intro.pdf#page=18]]) — TODO

## Fonti ingerite

3 — [[intro-corso]], [[elementi-teoria-probabilita]], [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-09-23 — primo ingest (3 fonti)_
