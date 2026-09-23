---
tipo: concetto
importanza_esame: alta
prerequisiti: ["conversione-ad-da", "disuguaglianza-di-chebyshev"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=25", "Campionamento_AD_DA.pdf#page=26", "Campionamento_AD_DA.pdf#page=27", "Campionamento_AD_DA.pdf#page=28", "Campionamento_AD_DA.pdf#page=29"]
---

# Quantizzazione uniforme, errore di quantizzazione e fattore di carico

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=25]], [[Campionamento_AD_DA.pdf#page=26]]

Nella conversione A/D, oltre a discretizzare i tempi (campionamento), bisogna discretizzare le **ampiezze** del segnale: è la **quantizzazione** ([[Campionamento_AD_DA.pdf#page=25]]). In pratica l'intervallo reale dei valori di ampiezza è suddiviso in **intervalli di quantizzazione**:
- a ogni intervallo è associato un **livello di restituzione** (o di quantizzazione);
- tutte le ampiezze di uno stesso intervallo sono rappresentate dal livello di restituzione di quell'intervallo.

**Esempio** ([[Campionamento_AD_DA.pdf#page=25]]): le ampiezze in $(1,2)$ sono rappresentate dal livello 1.5 (punto medio dell'intervallo), quelle in $(2,3)$ dal livello 2.5, e così via.

![[campionamento-p25-quantizzazione.png]]
*Asse delle ampiezze diviso in intervalli: intervallo #3 = (1,2) → livello #3 = 1.5; intervallo #2 = (2,3) → livello #2 = 2.5; intervallo #1 = (3,4) → livello #1 = 3.5. I punti rossi sono i livelli, al centro di ogni intervallo — [[Campionamento_AD_DA.pdf#page=25]]*

Il quantizzatore è un sistema a tempo discreto **non lineare** e **istantaneo**: $x_q(n) = Q[x(n)]$ ([[Campionamento_AD_DA.pdf#page=26]]).

**Quantizzatore uniforme**, due parametri ([[Campionamento_AD_DA.pdf#page=26]]):
- $\Delta$ = **passo di quantizzazione** (larghezza degli intervalli), nell'unità del segnale (es. V);
- $M$ = numero di intervalli / livelli di restituzione.

Se è **simmetrico**:
- $(-X_{max}, X_{max})$ = intervallo delle ampiezze di ingresso;
- $2X_{max} = M\Delta$ = **dinamica** del quantizzatore.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $2X_{max} = M\Delta \iff \Delta = \frac{2X_{max}}{M}$ | dinamica | [[Campionamento_AD_DA.pdf#page=26]] |
| $b \ge \log_2 M$, di solito $M = 2^b$ | bit per campione | [[Campionamento_AD_DA.pdf#page=27]] |
| $e(n) = x_q(n) - x(n) \iff x_q(n) = x(n)+e(n)$ | errore (rumore) di quantizzazione | [[Campionamento_AD_DA.pdf#page=28]] |
| $R_g = [-X_{max}, X_{max}]$: $\|e(n)\|\le\Delta/2$ | regione granulare | [[Campionamento_AD_DA.pdf#page=28]] |
| $R_s = ]-\infty,-X_{max}[\ \cup\ ]X_{max},+\infty[$: $e(n)$ non limitato | regione di sovraccarico | [[Campionamento_AD_DA.pdf#page=28]] |
| $k_c \triangleq \dfrac{X_{max}}{x_{rms}}$, $x_{rms} = \sqrt{P_x}$ | **fattore di carico** (adimensionale) | [[Campionamento_AD_DA.pdf#page=29]] |
| $P_s = P(\|x(n)\|>X_{max}) \le \dfrac{1}{k_c^2}$ | probabilità di sovraccarico | [[Campionamento_AD_DA.pdf#page=29]] |

> 🧮 Formula chiave: $\Delta = 2X_{max}/M$, $k_c = X_{max}/x_{rms}$, $P_s\le1/k_c^2$.

## Derivazioni

### Derivazione — $|e(n)|\le\Delta/2$ nella regione granulare
**Fonte:** [[Campionamento_AD_DA.pdf#page=28]] (risultato dato)
> 🧩 Derivazione mia
In $R_g$ ogni $x(n)$ cade in un intervallo di larghezza $\Delta$ e il livello di restituzione ne è il **punto medio** (esempio di [[Campionamento_AD_DA.pdf#page=25]]). La distanza massima tra un punto dell'intervallo e il suo punto medio è metà della larghezza: $|e(n)| = |x_q(n)-x(n)| \le \Delta/2$.
In $R_s$ il livello resta quello estremo (es. $q_M = X_{max}-\Delta/2$) mentre $x(n)$ può crescere senza limite, quindi $e(n)$ non è limitato.

### Derivazione — $b\ge\log_2M$
Con $b$ bit si scrivono $2^b$ stringhe distinte. Per dare un codice diverso a ciascuno degli $M$ livelli serve $2^b\ge M$, cioè $b\ge\log_2M$ ([[Campionamento_AD_DA.pdf#page=27]]).

### Derivazione — Probabilità di sovraccarico e four-sigma loading
**Fonte:** [[Campionamento_AD_DA.pdf#page=29]] → derivazione completa in [[disuguaglianza-di-chebyshev]].
**Numeri:** $k_c = 4$ → $P_s\le 1/4^2 = 1/16 = 0.0625$ (6.25%).

### Esempio — Quantizzatore con $M = 4$
**Fonte:** [[Campionamento_AD_DA.pdf#page=26]], [[Campionamento_AD_DA.pdf#page=27]] (figura)
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

## Spiegazione

![[campionamento-p26-quantizzatore-uniforme.png]]

### Codifica binaria
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=27]]

Per completare la A/D, gli $M$ livelli $\{q_1,\dots,q_M\}$ si convertono in **stringhe di bit**:
- servono $b\ge\log_2M$ bit per rappresentare $M$ livelli;
- di solito si sceglie $M = 2^b$ per semplificare la codifica binaria.

Schemi di codifica binaria (associano stringhe di bit ai livelli):
- codifica **naturale** (vedi esempio);
- codifica in **segno e modulo**;
- codifica in **complemento a due**.

La scelta dipende dall'architettura del sistema digitale di elaborazione.

![[campionamento-p27-codifica-binaria.png]]
*Esempio: $M = 4 \Rightarrow b = 2$ bit; codifica naturale dal livello più basso al più alto: 00, 01, 10, 11 — [[Campionamento_AD_DA.pdf#page=27]]*

### Modello additivo
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=28]]

Obiettivo della slide: fissare **criteri quantitativi** per dimensionare un quantizzatore. Scrivere $x_q = x+e$ trasforma il quantizzatore (non lineare) in un **sommatore** con un "rumore" $e(n)$: il **rumore di quantizzazione**. È il modello che permette di parlare di SNR ([[snr-di-quantizzazione]]).

![[campionamento-p28-errore-quantizzazione.png]]
*A destra: modello a sommatore $x(n) + e(n) = x_q(n)$ e caratteristica $Q(x)$ a gradini tra $q_1$ e $q_M$. Nella regione granulare $\mathcal{R}_g = [-X_{max}, X_{max}]$ i gradini seguono la bisettrice; nelle regioni di sovraccarico $\mathcal{R}_s$ l'uscita resta ferma a $q_1$ o $q_M$ — [[Campionamento_AD_DA.pdf#page=28]]*

### Trade-off su $X_{max}$
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=29]]

- L'errore di quantizzazione è **irreversibile**, quindi bisogna evitare che il quantizzatore lavori nella regione di sovraccarico, e per questo si vorrebbe **aumentare $X_{max}$**.
- Ma a parità di $M$, aumentare $X_{max}$ aumenta $\Delta$, e quindi l'errore nella regione granulare.
- È ragionevole scegliere $X_{max}$ **proporzionale al livello del segnale**, misurato dal **valore efficace** $x_{rms} = \sqrt{P_x}$. Da qui la definizione del fattore di carico $k_c = X_{max}/x_{rms}$.
- Assimilando $x(n)$ a una v.a. a media nulla e deviazione standard $x_{rms}$, la disuguaglianza di Chebyshev dà $P_s\le1/k_c^2$.
- Con $k_c = 4$ (*four-sigma loading*): $P_s\le1/16 = 0.0625$ (6.25%).

> 🎯 Esame: le due regioni, perché serve $k_c$, da dove viene il 6.25% del four-sigma loading.

## Perché importa

È il secondo stadio della A/D ([[conversione-ad-da]]) e l'unico **irreversibile**. $b$ fissa sia la qualità (SNR) sia il bit rate ($b\cdot f_c$).

## Connessioni

- [[snr-di-quantizzazione]] — misura l'accuratezza nella regione granulare.
- [[disuguaglianza-di-chebyshev]] — limite su $P_s$.
- [[quantizzazione-non-uniforme]] — cosa cambia se gli intervalli non sono uguali.
- [[variabili-aleatorie-notevoli]] — modello uniforme di $e(n)$.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=25]] – [[Campionamento_AD_DA.pdf#page=29]]

_Aggiornato: 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
