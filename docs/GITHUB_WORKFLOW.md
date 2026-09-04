# GitHub workflow for RPL AI Agent

## Repository convention

- Local root directory: `RPL AI AGENT`
- GitHub repository: `KtulhuSMM/RPL-AI-AGENTS`
- Main remote: `origin`

Remote `origin` должен указывать на:

```text
https://github.com/KtulhuSMM/RPL-AI-AGENTS.git
```

Проверка:

```bash
git remote -v
```

Если `origin` настроен неверно:

```bash
git remote set-url origin https://github.com/KtulhuSMM/RPL-AI-AGENTS.git
```

## One-time setup

Для локальной папки проекта:

```bash
git init
git branch -M main
git remote add origin https://github.com/KtulhuSMM/RPL-AI-AGENTS.git
git add -A
git commit -m "chore: initialize RPL AI Agent"
git push -u origin main
```

Если `origin` уже существует, не добавляй его повторно — используй `git remote set-url origin ...`.

Никогда не помещай personal access token, API key или другой секрет в committed remote URL или файлы репозитория.

## Daily closing rule

The project has a 120-minute daily budget. At the limit the coding agent must run:

```bash
python scripts/project_time.py finish
```

Success means the output contains `END_DAY_COMPLETE` and the current branch was successfully pushed to `origin`, то есть в `KtulhuSMM/RPL-AI-AGENTS`.

Failure means the output contains `END_DAY_FAILED`. In this case the agent must tell the user what blocked the push and must not claim that the GitHub backup exists.

## Commit policy

Normal finished work:

```text
feat: ...
fix: ...
docs: ...
refactor: ...
```

Mandatory daily checkpoint when work remains:

```text
chore: end-of-day checkpoint YYYY-MM-DD
```

If verification is failing and cannot be repaired before the hard stop:

```text
WIP: end-of-day checkpoint YYYY-MM-DD
```

WIP is acceptable only for the time-limit checkpoint and should be resolved at the beginning of the next development session.
