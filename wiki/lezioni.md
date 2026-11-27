# Lezioni — Trasmissione dei Segnali Digitali

Elenco delle lezioni con gli argomenti del wiki. Per ogni lezione c'è **un punto per ogni pagina del wiki**, con una sintesi di cosa contiene e le pagine PDF da cui viene. I punti seguono l'ordine in cui l'argomento compare per la prima volta nel PDF.
Regola: 1 PDF = 1 lezione, salvo diversa indicazione (lezioni con più PDF vengono unite su richiesta).
Ordine delle lezioni ricavato dalla data di creazione dei PDF.
Il testo di studio schematico di tutte le lezioni è [[corso-completo]]; i PDF delle lezioni si creano con `output/crea_pdf.py` (cartella `output/pdf/`).

---

## Lezione 1 — Introduzione al corso
**PDF:** [[Intro.pdf]] (pp. 1–21) · **Fonte:** [[intro-corso]]

1. [[intro-corso]] — organizzazione del corso (docente, testo, esame orale) e programma ([[Intro.pdf#page=2|p. 2]]–[[Intro.pdf#page=3|3]]).
2. [[sistema-comunicazione-digitale]] — cos'è la comunicazione e come avviene; elementi di un sistema (trasmettitore, canale, ricevitore); digitale contro analogico ([[Intro.pdf#page=4|p. 4]]–[[Intro.pdf#page=10|10]]). Poi altri vantaggi dei circuiti digitali e lo schema a blocchi del sistema digitale, blocco per blocco: codificatore di sorgente (con bit rate tipici), codificatore di canale e modulatore, canale e rumore termico, demodulatore e decodificatore di canale, decodificatore di sorgente. Chiude con i vantaggi dell'approccio digitale, il principio di separazione e le comunicazioni semantiche ([[Intro.pdf#page=13|p. 13]]–[[Intro.pdf#page=21|21]]).
3. [[ripetitore-rigenerativo]] — come gli impulsi si degradano lungo il canale e come il ripetitore li rigenera ([[Intro.pdf#page=11|p. 11]]–[[Intro.pdf#page=12|12]]).

---

## Lezione 2 — Elementi di teoria della probabilità
**PDF:** [[Probabilità.pdf]] (pp. 1–38) · **Fonte:** [[elementi-teoria-probabilita]]

1. [[spazio-di-probabilita]] — esperimento aleatorio, spazio campione ed eventi; spazio degli eventi e assiomi di Kolmogorov; proprietà elementari della probabilità ([[Probabilità.pdf#page=2|p. 2]]–[[Probabilità.pdf#page=6|6]]).
2. [[probabilita-condizionale]] — probabilità condizionale; legge della probabilità composta e regola della catena; indipendenza tra eventi ([[Probabilità.pdf#page=7|p. 7]]–[[Probabilità.pdf#page=12|12]]).
3. [[probabilita-totale-e-bayes]] — teorema della probabilità totale e teorema di Bayes ([[Probabilità.pdf#page=13|p. 13]]–[[Probabilità.pdf#page=14|14]]).
4. [[variabile-aleatoria]] — definizione di variabile aleatoria; CDF e v.a. discrete, continue e miste; pdf; DF (pmf) ([[Probabilità.pdf#page=15|p. 15]]–[[Probabilità.pdf#page=19|19]]).
5. [[variabili-aleatorie-notevoli]] — v.a. di Bernoulli, Binomiale e Uniforme ([[Probabilità.pdf#page=20|p. 20]]–[[Probabilità.pdf#page=22|22]]).
6. [[variabile-aleatoria-gaussiana]] — pdf gaussiana; CDF, erf, erfc e funzione Q, con il calcolo in Matlab ([[Probabilità.pdf#page=23|p. 23]]–[[Probabilità.pdf#page=26|26]]).
7. [[funzione-di-variabile-aleatoria]] — pdf di una funzione $Y = g(X)$ di una variabile aleatoria ([[Probabilità.pdf#page=27|p. 27]]).
8. [[media-e-varianza]] — media statistica, momenti e teorema fondamentale della media; varianza e deviazione standard; proprietà di media e varianza ([[Probabilità.pdf#page=28|p. 28]]–[[Probabilità.pdf#page=30|30]]).
9. [[coppie-di-variabili-aleatorie]] — CDF e pdf congiunte e marginali; distribuzioni condizionali; indipendenza statistica ([[Probabilità.pdf#page=31|p. 31]]–[[Probabilità.pdf#page=35|35]]).
10. [[correlazione-e-covarianza]] — teorema fondamentale della media per coppie; correlazione, covarianza e coefficiente di correlazione; proprietà e disuguaglianza di Schwarz ([[Probabilità.pdf#page=36|p. 36]]–[[Probabilità.pdf#page=38|38]]).

Esercizi collegati: [[calcolo-probabilita-eventi]], [[cdf-pdf-variabili-notevoli]]

---

## Lezione 3 — Campionamento e conversione A/D e D/A
**PDF:** [[Campionamento_AD_DA.pdf]] (pp. 1–43) · **Fonte:** [[campionamento-conversione-ad-da]]

1. [[conversione-ad-da]] — perché si passa dall'elaborazione analogica a quella digitale (tecnologie e vantaggi); la conversione A/D come campionamento + quantizzazione, la D/A come interpolazione ([[Campionamento_AD_DA.pdf#page=2|p. 2]]–[[Campionamento_AD_DA.pdf#page=6|6]]).
2. [[teorema-del-campionamento]] — campionamento uniforme e scelta di $f_c$; quando il campionamento è invertibile; campionamento ideale e spettro del segnale campionato (repliche ogni $f_c$); i tre casi e il teorema di Shannon; ricostruzione con LPF ideale; effetti pratici e sovracampionamento ([[Campionamento_AD_DA.pdf#page=7|p. 7]]–[[Campionamento_AD_DA.pdf#page=16|16]]).
3. [[interpolazione]] — interpolazione ideale con la serie di Shannon ([[Campionamento_AD_DA.pdf#page=17|p. 17]]); interpolazione non ideale vista in frequenza, Zero-Order Hold e First-Order Hold ([[Campionamento_AD_DA.pdf#page=22|p. 22]]–[[Campionamento_AD_DA.pdf#page=24|24]]).
4. [[aliasing]] — cos'è l'aliasing e perché un coseno a 1.5 kHz campionato a 2 kHz si ricostruisce a 0.5 kHz; le due ipotesi ideali del teorema; segnali a banda solo praticamente limitata; sovracampionamento e filtro antialiasing ([[Campionamento_AD_DA.pdf#page=18|p. 18]]–[[Campionamento_AD_DA.pdf#page=21|21]]).
5. [[quantizzazione-uniforme]] — quantizzatore uniforme ($\Delta$, $M$, dinamica); codifica binaria; errore di quantizzazione, regione granulare e di sovraccarico; fattore di carico e probabilità di sovraccarico con la [[disuguaglianza-di-chebyshev]] ([[Campionamento_AD_DA.pdf#page=25|p. 25]]–[[Campionamento_AD_DA.pdf#page=29|29]]).
6. [[disuguaglianza-di-chebyshev]] — la disuguaglianza di Chebyshev e il limite superiore alla probabilità di sovraccarico, $P_s \le 1/k_c^2$, confrontato con il valore esatto per la pdf di Laplace ([[Campionamento_AD_DA.pdf#page=29|p. 29]]).
7. [[snr-di-quantizzazione]] — SNR di quantizzazione e legge dei 6 dB/bit; progetto di un quantizzatore audio, Esempio 7.6, svolto in [[dimensionamento-quantizzatore]] ([[Campionamento_AD_DA.pdf#page=30|p. 30]]–[[Campionamento_AD_DA.pdf#page=31|31]]).
8. [[quantizzazione-non-uniforme]] — limiti della quantizzazione uniforme e pdf di Laplace della voce; quantizzatore non uniforme; quantizzatore ottimo di Lloyd-Max ([[algoritmo-lloyd-max]]); limiti della quantizzazione ottima e quantizzazione robusta ([[Campionamento_AD_DA.pdf#page=32|p. 32]]–[[Campionamento_AD_DA.pdf#page=36|36]]).
9. [[companding]] — perché compressione + quantizzazione uniforme equivale a una quantizzazione non uniforme; analisi ad alta risoluzione; legge logaritmica; leggi [[legge-mu]] e [[legge-a]] (standard [[g711]]); prestazioni ([[Campionamento_AD_DA.pdf#page=36|p. 36]]–[[Campionamento_AD_DA.pdf#page=43|43]]).

Esercizi collegati: [[campionamento-e-aliasing]], [[dimensionamento-quantizzatore]]
Entità collegate: [[algoritmo-lloyd-max]], [[legge-mu]], [[legge-a]], [[g711]]

---

## Lezione 4 — Rappresentazione complessa in banda base
**PDF:** [[Rappresentazione_Rice.pdf]] (pp. 1–27: 19 slide più 8 pagine di appunti a mano) · **Fonte:** [[rappresentazione-complessa-banda-base]]
Le pagine sotto sono quelle del PDF, non i numeri delle slide; la corrispondenza è nella pagina fonte.

1. [[modulazione-digitale]] — la catena sorgente → modulatore → canale; la modulazione come rappresentazione dei bit con forme d'onda analogiche; esempio di modulazione lineare binaria con impulsi rettangolari; le forme d'onda devono stare in una porzione di spettro ([[Rappresentazione_Rice.pdf#page=2|p. 2]]–[[Rappresentazione_Rice.pdf#page=3|3]]).
2. [[segnali-banda-base-e-passa-banda]] — definizioni di segnale e canale in banda base e in banda passante; simmetria hermitiana dei segnali reali; banda monolatera e bilatera; segnali a banda stretta ([[Rappresentazione_Rice.pdf#page=4|p. 4]]–[[Rappresentazione_Rice.pdf#page=8|8]]).
3. [[inviluppo-complesso]] — perché tutta l'informazione sta in un segnale complesso in banda base e perché conviene elaborarlo in digitale, con i vantaggi elencati negli appunti ([[Rappresentazione_Rice.pdf#page=6|p. 6]], [[Rappresentazione_Rice.pdf#page=9|9]]–[[Rappresentazione_Rice.pdf#page=10|10]]). Poi la definizione dell'inviluppo, le componenti in fase e quadratura, il ritorno al passa-banda, l'ortogonalità di I e Q e la conservazione dell'energia, con le dimostrazioni degli appunti ([[Rappresentazione_Rice.pdf#page=15|p. 15]]–[[Rappresentazione_Rice.pdf#page=19|19]]). Infine la banda di un segnale complesso ([[Rappresentazione_Rice.pdf#page=27|p. 27]]).
4. [[segnale-analitico]] — definizione con il $\sqrt2$, espressione nel tempo con la trasformata di Hilbert, ritorno al segnale reale, trasformata di Hilbert in frequenza e sfasamento di ∓90°; trasformata di $\text{sgn}$ negli appunti ([[Rappresentazione_Rice.pdf#page=11|p. 11]]–[[Rappresentazione_Rice.pdf#page=14|14]]).
5. [[upconversion-e-downconversion]] — il passaggio complesso ↔ reale in trasmissione e ricezione ([[Rappresentazione_Rice.pdf#page=2|p. 2]]); schemi con moltiplicatori e passa-basso; upconverter, canale e downconverter visti come un unico canale; la fase dovuta a $f_c$ non porta informazione ([[Rappresentazione_Rice.pdf#page=20|p. 20]]–[[Rappresentazione_Rice.pdf#page=22|22]]).
6. [[equivalente-banda-base-dei-filtri]] — un filtro passa-banda in banda base complessa: $Y = SH/\sqrt2$, $y = s \ast h/\sqrt2$, dimostrazione della (22) negli appunti; realizzazione con quattro filtri reali ([[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]).

---

## Lezione 5 — Laboratorio Matlab: conversione A/D e D/A (28/09)
**Materiale:** [[AD_conversion.m]] e 3 figure, in `raw/scripts/09_28_2006/` · **Fonte:** [[laboratorio-conversione-ad]]
> ⚠️ Non materia d'esame: serve a vedere cosa succede nella teoria della Lezione 3. Riferimenti alle righe dello script.

1. [[lab-setup-e-spettro]] — il tempo "continuo" simulato con una griglia di passo $dt = 6$ ms; i due segnali di prova (trapezio e tre sinusoidi); lo spettro come $dt\cdot$FFT, confrontato con la trasformata esatta del trapezio (righe 5–85; [[Figure_1.png]]).
2. [[lab-campionamento]] — $f_s = 2W$ arrotondato alla griglia; `s.*high` come segnale campionato idealmente; repliche e aliasing; esempio 2 campionato sotto Nyquist (righe 87–101; [[Figure_1.png]]).
3. [[lab-interpolazione]] — rettangolo, triangolo e sinc; la convoluzione come serie di interpolazione; perché dura la somma delle durate e dove va tagliata (righe 103–144, 199–202; [[Figure_2_interpolazione_lineaare.png]], [[Figure_2_interpolazione_shannon.png]]).
4. [[lab-quantizzazione]] — quantizzatore uniforme a 4 bit con i livelli al centro delle celle; lo zero diventa $\Delta/2$ (righe 146–187).
5. [[lab-snr]] — cosa misura l'SNR stampato (16.7 dB); la pendenza di 6 dB/bit e perché resta 4.77 dB sotto il modello $\Delta^2/12$ (righe 189–192).

---

## Lezione 6 — Processi aleatori
**PDF:** [[random_processes.pdf]] (pp. 1–46: 41 slide più 5 pagine di appunti a mano); versione aggiornata dalla docente [[random_processes_v2.pdf]] (41 pagine, cambiate le slide 33, 40, 41) · **Fonte:** [[processi-aleatori]]

1. [[processo-aleatorio]] — il processo come estensione della variabile aleatoria ai segnali; i due punti di vista (forme d'onda e variabili aleatorie nel tempo) e cosa si ottiene fissando $\omega$ o $t$; esempi del rettangolo di segno casuale e, negli appunti, della sinusoide a fase casuale; caratterizzazione completa con le distribuzioni congiunte di ordine $k$, costruite negli appunti dal primo e dal secondo ordine; DF del processo di Bernoulli (appunti) ([[random_processes.pdf#page=2|p. 2]]–[[random_processes.pdf#page=11|11]]); processi a tempo discreto ([[random_processes.pdf#page=45|p. 45]]).
2. [[momenti-di-un-processo]] — media, autocorrelazione e autocovarianza, con i momenti calcolati per il rettangolo e per la sinusoide degli appunti ([[random_processes.pdf#page=4|p. 4]]–[[random_processes.pdf#page=5|5]], [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]]); mutue correlazioni e covarianze, processi indipendenti, incoerenti e incorrelati, processi complessi ([[random_processes.pdf#page=22|p. 22]]–[[random_processes.pdf#page=25|25]]); momenti a tempo discreto ([[random_processes.pdf#page=45|p. 45]]–[[random_processes.pdf#page=46|46]]).
3. [[stazionarieta]] — stazionarietà di ordine $k$, in senso stretto, del primo e del secondo ordine, in senso lato (WSS); SSS ⇒ WSS ([[random_processes.pdf#page=15|p. 15]]–[[random_processes.pdf#page=18|18]]).
4. [[autocorrelazione-processi-wss]] — lag-acf e sue proprietà, autocorrelazione normalizzata, significato fisico e tempo di decorrelazione ([[random_processes.pdf#page=19|p. 19]]–[[random_processes.pdf#page=21|21]]).
5. [[processi-e-sistemi-lti]] — media e correlazioni all'uscita di un filtro LTI; ingresso WSS ⇒ uscita WSS; l'incoerenza si conserva ([[random_processes.pdf#page=26|p. 26]]–[[random_processes.pdf#page=31|31]]); PSD dell'uscita ([[random_processes.pdf#page=33|p. 33]]).
6. [[densita-spettrale-di-potenza]] — definizione e Wiener-Khinchin ([[random_processes.pdf#page=32|p. 32]]); significato fisico, proprietà, densità spettrali mutue, PSD della somma di due processi ([[random_processes.pdf#page=34|p. 34]]–[[random_processes.pdf#page=40|40]]); PSD a tempo discreto ([[random_processes.pdf#page=46|p. 46]]).
7. [[processo-gaussiano]] — definizione, gaussiana multivariata, perché è così usato, proprietà ([[random_processes.pdf#page=41|p. 41]]–[[random_processes.pdf#page=44|44]]).

Esercizi collegati: [[calcolo-densita-spettrale]] (esempio della slide 32)

---

## Lezione 7 — Rappresentazione dei processi passa-banda
**PDF:** [[Rappresentazione_Rice_processi.pdf]] (pp. 1–25: 13 slide più 12 pagine di appunti a mano) · **Fonte:** [[rappresentazione-processi-passa-banda]]
Le pagine sotto sono quelle del PDF, non i numeri delle slide; la corrispondenza è nella pagina fonte.

1. [[processi-passa-banda]] — ipotesi (processi reali, WSS, a media nulla); processi in banda base e passa-banda; processo analitico e filtro di Hilbert; inviluppo complesso del processo e componenti in fase e quadratura ([[Rappresentazione_Rice_processi.pdf#page=2|p. 2]]–[[Rappresentazione_Rice_processi.pdf#page=5|5]]). Teorema: se $x_p$ è WSS a media nulla, $x_c$ e $x_s$ sono congiuntamente WSS; media nulla, relazioni tra $x_p$ e la sua trasformata di Hilbert, $R_{x_cx_c}$ e mutue passo per passo, condizioni (10), acf dell'inviluppo e $R_{x_cx_s}(0) = 0$ ([[Rappresentazione_Rice_processi.pdf#page=6|p. 6]]–[[Rappresentazione_Rice_processi.pdf#page=11|11]]).
2. [[psd-componenti-in-quadratura]] — PSD delle componenti in quadratura (eq. 13) e cross-PSD ([[Rappresentazione_Rice_processi.pdf#page=12|p. 12]], [[Rappresentazione_Rice_processi.pdf#page=13|13]]); PSD dell'inviluppo come PSD del processo analitico traslata (eq. 14, [[Rappresentazione_Rice_processi.pdf#page=14|p. 14]]–[[Rappresentazione_Rice_processi.pdf#page=16|16]]); caso di spettro simmetrico attorno a $f_c$: $S_{xx}$ pari, $R_{xx}$ reale, componenti incoerenti, $S_{xx} = 2S_{x_cx_c}$ ([[Rappresentazione_Rice_processi.pdf#page=17|p. 17]]–[[Rappresentazione_Rice_processi.pdf#page=19|19]]); vista grafica ([[Rappresentazione_Rice_processi.pdf#page=20|p. 20]]).
3. [[rumore-in-banda-passante]] — rumore a PSD costante in banda, perché l'AWGN ha potenza infinita e il ricevitore filtra; PSD delle componenti e dell'inviluppo, costruzione grafica con la (13), conservazione della potenza $N_0W$, indipendenza delle componenti se gaussiano ([[Rappresentazione_Rice_processi.pdf#page=21|p. 21]]–[[Rappresentazione_Rice_processi.pdf#page=25|25]]).

## Lezione 8 — Principi di modulazione
**PDF:** [[Modulazione.pdf]] (copia GoodNotes in `raw/goodnotes/`: 23 slide più 16 pagine di appunti a lezione; primo caricamento 16/10) · **Fonte:** [[principles-of-modulation]]

1. [[principi-di-modulazione]] — modulatore = mapper + generatore, bit rate raw ([[Modulazione.pdf#page=2|p. 2]], [[Modulazione.pdf#page=3|p. 3]]); simboli, baud rate $R_s=R_b/\log_2M$, modulazione con e senza memoria ([[Modulazione.pdf#page=4|p. 4]], [[Modulazione.pdf#page=5|p. 5]]); esempio di Benedetto-Biglieri con $M=2,4,8$ ([[Modulazione.pdf#page=6|p. 6]], [[Modulazione.pdf#page=7|p. 7]]); compromesso potenza-banda-complessità e spettro sinc² ([[Modulazione.pdf#page=8|p. 8]]–[[Modulazione.pdf#page=11|11]]).
2. [[spazio-dei-segnali]] — rappresentazione discreta, campioni di Nyquist ([[Modulazione.pdf#page=12|p. 12]]–[[Modulazione.pdf#page=15|15]]); gradi di libertà $D=WT_0$ ([[Modulazione.pdf#page=16|p. 16]]–[[Modulazione.pdf#page=19|19]]); base ortonormale, coefficienti, conservazione del prodotto scalare ([[Modulazione.pdf#page=20|p. 20]]–[[Modulazione.pdf#page=22|22]]).
3. [[modulazione-lineare]] — $s(t)=\sum_k\xi_kg_{TX}(t-kT)$ ([[Modulazione.pdf#page=23|p. 23]]–[[Modulazione.pdf#page=25|25]]); codici di linea, NRZ, RZ ([[Modulazione.pdf#page=26|p. 26]]–[[Modulazione.pdf#page=29|29]]); I/Q in banda passante ([[Modulazione.pdf#page=30|p. 30]]); PSK e mapping di Gray ([[Modulazione.pdf#page=31|p. 31]], [[Modulazione.pdf#page=32|p. 32]]); QAM, PAM ([[Modulazione.pdf#page=33|p. 33]], [[Modulazione.pdf#page=34|p. 34]]); scelte di progetto ([[Modulazione.pdf#page=35|p. 35]]); PSD ([[Modulazione.pdf#page=36|p. 36]], [[Modulazione.pdf#page=37|p. 37]]).
4. [[modulazione-ortogonale]] — FSK, condizione di ortogonalità, spaziatura $1/(2T)$ e $1/T$ ([[Modulazione.pdf#page=38|p. 38]], [[Modulazione.pdf#page=39|p. 39]]).

## Lezione 9 — Elementi di teoria della rivelazione
**PDF:** [[Detection.pdf]] (copia GoodNotes: dispense della docente a p. 1 e 10–18, appunti a lezione a p. 2–9; primo caricamento 20/10) · **Fonte:** [[elementi-teoria-rivelazione]]

1. [[rivelazione-map-ml]] — modulazione on-off in AWGN, rumore bianco ([[Detection.pdf#page=1|p. 1]]–[[Detection.pdf#page=2|2]]); ipotesi, base ortonormale, proiezioni del rumore, test di ipotesi ([[Detection.pdf#page=10|p. 10]]–[[Detection.pdf#page=11|11]], [[Detection.pdf#page=3|p. 3]]); criterio MAP, irrilevanza, statistica sufficiente, verosimiglianza ([[Detection.pdf#page=12|p. 12]], [[Detection.pdf#page=4|p. 4]], [[Detection.pdf#page=5|p. 5]]); ML ([[Detection.pdf#page=13|p. 13]]); caso M-ario e Gram-Schmidt ([[Detection.pdf#page=14|p. 14]], [[Detection.pdf#page=6|p. 6]], [[Detection.pdf#page=7|p. 7]]).
2. [[ricevitore-ottimo-awgn]] — filtro adattato ([[Detection.pdf#page=13|p. 13]]); correlatori e filtri adattati ([[Detection.pdf#page=15|p. 15]], [[Detection.pdf#page=8|p. 8]]); segnali passa-banda ([[Detection.pdf#page=16|p. 16]]); minima distanza e regioni di Voronoi ([[Detection.pdf#page=17|p. 17]], [[Detection.pdf#page=18|p. 18]], [[Detection.pdf#page=9|p. 9]]).

## Lezione 10 — Prestazioni delle modulazioni binarie e della QPSK
**PDF:** [[Lezione 10-28.pdf]] (appunti a lezione del 28/10, 4 pagine) · **Fonte:** [[appunti-lezione-28-ottobre]]

1. [[probabilita-errore-binaria]] — on-off, regioni congruenti, Monte Carlo ([[Lezione 10-28.pdf#page=1|p. 1]]); antipodale, ortogonale, formula con la distanza, invarianza ed energia minima ([[Lezione 10-28.pdf#page=2|p. 2]]); modulazione binaria con coefficiente di correlazione ([[Lezione 10-28.pdf#page=3|p. 3]]).
2. [[probabilita-errore-m-aria]] — QPSK: base, inviluppo, ricevitore sui segni ([[Lezione 10-28.pdf#page=3|p. 3]]); SER via corretta decisione e BER con Gray ([[Lezione 10-28.pdf#page=4|p. 4]]).

## Lezione 11 — Union bound e approssimazione dei primi vicini
**PDF:** [[Lezione 11-2.pdf]] (appunti a lezione del 2/11, 3 pagine; p. 1 copertina) · **Fonte:** [[appunti-lezione-2-novembre]]

1. [[probabilita-errore-m-aria]] — union bound e pairwise error probability, primi vicini, 16-QAM, $M$ ortogonali ([[Lezione 11-2.pdf#page=2|p. 2]]); rimandi a figure ([[Lezione 11-2.pdf#page=3|p. 3]]).

## Lezione 12 — Parametri globali delle modulazioni e capacità di canale
**PDF:** [[Confronto_new.pdf]] (pp. 1–33, slide in inglese con note a mano della docente) · **Fonte:** [[parametri-globali-e-capacita]]

1. [[informazione-mutua-e-capacita]] — obiettivi e motivazione ([[Confronto_new.pdf#page=2|p. 2]], [[Confronto_new.pdf#page=3|3]]); informazione mutua, simmetria, indipendenza ([[Confronto_new.pdf#page=4|p. 4]]); legame con le entropie $I=H(Y)-H(Y\mid X)$ ([[Confronto_new.pdf#page=5|p. 5]]); capacità $C=\max_{p(x)}I$ ([[Confronto_new.pdf#page=6|p. 6]]); secondo teorema di Shannon ([[Confronto_new.pdf#page=7|p. 7]]); capacità AWGN $C=W\log_2(1+\gamma)$, da non dimostrare ([[Confronto_new.pdf#page=8|p. 8]]), e sua interpretazione: lineare in $W$, logaritmica in $\gamma$ ([[Confronto_new.pdf#page=9|p. 9]]).
2. [[parametri-globali-modulazioni]] — perché serve una banda «astratta» ([[Confronto_new.pdf#page=10|p. 10]]); banda di Shannon $W=N/(2T)$ ([[Confronto_new.pdf#page=11|p. 11]]); potenza ed energia per bit, eq. (1)–(3) ([[Confronto_new.pdf#page=12|p. 12]]); SNR $=\frac{E_b}{N_0}\eta_B$ ed efficienza spettrale $\eta_B=2\log_2M/N$ ([[Confronto_new.pdf#page=13|p. 13]], [[Confronto_new.pdf#page=14|14]]); efficienza in potenza $\eta_P$ con gli esempi OOK, antipodale, ortogonale ([[Confronto_new.pdf#page=15|p. 15]], [[Confronto_new.pdf#page=16|16]]); probabilità d'errore con l'approssimazione dei vicini, eq. (5)–(6) ([[Confronto_new.pdf#page=17|p. 17]]); parametri globali e compromesso ([[Confronto_new.pdf#page=18|p. 18]]); tabella PAM/PSK/QAM/ortogonali e compromesso energia-banda ([[Confronto_new.pdf#page=19|p. 19]]).
3. [[limite-di-shannon]] — dalla condizione $R_b\le C$ alla frontiera $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$ ([[Confronto_new.pdf#page=20|p. 20]]); limite $\ln2=-1.59$ dB ([[Confronto_new.pdf#page=21|p. 21]]); interpretazione fisica ([[Confronto_new.pdf#page=22|p. 22]]); piano efficienza spettrale – $E_b/N_0$ con le modulazioni reali, regioni limitate in banda e in potenza ([[Confronto_new.pdf#page=23|p. 23]]).
4. [[link-budget]] — elementi e procedura ([[Confronto_new.pdf#page=24|p. 24]]); potenza di rumore e sensibilità ([[Confronto_new.pdf#page=25|p. 25]]); equazione di Friis ([[Confronto_new.pdf#page=26|p. 26]]); path loss massimo in dB ([[Confronto_new.pdf#page=27|p. 27]]); osservazione sulle costellazioni dense e messaggio conclusivo ([[Confronto_new.pdf#page=32|p. 32]], [[Confronto_new.pdf#page=33|33]]).
5. [[link-budget-wlan]] (esercizio) — WLAN a 5 GHz con QPSK: bit rate, sensibilità, path loss e portata ([[Confronto_new.pdf#page=28|p. 28]]–[[Confronto_new.pdf#page=31|31]]).

## Lezione 13 — Stima dei parametri per la sincronizzazione
**PDF:** [[11-9.pdf]] (appunti del 9/11, 2 pagine) e [[Synchro_Kay_example (1).pdf]] (33 slide con 3 pagine di appunti; la copia senza «(1)» è la versione meno annotata) · **Fonte:** [[parameter-estimation-synchronization]]

1. [[sincronizzazione]] — perché sincronizzare ([[11-9.pdf#page=2|p. 2]]); effetto di ritardo e offset dell'LO, modello (1) ([[Synchro_Kay_example (1).pdf#page=2|p. 2]]–[[Synchro_Kay_example (1).pdf#page=4|4]]); derivazione del modello in banda base complessa ([[Synchro_Kay_example (1).pdf#page=5|p. 5]]–[[Synchro_Kay_example (1).pdf#page=9|9]]); timing e portante, acquisizione e tracking, decision-directed e blind ([[Synchro_Kay_example (1).pdf#page=10|p. 10]], [[Synchro_Kay_example (1).pdf#page=11|11]]); stima ML della fase, mismatch e Doppler, schema ([[Synchro_Kay_example (1).pdf#page=25|p. 25]]–[[Synchro_Kay_example (1).pdf#page=28|28]]).
2. [[stima-dei-parametri]] — problema e modello dei dati ([[Synchro_Kay_example (1).pdf#page=12|p. 12]], [[Synchro_Kay_example (1).pdf#page=13|13]]); livello DC nel rumore ([[Synchro_Kay_example (1).pdf#page=14|p. 14]]); classico e bayesiano ([[Synchro_Kay_example (1).pdf#page=15|p. 15]]); MLE e legame con la rivelazione ([[Synchro_Kay_example (1).pdf#page=16|p. 16]], [[Synchro_Kay_example (1).pdf#page=17|17]]); stima d'ampiezza: modello, training-based, blind, conclusioni ([[Synchro_Kay_example (1).pdf#page=18|p. 18]]–[[Synchro_Kay_example (1).pdf#page=23|23]]); rivelazione M-aria come stima ([[Synchro_Kay_example (1).pdf#page=24|p. 24]]).
3. [[phase-locked-loop]] — phase tracking, steepest ascent e gradient descent ([[Synchro_Kay_example (1).pdf#page=29|p. 29]], [[Synchro_Kay_example (1).pdf#page=30|30]]); PLL: modello, funzione costo, struttura, VCO, termine d'errore ([[Synchro_Kay_example (1).pdf#page=31|p. 31]]–[[Synchro_Kay_example (1).pdf#page=35|35]]); Costas loop ([[Synchro_Kay_example (1).pdf#page=36|p. 36]]).

## Lezione 14 — Segnalazione su canali a banda limitata
**PDF:** [[signaling_bandlimited_channel_NEW.pdf]] (versione aggiornata del 23/11: 59 slide più 2 pagine di appunti, con appunti a lezione) · appunti delle slide 2, 3, 9, 13, 14, 18 nella versione precedente [[signaling_bandlimited_channel.pdf]] · **Fonte:** [[signaling-bandlimited-channels]]

1. [[interferenza-intersimbolica]] — canale a banda limitata, ISI e rumore ([[signaling_bandlimited_channel_NEW.pdf#page=2|p. 2]], [[signaling_bandlimited_channel_NEW.pdf#page=3|3]]; appunti [[signaling_bandlimited_channel.pdf#page=2|p. 2]], [[signaling_bandlimited_channel.pdf#page=3|3]]); perdita di SNR e BER floor ([[signaling_bandlimited_channel_NEW.pdf#page=4|p. 4]]–[[signaling_bandlimited_channel_NEW.pdf#page=7|7]]); modulazione lineare e modello del sistema ([[signaling_bandlimited_channel_NEW.pdf#page=8|p. 8]], [[signaling_bandlimited_channel_NEW.pdf#page=9|9]]; appunti [[signaling_bandlimited_channel.pdf#page=9|p. 9]]); ISI, eq. (2)–(3) ([[signaling_bandlimited_channel_NEW.pdf#page=10|p. 10]]–[[signaling_bandlimited_channel_NEW.pdf#page=13|13]]; appunti [[signaling_bandlimited_channel.pdf#page=13|p. 13]]).
2. [[criterio-di-nyquist]] — signal design e criterio (4) ([[signaling_bandlimited_channel_NEW.pdf#page=14|p. 14]], [[signaling_bandlimited_channel_NEW.pdf#page=15|15]]; appunti [[signaling_bandlimited_channel.pdf#page=14|p. 14]]), con gli approcci al trattamento dell'ISI annotati il 19/11: Viterbi, equalizzatori, OFDM ([[signaling_bandlimited_channel (19-11).pdf#page=15|appunti p. 15]]); forma in frequenza (5)–(6) ([[signaling_bandlimited_channel_NEW.pdf#page=16|p. 16]], [[signaling_bandlimited_channel_NEW.pdf#page=17|17]]); impulso ideale e banda di Nyquist ([[signaling_bandlimited_channel_NEW.pdf#page=18|p. 18]]–[[signaling_bandlimited_channel_NEW.pdf#page=21|21]]; appunti [[signaling_bandlimited_channel.pdf#page=18|p. 18]]); difficoltà pratiche ed errore di timing ([[signaling_bandlimited_channel_NEW.pdf#page=22|p. 22]]–[[signaling_bandlimited_channel_NEW.pdf#page=24|24]]); coseno rialzato ([[signaling_bandlimited_channel_NEW.pdf#page=25|p. 25]]–[[signaling_bandlimited_channel_NEW.pdf#page=29|29]]); filtri a radice di Nyquist e a radice di coseno rialzato, RRC ([[signaling_bandlimited_channel_NEW.pdf#page=30|p. 30]], [[signaling_bandlimited_channel_NEW.pdf#page=31|31]]); efficienza di banda ([[signaling_bandlimited_channel_NEW.pdf#page=32|p. 32]]).
3. [[equalizzazione]] — limiti della condizione di ISI nulla ([[signaling_bandlimited_channel_NEW.pdf#page=33|p. 33]]); tipi di equalizzatori ([[signaling_bandlimited_channel_NEW.pdf#page=34|p. 34]], [[signaling_bandlimited_channel_NEW.pdf#page=35|35]]); equalizzazione a spaziatura frazionaria: sistema con filtri RRC, ISI con memoria finita $L$, perché sovracampionare ($S\ge L+1$), modello vettoriale ([[signaling_bandlimited_channel_NEW.pdf#page=36|p. 36]]–[[signaling_bandlimited_channel_NEW.pdf#page=41|41]], con la pagina di appunti [[signaling_bandlimited_channel_NEW.pdf#page=38|p. 38]]); equalizzatore zero-forcing a norma minima e amplificazione del rumore ([[signaling_bandlimited_channel_NEW.pdf#page=42|p. 42]], [[signaling_bandlimited_channel_NEW.pdf#page=43|43]]); equalizzatore MMSE ([[signaling_bandlimited_channel_NEW.pdf#page=44|p. 44]], [[signaling_bandlimited_channel_NEW.pdf#page=45|45]]); MLSE e suo criterio ([[signaling_bandlimited_channel_NEW.pdf#page=46|p. 46]]–[[signaling_bandlimited_channel_NEW.pdf#page=51|51]]); coefficienti $\beta(\ell)$ e memoria del canale, esempio rettangolare ([[signaling_bandlimited_channel_NEW.pdf#page=56|p. 56]], [[signaling_bandlimited_channel_NEW.pdf#page=57|57]]); applicazione del VA alla MLSE, (15)–(16) e ricorsione U/V ([[signaling_bandlimited_channel_NEW.pdf#page=58|p. 58]]–[[signaling_bandlimited_channel_NEW.pdf#page=61|61]], con la pagina di appunti [[signaling_bandlimited_channel_NEW.pdf#page=59|p. 59]]).
4. [[algoritmo-di-viterbi]] — traliccio, metriche, ACS ([[signaling_bandlimited_channel_NEW.pdf#page=52|p. 52]]–[[signaling_bandlimited_channel_NEW.pdf#page=55|55]]); complessità e latenza dagli appunti ([[signaling_bandlimited_channel_NEW.pdf#page=36|p. 36]]).

## Lezione 15 — Segnalazione su canali a banda limitata: OFDM
**PDF:** [[ofdm_goldsmith_slides.pdf]] (lezione del 27/11: 53 slide con appunti, più 5 pagine di soli appunti a p. 4, 9, 10, 13, 14) · **Fonte:** [[signaling-ofdm]] · **Approfondimento facoltativo:** [[multiportante-ofdm-dmt-gelli]] (non d'esame)

1. [[ofdm]] — perché multiportante; FDM: S/P, trasmettitore e ricevitore a banco di filtri ([[ofdm_goldsmith_slides.pdf#page=2|p. 2]]–[[ofdm_goldsmith_slides.pdf#page=3|3]], [[ofdm_goldsmith_slides.pdf#page=5|5]], [[ofdm_goldsmith_slides.pdf#page=6|6]]); S/P come decomposizione polifase, $T_u=NT_b$, rate più basso contro l'ISI, canale piatto per sottoportante (appunti [[ofdm_goldsmith_slides.pdf#page=4|p. 4]], [[ofdm_goldsmith_slides.pdf#page=9|9]], [[ofdm_goldsmith_slides.pdf#page=10|10]]); FDM e OFDM a confronto, frame multicanale ([[ofdm_goldsmith_slides.pdf#page=7|p. 7]], [[ofdm_goldsmith_slides.pdf#page=8|8]]); impulsi ortogonali, ISI e ICI, calcolo dell'ortogonalità e ruolo della FFT ([[ofdm_goldsmith_slides.pdf#page=11|p. 11]]–[[ofdm_goldsmith_slides.pdf#page=14|14]]); ortogonalità, condizione sinc e $\Delta f=1/T_u$ ([[ofdm_goldsmith_slides.pdf#page=15|p. 15]], [[ofdm_goldsmith_slides.pdf#page=16|16]]); banco di correlatori, AWGN, rumore i.i.d. ([[ofdm_goldsmith_slides.pdf#page=17|p. 17]]–[[ofdm_goldsmith_slides.pdf#page=19|19]]); autocorrelazione ciclostazionaria e PSD, risparmio di banda ([[ofdm_goldsmith_slides.pdf#page=20|p. 20]]–[[ofdm_goldsmith_slides.pdf#page=22|22]]).
2. [[prefisso-ciclico]] — canale dispersivo, guardia contro prefisso ciclico, estensione ciclica, condizione $T_g\ge T_h$, niente ISI ([[ofdm_goldsmith_slides.pdf#page=23|p. 23]]–[[ofdm_goldsmith_slides.pdf#page=28|28]]); autofunzioni LTI e niente ICI, normalizzazione su $T$ ([[ofdm_goldsmith_slides.pdf#page=29|p. 29]]–[[ofdm_goldsmith_slides.pdf#page=31|31]]); CP a tempo discreto, esempio $N=8$, convoluzione circolare, teorema e relazione $Y_n[k]=H[k]a_k[n]+W_n[k]$ ([[ofdm_goldsmith_slides.pdf#page=36|p. 36]]–[[ofdm_goldsmith_slides.pdf#page=40|40]]); prezzo del CP ed esempio di Goldsmith, bit rate ([[ofdm_goldsmith_slides.pdf#page=48|p. 48]]–[[ofdm_goldsmith_slides.pdf#page=50|50]]).
3. [[ofdm-con-fft]] — campionamento e IDFT, matrice DFT e Parseval, serializzazione ([[ofdm_goldsmith_slides.pdf#page=33|p. 33]]–[[ofdm_goldsmith_slides.pdf#page=35|35]]); trasmettitore e ricevitore completi ([[ofdm_goldsmith_slides.pdf#page=46|p. 46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]).
4. [[equalizzazione-ofdm]] — equalizzazione in frequenza ([[ofdm_goldsmith_slides.pdf#page=32|p. 32]]); matrice diagonale, esempio a due prese, nullo spettrale, ZF e MMSE a una presa, codifica e interleaving ([[ofdm_goldsmith_slides.pdf#page=41|p. 41]]–[[ofdm_goldsmith_slides.pdf#page=45|45]]); modulazione adattativa ([[ofdm_goldsmith_slides.pdf#page=53|p. 53]]).
5. [[limiti-dell-ofdm]] — PAPR e caso peggiore ([[ofdm_goldsmith_slides.pdf#page=54|p. 54]], [[ofdm_goldsmith_slides.pdf#page=55|55]]); offset di frequenza, modello discreto con $C_m(\epsilon_f)$, offset di tempo ([[ofdm_goldsmith_slides.pdf#page=56|p. 56]], [[ofdm_goldsmith_slides.pdf#page=57|57]]); scelta di $N$ ([[ofdm_goldsmith_slides.pdf#page=58|p. 58]]).
6. [[ieee-802-11a]] — parametri temporali e bit rate non codificati ([[ofdm_goldsmith_slides.pdf#page=51|p. 51]], [[ofdm_goldsmith_slides.pdf#page=52|52]]).
7. [[fft]] — FFT e IFFT come algoritmi veloci per DFT e IDFT ([[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=34|34]]).
8. [[dimensionamento-ofdm]] — esercizi: banda con sovrapposizione, CP di Goldsmith, 802.11a, scelta di $N$, nullo spettrale ([[ofdm_goldsmith_slides.pdf#page=22|p. 22]], [[ofdm_goldsmith_slides.pdf#page=43|43]], [[ofdm_goldsmith_slides.pdf#page=49|49]], [[ofdm_goldsmith_slides.pdf#page=51|51]], [[ofdm_goldsmith_slides.pdf#page=52|52]], [[ofdm_goldsmith_slides.pdf#page=58|58]]).

## Approfondimenti (non lezioni, non d'esame)

### Note di G. Gelli — Modulazione multiportante, sistemi OFDM e DMT
**PDF:** [[Note 2001 Gelli G.pdf]] (maggio 2001, 24 pagine; lettura facoltativa collegata alla Lezione 15) · **Fonte:** [[note-gelli-multiportante]] · **Pagina:** [[multiportante-ofdm-dmt-gelli]]

1. Introduzione: vantaggi, OFDM e DMT, svantaggi, applicazioni ([[Note 2001 Gelli G.pdf#page=1|p. 1]]–[[Note 2001 Gelli G.pdf#page=2|2]]).
2. Principio, biortogonalità, codificatore, spettro e banda ([[Note 2001 Gelli G.pdf#page=2|p. 2]]–[[Note 2001 Gelli G.pdf#page=7|7]]).
3. Prestazioni in AWGN: QAM a portante singola e multiportante ([[Note 2001 Gelli G.pdf#page=7|p. 7]]–[[Note 2001 Gelli G.pdf#page=10|10]]).
4. Canale e tempi di guardia ([[Note 2001 Gelli G.pdf#page=10|p. 10]]–[[Note 2001 Gelli G.pdf#page=13|13]]).
5. Realizzazione con FFT, rumore dopo la DFT, prefisso ciclico ([[Note 2001 Gelli G.pdf#page=13|p. 13]]–[[Note 2001 Gelli G.pdf#page=19|19]]).
6. Bit loading, SNR gap, water filling; riferimenti e indice ([[Note 2001 Gelli G.pdf#page=19|p. 19]]–[[Note 2001 Gelli G.pdf#page=24|24]]).

## Appunti sparsi — quaderno «Lezioni»
**PDF:** [[Lezioni.pdf]] (3 pagine, primo caricamento 14/09; non è una lezione) · **Fonte:** [[appunti-sparsi-lezioni]]

1. [[lab-setup-e-spettro]] — DFT come campionamento della DTFT ([[Lezioni.pdf#page=2|p. 2]]).
2. [[inviluppo-complesso]] — dimostrazione della (14) e ortogonalità di I e Q, ripasso della Lezione 4 ([[Lezioni.pdf#page=3|p. 3]]).

_Aggiornato: 2026-11-27 — aggiunta la Lezione 15 (ofdm_goldsmith_slides.pdf, OFDM) e la sezione «Approfondimenti» con le note di Gelli (non d'esame); 2026-11-23 — Lezione 14 rifatta sulla versione aggiornata delle slide (signaling_bandlimited_channel_NEW.pdf): RRC, equalizzazione frazionaria, ZF, MMSE, coefficienti β(ℓ), nuova numerazione delle pagine; 2026-11-16 — aggiunte Lezioni 13 (11-9 e Synchro) e 14 (signaling) e gli appunti sparsi di Lezioni.pdf; lezioni rinumerate secondo il primo caricamento su OneDrive (laboratorio 5, processi 6, Confronto 12); aggiunte Lezioni 8–11 (Modulazione, Detection, appunti del 28/10 e del 2/11); 2026-11-15 — aggiunta Lezione 8 (Confronto_new.pdf); 2026-11-01 — aggiunta Lezione 7 (Rappresentazione_Rice_processi.pdf); 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-10-11 — Lezione 3: aggiunti Chebyshev e la riga delle entità collegate; 2026-09-30 — aggiunta Lezione 6 (laboratorio Matlab, non d'esame); 2026-09-28 — re-ingest dei PDF con appunti a mano: argomenti e pagine delle Lezioni 4 e 5 aggiornati; aggiunta Lezione 5 (random_processes.pdf); 2026-09-25 — aggiunta Lezione 4 (Rappresentazione_Rice.pdf); 2026-09-24 — un punto per pagina del wiki: argomenti della stessa pagina raggruppati in un unico punto con sintesi; 2026-09-23 — creazione (3 lezioni, 1 PDF ciascuna)_
