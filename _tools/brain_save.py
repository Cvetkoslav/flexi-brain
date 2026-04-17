"""
PreCompact hook za Claude Code.
Ekstraktuje session izveštaj iz transcripta i zapisuje u Obsidian vault pre kompaktovanja.

Kako radi:
  Claude Code šalje JSON payload na stdin pre /compact.
  Ova skripta generiše izveštaj, zapisuje ga, ažurira INDEX + teme + meta, pa push-uje na GitHub.
  Mora exit 0 — ne sme nikad blokirati /compact.

Poziv:
  echo '<json>' | python brain_save.py
  ili direktno (za test): python brain_save.py --test
"""
import json
import logging
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[brain_save] %(levelname)s %(message)s")
log = logging.getLogger(__name__)

VAULT       = Path(__file__).parent.parent
SESSIONS    = VAULT / "sessions"
TEME        = VAULT / "teme"
META        = VAULT / "meta"
PROMPTS_DIR = Path(__file__).parent / "prompts"
EXTRACT_PROMPT = PROMPTS_DIR / "extract_session.txt"

VALID_TEME = {
    "Dragana", "Reaktivacija", "Followup", "Database",
    "Briefing", "AdminHandler", "Brain", "Meta", "Drugo"
}

MAX_TRANSCRIPT_CHARS = 40_000   # sigurnosni cap za Claude API
MAX_SESSIONS_IN_INDEX = 25      # koliko sesija prikazujemo u INDEX.md


def _safe_exit(code: int = 0):
    sys.exit(code)


def _read_transcript(path: str) -> str:
    """Čita .jsonl transcript i vraća user/assistant poruke kao čist tekst."""
    try:
        lines = []
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    obj = json.loads(raw)
                except json.JSONDecodeError:
                    continue

                msg_type = obj.get("type") or ""
                # Podržavamo oba formata: {role, content} i {type, message}
                if msg_type in ("user", "assistant"):
                    role = msg_type
                    content = obj.get("message") or obj.get("content") or ""
                elif isinstance(obj.get("role"), str):
                    role = obj["role"]
                    content = obj.get("content") or ""
                else:
                    continue

                if isinstance(content, list):
                    # content može biti lista blokova
                    text_parts = []
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            text_parts.append(block.get("text", ""))
                        elif isinstance(block, str):
                            text_parts.append(block)
                    content = " ".join(text_parts)

                if content and role in ("user", "assistant"):
                    prefix = "KORISNIK" if role == "user" else "CLAUDE"
                    lines.append(f"[{prefix}]: {content.strip()}")

        transcript = "\n\n".join(lines)
        # Ograniči dužinu
        if len(transcript) > MAX_TRANSCRIPT_CHARS:
            transcript = transcript[-MAX_TRANSCRIPT_CHARS:]
            log.warning(f"Transcript skraćen na {MAX_TRANSCRIPT_CHARS} znakova.")
        return transcript

    except Exception as e:
        log.error(f"Greška pri čitanju transcripta {path}: {e}")
        return ""


def _call_claude(transcript: str) -> str:
    """Poziva Claude CLI da generiše session izveštaj."""
    prompt_text = EXTRACT_PROMPT.read_text(encoding="utf-8")
    full_prompt = f"{prompt_text}\n\n---TRANSCRIPT---\n{transcript}\n---KRAJ---"

    try:
        result = subprocess.run(
            ["claude", "-p", full_prompt, "--model", "claude-sonnet-4-6", "--output-format", "text"],
            capture_output=True,
            text=True,
            timeout=120,
            encoding="utf-8"
        )
        if result.returncode != 0:
            log.error(f"Claude CLI greška: {result.stderr[:500]}")
            return ""
        return result.stdout.strip()

    except FileNotFoundError:
        log.error("'claude' CLI nije pronađen u PATH-u.")
        return ""
    except subprocess.TimeoutExpired:
        log.error("Claude CLI timeout (120s).")
        return ""
    except Exception as e:
        log.error(f"Claude CLI izuzetak: {e}")
        return ""


def _parse_metadata(report_md: str) -> dict:
    """Izvlači slug i temu iz poslednjih linija izveštaja."""
    slug = "sesija"
    tema = "Drugo"

    for line in reversed(report_md.splitlines()):
        line = line.strip()
        if line.startswith("SLUG:"):
            raw = line[5:].strip().lower()
            # Sanitizuj — samo a-z, 0-9, crtice
            raw = re.sub(r"[^a-z0-9\-]", "-", raw)
            raw = re.sub(r"-+", "-", raw).strip("-")
            if raw:
                slug = raw[:60]
        elif line.startswith("TEMA:"):
            raw = line[5:].strip()
            if raw in VALID_TEME:
                tema = raw

    return {"slug": slug, "tema": tema}


def _write_session(report_md: str, slug: str, now: datetime) -> Path | None:
    """Zapisuje session fajl u sessions/."""
    SESSIONS.mkdir(exist_ok=True)
    fname = f"{now:%Y-%m-%d_%H%M}_{slug}.md"
    fpath = SESSIONS / fname

    # Ukloni SLUG:/TEMA: linije iz krajnjeg fajla (meta info za parser)
    lines = [l for l in report_md.splitlines()
             if not l.strip().startswith("SLUG:") and not l.strip().startswith("TEMA:")]
    clean = "\n".join(lines).rstrip() + "\n"

    try:
        fpath.write_text(clean, encoding="utf-8")
        log.info(f"Zapisao session: {fname}")
        return fpath
    except Exception as e:
        log.error(f"Greška pri zapisivanju sesije: {e}")
        return None


def _update_index(session_fname: str, slug: str, tema: str, now: datetime):
    """Prepend-uje link nove sesije u INDEX.md pod 'Najnovije sesije'."""
    index_path = VAULT / "INDEX.md"
    if not index_path.exists():
        log.warning("INDEX.md ne postoji, preskačem ažuriranje.")
        return

    try:
        content = index_path.read_text(encoding="utf-8")
        datum_str = now.strftime("%d.%m.%Y. %H:%M")
        novi_link = f"- [[sessions/{session_fname.replace('.md', '')}]] — {datum_str} ({tema})"

        marker = "## Najnovije sesije"
        if marker not in content:
            content += f"\n\n{marker}\n{novi_link}\n"
        else:
            # Ubaci link ispod marker linije
            idx = content.index(marker) + len(marker)
            # Nađi kraj te linije
            newline_pos = content.find("\n", idx)
            if newline_pos == -1:
                newline_pos = len(content)
            # Skupi postojeće linkove
            after = content[newline_pos:]
            existing_links = [l for l in after.split("\n") if l.strip().startswith("- [[sessions/")]
            # Zadrži max MAX_SESSIONS_IN_INDEX
            all_links = [novi_link] + existing_links
            all_links = all_links[:MAX_SESSIONS_IN_INDEX]
            links_block = "\n".join(all_links)
            # Sve što nije sesija-link ostaje
            non_links = [l for l in after.split("\n")
                         if not l.strip().startswith("- [[sessions/")]
            new_after = "\n" + links_block + "\n".join(non_links)
            content = content[:newline_pos] + new_after

        index_path.write_text(content, encoding="utf-8")
        log.info("INDEX.md ažuriran.")
    except Exception as e:
        log.error(f"Greška pri ažuriranju INDEX.md: {e}")


def _update_tema(tema: str, session_fname: str, now: datetime):
    """Prepend-uje link sesije u teme/<tema>.md."""
    tema_path = TEME / f"{tema}.md"
    if not tema_path.exists():
        log.warning(f"teme/{tema}.md ne postoji, preskačem.")
        return

    try:
        content = tema_path.read_text(encoding="utf-8")
        datum_str = now.strftime("%d.%m.%Y. %H:%M")
        novi_link = f"- [[sessions/{session_fname.replace('.md', '')}]] — {datum_str}"

        marker = "## Sesije"
        if marker not in content:
            content += f"\n\n{marker}\n{novi_link}\n"
        else:
            idx = content.index(marker) + len(marker)
            newline_pos = content.find("\n", idx)
            if newline_pos == -1:
                newline_pos = len(content)
            after = content[newline_pos:]
            existing = [l for l in after.split("\n") if l.strip().startswith("- [[sessions/")]
            all_links = [novi_link] + existing
            all_links = all_links[:15]
            non_links = [l for l in after.split("\n") if not l.strip().startswith("- [[sessions/")]
            content = content[:newline_pos] + "\n" + "\n".join(all_links) + "\n".join(non_links)

        tema_path.write_text(content, encoding="utf-8")
        log.info(f"teme/{tema}.md ažuriran.")
    except Exception as e:
        log.error(f"Greška pri ažuriranju teme/{tema}.md: {e}")


def _extract_and_append_feedback(report_md: str):
    """Parsira Feedback sekciju iz izveštaja i dopunjuje meta/Feedback-Ognjen.md."""
    feedback_path = META / "Feedback-Ognjen.md"
    if not feedback_path.exists():
        return

    try:
        match = re.search(r"## Feedback od Ognjena\n(.*?)(?=\n##|\Z)", report_md, re.DOTALL)
        if not match:
            return
        block = match.group(1).strip()
        if not block or block == "—":
            return
        # Filtriraj samo linije sa citatima
        citati = [l for l in block.splitlines() if '"' in l or "'" in l]
        if not citati:
            return
        existing = feedback_path.read_text(encoding="utf-8")
        addition = "\n## " + datetime.now().strftime("%d.%m.%Y.") + "\n" + "\n".join(citati) + "\n"
        feedback_path.write_text(existing.rstrip() + "\n" + addition, encoding="utf-8")
        log.info(f"meta/Feedback-Ognjen.md ažuriran sa {len(citati)} citat(a).")
    except Exception as e:
        log.error(f"Greška pri ažuriranju Feedback-Ognjen.md: {e}")


def _extract_and_append_todo(report_md: str):
    """Parsira TODO sekciju i dopunjuje meta/TODO.md."""
    todo_path = META / "TODO.md"
    if not todo_path.exists():
        return

    try:
        match = re.search(r"## TODO za sledeći put\n(.*?)(?=\n##|\Z)", report_md, re.DOTALL)
        if not match:
            return
        block = match.group(1).strip()
        if not block or block == "—":
            return
        items = [l for l in block.splitlines() if l.strip().startswith("- [")]
        if not items:
            return
        existing = todo_path.read_text(encoding="utf-8")
        addition = "\n### " + datetime.now().strftime("%d.%m.%Y.") + "\n" + "\n".join(items) + "\n"
        todo_path.write_text(existing.rstrip() + "\n" + addition, encoding="utf-8")
        log.info(f"meta/TODO.md ažuriran sa {len(items)} stavk(i).")
    except Exception as e:
        log.error(f"Greška pri ažuriranju TODO.md: {e}")


def _git_commit_and_push(session_fname: str):
    """git add . && git commit && git push — tiho, ne blokira."""
    try:
        subprocess.run(["git", "add", "."], cwd=VAULT, capture_output=True, timeout=30)
        msg = f"brain: {session_fname}"
        result = subprocess.run(
            ["git", "commit", "-m", msg],
            cwd=VAULT, capture_output=True, text=True, timeout=30
        )
        if "nothing to commit" in result.stdout + result.stderr:
            log.info("git: nema novih promena.")
            return
        push = subprocess.run(
            ["git", "push"],
            cwd=VAULT, capture_output=True, text=True, timeout=60
        )
        if push.returncode == 0:
            log.info("git push uspešan.")
        else:
            log.warning(f"git push nije uspeo (lokalni commit sačuvan): {push.stderr[:200]}")
    except Exception as e:
        log.warning(f"git greška (nastavljamo): {e}")


def _fallback_report(now: datetime) -> str:
    """Kreira minimalni izveštaj ako Claude CLI nije dostupan."""
    slug = f"sesija-{now:%Y-%m-%d}"
    return f"""---
datum: {now:%Y-%m-%d}
vreme: {now:%H:%M}
tema: Drugo
status: u-toku
---

# Sesija {now:%d.%m.%Y.}

**Povezano:** [[INDEX]] · [[teme/Drugo]] · [[meta/TODO]]

## Kontekst
Automatski generisan izveštaj — Claude CLI nije bio dostupan.

## Šta je urađeno
— Nije moguće automatski rekonstruisati.

## Odluke (zašto)
—

## Planirano a nije urađeno
—

## TODO za sledeći put
— Pogledaj prethodnu sesiju ručno.

## Feedback od Ognjena
—

## Budući ciljevi
—

SLUG: {slug}
TEMA: Drugo
"""


def main():
    test_mode = "--test" in sys.argv

    if test_mode:
        # Test mod — generiši prazan izveštaj bez transcripta
        log.info("Test mod — generišem fallback izveštaj.")
        transcript = "[KORISNIK]: Test poruka.\n[CLAUDE]: Test odgovor."
    else:
        # Normalni hook mod — čitaj JSON payload sa stdin
        try:
            payload_raw = sys.stdin.read()
            if not payload_raw.strip():
                log.warning("Prazan stdin payload — generijem fallback.")
                payload = {}
            else:
                payload = json.loads(payload_raw)
        except Exception as e:
            log.warning(f"Ne mogu parsirati stdin payload: {e}")
            payload = {}

        transcript_path = payload.get("transcript_path", "")
        if transcript_path and Path(transcript_path).exists():
            transcript = _read_transcript(transcript_path)
        else:
            log.warning(f"Transcript ne postoji: {transcript_path}")
            transcript = ""

    now = datetime.now()

    # Generiši izveštaj
    if transcript:
        report_md = _call_claude(transcript)
    else:
        report_md = ""

    if not report_md:
        log.warning("Claude nije vratio izveštaj — koristim fallback.")
        report_md = _fallback_report(now)

    # Parsiraj metadata
    meta = _parse_metadata(report_md)
    slug = meta["slug"]
    tema = meta["tema"]
    session_fname_stem = f"{now:%Y-%m-%d_%H%M}_{slug}"
    session_fname = session_fname_stem + ".md"

    # Zapisuj
    session_path = _write_session(report_md, slug, now)
    if session_path:
        _update_index(session_fname, slug, tema, now)
        _update_tema(tema, session_fname, now)
        _extract_and_append_feedback(report_md)
        _extract_and_append_todo(report_md)
        _git_commit_and_push(session_fname)
    else:
        log.error("Session fajl nije zapisan — preskačem sve ostalo.")

    log.info("brain_save završen.")
    _safe_exit(0)


if __name__ == "__main__":
    main()
