---
tipo: fonte
titolo: "Parameter estimation for synchronization (con gli appunti del 9/11)"
file_raw: "goodnotes/Synchro_Kay_example (1).pdf; goodnotes/11-9.pdf"
pagine: "Synchro 1-36; 11-9 1-2"
data_ingest: 2026-11-16
formato: slide-pdf
argomenti: ["sincronizzazione di tempo e di portante", "modello con ritardo e offset dell'LO", "acquisizione e tracking", "decision-directed e blind", "stima classica e bayesiana", "stima ML", "stima d'ampiezza training-based e blind", "stima ML della fase", "steepest ascent", "PLL", "Costas loop"]
---

# Parameter estimation for synchronization (Lezione 13)

## Sommario · 11-9 [[11-9.pdf#page=2|p. 2]] · Synchro [[Synchro_Kay_example (1).pdf#page=2|p. 2]]–[[Synchro_Kay_example (1).pdf#page=36|36]]

Lezione del 9/11: una pagina di appunti (11-9.pdf, p. 2) e le 33 slide «Parameter estimation for synchronization» annotate a mano (Synchro_Kay_example (1).pdf, 36 pagine con 3 pagine di soli appunti alle p. 4, 7, 17). Il file `Synchro_Kay_example.pdf` (33 pagine, primo caricamento 09/11) è la versione meno annotata delle stesse slide; la copia «(1)», ricaricata il 15/11, contiene tutte le note e viene usata come fonte.

La lezione toglie l'ipotesi di sincronizzazione perfetta. Un canale non dispersivo scala e ritarda il segnale, e l'LO del ricevitore ha un offset $\Delta f$: l'inviluppo ricevuto è $Ae^{j(2\pi\Delta ft+\theta)}u(t-\tau)+n(t)$, ricavato passo per passo dalla down-conversion. Il ricevitore deve stimare $\tau$ (timing) e $\Delta f$, $\theta$ (portante), in acquisizione e in tracking (decision-directed o blind). Seguono i fondamenti della stima (famiglia di pdf, approccio classico e bayesiano, MLE), l'esempio della stima d'ampiezza training-based e blind (equazione con la tanh), la rivelazione M-aria come stima, la stima ML della fase ($\arg\langle y,s\rangle$), lo steepest ascent e il PLL, e infine il Costas loop.

## Punti chiave · Synchro [[Synchro_Kay_example (1).pdf#page=3|p. 3]], [[Synchro_Kay_example (1).pdf#page=10|10]], [[Synchro_Kay_example (1).pdf#page=16|16]], [[Synchro_Kay_example (1).pdf#page=20|20]]–[[Synchro_Kay_example (1).pdf#page=22|22]], [[Synchro_Kay_example (1).pdf#page=28|28]], [[Synchro_Kay_example (1).pdf#page=32|32]]

1. Il ritardo entra due volte: nell'inviluppo e nella fase $\theta=-2\pi f_c\tau$, molto sensibile perché $f_c\tau\gg1$.
2. Un LO a $f_c-\Delta f$ fa ruotare la costellazione di $2\pi\Delta ft$: un errore che cresce nel tempo.
3. Timing ⇒ $\hat\tau$; portante ⇒ $\widehat{\Delta f}$, $\hat\theta$. Acquisizione con training, tracking decision-directed o blind.
4. MLE: $\hat\theta=\arg\max_\theta\log f(\mathbf y;\theta)$; la rivelazione ML ne è il caso a $M$ valori.
5. Ampiezza: training $\hat A=\frac1K\sum y(k)b(k)$; blind $\hat A=\frac1K\sum y(k)\tanh(\hat Ay(k)/\sigma^2)$.
6. Fase: $\hat\theta=\arg\langle y,s\rangle=\tan^{-1}(Z_s/Z_c)$.
7. PLL: steepest ascent sulla log-verosimiglianza; errore $\frac{T_0}2\sin(\hat\theta_k-\theta_{k+1})$; Costas loop per segnali modulati in ampiezza.

## Concetti introdotti

- [[sincronizzazione]]
- [[stima-dei-parametri]]
- [[phase-locked-loop]]

## Domande aperte

- Il Costas loop (p. 36) è solo disegnato: le slide non spiegano perché funzioni. Nel wiki c'è una spiegazione mia ([[phase-locked-loop]]); conviene confrontarla con il libro di testo.
- La stima di $\tau$ e di $\Delta f$ non è trattata nelle slide (solo ampiezza e fase).
- La generalizzazione a simboli complessi della stima training-based è «lasciata al lettore» (p. 20).

## Domande da esame

- Ricavare il modello in banda base complessa con ritardo e offset dell'LO, partendo dalla down-conversion a $f_c-\Delta f$.
- Perché la fase $\theta$ è così sensibile al ritardo? Chi la compensa?
- Differenza tra acquisizione e tracking; tra modalità decision-directed e blind.
- Differenza tra approccio classico e bayesiano alla stima; definizione di MLE.
- Stimare l'ampiezza con e senza training: ricavare le due espressioni e commentarle.
- In che senso la rivelazione ML è un caso particolare della stima ML?
- Ricavare la stima ML della fase e disegnare lo schema a blocchi.
- Ricavare l'aggiornamento del PLL dallo steepest ascent e commentare il termine d'errore.

_Aggiornato: 2026-11-16 — creazione da ingest di 11-9.pdf e Synchro_Kay_example (1).pdf_
