# La Rotta — Basi scientifiche

Documento di riferimento per l'app di auto-monitoraggio `app/la-rotta.html`.
Ogni componente dell'app deriva da un intervento con prove di efficacia; questo
documento dichiara quale, e con quale livello di solidità.

**Premessa vincolante.** L'app è uno strumento *adiuvante*: l'evidenza più
solida, per il quadro a cui è destinata (disturbo bipolare I, tratti di
personalità del cluster B, disturbo da uso di cocaina), riguarda la
combinazione di farmacoterapia stabilizzante, psicoterapia strutturata e presa
in carico specialistica per la sostanza (SerD). Nessun componente dell'app
sostituisce questi pilastri; ciascuno è progettato per potenziarli.

---

## 1. Check-in quotidiano dell'umore (scala −3 … +3)

- **Origine**: auto-monitoraggio prospettico dell'umore sul modello del
  *Life Chart Method* (NIMH) e delle mood chart usate di routine nei centri per
  i disturbi bipolari.
- **Razionale**: la registrazione quotidiana rende visibili le oscillazioni
  prima che diventino episodi e fornisce al clinico dati prospettici, molto più
  affidabili del ricordo retrospettivo.
- **Solidità**: pratica clinica standard raccomandata dalle principali linee
  guida sul disturbo bipolare (es. CANMAT/ISBD); l'efficacia come intervento
  isolato è modesta, il valore è nell'integrazione con la cura.

## 2. Monitoraggio del sonno e avviso precoce

- **Origine**: psicoeducazione sul riconoscimento dei segnali precoci
  (*early warning signs*) e terapia interpersonale e dei ritmi sociali (IPSRT,
  Frank e coll.).
- **Razionale**: la riduzione del bisogno di sonno è tra i prodromi più
  affidabili dell'episodio maniacale; la regolarità dei ritmi sociali
  (sveglia, pasti, contatti) ha mostrato effetti protettivi sulle ricadute.
- **Solidità**: gli interventi di riconoscimento dei segnali precoci hanno
  evidenza da studi randomizzati e revisioni sistematiche (riduzione delle
  ricadute e delle ospedalizzazioni, in particolare per gli episodi
  maniacali); IPSRT ha evidenza da RCT come terapia aggiuntiva.
- **Implementazione nell'app**: avviso automatico quando sonno ≤ 5 ore con
  umore in salita (≥ +1); avviso dopo 3 giorni consecutivi con umore ≤ −2.

## 3. Monitoraggio di craving e uso, striscia di giorni puliti, premi

- **Origine**: *contingency management* (rinforzo dei comportamenti di
  astinenza) e prevenzione delle ricadute.
- **Razionale**: per il disturbo da uso di cocaina non esiste ad oggi una
  farmacoterapia approvata; il contingency management è l'intervento con le
  prove di efficacia più consistenti nelle meta-analisi (effetto da moderato
  in su sull'astinenza durante il trattamento), seguito dagli approcci
  cognitivo-comportamentali.
- **Solidità**: alta per il contingency management erogato professionalmente;
  la versione auto-gestita dell'app (traguardi e premi auto-assegnati) è una
  trasposizione a intensità ridotta, da considerare supporto motivazionale,
  non equivalente al trattamento formale.
- **Implementazione nell'app**: contatore dei giorni senza uso, sezione
  "Traguardi e premi" definita in anticipo nei giorni stabili, registrazione
  non giudicante dell'uso (contrasto all'*abstinence violation effect*: la
  vergogna post-ricaduta è un predittore documentato della ricaduta
  successiva).

## 4. Cassetta degli attrezzi

| Strumento | Fonte | Note sull'evidenza |
|---|---|---|
| STOP | DBT, tolleranza del disagio | La DBT ha evidenza da RCT e meta-analisi per il disturbo borderline (riduzione di autolesionismo e impulsività) |
| TIPP | DBT, sopravvivenza alla crisi | Come sopra; agisce sulla fisiologia dell'attivazione |
| Azione opposta | DBT, regolazione emotiva | Come sopra |
| Surf dell'impulso | Prevenzione ricadute basata su mindfulness (Marlatt, Bowen) | Evidenza da RCT su riduzione di craving e uso come componente di programmi MBRP |
| HALT | Prevenzione delle ricadute | Strumento clinico consolidato; evidenza indiretta tramite i programmi che lo includono |
| Pausa di auto-compassione | Self-compassion (Neff) | Evidenza meta-analitica su riduzione di vergogna e autocritica; rilevante per i tratti narcisistici covert, dove la vergogna è il perno |
| Ritmi regolari | IPSRT (Frank) | RCT come terapia aggiuntiva nel bipolare |

## 5. Piano di prevenzione e piano di crisi

- **Origine**: psicoeducazione per il disturbo bipolare (programma di
  Barcellona, Colom e Vieta) e *safety planning* (Stanley e Brown).
- **Razionale**: un piano scritto nei periodi stabili — segnali personali,
  azioni concordate, contatti — riduce il tempo tra prodromo e intervento;
  il safety planning ha evidenza propria nella riduzione dei comportamenti
  suicidari.
- **Solidità**: la psicoeducazione strutturata per il bipolare ha evidenza da
  RCT con follow-up pluriennale sulla riduzione delle ricadute.

## 6. Aderenza farmacologica

- **Razionale**: l'interruzione dei farmaci stabilizzanti è tra le prime cause
  di ricaduta nel disturbo bipolare; il monitoraggio quotidiano rende visibile
  il pattern di assunzione al clinico.
- **Implementazione**: registrazione sì / in parte / no, con avviso
  non giudicante in caso di sospensione e invito esplicito a decidere ogni
  modifica con lo psichiatra.

---

## Limiti dichiarati

1. L'auto-monitoraggio digitale, da solo, ha effetti piccoli: il valore atteso
   dell'app dipende dal suo uso *dentro* una relazione di cura.
2. I premi auto-gestiti non replicano l'efficacia del contingency management
   formale (dove il rinforzo è esterno e immediato).
3. Le soglie di avviso (sonno ≤ 5h, craving ≥ 7, tre giorni a umore ≤ −2) sono
   euristiche cliniche ragionevoli, non soglie validate individualmente: vanno
   tarate con il clinico di riferimento.
4. Nessuna parte dell'app è un dispositivo medico né fa diagnosi.

## Numeri utili integrati nell'app

- **112** — emergenza.
- **Telefono Amico Italia** — 02 2327 2327 (fascia oraria indicativa 10–24;
  verificare eventuali aggiornamenti su telefonoamico.it).
- Contatti personali (psichiatra, SerD, persone fidate) configurabili nella
  sezione Piano.
