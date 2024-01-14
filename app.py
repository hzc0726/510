import streamlit as st
from PIL import Image

st.title('This is Chaney')

image = Image.open('./linkedin title.jpg')



st.image(image)