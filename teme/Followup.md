---
type: hub-tema
---

# Followup — Agent 2

**Povezano:** [[INDEX]]

## Šta je
Proaktivni followup agent — šalje klijentima koji su `awaiting_reply=True`. Max 5 ignorisanih pre nego što dobije labelu "Zimski kontakt".

## Fajlovi
- `agents/followup.py` — check_and_send()
- APScheduler job svakih 30 min (app.py:601)

## Sesije
_(automatski ažurirano)_
