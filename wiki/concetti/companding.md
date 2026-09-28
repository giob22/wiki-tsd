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

Perché questa catena *è* un quantizzatore non uniforme, e che cosa resta da progettare, è spiegato in [[#Idea chiave del companding]], qui sotto.

Obiettivo: **quantizzazione robusta**, cioè SNR circa **indipendente dal livello** del segnale d'ingresso. In telefonia serve per la grande variabilità dei parlatori.

Motivazione ([[Campionamento_AD_DA.pdf#page=36]]):
- il quantizzatore ottimo di Lloyd-Max assume segnale **stazionario** e richiede di conoscere la pdf;
- come il quantizzatore uniforme, ha prestazioni **fortemente dipendenti dal livello** del segnale d'ingresso;
- in telefonia è fondamentale che le prestazioni siano circa indipendenti dal livello, vista la grande variabilità dei parlatori: è la **quantizzazione robusta**;
- per studiarla si assume che la legge non uniforme sia realizzata con il companding; in decodifica si applica la legge simmetrica, l'**espansione**.

![[campionamento-p36-companding.png]]
*Schema ([[Campionamento_AD_DA.pdf#page=36]]): compressore analogico $F(x)$ → quantizzatore uniforme a $n$ bit → decodificatore uniforme a $n$ bit → espansore analogico $F^{-1}(x)$.*

> ⚠️ Probabile refuso nella figura: il secondo blocco è etichettato «n-bit uniform **decoder**» come il terzo. Dal testo («compressione seguita da una quantizzazione uniforme») dovrebbe essere l'**encoder** (quantizzatore/codificatore uniforme).

### Idea chiave del companding
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=36]] (schema), [[Campionamento_AD_DA.pdf#page=38]] (soglie), [[Campionamento_AD_DA.pdf#page=39]] (MSE in funzione di $F'$)

In una frase: **quantizzare in modo uniforme il segnale compresso $F(x)$ equivale a quantizzare in modo non uniforme il segnale vero $x$.** Per questo il progetto del quantizzatore non uniforme si riduce alla scelta della legge di compressione $F$.

**1. Il problema di partenza.** Per la voce servono intervalli **stretti** vicino a zero, dove la pdf è alta, e **larghi** sulle ampiezze grandi, che sono rare ([[Campionamento_AD_DA.pdf#page=32]]). Costruire direttamente un quantizzatore così vuol dire scegliere le $M-1$ soglie $x_i$ e gli $M$ livelli $q_i$. È quello che fa Lloyd-Max ([[Campionamento_AD_DA.pdf#page=34]]), con i limiti elencati sopra ([[Campionamento_AD_DA.pdf#page=36]]).

**2. L'idea.** Il companding non costruisce direttamente il quantizzatore non uniforme. Deforma l'asse delle ampiezze e poi usa il quantizzatore uniforme, già noto ([[Campionamento_AD_DA.pdf#page=36]]):
1. il compressore calcola $y = F(x)$;
2. un quantizzatore uniforme $Q_u$ quantizza $y$, con passo $\Delta = 2X_{max}/M$ e livelli al centro degli intervalli ([[quantizzazione-uniforme]]);
3. l'espansore riporta il livello sull'asse originale con $F^{-1}$.

**3. Perché la catena è un quantizzatore non uniforme su $x$** ([[Campionamento_AD_DA.pdf#page=38]]).
- Sull'asse $y$ le soglie $y_i$ di $Q_u$ sono equidistanti, a distanza $\Delta$.
- $F$ è crescente, quindi $x_{i-1} < x < x_i \iff F(x_{i-1}) < F(x) < F(x_i)$. In parole: $x$ cade in $R_i = (x_{i-1}, x_i)$ **se e solo se** $y = F(x)$ cade nell'intervallo uniforme $(F(x_{i-1}), F(x_i))$.
- Quindi le soglie sull'asse $x$ sono le controimmagini delle soglie uniformi: $x_i = F^{-1}(y_i)$. È la frase della slide letta al contrario: $F$ trasforma le soglie $x_{i-1}, x_i$ del quantizzatore non uniforme nelle soglie $F(x_{i-1}), F(x_i)$ di quello uniforme, e $F(x_i) - F(x_{i-1}) = \Delta$.
- Sull'asse $y$ gli intervalli hanno tutti ampiezza $\Delta$. Sull'asse $x$ hanno ampiezza $\Delta_i \approx \Delta/F'(x_i)$ (derivazione sotto): **stretti dove $F$ è ripida** ($F'$ grande), larghi dove $F$ è piatta ($F'$ piccola).

> 🧩 Derivazione mia (completa lo schema di [[Campionamento_AD_DA.pdf#page=36]]):
> - $F$ deve essere **strettamente crescente**, altrimenti non è invertibile e l'espansore $F^{-1}$ non esiste. La legge logaritmica, la µ-law e la A-law lo sono.
> - L'uscita della catena è $F^{-1}$ del livello uniforme. In formula:
>
> $$Q(x) = F^{-1}\big(Q_u(F(x))\big)$$
>
> - Anche i livelli restituiti, $q_i = F^{-1}(\text{livello uniforme } i)$, sono quindi non uniformi. Senza l'espansore l'uscita resterebbe sulla scala compressa $y$.
> - L'equivalenza è **esatta** per qualunque $M$, perché usa solo il fatto che $F$ è crescente. È approssimata solo la formula $\Delta_i\approx\Delta/F'(x_i)$, che richiede l'alta risoluzione ([[Campionamento_AD_DA.pdf#page=37]]). Verifica numerica in [[#Derivazione — Esempio µ-law, soglie e livelli equivalenti]].
> - Intuizione, la "lente d'ingrandimento": dove $F'>1$ il compressore allarga le ampiezze, dove $F'<1$ le schiaccia. Per la µ-law $F'(0)\approx46$ e $F'(X_{max})\approx0.18$ (calcolo nell'esempio). Il quantizzatore uniforme vede quindi le ampiezze piccole ingrandite circa 46 volte e quelle grandi rimpicciolite, e quantizza le prime molto più finemente.

**4. Cosa si sposta su $F$.**
- Il quantizzatore uniforme è **fisso**: scelto $M$, il passo è $\Delta = 2X_{max}/M$ e non c'è altro da decidere.
- Tutta la non uniformità sta in $F$: la pendenza $F'(x)$ decide dove gli intervalli su $x$ sono stretti e dove sono larghi.
- [[Campionamento_AD_DA.pdf#page=39]] lo rende quantitativo: $\text{MSE} = \frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$. Fissati $M$ e la pdf $f_X$, l'MSE dipende **solo da $F'$**.
- Progettare il quantizzatore non uniforme vuol dire quindi **scegliere la funzione $F$**.

> 🧩 Confronto mio: Lloyd-Max sceglie $2M-1$ numeri, cioè $M-1$ soglie e $M$ livelli ([[Campionamento_AD_DA.pdf#page=34]]). Il companding sceglie **una funzione**, e soglie e livelli ne discendono: $x_i = F^{-1}(y_i)$ e $q_i = F^{-1}(\text{livello uniforme } i)$.

**5. Con quale criterio si sceglie $F$.** Nel corso il criterio è la **robustezza** ([[Campionamento_AD_DA.pdf#page=36]]): l'SNR deve essere circa indipendente dal livello del segnale. Da questo criterio viene la legge logaritmica ([[Campionamento_AD_DA.pdf#page=40]], derivazione sotto), approssimata in pratica dalla µ-law e dalla A-law ([[Campionamento_AD_DA.pdf#page=41]], [[Campionamento_AD_DA.pdf#page=42]]). Non è il criterio di Lloyd-Max, cioè l'MSE minimo per una pdf nota. A pieno carico la legge logaritmica perde circa 3 dB rispetto all'uniforme con $k_c = 4$, ma mantiene l'SNR quando il livello scende ([[Campionamento_AD_DA.pdf#page=43]], vedi *Confronto delle prestazioni*).

![[grafico-companding-soglie-mu.png]]
*🧩 Grafico mio (legge µ di [[Campionamento_AD_DA.pdf#page=41]], principio di [[Campionamento_AD_DA.pdf#page=38]]; script in `output/grafici/`). $\mu = 255$, $M = 8$ ($b = 3$ bit), semiasse positivo: $F$ è dispari e il lato negativo è simmetrico. **Sinistra:** le soglie uniformi sull'asse $y$ (0.25, 0.5, 0.75, 1 in unità di $X_{max}$) scendono sull'asse $x$ attraverso la curva e diventano 0.012, 0.059, 0.247, 1. Stesso colore = stesso intervallo: quattro intervalli uguali su $y$ diventano quattro intervalli su $x$, ognuno 4 volte il precedente. Senza compressione ($F(x) = x$, puntinata) le soglie resterebbero equidistanti. **Destra:** la caratteristica della catena completa $Q(x) = F^{-1}(Q_u(F(x)))$ (arancione) confrontata con il quantizzatore uniforme con lo stesso $M$ (tratteggiata): gradini fitti vicino a zero e un solo gradino largo da 0.247 a 1. I numeri sono quelli della [[#Derivazione — Esempio µ-law, soglie e livelli equivalenti]].*

> 🎯 Esame: spiegare perché compressione + quantizzazione uniforme + espansione equivale a un quantizzatore non uniforme su $x$, perché il progetto si riduce alla scelta di $F$, e con quale criterio la si sceglie.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $Q(x) = F^{-1}\big(Q_u(F(x))\big)$, soglie $x_i = F^{-1}(y_i)$ | catena compressore → quantizzatore uniforme $Q_u$ → espansore: è un quantizzatore non uniforme su $x$ | 🧩 dallo schema di [[Campionamento_AD_DA.pdf#page=36]] e da [[Campionamento_AD_DA.pdf#page=38]] |
| $\text{MSE}\approx\frac{1}{12}\sum_{i=1}^M p_i\Delta_i^2$, $\Delta_i = x_i-x_{i-1}$, $p_i\approx f_X(x_i)\Delta_i$ | MSE ad alta risoluzione | [[Campionamento_AD_DA.pdf#page=37]] |
| $\Delta_i\approx\dfrac{\Delta}{F'(x_i)} = \dfrac{1}{F'(x_i)}\dfrac{2X_{max}}{M}$ | ampiezza locale degli intervalli | [[Campionamento_AD_DA.pdf#page=38]] |
| $\text{MSE} = \dfrac{X_{max}^2}{3M^2}\displaystyle\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$ | MSE in forma integrale | [[Campionamento_AD_DA.pdf#page=39]] |
| $\text{SNR} = \dfrac{\int_0^{X_{max}}x^2f_X(x)\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx}$ | SNR del compander | [[Campionamento_AD_DA.pdf#page=39]] |
| $F(x) = X_{max}+\frac1k\ln\frac{x}{X_{max}}$, $x\in[0,X_{max}]$ | legge logaritmica ideale | [[Campionamento_AD_DA.pdf#page=40]] |
| $\text{SNR} = \dfrac{3M^2}{k^2X_{max}^2}$ | SNR della legge logaritmica | [[Campionamento_AD_DA.pdf#page=40]] |
| $F(x) = X_{max}\dfrac{\ln(1+\mu\|x\|/X_{max})}{\ln(1+\mu)}\text{sgn}(x)$ | **µ-law** ($\mu=255$) → [[legge-mu]] | [[Campionamento_AD_DA.pdf#page=41]] |
| $x_j = \dfrac{X_{max}}{\mu}\Big[(1+\mu)^{2j/M}-1\Big]$, $j = 0,\dots,M/2$ | soglie equivalenti della µ-law sull'asse $x$ | 🧩 da [[Campionamento_AD_DA.pdf#page=41]], vedi [[#Derivazione — Esempio µ-law, soglie e livelli equivalenti]] |
| $F(x) = \begin{cases}X_{max}\frac{A\|x\|/X_{max}}{1+\ln A}\text{sgn}(x) & 0\le\|x\|\le X_{max}/A\\ X_{max}\frac{1+\ln(A\|x\|/X_{max})}{1+\ln A}\text{sgn}(x) & X_{max}/A\le\|x\|\le X_{max}\end{cases}$ | **A-law** ($A=87.6$) → [[legge-a]] | [[Campionamento_AD_DA.pdf#page=42]] |

> 🧮 Formula chiave — prestazioni ([[Campionamento_AD_DA.pdf#page=43]]), segnale che impegna tutta la dinamica:
> $$\text{SNR}_{dB}\approx6.02\,b+\alpha,\qquad \alpha = \begin{cases}4.77-20\log_{10}[\ln(1+\mu)] & \mu\text{-law}\\ 4.77-20\log_{10}[1+\ln A] & A\text{-law}\\ 4.77-20\log_{10}(X_{max}/x_{rms}) & \text{uniforme}\end{cases}$$

Simboli: $M$ = numero di livelli; $\Delta = 2X_{max}/M$ = passo del quantizzatore uniforme **dopo** la compressione; $y = F(x)$ = segnale compresso [V]; $Q_u$ = quantizzatore uniforme sull'asse $y$, con soglie $y_i$ equidistanti; $F'$ = derivata della legge (adimensionale); $k$ [1/V] e $c$ [V] costanti; $\mu$, $A$ parametri adimensionali; $\text{sgn}$ = funzione segno.

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

> 🧩 Lettura mia: è la forma quantitativa dell'[[#Idea chiave del companding]]. Intervalli uguali ($\Delta$) sull'asse compresso corrispondono a intervalli diversi ($\Delta_i$) sull'asse $x$, e il fattore di conversione è la pendenza locale $F'(x_i)$. Il segno $\approx$ viene solo dal rapporto incrementale sostituito con la derivata: le soglie $x_i = F^{-1}(y_i)$ sono esatte.

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

### Derivazione — Esempio µ-law, soglie e livelli equivalenti
**Fonte:** [[Campionamento_AD_DA.pdf#page=41]] (µ-law), [[Campionamento_AD_DA.pdf#page=38]] (soglie $x_i \leftrightarrow F(x_i)$), [[Campionamento_AD_DA.pdf#page=40]] (intervallo che raddoppia col livello)
> 🧩 Derivazione mia: rende numerica l'[[#Idea chiave del companding]]. Lavoro sul semiasse $0\le x\le X_{max}$; il semiasse negativo è simmetrico perché $F$ è dispari.

**Passo 1 — inversa della µ-law** (è l'espansore, e serve per calcolare le soglie):
$$
\begin{aligned}
y &= X_{max}\frac{\ln(1+\mu x/X_{max})}{\ln(1+\mu)} && \mu\text{-law per } x\ge0\ \text{(p.41)} \\
\frac{y}{X_{max}}\ln(1+\mu) &= \ln\Big(1+\frac{\mu x}{X_{max}}\Big) && \text{moltiplico per } \ln(1+\mu)/X_{max} \\
(1+\mu)^{y/X_{max}} &= 1+\frac{\mu x}{X_{max}} && \text{esponenziale dei due membri: } e^{a\ln b} = b^{a} \\
x = F^{-1}(y) &= \frac{X_{max}}{\mu}\Big[(1+\mu)^{y/X_{max}}-1\Big] && \text{isolo } x
\end{aligned}
$$

**Passo 2 — soglie equivalenti.** Le soglie uniformi positive sull'asse $y$ sono $y_j = j\Delta$, $j = 0,\dots,M/2$, con $\Delta = 2X_{max}/M$. Con $M$ pari lo zero è una soglia (come nell'esempio $M = 4$ di [[quantizzazione-uniforme]]).
$$
\begin{aligned}
x_j &= F^{-1}(j\Delta) = \frac{X_{max}}{\mu}\Big[(1+\mu)^{j\Delta/X_{max}}-1\Big] && \text{passo 1 con } y = j\Delta \\
&= \frac{X_{max}}{\mu}\Big[(1+\mu)^{2j/M}-1\Big] && \Delta/X_{max} = 2/M
\end{aligned}
$$

**Passo 3 — ampiezze degli intervalli.**
$$
\begin{aligned}
\Delta_j = x_j - x_{j-1} &= \frac{X_{max}}{\mu}\Big[(1+\mu)^{2j/M}-(1+\mu)^{2(j-1)/M}\Big] && \text{differenza di due soglie: i } -1 \text{ si elidono} \\
&= \frac{X_{max}}{\mu}(1+\mu)^{2(j-1)/M}\Big[(1+\mu)^{2/M}-1\Big] && \text{raccolgo } (1+\mu)^{2(j-1)/M} \\
\frac{\Delta_{j+1}}{\Delta_j} &= (1+\mu)^{2/M} && \text{rapporto tra ampiezze consecutive: costante}
\end{aligned}
$$
Ogni intervallo è più largo del precedente sempre dello stesso fattore: le ampiezze crescono in **progressione geometrica**.

**Passo 4 — numeri con $\mu = 255$ e $M = 8$ ($b = 3$ bit).**
- $1+\mu = 256$, quindi $(1+\mu)^{2/M} = 256^{1/4} = 4$ e $x_j = \frac{4^j-1}{255}X_{max}$.
- Il quantizzatore uniforme con lo stesso $M$ ha $\Delta = 2X_{max}/8 = 0.25\,X_{max}$.
- I livelli vengono dal passo 1 con $y = (j-\tfrac12)\Delta$, cioè il centro dell'intervallo uniforme $j$: $q_j = \frac{X_{max}}{255}\big[256^{(2j-1)/8}-1\big] = \frac{2^{2j-1}-1}{255}X_{max}$, perché $256^{1/8} = 2$.

| $j$ | soglia uniforme $y_j = j\Delta$ | soglia su $x$: $x_j$ | ampiezza $\Delta_j$ | $\Delta_j/\Delta$ | livello $q_j$ |
|---|---|---|---|---|---|
| 1 | $0.25\,X_{max}$ | $3/255 = 0.0118\,X_{max}$ | $0.0118\,X_{max}$ | $0.047$ (21 volte più stretto) | $1/255 = 0.0039\,X_{max}$ |
| 2 | $0.50\,X_{max}$ | $15/255 = 0.0588\,X_{max}$ | $0.0471\,X_{max}$ | $0.188$ | $7/255 = 0.0275\,X_{max}$ |
| 3 | $0.75\,X_{max}$ | $63/255 = 0.2471\,X_{max}$ | $0.1882\,X_{max}$ | $0.753$ | $31/255 = 0.1216\,X_{max}$ |
| 4 | $1.00\,X_{max}$ | $255/255 = X_{max}$ | $0.7529\,X_{max}$ | $3.01$ (3 volte più largo) | $127/255 = 0.4980\,X_{max}$ |

**Lettura:** quattro intervalli **uguali** sull'asse compresso diventano quattro intervalli **diversi** sull'asse $x$, ognuno 4 volte il precedente. Sotto $X_{max}/4$ il companding mette tre soglie ($0.0118$, $0.0588$ e $0.2471\,X_{max}$), mentre l'uniforme non ne ha nessuna oltre allo zero. Sopra $0.2471\,X_{max}$ c'è un solo intervallo, restituito col livello $0.498\,X_{max}$.

**Verifiche:**
- Estremi: $x_0 = 0$ e $x_{M/2} = \frac{X_{max}}{\mu}\big[(1+\mu)-1\big] = X_{max}$. Le soglie coprono esattamente $[0, X_{max}]$ ✓.
- Somma delle ampiezze: $(3+12+48+192)/255 = 255/255 = 1$, cioè $X_{max}$ ✓.
- Caso limite $\mu\to0$: per Taylor $(1+\mu)^{2j/M}\approx1+\frac{2j}{M}\mu$, quindi $x_j\approx\frac{X_{max}}{\mu}\cdot\frac{2j}{M}\mu = j\Delta$. Si ritrova il quantizzatore uniforme, coerente con $F(x) = x$ per $\mu = 0$ ([[Campionamento_AD_DA.pdf#page=41]]) ✓.
- Livelli: $q_4 = 0.498\,X_{max}$ non sta al centro di $R_4 = (0.247, 1)\,X_{max}$, che è $0.624\,X_{max}$. $F^{-1}$ non è lineare e sposta verso lo zero il centro dell'intervallo uniforme. Con $M = 8$ non siamo ad alta risoluzione. Al crescere di $M$, $F$ è quasi lineare dentro ogni intervallo e $q_i$ torna circa al centro, come assume [[Campionamento_AD_DA.pdf#page=37]].

**Passo 5 — esatto contro alta risoluzione.** Derivata della µ-law:
$$
\begin{aligned}
F'(x) &= \frac{X_{max}}{\ln(1+\mu)}\cdot\frac{\mu/X_{max}}{1+\mu x/X_{max}} && \tfrac{d}{dx}\ln(1+ax) = \tfrac{a}{1+ax},\ a = \mu/X_{max} \\
&= \frac{\mu}{\ln(1+\mu)\,(1+\mu x/X_{max})} && X_{max} \text{ si semplifica} \\
F'(0) &= \frac{\mu}{\ln(1+\mu)} = \frac{255}{5.545} = 45.99 && x = 0 \\
F'(X_{max}) &= \frac{\mu}{(1+\mu)\ln(1+\mu)} = \frac{255}{256\cdot5.545} = 0.180 && x = X_{max}
\end{aligned}
$$
La formula ad alta risoluzione $\Delta_i\approx\Delta/F'(x_i)$ prevede quindi un intervallo più stretto $\approx\Delta/46$ e uno più largo $\approx\Delta/0.180 = 5.57\,\Delta$. Le ampiezze esatte del passo 3 si avvicinano a questi valori al crescere di $M$:

| $b$ | $M$ | $(1+\mu)^{2/M}$ | più stretto / $\Delta$ (esatto) | più largo / $\Delta$ (esatto) |
|---|---|---|---|---|
| 3 | 8 | 4 | $1/21.3$ | $3.01$ |
| 4 | 16 | 2 | $1/31.9$ | $4.02$ |
| 8 | 256 | 1.044 | $1/45.0$ | $5.45$ |
| $\to\infty$ | $\to\infty$ | $\to1$ | $\to 1/F'(0) = 1/46.0$ | $\to 1/F'(X_{max}) = 5.57$ |

Le soglie $x_j = F^{-1}(j\Delta)$ sono esatte per ogni $M$. La formula $\Delta_i\approx\Delta/F'(x_i)$ invece diventa accurata solo per $M$ grande: con $b = 8$ sbaglia già solo del 2% circa.

**Collegamento con [[Campionamento_AD_DA.pdf#page=40]].** Con $M = 16$ il rapporto è esattamente 2: ogni intervallo è il doppio del precedente, e le soglie $x_j = \frac{2^j-1}{255}X_{max}$ quasi raddoppiano a ogni passo. È il comportamento della legge logaritmica descritto a p.40: l'intervallo raddoppia quando raddoppia il livello. In generale, dal passo 2 si ha $\frac{X_{max}}{\mu}(1+\mu)^{2(j-1)/M} = x_{j-1}+\frac{X_{max}}{\mu}$, e sostituendo nel passo 3:
$$\Delta_j = \Big(x_{j-1}+\frac{X_{max}}{\mu}\Big)\Big[(1+\mu)^{2/M}-1\Big]$$
L'ampiezza è proporzionale al livello $x_{j-1}$, a meno della costante $X_{max}/\mu$. Per $x\gg X_{max}/\mu$ il comportamento è logaritmico puro ($\Delta_i\propto x_i$). La costante è il prezzo di avere $F(0) = 0$: è lo stesso termine trascurato nella derivazione di $\alpha$ per la µ-law.

**Ipotesi:** $F$ = µ-law (strettamente crescente e dispari); quantizzatore uniforme simmetrico con $M$ pari e livelli al centro degli intervalli; nessun sovraccarico ($|x|\le X_{max}$).

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

- [[quantizzazione-non-uniforme]] — il companding la realizza con compressione + quantizzazione uniforme + espansione, e riduce il progetto alla scelta di $F$ ([[#Idea chiave del companding]]).
- [[quantizzazione-uniforme]] — è il blocco centrale della catena: il companding lo riusa così com'è, invece di progettare un quantizzatore nuovo.
- [[snr-di-quantizzazione]] — stessa pendenza di 6 dB/bit, costante diversa.
- [[funzione-di-variabile-aleatoria]] — $F(x)$ è una trasformazione non lineare della v.a. $x(n)$.
- [[legge-mu]], [[legge-a]], [[g711]] — le leggi e lo standard.
- [[variabili-aleatorie-notevoli]] — pdf di Laplace della voce.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=36]] – [[Campionamento_AD_DA.pdf#page=43]]

_Aggiornato: 2026-09-24 — resa esplicita l'idea chiave (quantizzare uniformemente $F(x)$ = quantizzare in modo non uniforme $x$; il progetto si sposta su $F$), esempio µ-law con soglie e livelli; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
