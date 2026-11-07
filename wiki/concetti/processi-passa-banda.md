---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso", "segnale-analitico", "stazionarieta", "processi-e-sistemi-lti", "momenti-di-un-processo"]
fonti_pdf: ["Rappresentazione_Rice_processi.pdf#page=2", "Rappresentazione_Rice_processi.pdf#page=4", "Rappresentazione_Rice_processi.pdf#page=6", "Rappresentazione_Rice_processi.pdf#page=10", "Rappresentazione_Rice_processi.pdf#page=11"]
---

# Processi passa-banda: inviluppo complesso e componenti in quadratura

## Definizione · [[Rappresentazione_Rice_processi.pdf#page=2|p. 2]], [[Rappresentazione_Rice_processi.pdf#page=3|3]]

Si lavora con processi aleatori **reali** (ipotesi «non troppo restrittiva»), **WSS** ([[stazionarieta]]) e **a media nulla** ($\mu_x = E[x(t)] = 0$).

- $x_b(t)$ è **in banda base** se la sua PSD ([[densita-spettrale-di-potenza]]) è limitata attorno all'origine: $S_{x_bx_b}(f) = 0$ per $|f| > W > 0$.
- $x_p(t)$ è **passa-banda** se la sua PSD è concentrata attorno alle frequenze $\pm f_c$: $S_{x_px_p}(f) = 0$ per $|f \pm f_c| > W > 0$, con $f_c \gg W$ (appunti).

> ⚠️ Convenzione su $W$: qui $W$ è la **semilarghezza** di ogni lobo (lo spettro è non nullo per $|f - f_c| \le W$). Nelle slide successive ([[psd-componenti-in-quadratura]], [[rumore-in-banda-passante]]) $W$ è invece la **larghezza** del lobo, con inviluppo in banda base per $|f| < W/2$. Il significato va sempre letto dal contesto.

Come per i segnali deterministici ([[segnale-analitico]]) si costruisce il **processo analitico**, che elimina la ridondanza delle frequenze negative:

$$x_p^+(t) = \frac{1}{\sqrt2}\,x_p(t) + \frac{j}{\sqrt2}\,\widehat{x}_p(t)$$

dove $\widehat{x}_p(t)$ è la **trasformata di Hilbert** del processo, uscita del filtro di Hilbert ideale con risposta impulsiva $h(t) = \frac{1}{\pi t}$ e risposta in frequenza $H(f) = -j\,\text{sgn}(f)$ ($-j$ per $f > 0$, $+j$ per $f < 0$).

L'**inviluppo complesso** del processo è, in modo omologo al caso deterministico ([[inviluppo-complesso]]):

$$x(t) \triangleq x_p^+(t)\,e^{-j2\pi f_ct} = x_c(t) + jx_s(t) \tag{1}$$

È una **traslazione in frequenza** del processo che centra la PSD nell'origine. $x_c(t)$ è la componente **in fase** e $x_s(t)$ quella **in quadratura** di $x_p$; entrambe sono processi aleatori reali in banda base.

## Formule · [[Rappresentazione_Rice_processi.pdf#page=4|p. 4]]–[[Rappresentazione_Rice_processi.pdf#page=6|6]], [[Rappresentazione_Rice_processi.pdf#page=10|10]]–[[Rappresentazione_Rice_processi.pdf#page=11|11]]

| Formula | Significato |
|---|---|
| $x_p(t) = \sqrt2\,x_c(t)\cos(2\pi f_ct) - \sqrt2\,x_s(t)\sin(2\pi f_ct)$ | ritorno al passa-banda: $x_p = \sqrt2\,\text{Re}\{x\,e^{j2\pi f_ct}\}$ |
| $x_c(t) = \frac{1}{\sqrt2}\big[x_p(t)\cos(2\pi f_ct) + \widehat{x}_p(t)\sin(2\pi f_ct)\big]$ | componente in fase |
| $x_s(t) = \frac{1}{\sqrt2}\big[-x_p(t)\sin(2\pi f_ct) + \widehat{x}_p(t)\cos(2\pi f_ct)\big]$ | componente in quadratura |
| $S_{\widehat{x}_p\widehat{x}_p} = S_{x_px_p}$, $\ R_{\widehat{x}_p\widehat{x}_p}(\tau) = R_{x_px_p}(\tau)$ | (2) |
| $S_{\widehat{x}_px_p} = -j\,\text{sgn}(f)\,S_{x_px_p}$, $\ R_{\widehat{x}_px_p}(\tau) = \widehat{R}_{x_px_p}(\tau)$ | (3) |
| $S_{x_p\widehat{x}_p} = j\,\text{sgn}(f)\,S_{x_px_p}$, $\ R_{x_p\widehat{x}_p}(\tau) = -\widehat{R}_{x_px_p}(\tau)$ | (4) |
| $2R_{x_cx_c}(\tau) = R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau)$ | (6) |
| $2R_{x_cx_s}(\tau) = R_{x_px_p}(\tau)\sin(2\pi f_c\tau) - \widehat{R}_{x_px_p}(\tau)\cos(2\pi f_c\tau)$ | (8) |
| $R_{x_cx_c} = R_{x_sx_s}$, $\ R_{x_cx_s} = -R_{x_sx_c}$ | (10) |
| $R_{xx}(\tau) = 2R_{x_cx_c}(\tau) + 2j\,R_{x_sx_c}(\tau)$ | (12): acf dell'inviluppo |

> 🧮 Formula chiave: per un processo passa-banda WSS a media nulla, $x_c$ e $x_s$ sono congiuntamente WSS, con $R_{x_cx_c} = R_{x_sx_s}$ e $R_{x_cx_s} = -R_{x_sx_c}$.

Simboli: $R_{ab}(\tau) = E[a(t)\,b(t-\tau)]$ (acf per $a = b$, crosscorrelazione altrimenti; per l'inviluppo complesso $R_{xx}(\tau) = E[x(t)\,x^\ast(t-\tau)]$); $\widehat{R}$ = trasformata di Hilbert di $R$, cioè $R \ast \frac{1}{\pi\tau}$; $f_c$ [Hz] frequenza portante; $\tau$ [s] ritardo. Ipotesi: $x_p$ reale, WSS, media nulla.

## Derivazioni

### Derivazione — $x_c$ e $x_s$ hanno media nulla · [[Rappresentazione_Rice_processi.pdf#page=7|p. 7]]
**Fonte:** appunti, enunciato del teorema («se $x_p$ è WSS a media nulla, le sue componenti in banda base sono congiuntamente WSS a media nulla»).
**Si parte da:** $E[x_p(t)] = 0$ per ipotesi e $\widehat{x}_p = x_p \ast \frac{1}{\pi t}$.

$$
\begin{aligned}
E[\widehat{x}_p(t)] &= E\Big[\int_{-\infty}^{+\infty} x_p(t-\tau)\,\frac{1}{\pi\tau}\,d\tau\Big] && \text{definizione di } \widehat{x}_p \\
&= \int_{-\infty}^{+\infty} E[x_p(t-\tau)]\,\frac{1}{\pi\tau}\,d\tau = 0 && \text{valore atteso e integrale si scambiano; } E[x_p] = 0
\end{aligned}
$$

> 🧩 L'integrale è un valore principale di Cauchy intorno a $\tau = 0$; qui basta che il suo integrando sia nullo. In pratica: un filtro LTI di risposta $H(f)$ dà $\mu_y = \mu_x H(0)$ ([[processi-e-sistemi-lti]]), e se $\mu_x = 0$ la media resta zero.

Poiché $x_c$ e $x_s$ sono combinazioni di $x_p$ e $\widehat{x}_p$ con coefficienti deterministici $\cos$ e $\sin$:

$$E[x_c(t)] = \tfrac{1}{\sqrt2}\big(E[x_p]\cos + E[\widehat{x}_p]\sin\big) = 0, \qquad E[x_s(t)] = 0$$

Una media costante (nulla) è la prima metà della WSS; resta da mostrare che le correlazioni dipendono solo da $\tau$.

### Derivazione — Relazioni (2), (3), (4) tra $x_p$ e $\widehat{x}_p$ · [[Rappresentazione_Rice_processi.pdf#page=6|p. 6]], [[Rappresentazione_Rice_processi.pdf#page=7|7]]
**Fonte:** slide e appunti: relazioni date con la sola indicazione «ricordando $S_{yy} = S_{xx}|H|^2$ e $R_{yy} = R_{xx} \ast h \ast h(-\tau)$».
**Si parte da:** [[processi-e-sistemi-lti]] — uscita $y = x \ast h$ di un filtro LTI con ingresso WSS: $S_{yy} = |H|^2 S_{xx}$ e $S_{yx} = H\,S_{xx}$.

> 🧩 Derivazione mia del passo sulla crosscorrelazione: $R_{yx}(\tau) = E[y(t)\,x(t-\tau)] = \int h(u)\,E[x(t-u)\,x(t-\tau)]\,du = \int h(u)\,R_{xx}(\tau - u)\,du = (h \ast R_{xx})(\tau)$, quindi in frequenza $S_{yx} = H\,S_{xx}$.

Qui $x = x_p$, $y = \widehat{x}_p$, $H(f) = -j\,\text{sgn}(f)$, con $|H(f)|^2 = 1$ per $f \ne 0$:

$$
\begin{aligned}
S_{\widehat{x}_p\widehat{x}_p}(f) &= |{-j}\,\text{sgn}(f)|^2\,S_{x_px_p}(f) = S_{x_px_p}(f) && |H|^2 = 1 \ (f \ne 0) \\
&\Rightarrow R_{\widehat{x}_p\widehat{x}_p}(\tau) = R_{x_px_p}(\tau) && \text{antitrasformata, (2)} \\
S_{\widehat{x}_px_p}(f) &= -j\,\text{sgn}(f)\,S_{x_px_p}(f) && S_{yx} = H\,S_{xx} \\
&\Rightarrow R_{\widehat{x}_px_p}(\tau) = \big(R_{x_px_p} \ast \tfrac{1}{\pi\tau}\big)(\tau) = \widehat{R}_{x_px_p}(\tau) && \text{(3): moltiplicare per } -j\,\text{sgn} \text{ = trasformata di Hilbert} \\
S_{x_p\widehat{x}_p}(f) &= S_{\widehat{x}_px_p}^\ast(f) = j\,\text{sgn}(f)\,S_{x_px_p}(f) && S_{xy} = S_{yx}^\ast; \ S_{x_px_p} \text{ reale} \\
&\Rightarrow R_{x_p\widehat{x}_p}(\tau) = -\widehat{R}_{x_px_p}(\tau) && \text{(4)}
\end{aligned}
$$

**Sanity check:** $\widehat{R}$ è dispari perché $R_{x_px_p}$ è pari; allora $R_{x_p\widehat{x}_p}(\tau) = R_{\widehat{x}_px_p}(-\tau) = \widehat{R}(-\tau) = -\widehat{R}(\tau)$, coerente con la (4).
**Ipotesi:** $x_p$ WSS reale; $f = 0$ ha misura nulla e non influisce sulle antitrasformate.

### Derivazione — Autocorrelazione di $x_c$, eq. (5)–(6) · [[Rappresentazione_Rice_processi.pdf#page=8|p. 8]], [[Rappresentazione_Rice_processi.pdf#page=10|10]]
**Fonte:** appunti p. 8, la slide ne dà il risultato. Riporto i passaggi a parole.
**Si parte da:** $x_c(t) = \frac{1}{\sqrt2}\big[x_p(t)\cos a + \widehat{x}_p(t)\sin a\big]$ con $a = 2\pi f_ct$, e $b = 2\pi f_c(t-\tau)$.

$$
\begin{aligned}
2R_{x_cx_c}(t,\tau) &= 2E[x_c(t)\,x_c(t-\tau)] && \text{definizione} \\
&= E\big[\big(x_p(t)\cos a + \widehat{x}_p(t)\sin a\big)\big(x_p(t-\tau)\cos b + \widehat{x}_p(t-\tau)\sin b\big)\big] && \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2} = \tfrac12 \text{ portato a sinistra} \\
&= R_{x_px_p}\cos a\cos b + R_{x_p\widehat{x}_p}\cos a\sin b + R_{\widehat{x}_px_p}\sin a\cos b + R_{\widehat{x}_p\widehat{x}_p}\sin a\sin b && \text{(5): cos e sin deterministici escono dal valore atteso} \\
&= R_{x_px_p}(\cos a\cos b + \sin a\sin b) + \widehat{R}_{x_px_p}(\sin a\cos b - \cos a\sin b) && \text{(2), (3), (4)} \\
&= R_{x_px_p}(\tau)\cos(a-b) + \widehat{R}_{x_px_p}(\tau)\sin(a-b) && \text{formule di addizione} \\
&= R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau) && a - b = 2\pi f_c\tau \ \text{(6)}
\end{aligned}
$$

Il tempo $t$ è sparito: $R_{x_cx_c}(t,\tau) = R_{x_cx_c}(\tau)$. Gli appunti usano le **formule di Werner** (prodotti di seno e coseno come somme) per arrivare allo stesso risultato.

### Derivazione — $x_s$ e mutue, eq. (7)–(9) · [[Rappresentazione_Rice_processi.pdf#page=8|p. 8]], [[Rappresentazione_Rice_processi.pdf#page=10|10]]
**Fonte:** appunti p. 8: «ripetendo gli stessi passaggi per $x_s$ e per la mutua correlazione si ricava».
**Si parte da:** $x_s(t) = \frac{1}{\sqrt2}\big[-x_p(t)\sin a + \widehat{x}_p(t)\cos a\big]$.

$$
\begin{aligned}
2R_{x_sx_s}(t,\tau) &= R_{x_px_p}\sin a\sin b - R_{x_p\widehat{x}_p}\sin a\cos b - R_{\widehat{x}_px_p}\cos a\sin b + R_{\widehat{x}_p\widehat{x}_p}\cos a\cos b && \text{prodotto delle due espressioni} \\
&= R_{x_px_p}\cos(a-b) + \widehat{R}_{x_px_p}\sin(a-b) = 2R_{x_cx_c}(\tau) && \text{(2), (3), (4)} \\
2R_{x_cx_s}(t,\tau) &= -R_{x_px_p}\cos a\sin b + R_{x_p\widehat{x}_p}\cos a\cos b - R_{\widehat{x}_px_p}\sin a\sin b + R_{\widehat{x}_p\widehat{x}_p}\sin a\cos b && x_c(t)\,x_s(t-\tau) \\
&= R_{x_px_p}\sin(a-b) - \widehat{R}_{x_px_p}\cos(a-b) && \text{(2), (3), (4)} \\
&= R_{x_px_p}(\tau)\sin(2\pi f_c\tau) - \widehat{R}_{x_px_p}(\tau)\cos(2\pi f_c\tau) && \text{(8)} \\
2R_{x_sx_c}(t,\tau) &= -R_{x_px_p}\sin(2\pi f_c\tau) + \widehat{R}_{x_px_p}\cos(2\pi f_c\tau) = -2R_{x_cx_s}(\tau) && \text{(9): stessi passaggi, segni scambiati}
\end{aligned}
$$

Tutte le funzioni dipendono solo da $\tau$: $x_c$ e $x_s$ sono **congiuntamente WSS**, e valgono le condizioni (10). ∎

> 🧩 Verifica di coerenza (conversione inversa): da $x_p = \sqrt2(x_c\cos a - x_s\sin a)$ e (10), $R_{x_px_p}(t,\tau) = 2R_{x_cx_c}(\tau)\cos(a-b) + 2R_{x_cx_s}(\tau)\sin(a-b)$. Sostituendo (6) e (8): $R_{x_px_p}(\cos^2 + \sin^2) + \widehat{R}_{x_px_p}(\sin\cos - \cos\sin) = R_{x_px_p}(\tau)$ ✓, indipendente da $t$. Le (10) sono proprio ciò che serve perché i termini periodici in $t$ si cancellino.

### Derivazione — Autocorrelazione dell'inviluppo, eq. (11)–(12) · [[Rappresentazione_Rice_processi.pdf#page=9|p. 9]], [[Rappresentazione_Rice_processi.pdf#page=11|11]]
**Fonte:** appunti p. 9 e slide 6.
**Si parte da:** $x = x_c + jx_s$ e $R_{xx}(\tau) = E[x(t)\,x^\ast(t-\tau)]$ (il coniugato serve perché $x$ è complesso).

$$
\begin{aligned}
R_{xx}(\tau) &= E\big[(x_c(t) + jx_s(t))(x_c(t-\tau) - jx_s(t-\tau))\big] && x^\ast = x_c - jx_s \\
&= R_{x_cx_c}(\tau) + R_{x_sx_s}(\tau) + j\big[R_{x_sx_c}(\tau) - R_{x_cx_s}(\tau)\big] && \text{(11): sviluppo e raccolgo } j \\
&= 2R_{x_cx_c}(\tau) + 2j\,R_{x_sx_c}(\tau) && \text{(10): } R_{x_sx_s} = R_{x_cx_c},\ R_{x_cx_s} = -R_{x_sx_c} \ \text{(12)}
\end{aligned}
$$

La parte reale è **2× l'autocorrelazione di $x_c$**, la parte immaginaria è **2× la mutua correlazione** $R_{x_sx_c}$ (appunti).

### Derivazione — Perché $R_{x_cx_s}(0) = 0$ · [[Rappresentazione_Rice_processi.pdf#page=9|p. 9]], [[Rappresentazione_Rice_processi.pdf#page=11|11]]
**Fonte:** appunti p. 9, che rispondono al «Perché?» della slide 6.
**Si parte da:** $R_{xx}(0) = E[|x(t)|^2] = P_x$ è una quantità **reale**.

$$
\begin{aligned}
R_{xx}(0) &= 2R_{x_cx_c}(0) + 2j\,R_{x_sx_c}(0) \in \mathbb{R} && \text{(12) con } \tau = 0 \\
&\Rightarrow R_{x_sx_c}(0) = 0 && \text{la parte immaginaria deve annullarsi} \\
&\Rightarrow R_{x_cx_s}(0) = -R_{x_sx_c}(0) = 0 && \text{(10)}
\end{aligned}
$$

> 🧩 Seconda strada, senza passare da $R_{xx}$: spostando l'origine dei tempi, $R_{x_sx_c}(\tau) = E[x_s(t)\,x_c(t-\tau)] = R_{x_cx_s}(-\tau)$; con la (10) si ha $R_{x_cx_s}(\tau) = -R_{x_cx_s}(-\tau)$, cioè $R_{x_cx_s}$ è **dispari**, quindi nulla in $\tau = 0$.

Con medie nulle la covarianza coincide con la correlazione: $C_{x_cx_s}(0) = R_{x_cx_s}(0) - \mu_{x_c}\mu_{x_s} = 0$. Quindi per ogni $t_0$ le variabili aleatorie a media nulla $x_c(t_0)$ e $x_s(t_0)$ sono **incorrelate**; se sono **congiuntamente gaussiane** ([[processo-gaussiano]]) sono anche **statisticamente indipendenti**.

> 🧩 Per $x_p$ gaussiano, $\widehat{x}_p$ è uscita di un filtro lineare e $x_c$, $x_s$ sono combinazioni lineari di $x_p$ e $\widehat{x}_p$ con coefficienti deterministici: congiuntamente gaussiane (proprietà del processo gaussiano, [[processo-gaussiano]]).

## Spiegazione

Un processo passa-banda $x_p$ oscilla alla portante $f_c$ con ampiezza e fase che variano lentamente; l'inviluppo complesso $x = x_c + jx_s$ raccoglie queste variazioni e vive in banda base, a una frequenza molto più bassa. È lo stesso passaggio fatto nel caso deterministico ([[inviluppo-complesso]]), con una novità: ora i segnali sono aleatori, e bisogna chiedersi **se le proprietà statistiche si conservano**.

La risposta del teorema è sì, con una struttura precisa. La portante $\cos(2\pi f_ct)$ è periodica in $t$, quindi $x_p = \sqrt2\,x_c\cos - \sqrt2\,x_s\sin$ è WSS solo se $x_c$ e $x_s$ hanno le stesse acf e crosscorrelazioni opposte: allora i termini che dipendono da $t$ si cancellano (verifica 🧩 sopra). La trasformata di Hilbert entra perché fornisce il «complice» in quadratura di $x_p$: $x_p$ da sola non basta a ricavare entrambe le componenti.

Il risultato più utile è che, **nello stesso istante**, $x_c$ e $x_s$ sono incorrelate. Che lo siano **a istanti diversi** non segue in generale: se $R_{x_sx_c}(\tau) \neq 0$ per $\tau \neq 0$, l'inviluppo ha una parte immaginaria correlata con quella reale ([[psd-componenti-in-quadratura]] studia quando questo accade).

## Perché importa

Segnali e rumore reali sono passa-banda e aleatori. Per progettare il ricevitore, il DSP lavora sull'inviluppo complesso in banda base ([[inviluppo-complesso]], [[upconversion-e-downconversion]]): serve sapere che statistica ha. In particolare, per il rumore gaussiano passa-banda ([[rumore-in-banda-passante]]) le due componenti in quadratura nello stesso istante sono **gaussiane indipendenti**.

## Connessioni

- [[inviluppo-complesso]] — stessa definizione, ma per segnali deterministici; qui il teorema sulla WSS è la novità.
- [[segnale-analitico]] — il processo analitico $x_p^+$ è il segnale analitico applicato a un processo; il $\sqrt2$ conserva la potenza.
- [[processi-e-sistemi-lti]] — le relazioni (2)–(4) sono l'applicazione del filtro di Hilbert.
- [[stazionarieta]] — il teorema dice quando la WSS passa dal processo passa-banda alle componenti.
- [[momenti-di-un-processo]] — incoerenza, incorrelazione e indipendenza delle componenti; $R_{xx}$ per processi complessi con il coniugato.
- [[processo-gaussiano]] — incorrelate ⇒ indipendenti.
- [[psd-componenti-in-quadratura]] — la stessa analisi in frequenza.

## Fonti · [[Rappresentazione_Rice_processi.pdf#page=2|p. 2]]–[[Rappresentazione_Rice_processi.pdf#page=11|11]]

[[rappresentazione-processi-passa-banda]] — Rappresentazione_Rice_processi.pdf, slide 2–6 e appunti.

_Aggiornato: 2026-11-01 — creazione da ingest Rappresentazione_Rice_processi.pdf_
