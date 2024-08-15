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

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual", "Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental para tu interfaz")
