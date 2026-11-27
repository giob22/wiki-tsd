---
tipo: concetto
importanza_esame: alta
prerequisiti: ["prefisso-ciclico", "equalizzazione"]
fonti_pdf: ["ofdm_goldsmith_slides.pdf#page=32", "ofdm_goldsmith_slides.pdf#page=41", "ofdm_goldsmith_slides.pdf#page=42", "ofdm_goldsmith_slides.pdf#page=43", "ofdm_goldsmith_slides.pdf#page=44", "ofdm_goldsmith_slides.pdf#page=45", "ofdm_goldsmith_slides.pdf#page=53"]
---

# Equalizzazione nel dominio della frequenza, codifica e modulazione adattativa nell'OFDM

## Definizione · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=41|41]], [[ofdm_goldsmith_slides.pdf#page=44|44]]

Dopo la rimozione di un CP sufficiente e la FFT, ogni sottoportante vede un canale **scalare** $Y[k]=H[k]a[k]+W[k]$. L'equalizzazione si fa allora **separatamente su ogni sottoportante** con una sola presa complessa (*one-tap frequency-domain equalization*): la matrice del canale in frequenza è **diagonale**. I coefficienti $H[k]$ possono essere diversi da una sottoportante all'altra; le sottoportanti molto attenuate si proteggono con codifica e interleaving, o con costellazioni diverse per tono (modulazione adattativa).

## Formule · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=41|41]]–[[ofdm_goldsmith_slides.pdf#page=44|44]], [[ofdm_goldsmith_slides.pdf#page=53|53]]

| Formula | Significato |
|---|---|
| $\mathbf Y_n=\boldsymbol\Lambda_H\,\mathbf a_n+\mathbf W_n$, $\boldsymbol\Lambda_H=\text{diag}(H[0],\dots,H[N-1])$ | $N$ relazioni scalari indipendenti |
| $\hat a_i[n]=\dfrac{r_i[n]}{H(i/T_u)}=a_i[n]+\dfrac{w_i[n]}{H(i/T_u)}$ | divisione complessa (tempo continuo) |
| $\hat a_{ZF}[k]=\dfrac{Y[k]}{H[k]}$, $H[k]\neq0$; varianza del rumore $N_0/\lvert H[k]\rvert^2$ | zero forcing a una presa |
| $\hat a_{LMMSE}[k]=\dfrac{E_sH^\ast[k]}{E_s\lvert H[k]\rvert^2+N_0}\,Y[k]$ | MMSE lineare a una presa |
| $H[k]=1+\alpha e^{-j2\pi k/N}$ | canale a due prese $h[0]=1$, $h[1]=\alpha$ |
| $\lvert H[k]\rvert^2=4\cos^2(\pi k/16)$ per $\alpha=1$, $N=16$ | nullo spettrale in $k=8$ |
| $R_{gross}=\frac1T\sum_{k\in\mathcal D}\log_2M_k$, $M_k\ge2$ | bit rate lordo con costellazioni diverse per tono |

Simboli: $E_s$ energia media dei simboli; $N_0$ varianza del rumore su ogni uscita FFT; $\mathcal D$ insieme dei toni dati attivi; $M_k$ ordine della costellazione sul tono $k$; $T=T_u+T_g$ durata del simbolo OFDM [s].

## Derivazioni

### Derivazione — Matrice diagonale ed equalizzazione indipendente · [[ofdm_goldsmith_slides.pdf#page=41|p. 41]]

**Fonte:** slide 36. Mettendo in colonna le $N$ relazioni $Y_n[k]=H[k]a_k[n]+W_n[k]$ di [[prefisso-ciclico]]:

$$
\underbrace{\begin{bmatrix}Y_n[0]\\ \vdots\\ Y_n[N-1]\end{bmatrix}}_{\mathbf Y_n}=\underbrace{\begin{bmatrix}H[0]&&0\\&\ddots&\\0&&H[N-1]\end{bmatrix}}_{\boldsymbol\Lambda_H}\underbrace{\begin{bmatrix}a_0[n]\\ \vdots\\ a_{N-1}[n]\end{bmatrix}}_{\mathbf a_n}+\mathbf W_n
$$

Fuori diagonale ci sono zeri perché il canale non mescola sottoportanti diverse: invertire $\boldsymbol\Lambda_H$ vuol dire dividere ogni riga per il suo $H[k]$. Il modello diagonale regge solo con le ipotesi dette: CP sufficiente, sincronizzazione, canale LTI.

### Derivazione — Esempio a due prese e nullo spettrale · [[ofdm_goldsmith_slides.pdf#page=42|p. 42]], [[ofdm_goldsmith_slides.pdf#page=43|43]]

**Fonte:** slide 37–38. **Si parte da:** $h[0]=1$, $h[1]=\alpha$, $h[\ell]=0$ per $\ell\ge2$ (quindi $L_h=1$, basta $L_{cp}\ge1$).

$$
\begin{aligned}
H[k]&=\sum_\ell h[\ell]e^{-j2\pi k\ell/N}=1+\alpha e^{-j2\pi k/N} && \text{DFT non unitaria dei tap}\\
Y_n[k]&=\big(1+\alpha e^{-j2\pi k/N}\big)a_k[n]+W_n[k] && \text{relazione in frequenza}\\
\alpha=1:\ \lvert H[k]\rvert^2&=\lvert1+e^{-j\theta}\rvert^2=(1+\cos\theta)^2+\sin^2\theta && \theta=2\pi k/N\\
&=2+2\cos\theta=4\cos^2(\theta/2) && 1+\cos\theta=2\cos^2(\theta/2)\\
N=16:\ \lvert H[k]\rvert^2&=4\cos^2\Big(\frac{\pi k}{16}\Big) && \theta/2=\pi k/16
\end{aligned}
$$

**Numeri:** $k=0$: $4$; $k=4$: $4\cos^2(\pi/4)=2$; $k=8$: $4\cos^2(\pi/2)=0$, cioè $H[8]=1+e^{-j\pi}=0$.
**Sanity check:** il canale $1+z^{-1}$ è un filtro a media mobile, passa-basso, con lo zero a metà banda: è il grafico della slide 38, con i 16 valori campionati sulla curva continua.
**Ipotesi:** canale noto e LTI.

Sottoportanti diverse hanno coefficienti complessi diversi, ma restano relazioni scalari separate. Non serve un modello di propagazione radio: basta la risposta impulsiva elementare di un sistema LTI. In $k=8$ però il simbolo **non arriva** al ricevitore e nessun equalizzatore può recuperarlo: il CP elimina l'interferenza, **non i nulli spettrali**.

### Derivazione — Zero forcing e MMSE a una presa · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=44|44]]

**Fonte:** slide 27 e 39, risultati dati. **Si parte da:** $Y=Ha+W$ su un tono fissato, con $E\{\lvert a\rvert^2\}=E_s$, $E\{\lvert W\rvert^2\}=N_0$, $a$ e $W$ indipendenti a media nulla.

$$
\begin{aligned}
\hat a_{ZF}&=\frac{Y}{H}=a+\frac{W}{H} && \text{divido per } H\neq0\\
E\Big\{\Big\lvert\frac WH\Big\rvert^2\Big\}&=\frac{N_0}{\lvert H\rvert^2} && \text{rumore amplificato se }\lvert H\rvert\text{ è piccolo}\\
\hat a&=cY,\quad c=\arg\min_cE\{\lvert a-cY\rvert^2\} && \text{MMSE lineare}\\
E\{(a-cY)Y^\ast\}&=0\ \Rightarrow\ c=\frac{E\{aY^\ast\}}{E\{\lvert Y\rvert^2\}} && \text{principio di ortogonalità}\\
E\{aY^\ast\}&=E\{a(Ha+W)^\ast\}=H^\ast E_s,\qquad E\{\lvert Y\rvert^2\}=\lvert H\rvert^2E_s+N_0 && \text{indipendenza di } a,\ W\\
\hat a_{LMMSE}&=\frac{E_sH^\ast}{E_s\lvert H\rvert^2+N_0}\,Y && \text{sostituisco}
\end{aligned}
$$

**Sanity check:** per $N_0\to0$ il coefficiente diventa $E_sH^\ast/(E_s\lvert H\rvert^2)=1/H$: si ritrova lo ZF. Per $\lvert H\rvert\to0$ il coefficiente tende a $0$ invece di esplodere: l'MMSE limita l'amplificazione del rumore.
**Ipotesi:** canale noto, simboli indipendenti. La stima MMSE è **polarizzata**: $E\{\hat a\mid a\}=\frac{E_s\lvert H\rvert^2}{E_s\lvert H\rvert^2+N_0}\,a\neq a$.

> 💡 Connessione: sono le versioni scalari dello ZF e dell'MMSE della Lezione 14 ([[equalizzazione]]): là $\mathbf c_{MMSE}=\sigma_s^2\mathbf R_{rr}^{-1}\mathbf p_0$, qui $\mathbf p_0$ si riduce al numero $H$ e $\mathbf R_{rr}$ al numero $E_s\lvert H\rvert^2+N_0$. Anche il difetto dello ZF è lo stesso: amplifica il rumore dove il canale attenua.

### Derivazione — Bit per blocco con modulazione adattativa · [[ofdm_goldsmith_slides.pdf#page=53|p. 53]]

**Fonte:** slide 48. Nella figura i toni $0,\dots,6$ usano QPSK, QPSK, 16-QAM, 64-QAM, nessun dato, 16-QAM, QPSK:

$$\sum_{k\in\mathcal D}\log_2M_k=2+2+4+6+0+4+2=20\ \text{bit per blocco},\qquad R_{gross}=\frac{20}{T}$$

(🧩 conto mio sulla figura; il tono 4, debole, non porta dati ed è escluso da $\mathcal D$.)

## Spiegazione · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=44|44]], [[ofdm_goldsmith_slides.pdf#page=45|45]], [[ofdm_goldsmith_slides.pdf#page=53|53]]

- **Un'equalizzazione che costa una divisione.** Dentro il modello ideale il ricevitore non ha bisogno di un equalizzatore multicanale o di sequenza (slide 27): una divisione complessa per sottoportante compensa il canale. Se $\lvert H(i/T_u)\rvert$ è piccolo, la divisione amplifica il rumore.
- **Serve conoscere il canale.** La rivelazione coerente richiede di stimare $H[k]$ (slide 39): per questo alcune posizioni della IFFT sono riservate ai **piloti** ([[ofdm-con-fft]]).
- **Codifica e interleaving (slide 40).** Se $\lvert H[k]\rvert$ è piccolo su alcuni toni, i simboli rivelati lì sono poco affidabili. Il codice di canale aggiunge ridondanza; l'**interleaver** sparge i bit codificati su sottoportanti e blocchi OFDM diversi (la griglia tempo-frequenza della figura, con le celle colorate come schema, non un codice specifico). Il decodificatore usa i bit ricevuti bene per correggere quelli dei toni attenuati: è il motivo semplice per cui l'OFDM si combina con codifica e interleaving in frequenza.
- **Modulazione adattativa (slide 48).** Se il trasmettitore conosce i guadagni $H[k]$ può cambiare ordine della costellazione o potenza da un tono all'altro: costellazioni robuste (o nessun dato) sui toni deboli, più bit sui toni forti. Richiede che il trasmettitore abbia informazione sulla qualità del canale, e non è obbligatoria in tutti gli standard OFDM.

> 🎯 Esame: scrivere ZF e MMSE a una presa, dire perché bastano (matrice diagonale) e perché un nullo spettrale non si recupera; spiegare il ruolo di codifica, interleaving e modulazione adattativa.

## Perché importa · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=43|43]]

Confrontata con la Lezione 14 è la grande semplificazione dell'OFDM: invece di un equalizzatore frazionario con il suo vettore di coefficienti o di un traliccio di Viterbi a $M^L$ stati, $N$ divisioni. Il prezzo è che i toni attenuati restano attenuati: l'OFDM sposta il problema dall'ISI alla diversità in frequenza, da recuperare con la codifica.

## Connessioni

- [[equalizzazione]] — ZF e MMSE vettoriali della Lezione 14; qui diventano scalari.
- [[prefisso-ciclico]] — da cui viene $Y_n[k]=H[k]a_k[n]+W_n[k]$.
- [[stima-dei-parametri]] — la stima di $H[k]$ dai piloti è una stima training-based come quella dell'ampiezza nella Lezione 13.
- [[ieee-802-11a]] — 48 portanti dati, costellazioni da BPSK a 64-QAM.

> 📚 Approfondimento (non d'esame): [[multiportante-ofdm-dmt-gelli]] — il bit loading ottimo (water filling) e la probabilità d'errore QAM per sottoportante, che danno la versione quantitativa della modulazione adattativa.

## Fonti · [[ofdm_goldsmith_slides.pdf#page=32|p. 32]], [[ofdm_goldsmith_slides.pdf#page=41|41]]–[[ofdm_goldsmith_slides.pdf#page=45|45]], [[ofdm_goldsmith_slides.pdf#page=53|53]]

- [[signaling-ofdm]] — Lezione 15, slide 27, 36–40, 48.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15, ofdm_goldsmith_slides.pdf)_
