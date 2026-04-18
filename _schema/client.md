# Client memorija — schema

Memorija svakog klijenta živi u **SQLite** (`/data/data.db` na Railway volume).
Obsidian `clients/{sender_id}.md` je samo **dnevni eksport** za Ognjenov vizuelni pregled — bot ga ne čita.

## SQLite tabela `clients`

| Kolona | Tip | Opis |
|---|---|---|
| `sender_id` | TEXT PK | Facebook sender ID |
| `stanje` | TEXT | Trenutno stanje (POCETAK, PRIKUPLJANJE, ...) |
| `ime` | TEXT | Ime iz Facebook profila |
| `vokativ` | TEXT | Ime u vokativu (Milane, Ano, ...) |
| `godine` | INTEGER | Ako klijent pomene, inače NULL |
| `lokacija` | TEXT | Gdje ga boli (koleno / leđa / vrat / ...) |
| `simptomi_detalji` | TEXT | Krckanje, trnjenje, otekline, ukočenost, trajanje |
| `lijekovi` | TEXT | Betaserc, tablete za pritisak, ... (flag-ovi za kontraindikacije) |
| `probao_prije` | TEXT | "Svašta sam probao i ništa ne pomaže" / "Ništa još" / ... |
| `prigovori` | JSON | Lista prigovora: `["nema para", "ne vjeruje u prirodno"]` |
| `dato_cijena` | BOOLEAN | Da li je bot već rekao cijenu |
| `samo_balzam` | BOOLEAN | Flag: preporuči samo balzam (betaserc/cirkulacija) |
| `bez_medicinskih_garancija` | BOOLEAN | Flag: ne obećavaj rezultat (srce/dijabetes) |
| `first_contact_ts` | TEXT | ISO timestamp prvog kontakta |
| `last_seen_ts` | TEXT | ISO timestamp zadnje klijentove poruke |
| `last_bot_ts` | TEXT | ISO timestamp zadnje bot poruke |
| `message_seen` | BOOLEAN | Da li je klijent vidio zadnju bot poruku |
| `follow_up_index` | INTEGER | Koji je follow-up u redu (0-N) |
| `follow_ups_today` | INTEGER | Koliko follow-upa je poslato danas |
| `memorija_md` | TEXT | Free-text sažetak razgovora (bot dopunjuje) |

## Tabela `messages` (log, nije za kontekst)

| Kolona | Tip | Opis |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | |
| `sender_id` | TEXT | FK na clients |
| `role` | TEXT | "user" ili "assistant" |
| `text` | TEXT | |
| `ts` | TEXT | ISO timestamp |

Koristi se za admin endpoint `/admin/history/{sid}` i eventualnu obuku, **ne** za prompt kontekst (taj dolazi iz strukturirane memorije).

## Obsidian eksport format (`clients/{sid}.md`)

Dnevni cron eksportuje svakog klijenta u markdown za Ognjenov pregled:

```markdown
---
sender_id: 1234567890
ime: Milan
vokativ: Milane
stanje: UBJEDJIVANJE
lokacija: koleno
simptomi_detalji: krckanje, 3 mjeseca
probao_prije: svašta sam probao
prigovori:
  - nema para
dato_cijena: true
first_contact: 2026-04-15T10:23:00
last_seen: 2026-04-17T14:12:00
---

## Sažetak
(sadržaj memorija_md polja)

## Poruke
- 2026-04-15 10:23 [user] Pozdrav, koliko košta za koleno?
- 2026-04-15 10:24 [bot] Zdravo Milane...
```
