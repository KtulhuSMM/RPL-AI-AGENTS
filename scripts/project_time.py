"""Simple local daily work timer for the RPL AI Agent project.

Usage:
    python scripts/project_time.py start
    python scripts/project_time.py status
    python scripts/project_time.py reset
    python scripts/project_time.py finish

The timer is intentionally local and explicit. It does not run in the background.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = PROJECT_ROOT / ".project_time.json"
DAILY_LIMIT_MINUTES = 120
WARNING_30_MINUTES = 90
WARNING_10_MINUTES = 110


def now_local() -> datetime:
    return datetime.now().astimezone()


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def today_key(now: datetime) -> str:
    return now.date().isoformat()


def start() -> int:
    now = now_local()
    state = load_state()
    today = today_key(now)

    if state.get("date") == today and state.get("started_at"):
        started = datetime.fromisoformat(state["started_at"])
        print(f"Session already started today at {started.strftime('%H:%M:%S %z')}.")
        return status()

    state = {
        "date": today,
        "started_at": now.isoformat(),
        "daily_limit_minutes": DAILY_LIMIT_MINUTES,
    }
    save_state(state)
    print(f"Project session started at {now.strftime('%H:%M:%S %z')}.")
    print(f"Daily limit: {DAILY_LIMIT_MINUTES} minutes.")
    return 0


def status() -> int:
    now = now_local()
    state = load_state()
    today = today_key(now)

    if state.get("date") != today or not state.get("started_at"):
        print("NO_SESSION: No project session has been started today.")
        print("Run: python scripts/project_time.py start")
        return 2

    started = datetime.fromisoformat(state["started_at"])
    elapsed = max(0, int((now - started).total_seconds() // 60))
    remaining = max(0, DAILY_LIMIT_MINUTES - elapsed)

    if elapsed >= DAILY_LIMIT_MINUTES:
        level = "LIMIT_REACHED"
        message = "Daily 120-minute project limit reached. Run: python scripts/project_time.py finish"
    elif elapsed >= WARNING_10_MINUTES:
        level = "WARNING_10"
        message = "About 10 minutes remain. Wrap up, verify, and checkpoint."
    elif elapsed >= WARNING_30_MINUTES:
        level = "WARNING_30"
        message = "About 30 minutes remain. Finish the current small task; avoid large new work."
    else:
        level = "OK"
        message = "Within the daily project budget."

    print(f"STATUS: {level}")
    print(f"Started: {started.strftime('%Y-%m-%d %H:%M:%S %z')}")
    print(f"Elapsed minutes: {elapsed}")
    print(f"Remaining minutes: {remaining}")
    print(message)
    return 0 if level == "OK" else 1


def reset() -> int:
    if STATE_FILE.exists():
        STATE_FILE.unlink()
    print("Project timer state reset.")
    return 0


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "status"
    if command == "start":
        return start()
    if command == "status":
        return status()
    if command == "reset":
        return reset()
    if command == "finish":
        import subprocess
        proc = subprocess.run([sys.executable, str(PROJECT_ROOT / "scripts" / "end_day.py")], cwd=PROJECT_ROOT)
        return proc.returncode
    print("Usage: python scripts/project_time.py [start|status|reset|finish]")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
