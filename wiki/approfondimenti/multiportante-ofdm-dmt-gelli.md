---
tipo: approfondimento
esame: no
lezione_collegata: 15
fonti_pdf: ["Note 2001 Gelli G.pdf"]
---

# Modulazione multiportante, OFDM e DMT — note di G. Gelli

> 📚 **Approfondimento, non materia d'esame.** Dispensa di Giacinto Gelli (maggio 2001, 24 pagine), da leggere dopo la [[signaling-ofdm|Lezione 15]]. Per l'esame valgono le slide della prof. Darsena e le pagine [[ofdm]], [[prefisso-ciclico]], [[ofdm-con-fft]], [[equalizzazione-ofdm]], [[limiti-dell-ofdm]]. Questa pagina riassume le note e ne espande i calcoli; non viene richiamata nel corso completo.

## Come si lega alla Lezione 15 · [[Note 2001 Gelli G.pdf#page=1|p. 1]]–[[Note 2001 Gelli G.pdf#page=3|3]], [[Note 2001 Gelli G.pdf#page=10|10]], [[Note 2001 Gelli G.pdf#page=13|13]], [[Note 2001 Gelli G.pdf#page=17|17]]

Le note seguono lo stesso percorso delle slide (impulsi ortogonali, spettro, canale e tempo di guardia, realizzazione con DFT, prefisso ciclico) e aggiungono due parti che le slide non hanno: le **prestazioni** QAM per sottoportante e il **bit loading** ottimo (*water filling*). Le notazioni però sono diverse, e conviene saperlo prima di confrontare le formule:

| Grandezza | Note di Gelli | Slide della Lezione 15 |
|---|---|---|
| durata del blocco senza guardia | $T$ (spaziatura $1/T$) | $T_u$ (spaziatura $1/T_u$) |
| blocco con guardia | $T=T_g+T_u$, impulsi normalizzati su $T$ ($R_T=1/\sqrt T$) | $T=T_u+T_g$, impulsi normalizzati su $T_u$ |
| guadagno sulla sottoportante | $\frac{T_u}{T}H(i/T_u)$ | $H(i/T_u)$ (il fattore $T_u/T$ è nella nota della slide 26) |
| IDFT / DFT | $A_k=\frac1N\sum_ia_ie^{j2\pi ik/N}$, DFT senza fattore | entrambe unitarie, $1/\sqrt N$ |
| rumore in banda base | $r_n(\tau)=2N_0\delta(\tau)$ (passa-banda $N_0/2$) | $E\{w(t)w^\ast(u)\}=N_0\delta(t-u)$ |
| energia | $\mathcal E$ = energia a radiofrequenza, $E=2\mathcal E$ quella dell'equivalente passabasso | inviluppo con $\sqrt2$, stesse energie |
| campioni del prefisso | $L$, canale lungo $M$ campioni | $L_{cp}$, canale con tap $0,\dots,L_h$ |

> 💡 Connessione: la slide 26 dice che "negli appunti a mano della lezione" gli impulsi possono essere normalizzati su $T$ invece che su $T_u$, e allora $r_i[n]=\frac{T_u}{T}H(i/T_u)a_i[n]+w_i[n]$: è esattamente la (46)–(48) di queste note.

## 1. Introduzione: cos'è la modulazione multiportante · [[Note 2001 Gelli G.pdf#page=1|p. 1]], [[Note 2001 Gelli G.pdf#page=2|2]]

- La **modulazione multiportante** trasporta un flusso di bit con segnali modulati a portanti diverse: è la somma di $N$ segnali indipendenti con la stessa banda e portanti $f_i$, $i=0,\dots,N-1$, detti **sottoportanti** o **sottocanali**, modulati di solito PSK o QAM.
- A differenza della FDM convenzionale si può assegnare un numero diverso di bit a ogni sottoportante (**bit loading**) per ottimizzare le prestazioni.

> ⚠️ Contraddizione (refuso nelle note): a p. 1 si legge che si fa in modo che le sottoportanti che incontrano una **minore** attenuazione e/o maggior rumore trasportino meno bit. Dalla (112) di p. 20 il numero di bit cresce con $\mathcal E_i\lvert H_i\rvert^2/\sigma_i^2$: sono le sottoportanti con **maggiore** attenuazione (o più rumore) a portare meno bit.

- **Vantaggi** (sezione 1.1): con il bit loading si arriva con relativa semplicità a velocità vicine ai limiti della teoria dell'informazione; abbassando il tasso di simbolo sul canale si riduce molto l'ISI e quindi la complessità degli equalizzatori. Più complessa della portante singola, introdotta più di 40 anni prima nei primi modem (sistema **Kineplex**), è diventata interessante solo con le realizzazioni numeriche a bassa complessità (FFT).
- **Due realizzazioni** (sezione 1.2): **OFDM** per applicazioni punto-multipunto (broadcast), in genere senza allocazione ottima dei bit; **DMT** (*discrete multitone*) per applicazioni punto-punto, tipicamente DSL, con bit loading.
- **Svantaggi** (sezione 1.3): oltre alla complessità, (1) l'elevato rapporto tra potenza di picco e potenza media: l'ampiezza, somma di molti contributi indipendenti, tende ad avere distribuzione **gaussiana** e quindi un fattore di cresta elevato, che mette alla prova la linearità degli amplificatori; (2) la sensibilità agli errori di sincronizzazione nel tempo e in frequenza (anche per effetto Doppler), che introducono ISI e ICI.
- **Applicazioni** (sezione 1.4, situazione del 2001): DMT in HDSL e ADSL per l'accesso a larga banda nel local loop, proposto anche per le power line; OFDM nel DAB e nel DVB-T (circa 20 Mbit/s), proposto per i sistemi radiomobili di terza generazione, HIPERLAN/2 e un'evoluzione di IEEE 802.11 fino a 54 Mbit/s; sistemi ibridi OFDM/CDMA (MC-CDMA), in cui più utenti condividono le sottoportanti.

## 2. Principio della modulazione multiportante · [[Note 2001 Gelli G.pdf#page=2|p. 2]]–[[Note 2001 Gelli G.pdf#page=4|4]]

Flusso binario $d(n)$ a $R_b=1/T_b$, periodo di simbolo multiportante $T\gg T_b$. Un buffer (S/P) accumula $B=R_bT$ bit nell'intervallo $[nT,(n+1)T]$, formando il blocco $\mathbf d(n)=[d_0(n),\dots,d_{B-1}(n)]^T$ con $d_i(n)=d(nB+i)$. Un **codificatore** (mapping) trasforma il blocco nel vettore $\mathbf a(n)=[a_0(n),\dots,a_{N-1}(n)]^T$ di $N\le B$ simboli complessi, uno per sottocanale. Figura 1: S/P, codificatore, $N$ rami con impulsi $p_i(t-nT)$, somma $x(t)$, canale con rumore $n(t)$, banco di correlatori con $p_i^\ast(t-nT)$, decisione, decodificatore, P/S.

Con modulazione lineare la **frame multicanale** e il segnale sono

$$f_n(t)=\sum_{i=0}^{N-1}a_i(n)\,p_i(t-nT)\quad(1),\qquad x(t)=\sum_{n=-\infty}^{\infty}\sum_{i=0}^{N-1}a_i(n)\,p_i(t-nT)\quad(2)$$

Correlando con $p_i(t-nT)$ (sistema ideale, senza canale né rumore):

$$r_i(n)=\sum_{m}\sum_{k}a_k(m)\int_{-\infty}^{\infty}p_k(t-mT)\,p_i^\ast(t-nT)\,dt\quad(3)$$

A $r_i(n)$ contribuiscono, oltre a $a_i(n)$, i simboli $a_i(m)$ con $m\neq n$ (**ISI**) e $a_k(m)$ con $k\neq i$ (**ICI**, interferenza intercanale); la loro entità dipende dal prodotto scalare tra gli impulsi. Con la **condizione di biortogonalità**

$$\langle p_k(t-mT),p_i(t-nT)\rangle=\delta_{k-i}\,\delta_{m-n}\quad(4)\qquad\Rightarrow\qquad r_i(n)=a_i(n)\quad(5)$$

si annullano ISI e ICI: un sistema multicanale ideale. La (4) implica impulsi a energia unitaria. Nota 1: poiché $p_i(t)$ è un equivalente passabasso, la sua energia è in genere il doppio di quella dell'impulso a radiofrequenza; nelle note $\mathcal E_i$ indica quest'ultima, quindi $E_i=2\mathcal E_i$.

### Derivazione — Impulsi rettangolari biortogonali, (6)–(13) · [[Note 2001 Gelli G.pdf#page=4|p. 4]]

**Si parte da:** $R_T(t)=1/\sqrt T$ per $t\in[0,T]$, $0$ altrove (6), e $p_i(t)=R_T(t)e^{j2\pi f_it}$ (7).

$$
\begin{aligned}
\langle p_k(t-mT),p_i(t-nT)\rangle&=\int R_T(t-mT)e^{j2\pi f_k(t-mT)}R_T(t-nT)e^{-j2\pi f_i(t-nT)}dt && \text{definizione}\\
&=\frac1T\,\delta_{n-m}\int_{nT}^{(n+1)T}e^{j2\pi f_k(t-nT)}e^{-j2\pi f_i(t-nT)}dt && \text{le finestre si sovrappongono solo per } m=n\\
&=\frac1T\,\delta_{n-m}\,e^{-j2\pi(f_k-f_i)nT}\int_{nT}^{(n+1)T}e^{j2\pi(f_k-f_i)t}dt && (8)\\
&=\delta_{n-m}\,e^{j\pi(f_k-f_i)T}\,\text{sinc}\big((f_k-f_i)T\big) && \text{🧩 integrale come nella slide 11}
\end{aligned}
$$

L'ultima riga si annulla se la spaziatura è un multiplo non nullo di $1/T$; il valore minimo è $1/T$, che dà la massima efficienza spettrale: $p_i(t)=R_T(t)e^{j2\pi\frac iTt}$ (9). Poiché $e^{-j2\pi in}=1$, $p_i(t-nT)=R_T(t-nT)e^{j2\pi\frac iTt}$ (10), quindi

$$x(t)=\sum_n\Big[\sum_{i=0}^{N-1}a_i(n)e^{j2\pi\frac iTt}\Big]R_T(t-nT)\quad(11),\qquad r_i(n)=\int x(t)R_T(t-nT)e^{-j2\pi\frac iTt}dt=a_i(n)\quad(12)\text{–}(13)$$

**Sanity check:** è la derivazione della slide 10 con $T$ al posto di $T_u$.

### 2.1 Struttura del codificatore · [[Note 2001 Gelli G.pdf#page=4|p. 4]], [[Note 2001 Gelli G.pdf#page=5|5]]

Il blocco di $B$ bit si divide in $N$ sottoblocchi $\mathbf d_i(n)$ di $b_i$ bit, con $B=\sum_ib_i$ (14). Il sottoblocco $i$ assume uno di $M_i=2^{b_i}$ valori, quindi la sottoportante $i$ usa una modulazione a $M_i$ livelli (PSK o QAM). In mancanza di altre informazioni si sceglie $b_i=B/N$ e $M_i=2^{B/N}$, con potenze uguali: è il caso tipico dell'**OFDM**, usato nel punto-multipunto, dove non c'è canale di ritorno e non si può ottimizzare per più utenti. Allocare bit e potenze in modo diverso (**bit loading**) serve quando alcune sottoportanti sono più sfavorite: è usato nei **DMT**, punto-punto, dove c'è un canale di ritorno (sezione 6).

### 2.2 Spettro di un sistema multiportante · [[Note 2001 Gelli G.pdf#page=5|p. 5]]–[[Note 2001 Gelli G.pdf#page=7|7]]

Con bit i.i.d. in ingresso, i simboli $a_i(n)$ e $a_j(n)$ ($i\neq j$) sono indipendenti (sottoblocchi diversi dello stesso blocco), e così $a_i(n)$, $a_j(m)$ con $n\neq m$ (blocchi diversi): ogni sequenza è i.i.d. e sequenze diverse sono indipendenti. Con media nulla vale la biortogonalità statistica $E[a_i(n)a_j^\ast(m)]=\sigma_{a_i}^2\delta_{i-j}\delta_{n-m}$ (16).

$$
\begin{aligned}
r_x(t,\tau)&=E[x(t)x^\ast(t-\tau)]=\sum_{i=0}^{N-1}\sigma_{a_i}^2\sum_np_i(t-nT)p_i^\ast(t-\tau-nT)=\sum_i\sigma_{a_i}^2\,\text{rep}_T\big[p_i(t)p_i^\ast(t-\tau)\big] && (17)\\
r_x(\tau)&=\langle r_x(t,\tau)\rangle=\frac1T\sum_i\sigma_{a_i}^2\,r_{p_i}(\tau),\qquad r_{p_i}(\tau)=\int p_i(t)p_i^\ast(t-\tau)dt && (18)\text{–}(19)\\
S_x(f)&=\frac1T\sum_i\sigma_{a_i}^2\lvert P_i(f)\rvert^2,\qquad P_i(f)=\sqrt T\,\text{sinc}(fT-i)\,e^{-j\pi(fT-i)} && (20)\text{–}(22)\\
S_x(f)&=\sum_{i=0}^{N-1}\sigma_{a_i}^2\,\text{sinc}^2(fT-i) && (23)
\end{aligned}
$$

$\text{rep}_T$ è la replicazione con passo $T$: $r_x(t,\tau)$ è periodica in $t$, il segnale è **ciclostazionario** di periodo $T$ e si media su $t$. La figura 2 mostra la PSD per $N=8$ con simboli di valore quadratico medio unitario: spettro complessivo continuo, sottoportanti tratteggiate.

### Derivazione — Occupazione di banda (24) · [[Note 2001 Gelli G.pdf#page=7|p. 7]]

$$
\begin{aligned}
B_T&=\frac{N-1}{T}+\frac2T && \text{dal centro della prima a quello dell'ultima: }(N-1)/T;\ \text{più mezzo lobo principale } (1/T) \text{ per lato}\\
&=\frac{N+1}{T}\simeq\frac NT && N\gg1\ (\text{valori tipici da } 64)
\end{aligned}
$$

Gli spettri si sovrappongono molto: l'efficienza spettrale è molto maggiore (circa doppia) di una FDM convenzionale. Il prezzo è l'elevata sensibilità agli errori di sincronizzazione, nel tempo e in frequenza, che distruggono l'ortogonalità.

## 3. Prestazioni in AWGN · [[Note 2001 Gelli G.pdf#page=7|p. 7]]–[[Note 2001 Gelli G.pdf#page=10|10]]

Rumore AWGN con PSD $N_0/2$; il suo equivalente passabasso $n(t)$ è SSL a media nulla con $r_n(\tau)=E[n(t)n^\ast(t-\tau)]=2N_0\delta(\tau)$ (26) e autocorrelazione coniugata nulla (simmetria circolare). Il correlatore dà $r_i(n)=a_i(n)+n_i(n)$ (27), con $n_i(n)=\int n(t)R_T(t-nT)e^{-j2\pi\frac iTt}dt$ (28).

### Derivazione — Correlazione del rumore (29) · [[Note 2001 Gelli G.pdf#page=7|p. 7]], [[Note 2001 Gelli G.pdf#page=8|8]]

$$
\begin{aligned}
E[n_i(n)n_j^\ast(k)]&=\iint E[n(t)n^\ast(u)]\,R_T(t-nT)R_T(u-kT)\,e^{-j2\pi\frac iTt}e^{j2\pi\frac jTu}\,dt\,du && \text{linearità}\\
&=2N_0\int R_T(t-nT)R_T(t-kT)\,e^{-j2\pi\frac{i-j}{T}t}dt && E[n(t)n^\ast(u)]=2N_0\delta(t-u)\\
&=2N_0\,\delta_{n-k}\,\delta_{i-j} && \text{biortogonalità}
\end{aligned}
$$

Rumori gaussiani, incorrelati e quindi indipendenti, con varianza $\sigma^2=2N_0$. Decisione $\hat a_i(n)=\mathcal D_i[a_i(n)+n_i(n)]$ (30); nota 2: con ISI e ICI la decisione ottima userebbe congiuntamente più simboli e più canali, ma nelle condizioni ideali i canali sono indipendenti e si decide simbolo per simbolo. Con QAM su ogni sottoportante il sistema ideale equivale a **$N$ canali QAM a portante singola indipendenti**.

> 💡 Connessione: con la convenzione delle slide il rumore ha varianza $N_0$ (slide 14); qui $2N_0$ perché la PSD passa-banda è $N_0/2$ e l'equivalente passabasso definito senza $\sqrt2$ la moltiplica per 4. I rapporti segnale/rumore finali coincidono, perché anche l'energia dei simboli è raddoppiata ($E=2\mathcal E$).

### 3.1 QAM a portante singola · [[Note 2001 Gelli G.pdf#page=8|p. 8]], [[Note 2001 Gelli G.pdf#page=9|9]]

Modello $r(n)=Ha(n)+n(n)$ (31), figura 3, con guadagno complesso $H$ del canale e rumore bianco di potenza $\sigma^2=2N_0$. Costellazione QAM quadrata con $M=2^b$ punti ($b$ pari), distanza $d$ tra simboli adiacenti (figura 4: 64-QAM), simboli equiprobabili.

### Derivazione — Potenza della costellazione (32) · [[Note 2001 Gelli G.pdf#page=8|p. 8]]

$$
\begin{aligned}
L&=\sqrt M && \text{livelli per asse (QAM} = \text{due ASK in quadratura)}\\
E[(\text{Re}\,a)^2]&=\frac{d^2}{4}\cdot\frac{2}{L}\sum_{k=1}^{L/2}(2k-1)^2=\frac{d^2}{4}\cdot\frac{L^2-1}{3}=\frac{(L^2-1)d^2}{12} && \text{livelli } \pm\tfrac d2,\pm\tfrac{3d}2,\dots;\ \textstyle\sum_{k=1}^{m}(2k-1)^2=\tfrac{m(4m^2-1)}3\\
\sigma_a^2&=E[\lvert a\rvert^2]=2\cdot\frac{(M-1)d^2}{12}=\frac{M-1}{6}\,d^2 && \text{due assi, } L^2=M
\end{aligned}
$$

**Sanity check:** 4-QAM ($M=4$): punti $(\pm\frac d2,\pm\frac d2)$, $\lvert a\rvert^2=\frac{d^2}{2}=\frac{3}{6}d^2$ ✓. Vale esattamente per $M$ potenza di 4 (4, 16, 64, 256, 1024-QAM); per $b$ dispari è solo un'approssimazione.

### Derivazione — Probabilità d'errore QAM (34)–(39) · [[Note 2001 Gelli G.pdf#page=9|p. 9]]

**Si parte da:** QAM = due ASK in quadratura, ciascuna con $\sqrt M$ livelli e metà dell'energia; i due flussi si separano perfettamente.

$$
\begin{aligned}
P_{QAM}&=1-(1-P_{ASK})^2\simeq2P_{ASK} && (34):\ \text{corretto solo se entrambe giuste}; P_{ASK}\ll1\\
P_{ASK}&=2\Big(1-\frac{1}{\sqrt M}\Big)Q\Big(\frac{d\lvert H\rvert/2}{\sqrt{\sigma^2/2}}\Big) && \text{🧩 ASK: errore se il rumore di un asse supera metà distanza}\\
\frac{d\lvert H\rvert/2}{\sqrt{\sigma^2/2}}&=\frac{d\lvert H\rvert}{\sqrt2\,\sigma}=\sqrt{\frac{3}{M-1}\frac{\lvert H\rvert^2\mathcal E}{N_0}} && 2\mathcal E=\tfrac{M-1}6d^2\ (37),\ \sigma^2=2N_0\\
P_{QAM}&\simeq4\Big(1-\frac1{\sqrt M}\Big)Q\Big(\sqrt{\frac{3}{M-1}\frac{\lvert H\rvert^2\mathcal E}{N_0}}\Big)=4\Big(1-\frac1{\sqrt M}\Big)Q\Big(\frac{d\lvert H\rvert}{\sqrt2\sigma}\Big) && (36),\ (38)\\
\text{BER}_{QAM}&\simeq\frac{P_{QAM}}{\log_2M} && (39):\ \text{codifica di Gray, un bit sbagliato per simbolo sbagliato}
\end{aligned}
$$

Il fattore $2(1-1/\sqrt M)$ conta che i livelli interni hanno due vicini e quelli esterni uno solo. La (36) è comunque un limite superiore per QAM con $b$ qualsiasi. Nota 3: le note di Proakis usano $\text{erfc}$, con $Q(x)=\frac12\text{erfc}(x/\sqrt2)$.

**Sanity check:** $M=4$: $P_{QAM}\simeq2Q\big(\sqrt{\lvert H\rvert^2\mathcal E/N_0}\big)$, cioè ogni asse è una BPSK con energia $\mathcal E/2$ per bit, come la QPSK della Lezione 10.

### 3.2 QAM multiportante · [[Note 2001 Gelli G.pdf#page=10|p. 10]]

Senza effetti del canale ($H=1$) e con rumore bianco, ha senso usare la stessa QAM ($M=2^b$) e la stessa energia $\mathcal E/N$ su ogni sottoportante, come nell'OFDM: tutte hanno la stessa probabilità d'errore, quella del sistema,

$$P_M\simeq4\Big(1-\frac1{\sqrt M}\Big)Q\Big(\sqrt{\frac{3}{M-1}\frac{\mathcal E}{NN_0}}\Big)\quad(40),\qquad\text{BER}_M=\frac{4}{\log_2M}\Big(1-\frac1{\sqrt M}\Big)Q(\cdot)\quad(41)$$

Con il canale, le probabilità sulle sottoportanti differiscono: il sistema ha una probabilità media o è dominato dalla peggiore, e non ha più senso usare modulatori uguali (sezione 6).

## 4. Effetti del canale e tempi di guardia · [[Note 2001 Gelli G.pdf#page=10|p. 10]]–[[Note 2001 Gelli G.pdf#page=13|13]]

Ridurre il tasso di simbolo per sottoportante mitiga l'ISI, ma ne resta un residuo, e c'è l'ICI. Si divide allora $T$ in un **tempo di guardia** $T_g$ e un tempo utile $T_u$ ($T=T_g+T_u$) e la spaziatura diventa $1/T_u$ invece di $1/T$. Tre conseguenze: (1) gli impulsi sono biortogonali su $T_u$, non più su $T$; (2) la banda aumenta perché aumenta la spaziatura; (3) l'energia per la rivelazione si riduce, perché una frazione $T_g/T$ si spende nella guardia.

Segnale trasmesso $x(t)=\sum_n\big[\sum_ia_i(n)e^{j2\pi\frac{i}{T_u}t}\big]R_T(t-nT)$ (42), canale LTI causale $r(t)=x(t)\ast h(t)+n(t)$ (43) con risposta di durata $T_h\le T$: ISI solo dalla frame precedente. Il ricevitore integra su $[nT+T_g,(n+1)T]$, di ampiezza $T_u$, dove arrivano solo la frame $n$ e la $n-1$ (44).

### Derivazione — Uscita del correlatore con tempo di guardia (45)–(48) · [[Note 2001 Gelli G.pdf#page=11|p. 11]], [[Note 2001 Gelli G.pdf#page=12|12]]

$$
\begin{aligned}
r_i(n)&=\int_{nT+T_g}^{(n+1)T}r(t)\,R_T(t-nT)\,e^{-j2\pi\frac{i}{T_u}t}dt && \text{finestra utile, ampiezza } 1/\sqrt T\\
&=\frac{1}{\sqrt T}\sum_ka_k(n)\int_{nT+T_g}^{(n+1)T}\!\!\int_0^{T_h}h(\tau)e^{-j2\pi\frac{k}{T_u}\tau}e^{j2\pi\frac{k-i}{T_u}t}R_T(t-\tau-nT)\,d\tau\,dt+(\text{termine in } a_k(n-1)) && (45)\\
&t-\tau\in[nT+T_g-T_h,(n+1)T]\subseteq[nT,(n+1)T]\ \text{se } T_g\ge T_h\ \Rightarrow\ R_T(t-\tau-nT)=1/\sqrt T && \text{primo integrale}\\
&R_T(t-\tau-(n-1)T)\neq0\iff(n-1)T+\tau<t<nT+\tau\le nT+T_g && \text{nessuna intersezione con } [nT+T_g,(n+1)T]\\
r_i(n)&=\sum_ka_k(n)\underbrace{\int_0^{T_h}h(\tau)e^{-j2\pi\frac{k}{T_u}\tau}d\tau}_{H(k/T_u)}\cdot\frac1T\int_{nT+T_g}^{(n+1)T}e^{j2\pi\frac{k-i}{T_u}t}dt && \text{il secondo integrale si annulla}\\
\frac1T\int_{nT+T_g}^{(n+1)T}e^{j2\pi\frac{k-i}{T_u}t}dt&=\frac{T_u}{T}\,\delta_{k-i} && (47):\ \text{intervallo lungo } T_u,\ k-i \text{ periodi interi}\\
r_i(n)&=\frac{T_u}{T}\,a_i(n)\,H\Big(\frac{i}{T_u}\Big)+n_i(n) && (46),\ (48)
\end{aligned}
$$

Il sistema equivale a **$N$ canali AWGN indipendenti** con fattori di scala diversi, i campioni di $H(f)$ a passo $1/T_u$. Con $H_i=H(i/T_u)$ e $\gamma=T_g/T$ (in pratica tipicamente $0.25$): $r_i(n)=(1-\gamma)H_ia_i(n)+n_i(n)$ (49).

### Derivazione — Energia, rumore e probabilità d'errore con la guardia (50)–(55) · [[Note 2001 Gelli G.pdf#page=12|p. 12]], [[Note 2001 Gelli G.pdf#page=13|13]]

$$
\begin{aligned}
2\mathcal E_i&=\sigma_{a_i}^2 && (50):\ \text{energia trasmessa per la portante } i\\
\text{segnale utile}&\to(1-\gamma)^2\lvert H_i\rvert^2\,\sigma_{a_i}^2 && \text{dalla (49)}\\
E[\lvert n_i(n)\rvert^2]&=2N_0\,\frac{T_u}{T}=2N_0(1-\gamma) && (51):\ \text{si integra su } T_u \text{ con ampiezza } 1/\sqrt T\\
\frac{\text{segnale}}{\text{rumore}}&\ \propto\ \frac{(1-\gamma)^2\lvert H_i\rvert^2}{(1-\gamma)}=\lvert H_i\rvert^2(1-\gamma) && (52)\\
P_i&=4\Big(1-\frac{1}{\sqrt{M_i}}\Big)Q\Big(\sqrt{\frac{3}{M_i-1}\frac{\mathcal E_i(1-\gamma)}{N_0}}\Big) && (53)\\
\text{BER}&=\frac1N\sum_{i=0}^{N-1}\text{BER}_i && (55),\ \text{con } \text{BER}_i \text{ come la (54)}
\end{aligned}
$$

> ⚠️ Contraddizione (nelle note): la (52) dice che il contrasto di energia si modifica del fattore $\lvert H_i\rvert^2(1-\gamma)$, ma la (53) e la (54) riportano sotto radice solo $\mathcal E_i(1-\gamma)/N_0$, senza $\lvert H_i\rvert^2$. Coerentemente con la (36) e con la (52) l'argomento dovrebbe essere $\frac{3}{M_i-1}\frac{\lvert H_i\rvert^2\mathcal E_i(1-\gamma)}{N_0}$ (a meno che $\mathcal E_i$ indichi già l'energia ricevuta, cosa che il testo non dice).

Nota 4: si potrebbe non trasmettere affatto durante la guardia, ma la trasmissione discontinua darebbe seri problemi di compatibilità elettromagnetica. Con BER diverse sulle portanti, la BER complessiva è dominata dalle peggiori: in un sistema ottimizzato la BER è la stessa su tutte, e per BER e potenza fissate si assegnano i bit per massimizzare la velocità (sezione 6).

## 5. Realizzazione mediante FFT · [[Note 2001 Gelli G.pdf#page=13|p. 13]]–[[Note 2001 Gelli G.pdf#page=19|19]]

Proposta già negli anni '50 (Kineplex), la tecnica non si è diffusa per la difficoltà di realizzarla in analogico: era impossibile costruire oscillatori abbastanza stabili da garantire l'ortogonalità. Il problema è stato superato dalle tecnologie numeriche e dalla FFT.

### Derivazione — Spettro della frame e campionamento (56)–(59) · [[Note 2001 Gelli G.pdf#page=13|p. 13]], [[Note 2001 Gelli G.pdf#page=14|14]]

**Si parte da:** la frame $f_n(t)=\sum_ia_i(n)e^{j2\pi\frac iTt}R_T(t-nT)$ (56), con i simboli trattati come deterministici.

$$
\begin{aligned}
\mathcal F\{R_T(t)\}&=\frac{1}{\sqrt T}\int_0^Te^{-j2\pi ft}dt=\sqrt T\,\text{sinc}(fT)\,e^{-j\pi fT} && \text{finestra}\\
\mathcal F\{R_T(t-nT)e^{j2\pi\frac iTt}\}&=\sqrt T\,\text{sinc}(fT-i)\,e^{-j\pi(fT-i)}\,e^{-j2\pi(fT-i)n} && \text{ritardo } nT \text{ e traslazione di } i/T\\
F_n(f)&=\sum_ia_i(n)\sqrt T\,\text{sinc}(fT-i)\,e^{-j\pi(fT-i)(2n+1)} && \text{🧩 forma che ricavo}
\end{aligned}
$$

> ⚠️ Contraddizione (refuso probabile nella (57)): le note scrivono la fase come $e^{-j\pi(fT-i)(n-0.5)}$; dal calcolo sopra viene $e^{-j\pi(fT-i)(2n+1)}=e^{-j2\pi(fT-i)(n+0.5)}$. Il modulo, l'unica cosa che serve per la banda, è lo stesso.

La banda non è limitata (sinc), ma in pratica è circa $2W=N/T$ per $N\gg1$: per il teorema del campionamento basta il passo $T_c=1/(2W)=T/N$, e in $[nT,(n+1)T]$ ci sono esattamente $N$ campioni:

$$
\begin{aligned}
f_n(nT+kT_c)&=\frac{1}{\sqrt T}\sum_ia_i(n)e^{j2\pi\frac iT(nT+k\frac TN)}=\frac{1}{\sqrt T}\sum_ia_i(n)e^{j2\pi\frac{ik}N} && e^{j2\pi in}=1\\
&=\frac{N}{\sqrt T}A_k(n),\qquad A_k(n)=\text{IDFT}[a_i(n)]=\frac1N\sum_{i=0}^{N-1}a_i(n)e^{j2\pi\frac{ik}N} && (58)\text{–}(59)
\end{aligned}
$$

Si genera quindi il segnale con la IDFT, una conversione P/S e un D/A a passo $T_c=T/N$ (figura 5): con $h_{D/A}(t)$ risposta del convertitore (idealmente una sinc, serie di Shannon) $x(t)=\frac{N}{\sqrt T}\sum_n\sum_kA_k(n)h_{D/A}(t-nT-kT_c)$ (60). Con $A_k(n)=A(nN+k)$ (61), la **decomposizione polifase** di $A(n)$, diventa $x(t)=\frac N{\sqrt T}\sum_nA(n)h_{D/A}(t-nT_c)$ (62).

### Derivazione — Ricezione ideale con convertitori sinc (63)–(73) · [[Note 2001 Gelli G.pdf#page=14|p. 14]], [[Note 2001 Gelli G.pdf#page=15|15]]

$$
\begin{aligned}
r_{filt}(t)&=x(t)\ast h_{A/D}(t)=\frac N{\sqrt T}\sum_nA(n)\,h_{conv}(t-nT_c),\quad h_{conv}=h_{D/A}\ast h_{A/D} && (63)\\
r_k(n)&=r_{filt}(nT+kT_c)=\sum_mA(m)\,h_{conv}(nN+k-m),\quad h_{conv}(n)\triangleq\tfrac{N}{\sqrt T}h_{conv}(nT_c) && (64)\text{–}(66),\ T=NT_c\\
h_{D/A}&=\text{sinc}(t/T_c),\quad h_{A/D}=\tfrac1{\sqrt T}\text{sinc}(t/T_c) && (67)\text{–}(68)\\
h_{conv}(t)&=\frac1{\sqrt T}\,T_c\,\text{sinc}(t/T_c)=\frac{\sqrt T}{N}\text{sinc}(t/T_c) && (69):\ \text{🧩 } \mathcal F\{\text{sinc}(t/T_c)\}=T_c\Pi(fT_c),\ \text{prodotto } T_c^2\Pi\\
h_{conv}(n)&=\frac N{\sqrt T}\cdot\frac{\sqrt T}{N}\,\text{sinc}(n)=\delta(n) && (70)\\
r_k(n)&=A(nN+k)=A_k(n),\qquad s_i(n)=\text{DFT}[r_k(n)]=\sum_kr_k(n)e^{-j2\pi\frac{ik}N}=a_i(n) && (71)\text{–}(73)
\end{aligned}
$$

ISI e ICI si eliminano del tutto: basta una DFT per riavere i simboli.

### Derivazione — Varianza del rumore dopo la DFT (74)–(86) · [[Note 2001 Gelli G.pdf#page=15|p. 15]], [[Note 2001 Gelli G.pdf#page=16|16]]

$$
\begin{aligned}
S_{n_{filt}}(f)&=2N_0\lvert H_{A/D}(f)\rvert^2=2N_0\frac{T_c^2}{T}\Pi(fT_c) && (75),\ (82)\text{–}(83):\ H_{A/D}=\tfrac{T_c}{\sqrt T}\Pi(fT_c)\\
r_{n_{filt}}(\tau)&=2N_0\frac{T_c}{T}\,\text{sinc}(\tau/T_c)\ \Rightarrow\ r_{n_{filt}}[(k-h)T_c]=2N_0\frac{T_c}{T}\delta_{k-h} && (84)\text{–}(85):\ \text{campioni incorrelati}\\
\text{VAR}[w_i(n)]&=\sum_{k,h}E[n_k(n)n_h^\ast(n)]e^{-j2\pi\frac{i(k-h)}N}=\sum_{k=0}^{N-1}2N_0\frac{T_c}{T}=2N_0\frac{T_c}{T}N=2N_0 && (79),\ (86):\ T=NT_c
\end{aligned}
$$

È la stessa varianza del ricevitore a tempo continuo (29): con convertitori ideali la realizzazione con DFT non peggiora le prestazioni rispetto al banco di oscillatori analogici. $s_i(n)=a_i(n)+w_i(n)$ (78), con $w_i(n)$ gaussiano a media nulla.

### 5.2 Prefisso ciclico · [[Note 2001 Gelli G.pdf#page=17|p. 17]]–[[Note 2001 Gelli G.pdf#page=19|19]]

Con la DFT il tempo di guardia si realizza con il **prefisso ciclico**: al prodotto delle DFT corrisponde la convoluzione **circolare**, mentre il canale fa una convoluzione lineare; premettendo agli $N$ campioni della IDFT la copia degli ultimi $L\le N$, il canale "vede" periodica la sequenza e la convoluzione lineare coincide con quella circolare. Con $P=N+L$:

$$
\begin{aligned}
\tilde A_p(n)&=\begin{cases}A_{p+N}(n), & p=-L,\dots,-1\\ A_p(n), & p=0,\dots,N-1\end{cases}\ \Rightarrow\ \tilde A_p(n)=\frac1N\sum_ia_i(n)e^{j2\pi\frac{ip}N},\ p=-L,\dots,N-1 && (88)\text{–}(90):\ e^{j2\pi i(p+N)/N}=e^{j2\pi ip/N}\\
\tilde A_p(n)&=\tilde A(nP+p),\quad T_c=T/P,\quad x(t)=\tfrac N{\sqrt T}\textstyle\sum_n\tilde A(n)h_{D/A}(t-nT_c) && (91)\text{–}(92)\\
r_p(n)&=\sum_{m=0}^{M-1}h_{tot}(m)\,\tilde A(nP+p-m),\quad h_{tot}=h_{D/A}\ast h\ast h_{A/D},\ M=\lceil T_h/T_c\rceil && (93)\text{–}(97)\\
r_p(n)&=\underbrace{\sum_{m=0}^{p+L}h_{tot}(m)\tilde A_{p-m}(n)}_{\text{frame } n}+\underbrace{\sum_{m=p+L+1}^{M-1}h_{tot}(m)\tilde A_{P+p-m}(n-1)}_{\text{ISI dalla frame } n-1} && (98)\text{–}(100):\ p-m\ge-L \text{ oppure } <-L
\end{aligned}
$$

Scartando i primi $L$ valori ($p=0,\dots,N-1$, cioè **rimozione del prefisso**) la seconda somma è vuota purché $L\ge M$, perché $h_{tot}(m)=0$ per $m\ge M$ (101): è la condizione $T_g\ge T_h$ del tempo di guardia. 🧩 Per $p=0$ la somma va da $m=L+1$ a $M-1$ ed è vuota già con $L\ge M-1$: è la condizione $L_{cp}\ge L_h$ delle slide, con $L_h=M-1$ ultimo tap; le note usano la condizione appena più forte $L\ge M$.

$$
\begin{aligned}
r_p(n)&=\sum_{m}h_{tot}(m)\frac1N\sum_ia_i(n)e^{j2\pi\frac{i(p-m)}N}=\frac1N\sum_ia_i(n)e^{j2\pi\frac{ip}N}\underbrace{\sum_{m=0}^{M-1}h_{tot}(m)e^{-j2\pi\frac{im}N}}_{H_{tot}(i)} && (102)\text{–}(104)\\
r_p(n)&=\text{IDFT}[a_i(n)H_{tot}(i)]\ \Rightarrow\ s_i(n)=\text{DFT}[r_p(n)]=a_i(n)\,H_{tot}(i) && (105)\text{–}(107)
\end{aligned}
$$

Si riottengono i simboli a meno di un fattore complesso, che si compensa con un **equalizzatore a una sola presa**. In AWGN il contrasto di energia per sottoportante si modifica del fattore $\lvert H_{tot}(i)\rvert^2(1-\gamma)$ con $\gamma=L/P$, la frazione di campioni spesi per il prefisso.

## 6. Bit loading · [[Note 2001 Gelli G.pdf#page=19|p. 19]]–[[Note 2001 Gelli G.pdf#page=22|22]]

Se il canale non è ideale o il rumore cambia da sottoportante a sottoportante (rumore non bianco: nei DSL domina la diafonia NEXT/FEXT, nota 5), conviene allocare un numero diverso di bit alle sottoportanti: **bit loading** o precodifica. Si usa nel punto-punto, dove un canale di ritorno permette al ricevitore di comunicare al trasmettitore una stima dell'SNR per sottoportante (per esempio nei modem ADSL in downstream). Con guardia o CP il sistema è ricondotto a $N$ canali AWGN indipendenti (figura 6), con guadagno $H_i$ e rumore di potenza $\sigma_i^2$.

### Derivazione — Bit per sottoportante a probabilità d'errore fissata (108)–(113) · [[Note 2001 Gelli G.pdf#page=19|p. 19]], [[Note 2001 Gelli G.pdf#page=20|20]]

**Si parte da:** la (38) con $M_i\gg1$, cioè $1-1/\sqrt{M_i}\simeq1$.

$$
\begin{aligned}
P_i&=4Q\Big(\frac{d_i\lvert H_i\rvert}{\sqrt2\,\sigma_i}\Big) && (108)\\
2\mathcal E_i&=\frac{M_i-1}{6}d_i^2\ \Rightarrow\ d_i^2=\frac{12\mathcal E_i}{M_i-1} && (109)\\
P_i&=4Q\Big(\sqrt{\frac{12\mathcal E_i\lvert H_i\rvert^2}{(M_i-1)2\sigma_i^2}}\Big) && (110)\\
\frac{12\mathcal E_i\lvert H_i\rvert^2}{(M_i-1)2\sigma_i^2}&=\Big[Q^{-1}\Big(\frac P4\Big)\Big]^2=\text{cost} && (111):\ \text{stessa } P \text{ su tutte}\\
M_i-1&=\frac{6\mathcal E_i\lvert H_i\rvert^2}{\sigma_i^2}\cdot\frac{1}{[Q^{-1}(P/4)]^2} && \text{🧩 risolvo per } M_i\ (12/2=6)\\
b_i&=\log_2M_i=\log_2\Big(1+\frac{6\mathcal E_i\lvert H_i\rvert^2}{\sigma_i^2}\frac{1}{[Q^{-1}(P/4)]^2}\Big) && (112)\\
R_b&=\frac BT=\frac1T\sum_{i=0}^{N-1}b_i && (113)
\end{aligned}
$$

La (108) è esatta per $b_i$ pari (QAM quadrata) con $M_i\gg1$, e un limite superiore per $b_i$ qualsiasi.

### Derivazione — SNR gap e confronto con la capacità (114)–(116) · [[Note 2001 Gelli G.pdf#page=20|p. 20]], [[Note 2001 Gelli G.pdf#page=21|21]]

La capacità di $N$ canali AWGN indipendenti in parallelo è $C=\frac1T\sum_i\log_2\big(1+\frac{\mathcal E_i\lvert H_i\rvert^2}{\sigma_i^2}\big)$ (114). Ponendo

$$\Gamma=\frac16\Big[Q^{-1}\Big(\frac P4\Big)\Big]^2\quad(115)\qquad\Rightarrow\qquad R_b=\frac1T\sum_{i=0}^{N-1}\log_2\Big(1+\frac1\Gamma\frac{\mathcal E_i\lvert H_i\rvert^2}{\sigma_i^2}\Big)\quad(116)$$

il bit rate ha la forma della capacità con il contrasto di energia diviso per $\Gamma$: per arrivare alla capacità ideale bisognerebbe aumentare il contrasto di un fattore $\Gamma$, lo **SNR gap**. Più $\Gamma$ è piccolo, più il sistema è vicino all'ideale.

**Numeri (🧩, con le definizioni delle note):** $P=10^{-6}$: $Q^{-1}(2.5\cdot10^{-7})\approx5.03$, $\Gamma\approx25.3/6\approx4.2$, cioè $6.2$ dB; $P=10^{-3}$: $Q^{-1}(2.5\cdot10^{-4})\approx3.48$, $\Gamma\approx2.0$ ($3.1$ dB). Il gap cresce lentamente con l'affidabilità richiesta.

> 💡 Connessione: è la capacità $\log_2(1+\text{SNR})$ della Lezione 12 ([[informazione-mutua-e-capacita]], [[limite-di-shannon]]) applicata a $N$ canali in parallelo; la QAM non codificata ne resta lontana di $\Gamma$, e la codifica di canale serve a ridurre questo gap.

### Derivazione — Distribuzione ottima dell'energia: water filling (117)–(121) · [[Note 2001 Gelli G.pdf#page=21|p. 21]], [[Note 2001 Gelli G.pdf#page=22|22]]

**Problema:** massimizzare $R_b$ (116) con energia totale assegnata $\mathcal E=\sum_i\mathcal E_i$ (117). Pongo $n_i=\Gamma\sigma_i^2/\lvert H_i\rvert^2$ (il "fondo" della sottoportante $i$).

$$
\begin{aligned}
\mathcal L&=\sum_i\log_2\Big(1+\frac{\mathcal E_i}{n_i}\Big)-\lambda\Big(\sum_i\mathcal E_i-\mathcal E\Big) && \text{🧩 Lagrangiana}\\
\frac{\partial\mathcal L}{\partial\mathcal E_i}&=\frac{1}{\ln2}\,\frac{1}{n_i+\mathcal E_i}-\lambda=0\ \Rightarrow\ n_i+\mathcal E_i=\frac{1}{\lambda\ln2}\triangleq K && (118):\ \frac{\sigma_i^2\Gamma}{\lvert H_i\rvert^2}+\mathcal E_i=K\\
\mathcal E_i&=\begin{cases}K-\dfrac{\sigma_i^2\Gamma}{\lvert H_i\rvert^2}, & K-\dfrac{\sigma_i^2\Gamma}{\lvert H_i\rvert^2}\ge0\\[4pt]0 & \text{altrimenti}\end{cases} && (119):\ \mathcal E_i\ge0\\
\sum_i(K-n_i)&=\mathcal E\ \Rightarrow\ K=\frac1N\Big(\mathcal E+\sum_in_i\Big) && (120):\ \text{tutte attive}\\
\mathcal E_i&=\frac{\mathcal E}N+\Gamma\Big(\frac1N\sum_j\frac{\sigma_j^2}{\lvert H_j\rvert^2}-\frac{\sigma_i^2}{\lvert H_i\rvert^2}\Big) && (121)
\end{aligned}
$$

Alla distribuzione uniforme $\mathcal E/N$ si aggiunge un termine che misura quanto la sottoportante $i$ si scosta dalla media delle condizioni di tutte. Il nome **water filling** (o *water pouring*) viene dall'analogia idraulica della figura 7: il profilo del canale $\sigma_i^2\Gamma/\lvert H_i\rvert^2$ è il fondo di un recipiente, si versa l'energia totale come acqua, il pelo libero si porta al livello $K$ e la profondità dell'acqua sopra la sottoportante $i$ è $\mathcal E_i$. 🧩 La (120) vale se tutte le sottoportanti sono attive; se qualcuna risulta con $\mathcal E_i<0$ va spenta e $K$ si ricalcola con le sole attive.

![[grafico-gelli-water-filling.png|660]]

*🧩 Water filling su $N=8$ sottoportanti di un canale a due prese $h=[1,\,0.6]$, con $\Gamma\sigma^2=0.25$ ed energia totale $2$ (script `output/grafici/genera_grafici_approfondimenti.py`). Le sottoportanti con il fondo basso (canale buono) ricevono più energia e portano più bit; la 4, sul minimo di $\lvert H_i\rvert^2$, ha il fondo sopra il livello $K\approx0.52$ e viene spenta. I bit $b_i=\log_2(1+\mathcal E_i/n_i)$ non sono interi: vanno arrotondati, come dicono le note.*

**Algoritmo di bit loading ideale** (p. 21–22):
1. per una probabilità d'errore $P$ fissata si calcola lo SNR gap $\Gamma$ con la (115);
2. per un'energia $\mathcal E$ fissata si calcola $K$ con la (120) e le $\mathcal E_i$ con la (119);
3. se $\mathcal E_i=0$ per ogni $i$, la probabilità $P$ non si può garantire con l'energia $\mathcal E$: si aumenta l'energia o si rilassa $P$ e si ripetono i passi 1 e 2;
4. si calcolano i $b_i$, e quindi le costellazioni, con la (112).

Nulla garantisce che i $b_i$ siano interi: si arrotonda e si aggiustano le energie per rispettare vincolo e $P$ obiettivo; in alternativa esistono algoritmi di ottimizzazione discreta che risolvono direttamente il problema vincolato. La formulazione non è l'unica: a bit rate ed energia fissati si può minimizzare la probabilità d'errore, oppure a bit rate e probabilità fissati minimizzare l'energia.

## Riferimenti e indice delle note · [[Note 2001 Gelli G.pdf#page=22|p. 22]]–[[Note 2001 Gelli G.pdf#page=24|24]]

Le note citano dieci riferimenti: tra gli altri il lavoro sul Kineplex (Doelz, Heald e Martin, 1957), gli algoritmi di loading di Chow-Cioffi-Bingham e di Fischer-Huber, il "multicarrier primer" di Cioffi, l'articolo di Bingham del 1990 ("an idea whose time has come"), Proakis per le probabilità d'errore QAM e Gallager per la capacità. Pagina 24: indice delle sezioni (1 Introduzione, 2 Principio, 3 Prestazioni, 4 Canale e tempi di guardia, 5 FFT, 6 Bit loading).

## Collegamenti

- Lezione 15: [[ofdm]], [[prefisso-ciclico]], [[ofdm-con-fft]], [[equalizzazione-ofdm]], [[limiti-dell-ofdm]].
- Prestazioni QAM: [[probabilita-errore-m-aria]] (Lezioni 10–11).
- Capacità di canali in parallelo: [[informazione-mutua-e-capacita]], [[limite-di-shannon]] (Lezione 12).
- Fonte: [[note-gelli-multiportante]].

_Aggiornato: 2026-11-27 — creazione (approfondimento della Lezione 15, Note 2001 Gelli G.pdf)_
