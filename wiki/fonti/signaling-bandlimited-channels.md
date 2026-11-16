---
tipo: fonte
titolo: "Signaling over bandlimited channels"
file_raw: "goodnotes/signaling_bandlimited_channel.pdf"
pagine: "1-47"
data_ingest: 2026-11-16
formato: slide-pdf
argomenti: ["ISI", "perdita di SNR e BER floor", "modello con filtri di trasmissione e ricezione", "criterio di Nyquist", "impulso di Nyquist ideale", "coseno rialzato", "radice di Nyquist", "efficienza di banda", "equalizzazione", "MLSE", "algoritmo di Viterbi"]
---

# Signaling over bandlimited channels (Lezione 14)

## Sommario · [[signaling_bandlimited_channel.pdf#page=2|p. 2]]–[[signaling_bandlimited_channel.pdf#page=47|47]]

Lezione del 16/11: 47 slide con appunti a mano sulle slide 2, 3, 9, 13, 14 e 18. Un canale reale ha banda finita e deforma gli impulsi: nasce l'interferenza intersimbolica, che a differenza del rumore dipende dal segnale e può creare un pavimento nella BER. Con il modello filtro di trasmissione – canale – filtro di ricezione – campionatore si ricava il campione $y(kT)=s(k)+\text{ISI}$. Il criterio di Nyquist (nel tempo e in frequenza) dà la condizione di ISI nulla; la sinc la soddisfa con la banda minima $1/(2T)$ ma è irrealizzabile e fragile agli errori di timing, quindi si usa il coseno rialzato con roll-off $\alpha$ (banda $(1+\alpha)/(2T)$) e, in pratica, filtri a radice di Nyquist. Quando il canale non si controlla serve l'equalizzazione: lineare (ZF, MMSE), DFE, e la MLSE ottima, resa trattabile dall'algoritmo di Viterbi.

## Punti chiave · [[signaling_bandlimited_channel.pdf#page=3|p. 3]], [[signaling_bandlimited_channel.pdf#page=13|13]], [[signaling_bandlimited_channel.pdf#page=17|17]], [[signaling_bandlimited_channel.pdf#page=26|26]], [[signaling_bandlimited_channel.pdf#page=27|27]], [[signaling_bandlimited_channel.pdf#page=31|31]], [[signaling_bandlimited_channel.pdf#page=39|39]], [[signaling_bandlimited_channel.pdf#page=43|43]]

1. ISI dipende dal segnale, il rumore no; l'ISI può dare un BER floor, la perdita di SNR solo uno spostamento della curva.
2. $p(t)=g\ast h\ast c$; $y(kT)=s(k)+\sum_{n\neq k}s(n)p((k-n)T)$.
3. Nyquist: $p(kT)=\delta_k$ ⇔ $\sum_kP(f-k/T)=T$.
4. Sinc: banda minima $W_N=1/(2T)$, ma non causale e con code $1/|t|$.
5. Coseno rialzato: banda $W_N(1+\alpha)$, code $1/|t|^3$; $W_{actual}=(1+\alpha)R_b/\eta_B$.
6. In pratica $G$ e $C$ radici di Nyquist; l'ISI del canale va equalizzata.
7. MLSE: filtro adattato a $q=g\ast h$ + massimizzazione su sequenze; Viterbi con ACS, complessità lineare nel numero di simboli ed esponenziale nella memoria del canale.

## Concetti introdotti

- [[interferenza-intersimbolica]]
- [[criterio-di-nyquist]]
- [[equalizzazione]]
- [[algoritmo-di-viterbi]]

## Domande aperte

- Nelle (15)–(16) e in $V_k$ l'ultimo termine dovrebbe essere $-\frac12|s(K)|^2\beta(0)$ e non $+|s(K)|^2\beta(0)$ (vedi [[equalizzazione]]).
- A p. 16 «trasformando la (16)» si riferisce all'equazione appena scritta, non alla (16) delle slide.
- ZF, MMSE e DFE sono solo nominati: niente formule né schemi.
- La figura dell'impulso deformato dal canale, a cui si riferiscono i «sidelobes» di p. 3, non è nelle slide.

## Domande da esame

- Che cos'è l'ISI e in cosa differisce dal rumore? Perché può produrre un BER floor?
- Ricavare l'espressione del campione $y(kT)$ e individuare il termine di ISI.
- Enunciare il criterio di Nyquist nel tempo e ricavarne la forma in frequenza.
- Perché la sinc è la soluzione a banda minima e perché non si usa in pratica?
- Spettro e impulso a coseno rialzato: banda, ruolo del roll-off, decadimento delle code.
- Che cos'è un impulso a radice di Nyquist e perché si usa?
- Tipi di equalizzatori e loro limiti.
- Ricavare il criterio MLSE con $\alpha(n)$ e $\beta(\ell)$ e spiegare come si applica l'algoritmo di Viterbi.

_Aggiornato: 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf_
