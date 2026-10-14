---
tipo: concetto
importanza_esame: alta
prerequisiti: ["segnali-banda-base-e-passa-banda"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=11", "Rappresentazione_Rice.pdf#page=12", "Rappresentazione_Rice.pdf#page=13", "Rappresentazione_Rice.pdf#page=14"]
---

# Segnale analitico e trasformata di Hilbert

## Definizione · [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=12|12]]

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

## Formule · [[Rappresentazione_Rice.pdf#page=11|p. 11]]–[[Rappresentazione_Rice.pdf#page=13|13]]

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

## Derivazioni

### Derivazione — Eq. (4): dal prodotto in frequenza alla convoluzione nel tempo · [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=12|12]]
$$
\begin{aligned}
s_p^+(t) &= \mathcal{F}^{-1}\big[S_p^+(f)\big] && \text{definizione di } s_p^+(t) \\
&= \mathcal{F}^{-1}\big[\sqrt2\,S_p(f)\cdot u(f)\big] && \text{sostituisco la (3)} \\
&= \sqrt2\,s_p(t) * \mathcal{F}^{-1}[u(f)] && \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
\end{aligned}
$$
Lo stesso passaggio è annotato a mano sopra la (4): $\sqrt2\,\mathcal{F}^{-1}[S_p(f)] * \mathcal{F}^{-1}[u(f)]$. Resta da calcolare l'antitrasformata del gradino **in frequenza**, che la nota a mano sulla (7) chiama appunto «antitrasformata del gradino».

### Derivazione — Eq. (7): antitrasformata di $u(f)$ · [[Rappresentazione_Rice.pdf#page=12|p. 12]]
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

### Derivazione — Eq. (8): il segnale analitico nel tempo · [[Rappresentazione_Rice.pdf#page=12|p. 12]]
$$
\begin{aligned}
s_p^+(t) &= \sqrt2\,s_p(t) * \Big[\tfrac12\,\delta(t) + \frac{j}{2\pi t}\Big] && \text{la (7) nella (4)} \\
&= \frac{\sqrt2}{2}\,s_p(t) + \frac{\sqrt2\,j}{2}\;s_p(t) * \frac{1}{\pi t} && s * \delta = s;\ \tfrac{1}{2\pi t} = \tfrac12\cdot\tfrac{1}{\pi t} \\
&= \frac{1}{\sqrt2}\,s_p(t) + \frac{j}{\sqrt2}\,\widehat{s}_p(t) && \tfrac{\sqrt2}{2} = \tfrac{1}{\sqrt2};\ \text{definizione (9)}
\end{aligned}
$$
Note a mano: $s_p(t)$ è il «segnale reale passa-banda», $\widehat{s}_p(t)$ è la «trasformata di Hilbert di $s_p$».

### Derivazione — Eq. (10) e corrispondenza biunivoca · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
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

### Derivazione — Trasformata di $\text{sgn}(t)$ e di $1/(\pi t)$ · [[Rappresentazione_Rice.pdf#page=13|p. 13]], [[Rappresentazione_Rice.pdf#page=14|14]]
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

### Derivazione — Trasformata di Hilbert in frequenza, eq. (12) · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
$$
\begin{aligned}
\widehat{S}_p(f) &= \mathcal{F}\Big[s_p(t) * \frac{1}{\pi t}\Big] = S_p(f)\,\mathcal{F}\Big[\frac{1}{\pi t}\Big] && \text{convoluzione} \to \text{prodotto, eq. (12)} \\
&= -j\,\text{sgn}(f)\,S_p(f) && \text{derivazione precedente}
\end{aligned}
$$
Note a mano sulla slide 10: sopra $\widehat{S}_p$ «$s_p(t) * \frac{1}{\pi t}$», sul segno di uguale «proprietà di Fourier» (convoluzione → prodotto), sotto il risultato «la trasformata di Hilbert in frequenza».

> ⚠️ Refuso della slide, corretto a mano nel PDF: nella (12) e nell'ultima formula compare $S(f)$ invece di $S_p(f)$. Qui $S(f)$ sarebbe l'inviluppo complesso, un'altra cosa.

### Derivazione — Controllo: dalla (11) si ritrova la (3) · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
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

### Derivazione — Perché proprio √2 · [[Rappresentazione_Rice.pdf#page=11|p. 11]]
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

### La trasformata di Hilbert come sfasatore di 90° · [[Rappresentazione_Rice.pdf#page=13|p. 13]]
> 📄 Fonte: nota a mano su p. 13 (slide 10): «in pratica la trasformata di Hilbert di un segnale equivale a sfasare di −90° tutte le componenti frequenziali positive e di +90° tutte quelle negative».

![[rappresentazione-rice-p13-segnale-analitico-hilbert.png]]
*con le note a mano: relazione inversa (10), proprietà di Fourier nella (12), trasformata di Hilbert in frequenza e sfasamento di ∓90°.*

> 🧩 Perché, in termini di filtro (lettura mia): il trasformatore di Hilbert è un sistema LTI con risposta in frequenza $H_{\mathcal{H}}(f) = -j\,\text{sgn}(f)$ e risposta impulsiva $1/(\pi t)$.
> - $|H_{\mathcal{H}}(f)| = 1$: non cambia l'ampiezza di nessuna componente.
> - Per $f > 0$ moltiplica per $-j = e^{-j\pi/2}$, cioè fase $-90°$; per $f < 0$ moltiplica per $+j = e^{+j\pi/2}$, cioè $+90°$. È lo sfasamento della nota, verificato sul coseno qui sopra.

Il segnale analitico (8) è quindi il segnale di partenza più $j$ volte la sua versione sfasata di 90°, a meno del fattore $1/\sqrt2$. La somma cancella le frequenze negative e raddoppia le positive.

> 🎯 Esame: definire il segnale analitico (3); ricavarne l'espressione nel tempo (8) passando per la (7); dimostrare la (10) e la biunivocità; ricavare $\widehat{S}_p(f) = -j\,\text{sgn}(f)\,S_p(f)$; spiegare il ruolo del $\sqrt2$.

## Perché importa

È il passo intermedio verso l'[[inviluppo-complesso]]. Scartare le frequenze negative non perde nulla, perché sono ridondanti per un segnale reale. Dopo lo scarto resta un solo lobo, attorno a $+f_c$, che si può traslare in banda base (eq. (13)).

## Connessioni

- [[segnali-banda-base-e-passa-banda]] — la simmetria hermitiana rende ridondante la metà negativa dello spettro.
- [[inviluppo-complesso]] — si ottiene traslando il segnale analitico di $-f_c$: $S(f) = S_p^+(f + f_c)$.
- [[upconversion-e-downconversion]] — la (10), $s_p = \sqrt2\,\text{Re}\{\cdot\}$, è anche il principio dell'upconversion.

## Fonti · [[Rappresentazione_Rice.pdf#page=11|p. 11]]–[[Rappresentazione_Rice.pdf#page=14|14]]

- [[rappresentazione-complessa-banda-base]]

_Aggiornato: 2026-09-28 — re-ingest del PDF con nuovi appunti: scopo del segnale analitico, $\sqrt2$ per conservare l'energia, parte reale e immaginaria della (8), trasformata di sgn (appunti p.14, con segno sbagliato su $1/(\pi t)$), sfasamento di ∓90° ora da fonte; pagine rimappate; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
