import streamlit as st
import math

# halaman utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.header('ini buatan anak SI')

# sidebar
menu = st.sidebar.selectbox('Pilih aplikasi ', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'Luas Persegi Panjang'])

# jenis aplikasi perhitungan
if menu == 'Luas Persegi':
    st.write('Ini halaman untuk menghitung luas persegi')
    st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOYAAADbCAMAAABOUB36AAAAeFBMVEX///8AAAAiIiL8/Pzx8fFbW1vc3Nz4+Pjk5ORfX1+WlpZzc3Obm5vh4eE8PDw0NDRISEhUVFRCQkKQkJDr6+vMzMx5eXkvLy+EhIQmJibDw8Onp6dNTU0dHR26urptbW0XFxcODg6Hh4evr69lZWW/v7+lpaXT09M+BKV/AAAEW0lEQVR4nO3de4+qOBgGcF6LFFHkIqh4Q3SOfv9vuC04yWYzs7OWPOWc7PPLXJw/aPtQWjCx0yAgIiIiIiIiIiIiIiIi+pGaugFeqDCcugk+bLqsmroNQfCsD3WMO98qzETusOL/czNKMcojbAAdTPGn6cdnLufyKrJBteRD5o2kmLLfkMs2UIlIDSldxyLPhT2JE/enjal1aX4CqOAopXpIFqqJc+ayN63ZmtYAClfKFh+J/Jp6dPYx1VYyjSg9FdnlZWcHxvS9qU3ME6T0lQxm8W8QM9Br0NjcSRunUWRvnSNimlM0dmz3vbkxMy3ibF9e5e7kpN3LV8P3qKC5zNYze99EjM06OfYPWPXmMab4w6qKNvWoWWxth87pCHkjob545VLMXA53uY0qwoycKFaeJkLHSlqp7+Z6c6307+nwMVWw+ljMHSwaKXLJ2oWbvVZeH06qpivL9duy9VV2O2ny7G328LNEfmOGzVIb4Zu0/rAX7U1pF+Z5PfXcm7OlS31KmZgX57FpYo6+675liPluheaA+h5W98ix1iGm48EuwtnS5Sav/vH7TdPE9C7x/aZ+uphe3zYwJhBjYjAmEGNiMCYQY2IwJhBjYjAmEGNiMCYQY2IwJhBjYjAmEGNiMCYQY2IwJhBjYjAmEGNiMCYQY2IwJhBjYjAmEGNiMCYQY2IwJoz6f8S0q/Fin9VVcdq0wMXqX9rPF5kUC3+fj46vchWRhbcKrWGBvMjTW41VURRdU0DWT35HqTRKt3KIIEtwv5XtvVZnZp76cmnlcfc3VKqyLLtz6bc3g9dFi/k3AF+Ju75Cv2MzuCSrQm4rf72p0jhq2srvTGvvl4nfG0qgwl07YumxU5VKTRDTPB74XTA/TW9O9EzLmACMicSYEIyJxJgQjInEmBCMicSYEIyJxJgQjInEmBCMicSYEIyJxJgQjInEmBCMicSYEIyJxJgQjInEmBCMicSYEIyJxJgQjInEmBCM+cOBn19O/piYQVhp7fwpeR8xo4MRhf1Hv91jJnJ/iusF7yNmPqwDOdrXJqbjKpTfPmYhzbbNXutdqmaduFjNZbmV3XHlZP5a2DiMbcyKgkLm/UqbxNYQnsRZJ53roU3Vx1P1MbmAdoAppDAzyFke9g8VR2lq9y17U7yX1UU+4veP7A0bEOttf7aOkH2L7EW7zWUxbq/jlR2b7suu+lgbkfYxt8MHsOSnGK6b7Yh9DM3JX8klOjtOX6++M1fUzfzRb5Hr3JZvFZKnUX1137lumD20Nt8jCgiCWuyuacGv29G5Jf+iH5vBUoqRp3D0eDrI530FMQeZmEpHmfNN79PoppmY/YSL2TitkK7MO5/rRL9hLtrYRtSQ9cdzOwHNigui7LdEIgfTl0kDeZOkw8o8d/vY9vIHqpRC2+X6npd3+/Ycbm073APu5F3ZO5Qi53b63e3BVBin4x7G/gi+9v8lIiIiIiIiIiIiIiIiIiIiIiIiX/4CrfNF0obpmHoAAAAASUVORK5CYII=', caption='gambar persegi')
    sisi = st.number_input('silahkan masukkan nilai sisi', min_value=0, )
    if st.button('Hitung'):
        luas = sisi * sisi
        st.success(f'luas persegi adalah {luas}')

elif menu == 'Luas Segitiga':
    st.write('Ini halaman untuk menghitung luas segitiga')
    st.image('segitiga.jpg')
    alas = st.number_input('silahkan masukan nilai alas', min_value=0)
    tinggi = st.number_input('silahkan masukan nilai tinggi',min_value=0)
    if st.button('hitung'):
        luas = 0.5 * alas * tinggi
        st.success(f'luas segitiga adalah {luas}')
    

elif menu == 'Luas Lingkaran':
    st.write('Ini halaman untuk menghitung luas lingkaran')
    st.image('lingkaran.png')
    jari_jari = st.number_input('silahkan masukkan nilai jari-jari', min_value=0)
    if st.button('hitung'):
        luas = math.pi * (jari_jari**2)
        st.success(f'luas lingkaran adalah {luas}')

elif menu == "Luas Persegi Panjang":
    st.write('ini halaman untuk menghitung luas persegi panjang')
    st.image('persegi panjang.png')
    panjang = st.number_input('silahkan masukkan nilai panjang', min_value=0)
    lebar = st.number_input('silahkan masukkan nilai lebar', min_value=0)
    if st.button('hitung'):
        luas = panjang * lebar
        st.success(f'luas dari persegi panjang adalah {luas}')





