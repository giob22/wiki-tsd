---
tipo: fonte
titolo: "Appunti sparsi (quaderno «Lezioni»)"
file_raw: "goodnotes/Lezioni.pdf"
pagine: "1-3"
data_ingest: 2026-11-16
formato: appunti
argomenti: ["DFT e DTFT", "segnale analitico", "trasformata di Hilbert", "inviluppo complesso", "ortogonalità delle componenti I e Q"]
---

# Appunti sparsi del quaderno «Lezioni»

## Sommario · [[Lezioni.pdf#page=2|p. 2]], [[Lezioni.pdf#page=3|3]]

Quaderno GoodNotes caricato per primo (14/09), usato per appunti fuori dalle slide. P. 1 è la copertina. P. 2 confronta DFT e trasformata a tempo discreto: la DFT è il campionamento della DTFT in $\nu=k/N$; l'ultima riga («la componente continua viene spezzata e spostata») è segnata come da capire. P. 3 ripassa la rappresentazione di Rice: segnale analitico nel tempo con la trasformata di Hilbert, $s_p=\sqrt2\,\text{Re}\{s_p^+\}$, spettro della trasformata di Hilbert, inviluppo complesso e relazione inversa (14), componenti in fase e quadratura e la loro ortogonalità con Parseval.

## Punti chiave · [[Lezioni.pdf#page=2|p. 2]], [[Lezioni.pdf#page=3|3]]

1. DFT di una sequenza lunga $N$ = DTFT campionata in $\nu=k/N$.
2. La relazione inversa (14) si dimostra con $\mathcal F\{x^\ast(t)\}=X^\ast(-f)$.
3. Ortogonalità di $x_c$ e $x_s$: i termini misti si annullano perché $2f_c>B$.

## Concetti introdotti

Nessuno nuovo: gli appunti completano [[segnale-analitico]], [[inviluppo-complesso]] e la pagina di laboratorio [[lab-setup-e-spettro]].

## Domande aperte

- Il dubbio di p. 2 sulla componente continua è chiarito in [[lab-setup-e-spettro]] (effetto di `fft` e `fftshift`).

## Domande da esame

- Che relazione c'è tra DFT e trasformata di Fourier a tempo discreto?
- Dimostrare la relazione tra spettro del segnale passa-banda e spettro dell'inviluppo complesso.

_Aggiornato: 2026-11-16 — creazione da ingest Lezioni.pdf_
