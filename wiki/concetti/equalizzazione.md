---
tipo: concetto
importanza_esame: alta
prerequisiti: ["interferenza-intersimbolica", "criterio-di-nyquist", "ricevitore-ottimo-awgn", "rivelazione-map-ml"]
fonti_pdf: ["signaling_bandlimited_channel.pdf#page=32", "signaling_bandlimited_channel.pdf#page=33", "signaling_bandlimited_channel.pdf#page=34", "signaling_bandlimited_channel.pdf#page=35", "signaling_bandlimited_channel.pdf#page=36", "signaling_bandlimited_channel.pdf#page=37", "signaling_bandlimited_channel.pdf#page=38", "signaling_bandlimited_channel.pdf#page=39", "signaling_bandlimited_channel.pdf#page=40", "signaling_bandlimited_channel.pdf#page=45", "signaling_bandlimited_channel.pdf#page=46", "signaling_bandlimited_channel.pdf#page=47"]
---

# Equalizzazione e stima di sequenza a massima verosimiglianza (MLSE)

## Definizione · [[signaling_bandlimited_channel.pdf#page=32|p. 32]], [[signaling_bandlimited_channel.pdf#page=33|33]], [[signaling_bandlimited_channel.pdf#page=35|35]]

**Equalizzazione** è qualunque tecnica di elaborazione o filtraggio progettata per eliminare o ridurre l'ISI. Serve quando non si può soddisfare il criterio di Nyquist, perché la risposta del canale non è nota al trasmettitore o varia nel tempo.

- **Lineari**: zero-forcing (ZF) e minimum mean-square error (MMSE). Semplici, ma amplificano il rumore.
- **Non lineari**: decision-feedback equalization (DFE), la più comune, soffre di propagazione degli errori a basso SNR; **MLSE**, ottima, con complessità esponenziale nella memoria del canale.

La **MLSE** non filtra: sceglie l'intera **sequenza** di simboli che massimizza la verosimiglianza del segnale ricevuto, e si realizza in modo efficiente con l'[[algoritmo-di-viterbi]].

## Formule · [[signaling_bandlimited_channel.pdf#page=35|p. 35]], [[signaling_bandlimited_channel.pdf#page=37|37]]–[[signaling_bandlimited_channel.pdf#page=39|39]], [[signaling_bandlimited_channel.pdf#page=45|45]]–[[signaling_bandlimited_channel.pdf#page=47|47]]

| Formula | Significato |
|---|---|
| $y(t)=\sum_ns(n)\,q(t-nT)$, $q=g\ast h$, $q\equiv0$ fuori da $[0,LT]$ | uscita del canale (11), memoria $L$ |
| $\lambda(y)=\text{Re}\langle r,y\rangle-\frac12\lVert y\rVert^2$ | log-verosimiglianza della sequenza (12)–(13) |
| $\alpha(n)=\int r(t)q^\ast(t-nT)\,dt$ | uscita del filtro adattato $q^\ast(-t)$ in $nT$ |
| $\beta_{m,n}=\int q(t-nT)q^\ast(t-mT)\,dt$ | autocorrelazione dell'impulso (dipende da $n-m$) |
| $\hat{\mathbf s}=\arg\max_{\mathbf s}\big\{\text{Re}\sum_ns^\ast(n)\alpha(n)-\frac12\sum_n\sum_ms(n)s^\ast(m)\beta(n-m)\big\}$ | regola MLSE |
| $\lambda(y)=U_L(\sigma_L)+\sum_{k=L+1}^KV_k(\sigma_{k-1},\sigma_k)$ | scomposizione per Viterbi |

> 🧮 Formula chiave: MLSE = filtro adattato a $q$ + massimizzazione di $\text{Re}\sum s^\ast\alpha-\frac12\sum\sum ss^\ast\beta$ con Viterbi.

Simboli: $r(t)=y(t)+w(t)$ segnale ricevuto, $w$ rumore gaussiano di PSD $\sigma^2$; $q(t)$ risposta combinata di sagomatura e canale; $L$ memoria del canale in periodi di simbolo; $K+1$ numero di simboli del blocco; $M$ cardinalità della costellazione; $\sigma_\ell=(s(\ell-1),\dots,s(\ell-L))$ stato del traliccio.

## Derivazioni

### Derivazione — Log-verosimiglianza in funzione di α e β (14) · [[signaling_bandlimited_channel.pdf#page=37|p. 37]], [[signaling_bandlimited_channel.pdf#page=38|38]]
**Si parte da:** (13) con $y(t)=\sum_{n=0}^Ks(n)q(t-nT)$ ([[ricevitore-ottimo-awgn]]).

$$
\begin{aligned}
\text{Re}\int r\,y^\ast\,dt&=\text{Re}\int r(t)\sum_ns^\ast(n)q^\ast(t-nT)\,dt=\sum_n\text{Re}\Big(s^\ast(n)\underbrace{\int r(t)q^\ast(t-nT)\,dt}_{\alpha(n)}\Big) && \text{coniugo la somma, scambio somma e integrale}\\
\int|y|^2dt&=\int\sum_ns(n)q(t-nT)\sum_ms^\ast(m)q^\ast(t-mT)\,dt=\sum_n\sum_ms(n)s^\ast(m)\underbrace{\int q(t-nT)q^\ast(t-mT)\,dt}_{\beta_{m,n}} && |y|^2=y\,y^\ast
\end{aligned}
$$

> 🧩 Perché $\beta_{m,n}$ dipende solo da $n-m$ e perché $\alpha(n)$ è un filtro adattato (passaggi miei):

$$
\begin{aligned}
\beta_{m,n}&=\int q(\tau)\,q^\ast\big(\tau+(n-m)T\big)\,d\tau && \tau=t-nT\text{; integrale su tutto l'asse (intervallo lungo)}\\
\beta^\ast(n-m)&=\int q^\ast(\tau)\,q\big(\tau+(n-m)T\big)\,d\tau=\beta(m-n) && \text{simmetria hermitiana}\\
r(t)\ast q^\ast(-t)\big|_{t=nT}&=\int r(\tau)\,q^\ast\big(\tau-nT\big)\,d\tau=\alpha(n) && \text{filtro } q^\ast(-t)\text{ campionato in } nT
\end{aligned}
$$

### Derivazione — Separazione dell'ultimo simbolo (15) · [[signaling_bandlimited_channel.pdf#page=45|p. 45]]
**Si parte da:** la regola MLSE con $n,m\in\{0,\dots,K\}$; separo i termini con $s(K)$.

$$
\begin{aligned}
\text{Re}\sum_{n=0}^Ks^\ast(n)\alpha(n)&=\text{Re}\sum_{n=0}^{K-1}s^\ast(n)\alpha(n)+\text{Re}[s^\ast(K)\alpha(K)] && \text{termine } n=K\\
\sum_{n=0}^K\sum_{m=0}^K(\cdot)&=\sum_{n=0}^{K-1}\sum_{m=0}^{K-1}(\cdot)+\sum_{m<K}s(K)s^\ast(m)\beta(K-m)+\sum_{n<K}s(n)s^\ast(K)\beta(n-K)+|s(K)|^2\beta(0) && \text{righe e colonne con } K\\
&=\sum_{n=0}^{K-1}\sum_{m=0}^{K-1}(\cdot)+2\,\text{Re}\Big[s(K)\sum_{n<K}s^\ast(n)\beta(K-n)\Big]+|s(K)|^2\beta(0) && \beta(n-K)=\beta^\ast(K-n)\text{: i due termini sono coniugati}\\
-\frac12\sum\sum(\cdot)&=-\frac12\sum_{n,m<K}(\cdot)-\text{Re}\Big[s(K)\sum_{n<K}s^\ast(n)\beta(K-n)\Big]-\frac12|s(K)|^2\beta(0) && \text{moltiplico per } -\tfrac12
\end{aligned}
$$

> ⚠️ Contraddizione: nelle (15)–(16) delle slide l'ultimo termine è $+|s(K)|^2\beta(0)$; il conto dà $-\frac12|s(K)|^2\beta(0)$, e lo stesso vale per l'ultimo termine di $V_k$ a p. 46. Il segno non cambia la struttura della ricorsione (il termine dipende solo da $s(K)$), ma cambia i valori delle metriche: per simboli a energia costante (PSK) è una costante e non sposta il massimo, per QAM sì.

Infine, poiché $q(t)\equiv0$ fuori da $[0,LT]$, $\beta(\ell)=0$ per $|\ell|>L$: nella somma su $n$ restano solo $n=K-L,\dots,K-1$ (16). Il nuovo simbolo interagisce solo con gli ultimi $L$.

### Derivazione — Ricorsione U/V e traliccio · [[signaling_bandlimited_channel.pdf#page=46|p. 46]], [[signaling_bandlimited_channel.pdf#page=47|47]]
Con $U_k$ uguale alla log-verosimiglianza troncata al simbolo $k$, la (16) applicata a $K$ e poi a $K-1, K-2,\dots$ dà

$$
\begin{aligned}
U_K&=U_{K-1}+V_K && \text{(16) con la definizione di } U, V\\
&=U_{K-2}+V_{K-1}+V_K=\dots=U_L(\sigma_L)+\sum_{k=L+1}^KV_k && \text{iterando fino a } k=L
\end{aligned}
$$

$V_k$ dipende da $s(k)$ e da $s(k-1),\dots,s(k-L)$: cioè dalla **transizione** tra due stati consecutivi del traliccio. La log-verosimiglianza è una somma di metriche di ramo, e massimizzarla vuol dire cercare il cammino di metrica massima.

> 🧩 Nota mia sugli indici: con $\sigma_\ell=(s(\ell-1),\dots,s(\ell-L))$, il simbolo $s(k)$ compare per la prima volta in $\sigma_{k+1}$, quindi $V_k$ è etichetta del ramo $\sigma_k\to\sigma_{k+1}$; la slide la scrive come funzione di $(\sigma_{k-1},\sigma_k)$, uno slittamento d'indice che non cambia nulla nel ragionamento.

**Dimensioni:** gli stati sono $M^L$ (le possibili $L$-uple di simboli), da ogni stato escono $M$ rami. Per ogni simbolo si fanno $M^{L+1}$ somme: complessità $\propto KM^{L+1}$, lineare in $K$ ed esponenziale in $L$. Con 1000 simboli QPSK e $L=2$: $1000\cdot4^3=64\,000$ operazioni ACS invece di $4^{1000}$ sequenze.

## Spiegazione · [[signaling_bandlimited_channel.pdf#page=32|p. 32]]–[[signaling_bandlimited_channel.pdf#page=36|36]], [[signaling_bandlimited_channel.pdf#page=39|39]], [[signaling_bandlimited_channel.pdf#page=40|40]]

- **Perché equalizzare.** Il criterio di Nyquist richiede che $g\ast h\ast c$ sia un coseno rialzato: servirebbe conoscere $h(t)$ al trasmettitore e riprogettare i filtri a ogni variazione del canale. In pratica si rinuncia all'ISI nulla e si mette un equalizzatore al ricevitore.
- **Albero degli equalizzatori (p. 34).** Tipi: lineari, non lineari (DFE e MLSE). Strutture: transversal e lattice (lineari e DFE), transversal channel estimator (MLSE, che deve stimare $q(t)$). Algoritmi di aggiornamento dei coefficienti: LMS, RLS, Fast RLS, Square-Root LS per le strutture transversal, Gradient RLS per le lattice.
- **MLSE.** Non usa un filtro equalizzatore, quindi non amplifica il rumore: tratta il blocco di simboli come un unico «super-simbolo» e applica la rivelazione ML della Lezione 9 a $M^{K+1}$ ipotesi. Il ricevitore è un **solo filtro adattato** a $q(t)$ (che produce $\alpha(n)$) seguito dal **rivelatore di sequenza** (Viterbi), che usa le $\beta(\ell)$ per tenere conto dell'ISI.

> 📚 Fonte esterna: ZF, MMSE e DFE sono solo nominati nelle slide, senza formule. Le loro strutture (filtro trasversale con coefficienti, retroazione delle decisioni) sono nei testi, per esempio Madhow, *Fundamentals of Digital Communication*, cap. 5: da recuperare se la docente le approfondisce.

## Perché importa

Su canali dispersivi (multipath, cavi lunghi) l'ISI non si può evitare con il solo progetto degli impulsi. L'equalizzazione è il tema 5 del programma: la MLSE è il ricevitore ottimo, e l'algoritmo di Viterbi è ciò che la rende realizzabile.

## Connessioni

- [[interferenza-intersimbolica]], [[criterio-di-nyquist]]: il problema e la soluzione «di progetto».
- [[algoritmo-di-viterbi]]: realizza la MLSE.
- [[ricevitore-ottimo-awgn]], [[rivelazione-map-ml]]: la MLSE è la rivelazione ML applicata alle sequenze.

## Fonti · [[signaling_bandlimited_channel.pdf#page=32|p. 32]]–[[signaling_bandlimited_channel.pdf#page=40|40]], [[signaling_bandlimited_channel.pdf#page=45|45]]–[[signaling_bandlimited_channel.pdf#page=47|47]]

- [[signaling-bandlimited-channels]]

_Aggiornato: 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf (Lezione 14)_
