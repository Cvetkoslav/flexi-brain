---
type: hub-tema
---

# AdminHandler — Admin komande

**Povezano:** [[INDEX]]

## Šta je
Sve komande koje admin šalje u Messenger. Dispatcher pattern — `/komanda subkomanda`.

## Fajlovi
- `agents/admin_handler.py` — COMMANDS dict, cmd_* funkcije

## Ključne komande
- `/profile <ime>` — pregled klijenta
- `/label <ime> <labela>` — ručno labelisanje
- `/snooze <ime> <trajanje>` — pauziranje klijenta
- `/briefing` — ručni jutarnji izveštaj
- `/react <sub>` — reaktivacioni agent (status, list, sent, run, send, reset, off, on, toggle, log, msgs, stats, rebuild-labels)
- `/kb <tekst>` — dodaj KB pravilo
- `/brain sync` — ručni pull iz Git → Postgres
- `/brain status` — stanje KB sync-a
- `/cold` — lista cold/lost klijenata

## Sesije
_(automatski ažurirano)_
