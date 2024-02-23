from turtle import right
import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Comparison Indicators", page_icon="📊",layout="wide")
st.header("Comparison Indicators📊")

def getData():
    res=pd.read_csv("pages\Ratio.csv")
    return res
r=getData()
def graphs():
    g1=r.head(3)
    fig1 = px.bar(g1, x="district", y="Ratio",title="Top 3 Districts with High Domestic to Foreign Ratio" )
    fig1.update_traces(marker_color = '#f9c068',)
    fig1.update_layout(xaxis=dict(showgrid=False))
    fig1.update_xaxes(tickangle=45)
    g2=r.tail(3)
    fig2 = px.bar(g2, x="district", y="Ratio",title="Bottom 3 Districts with Low Domestic to Foreign Ratio" )
    fig2.update_traces(marker_color = '#f9c068',)
    fig2.update_layout(xaxis=dict(showgrid=False))
    fig2.update_xaxes(tickangle=45)
    left,right= st.columns(2)
    

    left,right= st.columns(2)
    left.plotly_chart(fig1,use_container_width=True)
    right.plotly_chart(fig2,use_container_width=True)
graphs()
st.markdown("---")
def graph2():
    st.subheader("Domestic to Foreign Visitors Ratio")
    st.dataframe(r)
  
graph2()