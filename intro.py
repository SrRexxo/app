import streamlit as st
from PIL import Image

st.title(" Primera app :D ")

st.header( " Esta es mi primera aplicacion con streamlit ")

image = Image.open("paleopapus.jpg")
st.image(image, caption = "paleopapus")
