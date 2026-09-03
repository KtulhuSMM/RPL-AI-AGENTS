# Daily project workflow — 2 hour limit

## Daily budget

Default maximum focused work on RPL AI Agent: **2 hours (120 minutes) per day**.

The purpose of the limit is to keep the project sustainable and force prioritization. It is not a background timer: Codex/another agent must explicitly check the repository timer while working.

## Start of every development session

Run:

```bash
python scripts/project_time.py start
```

Behavior:
- if no session has been started today, the script records the start time;
- if today's session already exists, it keeps the original start time rather than resetting the budget.

Then run:

```bash
python scripts/project_time.py status
```

## Mandatory time checks

The coding agent must check `status`:
- at the start of work;
- before beginning a substantial new task;
- after completing a substantial task;
- before starting a long test/debug/refactor cycle;
- before its final project update to the user.

The agent must not claim to monitor time continuously or in the background.

## Warning thresholds

### At 90 minutes elapsed
Tell the user clearly:

> До дневного лимита проекта осталось около 30 минут. Я завершу текущую небольшую задачу и не буду начинать крупную новую без необходимости.

Prioritize finishing the active slice, tests and documentation.

### At 110 minutes elapsed
Tell the user clearly:

> До дневного лимита осталось около 10 минут. Перехожу к завершению: проверка, фиксация состояния и следующий шаг на завтра.

Do not start a new feature.

### At or after 120 minutes elapsed
Tell the user clearly:

> Дневной лимит 2 часа на проект достигнут. Я не начинаю новую разработку сегодня; фиксирую текущее состояние и предлагаю следующий конкретный шаг на следующую сессию.

Then:
1. finish only actions needed to leave the repository in a safe state;
2. run the smallest relevant verification;
3. write/update a session note if useful;
4. do not start new implementation unless the user explicitly overrides the daily limit.

## User override

The 120-minute limit is a default project rule, not a hard technical restriction.
If the user explicitly says to continue today or changes the daily budget, follow the user's instruction and update this document/config if the change is intended to be persistent.

## If time tracking is unavailable

If the script cannot determine or persist the session start, the agent must say that reliable time tracking is unavailable rather than pretending the limit is being tracked.
Use the user's stated start time if available.

## Mandatory GitHub closeout

At the 120-minute limit, stopping work is not enough. The agent must execute:

```bash
python scripts/project_time.py finish
```

The finish procedure is mandatory and must create/preserve an end-of-day checkpoint and push the current branch to GitHub `origin`.

Required order:
1. stop starting new features;
2. run the smallest relevant verification;
3. create/update `docs/sessions/YYYY-MM-DD.md`;
4. stage safe project changes;
5. commit them (`chore: end-of-day checkpoint ...` or, if verification is failing, `WIP: end-of-day checkpoint ...`);
6. push the current branch to `origin`;
7. report completion only when push succeeds.

If push fails because the remote is missing, authentication is unavailable, the network is unavailable, or GitHub rejects the update, report the failure clearly. The day remains technically **open** until the checkpoint is present on GitHub.

### GitHub target

- Local project directory: `RPL AI AGENT`
- Intended GitHub repository: `RPL-AI-AGENT`
- Expected remote name: `origin`

Before relying on automatic closeout, verify once:

```bash
git remote -v
git branch --show-current
python scripts/end_day.py
```
