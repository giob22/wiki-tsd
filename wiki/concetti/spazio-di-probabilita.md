---
tipo: concetto
importanza_esame: media
prerequisiti: []
fonti_pdf: ["Probabilità.pdf#page=2", "Probabilità.pdf#page=5", "Probabilità.pdf#page=6"]
---

# Spazio di probabilità e assiomi di Kolmogorov

## Definizione · [[Probabilità.pdf#page=2|p. 2]], [[Probabilità.pdf#page=3|3]], [[Probabilità.pdf#page=5|p. 5]]

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

## Formule · [[Probabilità.pdf#page=5|p. 5]], [[Probabilità.pdf#page=6|6]]

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

## Derivazioni · [[Probabilità.pdf#page=6|p. 6]]

> 🧩 Derivazione mia: la slide dice che le proprietà «si possono dimostrare» dagli assiomi ma non mostra i passaggi.

### Derivazione — Proprietà 1: $P(\emptyset)=0$
**Si parte da:** assioma III con $A_1 = \Omega$, $A_n = \emptyset$ per $n \ge 2$ (a due a due disgiunti, perché $\Omega \cap \emptyset = \emptyset$).
$$
\begin{aligned}
P(\Omega) &= P(\Omega \cup \emptyset \cup \emptyset \cup \dots) && \Omega \cup \emptyset = \Omega \\
&= P(\Omega) + \sum_{n=2}^{\infty} P(\emptyset) && \text{assioma III} \\
\Rightarrow \sum_{n=2}^{\infty} P(\emptyset) &= 0 && \text{sottraggo } P(\Omega)=1 \text{ (finito)} \\
\Rightarrow P(\emptyset) &= 0 && \text{somma di infiniti termini uguali} \ge 0 \text{ (assioma I)}
\end{aligned}
$$

### Derivazione — Proprietà 2 (finita additività)
**Si parte da:** assioma III con $A_1 = A$, $A_2 = B$, $A_n = \emptyset$ per $n \ge 3$.
$$
\begin{aligned}
P(A \cup B) &= P(A) + P(B) + \sum_{n\ge3} P(\emptyset) && \text{assioma III} \\
&= P(A) + P(B) && \text{proprietà 1}
\end{aligned}
$$

### Derivazione — Proprietà 3 (complementare)
$$
\begin{aligned}
1 = P(\Omega) &= P(A \cup \bar A) && \text{assioma II; } A \cup \bar A = \Omega \\
&= P(A) + P(\bar A) && \text{prop. 2, perché } A \cap \bar A = \emptyset \\
\Rightarrow P(\bar A) &= 1 - P(A)
\end{aligned}
$$

### Derivazione — Proprietà 4 (unione di eventi qualsiasi)
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

### Derivazione — Proprietà 5 (Boole)
Dalla 4, visto che $P(AB) \ge 0$ (assioma I): $P(A\cup B) = P(A)+P(B)-P(AB) \le P(A)+P(B)$.

### Derivazione — Proprietà 6 (monotonia)
$$
\begin{aligned}
B \subseteq A \Rightarrow A &= B \cup (A \cap \bar B) && \text{unione disgiunta} \\
P(A) &= P(B) + P(A \bar B) && \text{prop. 2} \\
&\ge P(B) && P(A\bar B) \ge 0 \text{ (assioma I)}
\end{aligned}
$$

### Derivazione — Proprietà 7 · [[Probabilità.pdf#page=5|p. 5]]
$B \subseteq \Omega$, quindi per la prop. 6 $P(B) \le P(\Omega) = 1$.

**Sanity check:** tutte le proprietà danno valori in $[0,1]$, coerenti con la definizione di $P$.
**Ipotesi:** solo gli assiomi I–III; nessuna ipotesi su $\Omega$ (discreto o continuo).

## Spiegazione

### Terminologia sugli eventi · [[Probabilità.pdf#page=3|p. 3]], [[Probabilità.pdf#page=4|4]]

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

### Interpretazione
La probabilità è una *funzione d'insieme*: prende eventi, non numeri. Gli assiomi sono il minimo indispensabile. Tutto il resto (proprietà 1–7, [[probabilita-condizionale]], [[probabilita-totale-e-bayes]]) ne discende.

## Perché importa · [[Intro.pdf#page=9|p. 9]]

È la base formale per descrivere la natura statistica della comunicazione. La probabilità d'errore di un sistema digitale sarà la probabilità di un evento del tipo {simbolo deciso ≠ simbolo trasmesso}.

## Connessioni

- [[probabilita-condizionale]] — raffina $P(A)$ con l'informazione che $B$ si è verificato.
- [[variabile-aleatoria]] — associa numeri ai risultati $\omega$ per lavorare con funzioni reali.
- [[quantizzazione-uniforme]] — la probabilità di sovraccarico $P_s$ è una probabilità di evento, maggiorata con Chebyshev.

## Fonti · [[Probabilità.pdf#page=2|p. 2]], [[Probabilità.pdf#page=6|p. 6]]

- [[elementi-teoria-probabilita]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
