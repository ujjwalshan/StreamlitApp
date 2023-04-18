import streamlit as  st
import pandas as pd
import glob
import os
import datetime
from PIL import Image
#import plotly.express as px
#from PIL import Image

st.set_page_config(page_title="GIAM Liquidity Analsys dashboard" , page_icon = ":tada:" ,  layout = "wide")

#------- HEADER SECTION

st.subheader("Standard liquidity report")
st.title("Data analsys for liquidity risk measurement")
st.write("Dashboard to enable business get better insightes into liquidity risk data generatd by MSCI Risk Manager")

image = Image.open(r"C:\Users\v126852\AppData\Local\Programs\Python_Sandbox\Generali_Logo.jpg")

st.image(image, caption='Genrerali Investments')

Reporting_date = st.date_input("Select Reporting date")
st.write(Reporting_date)
#Read the latest data
folder_path = r'\\corp.generali.net\FSGRUPPOGENERALI\DISCO_V_GI\RiskMetrics\07_GIAM\01_Liquidity\02_Weekly_Standard_Liquidity'
#folder_path = r'D:\Data\v126852\Documents'
file_type = r'\Liquidity GIAM.Standard Liquidity Report.Liquidity_Aggr*' #Looks for a file that matches a set regular expression
files = glob.glob(folder_path + file_type) 
max_file = max(files, key=os.path.getctime) #Finds the latest available file in order to process it
max_file_nameArr = max_file.split('.')    
file_Date =  max_file_nameArr[5]            #extracts the date of the file to be used in the output 
max_file = r"\\corp.generali.net\FSGRUPPOGENERALI\DISCO_V_GI\RiskMetrics\07_GIAM\01_Liquidity\02_Weekly_Standard_Liquidity\Liquidity GIAM.Standard Liquidity Report.Liquidity_Aggr.20220831.csv"
dfPos_Level = pd.read_csv (max_file)        #read the latest file and load it into the pandas dataframe
dfPor_Level = dfPos_Level.query('level == 0') #Filter the file only portfolio level , this also drops all the position level data that is not needed.

#option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

st.dataframe(dfPor_Level)
