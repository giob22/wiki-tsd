---
tipo: concetto
importanza_esame: alta
prerequisiti: ["rivelazione-map-ml", "spazio-dei-segnali", "inviluppo-complesso"]
fonti_pdf: ["Detection.pdf#page=13", "Detection.pdf#page=15", "Detection.pdf#page=16", "Detection.pdf#page=17", "Detection.pdf#page=18"]
---

# Ricevitore ottimo in AWGN

## Definizione · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=15|15]]–[[Detection.pdf#page=18|18]]

Il **ricevitore ottimo** (ML) in AWGN per modulazione senza memoria calcola, per ogni segnale $s_k(t)$, la correlazione $\langle r(t),s_k(t)\rangle$ meno metà dell'energia, e sceglie il massimo. Si realizza con un **banco di correlatori** o, in modo equivalente, con un **banco di filtri adattati** $h_k(t)=s_k(T-t)$ campionati in $t=T$. Geometricamente è un **ricevitore a minima distanza**: decide per il punto della costellazione più vicino al vettore ricevuto; le regioni di decisione sono le **regioni di Voronoi**.

## Formule · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=15|p. 15]]–[[Detection.pdf#page=17|17]]

| Formula | Significato |
|---|---|
| $\lambda_k=\int_0^Tr(t)s_k(t)\,dt-\frac12E_{s,k}$ | statistica del correlatore (II.11) |
| $h_k(t)=s_k(T-t)$, $\int_0^Tr(\tau)s_k(\tau)d\tau=r\ast h_k\vert_{t=T}$ | filtro adattato (I.12) |
| $\text{Re}\langle\tilde r,\tilde s_k\rangle-\frac12E_{s,k}$ | statistica per segnali passa-banda, in inviluppo complesso (III.1) |
| $\max_k\lambda_k\iff\min_k\lVert\mathbf r-\mathbf s^{(k)}\rVert^2$ | minima distanza |
| $Z_k=\{\mathbf r:\lVert\mathbf r-\mathbf s^{(k)}\rVert=\min_\ell\lVert\mathbf r-\mathbf s^{(\ell)}\rVert\}$ | regioni di Voronoi |

> 🧮 Formula chiave: $h(t)=s(T-t)$ campionato in $T$; ML in AWGN = minima distanza euclidea.

Simboli: $T$ [s] durata del simbolo; $E_{s,k}$ [J] energia di $s_k$; $\tilde r$, $\tilde s_k$ inviluppi complessi; $\tilde n$ rumore complesso in banda base con PSD $N_0$.

## Derivazioni

### Derivazione — Filtro adattato · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=5|p. 5]], [[Detection.pdf#page=8|8]]
**Fonte:** dispense (I.12) e appunti p. 5 e p. 8.

$$
\begin{aligned}
r(t)\ast h(t)\Big|_{t=T}&=\int r(\tau)\,h(T-\tau)\,d\tau && \text{convoluzione valutata in } T\\
&=\int r(\tau)\,s\big(T-(T-\tau)\big)\,d\tau=\int_0^Tr(\tau)\,s(\tau)\,d\tau && h(t)=s(T-t)
\end{aligned}
$$

Il filtro adattato campionato in $T$ calcola esattamente la correlazione del correlatore: le due realizzazioni sono equivalenti.

### Derivazione — Minima distanza (IV.1)–(IV.2) · [[Detection.pdf#page=17|p. 17]], [[Detection.pdf#page=9|p. 9]]
**Fonte:** dispense p. 9 (che nella (IV.2) omettono un fattore $\frac12$) e appunti p. 9, che lo riportano.

$$
\begin{aligned}
\lambda_k&=\int_0^Tr\,s_k\,dt-\frac12\int_0^Ts_k^2\,dt && \text{(IV.1)}\\
&=\int_0^Tr\,s_k\,dt-\frac12\int_0^Ts_k^2\,dt-\frac12\int_0^Tr^2\,dt+\frac12\int_0^Tr^2\,dt && \text{sommo e sottraggo}\\
&=-\frac12\int_0^T\big(r^2-2rs_k+s_k^2\big)dt+\frac12\int_0^Tr^2\,dt=-\frac12\int_0^T[r(t)-s_k(t)]^2dt+\frac12\int_0^Tr^2dt && \text{completo il quadrato}
\end{aligned}
$$

> ⚠️ Contraddizione: nella (IV.2) delle dispense il primo integrale non ha il fattore $\frac12$; il conto (e gli appunti a lezione) lo richiedono. La conclusione non cambia.

Il termine $\frac12\int r^2$ non dipende da $k$: massimizzare $\lambda_k$ equivale a minimizzare $\int_0^T[r-s_k]^2dt=\lVert\mathbf r-\mathbf s^{(k)}\rVert^2$.

### Derivazione — Rumore in banda base complessa · [[Detection.pdf#page=16|p. 16]], [[Detection.pdf#page=8|p. 8]]
**Fonte:** dispense p. 8 (Fig. 3) e appunti p. 8.

Il rumore passa-banda ha PSD $N_0/2$ attorno a $\pm f_c$; il suo inviluppo complesso ha PSD $2\cdot\frac{N_0}{2}=N_0$ in banda ([[rumore-in-banda-passante]]). Nel modello semplificato lo si estende a tutte le frequenze: rumore complesso **bianco** di PSD $N_0$. Inoltre $\langle r_p,s_{p,k}\rangle=\text{Re}\langle\tilde r,\tilde s_k\rangle$ ([[inviluppo-complesso]]), da cui la (III.1).

## Spiegazione · appunti [[Detection.pdf#page=5|p. 5]], [[Detection.pdf#page=8|8]], [[Detection.pdf#page=9|9]]

Il criterio ML diventa un circuito molto semplice. Per ogni segnale possibile si misura quanto il ricevuto gli **somiglia** (la correlazione $\int r\,s_k$), si toglie metà della sua energia (per non favorire i segnali più energetici) e si sceglie il più somigliante.

- **Correlatore**: un moltiplicatore e un integratore per ogni segnale.
- **Filtro adattato**: un filtro con risposta impulsiva uguale al segnale ribaltato e ritardato, letto alla fine del simbolo. Fa la stessa cosa con un solo filtro LTI per ramo.
- **Geometria**: completando il quadrato, «più somigliante» diventa «più vicino». Il ricevitore si fida del canale e sceglie il punto della costellazione più vicino al punto ricevuto. Le regioni di decisione sono le celle di Voronoi, separate dagli assi dei segmenti tra punti vicini.
- **Passa-banda**: dopo la downconversion si lavora sugli inviluppi complessi, con la parte reale del prodotto scalare.

> 🎯 Esame: le due strutture del ricevitore ottimo (disegnarle), dimostrazione dell'equivalenza filtro adattato/correlatore, passaggio a minima distanza completando il quadrato, regioni di Voronoi, estensione passa-banda.

## Perché importa

Le probabilità d'errore di tutte le modulazioni si calcolano con questo ricevitore: dipendono solo dalle distanze tra i punti e dalla forma delle regioni di Voronoi ([[probabilita-errore-binaria]], [[probabilita-errore-m-aria]]).

## Connessioni

- [[rivelazione-map-ml]] — da dove viene la statistica $\lambda_k$.
- [[spazio-dei-segnali]] — distanze conservate tra segnali e vettori.
- [[inviluppo-complesso]], [[rumore-in-banda-passante]] — estensione ai segnali passa-banda.
- [[probabilita-errore-binaria]] — prestazioni del ricevitore.

## Fonti · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=15|15]]–[[Detection.pdf#page=18|18]], [[Detection.pdf#page=5|p. 5]], [[Detection.pdf#page=8|8]], [[Detection.pdf#page=9|9]]

[[elementi-teoria-rivelazione]] — Detection.pdf, dispense p. 5–10 e appunti.

_Aggiornato: 2026-11-16 — creazione da ingest Detection.pdf_
