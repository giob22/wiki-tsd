---
tipo: concetto
importanza_esame: alta
prerequisiti: ["processi-passa-banda", "psd-componenti-in-quadratura", "processo-gaussiano"]
fonti_pdf: ["Rappresentazione_Rice_processi.pdf#page=21", "Rappresentazione_Rice_processi.pdf#page=22", "Rappresentazione_Rice_processi.pdf#page=24", "Rappresentazione_Rice_processi.pdf#page=25"]
---

# Rumore in banda passante

## Definizione · [[Rappresentazione_Rice_processi.pdf#page=21|p. 21]], [[Rappresentazione_Rice_processi.pdf#page=22|22]]

Il **rumore in banda passante** $w_p(t)$ è un processo WSS, a media nulla, con PSD **costante** $S_{w_pw_p}(f) = \frac{N_0}{2}$ in una banda di larghezza $W$ centrata in $\pm f_c$, e nulla altrove. Un rumore bianco gaussiano (AWGN) avrebbe $S(f) = \frac{N_0}{2}$ su **tutte** le frequenze, cioè $R_{ww}(\tau) = \frac{N_0}{2}\delta(\tau)$ e potenza media infinita: non esiste fisicamente. Nei sistemi reali il ricevitore **filtra** il segnale in ingresso con un filtro di banda $W$ centrato su $f_c$, e ciò che resta è un rumore con $S = N_0/2$ e banda $W$.

Le componenti in quadratura $w_c$ e $w_s$ del rumore sono le componenti di $w_p$ come in [[processi-passa-banda]]. Interessano le loro PSD, quella dell'inviluppo $w = w_c + jw_s$ e il legame con la potenza.

## Formule · [[Rappresentazione_Rice_processi.pdf#page=21|p. 21]], [[Rappresentazione_Rice_processi.pdf#page=22|22]], [[Rappresentazione_Rice_processi.pdf#page=24|24]], [[Rappresentazione_Rice_processi.pdf#page=25|25]]

| Formula | Significato |
|---|---|
| $S_{w_pw_p}(f) = \frac{N_0}{2}$ per $\lvert\lvert f\rvert - f_c\rvert < \frac W2$ | PSD del rumore passa-banda [W/Hz] |
| $S_{w_cw_c}(f) = S_{w_sw_s}(f) = \frac{N_0}{2}$ per $\lvert f\rvert < \frac W2$ | PSD delle componenti in quadratura |
| $S_{ww}(f) = 2S_{w_cw_c}(f) = N_0$ per $\lvert f\rvert < \frac W2$ | PSD dell'inviluppo complesso |
| $P_{w_p} = 2W\cdot\frac{N_0}{2} = N_0W = P_w$ | potenza del rumore passa-banda = potenza dell'inviluppo [W] |

> 🧮 Formula chiave: $S_{w_cw_c} = S_{w_sw_s} = \frac{N_0}{2}$ e $S_{ww} = N_0$ per $\lvert f\rvert < W/2$; $P_{w_p} = N_0W = P_w$.

Simboli: $N_0/2$ [W/Hz] livello della PSD bilatera; $W$ [Hz] larghezza di ciascun lobo (convenzione delle slide 10–13); $f_c$ [Hz] portante, $f_c > W/2$.

## Derivazioni

### Derivazione — PSD delle componenti in quadratura · [[Rappresentazione_Rice_processi.pdf#page=21|p. 21]], [[Rappresentazione_Rice_processi.pdf#page=22|22]]
**Fonte:** slide 11 e appunti p. 22, che scrivono $S_{ww}(f) = 2S_{w_pw_p}(f - f_c)\,u(f - f_c) = N_0\,u(f - f_c)$ per $\lvert f\rvert < W/2$. Il segno di $f_c$ negli argomenti va letto come nella (14), cioè $f + f_c$ (l'inviluppo si trasla verso sinistra).
**Si parte da:** (14) di [[psd-componenti-in-quadratura]].

$$
\begin{aligned}
S_{ww}(f) &= 2S_{w_pw_p}(f + f_c)\,u(f + f_c) && \text{(14)} \\
&= 2\cdot\frac{N_0}{2}\cdot 1 = N_0 \quad (\lvert f\rvert < W/2) && S_{w_pw_p}(f + f_c) = N_0/2 \text{ sul lobo traslato; } u = 1 \text{ per } f > -f_c \\
S_{ww}(f) &= 2S_{w_cw_c}(f) && \text{PSD simmetrica attorno a } f_c \text{ (reale e costante)} \\
\Rightarrow S_{w_cw_c}(f) &= S_{w_sw_s}(f) = \frac{S_{ww}}{2} = \frac{N_0}{2} \quad (\lvert f\rvert < W/2) && \text{caso simmetrico}
\end{aligned}
$$

Il motivo per cui $S_{w_pw_p}$ è simmetrica rispetto a $f_c$: è reale e **costante** sul lobo, quindi uguale a sinistra e a destra di $f_c$.

### Derivazione — Costruzione grafica con (13) · [[Rappresentazione_Rice_processi.pdf#page=24|p. 24]], [[Rappresentazione_Rice_processi.pdf#page=25|25]]
**Fonte:** slide 12–13, che applicano la (13): prima si trasla la PSD passa-banda di $\pm f_c$, poi si moltiplica per i gradini $u(f_c - f)$ e $u(f + f_c)$.
**Si parte da:** $S_{w_cw_c} = \frac12\big[S(f - f_c)\,u(f_c - f) + S(f + f_c)\,u(f + f_c)\big]$.

![[processi-passabanda-p24-rumore-costruzione-1.png|560]]
*(a) $S_{w_pw_p}$: due lobi di altezza $N_0/2$ e larghezza $W$ in $\pm f_c$. (b) Traslata di $+f_c$: i lobi vanno in $0$ e $2f_c$. (c) Traslata di $-f_c$: lobi in $-2f_c$ e $0$. (d)–(e) I gradini $u(f_c - f)$ e $u(f + f_c)$.*

Ciascun gradino mantiene solo il lobo vicino a $f = 0$ e taglia quello in $\pm 2f_c$:

$$
\begin{aligned}
S_{w_pw_p}(f - f_c)\,u(f_c - f) &= \tfrac{N_0}{2} && \lvert f\rvert < W/2 \ \text{(il lobo in } 2f_c \text{ cade dove } f > f_c\text{, quindi viene azzerato)} \\
S_{w_pw_p}(f + f_c)\,u(f + f_c) &= \tfrac{N_0}{2} && \lvert f\rvert < W/2 \ \text{(il lobo in } -2f_c \text{ cade dove } f < -f_c\text{)} \\
S_{w_cw_c}(f) &= \tfrac12\Big[\tfrac{N_0}{2} + \tfrac{N_0}{2}\Big] = \tfrac{N_0}{2} && \text{somma e dimezzo (13)}
\end{aligned}
$$

![[processi-passabanda-p25-rumore-costruzione-2.png|560]]
*(f), (g) I due prodotti: restano i soli lobi centrati in 0, di altezza $N_0/2$. (h) $\frac12[(f)+(g)]$: $S_{w_cw_c} = S_{w_sw_s} = N_0/2$ su $\lvert f\rvert < W/2$. (i) Moltiplicando per 2: $S_{ww} = N_0$.*

> 🧩 Nel disegno (h) i due contributi sono sovrapposti: ciascuno vale $\tfrac12\cdot\tfrac{N_0}{2} = \tfrac{N_0}{4}$ (blu e arancione) e insieme danno $\tfrac{N_0}{2}$.

### Derivazione — Conservazione della potenza · [[Rappresentazione_Rice_processi.pdf#page=22|p. 22]], [[Rappresentazione_Rice_processi.pdf#page=25|25]]
**Fonte:** appunti p. 22, slide 13.

$$
\begin{aligned}
P_{w_p} &= \int_{-\infty}^{+\infty}S_{w_pw_p}(f)\,df = 2W\cdot\frac{N_0}{2} = N_0W && \text{due lobi di larghezza } W \text{ e altezza } N_0/2 \\
P_w &= \int_{-W/2}^{W/2}S_{ww}(f)\,df = N_0\cdot W = N_0W && \text{un lobo di larghezza } W \text{ e altezza } N_0 \\
P_{w_c} + P_{w_s} &= 2\cdot\frac{N_0}{2}W = N_0W && \text{ciascuna componente: } \tfrac{N_0}{2}\cdot W
\end{aligned}
$$

La potenza del processo originale coincide con quella dell'inviluppo complesso, come per i segnali deterministici (il $\sqrt2$ nella definizione di segnale analitico serve a questo). **Unità:** $N_0$ in W/Hz, $W$ in Hz ⇒ potenze in W. **Sanity check:** $N_0W$ cresce con la banda: più banda, più rumore.

### Derivazione — Indipendenza delle componenti · [[Rappresentazione_Rice_processi.pdf#page=23|p. 23]]
**Fonte:** appunti p. 23.

Poiché $S_{ww}(f)$ è **reale** (il rumore passa-banda ha spettro simmetrico attorno a $f_c$), $S_{w_cw_s}(f) = 0$ per ogni $f$: le componenti $w_c$ e $w_s$ sono **incoerenti**. Con media nulla, sono **incorrelate**, e nello stesso istante sono statisticamente **indipendenti se $w_p$ è gaussiano** ([[processo-gaussiano]], [[psd-componenti-in-quadratura]]).

## Spiegazione

Nell'esempio il rumore è «bianco dentro la banda»: tutte le frequenze utili ricevono la stessa potenza per unità di frequenza. Il filtro del ricevitore è centrato su $f_c$, quindi lo spettro risulta simmetrico attorno a $f_c$ e vale tutta la teoria del caso simmetrico: in banda base le due componenti in quadratura sono processi reali con la stessa PSD piatta $N_0/2$ e l'inviluppo ha PSD $N_0$.

Perché $N_0$ e non $N_0/2$ per l'inviluppo? Nell'inviluppo si eliminano le frequenze negative (un lobo su due) raddoppiando l'altezza: $2\cdot N_0/2 = N_0$. La potenza non cambia perché la banda dell'inviluppo è la metà della banda totale ($W$ invece di $2W$).

## Perché importa

È il modello del rumore nel ricevitore, dove il DSP lavora sull'inviluppo in banda base ([[inviluppo-complesso]]): sapere che $w_c$ e $w_s$ hanno la stessa PSD piatta e, se il rumore è gaussiano, sono **indipendenti** descrive statisticamente il rumore in banda base.

## Connessioni

- [[psd-componenti-in-quadratura]] — le formule (13) e (14) applicate.
- [[processi-passa-banda]] — componenti in quadratura di un processo.
- [[processo-gaussiano]] — incorrelate ⇒ indipendenti.
- [[densita-spettrale-di-potenza]] — potenza come area della PSD.
- [[correlazione-e-covarianza]] — incorrelazione, quando la media è nulla.

## Fonti · [[Rappresentazione_Rice_processi.pdf#page=21|p. 21]]–[[Rappresentazione_Rice_processi.pdf#page=25|25]]

[[rappresentazione-processi-passa-banda]] — Rappresentazione_Rice_processi.pdf, slide 11–13 e appunti.

_Aggiornato: 2026-11-01 — creazione da ingest Rappresentazione_Rice_processi.pdf_
