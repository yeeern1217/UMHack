import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pickle
import plotly.express as px
import altair as alt 
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()

data = pd.read_csv("final dataset.csv")

def load_model():
    loaded_model = pickle.load(open("par_model.pkl", 'rb'))

def run_website():
    
   with st.sidebar:
        selected = option_menu('Venture Capital Analysis Website',
                            
                            [
                            'Prediction'],
                            default_index=0)
        
   if(selected == 'Prediction'):
        scaler = StandardScaler()
            
        # page title
        st.title('Company growth potential prediction')
            
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        with col1:
            total_funding_c = st.text_input('Total Funding Till Date')
        
        with col2:
            revenue_c = st.text_input('Revenue for Latest Financial Year')

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
            median_share = st.text_input('Median Share in %')


                    # creating a button for Prediction
        
        if st.button('Predict Growth Potential Score'):
                total_funding_c = (float(total_funding_c)-1.22582666e+06)/1.02480673e+07 
                revenue_c = (float(revenue_c)-3.62958388e+06)/3.45839270e+07
                EBIT_c = (float(EBIT_c)-6.20091324e+00)/3.69223645e+01
                employee_growth_6percent = (float(employee_growth_6percent)-3.11255708e+01)/ 1.11832148e+02
                employee_growth_12percent = (float(employee_growth_12percent) - 2.56401771e+00)/2.88048906e+00
                num_founders = (float(num_founders)-1.89497717e-01)/6.25324919e-01
                num_funding_rounds = (float(num_funding_rounds)-5.40612725e+00)/1.24999836e+01
                num_shareholders = (float(num_shareholders)-4.40163699e+01)/  3.23090170e+01
                median_share = (float(median_share)-2.45337900e+02)/1.47928736e+03

                prediction = model.predict([total_funding_c, 
                                             revenue_c, EBIT_c, 
                                             employee_growth_6percent, employee_growth_12percent, 
                                             num_founders,num_funding_rounds,num_shareholders,
                                             median_share])
                
                st.write('Growth Potential Score: ', str(int(prediction)))



run_website()
