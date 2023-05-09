import pandas as pd
import random
import streamlit as st
try: 
    import quiz_state
except:
    state = 0
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
    
def get_question(any_df):
    correct_count = 0
    wrong_count = 0
    index_list = list(any_df.index.values)
    question_index = random.choice(index_list)
    question = any_df.at[question_index, 'Domanda']
    answers = any_df.at[question_index, 'Risposte'].split('|') 
    c_answer_n = any_df.at[question_index, 'Corretta_n']
    c_answer = answers[int(c_answer_n)-1]   
    returndict = {}
    returndict['question'] = question
    returndict['answers'] = answers
    returndict['c_answer_n'] = c_answer_n
    returndict['c_answer'] = c_answer
    return(returndict)

def show_question(question_dict):
     with st.form("my_form"):
        st.subheader(question_dict['question'])
        question_radio = st.radio('La tua risposta', question_dict['answers'])
        submitted = st.form_submit_button("Ok")
        if submitted:
            with open('quiz_state.py', 'w') as quiz_state_file:
                quiz_state_file.write('answer_n = ' + question_radio)
                quiz_state_file.write('c_answer_n = ' + question_dict[c_answer_n])
            
    
if state == 0:
    show_question(get_question(domande_df))
else:
    st.write(quiz_state.answer_n)
    st.write(quiz_state.c_answer_n)
    if quiz_state.answer_n == quiz_state.c_answer_n:
        st.success('well done')
    else:
        st.error('Argh')
