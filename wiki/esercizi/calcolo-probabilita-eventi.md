---
tipo: esercizio
argomento: "Probabilità di eventi: operazioni su insiemi, probabilità condizionale, indipendenza"
difficoltà: bassa
---

# Calcolo di probabilità di eventi

## Metodo

1. **Definire** $\Omega$ ed esplicitare gli eventi come sottoinsiemi ([[spazio-di-probabilita]]).
2. Tradurre il testo: "e" → $\cap$, "o" → $\cup$, "non" → complementare.
3. Scegliere lo strumento:
   - risultati **equiprobabili** in $\Omega$ finito → $P(A) = |A|/|\Omega|$ (conteggio / combinatoria);
   - esperimento **in più passi** → probabilità composta / regola della catena, condizionando sull'evento che avviene "prima" ([[Probabilità.pdf#page=9]]);
   - **cause/effetto** → probabilità totale e Bayes ([[probabilita-totale-e-bayes]]).
4. Per l'**indipendenza**: controllare $P(AB) = P(A)P(B)$, non l'intuizione.
5. Sanity check: $0\le P\le1$, complementari che sommano a 1.

## Formule usate

- $P(A\cup B) = P(A)+P(B)-P(AB)$ — [[spazio-di-probabilita]] ([[Probabilità.pdf#page=6]])
- $P(AB) = P(A|B)P(B)$ — [[probabilita-condizionale]] ([[Probabilità.pdf#page=9]])
- $P(AB) = P(A)P(B)$ se indipendenti — [[probabilita-condizionale]] ([[Probabilità.pdf#page=11]])
- $P(B) = \sum_iP(B|A_i)P(A_i)$ — [[probabilita-totale-e-bayes]] ([[Probabilità.pdf#page=13]])

## Casi svolti

### Caso 1 — Esempio 1.4: lancio di un dado
**Traccia** ([[Probabilità.pdf#page=4]]): lancio di un dado, il risultato della prova è $\omega = 4$. Stabilire se si verificano $A$ = {pari}, $B$ = {≥ 3}, $C$ = {< 2}, "A e B", "A o C", "A e C".

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

**Risultato:** coincide con la slide ([[Probabilità.pdf#page=4]]).

> 🧩 Estensione mia — con dado equo: $P(A) = 3/6 = 1/2$, $P(B) = 4/6 = 2/3$, $P(AB) = 2/6 = 1/3 = P(A)P(B)$. Quindi $A$ e $B$ sono **indipendenti**, mentre $A$ e $C$ (disgiunti, a probabilità non nulla) sono **dipendenti**.

### Caso 2 — Esempio 2.3: estrazione di due palle
**Traccia** ([[Probabilità.pdf#page=9]]): «estrazione di una coppia di palle da una scatola contenente tre palle bianche e due rosse — soluzione combinatoria vs. soluzione con probabilità condizionale».

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

### Caso 3 — Esempio 2.6: moneta lanciata due volte
**Traccia** ([[Probabilità.pdf#page=11]]): «lancio di una moneta due volte» come esempio di indipendenza.

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

### Caso 4 — Esempio 2.2 (qualitativo)
**Traccia** ([[Probabilità.pdf#page=7]]): $A$ = {piove}; confrontare $P(A|B)$ e $P(A)$ con $B$ = {estate} e $B$ = {inverno}.
**Risultato** (dalla slide): $P(A|\text{estate})<P(A)$, quindi $A$ è "respinto" dall'estate; $P(A|\text{inverno})>P(A)$, quindi $A$ è "attratto" dall'inverno.

## Trappole

- **Disgiunti ≠ indipendenti**: due eventi disgiunti a probabilità non nulla sono sempre *dipendenti* ([[probabilita-condizionale]]).
- $P(A|B)\neq P(B|A)$ in generale: i denominatori sono diversi ([[Probabilità.pdf#page=8]]).
- Per tre eventi, $P(ABC) = P(A)P(B)P(C)$ **non basta** per l'indipendenza: servono anche le coppie ([[Probabilità.pdf#page=12]]).
- Nel metodo combinatorio, contare in modo coerente: o tutto ordinato o tutto non ordinato.
- Nella probabilità totale, verificare che le cause siano una **partizione**.

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
