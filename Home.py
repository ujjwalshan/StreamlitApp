import streamlit as  st
import pandas as pd
import glob
import os
import datetime
from PIL import Image
#import plotly.express as px
#from PIL import Image

st.set_page_config(page_title="GIAM Liquidity Analsys dashboard" , page_icon = ":tada:" ,  layout = "wide")

image = Image.open(r"C:\Users\v126852\AppData\Local\Programs\Python_Sandbox\Generali_Logo.jpg")

st.image(image, caption='Genrerali Investments')
#------- HEADER SECTION

st.subheader("Standard liquidity report")
st.title("Data Analysis for liquidity risk measurement")
st.write("Dashboard to enable business get better insightes into liquidity risk data generatd by MSCI Risk Manager")

Reporting_date = st.date_input("Select Reporting date")
st.write(Reporting_date)

