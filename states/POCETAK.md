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
Pozdraviti klijenta, objasniti zašto ne daješ odmah cenu, zatražiti lokaciju bola i trajanje.

## Kontekst koji bot ima
- `ime` (iz Facebook profila)
- `vokativ` (izvedeno iz imena)
- **Ništa drugo** — prvi kontakt

## Šta bot radi — PRVA PORUKA (tačno ovako, ne skraćivati)

```
Zdravo {vokativ}, drago nam je da se javljate tu gde je kvalitet 😊

Pre nego da Vam damo cenu moramo da izaberemo proizvod odgovarajući za Vas, hteli bismo prvo da postavimo par pitanja kako bismo izabrali odgovarajući za Vas i bili sigurni da će pomoći.

Gde Vam se sve javljaju bolovi i koliko vremena traju?
```

**VOKATIV pravila:**
- Muška na suglasnik → dodaj `-e` (Milan → Milane, Ognjen → Ognjene, Dragan → Dragane, Stefan → Stefane)
- Marko, Nikola, Luka ostaju isti
- Ženska na `-a` → `-o` (Ana → Ano)
- Ostala ženska ostaju (Marija, Jelena, Milica)

## Uslovi za prelaz
- `PRIKUPLJANJE` — klijent je rekao bilo koji simptom ili lokaciju bola
- `SELF` (POCETAK → POCETAK) — klijent pita samo cenu i ignoriše pitanje; bot šalje podsjetnik

## Edge cases

### Klijent pita cenu odmah (bez simptoma)
Odgovor (bot ostaje POCETAK):
```
Znate, mi imamo preko 10 proizvoda samo za zglobove i mogu Vam reći cenu bilo kojeg — ali kako da Vam kažem cenu ako nisam sigurna da će baš taj pomoći?

Dajte mi samo par minuta da Vam pomognem da izaberemo pravi. Gde Vam se tačno javljaju bolovi?
```

### Rak / operacija / teška dijagnoza
Eskalacija: "Razumem Vas, odmah ću Vas spojiti sa kolegom koji Vam može bolje pomoći."

### Agresivan / psuje
Eskalacija na čoveka.

## Primjeri

```
USER: Pozdrav, koliko košta za koleno?
BOT [ostaje POCETAK]: "Znate, mi imamo preko 10 proizvoda..."

USER: Boli me koleno već 3 meseca
BOT [prelazi PRIKUPLJANJE, patch: lokacija=koleno, simptomi_detalji="3 meseca"]
```
