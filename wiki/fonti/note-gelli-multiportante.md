---
tipo: fonte
titolo: "Modulazione multiportante, sistemi OFDM e DMT (G. Gelli, 2001)"
file_raw: "Note 2001 Gelli G.pdf"
pagine: "1-24"
data_ingest: 2026-11-27
formato: appunti
ruolo: approfondimento  # NON è una lezione e non è materia d'esame
argomenti: ["modulazione multiportante", "OFDM e DMT", "biortogonalità", "spettro multiportante", "prestazioni QAM", "tempo di guardia", "realizzazione con DFT", "prefisso ciclico", "bit loading", "SNR gap", "water filling"]
---

# Note di G. Gelli: modulazione multiportante, OFDM e DMT (approfondimento)

> 📚 **Approfondimento, non lezione.** Dispensa del prof. Giacinto Gelli (maggio 2001), fornita come lettura facoltativa insieme alla Lezione 15. Il contenuto completo, con le derivazioni espanse, sta in [[multiportante-ofdm-dmt-gelli]] (cartella `wiki/approfondimenti/`), separato dalle pagine d'esame.

## Sommario · [[Note 2001 Gelli G.pdf#page=1|p. 1]]–[[Note 2001 Gelli G.pdf#page=24|24]]

Dispensa di 22 pagine più bibliografia e indice. Presenta la modulazione multiportante come somma di $N$ sottoportanti QAM/PSK, con la possibilità di assegnare bit diversi a ciascuna (bit loading); distingue OFDM (broadcast, bit uguali) e DMT (punto-punto, DSL, bit loading). Ricava la condizione di biortogonalità degli impulsi rettangolari con spaziatura $1/T$, lo spettro somma di sinc² e la banda $(N+1)/T$; calcola le prestazioni QAM per sottoportante in AWGN; introduce il tempo di guardia ($T=T_g+T_u$, spaziatura $1/T_u$) e mostra che il sistema diventa $N$ canali AWGN indipendenti con guadagno $\frac{T_u}{T}H(i/T_u)$; realizza il sistema con IDFT/DFT e convertitori ideali senza perdita di prestazioni; ricava il prefisso ciclico a tempo discreto; chiude con il bit loading a probabilità d'errore costante, lo SNR gap e la distribuzione ottima dell'energia (water filling). Usa notazioni diverse dalle slide della Lezione 15 (tabella in [[multiportante-ofdm-dmt-gelli]]).

## Punti chiave · [[Note 2001 Gelli G.pdf#page=1|p. 1]], [[Note 2001 Gelli G.pdf#page=3|3]], [[Note 2001 Gelli G.pdf#page=7|7]], [[Note 2001 Gelli G.pdf#page=9|9]], [[Note 2001 Gelli G.pdf#page=12|12]], [[Note 2001 Gelli G.pdf#page=16|16]], [[Note 2001 Gelli G.pdf#page=19|19]], [[Note 2001 Gelli G.pdf#page=21|21]]

1. Multiportante = $N$ sottocanali; OFDM (broadcast) contro DMT (punto-punto con bit loading). Vantaggi: velocità vicine alla capacità, ISI ridotta. Svantaggi: PAPR (ampiezza circa gaussiana), sensibilità alla sincronizzazione.
2. Biortogonalità $\langle p_k(t-mT),p_i(t-nT)\rangle=\delta_{k-i}\delta_{m-n}$ ⇒ niente ISI e ICI; spaziatura minima $1/T$.
3. $S_x(f)=\sum_i\sigma_{a_i}^2\text{sinc}^2(fT-i)$, $B_T\simeq N/T$: efficienza circa doppia della FDM.
4. QAM: $\sigma_a^2=\frac{M-1}6d^2$, $P_{QAM}\simeq4(1-\frac1{\sqrt M})Q\big(\sqrt{\frac3{M-1}\frac{\lvert H\rvert^2\mathcal E}{N_0}}\big)$.
5. Tempo di guardia $T_g\ge T_h$: $r_i(n)=(1-\gamma)H_ia_i(n)+n_i(n)$, $\gamma=T_g/T$; contrasto ridotto di $\lvert H_i\rvert^2(1-\gamma)$.
6. Con IDFT, P/S, D/A e A/D ideali e DFT si ha $s_i(n)=a_i(n)+w_i(n)$ con la stessa varianza $2N_0$ del caso continuo.
7. Prefisso ciclico di $L\ge M$ campioni: $s_i(n)=a_i(n)H_{tot}(i)$, equalizzatore a una presa.
8. Bit loading: $b_i=\log_2\big(1+\frac1\Gamma\frac{\mathcal E_i\lvert H_i\rvert^2}{\sigma_i^2}\big)$, SNR gap $\Gamma=\frac16[Q^{-1}(P/4)]^2$; energia ottima a water filling $\mathcal E_i=(K-\Gamma\sigma_i^2/\lvert H_i\rvert^2)^+$.

## Concetti introdotti

- [[multiportante-ofdm-dmt-gelli]] (pagina di approfondimento)
- collegati alla Lezione 15: [[ofdm]], [[prefisso-ciclico]], [[ofdm-con-fft]], [[equalizzazione-ofdm]], [[limiti-dell-ofdm]]

## Domande aperte · [[Note 2001 Gelli G.pdf#page=1|p. 1]], [[Note 2001 Gelli G.pdf#page=12|12]], [[Note 2001 Gelli G.pdf#page=13|13]]

- Tre punti delle note sembrano refusi (segnalati con ⚠️ nella pagina di approfondimento): a p. 1 "minore attenuazione" invece di "maggiore"; la (53)–(54) senza il fattore $\lvert H_i\rvert^2$ annunciato dalla (52); la fase della (57) con $(n-0.5)$ invece di $(2n+1)$.
- La prof non ha indicato quali parti delle note siano da leggere: la pagina le riporta tutte, come approfondimento.

## Domande da esame

Nessuna: è materiale di approfondimento, non d'esame. Per le domande sull'OFDM vedi [[signaling-ofdm]].

_Aggiornato: 2026-11-27 — creazione (Note 2001 Gelli G.pdf, approfondimento della Lezione 15)_
