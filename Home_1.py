import streamlit as  st
import pandas as pd
import glob
import os
import datetime
from PIL import Image
import plotly.express as px
import streamlit_authenticator as stauth
#from PIL import Image
from yaml.loader import SafeLoader
import yaml


with open(r"C:\Users\v126852\AppData\Local\Programs\Python_Sandbox\GIAM.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

#Setting up logon page and  configurations for the users
#hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.set_page_config(page_title="GIAM Liquidity Analsys dashboard" , page_icon = ":tada:" ,  layout = "wide")

    #------- HEADER SECTION
    image = Image.open(r"C:\Users\v126852\AppData\Local\Programs\Python_Sandbox\Generali_Logo.jpg")
    new_image = image.resize((300, 100))
    st.image(new_image, caption='GIAM-RM')

    st.subheader("Historical Stress Test Analysis")
    st.title("Drill-Down analysis for historical stress tests for GIAM IC ")
    st.write("Dashboard to enable business get better insightes into liquidity risk data generatd by MSCI Risk Manager")

    #------- DATA PROCESSING SECTION
    stress_Scenario = st.selectbox(
        'Select a Stress scenario',
        ('Mild Recession','Deepening Energy crisis','Sharp Global recession','Asian Crisis (1997) 1D (USD) [rm4demo@riskmetrics]'))
    st.write(stress_Scenario)
    uploaded_file = st.file_uploader("Choose a stress test report from RiskMetrics", type ='xlsx')

    if uploaded_file : 
        st.markdown('---')
        df = pd.read_excel(uploaded_file, engine = 'openpyxl', sheet_name='TestSheet' , skiprows= 0,thousands=',')
        #st.dataframe(df)
        #df2=df.query("Level == '1'")   
        fig = px.treemap(df, path=['Class-1','Class_0','Class_2','Class_3','Class_4','Class_5','Name'], values=stress_Scenario,color_continuous_scale='RdBu')
        #fig = px.sunburst(df, path=['Class-1','Class_0','Class_2','Class_3','Class_4','Class_5','Name'], values=stress_Scenario,color_continuous_scale='RdBu')
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        fig.update_layout(width=1300,height=900)
        st.plotly_chart(fig)


    st.write('Developed by Ujjwal Shankar for GIAM')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


