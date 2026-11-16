---
tipo: fonte
titolo: "Elementi di teoria della rivelazione"
file_raw: "goodnotes/Detection.pdf"
pagine: "1-18"
data_ingest: 2026-11-16
formato: appunti
argomenti: ["modulazione on-off", "test di ipotesi", "criterio MAP", "criterio ML", "teorema dell'irrilevanza", "statistica sufficiente", "filtro adattato", "correlatore", "regioni di Voronoi"]
---

# Elementi di teoria della rivelazione (Lezione 9)

## Sommario · [[Detection.pdf#page=1|p. 1]]–[[Detection.pdf#page=18|18]]

Dispense della docente (10 pagine in italiano, p. 1 e p. 10–18 della copia GoodNotes; primo caricamento 20/10) con 8 pagine di appunti a lezione (p. 2–9) che ne svolgono i passaggi. Parte dalla modulazione on-off in AWGN e formula la rivelazione come test di ipotesi su vettori, proiettando $r(t)$ su una base ortonormale con $\psi_1=s/\lVert s\rVert$; le proiezioni del rumore bianco sono gaussiane indipendenti di varianza $N_0/2$. Minimizzando $P(e)$ ricava il criterio MAP, il teorema dell'irrilevanza, la statistica sufficiente e il rapporto di verosimiglianza; con simboli equiprobabili il criterio ML, realizzato con il filtro adattato. Generalizza al caso M-ario (Gram-Schmidt, banco di correlatori e di filtri adattati), ai segnali passa-banda tramite inviluppo complesso e dà l'interpretazione geometrica: ricevitore a minima distanza e regioni di Voronoi.

## Punti chiave · [[Detection.pdf#page=1|p. 1]]–[[Detection.pdf#page=18|18]]

1. Rumore bianco: $R_{nn}=\frac{N_0}{2}\delta(\tau)$, potenza infinita ma modello lecito perché il ricevitore filtra; $N_0=kT_0$.
2. Proiezioni del rumore: $n_i\sim\mathcal N(0,N_0/2)$, indipendenti.
3. MAP: $\Lambda(r)\gtrless q/p$; irrilevanza delle componenti fuori dallo spazio dei segnali; $r_1$ statistica sufficiente.
4. ML ($p=q$): non dipende da $N_0$; $\lambda_k=\langle r,s_k\rangle-\frac12E_{s,k}$.
5. Filtro adattato $h(t)=s(T-t)$ campionato in $T$.
6. Passa-banda: $\text{Re}\langle\tilde r,\tilde s_k\rangle-\frac12E_{s,k}$, rumore complesso bianco di PSD $N_0$.
7. ML = minima distanza; regioni di Voronoi.

## Concetti introdotti

- [[rivelazione-map-ml]]
- [[ricevitore-ottimo-awgn]]
- [[spazio-dei-segnali]] (Gram-Schmidt)

## Domande aperte

- Eq. (IV.2) delle dispense: manca il fattore $\frac12$ davanti a $\int(r-s_k)^2$ (corretto negli appunti e in [[ricevitore-ottimo-awgn]]).
- Le dispense rimandano a Benedetto-Biglieri per una trattazione rigorosa dell'espansione ortonormale dei processi.

## Domande da esame

- Formulare il problema della rivelazione per la modulazione on-off in AWGN.
- Mostrare che le proiezioni del rumore bianco su una base ortonormale sono gaussiane indipendenti.
- Ricavare il criterio MAP minimizzando la probabilità d'errore.
- Enunciare il teorema dell'irrilevanza e definire la statistica sufficiente.
- Differenza tra criterio MAP e ML; perché l'ML è il più usato.
- Disegnare il ricevitore ottimo a correlatori e a filtri adattati e dimostrarne l'equivalenza.
- Mostrare che il ricevitore ML in AWGN è a minima distanza; definire le regioni di Voronoi.

_Aggiornato: 2026-11-16 — creazione da ingest Detection.pdf_
