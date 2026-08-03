# Flussi operativi di NotebookLM

Passaggi pratici per ogni operazione. Ricorda il principio di base della
SKILL.md: **osserva la pagina, agisci per etichetta visibile, verifica dopo ogni
passo.** Le etichette ("Add", "Create new", ecc.) sono indizi: se non le trovi
identiche, cerca il controllo equivalente per significato.

## Indice
- [Notebook e fonti](#notebook-e-fonti)
- [Chat e domande](#chat-e-domande)
- [Studio: audio e video](#studio-audio-e-video)
- [Studio: report e note](#studio-report-e-note)
- [Condivisione e download](#condivisione-e-download)

---

## Notebook e fonti

### Creare un notebook
1. Vai su `https://notebooklm.google.com`. Si apre la home con la griglia dei
   notebook esistenti.
2. Clic su **"Create new"** (o "+ Create new notebook" / "Nuovo blocco note").
3. Si apre subito la finestra per aggiungere la prima fonte (vedi sotto): un
   notebook non è davvero utile finché non ha almeno una fonte.
4. Per rinominarlo, clic sul titolo in alto e digita il nuovo nome.

### Aprire un notebook esistente
Dalla home, leggi i titoli nella griglia e clicca quello richiesto. Se ce ne
sono molti, usa la barra di ricerca/filtro della home.

### Aggiungere una fonte
1. Nel pannello **Sources** (sinistra) clic su **"+ Add"** (o "Add source").
   Alla creazione del notebook questa finestra compare da sola.
2. Scegli il tipo nella finestra:
   - **Upload / dal computer** → usa lo strumento di upload file del browser per
     selezionare il file locale (PDF, .txt, markdown, audio, ecc.).
   - **Google Drive** → Google Docs o Google Slides.
   - **Link / Website** → incolla l'URL della pagina web.
   - **YouTube** → incolla il link del video (deve essere **pubblico**; viene
     usata solo la trascrizione testuale).
   - **Paste text / Copied text** → incolla testo grezzo.
3. Conferma. La fonte appare nell'elenco quando NotebookLM ha finito di
   processarla (per file grandi o audio può volerci qualche secondo): verifica
   che compaia prima di proseguire.

> Limiti: vedi `references/note-tecniche.md` (numero di fonti per notebook,
> dimensione massima, formati ammessi).

### Scoprire fonti con "Discover"
1. Nel pannello Sources clic su **"Discover"**.
2. Scrivi di cosa hai bisogno (un argomento, una domanda). NotebookLM propone
   fonti dal web con un riassunto.
3. Seleziona quelle utili e aggiungile con un clic.

### Eliminare una fonte
Seleziona la fonte nell'elenco, apri il suo menu (⋮) e scegli **Delete /
Remove**. **Chiedi conferma all'utente prima di eliminare.**

---

## Chat e domande

1. Apri il notebook: le risposte si basano **solo sulle fonti** che contiene.
2. Scrivi la domanda nel campo in basso al centro e invia. In alternativa clicca
   una delle **domande suggerite**.
3. Leggi la risposta dalla pagina e riportala all'utente. Le risposte includono
   **citazioni numerate** che rimandano ai passaggi delle fonti: se l'utente
   vuole verificare, puoi cliccare una citazione per aprire il punto esatto.
4. Per salvare una risposta utile come nota, usa l'azione **"Save to note"** (o
   "Add note") vicino alla risposta.

Suggerimenti:
- Per richieste complesse, fai domande mirate e in sequenza invece di una sola
  domanda enorme.
- Se l'utente chiede qualcosa che non è nelle fonti, NotebookLM lo dirà:
  riportalo onestamente, non inventare.

---

## Studio: audio e video

Gli output dello Studio (pannello destro) sono **asincroni**: si avviano e poi
si attende. Avvia, poi controlla periodicamente; **non riavviare** se è già "in
generazione".

### Audio Overview (il "podcast" a due voci)
1. Nel pannello **Studio** clic su **"Audio Overview"** (genera una
   conversazione tra due host che discutono le tue fonti).
2. *(Opzionale)* Prima di generare, usa **"Customize"** per dare istruzioni
   (es. focalizzati su un capitolo, parla a un pubblico di principianti) o per
   scegliere il **formato**:
   - **Deep Dive** — la conversazione approfondita classica (default).
   - **Brief** — un solo speaker, sintesi sotto i 2 minuti.
   - **Critique** — due host danno un feedback critico/valutazione del
     materiale.
   - **Debate** — due host in un dibattito a confronto.
3. Clic su **Generate**. Compare un riquadro "in generazione": può richiedere
   **diversi minuti**. Avvisa l'utente.
4. Quando è pronto, l'audio appare nello Studio con un player: si può
   **riprodurre**, e tramite il menu (⋮) di solito **scaricare** (file audio) o
   **condividere**.
5. **Modalità interattiva**: durante l'ascolto si può mettere in pausa e fare
   una domanda a voce/testo; gli host rispondono usando le fonti e poi
   riprendono. Segnalalo all'utente se può essergli utile.

### Video Overview
1. Nello Studio clic su **"Video Overview"** (genera un video "deep dive" con
   slide narrate / animazioni, tirando dentro immagini, diagrammi, citazioni e
   numeri dai documenti).
2. *(Opzionale)* "Customize" per indicare taglio, focus o pubblico.
3. **Generate** → attesa di alcuni minuti, come per l'audio.
4. A fine generazione il video è riproducibile nello Studio e in genere
   scaricabile/condivisibile dal suo menu.

---

## Studio: report e note

Sempre dal pannello **Studio**:

- **Mappa mentale (Mind map)**: clic sull'apposito pulsante; genera una mappa
  navigabile dei concetti delle fonti. Espandibile per ramo; di solito
  esportabile come immagine.
- **Report predefiniti**: cerca le opzioni per generare **FAQ**, **Study guide**
  (guida allo studio), **Briefing doc** (documento di sintesi) e **Timeline**.
  In più NotebookLM può proporre un **tipo di report suggerito dall'AI** in base
  alle fonti. Selezionane uno per generarlo; comparirà come nota nello Studio.
- **Note**: clic su **"Add note"** per una nota vuota da scrivere, oppure salva
  una risposta della chat con **"Save to note"**. Le note restano nel notebook
  e possono a loro volta essere usate come contesto.

Dopo aver generato un report, **aprilo e riportane il contenuto** (o i punti
chiave) all'utente; se vuole il file, vedi la sezione download.

---

## Condivisione e download

- **Condividere il notebook**: pulsante **"Share"** in alto a destra. Si può
  invitare via email o creare un link condivisibile. Le opzioni di
  visibilità/permessi dipendono dall'account (personale vs Workspace):
  **leggi ciò che mostra la finestra** e riferiscilo all'utente invece di darlo
  per scontato. Chiedi conferma prima di rendere pubblico un contenuto.
- **Scaricare/condividere un singolo output** (audio, video, mappa): usa il menu
  (⋮) accanto all'output nello Studio.
- **Riportare il link**: copia l'URL del notebook dalla barra degli indirizzi e
  dallo all'utente, così lo ritrova facilmente.
