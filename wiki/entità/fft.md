---
tipo: entità
categoria: algoritmo
---

# FFT e IFFT

## Cos'è · [[ofdm_goldsmith_slides.pdf#page=33|p. 33]], [[ofdm_goldsmith_slides.pdf#page=34|34]]

La **FFT** (*fast Fourier transform*) e la **IFFT** sono algoritmi veloci per calcolare la DFT e la IDFT su $N$ punti in $O(N\log N)$ operazioni invece di $O(N^2)$. Non sono trasformate diverse dalla DFT/IDFT: danno lo stesso risultato, più in fretta (slide 29).

## Come si usa nel corso · [[ofdm_goldsmith_slides.pdf#page=6|p. 6]], [[ofdm_goldsmith_slides.pdf#page=14|14]], [[ofdm_goldsmith_slides.pdf#page=33|33]], [[ofdm_goldsmith_slides.pdf#page=46|46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]

- Nel trasmettitore [[ofdm]] la IFFT su $N$ punti genera gli $N$ campioni del blocco utile a partire dagli $N$ simboli in frequenza, al posto di $N$ oscillatori a tempo continuo.
- Nel ricevitore la FFT calcola le $N$ proiezioni sulle sottoportanti, al posto del banco di correlatori (o di filtri passa-banda della FDM).
- Gli appunti di p. 14: prima l'OFDM non era di uso pubblico perché servivano banchi di oscillatori molto precisi; la FFT ha risolto questi problemi, e oggi è alla base del 5G.
- 🧩 Ordine di grandezza: per $N=64$ (802.11a) una DFT diretta richiede $N^2=4096$ moltiplicazioni complesse, una FFT radice 2 circa $\frac N2\log_2N=192$.

## Concetti correlati

- [[ofdm-con-fft]] — dove compare la IDFT campionando il blocco.
- [[prefisso-ciclico]] — la DFT diagonalizza la convoluzione circolare.
- [[lab-setup-e-spettro]] — la DFT come campionamento della DTFT (laboratorio).

## Fonti · [[ofdm_goldsmith_slides.pdf#page=6|p. 6]], [[ofdm_goldsmith_slides.pdf#page=14|14]], [[ofdm_goldsmith_slides.pdf#page=33|33]], [[ofdm_goldsmith_slides.pdf#page=34|34]], [[ofdm_goldsmith_slides.pdf#page=46|46]], [[ofdm_goldsmith_slides.pdf#page=47|47]]

- [[signaling-ofdm]] — Lezione 15.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15)_
