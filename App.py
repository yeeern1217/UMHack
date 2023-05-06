import pickle
import sklearn
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


def load_model():
    loaded_model = pickle.load(open("VCmodel.pkl", 'rb'))
    return loaded_model

def normalize(type,val):
    if type=="Funding":
        return (val-(1.373136e+06))/(1.645224e+07)
    elif type=="Revenue":
        return (val-(3.460575e+06))/(3.595783e+07)
    elif type=="ebit":
        return (val-(-1.068171e+05))/(7.485605e+06)	
    elif type=="E6":
        return (val-(8.060758))/(38.771438)	
    elif type=="E12":
        return (val-(25.505254))/(79.271844)	
    elif type=="Founders":
        return (val-(2.428510))/(2.629927)
    elif type=="Rounds":
        return (val-(0.203746))/(0.650948)	
    elif type=="Shareholder":
        return (val-(6.439745))/(14.708537)
    elif type=="Median":
        return (val-(42.792926))/(31.694526)


# page title
st.title('Company growth potential prediction')

# getting the input data from the user
col1, col2, col3 = st.columns(3)
with col1:
    funding = st.number_input(label='Total Funding Till Date')

with col2:
    revenue = st.number_input(label='Revenue for Latest Financial Year')

with col3:
    EBIT = st.number_input(label='Earnings before Interest and Fax')

with col1:
    e6 = st.number_input(label='Employee Growth Past 6 Months')

with col2:
    e12 = st.number_input(label='Employee Growth Past 12 Months')


with col3:
    founders = st.number_input(label='Number of Founders')

with col1:
    rounds = st.number_input(label='Number of Funding Rounds')

with col2:
    shareholders = st.number_input(label='Number of Shareholders')

with col3:
    median = st.number_input(label='Median Share in %')

features = {
  'Funding': funding, 'Revenue':revenue, 'ebit':EBIT,
  'E6':e6, 'E12':e12, 'Founders':founders, 'Rounds':rounds,
  'Shareholder':shareholders, 'Median':median}

adjusted_features=[normalize("Funding",funding), normalize("Revenue",revenue),normalize("ebit",EBIT),
                   normalize("E6",e6),normalize("E12",e12),normalize("Founders",founders),
                   normalize("Rounds", rounds), normalize("Shareholder",shareholders),normalize("Median", median)]

input=np.array(adjusted_features).reshape(1, -1)


            # creating a button for Prediction

if st.button('Predict Revenue Growth'):
  loaded = load_model()
  prediction = loaded.predict(input)
  st.write('Based on features values, the revenue growth is ' + str(int(prediction)))
