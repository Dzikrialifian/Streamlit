import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Learning")

datas = pd.DataFrame({
    'Name' : ["Dzikri Alifian", "Irma Putri", "Rizky"], 
    'Age' : [20, 20, 19],
    'Sex' : ["Male", "Female", "Male"]})

st.write("Showing DataFrame with st.write()")
st.write(datas)
st.write("Showing DataFrame with st.table()")
st.table(datas)

dataFrame = np.random.randn(2, 2)
# membuat matriks 10x10 dengan nilai random dari 1 sampai 100
datamatrik = np.random.randint(1, 100, (10, 10))
st.write(dataFrame)
st.dataframe(dataFrame)
st.write("Showing Matrix with st.dataframe()")
st.dataframe(datamatrik)

dataHighlight = pd.DataFrame(
    np.random.randn(10, 10),
    # mengambil nama kolom dari 0 sampai 9
    columns = ('col %d' % i for i in range(10))
)

st.dataframe(dataHighlight.style.highlight_min(axis=0)) #axis=0 untuk kolom, axis=1 untuk baris