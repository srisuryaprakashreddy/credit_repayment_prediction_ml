from PIL import Image
import streamlit as st

image =Image.open("wall.jpg")

st.image(image,caption="wallpaper")