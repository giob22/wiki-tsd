---
tipo: concetto
importanza_esame: alta
prerequisiti: ["interferenza-intersimbolica", "teorema-del-campionamento", "parametri-globali-modulazioni"]
fonti_pdf: ["signaling_bandlimited_channel_NEW.pdf#page=14", "signaling_bandlimited_channel_NEW.pdf#page=15", "signaling_bandlimited_channel_NEW.pdf#page=16", "signaling_bandlimited_channel_NEW.pdf#page=17", "signaling_bandlimited_channel_NEW.pdf#page=18", "signaling_bandlimited_channel_NEW.pdf#page=22", "signaling_bandlimited_channel_NEW.pdf#page=25", "signaling_bandlimited_channel_NEW.pdf#page=26", "signaling_bandlimited_channel_NEW.pdf#page=27", "signaling_bandlimited_channel_NEW.pdf#page=29", "signaling_bandlimited_channel_NEW.pdf#page=30", "signaling_bandlimited_channel_NEW.pdf#page=31", "signaling_bandlimited_channel_NEW.pdf#page=32"]
---

# Criterio di Nyquist e coseno rialzato

## Definizione · [[signaling_bandlimited_channel_NEW.pdf#page=14|p. 14]], [[signaling_bandlimited_channel_NEW.pdf#page=15|15]], [[signaling_bandlimited_channel_NEW.pdf#page=17|17]] · appunti [[signaling_bandlimited_channel.pdf#page=14|p. 14]]

Il **criterio di Nyquist** è la condizione sull'impulso complessivo $p(t)=g\ast h\ast c$ perché l'ISI sia nulla negli istanti di campionamento: $p(kT)=1$ per $k=0$ e $0$ per $k\neq0$. Un impulso che lo soddisfa è un **impulso di Nyquist**; ce ne sono infiniti. In frequenza la condizione è che le repliche di $P(f)$ traslate di multipli di $R_s=1/T$ sommino a una costante: $\sum_kP(f-kR_s)=T$.

Con ISI nulla, la rivelazione simbolo per simbolo, ottima in AWGN, resta ottima anche sul canale a banda limitata.

## Formule · [[signaling_bandlimited_channel_NEW.pdf#page=15|p. 15]]–[[signaling_bandlimited_channel_NEW.pdf#page=18|18]], [[signaling_bandlimited_channel_NEW.pdf#page=25|25]]–[[signaling_bandlimited_channel_NEW.pdf#page=27|27]], [[signaling_bandlimited_channel_NEW.pdf#page=31|31]], [[signaling_bandlimited_channel_NEW.pdf#page=32|32]] · appunti [[signaling_bandlimited_channel.pdf#page=18|p. 18]]

| Formula | Significato |
|---|---|
| $p(kT-nT)=1$ se $n=k$, $0$ se $n\neq k$ | criterio di Nyquist nel tempo (4) |
| $\sum_kP(f-kR_s)=T$ | criterio in frequenza (6) |
| $P(f)=T\,\text{rect}(fT)$, $p(t)=\text{sinc}(t/T)$ | impulso di Nyquist ideale (7) |
| $W_N=1/(2T)=R_s/2$ | banda di Nyquist (minima, monolatera, in banda base) |
| $P(f)$ a coseno rialzato, banda $W_N(1+\alpha)$ | roll-off $\alpha\in[0,1]$ |
| $p(t)=\text{sinc}(t/T)\,\dfrac{\cos(\pi\alpha t/T)}{1-(2\alpha t/T)^2}$ | impulso a coseno rialzato |
| $c(t)=g^\ast(-t)$, $\lvert G(f)\rvert^2=P_{RC}(f)$ | filtri a radice di coseno rialzato (RRC) |
| $G(f)=\sqrt{P_{RC}(f)}\,e^{j\phi(f)}$, $C(f)=\sqrt{P_{RC}(f)}\,e^{-j\phi(f)}$ | RRC di trasmissione e ricezione |
| $W_{actual}=(1+\alpha)R_b/\eta_B$ | banda effettiva con impulsi a coseno rialzato |

> 🧮 Formula chiave: $\sum_kP(f-k/T)=T$; coseno rialzato con banda $\frac{1+\alpha}{2T}$.

Simboli: $T$ [s] periodo di simbolo; $R_s=1/T$ [simboli/s]; $W_N$ [Hz]; $\alpha$ roll-off (adimensionale); $R_b$ [bit/s]; $\eta_B=R_b/W$ [bit/s/Hz]; $\text{sinc}(x)=\sin(\pi x)/(\pi x)$.

## Derivazioni

### Derivazione — Dal tempo alla frequenza (6) · [[signaling_bandlimited_channel_NEW.pdf#page=16|p. 16]], [[signaling_bandlimited_channel_NEW.pdf#page=17|17]]
**Fonte:** la slide scrive «taking the Fourier transform of both sides of (16)»: il numero è un refuso, si trasforma l'uguaglianza appena scritta.
**Si parte da:** (4) con $k=0$ e il treno di delta (5) ([[teorema-del-campionamento]]).

$$
\begin{aligned}
p(t)\,\Delta_T(t)&=\sum_mp(mT)\,\delta(t-mT) && \text{proprietà campionatrice della delta}\\
&=\delta(t) && \text{(4): } p(0)=1,\ p(mT)=0\ (m\neq0)\\
\mathcal F\{p\,\Delta_T\}&=P(f)\ast\frac1T\sum_k\delta\Big(f-\frac kT\Big)=\frac1T\sum_kP(f-kR_s) && \mathcal F\{\Delta_T\}=\tfrac1T\textstyle\sum_k\delta(f-k/T)\\
\frac1T\sum_kP(f-kR_s)&=\mathcal F\{\delta(t)\}=1\ \Rightarrow\ \sum_kP(f-kR_s)=T && \text{(6)}
\end{aligned}
$$

**Lettura:** è la stessa matematica del campionamento: campionare $p(t)$ ogni $T$ crea repliche dello spettro ogni $1/T$, e chiedere che i campioni siano «una delta» equivale a chiedere che le repliche sommino a una costante.

### Derivazione — Impulso ideale e banda minima · [[signaling_bandlimited_channel_NEW.pdf#page=18|p. 18]]–[[signaling_bandlimited_channel_NEW.pdf#page=21|21]] · appunti [[signaling_bandlimited_channel.pdf#page=18|p. 18]]

$$
\begin{aligned}
P(f)&=T\,\text{rect}(fT) && \text{(7): largo } 1/T\text{, centrato in 0}\\
\sum_kP(f-k/T)&=T && \text{rettangoli larghi } 1/T\text{ distanti } 1/T\text{: si affiancano senza buchi}\\
p(t)&=\mathcal F^{-1}\{T\,\text{rect}(fT)\}=T\cdot\frac1T\,\text{sinc}\Big(\frac tT\Big)=\text{sinc}\Big(\frac tT\Big) && \mathcal F^{-1}\{\text{rect}(f/B)\}=B\,\text{sinc}(Bt),\ B=1/T\\
p(kT)&=\frac{\sin(\pi k)}{\pi k}=0\ (k\neq0),\quad p(0)=1 && \text{zeri nei multipli di } T
\end{aligned}
$$

**Perché è la banda minima (🧩):** se $P(f)$ fosse nullo oltre una frequenza $W<\frac1{2T}$, le repliche distanti $1/T>2W$ lascerebbero buchi in cui la somma vale 0, e la (6) non potrebbe valere. Quindi $W_N=\frac1{2T}$ è la banda più piccola compatibile con ISI nulla (appunti di p. 18: soddisfa il criterio con la minima occupazione di banda).

### Derivazione — Errore di timing con la sinc · [[signaling_bandlimited_channel_NEW.pdf#page=22|p. 22]]–[[signaling_bandlimited_channel_NEW.pdf#page=24|24]]
**Fonte:** la slide dice che la serie dell'ISI «può divergere».

> 🧩 Derivazione mia:

$$
\begin{aligned}
\Big|\text{sinc}\Big(\frac{\Delta t-nT}{T}\Big)\Big|&=\frac{|\sin(\pi\Delta t/T-\pi n)|}{\pi|\Delta t/T-n|}=\frac{|\sin(\pi\Delta t/T)|}{\pi|n-\Delta t/T|} && \sin(x-\pi n)=\pm\sin x\\
\sum_{n\neq0}|s(n)|\,|\cdot|&\approx\frac{|\sin(\pi\Delta t/T)|}{\pi}\sum_{n\neq0}\frac1{|n|} && \text{caso peggiore: } |s(n)|=1,\ \text{segni allineati}\\
\sum_{n=1}^{N}\frac1n&\approx\ln N\to\infty && \text{serie armonica}
\end{aligned}
$$

Con il coseno rialzato le code decrescono come $1/|t|^3$ (sinc per $1/|t|^2$) e la serie $\sum1/n^3$ converge: l'ISI dovuta all'errore di timing resta limitata.

![[grafico-l14-errore-timing.png]]
*🧩 Grafico mio. ISI di caso peggiore per un errore di timing del 10% di $T$, in funzione del numero di simboli interferenti considerati per lato (scala logaritmica). Con la sinc (blu) cresce come $\ln N$ senza fermarsi; con il coseno rialzato $\alpha=0.5$ (arancio) si stabilizza dopo pochi simboli.*

### Derivazione — Il coseno rialzato soddisfa la (10) · [[signaling_bandlimited_channel_NEW.pdf#page=25|p. 25]], [[signaling_bandlimited_channel_NEW.pdf#page=26|26]]
> 🧩 Verifica mia, per $0<f<\frac1{2T}$ nella zona di roll-off; pongo $x=f-\frac1{2T}\in\big[-\frac{\alpha}{2T},0\big]$.

$$
\begin{aligned}
P(f)&=\frac T2\Big[1-\sin\Big(\frac{\pi T}{\alpha}x\Big)\Big] && |f|-\tfrac1{2T}=x\\
P\Big(f-\frac1T\Big)&=\frac T2\Big[1-\sin\Big(\frac{\pi T}{\alpha}(-x)\Big)\Big]=\frac T2\Big[1+\sin\Big(\frac{\pi T}{\alpha}x\Big)\Big] && \big|f-\tfrac1T\big|-\tfrac1{2T}=\tfrac1{2T}-f=-x\\
P(f)+P\Big(f-\frac1T\Big)+P\Big(f+\frac1T\Big)&=T+0=T && |f+\tfrac1T|>\tfrac{1+\alpha}{2T}\text{: lì } P=0
\end{aligned}
$$

Nella parte piatta $P(f)=T$ e le repliche sono nulle. Il roll-off è **antisimmetrico** attorno a $\frac1{2T}$, dove vale $T/2$: quello che una replica perde l'altra lo aggiunge.

### Derivazione — Impulso a coseno rialzato · [[signaling_bandlimited_channel_NEW.pdf#page=27|p. 27]], [[signaling_bandlimited_channel_NEW.pdf#page=29|29]]
**Fonte:** la slide dà $p(t)$ senza calcolo.
> 🧩 Derivazione mia, con un trucco: lo spettro a coseno rialzato è la convoluzione del rettangolo ideale con un mezzo coseno di area 1, $P(f)=T\,\text{rect}(fT)\ast h(f)$, con $h(f)=\frac{a}{2}\cos(af)$ per $|f|\le\frac{\pi}{2a}$ e $a=\pi T/\alpha$ (area: $\frac a2\cdot\frac2a=1$; larghezza $\pi/a=\alpha/T$, cioè tutta la zona di roll-off). La convoluzione nel dominio della frequenza è un prodotto nel tempo:

$$
\begin{aligned}
p(t)&=\text{sinc}\Big(\frac tT\Big)\cdot\mathcal F^{-1}\{h\}(t) && \text{convoluzione} \leftrightarrow \text{prodotto}\\
\mathcal F^{-1}\{h\}(t)&=\frac a2\int_{-\pi/(2a)}^{\pi/(2a)}\cos(af)\cos(2\pi ft)\,df && h\text{ pari: resta il coseno}\\
&=\frac a4\Big[\frac{2\sin\big(\frac{\pi}{2a}(a+2\pi t)\big)}{a+2\pi t}+\frac{2\sin\big(\frac{\pi}{2a}(a-2\pi t)\big)}{a-2\pi t}\Big] && \text{Werner e integrazione}\\
&=\frac a2\cos\Big(\frac{\pi^2t}{a}\Big)\Big[\frac1{a+2\pi t}+\frac1{a-2\pi t}\Big] && \sin(\tfrac\pi2\pm x)=\cos x\\
&=\frac{\cos(\pi^2t/a)}{1-(2\pi t/a)^2} && \text{somma delle frazioni}\\
&=\frac{\cos(\pi\alpha t/T)}{1-(2\alpha t/T)^2} && a=\pi T/\alpha
\end{aligned}
$$

**Sanity check:** con $\alpha=0$ il secondo fattore vale 1 e si ritrova la sinc ideale; $p(0)=1$ (area di $P$ pari a $T\cdot\frac1T=1$); il fattore $\frac{1}{1-(2\alpha t/T)^2}$ decresce come $1/t^2$, come dice la slide. In $t=\pm\frac{T}{2\alpha}$ numeratore e denominatore si annullano insieme e il limite è finito ($\frac\pi4\text{sinc}\frac1{2\alpha}$).

![[grafico-l14-coseno-rialzato.png]]
*🧩 Grafico mio (formule di p. 26–27). A sinistra lo spettro: piatto fino a $\frac{1-\alpha}{2T}$, nullo oltre $\frac{1+\alpha}{2T}$, sempre $T/2$ in $\frac{1}{2T}$. A destra l'impulso: tutti si annullano nei multipli di $T$, ma con $\alpha$ grande le code sono molto più basse. Corrisponde alla figura di p. 28.*

### Derivazione — Filtri a radice di coseno rialzato · [[signaling_bandlimited_channel_NEW.pdf#page=30|p. 30]], [[signaling_bandlimited_channel_NEW.pdf#page=31|31]]
**Fonte:** slide 31 della versione aggiornata. Si sceglie il filtro di ricezione **adattato** a quello di trasmissione, $c(t)=g^\ast(-t)$, e si chiede che la cascata dei due sia un coseno rialzato.

$$
\begin{aligned}
c(t)=g^\ast(-t)\ &\Longleftrightarrow\ C(f)=G^\ast(f) && \mathcal F\{g^\ast(-t)\}=\Big[\int g(-t)e^{j2\pi ft}dt\Big]^\ast=\Big[\int g(u)e^{-j2\pi fu}du\Big]^\ast,\ u=-t\\
P_{RC}(f)&=G(f)\,C(f)=G(f)\,G^\ast(f)=\lvert G(f)\rvert^2 && p_{RC}=g\ast c\text{: la convoluzione diventa prodotto}\\
\lvert G(f)\rvert&=\sqrt{P_{RC}(f)} && P_{RC}\ge0\text{, la radice esiste}\\
G(f)&=\sqrt{P_{RC}(f)}\,e^{j\phi(f)},\qquad C(f)=G^\ast(f)=\sqrt{P_{RC}(f)}\,e^{-j\phi(f)} && G=\lvert G\rvert e^{j\phi}
\end{aligned}
$$

Nel prodotto $G(f)C(f)$ le fasi $e^{j\phi}$ ed $e^{-j\phi}$ si cancellano: la fase $\phi(f)$ non influenza $P_{RC}(f)$, ed è il filtro adattato a cancellarla. La scelta usuale è $\phi(f)=0$: allora $G(f)=\sqrt{P_{RC}(f)}$ è reale e pari, quindi $g(t)$ è reale e pari e $c(t)=g^\ast(-t)=g(t)$. Per realizzarlo si tronca $g(t)$ e lo si ritarda, cioè si aggiunge una fase lineare.

$p_{RC}(t)$ è un impulso di Nyquist; il solo impulso RRC $g(t)$ **no**.

> 🧩 Perché $g(t)$ da solo non è di Nyquist: la (6) chiede che le repliche di $G(f)=\sqrt{P_{RC}(f)}$ sommino a una costante. Nella zona di roll-off due repliche si sovrappongono: per il coseno rialzato $P_{RC}(f)+P_{RC}(f-\frac1T)=T$, ma per le radici $\sqrt{P_{RC}(f)}+\sqrt{P_{RC}(f-\frac1T)}$ non è costante (a $f=\frac1{2T}$ ciascuna vale $\sqrt{T/2}$ e la somma $\sqrt{2T}$, mentre nella parte piatta si ha $\sqrt T$). Quindi $g(t)$ ha ISI propria; l'ISI sparisce solo dopo il filtro di ricezione.

### Derivazione — Banda effettiva · [[signaling_bandlimited_channel_NEW.pdf#page=32|p. 32]]
**Si parte da:** $\eta_B=R_b/W$ ([[parametri-globali-modulazioni]]).

> 🧩 Numeri miei: QPSK (bidimensionale, $M=4$) a $R_b=10$ Mbit/s ha $\eta_B=\log_24=2$ bit/s/Hz, quindi $W=R_b/\eta_B=5$ MHz attorno alla portante senza eccesso di banda (è la banda bilatera dell'inviluppo, $2W_N=R_s$); con roll-off $\alpha=0.25$, $W_{actual}=1.25\cdot5=6.25$ MHz. Con $\alpha=1$ la banda raddoppia (10 MHz).

## Spiegazione · [[signaling_bandlimited_channel_NEW.pdf#page=22|p. 22]], [[signaling_bandlimited_channel_NEW.pdf#page=29|29]]–[[signaling_bandlimited_channel_NEW.pdf#page=31|31]]

- **Perché non basta la sinc.** È la soluzione con la banda minima, ma ha uno spettro con spigoli: è non causale (viola il criterio di Paley-Wiener) e le sue code decrescono come $1/|t|$, quindi non c'è margine sugli istanti di campionamento.
- **Il compromesso del roll-off.** Più $\alpha$ è grande, più lo spettro è dolce e più le code nel tempo sono corte: si paga con banda $W_N(1+\alpha)$. Le code corte e gli zeri nei $kT$ aiutano anche a estrarre il timing per la [[sincronizzazione]].
- **Radice di Nyquist.** Il canale non si controlla: si scelgono $G(f)$ e $C(f)$ come radici quadrate di uno spettro di Nyquist (filtri a radice di coseno rialzato, RRC), così $G(f)C(f)$ è di Nyquist; l'ISI introdotta dal canale la toglie un equalizzatore ([[equalizzazione]]). Con $C=G^\ast$ il filtro di ricezione è anche adattato al filtro di trasmissione: la stessa scelta dà ISI nulla (senza canale) e massimo SNR al campionamento.

## Perché importa

Il coseno rialzato è la forma d'impulso usata in pratica nella modulazione lineare: fissa il legame tra symbol rate e banda occupata, $W=(1+\alpha)R_s/2$ in banda base. È il collegamento tra la banda «di Shannon» della Lezione 12 e la banda reale di un sistema.

## Connessioni

- [[interferenza-intersimbolica]]: il criterio di Nyquist la annulla negli istanti di campionamento.
- [[teorema-del-campionamento]]: stessa struttura (repliche spettrali ogni $1/T$) e stessa sinc.
- [[parametri-globali-modulazioni]]: efficienza di banda $\eta_B$.
- [[equalizzazione]]: cosa fare quando il canale rompe la condizione di Nyquist.

## Fonti · [[signaling_bandlimited_channel_NEW.pdf#page=14|p. 14]]–[[signaling_bandlimited_channel_NEW.pdf#page=32|32]] · appunti [[signaling_bandlimited_channel.pdf#page=14|p. 14]], [[signaling_bandlimited_channel.pdf#page=18|18]]

- [[signaling-bandlimited-channels]]

_Aggiornato: 2026-11-23 — versione aggiornata delle slide (signaling_bandlimited_channel_NEW.pdf): filtri a radice di coseno rialzato (slide 31), banda effettiva «con impulsi a coseno rialzato»; 2026-11-20 — revisione della traduzione delle slide (banda base, banda passante del filtro, log-likelihood ratio, livello del BER floor); 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf (Lezione 14)_
