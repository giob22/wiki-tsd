---
tipo: concetto
importanza_esame: alta
prerequisiti: ["segnali-banda-base-e-passa-banda", "segnale-analitico"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=6", "Rappresentazione_Rice.pdf#page=9", "Rappresentazione_Rice.pdf#page=10", "Rappresentazione_Rice.pdf#page=15", "Rappresentazione_Rice.pdf#page=16", "Rappresentazione_Rice.pdf#page=17", "Rappresentazione_Rice.pdf#page=18", "Rappresentazione_Rice.pdf#page=19", "Rappresentazione_Rice.pdf#page=21", "Rappresentazione_Rice.pdf#page=22", "Rappresentazione_Rice.pdf#page=27"]
---

# Inviluppo complesso e componenti in fase e quadratura

## Definizione · [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=15|p. 15]], [[Rappresentazione_Rice.pdf#page=16|16]]

Tutta l'informazione di un segnale passa-banda **reale** $s_p(t)$ è contenuta in un segnale **complesso in banda base**. Questo segnale si chiama **rappresentazione complessa in banda base**, o **inviluppo complesso** (*complex envelope*), di $s_p(t)$.

In frequenza è il [[segnale-analitico]] traslato di $-f_c$:
$$S(f) \triangleq S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c) \tag{13}$$

Nel tempo:
$$s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j\,s_s(t) \tag{15}$$
- $s_c(t)$ = componente **in fase** (*in-phase*, **I**), la parte reale;
- $s_s(t)$ = componente **in quadratura** (*quadrature*, **Q**), la parte immaginaria.

Sono entrambi segnali **reali** in banda base. Note a mano sulla slide 12:
- la (15) «corrisponde a una traslazione del segnale analitico», per la proprietà di Fourier della traslazione in frequenza;
- $s_c(t)$ è la componente in fase (I), $s_s(t)$ la componente in quadratura (Q), e insieme danno i «termini di seno e coseno»;
- «quadratura indica che il prodotto ortogonale [scalare] con $s_c$ è 0», proprietà dimostrata più sotto, eq. (18).

Il perché dei nomi è nella (17).

Il ritorno al segnale passa-banda vale **per qualunque** segnale passa-banda:
$$s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{16, 17}$$

> 🧩 Precisazione mia: l'inviluppo complesso è definito **rispetto a una frequenza di riferimento** $f_c$. Se si cambia il riferimento in $f_c + \Delta f$, la (15) dà $s_p^+(t)\,e^{-j2\pi(f_c + \Delta f)t} = s(t)\,e^{-j2\pi \Delta f\, t}$: lo stesso inviluppo traslato in frequenza di $-\Delta f$. Per questo la slide 16 parla di un «riferimento di frequenza comune» ([[equivalente-banda-base-dei-filtri]]).

## Formule · [[Rappresentazione_Rice.pdf#page=15|p. 15]]–[[Rappresentazione_Rice.pdf#page=17|17]]

| Formula | Significato |
|---|---|
| $S(f) = S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c)$ | inviluppo complesso in frequenza, eq. (13) |
| $S_p(f) = \dfrac{S(f - f_c) + S^\ast (-f - f_c)}{\sqrt2}$ | ritorno al passa-banda in frequenza, eq. (14) |
| $s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j s_s(t)$ | inviluppo nel tempo, eq. (15) |
| $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\}$ | eq. (16) |
| $s_p(t) = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ | forma I/Q, eq. (17) |
| $s_p(t) = \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big)$, con $a = \lvert s\rvert$ e $\theta = \arg s$ | forma ampiezza-fase |
| $\langle x_c, x_s\rangle = \int x_c(t)\,x_s(t)\,dt = 0$ | ortogonalità delle portanti I e Q, eq. (18) |
| $\langle u_p, v_p\rangle = \langle u_c, v_c\rangle + \langle u_s, v_s\rangle = \text{Re}\{\langle u, v\rangle\}$ | prodotto scalare, eq. (19) |
| $\lVert s_p\rVert^2 = \lVert s\rVert^2$ | conservazione dell'energia, eq. (20) |

Simboli:
- $f_c$ = frequenza portante [Hz]; $u(\cdot)$ = gradino unitario; $^\ast$ = coniugato;
- $s(t)$ = inviluppo complesso (stessa unità di $s_p$, es. V); $s_c$, $s_s$ = sue parti reale e immaginaria;
- $x_c(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t)$ e $x_s(t) = \sqrt2\,s_s(t)\sin(2\pi f_c t)$ = le due forme d'onda passa-banda di I e Q;
- $\langle x, y\rangle = \int x(t)\,y^\ast (t)\,dt$ = prodotto scalare [V²·s]; $\|x\|^2 = \langle x, x\rangle$ = energia [V²·s].

> 🧮 Formula chiave: $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ e $\|s_p\|^2 = \|s\|^2$.

## Derivazioni

### Derivazione — Eq. (15): l'inviluppo nel tempo · [[Rappresentazione_Rice.pdf#page=16|p. 16]]
$$
\begin{aligned}
s(t) &= \mathcal{F}^{-1}[S(f)] = \mathcal{F}^{-1}\big[S_p^+(f + f_c)\big] && \text{definizione (13)} \\
&= s_p^+(t)\,e^{-j2\pi f_c t} && \text{traslazione in frequenza: } X(f - f_0) \leftrightarrow x(t)\,e^{j2\pi f_0 t},\ f_0 = -f_c
\end{aligned}
$$
Moltiplicare per $e^{-j2\pi f_c t}$ sposta tutto lo spettro di $-f_c$: il lobo che il segnale analitico ha attorno a $+f_c$ finisce attorno a 0.

### Derivazione — Eq. (16) e (17): dall'inviluppo al segnale passa-banda · [[Rappresentazione_Rice.pdf#page=16|p. 16]]
**Fonte:** «si ottiene facilmente».
$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s_p^+(t)\} && \text{eq. (10) di [[segnale-analitico]]} \\
&= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{dalla (15): } s_p^+ = s\,e^{j2\pi f_c t} \quad \text{(16)} \\
&= \sqrt2\,\text{Re}\{(s_c + j s_s)(\cos\alpha + j\sin\alpha)\} && \text{Eulero, } \alpha = 2\pi f_c t \\
&= \sqrt2\,\text{Re}\{s_c\cos\alpha - s_s\sin\alpha + j(s_c\sin\alpha + s_s\cos\alpha)\} && \text{moltiplico; } j^2 = -1 \\
&= \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) && \text{parte reale} \quad \text{(17)}
\end{aligned}
$$
Il secondo passaggio è annotato a mano sulla slide: «abbiamo definito prima l'inviluppo come $s(t) = s_p^+(t)e^{-j2\pi f_c t}$, quindi $s_p^+(t) = s(t)e^{j2\pi f_c t} = [s_c(t) + js_s(t)]\,e^{j2\pi f_c t}$». Sotto la (17): «in termini di seno e coseno».
**Da qui i nomi:** $s_c$ moltiplica il **coseno** della portante, $s_s$ il **seno**. Seno e coseno sono sfasati di 90°, "in quadratura".
**Ipotesi:** nessuna oltre alla definizione. La slide sottolinea che la (17) vale per **qualunque** segnale passa-banda.

### Derivazione — Eq. (14): dall'inviluppo al passa-banda in frequenza · [[Rappresentazione_Rice.pdf#page=15|p. 15]]
**Fonte:** «la dimostrazione si ricava facilmente dalla (16)».
> 🧩 Derivazione mia

$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \frac{\sqrt2}{2}\Big[s(t)\,e^{j2\pi f_c t} + s^*(t)\,e^{-j2\pi f_c t}\Big] && \text{Re}\{z\} = (z + z^*)/2 \\
S_p(f) &= \frac{1}{\sqrt2}\Big[S(f - f_c) + S^*\big(-(f + f_c)\big)\Big] && x\,e^{j2\pi f_0 t} \leftrightarrow X(f - f_0);\ \ s^*(t) \leftrightarrow S^*(-f) \\
&= \frac{S(f - f_c) + S^*(-f - f_c)}{\sqrt2}
\end{aligned}
$$
**Lettura:** il primo termine ricostruisce il lobo attorno a $+f_c$, il secondo quello attorno a $-f_c$ come specchio coniugato. Il segnale che si ottiene è reale, perché il suo spettro è hermitiano per costruzione. Note a mano sulla (14): è la «relazione inversa», e il termine $S^\ast (-f - f_c)$ rimette la «parte tagliata da $u(f)$», cioè il lobo negativo scartato costruendo il segnale analitico.
**Sanity check:** per $f$ vicino a $+f_c$ il secondo termine è nullo e, dalla (13), $S(f - f_c) = \sqrt2\,S_p(f)$. Quindi $S_p(f) = \sqrt2\,S_p(f)/\sqrt2$ ✓.

### Derivazione — Forma ampiezza-fase · [[Rappresentazione_Rice.pdf#page=22|p. 22]]
**Fonte:** l'inviluppo descrive «le variazioni lente di ampiezza e fase».
> 🧩 Derivazione mia: rende esplicita la frase della slide.

$$
\begin{aligned}
s(t) &= a(t)\,e^{j\theta(t)}, \quad a = |s| = \sqrt{s_c^2 + s_s^2},\ \ \theta = \arg s && \text{forma polare del numero complesso } s(t) \\
s_p(t) &= \sqrt2\,\text{Re}\{a(t)\,e^{j\theta(t)}\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big) && \text{Re}\{e^{j\phi}\} = \cos\phi
\end{aligned}
$$
$s_p(t)$ è quindi una portante a $f_c$ con **ampiezza** $\sqrt2\,a(t)$ e **fase** $\theta(t)$. Se $s(t)$ ha banda molto minore di $f_c$ (banda stretta), ampiezza e fase cambiano lentamente rispetto alla portante.

### Derivazione — Eq. (18): ortogonalità delle componenti I e Q · [[Rappresentazione_Rice.pdf#page=16|p. 16]]–[[Rappresentazione_Rice.pdf#page=18|18]]
**Fonte:** p. 17 (slide 13), che rimanda al libro di testo. Accanto, una nota a mano dice che la dimostrazione è «sotto»: è negli appunti di p. 18, con l'uguaglianza di Parseval.
> 📄 La struttura della dimostrazione è quella degli appunti di p.18: Parseval, spettri di $x_c$ e $x_s$, termini incrociati nulli per la banda stretta, cambio di variabile. 🧩 Esplicito io i fattori e l'ipotesi minima. $S_c$ e $S_s$ sono le trasformate di $s_c$ e $s_s$, e $W$ la loro banda.

![[rappresentazione-rice-p18-appunti-ortogonalita-parseval.png]]
*Appunti a mano.*
- *In alto: la dimostrazione di $\langle x_c, x_s\rangle = 0$ con Parseval. Si sviluppa il prodotto; i due termini incrociati sono barrati, con la nota in rosso sulla banda stretta; dopo il cambio di variabile i due integrali restanti si cancellano.*
- *In basso: la verifica della (19), con i termini misti che si annullano per l'ortogonalità e i termini in $\cos(4\pi f_c t)$ che valgono circa 0.*

$$
\begin{aligned}
\langle x_c, x_s\rangle &= \int_{-\infty}^{+\infty} x_c(t)\,x_s(t)\,dt = \int_{-\infty}^{+\infty} X_c(f)\,X_s^*(f)\,df && \text{Parseval; } x_s \text{ reale} \\
X_c(f) &= \frac{1}{\sqrt2}\big[S_c(f - f_c) + S_c(f + f_c)\big] && \sqrt2\cos\alpha = \tfrac{\sqrt2}{2}(e^{j\alpha} + e^{-j\alpha}) \\
X_s(f) &= \frac{1}{j\sqrt2}\big[S_s(f - f_c) - S_s(f + f_c)\big] && \sqrt2\sin\alpha = \tfrac{\sqrt2}{2j}(e^{j\alpha} - e^{-j\alpha}) \\
X_s^*(f) &= \frac{1}{j\sqrt2}\big[S_s^*(f + f_c) - S_s^*(f - f_c)\big] && (1/j)^* = -1/j \text{: cambio segno alla parentesi} \\
\langle x_c, x_s\rangle &= \frac{1}{2j}\int\big[S_c(f - f_c) + S_c(f + f_c)\big]\big[S_s^*(f + f_c) - S_s^*(f - f_c)\big]\,df && \tfrac{1}{\sqrt2}\cdot\tfrac{1}{j\sqrt2} = \tfrac{1}{2j}
\end{aligned}
$$

Sviluppando il prodotto escono quattro termini:
- **$S_c(f - f_c)\,S_s^\ast (f + f_c)$ e $S_c(f + f_c)\,S_s^\ast (f - f_c)$** sono nulli. Il primo fattore vive attorno a $\pm f_c$, il secondo attorno a $\mp f_c$, e le due zone non si sovrappongono. Negli appunti la giustificazione è in rosso: «per ipotesi i segnali sono a banda stretta: lo spettro centrato a $+f_c$ non si sovrappone mai a quello centrato in $-f_c$, perché $B/f_c \ll 1$».
- Restano gli altri due, con il cambio di variabile $\nu = f \mp f_c$:
$$
\langle x_c, x_s\rangle = \frac{1}{2j}\Big[\underbrace{\int S_c(f + f_c)\,S_s^*(f + f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu} - \underbrace{\int S_c(f - f_c)\,S_s^*(f - f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu}\Big] = 0
$$

**Ipotesi:** gli appunti usano la banda stretta, $B/f_c \ll 1$. 🧩 In realtà basta di meno: che $s_c$ e $s_s$ abbiano banda $W < f_c$. Per un segnale passa-banda questo è sempre garantito: dalla (2) e dalla (13), con $f_c$ al centro del lobo, $S(f) \approx 0$ per $|f| > B/2$. Quindi $W = B/2 < f_c$, perché $f_c > B$.
**Alternativa nel tempo** (🧩 mia):
$$
\langle x_c, x_s\rangle = \int 2\,s_c s_s \cos\alpha\sin\alpha\,dt = \int s_c(t)\,s_s(t)\,\sin(4\pi f_c t)\,dt
$$
È la trasformata del prodotto $s_c s_s$ calcolata in $\pm 2f_c$. Il prodotto ha banda al più $2W < 2f_c$, quindi l'integrale è nullo.

> ⚠️ Segni negli appunti: gli appunti scrivono $X_s = -\frac{\sqrt2}{2j}S_s(f) \ast [\delta(f - f_c) - \delta(f + f_c)]$, con un meno davanti che non ci va, perché $\sqrt2\sin\alpha = \frac{\sqrt2}{2j}(e^{j\alpha} - e^{-j\alpha})$. Anche l'ordine dei due integrali finali è invertito rispetto allo sviluppo. Il risultato, $\frac{1}{2j}\big[\int S_c S_s^\ast - \int S_c S_s^\ast \big] = 0$, non cambia: è la differenza di due integrali uguali.

Nota a mano sulla slide 12: «quadratura indica che il prodotto ortogonale [scalare] con $s_c$ è 0». È proprio questa proprietà.

### Derivazione — Eq. (19): prodotto scalare tra segnali passa-banda · [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]]
**Fonte:** risultato dato senza dimostrazione. Verificato negli appunti di p. 18 e p. 19. Note a mano sulla slide: $\langle u_p, v_p\rangle$ è il «prodotto ortogonale, scalare», e $\text{Re}\{\langle u, v\rangle\}$ è «la parte reale del prodotto degli inviluppi».
> 📄 Gli appunti procedono così: sviluppano $\langle u_p, v_p\rangle$ con la (17); i termini misti si annullano perché le componenti in fase e in quadratura sono ortogonali; restano $2\int u_cv_c\cos^2$ e $2\int u_sv_s\sin^2$, che si scrivono con $\cos^2 = \frac{1 + \cos(4\pi f_ct)}{2}$ e $\sin^2 = \frac{1 - \cos(4\pi f_ct)}{2}$. I due integrali con $\cos(4\pi f_c t)$ valgono circa 0, perché «le aree positive vengono bilanciate da quelle negative, poiché $B/f_c \ll 1$». Resta $\text{Re}\{\int[u_c + ju_s][v_c - jv_s]\,dt\} = \text{Re}\{\langle u, v\rangle\}$.
> 🧩 Qui sotto lo stesso conto per esteso. $u_p$, $v_p$ sono reali passa-banda, con inviluppi $u = u_c + ju_s$ e $v = v_c + jv_s$; $\alpha = 2\pi f_c t$.

$$
\begin{aligned}
u_p v_p &= \big(\sqrt2 u_c\cos\alpha - \sqrt2 u_s\sin\alpha\big)\big(\sqrt2 v_c\cos\alpha - \sqrt2 v_s\sin\alpha\big) && \text{eq. (17) per entrambi} \\
&= 2u_cv_c\cos^2\alpha + 2u_sv_s\sin^2\alpha - 2(u_cv_s + u_sv_c)\sin\alpha\cos\alpha && \text{sviluppo} \\
&= u_cv_c + u_sv_s + (u_cv_c - u_sv_s)\cos 2\alpha - (u_cv_s + u_sv_c)\sin 2\alpha && 2\cos^2 = 1 + \cos 2\alpha;\ 2\sin^2 = 1 - \cos 2\alpha;\ 2\sin\cos = \sin 2\alpha \\
\langle u_p, v_p\rangle &= \int u_cv_c\,dt + \int u_sv_s\,dt + \underbrace{\int g_1\cos(4\pi f_c t)\,dt - \int g_2\sin(4\pi f_c t)\,dt}_{=\,0} && g_1, g_2 \text{ prodotti di segnali in banda base} \\
&= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle
\end{aligned}
$$
I termini a $2f_c$ si annullano. Gli appunti lo giustificano con le aree che si bilanciano, cioè un inviluppo lento moltiplicato per un coseno veloce, e scrivono "≈ 0".
> 🧩 Precisazione mia: se la banda è minore di $f_c$ l'integrale è **esattamente** 0. Infatti $\int g(t)\cos(4\pi f_c t)\,dt = \frac12[G(2f_c) + G(-2f_c)]$, e allo stesso modo per il seno. $G$ è la trasformata di un prodotto di due segnali con banda $\le W$, quindi ha banda $\le 2W < 2f_c$ e vale zero in $\pm 2f_c$.

Poi il confronto con l'inviluppo complesso:
$$
\begin{aligned}
\langle u, v\rangle &= \int u\,v^*\,dt = \int (u_c + ju_s)(v_c - jv_s)\,dt && \text{definizione; } v^* = v_c - jv_s \\
&= \int (u_cv_c + u_sv_s)\,dt + j\int (u_sv_c - u_cv_s)\,dt && \text{sviluppo} \\
\text{Re}\{\langle u, v\rangle\} &= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle && \text{è la (19)}
\end{aligned}
$$
**Ipotesi:** banda di $u_c, u_s, v_c, v_s$ minore di $f_c$ (segnali passa-banda secondo la (2)).

### Derivazione — Eq. (20): l'energia si conserva · [[Rappresentazione_Rice.pdf#page=17|p. 17]], [[Rappresentazione_Rice.pdf#page=19|p. 19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]
**Fonte:** p. 17 (slide 13); gli stessi passaggi sono negli appunti di p. 19. Note a mano sulla slide: «energia di $s_p$», «l'energia è reale».
$$
\begin{aligned}
\|s_p\|^2 &= \langle s_p, s_p\rangle = \int s_p^2(t)\,dt && \text{definizione di energia} \\
&= \text{Re}\{\langle s, s\rangle\} && \text{(19) con } u = v = s \\
&= \text{Re}\{\|s\|^2\} = \|s\|^2 && \langle s, s\rangle = \textstyle\int |s|^2 dt \text{ è reale: «posso togliere Re» (appunti p.19)}
\end{aligned}
$$
In componenti: $\|s_p\|^2 = \|s_c\|^2 + \|s_s\|^2$, cioè l'energia di I più quella di Q.

> ⚠️ Nelle note a mano sulla slide 13:
> - il secondo passaggio è indicato come «proprietà (10)», ma usa la (19);
> - in alto c'è scritto $s_p(t) = x_c(t) + x_s(t) = \sqrt2 s_c\cos(2\pi f_c t) + \sqrt2 s_s\sin(2\pi f_c t)$, ma dalla (17) è $s_p = x_c - x_s$, con il meno davanti al termine in seno. Per l'ortogonalità il segno non conta, per l'uguaglianza con $s_p$ sì.

![[rappresentazione-rice-p19-appunti-prodotto-scalare-energia.png]]
*Appunti a mano: conclusione della verifica della (19), $\text{Re}\{\int[u_c + ju_s][v_c - jv_s]\,dt\} = \text{Re}\{\langle u, v\rangle\}$, con $u$ inviluppo complesso di $u_p$ e $v^\ast$ il coniugato di $v$. Sotto, la (20): $\langle s_p, s_p\rangle = \int s_p^2\,dt = \|s_p\|^2 = \text{Re}\{\langle s, s\rangle\} = \text{Re}\{\int|s|^2dt\} = \|s\|^2$, dove l'integrale è reale e quindi si può togliere Re.*
**Perché torna esatto:** è l'effetto del $\sqrt2$ nella (3), vedi [[segnale-analitico]] (sezione «Derivazione — Perché proprio √2»). Nota a mano di p. 21: alla domanda se tutti i passaggi conservano l'energia, la risposta è «sì, per le accortezze fatte ($\sqrt2$)».

### Derivazione — Frequenza di campionamento: passa-banda contro inviluppo · Rice [[Rappresentazione_Rice.pdf#page=9|p. 9]] · Campionamento [[Campionamento_AD_DA.pdf#page=12|p. 12]], [[Campionamento_AD_DA.pdf#page=14|p. 14]]
**Fonte:** l'inviluppo «si può campionare a una frequenza molto più bassa» di $s_p(t)$.
> 🧩 Derivazione mia, con il teorema del campionamento ([[teorema-del-campionamento]]).
> ⚠️ Notazione: nella lezione sul campionamento $f_c$ era la frequenza di campionamento; qui $f_c$ è la portante, quindi la frequenza di campionamento si chiama $f_s$.

$$
\begin{aligned}
f_{s,\,p} &\ge 2\Big(f_c + \frac B2\Big) = 2f_c + B && s_p \text{ è reale e la sua frequenza massima è } f_c + B/2 \\
f_{s,\,\text{inv}} &\ge B && s(t) \text{ occupa } (-B/2,\ B/2):\ \text{repliche ogni } f_s \text{ senza sovrapposizione se } f_s \ge B \\
\frac{f_{s,\,p}}{f_{s,\,\text{inv}}} &= \frac{2f_c}{B} + 1 \gg 1 && \text{banda stretta: } B \ll f_c
\end{aligned}
$$
Ogni campione dell'inviluppo è complesso, cioè due numeri reali. Anche contando $2B$ numeri reali al secondo, il rapporto resta dell'ordine di $f_c/B$.
**Ipotesi:** $f_c$ al centro del lobo; campionamento ideale. Per $s(t)$ la condizione nasce dallo stesso argomento delle repliche di p. 12, applicato a uno spettro non simmetrico.

## Spiegazione

### Perché serve la rappresentazione in banda base (slide 6–7) · [[Rappresentazione_Rice.pdf#page=6|p. 6]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]]

- I canali passa-banda sono molto usati, quindi bisogna saper trasmettere e ricevere segnali passa-banda.
- Tutta l'informazione di un segnale passa-banda reale sta in un segnale complesso in banda base: l'inviluppo complesso.
- L'inviluppo si può rappresentare a tempo discreto, cioè campionato, a una frequenza **molto più bassa** di $s_p(t)$ (vedi la derivazione sopra). I transceiver moderni eseguono quindi in digitale, direttamente sull'inviluppo, algoritmi complicati, riducendo al minimo l'elaborazione analogica.

Le note a mano sulla slide 6 riscrivono questi punti in italiano e chiamano il campionamento a frequenza bassa **il vantaggio**: l'inviluppo si campiona a una frequenza «nettamente inferiore» a quella che servirebbe per il segnale passa-banda. Di conseguenza i ricetrasmettitori moderni possono implementare in digitale algoritmi molto complessi (DSP), riducendo al minimo la parte analogica.

**Perché conviene portare il segnale in banda base**, dagli appunti di p. 6. Oltre al fatto che l'informazione non dipende da $f_c$, la banda base permette di:
- **ridurre i costi hardware per il campionamento**;
- guadagnare **modularità e indipendenza**: si possono riutilizzare componenti che operano in banda base, senza costruirli ad hoc per la specifica banda del segnale;
- (in rosso) altrimenti non si potrebbero generalizzare gli algoritmi, e calcolarli in digitale costerebbe troppo.

![[rappresentazione-rice-p6-appunti-vantaggi-banda-base.png]]
*Appunti a mano: i vantaggi di portare il segnale in banda base (costi di campionamento, modularità e indipendenza).*

Lo schema modulare del transceiver:
1. un **DSP** codifica l'informazione nella forma d'onda complessa in banda base: codifica, modulazione, filtraggio;
2. l'inviluppo viene **convertito in su** (*upconverted*) nel segnale passa-banda da mandare sul canale fisico;
3. al ricevitore il segnale passa-banda ricevuto viene **convertito in giù** (*downconverted*) in banda base;
4. il DSP opera sull'inviluppo per sincronizzazione, demodulazione e decodifica.

Così gli algoritmi più sofisticati si sviluppano in banda base, **indipendentemente dalla banda fisica** usata. Le conversioni sono in [[upconversion-e-downconversion]].

Note a mano sulla slide 7:
- i punti 1–2 formano il **modulatore**, i punti 3–4 il **demodulatore**: «sono macroblocchi», e il modulatore «comprende anche l'up conversion»;
- dal punto 1 «si ottiene l'inviluppo complesso in banda base»;
- sviluppare gli algoritmi in banda base vuol dire che «ci si è svincolati dalla frequenza carrier ($f_c$)».

![[rappresentazione-rice-p10-schema-modulare-transceiver.png]]
*con le note a mano: le parentesi graffe raggruppano i quattro passi in modulatore e demodulatore.*

### Dallo spettro passa-banda all'inviluppo: le figure · [[Rappresentazione_Rice.pdf#page=2|p. 2]], [[Rappresentazione_Rice.pdf#page=11|p. 11]], [[Rappresentazione_Rice.pdf#page=15|p. 15]]

![[rappresentazione-rice-p15-inviluppo-complesso-spettri.png]]
*In alto, lo spettro del segnale passa-banda. $\text{Re}(S_p(f))$ ha due triangoli di altezza $A$ attorno a $\pm f_c$, speculari. $\text{Im}(S_p(f))$ ha due rettangoli di altezza $B$: positivo attorno a $f_c$, negativo attorno a $-f_c$. In basso, l'inviluppo: resta solo il lobo positivo, spostato attorno a 0 e moltiplicato per $\sqrt2$. $\text{Re}(S(f))$ è un triangolo di altezza $\sqrt2 A$, $\text{Im}(S(f))$ un rettangolo di altezza $\sqrt2 B$.*

> ⚠️ In questa figura, e nella slide 17, $A$ e $B$ sono **altezze** dello spettro, non la banda. Nel resto della lezione $B$ è la banda.

> 🧩 Controllo mio delle altezze con la (13): $S(f) = \sqrt2\,S_p(f + f_c)$ attorno a $f = 0$. Le altezze del lobo positivo vengono moltiplicate per $\sqrt2$: $A \to \sqrt2 A$ e $B \to \sqrt2 B$ ✓. Il lobo negativo sparisce per il fattore $u(f + f_c)$.

![[grafico-rice-catena-spettri.png]]
*🧩 Grafico mio (eq. (3) e (13), p. 11 e p. 15; script in `output/grafici/`). La catena in tre passi, con un lobo asimmetrico come quello della slide 11.*
- *(a) Lo spettro reale del segnale passa-banda: i lobi a $\pm f_c$ sono speculari, quindi portano la stessa informazione.*
- *(b) Il segnale analitico: si butta il lobo negativo e si moltiplica per $\sqrt2$.*
- *(c) L'inviluppo complesso: lo stesso lobo spostato in 0.*

*Il lobo in (c) non è simmetrico attorno a 0. Non vale $S(f) = S^\ast (-f)$, e per questo $s(t)$ è complesso: è la nota a mano di p. 2, «il ricevitore porta in banda base, e questo rende il segnale complesso».*

### Componenti I/Q nel tempo · [[Rappresentazione_Rice.pdf#page=16|p. 16]], [[Rappresentazione_Rice.pdf#page=22|p. 22]]

![[rappresentazione-rice-p16-componenti-iq.png]]
*con le note a mano:*
- *la (15) corrisponde a una traslazione del segnale analitico, per la proprietà di Fourier;*
- *$s_c$ è la componente in fase (I), $s_s$ quella in quadratura (Q); quadratura vuol dire prodotto scalare nullo con $s_c$;*
- *i passaggi $s_p^+ = s\,e^{j2\pi f_c t} = [s_c + js_s]\,e^{j2\pi f_c t}$ che portano alla (16)–(17), "in termini di seno e coseno".*

![[grafico-rice-iq-tempo.png]]
*🧩 Grafico mio (eq. (17)). Esempio con $s_c(t) = \cos(2\pi\cdot 1\,\text{kHz}\cdot t) + 0.5\cos(2\pi\cdot 2\,\text{kHz}\cdot t)$ e $s_s(t) = 0.8\sin(2\pi\cdot 1.5\,\text{kHz}\cdot t)$. In alto I, Q e il modulo $|s(t)|$, che variano lentamente. In basso $s_p(t)$ con $f_c = 10$ kHz: una portante veloce dentro l'inviluppo $\pm\sqrt2\,|s(t)|$, come prevede la forma ampiezza-fase. $f_c$ è scelta piccola per rendere visibili le oscillazioni; nei sistemi reali $f_c/B$ è molto più grande.*

**Cosa rappresenta l'inviluppo**:
- ricavare l'inviluppo complesso significa estrarre le variazioni **lente** di ampiezza e fase introdotte dalla modulazione in banda base, eliminando la variazione di fase **rapida e prevedibile** dovuta a $f_c$. Nota a mano: «l'inviluppo complesso ci permette di separare le variazioni lente introdotte dalla modulazione in banda base»;
- la fase dovuta a $f_c$ è prevedibile, quindi **non porta informazione**;
- l'informazione di un segnale passa-banda è **tutta** nel suo inviluppo complesso.

### Energia (slide 13) · [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]
> 📄 Fonte: p. 17 (slide 13), appunti a mano di p. 18, p. 19 e p. 21

- Le forme d'onda passa-banda di I e di Q, $x_c = \sqrt2 s_c\cos(2\pi f_c t)$ e $x_s = \sqrt2 s_s\sin(2\pi f_c t)$, sono **ortogonali**, eq. (18). La slide rimanda al libro per la dimostrazione, che è negli appunti di p.18 (derivazione della (18) qui sopra).
- Per due segnali passa-banda reali il prodotto scalare è la parte reale del prodotto scalare degli inviluppi, eq. (19). Verifica negli appunti di p.18–19.
- Con $u = v = s$: l'energia dell'inviluppo complesso è **uguale** a quella del segnale passa-banda, eq. (20), anch'essa negli appunti di p.19.

### Banda di un segnale complesso (slide 19) · [[Rappresentazione_Rice.pdf#page=27|p. 27]]

- L'occupazione spettrale di un segnale **fisico reale** è la più piccola banda di frequenze **positive** che contiene la maggior parte del segnale. Per un segnale reale vale $S(f) = S^\ast (-f)$, quindi le frequenze negative non aggiungono nulla.
- Nei segnali **complessi** in banda base l'informazione sta sia nelle frequenze positive sia in quelle **negative**.
- L'occupazione spettrale di un segnale complesso in banda base è quindi la più piccola banda **attorno all'origine** che contiene la maggior parte del segnale, contando frequenze positive e negative.

> 🧩 Esempio mio: un segnale passa-banda con banda monolatera $B$ e $f_c$ al centro del lobo ha l'inviluppo in $(-B/2,\ B/2)$. Contando i due lati, l'occupazione è $B$: la stessa larghezza del lobo positivo di $s_p$. Non va dimezzata né raddoppiata, perché le due metà dello spettro di $s(t)$ sono diverse (grafico (c) sopra).

> 🎯 Esame: definire l'inviluppo complesso, (13) e (15), e le componenti I/Q; ricavare la (17) e la (14); dimostrare l'ortogonalità (18) e la conservazione dell'energia (20); spiegare perché l'informazione sta tutta nell'inviluppo e perché conviene lavorare in banda base.

## Perché importa · [[Intro.pdf#page=3|p. 3]]

È il concetto centrale del primo tema del corso. Permette di:
- descrivere qualunque segnale passa-banda con un segnale in banda base, senza portarsi dietro $f_c$;
- campionarlo ed elaborarlo in digitale a frequenza bassa;
- progettare modulazione, sincronizzazione e demodulazione indipendentemente dalla banda fisica.

## Connessioni

- [[segnale-analitico]] — l'inviluppo è il segnale analitico traslato di $-f_c$.
- [[segnali-banda-base-e-passa-banda]] — la (2) garantisce la banda $B/2 < f_c$ delle componenti I/Q, che serve per (18)–(20).
- [[upconversion-e-downconversion]] — realizzano fisicamente la (17) e la sua inversa.
- [[equivalente-banda-base-dei-filtri]] — anche i filtri passa-banda si descrivono con il loro inviluppo complesso.
- [[teorema-del-campionamento]] — l'inviluppo si campiona a frequenza $\ge B$ invece di $\ge 2f_c + B$.
- [[modulazione-digitale]] — il modulatore produce l'inviluppo complesso.

## Fonti · [[Rappresentazione_Rice.pdf#page=6|p. 6]], [[Rappresentazione_Rice.pdf#page=9|p. 9]], [[Rappresentazione_Rice.pdf#page=10|10]], [[Rappresentazione_Rice.pdf#page=15|p. 15]], [[Rappresentazione_Rice.pdf#page=17|p. 17]]–[[Rappresentazione_Rice.pdf#page=19|19]], [[Rappresentazione_Rice.pdf#page=21|p. 21]], [[Rappresentazione_Rice.pdf#page=22|22]], [[Rappresentazione_Rice.pdf#page=27|p. 27]]

- [[rappresentazione-complessa-banda-base]]
- Appunti a mano: p. 6 (vantaggi della banda base), p. 18 e p. 19 (dimostrazioni di (18), (19), (20)), p. 21 (catena e energia)

_Aggiornato: 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-10-14 — formule nelle tabelle: modulo scritto con \lvert \rvert e condizionamento con \mid (il \| non si leggeva bene); 2026-09-28 — re-ingest del PDF con nuovi appunti: vantaggi della banda base (p.6), macroblocchi modulatore/demodulatore, note sulle slide 11–15; dimostrazioni di (18), (19), (20) ora da fonte (appunti p.18–19), con le mie precisazioni marcate 🧩 e i refusi degli appunti segnalati; pagine rimappate; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
