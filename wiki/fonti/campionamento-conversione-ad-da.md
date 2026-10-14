---
tipo: fonte
titolo: "Campionamento e conversione A/D e D/A"
file_raw: "Campionamento_AD_DA.pdf"
pagine: "1-43"
data_ingest: 2026-09-23
formato: slide-pdf
argomenti: [elaborazione digitale, conversione A/D e D/A, teorema del campionamento, aliasing, antialiasing, interpolazione ideale, ZOH, FOH, quantizzazione uniforme, fattore di carico, SNR di quantizzazione, Lloyd-Max, companding, µ-law, A-law]
---

# Campionamento e conversione A/D e D/A — Campionamento_AD_DA.pdf

## Sommario

Dopo aver motivato l'elaborazione digitale (tecnologie e vantaggi), la conversione A/D viene scomposta in **campionamento** (invertibile sotto ipotesi) e **quantizzazione** (irreversibile); la D/A si riduce all'**interpolazione**. La parte sul campionamento dimostra il **teorema di Shannon** per via spettrale (campionamento ideale con pettine di delta, repliche dello spettro, i tre casi, ricostruzione con LPF ideale), introduce la **serie di Shannon** e l'**aliasing**, e poi si occupa dei casi reali: segnali a banda solo praticamente limitata, filtro **antialiasing**, interpolatori **ZOH** e **FOH**. La parte sulla quantizzazione definisce il quantizzatore uniforme ($\Delta$, $M$, dinamica), la codifica binaria, l'errore di quantizzazione con le regioni granulare e di sovraccarico, il **fattore di carico** (con Chebyshev) e la **legge dei 6 dB/bit**, con un esempio di progetto audio. Chiude la **quantizzazione non uniforme**: pdf di Laplace della voce, quantizzatore ottimo di **Lloyd-Max**, analisi del **companding** ad alta risoluzione, legge logaritmica e leggi **µ** e **A** (ITU-T G.711) con le prestazioni.

## Punti chiave · [[Campionamento_AD_DA.pdf#page=5|p. 5]], [[Campionamento_AD_DA.pdf#page=6|6]], [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=14|p. 14]], [[Campionamento_AD_DA.pdf#page=15|15]], [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=18|18]], [[Campionamento_AD_DA.pdf#page=20|p. 20]], [[Campionamento_AD_DA.pdf#page=21|21]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]], [[Campionamento_AD_DA.pdf#page=26|p. 26]], [[Campionamento_AD_DA.pdf#page=28|p. 28]]–[[Campionamento_AD_DA.pdf#page=31|31]], [[Campionamento_AD_DA.pdf#page=35|p. 35]], [[Campionamento_AD_DA.pdf#page=36|36]], [[Campionamento_AD_DA.pdf#page=38|p. 38]], [[Campionamento_AD_DA.pdf#page=40|p. 40]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

1. A/D = campionamento + quantizzazione; D/A = interpolazione; la quantizzazione è irreversibile.
2. $X_\delta(f) = \frac1{T_c}\sum_kX_a(f-kf_c)$: repliche con passo $f_c$.
3. Teorema di Shannon: banda rigorosamente limitata $f_m$ e $f_c\ge2f_m$ ⇒ ricostruzione perfetta; frequenza di Nyquist $2f_m$.
4. LPF di ricostruzione $T_c\Pi(f/2f_r)$ con $f_m\le f_r\le f_c-f_m$; serie di Shannon con sinc.
5. Aliasing: $f_0>f_c/2$ ricompare a $f_c-f_0$ (es. 1.5 kHz → 0.5 kHz con $f_c = 2$ kHz).
6. I segnali reali hanno durata finita, quindi non sono a banda limitata: servono sovracampionamento e/o filtro antialiasing.
7. ZOH: $T_c\,\text{sinc}(fT_c)e^{-j\pi fT_c}$, causale; FOH: $T_c\,\text{sinc}^2(fT_c)$, non causale, realizzabile con ritardo $T_c$.
8. Quantizzatore uniforme: $2X_{max} = M\Delta$, $M = 2^b$; $|e|\le\Delta/2$ nella regione granulare.
9. $k_c = X_{max}/x_{rms}$; $P_s\le1/k_c^2$; four-sigma loading → 6.25%.
10. $\text{SNR}_{dB} = 6.02b-[k_c]_{dB}+4.77$; Esempio 7.6: 85 dB → 16 bit, 705.6 kbit/s per canale, 10.6 MB/min stereo.
11. Lloyd-Max: centroidi + punti medi, iterati.
12. Companding: quantizzare uniformemente il segnale compresso $F(x)$ equivale a quantizzare in modo non uniforme $x$, perché $F$ trasforma le soglie $x_i$ nelle soglie uniformi $F(x_i)$. Il progetto si riduce quindi alla scelta di $F$. Vale $\Delta_i\approx\Delta/F'(x_i)$, e la legge logaritmica rende l'SNR indipendente dalla pdf.
13. µ-law ($\mu = 255$) → $6.02b-10.11$ dB; A-law ($A = 87.6$) → $6.02b-9.99$ dB; uniforme con $k_c = 4$ → $6.02b-7.3$ dB.

## Concetti introdotti

- [[conversione-ad-da]]
- [[teorema-del-campionamento]]
- [[aliasing]]
- [[interpolazione]]
- [[quantizzazione-uniforme]]
- [[disuguaglianza-di-chebyshev]]
- [[snr-di-quantizzazione]]
- [[quantizzazione-non-uniforme]]
- [[companding]]

Entità: [[algoritmo-lloyd-max]], [[legge-mu]], [[legge-a]], [[g711]].
Esercizi: [[campionamento-e-aliasing]], [[dimensionamento-quantizzatore]].

## Figure estratte

29 immagini in `raw/assets/campionamento-pN-*.png`: 28 pagine intere più il ritaglio della caratteristica $Q(x)$ di p.28 (vedi [[index]]). Tutte le figure del PDF sono incorporate e descritte nelle pagine concetto.

## Refusi rilevati · [[Campionamento_AD_DA.pdf#page=24|p. 24]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

> ⚠️ p. 24: «First-Order Hold (ZOH)» → corretto FOH.
> ⚠️ p. 36 (figura): il secondo blocco del compander è etichettato «n-bit uniform decoder» come il terzo → probabilmente è «encoder».

## Domande aperte · [[Campionamento_AD_DA.pdf#page=16|p. 16]], [[Campionamento_AD_DA.pdf#page=29|p. 29]], [[Campionamento_AD_DA.pdf#page=30|30]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- La legge dei 6 dB/bit è ricavata «con semplici passaggi algebrici»: ricostruita nel wiki ([[snr-di-quantizzazione]]).
- Le costanti $\alpha$ di µ-law e A-law non sono derivate nelle slide. Ricostruite nel wiki con l'approssimazione $\mu|x|\gg X_{max}$ (per la A-law il ramo è esatto).
- Sovracampionamento «vantaggioso per contrastare alcuni problemi pratici»: quali, oltre all'aliasing e all'interpolazione non ideale?
- L'approssimazione a 7 segmenti di G.711 non è descritta: come cambia l'SNR rispetto alla legge continua?
- Chebyshev è usata senza enunciato: enunciato preso da fonte esterna 📚.

## Domande da esame

- Enunciare e dimostrare il teorema del campionamento; ruolo del filtro di ricostruzione.
- Cos'è l'aliasing? Come si evita in pratica? Dove si mette il filtro antialiasing?
- Serie di Shannon: perché non è realizzabile? Confronto ZOH/FOH.
- Quantizzatore uniforme: parametri, regioni, errore; fattore di carico e four-sigma loading.
- Ricavare la legge dei 6 dB/bit. Dimensionare un quantizzatore per un SNR dato.
- Condizioni di Lloyd-Max: derivazione e significato.
- Perché serve la quantizzazione robusta? Derivare la legge logaritmica. µ-law vs A-law.
- Perché compressione + quantizzazione uniforme + espansione equivale a un quantizzatore non uniforme? Cosa resta da progettare, e con quale criterio?

_Aggiornato: 2026-09-24 — punto chiave 12 e domanda d'esame sull'idea del companding; 2026-09-23 — ingest iniziale; revisione di copertura totale vs PDF_
