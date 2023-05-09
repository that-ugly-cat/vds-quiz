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
    df_cat = domande_df[domande_df['Categoria'] == x]
    df_cat = df_cat.reset_index()
    df_dict[df_name] = df_cat
    
'''for key, item in df_dict.items():
    st.dataframe(item)'''
    
def ask_questions(any_df):
    correct_count = 0
    wrong_count = 0
    index_list = list(any_df.index.values)
    question_index = random.choice(index_list)
    question = any_df.at[question_index, 'Domanda']
    answers = any_df.at[question_index, 'Risposte'].split('|') 
    c_answer_n = any_df.at[question_index, 'Corretta_n']
    c_answer = answers[int(c_answer_n)-1]
    
    with st.form("my_form"):
        st.subheader(question)
        st.radio('La tua risposta', answers)
        submitted = st.form_submit_button("Ok")
        if submitted:
            st.write(c_answer)
            st.write(c_answer_n)
    
    return(question, answers, c_answer_n, c_answer)

x = ask_questions(domande_df)

st.write(x)
'''for key, item in df_dict.items():
    x = ask_questions(item)'''
