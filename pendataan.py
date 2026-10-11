import streamlit as st
import pandas as pd

st.title("Pendataan Mahasiswa")

name = st.text_input("Masukkan Nama: ")
major = st.text_input("Masukkan Jurusan: ")

if st.button("Simpan"):
    with open("data_mahasiswa.csv", "a") as f:
        f.write(f"{name}, {major}\n")

isi = pd.read_csv("data_mahasiswa.csv")
st.table(isi)
