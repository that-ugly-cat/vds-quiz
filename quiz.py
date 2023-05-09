import pandas as pd
import random
import streamlit as st

domande_df = pd.read_excel('Domande.xlsx')
#st.dataframe(domande_df)

st.header('Quiz volo da diporto e sportivo')
st.subheader('...')

categories = domande_df['Categoria'].unique().tolist()
df_dict= {}
for x in categories:
    df_name = 'df_' + x
    df = domande_df[domande_df['Categoria'] == x]
    df = df.reset_index()
    df_dict[df_name] = df
    
for key, item in df_dict.items():
    st.dataframe(item)
    
def ask_questions(df):
    correct_count = 0
    wrong_count = 0
    
