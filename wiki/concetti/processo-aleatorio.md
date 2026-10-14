---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria", "coppie-di-variabili-aleatorie", "spazio-di-probabilita"]
fonti_pdf: ["random_processes.pdf#page=2", "random_processes.pdf#page=3", "random_processes.pdf#page=4", "random_processes.pdf#page=5", "random_processes.pdf#page=6", "random_processes.pdf#page=7", "random_processes.pdf#page=8", "random_processes.pdf#page=9", "random_processes.pdf#page=10", "random_processes.pdf#page=11", "random_processes.pdf#page=25", "random_processes.pdf#page=45"]
---

# Processo aleatorio (processo stocastico)

## Definizione · [[random_processes.pdf#page=2|p. 2]]–[[random_processes.pdf#page=7|7]]

Un **processo stocastico**, detto anche processo aleatorio o **segnale aleatorio** (*random signal*), è l'estensione naturale del concetto di [[variabile-aleatoria]] quando si ha a che fare con **segnali**. Si scrive $X(t, \omega)$, dove $t$ è il tempo e $\omega$ l'esito di un esperimento aleatorio.

**Perché serve.** In molte situazioni l'ipotesi che un segnale sia deterministico non regge, e conviene modellarlo come **funzione aleatoria**. Due esempi della slide:
- il **rumore termico** nei circuiti elettronici;
- i segnali generati da una **sorgente d'informazione**.

**Dal segnale deterministico al processo**. Gli appunti partono dai segnali visti finora:
- un segnale $s(t)$ descritto nel dominio del tempo, con una **descrizione analitica** (una formula) o con un **grafico**, è un **segnale deterministico**: il suo valore in ogni istante è noto;
- «prendiamo questi segnali e li estendiamo su fenomeni non predicibili a priori» (il verbo è di lettura incerta);
- una **variabile aleatoria** associa a ogni esito $\omega \in \Omega$ un numero: $X: \omega \to X(\omega) \in \mathbb{R}$;
- per un processo invece «dobbiamo non associare un campione ma una funzione nel tempo»: a ogni esito $\omega_i$ corrisponde una forma d'onda $S(\omega_i, t)$. «Ad ogni campione associo una funzione nel tempo».

> 🧩 Negli appunti "campione" vuol dire **esito** $\omega$, cioè un punto dello spazio campione $\Omega$, non un campione nel tempo. La frase va letta così: a ogni esito non associo un numero ma un'intera funzione del tempo. È la stessa osservazione della slide di p. 7, più sotto.

![[random-processes-p3-appunti-da-va-a-processo.png]]
*Appunti a mano.*
- *In alto: $s(t)$ descritto nel dominio del tempo (descrizione analitica, grafico). Sono segnali deterministici.*
- *A sinistra: lo spazio $\Omega$ con un esito $\omega$ mandato in un punto della retta reale $\mathbb{R}$. È la variabile aleatoria $X: \omega \to X(\omega) \in \mathbb{R}$.*
- *A destra: un altro $\Omega$ con tre esiti $\omega_1, \omega_2, \omega_3$, ciascuno mandato in una forma d'onda diversa: $S(\omega_1, t)$, $S(\omega_2, t)$, $S(\omega_3, t)$.*

**Due modi di vederlo**:
1. **Collezione di forme d'onda.** A ogni esito $\omega = \omega_i$ dello spazio di probabilità $(\Omega, S, P)$ corrisponde un segnale deterministico $X(t, \omega_i) \equiv x_i(t)$, detto **realizzazione** (*sample function*). È un'idea simile a quella di variabile aleatoria.
   - Fissando un istante $t_0$, la funzione $X(t_0, \omega)$ è una **variabile aleatoria**.
   - Fissando sia $t_0$ sia $\omega_i$, $X(t_0, \omega_i)$ è un **numero**.
2. **Collezione di variabili aleatorie indicizzate dal tempo**, il punto di vista più adatto allo sviluppo matematico della teoria:
   - se l'insieme degli indici è $\mathbb{R}$, il processo è **a tempo continuo**;
   - se è $\mathbb{Z}$, il processo è **a tempo discreto**: una successione di variabili aleatorie $\{X_i\}_{i=-\infty}^{+\infty}$.

Per semplicità si omette $\omega$ e si scrive $X(t)$, oppure $x(t)$ quando non c'è ambiguità.

**Fissare $\omega$ o fissare $t$**: «$X(t, \omega)$ si particolarizza a seconda che fissi $\omega$ o $t$».
- $X(t, \bar\omega) = x(t)$: fissato l'esito, resta un **segnale nel tempo**, cioè una realizzazione;
- $X(\bar t, \omega) = X(\omega)$: fissato l'istante, si ottiene una **variabile aleatoria**;
- $X(\bar\omega, \bar t)$: fissati entrambi, è **un numero**.

Accanto gli appunti annotano i «due punti di vista». Il primo è la «collezione di variabili aleatorie indicizzate rispetto al tempo»; il secondo è rimasto in bianco (🧩 dalla slide di p.6 è la collezione di forme d'onda, punto 1 sopra).

Negli appunti di p. 5 la distinzione sul tempo è scritta così: $X(t, \omega)$ con $t \in \mathbb{R}$ è un processo **a tempo continuo**; $X(n, \omega)$ con $n \in \mathbb{Z}$ è un processo **a tempo discreto**.

> 📄 Osservazione della slide: in una **variabile aleatoria** l'esito dell'esperimento viene associato a un **numero**; in un **processo aleatorio** viene associato a una **forma d'onda**, funzione del tempo.

## Formule · [[random_processes.pdf#page=4|p. 4]]–[[random_processes.pdf#page=6|6]], [[random_processes.pdf#page=8|p. 8]]–[[random_processes.pdf#page=10|10]], [[random_processes.pdf#page=45|p. 45]]

| Formula | Significato |
|---|---|
| $X(t, \omega)$, con $X(t, \omega_i) \equiv x_i(t)$ | processo e sue realizzazioni |
| $F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \triangleq P[X(t_1) \le x_1, \dots, X(t_k) \le x_k]$ | CDF congiunta di ordine $k$, eq. (1) |
| $f_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \triangleq \dfrac{\partial^k}{\partial x_1 \cdots \partial x_k}F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k)$ | pdf congiunta di ordine $k$, eq. (2) |
| $X(n; \omega)$, $n \in \mathbb{Z}$ | processo a tempo discreto |
| $X(t) = A\cos(2\pi f_0 t + \Theta)$, $\Theta \sim \mathcal{U}(0, 2\pi)$ | sinusoide a fase casuale (esempio) |
| $F_{X(t_1)}(x) \triangleq P(\{X(t_1) \le x\})$ | CDF del primo ordine ($k = 1$ nella (1)) |
| $F_{X(t_1)X(t_2)}(x_1, x_2) = P(\{X(t_1) \le x_1, X(t_2) \le x_2\})$ | CDF del secondo ordine ($k = 2$) |
| $\int_{-\infty}^{+\infty} f_{X(t_1)X(t_2)}(x_1, x_2)\,dx_2 = f_{X(t_1)}(x_1)$ | pdf del primo ordine dalla pdf del secondo |
| $p_{X(n)}(x) = p^x q^{1-x}$ | DF del primo ordine del processo di Bernoulli |
| $p_{X(n_1)X(n_2)}(x_1, x_2) = p^{w(\mathbf{x})}q^{2 - w(\mathbf{x})}$ | DF del secondo ordine, lanci indipendenti |

Simboli: $t$ = tempo [s]; $\omega$ = esito, elemento dello spazio campione $\Omega$; $(x_1,\dots,x_k) \in \mathbb{R}^k$ = valori (nell'unità del segnale, es. V); $F$ adimensionale (è una probabilità); $f$ in [1/V$^k$]. Esempio della sinusoide: $A$ = ampiezza [V], $f_0$ = frequenza [Hz], $\Theta$ = fase [rad]. Processo di Bernoulli: $x \in \{0, 1\}$, $p = P(X(n) = 1)$, $q = 1 - p$, $w(\mathbf{x})$ = numero di 1 nel vettore $\mathbf{x} = (x_1, x_2)$; DF adimensionali.

> ⚠️ Refusi della slide: la derivata nella (2) è scritta $\partial^n$, ma le variabili sono $k$, quindi $\partial^k$; la correzione è scritta anche a mano sul PDF. Più sotto la slide rimanda alla «CDF congiunta (36)» invece che alla (1).

## Derivazioni

### Derivazione — Coerenza delle distribuzioni: quelle di ordine basso sono marginali · [[random_processes.pdf#page=9|p. 9]], [[random_processes.pdf#page=11|p. 11]]
**Fonte:** le CDF e pdf di ordine più basso si devono ottenere come marginali di quelle di ordine più alto. La riga della pdf è scritta anche a mano sulla slide 5: «integrando rispetto a una variabile ottengo la pdf di primo ordine».
> 🧩 Derivazione mia per $k = 2$ (per $k$ qualunque è identica), con le regole delle marginali di [[coppie-di-variabili-aleatorie]].

$$
\begin{aligned}
F_{X(t_1)}(x_1) &= P[X(t_1) \le x_1] = P[X(t_1) \le x_1,\ X(t_2) \le +\infty] && \{X(t_2) \le +\infty\} \text{ è l'evento certo} \\
&= F_{X(t_1),X(t_2)}(x_1, +\infty) && \text{definizione (1)} \\
f_{X(t_1)}(x_1) &= \int_{-\infty}^{+\infty} f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_2 && \text{marginale della pdf: integro via } x_2 \text{ (nota a mano, p.9)}
\end{aligned}
$$

"Coerenti" vuol dire che le famiglie di CDF (o pdf) non si possono scegliere a caso ordine per ordine: quelle di ordine più alto determinano quelle di ordine più basso.

### Derivazione — DF del processo di Bernoulli, primo e secondo ordine · [[random_processes.pdf#page=10|p. 10]], [[random_processes.pdf#page=11|11]]
> 🧩 Passaggi miei. $X(n) \in \{0, 1\}$ è l'esito del lancio $n$-esimo, $P(X(n) = 1) = p$, $q = 1 - p$.

**Primo ordine.** La formula $p^x q^{1-x}$ scrive i due casi in una riga sola:
$$
\begin{aligned}
p_{X(n)}(1) &= p^1\,q^0 = p && x = 1 \text{ (successo): l'esponente di } q \text{ si annulla} \\
p_{X(n)}(0) &= p^0\,q^1 = q && x = 0 \text{ (insuccesso): l'esponente di } p \text{ si annulla}
\end{aligned}
$$

**Secondo ordine**, con istanti distinti $n_1 \neq n_2$:
$$
\begin{aligned}
p_{X(n_1)X(n_2)}(x_1, x_2) &= P(X(n_1) = x_1)\,P(X(n_2) = x_2) && \text{«lanci statisticamente indipendenti»: la congiunta si fattorizza} \\
&= p^{x_1}q^{1-x_1}\cdot p^{x_2}q^{1-x_2} && \text{DF del primo ordine per ciascun lancio} \\
&= p^{x_1 + x_2}\,q^{2 - (x_1 + x_2)} && \text{stessa base: sommo gli esponenti} \\
&= p^{w(\mathbf{x})}\,q^{2 - w(\mathbf{x})} && x_i \in \{0, 1\} \Rightarrow x_1 + x_2 = \text{numero di 1} = w(\mathbf{x})
\end{aligned}
$$

| $\mathbf{x} = (x_1, x_2)$ | $w(\mathbf{x})$ | $p_{X(n_1)X(n_2)}(x_1, x_2)$ |
|---|---|---|
| (0, 0) | 0 | $q^2$ |
| (0, 1) | 1 | $pq$ |
| (1, 0) | 1 | $pq$ |
| (1, 1) | 2 | $p^2$ |

**Perché serve $w$:** la probabilità di una coppia dipende solo da **quanti** 1 contiene, non da **dove** stanno: (0, 1) e (1, 0) hanno la stessa probabilità $pq$.
**Sanity check:**
- $q^2 + 2pq + p^2 = (p + q)^2 = 1$ ✓;
- sommando su $x_2$ si ritrova il primo ordine, per esempio $p_{X(n_1)}(1) = pq + p^2 = p(q + p) = p$ ✓. È la coerenza tra gli ordini della derivazione sopra, nella versione discreta: una somma al posto dell'integrale.

**Ipotesi:** lanci indipendenti; istanti distinti (con $n_1 = n_2$ le due v.a. sarebbero la stessa). Senza indipendenza la congiunta non si fattorizza e non basta conoscere $p$.

> 🧩 Con $k$ lanci indipendenti lo stesso argomento dà $p^{w(\mathbf{x})}\,q^{k - w(\mathbf{x})}$ per ogni $k$. Il processo di Bernoulli è quindi **completamente caratterizzato**, nel senso della slide 6, da un solo numero: $p$.

## Spiegazione

### Esempio della slide: un rettangolo di segno casuale · [[random_processes.pdf#page=2|p. 2]]

$\Omega = \{0, 1\}$ con $P(\{\omega = 1\}) \triangleq p$ e $P(\{\omega = 0\}) \triangleq q = 1 - p$. Il segnale aleatorio è
$$
X(t, \omega) = \begin{cases} A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 0 \\[2mm] -A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 1 \end{cases}
$$

![[random-processes-p2-esempio-rect.png]]
*le due realizzazioni. $x(t, \omega = 0)$ vale $A$ per $0 < t < T$; $x(t, \omega = 1)$ vale $-A$ nello stesso intervallo. Fuori da $(0, T)$ entrambe valgono 0.*

> 🧩 Le due facce sull'esempio (lettura mia):
> - **come forme d'onda**: ci sono due sole realizzazioni possibili, i due rettangoli della figura;
> - **fissato un istante $t_0 \in (0, T)$**: $X(t_0)$ è una variabile aleatoria **discreta** che vale $A$ con probabilità $q$ e $-A$ con probabilità $p$, del tipo di [[variabili-aleatorie-notevoli|Bernoulli]] a meno di una trasformazione affine;
> - **fissato $t_0$ fuori da $(0, T)$**: $X(t_0) = 0$ con certezza.
>
> Media, autocorrelazione e covarianza di questo processo sono calcolate in [[momenti-di-un-processo]]: la media dipende da $t$.

### Esempio degli appunti: sinusoide a fase casuale · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]]

$$X(t) = A\cos(2\pi f_0 t + \Theta), \qquad \Theta \sim \mathcal{U}(0, 2\pi)$$
- $A$ [V] e $f_0$ [Hz] sono **deterministiche**;
- l'unica cosa aleatoria è la fase $\Theta$ [rad], uniforme in $(0, 2\pi)$: $f_\Theta(\vartheta) = \frac{1}{2\pi}$ per $0 \le \vartheta \le 2\pi$ e zero altrove. È il rettangolo disegnato negli appunti ([[variabili-aleatorie-notevoli|uniforme]]);
- nota di p.5: è un «segnale aleatorio ad ampiezza continua».

![[random-processes-p4-appunti-sinusoide-fase-casuale.png]]
*Appunti a mano: il processo, la pdf uniforme di $\Theta$ (altezza $1/(2\pi)$ tra 0 e $2\pi$), le tre particolarizzazioni di $X(t, \omega)$ viste sopra e, a destra, i «due punti di vista».*

> 🧩 Le tre particolarizzazioni sull'esempio (lettura mia):
> - **fisso l'esito**, cioè un valore $\bar\vartheta$ della fase: $x(t) = A\cos(2\pi f_0 t + \bar\vartheta)$ è un normale coseno deterministico. Le realizzazioni sono tutti i coseni di ampiezza $A$ e frequenza $f_0$, ciascuno spostato di una fase diversa;
> - **fisso l'istante $\bar t$**: $X(\bar t) = A\cos(2\pi f_0 \bar t + \Theta)$ è una variabile aleatoria, funzione della v.a. $\Theta$, con valori in $[-A, A]$;
> - **fisso entrambi**: $A\cos(2\pi f_0\bar t + \bar\vartheta)$ è un numero.
>
> Perché "ad ampiezza continua": $\Theta$ assume un continuo di valori, quindi anche $X(\bar t)$ assume con continuità tutti i valori tra $-A$ e $A$. Nel rettangolo della slide 2, invece, $X(t_0)$ vale solo $\pm A$ (o 0): ampiezza discreta.
>
> Media e autocorrelazione di questo processo sono calcolate in [[momenti-di-un-processo]]. A differenza del rettangolo, il processo è WSS ([[stazionarieta]]).

### Il quadro generale: esiti, realizzazioni, variabili aleatorie · [[random_processes.pdf#page=6|p. 6]], [[random_processes.pdf#page=7|7]]

![[random-processes-p7-realizzazioni.png]]
*Lo spazio campione $S$ contiene gli esiti $s_1, s_2, \dots, s_n$. Ogni esito, cioè ogni prova dell'esperimento, produce una forma d'onda $x_1(t), x_2(t), \dots, x_n(t)$ sull'intervallo $(-T, +T)$. Una linea verticale all'istante $t_k$ taglia tutte le forme d'onda nei valori $x_1(t_k), x_2(t_k), \dots, x_n(t_k)$: al variare dell'esito, sono i valori della variabile aleatoria $X(t_k)$.*

![[grafico-rp-realizzazioni.png]]
*🧩 Grafico mio (definizioni di p. 6; script in `output/grafici/`). Processo gaussiano a media nulla con autocorrelazione $e^{-|\tau|/\tau_c}$, $\tau_c = 0.5$. A sinistra cinque realizzazioni: fissato $t_0 = 6$, ognuna dà un numero (punto arancio). A destra i valori $X(t_0)$ di 5000 realizzazioni: il loro istogramma riproduce la pdf gaussiana $\mathcal{N}(0, 1)$. È la variabile aleatoria che si ottiene fissando il tempo.*

### Caratterizzazione statistica completa · [[random_processes.pdf#page=8|p. 8]], [[random_processes.pdf#page=9|9]], [[random_processes.pdf#page=11|p. 11]]

- La descrizione statistica di un processo si basa sulla CDF (o, in modo equivalente, sulla pdf) di **vettori di campioni** del segnale aleatorio.
- $X(t_1), \dots, X(t_k)$ sono le variabili aleatorie ottenute campionando $X(t)$ negli istanti $t_1, \dots, t_k$. La loro CDF congiunta è la (1) e la pdf congiunta la (2).
- Se si conosce la (1), o la (2), per **qualunque scelta** degli istanti $t_1, \dots, t_k$, si conosce la **caratterizzazione statistica di ordine $k$**.
- Il processo è **completamente caratterizzato** se si conosce la CDF (o pdf) congiunta di ordine $k$ per **ogni** $k \in \mathbb{N}$ e ogni scelta degli istanti.
- CDF e pdf devono essere **coerenti**: quelle di ordine più basso si ottengono come marginali di quelle di ordine più alto (derivazione sopra).
- Finora si è supposta l'ampiezza **continua**. Se l'ampiezza di $X(t)$ è **discreta** conviene usare la distribuzione di probabilità (DF, vedi [[variabile-aleatoria]]), per esempio nel processo di Bernoulli (sezione sotto).
- La caratterizzazione completa è difficile da ottenere in molti casi pratici. Ci si accontenta allora di una **caratterizzazione parziale**, cioè media e autocorrelazione: [[momenti-di-un-processo]].

> 🧩 Perché "difficile": servono infinite funzioni (tutte le pdf di ogni ordine $k$, per ogni scelta di istanti), mentre media e autocorrelazione sono solo due funzioni, di una e di due variabili.

**Primo e secondo ordine negli appunti**. Gli appunti costruiscono la (1) partendo da $k = 1$ e $k = 2$, per un processo «a tempo continuo e ampiezza continua»:
- fissato $t = t_1$, $X(t_1)$ è una variabile aleatoria, con CDF $F_{X(t_1)}(x) \triangleq P(\{X(t_1) \le x\})$ per ogni $x \in \mathcal{X}$. Se la si conosce per ogni $t_1$ («se lo sappiamo»), si ha la **CDF del primo ordine**;
- campionando in due istanti, $X(t_1)$ e $X(t_2)$ sono una coppia di variabili aleatorie e se ne può definire la CDF congiunta, $F_{X(t_1)X(t_2)}(x_1, x_2) = P(\{X(t_1) \le x_1, X(t_2) \le x_2\})$ per ogni $(x_1, x_2) \in \mathcal{X}\times\mathcal{X}$. Se si «giunge a conoscerla» per ogni coppia $t_1, t_2$, si conosce la **CDF del secondo ordine**.

> 🧩 $\mathcal{X}$ è l'insieme dei valori che il processo può assumere: con ampiezza continua, $\mathbb{R}$ o un suo intervallo. "Per ogni $t_1$" è la parte importante: la CDF di $X(t_1)$ descrive un solo istante, mentre la CDF del primo ordine è l'intera famiglia di CDF, una per istante. È quindi una funzione sia di $x$ sia di $t_1$.

> ⚠️ Negli appunti c'è scritto $\forall t_1 \in \mathbb{Z}$, ma il processo è a tempo continuo: va letto $t_1 \in \mathbb{R}$.

![[random-processes-p8-appunti-cdf-primo-secondo-ordine.png]]
*Appunti a mano: CDF del primo ordine, con la nota in verde «se lo sappiamo → ottengo la CDF del primo ordine» sotto $\forall t_1$, e CDF congiunta del secondo ordine.*

**Dalla pdf del secondo ordine a quella del primo** (nota a mano sulla slide 5): «integrando rispetto a una variabile»
$$\int_{-\infty}^{+\infty} f_{X(t_1)X(t_2)}(x_1, x_2)\,dx_2 = f_{X(t_1)}(x_1)$$
«ottengo la pdf di primo ordine». È la riga della pdf nella derivazione della coerenza, sopra. Sotto c'è una seconda nota, che leggo «non si dice marginalizzazione».

> ❓ Nota non chiara: l'operazione scritta negli appunti è proprio quella che la slide di p. 11 descrive con le «marginali», e che in [[coppie-di-variabili-aleatorie]] si chiama marginalizzazione. Forse la nota va letta in un altro modo (per esempio «ciò si dice marginalizzazione»). Da verificare sugli appunti.

![[random-processes-p9-marginalizzazione.png]]
*con le note a mano: la correzione $\partial^n \to \partial^k$ nella (2) e, sotto, l'integrale che dalla pdf congiunta di $X(t_1), X(t_2)$ dà la pdf di $X(t_1)$.*

### Ampiezza discreta: la DF del processo di Bernoulli (appunti p.10) · [[random_processes.pdf#page=10|p. 10]], [[random_processes.pdf#page=11|11]]

La slide 6 dice che con ampiezza discreta conviene usare la DF e cita come esempio il processo di Bernoulli. Gli appunti di p.10 lo scrivono: «per processi aleatori discreti a tempo discreto utilizzo la DF».
- **DF del primo ordine:** $p_{X(n)}(x) \triangleq P(X(n) = x) = p^x\,q^{1-x}$, con $x \in \{0, 1\}$.
- **DF del secondo ordine:** $p_{X(n_1)X(n_2)}(x_1, x_2) \triangleq P(\{X(n_1) = x_1, X(n_2) = x_2\}) = p^{w(\mathbf{x})}\,q^{2 - w(\mathbf{x})}$. Qui $\mathbf{x} = (x_1, x_2)$ e $w(\mathbf{x})$ è il «numero di 1 contenuti nel vettore». L'ultima uguaglianza vale «supponendo che i lanci siano statisticamente indipendenti».

Passaggi e tabella dei quattro casi nella derivazione sopra.

> 🧩 Cosa modella: una sequenza di lanci di una moneta, uno per istante $n$. $X(n) = 1$ se il lancio $n$-esimo dà "successo" (probabilità $p$), 0 altrimenti. Fissato $n$, $X(n)$ è una v.a. di [[variabili-aleatorie-notevoli|Bernoulli]]: il processo è una successione di v.a. di Bernoulli indipendenti. Ha **ampiezza discreta** (solo 0 e 1) e **tempo discreto**, per questo si usa la DF invece di CDF e pdf.

![[random-processes-p10-appunti-processo-bernoulli.png]]
*Appunti a mano: le due DF, con le note in verde «numero di 1 contenuti nel vettore» su $w(\mathbf{x})$ e «supponendo che i lanci siano statisticamente indipendenti» sotto l'uguaglianza. Nella prima riga l'istante è scritto una volta $n$ e una volta $n_1$: è lo stesso.*

### Processi a tempo discreto · [[random_processes.pdf#page=5|p. 5]], [[random_processes.pdf#page=45|p. 45]]

- Finora $X(t; \omega)$ con $t \in \mathbb{R}$: processi **a tempo continuo**. Se il tempo appartiene a $\mathbb{Z}$, il processo è **a tempo discreto** e si scrive $X(n; \omega)$. Gli appunti di p. 5 lo anticipano: $X(n, \omega)$ con $n \in \mathbb{Z}$. Un esempio è il processo di Bernoulli degli appunti di p.10.
- È una successione di variabili aleatorie $\{X(n)\}_{n \in \mathbb{Z}}$, omettendo $\omega$. Con $n \in \{0, 1, \dots, N-1\}$ si riduce a un **vettore aleatorio**.
- CDF, pdf e DF si definiscono come a tempo continuo, sostituendo formalmente $t$ con $n$.
- Media, correlazioni e covarianze: [[momenti-di-un-processo]]. Densità spettrale: [[densita-spettrale-di-potenza]].

> 💡 Connessione (🧩 mia): campionando un processo a tempo continuo negli istanti $nT_c$ si ottiene un processo a tempo discreto, $X(n) = X(nT_c)$. È la versione aleatoria del campionamento di [[teorema-del-campionamento]].

### Processi complessi · [[random_processes.pdf#page=25|p. 25]]

Un processo complesso $Z(t) = X(t) + jY(t)$ si caratterizza completamente con la caratterizzazione **congiunta** delle parti reale e immaginaria. Media e autocorrelazione sono in [[momenti-di-un-processo]].

> 🎯 Esame: definire un processo aleatorio e spiegarne i due punti di vista (forme d'onda contro variabili aleatorie nel tempo); cosa si ottiene fissando $\omega$, $t$ o entrambi, anche sulla sinusoide a fase casuale; caratterizzazione completa e parziale; distribuzioni di ordine $k$ e loro coerenza (marginali); DF del processo di Bernoulli.

## Perché importa

È il modello del corso per i segnali che non si possono prevedere: il rumore termico ([[sistema-comunicazione-digitale]]) e i segnali d'informazione. Tutte le prestazioni di un sistema di comunicazione, come probabilità d'errore e rapporto segnale-rumore, si calcolano modellando rumore e messaggio come processi aleatori.

## Connessioni

- [[variabile-aleatoria]] — fissato $t$, il processo è una variabile aleatoria.
- [[coppie-di-variabili-aleatorie]] — le distribuzioni congiunte di ordine 2 sono quelle di una coppia di v.a.; le marginali danno la coerenza.
- [[momenti-di-un-processo]] — la caratterizzazione parziale.
- [[stazionarieta]] — quando le distribuzioni non dipendono dall'origine dei tempi.
- [[processo-gaussiano]] — il caso in cui media e covarianza bastano per la caratterizzazione completa.
- [[teorema-del-campionamento]] — dal processo a tempo continuo a quello a tempo discreto.
- [[variabili-aleatorie-notevoli]] — fissato $n$, il processo di Bernoulli è una v.a. di Bernoulli; la fase della sinusoide è uniforme.

## Fonti · [[random_processes.pdf#page=2|p. 2]], [[random_processes.pdf#page=11|p. 11]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]]

- [[processi-aleatori]]

_Aggiornato: 2026-09-28 — re-ingest del PDF con appunti: dal segnale deterministico al processo (p.3), particolarizzazioni e sinusoide a fase casuale (p.4–5), CDF del primo e secondo ordine (p.8), marginale della pdf e correzione $\partial^k$ (p.9), DF del processo di Bernoulli con derivazione (p.10). Prima, nello stesso giorno: creazione da ingest random_processes.pdf_
