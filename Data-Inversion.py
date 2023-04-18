import pandas as pd
import plotly.express as px

uploaded_file = r'D:\Data\v126852\Downloads\IC_Historical_Stress_Tests (1) - Copy.xlsx'
df = pd.read_excel(uploaded_file, engine = 'openpyxl', sheet_name='EU_credit_ST_2022 Scenarios C' , skiprows= 18,thousands=',')


#insert the classification level columns 
df.insert(3, "Class-1",'')
df.insert(4, "Class_0",'')
df.insert(5, "Class_1",'')
df.insert(6, "Class_2",'')
df.insert(7, "Class_3",'')
df.insert(8, "Class_4",'')
df.insert(9, "Class_5",'')

#Loop over the rows 

#Setting classification level 1 to Total 
for index in range(len(df)):
    df['Class-1'].loc[index] = "Total" 

#Set Class0
Class0 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 0:
        Class0 = df['Name'].loc[index]
    df['Class_0'].loc[index] = Class0

#Set Class1
Class1 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 1:
        Class1 = df['Name'].loc[index]
    df['Class_1'].loc[index] = Class1

#Set Class2
Class2 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 2:
        Class2 = df['Name'].loc[index]
    df['Class_2'].loc[index] = Class2

#Set Class3
Class3 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 3:
        Class3 = df['Name'].loc[index]
    df['Class_3'].loc[index] = Class3

#Set Class4
Class4 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 4:
        Class4 = df['Name'].loc[index]
    df['Class_4'].loc[index] = Class4

#Set Class5
Class5 = 'NA'
for index in range(len(df)):
    if df['Level'].loc[index] == 5:
        Class5 = df['Name'].loc[index]
    df['Class_5'].loc[index] = Class5


#Filter the value to only have the level 6 

df2 = df.loc[df['Level'] == 6]

fig = px.treemap(df2, path=['Class_0','Class_1','Class_2'], values='PV' ,color_continuous_scale='balance')

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show
#Output the results to the output file 
#df2.to_excel(r'D:\Data\v126852\Downloads\TestOutput.xlsx',index=False)