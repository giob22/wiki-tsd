---
tipo: laboratorio
esame: no
macroblocco: 3
codice: "AD_conversion.m, righe 146-187"
concetti: ["quantizzazione-uniforme", "conversione-ad-da"]
---

# Lab 3 — Quantizzazione

> ⚠️ Non materia d'esame: serve a vedere la [[quantizzazione-uniforme]] su numeri veri. Fonte: [[laboratorio-conversione-ad]]. Prima leggere [[lab-campionamento]] e [[lab-interpolazione]].

## Cosa fa il codice · [[AD_conversion.m]] righe 146–175

```matlab
bits  = 4;
s_min = min(s_samp);  s_max = max(s_samp);
range = s_max - s_min;                 % dinamica dei campioni
Nq    = pow2(bits);                    % 2^4 = 16 livelli
Delta = range/Nq;                      % larghezza di una cella
cbook = s_min+Delta/2:Delta:s_max;     % livelli al centro delle celle
for k=1:length(is)                     % per ogni campione:
   [~,index(k)] = min(abs(cbook-s_samp(is(k))));   % livello più vicino
end
s_q(is) = cbook(index);                % campioni quantizzati
sq_r_trunc = ...conv(s_q,h)...         % stessa interpolazione di prima
```

1. **Dinamica.** Si prende l'intervallo $[s_{min}, s_{max}]$ dei valori campionati.
2. **Celle.** Lo si divide in $N_q = 2^{b}$ celle uguali di larghezza $\Delta$.
3. **Codebook.** I livelli (parole codice) sono i **centri** delle celle.
4. **Quantizzazione.** Ogni campione va nel livello più vicino.
5. **Ricostruzione.** I campioni quantizzati passano nello stesso interpolatore di [[lab-interpolazione]], con lo stesso taglio.

## Cosa succede davvero

### I numeri dell'esempio 1 · [[Campionamento_AD_DA.pdf#page=26|p. 26]], [[Campionamento_AD_DA.pdf#page=28|p. 28]]
> 🧩 Derivazione mia

$$
\begin{aligned}
s_{min} &= 0,\quad s_{max} = 1 \Rightarrow \text{range} = 1 && \text{campioni del trapezio (lab 1)} \\
N_q &= 2^4 = 16 && b = 4\ \text{bit} \\
\Delta &= \text{range}/N_q = 1/16 = 0.0625 && \text{larghezza di una cella} \\
\text{cbook} &= 0.03125,\ 0.09375,\ \dots,\ 0.96875 && \text{da } \Delta/2 \text{ con passo } \Delta\text{: 16 valori}
\end{aligned}
$$

Cosa succede ai campioni:

| Campione | Livello più vicino | Errore $e = s_q - s$ |
|---|---|---|
| 0 (i 112 campioni fuori dal trapezio) | 0.03125 | $+0.03125 = +\Delta/2$ |
| 0.008 (in $\pm 1.992$) | 0.03125 | +0.023 |
| 0.506 (in $\pm 1.494$) | 0.53125 (distanza 0.025, contro 0.038 da 0.46875) | +0.025 |
| 1 (5 campioni) | 0.96875 | $-0.03125 = -\Delta/2$ |

È il quantizzatore uniforme delle slide: celle larghe $\Delta$, livello nel punto medio, $|e| \le \Delta/2$ nella regione granulare. Qui la dinamica non è simmetrica ($[0, 1]$ invece di $[-X_{max}, X_{max}]$), ma la relazione è la stessa: $M\Delta$ = ampiezza della dinamica, con $M = N_q$ ([[quantizzazione-uniforme]]).

### Lo zero non esiste · [[Campionamento_AD_DA.pdf#page=30|p. 30]]
Con i livelli al centro delle celle e l'estremo della dinamica in 0, **nessun livello vale 0**: il più basso è $\Delta/2$. Tutti i campioni nulli, cioè 112 su 121, diventano 0.03125. Dopo l'interpolazione il segnale ricostruito ha un "pavimento" a 0.031 su tutta la finestra fuori dal trapezio: è la riga sollevata che si vede in basso nelle due figure del laboratorio.

Allo stesso modo il massimo 1 diventa 0.96875: il plateau ricostruito si abbassa di $\Delta/2$.

> 🧩 Perché conta: l'errore di questi campioni non è "casuale tra $-\Delta/2$ e $\Delta/2$" come nel modello delle slide, ma vale **sempre esattamente** $+\Delta/2$. Il modello $\Delta^2/12$ sottostima quindi il rumore: le conseguenze sull'SNR sono in [[lab-snr]].

![[grafico-lab-quantizzazione.png]]
*🧩 Grafico mio (replica dello script, 4 bit).*
- *A sinistra: la caratteristica a gradini $Q(x)$ con i 16 livelli. I pallini arancio sono i valori dei campioni del trapezio (0, 0.008, 0.506, 1): lo 0 finisce su $\Delta/2$.*
- *Al centro: l'errore sui 121 campioni. Quasi tutti valgono $+\Delta/2$ (i campioni nulli); i 5 campioni a 1 valgono $-\Delta/2$; i quattro sui fianchi stanno in mezzo. Tutti restano dentro $\pm\Delta/2$ (linee rosse).*
- *A destra: il ricostruito dopo la quantizzazione (interpolazione lineare), con il pavimento a 0.031 e il plateau a 0.969.*

### Le figure del laboratorio
Nelle figure [[Figure_2_interpolazione_lineaare.png]] e [[Figure_2_interpolazione_shannon.png]] (embed in [[lab-interpolazione]]):
- **pannello centrale:** i campioni quantizzati $s_q(n)$. Le aste nulle ora partono da 0.03, quelle a 1 arrivano a 0.97, quelle a 0.5 a 0.53;
- **pannello in basso:** il ricostruito $\hat s_q(t)$. Con il triangolo si vede il pavimento a 0.03 e un piccolo gomito in $t = \pm 1.5$ s, dove il campione 0.506 è diventato 0.531. Con la sinc la curva è morbida e ha anche le oscillazioni fuori dal trapezio.

## Dubbi chiariti

- **"Perché il segnale ricostruito non torna a zero?"** Perché con i livelli al centro delle celle lo zero non è rappresentabile: il livello più basso è $\Delta/2$. Un quantizzatore con un livello in 0 (celle centrate sullo zero) non avrebbe questo difetto.
- **"Quantizzare cambia la durata o l'allineamento?"** No: `s_q` è nullo negli stessi punti di `s_samp` (solo i campioni vengono modificati), e si usano lo stesso $h$ e lo stesso taglio.

> 🧩 Dettaglio del codice: `s_min` e `s_max` sono calcolati su tutto `s_samp`, compresi gli zeri messi tra un campione e l'altro. Per il trapezio non cambia nulla, perché il minimo dei campioni è già 0. Con campioni tutti positivi, però, il minimo diventerebbe 0 anche se nessun campione vale 0, e la dinamica risulterebbe più larga del necessario. Andrebbe usato `s_samp(is)`.

## Collegamento alla teoria · [[Campionamento_AD_DA.pdf#page=25|p. 25]], [[Campionamento_AD_DA.pdf#page=27|p. 27]], [[Campionamento_AD_DA.pdf#page=28|28]]

[[quantizzazione-uniforme]] (celle, livelli al centro, errore $|e| \le \Delta/2$: p. 25 – p. 28); il codice binario dei livelli, 4 bit per 16 livelli, qui non viene scritto: lo script conserva direttamente i valori dei livelli.

_Aggiornato: 2026-09-30 — creazione da ingest del laboratorio (AD_conversion.m)_
