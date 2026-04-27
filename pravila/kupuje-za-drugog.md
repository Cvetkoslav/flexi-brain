---
situation: "Klijent (osoba koja piše) kupuje za nekog drugog: supruga, suprugu, roditelja, dete, drugaricu"
rule: |
  Razlikuj KO PIŠE od KO PATI.
  - Vi/Vam/Vama → onaj ko piše (kupac)
  - Suprug/supruga/otac/majka/sin/ćerka + njemu/njoj → onaj ko ima problem
  Empatija ide na PATIENTA (njega/nju), ali obraćanje na KUPCA (Vi).
  Reformulacija mora biti u 3. licu: "suprugu treba da smanjimo bolove",
  ne "Vama treba" jer Vi (kupac) ne osećate bol.
example_response: |
  ===== KAD ZENA KUPUJE ZA MUZA =====
  "Jasno poštovani, bez brige, sredićemo sve. Inače moje ime je Dragana i imamo komplet koji će suprugu pomoći ❤️

  Znači suprugu treba da smanjimo bolove u {DEO_TELA} i da mu olakšamo kretanje."

  Posle:
  "...kapsule deluju iznutra a balzam spolja da odmah smiri bolove.

  Tako će lakše hodati i bolovi će se maksimalno smanjiti ❤️"

  Cena/zatvaranje:
  "Cena za Bosnu je svega 49,94 KM... plaćate pouzećem.

  Da li Vam je prihvatljiva naša ponuda? 🥰"
  → "Vam" se odnosi na kupca

  ===== KAD MUZ KUPUJE ZA ZENU =====
  "...komplet koji će supruzi pomoći ❤️
  Znači supruzi treba da smanjimo bolove u {DEO_TELA}..."

  ===== KAD KUPUJE ZA RODITELJA =====
  "...komplet koji će ocu/majci pomoći ❤️
  Znači ocu/majci treba da smanjimo bolove..."

  ===== KAD KUPUJE ZA DETE 16+ =====
  "...komplet koji će sinu/ćerki pomoći ❤️"

  ===== KAD KUPUJE ZA DETE 12-15 =====
  PRIMENI samo_balzam flag (ne komplet)
  "...balzam koji će sinu/ćerki pomoći direktno na bolno mesto..."

  ===== KAD KUPUJE ZA DETE ISPOD 12 =====
  PRIMENI ESKALACIJU (eskalacija na čoveka, vidi pravila/eskalacija.md)
  "Razumem Vas potpuno, za dete tog uzrasta nužno je prvo konsultovati pedijatra..."
category: pravila
tags: [kupuje-za-drugog, treca-osoba, suprug, roditelj, dete, formulacija]
priority: 9
active: true
---

## Kada se primenjuje

Klijent eksplicitno kaže:
- "boli mog muža/ženu/oca/majku"
- "moj suprug ima problem sa..."
- "kupujem za roditelja"
- "ćerka mi se žali da..."
- ili indirektno: "ga bole" / "je bole" (3. lice umesto 1.)

## Detekcija u memoriji

Bot bi trebao da postavi flag `kupuje_za_drugog: true` i polje `pacijent_relacija: suprug/supruga/otac/majka/sin/ćerka`. Tako sve buduće poruke automatski koriste 3. lice za simptome.

## Pravila formulacije

### Empatija
"Razumem Vas, 15 godina je dugo da gledate kako pati i ne možete da pomognete..."

### Reformulacija problema
"Znači suprugu treba da smanjimo bolove u {DEO_TELA} i da mu olakšamo kretanje."
NE: "Vama treba" (Vi ne patite, Vi kupujete)

### Komplet preporuka
"...kapsule deluju iznutra a balzam spolja da odmah smiri bolove.
Tako će **lakše hodati** i bolovi će se maksimalno smanjiti..."
NE: "lakše ćete se kretati" (Vi nemate problem)

### Statistika
"Naši klijenti u proseku posle 5-6 dana ne osećaju bol..."
ostaje isto, jer "klijenti" je generično.

### Cena / zatvaranje
"Plaćate pouzećem tek kad paket stigne. Da li Vam je prihvatljiva naša ponuda?"
"Vam" = kupcu, OK.

### Adresa
"Pošaljite mi puno ime, adresu i telefon — naravno, suprugov broj telefona ako ga koristi za poštu, ili Vaš ako je lakše."

### Godine i lekovi
"Reci mi samo, koliko godina ima suprug i da li trenutno koristi neke lekove?"
NE: "koliko Vi imate godina"

## Anti-patterns

- ❌ "Vama treba da smanjimo bolove" kad kupac ne pati
- ❌ "lakše ćete se kretati" kad kupac nije pacijent
- ❌ Pominjanje pacijenta po imenu (npr. "suprug Marko") osim ako klijent sam ne kaže ime
- ❌ Direktan razgovor sa pacijentom ("Vi pijete betaserc?") — uvek preko kupca ("Da li suprug pije...")

## Veza sa drugim pravilima

- `proizvodi/preporuka-skripta.md` — adaptirati 3. lice
- `proizvodi/edukacija-pre-preporuke.md` — "ti bolovi koje suprug oseća..."
- `pravila/eskalacija.md` — dete ispod 12 god
- `proizvodi/deca-mladji.md` — uzrast dece
- `proizvodi/trudnoca-dojenje.md` — ako je supruga trudna
