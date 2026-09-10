# Formato di restituzione — schede, chiusura, adattamenti

Leggi questo file nella **Fase 6**. Contiene il modello completo della scheda con la guida campo per campo, la mini-scheda della modalità rapida, il trattamento dei testi con molte affermazioni, gli elementi di chiusura obbligatori e le regole di convivenza con i formati imposti dai connettori.

## Indice

1. Principi di forma
2. Scheda completa — modello e guida campo per campo
3. Mini-scheda (modalità rapida)
4. Testi con molte affermazioni
5. Elementi di chiusura
6. Convivenza con i formati dei connettori
7. Adattare la restituzione al tipo di deliverable
8. Numeri, unità, lingua
9. Una scheda compilata (esempio)
10. Checklist prima di consegnare

---

## 1. Principi di forma

- **Prosa per la sintesi, tabella per il dettaglio.** Il lettore deve capire la risposta leggendo due frasi; i numeri e i controlli stanno nella tabella per chi vuole verificare.
- **Una scheda per affermazione**, non per fonte: la stessa fonte può sostenere più affermazioni con certezze diverse.
- **Certezza in cima**, prima dei numeri: è la prima cosa che cambia il modo di leggere il resto.
- **Niente muri di elenchi puntati**: gli elenchi servono per i controlli e le fonti, non per il ragionamento.
- **Il «non so» ha lo stesso rilievo grafico del «so»**: la sezione «Che cosa non sappiamo» non è una nota a piè di pagina.

---

## 2. Scheda completa — modello

```
### [Affermazione in una riga, come la direbbe il lettore]

**Certezza dell'evidenza: ⬤⬤⬤◯ MODERATA** — [fonte del giudizio: «dichiarata dalla revisione» oppure «valutazione indicativa dell'assistente»]

Che cosa dicono i dati — [2–4 frasi in linguaggio chiaro, con i numeri assoluti e la loro
provenienza; lessico calibrato sulla certezza; una frase sui danni]

| Voce | Contenuto |
|---|---|
| Fonte | [Autori, anno, rivista/ente] — Livello [L0–L5] — [letto: abstract / full text] |
| Disegno | [Meta-analisi di k RCT, n = …; oppure RCT singolo, coorte…] |
| Effetto relativo | [RR/OR/HR/SMD con IC 95%] |
| Effetto assoluto | [rischio controllo → rischio intervento; differenza in pp o per 1000; NNT/NNH con IC] oppure «non riportato nella fonte» |
| Outcome | [reale / surrogato] · misurato con […] · follow-up [durata] |
| Popolazione | [chi, dove, quanti; limiti di trasferibilità] |
| Motivo del livello | [domini GRADE declassati o rialzati, e perché; oppure i motivi dichiarati dalla fonte] |
| Danni noti | [effetti avversi con numeri; NNH; oppure «non riportati nella fonte»] |
| Controlli | Ritrattazioni: [esito (strumento)] · Post-pubblicazione: [esito] · Rivista: [esito] · Conflitti: [esito] · Protocollo: [esito] · Attualità: [esito] · Coerenza numeri: [esito] |
| Link | [DOI come link] · [PMID/PMC] · [URL della fonte L0 se diversa] |
```

**Guida campo per campo**

- *Affermazione*: formulala come la direbbe il lettore («La vitamina C previene il raffreddore»), non come un titolo di paper. Se l'affermazione dell'utente è ambigua, sdoppiala in due schede (prevenzione vs cura).
- *Certezza*: usa il simbolo e la parola. Indica sempre se il giudizio viene dalla fonte o da te.
- *Che cosa dicono i dati*: prima l'effetto assoluto, poi il relativo; poi per chi e per quanto; poi i danni. Usa il lessico della tabella di `grade-e-efficacia.md` §11.
- *Fonte*: livello e profondità di lettura (abstract / full text) sono entrambi obbligatori: cambiano ciò che puoi dire nei controlli.
- *Effetto assoluto*: se l'hai calcolato tu (script), scrivi da quali numeri: «calcolato da OR 0,31 e rischio di base 45% del gruppo placebo».
- *Motivo del livello*: una riga per dominio; «non valutabile dai dati letti» è un valore ammesso.
- *Controlli*: sette voci, ciascuna con esito e strumento; vedi `controllo-qualita.md` §11.
- *Link*: il DOI in forma `https://doi.org/…`; per PubMed `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`.

---

## 3. Mini-scheda (modalità rapida)

```
**[Affermazione]** — Certezza ⬤⬤◯◯ BASSA (indicativa) · Modalità rapida: una fonte, controlli minimi.
- Dato: [effetto assoluto e relativo con IC, in una riga]
- Fonte: [autori anno, livello, letto: abstract] — [DOI link]
- Limiti: [una riga: popolazione, età della fonte, cosa non è stato verificato]
- Danni: [una riga o «non riportati»]
```

Quattro righe più il titolo. Se durante la modalità rapida emergono contraddizioni o l'utente rilancia, passa al protocollo completo e dillo.

---

## 4. Testi con molte affermazioni

Quando l'utente incolla un articolo, un capitolo o un post con molte affermazioni:

1. **Estrai** le affermazioni verificabili (non le opinioni) e numerale.
2. **Priorizza** con tre criteri: rilevanza per la tesi del testo, fragilità apparente (numeri tondi, «studi dimostrano», superlativi), rischio per il lettore (salute, denaro, decisioni). Le prime 5–7 ricevono la scheda completa.
3. **Le altre** vanno in una tabella riassuntiva:

```
| # | Affermazione | Certezza | Esito | Fonte |
|---|---|---|---|---|
| 8 | «…» | ⬤⬤◯◯ | ridimensionare: effetto piccolo | [1] |
| 9 | «…» | — | non verificata (fuori budget) | — |
```

4. Dichiara il tetto: «verificate in dettaglio 6 affermazioni su 14; le restanti sono in tabella con esito sommario o non verificate».

Esiti sommari ammessi: *confermata*, *confermata con riserva*, *ridimensionare*, *smentita*, *non verificabile*, *non verificata (fuori budget)*.

---

## 5. Elementi di chiusura

Ogni risposta in protocollo completo termina con quattro blocchi, in quest'ordine:

1. **Sintesi gerarchica** — la risposta in 3–6 frasi, con la certezza globale. La certezza globale è quella dell'outcome che conta di più per il quesito, **non una media**: se la mortalità ha certezza Alta e la qualità di vita Molto bassa, dì entrambe. Se due fonti L0 divergono, riportale entrambe con data e metodo, e spiega da cosa dipende la divergenza (popolazione, data della ricerca, criteri di inclusione).
2. **Che cosa non sappiamo** — lacune dell'evidenza (outcome non studiati, popolazioni escluse, follow-up brevi), contraddizioni aperte, e ciò che *tu* non hai potuto verificare. Mai facoltativa, mai una riga sola di cortesia.
3. **Fonti** — elenco numerato; per ciascuna: autori/ente, anno, livello gerarchico, cosa hai letto (abstract/full text), link cliccabile. Le fonti solo «individuate ma non lette» vanno in un sotto-elenco separato «Da approfondire», mai mescolate.
4. **Metodo e limiti** — 3–6 righe: query eseguite con strumento e numero di risultati; letture; controlli eseguiti e non; blocchi incontrati; budget speso. Formato in `strumenti-e-fallback.md` §10.

Chiudi con **una** frase di responsabilità quando il tema è clinico: «Queste informazioni riassumono l'evidenza disponibile e non sostituiscono la valutazione di un professionista che conosce il caso.» Una frase, non un paragrafo di avvertenze.

---

## 6. Convivenza con i formati dei connettori

Alcuni connettori impongono obblighi di attribuzione. Si **integrano** nella struttura della scheda, non la sostituiscono:

| Connettore | Obbligo | Dove finisce |
|---|---|---|
| PubMed MCP | dichiarare l'uso («secondo PubMed…») e linkare il DOI di ogni articolo | frase di attribuzione nella Sintesi o nel Metodo; DOI nella riga Link e nell'elenco Fonti |
| Consensus MCP | citazioni numerate inline `[n]`, elenco finale con link esatti, messaggio finale riportato parola per parola | i numeri coincidono con l'elenco Fonti; il messaggio va dopo «Metodo e limiti» |
| WebSearch | elenco «Sources» con i link usati | coincide con l'elenco Fonti (non duplicarlo) |

Se due obblighi chiedono numerazioni diverse, usa **una sola numerazione** (quella dell'elenco Fonti) e mappa le altre in nota.

---

## 7. Adattare la restituzione al deliverable

| Deliverable | Cosa cambia |
|---|---|
| Risposta in chat a un quesito | Scheda/e + chiusura, come sopra |
| Verifica di un testo dell'utente | Tabella delle affermazioni (§4) + schede prioritarie + suggerimenti di riformulazione calibrata («da "è dimostrato" a "probabilmente"») |
| Bozza per un articolo divulgativo | La prosa calibrata va nel testo; i numeri assoluti nel testo; le schede diventano note o un box «Le prove»; le fonti in bibliografia con link |
| Documento clinico o formativo | Schede complete in appendice; tabella riassuntiva nel corpo; certezza e forza delle raccomandazioni sempre distinte |
| Contenuto giornalistico | Link inline alla fonte primaria (non al comunicato stampa); ogni numero con la sua fonte nella stessa frase |

Quando la skill è chiamata da un'altra skill (per esempio `scrittura-di-valore`), consegna le schede e la chiusura come blocco riutilizzabile: la skill chiamante decide dove metterle.

---

## 8. Numeri, unità, lingua

- Nelle tabelle riporta i numeri **come nella fonte** (punto decimale, stesse cifre significative); nella prosa italiana puoi usare la virgola decimale, ma non mescolare le due convenzioni nella stessa frase.
- Le differenze assolute si esprimono in **punti percentuali** (pp) o **per 1000**; mai «% in meno» senza specificare se relativo o assoluto.
- Ogni numero porta unità, popolazione e tempo: «−8% della durata (IC 95% 3–12%), adulti, sui giorni di malattia per episodio».
- Termini tecnici in inglese tra parentesi la prima volta se aiutano a ritrovare la fonte («rischio relativo (risk ratio, RR)»).
- Rispondi nella lingua dell'utente; le query e le citazioni restano nella lingua originale.

---

## 9. Una scheda compilata

Dalla revisione Cochrane 2022 sulle combinazioni antistaminico-decongestionante per il raffreddore (De Sutter e coll.), letta via abstract PubMed. Numeri reali; vedi `esempi-svolti.md`, Esempio B, per il percorso completo.

```
### Le combinazioni antistaminico + decongestionante da banco riducono i sintomi del raffreddore negli adulti

**Certezza dell'evidenza: ⬤⬤⬤◯ MODERATA** — dichiarata dalla revisione (GRADE)

Che cosa dicono i dati — Negli adulti, la combinazione probabilmente aumenta la quota di persone
che riferiscono un beneficio complessivo: circa 25 persone in più ogni 100 trattate (NNTB 4,
calcolato dall'OR 0,31 con rischio di fallimento del 45% nel gruppo placebo; la revisione riporta
NNTB 3,9). Il prezzo: più effetti avversi (sonnolenza, secchezza), con una stima imprecisa.
Nessuna evidenza di beneficio nei bambini piccoli.

| Voce | Contenuto |
|---|---|
| Fonte | De Sutter, Eriksson, van Driel 2022, Cochrane Database Syst Rev — L0 — letto: abstract |
| Disegno | Revisione sistematica; per questo confronto 6 studi pooled, 281 vs 284 partecipanti |
| Effetto relativo | OR di fallimento del trattamento 0,31 (IC 95% 0,20–0,48) |
| Effetto assoluto | risposta favorevole 55% con placebo → 70% con trattamento (giorno finale, 3–10 gg); NNTB 3,9 (IC 3,03–5,2) dichiarato; script: −24,8 pp [−30,9; −16,8] da OR e rischio di base 45% |
| Outcome | reale (beneficio globale riferito) · follow-up 3–10 giorni |
| Popolazione | adulti con raffreddore, ambulatori e cliniche universitarie; bambini: nessuna evidenza di efficacia |
| Motivo del livello | dichiarato «moderate certainty»; motivi non dettagliati nell'abstract (probabile imprecisione e rischio di bias: «reporting of methods was generally poor») |
| Danni noti | effetti avversi 128/419 vs 100/423 (30,5% vs 23,6% ricalcolati; l'abstract scrive «13%»: incoerenza segnalata); OR pooled 1,58 (IC 0,78–3,21), certezza moderata |
| Controlli | Ritrattazioni: superato (PubMed article_types) · Post-pubblicazione: non verificato (PubPeer non accessibile) · Rivista: superato (Cochrane/MEDLINE) · Conflitti: non verificato (solo abstract) · Protocollo: superato per costruzione (Cochrane) · Attualità: ricerca al giugno 2021, 5 anni · Coerenza numeri: **fallito** sulla percentuale degli effetti avversi nel gruppo placebo |
| Link | https://doi.org/10.1002/14651858.CD004976.pub4 · PMID 35060618 · PMC8780136 |
```

---

## 10. Checklist prima di consegnare

- [ ] Ho dichiarato la modalità (rapida/completa)?
- [ ] Ogni numero citato viene da una fonte che ho aperto (non da uno snippet)?
- [ ] Ogni effetto relativo ha l'assoluto, o la dicitura «non riportato nella fonte»?
- [ ] La certezza è dichiarata, con la sua origine (fonte / indicativa)?
- [ ] Il lessico è calibrato sulla certezza?
- [ ] I danni sono riportati o dichiarati non riportati?
- [ ] La riga Controlli ha sette voci con esito e strumento, e nessun esito simulato?
- [ ] «Che cosa non sappiamo» esiste ed è sostanziale?
- [ ] Le fonti hanno livello, profondità di lettura e link?
- [ ] La nota «Metodo e limiti» permette di rifare la ricerca?
