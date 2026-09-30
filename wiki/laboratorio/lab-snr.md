---
tipo: laboratorio
esame: no
macroblocco: 4
codice: "AD_conversion.m, righe 189-192"
concetti: ["snr-di-quantizzazione", "quantizzazione-uniforme", "interpolazione"]
---

# Lab 4 — SNR: cosa misura il numero stampato

> ⚠️ Non materia d'esame: serve a capire la legge dei 6 dB/bit di [[snr-di-quantizzazione]] e i suoi limiti. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-quantizzazione]].

## Cosa fa il codice

> 📄 Fonte: [[AD_conversion.m]], righe 189–192

```matlab
P_s   = mean(s.^2);                  % potenza del segnale originale
E_q   = mean((s-sq_r_trunc).^2);     % potenza dell'errore
SNR_q = 10*log10(P_s/E_q)            % in dB (senza ';': viene stampato)
```

È la definizione delle slide, $\text{SNR} = \langle x^2\rangle / \langle e^2\rangle$ ([[Campionamento_AD_DA.pdf#page=30]]), con le medie temporali calcolate sulla griglia. C'è però una differenza importante: l'errore è `s - sq_r_trunc`, cioè **segnale originale meno segnale ricostruito dopo quantizzazione e interpolazione**. Non è l'errore di quantizzazione $e(n) = x_q(n) - x(n)$ sui soli campioni.

## Cosa succede davvero

### Il valore stampato: 16.7 dB (esempio 1, triangolo, 4 bit)
> 🧩 Derivazione mia, con i numeri della replica Python

$$
\begin{aligned}
P_s &= \frac{1}{N}\sum_n s^2(t_n) = \frac{1}{N\,dt}\sum_n s^2(t_n)\,dt \approx \frac{E}{D} && \text{media su tutta la finestra} \\
&= \frac{8/3}{60} = 0.0444 && E = 8/3 \text{ (lab 0)},\ D = 60\ \text{s} \\
E_q &\approx \frac{56}{60}\cdot\Big(\frac{\Delta}{2}\Big)^2 + \text{(errore sul trapezio)} && \text{fuori dal trapezio l'errore vale sempre } \Delta/2 \\
&= 0.933\cdot 9.77\cdot10^{-4} + \dots \approx 9.1\cdot10^{-4} + 0.5\cdot10^{-4} = 9.6\cdot10^{-4} && \Delta = 1/16 \\
\text{SNR}_q &= 10\log_{10}\frac{0.0444}{9.6\cdot10^{-4}} = 10\log_{10}46.4 \approx 16.7\ \text{dB} && \text{valore stampato}
\end{aligned}
$$
Nella simulazione il 95% dell'errore viene dai 56 s in cui il segnale è **nullo** e il ricostruito vale 0.031 ([[lab-quantizzazione]]).

### Tre cose che il numero mescola
1. **La quantizzazione**, che è quello che si vorrebbe misurare.
2. **L'interpolazione.** Anche senza quantizzare, il ricostruito non è identico all'originale. Senza quantizzazione l'SNR vale 50.2 dB con il triangolo, 26.7 dB con la sinc e 15.8 dB con il rettangolo del codice ([[lab-interpolazione]]). Con la sinc, quindi, l'SNR non può superare circa 27 dB, qualunque sia il numero di bit.
3. **La finestra di osservazione.** $P_s$ e $E_q$ sono medie su 60 s, di cui 56 di "silenzio". Calcolando lo stesso SNR solo su $|t| < 2.5$ s si ottengono **28.4 dB** invece di 16.7: la potenza del segnale sale di 12 volte, quella dell'errore molto meno.

### Confronto con la legge dei 6 dB/bit
> 🧩 Derivazione mia

Il modello delle slide suppone l'errore uniforme in $(-\Delta/2, \Delta/2)$, quindi con potenza $\Delta^2/12$ ([[snr-di-quantizzazione]]). Qui invece quasi tutti gli errori valgono esattamente $\Delta/2$, con potenza $(\Delta/2)^2 = \Delta^2/4$:
$$
\begin{aligned}
\frac{\Delta^2/4}{\Delta^2/12} &= 3 && \text{rumore vero / rumore del modello} \\
10\log_{10}3 &= 4.77\ \text{dB} && \text{l'SNR vero è più basso di tanto}
\end{aligned}
$$
- **Modello:** $10\log_{10}\dfrac{0.0444}{(1/16)^2/12} = 21.4$ dB.
- **Misurato:** 16.7 dB. La differenza, 4.7 dB, è proprio il fattore 3.

La **pendenza** di 6 dB/bit invece resta: ogni bit in più dimezza $\Delta$, qualunque sia la forma dell'errore. Se l'errore è proporzionale a $\Delta$, la sua potenza si divide per 4, cioè $10\log_{10}4 = 6.02$ dB in più di SNR.

| $b$ [bit] | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| SNR del codice [dB] | −1.4 | 4.6 | 10.6 | **16.7** | 22.7 | 28.7 | 34.4 | 40.0 | 44.7 | 47.9 |
| SNR sui soli campioni [dB] | −1.4 | 4.7 | 10.7 | 16.7 | 22.8 | 28.9 | 34.8 | 40.9 | 46.8 | 52.9 |

*🧩 Valori dalla replica Python, esempio 1 con triangolo. Fino a 7–8 bit le due righe coincidono e crescono di 6.0 dB per bit. Poi quella del codice si ferma verso il limite dell'interpolazione (50.2 dB): il rumore di quantizzazione è ormai più piccolo dell'errore di ricostruzione.*

![[grafico-lab-snr-vs-bit.png]]
*🧩 Grafico mio.*
- *Blu: SNR stampato dal codice al variare di $b$. Arancio: SNR dei soli campioni.*
- *Nero tratteggiato: il modello $\Delta^2/12$, parallelo ma 4.77 dB più in alto.*
- *Linee orizzontali: i limiti senza quantizzazione, 50.2 dB con il triangolo e 26.7 dB con la sinc. La curva blu non può superarli.*

## Dubbi chiariti

- **"16.7 dB con 4 bit: la formula non dava di più?"** La formula $6.02b + 4.77 - [k_c]_{dB}$ vale con l'errore uniforme. Qui l'errore è sistematico ($\Delta/2$ sugli zeri) e costa 4.77 dB. In più $P_s$ è piccola, perché il segnale occupa 4 s su 60.
- **"Allora il codice sbaglia?"** No: misura l'SNR **dell'intera catena** A/D + D/A su quella finestra. È una misura diversa, più "da ingegnere", di quella della slide, che isola la sola quantizzazione.
- **"Aumentare i bit migliora sempre?"** Solo finché domina la quantizzazione. Oltre, conta l'interpolatore (e prima ancora il campionamento: vedi l'esempio 2 in [[lab-campionamento]], dove l'aliasing tiene l'SNR a 2 dB).

## Collegamento alla teoria

[[snr-di-quantizzazione]]: definizione, modello $\Delta^2/12$ e legge dei 6 dB/bit ([[Campionamento_AD_DA.pdf#page=30]]). Il fattore di carico $k_c$ di [[quantizzazione-uniforme]] ([[Campionamento_AD_DA.pdf#page=29]]) qui è grande, perché la potenza media è piccola rispetto alla dinamica: anche questo abbassa l'SNR.

_Aggiornato: 2026-09-30 — creazione da ingest del laboratorio (AD_conversion.m)_
