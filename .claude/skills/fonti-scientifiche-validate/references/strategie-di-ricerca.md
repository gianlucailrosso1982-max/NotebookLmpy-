# Strategie di ricerca — dal quesito alla query

Leggi questo file nella **Fase 1–2** quando devi costruire o correggere una ricerca. Contiene la sintassi PubMed che funziona con il connettore MCP, i modelli di query per tipo di quesito, i set di domini per WebSearch e la procedura di calibrazione quando i risultati sono troppi, troppo pochi o fuori tema.

## Indice

1. Dal quesito alla query in cinque passi
2. Sintassi PubMed essenziale
3. Filtri per disegno di studio
4. Modelli di query per tipo di quesito
5. Calibrare: troppi, troppo pochi, fuori tema (con un caso reale)
6. Trovare la sintesi più recente
7. Cercare nei registri
8. Query per Consensus e per WebSearch (set di domini)
9. Terminologia: dall'italiano all'inglese senza perdere il senso
10. Il registro delle query

---

## 1. Dal quesito alla query in cinque passi

1. **Scomponi** il quesito in concetti (PICO per i quesiti clinici: Popolazione, Intervento, Confronto, Outcome; per gli altri: fenomeno, contesto, misura, periodo). Di norma bastano 2–3 concetti per la query: Popolazione + Intervento, oppure Intervento + Outcome. Il confronto raramente serve nella query.
2. **Traduci in inglese** ogni concetto e cerca i sinonimi: nome comune, termine tecnico, sigla, nome commerciale e principio attivo (INN).
3. **Cerca il termine MeSH** (Medical Subject Headings) corrispondente: PubMed mappa automaticamente molte parole (leggi `query_translation` nel risultato del connettore per vedere cosa ha capito). Il MeSH cattura anche gli articoli che usano sinonimi che non hai pensato.
4. **Combina**: OR dentro a ciascun concetto, AND tra concetti. Metti le frasi tra virgolette.
5. **Aggiungi il filtro di disegno** solo dopo aver visto che la query di base è pertinente: `systematic review[pt]`, `meta-analysis[pt]`, `randomized controlled trial[pt]`.

Esempio — «La vitamina C previene il raffreddore?»:
- Concetti: vitamina C (ascorbic acid, vitamin C) · raffreddore comune (common cold) · outcome: incidenza/durata.
- Query: `("vitamin C" OR "ascorbic acid") AND "common cold" AND (systematic review[pt] OR meta-analysis[pt])`

---

## 2. Sintassi PubMed essenziale

| Elemento | Sintassi | Note |
|---|---|---|
| Campo titolo | `termine[ti]` | massima precisione |
| Titolo o abstract | `termine[tiab]` | il campo più usato |
| Termine MeSH | `termine[mh]` | include i termini più specifici sotto di esso |
| MeSH principale | `termine[majr]` | solo articoli in cui è argomento centrale |
| Autore | `Cognome I[au]` | |
| Rivista | `"Cochrane Database Syst Rev"[journal]` | anche `[ta]` |
| Tipo di pubblicazione | `systematic review[pt]` | vedi sezione 3 |
| Data di pubblicazione | `2020:2026[dp]` oppure `"last 5 years"[dp]` | |
| Lingua | `english[la]`, `italian[la]` | |
| Specie | `humans[mh]` | esclude gli studi solo animali |
| Frase esatta | `"metacognitive therapy"` | |
| Booleani | `AND`, `OR`, `NOT` | in maiuscolo; `NOT` con cautela: esclude anche articoli che citano il termine per negarlo |
| Parentesi | `(a OR b) AND c` | obbligatorie quando mescoli AND e OR |
| Troncamento | `terap*` | **non supportato dal connettore MCP** (rifiuta i wildcard): usa OR di varianti |

Suggerimento: il connettore restituisce `query_translation`, cioè come PubMed ha espanso la query. Leggilo: se ha mappato «hydration» su dodici varianti e «caffeine» su «caffeinism», capisci perché arrivano risultati fuori tema.

---

## 3. Filtri per disegno di studio

| Cosa cerchi | Filtro |
|---|---|
| Revisioni sistematiche | `systematic review[pt]` — copre anche molte meta-analisi; è un filtro di PubMed basato su un classificatore, non solo sull'etichetta degli autori |
| Meta-analisi | `meta-analysis[pt]` |
| RCT | `randomized controlled trial[pt]` — oppure la versione sensibile: `(randomized controlled trial[pt] OR randomized[tiab] OR placebo[tiab] OR randomly[tiab] OR trial[ti])` |
| Linee guida | `practice guideline[pt] OR guideline[pt]` |
| Studi osservazionali | `observational study[pt] OR cohort studies[mh] OR case-control studies[mh]` |
| Studi diagnostici | `"sensitivity and specificity"[mh] OR diagnostic accuracy[tiab]` |
| Prognosi | `prognosis[mh] OR cohort studies[mh] OR "risk factors"[mh]` |
| Danni | `("adverse effects"[sh] OR "adverse events"[tiab] OR harms[tiab] OR safety[tiab])` |

Attenzione: molte meta-analisi **non sono etichettate** `meta-analysis[pt]` (l'etichetta è assegnata dagli indicizzatori con ritardo o mai). Se il filtro elimina troppo, sostituiscilo con `(meta-analysis[tiab] OR "systematic review"[tiab])`.

---

## 4. Modelli di query per tipo di quesito

**Terapia / efficacia**
`(<intervento>) AND (<condizione>) AND (systematic review[pt] OR meta-analysis[pt])` → poi, se serve, `… AND randomized controlled trial[pt] AND 2020:2026[dp]` per i trial recenti non ancora inclusi.

**Danni / sicurezza**
`(<intervento>) AND ("adverse effects"[sh] OR adverse[tiab] OR harms[tiab] OR safety[tiab] OR tolerability[tiab])` — non filtrare per RCT: i danni rari emergono da coorti, registri e farmacovigilanza (EMA/FDA in L0).

**Prognosi**
`(<condizione>) AND (prognosis[mh] OR "natural history"[tiab] OR cohort studies[mh]) AND (mortality[tiab] OR recurrence[tiab] OR <esito>)`

**Diagnosi**
`(<test>) AND (<condizione>) AND ("sensitivity and specificity"[mh] OR accuracy[tiab])` — cerca anche revisioni Cochrane di accuratezza diagnostica.

**Prevalenza / epidemiologia**
Parti da L4 (GBD, WHO GHO, ISTAT, ECDC) e usa PubMed per revisioni di prevalenza: `(<condizione>) AND (prevalence[tiab] OR incidence[tiab]) AND (systematic review[pt] OR meta-analysis[pt])`.

**Causalità (esposizione → esito)**
`(<esposizione>) AND (<esito>) AND (cohort studies[mh] OR case-control studies[mh] OR "mendelian randomization"[tiab] OR meta-analysis[pt])` — poi valuta con i criteri di Bradford Hill (vedi `grade-e-efficacia.md`, §13).

**Interventi psicologici**
`("<approccio>"[tiab] OR <sinonimi>) AND (<disturbo>) AND (randomized controlled trial[pt] OR meta-analysis[pt])` — esempi di approcci: `"cognitive behavioral therapy"`, `"schema therapy"`, `"metacognitive interpersonal therapy"`, `"mentalization-based"`, `"dialectical behavior therapy"`. Aggiungi `replication[tiab]` in una ricerca separata per gli effetti celebri della psicologia sociale.

**Nutrizione e integratori**
`(<nutriente> OR "dietary supplements"[mh]) AND (<esito>) AND (systematic review[pt] OR meta-analysis[pt])` — e in parallelo su EFSA: `site:efsa.europa.eu <nutriente> claim`.

**Quesiti non biomedici** (educazione, criminologia, economia, clima)
PubMed non li copre. Usa WebSearch con i set di domini della sezione 8 (Campbell, ERIC, NBER, IPCC), Consensus, e le API di OpenAlex/Semantic Scholar per la mappatura.

---

## 5. Calibrare: troppi, troppo pochi, fuori tema

**Troppi risultati** (centinaia, poco pertinenti): sposta i concetti chiave su `[ti]`; aggiungi il filtro di disegno; restringi le date; aggiungi `humans[mh]`.

**Troppo pochi o zero**: rimuovi il filtro di disegno (molte sintesi non sono etichettate); passa da `[ti]` a `[tiab]`; aggiungi sinonimi in OR; togli il concetto meno essenziale (di solito il confronto o l'outcome); prova il MeSH più generale. Se ancora nulla, scendi di livello (L1 → L2/L3/L5) e dichiaralo.

**Fuori tema**: leggi `query_translation`; spesso un termine generico («hydration», «balance») è stato espanso su tutto. Vincola quel termine a `[ti]` o sostituiscilo con il MeSH preciso.

**Caso reale** (sessione di settembre 2026, connettore PubMed):
- Query 1: `caffeine AND (hydration OR diuresis OR fluid balance) AND (meta-analysis[pt] OR systematic review[pt])` → 8 risultati, di cui pertinente uno solo e in modo laterale; gli altri riguardavano la voce, il danno renale neonatale e persino la depurazione delle acque reflue (dove «caffeine» compare come inquinante). Causa: l'espansione automatica di «hydration» e «fluid balance».
- Query 2: `caffeine[Title] AND (diuresis[Title] OR diuretic[Title] OR hydration[Title] OR "fluid balance"[Title]) AND (meta-analysis OR "systematic review")` → 1 risultato, esattamente la meta-analisi cercata.
- Lezione: prima di scendere di livello o concludere «non esistono sintesi», calibra la query. Due tentativi ben ragionati valgono più di dieci ricerche a tentoni.

---

## 6. Trovare la sintesi più recente

- Ordina per data (`sort: pub_date`) e guarda gli ultimi 5 anni.
- Nel record PubMed di una revisione Cochrane cerca la versione (`.pub2`, `.pub3`…) e la dicitura «Update in»; cerca il titolo esatto con `[ti]` per elencare tutte le versioni.
- Una revisione dichiara la data della propria ricerca («searched to November 2012»): cerca gli RCT pubblicati **dopo** quella data (`randomized controlled trial[pt] AND 2013:2026[dp]`) per capire se la sintesi è ancora attuale. Se trovi trial grandi successivi, la revisione va segnalata come potenzialmente superata.
- Le «living systematic reviews» si aggiornano di continuo: preferiscile quando esistono (frequenti in area COVID-19 e oncologia).

---

## 7. Cercare nei registri

- Trova il numero di registrazione nell'abstract o nel full text (`NCT01234567`, `ISRCTN…`, `EudraCT 20xx-…`, `CRD42020…` per PROSPERO).
- ClinicalTrials.gov API v2: `https://clinicaltrials.gov/api/v2/studies/NCT01234567` restituisce JSON con `protocolSection.outcomesModule` (outcome primari e secondari con misura e tempo), `designModule` (campione previsto), `statusModule` (date). Confronta con la pubblicazione: outcome primario, tempo di misura, campione, date di inizio e di registrazione (registrazione *dopo* l'inizio = registrazione retrospettiva, un segnale di rischio).
- Ricerca per argomento: `https://clinicaltrials.gov/api/v2/studies?query.term=<termini>&filter.overallStatus=COMPLETED` per scoprire trial completati e mai pubblicati (controlla `resultsSection`).
- PROSPERO non ha API: pagina `https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=<numero>`.

---

## 8. Query per Consensus e per WebSearch

**Consensus**: query in inglese, formulata come domanda o come combinazione di termini accademici («vitamin C common cold duration randomized»). Nessun filtro salvo richiesta esplicita dell'utente. Usa il risultato per raccogliere DOI/URL da aprire, non per citare.

**WebSearch — set di domini pronti** (5–10 per chiamata):

| Set | Domini |
|---|---|
| L0 sanità internazionale | `cochranelibrary.com`, `who.int`, `nice.org.uk`, `uspreventiveservicestaskforce.org`, `effectivehealthcare.ahrq.gov`, `sign.ac.uk` |
| L0 Italia/Europa | `snlg.iss.it`, `iss.it`, `aifa.gov.it`, `ema.europa.eu`, `ecdc.europa.eu`, `efsa.europa.eu` |
| L0 scienze sociali | `campbellcollaboration.org`, `educationendowmentfoundation.org.uk`, `3ieimpact.org`, `eric.ed.gov` |
| L0 ambiente/clima | `ipcc.ch`, `copernicus.eu`, `noaa.gov`, `nasa.gov`, `eea.europa.eu` |
| L1 biomedicina | `pubmed.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov`, `europepmc.org` |
| L2 registri | `clinicaltrials.gov`, `trialsearch.who.int`, `crd.york.ac.uk`, `isrctn.com` |
| L4 statistiche | `healthdata.org`, `who.int`, `dati.istat.it`, `ec.europa.eu`, `data.worldbank.org` |
| L5 preprint | `medrxiv.org`, `biorxiv.org`, `psyarxiv.com`, `arxiv.org`, `osf.io` |

Ricorda che il filtro opera sul dominio registrabile: controlla i risultati.

---

## 9. Terminologia: dall'italiano all'inglese

| Italiano | Inglese da usare | Attenzione |
|---|---|---|
| efficacia | *efficacy* (condizioni ideali, RCT) / *effectiveness* (pratica reale) | scegli in base al quesito |
| prova, evidenza | *evidence* | «proof» è raro in medicina |
| studio clinico | *clinical trial*; randomizzato: *randomized controlled trial* | |
| linee guida | *guideline(s)* | |
| revisione sistematica | *systematic review* | non «systematic revision» |
| effetti collaterali | *adverse effects / adverse events* | «side effects» è divulgativo |
| guarigione | *remission / cure / recovery* secondo il contesto | |
| ricaduta | *relapse / recurrence* | |
| sopravvivenza | *survival* (overall, progression-free) | |
| dipendenza affettiva | *love addiction / emotional dependency / dependent personality* | i termini variano: prova più sinonimi |
| terapia metacognitiva interpersonale | *metacognitive interpersonal therapy (MIT)* | diversa dalla *metacognitive therapy* di Wells |
| schema therapy | *schema therapy* | |
| leve di persuasione | *persuasion techniques, compliance, social influence* | |
| narcisismo | *narcissism; narcissistic personality disorder (NPD)* | |

Per i farmaci usa il principio attivo internazionale (INN): «paracetamolo» → *paracetamol / acetaminophen* (entrambi, in OR). Per verificare un termine MeSH: `meshb.nlm.nih.gov`.

---

## 10. Il registro delle query

Annota ogni query eseguita con strumento, testo esatto e numero di risultati: va nella nota «Metodo e limiti» della risposta. È ciò che rende la ricerca riproducibile e permette all'utente (o a te in una sessione futura) di riprendere da dove ti sei fermato invece di ricominciare.
