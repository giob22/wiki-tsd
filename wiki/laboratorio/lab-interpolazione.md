---
tipo: laboratorio
esame: no
macroblocco: 2
codice: "AD_conversion.m, righe 103-144 e 199-202"
concetti: ["interpolazione", "teorema-del-campionamento"]
---

# Lab 2 — Interpolazione: convoluzione, durata e taglio

> ⚠️ Non materia d'esame: serve a vedere l'[[interpolazione]] all'opera e a capire due cose che nel codice sembrano misteriose: perché il ricostruito è più lungo del segnale e perché va tagliato. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-campionamento]].

## Cosa fa il codice

> 📄 Fonte: [[AD_conversion.m]], righe 103–131

```matlab
C = 2;                          % 1 rettangolo, 2 triangolo, 3 sinc
switch C
case 1   % rect((t-Ts/2)/Ts): th = 0:dt:Ts;       h = ones(...)
case 2   % lambda(t/Ts):      th = -Ts:dt:Ts;     h = 1-abs(th/Ts);
case 3   % sinc(t/Ts):        th = -25*Ts:dt:25*Ts; h = sinc(th/Ts);
end
L = length(h);
s_r       = conv(s_samp,h);                            % convoluzione
s_r_trunc = s_r(floor((L-1)/2)+1 : floor((L-1)/2)+N);  % taglio
% il segnale risultante da una convoluzione ha una durata pari alla somma
% della durata dei segnali convoluti
```

- Il filtro $h$ è definito sulla **stessa griglia** $dt$ del segnale, sul suo asse dei tempi `th`.
- `conv` calcola la convoluzione dei due vettori.
- Il risultato viene tagliato a $N$ punti, con il commento sulla durata.
- In fondo allo script (righe 199–202) viene costruito l'asse dei tempi dell'uscita completa:

```matlab
t_conv_start = t(1) + th(1);
t_conv = t_conv_start + (0:(length(s_r)-1)) * dt;
```

## Cosa succede davvero

### 1. La convoluzione è la formula di interpolazione
Nelle slide la ricostruzione è $x_r(t) = \sum_n x(n)\,h_r(t - nT_c)$ ([[interpolazione]], [[Campionamento_AD_DA.pdf#page=17]]): ogni campione "accende" una copia del filtro centrata sul suo istante e pesata dal suo valore, e le copie si sommano.
> 🧩 Perché `conv` fa proprio questo (derivazione mia):

$$
\begin{aligned}
s_r[k] &= \sum_m s_{samp}[m]\,h[k - m] && \text{definizione di conv} \\
&= \sum_{m \in \text{campioni}} s(t_m)\,h[k - m] && s_{samp} = 0 \text{ fuori dagli istanti } nT_s \\
&= \sum_n s(nT_s)\,h(t - nT_s) && \text{l'indice } k - m \text{ è la distanza, in passi } dt\text{, dal campione}
\end{aligned}
$$
Poiché $h$ vale 1 al centro, la copia del campione $n$ passa esattamente per il valore $s(nT_s)$.

![[grafico-lab-interpolazione.gif]]
*🧩 Animazione mia (replica dello script, esempio 1). Si aggiungono i 9 campioni non nulli uno alla volta. Ogni campione (asta arancio) accende una copia di $h$ (verde); la curva blu è la somma delle copie accese finora, cioè il risultato di `conv`.*
- *In alto, triangoli: la somma diventa la spezzata che unisce i campioni.*
- *In basso, sinc: le copie oscillano e si compensano a vicenda; la somma è morbida.*

### 2. Perché il risultato dura di più: le durate si sommano
Il commento del codice (riga 129) è una proprietà generale della convoluzione.
> 🧩 Derivazione mia. Se $x$ è diverso da zero solo in $[a_1, b_1]$ e $h$ solo in $[a_2, b_2]$:

$$
\begin{aligned}
y(t) &= \int x(\tau)\,h(t - \tau)\,d\tau && \text{convoluzione} \\
&\neq 0 \ \text{solo se esiste } \tau \text{ con } a_1 \le \tau \le b_1 \text{ e } a_2 \le t - \tau \le b_2 && \text{servono entrambi i fattori non nulli} \\
&\Rightarrow a_1 + a_2 \le t \le b_1 + b_2 && \text{sommo le due disuguaglianze} \\
\text{durata}(y) &= (b_1 + b_2) - (a_1 + a_2) = (b_1 - a_1) + (b_2 - a_2) && \text{somma delle durate}
\end{aligned}
$$
Intuizione: mentre $h$ "scorre" su $x$, l'uscita comincia appena i due si toccano (il bordo sinistro di uno sul bordo destro dell'altro) e finisce quando si lasciano. Per vettori è lo stesso: $N$ e $L$ punti danno $N + L - 1$ punti.

**Numeri dell'esempio 1** ($N = 10^4$, $T_s = 83\,dt$):

| Filtro | `th` | $L$ | Uscita di `conv` | Asse dell'uscita |
|---|---|---|---|---|
| triangolo (C = 2) | $[-T_s, T_s]$ | $2\cdot 83 + 1 = 167$ | $10^4 + 166 = 10166$ punti | $[-30.498,\ 30.492]$ s |
| sinc, 25 lobi (C = 3) | $[-25T_s, 25T_s]$ | $2\cdot 25\cdot 83 + 1 = 4151$ | $14150$ punti | $[-42.45,\ 42.44]$ s |
| rettangolo (C = 1) | $[0, T_s]$ | 84 | $10083$ punti | $[-30,\ 30.492]$ s |

L'asse dell'uscita è quello costruito alle righe 199–202: parte da $t(1) + th(1)$ e avanza di $dt$. Per la sinc: $-30 + (-12.45) = -42.45$ s.

> 🧩 Anche nel segnale "vero" si vede la somma delle durate. I campioni non nulli vanno da $-1.992$ a $1.992$ s e il triangolo dura $2T_s \approx 1$ s. Il ricostruito lineare è quindi diverso da zero da $-1.992 - 0.498$ a $1.992 + 0.498$, cioè su circa $[-2.49, 2.49]$ s. Lì i due campioni da 0.008 danno code alte 0.008, invisibili.

### 3. Perché si taglia, e perché proprio lì
Per due motivi:
1. **Confrontare.** Per disegnare $s_r$ sullo stesso asse di $s$ e soprattutto per calcolare l'errore `s - sq_r_trunc` ([[lab-snr]]) i due vettori devono avere **la stessa lunghezza** e **gli stessi istanti**, punto per punto.
2. **Le parti in più sono "code".** I punti che escono dalla finestra $[-30, 30)$ sono le code dei filtri centrati sui campioni vicini ai bordi. Non corrispondono a nessun istante in cui conosciamo $s(t)$.

Dove tagliare lo dice l'asse del punto 2.
> 🧩 Derivazione mia. Il punto $k$ dell'uscita (indice Matlab da 1) sta all'istante

$$t_{conv}(k) = t(1) + th(1) + (k - 1)\,dt$$
Voglio il punto che cade in $t(1)$, l'inizio dell'asse di $s$:
$$
\begin{aligned}
t(1) + th(1) + (k - 1)\,dt &= t(1) && \text{condizione} \\
k - 1 &= -th(1)/dt && \\
&= \frac{L - 1}{2} && \text{filtro simmetrico: } th(1) = -\tfrac{L-1}{2}\,dt
\end{aligned}
$$
Quindi si parte da $k = \frac{L-1}{2} + 1$ e si prendono $N$ punti: è esattamente `s_r(floor((L-1)/2)+1 : floor((L-1)/2)+N)`. Si butta metà dell'eccesso a sinistra e metà a destra, cioè $\frac{L-1}{2}$ punti per lato: 83 per il triangolo ($T_s$), 2075 per la sinc (12.45 s).

**Cosa succede se si taglia male.** Prendendo semplicemente i primi $N$ punti, ogni valore viene disegnato $-th(1)$ secondi prima di dove dovrebbe stare: il ricostruito appare **ritardato**, di $T_s = 0.498$ s con il triangolo e di 12.45 s con la sinc.

![[grafico-lab-durata-convoluzione.png]]
*🧩 Grafico mio (esempio 1, sinc con 25 lobi).*
- *In alto: gli ingressi di `conv`. I campioni stanno su un asse di $10^4$ punti, $[-30, 30)$ s (barra azzurra); il filtro sinc su 4151 punti, $[-12.45, 12.45]$ s.*
- *Al centro: l'uscita completa, 14150 punti da $-42.45$ a $42.44$ s. Le fasce rosse sono i pezzi che il codice taglia.*
- *In basso: con il taglio del codice (blu) il ricostruito si sovrappone al trapezio; con il taglio sbagliato, i primi $N$ punti (rosso tratteggiato), è spostato di 12.45 s.*

### 4. I tre filtri a confronto
![[grafico-lab-interpolatori.png]]
*🧩 Grafico mio, esempio 1 senza quantizzazione; SNR calcolato come in [[lab-snr]].*
- *Rettangolo (C = 1), SNR 15.8 dB: gradini, con picchi verticali (spiegati sotto). In verde tratteggiato lo ZOH corretto e causale, SNR 12.2 dB.*
- *Triangolo (C = 2), SNR 50.2 dB: la spezzata coincide con il trapezio.*
- *Sinc (C = 3), SNR 26.7 dB: curva morbida con piccole oscillazioni, massimo 1.029 in $t = -0.82$ s.*

**Perché il triangolo vince qui.** Il trapezio è esso stesso una spezzata, e i suoi spigoli ($\pm 1$, $\pm 2$) cadono quasi esattamente su campioni ($\pm 0.996$, $\pm 1.992$). La FOH, che unisce i campioni con segmenti, lo ricostruisce quasi alla perfezione: errore massimo 0.008. È una coincidenza favorevole di questo segnale, non una regola.

**Perché la sinc oscilla.** La serie di Shannon ricostruisce l'unico segnale **a banda limitata** $|f| < f_s/2$ che passa per i campioni ([[Campionamento_AD_DA.pdf#page=17]]). Il trapezio non è a banda limitata: i suoi spigoli richiedono frequenze alte, che la sinc non può produrre. Ottiene quindi una versione "smussata" con piccole oscillazioni, a cui si aggiungono il poco aliasing ([[lab-campionamento]]) e il troncamento a 25 lobi. Nell'esempio 2, che è a banda limitata, la sinc è la scelta giusta ([[lab-campionamento]]).

**Il rettangolo del codice (C = 1) ha due particolarità** (🧩 osservazioni mie, dalla replica):
1. `th = 0:dt:Ts` contiene **sia 0 sia $T_s$**: 84 punti per un intervallo lungo $T_s$ = 83 passi. Due rettangoli adiacenti hanno quindi un punto in comune, che viene sommato due volte. Da qui i picchi a 2 (dove due campioni valgono 1) e a 1.5 (dove valgono 1 e 0.5). Con `th = 0:dt:Ts-dt` spariscono.
2. Il filtro è **causale**: `th` parte da 0, non da $-T_s/2$. Il taglio "da $(L-1)/2$" pensato per i filtri simmetrici lo anticipa di $41\,dt = 0.246 \approx T_s/2$. I gradini risultano centrati sui campioni, cioè un'interpolazione "al campione più vicino", non causale. Lo ZOH vero delle slide ([[Campionamento_AD_DA.pdf#page=23]]) tiene invece il campione **dopo** l'istante di campionamento: è la curva verde, più in ritardo e con SNR più basso (12.2 dB).

### Le figure del laboratorio
![[lab-0928-figure2-interpolazione-lineare.png]]
*Figura del laboratorio ([[Figure_2_interpolazione_lineaare.png]]), C = 2. In alto il ricostruito $s_r(t)$: il trapezio ritorna identico. Al centro e in basso la parte quantizzata ([[lab-quantizzazione]]).*

![[lab-0928-figure2-interpolazione-shannon.png]]
*Figura del laboratorio ([[Figure_2_interpolazione_shannon.png]]), C = 3. In alto il ricostruito con la sinc: fianchi arrotondati, due gobbe sopra 1 attorno a $\pm 0.8$ s e piccole oscillazioni fuori da $[-2, 2]$.*

## Dubbi chiariti

- **"Perché il ricostruito dura più dei due segnali presi singolarmente?"** Perché la convoluzione fa scorrere un segnale sull'altro: l'uscita esiste da quando si toccano a quando si lasciano, cioè per la somma delle durate (derivazione al punto 2).
- **"Perché tagliarlo?"** Per riportarlo sull'asse di $s(t)$ e confrontarlo punto per punto. I pezzi tolti sono code fuori dalla finestra in cui conosciamo il segnale.
- **"Perché da $(L-1)/2$?"** Perché è il ritardo introdotto da un filtro centrato in 0 ma memorizzato a partire da $th(1) = -\frac{L-1}{2}dt$: lo si compensa scartando quei punti.

## Collegamento alla teoria

[[interpolazione]]: serie di Shannon ([[Campionamento_AD_DA.pdf#page=17]]), ZOH ([[Campionamento_AD_DA.pdf#page=23]]), FOH ([[Campionamento_AD_DA.pdf#page=24]]). Il confronto tra i tre SNR corrisponde a quello tra le loro $H_r(f)$ nel grafico di quella pagina.

_Aggiornato: 2026-09-30 — creazione da ingest del laboratorio (AD_conversion.m)_
