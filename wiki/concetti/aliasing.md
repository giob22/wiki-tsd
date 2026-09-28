---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento"]
fonti_pdf: ["Campionamento_AD_DA.pdf#page=18", "Campionamento_AD_DA.pdf#page=20", "Campionamento_AD_DA.pdf#page=21"]
---

# Aliasing e filtraggio antialiasing

## Definizione

> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=18]]

L'**aliasing** si verifica quando $f_c$ non soddisfa la condizione del [[teorema-del-campionamento]] ($f_c<2f_m$): le repliche spettrali si **sovrappongono**. Una componente a frequenza $f_0>f_c/2$ viene "spostata" (*aliased*) e nel segnale ricostruito compare alla **frequenza alias** $f_c-f_0$.

## Formule

> 🧮 Formula chiave ([[Campionamento_AD_DA.pdf#page=18]]): $f_{alias} = f_c - f_0$ per $f_0 > f_c/2$

Validità (🧩 mia precisazione): la formula della slide vale per $f_c/2 < f_0 < f_c$. In generale la frequenza ricostruita è la replica $|f_0 - kf_c|$ che cade in $[0, f_c/2]$ (grafico in [[#Perché il segnale ricostruito è a 0.5 kHz]]).

**Filtro antialiasing** ([[Campionamento_AD_DA.pdf#page=21]]): LPF **analogico**, ideale con taglio $f_c/2$, messo **prima** del campionatore.

## Derivazioni

### Derivazione — Frequenza alias di una sinusoide
**Fonte:** [[Campionamento_AD_DA.pdf#page=18]] (esempio numerico con risultato)
> 🧩 Derivazione mia, nel dominio dei campioni
$$
\begin{aligned}
x_a(t) &= \cos(2\pi f_0 t) && \text{sinusoide a } f_0 \\
x(n) &= \cos\!\left(2\pi \tfrac{f_0}{f_c}n\right) && t = nT_c = n/f_c \\
&= \cos\!\left(2\pi n - 2\pi\tfrac{f_0}{f_c}n\right) && \cos \text{ periodica di } 2\pi,\ n \text{ intero} \\
&= \cos\!\left(2\pi\tfrac{f_c-f_0}{f_c}n\right) && \text{raccolgo; } \cos(-\theta)=\cos\theta
\end{aligned}
$$
I campioni coincidono quindi con quelli di una sinusoide a $f_c-f_0$. Se $f_0>f_c/2$ allora $f_c-f_0<f_c/2$, e il LPF di ricostruzione (taglio $f_c/2$) restituisce la sinusoide a **bassa** frequenza.

**Numeri** ([[Campionamento_AD_DA.pdf#page=18]]): $f_0 = 1.5$ kHz, $f_c = 2$ kHz:
$$f_{alias} = f_c - f_0 = 2\,\text{kHz} - 1.5\,\text{kHz} = 0.5\,\text{kHz}$$
Verifica sui campioni: $f_0/f_c = 0.75$, quindi $x(n) = \cos(1.5\pi n) = \cos(2\pi n - 0.5\pi n) = \cos(0.5\pi n)$, cioè $0.25\cdot f_c = 0.5$ kHz ✓.
**Sanity check:** $f_0 = 1.5$ kHz $> f_c/2 = 1$ kHz, quindi aliasing atteso; con $f_c\ge 3$ kHz non ci sarebbe aliasing.
**Ipotesi:** ricostruzione con LPF ideale di taglio $f_c/2$.

Perché il ricostruttore restituisce proprio questa frequenza, passo per passo e con due animazioni: [[#Perché il segnale ricostruito è a 0.5 kHz]].

### Derivazione — Perché un segnale di durata finita non è a banda limitata
**Fonte:** [[Campionamento_AD_DA.pdf#page=20]] (affermazione senza dimostrazione)
> 📚 Fonte esterna: proprietà standard della trasformata di Fourier (un segnale non nullo non può avere supporto limitato sia nel tempo sia in frequenza).

La slide dà l'esempio: un segnale a banda rigorosamente limitata ha necessariamente durata infinita (es. sinc, sinc²).

## Spiegazione

![[campionamento-p18-aliasing-sinusoide.png]]
*[[Campionamento_AD_DA.pdf#page=18]]. In alto, sull'asse delle frequenze: la frequenza originaria $f_0$ (a destra di $f_c/2$) viene "ribaltata" rispetto a $f_c/2$ sulla frequenza alias $f_c - f_0$. In basso: i campioni $x_a(nT_c)$ in funzione di $t/T_c$, e la sinusoide a 1.5 kHz (nera) insieme a quella a 0.5 kHz (rossa), che passano per gli **stessi campioni** $x(n)$.*

> 💡 Connessione: la figura mostra bene la "simmetria" dell'aliasing. $f_0$ e $f_c - f_0$ sono equidistanti da $f_c/2$: la frequenza $f_c/2$ fa da "specchio".

### Perché il segnale ricostruito è a 0.5 kHz
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=18]] (esempio), [[Campionamento_AD_DA.pdf#page=12]] (repliche dello spettro), [[Campionamento_AD_DA.pdf#page=14]] (teorema), [[Campionamento_AD_DA.pdf#page=15]] e [[Campionamento_AD_DA.pdf#page=17]] (ricostruzione con LPF ideale)

La slide dice che un coseno a 1.5 kHz, campionato a 2 kHz, viene ricostruito come un coseno a 0.5 kHz, e che i due hanno gli stessi campioni. Il ragionamento completo ha quattro passi.

**Passo 1 — Il ricostruttore vede solo i campioni.** Con $f_c = 2$ kHz si prende un campione ogni $T_c = 1/f_c = 0.5$ ms. Dopo il campionamento esiste solo la sequenza $x(n) = x_a(nT_c)$: quello che il segnale faceva *tra* due campioni è perso.

**Passo 2 — Quei campioni sono anche i campioni di un coseno a 0.5 kHz, e di molti altri.** L'argomento del coseno all'istante $nT_c$ è $2\pi f\,nT_c$; con $f$ in kHz e $T_c = 0.5$ ms il prodotto kHz·ms è adimensionale, quindi vale $2\pi\cdot1.5\cdot0.5\,n = 1.5\pi n$ per 1.5 kHz, $0.5\pi n$ per 0.5 kHz, $2.5\pi n$ per 2.5 kHz.

| $n$ | $t = nT_c$ | 1.5 kHz: $\cos(1.5\pi n)$ | 0.5 kHz: $\cos(0.5\pi n)$ | 2.5 kHz: $\cos(2.5\pi n)$ |
|---|---|---|---|---|
| 0 | 0 ms | 1 | 1 | 1 |
| 1 | 0.5 ms | 0 | 0 | 0 |
| 2 | 1.0 ms | −1 | −1 | −1 |
| 3 | 1.5 ms | 0 | 0 | 0 |
| 4 | 2.0 ms | 1 | 1 | 1 |

> 🧩 Derivazione mia: perché coincidono. Per ogni intero $k$, e ricordando che $f_cT_c = 1$:
> $$
> \begin{aligned}
> \cos\big(2\pi(f_0 + kf_c)nT_c\big) &= \cos(2\pi f_0nT_c + 2\pi kn) = \cos(2\pi f_0nT_c) && kn \text{ intero: } 2\pi kn \text{ è un numero intero di giri} \\
> \cos\big(2\pi(kf_c - f_0)nT_c\big) &= \cos(2\pi kn - 2\pi f_0nT_c) = \cos(2\pi f_0nT_c) && \text{idem, più } \cos(-\theta) = \cos\theta
> \end{aligned}
> $$
> Tutte le frequenze $|f_0 + kf_c|$ e $|kf_c - f_0|$ danno quindi gli stessi campioni. Con $f_0 = 1.5$ kHz e $f_c = 2$ kHz sono $1.5$, $0.5 = 2 - 1.5$, $2.5 = 4 - 1.5$, $3.5 = 1.5 + 2$, … kHz, cioè tutti i multipli dispari di 0.5 kHz. Dai soli campioni **non si può capire** quale di questi coseni c'era all'ingresso.

**Passo 3 — Il ricostruttore sceglie la frequenza sotto $f_c/2$.** La ricostruzione ideale usa il LPF $H_r(f) = T_c\,\Pi\!\big(f/2f_r\big)$ con, di solito, $f_r = f_c/2$ ([[Campionamento_AD_DA.pdf#page=15]]); è la serie di Shannon con le sinc ([[Campionamento_AD_DA.pdf#page=17]]). Il filtro lascia passare solo le frequenze con $|f| < f_c/2 = 1$ kHz. Tra i candidati del passo 2 l'unico sotto 1 kHz è **0.5 kHz**, quindi l'uscita è il coseno a 0.5 kHz.

> 🧩 Detto in un altro modo: il ricostruttore applica il teorema del campionamento *come se* la sua ipotesi fosse vera ([[Campionamento_AD_DA.pdf#page=14]]). Restituisce cioè l'unico segnale con banda sotto $f_c/2$ che ha quei campioni, e quel segnale esiste: è il coseno a 0.5 kHz. Il coseno a 1.5 kHz non si può recuperare perché l'ipotesi del teorema è violata: $f_c = 2$ kHz $< 2f_0 = 3$ kHz.

**Passo 4 — La stessa cosa vista in frequenza** ([[Campionamento_AD_DA.pdf#page=12]], [[Campionamento_AD_DA.pdf#page=15]]).
> 🧩 Derivazione mia
$$
\begin{aligned}
X_a(f) &= \tfrac12\big[\delta(f - f_0) + \delta(f + f_0)\big] && \text{spettro del coseno: due righe a } \pm1.5 \text{ kHz} \\
X(f) &= \frac{1}{T_c}\sum_{k=-\infty}^{+\infty}X_a(f - kf_c) && \text{campionamento: repliche con passo } f_c \text{ (p.12)} \\
&\to \text{righe a } \pm0.5,\ \pm1.5,\ \pm2.5,\ \dots \text{ kHz, ognuna di peso } \tfrac{1}{2T_c} && \text{le righe } \pm1.5 \text{ spostate di } kf_c = 2k \text{ kHz} \\
-1.5 + 2 &= +0.5,\qquad +1.5 - 2 = -0.5 && \text{le due repliche che cadono in } (-1, 1) \text{ kHz} \\
X_r(f) &= H_r(f)\,X(f) = \tfrac12\big[\delta(f - 0.5) + \delta(f + 0.5)\big] && H_r = T_c \text{ per } |f| < 1 \text{ kHz, } 0 \text{ fuori} \\
x_r(t) &= \cos(2\pi\cdot0.5\,\text{kHz}\cdot t) && \text{antitrasformata: coseno di ampiezza 1}
\end{aligned}
$$
La riga a $+0.5$ kHz che sopravvive è la replica della riga **negativa** $-1.5$ kHz spostata di $+f_c$: ecco da dove viene $f_c - f_0$. L'ampiezza torna quella originale perché il guadagno $T_c$ del filtro compensa il fattore $1/T_c$ delle repliche ([[Campionamento_AD_DA.pdf#page=15]]).

![[grafico-aliasing-animazione.gif]]
*🧩 Animazione mia (formule di [[Campionamento_AD_DA.pdf#page=12]], [[Campionamento_AD_DA.pdf#page=15]], [[Campionamento_AD_DA.pdf#page=18]]; script in `output/grafici/`). In alto il tempo, in basso lo spettro a righe, nei sei passi appena descritti. (1) Coseno a 1.5 kHz, righe a ±1.5 kHz. (2) Un campione ogni 0.5 ms; nello spettro compaiono le repliche ogni 2 kHz, e le frecce mostrano le due che finiscono a ±0.5 kHz. (3) Il coseno originale sfuma: restano solo i campioni. (4) Per gli stessi campioni passano i coseni a 0.5 kHz (rosso) e a 2.5 kHz (grigio). (5) Il LPF di ricostruzione (riquadro blu, $|f| < f_c/2$) tiene solo le righe a ±0.5 kHz. (6) Uscita: coseno a 0.5 kHz.*

**Intuizione — l'effetto stroboscopio.**
> 🧩 Spiegazione mia. Il coseno è la parte reale di un fasore, un vettore che ruota: $\cos(2\pi f_0t) = \text{Re}\{e^{j2\pi f_0t}\}$.
> - In un intervallo di campionamento il fasore ruota di $2\pi f_0T_c = 2\pi\cdot0.75$ rad, cioè di **270°**, tre quarti di giro in senso antiorario.
> - Ruotare di 270° in avanti porta nella stessa posizione in cui si arriva ruotando di **90° all'indietro**.
> - Visto solo agli istanti di campionamento, come sotto una luce stroboscopica, il fasore sembra quindi girare all'indietro di un quarto di giro per campione: 0.25 giri ogni 0.5 ms, cioè **0.5 kHz**.
> - Il coseno non distingue il verso di rotazione, perché $\cos(-\theta) = \cos\theta$: un fasore a 0.5 kHz che gira all'indietro dà proprio un coseno a 0.5 kHz.
>
> È lo stesso effetto delle ruote delle auto che nei film sembrano girare lentamente all'indietro: la cinepresa "campiona" la ruota.

![[grafico-aliasing-stroboscopio.gif]]
*🧩 Animazione mia. A sinistra il fasore a 1.5 kHz (nero, antiorario) e quello a 0.5 kHz (rosso, orario); i punti neri sono le posizioni negli istanti di campionamento, numerati con $n$. Tra un campione e l'altro i due fasori sono in posizioni diverse. Negli istanti $nT_c$ coincidono: il nero ha fatto $270°\cdot n$, il rosso $-90°\cdot n$, e i due angoli differiscono di $360°\cdot n$, cioè di un numero intero di giri. A destra i due coseni (proiezioni sull'asse orizzontale): diversi tra i campioni, uguali nei campioni.*

**Regola generale.**
> 🧩 Mia: la frequenza ricostruita è la replica $|f_0 - kf_c|$ che cade in $[0, f_c/2]$, con $k$ = intero più vicino a $f_0/f_c$. Per $f_c/2 < f_0 < f_c$ si ha $k = 1$ e si ritrova la formula della slide, $f_c - f_0$ ([[Campionamento_AD_DA.pdf#page=18]]).

![[grafico-aliasing-ripiegamento.png]]
*🧩 Grafico mio: frequenza ricostruita in funzione di $f_0$ con $f_c = 2$ kHz. Fino a $f_c/2 = 1$ kHz (zona grigia) la ricostruzione è corretta. Oltre, la frequenza si "ripiega" come in uno specchio posto a $f_c/2$: sale e scende a zig-zag tra 0 e 1 kHz. Il punto rosso è l'esempio della slide (1.5 kHz → 0.5 kHz); anche 2.5, 3.5 e 4.5 kHz finiscono a 0.5 kHz, in accordo con il passo 2.*

> 🧩 Nota sul seno: con $\sin$ al posto di $\cos$ i campioni coincidono a meno del segno, $\sin(1.5\pi n) = \sin(2\pi n - 0.5\pi n) = -\sin(0.5\pi n)$. L'uscita è quindi $-\sin(2\pi\cdot0.5\,\text{kHz}\cdot t)$: stessa frequenza, 0.5 kHz, ma fase invertita. È la "rotazione all'indietro" dello stroboscopio, che per il coseno non si vede perché il coseno è pari.

> 🎯 Esame: saper spiegare perché la ricostruzione dà $f_c - f_0$, e non $f_0$. I campioni sono ambigui, e il filtro di ricostruzione sceglie l'unica replica con $|f| < f_c/2$.

### Le due ipotesi ideali del teorema
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=19]]

Lo studio del campionamento riassunto dal teorema di Shannon si basa su **due ipotesi ideali**:
1. il segnale è a **banda rigorosamente limitata** → cosa succede quando cade: questa pagina;
2. l'**interpolazione è ideale**, con funzioni sinc → cosa succede quando cade: [[interpolazione]].

Le slide approfondiscono separatamente i due aspetti.

### Segnali a banda praticamente limitata
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=20]]

In pratica si campionano segnali di **durata finita**, che quindi **non** possono avere banda rigorosamente limitata. Sono al più a banda **praticamente** limitata: qualunque sia $f_c$, le repliche di $X_a(f)$ si sovrappongono un po', e c'è sempre un po' di aliasing nella ricostruzione.

![[campionamento-p20-banda-praticamente-limitata.png]]
*[[Campionamento_AD_DA.pdf#page=20]]: (a) spettro $X_a(f)$ di altezza 1 che non si annulla mai del tutto (code oltre $\pm f_c/2$); (b) $X_\delta(f)$: le repliche di altezza $1/T_c$ si sovrappongono e la loro somma (rosso) differisce da ogni singola replica; (c) filtro di ricostruzione $H_r(f)$ di altezza $T_c$ su $[-f_c/2, f_c/2]$; (d) confronto fra $X_r(f)$ e $X_a(f)$: il segnale ricostruito è diverso da quello originale, per effetto dell'aliasing.*

### Come ridurre l'aliasing
> 📄 Fonte: [[Campionamento_AD_DA.pdf#page=21]]

| Strategia | Pro | Contro |
|---|---|---|
| **Sovracampionamento** | repliche più distanti, meno sovrapposizione | costo e memoria (più campioni/s) |
| **Filtraggio antialiasing** (LPF prima del campionatore, taglio $f_c/2$) | più efficiente: elimina a monte l'energia oltre $f_c/2$ | è un filtro **analogico**, anch'esso non ideale in pratica |

![[campionamento-p21-antialiasing.png]]
*[[Campionamento_AD_DA.pdf#page=21]]: (a) $X_\delta(f)$ con $f_{c1}$: repliche di altezza $1/T_c$ fortemente sovrapposte intorno a $f_{c1}/2$; (b) con $f_{c2} = 2f_{c1}$ (sovracampionamento ×2) le repliche sono più distanti e la sovrapposizione intorno a $f_{c2}/2$ è molto minore; in basso, lo schema $x_a(t)$ → $H_{aa}(f)$ (filtro antialiasing) → $y_a(t)$ → campionatore ($T_c$) → $y(n)$.*

Dettagli della slide sul filtro antialiasing ([[Campionamento_AD_DA.pdf#page=21]]):
- LPF **ideale** con frequenza di taglio $f_c/2$;
- filtro **analogico**, perché agisce prima del campionamento;
- in pratica anche questo filtro sarà **non ideale**.

> 🎯 Esame: dove va il filtro antialiasing (prima del campionatore, in analogico) e perché (il segnale reale non è a banda limitata). Da non confondere con il filtro di ricostruzione (dopo, in D/A).

> 💡 Connessione: l'antialiasing *toglie* informazione oltre $f_c/2$ ma evita che quella energia si "ripieghi" sulle frequenze utili. Si perde la parte alta dello spettro invece di corrompere la parte bassa.

## Perché importa

L'aliasing è una distorsione **irreversibile**: dopo il campionamento la componente alias è indistinguibile da una componente vera a $f_c-f_0$. È per questo che ogni catena A/D reale ha un filtro antialiasing.

## Connessioni

- [[teorema-del-campionamento]] — le ipotesi la cui violazione causa aliasing.
- [[interpolazione]] — l'altra ipotesi ideale: l'interpolazione con sinc.
- [[campionamento-e-aliasing]] — esercizi.

## Fonti

- [[campionamento-conversione-ad-da]]
- [[Campionamento_AD_DA.pdf#page=18]] – [[Campionamento_AD_DA.pdf#page=21]]

_Aggiornato: 2026-09-24 — ragionamento esplicito sul perché si ricostruisce 0.5 kHz (campioni ambigui, scelta del LPF, repliche, stroboscopio), due animazioni e grafico del ripiegamento; 2026-09-23 — creazione da ingest Campionamento_AD_DA.pdf; revisione di copertura totale vs PDF (testo + figure)_
