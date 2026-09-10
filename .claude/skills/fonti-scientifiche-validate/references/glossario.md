# Glossario operativo

Definizioni brevi dei termini usati nella skill, pensate per chi deve *leggere* uno studio, non per chi deve condurlo. Quando un termine compare in una scheda, usa la definizione qui sotto per spiegarlo al lettore se il contesto è divulgativo.

## Misure di effetto

| Termine | Definizione operativa | Come leggerlo |
|---|---|---|
| **RR — rischio relativo** | Rapporto tra la probabilità dell'evento nel gruppo intervento e quella nel gruppo controllo. | RR 0,5 = rischio dimezzato *in proporzione*; da solo non dice quanto sia grande il rischio di partenza. |
| **OR — odds ratio** | Rapporto tra le *odds* (evento / non-evento) nei due gruppi. Tipico di studi caso-controllo, regressioni logistiche e molte meta-analisi. | Con eventi rari (< 10%) OR ≈ RR; con eventi frequenti l'OR esagera: OR 0,31 non significa «rischio ridotto del 69%». |
| **HR — hazard ratio** | Rapporto istantaneo dei tassi di evento nel tempo (analisi di sopravvivenza). | HR 0,8 = a ogni istante il gruppo trattato ha un tasso di evento inferiore del 20%; si legge insieme all'orizzonte temporale. |
| **ARR / ARI — riduzione (o aumento) assoluto del rischio** | Differenza tra le probabilità dell'evento nei due gruppi, in punti percentuali. | È il numero che conta per la persona: «2 casi in meno ogni 100 trattati». |
| **NNT / NNTB** | Number Needed to Treat (to Benefit): 1 / ARR. Persone da trattare perché *una in più* tragga beneficio. | NNT 7 = su 7 trattati, uno beneficia grazie al trattamento; gli altri 6 avrebbero avuto lo stesso esito comunque. |
| **NNH / NNTH** | Number Needed to Harm: 1 / ARI. Persone da trattare perché *una in più* subisca un danno. | Va sempre accanto all'NNT: NNT 7 con NNH 15 è un profilo molto diverso da NNT 7 con NNH 200. |
| **MD — differenza media** | Differenza tra le medie di un outcome continuo, nell'unità originale (mm di scala del dolore, kg, punti di un questionario). | Confrontala con la MCID. |
| **SMD — differenza media standardizzata** (d di Cohen, g di Hedges) | MD divisa per la deviazione standard: rende confrontabili scale diverse. | Convenzione: 0,2 piccolo, 0,5 medio, 0,8 grande — ma dipende dal campo. |
| **Ratio of means** | Rapporto tra le medie nei due gruppi (es. durata dei sintomi). | 0,92 = durata ridotta dell'8%. |
| **MCID — differenza minima clinicamente importante** | La più piccola variazione che la persona percepisce come rilevante. | Un effetto statisticamente significativo ma sotto la MCID è, per la persona, nullo. |
| **IC 95% — intervallo di confidenza** | Intervallo di valori compatibili con i dati; se ripetessimo lo studio molte volte, il 95% degli intervalli conterrebbe il valore vero. | Guarda gli estremi: se includono sia un beneficio rilevante sia un danno, la stima è imprecisa. |
| **p-value** | Probabilità di osservare dati almeno così estremi se l'effetto vero fosse nullo. | Non misura la grandezza né l'importanza dell'effetto. Un p < 0,05 con effetto minuscolo è irrilevante. |
| **Significatività statistica vs rilevanza clinica** | La prima riguarda l'incertezza sul numero, la seconda l'importanza del numero. | Vanno sempre giudicate separatamente. |

## Disegni di studio

| Termine | Definizione | Cosa può dimostrare |
|---|---|---|
| **RCT — studio randomizzato controllato** | I partecipanti sono assegnati a caso ai gruppi; idealmente in cieco. | Nesso causale tra intervento e outcome (se ben condotto). |
| **Revisione sistematica** | Ricerca esaustiva, riproducibile e pre-registrata di tutti gli studi su un quesito, con valutazione del rischio di bias. | Il quadro complessivo dell'evidenza, incluse le contraddizioni. |
| **Meta-analisi** | Combinazione statistica dei risultati di più studi in una stima pooled. | Precisione maggiore; ma «pooled» non significa «vero» se gli studi sono distorti. |
| **Revisione narrativa** | Sintesi non sistematica, spesso di esperti. | Orientamento; non prova. |
| **Studio di coorte** | Si seguono nel tempo gruppi esposti e non esposti. | Associazioni; causalità solo con cautela (confondimento). |
| **Studio caso-controllo** | Si parte dai casi (con l'esito) e si cercano le esposizioni passate. | Associazioni, utili per esiti rari; soggetto a bias di ricordo e selezione. |
| **Studio trasversale** | Fotografia in un solo momento. | Prevalenze, correlazioni; nessuna direzione causale. |
| **Serie di casi / caso clinico** | Descrizione senza gruppo di confronto. | Segnalazione; nessuna stima di efficacia. |
| **Studio pre-clinico** | In vitro, su animali, modelli computazionali. | Meccanismi plausibili; non trasferibile all'uomo senza studi clinici. |
| **N-of-1** | Sperimentazione crossover ripetuta su un singolo individuo. | Effetto in *quella* persona. |
| **Studio pragmatico vs esplicativo** | Pragmatico: condizioni reali; esplicativo: condizioni ideali. | Il pragmatico dice se funziona in pratica, l'esplicativo se *può* funzionare. |

## Bias e qualità

| Termine | Definizione |
|---|---|
| **Rischio di bias** | Probabilità che il disegno o la conduzione dello studio abbiano distorto il risultato in modo sistematico. Strumenti: RoB 2 (RCT), ROBINS-I (osservazionali), AMSTAR 2 (revisioni), AGREE II (linee guida). |
| **Cecità (blinding)** | Partecipanti, operatori e valutatori non sanno chi riceve cosa. La sua assenza gonfia gli effetti soggettivi. |
| **Intention-to-treat (ITT)** | Analisi di tutti i randomizzati nel gruppo assegnato, anche se non hanno completato il trattamento. Protegge la randomizzazione. |
| **Per-protocol** | Analisi dei soli aderenti. Tende a sovrastimare l'efficacia. |
| **Attrition (abbandoni)** | Partecipanti persi al follow-up; se sbilanciati tra i gruppi distorcono il risultato. |
| **Outcome switching** | Cambiare l'outcome primario dopo aver visto i dati. Si scopre confrontando la pubblicazione con il registro. |
| **Bias di pubblicazione** | Gli studi positivi vengono pubblicati più spesso di quelli negativi: la letteratura appare più favorevole della realtà. |
| **Small-study effects** | Gli studi piccoli mostrano effetti maggiori (asimmetria del funnel plot). |
| **Eterogeneità (I²)** | Quota di variabilità tra studi non attribuibile al caso. 0–40% modesta, 30–60% moderata, 50–90% sostanziale, 75–100% considerevole (Cochrane Handbook). |
| **Confondimento** | Una terza variabile legata sia all'esposizione sia all'esito produce un'associazione spuria. |
| **Causalità inversa** | È l'esito a causare l'esposizione, non viceversa. |
| **Outcome surrogato** | Marcatore intermedio (LDL, HbA1c, densità ossea) al posto dell'esito che conta (infarto, complicanze, fratture). |
| **Outcome composito** | Più esiti aggregati; può nascondere che l'effetto è guidato dal componente meno importante. |
| **Analisi per sottogruppi** | Risultati in fette della popolazione; con molte fette, qualcuna «significativa» emerge per caso. |
| **Regressione verso la media** | Valori estremi tendono a normalizzarsi da soli: senza controllo, un miglioramento può essere spontaneo. |
| **Effetto placebo / Hawthorne** | Miglioramento dovuto all'aspettativa o all'essere osservati. |
| **Replicazione** | Ripetizione indipendente dello studio. Un risultato non replicato è un'ipotesi, non un fatto. |
| **Rivista predatoria** | Rivista che incassa tariffe di pubblicazione senza peer review reale. |
| **Ritrattazione / expression of concern / erratum** | Ritiro formale dell'articolo; avviso di dubbi seri; correzione di errori che non invalidano il lavoro. |

## Sistemi di valutazione

| Sigla | Cos'è |
|---|---|
| **GRADE** | Grading of Recommendations Assessment, Development and Evaluation: certezza dell'evidenza in quattro livelli (Alta, Moderata, Bassa, Molto bassa) e forza delle raccomandazioni (forte/debole). |
| **Summary of Findings (SoF)** | Tabella GRADE che riporta, per ogni outcome: rischio assunto, rischio corrispondente, effetto relativo, partecipanti (studi), certezza, commenti. |
| **PICO** | Popolazione, Intervento, Confronto, Outcome: struttura del quesito clinico. |
| **PRISMA** | Standard di rendicontazione delle revisioni sistematiche (diagramma di flusso, checklist). |
| **CONSORT** | Standard di rendicontazione degli RCT. |
| **STROBE** | Standard di rendicontazione degli studi osservazionali. |
| **AMSTAR 2** | Checklist per giudicare la qualità di una revisione sistematica (16 item, 7 critici). |
| **AGREE II** | Strumento per giudicare la qualità di una linea guida (6 domini, 23 item). |
| **RoB 2 / ROBINS-I** | Strumenti Cochrane per il rischio di bias in RCT / studi non randomizzati. |
| **Criteri di Bradford Hill** | Nove considerazioni per giudicare la causalità in studi osservazionali (forza, coerenza, temporalità, gradiente, plausibilità, ecc.). |
| **OIS — optimal information size** | Numero di partecipanti/eventi che una meta-analisi dovrebbe avere per non essere «imprecisa» (GRADE). |

## Identificatori

| Sigla | Cos'è | Forma del link |
|---|---|---|
| **DOI** | Identificatore permanente del documento. | `https://doi.org/10.xxxx/yyyy` |
| **PMID** | Identificatore PubMed. | `https://pubmed.ncbi.nlm.nih.gov/PMID/` |
| **PMCID** | Identificatore PubMed Central (full text libero). | `https://pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxxx/` |
| **NCT** | Numero di registrazione su ClinicalTrials.gov. | `https://clinicaltrials.gov/study/NCTxxxxxxxx` |
| **CRD / PROSPERO ID** | Registrazione della revisione sistematica. | `https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=xxxxxx` |
| **ISRCTN** | Registro internazionale di trial. | `https://www.isrctn.com/ISRCTNxxxxxxxx` |
