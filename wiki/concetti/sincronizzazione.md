---
tipo: concetto
importanza_esame: alta
prerequisiti: ["inviluppo-complesso", "upconversion-e-downconversion", "stima-dei-parametri", "ricevitore-ottimo-awgn"]
fonti_pdf: ["11-9.pdf#page=2", "Synchro_Kay_example (1).pdf#page=2", "Synchro_Kay_example (1).pdf#page=3", "Synchro_Kay_example (1).pdf#page=5", "Synchro_Kay_example (1).pdf#page=9", "Synchro_Kay_example (1).pdf#page=10", "Synchro_Kay_example (1).pdf#page=11", "Synchro_Kay_example (1).pdf#page=25", "Synchro_Kay_example (1).pdf#page=28"]
---

# Sincronizzazione

## Definizione · Synchro [[Synchro_Kay_example (1).pdf#page=10|p. 10]], [[Synchro_Kay_example (1).pdf#page=11|11]]

La **sincronizzazione** è l'insieme delle stime che il ricevitore fa per compensare ritardo, fase e offset di frequenza introdotti dal canale e dal disaccordo tra gli oscillatori:

- **sincronizzazione di tempo** (timing): stima del ritardo $\tau$;
- **sincronizzazione di portante**: stima dell'offset di frequenza $\Delta f$ e della fase $\theta$.

Avviene in due fasi: **acquisizione** (stima iniziale, di solito con simboli di training in un preambolo) e **inseguimento** o tracking (aggiornamento continuo contro il drift). Durante il tracking l'algoritmo è **decision-directed** (usa le decisioni del demodulatore) oppure **blind** (insensibile ai simboli trasmessi, usa solo la loro statistica). Nei sistemi a pacchetto il tracking spesso non serve.

## Formule · 11-9 [[11-9.pdf#page=2|p. 2]] · Synchro [[Synchro_Kay_example (1).pdf#page=3|p. 3]], [[Synchro_Kay_example (1).pdf#page=9|9]], [[Synchro_Kay_example (1).pdf#page=25|25]]–[[Synchro_Kay_example (1).pdf#page=28|28]]

| Formula | Significato |
|---|---|
| $y_p(t)=A\,u_p(t-\tau)+n_p(t)$ | canale non dispersivo: scala e ritarda |
| $\theta=-2\pi f_c\tau\bmod2\pi$ | fase prodotta dal ritardo sulla portante |
| $y(t)=Ae^{j(2\pi\Delta ft+\theta)}u(t-\tau)+n(t)$ | inviluppo complesso ricevuto con LO a $f_c-\Delta f$ (1) |
| $\Delta f_{Doppler}=vf_c/c$ | spostamento Doppler |
| $\hat\theta=\arg\langle y(t),s(t)\rangle=\tan^{-1}(Z_s/Z_c)$ | stima ML della fase |

> 🧮 Formula chiave: $y(t)=Ae^{j(2\pi\Delta ft+\theta)}u(t-\tau)+n(t)$ e $\hat\theta_{ML}=\arg\langle y,s\rangle$.

Simboli: $A$ ampiezza (adimensionale, guadagno del canale); $\tau$ ritardo [s]; $f_c$ portante [Hz]; $\Delta f$ offset di frequenza [Hz]; $\theta$ fase [rad]; $u(t)=\sum_nb(n)g_{TX}(t-nT)$ inviluppo trasmesso; $n(t)$ WGN complesso; $v$ velocità relativa [m/s]; $c=3\cdot10^8$ m/s; $Z=Z_c+jZ_s=\langle y,s\rangle$.

## Derivazioni

### Derivazione — La fase prodotta dal ritardo · Synchro [[Synchro_Kay_example (1).pdf#page=3|p. 3]], [[Synchro_Kay_example (1).pdf#page=4|4]]
**Si parte da:** $u_p(t)=\sqrt2\,\text{Re}\{u(t)e^{j2\pi f_ct}\}$ ([[inviluppo-complesso]]).

$$
\begin{aligned}
u_p(t-\tau)&=\sqrt2\,\text{Re}\{u(t-\tau)\,e^{j2\pi f_c(t-\tau)}\} && \text{sostituisco } t\to t-\tau\text{ ovunque}\\
&=\sqrt2\,\text{Re}\{u(t-\tau)\,e^{-j2\pi f_c\tau}\,e^{j2\pi f_ct}\} && \text{separo l'esponenziale}\\
&=\sqrt2\,\text{Re}\{[u(t-\tau)\,e^{j\theta}]\,e^{j2\pi f_ct}\},\quad\theta=-2\pi f_c\tau && \text{il ritardo entra due volte}
\end{aligned}
$$

L'inviluppo complesso del segnale ritardato è $u(t-\tau)e^{j\theta}$: il ritardo trasla l'inviluppo **e** lo ruota di $\theta$ (gli appunti di p. 4 lo sottolineano).

> 🧩 Numeri miei (sensibilità): con $f_c=2.4$ GHz la fase compie un giro completo ($2\pi$) quando $\tau$ cambia di $1/f_c\approx0.42$ ns. Un errore di 0.1 ns, irrilevante per il timing di simboli lunghi 1 µs, sposta la fase di $2\pi\cdot2.4\cdot10^9\cdot10^{-10}\approx1.5$ rad $\approx86°$. Per questo $\theta$ si stima a parte (sincronizzazione di portante) e non si ricava dalla stima di $\tau$.

### Derivazione — Down-conversion con LO disaccordato · Synchro [[Synchro_Kay_example (1).pdf#page=5|p. 5]]–[[Synchro_Kay_example (1).pdf#page=9|9]]
**Fonte:** le slide scrivono i risultati dopo «product-to-sum identities».
**Si parte da:** $y_p=\sqrt2[v_I\cos\omega_ct-v_Q\sin\omega_ct]$ (rumore trascurato), $\omega_{LO}=\omega_c-2\pi\Delta f$, $\varphi=(\omega_c-\omega_{LO})t$ ([[upconversion-e-downconversion]]).

Ramo in fase, con $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$ e $\sin a\cos b=\frac12[\sin(a-b)+\sin(a+b)]$, $a=\omega_ct$, $b=\omega_{LO}t$:

$$
\begin{aligned}
I_{mix,s}&=\sqrt2\,y_p\cos\omega_{LO}t=2v_I\cos a\cos b-2v_Q\sin a\cos b && \text{definizione}\\
&=v_I[\cos\varphi+\cos(a+b)]-v_Q[\sin\varphi+\sin(a+b)] && \text{prostaferesi}\\
y_I&=v_I\cos\varphi-v_Q\sin\varphi && \text{LPF: via i termini a } \omega_c+\omega_{LO}
\end{aligned}
$$

Ramo in quadratura, con $\cos a\sin b=\frac12[\sin(a+b)-\sin(a-b)]$ e $\sin a\sin b=\frac12[\cos(a-b)-\cos(a+b)]$:

$$
\begin{aligned}
Q_{mix,s}&=-\sqrt2\,y_p\sin\omega_{LO}t=-2v_I\cos a\sin b+2v_Q\sin a\sin b && \text{definizione}\\
&=v_I[\sin\varphi-\sin(a+b)]+v_Q[\cos\varphi-\cos(a+b)] && \text{prostaferesi}\\
y_Q&=v_I\sin\varphi+v_Q\cos\varphi && \text{LPF}
\end{aligned}
$$

Ricombinazione:

$$
\begin{aligned}
y_I+jy_Q&=v_I(\cos\varphi+j\sin\varphi)+jv_Q(\cos\varphi+j\sin\varphi) && \text{raccolgo } v_I \text{ e } v_Q\ (j\cdot j=-1)\\
&=(v_I+jv_Q)\,e^{j\varphi}=A\,u(t-\tau)\,e^{j\theta}\,e^{j2\pi\Delta ft} && v=Au(t-\tau)e^{j\theta}
\end{aligned}
$$

**Sanity check:** con $\Delta f=0$ si ha $\varphi=0$, $y_I=v_I$, $y_Q=v_Q$: la down-conversion ideale della Lezione 4.
**Ipotesi:** il passa-basso elimina i termini a $\omega_c+\omega_{LO}\approx2\omega_c$ e lascia passare $v$ (banda di $v$ molto minore di $f_c$; $\Delta f$ piccolo rispetto alla banda del filtro).

Il termine $e^{j2\pi\Delta ft}$ è una **rotazione che cresce nel tempo**: la costellazione ricevuta gira con velocità angolare $2\pi\Delta f$ (appunti di 11-9: l'effetto della non sincronizzazione dipende dal tempo). In componenti, $y_I$ mescola $v_I$ e $v_Q$: non si riesce più a separare I e Q.

### Derivazione — Ordini di grandezza di mismatch e Doppler · Synchro [[Synchro_Kay_example (1).pdf#page=25|p. 25]], [[Synchro_Kay_example (1).pdf#page=26|26]]
**Fonte:** la slide dà 10–100 ppm per il mismatch e 0.2 ppm per il Doppler a 200 km/h.

$$
\begin{aligned}
\frac{\Delta f_D}{f_c}&=\frac vc=\frac{200/3.6\ \text{m/s}}{3\cdot10^8\ \text{m/s}} && \text{km/h}\to\text{m/s: divido per 3.6}\\
&=\frac{55.6}{3\cdot10^8}\approx1.85\cdot10^{-7}\approx0.2\ \text{ppm} && 1\ \text{ppm}=10^{-6}
\end{aligned}
$$

> 🧩 Numeri miei: con $f_c=2$ GHz il Doppler a 200 km/h vale circa 370 Hz, mentre il mismatch degli LO vale 20 kHz (10 ppm) – 200 kHz (100 ppm): domina il mismatch. Con $\Delta f=20$ kHz e $R_s=10$ Msimboli/s ($T=0.1$ µs) la rotazione per simbolo è $2\pi\Delta fT=2\pi\cdot2\cdot10^4\cdot10^{-7}\approx0.013$ rad $\approx0.7°$: trascurabile sul singolo simbolo (ipotesi della slide 23), ma dopo 100 simboli sono già circa 70°. Per questo la fase si tratta come costante su un blocco di simboli e poi si **insegue** ([[phase-locked-loop]]).

### Derivazione — Stima ML della fase · Synchro [[Synchro_Kay_example (1).pdf#page=26|p. 26]]–[[Synchro_Kay_example (1).pdf#page=28|28]]
**Si parte da:** la verosimiglianza (8) con $s_k\to s\,e^{j\theta}$ ([[stima-dei-parametri]]).

$$
\begin{aligned}
\lVert s\,e^{j\theta}\rVert^2&=\int|s(t)|^2|e^{j\theta}|^2dt=\lVert s\rVert^2 && |e^{j\theta}|=1\text{: non dipende da } \theta\\
\langle y,s\,e^{j\theta}\rangle&=\int y(t)\,[s(t)e^{j\theta}]^\ast dt=e^{-j\theta}\langle y,s\rangle && \text{il coniugato porta fuori } e^{-j\theta}\\
\text{Re}\{e^{-j\theta}|Z|e^{j\phi}\}&=|Z|\cos(\phi-\theta) && \langle y,s\rangle=|Z|e^{j\phi}\\
\hat\theta&=\arg\max_\theta|Z|\cos(\phi-\theta)=\phi && \cos\text{ massimo per argomento nullo (mod } 2\pi)
\end{aligned}
$$

Quindi $\hat\theta=\arg\langle y,s\rangle=\tan^{-1}(Z_s/Z_c)$ (con l'arcotangente a quattro quadranti, che usa i segni di $Z_c$ e $Z_s$).

Per lo schema: con $y=y_c+jy_s$ e $s=s_c+js_s$,

$$
\langle y,s\rangle=\int(y_c+jy_s)(s_c-js_s)\,dt=\underbrace{\langle y_c,s_c\rangle+\langle y_s,s_s\rangle}_{Z_c}+j\,\underbrace{\big(\langle y_s,s_c\rangle-\langle y_c,s_s\rangle\big)}_{Z_s}
$$

ognuno dei quattro prodotti scalari è un filtro adattato ($s_c(-t)$ o $s_s(-t)$) campionato in $t=0$, come nella figura di p. 28.

**Sanity check:** senza rumore $y=e^{j\theta}s$ e $\langle y,s\rangle=e^{j\theta}\lVert s\rVert^2$, il cui argomento è proprio $\theta$.
**Ipotesi:** timing e ampiezza già stimati; fase costante sull'intervallo d'osservazione; segnale $s(t)$ noto (training) o già deciso.

## Spiegazione · 11-9 [[11-9.pdf#page=2|p. 2]] · Synchro [[Synchro_Kay_example (1).pdf#page=7|p. 7]], [[Synchro_Kay_example (1).pdf#page=28|28]]

- **Più inviluppi per lo stesso segnale.** L'inviluppo complesso dipende dalla frequenza di riferimento: rispetto a $f_c$ è $v(t)$, rispetto a $f_c-\Delta f$ è $v(t)e^{j2\pi\Delta ft}$. Il ricevitore vede il secondo, e deve «riportarlo» al primo.
- **Effetti sulla costellazione.** $A$ scala la costellazione, $\theta$ la ruota di un angolo fisso, $\Delta f$ la fa ruotare in continuazione, $\tau$ sposta l'istante di campionamento ottimo. Gli appunti di p. 28 annotano che l'errore dovuto alla rotazione della costellazione non dipende dall'errore additivo: è un errore sistematico che non sparisce aumentando l'SNR, e va corretto stimando la fase.
- **Chi stima cosa.** Anche se $\theta$ nasce dal ritardo, lo compensa il blocco di sincronizzazione di portante (appunti di p. 10).

## Perché importa

Tutte le prestazioni ricavate nelle Lezioni 9–11 ([[probabilita-errore-m-aria]]) valgono con sincronizzazione perfetta. Una rotazione residua di fase avvicina i punti della costellazione ai confini delle regioni di decisione e fa crescere la probabilità d'errore; un $\Delta f$ non compensato, dopo pochi simboli, rende le decisioni inutilizzabili.

## Connessioni

- [[inviluppo-complesso]], [[upconversion-e-downconversion]]: il modello (1) è una down-conversion con LO sbagliato.
- [[stima-dei-parametri]]: la stima di fase è una MLE.
- [[phase-locked-loop]]: inseguimento della fase nel tempo.
- [[ricevitore-ottimo-awgn]]: lo stimatore di fase usa gli stessi correlatori del ricevitore ottimo.
- [[criterio-di-nyquist]]: le code corte del coseno rialzato aiutano a estrarre il timing.

## Fonti · 11-9 [[11-9.pdf#page=2|p. 2]] · Synchro [[Synchro_Kay_example (1).pdf#page=2|p. 2]]–[[Synchro_Kay_example (1).pdf#page=11|11]], [[Synchro_Kay_example (1).pdf#page=25|25]]–[[Synchro_Kay_example (1).pdf#page=28|28]]

- [[parameter-estimation-synchronization]]

_Aggiornato: 2026-11-16 — creazione da ingest di 11-9.pdf e Synchro_Kay_example (1).pdf (Lezione 13)_
