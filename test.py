import pandas as pd
import streamlit as st
df=pd.read_csv(r"C:\Users\priya\Downloads\train.csv")
st.dataframe(df)