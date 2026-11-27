---
tipo: concetto
importanza_esame: alta
prerequisiti: ["ofdm", "processi-e-sistemi-lti", "interferenza-intersimbolica"]
fonti_pdf: ["ofdm_goldsmith_slides.pdf#page=23", "ofdm_goldsmith_slides.pdf#page=24", "ofdm_goldsmith_slides.pdf#page=25", "ofdm_goldsmith_slides.pdf#page=26", "ofdm_goldsmith_slides.pdf#page=27", "ofdm_goldsmith_slides.pdf#page=28", "ofdm_goldsmith_slides.pdf#page=29", "ofdm_goldsmith_slides.pdf#page=30", "ofdm_goldsmith_slides.pdf#page=31", "ofdm_goldsmith_slides.pdf#page=32", "ofdm_goldsmith_slides.pdf#page=36", "ofdm_goldsmith_slides.pdf#page=37", "ofdm_goldsmith_slides.pdf#page=38", "ofdm_goldsmith_slides.pdf#page=39", "ofdm_goldsmith_slides.pdf#page=40", "ofdm_goldsmith_slides.pdf#page=48", "ofdm_goldsmith_slides.pdf#page=49", "ofdm_goldsmith_slides.pdf#page=50"]
---

# Prefisso ciclico e convoluzione circolare

## Definizione · [[ofdm_goldsmith_slides.pdf#page=23|p. 23]], [[ofdm_goldsmith_slides.pdf#page=24|24]], [[ofdm_goldsmith_slides.pdf#page=26|26]], [[ofdm_goldsmith_slides.pdf#page=36|36]]

Un canale LTI dispersivo con risposta impulsiva $h(\tau)$ non nulla per $0\le\tau\le T_h$ fa "sbordare" la coda di ogni blocco OFDM nel blocco successivo: è ISI tra blocchi, e i termini ritardati rovinano anche l'ortogonalità tra le sottoportanti.

Si allunga allora ogni blocco a $T=T_u+T_g$, dove $T_g$ è l'**intervallo di guardia**. Un intervallo di guardia **vuoto** evita la sovrapposizione tra blocchi vicini, ma in generale non ripristina l'ortogonalità delle sottoportanti ritardate sulla finestra FFT lunga $T_u$. Si riempie invece $T_g$ con la **copia degli ultimi $T_g$ secondi** del blocco utile, messa davanti: è il **prefisso ciclico** (*cyclic prefix*, CP).

In ricezione si scarta il prefisso e si demodulano esattamente $T_u$ secondi. Se

$$T_g\ge T_h\qquad(\text{a tempo discreto } L_{cp}\ge L_h)$$

la finestra osservata contiene solo il blocco corrente (niente ISI) e il canale agisce come una **convoluzione circolare**, che la DFT trasforma in un prodotto: ogni sottoportante esce moltiplicata per un solo coefficiente complesso (niente ICI).

## Formule · [[ofdm_goldsmith_slides.pdf#page=25|p. 25]]–[[ofdm_goldsmith_slides.pdf#page=32|32]], [[ofdm_goldsmith_slides.pdf#page=36|36]]–[[ofdm_goldsmith_slides.pdf#page=40|40]], [[ofdm_goldsmith_slides.pdf#page=48|48]]–[[ofdm_goldsmith_slides.pdf#page=50|50]]

| Formula | Significato |
|---|---|
| $r(t)=\int_0^{T_h}h(\tau)x(t-\tau)\,d\tau+w(t)$ | canale LTI causale di memoria $T_h$ |
| $f_n(t)=\frac{1}{\sqrt{T_u}}\sum_{i=0}^{N-1}a_i[n]e^{j2\pi it/T_u}$, $0\le t<T_u$ | blocco utile |
| $\tilde f_n(t)=f_n(t\bmod T_u)$, $-T_g\le t<T_u$ | blocco esteso ciclicamente |
| $x_{cp}(t)=\sum_n\tilde f_n(t-nT-T_g)$, $T=T_u+T_g$ | segnale trasmesso con CP |
| $h(t)\ast e^{j2\pi ft}=H(f)\,e^{j2\pi ft}$ | l'esponenziale è autofunzione di un sistema LTI |
| $r_i[n]=H(i/T_u)\,a_i[n]+w_i[n]$ | dopo la rimozione del CP: niente ISI né ICI |
| $\tilde x_n[q]=x_n[q\bmod N]$, $q=-L_{cp},\dots,N-1$, $P=N+L_{cp}$, $T_g=L_{cp}T_c$ | CP a tempo discreto |
| $y_n[q]=\sum_{\ell=0}^{L_h}h[\ell]\,x_n[(q-\ell)\bmod N]+w_n[q]$ | convoluzione circolare su $N$ punti |
| $Y_n[k]=H[k]\,a_k[n]+W_n[k]$, $H[k]=\sum_{\ell}h[\ell]e^{-j2\pi k\ell/N}$ | relazione ingresso-uscita in frequenza |
| $\eta_{cp}=\frac{N}{N+L_{cp}}=\frac{T_u}{T_u+T_g}$ | frazione di campioni utili |
| $R_b=\frac{N_d\log_2M}{T_u+T_g}=\frac{N_d\log_2M}{T_u}\cdot\frac{N}{N+L_{cp}}$ | bit rate non codificato con $N_d$ portanti dati |

Simboli: $T_h$ memoria del canale [s]; $T_g$ durata del prefisso [s]; $T_c=T_u/N$ periodo di campionamento [s]; $L_h$ indice dell'ultimo tap del canale campionato ($h[\ell]=0$ per $\ell\notin\{0,\dots,L_h\}$); $L_{cp}$ campioni di prefisso; $P$ campioni trasmessi per blocco; $N_d$ sottoportanti che portano dati; $M$ ordine della costellazione.

> 🧮 Formula chiave: con $T_g\ge T_h$ (cioè $L_{cp}\ge L_h$) vale $Y_n[k]=H[k]a_k[n]+W_n[k]$.

## Derivazioni

### Derivazione — Il CP isola il blocco: la condizione $T_g\ge T_h$ · [[ofdm_goldsmith_slides.pdf#page=25|p. 25]], [[ofdm_goldsmith_slides.pdf#page=26|26]], [[ofdm_goldsmith_slides.pdf#page=27|27]], [[ofdm_goldsmith_slides.pdf#page=28|28]]

**Fonte:** slide 20–23. **Si parte da:** il blocco $n$ occupa $nT\le t<(n+1)T$: il CP in $[nT,nT+T_g)$, la parte utile in $[nT+T_g,(n+1)T)$. Il ricevitore osserva $t=nT+T_g+u$, $0\le u<T_u$.

$$
\begin{aligned}
x_{cp}(t)&=\tilde f_n(t-nT-T_g) && \text{per } nT\le t<(n+1)T:\ t-nT-T_g\in[-T_g,T_u)\\
t-\tau&=nT+T_g+u-\tau && \text{argomento dentro la convoluzione}\\
&\ge nT+T_g-T_h\ \ge\ nT && u\ge0,\ \tau\le T_h,\ T_g\ge T_h\\
&<nT+T_g+T_u=(n+1)T && \tau\ge0,\ u<T_u\\
y_n(u)&=\int_0^{T_h}h(\tau)\,x_{cp}(nT+T_g+u-\tau)\,d\tau+w_n(u) && \text{tutto il ritardato appartiene al blocco } n\\
&=\int_0^{T_h}h(\tau)\,f_n\big((u-\tau)\bmod T_u\big)\,d\tau+w_n(u) && x_{cp}=\tilde f_n(u-\tau),\ u-\tau\in[-T_g,T_u)
\end{aligned}
$$

I contributi di $a_i[n-1]$ spariscono: **niente ISI tra blocchi**. Il CP deve coprire la **memoria del canale**, non una frazione arbitraria del tempo di simbolo (slide 22).

**Sanity check:** se fosse $T_g<T_h$, per $u$ piccolo e $\tau$ vicino a $T_h$ si avrebbe $t-\tau<nT$, cioè un campione del blocco $n-1$ dentro la finestra: è esattamente l'ISI della figura di slide 18.
**Ipotesi:** canale LTI causale di durata $T_h$; finestra FFT che inizia esattamente a $nT+T_g$.

### Derivazione — Perché sparisce anche l'ICI (tempo continuo) · [[ofdm_goldsmith_slides.pdf#page=29|p. 29]], [[ofdm_goldsmith_slides.pdf#page=30|30]]

**Fonte:** slide 24–25. **Si parte da:** l'esponenziale complesso è autofunzione di un sistema LTI, $h(t)\ast e^{j2\pi ft}=H(f)e^{j2\pi ft}$, e dall'espressione di $y_n(u)$ appena trovata.

$$
\begin{aligned}
f_n\big((u-\tau)\bmod T_u\big)&=\frac{1}{\sqrt{T_u}}\sum_ka_k[n]\,e^{j2\pi k(u-\tau)/T_u} && k\text{ intero: l'esponenziale è } T_u\text{-periodico, il mod si toglie}\\
\int_0^{T_h}h(\tau)e^{j2\pi k(u-\tau)/T_u}d\tau&=e^{j2\pi ku/T_u}\int_0^{T_h}h(\tau)e^{-j2\pi k\tau/T_u}d\tau=H\Big(\frac{k}{T_u}\Big)e^{j2\pi ku/T_u} && h=0\text{ fuori da }[0,T_h]\\
y_n(u)&=\frac{1}{\sqrt{T_u}}\sum_{k=0}^{N-1}a_k[n]\,H\Big(\frac{k}{T_u}\Big)e^{j2\pi ku/T_u}+w_n(u) && \text{linearità}\\
r_i[n]&=\frac{1}{\sqrt{T_u}}\int_0^{T_u}y_n(u)\,e^{-j2\pi iu/T_u}\,du && \text{proiezione sulla sottoportante } i\\
&=\sum_ka_k[n]H\Big(\frac{k}{T_u}\Big)\underbrace{\frac{1}{T_u}\int_0^{T_u}e^{j2\pi(k-i)u/T_u}du}_{\delta_{k-i}}+w_i[n] && \text{ortonormalità su } T_u\\
&=H\Big(\frac{i}{T_u}\Big)a_i[n]+w_i[n] && \text{niente ICI}
\end{aligned}
$$

Grazie al CP, nell'intervallo utile ogni sottoportante è **esattamente** una sinusoide complessa (non una sinusoide troncata), quindi il canale la moltiplica soltanto per il numero complesso $H(k/T_u)$.

**Sanity check:** canale ideale $h(\tau)=\delta(\tau)$ ⇒ $H(f)=1$ ⇒ si ritrova $r_i[n]=a_i[n]+w_i[n]$ della slide 13.
**Ipotesi:** $T_g\ge T_h$; canale LTI per tutta la trasmissione; sincronizzazione ideale.

### Derivazione — Nota sulla normalizzazione degli impulsi · [[ofdm_goldsmith_slides.pdf#page=31|p. 31]]

**Fonte:** slide 26. Negli appunti a mano della lezione gli impulsi possono essere normalizzati sulla durata **completa** del blocco $T=T_u+T_g$ invece che su $T_u$. Con ampiezza $1/\sqrt T$ in trasmissione e in ricezione:

$$
\begin{aligned}
\frac{1}{T}\int_0^{T_u}e^{j2\pi(k-i)u/T_u}du&=\frac{T_u}{T}\,\delta_{k-i} && \text{l'integrale vale } T_u\text{ se }k=i\\
r_i[n]&=\frac{T_u}{T}\,H\Big(\frac{i}{T_u}\Big)a_i[n]+w_i[n] && \text{stessa derivazione}
\end{aligned}
$$

Nella derivazione della slide gli impulsi utili hanno energia unitaria su $T_u$ e il fattore vale 1: le due formule differiscono solo per la normalizzazione, non per la proprietà OFDM. Il fattore $T_u/T<1$ ricorda che l'energia spesa nel prefisso non arriva al decisore.

### Derivazione — Esempio numerico di inserimento del CP · [[ofdm_goldsmith_slides.pdf#page=36|p. 36]], [[ofdm_goldsmith_slides.pdf#page=37|37]]

**Fonte:** slide 31–32. Con $N=8$ e $L_{cp}=3$ la sequenza utile è $x[0],\dots,x[7]$. Si copiano gli ultimi tre campioni all'inizio:

$$x[5],x[6],x[7],\ x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]$$

cioè $\tilde x[q]=x[(q)_8]$ con $(q)_8=q\bmod 8$, $q=-3,\dots,7$: per esempio $\tilde x[-3]=x[5]$ perché $-3+8=5$. Il blocco trasmesso ha $P=N+L_{cp}=11$ campioni; il ricevitore scarta i primi 3 e tiene gli 8 successivi.

### Derivazione — Da convoluzione lineare a circolare (tempo discreto) · [[ofdm_goldsmith_slides.pdf#page=38|p. 38]]

**Fonte:** slide 33. **Si parte da:** canale campionato con $h[\ell]=0$ per $\ell\notin\{0,1,\dots,L_h\}$ e $L_{cp}\ge L_h$.

$$
\begin{aligned}
y_n[q]&=\sum_{\ell=0}^{L_h}h[\ell]\,\tilde x_n[q-\ell]+w_n[q],\quad q=0,\dots,N-1 && \text{convoluzione lineare, dopo aver tolto il CP}\\
q-\ell&\ge0-L_h\ge-L_{cp} && \text{l'indice resta dentro il blocco esteso}\\
y_n[q]&=\sum_{\ell=0}^{L_h}h[\ell]\,x_n[(q-\ell)\bmod N]+w_n[q] && \tilde x_n[q]=x_n[q\bmod N]
\end{aligned}
$$

Il canale fisico fa una convoluzione **lineare**; estensione ciclica e rimozione del CP fanno sì che gli $N$ campioni utili in uscita siano una convoluzione **circolare** su $N$ punti.

**Sanity check:** per $q\ge L_h$ non serve il prefisso ($q-\ell\ge0$); il prefisso lavora solo per i primi $L_h$ campioni, quelli che altrimenti "pescherebbero" nel blocco precedente.

### Derivazione — Teorema della convoluzione circolare e relazione in frequenza · [[ofdm_goldsmith_slides.pdf#page=39|p. 39]], [[ofdm_goldsmith_slides.pdf#page=40|40]]

**Fonte:** slide 34–35. **Si parte da:** DFT unitaria $Y[k]=\frac{1}{\sqrt N}\sum_qy[q]e^{-j2\pi kq/N}$ (vedi [[ofdm-con-fft]]).

$$
\begin{aligned}
Y_n[k]&=\frac{1}{\sqrt N}\sum_{q=0}^{N-1}\sum_{\ell=0}^{L_h}h[\ell]\,x_n[(q-\ell)\bmod N]\,e^{-j2\pi kq/N}+W_n[k] && \text{DFT della convoluzione circolare}\\
&=\sum_{\ell=0}^{L_h}h[\ell]\,\frac{1}{\sqrt N}\sum_{q=0}^{N-1}x_n[(q-\ell)\bmod N]\,e^{-j2\pi kq/N}+W_n[k] && \text{scambio le somme}\\
&=\sum_{\ell}h[\ell]\,e^{-j2\pi k\ell/N}\,\frac{1}{\sqrt N}\sum_{p=0}^{N-1}x_n[p]\,e^{-j2\pi kp/N}+W_n[k] && p=(q-\ell)\bmod N:\ e^{-j2\pi kq/N}=e^{-j2\pi k(p+\ell)/N}\\
&=H[k]\,a_k[n]+W_n[k] && \text{la DFT di } x_n \text{ è } a_n,\ H[k]=\textstyle\sum_\ell h[\ell]e^{-j2\pi k\ell/N}
\end{aligned}
$$

Il passaggio chiave è il terzo: l'esponenziale ha periodo $N$ in $q$, quindi $q$ e $p+\ell$ danno lo stesso valore, e quando $q$ percorre $0,\dots,N-1$ anche $p$ percorre tutti i resti. La DFT del canale $H[k]$ è **non unitaria** (senza $1/\sqrt N$).

**Sanity check:** $H[k]$ è la risposta in frequenza del canale campionato in $f_k=k/T_u$: la controparte discreta di $H(k/T_u)$ trovata a tempo continuo. Il canale non mescola mai valori diversi di $k$.
**Ipotesi:** $L_{cp}\ge L_h$, $L_h<N$, canale LTI, sincronizzazione ideale.

### Derivazione — Prezzo del CP e bit rate · [[ofdm_goldsmith_slides.pdf#page=48|p. 48]], [[ofdm_goldsmith_slides.pdf#page=49|49]], [[ofdm_goldsmith_slides.pdf#page=50|50]]

**Fonte:** slide 43–45. **Si parte da:** $N$ campioni utili richiedono $P=N+L_{cp}$ campioni trasmessi.

$$
\begin{aligned}
\eta_{cp}&=\frac{N}{N+L_{cp}}=\frac{NT_c}{NT_c+L_{cp}T_c}=\frac{T_u}{T_u+T_g} && T_u=NT_c,\ T_g=L_{cp}T_c\\
N_b&=N_d\log_2M && \text{bit non codificati per blocco}\\
R_b&=\frac{N_d\log_2M}{T_u+T_g}=\frac{N_d\log_2M}{T_u}\cdot\frac{T_u}{T_u+T_g}=\frac{N_d\log_2M}{T_u}\cdot\frac{N}{N+L_{cp}} && \text{un simbolo OFDM dura } T_u+T_g
\end{aligned}
$$

**Numeri (Goldsmith, esempio 12.4):** $T_c=1\ \mu$s, memoria massima del canale $5\ \mu$s, $N=128$, $L_{cp}=8$:
$T_u=128\ \mu$s, $T_g=8\ \mu$s $>5\ \mu$s, $T=136\ \mu$s, $\eta_{cp}=128/136\approx94.1\%$; con tutti i 128 toni in 16-QAM non codificata $R_b=128\cdot4/136\ \mu\text{s}=512/(1.36\cdot10^{-4}\ \text{s})\approx3.76$ Mbit/s.
**Sanity check:** senza CP sarebbe $512/128\ \mu\text{s}=4$ Mbit/s; il CP toglie il $5.9\%$, cioè $L_{cp}/P=8/136$.
**Ipotesi:** il rate netto si riduce ancora per portanti riservate (pilota, guardie spettrali) e per il tasso del codice correttore.

L'overhead del CP è **in tempo e in energia trasmessa**, non nel numero di sottoportanti che portano informazione.

## Spiegazione · [[ofdm_goldsmith_slides.pdf#page=23|p. 23]], [[ofdm_goldsmith_slides.pdf#page=24|24]], [[ofdm_goldsmith_slides.pdf#page=26|26]], [[ofdm_goldsmith_slides.pdf#page=29|29]], [[ofdm_goldsmith_slides.pdf#page=38|38]], [[ofdm_goldsmith_slides.pdf#page=48|48]]

- **Il problema.** Un canale con memoria $T_h$ "spalma" ogni blocco per $T_h$ secondi: la coda del blocco $n$ cade nel blocco $n+1$ (figura di slide 18). Ma c'è un danno peggiore: dentro la finestra di un blocco, una sottoportante ritardata è una sinusoide **troncata** (accesa a metà finestra), e una sinusoide troncata non è più ortogonale alle altre.
- **Perché non basta una guardia vuota.** La guardia vuota risolve la sovrapposizione tra blocchi, ma il ritardato del blocco corrente resta troncato sulla finestra di $T_u$ secondi: l'ICI rimane.
- **Perché la copia della coda funziona.** Le sottoportanti hanno periodo $T_u$ (l'indice $i$ è intero), quindi il prefisso è una vera estensione periodica. Qualunque ritardo $\tau\le T_g$ fa entrare nella finestra la coda copiata, che è la continuazione esatta della sinusoide: nella finestra si vede sempre un periodo intero di ogni sottoportante, e il canale la moltiplica soltanto per $H(k/T_u)$.
- **A tempo discreto** lo stesso fatto si chiama convoluzione circolare, e la DFT diagonalizza la convoluzione circolare: il sistema diventa $N$ canali scalari indipendenti ([[equalizzazione-ofdm]]).

> 🎯 Esame: spiegare a parole e con la condizione $T_g\ge T_h$ perché il CP elimina l'ISI e l'ICI; scrivere $Y_n[k]=H[k]a_k[n]+W_n[k]$ e dire quanto costa il CP ($\eta_{cp}$).

## Perché importa · [[ofdm_goldsmith_slides.pdf#page=26|p. 26]], [[ofdm_goldsmith_slides.pdf#page=36|36]]

Il CP è ciò che rende l'OFDM robusto ai canali dispersivi senza un equalizzatore complicato: al posto di un equalizzatore a più prese o della MLSE della Lezione 14 basta una divisione per sottoportante. In cambio si paga una frazione $L_{cp}/(N+L_{cp})$ di tempo e di energia.

## Connessioni

- [[ofdm]] — l'ortogonalità che il CP preserva.
- [[processi-e-sistemi-lti]] — autofunzioni esponenziali di un sistema LTI: è la proprietà che fa sparire l'ICI.
- [[interferenza-intersimbolica]] — il CP la elimina tra blocchi purché copra la memoria del canale.
- [[ofdm-con-fft]] — convoluzione circolare e DFT.
- [[equalizzazione-ofdm]] — cosa si fa con $Y_n[k]=H[k]a_k[n]+W_n[k]$.
- [[ieee-802-11a]] — un CP reale: $L_{cp}=16$ su $N=64$.

> 📚 Approfondimento (non d'esame): [[multiportante-ofdm-dmt-gelli]] — tempi di guardia e prefisso ciclico ricavati con il blocco normalizzato su $T$, da cui il fattore $T_u/T$ della slide 26.

## Fonti · [[ofdm_goldsmith_slides.pdf#page=23|p. 23]]–[[ofdm_goldsmith_slides.pdf#page=32|32]], [[ofdm_goldsmith_slides.pdf#page=36|36]]–[[ofdm_goldsmith_slides.pdf#page=40|40]], [[ofdm_goldsmith_slides.pdf#page=48|48]]–[[ofdm_goldsmith_slides.pdf#page=50|50]]

- [[signaling-ofdm]] — Lezione 15, slide 18–27, 31–35, 43–45.

_Aggiornato: 2026-11-27 — creazione (ingest della Lezione 15, ofdm_goldsmith_slides.pdf)_
