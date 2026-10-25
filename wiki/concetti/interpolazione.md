---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=17", "Campionamento_AD_DA.pdf#page=22", "Campionamento_AD_DA.pdf#page=23", "Campionamento_AD_DA.pdf#page=24"]
---

# Interpolazione: ideale (serie di Shannon), ZOH, FOH

## Definizione · [[Campionamento_AD_DA.pdf#page=6|p. 6]], [[Campionamento_AD_DA.pdf#page=17|p. 17]]

L'**interpolazione** ricostruisce un segnale a tempo continuo $x_r(t)$ dai campioni $x(n)$: è l'unica operazione della conversione D/A. Si modella come il passaggio di $x_\delta(t) = \sum_n x(n)\delta(t-nT_c)$ in un **filtro di ricostruzione** $h_r(t)$:
$$x_r(t) = \sum_{n} x(n)\,h_r(t-nT_c)$$

> 🧩 Derivazione mia (forma generale): $x_r = x_\delta \ast h_r$ e $\delta(t-nT_c)\ast h_r(t) = h_r(t-nT_c)$. Le tre interpolazioni seguenti sono casi particolari di questa formula.

## Formule · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]

| Interpolatore | $h_r(t)$ | $H_r(f)$ | Proprietà |
|---|---|---|---|
| **Ideale** (serie di Shannon) | $\text{sinc}\left(\frac{t}{T_c}\right)$ | $T_c\,\Pi(fT_c)$ | instabile, non causale → **non realizzabile** |
| **ZOH** (mantenimento) | $\Pi\left(\frac{t-T_c/2}{T_c}\right)$ | $T_c\,\text{sinc}(fT_c)\,e^{-j\pi fT_c}$ | stabile e **causale** → realizzabile |
| **FOH** (lineare) | $\Lambda\left(\frac{t}{T_c}\right)$ | $T_c\,\text{sinc}^2(fT_c)$ | stabile, **non causale** → realizzabile con un ritardo di $T_c$ |

Simboli: $\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$; $\Pi(x)$ = rettangolo unitario su $|x|<1/2$; $\Lambda(x) = 1-|x|$ per $|x|\le1$ (triangolo); $T_c$ [s].

> 🧮 Formula chiave — **Serie di Shannon**:
> $$x_r(t) = \sum_{n=-\infty}^{+\infty}x_a(nT_c)\,\text{sinc}\left(\frac{t-nT_c}{T_c}\right)$$

> ⚠️ Contraddizione (refuso nelle slide): p. 24 scrive «First-Order Hold (ZOH)». La sigla corretta è **FOH**.

## Derivazioni

### Derivazione — Risposta impulsiva dell'interpolatore ideale · [[Campionamento_AD_DA.pdf#page=17|p. 17]]
$$
\begin{aligned}
H_r(f) &= T_c\,\Pi\left(\tfrac{f}{2f_r}\right),\quad f_r = f_c/2 = \tfrac{1}{2T_c} && \text{scelta comune} \\
&= T_c\,\Pi(fT_c) && 2f_r = 1/T_c \\
\Pi(f/W) &\xleftrightarrow{FT^{-1}} W\,\text{sinc}(Wt) && \text{coppia nota} \\
h_r(t) &= T_c\cdot\tfrac{1}{T_c}\,\text{sinc}\left(\tfrac{t}{T_c}\right) = \text{sinc}\left(\tfrac{t}{T_c}\right) && W = 1/T_c
\end{aligned}
$$
Sostituendo in $x_r(t) = \sum_n x(n)h_r(t-nT_c)$ si ottiene la serie di Shannon.
**Sanity check** (🧩 mio): in $t = mT_c$ si ha $\text{sinc}(m-n) = 1$ se $n=m$ e 0 altrimenti, quindi $x_r(mT_c) = x_a(mT_c)$. L'interpolatore passa esattamente per i campioni.

### Derivazione — Filtro ZOH · [[Campionamento_AD_DA.pdf#page=23|p. 23]]
$$
\begin{aligned}
\Pi\left(\tfrac{t}{T_c}\right) &\xleftrightarrow{FT} T_c\,\text{sinc}(fT_c) && \text{coppia nota (rettangolo di durata } T_c) \\
\Pi\left(\tfrac{t-T_c/2}{T_c}\right) &\xleftrightarrow{FT} T_c\,\text{sinc}(fT_c)\,e^{-j2\pi f T_c/2} && \text{ritardo di } T_c/2 \\
&= T_c\,\text{sinc}(fT_c)\,e^{-j\pi fT_c}
\end{aligned}
$$
$h_r(t)$ ha supporto $[0, T_c]$, quindi è **causale**; $\int|h_r| = T_c<\infty$, quindi è **stabile** (BIBO).
Nel tempo: $x_r(t) = x(n)$ per $t\in[nT_c,(n+1)T_c)$, cioè ogni campione è mantenuto fino al successivo.

### Derivazione — Filtro FOH · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=23|p. 23]], [[Campionamento_AD_DA.pdf#page=24|24]]
> 🧩 Derivazione mia
$$
\begin{aligned}
\Pi\left(\tfrac{t}{T_c}\right) * \Pi\left(\tfrac{t}{T_c}\right) &= T_c\,\Lambda\left(\tfrac{t}{T_c}\right) && \text{autoconvoluzione del rettangolo} \\
\Lambda\left(\tfrac{t}{T_c}\right) &= \tfrac{1}{T_c}\,\Pi * \Pi \xleftrightarrow{FT} \tfrac{1}{T_c}\,[T_c\,\text{sinc}(fT_c)]^2 && \text{convoluzione} \leftrightarrow \text{prodotto} \\
&= T_c\,\text{sinc}^2(fT_c)
\end{aligned}
$$
$h_r(t)$ ha supporto $[-T_c, T_c]$, quindi **non causale**: per $t$ tra $nT_c$ e $(n+1)T_c$ serve già il campione $n+1$. Ritardando di $T_c$ (un campione) il filtro diventa causale.
Nel tempo, per $t\in[nT_c,(n+1)T_c]$ contribuiscono solo i due triangoli centrati in $nT_c$ e $(n+1)T_c$, con pesi $1-\tau$ e $\tau$ dove $\tau = (t-nT_c)/T_c$: è l'**interpolazione lineare** tra campioni consecutivi.

**Confronto spettrale** (🧩 mio): fuori banda, $|\text{sinc}^2|$ decresce come $1/f^2$ e $|\text{sinc}|$ come $1/f$. Per questo la FOH ha meno contenuto ad alta frequenza della ZOH.

![[grafico-interpolatori-risposta.png]]
*🧩 Grafico mio delle tre $H_r(f)$ di p. 17, p. 23, p. 24 (moduli, normalizzati a $T_c$). L'ideale passa tutto fino a $f_c/2$ e blocca tutto oltre. ZOH e FOH hanno zeri in $f_c, 2f_c, \dots$, cioè al centro delle repliche, ma lasciano passare i lobi laterali: la ZOH molto (picco ≈ 0.22), la FOH molto meno (≈ 0.05). Entrambe attenuano anche la banda utile: in $f_c/2$ la ZOH vale $\text{sinc}(0.5) = 2/\pi \approx 0.64$, la FOH $(2/\pi)^2 \approx 0.41$. Da qui l'utilità del LPF aggiuntivo dopo lo ZOH.*

## Spiegazione

### Interpolazione ideale · [[Campionamento_AD_DA.pdf#page=17|p. 17]]

- La ricostruzione prevista dal teorema del campionamento usa un LPF ideale $H_r(f) = T_c\Pi(f/2f_r)$ con $f_m\le f_r\le f_c-f_m$; scegliendo $f_r = f_c/2$ si ottiene la serie di Shannon.
- L'interpolazione ideale usa segnali **sinc**, che hanno **banda rigorosamente limitata**.
- Non è fisicamente realizzabile: il filtro è **instabile** e **non causale**.

![[campionamento-p17-serie-shannon.png]]
*Serie di Shannon: ogni campione (asta nera) genera una sinc centrata in $nT_c$ e scalata del valore del campione (curve sottili). La loro somma è il segnale ricostruito $x_r(t)$ (rosso), che passa esattamente per tutti i campioni. Asse orizzontale: $t/T_c$.*

### Perché serve l'interpolazione non ideale · [[Campionamento_AD_DA.pdf#page=19|p. 19]]

L'interpolazione con sinc è una delle **due ipotesi ideali** del teorema di Shannon (l'altra è la banda rigorosamente limitata, vedi [[aliasing]]). Nella pratica va sostituita da interpolatori realizzabili.

### Interpolazione non ideale in frequenza · [[Campionamento_AD_DA.pdf#page=22|p. 22]]

![[campionamento-p22-interpolazione-non-ideale.png]]

(a) $X_\delta(f)$: repliche di altezza $1/T_c$ con passo $f_c$ (senza sovrapposizione). Un $H_r(f)$ reale (b), di altezza massima $T_c$ (in tratteggio l'ideale su $[-f_c/2, f_c/2]$), non è un rettangolo: la transizione è graduale, quindi attenua in parte la banda utile e lascia passare residui delle repliche intorno a $\pm f_c$. Lo spettro ricostruito $X_r(f)$ (c) contiene così componenti spurie ad alta frequenza.

### ZOH · [[Campionamento_AD_DA.pdf#page=23|p. 23]]

- Nella pratica il filtro di interpolazione ideale (LPF ideale) **non è fisicamente realizzabile**.
- Un'interpolazione più semplice **mantiene** il valore di un campione fino al campione successivo: è lo **Zero-Order Hold** (ZOH), o **interpolazione a mantenimento**.
- Approssima male il segnale: l'effetto "**scalettatura**" produce un elevato contenuto spettrale ad alta frequenza.
- È un sistema LTI **stabile e causale**, quindi fisicamente realizzabile.
- L'approssimazione si migliora con un ulteriore **filtraggio LPF** del segnale ZOH, che elimina le transizioni brusche e rende il segnale ricostruito più "**dolce**".

![[campionamento-p23-zoh.png]]
*$x_{ZOH}(t)$: gradini di durata $T_c$ che partono da ogni campione, confrontati con il segnale originale tratteggiato*

### FOH · [[Campionamento_AD_DA.pdf#page=24|p. 24]]

- Una ricostruzione **più accurata** si ottiene interpolando **linearmente** due campioni consecutivi: è il **First-Order Hold** (FOH), o **interpolazione lineare**.
- Approssima meglio il segnale e ha minor contenuto spettrale ad alta frequenza.
- È un sistema LTI **stabile** ma **non causale**; diventa fisicamente realizzabile introducendo un **ritardo di $T_c$** (un campione).

![[campionamento-p24-foh.png]]
*$x_{FOH}(t)$: spezzata che unisce i campioni consecutivi, confrontata con il segnale originale tratteggiato*

> 🎯 Esame: confronto ideale/ZOH/FOH su $h_r$, $H_r$, causalità, stabilità e realizzabilità. Perché la sinc non è realizzabile: è non causale (ha supporto su tutto $\mathbb{R}$) e instabile ($\int|\text{sinc}| = \infty$).
> 📚 Fonte esterna: la non assoluta integrabilità della sinc ($\int|\sin x/x|\,dx$ diverge) è un risultato standard di analisi; la slide dice solo «instabile e non causale».

## Perché importa · [[Campionamento_AD_DA.pdf#page=6|p. 6]]

È l'unica operazione della conversione D/A. Il passaggio da interpolatore ideale (irrealizzabile) a ZOH/FOH (realizzabili) mostra il compromesso tra fedeltà della ricostruzione e realizzabilità fisica del filtro.

## Connessioni

- [[lab-interpolazione]] — 🧪 laboratorio (non d'esame): ZOH, FOH e sinc applicati a un trapezio in Matlab; perché la convoluzione dura la somma delle durate e dove va tagliata.
- [[teorema-del-campionamento]] — dimostra che l'interpolazione ideale ricostruisce perfettamente.
- [[aliasing]] — l'altra ipotesi ideale (banda limitata) e le sue violazioni.
- [[conversione-ad-da]] — l'interpolazione è la D/A.

## Fonti · [[Campionamento_AD_DA.pdf#page=17|p. 17]], [[Campionamento_AD_DA.pdf#page=19|p. 19]], [[Campionamento_AD_DA.pdf#page=24|p. 24]]

- [[campionamento-conversione-ad-da]]

_Aggiornato: 2026-10-20 — formule con * (convoluzione, coniugato) scritte con \ast, perché in una riga in corsivo l'asterisco spezzava la formula; 2026-09-30 — collegamento al laboratorio Matlab; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
