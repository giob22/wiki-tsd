---
tipo: concetto
importanza_esame: alta
prerequisiti: ["principi-di-modulazione", "spazio-dei-segnali", "upconversion-e-downconversion", "densita-spettrale-di-potenza"]
fonti_pdf: ["Modulazione.pdf#page=23", "Modulazione.pdf#page=26", "Modulazione.pdf#page=28", "Modulazione.pdf#page=30", "Modulazione.pdf#page=31", "Modulazione.pdf#page=33", "Modulazione.pdf#page=34", "Modulazione.pdf#page=36"]
---

# Modulazione lineare

## Definizione · [[Modulazione.pdf#page=23|p. 23]]

Una modulazione è **lineare** quando l'inviluppo complesso trasmesso è una somma di copie traslate di un unico impulso, pesate dai simboli:

$$s(t)=\sum_{k=-\infty}^{+\infty}\xi_k\,g_{TX}(t-kT)$$

$\xi_k$ sono i simboli (valori di una **costellazione**, inviati a rate $1/T$), $g_{TX}(t)$ è un impulso deterministico in banda base. In banda base fisica i simboli sono reali (**codici di linea**: NRZ, RZ, PAM); in banda passante sono complessi e si dispongono su un piano (PSK, QAM).

## Formule · [[Modulazione.pdf#page=28|p. 28]]–[[Modulazione.pdf#page=36|36]]

| Formula | Significato |
|---|---|
| $\xi_k=(-1)^{b_k}$, $g_{TX}=A\,\text{rect}\big(\frac{t-0.5T}{T}\big)$ | NRZ ($R_b=R_s=1/T$) |
| $g_{TX}=A\,\text{rect}\big(\frac{t-0.25T}{0.5T}\big)$ | RZ |
| $s_c=\sum_k\text{Re}(\xi_k)g_{TX}(t-kT)$, $s_s=\sum_k\text{Im}(\xi_k)g_{TX}(t-kT)$ | componenti I/Q, eq. (1)–(2) |
| $\xi_k=e^{j\Phi_k}$, $\Phi_k\in\{\frac{2\pi}{M}(i-1)+\Phi\}$ | PSK (modulo costante) |
| $a_i=(2i-1-M)\frac d2$ | PAM, livelli equispaziati |
| $S_{ss}(f)=\frac{E[\lvert\xi_k\rvert^2]}{T}\lvert G_{TX}(f)\rvert^2$ | PSD con simboli i.i.d. a media nulla |

> 🧮 Formula chiave: $s(t)=\sum_k\xi_kg_{TX}(t-kT)$ e $S_{ss}(f)=\dfrac{E[\lvert\xi_k\rvert^2]}{T}\lvert G_{TX}(f)\rvert^2$.

Simboli: $T$ [s] periodo di simbolo; $A$ ampiezza; $d$ distanza tra livelli PAM; $G_{TX}(f)$ trasformata dell'impulso; $\Phi$ fase costante arbitraria.

## Derivazioni

### Derivazione — PSD di un segnale modulato linearmente · [[Modulazione.pdf#page=36|p. 36]]
**Fonte:** la slide 20 dà il risultato («it can be proven»); gli appunti ricordano $E[\xi_k\xi_{k-m}^\ast]=\sigma_\xi^2\delta(m)+\lvert\mu_\xi\rvert^2$. Il calcolo è lo stesso dell'esempio della Lezione 6 ([[calcolo-densita-spettrale]]).

> 🧩 Derivazione mia (con un ritardo casuale uniforme che rende il processo WSS, come in [[densita-spettrale-di-potenza]]).

$$
\begin{aligned}
R_{ss}(\tau)&=\sum_n\sum_mE[\xi_n\xi_m^\ast]\;\frac1T\int g_{TX}(u)\,g_{TX}^\ast(u-\tau-(m-n)T)\,du && \text{simboli e ritardo indipendenti}\\
E[\xi_n\xi_m^\ast]&=E[\lvert\xi\rvert^2]\,\delta_{nm} && \text{i.i.d. a media nulla}\\
R_{ss}(\tau)&=\frac{E[\lvert\xi\rvert^2]}{T}\,\big[g_{TX}(\tau)\ast g_{TX}^\ast(-\tau)\big] && \text{resta solo } m=n\\
S_{ss}(f)&=\frac{E[\lvert\xi\rvert^2]}{T}\,\lvert G_{TX}(f)\rvert^2 && \text{Wiener-Khinchin}
\end{aligned}
$$

**Numeri:** impulso rettangolare di durata $T$ e ampiezza 1, $G_{TX}(f)=T\,\text{sinc}(fT)$, quindi $S_{ss}(f)=E[\lvert\xi\rvert^2]\,T\,\text{sinc}^2(fT)$: primo zero in $f=1/T$, come nella figura della slide.
**Ipotesi:** simboli i.i.d. a **media nulla**; con media non nulla si aggiungono righe spettrali.

### Derivazione — Componenti I/Q della PSK · [[Modulazione.pdf#page=30|p. 30]], [[Modulazione.pdf#page=31|31]]
**Fonte:** eq. (1)–(4).

$$
\begin{aligned}
A\,\xi_k&=A\,e^{j\Phi_k}=A\cos\Phi_k+jA\sin\Phi_k && \text{Eulero; } \xi_k=e^{j\Phi_k}\text{ ha modulo 1, } A \text{ è il fattore d'ampiezza}\\
s_c(t)&=\sum_k\text{Re}(A\,\xi_k)\,g_{TX}(t-kT)=A\sum_k\cos(\Phi_k)\,g_{TX}(t-kT) && \text{(1) con i simboli scalati di } A\text{: è la (3)}\\
s_s(t)&=\sum_k\text{Im}(A\,\xi_k)\,g_{TX}(t-kT)=A\sum_k\sin(\Phi_k)\,g_{TX}(t-kT) && \text{(2): è la (4)}
\end{aligned}
$$

### Derivazione — Livelli PAM · [[Modulazione.pdf#page=34|p. 34]]
**Fonte:** slide 18.

$$
a_i=(2i-1-M)\frac d2:\qquad M=4,\ d=2:\ a_1=-3,\ a_2=-1,\ a_3=1,\ a_4=3
$$

Livelli adiacenti distano $a_{i+1}-a_i=d$; i livelli sono simmetrici attorno a 0 (baricentro nell'origine, quindi energia minima per la distanza data).

## Spiegazione · appunti [[Modulazione.pdf#page=24|p. 24]], [[Modulazione.pdf#page=25|25]], [[Modulazione.pdf#page=27|27]], [[Modulazione.pdf#page=32|32]]

Nella modulazione lineare il segnale è costruito come un treno di impulsi tutti uguali, ciascuno moltiplicato per il simbolo del suo intervallo. Due scelte lo definiscono: l'**impulso** $g_{TX}$, che fissa la forma dello spettro, e la **costellazione**, che fissa dove stanno i simboli.

**Banda base reale.** Se il canale è in banda base (cavo, bus), il segnale va trasmesso così com'è e deve essere reale: i simboli sono numeri reali e le costellazioni sono **unidimensionali**. NRZ e RZ usano due livelli $\pm A$ (multipli di un'unica forma d'onda); la PAM ne usa $M$.

**Banda passante.** Con l'upconverter si trasmettono insieme due segnali reali, in fase e in quadratura: il simbolo diventa un numero complesso, un punto del piano. La parte reale va sul ramo del coseno, la parte immaginaria su quello del seno.
- **PSK**: tutti i punti su un cerchio, informazione solo nella fase. Il modulo costante è comodo, ma aumentando $M$ i punti si affollano sul cerchio e si avvicinano.
- **QAM**: punti su una griglia, varia sia il modulo sia la fase; a parità di energia separa meglio i punti per $M$ grande.
- **Mapping di Gray**: a simboli adiacenti si danno parole di bit che differiscono per un solo bit; così l'errore più probabile (confondere un simbolo con un vicino) costa un bit solo.

**Spettro.** Con simboli i.i.d. a media nulla, la PSD ha la forma di $\lvert G_{TX}(f)\rvert^2$: la costellazione cambia solo il livello $E[\lvert\xi\rvert^2]$. Per controllare la banda si lavora sull'impulso. La banda di un processo si legge sulla sua PSD; per l'inviluppo complesso si usa la banda bilatera, uguale alla banda monolatera del segnale passa-banda.

> 🎯 Esame: forma generale della modulazione lineare, NRZ/RZ, I/Q in banda passante, PSK, QAM, PAM con i livelli e il mapping di Gray, PSD di un segnale modulato linearmente e da cosa dipende.

## Perché importa

È la famiglia di modulazioni più usata: tutte le prestazioni calcolate nelle lezioni successive (probabilità d'errore di PAM, QPSK, 16-QAM) e la tabella delle efficienze di [[parametri-globali-modulazioni]] riguardano costellazioni di questo tipo.

## Connessioni

- [[principi-di-modulazione]] — mapper, baud rate, compromesso potenza-banda.
- [[spazio-dei-segnali]] — PAM unidimensionale, PSK/QAM bidimensionali.
- [[upconversion-e-downconversion]] — lo schema che porta $s_c$, $s_s$ in banda passante.
- [[densita-spettrale-di-potenza]], [[calcolo-densita-spettrale]] — la PSD di un segnale modulato linearmente.
- [[modulazione-ortogonale]] — l'alternativa non lineare (FSK).
- [[probabilita-errore-m-aria]] — prestazioni di QPSK e 16-QAM.

## Fonti · [[Modulazione.pdf#page=23|p. 23]]–[[Modulazione.pdf#page=37|37]]

[[principles-of-modulation]] — Modulazione.pdf, slide 11–21 e appunti.

_Aggiornato: 2026-11-19 — derivazione I/Q della PSK resa coerente con la slide ($\xi_k=e^{j\Phi_k}$ di modulo 1 e fattore $A$ separato); 2026-11-16 — creazione da ingest Modulazione.pdf_
