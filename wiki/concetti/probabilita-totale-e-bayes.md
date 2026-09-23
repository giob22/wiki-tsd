---
tipo: concetto
importanza_esame: alta
prerequisiti: ["probabilita-condizionale"]
fonti_pdf: ["Probabilità.pdf#page=13", "Probabilità.pdf#page=14"]
---

# Teorema della probabilità totale e teorema di Bayes

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=13]], [[Probabilità.pdf#page=14]]

**Ipotesi comuni:** $A_1, \dots, A_n$ eventi mutuamente esclusivi ($A_i \cap A_j = \emptyset$ per $i\neq j$) e $B \subseteq \bigcup_{i=1}^n A_i$.

- **Probabilità totale**: calcola $P(B)$ (l'*effetto*) a partire dalle probabilità **a priori** delle cause $P(A_i)$ e dalle condizionali $P(B|A_i)$.
- **Bayes**: sapendo che si è verificato $B$, calcola le probabilità **a posteriori** delle cause $P(A_i|B)$. È l'**inferenza bayesiana**.

> ⚠️ Contraddizione (refuso nelle slide): le pagine 13 e 14 scrivono "$A_j \cap A_j = \emptyset,\ i\neq j$". La condizione corretta è $A_i \cap A_j = \emptyset$ per $i \neq j$.

## Formule

> 🧮 Formula chiave — Probabilità totale ([[Probabilità.pdf#page=13]]):
> $$P(B) = \sum_{i=1}^{n} P(B|A_i)\,P(A_i)$$

> 🧮 Formula chiave — Bayes ([[Probabilità.pdf#page=14]]):
> $$P(A_i|B) = \frac{P(B|A_i)\,P(A_i)}{\sum_{j=1}^{n} P(B|A_j)\,P(A_j)} = \frac{P(B|A_i)\,P(A_i)}{P(B)}$$

Simboli: $P(A_i)$ = probabilità a priori della causa $i$; $P(B|A_i)$ = probabilità dell'effetto data la causa (verosimiglianza); $P(A_i|B)$ = probabilità a posteriori. Sono tutte adimensionali.

## Derivazioni

### Derivazione — Teorema della probabilità totale
**Fonte:** [[Probabilità.pdf#page=13]] (enunciato senza dimostrazione)
> 🧩 Derivazione mia
$$
\begin{aligned}
B &= B \cap \Big(\textstyle\bigcup_i A_i\Big) && B \subseteq \cup_i A_i \\
&= \textstyle\bigcup_i (B \cap A_i) && \text{distributività} \\
P(B) &= \sum_i P(B A_i) && BA_i \text{ disgiunti (perché } A_i \text{ lo sono); additività} \\
&= \sum_i P(B|A_i)P(A_i) && \text{prob. composta, } [[probabilita-condizionale]]
\end{aligned}
$$

### Derivazione — Teorema di Bayes
$$
\begin{aligned}
P(A_i|B) &= \frac{P(A_iB)}{P(B)} && \text{def. condizionale} \\
&= \frac{P(B|A_i)P(A_i)}{P(B)} && \text{prob. composta al numeratore} \\
&= \frac{P(B|A_i)P(A_i)}{\sum_j P(B|A_j)P(A_j)} && \text{prob. totale al denominatore}
\end{aligned}
$$
**Sanity check:** $\sum_i P(A_i|B) = 1$, perché il numeratore sommato su $i$ dà proprio il denominatore.
**Ipotesi:** $P(B) \neq 0$; cause mutuamente esclusive; ogni effetto ha almeno una causa.

## Spiegazione

> 📄 Fonte: [[Probabilità.pdf#page=13]]

![[probabilita-p13-probabilita-totale.png]]

Lettura "logica" delle ipotesi:
- le cause sono **mutuamente esclusive**;
- se si verifica l'effetto, si è verificata **una (e una sola)** delle cause.

Verificare $B \subseteq \bigcup_i A_i$ può essere complicato. Conviene scegliere gli $A_i$ come **partizione** di $\Omega$ ($\bigcup_i A_i = \Omega$): la condizione vale allora per ogni $B$.

> 🎯 Esame: saper enunciare le ipotesi, dire perché servono (senza esclusività si conterebbero due volte le intersezioni) e dare la lettura cause/effetto.

## Perché importa

Bayes è la base della **decisione** in ricezione, che la fonte cita come compito del demodulatore ([[Intro.pdf#page=19]]). Le cause sono i simboli trasmessi e l'effetto è il segnale ricevuto; scegliere la causa con la massima probabilità a posteriori è l'idea del ricevitore MAP.

> 📚 Fonte esterna: il collegamento con il criterio MAP è standard (es. Madhow, *Fundamentals of Digital Communication*, cap. sulla demodulazione ottima), ma non compare ancora nelle slide ingerite. TODO: verificare quando arriverà la fonte sulla modulazione digitale.

## Connessioni

- [[probabilita-condizionale]] — entrambi i teoremi sono conseguenze dirette della probabilità composta.
- [[coppie-di-variabili-aleatorie]] — versione per densità: $f_X(x|y) = f_Y(y|x) f_X(x)/f_Y(y)$, che segue dalle definizioni di [[Probabilità.pdf#page=34]].
- [[media-e-varianza]] — il centroide di Lloyd-Max $E[x|x\in R_i]$ è una media condizionale ([[quantizzazione-non-uniforme]]).

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=13]], [[Probabilità.pdf#page=14]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
