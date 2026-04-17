# Flexi Brain

Obsidian vault i znanje-baza za **Flexi Bot** (Facebook Messenger sales bot za Flexi Zglobovi proizvode).

## Šta je ovo

Ovaj repo sadrži dve stvari:

1. **KB pravila** (`stil-govora/`, `objekcije/`, `zatvaranje/`, `proizvodi/`, `pravila/`, `struktura/`) — `.md` fajlovi sa YAML frontmatter-om koje produkcijski bot (Dragana) čita iz Postgres-a. Sinhronizacija ide preko `brain/git_sync.py` na Railway-u, svakih 15 minuta.

2. **Session logovi + topic hubovi** (`sessions/`, `teme/`, `meta/`) — Obsidian graph za Ognjenovu memoriju, NE konzumira ih bot.

## Workflow

- Ognjen radi sesije sa Claude Code-om
- Na `/compact`, PreCompact hook (`_tools/brain_save.py`) generiše izveštaj u `sessions/`
- Hook commit-uje i push-uje na GitHub
- Railway server povlači nove fajlove svakih 15 min i upsert-uje u Postgres `knowledge_base` tabelu
- Dragana pri sledećem odgovoru klijentu koristi sveže rules

## Format KB fajla

```yaml
---
situation: "Kad klijent kaže X"
rule: "Uradi Y, izbegni Z"
example_response: "Konkretan primer odgovora"
category: objekcije | zatvaranje | proizvodi | pravila | struktura
tags: [tag1, tag2]
priority: 1-10
active: true
---
```

Fajlovi bez `situation` + `rule` se ignorišu (tako se `sessions/`, `teme/`, `meta/` preskaču).
