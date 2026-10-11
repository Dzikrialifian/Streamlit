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

# draw a line chart
chart_data = pd.DataFrame(
    np.random.randint(1, 20, (20, 2)),
    columns = ['a', 'b']
)
st.line_chart(chart_data)
st.table(chart_data)

dates = pd.DataFrame({'date': pd.date_range("20261010", periods = 6)})
st.line_chart(dates)
st.dataframe(dates)

date = pd.date_range("20261010", periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), index = date, columns = list("ABCD"))
st.dataframe(df)

# menampilkan 5 baris pertama
df.head()
# menampilkan 3 baris terakhir
df.tail(3) 
# menampilkan index dari dataframe
st.write("Index dari dataframe:")
st.write(df.index)
# menampilkan nama kolom dari dataframe
st.write("Nama kolom dari dataframe:")
st.write(df.columns)

st.write("Data as NumPy array:")
st.write(df.to_numpy())

x = st.slider('X')
st.write(x, 'squared is', x * x)

name = st.text_input("Enter your name", key="name")
st.write("Hello, ", name)
st.session_state.name