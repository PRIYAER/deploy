import pandas as pd
import streamlit as st
df=pd.read_csv("train.csv")
st.dataframe(df)
