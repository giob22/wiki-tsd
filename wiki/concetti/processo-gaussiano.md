---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria-gaussiana", "momenti-di-un-processo", "stazionarieta"]
fonti_pdf: ["random_processes.pdf#page=41", "random_processes.pdf#page=42", "random_processes.pdf#page=43", "random_processes.pdf#page=44"]
---

# Processo gaussiano

## Definizione

> 📄 Fonte: [[random_processes.pdf#page=41]], [[random_processes.pdf#page=42]]

Il **processo gaussiano** è il processo aleatorio più usato nello studio dei sistemi di comunicazione: ha molte applicazioni pratiche ed è matematicamente trattabile.

$X(t)$ è gaussiano se, campionandolo in $t_1, \dots, t_n$, le variabili aleatorie $X(t_1), \dots, X(t_n)$ sono **congiuntamente gaussiane per ogni $n$**. La loro pdf congiunta di ordine $n$ è determinata completamente da:
- le **medie** $\mu_{X(t_i)} = E[X(t_i)]$, per $i \in \{1, \dots, n\}$ — eq. (31);
- le **covarianze** $C_{XX}(t_k, t_i) = E\{[X(t_k) - \mu_{X(t_k)}][X(t_i) - \mu_{X(t_i)}]\}$, per $k, i \in \{1, \dots, n\}$ — eq. (32).

In forma matriciale, con il vettore aleatorio $\mathbf{X} = [X(t_1), \dots, X(t_n)]^T$ e un suo valore $\mathbf{x} = [x_1, \dots, x_n]^T$ ($^T$ = trasposto), la pdf **gaussiana multivariata** è ([[random_processes.pdf#page=42]])
$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n\det(\boldsymbol{\Sigma})}}\;e^{-\frac12(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})} \tag{33}$$
- $\boldsymbol{\mu} = [\mu_{X(t_1)}, \dots, \mu_{X(t_n)}]^T$ è il **vettore delle medie**;
- $\boldsymbol{\Sigma}$ è la **matrice di covarianza**, con elemento $(k, i)$ pari a $\{\boldsymbol{\Sigma}\}_{k,i} = C_{XX}(t_k, t_i)$;
- $\boldsymbol{\Sigma}^{-1}$ è la sua inversa.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $\mu_{X(t_i)} = E[X(t_i)]$ | medie dei campioni, eq. (31) | [[random_processes.pdf#page=41]] |
| $C_{XX}(t_k, t_i)$ | covarianze dei campioni, eq. (32) | [[random_processes.pdf#page=41]] |
| $f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n\det\boldsymbol{\Sigma}}}e^{-\frac12(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})}$ | gaussiana multivariata, eq. (33) | [[random_processes.pdf#page=42]] |
| $\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$, $\ \mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} \ge 0\ \forall\,\mathbf{u} \in \mathbb{R}^n$ | covarianza simmetrica e semidefinita positiva | [[random_processes.pdf#page=42]] |
| $\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} > 0\ \forall\,\mathbf{u} \neq \mathbf{0}$ | caso non degenere: definita positiva, invertibile | [[random_processes.pdf#page=42]] |
| $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \dots, \sigma_n^2) \Rightarrow f_{\mathbf{X}}(\mathbf{x}) = \prod_i f_{X(t_i)}(x_i)$ | incorrelati ⇒ indipendenti, eq. (34) | [[random_processes.pdf#page=44]] |

Simboli: $n$ = numero di campioni; $\det$ = determinante; $\sigma_i^2$ = varianza di $X(t_i)$; $\mathbf{u}$ = vettore reale qualunque; $f_{\mathbf{X}}$ in [1/V$^n$].

## Derivazioni

### Derivazione — Con $n = 1$ si ritrova la gaussiana scalare
**Fonte:** [[random_processes.pdf#page=42]] per la (33); gaussiana scalare in [[variabile-aleatoria-gaussiana]] ([[Probabilità.pdf#page=23]]).
> 🧩 Verifica mia

$$
\begin{aligned}
\boldsymbol{\Sigma} &= \sigma^2,\quad \det\boldsymbol{\Sigma} = \sigma^2,\quad \boldsymbol{\Sigma}^{-1} = 1/\sigma^2 && n = 1: \text{ la matrice è un numero} \\
f_X(x) &= \frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{(x - \mu)^2}{2\sigma^2}} && \text{sostituisco nella (33)}
\end{aligned}
$$
È la pdf gaussiana di una variabile ✓.

### Derivazione — Due campioni: la gaussiana bivariata
> 🧩 Caso $n = 2$ scritto per esteso (usato nel grafico). Media nulla, varianze 1, coefficiente di correlazione $\rho$ ([[correlazione-e-covarianza]]).

$$
\begin{aligned}
\boldsymbol{\Sigma} &= \begin{pmatrix} 1 & \rho \\ \rho & 1\end{pmatrix},\quad \det\boldsymbol{\Sigma} = 1 - \rho^2,\quad \boldsymbol{\Sigma}^{-1} = \frac{1}{1 - \rho^2}\begin{pmatrix} 1 & -\rho \\ -\rho & 1\end{pmatrix} && \text{inversa di una } 2\times2 \\
\mathbf{x}^T\boldsymbol{\Sigma}^{-1}\mathbf{x} &= \frac{x_1^2 - 2\rho x_1x_2 + x_2^2}{1 - \rho^2} && \text{forma quadratica} \\
f(x_1, x_2) &= \frac{1}{2\pi\sqrt{1 - \rho^2}}\,e^{-\frac{x_1^2 - 2\rho x_1x_2 + x_2^2}{2(1 - \rho^2)}} && \text{(33) con } n = 2:\ \sqrt{(2\pi)^2} = 2\pi
\end{aligned}
$$
Le curve di livello sono ellissi; con $\rho = 0$ sono cerchi.

### Derivazione — $\boldsymbol{\Sigma}$ è simmetrica e semidefinita positiva
**Fonte:** [[random_processes.pdf#page=42]]: proprietà date senza dimostrazione.
> 🧩 Derivazione mia. Scrivo $\tilde X_k = X(t_k) - \mu_{X(t_k)}$.

$$
\begin{aligned}
\{\boldsymbol{\Sigma}\}_{k,i} &= E[\tilde X_k\tilde X_i] = E[\tilde X_i\tilde X_k] = \{\boldsymbol{\Sigma}\}_{i,k} && \text{il prodotto commuta: simmetrica} \\
\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u} &= \sum_k\sum_i u_k\,u_i\,E[\tilde X_k\tilde X_i] && \text{prodotto matrice-vettore} \\
&= E\Big[\Big(\sum_k u_k\tilde X_k\Big)^2\Big] \ge 0 && \text{linearità di } E;\ \text{valore atteso di un quadrato}
\end{aligned}
$$
**Lettura:** $\mathbf{u}^T\boldsymbol{\Sigma}\mathbf{u}$ è la **varianza** della combinazione lineare $\sum_k u_k X(t_k)$, e una varianza non può essere negativa. Vale 0 solo se quella combinazione è (quasi certamente) costante. Il caso **non degenere**, $\boldsymbol{\Sigma}$ definita positiva e quindi invertibile, è quello in cui nessuna combinazione non banale dei campioni è costante. Serve perché la (33) contiene $\boldsymbol{\Sigma}^{-1}$ e $\det\boldsymbol{\Sigma}$ al denominatore.

### Derivazione — Incorrelati ⇒ indipendenti, eq. (34)
**Fonte:** [[random_processes.pdf#page=44]]
$$
\begin{aligned}
\boldsymbol{\Sigma} &= \text{diag}(\sigma_1^2, \dots, \sigma_n^2) && C_{XX}(t_k, t_i) = 0 \text{ per } k \neq i \\
\det\boldsymbol{\Sigma} &= \prod_i \sigma_i^2,\qquad \boldsymbol{\Sigma}^{-1} = \text{diag}(1/\sigma_1^2, \dots, 1/\sigma_n^2) && \text{matrice diagonale} \\
(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu}) &= \sum_i \frac{(x_i - \mu_i)^2}{\sigma_i^2} && \text{spariscono i termini misti} \\
f_{\mathbf{X}}(\mathbf{x}) &= \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}}\,e^{-\frac{(x_i - \mu_i)^2}{2\sigma_i^2}} = \prod_{i=1}^n f_{X(t_i)}(x_i) && e^{\sum} = \prod e;\ \sqrt{(2\pi)^n\prod\sigma_i^2} = \prod\sqrt{2\pi\sigma_i^2}
\end{aligned}
$$
La pdf congiunta è il **prodotto** delle marginali, cioè i campioni sono **indipendenti** ([[coppie-di-variabili-aleatorie]]). Per variabili qualunque, invece, incorrelazione non implica indipendenza ([[correlazione-e-covarianza]]).

### Derivazione — WSS ⇒ SSS per un processo gaussiano
**Fonte:** [[random_processes.pdf#page=44]]: proprietà data senza dimostrazione.
> 🧩 Derivazione mia

- La pdf di ordine $n$ (33) dipende **solo** da $\boldsymbol{\mu}$ e $\boldsymbol{\Sigma}$.
- Se il processo è WSS, la media è costante e la covarianza dipende solo dalla differenza tra gli istanti: $C_{XX}(t_k + \tau, t_i + \tau) = C_{XX}(t_k - t_i)$.
- Quindi i campioni traslati $X(t_1 + \tau), \dots, X(t_n + \tau)$ hanno gli stessi $\boldsymbol{\mu}$ e $\boldsymbol{\Sigma}$ di quelli originali, e quindi la stessa pdf. Questo per ogni $n$: è la (6) per ogni ordine, cioè SSS ([[stazionarieta]]).

Per un processo qualunque questo ragionamento non funziona: le distribuzioni di ordine superiore non sono determinate da media e covarianza.

### Derivazione — Un filtro lineare stabile conserva la gaussianità
**Fonte:** [[random_processes.pdf#page=44]]: proprietà data senza dimostrazione.
> 🧩 Idea della dimostrazione, non una dimostrazione completa. $Y(t) = \int h(\tau)X(t - \tau)\,d\tau \approx \sum_k h(\tau_k)X(t - \tau_k)\,\Delta\tau$: ogni campione dell'uscita è il limite di una **combinazione lineare** di campioni dell'ingresso.
> 📚 Fonte esterna (proprietà standard della gaussiana multivariata, per esempio nel testo di Madhow): combinazioni lineari di variabili congiuntamente gaussiane sono ancora congiuntamente gaussiane.
>
> Quindi i campioni $Y(t_1), \dots, Y(t_n)$ sono congiuntamente gaussiani. Le loro medie e covarianze si calcolano con [[processi-e-sistemi-lti]].

## Spiegazione

### Perché è così importante (slide 38)
> 📄 Fonte: [[random_processes.pdf#page=43]]

- I processi prodotti da fenomeni fisici sono spesso tali che un **modello gaussiano** è adeguato, e gli esperimenti lo confermano.
- Il **teorema del limite centrale** dà la giustificazione matematica: la somma di molti contributi indipendenti tende a una gaussiana ([[variabile-aleatoria-gaussiana]]).
- Il processo gaussiano è molto frequente nei fenomeni fisici e facile da trattare matematicamente: per questo è centrale nello studio dei sistemi di comunicazione.

### Proprietà (slide 39)
> 📄 Fonte: [[random_processes.pdf#page=44]]

1. Un processo gaussiano applicato a un **filtro lineare stabile** dà in uscita un processo ancora **gaussiano**.
2. Un processo gaussiano **WSS** (debolmente stazionario) è anche **stazionario in senso stretto**.
3. Se i campioni $X(t_1), \dots, X(t_n)$ sono **incorrelati**, cioè $C_{XX}(t_k, t_i) = 0$ per $k \neq i$, sono anche **statisticamente indipendenti**. La matrice di covarianza è diagonale e la pdf congiunta è il prodotto delle pdf dei singoli campioni, eq. (34).

> 🧩 In sintesi: per un processo gaussiano, **media e covarianza sono tutto**. La caratterizzazione parziale ([[momenti-di-un-processo]]) coincide con quella completa ([[processo-aleatorio]]), ed è per questo che le proprietà 2 e 3 valgono.

![[grafico-rp-gaussiana-bivariata.png]]
*🧩 Grafico mio (eq. (33) con $n = 2$ e (34), [[random_processes.pdf#page=42]], [[random_processes.pdf#page=44]]). Curve di livello della pdf congiunta di due campioni $X(t_1)$, $X(t_2)$ a media nulla e varianza 1, con 400 coppie estratte.*
- *A sinistra $\rho = 0$: cerchi, e la pdf è il prodotto delle marginali. Incorrelati quindi indipendenti.*
- *A destra $\rho = 0.8$: ellissi inclinate lungo la bisettrice, cioè i due campioni tendono ad avere lo stesso segno.*

*Col processo esponenziale degli altri grafici ($R_{XX}(\tau) = e^{-|\tau|/\tau_c}$), $\rho = 0.8$ corrisponde a due campioni distanti $|t_1 - t_2| = \tau_c\ln(1/0.8) \approx 0.22\,\tau_c$.*

> 🎯 Esame: definire il processo gaussiano; scrivere la (33) e spiegarne i simboli; perché $\boldsymbol{\Sigma}$ è simmetrica e semidefinita positiva; dimostrare le proprietà (WSS ⇒ SSS, incorrelazione ⇒ indipendenza); perché il modello gaussiano è così usato.

## Perché importa

Il rumore termico nei ricevitori si modella come processo gaussiano ([[variabile-aleatoria-gaussiana]], [[sistema-comunicazione-digitale]]). Il processo gaussiano ha tre vantaggi:
- resta gaussiano attraverso i filtri;
- è descritto completamente da media e autocorrelazione;
- ha campioni incorrelati che sono indipendenti.

Per questo le prestazioni dei sistemi, come la probabilità d'errore con la funzione $Q$, si calcolano in forma chiusa.

## Connessioni

- [[variabile-aleatoria-gaussiana]] — il caso $n = 1$; CLT; funzione $Q$.
- [[momenti-di-un-processo]] — media e covarianza, che qui bastano a tutto.
- [[stazionarieta]] — WSS ⇒ SSS solo per i gaussiani.
- [[correlazione-e-covarianza]] e [[coppie-di-variabili-aleatorie]] — incorrelazione, indipendenza, pdf congiunta come prodotto.
- [[processi-e-sistemi-lti]] — medie e correlazioni dell'uscita gaussiana.

## Fonti

- [[processi-aleatori]]
- [[random_processes.pdf#page=41]] – [[random_processes.pdf#page=44]]

_Aggiornato: 2026-09-28 — creazione da ingest random_processes.pdf_
