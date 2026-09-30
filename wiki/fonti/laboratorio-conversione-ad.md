---
tipo: fonte
titolo: "Laboratorio Matlab: conversione A/D e D/A (AD_conversion.m)"
file_raw: "scripts/09_28_2006/AD_conversion.m"
pagine: "righe 1-204 + 3 figure"
data_ingest: 2026-09-30
formato: script
argomenti: [simulazione a tempo pseudo-continuo, spettro con FFT, campionamento, interpolazione ZOH/lineare/sinc, durata della convoluzione, quantizzazione uniforme, SNR di quantizzazione]
---

# Laboratorio Matlab: conversione A/D e D/A — AD_conversion.m

> ⚠️ **Non è materia d'esame.** Matlab non si chiede all'esame, e questa lezione serviva a *vedere* cosa succede. Le pagine del laboratorio servono a togliere i dubbi sulla teoria di [[campionamento-conversione-ad-da]], non a imparare il codice.

## Sommario

Lezione di laboratorio del 28/09 (la cartella si chiama `09_28_2006`: l'anno va letto 2026). Il materiale è lo script [[AD_conversion.m]] più tre figure salvate dall'esecuzione ([[Figure_1.png]], [[Figure_2_interpolazione_lineaare.png]], [[Figure_2_interpolazione_shannon.png]]).

Lo script percorre tutta la catena della conversione A/D e D/A su un segnale noto:
1. costruisce un segnale "a tempo continuo" su una griglia fittissima e ne calcola lo spettro con la FFT;
2. lo **campiona** a $f_s = 2W$;
3. lo **ricostruisce** convolvendo i campioni con un filtro interpolatore (rettangolo, triangolo o sinc), poi **taglia** il risultato;
4. **quantizza** i campioni con 4 bit e ricostruisce di nuovo;
5. misura quanto il ricostruito differisce dall'originale con l'**SNR**.

Due segnali di prova, scelti con `flag`: un trapezio (esempio 1, quello delle figure) e una somma di tre sinusoidi (esempio 2). Un blocco commentato permette di usare un file audio e di ascoltarlo con `sound`.

Nel wiki ogni macroblocco ha una pagina in `laboratorio/`, con cosa fa il codice, cosa succede davvero, i numeri ricostruiti e grafici 🧩 generati da una replica Python dello script (`output/grafici/genera_grafici_laboratorio_ad.py`, che riproduce gli stessi arrotondamenti e la stessa convoluzione).

## Macroblocchi

| # | Pagina | Righe | Domanda a cui risponde |
|---|---|---|---|
| 0 | [[lab-setup-e-spettro]] | 5–85 | come si simula il "tempo continuo" al computer e come si ottiene lo spettro |
| 1 | [[lab-campionamento]] | 87–101 | cosa vuol dire campionare in una simulazione, e cosa succede allo spettro |
| 2 | [[lab-interpolazione]] | 103–144, 199–202 | perché il ricostruito dura di più, perché va tagliato e dove |
| 3 | [[lab-quantizzazione]] | 146–187 | come lavora il quantizzatore a 16 livelli e perché lo zero diventa 0.031 |
| 4 | [[lab-snr]] | 189–192 | cosa misura davvero l'SNR stampato (16.7 dB) e perché non torna con la formula dei 6 dB/bit |

## Punti chiave

1. Il "tempo continuo" è una griglia con passo $dt = 6$ ms su 60 s ($10^4$ punti). Tutti gli istanti (inizio del segnale, $T_s$) vengono arrotondati a multipli di $dt$: per questo $T_s = 0.498$ s invece di 0.5 s ([[lab-setup-e-spettro]], [[lab-campionamento]]).
2. Lo spettro è $dt\cdot\text{FFT}$: una somma di Riemann dell'integrale di Fourier. Per il trapezio coincide con la trasformata esatta $3\,\text{sinc}(3f)\,\text{sinc}(f)$ ([[lab-setup-e-spettro]]).
3. Campionare = azzerare tutti i punti della griglia tranne quelli in $nT_s$. Il vettore che resta è la versione simulata di $x_\delta(t)$ ([[lab-campionamento]]).
4. Interpolare = convolvere i campioni con $h$. La convoluzione dura quanto la **somma** delle durate: $N + L - 1$ punti. Si tagliano $(L-1)/2$ punti all'inizio per riportare il risultato sull'asse di $s(t)$; tagliare nel posto sbagliato sposta il segnale ([[lab-interpolazione]]).
5. Il quantizzatore del codice ha i livelli al centro delle celle e nessun livello in 0: i campioni nulli diventano $\Delta/2 = 0.031$ ([[lab-quantizzazione]]).
6. L'SNR stampato (16.7 dB) mescola quantizzazione, interpolazione e finestra di osservazione. Cresce di 6 dB per bit finché domina la quantizzazione ([[lab-snr]]).
7. Nell'esempio 2 l'arrotondamento porta $f_s$ a 7.94 Hz, sotto $2W = 8$ Hz: la componente a 4 Hz va in aliasing e la ricostruzione è pessima (SNR ≈ 2 dB) ([[lab-campionamento]]).

## Figure del laboratorio

Copiate in `raw/assets/` con nomi parlanti; sono le figure Matlab dell'esempio 1 (`flag = 1`).

| File originale | In `raw/assets/` | Contenuto | Dove |
|---|---|---|---|
| [[Figure_1.png]] | `lab-0928-figure1-segnale-spettro-campioni.png` | trapezio, spettro, segnale campionato | [[lab-setup-e-spettro]], [[lab-campionamento]] |
| [[Figure_2_interpolazione_lineaare.png]] | `lab-0928-figure2-interpolazione-lineare.png` | ricostruito (triangolo), campioni quantizzati, ricostruito dopo la quantizzazione | [[lab-interpolazione]], [[lab-quantizzazione]] |
| [[Figure_2_interpolazione_shannon.png]] | `lab-0928-figure2-interpolazione-shannon.png` | le stesse tre cose con la sinc | [[lab-interpolazione]], [[lab-quantizzazione]] |

## Concetti collegati (teoria d'esame)

- [[conversione-ad-da]] — la catena campionamento → quantizzazione → interpolazione.
- [[teorema-del-campionamento]], [[aliasing]] — cosa succede allo spettro.
- [[interpolazione]] — ZOH, FOH, serie di Shannon.
- [[quantizzazione-uniforme]], [[snr-di-quantizzazione]] — livelli, $\Delta$, legge dei 6 dB/bit.

## Domande aperte

- Nel caso `C = 1` (rettangolo, commentato nello script) i rettangoli adiacenti hanno un punto in comune e producono picchi a valore doppio ([[lab-interpolazione]]). Probabilmente è per questo che a lezione si sono usati il triangolo e la sinc.
- Il file `Musica_1.wav` del blocco commentato (righe 52–64 e 194–196) non è nella cartella: l'esperimento audio non si può ripetere. Il blocco sostituisce il segnale con la musica, rifà la griglia e con `sound` fa ascoltare originale e ricostruito.
  > 🧩 Con i parametri scritti lì: $dt = 1.4512/16000 = 90.7\ \mu$s, cioè una griglia a $1/dt = 11025$ Hz, la frequenza tipica di un file audio. Con $W = 4$ kHz: $T_s = 1/8000 = 125\ \mu$s, e $T_s/dt = 1.38 \to 1$. Quindi $T_s = dt$: si "campionerebbe" ogni punto e il campionamento non toglierebbe nulla. Per sentire l'effetto del campionamento servirebbe un $W$ più piccolo, per esempio $W \le 2.7$ kHz, così che $T_s \ge 2\,dt$.
- Il commento della riga 88 dice che con $W = 1$ «è come se avessimo applicato un filtro anti-aliasing». Nessun filtro viene applicato: il trapezio ha solo lo 0.05% dell'energia oltre 1 Hz, quindi l'aliasing è piccolo ma non nullo ([[lab-campionamento]]).

## Domande da esame

Nessuna: materiale di laboratorio. Serve per rispondere meglio alle domande su [[teorema-del-campionamento]], [[interpolazione]], [[quantizzazione-uniforme]] e [[snr-di-quantizzazione]].

_Aggiornato: 2026-09-30 — creazione da ingest di raw/scripts/09_28_2006_
