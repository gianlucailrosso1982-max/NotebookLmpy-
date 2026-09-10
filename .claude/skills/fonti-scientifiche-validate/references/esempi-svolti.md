# Esempi svolti

Quattro percorsi reali, eseguiti con il connettore PubMed in un ambiente in cui WebFetch era bloccato verso tutti i domini scientifici (settembre 2026). I numeri sono quelli degli abstract letti; le query sono quelle eseguite. Servono a mostrare **come** si applica il protocollo, incluse le sue rinunce oneste.

## Indice

- Esempio A — Protocollo completo: «La vitamina C previene il raffreddore?»
- Esempio B — GRADE dichiarato dalla fonte, danni e coerenza dei numeri: «I farmaci da banco combinati funzionano?»
- Esempio C — Modalità rapida: «Il caffè disidrata?»
- Esempio D — Quando non si può verificare

---

## Esempio A — Protocollo completo

**Richiesta**: «Sto scrivendo un articolo divulgativo. È vero che la vitamina C previene il raffreddore?»

### Fase 0 — Triage
Contenuto destinato a pubblicazione, affermazione controversa da decenni → **protocollo completo**, dichiarato.

### Fase 1 — Quesito
PICO: P = popolazione generale (adulti e bambini sani); I = vitamina C per bocca, ≥ 0,2 g/die, in modo regolare; C = placebo; O = incidenza dei raffreddori; secondari: durata, gravità; variante: uso terapeutico all'esordio. In inglese: *vitamin C / ascorbic acid — common cold — incidence, duration, severity — prophylaxis vs therapy*. L'affermazione va sdoppiata: «previene» (incidenza) e «accorcia/attenua» (durata, gravità), che hanno risposte diverse.

### Fase 2 — Discesa gerarchica
Partenza da L0 (Cochrane) via connettore PubMed, perché il fetch verso cochranelibrary.com era bloccato.
Query: `vitamin C common cold AND (systematic review[pt] OR meta-analysis[pt])`, ordinata per data → 19 risultati; tra i primi la revisione Cochrane (2013) e una meta-analisi del 2023 dello stesso gruppo.

### Fase 3 — Recupero
Metadati e abstract via `get_article_metadata` per PMID 23440782 (Cochrane 2013) e PMID 38082300 (BMC Public Health 2023). Letto: abstract di entrambe; full text disponibile in PMC (PMC8078152, PMC10712193) ma non consultato in questo esempio: i controlli che richiedono il full text risultano «non verificati».

### Fase 4 — Controlli
- Ritrattazioni: `article_types` = «Systematic Review, Meta-Analysis» per la Cochrane, «Meta-Analysis, Review» per la 2023 → nessuna ritrattazione: **superato**.
- Post-pubblicazione: PubPeer non accessibile → **non verificato**.
- Rivista: Cochrane Database of Systematic Reviews e BMC Public Health, entrambe MEDLINE → **superato**.
- Conflitti: solo abstract → **non verificato**. Nota: le due sintesi condividono gli autori (Hemilä, Chalker): non sono replicazioni indipendenti.
- Protocollo: Cochrane, protocollo pubblicato → superato per costruzione.
- Attualità: la ricerca della Cochrane è aggiornata a novembre 2012 (13 anni); esiste una meta-analisi del 2023 sulla gravità, stesso gruppo; non è stata cercata la presenza di RCT successivi al 2012 (limite dichiarato).
- Coerenza numeri: gli abstract sono internamente coerenti → superato.

### Fase 5 — Certezza
L'abstract Cochrane 2013 non riporta giudizi GRADE per outcome → **valutazione indicativa dell'assistente**, per outcome:
- Incidenza, popolazione generale (29 confronti, 11.306 partecipanti; sottogruppo generale 10.708): meta-analisi di RCT, campione ampio, IC stretto attorno al nullo, «la maggior parte degli studi randomizzati in doppio cieco» → nessun declassamento evidente dai dati letti → **Alta (indicativa)** per «poca o nessuna differenza».
- Incidenza sotto sforzo fisico estremo (5 trial, 598 partecipanti): effetto grande ma pochi studi piccoli, popolazione molto particolare → declasso per imprecisione e indirettezza → **Bassa (indicativa)**.
- Durata (31 confronti, 9.745 episodi): effetto coerente ma piccolo; eterogeneità non riportata nell'abstract → **Moderata (indicativa)**, non valutabile l'incoerenza.
- Uso terapeutico (7 confronti, 3.249 episodi): «nessun effetto coerente» → **Bassa (indicativa)** per incoerenza e imprecisione.

### Fase 6 — Restituzione

### La vitamina C presa regolarmente previene il raffreddore nella popolazione generale

**Certezza dell'evidenza: ⬤⬤⬤⬤ ALTA (indicativa)** — l'abstract non riporta GRADE; valutazione dell'assistente

Che cosa dicono i dati — Secondo PubMed, la revisione Cochrane di Hemilä e Chalker (2013) trova che l'integrazione regolare **non riduce** il numero di raffreddori nella popolazione generale: RR 0,97 (IC 95% 0,94–1,00) su 10.708 partecipanti. In termini assoluti, l'abstract non riporta il rischio di base; anche assumendo che i raffreddori colpiscano la maggior parte dei partecipanti in una stagione, la riduzione sarebbe al massimo di 1–2 persone su 100, e l'intervallo include lo zero. Per chi scrive: «non previene il raffreddore» è la frase corretta.

| Voce | Contenuto |
|---|---|
| Fonte | Hemilä H, Chalker E. Cochrane Database Syst Rev 2013 — L0 — letto: abstract |
| Disegno | Meta-analisi di RCT controllati con placebo; 29 confronti, 11.306 partecipanti (10.708 nella popolazione generale) |
| Effetto relativo | RR 0,97 (IC 95% 0,94–1,00) |
| Effetto assoluto | non riportato nell'abstract (rischio di base non indicato); ordine di grandezza ≤ 2 per 100 |
| Outcome | reale (almeno un raffreddore nel periodo) · durata degli studi variabile |
| Popolazione | adulti e bambini della comunità generale, trial con ≥ 0,2 g/die |
| Motivo del livello | RCT, campione ampio, IC stretto; incoerenza e bias di pubblicazione non valutabili dall'abstract |
| Danni noti | non riportati nell'abstract |
| Controlli | Ritrattazioni: superato (PubMed) · Post-pubblicazione: non verificato · Rivista: superato · Conflitti: non verificato (solo abstract) · Protocollo: superato per costruzione · Attualità: ricerca al nov. 2012 · Coerenza numeri: superato |
| Link | https://doi.org/10.1002/14651858.CD000980.pub4 · PMID 23440782 · PMC8078152 |

### Sotto sforzo fisico estremo la vitamina C dimezza i raffreddori

**Certezza dell'evidenza: ⬤⬤◯◯ BASSA (indicativa)**

Che cosa dicono i dati — In cinque trial su 598 maratoneti, sciatori e soldati in condizioni subartiche, il RR è 0,48 (IC 95% 0,35–0,64). L'effetto è grande, ma gli studi sono pochi e piccoli e la popolazione è lontanissima dal lettore medio: potrebbe valere per chi affronta sforzi estremi, non è trasferibile alla vita quotidiana.

| Voce | Contenuto |
|---|---|
| Fonte | come sopra — L0 — abstract |
| Disegno | 5 RCT, 598 partecipanti |
| Effetto relativo | RR 0,48 (IC 95% 0,35–0,64) |
| Effetto assoluto | non riportato |
| Outcome | reale · periodi brevi di sforzo |
| Popolazione | atleti di resistenza e militari in ambienti estremi |
| Motivo del livello | declassato per imprecisione (pochi eventi) e indirettezza (popolazione) |
| Danni noti | non riportati |
| Controlli | come sopra |
| Link | come sopra |

### La vitamina C regolare accorcia un po' i raffreddori; presa all'esordio non ha effetto dimostrato

**Certezza dell'evidenza: ⬤⬤⬤◯ MODERATA (indicativa)** per la durata con uso regolare · **⬤⬤◯◯ BASSA (indicativa)** per l'uso terapeutico

Che cosa dicono i dati — Con l'uso regolare la durata si riduce dell'8% negli adulti (IC 95% 3–12%) e del 14% nei bambini (7–21%): su un raffreddore di una settimana, circa mezza giornata negli adulti e un giorno nei bambini. La gravità è ridotta; una meta-analisi del 2023 dello stesso gruppo stima −15% (IC 9–21%) sulla gravità con ≥ 1 g/die (10 trial). Presa solo all'esordio dei sintomi (7 confronti), non mostra un effetto coerente.

| Voce | Contenuto |
|---|---|
| Fonte | Hemilä & Chalker 2013 (Cochrane, L0, abstract) e Hemilä & Chalker 2023, BMC Public Health (L1, abstract) — stesso gruppo di autori |
| Disegno | 31 confronti, 9.745 episodi (durata); 10 trial, 15 confronti (gravità, 2023); 7 confronti, 3.249 episodi (terapeutico) |
| Effetto relativo | durata: −8% adulti (3–12%), −14% bambini (7–21%); gravità: −15% (9–21%) ratio of means |
| Effetto assoluto | ~0,5 giorni (adulti) e ~1 giorno (bambini) su 7 di malattia: stima dell'assistente dalla percentuale, non riportata così dalla fonte |
| Outcome | reale (giorni di malattia, gravità riferita) · surrogato per il lettore: assenze, disagio non misurati qui |
| Popolazione | adulti e bambini con integrazione regolare; l'effetto sui bambini è maggiore |
| Motivo del livello | effetto piccolo ma coerente; eterogeneità non riportata; il terapeutico è incoerente e poco studiato |
| Danni noti | non riportati nell'abstract («low cost and safety» affermati dagli autori senza dati) |
| Controlli | come sopra; Attualità: la sintesi 2023 aggiorna la gravità ma non l'incidenza |
| Link | https://doi.org/10.1002/14651858.CD000980.pub4 · https://doi.org/10.1186/s12889-023-17229-8 (PMID 38082300, PMC10712193) |

**Sintesi gerarchica** — La vitamina C non previene il raffreddore nella popolazione generale (certezza alta, indicativa). Presa regolarmente accorcia gli episodi di poco: circa mezza giornata negli adulti (certezza moderata). Presa all'esordio non ha un effetto dimostrato (certezza bassa). Solo in condizioni di sforzo fisico estremo l'evidenza, debole, suggerisce una prevenzione. Per un articolo divulgativo la frase onesta è: «non previene, forse accorcia un po'».

**Che cosa non sappiamo** — L'abstract non dà rischi di base né effetti assoluti; gli effetti avversi non sono riportati; la ricerca Cochrane è ferma al 2012 e non abbiamo verificato la presenza di RCT successivi; le due sintesi condividono gli autori; i conflitti d'interesse non sono stati letti; le segnalazioni post-pubblicazione non erano accessibili.

**Fonti** — [1] Hemilä H, Chalker E. *Vitamin C for preventing and treating the common cold.* Cochrane Database Syst Rev 2013 — L0 — abstract — https://doi.org/10.1002/14651858.CD000980.pub4 · [2] Hemilä H, Chalker E. *Vitamin C reduces the severity of common colds: a meta-analysis.* BMC Public Health 2023 — L1 — abstract — https://doi.org/10.1186/s12889-023-17229-8

**Metodo e limiti** — Ricerca: PubMed (MCP) «vitamin C common cold AND (systematic review[pt] OR meta-analysis[pt])», 19 risultati, ordinati per data. Letture: abstract di [1] e [2] via metadati. Controlli: ritrattazioni via `article_types` (superato); PubPeer, Retraction Watch, Crossref e cochranelibrary.com non accessibili (proxy di rete). Full text non consultato. Nessuna ricerca di RCT posteriori al 2012.

---

## Esempio B — GRADE dichiarato, danni, coerenza dei numeri

**Richiesta**: «I farmaci da banco per il raffreddore che combinano antistaminico e decongestionante funzionano davvero?»

Percorso: L0 via PubMed → revisione Cochrane 2022 (De Sutter, Eriksson, van Driel), PMID 35060618, abstract letto. La scheda compilata è in `formato-output.md` §9. Qui i tre passaggi didattici.

**1. Il GRADE lo dà la fonte.** L'abstract scrive «moderate certainty evidence» per l'OR di fallimento 0,31 (IC 95% 0,20–0,48) e «NNTB 3,9 (IC 3,03–5,2)». Si trascrive e si cita: nessuna valutazione propria.

**2. L'effetto assoluto si verifica con lo script.** Il rischio di base del fallimento nel gruppo placebo si ricava dal 55% di risposte favorevoli (quindi 45% di fallimenti):

```
python3 scripts/effetti.py relative --measure OR --value 0.31 --ci 0.20 0.48 --baseline 0.45
→ rischio intervento 20,2%; −24,8 pp [−30,9; −16,8]; NNTB 4,0 (IC 3,2–6,0)
```

Riproduce l'NNTB 3,9 della revisione (la lieve differenza dipende dal rischio di base pooled esatto, non riportato). Nota didattica: se invece si calcola la differenza tra 70% e 55% si ottiene 15 pp e NNT 7: numeri riferiti al «giorno finale di valutazione», un sottoinsieme diverso. Per questo si riporta **entrambi** i dati con la loro origine, senza scegliere.

**3. I danni e la coerenza.** L'abstract: «128/419 (31%) versus 100/423 (13%)». Ricalcolo:

```
python3 scripts/effetti.py table --ei 128 --ni 419 --ec 100 --nc 423
→ 30,5% vs 23,6%; +6,9 pp [+0,9; +12,9]; RR 1,29; NNTH 15
```

100/423 è 23,6%, non 13%: **incoerenza interna dell'abstract**, riportata nella riga Controlli come «Coerenza numeri: fallito» e nel testo come discrepanza da chiarire sul full text. L'OR pooled della revisione (1,58; IC 0,78–3,21; certezza moderata) è diverso dall'OR sui totali (1,42) perché la meta-analisi pesa gli studi: lo script non sostituisce la revisione, la verifica.

**Frase finale calibrata**: «Negli adulti queste combinazioni probabilmente aiutano (circa una persona su quattro in più riferisce un beneficio), al prezzo di più effetti avversi come sonnolenza; nei bambini piccoli non c'è evidenza di efficacia e la revisione ricorda l'avvertenza FDA del 2005 sulla fenilpropanolamina.»

---

## Esempio C — Modalità rapida

**Richiesta**: «È vero che il caffè disidrata?»

Fase 0: curiosità, non controversa in letteratura, nessuna pubblicazione → **modalità rapida**, dichiarata.

**Calibrazione della query** (parte istruttiva di questo esempio):
- `caffeine AND (hydration OR diuresis OR fluid balance) AND (meta-analysis[pt] OR systematic review[pt])` → 8 risultati, quasi tutti fuori tema (voce, reni neonatali, depurazione delle acque): l'espansione automatica di «hydration» e «fluid balance» ha preso tutto.
- `caffeine[Title] AND (diuresis[Title] OR diuretic[Title] OR hydration[Title] OR "fluid balance"[Title]) AND (meta-analysis OR "systematic review")` → 1 risultato: la meta-analisi cercata.

Lettura: abstract di Zhang e coll. 2015 (PMID 25154702) via metadati; `article_types` = Meta-Analysis, nessuna ritrattazione.

**Il caffè disidrata** — Certezza ⬤⬤◯◯ BASSA (indicativa) per l'affermazione così formulata; ⬤⬤⬤◯ MODERATA (indicativa) per «la caffeina aumenta un po' la diuresi acuta a riposo» · Modalità rapida: una fonte, controlli minimi.
- Dato: secondo PubMed, in 16 studi su adulti sani (28 confronti, dose mediana 300 mg) la caffeina aumenta il volume urinario di circa 109 mL (≈ +16%), SMD 0,29 (IC 95% 0,11–0,48); l'effetto **scompare con l'esercizio** (SMD 0,10; IC −0,07–0,27) ed è maggiore nelle donne (SMD 0,75) che negli uomini (0,13; IC include lo zero). Gli autori concludono per un effetto diuretico minore, che non giustifica timori di disidratazione, soprattutto prima dell'esercizio.
- Fonte: Zhang Y e coll., J Sci Med Sport 2015 — L1 — letto: abstract — https://doi.org/10.1016/j.jsams.2014.07.017 (PMC4725310)
- Limiti: dosi acute, adulti sani; il volume urinario è un surrogato dello stato di idratazione (non misurato qui); ricerca aggiornata a novembre 2013; eterogeneità presente (sottogruppi molto diversi); post-pubblicazione e conflitti non verificati; una sola fonte, non L0.
- Danni: non pertinenti/non riportati.

Frase per l'utente: «Una tazza di caffè fa urinare un po' di più nell'immediato, ma non "disidrata": l'effetto è piccolo, sparisce con l'attività fisica, e l'acqua del caffè conta comunque nel bilancio. Vuoi il protocollo completo (revisioni più recenti, misure dirette dello stato di idratazione)?»

---

## Esempio D — Quando non si può verificare

**Scenario**: nessun connettore attivo, WebFetch bloccato verso tutti i domini scientifici, WebSearch disponibile.

Cosa si può fare: cercare con `allowed_domains` sui livelli giusti e **individuare** le fonti (titoli, anni, DOI dagli URL). Cosa non si può fare: leggerle. Come si risponde:

```
**[Affermazione]** — Certezza: NON VALUTABILE in questo ambiente
- Fonti individuate (non lette): [1] Cochrane 2013, DOI …; [2] revisione 2023, DOI …
- Cosa dicono gli snippet: [una riga, etichettata «snippet del motore di ricerca, non verificato»]
- Cosa serve per verificare: aprire [1] e [2] (PubMed o editore), controllare ritrattazioni e data della ricerca
- Proposta: se incolli l'abstract o attivi il connettore PubMed, completo la scheda
```

Ciò che non va fatto: compilare la scheda con numeri «ricordati», assegnare una certezza, scrivere «nessuna ritrattazione». La risposta onesta in un ambiente cieco è una lista di fonti da aprire e una spiegazione del perché non si va oltre.
