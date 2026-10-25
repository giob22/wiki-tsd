---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso", "segnale-analitico"]
fonti_pdf: ["Rappresentazione_Rice.pdf#page=23", "Rappresentazione_Rice.pdf#page=24", "Rappresentazione_Rice.pdf#page=25", "Rappresentazione_Rice.pdf#page=26"]
---

# Equivalente in banda base di un filtro passa-banda

## Definizione · [[Rappresentazione_Rice.pdf#page=23|p. 23]]

**Qualunque filtro passa-banda si può realizzare in banda base complessa.** Sia $s_p(t)$ un segnale passa-banda che attraversa un filtro passa-banda con risposta impulsiva $h_p(t)$:
$$y_p(t) = s_p(t) * h_p(t)$$
Siano $s(t)$, $h(t)$, $y(t)$ gli inviluppi complessi di $s_p$, $h_p$, $y_p$, calcolati **rispetto alla stessa frequenza di riferimento** $f_c$, e $S(f)$, $H(f)$, $Y(f)$ le loro trasformate. Allora
$$Y(f) = \frac{1}{\sqrt2}\,S(f)\,H(f) \tag{22}$$
$$y(t) = \frac{1}{\sqrt2}\,s(t) * h(t) \tag{23}$$
In banda base, filtrare significa **convolvere gli inviluppi**, con un fattore $1/\sqrt2$.

> 🧩 Perché serve un riferimento comune: l'inviluppo dipende da $f_c$. Cambiare riferimento trasla l'inviluppo in frequenza ([[inviluppo-complesso]]), e la (22) vale solo se i tre inviluppi sono traslati della stessa quantità.

## Formule · [[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]

| Formula | Significato |
|---|---|
| $Y_p(f) = S_p(f)\,H_p(f)$ | filtro LTI in frequenza |
| $Y_p^+ = \sqrt2 Y_p u(f)$, $S_p^+ = \sqrt2 S_p u(f)$, $H_p^+ = \sqrt2 H_p u(f)$ | segnali analitici ("segmenti a frequenze positive") |
| $Y(f) = \frac{1}{\sqrt2}S(f)H(f)$ | eq. (22) |
| $y(t) = \frac{1}{\sqrt2}\,s(t) \ast h(t)$ | eq. (23) |
| $y_c = \frac{1}{\sqrt2}[s_c \ast h_c - s_s \ast h_s]$ | componente I dell'uscita, eq. (24) |
| $y_s = \frac{1}{\sqrt2}[s_s \ast h_c + s_c \ast h_s]$ | componente Q dell'uscita, eq. (25) |

Simboli: $h_p(t)$ = risposta impulsiva del filtro passa-banda [1/s]; $h = h_c + jh_s$ = suo inviluppo complesso; $s = s_c + js_s$ e $y = y_c + jy_s$ = inviluppi di ingresso e uscita; $\ast$ = convoluzione; $u(\cdot)$ = gradino unitario.

> 🧮 Formula chiave: $y(t) = \frac{1}{\sqrt2}\,s(t) \ast h(t)$.

## Derivazioni

### Derivazione — Eq. (22) · [[Rappresentazione_Rice.pdf#page=23|p. 23]], [[Rappresentazione_Rice.pdf#page=24|24]]
**Fonte:** p. 23 (slide 16) per l'impostazione; p. 24 (appunti a mano) per la catena completa, compreso il passaggio che la slide salta.
> 📄 La catena è quella degli appunti di p.24. Lì l'ingresso si chiama $x_p(t)$ (inviluppo $x(t)$); qui uso $s$ come nella slide. Tra virgolette le note a mano; gli altri commenti sono 🧩 miei.

Gli appunti partono da $y_p(t) = x_p(t) \ast h_p(t)$ e dalla domanda «l'uscita come diventa in termini di inviluppo complesso?». La risposta: «ragioniamo in $f$». Nel tempo c'è una convoluzione; in frequenza diventa un prodotto, $Y_p(f) = X_p(f)\,H_p(f)$, molto più facile da maneggiare. Servono poi i tre segnali analitici, scritti uno sotto l'altro negli appunti:
$$Y_p^+(f) = \sqrt2\,Y_p(f)\,u(f), \qquad X_p^+(f) = \sqrt2\,X_p(f)\,u(f), \qquad H_p^+(f) = \sqrt2\,H_p(f)\,u(f)$$

$$
\begin{aligned}
Y(f) &= Y_p^+(f + f_c) && \text{definizione (13) di inviluppo, applicata a } y_p \\
&= \sqrt2\,Y_p(f + f_c)\,u(f + f_c) && \text{definizione (3) di segnale analitico, calcolata in } f + f_c \\
&= \sqrt2\,S_p(f + f_c)\,H_p(f + f_c)\,u^2(f + f_c) && \text{«sostituisco l'uscita» } Y_p = S_p H_p;\ u \to u^2 \text{ «non altera nulla»} \\
&= \sqrt2\,S_p(f + f_c)\,H_p(f + f_c)\,u^2(f + f_c)\cdot\frac{\sqrt2}{\sqrt2} && \text{moltiplico e divido per } \sqrt2 \\
&= \frac{1}{\sqrt2}\,\big[\sqrt2\,S_p(f + f_c)\,u(f + f_c)\big]\,\big[\sqrt2\,H_p(f + f_c)\,u(f + f_c)\big] && \text{un } \sqrt2 \text{ e una } u \text{ per fattore; } \tfrac{1}{\sqrt2} \text{ «resta fuori»} \\
&= \frac{1}{\sqrt2}\,S(f)\,H(f) && \text{(13) per } s \text{ e per } h\text{: le parentesi sono } S(f) \text{ e } H(f)
\end{aligned}
$$

Il perché dei due trucchi:
- **$u \to u^2$.** Il gradino vale solo 0 o 1, e $0^2 = 0$, $1^2 = 1$: elevarlo al quadrato non cambia nulla. Serve ad avere **due** gradini, uno da assegnare a $S_p$ e uno a $H_p$. Così ciascuno dei due fattori diventa il segnale analitico del suo segnale.
- **$\cdot\sqrt2/\sqrt2$.** Anche questo non cambia il valore (moltiplica per 1). Nella riga c'è un solo $\sqrt2$, ma per ricostruire due inviluppi ne servono due, uno per fattore. Moltiplicando e dividendo per $\sqrt2$ al numeratore ce ne sono due, $\sqrt2\cdot\sqrt2$, e al denominatore resta un $\sqrt2$: è il $\frac{1}{\sqrt2}$ che «resta fuori».

**Da dove viene il $1/\sqrt2$:** ogni inviluppo porta con sé un $\sqrt2$ (definizione (3)). Nel prodotto $SH$ i fattori $\sqrt2$ sono due, mentre $Y$, che è un solo inviluppo, ne deve avere uno solo. Il $1/\sqrt2$ toglie quello in più.

**Sanity check (🧩):** controllo sulle altezze della figura di slide 17, più sotto: torna $\sqrt2 AB$ ✓.

![[rappresentazione-rice-p24-appunti-filtro-equivalente.png]]
*Appunti a mano.*
- *A sinistra, due schemi: in alto il sistema reale, $x_p(t)$ → LTI con $h_p(t)$ → $y_p(t)$; sotto lo stesso sistema visto sugli inviluppi, $x(t)$ → LTI con $h(t)$ → $y(t)$.*
- *A destra la catena della (22), come sopra, con le tre note in verde e azzurro: «sostituisco l'uscita», «non altera nulla» su $u^2$, «resta fuori» sotto $\frac{1}{\sqrt2}$.*
- *In fondo la conclusione: l'inviluppo complesso di $y_p(t)$ nel dominio della frequenza è $Y(f) = \frac{1}{\sqrt2}X(f)H(f)$, «che si traduce nel dominio del tempo» in $y(t) = \frac{1}{\sqrt2}\,x(t) \ast h(t)$.*

### Derivazione — Eq. (23) · [[Rappresentazione_Rice.pdf#page=24|p. 24]], [[Rappresentazione_Rice.pdf#page=25|25]]
**Fonte:** p. 25 (slide 17); lo stesso passaggio chiude gli appunti di p. 24.
$$
y(t) = \mathcal{F}^{-1}[Y(f)] = \frac{1}{\sqrt2}\,\mathcal{F}^{-1}\big[S(f)\,H(f)\big] = \frac{1}{\sqrt2}\,s(t) * h(t) \qquad \text{prodotto in frequenza} \leftrightarrow \text{convoluzione nel tempo}
$$

### Derivazione — Eq. (24) e (25): le componenti I e Q dell'uscita · [[Rappresentazione_Rice.pdf#page=26|p. 26]]
> 📄 La catena è scritta a mano sotto lo schema della slide 18 (prima riga, penultima e ultima). La riga intermedia con i quattro termini e i commenti a destra sono 🧩 miei.

$$
\begin{aligned}
y(t) &= \frac{1}{\sqrt2}\,s(t) * h(t) && \text{(23)} \\
&= \frac{1}{\sqrt2}\,\big[s_c(t) + js_s(t)\big] * \big[h_c(t) + jh_s(t)\big] && \text{componenti I e Q: } s = s_c + js_s,\ h = h_c + jh_s \\
&= \frac{1}{\sqrt2}\,\big[s_c * h_c + j\,s_c * h_s + j\,s_s * h_c + j^2\,s_s * h_s\big] && \text{la convoluzione è bilineare: si sviluppa come un prodotto} \\
&= \frac{1}{\sqrt2}\,\big[s_c * h_c - s_s * h_s\big] + \frac{j}{\sqrt2}\,\big[s_c * h_s + s_s * h_c\big] && j^2 = -1;\ \text{raccolgo parte reale e parte immaginaria} \\
y_c(t) &= \frac{1}{\sqrt2}\big[s_c * h_c - s_s * h_s\big] && \text{parte reale: eq. (24)} \\
y_s(t) &= \frac{1}{\sqrt2}\big[s_s * h_c + s_c * h_s\big] && \text{parte immaginaria: eq. (25)}
\end{aligned}
$$
Servono **quattro convoluzioni reali**. È la stessa regola del prodotto di due numeri complessi, $(a + jb)(c + jd) = (ac - bd) + j(bc + ad)$, con la convoluzione al posto del prodotto.

> 🧩 Perché si può sviluppare come un prodotto: la convoluzione è lineare in ciascuno dei due argomenti, $(a + b) \ast c = a \ast c + b \ast c$ e $(\alpha a) \ast c = \alpha\,(a \ast c)$ anche per $\alpha = j$. I segnali $s_c, s_s, h_c, h_s$ sono reali, quindi ogni convoluzione $s_\cdot \ast h_\cdot$ è reale e la separazione tra parte reale e immaginaria è quella scritta.

### Derivazione — Controllo sulle altezze della figura (slide 17) · [[Rappresentazione_Rice.pdf#page=25|p. 25]]
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

### Passa-banda e banda base a confronto (slide 17) · [[Rappresentazione_Rice.pdf#page=25|p. 25]]

![[rappresentazione-rice-p25-filtraggio-spettri.png]]
*A sinistra, in banda passante: filtro $H_p(f)$, rettangoli di altezza $A$ attorno a $\pm f_c$; ingresso $S_p(f)$, triangoli di altezza $B$; uscita $Y_p(f)$, il triangolo "tagliato" dal rettangolo, altezza $AB$. A destra, in banda base complessa, gli stessi spettri attorno a 0 con un solo lobo: filtro $H(f)$ di altezza $\sqrt2 A$, ingresso $S(f)$ di altezza $\sqrt2 B$, uscita $Y(f)$ di altezza $\sqrt2 AB$.*

### Realizzazione con operazioni reali (slide 18) · [[Rappresentazione_Rice.pdf#page=26|p. 26]]

![[rappresentazione-rice-p26-filtro-banda-base-iq.png]]
- *Il segnale passa-banda $s_p(t)$ entra nel downconverter, che produce $s_c(t)$ e $s_s(t)$.*
- *Il riquadro tratteggiato, "operazioni reali in banda base", contiene quattro filtri reali: $s_c$ passa per $h_c$ e $h_s$, $s_s$ per $h_c$ e $h_s$. Due sommatori formano $y_c = s_c \ast h_c - s_s \ast h_s$ (con il segno meno) e $y_s = s_s \ast h_c + s_c \ast h_s$.*
- *A mano, sotto: la catena delle (24)–(25) riportata nella derivazione sopra.*
- *A mano, a destra: le due uscite confluiscono in un sommatore che forma $y(t)$, «segnale in banda base». $y(t)$ va a un DSP «che lavora in banda base».*

> ⚠️ Nella figura manca il fattore $1/\sqrt2$ delle (24)–(25): le uscite disegnate sono $\sqrt2\,y_c$ e $\sqrt2\,y_s$. La nota a mano sotto lo schema invece il $1/\sqrt2$ ce l'ha.

> 🧩 Il sommatore disegnato a mano va letto come $y = y_c + j\,y_s$: la componente Q entra moltiplicata per $j$, non sommata così com'è. Nel DSP le due componenti viaggiano come parte reale e parte immaginaria di un unico numero complesso.

> 🧩 Quando i termini incrociati spariscono (osservazione mia): se $h(t)$ è reale, cioè $h_s = 0$, le (24)–(25) diventano $y_c = \frac{1}{\sqrt2}\,s_c \ast h_c$ e $y_s = \frac{1}{\sqrt2}\,s_s \ast h_c$. I e Q vengono filtrati separatamente, senza mescolarsi. Per la simmetria hermitiana ([[segnali-banda-base-e-passa-banda]]), $h$ è reale quando $H(f) = H^\ast (-f)$, cioè quando il filtro passa-banda è simmetrico (coniugato) attorno a $f_c$. Nella figura della slide 17 il rettangolo $H(f)$ non è centrato in 0: in quel caso $h_s \neq 0$ e i termini incrociati ci sono.

### A cosa serve · [[Rappresentazione_Rice.pdf#page=21|p. 21]], [[Rappresentazione_Rice.pdf#page=26|p. 26]]

Gli appunti di p. 21 vedono upconverter, canale fisico e downconverter come **un unico canale** ([[upconversion-e-downconversion]]). Questa pagina dice come descriverlo: se il canale fisico è un filtro LTI passa-banda $h_p$, visto dalla banda base è il filtro $h/\sqrt2$ che agisce sull'inviluppo. Tutto si può quindi simulare e trattare in banda base. La nota a mano della slide 18 chiude il cerchio: l'uscita $y(t)$ è un segnale in banda base e va al DSP del ricevitore, che lavora in banda base.

> 🎯 Esame: ricavare la (22) partendo dai segnali analitici; spiegare il fattore $1/\sqrt2$; scrivere le (24)–(25) e disegnare lo schema con quattro filtri reali.

## Perché importa

Completa la rappresentazione in banda base. Non solo i segnali, ma anche i **sistemi** passa-banda (filtri, canali LTI) hanno un equivalente in banda base. Si può allora lavorare interamente con gli inviluppi, dal modulatore al demodulatore, senza mai tornare a $f_c$.

## Connessioni

- [[inviluppo-complesso]] — definizione (13) usata per $s$, $h$ e $y$; dipendenza dal riferimento $f_c$.
- [[segnale-analitico]] — la dimostrazione passa per $Y_p^+$, $S_p^+$, $H_p^+$.
- [[upconversion-e-downconversion]] — il downconverter fornisce $s_c$ e $s_s$ ai quattro filtri; la catena diventa un canale in banda base.
- [[segnali-banda-base-e-passa-banda]] — il canale passa-banda è un sistema LTI che soddisfa la (2).

## Fonti · [[Rappresentazione_Rice.pdf#page=23|p. 23]]–[[Rappresentazione_Rice.pdf#page=26|26]]

- [[rappresentazione-complessa-banda-base]]

_Aggiornato: 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-09-28 — re-ingest del PDF con appunti: dimostrazione della (22) dagli appunti di p.24 (trucchi $u^2$ e $\sqrt2/\sqrt2$ spiegati), (24)–(25) dalla nota a mano di p.26, uscita verso il DSP in banda base; 2026-09-25 — creazione da ingest Rappresentazione_Rice.pdf_
