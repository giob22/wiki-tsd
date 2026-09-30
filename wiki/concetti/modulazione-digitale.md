---
tipo: concetto
importanza_esame: media
prerequisiti: ["sistema-comunicazione-digitale"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=2", "Rappresentazione_Rice.pdf#page=3", "Rappresentazione_Rice.pdf#page=10", "Intro.pdf#page=16"]
---

# Modulazione digitale

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=3]] (slide 2)

La **modulazione** è la rappresentazione dell'informazione digitale con **forme d'onda analogiche** che si possono trasmettere su canali fisici. Nota a mano sulla slide: è «il processo che permette di rappresentare l'informazione digitale tramite forme d'onda analogiche». È il compito del blocco **modulatore** dello schema del sistema digitale ([[sistema-comunicazione-digitale]], [[Intro.pdf#page=16]]).

Gli appunti a mano di [[Rappresentazione_Rice.pdf#page=2]] (pagina di appunti, prima della slide 2) mettono il modulatore nella catena:
- la sorgente produce $s(n)$, un segnale già ridotto a stringhe di bit;
- il modulatore (MOD) **associa una forma d'onda analogica a ogni simbolo o stringa di bit** e produce $s(t)$, che va sul canale fisico;
- deve **allocare** questo segnale in una specifica porzione dello spettro delle frequenze, **centrata attorno a una frequenza portante** $f_c$ (*carrier*);
- il segnale attraversa poi il **canale**, caratterizzato da una sua risposta in frequenza e da una determinata banda a disposizione.

Sempre negli appunti di p.2: sia in trasmissione sia in ricezione c'è un passaggio tra segnale complesso e segnale reale, ed è eseguito da un DSP.
- **In trasmissione:** complesso → reale.
- **In ricezione:** reale → complesso.

Il perché è in [[inviluppo-complesso]] e [[upconversion-e-downconversion]].

![[rappresentazione-rice-p2-appunti-sistema-e-canale.png]]
*Appunti a mano, [[Rappresentazione_Rice.pdf#page=2]].*
- *In alto a sinistra: sorgente S → $s(n)$ → MOD → $s(t)$ → canale fisico, con la definizione del modulatore.*
- *A destra: risposta in frequenza $H(f)$ di un canale passa-banda, con due lobi di larghezza $B$ (la "banda utile") centrati in $\pm f_c$, dove $f_c$ è la portante.*
- *Sotto: il trasmettitore porta il segnale nella porzione di spettro prevista, per adattarlo al canale; il ricevitore lo riporta in banda base, e questo rende il segnale complesso. Il passaggio complesso ↔ reale avviene in entrambe le fasi.*

> ⚠️ Nel disegno il lobo di sinistra è etichettato $f_c$: è il lobo in $-f_c$.

## Formule

La slide descrive la modulazione lineare a parole; la formula è scritta a mano accanto alla figura ([[Rappresentazione_Rice.pdf#page=3]]):
$$s(t) = \sum_{m} b[m]\,\Pi(t - mT), \qquad b \in \{-1, 1\}$$
- $b[m] \in \{-1, +1\}$: simboli, adimensionali;
- $\Pi$: impulso rettangolare, di durata $T$ nell'esempio della slide; è adimensionale, perché l'ampiezza del segnale la danno i simboli;
- $T$: intervallo di simbolo [s]; $\Pi(t - mT)$ è la copia dell'impulso traslata all'intervallo $m$-esimo.

> ⚠️ Negli appunti la somma è scritta da $i = 1$ a $m$, ma il termine dipende da $m$: la somma va letta sull'indice $m$ dei simboli.
> 🧩 Scrittura generale (mia), usata in [[calcolo-densita-spettrale]]: con un impulso qualunque $p(t)$ al posto del rettangolo, $s(t) = \sum_m b[m]\,p(t - mT)$.

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

- I simboli (bit) diventano una forma d'onda analogica moltiplicando ogni simbolo per una copia traslata di un impulso rettangolare: è la **modulazione lineare**. Nota a mano: si chiama così «perché $s(t)$ dipende linearmente dai simboli».
- La forma d'onda dell'esempio è **limitata nel tempo**. Le forme d'onda usate davvero per modulare, però, sono spesso **vincolate nel dominio della frequenza**:
  - per le caratteristiche fisiche del mezzo di comunicazione;
  - per fattori esterni, per esempio le **regole sull'uso dello spettro**.
- Note a mano ([[Rappresentazione_Rice.pdf#page=3]]): i segnali di comunicazione devono essere allocati in certe porzioni dello spettro. I segnali da trasmettere sul canale devono soddisfare **vincoli nel dominio della frequenza**, che riguardano **dove** è allocato il loro spettro.

> 🧩 Cosa vuol dire "dipende linearmente": moltiplicare tutti i $b[m]$ per una costante moltiplica $s(t)$ per la stessa costante, e la forma d'onda di una somma di sequenze di simboli è la somma delle forme d'onda.

### Dove deve finire il segnale modulato
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=10]] (slide 7), [[Rappresentazione_Rice.pdf#page=20]] (slide 14, nota a mano)

Il canale del disegno di p.2 lascia passare solo le frequenze attorno a $\pm f_c$: il segnale trasmesso deve quindi essere **in banda passante** ([[segnali-banda-base-e-passa-banda]]). Nello schema modulare della lezione:
1. il DSP del trasmettitore esegue codifica, modulazione e filtraggio **in banda base**, producendo l'inviluppo complesso ([[inviluppo-complesso]], slide 7);
2. l'upconverter lo porta in banda passante ([[upconversion-e-downconversion]]).

Note a mano sulla slide 7 ([[Rappresentazione_Rice.pdf#page=10]]):
- il **modulatore** è il macroblocco che comprende entrambi i passi, cioè il DSP e anche l'upconversion;
- il **demodulatore** è il macroblocco speculare: downconversion e DSP.

Nella figura della slide 14 ([[Rappresentazione_Rice.pdf#page=20]]) una nota a mano collega S → $s(n)$ → MOD alle due uscite $s_c(t)$ e $s_s(t)$ che entrano nell'upconverter. Dal modulatore «esce l'inviluppo».

## Perché importa

La modulazione digitale è il terzo tema del programma ([[Intro.pdf#page=3]]). In questa lezione fa da motivazione: il modulatore deve produrre forme d'onda che stiano in una precisa porzione di spettro, e per descriverle e generarle serve la rappresentazione complessa in banda base.

## Connessioni

- [[sistema-comunicazione-digitale]] — il modulatore è un blocco dello schema ([[Intro.pdf#page=16]]).
- [[segnali-banda-base-e-passa-banda]] — il segnale modulato deve occupare la banda passante del canale.
- [[inviluppo-complesso]] — il modulatore lavora sull'inviluppo complesso; l'upconverter lo porta a $f_c$.
- [[upconversion-e-downconversion]] — lo stadio che segue il modulatore.
- [[aliasing]] — un impulso limitato nel tempo non è a banda limitata, come i segnali di [[Campionamento_AD_DA.pdf#page=20]].
- [[calcolo-densita-spettrale]] — la PSD del segnale modulato linearmente è $\frac{\sigma_b^2}{T}|P(f)|^2$, con l'impulso rettangolare $\sigma_b^2 T\,\text{sinc}^2(fT)$ (esempio di [[random_processes.pdf#page=37]]).

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=2]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=3]] (slide 2), [[Rappresentazione_Rice.pdf#page=10]] (slide 7), [[Rappresentazione_Rice.pdf#page=20]] (slide 14)

_Aggiornato: 2026-09-28 — re-ingest del PDF con nuovi appunti: formula della modulazione lineare della docente, definizione estesa del modulatore, macroblocchi; pagine rimappate. Prima, nello stesso giorno: collegamento alla PSD del segnale modulato linearmente; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
