---
tipo: fonte
titolo: "Complex baseband representation (rappresentazione complessa in banda base)"
file_raw: "Rappresentazione_Rice.pdf"
pagine: "1-27"
data_ingest: 2026-09-25
formato: slide-pdf
argomenti: [modulazione, segnali in banda base e passa-banda, banda monolatera e bilatera, banda stretta, segnale analitico, trasformata di Hilbert, inviluppo complesso, componenti in fase e quadratura, energia, upconversion, downconversion, equivalente in banda base dei filtri]
---

# Complex baseband representation — Rappresentazione_Rice.pdf

## Sommario

Slide in inglese intitolate *Complex baseband representation*, del corso "Trasmissione dei segnali digitali" (Laurea Magistrale in Ingegneria Informatica, Università di Napoli Federico II), docente Donatella Darsena, a.a. 2026-27 ([[Rappresentazione_Rice.pdf#page=1]]). Trattano il primo tema del programma: la rappresentazione complessa in banda base. Il PDF contiene anche **appunti scritti a mano**: otto pagine intere (p. 2, 6, 8, 14, 18, 19, 21, 24), nella versione aggiornata del 2026-09-28, e annotazioni sopra alcune slide. Gli appunti sono integrati nel wiki come fonte, citando la pagina.

La lezione parte dalla modulazione: i bit diventano forme d'onda che devono stare in una porzione di spettro. Poi definisce i segnali in banda base e in banda passante, la banda monolatera e bilatera e i segnali a banda stretta. L'idea centrale è che un segnale passa-banda reale ha tutta l'informazione in un segnale complesso in banda base, l'**inviluppo complesso**. Ci si arriva in due passi:
1. il **segnale analitico** tiene le sole frequenze positive, con un fattore $\sqrt2$, e nel tempo si scrive con la **trasformata di Hilbert**;
2. la traslazione di $-f_c$ lo porta in banda base.

Seguono:
- le componenti **in fase e in quadratura**, con $s_p = \sqrt2\,s_c\cos - \sqrt2\,s_s\sin$;
- la **conservazione dell'energia**, garantita dal $\sqrt2$;
- gli schemi di **upconversion e downconversion**;
- l'**equivalente in banda base di un filtro passa-banda**, $y = s * h/\sqrt2$, realizzato con quattro filtri reali;
- la definizione di banda per i segnali complessi.

### Corrispondenza pagine PDF ↔ slide

Il numero di pagina del PDF non coincide con quello stampato sulla slide, perché le pagine di appunti sono intercalate.

| Pagina PDF | Contenuto | Pagina PDF | Contenuto |
|---|---|---|---|
| 1 | slide 1 (titolo) | 15 | slide 11 |
| 2 | appunti a mano | 16 | slide 12 |
| 3 | slide 2 | 17 | slide 13 |
| 4 | slide 3 | 18 | appunti a mano |
| 5 | slide 4 | 19 | appunti a mano |
| 6 | appunti a mano | 20 | slide 14 |
| 7 | slide 5 | 21 | appunti a mano |
| 8 | appunti a mano | 22 | slide 15 |
| 9 | slide 6 | 23 | slide 16 |
| 10 | slide 7 | 24 | appunti a mano |
| 11 | slide 8 | 25 | slide 17 |
| 12 | slide 9 | 26 | slide 18 |
| 13 | slide 10 | 27 | slide 19 |
| 14 | appunti a mano | | |

## Punti chiave

1. La modulazione rappresenta l'informazione digitale con forme d'onda analogiche; nell'esempio, simboli ±1 per impulsi rettangolari traslati (modulazione lineare). Le forme d'onda reali sono spesso vincolate in frequenza ([[Rappresentazione_Rice.pdf#page=3]], slide 2; appunti [[Rappresentazione_Rice.pdf#page=2]]).
2. Definizioni: banda base $S_b(f) \approx 0$ per $|f| > B$; banda passante $S_p(f) \approx 0$ per $|f \pm f_c| > B/2$, con $f_c > B > 0$. Le stesse valgono per i canali LTI ([[Rappresentazione_Rice.pdf#page=4]], slide 3).
3. Per i segnali reali $X(f) = X^*(-f)$, e la banda bilatera è il doppio della monolatera. "Banda" indica la monolatera. Banda stretta: $B/f_c \ll 1$ ([[Rappresentazione_Rice.pdf#page=5]], [[Rappresentazione_Rice.pdf#page=7]], slide 4–5).
4. Tutta l'informazione di un segnale passa-banda reale sta nel suo inviluppo complesso, campionabile a frequenza molto più bassa. Il DSP lavora in banda base e l'elaborazione analogica si riduce al minimo: fuori dal DSP restano upconversion e downconversion ([[Rappresentazione_Rice.pdf#page=9]], [[Rappresentazione_Rice.pdf#page=10]], slide 6–7).
5. Segnale analitico: $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$. Nel tempo $s_p^+ = \frac{1}{\sqrt2}s_p + \frac{j}{\sqrt2}\widehat{s}_p$, dove $\widehat{s}_p = s_p * \frac{1}{\pi t}$ è la trasformata di Hilbert. Si torna indietro con $s_p = \sqrt2\,\text{Re}\{s_p^+\}$, e vale $\widehat{S}_p = -j\,\text{sgn}(f)\,S_p$ ([[Rappresentazione_Rice.pdf#page=11]] – [[Rappresentazione_Rice.pdf#page=13]], slide 8–10).
6. Inviluppo complesso: $S(f) = S_p^+(f + f_c)$, cioè $s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c + js_s$. Ritorno: $s_p = \sqrt2\,\text{Re}\{s\,e^{j2\pi f_c t}\} = \sqrt2 s_c\cos(2\pi f_c t) - \sqrt2 s_s\sin(2\pi f_c t)$; in frequenza $S_p(f) = [S(f - f_c) + S^*(-f - f_c)]/\sqrt2$ ([[Rappresentazione_Rice.pdf#page=15]], [[Rappresentazione_Rice.pdf#page=16]], slide 11–12).
7. Le portanti modulate di I e Q sono ortogonali; $\langle u_p, v_p\rangle = \text{Re}\{\langle u, v\rangle\}$, quindi $\|s_p\|^2 = \|s\|^2$ ([[Rappresentazione_Rice.pdf#page=17]], slide 13; dimostrazione con Parseval negli appunti [[Rappresentazione_Rice.pdf#page=18]]).
8. Downconversion: $\sqrt2\,s_p\cos(2\pi f_c t) = s_c + s_c\cos(4\pi f_c t) - s_s\sin(4\pi f_c t)$, poi passa-basso; per Q si usa $-\sqrt2\sin$ ([[Rappresentazione_Rice.pdf#page=20]], slide 14). La fase dovuta a $f_c$ è prevedibile e non porta informazione ([[Rappresentazione_Rice.pdf#page=22]], slide 15).
9. Filtro passa-banda in banda base: $Y(f) = \frac{1}{\sqrt2}S(f)H(f)$ e $y = \frac{1}{\sqrt2}s * h$, con quattro convoluzioni reali per I e Q ([[Rappresentazione_Rice.pdf#page=23]] – [[Rappresentazione_Rice.pdf#page=26]], slide 16–18).
10. La banda di un segnale complesso si misura attorno all'origine, contando frequenze positive e negative ([[Rappresentazione_Rice.pdf#page=27]], slide 19).

## Concetti introdotti

- [[modulazione-digitale]]
- [[segnali-banda-base-e-passa-banda]]
- [[segnale-analitico]] (con la trasformata di Hilbert)
- [[inviluppo-complesso]]
- [[upconversion-e-downconversion]]
- [[equivalente-banda-base-dei-filtri]]

Grafici 🧩 in `output/grafici/` (script `genera_grafici_rappresentazione_rice.py`): catena degli spettri, componenti I/Q nel tempo, animazione della downconversion.

## Appunti a mano

Cosa aggiungono alle slide, nella versione del PDF aggiornata il 2026-09-28. Pagine intere di appunti in **grassetto**; le altre sono note scritte sopra le slide.

| Pagina | Contenuto | Dove nel wiki |
|---|---|---|
| **[[Rappresentazione_Rice.pdf#page=2]]** | catena sorgente → MOD → canale; definizione del modulatore; $H(f)$ di un canale passa-banda; il trasmettitore porta il segnale nella sua porzione di spettro, il ricevitore in banda base (segnale complesso); complesso → reale in Tx, reale → complesso in Rx, eseguiti da un DSP | [[modulazione-digitale]], [[upconversion-e-downconversion]], [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=3]] | definizione di modulazione in italiano; $s(t) = \sum_m b[m]\,\Pi(t - mT)$, $b \in \{-1, 1\}$; «lineare perché $s(t)$ dipende linearmente dai simboli»; vincoli in frequenza su dove sta lo spettro | [[modulazione-digitale]] |
| [[Rappresentazione_Rice.pdf#page=4]] | «si dice banda passante se»; «il contenuto informativo è traslato e centrato attorno a $f_c$»; nota incompleta «altrimenti c'è…» | [[segnali-banda-base-e-passa-banda]] |
| [[Rappresentazione_Rice.pdf#page=5]] | simmetria hermitiana dei segnali reali; «l'obiettivo è svincolarsi dalla $f_c$», perché l'informazione non dipende da $f_c$ | [[segnali-banda-base-e-passa-banda]] |
| **[[Rappresentazione_Rice.pdf#page=6]]** | vantaggi della banda base: costi hardware del campionamento, modularità e indipendenza, algoritmi generalizzabili | [[inviluppo-complesso]] |
| **[[Rappresentazione_Rice.pdf#page=8]]** | definizioni riscritte (larghezza di banda, monolatera e bilatera, banda stretta $B/f_c \ll 1$); «non è un'ipotesi stringente» | [[segnali-banda-base-e-passa-banda]] |
| [[Rappresentazione_Rice.pdf#page=9]] | slide 6 in italiano: il vantaggio del campionamento a frequenza bassa, DSP complessi in digitale, elaborazione analogica al minimo | [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=10]] | macroblocchi modulatore (DSP + upconversion) e demodulatore; «si ottiene l'inviluppo complesso in banda base»; «ci si è svincolati dalla frequenza carrier» | [[inviluppo-complesso]], [[modulazione-digitale]], [[upconversion-e-downconversion]] |
| [[Rappresentazione_Rice.pdf#page=11]] – [[Rappresentazione_Rice.pdf#page=13]] | scopo del segnale analitico; frequenze negative ridondanti; $\sqrt2$ «per motivi energetici»; antitrasformata del gradino; lettura della (8) (parte reale e parte immaginaria); «relazione inversa immediata»; correzione $S \to S_p$; sfasamento di ∓90° | [[segnale-analitico]] |
| **[[Rappresentazione_Rice.pdf#page=14]]** | $\mathcal{F}[\text{sgn}(t)] = \frac{1}{j\pi f}$ passo per passo; $\mathcal{F}[1/(\pi t)]$ (con il segno sbagliato) | [[segnale-analitico]] |
| [[Rappresentazione_Rice.pdf#page=15]] – [[Rappresentazione_Rice.pdf#page=16]] | (14) come relazione inversa e parte tagliata da $u(f)$; la (15) è una traslazione del segnale analitico; nomi di $s_c$, $s_s$; «quadratura: prodotto ortogonale nullo»; passaggi verso la (16)–(17) | [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=17]] | $s_p = x_c + x_s$ (segno da correggere); «sotto» per la dimostrazione; prodotto scalare; «energia di $s_p$», «energia è reale» | [[inviluppo-complesso]] |
| **[[Rappresentazione_Rice.pdf#page=18]]** | dimostrazione della (18) con Parseval, con l'ipotesi di banda stretta in rosso; verifica della (19) | [[inviluppo-complesso]] |
| **[[Rappresentazione_Rice.pdf#page=19]]** | fine della verifica della (19); energia (20) | [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=20]] | S → MOD, «esce l'inviluppo»; termini a $2f_c$ «tagliati dal filtro» | [[upconversion-e-downconversion]], [[modulazione-digitale]] |
| **[[Rappresentazione_Rice.pdf#page=21]]** | upconverter + canale + downconverter come un unico canale; energia conservata grazie al $\sqrt2$ | [[upconversion-e-downconversion]], [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=22]] | «l'inviluppo complesso ci permette di separare le variazioni lente introdotte dalla modulazione in banda base» | [[inviluppo-complesso]], [[upconversion-e-downconversion]] |
| **[[Rappresentazione_Rice.pdf#page=24]]** | dimostrazione della (22): trucchi $u \to u^2$ e $\cdot\sqrt2/\sqrt2$; passaggio al tempo, (23) | [[equivalente-banda-base-dei-filtri]] |
| [[Rappresentazione_Rice.pdf#page=26]] | catena delle (24)–(25); $y(t)$ «segnale in banda base» verso il DSP «che lavora in banda base» | [[equivalente-banda-base-dei-filtri]] |

Le pagine 1, 7, 23, 25 e 27 non hanno note scritte: al più sottolineature ed evidenziazioni.

## Refusi rilevati

> ⚠️ [[Rappresentazione_Rice.pdf#page=13]] (slide 10): nella (12) e in $\widehat{S}_p(f) = -j\,S(f)\,\text{sgn}(f)$ compare $S(f)$ invece di $S_p(f)$. È corretto a mano nel PDF.
> ⚠️ Appunti della versione aggiornata: $\mathcal{F}[1/(\pi t)] = j\,\text{sign}(f)$ senza il meno (p.14); $X_s$ con un meno in più (p.18); $s_p = x_c + x_s$ invece di $x_c - x_s$ e «proprietà (10)» invece della (19) (note sulla slide 13, p.17); indice della somma nella formula della modulazione (p.3). Dettagli nelle pagine concetto.
> ⚠️ [[Rappresentazione_Rice.pdf#page=15]] e [[Rappresentazione_Rice.pdf#page=25]] (slide 11 e 17): nelle figure $A$ e $B$ sono altezze, non bande. Da non confondere con la banda $B$.
> ⚠️ [[Rappresentazione_Rice.pdf#page=26]] (slide 18): la figura omette il fattore $1/\sqrt2$ delle (24)–(25).
> ⚠️ Refusi di inglese senza effetto sul contenuto: «unite step-function» (slide 8), «Though lowpass filtering» (slide 14).

## Domande aperte

- La dimostrazione dell'ortogonalità (18) è rimandata al libro ([[Rappresentazione_Rice.pdf#page=17]]). Nella versione aggiornata è negli appunti di [[Rappresentazione_Rice.pdf#page=18]], con l'ipotesi di banda stretta scritta in rosso: gli spettri attorno a $+f_c$ e $-f_c$ non si sovrappongono perché $B \ll f_c$. Nel wiki la condizione minima è resa esplicita come $W < f_c$ ([[inviluppo-complesso]]).
- La (19) è data senza dimostrazione nella slide; la verifica è negli appunti di p.18–19, dove i termini a $2f_c$ sono «circa 0» per $B/f_c \ll 1$ ([[inviluppo-complesso]]).
- Nota di p.2: il passaggio complesso ↔ reale è «eseguito da un DSP», mentre nello schema della slide 7 upconversion e downconversion sono passi distinti dal DSP. Da chiarire ([[upconversion-e-downconversion]]).
- Il nome del file, "Rappresentazione_Rice", richiama la *rappresentazione di Rice*, nome con cui è nota in letteratura la scrittura (17) di un segnale passa-banda in componenti in fase e quadratura. 📚 Fonte esterna: il nome non compare nelle slide. Da confermare a lezione.
- La slide 19 definisce la banda di un segnale complesso come «la più piccola banda attorno all'origine» che contiene la maggior parte del segnale. Per uno spettro non simmetrico attorno a 0, come in figura slide 11, non è specificato se l'intervallo debba essere simmetrico.

## Domande da esame

- Definire segnali e canali in banda base e in banda passante. Cos'è la banda monolatera e perché per un segnale reale la bilatera è il doppio? Cos'è un segnale a banda stretta?
- Definire il segnale analitico e ricavarne l'espressione nel tempo con la trasformata di Hilbert. Perché c'è $\sqrt2$? Perché la corrispondenza con $s_p$ è biunivoca?
- Definire l'inviluppo complesso e le componenti I/Q. Ricavare $s_p = \sqrt2 s_c\cos - \sqrt2 s_s\sin$ e $S_p(f)$ in funzione di $S(f)$.
- Dimostrare che l'energia dell'inviluppo è uguale a quella del segnale passa-banda.
- Disegnare e spiegare upconversion e downconversion. Perché serve il passa-basso?
- Ricavare l'equivalente in banda base di un filtro passa-banda e la sua realizzazione con filtri reali.
- Perché conviene elaborare i segnali in banda base?

_Aggiornato: 2026-09-28 — re-ingest della versione con appunti a mano (27 pagine): tabella di corrispondenza, tabella degli appunti rifatta, domande aperte aggiornate, revisione di copertura totale; 2026-09-25 — ingest iniziale e revisione di copertura totale vs PDF_
