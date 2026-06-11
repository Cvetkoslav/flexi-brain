# Flexi Brain

Obsidian vault i baza znanja za **Flexi Bot** (Facebook Messenger followup bot za Flexi Zglobovi proizvode).

## Novo stanje (jun 2026)

Bot je drastično pojednostavljen. **Dragana agent je uklonjen.** Ognjen sam piše poruke klijentima iz Messenger inboxa. Bot radi samo jedno: automatski followup poruke za klijente koji nisu odgovorili.

## Šta bot radi

1. Prima webhook event kad klijent pošalje poruku — loguje je, resetuje followup brojač
2. Svakih 30 min APScheduler poziva `followup.check_and_send()` — šalje automatske poruke onima koji nisu odgovorili

## Stack

- Python / Flask
- SQLite na Railway Volume (`/data/data.db`)
- APScheduler (followup svakih 30 min)
- Railway hosting, GitHub auto-deploy
- **Nema Anthropic/Claude API** — bot ne generiše tekst

## Fajlovi

```
app.py              — Flask webhook + scheduler + admin endpointi
agents/followup.py  — followup logika, poruke po stanjima
brain.py            — SQLite CRUD (klijenti, poruke)
facebook.py         — send_message, get_user_name, labele
config.py           — env vars
```

## Admin endpointi

- `GET  /health` — status
- `GET  /admin/status` — svi klijenti
- `GET  /admin/client/<id>` — jedan klijent + poruke
- `POST /admin/reopen/<id>?stanje=POCETAK` — otvori ponovo
- `POST /admin/set-state/<id>?stanje=UBJEDJIVANJE` — ručno postavi stanje

## KB fajlovi

Folder `stil-govora/`, `objekcije/`, `zatvaranje/` itd. ostaje kao referenca i dokumentacija, ali bot ih više NE čita. Koristi ih Ognjen kao podsjetnik kad piše poruke ručno.
