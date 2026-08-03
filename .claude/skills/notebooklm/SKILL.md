---
name: notebooklm
description: >-
  Comanda Google NotebookLM da Claude tramite il browser (Claude in Chrome):
  crea e apre notebook, aggiunge fonti (PDF, Google Docs, Google Slides, link
  web, video YouTube, testo, audio, EPUB), fa domande sulle fonti e genera gli
  output dello Studio — Audio Overview (il "podcast" a due voci), Video
  Overview, mappe mentali, riassunti, study guide, briefing doc, FAQ, timeline
  e note. Usa SEMPRE questa skill quando l'utente nomina "NotebookLM" o
  "Notebook LM", o quando chiede di "creare un notebook", "aggiungere una
  fonte", "fai un podcast / audio overview dalle mie fonti", "riassumi questi
  documenti in NotebookLM", "chiedi a NotebookLM", "genera una mappa mentale /
  study guide / briefing", anche in inglese (create a notebook, add a source,
  make an audio overview, ask NotebookLM, generate a video overview). Serve a
  controllare NotebookLM senza API ufficiali, pilotando l'interfaccia web nel
  Chrome dove l'utente è già loggato con Google.
---

# NotebookLM — controllo via browser

Questa skill permette a Claude di **pilotare Google NotebookLM**
(`https://notebooklm.google.com`) per conto dell'utente, usando gli strumenti
**Claude in Chrome**.

NotebookLM **non ha un'API pubblica per gli account consumer** (esiste solo una
API enterprise riservata alle aziende su Google Cloud). Per un utente normale,
quindi, l'unico modo affidabile di "comandarlo" è guidarne l'interfaccia web nel
browser dove l'utente è già autenticato con Google. È quello che fa questa
skill.

## Prerequisiti — controlla SEMPRE prima di iniziare

1. **Claude in Chrome deve essere attivo.** Verifica che gli strumenti del
   browser siano disponibili (es. elencando i browser connessi). Se non lo
   sono, spiega all'utente che per usare questa skill serve l'estensione
   *Claude in Chrome* collegata, e fermati.
2. **L'utente deve essere loggato con Google in Chrome.** NotebookLM richiede un
   account Google. Se dopo aver aperto il sito vedi una schermata di login,
   **non inserire tu credenziali**: chiedi all'utente di accedere nel suo Chrome
   e di dirti quando è pronto.

## Come pilotare NotebookLM (principio di base)

NotebookLM è una *single-page app* che Google aggiorna spesso, e le operazioni
pesanti (audio, video) sono **asincrone** e richiedono minuti. Per essere
affidabile, **non affidarti a selettori CSS fissi o a posizioni memorizzate**.
Lavora così, un passo alla volta:

1. **Vai e osserva.** Naviga all'URL e *leggi lo stato attuale della pagina*
   (estrai il testo / l'albero della pagina) **prima** di agire. Capisci dove
   sei: la home con la lista dei notebook, oppure dentro un notebook.
2. **Trova per etichetta visibile.** Individua i controlli dal loro testo o
   ruolo visibile ("Create new", "Add", "Discover", "Audio Overview", il campo
   della chat in basso…), non da coordinate fisse. Le etichette esatte possono
   cambiare: usa quelle indicate nei riferimenti come *indizi*, non come verità
   assoluta.
3. **Agisci e verifica.** Dopo ogni azione (clic, digitazione, upload) rileggi
   la pagina per confermare che sia successo ciò che ti aspettavi, poi prosegui.
   Non incatenare azioni alla cieca.
4. **Usa la vista quando il testo non basta.** Se non riesci a individuare un
   elemento dal testo della pagina, fai uno screenshot e ragiona visivamente.
5. **Pazienza con le operazioni asincrone.** Avviato un Audio o Video Overview,
   **non riavviarlo**: controlla periodicamente lo Studio (ricaricando se
   serve) finché l'output risulta pronto. Avvisa l'utente che può volerci
   qualche minuto.
6. **Niente credenziali.** Se compare il login, fermati e chiedi all'utente di
   accedere a Google da solo.

## Layout di un notebook

Aperto un notebook, ci sono tre pannelli:

- **Sources** (sinistra): le fonti caricate. Qui si aggiungono/eliminano fonti e
  c'è il pulsante **Discover** per farne scoprire di nuove dal web.
- **Chat** (centro): si fanno domande sulle fonti; in basso c'è il campo di
  testo, in alto eventuali "domande suggerite".
- **Studio** (destra): si generano gli output — Audio Overview, Video Overview,
  mappa mentale, report (FAQ, study guide, briefing doc, timeline, ecc.) e note.

## Cosa puoi fare → dove guardare

Per i passaggi dettagliati, apri il file di riferimento indicato.

| L'utente vuole… | Apri |
| --- | --- |
| Creare o aprire un notebook; aggiungere/eliminare fonti; usare Discover | `references/flussi.md` → "Notebook e fonti" |
| Fare domande sulle fonti / chattare | `references/flussi.md` → "Chat e domande" |
| Audio Overview (il podcast) e Video Overview | `references/flussi.md` → "Studio: audio e video" |
| Riassunti, study guide, briefing doc, FAQ, mappa mentale, timeline, note | `references/flussi.md` → "Studio: report e note" |
| Condividere un notebook o scaricare un output | `references/flussi.md` → "Condivisione e download" |
| Limiti, tipi di fonte ammessi, problemi comuni | `references/note-tecniche.md` |

## Avvio rapido (vale per qualsiasi richiesta)

1. Verifica i prerequisiti qui sopra.
2. Apri (o porta in primo piano) una scheda su `https://notebooklm.google.com` e
   leggi la pagina per capire lo stato.
3. Identifica quale flusso serve dalla tabella e leggi la sezione corrispondente
   in `references/flussi.md`.
4. Esegui i passi uno alla volta, verificando dopo ciascuno.
5. Al termine, riferisci all'utente il risultato in modo concreto (es. "Notebook
   *Tesi* creato con 3 fonti; Audio Overview in generazione, ti avviso quando è
   pronto") e, se utile, condividi il link del notebook.

## Buone abitudini

- **Conferma prima di azioni distruttive.** Non eliminare notebook o fonti senza
  l'ok esplicito dell'utente.
- **Una cosa alla volta, dichiarata.** Se la richiesta è composta ("crea un
  notebook con questi 3 PDF e fammi un podcast"), enuncia il piano e procedi in
  ordine, verificando.
- **Sii sincero sui limiti.** Se la UI è cambiata e non trovi un controllo,
  dillo e proponi un'alternativa, invece di inventare clic.
- **Riferisci i link.** Quando crei o apri un notebook, riporta l'URL così
  l'utente può ritrovarlo.
