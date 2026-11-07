---
tipo: esercizio
argomento: "Calcolo della densità spettrale di potenza di un processo (Wiener-Khinchin)"
difficoltà: media
---

# Calcolo della densità spettrale di potenza

## Metodo

1. **Scrivere il modello** del processo e le ipotesi statistiche (medie, correlazioni dei simboli, eventuali ritardi casuali).
2. **Verificare che sia WSS** ([[stazionarieta]]): media costante e $R_{XX}(t, \tau)$ indipendente da $t$. Se non lo è, bisogna prima renderlo WSS, per esempio con un ritardo casuale, altrimenti Wiener-Khinchin così come enunciato non si applica.
3. **Calcolare l'autocorrelazione** $R_{XX}(\tau) = E[X(t)X(t - \tau)]$ ([[autocorrelazione-processi-wss]]), usando linearità del valore atteso e indipendenza tra le variabili in gioco.
4. **Trasformare**: $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ ([[densita-spettrale-di-potenza]]).
5. **Controllare** con le proprietà: $S_{XX} \ge 0$, pari, $\int S_{XX}\,df = R_{XX}(0)$ (potenza), $S_{XX}(0) = \int R_{XX}\,d\tau$.

## Formule usate · Processi [[random_processes.pdf#page=19|p. 19]], [[random_processes.pdf#page=32|p. 32]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]]

- $R_{XX}(\tau) = E[X(t)X(t-\tau)]$ — [[autocorrelazione-processi-wss]]
- Wiener-Khinchin $S_{XX}(f) = \mathcal{F}[R_{XX}(\tau)]$ e potenza $P_X = R_{XX}(0) = \int S_{XX}\,df$ — [[densita-spettrale-di-potenza]]
- Modulazione lineare $s(t) = \sum_n b[n]\,p(t - nT)$ — [[modulazione-digitale]]
- Spettro dell'impulso rettangolare $P(f) = T\,\text{sinc}(fT)$ — [[modulazione-digitale]]

## Casi svolti

### Caso 1 — PSD di un segnale modulato linearmente · Processi [[random_processes.pdf#page=32|p. 32]], [[random_processes.pdf#page=37|p. 37]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]]
**Traccia**: «Example — Compute power spectral density of a linearly modulated signal.» La slide non dà lo svolgimento.
> 🧩 Svolgimento mio. Il modello viene dalla modulazione lineare della lezione precedente; le ipotesi statistiche sono mie, perché la slide non le specifica.

**Modello:**
$$X(t) = \sum_{n=-\infty}^{+\infty} b[n]\,p(t - nT - D)$$

**Ipotesi:**
- **(H1)** i simboli $b[n]$ hanno media nulla, sono incorrelati e hanno la stessa varianza: $E[b[n]] = 0$ e $E[b[n]\,b[m]] = \sigma_b^2\,\delta[n - m]$. Per esempio simboli $\pm A$ equiprobabili, con $\sigma_b^2 = A^2$.
- **(H2)** $D$ è un ritardo casuale uniforme in $[0, T)$, indipendente dai simboli. Modella il fatto che chi osserva il segnale non conosce l'istante in cui inizia ogni simbolo.
- **(H3)** $p(t)$ è un impulso reale di energia finita $E_p = \int p^2(t)\,dt$.

**Passo 0 — Cosa dice davvero «incorrelati, di varianza $\sigma_b^2$» (H1).** Due variabili sono incorrelate se la loro covarianza è nulla:

$$
\operatorname{Cov}(b[n], b[m]) = E[b[n]\,b[m]] - E[b[n]]\,E[b[m]] = 0 \quad (n \neq m)
$$

Con $E[b[n]] = 0$ il secondo termine sparisce: $E[b[n]\,b[m]] = 0$ per $n \neq m$. Per $n = m$ la varianza è $\operatorname{Var}(b[n]) = E[b^2[n]] - E[b[n]]^2 = E[b^2[n]] = \sigma_b^2$. Le due righe si riassumono in

$$
E[b[n]\,b[m]] = \sigma_b^2\,\delta[n - m]
$$

con $\delta[k] = 1$ per $k = 0$ e $0$ altrimenti. È l'unica proprietà dei simboli che serve (non serve che siano indipendenti, né $\pm A$).

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
**Passo 2, riga per riga.**

*(a) Prodotto di due somme.* Si usano due indici diversi, $n$ per $X(t)$ e $m$ per $X(t-\tau)$, altrimenti si perdono i termini misti:

$$
X(t)\,X(t-\tau) = \sum_n\sum_m b[n]\,b[m]\;p(t - nT - D)\;p(t - \tau - mT - D)
$$

*(b) Valore atteso.* Per linearità il valore atteso entra nelle somme. I simboli sono indipendenti da $D$ (H2), quindi il valore atteso del prodotto si spezza in quello dei simboli per quello di $D$:

$$
E\big[b[n]\,b[m]\;g(D)\big] = E[b[n]\,b[m]]\;E[g(D)], \qquad g(D) = p(t - nT - D)\,p(t - \tau - mT - D)
$$

*(c) Si azzerano i termini con $m \neq n$.* Dal passo 0, $E[b[n]\,b[m]] = \sigma_b^2\,\delta[n-m]$: la doppia somma diventa una somma singola, con $m = n$.

*(d) Media su $D$.* $D$ è uniforme in $[0, T)$, con densità $1/T$ in quell'intervallo, quindi $E[g(D)] = \frac1T\int_0^T g(d)\,dd$.

*(e) Cambio di variabile.* Per ogni $n$ si pone $u = t - nT - d$. Allora $t - \tau - nT - d = u - \tau$ e $dd = -du$. Gli estremi: $d = 0 \Rightarrow u = t - nT$, $d = T \Rightarrow u = t - (n+1)T$. Il segno meno si assorbe scambiando gli estremi:

$$
\int_0^T p(t - nT - d)\,p(t - \tau - nT - d)\,dd = \int_{t-(n+1)T}^{t-nT} p(u)\,p(u - \tau)\,du
$$

*(f) Somma su $n$.* Gli intervalli $[\,t-(n+1)T,\; t-nT\,)$ sono adiacenti, di lunghezza $T$ ciascuno: per $n \to +\infty$ vanno verso $-\infty$, per $n \to -\infty$ verso $+\infty$. Coprono tutto $\mathbb{R}$ senza sovrapporsi, quindi la somma degli integrali è un solo integrale su $\mathbb{R}$. Il $t$ è sparito: è questo che rende il processo WSS. La sparizione è l'effetto di $D$ (vedi la nota finale).

$r_{pp}(\tau) = p(\tau) \ast p(-\tau)$ è l'autocorrelazione deterministica dell'impulso (la stessa $r_{hh}$ di [[processi-e-sistemi-lti]]). Il risultato **non dipende da $t$**, e la media è costante: il processo è **WSS**.

**Passo 3 — PSD (Wiener-Khinchin).**
$$
\begin{aligned}
S_{XX}(f) &= \frac{\sigma_b^2}{T}\,\mathcal{F}\big[p(\tau) * p(-\tau)\big] = \frac{\sigma_b^2}{T}\,P(f)\,P(-f) && \text{convoluzione} \to \text{prodotto; riflessione} \\
&= \frac{\sigma_b^2}{T}\,|P(f)|^2 && p \text{ reale: } P(-f) = P^*(f)
\end{aligned}
$$
**Passo 3, riga per riga.** $r_{pp}(\tau) = \int p(u)\,p(u-\tau)\,du$ è una convoluzione: ponendo $q(x) = p(-x)$ si ha $q(\tau - u) = p(u - \tau)$, quindi $r_{pp} = p \ast q$. Le due proprietà di Fourier usate sono

$$
\mathcal{F}[p \ast q] = P(f)\,Q(f), \qquad Q(f) = \mathcal{F}[p(-x)] = P(-f) = P^\ast(f) \ \ (p \text{ reale})
$$

La seconda vale perché $P(-f) = \int p(t)\,e^{+j2\pi f t}\,dt = \big(\int p(t)\,e^{-j2\pi f t}\,dt\big)^\ast$ con $p$ reale. Il prodotto è $P(f)\,P^\ast(f) = |P(f)|^2$. Il fattore costante $\sigma_b^2/T$ esce dalla trasformata.

> 🧮 Risultato: $S_{XX}(f) = \dfrac{\sigma_b^2}{T}\,|P(f)|^2$. La **forma** dello spettro la decide l'impulso, il **livello** la varianza dei simboli per simbolo al secondo ($1/T$).

**Passo 4 — Impulso rettangolare**, come nell'esempio della modulazione binaria: $p(t) = \text{rect}\big((t - T/2)/T\big)$, altezza 1 e durata $T$.
$$
\begin{aligned}
|P(f)|^2 &= T^2\,\text{sinc}^2(fT) && \text{impulso centrato: } T\,\text{sinc}(fT) \text{ (modulazione-digitale); il ritardo } T/2 \text{ aggiunge } e^{-j\pi fT}, \text{ di modulo 1} \\
S_{XX}(f) &= \sigma_b^2\,T\,\text{sinc}^2(fT) && \text{sostituisco} \\
R_{XX}(\tau) &= \sigma_b^2\Big(1 - \frac{|\tau|}{T}\Big)\ \text{per } |\tau| < T,\ 0 \text{ altrove} && r_{pp}(\tau) = T - |\tau|: \text{ sovrapposizione di due rettangoli sfasati di } \tau
\end{aligned}
$$

**Passo 4, riga per riga.**

*(a) Trasformata dell'impulso* $p(t) = 1$ per $0 \le t \le T$, $0$ altrove:

$$
\begin{aligned}
P(f) &= \int_0^T e^{-j2\pi f t}\,dt = \frac{1 - e^{-j2\pi f T}}{j2\pi f} && \text{integrale di un'esponenziale} \\
&= e^{-j\pi f T}\,\frac{e^{j\pi f T} - e^{-j\pi f T}}{j2\pi f} && \text{raccolgo } e^{-j\pi f T} \\
&= e^{-j\pi f T}\,\frac{\sin(\pi f T)}{\pi f} = T\,\text{sinc}(fT)\,e^{-j\pi f T} && \text{Eulero; } \text{sinc}(x) = \tfrac{\sin(\pi x)}{\pi x}
\end{aligned}
$$

Il modulo quadro cancella la fase: $|P(f)|^2 = T^2\,\text{sinc}^2(fT)$, e quindi $S_{XX}(f) = \frac{\sigma_b^2}{T}\,T^2\,\text{sinc}^2(fT) = \sigma_b^2\,T\,\text{sinc}^2(fT)$.

*(b) Autocorrelazione dell'impulso*: $r_{pp}(\tau) = \int p(u)\,p(u-\tau)\,du$. Per $0 \le \tau \le T$, $p(u-\tau)$ vale 1 su $[\tau, \tau+T]$ e $p(u)$ su $[0, T]$: si sovrappongono su $[\tau, T]$, lunghezza $T - \tau$. Per $\tau < 0$ si ottiene lo stesso per simmetria, e per $|\tau| > T$ non c'è sovrapposizione:

$$
r_{pp}(\tau) = (T - |\tau|)\ \ (|\tau| < T), \qquad R_{XX}(\tau) = \frac{\sigma_b^2}{T}\,(T - |\tau|) = \sigma_b^2\Big(1 - \frac{|\tau|}{T}\Big)
$$

*(c) Integrale della sinc al quadrato* (usato per la potenza): $\int_{-\infty}^{+\infty}\text{sinc}^2(fT)\,df = \frac1T$, quindi $\int S_{XX}\,df = \sigma_b^2\,T\cdot\frac1T = \sigma_b^2 = R_{XX}(0)$, come richiede la proprietà 2.

**Verifiche:**
- **Potenza:** $R_{XX}(0) = \sigma_b^2$, cioè simboli di varianza $\sigma_b^2$ sempre "accesi". E $\int \sigma_b^2 T\,\text{sinc}^2(fT)\,df = \sigma_b^2 T\cdot\frac{1}{T} = \sigma_b^2$ ✓ (proprietà 2).
- **Valore in zero:** $S_{XX}(0) = \sigma_b^2 T$ = area del triangolo $R_{XX}$ (altezza $\sigma_b^2$, base $2T$) ✓ (proprietà 1).
- $S_{XX} \ge 0$ e pari ✓ (proprietà 3–4).
- **Zeri** in $f = k/T$, $k \neq 0$: il lobo principale è largo $2/T$. Raddoppiando la velocità di simbolo $1/T$ raddoppia la banda occupata.

**Risultato:** $S_{XX}(f) = \sigma_b^2\,T\,\text{sinc}^2(fT)$ [W/Hz se $\sigma_b^2$ è in W]. Con simboli $\pm A$ equiprobabili: $A^2 T\,\text{sinc}^2(fT)$.

> 💡 Connessione: la PSD decresce solo come $1/f^2$ lontano dall'origine, perché l'impulso rettangolare **non è a banda limitata** ([[modulazione-digitale]]). È il motivo per cui la slide 2 della lezione sulla banda base dice che le forme d'onda reali sono spesso vincolate in frequenza.

> 🧩 Perché serve il ritardo $D$: senza $D$, $R_{XX}(t, \tau) = \sigma_b^2\sum_n p(t - nT)\,p(t - \tau - nT)$ dipende da $t$, in modo periodico con periodo $T$. Il processo non sarebbe WSS e non si potrebbe applicare Wiener-Khinchin come enunciato a p. 32. Mediare su $D$ uniforme equivale a mediare $R_{XX}(t, \tau)$ su un periodo in $t$, e dà lo stesso risultato.

## Trappole

- **Non verificare la WSS**: senza ritardo casuale (o media su un periodo) l'autocorrelazione dipende da $t$.
- **$|P(f)|^2$, non $P(f)$**: la PSD è reale e non negativa, e la fase dell'impulso sparisce.
- **Il fattore $1/T$**: la PSD è potenza per unità di frequenza; con simboli più frequenti c'è più energia al secondo.
- **Media nulla dei simboli (H1)**: con simboli $\pm A$ **non** equiprobabili la media non è nulla e la derivazione non vale così com'è ($E[b[n]b[m]] \neq 0$ per $n \neq m$).
- **Banda e primo zero**: il lobo principale va da $-1/T$ a $1/T$. Dire che "la banda è $1/T$" è una convenzione, perché lo spettro non si annulla mai del tutto.

_Aggiornato: 2026-10-28 — passaggi del caso 1 resi espliciti riga per riga (passo 0, dettagli dei passi 2, 3, 4); 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-09-28 — creazione da ingest random_processes.pdf (esempio della slide 32)_
