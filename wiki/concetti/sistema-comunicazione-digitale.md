---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["Intro.pdf#page=6", "Intro.pdf#page=7", "Intro.pdf#page=14", "Intro.pdf#page=21"]
---

# Sistema di comunicazione digitale

## Definizione · [[Intro.pdf#page=4|p. 4]], [[Intro.pdf#page=6|p. 6]], [[Intro.pdf#page=10|p. 10]]

**Comunicazione**: trasferimento di informazione (voce, audio, video, file, pagine web...) tra punti diversi dello **spazio** (trasmissione) o del **tempo** (memorizzazione).

Ogni sistema di comunicazione, qualunque sia la sua forma, ha tre elementi base — p. 6:
- **trasmettitore** — converte il segnale messaggio in una forma adatta al canale;
- **canale** — mezzo fisico che collega trasmettitore e ricevitore;
- **ricevitore** — ricostruisce dal segnale ricevuto una forma riconoscibile del messaggio originale.

La cascata trasmettitore + ricevitore si chiama anche **transceiver**.

Un sistema è **digitale** quando l'informazione trasferita è rappresentata in forma digitale (di solito cifre binarie, *bit*); è **analogico** quando l'informazione assume un continuo di valori.

## Formule · [[Intro.pdf#page=15|p. 15]]

Il materiale di Intro è qualitativo: nessuna formula. Unici valori numerici (bit rate tipici di sorgente):

| Applicazione | Bit rate |
|---|---|
| Telefonia fissa convenzionale (voce) | 64 kbit/s |
| Lettori MP3 consumer | 128 kbit/s (tipico) |
| Audio digitale professionale da studio | ≈ 10 × 128 kbit/s ≈ 1.28 Mbit/s |

> 🧩 Derivazione mia: la terza riga è "circa dieci volte" il valore MP3, come dice la slide, non un dato esplicito.

## Derivazioni · [[Campionamento_AD_DA.pdf#page=16|p. 16]]

Nessun risultato numerico da espandere nella fonte. Il collegamento quantitativo con il bit rate da 64 kbit/s è in [[campionamento-e-aliasing]] e [[dimensionamento-quantizzatore]].

> 💡 Connessione: 64 kbit/s = 8 kHz × 8 bit/campione. La frequenza di campionamento di 8 kHz per la voce è in p. 16 (banda 4 kHz → $f_c \ge 8$ kHz, vedi [[teorema-del-campionamento]]).
> 📚 Fonte esterna: gli 8 bit/campione sono della raccomandazione ITU-T G.711 (vedi [[g711]]); le slide non riportano questo valore.

## Spiegazione

### Processo di comunicazione · [[Intro.pdf#page=5|p. 5]], [[Intro.pdf#page=7|p. 7]]–[[Intro.pdf#page=9|9]]

Passi logici del processo:
1. generazione del segnale messaggio (voce, musica, immagine, dati);
2. descrizione del messaggio con una certa precisione tramite un insieme di simboli;
3. codifica dei simboli in forma adatta al mezzo fisico;
4. trasmissione dei simboli codificati;
5. decodifica e riproduzione dei simboli originali;
6. ricreazione del messaggio con una degradazione definibile, dovuta a imperfezioni inevitabili.

Il segnale si distorce propagandosi nel canale; in più al ricevitore si sommano **rumore** e **interferenze**. Il segnale ricevuto è quindi una versione corrotta di quello trasmesso.

> 🎯 Esame: «Il processo di comunicazione, in ogni sistema, è di natura **statistica**». Per questo nel corso servono la [[spazio-di-probabilita|teoria della probabilità]] e i processi aleatori.

![[intro-p7-elementi-sistema-comunicazione.png]]
*Sorgente → trasmettitore → canale → ricevitore → utente*

### Schema a blocchi del sistema digitale · [[Intro.pdf#page=3|p. 3]], [[Intro.pdf#page=14|p. 14]]–[[Intro.pdf#page=17|17]], [[Intro.pdf#page=19|p. 19]], [[Intro.pdf#page=20|20]]

![[intro-p14-schema-sistema-digitale.png]]

| Blocco | Funzione |
|---|---|
| **Codificatore di sorgente** | Conversione A/D (per sorgenti analogiche) e riduzione della ridondanza, secondo i requisiti dell'utente finale |
| **Codificatore di canale** | Introduce ridondanza **controllata** contro gli errori del canale; produce una *parola di codice* |
| **Modulatore** | Traduce simboli (di messaggio o di canale) in forme d'onda analogiche trasmissibili |
| **Canale** | Distorce la forma d'onda: LTI (risposta impulsiva) per i canali cablati; tempo-variante per il wireless mobile; interferenza di accesso multiplo nel wireless (mezzo broadcast) |
| **Demodulatore** | Sincronizzazione (sfasamenti di fase, frequenza, tempo; clock non sincronizzati a priori), eventuale equalizzazione, **decisione** sui simboli (*detection*) |
| **Decodificatore di canale** | Sfrutta la ridondanza per stimare i simboli d'informazione |
| **Decodificatore di sorgente** | Converte i bit stimati in un formato usabile dall'utente (non per forza quello originale, es. voce → testo) |

Codifica di canale: per applicazioni insensibili al ritardo si usa rivelazione d'errore + ritrasmissione; per applicazioni real-time si usa correzione d'errore.

Il blocco tratteggiato dello schema (codificatore di canale →... → decodificatore di canale) è la parte "trasmissiva" su cui si concentra il corso (programma: p. 3).

### Rumore termico · Intro [[Intro.pdf#page=18|p. 18]] · Processi [[random_processes.pdf#page=2|p. 2]]

Il segnale ricevuto è corrotto dal **rumore termico** generato dai componenti elettronici. Un conduttore di resistenza $R$ (Ω) a temperatura sopra lo zero assoluto contiene elettroni liberi in moto casuale, che producono una tensione di rumore ai suoi capi. Il rumore è piccolo, ma diventa un problema quando viene amplificato da un ricevitore ad alto guadagno. Si caratterizza con la meccanica quantistica.

TODO: da espandere — la slide non dà formule (densità spettrale, $kT$). Le slide sui processi aleatori citano il rumore termico come esempio di segnale aleatorio ([[processo-aleatorio]]) e danno gli strumenti per descriverlo ([[densita-spettrale-di-potenza]], [[processo-gaussiano]]), ma non il suo modello quantitativo.

### Perché "going digital" · [[Intro.pdf#page=10|p. 10]], [[Intro.pdf#page=12|p. 12]], [[Intro.pdf#page=13|13]]

- **Rigenerazione**: il vantaggio principale. Vedi [[ripetitore-rigenerativo]].
- **Basse probabilità d'errore** grazie a rivelazione e correzione d'errore, che non hanno equivalenti analogici.
- Circuiti digitali più **affidabili** ed **economici**; implementazione **flessibile** (microprocessori, switching digitale, LSI).
- *«A bit is a bit»*: dati, telegrafo, telefono e TV vengono trattati come segnali identici.
- Gestione a **pacchetti**; protezione da interferenza/jamming; crittografia e privacy.
- Gran parte del traffico è tra computer, che per natura sono terminazioni digitali.

### Vantaggi dell'approccio digitale e principio di separazione · [[Intro.pdf#page=21|p. 21]]

- **Progetto indipendente dalla sorgente**: una volta ridotta in bit, l'informazione si memorizza o trasmette senza interpretarla, e sorgenti diverse condividono lo stesso mezzo.
- **Progetto ottimizzato per il canale**: codifica di canale e modulazione si ottimizzano per ogni collegamento. Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula**.

> 🎯 Esame: lo schema si basa sulla **separazione tra codifica di sorgente e di canale**. Il principio di separazione dà vantaggi pratici ed è **ottimo per collegamenti punto-punto** (risultato di teoria dell'informazione). In certi casi la *codifica congiunta sorgente-canale* dà prestazioni migliori.

**Comunicazioni semantiche** (tema emergente): invece di ricostruire fedelmente la sequenza di bit, si trasmette il *significato* della sorgente. La codifica semantica estrae le caratteristiche utili al compito che il ricevitore deve svolgere.

## Perché importa · [[Intro.pdf#page=3|p. 3]]

È il quadro di riferimento di tutto il corso: ogni argomento del programma corrisponde a un blocco dello schema:
- rappresentazione complessa in banda base → come modulatore e demodulatore lavorano in banda base, con upconverter e downconverter verso il canale ([[inviluppo-complesso]], [[upconversion-e-downconversion]]);
- modulazione digitale → modulatore/demodulatore ([[modulazione-digitale]]);
- stima dei parametri e sincronizzazione → demodulatore;
- canali selettivi in frequenza → canale ed equalizzazione;
- teoria dell'informazione e codifica di canale → codificatore/decodificatore di canale;
- conversione A/D → codificatore di sorgente ([[teorema-del-campionamento]], [[quantizzazione-uniforme]]).

## Connessioni · Intro [[Intro.pdf#page=9|p. 9]], [[Intro.pdf#page=15|p. 15]], [[Intro.pdf#page=16|16]] · Rice [[Rappresentazione_Rice.pdf#page=3|p. 3]], [[Rappresentazione_Rice.pdf#page=21|p. 21]]

- [[conversione-ad-da]] — è la prima parte del codificatore di sorgente per sorgenti analogiche.
- [[spazio-di-probabilita]] — la natura statistica della comunicazione motiva lo studio della probabilità.
- [[ripetitore-rigenerativo]] — è il meccanismo concreto del vantaggio del digitale.
- [[snr-di-quantizzazione]] — la "degradazione definibile" del passo 6 ha, per la quantizzazione, una misura precisa.
- [[modulazione-digitale]] — il modulatore «traduce simboli in forme d'onda»; la lezione sulla banda base ne dà un primo esempio, la modulazione lineare binaria.
- [[inviluppo-complesso]] — modulatore e demodulatore lavorano sull'inviluppo complesso in banda base; il canale fisico, tra upconverter e downconverter, si vede come un unico canale in banda base.

## Fonti · [[Intro.pdf#page=4|p. 4]], [[Intro.pdf#page=21|p. 21]]

- [[intro-corso]] — sommario della fonte

_Aggiornato: 2026-09-28 — rumore termico: collegamenti ai processi aleatori; 2026-09-25 — collegamenti a modulazione digitale e inviluppo complesso (ingest Rappresentazione_Rice.pdf); 2026-09-23 — creazione da ingest Intro.pdf_
