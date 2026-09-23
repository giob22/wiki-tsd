# Lezioni — Trasmissione dei Segnali Digitali

Elenco delle lezioni con gli argomenti del wiki, **nell'ordine in cui compaiono nei PDF**.
Regola: 1 PDF = 1 lezione, salvo diversa indicazione (lezioni con più PDF vengono unite su richiesta).
Ordine delle lezioni ricavato dalla data di creazione dei PDF.

---

## Lezione 1 — Introduzione al corso
**PDF:** [[Intro.pdf]] (pp. 1–21) · **Fonte:** [[intro-corso]]

1. Organizzazione del corso: docente, testo, esame orale → [[intro-corso]] ([[Intro.pdf#page=2]])
2. Programma del corso → [[intro-corso]] ([[Intro.pdf#page=3]])
3. Definizione di comunicazione → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=4]])
4. Processo di comunicazione → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=5]])
5. Elementi di un sistema: trasmettitore, canale, ricevitore → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=6]] – [[Intro.pdf#page=9]])
6. Comunicazione digitale vs analogica → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=10]])
7. Degradazione e rigenerazione degli impulsi → [[ripetitore-rigenerativo]] ([[Intro.pdf#page=11]], [[Intro.pdf#page=12]])
8. Altri vantaggi dei circuiti digitali → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=13]])
9. Schema a blocchi del sistema digitale → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=14]])
10. Codificatore di sorgente (e bit rate tipici) → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=15]])
11. Codificatore di canale e modulatore → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=16]])
12. Canale → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=17]])
13. Rumore termico → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=18]])
14. Demodulatore e decodificatore di canale → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=19]])
15. Decodificatore di sorgente → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=20]])
16. Vantaggi dell'approccio digitale, principio di separazione, comunicazioni semantiche → [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=21]])

---

## Lezione 2 — Elementi di teoria della probabilità
**PDF:** [[Probabilità.pdf]] (pp. 1–38) · **Fonte:** [[elementi-teoria-probabilita]]

1. Esperimento aleatorio, spazio campione, eventi → [[spazio-di-probabilita]] ([[Probabilità.pdf#page=2]] – [[Probabilità.pdf#page=4]])
2. Spazio degli eventi e assiomi di Kolmogorov → [[spazio-di-probabilita]] ([[Probabilità.pdf#page=5]])
3. Proprietà elementari della probabilità → [[spazio-di-probabilita]] ([[Probabilità.pdf#page=6]])
4. Probabilità condizionale → [[probabilita-condizionale]] ([[Probabilità.pdf#page=7]], [[Probabilità.pdf#page=8]])
5. Legge della probabilità composta → [[probabilita-condizionale]] ([[Probabilità.pdf#page=9]])
6. Regola della catena → [[probabilita-condizionale]] ([[Probabilità.pdf#page=10]])
7. Indipendenza tra eventi → [[probabilita-condizionale]] ([[Probabilità.pdf#page=11]], [[Probabilità.pdf#page=12]])
8. Teorema della probabilità totale → [[probabilita-totale-e-bayes]] ([[Probabilità.pdf#page=13]])
9. Teorema di Bayes → [[probabilita-totale-e-bayes]] ([[Probabilità.pdf#page=14]])
10. Variabile aleatoria → [[variabile-aleatoria]] ([[Probabilità.pdf#page=15]])
11. CDF; v.a. discrete, continue, miste → [[variabile-aleatoria]] ([[Probabilità.pdf#page=16]], [[Probabilità.pdf#page=17]])
12. pdf → [[variabile-aleatoria]] ([[Probabilità.pdf#page=18]])
13. DF (pmf) → [[variabile-aleatoria]] ([[Probabilità.pdf#page=19]])
14. V.a. di Bernoulli → [[variabili-aleatorie-notevoli]] ([[Probabilità.pdf#page=20]])
15. V.a. Binomiale → [[variabili-aleatorie-notevoli]] ([[Probabilità.pdf#page=21]])
16. V.a. Uniforme → [[variabili-aleatorie-notevoli]] ([[Probabilità.pdf#page=22]])
17. V.a. Gaussiana → [[variabile-aleatoria-gaussiana]] ([[Probabilità.pdf#page=23]])
18. CDF gaussiana, erf, erfc, funzione Q, Matlab → [[variabile-aleatoria-gaussiana]] ([[Probabilità.pdf#page=24]] – [[Probabilità.pdf#page=26]])
19. Funzione di una variabile aleatoria → [[funzione-di-variabile-aleatoria]] ([[Probabilità.pdf#page=27]])
20. Media statistica, momenti, teorema fondamentale della media → [[media-e-varianza]] ([[Probabilità.pdf#page=28]])
21. Varianza e deviazione standard → [[media-e-varianza]] ([[Probabilità.pdf#page=29]])
22. Proprietà di media e varianza → [[media-e-varianza]] ([[Probabilità.pdf#page=30]])
23. Coppie di v.a.: CDF e pdf congiunte, marginali → [[coppie-di-variabili-aleatorie]] ([[Probabilità.pdf#page=31]] – [[Probabilità.pdf#page=33]])
24. Distribuzioni condizionali → [[coppie-di-variabili-aleatorie]] ([[Probabilità.pdf#page=34]])
25. Indipendenza statistica di v.a. → [[coppie-di-variabili-aleatorie]] ([[Probabilità.pdf#page=35]])
26. Teorema fondamentale della media per coppie → [[correlazione-e-covarianza]] ([[Probabilità.pdf#page=36]])
27. Correlazione, covarianza, coefficiente di correlazione → [[correlazione-e-covarianza]] ([[Probabilità.pdf#page=37]])
28. Proprietà di correlazione e covarianza, disuguaglianza di Schwarz → [[correlazione-e-covarianza]] ([[Probabilità.pdf#page=38]])

Esercizi collegati: [[calcolo-probabilita-eventi]], [[cdf-pdf-variabili-notevoli]]

---

## Lezione 3 — Campionamento e conversione A/D e D/A
**PDF:** [[Campionamento_AD_DA.pdf]] (pp. 1–43) · **Fonte:** [[campionamento-conversione-ad-da]]

1. Dall'elaborazione analogica a quella digitale; tecnologie e vantaggi → [[conversione-ad-da]] ([[Campionamento_AD_DA.pdf#page=2]] – [[Campionamento_AD_DA.pdf#page=4]])
2. Conversione A/D: campionamento + quantizzazione → [[conversione-ad-da]] ([[Campionamento_AD_DA.pdf#page=5]])
3. Conversione D/A: interpolazione → [[conversione-ad-da]] ([[Campionamento_AD_DA.pdf#page=6]])
4. Campionamento uniforme e scelta di $f_c$ → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=7]] – [[Campionamento_AD_DA.pdf#page=9]])
5. Invertibilità del campionamento → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=10]])
6. Campionamento ideale e spettro del segnale campionato → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=11]], [[Campionamento_AD_DA.pdf#page=12]])
7. I tre casi e teorema di Shannon → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=13]], [[Campionamento_AD_DA.pdf#page=14]])
8. Ricostruzione con LPF ideale → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=15]])
9. Effetti pratici, sovracampionamento → [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=16]])
10. Interpolazione ideale (serie di Shannon) → [[interpolazione]] ([[Campionamento_AD_DA.pdf#page=17]])
11. Aliasing → [[aliasing]] ([[Campionamento_AD_DA.pdf#page=18]])
12. Segnali a banda praticamente limitata → [[aliasing]] ([[Campionamento_AD_DA.pdf#page=19]], [[Campionamento_AD_DA.pdf#page=20]])
13. Filtraggio antialiasing → [[aliasing]] ([[Campionamento_AD_DA.pdf#page=21]])
14. Interpolazione non ideale in frequenza → [[interpolazione]] ([[Campionamento_AD_DA.pdf#page=22]])
15. Zero-Order Hold → [[interpolazione]] ([[Campionamento_AD_DA.pdf#page=23]])
16. First-Order Hold → [[interpolazione]] ([[Campionamento_AD_DA.pdf#page=24]])
17. Quantizzazione e quantizzatore uniforme → [[quantizzazione-uniforme]] ([[Campionamento_AD_DA.pdf#page=25]], [[Campionamento_AD_DA.pdf#page=26]])
18. Codifica binaria → [[quantizzazione-uniforme]] ([[Campionamento_AD_DA.pdf#page=27]])
19. Errore di quantizzazione, regione granulare e di sovraccarico → [[quantizzazione-uniforme]] ([[Campionamento_AD_DA.pdf#page=28]])
20. Fattore di carico e disuguaglianza di Chebyshev → [[quantizzazione-uniforme]], [[disuguaglianza-di-chebyshev]] ([[Campionamento_AD_DA.pdf#page=29]])
21. SNR di quantizzazione, legge dei 6 dB/bit → [[snr-di-quantizzazione]] ([[Campionamento_AD_DA.pdf#page=30]])
22. Progetto di un quantizzatore (Esempio 7.6) → [[snr-di-quantizzazione]], [[dimensionamento-quantizzatore]] ([[Campionamento_AD_DA.pdf#page=31]])
23. Limiti della quantizzazione uniforme, pdf di Laplace → [[quantizzazione-non-uniforme]] ([[Campionamento_AD_DA.pdf#page=32]])
24. Quantizzazione non uniforme → [[quantizzazione-non-uniforme]] ([[Campionamento_AD_DA.pdf#page=33]])
25. Quantizzatore ottimo di Lloyd-Max → [[quantizzazione-non-uniforme]], [[algoritmo-lloyd-max]] ([[Campionamento_AD_DA.pdf#page=34]], [[Campionamento_AD_DA.pdf#page=35]])
26. Limiti della quantizzazione ottima, quantizzazione robusta → [[quantizzazione-non-uniforme]] ([[Campionamento_AD_DA.pdf#page=36]])
27. Analisi del companding → [[companding]] ([[Campionamento_AD_DA.pdf#page=37]] – [[Campionamento_AD_DA.pdf#page=39]])
28. Companding logaritmico → [[companding]] ([[Campionamento_AD_DA.pdf#page=40]])
29. Legge µ → [[legge-mu]], [[g711]] ([[Campionamento_AD_DA.pdf#page=41]])
30. Legge A → [[legge-a]], [[g711]] ([[Campionamento_AD_DA.pdf#page=42]])
31. Prestazioni del companding logaritmico → [[companding]] ([[Campionamento_AD_DA.pdf#page=43]])

Esercizi collegati: [[campionamento-e-aliasing]], [[dimensionamento-quantizzatore]]

_Aggiornato: 2026-09-23 — creazione (3 lezioni, 1 PDF ciascuna)_
