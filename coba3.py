import streamlit as st

st.title('Menghitung luas persegi panjang')
panjang = st.number_input ("masukkan nilai panjang",0)
lebar = st.number_input ("masukkan nilai lebar",0)

hitung = st.button("hitung luas")

if hitung :
    luas = panjang * lebar
    st.write("luas persegi panjang adalah =", luas)
    st.success(f'luas persegi panjang adalah = {luas}')