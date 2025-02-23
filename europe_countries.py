import streamlit as st 
from sqlalchemy import create_engine 
import pandas as pd 

engine = create_engine('mysql+mysqlconnector://root:Matthew19961024@localhost/europe')
query = "SELECT * FROM countries" 
df = pd.read_sql(query, engine) 

st.title('Europe Countries Languages & Population') 
st.dataframe(df)