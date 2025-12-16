import streamlit as st

# judul
st.title ('menghitung volume bangun ruang')
st.header ('aplikasi ini adalah aplikasi untuk menghitung volume dari bangun ruang ')

# navbar
menu = st.sidebar.selectbox ('pilih bangun ruang', ['kubus','balok','tabung'])
# menu = st.sidebar.selectbox ('Pilih bangun datar', ['persegi','persegi panjang'])

if menu == 'kubus':
    st.image('kubus.jpg')
    sisi = st.number_input('masukan sisi', min_value=0)
    if st.button('hitung'):
        volume = sisi **3
        st.success(f'volume dari kubus adalah {volume}')

elif menu == 'balok':
    st.image('balok.jpg')
    panjang = st.number_input('Masukan panjang balok', min_value=0)
    luas = st.number_input('Masukan luas balok', min_value=0)
    tinggi = st.number_input('Masukan tinggi balok', min_value=0)
    if st.button('hitung'):
        volume = panjang * luas * tinggi
        st.success(f'volume dari balok adalah {volume}')

elif menu == 'tabung':
    st.image('tabung.jpg')
    jari_jari = st.number_input('Masukan jari-jari tabung', min_value=0)
    tinggi = st.number_input('Masukan tinggi tabung', min_value=0)
    if st.button('hitung'):
        volume = 3.14 * jari_jari ** 2 * tinggi
        st.success(f'volume dari tabung adalah {volume}')
