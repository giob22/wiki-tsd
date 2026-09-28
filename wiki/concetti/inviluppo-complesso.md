---
tipo: concetto
importanza_esame: alta
prerequisiti: ["segnali-banda-base-e-passa-banda", "segnale-analitico"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=8", "Rappresentazione_Rice.pdf#page=9", "Rappresentazione_Rice.pdf#page=13", "Rappresentazione_Rice.pdf#page=14", "Rappresentazione_Rice.pdf#page=15", "Rappresentazione_Rice.pdf#page=16", "Rappresentazione_Rice.pdf#page=18", "Rappresentazione_Rice.pdf#page=19", "Rappresentazione_Rice.pdf#page=23"]
---

# Inviluppo complesso e componenti in fase e quadratura

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=8]] (slide 6), [[Rappresentazione_Rice.pdf#page=13]] (slide 11), [[Rappresentazione_Rice.pdf#page=14]] (slide 12)

Tutta l'informazione di un segnale passa-banda **reale** $s_p(t)$ è contenuta in un segnale **complesso in banda base**. Questo segnale si chiama **rappresentazione complessa in banda base**, o **inviluppo complesso** (*complex envelope*), di $s_p(t)$ ([[Rappresentazione_Rice.pdf#page=8]], slide 6).

In frequenza è il [[segnale-analitico]] traslato di $-f_c$ ([[Rappresentazione_Rice.pdf#page=13]], slide 11):
$$S(f) \triangleq S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c) \tag{13}$$

Nel tempo ([[Rappresentazione_Rice.pdf#page=14]], slide 12):
$$s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j\,s_s(t) \tag{15}$$
- $s_c(t)$ = componente **in fase** (*in-phase*, **I**), la parte reale;
- $s_s(t)$ = componente **in quadratura** (*quadrature*, **Q**), la parte immaginaria.

Sono entrambi segnali **reali** in banda base. Note a mano sulla slide 12 ([[Rappresentazione_Rice.pdf#page=14]]): $s_p^+(t)$ è il «segnale analitico nel dominio del tempo», $s(t)$ «è un segnale complesso», $s_c$ è la «componente coseno» e $s_s$ la «componente seno». Il perché dei nomi è nella (17).

Il ritorno al segnale passa-banda vale **per qualunque** segnale passa-banda:
$$s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) \tag{16, 17}$$

> 🧩 Precisazione mia: l'inviluppo complesso è definito **rispetto a una frequenza di riferimento** $f_c$. Se si cambia il riferimento in $f_c + \Delta f$, la (15) dà $s_p^+(t)\,e^{-j2\pi(f_c + \Delta f)t} = s(t)\,e^{-j2\pi \Delta f\, t}$: lo stesso inviluppo traslato in frequenza di $-\Delta f$. Per questo la slide 16 parla di un «riferimento di frequenza comune» ([[equivalente-banda-base-dei-filtri]]).

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $S(f) = S_p^+(f + f_c) = \sqrt2\,S_p(f + f_c)\,u(f + f_c)$ | inviluppo complesso in frequenza, eq. (13) | [[Rappresentazione_Rice.pdf#page=13]] (slide 11) |
| $S_p(f) = \dfrac{S(f - f_c) + S^*(-f - f_c)}{\sqrt2}$ | ritorno al passa-banda in frequenza, eq. (14) | [[Rappresentazione_Rice.pdf#page=13]] (slide 11) |
| $s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c(t) + j s_s(t)$ | inviluppo nel tempo, eq. (15) | [[Rappresentazione_Rice.pdf#page=14]] (slide 12) |
| $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\}$ | eq. (16) | [[Rappresentazione_Rice.pdf#page=14]] (slide 12) |
| $s_p(t) = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ | forma I/Q, eq. (17) | [[Rappresentazione_Rice.pdf#page=14]] (slide 12) |
| $s_p(t) = \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big)$, con $a = \|s\|$ e $\theta = \arg s$ | forma ampiezza-fase | 🧩 dalla (16) |
| $\langle x_c, x_s\rangle = \int x_c(t)\,x_s(t)\,dt = 0$ | ortogonalità delle portanti I e Q, eq. (18) | [[Rappresentazione_Rice.pdf#page=15]] (slide 13) |
| $\langle u_p, v_p\rangle = \langle u_c, v_c\rangle + \langle u_s, v_s\rangle = \text{Re}\{\langle u, v\rangle\}$ | prodotto scalare, eq. (19) | [[Rappresentazione_Rice.pdf#page=15]] (slide 13) |
| $\|s_p\|^2 = \|s\|^2$ | conservazione dell'energia, eq. (20) | [[Rappresentazione_Rice.pdf#page=15]] (slide 13) |

Simboli:
- $f_c$ = frequenza portante [Hz]; $u(\cdot)$ = gradino unitario; $^*$ = coniugato;
- $s(t)$ = inviluppo complesso (stessa unità di $s_p$, es. V); $s_c$, $s_s$ = sue parti reale e immaginaria;
- $x_c(t) = \sqrt2\,s_c(t)\cos(2\pi f_c t)$ e $x_s(t) = \sqrt2\,s_s(t)\sin(2\pi f_c t)$ = le due forme d'onda passa-banda di I e Q;
- $\langle x, y\rangle = \int x(t)\,y^*(t)\,dt$ = prodotto scalare [V²·s]; $\|x\|^2 = \langle x, x\rangle$ = energia [V²·s].

> 🧮 Formula chiave: $s_p(t) = \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} = \sqrt2\,s_c\cos(2\pi f_c t) - \sqrt2\,s_s\sin(2\pi f_c t)$ e $\|s_p\|^2 = \|s\|^2$.

## Derivazioni

### Derivazione — Eq. (15): l'inviluppo nel tempo
**Fonte:** [[Rappresentazione_Rice.pdf#page=14]] (slide 12)
$$
\begin{aligned}
s(t) &= \mathcal{F}^{-1}[S(f)] = \mathcal{F}^{-1}\big[S_p^+(f + f_c)\big] && \text{definizione (13)} \\
&= s_p^+(t)\,e^{-j2\pi f_c t} && \text{traslazione in frequenza: } X(f - f_0) \leftrightarrow x(t)\,e^{j2\pi f_0 t},\ f_0 = -f_c
\end{aligned}
$$
Moltiplicare per $e^{-j2\pi f_c t}$ sposta tutto lo spettro di $-f_c$: il lobo che il segnale analitico ha attorno a $+f_c$ finisce attorno a 0.

### Derivazione — Eq. (16) e (17): dall'inviluppo al segnale passa-banda
**Fonte:** [[Rappresentazione_Rice.pdf#page=14]] (slide 12): «si ottiene facilmente».
$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s_p^+(t)\} && \text{eq. (10) di [[segnale-analitico]]} \\
&= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{dalla (15): } s_p^+ = s\,e^{j2\pi f_c t} \quad \text{(16)} \\
&= \sqrt2\,\text{Re}\{(s_c + j s_s)(\cos\alpha + j\sin\alpha)\} && \text{Eulero, } \alpha = 2\pi f_c t \\
&= \sqrt2\,\text{Re}\{s_c\cos\alpha - s_s\sin\alpha + j(s_c\sin\alpha + s_s\cos\alpha)\} && \text{moltiplico; } j^2 = -1 \\
&= \sqrt2\,s_c(t)\cos(2\pi f_c t) - \sqrt2\,s_s(t)\sin(2\pi f_c t) && \text{parte reale} \quad \text{(17)}
\end{aligned}
$$
**Da qui i nomi:** $s_c$ moltiplica il **coseno** della portante, $s_s$ il **seno**. Seno e coseno sono sfasati di 90°, "in quadratura".
**Ipotesi:** nessuna oltre alla definizione. La slide sottolinea che la (17) vale per **qualunque** segnale passa-banda.

### Derivazione — Eq. (14): dall'inviluppo al passa-banda in frequenza
**Fonte:** [[Rappresentazione_Rice.pdf#page=13]] (slide 11): «la dimostrazione si ricava facilmente dalla (16)».
> 🧩 Derivazione mia

$$
\begin{aligned}
s_p(t) &= \sqrt2\,\text{Re}\{s(t)\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \frac{\sqrt2}{2}\Big[s(t)\,e^{j2\pi f_c t} + s^*(t)\,e^{-j2\pi f_c t}\Big] && \text{Re}\{z\} = (z + z^*)/2 \\
S_p(f) &= \frac{1}{\sqrt2}\Big[S(f - f_c) + S^*\big(-(f + f_c)\big)\Big] && x\,e^{j2\pi f_0 t} \leftrightarrow X(f - f_0);\ \ s^*(t) \leftrightarrow S^*(-f) \\
&= \frac{S(f - f_c) + S^*(-f - f_c)}{\sqrt2}
\end{aligned}
$$
**Lettura:** il primo termine ricostruisce il lobo attorno a $+f_c$, il secondo quello attorno a $-f_c$ come specchio coniugato. Il segnale che si ottiene è reale, perché il suo spettro è hermitiano per costruzione.
**Sanity check:** per $f$ vicino a $+f_c$ il secondo termine è nullo e, dalla (13), $S(f - f_c) = \sqrt2\,S_p(f)$. Quindi $S_p(f) = \sqrt2\,S_p(f)/\sqrt2$ ✓.

### Derivazione — Forma ampiezza-fase
**Fonte:** [[Rappresentazione_Rice.pdf#page=19]] (slide 15): l'inviluppo descrive «le variazioni lente di ampiezza e fase».
> 🧩 Derivazione mia: rende esplicita la frase della slide.

$$
\begin{aligned}
s(t) &= a(t)\,e^{j\theta(t)}, \quad a = |s| = \sqrt{s_c^2 + s_s^2},\ \ \theta = \arg s && \text{forma polare del numero complesso } s(t) \\
s_p(t) &= \sqrt2\,\text{Re}\{a(t)\,e^{j\theta(t)}\,e^{j2\pi f_c t}\} && \text{eq. (16)} \\
&= \sqrt2\,a(t)\cos\big(2\pi f_c t + \theta(t)\big) && \text{Re}\{e^{j\phi}\} = \cos\phi
\end{aligned}
$$
$s_p(t)$ è quindi una portante a $f_c$ con **ampiezza** $\sqrt2\,a(t)$ e **fase** $\theta(t)$. Se $s(t)$ ha banda molto minore di $f_c$ (banda stretta), ampiezza e fase cambiano lentamente rispetto alla portante.

### Derivazione — Eq. (18): ortogonalità delle componenti I e Q
**Fonte:** [[Rappresentazione_Rice.pdf#page=15]] (slide 13), che rimanda al libro di testo; dimostrazione negli appunti a mano di [[Rappresentazione_Rice.pdf#page=16]], con l'uguaglianza di Parseval.
> 🧩 Derivazione mia: segue gli appunti di p.16 e ne esplicita i passaggi e l'ipotesi che lasciano impliciti. $S_c$ e $S_s$ sono le trasformate di $s_c$ e $s_s$, e $W$ la loro banda.

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
- **$S_c(f - f_c)\,S_s^*(f + f_c)$ e $S_c(f + f_c)\,S_s^*(f - f_c)$** sono nulli. Il primo fattore vive attorno a $\pm f_c$, il secondo attorno a $\mp f_c$, e le due zone non si sovrappongono se $W < f_c$.
- Restano gli altri due, con il cambio di variabile $\nu = f \mp f_c$:
$$
\langle x_c, x_s\rangle = \frac{1}{2j}\Big[\underbrace{\int S_c(f + f_c)\,S_s^*(f + f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu} - \underbrace{\int S_c(f - f_c)\,S_s^*(f - f_c)\,df}_{=\int S_c(\nu) S_s^*(\nu)\,d\nu}\Big] = 0
$$

**Ipotesi:** $s_c$ e $s_s$ hanno banda $W < f_c$. Per un segnale passa-banda è garantita: dalla (2) e dalla (13), con $f_c$ al centro del lobo, $S(f) \approx 0$ per $|f| > B/2$. Quindi $W = B/2 < f_c$, perché $f_c > B$.
**Alternativa nel tempo** (🧩 mia):
$$
\langle x_c, x_s\rangle = \int 2\,s_c s_s \cos\alpha\sin\alpha\,dt = \int s_c(t)\,s_s(t)\,\sin(4\pi f_c t)\,dt
$$
È la trasformata del prodotto $s_c s_s$ calcolata in $\pm 2f_c$. Il prodotto ha banda al più $2W < 2f_c$, quindi l'integrale è nullo.

> ⚠️ Refuso negli appunti ([[Rappresentazione_Rice.pdf#page=16]]): nella riga $X_c(f) = \sqrt2\,S_c(f) * \big[\delta(f - f_c) - \delta(f + f_c)\big]/2$ il segno tra le delta dev'essere $+$, perché è un coseno. Nella prima riga degli appunti infatti la parentesi è $[S_c(f + f_c) + S_c(f - f_c)]$, con il $+$. La seconda riga degli appunti è incompleta; il risultato finale, $\frac{1}{2j}\big[\int S_c S_s^* - \int S_c S_s^*\big] = 0$, coincide con quello qui sopra.

Nota a mano sulla slide 12 ([[Rappresentazione_Rice.pdf#page=14]]): «quadratura: il prodotto [scalare] è 0». È proprio questa proprietà.

### Derivazione — Eq. (19): prodotto scalare tra segnali passa-banda
**Fonte:** [[Rappresentazione_Rice.pdf#page=15]] (slide 13): risultato dato senza dimostrazione.
> 🧩 Derivazione mia. $u_p$, $v_p$ reali passa-banda, con inviluppi $u = u_c + ju_s$ e $v = v_c + jv_s$; $\alpha = 2\pi f_c t$.

$$
\begin{aligned}
u_p v_p &= \big(\sqrt2 u_c\cos\alpha - \sqrt2 u_s\sin\alpha\big)\big(\sqrt2 v_c\cos\alpha - \sqrt2 v_s\sin\alpha\big) && \text{eq. (17) per entrambi} \\
&= 2u_cv_c\cos^2\alpha + 2u_sv_s\sin^2\alpha - 2(u_cv_s + u_sv_c)\sin\alpha\cos\alpha && \text{sviluppo} \\
&= u_cv_c + u_sv_s + (u_cv_c - u_sv_s)\cos 2\alpha - (u_cv_s + u_sv_c)\sin 2\alpha && 2\cos^2 = 1 + \cos 2\alpha;\ 2\sin^2 = 1 - \cos 2\alpha;\ 2\sin\cos = \sin 2\alpha \\
\langle u_p, v_p\rangle &= \int u_cv_c\,dt + \int u_sv_s\,dt + \underbrace{\int g_1\cos(4\pi f_c t)\,dt - \int g_2\sin(4\pi f_c t)\,dt}_{=\,0} && g_1, g_2 \text{ prodotti di segnali in banda base} \\
&= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle
\end{aligned}
$$
I termini a $2f_c$ si annullano. $\int g(t)\cos(4\pi f_c t)\,dt = \frac12[G(2f_c) + G(-2f_c)]$, e allo stesso modo per il seno. $G$ è la trasformata di un prodotto di due segnali con banda $\le W$, quindi ha banda $\le 2W < 2f_c$ e vale zero in $\pm 2f_c$.

Poi il confronto con l'inviluppo complesso:
$$
\begin{aligned}
\langle u, v\rangle &= \int u\,v^*\,dt = \int (u_c + ju_s)(v_c - jv_s)\,dt && \text{definizione; } v^* = v_c - jv_s \\
&= \int (u_cv_c + u_sv_s)\,dt + j\int (u_sv_c - u_cv_s)\,dt && \text{sviluppo} \\
\text{Re}\{\langle u, v\rangle\} &= \langle u_c, v_c\rangle + \langle u_s, v_s\rangle && \text{è la (19)}
\end{aligned}
$$
**Ipotesi:** banda di $u_c, u_s, v_c, v_s$ minore di $f_c$ (segnali passa-banda secondo la (2)).

### Derivazione — Eq. (20): l'energia si conserva
**Fonte:** [[Rappresentazione_Rice.pdf#page=15]] (slide 13)
$$
\begin{aligned}
\|s_p\|^2 &= \langle s_p, s_p\rangle && \text{definizione di energia} \\
&= \text{Re}\{\langle s, s\rangle\} && \text{(19) con } u = v = s \\
&= \text{Re}\{\|s\|^2\} = \|s\|^2 && \langle s, s\rangle = \textstyle\int |s|^2 dt \text{ è reale}
\end{aligned}
$$
In componenti: $\|s_p\|^2 = \|s_c\|^2 + \|s_s\|^2$, cioè l'energia di I più quella di Q.
**Perché torna esatto:** è l'effetto del $\sqrt2$ nella (3), vedi [[segnale-analitico#Derivazione — Perché proprio √2]]. Nota a mano di [[Rappresentazione_Rice.pdf#page=18]]: alla domanda se tutti i passaggi conservano l'energia, la risposta è «sì, per le accortezze fatte ($\sqrt2$)».

### Derivazione — Frequenza di campionamento: passa-banda contro inviluppo
**Fonte:** [[Rappresentazione_Rice.pdf#page=8]] (slide 6): l'inviluppo «si può campionare a una frequenza molto più bassa» di $s_p(t)$.
> 🧩 Derivazione mia, con il teorema del campionamento ([[teorema-del-campionamento]], [[Campionamento_AD_DA.pdf#page=14]]).
> ⚠️ Notazione: nella lezione sul campionamento $f_c$ era la frequenza di campionamento; qui $f_c$ è la portante, quindi la frequenza di campionamento si chiama $f_s$.

$$
\begin{aligned}
f_{s,\,p} &\ge 2\Big(f_c + \frac B2\Big) = 2f_c + B && s_p \text{ è reale e la sua frequenza massima è } f_c + B/2 \\
f_{s,\,\text{inv}} &\ge B && s(t) \text{ occupa } (-B/2,\ B/2):\ \text{repliche ogni } f_s \text{ senza sovrapposizione se } f_s \ge B \\
\frac{f_{s,\,p}}{f_{s,\,\text{inv}}} &= \frac{2f_c}{B} + 1 \gg 1 && \text{banda stretta: } B \ll f_c
\end{aligned}
$$
Ogni campione dell'inviluppo è complesso, cioè due numeri reali. Anche contando $2B$ numeri reali al secondo, il rapporto resta dell'ordine di $f_c/B$.
**Ipotesi:** $f_c$ al centro del lobo; campionamento ideale. Per $s(t)$ la condizione nasce dallo stesso argomento delle repliche di [[Campionamento_AD_DA.pdf#page=12]], applicato a uno spettro non simmetrico.

## Spiegazione

### Perché serve la rappresentazione in banda base (slide 6–7)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=8]] (slide 6), [[Rappresentazione_Rice.pdf#page=9]] (slide 7)

- I canali passa-banda sono molto usati, quindi bisogna saper trasmettere e ricevere segnali passa-banda.
- Tutta l'informazione di un segnale passa-banda reale sta in un segnale complesso in banda base: l'inviluppo complesso.
- L'inviluppo si può rappresentare a tempo discreto, cioè campionato, a una frequenza **molto più bassa** di $s_p(t)$ (vedi la derivazione sopra). I transceiver moderni eseguono quindi in digitale, direttamente sull'inviluppo, algoritmi complicati, riducendo al minimo l'elaborazione analogica.

Lo schema modulare del transceiver ([[Rappresentazione_Rice.pdf#page=9]], slide 7):
1. un **DSP** codifica l'informazione nella forma d'onda complessa in banda base: codifica, modulazione, filtraggio;
2. l'inviluppo viene **convertito in su** (*upconverted*) nel segnale passa-banda da mandare sul canale fisico;
3. al ricevitore il segnale passa-banda ricevuto viene **convertito in giù** (*downconverted*) in banda base;
4. il DSP opera sull'inviluppo per sincronizzazione, demodulazione e decodifica.

Così gli algoritmi più sofisticati si sviluppano in banda base, **indipendentemente dalla banda fisica** usata. Le conversioni sono in [[upconversion-e-downconversion]].

### Dallo spettro passa-banda all'inviluppo: le figure
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=13]] (slide 11)

![[rappresentazione-rice-p13-inviluppo-complesso-spettri.png]]
*[[Rappresentazione_Rice.pdf#page=13]] (slide 11). In alto, lo spettro del segnale passa-banda. $\text{Re}(S_p(f))$ ha due triangoli di altezza $A$ attorno a $\pm f_c$, speculari. $\text{Im}(S_p(f))$ ha due rettangoli di altezza $B$: positivo attorno a $f_c$, negativo attorno a $-f_c$. In basso, l'inviluppo: resta solo il lobo positivo, spostato attorno a 0 e moltiplicato per $\sqrt2$. $\text{Re}(S(f))$ è un triangolo di altezza $\sqrt2 A$, $\text{Im}(S(f))$ un rettangolo di altezza $\sqrt2 B$.*

> ⚠️ In questa figura, e nella slide 17, $A$ e $B$ sono **altezze** dello spettro, non la banda. Nel resto della lezione $B$ è la banda.

> 🧩 Controllo mio delle altezze con la (13): $S(f) = \sqrt2\,S_p(f + f_c)$ attorno a $f = 0$. Le altezze del lobo positivo vengono moltiplicate per $\sqrt2$: $A \to \sqrt2 A$ e $B \to \sqrt2 B$ ✓. Il lobo negativo sparisce per il fattore $u(f + f_c)$.

![[grafico-rice-catena-spettri.png]]
*🧩 Grafico mio (eq. (3) e (13), [[Rappresentazione_Rice.pdf#page=10]] e [[Rappresentazione_Rice.pdf#page=13]]; script in `output/grafici/`). La catena in tre passi, con un lobo asimmetrico come quello della slide 11.*
- *(a) Lo spettro reale del segnale passa-banda: i lobi a $\pm f_c$ sono speculari, quindi portano la stessa informazione.*
- *(b) Il segnale analitico: si butta il lobo negativo e si moltiplica per $\sqrt2$.*
- *(c) L'inviluppo complesso: lo stesso lobo spostato in 0.*

*Il lobo in (c) non è simmetrico attorno a 0. Non vale $S(f) = S^*(-f)$, e per questo $s(t)$ è complesso: è la nota a mano di [[Rappresentazione_Rice.pdf#page=2]], «il ricevitore porta in banda base, e questo rende il segnale complesso».*

### Componenti I/Q nel tempo
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=14]] (slide 12), [[Rappresentazione_Rice.pdf#page=19]] (slide 15)

![[rappresentazione-rice-p14-componenti-iq.png]]
*[[Rappresentazione_Rice.pdf#page=14]] (slide 12) con le note a mano: $s_p^+$ = segnale analitico nel tempo; $s_c$ = componente coseno, $s_s$ = componente seno; $s(t)$ è complesso; «quadratura: il prodotto [scalare] è 0».*

![[grafico-rice-iq-tempo.png]]
*🧩 Grafico mio (eq. (17), [[Rappresentazione_Rice.pdf#page=14]]). Esempio con $s_c(t) = \cos(2\pi\cdot 1\,\text{kHz}\cdot t) + 0.5\cos(2\pi\cdot 2\,\text{kHz}\cdot t)$ e $s_s(t) = 0.8\sin(2\pi\cdot 1.5\,\text{kHz}\cdot t)$. In alto I, Q e il modulo $|s(t)|$, che variano lentamente. In basso $s_p(t)$ con $f_c = 10$ kHz: una portante veloce dentro l'inviluppo $\pm\sqrt2\,|s(t)|$, come prevede la forma ampiezza-fase. $f_c$ è scelta piccola per rendere visibili le oscillazioni; nei sistemi reali $f_c/B$ è molto più grande.*

**Cosa rappresenta l'inviluppo** ([[Rappresentazione_Rice.pdf#page=19]], slide 15):
- ricavare l'inviluppo complesso significa estrarre le variazioni **lente** di ampiezza e fase introdotte dalla modulazione in banda base, eliminando la variazione di fase **rapida e prevedibile** dovuta a $f_c$;
- la fase dovuta a $f_c$ è prevedibile, quindi **non porta informazione**;
- l'informazione di un segnale passa-banda è **tutta** nel suo inviluppo complesso.

### Energia (slide 13)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=15]] (slide 13), appunti a mano di [[Rappresentazione_Rice.pdf#page=16]] e [[Rappresentazione_Rice.pdf#page=18]]

- Le forme d'onda passa-banda di I e di Q, $x_c = \sqrt2 s_c\cos(2\pi f_c t)$ e $x_s = \sqrt2 s_s\sin(2\pi f_c t)$, sono **ortogonali**, eq. (18). La slide rimanda al libro per la dimostrazione, che è negli appunti di p.16 ed è ricostruita sopra.
- Per due segnali passa-banda reali il prodotto scalare è la parte reale del prodotto scalare degli inviluppi, eq. (19).
- Con $u = v = s$: l'energia dell'inviluppo complesso è **uguale** a quella del segnale passa-banda, eq. (20).

![[rappresentazione-rice-p16-appunti-ortogonalita-parseval.png]]
*Appunti a mano, [[Rappresentazione_Rice.pdf#page=16]]: dimostrazione di $\langle x_c, x_s\rangle = 0$ con l'uguaglianza di Parseval. È ricostruita per esteso nella derivazione della (18), dove è segnalato anche un segno sbagliato nella riga di $X_c(f)$.*

### Banda di un segnale complesso (slide 19)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=23]] (slide 19)

- L'occupazione spettrale di un segnale **fisico reale** è la più piccola banda di frequenze **positive** che contiene la maggior parte del segnale. Per un segnale reale vale $S(f) = S^*(-f)$, quindi le frequenze negative non aggiungono nulla.
- Nei segnali **complessi** in banda base l'informazione sta sia nelle frequenze positive sia in quelle **negative**.
- L'occupazione spettrale di un segnale complesso in banda base è quindi la più piccola banda **attorno all'origine** che contiene la maggior parte del segnale, contando frequenze positive e negative.

> 🧩 Esempio mio: un segnale passa-banda con banda monolatera $B$ e $f_c$ al centro del lobo ha l'inviluppo in $(-B/2,\ B/2)$. Contando i due lati, l'occupazione è $B$: la stessa larghezza del lobo positivo di $s_p$. Non va dimezzata né raddoppiata, perché le due metà dello spettro di $s(t)$ sono diverse (grafico (c) sopra).

> 🎯 Esame: definire l'inviluppo complesso, (13) e (15), e le componenti I/Q; ricavare la (17) e la (14); dimostrare l'ortogonalità (18) e la conservazione dell'energia (20); spiegare perché l'informazione sta tutta nell'inviluppo e perché conviene lavorare in banda base.

## Perché importa

È il concetto centrale del primo tema del corso ([[Intro.pdf#page=3]]). Permette di:
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

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=8]] (slide 6), [[Rappresentazione_Rice.pdf#page=9]] (slide 7), [[Rappresentazione_Rice.pdf#page=13]] – [[Rappresentazione_Rice.pdf#page=15]] (slide 11–13), [[Rappresentazione_Rice.pdf#page=16]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=18]] (appunti a mano), [[Rappresentazione_Rice.pdf#page=19]] (slide 15), [[Rappresentazione_Rice.pdf#page=23]] (slide 19)

_Aggiornato: 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
