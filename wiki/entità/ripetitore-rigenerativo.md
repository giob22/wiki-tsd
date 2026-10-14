---
tipo: entità
categoria: dispositivo
---

# Ripetitore rigenerativo

## Cos'è · [[Intro.pdf#page=11|p. 11]], [[Intro.pdf#page=12|12]]

Circuito posto a **intervalli regolari** lungo una linea di trasmissione digitale. Prima che l'impulso trasmesso diventi ambiguo, lo amplifica con un amplificatore digitale e ne recupera la forma ideale originale: l'impulso viene "rigenerato" (*reborn*).

![[intro-p11-degradazione-impulso.png]]
*Impulso binario lungo una linea: distorsione crescente con la distanza (1→4) e rigenerazione (5)*

La forma d'onda si degrada con la lunghezza della linea per due meccanismi:
1. **distorsione**: linee e circuiti hanno una funzione di trasferimento non ideale;
2. **rumore** elettrico e interferenze.

## Come si usa nel corso · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=21|p. 21]]

È il motivo principale del passaggio al digitale. Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula** lungo il collegamento. Con un amplificatore analogico, invece, il rumore verrebbe amplificato insieme al segnale.

> 🧩 Derivazione mia: il confronto con l'amplificatore analogico è implicito nelle slide («similar procedures are not available with analog»), qui lo rendo esplicito.

## Concetti correlati

- [[sistema-comunicazione-digitale]]

## Fonti · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=12|p. 12]], [[Intro.pdf#page=21|p. 21]]

- [[intro-corso]]

_Aggiornato: 2026-09-23 — creazione da ingest Intro.pdf_
