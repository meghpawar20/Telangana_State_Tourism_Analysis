import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Telangana State Tourism Analysis",
    page_icon="	:chart_with_upwards_trend:",
)



image=Image.open("homepage.png")
st.header("Telangana State Tourism Analysis 📈📉📊")
st.markdown("---")

st.write("The Dashboard provides a comprehensive view of the Tourism Industry in Telangana State. It identifies the top and bottom performing district based on visitors, CAGR.")
st.image(image)
