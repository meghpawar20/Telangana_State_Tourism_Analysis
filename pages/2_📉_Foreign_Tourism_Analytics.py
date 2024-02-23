from turtle import right
import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px
from millify import millify

st.set_page_config(page_title="Foreign Toursism Analytics", page_icon="📈",layout="wide")
st.header("Foreign Tourism Analytics📈")
@st.cache_data(persist=True)
def getData():
    res=pd.read_csv("pages\\foreign_visitors.csv")
    return res
foreign=getData()
@st.cache_data(persist=True)
def getCAGRData():
    res=pd.read_csv("pages\\foreign_cagr.csv")
    return res
cfs=getCAGRData()
#st.dataframe(domestic)
Year=st.multiselect(
    "Select Year",
    options=foreign["year"].unique(),
    default=foreign["year"].unique(),
)

dfs=foreign.query("year==@Year")
#st.dataframe(dfs)
visitors=int(dfs["visitors"].sum())
district=int(foreign["district"].nunique())
cagr=cfs["CAGR"].mean()

t1,t2,t3=st.columns(3,gap="large")
with t1:
    st.info("Visitors",icon="📌")
    st.metric(label="No. of Vistors",value=millify(visitors, precision=2))
with t2:
    st.info("Districts",icon="📌")
    st.metric(label="No. of District",value=f"{district:}")
with t3:
    st.info("CAGR",icon="📌")
    st.metric(label="Average CAGR",value=f"{cagr:}")
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
    options=foreign["year"].unique()
)
yfs=foreign.query("year==@Year2")
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

def graph3():
    dom_max = cfs.sort_values(by="CAGR", ascending=False).head(3)
    dom_max = dom_max.reset_index()
    dom_max.drop("index", axis=1, inplace=True)
    fig1 = px.bar(dom_max, x="district", y="CAGR",title="Top 3 District Based on Domestic CAGR")
    fig1.update_traces(marker_color = '#f9c068',)
    fig1.update_layout(xaxis=dict(showgrid=False))
    left,right=st.columns(2)
    left.plotly_chart(fig1,use_container_width=True)
    dom_min = cfs.sort_values(by="CAGR", ascending=True).head(3)
    dom_min = dom_min.reset_index()
    dom_min.drop("index", axis=1, inplace=True)
    fig2 = px.bar(dom_min, x="district", y="CAGR",title="Bottom 3 District Based on Domestic CAGR")
    fig2.update_traces(marker_color = '#f9c068',)
    fig2.update_layout(xaxis=dict(showgrid=False))
    right.plotly_chart(fig2,use_container_width=True)

graph3()