# Corso completo — Trasmissione dei Segnali Digitali

> Tutto il wiki in un unico file, lezione per lezione e argomento per argomento, nell'ordine di [[lezioni]]. **File generato** da `output/genera_compendio.py` il 2026-10-12: non modificarlo a mano, modifica le pagine e rilancia lo script. Ogni argomento rimanda alla sua pagina con il link «pagina».

## Indice

- [[#Lezione 1 — Introduzione al corso]]
- [[#Lezione 2 — Elementi di teoria della probabilità]]
- [[#Lezione 3 — Campionamento e conversione A/D e D/A]]
- [[#Lezione 4 — Rappresentazione complessa in banda base]]
- [[#Lezione 5 — Processi aleatori]]
- [[#Lezione 6 — Laboratorio Matlab: conversione A/D e D/A (28/09)]]

---

## Lezione 1 — Introduzione al corso

### Introduzione al corso — Intro.pdf · [[intro-corso|pagina]]

#### Sommario · [[Intro.pdf#page=1|p. 1]]–[[Intro.pdf#page=3|3]]

Slide introduttive (in inglese, eccetto le prime tre) del corso *Trasmissione dei segnali digitali*, LM Ingegneria Informatica, Università di Napoli Federico II, a.a. 2026-27, docente Donatella Darsena. Contengono l'organizzazione (testo: Madhow, *Fundamentals of Digital Communication*; esame solo **orale**) e il **programma** in sei macro-argomenti. Il resto motiva la comunicazione digitale: il processo di comunicazione, i tre elementi (trasmettitore, canale, ricevitore), i vantaggi del digitale (soprattutto la rigenerazione degli impulsi) e lo schema a blocchi completo, descritto blocco per blocco. Si chiude con i vantaggi dell'approccio digitale e il principio di separazione tra codifica di sorgente e di canale. Il materiale è qualitativo: nessuna formula.

#### Punti chiave · [[Intro.pdf#page=2|p. 2]]–[[Intro.pdf#page=4|4]], [[Intro.pdf#page=6|p. 6]], [[Intro.pdf#page=9|p. 9]], [[Intro.pdf#page=10|10]], [[Intro.pdf#page=12|p. 12]], [[Intro.pdf#page=14|p. 14]], [[Intro.pdf#page=15|15]], [[Intro.pdf#page=18|p. 18]], [[Intro.pdf#page=19|19]], [[Intro.pdf#page=21|p. 21]]

1. **Programma del corso**:
   - rappresentazione complessa in banda base dei segnali;
   - processi aleatori;
   - modulazione digitale;
   - stima dei parametri e sincronizzazione;
   - comunicazione su canali selettivi in frequenza;
   - teoria dell'informazione e codifica di canale.
2. Esame: colloquio orale; testo di riferimento Madhow (Cambridge, 2008) più appunti.
3. Comunicazione = trasferimento di informazione nello spazio (trasmissione) o nel tempo (memorizzazione).
4. Tre elementi base: trasmettitore, canale, ricevitore; transceiver = TX + RX.
5. Il processo di comunicazione è **statistico**.
6. Vantaggio principale del digitale: la **rigenerazione** con ripetitori rigenerativi.
7. Schema a blocchi: codificatore di sorgente → codificatore di canale → modulatore → canale → demodulatore → decodificatore di canale → decodificatore di sorgente.
8. Bit rate tipici: voce 64 kbit/s, MP3 128 kbit/s, audio da studio ~10×.
9. Il demodulatore deve **sincronizzarsi** (fase, frequenza, tempo), eventualmente **equalizzare**, e **decidere**.
10. Rumore termico: moto casuale degli elettroni nei conduttori.
11. Principio di separazione sorgente/canale: ottimo per collegamenti punto-punto; la codifica congiunta a volte è migliore; comunicazioni semantiche come tema emergente.

#### Concetti introdotti

- [[sistema-comunicazione-digitale]]
- [[ripetitore-rigenerativo]]
- [[conversione-ad-da]] (citata come compito del codificatore di sorgente)

#### Figure estratte · [[Intro.pdf#page=7|p. 7]], [[Intro.pdf#page=11|p. 11]], [[Intro.pdf#page=14|p. 14]]

- ![[intro-p7-elementi-sistema-comunicazione.png]]
- ![[intro-p11-degradazione-impulso.png]]
- ![[intro-p14-schema-sistema-digitale.png]]

#### Domande aperte · [[Intro.pdf#page=21|p. 21]]

- Rumore termico: le slide non danno il modello quantitativo (densità spettrale $kT$, gaussianità). Nemmeno le slide sui processi aleatori ([[processi-aleatori]]) lo danno: lo citano solo come esempio. TODO.
- Perché il principio di separazione è ottimo **solo** punto-punto? Rimandato alla parte di teoria dell'informazione.
- In quali casi concreti la codifica congiunta sorgente-canale batte la separazione?

#### Domande da esame

- Descrivere lo schema a blocchi di un sistema di comunicazione digitale e la funzione di ogni blocco.
- Perché i sistemi di comunicazione "diventano digitali"? Cos'è un ripetitore rigenerativo?
- Quali compiti svolge il demodulatore?
- Cosa dice il principio di separazione e quali vantaggi porta?
- Perché il processo di comunicazione è di natura statistica?

### Sistema di comunicazione digitale · [[sistema-comunicazione-digitale|pagina]]

#### Definizione · [[Intro.pdf#page=4|p. 4]], [[Intro.pdf#page=6|p. 6]], [[Intro.pdf#page=10|p. 10]]

**Comunicazione**: trasferimento di informazione (voce, audio, video, file, pagine web...) tra punti diversi dello **spazio** (trasmissione) o del **tempo** (memorizzazione).

Ogni sistema di comunicazione, qualunque sia la sua forma, ha tre elementi base — p. 6:
- **trasmettitore** — converte il segnale messaggio in una forma adatta al canale;
- **canale** — mezzo fisico che collega trasmettitore e ricevitore;
- **ricevitore** — ricostruisce dal segnale ricevuto una forma riconoscibile del messaggio originale.

La cascata trasmettitore + ricevitore si chiama anche **transceiver**.

Un sistema è **digitale** quando l'informazione trasferita è rappresentata in forma digitale (di solito cifre binarie, *bit*); è **analogico** quando l'informazione assume un continuo di valori.

#### Formule · [[Intro.pdf#page=15|p. 15]]

Il materiale di Intro è qualitativo: nessuna formula. Unici valori numerici (bit rate tipici di sorgente):

| Applicazione | Bit rate |
|---|---|
| Telefonia fissa convenzionale (voce) | 64 kbit/s |
| Lettori MP3 consumer | 128 kbit/s (tipico) |
| Audio digitale professionale da studio | ≈ 10 × 128 kbit/s ≈ 1.28 Mbit/s |

> 🧩 Derivazione mia: la terza riga è "circa dieci volte" il valore MP3, come dice la slide, non un dato esplicito.

#### Derivazioni · [[Campionamento_AD_DA.pdf#page=16|p. 16]]

Nessun risultato numerico da espandere nella fonte. Il collegamento quantitativo con il bit rate da 64 kbit/s è in [[campionamento-e-aliasing]] e [[dimensionamento-quantizzatore]].

> 💡 Connessione: 64 kbit/s = 8 kHz × 8 bit/campione. La frequenza di campionamento di 8 kHz per la voce è in p. 16 (banda 4 kHz → $f_c \ge 8$ kHz, vedi [[teorema-del-campionamento]]).
> 📚 Fonte esterna: gli 8 bit/campione sono della raccomandazione ITU-T G.711 (vedi [[g711]]); le slide non riportano questo valore.

#### Spiegazione

##### Processo di comunicazione · [[Intro.pdf#page=5|p. 5]], [[Intro.pdf#page=7|p. 7]]–[[Intro.pdf#page=9|9]]

Passi logici del processo:
1. generazione del segnale messaggio (voce, musica, immagine, dati);
2. descrizione del messaggio con una certa precisione tramite un insieme di simboli;
3. codifica dei simboli in forma adatta al mezzo fisico;
4. trasmissione dei simboli codificati;
5. decodifica e riproduzione dei simboli originali;
6. ricreazione del messaggio con una degradazione definibile, dovuta a imperfezioni inevitabili.

Il segnale si distorce propagandosi nel canale; in più al ricevitore si sommano **rumore** e **interferenze**. Il segnale ricevuto è quindi una versione corrotta di quello trasmesso.

> 🎯 Esame: «Il processo di comunicazione, in ogni sistema, è di natura **statistica**». Per questo nel corso servono la [[spazio-di-probabilita|teoria della probabilità]] e i processi aleatori.

![[intro-p7-elementi-sistema-comunicazione.png]]
*Sorgente → trasmettitore → canale → ricevitore → utente*

##### Schema a blocchi del sistema digitale · [[Intro.pdf#page=3|p. 3]], [[Intro.pdf#page=14|p. 14]]–[[Intro.pdf#page=17|17]], [[Intro.pdf#page=19|p. 19]], [[Intro.pdf#page=20|20]]

![[intro-p14-schema-sistema-digitale.png]]

| Blocco | Funzione |
|---|---|
| **Codificatore di sorgente** | Conversione A/D (per sorgenti analogiche) e riduzione della ridondanza, secondo i requisiti dell'utente finale |
| **Codificatore di canale** | Introduce ridondanza **controllata** contro gli errori del canale; produce una *parola di codice* |
| **Modulatore** | Traduce simboli (di messaggio o di canale) in forme d'onda analogiche trasmissibili |
| **Canale** | Distorce la forma d'onda: LTI (risposta impulsiva) per i canali cablati; tempo-variante per il wireless mobile; interferenza di accesso multiplo nel wireless (mezzo broadcast) |
| **Demodulatore** | Sincronizzazione (sfasamenti di fase, frequenza, tempo; clock non sincronizzati a priori), eventuale equalizzazione, **decisione** sui simboli (*detection*) |
| **Decodificatore di canale** | Sfrutta la ridondanza per stimare i simboli d'informazione |
| **Decodificatore di sorgente** | Converte i bit stimati in un formato usabile dall'utente (non per forza quello originale, es. voce → testo) |

Codifica di canale: per applicazioni insensibili al ritardo si usa rivelazione d'errore + ritrasmissione; per applicazioni real-time si usa correzione d'errore.

Il blocco tratteggiato dello schema (codificatore di canale →... → decodificatore di canale) è la parte "trasmissiva" su cui si concentra il corso (programma: p. 3).

##### Rumore termico · Intro [[Intro.pdf#page=18|p. 18]] · Processi [[random_processes.pdf#page=2|p. 2]]

Il segnale ricevuto è corrotto dal **rumore termico** generato dai componenti elettronici. Un conduttore di resistenza $R$ (Ω) a temperatura sopra lo zero assoluto contiene elettroni liberi in moto casuale, che producono una tensione di rumore ai suoi capi. Il rumore è piccolo, ma diventa un problema quando viene amplificato da un ricevitore ad alto guadagno. Si caratterizza con la meccanica quantistica.

TODO: da espandere — la slide non dà formule (densità spettrale, $kT$). Le slide sui processi aleatori citano il rumore termico come esempio di segnale aleatorio ([[processo-aleatorio]]) e danno gli strumenti per descriverlo ([[densita-spettrale-di-potenza]], [[processo-gaussiano]]), ma non il suo modello quantitativo.

##### Perché "going digital" · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=12|p. 12]], [[Intro.pdf#page=13|13]]

- **Rigenerazione**: il vantaggio principale. Vedi [[ripetitore-rigenerativo]].
- **Basse probabilità d'errore** grazie a rivelazione e correzione d'errore, che non hanno equivalenti analogici.
- Circuiti digitali più **affidabili** ed **economici**; implementazione **flessibile** (microprocessori, switching digitale, LSI).
- *«A bit is a bit»*: dati, telegrafo, telefono e TV vengono trattati come segnali identici.
- Gestione a **pacchetti**; protezione da interferenza/jamming; crittografia e privacy.
- Gran parte del traffico è tra computer, che per natura sono terminazioni digitali.

##### Vantaggi dell'approccio digitale e principio di separazione · [[Intro.pdf#page=21|p. 21]]

- **Progetto indipendente dalla sorgente**: una volta ridotta in bit, l'informazione si memorizza o trasmette senza interpretarla, e sorgenti diverse condividono lo stesso mezzo.
- **Progetto ottimizzato per il canale**: codifica di canale e modulazione si ottimizzano per ogni collegamento. Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula**.

> 🎯 Esame: lo schema si basa sulla **separazione tra codifica di sorgente e di canale**. Il principio di separazione dà vantaggi pratici ed è **ottimo per collegamenti punto-punto** (risultato di teoria dell'informazione). In certi casi la *codifica congiunta sorgente-canale* dà prestazioni migliori.

**Comunicazioni semantiche** (tema emergente): invece di ricostruire fedelmente la sequenza di bit, si trasmette il *significato* della sorgente. La codifica semantica estrae le caratteristiche utili al compito che il ricevitore deve svolgere.

#### Perché importa · [[Intro.pdf#page=3|p. 3]]

È il quadro di riferimento di tutto il corso: ogni argomento del programma corrisponde a un blocco dello schema:
- rappresentazione complessa in banda base → come modulatore e demodulatore lavorano in banda base, con upconverter e downconverter verso il canale ([[inviluppo-complesso]], [[upconversion-e-downconversion]]);
- modulazione digitale → modulatore/demodulatore ([[modulazione-digitale]]);
- stima dei parametri e sincronizzazione → demodulatore;
- canali selettivi in frequenza → canale ed equalizzazione;
- teoria dell'informazione e codifica di canale → codificatore/decodificatore di canale;
- conversione A/D → codificatore di sorgente ([[teorema-del-campionamento]], [[quantizzazione-uniforme]]).

#### Connessioni · Intro [[Intro.pdf#page=9|p. 9]], [[Intro.pdf#page=15|p. 15]], [[Intro.pdf#page=16|16]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]

- [[conversione-ad-da]] — è la prima parte del codificatore di sorgente per sorgenti analogiche.
- [[spazio-di-probabilita]] — la natura statistica della comunicazione motiva lo studio della probabilità.
- [[ripetitore-rigenerativo]] — è il meccanismo concreto del vantaggio del digitale.
- [[snr-di-quantizzazione]] — la "degradazione definibile" del passo 6 ha, per la quantizzazione, una misura precisa.
- [[modulazione-digitale]] — il modulatore «traduce simboli in forme d'onda»; la lezione sulla banda base ne dà un primo esempio, la modulazione lineare binaria.
- [[inviluppo-complesso]] — modulatore e demodulatore lavorano sull'inviluppo complesso in banda base; il canale fisico, tra upconverter e downconverter, si vede come un unico canale in banda base.

#### Fonti · [[Intro.pdf#page=4|p. 4]], [[Intro.pdf#page=21|p. 21]]

- [[intro-corso]] — sommario della fonte

### Ripetitore rigenerativo · [[ripetitore-rigenerativo|pagina]]

#### Cos'è · [[Intro.pdf#page=11|p. 11]], [[Intro.pdf#page=12|12]]

Circuito posto a **intervalli regolari** lungo una linea di trasmissione digitale. Prima che l'impulso trasmesso diventi ambiguo, lo amplifica con un amplificatore digitale e ne recupera la forma ideale originale: l'impulso viene "rigenerato" (*reborn*).

![[intro-p11-degradazione-impulso.png]]
*Impulso binario lungo una linea: distorsione crescente con la distanza (1→4) e rigenerazione (5)*

La forma d'onda si degrada con la lunghezza della linea per due meccanismi:
1. **distorsione**: linee e circuiti hanno una funzione di trasferimento non ideale;
2. **rumore** elettrico e interferenze.

#### Come si usa nel corso · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=21|p. 21]]

È il motivo principale del passaggio al digitale. Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula** lungo il collegamento. Con un amplificatore analogico, invece, il rumore verrebbe amplificato insieme al segnale.

> 🧩 Derivazione mia: il confronto con l'amplificatore analogico è implicito nelle slide («similar procedures are not available with analog»), qui lo rendo esplicito.

#### Concetti correlati

- [[sistema-comunicazione-digitale]]

#### Fonti · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=12|p. 12]], [[Intro.pdf#page=21|p. 21]]

- [[intro-corso]]


---

## Lezione 2 — Elementi di teoria della probabilità

### Spazio di probabilità e assiomi di Kolmogorov · [[spazio-di-probabilita|pagina]]

#### Definizione · [[Probabilità.pdf#page=2|p. 2]], [[Probabilità.pdf#page=3|3]], [[Probabilità.pdf#page=5|p. 5]]

- **Esperimento aleatorio**: procedura con un insieme ben definito di risultati, il cui esito non si prevede a priori (moneta, dado, carta, lotto, roulette). Un risultato si indica con $\omega$.
- **Spazio campione** $\Omega$: insieme di tutti i possibili risultati.
- **Evento**: qualunque sottoinsieme $A \subseteq \Omega$.
- **Prova**: una singola ripetizione dell'esperimento, che restituisce un risultato $\omega \in \Omega$.
- **Spazio degli eventi** $\mathcal{S}$: collezione che contiene tutti gli eventi di interesse (spesso tutti i sottoinsiemi di $\Omega$, compresi $\Omega$ e $\emptyset$).
- **Probabilità**: legge $P: A \in \mathcal{S} \to P(A) \in [0,1]$ che misura il "grado di incertezza" del verificarsi di $A$.
- **Spazio di probabilità**: la tripla $(\Omega, \mathcal{S}, P)$.

Esempi di spazio campione:
- lancio di una moneta: $\Omega = \{T, C\}$;
- lancio di un dado: $\Omega = \{1,2,3,4,5,6\}$;
- arrivo di un cliente allo sportello tra le 9:00 e le 12:00: $\Omega = [0, 10800]$ s.

> 🧩 Derivazione mia: 3 h × 3600 s/h = 10800 s, quindi l'intervallo è corretto.

#### Formule · [[Probabilità.pdf#page=5|p. 5]], [[Probabilità.pdf#page=6|6]]

> 🧮 Formula chiave — **Assiomi di Kolmogorov**:
> I. $P(A) \ge 0$ (non negatività)
> II. $P(\Omega) = 1$ (normalizzazione)
> III. se $\{A_n\}_{n=1}^{\infty}$ sono mutuamente esclusivi ($A_i \cap A_j = \emptyset,\ \forall i \neq j$):
> $$P\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n) \quad \text{(numerabile additività)}$$

**Proprietà elementari**, con $A, B \in \mathcal{S}$ e $\bar A$ = complementare di $A$:

| # | Proprietà | Nome |
|---|---|---|
| 1 | $P(\emptyset) = 0$ | |
| 2 | $A \cap B = \emptyset \Rightarrow P(A \cup B) = P(A) + P(B)$ | finita additività |
| 3 | $P(\bar A) = 1 - P(A)$ | |
| 4 | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | |
| 5 | $P(A \cup B) \le P(A) + P(B)$ | disuguaglianza di Boole |
| 6 | $B \subseteq A \Rightarrow P(B) \le P(A)$ | monotonia |
| 7 | $P(B) \le 1$ | |

#### Derivazioni · [[Probabilità.pdf#page=6|p. 6]]

> 🧩 Derivazione mia: la slide dice che le proprietà «si possono dimostrare» dagli assiomi ma non mostra i passaggi.

##### Derivazione — Proprietà 1: $P(\emptyset)=0$
**Si parte da:** assioma III con $A_1 = \Omega$, $A_n = \emptyset$ per $n \ge 2$ (a due a due disgiunti, perché $\Omega \cap \emptyset = \emptyset$).
$$
\begin{aligned}
P(\Omega) &= P(\Omega \cup \emptyset \cup \emptyset \cup \dots) && \Omega \cup \emptyset = \Omega \\
&= P(\Omega) + \sum_{n=2}^{\infty} P(\emptyset) && \text{assioma III} \\
\Rightarrow \sum_{n=2}^{\infty} P(\emptyset) &= 0 && \text{sottraggo } P(\Omega)=1 \text{ (finito)} \\
\Rightarrow P(\emptyset) &= 0 && \text{somma di infiniti termini uguali} \ge 0 \text{ (assioma I)}
\end{aligned}
$$

##### Derivazione — Proprietà 2 (finita additività)
**Si parte da:** assioma III con $A_1 = A$, $A_2 = B$, $A_n = \emptyset$ per $n \ge 3$.
$$
\begin{aligned}
P(A \cup B) &= P(A) + P(B) + \sum_{n\ge3} P(\emptyset) && \text{assioma III} \\
&= P(A) + P(B) && \text{proprietà 1}
\end{aligned}
$$

##### Derivazione — Proprietà 3 (complementare)
$$
\begin{aligned}
1 = P(\Omega) &= P(A \cup \bar A) && \text{assioma II; } A \cup \bar A = \Omega \\
&= P(A) + P(\bar A) && \text{prop. 2, perché } A \cap \bar A = \emptyset \\
\Rightarrow P(\bar A) &= 1 - P(A)
\end{aligned}
$$

##### Derivazione — Proprietà 4 (unione di eventi qualsiasi)
**Idea:** scompongo in eventi disgiunti.
$$
\begin{aligned}
A \cup B &= A \cup (\bar A \cap B) && \text{unione disgiunta} \\
P(A \cup B) &= P(A) + P(\bar A B) && \text{prop. 2} \\
B &= (A \cap B) \cup (\bar A \cap B) && \text{unione disgiunta} \\
P(B) &= P(AB) + P(\bar A B) \Rightarrow P(\bar A B) = P(B) - P(AB) && \text{prop. 2} \\
P(A \cup B) &= P(A) + P(B) - P(AB) && \text{sostituisco}
\end{aligned}
$$

##### Derivazione — Proprietà 5 (Boole)
Dalla 4, visto che $P(AB) \ge 0$ (assioma I): $P(A\cup B) = P(A)+P(B)-P(AB) \le P(A)+P(B)$.

##### Derivazione — Proprietà 6 (monotonia)
$$
\begin{aligned}
B \subseteq A \Rightarrow A &= B \cup (A \cap \bar B) && \text{unione disgiunta} \\
P(A) &= P(B) + P(A \bar B) && \text{prop. 2} \\
&\ge P(B) && P(A\bar B) \ge 0 \text{ (assioma I)}
\end{aligned}
$$

##### Derivazione — Proprietà 7 · [[Probabilità.pdf#page=5|p. 5]]
$B \subseteq \Omega$, quindi per la prop. 6 $P(B) \le P(\Omega) = 1$.

**Sanity check:** tutte le proprietà danno valori in $[0,1]$, coerenti con la definizione di $P$.
**Ipotesi:** solo gli assiomi I–III; nessuna ipotesi su $\Omega$ (discreto o continuo).

#### Spiegazione

##### Terminologia sugli eventi · [[Probabilità.pdf#page=3|p. 3]], [[Probabilità.pdf#page=4|4]]

| Linguaggio | Insiemi |
|---|---|
| si verifica $A$ | $\omega \in A$ |
| non si verifica $A$ | $\omega \notin A \iff \omega \in \bar A$ |
| si verifica $A$ **o** $B$ | $\omega \in A \cup B$ |
| si verifica $A$ **e** $B$ | $\omega \in A \cap B$ (si scrive anche $AB$) |
| evento certo | $A = \Omega$ |
| evento impossibile | $A = \emptyset$ |
| evento elementare | $A = \{\omega\}$ |
| mutuamente esclusivi | $A \cap B = \emptyset$ |

**Esempio 1.4**: dado, risultato $\omega = 4$. Svolto in [[calcolo-probabilita-eventi]].

##### Interpretazione
La probabilità è una *funzione d'insieme*: prende eventi, non numeri. Gli assiomi sono il minimo indispensabile. Tutto il resto (proprietà 1–7, [[probabilita-condizionale]], [[probabilita-totale-e-bayes]]) ne discende.

#### Perché importa · [[Intro.pdf#page=9|p. 9]]

È la base formale per descrivere la natura statistica della comunicazione. La probabilità d'errore di un sistema digitale sarà la probabilità di un evento del tipo {simbolo deciso ≠ simbolo trasmesso}.

#### Connessioni

- [[probabilita-condizionale]] — raffina $P(A)$ con l'informazione che $B$ si è verificato.
- [[variabile-aleatoria]] — associa numeri ai risultati $\omega$ per lavorare con funzioni reali.
- [[quantizzazione-uniforme]] — la probabilità di sovraccarico $P_s$ è una probabilità di evento, maggiorata con Chebyshev.

#### Fonti · [[Probabilità.pdf#page=2|p. 2]], [[Probabilità.pdf#page=6|p. 6]]

- [[elementi-teoria-probabilita]]

### Probabilità condizionale, probabilità composta e indipendenza · [[probabilita-condizionale|pagina]]

#### Definizione · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=11|p. 11]]

Dati due eventi $A$ e $B$ di uno [[spazio-di-probabilita]] con $P(B) \neq 0$, la **probabilità condizionale di $A$ dato $B$** è

$$P(A|B) \triangleq \frac{P(AB)}{P(B)}, \qquad P(AB) \equiv P(A \cap B)$$

È un "raffinamento" di $P(A)$ che tiene conto dell'informazione "si è verificato $B$".

**Indipendenza** (statistica) di due eventi:
$$P(AB) = P(A)\,P(B)$$

#### Formule · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=9|p. 9]]–[[Probabilità.pdf#page=12|12]]

| Formula | Significato | Validità |
|---|---|---|
| $P(A\|B) = \dfrac{P(AB)}{P(B)}$ | condizionale | $P(B)\neq 0$ |
| $P(AB) = P(A\|B)P(B) = P(B\|A)P(A)$ | **legge della probabilità composta** | $P(A),P(B)\neq0$ |
| $P(A\|B,C) = \dfrac{P(ABC)}{P(BC)}$ | condizionamento su più eventi ($B\cap C$) | $P(BC)\neq 0$ |
| $P(A_1\cdots A_n) = P(A_1)P(A_2\|A_1)\cdots P(A_n\|A_1,\dots,A_{n-1})$ | **regola della catena** | condizionanti a prob. non nulla |
| $P(AB)=P(A)P(B)$ | indipendenza di due eventi | — |
| $P\left(\bigcap_{i\in I}A_i\right)=\prod_{i\in I}P(A_i)\ \forall I\subseteq\{1..n\}$ | indipendenza di $n$ eventi | — |

> 🧮 Formula chiave: $P(AB) = P(A|B)P(B)$ e regola della catena.

**Attrazione e repulsione**:
- $P(A|B) > P(A)$: $A$ è "attratto" da $B$;
- $P(A|B) < P(A)$: $A$ è "respinto" da $B$;
- $P(A|B) = P(A)$: $A$ è "indifferente" a $B$, cioè indipendente.

Esempio 2.2: con $A$={piove}, $P(A|\text{estate}) < P(A)$ e $P(A|\text{inverno}) > P(A)$.

#### Derivazioni

##### Derivazione — $P(\cdot|B)$ soddisfa gli assiomi di Kolmogorov · [[Probabilità.pdf#page=8|p. 8]]
> 🧩 Derivazione mia

$$
\begin{aligned}
\text{I: } P(A|B) &= \frac{P(AB)}{P(B)} \ge 0 && P(AB)\ge0,\ P(B)>0 \\
\text{II: } P(\Omega|B) &= \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1 && \Omega\cap B = B \\
\text{III: } P\Big(\textstyle\bigcup_n A_n \Big| B\Big) &= \frac{P\big(\bigcup_n (A_n \cap B)\big)}{P(B)} && \text{distributività di } \cap \\
&= \sum_n \frac{P(A_n B)}{P(B)} = \sum_n P(A_n|B) && A_nB \text{ disgiunti se lo sono gli } A_n
\end{aligned}
$$

Interpretazione 2: $P(\cdot|B)$ è una legge sul nuovo spazio campione $\Omega_B = B$, cioè la restrizione della legge originale a $B$, rinormalizzata di $1/P(B)$.

##### Derivazione — Caso $B \subseteq A$ · [[Probabilità.pdf#page=8|p. 8]]
$$
\begin{aligned}
P(A|B) &= \frac{P(AB)}{P(B)} = \frac{P(B)}{P(B)} = 1 && B\subseteq A \Rightarrow A\cap B = B \\
P(B|A) &= \frac{P(AB)}{P(A)} = \frac{P(B)}{P(A)} \ge P(B) && P(A) \le 1
\end{aligned}
$$
Da qui si vede che in generale $P(A|B) \neq P(B|A)$: i denominatori sono diversi.

##### Derivazione — Regola della catena per tre eventi · [[Probabilità.pdf#page=10|p. 10]]
$$
\begin{aligned}
P(ABC) &= P(A|B,C)\,P(BC) && \text{definizione di } P(A|B,C) \\
&= P(A|B,C)\,P(B|C)\,P(C) && \text{prob. composta su } P(BC)
\end{aligned}
$$
La successione logica è $C \to B \to A$. Scegliendo l'ordine $A\to B\to C$ si ottiene $P(ABC)=P(A)P(B|A)P(C|A,B)$. Le permutazioni dei 3 eventi sono $3! = 6$, quindi ci sono 6 scritture possibili. Per $n$ eventi si procede per induzione applicando la stessa idea a $P(A_1\cdots A_{n-1})$, e le scritture sono $n!$.

##### Derivazione — L'indipendenza è simmetrica · [[Probabilità.pdf#page=11|p. 11]]
> 🧩 Derivazione mia
$$
\begin{aligned}
P(A|B) = P(A) &\Rightarrow P(AB) = P(A|B)P(B) = P(A)P(B) && \text{prob. composta} \\
&\Rightarrow P(B|A) = \frac{P(AB)}{P(A)} = \frac{P(A)P(B)}{P(A)} = P(B) && P(A)\neq 0
\end{aligned}
$$

##### Derivazione — Perché per tre eventi servono entrambe le condizioni · [[Probabilità.pdf#page=12|p. 12]]
> 🧩 Derivazione mia: controesempi costruiti da me, non presenti nelle slide.

**(a) La fattorizzazione tripla non implica quella a coppie.** Prendo $\Omega = \{1,\dots,8\}$ equiprobabile, $A = B = \{1,2,3,4\}$, $C = \{1,5,6,7\}$:
$$
\begin{aligned}
P(ABC) &= P(\{1\}) = 1/8 = \tfrac12\cdot\tfrac12\cdot\tfrac12 = P(A)P(B)P(C) && \text{(2) vale} \\
P(AB) &= P(A) = 1/2 \neq 1/4 = P(A)P(B) && \text{(1) non vale}
\end{aligned}
$$

**(b) L'indipendenza a coppie non implica quella tripla.** Lancio due monete; $A$ = {testa al 1° lancio}, $B$ = {testa al 2°}, $C$ = {i due lanci danno lo stesso risultato}. Ogni evento ha probabilità $1/2$ e ogni coppia ha intersezione di probabilità $1/4$ (es. $AC$ = {TT}), quindi (1) vale. Però $ABC$ = {TT} e $P(ABC) = 1/4 \neq 1/8$.

**Ipotesi:** equiprobabilità dei risultati elementari in entrambi i controesempi.

#### Spiegazione · [[Probabilità.pdf#page=9|p. 9]], [[Probabilità.pdf#page=11|p. 11]], [[Probabilità.pdf#page=12|12]]

- **Ordine degli eventi**: matematicamente l'ordine nella probabilità composta è ininfluente, ma conviene condizionare sull'evento che si verifica *prima*, logicamente o cronologicamente. Esempio 2.3 (estrazione di due palle) → [[calcolo-probabilita-eventi]].
- **Indipendenti ≠ mutuamente esclusivi**.
  > 🧩 Derivazione mia: se $A\cap B = \emptyset$ con $P(A),P(B)>0$, allora $P(AB) = 0 \neq P(A)P(B) > 0$. Due eventi disgiunti a probabilità non nulla sono quindi sempre **dipendenti**: sapere che si è verificato $A$ esclude $B$.
- Per tre eventi indipendenti il condizionamento "non opera" mai: $P(A|B,C)=P(A)$, $P(AB|C) = P(AB)$, ecc.
- Esempio 2.6 (moneta lanciata due volte) → [[calcolo-probabilita-eventi]].

> 🎯 Esame: la confusione tra eventi indipendenti ed eventi mutuamente esclusivi è una domanda classica.

#### Perché importa

In ricezione si ragiona sempre per condizionamento: la probabilità d'errore *dato* il simbolo trasmesso, la verosimiglianza del segnale ricevuto *dato* un'ipotesi. L'indipendenza dei simboli e del rumore rende trattabili i calcoli.

#### Connessioni

- [[probabilita-totale-e-bayes]] — combina probabilità composta e partizione di $\Omega$.
- [[coppie-di-variabili-aleatorie]] — la pdf condizionale $f_Y(y|x)$ è la versione per v.a. di $P(A|B)$; l'indipendenza di v.a. è la fattorizzazione della pdf congiunta.

#### Fonti · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=12|p. 12]]

- [[elementi-teoria-probabilita]]

### Teorema della probabilità totale e teorema di Bayes · [[probabilita-totale-e-bayes|pagina]]

#### Definizione · [[Probabilità.pdf#page=13|p. 13]], [[Probabilità.pdf#page=14|14]]

**Ipotesi comuni:** $A_1, \dots, A_n$ eventi mutuamente esclusivi ($A_i \cap A_j = \emptyset$ per $i\neq j$) e $B \subseteq \bigcup_{i=1}^n A_i$.

- **Probabilità totale**: calcola $P(B)$ (l'*effetto*) a partire dalle probabilità **a priori** delle cause $P(A_i)$ e dalle condizionali $P(B|A_i)$.
- **Bayes**: sapendo che si è verificato $B$, calcola le probabilità **a posteriori** delle cause $P(A_i|B)$. È l'**inferenza bayesiana**.

> ⚠️ Contraddizione (refuso nelle slide): le pagine 13 e 14 scrivono "$A_j \cap A_j = \emptyset,\ i\neq j$". La condizione corretta è $A_i \cap A_j = \emptyset$ per $i \neq j$.

#### Formule · [[Probabilità.pdf#page=13|p. 13]], [[Probabilità.pdf#page=14|14]]

> 🧮 Formula chiave — Probabilità totale:
> $$P(B) = \sum_{i=1}^{n} P(B|A_i)\,P(A_i)$$

> 🧮 Formula chiave — Bayes:
> $$P(A_i|B) = \frac{P(B|A_i)\,P(A_i)}{\sum_{j=1}^{n} P(B|A_j)\,P(A_j)} = \frac{P(B|A_i)\,P(A_i)}{P(B)}$$

Simboli: $P(A_i)$ = probabilità a priori della causa $i$; $P(B|A_i)$ = probabilità dell'effetto data la causa (verosimiglianza); $P(A_i|B)$ = probabilità a posteriori. Sono tutte adimensionali.

#### Derivazioni

##### Derivazione — Teorema della probabilità totale · [[Probabilità.pdf#page=13|p. 13]]
> 🧩 Derivazione mia
$$
\begin{aligned}
B &= B \cap \Big(\textstyle\bigcup_i A_i\Big) && B \subseteq \cup_i A_i \\
&= \textstyle\bigcup_i (B \cap A_i) && \text{distributività} \\
P(B) &= \sum_i P(B A_i) && BA_i \text{ disgiunti (perché } A_i \text{ lo sono); additività} \\
&= \sum_i P(B|A_i)P(A_i) && \text{prob. composta, } [[probabilita-condizionale]]
\end{aligned}
$$

##### Derivazione — Teorema di Bayes
$$
\begin{aligned}
P(A_i|B) &= \frac{P(A_iB)}{P(B)} && \text{def. condizionale} \\
&= \frac{P(B|A_i)P(A_i)}{P(B)} && \text{prob. composta al numeratore} \\
&= \frac{P(B|A_i)P(A_i)}{\sum_j P(B|A_j)P(A_j)} && \text{prob. totale al denominatore}
\end{aligned}
$$
**Sanity check:** $\sum_i P(A_i|B) = 1$, perché il numeratore sommato su $i$ dà proprio il denominatore.
**Ipotesi:** $P(B) \neq 0$; cause mutuamente esclusive; ogni effetto ha almeno una causa.

#### Spiegazione · [[Probabilità.pdf#page=13|p. 13]]

![[probabilita-p13-probabilita-totale.png]]

Lettura "logica" delle ipotesi:
- le cause sono **mutuamente esclusive**;
- se si verifica l'effetto, si è verificata **una (e una sola)** delle cause.

Verificare $B \subseteq \bigcup_i A_i$ può essere complicato. Conviene scegliere gli $A_i$ come **partizione** di $\Omega$ ($\bigcup_i A_i = \Omega$): la condizione vale allora per ogni $B$.

> 🎯 Esame: saper enunciare le ipotesi, dire perché servono (senza esclusività si conterebbero due volte le intersezioni) e dare la lettura cause/effetto.

#### Perché importa · [[Intro.pdf#page=19|p. 19]]

Bayes è la base della **decisione** in ricezione, che la fonte cita come compito del demodulatore. Le cause sono i simboli trasmessi e l'effetto è il segnale ricevuto; scegliere la causa con la massima probabilità a posteriori è l'idea del ricevitore MAP.

> 📚 Fonte esterna: il collegamento con il criterio MAP è standard (es. Madhow, *Fundamentals of Digital Communication*, cap. sulla demodulazione ottima), ma non compare ancora nelle slide ingerite. TODO: verificare quando arriverà la fonte sulla modulazione digitale.

#### Connessioni · [[Probabilità.pdf#page=34|p. 34]]

- [[probabilita-condizionale]] — entrambi i teoremi sono conseguenze dirette della probabilità composta.
- [[coppie-di-variabili-aleatorie]] — versione per densità: $f_X(x|y) = f_Y(y|x) f_X(x)/f_Y(y)$, che segue dalle definizioni di p. 34.
- [[media-e-varianza]] — il centroide di Lloyd-Max $E[x|x\in R_i]$ è una media condizionale ([[quantizzazione-non-uniforme]]).

#### Fonti · [[Probabilità.pdf#page=13|p. 13]], [[Probabilità.pdf#page=14|14]]

- [[elementi-teoria-probabilita]]

### Variabile aleatoria: CDF, pdf, DF · [[variabile-aleatoria|pagina]]

#### Definizione · [[Probabilità.pdf#page=15|p. 15]]

Una **variabile aleatoria** (v.a.) è una funzione definita sullo spazio campione a valori nei reali estesi:
$$X: \omega \in \Omega \to X(\omega) \in \overline{\mathbb{R}} = \mathbb{R}\cup\{-\infty,+\infty\}$$
Serve a descrivere in forma numerica i risultati di un esperimento aleatorio, con $\Omega$ discreto o continuo e legge $P(\cdot)$.

![[probabilita-p15-variabile-aleatoria.png]]

#### Formule · [[Probabilità.pdf#page=16|p. 16]], [[Probabilità.pdf#page=18|p. 18]], [[Probabilità.pdf#page=19|19]]

| Funzione | Definizione |
|---|---|
| **CDF** (funzione di distribuzione cumulativa) | $F_X(x) \triangleq P(X \le x),\ \forall x\in\mathbb{R}$ |
| **pdf** (densità di probabilità) | $f_X(x) \triangleq \dfrac{d}{dx}F_X(x)$ (derivata generalizzata) |
| **DF / pmf** (distribuzione / "massa" di probabilità) | $p_X(x) \triangleq P(X = x)$ |

$F_X$ e $p_X$ sono adimensionali. $f_X$ ha le dimensioni di $[X]^{-1}$ (es. 1/V se $X$ è una tensione), perché $f_X(x)\,dx$ è una probabilità.

**Proprietà della CDF**:
1. $F(+\infty) = 1$, $F(-\infty) = 0$
2. monotona crescente (non strettamente): $x_1 < x_2 \Rightarrow F(x_1)\le F(x_2)$
3. $P(X>x) = 1-F(x)$ (CDF complementare o *funzione di affidabilità*)
4. continua da destra: $F(x^+) = F(x)$
5. $P(x_1 < X \le x_2) = F(x_2) - F(x_1)$
6. $P(X = x) = F(x) - F(x^-)$

**Proprietà della pdf**:
1. $f(x)\ge0$
2. $F(x) = \int_{-\infty}^{x} f(y)\,dy$
3. $\int_{-\infty}^{+\infty} f(x)\,dx = 1$
4. $P(x_1<X\le x_2) = \int_{x_1}^{x_2} f(x)\,dx$ (attenzione a eventuali impulsi in $x_1$ o $x_2$)
5. $P(x\le X\le x+\Delta x)\approx f(x)\Delta x \Rightarrow f(x) = \lim_{\Delta x\to0}\dfrac{P(x\le X\le x+\Delta x)}{\Delta x}$

**Proprietà della DF**: $p(x)\ge0$; $F(x) = \sum_{u\le x}p(u)$; $\sum_u p(u) = 1$; $P(x_1<X\le x_2) = \sum_{x_1<u\le x_2}p(u)$.

#### Derivazioni

> 🧩 Derivazione mia: le slide elencano le proprietà senza dimostrarle.

##### Derivazione — Proprietà 5 della CDF
$$
\begin{aligned}
\{X\le x_2\} &= \{X\le x_1\} \cup \{x_1 < X \le x_2\} && x_1<x_2,\ \text{unione disgiunta} \\
F(x_2) &= F(x_1) + P(x_1<X\le x_2) && \text{additività} \\
\Rightarrow P(x_1<X\le x_2) &= F(x_2) - F(x_1)
\end{aligned}
$$
La proprietà 2 segue subito: $F(x_2)-F(x_1)$ è una probabilità, quindi $\ge 0$.

##### Derivazione — Proprietà 3 della CDF
$\{X>x\}$ è il complementare di $\{X\le x\}$, quindi $P(X>x) = 1 - P(X\le x) = 1 - F(x)$ (proprietà 3 di [[spazio-di-probabilita]]).

##### Derivazione — Proprietà 6 della CDF
$$
\begin{aligned}
P(X = x) &= \lim_{\varepsilon\to0^+} P(x-\varepsilon < X \le x) && \{X=x\} = \textstyle\bigcap_\varepsilon \{x-\varepsilon<X\le x\} \\
&= \lim_{\varepsilon\to0^+} [F(x) - F(x-\varepsilon)] && \text{prop. 5} \\
&= F(x) - F(x^-)
\end{aligned}
$$
Quindi $P(X=x)$ è l'**ampiezza del salto** della CDF in $x$.

##### Derivazione — Proprietà 5 della pdf
$$
\begin{aligned}
P(x < X\le x+\Delta x) &= F(x+\Delta x) - F(x) && \text{prop. 5 CDF} \\
&= F'(x)\,\Delta x + o(\Delta x) && \text{Taylor al 1° ordine} \\
&\approx f(x)\,\Delta x && f = F'
\end{aligned}
$$
**Ipotesi:** $F$ derivabile in $x$, cioè nessun impulso della pdf in $x$.

##### Derivazione — Proprietà 3 della pdf
Dalla 2 e da $F(+\infty)=1$: $\int_{-\infty}^{+\infty}f = F(+\infty) = 1$.

#### Spiegazione

##### Tipi di v.a. e valore di $P(X=x)$ · [[Probabilità.pdf#page=17|p. 17]]–[[Probabilità.pdf#page=19|19]]
> 📄 Fonte: p. 17 («Discussione del valore assunto da $P(X=x)$ nei tre casi», lasciata alla lezione)

| Tipo | CDF | pdf | $P(X=x)$ |
|---|---|---|---|
| **Discreta** | costante a tratti: $F(x) = \sum_i p_i\,u(x-x_i)$ | $f(x) = \sum_i p_i\,\delta(x-x_i)$ | $p_i$ se $x=x_i$, 0 altrove |
| **Continua** | continua | senza impulsi | $0$ per ogni $x$ |
| **Mista** | discontinua ma non costante a tratti | parte continua + impulsi | $\neq 0$ solo nei punti di salto |

Simboli: $u(\cdot)$ = gradino unitario, $\delta(\cdot)$ = impulso di Dirac, $p_i = P(X=x_i)$.

> 🧩 Derivazione mia (la colonna $P(X=x)$): discende direttamente dalla prop. 6. Se $F$ è continua in $x$ il salto è nullo. Per una v.a. continua anche l'evento "$X$ vale esattamente $x$" ha probabilità zero, pur non essendo impossibile.

La DF "ha senso solo per v.a. discrete" e va calcolata solo nei punti $x=x_i$, altrove è nulla.

##### Esempio di v.a. mista
> 🧩 Derivazione mia (esempio non nelle slide): l'uscita di un [[quantizzazione-uniforme|quantizzatore]] con saturazione applicata a un ingresso gaussiano. È discreta; se invece si satura *senza* quantizzare, $Y = \min(X, X_{max})$ ha una parte continua più un impulso di area $P(X\ge X_{max})$ in $X_{max}$, quindi è mista.

#### Perché importa

Campioni di segnale, rumore ed errore di quantizzazione sono tutti modellati come v.a. Il modello $e(n)\sim\mathcal{U}(-\Delta/2,\Delta/2)$ è una pdf ([[snr-di-quantizzazione]]); la probabilità di sovraccarico è una CDF complementare ([[quantizzazione-uniforme]]).

#### Connessioni

- [[variabili-aleatorie-notevoli]] — CDF/pdf/DF di Bernoulli, Binomiale, Uniforme.
- [[variabile-aleatoria-gaussiana]] — la CDF non ha forma chiusa, quindi servono erf/erfc/Q.
- [[funzione-di-variabile-aleatoria]] — pdf di $Y=g(X)$.
- [[media-e-varianza]] — descrizione sintetica della pdf.

#### Fonti · [[Probabilità.pdf#page=15|p. 15]], [[Probabilità.pdf#page=19|p. 19]]

- [[elementi-teoria-probabilita]]

### Variabili aleatorie notevoli: Bernoulli, Binomiale, Uniforme (e Laplace) · [[variabili-aleatorie-notevoli|pagina]]

#### Definizione · Probabilità [[Probabilità.pdf#page=20|p. 20]]–[[Probabilità.pdf#page=23|23]] · Campionamento [[Campionamento_AD_DA.pdf#page=32|p. 32]]

| V.a. | Tipo | Parametri | Valori | Uso tipico |
|---|---|---|---|---|
| **Bernoulli** $X\sim\text{Bern}(p)$ | discreta | $p\in[0,1]$, $q=1-p$ | $\{0,1\}$ | successo/insuccesso; simile all'indicatrice di un evento |
| **Binomiale** $X\sim\mathcal{B}(n,p)$ | discreta | $n\in\mathbb{N}$, $p$ | $\{0,1,\dots,n\}$ | numero di successi in $n$ prove ripetute |
| **Uniforme** $X\sim\mathcal{U}(a,b)$ | continua | $a<b$ | $(a,b)$ | nessuna preferenza fra i valori di un intervallo limitato |
| **Gaussiana** $X\sim\mathcal{N}(\mu,\sigma)$ | continua | $\mu$, $\sigma>0$ | $\mathbb{R}$ | somma di molti contributi indipendenti → pagina dedicata [[variabile-aleatoria-gaussiana]] |
| **Laplace** | continua | $\lambda>0$ | $\mathbb{R}$ | ampiezze del segnale vocale |

#### Formule · Probabilità [[Probabilità.pdf#page=20|p. 20]]–[[Probabilità.pdf#page=22|22]] · Campionamento [[Campionamento_AD_DA.pdf#page=32|p. 32]]

| V.a. | DF / pdf | CDF |
|---|---|---|
| Bernoulli | $p(0)=q,\ p(1)=p$ | derivata sotto |
| Binomiale | $p(k) = \binom{n}{k}p^k q^{n-k}$ | derivata sotto |
| Uniforme | $f(x)=\frac{1}{b-a}$ per $x\in(a,b)$, 0 altrove | $F(x) = 0,\ \frac{x-a}{b-a},\ 1$ per $x<a$, $a\le x<b$, $x\ge b$ |
| Laplace | $f_X(x) = \frac{\lambda}{2}e^{-\lambda\|x\|}$ | — |

Unità: $f$ in $[X]^{-1}$; per la Laplace $\lambda$ ha unità $[X]^{-1}$ (es. 1/V).

**Momenti** (🧩 Derivazione mia; le slide sulla probabilità non li calcolano, ma servono: la varianza dell'uniforme dà $\Delta^2/12$ in [[snr-di-quantizzazione]]):

| V.a. | $E(X)$ | $\text{Var}(X)$ |
|---|---|---|
| Bern($p$) | $p$ | $pq$ |
| $\mathcal{B}(n,p)$ | $np$ | $npq$ |
| $\mathcal{U}(a,b)$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Laplace($\lambda$) | $0$ | $\frac{2}{\lambda^2}$ |

#### Derivazioni · [[Probabilità.pdf#page=20|p. 20]], [[Probabilità.pdf#page=21|21]]

Le CDF e pdf di Bernoulli e Binomiale sono esercizi lasciati al lettore nelle slide («Calcolare CDF e pdf»). Svolgimento completo in [[cdf-pdf-variabili-notevoli]]; qui i risultati:

$$
\begin{aligned}
\text{Bern:}\quad F(x) &= q\,u(x) + p\,u(x-1), & f(x) &= q\,\delta(x) + p\,\delta(x-1) \\
\text{Bin:}\quad F(x) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k}\,u(x-k), & f(x) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k}\,\delta(x-k)
\end{aligned}
$$

##### Derivazione — Normalizzazione della Binomiale · [[Probabilità.pdf#page=21|p. 21]]
$$
\begin{aligned}
\sum_{k=0}^n p(k) &= \sum_{k=0}^n \tbinom{n}{k}p^kq^{n-k} && \text{DF binomiale} \\
&= (p+q)^n && \text{sviluppo di Newton del binomio} \\
&= 1^n = 1 && p+q=1
\end{aligned}
$$

##### Derivazione — Da dove viene la DF binomiale · [[Probabilità.pdf#page=21|p. 21]]
> 🧩 Derivazione mia (la slide dà la formula senza giustificarla)

Faccio $n$ prove di Bernoulli **indipendenti**, ognuna con successo di probabilità $p$. Una sequenza *specifica* con $k$ successi e $n-k$ insuccessi ha probabilità $p^kq^{n-k}$, per l'indipendenza ([[probabilita-condizionale]]). Le sequenze con esattamente $k$ successi sono $\binom{n}{k}$ e sono eventi disgiunti; sommando si ottiene $p(k) = \binom nk p^kq^{n-k}$.

**Caso particolare** $n=1$: $p(0) = \binom10 q = q$ e $p(1) = \binom11 p = p$, cioè la Bernoulli.

##### Derivazione — CDF dell'Uniforme · [[Probabilità.pdf#page=22|p. 22]]
$$
\begin{aligned}
x<a:&\quad F(x) = \int_{-\infty}^x 0\,dy = 0 \\
a\le x<b:&\quad F(x) = \int_a^x \frac{1}{b-a}\,dy = \frac{x-a}{b-a} && \text{pdf costante in }(a,b) \\
x\ge b:&\quad F(x) = \int_a^b \frac{1}{b-a}\,dy = 1
\end{aligned}
$$
**Sanity check:** $F$ è continua in $a$ (vale 0) e in $b$ (vale 1), come deve per una v.a. continua.

##### Derivazione — Media e varianza dell'Uniforme · [[Campionamento_AD_DA.pdf#page=30|p. 30]]
> 🧩 Derivazione mia
$$
\begin{aligned}
E(X) &= \int_a^b \frac{x}{b-a}\,dx = \frac{b^2-a^2}{2(b-a)} = \frac{a+b}{2} && b^2-a^2=(b-a)(b+a) \\
E(X^2) &= \int_a^b \frac{x^2}{b-a}\,dx = \frac{b^3-a^3}{3(b-a)} = \frac{a^2+ab+b^2}{3} && b^3-a^3=(b-a)(a^2+ab+b^2) \\
\text{Var}(X) &= E(X^2) - E^2(X) && [[media-e-varianza]] \\
&= \frac{4(a^2+ab+b^2) - 3(a+b)^2}{12} && \text{denominatore comune} \\
&= \frac{a^2 - 2ab + b^2}{12} = \frac{(b-a)^2}{12}
\end{aligned}
$$
**Caso d'uso:** $a=-\Delta/2$, $b=\Delta/2$ → $\text{Var} = \Delta^2/12$, cioè la potenza del rumore di quantizzazione.

##### Derivazione — Media e varianza di Bernoulli e Binomiale
> 🧩 Derivazione mia
$$
\begin{aligned}
\text{Bern:}\ E(X) &= 0\cdot q + 1\cdot p = p, \quad E(X^2) = p, \quad \text{Var} = p - p^2 = pq \\
\text{Bin:}\ X &= \textstyle\sum_{i=1}^n X_i,\ X_i \sim \text{Bern}(p) \text{ indip.} && \text{conteggio dei successi} \\
E(X) &= \textstyle\sum_i E(X_i) = np && \text{linearità} \\
\text{Var}(X) &= \textstyle\sum_i \text{Var}(X_i) = npq && X_i \text{ incorrelate, } [[correlazione-e-covarianza]]
\end{aligned}
$$

##### Derivazione — Normalizzazione e varianza della Laplace · [[Campionamento_AD_DA.pdf#page=32|p. 32]]
> 🧩 Derivazione mia
$$
\begin{aligned}
\int_{-\infty}^{\infty}\tfrac{\lambda}{2}e^{-\lambda|x|}dx &= 2\cdot\tfrac{\lambda}{2}\int_0^\infty e^{-\lambda x}dx = \lambda\cdot\tfrac1\lambda = 1 && \text{pdf pari} \\
E(X) &= 0 && \text{pdf pari} \\
E(X^2) &= 2\cdot\tfrac\lambda2\int_0^\infty x^2e^{-\lambda x}dx = \lambda\cdot\tfrac{2}{\lambda^3} = \tfrac{2}{\lambda^2} && \textstyle\int_0^\infty x^2e^{-\lambda x}dx = 2/\lambda^3
\end{aligned}
$$
Quindi $x_{rms} = \sqrt2/\lambda$: più $\lambda$ è grande, più la pdf è concentrata intorno allo zero.

![[grafico-laplace-pdf-lambda.png]]
*🧩 Grafico mio (formula di p. 32): cuspide in 0 alta $\lambda/2$, code esponenziali; larghezza $\propto 1/\lambda$. Confronto con gaussiana e uniforme a pari potenza in [[quantizzazione-non-uniforme]].*

#### Spiegazione · Probabilità [[Probabilità.pdf#page=20|p. 20]], [[Probabilità.pdf#page=22|p. 22]] · Campionamento [[Campionamento_AD_DA.pdf#page=32|p. 32]]

![[probabilita-p22-uniforme.png]]

- **Esempio uniforme**: un bus arriva a caso tra le 10:00 e le 10:15, quindi $X\sim\mathcal{U}(0,900)$ s (15 min × 60 s/min = 900 s). Per esempio $P(X\le 300\,\text{s}) = 300/900 = 1/3$ (🧩 mio).
- La Bernoulli è simile alla v.a. **indicatrice** di un evento $A$: vale 1 se $\omega\in A$, 0 altrimenti, con $p = P(A)$.
- **Laplace e voce**: i valori vicini allo zero sono i più probabili, e per questo la quantizzazione uniforme non è ottima per la voce → [[quantizzazione-non-uniforme]].

#### Perché importa

- Bernoulli/Binomiale: il numero di bit errati in un blocco di $n$ bit, con errori indipendenti di probabilità $p$, è Binomiale.
  > 🧩 Derivazione mia: applicazione naturale, non nelle slide.
- Uniforme: è il modello dell'errore di quantizzazione ([[snr-di-quantizzazione]]).
- Laplace: è il modello delle ampiezze della voce ([[companding]]).

#### Connessioni

- [[variabile-aleatoria]] — definizioni di CDF, pdf, DF.
- [[variabile-aleatoria-gaussiana]] — la quarta v.a. notevole.
- [[media-e-varianza]] — i momenti in tabella.
- [[disuguaglianza-di-chebyshev]] — usata sul fattore di carico, vale per qualunque pdf.

#### Fonti · Probabilità [[Probabilità.pdf#page=20|p. 20]], [[Probabilità.pdf#page=23|p. 23]] · Campionamento [[Campionamento_AD_DA.pdf#page=32|p. 32]]

- [[elementi-teoria-probabilita]], [[campionamento-conversione-ad-da]]

### Variabile aleatoria Gaussiana e funzioni erf, erfc, Q · [[variabile-aleatoria-gaussiana|pagina]]

#### Definizione · [[Probabilità.pdf#page=23|p. 23]], [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=29|29]]

$X \sim \mathcal{N}(\mu,\sigma)$ (normale) è una v.a. continua con pdf a campana
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad x\in\mathbb{R}$$
- $\mu\in\mathbb{R}$: "baricentro" della pdf, cioè la media $E(X)$;
- $\sigma>0$: "larghezza" della pdf, cioè la deviazione standard, con $\sigma^2 = \text{Var}(X)$.

Descrive fenomeni che sono la somma di un gran numero di contributi indipendenti: **teorema centrale del limite** (CLT).

> ⚠️ Notazione: le slide scrivono $\mathcal{N}(\mu,\sigma)$ con la **deviazione standard** come secondo parametro. Molti testi usano $\mathcal{N}(\mu,\sigma^2)$. Nel wiki seguo la notazione delle slide.

![[probabilita-p23-gaussiana.png]]

#### Formule · [[Probabilità.pdf#page=24|p. 24]], [[Probabilità.pdf#page=25|25]]

**Funzioni integrali** (argomento adimensionale):
$$
\text{erf}(x) \triangleq \frac{2}{\sqrt\pi}\int_0^x e^{-t^2}dt, \qquad
\text{erfc}(x) \triangleq \frac{2}{\sqrt\pi}\int_x^{+\infty} e^{-t^2}dt = 1-\text{erf}(x)
$$
$$
Q(x) \triangleq \frac{1}{\sqrt{2\pi}}\int_x^{+\infty}e^{-t^2/2}dt \equiv \frac12\,\text{erfc}\!\left(\frac{x}{\sqrt2}\right)
$$

> 🧮 Formula chiave — CDF gaussiana:
> $$F(x) = \frac12\left[1+\text{erf}\left(\frac{x-\mu}{\sqrt2\,\sigma}\right)\right] = 1 - \frac12\,\text{erfc}\left(\frac{x-\mu}{\sqrt2\,\sigma}\right)$$

**Probabilità notevoli**, con $x \ge 0$ nelle ultime due:

| Evento | Espressione |
|---|---|
| $P(X<x)$ | $\frac12\left[1+\text{erf}\frac{x-\mu}{\sqrt2\sigma}\right] = \frac12\,\text{erfc}\frac{\mu-x}{\sqrt2\sigma}$ |
| $P(X>x)$ | $\frac12\,\text{erfc}\frac{x-\mu}{\sqrt2\sigma}$ |
| $P(\|X\|<x)$ | $\frac12\left[\text{erf}\frac{x-\mu}{\sqrt2\sigma} + \text{erf}\frac{x+\mu}{\sqrt2\sigma}\right]$ |
| $P(\|X\|>x)$ | $\frac12\left[\text{erfc}\frac{x-\mu}{\sqrt2\sigma} + \text{erfc}\frac{x+\mu}{\sqrt2\sigma}\right]$ |

> 🧮 Formula chiave (🧩 mia, conseguenza diretta): $P(X>x) = Q\!\left(\frac{x-\mu}{\sigma}\right)$.

#### Derivazioni

##### Derivazione — Normalizzazione della pdf · [[Probabilità.pdf#page=23|p. 23]]
$$
\begin{aligned}
\int_{-\infty}^{+\infty} \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx
&= \frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{+\infty} e^{-t^2}\sqrt2\,\sigma\,dt && t = \tfrac{x-\mu}{\sqrt2\sigma},\ dx = \sqrt2\sigma\,dt \\
&= \frac{1}{\sqrt\pi}\int_{-\infty}^{+\infty}e^{-t^2}dt && \text{semplifico } \sqrt2\sigma \\
&= \frac{1}{\sqrt\pi}\sqrt\pi = 1 && \text{integrale notevole}
\end{aligned}
$$

##### Derivazione — CDF in termini di erf · [[Probabilità.pdf#page=24|p. 24]]
$$
\begin{aligned}
F(x) &= \frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^x e^{-(t-\mu)^2/(2\sigma^2)}dt && \text{def. CDF} \\
&= \frac{1}{\sqrt\pi}\int_{-\infty}^{z} e^{-u^2}du, \quad z \triangleq \tfrac{x-\mu}{\sqrt2\sigma} && u = \tfrac{t-\mu}{\sqrt2\sigma} \\
&= \frac{1}{\sqrt\pi}\left[\int_{-\infty}^0 e^{-u^2}du + \int_0^z e^{-u^2}du\right] && \text{spezzo in } 0 \\
&= \frac{1}{\sqrt\pi}\left[\frac{\sqrt\pi}{2} + \frac{\sqrt\pi}{2}\text{erf}(z)\right] && \text{metà dell'integrale notevole; def. erf} \\
&= \frac12[1+\text{erf}(z)] = 1 - \frac12\text{erfc}(z) && \text{erf} = 1-\text{erfc}
\end{aligned}
$$
La formula vale anche per $z<0$: in quel caso $\int_0^z = -\int_z^0$ e $\text{erf}(z)<0$.

##### Derivazione — Le quattro probabilità notevoli · [[Probabilità.pdf#page=25|p. 25]]
> 🧩 Derivazione mia. Uso due proprietà: $\text{erf}$ è **dispari** ($\text{erf}(-z) = -\text{erf}(z)$, perché l'integrando è pari), e quindi $1+\text{erf}(z) = 1-\text{erf}(-z) = \text{erfc}(-z)$.

$$
\begin{aligned}
P(X<x) &= F(x) = \tfrac12[1+\text{erf}(z)] = \tfrac12\text{erfc}(-z) = \tfrac12\text{erfc}\tfrac{\mu-x}{\sqrt2\sigma} && \text{v.a. continua: } P(X=x)=0 \\
P(X>x) &= 1-F(x) = \tfrac12\text{erfc}(z) && \text{prop. 3 CDF} \\
P(|X|<x) &= F(x) - F(-x) && x\ge0 \\
&= \tfrac12\left[\text{erf}\tfrac{x-\mu}{\sqrt2\sigma} - \text{erf}\tfrac{-x-\mu}{\sqrt2\sigma}\right] && \text{sostituisco la CDF} \\
&= \tfrac12\left[\text{erf}\tfrac{x-\mu}{\sqrt2\sigma} + \text{erf}\tfrac{x+\mu}{\sqrt2\sigma}\right] && \text{erf dispari} \\
P(|X|>x) &= 1 - P(|X|<x) = \tfrac12\left[(1-\text{erf}\tfrac{x-\mu}{\sqrt2\sigma}) + (1-\text{erf}\tfrac{x+\mu}{\sqrt2\sigma})\right] && 1 = \tfrac12+\tfrac12 \\
&= \tfrac12\left[\text{erfc}\tfrac{x-\mu}{\sqrt2\sigma} + \text{erfc}\tfrac{x+\mu}{\sqrt2\sigma}\right]
\end{aligned}
$$
**Sanity check:** con $\mu=0$, $P(|X|>x) = \text{erfc}(x/(\sqrt2\sigma)) = 2Q(x/\sigma)$, due code uguali per simmetria.

##### Derivazione — $Q(x) = \frac12\text{erfc}(x/\sqrt2)$ · [[Probabilità.pdf#page=25|p. 25]]
$$
\begin{aligned}
Q(x) &= \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt && \text{def.} \\
&= \frac{1}{\sqrt{2\pi}}\int_{x/\sqrt2}^{\infty}e^{-u^2}\sqrt2\,du && t = \sqrt2 u \\
&= \frac12\cdot\frac{2}{\sqrt\pi}\int_{x/\sqrt2}^\infty e^{-u^2}du = \frac12\text{erfc}\left(\frac{x}{\sqrt2}\right) && \text{def. erfc}
\end{aligned}
$$
Quindi $P(X>x) = \frac12\text{erfc}\frac{x-\mu}{\sqrt2\sigma} = Q\left(\frac{x-\mu}{\sigma}\right)$: $Q$ è la coda della gaussiana **standard** $\mathcal{N}(0,1)$.

##### Derivazione — $E(X)=\mu$ e $\text{Var}(X)=\sigma^2$ · [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=29|29]]
> 🧩 Derivazione mia
$$
\begin{aligned}
E(X) &= \int x f(x)dx = \mu\underbrace{\int f(x)dx}_{=1} + \underbrace{\int (x-\mu) f(x)dx}_{=0} && x = \mu + (x-\mu);\ \text{integrando dispari intorno a } \mu \\
&= \mu \\
\text{Var}(X) &= \int (x-\mu)^2 f(x)dx = \frac{\sigma^2}{\sqrt{2\pi}}\int_{-\infty}^{\infty} t^2 e^{-t^2/2}dt && t=(x-\mu)/\sigma \\
&= \frac{\sigma^2}{\sqrt{2\pi}}\left( \left[-t e^{-t^2/2}\right]_{-\infty}^{\infty} + \int e^{-t^2/2}dt \right) && \text{per parti: } t\cdot t e^{-t^2/2} \\
&= \frac{\sigma^2}{\sqrt{2\pi}}(0 + \sqrt{2\pi}) = \sigma^2 && \int e^{-t^2/2}dt=\sqrt{2\pi}
\end{aligned}
$$

#### Spiegazione · [[Probabilità.pdf#page=24|p. 24]], [[Probabilità.pdf#page=26|p. 26]], [[Probabilità.pdf#page=27|27]]

- La CDF **non ha forma chiusa**: per questo si introducono funzioni tabulate/numeriche.
- In **Matlab**: `erf`, `erfc`, `qfunc`. Codice per la CDF di $\mathcal{N}(0,1)$:
  ```matlab
  x = -3:0.1:3;
  y = (1/2)*(1+erf(x/sqrt(2)));
  plot(x,y)
  grid on
  title('CDF of normal distribution with µ = 0 and σ = 1')
  xlabel('x')
  ylabel('CDF')
  ```
  Qui $\mu=0$, $\sigma=1$, quindi $z = x/\sqrt2$.
- Una **trasformazione affine** di una gaussiana è ancora gaussiana → [[funzione-di-variabile-aleatoria]].

> 🎯 Esame: saper passare da erf/erfc/Q in entrambi i sensi e scrivere $P(X>x)$, $P(|X|>x)$ per una gaussiana non standard. Nel corso la probabilità d'errore dei sistemi digitali si scriverà con $Q(\cdot)$.

**Valori di riferimento** — 📚 Fonte esterna (tabelle standard della Q, non nelle slide): $Q(1)\approx 0.159$, $Q(2)\approx 0.0228$, $Q(3)\approx 1.35\cdot10^{-3}$, $Q(4)\approx 3.17\cdot10^{-5}$.

> 💡 Connessione: con il *four-sigma loading* ([[quantizzazione-uniforme]]), se il segnale fosse gaussiano la probabilità di sovraccarico sarebbe $P(|X|>4\sigma) = 2Q(4) \approx 6.3\cdot10^{-5}$ (🧩 mio). È molto meno del limite di Chebyshev (6.25%), che vale per qualunque pdf ed è quindi pessimistico.

#### Perché importa · [[Intro.pdf#page=18|p. 18]]

Il rumore termico è somma di moltissimi contributi indipendenti (moto degli elettroni), quindi per il CLT è gaussiano. La funzione $Q$ sarà lo strumento standard per le probabilità d'errore.

#### Connessioni

- [[variabile-aleatoria]] — definizione di CDF/pdf.
- [[media-e-varianza]] — interpretazione di $\mu$ e $\sigma$.
- [[funzione-di-variabile-aleatoria]] — $aX+b$ resta gaussiana.
- [[disuguaglianza-di-chebyshev]] — limite generico contro calcolo esatto con la Q.
- [[processo-gaussiano]] — la versione a $n$ variabili (gaussiana multivariata); per $n = 1$ si ritrova questa pdf.

#### Fonti · [[Probabilità.pdf#page=23|p. 23]], [[Probabilità.pdf#page=26|p. 26]]

- [[elementi-teoria-probabilita]]

### Funzione di una variabile aleatoria · [[funzione-di-variabile-aleatoria|pagina]]

#### Definizione · [[Probabilità.pdf#page=27|p. 27]]

Se $X$ è una v.a. e $g$ una funzione reale, $Y = g(X)$ è a sua volta una v.a. La sua CDF si ricava dalla definizione:
$$F_Y(y) = P\big(\{\omega\in\Omega : g(X(\omega))\le y\}\big)$$

> ⚠️ Contraddizione (refuso nelle slide): la slide scrive "$g(X(\omega)) \le x$". L'argomento corretto è $y$.

#### Formule · [[Probabilità.pdf#page=27|p. 27]]

> 🧮 Formula chiave: se $y=g(x)$ ha un numero finito di soluzioni $x_i$ e in ciascuna $g'(x_i)$ esiste ed è $\neq 0$,
> $$f_Y(y) = \sum_i \frac{f_X(x_i)}{|g'(x_i)|}$$

Simboli: $x_i = x_i(y)$ radici di $g(x)=y$; $g'$ derivata di $g$.

Caso affine $Y = aX+b$ con $X\sim\mathcal{N}(0,1)$:
$$f_Y(y) = \frac{1}{|a|}f_X\!\left(\frac{y-b}{a}\right) = \frac{1}{\sqrt{2\pi a^2}}\,e^{-\frac{(y-b)^2}{2a^2}}$$

#### Derivazioni

##### Derivazione — Formula per $g$ monotona (giustifica il $|g'|$) · [[Probabilità.pdf#page=27|p. 27]]
> 🧩 Derivazione mia, caso di una sola radice

$g$ crescente ($g'>0$), $x_1 = g^{-1}(y)$:
$$
\begin{aligned}
F_Y(y) &= P(g(X)\le y) = P(X \le g^{-1}(y)) = F_X(g^{-1}(y)) && g \text{ crescente conserva } \le \\
f_Y(y) &= f_X(g^{-1}(y))\cdot\frac{d g^{-1}(y)}{dy} = \frac{f_X(x_1)}{g'(x_1)} && \text{derivata della funzione inversa}
\end{aligned}
$$
$g$ decrescente ($g'<0$):
$$
\begin{aligned}
F_Y(y) &= P(X \ge g^{-1}(y)) = 1 - F_X(g^{-1}(y)) && g \text{ decrescente inverte } \le;\ X \text{ continua} \\
f_Y(y) &= -\frac{f_X(x_1)}{g'(x_1)} = \frac{f_X(x_1)}{|g'(x_1)|} && g'<0
\end{aligned}
$$
I due casi si riassumono con $|g'|$. Con più radici, $\{Y\in(y,y+dy)\}$ è l'unione disgiunta degli intervalli intorno a ciascuna $x_i$, e i contributi si sommano.

##### Derivazione — $Y = aX+b$, $X\sim\mathcal{N}(0,1)$ · [[Probabilità.pdf#page=27|p. 27]], [[Probabilità.pdf#page=30|p. 30]]
$$
\begin{aligned}
g(x) &= ax+b,\quad g'(x) = a && a\neq0 \\
y = ax+b &\Rightarrow x_1 = \frac{y-b}{a} && \text{unica radice} \\
f_Y(y) &= \frac{f_X\left(\frac{y-b}{a}\right)}{|a|} && \text{formula generale} \\
&= \frac{1}{|a|}\cdot\frac{1}{\sqrt{2\pi}}e^{-\frac12\left(\frac{y-b}{a}\right)^2} && f_X(x) = \tfrac{1}{\sqrt{2\pi}}e^{-x^2/2} \\
&= \frac{1}{\sqrt{2\pi a^2}}e^{-\frac{(y-b)^2}{2a^2}} && |a|=\sqrt{a^2}
\end{aligned}
$$
**Risultato:** $Y\sim\mathcal{N}(b, |a|)$.
**Sanity check:** coerente con $E(aX+b) = aE(X)+b = b$ e $\sigma_Y = |a|\sigma_X = |a|$ (vedi [[media-e-varianza]]).

> 🧩 Generalizzazione mia: con $X\sim\mathcal{N}(\mu,\sigma)$ lo stesso procedimento dà $Y\sim\mathcal{N}(a\mu+b, |a|\sigma)$. Il caso $a = 1/\sigma$, $b = -\mu/\sigma$ è la **standardizzazione** $Z = (X-\mu)/\sigma \sim \mathcal{N}(0,1)$, cioè il passaggio che giustifica $P(X>x) = Q((x-\mu)/\sigma)$ in [[variabile-aleatoria-gaussiana]].

#### Spiegazione · [[Probabilità.pdf#page=27|p. 27]]

> 🎯 Esame: «La trasformazione affine di una v.a. Gaussiana è essa stessa una v.a. Gaussiana».

Metodo pratico:
1. risolvere $g(x)=y$ e trovare tutte le radici $x_i(y)$;
2. calcolare $|g'(x_i)|$;
3. sommare $f_X(x_i)/|g'(x_i)|$;
4. se per certi $y$ non ci sono radici, lì $f_Y(y) = 0$.

Esempio di non-monotonia (🧩 mio): per $Y = X^2$ le radici sono $\pm\sqrt y$ per $y>0$, quindi $f_Y(y) = [f_X(\sqrt y)+f_X(-\sqrt y)]/(2\sqrt y)$.

#### Perché importa

I sistemi trasformano v.a.: un amplificatore di guadagno $a$ con offset $b$ è una trasformazione affine, il quadrato corrisponde al calcolo di una potenza istantanea, il [[companding]] è una trasformazione non lineare $F(x)$. Un quantizzatore $Q[\cdot]$ è una $g$ a gradini: $g'=0$ quasi ovunque, quindi la formula non si applica e l'uscita è discreta.

#### Connessioni

- [[media-e-varianza]] — il teorema fondamentale della media permette di calcolare $E[g(X)]$ **senza** ricavare $f_Y$.
- [[variabile-aleatoria-gaussiana]] — la chiusura rispetto alle trasformazioni affini.
- [[companding]] — la legge di compressione $F(x)$ è una funzione di v.a.

#### Fonti · [[Probabilità.pdf#page=27|p. 27]]

- [[elementi-teoria-probabilita]]

### Media statistica, momenti e varianza · [[media-e-varianza|pagina]]

#### Definizione · [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=29|29]]

- **Media statistica** (valore atteso) di una v.a. $X$ con pdf $f(x)$: $E(X) \triangleq \int_{-\infty}^{+\infty}x\,f(x)\,dx$.
- **Momento $n$-esimo**: $\mu_n = E(X^n) \triangleq \int x^n f(x)\,dx$. Per $n=2$ si ha il **valor quadratico medio** $E(X^2)$.
- **Varianza**: $\text{Var}(X) = \sigma_X^2 \triangleq E[(X-E(X))^2]$.
- **Deviazione standard**: $\sigma_X \triangleq \sqrt{\text{Var}(X)}$.

Unità: $E(X)$ e $\sigma_X$ hanno l'unità di $X$ (es. V); $E(X^2)$ e $\text{Var}(X)$ il suo quadrato (es. V², che su 1 Ω è una potenza in W).

#### Formule · [[Probabilità.pdf#page=28|p. 28]]–[[Probabilità.pdf#page=30|30]]

> 🧮 Formula chiave — **Teorema fondamentale della media**:
> $$E[g(X)] = \int_{-\infty}^{+\infty} g(x)\,f(x)\,dx \qquad \text{(discreto: } \textstyle\sum_i p(x_i)g(x_i))$$

> 🧮 Formula chiave:
> $$\text{Var}(X) = E(X^2) - E^2(X)$$

**Proprietà della media**, con $a,b$ costanti reali e $g,h$ funzioni reali:
1. Linearità: $E[a\,g(X)+b\,h(X)] = a\,E[g(X)]+b\,E[h(X)]$; in particolare $E(aX+b) = aE(X)+b$
2. $g(x)\ge0\ \forall x \Rightarrow E[g(X)]\ge0$
3. $g_1\ge g_2\ \forall x \Rightarrow E[g_1(X)]\ge E[g_2(X)]$
4. $a\le g(x)\le b\ \forall x \Rightarrow a\le E[g(X)]\le b$

**Proprietà della varianza**:
- $\text{Var}(aX+b) = a^2\,\text{Var}(X)$: non dipende da $b$ (invarianza per traslazione); $\sigma_Y = |a|\sigma_X$
- v.a. **centrata** $Y = X-\mu_X$: $E(Y)=0$, $\text{Var}(Y) = \text{Var}(X)$

#### Derivazioni

##### Derivazione — $\text{Var}(X) = E(X^2)-E^2(X)$ · [[Probabilità.pdf#page=29|p. 29]]
$$
\begin{aligned}
\text{Var}(X) &= E[(X-\mu)^2], \quad \mu \triangleq E(X) && \text{def.} \\
&= E[X^2 - 2\mu X + \mu^2] && \text{sviluppo il quadrato} \\
&= E(X^2) - 2\mu E(X) + \mu^2 && \text{linearità; } \mu \text{ costante} \\
&= E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2 && E(X)=\mu
\end{aligned}
$$
**Sanity check:** $\text{Var}\ge0 \Rightarrow E(X^2)\ge E^2(X)$, cioè la potenza totale è almeno quella della componente continua.

##### Derivazione — $\text{Var}(aX+b) = a^2\text{Var}(X)$ · [[Probabilità.pdf#page=30|p. 30]]
$$
\begin{aligned}
E(aX+b) &= a\mu + b && \text{linearità} \\
\text{Var}(aX+b) &= E[(aX + b - a\mu - b)^2] && \text{def.} \\
&= E[a^2(X-\mu)^2] = a^2\,\text{Var}(X) && b \text{ si cancella}
\end{aligned}
$$

##### Derivazione — Linearità della media
Dal teorema fondamentale: $\int[a g(x)+b h(x)]f(x)dx = a\int g f + b\int h f$ (linearità dell'integrale). Le proprietà 2–4 seguono da $f\ge0$ (monotonia dell'integrale) e da $\int f = 1$ (per la 4).

##### Derivazione — Media e varianza della Gaussiana
Vedi [[variabile-aleatoria-gaussiana]] (derivazione $E(X)=\mu$, $\text{Var}(X)=\sigma^2$).

#### Spiegazione · Probabilità [[Probabilità.pdf#page=23|p. 23]] · Campionamento [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- La media è il **baricentro** della pdf, la deviazione standard ne misura la **larghezza**.
- Il teorema fondamentale della media è molto comodo: per calcolare $E[g(X)]$ basta $f_X$ e non serve ricavare la pdf di $Y=g(X)$ ([[funzione-di-variabile-aleatoria]]).
- Lettura "elettrica" (🧩 mia; nelle slide appare in p. 29 come $x_{rms} = \sqrt{P_x}$): per un segnale modellato come v.a., $E(X)$ è la componente continua, $E(X^2)$ la potenza (valor quadratico medio) e, per una v.a. a media nulla, $\sigma_X = x_{rms}$ è il valore efficace.

> 🎯 Esame: il valor quadratico medio dell'errore di quantizzazione $E[e^2] = \Delta^2/12$ è una varianza di un'uniforme a media nulla ([[snr-di-quantizzazione]]).

Momenti delle v.a. notevoli: tabella in [[variabili-aleatorie-notevoli]].

#### Perché importa

Potenza di segnale, potenza di rumore e SNR sono tutti momenti del secondo ordine. L'MSE che Lloyd-Max minimizza ([[quantizzazione-non-uniforme]]) è un valor quadratico medio; il centroide $E[x|x\in R_i]$ è una media condizionale.

#### Connessioni

- [[correlazione-e-covarianza]] — estende media e varianza alle coppie di v.a.
- [[disuguaglianza-di-chebyshev]] — usa media e varianza per limitare le code della pdf.
- [[snr-di-quantizzazione]] — $P_x = E[x^2]$, $P_e = E[e^2]$.

#### Fonti · [[Probabilità.pdf#page=28|p. 28]], [[Probabilità.pdf#page=30|p. 30]]

- [[elementi-teoria-probabilita]]

### Coppie di variabili aleatorie · [[coppie-di-variabili-aleatorie|pagina]]

#### Definizione · [[Probabilità.pdf#page=31|p. 31]]

Una **coppia di v.a.** è formata da due funzioni definite sullo stesso $\Omega$:
$$(X,Y): \omega\in\Omega \to (X(\omega), Y(\omega)) \in \mathbb{R}\times\mathbb{R}$$
Le CDF marginali $F_X$ e $F_Y$ descrivono le singole v.a. ma **non** la loro relazione. Per quella servono le funzioni congiunte.

![[probabilita-p31-coppia-va.png]]

#### Formule · [[Probabilità.pdf#page=31|p. 31]]–[[Probabilità.pdf#page=35|35]]

| Grandezza | Definizione |
|---|---|
| CDF congiunta | $F_{XY}(x,y) \triangleq P(X\le x, Y\le y)$ |
| pdf congiunta | $f_{XY}(x,y) \triangleq \dfrac{\partial^2 F_{XY}(x,y)}{\partial x\,\partial y}$ |
| pdf condizionale | $f_X(x\|y) \triangleq \dfrac{f_{XY}(x,y)}{f_Y(y)}$, $\quad f_Y(y\|x) \triangleq \dfrac{f_{XY}(x,y)}{f_X(x)}$ |
| indipendenza | $f_{XY}(x,y) = f_X(x)\,f_Y(y)$ |

Unità: $f_{XY}$ ha dimensione $[X]^{-1}[Y]^{-1}$.

**Proprietà di base**:
1. $F_X(x) = F_{XY}(x,+\infty)$ — CDF marginale di $X$
2. $F_Y(y) = F_{XY}(+\infty,y)$
3. $f_X(x) = \int_{-\infty}^{+\infty} f_{XY}(x,y)\,dy$ — pdf marginale
4. $f_Y(y) = \int_{-\infty}^{+\infty} f_{XY}(x,y)\,dx$
5. $\iint f_{XY}\,dx\,dy = 1$
6. $P((X,Y)\in A) = \iint_A f_{XY}(x,y)\,dx\,dy$
7. $F_{XY}(x,y) = \int_{-\infty}^x\int_{-\infty}^y f_{XY}(u,v)\,du\,dv$

**Proprietà della CDF congiunta**:
1. $F(-\infty,y) = F(x,-\infty) = 0$, $F(+\infty,+\infty) = 1$
2. $P(x_1<X\le x_2, Y\le y) = F(x_2,y) - F(x_1,y)$ (analoga in $y$)
3. $P(x_1<X\le x_2,\ y_1<Y\le y_2) = F(x_2,y_2) - F(x_1,y_2) - F(x_2,y_1) + F(x_1,y_1)$
   — regola mnemonica: "+" per le coppie concordi ($x_1y_1$, $x_2y_2$), "−" per le discordi.

#### Derivazioni

> 🧩 Derivazione mia: le slide riassumono le proprietà senza dimostrarle.

##### Derivazione — CDF marginale (prop. 1)
$\{Y\le+\infty\} = \Omega$, quindi $F_{XY}(x,+\infty) = P(\{X\le x\}\cap\Omega) = P(X\le x) = F_X(x)$.

##### Derivazione — pdf marginale (prop. 3)
$$
\begin{aligned}
F_X(x) &= F_{XY}(x,+\infty) = \int_{-\infty}^{x}\left[\int_{-\infty}^{+\infty} f_{XY}(u,v)\,dv\right]du && \text{prop. 1 + prop. 7} \\
f_X(x) &= \frac{dF_X}{dx} = \int_{-\infty}^{+\infty} f_{XY}(x,v)\,dv && \text{teorema fondamentale del calcolo}
\end{aligned}
$$

##### Derivazione — Probabilità di un rettangolo (prop. 3 della CDF)
$$
\begin{aligned}
P(x_1<X\le x_2,\ y_1<Y\le y_2) &= P(x_1<X\le x_2, Y\le y_2) - P(x_1<X\le x_2, Y\le y_1) && \{Y\le y_2\} = \{Y\le y_1\}\cup\{y_1<Y\le y_2\} \\
&= [F(x_2,y_2)-F(x_1,y_2)] - [F(x_2,y_1)-F(x_1,y_1)] && \text{prop. 2 applicata due volte}
\end{aligned}
$$

##### Derivazione — Normalizzazione delle pdf condizionali · [[Probabilità.pdf#page=34|p. 34]]
$$
\int_{-\infty}^{+\infty} f_X(x|y)\,dx = \frac{1}{f_Y(y)}\int f_{XY}(x,y)\,dx = \frac{f_Y(y)}{f_Y(y)} = 1 \qquad \text{(prop. 4 delle marginali)}
$$

##### Derivazione — Indipendenza ⇒ condizionale = marginale · [[Probabilità.pdf#page=35|p. 35]]
$$f_X(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)} = \frac{f_X(x)f_Y(y)}{f_Y(y)} = f_X(x)$$
Analogamente $f_Y(y|x) = f_Y(y)$.

#### Spiegazione · [[Probabilità.pdf#page=34|p. 34]], [[Probabilità.pdf#page=35|35]]

- **Pdf condizionale**: dice come cambia la distribuzione di $Y$ quando si fissa $\{X=x\}$. Esempio della slide: il peso $Y$ di una persona di cui si conosce l'altezza $X$. È l'analogo per densità di $P(A|B)$ ([[probabilita-condizionale]]).
- **Indipendenza**: la fattorizzazione si può scrivere in modo equivalente con la CDF congiunta ($F_{XY} = F_XF_Y$) o con la DF congiunta per v.a. discrete.
- Dalla congiunta si ricavano sempre le marginali. Il viceversa vale **solo** se c'è indipendenza.

> 🎯 Esame: marginali dalla congiunta, definizione di pdf condizionale, differenza tra indipendenza e incorrelazione (vedi [[correlazione-e-covarianza]]).

#### Perché importa · [[Intro.pdf#page=3|p. 3]]

Segnale e rumore, oppure due campioni successivi dello stesso segnale, sono coppie di v.a. La loro relazione statistica (indipendenza, correlazione) è la base dei **processi aleatori**, argomento del corso.

#### Connessioni · [[Probabilità.pdf#page=34|p. 34]]

- [[correlazione-e-covarianza]] — descrizione sintetica (momenti misti) della coppia.
- [[probabilita-totale-e-bayes]] — Bayes per densità: $f_X(x|y) = f_Y(y|x)f_X(x)/f_Y(y)$ (🧩 mio, combinando le due definizioni di p. 34).
- [[media-e-varianza]] — il teorema fondamentale della media si estende alle coppie.
- [[processo-aleatorio]] — due campioni di un processo sono una coppia di v.a.; le marginali danno la coerenza delle distribuzioni di ordine $k$.

#### Fonti · [[Probabilità.pdf#page=31|p. 31]], [[Probabilità.pdf#page=35|p. 35]]

- [[elementi-teoria-probabilita]]

### Correlazione, covarianza e coefficiente di correlazione · [[correlazione-e-covarianza|pagina]]

#### Definizione · [[Probabilità.pdf#page=37|p. 37]], [[Probabilità.pdf#page=38|38]]

Per una coppia $(X,Y)$ con pdf congiunta $f_{XY}$, medie $\mu_X,\mu_Y$ e deviazioni standard $\sigma_X,\sigma_Y$:

| Grandezza | Definizione |
|---|---|
| **Correlazione** | $\text{Corr}(X,Y) \triangleq E(XY) = \iint xy\,f_{XY}(x,y)\,dx\,dy$ |
| **Covarianza** | $\text{Cov}(X,Y) \triangleq E[(X-\mu_X)(Y-\mu_Y)]$ |
| **Coefficiente di correlazione** | $\rho_{XY} \triangleq \dfrac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y}$ (adimensionale) |

Correlazione e covarianza possono avere segno qualsiasi. Casi particolari: $\text{Corr}(X,X) = E(X^2)$ e $\text{Cov}(X,X) = \text{Var}(X)$.

Terminologia usata in p. 38:
- $X,Y$ **ortogonali** se $E(XY) = 0$;
- $X,Y$ **incorrelate** se $\text{Cov}(X,Y) = 0$.

#### Formule · [[Probabilità.pdf#page=36|p. 36]], [[Probabilità.pdf#page=38|p. 38]]

**Teorema fondamentale della media per coppie**: $E[g(X,Y)] = \iint g(x,y)f_{XY}(x,y)\,dx\,dy$ (per il caso discreto: $\sum_{i,j}g(x_i,y_j)p_{XY}(x_i,y_j)$). La media è lineare: $E(a_1X+a_2Y) = a_1E(X)+a_2E(Y)$.

**Proprietà**:
1. $\text{Cov}(X,Y) = E(XY) - E(X)E(Y)$ — relazione fondamentale
2. $E[(X+Y)^2] = E(X^2)+E(Y^2)+2E(XY)$; se $X,Y$ sono ortogonali, $E[(X+Y)^2] = E(X^2)+E(Y^2)$
3. $\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y)+2\,\text{Cov}(X,Y)$; se sono incorrelate, le varianze si sommano.
   In generale: $\text{Var}\left(\sum_i c_iX_i\right) = \sum_i c_i^2\text{Var}(X_i) + \sum_i\sum_{j\neq i}c_ic_j\text{Cov}(X_i,X_j)$
4. $|E(XY)| \le \sqrt{E(X^2)}\sqrt{E(Y^2)}$ — Schwarz; uguaglianza se e solo se $Y = a^*X$ in media quadratica
5. $|\text{Cov}(X,Y)| \le \sigma_X\sigma_Y$ — Schwarz; uguaglianza se e solo se $Y = a^*X+b^*$ in media quadratica
6. $|\rho_{XY}|\le 1$

> 🧮 Formula chiave: proprietà 1 e 3.

#### Derivazioni

> 🧩 Derivazione mia: le slide enunciano le proprietà senza passaggi.

##### Derivazione — Proprietà 1
$$
\begin{aligned}
\text{Cov}(X,Y) &= E[XY - \mu_YX - \mu_XY + \mu_X\mu_Y] && \text{sviluppo il prodotto} \\
&= E(XY) - \mu_Y\mu_X - \mu_X\mu_Y + \mu_X\mu_Y && \text{linearità} \\
&= E(XY) - E(X)E(Y)
\end{aligned}
$$

##### Derivazione — Proprietà 2 e 3
$$
\begin{aligned}
E[(X+Y)^2] &= E[X^2+2XY+Y^2] = E(X^2)+E(Y^2)+2E(XY) && \text{linearità} \\
\text{Var}(X+Y) &= E\big[\big((X-\mu_X)+(Y-\mu_Y)\big)^2\big] && \mu_{X+Y} = \mu_X+\mu_Y \\
&= \text{Var}(X)+\text{Var}(Y)+2\text{Cov}(X,Y) && \text{prop. 2 sulle v.a. centrate}
\end{aligned}
$$
Caso generale: $\text{Var}(\sum_ic_iX_i) = E[(\sum_ic_i(X_i-\mu_i))^2] = \sum_i\sum_jc_ic_j\text{Cov}(X_i,X_j)$. Separando i termini $i=j$, dove $\text{Cov}(X_i,X_i) = \text{Var}(X_i)$, si ottiene la formula della slide.

##### Derivazione — Disuguaglianza di Schwarz (prop. 4)
$$
\begin{aligned}
0 &\le E[(Y-aX)^2] \quad \forall a\in\mathbb{R} && \text{media di una quantità} \ge 0 \\
&= E(Y^2) - 2a\,E(XY) + a^2E(X^2) && \text{polinomio di 2° grado in } a \\
\Rightarrow \Delta &= 4E^2(XY) - 4E(X^2)E(Y^2) \le 0 && \text{mai negativo} \Rightarrow \text{discriminante} \le 0 \\
\Rightarrow |E(XY)| &\le \sqrt{E(X^2)E(Y^2)}
\end{aligned}
$$
L'uguaglianza vale se e solo se $\Delta = 0$, cioè esiste $a^*$ con $E[(Y-a^*X)^2] = 0$: $Y = a^*X$ in media quadratica.
**Prop. 5:** applico la 4 alle v.a. centrate $X-\mu_X$ e $Y-\mu_Y$. **Prop. 6:** divido la 5 per $\sigma_X\sigma_Y$.

##### Derivazione — Indipendenti ⇒ incorrelate · [[Probabilità.pdf#page=35|p. 35]], [[Probabilità.pdf#page=36|36]]
> 🧩 Derivazione mia (non esplicitata nelle slide, ma segue da p. 35 e p. 36)
$$
E(XY) = \iint xy\,f_X(x)f_Y(y)\,dx\,dy = \int xf_X\,dx\int yf_Y\,dy = E(X)E(Y) \Rightarrow \text{Cov} = 0
$$
Il **viceversa è falso** in generale. Controesempio (🧩 mio): $X\sim\mathcal{U}(-1,1)$ e $Y=X^2$ sono incorrelate, perché $E(XY) = E(X^3) = 0 = E(X)E(Y)$, ma $Y$ è funzione deterministica di $X$.

#### Spiegazione

- **Ortogonale ≠ incorrelato**: i due concetti coincidono se almeno una delle v.a. ha media nulla (per la prop. 1).
- $\rho_{XY}$ misura la **dipendenza lineare**: $|\rho|=1$ se e solo se $Y$ è una funzione affine di $X$ in media quadratica (prop. 5); $\rho=0$ significa nessuna dipendenza *lineare*, ma può esserci dipendenza non lineare.
- La prop. 3 serve a sommare potenze di rumore: segnale e rumore incorrelati → le potenze si sommano.

> 🎯 Esame: indipendenza ⇒ incorrelazione ma non viceversa; ortogonalità vs incorrelazione; dimostrazione di Schwarz.

#### Perché importa · [[Campionamento_AD_DA.pdf#page=28|p. 28]]

L'ipotesi "errore di quantizzazione incorrelato col segnale" (modello additivo $x_q = x + e$) serve a dire che la potenza di $x_q$ è $P_x + P_e$. La funzione di autocorrelazione dei processi aleatori estende $\text{Corr}(X,Y)$ a due campioni dello stesso processo.

> 🧩 Derivazione mia: il collegamento con il modello del quantizzatore è una mia lettura. La slide 28 introduce il modello a sommatore senza parlare di correlazione.

#### Connessioni

- [[media-e-varianza]] — per $X=Y$ le definizioni si riducono a valor quadratico medio e varianza.
- [[coppie-di-variabili-aleatorie]] — i momenti misti sono calcolati dalla pdf congiunta.
- [[variabili-aleatorie-notevoli]] — la varianza della binomiale ($npq$) usa la prop. 3 generalizzata.
- [[momenti-di-un-processo]] — autocorrelazione e autocovarianza di un processo sono correlazione e covarianza di due suoi campioni; incoerenza e incorrelazione tra processi ricalcano ortogonalità e incorrelazione tra v.a.
- [[autocorrelazione-processi-wss]] — la disuguaglianza di Schwarz dà $|R_{XX}(\tau)| \le R_{XX}(0)$.

#### Fonti · [[Probabilità.pdf#page=36|p. 36]], [[Probabilità.pdf#page=38|p. 38]]

- [[elementi-teoria-probabilita]]

### Calcolo di probabilità di eventi · [[calcolo-probabilita-eventi|pagina]]

#### Metodo · [[Probabilità.pdf#page=9|p. 9]]

1. **Definire** $\Omega$ ed esplicitare gli eventi come sottoinsiemi ([[spazio-di-probabilita]]).
2. Tradurre il testo: "e" → $\cap$, "o" → $\cup$, "non" → complementare.
3. Scegliere lo strumento:
   - risultati **equiprobabili** in $\Omega$ finito → $P(A) = |A|/|\Omega|$ (conteggio / combinatoria);
   - esperimento **in più passi** → probabilità composta / regola della catena, condizionando sull'evento che avviene "prima";
   - **cause/effetto** → probabilità totale e Bayes ([[probabilita-totale-e-bayes]]).
4. Per l'**indipendenza**: controllare $P(AB) = P(A)P(B)$, non l'intuizione.
5. Sanity check: $0\le P\le1$, complementari che sommano a 1.

#### Formule usate · [[Probabilità.pdf#page=6|p. 6]], [[Probabilità.pdf#page=9|p. 9]], [[Probabilità.pdf#page=11|p. 11]], [[Probabilità.pdf#page=13|p. 13]]

- $P(A\cup B) = P(A)+P(B)-P(AB)$ — [[spazio-di-probabilita]]
- $P(AB) = P(A|B)P(B)$ — [[probabilita-condizionale]]
- $P(AB) = P(A)P(B)$ se indipendenti — [[probabilita-condizionale]]
- $P(B) = \sum_iP(B|A_i)P(A_i)$ — [[probabilita-totale-e-bayes]]

#### Casi svolti

##### Caso 1 — Esempio 1.4: lancio di un dado · [[Probabilità.pdf#page=4|p. 4]]
**Traccia**: lancio di un dado, il risultato della prova è $\omega = 4$. Stabilire se si verificano $A$ = {pari}, $B$ = {≥ 3}, $C$ = {< 2}, "A e B", "A o C", "A e C".

**Svolgimento:**
$$
\begin{aligned}
\Omega &= \{1,2,3,4,5,6\} \\
A &= \{2,4,6\},\quad B = \{3,4,5,6\},\quad C = \{1\} && \text{esplicito gli insiemi}
\end{aligned}
$$

| Evento | Insieme | $4\in$? | Esito |
|---|---|---|---|
| $A$ | $\{2,4,6\}$ | sì | si verifica |
| $B$ | $\{3,4,5,6\}$ | sì | si verifica |
| $C$ | $\{1\}$ | no | non si verifica |
| $A$ e $B$ | $A\cap B = \{4,6\}$ | sì | si verifica |
| $A$ o $C$ | $A\cup C = \{1,2,4,6\}$ | sì | si verifica |
| $A$ e $C$ | $A\cap C = \emptyset$ | no | non si verifica (mai: $A$ e $C$ sono mutuamente esclusivi) |

**Risultato:** coincide con la slide.

> 🧩 Estensione mia — con dado equo: $P(A) = 3/6 = 1/2$, $P(B) = 4/6 = 2/3$, $P(AB) = 2/6 = 1/3 = P(A)P(B)$. Quindi $A$ e $B$ sono **indipendenti**, mentre $A$ e $C$ (disgiunti, a probabilità non nulla) sono **dipendenti**.

##### Caso 2 — Esempio 2.3: estrazione di due palle · [[Probabilità.pdf#page=9|p. 9]]
**Traccia**: «estrazione di una coppia di palle da una scatola contenente tre palle bianche e due rosse — soluzione combinatoria vs. soluzione con probabilità condizionale».

> ❓ Salto non ricostruito: la slide **non** dice quale evento calcolare né se l'estrazione è con o senza reinserimento; la soluzione era alla lavagna. Svolgo il caso più tipico: **senza reinserimento**, evento $E$ = {entrambe bianche}. Da verificare con gli appunti della lezione.

> 🧩 Derivazione mia

**Soluzione combinatoria:** coppie non ordinate equiprobabili.
$$
\begin{aligned}
|\Omega| &= \tbinom52 = \frac{5\cdot4}{2} = 10 && \text{coppie possibili} \\
|E| &= \tbinom32 = 3 && \text{coppie di bianche} \\
P(E) &= \frac{3}{10} = 0.3
\end{aligned}
$$

**Soluzione con probabilità condizionale:** $B_1$ = {1ª bianca}, $B_2$ = {2ª bianca}.
$$
\begin{aligned}
P(E) &= P(B_1B_2) = P(B_2|B_1)\,P(B_1) && \text{prob. composta, condiziono sulla 1ª estrazione} \\
P(B_1) &= 3/5 && \text{3 bianche su 5} \\
P(B_2|B_1) &= 2/4 && \text{restano 2 bianche su 4} \\
P(E) &= \frac35\cdot\frac24 = \frac{6}{20} = 0.3
\end{aligned}
$$
**Sanity check:** i due metodi coincidono ✓. Casi complementari (🧩): $P$(entrambe rosse) $= \binom22/10 = 0.1$, $P$(una per colore) $= 3\cdot2/10 = 0.6$; totale $0.3+0.1+0.6 = 1$ ✓.

##### Caso 3 — Esempio 2.6: moneta lanciata due volte · [[Probabilità.pdf#page=11|p. 11]]
**Traccia**: «lancio di una moneta due volte» come esempio di indipendenza.

> ❓ Salto non ricostruito: la slide dà solo il titolo, senza gli eventi. Svolgo il caso standard.

> 🧩 Derivazione mia
$$
\begin{aligned}
\Omega &= \{TT, TC, CT, CC\},\ \text{equiprobabili } (1/4) && \text{moneta equa} \\
A &= \{\text{T al 1° lancio}\} = \{TT,TC\},\ P(A) = 1/2 \\
B &= \{\text{T al 2° lancio}\} = \{TT,CT\},\ P(B) = 1/2 \\
P(AB) &= P(\{TT\}) = 1/4 = P(A)P(B) && \Rightarrow \text{indipendenti}
\end{aligned}
$$
**Commento:** l'indipendenza qui *discende* dall'equiprobabilità dei 4 risultati. Di solito si procede al contrario: si **assume** che i lanci siano indipendenti e se ne deduce $P(\{TT\}) = 1/4$.

##### Caso 4 — Esempio 2.2 (qualitativo) · [[Probabilità.pdf#page=7|p. 7]]
**Traccia**: $A$ = {piove}; confrontare $P(A|B)$ e $P(A)$ con $B$ = {estate} e $B$ = {inverno}.
**Risultato** (dalla slide): $P(A|\text{estate})<P(A)$, quindi $A$ è "respinto" dall'estate; $P(A|\text{inverno})>P(A)$, quindi $A$ è "attratto" dall'inverno.

#### Trappole · [[Probabilità.pdf#page=8|p. 8]], [[Probabilità.pdf#page=12|p. 12]]

- **Disgiunti ≠ indipendenti**: due eventi disgiunti a probabilità non nulla sono sempre *dipendenti* ([[probabilita-condizionale]]).
- $P(A|B)\neq P(B|A)$ in generale: i denominatori sono diversi.
- Per tre eventi, $P(ABC) = P(A)P(B)P(C)$ **non basta** per l'indipendenza: servono anche le coppie.
- Nel metodo combinatorio, contare in modo coerente: o tutto ordinato o tutto non ordinato.
- Nella probabilità totale, verificare che le cause siano una **partizione**.

### CDF e pdf di variabili aleatorie notevoli e trasformate · [[cdf-pdf-variabili-notevoli|pagina]]

#### Metodo

**V.a. discreta** con DF $p(x_i) = p_i$ ([[variabile-aleatoria]]):
1. CDF: somma di gradini, $F(x) = \sum_ip_i\,u(x-x_i)$, costante a tratti con salti di ampiezza $p_i$ in $x_i$;
2. pdf: derivata generalizzata, $f(x) = \sum_ip_i\,\delta(x-x_i)$;
3. verifica: $\sum_ip_i = 1$.

**V.a. continua** con pdf $f$:
1. CDF: $F(x) = \int_{-\infty}^xf$, **spezzando** l'integrale nei tratti in cui $f$ cambia espressione;
2. verifica: $F(-\infty)=0$, $F(+\infty)=1$, $F$ continua.

**Funzione di v.a.** $Y=g(X)$ ([[funzione-di-variabile-aleatoria]]):
1. radici $x_i(y)$ di $g(x)=y$;
2. $f_Y(y) = \sum_if_X(x_i)/|g'(x_i)|$;
3. controllo con media e varianza ($E(aX+b) = aE(X)+b$, $\text{Var}(aX+b) = a^2\text{Var}(X)$).

#### Formule usate · [[Probabilità.pdf#page=16|p. 16]], [[Probabilità.pdf#page=18|p. 18]]–[[Probabilità.pdf#page=20|20]], [[Probabilità.pdf#page=22|p. 22]], [[Probabilità.pdf#page=24|p. 24]], [[Probabilità.pdf#page=27|p. 27]]

- Definizioni di CDF, pdf, DF → [[variabile-aleatoria]]
- DF Bernoulli e Binomiale, pdf Uniforme → [[variabili-aleatorie-notevoli]]
- $f_Y = \sum f_X(x_i)/|g'(x_i)|$ → [[funzione-di-variabile-aleatoria]]
- CDF gaussiana con erf → [[variabile-aleatoria-gaussiana]]

#### Casi svolti

##### Caso 1 — CDF e pdf della Bernoulli · [[Probabilità.pdf#page=20|p. 20]]
**Traccia**: $X\sim\text{Bern}(p)$, «Calcolare CDF e pdf».
> 🧩 Derivazione mia (esercizio lasciato al lettore)
$$
\begin{aligned}
F(x) = P(X\le x) &= \begin{cases}0 & x<0 && \text{nessun valore} \le x\\ q & 0\le x<1 && \text{solo } X=0\\ q+p = 1 & x\ge1 && \text{entrambi}\end{cases} \\
&= q\,u(x) + p\,u(x-1) && \text{forma compatta con gradini} \\
f(x) = \frac{dF}{dx} &= q\,\delta(x) + p\,\delta(x-1) && \frac{d}{dx}u(x-x_0) = \delta(x-x_0)
\end{aligned}
$$
**Sanity check:** salto $q$ in 0 e $p$ in 1, che sommano a 1 ✓; $F$ continua da destra ✓ (con $u(0) = 1$).

##### Caso 2 — CDF e pdf della Binomiale · [[Probabilità.pdf#page=21|p. 21]]
**Traccia**: $X\sim\mathcal{B}(n,p)$, «Calcolare CDF e pdf»; verificare la normalizzazione.
> 🧩 Derivazione mia
$$
\begin{aligned}
F(x) &= \sum_{k\le x}p(k) = \sum_{k=0}^{\lfloor x\rfloor}\tbinom nkp^kq^{n-k} \quad (0\le x<n) && \text{prop. 2 della DF} \\
&= \sum_{k=0}^n\tbinom nkp^kq^{n-k}\,u(x-k) && \text{forma con gradini, valida } \forall x \\
f(x) &= \sum_{k=0}^n\tbinom nkp^kq^{n-k}\,\delta(x-k) \\
\sum_{k=0}^np(k) &= (p+q)^n = 1 && \text{binomio di Newton}
\end{aligned}
$$
**Esempio numerico** (🧩 mio): $n = 3$, $p = 0.5$: $p(k) = \binom3k/8 = 1/8, 3/8, 3/8, 1/8$ per $k = 0,1,2,3$. CDF: $1/8$, $1/2$, $7/8$, $1$ ✓.

##### Caso 3 — CDF dell'Uniforme ed esempio del bus · [[Probabilità.pdf#page=22|p. 22]]
**Traccia**: $X\sim\mathcal{U}(a,b)$, ricavare la CDF per integrazione; bus tra le 10:00 e le 10:15.
**Svolgimento:** derivazione completa in [[variabili-aleatorie-notevoli]]:
$$F(x) = 0\ (x<a),\quad\frac{x-a}{b-a}\ (a\le x<b),\quad1\ (x\ge b)$$
**Numeri:** 15 min × 60 s/min = 900 s, quindi $X\sim\mathcal{U}(0,900\,\text{s})$ ✓. Probabilità di attendere al più 5 min (🧩): $F(300\,\text{s}) = 300/900 = 0.333$.

##### Caso 4 — $Y = aX+b$ con $X$ gaussiana standard · [[Probabilità.pdf#page=27|p. 27]]
**Traccia**: $X\sim\mathcal{N}(0,1)$, calcolare la pdf di $Y = aX+b$.
**Svolgimento:** vedi [[funzione-di-variabile-aleatoria]] (derivazione passo-passo).
**Risultato:** $f_Y(y) = \frac{1}{\sqrt{2\pi a^2}}e^{-(y-b)^2/(2a^2)}$, cioè $Y\sim\mathcal{N}(b,|a|)$.

##### Caso 5 — CDF gaussiana standard in Matlab · [[Probabilità.pdf#page=26|p. 26]]
**Traccia**: rappresentare la CDF di $\mathcal{N}(0,1)$.
**Svolgimento:** con $\mu=0$, $\sigma=1$ la formula $F(x) = \frac12[1+\text{erf}(\frac{x-\mu}{\sqrt2\sigma})]$ diventa `y = (1/2)*(1+erf(x/sqrt(2)))`.
**Sanity check** (🧩 mio): $F(0) = \frac12(1+0) = 0.5$, per simmetria ✓; $F(3)\approx1-Q(3)\approx0.99865$.

#### Trappole · [[Probabilità.pdf#page=18|p. 18]]

- **Estremi di integrazione** nella CDF di pdf definite a tratti: per $x\ge b$ l'integrale si ferma a $b$, non a $x$.
- **Impulsi** negli estremi: $P(x_1<X\le x_2) = \int_{x_1}^{x_2}f$ vale solo se si gestiscono gli eventuali impulsi in $x_1$ e $x_2$.
- Nella formula di $f_Y$ il modulo $|g'|$ è necessario: senza, per $a<0$ la pdf verrebbe negativa.
- La notazione $\mathcal{N}(\mu,\sigma)$ delle slide usa $\sigma$, **non** $\sigma^2$.
- Per le v.a. discrete la pdf esiste solo in senso generalizzato (con le $\delta$).


---

## Lezione 3 — Campionamento e conversione A/D e D/A

### Conversione A/D e D/A · [[conversione-ad-da|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=3|p. 3]], [[Campionamento_AD_DA.pdf#page=5|p. 5]], [[Campionamento_AD_DA.pdf#page=6|6]]

- **Convertitore A/D**: trasforma un segnale analogico (continuo nel tempo e nell'ampiezza) in un segnale **digitale** (discreto nel tempo e nell'ampiezza).
- **Convertitore D/A**: esegue la trasformazione inversa.

La conversione **A/D** comprende due operazioni distinte:
1. **campionamento**: discretizzazione dei tempi, da tempo continuo a tempo discreto → [[teorema-del-campionamento]];
2. **quantizzazione**: discretizzazione delle ampiezze, da ampiezza continua a discreta → [[quantizzazione-uniforme]].

La conversione **D/A** esegue **una sola** operazione:
- **interpolazione**: da tempo discreto a tempo continuo → [[interpolazione]].

#### Formule · [[Campionamento_AD_DA.pdf#page=5|p. 5]], [[Campionamento_AD_DA.pdf#page=6|6]], [[Campionamento_AD_DA.pdf#page=8|p. 8]], [[Campionamento_AD_DA.pdf#page=26|p. 26]]

Schema (🧩 mia sintesi di p. 5):
$$
x_a(t) \xrightarrow{\ \text{campion.}\ } x(n) = x_a(nT_c) \xrightarrow{\ \text{quantizz.}\ } x_q(n) = Q[x(n)] \xrightarrow{\ \text{codifica}\ } \text{bit}
\;\;\cdots\;\;
x_q(n) \xrightarrow{\ \text{interpolaz.}\ } x_r(t)
$$

Anche con un campionamento perfettamente reversibile, la cascata A/D + D/A dà $x_r(t)\neq x_a(t)$ a causa della quantizzazione.

#### Derivazioni

Nessun risultato numerico in questa parte. Le derivazioni sono nelle pagine dei singoli stadi.

#### Spiegazione · [[Campionamento_AD_DA.pdf#page=5|p. 5]], [[Campionamento_AD_DA.pdf#page=6|6]]

![[campionamento-p5-conversione-ad.png]]
*Convertitore A/D: $x_a(t)$ → campionatore (comandato da $T_c$) → $x(n)$ → quantizzatore → $x_q(n)$.*

![[campionamento-p6-conversione-da.png]]
*Convertitore D/A: $x_q(n)$ → interpolatore (comandato da $T_c$) → $x_r(t)$.*

##### Invertibilità · [[Campionamento_AD_DA.pdf#page=5|p. 5]]

- Il **campionamento** è invertibile *sotto opportune ipotesi*: è il contenuto del [[teorema-del-campionamento]].
- La **quantizzazione** è **irreversibile**: più ampiezze vengono mappate sullo stesso livello e l'informazione persa non si recupera.

> 🎯 Esame: perché la D/A ha una sola operazione? Perché la quantizzazione non si può invertire: si può solo interpolare i campioni quantizzati.

##### Dall'elaborazione analogica a quella digitale · Campionamento [[Campionamento_AD_DA.pdf#page=2|p. 2]]–[[Campionamento_AD_DA.pdf#page=4|4]] · Intro [[Intro.pdf#page=13|p. 13]]

- I fenomeni fisici evolvono **con continuità** nel tempo e nell'ampiezza, quindi sono rappresentati da **segnali analogici**.
- Le prime elaborazioni dei segnali erano **analogiche**:
  - richiedevano il progetto e la realizzazione di un circuito elettrico/elettronico;
  - processo lungo, costoso e poco flessibile.
- Oggi l'elaborazione dei segnali si fa con **tecniche digitali**.
- Per essere elaborato, memorizzato o trasmesso digitalmente, un segnale analogico va trasformato in un **segnale digitale** (discreto nel tempo e nell'ampiezza).
- In molti casi serve anche la **trasformazione inversa**, da digitale ad analogico.

![[campionamento-p2-analogico-digitale.png]]
*Esempio di elaborazione analogica: un circuito passivo (induttori, condensatori, resistori) che divide il segnale fra tweeter e woofer. Ogni funzione richiede un circuito progettato apposta.*

![[campionamento-p3-dispositivi-digitali.png]]
*Elaborazione digitale di un segnale analogico: $x_a(t)$ → **A/D** → $x_q(n)$ → **DSP** → $y_q(n)$ → **D/A** → $y_a(t)$. Visto dall'esterno, l'insieme si comporta come un "sistema analogico" (riquadro tratteggiato).*

Due dispositivi di conversione fondamentali: convertitore **A/D** (segnale analogico → digitale) e convertitore **D/A** (segnale digitale → analogico). L'elaborazione avviene con **sistemi digitali**, realizzabili con diverse tecnologie:
- ASIC (application-specific integrated circuit)
- DSP (digital signal processor)
- FPGA (field-programmable gate array)
- microcontrollori (es. Atmel, STM)
- microprocessori general purpose (es. Intel, AMD)

L'elaborazione digitale è un **algoritmo** che si può tradurre in codice ed eseguire via software.

**Vantaggi**:
- **Programmabilità / versatilità / sviluppo rapido**: un dispositivo digitale si programma per un determinato compito e si riprogramma facilmente per un altro (*software upgrade*).
- **Stabilità / riproducibilità**: i risultati sono stabili nel tempo e riproducibili; dispositivi diversi che eseguono lo stesso programma danno gli stessi risultati.
- **Potenzialità**: si possono implementare algoritmi complessi non realizzabili in analogico (es. crittografia, correzione/rivelazione di errori, compressione dati).
- **Costi**: i dispositivi digitali si producono facilmente in grandi quantità e a basso costo.

> 💡 Connessione: sono gli stessi argomenti di "going digital" in [[sistema-comunicazione-digitale]], visti dal lato dell'elaborazione invece che della trasmissione.

#### Perché importa · [[Intro.pdf#page=15|p. 15]]

Il convertitore A/D è il primo stadio del codificatore di sorgente per sorgenti analogiche. Il suo dimensionamento ($f_c$, $b$) fissa il bit rate da trasmettere: $R_b = b\cdot f_c$ ([[dimensionamento-quantizzatore]]).

#### Connessioni

- [[laboratorio-conversione-ad]] — 🧪 laboratorio Matlab (non d'esame) che percorre tutta la catena: [[lab-setup-e-spettro]], [[lab-campionamento]], [[lab-interpolazione]], [[lab-quantizzazione]], [[lab-snr]].
- [[teorema-del-campionamento]], [[aliasing]], [[interpolazione]] — dimensione temporale.
- [[quantizzazione-uniforme]], [[snr-di-quantizzazione]], [[quantizzazione-non-uniforme]], [[companding]] — dimensione delle ampiezze.
- [[sistema-comunicazione-digitale]] — la collocazione nella catena di trasmissione.

#### Fonti · [[Campionamento_AD_DA.pdf#page=2|p. 2]], [[Campionamento_AD_DA.pdf#page=6|p. 6]]

- [[campionamento-conversione-ad-da]]

### Teorema del campionamento (teorema di Shannon) · [[teorema-del-campionamento|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=7|p. 7]], [[Campionamento_AD_DA.pdf#page=8|8]], [[Campionamento_AD_DA.pdf#page=14|p. 14]]

**Campionamento uniforme**: campionare un segnale a tempo continuo $x_a(t)$ significa estrarne i valori in istanti discreti di tempo, generalmente equispaziati di $T_c$ (**periodo di campionamento**).

![[campionamento-p7-campionamento-uniforme.png]]
*(a) Segnale TC $x_a(t)$ con i valori $x_a(nT_c)$ negli istanti $nT_c$; (b) segnale TD $x(n)$, sequenza indicizzata da $n$ intero*

**Relazione ingresso-uscita del campionatore**: la descrizione matematica è semplice,
$$x(n) = x_a(nT_c)$$
- $T_c$ = **periodo di campionamento**, in secondi (s) o sottomultipli;
- $f_c = 1/T_c$ = **frequenza di campionamento**, in Hertz (Hz) o multipli, a volte in campioni/s;
- il blocco che esegue l'operazione si chiama **sistema campionatore**: ingresso $x_a(t)$, uscita $x(n)$, comandato da $T_c$.

**Problema fondamentale**: scegliere in modo appropriato $f_c = 1/T_c$ per un dato segnale $x_a(t)$.

![[campionamento-p8-campionatore.png]]

![[campionamento-p14-teorema-shannon.png]]
*Spettro $X_a(f)$ di un segnale a banda rigorosamente limitata: nullo fuori da $[-f_m, f_m]$ (disegnato triangolare, di altezza 1)*

> 🧮 Formula chiave — **Teorema del campionamento**
> **Ipotesi:** $x_a(t)$ a banda **rigorosamente limitata** con banda monolatera $B_x = f_m$; $f_c = 1/T_c \ge 2f_m$; $x(n) = x_a(nT_c)$.
> **Tesi:** $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n)$.
> La minima frequenza di campionamento $f_{c,\min} = 2f_m$ è la **frequenza di Nyquist** di $x_a(t)$.

#### Formule · [[Campionamento_AD_DA.pdf#page=11|p. 11]]–[[Campionamento_AD_DA.pdf#page=13|13]], [[Campionamento_AD_DA.pdf#page=15|p. 15]]

| Formula | Significato |
|---|---|
| $x_\delta(t) = x_a(t)\sum_n\delta(t-nT_c) = \sum_n x_a(nT_c)\,\delta(t-nT_c)$ | segnale campionato idealmente |
| $\sum_n\delta(t-nT_c) \xleftrightarrow{FT} \frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)$ | trasformata del pettine di delta |
| $X_\delta(f) = \frac{1}{T_c}\sum_{k=-\infty}^{+\infty}X_a\left(f-\frac{k}{T_c}\right)$ | spettro periodico, periodo $f_c$ |
| $f_c \ge 2f_m$ | condizione di Nyquist |
| $H_r(f) = T_c\,\Pi\left(\frac{f}{2f_r}\right)$, $f_m\le f_r\le f_c-f_m$ | filtro di ricostruzione (LPF ideale) |

Simboli: $\delta(\cdot)$ = impulso di Dirac; $\Pi(x)$ = rettangolo unitario (1 per $|x|<1/2$); $X_a(f)$ = trasformata di Fourier di $x_a(t)$; $f_r$ = frequenza di taglio del filtro [Hz].

#### Derivazioni

##### Derivazione — Forma del segnale campionato idealmente · [[Campionamento_AD_DA.pdf#page=11|p. 11]]
$$
\begin{aligned}
x_\delta(t) &= x_a(t)\sum_n\delta(t-nT_c) && \text{1° stadio: prodotto per il pettine} \\
&= \sum_n x_a(t)\,\delta(t-nT_c) && \text{linearità} \\
&= \sum_n x_a(nT_c)\,\delta(t-nT_c) && \text{proprietà del campionamento della } \delta:\ g(t)\delta(t-t_0) = g(t_0)\delta(t-t_0)
\end{aligned}
$$

##### Derivazione — Trasformata del pettine di delta · [[Campionamento_AD_DA.pdf#page=12|p. 12]]
> 🧩 Derivazione mia (richiamo di teoria dei segnali)
$$
\begin{aligned}
\textstyle\sum_n\delta(t-nT_c) &= \textstyle\sum_k c_k\,e^{j2\pi k t/T_c} && \text{segnale periodico di periodo } T_c \Rightarrow \text{serie di Fourier} \\
c_k &= \frac{1}{T_c}\int_{-T_c/2}^{T_c/2}\delta(t)\,e^{-j2\pi kt/T_c}dt = \frac{1}{T_c} && \text{nel periodo c'è solo } \delta(t) \\
\textstyle\sum_n\delta(t-nT_c) &= \frac{1}{T_c}\textstyle\sum_k e^{j2\pi kf_ct} \xleftrightarrow{FT} \frac{1}{T_c}\textstyle\sum_k\delta(f-kf_c) && e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)
\end{aligned}
$$

##### Derivazione — Spettro del segnale campionato · [[Campionamento_AD_DA.pdf#page=12|p. 12]]
$$
\begin{aligned}
X_\delta(f) &= X_a(f) * \left[\frac{1}{T_c}\sum_k\delta\left(f-\frac{k}{T_c}\right)\right] && \text{prodotto nel tempo} \leftrightarrow \text{convoluzione in frequenza} \\
&= \frac{1}{T_c}\sum_k X_a(f)*\delta(f-kf_c) && \text{linearità} \\
&= \frac{1}{T_c}\sum_k X_a(f-kf_c) && X*\delta(f-f_0) = X(f-f_0)
\end{aligned}
$$
Il risultato è la **replicazione** di $X_a(f)$ con passo $f_c = 1/T_c$ e ampiezza scalata di $1/T_c$: uno spettro **periodico** di periodo $f_c$.

Conseguenze tratte dalla slide:
- l'invertibilità del campionamento equivale a stabilire **quando $X_a(f)$ si può ottenere univocamente dalla sua replicazione** con passo $f_c$;
- in generale la relazione tra "generatore" e replicazione **non è univoca**: generatori diversi possono dare la stessa replicazione;
- per questo si **assume** che $x_a(t)$ sia a **banda rigorosamente limitata**, con banda monolatera $B_x = f_m$, e si studia il problema **graficamente** al variare di $f_c$ (i tre casi qui sotto).

##### Derivazione — Condizione $f_c\ge2f_m$ · [[Campionamento_AD_DA.pdf#page=13|p. 13]]
> 🧩 Derivazione mia (traduzione algebrica della figura)
$$
\begin{aligned}
\text{supp}\,X_a &= [-f_m, f_m] && \text{banda rigorosamente limitata} \\
\text{supp}\,X_a(f-kf_c) &= [kf_c - f_m,\ kf_c+f_m] && \text{replica } k \\
\text{no sovrapposizione tra replica 0 e 1} &\iff f_m \le f_c - f_m && \text{estremo destro di 0} \le \text{estremo sinistro di 1} \\
&\iff f_c \ge 2f_m
\end{aligned}
$$
Per simmetria e periodicità basta controllare repliche adiacenti.

![[campionamento-p13-tre-casi-campionamento.png]]
*I tre casi: (a) $f_c>2f_m$, repliche separate da una banda di guardia $f_c-2f_m$; (b) $f_c=2f_m$, repliche che si toccano in $f_c/2$; (c) $f_c<2f_m$, repliche sovrapposte ([[aliasing]]).*

##### Derivazione — Caso limite: un coseno campionato esattamente a $f_c = 2f_0$ · [[Campionamento_AD_DA.pdf#page=13|p. 13]], [[Campionamento_AD_DA.pdf#page=14|14]], [[Campionamento_AD_DA.pdf#page=17|p. 17]]
> 🧩 Esempio e derivazione miei: approfondiscono il caso (b) della figura sopra, $f_c = 2f_m$, che il teorema ammette con il "$\ge$".

**Domanda:** $x(t) = \cos(2\pi f_0 t + \varphi)$, per esempio con $f_0 = \pi$ Hz, campionato alla frequenza di Nyquist $f_c = 2f_0 = 2\pi$ Hz, cioè $T_c = \frac{1}{2f_0}$. Si perde informazione? L'interpolazione ideale restituisce $x(t)$?

**I campioni:**
$$
\begin{aligned}
x(n) &= \cos\Big(2\pi f_0\,\frac{n}{2f_0} + \varphi\Big) && t = nT_c = \frac{n}{2f_0} \\
&= \cos(\pi n + \varphi) && \text{il coseno fa mezzo periodo tra un campione e l'altro} \\
&= \cos(\pi n)\cos\varphi - \sin(\pi n)\sin\varphi && \text{formula di addizione} \\
&= (-1)^n\cos\varphi && \cos(\pi n) = (-1)^n,\ \sin(\pi n) = 0
\end{aligned}
$$
La parte in $\sin\varphi$ sparisce: i campioni cadono sempre dove il seno vale zero. Dai campioni si legge **solo** $\cos\varphi$, non $\varphi$.

**La ricostruzione ideale** (serie di Shannon) con questi campioni dà:
$$x_r(t) = \sum_n (-1)^n\cos\varphi\ \text{sinc}\Big(\frac{t - nT_c}{T_c}\Big) = \cos\varphi\,\cos(2\pi f_0 t)$$
Il secondo passaggio usa l'identità $\sum_n (-1)^n\,\text{sinc}(x - n) = \cos(\pi x)$, verificata numericamente (scarto $< 10^{-4}$).

**Cosa succede al variare della fase:**
- **$\varphi = 0$** (coseno "puro"): i campioni cadono sui picchi, $\pm 1$, e $x_r(t) = \cos(2\pi f_0 t) = x(t)$. **Ricostruzione perfetta**, ma per una coincidenza di fase.
- **$\varphi = 45°$:** $x_r(t) = 0.71\cos(2\pi f_0 t)$. Ampiezza sbagliata e fase persa: il ricostruito è un coseno con fase 0, non $45°$.
- **$\varphi = 90°$**, cioè $x(t) = -\sin(2\pi f_0 t)$: tutti i campioni valgono 0 e $x_r(t) = 0$. **Il segnale sparisce del tutto.**

**Il perché in frequenza.** $x(t)$ ha due righe: $\frac{1}{2}e^{j\varphi}$ in $+f_0$ e $\frac{1}{2}e^{-j\varphi}$ in $-f_0$. Campionando, lo spettro si replica ogni $f_c = 2f_0$. La replica della riga in $-f_0$ finisce in $-f_0 + f_c = +f_0$: **esattamente sopra** la riga in $+f_0$. Le repliche "si toccano" proprio dove sta il segnale, e le due righe si sommano:
$$\tfrac{1}{2}e^{j\varphi} + \tfrac{1}{2}e^{-j\varphi} = \cos\varphi$$
Resta un numero reale: la fase è persa. È una forma di aliasing al bordo della banda.

![[grafico-nyquist-limite-coseno.gif]]
*🧩 Animazione mia (script `output/grafici/genera_grafici_nyquist_limite.py`): $f_0 = \pi$ Hz, $f_c = 2\pi$ Hz, fase $\varphi$ che va da $0°$ a $180°$.*
- *In alto: il segnale (grigio), i campioni (arancio) e il ricostruito ideale (blu). A $0°$ coincidono; a $90°$ i campioni sono tutti nulli e il ricostruito è piatto; a $180°$ il ricostruito torna intero perché $\cos\varphi = -1$ e il segnale è $-\cos(2\pi f_0 t)$.*
- *In basso a sinistra: i due fasori in $f_c/2$ (blu $\frac12 e^{j\varphi}$, verde $\frac12 e^{-j\varphi}$) e la loro somma (rosso), sempre sull'asse reale.*
- *In basso a destra: l'ampiezza ricostruita $\cos\varphi$ contro quella vera, 1.*

**Conclusione:**
- campionando un coseno esattamente a $2f_0$ **si perde informazione**: la fase, e con lei l'ampiezza apparente;
- l'interpolazione ideale restituisce il segnale di partenza **solo se** $\varphi = 0$ o $\varphi = \pi$, cioè se i campioni cadono sui picchi;
- per una sinusoide (o qualunque riga spettrale) proprio a $f_m$ serve $f_c > 2f_m$ **strettamente**.

Il "$\ge$" del teorema resta valido per segnali con spettro **continuo**: lì il punto $f = f_m$ ha energia nulla, e la sovrapposizione in un solo punto non conta. Diventa un problema solo quando c'è una riga, cioè una delta, proprio sul bordo. In pratica il caso limite si evita comunque sovracampionando (sezione «Effetti pratici» sotto).

**Ipotesi:** campionamento ideale e interpolatore ideale a durata infinita; nessun rumore.

##### Derivazione — Ricostruzione perfetta con LPF ideale · [[Campionamento_AD_DA.pdf#page=15|p. 15]]
$$
\begin{aligned}
X_r(f) &= H_r(f)\,X_\delta(f) = T_c\,\Pi\!\left(\tfrac{f}{2f_r}\right)\cdot\frac{1}{T_c}\sum_k X_a(f-kf_c) && \text{filtraggio LTI} \\
&= \Pi\!\left(\tfrac{f}{2f_r}\right)\sum_kX_a(f-kf_c) && T_c \text{ compensa } 1/T_c \\
&= X_a(f) && \text{se } f_r\ge f_m \text{ (passa la replica 0) e } f_r\le f_c-f_m \text{ (blocca la replica } \pm1)
\end{aligned}
$$
L'intervallo $[f_m,\,f_c-f_m]$ non è vuoto solo se $f_c\ge2f_m$. Scelta comune: $f_r = f_c/2$, il centro dell'intervallo.

![[campionamento-p15-filtro-ricostruzione.png]]
*Ricostruzione del segnale TC: (a) $X_\delta(f)$, repliche di altezza $1/T_c$ centrate in $0, \pm f_c, \dots$; (b) $H_r(f)$, rettangolo di altezza $T_c$ tra $-f_c/2$ e $f_c/2$; (c) $X_r(f) = X_a(f)$, la sola replica centrale riportata ad altezza 1.*
**Sanity check:** con $f_c = 2f_m$ l'intervallo si riduce al punto $f_r = f_m = f_c/2$ e il filtro deve essere perfettamente ideale.
**Ipotesi:** banda rigorosamente limitata; campionamento e filtro ideali (vedi [[aliasing]] e [[interpolazione]] per i casi reali).

#### Spiegazione

##### Intuizione · [[Campionamento_AD_DA.pdf#page=9|p. 9]], [[Campionamento_AD_DA.pdf#page=10|10]]

**Scelta di $f_c$**: è fondamentale per avere una buona rappresentazione del segnale e per poterlo ricostruire dai campioni a tempo discreto.
- $T_c$ **troppo grande** per un segnale che varia rapidamente (larga banda): i campioni non seguono le oscillazioni.
- $T_c$ **adeguato** per un segnale che varia lentamente (banda stretta): i campioni descrivono bene l'andamento.
- Quindi $f_c = 1/T_c$ va scelta **proporzionale alla rapidità di variazione** del segnale nel tempo, o equivalentemente alla sua **banda** in frequenza. È l'osservazione intuitiva alla base del teorema del campionamento.

![[campionamento-p9-scelta-fc.png]]

**Invertibilità del campionamento**: dai campioni $x(n)$ si può ricostruire il segnale TC originale $x_a(t)$?
- A prima vista **no**: esistono **infiniti** segnali TC che hanno gli stessi campioni $x(n)$ (es. $x_{a1}(t)$ e $x_{a2}(t)$ in figura), quindi servono condizioni aggiuntive.
- Con **ulteriori assunzioni** su $x_a(t)$ e una **scelta opportuna** di $f_c = 1/T_c$, $x_a(t)$ si ricostruisce **perfettamente** dai campioni $x(n) = x_a(nT_c)$.
- Questo risultato fondamentale è la tesi del **teorema del campionamento**, o **teorema di Shannon**.

![[campionamento-p10-invertibilita.png]]

##### Modello a due stadi · [[Campionamento_AD_DA.pdf#page=11|p. 11]]

Per dimostrare il teorema conviene schematizzare il campionamento in **due stadi**:
1. $x_a(t)$ viene moltiplicato per un **pettine di delta** $\Delta_{T_c}(t)$ di periodo $T_c$, e si ottiene $x_\delta(t)$ (ancora TC);
2. da $x_\delta(t)$ si estraggono i campioni $x(n) = x(nT_c)$: nello schema è il blocco "convertitore $\delta/n$", che trasforma il treno di impulsi nella sequenza.

È un modello utile per lo studio matematico, **senza alcun riscontro pratico**. Il segnale TC $x_\delta(t)$ si chiama **campionamento ideale**. Studiare l'invertibilità del campionamento equivale a studiare quella del **primo stadio**, perché il secondo è solo un cambio di rappresentazione.

![[campionamento-p11-campionamento-ideale.png]]
*Schema a due stadi e segnale $x_\delta(t)$: impulsi negli istanti $nT_c$, con aree pari ai campioni (inviluppo tratteggiato = $x_a(t)$)*

##### Effetti pratici · [[Campionamento_AD_DA.pdf#page=16|p. 16]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]

$f_c$ cresce **linearmente** con la banda:

| Segnale | $f_m$ | $f_c \ge 2f_m$ |
|---|---|---|
| Voce | 4 kHz | 8 kHz |
| Audio | 20 kHz | 40 kHz |
| Video | 5 MHz | 10 MHz |

Al crescere di $f_c$ crescono il **costo dell'hardware** (campionatore) e il **numero di campioni** generati (ingombro di memoria).

**Esempio**: 1 minuto di audio mono campionato a $f_c = 44.1$ kHz corrisponde a $60\times44\,100 = 2\,646\,000$ campioni. Il valore **raddoppia** per un segnale stereo (canali L e R). Svolgimento in [[campionamento-e-aliasing]].

**Sovracampionamento** (*oversampling*): campionare con $f_c$ maggiore della frequenza di Nyquist. Non conviene per complessità e costo, ma può essere vantaggioso contro alcuni problemi pratici. Per esempio riduce l'aliasing dei segnali a banda non rigorosamente limitata (vedi [[aliasing]]).

> 🎯 Esame: enunciato completo con ipotesi e tesi; dimostrazione grafica/spettrale; ruolo del guadagno $T_c$ del filtro; perché $f_r\in[f_m, f_c-f_m]$.

#### Perché importa · [[Campionamento_AD_DA.pdf#page=31|p. 31]]

Stabilisce quanti campioni al secondo servono per rappresentare un segnale senza perdite. Insieme al numero di bit per campione ([[quantizzazione-uniforme]]) fissa il bit rate prodotto dalla conversione A/D.

#### Connessioni · Intro [[Intro.pdf#page=15|p. 15]] · Rice [[Rappresentazione_Rice.pdf#page=9|p. 9]]

- [[lab-campionamento]] — 🧪 laboratorio (non d'esame): campionamento simulato, repliche dello spettro e un caso in cui l'arrotondamento porta $f_s$ sotto $2W$.
- [[aliasing]] — cosa succede quando le ipotesi cadono.
- [[interpolazione]] — la ricostruzione $x_r(t)$ nel dominio del tempo (serie di Shannon).
- [[conversione-ad-da]] — il campionamento è la prima metà della conversione A/D.
- [[sistema-comunicazione-digitale]] — il campionamento è il primo passo della conversione A/D svolta dal codificatore di sorgente.
- [[inviluppo-complesso]] — un segnale passa-banda va campionato a $f_c \ge 2 f_{max}$ (qui $f_{max}$ è la sua frequenza massima), il suo inviluppo complesso a una frequenza molto più bassa; il confronto è ricavato in quella pagina. Attenzione alla notazione: qui $f_c$ è la frequenza di campionamento, là è la portante.

#### Fonti · [[Campionamento_AD_DA.pdf#page=7|p. 7]], [[Campionamento_AD_DA.pdf#page=16|p. 16]]

- [[campionamento-conversione-ad-da]]

### Interpolazione: ideale (serie di Shannon), ZOH, FOH · [[interpolazione|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=6|p. 6]], [[Campionamento_AD_DA.pdf#page=17|p. 17]]

L'**interpolazione** ricostruisce un segnale a tempo continuo $x_r(t)$ dai campioni $x(n)$: è l'unica operazione della conversione D/A. Si modella come il passaggio di $x_\delta(t) = \sum_n x(n)\delta(t-nT_c)$ in un **filtro di ricostruzione** $h_r(t)$:
$$x_r(t) = \sum_{n} x(n)\,h_r(t-nT_c)$$

> 🧩 Derivazione mia (forma generale): $x_r = x_\delta * h_r$ e $\delta(t-nT_c)*h_r(t) = h_r(t-nT_c)$. Le tre interpolazioni seguenti sono casi particolari di questa formula.

#### Formule · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]

| Interpolatore | $h_r(t)$ | $H_r(f)$ | Proprietà |
|---|---|---|---|
| **Ideale** (serie di Shannon) | $\text{sinc}\left(\frac{t}{T_c}\right)$ | $T_c\,\Pi(fT_c)$ | instabile, non causale → **non realizzabile** |
| **ZOH** (mantenimento) | $\Pi\left(\frac{t-T_c/2}{T_c}\right)$ | $T_c\,\text{sinc}(fT_c)\,e^{-j\pi fT_c}$ | stabile e **causale** → realizzabile |
| **FOH** (lineare) | $\Lambda\left(\frac{t}{T_c}\right)$ | $T_c\,\text{sinc}^2(fT_c)$ | stabile, **non causale** → realizzabile con un ritardo di $T_c$ |

Simboli: $\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$; $\Pi(x)$ = rettangolo unitario su $|x|<1/2$; $\Lambda(x) = 1-|x|$ per $|x|\le1$ (triangolo); $T_c$ [s].

> 🧮 Formula chiave — **Serie di Shannon**:
> $$x_r(t) = \sum_{n=-\infty}^{+\infty}x_a(nT_c)\,\text{sinc}\left(\frac{t-nT_c}{T_c}\right)$$

> ⚠️ Contraddizione (refuso nelle slide): p. 24 scrive «First-Order Hold (ZOH)». La sigla corretta è **FOH**.

#### Derivazioni

##### Derivazione — Risposta impulsiva dell'interpolatore ideale · [[Campionamento_AD_DA.pdf#page=17|p. 17]]
$$
\begin{aligned}
H_r(f) &= T_c\,\Pi\left(\tfrac{f}{2f_r}\right),\quad f_r = f_c/2 = \tfrac{1}{2T_c} && \text{scelta comune} \\
&= T_c\,\Pi(fT_c) && 2f_r = 1/T_c \\
\Pi(f/W) &\xleftrightarrow{FT^{-1}} W\,\text{sinc}(Wt) && \text{coppia nota} \\
h_r(t) &= T_c\cdot\tfrac{1}{T_c}\,\text{sinc}\left(\tfrac{t}{T_c}\right) = \text{sinc}\left(\tfrac{t}{T_c}\right) && W = 1/T_c
\end{aligned}
$$
Sostituendo in $x_r(t) = \sum_n x(n)h_r(t-nT_c)$ si ottiene la serie di Shannon.
**Sanity check** (🧩 mio): in $t = mT_c$ si ha $\text{sinc}(m-n) = 1$ se $n=m$ e 0 altrimenti, quindi $x_r(mT_c) = x_a(mT_c)$. L'interpolatore passa esattamente per i campioni.

##### Derivazione — Filtro ZOH · [[Campionamento_AD_DA.pdf#page=23|p. 23]]
$$
\begin{aligned}
\Pi\left(\tfrac{t}{T_c}\right) &\xleftrightarrow{FT} T_c\,\text{sinc}(fT_c) && \text{coppia nota (rettangolo di durata } T_c) \\
\Pi\left(\tfrac{t-T_c/2}{T_c}\right) &\xleftrightarrow{FT} T_c\,\text{sinc}(fT_c)\,e^{-j2\pi f T_c/2} && \text{ritardo di } T_c/2 \\
&= T_c\,\text{sinc}(fT_c)\,e^{-j\pi fT_c}
\end{aligned}
$$
$h_r(t)$ ha supporto $[0, T_c]$, quindi è **causale**; $\int|h_r| = T_c<\infty$, quindi è **stabile** (BIBO).
Nel tempo: $x_r(t) = x(n)$ per $t\in[nT_c,(n+1)T_c)$, cioè ogni campione è mantenuto fino al successivo.

##### Derivazione — Filtro FOH · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]
> 🧩 Derivazione mia
$$
\begin{aligned}
\Pi\left(\tfrac{t}{T_c}\right) * \Pi\left(\tfrac{t}{T_c}\right) &= T_c\,\Lambda\left(\tfrac{t}{T_c}\right) && \text{autoconvoluzione del rettangolo} \\
\Lambda\left(\tfrac{t}{T_c}\right) &= \tfrac{1}{T_c}\,\Pi * \Pi \xleftrightarrow{FT} \tfrac{1}{T_c}\,[T_c\,\text{sinc}(fT_c)]^2 && \text{convoluzione} \leftrightarrow \text{prodotto} \\
&= T_c\,\text{sinc}^2(fT_c)
\end{aligned}
$$
$h_r(t)$ ha supporto $[-T_c, T_c]$, quindi **non causale**: per $t$ tra $nT_c$ e $(n+1)T_c$ serve già il campione $n+1$. Ritardando di $T_c$ (un campione) il filtro diventa causale.
Nel tempo, per $t\in[nT_c,(n+1)T_c]$ contribuiscono solo i due triangoli centrati in $nT_c$ e $(n+1)T_c$, con pesi $1-\tau$ e $\tau$ dove $\tau = (t-nT_c)/T_c$: è l'**interpolazione lineare** tra campioni consecutivi.

**Confronto spettrale** (🧩 mio): fuori banda, $|\text{sinc}^2|$ decresce come $1/f^2$ e $|\text{sinc}|$ come $1/f$. Per questo la FOH ha meno contenuto ad alta frequenza della ZOH.

![[grafico-interpolatori-risposta.png]]
*🧩 Grafico mio delle tre $H_r(f)$ di p. 17, p. 23, p. 24 (moduli, normalizzati a $T_c$). L'ideale passa tutto fino a $f_c/2$ e blocca tutto oltre. ZOH e FOH hanno zeri in $f_c, 2f_c, \dots$, cioè al centro delle repliche, ma lasciano passare i lobi laterali: la ZOH molto (picco ≈ 0.22), la FOH molto meno (≈ 0.05). Entrambe attenuano anche la banda utile: in $f_c/2$ la ZOH vale $\text{sinc}(0.5) = 2/\pi \approx 0.64$, la FOH $(2/\pi)^2 \approx 0.41$. Da qui l'utilità del LPF aggiuntivo dopo lo ZOH.*

#### Spiegazione

##### Interpolazione ideale · [[Campionamento_AD_DA.pdf#page=17|p. 17]]

- La ricostruzione prevista dal teorema del campionamento usa un LPF ideale $H_r(f) = T_c\Pi(f/2f_r)$ con $f_m\le f_r\le f_c-f_m$; scegliendo $f_r = f_c/2$ si ottiene la serie di Shannon.
- L'interpolazione ideale usa segnali **sinc**, che hanno **banda rigorosamente limitata**.
- Non è fisicamente realizzabile: il filtro è **instabile** e **non causale**.

![[campionamento-p17-serie-shannon.png]]
*Serie di Shannon: ogni campione (asta nera) genera una sinc centrata in $nT_c$ e scalata del valore del campione (curve sottili). La loro somma è il segnale ricostruito $x_r(t)$ (rosso), che passa esattamente per tutti i campioni. Asse orizzontale: $t/T_c$.*

##### Perché serve l'interpolazione non ideale · [[Campionamento_AD_DA.pdf#page=19|p. 19]]

L'interpolazione con sinc è una delle **due ipotesi ideali** del teorema di Shannon (l'altra è la banda rigorosamente limitata, vedi [[aliasing]]). Nella pratica va sostituita da interpolatori realizzabili.

##### Interpolazione non ideale in frequenza · [[Campionamento_AD_DA.pdf#page=22|p. 22]]

![[campionamento-p22-interpolazione-non-ideale.png]]

(a) $X_\delta(f)$: repliche di altezza $1/T_c$ con passo $f_c$ (senza sovrapposizione). Un $H_r(f)$ reale (b), di altezza massima $T_c$ (in tratteggio l'ideale su $[-f_c/2, f_c/2]$), non è un rettangolo: la transizione è graduale, quindi attenua in parte la banda utile e lascia passare residui delle repliche intorno a $\pm f_c$. Lo spettro ricostruito $X_r(f)$ (c) contiene così componenti spurie ad alta frequenza.

##### ZOH · [[Campionamento_AD_DA.pdf#page=23|p. 23]]

- Nella pratica il filtro di interpolazione ideale (LPF ideale) **non è fisicamente realizzabile**.
- Un'interpolazione più semplice **mantiene** il valore di un campione fino al campione successivo: è lo **Zero-Order Hold** (ZOH), o **interpolazione a mantenimento**.
- Approssima male il segnale: l'effetto "**scalettatura**" produce un elevato contenuto spettrale ad alta frequenza.
- È un sistema LTI **stabile e causale**, quindi fisicamente realizzabile.
- L'approssimazione si migliora con un ulteriore **filtraggio LPF** del segnale ZOH, che elimina le transizioni brusche e rende il segnale ricostruito più "**dolce**".

![[campionamento-p23-zoh.png]]
*$x_{ZOH}(t)$: gradini di durata $T_c$ che partono da ogni campione, confrontati con il segnale originale tratteggiato*

##### FOH · [[Campionamento_AD_DA.pdf#page=24|p. 24]]

- Una ricostruzione **più accurata** si ottiene interpolando **linearmente** due campioni consecutivi: è il **First-Order Hold** (FOH), o **interpolazione lineare**.
- Approssima meglio il segnale e ha minor contenuto spettrale ad alta frequenza.
- È un sistema LTI **stabile** ma **non causale**; diventa fisicamente realizzabile introducendo un **ritardo di $T_c$** (un campione).

![[campionamento-p24-foh.png]]
*$x_{FOH}(t)$: spezzata che unisce i campioni consecutivi, confrontata con il segnale originale tratteggiato*

> 🎯 Esame: confronto ideale/ZOH/FOH su $h_r$, $H_r$, causalità, stabilità e realizzabilità. Perché la sinc non è realizzabile: è non causale (ha supporto su tutto $\mathbb{R}$) e instabile ($\int|\text{sinc}| = \infty$).
> 📚 Fonte esterna: la non assoluta integrabilità della sinc ($\int|\sin x/x|\,dx$ diverge) è un risultato standard di analisi; la slide dice solo «instabile e non causale».

#### Perché importa · [[Campionamento_AD_DA.pdf#page=6|p. 6]]

È l'unica operazione della conversione D/A. Il passaggio da interpolatore ideale (irrealizzabile) a ZOH/FOH (realizzabili) mostra il compromesso tra fedeltà della ricostruzione e realizzabilità fisica del filtro.

#### Connessioni

- [[lab-interpolazione]] — 🧪 laboratorio (non d'esame): ZOH, FOH e sinc applicati a un trapezio in Matlab; perché la convoluzione dura la somma delle durate e dove va tagliata.
- [[teorema-del-campionamento]] — dimostra che l'interpolazione ideale ricostruisce perfettamente.
- [[aliasing]] — l'altra ipotesi ideale (banda limitata) e le sue violazioni.
- [[conversione-ad-da]] — l'interpolazione è la D/A.

#### Fonti · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=19|p. 19]], [[Campionamento_AD_DA.pdf#page=24|p. 24]]

- [[campionamento-conversione-ad-da]]

### Aliasing e filtraggio antialiasing · [[aliasing|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=18|p. 18]]

L'**aliasing** si verifica quando $f_c$ non soddisfa la condizione del [[teorema-del-campionamento]] ($f_c<2f_m$): le repliche spettrali si **sovrappongono**. Una componente a frequenza $f_0>f_c/2$ viene "spostata" (*aliased*) e nel segnale ricostruito compare alla **frequenza alias** $f_c-f_0$.

#### Formule · [[Campionamento_AD_DA.pdf#page=18|p. 18]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]

> 🧮 Formula chiave: $f_{alias} = f_c - f_0$ per $f_0 > f_c/2$

Validità (🧩 mia precisazione): la formula della slide vale per $f_c/2 < f_0 < f_c$. In generale la frequenza ricostruita è la replica $|f_0 - kf_c|$ che cade in $[0, f_c/2]$ (grafico in «Perché il segnale ricostruito è a 0.5 kHz» (in questa pagina)).

**Filtro antialiasing**: LPF **analogico**, ideale con taglio $f_c/2$, messo **prima** del campionatore.

#### Derivazioni

##### Derivazione — Frequenza alias di una sinusoide · [[Campionamento_AD_DA.pdf#page=18|p. 18]]
> 🧩 Derivazione mia, nel dominio dei campioni
$$
\begin{aligned}
x_a(t) &= \cos(2\pi f_0 t) && \text{sinusoide a } f_0 \\
x(n) &= \cos\!\left(2\pi \tfrac{f_0}{f_c}n\right) && t = nT_c = n/f_c \\
&= \cos\!\left(2\pi n - 2\pi\tfrac{f_0}{f_c}n\right) && \cos \text{ periodica di } 2\pi,\ n \text{ intero} \\
&= \cos\!\left(2\pi\tfrac{f_c-f_0}{f_c}n\right) && \text{raccolgo; } \cos(-\theta)=\cos\theta
\end{aligned}
$$
I campioni coincidono quindi con quelli di una sinusoide a $f_c-f_0$. Se $f_0>f_c/2$ allora $f_c-f_0<f_c/2$, e il LPF di ricostruzione (taglio $f_c/2$) restituisce la sinusoide a **bassa** frequenza.

**Numeri**: $f_0 = 1.5$ kHz, $f_c = 2$ kHz:
$$f_{alias} = f_c - f_0 = 2\,\text{kHz} - 1.5\,\text{kHz} = 0.5\,\text{kHz}$$
Verifica sui campioni: $f_0/f_c = 0.75$, quindi $x(n) = \cos(1.5\pi n) = \cos(2\pi n - 0.5\pi n) = \cos(0.5\pi n)$, cioè $0.25\cdot f_c = 0.5$ kHz ✓.
**Sanity check:** $f_0 = 1.5$ kHz $> f_c/2 = 1$ kHz, quindi aliasing atteso; con $f_c\ge 3$ kHz non ci sarebbe aliasing.
**Ipotesi:** ricostruzione con LPF ideale di taglio $f_c/2$.

Perché il ricostruttore restituisce proprio questa frequenza, passo per passo e con due animazioni: «Perché il segnale ricostruito è a 0.5 kHz» (in questa pagina).

##### Derivazione — Perché un segnale di durata finita non è a banda limitata · [[Campionamento_AD_DA.pdf#page=20|p. 20]]
> 📚 Fonte esterna: proprietà standard della trasformata di Fourier (un segnale non nullo non può avere supporto limitato sia nel tempo sia in frequenza).

La slide dà l'esempio: un segnale a banda rigorosamente limitata ha necessariamente durata infinita (es. sinc, sinc²).

#### Spiegazione · [[Campionamento_AD_DA.pdf#page=18|p. 18]]

![[campionamento-p18-aliasing-sinusoide.png]]
*In alto, sull'asse delle frequenze: la frequenza originaria $f_0$ (a destra di $f_c/2$) viene "ribaltata" rispetto a $f_c/2$ sulla frequenza alias $f_c - f_0$. In basso: i campioni $x_a(nT_c)$ in funzione di $t/T_c$, e la sinusoide a 1.5 kHz (nera) insieme a quella a 0.5 kHz (rossa), che passano per gli **stessi campioni** $x(n)$.*

> 💡 Connessione: la figura mostra bene la "simmetria" dell'aliasing. $f_0$ e $f_c - f_0$ sono equidistanti da $f_c/2$: la frequenza $f_c/2$ fa da "specchio".

##### Perché il segnale ricostruito è a 0.5 kHz · [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=14|p. 14]], [[Campionamento_AD_DA.pdf#page=15|15]], [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=18|18]]

La slide dice che un coseno a 1.5 kHz, campionato a 2 kHz, viene ricostruito come un coseno a 0.5 kHz, e che i due hanno gli stessi campioni. Il ragionamento completo ha quattro passi.

**Passo 1 — Il ricostruttore vede solo i campioni.** Con $f_c = 2$ kHz si prende un campione ogni $T_c = 1/f_c = 0.5$ ms. Dopo il campionamento esiste solo la sequenza $x(n) = x_a(nT_c)$: quello che il segnale faceva *tra* due campioni è perso.

**Passo 2 — Quei campioni sono anche i campioni di un coseno a 0.5 kHz, e di molti altri.** L'argomento del coseno all'istante $nT_c$ è $2\pi f\,nT_c$; con $f$ in kHz e $T_c = 0.5$ ms il prodotto kHz·ms è adimensionale, quindi vale $2\pi\cdot1.5\cdot0.5\,n = 1.5\pi n$ per 1.5 kHz, $0.5\pi n$ per 0.5 kHz, $2.5\pi n$ per 2.5 kHz.

| $n$ | $t = nT_c$ | 1.5 kHz: $\cos(1.5\pi n)$ | 0.5 kHz: $\cos(0.5\pi n)$ | 2.5 kHz: $\cos(2.5\pi n)$ |
|---|---|---|---|---|
| 0 | 0 ms | 1 | 1 | 1 |
| 1 | 0.5 ms | 0 | 0 | 0 |
| 2 | 1.0 ms | −1 | −1 | −1 |
| 3 | 1.5 ms | 0 | 0 | 0 |
| 4 | 2.0 ms | 1 | 1 | 1 |

> 🧩 Derivazione mia: perché coincidono. Per ogni intero $k$, e ricordando che $f_cT_c = 1$:
> $$
> \begin{aligned}
> \cos\big(2\pi(f_0 + kf_c)nT_c\big) &= \cos(2\pi f_0nT_c + 2\pi kn) = \cos(2\pi f_0nT_c) && kn \text{ intero: } 2\pi kn \text{ è un numero intero di giri} \\
> \cos\big(2\pi(kf_c - f_0)nT_c\big) &= \cos(2\pi kn - 2\pi f_0nT_c) = \cos(2\pi f_0nT_c) && \text{idem, più } \cos(-\theta) = \cos\theta
> \end{aligned}
> $$
> Tutte le frequenze $|f_0 + kf_c|$ e $|kf_c - f_0|$ danno quindi gli stessi campioni. Con $f_0 = 1.5$ kHz e $f_c = 2$ kHz sono $1.5$, $0.5 = 2 - 1.5$, $2.5 = 4 - 1.5$, $3.5 = 1.5 + 2$, … kHz, cioè tutti i multipli dispari di 0.5 kHz. Dai soli campioni **non si può capire** quale di questi coseni c'era all'ingresso.

**Passo 3 — Il ricostruttore sceglie la frequenza sotto $f_c/2$.** La ricostruzione ideale usa il LPF $H_r(f) = T_c\,\Pi\!\big(f/2f_r\big)$ con, di solito, $f_r = f_c/2$; è la serie di Shannon con le sinc. Il filtro lascia passare solo le frequenze con $|f| < f_c/2 = 1$ kHz. Tra i candidati del passo 2 l'unico sotto 1 kHz è **0.5 kHz**, quindi l'uscita è il coseno a 0.5 kHz.

> 🧩 Detto in un altro modo: il ricostruttore applica il teorema del campionamento *come se* la sua ipotesi fosse vera. Restituisce cioè l'unico segnale con banda sotto $f_c/2$ che ha quei campioni, e quel segnale esiste: è il coseno a 0.5 kHz. Il coseno a 1.5 kHz non si può recuperare perché l'ipotesi del teorema è violata: $f_c = 2$ kHz $< 2f_0 = 3$ kHz.

**Passo 4 — La stessa cosa vista in frequenza**.
> 🧩 Derivazione mia
$$
\begin{aligned}
X_a(f) &= \tfrac12\big[\delta(f - f_0) + \delta(f + f_0)\big] && \text{spettro del coseno: due righe a } \pm1.5 \text{ kHz} \\
X(f) &= \frac{1}{T_c}\sum_{k=-\infty}^{+\infty}X_a(f - kf_c) && \text{campionamento: repliche con passo } f_c \text{ (p.12)} \\
&\to \text{righe a } \pm0.5,\ \pm1.5,\ \pm2.5,\ \dots \text{ kHz, ognuna di peso } \tfrac{1}{2T_c} && \text{le righe } \pm1.5 \text{ spostate di } kf_c = 2k \text{ kHz} \\
-1.5 + 2 &= +0.5,\qquad +1.5 - 2 = -0.5 && \text{le due repliche che cadono in } (-1, 1) \text{ kHz} \\
X_r(f) &= H_r(f)\,X(f) = \tfrac12\big[\delta(f - 0.5) + \delta(f + 0.5)\big] && H_r = T_c \text{ per } |f| < 1 \text{ kHz, } 0 \text{ fuori} \\
x_r(t) &= \cos(2\pi\cdot0.5\,\text{kHz}\cdot t) && \text{antitrasformata: coseno di ampiezza 1}
\end{aligned}
$$
La riga a $+0.5$ kHz che sopravvive è la replica della riga **negativa** $-1.5$ kHz spostata di $+f_c$: ecco da dove viene $f_c - f_0$. L'ampiezza torna quella originale perché il guadagno $T_c$ del filtro compensa il fattore $1/T_c$ delle repliche.

![[grafico-aliasing-animazione.gif]]
*🧩 Animazione mia (formule di p. 12, p. 15, p. 18; script in `output/grafici/`). In alto il tempo, in basso lo spettro a righe, nei sei passi appena descritti. (1) Coseno a 1.5 kHz, righe a ±1.5 kHz. (2) Un campione ogni 0.5 ms; nello spettro compaiono le repliche ogni 2 kHz, e le frecce mostrano le due che finiscono a ±0.5 kHz. (3) Il coseno originale sfuma: restano solo i campioni. (4) Per gli stessi campioni passano i coseni a 0.5 kHz (rosso) e a 2.5 kHz (grigio). (5) Il LPF di ricostruzione (riquadro blu, $|f| < f_c/2$) tiene solo le righe a ±0.5 kHz. (6) Uscita: coseno a 0.5 kHz.*

**Intuizione — l'effetto stroboscopio.**
> 🧩 Spiegazione mia. Il coseno è la parte reale di un fasore, un vettore che ruota: $\cos(2\pi f_0t) = \text{Re}\{e^{j2\pi f_0t}\}$.
> - In un intervallo di campionamento il fasore ruota di $2\pi f_0T_c = 2\pi\cdot0.75$ rad, cioè di **270°**, tre quarti di giro in senso antiorario.
> - Ruotare di 270° in avanti porta nella stessa posizione in cui si arriva ruotando di **90° all'indietro**.
> - Visto solo agli istanti di campionamento, come sotto una luce stroboscopica, il fasore sembra quindi girare all'indietro di un quarto di giro per campione: 0.25 giri ogni 0.5 ms, cioè **0.5 kHz**.
> - Il coseno non distingue il verso di rotazione, perché $\cos(-\theta) = \cos\theta$: un fasore a 0.5 kHz che gira all'indietro dà proprio un coseno a 0.5 kHz.
>
> È lo stesso effetto delle ruote delle auto che nei film sembrano girare lentamente all'indietro: la cinepresa "campiona" la ruota.

![[grafico-aliasing-stroboscopio.gif]]
*🧩 Animazione mia. A sinistra il fasore a 1.5 kHz (nero, antiorario) e quello a 0.5 kHz (rosso, orario); i punti neri sono le posizioni negli istanti di campionamento, numerati con $n$. Tra un campione e l'altro i due fasori sono in posizioni diverse. Negli istanti $nT_c$ coincidono: il nero ha fatto $270°\cdot n$, il rosso $-90°\cdot n$, e i due angoli differiscono di $360°\cdot n$, cioè di un numero intero di giri. A destra i due coseni (proiezioni sull'asse orizzontale): diversi tra i campioni, uguali nei campioni.*

**Regola generale.**
> 🧩 Mia: la frequenza ricostruita è la replica $|f_0 - kf_c|$ che cade in $[0, f_c/2]$, con $k$ = intero più vicino a $f_0/f_c$. Per $f_c/2 < f_0 < f_c$ si ha $k = 1$ e si ritrova la formula della slide, $f_c - f_0$.

![[grafico-aliasing-ripiegamento.png]]
*🧩 Grafico mio: frequenza ricostruita in funzione di $f_0$ con $f_c = 2$ kHz. Fino a $f_c/2 = 1$ kHz (zona grigia) la ricostruzione è corretta. Oltre, la frequenza si "ripiega" come in uno specchio posto a $f_c/2$: sale e scende a zig-zag tra 0 e 1 kHz. Il punto rosso è l'esempio della slide (1.5 kHz → 0.5 kHz); anche 2.5, 3.5 e 4.5 kHz finiscono a 0.5 kHz, in accordo con il passo 2.*

> 🧩 Nota sul seno: con $\sin$ al posto di $\cos$ i campioni coincidono a meno del segno, $\sin(1.5\pi n) = \sin(2\pi n - 0.5\pi n) = -\sin(0.5\pi n)$. L'uscita è quindi $-\sin(2\pi\cdot0.5\,\text{kHz}\cdot t)$: stessa frequenza, 0.5 kHz, ma fase invertita. È la "rotazione all'indietro" dello stroboscopio, che per il coseno non si vede perché il coseno è pari.

> 🎯 Esame: saper spiegare perché la ricostruzione dà $f_c - f_0$, e non $f_0$. I campioni sono ambigui, e il filtro di ricostruzione sceglie l'unica replica con $|f| < f_c/2$.

##### Le due ipotesi ideali del teorema · [[Campionamento_AD_DA.pdf#page=19|p. 19]]

Lo studio del campionamento riassunto dal teorema di Shannon si basa su **due ipotesi ideali**:
1. il segnale è a **banda rigorosamente limitata** → cosa succede quando cade: questa pagina;
2. l'**interpolazione è ideale**, con funzioni sinc → cosa succede quando cade: [[interpolazione]].

Le slide approfondiscono separatamente i due aspetti.

##### Segnali a banda praticamente limitata · [[Campionamento_AD_DA.pdf#page=20|p. 20]]

In pratica si campionano segnali di **durata finita**, che quindi **non** possono avere banda rigorosamente limitata. Sono al più a banda **praticamente** limitata: qualunque sia $f_c$, le repliche di $X_a(f)$ si sovrappongono un po', e c'è sempre un po' di aliasing nella ricostruzione.

![[campionamento-p20-banda-praticamente-limitata.png]]
*(a) spettro $X_a(f)$ di altezza 1 che non si annulla mai del tutto (code oltre $\pm f_c/2$); (b) $X_\delta(f)$: le repliche di altezza $1/T_c$ si sovrappongono e la loro somma (rosso) differisce da ogni singola replica; (c) filtro di ricostruzione $H_r(f)$ di altezza $T_c$ su $[-f_c/2, f_c/2]$; (d) confronto fra $X_r(f)$ e $X_a(f)$: il segnale ricostruito è diverso da quello originale, per effetto dell'aliasing.*

##### Come ridurre l'aliasing · [[Campionamento_AD_DA.pdf#page=21|p. 21]]

| Strategia | Pro | Contro |
|---|---|---|
| **Sovracampionamento** | repliche più distanti, meno sovrapposizione | costo e memoria (più campioni/s) |
| **Filtraggio antialiasing** (LPF prima del campionatore, taglio $f_c/2$) | più efficiente: elimina a monte l'energia oltre $f_c/2$ | è un filtro **analogico**, anch'esso non ideale in pratica |

![[campionamento-p21-antialiasing.png]]
*(a) $X_\delta(f)$ con $f_{c1}$: repliche di altezza $1/T_c$ fortemente sovrapposte intorno a $f_{c1}/2$; (b) con $f_{c2} = 2f_{c1}$ (sovracampionamento ×2) le repliche sono più distanti e la sovrapposizione intorno a $f_{c2}/2$ è molto minore; in basso, lo schema $x_a(t)$ → $H_{aa}(f)$ (filtro antialiasing) → $y_a(t)$ → campionatore ($T_c$) → $y(n)$.*

Dettagli della slide sul filtro antialiasing:
- LPF **ideale** con frequenza di taglio $f_c/2$;
- filtro **analogico**, perché agisce prima del campionamento;
- in pratica anche questo filtro sarà **non ideale**.

> 🎯 Esame: dove va il filtro antialiasing (prima del campionatore, in analogico) e perché (il segnale reale non è a banda limitata). Da non confondere con il filtro di ricostruzione (dopo, in D/A).

> 💡 Connessione: l'antialiasing *toglie* informazione oltre $f_c/2$ ma evita che quella energia si "ripieghi" sulle frequenze utili. Si perde la parte alta dello spettro invece di corrompere la parte bassa.

#### Perché importa

L'aliasing è una distorsione **irreversibile**: dopo il campionamento la componente alias è indistinguibile da una componente vera a $f_c-f_0$. È per questo che ogni catena A/D reale ha un filtro antialiasing.

#### Connessioni

- [[lab-campionamento]] — 🧪 laboratorio (non d'esame): aliasing piccolo per un segnale quasi a banda limitata, grande per una sinusoide a 4 Hz campionata a 7.94 Hz.
- [[teorema-del-campionamento]] — le ipotesi la cui violazione causa aliasing.
- [[interpolazione]] — l'altra ipotesi ideale: l'interpolazione con sinc.
- [[campionamento-e-aliasing]] — esercizi.

#### Fonti · [[Campionamento_AD_DA.pdf#page=18|p. 18]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]

- [[campionamento-conversione-ad-da]]

### Quantizzazione uniforme, errore di quantizzazione e fattore di carico · [[quantizzazione-uniforme|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=26|26]]

Nella conversione A/D, oltre a discretizzare i tempi (campionamento), bisogna discretizzare le **ampiezze** del segnale: è la **quantizzazione**. In pratica l'intervallo reale dei valori di ampiezza è suddiviso in **intervalli di quantizzazione**:
- a ogni intervallo è associato un **livello di restituzione** (o di quantizzazione);
- tutte le ampiezze di uno stesso intervallo sono rappresentate dal livello di restituzione di quell'intervallo.

**Esempio**: le ampiezze in $(1,2)$ sono rappresentate dal livello 1.5 (punto medio dell'intervallo), quelle in $(2,3)$ dal livello 2.5, e così via.

![[campionamento-p25-quantizzazione.png]]
*Asse delle ampiezze diviso in intervalli: intervallo #3 = (1,2) → livello #3 = 1.5; intervallo #2 = (2,3) → livello #2 = 2.5; intervallo #1 = (3,4) → livello #1 = 3.5. I punti rossi sono i livelli, al centro di ogni intervallo*

Il quantizzatore è un sistema a tempo discreto **non lineare** e **istantaneo**: $x_q(n) = Q[x(n)]$.

**Quantizzatore uniforme**, due parametri:
- $\Delta$ = **passo di quantizzazione** (larghezza degli intervalli), nell'unità del segnale (es. V);
- $M$ = numero di intervalli / livelli di restituzione.

Se è **simmetrico**:
- $(-X_{max}, X_{max})$ = intervallo delle ampiezze di ingresso;
- $2X_{max} = M\Delta$ = **dinamica** del quantizzatore.

#### Formule · [[Campionamento_AD_DA.pdf#page=26|p. 26]]–[[Campionamento_AD_DA.pdf#page=29|29]]

| Formula | Significato |
|---|---|
| $2X_{max} = M\Delta \iff \Delta = \frac{2X_{max}}{M}$ | dinamica |
| $b \ge \log_2 M$, di solito $M = 2^b$ | bit per campione |
| $e(n) = x_q(n) - x(n) \iff x_q(n) = x(n)+e(n)$ | errore (rumore) di quantizzazione |
| $R_g = [-X_{max}, X_{max}]$: $\|e(n)\|\le\Delta/2$ | regione granulare |
| $R_s = ]-\infty,-X_{max}[\ \cup\ ]X_{max},+\infty[$: $e(n)$ non limitato | regione di sovraccarico |
| $k_c \triangleq \dfrac{X_{max}}{x_{rms}}$, $x_{rms} = \sqrt{P_x}$ | **fattore di carico** (adimensionale) |
| $P_s = P(\|x(n)\|>X_{max}) \le \dfrac{1}{k_c^2}$ | probabilità di sovraccarico |

> 🧮 Formula chiave: $\Delta = 2X_{max}/M$, $k_c = X_{max}/x_{rms}$, $P_s\le1/k_c^2$.

#### Derivazioni

##### Derivazione — $|e(n)|\le\Delta/2$ nella regione granulare · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=28|p. 28]]
> 🧩 Derivazione mia
In $R_g$ ogni $x(n)$ cade in un intervallo di larghezza $\Delta$ e il livello di restituzione ne è il **punto medio** (esempio di p. 25). La distanza massima tra un punto dell'intervallo e il suo punto medio è metà della larghezza: $|e(n)| = |x_q(n)-x(n)| \le \Delta/2$.
In $R_s$ il livello resta quello estremo (es. $q_M = X_{max}-\Delta/2$) mentre $x(n)$ può crescere senza limite, quindi $e(n)$ non è limitato.

##### Derivazione — $b\ge\log_2M$ · [[Campionamento_AD_DA.pdf#page=27|p. 27]]
Con $b$ bit si scrivono $2^b$ stringhe distinte. Per dare un codice diverso a ciascuno degli $M$ livelli serve $2^b\ge M$, cioè $b\ge\log_2M$.

##### Derivazione — Probabilità di sovraccarico e four-sigma loading · [[Campionamento_AD_DA.pdf#page=29|p. 29]]
**Fonte:** p. 29 → derivazione completa in [[disuguaglianza-di-chebyshev]].
**Numeri:** $k_c = 4$ → $P_s\le 1/4^2 = 1/16 = 0.0625$ (6.25%).

##### Esempio — Quantizzatore con $M = 4$ · [[Campionamento_AD_DA.pdf#page=26|p. 26]], [[Campionamento_AD_DA.pdf#page=27|27]]
> 🧩 Derivazione mia (lettura della figura)
$$
\begin{aligned}
M &= 4 \Rightarrow \Delta = \frac{2X_{max}}{4} = \frac{X_{max}}{2} \Rightarrow X_{max} = 2\Delta && \text{dinamica} \\
\text{soglie} &: -\Delta,\ 0,\ +\Delta \quad (\text{più } \pm X_{max} = \pm 2\Delta \text{ come bordi di } R_g) \\
\text{livelli} &: q_1 = -\tfrac32\Delta,\ q_2 = -\tfrac12\Delta,\ q_3 = +\tfrac12\Delta,\ q_4 = +\tfrac32\Delta && \text{punti medi} \\
b &= \log_2 4 = 2\ \text{bit} && \text{codifica naturale: } 00, 01, 10, 11
\end{aligned}
$$
Nessun livello cade in zero: con $M$ pari e livelli ai punti medi, lo zero è una soglia di decisione, non un livello.

#### Spiegazione

![[campionamento-p26-quantizzatore-uniforme.png]]

##### Codifica binaria · [[Campionamento_AD_DA.pdf#page=27|p. 27]]

Per completare la A/D, gli $M$ livelli $\{q_1,\dots,q_M\}$ si convertono in **stringhe di bit**:
- servono $b\ge\log_2M$ bit per rappresentare $M$ livelli;
- di solito si sceglie $M = 2^b$ per semplificare la codifica binaria.

Schemi di codifica binaria (associano stringhe di bit ai livelli):
- codifica **naturale** (vedi esempio);
- codifica in **segno e modulo**;
- codifica in **complemento a due**.

La scelta dipende dall'architettura del sistema digitale di elaborazione.

![[campionamento-p27-codifica-binaria.png]]
*Esempio: $M = 4 \Rightarrow b = 2$ bit; codifica naturale dal livello più basso al più alto: 00, 01, 10, 11*

##### Modello additivo · [[Campionamento_AD_DA.pdf#page=28|p. 28]]

Obiettivo della slide: fissare **criteri quantitativi** per dimensionare un quantizzatore. Scrivere $x_q = x+e$ trasforma il quantizzatore (non lineare) in un **sommatore** con un "rumore" $e(n)$: il **rumore di quantizzazione**. È il modello che permette di parlare di SNR ([[snr-di-quantizzazione]]).

![[campionamento-p28-errore-quantizzazione.png]]
*A destra: modello a sommatore $x(n) + e(n) = x_q(n)$ e caratteristica $Q(x)$ a gradini tra $q_1$ e $q_M$. Nella regione granulare $\mathcal{R}_g = [-X_{max}, X_{max}]$ i gradini seguono la bisettrice; nelle regioni di sovraccarico $\mathcal{R}_s$ l'uscita resta ferma a $q_1$ o $q_M$*

##### Trade-off su $X_{max}$ · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- L'errore di quantizzazione è **irreversibile**, quindi bisogna evitare che il quantizzatore lavori nella regione di sovraccarico, e per questo si vorrebbe **aumentare $X_{max}$**.
- Ma a parità di $M$, aumentare $X_{max}$ aumenta $\Delta$, e quindi l'errore nella regione granulare.
- È ragionevole scegliere $X_{max}$ **proporzionale al livello del segnale**, misurato dal **valore efficace** $x_{rms} = \sqrt{P_x}$. Da qui la definizione del fattore di carico $k_c = X_{max}/x_{rms}$.
- Assimilando $x(n)$ a una v.a. a media nulla e deviazione standard $x_{rms}$, la disuguaglianza di Chebyshev dà $P_s\le1/k_c^2$.
- Con $k_c = 4$ (*four-sigma loading*): $P_s\le1/16 = 0.0625$ (6.25%).

> 🎯 Esame: le due regioni, perché serve $k_c$, da dove viene il 6.25% del four-sigma loading.

#### Perché importa

È il secondo stadio della A/D ([[conversione-ad-da]]) e l'unico **irreversibile**. $b$ fissa sia la qualità (SNR) sia il bit rate ($b\cdot f_c$).

#### Connessioni

- [[lab-quantizzazione]] — 🧪 laboratorio (non d'esame): quantizzatore a 16 livelli sui campioni di un trapezio; lo zero diventa $\Delta/2$.
- [[snr-di-quantizzazione]] — misura l'accuratezza nella regione granulare.
- [[disuguaglianza-di-chebyshev]] — limite su $P_s$.
- [[quantizzazione-non-uniforme]] — cosa cambia se gli intervalli non sono uguali.
- [[variabili-aleatorie-notevoli]] — modello uniforme di $e(n)$.

#### Fonti · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- [[campionamento-conversione-ad-da]]

### Disuguaglianza di Chebyshev · [[disuguaglianza-di-chebyshev|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

> 📚 Fonte esterna: enunciato standard di qualunque testo di probabilità (es. Papoulis, *Probability, Random Variables and Stochastic Processes*, cap. 5).

Per ogni v.a. $X$ con media $\mu$ e deviazione standard $\sigma$ finite, e per ogni $k>0$:
$$P(|X-\mu|\ge k\sigma) \le \frac{1}{k^2}$$
Il limite vale **per qualunque pdf**: non richiede ipotesi sulla distribuzione oltre all'esistenza della varianza.

#### Formule · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

Applicazione del corso: $x(n)$ è assimilato a una v.a. a media nulla con $\sigma = x_{rms}$; $X_{max}$ è la soglia di sovraccarico; $k_c = X_{max}/x_{rms}$ è il fattore di carico:
$$P_s = P(|x(n)|>X_{max}) \le \frac{1}{k_c^2}$$

#### Derivazioni

##### Derivazione — Disuguaglianza di Chebyshev · [[Probabilità.pdf#page=28|p. 28]]
> 🧩 Derivazione mia (dimostrazione standard tramite il teorema fondamentale della media)
$$
\begin{aligned}
\sigma^2 &= \int_{-\infty}^{+\infty}(x-\mu)^2f(x)\,dx && \text{def. varianza} \\
&\ge \int_{|x-\mu|\ge k\sigma}(x-\mu)^2f(x)\,dx && \text{tolgo un integrando} \ge 0 \\
&\ge \int_{|x-\mu|\ge k\sigma}k^2\sigma^2f(x)\,dx && \text{lì } (x-\mu)^2\ge k^2\sigma^2 \\
&= k^2\sigma^2\,P(|X-\mu|\ge k\sigma) && \text{prop. 6 della pdf} \\
\Rightarrow P(|X-\mu|\ge k\sigma) &\le \frac{1}{k^2} && \text{divido per } k^2\sigma^2>0
\end{aligned}
$$

##### Derivazione — Probabilità di sovraccarico · [[Campionamento_AD_DA.pdf#page=29|p. 29]]
$$
\begin{aligned}
\mu &= 0,\ \sigma = x_{rms} && \text{ipotesi della slide} \\
k\sigma = X_{max} &\Rightarrow k = X_{max}/x_{rms} = k_c && \text{def. fattore di carico} \\
P(|x(n)|>X_{max}) &\le P(|x(n)|\ge X_{max}) \le \frac{1}{k_c^2} && \{>\} \subseteq \{\ge\};\ \text{Chebyshev}
\end{aligned}
$$
**Numeri:** $k_c=4$ (*four-sigma loading*) → $P_s\le 1/16 = 0.0625 = 6.25\%$.
**Sanity check:** per un segnale gaussiano la probabilità vera sarebbe $2Q(4)\approx6.3\cdot10^{-5}$ ([[variabile-aleatoria-gaussiana]]), molto sotto il limite. Chebyshev è quindi un maggiorante **conservativo**.
**Ipotesi:** media nulla; varianza finita; il segnale campionato è trattato come una v.a. (quindi statistiche costanti nel tempo).

##### Derivazione — Probabilità esatta di sovraccarico per Laplace · [[Campionamento_AD_DA.pdf#page=32|p. 32]]
> 🧩 Derivazione mia (serve al confronto nel grafico; pdf di Laplace da p. 32)
$$
\begin{aligned}
P(|X|>a) &= 2\int_a^\infty\tfrac\lambda2e^{-\lambda x}dx = e^{-\lambda a} && \text{pdf pari} \\
x_{rms} &= \sqrt2/\lambda \Rightarrow \lambda = \sqrt2/x_{rms} && [[variabili-aleatorie-notevoli]] \\
a = X_{max} = k_cx_{rms} &\Rightarrow P_s = e^{-\sqrt2\,k_c} && \text{sostituisco}
\end{aligned}
$$
**Numeri:** $k_c = 4$ → $P_s = e^{-5.657} \approx 3.5\cdot10^{-3}$ (0.35%), contro il limite di 6.25%.

#### Spiegazione

La disuguaglianza usa **solo** i primi due momenti, per questo è debole ma universale. Se si conosce la pdf (gaussiana, Laplace...) si calcola il valore esatto, molto più piccolo.

![[grafico-chebyshev-sovraccarico.png]]
*🧩 Grafico mio (scala logaritmica). Il limite di Chebyshev $1/k_c^2$ decresce solo come potenza. Le probabilità vere decrescono esponenzialmente: Laplace come $e^{-\sqrt2k_c}$, gaussiana ancora più in fretta, come $2Q(k_c)$. Al four-sigma loading il limite vale 6.25%, mentre per una voce di Laplace il valore esatto è circa 0.35%. La Laplace ha code più pesanti della gaussiana, quindi per la voce il sovraccarico è più probabile che per un segnale gaussiano con la stessa potenza.*

> 🎯 Esame: sapere da dove viene $P_s \le 1/k_c^2$ e perché con $k_c=4$ si ha $6.25\%$.

#### Perché importa

È il criterio usato per scegliere $X_{max}$ di un quantizzatore: trade-off tra sovraccarico e rumore granulare ([[quantizzazione-uniforme]], [[snr-di-quantizzazione]]).

#### Connessioni

- [[media-e-varianza]] — la dimostrazione è un'applicazione del teorema fondamentale della media.
- [[quantizzazione-uniforme]] — fattore di carico e probabilità di sovraccarico.
- [[variabile-aleatoria-gaussiana]] — confronto limite/valore esatto.

#### Fonti · [[Campionamento_AD_DA.pdf#page=29|p. 29]]

- [[campionamento-conversione-ad-da]]

### SNR di quantizzazione e legge dei 6 dB/bit · [[snr-di-quantizzazione|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=30|p. 30]]

Dopo aver fissato un criterio per scegliere $X_{max}$ (tramite $k_c$, [[quantizzazione-uniforme]]), si introduce un parametro che misura l'accuratezza della quantizzazione. Il **rapporto segnale-rumore di quantizzazione** misura l'accuratezza della quantizzazione nella **regione granulare** (il sovraccarico non è considerato):
$$\text{SNR} \triangleq \frac{P_x}{P_e} = \frac{\langle x^2(n)\rangle}{\langle e^2(n)\rangle}, \qquad \text{SNR}_{dB} = 10\log_{10}\text{SNR}$$
- $P_x$ = potenza del segnale; $P_e$ = potenza del rumore di quantizzazione; $\langle\cdot\rangle$ = media temporale. Le due potenze hanno la stessa unità (es. V² o W), quindi l'SNR è adimensionale e $\text{SNR}_{dB}$ si misura in dB.
- $\text{SNR}\gg1$ significa quantizzazione accurata.

#### Formule · [[Campionamento_AD_DA.pdf#page=30|p. 30]], [[Campionamento_AD_DA.pdf#page=31|31]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

> 🧮 Formula chiave — **legge dei 6 dB/bit**:
> $$\text{SNR}_{dB} = 6.02\,b - [k_c]_{dB} + 4.77$$

- $b$ = bit per campione ($M = 2^b$);
- $[k_c]_{dB} = 20\log_{10}k_c = 20\log_{10}(X_{max}/x_{rms})$. È esplicito in p. 43, dove per l'uniforme si scrive $\alpha = 4.77 - 20\log_{10}(X_{max}/x_{rms})$. Si usa $20\log$ perché $k_c$ è un rapporto di **ampiezze**;
- ipotesi: $e(n)\sim\mathcal{U}(-\Delta/2,\Delta/2)$, solo regione granulare.

Modello del rumore: $\langle e^2(n)\rangle \approx E[e^2(n)] = \Delta^2/12$.

**Formule di progetto**: $P_s\le 1/k_c^2$ e $\text{SNR}_{dB} = 6.02b - [k_c]_{dB} + 4.77$.

#### Derivazioni

##### Derivazione — Potenza del rumore di quantizzazione $\Delta^2/12$ · [[Campionamento_AD_DA.pdf#page=30|p. 30]]
**Si parte da:** varianza dell'uniforme ([[variabili-aleatorie-notevoli]]): $\mathcal{U}(a,b)\Rightarrow\text{Var} = (b-a)^2/12$
$$
\begin{aligned}
E[e] &= 0 && \text{uniforme simmetrica intorno a } 0 \\
E[e^2] &= \text{Var}(e) + E^2[e] = \text{Var}(e) && [[media-e-varianza]] \\
&= \frac{(\Delta/2-(-\Delta/2))^2}{12} = \frac{\Delta^2}{12} && a=-\Delta/2,\ b=\Delta/2
\end{aligned}
$$

![[grafico-errore-quantizzazione.png]]
*🧩 Grafico mio: sinusoide di ampiezza 0.9 quantizzata con $b = 3$ bit ($M = 8$, $X_{max} = 1$, $\Delta = 0.25$). L'errore $e(n)$ resta sempre in $[-\Delta/2, +\Delta/2]$ (regione granulare) e salta in modo irregolare dentro questa fascia. Per questo è ragionevole modellarlo come v.a. uniforme su $(-\Delta/2, \Delta/2)$, cioè il modello da cui viene $\Delta^2/12$.*

##### Derivazione — Legge dei 6 dB/bit · [[Campionamento_AD_DA.pdf#page=30|p. 30]]
**Si parte da:** $\text{SNR} = P_x/P_e$, $P_e = \Delta^2/12$, $\Delta = 2X_{max}/M$ ([[quantizzazione-uniforme]]), $k_c = X_{max}/x_{rms}$, $P_x = x_{rms}^2$
$$
\begin{aligned}
\text{SNR} &= \frac{P_x}{\Delta^2/12} = \frac{12\,x_{rms}^2}{\Delta^2} && \text{sostituisco } P_e \\
&= \frac{12\,x_{rms}^2}{4X_{max}^2/M^2} = \frac{3M^2\,x_{rms}^2}{X_{max}^2} && \Delta^2 = 4X_{max}^2/M^2 \\
&= \frac{3M^2}{k_c^2} && x_{rms}^2/X_{max}^2 = 1/k_c^2 \\
&= \frac{3\cdot 2^{2b}}{k_c^2} && M = 2^b \\
\text{SNR}_{dB} &= 10\log_{10}3 + 2b\cdot10\log_{10}2 - 20\log_{10}k_c && \log \text{ di prodotto/rapporto/potenza} \\
&= 4.771 + 6.0206\,b - [k_c]_{dB} && 10\log_{10}3 = 4.771;\ 20\log_{10}2 = 6.0206
\end{aligned}
$$
**Risultato:** $\text{SNR}_{dB} \approx 6.02\,b - [k_c]_{dB} + 4.77$ ✓ (3 cifre significative sui coefficienti).
**Sanity check:** un bit in più raddoppia $M$, quindi dimezza $\Delta$, divide $P_e$ per 4 e aggiunge $10\log_{10}4 = 6.02$ dB ✓. Controllo dimensionale: $x_{rms}^2/X_{max}^2$ è adimensionale ✓.
**Ipotesi:**
1. errore uniforme su $(-\Delta/2,\Delta/2)$, ragionevole se $M\gg1$ e il segnale "attraversa" molti livelli;
2. niente sovraccarico (conta solo la regione granulare);
3. quantizzatore uniforme simmetrico.
Se cade la 2, l'SNR reale è **peggiore** perché si aggiunge l'errore di sovraccarico, non limitato.

##### Derivazione — Costante per il four-sigma loading · [[Campionamento_AD_DA.pdf#page=43|p. 43]]
> 🧩 Derivazione mia (il valore −7.3 compare in p. 43)
$$
k_c = 4 \Rightarrow [k_c]_{dB} = 20\log_{10}4 = 12.04\,\text{dB} \Rightarrow \text{SNR}_{dB} = 6.02b - 12.04 + 4.77 = 6.02b - 7.27 \approx 6.02b - 7.3
$$

#### Spiegazione · [[Campionamento_AD_DA.pdf#page=30|p. 30]], [[Campionamento_AD_DA.pdf#page=31|31]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- **Legge dei 6 dB/bit**: l'SNR migliora di 6 dB per ogni bit in più, cioè ogni raddoppio del numero di livelli.

![[grafico-snr-vs-bit.png]]
*🧩 Grafico mio della formula di p. 30. Rette parallele di pendenza 6.02 dB/bit; raddoppiare $k_c$ trasla la retta verso il basso di $20\log_{10}2 = 6.02$ dB, cioè costa esattamente un bit. Il punto evidenziato è l'Esempio 7.6: con $k_c = 4$ il primo $b$ che supera 85 dB è 16 (89.1 dB).*
- **Trade-off di progetto**:
  - $k_c$ ↑ ⇒ $P_s$ ↓ (meno sovraccarico) ma $\text{SNR}_{dB}$ ↓ (più rumore granulare);
  - $M = 2^b$ ↑ ⇒ $\text{SNR}_{dB}$ ↑ (qualità) ma anche costo e memoria ↑.
- **Dipendenza dal livello del segnale**: a $X_{max}$ fisso, l'SNR dipende da $x_{rms}$ tramite $k_c$. Un segnale debole (es. un parlatore a bassa voce) ha $k_c$ grande e SNR basso. Da qui nasce il [[companding]].

##### Esempio 7.6 · [[Campionamento_AD_DA.pdf#page=31|p. 31]]
> 📄 Svolgimento completo in [[dimensionamento-quantizzatore]]

- Si vuole $\text{SNR}_{dB} = 85$ dB con $k_c = 4$: servono $b = 16$ bit (quantizzatore a 16 bit).
- Un segnale audio stereo campionato a $f_c = 44.1$ kHz e quantizzato così produce un flusso di $16\times44.1\,\text{kHz} = 705.6$ kbit/s **per canale** (L/R).
- 1 minuto di audio stereo: $2\times60\times44\,100\times16 = 84\,672\,000$ bit $= 10\,584\,000$ byte $= 10\,584$ kB $\approx 10.6$ MB.
- Fattori di conversione (ISO/IEC): 1 byte = 8 bit; 1 kB = 1000 byte; 1 MB = 1000 kB.

> 🎯 Esame: derivare la legge dei 6 dB/bit dall'inizio (è l'unico passaggio che le slide omettono esplicitamente) ed elencarne le ipotesi.

#### Perché importa

Collega qualità (SNR), numero di bit e quindi bit rate ($R_b = b\,f_c$). È il primo esempio del corso di un compromesso tra qualità e risorse.

#### Connessioni

- [[lab-snr]] — 🧪 laboratorio (non d'esame): SNR misurato in Matlab; pendenza di 6 dB/bit confermata, ma 4.77 dB sotto il modello $\Delta^2/12$ perché l'errore non è uniforme.
- [[quantizzazione-uniforme]] — definizioni di $\Delta$, $M$, $k_c$.
- [[variabili-aleatorie-notevoli]] — varianza dell'uniforme, da cui $\Delta^2/12$.
- [[companding]] — rende l'SNR indipendente dal livello di segnale; stessa pendenza di 6 dB/bit ma costante $\alpha$ diversa.
- [[dimensionamento-quantizzatore]] — esercizi.

#### Fonti · [[Campionamento_AD_DA.pdf#page=30|p. 30]], [[Campionamento_AD_DA.pdf#page=31|31]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- [[campionamento-conversione-ad-da]]

### Quantizzazione non uniforme e quantizzatore ottimo di Lloyd-Max · [[quantizzazione-non-uniforme|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=28|p. 28]], [[Campionamento_AD_DA.pdf#page=33|p. 33]]

Dati $M+1$ **livelli di decisione** $x_0<x_1<\dots<x_{M-1}<x_M$ con $x_0=-\infty$ e $x_M=+\infty$, si ha una partizione dell'asse reale in intervalli $R_i = (x_{i-1},x_i)$, $i=1,\dots,M$:
- **esterni**: $R_1 = ]-\infty,x_1]$ e $R_M = [x_{M-1},+\infty[$;
- **interni**: $R_i$ per $i=2,\dots,M-1$.

Assegnati $M$ **livelli di restituzione** $q_1,\dots,q_M$, la legge di quantizzazione (arbitraria, non uniforme) è
$$Q(x) = q_i \quad \text{se } x\in R_i$$
- regione granulare: $R_g = \bigcup_{i=2}^{M-1}R_i = (x_1,x_{M-1})$;
- regione di sovraccarico: $R_s = R_1\cup R_M$.

![[campionamento-p28-caratteristica-quantizzatore.png]]
*Caratteristica ingresso-uscita $Q(x)$ con regione granulare $\mathcal{R}_g$ e di sovraccarico $\mathcal{R}_s$ — p. 28. La figura della slide mostra gradini **uniformi**. In un quantizzatore non uniforme la struttura è la stessa (livelli $q_1,\dots,q_M$, regioni esterne che saturano a $q_1$ e $q_M$), ma i gradini hanno larghezze $\Delta_i = x_i - x_{i-1}$ diverse.*

#### Formule · [[Campionamento_AD_DA.pdf#page=32|p. 32]], [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=35|35]]

| Formula | Significato |
|---|---|
| $f_X(x) = \frac\lambda2 e^{-\lambda\|x\|}$ | pdf di Laplace (ampiezze della voce) |
| $\text{MSE} = E[e^2(n)] = \sum_{i=1}^M\int_{R_i}(q_i-x)^2f_X(x)\,dx$ | errore quadratico medio |
| $q_i = E[x(n)\,\|\,x(n)\in R_i] = \dfrac{\int_{x_{i-1}}^{x_i} x\,f_X(x)\,dx}{\int_{x_{i-1}}^{x_i} f_X(x)\,dx}$ | **condizione del centroide**: baricentro della pdf ristretta a $R_i=(x_{i-1},x_i)$ |
| $x_i = \dfrac{q_i+q_{i+1}}{2}$ | **condizione del punto medio** (minima distanza) |

> 🧩 Derivazione mia — perché quella frazione è una media: il numeratore $\int_{x_{i-1}}^{x_i}x\,f_X(x)\,dx$ pesa ogni valore $x$ per la sua densità di probabilità, come nella somma discreta $\sum_k x_k\,p(x_k)$ di [[media-e-varianza]], ma limitata all'intervallo $R_i$ invece che a tutto l'asse reale. Il denominatore $\int_{x_{i-1}}^{x_i}f_X(x)\,dx = P(x\in R_i)$ è l'area di $f_X$ dentro $R_i$: dividere per questa area **rinormalizza** i pesi, perché $f_X$ ristretta a $R_i$ non è di per sé una pdf valida (non integra a 1 su $R_i$). Il rapporto è quindi la media pesata dei valori di $x$ **condizionata** al fatto che $x$ sia caduto in $R_i$ ([[probabilita-condizionale]]) — cioè il baricentro (centro di massa) della sola fetta di pdf che sta in $R_i$, non di tutta $f_X$.

Simboli: $f_X$ = pdf del segnale, supposto **stazionario del primo ordine** (definizione in [[stazionarieta]]: tutti i campioni hanno la stessa pdf $f_X$); $e(n) = Q[x(n)]-x(n)$. MSE nell'unità del segnale al quadrato (es. V²).

> 🧮 Formula chiave: le due condizioni di Lloyd-Max.

#### Derivazioni

##### Derivazione — Condizione del centroide · [[Campionamento_AD_DA.pdf#page=35|p. 35]]
> 🧩 Derivazione mia. Fisso le regioni $R_i$ e ottimizzo rispetto a $q_i$, che compare solo nel termine $i$-esimo.
$$
\begin{aligned}
\frac{\partial\,\text{MSE}}{\partial q_i} &= \int_{R_i} 2(q_i-x)f_X(x)\,dx = 0 && \text{derivo sotto il segno di integrale} \\
q_i\int_{R_i}f_X(x)\,dx &= \int_{R_i}x\,f_X(x)\,dx && \text{separo} \\
q_i &= \frac{\int_{R_i}x\,f_X(x)\,dx}{\int_{R_i}f_X(x)\,dx} = \int_{R_i} x\,\frac{f_X(x)}{P(x\in R_i)}\,dx && \text{pdf condizionata a } \{x\in R_i\} \\
&= E[x(n)\,|\,x(n)\in R_i] && \text{media condizionale}
\end{aligned}
$$
È un minimo: $\partial^2\text{MSE}/\partial q_i^2 = 2P(x\in R_i)>0$.
**Interpretazione:** $q_i$ è il **baricentro** della porzione di pdf in $R_i$.

##### Derivazione — Condizione del punto medio · [[Campionamento_AD_DA.pdf#page=35|p. 35]]
> 🧩 Derivazione mia. Fisso i $q_i$; $x_i$ è l'estremo superiore di $R_i$ e quello inferiore di $R_{i+1}$.
$$
\begin{aligned}
\text{MSE} &\ni \int_{x_{i-1}}^{x_i}(q_i-x)^2f_X\,dx + \int_{x_i}^{x_{i+1}}(q_{i+1}-x)^2f_X\,dx && \text{termini che dipendono da } x_i \\
\frac{\partial\,\text{MSE}}{\partial x_i} &= (q_i-x_i)^2f_X(x_i) - (q_{i+1}-x_i)^2f_X(x_i) = 0 && \text{regola di Leibniz} \\
(x_i-q_i)^2 &= (q_{i+1}-x_i)^2 && f_X(x_i)>0 \\
x_i - q_i &= q_{i+1}-x_i && q_i<x_i<q_{i+1} \Rightarrow \text{entrambi positivi} \\
x_i &= \frac{q_i+q_{i+1}}{2}
\end{aligned}
$$
**Interpretazione:** ogni $x$ va al livello $q_i$ **più vicino** (regola a minima distanza).

##### Caso uniforme come verifica · [[Campionamento_AD_DA.pdf#page=32|p. 32]]
> 🧩 Sanity check mio: con $f_X$ uniforme su $(-X_{max},X_{max})$ e intervalli uguali, il centroide di ogni $R_i$ è il punto medio e le soglie sono a metà tra livelli adiacenti. Il quantizzatore uniforme soddisfa quindi entrambe le condizioni ed è ottimo, in accordo con p. 32.

#### Spiegazione

##### Perché non uniforme · [[Campionamento_AD_DA.pdf#page=32|p. 32]]

- Dal punto di vista teorico la quantizzazione uniforme è ottima **solo** se $x(n)$ è distribuito uniformemente in $(-X_{max},X_{max})$.
- Il segnale vocale ha una pdf **non uniforme**: i valori vicini allo zero sono più probabili di quelli elevati.
- Questo comportamento è ben modellato da una **distribuzione di Laplace**, $f_X(x) = \frac\lambda2e^{-\lambda|x|}$ con $\lambda>0$.
- Intuitivamente, le ampiezze più piccole vanno quantizzate **più finemente**: da qui la **quantizzazione non uniforme**.

![[grafico-laplace-pdf-lambda.png]]
*🧩 Grafico mio (formula di p. 32, script in `output/grafici/`). La pdf di Laplace ha una **cuspide** in 0 e code esponenziali. $\lambda$ regola la larghezza: il picco vale $\lambda/2$ e il valore efficace è $x_{rms} = \sqrt2/\lambda$ (derivazione in [[variabili-aleatorie-notevoli]]). Un parlatore a voce alta ha $\lambda$ piccolo (curva larga), uno a voce bassa ha $\lambda$ grande (curva stretta).*

![[grafico-laplace-gauss-uniforme.png]]
*🧩 Grafico mio: tre pdf con la **stessa potenza** $E[x^2] = 1$. Rispetto a gaussiana e uniforme, la Laplace concentra molta più probabilità vicino a zero e ha code più lunghe. Un quantizzatore uniforme, che spende gli stessi livelli ovunque, "spreca" risoluzione sulle ampiezze grandi (rare) e ne dà poca a quelle piccole (frequenti). È ottimo solo per la pdf uniforme (verde).*

##### Algoritmo di Lloyd-Max · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=35|35]]

- Errore di quantizzazione: $e(n) \triangleq x_q(n) - x(n) = Q[x(n)] - x(n)$, con $f_X(x)$ pdf del segnale $x(n)$ supposto **stazionario del primo ordine**. Il suo valor quadratico medio (*mean square error*, MSE) è la funzione da minimizzare.
- Trovare la legge ottima secondo il criterio a **minimo errore quadratico medio** (MMSE) significa determinare gli intervalli $R_1,\dots,R_M$ (cioè i livelli di decisione $x_1,\dots,x_{M-1}$) e i livelli di restituzione $q_1,\dots,q_M$ che minimizzano l'MSE.
- Il problema **non** ha soluzione in forma chiusa. Si ricavano però facilmente **due condizioni necessarie**, fissando un sottoinsieme delle variabili e ottimizzando rispetto all'altro: è il **quantizzatore ottimo di Lloyd-Max**.
- **Regioni fissate**: i livelli ottimi sono i **centroidi** delle regioni di decisione (centroide = media condizionale; risultato ben noto dalla teoria della stima ottima MMSE).
- **Livelli fissati**: le soglie sono i punti medi tra livelli adiacenti, cioè $x(n)$ viene approssimato con il livello $q_i$ più vicino (**regola a minima distanza**).
- L'algoritmo applica **alternativamente** le due condizioni e itera finché l'MSE si assesta su un valore sufficientemente piccolo → [[algoritmo-lloyd-max]].

![[grafico-lloyd-max-laplace.png]]
*🧩 Grafico mio: risultato dell'algoritmo di Lloyd-Max (le due condizioni di p. 35 iterate fino a convergenza) per $M = 8$ e pdf di Laplace con $x_{rms} = 1$. Livelli $q_i = \pm0.233, \pm0.833, \pm1.672, \pm3.087$; soglie $x_i = 0, \pm0.533, \pm1.253, \pm2.380$; MSE $= 0.0545$, quindi SNR $= 10\log_{10}(1/0.0545) \approx 12.6$ dB. Si vede l'idea della slide: intervalli **stretti** dove la pdf è alta, **larghi** sulle code. Ogni soglia sta a metà fra due livelli; ogni livello è il baricentro della pdf nel suo intervallo, quindi è spostato verso lo zero rispetto al centro dell'intervallo.*

##### Limiti del quantizzatore ottimo · [[Campionamento_AD_DA.pdf#page=36|p. 36]], [[Campionamento_AD_DA.pdf#page=38|p. 38]]

1. richiede segnale **stazionario** e **pdf nota**;
2. come l'uniforme, ha prestazioni **fortemente dipendenti dal livello** del segnale.

In telefonia serve una **quantizzazione robusta**, con prestazioni circa indipendenti dal livello, vista la grande variabilità dei parlatori. La soluzione è il [[companding]]: compressione, poi quantizzazione uniforme, e in decodifica espansione.

L'idea del companding è non progettare più soglie e livelli uno per uno. Si sceglie una legge di compressione $F$ e si quantizza uniformemente il segnale compresso $F(x)$. Quantizzare uniformemente $F(x)$ equivale a quantizzare in modo non uniforme $x$: le soglie sull'asse $x$ sono $x_i = F^{-1}(y_i)$, dove $y_i$ sono le soglie equidistanti del quantizzatore uniforme. Così tutto il progetto si sposta sulla scelta di $F$ → [[companding]] (sezione «Idea chiave del companding»).

> 🎯 Esame: derivare le due condizioni (centroide, punto medio), dire perché sono solo *necessarie*, spiegare i limiti che portano al companding.

#### Perché importa · [[Campionamento_AD_DA.pdf#page=36|p. 36]]

Mostra che il quantizzatore va progettato **sulla statistica** della sorgente: con la stessa $M$, mettere intervalli più stretti dove la pdf è più alta riduce l'MSE. Le sue limitazioni motivano il [[companding]].

#### Connessioni

- [[quantizzazione-uniforme]] — caso particolare, ottimo per pdf uniforme.
- [[media-e-varianza]], [[probabilita-totale-e-bayes]] — il centroide è una media condizionale.
- [[algoritmo-lloyd-max]] — procedura iterativa.
- [[companding]] — l'alternativa robusta: realizza la quantizzazione non uniforme con compressione + quantizzazione uniforme + espansione, e riduce il progetto alla scelta di $F$.
- [[variabili-aleatorie-notevoli]] — pdf di Laplace.
- [[stazionarieta]] — l'ipotesi di stazionarietà del primo ordine: una sola $f_X$ vale per tutti i campioni, quindi un solo quantizzatore va bene in ogni istante.

#### Fonti · [[Campionamento_AD_DA.pdf#page=32|p. 32]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

- [[campionamento-conversione-ad-da]]

### Companding e quantizzazione robusta (legge logaritmica, µ-law, A-law) · [[companding|pagina]]

#### Definizione · [[Campionamento_AD_DA.pdf#page=36|p. 36]]

Il **companding** (*compressing + expanding*) realizza una quantizzazione non uniforme in tre passi:
1. **legge di compressione** $F(x)$, non lineare;
2. **quantizzazione uniforme** del segnale compresso;
3. in decodifica, la legge inversa: **espansione** $F^{-1}$.

Perché questa catena *è* un quantizzatore non uniforme, e che cosa resta da progettare, è spiegato in «Idea chiave del companding» (in questa pagina), qui sotto.

Obiettivo: **quantizzazione robusta**, cioè SNR circa **indipendente dal livello** del segnale d'ingresso. In telefonia serve per la grande variabilità dei parlatori.

Motivazione:
- il quantizzatore ottimo di Lloyd-Max assume segnale **stazionario** e richiede di conoscere la pdf;
- come il quantizzatore uniforme, ha prestazioni **fortemente dipendenti dal livello** del segnale d'ingresso;
- in telefonia è fondamentale che le prestazioni siano circa indipendenti dal livello, vista la grande variabilità dei parlatori: è la **quantizzazione robusta**;
- per studiarla si assume che la legge non uniforme sia realizzata con il companding; in decodifica si applica la legge simmetrica, l'**espansione**.

![[campionamento-p36-companding.png]]
*Schema: compressore analogico $F(x)$ → quantizzatore uniforme a $n$ bit → decodificatore uniforme a $n$ bit → espansore analogico $F^{-1}(x)$.*

> ⚠️ Probabile refuso nella figura: il secondo blocco è etichettato «n-bit uniform **decoder**» come il terzo. Dal testo («compressione seguita da una quantizzazione uniforme») dovrebbe essere l'**encoder** (quantizzatore/codificatore uniforme).

##### Idea chiave del companding · [[Campionamento_AD_DA.pdf#page=32|p. 32]], [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]–[[Campionamento_AD_DA.pdf#page=43|43]]

In una frase: **quantizzare in modo uniforme il segnale compresso $F(x)$ equivale a quantizzare in modo non uniforme il segnale vero $x$.** Per questo il progetto del quantizzatore non uniforme si riduce alla scelta della legge di compressione $F$.

**1. Il problema di partenza.** Per la voce servono intervalli **stretti** vicino a zero, dove la pdf è alta, e **larghi** sulle ampiezze grandi, che sono rare. Costruire direttamente un quantizzatore così vuol dire scegliere le $M-1$ soglie $x_i$ e gli $M$ livelli $q_i$. È quello che fa Lloyd-Max, con i limiti elencati sopra.

**2. L'idea.** Il companding non costruisce direttamente il quantizzatore non uniforme. Deforma l'asse delle ampiezze e poi usa il quantizzatore uniforme, già noto:
1. il compressore calcola $y = F(x)$;
2. un quantizzatore uniforme $Q_u$ quantizza $y$, con passo $\Delta = 2X_{max}/M$ e livelli al centro degli intervalli ([[quantizzazione-uniforme]]);
3. l'espansore riporta il livello sull'asse originale con $F^{-1}$.

**3. Perché la catena è un quantizzatore non uniforme su $x$**.
- Sull'asse $y$ le soglie $y_i$ di $Q_u$ sono equidistanti, a distanza $\Delta$.
- $F$ è crescente, quindi $x_{i-1} < x < x_i \iff F(x_{i-1}) < F(x) < F(x_i)$. In parole: $x$ cade in $R_i = (x_{i-1}, x_i)$ **se e solo se** $y = F(x)$ cade nell'intervallo uniforme $(F(x_{i-1}), F(x_i))$.
- Quindi le soglie sull'asse $x$ sono le controimmagini delle soglie uniformi: $x_i = F^{-1}(y_i)$. È la frase della slide letta al contrario: $F$ trasforma le soglie $x_{i-1}, x_i$ del quantizzatore non uniforme nelle soglie $F(x_{i-1}), F(x_i)$ di quello uniforme, e $F(x_i) - F(x_{i-1}) = \Delta$.
- Sull'asse $y$ gli intervalli hanno tutti ampiezza $\Delta$. Sull'asse $x$ hanno ampiezza $\Delta_i \approx \Delta/F'(x_i)$ (derivazione sotto): **stretti dove $F$ è ripida** ($F'$ grande), larghi dove $F$ è piatta ($F'$ piccola).

> 🧩 Derivazione mia (completa lo schema di p. 36):
> - $F$ deve essere **strettamente crescente**, altrimenti non è invertibile e l'espansore $F^{-1}$ non esiste. La legge logaritmica, la µ-law e la A-law lo sono.
> - L'uscita della catena è $F^{-1}$ del livello uniforme. In formula:
>
> $$Q(x) = F^{-1}\big(Q_u(F(x))\big)$$
>
> - Anche i livelli restituiti, $q_i = F^{-1}(\text{livello uniforme } i)$, sono quindi non uniformi. Senza l'espansore l'uscita resterebbe sulla scala compressa $y$.
> - L'equivalenza è **esatta** per qualunque $M$, perché usa solo il fatto che $F$ è crescente. È approssimata solo la formula $\Delta_i\approx\Delta/F'(x_i)$, che richiede l'alta risoluzione. Verifica numerica in «Derivazione — Esempio µ-law, soglie e livelli equivalenti» (in questa pagina).
> - Intuizione, la "lente d'ingrandimento": dove $F'>1$ il compressore allarga le ampiezze, dove $F'<1$ le schiaccia. Per la µ-law $F'(0)\approx46$ e $F'(X_{max})\approx0.18$ (calcolo nell'esempio). Il quantizzatore uniforme vede quindi le ampiezze piccole ingrandite circa 46 volte e quelle grandi rimpicciolite, e quantizza le prime molto più finemente.

**4. Cosa si sposta su $F$.**
- Il quantizzatore uniforme è **fisso**: scelto $M$, il passo è $\Delta = 2X_{max}/M$ e non c'è altro da decidere.
- Tutta la non uniformità sta in $F$: la pendenza $F'(x)$ decide dove gli intervalli su $x$ sono stretti e dove sono larghi.
- La slide di p. 39 lo rende quantitativo: $\text{MSE} = \frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$. Fissati $M$ e la pdf $f_X$, l'MSE dipende **solo da $F'$**.
- Progettare il quantizzatore non uniforme vuol dire quindi **scegliere la funzione $F$**.

> 🧩 Confronto mio: Lloyd-Max sceglie $2M-1$ numeri, cioè $M-1$ soglie e $M$ livelli. Il companding sceglie **una funzione**, e soglie e livelli ne discendono: $x_i = F^{-1}(y_i)$ e $q_i = F^{-1}(\text{livello uniforme } i)$.

**5. Con quale criterio si sceglie $F$.** Nel corso il criterio è la **robustezza**: l'SNR deve essere circa indipendente dal livello del segnale. Da questo criterio viene la legge logaritmica (derivazione sotto), approssimata in pratica dalla µ-law e dalla A-law. Non è il criterio di Lloyd-Max, cioè l'MSE minimo per una pdf nota. A pieno carico la legge logaritmica perde circa 3 dB rispetto all'uniforme con $k_c = 4$, ma mantiene l'SNR quando il livello scende (vedi *Confronto delle prestazioni*).

![[grafico-companding-soglie-mu.png]]
*🧩 Grafico mio (legge µ di p. 41, principio di p. 38; script in `output/grafici/`). $\mu = 255$, $M = 8$ ($b = 3$ bit), semiasse positivo: $F$ è dispari e il lato negativo è simmetrico. **Sinistra:** le soglie uniformi sull'asse $y$ (0.25, 0.5, 0.75, 1 in unità di $X_{max}$) scendono sull'asse $x$ attraverso la curva e diventano 0.012, 0.059, 0.247, 1. Stesso colore = stesso intervallo: quattro intervalli uguali su $y$ diventano quattro intervalli su $x$, ognuno 4 volte il precedente. Senza compressione ($F(x) = x$, puntinata) le soglie resterebbero equidistanti. **Destra:** la caratteristica della catena completa $Q(x) = F^{-1}(Q_u(F(x)))$ (arancione) confrontata con il quantizzatore uniforme con lo stesso $M$ (tratteggiata): gradini fitti vicino a zero e un solo gradino largo da 0.247 a 1. I numeri sono quelli della «Derivazione — Esempio µ-law, soglie e livelli equivalenti» (in questa pagina).*

> 🎯 Esame: spiegare perché compressione + quantizzazione uniforme + espansione equivale a un quantizzatore non uniforme su $x$, perché il progetto si riduce alla scelta di $F$, e con quale criterio la si sceglie.

#### Formule · [[Campionamento_AD_DA.pdf#page=36|p. 36]]–[[Campionamento_AD_DA.pdf#page=43|43]]

| Formula | Significato |
|---|---|
| $Q(x) = F^{-1}\big(Q_u(F(x))\big)$, soglie $x_i = F^{-1}(y_i)$ | catena compressore → quantizzatore uniforme $Q_u$ → espansore: è un quantizzatore non uniforme su $x$ |
| $\text{MSE}\approx\frac{1}{12}\sum_{i=1}^M p_i\Delta_i^2$, $\Delta_i = x_i-x_{i-1}$, $p_i\approx f_X(x_i)\Delta_i$ | MSE ad alta risoluzione |
| $\Delta_i\approx\dfrac{\Delta}{F'(x_i)} = \dfrac{1}{F'(x_i)}\dfrac{2X_{max}}{M}$ | ampiezza locale degli intervalli |
| $\text{MSE} = \dfrac{X_{max}^2}{3M^2}\displaystyle\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx$ | MSE in forma integrale |
| $\text{SNR} = \dfrac{\int_0^{X_{max}}x^2f_X(x)\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx}$ | SNR del compander |
| $F(x) = X_{max}+\frac1k\ln\frac{x}{X_{max}}$, $x\in[0,X_{max}]$ | legge logaritmica ideale |
| $\text{SNR} = \dfrac{3M^2}{k^2X_{max}^2}$ | SNR della legge logaritmica |
| $F(x) = X_{max}\dfrac{\ln(1+\mu\|x\|/X_{max})}{\ln(1+\mu)}\text{sgn}(x)$ | **µ-law** ($\mu=255$) → [[legge-mu]] |
| $x_j = \dfrac{X_{max}}{\mu}\Big[(1+\mu)^{2j/M}-1\Big]$, $j = 0,\dots,M/2$ | soglie equivalenti della µ-law sull'asse $x$ |
| $F(x) = \begin{cases}X_{max}\frac{A\|x\|/X_{max}}{1+\ln A}\text{sgn}(x) & 0\le\|x\|\le X_{max}/A\\ X_{max}\frac{1+\ln(A\|x\|/X_{max})}{1+\ln A}\text{sgn}(x) & X_{max}/A\le\|x\|\le X_{max}\end{cases}$ | **A-law** ($A=87.6$) → [[legge-a]] |

> 🧮 Formula chiave — prestazioni, segnale che impegna tutta la dinamica:
> $$\text{SNR}_{dB}\approx6.02\,b+\alpha,\qquad \alpha = \begin{cases}4.77-20\log_{10}[\ln(1+\mu)] & \mu\text{-law}\\ 4.77-20\log_{10}[1+\ln A] & A\text{-law}\\ 4.77-20\log_{10}(X_{max}/x_{rms}) & \text{uniforme}\end{cases}$$

Simboli: $M$ = numero di livelli; $\Delta = 2X_{max}/M$ = passo del quantizzatore uniforme **dopo** la compressione; $y = F(x)$ = segnale compresso [V]; $Q_u$ = quantizzatore uniforme sull'asse $y$, con soglie $y_i$ equidistanti; $F'$ = derivata della legge (adimensionale); $k$ [1/V] e $c$ [V] costanti; $\mu$, $A$ parametri adimensionali; $\text{sgn}$ = funzione segno.

#### Derivazioni

##### Derivazione — MSE ad alta risoluzione · [[Campionamento_AD_DA.pdf#page=37|p. 37]]
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
**Sanity check:** con $\Delta_i = \Delta$ si ha $\text{MSE} = \frac{\Delta^2}{12}\sum_ip_i = \frac{\Delta^2}{12}$, come in [[snr-di-quantizzazione]].

##### Derivazione — $\Delta_i \approx \Delta/F'(x_i)$ · [[Campionamento_AD_DA.pdf#page=38|p. 38]]
$$
\begin{aligned}
F(x_i)-F(x_{i-1}) &= \Delta = \frac{2X_{max}}{M} && \text{dopo la compressione gli intervalli sono uniformi} \\
\frac{\Delta}{\Delta_i} &= \frac{F(x_i)-F(x_{i-1})}{x_i-x_{i-1}} \approx F'(x_i) && \text{rapporto incrementale, } \Delta_i \text{ piccolo} \\
\Delta_i &\approx \frac{\Delta}{F'(x_i)} = \frac{1}{F'(x_i)}\frac{2X_{max}}{M}
\end{aligned}
$$
Dove $F'$ è grande (compressione "ripida") gli intervalli originali sono **stretti**.

> 🧩 Lettura mia: è la forma quantitativa dell'«Idea chiave del companding» (in questa pagina). Intervalli uguali ($\Delta$) sull'asse compresso corrispondono a intervalli diversi ($\Delta_i$) sull'asse $x$, e il fattore di conversione è la pendenza locale $F'(x_i)$. Il segno $\approx$ viene solo dal rapporto incrementale sostituito con la derivata: le soglie $x_i = F^{-1}(y_i)$ sono esatte.

![[campionamento-p38-legge-compressione.png]]
*Legge di compressione $F(x)$ concava: l'intervallo $\Delta_i = x_i - x_{i-1}$ sull'asse $x$ viene mappato in un intervallo di ampiezza $\Delta$ sull'asse $F(x)$. Dove la curva è ripida, un $\Delta_i$ piccolo basta a coprire un $\Delta$ intero.*

##### Derivazione — MSE e SNR in forma integrale · [[Campionamento_AD_DA.pdf#page=39|p. 39]]
$$
\begin{aligned}
\text{MSE} &= \frac{1}{12}\sum_ip_i\Delta_i^2 = \frac1{12}\sum_ip_i\frac{4X_{max}^2}{M^2[F'(x_i)]^2} && \text{sostituisco } \Delta_i \\
&= \frac{X_{max}^2}{3M^2}\sum_i\frac{f_X(x_i)}{[F'(x_i)]^2}\Delta_i && 4/12 = 1/3;\ p_i = f_X(x_i)\Delta_i \\
&\to \frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X(x)}{[F'(x)]^2}dx && \Delta_i\to dx \text{ (somma di Riemann)} \\
\text{SNR} &= \frac{E[x^2]}{\text{MSE}} = \frac{\int_{-X_{max}}^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_{-X_{max}}^{X_{max}}\frac{f_X}{[F']^2}dx} && f_X = 0 \text{ fuori da } (-X_{max},X_{max}) \\
&= \frac{\int_0^{X_{max}}x^2f_X\,dx}{\frac{X_{max}^2}{3M^2}\int_0^{X_{max}}\frac{f_X}{[F']^2}dx} && f_X \text{ pari, } F \text{ dispari} \Rightarrow F' \text{ pari: integrandi pari, il fattore 2 si semplifica}
\end{aligned}
$$

##### Derivazione — Legge logaritmica ottima per la robustezza · [[Campionamento_AD_DA.pdf#page=40|p. 40]]
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
**Conclusione della slide**: per una pdf $f_X(x)$ **arbitraria**, la legge di compressione che rende l'SNR indipendente dal livello del segnale è di tipo **logaritmico**.
**Interpretazione**: $\Delta_i = \Delta/F'(x_i) = \Delta\,k\,x_i$, cioè l'intervallo raddoppia quando raddoppia il livello, e l'errore **relativo** resta costante.
**Limite:** per $x\to0$, $F(x)\to-\infty$, quindi non è implementabile esattamente. Si usano approssimazioni con $F(0) = 0$: µ-law e A-law.

##### Derivazione — Costante $\alpha$ per µ-law · [[Campionamento_AD_DA.pdf#page=43|p. 43]]
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
**Numeri:** $\mu = 255$: $\ln256 = 5.545$; $20\log_{10}5.545 = 14.88$ dB; $\alpha = 4.77-14.88 = -10.11$ dB ✓.
**Termine trascurato:** esattamente $1/F'(x) = \frac{\ln(1+\mu)}{X_{max}}\left(x + \frac{X_{max}}{\mu}\right)$. L'approssimazione trascura $X_{max}/\mu$ rispetto a $|x|$, quindi vale per $|x|\gg X_{max}/255$; per segnali molto deboli l'SNR peggiora.

##### Derivazione — Costante $\alpha$ per A-law
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

##### Derivazione — Controlli sulle leggi µ e A · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]
> 🧩 Sanity check miei
- $F(X_{max}) = X_{max}$ per entrambe: $\ln(1+\mu)/\ln(1+\mu) = 1$ e $(1+\ln A)/(1+\ln A) = 1$ ✓.
- A-law continua in $|x| = X_{max}/A$: entrambi i rami valgono $X_{max}/(1+\ln A)$ ✓.
- µ-law con $\mu\to0$: $\ln(1+\mu a)/\ln(1+\mu)\to\mu a/\mu = a$, quindi $F(x) = x$ ✓.
- A-law con $A = 1$: la soglia $X_{max}/A = X_{max}$ copre tutto il range, e $F(x) = X_{max}\cdot\frac{|x|/X_{max}}{1}\text{sgn}(x) = x$ ✓.

##### Derivazione — Esempio µ-law, soglie e livelli equivalenti · [[Campionamento_AD_DA.pdf#page=37|p. 37]], [[Campionamento_AD_DA.pdf#page=38|38]], [[Campionamento_AD_DA.pdf#page=40|p. 40]], [[Campionamento_AD_DA.pdf#page=41|41]]
**Fonte:** p. 41 (µ-law), p. 38 (soglie $x_i \leftrightarrow F(x_i)$), p. 40 (intervallo che raddoppia col livello)
> 🧩 Derivazione mia: rende numerica l'«Idea chiave del companding» (in questa pagina). Lavoro sul semiasse $0\le x\le X_{max}$; il semiasse negativo è simmetrico perché $F$ è dispari.

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
- Caso limite $\mu\to0$: per Taylor $(1+\mu)^{2j/M}\approx1+\frac{2j}{M}\mu$, quindi $x_j\approx\frac{X_{max}}{\mu}\cdot\frac{2j}{M}\mu = j\Delta$. Si ritrova il quantizzatore uniforme, coerente con $F(x) = x$ per $\mu = 0$ ✓.
- Livelli: $q_4 = 0.498\,X_{max}$ non sta al centro di $R_4 = (0.247, 1)\,X_{max}$, che è $0.624\,X_{max}$. $F^{-1}$ non è lineare e sposta verso lo zero il centro dell'intervallo uniforme. Con $M = 8$ non siamo ad alta risoluzione. Al crescere di $M$, $F$ è quasi lineare dentro ogni intervallo e $q_i$ torna circa al centro, come assume p. 37.

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

**Collegamento con p. 40.** Con $M = 16$ il rapporto è esattamente 2: ogni intervallo è il doppio del precedente, e le soglie $x_j = \frac{2^j-1}{255}X_{max}$ quasi raddoppiano a ogni passo. È il comportamento della legge logaritmica descritto a p.40: l'intervallo raddoppia quando raddoppia il livello. In generale, dal passo 2 si ha $\frac{X_{max}}{\mu}(1+\mu)^{2(j-1)/M} = x_{j-1}+\frac{X_{max}}{\mu}$, e sostituendo nel passo 3:
$$\Delta_j = \Big(x_{j-1}+\frac{X_{max}}{\mu}\Big)\Big[(1+\mu)^{2/M}-1\Big]$$
L'ampiezza è proporzionale al livello $x_{j-1}$, a meno della costante $X_{max}/\mu$. Per $x\gg X_{max}/\mu$ il comportamento è logaritmico puro ($\Delta_i\propto x_i$). La costante è il prezzo di avere $F(0) = 0$: è lo stesso termine trascurato nella derivazione di $\alpha$ per la µ-law.

**Ipotesi:** $F$ = µ-law (strettamente crescente e dispari); quantizzatore uniforme simmetrico con $M$ pari e livelli al centro degli intervalli; nessun sovraccarico ($|x|\le X_{max}$).

#### Spiegazione

##### Confronto delle prestazioni · [[Campionamento_AD_DA.pdf#page=43|p. 43]]

| Quantizzatore | $\text{SNR}_{dB}$ | Dipende dal livello? |
|---|---|---|
| A-law, $A=87.6$ | $6.02b-9.99$ | no (idealmente) |
| µ-law, $\mu=255$ | $6.02b-10.11$ | no (idealmente) |
| Uniforme, $k_c=4$ | $6.02b-7.3$ | **sì**, tramite $k_c = X_{max}/x_{rms}$ |

La legge dei 6 dB/bit vale ancora. A pieno carico il companding perde circa 3 dB rispetto all'uniforme con $k_c=4$, ma **mantiene** l'SNR quando il segnale si abbassa, mentre l'uniforme perde 6 dB per ogni dimezzamento di $x_{rms}$.

> 🧩 Derivazione mia (il confronto quantitativo): $-7.3-(-9.99)\approx2.7$ dB e $-7.3-(-10.11)\approx2.8$ dB. Con un segnale 20 dB sotto il four-sigma loading ($k_c = 40$), l'uniforme dà $6.02b + 4.77 - 32.04 = 6.02b - 27.3$ dB: 17 dB peggio del compander.

![[campionamento-p43-prestazioni-companding.png]]
*SNR (dB) in funzione del livello relativo d'ingresso (dB, da −50 a 0) — p. 43. La curva **µ-law** ($\mu = 255$) è quasi piatta su un ampio intervallo di livelli e cala solo per livelli molto bassi. La retta della **quantizzazione uniforme** (senza companding) cresce di 1 dB per ogni dB di livello, supera la µ-law solo vicino al fondo scala e le resta nettamente sotto per segnali deboli. La tacca a −4.77 dB sull'asse orizzontale segna l'estremo destro del grafico.*

> 🧩 Lettura mia della figura: la pendenza unitaria della retta uniforme discende da $\text{SNR}_{dB} = 6.02b + 4.77 - 20\log_{10}(X_{max}/x_{rms})$. Ogni dB in più di $x_{rms}$ riduce $[k_c]_{dB}$ di 1 dB.

##### Grafico SNR in funzione del livello, anche per la legge A · [[Campionamento_AD_DA.pdf#page=39|p. 39]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

![[grafico-snr-vs-livello-companding.png]]
*🧩 Grafico mio. Ricostruisce il grafico di p. 43 con le formule della slide, e aggiunge la legge A. Parametri: $b = 8$, ingresso di Laplace con $x_{rms}$ variabile, sovraccarico trascurato. Le curve µ e A si assestano proprio su $6.02b + \alpha$: $48.2 - 10.11 = 38.0$ dB e $48.2 - 9.99 = 38.2$ dB. Tra −40 e 0 dB restano entro circa 2.5 dB da quel valore (quantizzazione robusta), mentre la retta uniforme perde 1 dB per ogni dB di livello. L'uniforme è migliore solo sopra circa −15 dB. Con $k_c = 4$, cioè livello $-12$ dB, vale $48.2 - 7.3 = 40.9$ dB, in accordo con il valore di p. 43. La legge A cala prima della µ a livelli molto bassi: sotto $X_{max}/A$ lavora nel tratto lineare, che equivale a un quantizzatore uniforme.*

> 🧩 Derivazione mia delle curve (formula integrale di p. 39, $\text{MSE} = \frac{X_{max}^2}{3M^2}E\big[1/F'(x)^2\big]$, ingresso di Laplace con $\lambda = \sqrt2/x_{rms}$, $E|x| = x_{rms}/\sqrt2$):
> $$
> \begin{aligned}
> \text{uniforme: } F' = 1 &\Rightarrow \text{SNR} = 3M^2\,x_{rms}^2/X_{max}^2 \\
> \mu\text{-law: } \frac{1}{F'(x)} = \frac{\ln(1+\mu)}{\mu}\Big(1+\frac{\mu|x|}{X_{max}}\Big) &\Rightarrow E\Big[\frac{1}{F'^2}\Big] = \frac{\ln^2(1+\mu)}{\mu^2}\Big(1 + \frac{2\mu E|x|}{X_{max}} + \frac{\mu^2x_{rms}^2}{X_{max}^2}\Big) \\
> A\text{-law: } \frac{1}{F'(x)^2} = (1+\ln A)^2\cdot\begin{cases}1/A^2 & |x|<X_{max}/A\\ x^2/X_{max}^2 & \text{altrimenti}\end{cases} &\Rightarrow E\Big[\frac{1}{F'^2}\Big] = (1+\ln A)^2\Big[\frac{1-e^{-\lambda a}}{A^2} + \frac{e^{-\lambda a}(a^2+2a/\lambda+2/\lambda^2)}{X_{max}^2}\Big],\ a = \frac{X_{max}}{A}
> \end{aligned}
> $$
> Per $\mu|x|\gg X_{max}$ il termine dominante della µ-law è $\mu^2x_{rms}^2/X_{max}^2$: si ritrova $\text{SNR} = 3M^2/\ln^2(1+\mu)$, cioè il valore costante della slide.

##### Curve delle leggi µ e A · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]
![[campionamento-p41-mu-law.png]]
*$F(x)$ normalizzata (output vs input in $[0,1]$) per $\mu = 0, 1, 5, 100, 255$ — p. 41. Con $\mu = 0$ è la bisettrice (uniforme); al crescere di $\mu$ la curva è sempre più ripida vicino a 0, cioè comprime di più.*

![[campionamento-p42-a-law.png]]
*$F(x)$ normalizzata per $A = 1, 2, 5, 87.6, 100$ — p. 42. Con $A = 1$ è la bisettrice (uniforme); al crescere di $A$ la compressione aumenta.*

> 🎯 Esame: derivare la legge logaritmica dalla richiesta "SNR indipendente da $f_X$"; spiegare perché serve µ/A-law; confrontare gli SNR; sapere µ=255 (USA, Canada, Giappone) e A=87.6 (Europa, collegamenti internazionali), entrambe nella [[g711]].

#### Perché importa · [[Campionamento_AD_DA.pdf#page=36|p. 36]], [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]

Risolve il problema della quantizzazione robusta posto dalle applicazioni telefoniche. Le approssimazioni a 7 segmenti delle leggi µ e A sono standardizzate dall'ITU-T in [[g711]].

#### Connessioni

- [[quantizzazione-non-uniforme]] — il companding la realizza con compressione + quantizzazione uniforme + espansione, e riduce il progetto alla scelta di $F$ («Idea chiave del companding» (in questa pagina)).
- [[quantizzazione-uniforme]] — è il blocco centrale della catena: il companding lo riusa così com'è, invece di progettare un quantizzatore nuovo.
- [[snr-di-quantizzazione]] — stessa pendenza di 6 dB/bit, costante diversa.
- [[funzione-di-variabile-aleatoria]] — $F(x)$ è una trasformazione non lineare della v.a. $x(n)$.
- [[legge-mu]], [[legge-a]], [[g711]] — le leggi e lo standard.
- [[variabili-aleatorie-notevoli]] — pdf di Laplace della voce.

#### Fonti · [[Campionamento_AD_DA.pdf#page=36|p. 36]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- [[campionamento-conversione-ad-da]]

### Campionamento e aliasing · [[campionamento-e-aliasing|pagina]]

#### Metodo

1. Individuare la **banda monolatera** $f_m$ del segnale (per una sinusoide: la sua frequenza).
2. **Nyquist**: $f_c\ge2f_m$ ([[teorema-del-campionamento]]).
3. Se $f_c<2f_m$, trovare la **frequenza alias**: per ogni componente $f_0>f_c/2$, cercare la replica $|f_0-kf_c|$ che cade in $[0,f_c/2]$. Per $f_c/2<f_0<f_c$ si ha $f_c-f_0$ ([[aliasing]]).
4. **Numero di campioni** in una durata $T$: $N = T\cdot f_c$ (× numero di canali).
5. Controllare le unità: kHz × s = migliaia di campioni.

#### Formule usate · [[Campionamento_AD_DA.pdf#page=14|p. 14]], [[Campionamento_AD_DA.pdf#page=16|p. 16]], [[Campionamento_AD_DA.pdf#page=18|p. 18]]

- $f_c\ge2f_m$ — [[teorema-del-campionamento]]
- $f_{alias} = f_c-f_0$ — [[aliasing]]
- $N = T\,f_c$

#### Casi svolti

##### Caso 1 — Frequenze di Nyquist di voce, audio, video · [[Campionamento_AD_DA.pdf#page=16|p. 16]]
**Traccia**: banda monolatera 4 kHz (voce), 20 kHz (audio), 5 MHz (video). Frequenza minima di campionamento?
$$
\begin{aligned}
f_{c,\min} &= 2f_m && \text{Nyquist} \\
\text{voce: } &2\times4\,\text{kHz} = 8\,\text{kHz} \\
\text{audio: } &2\times20\,\text{kHz} = 40\,\text{kHz} \\
\text{video: } &2\times5\,\text{MHz} = 10\,\text{MHz}
\end{aligned}
$$
**Sanity check:** il CD audio usa 44.1 kHz, cioè più di 40 kHz: un leggero sovracampionamento che lascia spazio al filtro antialiasing reale (🧩 mia interpretazione).

##### Caso 2 — Campioni in 1 minuto di audio · [[Campionamento_AD_DA.pdf#page=16|p. 16]]
**Traccia**: 1 minuto di audio mono a $f_c = 44.1$ kHz. Quanti campioni? E in stereo?
$$
\begin{aligned}
N_{mono} &= T\cdot f_c = 60\,\text{s}\times44\,100\,\text{campioni/s} && \text{sostituisco} \\
&= 2\,646\,000\ \text{campioni} \\
N_{stereo} &= 2\times N_{mono} = 5\,292\,000\ \text{campioni} && \text{canali L e R}
\end{aligned}
$$
**Risultato:** 2 646 000 campioni (mono) ✓ come la slide; il doppio in stereo.

##### Caso 3 — Sinusoide sottocampionata · [[Campionamento_AD_DA.pdf#page=18|p. 18]]
**Traccia**: sinusoide a $f_0 = 1.5$ kHz campionata a $f_c = 2$ kHz. A quale frequenza viene ricostruita?
$$
\begin{aligned}
f_c/2 &= 1\,\text{kHz} < f_0 = 1.5\,\text{kHz} && \Rightarrow \text{aliasing} \\
f_{alias} &= f_c - f_0 = 2 - 1.5 = 0.5\,\text{kHz} && f_c/2<f_0<f_c
\end{aligned}
$$
**Verifica sui campioni** (derivazione completa in [[aliasing]]): $\cos(2\pi\cdot0.75\,n) = \cos(2\pi\cdot0.25\,n)$ per $n$ intero, e $0.25\cdot2\,\text{kHz} = 0.5$ kHz ✓.
**Risultato:** 0.5 kHz. Per evitare l'aliasing servirebbe $f_c\ge3$ kHz.
**Perché proprio 0.5 kHz:** i campioni del coseno a 1.5 kHz (1, 0, −1, 0, 1, …) sono anche quelli dei coseni a 0.5, 2.5, 3.5 kHz, …, e il filtro di ricostruzione lascia passare solo $|f| < f_c/2 = 1$ kHz. Ragionamento completo, con due animazioni: [[aliasing]] (sezione «Perché il segnale ricostruito è a 0.5 kHz»).

#### Trappole

- $f_c\ge2f_m$ con $f_m$ banda **monolatera**, non la larghezza totale dello spettro bilatero.
- Con $f_c = 2f_m$ esatto serve un filtro perfettamente ideale ($f_r = f_m$ esatta): in pratica si sovracampiona.
- La formula $f_c-f_0$ vale solo per $f_c/2<f_0<f_c$. Per $f_0>f_c$ bisogna prima sottrarre multipli di $f_c$.
- Il ricostruttore non "sa" quale fosse la frequenza vera: restituisce sempre la replica che cade sotto $f_c/2$ ([[aliasing]] (sezione «Perché il segnale ricostruito è a 0.5 kHz»)).
- Il filtro **antialiasing** va *prima* del campionatore ed è analogico; il filtro di **ricostruzione** va *dopo*, nella D/A ([[aliasing]], [[interpolazione]]).
- Stereo = 2 canali: raddoppiare campioni e bit.

### Dimensionamento di un quantizzatore e bit rate · [[dimensionamento-quantizzatore|pagina]]

#### Metodo · [[Campionamento_AD_DA.pdf#page=31|p. 31]]

1. **Fissare $k_c$** in base alla probabilità di sovraccarico ammessa: $P_s\le1/k_c^2$, cioè $k_c\ge1/\sqrt{P_s}$ ([[disuguaglianza-di-chebyshev]]). Default: $k_c = 4$ (four-sigma loading).
2. **Calcolare $[k_c]_{dB} = 20\log_{10}k_c$** (rapporto di ampiezze, quindi $20\log$).
3. **Invertire la legge dei 6 dB/bit** ([[snr-di-quantizzazione]]):
   $$b\ge\frac{\text{SNR}_{dB}+[k_c]_{dB}-4.77}{6.02}$$
   e arrotondare **per eccesso** all'intero.
4. **Verificare**: ricalcolare l'SNR con il $b$ scelto, e anche con $b-1$ per controllare che non basti.
5. **Bit rate**: $R_b = b\cdot f_c$ per canale; per $n_{ch}$ canali, $R_{tot} = n_{ch}\,b\,f_c$.
6. **Memoria**: bit $= R_{tot}\cdot T$; poi byte (÷8), kB (÷1000), MB (÷1000) secondo ISO/IEC.
7. Con companding: $\text{SNR}_{dB}\approx6.02b+\alpha$, con $\alpha = -9.99$ (A-law) o $-10.11$ (µ-law) ([[companding]]).

#### Formule usate · [[Campionamento_AD_DA.pdf#page=26|p. 26]], [[Campionamento_AD_DA.pdf#page=27|27]], [[Campionamento_AD_DA.pdf#page=29|p. 29]], [[Campionamento_AD_DA.pdf#page=30|30]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- $\Delta = 2X_{max}/M$, $M = 2^b$ — [[quantizzazione-uniforme]]
- $P_s\le1/k_c^2$ — [[disuguaglianza-di-chebyshev]]
- $\text{SNR}_{dB} = 6.02b-[k_c]_{dB}+4.77$ — [[snr-di-quantizzazione]]
- $\text{SNR}_{dB}\approx6.02b+\alpha$ — [[companding]]

#### Casi svolti

##### Caso 1 — Four-sigma loading · [[Campionamento_AD_DA.pdf#page=29|p. 29]]
**Traccia**: $k_c = 4$. Probabilità di sovraccarico massima?
$$P_s\le\frac{1}{k_c^2} = \frac{1}{16} = 0.0625 = 6.25\%$$
**Sanity check:** per un segnale gaussiano il valore vero è $2Q(4)\approx6.3\cdot10^{-5}$ ([[variabile-aleatoria-gaussiana]]); Chebyshev è molto conservativo.

##### Caso 2 — Esempio 7.6: quantizzatore audio a 85 dB · Campionamento [[Campionamento_AD_DA.pdf#page=31|p. 31]] · Intro [[Intro.pdf#page=15|p. 15]]
**Traccia**: si vuole $\text{SNR}_{dB} = 85$ dB con $k_c = 4$. Quanti bit? Bit rate per audio stereo a $f_c = 44.1$ kHz? Memoria per 1 minuto?

**Dati:** $\text{SNR}_{dB} = 85$ dB, $k_c = 4$, $f_c = 44.1$ kHz, 2 canali, $T = 60$ s.

**Passo 1 — numero di bit** (la slide dà solo «$b = 16$»):
$$
\begin{aligned}
[k_c]_{dB} &= 20\log_{10}4 = 20\times0.60206 = 12.04\,\text{dB} && \text{fattore di carico in dB} \\
6.02\,b - 12.04 + 4.77 &\ge 85 && \text{legge dei 6 dB/bit} \\
6.02\,b &\ge 85 + 12.04 - 4.77 = 92.27 && \text{isolo } b \\
b &\ge 92.27/6.02 = 15.33 && \\
b &= 16 && \text{arrotondo per eccesso}
\end{aligned}
$$
**Verifica:**
- $b = 16$: $6.02\times16-7.27 = 96.32-7.27 = 89.05$ dB ≥ 85 ✓;
- $b = 15$: $90.30-7.27 = 83.03$ dB < 85 ✗.

**Passo 2 — bit rate per canale:**
$$R_b = b\cdot f_c = 16\,\text{bit/campione}\times44\,100\,\text{campioni/s} = 705\,600\,\text{bit/s} = 705.6\,\text{kbit/s}$$

**Passo 3 — memoria per 1 minuto stereo:**
$$
\begin{aligned}
N_{bit} &= n_{ch}\times T\times f_c\times b = 2\times60\times44\,100\times16 && \text{canali} \times \text{s} \times \text{campioni/s} \times \text{bit/campione} \\
&= 2\times60 = 120;\quad 120\times44\,100 = 5\,292\,000;\quad 5\,292\,000\times16 = 84\,672\,000\,\text{bit} \\
&= 84\,672\,000/8 = 10\,584\,000\,\text{byte} && 1\,\text{byte} = 8\,\text{bit} \\
&= 10\,584\,\text{kB}\approx10.6\,\text{MB} && 1\,\text{kB} = 1000\,\text{byte},\ 1\,\text{MB} = 1000\,\text{kB}
\end{aligned}
$$
**Risultato:** $b = 16$ bit; 705.6 kbit/s per canale; ≈ 10.6 MB/minuto (tutti ✓ con la slide).
**Sanity check** (🧩 mio): bit rate stereo totale $= 2\times705.6 = 1411.2$ kbit/s, e $1411.2\,\text{kbit/s}\times60\,\text{s} = 84\,672$ kbit ✓. È circa 10× i 128 kbit/s di un MP3, in accordo con la stima «around ten times higher» per l'audio professionale.

##### Caso 3 — Costanti $\alpha$ del companding · [[Campionamento_AD_DA.pdf#page=43|p. 43]]
**Traccia**: verificare $\alpha = -9.99$ dB (A-law, $A=87.6$), $-10.11$ dB (µ-law, $\mu=255$), $-7.3$ dB (uniforme, $k_c=4$).
$$
\begin{aligned}
\text{A-law: } \alpha &= 4.77-20\log_{10}(1+\ln87.6) = 4.77-20\log_{10}(1+4.473) && \ln87.6 = 4.4728 \\
&= 4.77-20\log_{10}5.473 = 4.77-20\times0.7382 = 4.77-14.76 = -9.99\,\text{dB} \\
\mu\text{-law: } \alpha &= 4.77-20\log_{10}\ln256 = 4.77-20\log_{10}5.545 && \ln256 = 8\ln2 = 5.5452 \\
&= 4.77-20\times0.7439 = 4.77-14.88 = -10.11\,\text{dB} \\
\text{uniforme: } \alpha &= 4.77-20\log_{10}4 = 4.77-12.04 = -7.27\approx-7.3\,\text{dB}
\end{aligned}
$$
**Risultato:** tutti ✓.

#### Trappole · [[Campionamento_AD_DA.pdf#page=31|p. 31]]

- **$[k_c]_{dB}$ usa $20\log_{10}$**, non $10\log_{10}$: $k_c$ è un rapporto di ampiezze.
- **Arrotondare $b$ per eccesso**: 15.33 → 16, non 15.
- La legge dei 6 dB/bit ignora il **sovraccarico**: se $k_c$ è piccolo, l'SNR reale è peggiore.
- **Stereo** = 2 canali; «per canale» vs «totale».
- **Unità di memoria**: le slide usano i fattori ISO/IEC decimali (1 kB = 1000 byte), non 1024.
- Le costanti $\alpha$ del companding valgono con il segnale che impegna **tutta la dinamica**.

### Algoritmo di Lloyd-Max · [[algoritmo-lloyd-max|pagina]]

#### Cos'è · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=35|35]]

Procedura iterativa che progetta il quantizzatore **ottimo MMSE** per una pdf $f_X$ nota: cerca i livelli di decisione $x_1,\dots,x_{M-1}$ e i livelli di restituzione $q_1,\dots,q_M$ che minimizzano
$$\text{MSE} = \sum_{i=1}^M\int_{R_i}(q_i-x)^2f_X(x)\,dx$$
Il problema non ha soluzione in forma chiusa. L'algoritmo alterna le due condizioni necessarie (derivate in [[quantizzazione-non-uniforme]]):

1. **inizializza** i livelli di decisione (es. quelli uniformi);
2. **centroide**: con le regioni fissate, $q_i = E[x\,|\,x\in R_i]$;
3. **punto medio**: con i livelli fissati, $x_i = (q_i+q_{i+1})/2$;
4. ripeti 2–3 finché l'MSE si assesta su un valore sufficientemente piccolo.

> 🧩 Derivazione mia: ogni passo non aumenta l'MSE, perché ottimizza esattamente rispetto a un sottoinsieme di variabili con le altre fisse. L'MSE è limitato inferiormente da 0, quindi la successione converge. Può però convergere a un minimo **locale**: le condizioni sono solo necessarie.

#### Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=32|p. 32]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

È il quantizzatore ottimo per sorgenti stazionarie a pdf nota (es. voce modellata con Laplace). Limiti: serve conoscere la pdf e le prestazioni dipendono dal livello del segnale. Per questo in telefonia si preferisce il [[companding]].

#### Concetti correlati

- [[quantizzazione-non-uniforme]], [[media-e-varianza]] (media condizionale), [[companding]]
- [[stazionarieta]] — "sorgente stazionaria" (del primo ordine) vuol dire che la pdf dei campioni non cambia nel tempo

#### Fonti · [[Campionamento_AD_DA.pdf#page=34|p. 34]], [[Campionamento_AD_DA.pdf#page=36|p. 36]]

- [[campionamento-conversione-ad-da]]

### Legge µ (µ-law) · [[legge-mu|pagina]]

#### Cos'è · [[Campionamento_AD_DA.pdf#page=41|p. 41]]

Legge di compressione per il [[companding]]:
$$F(x) = X_{max}\frac{\ln(1+\mu|x|/X_{max})}{\ln(1+\mu)}\,\text{sgn}(x),\qquad |x|\le X_{max}$$
- $\mu$ (adimensionale) regola il grado di compressione; valore usato: $\mu = 255$;
- $\mu = 0$: $F(x) = x$, cioè quantizzazione uniforme;
- usata in Stati Uniti, Canada e Giappone; approssimazione a 7 segmenti in [[g711]].

![[campionamento-p41-mu-law.png]]

#### Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=43|p. 43]]

È un'approssimazione della legge logaritmica ideale che vale $0$ in $x=0$: il termine "$1+$" evita $\ln0 = -\infty$. Prestazioni:
$$\text{SNR}_{dB}\approx6.02\,b+4.77-20\log_{10}\ln(1+\mu)\overset{\mu=255}{=}6.02\,b-10.11$$
La derivazione di $\alpha$, i controlli ($F(X_{max}) = X_{max}$, limite $\mu\to0$) e l'approssimazione usata ($\mu|x|/X_{max}\gg1$) sono in [[companding]].

Come ogni legge di compressione, trasforma il quantizzatore uniforme in un quantizzatore non uniforme sull'asse $x$ ([[companding]] (sezione «Idea chiave del companding»)). Le soglie equivalenti sono $x_j = \frac{X_{max}}{\mu}\big[(1+\mu)^{2j/M}-1\big]$. Con $\mu = 255$ e $M = 8$ valgono $0.0118$, $0.0588$, $0.247$ e $1$ (in unità di $X_{max}$): ogni intervallo è 4 volte più largo del precedente (🧩 derivazione in [[companding]] (sezione «Derivazione — Esempio µ-law, soglie e livelli equivalenti»)).

#### Concetti correlati

- [[companding]], [[legge-a]], [[g711]], [[snr-di-quantizzazione]]

#### Fonti · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=43|p. 43]]

- [[campionamento-conversione-ad-da]]

### Legge A (A-law) · [[legge-a|pagina]]

#### Cos'è · [[Campionamento_AD_DA.pdf#page=42|p. 42]]

Legge di compressione per il [[companding]], definita a tratti:
$$
F(x) = \begin{cases}
X_{max}\dfrac{A|x|/X_{max}}{1+\ln A}\,\text{sgn}(x) & 0\le|x|\le X_{max}/A \quad\text{(tratto lineare)}\\[2mm]
X_{max}\dfrac{1+\ln(A|x|/X_{max})}{1+\ln A}\,\text{sgn}(x) & X_{max}/A\le|x|\le X_{max}\quad\text{(tratto logaritmico)}
\end{cases}
$$
- $A$ (adimensionale) regola il grado di compressione; valore usato: $A = 87.6$;
- $A = 1$: $F(x) = x$, cioè quantizzazione uniforme;
- usata in Europa e nei collegamenti internazionali; approssimazione a 7 segmenti in [[g711]].

![[campionamento-p42-a-law.png]]

#### Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=43|p. 43]]

Il tratto lineare vicino a zero risolve il problema $\ln0 = -\infty$ della legge logaritmica ideale. Prestazioni:
$$\text{SNR}_{dB}\approx6.02\,b+4.77-20\log_{10}(1+\ln A)\overset{A=87.6}{=}6.02\,b-9.99$$
Derivazione di $\alpha$ e verifiche (continuità in $X_{max}/A$, caso $A=1$) in [[companding]].

> 🧩 Derivazione mia: con $A=87.6$ la soglia lineare/logaritmica è a $X_{max}/87.6\approx0.0114\,X_{max}$, cioè circa $-38.9$ dB sotto il fondo scala ($20\log_{10}87.6 = 38.85$).

#### Concetti correlati

- [[companding]], [[legge-mu]], [[g711]], [[snr-di-quantizzazione]]

#### Fonti · [[Campionamento_AD_DA.pdf#page=42|p. 42]], [[Campionamento_AD_DA.pdf#page=43|43]]

- [[campionamento-conversione-ad-da]]

### ITU-T G.711 · [[g711|pagina]]

#### Cos'è · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]

Raccomandazione dell'**ITU-T** che standardizza un'**approssimazione a 7 segmenti** delle leggi di compressione logaritmica [[legge-mu]] e [[legge-a]]. Nelle slide viene citata alla fine della descrizione di ciascuna legge.

#### Come si usa nel corso · [[Campionamento_AD_DA.pdf#page=36|p. 36]], [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]

- Esempio concreto di [[companding]] standardizzato, cioè di quantizzazione robusta in telefonia.
- Varianti regionali:
  - µ-law ($\mu = 255$): Stati Uniti, Canada e Giappone;
  - A-law ($A = 87.6$): Europa e collegamenti internazionali.
- "Approssimazione a 7 segmenti" significa che la curva logaritmica continua $F(x)$ viene sostituita da una spezzata, cioè da tratti lineari, più semplice da realizzare. Le slide non ne danno i dettagli.

#### Concetti correlati

- [[companding]], [[legge-mu]], [[legge-a]]

#### Fonti · [[Campionamento_AD_DA.pdf#page=41|p. 41]], [[Campionamento_AD_DA.pdf#page=42|42]]

- [[campionamento-conversione-ad-da]]


---

## Lezione 4 — Rappresentazione complessa in banda base

### Modulazione digitale · [[modulazione-digitale|pagina]]

#### Definizione · Rice [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=3|3]] · Intro [[Intro.pdf#page=16|p. 16]]

La **modulazione** è la rappresentazione dell'informazione digitale con **forme d'onda analogiche** che si possono trasmettere su canali fisici. Nota a mano sulla slide: è «il processo che permette di rappresentare l'informazione digitale tramite forme d'onda analogiche». È il compito del blocco **modulatore** dello schema del sistema digitale ([[sistema-comunicazione-digitale]]).

Gli appunti a mano di p. 2 (pagina di appunti, prima della slide 2) mettono il modulatore nella catena:
- la sorgente produce $s(n)$, un segnale già ridotto a stringhe di bit;
- il modulatore (MOD) **associa una forma d'onda analogica a ogni simbolo o stringa di bit** e produce $s(t)$, che va sul canale fisico;
- deve **allocare** questo segnale in una specifica porzione dello spettro delle frequenze, **centrata attorno a una frequenza portante** $f_c$ (*carrier*);
- il segnale attraversa poi il **canale**, caratterizzato da una sua risposta in frequenza e da una determinata banda a disposizione.

Sempre negli appunti di p.2: sia in trasmissione sia in ricezione c'è un passaggio tra segnale complesso e segnale reale, ed è eseguito da un DSP.
- **In trasmissione:** complesso → reale.
- **In ricezione:** reale → complesso.

Il perché è in [[inviluppo-complesso]] e [[upconversion-e-downconversion]].

![[rappresentazione-rice-p2-appunti-sistema-e-canale.png]]
*Appunti a mano.*
- *In alto a sinistra: sorgente S → $s(n)$ → MOD → $s(t)$ → canale fisico, con la definizione del modulatore.*
- *A destra: risposta in frequenza $H(f)$ di un canale passa-banda, con due lobi di larghezza $B$ (la "banda utile") centrati in $\pm f_c$, dove $f_c$ è la portante.*
- *Sotto: il trasmettitore porta il segnale nella porzione di spettro prevista, per adattarlo al canale; il ricevitore lo riporta in banda base, e questo rende il segnale complesso. Il passaggio complesso ↔ reale avviene in entrambe le fasi.*

> ⚠️ Nel disegno il lobo di sinistra è etichettato $f_c$: è il lobo in $-f_c$.

#### Formule · [[Rappresentazione_Rice.pdf#page=3|p. 3]]

La slide descrive la modulazione lineare a parole; la formula è scritta a mano accanto alla figura:
$$s(t) = \sum_{m} b[m]\,\Pi(t - mT), \qquad b \in \{-1, 1\}$$
- $b[m] \in \{-1, +1\}$: simboli, adimensionali;
- $\Pi$: impulso rettangolare, di durata $T$ nell'esempio della slide; è adimensionale, perché l'ampiezza del segnale la danno i simboli;
- $T$: intervallo di simbolo [s]; $\Pi(t - mT)$ è la copia dell'impulso traslata all'intervallo $m$-esimo.

> ⚠️ Negli appunti la somma è scritta da $i = 1$ a $m$, ma il termine dipende da $m$: la somma va letta sull'indice $m$ dei simboli.
> 🧩 Scrittura generale (mia), usata in [[calcolo-densita-spettrale]]: con un impulso qualunque $p(t)$ al posto del rettangolo, $s(t) = \sum_m b[m]\,p(t - mT)$.

#### Derivazioni

##### Derivazione — Spettro dell'impulso rettangolare · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]] · Campionamento [[Campionamento_AD_DA.pdf#page=20|p. 20]]
**Fonte:** la slide contrappone la forma d'onda dell'esempio, «limitata nel tempo», alle forme d'onda reali, spesso «vincolate in frequenza». Qui si vede perché le due cose non vanno d'accordo.
> 🧩 Derivazione mia. Impulso $p(t) = 1$ per $|t| < T/2$, 0 altrove.

$$
\begin{aligned}
P(f) &= \int_{-T/2}^{T/2} e^{-j2\pi ft}\,dt && \text{definizione di trasformata, } p = 1 \text{ solo in } |t| < T/2 \\
&= \frac{e^{-j\pi fT} - e^{j\pi fT}}{-j2\pi f} && \text{primitiva di } e^{-j2\pi ft} \text{ è } e^{-j2\pi ft}/(-j2\pi f) \\
&= \frac{\sin(\pi fT)}{\pi f} && e^{jx} - e^{-jx} = 2j\sin x \\
&= T\,\text{sinc}(fT) && \text{sinc}(x) = \sin(\pi x)/(\pi x)
\end{aligned}
$$

**Risultato:** $|P(f)|$ si annulla solo nei punti $f = k/T$ ($k \neq 0$) e tra uno zero e l'altro decresce solo come $1/(\pi|f|)$: non esiste una $B$ oltre la quale $P(f) = 0$. L'impulso rettangolare, limitato nel tempo, **non è a banda limitata**.
**Sanity check:** $P(0) = T$, cioè l'area dell'impulso ✓. È lo stesso fatto di p. 20: un segnale di durata finita non può avere banda rigorosamente limitata ([[aliasing]]).
**Ipotesi:** impulso rettangolare ideale (fronti verticali).

#### Spiegazione

##### L'esempio della slide: modulazione lineare binaria · [[Rappresentazione_Rice.pdf#page=3|p. 3]]

![[rappresentazione-rice-p3-modulazione-binaria.png]]
*La sequenza di simboli +1, −1, −1, +1, +1, +1, −1, +1, −1, +1, +1, … diventa una forma d'onda a gradini: ogni simbolo moltiplica un impulso rettangolare traslato. Nota a mano sotto la figura: i segnali di comunicazione devono essere allocati in certe porzioni dello spettro.*

- I simboli (bit) diventano una forma d'onda analogica moltiplicando ogni simbolo per una copia traslata di un impulso rettangolare: è la **modulazione lineare**. Nota a mano: si chiama così «perché $s(t)$ dipende linearmente dai simboli».
- La forma d'onda dell'esempio è **limitata nel tempo**. Le forme d'onda usate davvero per modulare, però, sono spesso **vincolate nel dominio della frequenza**:
  - per le caratteristiche fisiche del mezzo di comunicazione;
  - per fattori esterni, per esempio le **regole sull'uso dello spettro**.
- Note a mano: i segnali di comunicazione devono essere allocati in certe porzioni dello spettro. I segnali da trasmettere sul canale devono soddisfare **vincoli nel dominio della frequenza**, che riguardano **dove** è allocato il loro spettro.

> 🧩 Cosa vuol dire "dipende linearmente": moltiplicare tutti i $b[m]$ per una costante moltiplica $s(t)$ per la stessa costante, e la forma d'onda di una somma di sequenze di simboli è la somma delle forme d'onda.

##### Dove deve finire il segnale modulato · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

Il canale del disegno di p.2 lascia passare solo le frequenze attorno a $\pm f_c$: il segnale trasmesso deve quindi essere **in banda passante** ([[segnali-banda-base-e-passa-banda]]). Nello schema modulare della lezione:
1. il DSP del trasmettitore esegue codifica, modulazione e filtraggio **in banda base**, producendo l'inviluppo complesso ([[inviluppo-complesso]], slide 7);
2. l'upconverter lo porta in banda passante ([[upconversion-e-downconversion]]).

Note a mano sulla slide 7:
- il **modulatore** è il macroblocco che comprende entrambi i passi, cioè il DSP e anche l'upconversion;
- il **demodulatore** è il macroblocco speculare: downconversion e DSP.

Nella figura della slide 14 una nota a mano collega S → $s(n)$ → MOD alle due uscite $s_c(t)$ e $s_s(t)$ che entrano nell'upconverter. Dal modulatore «esce l'inviluppo».

#### Perché importa · [[Intro.pdf#page=3|p. 3]]

La modulazione digitale è il terzo tema del programma. In questa lezione fa da motivazione: il modulatore deve produrre forme d'onda che stiano in una precisa porzione di spettro, e per descriverle e generarle serve la rappresentazione complessa in banda base.

#### Connessioni · Intro [[Intro.pdf#page=16|p. 16]] · Campionamento [[Campionamento_AD_DA.pdf#page=20|p. 20]] · Processi [[random_processes.pdf#page=37|p. 37]]

- [[sistema-comunicazione-digitale]] — il modulatore è un blocco dello schema.
- [[segnali-banda-base-e-passa-banda]] — il segnale modulato deve occupare la banda passante del canale.
- [[inviluppo-complesso]] — il modulatore lavora sull'inviluppo complesso; l'upconverter lo porta a $f_c$.
- [[upconversion-e-downconversion]] — lo stadio che segue il modulatore.
- [[aliasing]] — un impulso limitato nel tempo non è a banda limitata, come i segnali di p. 20.
- [[calcolo-densita-spettrale]] — la PSD del segnale modulato linearmente è $\frac{\sigma_b^2}{T}|P(f)|^2$, con l'impulso rettangolare $\sigma_b^2 T\,\text{sinc}^2(fT)$ (esempio di p. 37).

#### Fonti · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=3|3]], [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

- [[rappresentazione-complessa-banda-base]]

### Segnali in banda base e in banda passante · [[segnali-banda-base-e-passa-banda|pagina]]

#### Definizione · Rice [[Rappresentazione_Rice.pdf#page=4|p. 4]] · Campionamento [[Campionamento_AD_DA.pdf#page=20|p. 20]]

- Un segnale $s_b(t)$ è **in banda base** (*baseband*) se, per qualche $B > 0$,
$$S_b(f) \approx 0, \qquad |f| > B \tag{1}$$
- Un canale modellato come sistema **lineare tempo-invariante** (LTI) è in banda base se la sua funzione di trasferimento $H(f)$ soddisfa la (1).
- Un segnale $s_p(t)$ è **in banda passante** (*passband*) se
$$S_p(f) \approx 0, \qquad |f \pm f_c| > B/2 \tag{2}$$
  dove $f_c > B > 0$ si chiama frequenza **portante** (*carrier*). Nota a mano sulla slide: si dice banda passante perché «il contenuto informativo è traslato e centrato attorno a $f_c$».
- Un canale LTI è in banda passante se $H(f)$ soddisfa la (2).

> 🧩 Come leggere le due definizioni:
> - **"≈ 0", non "= 0".** I segnali reali sono solo *praticamente* limitati in banda: un segnale di durata finita non può avere banda rigorosamente limitata ([[aliasing]]).
> - **"$|f \pm f_c| > B/2$"** va letto come "sia $|f - f_c| > B/2$ sia $|f + f_c| > B/2$". Lo spettro è praticamente nullo fuori dai due intervalli $(f_c - B/2,\ f_c + B/2)$ e $(-f_c - B/2,\ -f_c + B/2)$, cioè quando $\big||f| - f_c\big| > B/2$.
> - **$B$ ha lo stesso significato nelle due definizioni: la banda monolatera.** In banda base lo spettro occupa $(-B, B)$, quindi $B$ di frequenze positive. In banda passante il lobo positivo è largo $B$, da $f_c - B/2$ a $f_c + B/2$.

#### Formule · [[Rappresentazione_Rice.pdf#page=4|p. 4]], [[Rappresentazione_Rice.pdf#page=5|5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]]

| Formula | Significato |
|---|---|
| $S_b(f)\approx 0$ per $\|f\|>B$ | segnale (o canale) in banda base |
| $S_p(f)\approx 0$ per $\|f\pm f_c\|>B/2$, con $f_c>B>0$ | segnale (o canale) in banda passante |
| $X(f) = X^*(-f)$ | simmetria coniugata (hermitiana) di un segnale reale |
| banda bilatera $= 2\times$ banda monolatera | vale per i segnali reali |
| $B/f_c \ll 1$ | segnale passa-banda **a banda stretta** |

Simboli: $B$ = banda monolatera [Hz]; $f_c$ = frequenza portante [Hz]; $S_b(f)$, $S_p(f)$, $X(f)$ = trasformate di Fourier (unità del segnale per secondo, es. V/Hz); $^*$ = complesso coniugato.

#### Derivazioni

##### Derivazione — Simmetria hermitiana di un segnale reale · [[Rappresentazione_Rice.pdf#page=5|p. 5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]]
**Fonte:** proprietà usata senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
X(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{-j2\pi ft}\,dt && \text{definizione di trasformata} \\
X^*(f) &= \int_{-\infty}^{+\infty} x(t)\,e^{+j2\pi ft}\,dt && \text{coniugo; } x(t) \text{ è reale, quindi } x^* = x \\
&= X(-f) && \text{è la stessa definizione calcolata in } -f \\
\Rightarrow\ X(f) &= X^*(-f) && \text{coniugo entrambi i membri}
\end{aligned}
$$

**Conseguenze**, scrivendo $X(-f) = X^*(f)$ per parte reale e parte immaginaria:
- $\text{Re}\,X(-f) = \text{Re}\,X(f)$: la parte reale è **pari**;
- $\text{Im}\,X(-f) = -\text{Im}\,X(f)$: la parte immaginaria è **dispari**;
- $|X(-f)| = |X(f)|$: il modulo è pari.

È quello che mostra la figura della slide 4. La metà a frequenze negative è l'immagine speculare (coniugata) di quella positiva: **non contiene informazione nuova**. È l'osservazione da cui nasce il [[segnale-analitico]].

##### Derivazione — La banda bilatera è il doppio della monolatera · [[Rappresentazione_Rice.pdf#page=7|p. 7]]
> 🧩 Derivazione mia

Se le frequenze positive occupate formano un insieme di ampiezza $B$, per $|X(-f)| = |X(f)|$ le frequenze negative occupate ne sono lo specchio, e hanno ampiezza $B$ anch'esse. In totale: $2B$.
**Caso limite:** per un segnale **complesso** la simmetria non vale e le due metà sono indipendenti, quindi la regola del "doppio" non si applica (banda dei segnali complessi: [[inviluppo-complesso]]).

##### Derivazione — Perché si chiede $f_c > B$ · [[Rappresentazione_Rice.pdf#page=4|p. 4]]
**Fonte:** condizione data senza commento. Accanto c'è una nota a mano rimasta incompleta («altrimenti c'è…»).
> 🧩 Derivazione mia: cosa succederebbe altrimenti.

$$
f_c > B \ \Rightarrow\ f_c - \frac{B}{2} > B - \frac{B}{2} = \frac{B}{2} > 0
$$

Il bordo inferiore del lobo positivo sta sopra $B/2 > 0$, e per simmetria il bordo superiore del lobo negativo sta sotto $-B/2$. I due lobi quindi **non si toccano e non contengono $f = 0$**. Senza questa condizione, "passa-banda" non avrebbe senso.

#### Spiegazione

##### Esempi di spettri (slide 4) · [[Rappresentazione_Rice.pdf#page=5|p. 5]], [[Rappresentazione_Rice.pdf#page=22|p. 22]]

La slide considera due segnali **reali**, $s_b(t)$ in banda base e $s_p(t)$ in banda passante. Le loro trasformate $S_b(f)$ e $S_p(f)$ possono esistere in senso ordinario o in **senso generalizzato**, per esempio con delta di Dirac. Per la simmetria coniugata $S_b(f) = S_b^*(-f)$ e $S_p(f) = S_p^*(-f)$.

![[rappresentazione-rice-p5-spettri-banda-base-passa-banda.png]]
- *A sinistra, il segnale in banda base. $\text{Re}(S(f))$ è un triangolo di altezza 1 su $(-B, B)$, pari. $\text{Im}(S(f))$ vale $+1$ su $(-B, 0)$ e $-1$ su $(0, B)$, dispari.*
- *A destra, il segnale passa-banda: stesse forme spostate attorno a $\pm f_c$, larghezza $B$; parte reale pari, parte immaginaria dispari.*
- *Note a mano: «le trasformate di Fourier dei segnali reali godono della simmetria hermitiana». Con $f_c$ cerchiato: «l'obiettivo è svincolarsi dalla $f_c$, ovvero dalla frequenza carrier, perché l'informazione di $s(t)$ non dipende da $f_c$: si può descrivere tutto con un segnale in banda base».*

> 💡 Connessione: "svincolarsi da $f_c$" è il programma della lezione. L'informazione di $s_p(t)$ non dipende da $f_c$, quindi si può descrivere tutto con un segnale in banda base: l'[[inviluppo-complesso]].

> ⚠️ Nella figura il segnale in banda base è indicato con $S(f)$ invece di $S_b(f)$. Più avanti, nella slide 11, $S(f)$ indica l'inviluppo complesso.

##### Banda (slide 5) · [[Rappresentazione_Rice.pdf#page=7|p. 7]]

- La **banda** è l'ampiezza dell'intervallo di frequenze occupato dalla trasformata di Fourier.
- **Banda monolatera** (*one-sided*): occupazione spettrale sulle frequenze positive.
- **Banda bilatera** (*two-sided*): occupazione su frequenze positive e negative.
- Per i segnali **reali** la bilatera è il doppio della monolatera, per la simmetria coniugata $X(f) = X^*(-f)$.
- Di solito "banda" senza aggettivi indica la **monolatera**.
- Un segnale passa-banda è **a banda stretta** (*narrowband*) se $B/f_c \ll 1$. Da qui in poi si considerano solo segnali passa-banda a banda stretta.

> 🧩 Con gli spettri della slide 4: il segnale in banda base ha banda monolatera $B$ e bilatera $2B$. Il passa-banda ha banda monolatera $B$ (il lobo positivo) e bilatera $2B$ (i due lobi).

##### Definizioni negli appunti e banda stretta (appunti p.8) · [[Rappresentazione_Rice.pdf#page=8|p. 8]]

Gli appunti riprendono in italiano le definizioni della slide 5:
- **larghezza di banda**: dimensione dell'intervallo di frequenze occupato dalla trasformata di Fourier del segnale;
- si distingue tra banda **monolatera** e **bilatera**; la bilatera considera sia le frequenze positive sia quelle negative;
- se $s(t)$ è reale, la bilatera è il doppio della monolatera, per la simmetria hermitiana $S(f) = S^*(-f)$;
- **segnale passa-banda a banda stretta**: la sua banda $B$ è molto minore della frequenza portante, $B/f_c \ll 1$. Nota: **non è un'ipotesi stringente**.

![[rappresentazione-rice-p8-appunti-banda-stretta.png]]
*Appunti a mano: un segnale a banda stretta ha banda molto minore di $f_c$ ($B \ll f_c$), cioè due lobi stretti attorno a $\pm f_c$. Sotto, le definizioni di larghezza di banda, banda monolatera e bilatera e segnale a banda stretta.*

> 🧩 Perché "non è un'ipotesi stringente" (lettura mia): nei sistemi reali la portante è molto più alta della banda del segnale. È lo stesso ordine di grandezza del grafico I/Q di [[inviluppo-complesso]], dove per rendere visibili le oscillazioni si è dovuta scegliere una $f_c$ artificialmente bassa.

> 🧩 Perché l'ipotesi di banda stretta aiuta, anticipando i risultati della lezione:
> - $s_p(t)$ appare come una portante a $f_c$ con ampiezza e fase che cambiano lentamente ([[inviluppo-complesso]]);
> - nella downconversion i termini a $2f_c$ cadono lontanissimi dalla banda base e si filtrano con facilità ([[upconversion-e-downconversion]]).

##### Canale passa-banda (appunti p.2) · [[Rappresentazione_Rice.pdf#page=2|p. 2]]

Il disegno di p.2 ([[modulazione-digitale]]) mostra la $H(f)$ di un canale passa-banda: due lobi di larghezza $B$, la "banda utile", centrati in $\pm f_c$.
- Il segnale attraversa il canale, che è caratterizzato da una sua risposta in frequenza e da una determinata banda a disposizione.
- Il trasmettitore deve portare il segnale in quella porzione di spettro, per adattarlo al canale.
- Il ricevitore lo riporta in banda base, «e questo rende il segnale complesso» ([[inviluppo-complesso]]).

> 🎯 Esame: dare le definizioni (1) e (2), spiegare banda monolatera e bilatera e perché per i segnali reali una è il doppio dell'altra, definire la banda stretta.

#### Perché importa · [[Rappresentazione_Rice.pdf#page=9|p. 9]]

I canali passa-banda sono molto usati, quindi bisogna saper trasmettere e ricevere segnali passa-banda. Le definizioni fissano la notazione ($B$, $f_c$) di tutta la lezione. L'ipotesi di banda stretta è usata in tutti i risultati successivi.

#### Connessioni

- [[teorema-del-campionamento]] — stessa nozione di segnale a banda limitata: la $f_m$ di quella lezione è la $B$ del segnale in banda base.
- [[aliasing]] — il "≈ 0": i segnali di durata finita sono solo praticamente limitati in banda.
- [[segnale-analitico]] — sfrutta la simmetria hermitiana: la metà negativa dello spettro è ridondante e si scarta.
- [[inviluppo-complesso]] — rappresentazione in banda base di un segnale passa-banda a banda stretta.
- [[modulazione-digitale]] — il modulatore deve collocare il segnale nella banda passante del canale.

#### Fonti · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=4|p. 4]], [[Rappresentazione_Rice.pdf#page=5|5]], [[Rappresentazione_Rice.pdf#page=7|p. 7]], [[Rappresentazione_Rice.pdf#page=8|8]]

- [[rappresentazione-complessa-banda-base]]

### Inviluppo complesso e componenti in fase e quadratura · [[inviluppo-complesso|pagina]]

#### Definizione · [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=15|p. 15]], [[Rappresentazione_Rice.pdf#page=16|16]]

Tutta l'informazione di un segnale passa-banda **reale** $s_p(t)$ è contenuta in un segnale **complesso in banda base**. Questo segnale si chiama **rappresentazione complessa in banda base**, o **inviluppo complesso** (*complex envelope*), di $s_p(t)$.

In frequenza è il [[segnale-analitico]] traslato di $-f_c$:
$$S(f) \triangleq S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c) \tag{13}$$

Nel tempo:
$$s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j\,s_s(t) \tag{15}$$
- $s_c(t)$ = componente **in fase** (*in-phase*, **I**), la parte reale;
- $s_s(t)$ = componente **in quadratura** (*quadrature*, **Q**), la parte immaginaria.

Sono entrambi segnali **reali** in banda base. Note a mano sulla slide 12:
- la (15) «corrisponde a una traslazione del segnale analitico», per la proprietà di Fourier della traslazione in frequenza;
- $s_c(t)$ è la componente in fase (I), $s_s(t)$ la componente in quadratura (Q), e insieme danno i «termini di seno e coseno»;
- «quadratura indica che il prodotto ortogonale [scalare] con $s_c$ è 0», proprietà dimostrata più sotto, eq. (18).

Il perché dei nomi è nella (17).

Il ritorno al segnale passa-banda vale **per qualunque** segnale passa-banda:
$$s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{16, 17}$$

> 🧩 Precisazione mia: l'inviluppo complesso è definito **rispetto a una frequenza di riferimento** $f_c$. Se si cambia il riferimento in $f_c + \Delta f$, la (15) dà $s_p^+(t)\,e^{-j2\pi(f_c + \Delta f)t} = s(t)\,e^{-j2\pi \Delta f\, t}$: lo stesso inviluppo traslato in frequenza di $-\Delta f$. Per questo la slide 16 parla di un «riferimento di frequenza comune» ([[equivalente-banda-base-dei-filtri]]).

#### Formule · [[Rappresentazione_Rice.pdf#page=15|p. 15]]–[[Rappresentazione_Rice.pdf#page=17|17]]

| Formula | Significato |
|---|---|
| $S(f) = S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c)$ | inviluppo complesso in frequenza, eq. (13) |
| $S_p(f) = \dfrac{S(f - f_c) + S^*(-f - f_c)}{\sqrt2}$ | ritorno al passa-banda in frequenza, eq. (14) |
| $s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j s_s(t)$ | inviluppo nel tempo, eq. (15) |
| $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\}$ | eq. (16) |
| $s_p(t) = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ | forma I/Q, eq. (17) |
| $s_p(t) = \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big)$, con $a = \|s\|$ e $\theta = \arg s$ | forma ampiezza-fase |
| $\langle x_c, x_s\rangle = \int x_c(t)\,x_s(t)\,dt = 0$ | ortogonalità delle portanti I e Q, eq. (18) |
| $\langle u_p, v_p\rangle = \langle u_c, v_c\rangle + \langle u_s, v_s\rangle = \text{Re}\{\langle u, v\rangle\}$ | prodotto scalare, eq. (19) |
| $\|s_p\|^2 = \|s\|^2$ | conservazione dell'energia, eq. (20) |

Simboli:
- $f_c$ = frequenza portante [Hz]; $u(\cdot)$ = gradino unitario; $^*$ = coniugato;
- $s(t)$ = inviluppo complesso (stessa unità di $s_p$, es. V); $s_c$, $s_s$ = sue parti reale e immaginaria;
- $x_c(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t)$ e $x_s(t) = \sqrt2\,s_s(t)\sin(2\pi f_c t)$ = le due forme d'onda passa-banda di I e Q;
- $\langle x, y\rangle = \int x(t)\,y^*(t)\,dt$ = prodotto scalare [V²·s]; $\|x\|^2 = \langle x, x\rangle$ = energia [V²·s].

> 🧮 Formula chiave: $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ e $\|s_p\|^2 = \|s\|^2$.

#### Derivazioni

##### Derivazione — Eq. (15): l'inviluppo nel tempo · [[Rappresentazione_Rice.pdf#page=16|p. 16]]
$$
\begin{aligned}
s(t) &= \mathcal{F}^{-1}[S(f)] = \mathcal{F}^{-1}\big[S_p^+(f + f_c)\big] && \text{definizione (13)} \\
&= s_p^+(t)\,e^{-j2\pi f_c t} && \text{traslazione in frequenza: } X(f - f_0) \leftrightarrow x(t)\,e^{j2\pi f_0 t},\ f_0 = -f_c
\end{aligned}
$$
Moltiplicare per $e^{-j2\pi f_c t}$ sposta tutto lo spettro di $-f_c$: il lobo che il segnale analitico ha attorno a $+f_c$ finisce attorno a 0.

##### Derivazione — Eq. (16) e (17): dall'inviluppo al segnale passa-banda · [[Rappresentazione_Rice.pdf#page=16|p. 16]]
**Fonte:** «si ottiene facilmente».
$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s_p^+(t)\} && \text{eq. (10) di [[segnale-analitico]]} \\
&= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{dalla (15): } s_p^+ = s\,e^{j2\pi f_c t} \quad \text{(16)} \\
&= \sqrt2\,\text{Re}\{(s_c + j s_s)(\cos\alpha + j\sin\alpha)\} && \text{Eulero, } \alpha = 2\pi f_c t \\
&= \sqrt2\,\text{Re}\{s_c\cos\alpha - s_s\sin\alpha + j(s_c\sin\alpha + s_s\cos\alpha)\} && \text{moltiplico; } j^2 = -1 \\
&= \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) && \text{parte reale} \quad \text{(17)}
\end{aligned}
$$
Il secondo passaggio è annotato a mano sulla slide: «abbiamo definito prima l'inviluppo come $s(t) = s_p^+(t)e^{-j2\pi f_c t}$, quindi $s_p^+(t) = s(t)e^{j2\pi f_c t} = [s_c(t) + js_s(t)]\,e^{j2\pi f_c t}$». Sotto la (17): «in termini di seno e coseno».
**Da qui i nomi:** $s_c$ moltiplica il **coseno** della portante, $s_s$ il **seno**. Seno e coseno sono sfasati di 90°, "in quadratura".
**Ipotesi:** nessuna oltre alla definizione. La slide sottolinea che la (17) vale per **qualunque** segnale passa-banda.

##### Derivazione — Eq. (14): dall'inviluppo al passa-banda in frequenza · [[Rappresentazione_Rice.pdf#page=15|p. 15]]
**Fonte:** «la dimostrazione si ricava facilmente dalla (16)».
> 🧩 Derivazione mia

$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \frac{\sqrt2}{2}\Big[s(t)\,e^{j2\pi f_c t} + s^*(t)\,e^{-j2\pi f_c t}\Big] && \text{Re}\{z\} = (z + z^*)/2 \\
S_p(f) &= \frac{1}{\sqrt2}\Big[S(f - f_c) + S^*\big(-(f + f_c)\big)\Big] && x\,e^{j2\pi f_0 t} \leftrightarrow X(f - f_0);\ \ s^*(t) \leftrightarrow S^*(-f) \\
&= \frac{S(f - f_c) + S^*(-f - f_c)}{\sqrt2}
\end{aligned}
$$
**Lettura:** il primo termine ricostruisce il lobo attorno a $+f_c$, il secondo quello attorno a $-f_c$ come specchio coniugato. Il segnale che si ottiene è reale, perché il suo spettro è hermitiano per costruzione. Note a mano sulla (14): è la «relazione inversa», e il termine $S^*(-f - f_c)$ rimette la «parte tagliata da $u(f)$», cioè il lobo negativo scartato costruendo il segnale analitico.
**Sanity check:** per $f$ vicino a $+f_c$ il secondo termine è nullo e, dalla (13), $S(f - f_c) = \sqrt2\,S_p(f)$. Quindi $S_p(f) = \sqrt2\,S_p(f)/\sqrt2$ ✓.

##### Derivazione — Forma ampiezza-fase · [[Rappresentazione_Rice.pdf#page=22|p. 22]]
**Fonte:** l'inviluppo descrive «le variazioni lente di ampiezza e fase».
> 🧩 Derivazione mia: rende esplicita la frase della slide.

$$
\begin{aligned}
s(t) &= a(t)\,e^{j\theta(t)}, \quad a = |s| = \sqrt{s_c^2 + s_s^2},\ \ \theta = \arg s && \text{forma polare del numero complesso } s(t) \\
s_p(t) &= \sqrt2\,\text{Re}\{a(t)\,e^{j\theta(t)}\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big) && \text{Re}\{e^{j\phi}\} = \cos\phi
\end{aligned}
$$
$s_p(t)$ è quindi una portante a $f_c$ con **ampiezza** $\sqrt2\,a(t)$ e **fase** $\theta(t)$. Se $s(t)$ ha banda molto minore di $f_c$ (banda stretta), ampiezza e fase cambiano lentamente rispetto alla portante.

##### Derivazione — Eq. (18): ortogonalità delle componenti I e Q · [[Rappresentazione_Rice.pdf#page=16|p. 16]]–[[Rappresentazione_Rice.pdf#page=18|18]]
**Fonte:** p. 17 (slide 13), che rimanda al libro di testo. Accanto, una nota a mano dice che la dimostrazione è «sotto»: è negli appunti di p. 18, con l'uguaglianza di Parseval.
> 📄 La struttura della dimostrazione è quella degli appunti di p.18: Parseval, spettri di $x_c$ e $x_s$, termini incrociati nulli per la banda stretta, cambio di variabile. 🧩 Esplicito io i fattori e l'ipotesi minima. $S_c$ e $S_s$ sono le trasformate di $s_c$ e $s_s$, e $W$ la loro banda.

![[rappresentazione-rice-p18-appunti-ortogonalita-parseval.png]]
*Appunti a mano.*
- *In alto: la dimostrazione di $\langle x_c, x_s\rangle = 0$ con Parseval. Si sviluppa il prodotto; i due termini incrociati sono barrati, con la nota in rosso sulla banda stretta; dopo il cambio di variabile i due integrali restanti si cancellano.*
- *In basso: la verifica della (19), con i termini misti che si annullano per l'ortogonalità e i termini in $\cos(4\pi f_c t)$ che valgono circa 0.*

$$
\begin{aligned}
\langle x_c, x_s\rangle &= \int_{-\infty}^{+\infty} x_c(t)\,x_s(t)\,dt = \int_{-\infty}^{+\infty} X_c(f)\,X_s^*(f)\,df && \text{Parseval; } x_s \text{ reale} \\
X_c(f) &= \frac{1}{\sqrt2}\big[S_c(f - f_c) + S_c(f + f_c)\big] && \sqrt2\cos\alpha = \tfrac{\sqrt2}{2}(e^{j\alpha} + e^{-j\alpha}) \\
X_s(f) &= \frac{1}{j\sqrt2}\big[S_s(f - f_c) - S_s(f + f_c)\big] && \sqrt2\sin\alpha = \tfrac{\sqrt2}{2j}(e^{j\alpha} - e^{-j\alpha}) \\
X_s^*(f) &= \frac{1}{j\sqrt2}\big[S_s^*(f + f_c) - S_s^*(f - f_c)\big] && (1/j)^* = -1/j \text{: cambio segno alla parentesi} \\
\langle x_c, x_s\rangle &= \frac{1}{2j}\int\big[S_c(f - f_c) + S_c(f + f_c)\big]\big[S_s^*(f + f_c) - S_s^*(f - f_c)\big]\,df && \tfrac{1}{\sqrt2}\cdot\tfrac{1}{j\sqrt2} = \tfrac{1}{2j}
\end{aligned}
$$

Sviluppando il prodotto escono quattro termini:
- **$S_c(f - f_c)\,S_s^*(f + f_c)$ e $S_c(f + f_c)\,S_s^*(f - f_c)$** sono nulli. Il primo fattore vive attorno a $\pm f_c$, il secondo attorno a $\mp f_c$, e le due zone non si sovrappongono. Negli appunti la giustificazione è in rosso: «per ipotesi i segnali sono a banda stretta: lo spettro centrato a $+f_c$ non si sovrappone mai a quello centrato in $-f_c$, perché $B/f_c \ll 1$».
- Restano gli altri due, con il cambio di variabile $\nu = f \mp f_c$:
$$
\langle x_c, x_s\rangle = \frac{1}{2j}\Big[\underbrace{\int S_c(f + f_c)\,S_s^*(f + f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu} - \underbrace{\int S_c(f - f_c)\,S_s^*(f - f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu}\Big] = 0
$$

**Ipotesi:** gli appunti usano la banda stretta, $B/f_c \ll 1$. 🧩 In realtà basta di meno: che $s_c$ e $s_s$ abbiano banda $W < f_c$. Per un segnale passa-banda questo è sempre garantito: dalla (2) e dalla (13), con $f_c$ al centro del lobo, $S(f) \approx 0$ per $|f| > B/2$. Quindi $W = B/2 < f_c$, perché $f_c > B$.
**Alternativa nel tempo** (🧩 mia):
$$
\langle x_c, x_s\rangle = \int 2\,s_c s_s \cos\alpha\sin\alpha\,dt = \int s_c(t)\,s_s(t)\,\sin(4\pi f_c t)\,dt
$$
È la trasformata del prodotto $s_c s_s$ calcolata in $\pm 2f_c$. Il prodotto ha banda al più $2W < 2f_c$, quindi l'integrale è nullo.

> ⚠️ Segni negli appunti: gli appunti scrivono $X_s = -\frac{\sqrt2}{2j}S_s(f) * [\delta(f - f_c) - \delta(f + f_c)]$, con un meno davanti che non ci va, perché $\sqrt2\sin\alpha = \frac{\sqrt2}{2j}(e^{j\alpha} - e^{-j\alpha})$. Anche l'ordine dei due integrali finali è invertito rispetto allo sviluppo. Il risultato, $\frac{1}{2j}\big[\int S_c S_s^* - \int S_c S_s^*\big] = 0$, non cambia: è la differenza di due integrali uguali.

Nota a mano sulla slide 12: «quadratura indica che il prodotto ortogonale [scalare] con $s_c$ è 0». È proprio questa proprietà.

##### Derivazione — Eq. (19): prodotto scalare tra segnali passa-banda · [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]]
**Fonte:** risultato dato senza dimostrazione. Verificato negli appunti di p. 18 e p. 19. Note a mano sulla slide: $\langle u_p, v_p\rangle$ è il «prodotto ortogonale, scalare», e $\text{Re}\{\langle u, v\rangle\}$ è «la parte reale del prodotto degli inviluppi».
> 📄 Gli appunti procedono così: sviluppano $\langle u_p, v_p\rangle$ con la (17); i termini misti si annullano perché le componenti in fase e in quadratura sono ortogonali; restano $2\int u_cv_c\cos^2$ e $2\int u_sv_s\sin^2$, che si scrivono con $\cos^2 = \frac{1 + \cos(4\pi f_ct)}{2}$ e $\sin^2 = \frac{1 - \cos(4\pi f_ct)}{2}$. I due integrali con $\cos(4\pi f_c t)$ valgono circa 0, perché «le aree positive vengono bilanciate da quelle negative, poiché $B/f_c \ll 1$». Resta $\text{Re}\{\int[u_c + ju_s][v_c - jv_s]\,dt\} = \text{Re}\{\langle u, v\rangle\}$.
> 🧩 Qui sotto lo stesso conto per esteso. $u_p$, $v_p$ sono reali passa-banda, con inviluppi $u = u_c + ju_s$ e $v = v_c + jv_s$; $\alpha = 2\pi f_c t$.

$$
\begin{aligned}
u_p v_p &= \big(\sqrt2 u_c\cos\alpha - \sqrt2 u_s\sin\alpha\big)\big(\sqrt2 v_c\cos\alpha - \sqrt2 v_s\sin\alpha\big) && \text{eq. (17) per entrambi} \\
&= 2u_cv_c\cos^2\alpha + 2u_sv_s\sin^2\alpha - 2(u_cv_s + u_sv_c)\sin\alpha\cos\alpha && \text{sviluppo} \\
&= u_cv_c + u_sv_s + (u_cv_c - u_sv_s)\cos 2\alpha - (u_cv_s + u_sv_c)\sin 2\alpha && 2\cos^2 = 1 + \cos 2\alpha;\ 2\sin^2 = 1 - \cos 2\alpha;\ 2\sin\cos = \sin 2\alpha \\
\langle u_p, v_p\rangle &= \int u_cv_c\,dt + \int u_sv_s\,dt + \underbrace{\int g_1\cos(4\pi f_c t)\,dt - \int g_2\sin(4\pi f_c t)\,dt}_{=\,0} && g_1, g_2 \text{ prodotti di segnali in banda base} \\
&= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle
\end{aligned}
$$
I termini a $2f_c$ si annullano. Gli appunti lo giustificano con le aree che si bilanciano, cioè un inviluppo lento moltiplicato per un coseno veloce, e scrivono "≈ 0".
> 🧩 Precisazione mia: se la banda è minore di $f_c$ l'integrale è **esattamente** 0. Infatti $\int g(t)\cos(4\pi f_c t)\,dt = \frac12[G(2f_c) + G(-2f_c)]$, e allo stesso modo per il seno. $G$ è la trasformata di un prodotto di due segnali con banda $\le W$, quindi ha banda $\le 2W < 2f_c$ e vale zero in $\pm 2f_c$.

Poi il confronto con l'inviluppo complesso:
$$
\begin{aligned}
\langle u, v\rangle &= \int u\,v^*\,dt = \int (u_c + ju_s)(v_c - jv_s)\,dt && \text{definizione; } v^* = v_c - jv_s \\
&= \int (u_cv_c + u_sv_s)\,dt + j\int (u_sv_c - u_cv_s)\,dt && \text{sviluppo} \\
\text{Re}\{\langle u, v\rangle\} &= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle && \text{è la (19)}
\end{aligned}
$$
**Ipotesi:** banda di $u_c, u_s, v_c, v_s$ minore di $f_c$ (segnali passa-banda secondo la (2)).

##### Derivazione — Eq. (20): l'energia si conserva · [[Rappresentazione_Rice.pdf#page=17|p. 17]], [[Rappresentazione_Rice.pdf#page=19|p. 19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]
**Fonte:** p. 17 (slide 13); gli stessi passaggi sono negli appunti di p. 19. Note a mano sulla slide: «energia di $s_p$», «l'energia è reale».
$$
\begin{aligned}
\|s_p\|^2 &= \langle s_p, s_p\rangle = \int s_p^2(t)\,dt && \text{definizione di energia} \\
&= \text{Re}\{\langle s, s\rangle\} && \text{(19) con } u = v = s \\
&= \text{Re}\{\|s\|^2\} = \|s\|^2 && \langle s, s\rangle = \textstyle\int |s|^2 dt \text{ è reale: «posso togliere Re» (appunti p.19)}
\end{aligned}
$$
In componenti: $\|s_p\|^2 = \|s_c\|^2 + \|s_s\|^2$, cioè l'energia di I più quella di Q.

> ⚠️ Nelle note a mano sulla slide 13:
> - il secondo passaggio è indicato come «proprietà (10)», ma usa la (19);
> - in alto c'è scritto $s_p(t) = x_c(t) + x_s(t) = \sqrt2 s_c\cos(2\pi f_c t) + \sqrt2 s_s\sin(2\pi f_c t)$, ma dalla (17) è $s_p = x_c - x_s$, con il meno davanti al termine in seno. Per l'ortogonalità il segno non conta, per l'uguaglianza con $s_p$ sì.

![[rappresentazione-rice-p19-appunti-prodotto-scalare-energia.png]]
*Appunti a mano: conclusione della verifica della (19), $\text{Re}\{\int[u_c + ju_s][v_c - jv_s]\,dt\} = \text{Re}\{\langle u, v\rangle\}$, con $u$ inviluppo complesso di $u_p$ e $v^*$ il coniugato di $v$. Sotto, la (20): $\langle s_p, s_p\rangle = \int s_p^2\,dt = \|s_p\|^2 = \text{Re}\{\langle s, s\rangle\} = \text{Re}\{\int|s|^2dt\} = \|s\|^2$, dove l'integrale è reale e quindi si può togliere Re.*
**Perché torna esatto:** è l'effetto del $\sqrt2$ nella (3), vedi [[segnale-analitico]] (sezione «Derivazione — Perché proprio √2»). Nota a mano di p. 21: alla domanda se tutti i passaggi conservano l'energia, la risposta è «sì, per le accortezze fatte ($\sqrt2$)».

##### Derivazione — Frequenza di campionamento: passa-banda contro inviluppo · Rice [[Rappresentazione_Rice.pdf#page=9|p. 9]] · Campionamento [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=14|p. 14]]
**Fonte:** l'inviluppo «si può campionare a una frequenza molto più bassa» di $s_p(t)$.
> 🧩 Derivazione mia, con il teorema del campionamento ([[teorema-del-campionamento]]).
> ⚠️ Notazione: nella lezione sul campionamento $f_c$ era la frequenza di campionamento; qui $f_c$ è la portante, quindi la frequenza di campionamento si chiama $f_s$.

$$
\begin{aligned}
f_{s,\,p} &\ge 2\Big(f_c + \frac B2\Big) = 2f_c + B && s_p \text{ è reale e la sua frequenza massima è } f_c + B/2 \\
f_{s,\,\text{inv}} &\ge B && s(t) \text{ occupa } (-B/2,\ B/2):\ \text{repliche ogni } f_s \text{ senza sovrapposizione se } f_s \ge B \\
\frac{f_{s,\,p}}{f_{s,\,\text{inv}}} &= \frac{2f_c}{B} + 1 \gg 1 && \text{banda stretta: } B \ll f_c
\end{aligned}
$$
Ogni campione dell'inviluppo è complesso, cioè due numeri reali. Anche contando $2B$ numeri reali al secondo, il rapporto resta dell'ordine di $f_c/B$.
**Ipotesi:** $f_c$ al centro del lobo; campionamento ideale. Per $s(t)$ la condizione nasce dallo stesso argomento delle repliche di p. 12, applicato a uno spettro non simmetrico.

#### Spiegazione

##### Perché serve la rappresentazione in banda base (slide 6–7) · [[Rappresentazione_Rice.pdf#page=6|p. 6]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

- I canali passa-banda sono molto usati, quindi bisogna saper trasmettere e ricevere segnali passa-banda.
- Tutta l'informazione di un segnale passa-banda reale sta in un segnale complesso in banda base: l'inviluppo complesso.
- L'inviluppo si può rappresentare a tempo discreto, cioè campionato, a una frequenza **molto più bassa** di $s_p(t)$ (vedi la derivazione sopra). I transceiver moderni eseguono quindi in digitale, direttamente sull'inviluppo, algoritmi complicati, riducendo al minimo l'elaborazione analogica.

Le note a mano sulla slide 6 riscrivono questi punti in italiano e chiamano il campionamento a frequenza bassa **il vantaggio**: l'inviluppo si campiona a una frequenza «nettamente inferiore» a quella che servirebbe per il segnale passa-banda. Di conseguenza i ricetrasmettitori moderni possono implementare in digitale algoritmi molto complessi (DSP), riducendo al minimo la parte analogica.

**Perché conviene portare il segnale in banda base**, dagli appunti di p. 6. Oltre al fatto che l'informazione non dipende da $f_c$, la banda base permette di:
- **ridurre i costi hardware per il campionamento**;
- guadagnare **modularità e indipendenza**: si possono riutilizzare componenti che operano in banda base, senza costruirli ad hoc per la specifica banda del segnale;
- (in rosso) altrimenti non si potrebbero generalizzare gli algoritmi, e calcolarli in digitale costerebbe troppo.

![[rappresentazione-rice-p6-appunti-vantaggi-banda-base.png]]
*Appunti a mano: i vantaggi di portare il segnale in banda base (costi di campionamento, modularità e indipendenza).*

Lo schema modulare del transceiver:
1. un **DSP** codifica l'informazione nella forma d'onda complessa in banda base: codifica, modulazione, filtraggio;
2. l'inviluppo viene **convertito in su** (*upconverted*) nel segnale passa-banda da mandare sul canale fisico;
3. al ricevitore il segnale passa-banda ricevuto viene **convertito in giù** (*downconverted*) in banda base;
4. il DSP opera sull'inviluppo per sincronizzazione, demodulazione e decodifica.

Così gli algoritmi più sofisticati si sviluppano in banda base, **indipendentemente dalla banda fisica** usata. Le conversioni sono in [[upconversion-e-downconversion]].

Note a mano sulla slide 7:
- i punti 1–2 formano il **modulatore**, i punti 3–4 il **demodulatore**: «sono macroblocchi», e il modulatore «comprende anche l'up conversion»;
- dal punto 1 «si ottiene l'inviluppo complesso in banda base»;
- sviluppare gli algoritmi in banda base vuol dire che «ci si è svincolati dalla frequenza carrier ($f_c$)».

![[rappresentazione-rice-p10-schema-modulare-transceiver.png]]
*con le note a mano: le parentesi graffe raggruppano i quattro passi in modulatore e demodulatore.*

##### Dallo spettro passa-banda all'inviluppo: le figure · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=15|p. 15]]

![[rappresentazione-rice-p15-inviluppo-complesso-spettri.png]]
*In alto, lo spettro del segnale passa-banda. $\text{Re}(S_p(f))$ ha due triangoli di altezza $A$ attorno a $\pm f_c$, speculari. $\text{Im}(S_p(f))$ ha due rettangoli di altezza $B$: positivo attorno a $f_c$, negativo attorno a $-f_c$. In basso, l'inviluppo: resta solo il lobo positivo, spostato attorno a 0 e moltiplicato per $\sqrt2$. $\text{Re}(S(f))$ è un triangolo di altezza $\sqrt2 A$, $\text{Im}(S(f))$ un rettangolo di altezza $\sqrt2 B$.*

> ⚠️ In questa figura, e nella slide 17, $A$ e $B$ sono **altezze** dello spettro, non la banda. Nel resto della lezione $B$ è la banda.

> 🧩 Controllo mio delle altezze con la (13): $S(f) = \sqrt2\,S_p(f + f_c)$ attorno a $f = 0$. Le altezze del lobo positivo vengono moltiplicate per $\sqrt2$: $A \to \sqrt2 A$ e $B \to \sqrt2 B$ ✓. Il lobo negativo sparisce per il fattore $u(f + f_c)$.

![[grafico-rice-catena-spettri.png]]
*🧩 Grafico mio (eq. (3) e (13), p. 11 e p. 15; script in `output/grafici/`). La catena in tre passi, con un lobo asimmetrico come quello della slide 11.*
- *(a) Lo spettro reale del segnale passa-banda: i lobi a $\pm f_c$ sono speculari, quindi portano la stessa informazione.*
- *(b) Il segnale analitico: si butta il lobo negativo e si moltiplica per $\sqrt2$.*
- *(c) L'inviluppo complesso: lo stesso lobo spostato in 0.*

*Il lobo in (c) non è simmetrico attorno a 0. Non vale $S(f) = S^*(-f)$, e per questo $s(t)$ è complesso: è la nota a mano di p. 2, «il ricevitore porta in banda base, e questo rende il segnale complesso».*

##### Componenti I/Q nel tempo · [[Rappresentazione_Rice.pdf#page=16|p. 16]], [[Rappresentazione_Rice.pdf#page=22|p. 22]]

![[rappresentazione-rice-p16-componenti-iq.png]]
*con le note a mano:*
- *la (15) corrisponde a una traslazione del segnale analitico, per la proprietà di Fourier;*
- *$s_c$ è la componente in fase (I), $s_s$ quella in quadratura (Q); quadratura vuol dire prodotto scalare nullo con $s_c$;*
- *i passaggi $s_p^+ = s\,e^{j2\pi f_c t} = [s_c + js_s]\,e^{j2\pi f_c t}$ che portano alla (16)–(17), "in termini di seno e coseno".*

![[grafico-rice-iq-tempo.png]]
*🧩 Grafico mio (eq. (17)). Esempio con $s_c(t) = \cos(2\pi\cdot 1\,\text{kHz}\cdot t) + 0.5\cos(2\pi\cdot 2\,\text{kHz}\cdot t)$ e $s_s(t) = 0.8\sin(2\pi\cdot 1.5\,\text{kHz}\cdot t)$. In alto I, Q e il modulo $|s(t)|$, che variano lentamente. In basso $s_p(t)$ con $f_c = 10$ kHz: una portante veloce dentro l'inviluppo $\pm\sqrt2\,|s(t)|$, come prevede la forma ampiezza-fase. $f_c$ è scelta piccola per rendere visibili le oscillazioni; nei sistemi reali $f_c/B$ è molto più grande.*

**Cosa rappresenta l'inviluppo**:
- ricavare l'inviluppo complesso significa estrarre le variazioni **lente** di ampiezza e fase introdotte dalla modulazione in banda base, eliminando la variazione di fase **rapida e prevedibile** dovuta a $f_c$. Nota a mano: «l'inviluppo complesso ci permette di separare le variazioni lente introdotte dalla modulazione in banda base»;
- la fase dovuta a $f_c$ è prevedibile, quindi **non porta informazione**;
- l'informazione di un segnale passa-banda è **tutta** nel suo inviluppo complesso.

##### Energia (slide 13) · [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]
> 📄 Fonte: p. 17 (slide 13), appunti a mano di p. 18, p. 19 e p. 21

- Le forme d'onda passa-banda di I e di Q, $x_c = \sqrt2 s_c\cos(2\pi f_c t)$ e $x_s = \sqrt2 s_s\sin(2\pi f_c t)$, sono **ortogonali**, eq. (18). La slide rimanda al libro per la dimostrazione, che è negli appunti di p.18 (derivazione della (18) qui sopra).
- Per due segnali passa-banda reali il prodotto scalare è la parte reale del prodotto scalare degli inviluppi, eq. (19). Verifica negli appunti di p.18–19.
- Con $u = v = s$: l'energia dell'inviluppo complesso è **uguale** a quella del segnale passa-banda, eq. (20), anch'essa negli appunti di p.19.

##### Banda di un segnale complesso (slide 19) · [[Rappresentazione_Rice.pdf#page=27|p. 27]]

- L'occupazione spettrale di un segnale **fisico reale** è la più piccola banda di frequenze **positive** che contiene la maggior parte del segnale. Per un segnale reale vale $S(f) = S^*(-f)$, quindi le frequenze negative non aggiungono nulla.
- Nei segnali **complessi** in banda base l'informazione sta sia nelle frequenze positive sia in quelle **negative**.
- L'occupazione spettrale di un segnale complesso in banda base è quindi la più piccola banda **attorno all'origine** che contiene la maggior parte del segnale, contando frequenze positive e negative.

> 🧩 Esempio mio: un segnale passa-banda con banda monolatera $B$ e $f_c$ al centro del lobo ha l'inviluppo in $(-B/2,\ B/2)$. Contando i due lati, l'occupazione è $B$: la stessa larghezza del lobo positivo di $s_p$. Non va dimezzata né raddoppiata, perché le due metà dello spettro di $s(t)$ sono diverse (grafico (c) sopra).

> 🎯 Esame: definire l'inviluppo complesso, (13) e (15), e le componenti I/Q; ricavare la (17) e la (14); dimostrare l'ortogonalità (18) e la conservazione dell'energia (20); spiegare perché l'informazione sta tutta nell'inviluppo e perché conviene lavorare in banda base.

#### Perché importa · [[Intro.pdf#page=3|p. 3]]

È il concetto centrale del primo tema del corso. Permette di:
- descrivere qualunque segnale passa-banda con un segnale in banda base, senza portarsi dietro $f_c$;
- campionarlo ed elaborarlo in digitale a frequenza bassa;
- progettare modulazione, sincronizzazione e demodulazione indipendentemente dalla banda fisica.

#### Connessioni

- [[segnale-analitico]] — l'inviluppo è il segnale analitico traslato di $-f_c$.
- [[segnali-banda-base-e-passa-banda]] — la (2) garantisce la banda $B/2 < f_c$ delle componenti I/Q, che serve per (18)–(20).
- [[upconversion-e-downconversion]] — realizzano fisicamente la (17) e la sua inversa.
- [[equivalente-banda-base-dei-filtri]] — anche i filtri passa-banda si descrivono con il loro inviluppo complesso.
- [[teorema-del-campionamento]] — l'inviluppo si campiona a frequenza $\ge B$ invece di $\ge 2f_c + B$.
- [[modulazione-digitale]] — il modulatore produce l'inviluppo complesso.

#### Fonti · [[Rappresentazione_Rice.pdf#page=6|p. 6]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]], [[Rappresentazione_Rice.pdf#page=15|p. 15]], [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]], [[Rappresentazione_Rice.pdf#page=22|22]], [[Rappresentazione_Rice.pdf#page=27|p. 27]]

- [[rappresentazione-complessa-banda-base]]
- Appunti a mano: p. 6 (vantaggi della banda base), p. 18 e p. 19 (dimostrazioni di (18), (19), (20)), p. 21 (catena e energia)

### Segnale analitico e trasformata di Hilbert · [[segnale-analitico|pagina]]

#### Definizione · [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=12|12]]

Dato un segnale passa-banda $s_p(t)$ con trasformata $S_p(f)$, il **segnale analitico** (*analytical signal*) associato ha trasformata
$$S_p^+(f) = \sqrt{2}\,S_p(f)\,u(f) \tag{3}$$
dove $u(\cdot)$ è il gradino unitario. In parole: si **tengono solo le frequenze positive** di $S_p(f)$ e le si moltiplica per $\sqrt2$.

Note a mano sulla slide 8:
- lo scopo: «per definire l'inviluppo dobbiamo costruire il segnale analitico $S_p^+(f)$ nel dominio $f$»;
- il gradino: «annulliamo le frequenze negative (ridondanti)»;
- il $\sqrt2$: è un «fattore introdotto per motivi energetici», che «serve per conservare l'energia». Il motivo è ricavato in «Derivazione — Perché proprio √2» (in questa pagina).

Ogni segnale passa-banda ha **un unico** segnale analitico, e viceversa.

La **trasformata di Hilbert** di $s_p(t)$ è
$$\widehat{s}_p(t) \triangleq s_p(t) * \frac{1}{\pi t} = \int_{-\infty}^{+\infty}\frac{s_p(\tau)}{\pi(t - \tau)}\,d\tau \tag{9}$$
e nel tempo il segnale analitico si scrive con essa:
$$s_p^+(t) = \frac{1}{\sqrt2}\,s_p(t) + \frac{j}{\sqrt2}\,\widehat{s}_p(t) \tag{8}$$

Nota a mano sulla (8): «questa equazione ci dice che il segnale analitico è un segnale **complesso**» con
- **parte reale**: il segnale passa-banda originale scalato di $1/\sqrt2$;
- **parte immaginaria**: la trasformata di Hilbert $\widehat{s}_p(t)$, anch'essa scalata di $1/\sqrt2$.

> 🧩 Precisazione mia: l'integrale (9) va inteso come **valore principale di Cauchy**, perché $1/(t - \tau)$ diverge in $\tau = t$.

#### Formule · [[Rappresentazione_Rice.pdf#page=11|p. 11]]–[[Rappresentazione_Rice.pdf#page=13|13]]

| Formula | Significato |
|---|---|
| $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$ | segnale analitico, eq. (3) |
| $s_p^+(t) = \mathcal{F}^{-1}[S_p^+(f)] = \sqrt2\,s_p(t) * \mathcal{F}^{-1}[u(f)]$ | eq. (4) |
| $\mathcal{F}[u(t)] = \frac12\delta(f) + \frac{1}{j2\pi f} \triangleq \text{U}(f)$ | eq. (5) |
| $\mathcal{F}[\text{U}(t)] = u(-f)$ | dualità, eq. (6) |
| $\mathcal{F}^{-1}[u(f)] = \text{U}(-t) = \frac12\delta(t) + \frac{j}{2\pi t}$ | eq. (7) |
| $s_p^+(t) = \frac{1}{\sqrt2}s_p(t) + \frac{j}{\sqrt2}\widehat{s}_p(t)$ | eq. (8) |
| $\widehat{s}_p(t) = s_p(t) * \frac{1}{\pi t}$ | trasformata di Hilbert, eq. (9) |
| $s_p(t) = \sqrt2\,\text{Re}\{s_p^+(t)\}$ | ritorno al segnale reale, eq. (10) |
| $S_p^+(f) = \frac{1}{\sqrt2}S_p(f) + \frac{j}{\sqrt2}\mathcal{F}[\widehat{s}_p(t)]$ | eq. (11) |
| $\widehat{S}_p(f) = S_p(f)\,\mathcal{F}\!\left[\frac{1}{\pi t}\right]$ | eq. (12) |
| $\mathcal{F}[\text{sgn}(t)] = \frac{1}{j\pi f}$, $\ \mathcal{F}\!\left[\frac{1}{\pi t}\right] = j\,\text{sgn}(-f)$ | trasformate ausiliarie |
| $\widehat{S}_p(f) = -j\,S_p(f)\,\text{sgn}(f)$ | Hilbert in frequenza |

Simboli: $u(\cdot)$ = gradino unitario; $\text{U}(f)$ = sua trasformata; $\delta$ = delta di Dirac; $\text{sgn}$ = funzione segno; $*$ = convoluzione; $\mathcal{F}$, $\mathcal{F}^{-1}$ = trasformata e antitrasformata di Fourier; $\widehat{s}_p$ = trasformata di Hilbert, con la stessa unità di $s_p$ (es. V). Anche $s_p^+$ ha l'unità di $s_p$, perché $\sqrt2$ è adimensionale.

> 🧮 Formula chiave: $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$ e $s_p(t) = \sqrt2\,\text{Re}\{s_p^+(t)\}$.

#### Derivazioni

##### Derivazione — Eq. (4): dal prodotto in frequenza alla convoluzione nel tempo · [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=12|12]]
$$
\begin{aligned}
s_p^+(t) &= \mathcal{F}^{-1}\big[S_p^+(f)\big] && \text{definizione di } s_p^+(t) \\
&= \mathcal{F}^{-1}\big[\sqrt2\,S_p(f)\cdot u(f)\big] && \text{sostituisco la (3)} \\
&= \sqrt2\,s_p(t) * \mathcal{F}^{-1}[u(f)] && \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
\end{aligned}
$$
Lo stesso passaggio è annotato a mano sopra la (4): $\sqrt2\,\mathcal{F}^{-1}[S_p(f)] * \mathcal{F}^{-1}[u(f)]$. Resta da calcolare l'antitrasformata del gradino **in frequenza**, che la nota a mano sulla (7) chiama appunto «antitrasformata del gradino».

##### Derivazione — Eq. (7): antitrasformata di $u(f)$ · [[Rappresentazione_Rice.pdf#page=12|p. 12]]
**Fonte:** «dalla (5) e dalla (6), applicando la riflessione».
> 🧩 Derivazione mia dei passaggi

$$
\begin{aligned}
\text{U}(t) &\ \xrightarrow{\ \mathcal{F}\ }\ u(-f) && \text{dualità, eq. (6): se } g(t) \to G(f) \text{ allora } G(t) \to g(-f) \\
\text{U}(-t) &\ \xrightarrow{\ \mathcal{F}\ }\ u(f) && \text{riflessione: } x(-t) \to X(-f) \\
\Rightarrow\ \mathcal{F}^{-1}[u(f)] &= \text{U}(-t) = \tfrac12\,\delta(-t) + \frac{1}{j2\pi(-t)} && \text{sostituisco } f \to -t \text{ nella (5)} \\
&= \tfrac12\,\delta(t) - \frac{1}{j2\pi t} && \delta \text{ è pari} \\
&= \tfrac12\,\delta(t) + \frac{j}{2\pi t} && -\tfrac1j = j
\end{aligned}
$$

##### Derivazione — Eq. (8): il segnale analitico nel tempo · [[Rappresentazione_Rice.pdf#page=12|p. 12]]
$$
\begin{aligned}
s_p^+(t) &= \sqrt2\,s_p(t) * \Big[\tfrac12\,\delta(t) + \frac{j}{2\pi t}\Big] && \text{la (7) nella (4)} \\
&= \frac{\sqrt2}{2}\,s_p(t) + \frac{\sqrt2\,j}{2}\;s_p(t) * \frac{1}{\pi t} && s * \delta = s;\ \tfrac{1}{2\pi t} = \tfrac12\cdot\tfrac{1}{\pi t} \\
&= \frac{1}{\sqrt2}\,s_p(t) + \frac{j}{\sqrt2}\,\widehat{s}_p(t) && \tfrac{\sqrt2}{2} = \tfrac{1}{\sqrt2};\ \text{definizione (9)}
\end{aligned}
$$
Note a mano: $s_p(t)$ è il «segnale reale passa-banda», $\widehat{s}_p(t)$ è la «trasformata di Hilbert di $s_p$».

##### Derivazione — Eq. (10) e corrispondenza biunivoca · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
**Fonte:** «dalla (8) si deduce immediatamente… Questo conclude la dimostrazione.» Nota a mano: «relazione inversa immediata», con accanto la (8).
> 🧩 Derivazione mia dei passaggi

$$
\begin{aligned}
\widehat{s}_p(t) &\in \mathbb{R} && \text{convoluzione di due funzioni reali, } s_p \text{ e } 1/(\pi t) \\
\text{Re}\{s_p^+(t)\} &= \frac{1}{\sqrt2}\,s_p(t) && \text{nella (8) } s_p \text{ e } \widehat{s}_p \text{ sono reali} \\
s_p(t) &= \sqrt2\,\text{Re}\{s_p^+(t)\} && \text{moltiplico per } \sqrt2
\end{aligned}
$$
**Cosa è stato dimostrato**, cioè l'affermazione della slide 8: da $s_p$ si calcola $s_p^+$ con la (8), e da $s_p^+$ si torna a $s_p$ con la (10). La corrispondenza è quindi **biunivoca**: il segnale analitico contiene tutta l'informazione di $s_p$.
> 🧩 Perché basta la parte reale: la parte negativa dello spettro scartata nella (3) si ricostruisce prendendo la parte reale, proprio perché per un segnale reale è lo specchio coniugato di quella positiva ([[segnali-banda-base-e-passa-banda]]).

##### Derivazione — Trasformata di $\text{sgn}(t)$ e di $1/(\pi t)$ · [[Rappresentazione_Rice.pdf#page=13|p. 13]], [[Rappresentazione_Rice.pdf#page=14|14]]
**Fonte:** risultati dati con un solo passaggio. La trasformata di $\text{sgn}(t)$ è svolta anche negli appunti di p. 14, con gli stessi passaggi.
> 📄 I primi tre passaggi sono quelli degli appunti di p.14; 🧩 gli ultimi due, con la dualità, sono miei.

![[rappresentazione-rice-p14-appunti-trasformata-sgn.png]]
*Appunti a mano: $\mathcal{F}[\text{sign}(t)] = \mathcal{F}[2u(t) - 1] = 2\mathcal{F}[u(t)] - \delta(f) = \delta(f) + \frac{1}{j\pi f} - \delta(f) = \frac{1}{j\pi f}$ (le due delta barrate si cancellano). Sotto, $\mathcal{F}[1/(\pi t)]$.*

$$
\begin{aligned}
\text{sgn}(t) &= 2\,u(t) - 1 && \text{vale } +1 \text{ per } t>0 \text{ e } -1 \text{ per } t<0 \\
\mathcal{F}[\text{sgn}(t)] &= 2\Big[\tfrac12\,\delta(f) + \frac{1}{j2\pi f}\Big] - \delta(f) && \text{linearità; eq. (5); } \mathcal{F}[1] = \delta(f) \\
&= \frac{1}{j\pi f} && \text{le delta si cancellano} \\
\mathcal{F}\Big[\frac{1}{j\pi t}\Big] &= \text{sgn}(-f) && \text{dualità} \\
\mathcal{F}\Big[\frac{1}{\pi t}\Big] &= j\,\text{sgn}(-f) = -j\,\text{sgn}(f) && \text{moltiplico per } j;\ \text{sgn è dispari}
\end{aligned}
$$

> ⚠️ Negli appunti di p.14 l'ultima riga è $\mathcal{F}[1/(\pi t)] = j\,\text{sign}(f)$: manca il meno. La slide scrive $j\,\text{sgn}(-f)$, cioè $-j\,\text{sgn}(f)$, ed è il segno giusto. È quello che dà $\widehat{S}_p = -j\,\text{sgn}(f)\,S_p$ e che fa tornare il controllo con la (3) qui sotto: con $+j$ si cancellerebbero le frequenze positive invece delle negative.

##### Derivazione — Trasformata di Hilbert in frequenza, eq. (12) · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
$$
\begin{aligned}
\widehat{S}_p(f) &= \mathcal{F}\Big[s_p(t) * \frac{1}{\pi t}\Big] = S_p(f)\,\mathcal{F}\Big[\frac{1}{\pi t}\Big] && \text{convoluzione} \to \text{prodotto, eq. (12)} \\
&= -j\,\text{sgn}(f)\,S_p(f) && \text{derivazione precedente}
\end{aligned}
$$
Note a mano sulla slide 10: sopra $\widehat{S}_p$ «$s_p(t) * \frac{1}{\pi t}$», sul segno di uguale «proprietà di Fourier» (convoluzione → prodotto), sotto il risultato «la trasformata di Hilbert in frequenza».

> ⚠️ Refuso della slide, corretto a mano nel PDF: nella (12) e nell'ultima formula compare $S(f)$ invece di $S_p(f)$. Qui $S(f)$ sarebbe l'inviluppo complesso, un'altra cosa.

##### Derivazione — Controllo: dalla (11) si ritrova la (3) · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
**Fonte:** p. 13 (slide 10), eq. (11)
> 🧩 Verifica mia: le due strade, frequenza (3) e tempo (8), devono dare lo stesso segnale analitico.

$$
\begin{aligned}
S_p^+(f) &= \frac{1}{\sqrt2}\,S_p(f) + \frac{j}{\sqrt2}\,\widehat{S}_p(f) && \text{eq. (11)} \\
&= \frac{1}{\sqrt2}\,S_p(f) + \frac{j}{\sqrt2}\big(-j\,\text{sgn}(f)\big)S_p(f) && \text{Hilbert in frequenza} \\
&= \frac{1}{\sqrt2}\,S_p(f)\,\big[1 + \text{sgn}(f)\big] && j\cdot(-j) = 1 \\
&= \frac{1}{\sqrt2}\,S_p(f)\cdot 2\,u(f) = \sqrt2\,S_p(f)\,u(f) && 1 + \text{sgn}(f) = 2\,u(f) \text{ per } f \neq 0
\end{aligned}
$$
È la (3) ✓. Il valore in $f = 0$ non conta: per un segnale passa-banda $S_p(0) \approx 0$.

##### Derivazione — Perché proprio √2 · [[Rappresentazione_Rice.pdf#page=11|p. 11]]
**Fonte:** nota a mano di p. 11 («introdotto per motivi energetici»)
> 🧩 Derivazione mia. Uso una costante generica $k$ al posto di $\sqrt2$: $S_p^+(f) = k\,S_p(f)\,u(f)$.

$$
\begin{aligned}
\|s_p^+\|^2 &= \int_{-\infty}^{+\infty}|S_p^+(f)|^2\,df && \text{Parseval: l'energia si calcola anche in frequenza} \\
&= k^2\int_{0}^{+\infty}|S_p(f)|^2\,df && S_p^+ = 0 \text{ per } f<0 \\
&= k^2\cdot\frac12\int_{-\infty}^{+\infty}|S_p(f)|^2\,df && |S_p(f)|^2 \text{ è pari: metà energia per lato} \\
&= \frac{k^2}{2}\,\|s_p\|^2 && \text{Parseval}
\end{aligned}
$$
**Risultato:** il segnale analitico ha la **stessa energia** di $s_p$ se e solo se $k^2/2 = 1$, cioè $k = \sqrt2$. Buttando via metà dello spettro si perde metà dell'energia, e il $\sqrt2$ la rimette.
**Conseguenza:** con la stessa scelta anche l'inviluppo complesso conserva l'energia, eq. (20) di [[inviluppo-complesso]].

#### Spiegazione

##### Esempio: il segnale analitico di un coseno
> 🧩 Esempio mio: applica le formule della slide al segnale passa-banda più semplice, $s_p(t) = \cos(2\pi f_0 t)$ con $f_0 > 0$.

$$
\begin{aligned}
s_p(t) &= \tfrac12\,e^{j2\pi f_0 t} + \tfrac12\,e^{-j2\pi f_0 t} && \text{Eulero: una riga a } +f_0 \text{ e una a } -f_0 \\
\widehat{s}_p(t) &= \tfrac12(-j)\,e^{j2\pi f_0 t} + \tfrac12(+j)\,e^{-j2\pi f_0 t} && -j\,\text{sgn}(f): \text{ la riga positiva } \times(-j), \text{ la negativa } \times(+j) \\
&= \frac{e^{j2\pi f_0 t} - e^{-j2\pi f_0 t}}{2j} = \sin(2\pi f_0 t) && -\tfrac{j}{2} = \tfrac{1}{2j} \\
s_p^+(t) &= \frac{1}{\sqrt2}\big[\cos(2\pi f_0 t) + j\sin(2\pi f_0 t)\big] = \frac{1}{\sqrt2}\,e^{j2\pi f_0 t} && \text{eq. (8) e formula di Eulero}
\end{aligned}
$$

Si legge tutto:
- la trasformata di Hilbert trasforma il coseno nel seno, cioè lo **sfasa di 90°**;
- il segnale analitico è un **esponenziale complesso**, un vettore che ruota. Ha una sola riga, a $+f_0$: è proprio lo spettro di $s_p$ senza la parte negativa, come vuole la (3);
- $\sqrt2\,\text{Re}\{s_p^+\} = \text{Re}\{e^{j2\pi f_0 t}\} = \cos(2\pi f_0 t)$ ✓, eq. (10);
- energia: la riga di $s_p^+$ ha modulo $1/\sqrt2$, quelle di $s_p$ hanno modulo $1/2$. Vale $(1/\sqrt2)^2 = 1/2 = (1/2)^2 + (1/2)^2$: la potenza è la stessa ✓.

##### La trasformata di Hilbert come sfasatore di 90° · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
> 📄 Fonte: nota a mano su p. 13 (slide 10): «in pratica la trasformata di Hilbert di un segnale equivale a sfasare di −90° tutte le componenti frequenziali positive e di +90° tutte quelle negative».

![[rappresentazione-rice-p13-segnale-analitico-hilbert.png]]
*con le note a mano: relazione inversa (10), proprietà di Fourier nella (12), trasformata di Hilbert in frequenza e sfasamento di ∓90°.*

> 🧩 Perché, in termini di filtro (lettura mia): il trasformatore di Hilbert è un sistema LTI con risposta in frequenza $H_{\mathcal{H}}(f) = -j\,\text{sgn}(f)$ e risposta impulsiva $1/(\pi t)$.
> - $|H_{\mathcal{H}}(f)| = 1$: non cambia l'ampiezza di nessuna componente.
> - Per $f > 0$ moltiplica per $-j = e^{-j\pi/2}$, cioè fase $-90°$; per $f < 0$ moltiplica per $+j = e^{+j\pi/2}$, cioè $+90°$. È lo sfasamento della nota, verificato sul coseno qui sopra.

Il segnale analitico (8) è quindi il segnale di partenza più $j$ volte la sua versione sfasata di 90°, a meno del fattore $1/\sqrt2$. La somma cancella le frequenze negative e raddoppia le positive.

> 🎯 Esame: definire il segnale analitico (3); ricavarne l'espressione nel tempo (8) passando per la (7); dimostrare la (10) e la biunivocità; ricavare $\widehat{S}_p(f) = -j\,\text{sgn}(f)\,S_p(f)$; spiegare il ruolo del $\sqrt2$.

#### Perché importa

È il passo intermedio verso l'[[inviluppo-complesso]]. Scartare le frequenze negative non perde nulla, perché sono ridondanti per un segnale reale. Dopo lo scarto resta un solo lobo, attorno a $+f_c$, che si può traslare in banda base (eq. (13)).

#### Connessioni

- [[segnali-banda-base-e-passa-banda]] — la simmetria hermitiana rende ridondante la metà negativa dello spettro.
- [[inviluppo-complesso]] — si ottiene traslando il segnale analitico di $-f_c$: $S(f) = S_p^+(f + f_c)$.
- [[upconversion-e-downconversion]] — la (10), $s_p = \sqrt2\,\text{Re}\{\cdot\}$, è anche il principio dell'upconversion.

#### Fonti · [[Rappresentazione_Rice.pdf#page=11|p. 11]]–[[Rappresentazione_Rice.pdf#page=14|14]]

- [[rappresentazione-complessa-banda-base]]

### Upconversion e downconversion · [[upconversion-e-downconversion|pagina]]

#### Definizione · [[Rappresentazione_Rice.pdf#page=20|p. 20]]

- **Upconversion** (conversione in su): passaggio dalla banda base alla banda passante. Dato l'inviluppo complesso $s = s_c + js_s$, si genera il segnale passa-banda con la (17) di [[inviluppo-complesso]]:
$$s_p(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{17}$$
  La slide dice che la (17) indica «immediatamente» come fare l'upconversion.
- **Downconversion** (conversione in giù): passaggio dalla banda passante alla banda base. Si moltiplica $s_p(t)$ per la portante e si filtra passa-basso:
$$\sqrt2\,s_p(t)\cos(2\pi f_c t) = s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) \tag{21}$$
  Un **filtro passa-basso** recupera la componente I. La componente Q si ottiene allo stesso modo, filtrando passa-basso $-\sqrt2\,s_p(t)\sin(2\pi f_c t)$.

##### Il passaggio complesso ↔ reale (appunti p.2) · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

Gli appunti di p.2 descrivono i due stadi dal punto di vista di cosa fanno al segnale:
- **Trasmettitore:** porta il segnale nella specifica porzione dello spettro, «per adattare il segnale rispetto alla capacità del canale». È l'upconversion.
- **Ricevitore:** porta il segnale in banda base, e questo «comporta che il segnale diventa complesso». È la downconversion.
- In entrambi i momenti, trasmissione e ricezione, il segnale in banda base è complesso. Quindi:
  - in trasmissione il passaggio è **complesso → reale**: dall'inviluppo $s = s_c + js_s$ al segnale fisico $s_p$;
  - in ricezione è **reale → complesso**: da $s_p$ di nuovo a $s_c$ e $s_s$.
- Nota finale: «in entrambi i casi è un processo eseguito da un DSP».

> 🧩 Perché il segnale fisico è reale e quello in banda base complesso: sul canale viaggia una tensione o un campo, che è una grandezza reale, quindi $s_p(t)$ è reale. In banda base invece lo spettro di $s_p$ attorno a $+f_c$, spostato in 0, non è in generale simmetrico, e un segnale con spettro non hermitiano è complesso ([[inviluppo-complesso]]). La (17) è il complesso → reale: prende $s_c$ e $s_s$ e restituisce un solo segnale reale. La downconversion fa il contrario.

> ⚠️ Da chiarire: nello schema della slide 7 upconversion e downconversion sono passi distinti dal DSP, che lavora solo sull'inviluppo in banda base. La slide 6 dice che l'elaborazione analogica va ridotta al minimo, senza dire quali blocchi restano analogici. La nota di p.2 attribuisce invece il passaggio complesso ↔ reale a un DSP.

#### Formule · [[Rappresentazione_Rice.pdf#page=16|p. 16]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

| Formula | Significato |
|---|---|
| $s_p = \sqrt2 s_c\cos(2\pi f_c t) - \sqrt2 s_s\sin(2\pi f_c t)$ | upconversion, eq. (17) |
| $\sqrt2\,s_p\cos(2\pi f_c t) = s_c + s_c\cos(4\pi f_c t) - s_s\sin(4\pi f_c t)$ | ramo I della downconversion, eq. (21) |
| $-\sqrt2\,s_p\sin(2\pi f_c t) = s_s - s_s\cos(4\pi f_c t) - s_c\sin(4\pi f_c t)$ | ramo Q della downconversion |
| $s(t) = \text{LPF}\big\{\sqrt2\,s_p(t)\,e^{-j2\pi f_c t}\big\}$ | i due rami in forma complessa |

Simboli: $f_c$ = portante [Hz]; $s_c$, $s_s$ = componenti I e Q (es. V); LPF = filtro passa-basso ideale; $4\pi f_c t = 2\pi(2f_c)t$, quindi i termini con $\cos(4\pi f_c t)$ e $\sin(4\pi f_c t)$ stanno attorno a $\pm 2f_c$.

#### Derivazioni

##### Derivazione — Eq. (21): ramo I della downconversion · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
$$
\begin{aligned}
\sqrt2\,s_p\cos\alpha &= \sqrt2\big[\sqrt2\,s_c\cos\alpha - \sqrt2\,s_s\sin\alpha\big]\cos\alpha && \text{sostituisco la (17); } \alpha = 2\pi f_c t \\
&= 2\,s_c\cos^2\alpha - 2\,s_s\sin\alpha\cos\alpha && \sqrt2\cdot\sqrt2 = 2 \\
&= s_c\,(1 + \cos 2\alpha) - s_s\sin 2\alpha && 2\cos^2\alpha = 1 + \cos 2\alpha;\ \ 2\sin\alpha\cos\alpha = \sin 2\alpha \\
&= s_c(t) + s_c(t)\cos(4\pi f_c t) - s_s(t)\sin(4\pi f_c t) && 2\alpha = 4\pi f_c t
\end{aligned}
$$
**Lettura:** il primo termine è $s_c(t)$, in banda base. Gli altri due sono $s_c$ e $s_s$ riportati attorno a $2f_c$. La nota a mano sulla slide li sottolinea con «tagliati dal filtro»: è il passa-basso a eliminarli. La componente Q compare **solo** attorno a $2f_c$: il prodotto $\sin\alpha\cos\alpha$ non ha parte lenta.

##### Derivazione — Ramo Q della downconversion · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** «similmente si ottiene la componente Q».
> 🧩 Derivazione mia

$$
\begin{aligned}
-\sqrt2\,s_p\sin\alpha &= -\sqrt2\big[\sqrt2\,s_c\cos\alpha - \sqrt2\,s_s\sin\alpha\big]\sin\alpha && \text{sostituisco la (17)} \\
&= -2\,s_c\sin\alpha\cos\alpha + 2\,s_s\sin^2\alpha && \text{sviluppo} \\
&= -s_c\sin 2\alpha + s_s\,(1 - \cos 2\alpha) && 2\sin^2\alpha = 1 - \cos 2\alpha \\
&= s_s(t) - s_s(t)\cos(4\pi f_c t) - s_c(t)\sin(4\pi f_c t)
\end{aligned}
$$
Dopo il passa-basso resta $s_s(t)$. Il segno meno davanti a $\sqrt2\sin$ compensa il meno della (17).

##### Derivazione — Requisito sul filtro passa-basso · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** la slide dice solo «filtrando passa-basso».
> 🧩 Derivazione mia. $W$ = banda di $s_c$ e $s_s$ (per un segnale passa-banda $W = B/2$, vedi [[inviluppo-complesso]]).

- Il termine utile $s_c(t)$ occupa $|f| < W$.
- I termini $s_c\cos(4\pi f_c t)$ e $s_s\sin(4\pi f_c t)$ occupano $|f \mp 2f_c| < W$, cioè da $2f_c - W$ in su.
- Un passa-basso con frequenza di taglio $f_{LP}$ li separa se
$$W \le f_{LP} \le 2f_c - W$$
- L'intervallo esiste se $W \le 2f_c - W$, cioè $W \le f_c$: sempre vero per un segnale passa-banda, perché $W = B/2 < f_c$. Con la banda stretta ($B \ll f_c$) i termini a $2f_c$ sono lontanissimi e il filtro è facile da realizzare.

##### Derivazione — Perché il √2 nei moltiplicatori · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
**Fonte:** figura di p. 20 (slide 14): portanti $\sqrt2\cos(2\pi f_c t)$ e $-\sqrt2\sin(2\pi f_c t)$ sia in trasmissione sia in ricezione.
> 🧩 Derivazione mia

Il guadagno complessivo del ramo I, dal trasmettitore all'uscita del filtro, è
$$\underbrace{\sqrt2}_{\text{upconverter}}\cdot\underbrace{\sqrt2}_{\text{downconverter}}\cdot\underbrace{\tfrac12}_{\text{parte lenta di }\cos^2} = 1$$
Quindi $s_c$ esce senza cambiare ampiezza. Nello stesso tempo $s_p$ ha la stessa energia di $s$, eq. (20) di [[inviluppo-complesso]].

##### Derivazione — I due rami sono una sola moltiplicazione complessa
> 🧩 Derivazione mia: collega lo schema a due rami alla (15).

$$
\begin{aligned}
\sqrt2\,s_p(t)\,e^{-j2\pi f_c t} &= \sqrt2\,s_p\cos\alpha - j\sqrt2\,s_p\sin\alpha && \text{Eulero: } e^{-j\alpha} = \cos\alpha - j\sin\alpha \\
&= \big[\sqrt2\,s_p\cos\alpha\big] + j\big[-\sqrt2\,s_p\sin\alpha\big] && \text{parte reale = ramo I, parte immaginaria = ramo Q} \\
\text{LPF}\{\cdot\} &= s_c(t) + j\,s_s(t) = s(t) && \text{(21) e ramo Q}
\end{aligned}
$$
La downconversion è quindi "moltiplica per $\sqrt2\,e^{-j2\pi f_c t}$ e filtra". Corrisponde alla (15), che trasla lo spettro di $-f_c$. Il filtro qui serve a eliminare le repliche a $\pm 2f_c$, che la (15) non genera perché parte dal segnale analitico, privo delle frequenze negative.

#### Spiegazione

##### Gli schemi a blocchi (slide 14) · [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]

![[rappresentazione-rice-p20-upconversion-downconversion.png]]
- *Upconversion (da banda base a banda passante): $s_c(t)$ moltiplicato per $\sqrt2\cos 2\pi f_c t$, $s_s(t)$ moltiplicato per $-\sqrt2\sin 2\pi f_c t$; la somma dei due dà $s_p(t)$.*
- *Downconversion (da banda passante a banda base): $s_p(t)$ entra in due rami; uno lo moltiplica per $\sqrt2\cos 2\pi f_c t$ e lo filtra passa-basso ottenendo $s_c(t)$, l'altro lo moltiplica per $-\sqrt2\sin 2\pi f_c t$ e lo filtra ottenendo $s_s(t)$.*
- *Note a mano: a sinistra S → $s(n)$ → MOD, che produce le due componenti $s_c(t)$ e $s_s(t)$ in ingresso all'upconverter. Sopra il modulatore: «esce l'inviluppo». Sotto la (21), i due termini a $2f_c$ sono sottolineati con «tagliati dal filtro».*

> 💡 Connessione: «esce l'inviluppo» vuol dire che il modulatore di questo disegno è la sola parte in banda base (il DSP della slide 7). Nelle note di p. 10 il macroblocco "modulatore" comprende anche l'upconversion: il nome MOD qui indica solo il primo dei due passi ([[modulazione-digitale]]).

##### La downconversion passo per passo (animazione) · [[Rappresentazione_Rice.pdf#page=20|p. 20]]
![[grafico-rice-downconversion.gif]]
*🧩 Animazione mia della (21). Stesso esempio del grafico I/Q in [[inviluppo-complesso]]: I con righe a 1 e 2 kHz (blu), Q con una riga a 1.5 kHz (arancio), $f_c = 10$ kHz.*
1. *Il segnale passa-banda ha le righe di I e di Q attorno a $\pm f_c$.*
2. *Moltiplicare per $\sqrt2\cos(2\pi f_c t)$ sdoppia ogni riga: una copia va verso 0, l'altra verso $\pm 2f_c$.*
3. *Attorno a 0 le due copie di I si sommano, quelle di Q hanno segno opposto e si cancellano.*
4. *Il passa-basso elimina le copie a $\pm 2f_c$.*
5. *Esce $s_c(t)$, identico a quello di partenza.*

*Le ampiezze delle righe sono controllate con la FFT nello script: 0.5 e 0.25 in banda base, nessuna riga a 1.5 kHz.*

##### Tutta la catena come un unico canale (appunti p.21) · [[Rappresentazione_Rice.pdf#page=21|p. 21]]

![[rappresentazione-rice-p21-appunti-canale-equivalente.png]]
*Appunti a mano: S → MOD → upconverter → canale fisico → downconverter → DEMOD → utente. I tre blocchi centrali, cerchiati, sono «modellati come un unico canale». A destra la domanda «con tutti i passaggi che abbiamo fatto si conserva l'energia?» e la risposta «sì, per le accortezze fatte ($\sqrt2$)».*

- Modulatore e demodulatore lavorano in banda base. Tutto quello che sta in mezzo (upconverter, canale fisico, downconverter) si può vedere come **un solo canale equivalente in banda base**. Come si descrive il filtraggio del canale in banda base è in [[equivalente-banda-base-dei-filtri]].
- L'energia si conserva lungo la catena grazie ai fattori $\sqrt2$: eq. (20) e derivazione del $\sqrt2$ qui sopra.

##### Cosa si recupera davvero (slide 15) · [[Rappresentazione_Rice.pdf#page=22|p. 22]]

La downconversion estrae le variazioni **lente** di ampiezza e fase dovute alla modulazione, e toglie la variazione di fase **rapida e prevedibile** dovuta a $f_c$. Quella variazione non porta informazione, quindi l'inviluppo complesso contiene **tutta** l'informazione del segnale passa-banda. Nota a mano in testa alla slide: «l'inviluppo complesso ci permette di separare le variazioni lente introdotte dalla modulazione in banda base». Sulla slide sono evidenziati «eliminating» e $f_c$: la parte eliminata è proprio quella legata alla portante. Dettagli e grafico in [[inviluppo-complesso]].

> 🎯 Esame: disegnare gli schemi di upconversion e downconversion; ricavare la (21) e il ramo Q; spiegare perché serve il passa-basso e che banda deve avere; spiegare perché Q non "sporca" il ramo I.

#### Perché importa · [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

Nello schema modulare del transceiver upconversion e downconversion sono gli unici passi che toccano il segnale passa-banda. Tutto il resto lo fa il DSP sull'inviluppo in banda base: codifica, modulazione e filtraggio in trasmissione; sincronizzazione, demodulazione e decodifica in ricezione. Upconverter e downconverter sono quindi l'interfaccia tra il mondo in banda base del DSP e il canale fisico passa-banda. La slide 6 aggiunge che così i transceiver elaborano in digitale direttamente l'inviluppo, «riducendo al minimo la parte di elaborazione analogica» (nota a mano).

Le note a mano della slide 7 raggruppano i passi in due **macroblocchi**:
- **modulatore** = DSP di trasmissione + upconversion;
- **demodulatore** = downconversion + DSP di ricezione.

Grazie a questa separazione gli algoritmi si sviluppano in banda base, indipendentemente dalla banda fisica usata. Nota a mano: «quindi ci si è svincolati dalla frequenza carrier ($f_c$)».

> 🧩 Conseguenza pratica (mia): $f_c$ compare solo nelle portanti $\sqrt2\cos(2\pi f_c t)$ e $-\sqrt2\sin(2\pi f_c t)$ dei due convertitori. Per trasmettere su un'altra banda basta cambiare quelle; il DSP resta identico.

#### Connessioni

- [[inviluppo-complesso]] — l'upconversion realizza la (17), la downconversion la (15).
- [[segnale-analitico]] — la forma complessa della downconversion è la traslazione di $-f_c$ del segnale analitico.
- [[equivalente-banda-base-dei-filtri]] — la catena upconverter + canale + downconverter diventa un canale in banda base.
- [[modulazione-digitale]] — il modulatore fornisce $s_c$ e $s_s$ all'upconverter.
- [[segnali-banda-base-e-passa-banda]] — il requisito $W < f_c$ sul filtro viene dalla definizione di passa-banda.

#### Fonti · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=10|p. 10]], [[Rappresentazione_Rice.pdf#page=20|p. 20]]–[[Rappresentazione_Rice.pdf#page=22|22]]

- [[rappresentazione-complessa-banda-base]]

### Equivalente in banda base di un filtro passa-banda · [[equivalente-banda-base-dei-filtri|pagina]]

#### Definizione · [[Rappresentazione_Rice.pdf#page=23|p. 23]]

**Qualunque filtro passa-banda si può realizzare in banda base complessa.** Sia $s_p(t)$ un segnale passa-banda che attraversa un filtro passa-banda con risposta impulsiva $h_p(t)$:
$$y_p(t) = s_p(t) * h_p(t)$$
Siano $s(t)$, $h(t)$, $y(t)$ gli inviluppi complessi di $s_p$, $h_p$, $y_p$, calcolati **rispetto alla stessa frequenza di riferimento** $f_c$, e $S(f)$, $H(f)$, $Y(f)$ le loro trasformate. Allora
$$Y(f) = \frac{1}{\sqrt2}\,S(f)\,H(f) \tag{22}$$
$$y(t) = \frac{1}{\sqrt2}\,s(t) * h(t) \tag{23}$$
In banda base, filtrare significa **convolvere gli inviluppi**, con un fattore $1/\sqrt2$.

> 🧩 Perché serve un riferimento comune: l'inviluppo dipende da $f_c$. Cambiare riferimento trasla l'inviluppo in frequenza ([[inviluppo-complesso]]), e la (22) vale solo se i tre inviluppi sono traslati della stessa quantità.

#### Formule · [[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]

| Formula | Significato |
|---|---|
| $Y_p(f) = S_p(f)\,H_p(f)$ | filtro LTI in frequenza |
| $Y_p^+ = \sqrt2 Y_p u(f)$, $S_p^+ = \sqrt2 S_p u(f)$, $H_p^+ = \sqrt2 H_p u(f)$ | segnali analitici ("segmenti a frequenze positive") |
| $Y(f) = \frac{1}{\sqrt2}S(f)H(f)$ | eq. (22) |
| $y(t) = \frac{1}{\sqrt2}\,s(t) * h(t)$ | eq. (23) |
| $y_c = \frac{1}{\sqrt2}[s_c * h_c - s_s * h_s]$ | componente I dell'uscita, eq. (24) |
| $y_s = \frac{1}{\sqrt2}[s_s * h_c + s_c * h_s]$ | componente Q dell'uscita, eq. (25) |

Simboli: $h_p(t)$ = risposta impulsiva del filtro passa-banda [1/s]; $h = h_c + jh_s$ = suo inviluppo complesso; $s = s_c + js_s$ e $y = y_c + jy_s$ = inviluppi di ingresso e uscita; $*$ = convoluzione; $u(\cdot)$ = gradino unitario.

> 🧮 Formula chiave: $y(t) = \frac{1}{\sqrt2}\,s(t) * h(t)$.

#### Derivazioni

##### Derivazione — Eq. (22) · [[Rappresentazione_Rice.pdf#page=23|p. 23]], [[Rappresentazione_Rice.pdf#page=24|24]]
**Fonte:** p. 23 (slide 16) per l'impostazione; p. 24 (appunti a mano) per la catena completa, compreso il passaggio che la slide salta.
> 📄 La catena è quella degli appunti di p.24. Lì l'ingresso si chiama $x_p(t)$ (inviluppo $x(t)$); qui uso $s$ come nella slide. Tra virgolette le note a mano; gli altri commenti sono 🧩 miei.

Gli appunti partono da $y_p(t) = x_p(t) * h_p(t)$ e dalla domanda «l'uscita come diventa in termini di inviluppo complesso?». La risposta: «ragioniamo in $f$». Nel tempo c'è una convoluzione; in frequenza diventa un prodotto, $Y_p(f) = X_p(f)\,H_p(f)$, molto più facile da maneggiare. Servono poi i tre segnali analitici, scritti uno sotto l'altro negli appunti:
$$Y_p^+(f) = \sqrt2\,Y_p(f)\,u(f), \qquad X_p^+(f) = \sqrt2\,X_p(f)\,u(f), \qquad H_p^+(f) = \sqrt2\,H_p(f)\,u(f)$$

$$
\begin{aligned}
Y(f) &= Y_p^+(f + f_c) && \text{definizione (13) di inviluppo, applicata a } y_p \\
&= \sqrt2\,Y_p(f + f_c)\,u(f + f_c) && \text{definizione (3) di segnale analitico, calcolata in } f + f_c \\
&= \sqrt2\,S_p(f + f_c)\,H_p(f + f_c)\,u^2(f + f_c) && \text{«sostituisco l'uscita» } Y_p = S_p H_p;\ u \to u^2 \text{ «non altera nulla»} \\
&= \sqrt2\,S_p(f + f_c)\,H_p(f + f_c)\,u^2(f + f_c)\cdot\frac{\sqrt2}{\sqrt2} && \text{moltiplico e divido per } \sqrt2 \\
&= \frac{1}{\sqrt2}\,\big[\sqrt2\,S_p(f + f_c)\,u(f + f_c)\big]\,\big[\sqrt2\,H_p(f + f_c)\,u(f + f_c)\big] && \text{un } \sqrt2 \text{ e una } u \text{ per fattore; } \tfrac{1}{\sqrt2} \text{ «resta fuori»} \\
&= \frac{1}{\sqrt2}\,S(f)\,H(f) && \text{(13) per } s \text{ e per } h\text{: le parentesi sono } S(f) \text{ e } H(f)
\end{aligned}
$$

Il perché dei due trucchi:
- **$u \to u^2$.** Il gradino vale solo 0 o 1, e $0^2 = 0$, $1^2 = 1$: elevarlo al quadrato non cambia nulla. Serve ad avere **due** gradini, uno da assegnare a $S_p$ e uno a $H_p$. Così ciascuno dei due fattori diventa il segnale analitico del suo segnale.
- **$\cdot\sqrt2/\sqrt2$.** Anche questo non cambia il valore (moltiplica per 1). Nella riga c'è un solo $\sqrt2$, ma per ricostruire due inviluppi ne servono due, uno per fattore. Moltiplicando e dividendo per $\sqrt2$ al numeratore ce ne sono due, $\sqrt2\cdot\sqrt2$, e al denominatore resta un $\sqrt2$: è il $\frac{1}{\sqrt2}$ che «resta fuori».

**Da dove viene il $1/\sqrt2$:** ogni inviluppo porta con sé un $\sqrt2$ (definizione (3)). Nel prodotto $SH$ i fattori $\sqrt2$ sono due, mentre $Y$, che è un solo inviluppo, ne deve avere uno solo. Il $1/\sqrt2$ toglie quello in più.

**Sanity check (🧩):** controllo sulle altezze della figura di slide 17, più sotto: torna $\sqrt2 AB$ ✓.

![[rappresentazione-rice-p24-appunti-filtro-equivalente.png]]
*Appunti a mano.*
- *A sinistra, due schemi: in alto il sistema reale, $x_p(t)$ → LTI con $h_p(t)$ → $y_p(t)$; sotto lo stesso sistema visto sugli inviluppi, $x(t)$ → LTI con $h(t)$ → $y(t)$.*
- *A destra la catena della (22), come sopra, con le tre note in verde e azzurro: «sostituisco l'uscita», «non altera nulla» su $u^2$, «resta fuori» sotto $\frac{1}{\sqrt2}$.*
- *In fondo la conclusione: l'inviluppo complesso di $y_p(t)$ nel dominio della frequenza è $Y(f) = \frac{1}{\sqrt2}X(f)H(f)$, «che si traduce nel dominio del tempo» in $y(t) = \frac{1}{\sqrt2}\,x(t) * h(t)$.*

##### Derivazione — Eq. (23) · [[Rappresentazione_Rice.pdf#page=24|p. 24]], [[Rappresentazione_Rice.pdf#page=25|25]]
**Fonte:** p. 25 (slide 17); lo stesso passaggio chiude gli appunti di p. 24.
$$
y(t) = \mathcal{F}^{-1}[Y(f)] = \frac{1}{\sqrt2}\,\mathcal{F}^{-1}\big[S(f)\,H(f)\big] = \frac{1}{\sqrt2}\,s(t) * h(t) \qquad \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
$$

##### Derivazione — Eq. (24) e (25): le componenti I e Q dell'uscita · [[Rappresentazione_Rice.pdf#page=26|p. 26]]
> 📄 La catena è scritta a mano sotto lo schema della slide 18 (prima riga, penultima e ultima). La riga intermedia con i quattro termini e i commenti a destra sono 🧩 miei.

$$
\begin{aligned}
y(t) &= \frac{1}{\sqrt2}\,s(t) * h(t) && \text{(23)} \\
&= \frac{1}{\sqrt2}\,\big[s_c(t) + js_s(t)\big] * \big[h_c(t) + jh_s(t)\big] && \text{componenti I e Q: } s = s_c + js_s,\ h = h_c + jh_s \\
&= \frac{1}{\sqrt2}\,\big[s_c * h_c + j\,s_c * h_s + j\,s_s * h_c + j^2\,s_s * h_s\big] && \text{la convoluzione è bilineare: si sviluppa come un prodotto} \\
&= \frac{1}{\sqrt2}\,\big[s_c * h_c - s_s * h_s\big] + \frac{j}{\sqrt2}\,\big[s_c * h_s + s_s * h_c\big] && j^2 = -1;\ \text{raccolgo parte reale e parte immaginaria} \\
y_c(t) &= \frac{1}{\sqrt2}\big[s_c * h_c - s_s * h_s\big] && \text{parte reale: eq. (24)} \\
y_s(t) &= \frac{1}{\sqrt2}\big[s_s * h_c + s_c * h_s\big] && \text{parte immaginaria: eq. (25)}
\end{aligned}
$$
Servono **quattro convoluzioni reali**. È la stessa regola del prodotto di due numeri complessi, $(a + jb)(c + jd) = (ac - bd) + j(bc + ad)$, con la convoluzione al posto del prodotto.

> 🧩 Perché si può sviluppare come un prodotto: la convoluzione è lineare in ciascuno dei due argomenti, $(a + b) * c = a * c + b * c$ e $(\alpha a) * c = \alpha\,(a * c)$ anche per $\alpha = j$. I segnali $s_c, s_s, h_c, h_s$ sono reali, quindi ogni convoluzione $s_\cdot * h_\cdot$ è reale e la separazione tra parte reale e immaginaria è quella scritta.

##### Derivazione — Controllo sulle altezze della figura (slide 17) · [[Rappresentazione_Rice.pdf#page=25|p. 25]]
> 🧩 Verifica mia. In figura $A$ è l'altezza del filtro e $B$ quella dello spettro d'ingresso (non la banda).

$$
\begin{aligned}
\text{passa-banda: } Y_p &= S_p H_p \Rightarrow \text{altezza } A\cdot B = AB && \text{dove i due spettri si sovrappongono} \\
\text{banda base: } H &\to \sqrt2 A,\quad S \to \sqrt2 B && \text{(13): gli inviluppi hanno altezza } \times\sqrt2 \\
Y &= \tfrac{1}{\sqrt2}\,(\sqrt2 A)(\sqrt2 B) = \sqrt2\,AB && \text{(22)}
\end{aligned}
$$
Coincide con il $\sqrt2 AB$ della figura, ed è anche l'inviluppo di $Y_p$ calcolato direttamente con la (13): $\sqrt2\cdot AB$ ✓.

#### Spiegazione

##### Passa-banda e banda base a confronto (slide 17) · [[Rappresentazione_Rice.pdf#page=25|p. 25]]

![[rappresentazione-rice-p25-filtraggio-spettri.png]]
*A sinistra, in banda passante: filtro $H_p(f)$, rettangoli di altezza $A$ attorno a $\pm f_c$; ingresso $S_p(f)$, triangoli di altezza $B$; uscita $Y_p(f)$, il triangolo "tagliato" dal rettangolo, altezza $AB$. A destra, in banda base complessa, gli stessi spettri attorno a 0 con un solo lobo: filtro $H(f)$ di altezza $\sqrt2 A$, ingresso $S(f)$ di altezza $\sqrt2 B$, uscita $Y(f)$ di altezza $\sqrt2 AB$.*

##### Realizzazione con operazioni reali (slide 18) · [[Rappresentazione_Rice.pdf#page=26|p. 26]]

![[rappresentazione-rice-p26-filtro-banda-base-iq.png]]
- *Il segnale passa-banda $s_p(t)$ entra nel downconverter, che produce $s_c(t)$ e $s_s(t)$.*
- *Il riquadro tratteggiato, "operazioni reali in banda base", contiene quattro filtri reali: $s_c$ passa per $h_c$ e $h_s$, $s_s$ per $h_c$ e $h_s$. Due sommatori formano $y_c = s_c * h_c - s_s * h_s$ (con il segno meno) e $y_s = s_s * h_c + s_c * h_s$.*
- *A mano, sotto: la catena delle (24)–(25) riportata nella derivazione sopra.*
- *A mano, a destra: le due uscite confluiscono in un sommatore che forma $y(t)$, «segnale in banda base». $y(t)$ va a un DSP «che lavora in banda base».*

> ⚠️ Nella figura manca il fattore $1/\sqrt2$ delle (24)–(25): le uscite disegnate sono $\sqrt2\,y_c$ e $\sqrt2\,y_s$. La nota a mano sotto lo schema invece il $1/\sqrt2$ ce l'ha.

> 🧩 Il sommatore disegnato a mano va letto come $y = y_c + j\,y_s$: la componente Q entra moltiplicata per $j$, non sommata così com'è. Nel DSP le due componenti viaggiano come parte reale e parte immaginaria di un unico numero complesso.

> 🧩 Quando i termini incrociati spariscono (osservazione mia): se $h(t)$ è reale, cioè $h_s = 0$, le (24)–(25) diventano $y_c = \frac{1}{\sqrt2}\,s_c * h_c$ e $y_s = \frac{1}{\sqrt2}\,s_s * h_c$. I e Q vengono filtrati separatamente, senza mescolarsi. Per la simmetria hermitiana ([[segnali-banda-base-e-passa-banda]]), $h$ è reale quando $H(f) = H^*(-f)$, cioè quando il filtro passa-banda è simmetrico (coniugato) attorno a $f_c$. Nella figura della slide 17 il rettangolo $H(f)$ non è centrato in 0: in quel caso $h_s \neq 0$ e i termini incrociati ci sono.

##### A cosa serve · [[Rappresentazione_Rice.pdf#page=21|p. 21]], [[Rappresentazione_Rice.pdf#page=26|p. 26]]

Gli appunti di p. 21 vedono upconverter, canale fisico e downconverter come **un unico canale** ([[upconversion-e-downconversion]]). Questa pagina dice come descriverlo: se il canale fisico è un filtro LTI passa-banda $h_p$, visto dalla banda base è il filtro $h/\sqrt2$ che agisce sull'inviluppo. Tutto si può quindi simulare e trattare in banda base. La nota a mano della slide 18 chiude il cerchio: l'uscita $y(t)$ è un segnale in banda base e va al DSP del ricevitore, che lavora in banda base.

> 🎯 Esame: ricavare la (22) partendo dai segnali analitici; spiegare il fattore $1/\sqrt2$; scrivere le (24)–(25) e disegnare lo schema con quattro filtri reali.

#### Perché importa

Completa la rappresentazione in banda base. Non solo i segnali, ma anche i **sistemi** passa-banda (filtri, canali LTI) hanno un equivalente in banda base. Si può allora lavorare interamente con gli inviluppi, dal modulatore al demodulatore, senza mai tornare a $f_c$.

#### Connessioni

- [[inviluppo-complesso]] — definizione (13) usata per $s$, $h$ e $y$; dipendenza dal riferimento $f_c$.
- [[segnale-analitico]] — la dimostrazione passa per $Y_p^+$, $S_p^+$, $H_p^+$.
- [[upconversion-e-downconversion]] — il downconverter fornisce $s_c$ e $s_s$ ai quattro filtri; la catena diventa un canale in banda base.
- [[segnali-banda-base-e-passa-banda]] — il canale passa-banda è un sistema LTI che soddisfa la (2).

#### Fonti · [[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]

- [[rappresentazione-complessa-banda-base]]


---

## Lezione 5 — Processi aleatori

### Processo aleatorio (processo stocastico) · [[processo-aleatorio|pagina]]

#### Definizione · [[random_processes.pdf#page=2|p. 2]]–[[random_processes.pdf#page=7|7]]

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

#### Formule · [[random_processes.pdf#page=4|p. 4]]–[[random_processes.pdf#page=6|6]], [[random_processes.pdf#page=8|p. 8]]–[[random_processes.pdf#page=10|10]], [[random_processes.pdf#page=45|p. 45]]

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

#### Derivazioni

##### Derivazione — Coerenza delle distribuzioni: quelle di ordine basso sono marginali · [[random_processes.pdf#page=9|p. 9]], [[random_processes.pdf#page=11|p. 11]]
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

##### Derivazione — DF del processo di Bernoulli, primo e secondo ordine · [[random_processes.pdf#page=10|p. 10]], [[random_processes.pdf#page=11|11]]
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

#### Spiegazione

##### Esempio della slide: un rettangolo di segno casuale · [[random_processes.pdf#page=2|p. 2]]

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

##### Esempio degli appunti: sinusoide a fase casuale · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]]

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

##### Il quadro generale: esiti, realizzazioni, variabili aleatorie · [[random_processes.pdf#page=6|p. 6]], [[random_processes.pdf#page=7|7]]

![[random-processes-p7-realizzazioni.png]]
*Lo spazio campione $S$ contiene gli esiti $s_1, s_2, \dots, s_n$. Ogni esito, cioè ogni prova dell'esperimento, produce una forma d'onda $x_1(t), x_2(t), \dots, x_n(t)$ sull'intervallo $(-T, +T)$. Una linea verticale all'istante $t_k$ taglia tutte le forme d'onda nei valori $x_1(t_k), x_2(t_k), \dots, x_n(t_k)$: al variare dell'esito, sono i valori della variabile aleatoria $X(t_k)$.*

![[grafico-rp-realizzazioni.png]]
*🧩 Grafico mio (definizioni di p. 6; script in `output/grafici/`). Processo gaussiano a media nulla con autocorrelazione $e^{-|\tau|/\tau_c}$, $\tau_c = 0.5$. A sinistra cinque realizzazioni: fissato $t_0 = 6$, ognuna dà un numero (punto arancio). A destra i valori $X(t_0)$ di 5000 realizzazioni: il loro istogramma riproduce la pdf gaussiana $\mathcal{N}(0, 1)$. È la variabile aleatoria che si ottiene fissando il tempo.*

##### Caratterizzazione statistica completa · [[random_processes.pdf#page=8|p. 8]], [[random_processes.pdf#page=9|9]], [[random_processes.pdf#page=11|p. 11]]

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

##### Ampiezza discreta: la DF del processo di Bernoulli (appunti p.10) · [[random_processes.pdf#page=10|p. 10]], [[random_processes.pdf#page=11|11]]

La slide 6 dice che con ampiezza discreta conviene usare la DF e cita come esempio il processo di Bernoulli. Gli appunti di p.10 lo scrivono: «per processi aleatori discreti a tempo discreto utilizzo la DF».
- **DF del primo ordine:** $p_{X(n)}(x) \triangleq P(X(n) = x) = p^x\,q^{1-x}$, con $x \in \{0, 1\}$.
- **DF del secondo ordine:** $p_{X(n_1)X(n_2)}(x_1, x_2) \triangleq P(\{X(n_1) = x_1, X(n_2) = x_2\}) = p^{w(\mathbf{x})}\,q^{2 - w(\mathbf{x})}$. Qui $\mathbf{x} = (x_1, x_2)$ e $w(\mathbf{x})$ è il «numero di 1 contenuti nel vettore». L'ultima uguaglianza vale «supponendo che i lanci siano statisticamente indipendenti».

Passaggi e tabella dei quattro casi nella derivazione sopra.

> 🧩 Cosa modella: una sequenza di lanci di una moneta, uno per istante $n$. $X(n) = 1$ se il lancio $n$-esimo dà "successo" (probabilità $p$), 0 altrimenti. Fissato $n$, $X(n)$ è una v.a. di [[variabili-aleatorie-notevoli|Bernoulli]]: il processo è una successione di v.a. di Bernoulli indipendenti. Ha **ampiezza discreta** (solo 0 e 1) e **tempo discreto**, per questo si usa la DF invece di CDF e pdf.

![[random-processes-p10-appunti-processo-bernoulli.png]]
*Appunti a mano: le due DF, con le note in verde «numero di 1 contenuti nel vettore» su $w(\mathbf{x})$ e «supponendo che i lanci siano statisticamente indipendenti» sotto l'uguaglianza. Nella prima riga l'istante è scritto una volta $n$ e una volta $n_1$: è lo stesso.*

##### Processi a tempo discreto · [[random_processes.pdf#page=5|p. 5]], [[random_processes.pdf#page=45|p. 45]]

- Finora $X(t; \omega)$ con $t \in \mathbb{R}$: processi **a tempo continuo**. Se il tempo appartiene a $\mathbb{Z}$, il processo è **a tempo discreto** e si scrive $X(n; \omega)$. Gli appunti di p. 5 lo anticipano: $X(n, \omega)$ con $n \in \mathbb{Z}$. Un esempio è il processo di Bernoulli degli appunti di p.10.
- È una successione di variabili aleatorie $\{X(n)\}_{n \in \mathbb{Z}}$, omettendo $\omega$. Con $n \in \{0, 1, \dots, N-1\}$ si riduce a un **vettore aleatorio**.
- CDF, pdf e DF si definiscono come a tempo continuo, sostituendo formalmente $t$ con $n$.
- Media, correlazioni e covarianze: [[momenti-di-un-processo]]. Densità spettrale: [[densita-spettrale-di-potenza]].

> 💡 Connessione (🧩 mia): campionando un processo a tempo continuo negli istanti $nT_c$ si ottiene un processo a tempo discreto, $X(n) = X(nT_c)$. È la versione aleatoria del campionamento di [[teorema-del-campionamento]].

##### Processi complessi · [[random_processes.pdf#page=25|p. 25]]

Un processo complesso $Z(t) = X(t) + jY(t)$ si caratterizza completamente con la caratterizzazione **congiunta** delle parti reale e immaginaria. Media e autocorrelazione sono in [[momenti-di-un-processo]].

> 🎯 Esame: definire un processo aleatorio e spiegarne i due punti di vista (forme d'onda contro variabili aleatorie nel tempo); cosa si ottiene fissando $\omega$, $t$ o entrambi, anche sulla sinusoide a fase casuale; caratterizzazione completa e parziale; distribuzioni di ordine $k$ e loro coerenza (marginali); DF del processo di Bernoulli.

#### Perché importa

È il modello del corso per i segnali che non si possono prevedere: il rumore termico ([[sistema-comunicazione-digitale]]) e i segnali d'informazione. Tutte le prestazioni di un sistema di comunicazione, come probabilità d'errore e rapporto segnale-rumore, si calcolano modellando rumore e messaggio come processi aleatori.

#### Connessioni

- [[variabile-aleatoria]] — fissato $t$, il processo è una variabile aleatoria.
- [[coppie-di-variabili-aleatorie]] — le distribuzioni congiunte di ordine 2 sono quelle di una coppia di v.a.; le marginali danno la coerenza.
- [[momenti-di-un-processo]] — la caratterizzazione parziale.
- [[stazionarieta]] — quando le distribuzioni non dipendono dall'origine dei tempi.
- [[processo-gaussiano]] — il caso in cui media e covarianza bastano per la caratterizzazione completa.
- [[teorema-del-campionamento]] — dal processo a tempo continuo a quello a tempo discreto.
- [[variabili-aleatorie-notevoli]] — fissato $n$, il processo di Bernoulli è una v.a. di Bernoulli; la fase della sinusoide è uniforme.

#### Fonti · [[random_processes.pdf#page=2|p. 2]], [[random_processes.pdf#page=11|p. 11]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]]

- [[processi-aleatori]]

### Momenti di un processo aleatorio: media, correlazioni, covarianze · [[momenti-di-un-processo|pagina]]

#### Definizione · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]]

La **caratterizzazione statistica parziale** di un processo reale $X(t)$ usa i momenti del primo e del secondo ordine, invece di tutte le distribuzioni ([[processo-aleatorio]]):
- **media**: il valore atteso del campione all'istante $t$;
- **funzione di autocorrelazione** (*acf*): il valore atteso del prodotto di due campioni, agli istanti $t_1$ e $t_2$;
- **funzione di autocovarianza**: lo stesso, dopo aver tolto le medie.

Con due processi $X(t)$ e $Y(t)$ si definiscono allo stesso modo la **mutua correlazione** e la **mutua covarianza**.

#### Formule · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

| Formula | Significato |
|---|---|
| $\mu_X(t) = E[X(t)] = \int_{-\infty}^{+\infty} x\,f_{X(t)}(x)\,dx$ | media, eq. (3): usa la pdf del **primo** ordine |
| $R_{XX}(t_1, t_2) = E[X(t_1)X(t_2)] = \iint x_1 x_2\,f_{X(t_1),X(t_2)}(x_1, x_2)\,dx_1dx_2$ | autocorrelazione, eq. (4): usa la pdf del **secondo** ordine |
| $C_{XX}(t_1, t_2) = E\{[X(t_1) - \mu_X(t_1)][X(t_2) - \mu_X(t_2)]\} = R_{XX}(t_1, t_2) - \mu_X(t_1)\mu_X(t_2)$ | autocovarianza, eq. (5) |
| $R_{XY}(t, \tau) = E[X(t)\,Y(t - \tau)]$, $\ R_{YX}(t, \tau) = E[Y(t)\,X(t - \tau)]$ | mutue correlazioni, eq. (9) |
| $R_{XY}(\tau) = R_{YX}(-\tau)$ | simmetria (processi congiuntamente WSS) |
| $C_{XY}(t, \tau) = E\{[X(t) - \mu_X(t)][Y(t-\tau) - \mu_Y(t-\tau)]\}$ | mutua covarianza, eq. (10); la (11) è $C_{YX}$ |
| $\mu_Z(t) = \mu_X(t) + j\mu_Y(t)$ | media di un processo complesso, eq. (12) |
| $R_{ZZ}(t_1, t_2) = E[Z(t_1)Z^*(t_2)]$ | autocorrelazione di un processo complesso, eq. (13) |
| $\mu_X(n)$, $R_{XY}(n, k) = E[X(n)Y(k)]$, $C_{XY}(n,k) = R_{XY}(n,k) - \mu_X(n)\mu_Y(k)$ | versioni a tempo discreto, eq. (35)–(37) |

Simboli: $E[\cdot]$ = valore atteso; $f_{X(t)}$ = pdf del primo ordine, $f_{X(t_1),X(t_2)}$ = pdf del secondo ordine; $\tau$ = ritardo (*lag*) [s]; $Z^*$ = coniugato. Unità: $\mu$ come il segnale (es. V); $R$ e $C$ come il segnale al quadrato (es. V², cioè W su 1 Ω).

#### Derivazioni

##### Derivazione — Eq. (5): autocovarianza da media e autocorrelazione · [[random_processes.pdf#page=14|p. 14]]
**Fonte:** se si conoscono media e autocorrelazione, si ricava l'autocovarianza.
> 🧩 Passaggi miei. Scrivo $X_1 = X(t_1)$, $X_2 = X(t_2)$, $\mu_1 = \mu_X(t_1)$, $\mu_2 = \mu_X(t_2)$.

$$
\begin{aligned}
C_{XX}(t_1, t_2) &= E[(X_1 - \mu_1)(X_2 - \mu_2)] && \text{definizione} \\
&= E[X_1X_2] - \mu_2E[X_1] - \mu_1E[X_2] + \mu_1\mu_2 && \text{sviluppo e linearità di } E \text{ (} \mu_i \text{ sono costanti)} \\
&= R_{XX}(t_1, t_2) - \mu_1\mu_2 - \mu_1\mu_2 + \mu_1\mu_2 && E[X_i] = \mu_i \\
&= R_{XX}(t_1, t_2) - \mu_X(t_1)\,\mu_X(t_2)
\end{aligned}
$$
È la stessa relazione $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$ di [[correlazione-e-covarianza]], applicata a due campioni dello stesso processo. Allo stesso modo si ottiene la (37) a tempo discreto.

##### Derivazione — Simmetria delle mutue correlazioni: $R_{XY}(\tau) = R_{YX}(-\tau)$ · [[random_processes.pdf#page=22|p. 22]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
R_{YX}(t', -\tau) &= E[Y(t')\,X(t' + \tau)] && \text{definizione (9) con ritardo } -\tau \\
&= E[Y(t - \tau)\,X(t)] && \text{scelgo } t' = t - \tau \\
&= E[X(t)\,Y(t - \tau)] = R_{XY}(t, \tau) && \text{il prodotto commuta}
\end{aligned}
$$
Per processi **congiuntamente WSS** nessuna delle due dipende da $t$, quindi $R_{XY}(\tau) = R_{YX}(-\tau)$.
**Perché $R_{XY}$ non è pari:** scambiare $\tau$ con $-\tau$ equivale a scambiare i ruoli di $X$ e $Y$, e in generale le due funzioni sono diverse. Per lo stesso motivo non c'è garanzia di un massimo in $\tau = 0$: il massimo sta dove i due processi "si somigliano di più", che può essere un ritardo diverso da zero.

##### Derivazione — Mutua covarianza: casi particolari · [[random_processes.pdf#page=23|p. 23]]
> 🧩 Passaggi miei, con lo stesso sviluppo della (5):

$$
C_{XY}(t, \tau) = R_{XY}(t, \tau) - \mu_X(t)\,\mu_Y(t - \tau)
$$
- **media nulla** ($\mu_X = \mu_Y = 0$ per ogni $t$): $C_{XY}(t, \tau) = R_{XY}(t, \tau)$, e allo stesso modo $C_{YX} = R_{YX}$;
- **congiuntamente WSS**: le medie sono costanti e $R_{XY}$ dipende solo da $\tau$, quindi $C_{XY}(t, \tau) = R_{XY}(\tau) - \mu_X\mu_Y = C_{XY}(\tau)$.

##### Derivazione — Indipendenti ⇒ incorrelati; con media nulla, incoerenti ⇔ incorrelati · [[random_processes.pdf#page=24|p. 24]]
**Fonte:** «si può dimostrare».
> 🧩 Derivazione mia (stesso argomento di [[correlazione-e-covarianza]] per due v.a.)

$$
\begin{aligned}
R_{XY}(\tau) &= E[X(t)\,Y(t - \tau)] = E[X(t)]\,E[Y(t - \tau)] = \mu_X\,\mu_Y && \text{indipendenza: il valore atteso del prodotto si fattorizza} \\
C_{XY}(\tau) &= R_{XY}(\tau) - \mu_X\mu_Y = 0 && \text{quindi incorrelati}
\end{aligned}
$$
Con $\mu_X = \mu_Y = 0$ vale $C_{XY} = R_{XY}$: $R_{XY} \equiv 0$ (incoerenti) se e solo se $C_{XY} \equiv 0$ (incorrelati).
Il viceversa, incorrelati ⇒ indipendenti, in generale **non** vale: vale per i processi gaussiani ([[processo-gaussiano]]).

##### Derivazione — Momenti dell'esempio della slide 2 · [[random_processes.pdf#page=2|p. 2]]
> 🧩 Calcolo mio: la slide definisce il processo ma non ne calcola i momenti.

$$
\begin{aligned}
\mu_X(t) &= A\cdot q + (-A)\cdot p = A(1 - 2p) && 0 < t < T:\ X(t) = A \text{ con prob. } q,\ -A \text{ con prob. } p \\
\mu_X(t) &= 0 && \text{fuori da } (0, T):\ X(t) = 0 \\
R_{XX}(t_1, t_2) &= E[X(t_1)X(t_2)] = A^2 && t_1, t_2 \in (0, T):\ \text{stesso } \omega, \text{ stesso segno: il prodotto è sempre } A^2 \\
C_{XX}(t_1, t_2) &= A^2 - A^2(1 - 2p)^2 = 4p(1 - p)\,A^2 = 4pq\,A^2 && \text{eq. (5); } 1 - (1 - 2p)^2 = 4p - 4p^2
\end{aligned}
$$
Fuori da $(0, T)^2$ autocorrelazione e covarianza sono nulle.
**Sanity check:**
- con $p = 0$ o $p = 1$ il segnale è deterministico e $C_{XX} = 0$ ✓;
- con $p = 1/2$ la media è nulla e $C_{XX} = R_{XX} = A^2$ ✓.

**Lettura:** la media dipende da $t$ (vale $A(1 - 2p)$ dentro il rettangolo e 0 fuori), quindi il processo **non è stazionario** ([[stazionarieta]]). In generale $\mu_X(t)$ è funzione di $t$ e $R_{XX}$, $C_{XX}$ lo sono di $t_1$ e $t_2$ separatamente, come dicono le slide 7–9.

##### Derivazione — Momenti della sinusoide a fase casuale degli appunti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]], [[random_processes.pdf#page=12|p. 12]], [[random_processes.pdf#page=13|13]]
**Fonte:** appunti a mano di p. 4 e p. 5: $X(t) = A\cos(2\pi f_0 t + \Theta)$, con $A$, $f_0$ deterministiche e $\Theta \sim \mathcal{U}(0, 2\pi)$ (vedi [[processo-aleatorio]]).
> 🧩 Calcolo mio: gli appunti definiscono il processo ma non ne calcolano i momenti. Applico le definizioni (3) e (4). L'unica v.a. è $\Theta$, quindi i valori attesi sono integrali su $\vartheta$ pesati con $f_\Theta(\vartheta) = \frac{1}{2\pi}$ in $[0, 2\pi]$.

**Media:**
$$
\begin{aligned}
\mu_X(t) &= E[A\cos(2\pi f_0 t + \Theta)] = \int_0^{2\pi} A\cos(2\pi f_0 t + \vartheta)\,\frac{1}{2\pi}\,d\vartheta && \text{valore atteso di una funzione di } \Theta \\
&= \frac{A}{2\pi}\Big[\sin(2\pi f_0 t + \vartheta)\Big]_0^{2\pi} && \text{primitiva di } \cos \text{ in } \vartheta \text{ (} t \text{ è fisso)} \\
&= \frac{A}{2\pi}\big[\sin(2\pi f_0 t + 2\pi) - \sin(2\pi f_0 t)\big] = 0 && \sin \text{ ha periodo } 2\pi
\end{aligned}
$$

**Autocorrelazione**, con $t_1 = t$ e $t_2 = t - \tau$ come nella convenzione del ritardo:
$$
\begin{aligned}
R_{XX}(t_1, t_2) &= A^2\,E\big[\cos(2\pi f_0 t_1 + \Theta)\cos(2\pi f_0 t_2 + \Theta)\big] && \text{definizione (4); } A \text{ è deterministica} \\
&= \frac{A^2}{2}\,E\big[\cos(2\pi f_0 (t_1 - t_2)) + \cos(2\pi f_0 (t_1 + t_2) + 2\Theta)\big] && \cos a\cos b = \tfrac12[\cos(a - b) + \cos(a + b)] \\
&= \frac{A^2}{2}\cos(2\pi f_0 (t_1 - t_2)) + \frac{A^2}{2}\,E\big[\cos(2\pi f_0 (t_1 + t_2) + 2\Theta)\big] && \text{il primo termine non contiene } \Theta \\
&= \frac{A^2}{2}\cos(2\pi f_0 (t_1 - t_2)) && \text{il secondo valore atteso è nullo (sotto)} \\
&= \frac{A^2}{2}\cos(2\pi f_0 \tau) && t_1 - t_2 = \tau
\end{aligned}
$$
Il valore atteso che si annulla: con $\varphi = 2\pi f_0(t_1 + t_2)$,
$$E[\cos(\varphi + 2\Theta)] = \frac{1}{2\pi}\int_0^{2\pi}\cos(\varphi + 2\vartheta)\,d\vartheta = \frac{1}{2\pi}\Big[\frac{\sin(\varphi + 2\vartheta)}{2}\Big]_0^{2\pi} = \frac{\sin(\varphi + 4\pi) - \sin\varphi}{4\pi} = 0$$
Il coseno fa due periodi interi in $\vartheta \in [0, 2\pi]$ e la sua media è zero.

**Risultato:** $\mu_X = 0$ e $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$. Poiché la media è nulla, anche $C_{XX}(\tau) = R_{XX}(\tau)$, eq. (5).
**Sanity check:**
- $R_{XX}(0) = \frac{A^2}{2} = E[X^2(t)]$: è la potenza media di una sinusoide di ampiezza $A$, come nel caso deterministico ✓;
- $R_{XX}$ è pari e $|R_{XX}(\tau)| \le R_{XX}(0)$, come vogliono le proprietà di [[autocorrelazione-processi-wss]] ✓.

**Ipotesi:** fase **uniforme su un intero periodo**. È lei che fa sparire la dipendenza da $t$. Se $\Theta$ fosse, per esempio, uniforme solo in $(0, \pi)$, la stessa integrazione darebbe
$$\mu_X(t) = \frac{A}{\pi}\big[\sin(2\pi f_0 t + \pi) - \sin(2\pi f_0 t)\big] = -\frac{2A}{\pi}\sin(2\pi f_0 t)$$
che dipende da $t$: il processo non sarebbe più WSS.

**Lettura:** la media non dipende da $t$ e l'autocorrelazione dipende solo da $\tau = t_1 - t_2$. Il processo è quindi **WSS** ([[stazionarieta]]), all'opposto del rettangolo della slide 2. Ogni realizzazione è un coseno deterministico. È l'incertezza sulla fase, uguale per tutte le fasi, a rendere la statistica indipendente dall'origine dei tempi.

#### Spiegazione

##### Media, autocorrelazione, autocovarianza (slide 7–9) · [[random_processes.pdf#page=12|p. 12]]–[[random_processes.pdf#page=14|14]]

- La **media** di $X(t)$ è il valore atteso della v.a. ottenuta campionando il processo in $t$. Usa solo la pdf del **primo ordine** $f_{X(t)}$ e in generale è una funzione di $t$.
- L'**autocorrelazione** è il valore atteso del prodotto di due v.a., $X(t_1)$ e $X(t_2)$. Usa la pdf del **secondo ordine** e in generale dipende da $t_1$ e $t_2$ separatamente.
- L'**autocovarianza** è l'autocorrelazione dei processi "centrati" (media sottratta). Conoscendo media e autocorrelazione si ottiene con la (5).

> 💡 Connessione: per $t_1 = t_2 = t$ si ritrovano grandezze note di [[media-e-varianza]]. $R_{XX}(t, t) = E[X^2(t)]$ è il valore quadratico medio, e $C_{XX}(t, t) = \text{Var}[X(t)]$ la varianza del campione in $t$.

##### Mutue correlazioni e covarianze (slide 17–18) · [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=23|23]]

- Con due processi reali $X(t)$ e $Y(t)$, di autocorrelazioni $R_{XX}(t, \tau)$ e $R_{YY}(t, \tau)$, si definiscono le **mutue correlazioni** con ritardo, eq. (9). Dipendono dall'**ordine** dei due processi.
- $X(t)$ e $Y(t)$ sono **congiuntamente WSS** se ciascuno è WSS ([[stazionarieta]]) e in più $R_{XY}(t, \tau) \equiv R_{XY}(\tau)$.
- In generale la mutua correlazione **non è pari** in $\tau$, a differenza dell'autocorrelazione, e **non ha il massimo nell'origine**. Rispetta però $R_{XY}(\tau) = R_{YX}(-\tau)$.
- Le **mutue covarianze** (10)–(11) dipendono anch'esse dall'ordine; con media nulla coincidono con le mutue correlazioni; per processi congiuntamente WSS dipendono solo da $\tau$.

##### Indipendenti, incoerenti, incorrelati (slide 19) · [[random_processes.pdf#page=24|p. 24]]

| Proprietà | Definizione |
|---|---|
| **indipendenti** | gli insiemi $\{X(t_1), \dots, X(t_k)\}$ e $\{Y(t'_1), \dots, Y(t'_j)\}$ sono indipendenti per ogni $k, j \in \mathbb{N}$ e ogni scelta degli istanti |
| **incoerenti** | $R_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$ |
| **incorrelati** | $C_{XY}(\tau) = 0$ per ogni $\tau \in \mathbb{R}$ |

- Indipendenti ⇒ incorrelati.
- Se $\mu_X = \mu_Y = 0$, incoerenza e incorrelazione coincidono.

> 🧩 L'ordine di forza: *indipendenza* riguarda tutte le distribuzioni congiunte, *incorrelazione* solo i momenti del secondo ordine. È la stessa gerarchia tra v.a. di [[correlazione-e-covarianza]]. "Incoerenti" corrisponde a "ortogonali" per due v.a. ($E[XY] = 0$).

##### Processi complessi (slide 20) · [[random_processes.pdf#page=25|p. 25]]

- $Z(t) = X(t) + jY(t)$. La caratterizzazione completa di $Z$ richiede quella **congiunta** di parte reale e immaginaria.
- Caratterizzazione parziale: media (12) e autocorrelazione (13), con il **coniugato** sul secondo fattore. Si può scrivere come funzione di $(t_1, t_2)$ o di $(t, \tau)$: $R_{ZZ}(t, \tau) = E[Z(t)Z^*(t - \tau)]$.
- A rigore servirebbe anche un altro momento del secondo ordine, la **autocorrelazione coniugata** $R_{ZZ^*}(t_1, t_2) = E[Z(t_1)Z(t_2)]$, senza coniugato. Per la maggior parte dei processi però è nulla.

> 🧩 Perché il coniugato (osservazione mia): con $t_1 = t_2 = t$ si ottiene $E[Z(t)Z^*(t)] = E[|Z(t)|^2] \ge 0$, un numero reale che è la potenza istantanea media. Senza coniugato si otterrebbe $E[Z^2(t)]$, che in generale è complesso e non misura la potenza. È lo stesso motivo del coniugato nel prodotto scalare $\langle u, v\rangle = \int u v^*$ di [[inviluppo-complesso]].

##### Tempo discreto (slide 40–41) · [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

$$
\mu_X(n) \triangleq E[X(n)] = \int x\,f_{X(n)}(x)\,dx \tag{35}
$$
$$
R_{XY}(n, k) \triangleq E[X(n)Y(k)] = \iint x\,y\,f_{X(n),Y(k)}(x, y)\,dx\,dy \tag{36}
$$
$$
C_{XY}(n, k) \triangleq E\{[X(n) - \mu_X(n)][Y(k) - \mu_Y(k)]\} = R_{XY}(n, k) - \mu_X(n)\mu_Y(k) \tag{37}
$$
Con $X(n) \equiv Y(n)$ nella (36) e nella (37) si ottengono autocorrelazione e autocovarianza a tempo discreto.

> ⚠️ Refuso della slide: nella (36) la pdf è scritta $f_{X(n),Y(k)}(x, x)$; deve essere $(x, y)$.

> 🎯 Esame: definire media, autocorrelazione e autocovarianza e ricavare la (5); mutue correlazioni e loro simmetria; differenza tra processi indipendenti, incoerenti e incorrelati; perché nell'autocorrelazione di un processo complesso c'è il coniugato.

#### Perché importa

Media e autocorrelazione sono le grandezze con cui si lavora in pratica. Si propagano con formule semplici attraverso i filtri ([[processi-e-sistemi-lti]]); dall'autocorrelazione si ottiene la densità spettrale di potenza ([[densita-spettrale-di-potenza]]); per un processo gaussiano bastano da sole a dare la caratterizzazione completa ([[processo-gaussiano]]).

#### Connessioni

- [[processo-aleatorio]] — la caratterizzazione parziale sostituisce quella completa.
- [[media-e-varianza]], [[correlazione-e-covarianza]] — gli stessi momenti per una o due v.a.; qui applicati ai campioni del processo.
- [[stazionarieta]] — WSS: media costante e autocorrelazione dipendente solo da $\tau$. La sinusoide a fase casuale degli appunti è WSS, il rettangolo della slide 2 no.
- [[autocorrelazione-processi-wss]] — proprietà dell'autocorrelazione nel caso WSS.
- [[inviluppo-complesso]] — processi complessi in banda base, coniugato nel prodotto scalare.

#### Fonti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=5|5]], [[random_processes.pdf#page=12|p. 12]], [[random_processes.pdf#page=14|p. 14]], [[random_processes.pdf#page=22|p. 22]], [[random_processes.pdf#page=25|p. 25]], [[random_processes.pdf#page=45|p. 45]], [[random_processes.pdf#page=46|46]]

- [[processi-aleatori]]

### Stazionarietà dei processi aleatori · [[stazionarieta|pagina]]

#### Definizione · [[random_processes.pdf#page=15|p. 15]]–[[random_processes.pdf#page=18|18]]

In generale la caratterizzazione statistica di un processo $X(t)$ **cambia nel tempo**. Se le sue proprietà statistiche non dipendono, entro certi limiti, dalla scelta dell'**origine dei tempi**, il processo si dice **stazionario** in qualche senso. Ci sono diverse forme di stazionarietà.

Il confronto che le definisce:
- si considera il processo iniziato a $t = -\infty$ e lo si campiona negli istanti $t_1, \dots, t_k$, con CDF congiunta di ordine $k$ $F_{X(t_1),\dots,X(t_k)}$;
- si spostano tutti gli istanti della stessa quantità $\tau$ (traslazione nel tempo): $X(t_1 + \tau), \dots, X(t_k + \tau)$, con CDF $F_{X(t_1+\tau),\dots,X(t_k+\tau)}$.

$X(t)$ è **stazionario di ordine $k$** se
$$F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1,\dots,x_k) = F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_k) \tag{6}$$
per ogni traslazione $\tau$ e ogni scelta di $t_1, \dots, t_k$.

| Tipo | Condizione |
|---|---|
| **in senso stretto** (SSS, *strict-sense*) | la (6) vale per **ogni** $k \in \mathbb{N}$: la forma più forte |
| **del primo ordine** | la (6) vale per $k = 1$ |
| **del secondo ordine** | la (6) vale per $k = 2$ |
| **in senso lato** (WSS, *wide-sense*, o *debolmente stazionario*) | media costante e autocorrelazione che dipende solo dalla differenza tra i due istanti |

Spesso bastano forme più deboli della stazionarietà in senso stretto.

#### Formule · [[random_processes.pdf#page=16|p. 16]]–[[random_processes.pdf#page=18|18]]

| Formula | Significato |
|---|---|
| $F_{X(t)}(x) = F_{X(t+\tau)}(x) = F_{X(0)}(x)$ | primo ordine: la distribuzione non dipende da $t$ |
| $\mu_X(t) = \int x\,f_{X(0)}(x)\,dx \equiv \mu_X$ | primo ordine: media costante |
| $F_{X(t_1),X(t_2)}(x_1, x_2) = F_{X(t_1-t_2),X(0)}(x_1, x_2)$ | secondo ordine: dipende solo da $t_1 - t_2$ |
| $R_{XX}(t_1, t_2) \equiv R_{XX}(t_1 - t_2)$ | secondo ordine: autocorrelazione in funzione della differenza |
| SSS ⇒ WSS |  |

Simboli: $\tau$ = traslazione temporale [s]; $F$ = CDF congiunte ([[processo-aleatorio]]); $\mu_X$ = media; $R_{XX}$ = autocorrelazione ([[momenti-di-un-processo]]).

#### Derivazioni

##### Derivazione — Primo ordine: distribuzione e media non dipendono da $t$ · [[random_processes.pdf#page=16|p. 16]]
**Fonte:** «ponendo $\tau = -t$ risulta…».
> 🧩 Passaggi esplicitati da me

$$
\begin{aligned}
F_{X(t_1+\tau)}(x) &= F_{X(t_1)}(x) \quad \forall\,\tau, t_1 && \text{(6) con } k = 1 \\
F_{X(t)}(x) &= F_{X(t - t)}(x) = F_{X(0)}(x) && t_1 = t,\ \tau = -t \\
f_{X(t)}(x) &= f_{X(0)}(x) && \text{derivo in } x \\
\mu_X(t) &= \int x\,f_{X(t)}(x)\,dx = \int x\,f_{X(0)}(x)\,dx \equiv \mu_X && \text{la media non dipende da } t
\end{aligned}
$$
Si può confrontare ogni istante con l'istante 0: se tutti hanno la stessa distribuzione di $X(0)$, hanno tutti la stessa distribuzione.

##### Derivazione — Secondo ordine: conta solo la distanza tra gli istanti · [[random_processes.pdf#page=17|p. 17]]
**Fonte:** «ponendo $\tau = -t_2$ risulta…».
$$
\begin{aligned}
F_{X(t_1),X(t_2)}(x_1, x_2) &= F_{X(t_1+\tau),X(t_2+\tau)}(x_1, x_2) && \text{(6) con } k = 2 \\
&= F_{X(t_1-t_2),X(0)}(x_1, x_2) && \tau = -t_2 \\
R_{XX}(t_1, t_2) &= \iint x_1x_2\,f_{X(t_1-t_2),X(0)}(x_1, x_2)\,dx_1dx_2 \equiv R_{XX}(t_1 - t_2) && \text{la (4) con la pdf traslata}
\end{aligned}
$$
La distribuzione del secondo ordine dipende solo dalla **differenza** $t_1 - t_2$, non dagli istanti particolari in cui si campiona. Di conseguenza anche l'autocorrelazione.

##### Derivazione — Stazionario di ordine $k$ ⇒ stazionario di ordine $k-1$ · [[random_processes.pdf#page=17|p. 17]]
**Fonte:** affermato senza dimostrazione.
> 🧩 Derivazione mia, con la coerenza delle distribuzioni di [[processo-aleatorio]].

$$
\begin{aligned}
F_{X(t_1+\tau),\dots,X(t_{k-1}+\tau)}(x_1,\dots,x_{k-1}) &= F_{X(t_1+\tau),\dots,X(t_k+\tau)}(x_1,\dots,x_{k-1}, +\infty) && \text{marginale} \\
&= F_{X(t_1),\dots,X(t_k)}(x_1,\dots,x_{k-1}, +\infty) && \text{(6) di ordine } k \\
&= F_{X(t_1),\dots,X(t_{k-1})}(x_1,\dots,x_{k-1}) && \text{marginale}
\end{aligned}
$$
È la (6) di ordine $k-1$; ripetendo si scende a $k-2$, e così via. Il viceversa in generale **non** vale: l'invarianza delle marginali non dice nulla su come i campioni dipendono tra loro.

##### Derivazione — SSS ⇒ WSS · [[random_processes.pdf#page=18|p. 18]], [[random_processes.pdf#page=44|p. 44]]
**Fonte:** affermato senza dimostrazione.
> 🧩 Derivazione mia

- SSS vuol dire che la (6) vale per ogni $k$, in particolare per $k = 1$ e $k = 2$.
- Per $k = 1$, la media è costante: prima condizione WSS.
- Per $k = 2$, l'autocorrelazione dipende solo da $t_1 - t_2$: seconda condizione WSS.

**Ipotesi:** media e autocorrelazione devono esistere, cioè momenti di secondo ordine finiti.
**Il viceversa** in generale non vale: WSS impone condizioni solo su due momenti, non su tutte le distribuzioni. Fa eccezione il processo gaussiano, per cui WSS ⇒ SSS ([[processo-gaussiano]]).

#### Spiegazione

##### Come leggere la definizione · [[random_processes.pdf#page=4|p. 4]]
> 🧩 Spiegazione mia

- "Stazionario" vuol dire che **non si può capire che ore sono** guardando la statistica del processo. Un blocco di campioni preso adesso e lo stesso blocco preso fra un'ora hanno la stessa distribuzione.
- La stazionarietà riguarda la **statistica**, non le realizzazioni: le forme d'onda cambiano nel tempo anche quando il processo è stazionario (grafico delle realizzazioni in [[processo-aleatorio]]).
- **Esempio non stazionario:** il rettangolo di segno casuale della slide 2 ha media $A(1-2p)$ dentro $(0, T)$ e 0 fuori ([[momenti-di-un-processo]]): la media dipende da $t$.
- **Esempio stazionario:** il processo gaussiano con $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$ dei grafici ([[autocorrelazione-processi-wss]]) è WSS e, essendo gaussiano, anche SSS.
- **Esempio WSS dagli appunti:** la sinusoide a fase casuale $A\cos(2\pi f_0 t + \Theta)$, $\Theta \sim \mathcal{U}(0, 2\pi)$, ha media nulla e $R_{XX}(\tau) = \frac{A^2}{2}\cos(2\pi f_0\tau)$: calcolo in [[momenti-di-un-processo]]. Ogni realizzazione è un coseno deterministico, ma la statistica non dipende da $t$.

##### Scala delle stazionarietà · Processi [[random_processes.pdf#page=16|p. 16]], [[random_processes.pdf#page=18|p. 18]] · Campionamento [[Campionamento_AD_DA.pdf#page=34|p. 34]]

$$\text{SSS} \ \Rightarrow\ \dots \ \Rightarrow\ \text{ordine } 2 \ \Rightarrow\ \text{ordine } 1$$
$$\text{ordine } 2 \ \Rightarrow\ \text{WSS} \quad (\text{se esistono i momenti})$$

La WSS è la forma di stazionarietà usata nel resto della lezione: [[autocorrelazione-processi-wss]], [[densita-spettrale-di-potenza]], [[processi-e-sistemi-lti]].

> 💡 Connessione: il quantizzatore di Lloyd-Max suppone il segnale **stazionario del primo ordine** ([[quantizzazione-non-uniforme]]). Vuol dire che tutti i campioni $x(n)$ hanno la stessa pdf $f_X$, e quindi un solo quantizzatore progettato su $f_X$ va bene in ogni istante.

> 🎯 Esame: definire la stazionarietà di ordine $k$, SSS, del primo e del secondo ordine, WSS; ricavare che al primo ordine la media è costante e al secondo l'autocorrelazione dipende da $t_1 - t_2$; mostrare SSS ⇒ WSS e perché non vale il viceversa.

#### Perché importa

Senza stazionarietà media e autocorrelazione sono funzioni di uno o due istanti, difficili da maneggiare. Con la WSS l'autocorrelazione diventa funzione del solo ritardo $\tau$, e si può farne la trasformata di Fourier: la densità spettrale di potenza ([[densita-spettrale-di-potenza]]).

#### Connessioni

- [[processo-aleatorio]] — le distribuzioni congiunte di cui si chiede l'invarianza.
- [[momenti-di-un-processo]] — media e autocorrelazione nella definizione di WSS.
- [[autocorrelazione-processi-wss]] — proprietà dell'autocorrelazione quando il processo è WSS.
- [[processo-gaussiano]] — WSS ⇒ SSS.
- [[quantizzazione-non-uniforme]] — ipotesi di stazionarietà del primo ordine in Lloyd-Max.

#### Fonti · [[random_processes.pdf#page=4|p. 4]], [[random_processes.pdf#page=15|p. 15]], [[random_processes.pdf#page=18|p. 18]]

- [[processi-aleatori]]

### Autocorrelazione dei processi WSS · [[autocorrelazione-processi-wss|pagina]]

#### Definizione · [[random_processes.pdf#page=17|p. 17]], [[random_processes.pdf#page=19|p. 19]]

Per un processo WSS ([[stazionarieta]]) l'autocorrelazione dipende solo dalla distanza tra i due campioni, e si scrive in funzione del **ritardo** (*lag*) $\tau$:
$$R_{XX}(\tau) \triangleq E[X(t)\,X(t - \tau)], \qquad \forall\,\tau \in \mathbb{R} \tag{7}$$
detta **lag-acf**. $\tau$ è la distanza temporale tra i campioni negli istanti $t_1 = t$ e $t_2 = t_1 - \tau$.

**Autocorrelazione normalizzata:**
$$\rho_{XX}(\tau) \triangleq \frac{R_{XX}(\tau)}{R_{XX}(0)} \tag{8}$$
con valori confinati in $[-1, 1]$, cioè $|\rho_{XX}(\tau)| \le 1$.

> 🧩 Coerenza con la notazione a due istanti: con $t_1 = t$ e $t_2 = t - \tau$ si ha $\tau = t_1 - t_2$, quindi la (7) è la $R_{XX}(t_1 - t_2)$ della stazionarietà del secondo ordine.

#### Formule · [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=20|20]]

| Formula | Significato |
|---|---|
| $R_{XX}(\tau) = E[X(t)X(t-\tau)]$ | lag-acf, eq. (7) |
| $R_{XX}(0) = E[X^2(t)]$ | proprietà 1: valore quadratico medio |
| $R_{XX}(-\tau) = R_{XX}(\tau)$ | proprietà 2: funzione pari |
| $\|R_{XX}(\tau)\| \le R_{XX}(0)$ | proprietà 3: massimo in modulo in $\tau = 0$ |
| $\rho_{XX}(\tau) = R_{XX}(\tau)/R_{XX}(0)$, $\ \|\rho_{XX}\| \le 1$ | normalizzata, eq. (8) |
| $\|R_{XX}(\tau)\| <$ valore prescritto per $\tau > \tau_{dec}$ | tempo di decorrelazione |

Simboli: $\tau$ = ritardo [s]; $R_{XX}$ nell'unità del segnale al quadrato (es. V²); $\rho_{XX}$ adimensionale; $\tau_{dec}$ = tempo di decorrelazione [s].

> 🧮 Formula chiave: $R_{XX}(0) = E[X^2]$, $\ R_{XX}(-\tau) = R_{XX}(\tau)$, $\ |R_{XX}(\tau)| \le R_{XX}(0)$.

#### Derivazioni

##### Derivazione — Proprietà 1: $R_{XX}(0) = E[X^2(t)]$ · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** «ponendo $\tau = 0$ nella (7)».
$$R_{XX}(0) = E[X(t)\,X(t - 0)] = E[X^2(t)]$$
È il **valore quadratico medio**, lo stesso per ogni $t$ perché il processo è WSS. In [[densita-spettrale-di-potenza]] è la **potenza** del processo.

##### Derivazione — Proprietà 2: $R_{XX}$ è pari · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia

$$
\begin{aligned}
R_{XX}(-\tau) &= E[X(t)\,X(t + \tau)] && \text{(7) con ritardo } -\tau \\
&= E[X(t' - \tau)\,X(t')] && t' = t + \tau \text{: per un processo WSS il risultato non dipende dall'istante scelto} \\
&= E[X(t')\,X(t' - \tau)] = R_{XX}(\tau) && \text{il prodotto commuta}
\end{aligned}
$$
**In parole:** "il campione di adesso con quello di $\tau$ secondi fa" e "il campione di adesso con quello fra $\tau$ secondi" sono la stessa coppia vista dall'altro lato.

##### Derivazione — Proprietà 3: $|R_{XX}(\tau)| \le R_{XX}(0)$ · [[random_processes.pdf#page=19|p. 19]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Due dimostrazioni mie

**Con la disuguaglianza di Schwarz** ([[correlazione-e-covarianza]]):
$$
|R_{XX}(\tau)| = |E[X(t)X(t-\tau)]| \le \sqrt{E[X^2(t)]\,E[X^2(t-\tau)]} = \sqrt{R_{XX}(0)\,R_{XX}(0)} = R_{XX}(0)
$$
L'ultima uguaglianza usa la WSS: il valore quadratico medio è lo stesso in $t$ e in $t - \tau$.

**Con un quadrato non negativo:**
$$
\begin{aligned}
0 &\le E\big[\big(X(t) \pm X(t - \tau)\big)^2\big] && \text{valore atteso di un quadrato} \\
&= E[X^2(t)] \pm 2E[X(t)X(t-\tau)] + E[X^2(t-\tau)] && \text{sviluppo} \\
&= 2R_{XX}(0) \pm 2R_{XX}(\tau) && \text{proprietà 1 e (7)} \\
\Rightarrow\ -R_{XX}(0) &\le R_{XX}(\tau) \le R_{XX}(0) && \text{segno } + \text{ e segno } -
\end{aligned}
$$

##### Derivazione — $|\rho_{XX}(\tau)| \le 1$ · [[random_processes.pdf#page=19|p. 19]]
Si divide la proprietà 3 per $R_{XX}(0) > 0$: $|\rho_{XX}(\tau)| = |R_{XX}(\tau)|/R_{XX}(0) \le 1$.
> 🧩 Se il processo ha **media nulla**, $\rho_{XX}(\tau)$ è proprio il **coefficiente di correlazione** tra i campioni $X(t)$ e $X(t-\tau)$ ([[correlazione-e-covarianza]]): $\text{Cov} = R_{XX}(\tau)$ e $\sigma^2 = R_{XX}(0)$ per entrambi.

##### Derivazione — Tempo di decorrelazione dell'esempio esponenziale · [[random_processes.pdf#page=20|p. 20]]
**Fonte:** definizione di p. 20
> 🧩 Calcolo mio per il processo dei grafici, $R_{XX}(\tau) = e^{-|\tau|/\tau_c}$ con $R_{XX}(0) = 1$ e soglia $0.1\,R_{XX}(0)$.

$$
\begin{aligned}
e^{-\tau_{dec}/\tau_c} &= 0.1 && |R_{XX}| \text{ scende sotto la soglia per } \tau > \tau_{dec} \\
\tau_{dec} &= \tau_c\ln 10 \approx 2.30\,\tau_c && \text{logaritmo di entrambi i membri}
\end{aligned}
$$
**Numeri:** $\tau_c = 2 \Rightarrow \tau_{dec} \approx 4.61$; $\tau_c = 0.1 \Rightarrow \tau_{dec} \approx 0.23$ (valori segnati nel grafico sotto).
**Sanity check:** $\tau_{dec}$ è proporzionale a $\tau_c$. Un processo con correlazione che si esaurisce 20 volte più in fretta ha un tempo di decorrelazione 20 volte più corto ✓. Il valore dipende dalla soglia scelta, che la slide lascia libera.

#### Spiegazione

##### Significato fisico (slide 15–16) · [[random_processes.pdf#page=19|p. 19]]–[[random_processes.pdf#page=21|21]], [[random_processes.pdf#page=32|p. 32]]

- $R_{XX}(\tau)$ descrive quanto sono **legati tra loro** due campioni presi a $\tau$ secondi di distanza.
- Più il processo **cambia rapidamente** nel tempo, più rapidamente $R_{XX}(\tau)$ scende dal massimo $R_{XX}(0)$ al crescere di $\tau$.
- Questo comportamento si riassume nel **tempo di decorrelazione** $\tau_{dec}$: per $\tau > \tau_{dec}$ il modulo di $R_{XX}(\tau)$ resta sotto un valore prescritto.

![[random-processes-p21-autocorrelazione-lento-veloce.png]]
*autocorrelazione di un processo che fluttua lentamente (curva larga, che scende piano) e di uno che fluttua rapidamente (curva stretta attorno a $\tau = 0$). Entrambe hanno il massimo in $\tau = 0$ e sono pari.*

![[grafico-rp-lento-veloce.png]]
*🧩 Grafico mio (definizioni di p. 19, p. 20 e Wiener-Khinchin di p. 32). Due processi gaussiani WSS con la stessa potenza $R_{XX}(0) = 1$: lento ($\tau_c = 2$) e veloce ($\tau_c = 0.1$).*
- *In alto una realizzazione di ciascuno: il veloce cambia molto di più da un istante all'altro.*
- *Al centro le autocorrelazioni $e^{-|\tau|/\tau_c}$: quella del veloce crolla subito ($\tau_{dec} \approx 0.23$), quella del lento dopo molto ($\tau_{dec} \approx 4.61$).*
- *In basso le PSD, trasformate delle autocorrelazioni: il lento concentra la potenza vicino a $f = 0$, il veloce la spalma su una banda larga. L'area è la stessa, 1.*

##### Come si costruisce $R_{XX}(\tau)$ (animazione) · [[random_processes.pdf#page=19|p. 19]]
![[grafico-rp-autocorrelazione.gif]]
*🧩 Animazione mia della (7), con 600 realizzazioni del processo esponenziale ($\tau_c = 1$).*
- *In alto: si fissa $t = 6$ e si prende il campione a $t - \tau$, con $\tau$ che cresce da 0 a 4.*
- *In basso a sinistra: le 600 coppie $(X(t), X(t-\tau))$. Per $\tau = 0$ stanno sulla bisettrice; al crescere di $\tau$ la nuvola si allarga fino a diventare circolare, cioè i campioni non si "somigliano" più.*
- *In basso a destra: la media del prodotto su tutte le realizzazioni è la stima di $R_{XX}(\tau)$, che segue la curva teorica $e^{-\tau/\tau_c}$.*

*È la definizione (7) letta nel senso del [[processo-aleatorio|primo punto di vista]]: il valore atteso è una media **sull'insieme delle realizzazioni**, a istanti fissati.*

> 🎯 Esame: definire la lag-acf; dimostrare le tre proprietà (valore in 0, parità, massimo in 0); definire l'autocorrelazione normalizzata; spiegare il legame tra velocità di variazione del processo, larghezza di $R_{XX}$ e tempo di decorrelazione.

#### Perché importa

Dice quanto "memoria" ha un processo: per quanto tempo il suo valore attuale dà informazione su quello futuro. Attraverso la trasformata di Fourier diventa la densità spettrale di potenza ([[densita-spettrale-di-potenza]]): un'autocorrelazione stretta corrisponde a uno spettro largo, e viceversa.

#### Connessioni

- [[stazionarieta]] — la WSS permette di scrivere $R_{XX}$ in funzione del solo $\tau$.
- [[momenti-di-un-processo]] — la definizione generale $R_{XX}(t_1, t_2)$.
- [[correlazione-e-covarianza]] — Schwarz per la proprietà 3; $\rho_{XX}$ come coefficiente di correlazione.
- [[densita-spettrale-di-potenza]] — Wiener-Khinchin: $S_{XX} = \mathcal{F}[R_{XX}]$.
- [[processi-e-sistemi-lti]] — come si trasforma $R_{XX}$ attraverso un filtro.

#### Fonti · [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=21|p. 21]]

- [[processi-aleatori]]

### Processi aleatori attraverso sistemi LTI · [[processi-e-sistemi-lti|pagina]]

#### Definizione · [[random_processes.pdf#page=26|p. 26]]

Un processo $X(t)$ entra in un **filtro LTI deterministico** con risposta impulsiva $h(t)$; l'uscita $Y(t)$ è un altro processo aleatorio, dato dall'integrale di convoluzione:
$$Y(t) = \int_{-\infty}^{+\infty} h(\tau_1)\,X(t - \tau_1)\,d\tau_1$$
- In generale è **difficile** trovare la distribuzione di $Y(t)$, anche conoscendo quella di $X(t)$.
- In molti casi basta calcolare **media e autocorrelazione** di $Y(t)$ a partire da quelle di $X(t)$, supponendo $X(t)$ **WSS**.

Risultati principali (ingresso WSS):
$$\mu_Y = \mu_X\,H(0) \qquad R_{YY}(\tau) = R_{XX}(\tau) * h(\tau) * h(-\tau) \qquad S_{YY}(f) = S_{XX}(f)\,|H(f)|^2$$

![[random-processes-p26-filtro-lti.png]]
*$X(t)$ → filtro con risposta impulsiva $h(t)$ → $Y(t)$.*

#### Formule · [[random_processes.pdf#page=27|p. 27]]–[[random_processes.pdf#page=31|31]], [[random_processes.pdf#page=33|p. 33]]

| Formula | Significato |
|---|---|
| $\mu_Y(t) = E\big[\int h(\tau_1)X(t - \tau_1)\,d\tau_1\big]$ | media dell'uscita, eq. (14) |
| $\mu_Y(t) = \int h(\tau_1)\,\mu_X(t - \tau_1)\,d\tau_1 = \mu_X(t) * h(t)$ | eq. (15) |
| $\mu_Y = \mu_X\int h(\tau_1)\,d\tau_1 = \mu_X H(0)$ | ingresso WSS, eq. (16) |
| $R_{Y_1Y_2}(t_1, t_2) = \iint h_1(\tau_1)h_2(\tau_2)\,R_{X_1X_2}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1 d\tau_2$ | mutua correlazione delle uscite, eq. (17)–(18) |
| $R_{Y_1Y_2}(\tau) = \iint h_1(\tau_1)h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_1 d\tau_2$ | ingressi congiuntamente WSS, eq. (19) |
| $R_{Y_1Y_2}(\tau) = R_{X_1X_2}(\tau) * h_1(\tau) * h_2(-\tau) = R_{X_1X_2}(\tau) * r_{h_1h_2}(\tau)$ | eq. (20) |
| $R_{YY}(\tau) = R_{XX}(\tau) * h(\tau) * h(-\tau) = R_{XX}(\tau) * r_{hh}(\tau)$ | autocorrelazione dell'uscita |
| $R_{YX}(\tau) = R_{XX}(\tau) * h(\tau)$, $\ R_{XY}(\tau) = R_{XX}(\tau) * h(-\tau)$ | mutue correlazioni ingresso-uscita |
| $S_{YY}(f) = S_{XX}(f)\,\|H(f)\|^2$ | PSD dell'uscita, eq. (22) |

Simboli:
- $h(t)$ = risposta impulsiva [1/s]; $H(f) = \int h(t)e^{-j2\pi ft}dt$ = risposta in frequenza (adimensionale); $H(0)$ = risposta a frequenza zero;
- $r_{h_1h_2}(\tau) = h_1(\tau) * h_2(-\tau) = \int h_1(s)\,h_2(s - \tau)\,ds$ = mutua correlazione **deterministica** delle due risposte impulsive (🧩 la slide la usa senza definirla), e $r_{hh}$ l'autocorrelazione deterministica di $h$;
- $S_{XX}$, $S_{YY}$ = densità spettrali di potenza ([[densita-spettrale-di-potenza]]).

> 🧮 Formula chiave: $\mu_Y = \mu_X H(0)$ e $S_{YY}(f) = S_{XX}(f)\,|H(f)|^2$.

#### Derivazioni

##### Derivazione — Media dell'uscita, eq. (15) e (16) · [[random_processes.pdf#page=27|p. 27]], [[random_processes.pdf#page=28|28]]
$$
\begin{aligned}
\mu_Y(t) &= E\Big[\int h(\tau_1)\,X(t - \tau_1)\,d\tau_1\Big] && \text{definizione, eq. (14)} \\
&= \int h(\tau_1)\,E[X(t - \tau_1)]\,d\tau_1 && \text{scambio } E \text{ e integrale: } E[X(t)] \text{ finita, filtro stabile} \\
&= \int h(\tau_1)\,\mu_X(t - \tau_1)\,d\tau_1 = \mu_X(t) * h(t) && \text{definizione di convoluzione, eq. (15)} \\
&= \mu_X\int h(\tau_1)\,d\tau_1 && \text{ingresso WSS: } \mu_X(t) \equiv \mu_X \\
&= \mu_X\,H(0) && H(0) = \textstyle\int h(t)\,e^{-j2\pi\cdot 0\cdot t}dt = \int h(t)\,dt \quad \text{(16)}
\end{aligned}
$$
**Lettura:** la media è la componente "continua" (a frequenza zero) del processo, e il filtro la moltiplica per il suo guadagno a frequenza zero.

##### Derivazione — Mutua correlazione delle uscite, eq. (17)–(18) · [[random_processes.pdf#page=29|p. 29]]

Due sistemi LTI: $X_1 \to h_1 \to Y_1$ e $X_2 \to h_2 \to Y_2$.
![[random-processes-p29-due-sistemi-lti.png]]
*$x_1(\cdot) \to h_1(\cdot) \to y_1(\cdot)$ e $x_2(\cdot) \to h_2(\cdot) \to y_2(\cdot)$.*

$$
\begin{aligned}
R_{Y_1Y_2}(t_1, t_2) &= E\Big[\int h_1(\tau_1)X_1(t_1 - \tau_1)\,d\tau_1\int h_2(\tau_2)X_2(t_2 - \tau_2)\,d\tau_2\Big] && \text{uscite come convoluzioni, eq. (17)} \\
&= \iint h_1(\tau_1)\,h_2(\tau_2)\,E[X_1(t_1 - \tau_1)X_2(t_2 - \tau_2)]\,d\tau_1 d\tau_2 && \text{prodotto di integrali = integrale doppio; scambio } E \\
&= \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(t_1 - \tau_1,\ t_2 - \tau_2)\,d\tau_1 d\tau_2 && \text{definizione di mutua correlazione, eq. (18)}
\end{aligned}
$$

##### Derivazione — Ingressi congiuntamente WSS, eq. (19)–(20) · [[random_processes.pdf#page=30|p. 30]]
**Fonte:** il passaggio dalla (19) alla (20) è dato senza calcoli.
$$
\begin{aligned}
(t_1 - \tau_1) - (t_2 - \tau_2) &= \tau - \tau_1 + \tau_2 && \tau = t_1 - t_2;\ \text{per ingressi congiuntamente WSS conta solo la differenza} \\
R_{Y_1Y_2}(\tau) &= \iint h_1(\tau_1)\,h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_1 d\tau_2 && \text{eq. (19)}
\end{aligned}
$$
> 🧩 Passaggi miei dalla (19) alla (20), con $\tilde h_2(\tau) = h_2(-\tau)$:

$$
\begin{aligned}
\int h_2(\tau_2)\,R_{X_1X_2}(\tau - \tau_1 + \tau_2)\,d\tau_2 &= \int \tilde h_2(u)\,R_{X_1X_2}\big((\tau - \tau_1) - u\big)\,du && u = -\tau_2 \\
&= \big[R_{X_1X_2} * \tilde h_2\big](\tau - \tau_1) && \text{definizione di convoluzione} \\
R_{Y_1Y_2}(\tau) &= \int h_1(\tau_1)\,\big[R_{X_1X_2} * \tilde h_2\big](\tau - \tau_1)\,d\tau_1 && \text{integrale esterno} \\
&= R_{X_1X_2}(\tau) * h_2(-\tau) * h_1(\tau) = R_{X_1X_2}(\tau) * r_{h_1h_2}(\tau) && \text{la convoluzione è commutativa e associativa}
\end{aligned}
$$
Il risultato dipende **solo dal ritardo** $\tau$.

**LTI conserva l'incoerenza**: se gli ingressi sono incoerenti, $R_{X_1X_2} \equiv 0$, allora $R_{Y_1Y_2} = 0 * r_{h_1h_2} \equiv 0$ e anche le uscite sono incoerenti.

##### Derivazione — Autocorrelazione dell'uscita e mutue correlazioni ingresso-uscita · [[random_processes.pdf#page=31|p. 31]]
$$
\begin{aligned}
R_{YY}(t_1, t_2) &= \iint h(\tau_1)\,h(\tau_2)\,R_{XX}(t_1 - \tau_1, t_2 - \tau_2)\,d\tau_1 d\tau_2 && \text{(18) con } h_1 = h_2 = h,\ X_1 = X_2 = X \\
R_{YY}(\tau) &= R_{XX}(\tau) * h(\tau) * h(-\tau) = R_{XX}(\tau) * r_{hh}(\tau) && \text{(20) con ingresso WSS}
\end{aligned}
$$
Per le mutue correlazioni ingresso-uscita si usa la (20), facendo passare uno dei due rami per un filtro "identità" $\delta(t)$:
$$
\begin{aligned}
R_{YX}(\tau) &= R_{XX}(\tau) * h(\tau) * \delta(-\tau) = R_{XX}(\tau) * h(\tau) && Y_1 = Y,\ Y_2 = X,\ h_1 = h,\ h_2 = \delta \\
R_{XY}(\tau) &= R_{XX}(\tau) * \delta(\tau) * h(-\tau) = R_{XX}(\tau) * h(-\tau) && Y_1 = X,\ Y_2 = Y,\ h_1 = \delta,\ h_2 = h
\end{aligned}
$$
**Sanity check** (🧩): la simmetria $R_{XY}(\tau) = R_{YX}(-\tau)$ di [[momenti-di-un-processo]] vale. Infatti $R_{YX}(-\tau) = [R_{XX} * h](-\tau) = [R_{XX}(-\cdot) * h(-\cdot)](\tau) = R_{XX}(\tau) * h(-\tau)$, perché $R_{XX}$ è pari ✓.

##### Derivazione — Ingresso WSS ⇒ uscita WSS · [[random_processes.pdf#page=31|p. 31]]
**Fonte:** «se l'ingresso di un sistema LTI stabile è WSS, anche l'uscita è WSS».
> 🧩 Derivazione mia: le due condizioni della WSS ([[stazionarieta]]).

- **Media costante:** $\mu_Y = \mu_X H(0)$, eq. (16), non dipende da $t$.
- **Autocorrelazione funzione del solo ritardo:** $R_{YY}(\tau) = R_{XX}(\tau) * r_{hh}(\tau)$ dipende solo da $\tau$.

##### Derivazione — PSD dell'uscita, eq. (22) · [[random_processes.pdf#page=33|p. 33]]
**Fonte:** dalla relazione di Wiener-Khinchin e da $R_{YY} = R_{XX} * h(\tau) * h(-\tau)$.
$$
\begin{aligned}
S_{YY}(f) &= \mathcal{F}\big[R_{XX}(\tau) * h(\tau) * h(-\tau)\big] && \text{Wiener-Khinchin: } S_{YY} = \mathcal{F}[R_{YY}] \\
&= S_{XX}(f)\,H(f)\,H(-f) && \text{convoluzioni} \to \text{prodotti; riflessione: } h(-\tau) \to H(-f) \\
&= S_{XX}(f)\,H(f)\,H^*(f) = S_{XX}(f)\,|H(f)|^2 && h \text{ reale: } H(-f) = H^*(f) \text{ (simmetria hermitiana)}
\end{aligned}
$$
**In parole**: la PSD dell'uscita è la PSD dell'ingresso moltiplicata per il **modulo quadro** della risposta in frequenza. La fase del filtro non conta.
**Potenza in uscita** (🧩): $P_Y = R_{YY}(0) = \int S_{XX}(f)\,|H(f)|^2\,df$, per la (21) di [[densita-spettrale-di-potenza]].
**Sanity check** (🧩): se $\mu_X \neq 0$, $R_{XX}$ contiene la costante $\mu_X^2$ e quindi $S_{XX}$ la riga $\mu_X^2\,\delta(f)$. Nella (22) la riga diventa $\mu_X^2|H(0)|^2\delta(f)$, cioè una media in uscita $|\mu_Y| = |\mu_X H(0)|$, in accordo con la (16) ✓.

#### Spiegazione

> 🧩 Il quadro (lettura mia):
> - Un filtro deterministico non rende "più aleatorio" il processo: lo rimodella. La media viene moltiplicata per $H(0)$; lo spettro di potenza per $|H(f)|^2$, quindi il filtro esalta o attenua le componenti di potenza alle varie frequenze.
> - Nel tempo, l'autocorrelazione dell'uscita è quella d'ingresso "spalmata" da $r_{hh}$. Un filtro passa-basso stretto ha $h$ lunga, quindi $r_{hh}$ larga, quindi un'uscita più lenta: il tempo di decorrelazione aumenta ([[autocorrelazione-processi-wss]]).
> - Non si conosce invece la distribuzione di $Y$, salvo per un ingresso gaussiano: in quel caso l'uscita resta gaussiana ([[processo-gaussiano]]).

> 🎯 Esame: ricavare $\mu_Y = \mu_X H(0)$ con le ipotesi per scambiare media e integrale; ricavare la (18) e la (20); dire perché ingresso WSS dà uscita WSS; ricavare $S_{YY} = S_{XX}|H|^2$.

#### Perché importa

Ogni blocco lineare di un sistema di comunicazione (filtri di trasmissione e ricezione, canale LTI) agisce su segnali e rumori aleatori. Queste formule dicono come cambiano media, correlazione e spettro di potenza, cioè le quantità che determinano il rapporto segnale-rumore.

#### Connessioni

- [[autocorrelazione-processi-wss]] — $R_{XX}(\tau)$ in ingresso e $R_{YY}(\tau)$ in uscita.
- [[densita-spettrale-di-potenza]] — la (22) e il suo significato fisico (filtro a banda stretta).
- [[momenti-di-un-processo]] — mutue correlazioni e loro simmetria.
- [[stazionarieta]] — WSS in ingresso ⇒ WSS in uscita.
- [[processo-gaussiano]] — un processo gaussiano attraverso un filtro stabile resta gaussiano.
- [[equivalente-banda-base-dei-filtri]] — gli stessi filtri LTI, descritti in banda base.

#### Fonti · [[random_processes.pdf#page=26|p. 26]], [[random_processes.pdf#page=31|p. 31]], [[random_processes.pdf#page=33|p. 33]]

- [[processi-aleatori]]

### Densità spettrale di potenza (PSD) · [[densita-spettrale-di-potenza|pagina]]

#### Definizione · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]]

La **densità spettrale di potenza** (*power spectral density*, PSD) di un processo $X(t)$ è
$$S_{XX}(f) \triangleq \lim_{T\to+\infty}\frac{1}{2T}\,E\big[|X_T(f)|^2\big]$$
dove $X_T(f)$ è la trasformata di Fourier della versione **finestrata** del processo, $X_T(t) = X(t)\,\text{rect}[t/(2T)]$ (il processo tenuto solo per $|t| < T$).

**Relazione di Wiener-Khinchin**: per un processo **WSS** la PSD è la trasformata di Fourier dell'autocorrelazione,
$$S_{XX}(f) = \int_{-\infty}^{+\infty} R_{XX}(\tau)\,e^{-j2\pi f\tau}\,d\tau$$

**Potenza:**
$$E[X^2(t)] = R_{XX}(0) = \int_{-\infty}^{+\infty} S_{XX}(f)\,df = P_X \tag{21}$$
dove $P_X$ è la potenza del processo WSS. $S_{XX}(f)$ si misura in **watt per hertz** (W/Hz).

#### Formule · [[random_processes.pdf#page=32|p. 32]]–[[random_processes.pdf#page=34|34]], [[random_processes.pdf#page=36|p. 36]]–[[random_processes.pdf#page=38|38]], [[random_processes.pdf#page=40|p. 40]], [[random_processes.pdf#page=46|p. 46]]

| Formula | Significato |
|---|---|
| $S_{XX}(f) = \lim_{T\to\infty}\frac{1}{2T}E[\|X_T(f)\|^2]$ | definizione |
| $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ | Wiener-Khinchin (processi WSS) |
| $E[X^2] = R_{XX}(0) = \int S_{XX}(f)\,df = P_X$ | potenza, eq. (21) |
| $S_{YY}(f) = S_{XX}(f)\,\|H(f)\|^2$ | PSD dopo un filtro LTI, eq. (22) |
| $\Delta P_X \approx 2\Delta f\,S_{XX}(f)$ | potenza nella banda $2\Delta f$ attorno a $\pm f$ |
| $S_{XX}(0) = \int R_{XX}(\tau)\,d\tau$ | proprietà 1, eq. (23) |
| $E[X^2] = \int S_{XX}(f)\,df = R_{XX}(0)$ | proprietà 2, eq. (24) |
| $S_{XX}(f) \ge 0$ | proprietà 3 |
| $S_{XX}(-f) = S_{XX}(f)$ | proprietà 4 (processo reale) |
| $p_{XX}(f) = S_{XX}(f)\big/\int S_{XX}(f)\,df$ | proprietà 5, PSD normalizzata, eq. (25) |
| $S_{XY}(f) = \lim\frac{1}{2T}E[X_T(f)Y_T^*(f)] = \int R_{XY}(\tau)e^{-j2\pi f\tau}d\tau$ | densità spettrale mutua, eq. (26) |
| $S_{XY}(f) = S_{YX}(-f) = S_{YX}^*(f)$ | simmetria |
| $S_{ZZ} = S_{XX} + S_{XY} + S_{YX} + S_{YY}$ | PSD della somma $Z = X + Y$, eq. (29) |
| $S_{ZZ} = S_{XX} + S_{YY}$ | somma di processi incoerenti, eq. (30) |
| $S_{XX}(\nu) = \lim_{N\to\infty}\frac{1}{2N+1}E[\|X_N(\nu)\|^2]$ | PSD a tempo discreto |

Simboli: $f$ = frequenza [Hz]; $T$ = semi-durata della finestra [s]; $S_{XX}$ [W/Hz] (o V²/Hz); $P_X$ [W]; $\Delta f$ = banda del filtro [Hz]; $\nu$ = frequenza normalizzata del tempo discreto (adimensionale); $X_N(\nu)$ = trasformata di Fourier a tempo discreto (DTFT) della versione troncata di $X(n)$.

> 🧮 Formula chiave: $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ e $P_X = R_{XX}(0) = \int S_{XX}(f)\,df$.

#### Derivazioni

##### Derivazione — Relazione di Wiener-Khinchin · [[random_processes.pdf#page=32|p. 32]]
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

##### Derivazione — Eq. (21) e proprietà 1–2: potenza e valore in zero · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=36|p. 36]]
$$
\begin{aligned}
R_{XX}(\tau) &= \int S_{XX}(f)\,e^{j2\pi f\tau}\,df && \text{antitrasformata (Wiener-Khinchin letta al contrario)} \\
R_{XX}(0) &= \int S_{XX}(f)\,df && \tau = 0 \text{: area sotto la PSD, eq. (21) e (24)} \\
&= E[X^2(t)] = P_X && \text{proprietà 1 dell'autocorrelazione} \\
S_{XX}(0) &= \int R_{XX}(\tau)\,e^{0}\,d\tau = \int R_{XX}(\tau)\,d\tau && f = 0 \text{ in Wiener-Khinchin: area sotto l'autocorrelazione, eq. (23)}
\end{aligned}
$$

##### Derivazione — Proprietà 3: $S_{XX}(f) \ge 0$ · [[random_processes.pdf#page=36|p. 36]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia, dalla definizione: $\frac{1}{2T}E[|X_T(f)|^2]$ è il valore atteso di una quantità non negativa, diviso per $2T > 0$, quindi è $\ge 0$ per ogni $T$; lo resta al limite. In alternativa, con il significato fisico qui sotto: se $S_{XX}$ fosse negativa attorno a qualche $f$, un filtro stretto centrato lì misurerebbe una potenza negativa, il che è assurdo.

##### Derivazione — Proprietà 4: PSD pari per un processo reale · [[random_processes.pdf#page=37|p. 37]]
> 🧩 Derivazione mia

$$
\begin{aligned}
S_{XX}(-f) &= \int R_{XX}(\tau)\,e^{+j2\pi f\tau}\,d\tau && \text{Wiener-Khinchin in } -f \\
&= \int R_{XX}(-u)\,e^{-j2\pi fu}\,du && u = -\tau \\
&= \int R_{XX}(u)\,e^{-j2\pi fu}\,du = S_{XX}(f) && R_{XX} \text{ è pari (proprietà 2 dell'autocorrelazione)}
\end{aligned}
$$
Con lo stesso conto, $S_{XX}^*(f) = S_{XX}(-f) = S_{XX}(f)$ perché $R_{XX}$ è reale: la PSD di un processo reale è **reale e pari**.

##### Derivazione — Proprietà 5: la PSD normalizzata si comporta come una pdf · [[random_processes.pdf#page=37|p. 37]]
$p_{XX}(f) \ge 0$ per la proprietà 3, e $\int p_{XX}(f)\,df = \int S_{XX}\,df\big/\int S_{XX}\,df = 1$.
> 🧩 Lettura mia: $p_{XX}(f)$ dice come la potenza è **distribuita** in frequenza, come una pdf dice come la probabilità è distribuita sui valori.

##### Derivazione — Significato fisico: $\Delta P_X \approx 2\Delta f\,S_{XX}(f)$ · [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=35|35]]
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

##### Derivazione — Densità spettrali mutue: $S_{XY}(f) = S_{YX}(-f) = S_{YX}^*(f)$ · [[random_processes.pdf#page=38|p. 38]]
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

##### Derivazione — PSD di una somma, eq. (27)–(30) · [[random_processes.pdf#page=39|p. 39]], [[random_processes.pdf#page=40|40]]
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
> 🧩 Sanity check: nella (29) i due termini misti sommano a $S_{XY} + S_{XY}^* = 2\,\text{Re}\{S_{XY}\}$, reale, per la simmetria appena ricavata. Anche $S_{ZZ}$ è quindi reale ✓.

##### Esempio — Wiener-Khinchin sull'autocorrelazione esponenziale
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

##### PSD a tempo discreto · [[random_processes.pdf#page=46|p. 46]]
$$
S_{XY}(\nu) \triangleq \lim_{N\to+\infty}\frac{1}{2N+1}E\big[X_N(\nu)\,Y_N^*(\nu)\big] \qquad S_{XX}(\nu) \triangleq \lim_{N\to+\infty}\frac{1}{2N+1}E\big[|X_N(\nu)|^2\big]
$$
$X_N(\nu)$ e $Y_N(\nu)$ sono le trasformate di Fourier a tempo discreto delle versioni **troncate** di $X(n)$ e $Y(n)$; la seconda si ottiene dalla prima con $X(n) \equiv Y(n)$. Per Wiener-Khinchin, la PSD di un processo WSS a tempo discreto è la trasformata a tempo discreto della sua autocorrelazione $R_{XX}(m)$.
> 🧩 In formula, con la convenzione $X(\nu) = \sum_n x(n)\,e^{-j2\pi\nu n}$ che la slide non scrive: $S_{XX}(\nu) = \sum_{m=-\infty}^{+\infty} R_{XX}(m)\,e^{-j2\pi\nu m}$. Il $2N + 1$ al denominatore è il numero di campioni tra $-N$ e $N$, l'analogo della durata $2T$.

#### Spiegazione · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=38|p. 38]]

- La PSD dice **come la potenza del processo si distribuisce in frequenza**. La sua area è la potenza totale, (21).
- Il **significato fisico** viene dal filtro a banda stretta: un filtro ideale centrato in $f_c$, largo $\Delta f$, lascia passare una potenza $\approx 2\Delta f\,S_{XX}(f_c)$. Misurare la potenza all'uscita di filtri sempre più stretti è un modo di "misurare" la PSD.
- La **densità spettrale mutua** misura i legami **in frequenza** tra due processi.

> 🧩 Perché serve Wiener-Khinchin: la definizione con la finestra e il limite è concettuale ma scomoda da calcolare. Il teorema la riduce a una trasformata di Fourier dell'autocorrelazione, che spesso si calcola in poche righe (esempio sopra).

> 🎯 Esame: definire la PSD; enunciare e dimostrare Wiener-Khinchin; ricavare potenza e significato fisico ($2\Delta f\,S_{XX}$); dimostrare le proprietà 1–5; densità spettrale mutua e sua simmetria; PSD della somma di processi incoerenti.

#### Perché importa

È lo strumento per descrivere segnali e rumori aleatori **in frequenza**: quanta potenza cade nella banda di un filtro, di un canale, di un ricevitore. Con $S_{YY} = S_{XX}|H|^2$ ([[processi-e-sistemi-lti]]) permette di calcolare la potenza di rumore all'uscita di qualunque filtro. Dà anche la banda occupata da un segnale modulato ([[calcolo-densita-spettrale]]).

#### Connessioni

- [[autocorrelazione-processi-wss]] — Wiener-Khinchin: la PSD è la sua trasformata; larghezze inversamente proporzionali.
- [[processi-e-sistemi-lti]] — la (22) e la potenza all'uscita.
- [[momenti-di-un-processo]] — mutue correlazioni, incoerenza, simmetria $R_{XY}(\tau) = R_{YX}(-\tau)$.
- [[segnali-banda-base-e-passa-banda]] — la stessa idea di banda, ora per segnali aleatori (e la simmetria pari della PSD corrisponde a quella hermitiana degli spettri reali).
- [[calcolo-densita-spettrale]] — esercizio della slide 32: PSD di un segnale modulato linearmente.

#### Fonti · [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=34|p. 34]], [[random_processes.pdf#page=40|p. 40]], [[random_processes.pdf#page=46|p. 46]]

- [[processi-aleatori]]

### Processo gaussiano · [[processo-gaussiano|pagina]]

#### Definizione · [[random_processes.pdf#page=41|p. 41]], [[random_processes.pdf#page=42|42]]

Il **processo gaussiano** è il processo aleatorio più usato nello studio dei sistemi di comunicazione: ha molte applicazioni pratiche ed è matematicamente trattabile.

$X(t)$ è gaussiano se, campionandolo in $t_1, \dots, t_n$, le variabili aleatorie $X(t_1), \dots, X(t_n)$ sono **congiuntamente gaussiane per ogni $n$**. La loro pdf congiunta di ordine $n$ è determinata completamente da:
- le **medie** $\mu_{X(t_i)} = E[X(t_i)]$, per $i \in \{1, \dots, n\}$ — eq. (31);
- le **covarianze** $C_{XX}(t_k, t_i) = E\{[X(t_k) - \mu_{X(t_k)}][X(t_i) - \mu_{X(t_i)}]\}$, per $k, i \in \{1, \dots, n\}$ — eq. (32).

In forma matriciale, con il vettore aleatorio $\mathbf{X} = [X(t_1), \dots, X(t_n)]^T$ e un suo valore $\mathbf{x} = [x_1, \dots, x_n]^T$ ($^T$ = trasposto), la pdf **gaussiana multivariata** è
$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n\det(\boldsymbol{\Sigma})}}\;e^{-\frac12(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})} \tag{33}$$
- $\boldsymbol{\mu} = [\mu_{X(t_1)}, \dots, \mu_{X(t_n)}]^T$ è il **vettore delle medie**;
- $\boldsymbol{\Sigma}$ è la **matrice di covarianza**, con elemento $(k, i)$ pari a $\{\boldsymbol{\Sigma}\}_{k,i} = C_{XX}(t_k, t_i)$;
- $\boldsymbol{\Sigma}^{-1}$ è la sua inversa.

#### Formule · [[random_processes.pdf#page=41|p. 41]], [[random_processes.pdf#page=42|42]], [[random_processes.pdf#page=44|p. 44]]

| Formula | Significato |
|---|---|
| $\mu_{X(t_i)} = E[X(t_i)]$ | medie dei campioni, eq. (31) |
| $C_{XX}(t_k, t_i)$ | covarianze dei campioni, eq. (32) |
| $f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n\det\boldsymbol{\Sigma}}}e^{-\frac12(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})}$ | gaussiana multivariata, eq. (33) |
| $\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$, $\ \mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} \ge 0\ \forall\,\mathbf{u} \in \mathbb{R}^n$ | covarianza simmetrica e semidefinita positiva |
| $\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} > 0\ \forall\,\mathbf{u} \neq \mathbf{0}$ | caso non degenere: definita positiva, invertibile |
| $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \dots, \sigma_n^2) \Rightarrow f_{\mathbf{X}}(\mathbf{x}) = \prod_i f_{X(t_i)}(x_i)$ | incorrelati ⇒ indipendenti, eq. (34) |

Simboli: $n$ = numero di campioni; $\det$ = determinante; $\sigma_i^2$ = varianza di $X(t_i)$; $\mathbf{u}$ = vettore reale qualunque; $f_{\mathbf{X}}$ in [1/V$^n$].

#### Derivazioni

##### Derivazione — Con $n = 1$ si ritrova la gaussiana scalare · Processi [[random_processes.pdf#page=42|p. 42]] · Probabilità [[Probabilità.pdf#page=23|p. 23]]
**Fonte:** p. 42 per la (33); gaussiana scalare in [[variabile-aleatoria-gaussiana]].
> 🧩 Verifica mia

$$
\begin{aligned}
\boldsymbol{\Sigma} &= \sigma^2,\quad \det\boldsymbol{\Sigma} = \sigma^2,\quad \boldsymbol{\Sigma}^{-1} = 1/\sigma^2 && n = 1: \text{ la matrice è un numero} \\
f_X(x) &= \frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{(x - \mu)^2}{2\sigma^2}} && \text{sostituisco nella (33)}
\end{aligned}
$$
È la pdf gaussiana di una variabile ✓.

##### Derivazione — Due campioni: la gaussiana bivariata
> 🧩 Caso $n = 2$ scritto per esteso (usato nel grafico). Media nulla, varianze 1, coefficiente di correlazione $\rho$ ([[correlazione-e-covarianza]]).

$$
\begin{aligned}
\boldsymbol{\Sigma} &= \begin{pmatrix} 1 & \rho \\ \rho & 1\end{pmatrix},\quad \det\boldsymbol{\Sigma} = 1 - \rho^2,\quad \boldsymbol{\Sigma}^{-1} = \frac{1}{1 - \rho^2}\begin{pmatrix} 1 & -\rho \\ -\rho & 1\end{pmatrix} && \text{inversa di una } 2\times2 \\
\mathbf{x}^T\boldsymbol{\Sigma}^{-1}\mathbf{x} &= \frac{x_1^2 - 2\rho x_1x_2 + x_2^2}{1 - \rho^2} && \text{forma quadratica} \\
f(x_1, x_2) &= \frac{1}{2\pi\sqrt{1 - \rho^2}}\,e^{-\frac{x_1^2 - 2\rho x_1x_2 + x_2^2}{2(1 - \rho^2)}} && \text{(33) con } n = 2:\ \sqrt{(2\pi)^2} = 2\pi
\end{aligned}
$$
Le curve di livello sono ellissi; con $\rho = 0$ sono cerchi.

##### Derivazione — $\boldsymbol{\Sigma}$ è simmetrica e semidefinita positiva · [[random_processes.pdf#page=42|p. 42]]
**Fonte:** proprietà date senza dimostrazione.
> 🧩 Derivazione mia. Scrivo $\tilde X_k = X(t_k) - \mu_{X(t_k)}$.

$$
\begin{aligned}
\{\boldsymbol{\Sigma}\}_{k,i} &= E[\tilde X_k\tilde X_i] = E[\tilde X_i\tilde X_k] = \{\boldsymbol{\Sigma}\}_{i,k} && \text{il prodotto commuta: simmetrica} \\
\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} &= \sum_k\sum_i u_k\,u_i\,E[\tilde X_k\tilde X_i] && \text{prodotto matrice-vettore} \\
&= E\Big[\Big(\sum_k u_k\tilde X_k\Big)^2\Big] \ge 0 && \text{linearità di } E;\ \text{valore atteso di un quadrato}
\end{aligned}
$$
**Lettura:** $\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u}$ è la **varianza** della combinazione lineare $\sum_k u_k X(t_k)$, e una varianza non può essere negativa. Vale 0 solo se quella combinazione è (quasi certamente) costante. Il caso **non degenere**, $\boldsymbol{\Sigma}$ definita positiva e quindi invertibile, è quello in cui nessuna combinazione non banale dei campioni è costante. Serve perché la (33) contiene $\boldsymbol{\Sigma}^{-1}$ e $\det\boldsymbol{\Sigma}$ al denominatore.

##### Derivazione — Incorrelati ⇒ indipendenti, eq. (34) · [[random_processes.pdf#page=44|p. 44]]
$$
\begin{aligned}
\boldsymbol{\Sigma} &= \text{diag}(\sigma_1^2, \dots, \sigma_n^2) && C_{XX}(t_k, t_i) = 0 \text{ per } k \neq i \\
\det\boldsymbol{\Sigma} &= \prod_i \sigma_i^2,\qquad \boldsymbol{\Sigma}^{-1} = \text{diag}(1/\sigma_1^2, \dots, 1/\sigma_n^2) && \text{matrice diagonale} \\
(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu}) &= \sum_i \frac{(x_i - \mu_i)^2}{\sigma_i^2} && \text{spariscono i termini misti} \\
f_{\mathbf{X}}(\mathbf{x}) &= \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}}\,e^{-\frac{(x_i - \mu_i)^2}{2\sigma_i^2}} = \prod_{i=1}^n f_{X(t_i)}(x_i) && e^{\sum} = \prod e;\ \sqrt{(2\pi)^n\prod\sigma_i^2} = \prod\sqrt{2\pi\sigma_i^2}
\end{aligned}
$$
La pdf congiunta è il **prodotto** delle marginali, cioè i campioni sono **indipendenti** ([[coppie-di-variabili-aleatorie]]). Per variabili qualunque, invece, incorrelazione non implica indipendenza ([[correlazione-e-covarianza]]).

##### Derivazione — WSS ⇒ SSS per un processo gaussiano · [[random_processes.pdf#page=44|p. 44]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Derivazione mia

- La pdf di ordine $n$ (33) dipende **solo** da $\boldsymbol{\mu}$ e $\boldsymbol{\Sigma}$.
- Se il processo è WSS, la media è costante e la covarianza dipende solo dalla differenza tra gli istanti: $C_{XX}(t_k + \tau, t_i + \tau) = C_{XX}(t_k - t_i)$.
- Quindi i campioni traslati $X(t_1 + \tau), \dots, X(t_n + \tau)$ hanno gli stessi $\boldsymbol{\mu}$ e $\boldsymbol{\Sigma}$ di quelli originali, e quindi la stessa pdf. Questo per ogni $n$: è la (6) per ogni ordine, cioè SSS ([[stazionarieta]]).

Per un processo qualunque questo ragionamento non funziona: le distribuzioni di ordine superiore non sono determinate da media e covarianza.

##### Derivazione — Un filtro lineare stabile conserva la gaussianità · [[random_processes.pdf#page=44|p. 44]]
**Fonte:** proprietà data senza dimostrazione.
> 🧩 Idea della dimostrazione, non una dimostrazione completa. $Y(t) = \int h(\tau)X(t - \tau)\,d\tau \approx \sum_k h(\tau_k)X(t - \tau_k)\,\Delta\tau$: ogni campione dell'uscita è il limite di una **combinazione lineare** di campioni dell'ingresso.
> 📚 Fonte esterna (proprietà standard della gaussiana multivariata, per esempio nel testo di Madhow): combinazioni lineari di variabili congiuntamente gaussiane sono ancora congiuntamente gaussiane.
>
> Quindi i campioni $Y(t_1), \dots, Y(t_n)$ sono congiuntamente gaussiani. Le loro medie e covarianze si calcolano con [[processi-e-sistemi-lti]].

#### Spiegazione

##### Perché è così importante (slide 38) · [[random_processes.pdf#page=43|p. 43]]

- I processi prodotti da fenomeni fisici sono spesso tali che un **modello gaussiano** è adeguato, e gli esperimenti lo confermano.
- Il **teorema del limite centrale** dà la giustificazione matematica: la somma di molti contributi indipendenti tende a una gaussiana ([[variabile-aleatoria-gaussiana]]).
- Il processo gaussiano è molto frequente nei fenomeni fisici e facile da trattare matematicamente: per questo è centrale nello studio dei sistemi di comunicazione.

##### Proprietà (slide 39) · [[random_processes.pdf#page=42|p. 42]], [[random_processes.pdf#page=44|p. 44]]

1. Un processo gaussiano applicato a un **filtro lineare stabile** dà in uscita un processo ancora **gaussiano**.
2. Un processo gaussiano **WSS** (debolmente stazionario) è anche **stazionario in senso stretto**.
3. Se i campioni $X(t_1), \dots, X(t_n)$ sono **incorrelati**, cioè $C_{XX}(t_k, t_i) = 0$ per $k \neq i$, sono anche **statisticamente indipendenti**. La matrice di covarianza è diagonale e la pdf congiunta è il prodotto delle pdf dei singoli campioni, eq. (34).

> 🧩 In sintesi: per un processo gaussiano, **media e covarianza sono tutto**. La caratterizzazione parziale ([[momenti-di-un-processo]]) coincide con quella completa ([[processo-aleatorio]]), ed è per questo che le proprietà 2 e 3 valgono.

![[grafico-rp-gaussiana-bivariata.png]]
*🧩 Grafico mio (eq. (33) con $n = 2$ e (34)). Curve di livello della pdf congiunta di due campioni $X(t_1)$, $X(t_2)$ a media nulla e varianza 1, con 400 coppie estratte.*
- *A sinistra $\rho = 0$: cerchi, e la pdf è il prodotto delle marginali. Incorrelati quindi indipendenti.*
- *A destra $\rho = 0.8$: ellissi inclinate lungo la bisettrice, cioè i due campioni tendono ad avere lo stesso segno.*

*Col processo esponenziale degli altri grafici ($R_{XX}(\tau) = e^{-|\tau|/\tau_c}$), $\rho = 0.8$ corrisponde a due campioni distanti $|t_1 - t_2| = \tau_c\ln(1/0.8) \approx 0.22\,\tau_c$.*

> 🎯 Esame: definire il processo gaussiano; scrivere la (33) e spiegarne i simboli; perché $\boldsymbol{\Sigma}$ è simmetrica e semidefinita positiva; dimostrare le proprietà (WSS ⇒ SSS, incorrelazione ⇒ indipendenza); perché il modello gaussiano è così usato.

#### Perché importa

Il rumore termico nei ricevitori si modella come processo gaussiano ([[variabile-aleatoria-gaussiana]], [[sistema-comunicazione-digitale]]). Il processo gaussiano ha tre vantaggi:
- resta gaussiano attraverso i filtri;
- è descritto completamente da media e autocorrelazione;
- ha campioni incorrelati che sono indipendenti.

Per questo le prestazioni dei sistemi, come la probabilità d'errore con la funzione $Q$, si calcolano in forma chiusa.

#### Connessioni

- [[variabile-aleatoria-gaussiana]] — il caso $n = 1$; CLT; funzione $Q$.
- [[momenti-di-un-processo]] — media e covarianza, che qui bastano a tutto.
- [[stazionarieta]] — WSS ⇒ SSS solo per i gaussiani.
- [[correlazione-e-covarianza]] e [[coppie-di-variabili-aleatorie]] — incorrelazione, indipendenza, pdf congiunta come prodotto.
- [[processi-e-sistemi-lti]] — medie e correlazioni dell'uscita gaussiana.

#### Fonti · [[random_processes.pdf#page=41|p. 41]], [[random_processes.pdf#page=44|p. 44]]

- [[processi-aleatori]]

### Calcolo della densità spettrale di potenza · [[calcolo-densita-spettrale|pagina]]

#### Metodo

1. **Scrivere il modello** del processo e le ipotesi statistiche (medie, correlazioni dei simboli, eventuali ritardi casuali).
2. **Verificare che sia WSS** ([[stazionarieta]]): media costante e $R_{XX}(t, \tau)$ indipendente da $t$. Se non lo è, bisogna prima renderlo WSS, per esempio con un ritardo casuale, altrimenti Wiener-Khinchin così come enunciato non si applica.
3. **Calcolare l'autocorrelazione** $R_{XX}(\tau) = E[X(t)X(t - \tau)]$ ([[autocorrelazione-processi-wss]]), usando linearità del valore atteso e indipendenza tra le variabili in gioco.
4. **Trasformare**: $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ ([[densita-spettrale-di-potenza]]).
5. **Controllare** con le proprietà: $S_{XX} \ge 0$, pari, $\int S_{XX}\,df = R_{XX}(0)$ (potenza), $S_{XX}(0) = \int R_{XX}\,d\tau$.

#### Formule usate · Processi [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=32|p. 32]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]]

- $R_{XX}(\tau) = E[X(t)X(t-\tau)]$ — [[autocorrelazione-processi-wss]]
- Wiener-Khinchin $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ e potenza $P_X = R_{XX}(0) = \int S_{XX}\,df$ — [[densita-spettrale-di-potenza]]
- Modulazione lineare $s(t) = \sum_n b[n]\,p(t - nT)$ — [[modulazione-digitale]]
- Spettro dell'impulso rettangolare $P(f) = T\,\text{sinc}(fT)$ — [[modulazione-digitale]]

#### Casi svolti

##### Caso 1 — PSD di un segnale modulato linearmente · Processi [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=37|p. 37]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]]
**Traccia**: «Example — Compute power spectral density of a linearly modulated signal.» La slide non dà lo svolgimento.
> 🧩 Svolgimento mio. Il modello viene dalla modulazione lineare della lezione precedente; le ipotesi statistiche sono mie, perché la slide non le specifica.

**Modello:**
$$X(t) = \sum_{n=-\infty}^{+\infty} b[n]\,p(t - nT - D)$$

**Ipotesi:**
- **(H1)** i simboli $b[n]$ hanno media nulla, sono incorrelati e hanno la stessa varianza: $E[b[n]] = 0$ e $E[b[n]\,b[m]] = \sigma_b^2\,\delta[n - m]$. Per esempio simboli $\pm A$ equiprobabili, con $\sigma_b^2 = A^2$.
- **(H2)** $D$ è un ritardo casuale uniforme in $[0, T)$, indipendente dai simboli. Modella il fatto che chi osserva il segnale non conosce l'istante in cui inizia ogni simbolo.
- **(H3)** $p(t)$ è un impulso reale di energia finita $E_p = \int p^2(t)\,dt$.

**Passo 1 — Media.**
$$
\mu_X(t) = \sum_n E[b[n]]\;E[p(t - nT - D)] = 0 \qquad \text{(H2): simboli e ritardo indipendenti; (H1): } E[b[n]] = 0
$$

**Passo 2 — Autocorrelazione.**
$$
\begin{aligned}
R_{XX}(t, \tau) &= E[X(t)\,X(t - \tau)] = \sum_n\sum_m E[b[n]b[m]]\;E\big[p(t - nT - D)\,p(t - \tau - mT - D)\big] && \text{sviluppo il prodotto delle somme; (H2)} \\
&= \sigma_b^2\sum_n E\big[p(t - nT - D)\,p(t - \tau - nT - D)\big] && \text{(H1): restano solo i termini } m = n \\
&= \sigma_b^2\sum_n \frac1T\int_0^T p(t - nT - d)\,p(t - \tau - nT - d)\,dd && D \text{ uniforme in } [0, T):\ \text{pdf } 1/T \\
&= \frac{\sigma_b^2}{T}\sum_n \int_{t-(n+1)T}^{t-nT} p(u)\,p(u - \tau)\,du && u = t - nT - d \\
&= \frac{\sigma_b^2}{T}\int_{-\infty}^{+\infty} p(u)\,p(u - \tau)\,du = \frac{\sigma_b^2}{T}\,r_{pp}(\tau) && \text{gli intervalli, al variare di } n, \text{ ricoprono } \mathbb{R} \text{ una volta sola}
\end{aligned}
$$
$r_{pp}(\tau) = p(\tau) * p(-\tau)$ è l'autocorrelazione deterministica dell'impulso (la stessa $r_{hh}$ di [[processi-e-sistemi-lti]]). Il risultato **non dipende da $t$**, e la media è costante: il processo è **WSS**.

**Passo 3 — PSD (Wiener-Khinchin).**
$$
\begin{aligned}
S_{XX}(f) &= \frac{\sigma_b^2}{T}\,\mathcal{F}\big[p(\tau) * p(-\tau)\big] = \frac{\sigma_b^2}{T}\,P(f)\,P(-f) && \text{convoluzione} \to \text{prodotto; riflessione} \\
&= \frac{\sigma_b^2}{T}\,|P(f)|^2 && p \text{ reale: } P(-f) = P^*(f)
\end{aligned}
$$
> 🧮 Risultato: $S_{XX}(f) = \dfrac{\sigma_b^2}{T}\,|P(f)|^2$. La **forma** dello spettro la decide l'impulso, il **livello** la varianza dei simboli per simbolo al secondo ($1/T$).

**Passo 4 — Impulso rettangolare**, come nell'esempio della modulazione binaria: $p(t) = \text{rect}\big((t - T/2)/T\big)$, altezza 1 e durata $T$.
$$
\begin{aligned}
|P(f)|^2 &= T^2\,\text{sinc}^2(fT) && \text{impulso centrato: } T\,\text{sinc}(fT) \text{ (modulazione-digitale); il ritardo } T/2 \text{ aggiunge } e^{-j\pi fT}, \text{ di modulo 1} \\
S_{XX}(f) &= \sigma_b^2\,T\,\text{sinc}^2(fT) && \text{sostituisco} \\
R_{XX}(\tau) &= \sigma_b^2\Big(1 - \frac{|\tau|}{T}\Big)\ \text{per } |\tau| < T,\ 0 \text{ altrove} && r_{pp}(\tau) = T - |\tau|: \text{ sovrapposizione di due rettangoli sfasati di } \tau
\end{aligned}
$$

**Verifiche:**
- **Potenza:** $R_{XX}(0) = \sigma_b^2$, cioè simboli di varianza $\sigma_b^2$ sempre "accesi". E $\int \sigma_b^2 T\,\text{sinc}^2(fT)\,df = \sigma_b^2 T\cdot\frac{1}{T} = \sigma_b^2$ ✓ (proprietà 2).
- **Valore in zero:** $S_{XX}(0) = \sigma_b^2 T$ = area del triangolo $R_{XX}$ (altezza $\sigma_b^2$, base $2T$) ✓ (proprietà 1).
- $S_{XX} \ge 0$ e pari ✓ (proprietà 3–4).
- **Zeri** in $f = k/T$, $k \neq 0$: il lobo principale è largo $2/T$. Raddoppiando la velocità di simbolo $1/T$ raddoppia la banda occupata.

**Risultato:** $S_{XX}(f) = \sigma_b^2\,T\,\text{sinc}^2(fT)$ [W/Hz se $\sigma_b^2$ è in W]. Con simboli $\pm A$ equiprobabili: $A^2 T\,\text{sinc}^2(fT)$.

> 💡 Connessione: la PSD decresce solo come $1/f^2$ lontano dall'origine, perché l'impulso rettangolare **non è a banda limitata** ([[modulazione-digitale]]). È il motivo per cui la slide 2 della lezione sulla banda base dice che le forme d'onda reali sono spesso vincolate in frequenza.

> 🧩 Perché serve il ritardo $D$: senza $D$, $R_{XX}(t, \tau) = \sigma_b^2\sum_n p(t - nT)\,p(t - \tau - nT)$ dipende da $t$, in modo periodico con periodo $T$. Il processo non sarebbe WSS e non si potrebbe applicare Wiener-Khinchin come enunciato a p. 32. Mediare su $D$ uniforme equivale a mediare $R_{XX}(t, \tau)$ su un periodo in $t$, e dà lo stesso risultato.

#### Trappole

- **Non verificare la WSS**: senza ritardo casuale (o media su un periodo) l'autocorrelazione dipende da $t$.
- **$|P(f)|^2$, non $P(f)$**: la PSD è reale e non negativa, e la fase dell'impulso sparisce.
- **Il fattore $1/T$**: la PSD è potenza per unità di frequenza; con simboli più frequenti c'è più energia al secondo.
- **Media nulla dei simboli (H1)**: con simboli $\pm A$ **non** equiprobabili la media non è nulla e la derivazione non vale così com'è ($E[b[n]b[m]] \neq 0$ per $n \neq m$).
- **Banda e primo zero**: il lobo principale va da $-1/T$ a $1/T$. Dire che "la banda è $1/T$" è una convenzione, perché lo spettro non si annulla mai del tutto.


---

## Lezione 6 — Laboratorio Matlab: conversione A/D e D/A (28/09)

### Lab 0 — Simulare il "tempo continuo" e calcolare lo spettro · [[lab-setup-e-spettro|pagina]]

> ⚠️ Non materia d'esame: serve a capire cosa fa lo script [[AD_conversion.m]] prima di campionare. Fonte: [[laboratorio-conversione-ad]].

#### Il problema

Un computer non può memorizzare un segnale a tempo continuo: conosce solo numeri, uno dopo l'altro. Per "vedere" il campionamento bisogna quindi fingere di avere un segnale continuo. Il trucco dello script: usare una griglia di tempi **molto più fitta** di quella di campionamento. Rispetto al campionamento vero ($T_s \approx 0.5$ s) la griglia con passo 6 ms si comporta come il continuo.

#### Cosa fa il codice · [[AD_conversion.m]] righe 5–13

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

##### Esempio 1: il trapezio (righe 21–35)

Il segnale vale 0 fino a $-2$, sale linearmente fino a 1 in $t = -1$, resta a 1 fino a $t = 1$, scende a 0 in $t = 2$. Il codice lo costruisce concatenando pezzi: zeri, rampa $t + 2$, uni, rampa $-t + 2$, zeri. `W = 1` è la banda "dichiarata" in Hz.

##### Esempio 2: tre sinusoidi (righe 44–48)

$$s(t) = 5\sin(2\pi\,4t + \tfrac{\pi}{5}) + 3\sin(2\pi\,\tfrac43 t + \tfrac{\pi}{8}) + 2\sin(2\pi\,0.4t - \tfrac{\pi}{3})$$
Frequenze 4 Hz, 1.33 Hz, 0.4 Hz; `W = 4` Hz, la più alta. Qui la banda è davvero limitata. Cosa succede campionandolo: [[lab-campionamento]].

##### Lo spettro (righe 79–85)

```matlab
S_dft = fftshift(fft(s));          % DFT, con la frequenza zero al centro
S     = dt*S_dft;                  % scala: approssima l'integrale di Fourier
f     = linspace(-0.5,0.5,N)/dt;   % asse delle frequenze in Hz
```

#### Cosa succede davvero

##### Perché `dt*fft` è la trasformata di Fourier
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

##### Lo spettro esatto del trapezio · [[Figure_1.png]]
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
*Figura del laboratorio, esempio 1. In alto il trapezio su $[-3, 3]$ s. Al centro lo spettro su tutto l'asse $\pm 83$ Hz: tutto concentrato attorno a 0, picco 3. In basso i campioni su tutta la finestra $[-30, 30]$ s: 121 aste, quasi tutte nulle, con i valori 0.5 e 1 attorno all'origine.*

#### Dubbi chiariti

- **"Ma il segnale è continuo o no?"** No: è un vettore di $10^4$ numeri. Si comporta come continuo perché $dt = 6$ ms è 83 volte più piccolo di $T_s$. Tra un campione e l'altro ci sono 82 punti "continui" che il campionamento butterà via.
- **"Perché la finestra è così lunga (60 s) se il trapezio dura 4 s?"** Per avere molta risoluzione in frequenza ($1/60$ Hz) e spazio per le code della sinc ([[lab-interpolazione]]). Ha però un effetto collaterale sull'SNR: [[lab-snr]].

#### Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=8|p. 8]]

- La domanda di p. 8 ([[teorema-del-campionamento]]), cioè come scegliere $f_c$ per un dato segnale, parte proprio dallo spettro: qui lo si calcola per poter scegliere $f_s = 2W$.
- Nelle slide la frequenza di campionamento si chiama $f_c$ e il periodo $T_c$; nel codice `fs` e `Ts`.

### Lab 1 — Campionamento · [[lab-campionamento|pagina]]

> ⚠️ Non materia d'esame: serve a vedere il [[teorema-del-campionamento]] all'opera. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-setup-e-spettro]].

#### Cosa fa il codice · [[AD_conversion.m]] righe 87–101

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

#### Cosa succede davvero

##### Il vettore `s_samp` è $x_\delta(t)$ · [[Campionamento_AD_DA.pdf#page=11|p. 11]]
Nelle slide il campionamento ideale è $x_\delta(t) = \sum_n x_a(nT_c)\,\delta(t - nT_c)$ ([[teorema-del-campionamento]]): un treno di impulsi pesati dai campioni, nullo tra un impulso e l'altro. `s_samp` è la sua versione simulata:
- è nullo tra un campione e l'altro;
- negli istanti $nT_s$ vale il campione.

> 🧩 Differenza (mia): la $\delta$ ha area 1, mentre nel vettore un punto isolato vale $s(nT_s)$ ma "occupa" solo $dt$. Il codice non corregge questa scala, e non serve: nell'interpolazione il filtro $h$ ha picco 1, quindi la convoluzione restituisce direttamente $\sum_n s(nT_s)\,h(t - nT_s)$ ([[lab-interpolazione]]).

##### I numeri dell'esempio 1
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

##### Cosa succede allo spettro · [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]
Campionare nel tempo **replica** lo spettro ogni $f_s$:
$$X_\delta(f) = \frac{1}{T_s}\sum_k S\Big(f - \frac{k}{T_s}\Big)$$
Le repliche sono distanti $f_{samp} = 2.008$ Hz, e la centrale occupa in teoria tutto l'asse, perché il trapezio non è a banda limitata. Le code delle repliche vicine entrano quindi nella banda $|f| < f_s/2$: è l'**aliasing** ([[aliasing]]). Qui è piccolo, perché oltre 1 Hz c'è solo lo 0.05% dell'energia ([[lab-setup-e-spettro]]).

![[grafico-lab-campionamento-spettro.png]]
*🧩 Grafico mio (replica dello script).*
- *In alto: il trapezio (grigio) e i campioni `s_samp` (aste blu) ogni $T_s = 0.498$ s.*
- *In basso: il modulo della trasformata dei campioni, moltiplicata per $T_s$ (blu), e le singole repliche $S(f)$, $S(f \mp f_s)$ (tratteggiate). La trasformata dei campioni è la somma delle repliche. Nella fascia azzurra $|f| < f_s/2 = 1.004$ Hz la replica centrale è quasi pulita: le code delle vicine valgono pochi centesimi.*

> 🧩 Il commento della riga 88 dice che con $W = 1$ «è come se avessimo applicato un filtro anti-aliasing». Va letto così: **nessun filtro** viene applicato, ma il segnale ha già quasi tutta l'energia sotto 1 Hz. Il risultato somiglia a quello che darebbe un filtro antialiasing. L'aliasing c'è, ma è trascurabile.

##### Esempio 2: quando l'arrotondamento rompe il teorema · [[Campionamento_AD_DA.pdf#page=13|p. 13]]
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

> 🧩 Anche senza arrotondamento, $f_s = 2W$ esatto è il **caso limite** (b) di p. 13: le repliche si toccano in $f_s/2$. Una sinusoide proprio a $f_s/2$ viene campionata sempre nella stessa fase, a meno del segno, e la sua ampiezza non si ricostruisce. Esempio: $\sin(2\pi\,4\,nT_s + \frac{\pi}{5})$ con $T_s = 1/8$ vale $(-1)^n\sin\frac{\pi}{5}$, quindi l'ampiezza apparente è $5\sin 36° = 2.94$ invece di 5. Per questo in pratica si sovracampiona ([[teorema-del-campionamento]]).

#### Dubbi chiariti

- **"Perché $T_s = 0.498$ e non 0.5?"** Perché nel vettore esistono solo multipli di $dt = 6$ ms, e 0.5 non lo è ($0.5/0.006 = 83.3$).
- **"Il segnale campionato è ancora un vettore di $10^4$ punti?"** Sì. È il modo di simulare $x_\delta(t)$ restando sulla griglia "continua": serve per poterlo convolvere con il filtro di ricostruzione, che vive sulla stessa griglia.
- **"Perché $f_s = 2W$ non basta?"** Nell'esempio 1 perché il segnale non è a banda limitata (aliasing piccolo). Nell'esempio 2 perché l'arrotondamento porta $f_s$ sotto $2W$ (aliasing grosso). E comunque $2W$ esatto è il caso limite.

#### Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=11|p. 11]], [[Campionamento_AD_DA.pdf#page=13|p. 13]], [[Campionamento_AD_DA.pdf#page=21|p. 21]]

[[teorema-del-campionamento]] (campionamento ideale e repliche), [[aliasing]] (ripiegamento, filtro antialiasing).

### Lab 2 — Interpolazione: convoluzione, durata e taglio · [[lab-interpolazione|pagina]]

> ⚠️ Non materia d'esame: serve a vedere l'[[interpolazione]] all'opera e a capire due cose che nel codice sembrano misteriose: perché il ricostruito è più lungo del segnale e perché va tagliato. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-campionamento]].

#### Cosa fa il codice · [[AD_conversion.m]] righe 103–131

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

#### Cosa succede davvero

##### 1. La convoluzione è la formula di interpolazione · [[Campionamento_AD_DA.pdf#page=17|p. 17]]
Nelle slide la ricostruzione è $x_r(t) = \sum_n x(n)\,h_r(t - nT_c)$ ([[interpolazione]]): ogni campione "accende" una copia del filtro centrata sul suo istante e pesata dal suo valore, e le copie si sommano.
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

##### 2. Perché il risultato dura di più: le durate si sommano
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

##### 3. Perché si taglia, e perché proprio lì
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

##### 4. I tre filtri a confronto · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]]
![[grafico-lab-interpolatori.png]]
*🧩 Grafico mio, esempio 1 senza quantizzazione; SNR calcolato come in [[lab-snr]].*
- *Rettangolo (C = 1), SNR 15.8 dB: gradini, con picchi verticali (spiegati sotto). In verde tratteggiato lo ZOH corretto e causale, SNR 12.2 dB.*
- *Triangolo (C = 2), SNR 50.2 dB: la spezzata coincide con il trapezio.*
- *Sinc (C = 3), SNR 26.7 dB: curva morbida con piccole oscillazioni, massimo 1.029 in $t = -0.82$ s.*

**Perché il triangolo vince qui.** Il trapezio è esso stesso una spezzata, e i suoi spigoli ($\pm 1$, $\pm 2$) cadono quasi esattamente su campioni ($\pm 0.996$, $\pm 1.992$). La FOH, che unisce i campioni con segmenti, lo ricostruisce quasi alla perfezione: errore massimo 0.008. È una coincidenza favorevole di questo segnale, non una regola.

**Perché la sinc oscilla.** La serie di Shannon ricostruisce l'unico segnale **a banda limitata** $|f| < f_s/2$ che passa per i campioni. Il trapezio non è a banda limitata: i suoi spigoli richiedono frequenze alte, che la sinc non può produrre. Ottiene quindi una versione "smussata" con piccole oscillazioni, a cui si aggiungono il poco aliasing ([[lab-campionamento]]) e il troncamento a 25 lobi. Nell'esempio 2, che è a banda limitata, la sinc è la scelta giusta ([[lab-campionamento]]).

**Il rettangolo del codice (C = 1) ha due particolarità** (🧩 osservazioni mie, dalla replica):
1. `th = 0:dt:Ts` contiene **sia 0 sia $T_s$**: 84 punti per un intervallo lungo $T_s$ = 83 passi. Due rettangoli adiacenti hanno quindi un punto in comune, che viene sommato due volte. Da qui i picchi a 2 (dove due campioni valgono 1) e a 1.5 (dove valgono 1 e 0.5). Con `th = 0:dt:Ts-dt` spariscono.
2. Il filtro è **causale**: `th` parte da 0, non da $-T_s/2$. Il taglio "da $(L-1)/2$" pensato per i filtri simmetrici lo anticipa di $41\,dt = 0.246 \approx T_s/2$. I gradini risultano centrati sui campioni, cioè un'interpolazione "al campione più vicino", non causale. Lo ZOH vero delle slide tiene invece il campione **dopo** l'istante di campionamento: è la curva verde, più in ritardo e con SNR più basso (12.2 dB).

##### 5. Quanto deve essere largo il filtro · [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]
> 📄 Larghezze delle slide: ZOH $h_r(t) = \Pi\big(\frac{t - T_c/2}{T_c}\big)$, un rettangolo largo $T_c$; FOH $h_r(t) = \Lambda(t/T_c)$, un triangolo con base da $-T_c$ a $T_c$, cioè larga $2T_c$. Nel codice: `th = 0:dt:Ts` e `th = -Ts:dt:Ts` ([[AD_conversion.m]], righe 111 e 115).
> 🧩 Il perché di quelle larghezze è una spiegazione mia.

**Risposta breve:**
- **rettangolo largo $T_s$**, un periodo di campionamento;
- **triangolo con base $2T_s$**, da $-T_s$ a $+T_s$, cioè alto 1 al centro e nullo sui campioni vicini.

Le larghezze non sono arbitrarie: sono le uniche per cui valgono **due condizioni** che ogni interpolatore di questo tipo deve rispettare.

**Condizione 1: passare per i campioni.** Nell'istante $mT_s$ il ricostruito deve valere esattamente $x(mT_s)$. Dalla serie
$$x_r(mT_s) = \sum_n x(nT_s)\,h\big((m - n)T_s\big)$$
serve che $h$ valga 1 in 0 e 0 in tutti gli altri multipli di $T_s$:
$$h(0) = 1, \qquad h(kT_s) = 0 \quad \text{per } k \neq 0$$
- Il triangolo con base $2T_s$ ci riesce: arriva a zero proprio in $\pm T_s$, sui campioni vicini.
- Con base $3T_s$ in $\pm T_s$ vale ancora $1/3$: ogni campione "sporca" i vicini, e il ricostruito non passa più per i campioni.
- La sinc $\text{sinc}(t/T_s)$ soddisfa la stessa condizione con i suoi zeri in $kT_s$.

**Condizione 2: niente buchi e niente sovrapposizioni.** Se il segnale è costante, per esempio tutti i campioni valgono 1, il ricostruito deve valere 1 **ovunque**, anche tra un campione e l'altro. Con tutti i campioni pari a 1 la serie diventa $\sum_n h(t - nT_s)$, quindi deve essere
$$\sum_n h(t - nT_s) = 1 \quad \text{per ogni } t$$
Le copie di $h$, messe una dopo l'altra ogni $T_s$, devono **pavimentare** l'asse esattamente una volta:
- **rettangolo:** copie larghe $T_s$ messe ogni $T_s$ si toccano senza sovrapporsi. Più strette lasciano buchi (somma 0), più larghe si sovrappongono (somma 2);
- **triangolo:** in ogni punto tra $nT_s$ e $(n+1)T_s$ ci sono esattamente due triangoli accesi. Uno scende come $1 - \tau/T_s$, l'altro sale come $\tau/T_s$, con $\tau = t - nT_s$, e i due pesi sommano sempre a 1. Il ricostruito è quindi la media pesata dei due campioni vicini: il segmento che li unisce.

![[grafico-lab-somma-pesi.png]]
*🧩 Grafico mio: la condizione 2 vista direttamente. Tutti i campioni valgono 1 (punti neri) e si disegna $\sum_n h(t - nT)$.*
- *Rettangolo: largo $T$ dà 1 ovunque (blu); largo $T/2$ alterna 1 e 0, perché ci sono buchi; largo $1.5T$ alterna 2 e 1, perché le copie si sovrappongono.*
- *Triangolo: base $2T$ dà 1 ovunque; base $T$ scende a 0 a metà tra i campioni; base $3T$ oscilla tra 1.33 e 1.67 e non vale 1 nemmeno sui campioni.*

![[grafico-lab-larghezza-filtro.png]]
*🧩 Grafico mio: lo stesso segnale lento (tratteggiato) campionato ogni $T$ (punti arancio) e ricostruito con sei larghezze. In verde le copie di $h$ (una per campione, scalata dal suo valore), in blu o rosso la loro somma.*
- *In alto, rettangolo:*
  - *largo $T/2$: ogni campione è tenuto solo per mezzo periodo, poi il segnale crolla a 0 (buchi);*
  - *largo $T$: la classica scala dello ZOH, ogni valore tenuto fino al campione successivo;*
  - *largo $1.5T$: nella seconda metà di ogni periodo due rettangoli si sommano. Per $t$ tra $2T$ e $2.5T$ il ricostruito vale $x(T) + x(2T) = 0.89 + 0.84 = 1.73$, quasi il doppio del segnale.*
- *In basso, triangolo:*
  - *base $T$: passa per i campioni ma tra l'uno e l'altro ricade a 0 (denti di sega);*
  - *base $2T$: la spezzata che unisce i campioni (FOH);*
  - *base $3T$: anche nei campioni si somma un terzo dei vicini. In $t = T$ il ricostruito vale $x(T) + \frac{x(0) + x(2T)}{3} = 1.39$ invece di $0.89$.*

**Collegamento con il codice.** Il triangolo del laboratorio è quello giusto: `th = -Ts:dt:Ts`, base $2T_s$, e il ricostruito lineare coincide con il trapezio. Il rettangolo del codice, `th = 0:dt:Ts`, è largo $T_s$ ma **più un punto**. È l'equivalente discreto del caso "troppo largo": nel punto in comune due copie si sommano, e da lì vengono i picchi a 2 descritti al punto 4.

> 💡 Connessione: le due condizioni si leggono anche in frequenza. La condizione 2, $\sum_n h(t - nT_s) = 1$, equivale a chiedere che $H_r(f)$ abbia area $H_r(0) = T_s$ e si annulli in $\pm f_s, \pm 2f_s, \dots$, cioè al centro delle repliche. È quello che fanno $T_c\,\text{sinc}(fT_c)$ e $T_c\,\text{sinc}^2(fT_c)$ nel grafico delle $H_r(f)$ di [[interpolazione]]. Un rettangolo largo $1.5T$ ha invece i suoi zeri ogni $\frac{1}{1.5T}$, non ogni $f_s$. (🧩 derivazione non svolta qui: segue dalla formula di Poisson, la stessa che dà le repliche in p. 12.)

##### Le figure del laboratorio · [[Figure_2_interpolazione_lineaare.png]], [[Figure_2_interpolazione_shannon.png]]
![[lab-0928-figure2-interpolazione-lineare.png]]
*Figura del laboratorio, C = 2. In alto il ricostruito $s_r(t)$: il trapezio ritorna identico. Al centro e in basso la parte quantizzata ([[lab-quantizzazione]]).*

![[lab-0928-figure2-interpolazione-shannon.png]]
*Figura del laboratorio, C = 3. In alto il ricostruito con la sinc: fianchi arrotondati, due gobbe sopra 1 attorno a $\pm 0.8$ s e piccole oscillazioni fuori da $[-2, 2]$.*

#### Dubbi chiariti

- **"Perché il ricostruito dura più dei due segnali presi singolarmente?"** Perché la convoluzione fa scorrere un segnale sull'altro: l'uscita esiste da quando si toccano a quando si lasciano, cioè per la somma delle durate (derivazione al punto 2).
- **"Perché tagliarlo?"** Per riportarlo sull'asse di $s(t)$ e confrontarlo punto per punto. I pezzi tolti sono code fuori dalla finestra in cui conosciamo il segnale.
- **"Quanto deve essere largo il rettangolo, o il triangolo?"** Rettangolo largo $T_s$, triangolo con base $2T_s$. Sono le uniche larghezze per cui il ricostruito passa per i campioni e le copie di $h$ non lasciano buchi né si sovrappongono (punto 5).
- **"Perché da $(L-1)/2$?"** Perché è il ritardo introdotto da un filtro centrato in 0 ma memorizzato a partire da $th(1) = -\frac{L-1}{2}dt$: lo si compensa scartando quei punti.

#### Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]

[[interpolazione]]: serie di Shannon, ZOH, FOH. Il confronto tra i tre SNR corrisponde a quello tra le loro $H_r(f)$ nel grafico di quella pagina.

### Lab 3 — Quantizzazione · [[lab-quantizzazione|pagina]]

> ⚠️ Non materia d'esame: serve a vedere la [[quantizzazione-uniforme]] su numeri veri. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-campionamento]] e [[lab-interpolazione]].

#### Cosa fa il codice · [[AD_conversion.m]] righe 146–175

```matlab
bits  = 4;
s_min = min(s_samp);  s_max = max(s_samp);
range = s_max - s_min;                 % dinamica dei campioni
Nq    = pow2(bits);                    % 2^4 = 16 livelli
Delta = range/Nq;                      % larghezza di una cella
cbook = s_min+Delta/2:Delta:s_max;     % livelli al centro delle celle
for k=1:length(is)                     % per ogni campione:
   [~,index(k)] = min(abs(cbook-s_samp(is(k))));   % livello più vicino
end
s_q(is) = cbook(index);                % campioni quantizzati
sq_r_trunc = ...conv(s_q,h)...         % stessa interpolazione di prima
```

1. **Dinamica.** Si prende l'intervallo $[s_{min}, s_{max}]$ dei valori campionati.
2. **Celle.** Lo si divide in $N_q = 2^{b}$ celle uguali di larghezza $\Delta$.
3. **Codebook.** I livelli (parole codice) sono i **centri** delle celle.
4. **Quantizzazione.** Ogni campione va nel livello più vicino.
5. **Ricostruzione.** I campioni quantizzati passano nello stesso interpolatore di [[lab-interpolazione]], con lo stesso taglio.

#### Cosa succede davvero

##### I numeri dell'esempio 1 · [[Campionamento_AD_DA.pdf#page=26|p. 26]], [[Campionamento_AD_DA.pdf#page=28|p. 28]]
> 🧩 Derivazione mia

$$
\begin{aligned}
s_{min} &= 0,\quad s_{max} = 1 \Rightarrow \text{range} = 1 && \text{campioni del trapezio (lab 1)} \\
N_q &= 2^4 = 16 && b = 4\ \text{bit} \\
\Delta &= \text{range}/N_q = 1/16 = 0.0625 && \text{larghezza di una cella} \\
\text{cbook} &= 0.03125,\ 0.09375,\ \dots,\ 0.96875 && \text{da } \Delta/2 \text{ con passo } \Delta\text{: 16 valori}
\end{aligned}
$$

Cosa succede ai campioni:

| Campione | Livello più vicino | Errore $e = s_q - s$ |
|---|---|---|
| 0 (i 112 campioni fuori dal trapezio) | 0.03125 | $+0.03125 = +\Delta/2$ |
| 0.008 (in $\pm 1.992$) | 0.03125 | +0.023 |
| 0.506 (in $\pm 1.494$) | 0.53125 (distanza 0.025, contro 0.038 da 0.46875) | +0.025 |
| 1 (5 campioni) | 0.96875 | $-0.03125 = -\Delta/2$ |

È il quantizzatore uniforme delle slide: celle larghe $\Delta$, livello nel punto medio, $|e| \le \Delta/2$ nella regione granulare. Qui la dinamica non è simmetrica ($[0, 1]$ invece di $[-X_{max}, X_{max}]$), ma la relazione è la stessa: $M\Delta = $ ampiezza della dinamica, con $M = N_q$ ([[quantizzazione-uniforme]]).

##### Lo zero non esiste · [[Campionamento_AD_DA.pdf#page=30|p. 30]]
Con i livelli al centro delle celle e l'estremo della dinamica in 0, **nessun livello vale 0**: il più basso è $\Delta/2$. Tutti i campioni nulli, cioè 112 su 121, diventano 0.03125. Dopo l'interpolazione il segnale ricostruito ha un "pavimento" a 0.031 su tutta la finestra fuori dal trapezio: è la riga sollevata che si vede in basso nelle due figure del laboratorio.

Allo stesso modo il massimo 1 diventa 0.96875: il plateau ricostruito si abbassa di $\Delta/2$.

> 🧩 Perché conta: l'errore di questi campioni non è "casuale tra $-\Delta/2$ e $\Delta/2$" come nel modello delle slide, ma vale **sempre esattamente** $+\Delta/2$. Il modello $\Delta^2/12$ sottostima quindi il rumore: le conseguenze sull'SNR sono in [[lab-snr]].

![[grafico-lab-quantizzazione.png]]
*🧩 Grafico mio (replica dello script, 4 bit).*
- *A sinistra: la caratteristica a gradini $Q(x)$ con i 16 livelli. I pallini arancio sono i valori dei campioni del trapezio (0, 0.008, 0.506, 1): lo 0 finisce su $\Delta/2$.*
- *Al centro: l'errore sui 121 campioni. Quasi tutti valgono $+\Delta/2$ (i campioni nulli); i 5 campioni a 1 valgono $-\Delta/2$; i quattro sui fianchi stanno in mezzo. Tutti restano dentro $\pm\Delta/2$ (linee rosse).*
- *A destra: il ricostruito dopo la quantizzazione (interpolazione lineare), con il pavimento a 0.031 e il plateau a 0.969.*

##### Le figure del laboratorio
Nelle figure [[Figure_2_interpolazione_lineaare.png]] e [[Figure_2_interpolazione_shannon.png]] (embed in [[lab-interpolazione]]):
- **pannello centrale:** i campioni quantizzati $s_q(n)$. Le aste nulle ora partono da 0.03, quelle a 1 arrivano a 0.97, quelle a 0.5 a 0.53;
- **pannello in basso:** il ricostruito $\hat s_q(t)$. Con il triangolo si vede il pavimento a 0.03 e un piccolo gomito in $t = \pm 1.5$ s, dove il campione 0.506 è diventato 0.531. Con la sinc la curva è morbida e ha anche le oscillazioni fuori dal trapezio.

#### Dubbi chiariti

- **"Perché il segnale ricostruito non torna a zero?"** Perché con i livelli al centro delle celle lo zero non è rappresentabile: il livello più basso è $\Delta/2$. Un quantizzatore con un livello in 0 (celle centrate sullo zero) non avrebbe questo difetto.
- **"Quantizzare cambia la durata o l'allineamento?"** No: `s_q` è nullo negli stessi punti di `s_samp` (solo i campioni vengono modificati), e si usano lo stesso $h$ e lo stesso taglio.

> 🧩 Dettaglio del codice: `s_min` e `s_max` sono calcolati su tutto `s_samp`, compresi gli zeri messi tra un campione e l'altro. Per il trapezio non cambia nulla, perché il minimo dei campioni è già 0. Con campioni tutti positivi, però, il minimo diventerebbe 0 anche se nessun campione vale 0, e la dinamica risulterebbe più larga del necessario. Andrebbe usato `s_samp(is)`.

#### Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=27|p. 27]], [[Campionamento_AD_DA.pdf#page=28|28]]

[[quantizzazione-uniforme]] (celle, livelli al centro, errore $|e| \le \Delta/2$: p. 25 – p. 28); il codice binario dei livelli, 4 bit per 16 livelli, qui non viene scritto: lo script conserva direttamente i valori dei livelli.

### Lab 4 — SNR: cosa misura il numero stampato · [[lab-snr|pagina]]

> ⚠️ Non materia d'esame: serve a capire la legge dei 6 dB/bit di [[snr-di-quantizzazione]] e i suoi limiti. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-quantizzazione]].

#### Cosa fa il codice · [[Campionamento_AD_DA.pdf#page=30|p. 30]] · [[AD_conversion.m]] righe 189–192

```matlab
P_s   = mean(s.^2);                  % potenza del segnale originale
E_q   = mean((s-sq_r_trunc).^2);     % potenza dell'errore
SNR_q = 10*log10(P_s/E_q)            % in dB (senza ';': viene stampato)
```

È la definizione delle slide, $\text{SNR} = \langle x^2\rangle / \langle e^2\rangle$, con le medie temporali calcolate sulla griglia. C'è però una differenza importante: l'errore è `s - sq_r_trunc`, cioè **segnale originale meno segnale ricostruito dopo quantizzazione e interpolazione**. Non è l'errore di quantizzazione $e(n) = x_q(n) - x(n)$ sui soli campioni.

#### Cosa succede davvero

##### Il valore stampato: 16.7 dB (esempio 1, triangolo, 4 bit)
> 🧩 Derivazione mia, con i numeri della replica Python

$$
\begin{aligned}
P_s &= \frac{1}{N}\sum_n s^2(t_n) = \frac{1}{N\,dt}\sum_n s^2(t_n)\,dt \approx \frac{E}{D} && \text{media su tutta la finestra} \\
&= \frac{8/3}{60} = 0.0444 && E = 8/3 \text{ (lab 0)},\ D = 60\ \text{s} \\
E_q &\approx \frac{56}{60}\cdot\Big(\frac{\Delta}{2}\Big)^2 + \text{(errore sul trapezio)} && \text{fuori dal trapezio l'errore vale sempre } \Delta/2 \\
&= 0.933\cdot 9.77\cdot10^{-4} + \dots \approx 9.1\cdot10^{-4} + 0.5\cdot10^{-4} = 9.6\cdot10^{-4} && \Delta = 1/16 \\
\text{SNR}_q &= 10\log_{10}\frac{0.0444}{9.6\cdot10^{-4}} = 10\log_{10}46.4 \approx 16.7\ \text{dB} && \text{valore stampato}
\end{aligned}
$$
Nella simulazione il 95% dell'errore viene dai 56 s in cui il segnale è **nullo** e il ricostruito vale 0.031 ([[lab-quantizzazione]]).

##### Tre cose che il numero mescola
1. **La quantizzazione**, che è quello che si vorrebbe misurare.
2. **L'interpolazione.** Anche senza quantizzare, il ricostruito non è identico all'originale. Senza quantizzazione l'SNR vale 50.2 dB con il triangolo, 26.7 dB con la sinc e 15.8 dB con il rettangolo del codice ([[lab-interpolazione]]). Con la sinc, quindi, l'SNR non può superare circa 27 dB, qualunque sia il numero di bit.
3. **La finestra di osservazione.** $P_s$ e $E_q$ sono medie su 60 s, di cui 56 di "silenzio". Calcolando lo stesso SNR solo su $|t| < 2.5$ s si ottengono **28.4 dB** invece di 16.7: la potenza del segnale sale di 12 volte, quella dell'errore molto meno.

##### Confronto con la legge dei 6 dB/bit
> 🧩 Derivazione mia

Il modello delle slide suppone l'errore uniforme in $(-\Delta/2, \Delta/2)$, quindi con potenza $\Delta^2/12$ ([[snr-di-quantizzazione]]). Qui invece quasi tutti gli errori valgono esattamente $\Delta/2$, con potenza $(\Delta/2)^2 = \Delta^2/4$:
$$
\begin{aligned}
\frac{\Delta^2/4}{\Delta^2/12} &= 3 && \text{rumore vero / rumore del modello} \\
10\log_{10}3 &= 4.77\ \text{dB} && \text{l'SNR vero è più basso di tanto}
\end{aligned}
$$
- **Modello:** $10\log_{10}\dfrac{0.0444}{(1/16)^2/12} = 21.4$ dB.
- **Misurato:** 16.7 dB. La differenza, 4.7 dB, è proprio il fattore 3.

La **pendenza** di 6 dB/bit invece resta: ogni bit in più dimezza $\Delta$, qualunque sia la forma dell'errore. Se l'errore è proporzionale a $\Delta$, la sua potenza si divide per 4, cioè $10\log_{10}4 = 6.02$ dB in più di SNR.

| $b$ [bit] | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| SNR del codice [dB] | −1.4 | 4.6 | 10.6 | **16.7** | 22.7 | 28.7 | 34.4 | 40.0 | 44.7 | 47.9 |
| SNR sui soli campioni [dB] | −1.4 | 4.7 | 10.7 | 16.7 | 22.8 | 28.9 | 34.8 | 40.9 | 46.8 | 52.9 |

*🧩 Valori dalla replica Python, esempio 1 con triangolo. Fino a 7–8 bit le due righe coincidono e crescono di 6.0 dB per bit. Poi quella del codice si ferma verso il limite dell'interpolazione (50.2 dB): il rumore di quantizzazione è ormai più piccolo dell'errore di ricostruzione.*

![[grafico-lab-snr-vs-bit.png]]
*🧩 Grafico mio.*
- *Blu: SNR stampato dal codice al variare di $b$. Arancio: SNR dei soli campioni.*
- *Nero tratteggiato: il modello $\Delta^2/12$, parallelo ma 4.77 dB più in alto.*
- *Linee orizzontali: i limiti senza quantizzazione, 50.2 dB con il triangolo e 26.7 dB con la sinc. La curva blu non può superarli.*

#### Dubbi chiariti

- **"16.7 dB con 4 bit: la formula non dava di più?"** La formula $6.02b + 4.77 - [k_c]_{dB}$ vale con l'errore uniforme. Qui l'errore è sistematico ($\Delta/2$ sugli zeri) e costa 4.77 dB. In più $P_s$ è piccola, perché il segnale occupa 4 s su 60.
- **"Allora il codice sbaglia?"** No: misura l'SNR **dell'intera catena** A/D + D/A su quella finestra. È una misura diversa, più "da ingegnere", di quella della slide, che isola la sola quantizzazione.
- **"Aumentare i bit migliora sempre?"** Solo finché domina la quantizzazione. Oltre, conta l'interpolatore (e prima ancora il campionamento: vedi l'esempio 2 in [[lab-campionamento]], dove l'aliasing tiene l'SNR a 2 dB).

#### Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=29|p. 29]], [[Campionamento_AD_DA.pdf#page=30|30]]

[[snr-di-quantizzazione]]: definizione, modello $\Delta^2/12$ e legge dei 6 dB/bit. Il fattore di carico $k_c$ di [[quantizzazione-uniforme]] qui è grande, perché la potenza media è piccola rispetto alla dinamica: anche questo abbassa l'SNR.
