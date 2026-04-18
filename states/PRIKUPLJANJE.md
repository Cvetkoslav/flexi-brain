---
stanje: PRIKUPLJANJE
opis: Sakuplja detalje simptoma kroz 1-2 ciljana pitanja
bot_odgovara: true
ulazi_iz:
  - POCETAK
  - UBJEDJIVANJE  # ako klijent pomene nove simptome usred UBJEDJIVANJA
prelazi_u:
  - PREPORUKA
  - SELF
memorija_cita:
  - ime
  - vokativ
  - lokacija
  - simptomi_detalji
  - probao_prije
memorija_pise:
  - lokacija
  - simptomi_detalji
  - probao_prije
  - lijekovi
  - samo_balzam
  - bez_medicinskih_garancija
---

# PRIKUPLJANJE

## Cilj
<!-- TODO: jedna rečenica. -->

## Kontekst koji bot ima
- `lokacija` (ako je klijent rekao u POCETAK)
- `simptomi_detalji` (ako je nešto već reklo)
- `probao_prije` (ako se pomenulo)

## Šta bot radi
<!-- TODO: popuniti kad Ognjen pošalje razgovore. -->

<!-- PLACEHOLDER — okvirna struktura:

1. Ako `lokacija` postoji ali nema `simptomi_detalji`:
   → pita ciljano pitanje iz mape (koleno → krckanje, leđa → trnjenje, ...)

2. Ako ima `simptomi_detalji` ali nema `probao_prije`:
   → kratka edukacija (1-2 rečenice) + "šta ste do sada probali?"

3. Ako ima lokaciju + detalje + (opciono) probao_prije:
   → prelazi PREPORUKA

-->

### Mapa lokacija → ciljano pitanje
<!-- TODO: finalne formulacije kad Ognjen pošalje razgovore. -->

| Lokacija | Pitanje |
|---|---|
| koleno | <!-- TODO --> |
| leđa / kičma / krsta | <!-- TODO --> |
| vrat | <!-- TODO --> |
| kuk | <!-- TODO --> |
| rame / ruka | <!-- TODO --> |
| više mjesta / opšte | <!-- TODO --> |

### Edukacijski paragraf po kombinaciji
<!-- TODO: kratki laički opis uzroka. -->

## Uslovi za prelaz
- `PREPORUKA` — ima `lokacija` + `simptomi_detalji`, opciono `probao_prije`
- `SELF` — jedno ili oba polja još nedostaju

## Edge cases
- **"Ne znam / svugdje malo"** → bot: "Šta Vas najviše ograničava u svakodnevnom životu?"
- **Pomene betaserc / cirkulacija / visok pritisak** → upiši `samo_balzam=true`
- **Pomene srce / dijabetes / stalne lijekove** → upiši `bez_medicinskih_garancija=true`
- **Daje sve info odjednom** (lokacija + detalji) → preskače pitanje 1, ide pravo na edukaciju + pitanje 2
- **Pomene rak / operaciju** → ESKALACIJA
- **Agresivan** → ESKALACIJA

## Primjer poruka
<!-- TODO: popuniti kad Ognjen pošalje razgovore. -->
