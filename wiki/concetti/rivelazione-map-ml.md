---
tipo: concetto
importanza_esame: alta
prerequisiti: ["spazio-dei-segnali", "processo-gaussiano", "probabilita-totale-e-bayes"]
fonti_pdf: ["Detection.pdf#page=1", "Detection.pdf#page=10", "Detection.pdf#page=11", "Detection.pdf#page=12", "Detection.pdf#page=13", "Detection.pdf#page=14"]
---

# Rivelazione: criteri MAP e ML

## Definizione · [[Detection.pdf#page=10|p. 10]]–[[Detection.pdf#page=12|12]]

La **rivelazione** (detection) simbolo a simbolo è il problema di decidere quale tra le $M$ forme d'onda possibili è stata trasmessa, osservando il segnale ricevuto $r(t)=s(t;\xi)+n(t)$ in un intervallo di simbolo, con $n(t)$ rumore AWGN. Proiettando $r(t)$ su una base ortonormale il problema diventa un **test di ipotesi** su vettori. La regola che minimizza la probabilità d'errore è il criterio **MAP** (massima probabilità a posteriori); con simboli equiprobabili diventa il criterio **ML** (massima verosimiglianza).

## Formule · [[Detection.pdf#page=11|p. 11]]–[[Detection.pdf#page=14|14]]

| Formula | Significato |
|---|---|
| $H_0:\ r(t)=n(t)$, $H_1:\ r(t)=s(t)+n(t)$ | ipotesi della modulazione on-off (I.2) |
| $n_i\sim\mathcal N(0,N_0/2)$ indipendenti | proiezioni del rumore bianco |
| $\Lambda(r)=\frac{f_{r_1\mid H_1}(r)}{f_{r_1\mid H_0}(r)}\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \frac qp$ | criterio MAP binario (I.4)–(I.7) |
| $\lambda(r)=\frac{2}{N_0}\int_0^{T_b}r(t)s(t)dt-\frac{E_s}{N_0}\ \gtrless\ \ln\frac qp$ | log-verosimiglianza (I.9)–(I.10) |
| $p_kf_{\mathbf r\mid H_k}(\mathbf r)=\max_ip_if_{\mathbf r\mid H_i}(\mathbf r)$ | MAP M-ario (II.3)–(II.4) |
| $\lambda_k(\mathbf r)=\mathbf r^T\mathbf s^{(k)}-\frac12\lVert\mathbf s^{(k)}\rVert^2$ | statistica ML (II.10) |

> 🧮 Formula chiave: decidere $H_k$ che massimizza $\lambda_k=\langle r(t),s_k(t)\rangle-\tfrac12E_{s,k}$ (ML in AWGN).

Simboli: $p=P(m_1)$, $q=P(m_0)$ probabilità a priori; $E_s$ [J] energia del segnale; $N_0/2$ [W/Hz] PSD del rumore; $r_i$, $n_i$ proiezioni sulle funzioni di base $\psi_i$; $Z_k$ regioni di decisione.

## Derivazioni

### Derivazione — Proiezioni del rumore bianco · [[Detection.pdf#page=11|p. 11]], [[Detection.pdf#page=3|p. 3]]
**Fonte:** dispense p. 3 e appunti p. 3.

$$
\begin{aligned}
E[n_i]&=\int_0^{T_b}E[n(t)]\,\psi_i(t)\,dt=0 && \text{media nulla}\\
E[n_in_j]&=\int_0^{T_b}\!\!\int_0^{T_b}E[n(t)n(u)]\,\psi_i(t)\psi_j(u)\,dt\,du && \text{scambio media e integrali}\\
&=\frac{N_0}{2}\int_0^{T_b}\!\!\int_0^{T_b}\delta(t-u)\,\psi_i(t)\psi_j(u)\,dt\,du=\frac{N_0}{2}\int_0^{T_b}\psi_i(t)\psi_j(t)\,dt=\frac{N_0}{2}\delta_{ij} && R_{nn}(\tau)=\tfrac{N_0}{2}\delta(\tau)\text{, ortonormalità}
\end{aligned}
$$

Le $n_i$ sono combinazioni lineari di un processo gaussiano, quindi congiuntamente gaussiane; essendo incorrelate sono **indipendenti** ([[processo-gaussiano]]).

### Derivazione — Criterio MAP (I.3)–(I.4) · [[Detection.pdf#page=12|p. 12]], [[Detection.pdf#page=4|p. 4]]
**Fonte:** dispense p. 4 e appunti p. 4.

$$
\begin{aligned}
P(e)&=P(\hat m_0\mid m_1)P(m_1)+P(\hat m_1\mid m_0)P(m_0) && \text{probabilità totale}\\
&=p\int_{Z_0}f_{\mathbf r\mid H_1}d\mathbf r+q\int_{Z_1}f_{\mathbf r\mid H_0}d\mathbf r && \text{errore = cadere nella regione sbagliata}\\
&=p\Big(1-\int_{Z_1}f_{\mathbf r\mid H_1}d\mathbf r\Big)+q\int_{Z_1}f_{\mathbf r\mid H_0}d\mathbf r && Z_0=\mathbb R^N-Z_1\text{, la pdf ha area 1}\\
&=p-\int_{Z_1}\big[p\,f_{\mathbf r\mid H_1}-q\,f_{\mathbf r\mid H_0}\big]d\mathbf r
\end{aligned}
$$

Per renderla minima si mette in $Z_1$ ogni punto in cui l'integranda è positiva: $p\,f_{\mathbf r\mid H_1}>q\,f_{\mathbf r\mid H_0}$, cioè $\frac{f_{\mathbf r\mid H_1}}{f_{\mathbf r\mid H_0}}>\frac qp$. Per Bayes $p\,f_{\mathbf r\mid H_1}\propto P(H_1\mid\mathbf r)$: si sceglie l'ipotesi con la **probabilità a posteriori** maggiore, da cui il nome MAP.

### Derivazione — Teorema dell'irrilevanza (I.5) · [[Detection.pdf#page=12|p. 12]], [[Detection.pdf#page=4|p. 4]]
**Fonte:** dispense p. 4 e appunti p. 4.

$$
\frac{f_{\mathbf r_N\mid H_1}}{f_{\mathbf r_N\mid H_0}}=\frac{f_{r_1\mid H_1}(r_1)\,f_{n_2}(r_2)\cdots f_{n_N}(r_N)}{f_{r_1\mid H_0}(r_1)\,f_{n_2}(r_2)\cdots f_{n_N}(r_N)}=\frac{f_{r_1\mid H_1}(r_1)}{f_{r_1\mid H_0}(r_1)}
$$

Le componenti sono indipendenti e, da $i=2$ in poi, sono solo rumore con la stessa pdf nelle due ipotesi: i fattori si semplificano. $(r_2,\dots,r_N)$ sono irrilevanti, $r_1$ è la **statistica sufficiente**.

### Derivazione — Rapporto di verosimiglianza gaussiano (I.8)–(I.9) · [[Detection.pdf#page=12|p. 12]], [[Detection.pdf#page=13|13]], [[Detection.pdf#page=5|p. 5]]
**Fonte:** dispense p. 4–5 e appunti p. 5.

$$
\begin{aligned}
\Lambda(r)&=\frac{\frac{1}{\sqrt{\pi N_0}}e^{-(r-\sqrt{E_s})^2/N_0}}{\frac{1}{\sqrt{\pi N_0}}e^{-r^2/N_0}}=\exp\Big\{-\frac{(r-\sqrt{E_s})^2-r^2}{N_0}\Big\} && r_1\sim\mathcal N(\sqrt{E_s},\tfrac{N_0}{2})\text{ o }\mathcal N(0,\tfrac{N_0}{2})\\
&=\exp\Big\{-\frac{1}{N_0}\big(E_s-2r\sqrt{E_s}\big)\Big\} && \text{sviluppo del quadrato}\\
\lambda(r)&=\ln\Lambda=\frac{2\sqrt{E_s}}{N_0}r-\frac{E_s}{N_0} && \text{logaritmo}\\
\sqrt{E_s}\,r&=\sqrt{E_s}\int_0^{T_b}r(t)\frac{s(t)}{\sqrt{E_s}}dt=\int_0^{T_b}r(t)s(t)\,dt && \psi_1=s/\sqrt{E_s}
\end{aligned}
$$

### Derivazione — Rapporto di verosimiglianza M-ario (II.9)–(II.11) · [[Detection.pdf#page=14|p. 14]], [[Detection.pdf#page=15|15]], [[Detection.pdf#page=7|p. 7]]
**Fonte:** dispense p. 6–7 e appunti p. 7.

$$
\begin{aligned}
\Lambda_k(\mathbf r)&=\frac{\exp\{-\frac{1}{N_0}(\mathbf r-\mathbf s^{(k)})^T(\mathbf r-\mathbf s^{(k)})\}}{\exp\{-\frac{1}{N_0}\mathbf r^T\mathbf r\}} && \text{gaussiane, covarianza } \tfrac{N_0}{2}\mathbf I\\
&=\exp\Big\{\frac{2}{N_0}\mathbf r^T\mathbf s^{(k)}-\frac{1}{N_0}(\mathbf s^{(k)})^T\mathbf s^{(k)}\Big\} && \mathbf r^T\mathbf r \text{ si cancella; } (\mathbf s^{(k)})^T\mathbf r=\mathbf r^T\mathbf s^{(k)} \text{ (scalare)}\\
\lambda_k&=\frac{N_0}{2}\ln\Lambda_k=\mathbf r^T\mathbf s^{(k)}-\frac12(\mathbf s^{(k)})^T\mathbf s^{(k)} && \text{tolgo il fattore comune } \tfrac{2}{N_0}\\
&=\int_0^Tr(t)s_k(t)\,dt-\frac12E_{s,k} && \text{conservazione del prodotto scalare}
\end{aligned}
$$

## Spiegazione · appunti [[Detection.pdf#page=2|p. 2]]–[[Detection.pdf#page=7|7]]

Il ricevitore vede una forma d'onda rumorosa e deve indovinare il simbolo. Il ragionamento segue tre passi.

1. **Dai segnali ai vettori.** Si sceglie una base ortonormale la cui prima funzione è il segnale stesso normalizzato (nel caso M-ario, una base dello spazio dei segnali con Gram-Schmidt). Il segnale vive tutto nelle prime $L$ coordinate; il rumore bianco ha componenti in **tutte** le infinite coordinate, indipendenti e con la stessa varianza $N_0/2$.
2. **Buttare via l'inutile.** Le coordinate fuori dallo spazio dei segnali contengono solo rumore indipendente da tutto il resto: non aiutano a decidere (**irrilevanza**). Bastano le $L$ proiezioni sullo spazio dei segnali: le **statistiche sufficienti**.
3. **Decidere bene.** Si dividono le possibili osservazioni in regioni, una per ipotesi, in modo da sbagliare il meno possibile. Il risultato è il **MAP**: si sceglie l'ipotesi più probabile dato ciò che si è osservato. Richiede di conoscere le probabilità a priori e $N_0$. Se i simboli sono equiprobabili, le probabilità a priori si semplificano e resta l'**ML**, che non dipende da $N_0$: per questo, anche se è ottimo solo con simboli equiprobabili, è il più usato in pratica.

> 🎯 Esame: formulazione del problema (ipotesi, base ortonormale con $\psi_1=s/\lVert s\rVert$), statistica del rumore proiettato, derivazione del criterio MAP da $P(e)$, teorema dell'irrilevanza, rapporto di verosimiglianza gaussiano, differenza MAP/ML, caso M-ario.

## Perché importa

È la base di tutto il ricevitore: dal criterio ML discendono il ricevitore a correlatori o a filtri adattati e la regola a minima distanza ([[ricevitore-ottimo-awgn]]), e da questa le probabilità d'errore delle modulazioni ([[probabilita-errore-binaria]], [[probabilita-errore-m-aria]]).

## Connessioni

- [[spazio-dei-segnali]] — base ortonormale e Gram-Schmidt.
- [[processo-gaussiano]] — proiezioni gaussiane incorrelate quindi indipendenti.
- [[probabilita-totale-e-bayes]] — $P(e)$ come somma pesata e probabilità a posteriori.
- [[rumore-in-banda-passante]] — perché il rumore bianco è un modello lecito se il ricevitore filtra.
- [[ricevitore-ottimo-awgn]] — come si realizza il criterio ML.

## Fonti · [[Detection.pdf#page=1|p. 1]]–[[Detection.pdf#page=7|7]], [[Detection.pdf#page=10|10]]–[[Detection.pdf#page=15|15]]

[[elementi-teoria-rivelazione]] — Detection.pdf, dispense p. 1–7 e appunti.

_Aggiornato: 2026-11-16 — creazione da ingest Detection.pdf_
