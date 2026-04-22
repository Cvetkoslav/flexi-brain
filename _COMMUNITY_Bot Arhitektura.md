---
type: community
cohesion: 0.12
members: 25
---

# Bot Arhitektura

**Cohesion:** 0.12 - loosely connected
**Members:** 25 nodes

## Members
- [[AB weighted scoring za reaktivacione poruke]] - document - flexi-brain/teme/Reaktivacija.md
- [[AdminHandler — Admin komande]] - document - flexi-brain/teme/AdminHandler.md
- [[Briefing — Jutarnji izveštaj]] - document - flexi-brain/teme/Briefing.md
- [[Client memorija schema (SQLite)]] - document - flexi-brain/_schema/client.md
- [[Conversation state enum (POCETAK..ZATVORENO)]] - document - flexi-brain/_schema/tool-use.md
- [[Database — Postgres schema]] - document - flexi-brain/teme/Database.md
- [[Downsell flow komplet → balzam]] - document - flexi-brain/struktura/downsell-balzam.md
- [[Downsell — samo balzam kao last resort]] - document - flexi-brain/struktura/downsell-balzam.md
- [[Dragana tool use — update_state schema]] - document - flexi-brain/_schema/tool-use.md
- [[Dragana — Sales Agent]] - document - flexi-brain/teme/Dragana.md
- [[Empatija pre prodaje]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[Followup — Agent 2]] - document - flexi-brain/teme/Followup.md
- [[Format poruka (Dragana stil)]] - document - flexi-brain/struktura/format-poruka.md
- [[Kratke poruke (max 2-3 rečenice)]] - document - flexi-brain/stil-govora/kratke-poruke.md
- [[Maksimalno 3 pitanja pre ponude]] - document - flexi-brain/stil-govora/max-3-pitanja.md
- [[Nema lažnih obećanja]] - document - flexi-brain/stil-govora/nema-laznih-obecanja.md
- [[Nema ponavljanja pitanja]] - document - flexi-brain/stil-govora/nema-ponavljanja.md
- [[Rationale bez empatije ponuda izgleda kao spam]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[Rationale ponavljanje narušava poverenje klijenta]] - document - flexi-brain/stil-govora/nema-ponavljanja.md
- [[Rationale pravni i etički razlog — ne smemo garantovati medicinske rezultate]] - document - flexi-brain/stil-govora/nema-laznih-obecanja.md
- [[Rationale tool use forsira validan JSON i sprečava izmišljanje stanja]] - document - flexi-brain/_schema/tool-use.md
- [[Reaktivacija — Agent 4]] - document - flexi-brain/teme/Reaktivacija.md
- [[Stil govora kategorija]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[extract_session prompt — kompaktovanje sesije]] - document - flexi-brain/_tools/prompts/extract_session.txt
- [[update_state Anthropic tool use]] - document - flexi-brain/_schema/tool-use.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bot_Arhitektura
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Zatvaranje i Dostava]]

## Top bridge nodes
- [[Dragana — Sales Agent]] - degree 9, connects to 1 community
- [[Downsell — samo balzam kao last resort]] - degree 3, connects to 1 community