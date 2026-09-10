---
name: fonti-scientifiche-validate
description: Instrada ogni ricerca su affermazioni fattuali verso le fonti scientifiche ad accesso libero più autorevoli, in ordine gerarchico, e assegna a ciascun dato una certezza GRADE con la sua efficacia reale (effetto assoluto, NNT, intervalli di confidenza). Usa questa skill quando l'utente chiede di verificare o documentare un'affermazione scientifica, clinica, psicologica, statistica, nutrizionale o di salute pubblica — "cosa dice la scienza", "quali sono le prove", "è vero che", "fonti autorevoli", "quanto è efficace", "verifica questa affermazione" — o quando scrive contenuti divulgativi, clinici, formativi o giornalistici che devono poggiare su fonti verificabili. Attivala anche in autonomia quando una risposta rischierebbe di presentare come certo un dato con basi deboli. Non attivarla per opinioni, preferenze, quesiti di programmazione o fatti banali non contestati.
---

# Fonti Scientifiche Validate — Protocollo di ricerca gerarchica e valutazione dell'efficacia reale

## 1. Principio guida

Due domande, sempre separate e mai confuse:

1. **Quanto è autorevole la FONTE?** → Livello gerarchico (L0–L5).
2. **Quanto è solido il DATO?** → Certezza GRADE (Alta / Moderata / Bassa / Molto bassa).

Una fonte di livello massimo può ospitare un dato di certezza molto bassa. Una revisione Cochrane può concludere "evidenza molto incerta". Non promuovere mai un dato solo perché sta su PubMed o su una rivista prestigiosa.

Terza domanda, quella che l'utente vuole davvero: **quanto conta questo effetto nella realtà?** Un risultato statisticamente significativo può essere clinicamente irrilevante. Riporta sempre la dimensione dell'effetto in termini assoluti, non solo relativi.

---

## 2. Protocollo operativo

**Fase 0 — Triage di proporzionalità.**
Prima di tutto, scegli la modalità e dichiarala nella risposta:

- **Modalità rapida** — quesito singolo, non controverso, non destinato a pubblicazione (una curiosità, un fatto da confermare): una sola ricerca sul livello più alto pertinente, una fonte L0/L1 verificata, mini-scheda a 4 righe (affermazione, certezza, effetto assoluto, fonte con link). Tutte le regole ferme della sezione 7 restano valide.
- **Protocollo completo** — quesito clinico o controverso, più affermazioni da verificare, o contenuto destinato a pubblicazione/divulgazione: tutte le fasi che seguono.

Nel dubbio, chiedi o usa la modalità rapida dichiarando il limite.

**Fase 1 — Formulare il quesito in forma strutturata.**
Per quesiti clinici e comportamentali usa PICO: Popolazione, Intervento, Confronto, Outcome. Per quesiti non clinici, esplicita: fenomeno, contesto, misura, periodo. Se il quesito è vago, restringilo prima di cercare. **Traduci sempre il quesito in inglese** prima di interrogare le fonti: quasi tutte le banche dati della sezione 3 indicizzano in inglese, e una query in italiano ne dimezza il recupero.

**Fase 2 — Discesa gerarchica.**
Parti sempre dal livello più alto e scendi solo se non trovi risposta; per affermazioni controverse, cerca comunque conferma incrociata su almeno due fonti indipendenti. Usa il parametro `allowed_domains` di WebSearch per vincolare la ricerca ai domini del livello che stai interrogando (elenco alla sezione 3). Non partire mai da una ricerca generica sul web aperto. Due avvertenze tecniche:

- Il filtro `allowed_domains` opera sul dominio registrabile, non sul sottodominio esatto: vincolare a `pubmed.ncbi.nlm.nih.gov` può restituire anche altre proprietà `ncbi.nlm.nih.gov`. Controlla che ogni risultato appartenga davvero al livello che stai interrogando.
- **Gli snippet dei risultati di ricerca servono a selezionare le fonti, mai a citarne i dati.** I riassunti restituiti dal motore contengono numeri ed effetti pre-digeriti: non sono lettura della fonte. Un numero è citabile solo dopo aver aperto il documento (Fase 3).

**Fase 3 — Recupero del testo, con fallback a cascata.**
Segui quest'ordine e fermati al primo canale che funziona:

1. **Connettori/MCP attivi** (es. PubMed, Consensus, ClinicalTrials.gov, ChEMBL, bioRxiv, Open Targets — verifica quali esistono davvero nella sessione: spesso solo alcuni sono presenti).
2. **`WebFetch` sugli URL trovati.** In ambienti con proxy di rete restrittivo molti domini scientifici risultano bloccati: un fetch fallito non è un errore tuo, è un limite dell'ambiente.
3. **Se entrambi i canali falliscono**, il documento è *non letto*: puoi indicarlo come riferimento da approfondire, ma nessun suo dato è citabile e la scheda deve riportare «non verificato (accesso bloccato)». Non ripiegare mai sugli snippet della Fase 2 come surrogato di lettura.

Leggi almeno l'abstract completo e, quando accessibile, la sezione metodi e i risultati numerici. Non citare mai un lavoro di cui hai letto solo il titolo o lo snippet.

**Fase 4 — Controllo qualità obbligatorio.**
Prima di citare qualunque studio, verifica: ritrattazioni, segnalazioni post-pubblicazione, natura della rivista, conflitti di interesse, finanziamento. Strumenti alla sezione 5. Salta questa fase solo per documenti istituzionali di livello L0.

**Fase 5 — Valutazione GRADE.**
Ordine di preferenza: **(a)** se la fonte L0 riporta già un proprio giudizio GRADE (le tabelle Summary of Findings di Cochrane, il grado delle raccomandazioni nelle linee guida, il grado A–D di USPSTF), usa quello e citalo come tale; **(b)** solo in assenza di una sintesi già valutata, assegna tu un livello secondo lo schema della sezione 4, motivando ogni declassamento o rialzo ed etichettandolo esplicitamente come «valutazione indicativa, non un GRADE formale». Non giudicare domini che richiedono dati non letti: se non hai visto I², funnel plot o protocollo registrato, scrivi «non valutabile dai dati accessibili» invece di stimare.

**Fase 6 — Restituzione strutturata.**
Usa il formato della sezione 6. Dichiara esplicitamente ciò che non hai trovato o che resta incerto: l'assenza di evidenza è essa stessa un'informazione da riportare.

---

## 3. Gerarchia delle fonti ad accesso libero

Ordinate per autorevolezza decrescente. Tutte consultabili gratuitamente; dove l'accesso ha condizioni, sono indicate.

### L0 — Sintesi critiche, revisioni sistematiche e linee guida istituzionali
Il vertice. Sono corpi di evidenza già valutati criticamente da panel indipendenti con metodologia dichiarata.

| Fonte | Dominio | Ambito | Accesso |
|---|---|---|---|
| Cochrane Library | `cochranelibrary.com` | Revisioni sistematiche in sanità | Abstract e Plain Language Summary sempre liberi; protocolli ed editoriali OA dal 2025; revisioni complete libere dopo 12 mesi; accesso nazionale gratuito in diversi paesi (Italia inclusa via provvedimenti nazionali/istituzionali) |
| Epistemonikos | `epistemonikos.org` | Revisioni sistematiche multilingue, matrici di evidenza | Libero |
| WHO — Linee guida e IRIS | `who.int`, `iris.who.int` | Salute globale, linee guida OMS | Libero |
| NICE | `nice.org.uk` | Linee guida cliniche e HTA (UK) | Libero |
| USPSTF | `uspreventiveservicestaskforce.org` | Raccomandazioni di prevenzione con grado A–D | Libero |
| ECRI Guidelines Trust | `guidelines.ecri.org` | Repository di linee guida valutate (TRUST Scorecard) | Registrazione gratuita |
| Guidelines International Network | `g-i-n.net` | Registro internazionale di linee guida | Libero |
| Campbell Collaboration | `campbellcollaboration.org` | Revisioni sistematiche in scienze sociali, educazione, criminologia, welfare | Open access integrale |
| JBI Evidence Synthesis | `jbi.global` | Revisioni sistematiche, evidenza qualitativa e assistenziale | Abstract liberi |
| INAHTA HTA Database | `database.inahta.org` | Health Technology Assessment internazionale | Libero |
| ISS / Sistema Nazionale Linee Guida | `iss.it`, `snlg.iss.it` | Linee guida italiane | Libero |
| CDC | `cdc.gov` | Salute pubblica, epidemiologia, ACIP GRADE | Libero |
| ECDC | `ecdc.europa.eu` | Epidemiologia europea | Libero |
| EMA / AIFA / FDA | `ema.europa.eu`, `aifa.gov.it`, `fda.gov` | Valutazioni regolatorie sui farmaci, EPAR, foglietti illustrativi | Libero |
| EFSA | `efsa.europa.eu` | Sicurezza alimentare, nutrizione, opinioni scientifiche | Libero |
| IARC Monographs | `monographs.iarc.who.int` | Classificazione cancerogeni | Libero |
| IPCC | `ipcc.ch` | Clima, rapporti di valutazione | Libero |
| National Academies (NASEM) | `nap.nationalacademies.org` | Rapporti di consenso multidisciplinari | Libero |

### L1 — Letteratura primaria peer-reviewed indicizzata

| Fonte | Dominio | Ambito | Note |
|---|---|---|---|
| PubMed / MEDLINE | `pubmed.ncbi.nlm.nih.gov` | Biomedicina, ~38M record | Indice + abstract liberi; usa i filtri "Systematic Review", "Meta-Analysis", "Randomized Controlled Trial" |
| PubMed Central (PMC) | `pmc.ncbi.nlm.nih.gov` | Full text libero biomedico | |
| Europe PMC | `europepmc.org` | 40M+ pubblicazioni e preprint, life sciences | Full text, API libera, collega dati e protocolli |
| DOAJ | `doaj.org` | 20.000+ riviste OA verificate | Usalo anche come filtro anti-predatorio |
| SciELO | `scielo.org` | America Latina, Iberia, Sudafrica | |
| ERIC | `eric.ed.gov` | Educazione e didattica | |
| NASA ADS | `ui.adsabs.harvard.edu` | Astronomia, astrofisica, fisica | |
| AGRIS (FAO) | `agris.fao.org` | Agricoltura, alimentazione | |
| PsycNet / APA (sezioni aperte) | `psycnet.apa.org` | Psicologia | Record e abstract; full text spesso a pagamento |

### L2 — Registri di studi e protocolli
Servono per verificare se un risultato pubblicato corrisponde a quanto pre-registrato: è il controllo più efficace contro l'outcome switching e il publication bias.

| Fonte | Dominio | Ambito |
|---|---|---|
| ClinicalTrials.gov | `clinicaltrials.gov` | Registro NIH degli studi clinici |
| WHO ICTRP | `trialsearch.who.int` | Meta-registro globale degli studi |
| EU CTIS / EudraCT | `euclinicaltrials.eu`, `clinicaltrialsregister.eu` | Registro europeo |
| PROSPERO | `crd.york.ac.uk/prospero` | Registro delle revisioni sistematiche |
| OSF Registries | `osf.io` | Pre-registrazioni multidisciplinari |

### L3 — Aggregatori e motori bibliografici aperti
Ottimi per scoprire e mappare la letteratura, **mai** come fonte terminale: portano sempre al documento primario.

| Fonte | Dominio | Punto di forza |
|---|---|---|
| OpenAlex | `openalex.org` | Catalogo aperto di ~250M+ opere, API senza restrizioni, dati di citazione |
| Semantic Scholar | `semanticscholar.org` | 200M+ paper, citazioni influenti, API gratuita |
| CORE | `core.ac.uk` | Aggregatore di repository OA, full text |
| BASE | `base-search.net` | Metadati OAI-PMH da repository accademici |
| Lens.org | `lens.org` | Integra letteratura e brevetti |
| Unpaywall / OA.Works | `unpaywall.org` | Trova la versione legalmente aperta di un DOI |
| Google Scholar | `scholar.google.com` | Copertura ampia ma opaca e non riproducibile: usalo solo in supporto, mai come base di una ricerca sistematica |

### L4 — Banche dati fattuali, statistiche ufficiali e dati strutturali
Autorevoli e generalmente accurate, ma **descrittive**: forniscono numeri, non nessi causali. Non usarle per sostenere affermazioni di efficacia.

**Statistiche e indicatori**
`who.int/data/gho` (WHO Global Health Observatory) · `ec.europa.eu/eurostat` · `data-explorer.oecd.org` · `data.worldbank.org` · `data.un.org` · `dati.istat.it` · `data.europa.eu` · `ourworldindata.org` (secondario ma con fonti primarie tracciabili) · `ihmeuw.org` / `healthdata.org` (Global Burden of Disease)

**Dati biologici e chimici**
`ncbi.nlm.nih.gov` (GenBank, Gene, dbSNP, ClinVar) · `uniprot.org` · `rcsb.org` (Protein Data Bank) · `ensembl.org` · `ebi.ac.uk/chembl` · `pubchem.ncbi.nlm.nih.gov` · `platform.opentargets.org` · `gbif.org` (biodiversità)

**Ambiente, spazio, geoscienze**
`copernicus.eu` · `noaa.gov` · `usgs.gov` · `esa.int` · `nasa.gov`

**Diritto e normativa**
`eur-lex.europa.eu` · `normattiva.it` · `gazzettaufficiale.it`

### L5 — Preprint e letteratura grigia
**Non peer-reviewed.** Utili per la frontiera della ricerca, per verificare se un risultato è recente o contestato, mai come prova di efficacia. Ogni citazione da questo livello va etichettata esplicitamente come "preprint, non sottoposto a revisione paritaria" e la certezza GRADE parte da **Bassa** o **Molto bassa**.

`arxiv.org` (fisica, matematica, informatica) · `biorxiv.org` (biologia) · `medrxiv.org` (medicina) · `chemrxiv.org` (chimica) · `psyarxiv.com` (psicologia) · `osf.io/preprints` · `socarxiv.org` · `eartharxiv.org` · `ssrn.com` · `researchsquare.com`

### Fuori gerarchia — da non usare come fonte
Blog divulgativi, siti commerciali, testate generaliste, social, contenuti generati da IA, aggregatori di notizie sanitarie, siti che vendono il prodotto di cui parlano. Possono servire solo per *individuare* uno studio, che va poi recuperato e verificato alla fonte primaria.

---

## 4. Valutazione della certezza: GRADE + piramide delle evidenze

### 4.1 Punto di partenza secondo il disegno dello studio

| Disegno | Posizione in piramide | Certezza iniziale |
|---|---|---|
| Revisione sistematica / meta-analisi di RCT | Vertice | **Alta** |
| RCT singolo, ben condotto | Alto | **Alta** |
| Studio di coorte prospettico | Medio | **Bassa** |
| Studio caso-controllo | Medio-basso | **Bassa** |
| Studio trasversale, serie di casi, registro | Basso | **Molto bassa** |
| Caso clinico singolo | Molto basso | **Molto bassa** |
| Studio in vitro / animale / modellistico | Pre-clinico | **Molto bassa** per conclusioni sull'uomo |
| Opinione di esperto, consenso non sistematico | Base | **Molto bassa** |
| Preprint (qualunque disegno) | — | Parte da **Bassa** (disegno sperimentale) o **Molto bassa** (osservazionale), coerentemente con la regola L5 |

### 4.2 Cinque motivi di declassamento (GRADE)

Abbassa di uno o due gradini per ciascuno:

1. **Rischio di bias** — randomizzazione o cecità assenti o poco chiare, alto tasso di abbandoni, outcome cambiati rispetto al protocollo registrato, analisi non per intention-to-treat.
2. **Incoerenza** — i risultati dei singoli studi divergono, eterogeneità elevata (I² alto), intervalli di confidenza che non si sovrappongono.
3. **Indirettezza** — popolazione, intervento, confronto o outcome diversi da quelli della domanda; uso di outcome surrogati al posto di esiti che contano davvero.
4. **Imprecisione** — campione piccolo, pochi eventi, intervallo di confidenza ampio che include sia beneficio sia danno.
5. **Bias di pubblicazione** — solo studi piccoli e positivi, asimmetria del funnel plot, finanziamento esclusivo da parte di chi ha interesse al risultato, studi registrati mai pubblicati.

### 4.3 Tre motivi di rialzo (solo per studi osservazionali)

1. Effetto di grandezza notevole (RR > 2 o < 0,5 in modo consistente).
2. Gradiente dose-risposta coerente.
3. Tutti i fattori confondenti plausibili spingerebbero verso la nullità, eppure l'effetto persiste.

### 4.4 Significato dei quattro livelli

| Simbolo | Livello | Significato operativo |
|---|---|---|
| ⬤⬤⬤⬤ | **Alta** | L'effetto reale è molto probabilmente vicino alla stima. Ricerche future difficilmente la cambieranno. Puoi affermarlo. |
| ⬤⬤⬤◯ | **Moderata** | L'effetto reale è probabilmente vicino alla stima, ma potrebbe differire in modo sostanziale. Puoi affermarlo con riserva esplicita. |
| ⬤⬤◯◯ | **Bassa** | La fiducia nella stima è limitata: l'effetto reale può essere sostanzialmente diverso. Presenta come ipotesi, non come fatto. |
| ⬤◯◯◯ | **Molto bassa** | Fiducia minima: la stima è molto incerta. Non usarla per orientare decisioni. Dichiara che non lo sappiamo. |

### 4.5 Efficacia reale — cosa riportare sempre

La certezza dice quanto ci fidiamo del numero. L'efficacia reale dice quanto quel numero conta. Riporta, quando disponibili:

- **Effetto assoluto**, non solo relativo. "Riduce il rischio del 50%" è vuoto: da 2% a 1% è un beneficio piccolo, da 40% a 20% è enorme. Riporta sempre ARR (riduzione assoluta del rischio) accanto al RR/OR/HR. Se la fonte letta riporta solo l'effetto relativo e il rischio di base non è disponibile, scrivi «effetto assoluto non riportato nella fonte» — **non calcolarlo mai da assunzioni non dichiarate**.
- **NNT / NNH** — quante persone bisogna trattare perché una ne tragga beneficio, e quante perché una subisca un danno.
- **Intervallo di confidenza al 95%**, non solo la stima puntuale.
- **Differenza minima clinicamente importante (MCID)** — l'effetto supera la soglia oltre la quale la persona se ne accorge davvero?
- **Outcome misurato**: reale (mortalità, ricadute, qualità di vita) o surrogato (un marcatore di laboratorio)? Gli outcome surrogati vanno segnalati come tali.
- **Durata del follow-up** e **popolazione studiata**, con esplicita indicazione dei limiti di trasferibilità.
- **Danni e effetti avversi**, non solo benefici. Un'analisi che riporta solo i benefici è incompleta per definizione.

---

## 5. Controllo qualità obbligatorio prima di citare

Ogni controllo ha uno strumento primario meccanicamente interrogabile e, dove esiste, uno di riserva. Priorità agli strumenti primari: quelli di riserva sono best effort (form o app JavaScript spesso non leggibili senza browser, o bloccati dai proxy di rete).

| Controllo | Strumento primario | Riserva (best effort) | Che cosa cerchi |
|---|---|---|---|
| Ritrattazione | **Metadati PubMed**: il campo `article_types` riporta «Retracted Publication»; le notice di ritrattazione ed errata sono collegate al record | API Crossref (`api.crossref.org/works/<DOI>`, campi `update-to`/`updated-by`, includono i dati Retraction Watch); `retractiondatabase.org` solo se raggiungibile | Articolo ritrattato, corretto o con expression of concern |
| Revisione post-pubblicazione | — | `pubpeer.com` (app JavaScript: spesso non interrogabile senza browser) | Segnalazioni su immagini duplicate, dati incoerenti, errori statistici |
| Legittimità della rivista | Indicizzazione MEDLINE/PubMed della rivista | `doaj.org`, `scimagojr.com` | Rivista indicizzata e con peer review reale; diffida di titoli assenti da DOAJ/Scopus e con tempi di pubblicazione lampo |
| Conflitti di interesse | Sezione "Funding" e "Competing interests" del full text (accessibile via PMC per gli articoli open access) | — | Chi ha finanziato e chi ha analizzato i dati |
| Corrispondenza col protocollo | `clinicaltrials.gov`, `crd.york.ac.uk/prospero` (via MCP o fetch, se raggiungibili) | — | Gli outcome pubblicati coincidono con quelli pre-registrati? |
| Attualità | Data di pubblicazione e di ultimo aggiornamento (nei metadati) | — | Una linea guida di 12 anni fa può essere superata |

Tre esiti possibili per ciascun controllo, e vanno riportati con queste parole:

- **superato** — il controllo è stato eseguito e non ha rilevato problemi;
- **fallito** — il controllo ha rilevato un problema: non citare quello studio; se lo citi comunque perché è l'unico disponibile, dichiara il problema nel testo;
- **non verificato (strumento non accessibile)** — il canale era bloccato o assente: esito legittimo e obbligatorio da dichiarare.

**Mai compilare l'esito di un controllo non eseguito.** Scrivere «nessuna ritrattazione» senza aver interrogato lo strumento è la violazione più grave di questo protocollo: simula il rigore che dovrebbe garantire.

---

## 6. Formato di restituzione

Per ogni affermazione rilevante, produci una scheda in questa forma. Usa prosa scorrevole per la sintesi e la tabella per il dettaglio; non trasformare tutto in elenchi puntati. Se il testo da verificare contiene molte affermazioni, produci la scheda completa solo per le più importanti o le più fragili (di norma non oltre 5–7, in ordine di rilevanza) e raccogli le restanti in una tabella riassuntiva a una riga ciascuna (affermazione · certezza · fonte).

```
### [Affermazione in una riga]

**Certezza dell'evidenza: ⬤⬤⬤◯ MODERATA**

Che cosa dicono i dati — [2-4 frasi in linguaggio chiaro, con i numeri assoluti]

| Voce | Contenuto |
|---|---|
| Fonte | [Nome] — Livello [L0–L5] |
| Disegno | [Meta-analisi di N RCT, n = totale partecipanti] |
| Effetto | [RR/OR/HR con IC 95%] · [ARR] · [NNT] |
| Outcome | [Reale o surrogato] · Follow-up [durata] |
| Popolazione | [Chi è stato studiato] |
| Motivo del livello | [Perché Alta/Moderata/Bassa: quale dominio GRADE è stato declassato e perché] |
| Danni noti | [Effetti avversi riportati, o "non riportati nello studio"] |
| Controlli | Ritrattazioni: [superato / fallito / non verificato] · Post-pubblicazione: [esito] · Conflitti: [esito] |
| Link | [URL diretto] |
```

Chiudi ogni ricerca con tre elementi:

1. **Sintesi gerarchica** — la risposta complessiva, con il livello di certezza globale. Se due fonti L0 divergono (due linee guida in disaccordo), riportale entrambe con data e metodologia: non sceglierne una in silenzio.
2. **Che cosa non sappiamo** — lacune, questioni aperte, aree in cui l'evidenza manca o si contraddice. Questa sezione non è mai facoltativa.
3. **Fonti** — elenco numerato con link cliccabili e livello gerarchico accanto a ciascuna.

**Precedenza dei formati di citazione.** Alcuni MCP impongono propri obblighi di attribuzione (Consensus: riferimenti numerati inline e messaggio finale da riportare verbatim; PubMed: attribuzione esplicita con DOI linkato). Questi obblighi **si integrano** nella scheda — il DOI va nella riga Link, i riferimenti numerati nell'elenco Fonti, i messaggi obbligatori in coda alla risposta — e non sostituiscono né smontano il formato di questa sezione.

---

## 7. Regole ferme

- **Mai citare ciò che non hai letto.** Nessun DOI, autore, anno o cifra inventati o ricostruiti a memoria. Gli snippet dei risultati di ricerca non sono lettura: un numero preso da uno snippet non è citabile. Se non hai potuto verificare, scrivilo.
- **Mai compilare l'esito di un controllo non eseguito.** «Non verificato (strumento non accessibile)» è sempre un esito ammesso; un esito inventato non lo è mai.
- **Mai spacciare un preprint per evidenza consolidata.**
- **Mai un rischio relativo senza il corrispettivo assoluto** quando la fonte lo riporta o lo rende ricavabile; se non lo è, dichiara «effetto assoluto non riportato nella fonte» invece di stimarlo.
- **Mai una conclusione più forte di quanto la certezza consenta.** Con certezza bassa si scrive "alcuni studi suggeriscono", non "è dimostrato che".
- **Mai omettere l'evidenza contraria.** Se esistono studi discordanti, vanno riportati con il loro peso.
- **Mai confondere correlazione e causalità**, nemmeno per semplificare.
- **Nessun consiglio clinico personalizzato.** Riporta l'evidenza e ricorda che le decisioni cliniche competono a un professionista che conosce il caso.
- Se la ricerca non produce risultati di livello adeguato, dillo chiaramente invece di ripiegare su fonti deboli presentate come solide.

---

## 8. Riferimenti metodologici

GRADE Working Group — sistema di valutazione della certezza dell'evidenza e della forza delle raccomandazioni (`gradeworkinggroup.org`, `gdt.gradepro.org/app/handbook/handbook.html`).
Cochrane Handbook for Systematic Reviews of Interventions (`training.cochrane.org/handbook`).
PRISMA 2020 per la rendicontazione delle revisioni sistematiche (`prisma-statement.org`).
Risk of Bias 2 (RoB 2) e ROBINS-I per la valutazione del rischio di bias.
AGREE II per la valutazione della qualità delle linee guida.
