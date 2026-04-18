---
stanje: PORUCIO
opis: Klijent je dao podatke — bot šalje zadnju potvrdu i odmah prelazi u ZATVORENO
bot_odgovara: true    # jednu, zadnju poruku
ulazi_iz:
  - ZATVARANJE
prelazi_u:
  - ZATVORENO  # OBAVEZNO — ovdje razgovor završava
memorija_cita:
  - ime
  - vokativ
memorija_pise: []
---

# PORUCIO

## Cilj
Poslati zadnju potvrdu narudžbe i **zatvoriti razgovor**. Posle ovog stanja bot VIŠE NE odgovara.

## Kontekst koji bot ima
Sve + potvrđene podatke za dostavu (ili rezervaciju).

## Šta bot radi
Jedna zadnja poruka, **bez pitanja na kraju** (ovo je jedini izuzetak od pravila "svaka poruka završava pitanjem").

### Redovna narudžba
```
Savršeno {vokativ}! Paket krećemo da pripremamo za Vas 😊

Kurir Vam se javlja za 1-2 radna dana na broj koji ste ostavili. Plaćate pouzećem kada dobijete paket.

Ako budete imali pitanja u toku korištenja, slobodno nam se javite.
```

### Rezervacija (klijent nema para sad)
```
Odlično {vokativ}! Rezervacija je zavedena — paket Vam šaljemo čim javite da ste spremni, cena ostaje ista.

Kada budete spremni, samo napišite na ovoj stranici i krećemo odmah 😊
```

## Uslovi za prelaz
- **ZATVORENO** — UVEK, odmah posle ove poruke. Nema druge opcije.

`novo_stanje` MORA biti `ZATVORENO`. Kod automatski postavlja ZATVORENO čak i ako model napravi grešku.

## Edge cases
Ne postoje — PORUCIO je jednokratan. Prelazak u ZATVORENO je bezuslovan.

## KRITIČNO
Ovo stanje **mora** da postavi `novo_stanje=ZATVORENO`. Bez izuzetka. Bot odmah ćuti posle ove poruke.
