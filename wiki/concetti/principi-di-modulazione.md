---
tipo: concetto
importanza_esame: alta
prerequisiti: ["modulazione-digitale", "inviluppo-complesso"]
fonti_pdf: ["Modulazione.pdf#page=2", "Modulazione.pdf#page=4", "Modulazione.pdf#page=6", "Modulazione.pdf#page=8"]
---

# Principi di modulazione

## Definizione · [[Modulazione.pdf#page=2|p. 2]]–[[Modulazione.pdf#page=5|5]]

Il **modulatore digitale** trasforma una sequenza di bit in una sequenza di forme d'onda trasmissibili. È composto da due stadi in cascata: il **mapper**, che raggruppa i bit in **simboli** (blocchi di $h$ bit, $M=2^h$ valori possibili), e il **generatore di forme d'onda**, che associa a ogni simbolo una delle $M$ forme d'onda disponibili. La corrispondenza può essere **senza memoria** (la forma d'onda dipende solo dal simbolo corrente) o **con memoria** (dipende anche dagli $L$ simboli precedenti).

## Formule · [[Modulazione.pdf#page=2|p. 2]], [[Modulazione.pdf#page=4|p. 4]], [[Modulazione.pdf#page=6|p. 6]]

| Formula | Significato |
|---|---|
| $R_b=1/T_b$ | bit rate (raw: include ridondanza e protocollo) [bit/s] |
| $\xi_k=[b_k,\dots,b_{k+h-1}]$, $M=2^h$ | simbolo di sorgente (messaggio) |
| $T=hT_b$ | periodo di simbolo [s] |
| $R_s=\frac1T=\frac{R_b}{\log_2M}$ | symbol rate o baud rate [baud] |
| $s_i(t)=(2i-1-M)A$ su $[0,T)$ | esempio di Benedetto-Biglieri (livelli equispaziati) |

> 🧮 Formula chiave: $R_s=\dfrac{R_b}{\log_2M}$.

Simboli: $b_k$ bit; $h$ bit per simbolo; $T_b$ [s] periodo di bit; $A$ [V] ampiezza.

## Derivazioni

### Derivazione — Baud rate · [[Modulazione.pdf#page=4|p. 4]]
**Fonte:** slide 3.

$$
\begin{aligned}
T&=hT_b && \text{un simbolo raccoglie } h \text{ bit, che arrivano ogni } T_b\\
R_s&=\frac1T=\frac{1}{hT_b}=\frac{R_b}{h}=\frac{R_b}{\log_2M} && h=\log_2M
\end{aligned}
$$

**Numeri** (esempio della slide 4): con $M=8$ ($h=3$) il simbolo dura $3T_b$ e $R_s=R_b/3$.
**Sanity check:** $M=2$ dà $R_s=R_b$: un simbolo per bit.

### Derivazione — Perché $M$ grande riduce la banda e costa potenza · [[Modulazione.pdf#page=8|p. 8]]–[[Modulazione.pdf#page=11|11]]
**Fonte:** slide 6 e appunti p. 9–11, enunciati qualitativi.

> 🧩 Derivazione mia, con i numeri dell'esempio. Impulsi rettangolari di durata $T$ hanno spettro $\propto\text{sinc}^2(fT)$, con primo zero a $1/T$ (appunti p. 11):

$$
\begin{aligned}
B_{\text{primo zero}}&\approx\frac1T=\frac{1}{T_b\log_2M} && \text{la banda si riduce di } \log_2M\\
\overline{s^2}&=\frac1M\sum_{i=1}^M\big[(2i-1-M)A\big]^2=\frac{(M^2-1)A^2}{3} && \text{valor quadratico medio dei livelli equiprobabili}\\
d_{min}&=2A && \text{distanza tra livelli adiacenti, fissa}
\end{aligned}
$$

A potenza media fissata, $A^2=3\,\overline{s^2}/(M^2-1)$: con più livelli la distanza tra quelli adiacenti si riduce come $1/\sqrt{M^2-1}$ e il rumore li confonde più facilmente. È il **compromesso potenza-banda**.

## Spiegazione · appunti [[Modulazione.pdf#page=3|p. 3]], [[Modulazione.pdf#page=5|5]], [[Modulazione.pdf#page=9|9]]–[[Modulazione.pdf#page=11|11]]

Il modulatore è il punto in cui i bit diventano segnale. Prima i bit vengono **raggruppati**: con $h$ bit per simbolo si ha un alfabeto di $M=2^h$ simboli, e ne parte uno ogni $T=hT_b$ secondi. Poi ogni simbolo diventa una **forma d'onda**. Il bit rate che entra è «raw»: conta anche i bit di ridondanza della codifica di canale e quelli di protocollo.

**Il compromesso.** Scegliere $M$ significa scegliere tra tre risorse:
- **banda**: più bit per simbolo vuol dire simboli più lunghi, quindi spettro più stretto;
- **potenza**: con potenza fissa, più livelli stanno più vicini e il ricevitore sbaglia più spesso; per mantenere la stessa affidabilità serve più potenza;
- **complessità**: la regolarità di una forma d'onda nel tempo determina quanto decade il suo spettro. Gli impulsi rettangolari hanno code che decadono lentamente; con la **memoria** il generatore raccorda dolcemente un simbolo al successivo, eliminando le discontinuità di ampiezza e fase e ottenendo uno spettro più compatto, al prezzo di un sistema più complesso.

> 🎯 Esame: struttura del modulatore (mapper e generatore), bit rate e baud rate con la relazione $R_s=R_b/\log_2M$, modulazione con e senza memoria, compromesso potenza-banda-complessità con l'esempio $M=2,4,8$.

## Perché importa

Tutte le lezioni successive scelgono costellazioni (PAM, PSK, QAM, FSK) e ne misurano banda e probabilità d'errore: il compromesso potenza-banda introdotto qui diventa quantitativo con l'efficienza spettrale e l'efficienza in potenza ([[parametri-globali-modulazioni]]).

## Connessioni

- [[modulazione-digitale]] — la definizione generale e l'esempio binario della lezione su Rice.
- [[spazio-dei-segnali]] — come si rappresentano le $M$ forme d'onda con vettori.
- [[modulazione-lineare]] — il caso $s(t)=\sum_k\xi_kg_{TX}(t-kT)$, a cui appartiene l'esempio.
- [[parametri-globali-modulazioni]] — il compromesso potenza-banda in forma quantitativa.

## Fonti · [[Modulazione.pdf#page=2|p. 2]]–[[Modulazione.pdf#page=11|11]]

[[principles-of-modulation]] — Modulazione.pdf, slide 2–6 e appunti.

_Aggiornato: 2026-11-16 — creazione da ingest Modulazione.pdf_
