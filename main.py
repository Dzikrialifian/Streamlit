import streamlit as st
import pandas as pd

st.title("Streamlit App")
st.write("Hello, this is a simple Streamlit app!")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))