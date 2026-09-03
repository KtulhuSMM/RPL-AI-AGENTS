def get_match_prediction(match_data: dict) -> dict:
    """Mock-прогноз. Позже здесь будет ML-модель."""
    home = match_data['home']

    presets = {
        'Зенит': {'p1': 45, 'x': 28, 'p2': 27, 'score': '2:1', 'confidence': 64},
        'ЦСКА': {'p1': 38, 'x': 30, 'p2': 32, 'score': '1:1', 'confidence': 56},
        'Краснодар': {'p1': 50, 'x': 26, 'p2': 24, 'score': '2:0', 'confidence': 68},
    }

    return presets.get(
        home,
        {'p1': 40, 'x': 30, 'p2': 30, 'score': '1:1', 'confidence': 50},
    )
