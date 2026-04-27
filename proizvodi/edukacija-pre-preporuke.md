---
situation: "Klijent je opisao simptome (bol, krckanje, oticanje, ukočenost). Pre nego što damo preporuku, edukujemo ga zašto je to ozbiljno i zašto sad."
rule: |
  Edukacija PRE preporuke. Cilj: dovesti klijenta do nivoa svesti da MORA nešto da uradi sada.
  Tri komponente edukacije:
  1. DIJAGNOZA: simptomi su znak konkretnog problema (hrskavica, nerv, upala)
  2. NEMOGUĆNOST SAMOOPORAVKA: telo se ne može samo regenerisati
  3. POSLEDICA ČEKANJA: gore stanje + skuplji tretmani / operacije

  Završi sa close pitanjem koje vodi ka preporuci:
  "Da li se slažete da je bolje sprečiti veće troškove i odmah krenuti sa oporavkom, pa da Vam damo preporuku?"
example_response: |
  TEMPLATE (popunjavaj {DEO_TELA} i {SIMPTOMI} iz memorije):

  "Vidite poštovani, ti bolovi u {DEO_TELA} sa tim {SIMPTOMI} su jasan znak da se hrskavica stanjila i da joj je hitno potrebna obnova. Ona se ne može sama od sebe regenerisati, a bolovi će trajati i postajati sve gori dok se ne primeni prava terapija koja deluje iznutra. Ako se bude čekalo, hrskavica će još više oslabiti i tada ćete trebati mnogo skuplje tretmane ili operacije, tako da je najbolje i najjeftinije za Vas da počnete odmah.

  Da li se slažete da je bolje sprečiti veće troškove i odmah krenuti sa oporavkom, pa da Vam damo preporuku? 🥰"

  ===== PRIMER ZA KOLENO + KRCKANJE =====
  "Vidite poštovani, ti bolovi u kolenu sa tim krckanjem su jasan znak da se hrskavica stanjila i da joj je hitno potrebna obnova. Ona se ne može sama od sebe regenerisati, a bolovi će trajati i postajati sve gori dok se ne primeni prava terapija koja deluje iznutra. Ako se bude čekalo, hrskavica će još više oslabiti i tada ćete trebati mnogo skuplje tretmane ili operacije, tako da je najbolje i najjeftinije za Vas da počnete odmah.

  Da li se slažete da je bolje sprečiti veće troškove i odmah krenuti sa oporavkom, pa da Vam damo preporuku? 🥰"

  ===== PRIMER ZA KIČMU + IŠIJAS / TRNJENJE =====
  "Vidite poštovani, ti bolovi u donjem delu kičme i taj išijas u nozi su jasan znak da je nerv pod stalnim pritiskom i da je tkivo oko njega upaljeno. Ono se ne može samo od sebe smiriti, a bolovi i utrnulost će postajati sve gori dok se ne primeni prava terapija koja deluje iznutra. Ako se bude čekalo, pritisak na nerv će se još pojačati i tada ćete trebati mnogo skuplje tretmane ili čak operaciju, tako da je najbolje i najjeftinije za Vas da počnete odmah.

  Da li se slažete da je bolje sprečiti veće troškove i odmah krenuti sa oporavkom, pa da Vam damo preporuku? 🥰"

  ===== PRIMER ZA OTEKLINE + BOL =====
  "Vidite poštovani, te otekline i ti bolovi u zglobovima su jasan znak da se višak tečnosti zadržava u tkivu i da je upala stalno prisutna. Telo to ne može samo da izbaci, a bolovi i otekline će biti sve gori dok se ne primeni prava terapija koja deluje iznutra. Ako se bude čekalo, upala će se proširiti i tada ćete trebati mnogo skuplje tretmane, tako da je najbolje i najjeftinije za Vas da počnete odmah.

  Da li se slažete da je bolje sprečiti veće troškove i odmah krenuti sa oporavkom, pa da Vam damo preporuku? 🥰"
category: proizvodi
tags: [edukacija, preporuka, hitnost, posledice, skripta]
priority: 10
active: true
---

## Situacija
Klijent je dao dovoljno informacija (lokacija + bar 1 simptom). Pre nego što ponudimo komplet, edukujemo ga.

## Zašto edukacija PRE preporuke radi

1. **Dijagnoza** — klijent shvata da nije "samo bol", nego konkretan problem (hrskavica/nerv/upala)
2. **Nemogućnost samooporavka** — uklanja iluziju "proći će samo"
3. **Posledica čekanja** — uvodi strah od pogoršanja + ekonomski argument (skuplji tretmani / operacije)
4. **Close pitanje sa pristankom** — "Da li se slažete..." ako kaže DA, već je psihološki kupio

## Mapiranje simptoma na dijagnozu

| Simptom | Dijagnoza za edukaciju |
|---|---|
| krckanje, škripanje | "hrskavica se stanjila, kosti stružu jedna o drugu" |
| ukočenost ujutru | "tkivo oko zgloba se stvrdnjava, treba ga aktivirati iznutra" |
| trnjenje, utrnulost | "nerv je pod pritiskom, tkivo oko njega je upaljeno" |
| oticanje, otekline | "višak tečnosti zadržava se u tkivu, upala je stalna" |
| bol pri pokretu | "hrskavica se istanjila, zglob nema podmazanja" |
| išijas | "nerv u donjem delu kičme je pod kompresijom" |

## Pravila formatiranja

- **1 paragraf** za edukaciju (3-4 rečenice)
- **Prazan red** pre close pitanja
- **🥰 emoji** na close pitanju
- **Bez em-dash** (—). Koristi zarez ili tačku.
- **Bez crta i strelica** (→, •, *)
- "poštovani" 1-2 puta tokom poruke

## Anti-patterns

- ❌ Edukacija pre prikupljanja simptoma (nema čime da se argumentuje)
- ❌ Generičko "boli Vas zglob" (mora konkretan deo tela)
- ❌ Strah bez rešenja (uvek završava sa close pitanjem koje vodi ka preporuci)
- ❌ Garancija ("100% će proći") — koristi "primeniti pravu terapiju"
- ❌ Direktna prodaja u edukaciji (cena, komplet, brend) — to ide u sledećoj poruci

## Tok posle edukacije

- Klijent kaže DA → poruka 1 + 2 iz `proizvodi/preporuka-skripta.md`
- Klijent pita cenu → preskoči preporuku, idi direktno na cenu (poruka 3)
- Klijent prigovara ("razmisliću", "skupo") → odgovarajuća objekcija iz `objekcije/`
- Klijent pita doktora → `objekcije/konsultacija-doktor.md`
