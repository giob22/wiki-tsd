---
tipo: concetto
importanza_esame: media
prerequisiti: ["ofdm", "ofdm-con-fft", "prefisso-ciclico", "sincronizzazione"]
fonti_pdf: ["ofdm_goldsmith_slides.pdf#page=54", "ofdm_goldsmith_slides.pdf#page=55", "ofdm_goldsmith_slides.pdf#page=56", "ofdm_goldsmith_slides.pdf#page=57", "ofdm_goldsmith_slides.pdf#page=58"]
---

# Limiti dell'OFDM: PAPR, offset di frequenza e di tempo, scelta di N

## Definizione · [[ofdm_goldsmith_slides.pdf#page=54|p. 54]], [[ofdm_goldsmith_slides.pdf#page=56|56]], [[ofdm_goldsmith_slides.pdf#page=58|58]]

- **PAPR** (*peak-to-average power ratio*): l'OFDM somma molte sinusoidi complesse, che ogni tanto si allineano in fase e producono un picco molto più alto della potenza media.
- **Offset di frequenza** (*carrier-frequency offset*): l'ortogonalità delle sottoportanti si basa su una spaziatura **esatta** $\Delta f=1/T_u$; un errore $\delta f$ dell'oscillatore del ricevitore fa nascere ICI. L'OFDM è sensibile agli errori di frequenza dell'oscillatore.
- **Offset di tempo**: un errore di timing *dentro* il CP, se la finestra FFT contiene ancora campioni periodici validi, provoca soprattutto una **rampa di fase** lungo le sottoportanti; oltre il CP provoca ISI e ICI.
- **Scelta di $N$**: compromesso tra overhead del CP, sensibilità all'offset di frequenza e PAPR.

## Formule · [[ofdm_goldsmith_slides.pdf#page=54|p. 54]]–[[ofdm_goldsmith_slides.pdf#page=58|58]]

| Formula | Significato |
|---|---|
| $\text{PAPR}=\dfrac{\max_{0\le t<T_u}\lvert f_n(t)\rvert^2}{\frac{1}{T_u}\int_0^{T_u}\lvert f_n(t)\rvert^2dt}$ | rapporto picco/media di un blocco |
| $x[0]=\sqrt N$, $\frac1N\sum_q\lvert x[q]\rvert^2=1$ ⇒ PAPR campionato $=N$ ($10\log_{10}N$ dB) | caso peggiore: simboli tutti in fase, $\lvert a[k]\rvert=1$ |
| $\frac{1}{T_u}\int_0^{T_u}e^{j2\pi[(k-i)/T_u+\delta f]t}dt\neq0$ per $k\neq i$ | proiezione con offset $\delta f$: ICI |
| $\epsilon_f=\delta f/\Delta f$ | offset normalizzato alla spaziatura |
| $Y[k]=C_0(\epsilon_f)H[k]a[k]+\sum_{i\neq k}C_{k-i}(\epsilon_f)H[i]a[i]+W[k]$ | modello discreto: utile + ICI |
| $C_m(\epsilon_f)=\frac1N\sum_{q=0}^{N-1}e^{j2\pi(\epsilon_f-m)q/N}$ | coefficienti di dispersione |

Simboli: $\delta f$ errore di frequenza della portante al ricevitore [Hz]; $\Delta f=1/T_u$ spaziatura [Hz]; $f_n(t)$ blocco utile; $x[q]$ uscita della IFFT unitaria.

## Derivazioni

### Derivazione — PAPR nel caso peggiore · [[ofdm_goldsmith_slides.pdf#page=55|p. 55]]

**Fonte:** slide 50. **Si parte da:** IFFT unitaria $x[q]=\frac{1}{\sqrt N}\sum_ka[k]e^{j2\pi kq/N}$ e simboli tutti con la stessa fase e $\lvert a[k]\rvert=1$ (per esempio $a[k]=1$).

$$
\begin{aligned}
x[0]&=\frac{1}{\sqrt N}\sum_{k=0}^{N-1}a[k]=\frac{N}{\sqrt N}=\sqrt N && q=0:\ \text{tutti gli esponenziali valgono }1\\
\lvert x[0]\rvert^2&=N && \text{picco}\\
\frac1N\sum_{q=0}^{N-1}\lvert x[q]\rvert^2&=\frac1N\sum_{k=0}^{N-1}\lvert a[k]\rvert^2=\frac NN=1 && \text{Parseval (IFFT unitaria)}\\
\text{PAPR}&=\frac{N}{1}=N\quad\big(10\log_{10}N\ \text{dB}\big) && \text{rapporto}
\end{aligned}
$$

**Numeri:** $N=16$ → $12$ dB; $N=64$ → $18$ dB (🧩). La figura della slide 49, un blocco con $N=16$ simboli QPSK casuali, ha un picco di $8.0$ dB: un blocco tipico sta sotto il caso peggiore.
**Sanity check:** con tutti i simboli in fase gli $N$ fasori si sommano in ampiezza ($N$ volte), mentre la potenza media cresce solo come $N$: il rapporto è $N$.
**Ipotesi:** PAPR **campionato** (sui soli $N$ campioni); il segnale continuo può avere picchi tra un campione e l'altro.

![[grafico-l15-papr-ccdf.png|640]]

*🧩 Probabilità che il PAPR di un blocco con simboli QPSK casuali superi una soglia, per $N=16,64,256$ (simulazione con IFFT sovracampionata, script `output/grafici/genera_grafici_lezione15.py`). Le curve si spostano a destra al crescere di $N$, come dice la slide 53; il caso peggiore $10\log_{10}N$ dB è rarissimo, ma picchi di 8–11 dB sono frequenti.*

### Derivazione — L'offset di frequenza rompe l'ortogonalità · [[ofdm_goldsmith_slides.pdf#page=56|p. 56]]

**Fonte:** slide 51. **Si parte da:** il segnale ricevuto contiene il fattore $e^{j2\pi\delta ft}$; la proiezione della sottoportante $k$ sul correlatore $i$ è proporzionale a

$$
\begin{aligned}
\frac{1}{T_u}\int_0^{T_u}e^{j2\pi[(k-i)/T_u+\delta f]t}dt&=e^{j\pi\nu T_u}\,\text{sinc}(\nu T_u),\quad\nu=\frac{k-i}{T_u}+\delta f && \text{condizione sinc della slide 11}\\
\nu T_u&=(k-i)+\delta fT_u=(k-i)+\epsilon_f && \delta fT_u=\delta f/\Delta f
\end{aligned}
$$

La sinc si annulla solo se $\nu T_u$ è un intero non nullo: per $k\neq i$ e $\epsilon_f$ non intero l'integrale è diverso da zero, quindi la variabile di decisione $i$ contiene contributi delle altre sottoportanti (**ICI**); e per $k=i$ vale $\text{sinc}(\epsilon_f)<1$, cioè si perde anche segnale utile.

### Derivazione — Modello discreto con offset: i coefficienti $C_m(\epsilon_f)$ · [[ofdm_goldsmith_slides.pdf#page=57|p. 57]]

**Fonte:** slide 52, risultato dato. **Si parte da:** campioni utili senza rumore $y[q]=\frac{1}{\sqrt N}\sum_iH[i]a[i]e^{j2\pi iq/N}$ (canale diagonale, CP sufficiente) moltiplicati per l'offset campionato.

$$
\begin{aligned}
e^{j2\pi\delta f\,qT_c}&=e^{j2\pi\delta f\,qT_u/N}=e^{j2\pi\epsilon_fq/N} && T_c=T_u/N,\ \delta fT_u=\epsilon_f\\
Y[k]&=\frac{1}{\sqrt N}\sum_{q=0}^{N-1}e^{j2\pi\epsilon_fq/N}\,\frac{1}{\sqrt N}\sum_iH[i]a[i]e^{j2\pi iq/N}\,e^{-j2\pi kq/N} && \text{DFT unitaria}\\
&=\sum_iH[i]a[i]\,\underbrace{\frac1N\sum_{q=0}^{N-1}e^{j2\pi(\epsilon_f-(k-i))q/N}}_{C_{k-i}(\epsilon_f)} && \text{scambio le somme}\\
&=\underbrace{C_0(\epsilon_f)H[k]a[k]}_{i=k:\ \text{utile}}+\underbrace{\sum_{i\neq k}C_{k-i}(\epsilon_f)H[i]a[i]}_{\text{ICI}}\ (+W[k]) && \text{separo } i=k
\end{aligned}
$$

**Sanity check:** per $\epsilon_f=0$: $C_0=\frac1N\cdot N=1$ e $C_m=\frac1N\sum_qe^{-j2\pi mq/N}=0$ per $m\neq0$ (serie geometrica): si ritrova $Y[k]=H[k]a[k]+W[k]$. Inoltre $\sum_m\lvert C_m(\epsilon_f)\rvert^2=1$ (Parseval sulla sequenza $e^{j2\pi\epsilon_fq/N}/N$): l'offset non distrugge potenza, la **sposta** dalla sottoportante giusta alle vicine.
**Ipotesi:** offset costante sul blocco; canale LTI per tutta la trasmissione (slide 52).

![[grafico-l15-ici-cfo.png|680]]

*🧩 A sinistra la frazione di potenza che resta sulla sottoportante, $\lvert C_0(\epsilon_f)\rvert^2$, e quella che finisce in ICI, $1-\lvert C_0(\epsilon_f)\rvert^2$, per $N=64$; a destra il loro rapporto in dB (script `output/grafici/genera_grafici_lezione15.py`). Con un offset del 10% della spaziatura ($\epsilon_f=0.1$) il rapporto segnale/ICI è già sceso a circa 15 dB, per quanto basso sia il rumore: è un pavimento dovuto all'interferenza.*

### Derivazione — Offset di tempo dentro il CP: rampa di fase · [[ofdm_goldsmith_slides.pdf#page=57|p. 57]]

**Fonte:** slide 52, affermazione senza calcolo. **Si parte da:** finestra FFT anticipata di $d$ campioni, con $0<d\le L_{cp}-L_h$ (la finestra contiene ancora solo campioni periodici validi del blocco $n$).

$$
\begin{aligned}
y'[q]&=y[(q-d)\bmod N] && \text{i campioni osservati sono una rotazione circolare}\\
Y'[k]&=e^{-j2\pi kd/N}\,Y[k]=e^{-j2\pi kd/N}H[k]a[k]+W'[k] && \text{proprietà di traslazione circolare della DFT}
\end{aligned}
$$

🧩 Derivazione mia: la fase $-2\pi kd/N$ cresce **linearmente** con l'indice $k$, è la rampa di fase della slide. Non c'è ICI e la si compensa insieme a $H[k]$ (sembra un canale con un ritardo in più). Se invece la finestra esce dalla zona valida, entra un pezzo del blocco precedente o successivo: ISI e ICI.

### Derivazione — Tabella della scelta di $N$ · [[ofdm_goldsmith_slides.pdf#page=58|p. 58]]

**Fonte:** slide 53, con $T_c$ fisso e $L_{cp}=8$:

| $N$ | $T_u$ | frazione di CP $L_{cp}/(N+L_{cp})$ | spaziatura $\Delta f=1/T_u$ |
|---|---|---|---|
| 16 | $16T_c$ | $8/24=33.3\%$ | $1/(16T_c)$ |
| 64 | $64T_c$ | $8/72=11.1\%$ | $1/(64T_c)$ |
| 128 | $128T_c$ | $8/136=5.9\%$ | $1/(128T_c)$ |

$N$ più grande riduce l'overhead **frazionario** del CP a parità di memoria del canale, ma riduce la spaziatura $\Delta f=1/T_u$: un offset di frequenza fisso $\delta f$ diventa un $\epsilon_f=\delta f/\Delta f=\delta f\,NT_c$ più grande, e l'ICI cresce. Anche il PAPR possibile cresce con $N$, e questo complica il progetto dell'amplificatore di potenza.

**Sanity check:** passando da $N=16$ a $N=128$ l'overhead scende di circa 6 volte, ma $\epsilon_f$ cresce di 8 volte a parità di $\delta f$.

## Spiegazione · [[ofdm_goldsmith_slides.pdf#page=54|p. 54]], [[ofdm_goldsmith_slides.pdf#page=56|56]], [[ofdm_goldsmith_slides.pdf#page=58|58]]

- **Perché il PAPR è un problema.** Un PAPR alto richiede un amplificatore di potenza lineare su un'ampia dinamica, quindi un grande *back-off* (si lavora lontano dalla saturazione), e questo abbassa l'efficienza in potenza. I picchi possono causare *clipping* e distorsione non lineare, con emissioni fuori banda.
- **Perché l'offset di frequenza è grave.** La sinc delle sottoportanti è larga $\Delta f$: spostarsi di una frazione di $\Delta f$ fa uscire dagli zeri delle altre sottoportanti. È la stessa sensibilità detta negli appunti di p. 14 ("basta una minima variazione della frequenza e ho ICI"), e il motivo per cui la sincronizzazione di portante della Lezione 13 è essenziale per l'OFDM.
- **La scelta di $N$** non è "più piccolo è meglio" né il contrario: si sceglie insieme alla memoria del canale, all'overhead di guardia e alla precisione di sincronizzazione (slide 53).

> 🎯 Esame: dare la definizione di PAPR e il caso peggiore $N$; spiegare perché un offset di frequenza crea ICI e un offset di tempo dentro il CP solo una rampa di fase; discutere i compromessi nella scelta di $N$.

## Perché importa · [[ofdm_goldsmith_slides.pdf#page=56|p. 56]], [[ofdm_goldsmith_slides.pdf#page=58|58]]

Sono il rovescio della medaglia dell'ortogonalità esatta: l'OFDM elimina ISI e ICI solo se tempo e frequenza sono quelli giusti, e chiede un'elettronica lineare. Sono i punti da citare quando si confronta l'OFDM con la trasmissione a portante singola equalizzata.

## Connessioni

- [[ofdm]] — la condizione sinc da cui nasce la sensibilità all'offset.
- [[sincronizzazione]] — stima di $\Delta f$ e del timing (Lezione 13): qui si vede che cosa costa sbagliarle.
- [[prefisso-ciclico]] — un CP più lungo del canale dà margine all'errore di timing.
- [[ofdm-con-fft]] — PAPR calcolato sui campioni della IFFT; Parseval.

> 📚 Approfondimento (non d'esame): [[multiportante-ofdm-dmt-gelli]] — fattore di cresta e distribuzione gaussiana dell'ampiezza del segnale multiportante, sensibilità a sincronismo e Doppler.

## Fonti · [[ofdm_goldsmith_slides.pdf#page=54|p. 54]]–[[ofdm_goldsmith_slides.pdf#page=58|58]]

- [[signaling-ofdm]] — Lezione 15, slide 49–53.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15, ofdm_goldsmith_slides.pdf)_
