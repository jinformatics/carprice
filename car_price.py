import streamlit as st
import pandas as pd
import pickle

st.markdown("<h1 style= 'text-align:center; color : red;'> Old Car Price Predictor </h1>" , unsafe_allow_html = True)
     
data = pd.read_csv('clean_data.csv')
Name = data['name'].drop_duplicates()
company = st.selectbox('Company' ,data['company'].unique())
name =st.selectbox('CarName' ,Name)
year =  st.slider('Year',2000 , 2021 , 2005 ,1)

kms_driven = st.slider('Kms-driven ',10000 , 500000 , 50000 ,10000)

option =['Petrol','Diesel','LPG']
fuel = st.selectbox('Fuel-Type ' ,option)

model = pickle.load(open('model.pkl','rb'))
val = model.predict(pd.DataFrame([[name ,company ,year ,kms_driven, fuel]] , columns=[ 'name' ,'company' ,'year' ,'kms_driven', 'fuel_type']))
df = pd.DataFrame([[company , name , year ,kms_driven , fuel]], columns=['Company','Name' ,'Year' ,'Kms_driven', 'Fuel_type'])
st.table(df)
if (val > 0):     
     st.write('Price =', float('%.2f'%val))
     
else:
     st.markdown("<p style= 'text-align:center; color :red;'> choose another input  </p>" , unsafe_allow_html = True)


hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} body {background-color:cyan;}</style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

