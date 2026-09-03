# RPL AI Agent

MVP веб-приложения для AI-аналитики матчей Российской Премьер-Лиги.

**Scope:** только РПЛ. Другие турниры в текущий проект не входят.

## Структура

```text
project/
├── app.py
├── requirements.txt
├── README.md
├── AGENTS.md             # инструкции для Codex
├── docs/
│   ├── SPECIFICATION.md   # продуктовая и техническая спецификация
│   ├── ROADMAP.md         # этапы и сроки реализации
│   ├── PRODUCT_QUESTIONS.md # вопросы и журнал продуктовых решений
│   └── API_FOOTBALL_TEST.md # протокол проверки API-Football Free
├── .gitignore
├── .env.example
├── assets/
│   └── logo.png          # добавь эмблему/placeholder вручную
└── src/
    ├── __init__.py
    ├── data.py
    ├── predictions.py
    ├── ai_agent.py
    └── components.py
```

## Документация для разработки

Перед работой с Codex используй три файла как единый контекст:

- `AGENTS.md` — короткие обязательные инструкции для Codex.
- `docs/SPECIFICATION.md` — что именно представляет собой продукт и как должна работать архитектура.
- `docs/ROADMAP.md` — последовательность реализации, сроки и текущий этап.
- `docs/PRODUCT_QUESTIONS.md` — наводящие вопросы, уже принятые решения и то, что нужно определить до реализации спорных функций.
- `docs/API_FOOTBALL_TEST.md` — обязательный протокол тестирования API-Football Free перед полноценной интеграцией данных.

**Текущий приоритет:** завершить визуальный MVP и затем провести **Этап 2A — diagnostic test API-Football Free**. Платный тариф пока не использовать.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Следующие этапы

1. Протестировать API-Football Free по `docs/API_FOOTBALL_TEST.md`, затем заменить только подтверждённые mock-данные на реальные.
2. Подключить базу PostgreSQL/Supabase.
3. Заменить mock-логику в `src/predictions.py` на Poisson/Elo или ML-модель.
4. Подключить LLM в `src/ai_agent.py`.
5. Перенести стили и повторяемые UI-блоки в `src/components.py`.
6. Добавить историю прогнозов и метрики качества модели.

## Секреты

Скопируй `.env.example` в `.env` и заполни ключи. `.env` не коммить в GitHub.

## Workflow разработки

Проект использует Superpowers-подход к работе с coding agent. Смотри:
- `docs/SUPERPOWERS.md` — правила проектирования, планирования, проверки и YAGNI;
- `docs/DAILY_WORKFLOW.md` — дневной лимит 2 часа и уведомления;
- `scripts/project_time.py` — локальный явный таймер сессии.

Начало рабочей сессии:

```bash
python scripts/project_time.py start
python scripts/project_time.py status
```

Superpowers plugin устанавливается в среде Codex отдельно; репозиторий хранит проектные правила и fallback workflow.

## GitHub and daily checkpoint

Локальная папка проекта: **`RPL AI AGENT`**. Целевой отдельный GitHub-репозиторий: **`RPL-AI-AGENT`**.

При достижении дневного лимита 120 минут обязательно выполнить:

```bash
python scripts/project_time.py finish
```

День считается закрытым только после успешного commit/push. Подробнее: `docs/GITHUB_WORKFLOW.md` и `docs/DAILY_WORKFLOW.md`.
