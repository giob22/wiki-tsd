# Overview — Trasmissione dei Segnali Digitali · [[Intro.pdf#page=1|p. 1]]–[[Intro.pdf#page=3|3]]

Corso della LM in Ingegneria Informatica, Università di Napoli Federico II, a.a. 2026-27, docente Donatella Darsena. Testo: U. Madhow, *Fundamentals of Digital Communication*, Cambridge 2008. Esame: colloquio orale.

> ⚠️ Nome del corso: il wiki era stato inizializzato come "Trasmissione dei **Sistemi** Digitali". Le slide dicono "Trasmissione dei **segnali** digitali". Nome corretto il 2026-09-23.

**Temi principali** (programma):
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
| **Tema 1** — Rappresentazione complessa in banda base | [[modulazione-digitale]], [[segnali-banda-base-e-passa-banda]], [[segnale-analitico]], [[inviluppo-complesso]], [[upconversion-e-downconversion]], [[equivalente-banda-base-dei-filtri]] | completo per la fonte |
| **Tema 2** — Processi aleatori | [[processo-aleatorio]], [[momenti-di-un-processo]], [[stazionarieta]], [[autocorrelazione-processi-wss]], [[processi-e-sistemi-lti]], [[densita-spettrale-di-potenza]], [[processo-gaussiano]] | completo per la fonte |

Filo logico finora:
- Il sistema digitale ([[sistema-comunicazione-digitale]]) comincia con la conversione A/D della sorgente ([[conversione-ad-da]]), che ne fissa il bit rate $b\cdot f_c$ ([[dimensionamento-quantizzatore]]).
- La natura statistica del canale e del rumore richiede la teoria della probabilità, già usata nella quantizzazione ([[disuguaglianza-di-chebyshev]], $\Delta^2/12$).
- I bit vanno poi trasmessi su canali passa-banda. La rappresentazione complessa in banda base ([[inviluppo-complesso]]) permette di descrivere segnali e canali passa-banda con segnali in banda base, quindi di fare modulazione e demodulazione in digitale. Il passaggio alla portante resta ai soli upconverter e downconverter ([[upconversion-e-downconversion]]).
- Rumore e segnali d'informazione non sono prevedibili: si modellano come processi aleatori ([[processo-aleatorio]]). Media, autocorrelazione e densità spettrale di potenza ([[densita-spettrale-di-potenza]]) dicono quanta potenza c'è e a quali frequenze, e come cambia attraverso i filtri ([[processi-e-sistemi-lti]]). Il processo gaussiano ([[processo-gaussiano]]) è il modello di riferimento per il rumore.

## Argomenti mancanti / da ingerire · [[Intro.pdf#page=18|p. 18]]

Temi principali ancora senza fonte (il tema 1 è coperto da [[rappresentazione-complessa-banda-base]], il tema 2 da [[processi-aleatori]]):
- modulazione digitale — TODO
- stima dei parametri e sincronizzazione — TODO
- canali selettivi in frequenza / equalizzazione — TODO
- teoria dell'informazione e codifica di canale — TODO
- rumore termico: solo qualitativo — TODO

## Fonti ingerite

6 — [[intro-corso]], [[elementi-teoria-probabilita]], [[campionamento-conversione-ad-da]], [[rappresentazione-complessa-banda-base]], [[processi-aleatori]], [[laboratorio-conversione-ad]] (laboratorio Matlab, non d'esame: macroblocchi in `laboratorio/`)

_Aggiornato: 2026-09-30 — ingest del laboratorio Matlab sulla conversione A/D (non d'esame); 2026-09-28 — re-ingest di Rappresentazione_Rice.pdf e random_processes.pdf nella versione con appunti a mano (dimostrazioni della docente integrate come fonte); ingest random_processes.pdf (tema 2); 2026-09-25 — ingest Rappresentazione_Rice.pdf (tema 1); 2026-09-23 — primo ingest (3 fonti)_
