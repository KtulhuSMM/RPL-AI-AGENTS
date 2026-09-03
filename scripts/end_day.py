"""Mandatory end-of-day checkpoint for RPL AI Agent.

This script verifies the repository, records a session note, commits all safe
tracked/untracked project changes, and pushes the current branch to `origin`.
It is intended to be run when the 120-minute daily limit is reached.

Usage:
    python scripts/end_day.py

Important:
- Secrets such as .env must remain ignored by git.
- If verification fails, the script still creates a clearly marked WIP
  checkpoint commit so the day's work is not lost, then pushes it.
- A day is NOT considered closed unless the push succeeds.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "docs" / "sessions"


def run(args: list[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        args,
        cwd=PROJECT_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(args)}\n{proc.stdout}")
    return proc


def verify_repo() -> tuple[bool, str]:
    checks: list[tuple[str, list[str]]] = [
        ("Python syntax", [sys.executable, "-m", "compileall", "-q", "app.py", "src", "scripts"]),
    ]
    lines: list[str] = []
    ok = True
    for name, cmd in checks:
        proc = run(cmd)
        passed = proc.returncode == 0
        ok = ok and passed
        lines.append(f"- {name}: {'PASS' if passed else 'FAIL'}")
        if proc.stdout.strip():
            lines.append(f"  - Output: {proc.stdout.strip()[:1200]}")
    return ok, "\n".join(lines)


def ensure_git_repo() -> None:
    proc = run(["git", "rev-parse", "--is-inside-work-tree"])
    if proc.returncode != 0 or proc.stdout.strip() != "true":
        raise RuntimeError("This project is not initialized as a git repository. Run git init and configure origin first.")


def ensure_origin() -> str:
    proc = run(["git", "remote", "get-url", "origin"])
    if proc.returncode != 0 or not proc.stdout.strip():
        raise RuntimeError(
            "Git remote 'origin' is not configured. Create the GitHub repository RPL-AI-AGENT and set origin before end-of-day automation can succeed."
        )
    return proc.stdout.strip()


def current_branch() -> str:
    proc = run(["git", "branch", "--show-current"], check=True)
    branch = proc.stdout.strip()
    if not branch:
        raise RuntimeError("Detached HEAD is not supported for mandatory end-of-day push.")
    return branch


def write_session_note(verification_ok: bool, verification_text: str, remote: str, branch: str) -> Path:
    now = datetime.now().astimezone()
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    note = LOG_DIR / f"{now.date().isoformat()}.md"
    status = run(["git", "status", "--short"]).stdout.strip() or "(clean before session note)"
    content = f"""# Session checkpoint — {now.date().isoformat()}\n\n- Closed at: {now.isoformat()}\n- Branch: `{branch}`\n- Remote: `{remote}`\n- Verification: **{'PASS' if verification_ok else 'FAIL / WIP checkpoint'}**\n\n## Verification\n\n{verification_text}\n\n## Git status before checkpoint\n\n```text\n{status}\n```\n\n## Next session\n\nContinue from the roadmap and inspect this checkpoint before starting new implementation.\n"""
    note.write_text(content, encoding="utf-8")
    return note


def commit_and_push(verification_ok: bool, branch: str) -> None:
    run(["git", "add", "-A"], check=True)
    staged = run(["git", "diff", "--cached", "--quiet"])
    if staged.returncode == 0:
        print("No project changes to commit. Proceeding to push current branch.")
    else:
        now = datetime.now().astimezone()
        prefix = "chore" if verification_ok else "WIP"
        message = f"{prefix}: end-of-day checkpoint {now.date().isoformat()}"
        run(["git", "commit", "-m", message], check=True)
        print(f"Created commit: {message}")

    push = run(["git", "push", "origin", branch])
    if push.returncode != 0:
        raise RuntimeError(
            "Mandatory GitHub push FAILED. The development day is not considered closed.\n" + push.stdout
        )
    print(push.stdout.strip())
    print(f"END_DAY_COMPLETE: branch '{branch}' pushed successfully to origin.")


def main() -> int:
    try:
        ensure_git_repo()
        remote = ensure_origin()
        branch = current_branch()
        verification_ok, verification_text = verify_repo()
        note = write_session_note(verification_ok, verification_text, remote, branch)
        print(f"Session note: {note.relative_to(PROJECT_ROOT)}")
        print(verification_text)
        commit_and_push(verification_ok, branch)
        return 0
    except Exception as exc:
        print(f"END_DAY_FAILED: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
