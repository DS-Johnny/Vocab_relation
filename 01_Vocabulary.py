import streamlit as st
import pandas as pd

st.sidebar.title('Vocabulary')

df = pd.read_csv('Vocabulary.xlsx', sep=';', encoding='utf-8-sig')

st.sidebar.markdown("""---""")


stage = st.sidebar.selectbox(
    'Stage:',
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))



df = df[df['Stage'] == stage]

vocab_types = df['Type'].unique().tolist()

vocab_type = st.sidebar.selectbox(
    'Type of word:',
    (vocab_types))

df = df[df['Type'] == vocab_type]


df