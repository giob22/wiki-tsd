---
tipo: laboratorio
esame: no
macroblocco: 0
codice: "AD_conversion.m, righe 5-85"
concetti: ["conversione-ad-da", "teorema-del-campionamento"]
---

# Lab 0 — Simulare il "tempo continuo" e calcolare lo spettro

> ⚠️ Non materia d'esame: serve a capire cosa fa lo script [[AD_conversion.m]] prima di campionare. Fonte: [[laboratorio-conversione-ad]].

## Il problema

Un computer non può memorizzare un segnale a tempo continuo: conosce solo numeri, uno dopo l'altro. Per "vedere" il campionamento bisogna quindi fingere di avere un segnale continuo. Il trucco dello script: usare una griglia di tempi **molto più fitta** di quella di campionamento. Rispetto al campionamento vero ($T_s \approx 0.5$ s) la griglia con passo 6 ms si comporta come il continuo.

## Cosa fa il codice

> 📄 Fonte: [[AD_conversion.m]], righe 5–13

```matlab
accuracy = 1e4;          % numero di punti della griglia
t_i = -30;  t_f = 30;    % asse dei tempi: da -30 s a 30 s
D  = t_f - t_i;          % 60 s
dt = D/accuracy;         % passo della griglia
t  = t_i:dt:t_f-dt;      % 10^4 istanti
```

$$
\begin{aligned}
D &= t_f - t_i = 30 - (-30) = 60\ \text{s} && \text{durata della finestra} \\
dt &= D/\text{accuracy} = 60/10^4 = 6\cdot10^{-3}\ \text{s} = 6\ \text{ms} && \text{passo della griglia} \\
N &= 10^4 && \text{da } t_i \text{ a } t_f - dt \text{: l'ultimo punto è escluso}
\end{aligned}
$$

**Regola d'oro del codice:** ogni istante "speciale" (inizio del segnale, spigoli, periodo di campionamento) viene arrotondato a un multiplo di $dt$ con `round(x/dt)*dt`. Serve perché nel vettore esistono solo i tempi della griglia: un istante che non sta sulla griglia non si può né leggere né scrivere.
> 🧩 Conseguenza: il trapezio parte a $-1.998$ s invece che a $-2$ s (perché $-2/0.006 = -333.3 \to -333$), e più avanti $T_s$ diventa 0.498 s invece di 0.5 s ([[lab-campionamento]]). Sono spostamenti di pochi ms, invisibili nei grafici ma presenti nei numeri.

### Esempio 1: il trapezio (righe 21–35)

Il segnale vale 0 fino a $-2$, sale linearmente fino a 1 in $t = -1$, resta a 1 fino a $t = 1$, scende a 0 in $t = 2$. Il codice lo costruisce concatenando pezzi: zeri, rampa $t + 2$, uni, rampa $-t + 2$, zeri. `W = 1` è la banda "dichiarata" in Hz.

### Esempio 2: tre sinusoidi (righe 44–48)

$$s(t) = 5\sin(2\pi\,4t + \tfrac{\pi}{5}) + 3\sin(2\pi\,\tfrac43 t + \tfrac{\pi}{8}) + 2\sin(2\pi\,0.4t - \tfrac{\pi}{3})$$
Frequenze 4 Hz, 1.33 Hz, 0.4 Hz; `W = 4` Hz, la più alta. Qui la banda è davvero limitata. Cosa succede campionandolo: [[lab-campionamento]].

### Lo spettro (righe 79–85)

```matlab
S_dft = fftshift(fft(s));          % DFT, con la frequenza zero al centro
S     = dt*S_dft;                  % scala: approssima l'integrale di Fourier
f     = linspace(-0.5,0.5,N)/dt;   % asse delle frequenze in Hz
```

## Cosa succede davvero

### Perché `dt*fft` è la trasformata di Fourier
> 🧩 Derivazione mia

$$
\begin{aligned}
S(f) &= \int_{-\infty}^{+\infty} s(t)\,e^{-j2\pi ft}\,dt && \text{definizione} \\
&\approx \sum_{n=0}^{N-1} s(t_n)\,e^{-j2\pi f t_n}\,dt && \text{somma di Riemann sulla griglia } t_n = t_i + n\,dt \\
&= dt\,e^{-j2\pi f t_i}\sum_{n=0}^{N-1} s(t_n)\,e^{-j2\pi f n\,dt} && t_n = t_i + n\,dt \\
\Rightarrow |S(f_k)| &\approx dt\,\big|\text{FFT}(s)[k]\big| && f_k = k/(N\,dt)\text{; il fattore di fase ha modulo 1}
\end{aligned}
$$
- Il fattore $e^{-j2\pi ft_i}$ nasce perché la griglia parte da $-30$ e non da 0: cambia la fase, non il modulo. Lo script disegna `abs(S)`, quindi non si vede.
- `fftshift` sposta le frequenze negative a sinistra, così l'asse va da $-\frac{1}{2dt}$ a $+\frac{1}{2dt}$.

**Numeri:**
- banda visibile $\pm\frac{1}{2dt} = \pm 83.3$ Hz: sono gli estremi dell'asse di [[Figure_1.png]];
- risoluzione in frequenza $\frac{1}{N\,dt} = \frac{1}{60}$ Hz, cioè l'inverso della durata della finestra.

> 🧩 Dettaglio: `linspace(-0.5,0.5,N)/dt` mette $N$ punti con passo $\frac{1}{(N-1)dt}$ invece di $\frac{1}{N\,dt}$. L'errore è di una parte su $10^4$: invisibile.

### Lo spettro esatto del trapezio
> 🧩 Derivazione mia: serve a controllare che la FFT dia il risultato giusto.

Il trapezio è la convoluzione di due rettangoli: $s(t) = \Pi(t/3) * \Pi(t)$.
- Un rettangolo largo 3 e uno largo 1 danno un risultato largo $3 + 1 = 4$ (da $-2$ a 2): è la regola "le durate si sommano", la stessa di [[lab-interpolazione]].
- Il risultato sale linearmente mentre i due si sovrappongono sempre di più, per un tratto lungo 1.
- Resta costante e pari a 1 (sovrapposizione piena: larghezza 1 × altezza 1) per $3 - 1 = 2$ s.

In frequenza la convoluzione diventa un prodotto, con $\mathcal{F}[\Pi(t/T)] = T\,\text{sinc}(fT)$ ([[modulazione-digitale]]):
$$S(f) = 3\,\text{sinc}(3f)\cdot\text{sinc}(f)$$
**Sanity check:**
- $S(0) = 3$ = area del trapezio, $\frac{(4 + 2)}{2}\cdot 1 = 3$ ✓, ed è il picco a 3 di [[Figure_1.png]];
- la FFT dà 2.986: la differenza viene dal trapezio "arrotondato" alla griglia.

**Energia:**
$$E = \int s^2\,dt = 2\int_1^2 (2 - t)^2\,dt + \int_{-1}^{1} 1\,dt = 2\cdot\tfrac13 + 2 = \tfrac83 \approx 2.667$$
Integrando $|S(f)|^2$ numericamente si ottiene lo stesso valore (Parseval). Di questa energia, solo lo **0.05%** sta oltre $|f| = 1$ Hz e lo 0.85% oltre $|f| = 0.5$ Hz (integrazione numerica mia). Per questo `W = 1` è una "banda" ragionevole, anche se il segnale non è a banda limitata.

![[grafico-lab-setup-spettro.png]]
*🧩 Grafico mio (replica Python dello script).*
- *A sinistra: zoom sullo spigolo in $t = -1$. Il "segnale continuo" è una fila di punti distanti 6 ms.*
- *Al centro: $|dt\cdot\text{FFT}(s)|$ (blu) sovrapposto alla trasformata esatta $3|\text{sinc}(3f)\,\text{sinc}(f)|$ (arancio tratteggiato): coincidono.*
- *A destra: lo stesso spettro in dB. I lobi scendono ma non arrivano mai a zero: un segnale limitato nel tempo non è limitato in banda ([[aliasing]]).*

![[lab-0928-figure1-segnale-spettro-campioni.png]]
*Figura del laboratorio ([[Figure_1.png]]), esempio 1. In alto il trapezio su $[-3, 3]$ s. Al centro lo spettro su tutto l'asse $\pm 83$ Hz: tutto concentrato attorno a 0, picco 3. In basso i campioni su tutta la finestra $[-30, 30]$ s: 121 aste, quasi tutte nulle, con i valori 0.5 e 1 attorno all'origine.*

## Dubbi chiariti

- **"Ma il segnale è continuo o no?"** No: è un vettore di $10^4$ numeri. Si comporta come continuo perché $dt = 6$ ms è 83 volte più piccolo di $T_s$. Tra un campione e l'altro ci sono 82 punti "continui" che il campionamento butterà via.
- **"Perché la finestra è così lunga (60 s) se il trapezio dura 4 s?"** Per avere molta risoluzione in frequenza ($1/60$ Hz) e spazio per le code della sinc ([[lab-interpolazione]]). Ha però un effetto collaterale sull'SNR: [[lab-snr]].

## Collegamento alla teoria

- La domanda di [[Campionamento_AD_DA.pdf#page=8]] ([[teorema-del-campionamento]]), cioè come scegliere $f_c$ per un dato segnale, parte proprio dallo spettro: qui lo si calcola per poter scegliere $f_s = 2W$.
- Nelle slide la frequenza di campionamento si chiama $f_c$ e il periodo $T_c$; nel codice `fs` e `Ts`.

_Aggiornato: 2026-09-30 — creazione da ingest del laboratorio (AD_conversion.m)_
