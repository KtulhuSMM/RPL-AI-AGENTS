import streamlit as st

from src.data import MATCHES
from src.predictions import get_match_prediction
from src.ai_agent import generate_ai_answer
from src.components import render_match_card, render_sidebar

st.set_page_config(page_title='RPL AI Agent', page_icon='⚽', layout='wide')

st.title('RPL AI Agent')
st.caption('Ваш AI-аналитик российского футбола')

selected_match = st.selectbox(
    'Выберите матч',
    options=list(MATCHES.keys())
)

match_data = MATCHES[selected_match]
prediction = get_match_prediction(match_data)

render_match_card(selected_match, match_data, prediction)
render_sidebar()

st.divider()
st.subheader('AI-чат')
question = st.text_input('Спроси меня о матче, команде или игроке…')

if question:
    answer = generate_ai_answer(question, match_data, prediction)
    st.write(answer)
