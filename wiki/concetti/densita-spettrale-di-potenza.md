---
tipo: concetto
importanza_esame: alta
prerequisiti: ["autocorrelazione-processi-wss", "processi-e-sistemi-lti"]
fonti_pdf: ["random_processes.pdf#page=32", "random_processes.pdf#page=34", "random_processes.pdf#page=35", "random_processes.pdf#page=36", "random_processes.pdf#page=37", "random_processes.pdf#page=38", "random_processes.pdf#page=39", "random_processes.pdf#page=40", "random_processes.pdf#page=46"]
---

# Densità spettrale di potenza (PSD)

## Definizione · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]]

La **densità spettrale di potenza** (*power spectral density*, PSD) di un processo $X(t)$ è
$$S_{XX}(f) \triangleq \lim_{T\to+\infty}\frac{1}{2T}\,E\big[|X_T(f)|^2\big]$$
dove $X_T(f)$ è la trasformata di Fourier della versione **finestrata** del processo, $X_T(t) = X(t)\,\text{rect}[t/(2T)]$ (il processo tenuto solo per $|t| < T$).

**Relazione di Wiener-Khinchin**: per un processo **WSS** la PSD è la trasformata di Fourier dell'autocorrelazione,
$$S_{XX}(f) = \int_{-\infty}^{+\infty} R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau$$

**Potenza:**
$$E[X^2(t)] = R_{XX}(0) = \int_{-\infty}^{+\infty} S_{XX}(f)\,df = P_X \tag{21}$$
dove $P_X$ è la potenza del processo WSS. $S_{XX}(f)$ si misura in **watt per hertz** (W/Hz).

## Formule · [[random_processes.pdf#page=32|p. 32]]–[[random_processes.pdf#page=34|34]], [[random_processes.pdf#page=36|p. 36]]–[[random_processes.pdf#page=38|38]], [[random_processes.pdf#page=40|p. 40]], [[random_processes.pdf#page=46|p. 46]]

| Formula | Significato |
|---|---|
| $S_{XX}(f) = \lim_{T\to\infty}\frac{1}{2T}E[\lvert X_T(f)\rvert^2]$ | definizione |
| $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ | Wiener-Khinchin (processi WSS) |
| $E[X^2] = R_{XX}(0) = \int S_{XX}(f)\,df = P_X$ | potenza, eq. (21) |
| $S_{YY}(f) = S_{XX}(f)\,\lvert H(f)\rvert^2$ | PSD dopo un filtro LTI, eq. (22) |
| $\Delta P_X \approx 2\Delta f\,S_{XX}(f)$ | potenza nella banda $2\Delta f$ attorno a $\pm f$ |
| $S_{XX}(0) = \int R_{XX}(\tau)\,d\tau$ | proprietà 1, eq. (23) |
| $E[X^2] = \int S_{XX}(f)\,df = R_{XX}(0)$ | proprietà 2, eq. (24) |
| $S_{XX}(f) \ge 0$ | proprietà 3 |
| $S_{XX}(-f) = S_{XX}(f)$ | proprietà 4 (processo reale) |
| $p_{XX}(f) = S_{XX}(f)\big/\int S_{XX}(f)\,df$ | proprietà 5, PSD normalizzata, eq. (25) |
| $S_{XY}(f) = \lim\frac{1}{2T}E[X_T(f)Y_T^\ast (f)] = \int R_{XY}(\tau)e^{-j2\pi f\tau}d\tau$ | densità spettrale mutua, eq. (26) |
| $S_{XY}(f) = S_{YX}(-f) = S_{YX}^\ast (f)$ | simmetria |
| $S_{ZZ} = S_{XX} + S_{XY} + S_{YX} + S_{YY}$ | PSD della somma $Z = X + Y$, eq. (29) |
| $S_{ZZ} = S_{XX} + S_{YY}$ | somma di processi incoerenti, eq. (30) |
| $S_{XX}(\nu) = \lim_{N\to\infty}\frac{1}{2N+1}E[\lvert X_N(\nu)\rvert^2]$ | PSD a tempo discreto |

Simboli: $f$ = frequenza [Hz]; $T$ = semi-durata della finestra [s]; $S_{XX}$ [W/Hz] (o V²/Hz); $P_X$ [W]; $\Delta f$ = banda del filtro [Hz]; $\nu$ = frequenza normalizzata del tempo discreto (adimensionale); $X_N(\nu)$ = trasformata di Fourier a tempo discreto (DTFT) della versione troncata di $X(n)$.

> 🧮 Formula chiave: $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ e $P_X = R_{XX}(0) = \int S_{XX}(f)\,df$.

## Derivazioni

### Derivazione — Relazione di Wiener-Khinchin · [[random_processes.pdf#page=32|p. 32]]
**Fonte:** «si può dimostrare che…», senza dimostrazione.
> 🧩 Dimostrazione mia, partendo dalla definizione. Processo reale e WSS.

$$
\begin{aligned}
X_T(f) &= \int_{-T}^{T} X(t)\,e^{-j2\pi ft}\,dt && \text{trasformata della versione finestrata} \\
|X_T(f)|^2 &= X_T(f)\,X_T^*(f) = \int_{-T}^{T}\!\!\int_{-T}^{T} X(t_1)X(t_2)\,e^{-j2\pi f(t_1 - t_2)}\,dt_1dt_2 && X \text{ reale: il coniugato cambia solo il segno dell'esponente} \\
E\big[|X_T(f)|^2\big] &= \int_{-T}^{T}\!\!\int_{-T}^{T} R_{XX}(t_1 - t_2)\,e^{-j2\pi f(t_1 - t_2)}\,dt_1dt_2 && \text{scambio } E \text{ e integrali; WSS} \\
&= \int_{-2T}^{2T} (2T - |\tau|)\,R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau && \tau = t_1 - t_2
\end{aligned}
$$
L'ultimo passaggio: nel quadrato $[-T, T]^2$ l'integrando dipende solo da $\tau = t_1 - t_2$. I punti con un dato $\tau$ formano un segmento, e la sua proiezione su un asse è lunga $2T - |\tau|$: questo è il "peso" di ogni $\tau$.
$$
\begin{aligned}
\frac{1}{2T}E\big[|X_T(f)|^2\big] &= \int_{-2T}^{2T}\Big(1 - \frac{|\tau|}{2T}\Big)R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau && \text{divido per } 2T \\
&\xrightarrow{T \to \infty} \int_{-\infty}^{+\infty} R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau = \mathcal{F}[R_{XX}(\tau)] && \text{il peso triangolare tende a 1 per ogni } \tau
\end{aligned}
$$
**Ipotesi:** processo WSS; $R_{XX}$ assolutamente integrabile (serve per passare al limite dentro l'integrale); scambio tra valore atteso e integrali lecito.

### Derivazione — Eq. (21) e proprietà 1–2: potenza e valore in zero · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=36|p. 36]]
$$
\begin{aligned}
R_{XX}(\tau) &= \int S_{XX}(f)\,e^{j2\pi f\tau}\,df && \text{antitrasformata (Wiener-Khinchin letta al contrario)} \\
R_{XX}(0) &= \int S_{XX}(f)\,df && \tau = 0 \text{: area sotto la PSD, eq. (21) e (24)} \\
&= E[X^2(t)] = P_X && \text{proprietà 1 dell'autocorrelazione} \\
S_{XX}(0) &= \int R_{XX}(\tau)\,e^{0}\,d\tau = \int R_{XX}(\tau)\,d\tau && f = 0 \text{ in Wiener-Khinchin: area sotto l'autocorrelazione, eq. (23)}
\end{aligned}
$$

### Derivazione — Proprietà 3: $S_{XX}(f) \ge 0$ · [[random_processes.pdf#page=36|p. 36]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia, dalla definizione: $\frac{1}{2T}E[|X_T(f)|^2]$ è il valore atteso di una quantità non negativa, diviso per $2T > 0$, quindi è $\ge 0$ per ogni $T$; lo resta al limite. In alternativa, con il significato fisico qui sotto: se $S_{XX}$ fosse negativa attorno a qualche $f$, un filtro stretto centrato lì misurerebbe una potenza negativa, il che è assurdo.

### Derivazione — Proprietà 4: PSD pari per un processo reale · [[random_processes.pdf#page=37|p. 37]]
> 🧩 Derivazione mia

$$
\begin{aligned}
S_{XX}(-f) &= \int R_{XX}(\tau)\,e^{+j2\pi f\tau}\,d\tau && \text{Wiener-Khinchin in } -f \\
&= \int R_{XX}(-u)\,e^{-j2\pi fu}\,du && u = -\tau \\
&= \int R_{XX}(u)\,e^{-j2\pi fu}\,du = S_{XX}(f) && R_{XX} \text{ è pari (proprietà 2 dell'autocorrelazione)}
\end{aligned}
$$
Con lo stesso conto, $S_{XX}^\ast (f) = S_{XX}(-f) = S_{XX}(f)$ perché $R_{XX}$ è reale: la PSD di un processo reale è **reale e pari**.

### Derivazione — Proprietà 5: la PSD normalizzata si comporta come una pdf · [[random_processes.pdf#page=37|p. 37]]
$p_{XX}(f) \ge 0$ per la proprietà 3, e $\int p_{XX}(f)\,df = \int S_{XX}\,df\big/\int S_{XX}\,df = 1$.
> 🧩 Lettura mia: $p_{XX}(f)$ dice come la potenza è **distribuita** in frequenza, come una pdf dice come la probabilità è distribuita sui valori.

### Derivazione — Significato fisico: $\Delta P_X \approx 2\Delta f\,S_{XX}(f)$ · [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=35|35]]
**Fonte:** risultato dato «dalla (22)».
> 🧩 Passaggi miei. Filtro ideale a banda stretta: $|H(f)| = 1$ in due finestre larghe $\Delta f$ centrate in $\pm f_c$, 0 altrove (figura della slide 30).

$$
\begin{aligned}
\Delta P_X &= \int S_{XX}(f)\,|H(f)|^2\,df && \text{potenza all'uscita del filtro: (22) e (21)} \\
&= \int_{f_c - \Delta f/2}^{f_c + \Delta f/2} S_{XX}(f)\,df + \int_{-f_c - \Delta f/2}^{-f_c + \Delta f/2} S_{XX}(f)\,df && |H|^2 = 1 \text{ solo nelle due finestre} \\
&\approx \Delta f\,S_{XX}(f_c) + \Delta f\,S_{XX}(-f_c) && \Delta f \ll f_c,\ S_{XX} \text{ continua: circa costante nella finestra} \\
&= 2\Delta f\,S_{XX}(f_c) && \text{proprietà 4: } S_{XX} \text{ pari}
\end{aligned}
$$
La slide scrive il risultato come $\Delta P_X \approx (2\Delta f)\,S_{XX}(f)$ «con $f_c \equiv f$ per generalità»: la frequenza centrale del filtro può essere qualunque, e il filtro "legge" la PSD proprio lì.
**Unità:** [W/Hz]·[Hz] = [W] ✓: per questo $S_{XX}$ è una **densità** di potenza per unità di frequenza.
**Il fattore 2:** la banda "fisica" larga $\Delta f$ attorno a $f_c$ ha una gemella attorno a $-f_c$, e la potenza reale le conta entrambe, per una larghezza totale $2\Delta f$.

![[random-processes-p35-filtro-banda-stretta.png]]
*modulo della risposta del filtro ideale a banda stretta: vale 1.0 in due finestre di larghezza $\Delta f$ centrate in $-f_c$ e $f_c$, 0 altrove.*

### Derivazione — Densità spettrali mutue: $S_{XY}(f) = S_{YX}(-f) = S_{YX}^\ast (f)$ · [[random_processes.pdf#page=38|p. 38]]
**Fonte:** «ricordando che $R_{XY}(\tau) = R_{YX}(-\tau)$».
> 🧩 Passaggi miei

$$
\begin{aligned}
S_{XY}(f) &= \int R_{XY}(\tau)\,e^{-j2\pi f\tau}\,d\tau = \int R_{YX}(-\tau)\,e^{-j2\pi f\tau}\,d\tau && \text{eq. (26) e simmetria di [[momenti-di-un-processo]]} \\
&= \int R_{YX}(u)\,e^{+j2\pi fu}\,du = S_{YX}(-f) && u = -\tau \\
&= S_{YX}^*(f) && R_{YX} \text{ reale: coniugare cambia solo il segno dell'esponente}
\end{aligned}
$$
$S_{XY}$ **non è necessariamente reale**, perché $R_{XY}$ non è pari.

### Derivazione — PSD di una somma, eq. (27)–(30) · [[random_processes.pdf#page=39|p. 39]], [[random_processes.pdf#page=40|40]]
$$
\begin{aligned}
R_{ZZ}(t_1, t_2) &= E\{[X(t_1) + Y(t_1)][X(t_2) + Y(t_2)]\} && Z = X + Y,\ \text{processi a media nulla} \\
&= R_{XX}(t_1, t_2) + R_{XY}(t_1, t_2) + R_{YX}(t_1, t_2) + R_{YY}(t_1, t_2) && \text{sviluppo e linearità di } E \quad \text{(27)} \\
R_{ZZ}(\tau) &= R_{XX}(\tau) + R_{XY}(\tau) + R_{YX}(\tau) + R_{YY}(\tau) && \tau = t_1 - t_2,\ \text{congiuntamente WSS} \quad \text{(28)} \\
S_{ZZ}(f) &= S_{XX}(f) + S_{XY}(f) + S_{YX}(f) + S_{YY}(f) && \text{trasformo, eq. (29)} \\
S_{ZZ}(f) &= S_{XX}(f) + S_{YY}(f) && \text{incoerenti: } R_{XY} = R_{YX} \equiv 0 \quad \text{(30)}
\end{aligned}
$$
**In parole:** la PSD della somma di processi WSS **incoerenti**, o in modo equivalente a media nulla e incorrelati, è la somma delle PSD. Le potenze si sommano solo se i processi non "interferiscono" tra loro.
> 🧩 Sanity check: nella (29) i due termini misti sommano a $S_{XY} + S_{XY}^\ast = 2\,\text{Re}\{S_{XY}\}$, reale, per la simmetria appena ricavata. Anche $S_{ZZ}$ è quindi reale ✓.

### Esempio — Wiener-Khinchin sull'autocorrelazione esponenziale
> 🧩 Esempio mio: il processo dei grafici, $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$ con potenza 1.

$$
\begin{aligned}
S_{XX}(f) &= \int_0^{\infty} e^{-\tau(1/\tau_c + j2\pi f)}\,d\tau + \int_0^{\infty} e^{-\tau(1/\tau_c - j2\pi f)}\,d\tau && \text{spezzo in } \tau > 0 \text{ e } \tau < 0 \ (\tau \to -\tau) \\
&= \frac{1}{1/\tau_c + j2\pi f} + \frac{1}{1/\tau_c - j2\pi f} && \textstyle\int_0^\infty e^{-a\tau}d\tau = 1/a,\ \text{Re}\,a > 0 \\
&= \frac{2/\tau_c}{1/\tau_c^2 + (2\pi f)^2} = \frac{2\tau_c}{1 + (2\pi f\tau_c)^2} && \text{denominatore comune; moltiplico sopra e sotto per } \tau_c^2
\end{aligned}
$$
**Verifiche con le proprietà:**
- proprietà 1: $S_{XX}(0) = 2\tau_c = \int e^{-|\tau|/\tau_c}d\tau$ ✓;
- proprietà 2: $\int S_{XX}\,df = 2\tau_c\cdot\frac{1}{2\pi\tau_c}\cdot\pi = 1 = R_{XX}(0)$ ✓, usando $\int\frac{du}{1 + u^2} = \pi$ con $u = 2\pi f\tau_c$;
- proprietà 3 e 4: $S_{XX}$ è positiva e pari ✓.

**Lettura:** $\tau_c$ grande (processo lento) dà una PSD alta e stretta; $\tau_c$ piccolo (processo veloce) una PSD bassa e larga. È il grafico "lento contro veloce" di [[autocorrelazione-processi-wss]].

### PSD a tempo discreto · [[random_processes.pdf#page=46|p. 46]]
$$
S_{XY}(\nu) \triangleq \lim_{N\to+\infty}\frac{1}{2N+1}E\big[X_N(\nu)\,Y_N^*(\nu)\big] \qquad S_{XX}(\nu) \triangleq \lim_{N\to+\infty}\frac{1}{2N+1}E\big[|X_N(\nu)|^2\big]
$$
$X_N(\nu)$ e $Y_N(\nu)$ sono le trasformate di Fourier a tempo discreto delle versioni **troncate** di $X(n)$ e $Y(n)$; la seconda si ottiene dalla prima con $X(n) \equiv Y(n)$. Per Wiener-Khinchin, la PSD di un processo WSS a tempo discreto è la trasformata a tempo discreto della sua autocorrelazione $R_{XX}(m)$.
> 🧩 In formula, con la convenzione $X(\nu) = \sum_n x(n)\,e^{-j2\pi\nu n}$ che la slide non scrive: $S_{XX}(\nu) = \sum_{m=-\infty}^{+\infty} R_{XX}(m)\,e^{-j2\pi\nu m}$. Il $2N + 1$ al denominatore è il numero di campioni tra $-N$ e $N$, l'analogo della durata $2T$.

## Spiegazione · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=38|p. 38]]

- La PSD dice **come la potenza del processo si distribuisce in frequenza**. La sua area è la potenza totale, (21).
- Il **significato fisico** viene dal filtro a banda stretta: un filtro ideale centrato in $f_c$, largo $\Delta f$, lascia passare una potenza $\approx 2\Delta f\,S_{XX}(f_c)$. Misurare la potenza all'uscita di filtri sempre più stretti è un modo di "misurare" la PSD.
- La **densità spettrale mutua** misura i legami **in frequenza** tra due processi.

> 🧩 Perché serve Wiener-Khinchin: la definizione con la finestra e il limite è concettuale ma scomoda da calcolare. Il teorema la riduce a una trasformata di Fourier dell'autocorrelazione, che spesso si calcola in poche righe (esempio sopra).

> 🎯 Esame: definire la PSD; enunciare e dimostrare Wiener-Khinchin; ricavare potenza e significato fisico ($2\Delta f\,S_{XX}$); dimostrare le proprietà 1–5; densità spettrale mutua e sua simmetria; PSD della somma di processi incoerenti.

## Perché importa

È lo strumento per descrivere segnali e rumori aleatori **in frequenza**: quanta potenza cade nella banda di un filtro, di un canale, di un ricevitore. Con $S_{YY} = S_{XX}|H|^2$ ([[processi-e-sistemi-lti]]) permette di calcolare la potenza di rumore all'uscita di qualunque filtro. Dà anche la banda occupata da un segnale modulato ([[calcolo-densita-spettrale]]).

## Connessioni

- [[autocorrelazione-processi-wss]] — Wiener-Khinchin: la PSD è la sua trasformata; larghezze inversamente proporzionali.
- [[processi-e-sistemi-lti]] — la (22) e la potenza all'uscita.
- [[momenti-di-un-processo]] — mutue correlazioni, incoerenza, simmetria $R_{XY}(\tau) = R_{YX}(-\tau)$.
- [[segnali-banda-base-e-passa-banda]] — la stessa idea di banda, ora per segnali aleatori (e la simmetria pari della PSD corrisponde a quella hermitiana degli spettri reali).
- [[calcolo-densita-spettrale]] — esercizio della slide 32: PSD di un segnale modulato linearmente.
- [[psd-componenti-in-quadratura]] — PSD dell'inviluppo complesso e delle componenti in fase e quadratura di un processo passa-banda; [[rumore-in-banda-passante]] — PSD costante in banda e potenza come area.

## Fonti · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=40|p. 40]], [[random_processes.pdf#page=46|p. 46]]

- [[processi-aleatori]]

_Aggiornato: 2026-11-01 — collegamento ai processi passa-banda; 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-10-14 — formule nelle tabelle: modulo scritto con \lvert \rvert e condizionamento con \mid (il \| non si leggeva bene); 2026-09-28 — creazione da ingest random_processes.pdf_
