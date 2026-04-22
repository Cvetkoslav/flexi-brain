---
type: community
cohesion: 0.09
members: 34
---

# Bot Arhitektura i Infrastruktura

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[AB weighted scoring za reaktivacione poruke]] - document - flexi-brain/teme/Reaktivacija.md
- [[AdminHandler — Admin komande]] - document - flexi-brain/teme/AdminHandler.md
- [[Briefing — Jutarnji izveštaj]] - document - flexi-brain/teme/Briefing.md
- [[Client memorija schema (SQLite)]] - document - flexi-brain/_schema/client.md
- [[Conversation state enum (POCETAK..ZATVORENO)]] - document - flexi-brain/_schema/tool-use.md
- [[Database — Postgres schema]] - document - flexi-brain/teme/Database.md
- [[Dostava — informacije i pravila]] - document - flexi-brain/struktura/dostava.md
- [[Downsell flow komplet → balzam]] - document - flexi-brain/struktura/downsell-balzam.md
- [[Downsell — samo balzam kao last resort]] - document - flexi-brain/struktura/downsell-balzam.md
- [[Dragana tool use — update_state schema]] - document - flexi-brain/_schema/tool-use.md
- [[Dragana — Sales Agent]] - document - flexi-brain/teme/Dragana.md
- [[Empatija pre prodaje]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[Followup — Agent 2]] - document - flexi-brain/teme/Followup.md
- [[Format poruka (Dragana stil)]] - document - flexi-brain/struktura/format-poruka.md
- [[Klijent kaže DA — odmah uzmi adresu]] - document - flexi-brain/zatvaranje/klijent-kaze-da.md
- [[Klijent odgađa — ponudi rezervaciju]] - document - flexi-brain/zatvaranje/odgada.md
- [[Kratke poruke (max 2-3 rečenice)]] - document - flexi-brain/stil-govora/kratke-poruke.md
- [[Maksimalno 3 pitanja pre ponude]] - document - flexi-brain/stil-govora/max-3-pitanja.md
- [[Nema lažnih obećanja]] - document - flexi-brain/stil-govora/nema-laznih-obecanja.md
- [[Nema ponavljanja pitanja]] - document - flexi-brain/stil-govora/nema-ponavljanja.md
- [[Rationale Bez empatije, ponuda izgleda kao spam]] - document - stil-govora/empatija-pre-prodaje.md
- [[Rationale bez empatije ponuda izgleda kao spam]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[Rationale ponavljanje narušava poverenje klijenta]] - document - flexi-brain/stil-govora/nema-ponavljanja.md
- [[Rationale pravni i etički razlog — ne smemo garantovati medicinske rezultate]] - document - flexi-brain/stil-govora/nema-laznih-obecanja.md
- [[Rationale tool use forsira validan JSON i sprečava izmišljanje stanja]] - document - flexi-brain/_schema/tool-use.md
- [[Razmisliću — dijagnoza prigovora]] - document - flexi-brain/zatvaranje/razmislicu.md
- [[Reaktivacija — Agent 4]] - document - flexi-brain/teme/Reaktivacija.md
- [[Stil govora kategorija]] - document - flexi-brain/stil-govora/empatija-pre-prodaje.md
- [[Upsell flow komplet + čajSynchrovitals]] - document - flexi-brain/zatvaranje/upsell.md
- [[Upsell — čaj ili Synchrovitals]] - document - flexi-brain/zatvaranje/upsell.md
- [[Urgencija — ograničene zalihe]] - document - flexi-brain/zatvaranje/urgencija.md
- [[Zatvaranje kategorija]] - document - flexi-brain/zatvaranje/klijent-kaze-da.md
- [[extract_session prompt — kompaktovanje sesije]] - document - flexi-brain/_tools/prompts/extract_session.txt
- [[update_state Anthropic tool use]] - document - flexi-brain/_schema/tool-use.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bot_Arhitektura_i_Infrastruktura
SORT file.name ASC
```
