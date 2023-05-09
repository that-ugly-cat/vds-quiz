import pandas as pd
import random
import streamlit as st

domande_df = pd.read_excel('Domande.xlsx')
st.dataframe(domande_df)
