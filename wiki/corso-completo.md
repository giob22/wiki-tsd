# Trasmissione dei Segnali Digitali — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, D. Darsena; testo Madhow, *Fundamentals of Digital Communication*; esame orale). Contiene **solo ciò che sta nei PDF del corso**, nell'ordine delle slide: definizioni, formule, esempi, figure e le dimostrazioni svolte a mano dalla docente. I passaggi che le slide saltano sono ricostruiti in una riga dove servono a seguire il discorso; le derivazioni estese, i grafici aggiuntivi, gli esercizi e le animazioni stanno nelle pagine concetto, esercizio e laboratorio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Le equazioni numerate (1)–(25) sono quelle delle slide della Lezione 4. Il PDF di una lezione si genera con `python output/crea_pdf.py N` (file in `output/pdf/`).

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 1 | [[#Lezione 1 — Introduzione al corso|Introduzione al corso]] | Intro.pdf |
| 2 | [[#Lezione 2 — Elementi di teoria della probabilità|Elementi di teoria della probabilità]] | Probabilità.pdf |
| 3 | [[#Lezione 3 — Campionamento e conversione A/D e D/A|Campionamento e conversione A/D e D/A]] | Campionamento_AD_DA.pdf |
| 4 | [[#Lezione 4 — Rappresentazione complessa in banda base|Rappresentazione complessa in banda base]] | Rappresentazione_Rice.pdf |
| 5 | [[#Lezione 5 — Processi aleatori|Processi aleatori]] | random_processes.pdf (+ random_processes_v2.pdf) |
| 6 | [[#Lezione 6 — Laboratorio Matlab: conversione A/D e D/A (28/09)|Laboratorio Matlab: conversione A/D e D/A]] | AD_conversion.m + figure |



## Lezione 1 — Introduzione al corso

*Fonte: Intro.pdf (21 pagine, slide). Materiale qualitativo, senza formule.*

### Organizzazione e programma · [[Intro.pdf#page=2|p. 2]], [[Intro.pdf#page=3|3]]

- Docente: Donatella Darsena (DIETI, UNINA); LM Ingegneria Informatica, a.a. 2026-27.
- Testo: U. Madhow, *Fundamentals of Digital Communication*, Cambridge, 2008 (altri testi per alcuni argomenti), più gli appunti delle lezioni. Lezioni con slide e lavagna.
- Esame: **colloquio orale**.
- Argomenti del corso:
  1. rappresentazione complessa in banda base dei segnali;
  2. processi aleatori;
  3. modulazione digitale dei segnali;
  4. stima dei parametri e sincronizzazione;
  5. comunicazione digitale su canali selettivi in frequenza;
  6. elementi di teoria dell'informazione e codifica di canale.

### Comunicazione e processo di comunicazione · [[Intro.pdf#page=4|p. 4]]–[[Intro.pdf#page=6|6]]

- **Comunicazione** = trasferimento di informazione (voce, audio, video, file, pagine web...) tra punti diversi dello **spazio** o del **tempo** (memorizzazione).
- Il processo di comunicazione comporta:
  1. generazione di un segnale messaggio (voce, musica, immagine, dati);
  2. sua descrizione, con una certa precisione, mediante un insieme di simboli (elettrici, sonori, visivi);
  3. codifica dei simboli in forma adatta a un mezzo fisico;
  4. trasmissione dei simboli codificati alla destinazione;
  5. decodifica e riproduzione dei simboli originali;
  6. ricostruzione del messaggio con una degradazione definibile, dovuta a imperfezioni inevitabili.
- Anche nelle comunicazioni tra computer la decisione umana interviene solo nell'impostazione dei programmi o nel controllo dei risultati.
- Ogni sistema ha tre elementi base: **trasmettitore**, **canale**, **ricevitore**. La cascata trasmettitore + ricevitore è detta **transceiver**.

### Elementi di un sistema di comunicazione · [[Intro.pdf#page=7|p. 7]]–[[Intro.pdf#page=9|9]]

![[intro-p7-elementi-sistema-comunicazione.png|420]]
*Sorgente → trasmettitore → canale → ricevitore → utente.*

- **Trasmissione:** il trasmettitore è in un punto, il ricevitore in un altro, il canale è il mezzo fisico che li collega. Il trasmettitore converte il segnale messaggio della sorgente in una forma adatta al canale.
- **Ricezione:** propagandosi, il segnale si distorce per le imperfezioni del canale; all'uscita si sommano **rumore** e **interferenze** (da altre sorgenti): il segnale ricevuto è una versione corrotta del trasmesso. Il ricevitore ricostruisce una forma riconoscibile del messaggio per l'utente.
- Il processo di comunicazione, in ogni sistema, è di natura **statistica**.

### Comunicazione digitale e rigenerazione · [[Intro.pdf#page=10|p. 10]]–[[Intro.pdf#page=13|13]]

- **Digitale:** l'informazione è rappresentata in forma digitale (di solito cifre binarie, bit). **Analogica:** l'informazione assume un continuo di valori.
- Perché si passa al digitale: il vantaggio primario è la facilità di **rigenerare** i segnali digitali; con rivelazione e correzione d'errore si hanno probabilità d'errore bassissime e alta fedeltà (procedure non disponibili per l'analogico).

![[intro-p11-degradazione-impulso.png|420]]
*Impulso binario ideale lungo una linea: degradazione crescente con la distanza (1→4) e rigenerazione (5).*

- La forma d'onda è alterata da due meccanismi: (i) linee e circuiti hanno una funzione di trasferimento non ideale (distorsione); (ii) rumore elettrico e altre interferenze. Entrambi degradano l'impulso con la lunghezza della linea.
- Finché l'impulso è ancora identificabile con affidabilità (prima di diventare ambiguo), un amplificatore digitale ne recupera la forma ideale: l'impulso «rinasce». I circuiti che lo fanno a intervalli regolari sono i **ripetitori rigenerativi**.
- Altri vantaggi: circuiti digitali più affidabili ed economici; hardware più flessibile (microprocessori, commutazione digitale, LSI); *a bit is a bit* (dati, telegrafo, telefono, TV trattati come segnali identici in trasmissione e commutazione); messaggi gestiti a **pacchetti**; elaborazioni contro interferenza e jamming, crittografia e privacy; molta comunicazione è tra computer, terminazioni digitali.

### Schema di un sistema di comunicazione digitale · [[Intro.pdf#page=14|p. 14]]–[[Intro.pdf#page=20|20]]

![[intro-p14-schema-sistema-digitale.png|560]]

| Blocco | Funzione (slide) |
|---|---|
| **Codificatore di sorgente** (p. 15) | Ogni informazione si rappresenta in modo efficiente in forma digitale con precisione arbitraria, con un numero di bit che dipende dalla fedeltà richiesta. Realizza la conversione A/D (sorgenti analogiche) e riduce la ridondanza tenendo conto dell'utente finale. Bit rate: voce 64 kbit/s (telefonia cablata), MP3 consumer 128 kbit/s tipici, audio da studio circa 10 volte di più |
| **Codificatore di canale** (p. 16) | Introduce ridondanza **controllata** contro errori dovuti a imperfezioni e rumore del canale; l'uscita è una *parola di codice* progettata sul canale e sui requisiti dei livelli di rete superiori: rivelazione d'errore + ritrasmissione per applicazioni insensibili al ritardo, correzione d'errore per applicazioni real-time |
| **Modulatore** (p. 16) | Traduce simboli di messaggio o di canale (se c'è codifica di canale) in forme d'onda analogiche trasmissibili sul canale fisico |
| **Canale** (p. 17) | Distorce la forma d'onda in modo diverso a seconda dei casi: cablato → sistema LTI descritto dalla risposta impulsiva; wireless mobile → variabile per la mobilità relativa TX-RX; il wireless è un mezzo broadcast, quindi può esserci interferenza di accesso multiplo |
| **Rumore termico** (p. 18) | Alla ricezione il segnale è corrotto dal rumore termico dei componenti. Un elemento con due terminali ha resistenza $R$ (Ω); contiene elettroni liberi in moto casuale se la temperatura è sopra lo zero assoluto, il che genera una tensione di rumore ai terminali. È piccolo, ma diventa un problema se amplificato da un ricevitore ad alto guadagno. Si caratterizza con la meccanica quantistica |
| **Demodulatore** (p. 19) | Elabora la forma d'onda ricevuta (distorta e rumorosa). Compito chiave: **sincronizzazione** (il canale produce sfasamenti di fase, frequenza e tempo; clock e oscillatori di TX e RX non sono sincronizzati a priori). Può fare anche equalizzazione di canale. Obiettivo finale: produrre **decisioni** sui simboli trasmessi (detection) per il decodificatore di canale |
| **Decodificatore di canale** (p. 19) | Sfrutta la ridondanza inserita in trasmissione per stimare i simboli di informazione in ingresso al codificatore di canale |
| **Decodificatore di sorgente** (p. 20) | Converte i bit stimati in un formato utilizzabile dall'utente, non necessariamente quello originale (esempio: la voce tradotta in testo, codificata in bit; il decodificatore mostra il testo invece di riprodurre la voce) |

### Vantaggi dell'approccio digitale e separazione · [[Intro.pdf#page=21|p. 21]]

- **Progetto indipendente dalla sorgente:** trasformata l'informazione in bit, la si memorizza o trasmette senza interpretarla; il mezzo non dipende dalla sorgente e sorgenti diverse condividono lo stesso mezzo.
- **Progetto ottimizzato per il canale:** per ogni collegamento si ottimizzano codifica di canale e modulazione per quel canale. Poiché i bit sono rigenerati a ogni tratta, non c'è accumulo di rumore.
- Osservazioni: (1) lo schema si basa sulla **separazione tra codifica di sorgente e di canale**, che dà vantaggi pratici ed è ottima per collegamenti punto-punto (teoria dell'informazione); in certi casi la codifica congiunta dà prestazioni migliori. (2) Le **comunicazioni semantiche** sono un tema emergente: invece di recuperare accuratamente la sequenza di bit, si trasmette il significato della sorgente; la codifica semantica estrae le caratteristiche utili ai compiti da eseguire al ricevitore.

*Approfondimenti nel wiki: [[sistema-comunicazione-digitale]], [[ripetitore-rigenerativo]], [[conversione-ad-da]].*


## Lezione 2 — Elementi di teoria della probabilità

*Fonte: Probabilità.pdf (38 slide). Simboli: $\bar A$ = complementare di $A$ (sulle slide è scritto con la sopralineatura), $AB = A\cap B$.*

### Definizioni preliminari · [[Probabilità.pdf#page=2|p. 2]]

- **Esperimento aleatorio:** procedura con un insieme ben definito di risultati, il cui esito non è prevedibile a priori (lancio di moneta o dado, estrazione di una carta, lotto, roulette). Il risultato è indicato con $\omega$.
- **Spazio campione** $\Omega$: insieme di tutti i possibili risultati. Moneta: $\Omega = \{T, C\}$; dado: $\Omega = \{1, \dots, 6\}$; arrivo di un cliente a uno sportello tra le 9:00 e le 12:00: $\Omega = [0, 10800]$ s.
- **Evento:** un qualunque sottoinsieme $A \subseteq \Omega$.

### Prova e significato degli eventi · [[Probabilità.pdf#page=3|p. 3]], [[Probabilità.pdf#page=4|4]]

**Prova** = singola ripetizione dell'esperimento, restituisce un risultato $\omega\in\Omega$.

| Si verifica | $\iff$ |
|---|---|
| $A$ | $\omega\in A$ |
| non $A$ ($\bar A$, complementare) | $\omega\notin A$ |
| $A$ o $B$ | $\omega\in A\cup B$ |
| $A$ e $B$ | $\omega\in A\cap B$ |

Eventi particolari: **certo** $A=\Omega$ (si verifica sempre); **impossibile** $A=\varnothing$ (mai); **elementare** $A=\{\omega\}$ (un solo risultato); **mutuamente esclusivi** $A\cap B=\varnothing$ (non possono verificarsi insieme).

*Esempio 1.4 (dado, prova $\omega=4$):* $A=\{\text{pari}\}$ si verifica; $B=\{\ge 3\}$ si verifica; $C=\{<2\}$ non si verifica; «$A$ e $B$» si verifica; «$A$ o $C$» si verifica; «$A$ e $C$» no.

### Spazio degli eventi e probabilità · [[Probabilità.pdf#page=5|p. 5]]

- **Spazio degli eventi** $S$: collezione di eventi che contiene tutti quelli di interesse (in molti casi, tutti i sottoinsiemi, compresi $\Omega$ e $\varnothing$).
- **Probabilità:** legge $P: A\in S \mapsto P(A)\in[0,1]$, misura del «grado di incertezza» sul verificarsi di $A$. Deve soddisfare gli **assiomi di Kolmogorov**:
  - I. $P(A)\ge 0$ (non negatività);
  - II. $P(\Omega)=1$ (normalizzazione);
  - III. per eventi mutuamente esclusivi $\{A_n\}_{n=1}^{\infty}$ ($A_i\cap A_j=\varnothing$, $\forall i\ne j$): $P\big(\bigcup_n A_n\big)=\sum_n P(A_n)$ (numerabile additività).
- La tripla $(\Omega, S, P)$ è lo **spazio di probabilità**.

### Proprietà elementari · [[Probabilità.pdf#page=6|p. 6]]

Dimostrabili dagli assiomi:
1. $P(\varnothing)=0$;
2. $A\cap B=\varnothing \Rightarrow P(A\cup B)=P(A)+P(B)$ (finita additività);
3. $P(\bar A)=1-P(A)$;
4. $P(A\cup B)=P(A)+P(B)-P(A\cap B)$;
5. $P(A\cup B)\le P(A)+P(B)$ (disuguaglianza di Boole);
6. $B\subseteq A\Rightarrow P(B)\le P(A)$;
7. $P(B)\le 1$.

### Probabilità condizionale · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=8|8]]

Dati $A$, $B$ con $P(B)\ne 0$:

$$P(A\mid B)\triangleq\frac{P(AB)}{P(B)}\qquad\text{«probabilità di }A\text{ dato }B\text{»}$$

- È un «raffinamento» di $P(A)$: tiene conto dell'informazione che $B$ si è verificato. *Esempio 2.2:* $A=\{\text{piove}\}$, $B=\{\text{estate}\}\Rightarrow P(A\mid B)<P(A)$; con $B=\{\text{inverno}\}\Rightarrow P(A\mid B)>P(A)$.
- $P(A\mid B)>P(A)$: $A$ è «attratto» da $B$; $<$: «respinto»; $=$: «indifferente» (indipendenza).
- **Dipende dall'ordine:** $P(A\mid B)=P(AB)/P(B)\ne P(B\mid A)=P(BA)/P(A)$ in generale (denominatori diversi). Es.: $B\subseteq A$ (B implica A) $\Rightarrow P(A\mid B)=1$ e $P(B\mid A)\ge P(B)$.
- Fissato $B\subseteq\Omega$, $P(\cdot\mid B)$ si interpreta come (1) una nuova legge di probabilità sullo stesso $\Omega$, o (2) una legge sul nuovo spazio campione $\Omega_B=B$ (restrizione della legge originale a $B$): in entrambi i casi gli assiomi di Kolmogorov sono soddisfatti.

### Legge della probabilità composta · [[Probabilità.pdf#page=9|p. 9]]

$$P(AB)=P(A\mid B)\,P(B)=P(B\mid A)\,P(A)$$

Scompone il calcolo della probabilità congiunta in più passi. Matematicamente l'ordine è ininfluente; in pratica conviene condizionare all'evento che si verifica «prima» (logicamente o cronologicamente).

*Esempio 2.3 (due palle da una scatola con 3 bianche e 2 rosse):* soluzione combinatoria vs condizionale. Per due bianche: $P(B_1B_2)=P(B_2\mid B_1)P(B_1)=\frac24\cdot\frac35=\frac{3}{10}$; combinatoria: $\binom32/\binom52=3/10$.

### Regola della catena · [[Probabilità.pdf#page=10|p. 10]]

$P(A\mid B,C)\triangleq P(ABC)/P(BC)$, con $P(BC)\ne0$ (l'evento condizionante è $B\cap C$). Applicando la probabilità composta a $P(BC)$:

$$P(ABC)=P(C)\,P(B\mid C)\,P(A\mid B,C)\qquad(\text{ordine logico }C\to B\to A)$$

Scegliendo $A\to B\to C$: $P(ABC)=P(A)P(B\mid A)P(C\mid A,B)$. Esistono $3!=6$ modi di scrivere $P(ABC)$. In generale:

$$P(A_1A_2\cdots A_n)=P(A_1)\,P(A_2\mid A_1)\,P(A_3\mid A_1,A_2)\cdots P(A_n\mid A_1,\dots,A_{n-1})$$

scrivibile in $n!$ modi (permutazioni degli eventi).

### Indipendenza tra eventi · [[Probabilità.pdf#page=11|p. 11]], [[Probabilità.pdf#page=12|12]]

- La condizione di «indifferenza» $P(A\mid B)=P(A)$ si chiama **indipendenza statistica**: sapere che $B$ è avvenuto non dà informazione su $A$. Implica $P(B\mid A)=P(B)$: proprietà simmetrica.
- $A$ e $B$ sono indipendenti se $P(AB)=P(A)P(B)$ (la congiunta si fattorizza nel prodotto delle marginali). **Non confondere** indipendenti con mutuamente esclusivi. *Esempio 2.6:* due lanci di moneta.
- **Tre eventi** $A,B,C$ sono indipendenti se (1) vale l'indipendenza a coppie, $P(AB)=P(A)P(B)$, $P(BC)=P(B)P(C)$, $P(AC)=P(A)P(C)$, **e** (2) $P(ABC)=P(A)P(B)P(C)$. Non basta la sola seconda fattorizzazione. Equivale a dire che in tutte le probabilità condizionali tra tre eventi il condizionamento non opera: $P(A\mid B,C)=P(A)$, ..., $P(AB\mid C)=P(AB)$, ...
- $A_1,\dots,A_n$ sono indipendenti se $P\big(\bigcap_{i\in I}A_i\big)=\prod_{i\in I}P(A_i)$ per ogni insieme $I\subseteq\{1,\dots,n\}$ di indici distinti.

### Teorema della probabilità totale · [[Probabilità.pdf#page=13|p. 13]]

![[probabilita-p13-probabilita-totale.png|300]]

Si vuole $P(B)$ note le probabilità a priori delle cause $P(A_i)$ e le condizionali $P(B\mid A_i)$. Con $A_1,\dots,A_n$ mutuamente esclusivi e $B\subseteq\bigcup_iA_i$:

$$P(B)=\sum_{i=1}^{n}P(B\mid A_i)\,P(A_i)$$

Le cause sono mutuamente esclusive: se si verifica l'effetto, si verifica una (e una sola) causa. Verificare logicamente $B\subseteq\bigcup A_i$ può essere complicato: più facile scegliere $\bigcup A_i=\Omega$ (partizione di $\Omega$).

### Teorema di Bayes · [[Probabilità.pdf#page=14|p. 14]]

![[probabilita-p14-bayes.png|300]]

Noto che si è verificato $B$ (effetto), si calcolano le probabilità a posteriori delle cause (**inferenza bayesiana**). Stesse ipotesi della probabilità totale:

$$P(A_i\mid B)=\frac{P(B\mid A_i)P(A_i)}{\sum_{j=1}^{n}P(B\mid A_j)P(A_j)}=\frac{P(B\mid A_i)P(A_i)}{P(B)}$$

### Variabile aleatoria · [[Probabilità.pdf#page=15|p. 15]]

Descrive numericamente i risultati di un esperimento aleatorio. Sia $\Omega$ lo spazio campione (discreto o continuo) con legge $P(\cdot)$. Una **variabile aleatoria (v.a.)** è una funzione definita su $\Omega$ a valori in $\bar{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$:

$$X:\omega\in\Omega\to X(\omega)\in\bar{\mathbb R}$$

![[probabilita-p15-variabile-aleatoria.png|420]]

### CDF · [[Probabilità.pdf#page=16|p. 16]], [[Probabilità.pdf#page=17|17]]

$$F_X(x)\triangleq P(X\le x)\qquad\forall x\in\mathbb R$$

Proprietà:
1. $F(+\infty)=1$, $F(-\infty)=0$;
2. monotona crescente (non strettamente): $x_1<x_2\Rightarrow F(x_1)\le F(x_2)$;
3. $P(X>x)=1-F(x)$ (CDF complementare o funzione di affidabilità);
4. continua da destra: $F(x^+)=F(x)$;
5. $P(x_1<X\le x_2)=F(x_2)-F(x_1)$;
6. $P(X=x)=F(x)-F(x^-)$.

**Tipi di v.a.:** *discreta* → CDF costante a tratti, $F(x)=\sum_ip_i\,u(x-x_i)$; *continua* → CDF continua (quindi $P(X=x)=0$ ovunque); *mista* → CDF discontinua ma non costante a tratti.

### pdf · [[Probabilità.pdf#page=18|p. 18]]

$$f_X(x)\triangleq\frac{d}{dx}F_X(x)\qquad\forall x\in\mathbb R$$

Per $X$ continua la pdf non contiene impulsi; per $X$ discreta $f(x)=\sum_ip_i\,\delta(x-x_i)$ (derivata in senso generalizzato). Proprietà:
1. $f(x)\ge0$;
2. $F(x)=\int_{-\infty}^{x}f(y)\,dy$;
3. $\int_{-\infty}^{+\infty}f(x)\,dx=1$;
4. $P(x_1<X\le x_2)=F(x_2)-F(x_1)=\int_{x_1}^{x_2}f(x)\,dx$ (attenzione se la pdf ha impulsi in $x_1$ e/o $x_2$);
5. $P(x\le X\le x+\Delta x)\approx f(x)\Delta x$, cioè $f(x)=\lim_{\Delta x\to0}\frac{P(x\le X\le x+\Delta x)}{\Delta x}$.

### DF (pmf) · [[Probabilità.pdf#page=19|p. 19]]

$$p_X(x)\triangleq P(X=x)\qquad\forall x\in\mathbb R$$

Utile solo per v.a. discrete (è nulla fuori dagli $x_i$); detta anche funzione «massa» di probabilità. Proprietà: $p(x)\ge0$; $F(x)=\sum_{u\le x}p(u)$; $\sum_up(u)=1$; $P(x_1<X\le x_2)=\sum_{x_1<u\le x_2}p(u)$.

### Variabili aleatorie notevoli · [[Probabilità.pdf#page=20|p. 20]]–[[Probabilità.pdf#page=26|26]]

**Bernoulli** $X\sim\text{Bern}(p)$ (discreta, valori $\{0,1\}$; simile all'indicatrice di un evento). $X=1$ con probabilità $p$ («successo»), $X=0$ con $q=1-p$ («insuccesso»), $p+q=1$:

$$p(x)=\begin{cases}q&x=0\\p&x=1\end{cases}\qquad F(x)=q\,u(x)+p\,u(x-1)\qquad f(x)=q\,\delta(x)+p\,\delta(x-1)$$

![[probabilita-p20-bernoulli.png|360]]

**Binomiale** $X\sim B(n,p)$ (discreta): conteggio del numero di «successi» su $n$ prove ripetute, valori $\{0,\dots,n\}$:

$$p(k)=P(X=k)=\binom nk p^kq^{n-k},\quad k\in\{0,\dots,n\},\ p+q=1$$

CDF e pdf: $F(x)=\sum_{k}p(k)\,u(x-k)$, $f(x)=\sum_kp(k)\,\delta(x-k)$. Normalizzazione dalla potenza di un binomio: $1=(p+q)^n=\sum_{k=0}^n\binom nk p^kq^{n-k}$. La Bernoulli è il caso $n=1$.

**Uniforme** $X\sim U(a,b)$ (continua), fenomeno in un intervallo limitato senza preferenza per i valori:

$$f(x)=\begin{cases}\frac1{b-a}&x\in(a,b)\\0&\text{altrimenti}\end{cases}\qquad F(x)=\begin{cases}0&x<a\\\frac{x-a}{b-a}&a\le x<b\\1&x\ge b\end{cases}$$

Esempio: un bus arriva a caso tra le 10:00 e le 10:15 $\Rightarrow X\sim U(0,900)$ s.

![[probabilita-p22-uniforme.png|360]]

**Gaussiana (normale)** $X\sim N(\mu,\sigma)$ (continua), curva a campana:

$$f(x)=\frac1{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$\mu\in\mathbb R$ è il «baricentro», $\sigma>0$ la «larghezza». Per la normalizzazione si usa $\int_{-\infty}^{+\infty}e^{-x^2}dx=\sqrt\pi$. Descrive fenomeni che sono somma di molti contributi indipendenti (**teorema centrale del limite, CLT**).

![[probabilita-p23-gaussiana.png|360]]

**CDF della gaussiana** — non in forma chiusa:

$$F(x)=\frac1{\sqrt{2\pi}\sigma}\int_{-\infty}^{x}e^{-(t-\mu)^2/(2\sigma^2)}dt$$

$$\text{erf}(x)\triangleq\frac2{\sqrt\pi}\int_0^xe^{-t^2}dt,\qquad\text{erfc}(x)\triangleq\frac2{\sqrt\pi}\int_x^{+\infty}e^{-t^2}dt=1-\text{erf}(x)$$

$$F(x)=1-\tfrac12\,\text{erfc}\Big(\frac{x-\mu}{\sqrt2\,\sigma}\Big)=\tfrac12\Big[1+\text{erf}\Big(\frac{x-\mu}{\sqrt2\,\sigma}\Big)\Big]$$

Da cui (p. 25):

$$
\begin{aligned}
P(X<x)&=\tfrac12\Big[1+\text{erf}\Big(\tfrac{x-\mu}{\sqrt2\sigma}\Big)\Big]=\tfrac12\,\text{erfc}\Big(\tfrac{\mu-x}{\sqrt2\sigma}\Big)\\
P(X>x)&=\tfrac12\,\text{erfc}\Big(\tfrac{x-\mu}{\sqrt2\sigma}\Big)\\
P(\lvert X\rvert<x)&=\tfrac12\Big[\text{erf}\Big(\tfrac{x-\mu}{\sqrt2\sigma}\Big)+\text{erf}\Big(\tfrac{x+\mu}{\sqrt2\sigma}\Big)\Big]\\
P(\lvert X\rvert>x)&=\tfrac12\Big[\text{erfc}\Big(\tfrac{x-\mu}{\sqrt2\sigma}\Big)+\text{erfc}\Big(\tfrac{x+\mu}{\sqrt2\sigma}\Big)\Big]
\end{aligned}
$$

**Q-function:** $Q(x)\triangleq\frac1{\sqrt{2\pi}}\int_x^{+\infty}e^{-t^2/2}dt\equiv\frac12\,\text{erfc}\big(\frac{x}{\sqrt2}\big)$.

In Matlab: `erf`, `erfc`, `qfunc`. Esempio (p. 26): CDF di $N(0,1)$ con `x = -3:0.1:3; y = (1/2)*(1+erf(x/sqrt(2))); plot(x,y)`.

### Funzione di una v.a. · [[Probabilità.pdf#page=27|p. 27]]

$Y=g(X)$ è a sua volta una v.a.; la sua CDF segue dalla definizione, $F_Y(y)=P(\omega: g(X(\omega))\le y)$. Se $y=g(x)$ ha un numero finito di soluzioni $x_i$ con $g'(x_i)\ne0$:

$$f_Y(y)=\sum_i\frac{f_X(x_i)}{\lvert g'(x_i)\rvert}$$

*Esempio:* $X\sim N(0,1)$, $Y=aX+b$: $g'(x)=a$, unica soluzione $x_1=(y-b)/a$, quindi

$$f_Y(y)=\frac{f_X\big(\frac{y-b}{a}\big)}{\lvert a\rvert}=\frac1{\sqrt{2\pi a^2}}\,e^{-\frac{(y-b)^2}{2a^2}}$$

La trasformazione affine di una gaussiana è ancora gaussiana.

### Media e momenti · [[Probabilità.pdf#page=28|p. 28]]

$$E(X)\triangleq\int_{-\infty}^{+\infty}x\,f(x)\,dx,\qquad\mu_n\triangleq E(X^n)=\int_{-\infty}^{+\infty}x^nf(x)\,dx$$

Per una gaussiana si prova che $\mu=E(X)$. **Teorema fondamentale della media:** per $Y=g(X)$

$$E(Y)=E[g(X)]=\int_{-\infty}^{+\infty}g(x)f(x)\,dx$$

Per v.a. discrete: $E(X)=\sum_ip(x_i)x_i$, $E[g(X)]=\sum_ip(x_i)g(x_i)$.

### Varianza · [[Probabilità.pdf#page=29|p. 29]]

Dal teorema fondamentale con $g(X)=(X-E(X))^2$:

$$\text{Var}(X)\triangleq E[(X-E(X))^2]=\sigma_X^2,\qquad\sigma_X\triangleq\sqrt{\text{Var}(X)}\ (\text{deviazione standard})$$

Per una gaussiana $\sigma^2=\text{Var}(X)$. Relazione fondamentale (espandendo il quadrato e usando la linearità): $\text{Var}(X)=E(X^2)-E^2(X)$, con $E(X^2)=\int x^2f(x)\,dx$ il **valor quadratico medio**.

### Proprietà di media e varianza · [[Probabilità.pdf#page=30|p. 30]]

Media: (1) *linearità* $E[a\,g(X)+b\,h(X)]=a\,E[g(X)]+b\,E[h(X)]$, in particolare $E(aX+b)=aE(X)+b$; (2) $g\ge0\Rightarrow E[g(X)]\ge0$; (3) $g_1\ge g_2\Rightarrow E[g_1]\ge E[g_2]$; (4) $a\le g\le b\Rightarrow a\le E[g(X)]\le b$.

Varianza: $\text{Var}(aX+b)=a^2\text{Var}(X)$ (non dipende da $b$: invarianza per traslazione), $\sigma_Y=\lvert a\rvert\sigma_X$. **V.a. centrata** $Y=X-\mu_X$: $E(Y)=0$, $\text{Var}(Y)=\text{Var}(X)$.

### Coppie di v.a. · [[Probabilità.pdf#page=31|p. 31]]–[[Probabilità.pdf#page=33|33]]

![[probabilita-p31-coppia-va.png|300]]

Una coppia di v.a. sono due funzioni su $\Omega$: $\omega\mapsto(X(\omega),Y(\omega))\in\mathbb R\times\mathbb R$. Studiare $X$ e $Y$ separatamente (CDF $F_X$, $F_Y$) non dice nulla sulla loro relazione. Si definiscono:

$$F_{XY}(x,y)\triangleq P(X\le x,Y\le y),\qquad f_{XY}(x,y)\triangleq\frac{\partial^2}{\partial x\,\partial y}F_{XY}(x,y)$$

Proprietà (p. 32):
1. $F_X(x)=F_{XY}(x,+\infty)$ e 2. $F_Y(y)=F_{XY}(+\infty,y)$ (CDF marginali);
3. $f_X(x)=\int f_{XY}(x,y)\,dy$ e 4. $f_Y(y)=\int f_{XY}(x,y)\,dx$ (pdf marginali);
5. $\iint f_{XY}\,dx\,dy=1$;
6. $P((X,Y)\in A)=\iint_Af_{XY}\,dx\,dy$;
7. $F_{XY}(x,y)=\int_{-\infty}^x\int_{-\infty}^yf_{XY}(u,v)\,du\,dv$.

Proprietà della CDF congiunta (p. 33): $F(-\infty,y)=F(x,-\infty)=0$, $F(+\infty,+\infty)=1$; $P(x_1<X\le x_2,Y\le y)=F(x_2,y)-F(x_1,y)$ (analoga in $Y$); e

$$P(x_1<X\le x_2,\ y_1<Y\le y_2)=F(x_2,y_2)-F(x_1,y_2)-F(x_2,y_1)+F(x_1,y_1)$$

(regola mnemonica: $+$ per coppie «concordi», $-$ per discordi).

### Distribuzioni condizionali e indipendenza · [[Probabilità.pdf#page=34|p. 34]], [[Probabilità.pdf#page=35|35]]

Come cambia la pdf marginale di $Y$ fissando $\{X=x\}$ (es.: il peso di una persona data la sua altezza):

$$f_X(x\mid y)\triangleq\frac{f_{XY}(x,y)}{f_Y(y)},\qquad f_Y(y\mid x)\triangleq\frac{f_{XY}(x,y)}{f_X(x)},\qquad\int f_X(x\mid y)\,dx=\int f_Y(y\mid x)\,dy=1$$

$X$ e $Y$ sono **statisticamente indipendenti** se $f_{XY}(x,y)=f_X(x)f_Y(y)$ (equivalente in termini di CDF congiunta o DF congiunta per v.a. discrete). Allora $f_X(x\mid y)=f_X(x)$ e $f_Y(y\mid x)=f_Y(y)$: la condizionale coincide con la marginale.

### Caratterizzazione sintetica di una coppia · [[Probabilità.pdf#page=36|p. 36]]–[[Probabilità.pdf#page=38|38]]

**Teorema fondamentale della media:** per $Z=g(X,Y)$

$$E(Z)=\iint g(x,y)f_{XY}(x,y)\,dx\,dy\qquad\Big(\text{discrete: }\sum_{i,j}g(x_i,y_j)\,p_{XY}(x_i,y_j)\Big)$$

*Linearità:* $E[a_1g_1+a_2g_2]=a_1E[g_1]+a_2E[g_2]$; in particolare $E(a_1X+a_2Y)=a_1E(X)+a_2E(Y)$.

$$
\begin{aligned}
\text{Corr}(X,Y)&\triangleq E(XY)=\iint xy\,f_{XY}\,dx\,dy&&\text{correlazione}\\
\text{Cov}(X,Y)&\triangleq E[(X-\mu_X)(Y-\mu_Y)]&&\text{covarianza}\\
\rho_{XY}&\triangleq\frac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y}&&\text{coefficiente di correlazione}
\end{aligned}
$$

Correlazione e covarianza possono avere segno qualsiasi. Con $X=Y$: $\text{Corr}(X,X)=E(X^2)$ (valor quadratico medio), $\text{Cov}(X,X)=\text{Var}(X)$.

Proprietà (p. 38):
1. $\text{Cov}(X,Y)=E(XY)-E(X)E(Y)$ (relazione fondamentale);
2. $E[(X+Y)^2]=E(X^2)+E(Y^2)+2E(XY)$; se $X,Y$ **ortogonali** ($E(XY)=0$): $E[(X+Y)^2]=E(X^2)+E(Y^2)$;
3. $\text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)+2\text{Cov}(X,Y)$; se **incorrelate** ($\text{Cov}=0$): $\text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)$. Per $n$ v.a.: $\text{Var}\big(\sum_ic_iX_i\big)=\sum_ic_i^2\text{Var}(X_i)+\sum_i\sum_{j\ne i}c_ic_j\text{Cov}(X_i,X_j)$;
4. $\lvert E(XY)\rvert\le\sqrt{E(X^2)}\sqrt{E(Y^2)}$ (Schwarz), con uguaglianza se e solo se $Y=a^\ast X$ in media quadratica;
5. $\lvert\text{Cov}(X,Y)\rvert\le\sigma_X\sigma_Y$ (Schwarz), con uguaglianza se e solo se $Y=a^\ast X+b^\ast$ in media quadratica;
6. $\lvert\rho_{XY}\rvert\le1$.

*Approfondimenti nel wiki: [[spazio-di-probabilita]], [[probabilita-condizionale]], [[variabili-aleatorie-notevoli]], [[variabile-aleatoria-gaussiana]], [[coppie-di-variabili-aleatorie]], [[correlazione-e-covarianza]].*


## Lezione 3 — Campionamento e conversione A/D e D/A

*Fonte: Campionamento_AD_DA.pdf (43 slide). Notazione delle slide: $T_c$ = periodo di campionamento, $f_c=1/T_c$ = frequenza di campionamento, $f_m$ = banda monolatera del segnale (le slide usano anche $B_x$). Le figure sono le slide stesse.*

### Elaborazione digitale dei segnali · [[Campionamento_AD_DA.pdf#page=2|p. 2]]–[[Campionamento_AD_DA.pdf#page=4|4]]

- I fenomeni fisici evolvono con continuità nel tempo e nell'ampiezza, quindi si rappresentano con segnali **analogici**. Le prime elaborazioni erano analogiche (progetto/realizzazione di un circuito: processo lungo, costoso, poco flessibile); oggi l'elaborazione è **digitale**.
- Per essere elaborato, memorizzato o trasmesso digitalmente, un segnale analogico va trasformato in digitale (discreto nel tempo e nell'ampiezza); spesso serve anche la trasformazione inversa. Due dispositivi fondamentali: **convertitore A/D** (analogico → digitale) e **convertitore D/A** (digitale → analogico).
- Sistemi digitali realizzabili con ASIC, DSP, FPGA, micro-controller (Atmel, STM), microprocessori general purpose (Intel, AMD). L'elaborazione è un algoritmo traducibile in codice software.
- **Vantaggi:** programmabilità/versatilità/sviluppo rapido (riprogrammabile: software upgrade); stabilità/riproducibilità (dispositivi diversi con lo stesso programma danno gli stessi risultati); potenzialità (algoritmi complessi non realizzabili in analogico: crittografia, correzione/rivelazione d'errore, compressione dati); costi (produzione in grandi quantità a basso costo).

### Conversione A/D e D/A · [[Campionamento_AD_DA.pdf#page=5|p. 5]], [[Campionamento_AD_DA.pdf#page=6|6]]

- **Conversione A/D** = due operazioni: **campionamento** (discretizzazione dei tempi: tempo continuo → discreto) e **quantizzazione** (discretizzazione delle ampiezze: continue → discrete).
- Il campionamento è invertibile sotto opportune ipotesi (**teorema del campionamento**); la quantizzazione è **irreversibile**.
- **Conversione D/A** = una sola operazione, l'**interpolazione** (tempo discreto → continuo). Anche con campionamento perfettamente reversibile, in cascata A/D + D/A si ha $x_r(t)\ne x_a(t)$ per effetto della quantizzazione.

### Campionamento uniforme · [[Campionamento_AD_DA.pdf#page=7|p. 7]], [[Campionamento_AD_DA.pdf#page=8|8]]

![[campionamento-p7-campionamento-uniforme.png|380]]

Campionare $x_a(t)$ = estrarne i valori in istanti discreti, in genere equispaziati di $T_c$:

$$x(n)=x_a(nT_c)$$

$T_c$ in s (o sottomultipli), $f_c=1/T_c$ in Hz (o multipli; talvolta in campioni/s). **Problema fondamentale:** scegliere $f_c=1/T_c$ in modo appropriato per un dato $x_a(t)$.

### Scelta della frequenza di campionamento · [[Campionamento_AD_DA.pdf#page=9|p. 9]]

![[campionamento-p9-scelta-fc.png|380]]

$f_c$ è fondamentale per una buona rappresentazione e per ricostruire il segnale dai campioni: $T_c$ troppo grande va bene solo per segnali lentamente variabili/a banda stretta; per segnali rapidamente variabili/a larga banda serve $T_c$ piccolo. $f_c$ è proporzionale alla rapidità di variazione nel tempo, o equivalentemente alla banda in frequenza: è l'osservazione intuitiva alla base del teorema del campionamento.

### Invertibilità del campionamento · [[Campionamento_AD_DA.pdf#page=10|p. 10]]

![[campionamento-p10-invertibilita.png|380]]

Dai campioni $x(n)$ si può ricostruire $x_a(t)$? A prima vista **no**: esistono infiniti segnali a tempo continuo con gli stessi campioni (es. $x_{a1}(t)$ e $x_{a2}(t)$ in figura). Occorrono condizioni aggiuntive: imponendo ipotesi su $x_a(t)$ e scegliendo $f_c$ opportunamente, $x_a(t)$ è ricostruibile perfettamente. È la tesi del **teorema del campionamento (di Shannon)**.

### Campionamento ideale · [[Campionamento_AD_DA.pdf#page=11|p. 11]]

![[campionamento-p11-campionamento-ideale.png|380]]

Per la dimostrazione si schematizza il campionamento in due stadi: (1) $x_a(t)$ è moltiplicato per un pettine di delta $\Delta_{T_c}(t)$ di periodo $T_c$; (2) dal segnale $x_\delta(t)$ si estraggono i campioni $x(n)=x(nT_c)$. Modello utile allo studio matematico, senza riscontro pratico. Il segnale a tempo continuo $x_\delta(t)$ è il **campionamento ideale**:

$$x_\delta(t)=x_a(t)\sum_{n=-\infty}^{+\infty}\delta(t-nT_c)=\sum_{n=-\infty}^{+\infty}x_a(nT_c)\,\delta(t-nT_c)$$

Lo studio dell'invertibilità equivale a quello del primo stadio.

### Spettro del segnale campionato idealmente · [[Campionamento_AD_DA.pdf#page=12|p. 12]]

Trasformata del pettine: $\sum_n\delta(t-nT_c)\ \overset{FT}{\longleftrightarrow}\ \frac1{T_c}\sum_k\delta\big(f-\frac k{T_c}\big)$. Il prodotto nel tempo diventa convoluzione in frequenza:

$$X_\delta(f)=\frac1{T_c}\sum_{k=-\infty}^{+\infty}X_a\Big(f-\frac k{T_c}\Big)$$

Replicazione dello spettro $X_a(f)$ con passo $f_c=1/T_c$: spettro periodico di periodo $f_c$. L'invertibilità equivale a stabilire quando $X_a(f)$ si ottiene univocamente dalla sua replicazione (la relazione generatore → replicazione non è, in generale, univoca). Si assume allora $x_a(t)$ a **banda rigorosamente limitata** con banda monolatera $B_x=f_m$ e si studia graficamente per diversi $f_c$.

### I tre casi del campionamento · [[Campionamento_AD_DA.pdf#page=13|p. 13]]

![[campionamento-p13-tre-casi-campionamento.png|420]]

Si può determinare $X_a(f)$ univocamente **solo se** $f_c\ge2f_m$.

### Teorema del campionamento (Shannon) · [[Campionamento_AD_DA.pdf#page=14|p. 14]]

- **Ipotesi:** $x_a(t)$ a banda rigorosamente limitata, banda monolatera $B_x=f_m$; $f_c=1/T_c\ge2f_m$; $x(n)=x_a(nT_c)$.
- **Tesi:** è possibile ricostruire perfettamente $x_a(t)$ dai suoi campioni $x(n)=x_a(nT_c)$.
- Minima frequenza di campionamento $f_{c,\min}=2f_m$: **frequenza di Nyquist** di $x_a(t)$.

### Ricostruzione del segnale a tempo continuo · [[Campionamento_AD_DA.pdf#page=15|p. 15]]

![[campionamento-p15-filtro-ricostruzione.png|380]]

Per ricostruire perfettamente $x_a(t)$ da $x_\delta(t)$ serve un LPF ideale:

$$H_r(f)=T_c\,\Pi\Big(\frac f{2f_r}\Big),\qquad f_m\le f_r\le f_c-f_m$$

Il guadagno $T_c$ compensa il fattore $1/T_c$ dello spettro; scelta comune $f_r=f_c/2$.

### Effetti del teorema · [[Campionamento_AD_DA.pdf#page=16|p. 16]]

La $f_c$ richiesta cresce linearmente con la banda:

| Segnale | Banda monolatera $f_m$ | Frequenza di campionamento $f_c$ |
|---|---|---|
| Voce | 4 kHz | $\ge 8$ kHz |
| Audio | 20 kHz | $\ge 40$ kHz |
| Video | 5 MHz | $\ge 10$ MHz |

Al crescere di $f_c$ crescono il costo dell'hardware (campionatore) e il numero di campioni (memoria). Esempio: 1 minuto di audio mono a $f_c=44.1$ kHz → $60\times44\,100=2\,646\,000$ campioni; il doppio in stereo (canali L ed R). Campionare con $f_c$ maggiore di Nyquist è il **sovracampionamento** (oversampling): non conveniente per complessità e costo, ma può servire contro alcuni problemi pratici.

### Interpolazione ideale (serie di Shannon) · [[Campionamento_AD_DA.pdf#page=17|p. 17]]

![[campionamento-p17-serie-shannon.png|380]]

La ricostruzione ideale usa $H_r(f)=T_c\Pi\big(\frac f{2f_r}\big)$ con $f_m\le f_r\le f_c-f_m$. Scegliendo $f_r=f_c/2$:

$$H_r(f)=T_c\,\Pi(fT_c)\ \overset{FT}{\longleftrightarrow}\ h_r(t)=\text{sinc}\Big(\frac t{T_c}\Big)$$

$$x_r(t)=\sum_{n=-\infty}^{+\infty}x_a(nT_c)\,\text{sinc}\Big(\frac{t-nT_c}{T_c}\Big)\qquad\text{(serie di Shannon)}$$

Usa segnali sinc (a banda rigorosamente limitata); fisicamente non realizzabile: instabile e non causale.

### Aliasing · [[Campionamento_AD_DA.pdf#page=18|p. 18]]

![[campionamento-p18-aliasing-sinusoide.png|380]]

Si verifica quando $f_c$ non soddisfa il teorema: sovrapposizione tra le repliche. Ogni componente a frequenza $f_0>f_c/2$ è spostata («aliased») e compare nel segnale ricostruito alla **frequenza alias** $f_c-f_0$. *Esempio:* $f_0=1.5$ kHz, $f_c=2$ kHz → frequenza alias $2-1.5=0.5$ kHz: una sinusoide a 1.5 kHz (nera) è ricostruita come una a 0.5 kHz (rossa), perché le due hanno gli stessi campioni $x(n)$.

### Campionamento e interpolazione in pratica · [[Campionamento_AD_DA.pdf#page=19|p. 19]]

Il teorema di Shannon si basa su due ipotesi ideali: (1) segnale a banda rigorosamente limitata; (2) interpolazione ideale con sinc. Si approfondiscono separatamente.

### Segnali a banda praticamente limitata · [[Campionamento_AD_DA.pdf#page=20|p. 20]]

![[campionamento-p20-banda-praticamente-limitata.png|380]]

In pratica il campionamento agisce su segnali di durata finita, che non possono avere banda rigorosamente limitata (un segnale a banda rigorosamente limitata ha durata infinita, es. $\text{sinc}$, $\text{sinc}^2$). Si hanno quindi segnali a banda *praticamente* limitata: qualunque sia $f_c$, le repliche di $X_a(f)$ si sovrappongono e c'è **aliasing** nella ricostruzione.

### Filtraggio antialiasing · [[Campionamento_AD_DA.pdf#page=21|p. 21]]

![[campionamento-p21-antialiasing.png|380]]

L'aliasing si riduce col sovracampionamento (a scapito di costo e memoria). Soluzione più efficiente: **filtrare** $x_a(t)$ prima del campionamento con un LPF ideale di frequenza di taglio $f_c/2$ (filtro analogico; in pratica anche questo filtro sarà non ideale).

### Interpolazione non ideale · [[Campionamento_AD_DA.pdf#page=22|p. 22]]–[[Campionamento_AD_DA.pdf#page=24|24]]

![[campionamento-p22-interpolazione-non-ideale.png|420]]

**ZOH (zero-order hold, mantenimento).** Il filtro ideale non è realizzabile; più semplice è mantenere il valore di un campione fino al successivo. Cattiva approssimazione: effetto «scalettatura», elevato contenuto spettrale ad alta frequenza.

$$h_r(t)=\Pi\Big(\frac{t-T_c/2}{T_c}\Big)\ \overset{FT}{\longleftrightarrow}\ H_r(f)=T_c\,\text{sinc}(fT_c)\,e^{-j\pi fT_c}$$

Sistema LTI stabile e causale → fisicamente realizzabile. Migliorabile con un ulteriore LPF del segnale ZOH, che elimina le transizioni brusche (ricostruito più «dolce»).

![[campionamento-p23-zoh.png|380]]

**FOH (first-order hold, interpolazione lineare).** Si interpolano linearmente due campioni consecutivi: migliore approssimazione, minor contenuto spettrale ad alta frequenza.

$$h_r(t)=\Lambda\Big(\frac t{T_c}\Big)\ \overset{FT}{\longleftrightarrow}\ H_r(f)=T_c\,\text{sinc}^2(fT_c)$$

Sistema LTI stabile ma non causale → realizzabile introducendo un ritardo di $T_c$ (un campione). *Nota: la slide scrive «First-Order Hold (ZOH)»: la sigla corretta è FOH.*

![[campionamento-p24-foh.png|380]]

### Quantizzazione · [[Campionamento_AD_DA.pdf#page=25|p. 25]]

![[campionamento-p25-quantizzazione.png|380]]

Oltre alla discretizzazione dei tempi occorre discretizzare le ampiezze. L'intervallo (reale) delle ampiezze è suddiviso in **intervalli di quantizzazione**; a ciascuno è associato un **livello di restituzione** (o di quantizzazione), che rappresenta tutte le ampiezze dell'intervallo. Esempio: le ampiezze in $(1,2)$ sono rappresentate dal livello 1.5 (punto medio), quelle in $(2,3)$ da 2.5, ecc.

### Relazione ingresso-uscita del quantizzatore · [[Campionamento_AD_DA.pdf#page=26|p. 26]]

![[campionamento-p26-quantizzatore-uniforme.png|380]]

Il quantizzatore è un sistema TD non lineare e istantaneo: $x_q(n)=Q[x(n)]$. Il **quantizzatore uniforme** ha due parametri: $\Delta$ = passo di quantizzazione (larghezza degli intervalli) e $M$ = numero di intervalli/livelli di restituzione. Per un quantizzatore simmetrico: $(-X_{max},X_{max})$ è l'intervallo delle ampiezze d'ingresso e

$$2X_{max}=M\Delta\quad(\text{dinamica del quantizzatore})$$

(figura: quantizzatore con $M=4$ livelli).

### Codifica binaria · [[Campionamento_AD_DA.pdf#page=27|p. 27]]

![[campionamento-p27-codifica-binaria.png|380]]

Gli $M$ livelli $\{q_1,\dots,q_M\}$ sono convertiti in stringhe di bit: servono $b\ge\log_2M$ bit; di solito $M=2^b$ per semplificare la codifica binaria. Schemi di codifica: **naturale** (esempio), in **segno e modulo**, in **complemento a due**; la scelta dipende dall'architettura del sistema di elaborazione. Esempio: $M=4\Rightarrow b=2$ bit.

### Errore di quantizzazione · [[Campionamento_AD_DA.pdf#page=28|p. 28]]

![[campionamento-p28-errore-quantizzazione.png|380]]

Per fissare criteri quantitativi di dimensionamento si definisce

$$e(n)=x_q(n)-x(n)\quad\Rightarrow\quad x_q(n)=x(n)+e(n)$$

Il quantizzatore si modella come un **sommatore**; $e(n)$ è il **rumore di quantizzazione**. Due regioni di ampiezza di $x(n)$:
1. $\mathcal R_g\triangleq[-X_{max},X_{max}]$ — **regione granulare**: $\lvert e(n)\rvert\le\frac12\Delta$;
2. $\mathcal R_s\triangleq\,]-\infty,-X_{max}[\,\cup\,]X_{max},+\infty[$ — **regione di sovraccarico**: $e(n)$ non limitato.

![[campionamento-p28-caratteristica-quantizzatore.png|420]]

### Fattore di carico · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

L'errore in sovraccarico è irreversibile: va evitato che il quantizzatore ci operi, aumentando $X_{max}$. Ma a parità di $M$, più $X_{max}$ → più $\Delta$ → più errore nella regione granulare. Ragionevole scegliere $X_{max}$ proporzionale al livello del segnale: $x_{rms}=\sqrt{P_x}$ (valore efficace). **Fattore di carico:**

$$k_c\triangleq\frac{X_{max}}{x_{rms}}$$

Assimilando $x(n)$ a una v.a. a media nulla e deviazione standard $x_{rms}$, dalla disuguaglianza di Chebyshev la probabilità di sovraccarico è

$$P_s=P(\lvert x(n)\rvert>X_{max})\le\frac1{k_c^2}$$

Con $k_c=4$ (*four-sigma loading*): $P_s\le\frac1{16}=0.0625$ (6.25%).

### SNR di quantizzazione · [[Campionamento_AD_DA.pdf#page=30|p. 30]]

Fissato $X_{max}$ tramite $k_c$, si misura l'accuratezza nella regione granulare con l'SNR di quantizzazione:

$$\text{SNR}\triangleq\frac{P_x}{P_e}=\frac{\langle x^2(n)\rangle}{\langle e^2(n)\rangle},\qquad\text{SNR}_{dB}=10\log_{10}\text{SNR}$$

$\text{SNR}\gg1$ ⇒ quantizzazione accurata; considera solo l'errore nella regione granulare. Modellando $e(n)\sim U(-\Delta/2,\Delta/2)$: $\langle e^2(n)\rangle\sim E[e^2(n)]=\Delta^2/12$. «Con semplici passaggi algebrici»:

$$
\begin{aligned}
\text{SNR}&=\frac{x_{rms}^2}{\Delta^2/12}=\frac{X_{max}^2/k_c^2}{(2X_{max}/M)^2/12}=\frac{3M^2}{k_c^2}&&P_x=X_{max}^2/k_c^2,\ \Delta=2X_{max}/M\\
\text{SNR}_{dB}&=10\log_{10}3+20\log_{10}2^b-20\log_{10}k_c&&M=2^b\\
&=6.02\,b-[k_c]_{dB}+4.77&&\textbf{legge dei 6 dB/bit}
\end{aligned}
$$

L'SNR migliora di 6 dB per ogni bit in più, cioè per ogni raddoppio del numero di livelli.

### Progetto di un quantizzatore · [[Campionamento_AD_DA.pdf#page=31|p. 31]]

Formule di progetto: $P_s\le1/k_c^2$ e $\text{SNR}_{dB}=6.02\,b-[k_c]_{dB}+4.77$. Al crescere di $k_c$: $P_s$ e $\text{SNR}_{dB}$ diminuiscono. Al crescere di $M=2^b$: $\text{SNR}_{dB}$ aumenta (migliora la qualità) ma crescono costo e memoria.

*Esempio 7.6:* si vuole $\text{SNR}_{dB}=85$ dB con $k_c=4$: $85=6.02\,b-12.04+4.77\Rightarrow b=\frac{85+7.27}{6.02}=15.3\Rightarrow b=16$ bit. Audio stereo a $f_c=44.1$ kHz: $16\times44.1$ kHz $=705.6$ kbit/s per canale (L/R); 1 minuto di stereo $=2\times60\times44\,100\times16=84\,672\,000$ bit $=10\,584\,000$ byte $=10\,584$ kB $\approx10.6$ MB. Conversioni (ISO/IEC): 1 byte = 8 bit; 1 kB = 1000 byte; 1 MB = 1000 kB.

### Limiti della quantizzazione uniforme · [[Campionamento_AD_DA.pdf#page=32|p. 32]]

La quantizzazione uniforme è teoricamente ottima solo se $x(n)$ è uniforme in $(-X_{max},X_{max})$. Il segnale vocale ha pdf non uniforme (valori vicini a zero più probabili), ben modellata da una **distribuzione di Laplace**:

$$f_X(x)=\frac\lambda2\,e^{-\lambda\lvert x\rvert}\qquad(\lambda>0)$$

Intuitivamente le ampiezze piccole vanno quantizzate più finemente ⇒ **quantizzazione non uniforme**.

### Quantizzazione non uniforme · [[Campionamento_AD_DA.pdf#page=33|p. 33]]

Dati $M+1$ livelli di decisione $x_0<x_1<\dots<x_M$, con $x_0=-\infty$, $x_M=+\infty$, si ha una partizione $R_1,\dots,R_M$ dell'asse reale, $R_i=(x_{i-1},x_i)$: intervalli *esterni* $R_1=\,]-\infty,x_1]$, $R_M=[x_{M-1},+\infty[$; *interni* $R_i$ per $i=2,\dots,M-1$. Assegnati gli $M$ livelli di restituzione $q_1,\dots,q_M$, una legge arbitraria è

$$Q(x)=q_i\quad\text{se }x\in R_i$$

Regione granulare $R_g=\bigcup_{i=2}^{M-1}R_i=(x_1,x_{M-1})$; regione di sovraccarico $R_s=R_1\cup R_M=\,]-\infty,x_1]\cup[x_{M-1},+\infty[$.

### Quantizzazione ottima: Lloyd-Max · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=35|35]]

Con $e(n)=Q[x(n)]-x(n)$ e $f_X(x)$ la pdf di $x(n)$ (supposto stazionario del primo ordine), il valore quadratico medio dell'errore (MSE) è

$$\text{MSE}\triangleq E[e^2(n)]=\sum_{i=1}^{M}\int_{R_i}(q_i-x)^2f_X(x)\,dx$$

Il quantizzatore ottimo secondo il criterio MMSE minimizza l'MSE rispetto a intervalli $R_i$ (livelli di decisione $x_1,\dots,x_{M-1}$) e livelli $q_1,\dots,q_M$. Non esiste soluzione in forma chiusa, ma si trovano **due condizioni necessarie** fissando un sottoinsieme di variabili e ottimizzando l'altro:

1. **Fissati i livelli di decisione**, i livelli di restituzione ottimi sono i **centroidi**: $q_i=E[x(n)\mid x(n)\in R_i]$, $i=1,\dots,M$ (media condizionale; risultato noto della stima ottima MMSE). *(Si ottiene azzerando la derivata dell'MSE rispetto a $q_i$: $2\int_{R_i}(q_i-x)f_X\,dx=0$.)*
2. **Fissati i livelli di restituzione**, i livelli di decisione sono i punti medi: $x_i=\frac{q_i+q_{i+1}}2$, $i=1,\dots,M-1$ (regola a minima distanza: $x(n)$ è approssimato dal livello $q_i$ più vicino).

**Algoritmo di Lloyd-Max:** si applicano alternativamente le due condizioni, iterando finché l'MSE non si assesta su un valore sufficientemente piccolo.

### Limiti della quantizzazione ottima · [[Campionamento_AD_DA.pdf#page=36|p. 36]]

![[campionamento-p36-companding.png|420]]

Lloyd-Max assume il segnale stazionario e richiede la conoscenza della pdf; come l'uniforme, ha prestazioni fortemente dipendenti dal livello d'ingresso. In telefonia serve che le prestazioni siano all'incirca **indipendenti dal livello** d'ingresso (grande variabilità dei parlatori): **quantizzazione robusta**. Si studia con lo schema del **companding**: legge di compressione seguita da quantizzazione uniforme; in decodifica si applica la legge simmetrica (espansione). *(Nella figura il secondo blocco è etichettato «n-bit uniform decoder» come il terzo; dal testo dovrebbe essere l'encoder.)*

### Analisi del companding · [[Campionamento_AD_DA.pdf#page=37|p. 37]]–[[Campionamento_AD_DA.pdf#page=39|39]]

**MSE (approssimazione high resolution)**, valida se $M\gg1$, sovraccarico trascurato e pdf circa costante in ogni intervallo:

$$\text{MSE}=E[\lvert e(n)\rvert^2]\approx\frac1{12}\sum_{i=1}^{M}p_i\Delta_i^2,\qquad\Delta_i\triangleq x_i-x_{i-1},\quad p_i\triangleq\Pr(x(n)\in R_i)\approx f_X(x_i)\Delta_i$$

Con $\Delta_i=\Delta$ (uniforme) si ritrova $\text{MSE}=\Delta^2/12$.

![[campionamento-p38-legge-compressione.png|420]]

**Legge di compressione** $F(x)$: i livelli $x_{i-1},x_i$ del quantizzatore non uniforme sono trasformati in $F(x_{i-1}),F(x_i)$ del quantizzatore uniforme, con $\Delta=\frac{2X_{max}}M=F(x_i)-F(x_{i-1})$. Quindi

$$\frac\Delta{\Delta_i}=\frac{F(x_i)-F(x_{i-1})}{x_i-x_{i-1}}\approx F'(x_i)\ \Rightarrow\ \Delta_i\approx\frac\Delta{F'(x_i)}=\frac1{F'(x_i)}\frac{2X_{max}}M$$

Sostituendo nell'MSE e passando all'integrale ($\Delta_i\to dx$):

$$\text{MSE}=\frac1{12}\sum_i\frac{p_i}{[F'(x_i)]^2}\Delta^2=\frac{X_{max}^2}{3M^2}\sum_i\frac{f_X(x_i)}{[F'(x_i)]^2}\Delta_i\ \longrightarrow\ \frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$$

Con $f_X(x)=0$ fuori da $(-X_{max},X_{max})$, $f_X$ pari e $F$ dispari:

$$\text{SNR}=\frac{E[x^2(n)]}{E[e^2(n)]}=\frac{\int_{-X_{max}}^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X}{[F']^2}dx}=\frac{\int_0^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X}{[F']^2}dx}$$

### Companding logaritmico · [[Campionamento_AD_DA.pdf#page=40|p. 40]]

Per rendere l'SNR indipendente dal livello basta scegliere $\frac1{F'(x)}=kx$, cioè

$$F'(x)=\frac1{kx}\ \Rightarrow\ F(x)=c+\frac1k\ln x$$

($c$, $k$ costanti arbitrarie). Imponendo $F(X_{max})=X_{max}$:

$$F(x)=X_{max}+\frac1k\ln\Big(\frac x{X_{max}}\Big),\qquad x\in[0,X_{max}]$$

Con questa $F$ l'integrale a denominatore diventa $k^2\int_0^{X_{max}}x^2f_X\,dx$, che si semplifica con il numeratore:

$$\text{SNR}=\frac{3M^2}{k^2X_{max}^2}$$

Per una pdf $f_X$ **arbitraria**, la legge di compressione che rende l'SNR indipendente dal livello è di tipo **logaritmico**: corrisponde a un raddoppio di $\Delta_i$ per ogni raddoppio del livello. Per $x\to0$ non è implementabile esattamente ($F(x)\to-\infty$): si usano approssimazioni che valgono zero in $x=0$.

### Legge µ · [[Campionamento_AD_DA.pdf#page=41|p. 41]]

![[campionamento-p41-mu-law.png|380]]

$$F(x)=X_{max}\,\frac{\ln(1+\mu\lvert x\rvert/X_{max})}{\ln(1+\mu)}\,\text{sgn}(x),\qquad\lvert x\rvert\le X_{max}$$

$\mu$ determina il livello di compressione; valore usato $\mu=255$; per $\mu=0$ si ha $F(x)=x$ (quantizzazione uniforme). Usata in USA, Canada, Giappone; una approssimazione a 7 segmenti è standardizzata ITU-T [G.711].

### Legge A · [[Campionamento_AD_DA.pdf#page=42|p. 42]]

![[campionamento-p42-a-law.png|380]]

$$F(x)=\begin{cases}X_{max}\dfrac{A\lvert x\rvert/X_{max}}{1+\ln A}\,\text{sgn}(x)&0\le\lvert x\rvert\le X_{max}/A\\[2mm]X_{max}\dfrac{1+\ln(A\lvert x\rvert/X_{max})}{1+\ln A}\,\text{sgn}(x)&X_{max}/A\le\lvert x\rvert\le X_{max}\end{cases}$$

$A$ determina la compressione; valore usato $A=87.6$; per $A=1$ si ha $F(x)=x$. Usata in Europa e nei collegamenti internazionali; approssimazione a 7 segmenti standardizzata ITU-T [G.711].

### Prestazioni del companding logaritmico · [[Campionamento_AD_DA.pdf#page=43|p. 43]]

![[campionamento-p43-prestazioni-companding.png|420]]

Se il segnale impegna tutta la dinamica del quantizzatore:

$$\text{SNR}_{dB}\approx6.02\,b+\alpha,\qquad\alpha=\begin{cases}4.77-20\log_{10}[\ln(1+\mu)]&\mu\text{-law}\\4.77-20\log_{10}[1+\ln A]&A\text{-law}\end{cases}$$

Vale ancora la legge dei 6 dB/bit; **quantizzazione robusta**: l'SNR non dipende (idealmente) dal livello di $x(n)$. Per la quantizzazione uniforme $\alpha=4.77-20\log_{10}(X_{max}/x_{rms})$, che dipende dal livello. Numeri:

- $A=87.6$: $1+\ln87.6=5.47$, $\alpha=4.77-14.76\Rightarrow\text{SNR}_{dB}\approx6.02\,b-9.99$;
- $\mu=255$: $\ln256=5.55$, $\alpha=4.77-14.88\Rightarrow\text{SNR}_{dB}\approx6.02\,b-10.11$;
- uniforme con $k_c=4$: $\alpha=4.77-12.04\Rightarrow\text{SNR}_{dB}\approx6.02\,b-7.3$.

*Approfondimenti nel wiki: [[teorema-del-campionamento]], [[aliasing]], [[interpolazione]], [[quantizzazione-uniforme]], [[snr-di-quantizzazione]], [[quantizzazione-non-uniforme]], [[companding]] (derivazioni estese, grafici, animazioni), [[dimensionamento-quantizzatore]], [[g711]].*


## Lezione 4 — Rappresentazione complessa in banda base

*Fonte: Rappresentazione_Rice.pdf (27 pagine: 19 slide, numerate «n/19», più 8 pagine di appunti a mano della docente, alle p. 2, 6, 8, 14, 18, 19, 21, 24). Le equazioni (1)–(25) sono quelle delle slide. Le slide sono in inglese; le note a mano in italiano.*

### Il modulatore nel sistema · appunti [[Rappresentazione_Rice.pdf#page=2|p. 2]]

![[rappresentazione-rice-p2-appunti-sistema-e-canale.png|520]]

- Sorgente → $s(n)$ → **modulatore** (MOD) → $s(t)$ → canale fisico. Il modulatore **associa una forma d'onda analogica a ogni simbolo o stringa di bit**.
- Deve **allocare** il segnale in una specifica porzione dello spettro, centrata attorno a una frequenza portante $f_c$ (*carrier*). Il canale è caratterizzato da una risposta in frequenza $H(f)$ e da una determinata banda a disposizione (disegno: due lobi di larghezza $B$ attorno a $\pm f_c$).
- Il **trasmettitore** porta il segnale nella porzione di spettro prevista, per adattarlo alla capacità del canale; il **ricevitore** lo riporta in banda base, e questo comporta che il segnale diventa **complesso**.
- In entrambi i momenti, trasmissione e ricezione, c'è un passaggio **complesso ↔ reale** (trasmissione: complesso → reale; ricezione: reale → complesso), eseguito da un DSP.

### Modulazione · [[Rappresentazione_Rice.pdf#page=3|p. 3]]

![[rappresentazione-rice-p3-modulazione-binaria.png|480]]

- La **modulazione** è la rappresentazione dell'informazione digitale con forme d'onda analogiche trasmissibili su canali fisici.
- Esempio di modulazione binaria: i simboli (bit) sono mappati su una forma d'onda moltiplicando ciascun simbolo per traslate di un impulso rettangolare (**modulazione lineare**; nota: «perché $s(t)$ dipende linearmente dai simboli»):

$$s(t)=\sum_m b[m]\,\Pi(t-mT),\qquad b[m]\in\{-1,+1\}$$

  (figura: sequenza $+1,-1,-1,+1,+1,+1,-1,+1,-1,+1,+1,\dots$). Gli appunti scrivono la somma con l'indice sbagliato: va letta sull'indice $m$ dei simboli.
- Nell'esempio la forma d'onda è limitata nel tempo; le forme d'onda usate per modulare sono spesso **vincolate nel dominio della frequenza**, per le caratteristiche fisiche del mezzo o per fattori esterni (es. regole sull'uso dello spettro). Nota: i segnali da trasmettere devono soddisfare vincoli nel dominio della frequenza, che riguardano **dove** è allocato il loro spettro.

### Segnali in banda base e in banda passante · [[Rappresentazione_Rice.pdf#page=4|p. 4]], [[Rappresentazione_Rice.pdf#page=5|5]]

- Un segnale $s_b(t)$ è **in banda base** se, per qualche $B>0$,

$$S_b(f)\approx0,\qquad\lvert f\rvert>B\tag{1}$$

  Un canale LTI è in banda base se la sua $H(f)$ soddisfa la (1).
- Un segnale $s_p(t)$ è **in banda passante** se

$$S_p(f)\approx0,\qquad\lvert f\pm f_c\rvert>B/2\tag{2}$$

  con $f_c>B>0$ detta frequenza **portante** (*carrier*). Un canale LTI è passa-banda se $H(f)$ soddisfa la (2). Nota: si dice banda passante perché il contenuto informativo è traslato e centrato attorno a $f_c$.
- Sia $s_b(t)$ che $s_p(t)$ reali, con trasformate (in senso ordinario o generalizzato) $S_b(f)$, $S_p(f)$: per la simmetria coniugata $S_b(f)=S_b^\ast(-f)$ e $S_p(f)=S_p^\ast(-f)$ (le trasformate dei segnali reali godono della **simmetria hermitiana**).

![[rappresentazione-rice-p5-spettri-banda-base-passa-banda.png|480]]

  A sinistra il segnale in banda base: $\text{Re}\,S(f)$ è un triangolo di altezza 1 su $(-B,B)$ (pari), $\text{Im}\,S(f)$ vale $+1$ su $(-B,0)$ e $-1$ su $(0,B)$ (dispari). A destra il passa-banda: stesse forme attorno a $\pm f_c$, larghe $B$. Nota (con $f_c$ cerchiato): **l'obiettivo è svincolarsi da $f_c$**, perché l'informazione di $s(t)$ non dipende da $f_c$ e si può descrivere tutto con un segnale in banda base.

![[grafico-rice-condizione-passabanda.png|480]]
*Figura di supporto: perché $f_c>B$. Il bordo inferiore del lobo positivo è $f_c-B/2>B/2>0$, quindi i due lobi non si toccano e non contengono $f=0$. (a) $f_c=2B$, (b) $f_c=B$ (soglia), (c) $f_c=B/2$: i lobi si toccano in 0, (d) $f_c=B/4$: si sovrappongono e lo spettro diventa di banda base.*

### Vantaggi della banda base · appunti [[Rappresentazione_Rice.pdf#page=6|p. 6]]

![[rappresentazione-rice-p6-appunti-vantaggi-banda-base.png|420]]

Portare il segnale in banda base permette di:
- ridurre i costi hardware per il campionamento;
- guadagnare **modularità e indipendenza**: si riutilizzano componenti che operano in banda base, senza costruirli ad hoc per la specifica banda del segnale;
- (in rosso) altrimenti non si potrebbero generalizzare gli algoritmi, e calcolarli in digitale costerebbe troppo.

### Banda · [[Rappresentazione_Rice.pdf#page=7|p. 7]], [[Rappresentazione_Rice.pdf#page=8|8]]

- **Banda** = ampiezza dell'intervallo di frequenze occupato dalla trasformata di Fourier. **Banda monolatera** (*one-sided*): occupazione spettrale sulle frequenze positive; **bilatera** (*two-sided*): su frequenze positive e negative. Per un segnale reale la bilatera è il doppio della monolatera, per la simmetria coniugata $X(f)=X^\ast(-f)$. Di solito «banda» indica la monolatera.
- Un segnale passa-banda è **a banda stretta** (*narrowband*) se $B/f_c\ll1$ (nota: non è un'ipotesi stringente). Da qui in poi si trattano solo segnali passa-banda a banda stretta.

![[rappresentazione-rice-p8-appunti-banda-stretta.png|420]]

### Rappresentazione complessa in banda base · [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

- I canali passa-banda sono molto usati: bisogna saper trasmettere e ricevere segnali passa-banda.
- **Tutta l'informazione** di un segnale passa-banda reale è contenuta in un corrispondente segnale **complesso in banda base**, detto *rappresentazione complessa in banda base* o **inviluppo complesso**.
- L'inviluppo si può rappresentare a tempo discreto con una frequenza di campionamento **molto più piccola** di quella del segnale passa-banda $s_p(t)$ (nota: «il vantaggio»). Perciò i transceiver moderni implementano algoritmi complessi in digitale (DSP), direttamente sui segnali complessi in banda base, **riducendo al minimo l'elaborazione analogica**. (Ordini di grandezza: per $s_p$ serve $f_s\ge2f_c+B$, per l'inviluppo $f_s\ge B$.)
- **Schema modulare del transceiver:**
  1. un DSP codifica l'informazione nella forma d'onda complessa in banda base (codifica, modulazione, filtraggio);
  2. la forma d'onda in banda base è convertita in su (*upconverted*) nel segnale passa-banda da inviare sul canale fisico;
  3. il segnale passa-banda ricevuto è convertito in giù (*downconverted*) in banda base;
  4. il DSP opera sul segnale in banda base per sincronizzazione, demodulazione e decodifica.

  Così algoritmi sofisticati si sviluppano in banda base, indipendentemente dalla banda fisica usata.

![[rappresentazione-rice-p10-schema-modulare-transceiver.png|480]]

  Note a mano: i punti 1–2 formano il **modulatore** e i punti 3–4 il **demodulatore** («macroblocchi»); il modulatore comprende anche l'upconversion; dal punto 1 si ottiene l'inviluppo complesso in banda base; ci si è svincolati dalla frequenza carrier $f_c$.

### Segnale analitico · [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=12|12]]

Per definire l'inviluppo si costruisce prima il **segnale analitico** associato a $s_p(t)$ (con trasformata $S_p(f)$):

$$S_p^+(f)=\sqrt2\,S_p(f)\,u(f)\tag{3}$$

con $u(\cdot)$ gradino unitario: si annullano le frequenze negative (ridondanti) e si moltiplica per $\sqrt2$, fattore «introdotto per motivi energetici» (conserva l'energia: la parte tenuta ha metà dell'energia, e il $\sqrt2$ la ripristina). A ogni segnale passa-banda corrisponde un unico segnale analitico, e viceversa. Nel tempo:

$$s_p^+(t)=\mathcal F^{-1}[S_p^+(f)]=\sqrt2\,s_p(t)\ast\mathcal F^{-1}[u(f)]\tag{4}$$

$$\mathcal F[u(t)]=\tfrac12\delta(f)+\frac1{j2\pi f}\triangleq U(f)\tag{5}\qquad\mathcal F[U(t)]=u(-f)\ \ (\text{dualità})\tag{6}$$

Dalla (5) e (6), con la proprietà di riflessione:

$$\mathcal F^{-1}[u(f)]=U(-t)=\tfrac12\delta(t)+\frac{j}{2\pi t}\tag{7}$$

Sostituendo la (7) nella (4):

$$s_p^+(t)=\frac1{\sqrt2}s_p(t)+\frac j{\sqrt2}\,s_p(t)\ast\frac1{\pi t}=\frac1{\sqrt2}s_p(t)+\frac j{\sqrt2}\widehat s_p(t)\tag{8}$$

dove

$$\widehat s_p(t)\triangleq s_p(t)\ast\frac1{\pi t}=\int_{-\infty}^{+\infty}\frac{s_p(\tau)}{\pi(t-\tau)}\,d\tau\tag{9}$$

è la **trasformata di Hilbert** di $s_p(t)$. La (8) dice che il segnale analitico è un segnale **complesso**: parte reale = il segnale passa-banda originale scalato; parte immaginaria = la sua trasformata di Hilbert scalata.

### Ritorno al segnale reale e Hilbert in frequenza · [[Rappresentazione_Rice.pdf#page=13|p. 13]], [[Rappresentazione_Rice.pdf#page=14|14]]

![[rappresentazione-rice-p13-segnale-analitico-hilbert.png|480]]

Dalla (8) si deduce immediatamente (relazione inversa) e questo conclude la dimostrazione della corrispondenza biunivoca:

$$s_p(t)=\sqrt2\,\text{Re}\{s_p^+(t)\}\tag{10}$$

Trasformata del segnale analitico:

$$S_p^+(f)=\frac1{\sqrt2}S_p(f)+\frac j{\sqrt2}\mathcal F[\widehat s_p(t)]\tag{11}\qquad\widehat S_p(f)=S_p(f)\,\mathcal F\Big[\frac1{\pi t}\Big]\tag{12}$$

Per calcolare la (12): $\text{sgn}(t)=2u(t)-1$, quindi (appunti p. 14, con la (5))

$$\mathcal F[\text{sgn}(t)]=2\,\mathcal F[u(t)]-\delta(f)=\delta(f)+\frac1{j\pi f}-\delta(f)=\frac1{j\pi f}$$

e per dualità $\mathcal F\big[\frac1{\pi t}\big]=j\,\text{sgn}(-f)=-j\,\text{sgn}(f)$. Perciò

$$\widehat S_p(f)=-j\,\text{sgn}(f)\,S_p(f)$$

![[rappresentazione-rice-p14-appunti-trasformata-sgn.png|420]]
*Appunti p. 14. Nell'ultima riga manca un meno ($j\,\text{sign}(f)$ invece di $-j\,\text{sgn}(f)$); la slide ha il segno giusto.*

**Interpretazione (nota a mano):** la trasformata di Hilbert equivale a sfasare di $-90°$ tutte le componenti frequenziali positive e di $+90°$ quelle negative. *(Refuso della slide, corretto a mano nel PDF: nella (12) e nell'ultima formula va $S_p(f)$, non $S(f)$.)*

### Inviluppo complesso · [[Rappresentazione_Rice.pdf#page=15|p. 15]], [[Rappresentazione_Rice.pdf#page=16|16]]

L'**inviluppo complesso** è il segnale analitico traslato in banda base:

$$S(f)\triangleq S_p^+(f+f_c)=\sqrt2\,S_p(f+f_c)\,u(f+f_c)\tag{13}$$

Viceversa, dato l'inviluppo in frequenza (relazione inversa; la parte tagliata dal gradino viene rimessa dal termine coniugato):

$$S_p(f)=\frac{S(f-f_c)+S^\ast(-f-f_c)}{\sqrt2}\tag{14}$$

*(dimostrazione dalla (16): $s_p=\frac{\sqrt2}2[s\,e^{j2\pi f_ct}+s^\ast e^{-j2\pi f_ct}]$ e traslazioni in frequenza.)*

![[rappresentazione-rice-p15-inviluppo-complesso-spettri.png|480]]
*In alto $S_p(f)$: $\text{Re}$ con due triangoli di altezza $A$ attorno a $\pm f_c$, $\text{Im}$ con due rettangoli di altezza $B$ (positivo in $f_c$, negativo in $-f_c$; qui $A$, $B$ sono altezze, non la banda). In basso l'inviluppo: resta solo il lobo positivo, spostato attorno a 0 e moltiplicato per $\sqrt2$ (altezze $\sqrt2A$, $\sqrt2B$).*

Nel tempo, per la proprietà di traslazione di Fourier (nota: «corrisponde a una traslazione del segnale analitico»):

$$s(t)=\mathcal F^{-1}[S(f)]=s_p^+(t)\,e^{-j2\pi f_ct}=s_c(t)+j\,s_s(t)\tag{15}$$

$s_c(t)$ = componente **in fase (I)**, $s_s(t)$ = componente **in quadratura (Q)**: segnali reali. Per ottenere $s_p$ dall'inviluppo ($s_p^+=s\,e^{j2\pi f_ct}=[s_c+js_s]e^{j2\pi f_ct}$), valida per **qualunque** segnale passa-banda:

$$s_p(t)=\sqrt2\,\text{Re}\{s_p^+(t)\}=\sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_ct}\}\tag{16}$$

$$s_p(t)=\sqrt2\,s_c(t)\cos(2\pi f_ct)-\sqrt2\,s_s(t)\sin(2\pi f_ct)\tag{17}$$

(«in termini di seno e coseno»; il $-$ viene da $\text{Re}\{(s_c+js_s)(\cos\alpha+j\sin\alpha)\}=s_c\cos\alpha-s_s\sin\alpha$, con $\alpha=2\pi f_ct$.) Nota: «quadratura» indica che il prodotto scalare con $s_c$ è nullo (eq. (18)).

![[rappresentazione-rice-p16-componenti-iq.png|480]]

### Energia dell'inviluppo · [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]]

Le forme d'onda passa-banda delle componenti I e Q, $x_c(t)=\sqrt2\,s_c(t)\cos(2\pi f_ct)$ e $x_s(t)=\sqrt2\,s_s(t)\sin(2\pi f_ct)$, sono **ortogonali**:

$$\langle x_c,x_s\rangle=\int_{-\infty}^{+\infty}x_c(t)\,x_s(t)\,dt=0\tag{18}$$

(dimostrazione negli appunti di p. 18, sotto). Per segnali passa-banda reali $u_p$, $v_p$ con inviluppi $u$, $v$:

$$\langle u_p,v_p\rangle=\langle u_c,v_c\rangle+\langle u_s,v_s\rangle=\text{Re}\{\langle u,v\rangle\}\tag{19}$$

Con $u=v=s$ l'**energia dell'inviluppo è uguale a quella del segnale passa-banda**:

$$\lVert s_p\rVert^2=\langle s_p,s_p\rangle=\text{Re}\{\langle s,s\rangle\}=\text{Re}\{\lVert s\rVert^2\}=\lVert s\rVert^2\tag{20}$$

(l'energia è reale, quindi si toglie $\text{Re}$). In componenti, $\lVert s_p\rVert^2=\lVert s_c\rVert^2+\lVert s_s\rVert^2$.

#### Dimostrazione di (18) — appunti p. 18

![[rappresentazione-rice-p18-appunti-ortogonalita-parseval.png|480]]

Con Parseval, $X_c(f)=\frac1{\sqrt2}[S_c(f-f_c)+S_c(f+f_c)]$ e $X_s(f)=\frac1{j\sqrt2}[S_s(f-f_c)-S_s(f+f_c)]$:

$$\langle x_c,x_s\rangle=\int X_c(f)X_s^\ast(f)\,df=\frac1{2j}\int\big[S_c(f-f_c)+S_c(f+f_c)\big]\big[S_s^\ast(f+f_c)-S_s^\ast(f-f_c)\big]\,df$$

Dei quattro termini del prodotto, i due **misti** $S_c(f\mp f_c)S_s^\ast(f\pm f_c)$ sono nulli: per ipotesi i segnali sono a banda stretta ($B/f_c\ll1$), e lo spettro centrato in $+f_c$ non si sovrappone mai a quello in $-f_c$. Restano, con il cambio di variabile $\nu=f\pm f_c$,

$$\frac1{2j}\Big[\int S_c(\nu)S_s^\ast(\nu)\,d\nu-\int S_c(\nu)S_s^\ast(\nu)\,d\nu\Big]=0$$

#### Verifica di (19) e (20) — appunti p. 18, 19

![[rappresentazione-rice-p19-appunti-prodotto-scalare-energia.png|480]]

Si sviluppa $\langle u_p,v_p\rangle$ con la (17). I termini misti si annullano per l'ortogonalità (18); restano $2\int u_cv_c\cos^2(2\pi f_ct)$ e $2\int u_sv_s\sin^2(2\pi f_ct)$, che con $\cos^2=\frac{1+\cos(4\pi f_ct)}2$, $\sin^2=\frac{1-\cos(4\pi f_ct)}2$ danno $\int u_cv_c+\int u_sv_s$ più integrali in $\cos(4\pi f_ct)$ che valgono circa 0 («le aree positive vengono bilanciate da quelle negative, poiché $B/f_c\ll1$»). Infine $\text{Re}\{\int[u_c+ju_s][v_c-jv_s]\,dt\}=\text{Re}\{\langle u,v\rangle\}$, cioè la (19); la (20) segue con $u=v=s$.

*(Nelle note della p. 17 la somma $x_c+x_s$ andrebbe scritta $x_c-x_s$, per il segno della (17); per l'ortogonalità non cambia nulla.)*

### Upconversion e downconversion · [[Rappresentazione_Rice.pdf#page=20|p. 20]], [[Rappresentazione_Rice.pdf#page=21|21]]

![[rappresentazione-rice-p20-upconversion-downconversion.png|520]]

- **Upconversion** (banda base → banda passante): la (17) dice «immediatamente» come farla. $s_c$ è moltiplicato per $\sqrt2\cos(2\pi f_ct)$, $s_s$ per $-\sqrt2\sin(2\pi f_ct)$ e i due rami si sommano.
- **Downconversion** (banda passante → banda base): si considera il prodotto

$$\sqrt2\,s_p(t)\cos(2\pi f_ct)=2s_c\cos^2(2\pi f_ct)-2s_s\sin(2\pi f_ct)\cos(2\pi f_ct)=s_c(t)+s_c(t)\cos(4\pi f_ct)-s_s(t)\sin(4\pi f_ct)\tag{21}$$

  Con un **filtro passa-basso** (i due termini a $2f_c$ sono «tagliati dal filtro») si recupera la componente I. Analogamente la componente Q si ottiene filtrando passa-basso $-\sqrt2\,s_p(t)\sin(2\pi f_ct)$: infatti $-\sqrt2s_p\sin\alpha=s_s-s_s\cos2\alpha-s_c\sin2\alpha$.
- Note a mano: S → $s(n)$ → MOD → ($s_c$, $s_s$); «dal modulatore esce l'inviluppo».

![[grafico-rice-requisito-passabasso.png|480]]
*Figura di supporto: posizione in banda del requisito sul passa-basso. Dopo il moltiplicatore la banda utile occupa $\lvert f\rvert<W$ ($W$ = banda di $s_c$, $s_s$) e le copie occupano $\lvert f\mp2f_c\rvert<W$; il taglio $f_{LP}$ deve stare in $W\le f_{LP}\le2f_c-W$ ((a) corretto; (b) $f_{LP}<W$ taglia il segnale; (c) $f_{LP}>2f_c-W$ lascia passare le copie).*

![[grafico-rice-up-down-frequenza.png|520]]
*Figura di supporto: up/down in frequenza con un $S(f)$ asimmetrico (quindi $s(t)$ complesso). Upconversion = (14); downconversion = tre copie ($\pm2f_c$ e una in banda base), il passa-basso lascia solo $[S(f)+S^\ast(-f)]/2$, trasformata di $\text{Re}\{s\}=s_c$.*

**Catena unica (appunti p. 21):** S → MOD → upconverter → canale fisico → downconverter → DEMOD → utente. I tre blocchi centrali sono modellati come **un unico canale**. «Con tutti i passaggi fatti si conserva l'energia?» — «Sì, per le accortezze fatte ($\sqrt2$).»

![[rappresentazione-rice-p21-appunti-canale-equivalente.png|480]]

### Cosa porta l'inviluppo · [[Rappresentazione_Rice.pdf#page=22|p. 22]]

La rappresentazione complessa in banda base corrisponde a ricavare le variazioni «lente» di ampiezza e fase indotte dalla modulazione in banda base, **eliminando** la rapida variazione di fase prevedibile dovuta alla portante $f_c$. Poiché quella variazione è prevedibile, non porta informazione: **l'informazione di un segnale passa-banda è interamente contenuta nel suo inviluppo complesso**. Nota: l'inviluppo permette di separare le variazioni lente dovute alla modulazione. (Forma ampiezza-fase: con $s=a\,e^{j\theta}$, $s_p=\sqrt2\,a(t)\cos(2\pi f_ct+\theta(t))$.)

### Filtraggio passa-banda in banda base · [[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]

**Qualunque filtro passa-banda si può realizzare in banda base complessa.** Sia $y_p(t)=s_p(t)\ast h_p(t)$ l'uscita di un filtro passa-banda di risposta impulsiva $h_p(t)$; siano $s(t)$, $h(t)$, $y(t)$ gli inviluppi complessi di $s_p$, $h_p$, $y_p$ rispetto a un **riferimento di frequenza comune** $f_c$, e $S$, $H$, $Y$ le loro trasformate. In frequenza $Y_p(f)=S_p(f)H_p(f)$; sui segmenti a frequenze positive $Y_p^+=\sqrt2Y_pu$, $S_p^+=\sqrt2S_pu$, $H_p^+=\sqrt2H_pu$.

**Catena (appunti p. 24):**

$$
\begin{aligned}
Y(f)&=Y_p^+(f+f_c)=\sqrt2\,Y_p(f+f_c)\,u(f+f_c)&&\text{(13) e (3)}\\
&=\sqrt2\,S_p(f+f_c)H_p(f+f_c)\,u^2(f+f_c)&&\text{«sostituisco l'uscita»; }u^2=u\text{ «non altera nulla»}\\
&=\frac1{\sqrt2}\big[\sqrt2\,S_p(f+f_c)u(f+f_c)\big]\big[\sqrt2\,H_p(f+f_c)u(f+f_c)\big]&&\text{moltiplico e divido per }\sqrt2\text{; }\tfrac1{\sqrt2}\text{ «resta fuori»}\\
&=\frac1{\sqrt2}\,S(f)\,H(f)&&\text{(13) per }s\text{ e }h
\end{aligned}
\tag{22}
$$

Nel tempo (prodotto → convoluzione):

$$y(t)=\frac1{\sqrt2}\,s(t)\ast h(t)\tag{23}$$

![[rappresentazione-rice-p24-appunti-filtro-equivalente.png|480]]

![[rappresentazione-rice-p25-filtraggio-spettri.png|520]]
*A sinistra, in banda passante: $H_p(f)$ rettangoli di altezza $A$ attorno a $\pm f_c$, $S_p(f)$ triangoli di altezza $B$, $Y_p(f)$ di altezza $AB$. A destra, in banda base: $H$ di altezza $\sqrt2A$, $S$ di altezza $\sqrt2B$, $Y$ di altezza $\sqrt2AB$ (coerente con la (22)).*

In termini di componenti I e Q ($s=s_c+js_s$, $h=h_c+jh_s$, la convoluzione si sviluppa come un prodotto):

$$y_c(t)=\frac1{\sqrt2}\big[s_c(t)\ast h_c(t)-s_s(t)\ast h_s(t)\big]\tag{24}$$

$$y_s(t)=\frac1{\sqrt2}\big[s_s(t)\ast h_c(t)+s_c(t)\ast h_s(t)\big]\tag{25}$$

![[rappresentazione-rice-p26-filtro-banda-base-iq.png|520]]
*Realizzazione in banda base: $s_p$ entra nel downconverter che produce $s_c$, $s_s$; il riquadro «operazioni reali in banda base» contiene quattro filtri reali ($h_c$, $h_s$ per ciascuna componente) e due sommatori ($y_c$ con il meno); le uscite formano $y(t)=y_c+jy_s$, «segnale in banda base», che va a un DSP in banda base. (Nella figura manca il fattore $1/\sqrt2$, presente nella nota a mano.)*

### Banda di un segnale complesso · [[Rappresentazione_Rice.pdf#page=27|p. 27]]

L'occupazione spettrale di un segnale fisico a valori reali è la più piccola banda di frequenze **positive** che ne contiene la maggior parte ($S(-f)=S^\ast(f)$). Per i segnali complessi in banda base l'informazione sta sia nelle frequenze positive sia in quelle negative: l'occupazione spettrale è la più piccola banda **attorno all'origine** che contiene la maggior parte del segnale (frequenze positive e negative).

*Approfondimenti nel wiki: [[modulazione-digitale]], [[segnali-banda-base-e-passa-banda]], [[segnale-analitico]], [[inviluppo-complesso]], [[upconversion-e-downconversion]], [[equivalente-banda-base-dei-filtri]] (derivazioni estese, esempi e grafici).*


## Lezione 5 — Processi aleatori

*Fonte: random_processes.pdf, 46 pagine (41 slide, 5 pagine di appunti a mano alle p. 3, 4, 5, 8, 10, e una nota a mano sulla slide 5, p. 9). Le slide 33, 40 e 41 sono quelle della versione aggiornata dalla docente (random_processes_v2.pdf). Corrispondenza: slide 1–2 = p. 1–2, slide 3 = p. 6, slide 4 = p. 7, slide 5 = p. 9, dalla slide 6 in poi pagina = slide + 5.*

### Introduzione ai processi aleatori

#### Slide 2 — Introduzione · [[random_processes.pdf#page=2|p. 2]]
- Un **processo stocastico** (o processo aleatorio, o segnale aleatorio) è l'estensione naturale del concetto di variabile aleatoria quando si trattano **segnali**.
- In molte situazioni l'ipotesi di segnale deterministico non regge, ed è più appropriato modellare i segnali come funzioni aleatorie. Esempi: il rumore termico nei circuiti elettronici; i segnali generati da una sorgente di informazione.
- **Esempio.** $\Omega = \{0, 1\}$ con $P(\{\omega = 1\}) \triangleq p$ e $P(\{\omega = 0\}) \triangleq q = 1 - p$. Il segnale aleatorio è

$$X(t, \omega) = \begin{cases} A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 0 \\[2mm] -A\,\text{rect}\Big(\dfrac{t - 0.5T}{T}\Big), & \omega = 1 \end{cases}$$

![[random-processes-p2-esempio-rect.png|520]]
*Le due realizzazioni: $x(t, \omega = 0)$ vale $A$ per $0 < t < T$, $x(t, \omega = 1)$ vale $-A$ nello stesso intervallo.*

#### Appunti — Dal segnale deterministico al processo · [[random_processes.pdf#page=3|p. 3]]
- Un segnale $s(t)$ descritto nel dominio del tempo, con una descrizione analitica o con un grafico, è un **segnale deterministico**. «Prendiamo questi segnali e li estendiamo su fenomeni non predicibili a priori».
- Una variabile aleatoria associa a ogni esito un numero: $X: \omega \to X(\omega) \in \mathbb{R}$.
- In un processo, a ogni esito $\omega_i$ si associa non un numero ma una **funzione del tempo** $S(\omega_i, t)$.

![[random-processes-p3-appunti-da-va-a-processo.png|520]]

#### Appunti — Sinusoide a fase casuale; fissare $\omega$ o $t$ · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|p. 5]]
- Esempio: $X(t) = A\cos(2\pi f_0 t + \Theta)$, con $A$ e $f_0$ deterministiche e $\Theta \sim \mathcal{U}(0, 2\pi)$. È un «segnale aleatorio ad ampiezza continua».
- $X(t, \omega)$ «si particolarizza» a seconda che si fissi $\omega$ o $t$:
  - fisso $\omega = \bar\omega$: $X(t, \bar\omega) = x(t)$, un **segnale nel tempo**;
  - fisso $t = \bar t$: $X(\bar t, \omega) = X(\omega)$, una **variabile aleatoria**;
  - fisso entrambi: un **numero**.
- Tempo continuo: $X(t, \omega)$ con $t \in \mathbb{R}$. Tempo discreto: $X(n, \omega)$ con $n \in \mathbb{Z}$.
- Due punti di vista: una collezione di variabili aleatorie indicizzate rispetto al tempo (il secondo è la collezione di forme d'onda, p. 6).

![[random-processes-p4-appunti-sinusoide-fase-casuale.png|520]]

#### Slide 3 — Definizione di processo stocastico (1/2) · [[random_processes.pdf#page=6|p. 6]]
- Un processo $X(t, \omega)$ si può vedere come una **collezione di segnali nel tempo** (dette *realizzazioni* o *sample functions*), corrispondenti ai diversi esiti di un esperimento aleatorio.
  - A ogni esito $\omega = \omega_i$ nello spazio di probabilità $(\Omega, \mathcal{S}, P)$ corrisponde un segnale deterministico $X(t, \omega_i) \equiv x_i(t)$ (descrizione analoga a quella delle variabili aleatorie).
  - Fissato un istante $t_0$, la funzione $X(t_0, \omega)$ è una **variabile aleatoria**.
  - Per ogni $t_0$ e ogni $\omega_i \in \Omega$, $X(t_0, \omega_i)$ è un **numero**.
- In alternativa, un processo è una **collezione di variabili aleatorie indicizzate nel tempo**.
  - Se l'insieme degli indici è $\mathbb{R}$: processo **a tempo continuo**.
  - Se è $\mathbb{Z}$: processo **a tempo discreto**, cioè una successione di variabili aleatorie $\{X_i\}_{i=-\infty}^{+\infty}$.
  - Questo punto di vista è adatto allo sviluppo matematico della teoria.
- Per semplicità si omette $\omega$ e si scrive $X(t)$ (o $x(t)$ se non c'è ambiguità).

#### Slide 4 — Definizione di processo stocastico (2/2) · [[random_processes.pdf#page=7|p. 7]]
- In una variabile aleatoria l'esito di un esperimento è associato a un **numero**. In un processo stocastico è associato a una **forma d'onda**, funzione del tempo.

![[random-processes-p7-realizzazioni.png|520]]
*Lo spazio campione $S$ con gli esiti $s_1, s_2, \dots, s_n$; ogni esito dà una forma d'onda $x_1(t), \dots, x_n(t)$ su $(-T, +T)$. Una verticale in $t_k$ taglia le forme d'onda nei valori $x_1(t_k), \dots, x_n(t_k)$, cioè i valori della variabile aleatoria $X(t_k)$.*

### Caratterizzazione statistica completa

#### Appunti — CDF del primo e del secondo ordine · [[random_processes.pdf#page=8|p. 8]]
- $X(t)$: processo a tempo continuo e ampiezza continua. Per $t = t_1$, $X(t_1)$ è una variabile aleatoria, con CDF $F_{X(t_1)}(x) \triangleq P(\{X(t_1) \le x\})$ per ogni $x$ e ogni $t_1$. Se la si conosce, si ha la **CDF del primo ordine**.
- Campionando in due istanti, $X(t_1)$ e $X(t_2)$ sono una coppia di variabili aleatorie con CDF congiunta $F_{X(t_1)X(t_2)}(x_1, x_2) = P(\{X(t_1) \le x_1, X(t_2) \le x_2\})$. Se la si conosce per ogni $t_1, t_2$, si ha la **CDF del secondo ordine**.
- Nota: negli appunti compare $\forall t_1 \in \mathbb{Z}$, da leggere $t_1 \in \mathbb{R}$ (tempo continuo).

![[random-processes-p8-appunti-cdf-primo-secondo-ordine.png|520]]

#### Slide 5 — Distribuzioni congiunte dei campioni temporali (1/2) · [[random_processes.pdf#page=9|p. 9]]
- La descrizione statistica di un processo si basa sulla CDF (o, equivalentemente, sulla pdf) di **vettori** di campioni del segnale aleatorio.
- $X(t_1), \dots, X(t_k)$ sono le variabili aleatorie ottenute campionando $X(t)$ negli istanti $t_1, \dots, t_k$. Per $(x_1, \dots, x_k) \in \mathbb{R}^k$, la **CDF congiunta** è

$$F_{X(t_1),\dots,X(t_k)}(x_1, \dots, x_k) \triangleq P[X(t_1) \le x_1, \dots, X(t_k) \le x_k] \tag{1}$$

  e la **pdf congiunta** è

$$f_{X(t_1),\dots,X(t_k)}(x_1, \dots, x_k) \triangleq \frac{\partial^k}{\partial x_1\,\partial x_2 \cdots \partial x_k}\,F_{X(t_1),\dots,X(t_k)}(x_1, \dots, x_k) \tag{2}$$

- Se si conosce la CDF congiunta (1), o la pdf (2), per **qualunque scelta** degli istanti $t_1, \dots, t_k$, si dice che si conosce la **caratterizzazione statistica di ordine $k$** del processo.
- Nota a mano: integrando rispetto a una variabile si ottiene la pdf del primo ordine, $\int_{-\infty}^{+\infty} f_{X(t_1)X(t_2)}(x_1, x_2)\,dx_2 = f_{X(t_1)}(x_1)$.
- Refusi della slide: nella (2) la derivata è scritta $\partial^n$ (corretta a mano in $\partial^k$); il rimando è alla «CDF congiunta (36)» invece che alla (1).

![[random-processes-p9-marginalizzazione.png|520]]

#### Appunti — Il processo di Bernoulli: DF del primo e del secondo ordine · [[random_processes.pdf#page=10|p. 10]]
- Per processi aleatori discreti a tempo discreto si usa la **DF** (distribuzione di probabilità).
- **Primo ordine:** $p_{X(n)}(x) \triangleq P(X(n) = x) = p^{x}\,q^{1-x}$, con $x \in \{0, 1\}$.
- **Secondo ordine:** $p_{X(n_1)X(n_2)}(x_1, x_2) \triangleq P(\{X(n_1) = x_1, X(n_2) = x_2\}) = p^{w(\mathbf{x})}\,q^{2 - w(\mathbf{x})}$, dove $\mathbf{x} = (x_1, x_2)$ e $w(\mathbf{x})$ è il **numero di 1 contenuti nel vettore**, supponendo che i lanci siano statisticamente indipendenti.

![[random-processes-p10-appunti-processo-bernoulli.png|520]]

#### Slide 6 — Distribuzioni congiunte dei campioni temporali (2/2) · [[random_processes.pdf#page=11|p. 11]]
- Un processo è **completamente caratterizzato** se la CDF congiunta di ordine $k$ (o la pdf) è nota per ogni $k \in \mathbb{N}$ e ogni scelta degli istanti $t_1, \dots, t_k$.
- La collezione di CDF e pdf deve essere **coerente**: quelle di ordine inferiore si ottengono come **marginali** di quelle di ordine superiore.
- Finora l'ampiezza di $X(t)$ è stata supposta continua. Se è **discreta**, conviene usare la distribuzione di probabilità (DF). Esempio: il processo di Bernoulli.
- La caratterizzazione completa è difficile da ottenere in molti casi pratici ⇒ si usa la **caratterizzazione statistica parziale**.

### Caratterizzazione statistica parziale

#### Slide 7 — Media di un processo · [[random_processes.pdf#page=12|p. 12]]
- Per un processo reale $X(t)$, la **media** è il valore atteso della variabile aleatoria ottenuta campionando il processo in $t$:

$$\mu_X(t) \triangleq E[X(t)] = \int_{-\infty}^{+\infty} x\,f_{X(t)}(x)\,dx \tag{3}$$

  con $f_{X(t)}(x)$ pdf del primo ordine. In generale $\mu_X(t)$ è funzione del tempo.

#### Slide 8 — Funzione di correlazione · [[random_processes.pdf#page=13|p. 13]]
- La **funzione di autocorrelazione** (acf) è il valore atteso del prodotto di due variabili aleatorie, $X(t_1)$ e $X(t_2)$:

$$R_{XX}(t_1, t_2) \triangleq E[X(t_1)X(t_2)] = \int_{-\infty}^{+\infty}\!\!\int_{-\infty}^{+\infty} x_1 x_2\,f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_1\,dx_2 \tag{4}$$

  con $f_{X(t_1),X(t_2)}$ pdf del secondo ordine. In generale dipende da $t_1$ e $t_2$ separatamente.

#### Slide 9 — Funzione di covarianza · [[random_processes.pdf#page=14|p. 14]]
- La **autocovarianza** è

$$
\begin{aligned}
C_{XX}(t_1, t_2) &\triangleq E\{[X(t_1) - \mu_X(t_1)][X(t_2) - \mu_X(t_2)]\} \\
&= \iint [x_1 - \mu_X(t_1)][x_2 - \mu_X(t_2)]\,f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_1\,dx_2 \\
&= R_{XX}(t_1, t_2) - \mu_X(t_1)\,\mu_X(t_2)
\end{aligned} \tag{5}
$$

- Se media e acf sono note, si ricava l'autocovarianza. In generale dipende da $t_1$ e $t_2$ separatamente.

### Processi stazionari

#### Slide 10 — Processi stazionari (1/3) · [[random_processes.pdf#page=15|p. 15]]
- In generale la caratterizzazione statistica di un processo cambia nel tempo. Se le proprietà statistiche non sono influenzate, in qualche misura, dalla scelta dell'origine dei tempi, il processo si dice **stazionario in qualche senso**. Si definiscono diverse forme di stazionarietà.
- Sia $X(t)$ un processo iniziato in $t = -\infty$, campionato in $t_1, \dots, t_k$, con CDF di ordine $k$ $F_{X(t_1),\dots,X(t_k)}(x_1, \dots, x_k)$.
- Si traslano tutti gli istanti di campionamento di una quantità fissa $\tau$ (traslazione temporale): le variabili $X(t_1 + \tau), \dots, X(t_k + \tau)$ hanno CDF $F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1, \dots, x_k)$.

#### Slide 11 — Processi stazionari (2/3) · [[random_processes.pdf#page=16|p. 16]]
- $X(t)$ è **stazionario di ordine $k$** se

$$F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1, \dots, x_k) = F_{X(t_1),\dots,X(t_k)}(x_1, \dots, x_k) \tag{6}$$

  per ogni traslazione $\tau$ e ogni scelta di $t_1, \dots, t_k$.
- $X(t)$ è **stazionario in senso stretto** (SSS) se la (6) vale per ogni $k \in \mathbb{N}$: è la forma più forte. Spesso bastano forme più deboli.
- **Stazionario del primo ordine**: la (6) vale per $k = 1$. Con $\tau = -t$ si ha $F_{X(t)}(x) = F_{X(t+\tau)}(x) = F_{X(0)}(x)$ per ogni $t \in \mathbb{R}$ ⇒ la distribuzione del primo ordine **non dipende dal tempo**.
- Per un processo stazionario del primo ordine la media è costante:

$$\mu_X(t) = \int_{-\infty}^{+\infty} x\,f_{X(t)}(x)\,dx = \int_{-\infty}^{+\infty} x\,f_{X(0)}(x)\,dx \equiv \mu_X, \quad \forall t \in \mathbb{R}$$

#### Slide 12 — Processi stazionari (3/3) · [[random_processes.pdf#page=17|p. 17]]
- **Stazionario del secondo ordine**: la (6) vale per $k = 2$. Con $\tau = -t_2$:

$$F_{X(t_1),X(t_2)}(x_1, x_2) = F_{X(t_1+\tau),X(t_2+\tau)}(x_1, x_2) = F_{X(t_1-t_2),X(0)}(x_1, x_2)$$

  La distribuzione del secondo ordine dipende **solo dalla differenza** tra gli istanti di campionamento, non dagli istanti particolari.
- Per un processo stazionario del secondo ordine, $f_{X(t_1),X(t_2)}(x_1, x_2)$ dipende solo da $t_1 - t_2$ e quindi anche

$$R_{XX}(t_1, t_2) \equiv R_{XX}(t_1 - t_2), \quad \forall (t_1, t_2) \in \mathbb{R}^2$$

- Se un processo è stazionario di ordine $k$, lo è anche di ordine $k-1$, $k-2$, e così via (il viceversa non vale in generale).

#### Slide 13 — Processi stazionari in senso lato · [[random_processes.pdf#page=18|p. 18]]
- Un'altra classe importante è quella dei processi **stazionari in senso lato** (WSS, *wide-sense stationary*, o debolmente stazionari). $X(t)$ è WSS se valgono due condizioni:
  1. la **media** è costante per ogni $t$;
  2. la **acf** dipende solo dalla differenza tra due istanti di campionamento.
- Stazionarietà in senso stretto ⇒ stazionarietà in senso lato.

### Funzione di autocorrelazione dei processi WSS

#### Slide 14 — Proprietà della acf (1/2) · [[random_processes.pdf#page=19|p. 19]]
- Per un processo WSS la acf si può scrivere come **lag-acf**:

$$R_{XX}(\tau) \triangleq E[X(t)\,X(t - \tau)], \quad \forall \tau \in \mathbb{R} \tag{7}$$

  dove $\tau$ è il **lag**, l'intervallo tra i campioni in $t_1 = t$ e $t_2 = t_1 - \tau$.
- Proprietà:
  1. il valore quadratico medio si ottiene ponendo $\tau = 0$: $R_{XX}(0) = E[X^2(t)]$;
  2. $R_{XX}(\tau)$ è una funzione **pari**: $R_{XX}(-\tau) = R_{XX}(\tau)$;
  3. $R_{XX}(\tau)$ ha il massimo in modulo in $\tau = 0$: $\lvert R_{XX}(\tau)\rvert \le R_{XX}(0)$.
- Acf **normalizzata**:

$$\rho_{XX}(\tau) \triangleq \frac{R_{XX}(\tau)}{R_{XX}(0)} \tag{8}$$

  con valori in $[-1, 1]$, cioè $\lvert\rho_{XX}(\tau)\rvert \le 1$.

#### Slide 15 — Significato fisico della acf (1/2) · [[random_processes.pdf#page=20|p. 20]]
- $R_{XX}(\tau)$ descrive l'interdipendenza di due variabili aleatorie ottenute campionando $X(t)$ a $\tau$ secondi di distanza.
- Più rapidamente $X(t)$ cambia nel tempo, più rapidamente $R_{XX}(\tau)$ decresce dal massimo $R_{XX}(0)$ al crescere di $\tau$.
- Questo comportamento si caratterizza con un **tempo di decorrelazione** $\tau_{dec}$: per $\tau > \tau_{dec}$, il modulo di $R_{XX}(\tau)$ resta sotto un valore prescritto.

#### Slide 16 — Significato fisico della acf (2/2) · [[random_processes.pdf#page=21|p. 21]]
![[random-processes-p21-autocorrelazione-lento-veloce.png|520]]
*Acf di processi che fluttuano lentamente e rapidamente: nel primo caso la acf decresce lentamente da $R_{XX}(0)$ (tempo di decorrelazione lungo), nel secondo rapidamente.*

### Funzioni di correlazione incrociata

#### Slide 17 — Crosscorrelazione · [[random_processes.pdf#page=22|p. 22]]
- Per due processi reali $X(t)$ e $Y(t)$, con acf $R_{XX}(t, \tau)$ e $R_{YY}(t, \tau)$, si definiscono le **lag-crosscorrelazioni**

$$R_{XY}(t, \tau) \triangleq E[X(t)\,Y(t - \tau)], \qquad R_{YX}(t, \tau) \triangleq E[Y(t)\,X(t - \tau)] \tag{9}$$

  che dipendono dall'**ordine** dei due processi.
- $X(t)$ e $Y(t)$ sono **congiuntamente WSS** se ciascuno è WSS e, in più, $R_{XY}(t, \tau) \equiv R_{XY}(\tau)$.
- In generale la crosscorrelazione **non è pari** in $\tau$ e **non ha il massimo nell'origine**, ma vale $R_{XY}(\tau) = R_{YX}(-\tau)$.

#### Slide 18 — Crosscovarianza · [[random_processes.pdf#page=23|p. 23]]
- Per due processi con autocovarianze $C_{XX}(\tau)$ e $C_{YY}(\tau)$, la **lag-crosscovarianza** è

$$C_{XY}(t, \tau) \triangleq E\{[X(t) - \mu_X(t)][Y(t - \tau) - \mu_Y(t - \tau)]\} \tag{10}$$

$$C_{YX}(t, \tau) \triangleq E\{[Y(t) - \mu_Y(t)][X(t - \tau) - \mu_X(t - \tau)]\} \tag{11}$$

  e dipende dall'ordine dei due processi.
- A media nulla ($\mu_X(t) = \mu_Y(t) = 0$): $C_{XY}(t, \tau) = R_{XY}(t, \tau)$ e $C_{YX}(t, \tau) = R_{YX}(t, \tau)$.
- Se sono congiuntamente WSS, $C_{XY}(t, \tau) = C_{XY}(\tau)$.

#### Slide 19 — Processi indipendenti, incoerenti, incorrelati · [[random_processes.pdf#page=24|p. 24]]
- **Indipendenti**: gli insiemi $\{X(t_1), \dots, X(t_k)\}$ e $\{Y(t'_1), \dots, Y(t'_j)\}$ sono indipendenti per ogni $k, j \in \mathbb{N}$ e per ogni scelta di $t_1, \dots, t_k$ e $t'_1, \dots, t'_j$.
- **Incoerenti**: $R_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$.
- **Incorrelati**: $C_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$.
- Si può dimostrare che se $X(t)$ e $Y(t)$ sono indipendenti, allora sono incorrelati. Se $\mu_X = \mu_Y = 0$, incoerenza e incorrelazione sono equivalenti.

### Processi complessi

#### Slide 20 — Processi stocastici complessi · [[random_processes.pdf#page=25|p. 25]]
- Un processo complesso si rappresenta come $Z(t) = X(t) + jY(t)$. La caratterizzazione statistica **completa** si ottiene dalla caratterizzazione congiunta di parte reale $X(t)$ e parte immaginaria $Y(t)$.
- Per la caratterizzazione **parziale**:

$$\mu_Z(t) \triangleq E[Z(t)] = E[X(t) + jY(t)] = \mu_X(t) + j\mu_Y(t) \tag{12}$$

$$R_{ZZ}(t_1, t_2) \triangleq E[Z(t_1)\,Z^\ast(t_2)] \quad \text{ovvero} \quad R_{ZZ}(t, \tau) \triangleq E[Z(t)\,Z^\ast(t - \tau)] \tag{13}$$

  con $Z^\ast$ il complesso coniugato di $Z$.
- A rigore servirebbe un altro momento del secondo ordine, la **acf coniugata** $R_{ZZ^\ast}(t_1, t_2) \triangleq E[Z(t_1)\,Z(t_2)]$, che però è nulla per la maggior parte dei processi.

### Trasmissione di un processo attraverso un filtro LTI

#### Slide 21 — Trasmissione di un processo WSS attraverso un filtro LTI · [[random_processes.pdf#page=26|p. 26]]
- $X(t)$ è l'ingresso di un filtro lineare tempo-invariante (LTI) deterministico, con risposta impulsiva $h(t)$; $Y(t)$ è l'uscita stocastica:

$$Y(t) = \int_{-\infty}^{+\infty} h(\tau_1)\,X(t - \tau_1)\,d\tau_1$$

- In generale è difficile ricavare la distribuzione di $Y(t)$, anche se si conosce quella di $X(t)$. Spesso basta calcolare media e acf di $Y(t)$ in funzione di quelle di $X(t)$, supponendo $X(t)$ WSS.

![[random-processes-p26-filtro-lti.png|420]]

#### Slide 22 — Media dell'uscita (1/2) · [[random_processes.pdf#page=27|p. 27]]
- $\mu_Y(t) = E[Y(t)] = E\Big[\int h(\tau_1)\,X(t - \tau_1)\,d\tau_1\Big]$ (14).
- Se $E[X(t)]$ è finito per ogni $t$ e il filtro è stabile, si scambiano valore atteso e integrale:

$$\mu_Y(t) = \int_{-\infty}^{+\infty} h(\tau_1)\,E[X(t - \tau_1)]\,d\tau_1 = \int h(\tau_1)\,\mu_X(t - \tau_1)\,d\tau_1 = \mu_X(t) \ast h(t) \tag{15}$$

  La media dell'uscita è la **convoluzione** tra la media dell'ingresso e la risposta impulsiva.

#### Slide 23 — Media dell'uscita (2/2) · [[random_processes.pdf#page=28|p. 28]]
- Con ingresso WSS, $\mu_X(t) \equiv \mu_X$:

$$\mu_Y(t) \equiv \mu_Y = \mu_X \int_{-\infty}^{+\infty} h(\tau_1)\,d\tau_1 = \mu_X\,H(0) \tag{16}$$

  $H(0)$ è la risposta del sistema a frequenza zero.
- La media dell'uscita di un filtro LTI con ingresso WSS è la media dell'ingresso moltiplicata per la risposta a frequenza zero del filtro.

#### Slide 24 — Funzioni di correlazione delle uscite di un sistema LTI (1/3) · [[random_processes.pdf#page=29|p. 29]]
- Si calcola la crosscorrelazione delle due uscite $Y_1(t)$ e $Y_2(t)$ di un sistema LTI, $R_{Y_1Y_2}(t_1, t_2) = E[Y_1(t_1)\,Y_2(t_2)]$.
- Con la relazione ingresso-uscita e scambiando l'ordine di integrazione (se possibile):

$$R_{Y_1Y_2}(t_1, t_2) = E\Big[\int h_1(\tau_1)X_1(t_1 - \tau_1)\,d\tau_1\int h_2(\tau_2)X_2(t_2 - \tau_2)\,d\tau_2\Big] \tag{17}$$

$$= \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1\,d\tau_2 \tag{18}$$

![[random-processes-p29-due-sistemi-lti.png|420]]

#### Slide 25 — Funzioni di correlazione delle uscite di un sistema LTI (2/3) · [[random_processes.pdf#page=30|p. 30]]
- Se $X_1(t)$ e $X_2(t)$ sono congiuntamente WSS, la crosscorrelazione dipende solo dalla differenza tra $t_1 - \tau_1$ e $t_2 - \tau_2$. Ponendo $\tau = t_1 - t_2$ nella (18):

$$R_{Y_1Y_2}(\tau) = \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_1\,d\tau_2 \tag{19}$$

$$= R_{X_1X_2}(\tau) \ast h_1(\tau) \ast h_2(-\tau) = R_{X_1X_2}(\tau) \ast r_{h_1h_2}(\tau) \tag{20}$$

  che dipende solo dal lag $\tau$. ($r_{h_1h_2}(\tau) = h_1(\tau) \ast h_2(-\tau)$.)
- Se i due ingressi sono **incoerenti**, lo sono anche le uscite: l'elaborazione LTI **preserva l'incoerenza** (la slide scrive «saves incoherence»).

#### Slide 26 — Funzioni di correlazione delle uscite di un sistema LTI (3/3) · [[random_processes.pdf#page=31|p. 31]]
- Particolarizzando la (18) a $h_1 = h_2 = h$ e $X_1 = X_2 = X$:

$$R_{YY}(t_1, t_2) = \iint h(\tau_1)\,h(\tau_2)\,R_{XX}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1\,d\tau_2$$

- Se $X(t)$ è WSS: $R_{YY}(\tau) = R_{XX}(\tau) \ast h(\tau) \ast h(-\tau) = R_{XX}(\tau) \ast r_{hh}(\tau)$.
- **Se l'ingresso di un sistema LTI stabile è WSS, anche l'uscita è WSS.**
- Dalle (18) e (20) si ricavano anche $R_{YX}(\tau)$ e $R_{XY}(\tau)$: ponendo $Y_1 = Y$, $Y_2 = X$, $h_1 = h$, $h_2 = \delta$ si ha $R_{YX}(\tau) = R_{XX}(\tau) \ast h(\tau)$. Analogamente $R_{XY}(\tau) = R_{XX}(\tau) \ast h(-\tau)$.

### Densità spettrale di potenza

#### Slide 27 — Densità spettrale di potenza (PSD) · [[random_processes.pdf#page=32|p. 32]]
- La **PSD** di $X(t)$ è

$$S_{XX}(f) \triangleq \lim_{T \to +\infty} \frac{1}{2T}\,E\big[\lvert X_T(f)\rvert^2\big]$$

  dove $X_T(f)$ è la trasformata di Fourier della versione finestrata $X_T(t) = X(t)\,\text{rect}[t/(2T)]$.
- Si può dimostrare che la PSD di un processo WSS è la **trasformata di Fourier della sua acf** $R_{XX}(\tau)$: è la **relazione di Wiener-Khinchin**.
- Il valore quadratico medio, cioè la potenza $P_X$ del processo WSS:

$$E[X^2(t)] = R_{XX}(0) = \int_{-\infty}^{+\infty} S_{XX}(f)\,df = P_X \tag{21}$$

#### Slide 28 — PSD e sistemi LTI · [[random_processes.pdf#page=33|p. 33]]
- Sia $S_{YY}(f)$ la PSD dell'uscita $Y(t)$ di un filtro con risposta in frequenza $H(f)$ e ingresso WSS $X(t)$. Dalla relazione di Wiener-Khinchin e da $R_{YY}(\tau) = R_{XX}(\tau) \ast h(\tau) \ast h(-\tau)$:

$$S_{YY}(f) = S_{XX}(f)\,\lvert H(f)\rvert^2 \tag{22}$$

- La PSD dell'uscita è la PSD dell'ingresso moltiplicata per il modulo quadro della risposta in frequenza del filtro.

#### Slide 29–30 — Significato fisico della PSD · [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=35|p. 35]]
- Si fa passare il processo WSS $X(t)$ in un **filtro ideale a banda stretta**, con $\lvert H(f)\rvert$ centrato in $f_c$ e banda $\Delta f$.
- Dalla (22), se $\Delta f$ è sufficientemente piccola rispetto a $f_c$ e $S_{XX}(f)$ è continua, la potenza $\Delta P_X$ delle componenti di $X(t)$ nell'intervallo di lunghezza $2\Delta f$ è

$$\Delta P_X \approx (2\,\Delta f)\,S_{XX}(f), \quad \text{con } f_c \equiv f$$

- $S_{XX}(f)$ si misura in **watt per hertz** (W/Hz).

![[random-processes-p35-filtro-banda-stretta.png|420]]
*Risposta in modulo del filtro ideale a banda stretta: vale 1 in due finestre di larghezza $\Delta f$ centrate in $\pm f_c$.*

#### Slide 31–32 — Proprietà della PSD · [[random_processes.pdf#page=36|p. 36]], [[random_processes.pdf#page=37|p. 37]]
1. Il valore a frequenza zero di un processo WSS è l'area sotto la acf: $S_{XX}(0) = \int_{-\infty}^{+\infty} R_{XX}(\tau)\,d\tau$ (23).
2. Il valore quadratico medio è l'area sotto la PSD: $E[X^2(t)] = \int_{-\infty}^{+\infty} S_{XX}(f)\,df = R_{XX}(0)$ (24).
3. La PSD è non negativa: $S_{XX}(f) \ge 0$, per ogni $f \in \mathbb{R}$.
4. La PSD di un processo WSS **reale** è una funzione pari: $S_{XX}(-f) = S_{XX}(f)$.
5. La PSD opportunamente normalizzata ha le proprietà di una pdf:

$$p_{XX}(f) \triangleq \frac{S_{XX}(f)}{\int_{-\infty}^{+\infty} S_{XX}(f)\,df} \tag{25}$$

   con $p_{XX}(f) \ge 0$ per ogni $f$ e area totale unitaria.
- **Esempio (slide 32): calcolare la PSD di un segnale modulato linearmente.** La slide non svolge l'esempio. Ipotesi usate qui: $X(t) = \sum_n b[n]\,p(t - nT - D)$, con simboli a media nulla, incorrelati e di varianza $\sigma_b^2$, e ritardo $D$ uniforme in $[0, T)$ indipendente dai simboli. Allora $R_{XX}(\tau) = \frac{\sigma_b^2}{T}\,r_{pp}(\tau)$, il processo è WSS e

$$S_{XX}(f) = \frac{\sigma_b^2}{T}\,\lvert P(f)\rvert^2$$

  Con l'impulso rettangolare di durata $T$ e altezza 1 si ottiene $S_{XX}(f) = \sigma_b^2\,T\,\text{sinc}^2(fT)$.

#### Slide 33 — Densità spettrali mutue (versione aggiornata) · [[random_processes_v2.pdf#page=33|p. 33 (v2)]]
- La **cross-spectral density** caratterizza le relazioni tra due processi nel dominio della frequenza:

$$S_{XY}(f) \triangleq \lim_{T \to +\infty} \frac{1}{2T}\,E\big[X_T(f)\,Y_T^\ast(f)\big]$$

  con $X_T(f)$ e $Y_T(f)$ trasformate di Fourier delle versioni finestrate di $X(t)$ e $Y(t)$.
- Per due processi **congiuntamente WSS**, la cross-spectral density è la trasformata di Fourier della loro crosscorrelazione:

$$S_{XY}(f) = \int_{-\infty}^{+\infty} R_{XY}(\tau)\,e^{-j2\pi f\tau}\,d\tau \tag{26}$$

- A differenza della PSD, $S_{XY}(f)$ non è necessariamente reale né non negativa.
- Per processi **complessi** la relazione $R_{XY}(\tau) = R_{YX}(-\tau)$ si generalizza a $R_{XY}(\tau) = R_{YX}^\ast(-\tau)$, e quindi

$$S_{XY}(f) = S_{YX}^\ast(f)$$

  (nella versione precedente della slide, per processi reali: $S_{XY}(f) = S_{YX}(-f) = S_{YX}^\ast(f)$).

#### Slide 34–35 — Somma di due processi WSS · [[random_processes.pdf#page=39|p. 39]], [[random_processes.pdf#page=40|p. 40]]
- $X(t)$ e $Y(t)$ hanno media nulla e $Z(t) = X(t) + Y(t)$. Si cerca la PSD di $Z(t)$.
- L'acf di $Z(t)$:

$$R_{ZZ}(t_1, t_2) = E\{[X(t_1) + Y(t_1)][X(t_2) + Y(t_2)]\} = R_{XX} + R_{XY} + R_{YX} + R_{YY} \tag{27}$$

- Con $\tau = t_1 - t_2$ e stazionarietà congiunta:

$$R_{ZZ}(\tau) = R_{XX}(\tau) + R_{XY}(\tau) + R_{YX}(\tau) + R_{YY}(\tau) \tag{28}$$

- Trasformando: $S_{ZZ}(f) = S_{XX}(f) + S_{XY}(f) + S_{YX}(f) + S_{YY}(f)$ (29).
- Se $X(t)$ e $Y(t)$ sono WSS **incoerenti**, $R_{XY}(\tau) = R_{YX}(\tau) = 0$ per ogni $\tau$, quindi $S_{XY} = S_{YX} = 0$ e

$$S_{ZZ}(f) = S_{XX}(f) + S_{YY}(f) \tag{30}$$

- La PSD della somma di processi WSS incoerenti (o, equivalentemente, a media nulla e incorrelati) è la **somma delle PSD**.

### Il processo gaussiano

#### Slide 36 — Il processo gaussiano (1/3) · [[random_processes.pdf#page=41|p. 41]]
- Il processo gaussiano è il più frequente nello studio dei sistemi di comunicazione, per applicabilità pratica e trattabilità matematica.
- Si campiona $X(t)$ in $t_1, \dots, t_n$. Se il processo è gaussiano, le variabili $X(t_1), \dots, X(t_n)$ sono **congiuntamente gaussiane** per ogni $n$, con pdf di ordine $n$ completamente determinata dalle **medie** e dalle **covarianze**:

$$\mu_X(t_i) \triangleq E[X(t_i)], \quad i \in \{1, \dots, n\} \tag{31}$$

$$C_{XX}(t_k, t_i) \triangleq E\{[X(t_k) - \mu_X(t_k)][X(t_i) - \mu_X(t_i)]\}, \quad k, i \in \{1, \dots, n\} \tag{32}$$

- Sia $\mathbf{X} \triangleq [X(t_1), \dots, X(t_n)]^T$ il vettore aleatorio e $\mathbf{x} \triangleq [x_1, \dots, x_n]^T$ un suo valore ($^T$ indica la trasposizione).

#### Slide 37 — Il processo gaussiano (2/3) · [[random_processes.pdf#page=42|p. 42]]
- Il vettore $\mathbf{X}$ ha **distribuzione gaussiana multivariata**:

$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n \det(\boldsymbol{\Sigma})}}\;e^{-\frac12(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})} \tag{33}$$

  dove $\boldsymbol{\mu} \triangleq [\mu_X(t_1), \dots, \mu_X(t_n)]^T$ è il vettore delle medie, $\boldsymbol{\Sigma}$ la **matrice di covarianza** con elemento $\{\boldsymbol{\Sigma}\}_{k,i} = C_{XX}(t_k, t_i)$, e $\boldsymbol{\Sigma}^{-1}$ la sua inversa.
- $\boldsymbol{\Sigma}$ è **simmetrica** ($\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$) e **semidefinita positiva** ($\mathbf{u}^T\boldsymbol{\Sigma}\,\mathbf{u} \ge 0$ per ogni $\mathbf{u} \in \mathbb{R}^n$). Per un processo gaussiano non degenere è **definita positiva** ($\mathbf{u}^T\boldsymbol{\Sigma}\,\mathbf{u} > 0$ per ogni $\mathbf{u} \ne \mathbf{0}$), quindi invertibile.

#### Slide 38 — Il processo gaussiano (3/3) · [[random_processes.pdf#page=43|p. 43]]
- I processi prodotti da fenomeni fisici sono spesso tali che un modello gaussiano è appropriato; questo è confermato dagli esperimenti.
- Il **teorema del limite centrale** ne fornisce una giustificazione matematica.
- La frequenza con cui un modello gaussiano è adatto e la facilità di trattazione rendono il processo gaussiano molto importante nello studio dei sistemi di comunicazione.

#### Slide 39 — Proprietà dei processi gaussiani · [[random_processes.pdf#page=44|p. 44]]
- Se un processo gaussiano è applicato a un **filtro lineare stabile**, il processo in uscita è anch'esso gaussiano.
- Se un processo gaussiano è WSS, allora è anche **strettamente stazionario**.
- Se le variabili $X(t_1), \dots, X(t_n)$ sono **incorrelate**, cioè $C_{XX}(t_k, t_i) = 0$ per $k \ne i$, allora sono **statisticamente indipendenti**.
  - L'incorrelazione vuol dire che la matrice di covarianza è diagonale, $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \dots, \sigma_n^2)$, con $\sigma_i^2$ varianza di $X(t_i)$ ⇒ la pdf (33) si semplifica in

$$f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^{n} f_{X(t_i)}(x_i) \tag{34}$$

  - La pdf congiunta è il prodotto delle pdf delle singole variabili.

### Processi a tempo discreto

#### Slide 40 — Processi aleatori a tempo discreto (1/2) (versione aggiornata) · [[random_processes_v2.pdf#page=40|p. 40 (v2)]]
- Finora si sono considerati processi a tempo continuo, $X(t; \omega)$ con $t \in \mathbb{R}$. Se la variabile temporale appartiene a $\mathbb{Z}$, il processo è **a tempo discreto** e si indica con $X(n; \omega)$.
- Un processo a tempo discreto è una **successione di variabili aleatorie** $\{X(n)\}_{n \in \mathbb{Z}}$ (con $\omega$ omesso). Per $n \in \{0, 1, \dots, N-1\}$ si può rappresentare con un **vettore aleatorio**.
- CDF, pdf e DF si definiscono come nel caso a tempo continuo, sostituendo $t$ con $n$.
- **Media e crosscorrelazione**:

$$\mu_X(n) \triangleq E[X(n)] \tag{35}$$

$$R_{XY}(n, k) \triangleq E[X(n)\,Y^\ast(k)] \tag{36}$$

  (nella versione precedente la (35) e la (36) erano scritte come integrali con le pdf, e la (36) senza il coniugato).

#### Slide 41 — Processi aleatori a tempo discreto (2/2) (versione aggiornata) · [[random_processes_v2.pdf#page=41|p. 41 (v2)]]
- La **crosscovarianza** di due processi a tempo discreto:

$$C_{XY}(n, k) \triangleq E\{[X(n) - \mu_X(n)][Y(k) - \mu_Y(k)]^\ast\} = R_{XY}(n, k) - \mu_X(n)\,\mu_Y^\ast(k) \tag{37}$$

- Con $X(n) \equiv Y(n)$ nelle (36) e (37) si ottengono le definizioni usuali di autocorrelazione e autocovarianza.
- Per due processi a tempo discreto congiuntamente WSS, la **cross-spectral density** è

$$S_{XY}(\nu) \triangleq \lim_{N \to +\infty} \frac{1}{2N+1}\,E\big[X_N(\nu)\,Y_N^\ast(\nu)\big]$$

  dove, per $Z \in \{X, Y\}$, $Z_N(\nu) \triangleq \sum_{n=-N}^{N} Z(n)\,e^{-j2\pi\nu n}$ è la trasformata di Fourier a tempo discreto (DTFT) del processo troncato $Z(n)$.
- Con $X(n) \equiv Y(n)$ si ottiene la **PSD** di un processo a tempo discreto:

$$S_{XX}(\nu) \triangleq \lim_{N \to +\infty} \frac{1}{2N+1}\,E\big[\lvert X_N(\nu)\rvert^2\big]$$

- Per il teorema di Wiener-Khinchin, la PSD di un processo WSS a tempo discreto è la DTFT della sua acf:

$$S_{XX}(\nu) = \sum_{m=-\infty}^{+\infty} R_{XX}(m)\,e^{-j2\pi\nu m}$$

---

*Approfondimenti nel wiki (derivazioni, esempi svolti, grafici): [[processo-aleatorio]], [[momenti-di-un-processo]], [[stazionarieta]], [[autocorrelazione-processi-wss]], [[processi-e-sistemi-lti]], [[densita-spettrale-di-potenza]], [[processo-gaussiano]], [[calcolo-densita-spettrale]].*


## Lezione 6 — Laboratorio Matlab: conversione A/D e D/A (28/09)

*Fonte: lo script `AD_conversion.m` e le tre figure della lezione di laboratorio (`raw/scripts/09_28_2006/`). Non è materia d'esame: serve a vedere sui numeri ciò che la Lezione 3 dice a parole. Le figure «replica» sono ricavate rieseguendo lo script in Python.*

Lo script simula la catena **campionamento → interpolazione → quantizzazione → SNR** su due segnali (esempio 1: il trapezio; esempio 2: tre sinusoidi). Il computer lavora su vettori, quindi il «tempo continuo» è una griglia molto fitta.

### 0. Il «tempo continuo» e lo spettro · [[Campionamento_AD_DA.pdf#page=8|p. 8]]

```matlab
accuracy = 1e4;  t_i = -30;  t_f = 30;
D  = t_f - t_i;                % 60 s
dt = D/accuracy;               % 6 ms
t  = t_i:dt:t_f-dt;            % N = 10^4 istanti
```

| Grandezza | Valore |
|---|---|
| finestra $D$ | 60 s ($-30 \to 30$) |
| passo $dt$ | $60/10^4 = 6$ ms |
| punti $N$ | $10^4$ (l'ultimo estremo è escluso) |
| banda visibile | $\pm 1/(2\,dt) = \pm 83.3$ Hz |
| risoluzione in frequenza | $1/(N\,dt) = 1/60$ Hz |

- **Regola del codice:** ogni istante «speciale» (spigoli, $T_s$) viene arrotondato a un multiplo di $dt$ con `round(x/dt)*dt`, perché nel vettore esistono solo i tempi della griglia.
- **Esempio 1 (trapezio):** 0 fino a $-2$ s, rampa fino a 1 in $-1$ s, costante a 1 fino a $+1$ s, rampa fino a 0 in $+2$ s. Banda dichiarata `W = 1` Hz.
- **Esempio 2:** $s(t) = 5\sin(2\pi\,4t + \tfrac{\pi}{5}) + 3\sin(2\pi\,\tfrac43 t + \tfrac{\pi}{8}) + 2\sin(2\pi\,0.4t - \tfrac{\pi}{3})$, frequenze 4, 1.33, 0.4 Hz, `W = 4` Hz (banda davvero limitata).

#### Lo spettro: perché `dt*fft`

```matlab
S_dft = fftshift(fft(s));     % DFT con la frequenza zero al centro
S     = dt*S_dft;             % approssima l'integrale di Fourier
f     = linspace(-0.5,0.5,N)/dt;
```

La trasformata è un integrale; sulla griglia diventa una somma di Riemann, e il passo $dt$ è l'ampiezza di ogni rettangolino:

$$S(f_k) = \int s(t)\,e^{-j2\pi f_k t}\,dt \approx dt\sum_{n} s(t_n)\,e^{-j2\pi f_k t_n} \;\Rightarrow\; \lvert S(f_k)\rvert \approx dt\,\lvert \text{FFT}(s)[k]\rvert$$

La FFT è la somma senza $dt$: moltiplicare per $dt$ dà le unità giuste (V·s = V/Hz) e rende il risultato indipendente da quanto è fitta la griglia. Il fattore di fase $e^{-j2\pi f t_i}$ (la griglia parte da $-30$, non da 0) non cambia il modulo.

**Spettro esatto del trapezio** (derivazione del lab): è la convoluzione di un rettangolo largo 3 e uno largo 1, $s = \Pi(t/3)\ast\Pi(t)$, quindi

$$S(f) = 3\,\text{sinc}(3f)\,\text{sinc}(f), \qquad S(0) = 3 = \text{area}, \qquad E = \tfrac83 \approx 2.667$$

La FFT dà $S(0) = 2.986$. Solo lo 0.05% dell'energia sta oltre 1 Hz (0.85% oltre 0.5 Hz): per questo `W = 1` è una banda ragionevole, anche se il trapezio non è a banda limitata.

![[grafico-lab-setup-spettro.png|640]]
*Replica: a sinistra lo spigolo in $t = -1$ visto come fila di punti ogni 6 ms; al centro $\lvert dt\cdot\text{FFT}\rvert$ (blu) sovrapposta alla trasformata esatta (arancio tratteggiato); a destra lo spettro in dB, con lobi che non arrivano mai a zero.*

![[lab-0928-figure1-segnale-spettro-campioni.png|520]]
*Figura 1 del laboratorio (esempio 1). In alto il trapezio su $[-3, 3]$ s; al centro lo spettro sull'asse $\pm 83$ Hz, concentrato attorno a 0 con picco 3; in basso i 121 campioni su $[-30, 30]$ s, quasi tutti nulli.*

### 1. Campionamento · [[Campionamento_AD_DA.pdf#page=11|p. 11]], [[Campionamento_AD_DA.pdf#page=12|12]], [[Campionamento_AD_DA.pdf#page=13|13]]

```matlab
fs   = 2*W;   Ts = 1/fs;
Ts   = round(Ts/dt)*dt;                     % multiplo di dt
high = (abs((t/Ts)-round(t/Ts)) < eps);     % 1 dove t è multiplo di Ts
s_samp = s.*high;                           % azzera tutto il resto
is   = find(high);                          % indici dei campioni
stem(t(is), s_samp(is));
```

- `high` vale 1 negli istanti $nT_s$ (con tolleranza `eps` per gli errori di virgola mobile); `s.*high` è il prodotto punto per punto: lascia $s$ ai campioni e mette 0 altrove.
- `find(high)` restituisce gli **indici** degli 1; `stem` disegna aste (campioni) invece di una curva.
- `s_samp` è la versione simulata di $x_\delta(t) = \sum_n x(nT_s)\,\delta(t - nT_s)$: ha ancora $10^4$ punti, ma solo i campioni possono essere non nulli. Il filtro di interpolazione ha picco 1, quindi non serve correggere la scala della $\delta$.

**Esempio 1:** $f_s = 2W = 2$ Hz → $T_s = 0.5$ s; $0.5/0.006 = 83.3 \to 83$, quindi $T_s = 0.498$ s e $f_{samp} = 2.008$ Hz. Nella finestra cadono $n = -60, \dots, 60$: **121 campioni**, di cui 9 non nulli:

| $nT_s$ [s] | $\pm 1.992$ | $\pm 1.494$ | $\pm 0.996$, $\pm 0.498$, 0 |
|---|---|---|---|
| $s(nT_s)$ | 0.008 | 0.506 | 1 |

**Spettro:** campionare replica lo spettro ogni $f_{samp}$, $X_\delta(f) = \frac{1}{T_s}\sum_k S\big(f - \frac{k}{T_s}\big)$. Il trapezio non è a banda limitata, quindi le code delle repliche entrano in $\lvert f\rvert < f_s/2$ (aliasing), ma qui è trascurabile (0.05% dell'energia oltre 1 Hz). Il commento del codice («come se avessimo applicato un filtro anti-aliasing») significa questo: nessun filtro è applicato, il segnale ha solo già quasi tutta l'energia sotto 1 Hz.

![[grafico-lab-campionamento-spettro.png|640]]
*Replica. In alto il trapezio e i campioni ogni 0.498 s; in basso lo spettro dei campioni (blu) come somma delle repliche $S(f)$, $S(f \mp f_s)$ (tratteggiate). Nella fascia $\lvert f\rvert < 1.004$ Hz la replica centrale è quasi pulita.*

**Esempio 2 (l'arrotondamento rompe il teorema):** $f_s = 2W = 8$ Hz → $T_s = 0.125$ s; $0.125/0.006 = 20.83 \to 21$, quindi $T_s = 0.126$ s e $f_{samp} = 7.937$ Hz $< 2W = 8$ Hz. La componente a 4 Hz supera $f_{samp}/2 = 3.968$ Hz e si ripiega in $f_{samp} - 4 = 3.937$ Hz: la ricostruzione con la sinc ha **SNR 2 dB**; con $f_s = 16.7$ Hz sale a **37.5 dB**. Anche $f_s = 2W$ esatto è il caso limite della p. 13: una sinusoide a $f_s/2$ viene campionata sempre nella stessa fase, e l'ampiezza non si ricostruisce.

![[grafico-lab-esempio2.png|520]]
*Replica. In alto $f_s = 7.94$ Hz: i campioni sono giusti ma la curva ricostruita non è il segnale (i campioni sono compatibili anche con una sinusoide più lenta); in basso $f_s = 16.67$ Hz: la ricostruzione coincide.*

### 2. Interpolazione · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|23]], [[Campionamento_AD_DA.pdf#page=24|24]]

```matlab
C = 2;                          % 1 rettangolo, 2 triangolo, 3 sinc
switch C
case 1  th = 0:dt:Ts;           h = ones(size(th));       % rect((t-Ts/2)/Ts)
case 2  th = -Ts:dt:Ts;         h = 1-abs(th/Ts);         % lambda(t/Ts)
case 3  th = -25*Ts:dt:25*Ts;   h = sinc(th/Ts);          % sinc(t/Ts)
end
L = length(h);
s_r       = conv(s_samp,h);                            % interpolazione
s_r_trunc = s_r(floor((L-1)/2)+1 : floor((L-1)/2)+N);  % taglio a N punti
t_conv = (t(1)+th(1)) + (0:length(s_r)-1)*dt;          % asse dell'uscita completa
```

- **La convoluzione è la formula di interpolazione:** $x_r(t) = \sum_n x(nT_s)\,h(t - nT_s)$. Ogni campione «accende» una copia di $h$ centrata sul suo istante e pesata dal suo valore; le copie si sommano. Con triangoli la somma è la spezzata che unisce i campioni; con la sinc le copie oscillano e si compensano.
- **Le durate si sommano.** `conv` di vettori con $N$ e $L$ punti dà $N + L - 1$ punti: l'uscita esiste da quando i due segnali si toccano a quando si lasciano. Se $x \ne 0$ solo su $[a_1, b_1]$ e $h$ solo su $[a_2, b_2]$, $y \ne 0$ solo su $[a_1 + a_2,\, b_1 + b_2]$.

| Filtro | `th` | $L$ | Punti di `conv` | Asse dell'uscita [s] |
|---|---|---|---|---|
| triangolo (C = 2) | $[-T_s, T_s]$ | $2\cdot 83 + 1 = 167$ | $10^4 + 166 = 10166$ | $[-30.498,\ 30.492]$ |
| sinc, 25 lobi (C = 3) | $[-25T_s, 25T_s]$ | $4151$ | $14150$ | $[-42.45,\ 42.44]$ |
| rettangolo (C = 1) | $[0, T_s]$ | $84$ | $10083$ | $[-30,\ 30.492]$ |

- **Perché si taglia:** per confrontare $s_r$ con $s$ (e calcolare l'errore) i due vettori devono avere la stessa lunghezza e gli stessi istanti; i punti in più sono le code dei filtri vicino ai bordi.
- **Perché proprio da $(L-1)/2 + 1$:** il punto $k$ dell'uscita sta a $t(1) + th(1) + (k-1)\,dt$; lo voglio a $t(1)$, quindi $k - 1 = -th(1)/dt = (L-1)/2$ (filtro simmetrico). Si scartano $(L-1)/2$ punti per lato: 83 per il triangolo, 2075 per la sinc (12.45 s). Tagliando i primi $N$ punti il ricostruito risulterebbe ritardato di 0.498 s (triangolo) o 12.45 s (sinc).

![[grafico-lab-durata-convoluzione.png|600]]
*Replica (esempio 1, sinc). In alto gli ingressi di `conv` (10⁴ punti e 4151 punti); al centro l'uscita completa (14150 punti, fasce rosse = parti tagliate); in basso il taglio del codice (blu) contro il taglio sbagliato (rosso, spostato di 12.45 s).*

**I tre filtri a confronto** (esempio 1 senza quantizzazione, SNR come in §4):

| Filtro | SNR | Comportamento |
|---|---|---|
| rettangolo (C = 1) | 15.8 dB | gradini con picchi |
| triangolo (C = 2) | 50.2 dB | la spezzata coincide con il trapezio (suoi spigoli $\pm1$, $\pm2$ cadono quasi su campioni: coincidenza favorevole) |
| sinc (C = 3) | 26.7 dB | curva morbida con piccole oscillazioni, massimo 1.029 in $t = -0.82$ s |

La sinc (serie di Shannon) ricostruisce l'unico segnale a banda limitata $\lvert f\rvert < f_s/2$ che passa per i campioni: il trapezio non lo è, quindi viene «smussato». Il rettangolo del codice ha due particolarità: `th = 0:dt:Ts` contiene sia 0 sia $T_s$ (84 punti per 83 passi: due copie adiacenti condividono un punto, da cui i picchi a 2 e a 1.5) ed è causale, quindi con il taglio da $(L-1)/2$ i gradini risultano centrati sui campioni (interpolazione «al campione più vicino»), non ZOH.

![[grafico-lab-interpolatori.png|600]]
*Replica: i tre interpolatori sull'esempio 1 senza quantizzazione (in verde tratteggiato lo ZOH causale vero, SNR 12.2 dB).*

#### Quanto deve essere largo il filtro

Rettangolo largo $T_s$; triangolo con base $2T_s$ (da $-T_s$ a $+T_s$). Sono le larghezze per cui valgono due condizioni:
1. **Passare per i campioni:** $h(0) = 1$ e $h(kT_s) = 0$ per $k \ne 0$ (il triangolo si annulla in $\pm T_s$; con base $3T_s$ varrebbe ancora $1/3$ e sporcherebbe i vicini; la sinc ha gli zeri in $kT_s$).
2. **Niente buchi né sovrapposizioni:** con tutti i campioni a 1, il ricostruito deve valere 1 ovunque, cioè $\sum_n h(t - nT_s) = 1$. Rettangoli larghi $T_s$ pavimentano l'asse; più stretti lasciano buchi, più larghi si sovrappongono. Tra due campioni i due triangoli valgono $1 - \tau/T_s$ e $\tau/T_s$, e sommano a 1.

![[grafico-lab-larghezza-filtro.png|600]]
*Replica: lo stesso segnale lento campionato ogni $T$ e ricostruito con sei larghezze (rettangolo $T/2$, $T$, $1.5T$; triangolo base $T$, $2T$, $3T$).*

![[lab-0928-figure2-interpolazione-lineare.png|520]]
*Figura 2 del laboratorio, C = 2 (triangolo): in alto il ricostruito $s_r(t)$, identico al trapezio; al centro e in basso la parte quantizzata (§3).*

![[lab-0928-figure2-interpolazione-shannon.png|520]]
*Figura 2 del laboratorio, C = 3 (sinc): fianchi arrotondati, due gobbe sopra 1 attorno a $\pm 0.8$ s e piccole oscillazioni fuori da $[-2, 2]$.*

### 3. Quantizzazione · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=26|26]], [[Campionamento_AD_DA.pdf#page=28|28]]

```matlab
bits  = 4;
s_min = min(s_samp);  s_max = max(s_samp);
range = s_max - s_min;
Nq    = pow2(bits);                    % 2^4 = 16 livelli
Delta = range/Nq;                      % larghezza di una cella
cbook = s_min+Delta/2:Delta:s_max;     % livelli al centro delle celle
for k=1:length(is)
   [~,index(k)] = min(abs(cbook-s_samp(is(k))));   % livello più vicino
end
s_q(is) = cbook(index);
```

1. Dinamica $[s_{min}, s_{max}]$ dei campioni; 2. divisa in $N_q = 2^b$ celle uguali di larghezza $\Delta$; 3. i livelli (codebook) sono i **centri** delle celle; 4. ogni campione va al livello più vicino; 5. i campioni quantizzati passano nello stesso interpolatore, con lo stesso taglio.

**Numeri (esempio 1, 4 bit):** $s_{min} = 0$, $s_{max} = 1$, $N_q = 16$, $\Delta = 1/16 = 0.0625$, codebook $0.03125, 0.09375, \dots, 0.96875$.

| Campione | Livello più vicino | Errore $e = s_q - s$ |
|---|---|---|
| 0 (112 campioni su 121) | 0.03125 | $+0.03125 = +\Delta/2$ |
| 0.008 | 0.03125 | $+0.023$ |
| 0.506 | 0.53125 | $+0.025$ |
| 1 (5 campioni) | 0.96875 | $-0.03125 = -\Delta/2$ |

È il quantizzatore uniforme della lezione 3: $\lvert e\rvert \le \Delta/2$. Con i livelli al centro delle celle e l'estremo della dinamica in 0, **lo zero non è rappresentabile** (il livello più basso è $\Delta/2$): fuori dal trapezio il ricostruito ha un «pavimento» a 0.031 e il plateau si abbassa a 0.969. Per quei campioni l'errore vale **sempre** $\Delta/2$, non è uniforme in $(-\Delta/2, \Delta/2)$ come nel modello. (Dettaglio: `s_min`/`s_max` sono presi su tutto `s_samp`, zeri compresi; per il trapezio non cambia nulla.)

![[grafico-lab-quantizzazione.png|640]]
*Replica (4 bit). A sinistra la caratteristica a 16 livelli con i valori dei campioni (lo 0 finisce su $\Delta/2$); al centro l'errore sui 121 campioni, sempre dentro $\pm\Delta/2$; a destra il ricostruito dopo la quantizzazione, con pavimento a 0.031 e plateau a 0.969.*

### 4. SNR · [[Campionamento_AD_DA.pdf#page=29|p. 29]], [[Campionamento_AD_DA.pdf#page=30|30]]

```matlab
P_s   = mean(s.^2);                  % potenza del segnale originale
E_q   = mean((s-sq_r_trunc).^2);     % potenza dell'errore
SNR_q = 10*log10(P_s/E_q)            % in dB
```

È la definizione della lezione 3, $\text{SNR} = \langle x^2\rangle/\langle e^2\rangle$, ma l'errore è **segnale originale − ricostruito dopo quantizzazione e interpolazione**: misura l'intera catena A/D + D/A, non la sola quantizzazione.

**Valore stampato (esempio 1, triangolo, 4 bit): 16.7 dB.** $P_s \approx E/D = (8/3)/60 = 0.0444$; $E_q \approx 9.6\cdot10^{-4}$ (il 95% viene dai 56 s con segnale nullo e ricostruito a 0.031); $\text{SNR} = 10\log_{10}(0.0444/9.6\cdot10^{-4}) \approx 16.7$ dB.

Il numero mescola tre cose: la quantizzazione; l'interpolazione (senza quantizzare: 50.2 dB triangolo, 26.7 dB sinc, 15.8 dB rettangolo, e sono tetti per qualunque numero di bit); la finestra (calcolato su $\lvert t\rvert < 2.5$ s l'SNR sale a 28.4 dB).

**Confronto con i 6 dB/bit:** il modello assume errore uniforme di potenza $\Delta^2/12$; qui quasi tutti gli errori valgono $\Delta/2$, potenza $\Delta^2/4$, cioè 3 volte tanto: $10\log_{10}3 = 4.77$ dB in meno. Modello: $10\log_{10}\frac{0.0444}{(1/16)^2/12} = 21.4$ dB; misurato 16.7 dB (differenza 4.7 dB). La **pendenza** resta 6.02 dB/bit: ogni bit dimezza $\Delta$, la potenza dell'errore si divide per 4.

| $b$ [bit] | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| SNR del codice [dB] | −1.4 | 4.6 | 10.6 | **16.7** | 22.7 | 28.7 | 34.4 | 40.0 | 44.7 | 47.9 |
| SNR sui soli campioni [dB] | −1.4 | 4.7 | 10.7 | 16.7 | 22.8 | 28.9 | 34.8 | 40.9 | 46.8 | 52.9 |

Fino a 7–8 bit le due righe coincidono e crescono di 6.0 dB/bit; poi quella del codice si ferma verso il limite dell'interpolazione (50.2 dB). Aumentare i bit migliora solo finché domina la quantizzazione; oltre contano l'interpolatore e, prima ancora, il campionamento (esempio 2: l'aliasing tiene l'SNR a 2 dB).

![[grafico-lab-snr-vs-bit.png|560]]
*Replica. Blu: SNR stampato dal codice; arancio: SNR dei soli campioni; nero tratteggiato: modello $\Delta^2/12$ (parallelo, +4.77 dB); linee orizzontali: i tetti senza quantizzazione (50.2 dB triangolo, 26.7 dB sinc).*

*Approfondimenti nel wiki: [[laboratorio-conversione-ad]], [[lab-setup-e-spettro]], [[lab-campionamento]], [[lab-interpolazione]], [[lab-quantizzazione]], [[lab-snr]] (derivazioni complete e animazione dell'interpolazione).*
