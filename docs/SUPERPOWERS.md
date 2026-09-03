# Superpowers workflow for RPL AI Agent

## Purpose

This project uses the **Superpowers** software-development workflow as the preferred way of working with a coding agent.

Superpowers is an agentic development methodology built around: clarification/specification, implementation planning, small tasks, test-driven development where appropriate, YAGNI, DRY, verification and review.

> Important: the actual Superpowers plugin is installed in the Codex environment, not copied into this repository. This repository contains project-specific instructions that remain useful even when the plugin is unavailable.

## Codex setup

### Codex App
1. Open **Plugins** in the Codex sidebar.
2. Find **Superpowers** in the Coding / Developer Tools section.
3. Install/enable it for Codex.

### Codex CLI
1. Open `/plugins`.
2. Search for `superpowers`.
3. Install the plugin.

If the plugin is unavailable, follow the local fallback workflow below.

## Required workflow for this repository

### 1. Understand before coding
Before any substantial implementation:
- read `AGENTS.md`;
- read `docs/SPECIFICATION.md`;
- read the relevant section of `docs/ROADMAP.md`;
- check `docs/PRODUCT_QUESTIONS.md` for unresolved decisions;
- for real RPL data, read `docs/API_FOOTBALL_TEST.md`.

Do not invent a product decision when the project marks it as unresolved.

### 2. Plan small slices
For work larger than a trivial change:
- state the goal;
- break it into small verifiable tasks;
- define how each task will be checked;
- implement the minimum needed for the current roadmap stage.

Prefer one completed vertical slice over several half-built features.

### 3. YAGNI
Do not add infrastructure only because it may be useful later.
Examples of things NOT required before the roadmap asks for them:
- microservices;
- Kubernetes;
- queues;
- complex agent orchestration;
- multi-league abstractions;
- paid sports-data providers;
- advanced deep-learning models.

The product scope is RPL only.

### 4. Tests and verification
For logic that affects predictions, parsing, API normalization or stored data:
- add or update a focused test when practical;
- reproduce a bug before fixing it when possible;
- verify the fix after implementation.

For UI changes:
- run the app;
- verify the affected interaction manually;
- check that no existing primary path breaks.

Never report a task as complete without verification.

### 5. Prediction boundary
- Prediction probabilities are produced by deterministic/statistical/ML code in `src/predictions.py` or its future replacements.
- The LLM/AI layer must not invent probabilities, match statistics or unavailable facts.
- The AI agent explains and uses supplied data.

### 6. Data-source discipline
The first real external provider is **API-Football Free**.
Do not purchase or require a paid tier until the diagnostic checklist in `docs/API_FOOTBALL_TEST.md` has been completed.

Persist normalized data in our own database when that stage of the roadmap begins. Do not make the UI depend directly on a live external request for every page view.

### 7. Review before moving on
At the end of a substantial task:
- summarize files changed;
- state what was verified;
- mention any unresolved risk or assumption;
- update documentation if project behavior or decisions changed.

## Daily work constraint

The default project work budget is **120 minutes per day**.
The repository includes `scripts/project_time.py` to help the agent respect that budget.

Required agent behavior is defined in `docs/DAILY_WORKFLOW.md` and `AGENTS.md`.
