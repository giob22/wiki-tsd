---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["Intro.pdf#page=6", "Intro.pdf#page=7", "Intro.pdf#page=14", "Intro.pdf#page=21"]
---

# Sistema di comunicazione digitale

## Definizione

> 📄 Fonte: [[Intro.pdf#page=4]], [[Intro.pdf#page=6]], [[Intro.pdf#page=10]]

**Comunicazione**: trasferimento di informazione (voce, audio, video, file, pagine web...) tra punti diversi dello **spazio** (trasmissione) o del **tempo** (memorizzazione) — [[Intro.pdf#page=4]].

Ogni sistema di comunicazione, qualunque sia la sua forma, ha tre elementi base — [[Intro.pdf#page=6]]:
- **trasmettitore** — converte il segnale messaggio in una forma adatta al canale;
- **canale** — mezzo fisico che collega trasmettitore e ricevitore;
- **ricevitore** — ricostruisce dal segnale ricevuto una forma riconoscibile del messaggio originale.

La cascata trasmettitore + ricevitore si chiama anche **transceiver** — [[Intro.pdf#page=6]].

Un sistema è **digitale** quando l'informazione trasferita è rappresentata in forma digitale (di solito cifre binarie, *bit*); è **analogico** quando l'informazione assume un continuo di valori — [[Intro.pdf#page=10]].

## Formule

Il materiale di Intro è qualitativo: nessuna formula. Unici valori numerici (bit rate tipici di sorgente, [[Intro.pdf#page=15]]):

| Applicazione | Bit rate |
|---|---|
| Telefonia fissa convenzionale (voce) | 64 kbit/s |
| Lettori MP3 consumer | 128 kbit/s (tipico) |
| Audio digitale professionale da studio | ≈ 10 × 128 kbit/s ≈ 1.28 Mbit/s |

> 🧩 Derivazione mia: la terza riga è "circa dieci volte" il valore MP3, come dice la slide, non un dato esplicito.

## Derivazioni

Nessun risultato numerico da espandere nella fonte. Il collegamento quantitativo con il bit rate da 64 kbit/s è in [[campionamento-e-aliasing]] e [[dimensionamento-quantizzatore]].

> 💡 Connessione: 64 kbit/s = 8 kHz × 8 bit/campione. La frequenza di campionamento di 8 kHz per la voce è in [[Campionamento_AD_DA.pdf#page=16]] (banda 4 kHz → $f_c \ge 8$ kHz, vedi [[teorema-del-campionamento]]).
> 📚 Fonte esterna: gli 8 bit/campione sono della raccomandazione ITU-T G.711 (vedi [[g711]]); le slide non riportano questo valore.

## Spiegazione

### Processo di comunicazione
> 📄 Fonte: [[Intro.pdf#page=5]], [[Intro.pdf#page=8]], [[Intro.pdf#page=9]]

Passi logici del processo ([[Intro.pdf#page=5]]):
1. generazione del segnale messaggio (voce, musica, immagine, dati);
2. descrizione del messaggio con una certa precisione tramite un insieme di simboli;
3. codifica dei simboli in forma adatta al mezzo fisico;
4. trasmissione dei simboli codificati;
5. decodifica e riproduzione dei simboli originali;
6. ricreazione del messaggio con una degradazione definibile, dovuta a imperfezioni inevitabili.

Il segnale si distorce propagandosi nel canale; in più al ricevitore si sommano **rumore** e **interferenze**. Il segnale ricevuto è quindi una versione corrotta di quello trasmesso ([[Intro.pdf#page=9]]).

> 🎯 Esame: «Il processo di comunicazione, in ogni sistema, è di natura **statistica**» ([[Intro.pdf#page=9]]). Per questo nel corso servono la [[spazio-di-probabilita|teoria della probabilità]] e i processi aleatori.

![[intro-p7-elementi-sistema-comunicazione.png]]
*Sorgente → trasmettitore → canale → ricevitore → utente — [[Intro.pdf#page=7]]*

### Schema a blocchi del sistema digitale
> 📄 Fonte: [[Intro.pdf#page=14]] – [[Intro.pdf#page=20]]

![[intro-p14-schema-sistema-digitale.png]]
*[[Intro.pdf#page=14]]*

| Blocco | Funzione | Pagina |
|---|---|---|
| **Codificatore di sorgente** | Conversione A/D (per sorgenti analogiche) e riduzione della ridondanza, secondo i requisiti dell'utente finale | [[Intro.pdf#page=15]] |
| **Codificatore di canale** | Introduce ridondanza **controllata** contro gli errori del canale; produce una *parola di codice* | [[Intro.pdf#page=16]] |
| **Modulatore** | Traduce simboli (di messaggio o di canale) in forme d'onda analogiche trasmissibili | [[Intro.pdf#page=16]] |
| **Canale** | Distorce la forma d'onda: LTI (risposta impulsiva) per i canali cablati; tempo-variante per il wireless mobile; interferenza di accesso multiplo nel wireless (mezzo broadcast) | [[Intro.pdf#page=17]] |
| **Demodulatore** | Sincronizzazione (sfasamenti di fase, frequenza, tempo; clock non sincronizzati a priori), eventuale equalizzazione, **decisione** sui simboli (*detection*) | [[Intro.pdf#page=19]] |
| **Decodificatore di canale** | Sfrutta la ridondanza per stimare i simboli d'informazione | [[Intro.pdf#page=19]] |
| **Decodificatore di sorgente** | Converte i bit stimati in un formato usabile dall'utente (non per forza quello originale, es. voce → testo) | [[Intro.pdf#page=20]] |

Codifica di canale: per applicazioni insensibili al ritardo si usa rivelazione d'errore + ritrasmissione; per applicazioni real-time si usa correzione d'errore — [[Intro.pdf#page=16]].

Il blocco tratteggiato dello schema (codificatore di canale → ... → decodificatore di canale) è la parte "trasmissiva" su cui si concentra il corso (programma: [[Intro.pdf#page=3]]).

### Rumore termico
> 📄 Fonte: [[Intro.pdf#page=18]]

Il segnale ricevuto è corrotto dal **rumore termico** generato dai componenti elettronici. Un conduttore di resistenza $R$ (Ω) a temperatura sopra lo zero assoluto contiene elettroni liberi in moto casuale, che producono una tensione di rumore ai suoi capi. Il rumore è piccolo, ma diventa un problema quando viene amplificato da un ricevitore ad alto guadagno. Si caratterizza con la meccanica quantistica.

TODO: da espandere — la slide non dà formule (densità spettrale, $kT$); verranno probabilmente con i processi aleatori.

### Perché "going digital"
> 📄 Fonte: [[Intro.pdf#page=10]] – [[Intro.pdf#page=13]]

- **Rigenerazione**: il vantaggio principale. Vedi [[ripetitore-rigenerativo]] ([[Intro.pdf#page=10]], [[Intro.pdf#page=12]]).
- **Basse probabilità d'errore** grazie a rivelazione e correzione d'errore, che non hanno equivalenti analogici ([[Intro.pdf#page=10]]).
- Circuiti digitali più **affidabili** ed **economici**; implementazione **flessibile** (microprocessori, switching digitale, LSI) ([[Intro.pdf#page=13]]).
- *«A bit is a bit»*: dati, telegrafo, telefono e TV vengono trattati come segnali identici ([[Intro.pdf#page=13]]).
- Gestione a **pacchetti**; protezione da interferenza/jamming; crittografia e privacy ([[Intro.pdf#page=13]]).
- Gran parte del traffico è tra computer, che per natura sono terminazioni digitali ([[Intro.pdf#page=13]]).

### Vantaggi dell'approccio digitale e principio di separazione
> 📄 Fonte: [[Intro.pdf#page=21]]

- **Progetto indipendente dalla sorgente**: una volta ridotta in bit, l'informazione si memorizza o trasmette senza interpretarla, e sorgenti diverse condividono lo stesso mezzo.
- **Progetto ottimizzato per il canale**: codifica di canale e modulazione si ottimizzano per ogni collegamento. Siccome i bit vengono rigenerati a ogni tratta, il rumore **non si accumula**.

> 🎯 Esame: lo schema si basa sulla **separazione tra codifica di sorgente e di canale**. Il principio di separazione dà vantaggi pratici ed è **ottimo per collegamenti punto-punto** (risultato di teoria dell'informazione). In certi casi la *codifica congiunta sorgente-canale* dà prestazioni migliori.

**Comunicazioni semantiche** (tema emergente): invece di ricostruire fedelmente la sequenza di bit, si trasmette il *significato* della sorgente. La codifica semantica estrae le caratteristiche utili al compito che il ricevitore deve svolgere ([[Intro.pdf#page=21]]).

## Perché importa

È il quadro di riferimento di tutto il corso: ogni argomento del programma ([[Intro.pdf#page=3]]) corrisponde a un blocco dello schema:
- modulazione digitale → modulatore/demodulatore;
- stima dei parametri e sincronizzazione → demodulatore;
- canali selettivi in frequenza → canale ed equalizzazione;
- teoria dell'informazione e codifica di canale → codificatore/decodificatore di canale;
- conversione A/D → codificatore di sorgente ([[teorema-del-campionamento]], [[quantizzazione-uniforme]]).

## Connessioni

- [[conversione-ad-da]] — è la prima parte del codificatore di sorgente per sorgenti analogiche ([[Intro.pdf#page=15]]).
- [[spazio-di-probabilita]] — la natura statistica della comunicazione ([[Intro.pdf#page=9]]) motiva lo studio della probabilità.
- [[ripetitore-rigenerativo]] — è il meccanismo concreto del vantaggio del digitale.
- [[snr-di-quantizzazione]] — la "degradazione definibile" del passo 6 ha, per la quantizzazione, una misura precisa.

## Fonti

- [[intro-corso]] — sommario della fonte
- [[Intro.pdf#page=4]] – [[Intro.pdf#page=21]]

_Aggiornato: 2026-09-23 — creazione da ingest Intro.pdf_
