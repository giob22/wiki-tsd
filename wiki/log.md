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

## [2026-09-30] query | larghezza del filtro interpolatore (rettangolo e triangolo)
- risposta salvata in [[lab-interpolazione]], punto 5: rettangolo largo T, triangolo con base 2T; due condizioni (h(kT) = 0 per k ≠ 0 e somma delle copie = 1), collegamento con gli zeri di H_r(f) e con il bug di C = 1
- grafici 🧩 `grafico-lab-larghezza-filtro.png` (6 larghezze sullo stesso segnale) e `grafico-lab-somma-pesi.png` (somma delle copie con campioni tutti a 1), da `genera_grafici_laboratorio_ad.py`

## [2026-10-11] riorganizzazione | riferimenti solo nei titoli + compendio unico
- richiesta dell'utente: tutte le lezioni in un unico file; riferimenti ai PDF solo nei titoli di sezione e sottosezione, su tutto il wiki
- 1175 riferimenti ai PDF spostati dal corpo ai titoli (script `output/riferimenti_nei_titoli.py`): righe "📄 Fonte" di sola citazione rimosse, colonne "Pagina" delle tabelle rimosse, citazioni in didascalie e parentesi rimosse, citazioni che fanno parte di una frase ridotte a testo semplice "p. N"; restano invariati lezioni.md (indice) e log.md (storico)
- laboratorio: riferimenti alle righe di AD_conversion.m e alle figure spostati nei titoli
- 16 link a titoli ([[pagina#Titolo]]) trasformati in link alla pagina, perché i titoli ora contengono link e l'ancora non funzionerebbe
- nuovo [[corso-completo]] (406 KB, 49 argomenti in 6 lezioni), generato da `output/genera_compendio.py` nell'ordine di [[lezioni]]; in lezioni.md aggiunti [[disuguaglianza-di-chebyshev]] (Lezione 3) e la riga "Entità collegate"
- CLAUDE.md aggiornato: nuova regola di tracciabilità (riferimenti solo nei titoli), compendio da rigenerare a ogni ingest
- controllo: 0 link rotti, 0 ancore rotte, 0 link ai PDF nel corpo (esclusi lezioni.md e log.md)

## [2026-10-12] query | coseno campionato esattamente a f_c = 2 f_0
- risposta salvata in [[teorema-del-campionamento]] (nuova derivazione "Caso limite"): campioni (-1)^n cos(φ), ricostruzione ideale cos(φ) cos(2π f0 t), perdita della fase; spiegazione con le righe in ±f0 che si sommano in f_c/2; il "≥" del teorema vale per spettri continui, per una riga sul bordo serve ">"
- animazione 🧩 `grafico-nyquist-limite-coseno.gif` (script `output/grafici/genera_grafici_nyquist_limite.py`); identità della serie di Shannon verificata numericamente; compendio rigenerato

## [2026-10-14] query | animazione del companding
- animazione 🧩 `grafico-companding-animazione.gif` (script `output/grafici/genera_animazione_companding.py`): legge µ con µ da ~0 a 255; soglie uniformi su y riportate su x, caratteristica complessiva, SNR vs livello con b = 8 bit (Laplace)
- inserita in [[companding]], nuova sezione "Il companding in movimento"; nota sul picco dell'uniforme (~35 dB invece di 40.9) dovuto al sovraccarico con pdf di Laplace; compendio rigenerato

## [2026-10-14] correzione | modulo nelle formule dentro le tabelle
- segnalazione dell'utente: nella µ-law di [[companding]] mancava il modulo |x|; nelle tabelle il | era scritto \| e non si leggeva bene
- 25 righe di tabella in 12 pagine: modulo scritto con \lvert x\rvert, condizionamento con \mid, norma dell'energia con \lVert s\rVert ([[inviluppo-complesso]]); compendio rigenerato

## [2026-10-16] query | grafico della condizione f_c > B per i segnali passa-banda
- nuovo grafico 🧩 `grafico-rice-condizione-passabanda.png` (script `output/grafici/genera_grafico_condizione_passabanda.py`): f_c = 2B, B, B/2, B/4 con il bordo f_c − B/2 del lobo positivo
- inserito in [[segnali-banda-base-e-passa-banda]] nella derivazione "Perché si chiede f_c > B", con l'osservazione che basterebbe f_c > B/2; compendio [[corso-completo]] rigenerato

## [2026-10-16] correzione | formule inline spezzate
- segnalazione dell'utente su [[inviluppo-complesso]] (tabella delle formule): le definizioni di x_c e x_s sono corrette (slide 13, p. 17), ma la forma ampiezza-fase si leggeva «a = |s|$e$θ»
- causa: la correzione del modulo del 2026-10-14 aveva lasciato uno spazio dopo \rvert, e "\rvert $" non chiude la formula in Obsidian; tolti 21 spazi in 10 pagine, più uno spazio prima di $ in [[lab-quantizzazione]]; controllo automatico: 0 formule inline con spazi ai bordi; compendio rigenerato

## [2026-10-16] riorganizzazione | compendio nell'ordine delle slide
- segnalazione dell'utente: nella Lezione 4 di [[corso-completo]] l'inviluppo complesso veniva prima del segnale analitico e della trasformata di Hilbert (le pagine erano copiate intere nell'ordine di lezioni.md, cioè per prima comparsa nel PDF)
- `output/genera_compendio.py` riscritto: ogni pagina viene spezzata in sezioni, ogni sezione va alla pagina PDF citata nel titolo (mediana), mai prima della "Definizione" del suo argomento; 11 eccezioni nel dizionario COLLOCA; pagine fonte ed entità restano intere; "Perché importa" e "Connessioni" in fondo alla lezione; aggiunti per ogni lezione i refusi delle slide e le domande da esame della pagina fonte
- controllo su tutte le lezioni: ordine rivisto lezione per lezione (alternanze corrette, es. interpolazione/aliasing in Campionamento, momenti/stazionarietà/acf in Processi); 0 sezioni perse, 3739/3764 righe presenti (le 25 mancanti sono i rimandi "Fonti", esclusi di proposito); pagine PDF non coperte: solo le copertine; 0 link o ancore rotti, 0 formule spezzate
- CLAUDE.md aggiornato (punto 12 dell'ingest)

## [2026-10-16] riorganizzazione | corso completo diviso in capitoli
- richiesta dell'utente: il file unico era troppo pesante da navigare; [[corso-completo]] diventa l'indice, e ogni lezione è un capitolo in un file a sé in `wiki/corso/` (6 file, da 14 a 121 KB), con navigazione ← Lezione precedente · Indice · Lezione successiva → in cima e in fondo
- `output/genera_compendio.py` aggiornato (titoli alzati di un livello nei capitoli, capitoli vecchi cancellati a ogni rigenerazione); `output/riferimenti_nei_titoli.py` ora salta la cartella `corso/`
- nuovo `output/controlla_compendio.py`: controllo di integrità da lanciare dopo ogni rigenerazione
- controllo: 6 capitoli tutti nell'indice; 0 link, ancore o formule rotte; 0 sezioni mancanti; 3725/3725 righe di contenuto presenti; pagine PDF non coperte: solo le copertine
- aggiornati CLAUDE.md (struttura e punto 12 dell'ingest) e [[index]]

## [2026-10-20] immagini | upconversion e downconversion (Lezione 4)
- richiesta dell'utente: aggiungere immagini dove si parla di upconversion e downconversion
- 3 grafici 🧩 nuovi da `output/grafici/genera_grafici_upconversion.py`: `grafico-rice-upconversion-tempo.png` (rami I e Q, somma e inviluppo, eq. (17)), `grafico-rice-downconversion-tempo.png` (parte lenta più termini a 2f_c, uscita del passa-basso, eq. (21); verificata la coincidenza con s_c e s_s), `grafico-rice-up-down-frequenza.png` (eq. (14), copie a ±2f_c, passa-basso; ramo Q ricavato)
- due immagini dei PDF già estratte inserite in [[upconversion-e-downconversion]]: appunti di p. 2 (passaggio complesso ↔ reale) e slide 7 con le note (macroblocchi); larghezza fissata a 650 px
- nel grafico in frequenza corretta un'etichetta: la copia in banda base è la somma di due lobi (picco ~0.67), non 1/2
- capitoli rigenerati e controllati: 0 problemi, 3748/3748 righe di contenuto presenti

## [2026-10-20] immagini | requisito sul filtro passa-basso
- nuovo grafico 🧩 `grafico-rice-requisito-passabasso.png` (stesso script `genera_grafici_upconversion.py`): spettro dopo il moltiplicatore con banda utile |f| < W, copie a ±2f_c e riquadro del passa-basso; tre casi (taglio 5 kHz giusto, 1 kHz < W troppo basso, 19 kHz > 2f_c − W troppo alto) con le parti perse o lasciate passare
- inserito in [[upconversion-e-downconversion]], nella derivazione "Requisito sul filtro passa-basso"; capitoli rigenerati, controllo di integrità senza problemi

## [2026-10-20] correzione | asterischi dentro le formule
- segnalazione dell'utente su [[equivalente-banda-base-dei-filtri]]: la formula $y(t) = \frac{1}{\sqrt2}\,x(t) * h(t)$ in una didascalia in corsivo si leggeva spezzata, perché il `*` della convoluzione chiudeva il corsivo
- sostituito `*` con `\ast` in tutte le formule in linea (86 formule, 72 righe, 15 pagine; convoluzioni e coniugati come $S^\ast$); controllo: 0 formule in linea con `*` rimaste; capitoli rigenerati e controllati
- nuova regola in CLAUDE.md (sezione "Matematica e notazione")

## [2026-10-25] riorganizzazione | corso completo in un unico file schematico
- richiesta: eliminare le ridondanze del corso completo, un solo file con tutte le lezioni, solo contenuto delle slide
- `wiki/corso-completo.md` riscritto a mano: indice + lezioni 1–6 nell'ordine delle slide (circa 119 KB contro 458 KB dei capitoli generati); contiene solo slide, appunti a mano della docente e figure dei PDF (più tre figure di supporto richieste in lezione 4 e le figure del laboratorio in lezione 6); derivazioni 🧩, esercizi e grafici extra restano nelle pagine concetto/esercizio/laboratorio, richiamati da «Approfondimenti nel wiki»
- eliminati `wiki/corso/` (capitoli generati), `output/genera_compendio.py`, `output/controlla_compendio.py`; nuovo `output/controlla_corso.py` (link, ancore, immagini, formule, riferimenti PDF solo nei titoli, copertura pagine) e `output/crea_pdf.py` (PDF delle lezioni con Chrome + KaTeX)
- lezione 5 aggiornata con le slide 33, 40, 41 della nuova versione `raw/random_processes_v2.pdf` (la docente ha ricaricato il PDF)
- PDF di studio delle lezioni 5 e 6 in `output/pdf/`
- CLAUDE.md aggiornato (struttura e passo 12 dell'ingest)

## [2026-10-28] approfondimento | calcolo-densita-spettrale | caso 1 (slide 32) espanso passo per passo, su richiesta

## [2026-11-01] ingest | Representation of passband random processes (Rappresentazione_Rice_processi.pdf) | pagine coperte: 1-25
- fonte: [[rappresentazione-processi-passa-banda]] (13 slide + 12 pagine di appunti a mano, nuova Lezione 7)
- 3 concetti nuovi: [[processi-passa-banda]] (processo analitico, inviluppo e componenti I/Q di un processo; teorema sulla WSS congiunta con tutti i passaggi: media, relazioni di Hilbert (2)-(4), eq. (5)-(9), (10)-(12), perché R_xcxs(0)=0), [[psd-componenti-in-quadratura]] (eq. (13), (14), cross-PSD ricavata come 🧩, caso simmetrico e incoerenza), [[rumore-in-banda-passante]] (esempio, costruzione grafica, potenza N0·W)
- aggiornate con un collegamento: [[inviluppo-complesso]], [[segnale-analitico]], [[processi-e-sistemi-lti]], [[densita-spettrale-di-potenza]], [[processo-gaussiano]], [[momenti-di-un-processo]]; aggiornati [[overview]], [[index]], [[lezioni]]
- [[corso-completo]]: nuova sezione «Lezione 7» (solo slide e appunti, schematica), con 3 figure dal PDF (`processi-passabanda-p20/p24/p25-*.png` in `raw/assets/`); `output/controlla_corso.py`: nessun problema (non citata solo p. 1, il titolo)
- revisione di copertura pagina per pagina: nulla mancante; aggiunte solo spiegazioni 🧩 (cross-PSD, seconda via per R_xcxs(0)=0 per disparità, verifica inversa che le condizioni (10) rendono x_p WSS, ruolo dei gradini nella simmetria)
- dubbi segnalati in [[rappresentazione-processi-passa-banda]]: W è semilarghezza nella slide 2 e larghezza del lobo dalla slide 10; nota a mano di p. 4 in parte illeggibile; segno di f_c negli appunti di p. 22

## [2026-11-07] aggiornamento | sito di studio dell'intercorso | frase della Lezione 7 riformulata
- `output/crea_sito.py` e `output/sito_disegni.py`: generano il sito (HTML statico con formule KaTeX, 19 disegni SVG, tema sistema/chiaro/scuro) a partire da [[corso-completo]] e dalle pagine concetto; pubblicato nel branch orfano `gh-pages`
- [[corso-completo]]: corrette due formule con doppio `\tag` (Lezione 4, eq. 5-6 e 11-12) che non si rendevano; riformulata la frase iniziale della Lezione 7 sul processo analitico (spiega la ridondanza dei lobi in ±f_c)

## [2026-11-08] aggiornamento | sito di studio | riferimenti alle equazioni con anteprima
- `output/crea_sito.py`: nel testo delle lezioni i richiami tipo «(10)» diventano link all'equazione numerata; al passaggio del mouse (o al tocco su telefono) compare un popup con la formula intera, rimpicciolita se serve per stare in una riga, e un link «vai all'equazione»; gli elenchi numerati «(1) … (2) …» non vengono scambiati per riferimenti

## [2026-11-08] aggiornamento | sito di studio | legge dei 6 dB nell'intercorso
- `output/crea_sito.py`: la Lezione 3 del sito parte ora dal quantizzatore uniforme (relazione ingresso-uscita, codifica binaria, errore, fattore di carico, SNR e legge dei 6 dB/bit, progetto) e include le pagine [[quantizzazione-uniforme]], [[snr-di-quantizzazione]] e l'esercizio [[dimensionamento-quantizzatore]]; aggiornati titolo, introduzione e legenda dell'indice

## [2026-11-09] aggiornamento | sito di studio | disegno «chi è chi» nell'upconverter
- `output/sito_disegni.py`, `output/crea_sito.py`: nuovo disegno nella Lezione 4 (sezione «Energia dell'inviluppo») che distingue $s_c$, $s_s$ (inviluppo, banda base) da $x_c$, $x_s$ (uscite dei due rami dell'upconverter, passa-banda, ortogonali) e da $s_p=x_c-x_s$, con gli spettri $S_c$, $X_c$, $S_p$; ramo I = coseno, ramo Q = seno
