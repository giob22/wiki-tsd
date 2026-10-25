---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=4", "Rappresentazione_Rice.pdf#page=5", "Rappresentazione_Rice.pdf#page=7", "Rappresentazione_Rice.pdf#page=8", "Rappresentazione_Rice.pdf#page=2"]
---

# Segnali in banda base e in banda passante

## Definizione · Rice [[Rappresentazione_Rice.pdf#page=4|p. 4]] · Campionamento [[Campionamento_AD_DA.pdf#page=20|p. 20]]

- Un segnale $s_b(t)$ è **in banda base** (*baseband*) se, per qualche $B > 0$,
$$S_b(f) \approx 0, \qquad |f| > B \tag{1}$$
- Un canale modellato come sistema **lineare tempo-invariante** (LTI) è in banda base se la sua funzione di trasferimento $H(f)$ soddisfa la (1).
- Un segnale $s_p(t)$ è **in banda passante** (*passband*) se
$$S_p(f) \approx 0, \qquad |f \pm f_c| > B/2 \tag{2}$$
  dove $f_c > B > 0$ si chiama frequenza **portante** (*carrier*). Nota a mano sulla slide: si dice banda passante perché «il contenuto informativo è traslato e centrato attorno a $f_c$».
- Un canale LTI è in banda passante se $H(f)$ soddisfa la (2).

> 🧩 Come leggere le due definizioni:
> - **"≈ 0", non "= 0".** I segnali reali sono solo *praticamente* limitati in banda: un segnale di durata finita non può avere banda rigorosamente limitata ([[aliasing]]).
> - **"$|f \pm f_c| > B/2$"** va letto come "sia $|f - f_c| > B/2$ sia $|f + f_c| > B/2$". Lo spettro è praticamente nullo fuori dai due intervalli $(f_c - B/2,\ f_c + B/2)$ e $(-f_c - B/2,\ -f_c + B/2)$, cioè quando $\big||f| - f_c\big| > B/2$.
> - **$B$ ha lo stesso significato nelle due definizioni: la banda monolatera.** In banda base lo spettro occupa $(-B, B)$, quindi $B$ di frequenze positive. In banda passante il lobo positivo è largo $B$, da $f_c - B/2$ a $f_c + B/2$.

## Formule · [[Rappresentazione_Rice.pdf#page=4|p. 4]], [[Rappresentazione_Rice.pdf#page=5|5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]]

| Formula | Significato |
|---|---|
| $S_b(f)\approx 0$ per $\lvert f\rvert>B$ | segnale (o canale) in banda base |
| $S_p(f)\approx 0$ per $\lvert f\pm f_c\rvert>B/2$, con $f_c>B>0$ | segnale (o canale) in banda passante |
| $X(f) = X^\ast (-f)$ | simmetria coniugata (hermitiana) di un segnale reale |
| banda bilatera $= 2\times$ banda monolatera | vale per i segnali reali |
| $B/f_c \ll 1$ | segnale passa-banda **a banda stretta** |

Simboli: $B$ = banda monolatera [Hz]; $f_c$ = frequenza portante [Hz]; $S_b(f)$, $S_p(f)$, $X(f)$ = trasformate di Fourier (unità del segnale per secondo, es. V/Hz); $^\ast$ = complesso coniugato.

## Derivazioni

### Derivazione — Simmetria hermitiana di un segnale reale · [[Rappresentazione_Rice.pdf#page=5|p. 5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]]
**Fonte:** proprietà usata senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
X(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{-j2\pi ft}\,dt && \text{definizione di trasformata} \\
X^*(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{+j2\pi ft}\,dt && \text{coniugo; } x(t) \text{ è reale, quindi } x^* = x \\
&= X(-f) && \text{è la stessa definizione calcolata in } -f \\
\Rightarrow\ X(f) &= X^*(-f) && \text{coniugo entrambi i membri}
\end{aligned}
$$

**Conseguenze**, scrivendo $X(-f) = X^\ast (f)$ per parte reale e parte immaginaria:
- $\text{Re}\,X(-f) = \text{Re}\,X(f)$: la parte reale è **pari**;
- $\text{Im}\,X(-f) = -\text{Im}\,X(f)$: la parte immaginaria è **dispari**;
- $|X(-f)| = |X(f)|$: il modulo è pari.

È quello che mostra la figura della slide 4. La metà a frequenze negative è l'immagine speculare (coniugata) di quella positiva: **non contiene informazione nuova**. È l'osservazione da cui nasce il [[segnale-analitico]].

### Derivazione — La banda bilatera è il doppio della monolatera · [[Rappresentazione_Rice.pdf#page=7|p. 7]]
> 🧩 Derivazione mia

Se le frequenze positive occupate formano un insieme di ampiezza $B$, per $|X(-f)| = |X(f)|$ le frequenze negative occupate ne sono lo specchio, e hanno ampiezza $B$ anch'esse. In totale: $2B$.
**Caso limite:** per un segnale **complesso** la simmetria non vale e le due metà sono indipendenti, quindi la regola del "doppio" non si applica (banda dei segnali complessi: [[inviluppo-complesso]]).

### Derivazione — Perché si chiede $f_c > B$ · [[Rappresentazione_Rice.pdf#page=4|p. 4]]
**Fonte:** condizione data senza commento. Accanto c'è una nota a mano rimasta incompleta («altrimenti c'è…»).
> 🧩 Derivazione mia: cosa succederebbe altrimenti.

$$
f_c > B \ \Rightarrow\ f_c - \frac{B}{2} > B - \frac{B}{2} = \frac{B}{2} > 0
$$

Il bordo inferiore del lobo positivo sta sopra $B/2 > 0$, e per simmetria il bordo superiore del lobo negativo sta sotto $-B/2$. I due lobi quindi **non si toccano e non contengono $f = 0$**. Senza questa condizione, "passa-banda" non avrebbe senso.

![[grafico-rice-condizione-passabanda.png|550]]
*🧩 Grafico mio (script `output/grafici/genera_grafico_condizione_passabanda.py`): stessi due lobi larghi $B$ in $\pm f_c$, con la portante sempre più bassa. La riga tratteggiata colorata segna il bordo inferiore del lobo positivo, $f_c - B/2$.*
- *(a) $f_c = 2B$: bordo a $1.5B$, i lobi sono lontanissimi dall'origine.*
- *(b) $f_c = B$, la soglia della slide: bordo a $B/2$. Attorno a $f = 0$ resta libera una fascia larga $B$, da $-B/2$ a $B/2$.*
- *(c) $f_c = B/2$: bordo a 0, i due lobi si toccano proprio in $f = 0$. È il limite oltre il quale smettono di essere separati.*
- *(d) $f_c = B/4$: bordo a $-0.25B$. I lobi si sovrappongono attorno all'origine, e la loro somma (tratteggiata nera) ha contenuto anche in $f = 0$: è uno spettro in banda base, non più un segnale passa-banda.*

> 🧩 Osservazione mia: per tenere separati i lobi basterebbe $f_c > B/2$, cioè il caso (c) escluso. La slide chiede di più, $f_c > B$, e quindi lascia sempre libera attorno all'origine almeno una fascia larga $B$, come nel caso (b).

## Spiegazione

### Esempi di spettri (slide 4) · [[Rappresentazione_Rice.pdf#page=5|p. 5]], [[Rappresentazione_Rice.pdf#page=22|p. 22]]

La slide considera due segnali **reali**, $s_b(t)$ in banda base e $s_p(t)$ in banda passante. Le loro trasformate $S_b(f)$ e $S_p(f)$ possono esistere in senso ordinario o in **senso generalizzato**, per esempio con delta di Dirac. Per la simmetria coniugata $S_b(f) = S_b^\ast (-f)$ e $S_p(f) = S_p^\ast (-f)$.

![[rappresentazione-rice-p5-spettri-banda-base-passa-banda.png]]
- *A sinistra, il segnale in banda base. $\text{Re}(S(f))$ è un triangolo di altezza 1 su $(-B, B)$, pari. $\text{Im}(S(f))$ vale $+1$ su $(-B, 0)$ e $-1$ su $(0, B)$, dispari.*
- *A destra, il segnale passa-banda: stesse forme spostate attorno a $\pm f_c$, larghezza $B$; parte reale pari, parte immaginaria dispari.*
- *Note a mano: «le trasformate di Fourier dei segnali reali godono della simmetria hermitiana». Con $f_c$ cerchiato: «l'obiettivo è svincolarsi dalla $f_c$, ovvero dalla frequenza carrier, perché l'informazione di $s(t)$ non dipende da $f_c$: si può descrivere tutto con un segnale in banda base».*

> 💡 Connessione: "svincolarsi da $f_c$" è il programma della lezione. L'informazione di $s_p(t)$ non dipende da $f_c$, quindi si può descrivere tutto con un segnale in banda base: l'[[inviluppo-complesso]].

> ⚠️ Nella figura il segnale in banda base è indicato con $S(f)$ invece di $S_b(f)$. Più avanti, nella slide 11, $S(f)$ indica l'inviluppo complesso.

### Banda (slide 5) · [[Rappresentazione_Rice.pdf#page=7|p. 7]]

- La **banda** è l'ampiezza dell'intervallo di frequenze occupato dalla trasformata di Fourier.
- **Banda monolatera** (*one-sided*): occupazione spettrale sulle frequenze positive.
- **Banda bilatera** (*two-sided*): occupazione su frequenze positive e negative.
- Per i segnali **reali** la bilatera è il doppio della monolatera, per la simmetria coniugata $X(f) = X^\ast (-f)$.
- Di solito "banda" senza aggettivi indica la **monolatera**.
- Un segnale passa-banda è **a banda stretta** (*narrowband*) se $B/f_c \ll 1$. Da qui in poi si considerano solo segnali passa-banda a banda stretta.

> 🧩 Con gli spettri della slide 4: il segnale in banda base ha banda monolatera $B$ e bilatera $2B$. Il passa-banda ha banda monolatera $B$ (il lobo positivo) e bilatera $2B$ (i due lobi).

### Definizioni negli appunti e banda stretta (appunti p.8) · [[Rappresentazione_Rice.pdf#page=8|p. 8]]

Gli appunti riprendono in italiano le definizioni della slide 5:
- **larghezza di banda**: dimensione dell'intervallo di frequenze occupato dalla trasformata di Fourier del segnale;
- si distingue tra banda **monolatera** e **bilatera**; la bilatera considera sia le frequenze positive sia quelle negative;
- se $s(t)$ è reale, la bilatera è il doppio della monolatera, per la simmetria hermitiana $S(f) = S^\ast (-f)$;
- **segnale passa-banda a banda stretta**: la sua banda $B$ è molto minore della frequenza portante, $B/f_c \ll 1$. Nota: **non è un'ipotesi stringente**.

![[rappresentazione-rice-p8-appunti-banda-stretta.png]]
*Appunti a mano: un segnale a banda stretta ha banda molto minore di $f_c$ ($B \ll f_c$), cioè due lobi stretti attorno a $\pm f_c$. Sotto, le definizioni di larghezza di banda, banda monolatera e bilatera e segnale a banda stretta.*

> 🧩 Perché "non è un'ipotesi stringente" (lettura mia): nei sistemi reali la portante è molto più alta della banda del segnale. È lo stesso ordine di grandezza del grafico I/Q di [[inviluppo-complesso]], dove per rendere visibili le oscillazioni si è dovuta scegliere una $f_c$ artificialmente bassa.

> 🧩 Perché l'ipotesi di banda stretta aiuta, anticipando i risultati della lezione:
> - $s_p(t)$ appare come una portante a $f_c$ con ampiezza e fase che cambiano lentamente ([[inviluppo-complesso]]);
> - nella downconversion i termini a $2f_c$ cadono lontanissimi dalla banda base e si filtrano con facilità ([[upconversion-e-downconversion]]).

### Canale passa-banda (appunti p.2) · [[Rappresentazione_Rice.pdf#page=2|p. 2]]

Il disegno di p.2 ([[modulazione-digitale]]) mostra la $H(f)$ di un canale passa-banda: due lobi di larghezza $B$, la "banda utile", centrati in $\pm f_c$.
- Il segnale attraversa il canale, che è caratterizzato da una sua risposta in frequenza e da una determinata banda a disposizione.
- Il trasmettitore deve portare il segnale in quella porzione di spettro, per adattarlo al canale.
- Il ricevitore lo riporta in banda base, «e questo rende il segnale complesso» ([[inviluppo-complesso]]).

> 🎯 Esame: dare le definizioni (1) e (2), spiegare banda monolatera e bilatera e perché per i segnali reali una è il doppio dell'altra, definire la banda stretta.

## Perché importa · [[Rappresentazione_Rice.pdf#page=9|p. 9]]

I canali passa-banda sono molto usati, quindi bisogna saper trasmettere e ricevere segnali passa-banda. Le definizioni fissano la notazione ($B$, $f_c$) di tutta la lezione. L'ipotesi di banda stretta è usata in tutti i risultati successivi.

## Connessioni

- [[teorema-del-campionamento]] — stessa nozione di segnale a banda limitata: la $f_m$ di quella lezione è la $B$ del segnale in banda base.
- [[aliasing]] — il "≈ 0": i segnali di durata finita sono solo praticamente limitati in banda.
- [[segnale-analitico]] — sfrutta la simmetria hermitiana: la metà negativa dello spettro è ridondante e si scarta.
- [[inviluppo-complesso]] — rappresentazione in banda base di un segnale passa-banda a banda stretta.
- [[modulazione-digitale]] — il modulatore deve collocare il segnale nella banda passante del canale.

## Fonti · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=4|p. 4]], [[Rappresentazione_Rice.pdf#page=5|5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]], [[Rappresentazione_Rice.pdf#page=8|8]]

- [[rappresentazione-complessa-banda-base]]

_Aggiornato: 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-10-16 — grafico della condizione f_c > B (quattro casi); 2026-10-14 — formule nelle tabelle: modulo scritto con \lvert \rvert e condizionamento con \mid (il \| non si leggeva bene); 2026-09-28 — re-ingest del PDF con nuovi appunti: definizione di banda passante, simmetria hermitiana, "svincolarsi da $f_c$", definizioni negli appunti, banda stretta "non stringente"; pagine rimappate; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
