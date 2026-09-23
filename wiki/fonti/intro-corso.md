---
tipo: fonte
titolo: "Introduzione al corso"
file_raw: "Intro.pdf"
pagine: "1-21"
data_ingest: 2026-09-23
formato: slide-pdf
argomenti: [organizzazione del corso, programma, sistema di comunicazione, comunicazione digitale, rigenerazione, schema a blocchi, rumore termico, principio di separazione]
---

# Introduzione al corso — Intro.pdf

## Sommario

Slide introduttive (in inglese, eccetto le prime tre) del corso *Trasmissione dei segnali digitali*, LM Ingegneria Informatica, Università di Napoli Federico II, a.a. 2026-27, docente Donatella Darsena ([[Intro.pdf#page=1]]). Contengono l'organizzazione (testo: Madhow, *Fundamentals of Digital Communication*; esame solo **orale**, [[Intro.pdf#page=2]]) e il **programma** in sei macro-argomenti ([[Intro.pdf#page=3]]). Il resto motiva la comunicazione digitale: il processo di comunicazione, i tre elementi (trasmettitore, canale, ricevitore), i vantaggi del digitale (soprattutto la rigenerazione degli impulsi) e lo schema a blocchi completo, descritto blocco per blocco. Si chiude con i vantaggi dell'approccio digitale e il principio di separazione tra codifica di sorgente e di canale. Il materiale è qualitativo: nessuna formula.

## Punti chiave

1. **Programma del corso** ([[Intro.pdf#page=3]]):
   - rappresentazione complessa in banda base dei segnali;
   - processi aleatori;
   - modulazione digitale;
   - stima dei parametri e sincronizzazione;
   - comunicazione su canali selettivi in frequenza;
   - teoria dell'informazione e codifica di canale.
2. Esame: colloquio orale; testo di riferimento Madhow (Cambridge, 2008) più appunti ([[Intro.pdf#page=2]]).
3. Comunicazione = trasferimento di informazione nello spazio (trasmissione) o nel tempo (memorizzazione) ([[Intro.pdf#page=4]]).
4. Tre elementi base: trasmettitore, canale, ricevitore; transceiver = TX + RX ([[Intro.pdf#page=6]]).
5. Il processo di comunicazione è **statistico** ([[Intro.pdf#page=9]]).
6. Vantaggio principale del digitale: la **rigenerazione** con ripetitori rigenerativi ([[Intro.pdf#page=10]] – [[Intro.pdf#page=12]]).
7. Schema a blocchi: codificatore di sorgente → codificatore di canale → modulatore → canale → demodulatore → decodificatore di canale → decodificatore di sorgente ([[Intro.pdf#page=14]]).
8. Bit rate tipici: voce 64 kbit/s, MP3 128 kbit/s, audio da studio ~10× ([[Intro.pdf#page=15]]).
9. Il demodulatore deve **sincronizzarsi** (fase, frequenza, tempo), eventualmente **equalizzare**, e **decidere** ([[Intro.pdf#page=19]]).
10. Rumore termico: moto casuale degli elettroni nei conduttori ([[Intro.pdf#page=18]]).
11. Principio di separazione sorgente/canale: ottimo per collegamenti punto-punto; la codifica congiunta a volte è migliore; comunicazioni semantiche come tema emergente ([[Intro.pdf#page=21]]).

## Concetti introdotti

- [[sistema-comunicazione-digitale]]
- [[ripetitore-rigenerativo]]
- [[conversione-ad-da]] (citata come compito del codificatore di sorgente)

## Figure estratte

- ![[intro-p7-elementi-sistema-comunicazione.png]] — [[Intro.pdf#page=7]]
- ![[intro-p11-degradazione-impulso.png]] — [[Intro.pdf#page=11]]
- ![[intro-p14-schema-sistema-digitale.png]] — [[Intro.pdf#page=14]]

## Domande aperte

- Rumore termico: le slide non danno il modello quantitativo (densità spettrale $kT$, gaussianità). Probabilmente arriverà con i processi aleatori. TODO.
- Perché il principio di separazione è ottimo **solo** punto-punto? Rimandato alla parte di teoria dell'informazione ([[Intro.pdf#page=21]]).
- In quali casi concreti la codifica congiunta sorgente-canale batte la separazione?

## Domande da esame

- Descrivere lo schema a blocchi di un sistema di comunicazione digitale e la funzione di ogni blocco.
- Perché i sistemi di comunicazione "diventano digitali"? Cos'è un ripetitore rigenerativo?
- Quali compiti svolge il demodulatore?
- Cosa dice il principio di separazione e quali vantaggi porta?
- Perché il processo di comunicazione è di natura statistica?

_Aggiornato: 2026-09-23 — ingest iniziale_
