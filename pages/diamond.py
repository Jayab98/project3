import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

img = Image.open("d.jpg")
st.image(img)

st.title(":blue[DIAMONDS DATA SET]")

st.header("Here we have a simple dashboard for :red[diamonds] data set")
df = pd.read_csv("diamonds.csv")

st.dataframe(df)

fig1 = plt.figure()
df["cut"].value_counts().plot(kind = "bar")
st.pyplot(fig1)

fig2 = plt.figure()
sns.stripplot(df[['cut','price']])
st.pyplot(fig2)

st.bar_chart(df["clarity"])
st.bar_chart(df[["carat","price"]])


