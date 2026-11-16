---
tipo: fonte
titolo: "Principles of modulation"
file_raw: "goodnotes/Modulazione.pdf"
pagine: "1-39"
data_ingest: 2026-11-16
formato: slide-pdf
argomenti: ["modulatore digitale", "baud rate", "compromesso potenza-banda", "spazio dei segnali", "modulazione lineare", "PSK", "QAM", "PAM", "mapping di Gray", "PSD", "FSK"]
---

# Principles of modulation (Lezione 8)

## Sommario · [[Modulazione.pdf#page=1|p. 1]]–[[Modulazione.pdf#page=39|39]]

23 slide in inglese con 16 pagine di appunti presi a lezione (copia GoodNotes, 39 pagine; primo caricamento 16/10). La lezione descrive il modulatore digitale (mapper e generatore di forme d'onda, bit rate «raw», baud rate $R_s=R_b/\log_2M$, modulazione con e senza memoria) e, con l'esempio di Benedetto-Biglieri, il compromesso tra banda, potenza e complessità. Introduce la rappresentazione discreta dei segnali: campioni di Nyquist, gradi di libertà $D=WT_0$, base ortonormale e conservazione dei prodotti scalari (spazio dei segnali). Poi la modulazione lineare $s(t)=\sum_k\xi_kg_{TX}(t-kT)$: codici di linea NRZ/RZ in banda base, I/Q in banda passante, PSK, QAM, PAM con mapping di Gray, PSD $\frac{E[|\xi|^2]}{T}|G_{TX}(f)|^2$. Chiude con la modulazione ortogonale FSK e la spaziatura minima dei toni.

## Punti chiave · [[Modulazione.pdf#page=2|p. 2]]–[[Modulazione.pdf#page=39|39]]

1. Modulatore = mapper + generatore; $T=hT_b$, $R_s=R_b/\log_2M$.
2. Aumentare $M$ riduce la banda ma, a potenza fissa, avvicina i livelli: compromesso potenza-banda; la memoria smussa le transizioni e stringe lo spettro.
3. Le forme d'onda si rappresentano con vettori su una base ortonormale; prodotti scalari e distanze si conservano.
4. $D=WT_0$ gradi di libertà complessi offerti dal canale; la costellazione ne usa $n\le M$.
5. Modulazione lineare: NRZ, RZ (unidimensionali); PSK a modulo costante; QAM a griglia; PAM $a_i=(2i-1-M)\frac d2$; mapping di Gray.
6. PSD con simboli i.i.d. a media nulla: forma di $|G_{TX}(f)|^2$.
7. FSK ortogonale: spaziatura $\frac{1}{2T}$ coerente, $\frac1T$ non coerente.

## Concetti introdotti

- [[principi-di-modulazione]]
- [[spazio-dei-segnali]]
- [[modulazione-lineare]]
- [[modulazione-ortogonale]]

## Domande aperte

- Slide 23: la soluzione dell'esercizio 2.25 del Madhow non è svolta; nel wiki è ricostruita ([[modulazione-ortogonale]]).
- Slide 22: la condizione di ortogonalità per i sistemi non coerenti è solo citata in nota.

## Domande da esame

- Descrivere la struttura del modulatore digitale e definire bit rate e baud rate.
- Illustrare il compromesso potenza-banda con l'esempio $M=2,4,8$.
- Perché si rappresentano le forme d'onda con vettori? Cosa sono i gradi di libertà $D=WT_0$?
- Dimostrare che il prodotto scalare si conserva passando dai segnali ai vettori.
- Definire la modulazione lineare; descrivere NRZ, RZ, PSK, QAM, PAM e il mapping di Gray.
- Scrivere la PSD di un segnale modulato linearmente e commentarla.
- Definire la modulazione ortogonale FSK e ricavare la spaziatura minima tra i toni.

_Aggiornato: 2026-11-16 — creazione da ingest Modulazione.pdf_
