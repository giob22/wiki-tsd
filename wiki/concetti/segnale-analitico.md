---
tipo: concetto
importanza_esame: alta
prerequisiti: ["segnali-banda-base-e-passa-banda"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=10", "Rappresentazione_Rice.pdf#page=11", "Rappresentazione_Rice.pdf#page=12"]
---

# Segnale analitico e trasformata di Hilbert

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=10]] (slide 8)

Dato un segnale passa-banda $s_p(t)$ con trasformata $S_p(f)$, il **segnale analitico** (*analytical signal*) associato ha trasformata
$$S_p^+(f) = \sqrt{2}\,S_p(f)\,u(f) \tag{3}$$
dove $u(\cdot)$ è il gradino unitario. In parole: si **tengono solo le frequenze positive** di $S_p(f)$ e le si moltiplica per $\sqrt2$.

- Nota a mano sul $\sqrt2$ ([[Rappresentazione_Rice.pdf#page=10]]): è «introdotto per motivi energetici». Il motivo è ricavato in [[#Derivazione — Perché proprio √2]].
- Ogni segnale passa-banda ha **un unico** segnale analitico, e viceversa ([[Rappresentazione_Rice.pdf#page=10]]).

La **trasformata di Hilbert** di $s_p(t)$ ([[Rappresentazione_Rice.pdf#page=11]], slide 9) è
$$\widehat{s}_p(t) \triangleq s_p(t) * \frac{1}{\pi t} = \int_{-\infty}^{+\infty}\frac{s_p(\tau)}{\pi(t - \tau)}\,d\tau \tag{9}$$
e nel tempo il segnale analitico si scrive con essa:
$$s_p^+(t) = \frac{1}{\sqrt2}\,s_p(t) + \frac{j}{\sqrt2}\,\widehat{s}_p(t) \tag{8}$$

> 🧩 Precisazione mia: l'integrale (9) va inteso come **valore principale di Cauchy**, perché $1/(t - \tau)$ diverge in $\tau = t$.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$ | segnale analitico, eq. (3) | [[Rappresentazione_Rice.pdf#page=10]] (slide 8) |
| $s_p^+(t) = \mathcal{F}^{-1}[S_p^+(f)] = \sqrt2\,s_p(t) * \mathcal{F}^{-1}[u(f)]$ | eq. (4) | [[Rappresentazione_Rice.pdf#page=10]] (slide 8) |
| $\mathcal{F}[u(t)] = \frac12\delta(f) + \frac{1}{j2\pi f} \triangleq \text{U}(f)$ | eq. (5) | [[Rappresentazione_Rice.pdf#page=10]] (slide 8) |
| $\mathcal{F}[\text{U}(t)] = u(-f)$ | dualità, eq. (6) | [[Rappresentazione_Rice.pdf#page=10]] (slide 8) |
| $\mathcal{F}^{-1}[u(f)] = \text{U}(-t) = \frac12\delta(t) + \frac{j}{2\pi t}$ | eq. (7) | [[Rappresentazione_Rice.pdf#page=11]] (slide 9) |
| $s_p^+(t) = \frac{1}{\sqrt2}s_p(t) + \frac{j}{\sqrt2}\widehat{s}_p(t)$ | eq. (8) | [[Rappresentazione_Rice.pdf#page=11]] (slide 9) |
| $\widehat{s}_p(t) = s_p(t) * \frac{1}{\pi t}$ | trasformata di Hilbert, eq. (9) | [[Rappresentazione_Rice.pdf#page=11]] (slide 9) |
| $s_p(t) = \sqrt2\,\text{Re}\{s_p^+(t)\}$ | ritorno al segnale reale, eq. (10) | [[Rappresentazione_Rice.pdf#page=12]] (slide 10) |
| $S_p^+(f) = \frac{1}{\sqrt2}S_p(f) + \frac{j}{\sqrt2}\mathcal{F}[\widehat{s}_p(t)]$ | eq. (11) | [[Rappresentazione_Rice.pdf#page=12]] (slide 10) |
| $\widehat{S}_p(f) = S_p(f)\,\mathcal{F}\!\left[\frac{1}{\pi t}\right]$ | eq. (12) | [[Rappresentazione_Rice.pdf#page=12]] (slide 10) |
| $\mathcal{F}[\text{sgn}(t)] = \frac{1}{j\pi f}$, $\ \mathcal{F}\!\left[\frac{1}{\pi t}\right] = j\,\text{sgn}(-f)$ | trasformate ausiliarie | [[Rappresentazione_Rice.pdf#page=12]] (slide 10) |
| $\widehat{S}_p(f) = -j\,S_p(f)\,\text{sgn}(f)$ | Hilbert in frequenza | [[Rappresentazione_Rice.pdf#page=12]] (slide 10) |

Simboli: $u(\cdot)$ = gradino unitario; $\text{U}(f)$ = sua trasformata; $\delta$ = delta di Dirac; $\text{sgn}$ = funzione segno; $*$ = convoluzione; $\mathcal{F}$, $\mathcal{F}^{-1}$ = trasformata e antitrasformata di Fourier; $\widehat{s}_p$ = trasformata di Hilbert, con la stessa unità di $s_p$ (es. V). Anche $s_p^+$ ha l'unità di $s_p$, perché $\sqrt2$ è adimensionale.

> 🧮 Formula chiave: $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$ e $s_p(t) = \sqrt2\,\text{Re}\{s_p^+(t)\}$.

## Derivazioni

### Derivazione — Eq. (4): dal prodotto in frequenza alla convoluzione nel tempo
**Fonte:** [[Rappresentazione_Rice.pdf#page=10]] (slide 8)
$$
\begin{aligned}
s_p^+(t) &= \mathcal{F}^{-1}\big[S_p^+(f)\big] && \text{definizione di } s_p^+(t) \\
&= \mathcal{F}^{-1}\big[\sqrt2\,S_p(f)\cdot u(f)\big] && \text{sostituisco la (3)} \\
&= \sqrt2\,s_p(t) * \mathcal{F}^{-1}[u(f)] && \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
\end{aligned}
$$
Resta da calcolare l'antitrasformata del gradino **in frequenza**.

### Derivazione — Eq. (7): antitrasformata di $u(f)$
**Fonte:** [[Rappresentazione_Rice.pdf#page=11]] (slide 9): «dalla (5) e dalla (6), applicando la riflessione».
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

### Derivazione — Eq. (8): il segnale analitico nel tempo
**Fonte:** [[Rappresentazione_Rice.pdf#page=11]] (slide 9)
$$
\begin{aligned}
s_p^+(t) &= \sqrt2\,s_p(t) * \Big[\tfrac12\,\delta(t) + \frac{j}{2\pi t}\Big] && \text{la (7) nella (4)} \\
&= \frac{\sqrt2}{2}\,s_p(t) + \frac{\sqrt2\,j}{2}\;s_p(t) * \frac{1}{\pi t} && s * \delta = s;\ \tfrac{1}{2\pi t} = \tfrac12\cdot\tfrac{1}{\pi t} \\
&= \frac{1}{\sqrt2}\,s_p(t) + \frac{j}{\sqrt2}\,\widehat{s}_p(t) && \tfrac{\sqrt2}{2} = \tfrac{1}{\sqrt2};\ \text{definizione (9)}
\end{aligned}
$$
Note a mano ([[Rappresentazione_Rice.pdf#page=11]]): $s_p(t)$ è il «segnale reale passa-banda», $\widehat{s}_p(t)$ è la «trasformata di Hilbert di $s_p$».

### Derivazione — Eq. (10) e corrispondenza biunivoca
**Fonte:** [[Rappresentazione_Rice.pdf#page=12]] (slide 10): «dalla (8) si deduce immediatamente… Questo conclude la dimostrazione.»
> 🧩 Derivazione mia dei passaggi

$$
\begin{aligned}
\widehat{s}_p(t) &\in \mathbb{R} && \text{convoluzione di due funzioni reali, } s_p \text{ e } 1/(\pi t) \\
\text{Re}\{s_p^+(t)\} &= \frac{1}{\sqrt2}\,s_p(t) && \text{nella (8) } s_p \text{ e } \widehat{s}_p \text{ sono reali} \\
s_p(t) &= \sqrt2\,\text{Re}\{s_p^+(t)\} && \text{moltiplico per } \sqrt2
\end{aligned}
$$
**Cosa è stato dimostrato**, cioè l'affermazione della slide 8: da $s_p$ si calcola $s_p^+$ con la (8), e da $s_p^+$ si torna a $s_p$ con la (10). La corrispondenza è quindi **biunivoca**: il segnale analitico contiene tutta l'informazione di $s_p$.
Nota a mano sulla (10) ([[Rappresentazione_Rice.pdf#page=12]]): è «legata alla simmetria del segnale reale». La parte negativa dello spettro scartata nella (3) si ricostruisce prendendo la parte reale, proprio perché per un segnale reale è lo specchio coniugato di quella positiva ([[segnali-banda-base-e-passa-banda]]).

### Derivazione — Trasformata di $\text{sgn}(t)$ e di $1/(\pi t)$
**Fonte:** [[Rappresentazione_Rice.pdf#page=12]] (slide 10): risultati dati con un solo passaggio.
> 🧩 Derivazione mia

$$
\begin{aligned}
\text{sgn}(t) &= 2\,u(t) - 1 && \text{vale } +1 \text{ per } t>0 \text{ e } -1 \text{ per } t<0 \\
\mathcal{F}[\text{sgn}(t)] &= 2\Big[\tfrac12\,\delta(f) + \frac{1}{j2\pi f}\Big] - \delta(f) && \text{linearità; eq. (5); } \mathcal{F}[1] = \delta(f) \\
&= \frac{1}{j\pi f} && \text{le delta si cancellano} \\
\mathcal{F}\Big[\frac{1}{j\pi t}\Big] &= \text{sgn}(-f) && \text{dualità} \\
\mathcal{F}\Big[\frac{1}{\pi t}\Big] &= j\,\text{sgn}(-f) = -j\,\text{sgn}(f) && \text{moltiplico per } j;\ \text{sgn è dispari}
\end{aligned}
$$

### Derivazione — Trasformata di Hilbert in frequenza, eq. (12)
**Fonte:** [[Rappresentazione_Rice.pdf#page=12]] (slide 10)
$$
\begin{aligned}
\widehat{S}_p(f) &= \mathcal{F}\Big[s_p(t) * \frac{1}{\pi t}\Big] = S_p(f)\,\mathcal{F}\Big[\frac{1}{\pi t}\Big] && \text{convoluzione} \to \text{prodotto, eq. (12)} \\
&= -j\,\text{sgn}(f)\,S_p(f) && \text{derivazione precedente}
\end{aligned}
$$

> ⚠️ Refuso della slide, corretto a mano nel PDF ([[Rappresentazione_Rice.pdf#page=12]]): nella (12) e nell'ultima formula compare $S(f)$ invece di $S_p(f)$. Qui $S(f)$ sarebbe l'inviluppo complesso, un'altra cosa.

### Derivazione — Controllo: dalla (11) si ritrova la (3)
**Fonte:** [[Rappresentazione_Rice.pdf#page=12]] (slide 10), eq. (11)
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

### Derivazione — Perché proprio √2
**Fonte:** nota a mano di [[Rappresentazione_Rice.pdf#page=10]] («introdotto per motivi energetici»)
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

## Spiegazione

### Esempio: il segnale analitico di un coseno
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

### La trasformata di Hilbert come filtro
> 🧩 Lettura mia di $\widehat{S}_p(f) = -j\,\text{sgn}(f)\,S_p(f)$ ([[Rappresentazione_Rice.pdf#page=12]])

Il trasformatore di Hilbert è un sistema LTI con risposta in frequenza $H_{\mathcal{H}}(f) = -j\,\text{sgn}(f)$ e risposta impulsiva $1/(\pi t)$:
- $|H_{\mathcal{H}}(f)| = 1$: non cambia l'ampiezza di nessuna componente;
- fase $-90°$ per $f > 0$ e $+90°$ per $f < 0$: è uno **sfasatore di 90°**, come si è visto sul coseno.

Il segnale analitico (8) è quindi il segnale di partenza più $j$ volte la sua versione sfasata di 90°, a meno del fattore $1/\sqrt2$. La somma cancella le frequenze negative e raddoppia le positive.

> 🎯 Esame: definire il segnale analitico (3); ricavarne l'espressione nel tempo (8) passando per la (7); dimostrare la (10) e la biunivocità; ricavare $\widehat{S}_p(f) = -j\,\text{sgn}(f)\,S_p(f)$; spiegare il ruolo del $\sqrt2$.

## Perché importa

È il passo intermedio verso l'[[inviluppo-complesso]]. Scartare le frequenze negative non perde nulla, perché sono ridondanti per un segnale reale. Dopo lo scarto resta un solo lobo, attorno a $+f_c$, che si può traslare in banda base (eq. (13)).

## Connessioni

- [[segnali-banda-base-e-passa-banda]] — la simmetria hermitiana rende ridondante la metà negativa dello spettro.
- [[inviluppo-complesso]] — si ottiene traslando il segnale analitico di $-f_c$: $S(f) = S_p^+(f + f_c)$.
- [[upconversion-e-downconversion]] — la (10), $s_p = \sqrt2\,\text{Re}\{\cdot\}$, è anche il principio dell'upconversion.

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=10]] (slide 8), [[Rappresentazione_Rice.pdf#page=11]] (slide 9), [[Rappresentazione_Rice.pdf#page=12]] (slide 10)

_Aggiornato: 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
