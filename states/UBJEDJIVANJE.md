---
stanje: UBJEDJIVANJE
opis: Klijent oklijeva poslije cijene — bot razlikuje povjerenje vs. cijena i vodi ka DA ili rezervaciji
bot_odgovara: true
ulazi_iz:
  - PREPORUKA
prelazi_u:
  - ZATVARANJE
  - PRIKUPLJANJE  # ako pomene novi simptom
  - SELF
memorija_cita:
  - ime
  - vokativ
  - lokacija
  - simptomi_detalji
  - probao_prije
  - prigovori
  - dato_cijena
memorija_pise:
  - prigovori
  - dato_cijena  # ako tek sad daje cijenu
---

# UBJEDJIVANJE

## Cilj
<!-- TODO: jedna rečenica. -->

## Kontekst koji bot ima
Puna slika + `prigovori` (lista prethodnih prigovora iz razgovora).

## Šta bot radi
<!-- TODO: popuniti kad Ognjen pošalje 5-10 primjera razgovora iz ove faze. -->

<!-- PLACEHOLDER — okvirna struktura iz starih SYSTEM_PROMPT pravila (verifikovati nad stvarnim razgovorima):

### Korak 1 — Dijagnoza prigovora
Pitanje: "Recite iskreno — da li Vas muči to da proizvod neće pomoći, ili je samo cena u pitanju?"

### Korak 2A — POVJERENJE (ako sumnja u efekat/sastav)
- Daj sastav (hondroitin, kamfor, mentol, papaja enzim, gavez, eterična ulja)
- Sertifikat ministarstva zdravlja, fiskalni račun
- "29 godina na tržištu, 68 zemalja"
- Lično iskustvo ("ja lično koristim")
- Pitanje: "Da li Vam je sada jasnije?"
- Ako kaže "jasnije mi je" / "razumijem" → prelazi ZATVARANJE

### Korak 2B — CIJENA (ako kaže nema para)
- NIKAD ne ulazi u matematiku "X din dnevno" — on je već rekao nema para, ne oklijeva oko vrijednosti
- Ponudi rezervaciju: "Vi nama ostavite podatke, šaljemo kada Vam budu primanja — cijena ostaje ista"
- Ako pristane → prelazi ZATVARANJE (sa flag-om rezervacija=true)

### Korak 3 — Ako odbije rezervaciju
Znači problem je i dalje povjerenje: "Šta Vam konkretno ne odgovara?" — čekaj odgovor, rješavaj samo taj razlog.

### Korak 4 — "Nema para" treći put
"Razumemo Vas. Da li Vam odgovara da se čujemo kada sredite finansijsku situaciju?" — ne guraj dalje, ali ostaje UBJEDJIVANJE (bot NE zatvara konverzaciju).

-->

## Uslovi za prelaz
- `ZATVARANJE` — klijent kaže DA (eksplicitno ili "u redu, kako šaljete") ili pristane na rezervaciju
- `PRIKUPLJANJE` — klijent pomene novi simptom koji nismo znali
- `SELF` — klijent iznosi prigovor, bot odgovara, čeka sljedeću reakciju

## Edge cases
- **"Idem kod lekara"** → "Pametno! Rezervišemo Vam paket za kada se vratite." (ne zatvaraj)
- **"Treba mi vremena da razmislim"** → ponudi rezervaciju, ne guraj
- **"Skupo je"** (bez "nemam para") → preformulacija vrijednosti ("X KM za 30 dana tretmana")
- **Pitanja o sastavu** → POVJERENJE grana
- **"Već sam probao svašta"** → POVJERENJE grana, naglasak na sertifikat i razlici

## Primjer poruka
<!-- TODO: popuniti iz Ognjenovih stvarnih razgovora. -->
