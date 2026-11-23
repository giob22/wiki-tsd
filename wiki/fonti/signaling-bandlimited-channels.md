---
tipo: fonte
titolo: "Signaling over bandlimited channels"
file_raw: "signaling_bandlimited_channel_NEW.pdf"  # versione aggiornata (23/11); la precedente, con appunti sulle slide 2, 3, 9, 13, 14, 18, è goodnotes/signaling_bandlimited_channel.pdf
pagine: "1-61"
data_ingest: 2026-11-23
formato: slide-pdf
argomenti: ["ISI", "perdita di SNR e BER floor", "modello con filtri di trasmissione e ricezione", "criterio di Nyquist", "impulso di Nyquist ideale", "coseno rialzato", "filtri a radice di coseno rialzato", "efficienza di banda", "equalizzazione", "equalizzazione frazionaria", "zero-forcing", "MMSE", "MLSE", "coefficienti beta e memoria del canale", "algoritmo di Viterbi"]
---

# Signaling over bandlimited channels (Lezione 14)

## Sommario · [[signaling_bandlimited_channel_NEW.pdf#page=2|p. 2]]–[[signaling_bandlimited_channel_NEW.pdf#page=61|61]] · appunti [[signaling_bandlimited_channel.pdf#page=2|p. 2]], [[signaling_bandlimited_channel.pdf#page=3|3]], [[signaling_bandlimited_channel.pdf#page=9|9]], [[signaling_bandlimited_channel.pdf#page=13|13]], [[signaling_bandlimited_channel.pdf#page=14|14]], [[signaling_bandlimited_channel.pdf#page=18|18]]

Lezione iniziata il 16/11 e conclusa il 23/11. La docente ha aggiornato le slide: la versione nuova (59 slide più 2 pagine di soli appunti, 61 pagine) aggiunge i filtri a radice di coseno rialzato, l'equalizzazione a spaziatura frazionaria, gli equalizzatori zero-forcing e MMSE con le loro formule, e due slide sulla memoria del canale e sui coefficienti $\beta(\ell)$; corregge anche le (15)–(16) e gli indici della ricorsione di Viterbi. Gli appunti a mano della versione precedente (slide 2, 3, 9, 13, 14, 18) restano validi e sono citati da quella copia.

Un canale reale ha banda finita e deforma gli impulsi: nasce l'interferenza intersimbolica, che a differenza del rumore dipende dal segnale e può creare un pavimento nella BER. Con il modello filtro di trasmissione – canale – filtro di ricezione – campionatore si ricava il campione $y(kT)=s(k)+\text{ISI}$. Il criterio di Nyquist (nel tempo e in frequenza) dà la condizione di ISI nulla; la sinc la soddisfa con la banda minima $1/(2T)$ ma è irrealizzabile e fragile agli errori di timing, quindi si usa il coseno rialzato con roll-off $\alpha$ (banda $(1+\alpha)/(2T)$), diviso tra trasmettitore e ricevitore come due filtri a radice di coseno rialzato adattati. Il canale però non si controlla, e l'ISI che introduce va tolta con un equalizzatore: campionando più volte per simbolo, un equalizzatore lineare ZF o MMSE può annullare o ridurre l'ISI di un canale a memoria finita $L$. La soluzione ottima è la MLSE, che stima l'intera sequenza; i coefficienti $\beta(\ell)$, campioni dell'autocorrelazione dell'impulso, sono nulli per $\lvert\ell\rvert\ge L$, e questo permette di scrivere la log-verosimiglianza come somma di metriche di ramo e di massimizzarla con l'algoritmo di Viterbi.

## Punti chiave · [[signaling_bandlimited_channel_NEW.pdf#page=3|p. 3]], [[signaling_bandlimited_channel_NEW.pdf#page=13|13]], [[signaling_bandlimited_channel_NEW.pdf#page=17|17]], [[signaling_bandlimited_channel_NEW.pdf#page=26|26]], [[signaling_bandlimited_channel_NEW.pdf#page=27|27]], [[signaling_bandlimited_channel_NEW.pdf#page=31|31]], [[signaling_bandlimited_channel_NEW.pdf#page=32|32]], [[signaling_bandlimited_channel_NEW.pdf#page=37|37]], [[signaling_bandlimited_channel_NEW.pdf#page=39|39]], [[signaling_bandlimited_channel_NEW.pdf#page=41|41]]–[[signaling_bandlimited_channel_NEW.pdf#page=45|45]], [[signaling_bandlimited_channel_NEW.pdf#page=50|50]], [[signaling_bandlimited_channel_NEW.pdf#page=54|54]], [[signaling_bandlimited_channel_NEW.pdf#page=56|56]], [[signaling_bandlimited_channel_NEW.pdf#page=61|61]]

1. ISI dipende dal segnale, il rumore no; l'ISI può dare un BER floor, la perdita di SNR solo uno spostamento della curva.
2. $p(t)=g\ast h\ast c$; $y(kT)=s(k)+\sum_{n\neq k}s(n)p((k-n)T)$.
3. Nyquist: $p(kT)=\delta_k$ ⇔ $\sum_kP(f-k/T)=T$.
4. Sinc: banda minima $W_N=1/(2T)$, ma non causale e con code $1/|t|$.
5. Coseno rialzato: banda $W_N(1+\alpha)$, code $1/|t|^3$; $W_{actual}=(1+\alpha)R_b/\eta_B$.
6. Filtri RRC: $c(t)=g^\ast(-t)$, $\lvert G(f)\rvert^2=P_{RC}(f)$; la cascata è di Nyquist, il solo $g(t)$ no. L'ISI del canale la toglie un equalizzatore.
7. Con memoria finita $L$: $y(k)=s(k)p(0)+\sum_{m=1}^Ls(k-m)p(m)$. Con un campione per simbolo un equalizzatore di un intervallo non può togliere l'ISI; con $S\ge L+1$ campioni sì: $\mathbf y(k)=s(k)\mathbf p_0+\sum_ms(k-m)\mathbf p_m$.
8. ZF: $\mathbf P^H\mathbf c=\mathbf e_1$, a norma minima $\mathbf c_{ZF}=\mathbf P(\mathbf P^H\mathbf P)^{-1}\mathbf e_1$, può amplificare il rumore. MMSE: $\mathbf c_{MMSE}=\sigma_s^2\mathbf R_{rr}^{-1}\mathbf p_0$.
9. MLSE: filtro adattato a $q=g\ast h$ + massimizzazione su sequenze; $\beta(\ell)=r_q(\ell T)$, nullo per $\lvert\ell\rvert\ge L$, hermitiano.
10. $\lambda(y)=U_{L-1}(\sigma_L)+\sum_{k=L}^KV_k(\sigma_k,\sigma_{k+1})$: Viterbi con ACS, complessità lineare nel numero di simboli ed esponenziale nella memoria del canale.

## Concetti introdotti

- [[interferenza-intersimbolica]]
- [[criterio-di-nyquist]]
- [[equalizzazione]]
- [[algoritmo-di-viterbi]]

## Domande aperte

- A p. 16 «trasformando la (16)» si riferisce all'equazione appena scritta, non alla (16) delle slide.
- La DFE è solo nominata: niente formule né schemi.
- La figura dell'impulso deformato dal canale, a cui si riferiscono i «sidelobes» di p. 3, non è nelle slide.
- Slide 57: la somma nella (16) parte da $n=K-L$, ma il termine $\beta(-L)$ è nullo; gli appunti scrivono infatti $-L<n-K<L$. Non cambia nulla, è solo un termine nullo in più.
- Risolta con la versione aggiornata: le (15)–(16) e $V_k$ hanno ora $-\frac12|s(K)|^2\beta(0)$ (prima $+|s(K)|^2\beta(0)$), e $V_k$ è scritta come funzione di $(\sigma_k,\sigma_{k+1})$.

## Domande da esame

- Che cos'è l'ISI e in cosa differisce dal rumore? Perché può produrre un BER floor?
- Ricavare l'espressione del campione $y(kT)$ e individuare il termine di ISI.
- Enunciare il criterio di Nyquist nel tempo e ricavarne la forma in frequenza.
- Perché la sinc è la soluzione a banda minima e perché non si usa in pratica?
- Spettro e impulso a coseno rialzato: banda, ruolo del roll-off, decadimento delle code.
- Che cosa sono i filtri a radice di coseno rialzato e perché il filtro di ricezione si sceglie adattato?
- Tipi di equalizzatori e loro limiti.
- Perché un equalizzatore a spaziatura frazionaria riesce dove uno al symbol rate non riesce? Quanti campioni servono?
- Ricavare l'equalizzatore zero-forcing a norma minima e spiegare l'amplificazione del rumore.
- Ricavare l'equalizzatore MMSE.
- Che cosa sono i coefficienti $\beta(\ell)$, perché sono nulli per $\lvert\ell\rvert\ge L$ e quanto valgono per un impulso rettangolare?
- Ricavare il criterio MLSE con $\alpha(n)$ e $\beta(\ell)$ e spiegare come si applica l'algoritmo di Viterbi.

_Aggiornato: 2026-11-23 — ingest della versione aggiornata delle slide (signaling_bandlimited_channel_NEW.pdf, 61 pagine): RRC, equalizzazione frazionaria, ZF, MMSE, coefficienti β(ℓ), (15)–(16) corrette, appunti a lezione; 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf_
