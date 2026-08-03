# Skill personali — NotebookLmpy-

Skill riutilizzabili di Gianluca, versionate nel repo e attive quando si lavora qui su Claude Code.

## Skill presenti

| Skill | A cosa serve |
|---|---|
| `fonti-scientifiche-validate` | Ricerca su fonti scientifiche autorevoli con livello GRADE ed efficacia reale |
| `gestione-tono-genere-scrittura` | Costruisce e applica il profilo stilistico personale (scrivere "come me") |
| `la-mia-mente` | Regole di lavoro sul vault "La mia Mente" (psicologia clinica, persuasione) |
| `manuali-memorabili` | Progetta e impagina manuali/guide/corsi che si imparano e si ricordano |
| `meta-prompt` | Costruisce meta-prompt riutilizzabili in 4 passaggi |
| `notebooklm` | Comanda Google NotebookLM dal browser (notebook, fonti, audio/video overview) |
| `persuasione-scientifica-strategica` | Scrittura persuasiva basata su evidenza (catene linguistiche + filtro scientifico) |
| `scrittura-di-valore` | Agente che fonde le tre skill di scrittura (fonti + manuali + persuasione) in un testo insieme vero, memorabile e persuasivo |
| `ultra-mode` | Modalità di massima qualità, con interruttore interno sintetico ↔ approfondito |

## Note sulla revisione (2026-08)

- **`super-skill` fusa in `ultra-mode`.** Le due skill si contendevano gli stessi trigger ("massima qualità", "dammi il meglio", ecc.). Ora un'unica skill con interruttore interno: **sintetico** (default, denso e a risparmio di token) o **approfondito** (ragionamento esteso). Assorbe i trigger di entrambe.
- **`persuasione-scientifica-strategica`**: rimosso un frontmatter duplicato che attivava la skill con una descrizione vaga ("da usare in tutte le guide e i manuali"), causa di sovrapposizione con `manuali-memorabili`. Ora usa la descrizione corretta e circoscritta ai testi persuasivi.
- **`meta-prompt`**: descrizione riscritta (era in maiuscolo, con refuso e trigger vaghi).
- **`scrittura-di-valore` (nuova).** Agente-orchestratore che fonde le tre skill di scrittura — `fonti-scientifiche-validate`, `manuali-memorabili`, `persuasione-scientifica-strategica` — in un unico flusso. Non le riscrive: le subordina l'una all'altra risolvendone le tensioni (il tetto GRADE frena la promessa persuasiva; l'attrito dell'apprendimento va sulla struttura, non sulla catena d'azione; magazzino dei fatti condiviso contro la doppia contabilità degli effect size). Trigger circoscritti all'orchestrazione ("testo dal valore eccezionale", "il migliore possibile", contenuto insieme vero + memorabile + persuasivo), per non collidere con i trigger delle tre skill sorgente. Chiude con un'unica dichiarazione di certezza integrata.
