---
stanje: PREPORUKA
opis: Daje prilagođenu preporuku proizvoda + cijenu ako klijent pita ili kaže DA
bot_odgovara: true
ulazi_iz:
  - PRIKUPLJANJE
prelazi_u:
  - UBJEDJIVANJE
  - ZATVARANJE
  - PRIKUPLJANJE  # ako klijent pomene novi simptom
  - SELF
memorija_cita:
  - ime
  - vokativ
  - lokacija
  - simptomi_detalji
  - probao_prije
  - samo_balzam
  - bez_medicinskih_garancija
memorija_pise:
  - dato_cijena
  - prigovori
---

# PREPORUKA

## Cilj
<!-- TODO: jedna rečenica. -->

## Kontekst koji bot ima
Sve što je sakupljeno u PRIKUPLJANJU — puna slika klijenta.

## Šta bot radi
<!-- TODO: popuniti kad Ognjen pošalje razgovore. -->

<!-- PLACEHOLDER — okvirna struktura:

1. Prva poruka: prilagođena preporuka
   - Empatija ("jasno, sredićemo")
   - Objašnjenje šta treba (balzam / kapsule / komplet — na osnovu simptoma)
   - Social proof (procent koji se popravi, "5-6 dana")
   - Pitanje: "Da li Vam odgovara?"

2. Ako pita cijenu ili kaže DA:
   - Izreci cijenu (49.94 KM komplet / 17.84 KM balzam / ...)
   - Upiši dato_cijena=true
   - Prelazi DAO_CIJENU (UBJEDJIVANJE) — skoro uvijek treba ubjeđivanje

-->

### Mapa (simptomi → preporuka)
<!-- TODO: popuniti kad Ognjen pošalje razgovore. -->

| Kombinacija | Preporuka | Framing |
|---|---|---|
| koleno + krckanje | <!-- TODO --> | <!-- TODO --> |
| leđa + trnjenje | <!-- TODO --> | <!-- TODO --> |
| kuk + ukočenost | <!-- TODO --> | <!-- TODO --> |
| samo_balzam=true | <!-- TODO: samo balzam --> | <!-- TODO --> |

## Uslovi za prelaz
- `UBJEDJIVANJE` — klijent je dobio cijenu ali oklijeva (najčešći put)
- `ZATVARANJE` — klijent direktno kaže DA, daje se/traži adresa
- `PRIKUPLJANJE` — klijent pomene novi simptom koji mijenja preporuku
- `SELF` — klijent pita dodatno (sastav, dostava) — bot odgovara pa ostaje

## Edge cases
- **Pita cijenu prije nego bot stigne da preporuči** → bot prvo preporuka, pa cijena u sljedećoj poruci
- **Kaže "idem kod lekara"** → "Pametno! Možemo Vam rezervisati paket za kada se vratite." (ostaje PREPORUKA, nudi rezervaciju)
- **Pomene srce/dijabetes** → preporuka bez medicinskih garancija

## Primjer poruka
<!-- TODO: popuniti. -->
