---
tipo: concetto
importanza_esame: alta
prerequisiti: ["sincronizzazione", "stima-dei-parametri", "inviluppo-complesso"]
fonti_pdf: ["Synchro_Kay_example (1).pdf#page=29", "Synchro_Kay_example (1).pdf#page=30", "Synchro_Kay_example (1).pdf#page=31", "Synchro_Kay_example (1).pdf#page=32", "Synchro_Kay_example (1).pdf#page=33", "Synchro_Kay_example (1).pdf#page=34", "Synchro_Kay_example (1).pdf#page=35", "Synchro_Kay_example (1).pdf#page=36"]
---

# Phase-locked loop (PLL) e inseguimento della fase

## Definizione · [[Synchro_Kay_example (1).pdf#page=29|p. 29]], [[Synchro_Kay_example (1).pdf#page=30|30]], [[Synchro_Kay_example (1).pdf#page=33|33]]

Il **phase tracking** aggiorna nel tempo la stima di fase massimizzando una funzione costo $J(\theta)$ proporzionale alla log-verosimiglianza, con un algoritmo iterativo. L'algoritmo **steepest ascent** (o **gradient descent**, se si minimizza) muove la stima nella direzione della derivata:

$$\hat\theta_{k+1}:=\hat\theta_k\pm\alpha\,\frac{\partial J}{\partial\theta}\Big|_{\theta=\hat\theta_k}$$

con $\alpha$ learning rate. Il **phase-locked loop** è la realizzazione analogica di questo aggiornamento per la fase della portante: moltiplicatore, **loop filter** (passa-basso che esegue l'integrale) e **VCO** (oscillatore la cui frequenza varia linearmente con la tensione di controllo), chiusi ad anello. Il **Costas loop** è la variante per segnali modulati in ampiezza.

## Formule · [[Synchro_Kay_example (1).pdf#page=31|p. 31]], [[Synchro_Kay_example (1).pdf#page=32|32]], [[Synchro_Kay_example (1).pdf#page=34|34]], [[Synchro_Kay_example (1).pdf#page=35|35]]

| Formula | Significato |
|---|---|
| $y_p(t)=\cos(2\pi f_ct+\theta(t))+n_p(t)$ | sinusoide rumorosa da agganciare |
| $J(\theta)=\int_{kT_0}^{(k+1)T_0}y_p(t)\cos(2\pi f_ct+\theta)\,dt$ | funzione costo (da (11), con $\lVert s_p\rVert^2\approx T_0/2$) |
| $\hat\theta_{k+1}:=\hat\theta_k-\alpha\int_{kT_0}^{(k+1)T_0}y_p(t)\sin(2\pi f_ct+\hat\theta_k)\,dt$ | aggiornamento (12) |
| $\frac{d\hat\theta}{dt}=\gamma\,c(t)$ | legge del VCO (13) |
| $\int y_p\sin(2\pi f_ct+\hat\theta_k)\,dt\approx\frac{T_0}2\sin(\hat\theta_k-\theta_{k+1})$ | termine d'errore senza rumore (15) |

> 🧮 Formula chiave: aggiornamento $\hat\theta_{k+1}=\hat\theta_k-\alpha\frac{T_0}{2}\sin(\hat\theta_k-\theta_{k+1})$.

Simboli: $T_0$ [s] durata dell'intervallo di osservazione; $f_c$ [Hz] portante; $\alpha$ passo (learning rate, in rad per unità d'integrale); $c(t)$ [V] tensione di controllo; $\gamma$ [rad/(s·V)] sensibilità del VCO; $\sigma^2$ PSD del rumore reale passa-banda.

## Derivazioni

### Derivazione — Energia del segnale ≈ T₀/2 · [[Synchro_Kay_example (1).pdf#page=32|p. 32]]
**Fonte:** la slide afferma $\lVert s_p\rVert^2\approx T_0/2$ sotto le due ipotesi.

> 🧩 Derivazione mia:

$$
\begin{aligned}
\lVert s_p\rVert^2&=\int_{kT_0}^{(k+1)T_0}\cos^2(2\pi f_ct+\theta)\,dt && \theta\text{ costante nell'intervallo (ipotesi 2)}\\
&=\int\frac{1+\cos(4\pi f_ct+2\theta)}2\,dt=\frac{T_0}2+\frac12\int\cos(4\pi f_ct+2\theta)\,dt && \cos^2x=\tfrac{1+\cos2x}2\\
\Big|\tfrac12\int\cos(4\pi f_ct+2\theta)\,dt\Big|&\le\frac{1}{4\pi f_c} && \text{primitiva } \tfrac{\sin(\cdot)}{4\pi f_c}\text{, seno limitato da 1}\\
\frac{1/(4\pi f_c)}{T_0/2}&=\frac{1}{2\pi f_cT_0}\ll1 && f_cT_0\gg1\ \text{(ipotesi 1)}
\end{aligned}
$$

Quindi l'energia non dipende da $\theta$ e nella (11) il termine $-\frac12\lVert s_p\rVert^2$ si può ignorare: resta $J(\theta)=\langle y_p,s_p\rangle$. Gli appunti di p. 32 lo dicono così: senza ipotesi l'energia dipenderebbe da $\theta(t)$, e se $\theta$ varia bruscamente non c'è garanzia che ne sia indipendente.

### Derivazione — Aggiornamento (12) · [[Synchro_Kay_example (1).pdf#page=30|p. 30]], [[Synchro_Kay_example (1).pdf#page=32|32]]

$$
\begin{aligned}
\frac{\partial J}{\partial\theta}&=\int_{kT_0}^{(k+1)T_0}y_p(t)\,\frac{\partial}{\partial\theta}\cos(2\pi f_ct+\theta)\,dt=-\int y_p(t)\sin(2\pi f_ct+\theta)\,dt && \text{derivo sotto l'integrale}\\
\hat\theta_{k+1}&:=\hat\theta_k+\alpha\,\frac{\partial J}{\partial\theta}\Big|_{\hat\theta_k}=\hat\theta_k-\alpha\int y_p(t)\sin(2\pi f_ct+\hat\theta_k)\,dt && \text{steepest ascent: è la (12)}
\end{aligned}
$$

### Derivazione — Termine d'errore (15) · [[Synchro_Kay_example (1).pdf#page=35|p. 35]]
**Si parte da:** (12) senza rumore, $y_p=\cos(2\pi f_ct+\theta(t))$; formula di Werner $\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$.

$$
\begin{aligned}
\int y_p\sin(2\pi f_ct+\hat\theta_k)\,dt&=\int\sin(2\pi f_ct+\hat\theta_k)\cos(2\pi f_ct+\theta(t))\,dt && a=2\pi f_ct+\hat\theta_k,\ b=2\pi f_ct+\theta(t)\\
&=\frac12\int\big[\sin(4\pi f_ct+\hat\theta_k+\theta(t))+\sin(\hat\theta_k-\theta(t))\big]dt && \text{Werner}\\
&\approx\frac12\int_{kT_0}^{(k+1)T_0}\sin(\hat\theta_k-\theta(t))\,dt && f_cT_0\gg1\text{: il termine a } 2f_c\text{ ha media nulla}\\
&\approx\frac{T_0}2\sin(\hat\theta_k-\theta_{k+1}) && \theta(t)\approx\theta_{k+1}\text{ nell'intervallo}
\end{aligned}
$$

**Sanity check:** se $\hat\theta_k=\theta_{k+1}$ l'integrale è nullo e la stima non cambia: è lo stato di aggancio (appunti di p. 35: se $\hat\theta=\theta$, agganciato).

> 🧩 Convergenza (mia): con $\theta$ costante e $e_k\triangleq\hat\theta_k-\theta$, la (12) diventa $e_{k+1}=e_k-\alpha\frac{T_0}2\sin e_k$. Per errori piccoli $\sin e_k\approx e_k$ e $e_{k+1}\approx(1-\alpha T_0/2)\,e_k$: l'errore si riduce geometricamente se $0<\alpha T_0/2<2$, e con $\alpha T_0/2=1$ si annulla in un passo (nel caso senza rumore). Un passo grande corregge in fretta ma, con il rumore, rende la stima più agitata: è il compromesso del learning rate.

![[grafico-l13-curva-s-pll.png]]
*🧩 Grafico mio. Il termine d'errore della (15) in funzione di $\hat\theta_k-\theta_{k+1}$: positivo quando la stima è troppo grande (la (12) la fa diminuire), negativo quando è troppo piccola, nullo all'aggancio. Vicino a 0 è quasi lineare: il modulo dice quanto la stima è lontana.*

### Derivazione — Il VCO realizza la (12) · [[Synchro_Kay_example (1).pdf#page=34|p. 34]]

$$
\begin{aligned}
\frac{d\hat\theta}{dt}&=\gamma\,c(t) && \text{(13), VCO}\\
\frac{\hat\theta(t)-\hat\theta(t-\Delta t)}{\Delta t}&\approx\gamma\,c(t)\ \Rightarrow\ \hat\theta(t)\approx\hat\theta(t-\Delta t)+\gamma\,\Delta t\,c(t) && \text{(14), variazioni piccole}
\end{aligned}
$$

Con $c(t)$ uguale all'uscita del loop filter, cioè (a meno del segno) all'integrale del prodotto $y_p\cdot\sin(\cdot)$, questa è la (12) con $\alpha$ proporzionale a $\gamma\Delta t$. Se $c(t)=0$ la fase non cambia: **stato di aggancio**.

### Derivazione — Inviluppo della sinusoide · [[Synchro_Kay_example (1).pdf#page=31|p. 31]]
$\sqrt2\,\text{Re}\{\frac{e^{j\theta}}{\sqrt2}e^{j2\pi f_ct}\}=\text{Re}\{e^{j(2\pi f_ct+\theta)}\}=\cos(2\pi f_ct+\theta)$: con la convenzione $\sqrt2\,\text{Re}\{\cdot\}$ della Lezione 4 l'inviluppo della sinusoide unitaria è $e^{j\theta}/\sqrt2$, come dice la slide.

## Spiegazione · [[Synchro_Kay_example (1).pdf#page=33|p. 33]], [[Synchro_Kay_example (1).pdf#page=36|36]]

- **Il PLL è uno stimatore ML iterativo** (appunti di p. 32): invece di calcolare $\arg\langle y,s\rangle$ su un blocco, corregge la stima un po' alla volta usando l'errore $\sin(\hat\theta-\theta)$.
- **Schema (p. 33).** Il segnale ricevuto è moltiplicato per $-\sin(2\pi f_ct+\hat\theta)$ prodotto dal VCO; il loop filter integra (media) il prodotto, togliendo il termine a $2f_c$; la sua uscita pilota il VCO, che cambia fase finché l'errore si annulla.
- **Costas loop (p. 36).** Il PLL non funziona bene se il segnale ha rapide variazioni d'ampiezza o di fase dovute alla modulazione. Per segnali modulati in ampiezza si usa il Costas loop: due rami, con $\cos[2\pi f_ct+\phi_v(t)]$ e $-\sin[2\pi f_ct+\phi_v(t)]$ (sfasatore $\pi/2$), due LPF che danno $e_1(t)$ ed $e_2(t)$, il loro prodotto $e(t)$ nel loop filter e la tensione $v(t)$ al VCO.

> 🧩 Perché il Costas loop funziona (spiegazione mia, le slide mostrano solo lo schema): con $r(t)=m(t)\cos(2\pi f_ct+\theta)$ e $\Delta\triangleq\theta-\phi_v$, i due rami danno $e_1=\frac12m(t)\cos\Delta$ ed $e_2=\frac12m(t)\sin\Delta$. Il prodotto è $e=\frac14m^2(t)\sin\Delta\cos\Delta=\frac18m^2(t)\sin2\Delta$: dipende da $m^2\ge0$, quindi il segno dei simboli (che nel PLL semplice invertirebbe l'errore) sparisce. Il prezzo è un'ambiguità di $\pi$: $\sin2\Delta$ si annulla anche per $\Delta=\pi$.

## Perché importa

Nei sistemi con tracking, la fase deriva nel tempo (mismatch e Doppler, [[sincronizzazione]]): una stima fatta una volta sola non basta. Il PLL e il Costas loop sono i blocchi che, nella pratica, tengono la costellazione ferma.

## Connessioni

- [[sincronizzazione]]: il PLL insegue la fase stimata in acquisizione.
- [[stima-dei-parametri]]: $J(\theta)$ è la log-verosimiglianza a meno di costanti.
- [[upconversion-e-downconversion]]: il prodotto per la portante locale e il passa-basso sono gli stessi della down-conversion.

## Fonti · [[Synchro_Kay_example (1).pdf#page=29|p. 29]]–[[Synchro_Kay_example (1).pdf#page=36|36]]

- [[parameter-estimation-synchronization]]

_Aggiornato: 2026-11-16 — creazione da ingest Synchro_Kay_example (1).pdf (Lezione 13)_
