# GitHub workflow for RPL AI Agent

## Repository convention

- Local root directory: `RPL AI AGENT`
- Separate GitHub repository slug: `RPL-AI-AGENT`
- Main remote: `origin`

GitHub does not provide free-standing folders outside repositories, so the project should live in its own repository named `RPL-AI-AGENT` rather than as an unrelated folder on the GitHub account.

## One-time setup

After creating the repository on GitHub, initialize/configure the local project:

```bash
git init
git branch -M main
git remote add origin <YOUR_RPL_AI_AGENT_REPOSITORY_URL>
git add -A
git commit -m "chore: initialize RPL AI Agent"
git push -u origin main
```

Never place a personal access token or API key directly in this file or in a committed remote URL.

## Daily closing rule

The project has a 120-minute daily budget. At the limit the coding agent must run:

```bash
python scripts/project_time.py finish
```

Success means the output contains `END_DAY_COMPLETE` and the branch was pushed to `origin`.

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
