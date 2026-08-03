# Distribuire queste skill su claude.ai e Cowork

Il formato **Agent Skills** (cartella con `SKILL.md`) è lo stesso su Claude Code, claude.ai e Cowork,
ma **le skill NON si sincronizzano tra le superfici**: vanno caricate separatamente su ognuna.
Fonte: [Agent Skills — Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Vincoli da rispettare (validi per claude.ai e Cowork, non per Claude Code)

- `description` **massimo 1024 caratteri**. La versione lunga di `persuasione-scientifica-strategica`
  (1465 char) è accettata solo su Claude Code; per claude.ai/Cowork esiste una variante ridotta a 999 char
  nei pacchetti di upload.
- `name` solo minuscole, numeri e trattini; **non può contenere "claude" o "anthropic"**. Le 8 skill sono già conformi.
- Zip: la cartella della skill deve stare **alla radice** dell'archivio (non il solo `SKILL.md`).

## Caricare su claude.ai

Requisiti: piano **Pro / Max / Team / Enterprise** con **creazione file / code execution attiva**.
Le skill sono **individuali** (non condivisibili a livello di organizzazione).

1. Impostazioni → **Funzionalità (Features)** → **Skills** → **Carica (Upload)**.
2. Carica **un file zip per skill** (le 8 zip singole). Il bundle unico serve solo come archivio/backup: non caricarlo come skill singola.
3. Claude legge il `SKILL.md` e mostra nome + descrizione. Attiva/disattiva ogni skill dallo stesso pannello.

## Caricare su Cowork

In Cowork le skill arrivano tramite il pannello **Customize** (barra laterale sinistra).

1. **Customize** → **+** → apri la directory → scheda **Skills**.
2. Aggiungi le skill dalla directory oppure carica un tuo file. Se Cowork accetta solo **plugin**,
   la skill va impacchettata in un plugin minimo (posso generarlo su richiesta).
3. Le skill/plugin che aggiungi tu su desktop sono salvati **in locale** sul tuo computer.

## Portabilità per skill

Cowork (desktop) accede al filesystem locale come Claude Code; claude.ai gira in una VM sandbox
senza controllo del browser e con rete variabile.

| Skill | claude.ai | Cowork | Note |
|---|:---:|:---:|---|
| `ultra-mode` | ✅ | ✅ | Pura istruzione comportamentale |
| `meta-prompt` | ✅ | ✅ | Pura istruzione |
| `persuasione-scientifica-strategica` | ✅ | ✅ | Usa la descrizione ridotta (≤1024) |
| `manuali-memorabili` | ✅ | ✅ | Genera PDF via code execution |
| `fonti-scientifiche-validate` | ⚠️ | ✅ | Su claude.ai serve la ricerca web abilitata |
| `gestione-tono-genere-scrittura` | ⚠️ | ✅ | Legge/scrive `profilo-stilistico.md`: su web niente persistenza tra sessioni → ricarica il profilo ogni volta |
| `la-mia-mente` | ⚠️ | ✅ | Il vault Obsidian è sul tuo disco: su web va caricato manualmente; Cowork lo legge in locale |
| `notebooklm` | ❌ | ⚠️ | Pilota NotebookLM via "Claude in Chrome": non disponibile nella VM di claude.ai; su Cowork solo se ha controllo del browser |

Legenda: ✅ funziona · ⚠️ funziona con limiti/condizioni · ❌ non funziona su quella superficie.
