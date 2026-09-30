---
tipo: fonte
titolo: "Stochastic processes (processi aleatori)"
file_raw: "random_processes.pdf"
pagine: "1-46"
data_ingest: 2026-09-28
formato: slide-pdf
argomenti: [processo aleatorio, realizzazioni, caratterizzazione completa e parziale, media, autocorrelazione, autocovarianza, stazionarietà, SSS, WSS, proprietà dell'autocorrelazione, tempo di decorrelazione, mutua correlazione, processi incoerenti e incorrelati, processi complessi, sistemi LTI, densità spettrale di potenza, Wiener-Khinchin, densità spettrale mutua, processo gaussiano, processi a tempo discreto]
---

# Stochastic processes — random_processes.pdf

## Sommario

Slide in inglese intitolate *Stochastic processes*, del corso "Trasmissione dei segnali digitali" (Laurea Magistrale in Ingegneria Informatica, Università di Napoli Federico II), docente Donatella Darsena, a.a. 2026-27 ([[random_processes.pdf#page=1]]). Coprono il secondo tema del programma. Nella versione aggiornata (2026-09-28) il PDF ha 46 pagine: 41 slide più 5 pagine di appunti a mano (p. 3, 4, 5, 8, 10) e un'annotazione sulla slide 5 (p. 9). Slide 1–2 = p. 1–2, slide 3–4 = p. 6–7, slide 5 = p. 9, dalla slide 6 in poi pagina = slide + 5.

Il processo aleatorio è introdotto come estensione della variabile aleatoria ai segnali. Si può vedere come insieme di forme d'onda, una per esito, oppure come famiglia di variabili aleatorie indicizzate dal tempo. La descrizione completa (distribuzioni congiunte di ogni ordine) lascia il posto a quella parziale: media, autocorrelazione, autocovarianza. Poi vengono definite le forme di stazionarietà (di ordine $k$, in senso stretto, del primo e del secondo ordine, in senso lato) e studiate le proprietà dell'autocorrelazione dei processi WSS. Seguono le correlazioni tra due processi e i processi complessi, e la propagazione di media e correlazioni attraverso i filtri LTI. La parte centrale è la **densità spettrale di potenza**: definizione, relazione di Wiener-Khinchin, significato fisico, proprietà, densità mutue, PSD di una somma. Chiudono il **processo gaussiano** e i processi a tempo discreto.

## Punti chiave

1. Processo aleatorio $X(t, \omega)$: fissato $\omega_i$ è una forma d'onda $x_i(t)$, fissato $t_0$ è una variabile aleatoria, fissati entrambi è un numero. Esempi: $\pm A\,\text{rect}$ con probabilità $q$ e $p$ (slide); sinusoide a fase casuale $A\cos(2\pi f_0 t + \Theta)$, $\Theta \sim \mathcal{U}(0, 2\pi)$ (appunti) ([[random_processes.pdf#page=2]] – [[random_processes.pdf#page=7]]).
2. Caratterizzazione completa: CDF/pdf congiunte di ordine $k$ per ogni $k$ e ogni scelta di istanti, coerenti tra loro (le marginali danno gli ordini più bassi). Con ampiezza discreta si usa la DF: processo di Bernoulli, $p^x q^{1-x}$ al primo ordine. È difficile da ottenere, quindi si usa la caratterizzazione parziale ([[random_processes.pdf#page=8]] – [[random_processes.pdf#page=11]]).
3. Media $\mu_X(t)$, autocorrelazione $R_{XX}(t_1, t_2)$ e autocovarianza $C_{XX} = R_{XX} - \mu\mu$ ([[random_processes.pdf#page=12]] – [[random_processes.pdf#page=14]]).
4. Stazionarietà di ordine $k$ (6), SSS, del primo ordine (media costante), del secondo ordine ($R$ dipende da $t_1 - t_2$), WSS; SSS ⇒ WSS ([[random_processes.pdf#page=15]] – [[random_processes.pdf#page=18]]).
5. Lag-acf $R_{XX}(\tau) = E[X(t)X(t-\tau)]$: $R(0) = E[X^2]$, è pari, $|R(\tau)| \le R(0)$. Normalizzata $\rho_{XX}$; tempo di decorrelazione ([[random_processes.pdf#page=19]] – [[random_processes.pdf#page=21]]).
6. Mutue correlazioni e covarianze, con $R_{XY}(\tau) = R_{YX}(-\tau)$; processi indipendenti ⇒ incorrelati; con media nulla, incoerenti ⇔ incorrelati ([[random_processes.pdf#page=22]] – [[random_processes.pdf#page=24]]).
7. Processi complessi: $\mu_Z = \mu_X + j\mu_Y$ e $R_{ZZ} = E[Z(t_1)Z^*(t_2)]$ ([[random_processes.pdf#page=25]]).
8. Filtro LTI: $\mu_Y = \mu_X * h$, che per ingresso WSS diventa $\mu_X H(0)$; $R_{Y_1Y_2} = R_{X_1X_2} * h_1(\tau) * h_2(-\tau)$; ingresso WSS ⇒ uscita WSS; l'incoerenza si conserva ([[random_processes.pdf#page=26]] – [[random_processes.pdf#page=31]]).
9. PSD $S_{XX}(f) = \lim\frac{1}{2T}E|X_T(f)|^2 = \mathcal{F}[R_{XX}]$ (Wiener-Khinchin); $P_X = \int S_{XX}\,df$; $S_{YY} = S_{XX}|H|^2$ ([[random_processes.pdf#page=32]], [[random_processes.pdf#page=33]]).
10. Significato fisico: $\Delta P_X \approx 2\Delta f\,S_{XX}(f)$, [W/Hz]. Proprietà 1–5 ([[random_processes.pdf#page=34]] – [[random_processes.pdf#page=37]]).
11. Densità spettrali mutue: $S_{XY} = S_{YX}(-f) = S_{YX}^*(f)$. La PSD di una somma di processi incoerenti è la somma delle PSD ([[random_processes.pdf#page=38]] – [[random_processes.pdf#page=40]]).
12. Processo gaussiano: pdf multivariata (33); resta gaussiano attraverso filtri stabili; WSS ⇒ SSS; incorrelati ⇒ indipendenti ([[random_processes.pdf#page=41]] – [[random_processes.pdf#page=44]]).
13. Tempo discreto: $X(n)$, momenti (35)–(37), PSD con DTFT e Wiener-Khinchin discreto ([[random_processes.pdf#page=45]], [[random_processes.pdf#page=46]]).

## Concetti introdotti

- [[processo-aleatorio]]
- [[momenti-di-un-processo]]
- [[stazionarieta]]
- [[autocorrelazione-processi-wss]]
- [[processi-e-sistemi-lti]]
- [[densita-spettrale-di-potenza]]
- [[processo-gaussiano]]

Esercizi: [[calcolo-densita-spettrale]] (esempio della slide 32).
Grafici 🧩 in `output/grafici/` (script `genera_grafici_random_processes.py`): realizzazioni e v.a. a $t_0$, processo lento contro veloce (autocorrelazione e PSD), animazione della costruzione di $R_{XX}(\tau)$, gaussiana bivariata.

## Figure estratte

6 immagini in `raw/assets/random-processes-pN-*.png`: esempio del rettangolo (p.2), realizzazioni (p.7), autocorrelazioni lenta e veloce (p.21), filtro LTI (p.26), due sistemi LTI (p.29), filtro a banda stretta (p.35); in più le pagine di appunti p.3, 4, 8, 9, 10.

## Appunti a mano

Cosa aggiungono alle slide, nella versione del PDF aggiornata il 2026-09-28. Pagine intere di appunti in **grassetto**.

| Pagina | Contenuto | Dove nel wiki |
|---|---|---|
| **[[random_processes.pdf#page=3]]** | segnali deterministici (descrizione analitica, grafico); v.a. $X: \omega \to X(\omega) \in \mathbb{R}$; nel processo a ogni esito si associa una funzione del tempo $S(\omega_i, t)$ | [[processo-aleatorio]] |
| **[[random_processes.pdf#page=4]]** | sinusoide $A\cos(2\pi f_0 t + \Theta)$, $\Theta \sim \mathcal{U}(0, 2\pi)$; $X(t, \omega)$ «si particolarizza» fissando $\omega$ (segnale), $t$ (v.a.) o entrambi (numero); i «due punti di vista», il secondo lasciato in bianco | [[processo-aleatorio]], [[momenti-di-un-processo]], [[stazionarieta]] |
| **[[random_processes.pdf#page=5]]** | $X(t, \omega)$, $t \in \mathbb{R}$: tempo continuo; $X(n, \omega)$, $n \in \mathbb{Z}$: tempo discreto; la sinusoide è un «segnale aleatorio ad ampiezza continua» | [[processo-aleatorio]] |
| **[[random_processes.pdf#page=8]]** | CDF del primo ordine $F_{X(t_1)}(x)$ per ogni $t_1$; CDF congiunta del secondo ordine per ogni $t_1, t_2$ | [[processo-aleatorio]] |
| [[random_processes.pdf#page=9]] | correzione $\partial^n \to \partial^k$ nella (2); marginale $\int f_{X(t_1)X(t_2)}\,dx_2 = f_{X(t_1)}$, «ottengo la pdf di primo ordine»; nota poco leggibile sulla marginalizzazione | [[processo-aleatorio]] |
| **[[random_processes.pdf#page=10]]** | DF del processo di Bernoulli: $p^x q^{1-x}$ al primo ordine, $p^{w(\mathbf{x})}q^{2 - w(\mathbf{x})}$ al secondo con lanci indipendenti | [[processo-aleatorio]] |

Le slide da p.11 in poi non hanno note scritte.

## Refusi rilevati

> ⚠️ [[random_processes.pdf#page=9]]: nella (2) la derivata è $\partial^n$ invece di $\partial^k$ (corretta a mano nella versione aggiornata); la slide rimanda alla «joint CDF (36)» invece che alla (1).
> ⚠️ Appunti: $\forall t_1 \in \mathbb{Z}$ per un processo a tempo continuo (p.8), da leggere $t_1 \in \mathbb{R}$.
> ⚠️ [[random_processes.pdf#page=45]]: nella (36) la pdf è scritta $f_{X(n),Y(k)}(x, x)$ invece di $(x, y)$.
> ⚠️ Inglese: «LTI processing saves incoherence» (p.30) va letto «preserva l'incoerenza»; «dependance» (p.45). Le slide 40–41 hanno ancora l'intestazione di sezione «Gaussian process».

## Domande aperte

- Nota sotto la marginale, [[random_processes.pdf#page=9]]: si legge «non si dice marginalizzazione», ma l'operazione è proprio la marginalizzazione delle slide ([[random_processes.pdf#page=11]]). Da verificare cosa volesse dire ([[processo-aleatorio]]).
- Media e autocorrelazione della sinusoide a fase casuale degli appunti non sono calcolate a lezione: calcolate nel wiki ($\mu_X = 0$, $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$, processo WSS) in [[momenti-di-un-processo]].
- Wiener-Khinchin è solo enunciato («it can be proven», [[random_processes.pdf#page=32]]): dimostrato nel wiki sotto l'ipotesi di autocorrelazione assolutamente integrabile ([[densita-spettrale-di-potenza]]).
- La conservazione della gaussianità attraverso un filtro ([[random_processes.pdf#page=44]]) è data senza dimostrazione: nel wiki c'è l'idea, con il rimando a una proprietà standard della gaussiana multivariata (📚).
- Esempio della slide 32 (PSD di un segnale modulato linearmente): svolto nel wiki con ipotesi mie (simboli a media nulla e incorrelati, ritardo casuale uniforme). Da confrontare con lo svolgimento fatto a lezione.
- Il rumore termico è citato come esempio di segnale aleatorio ([[random_processes.pdf#page=2]]), ma il suo modello quantitativo (PSD, gaussianità) non è in queste slide: resta TODO in [[sistema-comunicazione-digitale]].
- $r_{h_1h_2}(\tau)$ è usata a p.30 senza definizione: nel wiki è $h_1(\tau) * h_2(-\tau)$, la mutua correlazione deterministica delle risposte impulsive.

## Domande da esame

- Definire un processo aleatorio: i due punti di vista, le realizzazioni, la variabile aleatoria a istante fissato. Applicarli alla sinusoide a fase casuale.
- Caratterizzazione completa e parziale; distribuzioni di ordine $k$ e loro coerenza; DF del processo di Bernoulli.
- Media, autocorrelazione e autocovarianza; ricavare $C = R - \mu\mu$.
- Stazionarietà: ordine $k$, SSS, primo e secondo ordine, WSS; SSS ⇒ WSS.
- Proprietà dell'autocorrelazione di un processo WSS, con dimostrazione; tempo di decorrelazione.
- Mutue correlazioni; processi indipendenti, incoerenti, incorrelati.
- Media e autocorrelazione dell'uscita di un filtro LTI; ingresso WSS ⇒ uscita WSS.
- PSD: definizione, Wiener-Khinchin (con dimostrazione), $S_{YY} = S_{XX}|H|^2$, significato fisico, proprietà.
- PSD della somma di due processi; ruolo dell'incoerenza.
- Processo gaussiano: pdf multivariata e proprietà.
- PSD di un segnale modulato linearmente.

_Aggiornato: 2026-09-28 — re-ingest della versione con appunti a mano (46 pagine): sezione "Appunti a mano", punti chiave 1–2, domande aperte, revisione di copertura. Prima, nello stesso giorno: ingest iniziale e revisione di copertura totale vs PDF_
