---
tipo: fonte
titolo: "Global parameters for memoryless modulation and channel capacity"
file_raw: "Confronto_new.pdf"  # appunti presi a lezione: "Confronto new.pdf"
pagine: "1-33"
data_ingest: 2026-11-15
formato: slide-pdf
argomenti: ["informazione mutua", "capacità di canale", "capacità AWGN", "banda di Shannon", "efficienza spettrale", "efficienza in potenza", "limite di Shannon", "link budget"]
---

# Parametri globali delle modulazioni e capacità di canale

## Sommario · [[Confronto_new.pdf#page=1|p. 1]]–[[Confronto_new.pdf#page=33|33]]

Lezione 8 del corso (33 slide in inglese, con note a mano della docente). Introduce l'**informazione mutua** e la **capacità di canale** come limiti teorici, con il secondo teorema di Shannon e la capacità del canale AWGN $C=W\log_2(1+\gamma)$, che la docente indica come risultato da **non dimostrare**. Definisce poi i **parametri globali** per confrontare le modulazioni a partire dalla sola geometria della costellazione: banda di Shannon $W=N/(2T)$, energia per bit $E_b$, SNR $=\frac{E_b}{N_0}\eta_B$, efficienza spettrale $\eta_B=2\log_2M/N$ ed efficienza in potenza $\eta_P=d_{min}^2/(4E_b)$, che governa la probabilità d'errore. Una tabella mette a confronto PAM, PSK, QAM e ortogonali e mostra il compromesso energia-banda. Da $R_b\le C$ si ricava la **frontiera di Shannon** $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$, con il minimo assoluto $\ln2=-1.59$ dB, e il grafico delle modulazioni reali nel piano efficienza spettrale – $E_b/N_0$. Gli appunti presi a lezione stanno nella copia annotata `Confronto new.pdf` (35 pagine, con due pagine di soli appunti: la dimostrazione di $I=H(Y)-H(Y\mid X)$ con l'entropia come media dell'autoinformazione, e lo schizzo del rumore in banda contro il rumore bianco); sono riportati slide per slide in [[corso-completo]]. La lezione si chiude con il **link budget** (rumore, sensibilità, Friis, path loss) e un esempio completo di collegamento WLAN a 5 GHz.

## Punti chiave · [[Confronto_new.pdf#page=4|p. 4]]–[[Confronto_new.pdf#page=32|32]]

1. $I(X;Y)=H(Y)-H(Y\mid X)=H(X)-H(X\mid Y)$: riduzione media di incertezza; simmetrica, nulla per variabili indipendenti.
2. $C=\max_{p(x)}I(X;Y)$; secondo teorema di Shannon: $R_b<C$ errore piccolo a piacere, $R_b>C$ impossibile.
3. AWGN: $C=W\log_2(1+P/(N_0W))$, lineare in $W$, logaritmica in $\gamma$ (non va dimostrata).
4. Banda di Shannon $W=N/(2T)$; $P=E_bR_b$; $\text{SNR}=\frac{E_b}{N_0}\frac{R_b}{W}$.
5. $\eta_B=2\log_2M/N$; $\eta_P=d_{min}^2/(4E_b)$: OOK $\frac12$, antipodale 1, ortogonale binaria $\frac12$.
6. $P(e)\approx\frac{\bar N_{d_{min}}}{2}\text{erfc}\sqrt{\eta_PE_b/N_0}$: $\eta_P$ basta a confrontare le modulazioni a SNR alto.
7. Dimensionalità fissa (PAM, PSK, QAM): $M$ più grande, più $\eta_B$ e meno $\eta_P$; ortogonali: il contrario.
8. Frontiera di Shannon $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$, minimo $-1.59$ dB; regioni limitata in banda ($\eta_B>1$) e in potenza ($\eta_B<1$).
9. Link budget: $\text{SNR}_{req}$, $P_n=kT_0FW$, sensibilità, Friis, path loss massimo con margine.
10. Esempio WLAN: 30 Mbit/s, sensibilità $-83$ dBm, portata circa 107 m.

## Concetti introdotti

- [[informazione-mutua-e-capacita]]
- [[parametri-globali-modulazioni]]
- [[limite-di-shannon]]
- [[link-budget]]
- [[link-budget-wlan]] (esercizio)

## Domande aperte

- Slide 30: l'$E_b/N_0$ richiesto per BER $=10^{-6}$ con QPSK è dato come 10.2 dB; dalla formula $Q(\sqrt{2E_b/N_0})=10^{-6}$ risulta circa 10.5 dB (vedi [[link-budget-wlan]]).
- Slide 19: nella riga delle ortogonali $\eta_P$ è stampata come $2\log_2M$ con una correzione a mano; il valore coerente con gli esempi è $\frac12\log_2M$.
- Slide 23: l'ordinata è scritta $R_s/W$, ma nel resto della lezione è l'efficienza spettrale $\eta_B=R_b/W$.
- Copia annotata, p. 15: «è il canale che fa da filtro, oppure bisogna aggiungerne uno al ricevitore?». La slide 13 indica il filtro di ricezione di banda $W$.
- Slide 17 rimanda alle «lecture notes» per l'approssimazione della probabilità d'errore: le dispense sulla rivelazione non sono ancora nel wiki.

## Domande da esame

- Definire l'informazione mutua e dimostrare che $I(X;Y)=H(Y)-H(Y\mid X)$. Quando è nulla?
- Definire la capacità di canale ed enunciare il secondo teorema di Shannon.
- Scrivere la capacità del canale AWGN e commentarne la dipendenza da banda e SNR.
- Che cos'è la banda di Shannon e perché si usa per confrontare le modulazioni?
- Definire efficienza spettrale ed efficienza in potenza; calcolarle per OOK, antipodale e ortogonale binaria.
- Perché l'efficienza in potenza permette di confrontare le probabilità d'errore delle modulazioni?
- Illustrare il compromesso energia-banda per modulazioni a dimensionalità fissa e ortogonali.
- Derivare la frontiera di Shannon e il limite di $-1.59$ dB.
- Descrivere il piano efficienza spettrale – $E_b/N_0$: regioni limitate in banda e in potenza.
- Descrivere la procedura di link budget e calcolare sensibilità e portata di un collegamento.

_Aggiornato: 2026-11-15 — integrati gli appunti presi a lezione (Confronto new.pdf); creazione da ingest Confronto_new.pdf_
