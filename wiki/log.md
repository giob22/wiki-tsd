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

## [2026-09-24] revisione | companding: resa esplicita l'idea "quantizzare uniformemente F(x) = quantizzare in modo non uniforme x"
- [[companding]]: nuova sezione *Idea chiave del companding* (pp. 36, 38, 39): problema, idea, perché la catena è un quantizzatore non uniforme, cosa si sposta su $F$, criterio di scelta; formula 🧩 $Q(x) = F^{-1}(Q_u(F(x)))$
- nuova derivazione 🧩 *Esempio µ-law, soglie e livelli equivalenti* ($\mu = 255$, $M = 8$; confronto esatto/alta risoluzione per $M$ = 8, 16, 256); grafico `grafico-companding-soglie-mu.png`
- collegamenti espliciti in [[quantizzazione-non-uniforme]], [[legge-mu]], [[campionamento-conversione-ad-da]] (punto chiave 12, domanda d'esame), [[index]]
- regola dell'utente da oggi: ogni concetto va reso esplicito (la wiki serve per studiare)

## [2026-09-24] query | aliasing: perché il coseno a 1.5 kHz campionato a 2 kHz si ricostruisce a 0.5 kHz
- [[aliasing]]: nuova sezione *Perché il segnale ricostruito è a 0.5 kHz* (pp. 12, 14, 15, 17, 18): campioni ambigui (tabella + derivazione 🧩), scelta del LPF, vista in frequenza con le repliche, effetto stroboscopio, regola generale, nota sul seno
- 2 animazioni GIF (`grafico-aliasing-animazione.gif`, `grafico-aliasing-stroboscopio.gif`) + grafico `grafico-aliasing-ripiegamento.png`; link da [[campionamento-e-aliasing]] (Caso 3, trappole)
- venv Python in `C:\Users\giova\.venvs\wiki-tsd` (numpy, scipy, matplotlib, pillow), fuori da OneDrive e dalla repo

## [2026-09-24] revisione | lezioni.md: un punto per pagina del wiki
- argomenti che portano alla stessa pagina raggruppati in un solo punto, con sintesi del contenuto e pagine PDF (link abbreviati «p. N»); ordine = prima comparsa nel PDF
- Lezione 1: 16 → 3 punti; Lezione 2: 28 → 10; Lezione 3: 31 → 8. Tutte le pagine PDF restano coperte

## [2026-09-25] ingest | Complex baseband representation (Rappresentazione_Rice.pdf) | pagine coperte: 1-23
- PDF di 23 pagine: 19 slide + 4 pagine di appunti a mano (p. 2, 7, 16, 18) e annotazioni sulle slide; appunti integrati come fonte (scelta dell'utente), citazioni «p. N (slide M)»
- fonte: [[rappresentazione-complessa-banda-base]] (con tabella pagine PDF ↔ slide); 6 concetti: [[modulazione-digitale]], [[segnali-banda-base-e-passa-banda]], [[segnale-analitico]], [[inviluppo-complesso]], [[upconversion-e-downconversion]], [[equivalente-banda-base-dei-filtri]]
- derivazioni espanse: (4), (7), (8), (10), trasformate di sgn e 1/(πt), controllo (11)→(3), perché √2 (energia), (14), (15)–(17), forma ampiezza-fase, (18) con Parseval (dagli appunti p.16, ipotesi W < f_c esplicitata), (19), (20), campionamento passa-banda vs inviluppo, (21) e ramo Q, requisito sul passa-basso, (22)–(25), altezze delle figure
- refusi: slide 10 S→S_p (corretto a mano), appunti p.16 segno in X_c(f), A e B come altezze nelle figure slide 11/17, figura slide 18 senza 1/√2
- 11 figure in raw/assets (rappresentazione-rice-pN-*.png); grafici 🧩: catena degli spettri, I/Q nel tempo, GIF della downconversion (script genera_grafici_rappresentazione_rice.py; PyMuPDF aggiunto al venv per leggere le pagine)
- aggiornati: [[sistema-comunicazione-digitale]], [[teorema-del-campionamento]], [[overview]], [[index]], [[lezioni]] (Lezione 4)
- revisione di copertura totale pp. 1–23 (testo, figure, appunti): aggiunta l'intestazione della slide 1

## [2026-09-28] ingest | Stochastic processes (random_processes.pdf) | pagine coperte: 1-41
- 41 slide, nessun appunto a mano (pagina PDF = numero di slide)
- fonte: [[processi-aleatori]]; 7 concetti: [[processo-aleatorio]], [[momenti-di-un-processo]], [[stazionarieta]], [[autocorrelazione-processi-wss]], [[processi-e-sistemi-lti]], [[densita-spettrale-di-potenza]], [[processo-gaussiano]]; esercizio: [[calcolo-densita-spettrale]] (esempio della slide 32 svolto con ipotesi esplicite, scelta dell'utente)
- derivazioni espanse: coerenza delle marginali, (5), R_XY(τ) = R_YX(−τ), indipendenti ⇒ incorrelati, momenti dell'esempio rect, stazionarietà di primo e secondo ordine, ordine k ⇒ k−1, SSS ⇒ WSS, proprietà 1–3 dell'autocorrelazione (anche con Schwarz), τ_dec, (15)–(16), (19)→(20), R_YX e R_XY, ingresso WSS ⇒ uscita WSS, (22), dimostrazione di Wiener-Khinchin, proprietà 1–5 della PSD, 2Δf·S_XX, S_XY = S*_YX, (27)–(30), esempio esponenziale, gaussiana n = 1 e n = 2, Σ semidefinita positiva, (34), WSS ⇒ SSS per i gaussiani
- refusi: p.5 (∂^n → ∂^k, rimando alla (36) → (1)), p.40 (f(x,x) → f(x,y))
- 6 figure in raw/assets (random-processes-pN-*.png); grafici 🧩: realizzazioni e v.a. a t0, lento contro veloce (acf e PSD), gaussiana bivariata, GIF della costruzione di R_XX(τ) (script genera_grafici_random_processes.py)
- collegamenti aggiunti: [[quantizzazione-non-uniforme]] e [[algoritmo-lloyd-max]] (stazionarietà del primo ordine), [[correlazione-e-covarianza]], [[coppie-di-variabili-aleatorie]], [[variabile-aleatoria-gaussiana]], [[modulazione-digitale]], [[sistema-comunicazione-digitale]] (rumore termico: resta TODO), [[intro-corso]]; aggiornati [[overview]], [[index]], [[lezioni]] (Lezione 5)
- revisione di copertura totale pp. 1–41 (testo e figure)

## [2026-09-28] re-ingest | Rappresentazione_Rice.pdf (27 pp.) e random_processes.pdf (46 pp.) con appunti a mano e dimostrazioni della docente | parziale
- tutti i riferimenti di pagina rimappati (480 link + intestazioni YAML); 28 figure rigenerate dai nuovi PDF, 13 vecchie rimosse
- integrati gli appunti in [[modulazione-digitale]], [[segnali-banda-base-e-passa-banda]], [[segnale-analitico]], [[inviluppo-complesso]] (dimostrazioni di (18)–(20) ora da fonte; refusi degli appunti segnalati)
- TODO (interrotto su richiesta dell'utente): [[equivalente-banda-base-dei-filtri]] (appunti p.24, slide 18), [[upconversion-e-downconversion]] (note p.2, p.20, p.22), appunti dei processi aleatori (p.3–5, 8–10) in [[processo-aleatorio]] e [[momenti-di-un-processo]]; revisione di copertura da rifare. Elenco nelle "Domande aperte" delle due pagine fonte

## [2026-09-28] re-ingest | Rappresentazione_Rice.pdf e random_processes.pdf con appunti a mano | completato | pagine coperte: 1-27 e 1-46
- [[equivalente-banda-base-dei-filtri]]: dimostrazione della (22) presa dagli appunti di p.24, con i due trucchi spiegati ($u \to u^2$ e $\cdot\sqrt2/\sqrt2$); (24)–(25) dalla nota a mano di p.26 (📄 invece di 🧩); uscita $y(t)$ verso il DSP in banda base; embed di p.24
- [[upconversion-e-downconversion]]: passaggio complesso ↔ reale in Tx e Rx (p.2), con ⚠️ sul DSP rispetto allo schema della slide 7; «esce l'inviluppo» e «tagliati dal filtro» (p.20); macroblocchi e svincolo da $f_c$ (p.10); nota di p.22; ruolo dei convertitori riformulato su slide 6–7
- [[processo-aleatorio]]: dal segnale deterministico al processo (p.3); fissare $\omega$ o $t$ e tempo continuo/discreto (p.4–5); esempio della sinusoide a fase casuale; CDF del primo e del secondo ordine (p.8, ⚠️ $t_1 \in \mathbb{Z}$); marginale della pdf e correzione $\partial^k$ (p.9, ❓ nota «non si dice marginalizzazione»); DF del processo di Bernoulli con derivazione, tabella e sanity check (p.10); 5 embed degli appunti
- [[momenti-di-un-processo]]: 🧩 media e autocorrelazione della sinusoide a fase casuale ($\mu_X = 0$, $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$, WSS), verificate con Monte Carlo; [[stazionarieta]]: la sinusoide come esempio WSS
- pagine fonte: tabella "Appunti a mano" rifatta per [[rappresentazione-complessa-banda-base]] (19 righe) e creata per [[processi-aleatori]]; domande aperte aggiornate, TODO rimossi; aggiornati [[lezioni]], [[index]] (range di pagine erano ancora quelli vecchi), [[overview]]
- corretti due TAB spuri (`\to`, `\text` rovinati da script precedenti) in [[processi-aleatori]] e [[rappresentazione-complessa-banda-base]]
- revisione di copertura totale su entrambi i PDF, pagina per pagina: ogni pagina di appunti e ogni nota sulle slide ha una controparte nel wiki; in random_processes le pagine 11–46 non hanno inchiostro (verificato sui tracciati vettoriali del PDF); link check: 0 link rotti

## [2026-09-30] ingest | Laboratorio Matlab: conversione A/D e D/A (raw/scripts/09_28_2006) | coperto: AD_conversion.m righe 1-204 + 3 figure
- materiale non d'esame (Matlab escluso dall'esame), registrato come Lezione 6 in [[lezioni]]; scelte dell'utente: cartella `laboratorio/`, un macroblocco per pagina, macroblocco 0 di setup aggiunto ai quattro richiesti
- fonte: [[laboratorio-conversione-ad]]; macroblocchi: [[lab-setup-e-spettro]], [[lab-campionamento]], [[lab-interpolazione]], [[lab-quantizzazione]], [[lab-snr]]
- derivazioni: dt e Ts arrotondati, dt*FFT come somma di Riemann, trapezio = rect * rect e S(f) = 3 sinc(3f) sinc(f), energia 8/3, conv = serie di interpolazione, durata della convoluzione = somma delle durate, indice del taglio (L-1)/2, codebook e livelli, SNR stampato 16.7 dB, fattore 3 (4.77 dB) rispetto al modello Δ²/12, pendenza 6 dB/bit, aliasing dell'esempio 2 (fs = 7.94 Hz < 8 Hz)
- osservazioni sul codice: ZOH (C = 1) con punto in comune tra rettangoli (picchi a 2) e anticipato di Ts/2 dal taglio simmetrico; zero non rappresentabile (livelli al centro delle celle); s_min calcolato anche sugli zeri; SNR dipendente dalla finestra (28.4 dB su |t| < 2.5 s)
- replica Python dello script e grafici 🧩 in `output/grafici/genera_grafici_laboratorio_ad.py`: 7 PNG + GIF dell'interpolazione; 3 figure del laboratorio copiate in raw/assets (lab-0928-*)
- collegamenti aggiunti nei concetti teorici: [[interpolazione]], [[teorema-del-campionamento]], [[aliasing]], [[quantizzazione-uniforme]], [[snr-di-quantizzazione]], [[conversione-ad-da]]; aggiornati [[index]], [[overview]], [[lezioni]]
- revisione di copertura: tutte le righe dello script (compreso il blocco audio commentato e le righe 199-202) e tutti i pannelli delle 3 figure hanno una controparte nel wiki
