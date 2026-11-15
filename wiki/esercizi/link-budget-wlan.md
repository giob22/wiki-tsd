---
tipo: esercizio
argomento: "link budget: bit rate, sensibilità e portata di un collegamento"
difficoltà: media
---

# Link budget di un collegamento WLAN

## Metodo

Si applica quando, dati modulazione, banda, BER obiettivo, cifra di rumore, potenza e antenne, si chiedono bit rate, sensibilità e portata.

1. **Symbol rate** dalla banda: con impulsi a eccesso di banda $a$ la banda occupata è $R_s(1+a)$, quindi $R_s=W/(1+a)$.
2. **Bit rate**: $R_b=R_s\log_2M$.
3. **$E_b/N_0$ richiesto** dalla curva BER della modulazione.
4. **SNR richiesto**: $\text{SNR}_{req,\text{dB}}=(E_b/N_0)_{req,\text{dB}}+10\log_{10}(R_b/W)$.
5. **Rumore**: $P_{n,\text{dBm}}=-174+F_{\text{dB}}+10\log_{10}W$.
6. **Sensibilità**: $P_{rx,min,\text{dBm}}=P_{n,\text{dBm}}+\text{SNR}_{req,\text{dB}}$.
7. **Path loss massimo**: $L_{path}=P_{tx,\text{dBm}}-P_{rx,min,\text{dBm}}+G_{tx}+G_{rx}-L_{margin}$.
8. **Portata**: $R=\frac{\lambda}{4\pi}10^{L_{path}/20}$ con $\lambda=c/f_c$.

## Formule usate

- [[link-budget]] — sensibilità, Friis, path loss.
- [[parametri-globali-modulazioni]] — $\text{SNR}=\frac{E_b}{N_0}\frac{R_b}{W}$.
- [[variabile-aleatoria-gaussiana]] — $Q(x)=\frac12\text{erfc}(x/\sqrt2)$.

## Casi svolti

### Caso 1 — WLAN a 5 GHz con QPSK · [[Confronto_new.pdf#page=28|p. 28]]–[[Confronto_new.pdf#page=31|31]]

**Traccia.** Portante 5 GHz, banda del canale 20 MHz, QPSK, eccesso di banda $a=0.33$, cifra di rumore $F=6$ dB. Determinare: (1) il bit rate; (2) la sensibilità del ricevitore per BER $=10^{-6}$; (3) la portata con $P_{tx}=100$ mW, $G_{tx}=G_{rx}=2$ dBi e margine 20 dB.

**1. Bit rate.**

$$
\begin{aligned}
R_s&=\frac{W}{1+a}=\frac{20\ \text{MHz}}{1.33}=15.04\cdot10^6\ \text{simboli/s}\approx15\ \text{Msimboli/s} && \text{la banda occupata è } R_s(1+a)\\
R_b&=R_s\log_2M=15\cdot2=30\ \text{Mbit/s} && \text{QPSK: } M=4,\ 2 \text{ bit per simbolo}
\end{aligned}
$$

**2. Sensibilità.** Per QPSK con codifica di Gray $\text{BER}=Q\big(\sqrt{2E_b/N_0}\big)$, con $Q(x)=\frac12\text{erfc}(x/\sqrt2)$ (nota a mano della slide 30).

$$
\begin{aligned}
Q\Big(\sqrt{2E_b/N_0}\Big)&=10^{-6} && \text{BER obiettivo}\\
\sqrt{2E_b/N_0}&=Q^{-1}(10^{-6})\approx4.75 && \text{dalla tabella della } Q\\
\frac{E_b}{N_0}&=\frac{4.75^2}{2}=11.3\ \Rightarrow\ 10.5\ \text{dB} && 10\log_{10}11.3
\end{aligned}
$$

> ⚠️ Contraddizione: la slide 30 usa $(E_b/N_0)_{req}\approx10.2$ dB; dalla formula esatta $Q(\sqrt{2E_b/N_0})=10^{-6}$ risulta circa $10.5$ dB. Per coerenza con la slide i conti seguenti usano $10.2$ dB; con $10.5$ dB tutto si sposta di 0.3 dB (sensibilità $-82.7$ dBm, portata circa 103 m).

$$
\begin{aligned}
\text{SNR}_{req,\text{dB}}&=10.2+10\log_{10}\frac{30}{20}=10.2+1.76\approx12\ \text{dB} && \eta_B=R_b/W=1.5\\
P_{n,\text{dBm}}&=-174+6+10\log_{10}(20\cdot10^6)=-174+6+73=-95\ \text{dBm} && \text{rumore termico più cifra di rumore}\\
P_{rx,min,\text{dBm}}&=-95+12=-83\ \text{dBm} && \text{sensibilità}
\end{aligned}
$$

La slide dà direttamente la potenza di rumore $-95$ dBm; il calcolo con $kT_0$ la conferma ([[link-budget]]).

**3. Portata.**

$$
\begin{aligned}
P_{tx}&=10\log_{10}\frac{100\ \text{mW}}{1\ \text{mW}}=20\ \text{dBm}\\
L_{path}&=20-(-83)+2+2-20=87\ \text{dB} && \text{path loss massimo con margine}\\
\lambda&=\frac{c}{f_c}=\frac{3\cdot10^8\ \text{m/s}}{5\cdot10^9\ \text{Hz}}=0.06\ \text{m}\\
R&=\frac{\lambda}{4\pi}10^{L_{path}/20}=\frac{0.06}{12.57}\cdot10^{4.35}=4.77\cdot10^{-3}\cdot22\,387\approx107\ \text{m} && \text{inverto } 20\log_{10}\tfrac{4\pi R}{\lambda}=87
\end{aligned}
$$

**Risultati:** $R_b=30$ Mbit/s; sensibilità $-83$ dBm; portata circa 107 m in spazio libero.
**Sanity check:** verifica inversa, $20\log_{10}\frac{4\pi\cdot107}{0.06}=20\log_{10}22\,410\approx87$ dB ✓. Bilancio: $P_{rx}=20+2+2-87=-63$ dBm, cioè esattamente 20 dB (il margine) sopra la sensibilità di $-83$ dBm.
**Ipotesi:** propagazione in spazio libero (LOS ideale), AWGN, BER della QPSK ideale senza codifica.

**Osservazione finale (slide 32).** Con 16-QAM o 64-QAM nella stessa banda $R_b$ ed $\eta_B$ salgono, ma l'$E_b/N_0$ richiesto per la stessa BER cresce: $\text{SNR}_{req}$ aumenta per entrambi i motivi, la sensibilità peggiora e, con lo stesso $P_{tx}$, il path loss ammissibile e la portata diminuiscono.

## Trappole

- **dB e dBm**: le potenze assolute sono in dBm, i guadagni e le perdite in dB (o dBi). Sommare dBm a dBm non ha senso, sommare dB a dBm sì.
- **$R_b/W$ e non $R_s/W$** nell'SNR richiesto: l'$E_b/N_0$ è per **bit**.
- **$F$ è in dB**: nella formula lineare compare $10^{F/10}$, in dB si somma direttamente.
- **Il margine si sottrae** dal path loss ammissibile: riduce la portata.
- **Inversione di Friis**: $20\log_{10}$ (non $10\log_{10}$), perché la distanza è al quadrato.

_Aggiornato: 2026-11-15 — creazione da ingest Confronto_new.pdf_
