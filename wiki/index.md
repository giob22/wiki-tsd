# Index — Trasmissione dei Segnali Digitali

## Overview
- [[overview]] — panoramica del corso, programma, copertura
- [[lezioni]] — elenco lezioni con gli argomenti in ordine di PDF
- [[corso-completo]] — tutto il corso in un unico file, lezione per lezione (generato da `output/genera_compendio.py`)

## Concetti

**Sistema di comunicazione**
- [[sistema-comunicazione-digitale]] — elementi, schema a blocchi, vantaggi del digitale, separazione (alta)

**Probabilità**
- [[spazio-di-probabilita]] — assiomi di Kolmogorov, proprietà elementari (media)
- [[probabilita-condizionale]] — condizionale, probabilità composta, catena, indipendenza (alta)
- [[probabilita-totale-e-bayes]] — probabilità totale, Bayes (alta)
- [[variabile-aleatoria]] — CDF, pdf, DF; v.a. discrete/continue/miste (alta)
- [[variabili-aleatorie-notevoli]] — Bernoulli, Binomiale, Uniforme, Laplace (alta)
- [[variabile-aleatoria-gaussiana]] — pdf gaussiana, erf, erfc, Q (alta)
- [[funzione-di-variabile-aleatoria]] — $f_Y = \sum f_X/|g'|$ (media)
- [[media-e-varianza]] — teorema fondamentale, momenti, varianza (alta)
- [[coppie-di-variabili-aleatorie]] — congiunte, marginali, condizionali (media)
- [[correlazione-e-covarianza]] — Corr, Cov, ρ, Schwarz (alta)
- [[disuguaglianza-di-chebyshev]] — limite sulle code; sovraccarico (media)

**Conversione A/D e D/A**
- [[conversione-ad-da]] — campionamento + quantizzazione; interpolazione (media)
- [[teorema-del-campionamento]] — Shannon, Nyquist, ricostruzione (alta)
- [[aliasing]] — frequenza alias (perché si ricostruisce $f_c - f_0$, con animazioni), antialiasing (alta)
- [[interpolazione]] — serie di Shannon, ZOH, FOH (alta)
- [[quantizzazione-uniforme]] — Δ, M, regioni, fattore di carico (alta)
- [[snr-di-quantizzazione]] — legge dei 6 dB/bit (alta)
- [[quantizzazione-non-uniforme]] — Lloyd-Max: centroide e punto medio (alta)
- [[companding]] — quantizzare uniformemente $F(x)$ = quantizzare in modo non uniforme $x$ (il progetto si sposta su $F$); legge logaritmica, µ/A-law, prestazioni (alta)

**Rappresentazione complessa in banda base**
- [[modulazione-digitale]] — bit → forme d'onda; modulazione lineare binaria; vincoli di banda (media)
- [[segnali-banda-base-e-passa-banda]] — definizioni, simmetria hermitiana, banda mono/bilatera, banda stretta (alta)
- [[segnale-analitico]] — $S_p^+ = \sqrt2 S_p u(f)$, trasformata di Hilbert, perché $\sqrt2$ (alta)
- [[inviluppo-complesso]] — $s = s_c + js_s$, $s_p = \sqrt2\,\text{Re}\{s\,e^{j2\pi f_c t}\}$, ortogonalità I/Q, energia, banda (alta)
- [[upconversion-e-downconversion]] — mixer $\sqrt2\cos$, $-\sqrt2\sin$ e passa-basso; complesso ↔ reale in Tx e Rx; catena come canale unico (alta)
- [[equivalente-banda-base-dei-filtri]] — $y = s * h/\sqrt2$ con la dimostrazione degli appunti, quattro filtri reali (alta)

**Processi aleatori**
- [[processo-aleatorio]] — realizzazioni e v.a. a $t_0$, sinusoide a fase casuale, distribuzioni di ordine $k$ e marginali, DF del processo di Bernoulli, tempo discreto (alta)
- [[momenti-di-un-processo]] — media, autocorrelazione, autocovarianza, mutue correlazioni; indipendenti/incoerenti/incorrelati; processi complessi; momenti del rettangolo (non stazionario) e della sinusoide (WSS) (alta)
- [[stazionarieta]] — ordine $k$, SSS, primo e secondo ordine, WSS; SSS ⇒ WSS (alta)
- [[autocorrelazione-processi-wss]] — lag-acf, proprietà, $\rho_{XX}$, tempo di decorrelazione (alta)
- [[processi-e-sistemi-lti]] — $\mu_Y = \mu_X H(0)$, $R_{YY} = R_{XX} * h * h(-\tau)$, $S_{YY} = S_{XX}|H|^2$ (alta)
- [[densita-spettrale-di-potenza]] — definizione, Wiener-Khinchin, $2\Delta f\,S_{XX}$, proprietà, PSD mutue e della somma (alta)
- [[processo-gaussiano]] — gaussiana multivariata; WSS ⇒ SSS; incorrelati ⇒ indipendenti (alta)

## Entità
- [[ripetitore-rigenerativo]] — dispositivo
- [[g711]] — standard ITU-T PCM voce
- [[legge-mu]] — algoritmo di compressione (µ = 255)
- [[legge-a]] — algoritmo di compressione (A = 87.6)
- [[algoritmo-lloyd-max]] — quantizzatore ottimo MMSE

## Fonti
- [[intro-corso]] — Intro.pdf, pp. 1–21
- [[elementi-teoria-probabilita]] — Probabilità.pdf, pp. 1–38
- [[campionamento-conversione-ad-da]] — Campionamento_AD_DA.pdf, pp. 1–43
- [[rappresentazione-complessa-banda-base]] — Rappresentazione_Rice.pdf, pp. 1–27 (19 slide + 8 pagine di appunti a mano)
- [[processi-aleatori]] — random_processes.pdf, pp. 1–46 (41 slide + 5 pagine di appunti a mano)
- [[laboratorio-conversione-ad]] — scripts/09_28_2006: AD_conversion.m + 3 figure (laboratorio, non d'esame)

## Laboratorio (non materia d'esame)
Esperimenti Matlab per vedere la teoria all'opera; un macroblocco per pagina.
- [[lab-setup-e-spettro]] — tempo "pseudo-continuo" con passo $dt$, spettro come $dt\cdot$FFT, trasformata esatta del trapezio
- [[lab-campionamento]] — `s.*high` come $x_\delta(t)$, repliche e aliasing, $T_s$ arrotondato; esempio 2 sotto Nyquist
- [[lab-interpolazione]] — conv = serie di interpolazione; durate che si sommano, dove e perché tagliare; ZOH/FOH/sinc a confronto
- [[lab-quantizzazione]] — 16 livelli al centro delle celle; lo zero diventa $\Delta/2$
- [[lab-snr]] — cosa misura l'SNR stampato; 6 dB/bit, 4.77 dB sotto il modello $\Delta^2/12$, limite dell'interpolatore

## Esercizi
- [[calcolo-probabilita-eventi]] — eventi, condizionale, indipendenza (bassa)
- [[cdf-pdf-variabili-notevoli]] — CDF/pdf di v.a. notevoli e trasformate (media)
- [[campionamento-e-aliasing]] — Nyquist, alias, numero di campioni (bassa)
- [[dimensionamento-quantizzatore]] — bit, SNR, $k_c$, bit rate, companding (media)
- [[calcolo-densita-spettrale]] — PSD con Wiener-Khinchin; segnale modulato linearmente (media)

## Esame
_nessun materiale ancora — lancia `prepara esame`_

## Asset
Figure in `raw/assets/`: 3 da Intro, 7 da Probabilità, 29 da Campionamento, 11 da Rappresentazione_Rice (di cui 4 pagine di appunti a mano), 6 da random_processes (nome `file-pN-descrizione.png`).
Figure del laboratorio in `raw/assets/lab-0928-*.png` (3, copiate da `raw/scripts/09_28_2006/`).
Grafici 🧩 del laboratorio — script `genera_grafici_laboratorio_ad.py` (replica Python di AD_conversion.m): setup e spettro, spettro del campionato, durata della convoluzione e taglio, confronto interpolatori, quantizzazione, SNR vs bit, esempio 2; animazione `grafico-lab-interpolazione.gif`.
Grafici 🧩 dei processi aleatori — script `genera_grafici_random_processes.py`: realizzazioni e v.a. a $t_0$, processo lento contro veloce (autocorrelazione e PSD), gaussiana bivariata, animazione della costruzione di $R_{XX}(\tau)$ (`grafico-rp-autocorrelazione.gif`).
Grafici 🧩 della lezione sulla banda base — script `genera_grafici_rappresentazione_rice.py`: catena degli spettri $S_p \to S_p^+ \to S$, componenti I/Q nel tempo, animazione della downconversion (`grafico-rice-downconversion.gif`).
Grafici di funzione generati (🧩) in `output/grafici/` — script `genera_grafici_campionamento.py`: pdf di Laplace, Laplace/gauss/uniforme, Lloyd-Max M=8, SNR vs bit, errore di quantizzazione, Chebyshev vs esatto, $|H_r(f)|$ interpolatori, SNR vs livello (uniforme/µ/A), soglie equivalenti della µ-law (companding), ripiegamento della frequenza ricostruita. Animazioni GIF (🧩): `grafico-aliasing-animazione.gif` (tempo + spettro, 6 passi), `grafico-aliasing-stroboscopio.gif` (fasori).
Ambiente Python per rigenerarli: venv in `C:\Users\giova\.venvs\wiki-tsd` (fuori da OneDrive e dalla repo).
