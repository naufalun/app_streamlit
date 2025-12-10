import streamlit as st
st.title("Cekidot Streamlit Perdana")
st.markdown(
    """ini adalah percobaan streamlit pertama saya.

streamlit itu menyenangkan untuk seorang pemula.

**saya penasaran :rainbow[projek apa saja] yang bisa dilakukan dengan streamlit!**

ternyata pembuatan projek lebih mudah menggunakan streamlit dibandingkan dengan coding menggunakan :rainbow[HTML,CSS & JavaScript]! Sepertinya saya akan suka dan nyaman memakai streamlit untuk menambah porofolio saya.
"""
)

if st.button("pencet saya!"):
    st.balloons()