---
tipo: concetto
importanza_esame: alta
prerequisiti: ["interferenza-intersimbolica", "spazio-dei-segnali", "ricevitore-ottimo-awgn", "densita-spettrale-di-potenza", "upconversion-e-downconversion"]
fonti_pdf: ["ofdm_goldsmith_slides.pdf#page=2", "ofdm_goldsmith_slides.pdf#page=3", "ofdm_goldsmith_slides.pdf#page=4", "ofdm_goldsmith_slides.pdf#page=5", "ofdm_goldsmith_slides.pdf#page=6", "ofdm_goldsmith_slides.pdf#page=7", "ofdm_goldsmith_slides.pdf#page=8", "ofdm_goldsmith_slides.pdf#page=9", "ofdm_goldsmith_slides.pdf#page=10", "ofdm_goldsmith_slides.pdf#page=11", "ofdm_goldsmith_slides.pdf#page=12", "ofdm_goldsmith_slides.pdf#page=13", "ofdm_goldsmith_slides.pdf#page=14", "ofdm_goldsmith_slides.pdf#page=15", "ofdm_goldsmith_slides.pdf#page=16", "ofdm_goldsmith_slides.pdf#page=17", "ofdm_goldsmith_slides.pdf#page=18", "ofdm_goldsmith_slides.pdf#page=19", "ofdm_goldsmith_slides.pdf#page=20", "ofdm_goldsmith_slides.pdf#page=21", "ofdm_goldsmith_slides.pdf#page=22"]
---

# OFDM: trasmissione multiportante con sottoportanti ortogonali

## Definizione · [[ofdm_goldsmith_slides.pdf#page=2|p. 2]], [[ofdm_goldsmith_slides.pdf#page=3|3]], [[ofdm_goldsmith_slides.pdf#page=7|7]], [[ofdm_goldsmith_slides.pdf#page=11|11]]

Un sistema **multiportante** divide il flusso di bit in ingresso, a bit rate $R_b$, in $N$ flussi più lenti, a rate $R_b/N$, e trasmette ciascuno su una frequenza diversa (sottoportante).

- **FDM** (*frequency-division multiplexing*) convenzionale: le bande dei flussi sono **separate**, con bande di guardia tra l'una e l'altra; in ricezione un banco di filtri passa-banda isola ogni flusso.
- **OFDM** (*orthogonal FDM*): le bande delle sottoportanti si **sovrappongono**, ma le forme d'onda sono **ortogonali** sull'intervallo di simbolo $T_u$, quindi si separano con proiezioni ortogonali (un banco di correlatori, realizzato con una FFT).

L'ortogonalità è una proprietà delle forme d'onda **su un intervallo di osservazione finito**, non della non sovrapposizione degli spettri.

Impulsi OFDM (finestra rettangolare di energia unitaria):

$$R_{T_u}(t)=\begin{cases}\dfrac{1}{\sqrt{T_u}}, & 0\le t<T_u\\[4pt] 0 & \text{altrove}\end{cases}\qquad \phi_i(t)=R_{T_u}(t)\,e^{j2\pi it/T_u},\qquad f_i=i\,\Delta f,\quad \Delta f=\frac{1}{T_u}$$

## Formule · [[ofdm_goldsmith_slides.pdf#page=3|p. 3]], [[ofdm_goldsmith_slides.pdf#page=8|8]], [[ofdm_goldsmith_slides.pdf#page=12|12]], [[ofdm_goldsmith_slides.pdf#page=15|15]]–[[ofdm_goldsmith_slides.pdf#page=22|22]]

| Formula | Significato |
|---|---|
| $d_i[n]=d[nN+i]$, $i=0,\dots,N-1$, $R_{b,i}=R_b/N$ | conversione serie/parallelo (segnalazione binaria) |
| $f_n(t)=\sum_{i=0}^{N-1}a_i[n]\,\phi_i(t-nT_u)$, $x(t)=\sum_{n\in\mathbb Z}f_n(t)$ | frame multicanale del blocco $n$ e segnale trasmesso |
| $\langle\phi_k(t-mT_u),\phi_i(t-nT_u)\rangle=\delta_{k-i}\,\delta_{m-n}$ | ortonormalità: nel tempo (blocchi) e in frequenza (sottoportanti) |
| $\langle\phi_k,\phi_i\rangle=e^{j\pi\nu T_u}\,\text{sinc}(\nu T_u)$, $\nu=f_k-f_i$ | prodotto scalare tra due impulsi di frequenza generica |
| $r_i[n]=\int r(t)\,\phi_i^\ast(t-nT_u)\,dt$ | uscita dell'$i$-esimo correlatore |
| $r_i[n]=a_i[n]+w_i[n]$, $w_i[n]\sim\mathcal{CN}(0,N_0)$ | in AWGN ideale: niente ISI né ICI |
| $E\{w_i[n]\,w_k^\ast[m]\}=N_0\,\delta_{i-k}\,\delta_{n-m}$ | campioni di rumore incorrelati, quindi indipendenti |
| $S_{xx}(f)=E_s\sum_{i=0}^{N-1}\text{sinc}^2\big[T_u(f-i/T_u)\big]$ | PSD: somma di sinc² traslate |

Simboli: $a_i[n]$ simbolo (complesso, per esempio QPSK) della sottoportante $i$ nel blocco $n$; $T_u$ durata utile del blocco [s]; $\Delta f$ spaziatura delle sottoportanti [Hz]; $N_0$ PSD bilatera del rumore complesso in banda base [W/Hz]; $E_s=E\{\lvert a_i[n]\rvert^2\}$ energia media dei simboli [J]; $\text{sinc}(u)=\sin(\pi u)/(\pi u)$.

> 🧮 Formula chiave: $\Delta f=1/T_u$ è la spaziatura minima che rende ortogonali le sottoportanti; con l'ortonormalità $r_i[n]=a_i[n]+w_i[n]$.

## Derivazioni

### Derivazione — Conversione serie/parallelo come decomposizione polifase · [[ofdm_goldsmith_slides.pdf#page=3|p. 3]], [[ofdm_goldsmith_slides.pdf#page=4|4]], [[ofdm_goldsmith_slides.pdf#page=9|9]]

**Fonte:** slide 3 e pagine di appunti 4 e 9. **Si parte da:** il flusso seriale $d[\ell]$ a rate $R_b=1/T_b$.

Il convertitore S/P mette il bit $d[nN+i]$ sull'uscita $i$ al passo $n$: è la **decomposizione polifase** del flusso (appunti).

$$
\begin{aligned}
n=0:&\quad d_0(0)=d(0),\ d_1(0)=d(1),\ \dots,\ d_{N-1}(0)=d(N-1) && \text{primo blocco di } N \text{ bit}\\
n=1:&\quad d_0(1)=d(N),\ d_1(1)=d(N+1),\ \dots && \text{secondo istante: blocco successivo}\\
R_{b,i}&=\frac{R_b}{N}=\frac{1}{NT_b} && \text{su ogni uscita esce un bit ogni } N
\end{aligned}
$$

Ogni uscita va al ritmo $R_b/N$ perché bisogna **aspettare che il blocco sia completo** (appunti). Gli impulsi $\phi_i(t-nT_u)$ non durano $T_b$ ma $T_u=NT_b$, l'**intervallo di blocco**: il bit rate su ogni ramo è diminuito.

**Sanity check:** in $T_u=NT_b$ secondi entrano $N$ bit e ne escono $N$ (uno per ramo): il bit rate totale resta $R_b$.
**Ipotesi:** segnalazione binaria (un bit per ramo e per blocco), come nella slide 3. Con un mapper a $b$ bit per simbolo ogni ramo prende $b$ bit per blocco.

### Derivazione — Ortonormalità degli impulsi OFDM · [[ofdm_goldsmith_slides.pdf#page=13|p. 13]], [[ofdm_goldsmith_slides.pdf#page=14|14]], [[ofdm_goldsmith_slides.pdf#page=15|15]]

**Fonte:** slide 10 e appunti di p. 13–14. **Si parte da:** $\phi_i(t)=R_{T_u}(t)e^{j2\pi it/T_u}$.

$$
\begin{aligned}
\langle\phi_k(t-mT_u),\phi_i(t-nT_u)\rangle&=\int_{-\infty}^{+\infty}R_{T_u}(t-mT_u)\,R_{T_u}(t-nT_u)\,e^{j2\pi\frac{k}{T_u}(t-mT_u)}e^{-j2\pi\frac{i}{T_u}(t-nT_u)}dt && \text{definizione}\\
&=0\quad (m\neq n) && \text{le finestre non si sovrappongono nel tempo}\\
m=n:\quad&=\frac{1}{T_u}\int_{nT_u}^{(n+1)T_u}e^{j2\pi\frac{k-i}{T_u}t}\,dt && e^{-j2\pi km}=e^{-j2\pi in}=1\\
&=\frac{1}{T_u}\int_0^{T_u}e^{j2\pi\frac{k-i}{T_u}u}\,du && u=t-nT_u\\
&=\begin{cases}1, & k=i\\[4pt] \dfrac{e^{j2\pi(k-i)}-1}{j2\pi(k-i)}, & k\neq i\end{cases} && \text{integrale dell'esponenziale}\\
&=\delta_{k-i} && k-i\in\mathbb Z\Rightarrow e^{j2\pi(k-i)}=1
\end{aligned}
$$

Quindi $\langle\phi_k(t-mT_u),\phi_i(t-nT_u)\rangle=\delta_{k-i}\,\delta_{m-n}$. Gli appunti di p. 13 chiamano le due condizioni **ortogonalità temporale** ($n=m$) e **ortogonalità fra gli impulsi** ($i=k$).

**Sanity check:** per $k=i$ l'integrale vale $\frac{1}{T_u}\cdot T_u=1$: l'impulso ha energia unitaria, come voluto dal fattore $1/\sqrt{T_u}$.
**Ipotesi:** frequenze esattamente multiple di $1/T_u$; integrazione su un blocco intero. Se una delle due cade, il risultato non è più zero (vedi la derivazione seguente).

### Derivazione — Condizione sinc e spaziatura minima $\Delta f=1/T_u$ · [[ofdm_goldsmith_slides.pdf#page=14|p. 14]], [[ofdm_goldsmith_slides.pdf#page=16|16]]

**Fonte:** slide 11. **Si parte da:** due impulsi alle frequenze generiche $f_k$, $f_i$, con $\nu=f_k-f_i$.

$$
\begin{aligned}
\langle\phi_k,\phi_i\rangle&=\frac{1}{T_u}\int_0^{T_u}e^{j2\pi\nu t}\,dt && \text{stesso blocco}\\
&=\frac{e^{j2\pi\nu T_u}-1}{j2\pi\nu T_u} && \text{primitiva } \tfrac{e^{j2\pi\nu t}}{j2\pi\nu}\\
&=e^{j\pi\nu T_u}\,\frac{e^{j\pi\nu T_u}-e^{-j\pi\nu T_u}}{2j\,\pi\nu T_u} && \text{raccolgo } e^{j\pi\nu T_u}\\
&=e^{j\pi\nu T_u}\,\frac{\sin(\pi\nu T_u)}{\pi\nu T_u}=e^{j\pi\nu T_u}\,\text{sinc}(\nu T_u) && \text{Eulero}
\end{aligned}
$$

La sinc si annulla quando $\nu T_u$ è un intero non nullo: le sottoportanti sono ortogonali se $(f_k-f_i)T_u\in\mathbb Z\setminus\{0\}$. La spaziatura **uniforme più piccola** che lo garantisce è $\Delta f=1/T_u$.

**Numeri:** con $T_u=3.2\ \mu$s (802.11a, slide 46) $\Delta f=1/T_u=312.5$ kHz.
**Sanity check:** per $\nu=0$ si ritrova $\text{sinc}(0)=1$. Se $\nu T_u=0.1$ (errore del 10% della spaziatura), $\lvert\langle\phi_k,\phi_i\rangle\rvert=\text{sinc}(0.1)\approx0.98$: due sottoportanti quasi uguali non sono quasi ortogonali, sono quasi parallele. L'ortogonalità vale solo sui multipli esatti.
**Ipotesi:** stesso intervallo di integrazione $[0,T_u)$ per entrambe.

> 💡 Connessione: gli appunti di p. 14 lo dicono così: **basta una minima variazione della frequenza e si ha ICI**. Per questo l'OFDM non era di uso pubblico: servivano banchi di oscillatori molto precisi. La FFT ha risolto il problema, e oggi l'OFDM è alla base del 5G.

### Derivazione — ISI e ICI nella statistica di decisione · [[ofdm_goldsmith_slides.pdf#page=12|p. 12]], [[ofdm_goldsmith_slides.pdf#page=13|13]], [[ofdm_goldsmith_slides.pdf#page=18|18]]

**Fonte:** slide 9 e 13. **Si parte da:** $r(t)=x(t)+w(t)$ e dal correlatore $r_i[m]=\int r(t)\phi_i^\ast(t-mT_u)dt$, che serve a ricavare il simbolo trasmesso nell'$m$-esimo intervallo sull'$i$-esimo ramo (appunti).

$$
\begin{aligned}
r_i[m]&=\int\Big[\sum_{n\in\mathbb Z}\sum_{k=0}^{N-1}a_k[n]\phi_k(t-nT_u)+w(t)\Big]\phi_i^\ast(t-mT_u)\,dt && \text{sostituisco } x(t)\\
&=\sum_{n\in\mathbb Z}\sum_{k=0}^{N-1}a_k[n]\,\langle\phi_k(t-nT_u),\phi_i(t-mT_u)\rangle+w_i[m] && \text{linearità dell'integrale}\\
&=\underbrace{a_i[m]}_{n=m,\ k=i}+\underbrace{\sum_{n\neq m}\sum_k(\cdot)}_{\text{ISI}}+\underbrace{\sum_{k\neq i}(\cdot)\big|_{n=m}}_{\text{ICI}}+w_i[m] && \text{separo i termini}\\
&=a_i[m]+w_i[m] && \langle\cdot,\cdot\rangle=\delta_{k-i}\delta_{m-n}
\end{aligned}
$$

L'ISI viene dagli altri blocchi dello stesso ramo, l'ICI (*intercarrier interference*) dagli altri rami nello stesso blocco: gli appunti di p. 13 cerchiano $d_1(0)$, che subisce l'interferenza dei simboli dello stesso stream e di fili diversi.

**Ipotesi:** sincronizzazione ideale di tempo e di portante, canale non dispersivo, impulsi di ricezione ortonormali (slide 13).

### Derivazione — Statistica del rumore all'uscita dei correlatori · [[ofdm_goldsmith_slides.pdf#page=18|p. 18]], [[ofdm_goldsmith_slides.pdf#page=19|19]]

**Fonte:** slide 14. **Si parte da:** $w(t)$ gaussiano complesso bianco a media nulla, $E\{w(t)w^\ast(u)\}=N_0\delta(t-u)$.

$$
\begin{aligned}
E\{w_i[n]\}&=\int E\{w(t)\}\,\phi_i^\ast(t-nT_u)\,dt=0 && \text{media nulla}\\
E\{w_i[n]w_k^\ast[m]\}&=\iint E\{w(t)w^\ast(u)\}\,\phi_i^\ast(t-nT_u)\,\phi_k(u-mT_u)\,dt\,du && \text{scambio media e integrali}\\
&=N_0\int\phi_i^\ast(t-nT_u)\,\phi_k(t-mT_u)\,dt && \delta(t-u)\text{ fa sparire l'integrale in } u\\
&=N_0\,\delta_{i-k}\,\delta_{n-m} && \text{ortonormalità}
\end{aligned}
$$

I campioni di rumore sono incorrelati, con la stessa varianza $N_0$; essendo gaussiani (trasformazione lineare di un processo gaussiano) sono anche **indipendenti**: $w_i[n]\sim\mathcal{CN}(0,N_0)$.

**Sanity check:** è lo stesso risultato della Lezione 9 (proiezioni del rumore bianco su una base ortonormale): ogni correlatore vede rumore di varianza pari alla PSD.
**Ipotesi:** rumore bianco; impulsi ortonormali. Se il rumore non è bianco i campioni restano gaussiani ma correlati.

### Derivazione — Autocorrelazione e PSD del segnale OFDM · [[ofdm_goldsmith_slides.pdf#page=20|p. 20]], [[ofdm_goldsmith_slides.pdf#page=21|21]]

**Fonte:** slide 15–16. **Si parte da:** simboli indipendenti a media nulla, $E\{a_i[n]a_k^\ast[m]\}=E_s\delta_{i-k}\delta_{n-m}$.

$$
\begin{aligned}
R_{xx}(t,\tau)&=E\{x(t)x^\ast(t-\tau)\} && \text{definizione}\\
&=\sum_{n,m}\sum_{i,k}E\{a_i[n]a_k^\ast[m]\}\,\phi_i(t-nT_u)\,\phi_k^\ast(t-\tau-mT_u) && \text{linearità della media}\\
&=E_s\sum_{n\in\mathbb Z}\sum_{i=0}^{N-1}\phi_i(t-nT_u)\,\phi_i^\ast(t-\tau-nT_u) && \text{restano } i=k,\ n=m\\
R_{xx}(t+T_u,\tau)&=R_{xx}(t,\tau) && n\to n+1 \text{ nella somma: ciclostazionario}\\
\bar R_{xx}(\tau)&=\frac{1}{T_u}\int_0^{T_u}R_{xx}(t,\tau)\,dt=\frac{E_s}{T_u}\sum_i\sum_n\int_{-nT_u}^{(1-n)T_u}\phi_i(u)\phi_i^\ast(u-\tau)\,du && u=t-nT_u\\
&=\frac{E_s}{T_u}\sum_{i=0}^{N-1}\int_{-\infty}^{+\infty}\phi_i(u)\phi_i^\ast(u-\tau)\,du=\frac{E_s}{T_u}\sum_iR_{\phi_i\phi_i}(\tau) && \text{gli intervalli coprono tutta la retta}\\
\Phi_0(f)&=\frac{1}{\sqrt{T_u}}\int_0^{T_u}e^{-j2\pi ft}dt=\sqrt{T_u}\,e^{-j\pi fT_u}\,\text{sinc}(fT_u) && \text{trasformata della finestra}\\
\Phi_i(f)&=\Phi_0(f-i/T_u)\ \Rightarrow\ \lvert\Phi_i(f)\rvert^2=T_u\,\text{sinc}^2\big[T_u(f-i/T_u)\big] && \text{modulazione} = \text{traslazione}\\
S_{xx}(f)&=\frac{E_s}{T_u}\sum_i\lvert\Phi_i(f)\rvert^2=E_s\sum_{i=0}^{N-1}\text{sinc}^2\Big[T_u\Big(f-\frac{i}{T_u}\Big)\Big] && \text{Wiener-Khinchin}
\end{aligned}
$$

**Sanity check:** potenza $=\int S_{xx}df=E_s\sum_i\frac{1}{T_u}=NE_s/T_u$: $N$ simboli di energia $E_s$ ogni $T_u$ secondi. Corretto.
**Ipotesi:** simboli indipendenti e a media nulla. Le sottoportanti si sovrappongono in frequenza, ma con simboli indipendenti le loro PSD **si sommano** e basta.

![[grafico-l15-psd-ofdm.png|680]]

*🧩 La PSD della slide 16 per $N=8$ (script `output/grafici/genera_grafici_lezione15.py`). Ogni tratteggiata è la $\text{sinc}^2$ di una sottoportante, centrata in $i/T_u$; nel picco di ciascuna tutte le altre passano per zero. La somma (nera) è quasi piatta su circa $N/T_u$, con un'ondulazione di circa il 5% e lobi laterali fuori banda dovuti alla finestra rettangolare.*

### Derivazione — Risparmio di banda con la sovrapposizione (esempio) · [[ofdm_goldsmith_slides.pdf#page=22|p. 22]]

**Fonte:** slide 17, risultato dato. **Si parte da:** $N$ sottocanali con tempo di simbolo $T_u$, impulsi a coseno rialzato con roll-off $\beta$ (Lezione 14), più un margine $\varepsilon$ ai bordi.

$$
\begin{aligned}
B_{\text{sottocanale}}&=\frac{1+\beta}{T_u} && \text{coseno rialzato in banda passante: } 2\cdot\tfrac{1+\beta}{2T_u}\\
B_{FDM}&\simeq N\,\frac{1+\beta+\varepsilon}{T_u} && N \text{ bande separate, ognuna col suo margine}\\
B_{overlap}&\simeq\frac{N}{T_u}+\frac{\beta+\varepsilon}{T_u}=\frac{N+\beta+\varepsilon}{T_u} && \text{portanti a } 1/T_u\text{; il bordo si conta una volta}
\end{aligned}
$$

**Numeri:** $N=128$, $T_u=0.2$ ms, $\beta=1$, $\varepsilon=0.1$:
$B_{FDM}=128\cdot2.1/(2\cdot10^{-4}\,\text{s})=1.344$ MHz; $B_{overlap}=129.1/(2\cdot10^{-4}\,\text{s})=645.5$ kHz $\approx0.646$ MHz.
**Sanity check:** $0.646/1.344\approx0.48$: la sovrapposizione dimezza circa la banda. Il guadagno viene tutto dal roll-off: con $\beta=\varepsilon=0$ le due formule coinciderebbero.
**Ipotesi:** confronto illustrativo (Goldsmith, esempi 12.2–12.3), non una formula esatta di banda occupata: l'OFDM a finestra rettangolare ha lobi laterali sinc.

## Spiegazione · [[ofdm_goldsmith_slides.pdf#page=2|p. 2]]–[[ofdm_goldsmith_slides.pdf#page=12|12]], [[ofdm_goldsmith_slides.pdf#page=17|17]], [[ofdm_goldsmith_slides.pdf#page=18|18]]

- **Perché multiportante.** Nella Lezione 14 il canale a banda limitata con memoria era una convoluzione, e i contributi di simboli diversi si sovrapponevano (ISI). Gli appunti di p. 9 spiegano il trucco: se $R_b$ è alto il segnale varia rapidamente, la banda trasmessa cresce e l'ISI aumenta. Con la S/P ogni ramo ha un rate $R_b/N$ più basso, quindi banda minore: il sistema è "rallentato" e lotta meglio con l'ISI.
- **Il canale visto da una sottoportante.** Gli appunti di p. 10 lo disegnano: un segnale a portante singola occupa tutta la banda del canale e ne vede la risposta non piatta; spezzato in tante sottoportanti strette, su ciascuna il canale è **approssimabile piatto**, quindi più robustezza all'ISI.
- **FDM.** Trasmettitore (slide 4): S/P, per ogni ramo un mapper, un impulso $g(t)$ e un esponenziale $e^{j2\pi f_it}$; i rami si sommano in $x(t)$, il **segnale multiportante in banda base**. Le $f_i$ non sono ancora la portante finale: poi l'upconverter trasla tutto alla radiofrequenza (appunti). Nella FDM l'ortogonalità è garantita dalla non sovrapposizione; ricevitore (slide 5) = **banco di filtri** passa-banda, un demodulatore per ramo, P/S.
- **OFDM.** Le bande si sovrappongono, quindi la demodulazione è più difficile (appunti p. 5): serve una forma di ortogonalità **che agisca anche nel dominio del tempo** (appunti p. 7), cioè impulsi di forma particolare (appunti p. 11: "devo imporre una biortogonalità"). Le frequenze $f_i=i/T_u$ non sono quelle finali: si passa ancora per l'upconverter.
- **Impulsi diversi per ramo.** Nella slide 7 ogni ramo ha il suo $\phi_i(t)$: in generale possono essere diversi, e in alcuni casi non si può proprio usare lo stesso impulso di base (appunti). $f_n(t)$ è la **frame multicanale**, cioè quella prodotta nell'$n$-esimo intervallo di simbolo.
- **Due ortogonalità.** Sottoportanti diverse ($i\neq k$) sono ortogonali *dentro* un blocco; blocchi diversi ($n\neq m$) non si sovrappongono nel tempo (modello ideale senza prefisso ciclico, slide 8).
- **Ricevitore.** Un banco di $N$ correlatori, ciascuno moltiplica per $\phi_i^\ast(t-nT_u)$ e integra (slide 12): un solo calcolo estrae l'$i$-esimo simbolo, a meno del rumore, se il canale non distorce. Nella slide 5 la prof sottolinea che l'OFDM sostituisce i filtri con un **banco di proiezioni ortogonali, realizzato con una FFT** ([[ofdm-con-fft]]).

> 🎯 Esame: saper scrivere $\phi_i(t)$, dimostrare l'ortonormalità con l'integrale dell'esponenziale, dire perché $\Delta f=1/T_u$ è la spaziatura minima, e distinguere ISI (altri blocchi) e ICI (altre sottoportanti).

## Perché importa · [[ofdm_goldsmith_slides.pdf#page=2|p. 2]], [[ofdm_goldsmith_slides.pdf#page=6|6]], [[ofdm_goldsmith_slides.pdf#page=14|14]]

L'OFDM è il terzo modo di trattare l'ISI della Lezione 14, dopo equalizzatori e MLSE: invece di correggere l'ISI, la rende trascurabile su ogni sottoportante e la elimina del tutto con il [[prefisso-ciclico]]. È la base di Wi-Fi ([[ieee-802-11a]]) e del 5G (appunti di p. 14).

## Connessioni

- [[interferenza-intersimbolica]] — l'OFDM nasce per combatterla: rate più basso per ramo, canale piatto per sottoportante.
- [[criterio-di-nyquist]] e [[modulazione-ortogonale]] — l'ortogonalità tra le $\phi_i$ è la stessa idea della FSK ortogonale (Lezione 8), con spaziatura minima $1/T_u$ per segnali complessi in banda base.
- [[ricevitore-ottimo-awgn]] — il banco di correlatori è il ricevitore ottimo per una base ortonormale; il rumore sulle uscite è i.i.d. come nella Lezione 9.
- [[densita-spettrale-di-potenza]] — la PSD si ricava mediando un'autocorrelazione ciclostazionaria, come per i segnali modulati della Lezione 8.
- [[prefisso-ciclico]] — che cosa succede quando il canale è dispersivo.
- [[ofdm-con-fft]] — il banco di modulatori e correlatori diventa una IFFT e una FFT.
- [[limiti-dell-ofdm]] — la stessa ortogonalità esatta rende l'OFDM sensibile agli errori di frequenza.

> 📚 Approfondimento (non d'esame): [[multiportante-ofdm-dmt-gelli]] — le note di G. Gelli ricavano gli stessi risultati con il blocco $T$ al posto di $T_u$ e aggiungono le prestazioni QAM per sottoportante e il bit loading.

## Fonti · [[ofdm_goldsmith_slides.pdf#page=2|p. 2]]–[[ofdm_goldsmith_slides.pdf#page=22|22]]

- [[signaling-ofdm]] — Lezione 15, slide 2–17 e pagine di appunti 4, 9, 10, 13, 14.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15, ofdm_goldsmith_slides.pdf)_
