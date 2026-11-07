---
tipo: fonte
titolo: "Representation of passband random processes (rappresentazione dei processi aleatori passa-banda)"
file_raw: "Rappresentazione_Rice_processi.pdf"
pagine: "1-25"
data_ingest: 2026-11-01
formato: slide-pdf
argomenti: [processi passa-banda, processo analitico, inviluppo complesso di un processo, componenti in fase e quadratura, WSS congiunta, trasformata di Hilbert, PSD delle componenti, simmetria attorno alla portante, incoerenza, rumore in banda passante]
---

# Representation of passband random processes — Rappresentazione_Rice_processi.pdf

## Sommario · [[Rappresentazione_Rice_processi.pdf#page=1|p. 1]], [[Rappresentazione_Rice_processi.pdf#page=2|2]]

Slide in inglese (13) con **12 pagine di appunti a mano** della docente Donatella Darsena (a.a. 2026-27). È il seguito della lezione sulla rappresentazione complessa in banda base ([[rappresentazione-complessa-banda-base]]): le stesse idee (segnale analitico, inviluppo complesso, componenti in fase e quadratura) vengono riprese per i **processi aleatori**, cioè per segnali di informazione e rumore che non si conoscono a priori.

Il discorso, per un processo reale $x_p(t)$ WSS, a media nulla e passa-banda:
1. si costruisce il **processo analitico** $x_p^+ = \frac{1}{\sqrt2}x_p + \frac{j}{\sqrt2}\widehat{x}_p$ con il filtro di Hilbert;
2. lo si trasla in banda base e si ottiene l'**inviluppo complesso** $x = x_c + jx_s$, con le componenti reali $x_c$ (in fase) e $x_s$ (in quadratura);
3. si dimostra che, se $x_p$ è WSS a media nulla, $x_c$ e $x_s$ sono **congiuntamente WSS** a media nulla, con $R_{x_cx_c} = R_{x_sx_s}$ e $R_{x_cx_s} = -R_{x_sx_c}$; la dimostrazione passa per le relazioni tra $x_p$ e la sua trasformata di Hilbert;
4. si ricavano le **PSD** delle componenti e dell'inviluppo: la PSD dell'inviluppo è quella del processo analitico traslata nell'origine, $S_{xx}(f) = 2S_{x_px_p}(f+f_c)\,u(f+f_c)$;
5. se la PSD passa-banda è **simmetrica rispetto a $f_c$**, $S_{xx}$ è pari, $R_{xx}$ è reale, $x_c$ e $x_s$ sono incoerenti (e indipendenti se gaussiani) e $S_{xx} = 2S_{x_cx_c} = 2S_{x_sx_s}$;
6. esempio: il **rumore in banda passante**, con la costruzione grafica di $S_{w_cw_c}$.

### Corrispondenza pagine PDF ↔ slide

Le pagine di appunti sono intercalate alle slide (il numero stampato sulla slide è «k / 13»).

| Pagina PDF | Contenuto | Pagina PDF | Contenuto |
|---|---|---|---|
| 1 | slide 1 (titolo) | 14 | slide 8 |
| 2 | slide 2 | 15 | appunti a mano |
| 3 | appunti a mano | 16 | appunti a mano |
| 4 | slide 3 (+ nota a mano) | 17 | slide 9 |
| 5 | appunti a mano | 18 | appunti a mano |
| 6 | slide 4 | 19 | appunti a mano |
| 7 | appunti a mano | 20 | slide 10 (+ note a mano) |
| 8 | appunti a mano | 21 | slide 11 |
| 9 | appunti a mano | 22 | appunti a mano |
| 10 | slide 5 | 23 | appunti a mano |
| 11 | slide 6 (+ «Perché?») | 24 | slide 12 |
| 12 | slide 7 | 25 | slide 13 |
| 13 | appunti a mano | | |

## Punti chiave · [[Rappresentazione_Rice_processi.pdf#page=2|p. 2]], [[Rappresentazione_Rice_processi.pdf#page=4|4]], [[Rappresentazione_Rice_processi.pdf#page=6|6]], [[Rappresentazione_Rice_processi.pdf#page=10|10]]–[[Rappresentazione_Rice_processi.pdf#page=12|12]], [[Rappresentazione_Rice_processi.pdf#page=14|14]], [[Rappresentazione_Rice_processi.pdf#page=17|17]], [[Rappresentazione_Rice_processi.pdf#page=20|20]], [[Rappresentazione_Rice_processi.pdf#page=21|21]], [[Rappresentazione_Rice_processi.pdf#page=24|24]], [[Rappresentazione_Rice_processi.pdf#page=25|25]]

1. Si lavora con processi **reali, WSS, a media nulla**. Banda base: $S_{x_bx_b}(f) = 0$ per $|f| > W$; passa-banda: $S_{x_px_p}(f) = 0$ per $|f \pm f_c| > W$.
2. Processo analitico: $x_p^+(t) = \frac{1}{\sqrt2}x_p(t) + \frac{j}{\sqrt2}\widehat{x}_p(t)$, con $\widehat{x}_p$ uscita del filtro di Hilbert $h(t) = 1/(\pi t)$, $H(f) = -j\,\text{sgn}(f)$.
3. Inviluppo complesso $x(t) = x_p^+(t)\,e^{-j2\pi f_ct} = x_c(t) + jx_s(t)$; $x_p = \sqrt2\,x_c\cos(2\pi f_ct) - \sqrt2\,x_s\sin(2\pi f_ct)$.
4. **Teorema:** $x_p$ WSS a media nulla ⇒ $x_c$, $x_s$ congiuntamente WSS a media nulla. Relazioni usate: $R_{\widehat{x}_p\widehat{x}_p} = R_{x_px_p}$, $R_{\widehat{x}_px_p} = \widehat{R}_{x_px_p}$, $R_{x_p\widehat{x}_p} = -\widehat{R}_{x_px_p}$.
5. Condizioni (10): $R_{x_cx_c} = R_{x_sx_s}$ e $R_{x_cx_s} = -R_{x_sx_c}$; l'acf dell'inviluppo è $R_{xx} = 2R_{x_cx_c} + 2jR_{x_sx_c}$; $R_{x_cx_s}(0) = 0$, quindi nello stesso istante $x_c$ e $x_s$ sono incorrelate (indipendenti se gaussiane).
6. PSD: $S_{x_cx_c}(f) = \frac12[S_{x_px_p}(f-f_c)\,u(f_c-f) + S_{x_px_p}(f+f_c)\,u(f+f_c)]$ (13); $S_{xx}(f) = S_{x_p^+x_p^+}(f+f_c) = 2S_{x_px_p}(f+f_c)\,u(f+f_c)$ (14).
7. Spettro simmetrico attorno a $f_c$ ⇒ $S_{xx}$ pari ⇒ $R_{xx}$ reale ⇒ $R_{x_sx_c} = 0$ per ogni $\tau$ ⇒ $S_{xx} = 2S_{x_cx_c} = 2S_{x_sx_s}$.
8. Rumore in banda passante con PSD $N_0/2$ su due lobi di larghezza $W$: $S_{w_cw_c} = S_{w_sw_s} = N_0/2$ e $S_{ww} = N_0$ per $|f| < W/2$; la potenza $P_{w_p} = N_0W$ coincide con quella dell'inviluppo.

## Concetti introdotti

- [[processi-passa-banda]] — processo analitico, inviluppo complesso e componenti I/Q di un processo; teorema sulla WSS congiunta con le dimostrazioni degli appunti
- [[psd-componenti-in-quadratura]] — PSD delle componenti e dell'inviluppo; caso simmetrico e incoerenza
- [[rumore-in-banda-passante]] — esempio del rumore a PSD costante in banda, costruzione grafica

Pagine già esistenti toccate: [[inviluppo-complesso]], [[segnale-analitico]], [[processi-e-sistemi-lti]], [[densita-spettrale-di-potenza]], [[processo-gaussiano]], [[momenti-di-un-processo]].

## Appunti a mano · [[Rappresentazione_Rice_processi.pdf#page=3|p. 3]], [[Rappresentazione_Rice_processi.pdf#page=5|5]], [[Rappresentazione_Rice_processi.pdf#page=7|7]]–[[Rappresentazione_Rice_processi.pdf#page=9|9]], [[Rappresentazione_Rice_processi.pdf#page=13|13]], [[Rappresentazione_Rice_processi.pdf#page=15|15]], [[Rappresentazione_Rice_processi.pdf#page=16|16]], [[Rappresentazione_Rice_processi.pdf#page=18|18]], [[Rappresentazione_Rice_processi.pdf#page=19|19]], [[Rappresentazione_Rice_processi.pdf#page=22|22]], [[Rappresentazione_Rice_processi.pdf#page=23|23]]

Cosa aggiungono alle slide. Tutte le dimostrazioni dei passaggi che le slide lasciano a lavagna stanno qui.

| Pagina | Contenuto | Dove nel wiki |
|---|---|---|
| p. 3 | ipotesi (reale, WSS, a media nulla); definizioni di processo in banda base e passa-banda; processo analitico e filtro di Hilbert | [[processi-passa-banda]] |
| p. 5 | definizione dell'inviluppo complesso come traslazione in frequenza; $x_c$ e $x_s$ sono processi reali in banda base; estrazione delle componenti | [[processi-passa-banda]] |
| p. 7 | enunciato del teorema; media nulla di $x_c$, $x_s$ (anche la trasformata di Hilbert ha media nulla); relazioni (2)–(4) tra $x_p$ e $\widehat{x}_p$ | [[processi-passa-banda]] |
| p. 8 | calcolo di $R_{x_cx_c}(t,\tau)$ passo per passo, con le formule di Werner; stessi passaggi per $x_s$ e per le mutue | [[processi-passa-banda]] |
| p. 9 | $R_{x_cx_c} = R_{x_sx_s}$, $R_{x_cx_s} = -R_{x_sx_c}$; $R_{xx}(\tau) = 2R_{x_cx_c} + j2R_{x_sx_c}$; $R_{x_cx_s}(0) = 0$ perché $R_{xx}(0)$ è reale: risposta al «Perché?» della slide 6 | [[processi-passa-banda]] |
| p. 13 | trasformata di $R_{x_cx_c}$ passo per passo, con $1 \mp \text{sgn} = 2u$; $S_{x_cx_c} = S_{x_sx_s}$; relazione per la cross-PSD | [[psd-componenti-in-quadratura]] |
| p. 15 | processo analitico come uscita di un filtro con $H = \sqrt2\,u(f)$; $R_{xx} = R_{x_p^+x_p^+}e^{-j2\pi f_c\tau}$: la moltiplicazione per un esponenziale complesso conserva la WSS; PSD traslata | [[psd-componenti-in-quadratura]] |
| p. 16 | riassunto dei tre passi per ottenere la PSD dell'inviluppo | [[psd-componenti-in-quadratura]] |
| p. 18 | caso particolare molto frequente: PSD simmetrica rispetto a $f_c$ ⇒ $S_{xx}$ pari ⇒ $R_{xx}$ reale e pari ⇒ $R_{x_sx_c} = 0$ ⇒ incoerenti; incorrelate se a media nulla; indipendenti se gaussiane | [[psd-componenti-in-quadratura]] |
| p. 19 | l'incoerenza in generale vale solo in $\tau = 0$; con spettro simmetrico per ogni $\tau$ | [[psd-componenti-in-quadratura]] |
| p. 22 | rumore in banda passante: calcolo delle PSD in banda base, potenza $N_0W$ | [[rumore-in-banda-passante]] |
| p. 23 | $w_c$ e $w_s$ nello stesso istante incorrelate; $S_{w_cw_s} = 0$ perché $S_{ww}$ è reale; indipendenti se $w_p$ è gaussiano | [[rumore-in-banda-passante]] |

Note a mano scritte sopra le slide: p. 4 (annotazione sulle espressioni di $x_c$ e $x_s$, in parte illeggibile: dice «perché tutte e due hanno media nulla»), p. 11 («Perché?» accanto a $R_{x_cx_s}(0) = 0$), p. 20 (descrizione dei quattro grafici, $R_{xx} = 2R_{x_cx_c} + j2R_{x_sx_c}$ e $S_{xx}$ reale per definizione).

## Domande aperte

- La slide 2 dice «passa-banda se $S = 0$ per $|f \pm f_c| > W$», cioè $W$ è la **semilarghezza** di ogni lobo; dalla slide 10 in poi $W$ è la **larghezza** del lobo ($S_{xx} \ne 0$ per $|f| < W/2$, potenza $2W\cdot N_0/2$). Le condizioni di supporto restano valide, ma il simbolo cambia significato: nel wiki si indica ogni volta quale convenzione vale.
- Nota a mano di p. 4 solo in parte leggibile: «…perché tutte e due hanno media nulla». Interpretata come: $x_c$ e $x_s$ hanno media nulla perché $x_p$ e $\widehat{x}_p$ ce l'hanno. Da confermare con la docente.
- La slide 7 dice solo che le cross-PSD «si ottengono» trasformando (8) e (9). Il risultato è ricavato nel wiki (🧩) in [[psd-componenti-in-quadratura]].
- La (14) usa $u(f+f_c)$; nella verifica dell'evenness (p. 18) compare anche $u(-f+f_c)$: i due gradini valgono 1 entrambi sul supporto $|f| < W/2$ del lobo, purché $f_c > W/2$. Ragionamento mio, non scritto negli appunti.

## Domande da esame

- Come si costruisce l'inviluppo complesso di un processo passa-banda? Perché si usa il processo analitico?
- Dimostra che, se $x_p$ è WSS a media nulla, $x_c$ e $x_s$ sono congiuntamente WSS.
- Quali relazioni valgono tra $R_{x_cx_c}$, $R_{x_sx_s}$, $R_{x_cx_s}$ e $R_{x_sx_c}$? Perché $R_{x_cx_s}(0) = 0$?
- Che relazione c'è tra la PSD del processo passa-banda e quella dell'inviluppo complesso? E quella di $x_c$?
- Cosa cambia se la PSD passa-banda è simmetrica attorno a $f_c$? Quando $x_c$ e $x_s$ sono indipendenti?
- Calcola le PSD delle componenti in quadratura del rumore a PSD $N_0/2$ in banda $W$ e verifica la conservazione della potenza.

_Aggiornato: 2026-11-01 — creazione da ingest Rappresentazione_Rice_processi.pdf_
