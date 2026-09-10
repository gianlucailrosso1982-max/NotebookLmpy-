# GRADE ed efficacia reale — riferimento esteso

Leggi questo file nella **Fase 5** (valutazione della certezza) e ogni volta che devi trasformare un effetto relativo in un effetto assoluto, giudicare la rilevanza clinica di un risultato, o scegliere le parole con cui riportarlo.

## Indice

1. Certezza: cosa misura e cosa no
2. Livello di partenza per disegno
3. I cinque motivi di declassamento, con criteri operativi
4. I tre motivi di rialzo
5. Leggere il GRADE già dichiarato dalla fonte
6. Valutazione indicativa propria: procedura e limiti
7. Effetti assoluti: formule, rischio di base, script
8. Outcome continui: MD, SMD, ratio of means e MCID
9. Outcome surrogati e outcome che contano
10. Danni: come riportarli
11. Il lessico calibrato sulla certezza
12. Trappole frequenti
13. Causalità negli studi osservazionali

---

## 1. Certezza: cosa misura e cosa no

La certezza GRADE esprime **quanto siamo fiduciosi che la stima dell'effetto sia adeguata a sostenere una conclusione**. Non misura la grandezza dell'effetto (un effetto minuscolo può avere certezza Alta), né la qualità della rivista, né l'autorevolezza degli autori. È specifica per **ogni outcome**: la stessa revisione può avere certezza Alta sulla mortalità e Molto bassa sulla qualità di vita.

Quattro livelli:

| Simbolo | Livello | Significato | Come si scrive |
|---|---|---|---|
| ⬤⬤⬤⬤ | Alta | L'effetto vero è molto probabilmente vicino alla stima | «riduce», «aumenta», «produce poca o nessuna differenza» |
| ⬤⬤⬤◯ | Moderata | Probabilmente vicino, ma potrebbe differire in modo sostanziale | «probabilmente riduce…» |
| ⬤⬤◯◯ | Bassa | Fiducia limitata: l'effetto vero può essere sostanzialmente diverso | «potrebbe ridurre…», «l'evidenza suggerisce…» |
| ⬤◯◯◯ | Molto bassa | Fiducia minima | «non è chiaro se…», «l'evidenza è molto incerta» |

---

## 2. Livello di partenza per disegno

| Disegno | Certezza iniziale |
|---|---|
| Revisione sistematica / meta-analisi di RCT | Alta (poi si applicano i declassamenti alla stima pooled) |
| RCT singolo | Alta |
| Studio osservazionale (coorte, caso-controllo, registro) | Bassa |
| Studio trasversale, serie di casi | Molto bassa |
| Caso singolo, opinione di esperti, consenso non sistematico | Molto bassa |
| Pre-clinico (in vitro, animale, modellistico) | Molto bassa per conclusioni sull'uomo |
| Preprint | Bassa se sperimentale, Molto bassa se osservazionale (coerente con L5) |
| Revisione sistematica di studi osservazionali | Bassa (parte dal disegno degli studi inclusi, non dalla revisione) |

Una revisione sistematica non «alza» la certezza dei suoi studi: la sintetizza. Una meta-analisi di studi osservazionali parte da Bassa.

---

## 3. I cinque motivi di declassamento

Ogni motivo abbassa di uno o due gradini. Per ciascuno: cosa cercare, cosa si vede dall'abstract, cosa richiede il full text.

### 3.1 Rischio di bias
- **Cosa cercare**: randomizzazione e occultamento dell'allocazione; cecità di partecipanti, operatori e valutatori; abbandoni sbilanciati o > 20%; outcome cambiati rispetto al protocollo; analisi non intention-to-treat; interruzione precoce per beneficio.
- **Dall'abstract**: spesso solo «double-blind, placebo-controlled»; le revisioni Cochrane dichiarano nell'abstract il giudizio di rischio di bias complessivo.
- **Serve il full text**: la tabella RoB 2 / ROBINS-I, i flussi CONSORT, il confronto col protocollo.
- Declassa di 1 se la maggior parte dell'evidenza viene da studi ad alto rischio; di 2 se il rischio è grave e pervasivo.

### 3.2 Incoerenza (eterogeneità)
- **Cosa cercare**: stime puntuali che vanno in direzioni opposte; intervalli di confidenza che non si sovrappongono; I² alto (Cochrane: 30–60% moderata, 50–90% sostanziale, 75–100% considerevole); test di eterogeneità con p < 0,10; sottogruppi con effetti molto diversi senza spiegazione.
- **Dall'abstract**: talvolta l'I²; più spesso «substantial heterogeneity».
- Non declassare per eterogeneità se la direzione è coerente e varia solo la grandezza, purché tutte le stime superino la soglia di importanza.

### 3.3 Indirettezza
- **Cosa cercare**: popolazione diversa da quella del quesito (età, gravità, contesto), intervento diverso (dose, durata, formato), confronto diverso (placebo invece di trattamento attivo), outcome surrogato invece di quello che conta, confronto indiretto tra trattamenti mai confrontati testa a testa.
- **Dall'abstract**: quasi sempre valutabile, perché popolazione e outcome sono dichiarati.
- Esempio: trial su atleti sotto sforzo estremo → indiretti per la popolazione generale (vedi l'esempio svolto sulla vitamina C).

### 3.4 Imprecisione
- **Cosa cercare**: intervallo di confidenza che include sia un beneficio rilevante sia un danno rilevante (regola pratica per gli outcome dicotomici: l'IC del RR attraversa 0,75 e/o 1,25); pochi eventi (< 300–400 in totale per un outcome dicotomico è il segnale classico di «optimal information size» non raggiunta); campione piccolo per un outcome continuo (< 400 partecipanti, con l'IC che attraversa la MCID).
- **Dall'abstract**: sì, se riporta IC e numeri.
- Un IC stretto attorno a un effetto nullo **non** è imprecisione: è certezza di un effetto piccolo o assente.

### 3.5 Bias di pubblicazione
- **Cosa cercare**: solo studi piccoli e positivi; asimmetria del funnel plot (valutabile solo con ≥ 10 studi); tutti gli studi finanziati dall'industria; studi registrati e mai pubblicati; revisioni che non hanno cercato la letteratura grigia o i registri.
- **Dall'abstract**: raramente; le revisioni Cochrane lo dichiarano quando sospettato.
- Declassa di 1 quando il sospetto è fondato; non declassare «per principio».

---

## 4. I tre motivi di rialzo (solo studi osservazionali, e solo se non già declassati)

1. **Effetto grande**: RR > 2 o < 0,5 (+1); RR > 5 o < 0,2 (+2), purché coerente tra studi e senza confondimento plausibile che lo spieghi.
2. **Gradiente dose-risposta**: più esposizione, più effetto (+1).
3. **Confondimento residuo che va nella direzione opposta**: tutti i confondenti plausibili ridurrebbero l'effetto, eppure l'effetto persiste (+1).

Esempi classici di certezza alta da studi osservazionali: fumo e cancro del polmone (effetto enorme, dose-risposta), insulina nel diabete di tipo 1.

---

## 5. Leggere il GRADE già dichiarato dalla fonte

Quando la fonte L0 riporta la certezza, **usa quella e citala**: è il giudizio di un panel che ha letto i full text, cosa che tu spesso non puoi fare.

**Tabella Summary of Findings (Cochrane, linee guida GRADE)** — colonne tipiche:

| Colonna | Cosa contiene | Dove va nella scheda |
|---|---|---|
| Outcome | esito, strumento, tempo di follow-up | riga Outcome |
| Rischio assunto (con controllo) | rischio di base, es. 450 per 1000 | serve per l'effetto assoluto |
| Rischio corrispondente (con intervento) | es. 202 per 1000 (da 141 a 282) | riga Effetto (assoluto) |
| Effetto relativo | RR/OR/HR con IC 95% | riga Effetto (relativo) |
| Partecipanti (studi) | n (k) | riga Disegno |
| Certezza | ⊕⊕⊕◯ con i motivi in nota | riga Certezza e Motivo del livello |
| Commenti | note del panel | Motivo del livello |

Nell'abstract Cochrane le certezze compaiono come «high-certainty evidence», «moderate-certainty», «low-certainty», «very low-certainty» accanto a ciascun risultato: trascrivile.

**Linee guida**: distingui sempre la **certezza dell'evidenza** dalla **forza della raccomandazione** (forte/debole o condizionale). Una raccomandazione forte può poggiare su certezza moderata (quando i benefici superano nettamente i danni) e una debole su certezza alta (quando il bilancio dipende dai valori della persona). Riporta entrambe.

**Altri sistemi**: USPSTF (A/B/C/D/I: A e B = beneficio netto da moderato a sostanziale, I = insufficiente); Oxford CEBM (livelli 1–5); SIGN (1++, 1+, 2++…); IPCC (linguaggio di probabilità e di confidenza). Non convertirli meccanicamente in GRADE: riporta il sistema originale e, se ti serve una mappatura, dichiara che è approssimativa.

---

## 6. Valutazione indicativa propria

Solo quando nessuna sintesi valutata esiste. Procedura:

1. Parti dal livello del disegno (§2).
2. Passa in rassegna i cinque motivi (§3) segnando per ciascuno: «declasso di 1/2 perché…», «non declasso perché…», oppure «**non valutabile dai dati letti**».
3. Applica i rialzi (§4) solo se osservazionale.
4. Scrivi il livello con l'etichetta obbligatoria: «valutazione indicativa dell'assistente, non un GRADE formale» e i motivi in una riga.

Non fingere di aver valutato un dominio che non hai potuto vedere. «Bias di pubblicazione: non valutabile (funnel plot non riportato nell'abstract)» è una frase corretta; «bias di pubblicazione: non sospettato» senza aver visto nulla non lo è.

---

## 7. Effetti assoluti: formule, rischio di base, script

Il rischio relativo senza il rischio di base è un numero vuoto. Formule:

- **ARR** (riduzione assoluta) = rischio controllo − rischio intervento. **NNT** = 1 / ARR.
- Da **RR** e rischio di base p₀: rischio intervento = p₀ × RR.
- Da **OR** e p₀: rischio intervento = (OR × p₀) / (1 − p₀ + OR × p₀). Con p₀ > 20%, OR e RR divergono molto: mai leggere un OR come «riduzione percentuale del rischio».
- Da **HR** e p₀ (a un orizzonte definito): rischio intervento = 1 − (1 − p₀)^HR.
- Applica la stessa trasformazione agli estremi dell'IC per ottenere l'IC dell'effetto assoluto (è ciò che fanno le SoF).
- **NNT e IC**: se l'IC della differenza include lo zero, l'IC dell'NNT passa per l'infinito (Altman 1998): scrivi «NNTB 8 (IC da NNTB 4 a ∞ a NNTH 50)», non un intervallo finito inventato.
- Arrotonda l'NNT a numero intero nel testo (per prudenza, per eccesso).

**Il rischio di base va dichiarato**: viene dal gruppo di controllo della revisione (SoF «rischio assunto»), da un registro o statistica L4, o dalla popolazione dell'utente. Cambiare rischio di base cambia l'NNT: NNT 4 con rischio di base 45% diventa NNT 40 con rischio di base 4,5%.

**Usa lo script**: `scripts/effetti.py` esegue questi calcoli con IC e ti dice come leggere il segno. Esempi verificati sulla revisione Cochrane 2022 sui farmaci combinati per il raffreddore (De Sutter e coll.):

```
python3 scripts/effetti.py relative --measure OR --value 0.31 --ci 0.20 0.48 --baseline 0.45
# → rischio intervento 20,2%; differenza −24,8 pp [−30,9; −16,8]; NNTB 4,0 (IC 3,2–6,0)
#   La revisione riporta NNTB 3,9 (IC 3,03–5,2): lo script riproduce l'ordine di grandezza; la
#   differenza dipende dal rischio di base esatto usato dagli autori (pooled), non riportato nell'abstract.

python3 scripts/effetti.py table --ei 128 --ni 419 --ec 100 --nc 423
# → rischio 30,5% vs 23,6%; +6,9 pp [+0,9; +12,9]; RR 1,29; OR 1,42; NNTH 15
#   L'abstract scrive «128/419 (31%) versus 100/423 (13%)»: 100/423 è 23,6%, non 13%. Segnala
#   l'incoerenza, non scegliere. E ricorda: OR pooled della revisione = 1,58 (0,78–3,21): sommare
#   gli eventi di più studi NON riproduce la meta-analisi.
```

Quando la fonte dà solo l'effetto relativo e nessun rischio di base: scrivi «effetto assoluto non riportato nella fonte» e, se vuoi dare un ordine di grandezza, calcolalo **dichiarando** il rischio di base assunto e la sua provenienza («assumendo il 30% di raffreddori/anno nella popolazione generale, fonte…»). Mai un numero assoluto senza la sua origine.

Presentazione consigliata (stile GRADE): «per 1000 persone: 450 con placebo, 202 con il trattamento (da 141 a 282); 248 in meno».

---

## 8. Outcome continui: MD, SMD, ratio of means e MCID

- **MD** nell'unità originale: confrontala con la MCID dello strumento. Esempio: −2 punti su una scala 0–10 del dolore, con MCID ≈ 1,5–2: al limite della rilevanza.
- **SMD** (d di Cohen, g di Hedges): 0,2 piccolo, 0,5 medio, 0,8 grande **per convenzione**; in psicoterapia una SMD di 0,3–0,5 contro il trattamento abituale è tipica e rilevante; in farmacologia 0,3 può essere sotto la MCID. Riconverti in unità della scala quando puoi (SMD × DS del gruppo di controllo). Lo script (`effetti.py smd`) dà anche la «probabilità di superiorità» e un OR approssimato.
- **Ratio of means**: 0,92 = −8%. Chiedi: −8% di cosa? Su un raffreddore di 7 giorni sono ~13 ore.
- **Valori orientativi di MCID** (spesso citati; verificali per lo strumento e la popolazione specifici): dolore su VAS 0–100 mm ≈ 10–20 mm; PHQ-9 ≈ 5 punti; HbA1c ≈ 0,5 punti percentuali; test del cammino 6 minuti ≈ 30 m; scale di qualità di vita SF-36 ≈ 3–5 punti per dominio. Se non conosci la MCID, dillo: «MCID non nota all'assistente per questo strumento».

---

## 9. Outcome surrogati e outcome che contano

| Surrogato | Outcome che conta | Perché non basta |
|---|---|---|
| Colesterolo LDL | Infarto, ictus, mortalità | Molecole che abbassano l'LDL senza ridurre gli eventi sono esistite |
| HbA1c | Complicanze, mortalità | Abbassamenti intensivi hanno aumentato la mortalità in alcuni trial |
| Densità ossea | Fratture | Il fluoro aumentava la densità e le fratture |
| Sopravvivenza libera da progressione | Sopravvivenza globale, qualità di vita | La correlazione con la sopravvivenza globale è variabile |
| Punteggio a un questionario di sintomi | Funzionamento, ricadute, qualità di vita | Miglioramenti soggettivi sotto la MCID |
| Marcatori infiammatori, ormoni | Esiti clinici | Meccanismo ≠ beneficio |
| Performance a un test cognitivo di laboratorio | Funzionamento nella vita reale | Effetti di allenamento specifici del test |

Segnala sempre quando l'outcome è surrogato e declassa per indirettezza se il quesito riguarda l'esito clinico.

---

## 10. Danni: come riportarli

- Ogni scheda ha la riga «Danni noti»: effetti avversi con frequenza assoluta nei due gruppi, NNH se calcolabile; «non riportati nello studio» quando è così; «riportati come assenti» solo se lo studio lo dichiara esplicitamente.
- I danni sono di norma misurati peggio dei benefici (follow-up brevi, definizioni vaghe, campioni sottodimensionati): la certezza sui danni è spesso più bassa e va detto.
- Danni rari o tardivi non emergono dagli RCT: integra con farmacovigilanza (EMA, FDA, AIFA) e coorti.
- Riporta anche il costo, il carico per la persona e le alternative quando l'utente deve decidere.

---

## 11. Il lessico calibrato sulla certezza

Segui le «informative statements» adottate da Cochrane: la frase incorpora sia la certezza sia la grandezza.

| Certezza | Effetto importante | Effetto piccolo / trascurabile | Nessuna differenza |
|---|---|---|---|
| Alta | «riduce di molto…» / «riduce…» | «riduce di poco…» | «produce poca o nessuna differenza» |
| Moderata | «probabilmente riduce…» | «probabilmente riduce di poco…» | «probabilmente produce poca o nessuna differenza» |
| Bassa | «potrebbe ridurre…» | «potrebbe ridurre di poco…» | «potrebbe produrre poca o nessuna differenza» |
| Molto bassa | «non è chiaro se…» / «l'evidenza è molto incerta sull'effetto di…» | idem | idem |

Frasi da evitare: «è dimostrato che» con certezza < Alta; «non funziona» quando l'evidenza è assente (l'assenza di evidenza non è evidenza di assenza); «significativo» senza specificare se statistico o clinico; «sicuro» quando i danni non sono stati misurati.

---

## 12. Trappole frequenti

1. Relativo senza assoluto.
2. OR letto come RR con eventi frequenti.
3. Significatività statistica scambiata per rilevanza.
4. Sottogruppo «positivo» estratto da uno studio globalmente negativo.
5. Outcome composito guidato dal componente meno importante.
6. Analisi per-protocol presentata come principale.
7. Interruzione precoce del trial per beneficio (sovrastima).
8. Run-in che elimina i non-responder prima della randomizzazione.
9. Confronto con placebo quando esiste un trattamento attivo efficace.
10. Dose o durata dello studio non trasferibili alla pratica.
11. Effetto misurato subito dopo l'intervento, senza follow-up.
12. Stesso gruppo di autori che «conferma» i propri risultati: non è replicazione indipendente.
13. Meta-analisi che include studi ritrattati o duplicati.
14. Studio pre-clinico presentato come prova nell'uomo.
15. Correlazione temporale o ecologica presentata come causa.

---

## 13. Causalità negli studi osservazionali

Quando la domanda è «X causa Y?» e non esistono RCT (spesso per ragioni etiche o pratiche), usa i criteri di Bradford Hill come griglia di ragionamento, non come checklist da sommare: forza dell'associazione, coerenza tra studi e popolazioni, specificità, temporalità (la causa precede l'effetto: l'unico criterio necessario), gradiente dose-risposta, plausibilità biologica, coerenza con le conoscenze, evidenza sperimentale (anche naturale: randomizzazione mendeliana, esperimenti naturali), analogia. Cerca la **triangolazione**: disegni diversi con bias diversi che convergono sulla stessa conclusione valgono più di dieci studi con lo stesso bias. Dichiara sempre i confondenti plausibili non controllati e la possibilità di causalità inversa.
