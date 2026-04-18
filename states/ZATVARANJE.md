---
stanje: ZATVARANJE
opis: Klijent kaže DA — bot traži podatke za dostavu ili rezervaciju
bot_odgovara: true
ulazi_iz:
  - PREPORUKA
  - UBJEDJIVANJE
prelazi_u:
  - PORUCIO
  - SELF
memorija_cita:
  - ime
  - vokativ
memorija_pise:
  - prigovori  # ako se u zadnji čas pojavi prigovor
---

# ZATVARANJE

## Cilj
<!-- TODO: jedna rečenica. -->

## Kontekst koji bot ima
Puna slika, klijent je rekao DA.

## Šta bot radi
<!-- TODO: popuniti. -->

<!-- PLACEHOLDER:

1. Prva poruka: "Odlično {vokativ}! Pošaljite puno ime, ulicu i broj, i Vaš telefon."

2. Klijent šalje podatke → bot potvrđuje → prelazi PORUCIO

3. Ako nedostaje nešto (npr. samo ime bez adrese) → ostaje SELF, traži što nedostaje

4. Rezervacija grana — drugačiji tekst ali ista mehanika, samo napomene "šaljemo kad budete spremni"

-->

## Uslovi za prelaz
- `PORUCIO` — klijent je poslao ime + adresu + telefon
- `SELF` — dio podataka nedostaje, bot traži ostatak

## Edge cases
- **U zadnji čas "ipak ne"** → nazad u UBJEDJIVANJE sa novim prigovorom
- **Samo ime ili samo telefon** → traži što nedostaje, ne zapisuj "PORUCIO" dok nije kompletno
- **Pita za dostavu/plaćanje** → bot odgovara (plaćanje pouzećem, 2-3 dana), ostaje ZATVARANJE

## Primjer poruka
<!-- TODO -->
