---
tipo: laboratorio
esame: no
macroblocco: 1
codice: "AD_conversion.m, righe 87-101"
concetti: ["teorema-del-campionamento", "aliasing"]
---

# Lab 1 — Campionamento

> ⚠️ Non materia d'esame: serve a vedere il [[teorema-del-campionamento]] all'opera. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-setup-e-spettro]].

## Cosa fa il codice

> 📄 Fonte: [[AD_conversion.m]], righe 87–101

```matlab
fs = 2*W;                                   % frequenza di Nyquist
Ts = 1/fs;
Ts = round(Ts/dt)*dt;                       % Ts deve stare sulla griglia
f_samp = 1/Ts;                              % fs vera, dopo l'arrotondamento
high   = (abs((t/Ts)-round(t/Ts))<eps);     % true dove t è multiplo di Ts
s_samp = s.*high;                           % azzera tutto il resto
is     = find(high);                        % indici dei campioni
stem(t(is),s_samp(is));
```

Passo per passo:
1. **Scelta di $f_s$.** Si prende il minimo del teorema, $f_s = 2W$.
2. **Arrotondamento.** $T_s$ viene arrotondato a un multiplo di $dt$, altrimenti gli istanti $nT_s$ non esisterebbero nel vettore $t$ ([[lab-setup-e-spettro]]).
3. **Ricerca degli istanti.** `high` è un vettore di 0 e 1: vale 1 dove $t/T_s$ è un intero, a meno di `eps` $= 10^{-8}$ per gli errori di arrotondamento dei numeri in virgola mobile.
4. **Campionamento.** `s.*high` moltiplica punto per punto: lascia $s$ negli istanti $nT_s$ e mette 0 ovunque altrove. Il vettore ha ancora $10^4$ punti, ma solo 121 possono essere diversi da zero.

## Cosa succede davvero

### Il vettore `s_samp` è $x_\delta(t)$
Nelle slide il campionamento ideale è $x_\delta(t) = \sum_n x_a(nT_c)\,\delta(t - nT_c)$ ([[Campionamento_AD_DA.pdf#page=11]], [[teorema-del-campionamento]]): un treno di impulsi pesati dai campioni, nullo tra un impulso e l'altro. `s_samp` è la sua versione simulata:
- è nullo tra un campione e l'altro;
- negli istanti $nT_s$ vale il campione.

> 🧩 Differenza (mia): la $\delta$ ha area 1, mentre nel vettore un punto isolato vale $s(nT_s)$ ma "occupa" solo $dt$. Il codice non corregge questa scala, e non serve: nell'interpolazione il filtro $h$ ha picco 1, quindi la convoluzione restituisce direttamente $\sum_n s(nT_s)\,h(t - nT_s)$ ([[lab-interpolazione]]).

### I numeri dell'esempio 1
> 🧩 Derivazione mia

$$
\begin{aligned}
f_s &= 2W = 2\cdot 1 = 2\ \text{Hz} \Rightarrow T_s = 0.5\ \text{s} && \text{riga 88} \\
T_s/dt &= 0.5/0.006 = 83.33 \to 83 && \text{arrotondamento} \\
T_s &= 83\cdot 0.006 = 0.498\ \text{s} \Rightarrow f_{samp} = 1/0.498 = 2.008\ \text{Hz} && \text{riga 91}
\end{aligned}
$$
Nella finestra $[-30, 30)$ cadono i campioni $n = -60, \dots, 60$: **121** campioni. Sono diversi da zero solo i 9 tra $-1.992$ e $1.992$ s:

| $nT_s$ [s] | $\pm 1.992$ | $\pm 1.494$ | $\pm 0.996$, $\pm 0.498$, 0 |
|---|---|---|---|
| $s(nT_s)$ | 0.008 | 0.506 | 1 |

I due campioni da 0.008 sono appena dentro il trapezio: $-1.992 + 2 = 0.008$.

### Cosa succede allo spettro
Campionare nel tempo **replica** lo spettro ogni $f_s$ ([[Campionamento_AD_DA.pdf#page=12]]):
$$X_\delta(f) = \frac{1}{T_s}\sum_k S\Big(f - \frac{k}{T_s}\Big)$$
Le repliche sono distanti $f_{samp} = 2.008$ Hz, e la centrale occupa in teoria tutto l'asse, perché il trapezio non è a banda limitata. Le code delle repliche vicine entrano quindi nella banda $|f| < f_s/2$: è l'**aliasing** ([[aliasing]]). Qui è piccolo, perché oltre 1 Hz c'è solo lo 0.05% dell'energia ([[lab-setup-e-spettro]]).

![[grafico-lab-campionamento-spettro.png]]
*🧩 Grafico mio (replica dello script).*
- *In alto: il trapezio (grigio) e i campioni `s_samp` (aste blu) ogni $T_s = 0.498$ s.*
- *In basso: il modulo della trasformata dei campioni, moltiplicata per $T_s$ (blu), e le singole repliche $S(f)$, $S(f \mp f_s)$ (tratteggiate). La trasformata dei campioni è la somma delle repliche. Nella fascia azzurra $|f| < f_s/2 = 1.004$ Hz la replica centrale è quasi pulita: le code delle vicine valgono pochi centesimi.*

> 🧩 Il commento della riga 88 dice che con $W = 1$ «è come se avessimo applicato un filtro anti-aliasing». Va letto così: **nessun filtro** viene applicato, ma il segnale ha già quasi tutta l'energia sotto 1 Hz. Il risultato somiglia a quello che darebbe un filtro antialiasing ([[Campionamento_AD_DA.pdf#page=21]]). L'aliasing c'è, ma è trascurabile.

### Esempio 2: quando l'arrotondamento rompe il teorema
> 🧩 Esperimento mio con la replica dello script, `flag = 2` (nessuna figura del laboratorio per questo caso).

$$
\begin{aligned}
f_s &= 2W = 8\ \text{Hz} \Rightarrow T_s = 0.125\ \text{s} && W = 4\ \text{Hz, la sinusoide più veloce} \\
T_s/dt &= 0.125/0.006 = 20.83 \to 21 \Rightarrow T_s = 0.126\ \text{s} && \text{arrotondamento} \\
f_{samp} &= 1/0.126 = 7.937\ \text{Hz} < 2W = 8\ \text{Hz} && \text{sotto Nyquist!}
\end{aligned}
$$
- La componente a 4 Hz supera $f_{samp}/2 = 3.968$ Hz e si ripiega in $f_{samp} - 4 = 3.937$ Hz, come nell'esempio da 1.5 kHz di [[aliasing]].
- L'originale (4 Hz) e il suo alias (3.937 Hz) differiscono di 0.063 Hz: la fase dell'uno scorre lentamente rispetto a quella dell'altro. In certi tratti la ricostruzione segue il segnale, in altri è sfasata di mezzo periodo. L'errore ha un andamento periodico di circa $1/0.063 \approx 16$ s: minimi attorno a $t \approx -12,\ 4,\ 20$ s nella simulazione.
- **SNR della ricostruzione con la sinc: 2 dB.** Con $f_s = 16.7$ Hz, cioè il doppio, sale a 37.5 dB.

![[grafico-lab-esempio2.png]]
*🧩 Grafico mio. In alto l'esempio 2 con i parametri del codice ($f_s = 7.94$ Hz): i campioni (arancio) sono giusti, ma la curva ricostruita (blu) non è il segnale (grigio), perché i campioni sono compatibili anche con un'altra sinusoide più lenta. In basso con $f_s = 16.67$ Hz: la ricostruzione coincide.*

> 🧩 Anche senza arrotondamento, $f_s = 2W$ esatto è il **caso limite** (b) di [[Campionamento_AD_DA.pdf#page=13]]: le repliche si toccano in $f_s/2$. Una sinusoide proprio a $f_s/2$ viene campionata sempre nella stessa fase, a meno del segno, e la sua ampiezza non si ricostruisce. Esempio: $\sin(2\pi\,4\,nT_s + \frac{\pi}{5})$ con $T_s = 1/8$ vale $(-1)^n\sin\frac{\pi}{5}$, quindi l'ampiezza apparente è $5\sin 36° = 2.94$ invece di 5. Per questo in pratica si sovracampiona ([[teorema-del-campionamento]]).

## Dubbi chiariti

- **"Perché $T_s = 0.498$ e non 0.5?"** Perché nel vettore esistono solo multipli di $dt = 6$ ms, e 0.5 non lo è ($0.5/0.006 = 83.3$).
- **"Il segnale campionato è ancora un vettore di $10^4$ punti?"** Sì. È il modo di simulare $x_\delta(t)$ restando sulla griglia "continua": serve per poterlo convolvere con il filtro di ricostruzione, che vive sulla stessa griglia.
- **"Perché $f_s = 2W$ non basta?"** Nell'esempio 1 perché il segnale non è a banda limitata (aliasing piccolo). Nell'esempio 2 perché l'arrotondamento porta $f_s$ sotto $2W$ (aliasing grosso). E comunque $2W$ esatto è il caso limite.

## Collegamento alla teoria

[[teorema-del-campionamento]] (campionamento ideale e repliche, [[Campionamento_AD_DA.pdf#page=11]] – [[Campionamento_AD_DA.pdf#page=13]]), [[aliasing]] (ripiegamento, filtro antialiasing, [[Campionamento_AD_DA.pdf#page=21]]).

_Aggiornato: 2026-09-30 — creazione da ingest del laboratorio (AD_conversion.m)_
