---
tipo: concetto
importanza_esame: alta
prerequisiti: ["quantizzazione-non-uniforme", "snr-di-quantizzazione", "funzione-di-variabile-aleatoria"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=36", "Campionamento_AD_DA.pdf#page=37", "Campionamento_AD_DA.pdf#page=38", "Campionamento_AD_DA.pdf#page=39", "Campionamento_AD_DA.pdf#page=40", "Campionamento_AD_DA.pdf#page=41", "Campionamento_AD_DA.pdf#page=42", "Campionamento_AD_DA.pdf#page=43"]
---

# Companding e quantizzazione robusta (legge logaritmica, µ-law, A-law)

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=36]]

Il **companding** (*compressing + expanding*) realizza una quantizzazione non uniforme in tre passi:
1. **legge di compressione** $F(x)$, non lineare;
2. **quantizzazione uniforme** del segnale compresso;
3. in decodifica, la legge inversa: **espansione** $F^{-1}$.

Obiettivo: **quantizzazione robusta**, cioè SNR circa **indipendente dal livello** del segnale d'ingresso. In telefonia serve per la grande variabilità dei parlatori.

Motivazione ([[Campionamento_AD_DA.pdf#page=36]]):
- il quantizzatore ottimo di Lloyd-Max assume segnale **stazionario** e richiede di conoscere la pdf;
- come il quantizzatore uniforme, ha prestazioni **fortemente dipendenti dal livello** del segnale d'ingresso;
- in telefonia è fondamentale che le prestazioni siano circa indipendenti dal livello, vista la grande variabilità dei parlatori: è la **quantizzazione robusta**;
- per studiarla si assume che la legge non uniforme sia realizzata con il companding; in decodifica si applica la legge simmetrica, l'**espansione**.

![[campionamento-p36-companding.png]]
*Schema ([[Campionamento_AD_DA.pdf#page=36]]): compressore analogico $F(x)$ → quantizzatore uniforme a $n$ bit → decodificatore uniforme a $n$ bit → espansore analogico $F^{-1}(x)$.*

> ⚠️ Probabile refuso nella figura: il secondo blocco è etichettato «n-bit uniform **decoder**» come il terzo. Dal testo («compressione seguita da una quantizzazione uniforme») dovrebbe essere l'**encoder** (quantizzatore/codificatore uniforme).

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $\text{MSE}\approx\frac{1}{12}\sum_{i=1}^M p_i\Delta_i^2$, $\Delta_i = x_i-x_{i-1}$, $p_i\approx f_X(x_i)\Delta_i$ | MSE ad alta risoluzione | [[Campionamento_AD_DA.pdf#page=37]] |
| $\Delta_i\approx\dfrac{\Delta}{F'(x_i)} = \dfrac{1}{F'(x_i)}\dfrac{2X_{max}}{M}$ | ampiezza locale degli intervalli | [[Campionamento_AD_DA.pdf#page=38]] |
| $\text{MSE} = \dfrac{X_{max}^2}{3M^2}\displaystyle\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$ | MSE in forma integrale | [[Campionamento_AD_DA.pdf#page=39]] |
| $\text{SNR} = \dfrac{\int_0^{X_{max}}x^2f_X(x)\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx}$ | SNR del compander | [[Campionamento_AD_DA.pdf#page=39]] |
| $F(x) = X_{max}+\frac1k\ln\frac{x}{X_{max}}$, $x\in[0,X_{max}]$ | legge logaritmica ideale | [[Campionamento_AD_DA.pdf#page=40]] |
| $\text{SNR} = \dfrac{3M^2}{k^2X_{max}^2}$ | SNR della legge logaritmica | [[Campionamento_AD_DA.pdf#page=40]] |
| $F(x) = X_{max}\dfrac{\ln(1+\mu\|x\|/X_{max})}{\ln(1+\mu)}\text{sgn}(x)$ | **µ-law** ($\mu=255$) → [[legge-mu]] | [[Campionamento_AD_DA.pdf#page=41]] |
| $F(x) = \begin{cases}X_{max}\frac{A\|x\|/X_{max}}{1+\ln A}\text{sgn}(x) & 0\le\|x\|\le X_{max}/A\\ X_{max}\frac{1+\ln(A\|x\|/X_{max})}{1+\ln A}\text{sgn}(x) & X_{max}/A\le\|x\|\le X_{max}\end{cases}$ | **A-law** ($A=87.6$) → [[legge-a]] | [[Campionamento_AD_DA.pdf#page=42]] |

> 🧮 Formula chiave — prestazioni ([[Campionamento_AD_DA.pdf#page=43]]), segnale che impegna tutta la dinamica:
> $$\text{SNR}_{dB}\approx6.02\,b+\alpha,\qquad \alpha = \begin{cases}4.77-20\log_{10}[\ln(1+\mu)] & \mu\text{-law}\\ 4.77-20\log_{10}[1+\ln A] & A\text{-law}\\ 4.77-20\log_{10}(X_{max}/x_{rms}) & \text{uniforme}\end{cases}$$

Simboli: $M$ = numero di livelli; $\Delta = 2X_{max}/M$ = passo del quantizzatore uniforme **dopo** la compressione; $F'$ = derivata della legge (adimensionale); $k$ [1/V] e $c$ [V] costanti; $\mu$, $A$ parametri adimensionali; $\text{sgn}$ = funzione segno.

## Derivazioni

### Derivazione — MSE ad alta risoluzione
**Fonte:** [[Campionamento_AD_DA.pdf#page=37]] (approssimazione data)
> 🧩 Derivazione mia del termine $\Delta_i^2/12$
$$
\begin{aligned}
\text{MSE} &= \sum_i\int_{R_i}(q_i-x)^2f_X(x)\,dx && [[quantizzazione-non-uniforme]] \\
&\approx \sum_i f_X(x_i)\int_{-\Delta_i/2}^{\Delta_i/2}u^2\,du && f_X \approx \text{cost. in } R_i;\ q_i \text{ al centro};\ u = x-q_i \\
&= \sum_i f_X(x_i)\frac{\Delta_i^3}{12} && \textstyle\int_{-a}^{a}u^2du = 2a^3/3,\ a=\Delta_i/2 \\
&= \frac{1}{12}\sum_i p_i\Delta_i^2 && p_i\approx f_X(x_i)\Delta_i
\end{aligned}
$$
**Ipotesi (high resolution):** $M\gg1$; sovraccarico trascurato; $f_X$ circa costante in ogni intervallo; $q_i$ circa al centro di $R_i$ (ipotesi implicita, 🧩 esplicitata da me).
**Sanity check:** con $\Delta_i = \Delta$ si ha $\text{MSE} = \frac{\Delta^2}{12}\sum_ip_i = \frac{\Delta^2}{12}$, come in [[snr-di-quantizzazione]] ([[Campionamento_AD_DA.pdf#page=37]]).

### Derivazione — $\Delta_i \approx \Delta/F'(x_i)$
**Fonte:** [[Campionamento_AD_DA.pdf#page=38]]
$$
\begin{aligned}
F(x_i)-F(x_{i-1}) &= \Delta = \frac{2X_{max}}{M} && \text{dopo la compressione gli intervalli sono uniformi} \\
\frac{\Delta}{\Delta_i} &= \frac{F(x_i)-F(x_{i-1})}{x_i-x_{i-1}} \approx F'(x_i) && \text{rapporto incrementale, } \Delta_i \text{ piccolo} \\
\Delta_i &\approx \frac{\Delta}{F'(x_i)} = \frac{1}{F'(x_i)}\frac{2X_{max}}{M}
\end{aligned}
$$
Dove $F'$ è grande (compressione "ripida") gli intervalli originali sono **stretti**.

![[campionamento-p38-legge-compressione.png]]
*Legge di compressione $F(x)$ concava ([[Campionamento_AD_DA.pdf#page=38]]): l'intervallo $\Delta_i = x_i - x_{i-1}$ sull'asse $x$ viene mappato in un intervallo di ampiezza $\Delta$ sull'asse $F(x)$. Dove la curva è ripida, un $\Delta_i$ piccolo basta a coprire un $\Delta$ intero.*

### Derivazione — MSE e SNR in forma integrale
**Fonte:** [[Campionamento_AD_DA.pdf#page=39]]
$$
\begin{aligned}
\text{MSE} &= \frac{1}{12}\sum_ip_i\Delta_i^2 = \frac1{12}\sum_ip_i\frac{4X_{max}^2}{M^2[F'(x_i)]^2} && \text{sostituisco } \Delta_i \\
&= \frac{X_{max}^2}{3M^2}\sum_i\frac{f_X(x_i)}{[F'(x_i)]^2}\Delta_i && 4/12 = 1/3;\ p_i = f_X(x_i)\Delta_i \\
&\to \frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx && \Delta_i\to dx \text{ (somma di Riemann)} \\
\text{SNR} &= \frac{E[x^2]}{\text{MSE}} = \frac{\int_{-X_{max}}^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X}{[F']^2}dx} && f_X = 0 \text{ fuori da } (-X_{max},X_{max}) \\
&= \frac{\int_0^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X}{[F']^2}dx} && f_X \text{ pari, } F \text{ dispari} \Rightarrow F' \text{ pari: integrandi pari, il fattore 2 si semplifica}
\end{aligned}
$$

### Derivazione — Legge logaritmica ottima per la robustezza
**Fonte:** [[Campionamento_AD_DA.pdf#page=40]]
**Idea:** l'SNR è indipendente da $f_X$ se il denominatore è proporzionale al numeratore, cioè se $1/[F'(x)]^2\propto x^2$.
$$
\begin{aligned}
\frac{1}{F'(x)} &= kx \Rightarrow F'(x) = \frac{1}{kx} && \text{scelta} \\
F(x) &= c+\frac1k\ln x && \text{integro} \\
F(X_{max}) &= X_{max} \Rightarrow c = X_{max}-\frac1k\ln X_{max} && \text{vincolo sul fondo scala} \\
F(x) &= X_{max}+\frac1k\ln\frac{x}{X_{max}},\quad x\in[0,X_{max}] && \ln x - \ln X_{max} = \ln(x/X_{max}) \\
\text{SNR} &= \frac{\int_0^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}k^2x^2f_X\,dx} = \frac{3M^2}{k^2X_{max}^2} && \text{gli integrali si semplificano}
\end{aligned}
$$
**Risultato:** SNR **indipendente dalla pdf**, quindi anche dal livello $x_{rms}$ del segnale. $c$ e $k$ sono costanti arbitrarie; $c$ si fissa con il vincolo $F(X_{max}) = X_{max}$.
**Conclusione della slide** ([[Campionamento_AD_DA.pdf#page=40]]): per una pdf $f_X(x)$ **arbitraria**, la legge di compressione che rende l'SNR indipendente dal livello del segnale è di tipo **logaritmico**.
**Interpretazione** ([[Campionamento_AD_DA.pdf#page=40]]): $\Delta_i = \Delta/F'(x_i) = \Delta\,k\,x_i$, cioè l'intervallo raddoppia quando raddoppia il livello, e l'errore **relativo** resta costante.
**Limite:** per $x\to0$, $F(x)\to-\infty$, quindi non è implementabile esattamente. Si usano approssimazioni con $F(0) = 0$: µ-law e A-law.

### Derivazione — Costante $\alpha$ per µ-law
**Fonte:** [[Campionamento_AD_DA.pdf#page=43]] (formula data senza passaggi)
> 🧩 Derivazione mia (ricondotta alla legge logaritmica per $\mu|x|/X_{max}\gg1$)
$$
\begin{aligned}
F(x) &= \frac{X_{max}}{\ln(1+\mu)}\ln\left(1+\frac{\mu x}{X_{max}}\right) && x>0 \\
&\approx \frac{X_{max}}{\ln(1+\mu)}\left[\ln\frac{\mu}{X_{max}} + \ln x\right] && 1+\mu x/X_{max}\approx\mu x/X_{max} \\
\Rightarrow \frac1k &= \frac{X_{max}}{\ln(1+\mu)} \Rightarrow kX_{max} = \ln(1+\mu) && \text{confronto con } c+\tfrac1k\ln x \\
\text{SNR} &= \frac{3M^2}{(kX_{max})^2} = \frac{3\cdot2^{2b}}{\ln^2(1+\mu)} && \text{SNR logaritmico} \\
\text{SNR}_{dB} &= 6.02\,b + 4.77 - 20\log_{10}\ln(1+\mu) && \text{come per i 6 dB/bit}
\end{aligned}
$$
**Numeri:** $\mu = 255$: $\ln256 = 5.545$; $20\log_{10}5.545 = 14.88$ dB; $\alpha = 4.77-14.88 = -10.11$ dB ✓ ([[Campionamento_AD_DA.pdf#page=43]]).
**Termine trascurato:** esattamente $1/F'(x) = \frac{\ln(1+\mu)}{X_{max}}\left(x + \frac{X_{max}}{\mu}\right)$. L'approssimazione trascura $X_{max}/\mu$ rispetto a $|x|$, quindi vale per $|x|\gg X_{max}/255$; per segnali molto deboli l'SNR peggiora.

### Derivazione — Costante $\alpha$ per A-law
> 🧩 Derivazione mia
$$
\begin{aligned}
F(x) &= \frac{X_{max}}{1+\ln A}\left[1+\ln A+\ln\frac{x}{X_{max}}\right] && \text{ramo logaritmico, } x\ge X_{max}/A \\
\Rightarrow \frac1k &= \frac{X_{max}}{1+\ln A} \Rightarrow kX_{max} = 1+\ln A && \text{coefficiente di } \ln x \\
\text{SNR}_{dB} &= 6.02\,b+4.77-20\log_{10}(1+\ln A)
\end{aligned}
$$
**Numeri:** $A = 87.6$: $\ln87.6 = 4.473$; $1+\ln A = 5.473$; $20\log_{10}5.473 = 14.76$ dB; $\alpha = 4.77-14.76 = -9.99$ dB ✓.
Qui il ramo logaritmico è **esatto** (non approssimato) per $|x|\ge X_{max}/A$. Sotto quella soglia la legge è **lineare**, cioè equivale a una quantizzazione uniforme.

### Derivazione — Controlli sulle leggi µ e A
> 🧩 Sanity check miei
- $F(X_{max}) = X_{max}$ per entrambe: $\ln(1+\mu)/\ln(1+\mu) = 1$ e $(1+\ln A)/(1+\ln A) = 1$ ✓.
- A-law continua in $|x| = X_{max}/A$: entrambi i rami valgono $X_{max}/(1+\ln A)$ ✓.
- µ-law con $\mu\to0$: $\ln(1+\mu a)/\ln(1+\mu)\to\mu a/\mu = a$, quindi $F(x) = x$ ✓ ([[Campionamento_AD_DA.pdf#page=41]]).
- A-law con $A = 1$: la soglia $X_{max}/A = X_{max}$ copre tutto il range, e $F(x) = X_{max}\cdot\frac{|x|/X_{max}}{1}\text{sgn}(x) = x$ ✓ ([[Campionamento_AD_DA.pdf#page=42]]).

## Spiegazione

### Confronto delle prestazioni
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=43]]

| Quantizzatore | $\text{SNR}_{dB}$ | Dipende dal livello? |
|---|---|---|
| A-law, $A=87.6$ | $6.02b-9.99$ | no (idealmente) |
| µ-law, $\mu=255$ | $6.02b-10.11$ | no (idealmente) |
| Uniforme, $k_c=4$ | $6.02b-7.3$ | **sì**, tramite $k_c = X_{max}/x_{rms}$ |

La legge dei 6 dB/bit vale ancora. A pieno carico il companding perde circa 3 dB rispetto all'uniforme con $k_c=4$, ma **mantiene** l'SNR quando il segnale si abbassa, mentre l'uniforme perde 6 dB per ogni dimezzamento di $x_{rms}$.

> 🧩 Derivazione mia (il confronto quantitativo): $-7.3-(-9.99)\approx2.7$ dB e $-7.3-(-10.11)\approx2.8$ dB. Con un segnale 20 dB sotto il four-sigma loading ($k_c = 40$), l'uniforme dà $6.02b + 4.77 - 32.04 = 6.02b - 27.3$ dB: 17 dB peggio del compander.

![[campionamento-p43-prestazioni-companding.png]]
*SNR (dB) in funzione del livello relativo d'ingresso (dB, da −50 a 0) — [[Campionamento_AD_DA.pdf#page=43]]. La curva **µ-law** ($\mu = 255$) è quasi piatta su un ampio intervallo di livelli e cala solo per livelli molto bassi. La retta della **quantizzazione uniforme** (senza companding) cresce di 1 dB per ogni dB di livello, supera la µ-law solo vicino al fondo scala e le resta nettamente sotto per segnali deboli. La tacca a −4.77 dB sull'asse orizzontale segna l'estremo destro del grafico.*

> 🧩 Lettura mia della figura: la pendenza unitaria della retta uniforme discende da $\text{SNR}_{dB} = 6.02b + 4.77 - 20\log_{10}(X_{max}/x_{rms})$. Ogni dB in più di $x_{rms}$ riduce $[k_c]_{dB}$ di 1 dB.

### Grafico SNR in funzione del livello, anche per la legge A

![[grafico-snr-vs-livello-companding.png]]
*🧩 Grafico mio. Ricostruisce il grafico di [[Campionamento_AD_DA.pdf#page=43]] con le formule della slide, e aggiunge la legge A. Parametri: $b = 8$, ingresso di Laplace con $x_{rms}$ variabile, sovraccarico trascurato. Le curve µ e A si assestano proprio su $6.02b + \alpha$: $48.2 - 10.11 = 38.0$ dB e $48.2 - 9.99 = 38.2$ dB. Tra −40 e 0 dB restano entro circa 2.5 dB da quel valore (quantizzazione robusta), mentre la retta uniforme perde 1 dB per ogni dB di livello. L'uniforme è migliore solo sopra circa −15 dB. Con $k_c = 4$, cioè livello $-12$ dB, vale $48.2 - 7.3 = 40.9$ dB, in accordo con il valore di [[Campionamento_AD_DA.pdf#page=43]]. La legge A cala prima della µ a livelli molto bassi: sotto $X_{max}/A$ lavora nel tratto lineare, che equivale a un quantizzatore uniforme.*

> 🧩 Derivazione mia delle curve (formula integrale di [[Campionamento_AD_DA.pdf#page=39]], $\text{MSE} = \frac{X_{max}^2}{3M^2}E\big[1/F'(x)^2\big]$, ingresso di Laplace con $\lambda = \sqrt2/x_{rms}$, $E|x| = x_{rms}/\sqrt2$):
> $$
> \begin{aligned}
> \text{uniforme: } F' = 1 &\Rightarrow \text{SNR} = 3M^2\,x_{rms}^2/X_{max}^2 \\
> \mu\text{-law: } \frac{1}{F'(x)} = \frac{\ln(1+\mu)}{\mu}\Big(1+\frac{\mu|x|}{X_{max}}\Big) &\Rightarrow E\Big[\frac{1}{F'^2}\Big] = \frac{\ln^2(1+\mu)}{\mu^2}\Big(1 + \frac{2\mu E|x|}{X_{max}} + \frac{\mu^2x_{rms}^2}{X_{max}^2}\Big) \\
> A\text{-law: } \frac{1}{F'(x)^2} = (1+\ln A)^2\cdot\begin{cases}1/A^2 & |x|<X_{max}/A\\ x^2/X_{max}^2 & \text{altrimenti}\end{cases} &\Rightarrow E\Big[\frac{1}{F'^2}\Big] = (1+\ln A)^2\Big[\frac{1-e^{-\lambda a}}{A^2} + \frac{e^{-\lambda a}(a^2+2a/\lambda+2/\lambda^2)}{X_{max}^2}\Big],\ a = \frac{X_{max}}{A}
> \end{aligned}
> $$
> Per $\mu|x|\gg X_{max}$ il termine dominante della µ-law è $\mu^2x_{rms}^2/X_{max}^2$: si ritrova $\text{SNR} = 3M^2/\ln^2(1+\mu)$, cioè il valore costante della slide.

### Curve delle leggi µ e A
![[campionamento-p41-mu-law.png]]
*$F(x)$ normalizzata (output vs input in $[0,1]$) per $\mu = 0, 1, 5, 100, 255$ — [[Campionamento_AD_DA.pdf#page=41]]. Con $\mu = 0$ è la bisettrice (uniforme); al crescere di $\mu$ la curva è sempre più ripida vicino a 0, cioè comprime di più.*

![[campionamento-p42-a-law.png]]
*$F(x)$ normalizzata per $A = 1, 2, 5, 87.6, 100$ — [[Campionamento_AD_DA.pdf#page=42]]. Con $A = 1$ è la bisettrice (uniforme); al crescere di $A$ la compressione aumenta.*

> 🎯 Esame: derivare la legge logaritmica dalla richiesta "SNR indipendente da $f_X$"; spiegare perché serve µ/A-law; confrontare gli SNR; sapere µ=255 (USA, Canada, Giappone) e A=87.6 (Europa, collegamenti internazionali), entrambe nella [[g711]].

## Perché importa

Risolve il problema della quantizzazione robusta posto dalle applicazioni telefoniche ([[Campionamento_AD_DA.pdf#page=36]]). Le approssimazioni a 7 segmenti delle leggi µ e A sono standardizzate dall'ITU-T in [[g711]] ([[Campionamento_AD_DA.pdf#page=41]], [[Campionamento_AD_DA.pdf#page=42]]).

## Connessioni

- [[quantizzazione-non-uniforme]] — il companding è un modo di realizzarla.
- [[snr-di-quantizzazione]] — stessa pendenza di 6 dB/bit, costante diversa.
- [[funzione-di-variabile-aleatoria]] — $F(x)$ è una trasformazione non lineare della v.a. $x(n)$.
- [[legge-mu]], [[legge-a]], [[g711]] — le leggi e lo standard.
- [[variabili-aleatorie-notevoli]] — pdf di Laplace della voce.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=36]] – [[Campionamento_AD_DA.pdf#page=43]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
