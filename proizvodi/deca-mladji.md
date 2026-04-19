---
situation: "Klijent pita za dete, tinejdžera, mlađu osobu ispod 16 godina"
rule: "Balzam (spolja) može kod dece preko 12 godina. Kapsule NE kod dece — preporuka od 16+. Ako je dete mlađe od 12, eskalacija ili rezervacija + 'konsultujte pedijatra'."
example_response: "Balzam se spolja može koristiti kod dece iznad 12 godina — hladi i smiruje bol, nanesite tanak sloj 1-2 puta dnevno. Kapsule su namenjene odraslima, iznad 16 godina. Koliko godina ima?"
category: proizvodi
tags: ["medicinski_flag"]
priority: 8
active: true
---

## Situacija
Klijent pita:
- "Može li za dete?"
- "Mladić od 15 godina..."
- "Sin je povredio koleno, može li?"

## Pravilo — po uzrastu

**Ispod 12 godina:**
- NE preporučuj — eskalacija ili usmeri na pedijatra
- "U ovom uzrastu preporučujem da se prvo konsultujete sa pedijatrom."

**12-15 godina:**
- **Samo balzam** (tanak sloj, 1-2 puta dnevno)
- Kapsule NE
- Postavi flag `samo_balzam=true`

**16+ godina:**
- Komplet može
- Ista preporuka kao za odrasle

## Pravilo — uvek pitaj godine
Ako klijent kaže "za dete" bez godina, **obavezno pitaj** koliko godina ima.

## Primer odgovora
Balzam se spolja može koristiti kod dece iznad 12 godina — hladi i smiruje bol, nanesite tanak sloj 1-2 puta dnevno. Kapsule su namenjene odraslima, iznad 16 godina. Koliko godina ima?
