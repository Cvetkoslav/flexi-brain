---
stanje: POCETAK
opis: Prva poruka klijentu — pozdrav + pitanje za simptome
bot_odgovara: true
ulazi_iz: []
prelazi_u:
  - PRIKUPLJANJE
  - SELF
memorija_cita:
  - ime
  - vokativ
memorija_pise:
  - lokacija
  - simptomi_detalji
---

# POCETAK

## Cilj
Pozdraviti klijenta, objasniti zašto ne dajemo odmah cijenu, zatražiti lokaciju bola i trajanje.

## Kontekst koji bot ima
- `ime` (iz Facebook profila)
- `vokativ` (izvedeno iz imena)
- **Ništa drugo** — prvi kontakt

## Šta bot radi
Šalje fiksni pozdrav (3 paragrafa odvojeni praznim redom).

**Tekst poruke:**
```
Zdravo {vokativ}, drago nam je da se javljate tu gde je kvalitet 😊

Pre nego da Vam damo cenu moramo da izaberemo proizvod odgovarajući za Vas, hteli bismo prvo da postavimo par pitanja kako bismo izabrali odgovarajući za Vas i bili sigurni da će pomoći.

Gde Vam se sve javljaju bolovi i koliko vremena traju?
```

**Vokativ pravila:**
- Muška na suglasnik → `-e` (Milan → Milane, Ognjen → Ognjene)
- Muška na samoglasnik ostaju (Marko, Nikola, Luka)
- Ženska na `-a` → `-o` (Ana → Ano)
- Ostala ženska ostaju (Marija, Jelena)

## Uslovi za prelaz
- `PRIKUPLJANJE` — klijent je rekao lokaciju bola (koleno, leđa, ...) ili dao bilo koji simptom
- `SELF` — klijent pita samo cijenu i ignoriše pitanje (bot šalje kraći podsjetnik)

## Edge cases
- **Pita cijenu odmah** → ostaje POCETAK, šalje: "Imamo preko 10 proizvoda... ne mogu cijenu bez pitanja. Gdje Vas boli?"
- **Pominje rak / operaciju** → ESKALACIJA (još ne implementirano, placeholder)
- **Agresivan / psuje** → ESKALACIJA

## Primjer poruka
```
USER: Pozdrav, koliko košta za koleno?
BOT:  [ostaje POCETAK, šalje podsjetnik]

USER: Boli me koleno već 3 mjeseca
BOT:  [prelazi PRIKUPLJANJE, upisuje lokacija=koleno, simptomi_detalji="3 mjeseca"]
```
