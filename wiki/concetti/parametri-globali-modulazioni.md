---
tipo: concetto
importanza_esame: alta
prerequisiti: ["informazione-mutua-e-capacita", "variabile-aleatoria-gaussiana"]
fonti_pdf: ["Confronto_new.pdf#page=10", "Confronto_new.pdf#page=11", "Confronto_new.pdf#page=12", "Confronto_new.pdf#page=13", "Confronto_new.pdf#page=14", "Confronto_new.pdf#page=15", "Confronto_new.pdf#page=16", "Confronto_new.pdf#page=17", "Confronto_new.pdf#page=18", "Confronto_new.pdf#page=19"]
---

# Parametri globali delle modulazioni

## Definizione · [[Confronto_new.pdf#page=10|p. 10]]–[[Confronto_new.pdf#page=18|18]]

I **parametri globali** sono le grandezze con cui si confrontano schemi di modulazione diversi senza entrare nei dettagli delle forme d'onda, guardando solo alla **geometria della costellazione**: la **banda di Shannon** $W$, l'**energia per bit** $E_b$, il rapporto $E_b/N_0$, l'**efficienza spettrale** $\eta_B=R_b/W$ e l'**efficienza in potenza** $\eta_P=d_{min}^2/(4E_b)$. Fissata la probabilità d'errore, una modulazione è buona se usa poca banda (alto $\eta_B$) e poca energia per bit (alto $\eta_P$); in generale le due cose non si ottengono insieme.

## Formule · [[Confronto_new.pdf#page=11|p. 11]]–[[Confronto_new.pdf#page=19|19]]

| Formula | Significato |
|---|---|
| $N=2WT$, $W=\frac{N}{2T}$ | prodotto tempo-banda; banda di Shannon [Hz, o dimensioni/s] |
| $P=\frac ET$ (1) | potenza media del modulatore [W] |
| $E_b=\frac{E}{\log_2M}$ (2) | energia media per bit [J] |
| $P=E_bR_b$ (3) | potenza = energia per bit × bit rate |
| $\text{SNR}=\frac{P}{N_0W}=\frac{E_b}{N_0}\frac{R_b}{W}$ | SNR al ricevitore |
| $\eta_B=\frac{R_b}{W}=\frac{2\log_2M}{N}$ | efficienza spettrale [bit/s/Hz] |
| $\eta_P=\frac{d_{min}^2}{4E_b}$ (4) | efficienza in potenza (adimensionale) |
| $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\big(\sqrt{\eta_PE_b/N_0}\big)$ (6) | probabilità d'errore di simbolo, approssimazione dei vicini |

> 🧮 Formula chiave: $\text{SNR}=\dfrac{E_b}{N_0}\,\eta_B$, $\eta_B=\dfrac{2\log_2M}{N}$, $\eta_P=\dfrac{d_{min}^2}{4E_b}$.

Simboli: $M$ cardinalità della costellazione; $N$ dimensionalità dello spazio dei segnali; $T=T_b\log_2M$ [s] periodo di simbolo, $T_b$ periodo di bit; $R_b=1/T_b$ [bit/s]; $E$ [J] energia media dei segnali; $N_0$ [W/Hz] densità spettrale del rumore; $d_{min}$ [$\sqrt{\text{J}}$] distanza minima tra i punti della costellazione; $\bar N_{d_{min}}$ numero medio di vicini a distanza minima.

## Derivazioni

### Derivazione — Banda di Shannon · [[Confronto_new.pdf#page=11|p. 11]]
**Fonte:** la slide definisce $W=N/(2T)$ a partire da $N=2WT$ e dà l'esempio M-PSK.

$$
\begin{aligned}
N&=2WT && \text{dimensioni disponibili in durata } T \text{ e banda } W\\
W&=\frac{N}{2T} && \text{banda minima per ospitare } N \text{ dimensioni in } T\\
\text{M-PSK: }N=2\ \Rightarrow\ W&=\frac{2}{2T}=\frac1T && \text{seno e coseno: 2 dimensioni}\\
\text{ortogonale: }N=M\ \Rightarrow\ W&=\frac{M}{2T} && \text{una dimensione per segnale}
\end{aligned}
$$

**Unità:** $N$ è un numero puro e $T$ un tempo, quindi $W$ si misura in 1/s, cioè Hz o «dimensioni al secondo».

### Derivazione — Potenza ed energia per bit, eq. (1)–(3) · [[Confronto_new.pdf#page=12|p. 12]]
**Fonte:** slide 12.

$$
\begin{aligned}
P&=\frac ET && \text{(1): energia per simbolo diviso durata del simbolo}\\
E_b&=\frac{E}{\log_2M} && \text{(2): ogni simbolo porta } \log_2M \text{ bit}\\
P&=\frac{E_b\log_2M}{T}=E_b\,\frac{\log_2M}{T}=E_b\,R_b && \text{(2) in (1); } R_b=\tfrac{\log_2M}{T}=\tfrac1{T_b}
\end{aligned}
$$

**Unità:** J · bit/s = W. **Sanity check:** a parità di $E_b$, trasmettere più bit al secondo costa proporzionalmente più potenza.

### Derivazione — SNR ed efficienza spettrale · [[Confronto_new.pdf#page=13|p. 13]], [[Confronto_new.pdf#page=14|14]]
**Fonte:** slide 13–14, risultati senza passaggi.

$$
\begin{aligned}
\text{SNR}&=\frac{P}{N_0W} && \text{potenza del segnale su potenza del rumore in banda } W\\
&=\frac{E_bR_b}{N_0W}=\frac{E_b}{N_0}\cdot\frac{R_b}{W}=\frac{E_b}{N_0}\,\eta_B && \text{(3)}\\
\eta_B&=\frac{R_b}{W}=\frac{\log_2M/T}{N/(2T)}=\frac{2\log_2M}{N} && R_b=\tfrac{\log_2M}{T},\ W=\tfrac{N}{2T}
\end{aligned}
$$

**Numeri (slide 14):** $R_b=9.6$ kbit/s, $W=4.8$ kHz $\Rightarrow\eta_B=9.6/4.8=2$ bit/s/Hz.
**Lettura:** il periodo $T$ si semplifica, quindi $\eta_B$ dipende solo da quanti bit porta un simbolo ($\log_2M$) e da quante dimensioni usa ($N$).

### Derivazione — Esempi di efficienza in potenza · [[Confronto_new.pdf#page=15|p. 15]], [[Confronto_new.pdf#page=16|16]]
**Fonte:** slide 16. Tutti binari, quindi $M=2$, $\log_2M=1$ ed $E_b=E$.

$$
\begin{aligned}
\text{OOK: }&d_{min}=A,\ E_b=\tfrac12(0+A^2)=\tfrac{A^2}{2} &&\Rightarrow\ \eta_P=\frac{A^2}{4\cdot A^2/2}=\frac12\\
\text{antipodale: }&d_{min}=2A,\ E_b=\tfrac12(A^2+A^2)=A^2 &&\Rightarrow\ \eta_P=\frac{4A^2}{4A^2}=1\\
\text{ortogonale: }&d_{min}=\lVert(A,-A)\rVert=\sqrt2A,\ E_b=A^2 &&\Rightarrow\ \eta_P=\frac{2A^2}{4A^2}=\frac12
\end{aligned}
$$

**Lettura:** a parità di energia per bit, l'antipodale separa i punti il doppio (in $d^2$) rispetto a OOK e ortogonale: per la stessa probabilità d'errore richiede $10\log_{10}2\approx3$ dB in meno di $E_b/N_0$.

### Derivazione — Dalla (5) alla (6) · [[Confronto_new.pdf#page=17|p. 17]]
**Fonte:** slide 17, «sostituendo (4) in (5)».

$$
\begin{aligned}
\frac{d_{min}}{2\sqrt{N_0}}&=\sqrt{\frac{d_{min}^2}{4N_0}} && \text{porto tutto sotto radice}\\
&=\sqrt{\frac{\eta_P\cdot4E_b}{4N_0}}=\sqrt{\eta_P\frac{E_b}{N_0}} && \text{dalla (4): } d_{min}^2=4\eta_PE_b
\end{aligned}
$$

quindi $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\big(\sqrt{\eta_PE_b/N_0}\big)$.
**Perché basta $\eta_P$ per confrontare:** la erfc decresce in modo esponenziale con il quadrato dell'argomento, mentre $\bar N_{d_{min}}$ è solo un fattore moltiplicativo. Due modulazioni con $\eta_{P,1}$ ed $\eta_{P,2}$ raggiungono quasi la stessa $P(e)$ quando $\eta_{P,1}E_b/N_0=\eta_{P,2}E_b/N_0$: la distanza orizzontale tra le curve è $10\log_{10}(\eta_{P,1}/\eta_{P,2})$ dB.
**Ipotesi:** SNR moderatamente alto, rumore AWGN, decisione a minima distanza.

### Derivazione — Tabella di $\eta_B$ ed $\eta_P$ · [[Confronto_new.pdf#page=19|p. 19]]
**Fonte:** la tabella della slide 19 è data senza passaggi.

> 🧩 Derivazione mia. $\eta_B=2\log_2M/N$ discende solo dalla dimensionalità; per $\eta_P$ servono $d_{min}$ ed $E$ di ciascuna costellazione.

**PAM** ($N=1$): livelli $\pm A,\pm3A,\dots,\pm(M-1)A$, quindi $d_{min}=2A$. L'energia media usa $\sum_{k=1}^{n}(2k-1)^2=\frac{n(4n^2-1)}{3}$ con $n=M/2$:

$$
E=\frac{2A^2}{M}\sum_{k=1}^{M/2}(2k-1)^2=\frac{2A^2}{M}\cdot\frac{\frac M2(M^2-1)}{3}=\frac{A^2(M^2-1)}{3},\qquad\eta_P=\frac{4A^2\log_2M}{4E}=\frac{3\log_2M}{M^2-1}
$$

**PSK** ($N=2$): punti sul cerchio di raggio $\sqrt E$ con angoli $2\pi k/M$; due punti adiacenti distano una corda $d_{min}=2\sqrt E\sin\frac{\pi}{M}$:

$$
\eta_P=\frac{4E\sin^2(\pi/M)}{4E/\log_2M}=\log_2M\,\sin^2\frac{\pi}{M}
$$

**QAM quadrata** ($N=2$, $M=L^2$): due $L$-PAM in quadratura, ciascuna con energia $A^2(L^2-1)/3=A^2(M-1)/3$, e $d_{min}=2A$:

$$
E=\frac{2A^2(M-1)}{3},\qquad\eta_P=\frac{4A^2\log_2M}{4\cdot\frac{2A^2(M-1)}{3}}=\frac{3\log_2M}{2(M-1)}
$$

**Ortogonale** ($N=M$): $\mathbf s_i=\sqrt E\,\mathbf e_i$, quindi $d_{min}=\lVert\mathbf s_i-\mathbf s_j\rVert=\sqrt{2E}$:

$$
\eta_P=\frac{2E}{4E/\log_2M}=\frac{\log_2M}{2},\qquad\eta_B=\frac{2\log_2M}{M}
$$

**Sanity check:** $M=2$ dà PAM = PSK = antipodale ($\eta_P=1$) e ortogonale binaria ($\eta_P=\frac12$), come gli esempi della slide 16; $M=4$ dà QPSK = 4-QAM ($\eta_P=1$, $\eta_B=2$) con entrambe le formule.

**Valori numerici** (calcolati dalle formule):

| $M$ | PAM $\eta_B$ / $\eta_P$ | PSK $\eta_B$ / $\eta_P$ | QAM $\eta_B$ / $\eta_P$ | ortogonale $\eta_B$ / $\eta_P$ |
|---|---|---|---|---|
| 2 | 2 / 1 | 1 / 1 | — | 1 / 0.5 |
| 4 | 4 / 0.4 | 2 / 1 | 2 / 1 | 1 / 1 |
| 8 | 6 / 0.143 | 3 / 0.439 | — | 0.75 / 1.5 |
| 16 | 8 / 0.047 | 4 / 0.152 | 4 / 0.4 | 0.5 / 2 |
| 64 | 12 / 0.004 | 6 / 0.014 | 6 / 0.143 | 0.19 / 3 |

Con $M$ crescente, PAM, PSK e QAM salgono in $\eta_B$ e scendono in $\eta_P$; le ortogonali fanno l'opposto. A parità di $\eta_B$ la QAM ha l'$\eta_P$ migliore tra gli schemi bidimensionali: a $\eta_B=4$, 16-QAM ha $\eta_P=0.4$ contro $0.152$ della 16-PSK, cioè circa $10\log_{10}(0.4/0.152)\approx4.2$ dB in meno di $E_b/N_0$.

## Spiegazione · appunti [[Confronto new.pdf#page=11|p. 11]]–[[Confronto new.pdf#page=21|21]]

Per confrontare modulazioni diverse servono grandezze che non dipendano dalla forma d'onda scelta. La slide 10 spiega il problema della **banda**: con impulsi di durata finita lo spettro è infinito, e ogni definizione pratica di banda (null-to-null, frazione di potenza) dà un numero diverso. Si usa allora una banda «astratta», la **banda di Shannon**: un insieme di segnali che occupa $N$ dimensioni ogni $T$ secondi richiede almeno $W=N/(2T)$ Hz, perché in banda $W$ e durata $T$ entrano $2WT$ dimensioni. La banda reale sarà $\alpha/T$ con $\alpha$ che dipende dall'impulso, ma il confronto tra costellazioni non cambia.

**Energia.** Le modulazioni hanno $M$ diversi, quindi non si confrontano le energie di simbolo ma l'**energia per bit** $E_b=E/\log_2M$. Il rapporto $E_b/N_0$ è la «qualità energetica» del collegamento e non dipende dalla banda.

**Due efficienze, un compromesso.**
- $\eta_B=R_b/W$ dice quanti bit/s si trasmettono per ogni Hz. Cresce se ogni simbolo porta più bit ($M$ grande) o se si usano meno dimensioni ($N$ piccolo).
- $\eta_P=d_{min}^2/(4E_b)$ dice quanta separazione tra i punti si ottiene per ogni joule speso per bit. Determina la probabilità d'errore: punti più lontani si confondono meno.
- L'SNR lega le due cose: $\text{SNR}=\frac{E_b}{N_0}\eta_B$. A parità di SNR disponibile, chi vuole più bit/s/Hz ha meno energia per bit.

**Il compromesso della tabella.** Le costellazioni a dimensionalità fissa (PAM, PSK, QAM) mettono più punti nello stesso spazio: più bit per simbolo nella stessa banda, ma i punti si avvicinano e serve più $E_b/N_0$. Le ortogonali aggiungono una dimensione per ogni segnale: i punti restano lontani (anzi $\eta_P$ cresce), ma la banda cresce con $M$.

**Dagli appunti presi a lezione.**
- Tra le risorse c'è anche la complessità: il problema non è tanto l'elaborazione quanto il **ritardo** dovuto ai dati da elaborare.
- $N$ è la dimensionalità della costellazione (approccio geometrico) e $N/T$ il numero di dimensioni trasmesse al secondo: è ciò che la banda di Shannon conta.
- Nell'SNR $=\frac{E_b}{N_0}\frac{R_b}{W}$ il primo fattore è il contributo dell'energia, il secondo quello dell'efficienza in banda.
- La $W$ dell'SNR è la banda del **filtro di ricezione**: il rumore bianco (PSD piatta $N_0/2$, acf impulsiva) è un modello di comodo per i calcoli, ed è il ricevitore a limitarlo alla banda utile, come in [[rumore-in-banda-passante]].
- Le ortogonali aggiungono una dimensione per ogni nuovo segnale: la banda cresce con $M$, quindi si usano **quando la banda è disponibile** e conta risparmiare energia.

> 🎯 Esame: definizione e significato di banda di Shannon, $E_b$, $\eta_B$, $\eta_P$; perché $\eta_P$ basta a confrontare le probabilità d'errore (passaggio dalla (5) alla (6)); esempi OOK, antipodale, ortogonale; il compromesso energia-banda della tabella con il diverso comportamento delle modulazioni a dimensionalità fissa e di quelle ortogonali.

## Perché importa

Questi parametri sono gli assi su cui si disegna il confronto con il limite teorico ([[limite-di-shannon]]): ogni modulazione è un punto nel piano $(E_b/N_0,\eta_B)$ a BER fissata. Sono anche le grandezze del progetto reale: dall'$E_b/N_0$ richiesto e dall'$\eta_B$ si calcola l'SNR richiesto, e da lì la sensibilità del ricevitore e la portata ([[link-budget]]).

## Connessioni

- [[informazione-mutua-e-capacita]] — il $\gamma$ della capacità AWGN è proprio $\frac{E_b}{N_0}\eta_B$.
- [[limite-di-shannon]] — il minimo $E_b/N_0$ per ogni $\eta_B$.
- [[link-budget]] — $\text{SNR}_{req}=(E_b/N_0)_{req}\,R_b/W$.
- [[variabile-aleatoria-gaussiana]] — la erfc della probabilità d'errore è la coda della gaussiana.
- [[rumore-in-banda-passante]] — $N_0$ e la potenza di rumore $N_0W$.

## Fonti · [[Confronto_new.pdf#page=10|p. 10]]–[[Confronto_new.pdf#page=19|19]]

[[parametri-globali-e-capacita]] — Confronto_new.pdf, slide 10–19.

_Aggiornato: 2026-11-15 — appunti presi a lezione dalla copia annotata Confronto new.pdf; creazione da ingest Confronto_new.pdf_
