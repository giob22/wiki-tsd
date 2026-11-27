---
tipo: fonte
titolo: "Signaling over bandlimited channels: OFDM"
file_raw: "ofdm_goldsmith_slides.pdf"  # 53 slide con appunti a lezione, più 5 pagine di soli appunti (p. 4, 9, 10, 13, 14): 58 pagine
pagine: "1-58"
data_ingest: 2026-11-27
formato: slide-pdf
argomenti: ["trasmissione multiportante", "FDM", "OFDM", "ortogonalità delle sottoportanti", "ISI e ICI", "banco di correlatori", "PSD dell'OFDM", "prefisso ciclico", "convoluzione circolare", "IFFT e FFT", "equalizzazione a una presa", "codifica e interleaving", "IEEE 802.11a", "modulazione adattativa", "PAPR", "offset di frequenza e di tempo", "scelta del numero di sottoportanti"]
---

# Signaling over bandlimited channels: OFDM (Lezione 15)

## Sommario · [[ofdm_goldsmith_slides.pdf#page=1|p. 1]]–[[ofdm_goldsmith_slides.pdf#page=58|58]]

Lezione del 27/11, slide della prof. Darsena (a.a. 2026-27) basate su Goldsmith, cap. 12. Il PDF ha 53 slide e 5 pagine di soli appunti a mano: p. 4 (conversione serie/parallelo come decomposizione polifase), p. 9 (schema con i mapper, $T_u=NT_b$, perché rallentare il sistema aiuta contro l'ISI), p. 10 (canale piatto su ogni sottoportante), p. 13 (ISI e ICI, due ortogonalità), p. 14 (calcolo dell'ortogonalità e perché la FFT ha reso pratico l'OFDM). Corrispondenza: slide 1–3 = p. 1–3, slide 4–7 = p. 5–8, slide 8–9 = p. 11–12, slide 10–53 = p. 15–58.

È la terza risposta all'ISI della Lezione 14, dopo equalizzatori e MLSE. Il flusso di bit si divide in $N$ flussi lenti, ciascuno su una sottoportante: su ogni sottoportante il canale sembra piatto. Nella FDM le bande sono separate da guardie; nell'OFDM si sovrappongono ma restano ortogonali perché gli impulsi sono esponenziali troncati su $T_u$ con spaziatura $\Delta f=1/T_u$, la minima per cui la sinc del prodotto scalare si annulla. In ricezione un banco di correlatori dà $r_i[n]=a_i[n]+w_i[n]$, senza ISI né ICI, con rumore i.i.d.; la PSD è una somma di sinc². Su un canale dispersivo il prefisso ciclico, una copia della coda del blocco lunga almeno quanto la memoria del canale, isola i blocchi e trasforma la convoluzione in circolare: dopo la FFT ogni sottoportante vede un solo coefficiente, $Y_n[k]=H[k]a_k[n]+W_n[k]$, e si equalizza con una divisione (ZF) o con l'MMSE a una presa. Campionando a $T_u/N$ il modulatore diventa una IFFT e il demodulatore una FFT. Il CP costa $L_{cp}/(N+L_{cp})$ di tempo ed energia; i nulli spettrali non si recuperano e si combattono con codifica, interleaving e modulazione adattativa. I limiti dell'OFDM sono il PAPR elevato e la sensibilità agli offset di frequenza (ICI) e di tempo; la scelta di $N$ bilancia overhead, sensibilità all'offset e PAPR. Esempi numerici: Goldsmith 12.2–12.4 e IEEE 802.11a.

## Punti chiave · [[ofdm_goldsmith_slides.pdf#page=2|p. 2]], [[ofdm_goldsmith_slides.pdf#page=7|7]], [[ofdm_goldsmith_slides.pdf#page=11|11]], [[ofdm_goldsmith_slides.pdf#page=12|12]], [[ofdm_goldsmith_slides.pdf#page=16|16]], [[ofdm_goldsmith_slides.pdf#page=18|18]], [[ofdm_goldsmith_slides.pdf#page=21|21]], [[ofdm_goldsmith_slides.pdf#page=24|24]], [[ofdm_goldsmith_slides.pdf#page=26|26]], [[ofdm_goldsmith_slides.pdf#page=30|30]], [[ofdm_goldsmith_slides.pdf#page=33|33]], [[ofdm_goldsmith_slides.pdf#page=38|38]], [[ofdm_goldsmith_slides.pdf#page=40|40]], [[ofdm_goldsmith_slides.pdf#page=43|43]], [[ofdm_goldsmith_slides.pdf#page=44|44]], [[ofdm_goldsmith_slides.pdf#page=48|48]], [[ofdm_goldsmith_slides.pdf#page=54|54]], [[ofdm_goldsmith_slides.pdf#page=56|56]], [[ofdm_goldsmith_slides.pdf#page=58|58]]

1. Multiportante: S/P in $N$ flussi a $R_b/N$; FDM a bande separate, OFDM a bande sovrapposte e ortogonali. L'ortogonalità è una proprietà delle forme d'onda su un intervallo finito.
2. $\phi_i(t)=R_{T_u}(t)e^{j2\pi it/T_u}$, $\Delta f=1/T_u$; $\langle\phi_k(t-mT_u),\phi_i(t-nT_u)\rangle=\delta_{k-i}\delta_{m-n}$.
3. Prodotto scalare con frequenze generiche: $e^{j\pi\nu T_u}\text{sinc}(\nu T_u)$, nullo per $\nu T_u$ intero non nullo; spaziatura minima $1/T_u$.
4. ISI = termini con $n\neq m$; ICI = termini con $n=m$, $k\neq i$. In AWGN ideale $r_i[n]=a_i[n]+w_i[n]$, $w_i[n]\sim\mathcal{CN}(0,N_0)$ indipendenti.
5. Segnale ciclostazionario; $S_{xx}(f)=E_s\sum_i\text{sinc}^2[T_u(f-i/T_u)]$. La sovrapposizione dimezza circa la banda rispetto alla FDM.
6. Canale dispersivo: guardia vuota non basta; prefisso ciclico con $T_g\ge T_h$ ⇒ niente ISI, sottoportanti autofunzioni ⇒ $r_i[n]=H(i/T_u)a_i[n]+w_i[n]$, niente ICI.
7. Campionando a $T_c=T_u/N$: $x_n[q]=\text{IDFT}\{a_i[n]\}$; $\mathbf x_n=\mathbf F_N^H\mathbf a_n$; FFT $O(N\log N)$.
8. A tempo discreto: con $L_{cp}\ge L_h$ la convoluzione diventa circolare e $Y_n[k]=H[k]a_k[n]+W_n[k]$: matrice diagonale.
9. Equalizzazione a una presa: ZF (rumore $N_0/\lvert H[k]\rvert^2$) o LMMSE; il CP non elimina i nulli spettrali ⇒ codifica, interleaving, modulazione adattativa.
10. Prezzo del CP: $\eta_{cp}=N/(N+L_{cp})$; $R_b=N_d\log_2M/(T_u+T_g)$. 802.11a: $T_u=3.2\ \mu$s, $T_g=0.8\ \mu$s, 48 portanti dati, da 12 a 72 Mbit/s non codificati.
11. Limiti: PAPR fino a $N$; offset di frequenza ⇒ ICI con coefficienti $C_m(\epsilon_f)$; offset di tempo dentro il CP ⇒ rampa di fase. $N$ grande: meno overhead, più sensibilità all'offset, più PAPR.

## Concetti introdotti

- [[ofdm]]
- [[prefisso-ciclico]]
- [[ofdm-con-fft]]
- [[equalizzazione-ofdm]]
- [[limiti-dell-ofdm]]
- entità: [[ieee-802-11a]], [[fft]]
- esercizi: [[dimensionamento-ofdm]]

## Domande aperte · [[ofdm_goldsmith_slides.pdf#page=31|p. 31]]

- La slide 26 cita "gli appunti a mano della lezione" con impulsi normalizzati su $T=T_u+T_g$: in questo PDF non ci sono appunti con quella normalizzazione. Quella convenzione è la stessa delle note di Gelli (approfondimento, [[multiportante-ofdm-dmt-gelli]]), che danno $r_i(n)=\frac{T_u}{T}a_i(n)H(i/T_u)$.
- Il PDF non tratta come si stimano in pratica $H[k]$, l'offset di frequenza e il timing in un sistema OFDM (solo l'accenno ai piloti della slide 41 e il rinvio alla stima di canale della slide 39).

## Domande da esame

- Perché un sistema multiportante combatte l'ISI? Che differenza c'è tra FDM e OFDM?
- Scrivi gli impulsi OFDM e dimostra che sono ortonormali. Perché la spaziatura minima è $1/T_u$?
- Che cosa sono ISI e ICI nella statistica di decisione di un sistema multiportante? Quando si annullano?
- Ricava la statistica del rumore all'uscita dei correlatori OFDM.
- Ricava la PSD di un segnale OFDM. Perché il segnale è ciclostazionario?
- Che cos'è il prefisso ciclico? Perché una guardia vuota non basta? Qual è la condizione sulla sua durata?
- Dimostra che con il CP l'uscita del correlatore $i$ è $H(i/T_u)a_i[n]+w_i[n]$.
- Come si realizza l'OFDM con IFFT/FFT? Disegna trasmettitore e ricevitore in banda base.
- Perché il CP trasforma la convoluzione lineare in circolare? Ricava $Y_n[k]=H[k]a_k[n]+W_n[k]$.
- Equalizzazione a una presa: ZF e MMSE. Che succede su un nullo spettrale?
- Quanto costa il CP? Calcola efficienza e bit rate di un sistema dato (esempio 802.11a).
- Che cos'è il PAPR e perché è un problema? Qual è il caso peggiore?
- Perché l'OFDM è sensibile agli offset di frequenza? Che effetto ha un errore di timing dentro il CP?
- Come si sceglie il numero di sottoportanti?

_Aggiornato: 2026-11-27 — creazione (ingest di ofdm_goldsmith_slides.pdf, Lezione 15)_
