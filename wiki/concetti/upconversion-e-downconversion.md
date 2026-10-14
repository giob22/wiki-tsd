---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=2", "Rappresentazione_Rice.pdf#page=10", "Rappresentazione_Rice.pdf#page=20", "Rappresentazione_Rice.pdf#page=21", "Rappresentazione_Rice.pdf#page=22"]
---

# Upconversion e downconversion

## Definizione · [[Rappresentazione_Rice.pdf#page=20|p. 20]]

- **Upconversion** (conversione in su): passaggio dalla banda base alla banda passante. Dato l'inviluppo complesso $s = s_c + js_s$, si genera il segnale passa-banda con la (17) di [[inviluppo-complesso]]:
$$s_p(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{17}$$
  La slide dice che la (17) indica «immediatamente» come fare l'upconversion.
- **Downconversion** (conversione in giù): passaggio dalla banda passante alla banda base. Si moltiplica $s_p(t)$ per la portante e si filtra passa-basso:
$$\sqrt2\,s_p(t)\cos(2\pi f_c t) = s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) \tag{21}$$
  Un **filtro passa-basso** recupera la componente I. La componente Q si ottiene allo stesso modo, filtrando passa-basso $-\sqrt2\,s_p(t)\sin(2\pi f_c t)$.

### Il passaggio complesso ↔ reale (appunti p.2) · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

Gli appunti di p.2 descrivono i due stadi dal punto di vista di cosa fanno al segnale:
- **Trasmettitore:** porta il segnale nella specifica porzione dello spettro, «per adattare il segnale rispetto alla capacità del canale». È l'upconversion.
- **Ricevitore:** porta il segnale in banda base, e questo «comporta che il segnale diventa complesso». È la downconversion.
- In entrambi i momenti, trasmissione e ricezione, il segnale in banda base è complesso. Quindi:
  - in trasmissione il passaggio è **complesso → reale**: dall'inviluppo $s = s_c + js_s$ al segnale fisico $s_p$;
  - in ricezione è **reale → complesso**: da $s_p$ di nuovo a $s_c$ e $s_s$.
- Nota finale: «in entrambi i casi è un processo eseguito da un DSP».

> 🧩 Perché il segnale fisico è reale e quello in banda base complesso: sul canale viaggia una tensione o un campo, che è una grandezza reale, quindi $s_p(t)$ è reale. In banda base invece lo spettro di $s_p$ attorno a $+f_c$, spostato in 0, non è in generale simmetrico, e un segnale con spettro non hermitiano è complesso ([[inviluppo-complesso]]). La (17) è il complesso → reale: prende $s_c$ e $s_s$ e restituisce un solo segnale reale. La downconversion fa il contrario.

> ⚠️ Da chiarire: nello schema della slide 7 upconversion e downconversion sono passi distinti dal DSP, che lavora solo sull'inviluppo in banda base. La slide 6 dice che l'elaborazione analogica va ridotta al minimo, senza dire quali blocchi restano analogici. La nota di p.2 attribuisce invece il passaggio complesso ↔ reale a un DSP.

## Formule · [[Rappresentazione_Rice.pdf#page=16|p. 16]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

| Formula | Significato |
|---|---|
| $s_p = \sqrt2 s_c\cos(2\pi f_c t) - \sqrt2 s_s\sin(2\pi f_c t)$ | upconversion, eq. (17) |
| $\sqrt2\,s_p\cos(2\pi f_c t) = s_c + s_c\cos(4\pi f_c t) - s_s\sin(4\pi f_c t)$ | ramo I della downconversion, eq. (21) |
| $-\sqrt2\,s_p\sin(2\pi f_c t) = s_s - s_s\cos(4\pi f_c t) - s_c\sin(4\pi f_c t)$ | ramo Q della downconversion |
| $s(t) = \text{LPF}\big\{\sqrt2\,s_p(t)\,e^{-j2\pi f_c t}\big\}$ | i due rami in forma complessa |

Simboli: $f_c$ = portante [Hz]; $s_c$, $s_s$ = componenti I e Q (es. V); LPF = filtro passa-basso ideale; $4\pi f_c t = 2\pi(2f_c)t$, quindi i termini con $\cos(4\pi f_c t)$ e $\sin(4\pi f_c t)$ stanno attorno a $\pm 2f_c$.

## Derivazioni

### Derivazione — Eq. (21): ramo I della downconversion · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
$$
\begin{aligned}
\sqrt2\,s_p\cos\alpha &= \sqrt2\big[\sqrt2\,s_c\cos\alpha - \sqrt2\,s_s\sin\alpha\big]\cos\alpha && \text{sostituisco la (17); } \alpha = 2\pi f_c t \\
&= 2\,s_c\cos^2\alpha - 2\,s_s\sin\alpha\cos\alpha && \sqrt2\cdot\sqrt2 = 2 \\
&= s_c\,(1 + \cos 2\alpha) - s_s\sin 2\alpha && 2\cos^2\alpha = 1 + \cos 2\alpha;\ \ 2\sin\alpha\cos\alpha = \sin 2\alpha \\
&= s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) && 2\alpha = 4\pi f_c t
\end{aligned}
$$
**Lettura:** il primo termine è $s_c(t)$, in banda base. Gli altri due sono $s_c$ e $s_s$ riportati attorno a $2f_c$. La nota a mano sulla slide li sottolinea con «tagliati dal filtro»: è il passa-basso a eliminarli. La componente Q compare **solo** attorno a $2f_c$: il prodotto $\sin\alpha\cos\alpha$ non ha parte lenta.

### Derivazione — Ramo Q della downconversion · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** «similmente si ottiene la componente Q».
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

### Derivazione — Requisito sul filtro passa-basso · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** la slide dice solo «filtrando passa-basso».
> 🧩 Derivazione mia. $W$ = banda di $s_c$ e $s_s$ (per un segnale passa-banda $W = B/2$, vedi [[inviluppo-complesso]]).

- Il termine utile $s_c(t)$ occupa $|f| < W$.
- I termini $s_c\cos(4\pi f_c t)$ e $s_s\sin(4\pi f_c t)$ occupano $|f \mp 2f_c| < W$, cioè da $2f_c - W$ in su.
- Un passa-basso con frequenza di taglio $f_{LP}$ li separa se
$$W \le f_{LP} \le 2f_c - W$$
- L'intervallo esiste se $W \le 2f_c - W$, cioè $W \le f_c$: sempre vero per un segnale passa-banda, perché $W = B/2 < f_c$. Con la banda stretta ($B \ll f_c$) i termini a $2f_c$ sono lontanissimi e il filtro è facile da realizzare.

### Derivazione — Perché il √2 nei moltiplicatori · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** figura di p. 20 (slide 14): portanti $\sqrt2\cos(2\pi f_c t)$ e $-\sqrt2\sin(2\pi f_c t)$ sia in trasmissione sia in ricezione.
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

### Gli schemi a blocchi (slide 14) · [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

![[rappresentazione-rice-p20-upconversion-downconversion.png]]
- *Upconversion (da banda base a banda passante): $s_c(t)$ moltiplicato per $\sqrt2\cos 2\pi f_c t$, $s_s(t)$ moltiplicato per $-\sqrt2\sin 2\pi f_c t$; la somma dei due dà $s_p(t)$.*
- *Downconversion (da banda passante a banda base): $s_p(t)$ entra in due rami; uno lo moltiplica per $\sqrt2\cos 2\pi f_c t$ e lo filtra passa-basso ottenendo $s_c(t)$, l'altro lo moltiplica per $-\sqrt2\sin 2\pi f_c t$ e lo filtra ottenendo $s_s(t)$.*
- *Note a mano: a sinistra S → $s(n)$ → MOD, che produce le due componenti $s_c(t)$ e $s_s(t)$ in ingresso all'upconverter. Sopra il modulatore: «esce l'inviluppo». Sotto la (21), i due termini a $2f_c$ sono sottolineati con «tagliati dal filtro».*

> 💡 Connessione: «esce l'inviluppo» vuol dire che il modulatore di questo disegno è la sola parte in banda base (il DSP della slide 7). Nelle note di p. 10 il macroblocco "modulatore" comprende anche l'upconversion: il nome MOD qui indica solo il primo dei due passi ([[modulazione-digitale]]).

### La downconversion passo per passo (animazione) · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
![[grafico-rice-downconversion.gif]]
*🧩 Animazione mia della (21). Stesso esempio del grafico I/Q in [[inviluppo-complesso]]: I con righe a 1 e 2 kHz (blu), Q con una riga a 1.5 kHz (arancio), $f_c = 10$ kHz.*
1. *Il segnale passa-banda ha le righe di I e di Q attorno a $\pm f_c$.*
2. *Moltiplicare per $\sqrt2\cos(2\pi f_c t)$ sdoppia ogni riga: una copia va verso 0, l'altra verso $\pm 2f_c$.*
3. *Attorno a 0 le due copie di I si sommano, quelle di Q hanno segno opposto e si cancellano.*
4. *Il passa-basso elimina le copie a $\pm 2f_c$.*
5. *Esce $s_c(t)$, identico a quello di partenza.*

*Le ampiezze delle righe sono controllate con la FFT nello script: 0.5 e 0.25 in banda base, nessuna riga a 1.5 kHz.*

### Tutta la catena come un unico canale (appunti p.21) · [[Rappresentazione_Rice.pdf#page=21|p. 21]]

![[rappresentazione-rice-p21-appunti-canale-equivalente.png]]
*Appunti a mano: S → MOD → upconverter → canale fisico → downconverter → DEMOD → utente. I tre blocchi centrali, cerchiati, sono «modellati come un unico canale». A destra la domanda «con tutti i passaggi che abbiamo fatto si conserva l'energia?» e la risposta «sì, per le accortezze fatte ($\sqrt2$)».*

- Modulatore e demodulatore lavorano in banda base. Tutto quello che sta in mezzo (upconverter, canale fisico, downconverter) si può vedere come **un solo canale equivalente in banda base**. Come si descrive il filtraggio del canale in banda base è in [[equivalente-banda-base-dei-filtri]].
- L'energia si conserva lungo la catena grazie ai fattori $\sqrt2$: eq. (20) e derivazione del $\sqrt2$ qui sopra.

### Cosa si recupera davvero (slide 15) · [[Rappresentazione_Rice.pdf#page=22|p. 22]]

La downconversion estrae le variazioni **lente** di ampiezza e fase dovute alla modulazione, e toglie la variazione di fase **rapida e prevedibile** dovuta a $f_c$. Quella variazione non porta informazione, quindi l'inviluppo complesso contiene **tutta** l'informazione del segnale passa-banda. Nota a mano in testa alla slide: «l'inviluppo complesso ci permette di separare le variazioni lente introdotte dalla modulazione in banda base». Sulla slide sono evidenziati «eliminating» e $f_c$: la parte eliminata è proprio quella legata alla portante. Dettagli e grafico in [[inviluppo-complesso]].

> 🎯 Esame: disegnare gli schemi di upconversion e downconversion; ricavare la (21) e il ramo Q; spiegare perché serve il passa-basso e che banda deve avere; spiegare perché Q non "sporca" il ramo I.

## Perché importa · [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

Nello schema modulare del transceiver upconversion e downconversion sono gli unici passi che toccano il segnale passa-banda. Tutto il resto lo fa il DSP sull'inviluppo in banda base: codifica, modulazione e filtraggio in trasmissione; sincronizzazione, demodulazione e decodifica in ricezione. Upconverter e downconverter sono quindi l'interfaccia tra il mondo in banda base del DSP e il canale fisico passa-banda. La slide 6 aggiunge che così i transceiver elaborano in digitale direttamente l'inviluppo, «riducendo al minimo la parte di elaborazione analogica» (nota a mano).

Le note a mano della slide 7 raggruppano i passi in due **macroblocchi**:
- **modulatore** = DSP di trasmissione + upconversion;
- **demodulatore** = downconversion + DSP di ricezione.

Grazie a questa separazione gli algoritmi si sviluppano in banda base, indipendentemente dalla banda fisica usata. Nota a mano: «quindi ci si è svincolati dalla frequenza carrier ($f_c$)».

> 🧩 Conseguenza pratica (mia): $f_c$ compare solo nelle portanti $\sqrt2\cos(2\pi f_c t)$ e $-\sqrt2\sin(2\pi f_c t)$ dei due convertitori. Per trasmettere su un'altra banda basta cambiare quelle; il DSP resta identico.

## Connessioni

- [[inviluppo-complesso]] — l'upconversion realizza la (17), la downconversion la (15).
- [[segnale-analitico]] — la forma complessa della downconversion è la traslazione di $-f_c$ del segnale analitico.
- [[equivalente-banda-base-dei-filtri]] — la catena upconverter + canale + downconverter diventa un canale in banda base.
- [[modulazione-digitale]] — il modulatore fornisce $s_c$ e $s_s$ all'upconverter.
- [[segnali-banda-base-e-passa-banda]] — il requisito $W < f_c$ sul filtro viene dalla definizione di passa-banda.

## Fonti · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]–[[Rappresentazione_Rice.pdf#page=22|22]]

- [[rappresentazione-complessa-banda-base]]

_Aggiornato: 2026-09-28 — re-ingest del PDF con appunti: passaggio complesso ↔ reale (p.2), macroblocchi e svincolo da $f_c$ (p.10), «esce l'inviluppo» e «tagliati dal filtro» (p.20), nota di p.22; ruolo dei convertitori riformulato su slide 6–7; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
