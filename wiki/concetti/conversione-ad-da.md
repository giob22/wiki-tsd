---
tipo: concetto
importanza_esame: media
prerequisiti: []
fonti_pdf: ["Campionamento_AD_DA.pdf#page=2", "Campionamento_AD_DA.pdf#page=3", "Campionamento_AD_DA.pdf#page=4", "Campionamento_AD_DA.pdf#page=5", "Campionamento_AD_DA.pdf#page=6"]
---

# Conversione A/D e D/A

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=3]], [[Campionamento_AD_DA.pdf#page=5]], [[Campionamento_AD_DA.pdf#page=6]]

- **Convertitore A/D**: trasforma un segnale analogico (continuo nel tempo e nell'ampiezza) in un segnale **digitale** (discreto nel tempo e nell'ampiezza).
- **Convertitore D/A**: esegue la trasformazione inversa.

La conversione **A/D** comprende due operazioni distinte ([[Campionamento_AD_DA.pdf#page=5]]):
1. **campionamento**: discretizzazione dei tempi, da tempo continuo a tempo discreto → [[teorema-del-campionamento]];
2. **quantizzazione**: discretizzazione delle ampiezze, da ampiezza continua a discreta → [[quantizzazione-uniforme]].

La conversione **D/A** esegue **una sola** operazione ([[Campionamento_AD_DA.pdf#page=6]]):
- **interpolazione**: da tempo discreto a tempo continuo → [[interpolazione]].

## Formule

Schema (🧩 mia sintesi di [[Campionamento_AD_DA.pdf#page=5]], [[Campionamento_AD_DA.pdf#page=6]], [[Campionamento_AD_DA.pdf#page=8]], [[Campionamento_AD_DA.pdf#page=26]]):
$$
x_a(t) \xrightarrow{\ \text{campion.}\ } x(n) = x_a(nT_c) \xrightarrow{\ \text{quantizz.}\ } x_q(n) = Q[x(n)] \xrightarrow{\ \text{codifica}\ } \text{bit}
\;\;\cdots\;\;
x_q(n) \xrightarrow{\ \text{interpolaz.}\ } x_r(t)
$$

Anche con un campionamento perfettamente reversibile, la cascata A/D + D/A dà $x_r(t)\neq x_a(t)$ a causa della quantizzazione ([[Campionamento_AD_DA.pdf#page=6]]).

## Derivazioni

Nessun risultato numerico in questa parte. Le derivazioni sono nelle pagine dei singoli stadi.

## Spiegazione

![[campionamento-p5-conversione-ad.png]]
*Convertitore A/D ([[Campionamento_AD_DA.pdf#page=5]]): $x_a(t)$ → campionatore (comandato da $T_c$) → $x(n)$ → quantizzatore → $x_q(n)$.*

![[campionamento-p6-conversione-da.png]]
*Convertitore D/A ([[Campionamento_AD_DA.pdf#page=6]]): $x_q(n)$ → interpolatore (comandato da $T_c$) → $x_r(t)$.*

### Invertibilità
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=5]]

- Il **campionamento** è invertibile *sotto opportune ipotesi*: è il contenuto del [[teorema-del-campionamento]].
- La **quantizzazione** è **irreversibile**: più ampiezze vengono mappate sullo stesso livello e l'informazione persa non si recupera.

> 🎯 Esame: perché la D/A ha una sola operazione? Perché la quantizzazione non si può invertire: si può solo interpolare i campioni quantizzati.

### Dall'elaborazione analogica a quella digitale
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=2]] – [[Campionamento_AD_DA.pdf#page=4]]

([[Campionamento_AD_DA.pdf#page=2]])
- I fenomeni fisici evolvono **con continuità** nel tempo e nell'ampiezza, quindi sono rappresentati da **segnali analogici**.
- Le prime elaborazioni dei segnali erano **analogiche**:
  - richiedevano il progetto e la realizzazione di un circuito elettrico/elettronico;
  - processo lungo, costoso e poco flessibile.
- Oggi l'elaborazione dei segnali si fa con **tecniche digitali**.
- Per essere elaborato, memorizzato o trasmesso digitalmente, un segnale analogico va trasformato in un **segnale digitale** (discreto nel tempo e nell'ampiezza).
- In molti casi serve anche la **trasformazione inversa**, da digitale ad analogico.

![[campionamento-p2-analogico-digitale.png]]
*Esempio di elaborazione analogica ([[Campionamento_AD_DA.pdf#page=2]]): un circuito passivo (induttori, condensatori, resistori) che divide il segnale fra tweeter e woofer. Ogni funzione richiede un circuito progettato apposta.*

![[campionamento-p3-dispositivi-digitali.png]]
*Elaborazione digitale di un segnale analogico ([[Campionamento_AD_DA.pdf#page=3]]): $x_a(t)$ → **A/D** → $x_q(n)$ → **DSP** → $y_q(n)$ → **D/A** → $y_a(t)$. Visto dall'esterno, l'insieme si comporta come un "sistema analogico" (riquadro tratteggiato).*

Due dispositivi di conversione fondamentali ([[Campionamento_AD_DA.pdf#page=3]]): convertitore **A/D** (segnale analogico → digitale) e convertitore **D/A** (segnale digitale → analogico). L'elaborazione avviene con **sistemi digitali**, realizzabili con diverse tecnologie:
- ASIC (application-specific integrated circuit)
- DSP (digital signal processor)
- FPGA (field-programmable gate array)
- microcontrollori (es. Atmel, STM)
- microprocessori general purpose (es. Intel, AMD)

L'elaborazione digitale è un **algoritmo** che si può tradurre in codice ed eseguire via software.

**Vantaggi** ([[Campionamento_AD_DA.pdf#page=4]]):
- **Programmabilità / versatilità / sviluppo rapido**: un dispositivo digitale si programma per un determinato compito e si riprogramma facilmente per un altro (*software upgrade*).
- **Stabilità / riproducibilità**: i risultati sono stabili nel tempo e riproducibili; dispositivi diversi che eseguono lo stesso programma danno gli stessi risultati.
- **Potenzialità**: si possono implementare algoritmi complessi non realizzabili in analogico (es. crittografia, correzione/rivelazione di errori, compressione dati).
- **Costi**: i dispositivi digitali si producono facilmente in grandi quantità e a basso costo.

> 💡 Connessione: sono gli stessi argomenti di "going digital" in [[sistema-comunicazione-digitale]] ([[Intro.pdf#page=13]]), visti dal lato dell'elaborazione invece che della trasmissione.

## Perché importa

Il convertitore A/D è il primo stadio del codificatore di sorgente per sorgenti analogiche ([[Intro.pdf#page=15]]). Il suo dimensionamento ($f_c$, $b$) fissa il bit rate da trasmettere: $R_b = b\cdot f_c$ ([[dimensionamento-quantizzatore]]).

## Connessioni

- [[teorema-del-campionamento]], [[aliasing]], [[interpolazione]] — dimensione temporale.
- [[quantizzazione-uniforme]], [[snr-di-quantizzazione]], [[quantizzazione-non-uniforme]], [[companding]] — dimensione delle ampiezze.
- [[sistema-comunicazione-digitale]] — la collocazione nella catena di trasmissione.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=2]] – [[Campionamento_AD_DA.pdf#page=6]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
