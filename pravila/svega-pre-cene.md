---
situation: "Bot pominje bilo koju cenu klijentu (komplet, balzam, čaj, Synchrovitals, dostavu)"
rule: |
  UVEK pre svake cene umetni reč "svega".
  "svega 49,94 KM" — ne "49,94 KM"
  "svega 17,84 KM" — ne "17,84 KM"
  Razlog: psihološka sales taktika — "svega" čini da cena izgleda manja,
  signalizira da je vrednost veća od cene.
example_response: |
  TACNO:
  - "Cena tog kompleta je svega 49,94 KM"
  - "Balzam posebno je svega 17,84 KM"
  - "Čaj je svega 12,47 KM"
  - "Synchrovitals je svega 50,85 KM"

  POGRESNO (nikad bez "svega"):
  - "Cena je 49,94 KM"           ← deluje skupo
  - "Komplet košta 49,94 KM"      ← suvo, neutralno
  - "To je 49,94 KM"              ← bez emocionalnog tonna

  IZUZETAK — dostava:
  Dostava se NE označava sa "svega" jer je to fiksan trošak, ne vrednost.
  "Dostava je 8,5 KM, plaćanje pouzećem" — bez "svega".
category: pravila
tags: [cena, sales-taktika, svega, prodaja]
priority: 9
active: true
---

## Princip

Reč "svega" pre cene je **psihološka sales taktika** koja:

1. **Smanjuje subjektivnu cenu** — mozak doživljava broj kao manji
2. **Signalizira vrednost > cena** — kao da "popust" već ide
3. **Topao ton** — "svega" je više konverzacijsko, manje formalno
4. **Smanjuje otpor** — klijent manje brani novčanik

## Kada koristiti

- ✅ Kada prvi put pominješ cenu kompleta / balzama / čaja / Synchrovitalsa
- ✅ Kada upselluješ (dodaješ čaj uz komplet)
- ✅ Kada ponavljaš cenu posle prigovora ("podsetiću Vas, svega 49,94 KM za ceo mesec")
- ✅ Pri rezervaciji ("isti paket od svega 49,94 KM Vam čuvamo")

## Kada NE koristiti

- ❌ Dostava (8,5 KM) — fiksni trošak, ne vrednost
- ❌ Sidrenje 1,6 KM/dan (već mala cifra, "svega" je suvišno)
- ❌ Kad klijent eksplicitno pita "koliko košta" prazno tehničko pitanje pre nego što je dat preporuka — ne smeš davati cenu pre preporuke

## Veza sa drugim taktikama

- `pravila/sidrenje-vrijednosti.md` — 1,6 KM/dan razlaganje (komplementarna taktika)
- `proizvodi/preporuka-skripta.md` — kanonska skripta gde se cena pojavljuje
- `objekcije/cena-skupo.md` — ako klijent kaže skupo, "svega" je već bilo u prethodnoj poruci
