# Index — Trasmissione dei Segnali Digitali

## Overview
- [[overview]] — panoramica del corso, programma, copertura
- [[lezioni]] — elenco lezioni con gli argomenti in ordine di PDF
- [[corso-completo]] — il corso in un unico file schematico, lezioni 1–7 nell'ordine delle slide (solo contenuto dei PDF; PDF di studio con `output/crea_pdf.py`)
- [[mie-considerazioni]] — ragionamenti personali salvati durante lo studio, non detti a lezione (pagina separata anche sul sito)

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
- [[equivalente-banda-base-dei-filtri]] — $y = s \ast h/\sqrt2$ con la dimostrazione degli appunti, quattro filtri reali (alta)

**Processi aleatori**
- [[processo-aleatorio]] — realizzazioni e v.a. a $t_0$, sinusoide a fase casuale, distribuzioni di ordine $k$ e marginali, DF del processo di Bernoulli, tempo discreto (alta)
- [[momenti-di-un-processo]] — media, autocorrelazione, autocovarianza, mutue correlazioni; indipendenti/incoerenti/incorrelati; processi complessi; momenti del rettangolo (non stazionario) e della sinusoide (WSS) (alta)
- [[stazionarieta]] — ordine $k$, SSS, primo e secondo ordine, WSS; SSS ⇒ WSS (alta)
- [[autocorrelazione-processi-wss]] — lag-acf, proprietà, $\rho_{XX}$, tempo di decorrelazione (alta)
- [[processi-e-sistemi-lti]] — $\mu_Y = \mu_X H(0)$, $R_{YY} = R_{XX} \ast h \ast h(-\tau)$, $S_{YY} = S_{XX}|H|^2$ (alta)
- [[densita-spettrale-di-potenza]] — definizione, Wiener-Khinchin, $2\Delta f\,S_{XX}$, proprietà, PSD mutue e della somma (alta)
- [[processo-gaussiano]] — gaussiana multivariata; WSS ⇒ SSS; incorrelati ⇒ indipendenti (alta)

**Processi passa-banda**
- [[processi-passa-banda]] — processo analitico, inviluppo complesso e componenti I/Q di un processo; teorema: $x_c$, $x_s$ congiuntamente WSS; $R_{x_cx_c} = R_{x_sx_s}$, $R_{x_cx_s} = -R_{x_sx_c}$; $R_{xx} = 2R_{x_cx_c} + 2jR_{x_sx_c}$ (alta)
- [[psd-componenti-in-quadratura]] — $S_{x_cx_c}$ (13), $S_{xx} = 2S_{x_px_p}(f+f_c)u(f+f_c)$ (14), cross-PSD, spettro simmetrico ⇒ componenti incoerenti (alta)
- [[rumore-in-banda-passante]] — PSD $N_0/2$ in banda $W$: $S_{w_cw_c} = N_0/2$, $S_{ww} = N_0$, potenza $N_0W$; costruzione grafica (alta)

**Modulazione e rivelazione**
- [[principi-di-modulazione]] — mapper e generatore, $R_s=R_b/\log_2M$, memoria, compromesso potenza-banda (alta)
- [[spazio-dei-segnali]] — rappresentazione vettoriale, $D=WT_0$, base ortonormale, Gram-Schmidt (alta)
- [[modulazione-lineare]] — NRZ/RZ, I/Q, PSK, QAM, PAM, Gray, PSD $\frac{E|\xi|^2}{T}|G_{TX}|^2$ (alta)
- [[modulazione-ortogonale]] — FSK, spaziatura $1/(2T)$ e $1/T$ (media)
- [[rivelazione-map-ml]] — test di ipotesi, MAP, irrilevanza, statistica sufficiente, ML (alta)
- [[ricevitore-ottimo-awgn]] — correlatori, filtro adattato, minima distanza, Voronoi (alta)
- [[probabilita-errore-binaria]] — on-off, antipodale, ortogonale, $\frac12\text{erfc}(d/2\sqrt{N_0})$ (alta)
- [[probabilita-errore-m-aria]] — QPSK, union bound, primi vicini, 16-QAM (alta)

**Stima e sincronizzazione**
- [[sincronizzazione]] — modello con ritardo e offset dell'LO, timing e portante, stima ML della fase (alta)
- [[stima-dei-parametri]] — MLE, classico e bayesiano, stima d'ampiezza training-based e blind (tanh) (alta)
- [[phase-locked-loop]] — steepest ascent, PLL, termine d'errore, Costas loop (alta)

**Canali a banda limitata**
- [[interferenza-intersimbolica]] — ISI, perdita di SNR e BER floor, modello con $p=g\ast h\ast c$ (alta)
- [[criterio-di-nyquist]] — ISI nulla, sinc, coseno rialzato, filtri a radice di coseno rialzato (RRC), $W=(1+\alpha)R_b/\eta_B$ (alta)
- [[equalizzazione]] — equalizzazione frazionaria, ZF e MMSE con formule, DFE, MLSE con $\alpha(n)$ e $\beta(\ell)$ (alta)

**OFDM (Lezione 15)**
- [[ofdm]] — multiportante, FDM e OFDM, impulsi $\phi_i(t)$ ortonormali, $\Delta f=1/T_u$, ISI e ICI, correlatori, PSD somma di sinc² (alta)
- [[prefisso-ciclico]] — $T_g\ge T_h$, niente ISI né ICI, convoluzione circolare, $Y_n[k]=H[k]a_k[n]+W_n[k]$, prezzo del CP (alta)
- [[ofdm-con-fft]] — campionamento a $T_u/N$ = IDFT, matrice DFT unitaria, trasmettitore e ricevitore completi (alta)
- [[equalizzazione-ofdm]] — matrice diagonale, ZF e MMSE a una presa, nulli spettrali, codifica e interleaving, modulazione adattativa (alta)
- [[limiti-dell-ofdm]] — PAPR, offset di frequenza ($C_m(\epsilon_f)$) e di tempo, scelta di $N$ (media)

**Parametri globali e capacità**
- [[informazione-mutua-e-capacita]] — $I(X;Y)=H(Y)-H(Y\mid X)$, $C=\max_{p(x)}I$, teorema di Shannon, $C=W\log_2(1+\gamma)$ (alta)
- [[parametri-globali-modulazioni]] — banda di Shannon, $E_b$, $\text{SNR}=\frac{E_b}{N_0}\eta_B$, $\eta_B$, $\eta_P$, tabella PAM/PSK/QAM/ortogonali (alta)
- [[limite-di-shannon]] — frontiera $E_b/N_0\ge(2^{\eta_B}-1)/\eta_B$, limite $-1.59$ dB, regioni limitate in banda e in potenza (alta)
- [[link-budget]] — rumore $kT_0FW$, sensibilità, Friis, path loss massimo (media)

## Entità
- [[ripetitore-rigenerativo]] — dispositivo
- [[g711]] — standard ITU-T PCM voce
- [[legge-mu]] — algoritmo di compressione (µ = 255)
- [[legge-a]] — algoritmo di compressione (A = 87.6)
- [[algoritmo-lloyd-max]] — quantizzatore ottimo MMSE
- [[algoritmo-di-viterbi]] — cammino ottimo in un traliccio (ACS), usato per la MLSE
- [[ieee-802-11a]] — standard Wi-Fi OFDM: $N=64$, $L_{cp}=16$, 48 portanti dati, 12–72 Mbit/s non codificati
- [[fft]] — algoritmo veloce per DFT/IDFT, $O(N\log N)$: il cuore dell'OFDM

## Fonti
- [[intro-corso]] — Intro.pdf, pp. 1–21
- [[elementi-teoria-probabilita]] — Probabilità.pdf, pp. 1–38
- [[campionamento-conversione-ad-da]] — Campionamento_AD_DA.pdf, pp. 1–43
- [[rappresentazione-complessa-banda-base]] — Rappresentazione_Rice.pdf, pp. 1–27 (19 slide + 8 pagine di appunti a mano)
- [[processi-aleatori]] — random_processes.pdf, pp. 1–46 (41 slide + 5 pagine di appunti a mano)
- [[laboratorio-conversione-ad]] — scripts/09_28_2006: AD_conversion.m + 3 figure (laboratorio, non d'esame)
- [[rappresentazione-processi-passa-banda]] — Rappresentazione_Rice_processi.pdf, pp. 1–25 (13 slide + 12 pagine di appunti a mano)
- [[principles-of-modulation]] — goodnotes/Modulazione.pdf, pp. 1–39 (23 slide + 16 pagine di appunti)
- [[elementi-teoria-rivelazione]] — goodnotes/Detection.pdf, pp. 1–18 (dispense + 8 pagine di appunti)
- [[appunti-lezione-28-ottobre]] — goodnotes/Lezione 10-28.pdf, pp. 1–4
- [[appunti-lezione-2-novembre]] — goodnotes/Lezione 11-2.pdf, pp. 1–3
- [[parametri-globali-e-capacita]] — Confronto_new.pdf, pp. 1–33 (slide con note a mano)
- [[parameter-estimation-synchronization]] — goodnotes/Synchro_Kay_example (1).pdf, pp. 1–36, e goodnotes/11-9.pdf, pp. 1–2
- [[signaling-bandlimited-channels]] — signaling_bandlimited_channel_NEW.pdf, pp. 1–61 (versione aggiornata del 23/11), con gli appunti di goodnotes/signaling_bandlimited_channel.pdf (versione precedente, 47 pagine)
- [[signaling-ofdm]] — ofdm_goldsmith_slides.pdf, pp. 1–58 (53 slide della Lezione 15 con appunti, più 5 pagine di soli appunti)
- [[note-gelli-multiportante]] — Note 2001 Gelli G.pdf, pp. 1–24 (dispensa di G. Gelli, **approfondimento, non d'esame**)
- [[appunti-sparsi-lezioni]] — goodnotes/Lezioni.pdf, pp. 1–3 (DFT, ripasso di Rice)

## Approfondimenti (non materia d'esame)
Letture facoltative fornite a lezione, tenute separate dalle pagine d'esame (cartella `wiki/approfondimenti/`, pagina «Approfondimenti» sul sito).
- [[multiportante-ofdm-dmt-gelli]] — note di G. Gelli (2001): multiportante, OFDM e DMT, prestazioni QAM, tempo di guardia, DFT, prefisso ciclico, bit loading e water filling; notazioni a confronto con la Lezione 15

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
- [[link-budget-wlan]] — bit rate, sensibilità e portata di un collegamento WLAN (media)
- [[dimensionamento-ofdm]] — spaziatura, prefisso, efficienza e bit rate di un sistema OFDM; 802.11a (bassa)

## Esame
_nessun materiale ancora — lancia `prepara esame`_

## Asset
Figure in `raw/assets/`: 3 da Intro, 7 da Probabilità, 29 da Campionamento, 11 da Rappresentazione_Rice (di cui 4 pagine di appunti a mano), 6 da random_processes (nome `file-pN-descrizione.png`).
3 da Rappresentazione_Rice_processi (`processi-passabanda-pN-*.png`: vista grafica delle PSD, costruzione grafica del rumore in banda).
1 da Confronto_new (`confronto-p23-efficienza-banda-potenza.png`: piano efficienza spettrale – $E_b/N_0$).
Figure del laboratorio in `raw/assets/lab-0928-*.png` (3, copiate da `raw/scripts/09_28_2006/`).
Grafici 🧩 del laboratorio — script `genera_grafici_laboratorio_ad.py` (replica Python di AD_conversion.m): setup e spettro, spettro del campionato, durata della convoluzione e taglio, confronto interpolatori, quantizzazione, SNR vs bit, esempio 2; animazione `grafico-lab-interpolazione.gif`.
Grafici 🧩 dei processi aleatori — script `genera_grafici_random_processes.py`: realizzazioni e v.a. a $t_0$, processo lento contro veloce (autocorrelazione e PSD), gaussiana bivariata, animazione della costruzione di $R_{XX}(\tau)$ (`grafico-rp-autocorrelazione.gif`).
Grafici 🧩 della lezione sulla banda base — script `genera_grafici_rappresentazione_rice.py`: catena degli spettri $S_p \to S_p^+ \to S$, componenti I/Q nel tempo, animazione della downconversion (`grafico-rice-downconversion.gif`).
Grafici di funzione generati (🧩) in `output/grafici/` — script `genera_grafici_campionamento.py`: pdf di Laplace, Laplace/gauss/uniforme, Lloyd-Max M=8, SNR vs bit, errore di quantizzazione, Chebyshev vs esatto, $|H_r(f)|$ interpolatori, SNR vs livello (uniforme/µ/A), soglie equivalenti della µ-law (companding), ripiegamento della frequenza ricostruita. Animazioni GIF (🧩): `grafico-aliasing-animazione.gif` (tempo + spettro, 6 passi), `grafico-aliasing-stroboscopio.gif` (fasori).
Grafici 🧩 delle Lezioni 13–14 — script `genera_grafici_lezioni13_14.py`: verosimiglianza blind, curva d'errore del PLL, coseno rialzato, ISI da errore di timing.
Grafici 🧩 della Lezione 15 — script `genera_grafici_lezione15.py`: ricevitore FDM della slide 5 con il flusso del segnale blocco per blocco (esempio QPSK), PSD dell'OFDM (somma di sinc²), potenza utile e ICI con offset di frequenza, CCDF del PAPR per $N=16,64,256$. Ridisegni 🧩 dei disegni a mano degli appunti (p. 4, 9, 10, 13, 14) — script `genera_figure_appunti_lezione15.py`: S/P polifase, simboli più lunghi e banda più stretta, canale piatto sulla sottoportante, griglia ISI/ICI, calcolo dell'ortogonalità. Grafico 🧩 dell'approfondimento di Gelli — script `genera_grafici_approfondimenti.py`: water filling su 8 sottoportanti.

Copie GoodNotes di tutti i PDF delle lezioni (versioni annotate più recenti, tranne Intercorso.pdf) in `raw/goodnotes/`: i file già presenti in `raw/` hanno il suffisso « (GoodNotes)»; la cartella `matlab/` contiene gli script del laboratorio.
Ambiente Python per rigenerarli: venv in `C:\Users\giova\.venvs\wiki-tsd` (fuori da OneDrive e dalla repo).
