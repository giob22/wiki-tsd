---
tipo: fonte
titolo: "Complex baseband representation (rappresentazione complessa in banda base)"
file_raw: "Rappresentazione_Rice.pdf"
pagine: "1-23"
data_ingest: 2026-09-25
formato: slide-pdf
argomenti: [modulazione, segnali in banda base e passa-banda, banda monolatera e bilatera, banda stretta, segnale analitico, trasformata di Hilbert, inviluppo complesso, componenti in fase e quadratura, energia, upconversion, downconversion, equivalente in banda base dei filtri]
---

# Complex baseband representation — Rappresentazione_Rice.pdf

## Sommario

Slide in inglese intitolate *Complex baseband representation*, del corso "Trasmissione dei segnali digitali" (Laurea Magistrale in Ingegneria Informatica, Università di Napoli Federico II), docente Donatella Darsena, a.a. 2026-27 ([[Rappresentazione_Rice.pdf#page=1]]). Trattano il primo tema del programma: la rappresentazione complessa in banda base. Il PDF contiene anche **appunti scritti a mano**: quattro pagine intere (p. 2, 7, 16, 18) e annotazioni sopra alcune slide. Gli appunti sono integrati nel wiki come fonte, citando la pagina.

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
| 1 | slide 1 (titolo) | 13 | slide 11 |
| 2 | appunti a mano | 14 | slide 12 |
| 3 | slide 2 | 15 | slide 13 |
| 4 | slide 3 | 16 | appunti a mano |
| 5 | slide 4 | 17 | slide 14 |
| 6 | slide 5 | 18 | appunti a mano |
| 7 | appunti a mano | 19 | slide 15 |
| 8 | slide 6 | 20 | slide 16 |
| 9 | slide 7 | 21 | slide 17 |
| 10 | slide 8 | 22 | slide 18 |
| 11 | slide 9 | 23 | slide 19 |
| 12 | slide 10 | | |

## Punti chiave

1. La modulazione rappresenta l'informazione digitale con forme d'onda analogiche; nell'esempio, simboli ±1 per impulsi rettangolari traslati (modulazione lineare). Le forme d'onda reali sono spesso vincolate in frequenza ([[Rappresentazione_Rice.pdf#page=3]], slide 2; appunti [[Rappresentazione_Rice.pdf#page=2]]).
2. Definizioni: banda base $S_b(f) \approx 0$ per $|f| > B$; banda passante $S_p(f) \approx 0$ per $|f \pm f_c| > B/2$, con $f_c > B > 0$. Le stesse valgono per i canali LTI ([[Rappresentazione_Rice.pdf#page=4]], slide 3).
3. Per i segnali reali $X(f) = X^*(-f)$, e la banda bilatera è il doppio della monolatera. "Banda" indica la monolatera. Banda stretta: $B/f_c \ll 1$ ([[Rappresentazione_Rice.pdf#page=5]], [[Rappresentazione_Rice.pdf#page=6]], slide 4–5).
4. Tutta l'informazione di un segnale passa-banda reale sta nel suo inviluppo complesso, campionabile a frequenza molto più bassa. Il DSP lavora in banda base; l'hardware analogico fa solo upconversion e downconversion ([[Rappresentazione_Rice.pdf#page=8]], [[Rappresentazione_Rice.pdf#page=9]], slide 6–7).
5. Segnale analitico: $S_p^+(f) = \sqrt2\,S_p(f)\,u(f)$. Nel tempo $s_p^+ = \frac{1}{\sqrt2}s_p + \frac{j}{\sqrt2}\widehat{s}_p$, dove $\widehat{s}_p = s_p * \frac{1}{\pi t}$ è la trasformata di Hilbert. Si torna indietro con $s_p = \sqrt2\,\text{Re}\{s_p^+\}$, e vale $\widehat{S}_p = -j\,\text{sgn}(f)\,S_p$ ([[Rappresentazione_Rice.pdf#page=10]] – [[Rappresentazione_Rice.pdf#page=12]], slide 8–10).
6. Inviluppo complesso: $S(f) = S_p^+(f + f_c)$, cioè $s(t) = s_p^+(t)\,e^{-j2\pi f_c t} = s_c + js_s$. Ritorno: $s_p = \sqrt2\,\text{Re}\{s\,e^{j2\pi f_c t}\} = \sqrt2 s_c\cos(2\pi f_c t) - \sqrt2 s_s\sin(2\pi f_c t)$; in frequenza $S_p(f) = [S(f - f_c) + S^*(-f - f_c)]/\sqrt2$ ([[Rappresentazione_Rice.pdf#page=13]], [[Rappresentazione_Rice.pdf#page=14]], slide 11–12).
7. Le portanti modulate di I e Q sono ortogonali; $\langle u_p, v_p\rangle = \text{Re}\{\langle u, v\rangle\}$, quindi $\|s_p\|^2 = \|s\|^2$ ([[Rappresentazione_Rice.pdf#page=15]], slide 13; dimostrazione con Parseval negli appunti [[Rappresentazione_Rice.pdf#page=16]]).
8. Downconversion: $\sqrt2\,s_p\cos(2\pi f_c t) = s_c + s_c\cos(4\pi f_c t) - s_s\sin(4\pi f_c t)$, poi passa-basso; per Q si usa $-\sqrt2\sin$ ([[Rappresentazione_Rice.pdf#page=17]], slide 14). La fase dovuta a $f_c$ è prevedibile e non porta informazione ([[Rappresentazione_Rice.pdf#page=19]], slide 15).
9. Filtro passa-banda in banda base: $Y(f) = \frac{1}{\sqrt2}S(f)H(f)$ e $y = \frac{1}{\sqrt2}s * h$, con quattro convoluzioni reali per I e Q ([[Rappresentazione_Rice.pdf#page=20]] – [[Rappresentazione_Rice.pdf#page=22]], slide 16–18).
10. La banda di un segnale complesso si misura attorno all'origine, contando frequenze positive e negative ([[Rappresentazione_Rice.pdf#page=23]], slide 19).

## Concetti introdotti

- [[modulazione-digitale]]
- [[segnali-banda-base-e-passa-banda]]
- [[segnale-analitico]] (con la trasformata di Hilbert)
- [[inviluppo-complesso]]
- [[upconversion-e-downconversion]]
- [[equivalente-banda-base-dei-filtri]]

Grafici 🧩 in `output/grafici/` (script `genera_grafici_rappresentazione_rice.py`): catena degli spettri, componenti I/Q nel tempo, animazione della downconversion.

## Appunti a mano

Cosa aggiungono alle slide:

| Pagina | Contenuto | Dove nel wiki |
|---|---|---|
| [[Rappresentazione_Rice.pdf#page=2]] | catena sorgente → MOD → canale; $H(f)$ di un canale passa-banda; ruolo di trasmettitore e ricevitore | [[modulazione-digitale]], [[segnali-banda-base-e-passa-banda]] |
| [[Rappresentazione_Rice.pdf#page=3]] | i segnali vanno allocati in porzioni dello spettro | [[modulazione-digitale]] |
| [[Rappresentazione_Rice.pdf#page=5]] | "simmetria hermitiana"; "l'obiettivo è sbarazzarsi di $f_c$" | [[segnali-banda-base-e-passa-banda]] |
| [[Rappresentazione_Rice.pdf#page=7]] | banda stretta: $B \ll f_c$ | [[segnali-banda-base-e-passa-banda]] |
| [[Rappresentazione_Rice.pdf#page=10]] – [[Rappresentazione_Rice.pdf#page=12]] | $\sqrt2$ "per motivi energetici"; nomi dei termini della (8); (10) legata alla simmetria del segnale reale; correzione $S \to S_p$ | [[segnale-analitico]] |
| [[Rappresentazione_Rice.pdf#page=14]] | nomi di $s_p^+$, $s_c$, $s_s$; "quadratura: prodotto [scalare] nullo" | [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=16]] | dimostrazione di $\langle x_c, x_s\rangle = 0$ con Parseval | [[inviluppo-complesso]] |
| [[Rappresentazione_Rice.pdf#page=17]] | S → MOD collegato a $s_c$, $s_s$ dell'upconverter | [[upconversion-e-downconversion]] |
| [[Rappresentazione_Rice.pdf#page=18]] | upconverter + canale + downconverter come un unico canale; energia conservata grazie al $\sqrt2$ | [[upconversion-e-downconversion]], [[inviluppo-complesso]] |

## Refusi rilevati

> ⚠️ [[Rappresentazione_Rice.pdf#page=12]] (slide 10): nella (12) e in $\widehat{S}_p(f) = -j\,S(f)\,\text{sgn}(f)$ compare $S(f)$ invece di $S_p(f)$. È corretto a mano nel PDF.
> ⚠️ [[Rappresentazione_Rice.pdf#page=16]] (appunti): nella riga $X_c(f) = \sqrt2 S_c(f) * [\delta(f - f_c) - \delta(f + f_c)]/2$ il segno tra le delta dev'essere $+$ (coseno).
> ⚠️ [[Rappresentazione_Rice.pdf#page=13]] e [[Rappresentazione_Rice.pdf#page=21]] (slide 11 e 17): nelle figure $A$ e $B$ sono altezze, non bande. Da non confondere con la banda $B$.
> ⚠️ [[Rappresentazione_Rice.pdf#page=22]] (slide 18): la figura omette il fattore $1/\sqrt2$ delle (24)–(25).
> ⚠️ Refusi di inglese senza effetto sul contenuto: «unite step-function» (slide 8), «Though lowpass filtering» (slide 14).

## Domande aperte

- La dimostrazione dell'ortogonalità (18) è rimandata al libro ([[Rappresentazione_Rice.pdf#page=15]]); negli appunti di p.16 manca l'ipotesi che rende nulli i termini incrociati. Ricostruita nel wiki con l'ipotesi esplicita $W < f_c$ ([[inviluppo-complesso]]).
- La (19) è data senza dimostrazione: ricostruita nel wiki con lo stesso argomento (termini a $2f_c$ nulli per banda $< f_c$).
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

_Aggiornato: 2026-09-25 — ingest iniziale e revisione di copertura totale vs PDF_
