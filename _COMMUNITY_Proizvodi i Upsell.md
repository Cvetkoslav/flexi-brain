---
type: community
cohesion: 0.11
members: 27
---

# Proizvodi i Upsell

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[Admin endpoint rucno otvaranje razgovora (POST adminreopen)]] - document - states/ZATVORENO.md
- [[Caj za otekline (upsell pravilo)]] - document - proizvodi/caj-otekline.md
- [[Caj — proizvod (12.47 KM)]] - document - proizvodi/caj-otekline.md
- [[Cena ne pominjati dok klijent ne pita ili kaze DA]] - document - states/PREPORUKA.md
- [[Detekcija pritisnutog nerva (trnjenjeutrnulost)]] - document - proizvodi/kicma-nerv.md
- [[Flag bez_medicinskih_garancija=true (srcedijabetes)]] - document - states/PRIKUPLJANJE.md
- [[Flag samo_balzam=true (betaserccirkulacijapritisak)]] - document - states/PRIKUPLJANJE.md
- [[Kombinacija kapsule iznutra + balzam spolja (nerv)]] - document - proizvodi/kicma-nerv.md
- [[Mapa lokacija → ciljano pitanje (koleno, ledja, vrat, kuk...)]] - document - states/PRIKUPLJANJE.md
- [[Mapiranje stanje → FB labela (leadordered)]] - document - sessions/2026-04-19_2325_sesija-2026-04-19.md
- [[Pravilo vokativ iz imena (muškaženska deklinacija)]] - document - states/POCETAK.md
- [[Prikupljanje podataka ime + ulicabroj + telefon (sva 3 polja)]] - document - states/ZATVARANJE.md
- [[Prilagodjavanje preporuke po flagovima (samo_balzam, bez_medicinskih_garancija)]] - document - states/PREPORUKA.md
- [[Situacija kicmaledjaisijasbol koji se siri]] - document - proizvodi/kicma-nerv.md
- [[Situacija otekline  nateceni zglobovi]] - document - proizvodi/caj-otekline.md
- [[Situacija ponovni kupac  trazi dugorocnu podrsku]] - document - proizvodi/synchrovitals-povratnik.md
- [[Stanje POCETAK (prvi kontakt, pitanje za simptome)]] - document - states/POCETAK.md
- [[Stanje PORUCIO (zadnja potvrda, prelaz u ZATVORENO)]] - document - states/PORUCIO.md
- [[Stanje PREPORUKA (edukacija + prilagodjena preporuka + cena)]] - document - states/PREPORUKA.md
- [[Stanje PRIKUPLJANJE (max 3 pitanja, detalji simptoma)]] - document - states/PRIKUPLJANJE.md
- [[Stanje ZATVARANJE (prikupi ime, adresu, telefon)]] - document - states/ZATVARANJE.md
- [[Stanje ZATVORENO (bot ne odgovara, razgovor završen)]] - document - states/ZATVORENO.md
- [[Synchrovitals — proizvod (50.85 KM, 24h dejstvo)]] - document - proizvodi/synchrovitals-povratnik.md
- [[Synchrovitals pravilo za povratnika  dugotrajnu podršku]] - document - proizvodi/synchrovitals-povratnik.md
- [[Template za nova stanja (TEMPLATE.md)]] - document - states/_TEMPLATE.md
- [[Upsell u ZATVARANJU caj ili Synchrovitals uz narudžbu]] - document - states/ZATVARANJE.md
- [[Upsell caj uz komplet, postarina ista]] - document - proizvodi/caj-otekline.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Proizvodi_i_Upsell
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Ubjedjivanje i Argumenti]]
- 2 edges to [[_COMMUNITY_Pravila Sigurnosti]]

## Top bridge nodes
- [[Mapiranje stanje → FB labela (leadordered)]] - degree 8, connects to 2 communities
- [[Stanje PREPORUKA (edukacija + prilagodjena preporuka + cena)]] - degree 9, connects to 1 community
- [[Stanje PRIKUPLJANJE (max 3 pitanja, detalji simptoma)]] - degree 8, connects to 1 community
- [[Stanje ZATVARANJE (prikupi ime, adresu, telefon)]] - degree 6, connects to 1 community
- [[Synchrovitals — proizvod (50.85 KM, 24h dejstvo)]] - degree 4, connects to 1 community