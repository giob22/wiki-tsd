---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria", "coppie-di-variabili-aleatorie", "spazio-di-probabilita"]
fonti_pdf: ["random_processes.pdf#page=2", "random_processes.pdf#page=3", "random_processes.pdf#page=4", "random_processes.pdf#page=5", "random_processes.pdf#page=6", "random_processes.pdf#page=40"]
---

# Processo aleatorio (processo stocastico)

## Definizione

> 📄 Fonte: [[random_processes.pdf#page=2]], [[random_processes.pdf#page=3]], [[random_processes.pdf#page=4]]

Un **processo stocastico**, detto anche processo aleatorio o **segnale aleatorio** (*random signal*), è l'estensione naturale del concetto di [[variabile-aleatoria]] quando si ha a che fare con **segnali**. Si scrive $X(t, \omega)$, dove $t$ è il tempo e $\omega$ l'esito di un esperimento aleatorio ([[random_processes.pdf#page=2]]).

**Perché serve.** In molte situazioni l'ipotesi che un segnale sia deterministico non regge, e conviene modellarlo come **funzione aleatoria**. Due esempi della slide:
- il **rumore termico** nei circuiti elettronici;
- i segnali generati da una **sorgente d'informazione**.

**Due modi di vederlo** ([[random_processes.pdf#page=3]]):
1. **Collezione di forme d'onda.** A ogni esito $\omega = \omega_i$ dello spazio di probabilità $(\Omega, S, P)$ corrisponde un segnale deterministico $X(t, \omega_i) \equiv x_i(t)$, detto **realizzazione** (*sample function*). È un'idea simile a quella di variabile aleatoria.
   - Fissando un istante $t_0$, la funzione $X(t_0, \omega)$ è una **variabile aleatoria**.
   - Fissando sia $t_0$ sia $\omega_i$, $X(t_0, \omega_i)$ è un **numero**.
2. **Collezione di variabili aleatorie indicizzate dal tempo**, il punto di vista più adatto allo sviluppo matematico della teoria:
   - se l'insieme degli indici è $\mathbb{R}$, il processo è **a tempo continuo**;
   - se è $\mathbb{Z}$, il processo è **a tempo discreto**: una successione di variabili aleatorie $\{X_i\}_{i=-\infty}^{+\infty}$.

Per semplicità si omette $\omega$ e si scrive $X(t)$, oppure $x(t)$ quando non c'è ambiguità.

> 📄 Osservazione della slide ([[random_processes.pdf#page=4]]): in una **variabile aleatoria** l'esito dell'esperimento viene associato a un **numero**; in un **processo aleatorio** viene associato a una **forma d'onda**, funzione del tempo.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $X(t, \omega)$, con $X(t, \omega_i) \equiv x_i(t)$ | processo e sue realizzazioni | [[random_processes.pdf#page=3]] |
| $F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \triangleq P[X(t_1) \le x_1, \dots, X(t_k) \le x_k]$ | CDF congiunta di ordine $k$, eq. (1) | [[random_processes.pdf#page=5]] |
| $f_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \triangleq \dfrac{\partial^k}{\partial x_1 \cdots \partial x_k}F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k)$ | pdf congiunta di ordine $k$, eq. (2) | [[random_processes.pdf#page=5]] |
| $X(n; \omega)$, $n \in \mathbb{Z}$ | processo a tempo discreto | [[random_processes.pdf#page=40]] |

Simboli: $t$ = tempo [s]; $\omega$ = esito, elemento dello spazio campione $\Omega$; $(x_1,\dots,x_k) \in \mathbb{R}^k$ = valori (nell'unità del segnale, es. V); $F$ adimensionale (è una probabilità); $f$ in [1/V$^k$].

> ⚠️ Refusi della slide ([[random_processes.pdf#page=5]]): la derivata nella (2) è scritta $\partial^n$, ma le variabili sono $k$, quindi $\partial^k$. Più sotto la slide rimanda alla «CDF congiunta (36)» invece che alla (1).

## Derivazioni

### Derivazione — Coerenza delle distribuzioni: quelle di ordine basso sono marginali
**Fonte:** [[random_processes.pdf#page=6]]: le CDF e pdf di ordine più basso si devono ottenere come marginali di quelle di ordine più alto.
> 🧩 Derivazione mia per $k = 2$ (per $k$ qualunque è identica), con le regole delle marginali di [[coppie-di-variabili-aleatorie]].

$$
\begin{aligned}
F_{X(t_1)}(x_1) &= P[X(t_1) \le x_1] = P[X(t_1) \le x_1,\ X(t_2) \le +\infty] && \{X(t_2) \le +\infty\} \text{ è l'evento certo} \\
&= F_{X(t_1),X(t_2)}(x_1, +\infty) && \text{definizione (1)} \\
f_{X(t_1)}(x_1) &= \int_{-\infty}^{+\infty} f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_2 && \text{marginale della pdf: integro via } x_2
\end{aligned}
$$

"Coerenti" vuol dire che le famiglie di CDF (o pdf) non si possono scegliere a caso ordine per ordine: quelle di ordine più alto determinano quelle di ordine più basso.

## Spiegazione

### Esempio della slide: un rettangolo di segno casuale
> 📄 Fonte: [[random_processes.pdf#page=2]]

$\Omega = \{0, 1\}$ con $P(\{\omega = 1\}) \triangleq p$ e $P(\{\omega = 0\}) \triangleq q = 1 - p$. Il segnale aleatorio è
$$
X(t, \omega) = \begin{cases} A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 0 \\[2mm] -A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 1 \end{cases}
$$

![[random-processes-p2-esempio-rect.png]]
*[[random_processes.pdf#page=2]]: le due realizzazioni. $x(t, \omega = 0)$ vale $A$ per $0 < t < T$; $x(t, \omega = 1)$ vale $-A$ nello stesso intervallo. Fuori da $(0, T)$ entrambe valgono 0.*

> 🧩 Le due facce sull'esempio (lettura mia):
> - **come forme d'onda**: ci sono due sole realizzazioni possibili, i due rettangoli della figura;
> - **fissato un istante $t_0 \in (0, T)$**: $X(t_0)$ è una variabile aleatoria **discreta** che vale $A$ con probabilità $q$ e $-A$ con probabilità $p$, del tipo di [[variabili-aleatorie-notevoli|Bernoulli]] a meno di una trasformazione affine;
> - **fissato $t_0$ fuori da $(0, T)$**: $X(t_0) = 0$ con certezza.
>
> Media, autocorrelazione e covarianza di questo processo sono calcolate in [[momenti-di-un-processo]]: la media dipende da $t$.

### Il quadro generale: esiti, realizzazioni, variabili aleatorie
> 📄 Fonte: [[random_processes.pdf#page=4]]

![[random-processes-p4-realizzazioni.png]]
*[[random_processes.pdf#page=4]]. Lo spazio campione $S$ contiene gli esiti $s_1, s_2, \dots, s_n$. Ogni esito, cioè ogni prova dell'esperimento, produce una forma d'onda $x_1(t), x_2(t), \dots, x_n(t)$ sull'intervallo $(-T, +T)$. Una linea verticale all'istante $t_k$ taglia tutte le forme d'onda nei valori $x_1(t_k), x_2(t_k), \dots, x_n(t_k)$: al variare dell'esito, sono i valori della variabile aleatoria $X(t_k)$.*

![[grafico-rp-realizzazioni.png]]
*🧩 Grafico mio (definizioni di [[random_processes.pdf#page=3]]; script in `output/grafici/`). Processo gaussiano a media nulla con autocorrelazione $e^{-|\tau|/\tau_c}$, $\tau_c = 0.5$. A sinistra cinque realizzazioni: fissato $t_0 = 6$, ognuna dà un numero (punto arancio). A destra i valori $X(t_0)$ di 5000 realizzazioni: il loro istogramma riproduce la pdf gaussiana $\mathcal{N}(0, 1)$. È la variabile aleatoria che si ottiene fissando il tempo.*

### Caratterizzazione statistica completa
> 📄 Fonte: [[random_processes.pdf#page=5]], [[random_processes.pdf#page=6]]

- La descrizione statistica di un processo si basa sulla CDF (o, in modo equivalente, sulla pdf) di **vettori di campioni** del segnale aleatorio.
- $X(t_1), \dots, X(t_k)$ sono le variabili aleatorie ottenute campionando $X(t)$ negli istanti $t_1, \dots, t_k$. La loro CDF congiunta è la (1) e la pdf congiunta la (2).
- Se si conosce la (1), o la (2), per **qualunque scelta** degli istanti $t_1, \dots, t_k$, si conosce la **caratterizzazione statistica di ordine $k$**.
- Il processo è **completamente caratterizzato** se si conosce la CDF (o pdf) congiunta di ordine $k$ per **ogni** $k \in \mathbb{N}$ e ogni scelta degli istanti.
- CDF e pdf devono essere **coerenti**: quelle di ordine più basso si ottengono come marginali di quelle di ordine più alto (derivazione sopra).
- Finora si è supposta l'ampiezza **continua**. Se l'ampiezza di $X(t)$ è **discreta** conviene usare la distribuzione di probabilità (DF, vedi [[variabile-aleatoria]]), per esempio nel processo di Bernoulli.
- La caratterizzazione completa è difficile da ottenere in molti casi pratici. Ci si accontenta allora di una **caratterizzazione parziale**, cioè media e autocorrelazione: [[momenti-di-un-processo]].

> 🧩 Perché "difficile": servono infinite funzioni (tutte le pdf di ogni ordine $k$, per ogni scelta di istanti), mentre media e autocorrelazione sono solo due funzioni, di una e di due variabili.

### Processi a tempo discreto
> 📄 Fonte: [[random_processes.pdf#page=40]]

- Finora $X(t; \omega)$ con $t \in \mathbb{R}$: processi **a tempo continuo**. Se il tempo appartiene a $\mathbb{Z}$, il processo è **a tempo discreto** e si scrive $X(n; \omega)$.
- È una successione di variabili aleatorie $\{X(n)\}_{n \in \mathbb{Z}}$, omettendo $\omega$. Con $n \in \{0, 1, \dots, N-1\}$ si riduce a un **vettore aleatorio**.
- CDF, pdf e DF si definiscono come a tempo continuo, sostituendo formalmente $t$ con $n$.
- Media, correlazioni e covarianze: [[momenti-di-un-processo]]. Densità spettrale: [[densita-spettrale-di-potenza]].

> 💡 Connessione (🧩 mia): campionando un processo a tempo continuo negli istanti $nT_c$ si ottiene un processo a tempo discreto, $X(n) = X(nT_c)$. È la versione aleatoria del campionamento di [[teorema-del-campionamento]].

### Processi complessi
> 📄 Fonte: [[random_processes.pdf#page=20]]

Un processo complesso $Z(t) = X(t) + jY(t)$ si caratterizza completamente con la caratterizzazione **congiunta** delle parti reale e immaginaria. Media e autocorrelazione sono in [[momenti-di-un-processo]].

> 🎯 Esame: definire un processo aleatorio e spiegarne i due punti di vista (forme d'onda contro variabili aleatorie nel tempo); caratterizzazione completa e parziale; distribuzioni di ordine $k$ e loro coerenza.

## Perché importa

È il modello del corso per i segnali che non si possono prevedere: il rumore termico ([[sistema-comunicazione-digitale]]) e i segnali d'informazione. Tutte le prestazioni di un sistema di comunicazione, come probabilità d'errore e rapporto segnale-rumore, si calcolano modellando rumore e messaggio come processi aleatori.

## Connessioni

- [[variabile-aleatoria]] — fissato $t$, il processo è una variabile aleatoria.
- [[coppie-di-variabili-aleatorie]] — le distribuzioni congiunte di ordine 2 sono quelle di una coppia di v.a.; le marginali danno la coerenza.
- [[momenti-di-un-processo]] — la caratterizzazione parziale.
- [[stazionarieta]] — quando le distribuzioni non dipendono dall'origine dei tempi.
- [[processo-gaussiano]] — il caso in cui media e covarianza bastano per la caratterizzazione completa.
- [[teorema-del-campionamento]] — dal processo a tempo continuo a quello a tempo discreto.

## Fonti

- [[processi-aleatori]]
- [[random_processes.pdf#page=2]] – [[random_processes.pdf#page=6]], [[random_processes.pdf#page=20]], [[random_processes.pdf#page=40]]

_Aggiornato: 2026-09-28 — creazione da ingest random_processes.pdf_
