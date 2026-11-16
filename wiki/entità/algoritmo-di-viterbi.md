---
tipo: entità
categoria: algoritmo
---

# Algoritmo di Viterbi

## Cos'è · [[signaling_bandlimited_channel.pdf#page=40|p. 40]]–[[signaling_bandlimited_channel.pdf#page=43|43]]

L'**algoritmo di Viterbi** (VA) trova, tra tutti i cammini che attraversano da sinistra a destra un **traliccio** (trellis) finito, quello con metrica totale massima (o minima). Ogni ramo ha una **metrica di ramo** $m(\sigma_k,\sigma_{k+1})$; le metriche sono additive, e la metrica di un cammino è la somma delle etichette dei suoi rami:

$$\lambda(\sigma_0,\dots,\sigma_K)=\sum_{k=0}^{K-1}m(\sigma_k,\sigma_{k+1})$$

con $\sigma_k\in\{S_1,\dots,S_{N_\sigma}\}$ stato al tempo $k$ e $K$ profondità del traliccio.

- **Forza bruta**: si valutano tutti i cammini, con complessità esponenziale in $K$ e ritardo di decisione $K$ (si decide solo alla fine).
- **VA**: complessità **lineare in $K$**. La versione **troncata** decide con ritardo molto minore di $K$.

## Come funziona: Add, Compare, Select · [[signaling_bandlimited_channel.pdf#page=43|p. 43]], [[signaling_bandlimited_channel.pdf#page=44|44]]

Per ogni stato $\sigma_{k+1}$, a ogni passo:
1. **Add**: per ogni ramo entrante, somma la metrica accumulata nello stato di partenza $\sigma_k$ e la metrica del ramo;
2. **Compare**: confronta le somme;
3. **Select**: tiene il ramo migliore (il **sopravvissuto**) e scarta tutti gli altri rami entranti in $\sigma_{k+1}$.

Si ripete dallo stato iniziale a quello finale; alla fine si risale all'indietro lungo i sopravvissuti. La figura di p. 41 mostra un traliccio con $N_\sigma=4$ stati e $K=6$; quella di p. 44 i sopravvissuti passo per passo, fino a un solo cammino a $k=6$.

**Perché scartare è lecito:** se il cammino ottimo passa per $\sigma_{k+1}$, il suo tratto iniziale fino a $\sigma_{k+1}$ è per forza il migliore tra quelli che arrivano lì, perché il resto del cammino si somma allo stesso modo a tutti (principio di ottimalità, 🧩 spiegazione mia).

### Esempio svolto (mio)
> 🧩 Esempio mio, non dalle slide: due stati A e B, partenza e arrivo in A, $K=3$, si cerca la metrica **minima**.

| Ramo | $k=0\to1$ | $k=1\to2$ | $k=2\to3$ |
|---|---|---|---|
| A → A | 1 | 2 | 3 |
| A → B | 3 | 1 | 1 |
| B → A | – | 1 | 1 |
| B → B | – | 3 | 2 |

$$
\begin{aligned}
k=1:&\quad \Gamma_A=1,\ \Gamma_B=3 && \text{un solo ramo entrante}\\
k=2:&\quad \Gamma_A=\min(1+2,\ 3+1)=3\ (\text{da A}),\quad \Gamma_B=\min(1+1,\ 3+3)=2\ (\text{da A}) && \text{ACS}\\
k=3:&\quad \Gamma_A=\min(3+3,\ 2+1)=3\ (\text{da B}) && \text{arrivo in A}
\end{aligned}
$$

Risalendo i sopravvissuti: A → A → B → A, metrica $1+1+1=3$. **Verifica a forza bruta:** i quattro cammini da A ad A valgono AAAA $=6$, AABA $=3$, ABAA $=7$, ABBA $=7$: il minimo è 3, lo stesso. Il VA ha fatto 3 confronti invece di valutare tutti i cammini; con $K$ grande la differenza diventa enorme.

## Come si usa nel corso · [[signaling_bandlimited_channel.pdf#page=45|p. 45]]–[[signaling_bandlimited_channel.pdf#page=47|47]]

Nella [[equalizzazione]] a massima verosimiglianza (MLSE) la log-verosimiglianza della sequenza si scompone come $\lambda(y)=U_L(\sigma_L)+\sum_kV_k$: gli stati sono le ultime $L$ decisioni sui simboli ($M^L$ stati) e le metriche di ramo sono le $V_k$. La MLSE diventa la ricerca del cammino di metrica **massima**, e il VA ne riduce la complessità da $M^{K+1}$ a circa $KM^{L+1}$.

## Concetti correlati

- [[equalizzazione]]: MLSE, la sua applicazione nel corso.
- [[interferenza-intersimbolica]]: la memoria $L$ del canale fissa il numero di stati.
- [[rivelazione-map-ml]]: il VA massimizza la stessa verosimiglianza, su sequenze.

## Fonti · [[signaling_bandlimited_channel.pdf#page=39|p. 39]]–[[signaling_bandlimited_channel.pdf#page=47|47]]

- [[signaling-bandlimited-channels]]

_Aggiornato: 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf (Lezione 14)_
