---
stanje: ZATVORENO
opis: Razgovor je završen (klijent je poručio ili rezervisao). Bot NE odgovara na poruke.
bot_odgovara: false
ulazi_iz:
  - PORUCIO
prelazi_u: []
memorija_cita: []
memorija_pise: []
---

# ZATVORENO

## Cilj
**Ne odgovarati klijentu.** Rješava problem beskonačne petlje "hvala" → "nema na čemu" → "a hvala" → itd.

## Kontekst
Razgovor je logički završen — klijent je poručio ili prihvatio rezervaciju, bot je poslao zadnju potvrdu.

## Šta bot radi
**NIŠTA.** Bot se **NE poziva** u ovom stanju.

Webhook handler u `app.py`, **odmah poslije parsinga poruke**, provjerava stanje. Ako je `ZATVORENO`:
1. Log: `ignoring message from closed conversation {sender_id}`
2. Ne dodaje u debounce queue
3. Ne poziva Dragana
4. Vraća `200 EVENT_RECEIVED`

## Kako otvoriti razgovor nazad
Ognjen ručno preko admin endpoint-a:
```
POST /admin/reopen/{sender_id}?stanje=POCETAK
```
Postavlja stanje nazad u neko aktivno (POCETAK / PRIKUPLJANJE / itd.), bot opet odgovara.

## Edge cases
- **Klijent pošalje "hvala"** → ignoriše
- **Klijent pošalje lajk (reakcija)** → ignoriše
- **Klijent pita dodatno pitanje par mjeseci kasnije** → ignoriše (Ognjen odlučuje ručno da li ponovo otvoriti)
- **Klijent se žali "nisam dobio paket"** → ignoriše od strane bota (ljudski intervenisan tok — Ognjen vidi kroz FB admin, reaguje sam)

## KRITIČNO
Ovo stanje nema state prompt jer bot ne generiše poruku. `load_state_prompt("ZATVORENO")` se **nikad ne poziva** — stanje se filtrira prije.
