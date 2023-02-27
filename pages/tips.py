import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
img = Image.open("t.jpg")
st.image(img)


st. title(":blue[TIPS DATA SET]")
st.header("Here we have a simple dashboard for :red[tips] data set")
df = pd.read_csv("tips.csv")

st.dataframe(df)

fig1 = plt.figure()
df["day"].value_counts().plot(kind = "bar")
st.pyplot(fig1)

fig2 = plt.figure()
sns.stripplot(df[['sex','tip']])
st.pyplot(fig2)

st.bar_chart(df["size"])
st.bar_chart(df[["total_bill","tip"]])
