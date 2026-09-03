def generate_ai_answer(question: str, match_data: dict, prediction: dict) -> str:
    """Заглушка AI-агента. Позже заменить вызовом LLM API."""
    return (
        f"Матч: {match_data['home']} — {match_data['away']}. "
        f"Модель оценивает П1 в {prediction['p1']}%, ничью в {prediction['x']}%, "
        f"П2 в {prediction['p2']}%. Прогноз счёта: {prediction['score']}. "
        f"Уверенность модели: {prediction['confidence']}%. "
        f"Ваш вопрос: {question}"
    )
