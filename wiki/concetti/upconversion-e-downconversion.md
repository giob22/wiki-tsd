---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=17", "Rappresentazione_Rice.pdf#page=18", "Rappresentazione_Rice.pdf#page=19", "Rappresentazione_Rice.pdf#page=9"]
---

# Upconversion e downconversion

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=17]] (slide 14)

- **Upconversion** (conversione in su): passaggio dalla banda base alla banda passante. Dato l'inviluppo complesso $s = s_c + js_s$, si genera il segnale passa-banda con la (17) di [[inviluppo-complesso]]:
$$s_p(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{17}$$
  La slide dice che la (17) indica «immediatamente» come fare l'upconversion.
- **Downconversion** (conversione in giù): passaggio dalla banda passante alla banda base. Si moltiplica $s_p(t)$ per la portante e si filtra passa-basso:
$$\sqrt2\,s_p(t)\cos(2\pi f_c t) = s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) \tag{21}$$
  Un **filtro passa-basso** recupera la componente I. La componente Q si ottiene allo stesso modo, filtrando passa-basso $-\sqrt2\,s_p(t)\sin(2\pi f_c t)$.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $s_p = \sqrt2 s_c\cos(2\pi f_c t) - \sqrt2 s_s\sin(2\pi f_c t)$ | upconversion, eq. (17) | [[Rappresentazione_Rice.pdf#page=14]] (slide 12), [[Rappresentazione_Rice.pdf#page=17]] (slide 14) |
| $\sqrt2\,s_p\cos(2\pi f_c t) = s_c + s_c\cos(4\pi f_c t) - s_s\sin(4\pi f_c t)$ | ramo I della downconversion, eq. (21) | [[Rappresentazione_Rice.pdf#page=17]] (slide 14) |
| $-\sqrt2\,s_p\sin(2\pi f_c t) = s_s - s_s\cos(4\pi f_c t) - s_c\sin(4\pi f_c t)$ | ramo Q della downconversion | 🧩 da [[Rappresentazione_Rice.pdf#page=17]] («similmente») |
| $s(t) = \text{LPF}\big\{\sqrt2\,s_p(t)\,e^{-j2\pi f_c t}\big\}$ | i due rami in forma complessa | 🧩 da (15) e (21) |

Simboli: $f_c$ = portante [Hz]; $s_c$, $s_s$ = componenti I e Q (es. V); LPF = filtro passa-basso ideale; $4\pi f_c t = 2\pi(2f_c)t$, quindi i termini con $\cos(4\pi f_c t)$ e $\sin(4\pi f_c t)$ stanno attorno a $\pm 2f_c$.

## Derivazioni

### Derivazione — Eq. (21): ramo I della downconversion
**Fonte:** [[Rappresentazione_Rice.pdf#page=17]] (slide 14)
$$
\begin{aligned}
\sqrt2\,s_p\cos\alpha &= \sqrt2\big[\sqrt2\,s_c\cos\alpha - \sqrt2\,s_s\sin\alpha\big]\cos\alpha && \text{sostituisco la (17); } \alpha = 2\pi f_c t \\
&= 2\,s_c\cos^2\alpha - 2\,s_s\sin\alpha\cos\alpha && \sqrt2\cdot\sqrt2 = 2 \\
&= s_c\,(1 + \cos 2\alpha) - s_s\sin 2\alpha && 2\cos^2\alpha = 1 + \cos 2\alpha;\ \ 2\sin\alpha\cos\alpha = \sin 2\alpha \\
&= s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) && 2\alpha = 4\pi f_c t
\end{aligned}
$$
**Lettura:** il primo termine è $s_c(t)$, in banda base. Gli altri due sono $s_c$ e $s_s$ riportati attorno a $2f_c$. La componente Q compare **solo** attorno a $2f_c$: il prodotto $\sin\alpha\cos\alpha$ non ha parte lenta.

### Derivazione — Ramo Q della downconversion
**Fonte:** [[Rappresentazione_Rice.pdf#page=17]] (slide 14): «similmente si ottiene la componente Q».
> 🧩 Derivazione mia

$$
\begin{aligned}
-\sqrt2\,s_p\sin\alpha &= -\sqrt2\big[\sqrt2\,s_c\cos\alpha - \sqrt2\,s_s\sin\alpha\big]\sin\alpha && \text{sostituisco la (17)} \\
&= -2\,s_c\sin\alpha\cos\alpha + 2\,s_s\sin^2\alpha && \text{sviluppo} \\
&= -s_c\sin 2\alpha + s_s\,(1 - \cos 2\alpha) && 2\sin^2\alpha = 1 - \cos 2\alpha \\
&= s_s(t) - s_s(t)\cos(4\pi f_c t) - s_c(t)\sin(4\pi f_c t)
\end{aligned}
$$
Dopo il passa-basso resta $s_s(t)$. Il segno meno davanti a $\sqrt2\sin$ compensa il meno della (17).

### Derivazione — Requisito sul filtro passa-basso
**Fonte:** [[Rappresentazione_Rice.pdf#page=17]] (slide 14): la slide dice solo «filtrando passa-basso».
> 🧩 Derivazione mia. $W$ = banda di $s_c$ e $s_s$ (per un segnale passa-banda $W = B/2$, vedi [[inviluppo-complesso]]).

- Il termine utile $s_c(t)$ occupa $|f| < W$.
- I termini $s_c\cos(4\pi f_c t)$ e $s_s\sin(4\pi f_c t)$ occupano $|f \mp 2f_c| < W$, cioè da $2f_c - W$ in su.
- Un passa-basso con frequenza di taglio $f_{LP}$ li separa se
$$W \le f_{LP} \le 2f_c - W$$
- L'intervallo esiste se $W \le 2f_c - W$, cioè $W \le f_c$: sempre vero per un segnale passa-banda, perché $W = B/2 < f_c$. Con la banda stretta ($B \ll f_c$) i termini a $2f_c$ sono lontanissimi e il filtro è facile da realizzare.

### Derivazione — Perché il √2 nei moltiplicatori
**Fonte:** figura di [[Rappresentazione_Rice.pdf#page=17]] (slide 14): portanti $\sqrt2\cos(2\pi f_c t)$ e $-\sqrt2\sin(2\pi f_c t)$ sia in trasmissione sia in ricezione.
> 🧩 Derivazione mia

Il guadagno complessivo del ramo I, dal trasmettitore all'uscita del filtro, è
$$\underbrace{\sqrt2}_{\text{upconverter}}\cdot\underbrace{\sqrt2}_{\text{downconverter}}\cdot\underbrace{\tfrac12}_{\text{parte lenta di }\cos^2} = 1$$
Quindi $s_c$ esce senza cambiare ampiezza. Nello stesso tempo $s_p$ ha la stessa energia di $s$, eq. (20) di [[inviluppo-complesso]].

### Derivazione — I due rami sono una sola moltiplicazione complessa
> 🧩 Derivazione mia: collega lo schema a due rami alla (15).

$$
\begin{aligned}
\sqrt2\,s_p(t)\,e^{-j2\pi f_c t} &= \sqrt2\,s_p\cos\alpha - j\sqrt2\,s_p\sin\alpha && \text{Eulero: } e^{-j\alpha} = \cos\alpha - j\sin\alpha \\
&= \big[\sqrt2\,s_p\cos\alpha\big] + j\big[-\sqrt2\,s_p\sin\alpha\big] && \text{parte reale = ramo I, parte immaginaria = ramo Q} \\
\text{LPF}\{\cdot\} &= s_c(t) + j\,s_s(t) = s(t) && \text{(21) e ramo Q}
\end{aligned}
$$
La downconversion è quindi "moltiplica per $\sqrt2\,e^{-j2\pi f_c t}$ e filtra". Corrisponde alla (15), che trasla lo spettro di $-f_c$. Il filtro qui serve a eliminare le repliche a $\pm 2f_c$, che la (15) non genera perché parte dal segnale analitico, privo delle frequenze negative.

## Spiegazione

### Gli schemi a blocchi (slide 14)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=17]] (slide 14)

![[rappresentazione-rice-p17-upconversion-downconversion.png]]
*[[Rappresentazione_Rice.pdf#page=17]] (slide 14).*
- *Upconversion (da banda base a banda passante): $s_c(t)$ moltiplicato per $\sqrt2\cos 2\pi f_c t$, $s_s(t)$ moltiplicato per $-\sqrt2\sin 2\pi f_c t$; la somma dei due dà $s_p(t)$.*
- *Downconversion (da banda passante a banda base): $s_p(t)$ entra in due rami; uno lo moltiplica per $\sqrt2\cos 2\pi f_c t$ e lo filtra passa-basso ottenendo $s_c(t)$, l'altro lo moltiplica per $-\sqrt2\sin 2\pi f_c t$ e lo filtra ottenendo $s_s(t)$.*
- *Nota a mano: a sinistra S → $s(n)$ → MOD, che produce le due componenti $s_c(t)$ e $s_s(t)$ in ingresso all'upconverter.*

### La downconversion passo per passo (animazione)
![[grafico-rice-downconversion.gif]]
*🧩 Animazione mia della (21) ([[Rappresentazione_Rice.pdf#page=17]]). Stesso esempio del grafico I/Q in [[inviluppo-complesso]]: I con righe a 1 e 2 kHz (blu), Q con una riga a 1.5 kHz (arancio), $f_c = 10$ kHz.*
1. *Il segnale passa-banda ha le righe di I e di Q attorno a $\pm f_c$.*
2. *Moltiplicare per $\sqrt2\cos(2\pi f_c t)$ sdoppia ogni riga: una copia va verso 0, l'altra verso $\pm 2f_c$.*
3. *Attorno a 0 le due copie di I si sommano, quelle di Q hanno segno opposto e si cancellano.*
4. *Il passa-basso elimina le copie a $\pm 2f_c$.*
5. *Esce $s_c(t)$, identico a quello di partenza.*

*Le ampiezze delle righe sono controllate con la FFT nello script: 0.5 e 0.25 in banda base, nessuna riga a 1.5 kHz.*

### Tutta la catena come un unico canale (appunti p.18)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=18]] (appunti a mano)

![[rappresentazione-rice-p18-appunti-canale-equivalente.png]]
*Appunti a mano, [[Rappresentazione_Rice.pdf#page=18]]: S → MOD → upconverter → canale fisico → downconverter → DEMOD → utente. I tre blocchi centrali, cerchiati, sono «modellati come un unico canale». A destra la domanda «con tutti i passaggi che abbiamo fatto si conserva l'energia?» e la risposta «sì, per le accortezze fatte ($\sqrt2$)».*

- Modulatore e demodulatore lavorano in banda base. Tutto quello che sta in mezzo (upconverter, canale fisico, downconverter) si può vedere come **un solo canale equivalente in banda base**. Come si descrive il filtraggio del canale in banda base è in [[equivalente-banda-base-dei-filtri]].
- L'energia si conserva lungo la catena grazie ai fattori $\sqrt2$: eq. (20) e derivazione del $\sqrt2$ qui sopra.

### Cosa si recupera davvero (slide 15)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=19]] (slide 15)

La downconversion estrae le variazioni **lente** di ampiezza e fase dovute alla modulazione, e toglie la variazione di fase **rapida e prevedibile** dovuta a $f_c$. Quella variazione non porta informazione, quindi l'inviluppo complesso contiene **tutta** l'informazione del segnale passa-banda. Dettagli e grafico in [[inviluppo-complesso]].

> 🎯 Esame: disegnare gli schemi di upconversion e downconversion; ricavare la (21) e il ramo Q; spiegare perché serve il passa-basso e che banda deve avere; spiegare perché Q non "sporca" il ramo I.

## Perché importa

È la parte analogica minima dello schema modulare del transceiver ([[Rappresentazione_Rice.pdf#page=9]], slide 7): tutto il resto (modulazione, sincronizzazione, demodulazione, decodifica) si fa in digitale in banda base. Upconverter e downconverter sono l'interfaccia tra il mondo in banda base del DSP e il canale fisico passa-banda.

## Connessioni

- [[inviluppo-complesso]] — l'upconversion realizza la (17), la downconversion la (15).
- [[segnale-analitico]] — la forma complessa della downconversion è la traslazione di $-f_c$ del segnale analitico.
- [[equivalente-banda-base-dei-filtri]] — la catena upconverter + canale + downconverter diventa un canale in banda base.
- [[modulazione-digitale]] — il modulatore fornisce $s_c$ e $s_s$ all'upconverter.
- [[segnali-banda-base-e-passa-banda]] — il requisito $W < f_c$ sul filtro viene dalla definizione di passa-banda.

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=17]] (slide 14), [[Rappresentazione_Rice.pdf#page=18]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=19]] (slide 15), [[Rappresentazione_Rice.pdf#page=9]] (slide 7)

_Aggiornato: 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
