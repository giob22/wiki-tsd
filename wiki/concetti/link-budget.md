---
tipo: concetto
importanza_esame: media
prerequisiti: ["parametri-globali-modulazioni", "rumore-in-banda-passante"]
fonti_pdf: ["Confronto_new.pdf#page=24", "Confronto_new.pdf#page=25", "Confronto_new.pdf#page=26", "Confronto_new.pdf#page=27", "Confronto_new.pdf#page=32", "Confronto_new.pdf#page=33"]
---

# Link budget

## Definizione · [[Confronto_new.pdf#page=24|p. 24]], [[Confronto_new.pdf#page=27|27]]

Il **link budget** è il bilancio delle potenze di un collegamento: parte dalla potenza trasmessa, aggiunge i guadagni d'antenna, sottrae le perdite di propagazione e confronta la potenza ricevuta con la **sensibilità** del ricevitore, cioè la minima potenza ricevuta che garantisce la BER richiesta. Serve a ricavare la potenza trasmessa necessaria o, a potenza fissata, la massima distanza raggiungibile.

## Formule · [[Confronto_new.pdf#page=24|p. 24]]–[[Confronto_new.pdf#page=27|27]]

| Formula | Significato |
|---|---|
| $\text{SNR}_{req}=\big(\frac{E_b}{N_0}\big)_{req}\frac{R_b}{W}$ | SNR richiesto dalla BER obiettivo |
| $P_n=N_0W=kT_0\,10^{F/10}\,W$ | potenza di rumore [W] |
| $P_{rx,min}=\text{SNR}_{req}\,P_n$ | sensibilità del ricevitore [W] |
| $P^{\text{dBm}}=10\log_{10}\frac{P}{1\ \text{mW}}$ | potenza in dBm |
| $P_{rx}=P_{tx}G_{tx}G_{rx}\frac{\lambda^2}{(4\pi R)^2}$ | equazione di Friis (spazio libero, LOS) |
| $L_{path,\text{dB}}=P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{margin,\text{dB}}$ | massimo path loss ammissibile [dB] |

> 🧮 Formula chiave: $P_{rx,min,\text{dBm}}=-174+F_{\text{dB}}+10\log_{10}W+\text{SNR}_{req,\text{dB}}$ e $L_{path,\text{dB}}=P_{tx}-P_{rx,min}+G_{tx}+G_{rx}-L_{margin}$.

Simboli: $k=1.38\cdot10^{-23}$ J/K costante di Boltzmann; $T_0=290$ K temperatura di riferimento; $F$ [dB] cifra di rumore del ricevitore ($10^{F/10}$ è la stessa grandezza in scala lineare); $W$ [Hz] banda; $P_{tx}$ [W o dBm] potenza trasmessa; $G_{tx}$, $G_{rx}$ guadagni d'antenna (in dBi: dB rispetto all'antenna isotropa); $\lambda=c/f_c$ [m] lunghezza d'onda; $R$ [m] distanza; $L_{margin}$ [dB] margine di sicurezza.

## Derivazioni

### Derivazione — Potenza di rumore in dBm · [[Confronto_new.pdf#page=25|p. 25]]
**Fonte:** slide 25 dà $P_n=kT_0\,10^{F/10}\,W$; il valore numerico $-174$ dBm/Hz non è sulle slide.

> 🧩 Derivazione mia, utile per tutti i conti in dB.

$$
\begin{aligned}
kT_0&=1.38\cdot10^{-23}\ \tfrac{\text{J}}{\text{K}}\cdot290\ \text{K}=4.0\cdot10^{-21}\ \text{W/Hz} && \text{densità di rumore termico}\\
10\log_{10}\frac{4.0\cdot10^{-21}\ \text{W/Hz}}{10^{-3}\ \text{W}}&=-174\ \text{dBm/Hz} && \text{in dBm per Hz di banda}\\
P_{n,\text{dBm}}&=-174+F_{\text{dB}}+10\log_{10}(W/1\ \text{Hz}) && \text{il prodotto diventa somma in dB}
\end{aligned}
$$

**Sanity check:** con $F=6$ dB e $W=20$ MHz, $10\log_{10}(2\cdot10^7)=73$ dB, quindi $P_n=-174+6+73=-95$ dBm, proprio il valore usato nell'esempio della slide 30 ([[link-budget-wlan]]).

### Derivazione — Sensibilità in dB · [[Confronto_new.pdf#page=24|p. 24]], [[Confronto_new.pdf#page=25|25]]
**Fonte:** procedura della slide 24, formule della slide 25.

$$
\begin{aligned}
\text{SNR}_{req}&=\Big(\frac{E_b}{N_0}\Big)_{req}\frac{R_b}{W} && \text{dalla definizione } \text{SNR}=\tfrac{E_b}{N_0}\eta_B\\
P_{rx,min}&=\text{SNR}_{req}\cdot P_n && \text{serve almeno questo SNR sopra il rumore}\\
P_{rx,min,\text{dBm}}&=P_{n,\text{dBm}}+\Big(\frac{E_b}{N_0}\Big)_{req,\text{dB}}+10\log_{10}\frac{R_b}{W} && \text{in dB i prodotti diventano somme}
\end{aligned}
$$

La sensibilità è un numero **negativo** in dBm (frazioni di mW): più è negativo, migliore è il ricevitore.

### Derivazione — Friis e path loss in dB · [[Confronto_new.pdf#page=26|p. 26]], [[Confronto_new.pdf#page=27|27]]
**Fonte:** slide 26 (Friis) e 27 (formula del path loss, data senza passaggi).

$$
\begin{aligned}
P_{rx}&=P_{tx}\,G_{tx}\,G_{rx}\Big(\frac{\lambda}{4\pi R}\Big)^2 && \text{Friis}\\
P_{rx,\text{dBm}}&=P_{tx,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{fs,\text{dB}},\qquad L_{fs,\text{dB}}=20\log_{10}\frac{4\pi R}{\lambda} && 10\log_{10}\text{ di ogni fattore}\\
P_{rx,\text{dBm}}&\ge P_{rx,min,\text{dBm}}+L_{margin,\text{dB}} && \text{si vuole un margine sopra la sensibilità}\\
L_{fs,\text{dB}}&\le P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{margin,\text{dB}}=L_{path,\text{dB}} && \text{isolo la perdita}\\
R_{max}&=\frac{\lambda}{4\pi}\,10^{L_{path,\text{dB}}/20} && \text{inverto } L_{fs}
\end{aligned}
$$

**Lettura:** in spazio libero la potenza cala con $R^2$. Raddoppiare la distanza costa $20\log_{10}2\approx6$ dB, quindi ogni 6 dB guadagnati (più potenza, antenne migliori, ricevitore più sensibile) raddoppiano la portata.

## Spiegazione · appunti [[Confronto new.pdf#page=27|p. 27]]–[[Confronto new.pdf#page=29|29]]

Il link budget porta i concetti astratti della lezione (capacità, $E_b/N_0$, efficienza spettrale) nel mondo delle potenze in dBm e delle distanze in metri. La catena è:

1. dal bit rate e dalla costellazione si ricava il symbol rate e la banda;
2. la modulazione e la BER obiettivo fissano l'$E_b/N_0$ richiesto;
3. moltiplicando per $\eta_B=R_b/W$ si ottiene l'SNR richiesto;
4. il rumore del ricevitore ($kT_0FW$) dice a quale potenza sta il «pavimento»: la sensibilità è l'SNR richiesto sopra quel pavimento;
5. l'equazione di Friis dice quanta potenza si perde nella propagazione; il path loss massimo tollerabile, tolto un margine, fissa la portata.

**Dagli appunti presi a lezione.** In Friis, $\frac{\lambda^2}{(4\pi R)^2}=\frac{1}{L_{path}}$ è il fattore di attenuazione. Vale per il collegamento ideale in visibilità: il canale radio è «aperto», e in un canale wireless il segnale può arrivare anche tramite riflessioni multiple. $F$ misura la rumorosità del ricevitore; $k$ è la costante di Boltzmann.

**Perché in dB.** Tutte le grandezze si moltiplicano (guadagni, perdite, rapporti), quindi in scala logaritmica si sommano: il bilancio diventa una somma di voci con il loro segno. dBm vuol dire dB rispetto a 1 mW, dBi dB rispetto all'antenna isotropa.

**Il compromesso finale (slide 32).** Costellazioni più dense nella stessa banda aumentano bit rate ed efficienza spettrale, ma alzano l'$E_b/N_0$ richiesto, quindi la sensibilità peggiora (diventa meno negativa) e la portata si riduce. È lo stesso compromesso energia-banda di [[parametri-globali-modulazioni]], tradotto in metri.

> 🎯 Esame: i passi della procedura di link budget, il significato di sensibilità e la sua formula, l'equazione di Friis e la formula del path loss massimo; saper rifare i conti dell'esempio WLAN.

## Perché importa

È il ponte tra teoria e progetto: dice se un collegamento con una certa modulazione, potenza e antenne funziona a una data distanza. L'esempio WLAN mostra come scegliere una modulazione più efficiente in banda riduca la copertura.

## Connessioni

- [[parametri-globali-modulazioni]] — $\text{SNR}=\frac{E_b}{N_0}\eta_B$ e l'$E_b/N_0$ richiesto dalle modulazioni.
- [[rumore-in-banda-passante]] — la potenza di rumore in banda $W$ è $N_0W$.
- [[limite-di-shannon]] — il minimo teorico di $E_b/N_0$, sotto cui nessun link budget può scendere.
- [[link-budget-wlan]] — l'esempio svolto.

## Fonti · [[Confronto_new.pdf#page=24|p. 24]]–[[Confronto_new.pdf#page=27|27]], [[Confronto_new.pdf#page=32|32]], [[Confronto_new.pdf#page=33|33]]

[[parametri-globali-e-capacita]] — Confronto_new.pdf, slide 24–27, 32–33.

_Aggiornato: 2026-11-15 — appunti presi a lezione dalla copia annotata Confronto new.pdf; creazione da ingest Confronto_new.pdf_
