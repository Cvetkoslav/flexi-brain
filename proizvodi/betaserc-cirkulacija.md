---
situation: "Klijent pije Betaserc, lekove za cirkulaciju, krvni pritisak ili za vrtoglavicu"
rule: "SAMO balzam preporučiti (17,84 KM). Kapsule nisu kompatibilne sa lekovima za cirkulaciju. Postavi flag samo_balzam=true u memoriji. NE pokušavaj komplet ni kao downsell."
example_response: "Zahvaljujući Vašoj terapiji, u Vašem slučaju preporučujem samo balzam — direktno na bolno mesto, bezbedan uz sve lekove. Balzam posebno košta 17,84 KM. Da li Vam to odgovara?"
category: proizvodi
tags: ["treba_edukaciju", "medicinski_flag"]
priority: 10
active: true
---

## Situacija
Klijent pominje:
- Betaserc
- lekove za cirkulaciju
- lekove za krvni pritisak
- lekove za vrtoglavicu
- antikoagulanse (Farin, Sintrom, razređivači krvi)

## Pravilo
1. Postavi flag `samo_balzam=true` u memoriji klijenta.
2. **SAMO balzam preporuči** (17,84 KM) — kapsule NISU kompatibilne.
3. NE pominji komplet čak ni kao upsell/downsell.
4. Ako klijent pita "zašto samo balzam" → "Zato što je balzam spoljni i bezbedan uz Vašu terapiju, dok bi kapsule mogle da ometaju efekat lekova za cirkulaciju."

## Primer odgovora
Zahvaljujući Vašoj terapiji, u Vašem slučaju preporučujem samo balzam — direktno na bolno mesto, bezbedan uz sve lekove. Balzam posebno košta 17,84 KM. Da li Vam to odgovara?
