---
source_file: "states/PRIKUPLJANJE.md"
type: "document"
community: "Proizvodi i Upsell"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Proizvodi_i_Upsell
---

# Stanje: PRIKUPLJANJE (max 3 pitanja, detalji simptoma)

## Connections
- [[Detekcija pritisnutog nerva (trnjenjeutrnulost)]] - `references` [EXTRACTED]
- [[Flag bez_medicinskih_garancija=true (srcedijabetes)]] - `implements` [EXTRACTED]
- [[Flag samo_balzam=true (betaserccirkulacijapritisak)]] - `implements` [EXTRACTED]
- [[Mapa lokacija → ciljano pitanje (koleno, ledja, vrat, kuk...)]] - `implements` [EXTRACTED]
- [[Mapiranje stanje → FB labela (leadordered)]] - `references` [EXTRACTED]
- [[Stanje POCETAK (prvi kontakt, pitanje za simptome)]] - `references` [EXTRACTED]
- [[Stanje PREPORUKA (edukacija + prilagodjena preporuka + cena)]] - `references` [EXTRACTED]
- [[Zabrana kvalifikacije u UBJEDJIVANJU (ne pitaj o simptomima)]] - `rationale_for` [INFERRED]

#graphify/document #graphify/EXTRACTED #community/Proizvodi_i_Upsell