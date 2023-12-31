import streamlit as st
import pandas as pd

st.sidebar.title('Idioms')

df = pd.read_csv('Vocabulary.csv', sep=';', encoding='utf-8-sig')

df = df[df['Idiom'] == True]

st.sidebar.markdown("""---""")


stage = st.sidebar.selectbox(
    'Stage:',
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))



df = df[df['Stage'] == stage]




df