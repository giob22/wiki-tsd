---
tipo: concetto
importanza_esame: media
prerequisiti: ["spazio-dei-segnali", "inviluppo-complesso"]
fonti_pdf: ["Modulazione.pdf#page=38", "Modulazione.pdf#page=39"]
---

# Modulazione ortogonale (FSK)

## Definizione · [[Modulazione.pdf#page=38|p. 38]]

Nella **modulazione ortogonale** le $M$ forme d'onda sono mutuamente ortogonali, quindi lo spazio dei segnali ha dimensione $n=M$. L'esempio classico è la **FSK** (frequency shift keying), modulazione **non lineare** in cui l'informazione sta nella frequenza: $s_i(t)=e^{j2\pi f_it}g_{TX}(t)$, con spaziature $\lvert f_i-f_k\rvert$ scelte per l'ortogonalità.

## Formule · [[Modulazione.pdf#page=38|p. 38]], [[Modulazione.pdf#page=39|39]]

| Formula | Significato |
|---|---|
| $s_i(t)=e^{j2\pi f_it}g_{TX}(t)$ | forme d'onda FSK in banda base complessa |
| $\langle s_{i,p},s_{k,p}\rangle=\text{Re}\langle s_i,s_k\rangle=0$ | ortogonalità dei segnali passa-banda (sistemi coerenti) |
| $\Delta f_{min}=\frac{1}{2T}$ (coerente), $\frac1T$ (non coerente) | spaziatura minima tra i toni |
| $s(t)=A\sum_ke^{j2\pi\frac{b_k}{2T}(t-kT)}g_{TX}(t-kT)$, $b_k\in\{2i-1-M\}$ | segnale FSK ortogonale |

> 🧮 Formula chiave: spaziatura $\dfrac{1}{2T}$ per la FSK coerente, $\dfrac1T$ per la non coerente.

Simboli: $f_i$ [Hz] frequenza del tono $i$; $T$ [s] durata del simbolo; $\phi_0,\phi_1$ fasi dei due toni.

## Derivazioni

### Derivazione — Spaziatura minima dei toni (esercizio 2.25) · [[Modulazione.pdf#page=39|p. 39]]
**Fonte:** la slide riporta il testo dell'esercizio 2.25 del Madhow: con $\phi_0=\phi_1=0$ la minima separazione è $1/(2T)$, per fasi arbitrarie è $1/T$. La soluzione non è svolta.

> 🧩 Derivazione mia. $s_0=\cos(2\pi f_0t+\phi_0)$, $s_1=\cos(2\pi f_1t+\phi_1)$ su $[0,T]$, $f_1>f_0\gg1/T$, $\Delta f=f_1-f_0$.

$$
\begin{aligned}
\langle s_0,s_1\rangle&=\frac12\int_0^T\cos(2\pi\Delta f\,t+\phi_1-\phi_0)\,dt+\frac12\int_0^T\cos(2\pi(f_0+f_1)t+\phi_0+\phi_1)\,dt && \text{Werner}\\
&\approx\frac12\int_0^T\cos(2\pi\Delta f\,t+\Delta\phi)\,dt && \text{il termine a } f_0+f_1\gg1/T \text{ si annulla}\\
&=\frac{\sin(2\pi\Delta fT+\Delta\phi)-\sin\Delta\phi}{4\pi\Delta f} && \Delta\phi=\phi_1-\phi_0
\end{aligned}
$$

- **Coerente** ($\Delta\phi=0$): $\langle s_0,s_1\rangle=\frac{\sin(2\pi\Delta fT)}{4\pi\Delta f}=0$ per $2\pi\Delta fT=k\pi$: la prima soluzione è $\Delta f=\frac{1}{2T}$.
- **Non coerente** ($\Delta\phi$ qualunque): serve $\sin(2\pi\Delta fT+\Delta\phi)=\sin\Delta\phi$ per ogni $\Delta\phi$, cioè $2\pi\Delta fT=2\pi k$: la prima soluzione è $\Delta f=\frac1T$.

**Sanity check:** nel segnale della slide le frequenze sono $b_k/(2T)$ con $b_k$ dispari e passo 2: toni distanti $2\cdot\frac{1}{2T}=\frac1T$. Con $\frac{1}{2T}$ si risparmia metà banda, ma serve un riferimento di fase accurato.

## Spiegazione · appunti [[Modulazione.pdf#page=38|p. 38]], [[Modulazione.pdf#page=39|39]]

Nelle modulazioni lineari i punti della costellazione stanno in poche dimensioni (1 o 2). Nella modulazione ortogonale ogni segnale ha la **sua** dimensione: con la FSK, un tono diverso per ogni simbolo. I segnali sono tutti alla stessa distanza $\sqrt{2E_s}$ l'uno dall'altro, e aumentando $M$ la distanza non si riduce: per questo le ortogonali sono **efficienti in potenza**. Il prezzo è la banda, che cresce con $M$ perché servono $M$ toni distanziati di almeno $1/(2T)$.

**Coerente o non coerente.** Se il ricevitore conosce la fase della portante (sistema coerente) basta che la parte reale del prodotto scalare sia nulla, e la spaziatura minima è $1/(2T)$. Se non la conosce, i segnali devono essere ortogonali per qualunque fase, e la spaziatura raddoppia a $1/T$.

> 🎯 Esame: definizione di modulazione ortogonale, FSK come esempio non lineare, condizione di ortogonalità $\text{Re}\langle s_i,s_k\rangle=0$, spaziature $1/(2T)$ e $1/T$.

## Perché importa

È l'esempio di modulazione a dimensionalità crescente con $M$: nel confronto delle modulazioni ([[parametri-globali-modulazioni]]) e nel piano di Shannon ([[limite-di-shannon]]) occupa la regione limitata in potenza.

## Connessioni

- [[spazio-dei-segnali]] — dimensione $n=M$.
- [[inviluppo-complesso]] — $\langle u_p,v_p\rangle=\text{Re}\langle u,v\rangle$, da cui la condizione di ortogonalità sugli inviluppi.
- [[probabilita-errore-binaria]] — ortogonale binaria, $P(e)=\frac12\text{erfc}\sqrt{E_s/(2N_0)}$.
- [[probabilita-errore-m-aria]] — union bound per $M$ ortogonali.

## Fonti · [[Modulazione.pdf#page=38|p. 38]], [[Modulazione.pdf#page=39|39]]

[[principles-of-modulation]] — Modulazione.pdf, slide 22–23.

_Aggiornato: 2026-11-16 — creazione da ingest Modulazione.pdf_
