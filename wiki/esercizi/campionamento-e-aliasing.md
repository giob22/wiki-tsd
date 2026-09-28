---
tipo: esercizio
argomento: "Scelta della frequenza di campionamento, aliasing, numero di campioni"
difficoltà: bassa
---

# Campionamento e aliasing

## Metodo

1. Individuare la **banda monolatera** $f_m$ del segnale (per una sinusoide: la sua frequenza).
2. **Nyquist**: $f_c\ge2f_m$ ([[teorema-del-campionamento]]).
3. Se $f_c<2f_m$, trovare la **frequenza alias**: per ogni componente $f_0>f_c/2$, cercare la replica $|f_0-kf_c|$ che cade in $[0,f_c/2]$. Per $f_c/2<f_0<f_c$ si ha $f_c-f_0$ ([[aliasing]]).
4. **Numero di campioni** in una durata $T$: $N = T\cdot f_c$ (× numero di canali).
5. Controllare le unità: kHz × s = migliaia di campioni.

## Formule usate

- $f_c\ge2f_m$ — [[teorema-del-campionamento]] ([[Campionamento_AD_DA.pdf#page=14]])
- $f_{alias} = f_c-f_0$ — [[aliasing]] ([[Campionamento_AD_DA.pdf#page=18]])
- $N = T\,f_c$ — [[Campionamento_AD_DA.pdf#page=16]]

## Casi svolti

### Caso 1 — Frequenze di Nyquist di voce, audio, video
**Traccia** ([[Campionamento_AD_DA.pdf#page=16]]): banda monolatera 4 kHz (voce), 20 kHz (audio), 5 MHz (video). Frequenza minima di campionamento?
$$
\begin{aligned}
f_{c,\min} &= 2f_m && \text{Nyquist} \\
\text{voce: } &2\times4\,\text{kHz} = 8\,\text{kHz} \\
\text{audio: } &2\times20\,\text{kHz} = 40\,\text{kHz} \\
\text{video: } &2\times5\,\text{MHz} = 10\,\text{MHz}
\end{aligned}
$$
**Sanity check:** il CD audio usa 44.1 kHz ([[Campionamento_AD_DA.pdf#page=16]]), cioè più di 40 kHz: un leggero sovracampionamento che lascia spazio al filtro antialiasing reale (🧩 mia interpretazione).

### Caso 2 — Campioni in 1 minuto di audio
**Traccia** ([[Campionamento_AD_DA.pdf#page=16]]): 1 minuto di audio mono a $f_c = 44.1$ kHz. Quanti campioni? E in stereo?
$$
\begin{aligned}
N_{mono} &= T\cdot f_c = 60\,\text{s}\times44\,100\,\text{campioni/s} && \text{sostituisco} \\
&= 2\,646\,000\ \text{campioni} \\
N_{stereo} &= 2\times N_{mono} = 5\,292\,000\ \text{campioni} && \text{canali L e R}
\end{aligned}
$$
**Risultato:** 2 646 000 campioni (mono) ✓ come la slide; il doppio in stereo.

### Caso 3 — Sinusoide sottocampionata
**Traccia** ([[Campionamento_AD_DA.pdf#page=18]]): sinusoide a $f_0 = 1.5$ kHz campionata a $f_c = 2$ kHz. A quale frequenza viene ricostruita?
$$
\begin{aligned}
f_c/2 &= 1\,\text{kHz} < f_0 = 1.5\,\text{kHz} && \Rightarrow \text{aliasing} \\
f_{alias} &= f_c - f_0 = 2 - 1.5 = 0.5\,\text{kHz} && f_c/2<f_0<f_c
\end{aligned}
$$
**Verifica sui campioni** (derivazione completa in [[aliasing]]): $\cos(2\pi\cdot0.75\,n) = \cos(2\pi\cdot0.25\,n)$ per $n$ intero, e $0.25\cdot2\,\text{kHz} = 0.5$ kHz ✓.
**Risultato:** 0.5 kHz. Per evitare l'aliasing servirebbe $f_c\ge3$ kHz.
**Perché proprio 0.5 kHz:** i campioni del coseno a 1.5 kHz (1, 0, −1, 0, 1, …) sono anche quelli dei coseni a 0.5, 2.5, 3.5 kHz, …, e il filtro di ricostruzione lascia passare solo $|f| < f_c/2 = 1$ kHz. Ragionamento completo, con due animazioni: [[aliasing#Perché il segnale ricostruito è a 0.5 kHz]].

## Trappole

- $f_c\ge2f_m$ con $f_m$ banda **monolatera**, non la larghezza totale dello spettro bilatero.
- Con $f_c = 2f_m$ esatto serve un filtro perfettamente ideale ($f_r = f_m$ esatta): in pratica si sovracampiona.
- La formula $f_c-f_0$ vale solo per $f_c/2<f_0<f_c$. Per $f_0>f_c$ bisogna prima sottrarre multipli di $f_c$.
- Il ricostruttore non "sa" quale fosse la frequenza vera: restituisce sempre la replica che cade sotto $f_c/2$ ([[aliasing#Perché il segnale ricostruito è a 0.5 kHz]]).
- Il filtro **antialiasing** va *prima* del campionatore ed è analogico; il filtro di **ricostruzione** va *dopo*, nella D/A ([[aliasing]], [[interpolazione]]).
- Stereo = 2 canali: raddoppiare campioni e bit.

_Aggiornato: 2026-09-24 — Caso 3: perché si ricostruisce 0.5 kHz, link al ragionamento completo; 2026-09-23 — revisione di copertura: rimosso caso inventato (scelta di f_r)_
