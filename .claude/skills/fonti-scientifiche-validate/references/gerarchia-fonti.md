# Gerarchia delle fonti ad accesso libero — riferimento esteso

Leggi questo file nella **Fase 2** (discesa gerarchica) quando devi scegliere da dove partire, o quando una fonte del livello atteso non risponde e ti serve un'alternativa dello stesso livello.

## Indice

1. Da dove parto — tabella per tipo di quesito
2. L0 — Sintesi critiche, revisioni sistematiche e linee guida istituzionali
3. L1 — Letteratura primaria peer-reviewed indicizzata
4. L2 — Registri di studi e protocolli
5. L3 — Aggregatori, motori bibliografici e API aperte
6. L4 — Banche dati fattuali, statistiche ufficiali, dati strutturali
7. L5 — Preprint e letteratura grigia
8. Fuori gerarchia: uso strumentale, mai come fonte
9. Percorsi tematici: psicologia clinica, nutrizione, fonti italiane, scienze sociali, scienze dure
10. Come giudicare una fonte non in elenco

Regola trasversale: **il livello descrive la fonte, non il dato**. Un dato di certezza Molto bassa può stare in una fonte L0 (una linea guida che dichiara «evidenza molto incerta»); un dato di certezza Alta può stare in L1 (un grande RCT pubblicato ieri, non ancora incluso in alcuna revisione).

---

## 1. Da dove parto — tabella per tipo di quesito

| Tipo di quesito | Livello di partenza | Prime fonti da interrogare | Filtri utili |
|---|---|---|---|
| Efficacia di un trattamento/intervento sanitario | L0 | Cochrane (via PubMed), Epistemonikos, NICE, WHO | `"Cochrane Database Syst Rev"[Journal]`, `systematic review[pt]` |
| Sicurezza, effetti avversi di farmaci | L0 | EMA (EPAR), FDA (label, FAERS), AIFA, Cochrane | cerca «adverse», «harms», «safety» |
| Prevenzione, screening | L0 | USPSTF, NICE, Cochrane, ECDC/CDC | grado USPSTF A–D/I |
| Psicoterapia, interventi psicologici | L0 → L1 | Cochrane, NICE (mental health), Campbell, PubMed/PsycNet | vedi §9 |
| Nutrizione, integratori | L0 | EFSA (opinioni scientifiche, claims), Cochrane, WHO | attenzione ai conflitti d'interesse dell'industria |
| Epidemiologia, prevalenze, incidenze | L4 → L0 | GBD/IHME, WHO GHO, ECDC, ISTAT, Eurostat | i numeri descrittivi non provano cause |
| Cancerogenicità, tossicologia | L0 | IARC Monographs, EFSA, ECHA, NTP | distingui «pericolo» (IARC) da «rischio» (dose) |
| Educazione, welfare, criminologia, politiche sociali | L0 | Campbell Collaboration, EEF (UK), ERIC, 3ie | molti RCT sono cluster o quasi-sperimentali |
| Clima, ambiente | L0 | IPCC (AR6), Copernicus, NOAA, NASA | riporta i livelli di confidenza IPCC («very likely» ecc.) |
| Fisica, chimica, dati costanti | L4 → L1 | NIST, IUPAC, CODATA, arXiv (per la frontiera) | i dati di riferimento sono L4 ma di massima affidabilità |
| Norme e diritto | L4 | Normattiva, EUR-Lex, Gazzetta Ufficiale | non «efficacia», ma «cosa dice la norma» |
| Fatti storici, biografici | fuori protocollo | fonti primarie d'archivio, enciclopedie accademiche | questa skill non è pensata per la storiografia |

---

## 2. L0 — Sintesi critiche, revisioni sistematiche e linee guida istituzionali

Corpi di evidenza già valutati criticamente da panel con metodologia dichiarata. Quando esistono, sono il punto di partenza e, spesso, di arrivo.

### Cochrane Library — `cochranelibrary.com`
- **Cosa ci trovi**: revisioni sistematiche di interventi sanitari, con tabelle Summary of Findings (SoF) GRADE, Plain Language Summary, protocolli, aggiornamenti.
- **Accesso reale**: abstract e Plain Language Summary sempre liberi. Cochrane ha annunciato la transizione all'open access per le nuove revisioni a partire dal 2025; le revisioni precedenti diventano libere dopo un periodo di embargo di 12 mesi, salvo licenze nazionali (verifica quella del paese: alcune nazioni hanno accesso integrale). Non dare per scontato l'accesso italiano: controlla il singolo record.
- **Via alternativa decisiva**: **ogni revisione Cochrane è indicizzata in PubMed con l'abstract completo**, che contiene i risultati numerici principali (RR/OR con IC, numero di studi e partecipanti) e spesso la certezza GRADE per outcome («moderate certainty evidence»). Quando `cochranelibrary.com` è bloccato o a pagamento, cerca su PubMed: `<argomento> AND "Cochrane Database Syst Rev"[Journal]`. Le SoF complete non sono in PubMed. **Il record PMC di una revisione Cochrane contiene di norma solo abstract e Plain Language Summary**: `get_full_text_article` restituisce un `full_text` vuoto. La PLS riporta spesso gli effetti assoluti (per 1000) e la certezza per outcome: usala. Metodi, tabelle SoF, Funding e Competing interests sono solo sul sito Cochrane.
- **Trappole**: revisioni ritirate compaiono con prefisso «WITHDRAWN:» nel titolo; controlla sempre la versione (`.pub2`, `.pub3`…) e il campo «Update in» del record PubMed per trovare l'aggiornamento più recente; una revisione di 10+ anni fa va segnalata come potenzialmente superata.

### Linee guida di società scientifiche (CANMAT, APA, ESC, ESMO, AIOM, SIP, …) — L0 condizionato
- Sono L0 **solo se** dichiarano metodo di ricerca dell'evidenza, sistema di grading (GRADE o equivalente), gestione dei conflitti d'interesse e revisione esterna (le domande AGREE II in `controllo-qualita.md` §10). Altrimenti sono «consenso di esperti»: come fonte valgono L1 se pubblicate su rivista peer-reviewed, e il dato che ne deriva ha certezza Molto bassa; vanno etichettate «consenso». Segnala le linee guida sponsorizzate dall'industria o prodotte da società con interessi nel tema (nutraceutica, dispositivi). Se due società divergono, riporta entrambe con anno e metodo.

### Epistemonikos — `epistemonikos.org`
- Database multilingue di revisioni sistematiche in sanità, con «matrici di evidenza» che collegano revisioni e studi primari. La ricerca è un'app JavaScript: spesso non leggibile via fetch. Fallback: PubMed con filtro `systematic review[pt]`.

### Organizzazione Mondiale della Sanità — `who.int`, `iris.who.int`
- Linee guida basate su GRADE (obbligatorio per le linee guida OMS dal 2007), rapporti tecnici, position paper sui vaccini. IRIS è il repository istituzionale con PDF liberi. Cerca «WHO guideline» + argomento.

### NICE — `nice.org.uk`
- Linee guida cliniche e di salute pubblica del Regno Unito, con «evidence reviews» dettagliate per ogni raccomandazione e valutazioni HTA. Contesto sanitario britannico: verifica la trasferibilità. Le pagine sono HTML statico, di norma leggibili via fetch.

### USPSTF — `uspreventiveservicestaskforce.org`
- Raccomandazioni di prevenzione e screening con grado A (raccomandato, beneficio sostanziale), B (moderato), C (individuale), D (sconsigliato), I (evidenza insufficiente). Ogni raccomandazione ha una revisione sistematica allegata.

### AHRQ Effective Health Care — `effectivehealthcare.ahrq.gov`
- Revisioni sistematiche e «comparative effectiveness reviews» statunitensi, con valutazione della forza dell'evidenza. Full text libero.

### SIGN — `sign.ac.uk`
- Linee guida scozzesi, con metodologia trasparente e livelli di evidenza. Libere.

### Health Evidence — `healthevidence.org`
- Revisioni sistematiche di salute pubblica valutate per qualità metodologica (punteggio 1–10). Registrazione gratuita per alcune funzioni; i punteggi sono visibili.

### ECRI Guidelines Trust — `guidelines.ecri.org`
- Repository di linee guida con TRUST Scorecard. **Richiede registrazione**: un agente non può registrarsi. Usalo solo se l'utente fornisce i contenuti.

### Guidelines International Network — `g-i-n.net`
- Registro internazionale di linee guida. Utile per scoprire quale società ha prodotto una linea guida, che poi va cercata sul sito dell'ente.

### Campbell Collaboration — `campbellcollaboration.org`
- Revisioni sistematiche in scienze sociali: educazione, welfare, criminologia, giustizia, sviluppo internazionale, disabilità, metodi. Open access integrale sulla rivista *Campbell Systematic Reviews* (Wiley). È la «Cochrane» delle scienze sociali: se il quesito è educativo o comportamentale, parti da qui.

### Education Endowment Foundation — `educationendowmentfoundation.org.uk`
- Teaching and Learning Toolkit: sintesi di meta-analisi in educazione con «mesi di progresso» e forza dell'evidenza. Secondario ma con fonti tracciabili.

### 3ie — `3ieimpact.org`
- Revisioni sistematiche e mappe di evidenza sullo sviluppo internazionale. Libero.

### JBI Evidence Synthesis — `jbi.global`
- Revisioni sistematiche in ambito assistenziale, qualitativo, di prevalenza e scoping review. Abstract liberi; full text spesso a pagamento.

### INAHTA HTA Database — `database.inahta.org`
- Valutazioni di tecnologia sanitaria di agenzie di tutto il mondo. Libero.

### Istituto Superiore di Sanità / SNLG — `iss.it`, `snlg.iss.it`, `epicentro.iss.it`
- Linee guida italiane del Sistema Nazionale Linee Guida (metodologia GRADE), schede epidemiologiche EpiCentro. Libero. Prima scelta per il contesto italiano.

### Agenzie di salute pubblica — CDC `cdc.gov`, ECDC `ecdc.europa.eu`
- Epidemiologia, sorveglianza, raccomandazioni vaccinali (ACIP usa GRADE). Libero.

### Agenzie regolatorie — EMA `ema.europa.eu`, AIFA `aifa.gov.it`, FDA `fda.gov`
- EPAR (European Public Assessment Report) con la valutazione completa di efficacia e sicurezza; riassunto delle caratteristiche del prodotto; FDA label e database FAERS per le segnalazioni avverse. Libero. Valore particolare: contengono anche i dati degli studi non pubblicati presentati per la registrazione.

### EFSA — `efsa.europa.eu`
- Opinioni scientifiche su sicurezza alimentare, valori di riferimento nutrizionali, valutazione dei «claims» salutistici (un claim respinto da EFSA è un forte segnale contro l'affermazione). Libero.

### IARC Monographs — `monographs.iarc.who.int`
- Classificazione dei cancerogeni (Gruppo 1, 2A, 2B, 3). Ricorda: il gruppo misura la *forza dell'evidenza* che l'agente possa causare cancro, non *quanto* rischio comporta a una data dose.

### IPCC — `ipcc.ch`
- Rapporti di valutazione sul clima con linguaggio calibrato di confidenza (*virtually certain*, *very likely*, *likely*, *medium confidence*…): riportalo tale e quale accanto a ogni dato.

### National Academies (NASEM) — `nap.nationalacademies.org`
- Rapporti di consenso multidisciplinari (salute, ambiente, energia, educazione). Lettura online libera.

---

## 3. L1 — Letteratura primaria peer-reviewed indicizzata

### PubMed / MEDLINE — `pubmed.ncbi.nlm.nih.gov`
- ~38 milioni di record biomedici con abstract. È il livello meglio servito dagli strumenti: se esiste il connettore MCP PubMed, usalo per cercare (`search_articles`), leggere i metadati (`get_article_metadata`, che include `article_types` — dove compare «Retracted Publication» se ritrattato — e il PMCID se esiste il full text libero) e leggere il full text degli articoli open access (`get_full_text_article`).
- Senza MCP: le E-utilities (`eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json` e `efetch.fcgi?db=pubmed&id=...&rettype=abstract`) sono API libere, se la rete le lascia passare.
- Filtri: `systematic review[pt]`, `meta-analysis[pt]`, `randomized controlled trial[pt]`, `humans[mh]`, `english[la]`, date `2020:2026[dp]`. Sintassi completa in `strategie-di-ricerca.md`.

### PubMed Central — `pmc.ncbi.nlm.nih.gov`
- Full text libero. Se il record PubMed ha un PMCID, i metodi, la sezione Funding e le tabelle sono leggibili.

### Europe PMC — `europepmc.org`
- 40+ milioni di record (include preprint etichettati, e collega la versione preprint a quella pubblicata). API REST libera: `www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json`. Utile anche per trovare il full text quando PMC non lo ha.

### DOAJ — `doaj.org`
- Directory delle riviste open access verificate. Usalo come filtro anti-predatorio: una rivista OA assente da DOAJ merita un controllo.

### SciELO — `scielo.org`
- Riviste di America Latina, Spagna, Portogallo, Sudafrica. Full text libero.

### ERIC — `eric.ed.gov`
- Educazione: articoli, rapporti, tesi. Molti full text.

### PEDro — `pedro.org.au`
- Fisioterapia: trial e revisioni con punteggio di qualità PEDro (0–10). Libero.

### PubPsych — `pubpsych.eu`
- Motore europeo per la psicologia (PSYNDEX, ERIC, MEDLINE, NARCIS e altri). Libero; buon complemento a PsycNet.

### PsycNet / APA — `psycnet.apa.org`
- Record e abstract della psicologia; full text a pagamento. Molti articoli di psicologia clinica sono comunque indicizzati in PubMed.

### NASA ADS — `ui.adsabs.harvard.edu`
- Astronomia, astrofisica, fisica. API libera con token.

### AGRIS (FAO) — `agris.fao.org`
- Agricoltura, alimentazione, ambiente rurale.

### RePEc / IDEAS — `ideas.repec.org`
- Economia: articoli e working paper. Attenzione: mescola peer-reviewed (L1) e working paper (L5): controlla lo stato di pubblicazione di ogni record.

---

## 4. L2 — Registri di studi e protocolli

Servono per il controllo anti-outcome-switching e per scoprire studi completati ma mai pubblicati (segnale di publication bias).

| Registro | Dominio | Come interrogarlo |
|---|---|---|
| ClinicalTrials.gov | `clinicaltrials.gov` | API v2 libera: `clinicaltrials.gov/api/v2/studies/NCTxxxxxxxx` (JSON) e `…/api/v2/studies?query.term=…`. Pagina web: `clinicaltrials.gov/study/NCTxxxxxxxx`. Confronta outcome primario, misura, tempo, campione previsto e date con la pubblicazione. |
| WHO ICTRP | `trialsearch.who.int` | Meta-registro globale; ricerca web. |
| EU CTIS / EU CTR | `euclinicaltrials.eu`, `clinicaltrialsregister.eu` | Registro europeo (CTIS dal 2023; EudraCT storico). |
| ISRCTN | `isrctn.com` | Registro internazionale, con API. |
| DRKS | `drks.de` | Registro tedesco. |
| PROSPERO | `crd.york.ac.uk/prospero` | Registro delle revisioni sistematiche; nessuna API, pagina per record `display_record.php?RecordID=…`. Una revisione non registrata è un segnale di rischio (non una prova di scarsa qualità). |
| OSF Registries | `osf.io/registries` | Pre-registrazioni multidisciplinari (psicologia in particolare). |
| Cochrane protocols | via PubMed | I protocolli Cochrane sono pubblicati e indicizzati: cerca il titolo + «protocol». |

---

## 5. L3 — Aggregatori, motori bibliografici e API aperte

Mai fonte terminale: servono a **trovare** il documento primario e a misurare quanto è stato ripreso o contestato.

| Strumento | Dominio | Punto di forza | Interrogazione |
|---|---|---|---|
| OpenAlex | `openalex.org` | ~250M+ opere, citazioni, autori, concetti; dati aperti | API senza chiave: `api.openalex.org/works?search=…` (aggiungi `&mailto=` per la corsia cortese) |
| Semantic Scholar | `semanticscholar.org` | Citazioni «influenti», TLDR, PDF OA | API libera con limiti: `api.semanticscholar.org/graph/v1/paper/search?query=…` |
| Crossref | `crossref.org` | Metadati di ogni DOI, incluse ritrattazioni e correzioni (campi `update-to`/`updated-by`, che integrano i dati Retraction Watch) | `api.crossref.org/works/<DOI>` |
| Unpaywall | `unpaywall.org` | Trova la versione legalmente aperta di un DOI | `api.unpaywall.org/v2/<DOI>?email=…` |
| CORE | `core.ac.uk` | Aggregatore di repository istituzionali con full text | API con chiave gratuita |
| BASE | `base-search.net` | Metadati da migliaia di repository accademici | ricerca web |
| Lens.org | `lens.org` | Letteratura + brevetti | l'uso avanzato richiede login |
| Dimensions (free) | `app.dimensions.ai` | Pubblicazioni, grant, citazioni | ricerca web, funzioni limitate |
| scite | `scite.ai` | «Smart citations»: quante citazioni *sostengono* o *contraddicono* un lavoro | freemium; utile per capire se un risultato è contestato |
| Google Scholar | `scholar.google.com` | Copertura ampia | opaco, non riproducibile, blocca gli agenti: solo in supporto |

---

## 6. L4 — Banche dati fattuali, statistiche ufficiali, dati strutturali

Autorevoli e accurate, ma **descrittive**: forniscono numeri, non nessi causali. Usale per rischi di base, prevalenze, valori di riferimento — mai per sostenere l'efficacia di un intervento.

**Salute e demografia**: `who.int/data/gho` · `healthdata.org` (GBD, con Results Tool) · `ecdc.europa.eu/en/data` · `dati.istat.it` · `demo.istat.it` · `ec.europa.eu/eurostat` · `data-explorer.oecd.org` · `data.worldbank.org` · `data.un.org` · `ourworldindata.org` (secondario: risali sempre alla fonte primaria indicata sotto ogni grafico).

**Farmaci e sostanze**: `aifa.gov.it` (banca dati farmaci) · `ema.europa.eu/en/medicines` · `dailymed.nlm.nih.gov` (label FDA) · `pubchem.ncbi.nlm.nih.gov` · `ebi.ac.uk/chembl` · `go.drugbank.com` (accademico libero con limiti).

**Biologia e genetica**: `ncbi.nlm.nih.gov` (Gene, ClinVar, dbSNP, GenBank) · `uniprot.org` · `rcsb.org` · `ensembl.org` · `platform.opentargets.org` · `omim.org` · `gbif.org`.

**Fisica e chimica**: `nist.gov` e `webbook.nist.gov` (dati di riferimento) · `iupac.org` · `codata.org` (costanti fondamentali) · `pdg.lbl.gov` (fisica delle particelle).

**Ambiente, spazio, geoscienze**: `copernicus.eu` · `noaa.gov` · `usgs.gov` · `esa.int` · `nasa.gov` · `epa.gov` · `eea.europa.eu`.

**Diritto e normativa**: `normattiva.it` · `eur-lex.europa.eu` · `gazzettaufficiale.it` · `curia.europa.eu`.

---

## 7. L5 — Preprint e letteratura grigia

**Non peer-reviewed.** Utili per la frontiera della ricerca e per verificare se un risultato è recente o contestato; mai come prova di efficacia. La certezza parte da **Bassa** (disegno sperimentale) o **Molto bassa** (osservazionale), e ogni citazione porta l'etichetta «preprint, non sottoposto a revisione paritaria».

**Server di preprint**: `arxiv.org` (fisica, matematica, informatica; API libera `export.arxiv.org/api/query?search_query=…`) · `biorxiv.org` e `medrxiv.org` (biologia, medicina; API `api.biorxiv.org`) · `chemrxiv.org` · `psyarxiv.com` · `osf.io/preprints` · `socarxiv.org` · `eartharxiv.org` · `ssrn.com` · `researchsquare.com`.

**Working paper autorevoli ma non revisionati**: `nber.org` · `iza.org` · `cepr.org`. In economia sono spesso la forma in cui i risultati circolano per anni: trattali come L5 di alta qualità, e verifica se nel frattempo sono stati pubblicati.

**Tesi e rapporti**: `oatd.org` (tesi OA) · rapporti governativi e di agenzie (possono essere autorevoli: giudicali con AGREE II o con i criteri della sezione 10).

**Controllo obbligatorio per i preprint**: verifica se esiste una versione pubblicata (Europe PMC collega preprint e articolo; bioRxiv/medRxiv mostrano «Now published in…»). Se esiste, cita quella. Se il preprint ha più di 2 anni e non è mai stato pubblicato, è un segnale negativo da riportare.

---

## 8. Fuori gerarchia: uso strumentale, mai come fonte

Blog divulgativi, siti commerciali, testate generaliste, social network, contenuti generati da IA (inclusi i riassunti di Consensus, Scholar GPT e simili), aggregatori di notizie sanitarie, Wikipedia, siti che vendono il prodotto di cui parlano.

Possono servire solo per **individuare** uno studio, che va poi recuperato e verificato alla fonte primaria. Wikipedia è utile per la sua bibliografia, non per il suo testo. Un articolo di giornale che dice «uno studio dimostra» è un indizio per una ricerca, non una citazione. Sci-Hub e simili non vanno mai usati né suggeriti.

---

## 9. Percorsi tematici

### Psicologia clinica e psicoterapia
1. **Cochrane** (Common Mental Disorders, Schizophrenia, Developmental Psychosocial Learning Problems) via PubMed con `"Cochrane Database Syst Rev"[Journal]`.
2. **NICE** linee guida di salute mentale (depressione, ansia, PTSD, disturbi di personalità): contengono revisioni per ogni intervento psicologico.
3. **Campbell Collaboration** per interventi psicosociali, scolastici, familiari.
4. **APA Division 12** — `div12.org/psychological-treatments`: elenco dei trattamenti con supporto empirico, con forza della ricerca dichiarata. Secondario ma con fonti.
5. **PubMed** con `psychotherapy[mh]` o il nome dell'approccio (es. `"schema therapy"`, `"metacognitive therapy"`) + `randomized controlled trial[pt]`.
6. **PsyArXiv/OSF** per preprint e **replicazioni**: in psicologia la crisi di replicabilità impone di cercare esplicitamente «replication» + titolo/effetto. Un effetto celebre non replicato (molti effetti di *priming* sociale, *ego depletion* nelle forme originali, *power posing* sugli ormoni) va presentato come contestato, non come acquisito.
7. Persuasione e bias cognitivi: molte «leve» divulgate poggiano su studi singoli degli anni '70–'90 con campioni piccoli. Cerca meta-analisi recenti (PubMed, PsycNet, Campbell) e le replicazioni multi-laboratorio (Many Labs, su OSF) prima di attribuire un effect size.

### Nutrizione e integratori
EFSA (valori di riferimento e claims) → Cochrane → PubMed (`dietary supplements[mh]`). Segnala sempre il finanziamento: l'industria degli integratori finanzia molti trial piccoli e positivi.

### Fonti italiane
ISS/SNLG e EpiCentro (linee guida, epidemiologia) · AIFA (farmaci, note, rapporti OsMed) · Ministero della Salute `salute.gov.it` · ISTAT · Normattiva. Per la pratica clinica italiana, la fonte L0 più pertinente è spesso SNLG; per i dati L4, ISTAT.

### Scienze sociali ed educazione
Campbell → EEF Toolkit → ERIC → PubPsych → NBER/IZA (L5). Molti effetti sono contestuali (paese, sistema scolastico): dichiara sempre la trasferibilità.

### Scienze dure
Per le costanti e i dati di riferimento parti da NIST/CODATA (L4 di massima affidabilità); per la frontiera da arXiv con la verifica della pubblicazione successiva; per le revisioni, `Reviews of Modern Physics`, `Chemical Reviews`, `Annual Reviews` (spesso a pagamento: usa l'abstract e cerca la versione arXiv).

---

## 10. Come giudicare una fonte non in elenco

Quando trovi una fonte che non compare qui, assegnale un livello rispondendo a queste domande, nell'ordine:

1. **Chi la produce e con quale processo dichiarato?** Panel indipendente con metodologia pubblicata (GRADE, AGREE II) → candidata L0. Rivista con peer review verificabile (indicizzata in MEDLINE/Scopus/DOAJ) → L1. Nessuna revisione → L5 o fuori gerarchia.
2. **È un'analisi critica o una raccolta?** Sintetizza e valuta → L0; presenta dati primari → L1; cataloga → L3; misura → L4.
3. **Ha un interesse nel risultato?** Un ente che vende, promuove o regola ciò di cui parla può essere autorevole (le agenzie regolatorie lo sono) ma richiede la nota sul conflitto.
4. **È aggiornata e versionata?** Data, versione, procedura di aggiornamento dichiarata sono segnali di serietà.
5. **È riproducibile?** Se non puoi risalire ai dati o alle fonti primarie, non può stare sopra L5.

Nel dubbio tra due livelli, assegna il più basso e dillo.
