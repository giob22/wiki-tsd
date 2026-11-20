---
tipo: concetto
importanza_esame: alta
prerequisiti: ["modulazione-lineare", "ricevitore-ottimo-awgn", "probabilita-errore-binaria", "equivalente-banda-base-dei-filtri"]
fonti_pdf: ["signaling_bandlimited_channel.pdf#page=2", "signaling_bandlimited_channel.pdf#page=3", "signaling_bandlimited_channel.pdf#page=4", "signaling_bandlimited_channel.pdf#page=5", "signaling_bandlimited_channel.pdf#page=6", "signaling_bandlimited_channel.pdf#page=7", "signaling_bandlimited_channel.pdf#page=8", "signaling_bandlimited_channel.pdf#page=9", "signaling_bandlimited_channel.pdf#page=10", "signaling_bandlimited_channel.pdf#page=11", "signaling_bandlimited_channel.pdf#page=12", "signaling_bandlimited_channel.pdf#page=13"]
---

# Interferenza intersimbolica (ISI)

## Definizione · [[signaling_bandlimited_channel.pdf#page=2|p. 2]], [[signaling_bandlimited_channel.pdf#page=3|3]], [[signaling_bandlimited_channel.pdf#page=13|13]]

Un canale reale ha **banda finita**: un impulso che lo attraversa esce deformato e allungato, e le sue code (i lobi laterali) si sovrappongono agli impulsi dei simboli vicini. Il contributo dei simboli diversi da quello che si sta decidendo, presente nel campione all'istante di decisione, è l'**interferenza intersimbolica** (ISI).

A differenza del rumore, l'ISI **dipende dal segnale trasmesso**: il rumore c'è appena si accende il sistema, l'ISI sparisce solo se si spegne il segnale.

## Formule · [[signaling_bandlimited_channel.pdf#page=8|p. 8]], [[signaling_bandlimited_channel.pdf#page=10|10]]–[[signaling_bandlimited_channel.pdf#page=13|13]]

| Formula | Significato |
|---|---|
| $u(t)=\sum_ns(n)\,g(t-nT)$ | modulazione lineare (1) |
| $x(t)=u(t)\ast h(t)+n(t)$ | segnale ricevuto in banda base complessa, dopo la downconversion |
| $p(t)=g(t)\ast h(t)\ast c(t)$, $P(f)=G(f)H(f)C(f)$ | impulso complessivo (2)–(3) |
| $y(t_k)=s(k)+\sum_{n\neq k}s(n)\,p[(k-n)T]$ | campione all'istante $kT$, con $p(0)=1$ |

> 🧮 Formula chiave: $y(kT)=s(k)p(0)+\sum_{n\neq k}s(n)p((k-n)T)+n(k)$: simbolo utile, ISI, rumore.

Simboli: $s(n)$ simboli complessi; $g$, $h$, $c$ risposte impulsive di filtro di trasmissione, canale e filtro di ricezione; $T$ [s] periodo di simbolo; $n(t)$ WGN complesso; $P(f)$ trasformata dell'impulso complessivo.

## Derivazioni

### Derivazione — Campione all'uscita del filtro di ricezione · [[signaling_bandlimited_channel.pdf#page=11|p. 11]]–[[signaling_bandlimited_channel.pdf#page=13|13]]
**Si parte da:** (1) e linearità della convoluzione.

$$
\begin{aligned}
y(t)&=u(t)\ast h(t)\ast c(t)=\Big[\sum_ns(n)\,\delta(t-nT)\Big]\ast g(t)\ast h(t)\ast c(t) && \text{senza rumore}\\
&=\sum_ns(n)\,p(t-nT) && \delta(t-nT)\ast p(t)=p(t-nT)\\
y(kT)&=\sum_ns(n)\,p\big((k-n)T\big) && t=kT\\
&=s(k)\,p(0)+\sum_{n\neq k}s(n)\,p\big((k-n)T\big) && \text{separo } n=k\\
&=s(k)+\underbrace{\sum_{n\neq k}s(n)\,p\big((k-n)T\big)}_{\text{ISI}} && p(0)=1
\end{aligned}
$$

La normalizzazione $p(0)=1$ è, come annotato a p. 13, un guadagno in ricezione: non cambia il rapporto tra simbolo utile e ISI.
**Sanity check:** se $p(t)$ si annulla in tutti i $kT$ con $k\neq0$ (per esempio un impulso più corto di $T$), l'ISI è nulla e si torna al modello AWGN $y_k=s(k)+n(k)$.

### Derivazione — Perché c'è un BER floor · [[signaling_bandlimited_channel.pdf#page=6|p. 6]], [[signaling_bandlimited_channel.pdf#page=7|7]], [[signaling_bandlimited_channel.pdf#page=13|13]]
**Fonte:** gli appunti di p. 13 scrivono $y_k=p(0)s(k)+i(k)+n(k)$ e indicano $i(k)$ come motivo del BER floor.

> 🧩 Ragionamento mio. Con simboli antipodali $\pm1$ e soglia in 0, si sbaglia quando $i(k)+n(k)$ ha modulo maggiore di 1 e segno opposto al simbolo. Aumentando $E_b/N_0$ la varianza di $n(k)$ va a zero, ma $i(k)$ non cambia, perché scala con il segnale: se per qualche combinazione dei simboli vicini $|i(k)|\ge1$, quell'errore resta anche con rumore nullo. La BER tende allora alla probabilità di quelle combinazioni e non scende sotto quel valore: è il pavimento poco sotto $10^{-4}$ (circa $4\cdot10^{-5}$) della figura di p. 7. La perdita di SNR (p. 4–5) è un'altra cosa: la curva si sposta a destra (2 dB a BER $10^{-5}$) ma continua a scendere.

## Spiegazione · [[signaling_bandlimited_channel.pdf#page=2|p. 2]], [[signaling_bandlimited_channel.pdf#page=4|4]]–[[signaling_bandlimited_channel.pdf#page=10|10]]

- **Il canale non è più un sommatore** (appunti di p. 2): ha una risposta impulsiva che modifica lo spettro del segnale. In AWGN conta solo $E_b/N_0$; con banda limitata conta anche la forma degli impulsi.
- **Perdita di SNR e ISI.** Una perdita di SNR costa decibel (da 10 a 12 dB per BER $10^{-5}$ nell'esempio): si recupera con più potenza, il che è un problema per i sistemi limitati in potenza. L'ISI può invece creare un pavimento: più potenza non serve, serve l'**equalizzazione**, che inverte gli effetti di filtraggio non ottimi di trasmettitore e canale.
- **Modello del sistema (p. 9).** Si lavora con gli inviluppi complessi: simboli $s(n)$ → filtro di trasmissione $g(t)$ → canale $h(t)$ (non trasparente) + rumore → filtro di ricezione $c(t)$ → campionatore a $kT$, supposto perfettamente sincronizzato → decisore. In AWGN con $h=\delta$ il ricevitore ottimo è filtro adattato + campionatore ([[ricevitore-ottimo-awgn]]); qui si cerca un filtro di ricezione $c(t)$ che, insieme a $g$, renda l'ISI nulla negli istanti di campionamento ([[criterio-di-nyquist]]).
- Il ritardo di trasmissione $t_0$ andrebbe nell'argomento di $p(t-nT)$; si pone a zero senza perdere generalità, perché la [[sincronizzazione]] lo stima e lo compensa.

> 📚 Fonte esterna: la figura dell'impulso rettangolare deformato dal canale, a cui si riferiscono i «sidelobes» di p. 3, non è nelle slide. È tipica dei testi di comunicazioni (per esempio Sklar, *Digital Communications*, capitolo sull'ISI): da chiedere o recuperare se serve.

## Perché importa

L'ISI è il limite principale della trasmissione veloce su canali a banda limitata: a parità di banda, aumentare il symbol rate avvicina gli impulsi e fa crescere l'ISI. Da qui nascono il progetto degli impulsi di Nyquist e le tecniche di equalizzazione (tema 5 del programma, canali selettivi in frequenza).

## Connessioni

- [[criterio-di-nyquist]]: come annullare l'ISI con il progetto di $p(t)$.
- [[equalizzazione]]: come trattarla quando il canale non si controlla.
- [[modulazione-lineare]]: il modello (1) è quello della Lezione 8.
- [[probabilita-errore-binaria]]: le curve di BER senza ISI sono quelle della Lezione 10.

## Fonti · [[signaling_bandlimited_channel.pdf#page=2|p. 2]]–[[signaling_bandlimited_channel.pdf#page=13|13]]

- [[signaling-bandlimited-channels]]

_Aggiornato: 2026-11-20 — revisione della traduzione delle slide (banda base, banda passante del filtro, log-likelihood ratio, livello del BER floor); 2026-11-16 — creazione da ingest signaling_bandlimited_channel.pdf (Lezione 14)_
