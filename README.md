# RPL AI Agent

MVP веб-приложения для AI-аналитики матчей Российской Премьер-Лиги.

**Scope:** только РПЛ. Другие турниры в текущий проект не входят.

## Структура

```text
RPL AI AGENT/
├── app.py
├── requirements.txt
├── README.md
├── AGENTS.md
├── docs/
│   ├── SPECIFICATION.md
│   ├── ROADMAP.md
│   ├── PRODUCT_QUESTIONS.md
│   ├── API_FOOTBALL_TEST.md
│   ├── SUPERPOWERS.md
│   ├── DAILY_WORKFLOW.md
│   └── GITHUB_WORKFLOW.md
├── scripts/
│   ├── project_time.py
│   └── end_day.py
├── .gitignore
├── .env.example
├── assets/
│   └── logo.png
└── src/
    ├── __init__.py
    ├── data.py
    ├── predictions.py
    ├── ai_agent.py
    └── components.py
```

## GitHub

Основной репозиторий проекта: **`KtulhuSMM/RPL-AI-AGENTS`**.

Remote `origin` локальной папки должен указывать на:

```text
https://github.com/KtulhuSMM/RPL-AI-AGENTS.git
```

Проверить можно командой:

```bash
git remote -v
```

## Документация для разработки

Перед работой с Codex используй файлы как единый контекст:

- `AGENTS.md` — обязательные инструкции для Codex.
- `docs/SPECIFICATION.md` — продуктовая и техническая спецификация.
- `docs/ROADMAP.md` — последовательность реализации и сроки.
- `docs/PRODUCT_QUESTIONS.md` — принятые и открытые продуктовые решения.
- `docs/API_FOOTBALL_TEST.md` — протокол тестирования API-Football Free.
- `docs/SUPERPOWERS.md` — рабочий процесс Superpowers.
- `docs/DAILY_WORKFLOW.md` — дневной лимит 2 часа.
- `docs/GITHUB_WORKFLOW.md` — обязательный commit/push по окончании сессии.

**Текущий приоритет:** завершить визуальный MVP и затем провести diagnostic test API-Football Free. Платный тариф пока не использовать.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Следующие этапы

1. Протестировать API-Football Free по `docs/API_FOOTBALL_TEST.md`.
2. Заменить только подтверждённые mock-данные на реальные.
3. Подключить PostgreSQL/Supabase.
4. Заменить mock-логику в `src/predictions.py` на Poisson/Elo или ML-модель.
5. Подключить LLM в `src/ai_agent.py`.
6. Добавить историю прогнозов и метрики качества.

## Секреты

Скопируй `.env.example` в `.env` и заполни ключи. `.env` не коммить в GitHub.

## Workflow разработки

Начало рабочей сессии:

```bash
python scripts/project_time.py start
python scripts/project_time.py status
```

Проект использует дневной лимит **120 минут**. При достижении лимита обязательно выполнить:

```bash
python scripts/project_time.py finish
```

День считается закрытым только после успешного commit/push в **`KtulhuSMM/RPL-AI-AGENTS`**. Если push не прошёл, агент обязан сообщить `END_DAY_FAILED` и не считать сессию закрытой.
