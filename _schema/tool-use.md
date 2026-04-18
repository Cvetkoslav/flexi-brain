# Dragana tool use — schema

Dragana ne vraća plain text ni raw JSON. Koristi **Anthropic tool use** — model je prisiljen da vrati structured output prema šemi alata.

## Alat `update_state`

```python
update_state_tool = {
    "name": "update_state",
    "description": (
        "Pošalji poruku klijentu i ažuriraj stanje razgovora. "
        "Ovo je JEDINI način na koji možeš da odgovoriš klijentu."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "poruka": {
                "type": "string",
                "description": (
                    "Tekst koji će se poslati klijentu na Facebook Messenger. "
                    "Max 3 kratke rečenice, paragrafi odvojeni \\n\\n. "
                    "Uvijek se završava pitanjem osim u ZATVORENO stanju."
                )
            },
            "novo_stanje": {
                "type": "string",
                "enum": [
                    "POCETAK",
                    "PRIKUPLJANJE",
                    "PREPORUKA",
                    "UBJEDJIVANJE",
                    "ZATVARANJE",
                    "PORUCIO",
                    "ZATVORENO"
                ],
                "description": (
                    "Stanje u koje razgovor prelazi poslije ove poruke. "
                    "Ako ostaješ u istom stanju, ponovi trenutno stanje."
                )
            },
            "memorija_patch": {
                "type": "object",
                "description": (
                    "Polja koja se dodaju/mijenjaju u klijentskoj memoriji. "
                    "Šalji samo polja koja imaju NOVU vrijednost iz ove poruke. "
                    "Prigovori su lista — šalji cijelu ažuriranu listu."
                ),
                "properties": {
                    "ime": {"type": "string"},
                    "vokativ": {"type": "string"},
                    "godine": {"type": "integer"},
                    "lokacija": {"type": "string"},
                    "simptomi_detalji": {"type": "string"},
                    "lijekovi": {"type": "string"},
                    "probao_prije": {"type": "string"},
                    "prigovori": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "dato_cijena": {"type": "boolean"},
                    "samo_balzam": {"type": "boolean"},
                    "bez_medicinskih_garancija": {"type": "boolean"}
                }
            }
        },
        "required": ["poruka", "novo_stanje"]
    }
}
```

## Poziv API-ja

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=persona_prompt + "\n\n" + state_prompt + "\n\n" + memory_block,
    messages=[{"role": "user", "content": klijentova_poruka}],
    tools=[update_state_tool],
    tool_choice={"type": "tool", "name": "update_state"}
)

tool_use = next(b for b in response.content if b.type == "tool_use")
poruka = tool_use.input["poruka"]
novo_stanje = tool_use.input["novo_stanje"]
patch = tool_use.input.get("memorija_patch", {})
```

`tool_choice` forsira model da pozove baš ovaj alat — nema rizika da pošalje plain text.

## Zašto ovo radi
- Anthropic garantuje validan JSON prema `input_schema`
- `enum` na `novo_stanje` sprečava da model izmisli novo stanje
- Ako polje u `memorija_patch` nije u šemi, šema ga odbija — model ne može da izmisli random ključeve
