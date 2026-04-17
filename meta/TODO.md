---
type: meta-todo
---

# TODO — Aktivne obaveze

**Povezano:** [[INDEX]]

## Prioritetno

- [ ] **Dragana faze state machine** — PRVA_PORUKA → PITANJA → PONUDA → UBEDJIVANJE → DOGOVARANJE
  - Dodati `phase` field u client_states
  - Phase-specific block u system prompt
  - Enforcement max 3 pitanja na Python strani (ne samo u promptu)
  - Strict ekavski zabranka u PERSONA_PROMPT

## Planirano

- [ ] Slike kapsule i balzam — pravi URLovi (7 CUSTOMER_IMAGES + 2 product images)
- [ ] Dragana faza UBEDJIVANJE — kada klijent odbije ponudu, bot prelazi u ubedivanje (ne pita nova pitanja)
- [ ] Migracija 33 seed KB entry-ja iz `brain/seed_knowledge.py` u `.md` fajlove

## Na čekanju

- [ ] Dragana faze — odobreno, implementacija sledeća sesija

---

_(automatski ažurirano via /compact hook)_
