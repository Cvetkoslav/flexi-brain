---
type: hub-tema
---

# Briefing — Jutarnji izveštaj

**Povezano:** [[INDEX]]

## Šta je
Šalje jutarnji pregled svim ADMIN_PSIDS u 08:05. Može se pozvati ručno sa `/briefing`.

## Fajlovi
- `agents/briefing.py` — send_briefing(), _build_messages()
- APScheduler cron job 08:05 (app.py:604)

## Sadržaj izveštaja
- Poruka 1: statistike 24h (novi, aktivni, prodaje, snooze)
- Poruka 2: top 5 vrućih leadova + potrebna akcija (call)
- Poruka 3: snooze ističe danas + cold/lost count
- Poruka 4: reaktivacija 24h + A/B pobednik

## Sesije
_(automatski ažurirano)_
