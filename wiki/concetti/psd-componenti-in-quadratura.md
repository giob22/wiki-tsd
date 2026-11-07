---
tipo: concetto
importanza_esame: alta
prerequisiti: ["processi-passa-banda", "densita-spettrale-di-potenza", "segnale-analitico"]
fonti_pdf: ["Rappresentazione_Rice_processi.pdf#page=12", "Rappresentazione_Rice_processi.pdf#page=14", "Rappresentazione_Rice_processi.pdf#page=17", "Rappresentazione_Rice_processi.pdf#page=20"]
---

# PSD delle componenti in quadratura e dell'inviluppo complesso

## Definizione · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]], [[Rappresentazione_Rice_processi.pdf#page=14|14]], [[Rappresentazione_Rice_processi.pdf#page=17|17]]

Dato un processo passa-banda $x_p(t)$ reale, WSS e a media nulla ([[processi-passa-banda]]), la sua rappresentazione in banda base ha tre densità spettrali da conoscere:

- $S_{x_cx_c}(f)$ e $S_{x_sx_s}(f)$ — PSD delle componenti **in fase** e **in quadratura**; si ottengono da $S_{x_px_p}$ (eq. 13);
- $S_{xx}(f)$ — PSD dell'**inviluppo complesso** $x = x_c + jx_s$: è la PSD del **processo analitico** $x_p^+$ traslata nell'origine (eq. 14);
- le **cross-spectral density** $S_{x_cx_s}$, $S_{x_sx_c}$ ([[densita-spettrale-di-potenza]]).

Se $S_{x_px_p}$ è **simmetrica attorno a $f_c$** (caso molto frequente nei sistemi di trasmissione), tutto si semplifica: $S_{xx}$ è pari, $x_c$ e $x_s$ sono incoerenti e $S_{xx} = 2S_{x_cx_c} = 2S_{x_sx_s}$.

## Formule · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]]–[[Rappresentazione_Rice_processi.pdf#page=20|20]]

| Formula | Significato |
|---|---|
| $S_{x_cx_c}(f) = \frac12\big[S_{x_px_p}(f - f_c)\,u(f_c - f) + S_{x_px_p}(f + f_c)\,u(f + f_c)\big]$ | PSD della componente in fase (13) |
| $S_{x_sx_s}(f) = S_{x_cx_c}(f)$ | perché $R_{x_sx_s} = R_{x_cx_c}$ |
| $S_{x_p^+x_p^+}(f) = S_{x_px_p}(f)\,\lvert H(f)\rvert^2 = 2S_{x_px_p}(f)\,u(f)$ | PSD del processo analitico, filtro $H(f) = \sqrt2\,u(f)$ |
| $R_{xx}(\tau) = R_{x_p^+x_p^+}(\tau)\,e^{-j2\pi f_c\tau}$ | l'esponenziale complesso conserva la WSS |
| $S_{xx}(f) = S_{x_p^+x_p^+}(f + f_c) = 2S_{x_px_p}(f + f_c)\,u(f + f_c)$ | PSD dell'inviluppo (14) |
| $S_{xx}(f) = 2S_{x_cx_c}(f) + 2j\,S_{x_sx_c}(f)$ | dalla (12) |
| (caso simmetrico) $S_{xx}(-f) = S_{xx}(f)$, $\ R_{x_sx_c} \equiv 0$, $\ S_{xx} = 2S_{x_cx_c} = 2S_{x_sx_s}$ | spettro simmetrico attorno a $f_c$ |

> 🧮 Formula chiave: $S_{xx}(f) = 2S_{x_px_p}(f + f_c)\,u(f + f_c)$ — si prende lo spettro del processo reale, si elimina la parte a frequenze negative moltiplicando per $u(f)$, si raddoppia e si trasla a sinistra di $f_c$.

Simboli: $u(f)$ gradino unitario (0 per $f < 0$, 1 per $f > 0$); $f_c$ [Hz]; PSD in [W/Hz]. Ipotesi: $x_p$ reale, WSS, media nulla.

## Derivazioni

### Derivazione — PSD della componente in fase, eq. (13) · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]], [[Rappresentazione_Rice_processi.pdf#page=13|13]]
**Fonte:** slide 7 e appunti p. 13; qui ogni passaggio è commentato.
**Si parte da:** (6), $R_{x_cx_c}(\tau) = \frac12\big[R_{x_px_p}(\tau)\cos(2\pi f_c\tau) + \widehat{R}_{x_px_p}(\tau)\sin(2\pi f_c\tau)\big]$, e dal teorema di Wiener-Khinchin: $S_{x_cx_c} = \mathcal{F}\{R_{x_cx_c}\}$. Con $S \equiv S_{x_px_p}$ e $\widehat{S}(f) = -j\,\text{sgn}(f)\,S(f)$ (trasformata di $\widehat{R}$).

$$
\begin{aligned}
\mathcal{F}\{R\cos(2\pi f_c\tau)\} &= \tfrac12\big[S(f - f_c) + S(f + f_c)\big] && \text{modulazione: } \cos = \tfrac12(e^{j2\pi f_c\tau} + e^{-j2\pi f_c\tau}) \\
\mathcal{F}\{\widehat{R}\sin(2\pi f_c\tau)\} &= \tfrac{1}{2j}\big[\widehat{S}(f - f_c) - \widehat{S}(f + f_c)\big] && \sin = \tfrac{1}{2j}(e^{j2\pi f_c\tau} - e^{-j2\pi f_c\tau}) \\
&= \tfrac{1}{2j}\big[-j\,\text{sgn}(f - f_c)S(f - f_c) + j\,\text{sgn}(f + f_c)S(f + f_c)\big] && \widehat{S} = -j\,\text{sgn}\,S \\
S_{x_cx_c}(f) &= \tfrac12\Big[S(f - f_c)\,\tfrac{1 - \text{sgn}(f - f_c)}{2} + S(f + f_c)\,\tfrac{1 + \text{sgn}(f + f_c)}{2}\Big] && \text{somma; } \tfrac{-j}{2j} = -\tfrac12,\ \tfrac{j}{2j} = \tfrac12 \\
&= \tfrac12\big[S(f - f_c)\,u(f_c - f) + S(f + f_c)\,u(f + f_c)\big] && \tfrac{1 - \text{sgn}(x)}{2} = u(-x),\ \tfrac{1 + \text{sgn}(x)}{2} = u(x)
\end{aligned}
$$

Il risultato è la (13). Cosa fa: $S(f - f_c)$ è lo spettro traslato a destra di $f_c$; il gradino $u(f_c - f)$ tiene solo la parte a sinistra di $f_c$, cioè il lobo che sta intorno a $f = 0$ (quello che era in $+f_c$ nello spettro originale è stato portato in 0, quello in $-f_c$ è finito in $-2f_c$ e viene eliminato). Analogo per $S(f + f_c)$.

**Sanity check:** $S_{x_sx_s} = S_{x_cx_c}$ perché $R_{x_sx_s} = R_{x_cx_c}$ (10). Per l'esempio in [[rumore-in-banda-passante]] si ritrova il valore delle slide 21–25.

### Derivazione — Cross-PSD $S_{x_cx_s}$ · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]], [[Rappresentazione_Rice_processi.pdf#page=13|13]]
**Fonte:** la slide 7 dice solo che si ottiene trasformando (8) e (9); negli appunti p. 13 compare $R_{x_cx_s} = -R_{x_sx_c}$.
> 🧩 Derivazione mia, stessi passaggi della (13).

**Si parte da:** (8), $R_{x_cx_s}(\tau) = \frac12\big[R\sin(2\pi f_c\tau) - \widehat{R}\cos(2\pi f_c\tau)\big]$.

$$
\begin{aligned}
S_{x_cx_s}(f) &= \tfrac12\Big\{\tfrac{1}{2j}\big[S(f - f_c) - S(f + f_c)\big] - \tfrac12\big[\widehat{S}(f - f_c) + \widehat{S}(f + f_c)\big]\Big\} && \mathcal{F}\{R\sin\},\ \mathcal{F}\{\widehat{R}\cos\} \\
&= \tfrac{j}{4}\Big\{S(f - f_c)\big[\text{sgn}(f - f_c) - 1\big] + S(f + f_c)\big[\text{sgn}(f + f_c) + 1\big]\Big\} && \tfrac{1}{2j} = -\tfrac{j}{2}; \ \widehat{S} = -j\,\text{sgn}\,S \\
&= \tfrac{j}{2}\big[S(f + f_c)\,u(f + f_c) - S(f - f_c)\,u(f_c - f)\big] && \text{sgn}(x) - 1 = -2u(-x),\ \text{sgn}(x) + 1 = 2u(x)
\end{aligned}
$$

**Sanity check:** è puramente immaginaria e dispari, coerente con $R_{x_cx_s}$ reale e dispari (derivazione in [[processi-passa-banda]]). Con $S_{x_sx_c} = -S_{x_cx_s}$ nella (12) si ritrova la (14):

$$S_{xx} = 2S_{x_cx_c} - 2j\,S_{x_cx_s} = \big[S_-u_- + S_+u_+\big] + \big[S_+u_+ - S_-u_-\big] = 2S(f + f_c)\,u(f + f_c)$$

con $S_\mp = S(f \mp f_c)$ e $u_- = u(f_c - f)$, $u_+ = u(f + f_c)$ ✓.

### Derivazione — PSD dell'inviluppo, eq. (14) · [[Rappresentazione_Rice_processi.pdf#page=14|p. 14]], [[Rappresentazione_Rice_processi.pdf#page=15|15]], [[Rappresentazione_Rice_processi.pdf#page=16|16]]
**Fonte:** slide 8 e appunti p. 15–16.
**Si parte da:** il processo analitico $x_p^+$ è l'uscita del filtro con $H(f) = \sqrt2\,u(f)$ ([[segnale-analitico]]) con ingresso $x_p$; $S_{\text{out}} = S_{\text{in}}\,|H|^2$ ([[processi-e-sistemi-lti]]).

$$
\begin{aligned}
S_{x_p^+x_p^+}(f) &= S_{x_px_p}(f)\,\lvert\sqrt2\,u(f)\rvert^2 = 2S_{x_px_p}(f)\,u(f) && u^2 = u \\
R_{xx}(\tau) &= E\big[x_p^+(t)\,e^{-j2\pi f_ct}\;x_p^{+\ast}(t-\tau)\,e^{+j2\pi f_c(t-\tau)}\big] && x = x_p^+\,e^{-j2\pi f_ct}, \text{ coniugato in } t-\tau \\
&= E\big[x_p^+(t)\,x_p^{+\ast}(t-\tau)\big]\,e^{-j2\pi f_c\tau} && \text{esponenziali portati fuori: } e^{-j2\pi f_ct + j2\pi f_c(t-\tau)} = e^{-j2\pi f_c\tau} \\
&= R_{x_p^+x_p^+}(\tau)\,e^{-j2\pi f_c\tau} && \text{dipende solo da } \tau \\
S_{xx}(f) &= \mathcal{F}\{R_{x_p^+x_p^+}(\tau)\,e^{-j2\pi f_c\tau}\} = S_{x_p^+x_p^+}(f + f_c) && \text{moltiplicare per } e^{-j2\pi f_c\tau} \text{ sposta lo spettro di } f_c \text{ a sinistra} \\
&= 2S_{x_px_p}(f + f_c)\,u(f + f_c) && \text{(14)}
\end{aligned}
$$

La seconda riga mostra che **moltiplicare per un esponenziale complesso conserva la WSS**: $R_{xx}$ dipende solo da $\tau$ (e la media resta zero).

**Riassunto operativo (appunti p. 16)** per avere la PSD dell'inviluppo di un processo passa-banda:
1. si disegna la PSD del processo passa-banda, $S_{x_px_p}(f)$;
2. si eliminano le frequenze negative con $H(f) = \sqrt2\,u(f)$ e si moltiplica per $\sqrt2$ (il fattore **conserva la potenza**), ottenendo $S_{x_p^+x_p^+} = 2S_{x_px_p}u$;
3. si trasla a sinistra di $f_c$, portando la PSD del segnale analitico centrata nell'origine.

**Sanity check (potenza):** $\int S_{xx}\,df = \int S_{x_p^+x_p^+}\,df = \int_0^{+\infty}2S_{x_px_p}\,df = \int_{-\infty}^{+\infty}S_{x_px_p}\,df$, perché $S_{x_px_p}$ è pari (processo reale): la potenza dell'inviluppo è quella del processo passa-banda.

### Derivazione — Spettro simmetrico attorno a $f_c$ · [[Rappresentazione_Rice_processi.pdf#page=17|p. 17]], [[Rappresentazione_Rice_processi.pdf#page=18|18]], [[Rappresentazione_Rice_processi.pdf#page=19|19]]
**Fonte:** slide 9 e appunti p. 18–19.
**Ipotesi:** $S_{x_px_p}(f_c + g) = S_{x_px_p}(f_c - g)$ per ogni $g$ (simmetria attorno alla portante).

$$
\begin{aligned}
S_{xx}(-f) &= 2S_{x_px_p}(-f + f_c)\,u(-f + f_c) && \text{(14) in } -f \\
&= 2S_{x_px_p}(f + f_c)\,u(f + f_c) = S_{xx}(f) && \text{simmetria: } S(f_c - f) = S(f_c + f); \ u(f_c - f) = u(f_c + f) = 1 \text{ sul lobo}
\end{aligned}
$$

> 🧩 L'ultima uguaglianza usa che i due gradini valgono entrambi 1 dove $S(f + f_c) \ne 0$, cioè per $|f| < W/2$ con $f_c > W/2$: fuori dal lobo $S = 0$ e il gradino non conta.

Quindi $S_{xx}$ è **pari**. Poiché $S_{xx}$ è reale e pari, la sua antitrasformata $R_{xx}$ è **reale e pari**, dunque $\text{Im}\{R_{xx}(\tau)\} = 0$ per ogni $\tau$. Dalla (12):

$$
\begin{aligned}
R_{xx}(\tau) &= 2R_{x_cx_c}(\tau) + 2j\,R_{x_sx_c}(\tau) && \text{(12)} \\
\text{Im}\{R_{xx}\} = 0 &\Rightarrow R_{x_sx_c}(\tau) = 0 \ \ \forall\tau \Rightarrow R_{x_cx_s}(\tau) = -R_{x_sx_c}(\tau) = 0 && \text{(10); } x_p \text{ WSS}
\end{aligned}
$$

$x_c$ e $x_s$ sono **incoerenti** ($R_{x_cx_s} \equiv 0$). Con medie nulle sono anche **incorrelate**; se $x_p$ è gaussiano, sono **statisticamente indipendenti** (e non solo nello stesso istante: per ogni coppia di istanti). Infine, trasformando la (12):

$$S_{xx}(f) = 2S_{x_cx_c}(f) + 2j\,S_{x_sx_c}(f) = 2S_{x_cx_c}(f) = 2S_{x_sx_s}(f) \qquad (S_{x_sx_c} = 0)$$

Gli appunti aggiungono che $S_{xx}$ è reale per definizione: $S_{xx}(f) = \lim_{T\to\infty}\frac{1}{2T}E[\lvert X_T(f)\rvert^2]$.

**Confronto con il caso generale (appunti p. 19):** l'incoerenza di $x_c$ e $x_s$ è sempre garantita nel solo istante coincidente ($\tau = 0$, vedi [[processi-passa-banda]]); quando lo spettro è simmetrico attorno a $f_c$ lo è per ogni $\tau$ — le due componenti sono *completamente* incoerenti/incorrelate.

## Spiegazione · [[Rappresentazione_Rice_processi.pdf#page=20|p. 20]]

![[processi-passabanda-p20-vista-grafica-psd.png|650]]
*(a) PSD del processo passa-banda: due lobi in $\pm f_c$. (b) Si elimina la parte a frequenze negative e si moltiplica per 2 (filtro con $\lvert H\rvert^2 = 2u(f)$): rimane il solo lobo in $+f_c$, di altezza $2A$. (c) Si trasla di $-f_c$: PSD dell'inviluppo, pari per l'ipotesi di simmetria, con $R_{xx}$ reale. (d) Dividendo per 2 si ha $S_{x_cx_c} = S_{x_sx_s}$ (altezza $A$): $S_{xx} = 2S_{x_cx_c}$.*

I quattro grafici sono la costruzione di (14) a occhio. Il passaggio (a)→(b) è l'unica operazione sulla PSD del processo reale; (b)→(c) è solo una traslazione. Quando il lobo è simmetrico attorno a $f_c$, ritrovato nell'origine è simmetrico attorno a 0, cioè pari. Una PSD pari ha antitrasformata reale: ecco perché la parte immaginaria di $R_{xx}$ ($\propto R_{x_sx_c}$) sparisce.

Se il lobo **non** fosse simmetrico, $S_{xx}$ non sarebbe pari, $R_{xx}$ sarebbe complessa e $x_c$, $x_s$ avrebbero una crosscorrelazione non nulla fuori da $\tau = 0$.

## Perché importa

Il rumore passa-banda dei sistemi reali ha quasi sempre una PSD simmetrica attorno alla portante (filtro del ricevitore centrato su $f_c$). In questo caso le due componenti in quadratura sono processi reali indipendenti con la stessa PSD: la base per i ricevitori in banda base. Vedi l'esempio in [[rumore-in-banda-passante]].

## Connessioni

- [[processi-passa-banda]] — i risultati su $R_{x_cx_c}$, $R_{x_cx_s}$ da cui si ricavano le PSD.
- [[densita-spettrale-di-potenza]] — Wiener-Khinchin e cross-spectral density.
- [[segnale-analitico]] — il filtro $\sqrt2\,u(f)$ e il raddoppio della PSD dei soli segnali a frequenze positive.
- [[processi-e-sistemi-lti]] — $S_{\text{out}} = S_{\text{in}}|H|^2$ per il processo analitico.
- [[processo-gaussiano]] — incorrelate ⇒ indipendenti.
- [[rumore-in-banda-passante]] — applicazione con costruzione grafica.

## Fonti · [[Rappresentazione_Rice_processi.pdf#page=12|p. 12]]–[[Rappresentazione_Rice_processi.pdf#page=20|20]]

[[rappresentazione-processi-passa-banda]] — Rappresentazione_Rice_processi.pdf, slide 7–10 e appunti.

_Aggiornato: 2026-11-01 — creazione da ingest Rappresentazione_Rice_processi.pdf_
