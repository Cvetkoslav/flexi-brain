---
type: hub-tema
---

# Reaktivacija — Agent 4

**Povezano:** [[INDEX]]

## Šta je
Cron agent koji svakih 60 min šalje "da li si još zainteresovan" poruku klijentima koji su ćutali 7+ dana. Nema Claude API poziva — 0 tokena.

## Fajlovi
- `agents/reactivation.py` — check_and_send(), _is_candidate(), _send()
- `db.py` — tabela `reactivation_msg_stats` za A/B scoring
- `agents/admin_handler.py` — `/react` komanda sa 13 podkomandi

## Parametri
- SILENCE_DAYS = 7 · REPEAT_DAYS = 14
- Rate limit: 15 poruka/sat (sleep 220-260s)
- Radi 8-22h
- 10 core varijacija × 5 prefiksa × 5 sufiksa = 250 kombinacija
- A/B weighted: `(replies+1)/(sent+5)` Laplace smoothing

## Sesije
_(automatski ažurirano)_
