# Strumenti, ambienti e fallback — manuale operativo

Leggi questo file all'inizio della **Fase 3** (recupero del testo) e ogni volta che uno strumento fallisce. Spiega cosa fa davvero ciascuno strumento, cosa non può fare, e come degradare con onestà quando un canale è chiuso.

## Indice

1. Riconoscere l'ambiente in cui stai girando
2. WebSearch — cosa restituisce davvero
3. WebFetch — limiti e segnali di blocco
4. Connettore MCP PubMed — inventario e usi
5. Connettore MCP Consensus — usi e cautele
6. Altri connettori possibili
7. Tabella dei fallback per ogni bisogno
8. Gestione degli errori: quando riprovare, quando fermarsi
9. Budget di chiamate per modalità
10. Il registro delle ricerche (riproducibilità)

---

## 1. Riconoscere l'ambiente

La stessa skill gira su superfici con capacità diverse. Prima di cercare, guarda quali strumenti hai davvero e adatta il piano; dichiara nella risposta le limitazioni incontrate.

| Superficie | Ricerca web | Lettura pagine | Connettori MCP | Shell/script | Note |
|---|---|---|---|---|---|
| Claude Code (locale) | `WebSearch` | `WebFetch`, `curl` | quelli configurati dall'utente | sì | rete di norma aperta |
| Claude Code (web/remoto) | `WebSearch` | `WebFetch` **spesso bloccato** da proxy di rete; anche `curl` passa dal proxy | quelli del progetto (es. PubMed, Consensus) | sì | i connettori MCP passano per canali autenticati e di norma funzionano anche quando il fetch è bloccato |
| claude.ai (chat) | `web_search` | `web_fetch` | connettori attivati dall'utente | code execution se attiva | serve la ricerca web abilitata |
| Cowork | come claude.ai | come claude.ai | connettori dell'app | sì | filesystem locale |

Come capire se un dominio è bloccato: l'errore riporta `EGRESS_BLOCKED` o «blocked by the network egress proxy». Non è un errore tuo né della fonte: è la policy dell'ambiente. Non riprovare sullo stesso dominio più di una volta; passa al fallback.

Se non hai **né** ricerca web **né** connettori, la skill non può verificare nulla: dillo subito all'utente, offri di lavorare su testi che lui incolla, e non produrre schede con dati «ricordati».

---

## 2. WebSearch — cosa restituisce davvero

- Restituisce **link + snippet sintetizzati**, e talvolta un riassunto pre-digerito con numeri dentro. Quel riassunto è prodotto da un modello, non è la fonte: **serve a scegliere cosa aprire, non a citare**. Un numero letto solo in uno snippet non è citabile; se non riesci ad aprire la fonte, il dato resta «non verificato».
- `allowed_domains` limita i risultati, ma il matching avviene sul **dominio registrabile**: chiedendo `pubmed.ncbi.nlm.nih.gov` puoi ricevere anche `ncbi.nlm.nih.gov/pmc` o altre proprietà NCBI. Controlla che ogni risultato appartenga al livello che stavi interrogando.
- Passa liste di domini **brevi e omogenee per livello** (5–10 domini per chiamata): liste lunghe diluiscono la ricerca. Per L0 sanitario, ad esempio: `cochranelibrary.com, who.int, nice.org.uk, uspreventiveservicestaskforce.org, effectivehealthcare.ahrq.gov, snlg.iss.it`.
- Le query in **inglese** rendono molto di più; per le fonti italiane (ISS, AIFA) usa l'italiano.
- La ricerca è orientata agli Stati Uniti: per fonti europee o italiane vincola i domini.
- Ogni risposta che usa risultati di ricerca deve chiudere con l'elenco delle fonti linkate: coincide con la sezione «Fonti» della scheda.

---

## 3. WebFetch — limiti e segnali di blocco

- Converte la pagina in testo e risponde a un prompt sul contenuto: chiedi cose precise («riporta i risultati numerici della sezione Results con gli intervalli di confidenza», «riporta la sezione Funding e Competing interests»), non «riassumi».
- I redirect verso un altro host **non vengono seguiti**: ti viene restituito l'URL di destinazione, richiama lo strumento su quello (tipico dei link `doi.org`, che rimandano all'editore).
- Cache di 15 minuti per URL.
- **Siti che non si leggono senza browser** (app JavaScript): PubPeer, la ricerca di Epistemonikos, Lens, l'interfaccia di Semantic Scholar, molte pagine editoriali. Usa le API (sezione 5 di `gerarchia-fonti.md`) o il record PubMed.
- **Paywall**: se la pagina mostra solo l'abstract, hai letto l'abstract: scrivilo nella scheda («letto: abstract; full text non accessibile»).
- **Blocco di rete**: errore `EGRESS_BLOCKED`. Nessun tentativo ulteriore sullo stesso dominio; passa a MCP o dichiara «non verificato (accesso bloccato)».

---

## 4. Connettore MCP PubMed — inventario e usi

Quando è presente, è il canale più affidabile per L0 sanitario (via abstract Cochrane) e L1, e funziona anche quando WebFetch è bloccato.

| Strumento | Cosa fa | Quando usarlo |
|---|---|---|
| `search_articles` | Ricerca con sintassi PubMed (campi, MeSH, booleani, `[pt]`, date) | Fase 2, per ogni quesito biomedico |
| `get_article_metadata` | Titolo, abstract completo, autori con affiliazioni, rivista, date, MeSH, `article_types`, PMCID, DOI | Fase 3 (lettura dell'abstract) e Fase 4: `article_types` contiene «Retracted Publication» se ritrattato; il PMCID dice se il full text è libero |
| `get_full_text_article` | Full text degli articoli in PMC open access | Fase 3–4: metodi, Funding, Competing interests, tabelle |
| `find_related_articles` | Articoli correlati | Allargare la ricerca quando i risultati sono pochi |
| `lookup_article_by_citation` | Da una citazione testuale al record | Verificare citazioni che l'utente ha incollato |
| `convert_article_ids` | PMID ↔ PMCID ↔ DOI | Costruire link corretti |
| `get_copyright_status` | Licenza del full text | Prima di riprodurre tabelle o testi lunghi |

Obbligo di attribuzione del connettore: ogni uso va dichiarato («secondo PubMed…») e ogni articolo citato porta il DOI come link. Questi obblighi si integrano nella scheda (riga Link, elenco Fonti); non la sostituiscono.

Il connettore copre **solo biomedicina e scienze della vita**: per fisica, informatica, economia, scienze sociali non mediche usa gli altri canali.

---

## 5. Connettore MCP Consensus — usi e cautele

- Cerca su un corpus multi-fonte (Semantic Scholar, PubMed, Scopus, arXiv) e restituisce titoli, abstract, conteggi di citazioni, quartile della rivista, URL. Ottimo per **scoprire** letteratura fuori dalla biomedicina e per stimare quanto un lavoro è stato ripreso.
- Non applicare filtri (anno, tipo di studio, dimensione campionaria…) se l'utente non li ha chiesti: il connettore lo richiede, e i filtri escludono evidenza valida.
- I riassunti e le «risposte» generate da Consensus sono **contenuti generati da IA**: valgono come snippet, non come lettura. Apri sempre il paper (via URL o via PubMed).
- Obblighi di formato del connettore: citazioni numerate inline, elenco finale con link esatti, messaggio finale riportato verbatim. Si integrano nella scheda: i numeri delle citazioni vanno nell'elenco «Fonti», il messaggio in coda alla risposta.
- Limite: al massimo 3 ricerche per volta; in caso di rate limit, attendi 30 secondi prima di riprovare, una sola volta.

---

## 6. Altri connettori possibili

La skill può incontrare connettori per ClinicalTrials.gov, ChEMBL, bioRxiv, Open Targets, Europe PMC, OpenAlex. Regola generale: verifica che esistano *in questa sessione* prima di pianificare su di essi; se esistono, hanno la precedenza sul fetch per lo stesso compito; se non esistono, non nominarli nella risposta come se li avessi usati.

---

## 7. Tabella dei fallback per ogni bisogno

| Bisogno | Canale primario | Fallback 1 | Fallback 2 | Se tutto fallisce, scrivi |
|---|---|---|---|---|
| Trovare revisioni sistematiche (sanità) | MCP PubMed con `systematic review[pt]` | WebSearch con domini L0 | Consensus con query mirata | «ricerca eseguita su …; nessuna revisione sistematica reperibile con i canali disponibili» |
| Leggere l'abstract con i numeri | MCP PubMed `get_article_metadata` | WebFetch sul record PubMed o sull'editore | Europe PMC REST | «abstract non accessibile: dato non verificato» |
| Leggere metodi, Funding, COI | MCP PubMed `get_full_text_article` (se PMC) | WebFetch sull'editore (se OA) | Unpaywall → repository | «full text non accessibile: conflitti d'interesse non verificati» |
| Controllare ritrattazioni | `article_types` nei metadati PubMed | API Crossref `works/<DOI>` | Retraction Watch database (se raggiungibile) | «ritrattazione: non verificata (strumento non accessibile)» |
| Segnalazioni post-pubblicazione | PubPeer (best effort) | scite (citazioni contrastanti) | — | «post-pubblicazione: non verificato» |
| Legittimità della rivista | indicizzazione MEDLINE (il record PubMed esiste) | DOAJ | SCImago | «rivista non verificata» |
| Corrispondenza col protocollo | API ClinicalTrials.gov v2 | pagina web del registro | PROSPERO (revisioni) | «protocollo non confrontato (registro non accessibile)» |
| Attualità | data nei metadati + ricerca di aggiornamenti con filtro data | «Update in» nel record PubMed | — | «aggiornamenti non verificati» |
| Rischio di base per l'effetto assoluto | gruppo di controllo della revisione (SoF) | registri/statistiche L4 | — | «effetto assoluto non riportato nella fonte» |

---

## 8. Gestione degli errori

- **Un solo tentativo di ripetizione** per errore transitorio (timeout, 5xx, rate limit). Un blocco di rete o un 403 non sono transitori: nessuna ripetizione.
- **Non cambiare fonte per aggirare un blocco verso una fonte più debole** senza dirlo: se Cochrane è bloccato e ripieghi su un blog che la riassume, il blog non è una fonte; cerca il record PubMed della revisione.
- **Registra ogni fallimento** nella nota «Metodo e limiti» della risposta (sezione 10).
- Se la lettura è parziale (solo abstract), la scheda riporta «letto: abstract». La certezza può restare quella dichiarata dalla fonte, ma i controlli che richiedono il full text (COI, ITT, protocollo) sono «non verificati».

---

## 9. Budget di chiamate per modalità

| Modalità | Ricerche | Letture | Controlli | Tetto indicativo totale |
|---|---|---|---|---|
| Rapida | 1–2 | 1–2 | ritrattazione + attualità | ~5 chiamate |
| Completa, quesito singolo | 3–6 (discesa L0→L1, più L2 se serve) | 3–8 | tutti quelli eseguibili | ~15–20 chiamate |
| Completa, testo multi-affermazione | per ciascuna delle 5–7 affermazioni prioritarie, come sopra in versione ridotta | | | dichiara il tetto e cosa è rimasto fuori |

Criterio di arresto: fermati quando (a) hai una fonte L0 pertinente e aggiornata che risponde, oppure (b) hai due fonti L1 indipendenti concordi, oppure (c) hai esaurito il budget: in quel caso la sezione «Che cosa non sappiamo» dice cosa non hai potuto cercare. Continuare a cercare finché si trova la risposta desiderata è una forma di bias: dichiara il piano prima e rispettalo.

---

## 10. Il registro delle ricerche

Ogni risposta in protocollo completo chiude con una nota «Metodo e limiti» di 3–6 righe:

```
Metodo e limiti — Ricerche: PubMed «<query 1>» (N risultati), «<query 2>» (N); WebSearch domini L0 «<query>».
Letture: abstract di [1], [2]; full text di [3] (PMC). Controlli: ritrattazioni via metadati PubMed (superato per [1]–[3]);
PubPeer non accessibile; protocollo confrontato per [2] (NCT…), non per [1]. Full text di [1] non accessibile:
conflitti d'interesse non verificati. Ambiente: fetch bloccato verso cochranelibrary.com.
```

Serve a tre cose: rende la verifica riproducibile, rende visibili i buchi, e impedisce di far apparire come «controllato» ciò che non lo è.
