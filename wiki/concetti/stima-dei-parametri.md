---
tipo: concetto
importanza_esame: alta
prerequisiti: ["variabile-aleatoria-gaussiana", "probabilita-totale-e-bayes", "rivelazione-map-ml", "media-e-varianza"]
fonti_pdf: ["Synchro_Kay_example (1).pdf#page=12", "Synchro_Kay_example (1).pdf#page=13", "Synchro_Kay_example (1).pdf#page=14", "Synchro_Kay_example (1).pdf#page=15", "Synchro_Kay_example (1).pdf#page=16", "Synchro_Kay_example (1).pdf#page=17", "Synchro_Kay_example (1).pdf#page=18", "Synchro_Kay_example (1).pdf#page=19", "Synchro_Kay_example (1).pdf#page=20", "Synchro_Kay_example (1).pdf#page=21", "Synchro_Kay_example (1).pdf#page=22", "Synchro_Kay_example (1).pdf#page=23", "Synchro_Kay_example (1).pdf#page=24"]
---

# Stima dei parametri

## Definizione · [[Synchro_Kay_example (1).pdf#page=12|p. 12]], [[Synchro_Kay_example (1).pdf#page=13|13]], [[Synchro_Kay_example (1).pdf#page=15|15]], [[Synchro_Kay_example (1).pdf#page=16|16]]

Dato un insieme di $K$ dati $\mathbf y=[y(0),\dots,y(K-1)]$ che dipende da un parametro incognito $\theta$, uno **stimatore** è una funzione dei dati $\hat\theta=g(\mathbf y)$. I dati si descrivono con una **famiglia di pdf** $f(\mathbf y;\theta)$, una per ogni valore del parametro.

- **Approccio classico**: $\theta$ è deterministico ma incognito; non si può usare informazione a priori.
- **Approccio bayesiano**: $\theta$ è una variabile aleatoria con pdf $f(\theta)$; dati e parametro hanno la pdf congiunta $f(\mathbf y,\theta)=f(\mathbf y\mid\theta)f(\theta)$.
- **Stima a massima verosimiglianza** (MLE), nel quadro classico: $\hat\theta=\arg\max_\theta f(\mathbf y;\theta)=\arg\max_\theta\log f(\mathbf y;\theta)$. La pdf vista come funzione di $\theta$ a dati fissati è la **funzione di verosimiglianza** $\Lambda_\theta(\mathbf y)$.

## Formule · [[Synchro_Kay_example (1).pdf#page=14|p. 14]], [[Synchro_Kay_example (1).pdf#page=19|19]]–[[Synchro_Kay_example (1).pdf#page=22|22]], [[Synchro_Kay_example (1).pdf#page=24|24]]

| Formula | Significato |
|---|---|
| $\hat A=\frac1K\sum_ky(k)$, $E[\hat A]=A$, $\text{Var}(\hat A)=\sigma^2/K$ | livello continuo nel rumore: media campionaria |
| $\hat A=\arg\max_A\sum_k\log f(y(k);A)$ | MLE con campioni indipendenti (3) |
| $\hat A=\frac1K\sum_ky(k)\,b(k)$ | stima d'ampiezza training-based |
| $f(y;A)=\frac12\mathcal N(y;-A,\sigma^2)+\frac12\mathcal N(y;A,\sigma^2)$ | verosimiglianza blind, miscela (6)–(7) |
| $\hat A=\frac1K\sum_ky(k)\tanh\big(\hat Ay(k)/\sigma^2\big)$ | stima d'ampiezza blind (equazione trascendente) |
| $\hat H_k=\arg\max_k\Lambda_k(y)$ | la rivelazione ML è la MLE di un parametro a $M$ valori (9) |

> 🧮 Formula chiave: training-based $\hat A=\frac1K\sum y(k)b(k)$; blind $\hat A=\frac1K\sum y(k)\tanh(\hat Ay(k)/\sigma^2)$.

Simboli: $y(k)$ campioni all'uscita di filtro adattato e campionatore (stessa unità del segnale, ad esempio V); $A$ ampiezza incognita; $b(k)\in\{\pm1\}$ simboli antipodali; $n(k)\sim\mathcal N(0,\sigma^2)$ rumore, con $\sigma^2$ in V²; $K$ numero di campioni.

## Derivazioni

### Derivazione — Media e varianza della media campionaria · [[Synchro_Kay_example (1).pdf#page=14|p. 14]]
**Fonte:** la slide dà $E[\hat A]=A$ e $\text{Var}(\hat A)=\sigma^2/K$ senza passaggi.
**Si parte da:** $y(k)=A+n(k)$, $n(k)$ i.i.d. $\mathcal N(0,\sigma^2)$ ([[media-e-varianza]]).

> 🧩 Derivazione mia:

$$
\begin{aligned}
E[\hat A]&=\frac1K\sum_{k=0}^{K-1}E[A+n(k)]=\frac1K\cdot KA=A && \text{linearità, } E[n(k)]=0\\
\text{Var}(\hat A)&=\text{Var}\Big(\frac1K\sum_kn(k)\Big)=\frac1{K^2}\sum_k\text{Var}(n(k))=\frac{K\sigma^2}{K^2}=\frac{\sigma^2}{K} && A\text{ costante; } n(k)\text{ indipendenti}
\end{aligned}
$$

**Sanity check:** con $K=1$ si ritrova la varianza del singolo campione; per $K\to\infty$ la varianza va a zero (consistenza).
**Ipotesi:** rumore a media nulla (altrimenti lo stimatore è polarizzato) e campioni indipendenti (altrimenti compaiono le covarianze e la varianza non scende come $1/K$).

La media campionaria è anche la MLE di $A$: massimizzare $\sum_k\log\mathcal N(y(k);A,\sigma^2)$ equivale a minimizzare $\sum_k(y(k)-A)^2$, la cui derivata $-2\sum_k(y(k)-A)$ si annulla per $A=\frac1K\sum_ky(k)$ (🧩 osservazione mia, la slide non lo dice).

### Derivazione — Stima training-based · [[Synchro_Kay_example (1).pdf#page=20|p. 20]]
**Fonte:** la slide dà il risultato «derivando rispetto ad $A$».
**Si parte da:** (3) con $f(y(k);A)=\mathcal N(y(k);Ab(k),\sigma^2)$.

$$
\begin{aligned}
\sum_k\log f(y(k);A)&=-\frac K2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_k\big(y(k)-Ab(k)\big)^2 && \text{log della gaussiana}\\
\arg\max_A(\cdot)&=\arg\min_A\sum_k\big(y(k)-Ab(k)\big)^2 && \text{il primo termine non dipende da } A\\
\frac{\partial}{\partial A}\sum_k(y(k)-Ab(k))^2&=-2\sum_kb(k)\big(y(k)-Ab(k)\big)=0 && \text{derivata nulla}\\
\sum_kb(k)y(k)&=A\sum_kb^2(k)=AK && b^2(k)=1\\
\hat A&=\frac1K\sum_ky(k)\,b(k)
\end{aligned}
$$

**Sanity check:** senza rumore $y(k)b(k)=Ab^2(k)=A$ per ogni $k$, e la media dà esattamente $A$.
**Ipotesi:** simboli noti e antipodali ($b^2=1$); rumore gaussiano bianco (campioni indipendenti). Per simboli complessi qualunque (🧩) lo stesso conto con $|y-Ab|^2$ dà $\hat A=\text{Re}\big\{\sum_kb^\ast(k)y(k)\big\}/\sum_k|b(k)|^2$ per $A$ reale.

### Derivazione — Stima blind e funzione tanh · [[Synchro_Kay_example (1).pdf#page=21|p. 21]], [[Synchro_Kay_example (1).pdf#page=22|22]]
**Fonte:** la slide scrive «it can be shown» e dà l'equazione trascendente.
**Si parte da:** la miscela (7) ([[probabilita-totale-e-bayes]]).

> 🧩 Derivazione mia:

$$
\begin{aligned}
f(y;A)&=\frac{1}{2\sqrt{2\pi\sigma^2}}\Big[e^{-\frac{(y+A)^2}{2\sigma^2}}+e^{-\frac{(y-A)^2}{2\sigma^2}}\Big] && \text{(7)}\\
&=\frac{1}{2\sqrt{2\pi\sigma^2}}\,e^{-\frac{y^2+A^2}{2\sigma^2}}\Big[e^{-\frac{Ay}{\sigma^2}}+e^{\frac{Ay}{\sigma^2}}\Big] && (y\pm A)^2=y^2+A^2\pm2Ay\\
&=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{y^2+A^2}{2\sigma^2}}\cosh\Big(\frac{Ay}{\sigma^2}\Big) && \cosh x=\tfrac{e^x+e^{-x}}2\\
\log f(y;A)&=c-\frac{y^2+A^2}{2\sigma^2}+\log\cosh\Big(\frac{Ay}{\sigma^2}\Big) && c\text{ non dipende da } A\\
\frac{\partial}{\partial A}\log f(y;A)&=-\frac{A}{\sigma^2}+\frac{y}{\sigma^2}\tanh\Big(\frac{Ay}{\sigma^2}\Big) && \tfrac{d}{dx}\log\cosh x=\tanh x\\
\sum_{k=0}^{K-1}\Big[-\frac{A}{\sigma^2}+\frac{y(k)}{\sigma^2}\tanh\Big(\frac{Ay(k)}{\sigma^2}\Big)\Big]&=0 && \text{derivata della (3) nulla}\\
\hat A&=\frac1K\sum_{k=0}^{K-1}y(k)\tanh\Big(\frac{\hat Ay(k)}{\sigma^2}\Big) && \text{moltiplico per } \sigma^2/K
\end{aligned}
$$

**Interpretazione:** confrontando con la stima training-based, $\tanh(\hat Ay(k)/\sigma^2)$ prende il posto del simbolo $b(k)$: è una **decisione soffice**. Infatti, con simboli equiprobabili, $E[b(k)\mid y(k)]=\frac{e^{Ay/\sigma^2}-e^{-Ay/\sigma^2}}{e^{Ay/\sigma^2}+e^{-Ay/\sigma^2}}=\tanh(Ay/\sigma^2)$ (Bayes con le (4)–(5)).
**Caso limite:** ad alto SNR ($A|y|/\sigma^2\gg1$) $\tanh\to\text{sgn}(y)$ e $\hat A\approx\frac1K\sum_k|y(k)|$: la stima diventa decision-directed, con le decisioni $\text{sgn}(y(k))$ al posto dei simboli noti.
**Ipotesi:** simboli indipendenti ed equiprobabili, rumore gaussiano di varianza $\sigma^2$ **nota** (serve nella tanh: è la «PSD del disturbo» citata nelle conclusioni della slide 20).

![[grafico-l13-verosimiglianza-blind.png]]
*🧩 Grafico mio (script `output/grafici/genera_grafici_lezioni13_14.py`). A sinistra la miscela (7) di p. 22 con $A=1$, $\sigma^2=0.25$: due gaussiane di peso ½ centrate in $\pm A$. A destra la log-verosimiglianza di 200 campioni simulati in funzione dell'$A$ di prova: con questo SNR la curva blind e quella training hanno lo stesso massimo, e l'iterazione di punto fisso della tanh converge allo stesso $\hat A$.*

### Derivazione — Indipendenza e somma dei logaritmi · [[Synchro_Kay_example (1).pdf#page=19|p. 19]]
Con campioni indipendenti $f(\mathbf y;A)=\prod_kf(y(k);A)$, e il logaritmo trasforma il prodotto in somma: $\log f(\mathbf y;A)=\sum_k\log f(y(k);A)$. Il logaritmo è crescente, quindi non sposta il massimo. Lo annotano gli appunti di p. 19.

## Spiegazione · [[Synchro_Kay_example (1).pdf#page=17|p. 17]], [[Synchro_Kay_example (1).pdf#page=23|23]], [[Synchro_Kay_example (1).pdf#page=24|24]]

- **Rivelazione come stima.** La rivelazione ML della Lezione 9 è una stima ML in cui il parametro (il simbolo trasmesso) può assumere solo $M$ valori: la massimizzazione è un confronto tra $M$ numeri, fatto con un banco di correlatori. Nella stima il parametro è continuo e si massimizza annullando la derivata.
- **Training (DA) e blind (NDA).** Con il training la stima è semplice e robusta, ma una parte della trasmissione è occupata da simboli noti (perdita di risorse). La stima blind non spreca simboli ma richiede la statistica dei simboli e del rumore ed è più complessa: si risolve un'equazione trascendente (per esempio iterando $\hat A\leftarrow\frac1K\sum y\tanh(\hat Ay/\sigma^2)$).
- La modalità decision-directed sta in mezzo: usa le decisioni del demodulatore come se fossero simboli di training, il che funziona se le decisioni sono affidabili.

## Perché importa

Le stime di ampiezza, fase, ritardo e frequenza servono al ricevitore per riportarsi nelle ipotesi del ricevitore ottimo ([[ricevitore-ottimo-awgn]]): senza sincronizzazione la costellazione ricevuta è scalata e ruotata e le regioni di decisione sono sbagliate. Sono il cuore della [[sincronizzazione]].

## Connessioni

- [[rivelazione-map-ml]]: stessa funzione di verosimiglianza; la rivelazione è il caso discreto.
- [[sincronizzazione]]: applica la MLE alla fase (stimatore $\arg\langle y,s\rangle$).
- [[phase-locked-loop]]: realizza in modo iterativo la massimizzazione della log-verosimiglianza.
- [[probabilita-totale-e-bayes]]: la verosimiglianza blind è una probabilità totale.

## Fonti · [[Synchro_Kay_example (1).pdf#page=12|p. 12]]–[[Synchro_Kay_example (1).pdf#page=24|24]]

- [[parameter-estimation-synchronization]]

_Aggiornato: 2026-11-16 — creazione da ingest Synchro_Kay_example (1).pdf (Lezione 13)_
