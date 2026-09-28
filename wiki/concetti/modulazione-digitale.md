---
tipo: concetto
importanza_esame: media
prerequisiti: ["sistema-comunicazione-digitale"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=2", "Rappresentazione_Rice.pdf#page=3", "Intro.pdf#page=16"]
---

# Modulazione digitale

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=3]] (slide 2)

La **modulazione** è la rappresentazione dell'informazione digitale con **forme d'onda analogiche** che si possono trasmettere su canali fisici. È il compito del blocco **modulatore** dello schema del sistema digitale ([[sistema-comunicazione-digitale]], [[Intro.pdf#page=16]]).

Gli appunti a mano di [[Rappresentazione_Rice.pdf#page=2]] (pagina di appunti, prima della slide 2) mettono il modulatore nella catena:
- la sorgente produce $s(n)$, un segnale già ridotto a stringhe di bit;
- il modulatore (MOD) **associa una forma d'onda a ogni stringa di bit** e produce $s(t)$, che va sul canale fisico;
- il modulatore deve anche **portare il segnale in un certo intervallo di frequenze**, quello in cui il canale lo lascia passare.

![[rappresentazione-rice-p2-appunti-sistema-e-canale.png]]
*Appunti a mano, [[Rappresentazione_Rice.pdf#page=2]]. A sinistra: sorgente S → $s(n)$ → MOD → $s(t)$ → canale fisico. A destra: risposta in frequenza $H(f)$ di un canale passa-banda, con due lobi di larghezza $B$ (la "banda utile") centrati in $\pm f_c$, dove $f_c$ è la portante (*carrier*). Sotto: il trasmettitore porta il segnale nella porzione di spettro prevista, per adattarlo al canale; il ricevitore lo riporta in banda base, e questo rende il segnale complesso ([[inviluppo-complesso]]).*

> ⚠️ Nel disegno il lobo di sinistra è etichettato $f_c$: è il lobo in $-f_c$.

## Formule

La slide descrive la modulazione lineare a parole, senza formula.

> 🧩 Formalizzazione mia della frase della slide («each symbol multiplies translates of a rectangular pulse»):
> $$s(t) = \sum_{n} b[n]\,p(t - nT)$$
> - $b[n] \in \{+1, -1\}$: simboli, adimensionali;
> - $p(t)$: impulso rettangolare di durata $T$, adimensionale (l'ampiezza del segnale la danno i simboli);
> - $T$: intervallo di simbolo [s]; $p(t - nT)$ è la copia di $p$ traslata all'intervallo $n$-esimo.
>
> Vale per l'esempio della slide: modulazione lineare binaria con impulso rettangolare.

## Derivazioni

### Derivazione — Spettro dell'impulso rettangolare
**Fonte:** [[Rappresentazione_Rice.pdf#page=3]] (slide 2): la slide contrappone la forma d'onda dell'esempio, «limitata nel tempo», alle forme d'onda reali, spesso «vincolate in frequenza». Qui si vede perché le due cose non vanno d'accordo.
> 🧩 Derivazione mia. Impulso $p(t) = 1$ per $|t| < T/2$, 0 altrove.

$$
\begin{aligned}
P(f) &= \int_{-T/2}^{T/2} e^{-j2\pi ft}\,dt && \text{definizione di trasformata, } p = 1 \text{ solo in } |t| < T/2 \\
&= \frac{e^{-j\pi fT} - e^{j\pi fT}}{-j2\pi f} && \text{primitiva di } e^{-j2\pi ft} \text{ è } e^{-j2\pi ft}/(-j2\pi f) \\
&= \frac{\sin(\pi fT)}{\pi f} && e^{jx} - e^{-jx} = 2j\sin x \\
&= T\,\text{sinc}(fT) && \text{sinc}(x) = \sin(\pi x)/(\pi x)
\end{aligned}
$$

**Risultato:** $|P(f)|$ si annulla solo nei punti $f = k/T$ ($k \neq 0$) e tra uno zero e l'altro decresce solo come $1/(\pi|f|)$: non esiste una $B$ oltre la quale $P(f) = 0$. L'impulso rettangolare, limitato nel tempo, **non è a banda limitata**.
**Sanity check:** $P(0) = T$, cioè l'area dell'impulso ✓. È lo stesso fatto di [[Campionamento_AD_DA.pdf#page=20]]: un segnale di durata finita non può avere banda rigorosamente limitata ([[aliasing]]).
**Ipotesi:** impulso rettangolare ideale (fronti verticali).

## Spiegazione

### L'esempio della slide: modulazione lineare binaria
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=3]] (slide 2)

![[rappresentazione-rice-p3-modulazione-binaria.png]]
*[[Rappresentazione_Rice.pdf#page=3]] (slide 2). La sequenza di simboli +1, −1, −1, +1, +1, +1, −1, +1, −1, +1, +1, … diventa una forma d'onda a gradini: ogni simbolo moltiplica un impulso rettangolare traslato. Nota a mano sotto la figura: i segnali di comunicazione devono essere allocati in certe porzioni dello spettro.*

- I simboli (bit) diventano una forma d'onda analogica moltiplicando ogni simbolo per una copia traslata di un impulso rettangolare: è la **modulazione lineare**.
- La forma d'onda dell'esempio è **limitata nel tempo**. Le forme d'onda usate davvero per modulare, però, sono spesso **vincolate nel dominio della frequenza**:
  - per le caratteristiche fisiche del mezzo di comunicazione;
  - per fattori esterni, per esempio le **regole sull'uso dello spettro**.
- Nota a mano ([[Rappresentazione_Rice.pdf#page=3]]): i segnali di comunicazione devono essere allocati in certe porzioni dello spettro.

> 🧩 Perché si chiama "lineare": $s(t)$ dipende linearmente dai simboli. Moltiplicare tutti i $b[n]$ per una costante moltiplica $s(t)$ per la stessa costante, e la forma d'onda di una somma di sequenze è la somma delle forme d'onda.

### Dove deve finire il segnale modulato
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=9]] (slide 7), [[Rappresentazione_Rice.pdf#page=17]] (slide 14, nota a mano)

Il canale del disegno di p.2 lascia passare solo le frequenze attorno a $\pm f_c$: il segnale trasmesso deve quindi essere **in banda passante** ([[segnali-banda-base-e-passa-banda]]). Nello schema modulare della lezione:
1. il DSP del trasmettitore esegue codifica, modulazione e filtraggio **in banda base**, producendo l'inviluppo complesso ([[inviluppo-complesso]], slide 7);
2. l'upconverter lo porta in banda passante ([[upconversion-e-downconversion]]).

Nella figura della slide 14 una nota a mano collega proprio S → $s(n)$ → MOD alle due uscite $s_c(t)$ e $s_s(t)$ che entrano nell'upconverter.

## Perché importa

La modulazione digitale è il terzo tema del programma ([[Intro.pdf#page=3]]). In questa lezione fa da motivazione: il modulatore deve produrre forme d'onda che stiano in una precisa porzione di spettro, e per descriverle e generarle serve la rappresentazione complessa in banda base.

## Connessioni

- [[sistema-comunicazione-digitale]] — il modulatore è un blocco dello schema ([[Intro.pdf#page=16]]).
- [[segnali-banda-base-e-passa-banda]] — il segnale modulato deve occupare la banda passante del canale.
- [[inviluppo-complesso]] — il modulatore lavora sull'inviluppo complesso; l'upconverter lo porta a $f_c$.
- [[upconversion-e-downconversion]] — lo stadio che segue il modulatore.
- [[aliasing]] — un impulso limitato nel tempo non è a banda limitata, come i segnali di [[Campionamento_AD_DA.pdf#page=20]].
- [[calcolo-densita-spettrale]] — la PSD del segnale modulato linearmente è $\frac{\sigma_b^2}{T}|P(f)|^2$, con l'impulso rettangolare $\sigma_b^2 T\,\text{sinc}^2(fT)$ (esempio di [[random_processes.pdf#page=32]]).

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=3]] (slide 2)

_Aggiornato: 2026-09-28 — collegamento alla PSD del segnale modulato linearmente; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
