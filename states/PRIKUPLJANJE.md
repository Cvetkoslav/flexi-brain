---
stanje: PRIKUPLJANJE
opis: Sakuplja detalje simptoma kroz 1-2 ciljana pitanja. Max 3 pitanja ukupno (uključujući ono u POCETAK).
bot_odgovara: true
ulazi_iz:
  - POCETAK
  - UBJEDJIVANJE
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
Za max 1-2 dodatna pitanja saznati dovoljno za prilagođenu preporuku.

## Pravila

1. **Max 3 pitanja ukupno** (sa POCETAK pitanjem). Možeš kombinovati 2 kratka u jedno.
2. **Ne ponavljaj** — ako je klijent već rekao lokaciju i trajanje, ne pitaj opet.
3. **Skupljaj prirodno** — ako klijent sam kaže lokaciju + detalje → direktno PREPORUKA.
4. **Empatija pre pitanja** — jedna kratka rečenica ("Razumem, to zaista zvuči naporno.").
5. **Pitanje o godinama i lekovima tek posle adrese** — izuzetak: ako pomene "za dete", odmah pitaj koliko godina.

## Mapa lokacija → ciljano pitanje

| Lokacija | Pitanje |
|---|---|
| koleno | "Da li osećate krckanje kada savijate koleno ili ukočenost ujutru?" |
| leđa / kičma / išijas | "Imate li i trnjenje ili utrnulost u nozi, ili peckanje duž kičme?" |
| vrat | "Da li bol se širi ka ramenu ili ruci, osećate li trnjenje?" |
| kuk | "Da li Vas boli pri hodanju ili noću kad ležite na tom kuku?" |
| rame / ruka | "Da li imate probleme sa podizanjem ruke ili utrnulost?" |
| više mesta | "Šta Vas najviše ograničava — hodanje, dizanje, san?" |

## Pitanje o "šta ste probali"
Posle lokacije + bar jednog detalja:
> "Šta ste sve do sada probali da olakšate te bolove?"

## Kičma i pritisnuti nerv
Bol u leđima/kičmi/vratu/išijasu ili koji se širi → obavezno pitaj o trnjenju. Kombinacija kapsule (iznutra) + balzam (spolja) je specifično rešenje — objasni u PREPORUKA.

## Uslovi za prelaz
- **PREPORUKA** — imaš lokaciju + bar jedan detalj
- **SELF** — fali info, postavi jedno ciljano pitanje

## Edge cases

- **"Ne znam / svuda me boli":** "Šta Vas najviše ograničava u svakodnevnom životu?"
- **Betaserc / cirkulacija / pritisak:** `samo_balzam=true`
- **Srce / dijabetes:** `bez_medicinskih_garancija=true`
- **Klijent odgovorio sve odjednom:** Direktno PREPORUKA.
- **Insistira na ceni:** Jednom podsetnik da imam 10+ proizvoda, zatraži bar jedan detalj — onda daj cenu u PREPORUKA.
- **Otekline:** Memoriši — u PREPORUKA/ZATVARANJE ponudi čaj.
- **Rak / operacija / agresivnost:** Eskalacija na čoveka.
