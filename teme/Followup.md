---
type: hub-tema
---

# Followup — Jedini aktivni agent

**Povezano:** [[INDEX]]

## Šta je

Jedina automatizacija u botu. Svakih 30 min provjerava ko nije odgovorio i šalje poruke prilagođene stanju razgovora.

## Pravila

- Ne šalje između 22h i 8h
- Max 5 followupa dnevno po klijentu
- Čeka 2h ako je klijent pročitao poruku, 3h ako nije
- Preskače ZATVORENO i PORUCIO stanja

## Poruke po stanju

| Stanje | Poruke |
|--------|--------|
| POCETAK, PRIKUPLJANJE | Pita za simptome |
| PREPORUKA, UBJEDJIVANJE | Podseća na ponudu, otklanja sumnje |
| ZATVARANJE | Traži podatke za dostavu |

## Fajlovi

- `agents/followup.py` — `check_and_send()`
- `app.py` — APScheduler job svakih 30 min

## Ručno upravljanje stanjima

Ognjen postavlja stanje klijentu ručno preko admin endpointa:
`POST /admin/set-state/<sender_id>?stanje=UBJEDJIVANJE`

Ovo kontroliše koje followup poruke klijent dobija.
