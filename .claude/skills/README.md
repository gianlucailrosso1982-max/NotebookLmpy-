# Skill personali — NotebookLmpy-

Skill riutilizzabili di Gianluca, versionate nel repo e attive quando si lavora qui su Claude Code.

## Skill presenti

| Skill | A cosa serve |
|---|---|
| `fonti-scientifiche-validate` | Ricerca su fonti scientifiche autorevoli con livello GRADE ed efficacia reale — skill multi-file: `SKILL.md` + `references/` + `scripts/effetti.py` |
| `gestione-tono-genere-scrittura` | Costruisce e applica il profilo stilistico personale (scrivere "come me") |
| `la-mia-mente` | Regole di lavoro sul vault "La mia Mente" (psicologia clinica, persuasione) |
| `manuali-memorabili` | Progetta e impagina manuali/guide/corsi che si imparano e si ricordano |
| `meta-prompt` | Costruisce meta-prompt riutilizzabili in 4 passaggi |
| `notebooklm` | Comanda Google NotebookLM dal browser (notebook, fonti, audio/video overview) |
| `persuasione-scientifica-strategica` | Scrittura persuasiva basata su evidenza (catene linguistiche + filtro scientifico) |
| `ultra-mode` | Modalità di massima qualità, con interruttore interno sintetico ↔ approfondito |

## Note sulla revisione (2026-09)

- **`fonti-scientifiche-validate` ricostruita a divulgazione progressiva.** `SKILL.md` contiene il protocollo (triage rapido/completo, sei fasi con fallback a cascata, tre esiti per ogni controllo: superato / fallito / non verificato); otto file in `references/` approfondiscono gerarchia, strumenti, strategie di ricerca, GRADE ed effetti assoluti, controllo qualità, formato, esempi svolti con dati reali e glossario; `scripts/effetti.py` calcola RR/OR/ARR/NNT con IC 95% (validato sulla revisione Cochrane 2022 CD004976). Correzioni nate da un'analisi tecnica empirica: in ambienti con proxy restrittivo WebFetch è bloccato verso i domini scientifici, mentre i connettori MCP funzionano; il controllo delle ritrattazioni usa `article_types` dei metadati PubMed; i numeri degli snippet di ricerca non sono citabili.

## Note sulla revisione (2026-08)

- **`super-skill` fusa in `ultra-mode`.** Le due skill si contendevano gli stessi trigger ("massima qualità", "dammi il meglio", ecc.). Ora un'unica skill con interruttore interno: **sintetico** (default, denso e a risparmio di token) o **approfondito** (ragionamento esteso). Assorbe i trigger di entrambe.
- **`persuasione-scientifica-strategica`**: rimosso un frontmatter duplicato che attivava la skill con una descrizione vaga ("da usare in tutte le guide e i manuali"), causa di sovrapposizione con `manuali-memorabili`. Ora usa la descrizione corretta e circoscritta ai testi persuasivi.
- **`meta-prompt`**: descrizione riscritta (era in maiuscolo, con refuso e trigger vaghi).
