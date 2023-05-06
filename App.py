import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pickle
import plotly.express as px
import altair as alt 
pip install pycaret
import pycaret
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

data = pd.read_csv("final dataset.csv")

def run_website():
    
   with st.sidebar:
        selected = option_menu('Venture Capital Analysis Website',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Search',
                            'Company Profile',
                            'Prediction'],
                            default_index=0)
        
   if(selected == 'Prediction'):
        scaler = StandardScaler()

        # loading the saved models

        model = pickle.load(open("par_model.pkl",'rb'))
            
        # page title
        st.title('Company growth potential prediction')
            
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
            
        with col1:
            total_funding_c = st.text_input('Total Funding Till Date')
            

        with col2:
            last_valuation_c = st.text_input('Last Valuation')
        
        with col3:
            last_round_size_c = st.text_input('Amount Raised During Last Funding Round')
        
        with col1:
            revenue_c = st.text_input('Revenue for Latest Financial Year')

        with col2:
            revenue_growthpercent = st.text_input('Revenue Growth Compared to Last Financial Year')

        with col3:
            EBIT_c = st.text_input('Earnings before Interest and Fax')

        with col1:
            employee_growth_6percent = st.text_input('Employee Growth Past 6 Months')

        with col2:
            employee_growth_12percent = st.text_input('Employee Growth Past 12 Months')


        with col3:
            num_founders = st.text_input('Number of Founders')

        with col1:
            num_funding_rounds = st.text_input('Number of Funding Rounds')

        with col2:
            num_shareholders = st.text_input('Number of Shareholders')

        with col3:
            median_share = st.selectbox('Median Share in %')

            
            # creating a button for Prediction
            
        if st.button('Predict Growth Potential Score'):

                total_funding_c = scaler.transform(float(total_funding_c))  
                last_valuation_c = scaler.transform(float(last_valuation_c))  
                last_round_size_c = scaler.transform(float(last_round_size_c))  
                revenue_c = scaler.transform(float(revenue_c))  
                revenue_growthpercent = scaler.transform(float(revenue_growthpercent)) 
                EBIT_c = scaler.transform(float(EBIT_c)) 
                employee_growth_6percent = scaler.transform(float(employee_growth_6percent)) 
                employee_growth_12percent = scaler.transform(float(employee_growth_12percent)) 
                num_founders = scaler.transform(float(num_founders)) 
                num_founding_rounds = scaler.transform(float(num_founding_rounds))  
                num_shareholders = scaler.transform(float(num_shareholders)) 
                median_share = scaler.transform(float(median_share)) 

                prediction = model.predict([total_funding_c, last_valuation_c, last_round_size_c, 
                                             revenue_c, revenue_growthpercent, EBIT_c, 
                                             employee_growth_6percent, employee_growth_12percent, 
                                             num_founders,num_founding_rounds,num_shareholders,
                                             median_share])
                
                st.write('Growth Potential Score: ', str(int(prediction)))



run_website()
