---
tipo: concetto
importanza_esame: alta
prerequisiti: ["interferenza-intersimbolica", "criterio-di-nyquist", "ricevitore-ottimo-awgn", "rivelazione-map-ml"]
fonti_pdf: ["signaling_bandlimited_channel_NEW.pdf#page=33", "signaling_bandlimited_channel_NEW.pdf#page=34", "signaling_bandlimited_channel_NEW.pdf#page=35", "signaling_bandlimited_channel_NEW.pdf#page=36", "signaling_bandlimited_channel_NEW.pdf#page=37", "signaling_bandlimited_channel_NEW.pdf#page=38", "signaling_bandlimited_channel_NEW.pdf#page=39", "signaling_bandlimited_channel_NEW.pdf#page=40", "signaling_bandlimited_channel_NEW.pdf#page=41", "signaling_bandlimited_channel_NEW.pdf#page=42", "signaling_bandlimited_channel_NEW.pdf#page=43", "signaling_bandlimited_channel_NEW.pdf#page=44", "signaling_bandlimited_channel_NEW.pdf#page=45", "signaling_bandlimited_channel_NEW.pdf#page=46", "signaling_bandlimited_channel_NEW.pdf#page=47", "signaling_bandlimited_channel_NEW.pdf#page=48", "signaling_bandlimited_channel_NEW.pdf#page=49", "signaling_bandlimited_channel_NEW.pdf#page=50", "signaling_bandlimited_channel_NEW.pdf#page=51", "signaling_bandlimited_channel_NEW.pdf#page=56", "signaling_bandlimited_channel_NEW.pdf#page=57", "signaling_bandlimited_channel_NEW.pdf#page=58", "signaling_bandlimited_channel_NEW.pdf#page=59", "signaling_bandlimited_channel_NEW.pdf#page=60", "signaling_bandlimited_channel_NEW.pdf#page=61"]
---

# Equalizzazione e stima di sequenza a massima verosimiglianza (MLSE)

## Definizione · [[signaling_bandlimited_channel_NEW.pdf#page=33|p. 33]]–[[signaling_bandlimited_channel_NEW.pdf#page=36|36]], [[signaling_bandlimited_channel_NEW.pdf#page=46|46]]

**Equalizzazione** è qualunque tecnica di elaborazione o filtraggio progettata per eliminare o ridurre l'ISI. Serve quando non si può soddisfare il criterio di Nyquist, perché la risposta del canale non è nota al trasmettitore o varia nel tempo: i filtri di trasmissione e ricezione si progettano senza conoscere il canale (filtri a radice di coseno rialzato) e l'equalizzatore, al ricevitore, si occupa dell'ISI introdotta da $h(t)$.

- **Lineari**: zero-forcing (ZF) e minimum mean-square error (MMSE). Semplici; lo ZF in particolare può amplificare il rumore.
- **Non lineari**: decision-feedback equalization (DFE), la più comune, soffre di propagazione degli errori a basso SNR; **MLSE**, ottima, con complessità esponenziale nella memoria del canale.

Un equalizzatore lineare è un **filtro digitale** (appunti) che combina i campioni del segnale ricevuto con un vettore di coefficienti $\mathbf c$. Nell'**equalizzatore frazionario** (*fractionally spaced*) i campioni sono $S>1$ per intervallo di simbolo.

La **MLSE** non filtra: sceglie l'intera **sequenza** di simboli che massimizza la verosimiglianza del segnale ricevuto, e si realizza in modo efficiente con l'[[algoritmo-di-viterbi]].

## Formule · [[signaling_bandlimited_channel_NEW.pdf#page=37|p. 37]], [[signaling_bandlimited_channel_NEW.pdf#page=39|39]]–[[signaling_bandlimited_channel_NEW.pdf#page=46|46]], [[signaling_bandlimited_channel_NEW.pdf#page=48|48]]–[[signaling_bandlimited_channel_NEW.pdf#page=51|51]], [[signaling_bandlimited_channel_NEW.pdf#page=56|56]], [[signaling_bandlimited_channel_NEW.pdf#page=58|58]], [[signaling_bandlimited_channel_NEW.pdf#page=60|60]], [[signaling_bandlimited_channel_NEW.pdf#page=61|61]]

**Equalizzatori lineari (campioni del segnale ricevuto)**

| Formula | Significato |
|---|---|
| $y(k)=s(k)p(0)+\sum_{m=1}^Ls(k-m)p(m)$ | campione al symbol rate con memoria finita $L$: segnale utile + ISI |
| $t_{k,\ell}=kT+\ell T_c$, $T_c=T/S$, $\ell=0,\dots,S-1$ | istanti di campionamento frazionario |
| $\mathbf y(k)=s(k)\mathbf p_0+\sum_{m=1}^Ls(k-m)\mathbf p_m$ | modello vettoriale dell'ISI, $\mathbf y(k)\in\mathbb C^{S}$ |
| $z(k)=\mathbf c^H\mathbf y(k)$ | uscita dell'equalizzatore |
| $\mathbf P^H\mathbf c=\mathbf e_1$ | vincoli ZF: guadagno utile 1, ISI nulla |
| $\mathbf c_{ZF}=\mathbf P(\mathbf P^H\mathbf P)^{-1}\mathbf e_1$ | ZF a norma minima ($S\ge L+1$, $\mathbf P$ a rango pieno) |
| $J(\mathbf c)=E\{\lvert\mathbf c^H\mathbf r(k)-s(k)\rvert^2\}$ | errore quadratico medio |
| $\mathbf c_{MMSE}=\sigma_s^2\mathbf R_{rr}^{-1}\mathbf p_0$ | equalizzatore MMSE |

**MLSE**

| Formula | Significato |
|---|---|
| $y(t)=\sum_ns(n)\,q(t-nT)$, $q=g\ast h$, $q\equiv0$ fuori da $[0,LT]$ | uscita del canale (11), memoria $L$ |
| $\lambda(y)=\text{Re}\langle r,y\rangle-\frac12\lVert y\rVert^2$ | log del rapporto di verosimiglianza della sequenza (12)–(13) |
| $\alpha(n)=\int r(t)q^\ast(t-nT)\,dt$ | uscita del filtro adattato $q^\ast(-t)$ in $nT$ |
| $\beta(\ell)=\int q(t)q^\ast(t-\ell T)\,dt=r_q(\ell T)$ | campioni dell'autocorrelazione dell'impulso; $\beta_{m,n}=\beta(m-n)$ |
| $\beta(\ell)=0$ per $\lvert\ell\rvert\ge L$, $\beta(-\ell)=\beta^\ast(\ell)$ | supporto finito e simmetria hermitiana |
| $\hat{\mathbf s}=\arg\max_{\mathbf s}\big\{\text{Re}\sum_ns^\ast(n)\alpha(n)-\frac12\sum_n\sum_ms(n)s^\ast(m)\beta(m-n)\big\}$ | regola MLSE |
| $\lambda(y)=U_{L-1}(\sigma_L)+\sum_{k=L}^KV_k(\sigma_k,\sigma_{k+1})$ | scomposizione per Viterbi |

> 🧮 Formula chiave: $\mathbf c_{ZF}=\mathbf P(\mathbf P^H\mathbf P)^{-1}\mathbf e_1$, $\mathbf c_{MMSE}=\sigma_s^2\mathbf R_{rr}^{-1}\mathbf p_0$; MLSE = filtro adattato a $q$ + massimizzazione di $\text{Re}\sum s^\ast\alpha-\frac12\sum\sum ss^\ast\beta$ con Viterbi.

Simboli: $s(k)$ simbolo $k$-esimo, a media nulla e potenza $\sigma_s^2=E\{\lvert s(k)\rvert^2\}$; $p(t)=g\ast h\ast c$ impulso complessivo (filtro di trasmissione, canale, filtro di ricezione), $p(m)=p(mT)$; $L$ memoria in intervalli di simbolo; $S$ campioni per simbolo, $T_c=T/S$; $\mathbf p_m=[p(mT),p(mT+T_c),\dots,p(mT+(S-1)T_c)]^T$; $\mathbf P=[\mathbf p_0\ \mathbf p_1\cdots\mathbf p_L]\in\mathbb C^{S\times(L+1)}$; $\mathbf e_1=[1,0,\dots,0]^T$; $\mathbf c\in\mathbb C^{S}$ coefficienti dell'equalizzatore, $(\cdot)^H$ trasposto coniugato; $\mathbf r(k)=\mathbf y(k)+\mathbf n(k)$ campioni con rumore, $\mathbf R_{rr}=E\{\mathbf r\mathbf r^H\}$, $\mathbf R_{nn}=E\{\mathbf n\mathbf n^H\}$. Per la MLSE: $r(t)=y(t)+w(t)$ segnale ricevuto, $w$ rumore gaussiano di PSD $\sigma^2$; $q(t)$ risposta combinata di sagomatura e canale; $K+1$ numero di simboli del blocco; $M$ cardinalità della costellazione; $\sigma_\ell=(s(\ell-1),\dots,s(\ell-L))$ stato del traliccio.

## Derivazioni

### Derivazione — ISI con memoria finita · [[signaling_bandlimited_channel_NEW.pdf#page=37|p. 37]], [[signaling_bandlimited_channel_NEW.pdf#page=38|38]]
**Si parte da:** $y(t)=\sum_ns(n)p(t-nT)$, con $p(t)=0$ fuori da $[0,LT]$ (dopo troncamento e un ritardo opportuno). Gli appunti: «stiamo assumendo che il canale abbia memoria finita».

$$
\begin{aligned}
y(kT)&=\sum_ns(n)\,p\big((k-n)T\big) && \text{campiono al baud rate, } t_k=kT\\
&=\sum_{n=k-L}^ks(n)\,p\big((k-n)T\big) && p\neq0 \text{ solo se } 0\le(k-n)T\le LT\iff k-L\le n\le k\\
&=\sum_{m=0}^Ls(k-m)\,p(mT) && m=k-n:\ n=k\Rightarrow m=0,\ n=k-L\Rightarrow m=L\\
y(k)&=\underbrace{s(k)p(0)}_{\text{utile}}+\underbrace{\sum_{m=1}^Ls(k-m)p(m)}_{\text{ISI}} && \text{separo } m=0
\end{aligned}
$$

Anche se $g\ast c$ è un impulso di Nyquist, il canale rovina la condizione: $p(mT)$ non è nullo per $m\neq0$. Ogni campione contiene il simbolo attuale e gli $L$ precedenti.

### Derivazione — Perché sovracampionare: il caso L = 1 · [[signaling_bandlimited_channel_NEW.pdf#page=39|p. 39]]–[[signaling_bandlimited_channel_NEW.pdf#page=41|41]]
**Si parte da:** un equalizzatore che usa solo i campioni di **un** intervallo di simbolo e vuole guadagno utile 1 e ISI nulla.

**Un campione per simbolo ($S=1$).** Il coefficiente è uno scalare $c$:

$$
\begin{aligned}
z(k)&=c^\ast y(k)=c^\ast p(0)\,s(k)+c^\ast p(1)\,s(k-1) && L=1\\
&\begin{cases}c^\ast p(0)=1\\ c^\ast p(1)=0\end{cases} && \text{1 incognita, 2 equazioni}
\end{aligned}
$$

Dalla seconda $c=0$ (se $p(1)\neq0$), che contraddice la prima: si risolve solo se $p(1)=0$, cioè se l'ISI non c'era. Uno scalare moltiplica segnale utile e ISI per lo **stesso fattore**, quindi il loro rapporto non cambia.

**Due campioni per simbolo ($S=2$).** Ora $\mathbf c$, $\mathbf p_0$, $\mathbf p_1$ sono vettori del piano (primo campione, secondo campione). Basta prendere $\mathbf c$ **ortogonale** a $\mathbf p_1$: l'ISI sparisce, e finché $\mathbf p_0$ non è parallelo a $\mathbf p_1$ resta $\mathbf c^H\mathbf p_0\neq0$, che si porta a 1 scalando $\mathbf c$.

> 🧩 Numeri miei (vettori reali): $\mathbf p_0=[1,\ 0.5]^T$, $\mathbf p_1=[0.2,\ 0.4]^T$. Un vettore ortogonale a $\mathbf p_1$ è $[0.4,\ -0.2]^T$; con esso $\mathbf c^H\mathbf p_0=0.4-0.1=0.3$, quindi divido per 0.3: $\mathbf c=[1.33,\ -0.67]^T$. Verifica: $\mathbf c^H\mathbf p_1=0.267-0.267=0$ (ISI nulla) e $\mathbf c^H\mathbf p_0=1.33-0.33=1$ (guadagno utile 1).

**Regola generale.** Con $S$ campioni per simbolo, $\mathbf c\in\mathbb C^S$ ha $S$ incognite e le condizioni sono $L+1$ (una di guadagno, $L$ di ISI nulla): in generale serve $S\ge L+1$. Il modello vettoriale si ottiene ripetendo il conto della slide 37 per ogni istante frazionario:

$$
\begin{aligned}
y(kT+\ell T_c)&=\sum_{n=k-L}^ks(n)\,p\big((k-n)T+\ell T_c\big)=\sum_{m=0}^Ls(k-m)\,p(mT+\ell T_c) && \ell=0,\dots,S-1\\
\mathbf y(k)&=s(k)\,\mathbf p_0+\sum_{m=1}^Ls(k-m)\,\mathbf p_m && \text{impilo gli } S \text{ campioni}
\end{aligned}
$$

### Derivazione — Equalizzatore zero-forcing · [[signaling_bandlimited_channel_NEW.pdf#page=42|p. 42]], [[signaling_bandlimited_channel_NEW.pdf#page=43|43]]
**Si parte da:** $z(k)=\mathbf c^H\mathbf y(k)=s(k)\,\mathbf c^H\mathbf p_0+\sum_{m=1}^Ls(k-m)\,\mathbf c^H\mathbf p_m$.

$$
\begin{aligned}
\mathbf c^H\mathbf p_0&=1,\quad\mathbf c^H\mathbf p_m=0\ \ (m=1,\dots,L) && \text{criterio ZF}\\
\mathbf p_m^H\mathbf c&=(\mathbf c^H\mathbf p_m)^\ast && \text{coniugo: 1 e 0 sono reali, non cambiano}\\
\mathbf P^H\mathbf c&=\mathbf e_1 && \text{le righe di } \mathbf P^H \text{ sono le } \mathbf p_m^H
\end{aligned}
$$

Con $S>L+1$ le soluzioni sono infinite; la slide sceglie quella di **norma minima**, $\min_{\mathbf c}\lVert\mathbf c\rVert^2$ con $\mathbf P^H\mathbf c=\mathbf e_1$.

> 🧩 Derivazione mia della soluzione a norma minima. Scompongo $\mathbf c=\mathbf c_\parallel+\mathbf c_\perp$, con $\mathbf c_\parallel$ nello spazio generato dalle colonne di $\mathbf P$ e $\mathbf c_\perp$ ortogonale a tutte.

$$
\begin{aligned}
\mathbf P^H\mathbf c&=\mathbf P^H\mathbf c_\parallel && \mathbf P^H\mathbf c_\perp=\mathbf 0\text{: il vincolo vede solo } \mathbf c_\parallel\\
\lVert\mathbf c\rVert^2&=\lVert\mathbf c_\parallel\rVert^2+\lVert\mathbf c_\perp\rVert^2 && \text{Pitagora}\\
\mathbf c_\perp&=\mathbf 0,\quad\mathbf c=\mathbf P\mathbf a && \mathbf c_\perp \text{ aumenta solo la norma}\\
\mathbf P^H\mathbf P\,\mathbf a&=\mathbf e_1\ \Rightarrow\ \mathbf a=(\mathbf P^H\mathbf P)^{-1}\mathbf e_1 && \mathbf P^H\mathbf P \text{ invertibile se } \mathbf P \text{ ha rango pieno}\\
\mathbf c_{ZF}&=\mathbf P(\mathbf P^H\mathbf P)^{-1}\mathbf e_1=(\mathbf P^H)^\dagger\mathbf e_1 && \dagger \text{ pseudoinversa di Moore-Penrose}
\end{aligned}
$$

**Rumore.** Con $\mathbf r(k)=\mathbf y(k)+\mathbf n(k)$ l'uscita contiene anche $\mathbf c^H\mathbf n(k)$, di potenza

$$E\{\lvert\mathbf c^H\mathbf n(k)\rvert^2\}=E\{\mathbf c^H\mathbf n\,\mathbf n^H\mathbf c\}=\mathbf c^H\mathbf R_{nn}\mathbf c$$

I vincoli ZF possono portare ad **amplificazione del rumore** (*noise enhancement*).

> 🧩 Perché. Con rumore bianco, $\mathbf R_{nn}=\sigma_n^2\mathbf I$, la potenza del rumore in uscita è $\sigma_n^2\lVert\mathbf c\rVert^2$: per questo, tra gli ZF, conviene quello di norma minima. Ma se $\mathbf p_0$ è quasi parallelo a un $\mathbf p_m$, un $\mathbf c$ ortogonale a $\mathbf p_m$ è quasi ortogonale anche a $\mathbf p_0$, e per avere $\mathbf c^H\mathbf p_0=1$ va allungato molto: $\lVert\mathbf c\rVert$ cresce e con lei il rumore. Lo ZF elimina l'ISI **a qualunque costo** in rumore. Nell'esempio sopra $\lVert\mathbf c\rVert^2=1.33^2+0.67^2\approx2.2$: il rumore esce più che raddoppiato.

### Derivazione — Equalizzatore MMSE · [[signaling_bandlimited_channel_NEW.pdf#page=44|p. 44]], [[signaling_bandlimited_channel_NEW.pdf#page=45|45]]
**Si parte da:** $z(k)=\mathbf c^H\mathbf r(k)$ e dal costo $J(\mathbf c)=E\{\lvert\mathbf c^H\mathbf r(k)-s(k)\rvert^2\}$: invece di imporre ISI nulla, si vuole l'uscita il più vicina possibile al simbolo, rumore compreso.

$$
\begin{aligned}
J(\mathbf c)&=E\big\{(\mathbf c^H\mathbf r-s)(\mathbf c^H\mathbf r-s)^\ast\big\}=E\big\{(\mathbf c^H\mathbf r-s)(\mathbf r^H\mathbf c-s^\ast)\big\} && \lvert x\rvert^2=xx^\ast,\ (\mathbf c^H\mathbf r)^\ast=\mathbf r^H\mathbf c\\
&=\mathbf c^HE\{\mathbf r\mathbf r^H\}\mathbf c-\mathbf c^HE\{\mathbf rs^\ast\}-E\{s\mathbf r^H\}\mathbf c+E\{\lvert s\rvert^2\} && \text{prodotto e linearità di } E\\
&=\mathbf c^H\mathbf R_{rr}\mathbf c-\mathbf c^HE\{\mathbf rs^\ast\}-E\{s\mathbf r^H\}\mathbf c+\sigma_s^2 && \text{definizioni}
\end{aligned}
$$

Ipotesi: simboli a media nulla, incorrelati nel tempo e indipendenti dal rumore.

$$
\begin{aligned}
E\{\mathbf r(k)s^\ast(k)\}&=E\Big\{\Big[s(k)\mathbf p_0+\sum_{m=1}^Ls(k-m)\mathbf p_m+\mathbf n(k)\Big]s^\ast(k)\Big\} && \text{sostituisco } \mathbf r\\
&=E\{\lvert s(k)\rvert^2\}\mathbf p_0+\sum_{m=1}^LE\{s(k-m)s^\ast(k)\}\mathbf p_m+E\{\mathbf n(k)\}E\{s^\ast(k)\} && \text{linearità; rumore indipendente}\\
&=\sigma_s^2\,\mathbf p_0 && \text{simboli incorrelati e a media nulla}\\
J(\mathbf c)&=\mathbf c^H\mathbf R_{rr}\mathbf c-\sigma_s^2\big(\mathbf c^H\mathbf p_0+\mathbf p_0^H\mathbf c\big)+\sigma_s^2=\mathbf c^H\mathbf R_{rr}\mathbf c-2\sigma_s^2\,\text{Re}\{\mathbf c^H\mathbf p_0\}+\sigma_s^2 && E\{s\mathbf r^H\}=(E\{\mathbf rs^\ast\})^H,\ x+x^\ast=2\text{Re}\,x
\end{aligned}
$$

Si annulla la derivata rispetto a $\mathbf c^\ast$, trattando $\mathbf c$ e $\mathbf c^\ast$ come indipendenti:

$$
\begin{aligned}
\frac{\partial J}{\partial\mathbf c^\ast}&=\mathbf R_{rr}\mathbf c-\sigma_s^2\mathbf p_0=\mathbf 0 && \tfrac{\partial}{\partial\mathbf c^\ast}\mathbf c^H\mathbf A\mathbf c=\mathbf A\mathbf c,\ \tfrac{\partial}{\partial\mathbf c^\ast}\mathbf c^H\mathbf p_0=\mathbf p_0,\ \tfrac{\partial}{\partial\mathbf c^\ast}\mathbf p_0^H\mathbf c=\mathbf 0\\
\mathbf c_{MMSE}&=\sigma_s^2\,\mathbf R_{rr}^{-1}\mathbf p_0 && \mathbf R_{rr} \text{ non singolare}
\end{aligned}
$$

> 🧩 Cosa c'è dentro $\mathbf R_{rr}$ (passaggi miei, stesse ipotesi): $\mathbf R_{rr}=E\{\mathbf r\mathbf r^H\}=\sigma_s^2\sum_{m=0}^L\mathbf p_m\mathbf p_m^H+\mathbf R_{nn}$, perché i prodotti incrociati tra simboli diversi e tra simboli e rumore hanno media nulla. L'MMSE quindi «vede» sia l'ISI (i $\mathbf p_m$) sia il rumore ($\mathbf R_{nn}$) e li bilancia: non annulla del tutto l'ISI se farlo costerebbe troppo rumore. 📚 Ad alto SNR ($\mathbf R_{nn}\to\mathbf 0$) l'MMSE tende allo ZF.

### Derivazione — Log-verosimiglianza in funzione di α e β (14) · [[signaling_bandlimited_channel_NEW.pdf#page=48|p. 48]]–[[signaling_bandlimited_channel_NEW.pdf#page=50|50]]
**Si parte da:** (13) con $y(t)=\sum_{n=0}^Ks(n)q(t-nT)$ ([[ricevitore-ottimo-awgn]]).

$$
\begin{aligned}
\text{Re}\int r\,y^\ast\,dt&=\text{Re}\int r(t)\sum_ns^\ast(n)q^\ast(t-nT)\,dt=\sum_n\text{Re}\Big(s^\ast(n)\underbrace{\int r(t)q^\ast(t-nT)\,dt}_{\alpha(n)}\Big) && \text{coniugo la somma, scambio somma e integrale}\\
\int|y|^2dt&=\int\sum_ns(n)q(t-nT)\sum_ms^\ast(m)q^\ast(t-mT)\,dt=\sum_n\sum_ms(n)s^\ast(m)\underbrace{\int q(t-nT)q^\ast(t-mT)\,dt}_{\beta_{m,n}} && |y|^2=y\,y^\ast\\
r(t)\ast q^\ast(-t)\big|_{t=nT}&=\int r(\tau)\,q^\ast(\tau-nT)\,d\tau=\alpha(n) && \text{filtro adattato } q^\ast(-t) \text{ campionato in } nT
\end{aligned}
$$

### Derivazione — I coefficienti β(ℓ) e la memoria del canale · [[signaling_bandlimited_channel_NEW.pdf#page=56|p. 56]], [[signaling_bandlimited_channel_NEW.pdf#page=57|57]]
**Fonte:** le slide 55–56 della versione aggiornata (prima la proprietà $\beta_{m,n}=\beta_{m-n}$ era solo enunciata).

$$
\begin{aligned}
\beta_{m,n}&=\int_{-\infty}^{+\infty}q(t-nT)\,q^\ast(t-mT)\,dt && \text{intervallo d'osservazione abbastanza lungo}\\
&=\int_{-\infty}^{+\infty}q(u)\,q^\ast\big(u-(m-n)T\big)\,du=\beta(m-n) && u=t-nT,\ t-mT=u-(m-n)T\\
r_q(\tau)&\triangleq q(\tau)\ast q^\ast(-\tau)=\int q(t)\,q^\ast(t-\tau)\,dt && \text{uscita del filtro adattato con ingresso } q\\
\beta(\ell)&=r_q(\ell T) && \text{campioni ogni } T\\
\text{supp}\,r_q&=[0,LT]+[-LT,0]=[-LT,LT] && \text{il supporto della convoluzione è la somma dei supporti}\\
r_q(-\tau)&=\int q(t)q^\ast(t+\tau)\,dt=\Big[\int q(t')q^\ast(t'-\tau)\,dt'\Big]^\ast=r_q^\ast(\tau)\ \Rightarrow\ \beta(-\ell)=\beta^\ast(\ell) && t'=t+\tau
\end{aligned}
$$

La slide conclude $\beta(\ell)=0$ per $\lvert\ell\rvert\ge L$.

> 🧩 Perché anche gli estremi $\ell=\pm L$ danno zero: in $\tau=LT$ i supporti di $q(t)$ e $q^\ast(t-LT)$, cioè $[0,LT]$ e $[LT,2LT]$, si toccano in un solo punto, e l'integrale su un punto è nullo (per un impulso limitato). I $\beta(\ell)$ non nulli sono al più quelli con $\lvert\ell\rvert\le L-1$: il simbolo nuovo interagisce con gli $L-1$ precedenti tramite i $\beta$, e lo stato di $L$ simboli li contiene tutti.

**Esempio della slide 56: impulso rettangolare** $q(t)=A$ per $0\le t\le LT$.

$$
\begin{aligned}
r_q(\tau)&=\int_\tau^{LT}A\,A^\ast\,dt=\lvert A\rvert^2(LT-\tau) && 0\le\tau\le LT\text{: i due impulsi si sovrappongono su } [\tau,LT]\\
r_q(\tau)&=\lvert A\rvert^2(LT-\lvert\tau\rvert),\quad\lvert\tau\rvert\le LT && r_q(-\tau)=r_q^\ast(\tau)\text{: triangolo di semiampiezza } LT\\
\beta(\ell)&=r_q(\ell T)=\lvert A\rvert^2T(L-\lvert\ell\rvert),\quad\lvert\ell\rvert\le L && \tau=\ell T
\end{aligned}
$$

**Numeri ($L=3$):** $\beta(0)=3\lvert A\rvert^2T$, $\beta(\pm1)=2\lvert A\rvert^2T$, $\beta(\pm2)=\lvert A\rvert^2T$, $\beta(\pm3)=0$. La sovrapposizione è necessaria ma non sufficiente: per un $q(t)$ generico qualche $\beta(\ell)$ può annullarsi anche con $\lvert\ell\rvert<L$.

### Derivazione — Separazione dell'ultimo simbolo (15)–(16) · [[signaling_bandlimited_channel_NEW.pdf#page=58|p. 58]], [[signaling_bandlimited_channel_NEW.pdf#page=59|59]]
**Si parte da:** la regola MLSE con $n,m\in\{0,\dots,K\}$; separo i termini con $s(K)$. La pagina di appunti 59 fa lo stesso conto per la doppia somma.

$$
\begin{aligned}
\text{Re}\sum_{n=0}^Ks^\ast(n)\alpha(n)&=\text{Re}\sum_{n=0}^{K-1}s^\ast(n)\alpha(n)+\text{Re}[s^\ast(K)\alpha(K)] && \text{termine } n=K\\
\sum_{n=0}^K\sum_{m=0}^Ks(n)s^\ast(m)\beta(m-n)&=\sum_{n=0}^{K-1}\sum_{m=0}^{K-1}(\cdot)+\sum_{m=0}^{K-1}s(K)s^\ast(m)\beta(m-K)+\sum_{n=0}^{K-1}s(n)s^\ast(K)\beta(K-n)+\lvert s(K)\rvert^2\beta(0) && \text{riga } n=K\text{, colonna } m=K\text{, angolo}\\
&=\sum_{n=0}^{K-1}\sum_{m=0}^{K-1}(\cdot)+2\,\text{Re}\Big[s(K)\sum_{n=0}^{K-1}s^\ast(n)\beta(n-K)\Big]+\lvert s(K)\rvert^2\beta(0) && \beta(K-n)=\beta^\ast(n-K)\text{: i due termini sono coniugati}\\
-\frac12\sum\sum(\cdot)&=-\frac12\sum_{n,m<K}(\cdot)-\text{Re}\Big[s(K)\sum_{n=0}^{K-1}s^\ast(n)\beta(n-K)\Big]-\frac12\lvert s(K)\rvert^2\beta(0) && \text{moltiplico per } -\tfrac12
\end{aligned}
$$

È la (15). Poiché $\beta(\ell)=0$ per $\lvert\ell\rvert\ge L$, nella somma su $n$ restano solo i termini con $\lvert n-K\rvert<L$: la slide scrive $n=K-L,\dots,K-1$ (16), e gli appunti precisano $-L<n-K<L$. Il nuovo simbolo interagisce solo con gli ultimi simboli, non con tutta la storia.

> ⚠️ Contraddizione risolta: la versione precedente delle slide scriveva l'ultimo termine come $+\lvert s(K)\rvert^2\beta(0)$; la versione aggiornata lo corregge in $-\frac12\lvert s(K)\rvert^2\beta(0)$, il valore che dà il conto qui sopra. Anche $\beta(n-m)$ è diventato $\beta(m-n)$, coerente con la nuova definizione $\beta_{m,n}=\beta(m-n)$.

### Derivazione — Ricorsione U/V e traliccio · [[signaling_bandlimited_channel_NEW.pdf#page=60|p. 60]], [[signaling_bandlimited_channel_NEW.pdf#page=61|61]]
**Si parte da:** le definizioni della slide 58: stato $\sigma_\ell=(s(\ell-1),\dots,s(\ell-L))$, $\ell=L,\dots,K+1$; $U_k(\sigma_L,\dots,\sigma_{k+1})$ è la log-verosimiglianza troncata al simbolo $k$ ($k=L-1,\dots,K$); $V_k(\sigma_k,\sigma_{k+1})=\text{Re}[s^\ast(k)\alpha(k)]-\text{Re}\big[s(k)\sum_{m=k-L}^{k-1}s^\ast(m)\beta(m-k)\big]-\frac12\lvert s(k)\rvert^2\beta(0)$ ($k=L,\dots,K$).

$$
\begin{aligned}
\lambda(y)&=U_K(\sigma_L,\dots,\sigma_{K+1}) && \text{tutti i simboli } s(0),\dots,s(K)\\
U_K&=U_{K-1}(\sigma_L,\dots,\sigma_K)+V_K(\sigma_K,\sigma_{K+1}) && \text{(16) con le definizioni di } U, V\\
&=U_{K-2}+V_{K-1}+V_K=\dots && \text{«posso reiterare il ragionamento» (appunti)}\\
\lambda(y)&=U_{L-1}(\sigma_L)+V_L(\sigma_L,\sigma_{L+1})+\dots+V_K(\sigma_K,\sigma_{K+1}) && \text{fino a } k=L-1
\end{aligned}
$$

**Controllo degli indici (🧩).** $U_{L-1}$ contiene $s(0),\dots,s(L-1)$, che sono esattamente lo stato $\sigma_L=(s(L-1),\dots,s(0))$. $V_k$ contiene $s(k)$ e $s(k-L),\dots,s(k-1)$: $\sigma_k$ porta $s(k-1),\dots,s(k-L)$ e $\sigma_{k+1}$ aggiunge $s(k)$. Quindi $V_k$ dipende solo dalla **transizione** $\sigma_k\to\sigma_{k+1}$ ed è l'etichetta del ramo. Gli appunti chiamano $U_{L-1}$ la «metrica aggregata» di partenza e $V_\ell$ la «metrica» di ramo: la log-verosimiglianza è una somma di metriche di ramo, e massimizzarla vuol dire cercare il cammino di metrica massima. La versione precedente delle slide scriveva $V_k(\sigma_{k-1},\sigma_k)$: l'aggiornamento allinea gli indici al ramo $\sigma_k\to\sigma_{k+1}$.

**Come si legge $U_k$ (🧩).** $U_k$ è una definizione, non un risultato: è la $\lambda(y)$ calcolata sui soli simboli $s(0),\dots,s(k)$, un «totale parziale» ($U_K=\lambda$; con $k=K-1$ le somme vanno da 0 a $K-1$ e danno i primi due termini della (16)). L'indice $\ell$ delle somme è muto (nella (16) era $n$). Gli stati non compaiono nella formula perché ne sono le «coordinate» i simboli: fissati $\sigma_L,\dots,\sigma_{k+1}$ sono fissati $s(0),\dots,s(k)$, come $f(P)=x^2+y^2$ per $P=(x,y)$. Il pedice di uno stato indica l'istante: $\sigma_{k+1}=(s(k),\dots,s(k-L+1))$ non contiene $s(k+1)$, ed è l'unico che contiene $s(k)$. Gli estremi $\ell=L,\dots,K+1$ vengono dall'imporre che gli indici dentro $\sigma_\ell$, da $\ell-L$ a $\ell-1$, stiano tra 0 e $K$. Nella tabella delle coppie $(\ell,m)$ della doppia somma, passare da $U_{k-1}$ a $U_k$ aggiunge la riga e la colonna $k$ più il termine $\text{Re}[s^\ast(k)\alpha(k)]$: è $V_k$; poiché le caselle non nulle sono una fascia di semiampiezza $L-1$ attorno alla diagonale, la somma di $V_k$ parte da $k-L$, mentre quella di $U_k$ parte da 0 perché conta tutti i simboli.

**Perché non serve tutta la storia (🧩).** La catena di interazioni $s(k)\leftrightarrow s(k-1)\leftrightarrow\dots$ arriva fino a $s(0)$, ma la MLSE non decide i simboli uno alla volta in base ai precedenti: sceglie l'intera sequenza che massimizza $\lambda$, e l'ISI sta dentro la metrica. Viterbi ipotizza tutti gli stati: la metrica accumulata di ciascuno riassume il passato più vecchio dello stato, e a ogni passo basta $V_k(\sigma_k,\sigma_{k+1})$. L'algoritmo va solo in avanti e alla fine risale il sopravvissuto migliore.

**Dimensioni:** gli stati sono $M^L$ (le possibili $L$-uple di simboli), da ogni stato escono $M$ rami. Per ogni simbolo si fanno $M^{L+1}$ somme: complessità $\propto KM^{L+1}$, lineare in $K$ ed esponenziale in $L$ (appunti della slide 36: la complessità del VA è lineare in $K$, esponenziale in $L$, e introduce latenza). Con 1000 simboli QPSK e $L=2$: $1000\cdot4^3=64\,000$ operazioni ACS invece di $4^{1000}$ sequenze.

## Spiegazione · [[signaling_bandlimited_channel_NEW.pdf#page=33|p. 33]]–[[signaling_bandlimited_channel_NEW.pdf#page=37|37]], [[signaling_bandlimited_channel_NEW.pdf#page=39|39]], [[signaling_bandlimited_channel_NEW.pdf#page=43|43]], [[signaling_bandlimited_channel_NEW.pdf#page=46|46]], [[signaling_bandlimited_channel_NEW.pdf#page=47|47]]–[[signaling_bandlimited_channel_NEW.pdf#page=51|51]]

- **Perché equalizzare.** Il criterio di Nyquist richiede che $g\ast h\ast c$ sia un coseno rialzato: servirebbe conoscere $h(t)$ al trasmettitore e riprogettare i filtri a ogni variazione del canale. In pratica si rinuncia all'ISI nulla: $g$ e $c$ sono filtri a radice di coseno rialzato fissi, e l'equalizzatore al ricevitore toglie l'ISI del canale.
- **Albero degli equalizzatori (slide 35).** Tipi: lineari, non lineari (DFE e MLSE). Strutture: transversal e lattice (lineari e DFE), transversal channel estimator (MLSE, che deve stimare $q(t)$). Algoritmi di aggiornamento dei coefficienti: LMS, RLS, Fast RLS, Square-Root LS per le strutture transversal, Gradient RLS per le lattice.
- **Perché più campioni per simbolo.** Con un solo campione l'equalizzatore di un intervallo è un numero, che scala allo stesso modo segnale e ISI. Con $S$ campioni lavora in uno spazio a $S$ dimensioni, dove può «girarsi» ortogonale ai vettori dell'ISI e lasciare passare quello utile. Servono almeno tante dimensioni quante condizioni: $S\ge L+1$.
- **ZF contro MMSE.** Lo ZF impone ISI esattamente nulla e guadagno 1, ignorando il rumore: se il canale rende quasi paralleli i vettori utile e ISI, i coefficienti esplodono e il rumore con loro. L'MMSE minimizza l'errore totale tra uscita e simbolo, ISI e rumore insieme, quindi accetta un po' di ISI residua per non amplificare troppo il rumore.
- **MLSE.** Non usa un filtro equalizzatore, quindi non amplifica il rumore: tratta il blocco di simboli come un unico «super-simbolo» e applica la rivelazione ML della Lezione 9 a $M^{K+1}$ ipotesi. Il ricevitore è un **solo filtro adattato** a $q(t)$ (che produce $\alpha(n)$) seguito dal **rivelatore di sequenza** (Viterbi), che usa le $\beta(\ell)$ per tenere conto dell'ISI. Le $\beta(\ell)$ sono i campioni dell'uscita di quel filtro adattato quando l'ingresso è $q(t)$ stesso.
  - *Dov'è $c(t)$ (🧩).* Il filtro di ricezione c'è ancora, ma non è il $c(t)$ RRC fisso: è $q^\ast(-t)$, adattato a $g\ast h$, quindi richiede di conoscere (stimare) il canale. Nelle (12)–(13) $r(t)$ è preso prima di ogni filtro perché la verosimiglianza in quella forma vale per rumore bianco.
  - *Un solo blocco al posto di equalizzatore + decisore (🧩).* Nel caso lineare l'equalizzatore, essendo un filtro, produce un numero qualsiasi ($z(k)=0.93$) e serve un decisore non lineare che lo arrotondi al simbolo ($+1$). Il rivelatore di sequenza confronta direttamente sequenze di simboli: gestisce l'ISI mettendola nella metrica e la sua uscita è già una decisione.
  - *Massimizzare la verosimiglianza (🧩).* Fissato il ricevuto $r(t)$, si sceglie la sequenza che avrebbe reso più probabile riceverlo: con rumore gaussiano bianco è quella la cui forma d'onda $y(t)$ è più vicina a $r(t)$, e $\lVert r-y\rVert^2=\lVert r\rVert^2-2\,\text{Re}\langle r,y\rangle+\lVert y\rVert^2$ con $\lVert r\rVert^2$ uguale per tutte dà la (12).

> 📚 Fonte esterna: la DFE è solo nominata nelle slide, senza formule. La sua struttura (filtro in avanti più retroazione delle decisioni già prese) è nei testi, per esempio Madhow, *Fundamentals of Digital Communication*, cap. 5.

## Perché importa

Su canali dispersivi (multipath, cavi lunghi) l'ISI non si può evitare con il solo progetto degli impulsi. L'equalizzazione è il tema 5 del programma: ZF e MMSE sono le soluzioni lineari, semplici e a bassa latenza; la MLSE è il ricevitore ottimo, e l'algoritmo di Viterbi è ciò che la rende realizzabile.

## Connessioni

- [[interferenza-intersimbolica]], [[criterio-di-nyquist]]: il problema e la soluzione «di progetto»; i filtri a radice di coseno rialzato sono la parte fissa del sistema.
- [[algoritmo-di-viterbi]]: realizza la MLSE.
- [[ricevitore-ottimo-awgn]], [[rivelazione-map-ml]]: la MLSE è la rivelazione ML applicata alle sequenze.
- [[quantizzazione-non-uniforme]]: lo stesso criterio MMSE (minimo errore quadratico medio) del quantizzatore di Lloyd-Max, qui applicato ai coefficienti di un filtro.

## Fonti · [[signaling_bandlimited_channel_NEW.pdf#page=33|p. 33]]–[[signaling_bandlimited_channel_NEW.pdf#page=51|51]], [[signaling_bandlimited_channel_NEW.pdf#page=56|56]]–[[signaling_bandlimited_channel_NEW.pdf#page=61|61]]

- [[signaling-bandlimited-channels]]

_Aggiornato: 2026-11-24 — chiarimenti 🧩 sulla MLSE (filtro di ricezione, un solo blocco, verosimiglianza, lettura di U_k e degli stati, perché Viterbi non ripercorre la storia); 2026-11-23 — versione aggiornata delle slide (signaling_bandlimited_channel_NEW.pdf): equalizzazione frazionaria, ZF e MMSE con derivazioni, coefficienti β(ℓ) e memoria del canale, (15)–(16) corrette e nuovi indici della ricorsione U/V, appunti a lezione; 2026-11-20 — revisione della traduzione delle slide; 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf (Lezione 14)_
