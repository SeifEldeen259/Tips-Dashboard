import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Tips Dashboard",
                   page_icon=None,
                   layout="wide",
                   initial_sidebar_state="expanded")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
df = pd.read_csv(uploaded_file)
# Sidebar
st.sidebar.header("Tips Dashboard")
img = st.sidebar.file_uploader("Upload jpg file", type=["jpg"])

if img is not None:
    image = Image.open(img)
    st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)

st.sidebar.write("This dashboard is using Tips dataset from seaborn for educational purposes.")
st.sidebar.write("")
st.sidebar.write("Filter your Data")
cat_filter = st.sidebar.selectbox("Categorical Filtering",[None,'sex','smoker','day','time'])
num_filter = st.sidebar.selectbox("Numerical Filtering",[None,'total_bill','tip'])
st.sidebar.write("")
st.sidebar.markdown("Made with Love :heart_eyes: by Eng. [SeifEldin Salama]")
raw_filter = st.sidebar.selectbox("Raw Filtering",[None,'sex','smoker','day','time'])
col_filter = st.sidebar.selectbox("Column Filtering",[None,'sex','smoker','day','time'])

a1, a2, a3, a4 =st.columns(4)
a1.metric("Max. Total Bill", df['total_bill'].max())
a2.metric("Min. Total Bill", df['total_bill'].min())
a3.metric("Mean. Total Bill", df['total_bill'].mean())
a4.metric("Median. Total Bill", df['total_bill'].median())


st.subheader("Total Bill vs. Tips")
fig = px.scatter(data_frame=df,
                 x='total_bill',
                 y='tip',
                 color=cat_filter,
                 size=num_filter,
                 facet_row=raw_filter,
                 facet_col=col_filter)
st.plotly_chart(fig, use_container_width=True)

c1, c2, c3 = st.columns((4,3,3))
with c1:
    st.text("Sex vs. Total Bill")
    fig = px.bar(data_frame=df, x='sex', y='total_bill', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.text("Smoker/Non-Smoker vs. Tips")
    fig = px.pie(data_frame=df, names='smoker', values='tip', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c3:
    st.text("Day vs. Tips")
    fig = px.pie(data_frame=df,
                names='day',
                values='tip',
                color=cat_filter,
                hole=0.4)
    st.plotly_chart(fig, use_container_width=True)