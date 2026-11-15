---
tipo: concetto
importanza_esame: alta
prerequisiti: ["coppie-di-variabili-aleatorie", "rumore-in-banda-passante", "processo-gaussiano"]
fonti_pdf: ["Confronto_new.pdf#page=3", "Confronto_new.pdf#page=4", "Confronto_new.pdf#page=5", "Confronto_new.pdf#page=6", "Confronto_new.pdf#page=7", "Confronto_new.pdf#page=8", "Confronto_new.pdf#page=9"]
---

# Informazione mutua e capacità di canale

## Definizione · [[Confronto_new.pdf#page=3|p. 3]]–[[Confronto_new.pdf#page=7|7]]

L'**informazione mutua** $I(X;Y)$ tra l'ingresso $X$ e l'uscita $Y$ di un canale senza memoria è la quantità media di informazione che l'osservazione di $Y$ fornisce su $X$, cioè la riduzione media dell'incertezza su $X$ dovuta all'osservazione dell'uscita. La **capacità** $C$ è il massimo dell'informazione mutua al variare della distribuzione dell'ingresso. Per il **secondo teorema di Shannon** è la massima velocità a cui si può trasmettere con probabilità d'errore piccola a piacere, senza vincoli di complessità o ritardo.

## Formule · [[Confronto_new.pdf#page=4|p. 4]]–[[Confronto_new.pdf#page=9|9]]

| Formula | Significato |
|---|---|
| $I(X;Y)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}$ | informazione mutua [bit] |
| $I(X;Y)=H(Y)-H(Y\mid X)=H(X)-H(X\mid Y)$ | legame con le entropie |
| $C=\max_{p(x)}I(X;Y)$ | capacità [bit/uso del canale; bit/s a tempo continuo] |
| $R_b<C$: errore piccolo a piacere; $R_b>C$: impossibile | secondo teorema di Shannon |
| $\gamma=\frac{P}{N_0W}$, $C=W\log_2(1+\gamma)$ | capacità del canale AWGN [bit/s] |
| $\frac CW=\log_2(1+\gamma)$ | capacità per unità di banda [bit/s/Hz] |

> 🧮 Formula chiave: $C=W\log_2\Big(1+\dfrac{P}{N_0W}\Big)$ bit/s. Il risultato **non va dimostrato** (nota della docente).

Simboli: $p(x,y)$ distribuzione congiunta di ingresso e uscita, $p(x)$ e $p(y)$ le marginali; $H(\cdot)$ entropia in bit; $W$ [Hz] banda disponibile; $P$ [W] potenza media trasmessa; $N_0$ [W/Hz] densità spettrale del rumore; $\gamma$ SNR (adimensionale); $R_b$ [bit/s] bit rate.

## Derivazioni

### Derivazione — Informazione mutua ed entropie · [[Confronto_new.pdf#page=5|p. 5]]
**Fonte:** la slide dà il risultato «usando $p(x,y)=p(y\mid x)p(x)$».
**Si parte da:** la definizione di $I(X;Y)$ e dalle entropie $H(Y)=-\sum_yp(y)\log_2p(y)$, $H(Y\mid X)=-\sum_{x,y}p(x,y)\log_2p(y\mid x)$.

$$
\begin{aligned}
I(X;Y)&=\sum_{x,y}p(x,y)\log_2\frac{p(y\mid x)\,p(x)}{p(x)\,p(y)} && p(x,y)=p(y\mid x)\,p(x)\\
&=\sum_{x,y}p(x,y)\log_2p(y\mid x)-\sum_{x,y}p(x,y)\log_2p(y) && \log\tfrac ab=\log a-\log b\\
&=-H(Y\mid X)-\sum_yp(y)\log_2p(y) && \textstyle\sum_xp(x,y)=p(y)\ \text{(marginale)}\\
&=H(Y)-H(Y\mid X)
\end{aligned}
$$

Scrivendo invece $p(x,y)=p(x\mid y)\,p(y)$ gli stessi passaggi danno $I(X;Y)=H(X)-H(X\mid Y)$.

**Sanity check:** canale perfetto $Y=X$: $H(X\mid Y)=0$ e $I=H(X)$, tutta l'informazione passa. Canale inutile ($Y$ indipendente da $X$): $H(X\mid Y)=H(X)$ e $I=0$.
**Ipotesi:** canale senza memoria, variabili discrete (per variabili continue le somme diventano integrali).

### Derivazione — Simmetria e indipendenza · [[Confronto_new.pdf#page=4|p. 4]]
**Fonte:** proprietà enunciate senza passaggi.

- **Simmetria.** Nella definizione $x$ e $y$ compaiono in modo simmetrico: $p(x,y)=p(y,x)$ e il denominatore $p(x)p(y)$ non cambia scambiandoli, quindi $I(X;Y)=I(Y;X)$.
- **Indipendenza.** Se $p(x,y)=p(x)\,p(y)$, ogni logaritmo vale $\log_21=0$ e quindi $I(X;Y)=0$: osservare $Y$ non dice nulla su $X$.

### Derivazione — Banda contro potenza nella capacità AWGN · [[Confronto_new.pdf#page=9|p. 9]]
**Fonte:** la slide afferma che per aumentare molto la capacità conviene spesso aumentare la banda piuttosto che solo la potenza.

> 🧩 Derivazione mia: confronto a SNR alto ($\gamma\gg1$, quindi $\log_2(1+\gamma)\approx\log_2\gamma$).

$$
\begin{aligned}
P\to2P:\quad C'&=W\log_2(1+2\gamma)\approx W(\log_2\gamma+1)=C+W && \text{raddoppiare la potenza aggiunge solo } W \text{ bit/s}\\
W\to2W:\quad C'&=2W\log_2\Big(1+\frac{\gamma}{2}\Big)\approx2W(\log_2\gamma-1)=2C-2W && \text{la capacità quasi raddoppia}
\end{aligned}
$$

Nel secondo caso $\gamma$ si dimezza perché la stessa potenza raccoglie il rumore di una banda doppia: $\gamma=P/(N_0W)$.

**Limite di banda infinita.** La banda però non fa crescere la capacità senza limite, perché aumenta anche il rumore raccolto:

$$
\lim_{W\to\infty}W\log_2\Big(1+\frac{P}{N_0W}\Big)=\lim_{W\to\infty}W\,\frac{P}{N_0W}\,\log_2e=\frac{P}{N_0}\log_2e\approx1.44\,\frac{P}{N_0}
$$

usando $\log_2(1+\epsilon)\approx\epsilon\log_2e$ per $\epsilon\to0$. Da questo limite discende il valore $-1.59$ dB di [[limite-di-shannon]].

**Ipotesi:** canale AWGN, potenza media $P$ fissata.

## Spiegazione · appunti [[Confronto new.pdf#page=4|p. 4]]–[[Confronto new.pdf#page=10|10]]

Si parte da una domanda pratica: dato un canale rumoroso, quanto velocemente si può trasmettere senza sbagliare? Shannon risponde con un numero, la **capacità**, che non dipende dalla modulazione scelta ma solo dal canale.

**Entropia e informazione mutua.** L'entropia $H(X)$ misura quanto è incerto l'ingresso prima di guardare l'uscita. Dopo aver osservato $Y$ resta un'incertezza $H(X\mid Y)$, dovuta al rumore. La differenza $H(X)-H(X\mid Y)$ è ciò che il canale ha effettivamente trasportato: l'informazione mutua. Nel disegno ad insiemi, $H(X)$ e $H(Y)$ sono due cerchi e $I(X;Y)$ è la loro intersezione.

**Capacità.** L'informazione mutua dipende sia dal canale, tramite $p(y\mid x)$, sia da come si usa l'ingresso, tramite $p(x)$. Scegliendo la $p(x)$ migliore si ottiene una proprietà del solo canale: $C=\max_{p(x)}I(X;Y)$.

**Secondo teorema di Shannon.** La capacità ha un significato operativo: sotto $C$ esistono codici che rendono l'errore piccolo quanto si vuole, sopra no. È un teorema di esistenza: dice cosa è possibile, non come farlo.

**Canale AWGN.** Con banda $W$, potenza $P$ e rumore bianco gaussiano di densità $N_0$, la capacità è $C=W\log_2(1+\gamma)$. Si legge così: la banda moltiplica (dipendenza **lineare**), l'SNR entra sotto logaritmo (dipendenza **logaritmica**). A SNR alto ogni raddoppio di potenza (+3 dB) aggiunge solo 1 bit/s/Hz.

**Dagli appunti presi a lezione.**
- Il canale è il meccanismo che associa **aleatoriamente** l'uscita $Y$ all'ingresso $X$; con il logaritmo in base 2 l'informazione si misura in bit, con il logaritmo naturale in nat.
- L'entropia è la media dell'**autoinformazione** $\log_2\frac{1}{p(y)}$, che cresce al diminuire della probabilità: un evento raro, quando accade, porta molta informazione.
- Il teorema di Shannon **non è costruttivo**: dice che sotto $C$ esistono tecniche con errore piccolo a piacere, ma non quale schema usare.
- Per rendere piccola la $P(e)$ Shannon indica una strada diversa dall'aumentare la potenza: **abbassare il rate** sotto la capacità. E per aumentare $C$ conviene allargare la banda, la risorsa preziosa.
- Nel canale AWGN $y[i]=x[i]+n[i]$ è l'uscita del demodulatore nell'$i$-esimo intervallo di simbolo: la demodulazione è fatta, manca solo la decisione.

> 🧩 Un'intuizione, non richiesta all'esame: in banda $W$ si trasmettono $2W$ dimensioni al secondo (il prodotto tempo-banda $N=2WT$ di [[parametri-globali-modulazioni]]), e ciascuna dimensione porta al massimo $\frac12\log_2(1+\gamma)$ bit: $2W\cdot\frac12\log_2(1+\gamma)=W\log_2(1+\gamma)$.

> 🎯 Esame: definizione di informazione mutua e il suo legame con le entropie (con il passaggio), definizione di capacità, enunciato del secondo teorema di Shannon, formula della capacità AWGN e sua interpretazione (lineare in $W$, logaritmica in $\gamma$). La formula AWGN non va dimostrata.

## Perché importa

La capacità è il **riferimento assoluto** con cui si misurano tutte le modulazioni del corso: da $R_b\le C$ nasce la frontiera di Shannon nel piano $(\eta_B,E_b/N_0)$ ([[limite-di-shannon]]), che dice quanta energia per bit serve come minimo per una data efficienza spettrale. Una modulazione reale si giudica dalla sua distanza da quella frontiera.

## Connessioni

- [[limite-di-shannon]] — da $R_b\le C$ alla frontiera $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$.
- [[parametri-globali-modulazioni]] — $\gamma=\frac{E_b}{N_0}\eta_B$: l'SNR della capacità riscritto con i parametri globali.
- [[rumore-in-banda-passante]] — il rumore con densità $N_0$ in banda $W$, di potenza $N_0W$, è il denominatore di $\gamma$.
- [[coppie-di-variabili-aleatorie]] — distribuzioni congiunte, marginali e condizionate usate nella definizione.
- [[processo-gaussiano]] — il rumore del canale AWGN.

## Fonti · [[Confronto_new.pdf#page=3|p. 3]]–[[Confronto_new.pdf#page=9|9]]

[[parametri-globali-e-capacita]] — Confronto_new.pdf, slide 3–9.

_Aggiornato: 2026-11-15 — appunti presi a lezione dalla copia annotata Confronto new.pdf; creazione da ingest Confronto_new.pdf_
