# Trasmissione dei Segnali Digitali — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, D. Darsena; testo Madhow, *Fundamentals of Digital Communication*; esame orale). Contiene **solo ciò che sta nei PDF del corso**, nell'ordine delle slide: definizioni, formule, esempi, figure e le dimostrazioni svolte a mano dalla docente. I passaggi che le slide saltano sono ricostruiti in una riga dove servono a seguire il discorso; le derivazioni estese, i grafici aggiuntivi, gli esercizi e le animazioni stanno nelle pagine concetto, esercizio e laboratorio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Le equazioni numerate sono quelle delle slide di ciascuna lezione. Il PDF di una lezione si genera con `python output/crea_pdf.py N` (file in `output/pdf/`).

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 1 | [[#Lezione 1 — Introduzione al corso\|Introduzione al corso]] | Intro.pdf |
| 2 | [[#Lezione 2 — Elementi di teoria della probabilità\|Elementi di teoria della probabilità]] | Probabilità.pdf |
| 3 | [[#Lezione 3 — Campionamento e conversione A/D e D/A\|Campionamento e conversione A/D e D/A]] | Campionamento_AD_DA.pdf |
| 4 | [[#Lezione 4 — Rappresentazione complessa in banda base\|Rappresentazione complessa in banda base]] | Rappresentazione_Rice.pdf |
| 5 | [[#Lezione 5 — Laboratorio Matlab: conversione A/D e D/A (28/09)\|Laboratorio Matlab: conversione A/D e D/A]] | AD_conversion.m + figure |
| 6 | [[#Lezione 6 — Processi aleatori\|Processi aleatori]] | random_processes.pdf (+ random_processes_v2.pdf) |
| 7 | [[#Lezione 7 — Rappresentazione dei processi passa-banda\|Rappresentazione dei processi passa-banda]] | Rappresentazione_Rice_processi.pdf |
| 8 | [[#Lezione 8 — Principi di modulazione\|Principi di modulazione]] | Modulazione.pdf |
| 9 | [[#Lezione 9 — Elementi di teoria della rivelazione\|Elementi di teoria della rivelazione]] | Detection.pdf |
| 10 | [[#Lezione 10 — Prestazioni delle modulazioni binarie e della QPSK\|Prestazioni delle modulazioni binarie e della QPSK]] | Lezione 10-28.pdf |
| 11 | [[#Lezione 11 — Union bound e approssimazione dei primi vicini\|Union bound e approssimazione dei primi vicini]] | Lezione 11-2.pdf |
| 12 | [[#Lezione 12 — Parametri globali delle modulazioni e capacità di canale\|Parametri globali delle modulazioni e capacità di canale]] | Confronto_new.pdf |
| 13 | [[#Lezione 13 — Stima dei parametri per la sincronizzazione\|Stima dei parametri per la sincronizzazione]] | 11-9.pdf, Synchro_Kay_example (1).pdf |
| 14 | [[#Lezione 14 — Segnalazione su canali a banda limitata\|Segnalazione su canali a banda limitata]] | signaling_bandlimited_channel.pdf |



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

$$\mathcal F[u(t)]=\tfrac12\delta(f)+\frac1{j2\pi f}\triangleq U(f)\quad(5)\qquad\mathcal F[U(t)]=u(-f)\ \ (\text{dualità})\quad(6)$$

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

$$S_p^+(f)=\frac1{\sqrt2}S_p(f)+\frac j{\sqrt2}\mathcal F[\widehat s_p(t)]\quad(11)\qquad\widehat S_p(f)=S_p(f)\,\mathcal F\Big[\frac1{\pi t}\Big]\quad(12)$$

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

#### Appunti sparsi — Dimostrazione della (14) · [[Lezioni.pdf#page=3|p. 3]]

Nel quaderno «Lezioni» sono ripassati i passaggi (3)–(9), (10), lo spettro della trasformata di Hilbert, la (17) e l'ortogonalità (18). Il passaggio in più è la dimostrazione della (14):

$$s_p(t)=\sqrt2\,\text{Re}\{s_p^+(t)\}=\frac{\sqrt2}{2}\big[s_p^+(t)+(s_p^+(t))^\ast\big]$$

e la trasformata del coniugato è il coniugato della trasformata riflessa, $\int(s_p^+(t))^\ast e^{-j2\pi ft}dt=\big[\int s_p^+(t)e^{+j2\pi ft}dt\big]^\ast=[S_p^+(-f)]^\ast$, quindi

$$S_p(f)=\frac1{\sqrt2}\big[S_p^+(f)+(S_p^+(-f))^\ast\big]$$

Poiché $S(f)=S_p^+(f+f_c)$, si ha $S_p^+(f)=S(f-f_c)$ e $S_p^+(-f)=S(-f-f_c)$: è la (14). Nella dimostrazione della (18) gli appunti annotano che i termini misti si annullano «per ipotesi di banda stretta»: la distanza tra i centri dei due spettri, $2f_c$, supera la banda $B$ (ipotesi $f_c>B$).

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


## Lezione 5 — Laboratorio Matlab: conversione A/D e D/A (28/09)

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

#### Appunti sparsi — DFT e DTFT · [[Lezioni.pdf#page=2|p. 2]]

Per una sequenza con $x(m)\neq0$ solo per $m=0,\dots,N-1$, la DFT $X_k=\sum_{m=0}^{N-1}x(m)e^{-j2\pi mk/N}$ coincide con la trasformata a tempo discreto $X(\nu)=\sum_mx(m)e^{-j2\pi m\nu}$ calcolata in $\nu=k/N$: la DFT è il campionamento della trasformata di Fourier a tempo discreto. Gli appunti segnano come «da capire» che, per effetto dell'elaborazione, la componente continua viene spezzata e spostata: è l'effetto di `fft` e `fftshift`, spiegato in [[lab-setup-e-spettro]].

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


## Lezione 6 — Processi aleatori

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

#### Slide 15 — Significato fisico della Auto Correlation Function (acf) (1/2) · [[random_processes.pdf#page=20|p. 20]]
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


## Lezione 7 — Rappresentazione dei processi passa-banda

*Fonte: Rappresentazione_Rice_processi.pdf, 25 pagine (13 slide e 12 pagine di appunti a mano alle p. 3, 5, 7, 8, 9, 13, 15, 16, 18, 19, 22, 23; note a mano sopra le slide a p. 4, 11, 20). Corrispondenza: slide 1 = p. 1, 2 = p. 2, 3 = p. 4, 4 = p. 6, 5 = p. 10, 6 = p. 11, 7 = p. 12, 8 = p. 14, 9 = p. 17, 10 = p. 20, 11 = p. 21, 12 = p. 24, 13 = p. 25. Le equazioni (1)–(14) sono quelle delle slide di questa lezione.*

### Processi in banda base e passa-banda

#### Slide 2 e appunti — Ipotesi, definizioni e processo analitico · [[Rappresentazione_Rice_processi.pdf#page=2|p. 2]], [[Rappresentazione_Rice_processi.pdf#page=3|3]]
- Si assumono processi stocastici **reali, WSS, a media nulla** ($\mu_x = E[x(t)] = 0$). L'ipotesi di processo reale è «non troppo restrittiva».
- $x_b(t)$ è **in banda base** se la sua PSD è in banda base: $S_{x_bx_b}(f) = 0$ per $|f| > W > 0$.
- $x_p(t)$ è **passa-banda** se la sua PSD è passa-banda, concentrata esclusivamente attorno alle frequenze $\pm f_c$ con $f_c \gg W$: $S_{x_px_p}(f) = 0$ per $|f \pm f_c| > W > 0$.
- I processi passa-banda sono reali, perciò il loro spettro ha due lobi speculari in $\pm f_c$, e quello a frequenze negative ripete le stesse informazioni di quello a frequenze positive. Per descriverli senza questa ridondanza si costruisce, come nel caso deterministico, il **processo (complesso) analitico**, che contiene solo le frequenze positive:

$$x_p^+(t) = \frac{1}{\sqrt2}\,x_p(t) + \frac{j}{\sqrt2}\,\widehat{x}_p(t)$$

  È il segnale ottenuto considerando unicamente lo spettro a frequenze positive.
- $\widehat{x}_p(t)$ è la **trasformata di Hilbert** del processo, ottenuta filtrando $x_p(t)$ con il filtro di Hilbert ideale di risposta impulsiva $h(t) = \dfrac{1}{\pi t}$ e risposta in frequenza $H(f) = -j\,\text{sgn}(f)$ (cioè $-j$ per $f > 0$, $+j$ per $f < 0$).

### Inviluppo complesso e componenti in fase e quadratura

#### Slide 3 e appunti — Definizione di inviluppo complesso · [[Rappresentazione_Rice_processi.pdf#page=4|p. 4]], [[Rappresentazione_Rice_processi.pdf#page=5|5]]
- In modo omologo al caso deterministico, l'**inviluppo complesso** del processo $x_p(t)$ è

$$x(t) = x_p^+(t)\,e^{-j2\pi f_ct} = x_c(t) + jx_s(t) \tag{1}$$

  È una **traslazione in frequenza** del processo che centra la PSD nell'origine. $x_c(t)$ e $x_s(t)$ sono le componenti **in fase** e **in quadratura** di $x_p(t)$; sono entrambe processi aleatori **reali in banda base**.
- Relazione tra il processo passa-banda e l'inviluppo:

$$x_p(t) = \sqrt2\,\text{Re}\{x_p^+(t)\} = \sqrt2\,\text{Re}\{x(t)\,e^{j2\pi f_ct}\} = \sqrt2\,x_c(t)\cos(2\pi f_ct) - \sqrt2\,x_s(t)\sin(2\pi f_ct)$$

- Estrazione delle componenti, da $x(t) = \big[\tfrac{1}{\sqrt2}x_p(t) + j\tfrac{1}{\sqrt2}\widehat{x}_p(t)\big]e^{-j2\pi f_ct}$ (parte reale e parte immaginaria):

$$x_c(t) = \frac{1}{\sqrt2}\Big[x_p(t)\cos(2\pi f_ct) + \widehat{x}_p(t)\sin(2\pi f_ct)\Big]$$

$$x_s(t) = \frac{1}{\sqrt2}\Big[-x_p(t)\sin(2\pi f_ct) + \widehat{x}_p(t)\cos(2\pi f_ct)\Big]$$

- Nota a mano sulla slide: le due componenti hanno media nulla (annotazione in parte illeggibile).

### Le componenti sono congiuntamente WSS

#### Slide 4–6 e appunti — Teorema e dimostrazione · [[Rappresentazione_Rice_processi.pdf#page=6|p. 6]]–[[Rappresentazione_Rice_processi.pdf#page=11|11]]
- **Teorema.** Se $x_p(t)$ è un processo passa-banda WSS a media nulla, allora le sue componenti in banda base $x_c(t)$ e $x_s(t)$ sono **processi congiuntamente WSS a media nulla**.
- **Dimostrazione.**
  - *Media.* $E[x_p(t)] = \mu_{x_p} = 0$ per ipotesi. Anche la trasformata di Hilbert ha media nulla: $E[\widehat{x}_p(t)] = E\big[\int x_p(t-\tau)\frac{1}{\pi\tau}\,d\tau\big] = \int E[x_p(t-\tau)]\frac{1}{\pi\tau}\,d\tau = 0$. Quindi $x_c$ e $x_s$ hanno media nulla, indipendente da $t$.
  - *Resta da verificare* che le acf $R_{x_cx_c}(t,\tau)$ e $R_{x_sx_s}(t,\tau)$ e la crosscorrelazione $R_{x_cx_s}(t,\tau)$ dipendano solo da $\tau$.
  - *Relazioni fondamentali tra $x_p$ e $\widehat{x}_p$*, ricordando $S_{yy}(f) = S_{xx}(f)\,|H(f)|^2$ e $R_{yy}(\tau) = R_{xx}(\tau) \ast h(\tau) \ast h(-\tau)$, con $\widehat{R}_{x_px_p}$ trasformata di Hilbert di $R_{x_px_p}$:

$$S_{\widehat{x}_p\widehat{x}_p}(f) = |{-j}\,\text{sgn}(f)|^2\,S_{x_px_p}(f) = S_{x_px_p}(f) \ \Longrightarrow\ R_{\widehat{x}_p\widehat{x}_p}(\tau) = R_{x_px_p}(\tau) \tag{2}$$

$$S_{\widehat{x}_px_p}(f) = -j\,\text{sgn}(f)\,S_{x_px_p}(f) \ \Longrightarrow\ R_{\widehat{x}_px_p}(\tau) = \widehat{R}_{x_px_p}(\tau) \tag{3}$$

$$S_{x_p\widehat{x}_p}(f) = j\,\text{sgn}(f)\,S_{x_px_p}(f) \ \Longrightarrow\ R_{x_p\widehat{x}_p}(\tau) = -\widehat{R}_{x_px_p}(\tau) \tag{4}$$

  - *Acf di $x_c$.* Con $a = 2\pi f_ct$ e $b = 2\pi f_c(t-\tau)$:

$$
\begin{aligned}
2R_{x_cx_c}(t,\tau) &= 2E[x_c(t)\,x_c(t-\tau)] \\
&= R_{x_px_p}(\tau)\cos a\cos b + R_{\widehat{x}_p\widehat{x}_p}(\tau)\sin a\sin b + R_{x_p\widehat{x}_p}(\tau)\cos a\sin b + R_{\widehat{x}_px_p}(\tau)\sin a\cos b
\end{aligned} \tag{5}
$$

  - Sostituendo (2), (3), (4) in (5) (e usando le formule di Werner $\sin\alpha\cos\beta = \frac12[\sin(\alpha+\beta) + \sin(\alpha-\beta)]$, $\cos\alpha\cos\beta = \frac12[\cos(\alpha+\beta) + \cos(\alpha-\beta)]$, $\sin\alpha\sin\beta = \frac12[\cos(\alpha-\beta) - \cos(\alpha+\beta)]$):

$$
\begin{aligned}
2R_{x_cx_c}(t,\tau) &= R_{x_px_p}(\tau)\{\cos a\cos b + \sin a\sin b\} + \widehat{R}_{x_px_p}(\tau)\{\sin a\cos b - \cos a\sin b\} \\
&= R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau) \triangleq 2R_{x_cx_c}(\tau)
\end{aligned} \tag{6}
$$

  La (6) **dipende unicamente dal ritardo** $\tau$.
  - Ripetendo gli stessi passaggi per $x_s$ e per le mutue correlazioni:

$$2R_{x_sx_s}(t,\tau) = R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau) = 2R_{x_cx_c}(\tau) \tag{7}$$

$$2R_{x_cx_s}(t,\tau) = R_{x_px_p}(\tau)\sin(2\pi f_c\tau) - \widehat{R}_{x_px_p}(\tau)\cos(2\pi f_c\tau) \triangleq 2R_{x_cx_s}(\tau) \tag{8}$$

$$2R_{x_sx_c}(t,\tau) = -R_{x_px_p}(\tau)\sin(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\cos(2\pi f_c\tau) = -2R_{x_cx_s}(\tau) \tag{9}$$

  Il teorema è dimostrato. ∎
- **Conclusione:** un processo passa-banda WSS è tale che

$$R_{x_cx_c}(\tau) = R_{x_sx_s}(\tau) \qquad R_{x_cx_s}(\tau) = -R_{x_sx_c}(\tau) \tag{10}$$

- **Acf dell'inviluppo complesso** (il coniugato serve perché $x$ è complesso):

$$
\begin{aligned}
R_{xx}(\tau) &\triangleq E[x(t)\,x^\ast(t-\tau)] \\
&= R_{x_cx_c}(\tau) + R_{x_sx_s}(\tau) + j\big[R_{x_sx_c}(\tau) - R_{x_cx_s}(\tau)\big]
\end{aligned} \tag{11}
$$

$$R_{xx}(\tau) = 2R_{x_cx_c}(\tau) + 2j\,R_{x_sx_c}(\tau) \tag{12}$$

  dove $2R_{x_cx_c}$ è l'autocorrelazione di $x_c$ e $R_{x_sx_c}$ la mutua correlazione $x_s$, $x_c$.
- Poiché $R_{xx}(0) = E[|x(t)|^2] = P_{x_p}$ è una quantità **reale**, risulta $R_{x_cx_s}(0) = 0 = R_{x_sx_c}(0)$ (la slide lo accompagna con la domanda «Perché?»: è la parte immaginaria di (12) per $\tau = 0$). Significa che, per ogni istante $t_0$, le variabili aleatorie a media nulla $x_c(t_0)$ e $x_s(t_0)$ sono **incorrelate** (infatti $C_{x_cx_s}(0) = R_{x_cx_s}(0) - \mu_{x_s}\mu_{x_c} = 0$). Quindi $x_c(t_0)$ e $x_s(t_0)$ sono **statisticamente indipendenti** per ogni $t_0$ se sono gaussiane.

### PSD delle componenti e dell'inviluppo

#### Slide 7 e appunti — PSD delle componenti in quadratura · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]], [[Rappresentazione_Rice_processi.pdf#page=13|13]]
- Per il teorema di Wiener-Khinchin la PSD delle componenti si ottiene trasformando (6) e (7). Per la componente in fase, con $R_{x_cx_c}(\tau) = \frac12\big[R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau)\big]$:

$$
\begin{aligned}
S_{x_cx_c}(f) &= \frac12\bigg[\frac{S_{x_px_p}(f-f_c) + S_{x_px_p}(f+f_c)}{2} + \frac{-j\,S_{x_px_p}(f-f_c)\,\text{sgn}(f-f_c) + j\,S_{x_px_p}(f+f_c)\,\text{sgn}(f+f_c)}{2j}\bigg] \\
&= \frac12\bigg[S_{x_px_p}(f-f_c)\,\frac{1 - \text{sgn}(f-f_c)}{2} + S_{x_px_p}(f+f_c)\,\frac{1 + \text{sgn}(f+f_c)}{2}\bigg] \\
&= \frac12\Big[S_{x_px_p}(f-f_c)\,u(-f+f_c) + S_{x_px_p}(f+f_c)\,u(f+f_c)\Big]
\end{aligned} \tag{13}
$$

  con $1 - \text{sgn}(f-f_c) = 2u(-f+f_c)$ e $1 + \text{sgn}(f+f_c) = 2u(f+f_c)$.
- Poiché $R_{x_cx_c}(\tau) = R_{x_sx_s}(\tau)$, si ha $S_{x_cx_c}(f) = S_{x_sx_s}(f)$.
- Le **cross-spectral density** di $x_c$ e $x_s$ si ottengono trasformando (8) e (9), sfruttando $R_{x_cx_s}(\tau) = -R_{x_sx_c}(\tau)$.

#### Slide 8 e appunti — Osservazione importante (1/2): PSD dell'inviluppo · [[Rappresentazione_Rice_processi.pdf#page=14|p. 14]], [[Rappresentazione_Rice_processi.pdf#page=15|15]], [[Rappresentazione_Rice_processi.pdf#page=16|16]]
- Il segnale analitico si ottiene filtrando $x_p(t)$ con $H(f) = \sqrt2\,u(f)$; ricordando che per un filtro LTI $S_{\text{out}}(f) = S_{\text{in}}(f)\,|H(f)|^2$:

$$S_{x_p^+x_p^+}(f) = S_{x_px_p}(f)\,|H(f)|^2 = 2S_{x_px_p}(f)\,u(f)$$

  Il segnale analitico annulla completamente le frequenze negative e **raddoppia la potenza delle frequenze positive**.
- Da $x(t) = x_p^+(t)\,e^{-j2\pi f_ct}$:

$$R_{xx}(\tau) = E[x(t)\,x^\ast(t-\tau)] = R_{x_p^+x_p^+}(\tau)\,e^{-j2\pi f_c\tau}$$

  cioè dipende unicamente dal ritardo: **la moltiplicazione per un esponenziale complesso conserva la stazionarietà in senso lato (WSS)**.
- Di conseguenza la PSD dell'inviluppo è la PSD del segnale analitico **traslata nell'origine** (spostata a sinistra di $f_c$):

$$S_{xx}(f) = S_{x_p^+x_p^+}(f + f_c) = 2S_{x_px_p}(f + f_c)\,u(f + f_c) \tag{14}$$

- **In conclusione**, per ottenere la PSD dell'inviluppo di un processo passa-banda si deve: (1) vedere la PSD del segnale passa-banda $S_{x_px_p}(f)$; (2) eliminare le frequenze negative con $H(f) = \sqrt2\,u(f)$ e moltiplicare per $\sqrt2$ (permette di preservare la potenza originaria del segnale), ottenendo $2S_{x_px_p}(f)\,u(f)$; (3) traslare a sinistra di $f_c$, portando la PSD del segnale analitico centrata nell'origine.

#### Slide 9 e appunti — Osservazione importante (2/2): spettro simmetrico · [[Rappresentazione_Rice_processi.pdf#page=17|p. 17]], [[Rappresentazione_Rice_processi.pdf#page=18|18]], [[Rappresentazione_Rice_processi.pdf#page=19|19]]
- Caso particolare molto frequente nei sistemi di trasmissione: la PSD del processo reale $S_{x_px_p}(f)$ è **simmetrica rispetto alla frequenza portante $f_c$**.
- Dalla relazione (14) la PSD dell'inviluppo è una funzione **pari**: $S_{xx}(-f) = S_{xx}(f)$. Infatti $S_{xx}(-f) = 2S_{x_px_p}(-f+f_c)\,u(-f+f_c) = 2S_{x_px_p}(f+f_c)\,u(f+f_c)$, perché $S_{x_px_p}$ è pari rispetto a $f_c$.
- Essendo $S_{xx}(f) = \mathcal{F}\{R_{xx}(\tau)\}$, per le proprietà della trasformata di Fourier l'antitrasformata di una funzione pari e reale è anch'essa pari e reale: $R_{xx}(\tau)$ è **reale e pari**, quindi $\text{Im}\{R_{xx}(\tau)\} = 0$ per ogni $\tau$.
- Dalla (12), $R_{xx}(\tau) = 2R_{x_cx_c}(\tau) + j2R_{x_sx_c}(\tau)$, segue (con $x_p$ WSS)

$$R_{x_sx_c}(\tau) = 0 \ \Rightarrow\ R_{x_cx_s}(\tau) = -R_{x_sx_c}(\tau) = 0 \qquad \forall\tau$$

  Quindi $x_c(t)$ e $x_s(t)$ sono **incoerenti**. Se $x_p(t)$ ha anche media nulla, sono **incorrelate**, e **statisticamente indipendenti** supponendo $x_p$ gaussiano.
- In questa situazione, dalla (12): $S_{xx}(f) = 2S_{x_cx_c}(f) = 2S_{x_sx_s}(f)$.
- Mentre l'incoerenza in generale è garantita solo nel singolo istante ($\tau = 0$), quando lo spettro è simmetrico attorno a $f_c$ le due componenti $x_c(t)$ e $x_s(t)$ sono **completamente incoerenti/incorrelate** per ogni $\tau \in \mathbb{R}$.

#### Slide 10 — Vista grafica · [[Rappresentazione_Rice_processi.pdf#page=20|p. 20]]

![[processi-passabanda-p20-vista-grafica-psd.png|650]]
*(a) $S_{x_px_p}(f)$: lobi di altezza $A$ in $\pm f_c$, larghezza $W$. (b) Il processo analitico $S_{x_p^+x_p^+}(f)$: si elimina lo spettro a frequenze negative e si moltiplica per 2 ($|H(f)|^2 = 2u(f)$): altezza $2A$ in $f_c$. (c) $S_{xx}(f)$: traslazione di $-f_c$, secondo la (14); è **pari**, quindi $R_{xx}(\tau)$ è reale. (d) Dividendo per 2: $S_{x_cx_c}(f) = S_{x_sx_s}(f)$, altezza $A$ su $|f| < W/2$.*

- Se $S_{x_px_p}(f)$ è simmetrica attorno a $f_c$, allora $S_{xx}(f)$ è pari $\Rightarrow R_{x_sx_c}(\tau) = 0$ e $S_{xx}(f) = 2S_{x_cx_c}(f) = 2S_{x_sx_s}(f)$.
- Note a mano sulla slide: da $R_{xx}(\tau) = 2R_{x_cx_c}(\tau) + j2R_{x_sx_c}(\tau)$ si ha $S_{xx}(f) = 2S_{x_cx_c}(f) + j2S_{x_sx_c}(f)$, e con $R_{x_sx_c} = 0$ resta $S_{xx}(f) = 2S_{x_cx_c}(f)$; $S_{xx}(f)$ è reale per definizione, $S_{xx}(f) = \lim_{T\to\infty}\frac{1}{2T}E\big[|X_T(f)|^2\big]$.

### Esempio: rumore in banda passante

#### Slide 11 e appunti — Rumore in banda · [[Rappresentazione_Rice_processi.pdf#page=21|p. 21]], [[Rappresentazione_Rice_processi.pdf#page=22|22]], [[Rappresentazione_Rice_processi.pdf#page=23|23]]
- Si consideri un rumore passa-banda $w_p(t)$ con PSD costante $S_{w_pw_p}(f) = N_0/2$ su una banda $W$.
- Un **rumore bianco gaussiano (AWGN)**, con $R_{w_pw_p}(\tau) = \frac{N_0}{2}\delta(\tau)$, ha PSD costante $N_0/2$ su tutte le frequenze $(-\infty, +\infty)$, quindi potenza media infinita. Nei sistemi reali il ricevitore **filtra** il segnale in ingresso con un filtro di banda $W$ centrato su $f_c$, ottenendo un rumore con $S(f) = N_0/2$ e banda pari a $W$.
- Si calcolano le PSD $S_{w_cw_c}(f)$ e $S_{w_sw_s}(f)$ delle componenti in quadratura. Si vede facilmente che

$$S_{w_cw_c}(f) = S_{w_sw_s}(f) = \frac{N_0}{2} \quad \text{per } |f| < \frac W2$$

  Infatti $S_{ww}(f) = 2S_{w_pw_p}(f+f_c)\,u(f+f_c) = 2\cdot\frac{N_0}{2} = N_0$ per $|f| < W/2$; essendo $S_{w_pw_p}(f)$ reale e costante, e quindi pari rispetto alla banda, $S_{ww}(f) = 2S_{w_cw_c}(f)$.
- È utile notare che la **potenza** del processo passa-banda originale è $P_{w_p} = 2W\cdot\frac{N_0}{2} = N_0W$ e **coincide con la potenza dell'inviluppo complesso**.
- Le condizioni (10) sono di particolare importanza: le proprietà di correlazione dell'inviluppo complesso di un qualunque processo passa-banda WSS si specificano con l'acf della componente in fase e la crosscorrelazione tra le componenti in quadratura. Inoltre, la componente in fase e quella in quadratura nello stesso istante sono **incorrelate**: le componenti in quadratura di un processo gaussiano complesso nello stesso istante sono **statisticamente indipendenti**.
- Appunti p. 23: essendo $S_{ww}(f)$ reale, $S_{w_cw_s}(f) = 0$ per ogni $f \in \mathbb{R}$: sono incoerenti, quindi incorrelate, quindi statisticamente indipendenti se $w_p$ è gaussiano.

#### Slide 12–13 — Costruzione grafica di $S_{w_cw_c}(f)$ · [[Rappresentazione_Rice_processi.pdf#page=24|p. 24]], [[Rappresentazione_Rice_processi.pdf#page=25|25]]
- Applicando la (13) a $S_{w_pw_p}(f)$: prima si trasla la PSD passa-banda di $\pm f_c$, poi si moltiplica per i gradini unitari $u(f_c - f)$ e $u(f+f_c)$.

![[processi-passabanda-p24-rumore-costruzione-1.png|560]]
*(a) $S_{w_pw_p}(f)$: due lobi di altezza $N_0/2$ e larghezza $W$ in $\pm f_c$. (b) $S_{w_pw_p}(f-f_c)$: traslata di $+f_c$ (lobi in $0$ e $2f_c$). (c) $S_{w_pw_p}(f+f_c)$: traslata di $-f_c$ (lobi in $-2f_c$ e $0$). (d) $u(f_c - f)$. (e) $u(f + f_c)$.*

- Ogni gradino unitario trattiene solo il lobo che cade attorno a $f = 0$; sommando e dimezzando si ottiene $S_{w_cw_c}(f) = S_{w_sw_s}(f) = N_0/2$ per $|f| < W/2$.

![[processi-passabanda-p25-rumore-costruzione-2.png|560]]
*(f) $S_{w_pw_p}(f-f_c)\,u(f_c-f)$ e (g) $S_{w_pw_p}(f+f_c)\,u(f+f_c)$: restano i lobi in 0 (le copie in $\pm 2f_c$ sono barrate). (h) $\frac12[(f)+(g)]$ (eq. (13)): $S_{w_cw_c}(f) = S_{w_sw_s}(f)$, con i due contributi di altezza $N_0/4$ che insieme valgono $N_0/2$. (i) $S_{ww}(f) = 2S_{w_cw_c}(f)$, altezza $N_0$, ×2.*

- Poiché $S_{w_pw_p}(f)$ è simmetrica attorno a $f_c$: $S_{ww}(f) = 2S_{w_cw_c}(f) = N_0$ per $|f| < W/2$, e $P_{w_p} = N_0W = P_w$.

---

*Approfondimenti nel wiki (derivazioni passo per passo, controlli, cross-PSD): [[processi-passa-banda]], [[psd-componenti-in-quadratura]], [[rumore-in-banda-passante]]; sul caso deterministico [[inviluppo-complesso]] e [[segnale-analitico]].*


## Lezione 8 — Principi di modulazione

*Fonte: Modulazione.pdf (copia GoodNotes in `raw/goodnotes/`, 39 pagine: le 23 slide «Principles of modulation» più 16 pagine di appunti a lezione alle p. 3, 5, 9–11, 13, 15, 17–19, 21, 22, 24, 25, 27, 32). Corrispondenza: slide 1–2 = p. 1–2, 3 = p. 4, 4–6 = p. 6–8, 7 = p. 12, 8 = p. 14, 9 = p. 16, 10 = p. 20, 11 = p. 23, 12 = p. 26, 13–17 = p. 28–31 e 33, 18–23 = p. 34–39. Le equazioni (1)–(4) sono quelle delle slide.*

### Il modulatore digitale

#### Slide 2 e appunti — Struttura del modulatore · [[Modulazione.pdf#page=2|p. 2]], [[Modulazione.pdf#page=3|3]]
- Il **modulatore digitale** è composto da due stadi in cascata: il **mapper**, che converte la sequenza di bit in ingresso in simboli, e il **generatore di forme d'onda**, che associa a ciascun simbolo una forma d'onda da inviare sul canale (schema: dal codificatore di canale, bit $b_k$ → mapper → simboli $\xi_k$ → generatore → segnali $s(t;\xi_k)$ → al canale).
- Una sequenza di bit $\{b_k\}$ con **bit rate** $R_b=1/T_b$ (bit/s) alimenta il mapper: è la velocità con cui i bit alimentano il modulatore.
- Il bit rate così definito conta tutti i bit trasferiti fisicamente, cioè sia quelli d'informazione sia quelli di ridondanza (codifica di canale) o di protocollo: è un **raw bit rate**.

#### Slide 3 e appunti — Simboli, baud rate, memoria · [[Modulazione.pdf#page=4|p. 4]], [[Modulazione.pdf#page=5|5]]
- Il mapper raggruppa i bit in blocchi $\xi_k\triangleq[b_k,b_{k+1},\dots,b_{k+h-1}]$ di lunghezza $h$, detti **simboli di sorgente** o **messaggi**. Ogni simbolo assume uno degli $M=2^h$ valori dell'insieme $\mathcal M=\{m_i\}_{i=1}^M$, ciascuno con probabilità $P(m_i)$. (Appunti: con $h=1$ il mapper non fa nulla.)
- Il mapper emette un simbolo ogni $T=hT_b$ secondi (**periodo di simbolo**), quindi il

$$R_s\triangleq\frac1T=\frac{1}{hT_b}=\frac{R_b}{\log_2M}$$

  è il **symbol rate** o **baud rate** (simboli/s, baud): il numero di forme d'onda trasmesse dal modulatore nell'unità di tempo, detto anche **signaling rate**.
- Il generatore associa a ogni simbolo una forma d'onda presa da un insieme di $M$ forme d'onda. La corrispondenza può essere **senza memoria** (biunivoca: la forma d'onda dipende solo da $\xi_k$) o **con memoria** (dipende anche da $\xi_{k-1},\dots,\xi_{k-L}$, con $L\ge1$ memoria della modulazione).
- Appunti a lezione: con la memoria si possono raccordare dolcemente le transizioni da un simbolo all'altro: si contiene la banda, ma si rallenta il sistema (un simbolo viene inviato solo dopo $T$).

### Un esempio e il compromesso potenza-banda

#### Slide 4–5 — Esempio di Benedetto-Biglieri · [[Modulazione.pdf#page=6|p. 6]], [[Modulazione.pdf#page=7|7]]
- Il modulatore usa $M$ segnali $\{s_i(t)\}_{i=1}^M$ di durata $T=hT_s$ ($T_s$ tempo di bit). Per $M=2$: $s_1=+A$, $s_2=-A$ su $[0,T_s)$; per $M=4$: $-3A,-A,+A,+3A$ su $[0,2T_s)$; per $M=8$: $s_i=(2i-9)A$, $i=1,\dots,8$, su $[0,3T_s)$. Ogni segnale dura $hT_s$: a parità di rate della sorgente, la durata è proporzionale a $h$ (appunti: è la distanza tra un simbolo e il successivo).
- La figura mostra la stessa sequenza binaria $1\,0\,0\,1\,0\,1\,1\,1\,1\,0\,0\,0$ trasmessa con $M=2$ ($T=T_s$), $M=4$ ($T=2T_s$, livelli $\pm A,\pm3A$) e $M=8$ ($T=3T_s$, livelli da $-7A$ a $+7A$). Appunti: l'ampiezza $+A$ ha ripercussione diretta sull'SNR; schizzi di segnale in banda base (canale) e in banda passante (up → canale → down).
- Mapping della figura: $M=4$: 10 → $+3A$, 11 → $+A$, 01 → $-A$, 00 → $-3A$; $M=8$: 111 → $+7A$, 101 → $+5A$, 100 → $+3A$, 110 → $+A$, 010 → $-A$, 011 → $-3A$, 001 → $-5A$, 000 → $-7A$.

> ⚠️ Errore nella figura, riga con $M=8$: la sequenza si divide in 100, 101, 111, 000, quindi i livelli dovrebbero essere $+3A,+5A,+7A,-7A$. Nella figura il terzo simbolo (111) è disegnato a $-A$, che secondo la tabella accanto corrisponde a 010. Le righe con $M=2$ e $M=4$ sono corrette.

#### Slide 6 e appunti — Come scegliere la modulazione · [[Modulazione.pdf#page=8|p. 8]]–[[Modulazione.pdf#page=11|11]]
- Uno schema di modulazione è il procedimento con cui una sequenza numerica di bit viene convertita in un segnale analogico a tempo continuo. La scelta è un **compromesso** tra complessità, efficienza di potenza ed efficienza di banda (appunti: i segnali dell'esempio sono tutti segnali PAM).
- A bit rate costante, le forme d'onda con $M=8$ richiedono meno banda di quelle con $M=2$ perché l'impulso dura di più: **aumentare $M$ riduce in generale l'occupazione di banda** (appunti: $M=2$, un simbolo per bit, durata $T=T_s$; $M=8$, un simbolo ogni 3 bit, durata $3T_s$; durata e banda sono inversamente proporzionali).
- Se il budget di potenza è fisso al variare di $M$, con il rumore il demodulatore distingue peggio i segnali quando $M$ è grande, perché i livelli sono più vicini (appunti: con $M=2$ si distinguono 2 livelli lontani, con $M=8$ otto livelli vicini): **compromesso potenza-banda**. Appunti (p. 10): aumentare $M$ fa risparmiare banda (efficienza di banda), ma rende il segnale più fragile al rumore (efficienza di potenza): per mantenere la stessa affidabilità serve più potenza.
- Dalla teoria dei segnali, la regolarità di una funzione nel tempo è legata alla rapidità con cui decade la sua trasformata: per uno spettro più stretto si «smussano» le discontinuità della forma d'onda ⇒ **modulazione con memoria** (appunti, alla voce complessità: gli impulsi a gradino generano code spettrali che decadono lentamente; con la memoria nel generatore di forme d'onda il simbolo corrente si raccorda con i precedenti, si eliminano le discontinuità di ampiezza e fase e lo spettro diventa più stretto e compatto).
- Appunti a lezione (p. 11), sulla banda occupata. Per una modulazione lineare la densità spettrale di potenza del segnale è

$$S_{xx}(f)=\frac1T\,S_{aa}(fT)\,|P(f)|^2$$

  con $T$ periodo di simbolo, $S_{aa}$ spettro della sequenza dei simboli e $P(f)$ trasformata dell'impulso $p(t)$. Il bit rate è $R_b=1/T_b$.
  - Se $p(t)$ è un rettangolo di durata $T$, allora $|P(f)|^2\propto\text{sinc}^2(fT)$. Lo schizzo mostra un lobo principale con il primo zero in $f=1/T$, seguito da lobi laterali piccoli.
  - Quindi la banda è dell'ordine di $1/T$: simboli più lunghi (cioè $M$ più grande) occupano meno banda.
  - C'è un compromesso tra potenza del segnale e banda, perché il budget di potenza è limitato. Nota riquadrata: fissare il budget significa fissare un intervallo sull'asse delle ascisse (🧩 sulla pagina l'unico asse delle ascisse è quello delle frequenze dello schizzo, quindi la nota lega il budget a un intervallo di frequenze, cioè alla banda).

### Rappresentazione discreta e spazio dei segnali

#### Slide 7 e appunti — Rappresentazione discreta dei segnali (1/2) · [[Modulazione.pdf#page=12|p. 12]], [[Modulazione.pdf#page=13|13]]
- Nella forma più semplice il modulatore mappa ogni messaggio su un insieme di $M$ forme d'onda $\mathcal S=\{s_i(t)\}_{i=1}^M$ trasmesse in sequenza (appunti: ogni simbolo è mappato su una singola forma d'onda dell'insieme). Esiste una grande varietà di schemi di modulazione digitale, cioè di regole di mapping.
- Lavorare con funzioni del tempo è analiticamente e computazionalmente complesso: conviene associare a ogni $s_i(t)$ una **rappresentazione discreta**, una sequenza $s_i(\ell)$ raccolta nel vettore $\mathbf s_i$. Così la comunicazione si descrive in uno **spazio vettoriale** di dimensione finita o infinita numerabile, e l'analisi si riduce a operazioni geometriche tra vettori.
- Se il segnale è a banda limitata si prendono i campioni equispaziati (teorema del campionamento di Nyquist); per segnali periodici, i coefficienti della serie di Fourier.

#### Slide 8 e appunti — Rappresentazione discreta (2/2) · [[Modulazione.pdf#page=14|p. 14]], [[Modulazione.pdf#page=15|15]]
- Canale passa-banda idealmente limitato $f_c-W/2\le f\le f_c+W/2$: presa $f_c$ come riferimento, equivale a un canale complesso in banda base su $[-W/2,W/2]$ (appunti: l'inviluppo complesso). Il progetto del modulatore diventa la scelta di forme d'onda complesse in banda base limitate a $[-W/2,W/2]$, indipendentemente da $f_c$.
- Per il teorema del campionamento $s_i(t)$ è determinata dai campioni $s_i(\ell/W)$ presi a frequenza $W$, e si ricostruisce con

$$s_i(t)=\sum_{\ell=-\infty}^{+\infty}s_i\Big(\frac{\ell}{W}\Big)\,p\Big(t-\frac{\ell}{W}\Big),\qquad p(t)=\text{sinc}(Wt)$$

- Appunti: $s_i(\ell/W)$ è la $\ell$-esima componente discreta associata alla $i$-esima forma d'onda; con la somma da $-\infty$ a $+\infty$ bisogna associare infinite componenti.

#### Slide 9 e appunti — Gradi di libertà della modulazione · [[Modulazione.pdf#page=16|p. 16]]–[[Modulazione.pdf#page=19|19]]
- Basta specificare i campioni $s_i(\ell/W)$, ma su tutto l'asse dei tempi il vettore dei campioni ha dimensione infinita.
- Nessun segnale limitato nel tempo è limitato in banda: $x_{T_0}(t)=x(t)\,\text{rect}(t/T_0)\Leftrightarrow X_{T_0}(f)=X(f)\ast T_0\,\text{sinc}(fT_0)$ (appunti: i segnali desiderati sono a banda limitata perché il canale si comporta come un filtro passa-banda; troncandoli nel tempo, la convoluzione con la sinc allarga la banda).
- Se però i segnali occupano un intervallo $T_0$ abbastanza lungo da considerarli approssimativamente a banda limitata, il modulatore deve specificare circa $WT_0$ campioni complessi: l'insieme dei segnali sta in un sottospazio complesso di dimensione $WT_0$, cioè reale di dimensione $2WT_0$ (appunti: ogni valore complesso porta 2 gradi di libertà reali).
- Il massimo numero di dimensioni dello spazio dei segnali complessi (**gradi di libertà**) è il prodotto tempo-banda $D=WT_0$; in pratica il numero effettivo è minore, per vincoli implementativi.
- Appunti (p. 18–19): l'obiettivo è rappresentare una forma d'onda con un numero finito di valori senza perdere informazione. Usare tutti i $D$ campioni è ridondante se si usano solo $M$ forme d'onda: $D$ sono i gradi di libertà offerti dal canale, $n\le M\le D$ quelli usati davvero, perché le $M$ forme d'onda stanno in un sottospazio di dimensione $n$ (alcune possono essere combinazioni lineari delle altre). Con una base ortonormale di quel sottospazio ogni $s_i(t)$ diventa un vettore di $n$ componenti: si lavora nello spazio di dimensione minima. Riquadro riassuntivo negli appunti: Nyquist e $D$ servono a giustificare che il problema continuo si può ridurre a un numero finito di valori (dimostrano che l'approssimazione è fattibile); lo sviluppo su base ortonormale con $n$ componenti è la rappresentazione compatta usata in pratica dal ricevitore per calcolare le distanze euclidee e decidere sui simboli trasmessi.

#### Slide 10 e appunti — Descrizione nello spazio dei segnali · [[Modulazione.pdf#page=20|p. 20]]–[[Modulazione.pdf#page=22|22]]
- L'insieme $\mathcal S$ sta in uno spazio di dimensione finita: si lavora con i vettori $\mathbf s_i$. Sia $n\le M$ la dimensione dello spazio generato. Ogni segnale si rappresenta con $\mathbf s_i=[s_i(1),\dots,s_i(n)]^T$ rispetto a una **base ortonormale** $\psi_1(t),\dots,\psi_n(t)$:

$$\langle\psi_k(t),\psi_\ell(t)\rangle=\delta_{k\ell},\qquad s_i(t)=\sum_{\ell=1}^{n}s_i(\ell)\,\psi_\ell(t),\qquad s_i(\ell)=\langle s_i(t),\psi_\ell(t)\rangle=\int_{\mathcal T}s_i(t)\,\psi_\ell^\ast(t)\,dt$$

- Prodotti scalari e distanze euclidee si conservano passando dai segnali ai vettori: $\langle s_i(t),s_j(t)\rangle=\langle\mathbf s_i,\mathbf s_j\rangle$.
- Appunti (p. 20–21): $n$ è la dimensione effettiva; lo spazio è finito grazie all'approssimazione di banda e durata limitate ($T_0$ grande); i segnali di energia formano uno spazio vettoriale, e allo spazio dei segnali complessi si associa uno spazio euclideo con una corrispondenza 1:1.
- Appunti (p. 22): la verifica sviluppa entrambi i segnali sulla base e usa l'ortonormalità, $\int\psi_\ell\psi_k^\ast\,dt=\delta_{\ell k}$. Perché importa: per calcolare energia dei segnali, effetto del rumore e decisioni del ricevitore basta la distanza euclidea tra punti di uno spazio a $n$ dimensioni. I punti della costellazione generano un sottospazio di dimensione $n$ dentro lo spazio di dimensione $D$ offerto dal canale.

### Modulazione lineare

#### Slide 11 e appunti — Modulazione lineare · [[Modulazione.pdf#page=23|p. 23]]–[[Modulazione.pdf#page=25|25]]
- Ci si concentra sul caso più generale dei sistemi passa-banda: l'informazione è codificata in una forma d'onda complessa in banda base (l'inviluppo). I sistemi reali in banda base sono un caso particolare (appunti: prima si era trattato il caso particolare con componente in quadratura nulla).
- Segnale modulato linearmente in banda base complessa:

$$s(t)=\sum_{k=-\infty}^{+\infty}\xi_k\,g_{TX}(t-kT)$$

  con $T$ periodo di simbolo, $\{\xi_k\}$ simboli trasmessi a rate $1/T$ con valori in un alfabeto fisso (**costellazione**), $g_{TX}(t)$ forma d'onda deterministica in banda base.
- Appunti: i simboli si modellano come una sequenza di v.a. i.i.d.; la costellazione è fissata quando si fissa $h$. Lo spazio dei segnali complessi ha dimensione 2 (parte reale in fase, parte immaginaria in quadratura); con simboli reali il canale può essere un passa-basso o un passa-banda con filtro simmetrico rispetto a $f_c$, e la dimensione è 1.

#### Slide 12 e appunti — Codici di linea in banda base · [[Modulazione.pdf#page=26|p. 26]], [[Modulazione.pdf#page=27|27]]
- Se il canale fisico è in banda base, $s(t)$ è trasmesso direttamente e deve essere **reale**. I metodi per mappare bit in forme d'onda analogiche reali sono i **codici di linea**.
- Sorgente che emette bit $b_k\in\{0,1\}$ a rate $R_b=1/T_b$ con $p=P(b_k=1)$, $q=P(b_k=0)$, $p+q=1$ (processo di Bernoulli), bit statisticamente indipendenti e identicamente distribuiti.

#### Slide 13–14 — NRZ e RZ · [[Modulazione.pdf#page=28|p. 28]], [[Modulazione.pdf#page=29|29]]
- **NRZ**: $\xi_k=(-1)^{b_k}\in\{-1,1\}$ ($R_b=R_s=1/T$), $g_{TX}(t)=A\,\text{rect}\big(\frac{t-0.5T}{T}\big)$:

$$s(t)=A\sum_{k}\xi_k\,\text{rect}\Big(\frac{t-0.5T-kT}{T}\Big)$$

  Le forme d'onda sono multipli scalari di un'unica forma d'onda, $\{-Ag_{TX}(t),Ag_{TX}(t)\}$ (appunti: modulazione con cardinalità $M=2$ e dimensione 1). Figura: una realizzazione che salta tra $+A$ e $-A$. È usata nel protocollo CAN.
- **RZ**: $g_{TX}(t)=A\,\text{rect}\big(\frac{t-0.25T}{0.5T}\big)$, l'impulso occupa solo metà intervallo e torna a zero. Per NRZ e RZ l'insieme dei segnali è **unidimensionale** (appunti: entrambe vanno bene per canali in banda base, perché i simboli sono reali e si assume un canale in banda base).

### Modulazione lineare passa-banda

#### Slide 15 — I/Q e conversione · [[Modulazione.pdf#page=30|p. 30]]
- In passa-banda i simboli possono essere complessi: si rappresentano su un piano (**modulazione bidimensionale**). Con $g_{TX}(t)$ reale (appunti: forma d'onda deterministica in banda base):

$$s_c(t)=\sum_k\text{Re}(\xi_k)\,g_{TX}(t-kT)\quad(1)\qquad s_s(t)=\sum_k\text{Im}(\xi_k)\,g_{TX}(t-kT)\quad(2)$$

- L'inviluppo $s(t)=s_c(t)+js_s(t)$ si porta in banda passante con l'upconverter ($\sqrt2\cos2\pi f_ct$, $-\sqrt2\sin2\pi f_ct$, somma) prima di trasmetterlo sul canale fisico; il downconverter (moltiplicatori e passa-basso) restituisce $s_c(t)$, che contiene la parte reale dei simboli, e $s_s(t)$, che ne contiene la parte immaginaria.

#### Slide 16 e appunti — PSK · [[Modulazione.pdf#page=31|p. 31]], [[Modulazione.pdf#page=32|32]]
- **Phase shift keying**: si sceglie $\arg(\xi_k)$ in una costellazione a modulo costante, $\xi_k=e^{j\Phi_k}$, con $\Phi_k\in\big\{\frac{2\pi}{M}(i-1)+\Phi\big\}_{i=1}^M$ ($\Phi$ fase costante arbitraria, $R_b=\log_2M/T$). Appunti: l'informazione è contenuta nella fase; $\Phi_k$ è un processo aleatorio discreto a tempo discreto; modulazione a modulo costante, ogni simbolo ha modulo unitario.
- Costellazioni per $M=4$ (QPSK) e $M=8$. Componenti:

$$s_c(t)=A\sum_k\cos(\Phi_k)\,g_{TX}(t-kT)\quad(3)\qquad s_s(t)=A\sum_k\sin(\Phi_k)\,g_{TX}(t-kT)\quad(4)$$

  con $A$ fattore di ampiezza (appunti: permette di gestire la potenza del segnale).
- Appunti (p. 32): **mapping di Gray**: a simboli a distanza minima si assegnano sequenze di bit che differiscono per un solo bit (QPSK: 00, 01, 11, 10 in giro sul cerchio). Così l'errore più probabile del ricevitore (scambiare un simbolo con un vicino) costa un solo bit. Il problema della PSK: il modulo è costante, quindi aumentando $M$ la costellazione si affolla e la distanza tra simboli diminuisce; per allontanarli bisogna aumentare la potenza.

#### Slide 17–18 — QAM e PAM · [[Modulazione.pdf#page=33|p. 33]], [[Modulazione.pdf#page=34|34]]
- **QAM**: variano sia $|\xi_k|$ sia $\arg(\xi_k)$; di solito la costellazione è una griglia di $M$ punti regolarmente spaziati (figura: QPSK, 8-PSK e 16-QAM). Appunti: i punti si dispongono su un piano; in tutte queste costellazioni la successione dei simboli ha media nulla, se ogni simbolo è equiprobabile.
- **PAM**: se $\xi_k$ è reale la QAM diventa modulazione d'ampiezza, con livelli equispaziati

$$a_i=(2i-1-M)\frac d2,\qquad i=1,\dots,M$$

  Figura per $d=2$: $M=4$ con livelli $-3,-1,1,3$ (Gray 00, 10, 11, 01) e $M=8$ con livelli da $-7$ a $7$ (000, 001, 101, 100, 110, 111, 011, 010). La PAM è **unidimensionale** (appunti: si suppone un canale in banda base).

#### Slide 19 — Scelte di progetto · [[Modulazione.pdf#page=35|p. 35]]
- Nei sistemi modulati linearmente si scelgono: la forma dell'impulso $g_{TX}(t)$, il symbol rate $R_s=1/T$, la costellazione, il mapping bit-simboli. Symbol rate e forma dell'impulso dipendono soprattutto dalla banda disponibile; il resto si vedrà nelle lezioni successive.
- Appunti:
  - $g_{TX}(t)$ determina lo spettro e la banda occupata dal segnale sul canale;
  - $R_s$ è limitato superiormente dalla banda passante disponibile ($R_s\le W$);
  - la costellazione è l'insieme dei valori su cui si mappano gli $h$ bit: sono $2^h=M$;
  - il mapping è, per esempio, quello di Gray;
  - $T$ è la durata della forma d'onda: diminuendola la banda aumenta, e si sforerebbe la banda $W$ del canale. Schizzo: impulso rettangolare e il suo spettro, con gli zeri in $\pm1/T=\pm R_s$ confrontati con $\pm W$.

### Occupazione spettrale e modulazione ortogonale

#### Slide 20–21 — Occupazione spettrale · [[Modulazione.pdf#page=36|p. 36]], [[Modulazione.pdf#page=37|37]]
- Con $\xi_k$ i.i.d. a media nulla e valore quadratico medio $E[|\xi_k|^2]$ (appunti: $=\sigma_\xi^2$), la PSD di $s(t)=\sum_k\xi_kg_{TX}(t-kT)$ è

$$S_{ss}(f)=\frac{E[|\xi_k|^2]}{T}\,|G_{TX}(f)|^2$$

  con $G_{TX}(f)$ trasformata dell'impulso (figura: PSD per impulso rettangolare in funzione di $fT$, lobo principale tra $-1$ e $1$). Appunti: in generale $E[\xi_k\xi_{k-m}^\ast]=\sigma_\xi^2\delta(m)+|\mu_\xi|^2$, che con media nulla dà la formula.
- Con simboli i.i.d. la forma della PSD è determinata solo dallo spettro dell'impulso. Per un processo la banda si definisce sulla PSD; si usa la banda **bilatera** dell'inviluppo complesso, che coincide con la banda monolatera fisica del segnale passa-banda.

#### Slide 22–23 — Modulazione ortogonale · [[Modulazione.pdf#page=38|p. 38]], [[Modulazione.pdf#page=39|39]]
- Nella modulazione ortogonale lo spazio dei segnali ha dimensione $n=M$ ($R_b=\log_2M/T$). Esempio classico: **FSK**, modulazione **non lineare** (appunti: l'informazione si trova nella frequenza; lo schema va bene solo in banda base):

$$s_i(t)=e^{j2\pi f_it}g_{TX}(t),\qquad i=1,\dots,M$$

  con le spaziature $|f_i-f_k|$ scelte per rendere ortogonali le forme d'onda.
- Condizione di ortogonalità sui segnali passa-banda $s_{i,p}(t)=\text{Re}(\sqrt2\,s_i(t)e^{j2\pi f_ct})$:

$$\langle s_{i,p}(t),s_{k,p}(t)\rangle=\text{Re}(\langle s_i(t),s_k(t)\rangle)=0$$

  (nota della slide: esiste un'altra condizione per i sistemi **non coerenti**, senza riferimento di fase accurato).
- Dall'esercizio 2.25 (Madhow, riportato nella slide): per $s_0=\cos(2\pi f_0t+\phi_0)$ e $s_1=\cos(2\pi f_1t+\phi_1)$ su $[0,T]$, con $f_1>f_0\gg1/T$, la minima spaziatura che dà ortogonalità è $1/(2T)$ con $\phi_0=\phi_1=0$ (FSK coerente) e $1/T$ per fasi arbitrarie (FSK non coerente).
- Segnale FSK ortogonale in banda base complessa, con $b_k\in\{2i-1-M\}_{i=1}^M$:

$$s(t)=A\sum_{k}e^{j2\pi\frac{b_k}{2T}(t-kT)}\,g_{TX}(t-kT)$$

---

*Approfondimenti nel wiki: [[principi-di-modulazione]], [[spazio-dei-segnali]], [[modulazione-lineare]], [[modulazione-ortogonale]], [[modulazione-digitale]].*

## Lezione 9 — Elementi di teoria della rivelazione

*Fonte: Detection.pdf (copia GoodNotes in `raw/goodnotes/`, 18 pagine): le 10 pagine di dispense della docente «Elementi di teoria della rivelazione» sono p. 1 e p. 10–18; le p. 2–9 sono appunti a lezione che ne svolgono i passaggi. Le equazioni (I.1)–(IV.2) sono quelle delle dispense.*

### Modulazione on-off e problema della rivelazione

#### Dispense p. 1 e appunti — Modello · [[Detection.pdf#page=1|p. 1]], [[Detection.pdf#page=2|2]]
- Sorgente di bit $\{b_k\}$ a rate $R_b=1/T_b$; il mapper associa $0\to m_0$, $1\to m_1$ ($h=1$, quindi $R_s=R_b$). Il simbolo $\xi_k$ è una v.a. (i.i.d.) con valori in $\mathcal M=\{m_0,m_1\}$, $M=2$, $p=P(m_1)$, $q=P(m_0)$, $p+q=1$.
- Il generatore associa segnali a energia finita: $m_0\to s_0(t)=0$ e $m_1\to s_1(t)=s(t)$ per $t\in(kT_b,(k+1)T_b)$ (**modulazione on-off**, senza memoria).
- Segnalazione in AWGN: $r(t)=s(t;\xi_k)+n(t)$ (I.1), con $n(t)$ rumore termico gaussiano, WSS, a media nulla, indipendente dal segnale, $R_{nn}(\tau)=\frac{N_0}{2}\delta(\tau)$, $S_{nn}(f)=\frac{N_0}{2}$. Un segnale a media nulla con acf impulsiva si dice **bianco**.
- Il rumore bianco ha potenza infinita, ma il modello è comodo ricordando che ogni ricevitore filtra a banda limitata. Per un ricevitore ideale $N_0=kT_0$, con $T_0=290$ K e $k=1.38\cdot10^{-23}$ J/K (costante di Boltzmann).

#### Dispense p. 2 e appunti — Ipotesi e base ortonormale · [[Detection.pdf#page=10|p. 10]], [[Detection.pdf#page=2|p. 2]], [[Detection.pdf#page=3|3]]
- Si deve decidere quale tra $s_0(t)$ e $s_1(t)$ è stato trasmesso osservando $r(t)$ in $(0,T_b)$: **rivelazione simbolo a simbolo**. Ipotesi $H_0=\{$trasmesso «0»$\}$, $H_1=\{$trasmesso «1»$\}$:

$$H_0:\ r(t)=n(t)\qquad H_1:\ r(t)=s(t)+n(t),\qquad t\in(0,T_b)\tag{I.2}$$

  Sotto $H_0$ $r(t)$ è gaussiano a media nulla con acf $\frac{N_0}{2}\delta(\tau)$; sotto $H_1$ gaussiano a media $s(t)$ con autocovarianza $\frac{N_0}{2}\delta(\tau)$.
- Si proietta $r(t)$ su una base ortonormale completa $\{\psi_i(t)\}_{i=1}^{+\infty}$ in $(0,T_b)$, $\langle\psi_i,\psi_j\rangle=\delta_{ij}$, con prima funzione $\psi_1(t)=s(t)/\lVert s(t)\rVert$, $\lVert s\rVert^2=E_s$. Il segnale diventa $(\sqrt{E_s},0,0,\dots)$, il rumore $(n_1,n_2,\dots)$ con $n_i=\langle n(t),\psi_i(t)\rangle$. Appunti: il rumore non si rappresenta in dimensione finita (ha banda infinita, la sua energia è distribuita su tutto lo spettro); $r_1=\langle s+n,\psi_1\rangle=\sqrt{E_s}+n_1$, cioè l'ampiezza energetica del segnale lungo la prima dimensione. (Rimando delle dispense: Benedetto-Biglieri per una trattazione rigorosa dell'espansione dei processi.)

#### Dispense p. 3 e appunti — Proiezioni del rumore e test di ipotesi · [[Detection.pdf#page=11|p. 11]], [[Detection.pdf#page=3|p. 3]]
- Le proiezioni $n_i$ sono v.a. congiuntamente gaussiane, a media nulla e incorrelate:

$$E[n_i]=\int_0^{T_b}E[n(t)]\psi_i(t)\,dt=0,\qquad E[n_in_j]=\iint\frac{N_0}{2}\delta(t-u)\psi_i(t)\psi_j(u)\,dt\,du=\frac{N_0}{2}\delta_{ij}$$

  quindi **statisticamente indipendenti**, con $n_i\sim\mathcal N(0,N_0/2)$. Con $r_i=\langle r(t),\psi_i(t)\rangle$: $H_0:\ r_1=n_1$, $H_1:\ r_1=\sqrt{E_s}+n_1$, e $r_i=n_i$ per $i\ge2$ in entrambe.
- Con vettori troncati $\mathbf r_N$, $\mathbf n_N$, $\mathbf s_N=(\sqrt{E_s},0,\dots,0)$ (poi $N\to\infty$) il problema diventa un **test di ipotesi**: $H_0:\mathbf r_N=\mathbf n_N$, $H_1:\mathbf r_N=\mathbf s_N+\mathbf n_N$. Si passa da funzioni del tempo a punti dello **spazio degli osservabili** $\mathbb R^N$.
- Regola di decisione $\delta:\mathbb R^N\to\{H_0,H_1\}$ con il criterio a **minima probabilità d'errore**, $P(e)\triangleq P(\{\hat m_0\neq m_0\}\cup\{\hat m_1\neq m_1\})$; equivalentemente si partiziona $\mathbb R^N=Z_0\cup Z_1$, $Z_0\cap Z_1=\varnothing$ (**regioni di decisione**).

### Criterio MAP, irrilevanza, filtro adattato

#### Dispense p. 4 e appunti — Criterio MAP e teorema di irrilevanza · [[Detection.pdf#page=12|p. 12]], [[Detection.pdf#page=4|p. 4]], [[Detection.pdf#page=5|5]]
- Probabilità d'errore:

$$P(e)=p\int_{Z_0}f_{\mathbf r_N|H_1}d\mathbf r_N+q\int_{Z_1}f_{\mathbf r_N|H_0}d\mathbf r_N=p-\int_{Z_1}\big[p\,f_{\mathbf r_N|H_1}-q\,f_{\mathbf r_N|H_0}\big]d\mathbf r_N\tag{I.3}$$

  Si minimizza assegnando a $Z_1$ i punti in cui l'integranda è positiva:

$$\frac{f_{\mathbf r_N|H_1}(\mathbf r_N)}{f_{\mathbf r_N|H_0}(\mathbf r_N)}\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \frac qp\tag{I.4}$$

- Per l'indipendenza delle proiezioni il rapporto si riduce al solo $r_1$ (I.5): $(r_2,\dots,r_N)$ sono **irrilevanti** e si eliminano senza degradare le prestazioni (**teorema dell'irrilevanza**); $r_1$ è la **statistica sufficiente**. Con il **rapporto di verosimiglianza** $\Lambda(r)\triangleq f_{r_1|H_1}(r)/f_{r_1|H_0}(r)$ (I.6) la regola è $\Lambda(r)\gtrless q/p$ (I.7): criterio **MAP** (Maximum A Posteriori), ottimo in termini di probabilità d'errore.
- Con $r_1\sim\mathcal N(0,N_0/2)$ sotto $H_0$ e $\mathcal N(\sqrt{E_s},N_0/2)$ sotto $H_1$:

$$\Lambda(r)=\exp\Big\{-\frac{1}{N_0}\big(E_s-2r\sqrt{E_s}\big)\Big\}\tag{I.8}$$

#### Dispense p. 5 e appunti — Log-verosimiglianza, ML, filtro adattato · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=5|p. 5]]
- Log-verosimiglianza:

$$\lambda(r)\triangleq\ln\Lambda(r)=\frac{2}{N_0}\sqrt{E_s}\,r-\frac{E_s}{N_0}=\frac{2}{N_0}\int_0^{T_b}r(t)s(t)\,dt-\frac{1}{N_0}\int_0^{T_b}s^2(t)\,dt\tag{I.9}$$

  e la regola è $\lambda(r)\gtrless\ln\frac qp$ (I.10). Appunti: schema del demodulatore MAP (moltiplicatore per $s(t)$, integratore $\frac{2}{N_0}\int_0^{T_b}$, sottrazione di $E_s/N_0$, confronto con $\ln\frac qp$); il demodulatore MAP deve conoscere $\{s_i(t)\}$, $N_0$, $p$ e $q$.
- Con $p=q=1/2$ la regola diventa $\lambda(r)\gtrless0$ (I.11): non dipende dalla densità spettrale del rumore. È il criterio a **massima verosimiglianza** (ML). Appunti: si semplifica in $\int_0^{T_b}r(t)s(t)\,dt\gtrless E_s/2$, indipendente da $N_0$; usarlo con simboli non equiprobabili fa perdere l'ottimalità, ma non serve conoscere $N_0$, $p$, $q$.
- La statistica sufficiente si ottiene come uscita in $t=T_b$ di un filtro LTI con $h(t)=s(T_b-t)$:

$$r=\int_0^{T_b}r(t)\psi_1(t)\,dt=\frac{1}{\sqrt{E_s}}\int_0^{T_b}r(t)s(t)\,dt=\frac{1}{\sqrt{E_s}}\,r(t)\ast h(t)\Big|_{t=T_b}\tag{I.12}$$

  $h(t)$ è il **filtro adattato** a $s(t)$: campionato in $T_b$ estrae la statistica sufficiente.

### Modulazione M-aria

#### Dispense p. 5–6 e appunti — Generalizzazione · [[Detection.pdf#page=13|p. 13]], [[Detection.pdf#page=14|14]], [[Detection.pdf#page=6|p. 6]], [[Detection.pdf#page=7|7]]
- $M=2^h$ messaggi $m_k$, forme d'onda $s_k(t)$ su $[0,T]$, $T=hT_b$, probabilità $p_k$. Ipotesi $H_k=\{$trasmesso $m_k\}$. La base $\{\psi_i\}$ ha le prime $L\le M$ funzioni che sono una base dello spazio dei segnali, costruita con la procedura di **Gram-Schmidt** (appunti: $\psi_1=s_1/\lVert s_1\rVert$, poi si sottraggono le proiezioni sulle funzioni già trovate e si normalizza; fuori dallo spazio dei segnali restano solo componenti di rumore).

$$H_k:\ \mathbf r_N=\mathbf s^{(k)}_N+\mathbf n_N\tag{II.1}$$

$$r_i=\begin{cases}s^{(k)}_i+n_i&i=1,\dots,L\\ n_i&i=L+1,\dots,N\end{cases}\tag{II.2}$$

- Criterio MAP M-ario: si decide $H_k$ se $p_kf_{\mathbf r_N|H_k}=\max_ip_if_{\mathbf r_N|H_i}$ (II.3); per l'irrilevanza bastano $r_1,\dots,r_L$ (II.4), le **statistiche sufficienti**. Con $p_k=1/M$ si ha il criterio **ML** (II.5): minimizza $P(e)$ solo con ipotesi equiprobabili, ma è il più usato in pratica.
- Con l'ipotesi ausiliaria $H_0:\mathbf r_L=\mathbf n_L$ (II.6), ML equivale a massimizzare $\Lambda_k=f_{\mathbf r_L|H_k}/f_{\mathbf r_L|H_0}$ (II.7)–(II.8). Essendo $\mathbf r|H_k$ gaussiano con media $\mathbf s^{(k)}$, componenti indipendenti di varianza $N_0/2$:

$$\Lambda_k(\mathbf r)=\exp\Big\{\frac{2}{N_0}\mathbf r^T\mathbf s^{(k)}-\frac{1}{N_0}(\mathbf s^{(k)})^T\mathbf s^{(k)}\Big\}\tag{II.9}$$

#### Dispense p. 7 e appunti — Correlatore e filtro adattato · [[Detection.pdf#page=15|p. 15]], [[Detection.pdf#page=7|p. 7]], [[Detection.pdf#page=8|8]]
- Log-verosimiglianza (il fattore $2/N_0$ si toglie: è una costante comune):

$$\lambda_k(\mathbf r)=\mathbf r^T\mathbf s^{(k)}-\frac12(\mathbf s^{(k)})^T\mathbf s^{(k)}\tag{II.10}$$

$$\lambda_k(\mathbf r)=\int_0^Tr(t)s_k(t)\,dt-\frac12\int_0^Ts_k^2(t)\,dt=\langle r(t),s_k(t)\rangle-\frac12E_{s,k}\tag{II.11}$$

- Due implementazioni equivalenti del ricevitore ottimo in AWGN per modulazione senza memoria (Fig. 1–2): **banco di correlatori** ($r(t)$ moltiplicato per ogni $s_k(t)$, integrato su $[0,T]$, meno $\frac12E_{s,k}$, poi MAX) e **banco di filtri adattati** $s_k(T-t)$ campionati in $t=T$.

### Segnali passa-banda e interpretazione geometrica

#### Dispense p. 8 e appunti — Estensione ai segnali passa-banda · [[Detection.pdf#page=16|p. 16]], [[Detection.pdf#page=8|p. 8]]
- Segnali reali passa-banda $s_{p,k}(t)$, ricevuto $r_p(t)$, rumore $n_p(t)$ con PSD $N_0/2$. Dopo la downconversion, con inviluppi $\tilde s_k(t)$ e $\tilde r(t)$:

$$H_k:\ r_p(t)=s_{p,k}(t)+n_p(t)\quad\longrightarrow\quad H_k:\ \tilde r(t)=\tilde s_k(t)+\tilde n(t)$$

  con $\tilde n(t)$ gaussiano bianco di PSD $N_0$. Fig. 3: PSD di $n_p$ (due lobi $N_0/2$ attorno a $\pm f_c$), PSD di $\tilde n$ dopo la downconversion ($N_0$ in banda), e il modello semplificato piatto $N_0$ (appunti: si preferisce modellare il rumore complesso in banda base come bianco ideale, perché i limiti di banda complicherebbero gli integrali).
- Statistiche sufficienti:

$$\langle r_p(t),s_{p,k}(t)\rangle-\frac12E_{s,k}=\text{Re}(\langle\tilde r(t),\tilde s_k(t)\rangle)-\frac12E_{s,k}\tag{III.1}$$

  usando che l'energia dell'inviluppo è uguale a quella del segnale passa-banda (lezione su Rice).

#### Dispense p. 8–10 e appunti — Demodulatore a minima distanza e regioni di Voronoi · [[Detection.pdf#page=16|p. 16]]–[[Detection.pdf#page=18|18]], [[Detection.pdf#page=9|p. 9]]
- Le proiezioni $\mathbf r$, $\mathbf s^{(k)}$, $\mathbf n$ sulle $L$ funzioni di base sono punti di uno spazio euclideo $L$-dimensionale. Completando il quadrato:

$$\lambda_k(\mathbf r)=-\frac12\int_0^T[r(t)-s_k(t)]^2dt+\frac12\int_0^Tr^2(t)\,dt$$

  (le dispense, eq. (IV.2), omettono il fattore $\frac12$ davanti al primo integrale; gli appunti lo riportano). Il secondo termine non dipende da $k$ ed è irrilevante: massimizzare $\lambda_k$ equivale a minimizzare $\lVert\mathbf r-\mathbf s^{(k)}\rVert^2$.
- Il demodulatore ML decide per il segnale **più vicino** al ricevuto: è un **ricevitore a minima distanza**, che «si fida del canale».
- Regioni di decisione ML o **regioni di Voronoi**: $Z_k\triangleq\{\mathbf r\in\mathbb R^L:\lVert\mathbf r-\mathbf s^{(k)}\rVert^2=\min_\ell\lVert\mathbf r-\mathbf s^{(\ell)}\rVert^2\}$. Fig. 4: esempio di regioni di Voronoi. I confini sono iperpiani, luoghi dei punti equidistanti da due segnali vicini.

---

*Approfondimenti nel wiki: [[rivelazione-map-ml]], [[ricevitore-ottimo-awgn]], [[spazio-dei-segnali]].*

## Lezione 10 — Prestazioni delle modulazioni binarie e della QPSK

*Fonte: Lezione 10-28.pdf (appunti a lezione del 28/10, 4 pagine, in `raw/goodnotes/`).*

### Segnalazione on-off · [[Lezione 10-28.pdf#page=1|p. 1]]
- Con la base $\psi(t)=s(t)/\sqrt{E_s}$, $E_s=\int_0^Ts^2(t)\,dt$ (energia della forma d'onda), $s(t)=\sqrt{E_s}\,\psi(t)$ e $\lambda(r)=\frac{2\sqrt{E_s}}{N_0}r-\frac{E_s}{N_0}$, con $r=\langle r(t),\psi(t)\rangle$.
- Ipotesi equiprobabili ($p=q=\frac12$), demodulatore ML: $\lambda(r)\gtrless0\iff r\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \frac{\sqrt{E_s}}{2}$, una soglia puramente geometrica che non richiede $N_0$. Schema: correlatore con $\psi(t)$ (o filtro adattato $h(t)=\psi(T_b-t)$ campionato in $T_b$) e comparatore a soglia $\sqrt{E_s}/2$.
- Lo spazio dei segnali coincide con quello degli osservabili (una dimensione): $Z_0$ a sinistra della soglia, $Z_1$ a destra; la partizione minimizza $P(e)$ e il demodulatore decide a minima distanza.
- Probabilità d'errore, con $n=\langle n(t),\psi(t)\rangle\sim\mathcal N(0,N_0/2)$:

$$P(e)=\tfrac12\big[P(e|H_0)+P(e|H_1)\big],\qquad P(e|H_0)=P\Big(n>\frac{\sqrt{E_s}}{2}\Big)=\frac12\,\text{erfc}\Big(\frac12\sqrt{\frac{E_s}{N_0}}\Big)$$

  e $P(e|H_1)=P(\sqrt{E_s}+n<\sqrt{E_s}/2)$ dà lo stesso valore (usando $\text{erfc}(-x)=2-\text{erfc}(x)$). È così perché le regioni di decisione sono **congruenti** (stessa forma, estensione e dimensione geometrica): con regioni congruenti basta calcolare la probabilità d'errore per una sola regione. Quindi $P(e)=\frac12\text{erfc}\big(\frac12\sqrt{E_s/N_0}\big)$, dove $\sqrt{E_s/N_0}$ è il **contrasto di energia**.
- Schizzo: $P(e)$ in scala logaritmica decresce con $E_s/N_0$ in dB. In questo caso la BER (bit error rate) coincide con $P(e)$; la BER è un rate «raw» perché conta tutti i bit, non solo quelli d'informazione.
- Per stimare una probabilità con il metodo Monte Carlo servono circa $n=100/p$ prove: per $p\approx10^{-4}$, $10^6$ prove.

### Segnalazione antipodale e ortogonale · [[Lezione 10-28.pdf#page=2|p. 2]]
- **Antipodale** (due punti agli estremi opposti di un diametro): $s_1(t)=A\,\text{rect}\big(\frac{t-T_b/2}{T_b}\big)$, $s_2(t)=-s_1(t)$, simboli equiprobabili; segnali equienergetici, $E_s=A^2T_b$; base $\psi=s_1/\sqrt{E_s}$.
- Per segnali equienergetici si toglie $\frac12E_s$ dalla log-verosimiglianza: $\lambda_k=\int_0^Tr(t)s_k(t)\,dt$. Con $s^{(1)}=\sqrt{E_s}$, $s^{(2)}=-\sqrt{E_s}$: $\lambda_1\gtrless\lambda_2\iff r\gtrless0$ (comparatore a soglia 0).
- $P(e)=P(e|H_2)=P(-\sqrt{E_s}+n>0)=P(n>\sqrt{E_s})=\frac12\text{erfc}\big(\sqrt{E_s/N_0}\big)$.
- Confronto: antipodale $\frac12\text{erfc}\sqrt{E_s/N_0}$ («sfrutta meglio i gradi di libertà a disposizione»), on-off $\frac12\text{erfc}\big(\frac12\sqrt{E_s/N_0}\big)$: a parità di $E_s/N_0$ l'antipodale ha $P(e)$ minore, perché l'erfc decresce rapidamente. Distanze: $d=2\sqrt{E_s}$ (antipodale) e $d=\sqrt{E_s}$ (on-off).
- In generale per una modulazione binaria $P(e)=\frac12\text{erfc}\big(\frac{d}{2\sqrt{N_0}}\big)$, con $d=\lVert s_1(t)-s_2(t)\rVert=\lVert\mathbf s_1-\mathbf s_2\rVert$.
- **Ortogonale binaria**: $\mathbf s_1=(\sqrt{E_s},0)$, $\mathbf s_2=(0,\sqrt{E_s})$, $d=\sqrt{2E_s}$, regioni congruenti separate dalla bisettrice: $P(e)=\frac12\text{erfc}\big(\sqrt{E_s/(2N_0)}\big)$.
- **Invarianza**: $P(e)$ non cambia per traslazioni e rotazioni della costellazione (stessa $d$). Cambia invece l'energia media $E_s=\sum_ip_i\lVert\mathbf s_i\rVert^2$ (con simboli equiprobabili $\frac1M\sum_i\lVert\mathbf s_i\rVert^2$), minima quando $\sum_i\mathbf s_i=0$ (baricentro nell'origine): una costellazione spostata non si sceglierebbe mai, perché richiede più energia. Vale anche per la FSK: due costellazioni con la stessa forma hanno la stessa $P(e)$ ma medie diverse.

### Modulazione binaria generica · [[Lezione 10-28.pdf#page=3|p. 3]]
- Distanza tra due segnali e **coefficiente di correlazione**:

$$d^2=E_{s_1}+E_{s_2}-2\int_0^{T_b}s_1(t)s_2(t)\,dt,\qquad\rho\triangleq\frac{\langle s_1,s_2\rangle}{\lVert s_1\rVert\lVert s_2\rVert}\ \Rightarrow\ d^2=E_{s_1}+E_{s_2}-2\rho\sqrt{E_{s_1}E_{s_2}}$$

$$P(e)=\frac12\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)=\frac12\text{erfc}\Big(\sqrt{\frac{E_{s_1}+E_{s_2}-2\rho\sqrt{E_{s_1}E_{s_2}}}{4N_0}}\Big)$$

- Segnali equienergetici: $P(e)=\frac12\text{erfc}\big(\sqrt{E_s(1-\rho)/(2N_0)}\big)$. Antipodale $\rho=-1$: $\frac12\text{erfc}\sqrt{E_s/N_0}$ (sfrutta meglio l'energia: la $P(e)$ scende più rapidamente all'aumentare di $E_s$); ortogonale $\rho=0$: $\frac12\text{erfc}\sqrt{E_s/(2N_0)}$; on-off (non equienergetica, $E_{s_1}=0$, $E_{s_2}=E_s$): $\frac12\text{erfc}\big(\frac12\sqrt{E_s/N_0}\big)$.

### QPSK · [[Lezione 10-28.pdf#page=3|p. 3]], [[Lezione 10-28.pdf#page=4|4]]
- M-PSK: $\xi=e^{j\phi}$, $\phi\in\{\frac{2\pi}{M}(i-1)+\phi_0\}$. QPSK, $M=4$: $\phi\in\{\frac\pi4,\frac34\pi,\frac54\pi,\frac74\pi\}$. La probabilità d'errore $P(e)$ è sul **simbolo**, non sul bit (come nella modulazione binaria). La $P(e)$ è **invariante per rotazioni della costellazione** (figura degli appunti: la stessa costellazione con i punti sugli assi e ruotata con i punti sulle diagonali): la fase $\phi_0$ si sceglie liberamente e si prende $\phi_0=\frac\pi4$.

> 🧩 Perché la $P(e)$ non cambia: in AWGN dipende solo dalle distanze tra i punti, e una rotazione le lascia uguali, come le regioni di decisione; il rumore gaussiano bianco ha la stessa varianza $N_0/2$ in ogni direzione, quindi ruotato resta uguale. Anche l'energia media $E_s$ non cambia, perché i punti restano alla stessa distanza dall'origine. Con $\phi_0=\frac\pi4$ c'è un punto per quadrante e la decisione si fa sui soli segni di $z_1$ e $z_2$ (vedi sotto).

- Segnale passa-banda (modulazione a modulo costante): $s_{p,i}(t)=A\cos(2\pi f_0t+\phi_i)=A\cos\phi_i\cos(2\pi f_0t)-A\sin\phi_i\sin(2\pi f_0t)$, $t\in[0,T]$, $T=2T_b$, quindi $R_s=\frac{1}{2T_b}=\frac{R_b}{2}$: combinazione lineare di due funzioni ortogonali, spazio dei segnali di dimensione 2.
- Base: $\lVert\cos(2\pi f_0t)\rVert^2=\int_0^T\frac{1+\cos(4\pi f_0t)}{2}dt\approx\frac T2$ (per $f_0T\gg1$ le aree positive e negative del coseno a $2f_0$ si bilanciano), quindi $\psi_1=\sqrt{\frac2T}\cos(2\pi f_0t)$, $\psi_2=-\sqrt{\frac2T}\sin(2\pi f_0t)$.
- **Inviluppo complesso del segnale.** Si pone $\tilde A=A/\sqrt2$, così $s_{p,i}(t)=\sqrt2\,\text{Re}\{\tilde s_i(t)\,e^{j2\pi f_0t}\}$ con

$$\tilde s_i(t)=\tilde Ae^{j\phi_i}\,\text{rect}\Big(\frac{t-T/2}{T}\Big)=\underbrace{\tilde A\cos\phi_i\,\text{rect}\Big(\frac{t-T/2}{T}\Big)}_{s_{ic}(t)}+j\,\underbrace{\tilde A\sin\phi_i\,\text{rect}\Big(\frac{t-T/2}{T}\Big)}_{s_{is}(t)},\qquad i=1,2,3,4$$

  Le componenti in fase $s_{ic}$ e in quadratura $s_{is}$ sono due rettangoli su $[0,T]$, di altezza costante $\tilde A\cos\phi_i$ e $\tilde A\sin\phi_i$ (negli appunti l'ampiezza è scritta $A$: un fattore positivo comune a tutti i simboli non cambia la decisione).
- **Perché l'inviluppo complesso.** Si vuole lavorare **a valle del down converter**, che dal segnale ricevuto $r_p(t)$ restituisce l'inviluppo complesso $\tilde r(t)=r_c(t)+j\,r_s(t)$: $r_c$ è la componente in fase, $r_s$ quella in quadratura.
- **Statistica di decisione.** Demodulazione ML con simboli equiprobabili, scritta con gli inviluppi complessi: $\lambda_k(\tilde r)=\text{Re}\langle\tilde r,\tilde s_k\rangle-\frac12E_{s_k}$, e si sceglie il $k$ che la rende massima. I segnali sono equienergetici ($E_{s_k}=E_s$ per ogni $k$), quindi $\frac12E_{s_k}$ è lo stesso per tutti i candidati e si toglie: $\lambda_k(\tilde r)=\text{Re}\langle\tilde r,\tilde s_k\rangle$.
- **Da $\lambda_k$ a $z_1$ e $z_2$.** Si scrive il prodotto scalare e si separano parte reale e immaginaria:

$$
\begin{aligned}
\lambda_k&=\text{Re}\Big\{\int_0^T\tilde r(t)\,\tilde s_k^{\ast}(t)\,dt\Big\} && \text{prodotto scalare tra segnali complessi}\\
&=\text{Re}\Big\{\int_0^T\big(r_c+j\,r_s\big)\big(s_{kc}-j\,s_{ks}\big)\,dt\Big\} && \text{il coniugato cambia segno alla parte immaginaria}\\
&=\text{Re}\Big\{\int_0^T\big[r_cs_{kc}+r_ss_{ks}+j\,(r_ss_{kc}-r_cs_{ks})\big]\,dt\Big\} && \text{svolgo il prodotto: } j\cdot(-j)=+1\\
&=\int_0^Tr_c(t)\,s_{kc}(t)\,dt+\int_0^Tr_s(t)\,s_{ks}(t)\,dt && \text{la parte reale elimina il termine con } j\\
&=\tilde A\cos\phi_k\int_0^Tr_c(t)\,dt+\tilde A\sin\phi_k\int_0^Tr_s(t)\,dt && s_{kc},\,s_{ks}\text{ costanti su }[0,T]\text{: escono dall'integrale}\\
&=\tilde A\cos\phi_k\,z_1+\tilde A\sin\phi_k\,z_2 && z_1=\int_0^Tr_c(t)\,dt,\ z_2=\int_0^Tr_s(t)\,dt
\end{aligned}
$$

  $z_1$ e $z_2$ nascono quindi dal fatto che l'impulso è un **rettangolo**: correlare con un rettangolo vuol dire solo integrare il ricevuto su $[0,T]$. Gli appunti annotano che $(z_1,z_2)$ «dovrebbe combaciare con un punto della costellazione»: senza rumore è proprio il punto trasmesso.

> 🧩 Due osservazioni per seguire il passaggio successivo. (1) $z_1$ e $z_2$ **non dipendono da $k$**: sono gli stessi due numeri per tutti e 4 i candidati, che cambiano solo i pesi $\cos\phi_k$, $\sin\phi_k$. Il ricevitore calcola solo $z_1$ e $z_2$, con due integratori. (2) Con $\phi_k\in\{\frac\pi4,\frac34\pi,\frac54\pi,\frac74\pi\}$ si ha $\cos\phi_k=\pm\frac1{\sqrt2}$ e $\sin\phi_k=\pm\frac1{\sqrt2}$, quindi $\lambda_k=\frac{\tilde A}{\sqrt2}(\pm z_1\pm z_2)$. Il massimo si ottiene scegliendo il segno di $\cos\phi_k$ uguale a quello di $z_1$ e il segno di $\sin\phi_k$ uguale a quello di $z_2$: si decide per il simbolo nel **quadrante** in cui cade $(z_1,z_2)$. Per esempio $z_1>0$, $z_2<0$ dà $\phi=\frac74\pi$.

- **Decisione.** Il criterio di decisione ottimo si riduce a valutare i **segni** di $z_1$ e $z_2$. Schema: canale → $r_p(t)$ → down conversion → $r_c(t)$, $r_s(t)$ → due integratori $\int_0^T dt$ → $z_1$, $z_2$ → decisore sul segno.
- Probabilità d'errore sul simbolo (SER), conviene passare per la **corretta decisione**: $P(e)=1-P(c)$, $P(c)=\frac1M\sum_kP(c|H_k)=P(c|H_1)$ (regioni congruenti). Con $\mathbf s_1=\big(\frac{A\sqrt T}{2},\frac{A\sqrt T}{2}\big)$ e $n_1,n_2$ gaussiane indipendenti $\mathcal N(0,N_0/2)$:

$$P(c|H_1)=P\Big(n_1>-\frac{A\sqrt T}{2}\Big)^2=(1-p)^2,\qquad p=\frac12\text{erfc}\Big(\frac A2\sqrt{\frac{T}{N_0}}\Big)$$

- $P(e)=1-(1-p)^2=2p-p^2$. Con $E_s=\lVert\mathbf s_i\rVert^2=\frac{A^2T}{2}$: $p=\frac12\text{erfc}\sqrt{E_s/(2N_0)}$ e

$$P(e)=\text{erfc}\Big(\sqrt{\frac{E_s}{2N_0}}\Big)-\frac14\text{erfc}^2\Big(\sqrt{\frac{E_s}{2N_0}}\Big)\simeq\text{erfc}\Big(\sqrt{\frac{E_s}{2N_0}}\Big)$$

  trascurando il quadrato ad alto SNR. Con $E_s=E_b\log_2M=2E_b$: $P(e)\simeq\text{erfc}\sqrt{E_b/N_0}$, il **doppio** della $P(e)$ dell'antipodale.
- Con il mapping di Gray (ottima approssimazione ad alto SNR) $\text{BER}=\frac{\text{SER}}{\log_2M}=\frac12\text{erfc}\sqrt{E_b/N_0}$: la BER della QPSK è la stessa dell'antipodale.

---

*Approfondimenti nel wiki: [[probabilita-errore-binaria]], [[probabilita-errore-m-aria]], [[ricevitore-ottimo-awgn]].*

## Lezione 11 — Union bound e approssimazione dei primi vicini

*Fonte: Lezione 11-2.pdf (appunti a lezione del 2/11, 3 pagine in `raw/goodnotes/`; p. 1 è la copertina del quaderno).*

### Union bound · [[Lezione 11-2.pdf#page=2|p. 2]]
- Per schemi più complessi la $P(e)$ esatta è difficile: si ricorre ad approssimazioni e allo **union bound**.
- Regola ML: si decide $H_k$ se $\lambda_k(\mathbf r)=\int_0^Tr(t)s_k(t)\,dt-\frac12E_{s,k}$ è massima (caso non equienergetico); in termini geometrici $\lambda_k=\mathbf r^T\mathbf s^{(k)}-\frac12E_k$ e si decide $H_k$ se $\mathbf r\in Z_k=\{\mathbf r:\lambda_k(\mathbf r)>\lambda_i(\mathbf r),\ \forall i\neq k\}$.
- Probabilità d'errore sotto $H_k$, con eventi non mutuamente esclusivi e $P(A\cup B)\le P(A)+P(B)$:

$$P(e|H_k)=P\Big(\bigcup_{i\neq k}\{\lambda_i(\mathbf r)>\lambda_k(\mathbf r)\}\,\Big|\,H_k\Big)\le\sum_{i\neq k}P\big(\lambda_i>\lambda_k\,|\,H_k\big)=\frac12\sum_{i\neq k}\text{erfc}\Big(\frac{d_{ik}}{2\sqrt{N_0}}\Big)$$

  Ogni termine è la **pairwise error probability** (PEP), la probabilità di confondere $s_k$ con $s_i$: ci si riconduce a un problema binario. Si ottiene un maggiorante:

$$P(e)=\frac1M\sum_{k=1}^MP(e|H_k)\le\frac{1}{2M}\sum_{k=1}^M\sum_{i\neq k}\text{erfc}\Big(\frac{d_{ik}}{2\sqrt{N_0}}\Big)$$

### Approssimazione dei primi vicini · [[Lezione 11-2.pdf#page=2|p. 2]]
- **Nearest neighbors approximation**: $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\big(\frac{d_{min}}{2\sqrt{N_0}}\big)$, con $d_{min}$ distanza minima della costellazione e $\bar N_{d_{min}}=\frac1M\sum_iN_{d_{min}}(i)$ numero medio di vicini a distanza minima.

### Esempio: 16-QAM · [[Lezione 11-2.pdf#page=2|p. 2]]
- Per il calcolo esatto: $P(e)=1-\frac1M\sum_kP(c|H_k)$, con tre tipi di regioni congruenti (interne, di bordo, d'angolo); per un punto interno $P(c|H_k)=\big[P(-\frac d2<n<\frac d2)\big]^2$. Si dovrebbe calcolare per i tre tipi e poi mediare.
- Con i primi vicini: $d_{min}=d$, $\bar N_{d_{min}}=\frac{1}{16}(4\cdot4+8\cdot3+4\cdot2)=3$, quindi $P(e)\approx\frac32\text{erfc}\big(\frac{d}{2\sqrt{N_0}}\big)$.
- In termini di energia per bit: $E_s=\frac{1}{16}\big(4\cdot\frac{d^2}{2}+8\cdot\frac{5d^2}{2}+4\cdot\frac{9d^2}{2}\big)=\frac52d^2=E_b\log_2M=4E_b$, quindi $d^2=\frac85E_b$ e

$$P(e)\approx\frac32\,\text{erfc}\Big(\sqrt{\frac25\frac{E_b}{N_0}}\Big)$$

### Esempio: modulazione ortogonale · [[Lezione 11-2.pdf#page=2|p. 2]]
- Con $M=3$ segnali $\mathbf s_1=(\frac{d}{\sqrt2},0,0)$, $\mathbf s_2=(0,\frac{d}{\sqrt2},0)$, $\mathbf s_3=(0,0,\frac{d}{\sqrt2})$ tutte le distanze valgono $d$; lo union bound dà

$$P(e)\le\frac{1}{2M}\sum_k\sum_{i\neq k}\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)=\frac{M-1}{2}\text{erfc}\Big(\frac{d}{2\sqrt{N_0}}\Big)$$

- Con $E_s=\frac1M\sum\lVert\mathbf s_i\rVert^2=\frac{d^2}{2}$, $d=\sqrt{2E_s}=\sqrt{2E_b\log_2M}$:

$$P(e)\le\frac{M-1}{2}\text{erfc}\Big(\sqrt{\frac{E_b\log_2M}{2N_0}}\Big)$$

  Se $M$ aumenta con $E_b$ fisso, $P(e)$ diminuisce; se invece è fisso $E_s$, $P(e)$ aumenta con $M$.

### Note finali · [[Lezione 11-2.pdf#page=3|p. 3]]
- Rimandi a figure da vedere: la $P(e)$ in funzione del contrasto di energia, e perché a basso SNR i vicini più lontani diventano rilevanti (a basso SNR l'approssimazione dei primi vicini è poco affidabile; ad alto SNR contano solo i punti a distanza minima).

---

*Approfondimenti nel wiki: [[probabilita-errore-m-aria]], [[probabilita-errore-binaria]], [[parametri-globali-modulazioni]].*

## Lezione 12 — Parametri globali delle modulazioni e capacità di canale

*Fonte: Confronto_new.pdf («Global parameters for memoryless modulation and channel capacity», a.a. 2026-27), 33 slide, slide N = p. N, con note a mano della docente a p. 8, 19, 21, 23, 25, 30. Appunti presi a lezione nella copia annotata Confronto new.pdf (35 pagine: slide 1–4 = p. 1–4, pagina di appunti p. 5, slide 5–13 = p. 6–14, pagina di appunti p. 15, slide 14–33 = p. 16–35). Le equazioni (1)–(6) sono quelle delle slide di questa lezione.*

### Obiettivi e introduzione · slide [[Confronto_new.pdf#page=2|p. 2]], [[Confronto_new.pdf#page=3|3]] · appunti [[Confronto new.pdf#page=3|p. 3]]
- Obiettivi: introdurre **informazione mutua** e **capacità di canale** come limiti teorici fondamentali; definire i **parametri globali** con cui si confrontano gli schemi di modulazione (efficienza spettrale, efficienza in potenza, rapporto $E_b/N_0$); confrontare le modulazioni reali con il **limite di Shannon**; mostrare come questi concetti entrano nel **link budget** di un collegamento reale.
- La domanda di velocità sempre maggiori rende importante sapere qual è la **massima velocità di trasmissione** ottenibile su un canale.
- La **capacità di canale** (Shannon) è la massima velocità per cui si può ottenere una probabilità d'errore piccola a piacere. È definita **senza vincoli** di complessità o di ritardo. Per il canale AWGN ha un'espressione in forma chiusa particolarmente semplice.
- Appunti a lezione: superare la capacità significa non poter avere una $P(e)$ arbitrariamente piccola, qualunque sia lo schema di modulazione.

### Informazione mutua e capacità

#### Slide 4 — Informazione mutua · slide [[Confronto_new.pdf#page=4|p. 4]] · appunti [[Confronto new.pdf#page=4|p. 4]]
- Per un canale **senza memoria** con ingresso aleatorio $X$ e uscita $Y$:

$$I(X;Y)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)\,p(y)}$$

- Misura quanta informazione l'osservazione di $Y$ fornisce su $X$. È **simmetrica**, $I(X;Y)=I(Y;X)$; se $X$ e $Y$ sono indipendenti, $I(X;Y)=0$. Si misura in **bit**.
- Appunti a lezione: il canale è il **meccanismo che associa aleatoriamente $X$ a $Y$** (effetto del canale): è un modello di canale discreto senza memoria e $p(x,y)$ è la DF congiunta. Il logaritmo in base 2 fa misurare l'informazione mutua in **bit**; con il logaritmo naturale si misura in **nat**. La domanda guida: «osservando $Y$, quanta informazione ho su cosa ho trasmesso ($X$)?»; la risposta è l'informazione mutua. Con $X$ e $Y$ indipendenti, osservare l'uscita non dà alcuna informazione su cosa è stato trasmesso.

#### Appunti — Dimostrazione di $I=H(Y)-H(Y\mid X)$ · appunti [[Confronto new.pdf#page=5|p. 5]]
- Pagina di appunti a lezione tra le slide 4 e 5: da $p(y\mid x)=\frac{p(x,y)}{p(x)}$ si ha $\frac{p(x,y)}{p(x)p(y)}=\frac{p(y\mid x)}{p(y)}$, quindi
$$I(X;Y)=\sum_x\sum_y p(x,y)\log_2p(y\mid x)-\sum_x\sum_y p(x,y)\log_2p(y)$$
  Il primo termine è $-H(Y\mid X)$ (entropia condizionale); nel secondo $\sum_xp(x,y)=p(y)$ e resta $-\sum_yp(y)\log_2p(y)=H(Y)$, l'entropia di $Y$.
- **Entropia**: $H(Y)=\sum_yp(y)\log_2\frac{1}{p(y)}$, media dell'**autoinformazione** $\log_2\frac{1}{p(y)}$, che cresce al diminuire della probabilità; è la misura dell'informazione associata alla variabile aleatoria (Shannon).

#### Slide 5 — Informazione mutua ed entropia · slide [[Confronto_new.pdf#page=5|p. 5]] · appunti [[Confronto new.pdf#page=6|p. 6]]
- Usando $p(x,y)=p(y\mid x)\,p(x)$:

$$I(X;Y)=H(Y)-H(Y\mid X)=H(X)-H(X\mid Y)$$

- $H(Y)$ è l'**entropia** di $Y$, l'incertezza media su $Y$; $H(Y\mid X)$ è l'incertezza residua su $Y$ quando $X$ è noto. Analogamente $H(X)$ e $H(X\mid Y)$, incertezza residua su $X$ dopo aver osservato $Y$.
- **Interpretazione:** l'informazione mutua è la riduzione media di incertezza ottenuta osservando l'uscita del canale.
- Appunti a lezione: l'entropia è una misura dell'**incertezza media**; se $X$ e $Y$ sono statisticamente indipendenti, osservare l'uscita del canale è inutile.

#### Slide 6 — Capacità di canale · slide [[Confronto_new.pdf#page=6|p. 6]] · appunti [[Confronto new.pdf#page=7|p. 7]]

$$C=\max_{p(x)}I(X;Y)$$

- Il massimo è preso rispetto alla **distribuzione dell'ingresso**. Nel caso discreto la capacità si misura in **bit/uso del canale**; per canali a tempo continuo in **bit/s**.
- **Interpretazione operativa:** la capacità è la massima velocità teoricamente ottenibile con probabilità d'errore piccola a piacere.
- Appunti a lezione: la capacità è il massimo rate che il canale può sostenere con $P(e)$ arbitrariamente piccola; a seconda dello schema di modulazione e dell'energia a disposizione si sceglie il rate di trasmissione, agendo sul compromesso con l'energia.

#### Slide 7 — Secondo teorema di Shannon · slide [[Confronto_new.pdf#page=7|p. 7]] · appunti [[Confronto new.pdf#page=8|p. 8]]
- Sia $R_b$ il bit rate all'ingresso del canale.
  - Se $R_b<C$, **esistono** tecniche di trasmissione che rendono la probabilità d'errore piccola a piacere.
  - Se $R_b>C$, **non** è possibile ottenere una probabilità d'errore piccola a piacere.
- La capacità è un limite teorico: non descrive uno schema di modulazione specifico, ma le migliori prestazioni possibili.
- Appunti a lezione: il teorema non dice quale schema usare: **non è costruttivo**.

### Capacità del canale AWGN

#### Slide 8 — Capacità del canale AWGN · slide [[Confronto_new.pdf#page=8|p. 8]] · appunti [[Confronto new.pdf#page=9|p. 9]]
- Canale AWGN: $y[i]=x[i]+n[i]$, con $n[i]$ processo gaussiano bianco. Con banda disponibile $W$, potenza media trasmessa $P$ e densità spettrale di rumore $N_0$, il rapporto segnale-rumore è

$$\gamma=\frac{P}{N_0W}$$

  e la capacità è

$$C=W\log_2(1+\gamma)\qquad[\text{bit/s}]$$

- Nota a mano (in rosso): **«questo risultato non va dimostrato»**.
- Appunti a lezione: «abbiamo fatto la demodulazione, manca la decisione»: $y[i]$ è l'uscita del demodulatore nell'$i$-esimo intervallo di tempo ($i\in\mathbb Z$) e $n[i]$ è il rumore AWGN.

#### Slide 9 — Interpretazione della capacità AWGN · slide [[Confronto_new.pdf#page=9|p. 9]] · appunti [[Confronto new.pdf#page=10|p. 10]]
- La capacità cresce **linearmente** con la banda $W$ e **logaritmicamente** con l'SNR $\gamma$.
- Capacità per unità di banda: $\dfrac CW=\log_2(1+\gamma)$ [bit/s/Hz].
- Per aumenti significativi di capacità è spesso più efficace aumentare la banda che aumentare soltanto la potenza.
- Appunti a lezione: per aumentare $C$ conviene aumentare $W$, che è la risorsa preziosa. Shannon mostra che per ottenere una $P(e)$ arbitrariamente piccola si può **abbassare il rate** fino a $R<C$, invece di aumentare la potenza del segnale.

### Banda dei segnali digitali

#### Slide 10 — Banda dei segnali digitali · slide [[Confronto_new.pdf#page=10|p. 10]] · appunti [[Confronto new.pdf#page=11|p. 11]]
- Ogni schema di modulazione usa le risorse disponibili (**potenza, banda, complessità**) per ottenere una probabilità d'errore prefissata.
- Con spettro a supporto finito la banda sarebbe la larghezza del supporto; ma per modulazioni con forme d'onda di **durata finita** la PSD si estende da $-\infty$ a $+\infty$.
- Esistono varie definizioni di banda (es. *null-to-null*, banda che contiene una frazione prefissata della potenza). Poiché il confronto prescinde dai segnali effettivi e guarda alle caratteristiche **geometriche delle costellazioni**, conviene una definizione «astratta» di banda.
- Appunti a lezione: tra le risorse c'è la complessità computazionale; il problema non è tanto l'elaborazione in sé quanto il **ritardo** dovuto a tutti i dati da elaborare.

#### Slide 11 — Banda di Shannon · slide [[Confronto_new.pdf#page=11|p. 11]] · appunti [[Confronto new.pdf#page=12|p. 12]]
- La dimensionalità di un insieme di segnali di durata $T$ e banda monolatera $W$ è $N=2WT$ (prodotto tempo-banda). Si definisce la **banda di Shannon**

$$W=\frac{N}{2T}$$

  in Hz o, più propriamente, in **dimensioni al secondo**.
- Esempio: un segnale M-PSK ha 2 dimensioni, quindi $W=1/T$.
- In generale la banda del segnale è $\alpha/T$, con $\alpha$ che dipende dalla definizione di banda e dal tipo di segnale: la durata di un segnale è inversamente proporzionale alla sua occupazione di banda (teoria di Fourier).
- Appunti a lezione: $N$ è la dimensionalità del formato di modulazione, cioè della costellazione (approccio geometrico); $N/T$ è il numero di dimensioni trasmesse nell'unità di tempo.

### Potenza, energia per bit ed efficienze

#### Slide 12 — Potenza media ed energia per bit · slide [[Confronto_new.pdf#page=12|p. 12]] · appunti [[Confronto new.pdf#page=13|p. 13]]
- Potenza media spesa dal modulatore:

$$P=\frac ET\tag{1}$$

  con $E$ energia media dei segnali del modulatore e $T=\log_2M\cdot T_b$ periodo di simbolo ($M$ cardinalità della costellazione, $T_b$ periodo di bit).
- Ogni simbolo porta $\log_2M$ bit, quindi l'energia media spesa per trasmettere un bit è

$$E_b=\frac{E}{\log_2M}\tag{2}$$

- Sostituendo (2) in (1):

$$P=\frac{E_b\log_2M}{T}=E_b\,R_b\tag{3}$$

  con $R_b$ bit rate.
- Appunti a lezione: $E$ è l'energia media della costellazione, $E_b$ l'energia media per bit.

#### Slide 13–14 — SNR ed efficienza spettrale · slide [[Confronto_new.pdf#page=13|p. 13]], [[Confronto_new.pdf#page=14|14]] · appunti [[Confronto new.pdf#page=14|p. 14]], [[Confronto new.pdf#page=16|16]]
- L'SNR è il rapporto tra potenza media del segnale e potenza media del rumore:

$$\text{SNR}\triangleq\frac{P}{N_0W}=\frac{E_b}{N_0}\,\frac{R_b}{W}$$

  con $W$ banda monolatera del filtro di ricezione, che limita la potenza di rumore lasciando il segnale indistorto.
- $\eta_B\triangleq R_b/W$ è l'**efficienza spettrale** (o in banda), in bit/s/Hz: quanti bit al secondo si trasmettono in una banda $W$. L'SNR complessivo dipende dalla qualità energetica del collegamento, $E_b/N_0$, e da quanto efficientemente si usa la banda, $\eta_B$.
- Con la banda di Shannon:

$$\eta_B=\frac{2\log_2M}{N}$$

  L'efficienza spettrale cresce con $M$; a parità di $M$, cresce al diminuire della dimensionalità necessaria a rappresentare i segnali.
- Esempio: $R_b=9.6$ kbit/s e $W=4.8$ kHz danno $\eta_B=2$ bit/s/Hz.
- Appunti a lezione: nell'SNR, $E_b/N_0$ è il contributo dell'**energia** e $R_b/W$ quello dell'**efficienza spettrale** (o in banda).

#### Appunti — Rumore in banda e rumore bianco · appunti [[Confronto new.pdf#page=15|p. 15]]
- Pagina di appunti a lezione dopo la slide 13: la PSD del rumore $S_n(f)$ disegnata come due rettangoli di altezza $N_0/2$ attorno a $\pm f_c$ (rumore in banda), e il rumore bianco con PSD piatta $N_0/2$ su tutte le frequenze, «utilizzato per facilitarci nei calcoli», che ha funzione di autocorrelazione impulsiva.
- Domanda annotata: è il canale che fa da filtro, oppure bisogna aggiungerne uno al ricevitore? (La slide 13 risponde: $W$ è la banda del **filtro di ricezione**, che limita il rumore lasciando indistorto il segnale.)

#### Slide 15–16 — Efficienza in potenza · slide [[Confronto_new.pdf#page=15|p. 15]], [[Confronto_new.pdf#page=16|16]] · appunti [[Confronto new.pdf#page=18|p. 18]]

$$\eta_P\triangleq\frac{d_{min}^2}{4E_b}\tag{4}$$

- $d_{min}$ è la distanza minima tra i segnali. $\eta_P$ misura quanto efficientemente l'energia disponibile viene usata per **separare geometricamente** i punti della costellazione.
- Esempi:
  - **OOK**: $s_0=0$, $s_1=A$; $d_{min}=A$, $E=E_b=\frac12(s_0^2+s_1^2)=\frac{A^2}{2}\Rightarrow\eta_P=\frac12$.
  - **Antipodale**: $s_1=-A$, $s_2=A$; $d_{min}=2A$, $E=E_b=A^2\Rightarrow\eta_P=1$.
  - **Ortogonale binaria**: $\mathbf s_1=(A,0)$, $\mathbf s_2=(0,A)$; $d_{min}=\sqrt2A$, $E=E_b=A^2\Rightarrow\eta_P=\frac12$.
- Appunti a lezione: l'antipodale **utilizza meglio l'energia a disposizione**.

#### Slide 17 — Probabilità d'errore e ruolo di $\eta_P$ · slide [[Confronto_new.pdf#page=17|p. 17]] · appunti [[Confronto new.pdf#page=19|p. 19]]
- Per SNR moderatamente grandi la probabilità d'errore di simbolo è approssimata da (vedi dispense)

$$P(e)\approx\frac{\bar N_{d_{min}}}{2}\,\text{erfc}\Big(\frac{d_{min}}{2\sqrt{N_0}}\Big)\tag{5}$$

  con $\bar N_{d_{min}}$ numero medio di vicini a distanza minima (*nearest neighbors approximation*). Sostituendo (4):

$$P(e)\approx\frac{\bar N_{d_{min}}}{2}\,\text{erfc}\Big(\sqrt{\eta_P\frac{E_b}{N_0}}\Big)\tag{6}$$

- A SNR moderatamente grande il termine dominante è l'argomento della erfc: per questo $\eta_P$ permette un confronto rapido tra modulazioni.
- Appunti a lezione: la (5) vale in regime di alto SNR; nell'argomento della erfc compare $\eta_P$, l'efficienza in potenza.

### Confronto tra modulazioni

#### Slide 18 — Parametri globali · [[Confronto_new.pdf#page=18|p. 18]]
- Una modulazione si valuta in termini di probabilità d'errore $P(e)$, rapporto $E_b/N_0$ ed efficienza spettrale $\eta_B$. Per basse probabilità d'errore conviene ragionare su $\eta_P$ e $\eta_B$.
- **Compromesso fondamentale:** in generale non si possono massimizzare insieme l'efficienza energetica e quella spettrale.

#### Slide 19 — Compromesso energia-banda · slide [[Confronto_new.pdf#page=19|p. 19]] · appunti [[Confronto new.pdf#page=21|p. 21]]

| Modulazione | $N$ | $\eta_B$ | $\eta_P$ |
|---|---|---|---|
| PAM | 1 | $2\log_2M$ | $\dfrac{3\log_2M}{M^2-1}$ |
| PSK | 2 | $\log_2M$ | $\log_2M\,\sin^2\dfrac{\pi}{M}$ |
| QAM | 2 | $\log_2M$ | $\dfrac{3\log_2M}{2(M-1)}$ |
| Ortogonale | $M$ | $\dfrac{2\log_2M}{M}$ | $\dfrac{\log_2M}{2}$ |

- Note a mano: $\eta_B$ «efficienza in banda», $\eta_P$ «efficienza in potenza»; una graffa sulle righe: «chiaro trade-off banda-potenza». (Nell'ultima riga la slide stampa $\eta_P=2\log_2M$ con un 1 scritto a mano sopra: va letto $\frac12\log_2M$, coerente con l'esempio ortogonale binario $\eta_P=\frac12$.)
- Per modulazioni la cui dimensionalità **cresce con $M$** (ortogonali), aumentare $M$ migliora l'efficienza in potenza ma riduce quella spettrale.
- Per modulazioni a **dimensionalità fissa** (PAM, PSK, QAM), aumentare $M$ migliora l'efficienza spettrale ma richiede un $E_b/N_0$ più alto a parità di affidabilità.
- Poiché la dimensionalità è legata alla banda di trasmissione, il risultato è un compromesso tra **energia e banda**.
- Appunti a lezione: per PAM, PSK e QAM $\eta_B$ **cresce** con $M$ (più efficienti in banda); per le ortogonali **decresce**, perché a ogni nuovo segnale si aggiunge una dimensione, e la dimensione è legata alla banda dal prodotto tempo-banda: aumenta anche la banda. Per questo le ortogonali sono efficienti in potenza ($\eta_P$ cresce con $M$) e si usano quando la banda è una risorsa a disposizione.

### Il limite di Shannon

#### Slide 20 — Dai parametri globali al limite di Shannon · slide [[Confronto_new.pdf#page=20|p. 20]] · appunti [[Confronto new.pdf#page=22|p. 22]]
- Per il canale AWGN: $\eta_B=R_b/W$, $\gamma=P/(N_0W)$, $\gamma=\frac{E_b}{N_0}\eta_B$.
- Dalla capacità $C=W\log_2(1+\gamma)$ e dalla condizione necessaria $R_b\le C$ segue $\eta_B\le\log_2(1+\gamma)$. Sostituendo $\gamma=\eta_BE_b/N_0$:

$$\eta_B\le\log_2\Big(1+\eta_B\frac{E_b}{N_0}\Big)\qquad\Longleftrightarrow\qquad\frac{E_b}{N_0}\ge\frac{2^{\eta_B}-1}{\eta_B}$$
- Appunti a lezione: la frontiera è un altro modo di scrivere la condizione del secondo teorema di Shannon.

#### Slide 21 — Frontiera di Shannon · slide [[Confronto_new.pdf#page=21|p. 21]] · appunti [[Confronto new.pdf#page=23|p. 23]]
- La relazione $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$ definisce la **frontiera di Shannon** nel piano $(\eta_B,E_b/N_0)$: per ogni $\eta_B$ dà il minimo $E_b/N_0$ compatibile con probabilità d'errore piccola a piacere. Ogni sistema reale deve operare **sopra** questa curva.
- Nel limite di efficienza spettrale molto bassa:

$$\lim_{\eta_B\to0}\frac{2^{\eta_B}-1}{\eta_B}=\ln2\qquad\Longrightarrow\qquad\Big(\frac{E_b}{N_0}\Big)_{min}=\ln2\approx-1.59\ \text{dB}$$

- Nota a mano: $\lim_{x\to0}\dfrac{a^x-1}{x}=\ln a$.
- Appunti a lezione (con uno schizzo delle curve BER che si avvicinano alla verticale di $-1.6$ dB): è un **limite invalicabile**; oltre non è più garantito il teorema di Shannon.

#### Slide 22 — Interpretazione fisica del limite · [[Confronto_new.pdf#page=22|p. 22]]
- Al crescere dell'efficienza spettrale $\eta_B$ cresce anche il minimo $E_b/N_0$ richiesto.
- In un sistema **limitato in potenza** si può usare banda per ridurre l'energia richiesta per bit; in un sistema **limitato in banda** si sceglie un'efficienza spettrale più alta, al costo di una potenza richiesta maggiore.
- Le curve BER delle modulazioni descrivono le prestazioni pratiche; la capacità di Shannon è il riferimento teorico assoluto.

#### Slide 23 — Compromessi nella scelta della modulazione · slide [[Confronto_new.pdf#page=23|p. 23]] · appunti [[Confronto new.pdf#page=25|p. 25]]

![[confronto-p23-efficienza-banda-potenza.png|560]]
*Piano efficienza spettrale – $E_b/N_0$ a $P_b(e)=10^{-5}$, con $W$ banda di Shannon: curva di capacità di Shannon (asintoto verticale a $-1.6$ dB), linea orizzontale a $\eta_B=1$ che separa la regione limitata in banda (sopra) da quella limitata in potenza (sotto); punti per PAM, PSK coerente, QAM, PSK differenziale, FSK coerente e FSK incoerente, con il valore di $M$ accanto.*

- Fissata la BER, ogni schema di modulazione/demodulazione è un **punto** con ascissa $E_b/N_0$ e ordinata la sua efficienza spettrale (la slide scrive $R_s/W$; è il rapporto bit rate/banda, $\eta_B$).
- **Regione limitata in banda** ($\eta_B>1$): la banda è scarsa e va scambiata con potenza, cioè con $E_b/N_0$.
- **Regione limitata in potenza** ($\eta_B<1$): gli schemi usano la banda in modo poco efficiente e la scambiano con una riduzione di $E_b/N_0$ a parità di BER.
- Nota a mano: «non viene utilizzata una codifica; in caso, i punti verrebbero traslati verso sinistra».
- Appunti a lezione: il grafico viene dal libro di **Biglieri**, da cui vedere i grafici; l'ordinata è l'efficienza in banda; la distanza dalla curva è il **margine di miglioramento**: con una codifica di canale tutti questi punti si avvicinano al limite.

### Link budget

#### Slide 24 — Elementi di un link budget · [[Confronto_new.pdf#page=24|p. 24]]
- Il progetto di un collegamento richiede: bit rate, banda disponibile, modulazione e codifica, potenza trasmessa, distanza desiderata.
- Procedura tipica:
  1. dati $R_b$ e la costellazione, si ricava il symbol rate $R_s$;
  2. si determina la banda effettiva $W$;
  3. dalla BER obiettivo e dalla modulazione si ricava il valore richiesto di $E_b/N_0$;
  4. si calcola $\text{SNR}_{req}=\big(\frac{E_b}{N_0}\big)_{req}\frac{R_b}{W}$;
  5. nota la potenza di rumore, si determina la **sensibilità** del ricevitore.

#### Slide 25 — Potenza di rumore e sensibilità · slide [[Confronto_new.pdf#page=25|p. 25]] · appunti [[Confronto new.pdf#page=27|p. 27]]
- Data la cifra di rumore $F$ del ricevitore (in dB), la potenza di rumore è

$$P_n=N_0W=kT_0\,10^{F/10}\,W$$

- La minima potenza ricevuta necessaria è $P_{rx,min}=\text{SNR}_{req}\,P_n$: è la **sensibilità** del ricevitore, spesso espressa in dBm:

$$P^{\text{dBm}}_{rx,min}=10\log_{10}\Big(\frac{P_{rx,min}}{1\ \text{mW}}\Big)$$

- Note a mano: $k$ è la costante di **Boltzmann**; $10^{F/10}$ è la «figura di rumorosità»; la formula «deriva da considerazioni quantistiche»; il dBm è «normalizzato rispetto al milliwatt», $P_0=1$ mW.
- Appunti a lezione: $k$ costante di Boltzmann; $F$ cifra di rumore, misura della rumorosità del ricevitore.

#### Slide 26 — Equazione di Friis e path loss · slide [[Confronto_new.pdf#page=26|p. 26]] · appunti [[Confronto new.pdf#page=28|p. 28]]
- Per un collegamento LOS ideale la potenza ricevuta è

$$P_{rx}=P_{tx}\,G_{tx}\,G_{rx}\,\frac{\lambda^2}{(4\pi R)^2}$$

  con $P_{tx}$ potenza trasmessa, $G_{tx}$ e $G_{rx}$ guadagni d'antenna, $\lambda=c/f_c$ lunghezza d'onda, $R$ distanza tra trasmettitore e ricevitore.
- Appunti a lezione: $\frac{\lambda^2}{(4\pi R)^2}=\frac{1}{L_{path}}$ è il **fattore di attenuazione**. Il canale radio è «aperto»: in un canale wireless il segnale può arrivare anche tramite riflessioni multiple, mentre Friis descrive il collegamento ideale in visibilità.

#### Slide 27 — Link budget in scala logaritmica · slide [[Confronto_new.pdf#page=27|p. 27]] · appunti [[Confronto new.pdf#page=29|p. 29]]
- Massimo path loss ammissibile:

$$L_{path,\text{dB}}=P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{margin,\text{dB}}$$

- Imponendo $P_{rx}\ge P_{rx,min}$ si ricava la minima potenza trasmessa necessaria oppure, a potenza fissata, la massima distanza raggiungibile.
- Appunti a lezione: $L_{path}=\big(\frac{4\pi R}{\lambda}\big)^2$; la potenza del segnale ricevuto deve essere maggiore della minima, e da qui si ricava la distanza alla quale si riesce a trasmettere e ricevere.

### Esempio: collegamento WLAN a 5 GHz

#### Slide 28–29 — Dati e bit rate · [[Confronto_new.pdf#page=28|p. 28]], [[Confronto_new.pdf#page=29|29]]
- Dati: portante 5 GHz; banda del canale 20 MHz; modulazione QPSK; eccesso di banda $a=0.33$; cifra di rumore $F=6$ dB. Si chiedono: (1) il bit rate; (2) la sensibilità per BER $=10^{-6}$; (3) la portata con $P_{tx}=100$ mW, $G_{tx}=G_{rx}=2$ dBi, margine 20 dB.
- Symbol rate: $R_s=\dfrac{W}{1+a}=\dfrac{20}{1.33}\approx15$ Msimboli/s. QPSK: $\log_2M=2$, quindi $R_b=R_s\log_2M=30$ Mbit/s.

#### Slide 30 — Sensibilità del ricevitore · [[Confronto_new.pdf#page=30|p. 30]]
- QPSK con codifica di Gray: $\text{BER}=Q\big(\sqrt{2E_b/N_0}\big)$. Nota a mano: $Q(x)=\frac12\text{erfc}\big(\frac{x}{\sqrt2}\big)$.
- Per BER $=10^{-6}$ serve circa $(E_b/N_0)_{req}\approx10.2$ dB. Quindi

$$\text{SNR}_{req,\text{dB}}=\Big(\frac{E_b}{N_0}\Big)_{req,\text{dB}}+10\log_{10}\frac{R_b}{W}=10.2+10\log_{10}\frac{30}{20}\approx12\ \text{dB}$$

- Con potenza di rumore $-95$ dBm: $P_{rx,min,\text{dBm}}=-95+12=-83$ dBm.

#### Slide 31 — Path loss ammissibile e portata · [[Confronto_new.pdf#page=31|p. 31]]
- $P_{tx}=100$ mW $=20$ dBm. Path loss massimo: $L_{path,\text{dB}}=20-(-83)+2+2-20=87$ dB.
- Invertendo la formula del path loss in spazio libero si ottiene una portata di circa $R\approx107$ m.

#### Slide 32 — Osservazione finale sull'esempio · [[Confronto_new.pdf#page=32|p. 32]]
- Con costellazioni più dense (16-QAM, 64-QAM) nella stessa banda: l'efficienza spettrale e il bit rate aumentano; l'$E_b/N_0$ richiesto per la stessa BER aumenta; la sensibilità peggiora; la portata diminuisce.
- Il progetto di un collegamento nasce sempre da un compromesso tra velocità, affidabilità, banda, energia e copertura.

### Messaggio conclusivo · [[Confronto_new.pdf#page=33|p. 33]]
- I parametri globali permettono di confrontare sistemi reali in termini di efficienza energetica e spettrale.
- La capacità di Shannon è il limite teorico fondamentale che lega bit rate, banda e SNR; il confronto con la frontiera di Shannon misura quanto una soluzione pratica è vicina all'ottimo.
- Il link budget traduce questi requisiti teorici in potenze, sensibilità e portata di un collegamento reale.

---

*Approfondimenti nel wiki (derivazioni passo per passo, grafici, esempio svolto): [[informazione-mutua-e-capacita]], [[parametri-globali-modulazioni]], [[limite-di-shannon]], [[link-budget]], [[link-budget-wlan]].*

## Lezione 13 — Stima dei parametri per la sincronizzazione

*Fonte: 11-9.pdf (appunti del 9/11, 2 pagine: p. 1 copertina, p. 2 appunti) e Synchro_Kay_example (1).pdf (36 pagine: le 33 slide «Parameter estimation for synchronization» più 3 pagine di appunti a lezione alle p. 4, 7, 17), entrambi in `raw/goodnotes/`. Corrispondenza: slide 1–3 = p. 1–3, slide 4–5 = p. 5–6, slide 6–14 = p. 8–16, slide 15–33 = p. 18–36. Le equazioni (1)–(15) sono quelle delle slide.*

### Il problema della sincronizzazione

#### Appunti — Perché serve sincronizzare · [[11-9.pdf#page=2|p. 2]]
- Finora si è supposto che trasmettitore e ricevitore siano perfettamente sincronizzati: in pratica l'ipotesi non è sempre vera, e il ricevitore deve riuscire ad agganciarsi al segnale in ingresso.
- Al ricevitore arriva $y_p(t)=A\,u_p(t-\tau)+n_p(t)$, dove $n_p(t)$ è la versione passa-banda del rumore termico.
- Poiché $f_c\tau\gg1$, anche piccoli sfasamenti provocano errori non trascurabili.
- Si suppone che l'oscillatore locale (LO) del ricevitore sia a $f_c-\Delta f$, per vedere l'effetto del non perfetto accordo tra i due oscillatori. Con il ritardo le due componenti si accoppiano: $y_I$ dipende da $v_I$ e $v_Q$ anche dopo il filtro, e non si riesce più a disaccoppiare le componenti I e Q del segnale. Il ritardo compare sia in $\theta$ sia in $\tau$.
- L'effetto della non sincronizzazione è il termine $2\pi\Delta f\,t$, che **dipende dal tempo**.

#### Slide 2 e appunti — Effetto di ritardo e offset dell'LO (1/2) · [[Synchro_Kay_example (1).pdf#page=2|p. 2]]
- Segnale in banda base complessa: $u(t)=\sum_nb(n)\,g_{TX}(t-nT)$, con $\{b(n)\}_n$ sequenza dei simboli d'informazione, $g_{TX}(t)$ impulso di trasmissione e $T$ periodo di simbolo.
- $u(t)$ è portato in banda passante da un LO alla frequenza portante $f_c$: $u_p(t)=\sqrt2\,\text{Re}(u(t)\,e^{j2\pi f_ct})$.
- Il canale è modellato come un sistema **non dispersivo**, che causa solo una scalatura d'ampiezza e un ritardo (appunti: non deforma la forma d'onda, al più ne cambia ampiezza e ritardo):

$$y_p(t)=A\,u_p(t-\tau)+n_p(t)$$

  con $A$ e $\tau$ ampiezza e ritardo incogniti e $n_p(t)$ rumore passa-banda.

#### Slide 3 e appunti — Effetto di ritardo e offset dell'LO (2/2) · [[Synchro_Kay_example (1).pdf#page=3|p. 3]], [[Synchro_Kay_example (1).pdf#page=4|4]]
- Il segnale ritardato è

$$u_p(t-\tau)=\sqrt2\,\text{Re}\big(u(t-\tau)\,e^{j2\pi f_c(t-\tau)}\big)=\sqrt2\,\text{Re}\big(u(t-\tau)\,e^{j\theta}e^{j2\pi f_ct}\big),\qquad\theta=-2\pi f_c\tau\bmod2\pi$$

- La fase $\theta$ è molto sensibile al ritardo $\tau$, perché $f_c$ assume valori molto grandi ($f_c\tau\gg1$).
- Al ricevitore $y_p(t)$ è riportato in banda base da un LO la cui frequenza in genere differisce da quella del trasmettitore. Se l'LO è a $f_c-\Delta f$, l'uscita del down-converter è l'inviluppo complesso di $y_p(t)$ rispetto a $f_c-\Delta f$:

$$y(t)=A\,e^{j(2\pi\Delta ft+\theta)}\,u(t-\tau)+n(t)=A\,e^{j(2\pi\Delta ft+\theta)}\sum_nb(n)\,g_{TX}(t-nT-\tau)+n(t)\tag{1}$$

  con $n(t)$ WGN complesso. Appunti: $\Delta f$ è l'offset (mismatch) di frequenza, e produce una rotazione residua.
- Appunti p. 4: il ritardo compare due volte nella (1), in $\theta$ e nell'argomento dell'impulso. Il motivo è che il segnale trasmesso è $u_p(t)=\sqrt2\,\text{Re}\{u(t)e^{j2\pi f_ct}\}$: quando il canale ritarda il segnale, il ritardo agisce sia sull'inviluppo sia sull'esponenziale, $u_p(t-\tau)=\sqrt2\,\text{Re}\{u(t-\tau)e^{j2\pi f_c(t-\tau)}\}$.

### Il modello in banda base complessa

#### Slide 4 e appunti — Derivazione del modello (1/4) · [[Synchro_Kay_example (1).pdf#page=5|p. 5]]
- Il segnale ricevuto è $y_p(t)=\sqrt2A\,\text{Re}\{u(t-\tau)e^{j(\omega_ct+\theta)}\}+n_p(t)$, con $\omega_c=2\pi f_c$ e $\theta=-2\pi f_c\tau$.
- Si pone $v(t)\triangleq A\,u(t-\tau)e^{j\theta}=v_I(t)+jv_Q(t)$ (appunti: l'inviluppo complesso ritardato, sfasato e scalato, cioè il segnale utile che arriva al ricevitore). Sviluppando la parte reale:

$$y_p(t)=\sqrt2\,[v_I(t)\cos(\omega_ct)-v_Q(t)\sin(\omega_ct)]+n_p(t)$$

- Il ricevitore usa un LO a $\omega_{LO}=2\pi(f_c-\Delta f)$ con due rami in quadratura (appunti: down-conversion con un oscillatore che ha un offset $\Delta f$):

$$I_{mix}(t)=\sqrt2\,y_p(t)\cos(\omega_{LO}t),\qquad Q_{mix}(t)=-\sqrt2\,y_p(t)\sin(\omega_{LO}t)$$

#### Slide 5 e appunti — Derivazione del modello (2/4): ramo in fase · [[Synchro_Kay_example (1).pdf#page=6|p. 6]], [[Synchro_Kay_example (1).pdf#page=7|7]]
- Si moltiplica $y_p$ per $\sqrt2\cos(\omega_{LO}t)$ trascurando per ora il rumore:

$$I_{mix,s}(t)=2v_I(t)\cos(\omega_ct)\cos(\omega_{LO}t)-2v_Q(t)\sin(\omega_ct)\cos(\omega_{LO}t)$$

- Con le formule di prostaferesi e $\varphi(t)\triangleq(\omega_c-\omega_{LO})t=2\pi\Delta f\,t$:

$$I_{mix,s}(t)=v_I(t)\big[\cos\varphi(t)+\cos((\omega_c+\omega_{LO})t)\big]-v_Q(t)\big[\sin\varphi(t)+\sin((\omega_c+\omega_{LO})t)\big]$$

  (appunti: il termine somma sta alla frequenza $2f_c-\Delta f$, il termine differenza è $2\pi\Delta f\,t$).
- Il filtro passa-basso elimina i termini ad alta frequenza:

$$y_I(t)=v_I(t)\cos\varphi(t)-v_Q(t)\sin\varphi(t)+n_I(t),\qquad n_I(t)=\text{LPF}\{\sqrt2\,n_p(t)\cos(\omega_{LO}t)\}$$

- Appunti p. 7: $y_I$ è la componente in fase dell'inviluppo complesso del segnale ricevuto rispetto a $f_c-\Delta f$, e dipende sia dalla componente in fase sia da quella in quadratura dell'inviluppo dello stesso segnale rispetto a $f_c$. Un segnale passa-banda può avere più inviluppi complessi, a seconda della $f_c$ che si considera.

#### Slide 6 — Derivazione del modello (3/4): ramo in quadratura · [[Synchro_Kay_example (1).pdf#page=8|p. 8]]
- Si moltiplica $y_p$ per $-\sqrt2\sin(\omega_{LO}t)$, sempre senza rumore:

$$Q_{mix,s}(t)=-2v_I(t)\cos(\omega_ct)\sin(\omega_{LO}t)+2v_Q(t)\sin(\omega_ct)\sin(\omega_{LO}t)=v_I(t)\big[\sin\varphi(t)-\sin((\omega_c+\omega_{LO})t)\big]+v_Q(t)\big[\cos\varphi(t)-\cos((\omega_c+\omega_{LO})t)\big]$$

- Dopo il passa-basso: $y_Q(t)=v_I(t)\sin\varphi(t)+v_Q(t)\cos\varphi(t)+n_Q(t)$, con $n_Q(t)=\text{LPF}\{-\sqrt2\,n_p(t)\sin(\omega_{LO}t)\}$.

#### Slide 7 e appunti — Derivazione del modello (4/4): ricombinazione · [[Synchro_Kay_example (1).pdf#page=9|p. 9]]
- Ricombinando le uscite dei due rami si ottiene l'inviluppo complesso del segnale ricevuto:

$$y(t)\triangleq y_I(t)+jy_Q(t)=[v_I(t)+jv_Q(t)]\,[\cos\varphi(t)+j\sin\varphi(t)]+n(t)=v(t)\,e^{j\varphi(t)}+n(t)$$

  con $n(t)\triangleq n_I(t)+jn_Q(t)$.
- Ricordando $v(t)=A\,u(t-\tau)e^{j\theta}$ e $\varphi(t)=2\pi\Delta ft$ si ritrova la (1): $y(t)=A\,e^{j(2\pi\Delta ft+\theta)}u(t-\tau)+n(t)$.

### Sincronizzazione di tempo e di portante

#### Slide 8 e appunti — Compiti e fasi · [[Synchro_Kay_example (1).pdf#page=10|p. 10]]
- Compiti del blocco di sincronizzazione del ricevitore:
  - **sincronizzazione di tempo** (timing) ⇒ stima di $\tau$;
  - **sincronizzazione di portante** ⇒ stima di $\Delta f$ e $\theta$ (appunti: lo sfasamento provocato dal ritardo). Appunti: anche se $\theta$ è provocato dal ritardo, lo risolve il blocco di sincronizzazione della portante.
- Il processo avviene di solito in due fasi:
  - **acquisizione** dei parametri: si ottiene una stima iniziale, spesso con un blocco di simboli di training noti posti in un preambolo all'inizio della trasmissione;
  - **inseguimento** (tracking): le stime iniziali sono aggiornate di continuo per seguire i parametri che variano lentamente nel tempo (fenomeno di **drift**).

#### Slide 9 e appunti — Modalità decision-directed e blind · [[Synchro_Kay_example (1).pdf#page=11|p. 11]]
- Nei sistemi a pacchetto, molto comuni sia su filo sia senza fili, la variazione dei parametri in un pacchetto è spesso trascurabile: la fase di tracking si può eliminare.
- Il tracking segue l'acquisizione, e durante il tracking i simboli di training non sono più disponibili. L'algoritmo lavora allora in uno di due modi:
  - **decision-directed** ⇒ i simboli di training sono sostituiti dalle decisioni retroazionate dal demodulatore al blocco di sincronizzazione (appunti: la sincronizzazione è guidata dalle decisioni del demodulatore, per una stima continua dei parametri);
  - **blind** ⇒ il blocco è progettato in modo da essere insensibile ai valori specifici dei simboli trasmessi (appunti: non riceve alcuna informazione dal demodulatore e conosce solo le proprietà statistiche dei simboli; stima i parametri senza sapere quali simboli sono stati trasmessi).

### Fondamenti della stima dei parametri

#### Slide 10 e appunti — Il problema della stima · [[Synchro_Kay_example (1).pdf#page=12|p. 12]]
- Il problema della stima consiste nell'estrarre i valori di parametri (qui $\tau$, $\theta$ o $\Delta f$) da un segnale a tempo continuo o, in modo equivalente, da un segnale a tempo discreto o da un insieme di dati. Molti campi diversi usano la teoria della stima.
- Si ha l'insieme di $K$ dati (appunti: campioni del segnale ricevuto) $\{y(0),y(1),\dots,y(K-1)\}$ che dipende da un parametro incognito $\theta$; si vuole determinare $\theta$ dai dati, cioè definire uno **stimatore**

$$\hat\theta=g\big(y(0),y(1),\dots,y(K-1)\big)$$

  con $g(\cdot)$ una funzione.

#### Slide 11 e appunti — Il modello dei dati · [[Synchro_Kay_example (1).pdf#page=13|p. 13]]
- Il primo passo è modellare matematicamente i dati. Essendo intrinsecamente aleatori, si descrivono con la pdf $f(\mathbf y;\theta)$, $\mathbf y\triangleq[y(0),y(1),\dots,y(K-1)]$ (appunti: la pdf congiunta dei $K$ campioni, che dice quanto è probabile ottenere quei campioni).
- $f(\mathbf y;\theta)$ è parametrizzata dal parametro incognito: si ha una **famiglia di pdf**, una diversa per ogni valore di $\theta$.
- Esempio: con $K=1$ e $\theta$ uguale alla media,

$$f(y(0);\theta)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{1}{2\sigma^2}\big(y(0)-\theta\big)^2\Big]\tag{2}$$

  Figura: tre pdf gaussiane della famiglia, centrate in $\theta_1<\theta_2<\theta_3$. Se il dato osservato $y(0)$ è negativo, è ragionevole il valore $\theta=\theta_1$, quello della pdf più a sinistra.

#### Slide 12 e appunti — Esempio: livello continuo nel rumore · [[Synchro_Kay_example (1).pdf#page=14|p. 14]]
- $K$ osservazioni rumorose di un'ampiezza costante incognita $A$ (appunti: il segnale inviato è costante e uguale ad $A$, e vi si aggiunge rumore):

$$y(k)=A+n(k),\qquad k=0,\dots,K-1,\qquad n(k)\ \text{i.i.d.}\sim\mathcal N(0,\sigma^2)$$

- $A$ è fissa, ma le osservazioni sono aleatorie: ripetendo l'esperimento con la stessa $A$ si ottengono insiemi di dati diversi.
- Uno stimatore semplice (appunti: il più semplice) è la **media campionaria**:

$$\hat A=\frac1K\sum_{k=0}^{K-1}y(k)=A+\frac1K\sum_{k=0}^{K-1}n(k)$$

  $\hat A$ è anch'essa una variabile aleatoria, con $E[\hat A]=A$ (il rumore ha media nulla) e $\text{Var}(\hat A)=\sigma^2/K$ (la varianza della somma di $K$ termini indipendenti è $K\sigma^2$, divisa per $K^2$).
- Lo stimatore è **non polarizzato** (in media dà il valore giusto, senza errori sistematici) e **consistente** (più campioni si considerano, più la varianza si riduce: tende a zero per $K\to\infty$).

#### Slide 13 e appunti — Approccio classico e approccio bayesiano · [[Synchro_Kay_example (1).pdf#page=15|p. 15]]
- Se il parametro è **deterministico ma incognito** ⇒ **approccio classico**: non c'è modo di includere informazioni a priori su $\theta$. La stima basata sulla (2) è un esempio di stima classica.
- Se il parametro è modellato come **variabile aleatoria** con una sua pdf ⇒ **approccio bayesiano**: il parametro da stimare è visto come una realizzazione della v.a. $\theta$.
- Nella stima bayesiana dati e parametro sono descritti dalla pdf congiunta

$$f(\mathbf y,\theta)=f(\mathbf y\mid\theta)\,f(\theta)$$

  con $f(\mathbf y\mid\theta)$ pdf condizionata (la conoscenza fornita dai dati, noto $\theta$) e $f(\theta)$ pdf del parametro. La conoscenza a priori entra nella stima attraverso il modello stocastico del parametro.
- Va notata la differenza tra $f(\mathbf y;\theta)$, una **famiglia** di pdf (approccio classico), e $f(\mathbf y\mid\theta)$, una pdf **condizionata** (approccio bayesiano).

#### Slide 14 e appunti — Stima a massima verosimiglianza · [[Synchro_Kay_example (1).pdf#page=16|p. 16]], [[Synchro_Kay_example (1).pdf#page=17|17]]
- Da qui si segue l'approccio classico e in particolare la **stima a massima verosimiglianza** (MLE): il valore di $\theta$ che massimizza la funzione di verosimiglianza $f(\mathbf y;\theta)$,

$$\hat\theta=\arg\max_\theta f(\mathbf y;\theta)=\arg\max_\theta\log f(\mathbf y;\theta)$$

- Quando la pdf è vista come funzione del parametro incognito, con i dati $\mathbf y$ fissati, si chiama **funzione di verosimiglianza** e si indica con $\Lambda_\theta(\mathbf y)$, come nella rivelazione.
- Appunti p. 17: la decisione a massima verosimiglianza della rivelazione è un caso particolare della stima ML, in cui il parametro da stimare è il simbolo trasmesso e può assumere solo $M$ valori. In entrambi i casi si usa la pdf dei valori osservati vista come funzione del parametro e si sceglie il valore che la massimizza. Nella rivelazione la massimizzazione è un confronto tra $M$ valori, realizzato con un banco di correlatori; nella stima il parametro è continuo e si massimizza annullando la derivata.

### Esempio: stima ML dell'ampiezza

#### Slide 15 e appunti — Il modello · [[Synchro_Kay_example (1).pdf#page=18|p. 18]]
- Si considera un segnale antipodale binario all'uscita del down-converter, con $\tau=0$ e $\Delta f=0$ (appunti: niente ritardo e niente offset di frequenza, il segnale ricevuto è solo scalato):

$$y(t)=A\sum_nb(n)\,g_{TX}(t-nT)+n(t)$$

- I campioni all'uscita della cascata filtro adattato $g_{TX}(T-t)$ (che massimizza il rapporto segnale-rumore, vedi la rivelazione) e campionatore a $kT$, seguita dal decisore (figura), sono

$$y(k)=A\,b(k)+n(k),\qquad k=0,1,\dots,K-1$$

  con $y(k)\triangleq y(kT)$, $n(k)\triangleq n(kT)\sim\mathcal N(0,\sigma^2)$, $b(k)\in\{+1,-1\}$ simboli trasmessi e $A$ ampiezza incognita da stimare.

#### Slide 16 e appunti — Training-based e blind · [[Synchro_Kay_example (1).pdf#page=19|p. 19]]
- Si vuole la stima ML di $A$ dai dati $\mathbf y=(y(0),\dots,y(K-1))$. La stima dell'ampiezza è cruciale nei ricevitori per segnali modulati in ampiezza.
- Due casi:
  1. i simboli $\{b(k)\}$ sono **noti** ⇒ **stima training-based** (appunti: stima basata su una sequenza di simboli noti);
  2. i simboli sono **incogniti** e modellati come v.a. statisticamente indipendenti ⇒ **stima blind** (appunti: non si sfruttano le decisioni del demodulatore).
- La stima ML è

$$\hat A=\arg\max_A\log f(\mathbf y;A)=\arg\max_A\sum_{k=0}^{K-1}\log f(y(k);A)\tag{3}$$

  (appunti: i campioni sono statisticamente indipendenti, quindi la pdf congiunta è il prodotto delle marginali e il logaritmo del prodotto è la somma dei logaritmi).

#### Slide 17 e appunti — Approccio training-based · [[Synchro_Kay_example (1).pdf#page=20|p. 20]]
- Se $b(k)$ è noto, $y(k)=A\,b(k)+n(k)$ è una v.a. gaussiana con media $A\,b(k)$ e varianza $\sigma^2$. La (3) diventa (appunti: resta l'esponente della pdf marginale, e massimizzare $-(\cdot)^2$ vuol dire minimizzarne l'argomento)

$$\arg\min_A\sum_{k=0}^{K-1}\big(y(k)-A\,b(k)\big)^2$$

- Derivando rispetto ad $A$ e annullando ($b^2(k)=1$):

$$\hat A=\frac1K\sum_{k=0}^{K-1}y(k)\,b(k)$$

- La MLE si ottiene **correlando i campioni ricevuti con la sequenza di training**. La generalizzazione a simboli complessi è lasciata al lettore (appunti: da generalizzare per segnali complessi).

#### Slide 18 — Blind approach (1/2) · [[Synchro_Kay_example (1).pdf#page=21|p. 21]]
- La stima **blind** (cieca) è la stima senza sequenza di training. I simboli $\{b(k)\}$ si modellano come v.a. statisticamente indipendenti che valgono $\pm1$ con uguale probabilità.
- Condizionato all'evento $\{b(k)=+1\}$, il campione $y(k)=A+n(k)$ è gaussiano con media $A$ e varianza $\sigma^2$:

$$f\big(y(k)\mid\{b(k)=1\};A\big)=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{1}{2\sigma^2}(y(k)-A)^2}\tag{4}$$

- Condizionato all'evento $\{b(k)=-1\}$, il campione $y(k)=-A+n(k)$ è gaussiano con media $-A$ e varianza $\sigma^2$:

$$f\big(y(k)\mid\{b(k)=-1\};A\big)=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{1}{2\sigma^2}(y(k)+A)^2}\tag{5}$$

- Si richiama la **legge della probabilità totale** per le pdf: $f(x)=\sum_{i=1}^nf(x\mid A_i)\,P(A_i)$.

#### Slide 19 e appunti — Blind approach (2/2) · [[Synchro_Kay_example (1).pdf#page=22|p. 22]]
- Con la probabilità totale la funzione di verosimiglianza diventa una **miscela di due gaussiane**:

$$f(y(k);A)=\tfrac12f\big(y(k)\mid\{b(k)=-1\};A\big)+\tfrac12f\big(y(k)\mid\{b(k)=1\};A\big)\tag{6}$$

$$f(y(k);A)=\frac12\,\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{1}{2\sigma^2}(y(k)+A)^2}+\frac12\,\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{1}{2\sigma^2}(y(k)-A)^2}\tag{7}$$

- La stima ML blind (appunti: il valore di $A$ che massimizza la funzione di verosimiglianza) è $\hat A=\arg\max_A\sum_{k=0}^{K-1}\log f(y(k);A)$ con $f(y(k);A)$ data dalla (7).
- Annullando la derivata della funzione costo rispetto ad $A$ si mostra che la MLE soddisfa l'**equazione trascendente**

$$\hat A=\frac1K\sum_{k=0}^{K-1}y(k)\,\tanh\Big(\frac{\hat A\,y(k)}{\sigma^2}\Big)$$

  (scrivendo la (7) come $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{y^2+A^2}{2\sigma^2}}\cosh\frac{Ay}{\sigma^2}$, la derivata del logaritmo è $-\frac{A}{\sigma^2}+\frac{y}{\sigma^2}\tanh\frac{Ay}{\sigma^2}$).

#### Slide 20 e appunti — Conclusioni · [[Synchro_Kay_example (1).pdf#page=23|p. 23]]
- La stima training-based usa simboli $b(k)$ noti a trasmettitore e ricevitore (simboli di training), di solito in un preambolo all'inizio della trasmissione. È detta anche **data-aided (DA)** (appunti: assistita dai dati) e si può realizzare anche in modalità decision-directed, se le decisioni fornite agli algoritmi di sincronizzazione sono abbastanza affidabili.
- Le sequenze di training rendono robusta la stima ma comportano una **perdita di risorse** (appunti: una parte della trasmissione è occupata da segnali noti).
- La stima blind non richiede i simboli $b(k)$ ma solo la loro statistica (informazione media) e la PSD del disturbo. È detta anche **non-data-aided (NDA)** ed è più complessa della DA.

### La rivelazione M-aria come stima

#### Slide 21 — Segnalazione M-aria in AWGN rivisitata · [[Synchro_Kay_example (1).pdf#page=24|p. 24]]
- Il test tra $M$ ipotesi $H_k:\ y(t)=s_k(t)+n(t)$, $k=1,\dots,M$, è un caso particolare di stima dei parametri, con parametro $\theta_k=H_k$ che assume uno di $M$ valori possibili.
- La funzione di verosimiglianza per la versione in banda base complessa del segnale ricevuto in AWGN (PSD totale $2\sigma^2$, cioè $\sigma^2$ per componente reale) è

$$\Lambda_k(y)=\exp\Big[\frac{1}{\sigma^2}\Big(\text{Re}\big(\langle y(t),s_k(t)\rangle\big)-\frac12\lVert s_k(t)\rVert^2\Big)\Big]\tag{8}$$

- La regola di decisione ML della rivelazione si interpreta come la MLE di un parametro a $M$ valori:

$$\hat H_k=\arg\max_k\Lambda_k(y)=\arg\max_k\lambda_k(y)\tag{9}$$

  con $\lambda_k(y)=\log\Lambda_k(y)$, realizzata con un banco di correlatori (o di filtri adattati seguiti da campionatori).

### Stima ML della fase

#### Slide 22 e appunti — Il modello e l'origine della fase · [[Synchro_Kay_example (1).pdf#page=25|p. 25]]
- Si riprende il modello (1), $y(t)=A\,e^{j(2\pi\Delta ft+\theta)}u(t-\tau)+n(t)$, supponendo già fatte la sincronizzazione di tempo e la stima d'ampiezza.
- Il termine di fase comprende il **mismatch degli LO** e l'**effetto Doppler** (appunti: $\Delta f$ produce una fase tempo-variante).
- Il mismatch degli LO è l'effetto dell'offset di frequenza tra gli oscillatori di trasmettitore e ricevitore: è dell'ordine di 10–100 ppm rispetto alla portante $f_c$.
- Lo spostamento Doppler nei canali radiomobili è $v f_c/c$, con $v$ velocità relativa tra trasmettitore e ricevitore e $c$ velocità della luce nel vuoto: circa 0,2 ppm per 200 km/h.

#### Slide 23 e appunti — Fase costante su più simboli · [[Synchro_Kay_example (1).pdf#page=26|p. 26]]
- Con le bande tipiche dei segnali in banda base, la variazione di fase $2\pi\Delta f\,T$ indotta in un intervallo di simbolo da mismatch e Doppler si può supporre piccola ⇒ la fase si può prendere **costante su più intervalli di simbolo** (appunti: tempo-invariante).
- Modello: $y(t)=e^{j\theta}s(t)+n(t)$, con $\theta$ fase incognita.
- Dalla (8), la funzione di verosimiglianza diventa

$$\Lambda_\theta(y)=\exp\Big[\frac{1}{\sigma^2}\Big(\text{Re}\big(\langle y(t),s(t)\,e^{j\theta}\rangle\big)-\frac12\lVert s(t)\,e^{j\theta}\rVert^2\Big)\Big]$$

#### Slide 24 — La funzione da massimizzare · [[Synchro_Kay_example (1).pdf#page=27|p. 27]]
- $\lVert s(t)\,e^{j\theta}\rVert^2=\lVert s(t)\rVert^2$: non dipende da $\theta$.
- Ponendo $\langle y(t),s(t)\rangle=|Z|\,e^{j\phi}=Z_c+jZ_s$:

$$\text{Re}\big(\langle y(t),s(t)\,e^{j\theta}\rangle\big)=\text{Re}\big(\langle y(t),s(t)\rangle\,e^{-j\theta}\big)=|Z|\cos(\phi-\theta)$$

- La stima ML di $\theta$ si ottiene massimizzando

$$\Lambda_\theta(y)=\exp\Big[\frac{1}{\sigma^2}\Big(|Z|\cos(\phi-\theta)-\frac12\lVert s(t)\rVert^2\Big)\Big]\tag{10}$$

#### Slide 25 e appunti — Lo stimatore e lo schema · [[Synchro_Kay_example (1).pdf#page=28|p. 28]]
- La soluzione è

$$\hat\theta=\phi=\arg\big(\langle y(t),s(t)\rangle\big)=\tan^{-1}\frac{Z_s}{Z_c}$$

- Schema del blocco di stima (figura): il segnale passa-banda ricevuto $y_p(t)$ è moltiplicato per $\sqrt2\cos2\pi f_ct$ e per $-\sqrt2\sin2\pi f_ct$ e filtrato passa-basso, dando $y_c(t)$ e $y_s(t)$; ciascuno passa per i filtri adattati $s_c(-t)$ e $s_s(-t)$ campionati in $t=0$; le uscite combinate danno $Z_c$ e $Z_s$, e il blocco $\tan^{-1}(Z_s/Z_c)$ fornisce $\hat\theta_{ML}$. Le combinazioni vengono da $\langle y,s\rangle=\int(y_c+jy_s)(s_c-js_s)\,dt$: $Z_c=\langle y_c,s_c\rangle+\langle y_s,s_s\rangle$, $Z_s=\langle y_s,s_c\rangle-\langle y_c,s_s\rangle$.
- Appunti: l'errore dovuto alla rotazione della costellazione non dipende dall'errore additivo.

### Inseguimento della fase

#### Slide 26 e appunti — Phase tracking · [[Synchro_Kay_example (1).pdf#page=29|p. 29]]
- Dopo la stima si possono aggiornare i parametri per seguirne le variazioni nel tempo.
- La maggior parte degli algoritmi di tracking massimizza rispetto a $\theta$ una funzione costo $J(\theta)$, di solito proporzionale alla log-verosimiglianza; la massimizzazione si fa con procedure iterative.
- Un approccio diffuso (appunti: uno degli algoritmi che possono realizzare il tracking) è l'algoritmo **steepest ascent**: parte da una stima iniziale di $\theta$ e la modifica ripetutamente per far crescere $J(\theta)$, finché si spera di convergere al valore che la massimizza.

#### Slide 27 e appunti — Steepest ascent e gradient descent · [[Synchro_Kay_example (1).pdf#page=30|p. 30]]
- Partendo da un valore iniziale di $\hat\theta$, l'algoritmo (appunti: un algoritmo per minimizzare o massimizzare funzionali) ripete l'aggiornamento

$$\hat\theta_{k+1}:=\hat\theta_k+\alpha\,\frac{\partial}{\partial\theta}J(\theta)\Big|_{\theta=\hat\theta_k}$$

  con $:=$ operatore di assegnazione, $\alpha$ **learning rate** (passo) e $k$ indice del passo; $J$ è la funzione da massimizzare.
- Se si deve **minimizzare** $J(\theta)$ si usa il **gradient descent** (steepest descent):

$$\hat\theta_{k+1}:=\hat\theta_k-\alpha\,\frac{\partial}{\partial\theta}J(\theta)\Big|_{\theta=\hat\theta_k}$$

### Il phase-locked loop

#### Slide 28 e appunti — Il modello · [[Synchro_Kay_example (1).pdf#page=31|p. 31]]
- Con questo schema si ricava la struttura classica del **phase-locked loop (PLL)** per l'inseguimento della fase della portante; per semplicità si lavora con segnali passa-banda nel dominio analogico (appunti: si usa questo framework per individuare e progettare il PLL).
- Si considera una sinusoide non modulata e rumorosa:

$$y_p(t)=\cos(2\pi f_ct+\theta(t))+n_p(t)=s_p(t)+n_p(t)$$

  con $\theta(t)$ fase da inseguire e $n_p(t)$ WGN reale passa-banda di PSD $\sigma^2$. Con la convenzione passa-banda vista prima, questa sinusoide di ampiezza unitaria corrisponde all'inviluppo complesso $u(t)=e^{j\theta(t)}/\sqrt2$, e la derivazione del PLL non cambia.
- Alla fine del $k$-esimo intervallo si ha la stima $\hat\theta_k$ e la si vuole correggere osservando il segnale nell'intervallo successivo, di durata $T_0$. La funzione di verosimiglianza (vedi la rivelazione) è

$$\Lambda_\theta(y_p)=\exp\Big[\frac{1}{\sigma^2}\Big(\langle y_p(t),s_p(t)\rangle-\frac12\lVert s_p(t)\rVert^2\Big)\Big]\tag{11}$$

  con $\langle x_1(t),x_2(t)\rangle=\int_{T_0}x_1(t)x_2(t)\,dt$ per segnali reali.

#### Slide 29 e appunti — Funzione costo e aggiornamento · [[Synchro_Kay_example (1).pdf#page=32|p. 32]]
- Ipotesi: $f_cT_0\gg1$ e $\theta(t)$ lentamente variabile in $[kT_0,(k+1)T_0]$. Allora l'energia del segnale è $\lVert s_p(t)\rVert^2\approx T_0/2$ (appunti: serve un'ipotesi, altrimenti l'energia dipenderebbe da $\theta(t)$; se $\theta$ varia bruscamente non c'è garanzia che ne sia indipendente).
- Dalla (11) si costruisce la funzione costo

$$J(\theta)=\langle y_p(t),s_p(t)\rangle=\int_{kT_0}^{(k+1)T_0}y_p(t)\cos(2\pi f_ct+\theta(t))\,dt$$

- Applicando lo steepest ascent (la derivata di $\cos$ dà $-\sin$):

$$\hat\theta_{k+1}:=\hat\theta_k-\alpha\int_{kT_0}^{(k+1)T_0}y_p(t)\sin(2\pi f_ct+\hat\theta_k)\,dt\tag{12}$$

- Appunti: il PLL è la realizzazione di uno stimatore ML.

#### Slide 30 e appunti — La struttura del PLL · [[Synchro_Kay_example (1).pdf#page=33|p. 33]]
- La realizzazione pratica della (12) è la struttura PLL della figura: il segnale ricevuto $y_p(t)=\cos(2\pi f_ct+\theta)+$ rumore è moltiplicato per $-\sin(2\pi f_ct+\hat\theta)$ generato dal VCO; il prodotto passa per il **loop filter**, la cui uscita pilota il VCO.
- Il loop filter è un filtro passa-basso che realizza l'integrale della (12) (appunti: esegue l'integrale).
- Il **VCO** (voltage controlled oscillator) genera una portante la cui frequenza varia linearmente con l'ampiezza di un segnale di controllo.

#### Slide 31 e appunti — VCO e aggancio · [[Synchro_Kay_example (1).pdf#page=34|p. 34]]
- Il prodotto tra portante generata e segnale ricevuto, filtrato passa-basso, va al VCO, la cui frequenza istantanea cambia secondo

$$\frac{d\hat\theta(t)}{dt}=\gamma\,c(t)\tag{13}$$

- Se la tensione di controllo è $c(t)=0$, $\hat\theta(t)$ è costante ⇒ **stato di aggancio** (phase-locked; appunti: condizione di aggancio).
- Per piccole variazioni di $\hat\theta(t)$, ragionevoli durante il tracking,

$$\frac{d\hat\theta(t)}{dt}\approx\frac{\hat\theta(t)-\hat\theta(t-\Delta t)}{\Delta t}\tag{14}$$

  che mostra che il PLL realizza una relazione come la (12).
- Per capire il comportamento del PLL si suppone il segnale ricevuto senza rumore.

#### Slide 32 e appunti — Il termine d'errore · [[Synchro_Kay_example (1).pdf#page=35|p. 35]]
- Senza rumore, con la formula di Werner $\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$:

$$\int_{kT_0}^{(k+1)T_0}y_p(t)\sin(2\pi f_ct+\hat\theta_k)\,dt=\frac12\int_{kT_0}^{(k+1)T_0}\big[\sin(4\pi f_ct+\hat\theta_k+\theta(t))+\sin(\hat\theta_k-\theta(t))\big]dt\approx\frac{T_0}{2}\sin(\hat\theta_k-\theta_{k+1})\tag{15}$$

  (il termine a $2f_c$ ha integrale trascurabile perché $f_cT_0\gg1$; $\theta(t)\approx\theta_{k+1}$ nell'intervallo).
- $\sin(\hat\theta_k-\theta_{k+1})$ è un buon **indicatore d'errore**: se è positivo $\hat\theta_k$ è maggiore di $\theta_{k+1}$, se è negativo è minore; il modulo dice quanto la stima precedente è lontana da $\theta_{k+1}$. Appunti: se $\hat\theta=\theta$ il PLL è agganciato.

#### Slide 33 — Costas loop · [[Synchro_Kay_example (1).pdf#page=36|p. 36]]
- Il PLL non funziona bene se il segnale d'ingresso ha rapide variazioni d'ampiezza o di fase dovute alla modulazione.
- Per i segnali modulati in ampiezza si può usare il **Costas loop** (figura): $r(t)$ è moltiplicato per $\cos[2\pi f_ct+\phi_v(t)]$ e per $-\sin[2\pi f_ct+\phi_v(t)]$ (il secondo ottenuto dal primo con uno sfasatore $\pi/2$), ciascun prodotto passa per un LPF dando $e_1(t)$ ed $e_2(t)$; il prodotto $e(t)=e_1(t)\,e_2(t)$ va al loop filter, che produce $v(t)$ e pilota il VCO.

---

*Approfondimenti nel wiki (derivazioni passo per passo, sanity check, grafici): [[stima-dei-parametri]], [[sincronizzazione]], [[phase-locked-loop]].*

## Lezione 14 — Segnalazione su canali a banda limitata

*Fonte: signaling_bandlimited_channel.pdf (47 slide «Signaling over bandlimited channels» con appunti a lezione sulle slide 2, 3, 9, 13, 14, 18; in `raw/goodnotes/`). Il numero di pagina coincide con quello della slide. Le equazioni (1)–(16) sono quelle delle slide.*

### Canali a banda limitata e interferenza intersimbolica

#### Slide 2 e appunti — Introduzione (1/2) · [[signaling_bandlimited_channel.pdf#page=2|p. 2]]
- Nella trasmissione su canale AWGN non c'è limite sulla banda del canale: $E_b/N_0$ è l'unico fattore che determina le prestazioni del ricevitore.
- Un canale reale non è solo rumoroso: ha anche **banda finita**. Se un impulso rettangolare, che rappresenta un simbolo, attraversa un canale a banda limitata, all'uscita la sua forma è distorta.
- Appunti (schizzo): finora il canale era un sommatore, $s(t)+n_p(t)$; adesso è un blocco **canale** seguito dal sommatore del rumore. Il canale non è solo un sommatore: ha una propria risposta impulsiva che modifica lo spettro del segnale in ingresso, e non è un sistema identico.

#### Slide 3 e appunti — Introduzione (2/2) · [[signaling_bandlimited_channel.pdf#page=3|p. 3]]
- I lobi laterali dell'impulso distorto sono una sorgente di distorsione detta **interferenza intersimbolica** (ISI), perché degrada i simboli adiacenti.
- Differenza fondamentale tra ISI e rumore:
  - il **rumore** è indipendente dal segnale trasmesso: il suo effetto compare all'ingresso del ricevitore appena si accende il sistema;
  - l'**ISI dipende dal segnale**: scompare solo quando si spegne il segnale trasmesso (appunti: dipende dal segnale trasmesso, a differenza del rumore termico).

#### Slide 4–5 — Effetto del rumore: perdita di SNR · [[signaling_bandlimited_channel.pdf#page=4|p. 4]], [[signaling_bandlimited_channel.pdf#page=5|5]]
- Un sistema ha BER teorica data dalla curva continua in funzione di $E_b/N_0$; se le prestazioni seguono invece la curva tratteggiata, si ha una **perdita di SNR**, causata da perdite di segnale o da un aumento di rumore o interferenza.
- Per BER $=10^{-5}$ la curva teorica richiede $E_b/N_0=10$ dB; quella tratteggiata 12 dB: servono **2 dB in più**. È un problema soprattutto per i sistemi limitati in potenza.
- Figura (slide 5): BER da $1$ a $10^{-5}$ in funzione di $E_b/N_0$ da $-10$ a 12 dB; la curva tratteggiata è la continua traslata di 2 dB a destra.

#### Slide 6–7 — Effetto dell'ISI: BER irriducibile · [[signaling_bandlimited_channel.pdf#page=6|p. 6]], [[signaling_bandlimited_channel.pdf#page=7|7]]
- Se il sistema è degradato da rumore **e** ISI (curva tratteggiata della slide 7), nessun aumento di $E_b/N_0$ risolve il problema: la curva presenta un **pavimento** (BER floor, nella figura poco sotto $10^{-4}$, circa $4\cdot10^{-5}$), e aumentare $E_b/N_0$ non serve se il pavimento sta sopra la BER richiesta.
- Il rimedio è l'**equalizzazione**: poiché l'ISI è causata dal filtraggio nel trasmettitore e nel canale, l'equalizzazione è il processo che inverte questi effetti di filtraggio non ottimi.

#### Slide 8 — Modulazione lineare · [[signaling_bandlimited_channel.pdf#page=8|p. 8]]
- Forma d'onda trasmessa in banda base complessa per modulazione lineare bidimensionale (PSK o QAM):

$$u(t)=\sum_ns(n)\,g(t-nT)=\Big[\sum_ns(n)\,\delta(t-nT)\Big]\ast g(t)\tag{1}$$

- $s(n)=s_1(n)+js_2(n)$, $n\in\mathbb Z$, sono i simboli complessi associati a $b=\log_2M$ bit, presi da una costellazione fissa $s(n)\in\{s_1,\dots,s_M\}$, $M=2^b$, $s_i=s_{i1}+js_{i2}$; $g(t)$ è un impulso di sagomatura fisso in banda base.
- Symbol rate (baud rate) $1/T$, con $T=bT_b$ intervallo di simbolo e $T_b$ intervallo di bit; bit rate $R_b=b/T=(\log_2M)/T$ bit/s.
- La PAM è il caso particolare della (1) con simboli reali (costellazione monodimensionale).

#### Slide 9 e appunti — Modello del sistema · [[signaling_bandlimited_channel.pdf#page=9|p. 9]]
- Schema: $s(n)$ (impulsi distanti $T$) → **filtro di trasmissione** $g(t)$ → $u(t)$ (impulsi sagomati) → **canale** $h(t)$, a cui si somma il **rumore** → **filtro di ricezione** $c(t)$ → campionatore a $t=kT$ → **decisore**.
- Appunti: si fa riferimento solo agli inviluppi complessi; il canale è un sistema non trasparente; il campionatore in prima ipotesi è perfettamente sincronizzato.

#### Slide 10 — Interferenza intersimbolica (1/4) · [[signaling_bandlimited_channel.pdf#page=10|p. 10]]
- Si usa la rappresentazione in banda base complessa di segnali e filtri e si suppone sincronizzazione perfetta.
- L'inviluppo $u(t)$ è modificato dal canale a banda limitata di risposta impulsiva $h(t)$: il segnale ricevuto in banda base complessa (dopo la downconversion) è $x(t)=u(t)\ast h(t)+n(t)$, con $n(t)$ WGN.
- In AWGN, con $h(t)=\delta(t)$, il rivelatore ottimo (simbolo per simbolo) è la cascata filtro adattato + campionatore.
- Su canale a banda limitata si vuole un ricevitore fatto da un filtro lineare (**filtro di ricezione**) di risposta $c(t)$ seguito da un campionatore a rate $1/T$; i campioni di $y(t)$ presi ogni $T$ secondi vanno al decisore.

#### Slide 11–12 — Interferenza intersimbolica (2/4)–(3/4) · [[signaling_bandlimited_channel.pdf#page=11|p. 11]], [[signaling_bandlimited_channel.pdf#page=12|12]]
- A meno di un fattore di scala, il segnale senza rumore all'uscita del filtro di ricezione è

$$y(t)=\sum_ns(n)\,p(t-nT)=\Big[\sum_ns(n)\,\delta(t-nT)\Big]\ast p(t),\qquad p(t)=g(t)\ast h(t)\ast c(t)\tag{2}$$

- Nell'argomento di $p(t-nT)$ andrebbe un ritardo arbitrario $t_0$ che rappresenta il ritardo di trasmissione attraverso il sistema; lo si pone a zero senza perdita di generalità.
- L'impulso complessivo è una doppia convoluzione (3); in frequenza la convoluzione diventa prodotto:

$$p(t)=g(t)\ast h(t)\ast c(t)\tag{3}\qquad\Longleftrightarrow\qquad P(f)=G(f)\,H(f)\,C(f)$$

#### Slide 13 e appunti — Interferenza intersimbolica (4/4) · [[signaling_bandlimited_channel.pdf#page=13|p. 13]]
- Campionando all'istante $t_k=kT$, $k\in\mathbb Z$ (appunti: si vuole ottenere il simbolo $k$-esimo):

$$y(t_k)=\sum_{n=-\infty}^{+\infty}s(n)\,p[(k-n)T]=s(k)+\sum_{\substack{n=-\infty\\n\neq k}}^{+\infty}s(n)\,p[(k-n)T]$$

  con l'impulso normalizzato, $p(0)=1$ (appunti: il primo termine sarebbe $s(k)p(0)$, e si normalizza come se si avesse un amplificatore in ricezione).
- $s(k)$ è il contributo del simbolo $k$-esimo; la somma è l'effetto residuo di tutti gli altri simboli sulla decisione del $k$-esimo, dovuto agli impulsi prima e dopo l'istante di campionamento: è l'**ISI** (appunti: due contributi per il simbolo $k$-esimo, il secondo è il termine di ISI, che dipende dai simboli precedenti e successivi).
- Senza ISI la somma è nulla ⇒ il modello del segnale è lo stesso del canale AWGN.
- Appunti: con il rumore $y_k=p(0)s(k)+i(k)+n(k)$, mentre in AWGN si aveva $y_k=s_kp(0)+n(k)$. Il termine $i(k)$ è il **motivo del BER floor**: a basso $E_b/N_0$ domina il rumore, ad alto domina $i(k)$, che non diminuisce aumentando la potenza.

### Progetto del segnale a ISI nulla: criterio di Nyquist

#### Slide 14 e appunti — Signal design per ISI nulla (1/2) · [[signaling_bandlimited_channel.pdf#page=14|p. 14]] · appunti del 19/11 [[signaling_bandlimited_channel (19-11).pdf#page=15|p. 15]]
- Problema: costruire l'impulso complessivo $p(t)$ dell'intero sistema in modo che il ricevitore possa ricostruire esattamente la sequenza di dati in ingresso al trasmettitore. La segnalazione sul canale a banda limitata diventa senza distorsione: è un **problema di progetto del segnale**.
- Gli impulsi sovrapposti si configurano in modo che all'uscita del ricevitore non interferiscano tra loro negli istanti di campionamento $t_k=kT$.
- In tal caso la rivelazione simbolo per simbolo, ottima in AWGN, resta ottima anche sul canale a banda limitata.
- Appunti: posso costruire $g(t)$ e $c(t)$ in modo che il contributo dell'ISI sia annullato ⇒ si ottiene il teorema di Nyquist.

> **Approcci per il trattamento dell'ISI** (appunti)
> - **Algoritmo di Viterbi**: sceglie la sequenza di simboli più verosimile (MLSE) percorrendo un traliccio, senza provare tutte le sequenze possibili.
> - **Equalizzatori**: filtri al ricevitore che compensano la distorsione del canale e riducono l'ISI residua (lineari ZF e MMSE, oppure DFE).
> - **OFDM**: divide la banda in molte sottoportanti strette, ognuna vista come un canale piatto; i simboli diventano lunghi e l'ISI trascurabile.
>
> 🧩 Le descrizioni sono mie: Viterbi ed equalizzatori si vedono alla fine di questa lezione, l'OFDM nelle slide non c'è ancora.

#### Slide 15 — Signal design per ISI nulla (2/2) · [[signaling_bandlimited_channel.pdf#page=15|p. 15]]
- Il criterio usato nel progetto del ricevitore è l'eliminazione dell'ISI dalla sequenza campionata $y(t_k)$. Il **criterio di Nyquist** richiede

$$p(kT-nT)=\begin{cases}1&n=k\\0&n\neq k\end{cases}\tag{4}$$

- Un impulso che soddisfa la (4) si chiama **impulso di Nyquist**. Non è unico: molte forme d'impulso soddisfano il criterio.

#### Slide 16 — Il criterio nel dominio della frequenza (1/2) · [[signaling_bandlimited_channel.pdf#page=16|p. 16]]
- Il titolo di questa slide e della successiva è «impulso di Nyquist ideale per la trasmissione dati **in banda base** senza distorsione».
- Treno periodico di delta distanti $T$:

$$\Delta_T(t)\triangleq\sum_{m=-\infty}^{+\infty}\delta(t-mT)\tag{5}$$

- La (4) equivale a $p(t)\,\Delta_T(t)=\sum_mp(mT)\,\delta(t-mT)=\delta(t)$.
- Trasformando entrambi i membri (la trasformata del treno di delta è $\frac1T$ per un treno di delta distanti $1/T$ in frequenza):

$$R_s\sum_{k=-\infty}^{+\infty}P(f-kR_s)=1$$

  con $R_s=1/T$ symbol rate in simboli/s. (La slide dice «trasformando la (16)»: si riferisce all'uguaglianza appena scritta.)

#### Slide 17 — Il criterio nel dominio della frequenza (2/2) · [[signaling_bandlimited_channel.pdf#page=17|p. 17]]
- La condizione per ISI nulla in frequenza è

$$\sum_{k=-\infty}^{+\infty}P(f-kR_s)=T\tag{6}$$

- **Criterio di Nyquist per la trasmissione in banda base senza distorsione**, nel dominio della frequenza: $P(f)$ elimina l'ISI per campioni presi a intervalli $T$ se soddisfa la (6). $P(f)$ si riferisce all'intero sistema: filtro di trasmissione, canale e filtro di ricezione.

#### Slide 18–19 e appunti — Impulso di Nyquist ideale (1/4)–(2/4) · [[signaling_bandlimited_channel.pdf#page=18|p. 18]], [[signaling_bandlimited_channel.pdf#page=19|19]]
- Il modo più semplice di soddisfare la (6) è uno spettro rettangolare:

$$P(f)=T\,\text{rect}\Big(\frac{f}{1/T}\Big)\tag{7}$$

  La banda (monolatera) in banda base è $1/(2T)=R_s/2$: con la (7) non serve nessuna frequenza di valore assoluto maggiore di metà del symbol rate.
- $W_N\triangleq1/(2T)=R_s/2$ è la **banda di Nyquist**.
- La forma d'onda a ISI nulla è la sinc: $p(t)=\text{sinc}(2W_Nt)=\text{sinc}(t/T)$, detta **impulso di Nyquist ideale**, ideale perché la sua trasformata è nulla fuori dall'intervallo di Nyquist. Appunti: soddisfa il criterio di Nyquist con la minima occupazione di banda.
- Figura (slide 19), modulazione binaria ($T=T_b$, $R_s=R_b$, $W\equiv W_N$): (a) risposta in ampiezza ideale: in ordinata $2W\,P(f)$, che vale 1 per $|f|/W<1$ (cioè $P(f)=1/(2W)$), con $W=1/(2T_b)=R_b/2$; (b) impulso ideale $p(t)$ in funzione di $t/T_b$, con picco 1 in 0 e zeri in $t=\pm T_b,\pm2T_b,\dots$; sotto, gli istanti di campionamento e gli intervalli di segnalazione lunghi $T_b$.

> 🧩 **Perché la banda minima è proprio $W_N=\frac1{2T}=\frac{R_s}2$** (spiegazione mia, dalla (6))
> - La (6) chiede che le repliche $P(f-kR_s)$, **distanti $R_s=1/T$**, sommate diano la costante $T$ a **ogni** frequenza.
> - Se $P(f)$ è nullo per $\lvert f\rvert>W$, ogni replica occupa un intervallo largo $2W$. Tre casi:
>   - $2W<\frac1T$: tra una replica e la successiva restano frequenze dove tutte valgono 0, quindi lì la somma è 0 e non $T$. Nessuna forma di $P(f)$ dà ISI nulla: la banda è **troppo stretta**;
>   - $2W=\frac1T$: le repliche si toccano bordo a bordo senza sovrapporsi, quindi in ogni punto ne lavora una sola, che deve valere $T$ da sola: l'unica soluzione è il rettangolo (7);
>   - $2W>\frac1T$: le repliche si sovrappongono e ci sono molte forme che sommano a $T$ (il coseno rialzato, più avanti).
> - Il confine è $2W=\frac1T$, cioè $W_N=\frac1{2T}$: la banda minima è **metà del symbol rate** (non del periodo).
> - Lettura con il campionamento (Lezione 2): il ricevitore campiona ogni $T$, cioè a frequenza $f_c=\frac1T$; il teorema del campionamento dice che un segnale è descritto dai suoi campioni se la sua banda è al più $f_c/2=\frac1{2T}$. Trasmettere vuol dire costruire un segnale continuo i cui campioni sono i simboli: per farlo basta, e serve, la banda $\frac1{2T}$.
> - Lettura con i gradi di libertà (Lezione 12): un segnale di banda $W$ e durata $T_0$ ha $2WT_0$ dimensioni reali, cioè porta al più $2W$ valori indipendenti al secondo; per $\frac1T$ simboli al secondo serve $2W\ge\frac1T$.
> - Esempio: la sequenza più «veloce», $+1,-1,+1,-1,\dots$, è un'oscillazione di periodo $2T$, cioè di frequenza $\frac1{2T}$: nessuna sequenza chiede frequenze più alte.

#### Slide 20–21 — Impulso di Nyquist ideale (3/4)–(4/4) · [[signaling_bandlimited_channel.pdf#page=20|p. 20]], [[signaling_bandlimited_channel.pdf#page=21|21]]
- $p(t)$ è la risposta impulsiva di un **filtro passa-basso** ideale con risposta in ampiezza $1/(2W_N)$ nella sua banda passante (*passband*, le frequenze che lascia passare: $|f|<W_N$) e banda $W_N$.
- $p(t)$ ha il picco nell'origine e si annulla nei multipli interi di $T$: se $y(t)$ è campionato in $t=0,\pm T,\pm2T,\dots$, gli impulsi $s(n)\,p(t-nT)$ non interferiscono tra loro.
- Figura (slide 21): modulazione binaria, somma di sinc per la sequenza di bit 1011010; in ogni istante di campionamento conta solo l'impulso centrato lì.

#### Slide 22 — Difficoltà pratiche (1/3) · [[signaling_bandlimited_channel.pdf#page=22|p. 22]]
- L'impulso di Nyquist ideale è economico in banda (ISI nulla con la minima banda possibile), ma ha due difficoltà pratiche:
  - richiede $|P(f)|$ piatto da $-W_N$ a $+W_N$ e nullo altrove: è **fisicamente irrealizzabile** (non causale), perché le transizioni brusche a $\pm W_N$ violano il **criterio di Paley-Wiener**;
  - $p(t)$ decresce come $1/|t|$ per $|t|$ grande: decadimento lento, dovuto anch'esso alla discontinuità di $P(f)$ in $\pm W_N$. Non c'è praticamente margine d'errore sugli istanti di campionamento.

#### Slide 23–24 — Difficoltà pratiche (2/3)–(3/3): errore di timing · [[signaling_bandlimited_channel.pdf#page=23|p. 23]], [[signaling_bandlimited_channel.pdf#page=24|24]]
- Si campiona in $t_k=kT+\Delta t$, con $\Delta t$ errore di timing; ci si concentra sull'intervallo di simbolo $[0,T)$, cioè $k=0$, e senza rumore:

$$y(t_0)=y(\Delta t)=\sum_{n=-\infty}^{+\infty}s(n)\,p(\Delta t-nT)\tag{8}$$

$$y(\Delta t)=\sum_{n=-\infty}^{+\infty}s(n)\,\text{sinc}\Big(\frac{\Delta t-nT}{T}\Big)\tag{9}$$

- Separando il termine $n=0$:

$$y(\Delta t)=s(0)\,\text{sinc}\Big(\frac{\Delta t}{T}\Big)+\sum_{n\neq0}s(n)\,\text{sinc}\Big(\frac{\Delta t-nT}{T}\Big)$$

  Il primo termine è il simbolo desiderato, la serie è l'ISI causata da $\Delta t$. La serie **può divergere**, causando decisioni errate.

### Lo spettro a coseno rialzato

#### Slide 25 — Raised cosine (1/5) · [[signaling_bandlimited_channel.pdf#page=25|p. 25]]
- Si superano le difficoltà estendendo la banda dal minimo $W_N=R_s/2=1/(2T)$ a un valore regolabile tra $W_N$ e $2W_N$.
- Un decadimento più rapido nel tempo implica un decadimento più lento in frequenza ⇒ serve **banda in eccesso** oltre il minimo di Nyquist: si scambia banda per un progetto più robusto agli errori di timing.
- Si impone a $P(f)$ una condizione più stringente di quella dell'impulso ideale:

$$P(f)+P\Big(f-\frac1T\Big)+P\Big(f+\frac1T\Big)=T,\qquad f\in\Big(-\frac1{2T},\frac1{2T}\Big)\tag{10}$$

#### Slide 26–27 — Raised cosine (2/5)–(3/5) · [[signaling_bandlimited_channel.pdf#page=26|p. 26]], [[signaling_bandlimited_channel.pdf#page=27|27]]
- Una forma con molte proprietà desiderabili è lo **spettro a coseno rialzato**: una parte piatta e una parte di roll-off sinusoidale,

$$P(f)=\begin{cases}T,&|f|\le\dfrac{1-\alpha}{2T}\\[2mm]\dfrac T2\Big[1-\sin\Big(\big(|f|-\tfrac1{2T}\big)\dfrac{\pi T}{\alpha}\Big)\Big],&\dfrac{1-\alpha}{2T}\le|f|<\dfrac{1+\alpha}{2T}\\[2mm]0,&|f|\ge\dfrac{1+\alpha}{2T}\end{cases}$$

- $\alpha\in[0,1]$ è il **fattore di roll-off**: indica la banda in eccesso rispetto alla soluzione ideale $W_N=1/(2T)$. La nuova banda di trasmissione (monolatera) è $W_N(1+\alpha)$.
- Antitrasformando:

$$p(t)=\text{sinc}\Big(\frac tT\Big)\,\frac{\cos(\pi\alpha t/T)}{1-(2\alpha t/T)^2}$$

#### Slide 28–29 — Raised cosine (4/5)–(5/5) · [[signaling_bandlimited_channel.pdf#page=28|p. 28]], [[signaling_bandlimited_channel.pdf#page=29|29]]
- Figura (slide 28), modulazione binaria ($T=T_b$): (a) risposta in frequenza e (b) risposta impulsiva per diversi roll-off.
- $p(t)$ è il prodotto di due fattori: $\text{sinc}(t/T)$, che garantisce gli zeri negli istanti $t=kT$, e un secondo fattore che decresce come $1/|t|^2$ per $|t|$ grande e riduce molto le code rispetto all'impulso ideale: la trasmissione diventa relativamente insensibile agli errori di campionamento.
- Queste due proprietà sono molto utili per estrarre dal segnale ricevuto l'informazione di timing ai fini della sincronizzazione. Il prezzo è una banda maggiore di quella del canale di Nyquist ideale ($\alpha=0$).

#### Slide 30 — Osservazioni: impulso a radice di Nyquist · [[signaling_bandlimited_channel.pdf#page=30|p. 30]]
- Il criterio di Nyquist riguarda la cascata di filtro di trasmissione, canale e filtro di ricezione; ma il canale di solito non è sotto controllo.
- In pratica si progettano trasmettitore e ricevitore in modo che $G(f)\,C(f)$ sia di Nyquist, e l'ISI introdotta dal canale si tratta a parte.
- Scelta tipica: $G(f)$ e $C(f)$ radici quadrate (in frequenza) di un impulso di Nyquist: **impulso a radice di Nyquist** (square root Nyquist).

#### Slide 31 — Efficienza di banda con ISI nulla · [[signaling_bandlimited_channel.pdf#page=31|p. 31]]
- In assenza di ISI l'efficienza di banda è $\eta_B=R_b/W$ (bit/s/Hz): $\eta_B=2\log_2M$ per modulazione lineare monodimensionale, $\eta_B=\log_2M$ per bidimensionale (Lezione 12).
- Noti $R_b$ ed $\eta_B$, la banda (monolatera) minima richiesta in assenza di ISI è $W=R_b/\eta_B$; in presenza di ISI, dice la slide, questa banda si espande della banda in eccesso, e la banda effettiva è

$$W_{actual}=(1+\alpha)\,\frac{R_b}{\eta_B}$$

### Equalizzazione

#### Slide 32 — Problemi nel soddisfare la condizione di ISI nulla · [[signaling_bandlimited_channel.pdf#page=32|p. 32]]
- Progettare il sistema con il criterio di Nyquist ha tre limiti pratici:
  - la risposta $h(t)$ del canale deve essere nota al trasmettitore, per fare in modo che $g(t)\ast h(t)\ast c(t)$ sia un coseno rialzato; in molti scenari non sono disponibili stime affidabili di $h(t)$ al trasmettitore;
  - i filtri di trasmissione e ricezione vanno progettati sulla risposta del canale, cosa irragionevole in ambienti tempo-varianti;
  - in pratica si può rinunciare alla condizione di ISI nulla ⇒ serve un **equalizzatore** al ricevitore.
- Si chiama **equalizzazione** qualunque tecnica di elaborazione o filtraggio progettata per eliminare o ridurre l'ISI.

#### Slide 33–34 — Tipi di equalizzatori · [[signaling_bandlimited_channel.pdf#page=33|p. 33]], [[signaling_bandlimited_channel.pdf#page=34|34]]
- L'equalizzazione si divide in **lineare** e **non lineare**.
- Le tecniche lineari, come **zero-forcing (ZF)** e **minimum mean-square error (MMSE)**, sono le più semplici da realizzare e da capire, ma in genere soffrono di più **amplificazione del rumore**.
- Tra le non lineari la più comune è la **decision-feedback equalization (DFE)**, abbastanza semplice e di solito efficace; su canali a basso SNR soffre di **propagazione degli errori** quando i bit sono decisi in modo errato.
- La tecnica ottima è la **maximum likelihood sequence estimation (MLSE)**, la cui complessità cresce esponenzialmente con la memoria del canale: è impraticabile sulla maggior parte dei canali d'interesse.
- Figura (slide 34): albero degli equalizzatori. Tipi: lineari e non lineari (DFE, MLSE). Strutture: transversal e lattice (lineari e DFE), transversal channel estimator (MLSE). Algoritmi di aggiornamento dei coefficienti: LMS, RLS, Fast RLS, Square-Root LS (strutture transversal), Gradient RLS (lattice).

### Stima di sequenza a massima verosimiglianza

#### Slide 35 — MLSE (1/2) · [[signaling_bandlimited_channel.pdf#page=35|p. 35]]
- La MLSE evita l'amplificazione del rumore perché non usa un filtro equalizzatore: stima la **sequenza** dei simboli trasmessi.
- Inviluppo trasmesso $u(t)=\sum_ns(n)\,g(t-nT)$; uscita del canale senza rumore

$$y(t)=\sum_ns(n)\,q(t-nT)\tag{11}$$

  con $q(t)=g(t)\ast h(t)$, risposta combinata di sagomatura e canale.
- In pratica $q(t)$ è causale e a memoria finita: $q(t)\equiv0$ per $t\notin[0,LT]$, con $L$ memoria del canale in intervalli di simbolo.

#### Slide 36 — MLSE (2/2) · [[signaling_bandlimited_channel.pdf#page=36|p. 36]]
- Noto $q(t)$, la MLSE sceglie la sequenza di simboli che massimizza la verosimiglianza del segnale ricevuto.
- Lavora su trasmissioni successive viste come un unico «simbolo a blocco»: per un messaggio di $K+1$ simboli di una costellazione di cardinalità $M$ bisogna scegliere tra $M^{K+1}$ messaggi. Con la forza bruta, 1000 simboli QPSK richiedono una complessità $4^{1000}$.
- Si considera il blocco $\mathbf s=[s(0),s(1),\dots,s(K)]^T$ trasmesso per $t\in[0,KT]$.

#### Slide 37 — Il criterio MLSE (1/3) · [[signaling_bandlimited_channel.pdf#page=37|p. 37]]
- Il logaritmo del rapporto di verosimiglianza (*log-likelihood ratio*) della sequenza $\mathbf s$ è (vedi la rivelazione)

$$\lambda(y)=\text{Re}\big(\langle r(t),y(t)\rangle\big)-\frac12\lVert y(t)\rVert^2\tag{12}$$

$$\lambda(y)=\text{Re}\Big(\int_{\mathcal T}r(t)\,y^\ast(t)\,dt\Big)-\frac12\int_{\mathcal T}|y(t)|^2dt\tag{13}$$

  con $r(t)=y(t)+w(t)$, $w(t)$ rumore gaussiano additivo di PSD $\sigma^2$, e $y(t)=\sum_{n=0}^Ks(n)\,q(t-nT)$ forma d'onda senza rumore associata a $\mathbf s$.
- L'intervallo d'osservazione $\mathcal T$ è abbastanza lungo da contenere per intero $q(t),q(t-T),\dots,q(t-KT)$.

#### Slide 38 — Il criterio MLSE (2/3) · [[signaling_bandlimited_channel.pdf#page=38|p. 38]]
- Sostituendo $y(t)$:

$$\lambda(y)=\sum_{n=0}^K\text{Re}\Big(s^\ast(n)\int_{\mathcal T}r(t)\,q^\ast(t-nT)\,dt\Big)-\frac12\sum_{n=0}^K\sum_{m=0}^Ks(n)\,s^\ast(m)\int_{\mathcal T}q(t-nT)\,q^\ast(t-mT)\,dt\tag{14}$$

- Si definiscono

$$\alpha(n)\triangleq\int_{\mathcal T}r(t)\,q^\ast(t-nT)\,dt,\qquad\beta_{m,n}\triangleq\int_{\mathcal T}q(t-nT)\,q^\ast(t-mT)\,dt$$

#### Slide 39 — Il criterio MLSE (3/3) · [[signaling_bandlimited_channel.pdf#page=39|p. 39]]
- $\alpha(n)$ si ottiene passando $r(t)$ in un filtro adattato di risposta $q^\ast(-t)$ e campionandone l'uscita in $t_n=nT$.
- $\beta_{m,n}$ dipende da $m$ e $n$ separatamente, ma con $\mathcal T$ abbastanza lungo $\beta_{m,n}=\beta_{m-n}$.
- La regola MLSE è

$$\hat{\mathbf s}=\arg\max_{\mathbf s}\Big\{\text{Re}\Big[\sum_{n=0}^Ks^\ast(n)\,\alpha(n)\Big]-\frac12\sum_{n=0}^K\sum_{m=0}^Ks(n)\,s^\ast(m)\,\beta(n-m)\Big\}$$

- La complessità cresce esponenzialmente con il numero di simboli trasmessi. L'**algoritmo di Viterbi** la riduce: diventa esponenziale nella memoria del canale ma lineare nel numero (di solito molto maggiore) di simboli.

#### Slide 40 — Il rivelatore di sequenza ML · [[signaling_bandlimited_channel.pdf#page=40|p. 40]]
- Per la regola MLSE serve prima la sequenza $\alpha(n)$, uscita di un unico filtro adattato.
- Poi bisogna massimizzare $\lambda(y)\triangleq\text{Re}\big[\sum_ns^\ast(n)\alpha(n)\big]-\frac12\sum_n\sum_ms(n)s^\ast(m)\beta(n-m)$ su tutte le sequenze: il filtro adattato è seguito da un processore, il **rivelatore di sequenza ML**, che sceglie tra le $M^{K+1}$ sequenze quella che massimizza $\lambda(y)$.
- L'algoritmo di Viterbi fa questa scelta in modo efficiente: si applica ai problemi di massimo (o minimo) formulabili come ricerca del cammino di lunghezza massima (o minima) in un traliccio finito.

### L'algoritmo di Viterbi

#### Slide 41 — Algoritmo di Viterbi (1/2) · [[signaling_bandlimited_channel.pdf#page=41|p. 41]]
- L'algoritmo di Viterbi (VA) cerca, tra i cammini che attraversano un **traliccio** (trellis) da sinistra a destra, quello di metrica massima o minima.
- Figura: traliccio con stati $\{S_i\}_{i=1}^{N_\sigma}$, $N_\sigma=4$, e profondità $K=6$ (da $k=0$ a $k=K$).
- A ogni ramo è associata una **metrica di ramo** (etichetta). Le metriche sono **additive**: la metrica di due rami adiacenti è la somma delle due.

#### Slide 42 — Algoritmo di Viterbi (2/2) · [[signaling_bandlimited_channel.pdf#page=42|p. 42]]
- La metrica totale di un cammino è la somma delle etichette dei suoi rami; si cerca il cammino di metrica totale massima (o minima).
- Con $\sigma_k$ stato al tempo $k$ (valori in $\{S_i\}_{i=1}^{N_\sigma}$) e $m(\sigma_k,\sigma_{k+1})$ metrica del ramo $\sigma_k\to\sigma_{k+1}$, si massimizza (o minimizza)

$$\lambda(\sigma_0,\sigma_1,\dots,\sigma_K)\triangleq\sum_{k=0}^{K-1}m(\sigma_k,\sigma_{k+1})$$

  su tutte le $(\sigma_0,\dots,\sigma_K)$.
- Forza bruta: si valutano tutti i valori possibili e si sceglie il massimo: complessità alta (esponenziale in $K$) e ritardo di decisione alto (si decide solo dopo aver calcolato tutta la sequenza, ritardo $K$).

#### Slide 43–44 — I passi chiave: add, compare, select · [[signaling_bandlimited_channel.pdf#page=43|p. 43]], [[signaling_bandlimited_channel.pdf#page=44|44]]
- Il VA riduce molto la complessità, che diventa **lineare in $K$**. Una versione detta **VA troncato** permette ritardi molto minori di $K$.
- I passi chiave sono **Add, Compare, Select (ACS)**. Per ogni stato $\sigma_{k+1}$:
  - **add**: somma la metrica accumulata nello stato $\sigma_k$ e la metrica del ramo;
  - **compare**: confronta queste somme;
  - **select**: tiene il ramo con il valore massimo (o minimo), il **sopravvissuto**, e scarta tutti gli altri rami entranti in $\sigma_{k+1}$.
- Ogni passo ACS si ripete dallo stato iniziale a quello finale del traliccio. Figura (slide 44): esempio di applicazione, con il traliccio etichettato e i sopravvissuti passo per passo da $k=1$ a $k=6$, dove resta un solo cammino.

#### Slide 45 — Il VA applicato alla MLSE (1/3) · [[signaling_bandlimited_channel.pdf#page=45|p. 45]]
- Si riscrive $\lambda(y)$ separando i termini con l'ultimo simbolo $s(K)$:

$$\lambda(y)=\text{Re}\Big[\sum_{n=0}^{K-1}s^\ast(n)\alpha(n)\Big]-\frac12\sum_{n=0}^{K-1}\sum_{m=0}^{K-1}s(n)s^\ast(m)\beta(n-m)+\text{Re}[s^\ast(K)\alpha(K)]-\text{Re}\Big[s(K)\sum_{n=0}^{K-1}s^\ast(n)\beta(K-n)\Big]+|s(K)|^2\beta(0)\tag{15}$$

- Poiché $q(t)\equiv0$ per $t\notin[0,LT]$, $\beta(\ell)\neq0$ solo per $\ell\in\{-L,\dots,L\}$, e la somma su $n$ dell'ultimo termine misto si restringe a $n=K-L,\dots,K-1$ (16).
- ⚠️ Nella (15)–(16) delle slide l'ultimo termine è $+|s(K)|^2\beta(0)$; separando il termine $n=m=K$ dalla doppia somma con il suo $-\frac12$ si ottiene $-\frac12|s(K)|^2\beta(0)$. Lo stesso vale per l'ultimo termine di $V_k$. La struttura della ricorsione non cambia.

#### Slide 46–47 — Il VA applicato alla MLSE (2/3)–(3/3) · [[signaling_bandlimited_channel.pdf#page=46|p. 46]], [[signaling_bandlimited_channel.pdf#page=47|47]]
- Si definiscono lo **stato** $\sigma_\ell\triangleq(s(\ell-1),s(\ell-2),\dots,s(\ell-L))$, $\ell=L,\dots,K$, e

$$U_k(\sigma_L,\dots,\sigma_k)\triangleq\text{Re}\Big[\sum_{\ell=0}^ks^\ast(\ell)\alpha(\ell)\Big]-\frac12\sum_{\ell=0}^k\sum_{m=0}^ks(\ell)s^\ast(m)\beta(\ell-m)$$

$$V_k(\sigma_{k-1},\sigma_k)\triangleq\text{Re}[s^\ast(k)\alpha(k)]-\text{Re}\Big[s(k)\sum_{m=k-L}^{k-1}s^\ast(m)\beta(k-m)\Big]+|s(k)|^2\beta(0)$$

  per $k=L,\dots,K$.
- Poiché $\lambda(y)=U_K(\sigma_L,\dots,\sigma_K)$, la (16) diventa la ricorsione $U_K=U_{K-1}(\sigma_L,\dots,\sigma_{K-1})+V_K(\sigma_{K-1},\sigma_K)$, e ripetendo

$$\lambda(y)=U_L(\sigma_L)+V_{L+1}(\sigma_L,\sigma_{L+1})+V_{L+2}(\sigma_{L+1},\sigma_{L+2})+\dots+V_K(\sigma_{K-1},\sigma_K)$$

- Questa scomposizione si presta al VA: ogni $\sigma_\ell$ è uno stato del traliccio e $V_{\ell+1}(\sigma_\ell,\sigma_{\ell+1})$ è la metrica (etichetta) del ramo tra $\sigma_\ell$ e $\sigma_{\ell+1}$. La MLSE diventa la ricerca del cammino di metrica massima nel traliccio.

---

*Approfondimenti nel wiki (derivazioni passo per passo, grafici, esempio di Viterbi svolto): [[interferenza-intersimbolica]], [[criterio-di-nyquist]], [[equalizzazione]], [[algoritmo-di-viterbi]].*
