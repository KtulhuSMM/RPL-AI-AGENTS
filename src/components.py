import streamlit as st

from src.data import STANDINGS, FORM, SCORERS


def render_match_card(match_name: str, match_data: dict, prediction: dict) -> None:
    st.subheader(match_name)
    st.caption(match_data['date'])

    c1, c2, c3 = st.columns(3)
    c1.metric('П1', f"{prediction['p1']}%")
    c2.metric('X', f"{prediction['x']}%")
    c3.metric('П2', f"{prediction['p2']}%")

    st.markdown(f"**Прогноз счёта:** {prediction['score']}")
    st.markdown(f"**Уверенность модели:** {prediction['confidence']}%")

    st.markdown('**Ключевые факторы:**')
    st.write('- Домашняя форма')
    st.write('- Результаты последних матчей')
    st.write('- Качество атаки и обороны')


def render_sidebar() -> None:
    with st.sidebar:
        st.header('РПЛ 2026/27')

        st.subheader('Турнирная таблица')
        for i, (team, points) in enumerate(STANDINGS, start=1):
            st.write(f'{i}. {team} — {points} очк.')

        st.subheader('Форма команд')
        for team, form in FORM.items():
            st.write(f'{team}: {form}')

        st.subheader('Бомбардиры')
        for player, team, goals in SCORERS:
            st.write(f'{player} ({team}) — {goals}')
