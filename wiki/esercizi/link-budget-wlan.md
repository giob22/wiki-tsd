---
tipo: esercizio
argomento: "link budget: bit rate, sensibilità e portata di un collegamento"
difficoltà: media
---

# Link budget di un collegamento WLAN

## Metodo · [[Confronto_new.pdf#page=24|p. 24]]–[[Confronto_new.pdf#page=27|27]]

Si applica quando, dati modulazione, banda, BER obiettivo, cifra di rumore, potenza e antenne, si chiedono bit rate, sensibilità e portata. L'idea è una catena: **dalla banda si ricava quanto si trasmette, dalla BER quanto il segnale deve stare sopra il rumore, da Friis quanto lontano si può arrivare.**

1. **Symbol rate** dalla banda: con impulsi a eccesso di banda $a$ la banda occupata è $R_s(1+a)$, quindi $R_s=W/(1+a)$.
2. **Bit rate**: $R_b=R_s\log_2M$.
3. **$E_b/N_0$ richiesto** dalla formula (o dalla curva) della BER della modulazione.
4. **SNR richiesto**: $\text{SNR}_{req,\text{dB}}=(E_b/N_0)_{req,\text{dB}}+10\log_{10}(R_b/W)$.
5. **Rumore**: $P_{n,\text{dBm}}=-174+F_{\text{dB}}+10\log_{10}W$.
6. **Sensibilità**: $P_{rx,min,\text{dBm}}=P_{n,\text{dBm}}+\text{SNR}_{req,\text{dB}}$.
7. **Path loss massimo**: $L_{path,\text{dB}}=P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{margin,\text{dB}}$.
8. **Portata**: $R=\frac{\lambda}{4\pi}10^{L_{path,\text{dB}}/20}$ con $\lambda=c/f_c$.

## Formule usate

- [[link-budget]] — rumore, sensibilità, Friis, path loss.
- [[parametri-globali-modulazioni]] — $\text{SNR}=\frac{E_b}{N_0}\frac{R_b}{W}$.
- [[criterio-di-nyquist]] — banda occupata da impulsi a coseno rialzato, $R_s(1+a)$.
- [[variabile-aleatoria-gaussiana]] — $Q(x)=\frac12\text{erfc}(x/\sqrt2)$.

## Casi svolti

### Caso 1 — WLAN a 5 GHz con QPSK · [[Confronto_new.pdf#page=28|p. 28]]–[[Confronto_new.pdf#page=31|31]]

**Traccia.** Portante $f_c=5$ GHz, banda del canale $W=20$ MHz, QPSK, eccesso di banda $a=0.33$, cifra di rumore $F=6$ dB. Determinare:
1. il bit rate;
2. la sensibilità del ricevitore per BER $=10^{-6}$;
3. la portata con $P_{tx}=100$ mW, $G_{tx}=G_{rx}=2$ dBi e margine di 20 dB.

**Dati in ordine d'uso.**

| Simbolo | Valore | Significato |
|---|---|---|
| $W$ | 20 MHz | banda del canale |
| $a$ | 0.33 | eccesso di banda degli impulsi |
| $M$ | 4 | QPSK: 4 simboli, 2 bit per simbolo |
| BER | $10^{-6}$ | probabilità d'errore sul bit voluta |
| $F$ | 6 dB | cifra di rumore del ricevitore |
| $P_{tx}$ | 100 mW | potenza trasmessa |
| $G_{tx},\,G_{rx}$ | 2 dBi | guadagni delle antenne |
| $L_{margin}$ | 20 dB | margine di sicurezza |
| $f_c$ | 5 GHz | portante, serve per $\lambda$ |

#### Passo 1 — Symbol rate · [[Confronto_new.pdf#page=29|p. 29]]

Gli impulsi con eccesso di banda $a$ occupano una banda **più larga** del minimo di Nyquist: in banda passante la banda occupata è $R_s(1+a)$. Il canale ha 20 MHz, quindi il massimo symbol rate che ci sta è quello che la riempie tutta.

$$
\begin{aligned}
W&=R_s(1+a) && \text{banda occupata = banda del canale}\\
R_s&=\frac{W}{1+a} && \text{isolo } R_s\\
&=\frac{20\cdot10^6\ \text{Hz}}{1.33}=15.04\cdot10^6\ \text{simboli/s}\approx15\ \text{Msimboli/s} && \text{sostituisco}
\end{aligned}
$$

#### Passo 2 — Bit rate · [[Confronto_new.pdf#page=29|p. 29]]

Ogni simbolo QPSK porta $\log_2M=\log_24=2$ bit.

$$
R_b=R_s\log_2M=15\cdot10^6\ \tfrac{\text{simboli}}{\text{s}}\cdot2\ \tfrac{\text{bit}}{\text{simbolo}}=30\ \text{Mbit/s}
$$

**Risultato (1):** $R_b=30$ Mbit/s. L'efficienza spettrale è $\eta_B=R_b/W=30/20=1.5$ bit/s/Hz, servirà al passo 4.

#### Passo 3 — $E_b/N_0$ richiesto · [[Confronto_new.pdf#page=30|p. 30]]

Per la QPSK con codifica di Gray la BER è $Q\big(\sqrt{2E_b/N_0}\big)$ (nota a mano della slide 30: $Q(x)=\frac12\text{erfc}(x/\sqrt2)$). Si impone la BER voluta e si risolve per $E_b/N_0$.

$$
\begin{aligned}
Q\Big(\sqrt{2E_b/N_0}\Big)&=10^{-6} && \text{BER obiettivo}\\
\sqrt{2E_b/N_0}&=Q^{-1}(10^{-6})\approx4.75 && \text{dalla tabella della } Q\\
\frac{E_b}{N_0}&=\frac{4.75^2}{2}=11.3 && \text{elevo al quadrato e divido per 2}\\
\Big(\frac{E_b}{N_0}\Big)_{\text{dB}}&=10\log_{10}11.3\approx10.5\ \text{dB} && \text{in dB}
\end{aligned}
$$

> ⚠️ Contraddizione: la slide 30 usa $(E_b/N_0)_{req}\approx10.2$ dB; dalla formula esatta risulta circa $10.5$ dB. Per seguire la slide i conti che seguono usano $10.2$ dB; alla fine c'è la variante con $10.5$ dB, che sposta tutto di 0.3 dB.

#### Passo 4 — SNR richiesto · [[Confronto_new.pdf#page=24|p. 24]], [[Confronto_new.pdf#page=30|30]]

Il ricevitore non «vede» $E_b/N_0$, vede il rapporto tra la potenza del segnale e la potenza del rumore nella sua banda. Il legame è:

$$
\begin{aligned}
\text{SNR}&=\frac{P}{P_n} && \text{definizione}\\
&=\frac{E_bR_b}{N_0W} && P=E_bR_b \text{ (energia per bit × bit al secondo)},\ P_n=N_0W\\
&=\frac{E_b}{N_0}\cdot\frac{R_b}{W} && \text{separo i due rapporti}\\
\text{SNR}_{\text{dB}}&=\Big(\frac{E_b}{N_0}\Big)_{\text{dB}}+10\log_{10}\frac{R_b}{W} && \text{in dB il prodotto diventa somma}\\
\text{SNR}_{req,\text{dB}}&=10.2+10\log_{10}1.5=10.2+1.76\approx12\ \text{dB} && \text{sostituisco}
\end{aligned}
$$

Il segnale deve stare **12 dB sopra il rumore**, cioè avere una potenza circa $10^{1.2}\approx16$ volte quella del rumore.

#### Passo 5 — Potenza di rumore · [[Confronto_new.pdf#page=25|p. 25]], [[Confronto_new.pdf#page=30|30]]

La slide dà direttamente $P_n=-95$ dBm. Si ricava da $P_n=kT_0\,10^{F/10}\,W$ (slide 25):

$$
\begin{aligned}
kT_0&=1.38\cdot10^{-23}\ \tfrac{\text{J}}{\text{K}}\cdot290\ \text{K}=4.0\cdot10^{-21}\ \text{W/Hz} && \text{rumore termico per Hz}\\
10\log_{10}\frac{4.0\cdot10^{-21}\ \text{W/Hz}}{10^{-3}\ \text{W}}&=-174\ \text{dBm/Hz} && \text{in dBm per Hz}\\
P_{n,\text{dBm}}&=-174+F_{\text{dB}}+10\log_{10}W && \text{prodotto} \to \text{somma}\\
&=-174+6+10\log_{10}(2\cdot10^7)=-174+6+73=-95\ \text{dBm} && \text{sostituisco}
\end{aligned}
$$

#### Passo 6 — Sensibilità · [[Confronto_new.pdf#page=25|p. 25]], [[Confronto_new.pdf#page=30|30]]

La sensibilità è la **minima potenza che deve arrivare** al ricevitore perché la BER sia quella voluta: il rumore più l'SNR richiesto.

$$
\begin{aligned}
P_{rx,min}&=\text{SNR}_{req}\cdot P_n && \text{slide 25}\\
P_{rx,min,\text{dBm}}&=P_{n,\text{dBm}}+\text{SNR}_{req,\text{dB}} && \text{in dB}\\
&=-95+12=-83\ \text{dBm} && \text{sostituisco}
\end{aligned}
$$

**Risultato (2):** sensibilità $-83$ dBm, cioè $10^{-8.3}$ mW $\approx5\cdot10^{-9}$ mW. È negativa perché è una frazione minuscola di milliwatt.

#### Passo 7 — Da Friis alla formula del path loss massimo · [[Confronto_new.pdf#page=26|p. 26]], [[Confronto_new.pdf#page=27|27]] · appunti [[Confronto new.pdf#page=28|p. 28]], [[Confronto new.pdf#page=29|29]]

La slide 27 scrive la formula del path loss massimo senza passaggi. Si ricava da Friis in quattro mosse.

**(a) Friis con il path loss.** Gli appunti chiamano $\frac{\lambda^2}{(4\pi R)^2}=\frac{1}{L_{path}}$ il fattore di attenuazione, quindi $L_{path}=\big(\frac{4\pi R}{\lambda}\big)^2$ è **quante volte** la potenza si riduce nel tragitto.

$$
P_{rx}=P_{tx}\,G_{tx}\,G_{rx}\,\frac{\lambda^2}{(4\pi R)^2}=\frac{P_{tx}\,G_{tx}\,G_{rx}}{L_{path}}
$$

**(b) Passo in dB.** Divido entrambi i membri per 1 mW e prendo $10\log_{10}$. Il logaritmo trasforma prodotti in somme e divisioni in differenze:

$$
\begin{aligned}
10\log_{10}\frac{P_{rx}}{1\ \text{mW}}&=10\log_{10}\frac{P_{tx}}{1\ \text{mW}}+10\log_{10}G_{tx}+10\log_{10}G_{rx}-10\log_{10}L_{path} && \log(ab/c)=\log a+\log b-\log c\\
P_{rx,\text{dBm}}&=P_{tx,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{path,\text{dB}} && \text{nomi delle grandezze in dB}
\end{aligned}
$$

Solo le potenze sono in dBm, perché solo loro sono state divise per 1 mW. Guadagni e path loss sono **rapporti** puri: in dB (dBi per le antenne, cioè rispetto all'antenna isotropa).

**(c) La condizione di funzionamento con il margine.** Serve $P_{rx}\ge P_{rx,min}$ (slide 27). Per stare tranquilli si chiede di più: almeno $L_{margin}$ dB **sopra** la sensibilità, per coprire attenuazioni impreviste (ostacoli, riflessioni, componenti peggiori del previsto).

$$
P_{rx,\text{dBm}}\ge P_{rx,min,\text{dBm}}+L_{margin,\text{dB}}
$$

**(d) Sostituisco (b) in (c) e isolo il path loss.**

$$
\begin{aligned}
P_{tx,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{path,\text{dB}}&\ge P_{rx,min,\text{dBm}}+L_{margin,\text{dB}} && \text{(b) dentro (c)}\\
-L_{path,\text{dB}}&\ge P_{rx,min,\text{dBm}}+L_{margin,\text{dB}}-P_{tx,\text{dBm}}-G_{tx,\text{dBi}}-G_{rx,\text{dBi}} && \text{porto tutto il resto a destra}\\
L_{path,\text{dB}}&\le P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx,\text{dBi}}+G_{rx,\text{dBi}}-L_{margin,\text{dB}} && \text{cambio segno, la disuguaglianza si gira}
\end{aligned}
$$

Il valore più grande ammesso, con l'uguale, è la formula della slide 27.

**Lettura dei segni.** Il path loss tollerabile **cresce** se aumento la potenza trasmessa o i guadagni d'antenna, e se la sensibilità è più bassa (più negativa: $-P_{rx,min}$ diventa più grande). **Diminuisce** con il margine, che è potenza tenuta da parte e non spesa per la distanza.

> 💡 Connessione: la stessa disuguaglianza, risolta per $P_{tx}$ invece che per $L_{path}$, dà la **minima potenza trasmessa** per coprire una distanza data, $P_{tx,\text{dBm}}\ge P_{rx,min,\text{dBm}}+L_{margin,\text{dB}}+L_{path,\text{dB}}-G_{tx,\text{dBi}}-G_{rx,\text{dBi}}$: è l'altro uso che la slide 27 indica.

#### Passo 8 — Path loss massimo con i numeri · [[Confronto_new.pdf#page=31|p. 31]]

$$
\begin{aligned}
P_{tx,\text{dBm}}&=10\log_{10}\frac{100\ \text{mW}}{1\ \text{mW}}=10\log_{10}100=20\ \text{dBm} && \text{potenza in dBm}\\
L_{path,\text{dB}}&=20-(-83)+2+2-20 && \text{formula del passo 7}\\
&=20+83+4-20=87\ \text{dB} && \text{il meno davanti a } -83 \text{ diventa } +83
\end{aligned}
$$

Il segnale può perdere al massimo 87 dB nel tragitto, cioè ridursi di un fattore $10^{8.7}\approx5\cdot10^8$.

#### Passo 9 — Dal path loss alla distanza · [[Confronto_new.pdf#page=31|p. 31]]

Gli appunti della slide 27 legano il path loss alla distanza: $L_{path}=\big(\frac{4\pi R}{\lambda}\big)^2$. Si inverte per $R$.

$$
\begin{aligned}
\lambda&=\frac{c}{f_c}=\frac{3\cdot10^8\ \text{m/s}}{5\cdot10^9\ \text{Hz}}=0.06\ \text{m} && \text{lunghezza d'onda}\\
L_{path,\text{dB}}&=10\log_{10}\Big(\frac{4\pi R}{\lambda}\Big)^2=20\log_{10}\frac{4\pi R}{\lambda} && \text{il quadrato porta fuori un 2}\\
\frac{4\pi R}{\lambda}&=10^{L_{path,\text{dB}}/20}=10^{87/20}=10^{4.35}=22\,387 && \text{tolgo il logaritmo}\\
R&=\frac{\lambda}{4\pi}\,10^{L_{path,\text{dB}}/20}=\frac{0.06\ \text{m}}{12.57}\cdot22\,387 && \text{isolo } R\\
&=4.77\cdot10^{-3}\ \text{m}\cdot22\,387\approx107\ \text{m} && \text{sostituisco}
\end{aligned}
$$

**Risultato (3):** portata circa 107 m in spazio libero.

#### Verifica

- **Inversa:** $20\log_{10}\frac{4\pi\cdot107}{0.06}=20\log_{10}22\,410\approx87$ dB ✓.
- **Bilancio completo:** a 107 m arrivano $P_{rx}=20+2-87+2=-63$ dBm, esattamente 20 dB (il margine) sopra la sensibilità di $-83$ dBm. È il disegno del bilancio di potenza della Lezione 12 sul sito.
- **Ordine di grandezza:** un access point Wi-Fi a 5 GHz copre decine di metri all'aperto senza ostacoli; 107 m è plausibile.

**Variante con $(E_b/N_0)_{req}=10.5$ dB (valore esatto).** $\text{SNR}_{req}=10.5+1.76\approx12.3$ dB, sensibilità $-95+12.3=-82.7$ dBm, $L_{path}=20+82.7+4-20=86.7$ dB, $R=4.77\cdot10^{-3}\cdot10^{86.7/20}\approx104$ m. Cambia poco: 0.3 dB in più di SNR costano circa il 3% della portata.

**Ipotesi:** propagazione in spazio libero (collegamento LOS ideale, Friis), rumore AWGN, BER della QPSK ideale senza codifica, banda del canale tutta occupata dagli impulsi.

**Osservazione finale (slide 32).** Con 16-QAM o 64-QAM nella stessa banda $R_b$ ed $\eta_B$ salgono, ma l'$E_b/N_0$ richiesto per la stessa BER cresce: $\text{SNR}_{req}$ aumenta per entrambi i motivi, la sensibilità peggiora e, con lo stesso $P_{tx}$, il path loss ammissibile e la portata diminuiscono.

## Trappole

- **dB e dBm**: le potenze assolute sono in dBm, i guadagni e le perdite in dB (o dBi). Sommare dBm a dBm non ha senso, sommare dB a dBm sì.
- **$R_b/W$ e non $R_s/W$** nell'SNR richiesto: l'$E_b/N_0$ è per **bit**.
- **$F$ è in dB**: nella formula lineare compare $10^{F/10}$, in dB si somma direttamente.
- **Il segno della sensibilità**: nella formula compare $-P_{rx,min}$, e con $P_{rx,min}=-83$ dBm diventa $+83$.
- **Il margine si sottrae** dal path loss ammissibile: riduce la portata.
- **Inversione di Friis**: $20\log_{10}$ (non $10\log_{10}$), perché la distanza è al quadrato.

_Aggiornato: 2026-11-22 — esercizio riscritto passo per passo, con la derivazione della formula del path loss massimo da Friis e la variante a 10.5 dB; 2026-11-15 — creazione da ingest Confronto_new.pdf_
