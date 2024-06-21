import streamlit as st
import pandas as pd

st.write(""" # My First App """)

# Load data
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv"
df = pd.read_csv(url)
st.line_chart(df)


