---
stanje: PORUCIO
opis: Klijent je dao podatke — bot šalje zadnju potvrdu i odmah prelazi u ZATVORENO
bot_odgovara: true    # jednu, zadnju poruku
ulazi_iz:
  - ZATVARANJE
prelazi_u:
  - ZATVORENO  # OBAVEZNO — ovdje razgovor završava
memorija_cita:
  - vokativ
memorija_pise: []
---

# PORUCIO

## Cilj
Poslati potvrdu narudžbe i **zatvoriti razgovor**. Poslije ovog stanja bot VIŠE NE odgovara.

## Kontekst koji bot ima
Sve + potvrđene podatke za dostavu.

## Šta bot radi
Šalje jednu zadnju poruku i **obavezno** postavlja `novo_stanje=ZATVORENO`.

**Template poruke:**
```
Hvala {vokativ}! Paket stiže za 2-3 dana, plaćate pouzećem. Ako budete imali pitanja u toku korištenja, slobodno nam se javite 😊
```

<!-- TODO: finalni tekst kad Ognjen potvrdi. -->

## Uslovi za prelaz
- `ZATVORENO` — UVIJEK, odmah poslije ove poruke. Nema druge opcije.

## Edge cases
Ne postoje — PORUCIO je jednokratan.

## KRITIČNO
Ovo stanje MORA da postavi `novo_stanje=ZATVORENO`. Bez izuzetka. Ako tool_use vrati bilo šta drugo, kod odbacuje odgovor.
