---
type: hub
---

# Flexi Brain — Index

Knowledge base i session graf za Flexi Bot. Bot čita iz `kb/` (sinhronizovano sa ovim vault-om).

## Bot-visible KB kategorije (čitaju se svaki razgovor)

### `states/` — 7 stanja prodajnog razgovora
- [[states/POCETAK]] — prva poruka (pozdrav + pitanje za simptome)
- [[states/PRIKUPLJANJE]] — max 3 pitanja o simptomima
- [[states/PREPORUKA]] — edukacija + prilagođena ponuda
- [[states/UBJEDJIVANJE]] — dijagnoza prigovora (povjerenje vs cena)
- [[states/ZATVARANJE]] — traženje adrese bez pauze
- [[states/PORUCIO]] — zadnja potvrda
- [[states/ZATVORENO]] — bot ne odgovara

### `proizvodi/` — informacije o proizvodima (10 fajlova)
- [[proizvodi/balzam-kapsule]] — glavni komplet (49,94 KM)
- [[proizvodi/betaserc-cirkulacija]] — samo_balzam flag
- [[proizvodi/caj-otekline]] — čaj upsell (12,47 KM)
- [[proizvodi/certifikati-sigurnost]] — 29 godina, ministarstvo
- [[proizvodi/kicma-nerv]] — detekcija pritisnutog nerva
- [[proizvodi/synchrovitals-povratnik]] — za povratnike (50,85 KM)
- [[proizvodi/primena-proizvoda]] — kako se koristi
- [[proizvodi/trajanje-rezultata]] — kada se vide rezultati
- [[proizvodi/trudnoca-dojenje]] — medicinski flag
- [[proizvodi/deca-mladji]] — po uzrastu

### `objekcije/` — kako odgovoriti na prigovore (7 fajlova)
- [[objekcije/cena-skupo]] — sidrenje vrednosti
- [[objekcije/nema-para]] — rezervacija + ne guraj posle 3x
- [[objekcije/skepticizam]] — Dragana iz iskustva
- [[objekcije/sve-probao]] — kombinacija iznutra+spolja
- [[objekcije/konsultacija-doktor]] — pohvali + rezervacija
- [[objekcije/popust]] — nema popusta → upsell
- [[objekcije/sta-ako-ne-pomogne]] — balzam 5min + 29god firma

### `zatvaranje/` — zatvaranje prodaje (5 fajlova)
- [[zatvaranje/klijent-kaze-da]] — bez pauze, traži adresu
- [[zatvaranje/upsell]] — čaj / Synchrovitals
- [[zatvaranje/urgencija]] — jednom po razgovoru
- [[zatvaranje/razmislicu]] — dijagnoza prigovora
- [[zatvaranje/odgada]] — ne potvrđuj odgodu

### `pravila/` — opšta prodajna pravila (4 fajla)
- [[pravila/prva-poruka]] — tačan tekst pozdrava
- [[pravila/cena-bez-simptoma]] — 10+ proizvoda
- [[pravila/sidrenje-vrijednosti]] — 1,6 KM dnevno
- [[pravila/eskalacija]] — rak/operacija/agresija → čovek

### `stil-govora/` — ton i jezik (6 fajlova)
- [[stil-govora/ekavski-obavezno]] — priority 10, globalno
- [[stil-govora/empatija-pre-prodaje]] — 1 rečenica empatije
- [[stil-govora/kratke-poruke]] — max 2-3 rečenice
- [[stil-govora/max-3-pitanja]] — ne maltretiraj klijenta
- [[stil-govora/nema-laznih-obecanja]] — bez garancija
- [[stil-govora/nema-ponavljanja]] — čitaj istoriju

### `struktura/` — format i tok (3 fajla)
- [[struktura/format-poruka]] — prazan red između delova
- [[struktura/dostava]] — 1-2 dana, 8,5 KM, pouzeće
- [[struktura/downsell-balzam]] — last resort samo balzam

---

## Non-bot kategorije (Ognjenova memorija, ne čita bot)

### Teme
- [[teme/Dragana]] · [[teme/Followup]] · [[teme/Reaktivacija]]
- [[teme/Database]] · [[teme/Briefing]] · [[teme/AdminHandler]]

### Meta
- [[meta/Feedback-Ognjen]] · [[meta/TODO]] · [[meta/Ciljevi]] · [[meta/Planirano-a-nije]]

### Sessions
- [[sessions/2026-04-19_2325_sesija-2026-04-19]]
- [[sessions/2026-04-18_1722_sesija-2026-04-18]]
- [[sessions/2026-04-18_1344_sesija-2026-04-18]]
- [[sessions/2026-04-17_1713_sesija-2026-04-17]]

---

## Workflow
1. Ognjen edituje u Obsidianu (ovaj vault)
2. `cp -r flexi-brain/* flexi-bot/kb/` (ili automatski sync)
3. `git push` → Railway auto-deploy
4. Dragana čita sveža pravila pri sledećem odgovoru


## Najnovije sesije
- [[sessions/2026-04-19_2327_sesija-2026-04-19]] — 19.04.2026. 23:27 (Drugo)
