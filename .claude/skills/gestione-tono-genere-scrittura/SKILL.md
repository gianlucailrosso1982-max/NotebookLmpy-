---
name: gestione-tono-genere-scrittura
description: Costruisce e applica il profilo stilistico personale di Gianluca — tono, lessico, sintassi, ritmo, tic ricorrenti — analizzando testi che ha scritto davvero, e lo salva su file perché sopravviva alla sessione. Usa SEMPRE questa skill quando l'utente chiede di scrivere, riscrivere o rifinire un testo "con il mio stile", "come scrivo io", "con la mia voce", "col mio tono", quando chiede che un testo "non sembri scritto dall'AI" o "suoni come me", quando dice che una bozza "non sembra sua" o "non lo rispecchia", e ogni volta che va prodotto un testo che lui firmerà come proprio — email, lettere, post, articoli, capitoli, introduzioni, presentazioni personali. Attivala anche per costruire o aggiornare il profilo stilistico stesso ("impara il mio stile", "analizza come scrivo", "aggiorna il profilo").
---

# Profilo stilistico personale

Due funzioni distinte: **costruire** il profilo (una volta, poi aggiornarlo) e
**applicarlo** (ogni volta che serve un testo a nome di Gianluca).

Prima di tutto: cerca `profilo-stilistico.md` nella cartella di lavoro.

- **Esiste** → vai direttamente ad APPLICAZIONE.
- **Non esiste** → vai a COSTRUZIONE.

---

# COSTRUZIONE DEL PROFILO

## Fase 0 — Selezione delle fonti (non saltare)

Questa fase esiste perché saltarla rovina tutto il resto.

Un profilo stilistico costruito su testi generati dall'AI non descrive lo stile
di Gianluca: descrive quello del modello. Il risultato è una skill che produce
testi che sembrano suoi e non lo sono — un errore invisibile, quindi grave.

**Ammetti solo testi scritti di suo pugno.** In pratica:

| Ammesso | Escluso |
|---|---|
| Email inviate, messaggi, appunti personali | Manuali e guide prodotti con le skill di manualistica |
| Note grezze del vault scritte a mano | Testi passati per `motore-persuasivo`, `sinergia-persuasiva`, `persuasione-*` |
| Diari, riflessioni, bozze non rifinite | Documenti impaginati o "ripuliti" dall'AI |
| Testi anteriori all'uso dell'AI | Qualsiasi output di cui non sia certa la paternità |

Nel dubbio su un testo, **chiedi** invece di assumere. Segnala esplicitamente
quanti campioni hai scartato e perché.

Attenzione ai vault e alle cartelle miste: contengono spesso sia note autentiche
sia output generati, indistinguibili dal nome del file. Indizi di generazione:
titolazione molto regolare, elenchi puntati simmetrici, tabelle riassuntive,
paragrafi di lunghezza uniforme, assenza di refusi e di frasi lasciate a metà.
Lo stile autentico è più irregolare.

Servono almeno **8-10 campioni** di lunghezza decente. Sotto quella soglia il
profilo è aneddotico: dillo invece di produrlo lo stesso.

## Fase 1 — Raccolta

**Se i testi stanno in una cartella** (vault, Drive, cartella locale): leggili
direttamente, applicando il filtro della Fase 0. Elenca a Gianluca cosa hai
preso e cosa hai scartato, e aspetta conferma prima di analizzare.

**Se li incolla lui:**

- Rispondi solo con: `INIZIA`
- Dopo ogni testo ricevuto rispondi solo con: `CONTINUA`
- Nessun commento, nessuna analisi, nessun riassunto in questa fase
- La fase termina quando scrive: `FINITO`

## Fase 2 — Analisi

Estrai un profilo su sette dimensioni. Per ciascuna, **cita esempi letterali**
dai campioni: un profilo senza prove è un'impressione, non un'analisi.

1. **Tono e registro** — formale/informale, ironico, emotivo, distaccato; come cambia per destinatario
2. **Lessico** — parole ricorrenti, espressioni caratteristiche, termini tecnici e come li introduce
3. **Sintassi** — lunghezza media delle frasi, paratassi vs ipotassi, uso della punteggiatura, incisi
4. **Ritmo** — cadenza, alternanza tra frasi brevi e lunghe, dove accelera e dove rallenta
5. **Struttura** — come apre, come ordina le idee, come chiude, uso di titolazione ed elenchi
6. **Figure e tic** — metafore ricorrenti, domande retoriche, ripetizioni, manierismi riconoscibili
7. **Evitamenti sistematici** — cosa non fa mai: parole, costrutti, mosse retoriche

Poi **scrivi il profilo su `profilo-stilistico.md`** nella cartella di lavoro,
con: data, numero e natura dei campioni, testi scartati e motivo, le sette
dimensioni con esempi, e una sezione finale `## Da verificare` per le dimensioni
su cui i campioni erano insufficienti.

Questo salvataggio è il punto della skill. Senza, il lavoro svanisce a fine
sessione.

## Fase 3 — Taratura

Scrivi un testo di prova su un argomento a scelta di Gianluca. Lui corregge, tu
affini. **A ogni correzione, aggiorna `profilo-stilistico.md`**: le correzioni
sono i dati migliori che avrai, meglio dei campioni iniziali.

---

# APPLICAZIONE

Leggi `profilo-stilistico.md`, poi scrivi rispettando il profilo.

Regole operative:

- Il profilo governa la **forma**, non i contenuti né l'accuratezza dei fatti.
- Se il testo richiede dati o affermazioni fattuali, valgono comunque le regole
  di verifica: componi con `fonti-scientifiche-validate`.
- Se il testo deve anche persuadere, il profilo stilistico ha la precedenza sul
  tono delle skill di persuasione: quelle danno la struttura argomentativa, questa
  dà la voce.
- Non "levigare" il testo. Le irregolarità dello stile di Gianluca sono lo stile:
  toglierle lo fa somigliare a un output generico.
- Se il profilo non copre un caso (registro nuovo, destinatario inedito), dillo e
  proponi due varianti invece di indovinare.

Quando Gianluca corregge una bozza, chiedi se aggiornare il profilo con quella
correzione. Il profilo migliora per uso, non per rifacimenti da zero.
