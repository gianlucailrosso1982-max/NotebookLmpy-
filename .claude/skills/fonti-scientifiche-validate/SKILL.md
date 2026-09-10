---
name: fonti-scientifiche-validate
description: Instrada ogni ricerca su affermazioni fattuali verso le fonti scientifiche ad accesso libero più autorevoli, in ordine gerarchico, e assegna a ciascun dato una certezza GRADE con la sua efficacia reale (effetto assoluto, NNT, intervalli di confidenza). Usa questa skill quando l'utente chiede di verificare o documentare un'affermazione scientifica, clinica, psicologica, statistica, nutrizionale o di salute pubblica — "cosa dice la scienza", "quali sono le prove", "è vero che", "fonti autorevoli", "quanto è efficace", "verifica questa affermazione" — o quando scrive contenuti divulgativi, clinici, formativi o giornalistici che devono poggiare su fonti verificabili. Attivala anche in autonomia quando una risposta rischierebbe di presentare come certo un dato con basi deboli. Non attivarla per opinioni, preferenze, quesiti di programmazione o fatti banali non contestati.
---

# Fonti Scientifiche Validate — Protocollo di ricerca gerarchica e valutazione dell'efficacia reale

## Mappa della skill

Questo file contiene il protocollo completo e basta da solo per la maggior parte dei quesiti. I file in `references/` approfondiscono; `scripts/effetti.py` fa i calcoli. Leggili quando la fase corrispondente lo richiede, non prima.

| File | Quando leggerlo |
|---|---|
| `references/strategie-di-ricerca.md` | Fase 1–2: costruire o correggere una query; sintassi PubMed; set di domini; terminologia italiano→inglese |
| `references/gerarchia-fonti.md` | Fase 2: scegliere da dove partire per tipo di quesito; alternative dello stesso livello; percorsi tematici (psicologia clinica, nutrizione, fonti italiane) |
| `references/strumenti-e-fallback.md` | Fase 3 e ogni volta che uno strumento fallisce: cosa fanno davvero WebSearch, WebFetch, i connettori PubMed e Consensus; tabella dei fallback; budget |
| `references/controllo-qualita.md` | Fase 4: procedure per ritrattazioni, conflitti, protocollo, coerenza dei numeri, attualità |
| `references/grade-e-efficacia.md` | Fase 5–6: criteri operativi GRADE, lettura delle tabelle Summary of Findings, effetti assoluti, MCID, lessico calibrato |
| `references/formato-output.md` | Fase 6: scheda completa campo per campo, mini-scheda, testi multi-affermazione, convivenza con i formati dei connettori |
| `references/esempi-svolti.md` | Per vedere il protocollo applicato a casi reali (dati verificati), inclusa la modalità rapida e il caso «non verificabile» |
| `references/glossario.md` | Quando devi spiegare un termine al lettore |
| `scripts/effetti.py` | Ogni volta che trasformi un effetto relativo in assoluto, calcoli un NNT, o controlli che i numeri di una fonte tornino |

---

## 1. Principio guida

Tre domande, sempre separate e mai confuse:

1. **Quanto è autorevole la FONTE?** → Livello gerarchico L0–L5 (sezione 4).
2. **Quanto è solido il DATO?** → Certezza GRADE: Alta, Moderata, Bassa, Molto bassa (sezione 5).
3. **Quanto conta l'effetto nella realtà?** → Effetto assoluto, NNT, danni, rilevanza per la persona (sezione 6).

Una fonte di livello massimo può ospitare un dato di certezza molto bassa: una revisione Cochrane può concludere «evidenza molto incerta». Un risultato statisticamente significativo può essere irrilevante per chi lo riceve. Non promuovere mai un dato per la rivista che lo ospita, e non riportare mai un effetto relativo senza chiederti da quale rischio di base parte.

Questa skill esiste per impedire tre errori che un assistente commette con naturalezza: **citare con sicurezza numeri che non ha letto**, **presentare come verificato ciò che non ha verificato**, e **far sembrare grande un effetto piccolo**. Ogni regola qui sotto discende da uno di questi tre rischi.

---

## 2. Fase 0 — Triage di proporzionalità

Scegli la modalità prima di cercare e dichiarala nella risposta.

- **Modalità rapida** — quesito singolo, non controverso, non destinato a pubblicazione (una curiosità, un fatto da confermare): una o due ricerche sul livello più alto pertinente, una fonte L0/L1 aperta e letta, mini-scheda a quattro righe (affermazione, certezza, effetto, fonte con link, limiti). Le regole ferme valgono per intero: cambia il numero di fonti, non l'onestà.
- **Protocollo completo** — quesito clinico o controverso, più affermazioni da verificare, contenuto destinato a pubblicazione o a decisioni: tutte le fasi che seguono.

Nel dubbio, usa la modalità rapida dichiarando il limite e offrendo il protocollo completo. Un protocollo completo per «il caffè disidrata?» spreca risorse; una modalità rapida per un capitolo clinico produce false sicurezze.

---

## 3. Protocollo operativo

**Fase 1 — Formulare il quesito.**
Per quesiti clinici e comportamentali usa PICO (Popolazione, Intervento, Confronto, Outcome); per gli altri esplicita fenomeno, contesto, misura, periodo. Se il quesito è vago, restringilo prima di cercare; se un'affermazione mescola due cose («previene e cura»), sdoppiala. **Traduci il quesito in inglese**: quasi tutte le fonti indicizzano in inglese, e una query in italiano ne dimezza il recupero. → `strategie-di-ricerca.md` §1, §9.

**Fase 2 — Discesa gerarchica.**
Parti dal livello più alto pertinente per il tipo di quesito (tabella in `gerarchia-fonti.md` §1) e scendi solo se non trovi risposta; per affermazioni controverse cerca comunque conferma incrociata su due fonti indipendenti (non dello stesso gruppo di autori). Usa i connettori quando esistono e `allowed_domains` di WebSearch per vincolare la ricerca al livello che interroghi. Non partire mai dal web aperto. Due avvertenze verificate sul campo:
- `allowed_domains` è un filtro **non garantito**: opera sul dominio registrabile e, in alcune chiamate, i risultati arrivano interamente da domini non richiesti. Controlla ogni risultato; se nessuno appartiene ai domini richiesti, la ricerca per quel livello è fallita: ripetila mettendo il nome dell'ente nella query o passa ai connettori.
- **Gli snippet dei risultati di ricerca servono a scegliere cosa aprire, mai a citare.** Contengono numeri pre-digeriti da un modello: non sono lettura della fonte. Un numero è citabile solo dopo la Fase 3.
Se la prima query restituisce rumore, calibrala (§5 di `strategie-di-ricerca.md`) prima di concludere che non esistono sintesi.

**Fase 3 — Recupero del testo, con fallback a cascata.**
Fermati al primo canale che funziona: (1) connettori MCP attivi in questa sessione (verificane l'esistenza: spesso ci sono solo PubMed e Consensus, e i connettori PubMed leggono anche gli abstract completi delle revisioni Cochrane); (2) WebFetch sull'URL della fonte; (3) se entrambi falliscono, il documento è **non letto**: puoi elencarlo come «da approfondire», ma nessun suo dato è citabile e i controlli risultano «non verificati (accesso bloccato)». In ambienti con proxy di rete restrittivo il fetch fallisce su quasi tutti i domini scientifici: non è un tuo errore, è un limite da dichiarare. Un connettore che risponde ma restituisce il full text **vuoto** conta come canale fallito: passa al successivo. Per le revisioni Cochrane, PMC contiene di norma solo abstract e Plain Language Summary (che però riporta numeri assoluti e certezza per outcome): usali e dichiara «letto: abstract + PLS». Richiedi i metadati a lotti di al massimo 8 PMID: le risposte grandi finiscono su file e costano letture aggiuntive. Leggi almeno l'abstract completo e, quando accessibile, metodi, risultati numerici, finanziamento. Annota per ogni fonte cosa hai letto (abstract / abstract + PLS / full text). → `strumenti-e-fallback.md` §7.

**Fase 4 — Controllo qualità prima di citare.**
Per ogni studio: ritrattazioni, segnalazioni post-pubblicazione, legittimità della rivista, conflitti di interesse, corrispondenza col protocollo registrato, coerenza interna dei numeri, attualità. Ogni controllo ha tre esiti — **superato / fallito / non verificato (strumento non accessibile)** — e va riportato con lo strumento usato. Salta questa fase solo per documenti istituzionali di livello L0, per i quali restano attualità e conflitti. → sezione 7 e `controllo-qualita.md`.

**Fase 5 — Certezza dell'evidenza.**
Se la fonte L0 riporta già un giudizio GRADE (abstract e Summary of Findings Cochrane, gradi delle linee guida, gradi USPSTF), usa quello e citalo. Solo in assenza di una sintesi già valutata assegna un livello tu, con lo schema della sezione 5, etichettandolo «valutazione indicativa dell'assistente, non un GRADE formale» e scrivendo «non valutabile dai dati letti» per i domini che non hai potuto vedere. → `grade-e-efficacia.md` §5–6.

**Fase 6 — Efficacia reale e restituzione.**
Trasforma il relativo in assoluto (script), riporta NNT, IC, danni, outcome e popolazione; scegli le parole in base alla certezza; produci le schede e i quattro blocchi di chiusura (sezione 8). Dichiara ciò che non hai trovato: l'assenza di evidenza è un'informazione. → sezioni 6 e 8, `formato-output.md`.

---

## 4. Gerarchia delle fonti ad accesso libero

Il livello descrive la fonte, non il dato. Elenco completo, accessi reali, API e percorsi tematici in `gerarchia-fonti.md`.

| Livello | Che cosa | Fonti principali | Nota operativa |
|---|---|---|---|
| **L0** | Sintesi critiche, revisioni sistematiche valutate, linee guida istituzionali; linee guida di società scientifiche **solo se** con metodo di ricerca e grading dichiarati (altrimenti «consenso di esperti», L1) | Cochrane, Epistemonikos, WHO, NICE, USPSTF, AHRQ, Campbell (scienze sociali), JBI, INAHTA, ISS/SNLG, CDC/ECDC, EMA/AIFA/FDA, EFSA, IARC, IPCC, NASEM | Ogni revisione Cochrane è su PubMed con l'abstract completo, risultati numerici e spesso la certezza GRADE: cercala lì quando il sito è bloccato (`"Cochrane Database Syst Rev"[journal]`) |
| **L1** | Letteratura primaria peer-reviewed indicizzata | PubMed/MEDLINE, PMC, Europe PMC, DOAJ, SciELO, ERIC, PEDro, PubPsych, PsycNet, NASA ADS, AGRIS | Il livello meglio servito dagli strumenti; usa i filtri `systematic review[pt]`, `meta-analysis[pt]`, `randomized controlled trial[pt]` |
| **L2** | Registri di studi e protocolli | ClinicalTrials.gov (API v2), WHO ICTRP, EU CTIS, ISRCTN, PROSPERO, OSF | Il controllo più efficace contro l'outcome switching e gli studi mai pubblicati |
| **L3** | Aggregatori e API bibliografiche | OpenAlex, Semantic Scholar, Crossref (metadati e ritrattazioni), Unpaywall, CORE, BASE, scite, Google Scholar (solo in supporto) | Mai fonte terminale: portano al documento primario |
| **L4** | Banche dati fattuali e statistiche ufficiali | WHO GHO, GBD/IHME, Eurostat, OECD, ISTAT, World Bank; NCBI, UniProt, PDB; NIST, CODATA; Copernicus, NOAA; Normattiva, EUR-Lex | Descrittive: forniscono numeri e rischi di base, non nessi causali né efficacia |
| **L5** | Preprint e letteratura grigia | arXiv, bioRxiv, medRxiv, PsyArXiv, OSF, SSRN, NBER | Non peer-reviewed: etichetta «preprint», certezza da Bassa (sperimentale) o Molto bassa (osservazionale); verifica se esiste la versione pubblicata |
| **Fuori** | Blog, testate generaliste, social, contenuti generati da IA, siti commerciali, Wikipedia | — | Solo per individuare uno studio, mai come fonte |

---

## 5. Certezza dell'evidenza (GRADE)

**Punto di partenza per disegno**: revisione sistematica o meta-analisi di RCT e RCT singolo → **Alta**; coorte e caso-controllo → **Bassa**; trasversale, serie di casi, caso singolo, opinione di esperti, studi pre-clinici (per conclusioni sull'uomo) → **Molto bassa**; preprint → Bassa se sperimentale, Molto bassa se osservazionale; meta-analisi di studi osservazionali → Bassa (parte dal disegno degli studi inclusi).

**Cinque motivi di declassamento** (uno o due gradini ciascuno): rischio di bias (randomizzazione o cecità assenti, abbandoni sbilanciati, outcome cambiati, analisi non ITT); incoerenza (stime in direzioni opposte, IC non sovrapposti, I² alto); indirettezza (popolazione, intervento, confronto o outcome diversi dal quesito; surrogati); imprecisione (pochi eventi, IC che include beneficio e danno rilevanti o attraversa la MCID); bias di pubblicazione (solo studi piccoli e positivi, funnel asimmetrico, evidenza solo sponsorizzata, studi registrati mai pubblicati). Criteri operativi in `grade-e-efficacia.md` §3.

**Tre motivi di rialzo** (solo osservazionali): effetto grande (RR > 2 o < 0,5; > 5 o < 0,2 vale due gradini), gradiente dose-risposta, confondimento residuo che andrebbe contro l'effetto.

| Simbolo | Livello | Significato | Lessico |
|---|---|---|---|
| ⬤⬤⬤⬤ | Alta | L'effetto vero è molto probabilmente vicino alla stima | «riduce», «produce poca o nessuna differenza» |
| ⬤⬤⬤◯ | Moderata | Probabilmente vicino, ma potrebbe differire | «probabilmente riduce» |
| ⬤⬤◯◯ | Bassa | Fiducia limitata | «potrebbe ridurre», «l'evidenza suggerisce» |
| ⬤◯◯◯ | Molto bassa | Fiducia minima | «non è chiaro se», «l'evidenza è molto incerta» |

La certezza è per outcome, non per studio: la stessa revisione può essere Alta sulla mortalità e Molto bassa sulla qualità di vita. La «certezza globale» della sintesi è quella dell'outcome che conta di più, non una media.

---

## 6. Efficacia reale — cosa riportare sempre

- **Effetto assoluto accanto al relativo.** «Riduce il rischio del 50%» è vuoto: da 2% a 1% è piccolo, da 40% a 20% è enorme. Riporta la differenza in punti percentuali o per 1000, con l'IC. Se la fonte dà solo il relativo e nessun rischio di base, scrivi «effetto assoluto non riportato nella fonte»; se vuoi un ordine di grandezza, calcolalo **dichiarando** il rischio di base assunto e la sua provenienza. Mai un numero assoluto senza origine.
- **NNT e NNH**, con IC; se l'IC della differenza include lo zero, l'IC dell'NNT passa per l'infinito e va scritto così, non come intervallo finito.
- **Intervallo di confidenza al 95%**, sempre; un IC stretto attorno al nullo è certezza di un effetto assente, non imprecisione.
- **MCID**: l'effetto supera la soglia che la persona percepisce? Se non conosci la MCID dello strumento, dillo.
- **Outcome reale o surrogato** (mortalità, ricadute, funzionamento vs marcatori di laboratorio, punteggi intermedi): segnala i surrogati e declassa per indirettezza se il quesito riguarda l'esito clinico.
- **Durata del follow-up, popolazione, dose, contesto**, con i limiti di trasferibilità.
- **Danni**, con frequenze assolute nei due gruppi; «non riportati nella fonte» quando è così. Un'analisi che riporta solo i benefici è incompleta per definizione.
- **Coerenza dei numeri della fonte**: percentuali che tornano con i conteggi, stima dentro l'IC, NNT ≈ 1/differenza. Se non tornano, segnala la discrepanza senza scegliere.

Usa lo script per non fare aritmetica a mente e per rendere ogni calcolo tracciabile:

```
python3 scripts/effetti.py relative --measure OR --value 0.31 --ci 0.20 0.48 --baseline 0.45   # fallimento del trattamento (evento indesiderato)
python3 scripts/effetti.py relative --measure RR --value 1.20 --ci 1.05 1.37 --baseline 0.30 --event desirable   # remissione (evento desiderato)
python3 scripts/effetti.py table --ei 128 --ni 419 --ec 100 --nc 423
python3 scripts/effetti.py nnt --arr -0.15 --ci -0.25 -0.05
python3 scripts/effetti.py smd --value 0.45
```

Senza `--event` lo script stampa entrambe le letture (evento indesiderato / desiderato): scegli quella giusta per l'outcome. Vale per uno studio o per una tabella già aggregata dagli autori: sommare gli eventi di più studi non riproduce una meta-analisi.

---

## 7. Controllo qualità prima di citare

Ogni controllo ha uno strumento primario **meccanicamente interrogabile**; gli strumenti di riserva sono best effort. Procedure complete in `controllo-qualita.md`.

| Controllo | Strumento primario | Riserva | Che cosa cerchi |
|---|---|---|---|
| Ritrattazione | Metadati PubMed: `article_types` contiene «Retracted Publication», «Expression of Concern», «Published Erratum»; collegamenti «Retraction in» / «Erratum in» | API Crossref (`api.crossref.org/works/<DOI>`, campi `update-to`/`updated-by`); Retraction Watch se raggiungibile | Articolo ritrattato, corretto o con dubbi formali |
| Post-pubblicazione | Ricerca mirata via connettore: `"<parole del titolo>"[ti] AND (comment[pt] OR letter[pt])`; i collegamenti «Comment in» del record PubMed sono visibili solo sulla pagina web (WebFetch) o via E-utilities, **non nei metadati del connettore** | PubPeer (app JavaScript, spesso non leggibile); scite | Segnalazioni su immagini, dati, statistiche; lettere critiche |
| Legittimità della rivista | Indicizzazione MEDLINE (il record esiste su PubMed) | DOAJ, SCImago | Peer review reale; segnali predatori |
| Conflitti di interesse | Sezioni Funding / Competing interests del full text (PMC) | registro del trial (sponsor) | Chi ha finanziato, chi ha analizzato; allegiance in psicoterapia |
| Corrispondenza col protocollo | API ClinicalTrials.gov v2 (`/api/v2/studies/<NCT>`), PROSPERO | pagina web del registro | Outcome primario, tempo, campione, data di registrazione |
| Coerenza dei numeri | `scripts/effetti.py` e controllo manuale | — | Percentuali vs conteggi, stima dentro l'IC, totali |
| Attualità | Data della ricerca dichiarata («searched to…»); versione `.pubN`; ricerca del titolo con `[ti]` ordinata per data per trovare aggiornamenti («Update in» non è esposto dal connettore); RCT successivi con filtro data | — | Sintesi superate, linee guida > 5 anni, note regolatorie recenti |

Tre esiti, sempre con lo strumento: **superato**, **fallito** (non citare come evidenza; se lo citi perché è l'unico, dichiara il problema nel testo), **non verificato (strumento non accessibile)**. **Mai compilare l'esito di un controllo non eseguito**: scrivere «nessuna ritrattazione» senza aver interrogato nulla è la violazione più grave di questo protocollo, perché simula proprio il rigore che dovrebbe garantire. Un «non verificato» onesto vale più di dieci «superato» presunti.

---

## 8. Formato di restituzione

Prosa per la sintesi, tabella per il dettaglio. Una scheda per affermazione. Per testi con molte affermazioni: scheda completa per le 5–7 più rilevanti o fragili, tabella riassuntiva per le altre, tetto dichiarato. Guida campo per campo e mini-scheda in `formato-output.md`.

```
### [Affermazione in una riga, come la direbbe il lettore]

**Certezza dell'evidenza: ⬤⬤⬤◯ MODERATA** — [dichiarata dalla fonte / valutazione indicativa dell'assistente]

Che cosa dicono i dati — [2–4 frasi in linguaggio chiaro: prima l'effetto assoluto, poi il relativo,
per chi e per quanto, e i danni; lessico calibrato sulla certezza]

| Voce | Contenuto |
|---|---|
| Fonte | [Autori, anno, rivista/ente] — Livello [L0–L5] — letto: [abstract / full text] |
| Disegno | [Meta-analisi di k RCT, n = …; RCT; coorte…] |
| Effetto relativo | [RR/OR/HR/SMD con IC 95%] |
| Effetto assoluto | [controllo → intervento; differenza in pp o per 1000; NNT/NNH con IC] oppure «non riportato nella fonte» |
| Outcome | [reale / surrogato] · strumento · follow-up |
| Popolazione | [chi, dove, quanti; trasferibilità] |
| Motivo del livello | [domini GRADE declassati/rialzati e perché; o i motivi dichiarati dalla fonte; «non valutabile dai dati letti» dove serve] |
| Danni noti | [con numeri; NNH; o «non riportati nella fonte»] |
| Controlli | Ritrattazioni: [esito (strumento)] · Post-pubblicazione: [esito] · Rivista: [esito] · Conflitti: [esito] · Protocollo: [esito] · Attualità: [esito] · Coerenza numeri: [esito] |
| Link | [https://doi.org/…] · [PMID/PMC] · [URL della fonte L0] |
```

**Chiusura obbligatoria in quattro blocchi**: (1) **Sintesi gerarchica** con la certezza globale; se due fonti L0 divergono, riportale entrambe con data e metodo, senza sceglierne una in silenzio; (2) **Che cosa non sappiamo** — lacune, contraddizioni, e ciò che tu non hai potuto verificare: mai facoltativa; (3) **Fonti** numerate con livello, profondità di lettura e link (le fonti individuate ma non lette in un sotto-elenco «Da approfondire»); (4) **Metodo e limiti** — query eseguite con strumento e numero di risultati, letture, controlli eseguiti e non, blocchi incontrati. Sui temi clinici, una sola frase di responsabilità: le decisioni competono a un professionista che conosce il caso.

**Formati dei connettori**: gli obblighi di attribuzione dei connettori (PubMed: «secondo PubMed» e DOI linkato per ogni articolo; Consensus: citazioni numerate e messaggio finale verbatim; WebSearch: elenco delle fonti) si integrano nella scheda — DOI nella riga Link, numeri nell'elenco Fonti, messaggi in coda — e non la sostituiscono. Una sola numerazione per tutte le fonti.

---

## 9. Regole ferme

- **Mai citare ciò che non hai letto.** Nessun DOI, autore, anno o cifra inventati o ricostruiti a memoria. Gli snippet non sono lettura. Se non hai potuto verificare, scrivilo.
- **Mai compilare l'esito di un controllo non eseguito.** «Non verificato (strumento non accessibile)» è sempre ammesso; un esito inventato mai.
- **Mai un rischio relativo senza il corrispettivo assoluto** quando la fonte lo riporta o lo rende ricavabile; altrimenti «effetto assoluto non riportato nella fonte», e nessuna stima da assunzioni non dichiarate.
- **Mai spacciare un preprint per evidenza consolidata**, né un'analisi dello stesso gruppo per una replicazione indipendente.
- **Mai una conclusione più forte di quanto la certezza consenta.** Con certezza bassa si scrive «alcuni studi suggeriscono», non «è dimostrato».
- **Mai omettere l'evidenza contraria.** Cercala attivamente; se esiste, riportala con il suo peso.
- **Mai confondere correlazione e causalità**, nemmeno per semplificare; con gli studi osservazionali ragiona con Bradford Hill e la triangolazione.
- **Mai «non funziona» quando l'evidenza è assente**: l'assenza di evidenza non è evidenza di assenza.
- **Nessun consiglio clinico personalizzato.** Riporta l'evidenza; le decisioni sul singolo caso competono a un professionista.
- Se la ricerca non produce risultati di livello adeguato, dillo, invece di ripiegare su fonti deboli presentate come solide.

---

## 10. Checklist prima di consegnare

1. Modalità dichiarata (rapida / completa)?
2. Ogni numero viene da una fonte che ho aperto?
3. Ogni relativo ha l'assoluto o la dicitura «non riportato nella fonte»?
4. Certezza dichiarata con la sua origine (fonte / indicativa)?
5. Lessico calibrato sulla certezza?
6. Danni riportati o dichiarati non riportati?
7. Riga Controlli con sette voci, ciascuna con esito e strumento, nessuna simulata?
8. «Che cosa non sappiamo» presente e sostanziale?
9. Fonti con livello, profondità di lettura e link; nessuna fonte non letta mescolata a quelle lette?
10. «Metodo e limiti» sufficiente a rifare la ricerca?

---

## 11. Riferimenti metodologici

GRADE Working Group — certezza dell'evidenza e forza delle raccomandazioni (`gradeworkinggroup.org`; GRADE Handbook, `gdt.gradepro.org/app/handbook/handbook.html`). Cochrane Handbook for Systematic Reviews of Interventions (`training.cochrane.org/handbook`), con le «informative statements» per il lessico calibrato. PRISMA 2020 (`prisma-statement.org`). RoB 2 e ROBINS-I per il rischio di bias; AMSTAR 2 per la qualità delle revisioni; AGREE II per le linee guida. Altman DG, «Confidence intervals for the number needed to treat», BMJ 1998, per l'IC dell'NNT. Bradford Hill A, «The environment and disease: association or causation?», 1965, per la causalità negli studi osservazionali.
