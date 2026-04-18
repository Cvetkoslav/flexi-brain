---
stanje: IME_STANJA
opis: jedna rečenica — šta se dešava u ovom stanju
bot_odgovara: true
ulazi_iz:
  - STANJE_A
  - STANJE_B
prelazi_u:
  - STANJE_C
  - STANJE_D
  - SELF          # bot ostaje u istom stanju (npr. prikuplja još info)
memorija_cita:    # polja koja bot čita iz klijentske memorije
  - ime
  - vokativ
memorija_pise:    # polja koja bot može da upiše/mijenja
  - simptomi_detalji
  - probao_prije
---

# IME_STANJA

## Cilj
<!-- Jedna rečenica: šta bot postiže u ovom stanju. -->

## Kontekst koji bot ima
<!-- Koja polja iz memorije bot koristi u odluci (iz memorija_cita). -->

## Šta bot radi
<!-- TODO sadržaj. Ovdje ide tekst poruke (ili template) + logika izbora. -->

## Uslovi za prelaz
<!-- Svaka strelica iz prelazi_u dobija jedan bullet: kad se to dešava. -->
- `STANJE_C` — <!-- uslov -->
- `STANJE_D` — <!-- uslov -->
- `SELF` — <!-- kad ostaje u istom stanju -->

## Edge cases
<!-- Sticky note stvari koje prekidaju normalan flow. -->
- <!-- TODO -->

## Primjer poruka
<!-- TODO: 1-3 konkretna primjera kako bot odgovara. -->
