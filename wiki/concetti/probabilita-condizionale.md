---
tipo: concetto
importanza_esame: alta
prerequisiti: ["spazio-di-probabilita"]
fonti_pdf: ["Probabilità.pdf#page=7", "Probabilità.pdf#page=9", "Probabilità.pdf#page=10", "Probabilità.pdf#page=11", "Probabilità.pdf#page=12"]
---

# Probabilità condizionale, probabilità composta e indipendenza

## Definizione · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=11|p. 11]]

Dati due eventi $A$ e $B$ di uno [[spazio-di-probabilita]] con $P(B) \neq 0$, la **probabilità condizionale di $A$ dato $B$** è

$$P(A|B) \triangleq \frac{P(AB)}{P(B)}, \qquad P(AB) \equiv P(A \cap B)$$

È un "raffinamento" di $P(A)$ che tiene conto dell'informazione "si è verificato $B$".

**Indipendenza** (statistica) di due eventi:
$$P(AB) = P(A)\,P(B)$$

## Formule · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=9|p. 9]]–[[Probabilità.pdf#page=12|12]]

| Formula | Significato | Validità |
|---|---|---|
| $P(A\mid B) = \dfrac{P(AB)}{P(B)}$ | condizionale | $P(B)\neq 0$ |
| $P(AB) = P(A\mid B)P(B) = P(B\mid A)P(A)$ | **legge della probabilità composta** | $P(A),P(B)\neq0$ |
| $P(A\mid B,C) = \dfrac{P(ABC)}{P(BC)}$ | condizionamento su più eventi ($B\cap C$) | $P(BC)\neq 0$ |
| $P(A_1\cdots A_n) = P(A_1)P(A_2\mid A_1)\cdots P(A_n\mid A_1,\dots,A_{n-1})$ | **regola della catena** | condizionanti a prob. non nulla |
| $P(AB)=P(A)P(B)$ | indipendenza di due eventi | — |
| $P\left(\bigcap_{i\in I}A_i\right)=\prod_{i\in I}P(A_i)\ \forall I\subseteq\{1..n\}$ | indipendenza di $n$ eventi | — |

> 🧮 Formula chiave: $P(AB) = P(A|B)P(B)$ e regola della catena.

**Attrazione e repulsione**:
- $P(A|B) > P(A)$: $A$ è "attratto" da $B$;
- $P(A|B) < P(A)$: $A$ è "respinto" da $B$;
- $P(A|B) = P(A)$: $A$ è "indifferente" a $B$, cioè indipendente.

Esempio 2.2: con $A$={piove}, $P(A|\text{estate}) < P(A)$ e $P(A|\text{inverno}) > P(A)$.

## Derivazioni

### Derivazione — $P(\cdot|B)$ soddisfa gli assiomi di Kolmogorov · [[Probabilità.pdf#page=8|p. 8]]
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

### Derivazione — Caso $B \subseteq A$ · [[Probabilità.pdf#page=8|p. 8]]
$$
\begin{aligned}
P(A|B) &= \frac{P(AB)}{P(B)} = \frac{P(B)}{P(B)} = 1 && B\subseteq A \Rightarrow A\cap B = B \\
P(B|A) &= \frac{P(AB)}{P(A)} = \frac{P(B)}{P(A)} \ge P(B) && P(A) \le 1
\end{aligned}
$$
Da qui si vede che in generale $P(A|B) \neq P(B|A)$: i denominatori sono diversi.

### Derivazione — Regola della catena per tre eventi · [[Probabilità.pdf#page=10|p. 10]]
$$
\begin{aligned}
P(ABC) &= P(A|B,C)\,P(BC) && \text{definizione di } P(A|B,C) \\
&= P(A|B,C)\,P(B|C)\,P(C) && \text{prob. composta su } P(BC)
\end{aligned}
$$
La successione logica è $C \to B \to A$. Scegliendo l'ordine $A\to B\to C$ si ottiene $P(ABC)=P(A)P(B|A)P(C|A,B)$. Le permutazioni dei 3 eventi sono $3! = 6$, quindi ci sono 6 scritture possibili. Per $n$ eventi si procede per induzione applicando la stessa idea a $P(A_1\cdots A_{n-1})$, e le scritture sono $n!$.

### Derivazione — L'indipendenza è simmetrica · [[Probabilità.pdf#page=11|p. 11]]
> 🧩 Derivazione mia
$$
\begin{aligned}
P(A|B) = P(A) &\Rightarrow P(AB) = P(A|B)P(B) = P(A)P(B) && \text{prob. composta} \\
&\Rightarrow P(B|A) = \frac{P(AB)}{P(A)} = \frac{P(A)P(B)}{P(A)} = P(B) && P(A)\neq 0
\end{aligned}
$$

### Derivazione — Perché per tre eventi servono entrambe le condizioni · [[Probabilità.pdf#page=12|p. 12]]
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

## Spiegazione · [[Probabilità.pdf#page=9|p. 9]], [[Probabilità.pdf#page=11|p. 11]], [[Probabilità.pdf#page=12|12]]

- **Ordine degli eventi**: matematicamente l'ordine nella probabilità composta è ininfluente, ma conviene condizionare sull'evento che si verifica *prima*, logicamente o cronologicamente. Esempio 2.3 (estrazione di due palle) → [[calcolo-probabilita-eventi]].
- **Indipendenti ≠ mutuamente esclusivi**.
  > 🧩 Derivazione mia: se $A\cap B = \emptyset$ con $P(A),P(B)>0$, allora $P(AB) = 0 \neq P(A)P(B) > 0$. Due eventi disgiunti a probabilità non nulla sono quindi sempre **dipendenti**: sapere che si è verificato $A$ esclude $B$.
- Per tre eventi indipendenti il condizionamento "non opera" mai: $P(A|B,C)=P(A)$, $P(AB|C) = P(AB)$, ecc.
- Esempio 2.6 (moneta lanciata due volte) → [[calcolo-probabilita-eventi]].

> 🎯 Esame: la confusione tra eventi indipendenti ed eventi mutuamente esclusivi è una domanda classica.

## Perché importa

In ricezione si ragiona sempre per condizionamento: la probabilità d'errore *dato* il simbolo trasmesso, la verosimiglianza del segnale ricevuto *dato* un'ipotesi. L'indipendenza dei simboli e del rumore rende trattabili i calcoli.

## Connessioni

- [[probabilita-totale-e-bayes]] — combina probabilità composta e partizione di $\Omega$.
- [[coppie-di-variabili-aleatorie]] — la pdf condizionale $f_Y(y|x)$ è la versione per v.a. di $P(A|B)$; l'indipendenza di v.a. è la fattorizzazione della pdf congiunta.

## Fonti · [[Probabilità.pdf#page=7|p. 7]], [[Probabilità.pdf#page=12|p. 12]]

- [[elementi-teoria-probabilita]]

_Aggiornato: 2026-10-14 — formule nelle tabelle: modulo scritto con \lvert \rvert e condizionamento con \mid (il \| non si leggeva bene); 2026-09-23 — creazione da ingest Probabilità.pdf_
