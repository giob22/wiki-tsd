# Overview — Trasmissione dei Segnali Digitali · [[Intro.pdf#page=1|p. 1]]–[[Intro.pdf#page=3|3]]

Corso della LM in Ingegneria Informatica, Università di Napoli Federico II, a.a. 2026-27, docente Donatella Darsena. Testo: U. Madhow, *Fundamentals of Digital Communication*, Cambridge 2008; a lezione la docente ha indicato come riferimento il libro di Biglieri (Benedetto-Biglieri, *Principles of Digital Transmission*). Esame: colloquio orale.

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
| **Tema 1 + 2** — Rappresentazione dei processi passa-banda | [[processi-passa-banda]], [[psd-componenti-in-quadratura]], [[rumore-in-banda-passante]] | completo per la fonte |
| **Tema 3** — Modulazione e rivelazione | [[principi-di-modulazione]], [[spazio-dei-segnali]], [[modulazione-lineare]], [[modulazione-ortogonale]], [[rivelazione-map-ml]], [[ricevitore-ottimo-awgn]], [[probabilita-errore-binaria]], [[probabilita-errore-m-aria]] | completo per le fonti |
| **Temi 3 + 6** — Parametri globali delle modulazioni e capacità | [[informazione-mutua-e-capacita]], [[parametri-globali-modulazioni]], [[limite-di-shannon]], [[link-budget]] | completo per la fonte |
| **Tema 5** — Canali selettivi in frequenza: ISI, equalizzazione, OFDM | [[interferenza-intersimbolica]], [[criterio-di-nyquist]], [[equalizzazione]], [[algoritmo-di-viterbi]], [[ofdm]], [[prefisso-ciclico]], [[ofdm-con-fft]], [[equalizzazione-ofdm]], [[limiti-dell-ofdm]] | completo per le fonti |

Filo logico finora:
- Il sistema digitale ([[sistema-comunicazione-digitale]]) comincia con la conversione A/D della sorgente ([[conversione-ad-da]]), che ne fissa il bit rate $b\cdot f_c$ ([[dimensionamento-quantizzatore]]).
- La natura statistica del canale e del rumore richiede la teoria della probabilità, già usata nella quantizzazione ([[disuguaglianza-di-chebyshev]], $\Delta^2/12$).
- I bit vanno poi trasmessi su canali passa-banda. La rappresentazione complessa in banda base ([[inviluppo-complesso]]) permette di descrivere segnali e canali passa-banda con segnali in banda base, quindi di fare modulazione e demodulazione in digitale. Il passaggio alla portante resta ai soli upconverter e downconverter ([[upconversion-e-downconversion]]).
- Rumore e segnali d'informazione non sono prevedibili: si modellano come processi aleatori ([[processo-aleatorio]]). Media, autocorrelazione e densità spettrale di potenza ([[densita-spettrale-di-potenza]]) dicono quanta potenza c'è e a quali frequenze, e come cambia attraverso i filtri ([[processi-e-sistemi-lti]]). Il processo gaussiano ([[processo-gaussiano]]) è il modello di riferimento per il rumore.
- I due temi si incontrano nei **processi passa-banda**: segnali e rumore reali, aleatori e passa-banda hanno un inviluppo complesso in banda base ([[processi-passa-banda]]), le cui componenti in fase e quadratura sono congiuntamente WSS. Le loro PSD discendono da quella del processo reale ([[psd-componenti-in-quadratura]]); con spettro simmetrico attorno alla portante le componenti sono incoerenti, e per il rumore gaussiano in banda ([[rumore-in-banda-passante]]) indipendenti.
- Il **modulatore** raggruppa i bit in simboli e li trasforma in forme d'onda ([[principi-di-modulazione]]); le forme d'onda diventano punti di uno spazio vettoriale ([[spazio-dei-segnali]]), e le costellazioni lineari (PAM, PSK, QAM) o ortogonali (FSK) sono configurazioni di punti ([[modulazione-lineare]], [[modulazione-ortogonale]]). Il ricevitore ottimo in AWGN decide con il criterio MAP/ML ([[rivelazione-map-ml]]), realizzato con correlatori o filtri adattati e equivalente alla minima distanza ([[ricevitore-ottimo-awgn]]); le prestazioni dipendono dalle distanze tra i punti ([[probabilita-errore-binaria]], [[probabilita-errore-m-aria]]).
- Per scegliere una modulazione servono criteri che non dipendano dalla forma d'onda: banda di Shannon, energia per bit, efficienza spettrale ed efficienza in potenza ([[parametri-globali-modulazioni]]). Il riferimento assoluto è la capacità di Shannon ([[informazione-mutua-e-capacita]]), da cui discende la frontiera $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$ ([[limite-di-shannon]]); il link budget ([[link-budget]]) traduce questi requisiti in potenze e distanze.
- Il ricevitore reale non è sincronizzato: il canale scala e ritarda il segnale e l'oscillatore locale ha un offset, quindi la costellazione arriva scalata e rotante ([[sincronizzazione]]). Ampiezza, fase, ritardo e frequenza si stimano a massima verosimiglianza ([[stima-dei-parametri]]), con simboli di training o in modo blind, e la fase si insegue nel tempo con il PLL ([[phase-locked-loop]]).
- Il canale reale ha anche banda limitata: gli impulsi si allargano e interferiscono ([[interferenza-intersimbolica]]). Il criterio di Nyquist e il coseno rialzato annullano l'ISI negli istanti di campionamento ([[criterio-di-nyquist]]); se il canale non si controlla, si equalizza, fino alla MLSE con l'algoritmo di Viterbi ([[equalizzazione]], [[algoritmo-di-viterbi]]).
- In alternativa all'equalizzazione si cambia il modo di trasmettere: l'OFDM divide il flusso su $N$ sottoportanti lente e ortogonali, su ognuna delle quali il canale è quasi piatto ([[ofdm]]); il prefisso ciclico elimina ISI e ICI e riduce il canale a un coefficiente per sottoportante ([[prefisso-ciclico]]), da compensare con una divisione ([[equalizzazione-ofdm]]); IFFT e FFT lo rendono realizzabile ([[ofdm-con-fft]]), al prezzo di PAPR alto e sensibilità agli offset ([[limiti-dell-ofdm]]). Approfondimento facoltativo, non d'esame: [[multiportante-ofdm-dmt-gelli]].

## Argomenti mancanti / da ingerire · [[Intro.pdf#page=18|p. 18]]

Temi principali ancora senza fonte (il tema 1 è coperto da [[rappresentazione-complessa-banda-base]], il tema 2 da [[processi-aleatori]], il 3 dalle Lezioni 8–12, il 4 da [[parameter-estimation-synchronization]], il 5 da [[signaling-bandlimited-channels]] e [[signaling-ofdm]]):
- teoria dell'informazione e codifica di canale — TODO
- rumore termico: solo qualitativo — TODO

## Fonti ingerite

16 — [[intro-corso]], [[elementi-teoria-probabilita]], [[campionamento-conversione-ad-da]], [[rappresentazione-complessa-banda-base]], [[processi-aleatori]], [[laboratorio-conversione-ad]] (laboratorio Matlab, non d'esame: macroblocchi in `laboratorio/`), [[rappresentazione-processi-passa-banda]], [[principles-of-modulation]], [[elementi-teoria-rivelazione]], [[appunti-lezione-28-ottobre]], [[appunti-lezione-2-novembre]], [[parametri-globali-e-capacita]], [[parameter-estimation-synchronization]], [[signaling-bandlimited-channels]], [[signaling-ofdm]], [[appunti-sparsi-lezioni]]

_Aggiornato: 2026-11-27 — Lezione 15 (OFDM), tema 5 completato; note di Gelli come approfondimento non d'esame, fuori dal conteggio; 2026-11-23 — Lezione 14 sulla versione aggiornata delle slide signaling (filtri RRC, equalizzazione frazionaria, ZF, MMSE, coefficienti β); 2026-11-22 — libro di riferimento di Biglieri indicato a lezione; 2026-11-16 — ingest di 11-9, Synchro, signaling e Lezioni.pdf (Lezioni 13–14, appunti sparsi); temi 4 e 5 coperti; ingest di Modulazione, Detection e appunti del 28/10 e del 2/11 (Lezioni 8–11), rinumerazione delle lezioni; 2026-11-15 — ingest di Confronto_new.pdf (parametri globali e capacità, Lezione 8, poi rinumerata 12); 2026-11-01 — ingest di Rappresentazione_Rice_processi.pdf (processi passa-banda, Lezione 7); 2026-09-30 — ingest del laboratorio Matlab sulla conversione A/D (non d'esame); 2026-09-28 — re-ingest di Rappresentazione_Rice.pdf e random_processes.pdf nella versione con appunti a mano (dimostrazioni della docente integrate come fonte); ingest random_processes.pdf (tema 2); 2026-09-25 — ingest Rappresentazione_Rice.pdf (tema 1); 2026-09-23 — primo ingest (3 fonti)_
