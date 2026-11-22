---
tipo: concetto
importanza_esame: alta
prerequisiti: ["informazione-mutua-e-capacita", "parametri-globali-modulazioni"]
fonti_pdf: ["Confronto_new.pdf#page=20", "Confronto_new.pdf#page=21", "Confronto_new.pdf#page=22", "Confronto_new.pdf#page=23"]
---

# Limite di Shannon

## Definizione · [[Confronto_new.pdf#page=20|p. 20]], [[Confronto_new.pdf#page=21|21]]

La **frontiera di Shannon** è la curva del piano $(\eta_B,E_b/N_0)$ che dà, per ogni efficienza spettrale $\eta_B$, il **minimo** $E_b/N_0$ con cui si può trasmettere sul canale AWGN con probabilità d'errore piccola a piacere. Si ottiene imponendo $R_b\le C$. Ogni sistema reale deve stare **sopra** la curva (a destra, nel grafico con $E_b/N_0$ in ascissa). Per $\eta_B\to0$ il minimo assoluto è $E_b/N_0=\ln2\approx-1.59$ dB.

## Formule · [[Confronto_new.pdf#page=20|p. 20]], [[Confronto_new.pdf#page=21|21]]

| Formula | Significato |
|---|---|
| $\gamma=\frac{E_b}{N_0}\eta_B$ | SNR scritto con i parametri globali |
| $\eta_B\le\log_2\big(1+\eta_B\frac{E_b}{N_0}\big)$ | condizione $R_b\le C$ divisa per $W$ |
| $\frac{E_b}{N_0}\ge\frac{2^{\eta_B}-1}{\eta_B}$ | frontiera di Shannon |
| $\big(\frac{E_b}{N_0}\big)_{min}=\ln2\approx-1.59$ dB | limite per $\eta_B\to0$ |

> 🧮 Formula chiave: $\dfrac{E_b}{N_0}\ge\dfrac{2^{\eta_B}-1}{\eta_B}$, e per $\eta_B\to0$ il minimo è $\ln2=-1.59$ dB.

Simboli: $\eta_B=R_b/W$ [bit/s/Hz] efficienza spettrale; $E_b/N_0$ adimensionale (si esprime in dB); $C=W\log_2(1+\gamma)$ capacità AWGN.

## Derivazioni

### Derivazione — Frontiera di Shannon · [[Confronto_new.pdf#page=20|p. 20]]
**Fonte:** slide 20, passaggi indicati senza esplicitare l'inversione.
**Si parte da:** $C=W\log_2(1+\gamma)$ ([[informazione-mutua-e-capacita]]) e $\gamma=\frac{E_b}{N_0}\eta_B$ ([[parametri-globali-modulazioni]]).

$$
\begin{aligned}
R_b&\le C=W\log_2(1+\gamma) && \text{condizione necessaria (secondo teorema di Shannon)}\\
\eta_B=\frac{R_b}{W}&\le\log_2(1+\gamma) && \text{divido per } W>0\\
\eta_B&\le\log_2\Big(1+\eta_B\frac{E_b}{N_0}\Big) && \gamma=\tfrac{E_b}{N_0}\eta_B\\
2^{\eta_B}&\le1+\eta_B\frac{E_b}{N_0} && 2^{(\cdot)}\ \text{è crescente: il verso resta}\\
\frac{E_b}{N_0}&\ge\frac{2^{\eta_B}-1}{\eta_B} && \text{sottraggo 1 e divido per } \eta_B>0
\end{aligned}
$$

**Numeri** (calcolati dalla formula):

| $\eta_B$ [bit/s/Hz] | $\frac{2^{\eta_B}-1}{\eta_B}$ | $E_b/N_0$ minimo [dB] |
|---|---|---|
| $\to0$ | $\ln2=0.693$ | $-1.59$ |
| 0.5 | 0.828 | $-0.82$ |
| 1 | 1 | 0 |
| 2 | 1.5 | 1.76 |
| 4 | 3.75 | 5.74 |
| 8 | 31.9 | 15.0 |

**Sanity check:** la curva è crescente: più bit/s/Hz richiedono più energia per bit. Per $\eta_B$ grande cresce circa come $2^{\eta_B}/\eta_B$: ogni bit/s/Hz in più costa quasi 3 dB.
**Ipotesi:** canale AWGN, nessun vincolo di complessità o ritardo (codici ideali).

### Derivazione — Il limite di $-1.59$ dB · [[Confronto_new.pdf#page=21|p. 21]]
**Fonte:** slide 21 e nota a mano $\lim_{x\to0}\frac{a^x-1}{x}=\ln a$.

$$
\begin{aligned}
2^{\eta_B}&=e^{\eta_B\ln2}=1+\eta_B\ln2+\frac{(\eta_B\ln2)^2}{2}+\dots && \text{sviluppo di Taylor dell'esponenziale}\\
\frac{2^{\eta_B}-1}{\eta_B}&=\ln2+\frac{\eta_B(\ln2)^2}{2}+\dots\ \xrightarrow{\ \eta_B\to0\ }\ \ln2 && \text{è il limite notevole con } a=2\\
10\log_{10}(\ln2)&=10\log_{10}(0.6931)=-1.59\ \text{dB} && \text{conversione in dB}
\end{aligned}
$$

**Significato:** anche con banda illimitata (quindi $\eta_B\to0$) non si può comunicare in modo affidabile con meno di $0.693$ volte $N_0$ di energia per bit. È lo stesso risultato del limite $C_\infty=\frac{P}{N_0}\log_2e$: con $R_b\le C_\infty$ e $P=E_bR_b$ si ottiene $E_b/N_0\ge1/\log_2e=\ln2$.

### Derivazione — Distanza delle modulazioni reali dal limite · [[Confronto_new.pdf#page=23|p. 23]]
**Fonte:** la figura della slide 23 riporta i punti delle modulazioni a $P_b(e)=10^{-5}$.

> 🧩 Derivazione mia, per leggere la figura. A $P_b(e)=10^{-5}$, con l'approssimazione (6) di [[parametri-globali-modulazioni]], BPSK e QPSK richiedono $E_b/N_0\approx9.6$ dB. La QPSK ha $\eta_B=2$, dove la frontiera chiede solo $1.76$ dB: restano circa **7.8 dB** di distanza dal limite. È il margine che la **codifica di canale** può recuperare; per questo la nota a mano dice che con una codifica i punti si sposterebbero verso sinistra.

## Spiegazione · appunti [[Confronto new.pdf#page=22|p. 22]]–[[Confronto new.pdf#page=25|25]]

La capacità dice quanti bit/s passano in un canale con banda $W$ e SNR $\gamma$. Riscrivendo tutto con i parametri globali ($\eta_B$ e $E_b/N_0$) si ottiene una curva che vale **per qualunque modulazione**: è il confine tra ciò che si può fare e ciò che è impossibile.

**Come si legge il piano.** In ascissa c'è l'energia per bit ($E_b/N_0$ in dB), in ordinata quanti bit/s si trasmettono per Hz ($\eta_B$, in scala logaritmica). A sinistra della frontiera c'è la regione impossibile. Ogni modulazione, fissata la BER, è un punto a destra della curva; più è vicino alla curva, meglio sfrutta le risorse.

**Le due regioni.** La linea $\eta_B=1$ separa due modi di progettare.
- **Limitato in banda** ($\eta_B>1$): la banda è la risorsa scarsa. Si usano costellazioni dense (M-PSK, M-QAM) che aumentano $\eta_B$ pagando in $E_b/N_0$.
- **Limitato in potenza** ($\eta_B<1$): l'energia è la risorsa scarsa e la banda è abbondante. Si usano schemi ortogonali (M-FSK) che, aumentando $M$, riducono l'$E_b/N_0$ richiesto consumando banda.

**Asintoto.** Per $\eta_B\to0$ la curva tende alla verticale $E_b/N_0=-1.59$ dB: nessuna quantità di banda permette di scendere sotto.

**Dagli appunti presi a lezione.** La frontiera è solo un altro modo di scrivere la condizione del secondo teorema di Shannon. Il valore di $-1.6$ dB è un **limite invalicabile**: sotto non vale più il teorema. La figura delle modulazioni viene dal libro di **Biglieri**; la distanza orizzontale tra ogni punto e la curva è il **margine di miglioramento**, che una codifica di canale permette di ridurre spostando i punti verso il limite.

![[confronto-p23-appunti-limite-shannon.png|260]]
*Schizzo della docente negli appunti: le curve di probabilità d'errore in funzione di $E_b/N_0$ diventano più ripide e si spostano a sinistra man mano che lo schema migliora, ma restano tutte a destra della verticale a $-1.6$ dB.*

> 🎯 Esame: derivazione della frontiera da $R_b\le C$ (tutti i passaggi), limite $\ln2=-1.59$ dB con il limite notevole, significato delle regioni limitate in banda e in potenza, lettura del grafico della slide 23 (anche che la codifica sposta i punti verso sinistra).

## Perché importa

È il **termine di paragone** di ogni sistema: un progettista confronta il suo punto di lavoro con la frontiera per sapere quanto margine resta da recuperare con la codifica, o se conviene cambiare modulazione. Spiega anche le scelte pratiche: costellazioni dense dove la banda è cara, schemi ortogonali dove è cara la potenza.

## Connessioni

- [[informazione-mutua-e-capacita]] — la capacità AWGN da cui discende la frontiera.
- [[parametri-globali-modulazioni]] — $\eta_B$, $\eta_P$ e la tabella delle modulazioni che si dispongono nel piano.
- [[link-budget]] — l'$E_b/N_0$ richiesto da una modulazione reale entra nel calcolo della sensibilità.

## Fonti · [[Confronto_new.pdf#page=20|p. 20]]–[[Confronto_new.pdf#page=23|23]]

[[parametri-globali-e-capacita]] — Confronto_new.pdf, slide 20–23.

_Aggiornato: 2026-11-22 — schizzo delle curve BER dagli appunti di p. 23; 2026-11-15 — appunti presi a lezione dalla copia annotata Confronto new.pdf; creazione da ingest Confronto_new.pdf_
