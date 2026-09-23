---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=18", "Campionamento_AD_DA.pdf#page=20", "Campionamento_AD_DA.pdf#page=21"]
---

# Aliasing e filtraggio antialiasing

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=18]]

L'**aliasing** si verifica quando $f_c$ non soddisfa la condizione del [[teorema-del-campionamento]] ($f_c<2f_m$): le repliche spettrali si **sovrappongono**. Una componente a frequenza $f_0>f_c/2$ viene "spostata" (*aliased*) e nel segnale ricostruito compare alla **frequenza alias** $f_c-f_0$.

## Formule

> 🧮 Formula chiave ([[Campionamento_AD_DA.pdf#page=18]]): $f_{alias} = f_c - f_0$ per $f_0 > f_c/2$

Validità (🧩 mia precisazione): la formula della slide vale per $f_c/2 < f_0 < f_c$. In generale la frequenza ricostruita è la replica $|f_0 - kf_c|$ che cade in $[0, f_c/2]$.

**Filtro antialiasing** ([[Campionamento_AD_DA.pdf#page=21]]): LPF **analogico**, ideale con taglio $f_c/2$, messo **prima** del campionatore.

## Derivazioni

### Derivazione — Frequenza alias di una sinusoide
**Fonte:** [[Campionamento_AD_DA.pdf#page=18]] (esempio numerico con risultato)
> 🧩 Derivazione mia, nel dominio dei campioni
$$
\begin{aligned}
x_a(t) &= \cos(2\pi f_0 t) && \text{sinusoide a } f_0 \\
x(n) &= \cos\!\left(2\pi \tfrac{f_0}{f_c}n\right) && t = nT_c = n/f_c \\
&= \cos\!\left(2\pi n - 2\pi\tfrac{f_0}{f_c}n\right) && \cos \text{ periodica di } 2\pi,\ n \text{ intero} \\
&= \cos\!\left(2\pi\tfrac{f_c-f_0}{f_c}n\right) && \text{raccolgo; } \cos(-\theta)=\cos\theta
\end{aligned}
$$
I campioni coincidono quindi con quelli di una sinusoide a $f_c-f_0$. Se $f_0>f_c/2$ allora $f_c-f_0<f_c/2$, e il LPF di ricostruzione (taglio $f_c/2$) restituisce la sinusoide a **bassa** frequenza.

**Numeri** ([[Campionamento_AD_DA.pdf#page=18]]): $f_0 = 1.5$ kHz, $f_c = 2$ kHz:
$$f_{alias} = f_c - f_0 = 2\,\text{kHz} - 1.5\,\text{kHz} = 0.5\,\text{kHz}$$
Verifica sui campioni: $f_0/f_c = 0.75$, quindi $x(n) = \cos(1.5\pi n) = \cos(2\pi n - 0.5\pi n) = \cos(0.5\pi n)$, cioè $0.25\cdot f_c = 0.5$ kHz ✓.
**Sanity check:** $f_0 = 1.5$ kHz $> f_c/2 = 1$ kHz, quindi aliasing atteso; con $f_c\ge 3$ kHz non ci sarebbe aliasing.
**Ipotesi:** ricostruzione con LPF ideale di taglio $f_c/2$.

### Derivazione — Perché un segnale di durata finita non è a banda limitata
**Fonte:** [[Campionamento_AD_DA.pdf#page=20]] (affermazione senza dimostrazione)
> 📚 Fonte esterna: proprietà standard della trasformata di Fourier (un segnale non nullo non può avere supporto limitato sia nel tempo sia in frequenza).

La slide dà l'esempio: un segnale a banda rigorosamente limitata ha necessariamente durata infinita (es. sinc, sinc²).

## Spiegazione

![[campionamento-p18-aliasing-sinusoide.png]]
*[[Campionamento_AD_DA.pdf#page=18]]. In alto, sull'asse delle frequenze: la frequenza originaria $f_0$ (a destra di $f_c/2$) viene "ribaltata" rispetto a $f_c/2$ sulla frequenza alias $f_c - f_0$. In basso: i campioni $x_a(nT_c)$ in funzione di $t/T_c$, e la sinusoide a 1.5 kHz (nera) insieme a quella a 0.5 kHz (rossa), che passano per gli **stessi campioni** $x(n)$.*

> 💡 Connessione: la figura mostra bene la "simmetria" dell'aliasing. $f_0$ e $f_c - f_0$ sono equidistanti da $f_c/2$: la frequenza $f_c/2$ fa da "specchio".

### Le due ipotesi ideali del teorema
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=19]]

Lo studio del campionamento riassunto dal teorema di Shannon si basa su **due ipotesi ideali**:
1. il segnale è a **banda rigorosamente limitata** → cosa succede quando cade: questa pagina;
2. l'**interpolazione è ideale**, con funzioni sinc → cosa succede quando cade: [[interpolazione]].

Le slide approfondiscono separatamente i due aspetti.

### Segnali a banda praticamente limitata
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=20]]

In pratica si campionano segnali di **durata finita**, che quindi **non** possono avere banda rigorosamente limitata. Sono al più a banda **praticamente** limitata: qualunque sia $f_c$, le repliche di $X_a(f)$ si sovrappongono un po', e c'è sempre un po' di aliasing nella ricostruzione.

![[campionamento-p20-banda-praticamente-limitata.png]]
*[[Campionamento_AD_DA.pdf#page=20]]: (a) spettro $X_a(f)$ di altezza 1 che non si annulla mai del tutto (code oltre $\pm f_c/2$); (b) $X_\delta(f)$: le repliche di altezza $1/T_c$ si sovrappongono e la loro somma (rosso) differisce da ogni singola replica; (c) filtro di ricostruzione $H_r(f)$ di altezza $T_c$ su $[-f_c/2, f_c/2]$; (d) confronto fra $X_r(f)$ e $X_a(f)$: il segnale ricostruito è diverso da quello originale, per effetto dell'aliasing.*

### Come ridurre l'aliasing
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=21]]

| Strategia | Pro | Contro |
|---|---|---|
| **Sovracampionamento** | repliche più distanti, meno sovrapposizione | costo e memoria (più campioni/s) |
| **Filtraggio antialiasing** (LPF prima del campionatore, taglio $f_c/2$) | più efficiente: elimina a monte l'energia oltre $f_c/2$ | è un filtro **analogico**, anch'esso non ideale in pratica |

![[campionamento-p21-antialiasing.png]]
*[[Campionamento_AD_DA.pdf#page=21]]: (a) $X_\delta(f)$ con $f_{c1}$: repliche di altezza $1/T_c$ fortemente sovrapposte intorno a $f_{c1}/2$; (b) con $f_{c2} = 2f_{c1}$ (sovracampionamento ×2) le repliche sono più distanti e la sovrapposizione intorno a $f_{c2}/2$ è molto minore; in basso, lo schema $x_a(t)$ → $H_{aa}(f)$ (filtro antialiasing) → $y_a(t)$ → campionatore ($T_c$) → $y(n)$.*

Dettagli della slide sul filtro antialiasing ([[Campionamento_AD_DA.pdf#page=21]]):
- LPF **ideale** con frequenza di taglio $f_c/2$;
- filtro **analogico**, perché agisce prima del campionamento;
- in pratica anche questo filtro sarà **non ideale**.

> 🎯 Esame: dove va il filtro antialiasing (prima del campionatore, in analogico) e perché (il segnale reale non è a banda limitata). Da non confondere con il filtro di ricostruzione (dopo, in D/A).

> 💡 Connessione: l'antialiasing *toglie* informazione oltre $f_c/2$ ma evita che quella energia si "ripieghi" sulle frequenze utili. Si perde la parte alta dello spettro invece di corrompere la parte bassa.

## Perché importa

L'aliasing è una distorsione **irreversibile**: dopo il campionamento la componente alias è indistinguibile da una componente vera a $f_c-f_0$. È per questo che ogni catena A/D reale ha un filtro antialiasing.

## Connessioni

- [[teorema-del-campionamento]] — le ipotesi la cui violazione causa aliasing.
- [[interpolazione]] — l'altra ipotesi ideale: l'interpolazione con sinc.
- [[campionamento-e-aliasing]] — esercizi.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=18]] – [[Campionamento_AD_DA.pdf#page=21]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
