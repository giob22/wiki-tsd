---
tipo: concetto
importanza_esame: alta
prerequisiti: ["quantizzazione-uniforme", "media-e-varianza", "variabili-aleatorie-notevoli"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=30", "Campionamento_AD_DA.pdf#page=31"]
---

# SNR di quantizzazione e legge dei 6 dB/bit

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=30]]

Dopo aver fissato un criterio per scegliere $X_{max}$ (tramite $k_c$, [[quantizzazione-uniforme]]), si introduce un parametro che misura l'accuratezza della quantizzazione. Il **rapporto segnale-rumore di quantizzazione** misura l'accuratezza della quantizzazione nella **regione granulare** (il sovraccarico non è considerato):
$$\text{SNR} \triangleq \frac{P_x}{P_e} = \frac{\langle x^2(n)\rangle}{\langle e^2(n)\rangle}, \qquad \text{SNR}_{dB} = 10\log_{10}\text{SNR}$$
- $P_x$ = potenza del segnale; $P_e$ = potenza del rumore di quantizzazione; $\langle\cdot\rangle$ = media temporale. Le due potenze hanno la stessa unità (es. V² o W), quindi l'SNR è adimensionale e $\text{SNR}_{dB}$ si misura in dB.
- $\text{SNR}\gg1$ significa quantizzazione accurata.

## Formule

> 🧮 Formula chiave — **legge dei 6 dB/bit** ([[Campionamento_AD_DA.pdf#page=30]]):
> $$\text{SNR}_{dB} = 6.02\,b - [k_c]_{dB} + 4.77$$

- $b$ = bit per campione ($M = 2^b$);
- $[k_c]_{dB} = 20\log_{10}k_c = 20\log_{10}(X_{max}/x_{rms})$. È esplicito in [[Campionamento_AD_DA.pdf#page=43]], dove per l'uniforme si scrive $\alpha = 4.77 - 20\log_{10}(X_{max}/x_{rms})$. Si usa $20\log$ perché $k_c$ è un rapporto di **ampiezze**;
- ipotesi: $e(n)\sim\mathcal{U}(-\Delta/2,\Delta/2)$, solo regione granulare.

Modello del rumore ([[Campionamento_AD_DA.pdf#page=30]]): $\langle e^2(n)\rangle \approx E[e^2(n)] = \Delta^2/12$.

**Formule di progetto** ([[Campionamento_AD_DA.pdf#page=31]]): $P_s\le 1/k_c^2$ e $\text{SNR}_{dB} = 6.02b - [k_c]_{dB} + 4.77$.

## Derivazioni

### Derivazione — Potenza del rumore di quantizzazione $\Delta^2/12$
**Fonte:** [[Campionamento_AD_DA.pdf#page=30]] (dato come modello)
**Si parte da:** varianza dell'uniforme ([[variabili-aleatorie-notevoli]]): $\mathcal{U}(a,b)\Rightarrow\text{Var} = (b-a)^2/12$
$$
\begin{aligned}
E[e] &= 0 && \text{uniforme simmetrica intorno a } 0 \\
E[e^2] &= \text{Var}(e) + E^2[e] = \text{Var}(e) && [[media-e-varianza]] \\
&= \frac{(\Delta/2-(-\Delta/2))^2}{12} = \frac{\Delta^2}{12} && a=-\Delta/2,\ b=\Delta/2
\end{aligned}
$$

![[grafico-errore-quantizzazione.png]]
*🧩 Grafico mio: sinusoide di ampiezza 0.9 quantizzata con $b = 3$ bit ($M = 8$, $X_{max} = 1$, $\Delta = 0.25$). L'errore $e(n)$ resta sempre in $[-\Delta/2, +\Delta/2]$ (regione granulare) e salta in modo irregolare dentro questa fascia. Per questo è ragionevole modellarlo come v.a. uniforme su $(-\Delta/2, \Delta/2)$, cioè il modello da cui viene $\Delta^2/12$ ([[Campionamento_AD_DA.pdf#page=30]]).*

### Derivazione — Legge dei 6 dB/bit
**Fonte:** [[Campionamento_AD_DA.pdf#page=30]] («con semplici passaggi algebrici», passaggi non mostrati)
**Si parte da:** $\text{SNR} = P_x/P_e$, $P_e = \Delta^2/12$, $\Delta = 2X_{max}/M$ ([[quantizzazione-uniforme]]), $k_c = X_{max}/x_{rms}$, $P_x = x_{rms}^2$
$$
\begin{aligned}
\text{SNR} &= \frac{P_x}{\Delta^2/12} = \frac{12\,x_{rms}^2}{\Delta^2} && \text{sostituisco } P_e \\
&= \frac{12\,x_{rms}^2}{4X_{max}^2/M^2} = \frac{3M^2\,x_{rms}^2}{X_{max}^2} && \Delta^2 = 4X_{max}^2/M^2 \\
&= \frac{3M^2}{k_c^2} && x_{rms}^2/X_{max}^2 = 1/k_c^2 \\
&= \frac{3\cdot 2^{2b}}{k_c^2} && M = 2^b \\
\text{SNR}_{dB} &= 10\log_{10}3 + 2b\cdot10\log_{10}2 - 20\log_{10}k_c && \log \text{ di prodotto/rapporto/potenza} \\
&= 4.771 + 6.0206\,b - [k_c]_{dB} && 10\log_{10}3 = 4.771;\ 20\log_{10}2 = 6.0206
\end{aligned}
$$
**Risultato:** $\text{SNR}_{dB} \approx 6.02\,b - [k_c]_{dB} + 4.77$ ✓ (3 cifre significative sui coefficienti).
**Sanity check:** un bit in più raddoppia $M$, quindi dimezza $\Delta$, divide $P_e$ per 4 e aggiunge $10\log_{10}4 = 6.02$ dB ✓. Controllo dimensionale: $x_{rms}^2/X_{max}^2$ è adimensionale ✓.
**Ipotesi:**
1. errore uniforme su $(-\Delta/2,\Delta/2)$, ragionevole se $M\gg1$ e il segnale "attraversa" molti livelli;
2. niente sovraccarico (conta solo la regione granulare);
3. quantizzatore uniforme simmetrico.
Se cade la 2, l'SNR reale è **peggiore** perché si aggiunge l'errore di sovraccarico, non limitato.

### Derivazione — Costante per il four-sigma loading
> 🧩 Derivazione mia (il valore −7.3 compare in [[Campionamento_AD_DA.pdf#page=43]])
$$
k_c = 4 \Rightarrow [k_c]_{dB} = 20\log_{10}4 = 12.04\,\text{dB} \Rightarrow \text{SNR}_{dB} = 6.02b - 12.04 + 4.77 = 6.02b - 7.27 \approx 6.02b - 7.3
$$

## Spiegazione

- **Legge dei 6 dB/bit**: l'SNR migliora di 6 dB per ogni bit in più, cioè ogni raddoppio del numero di livelli ([[Campionamento_AD_DA.pdf#page=30]]).

![[grafico-snr-vs-bit.png]]
*🧩 Grafico mio della formula di [[Campionamento_AD_DA.pdf#page=30]]. Rette parallele di pendenza 6.02 dB/bit; raddoppiare $k_c$ trasla la retta verso il basso di $20\log_{10}2 = 6.02$ dB, cioè costa esattamente un bit. Il punto evidenziato è l'Esempio 7.6 ([[Campionamento_AD_DA.pdf#page=31]]): con $k_c = 4$ il primo $b$ che supera 85 dB è 16 (89.1 dB).*
- **Trade-off di progetto** ([[Campionamento_AD_DA.pdf#page=31]]):
  - $k_c$ ↑ ⇒ $P_s$ ↓ (meno sovraccarico) ma $\text{SNR}_{dB}$ ↓ (più rumore granulare);
  - $M = 2^b$ ↑ ⇒ $\text{SNR}_{dB}$ ↑ (qualità) ma anche costo e memoria ↑.
- **Dipendenza dal livello del segnale** ([[Campionamento_AD_DA.pdf#page=43]]): a $X_{max}$ fisso, l'SNR dipende da $x_{rms}$ tramite $k_c$. Un segnale debole (es. un parlatore a bassa voce) ha $k_c$ grande e SNR basso. Da qui nasce il [[companding]].

### Esempio 7.6
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=31]] — svolgimento completo in [[dimensionamento-quantizzatore]]

- Si vuole $\text{SNR}_{dB} = 85$ dB con $k_c = 4$: servono $b = 16$ bit (quantizzatore a 16 bit).
- Un segnale audio stereo campionato a $f_c = 44.1$ kHz e quantizzato così produce un flusso di $16\times44.1\,\text{kHz} = 705.6$ kbit/s **per canale** (L/R).
- 1 minuto di audio stereo: $2\times60\times44\,100\times16 = 84\,672\,000$ bit $= 10\,584\,000$ byte $= 10\,584$ kB $\approx 10.6$ MB.
- Fattori di conversione (ISO/IEC): 1 byte = 8 bit; 1 kB = 1000 byte; 1 MB = 1000 kB.

> 🎯 Esame: derivare la legge dei 6 dB/bit dall'inizio (è l'unico passaggio che le slide omettono esplicitamente) ed elencarne le ipotesi.

## Perché importa

Collega qualità (SNR), numero di bit e quindi bit rate ($R_b = b\,f_c$). È il primo esempio del corso di un compromesso tra qualità e risorse.

## Connessioni

- [[quantizzazione-uniforme]] — definizioni di $\Delta$, $M$, $k_c$.
- [[variabili-aleatorie-notevoli]] — varianza dell'uniforme, da cui $\Delta^2/12$.
- [[companding]] — rende l'SNR indipendente dal livello di segnale; stessa pendenza di 6 dB/bit ma costante $\alpha$ diversa.
- [[dimensionamento-quantizzatore]] — esercizi.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=30]], [[Campionamento_AD_DA.pdf#page=31]], [[Campionamento_AD_DA.pdf#page=43]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
