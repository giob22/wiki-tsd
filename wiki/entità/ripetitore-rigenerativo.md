---
tipo: entità
categoria: dispositivo
---

# Ripetitore rigenerativo

## Cos'è

> 📄 Fonte: [[Intro.pdf#page=11]], [[Intro.pdf#page=12]]

Circuito posto a **intervalli regolari** lungo una linea di trasmissione digitale. Prima che l'impulso trasmesso diventi ambiguo, lo amplifica con un amplificatore digitale e ne recupera la forma ideale originale: l'impulso viene "rigenerato" (*reborn*).

![[intro-p11-degradazione-impulso.png]]
*Impulso binario lungo una linea: distorsione crescente con la distanza (1→4) e rigenerazione (5) — [[Intro.pdf#page=11]]*

La forma d'onda si degrada con la lunghezza della linea per due meccanismi ([[Intro.pdf#page=12]]):
1. **distorsione**: linee e circuiti hanno una funzione di trasferimento non ideale;
2. **rumore** elettrico e interferenze.

## Come si usa nel corso

È il motivo principale del passaggio al digitale ([[Intro.pdf#page=10]]). Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula** lungo il collegamento ([[Intro.pdf#page=21]]). Con un amplificatore analogico, invece, il rumore verrebbe amplificato insieme al segnale.

> 🧩 Derivazione mia: il confronto con l'amplificatore analogico è implicito nelle slide («similar procedures are not available with analog», [[Intro.pdf#page=10]]), qui lo rendo esplicito.

## Concetti correlati

- [[sistema-comunicazione-digitale]]

## Fonti

- [[intro-corso]]
- [[Intro.pdf#page=10]] – [[Intro.pdf#page=12]], [[Intro.pdf#page=21]]

_Aggiornato: 2026-09-23 — creazione da ingest Intro.pdf_
