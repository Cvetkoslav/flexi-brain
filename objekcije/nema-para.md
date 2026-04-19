---
situation: "Klijent više puta ponavlja da nema para ili da nije pravo vreme"
rule: "Ponudi rezervaciju: ostavi podatke, šaljemo kad budu primanja, cena ostaje ista. Posle treće iteracije NE guraj dalje — pristani da se čujete kasnije."
example_response: "Razumemo Vas potpuno. S obzirom da nam paketi idu velikom brzinom, da li želite da Vam odradimo rezervaciju? Vi nama ostavite podatke, mi Vama šaljemo kada Vam budu primanja — cena ostaje ista."
category: objekcije
tags: ["cenovni_prigovor"]
priority: 8
active: true
---

## Situacija
Klijent je rekao "nema para", "ne mogu sada", "sačekaću platu" — ili slično.

## Pravilo
1. **Prvi put** → ponudi rezervaciju (cena ostaje ista, paket čeka na njega).
2. **Drugi put** → ponovi mogućnost rezervacije kratko, bez pritiska.
3. **Treći put** → ne guraj: "Razumemo Vas. Da li Vam odgovara da se čujemo kada sredite finansijsku situaciju?"

Dodaj u `prigovori` listu: `"nema para"` (prvi put), `"nema para x2"` (drugi put), `"nema para x3"` (treći put).

**NIKAD** ne ulazi u sidrenje vrednosti ("1,6 KM dnevno") sa klijentom koji eksplicitno kaže "nema para" — on nije rekao da je skupo, rekao je da nema. To je druga objekcija.

## Primer odgovora
Razumemo Vas potpuno. S obzirom da nam paketi idu velikom brzinom, da li želite da Vam odradimo rezervaciju? Vi nama ostavite podatke, mi Vama šaljemo kada Vam budu primanja — cena ostaje ista.
