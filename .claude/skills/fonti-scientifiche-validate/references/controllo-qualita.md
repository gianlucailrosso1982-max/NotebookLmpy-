# Controllo qualità prima di citare — procedure

Leggi questo file nella **Fase 4**. Per ogni controllo trovi: perché conta, la procedura con gli strumenti realmente interrogabili, cosa fare se fallisce, e le parole esatte con cui riportare l'esito. Il principio che regge tutto: **un controllo non eseguito si dichiara, non si simula**.

## Indice

1. I tre esiti e perché la simulazione è il rischio principale
2. Ritrattazioni, expression of concern, errata
3. Segnalazioni post-pubblicazione
4. Legittimità della rivista
5. Conflitti di interesse e finanziamento
6. Corrispondenza col protocollo registrato
7. Coerenza interna dei numeri (con un caso reale)
8. Attualità
9. Indipendenza dell'evidenza
10. Valutazione rapida di revisioni (AMSTAR 2) e linee guida (AGREE II)
11. Formato della riga «Controlli»

---

## 1. I tre esiti

| Esito | Quando | Parole da usare |
|---|---|---|
| **superato** | il controllo è stato eseguito con uno strumento e non ha rilevato problemi | «Ritrattazioni: superato (metadati PubMed, 2026-09-10)» |
| **fallito** | il controllo ha rilevato un problema | «Ritrattazioni: **fallito** — articolo ritrattato nel 2010» |
| **non verificato** | lo strumento non era accessibile o il dato non era disponibile | «Post-pubblicazione: non verificato (PubPeer non accessibile dall'ambiente)» |

Perché la simulazione è il rischio principale: il lettore si fida della riga «Controlli» *perché* esiste. Se la riga viene compilata per abitudine («nessuna ritrattazione») senza interrogare nulla, il protocollo produce esattamente la falsa sicurezza che dovrebbe impedire. Un «non verificato» onesto vale più di dieci «superato» presunti.

Se un controllo fallisce: non citare lo studio come evidenza. Se è l'unico disponibile e serve al lettore saperlo, citalo **con il problema nel testo** («uno studio del 2009, poi ritrattato, sosteneva…»).

Salta la Fase 4 solo per i documenti istituzionali di livello L0 (linee guida, rapporti di agenzie): per loro valgono i controlli di attualità (§8) e conflitti (§5).

---

## 2. Ritrattazioni, expression of concern, errata

**Procedura primaria — metadati PubMed** (connettore MCP `get_article_metadata` o pagina del record):
- Guarda `article_types`. Valori che contano:
  - «Retracted Publication» → l'articolo è stato ritrattato: controllo **fallito**.
  - «Retraction of Publication» → il record è la *notizia* di ritrattazione di un altro articolo.
  - «Expression of Concern» → dubbi formali non risolti: trattalo come fallito salvo motivazione esplicita.
  - «Published Erratum» / «Corrected and Republished Article» → correzione: leggi l'erratum prima di citare i numeri.
- Nel record PubMed (pagina web) compaiono anche i collegamenti «Retraction in», «Erratum in», «Comment in», «Update in». **Il connettore MCP non li espone**: se la pagina web e le E-utilities non sono raggiungibili, cerca le notizie con una query mirata (`"<parole del titolo>"[ti] AND (retraction of publication[pt] OR published erratum[pt])`) e, in assenza di risultati, riporta «ritrattazioni: superato (article_types); notizie collegate non verificabili».

**Procedura secondaria — API Crossref** (`https://api.crossref.org/works/<DOI>`): i campi `update-to` (nel record della notizia) e `updated-by` (nel record dell'articolo) elencano ritrattazioni e correzioni con data; Crossref integra i dati di Retraction Watch.

**Terziaria** — Retraction Watch Database (`retractiondatabase.org`), se raggiungibile: è un form interattivo, spesso non interrogabile senza browser.

**Meta-analisi e ritrattazioni**: se citi una revisione, chiediti se include studi poi ritrattati (è accaduto in nutrizione, anestesiologia, oncologia). Se hai il full text, controlla gli studi inclusi più «influenti» (peso maggiore); se no, dichiara «studi inclusi non verificati per ritrattazione».

---

## 3. Segnalazioni post-pubblicazione

- **PubPeer** (`pubpeer.com/search?q=<DOI>`): commenti su immagini duplicate, statistiche impossibili, dati incoerenti. È un'app JavaScript: senza browser di norma non si legge → esito «non verificato» con la causa.
- **PubMed «Comment in»**: lettere all'editore e commenti indicizzati compaiono nel record web, non nei metadati del connettore. Via connettore: `"<parole del titolo>"[ti] AND (comment[pt] OR letter[pt])`, oppure una ricerca sul tema con `letter[pt]` negli anni successivi: è così che si trovano le lettere critiche a una linea guida o a una meta-analisi.
- **scite** (`scite.ai`): mostra quante citazioni successive *contraddicono* il lavoro; freemium.
- Segnali che puoi valutare da solo, se hai il full text: percentuali impossibili con quel campione (es. 33,3% su 10 partecipanti non esiste), medie e deviazioni standard incompatibili con scale limitate, IC asimmetrici attorno alla stima su scala lineare, tabelle con totali che non tornano (§7).

---

## 4. Legittimità della rivista

**Procedura**: (1) il record esiste su PubMed/MEDLINE? L'indicizzazione MEDLINE richiede una selezione di qualità; PMC da sola no (contiene anche riviste non MEDLINE). (2) La rivista è in DOAJ (`doaj.org`) se open access? (3) Ha un quartile SCImago (`scimagojr.com`)?

**Segnali di rivista predatoria** (bastano due o tre): tempi da sottomissione a pubblicazione di pochi giorni; tariffe di pubblicazione poco chiare; comitato editoriale non verificabile; nome che imita una rivista nota; ambito enciclopedico («International Journal of Science and Research»); email di sollecito agli autori; assenza da DOAJ/Scopus/MEDLINE; sito con errori e indirizzo postale generico. Criteri estesi: iniziativa «Think. Check. Submit.».

**Sfumature**: le mega-riviste OA legittime (PLOS ONE, Scientific Reports, Cureus…) pubblicano di tutto con peer review reale ma variabile: non sono predatorie, ma il singolo articolo va giudicato per sé. Le riviste di società scientifiche piccole possono essere legittime e non indicizzate: dichiara «non indicizzata, giudicata legittima per…».

---

## 5. Conflitti di interesse e finanziamento

- **Dove**: sezioni «Funding», «Declaration of interests», «Competing interests», «Acknowledgements» del full text; per i trial, anche il registro (sponsor). Nell'abstract quasi mai → se hai letto solo l'abstract, l'esito è «non verificato (solo abstract)».
- **Cosa classificare**: sponsor industriale del trial; autori dipendenti o consulenti dello sponsor; analisi statistica fatta dallo sponsor; scrittura medica pagata; finanziamento pubblico o di fondazioni indipendenti.
- **Perché conta**: le revisioni metodologiche Cochrane sull'argomento (Lundh e coll.) mostrano che gli studi sponsorizzati dall'industria giungono più spesso a conclusioni favorevoli allo sponsor, a parità di rischio di bias tradizionale. Non è motivo per scartare, è motivo per **declassare per bias di pubblicazione o rischio di bias** quando l'evidenza è *esclusivamente* sponsorizzata, e per dirlo.
- **Anche i non finanziari**: un autore che ha creato la terapia che valuta (allegiance effect in psicoterapia) è un conflitto da riportare.

---

## 6. Corrispondenza col protocollo registrato

Il controllo più efficace contro l'outcome switching. Procedura:

1. Trova l'identificativo: NCT (ClinicalTrials.gov), ISRCTN, EudraCT/CTIS, CRD (PROSPERO per le revisioni), OSF. È nell'abstract o nella prima pagina.
2. Recupera il record: API ClinicalTrials.gov v2 `https://clinicaltrials.gov/api/v2/studies/<NCT>` → `protocolSection.outcomesModule` (outcome primari/secondari con misura e tempo), `designModule.enrollmentInfo`, `statusModule` (date di inizio, registrazione, completamento). PROSPERO: pagina del record.
3. Confronta: l'outcome primario pubblicato è lo stesso, con la stessa misura e lo stesso tempo? Il campione è quello previsto? La registrazione è precedente all'arruolamento (altrimenti «registrazione retrospettiva»)? Gli outcome secondari «significativi» erano previsti?
4. Esito: «superato», oppure «fallito — outcome primario cambiato da X a Y» (declassa per rischio di bias), oppure «non verificato (registro non accessibile / identificativo non trovato)».

Per le revisioni Cochrane il protocollo è pubblicato per definizione: esito «superato per costruzione, dettaglio non confrontato» è accettabile e onesto.

---

## 7. Coerenza interna dei numeri

Prima di trascrivere un numero, controlla che i numeri della fonte siano coerenti tra loro:

- percentuale = eventi / totale (con tolleranza di arrotondamento);
- la stima puntuale sta dentro l'IC, e l'IC di RR/OR è asimmetrico sulla scala lineare (simmetrico su quella logaritmica);
- NNT ≈ 1 / differenza assoluta;
- i totali dei gruppi corrispondono a quelli dichiarati;
- l'abstract non «gonfia» rispetto ai risultati (l'abstract riporta l'outcome secondario positivo e tace il primario negativo).

**Caso reale** — abstract della revisione Cochrane 2022 sui farmaci combinati per il raffreddore (De Sutter e coll., DOI 10.1002/14651858.CD004976.pub4): «128/419 (31%) versus 100/423 (13%) participants suffered one or more adverse effects». 100/423 = 23,6%, non 13%. Come si riporta: «l'abstract contiene un'incoerenza (100/423 corrisponde al 23,6%, non al 13% dichiarato); riportiamo i conteggi e segnaliamo la discrepanza, da chiarire sul full text». Non scegliere uno dei due numeri, non «correggere» in silenzio, non ignorare. Lo script `scripts/effetti.py table` fa il ricalcolo in un secondo.

---

## 8. Attualità

- **Linee guida**: oltre 5 anni senza aggiornamento → cerca la versione successiva o linee guida di altri enti; segnala l'età.
- **Revisioni sistematiche**: guarda la data della ricerca dichiarata nell'abstract («searched to…»), non solo l'anno di pubblicazione. Cerca RCT pubblicati dopo quella data (`randomized controlled trial[pt] AND <anno+1>:2026[dp]`): se ne trovi di grandi, la revisione è potenzialmente superata. Nel record PubMed controlla «Update in»; per Cochrane, la versione (`.pubN`).
- **Farmaci e sicurezza**: verifica sempre le comunicazioni regolatorie recenti (EMA/AIFA/FDA): un ritiro o una nota informativa cambia tutto, indipendentemente dalla letteratura.
- **Campi in rapida evoluzione** (oncologia, malattie infettive, IA in medicina): due anni possono bastare a rendere obsoleta una sintesi.

---

## 9. Indipendenza dell'evidenza

- **Stesso gruppo di autori** che pubblica sintesi successive sullo stesso tema (esempio: le meta-analisi del 2013 e del 2023 sulla vitamina C e il raffreddore sono dello stesso gruppo): non è replicazione indipendente. Riportalo: «le due sintesi condividono gli autori».
- **Stessi trial contati più volte**: meta-analisi diverse che includono gli stessi studi non sono evidenza «convergente», sono la stessa evidenza. Una rete di 6 meta-analisi può poggiare su 4 RCT.
- **Stesso dataset ri-analizzato**: coorti famose producono decine di articoli; un'associazione trovata in tre articoli della stessa coorte è un risultato, non tre.
- **Evidenza contraria**: cercala attivamente (`<argomento> AND (no effect OR null OR negative OR "did not")`, scite per le citazioni contrastanti). L'assenza di evidenza contraria nel tuo elenco può dipendere da come hai cercato.

---

## 10. Valutazione rapida

**Revisione sistematica — AMSTAR 2, i 7 item critici**: (1) protocollo registrato prima dell'inizio; (2) ricerca completa (≥ 2 database, registri, letteratura grigia); (3) motivazione degli studi esclusi; (4) rischio di bias valutato per ogni studio; (5) metodi meta-analitici appropriati; (6) rischio di bias considerato nell'interpretazione; (7) bias di pubblicazione valutato. Due o più mancanze critiche → revisione di qualità «criticamente bassa»: la sua conclusione non vale più dei suoi studi.

**Linea guida — AGREE II, domande chiave** (decidono anche il livello: L0 se le risposte sono sì, altrimenti «consenso di esperti»): metodo di ricerca dell'evidenza dichiarato? Criteri di selezione e forza dell'evidenza espliciti? Collegamento visibile tra evidenza e raccomandazione? Revisione esterna? Procedura di aggiornamento? Conflitti d'interesse del panel dichiarati e gestiti? Indipendenza editoriale dal finanziatore?

**RCT dall'abstract — domande minime**: randomizzato? in cieco (chi)? placebo o confronto attivo? outcome primario dichiarato? ITT? dimensione campionaria e numero di eventi? durata del follow-up? registrazione?

---

## 11. Formato della riga «Controlli»

```
| Controlli | Ritrattazioni: superato (PubMed, article_types) · Post-pubblicazione: non verificato (PubPeer non accessibile) · Rivista: superato (MEDLINE) · Conflitti: non verificato (solo abstract) · Protocollo: superato per costruzione (Cochrane) · Attualità: ricerca al nov. 2012, 13 anni; sintesi più recente 2023 stesso gruppo · Coerenza numeri: superato |
```

Ogni voce porta strumento e, quando serve, la causa del «non verificato». La riga può essere lunga: è la parte della scheda che vale di più.
