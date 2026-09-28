---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=4", "Rappresentazione_Rice.pdf#page=5", "Rappresentazione_Rice.pdf#page=6", "Rappresentazione_Rice.pdf#page=7", "Rappresentazione_Rice.pdf#page=2"]
---

# Segnali in banda base e in banda passante

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=4]] (slide 3)

- Un segnale $s_b(t)$ è **in banda base** (*baseband*) se, per qualche $B > 0$,
$$S_b(f) \approx 0, \qquad |f| > B \tag{1}$$
- Un canale modellato come sistema **lineare tempo-invariante** (LTI) è in banda base se la sua funzione di trasferimento $H(f)$ soddisfa la (1).
- Un segnale $s_p(t)$ è **in banda passante** (*passband*) se
$$S_p(f) \approx 0, \qquad |f \pm f_c| > B/2 \tag{2}$$
  dove $f_c > B > 0$ si chiama frequenza **portante** (*carrier*).
- Un canale LTI è in banda passante se $H(f)$ soddisfa la (2).

> 🧩 Come leggere le due definizioni:
> - **"≈ 0", non "= 0".** I segnali reali sono solo *praticamente* limitati in banda: un segnale di durata finita non può avere banda rigorosamente limitata ([[Campionamento_AD_DA.pdf#page=20]], [[aliasing]]).
> - **"$|f \pm f_c| > B/2$"** va letto come "sia $|f - f_c| > B/2$ sia $|f + f_c| > B/2$". Lo spettro è praticamente nullo fuori dai due intervalli $(f_c - B/2,\ f_c + B/2)$ e $(-f_c - B/2,\ -f_c + B/2)$, cioè quando $\big||f| - f_c\big| > B/2$.
> - **$B$ ha lo stesso significato nelle due definizioni: la banda monolatera.** In banda base lo spettro occupa $(-B, B)$, quindi $B$ di frequenze positive. In banda passante il lobo positivo è largo $B$, da $f_c - B/2$ a $f_c + B/2$.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $S_b(f)\approx 0$ per $\|f\|>B$ | segnale (o canale) in banda base | [[Rappresentazione_Rice.pdf#page=4]] (slide 3) |
| $S_p(f)\approx 0$ per $\|f\pm f_c\|>B/2$, con $f_c>B>0$ | segnale (o canale) in banda passante | [[Rappresentazione_Rice.pdf#page=4]] (slide 3) |
| $X(f) = X^*(-f)$ | simmetria coniugata (hermitiana) di un segnale reale | [[Rappresentazione_Rice.pdf#page=5]] (slide 4), [[Rappresentazione_Rice.pdf#page=6]] (slide 5) |
| banda bilatera $= 2\times$ banda monolatera | vale per i segnali reali | [[Rappresentazione_Rice.pdf#page=6]] (slide 5) |
| $B/f_c \ll 1$ | segnale passa-banda **a banda stretta** | [[Rappresentazione_Rice.pdf#page=6]] (slide 5) |

Simboli: $B$ = banda monolatera [Hz]; $f_c$ = frequenza portante [Hz]; $S_b(f)$, $S_p(f)$, $X(f)$ = trasformate di Fourier (unità del segnale per secondo, es. V/Hz); $^*$ = complesso coniugato.

## Derivazioni

### Derivazione — Simmetria hermitiana di un segnale reale
**Fonte:** [[Rappresentazione_Rice.pdf#page=5]] (slide 4) e [[Rappresentazione_Rice.pdf#page=6]] (slide 5): proprietà usata senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
X(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{-j2\pi ft}\,dt && \text{definizione di trasformata} \\
X^*(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{+j2\pi ft}\,dt && \text{coniugo; } x(t) \text{ è reale, quindi } x^* = x \\
&= X(-f) && \text{è la stessa definizione calcolata in } -f \\
\Rightarrow\ X(f) &= X^*(-f) && \text{coniugo entrambi i membri}
\end{aligned}
$$

**Conseguenze**, scrivendo $X(-f) = X^*(f)$ per parte reale e parte immaginaria:
- $\text{Re}\,X(-f) = \text{Re}\,X(f)$: la parte reale è **pari**;
- $\text{Im}\,X(-f) = -\text{Im}\,X(f)$: la parte immaginaria è **dispari**;
- $|X(-f)| = |X(f)|$: il modulo è pari.

È quello che mostra la figura della slide 4. La metà a frequenze negative è l'immagine speculare (coniugata) di quella positiva: **non contiene informazione nuova**. È l'osservazione da cui nasce il [[segnale-analitico]].

### Derivazione — La banda bilatera è il doppio della monolatera
**Fonte:** [[Rappresentazione_Rice.pdf#page=6]] (slide 5)
> 🧩 Derivazione mia

Se le frequenze positive occupate formano un insieme di ampiezza $B$, per $|X(-f)| = |X(f)|$ le frequenze negative occupate ne sono lo specchio, e hanno ampiezza $B$ anch'esse. In totale: $2B$.
**Caso limite:** per un segnale **complesso** la simmetria non vale e le due metà sono indipendenti, quindi la regola del "doppio" non si applica (banda dei segnali complessi: [[inviluppo-complesso]]).

### Derivazione — Perché si chiede $f_c > B$
**Fonte:** [[Rappresentazione_Rice.pdf#page=4]] (slide 3), condizione data senza commento
> 🧩 Derivazione mia

$$
f_c > B \ \Rightarrow\ f_c - \frac{B}{2} > B - \frac{B}{2} = \frac{B}{2} > 0
$$

Il bordo inferiore del lobo positivo sta sopra $B/2 > 0$, e per simmetria il bordo superiore del lobo negativo sta sotto $-B/2$. I due lobi quindi **non si toccano e non contengono $f = 0$**. Senza questa condizione, "passa-banda" non avrebbe senso.

## Spiegazione

### Esempi di spettri (slide 4)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=5]] (slide 4)

La slide considera due segnali **reali**, $s_b(t)$ in banda base e $s_p(t)$ in banda passante. Le loro trasformate $S_b(f)$ e $S_p(f)$ possono esistere in senso ordinario o in **senso generalizzato**, per esempio con delta di Dirac. Per la simmetria coniugata $S_b(f) = S_b^*(-f)$ e $S_p(f) = S_p^*(-f)$.

![[rappresentazione-rice-p5-spettri-banda-base-passa-banda.png]]
*[[Rappresentazione_Rice.pdf#page=5]] (slide 4). A sinistra, il segnale in banda base: $\text{Re}(S(f))$ è un triangolo di altezza 1 su $(-B, B)$, pari (nota a mano: "simmetria hermitiana"); $\text{Im}(S(f))$ vale $+1$ su $(-B, 0)$ e $-1$ su $(0, B)$, dispari. A destra, il segnale passa-banda: stesse forme spostate attorno a $\pm f_c$, larghezza $B$. La parte reale è pari e quella immaginaria dispari. Nota a mano con $f_c$ cerchiato: "l'obiettivo è sbarazzarsi di $f_c$".*

> 💡 Connessione: "l'obiettivo è sbarazzarsi di $f_c$" è il programma della lezione. L'informazione di $s_p(t)$ non dipende da $f_c$ ([[Rappresentazione_Rice.pdf#page=19]], slide 15), e si può descrivere tutto con un segnale in banda base: l'[[inviluppo-complesso]].

> ⚠️ Nella figura il segnale in banda base è indicato con $S(f)$ invece di $S_b(f)$. Più avanti, nella slide 11, $S(f)$ indica l'inviluppo complesso.

### Banda (slide 5)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=6]] (slide 5)

- La **banda** è l'ampiezza dell'intervallo di frequenze occupato dalla trasformata di Fourier.
- **Banda monolatera** (*one-sided*): occupazione spettrale sulle frequenze positive.
- **Banda bilatera** (*two-sided*): occupazione su frequenze positive e negative.
- Per i segnali **reali** la bilatera è il doppio della monolatera, per la simmetria coniugata $X(f) = X^*(-f)$.
- Di solito "banda" senza aggettivi indica la **monolatera**.
- Un segnale passa-banda è **a banda stretta** (*narrowband*) se $B/f_c \ll 1$. Da qui in poi si considerano solo segnali passa-banda a banda stretta.

> 🧩 Con gli spettri della slide 4: il segnale in banda base ha banda monolatera $B$ e bilatera $2B$. Il passa-banda ha banda monolatera $B$ (il lobo positivo) e bilatera $2B$ (i due lobi).

### Segnale a banda stretta (appunti p.7)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=7]] (appunti a mano)

![[rappresentazione-rice-p7-appunti-banda-stretta.png]]
*Appunti a mano, [[Rappresentazione_Rice.pdf#page=7]]: un segnale a banda stretta ha banda molto minore di $f_c$ ($B \ll f_c$): due lobi stretti attorno a $\pm f_c$.*

> 🧩 Perché l'ipotesi di banda stretta aiuta, anticipando i risultati della lezione:
> - $s_p(t)$ appare come una portante a $f_c$ con ampiezza e fase che cambiano lentamente ([[inviluppo-complesso]]);
> - nella downconversion i termini a $2f_c$ cadono lontanissimi dalla banda base e si filtrano con facilità ([[upconversion-e-downconversion]]).

### Canale passa-banda (appunti p.2)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano)

Il disegno di p.2 ([[modulazione-digitale]]) mostra la $H(f)$ di un canale passa-banda: due lobi di larghezza $B$, la "banda utile", centrati in $\pm f_c$. Il trasmettitore deve portare il segnale in quella porzione di spettro, per adattarlo al canale. Il ricevitore lo riporta in banda base, "e questo rende il segnale complesso" ([[inviluppo-complesso]]).

> 🎯 Esame: dare le definizioni (1) e (2), spiegare banda monolatera e bilatera e perché per i segnali reali una è il doppio dell'altra, definire la banda stretta.

## Perché importa

I canali passa-banda sono molto usati ([[Rappresentazione_Rice.pdf#page=8]], slide 6), quindi bisogna saper trasmettere e ricevere segnali passa-banda. Le definizioni fissano la notazione ($B$, $f_c$) di tutta la lezione. L'ipotesi di banda stretta è usata in tutti i risultati successivi.

## Connessioni

- [[teorema-del-campionamento]] — stessa nozione di segnale a banda limitata: la $f_m$ di quella lezione è la $B$ del segnale in banda base.
- [[aliasing]] — il "≈ 0": i segnali di durata finita sono solo praticamente limitati in banda.
- [[segnale-analitico]] — sfrutta la simmetria hermitiana: la metà negativa dello spettro è ridondante e si scarta.
- [[inviluppo-complesso]] — rappresentazione in banda base di un segnale passa-banda a banda stretta.
- [[modulazione-digitale]] — il modulatore deve collocare il segnale nella banda passante del canale.

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=4]] – [[Rappresentazione_Rice.pdf#page=7]] (slide 3–5, con appunti a mano a p.7); [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano)

_Aggiornato: 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
