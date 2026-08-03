# Note tecniche, limiti e problemi comuni

## Tipi di fonte supportati
- PDF
- Google Docs e Google Slides (da Google Drive)
- Pagine web (URL)
- Testo incollato / Markdown / `.txt`
- Video **YouTube** (devono essere pubblici; viene usata solo la trascrizione)
- File **audio** (es. mp3)
- **EPUB**

## Limiti tipici (account consumer, possono cambiare)
- Fino a **~50 fonti per notebook**.
- Ogni fonte fino a **~500.000 parole**.
- Le operazioni dello Studio (Audio/Video Overview) sono **asincrone** e
  richiedono **minuti**, non secondi.

Questi numeri evolvono: se la UI mostra un limite diverso, fidati di quello che
vedi e riferiscilo all'utente.

## Niente API pubblica per i consumer
Non esiste un'API pubblica di NotebookLM per gli account personali. Google
offre solo una **API enterprise** (su Google Cloud, riservata ai clienti
aziendali). Perciò:
- Per un utente normale, l'automazione passa **sempre** dall'interfaccia web via
  Claude in Chrome.
- Non promettere integrazioni via API/REST/chiave: non sono disponibili per il
  suo account, salvo che l'utente dica di avere NotebookLM Enterprise.

## Problemi comuni e cosa fare

**Compare la schermata di login Google.**
→ Fermati. Chiedi all'utente di accedere a Google nel suo Chrome e di avvisarti
quando è pronto. Non inserire credenziali tu.

**Non trovo un pulsante che mi aspettavo (es. "Audio Overview").**
→ La UI potrebbe essere cambiata o l'elemento è in un menu. Rileggi tutta la
pagina, controlla menu a tendina / "More" / icone (⋮), e usa uno screenshot per
orientarti. Se davvero non c'è, dillo all'utente invece di tirare a indovinare.

**La generazione audio/video sembra ferma.**
→ È lenta per natura. Aspetta, ricarica il pannello Studio dopo qualche minuto e
ricontrolla. Non avviare una seconda generazione: rischi duplicati.

**Una fonte non viene accettata.**
→ Verifica il tipo (vedi sopra) e, per YouTube, che il video sia pubblico.
Audio/PDF molto grandi impiegano più tempo a essere processati: attendi che la
fonte compaia nell'elenco prima di proseguire.

**Più account Google nel browser.**
→ NotebookLM usa l'account attivo in Chrome. Se il notebook atteso non c'è,
chiedi all'utente se è sul profilo/account Google giusto.

**Lingua dell'output.**
→ NotebookLM genera nella lingua impostata nell'account/interfaccia. Se l'utente
vuole l'Audio Overview in italiano ma esce in un'altra lingua, verifica le
impostazioni di lingua del notebook o dell'account.

## Limiti onesti di questo approccio
Pilotare una UC web di terze parti è potente ma fragile: i layout cambiano, le
operazioni sono lente e alcuni passaggi (login, captcha, permessi di
condivisione) richiedono l'intervento umano. Quando qualcosa non si può fare in
automatico, la cosa giusta è spiegarlo all'utente e proporre il passo manuale,
non simulare un successo.
