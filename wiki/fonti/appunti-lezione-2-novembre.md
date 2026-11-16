---
tipo: fonte
titolo: "Appunti della lezione del 2/11"
file_raw: "goodnotes/Lezione 11-2.pdf"
pagine: "1-3"
data_ingest: 2026-11-16
formato: appunti
argomenti: ["union bound", "pairwise error probability", "approssimazione dei primi vicini", "16-QAM", "modulazione ortogonale M-aria"]
---

# Appunti della lezione del 2/11 (Lezione 11)

## Sommario · [[Lezione 11-2.pdf#page=2|p. 2]], [[Lezione 11-2.pdf#page=3|3]]

Tre pagine (primo caricamento 02/11; p. 1 è la copertina del quaderno). Per modulazioni più complesse introducono lo union bound, che maggiora la $P(e)$ con la somma delle pairwise error probability, e l'approssimazione dei primi vicini. Applicazioni: 16-QAM ($\bar N_{d_{min}}=3$, $E_s=\frac52d^2$, $P(e)\approx\frac32\text{erfc}\sqrt{\frac25E_b/N_0}$) e $M$ segnali ortogonali ($P(e)\le\frac{M-1}{2}\text{erfc}\sqrt{E_b\log_2M/(2N_0)}$). L'ultima pagina rimanda a due figure da vedere.

## Punti chiave · [[Lezione 11-2.pdf#page=2|p. 2]]

1. Union bound: $P(e)\le\frac{1}{2M}\sum_k\sum_{i\neq k}\text{erfc}\frac{d_{ik}}{2\sqrt{N_0}}$.
2. Primi vicini: $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\frac{d_{min}}{2\sqrt{N_0}}$.
3. 16-QAM: tre tipi di regioni congruenti; $d^2=\frac85E_b$.
4. Ortogonali: a $E_b$ fisso $P(e)$ diminuisce con $M$.

## Concetti introdotti

- [[probabilita-errore-m-aria]]

## Domande aperte

- p. 3: «vedi immagine nel $P(e)$ rispetto al contrasto di energia» e «vedi perché a basso SNR i vicini più lontani sono poco affidabili» rimandano a figure non presenti negli appunti (probabilmente del libro di testo).

## Domande da esame

- Ricavare lo union bound e spiegare cos'è la pairwise error probability.
- Enunciare l'approssimazione dei primi vicini e quando vale.
- Calcolare la $P(e)$ della 16-QAM in funzione di $E_b/N_0$.
- Maggiorare la $P(e)$ di $M$ segnali ortogonali e commentare l'effetto di $M$.

_Aggiornato: 2026-11-16 — creazione da ingest Lezione 11-2.pdf_
