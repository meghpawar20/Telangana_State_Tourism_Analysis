#🎯
from turtle import right
import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px
from millify import millify

st.set_page_config(page_title="Overall Tourism Analytics", page_icon="📈",layout="wide")
st.header("Overall Tourism Analytics📈")
@st.cache_data(persist=True)
def getData():
    res=pd.read_csv("pages\combined.csv")
    return res
c=getData()

#st.dataframe(domestic)
Year=st.multiselect(
    "Select Year",
    options=c["year"].unique(),
    default=c["year"].unique(),
)

dfs=c.query("year==@Year")
#st.dataframe(dfs)
visitors=int(dfs["visitors"].sum())
district=int(c["district"].nunique()-1)
#value= "$"+millify(total_sales, precision=2)
t1,t2=st.columns(2,gap="large")
with t1:
    st.info("Visitors",icon="📌")
    st.metric(label="No. of Vistors",value=millify(visitors, precision=2))
with t2:
    st.info("Districts",icon="📌")
    st.metric(label="No. of District",value=f"{district:}")

st.markdown("---")

def graphs():
    g1=dfs.groupby("district")["visitors"].sum().sort_values(ascending=True).nlargest(10)
    g1=g1.reset_index()
    g1=g1.groupby("district",as_index = False)["visitors"].sum()
    g1=g1.sort_values(by="visitors",ascending=True)
    fig1 = px.bar(g1, x="visitors", y="district",title="Top 10 Districts Based on Visitors" ,orientation='h')
    fig1.update_traces(marker_color = '#f9c068',)
    fig1.update_layout(xaxis=dict(showgrid=False))

    g2=dfs.groupby("district")["visitors"].sum().sort_values(ascending=True).nsmallest(10)
    g2=g2.reset_index()
    g2=g2.groupby("district",as_index = False)["visitors"].sum()
    g2=g2.sort_values(by="visitors",ascending=False)
    fig2 = px.bar(g2, x="visitors", y="district",title="Bottom 10 Districts Based on Visitors", orientation='h')
    fig2.update_traces(marker_color = '#f9c068',)
    fig2.update_layout(xaxis=dict(showgrid=False))

    left,right= st.columns(2)
    left.plotly_chart(fig1,use_container_width=True)
    right.plotly_chart(fig2,use_container_width=True)
graphs()
st.markdown("---")

Year2=st.selectbox(
    "Select Year",
    options=c["year"].unique()
)
yfs=c.query("year==@Year2")
#st.dataframe(yfs)


def graph2():
    g1=yfs.groupby("month")["visitors"].sum()
    g1=g1.reset_index()
    g1=g1.groupby("month",as_index = False)["visitors"].sum()
    g1=g1.sort_values(by="visitors",ascending=False)
    fig1= px.bar(g1, x="month", y="visitors", title='Variation of Visitors')
    fig1.update_traces(marker_color = '#f9c068',)
    fig1.update_layout(xaxis=dict(showgrid=False))
    st.plotly_chart(fig1,use_container_width=True)
graph2()
st.markdown("---")

