---
tipo: fonte
titolo: "Appunti della lezione del 28/10"
file_raw: "goodnotes/Lezione 10-28.pdf"
pagine: "1-4"
data_ingest: 2026-11-16
formato: appunti
argomenti: ["on-off", "antipodale", "ortogonale binaria", "coefficiente di correlazione", "QPSK", "SER e BER"]
---

# Appunti della lezione del 28/10 (Lezione 10)

## Sommario · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=4|4]]

Quattro pagine di appunti a mano (primo caricamento 27/10). Calcolano la probabilità d'errore con ricevitore ML in AWGN: on-off (soglia $\sqrt{E_s}/2$, $P(e)=\frac12\text{erfc}(\frac12\sqrt{E_s/N_0})$, regioni congruenti), antipodale ($\frac12\text{erfc}\sqrt{E_s/N_0}$), ortogonale binaria ($\frac12\text{erfc}\sqrt{E_s/(2N_0)}$), formula generale $\frac12\text{erfc}(d/2\sqrt{N_0})$ con il coefficiente di correlazione $\rho$; invarianza per traslazioni e rotazioni ed energia minima con baricentro nullo. Poi la QPSK: base, inviluppo complesso, ricevitore sui segni di $z_1$, $z_2$, SER via corretta decisione e BER con Gray uguale all'antipodale. Nota sul metodo Monte Carlo ($100/p$ prove).

## Punti chiave · [[Lezione 10-28.pdf#page=1|p. 1]]–[[Lezione 10-28.pdf#page=4|4]]

1. On-off: soglia $\sqrt{E_s}/2$, indipendente da $N_0$; $P(e)=\frac12\text{erfc}(\frac12\sqrt{E_s/N_0})$.
2. Regioni congruenti: stessa $P(e\mid H_k)$ per ogni $k$.
3. Binaria generica: $P(e)=\frac12\text{erfc}(d/2\sqrt{N_0})$, $d^2=E_{s_1}+E_{s_2}-2\rho\sqrt{E_{s_1}E_{s_2}}$.
4. Antipodale ($\rho=-1$) migliore di ortogonale ($\rho=0$) e on-off.
5. QPSK: $P(e)=2p-p^2\simeq\text{erfc}\sqrt{E_b/N_0}$; BER con Gray $=\frac12\text{erfc}\sqrt{E_b/N_0}$.

## Concetti introdotti

- [[probabilita-errore-binaria]]
- [[probabilita-errore-m-aria]] (QPSK)

## Domande aperte

- Lo schizzo della $P(e)$ in funzione di $E_s/N_0$ (p. 1) è qualitativo: una curva con i valori va presa dal libro.

## Domande da esame

- Ricavare la probabilità d'errore della modulazione on-off con ricevitore ML.
- Confrontare on-off, antipodale e ortogonale binaria.
- Ricavare $P(e)$ di una modulazione binaria generica in funzione della distanza e di $\rho$.
- Calcolare la SER e la BER della QPSK.

_Aggiornato: 2026-11-16 — creazione da ingest Lezione 10-28.pdf_
