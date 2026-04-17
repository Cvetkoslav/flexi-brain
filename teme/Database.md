---
type: hub-tema
---

# Database — Postgres schema

**Povezano:** [[INDEX]]

## Šta je
PostgreSQL na Railway-u. Glavna tabela `client_states` (po PSID-u) + `conversations` + `knowledge_base` + `reactivation_msg_stats`.

## Fajlovi
- `db.py` — init_db(), get_or_init_state(), persist_state(), load_all()
- `brain/git_sync.py` — sync KB iz Git repo-a u `knowledge_base` tabelu
- `brain/seed_knowledge.py` — inicijalnih 33 KB entry-ja

## Migracije
Idempotentan `ALTER TABLE ADD COLUMN IF NOT EXISTS` pattern za sve nove kolone. `CREATE TABLE IF NOT EXISTS` za nove tabele.

## Sesije
_(automatski ažurirano)_
