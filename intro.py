import streamlit as st
from PIL import Image

st.title(" Primera app :D ")

st.header( " Esta es mi primera aplicacion con streamlit ")

image = Image.open("paleopapus.jpg")
st.image(image, caption = "paleopapus")

texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("el texto escribido es", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")
