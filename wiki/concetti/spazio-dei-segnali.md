---
tipo: concetto
importanza_esame: alta
prerequisiti: ["teorema-del-campionamento", "inviluppo-complesso"]
fonti_pdf: ["Modulazione.pdf#page=12", "Modulazione.pdf#page=14", "Modulazione.pdf#page=16", "Modulazione.pdf#page=20", "Detection.pdf#page=14"]
---

# Spazio dei segnali

## Definizione · [[Modulazione.pdf#page=12|p. 12]]–[[Modulazione.pdf#page=22|22]]

Le $M$ forme d'onda $\mathcal S=\{s_i(t)\}_{i=1}^M$ di un modulatore, limitate in durata e in banda, stanno in uno spazio vettoriale di dimensione finita $n\le M$. Scelta una **base ortonormale** $\psi_1(t),\dots,\psi_n(t)$ di quello spazio, ogni forma d'onda è rappresentata dal vettore dei suoi coefficienti $\mathbf s_i=[s_i(1),\dots,s_i(n)]^T$. Il passaggio conserva prodotti scalari e distanze, quindi energia, rumore e decisioni si studiano con la **geometria** dei punti della costellazione.

## Formule · [[Modulazione.pdf#page=14|p. 14]], [[Modulazione.pdf#page=16|p. 16]], [[Modulazione.pdf#page=20|p. 20]]

| Formula | Significato |
|---|---|
| $s_i(t)=\sum_\ell s_i(\ell/W)\,\text{sinc}(Wt-\ell)$ | rappresentazione con i campioni (Nyquist) |
| $D=WT_0$ | gradi di libertà complessi (prodotto tempo-banda); $2WT_0$ reali |
| $\langle\psi_k,\psi_\ell\rangle=\delta_{k\ell}$ | base ortonormale |
| $s_i(t)=\sum_{\ell=1}^ns_i(\ell)\psi_\ell(t)$, $s_i(\ell)=\langle s_i,\psi_\ell\rangle$ | sviluppo e coefficienti |
| $\langle s_i(t),s_j(t)\rangle=\langle\mathbf s_i,\mathbf s_j\rangle$ | conservazione del prodotto scalare |

> 🧮 Formula chiave: $s_i(\ell)=\displaystyle\int_{\mathcal T}s_i(t)\,\psi_\ell^\ast(t)\,dt$ e $\langle s_i(t),s_j(t)\rangle=\langle\mathbf s_i,\mathbf s_j\rangle$.

Simboli: $W$ [Hz] banda del canale complesso; $T_0$ [s] durata considerata; $n\le M\le D$ dimensione effettiva; $\mathcal T$ intervallo di durata $T_0$.

## Derivazioni

### Derivazione — Conservazione del prodotto scalare · [[Modulazione.pdf#page=20|p. 20]], [[Modulazione.pdf#page=22|22]]
**Fonte:** la slide dice «it can be easily proven»; gli appunti di p. 22 svolgono il conto.

$$
\begin{aligned}
\langle s_i(t),s_j(t)\rangle&=\int_{\mathcal T}\Big[\sum_{\ell=1}^ns_i(\ell)\psi_\ell(t)\Big]\Big[\sum_{k=1}^ns_j(k)\psi_k(t)\Big]^\ast dt && \text{sviluppo sulla base}\\
&=\sum_{\ell=1}^n\sum_{k=1}^ns_i(\ell)s_j^\ast(k)\int_{\mathcal T}\psi_\ell(t)\psi_k^\ast(t)\,dt && \text{linearità}\\
&=\sum_{\ell=1}^n\sum_{k=1}^ns_i(\ell)s_j^\ast(k)\,\delta_{\ell k}=\sum_{\ell=1}^ns_i(\ell)s_j^\ast(\ell)=\langle\mathbf s_i,\mathbf s_j\rangle && \text{ortonormalità}
\end{aligned}
$$

Con $i=j$ si ottiene $E_i=\lVert s_i(t)\rVert^2=\lVert\mathbf s_i\rVert^2$; sviluppando $\lVert s_i-s_j\rVert^2$ anche le distanze si conservano.

### Derivazione — Gradi di libertà $D=WT_0$ · [[Modulazione.pdf#page=16|p. 16]], [[Modulazione.pdf#page=17|17]]
**Fonte:** slide 9 e appunti p. 17.

$$
\begin{aligned}
\text{campioni in } T_0&=\frac{T_0}{1/W}=WT_0 && \text{un campione complesso ogni } 1/W\\
\text{gradi reali}&=2WT_0 && \text{ogni campione complesso porta parte reale e immaginaria}
\end{aligned}
$$

È lo stesso conteggio $N=2WT$ della banda di Shannon ([[parametri-globali-modulazioni]]). Vale solo in modo approssimato: un segnale di durata finita non è a banda limitata ($X_{T_0}(f)=X(f)\ast T_0\,\text{sinc}(fT_0)$), ma per $T_0$ grande lo è quasi.

### Derivazione — Procedura di Gram-Schmidt · [[Detection.pdf#page=14|p. 14]], [[Detection.pdf#page=6|p. 6]]
**Fonte:** dispense p. 5 (la nomina) e appunti p. 6 (i primi passi).

$$
\begin{aligned}
\psi_1(t)&=\frac{s_1(t)}{\lVert s_1(t)\rVert} && \text{normalizzo il primo segnale}\\
\psi_2'(t)&=s_2(t)-\langle s_2,\psi_1\rangle\psi_1(t),\qquad\psi_2=\frac{\psi_2'}{\lVert\psi_2'\rVert} && \text{tolgo la componente lungo } \psi_1\\
\psi_3'(t)&=s_3(t)-\langle s_3,\psi_1\rangle\psi_1-\langle s_3,\psi_2\rangle\psi_2,\qquad\psi_3=\frac{\psi_3'}{\lVert\psi_3'\rVert} && \text{e così via}
\end{aligned}
$$

Se un $\psi_k'$ risulta nullo, $s_k$ è combinazione lineare dei precedenti e non aggiunge una dimensione: per questo $n\le M$.

## Spiegazione · appunti [[Modulazione.pdf#page=13|p. 13]], [[Modulazione.pdf#page=18|18]], [[Modulazione.pdf#page=19|19]], [[Modulazione.pdf#page=22|22]]

Lavorare con funzioni del tempo è scomodo: integrali, convoluzioni, forme diverse per ogni modulazione. L'idea è rappresentare ogni forma d'onda con **pochi numeri**.

1. **Quanti numeri servono al massimo.** Un canale di banda $W$ usato per $T_0$ secondi offre circa $D=WT_0$ gradi di libertà complessi (Nyquist): è lo spazio che il canale mette a disposizione.
2. **Quanti ne servono davvero.** Il modulatore usa solo $M$ forme d'onda, che generano un sottospazio di dimensione $n\le M$, di solito molto più piccolo di $D$. Usare tutti i $D$ campioni sarebbe ridondante.
3. **Come si ottengono.** Con una base ortonormale del sottospazio (Gram-Schmidt) ogni forma d'onda diventa un punto di $\mathbb R^n$ o $\mathbb C^n$: la **costellazione**.
4. **Perché funziona.** Prodotti scalari e distanze sono gli stessi nei due mondi: l'energia di un segnale è la lunghezza al quadrato del suo vettore, la distanza tra due segnali è la distanza tra due punti. Il ricevitore ottimo decide in base alle distanze ([[ricevitore-ottimo-awgn]]).

> 🎯 Esame: perché si passa ai vettori, gradi di libertà $D=WT_0$, base ortonormale e coefficienti, dimostrazione che il prodotto scalare si conserva, Gram-Schmidt.

## Perché importa

È il linguaggio di tutto il resto del corso: costellazioni PAM, PSK, QAM sono punti dello spazio dei segnali, il rumore proiettato sulla base è un vettore gaussiano, e la probabilità d'errore dipende solo dalle distanze tra i punti ([[probabilita-errore-binaria]]).

## Connessioni

- [[teorema-del-campionamento]] — i campioni $s_i(\ell/W)$ come prima rappresentazione discreta.
- [[inviluppo-complesso]] — il canale passa-banda diventa un canale complesso in banda base su $[-W/2,W/2]$.
- [[parametri-globali-modulazioni]] — $N=2WT$ e la banda di Shannon.
- [[ricevitore-ottimo-awgn]] — la decisione a minima distanza nello spazio dei segnali.

## Fonti · [[Modulazione.pdf#page=12|p. 12]]–[[Modulazione.pdf#page=22|22]] · Detection [[Detection.pdf#page=6|p. 6]], [[Detection.pdf#page=14|14]]

[[principles-of-modulation]] — Modulazione.pdf, slide 7–10 e appunti; [[elementi-teoria-rivelazione]] — Gram-Schmidt.

_Aggiornato: 2026-11-16 — creazione da ingest Modulazione.pdf e Detection.pdf_
