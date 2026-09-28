---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso", "segnale-analitico"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=20", "Rappresentazione_Rice.pdf#page=21", "Rappresentazione_Rice.pdf#page=22"]
---

# Equivalente in banda base di un filtro passa-banda

## Definizione

> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=20]] (slide 16)

**Qualunque filtro passa-banda si può realizzare in banda base complessa.** Sia $s_p(t)$ un segnale passa-banda che attraversa un filtro passa-banda con risposta impulsiva $h_p(t)$:
$$y_p(t) = s_p(t) * h_p(t)$$
Siano $s(t)$, $h(t)$, $y(t)$ gli inviluppi complessi di $s_p$, $h_p$, $y_p$, calcolati **rispetto alla stessa frequenza di riferimento** $f_c$, e $S(f)$, $H(f)$, $Y(f)$ le loro trasformate. Allora
$$Y(f) = \frac{1}{\sqrt2}\,S(f)\,H(f) \tag{22}$$
$$y(t) = \frac{1}{\sqrt2}\,s(t) * h(t) \tag{23}$$
In banda base, filtrare significa **convolvere gli inviluppi**, con un fattore $1/\sqrt2$.

> 🧩 Perché serve un riferimento comune: l'inviluppo dipende da $f_c$. Cambiare riferimento trasla l'inviluppo in frequenza ([[inviluppo-complesso]]), e la (22) vale solo se i tre inviluppi sono traslati della stessa quantità.

## Formule

| Formula | Significato | Pagina |
|---|---|---|
| $Y_p(f) = S_p(f)\,H_p(f)$ | filtro LTI in frequenza | [[Rappresentazione_Rice.pdf#page=20]] (slide 16) |
| $Y_p^+ = \sqrt2 Y_p u(f)$, $S_p^+ = \sqrt2 S_p u(f)$, $H_p^+ = \sqrt2 H_p u(f)$ | segnali analitici ("segmenti a frequenze positive") | [[Rappresentazione_Rice.pdf#page=20]] (slide 16) |
| $Y(f) = \frac{1}{\sqrt2}S(f)H(f)$ | eq. (22) | [[Rappresentazione_Rice.pdf#page=20]] (slide 16) |
| $y(t) = \frac{1}{\sqrt2}\,s(t) * h(t)$ | eq. (23) | [[Rappresentazione_Rice.pdf#page=21]] (slide 17) |
| $y_c = \frac{1}{\sqrt2}[s_c * h_c - s_s * h_s]$ | componente I dell'uscita, eq. (24) | [[Rappresentazione_Rice.pdf#page=22]] (slide 18) |
| $y_s = \frac{1}{\sqrt2}[s_s * h_c + s_c * h_s]$ | componente Q dell'uscita, eq. (25) | [[Rappresentazione_Rice.pdf#page=22]] (slide 18) |

Simboli: $h_p(t)$ = risposta impulsiva del filtro passa-banda [1/s]; $h = h_c + jh_s$ = suo inviluppo complesso; $s = s_c + js_s$ e $y = y_c + jy_s$ = inviluppi di ingresso e uscita; $*$ = convoluzione; $u(\cdot)$ = gradino unitario.

> 🧮 Formula chiave: $y(t) = \frac{1}{\sqrt2}\,s(t) * h(t)$.

## Derivazioni

### Derivazione — Eq. (22)
**Fonte:** [[Rappresentazione_Rice.pdf#page=20]] (slide 16)
$$
\begin{aligned}
Y(f) &= Y_p^+(f + f_c) && \text{definizione (13) di inviluppo, applicata a } y_p \\
&= \sqrt2\,Y_p(f + f_c)\,u(f + f_c) && \text{definizione (3) di segnale analitico} \\
&= \sqrt2\,S_p(f + f_c)\,H_p(f + f_c)\,u(f + f_c) && \text{filtro LTI: } Y_p = S_p H_p
\end{aligned}
$$
Per esprimere il risultato con $S$ e $H$, calcolo il loro prodotto (🧩 passaggio mio, la slide salta all'ultimo termine):
$$
\begin{aligned}
S(f)\,H(f) &= \big[\sqrt2\,S_p(f + f_c)\,u(f + f_c)\big]\big[\sqrt2\,H_p(f + f_c)\,u(f + f_c)\big] && \text{(13) per } s \text{ e per } h \\
&= 2\,S_p(f + f_c)\,H_p(f + f_c)\,u(f + f_c) && \sqrt2\cdot\sqrt2 = 2;\ \ u^2 = u \\
\Rightarrow\ Y(f) &= \frac{\sqrt2}{2}\,S(f)\,H(f) = \frac{1}{\sqrt2}\,S(f)\,H(f) && \text{confronto con la riga precedente}
\end{aligned}
$$
**Da dove viene il $1/\sqrt2$:** ogni inviluppo porta con sé un $\sqrt2$. Nel prodotto $SH$ i fattori diventano due, mentre $Y$ ne deve avere uno solo.

### Derivazione — Eq. (23)
**Fonte:** [[Rappresentazione_Rice.pdf#page=21]] (slide 17)
$$
y(t) = \mathcal{F}^{-1}[Y(f)] = \frac{1}{\sqrt2}\,\mathcal{F}^{-1}\big[S(f)\,H(f)\big] = \frac{1}{\sqrt2}\,s(t) * h(t) \qquad \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
$$

### Derivazione — Eq. (24) e (25): le componenti I e Q dell'uscita
**Fonte:** [[Rappresentazione_Rice.pdf#page=22]] (slide 18)
> 🧩 Passaggi miei: la slide dà solo il risultato.

$$
\begin{aligned}
s * h &= (s_c + js_s) * (h_c + jh_s) && \text{componenti I e Q} \\
&= s_c * h_c + j\,s_c * h_s + j\,s_s * h_c + j^2\,s_s * h_s && \text{la convoluzione è bilineare} \\
&= \big(s_c * h_c - s_s * h_s\big) + j\,\big(s_s * h_c + s_c * h_s\big) && j^2 = -1 \\
y_c &= \frac{1}{\sqrt2}\big[s_c * h_c - s_s * h_s\big] && \text{parte reale della (23)} \\
y_s &= \frac{1}{\sqrt2}\big[s_s * h_c + s_c * h_s\big] && \text{parte immaginaria}
\end{aligned}
$$
Servono **quattro convoluzioni reali**. È la stessa regola del prodotto di due numeri complessi, $(a + jb)(c + jd) = (ac - bd) + j(bc + ad)$, con la convoluzione al posto del prodotto.

### Derivazione — Controllo sulle altezze della figura (slide 17)
**Fonte:** [[Rappresentazione_Rice.pdf#page=21]] (slide 17)
> 🧩 Verifica mia. In figura $A$ è l'altezza del filtro e $B$ quella dello spettro d'ingresso (non la banda).

$$
\begin{aligned}
\text{passa-banda: } Y_p &= S_p H_p \Rightarrow \text{altezza } A\cdot B = AB && \text{dove i due spettri si sovrappongono} \\
\text{banda base: } H &\to \sqrt2 A,\quad S \to \sqrt2 B && \text{(13): gli inviluppi hanno altezza } \times\sqrt2 \\
Y &= \tfrac{1}{\sqrt2}\,(\sqrt2 A)(\sqrt2 B) = \sqrt2\,AB && \text{(22)}
\end{aligned}
$$
Coincide con il $\sqrt2 AB$ della figura, ed è anche l'inviluppo di $Y_p$ calcolato direttamente con la (13): $\sqrt2\cdot AB$ ✓.

## Spiegazione

### Passa-banda e banda base a confronto (slide 17)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=21]] (slide 17)

![[rappresentazione-rice-p21-filtraggio-spettri.png]]
*[[Rappresentazione_Rice.pdf#page=21]] (slide 17). A sinistra, in banda passante: filtro $H_p(f)$, rettangoli di altezza $A$ attorno a $\pm f_c$; ingresso $S_p(f)$, triangoli di altezza $B$; uscita $Y_p(f)$, il triangolo "tagliato" dal rettangolo, altezza $AB$. A destra, in banda base complessa, gli stessi spettri attorno a 0 con un solo lobo: filtro $H(f)$ di altezza $\sqrt2 A$, ingresso $S(f)$ di altezza $\sqrt2 B$, uscita $Y(f)$ di altezza $\sqrt2 AB$.*

### Realizzazione con operazioni reali (slide 18)
> 📄 Fonte: [[Rappresentazione_Rice.pdf#page=22]] (slide 18)

![[rappresentazione-rice-p22-filtro-banda-base-iq.png]]
*[[Rappresentazione_Rice.pdf#page=22]] (slide 18). Il segnale passa-banda $s_p(t)$ entra nel downconverter, che produce $s_c(t)$ e $s_s(t)$. Il riquadro tratteggiato, "operazioni reali in banda base", contiene quattro filtri reali. $s_c$ passa per $h_c$ e $h_s$, $s_s$ per $h_c$ e $h_s$. Due sommatori formano $y_c = s_c * h_c - s_s * h_s$ (con il segno meno) e $y_s = s_s * h_c + s_c * h_s$.*

> ⚠️ Nella figura manca il fattore $1/\sqrt2$ delle (24)–(25): le uscite disegnate sono $\sqrt2\,y_c$ e $\sqrt2\,y_s$.

> 🧩 Quando i termini incrociati spariscono (osservazione mia): se $h(t)$ è reale, cioè $h_s = 0$, le (24)–(25) diventano $y_c = \frac{1}{\sqrt2}\,s_c * h_c$ e $y_s = \frac{1}{\sqrt2}\,s_s * h_c$. I e Q vengono filtrati separatamente, senza mescolarsi. Per la simmetria hermitiana ([[segnali-banda-base-e-passa-banda]]), $h$ è reale quando $H(f) = H^*(-f)$, cioè quando il filtro passa-banda è simmetrico (coniugato) attorno a $f_c$. Nella figura della slide 17 il rettangolo $H(f)$ non è centrato in 0: in quel caso $h_s \neq 0$ e i termini incrociati ci sono.

### A cosa serve
Gli appunti di [[Rappresentazione_Rice.pdf#page=18]] vedono upconverter, canale fisico e downconverter come **un unico canale** ([[upconversion-e-downconversion]]). Questa pagina dice come descriverlo: se il canale fisico è un filtro LTI passa-banda $h_p$, visto dalla banda base è il filtro $h/\sqrt2$ che agisce sull'inviluppo. Tutto si può quindi simulare e trattare in banda base.

> 🎯 Esame: ricavare la (22) partendo dai segnali analitici; spiegare il fattore $1/\sqrt2$; scrivere le (24)–(25) e disegnare lo schema con quattro filtri reali.

## Perché importa

Completa la rappresentazione in banda base. Non solo i segnali, ma anche i **sistemi** passa-banda (filtri, canali LTI) hanno un equivalente in banda base. Si può allora lavorare interamente con gli inviluppi, dal modulatore al demodulatore, senza mai tornare a $f_c$.

## Connessioni

- [[inviluppo-complesso]] — definizione (13) usata per $s$, $h$ e $y$; dipendenza dal riferimento $f_c$.
- [[segnale-analitico]] — la dimostrazione passa per $Y_p^+$, $S_p^+$, $H_p^+$.
- [[upconversion-e-downconversion]] — il downconverter fornisce $s_c$ e $s_s$ ai quattro filtri; la catena diventa un canale in banda base.
- [[segnali-banda-base-e-passa-banda]] — il canale passa-banda è un sistema LTI che soddisfa la (2).

## Fonti

- [[rappresentazione-complessa-banda-base]]
- [[Rappresentazione_Rice.pdf#page=20]] (slide 16), [[Rappresentazione_Rice.pdf#page=21]] (slide 17), [[Rappresentazione_Rice.pdf#page=22]] (slide 18)

_Aggiornato: 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
