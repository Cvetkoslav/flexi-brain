---
type: hub-tema
---

# Dragana — Sales Agent

**Povezano:** [[INDEX]]

## Šta je
Glavni sales agent na Claude Sonnet 4.6. Vodi razgovor, empatiše, nudi komplet.

## Fajlovi u flexi-bot-u
- `agents/dragana.py` — glavna logika, system prompt, respond()
- `agents/knowledge.py` — keyword→tag mapping za KB fallback
- `db.py:518` `get_knowledge_by_tags()` — Dragana zove ovo za KB rules
- `db.py:557` `get_knowledge_by_keyword()` — keyword fallback
- `agents/labeler.py` — Haiku 4.5 koji posle svakog odgovora postavlja label, tags, next_action

## KB kategorije koje najviše utiču
- `stil-govora/` — jezik, ton, dužina
- `struktura/` — faze razgovora
- `objekcije/` — odgovori na prigovore
- `zatvaranje/` — kako tražiti adresu

## Poznati problemi
- Ijekavski leak u odgovorima (rešava se seed rules u `stil-govora/ekavski-obavezno.md`)
- Ponekad 6+ pitanja pre ponude (rešava `stil-govora/max-3-pitanja.md`)
- Slike kapsule/balzam koriste placeholder URL

## Sesije
_(automatski ažurirano)_
