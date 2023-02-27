import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
img = Image.open("w.jpg")
st.image(img)

st.title("Hello everyone, Welcome to our :blue[Internship] :green[2023] by :black[Innomatics] :red[Reaserch labs]")
st.header("I am :blue[Jayalakshmi Basetty].")
st.subheader("I have created new dashboards using the multipages technique please have a look")



if st.button('Click here'):
    st.write('Please refer pages')
    st.balloons()
else:
    st.write('Have a great day:smile:')
    




