# Lezioni — Trasmissione dei Segnali Digitali

Elenco delle lezioni con gli argomenti del wiki. Per ogni lezione c'è **un punto per ogni pagina del wiki**, con una sintesi di cosa contiene e le pagine PDF da cui viene. I punti seguono l'ordine in cui l'argomento compare per la prima volta nel PDF.
Regola: 1 PDF = 1 lezione, salvo diversa indicazione (lezioni con più PDF vengono unite su richiesta).
Ordine delle lezioni ricavato dalla data di creazione dei PDF.

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
6. [[snr-di-quantizzazione]] — SNR di quantizzazione e legge dei 6 dB/bit; progetto di un quantizzatore audio, Esempio 7.6, svolto in [[dimensionamento-quantizzatore]] ([[Campionamento_AD_DA.pdf#page=30|p. 30]]–[[Campionamento_AD_DA.pdf#page=31|31]]).
7. [[quantizzazione-non-uniforme]] — limiti della quantizzazione uniforme e pdf di Laplace della voce; quantizzatore non uniforme; quantizzatore ottimo di Lloyd-Max ([[algoritmo-lloyd-max]]); limiti della quantizzazione ottima e quantizzazione robusta ([[Campionamento_AD_DA.pdf#page=32|p. 32]]–[[Campionamento_AD_DA.pdf#page=36|36]]).
8. [[companding]] — perché compressione + quantizzazione uniforme equivale a una quantizzazione non uniforme; analisi ad alta risoluzione; legge logaritmica; leggi [[legge-mu]] e [[legge-a]] (standard [[g711]]); prestazioni ([[Campionamento_AD_DA.pdf#page=36|p. 36]]–[[Campionamento_AD_DA.pdf#page=43|43]]).

Esercizi collegati: [[campionamento-e-aliasing]], [[dimensionamento-quantizzatore]]

---

## Lezione 4 — Rappresentazione complessa in banda base
**PDF:** [[Rappresentazione_Rice.pdf]] (pp. 1–23: 19 slide più 4 pagine di appunti a mano) · **Fonte:** [[rappresentazione-complessa-banda-base]]
Le pagine sotto sono quelle del PDF, non i numeri delle slide; la corrispondenza è nella pagina fonte.

1. [[modulazione-digitale]] — la catena sorgente → modulatore → canale; la modulazione come rappresentazione dei bit con forme d'onda analogiche; esempio di modulazione lineare binaria con impulsi rettangolari; le forme d'onda devono stare in una porzione di spettro ([[Rappresentazione_Rice.pdf#page=2|p. 2]]–[[Rappresentazione_Rice.pdf#page=3|3]]).
2. [[segnali-banda-base-e-passa-banda]] — definizioni di segnale e canale in banda base e in banda passante; simmetria hermitiana dei segnali reali; banda monolatera e bilatera; segnali a banda stretta ([[Rappresentazione_Rice.pdf#page=4|p. 4]]–[[Rappresentazione_Rice.pdf#page=7|7]]).
3. [[inviluppo-complesso]] — perché tutta l'informazione sta in un segnale complesso in banda base e perché conviene elaborarlo in digitale ([[Rappresentazione_Rice.pdf#page=8|p. 8]]–[[Rappresentazione_Rice.pdf#page=9|9]]). Poi la definizione dell'inviluppo, le componenti in fase e quadratura, il ritorno al passa-banda, l'ortogonalità di I e Q e la conservazione dell'energia ([[Rappresentazione_Rice.pdf#page=13|p. 13]]–[[Rappresentazione_Rice.pdf#page=16|16]]). Infine la banda di un segnale complesso ([[Rappresentazione_Rice.pdf#page=23|p. 23]]).
4. [[segnale-analitico]] — definizione con il $\sqrt2$, espressione nel tempo con la trasformata di Hilbert, ritorno al segnale reale, trasformata di Hilbert in frequenza ([[Rappresentazione_Rice.pdf#page=10|p. 10]]–[[Rappresentazione_Rice.pdf#page=12|12]]).
5. [[upconversion-e-downconversion]] — schemi con moltiplicatori e passa-basso; upconverter, canale e downconverter visti come un unico canale; la fase dovuta a $f_c$ non porta informazione ([[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]]).
6. [[equivalente-banda-base-dei-filtri]] — un filtro passa-banda in banda base complessa: $Y = SH/\sqrt2$, $y = s * h/\sqrt2$, realizzazione con quattro filtri reali ([[Rappresentazione_Rice.pdf#page=20|p. 20]]–[[Rappresentazione_Rice.pdf#page=22|22]]).

---

## Lezione 5 — Processi aleatori
**PDF:** [[random_processes.pdf]] (pp. 1–41) · **Fonte:** [[processi-aleatori]]

1. [[processo-aleatorio]] — il processo come estensione della variabile aleatoria ai segnali; i due punti di vista (forme d'onda e variabili aleatorie nel tempo); esempio del rettangolo di segno casuale; caratterizzazione completa con le distribuzioni congiunte di ordine $k$ ([[random_processes.pdf#page=2|p. 2]]–[[random_processes.pdf#page=6|6]]); processi a tempo discreto ([[random_processes.pdf#page=40|p. 40]]).
2. [[momenti-di-un-processo]] — media, autocorrelazione e autocovarianza ([[random_processes.pdf#page=7|p. 7]]–[[random_processes.pdf#page=9|9]]); mutue correlazioni e covarianze, processi indipendenti, incoerenti e incorrelati, processi complessi ([[random_processes.pdf#page=17|p. 17]]–[[random_processes.pdf#page=20|20]]); momenti a tempo discreto ([[random_processes.pdf#page=40|p. 40]]–[[random_processes.pdf#page=41|41]]).
3. [[stazionarieta]] — stazionarietà di ordine $k$, in senso stretto, del primo e del secondo ordine, in senso lato (WSS); SSS ⇒ WSS ([[random_processes.pdf#page=10|p. 10]]–[[random_processes.pdf#page=13|13]]).
4. [[autocorrelazione-processi-wss]] — lag-acf e sue proprietà, autocorrelazione normalizzata, significato fisico e tempo di decorrelazione ([[random_processes.pdf#page=14|p. 14]]–[[random_processes.pdf#page=16|16]]).
5. [[processi-e-sistemi-lti]] — media e correlazioni all'uscita di un filtro LTI; ingresso WSS ⇒ uscita WSS; l'incoerenza si conserva ([[random_processes.pdf#page=21|p. 21]]–[[random_processes.pdf#page=26|26]]); PSD dell'uscita ([[random_processes.pdf#page=28|p. 28]]).
6. [[densita-spettrale-di-potenza]] — definizione e Wiener-Khinchin ([[random_processes.pdf#page=27|p. 27]]); significato fisico, proprietà, densità spettrali mutue, PSD della somma di due processi ([[random_processes.pdf#page=29|p. 29]]–[[random_processes.pdf#page=35|35]]); PSD a tempo discreto ([[random_processes.pdf#page=41|p. 41]]).
7. [[processo-gaussiano]] — definizione, gaussiana multivariata, perché è così usato, proprietà ([[random_processes.pdf#page=36|p. 36]]–[[random_processes.pdf#page=39|39]]).

Esercizi collegati: [[calcolo-densita-spettrale]] (esempio della slide 32)

_Aggiornato: 2026-09-28 — aggiunta Lezione 5 (random_processes.pdf); 2026-09-25 — aggiunta Lezione 4 (Rappresentazione_Rice.pdf); 2026-09-24 — un punto per pagina del wiki: argomenti della stessa pagina raggruppati in un unico punto con sintesi; 2026-09-23 — creazione (3 lezioni, 1 PDF ciascuna)_
