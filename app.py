import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

#load model and structure

model=joblib.load("water_quality_model.pkl")
model_cols=joblib.load("model_columns.pkl")

# Load external CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")


#create an user interface

st.title("Water Pollutants Predictor")
st.write("predict the water pollutants based on year and station ID")

#take user input values

year_input=st.number_input("enter year",min_value=2000,max_value=2100,value=2022)
station_id=st.text_input("enter station number",value='1')

#to encode and then predict

if st.button('Predict'):
    if not station_id:
        st.warning("please enter valid ID")
    else:
        #we prepare the input
        input_df=pd.DataFrame({'year':[year_input],'id':[station_id]})
        input_encoded=pd.get_dummies(input_df,columns=['id'])
        
        #align with model columns
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col]=0
        input_encoded=input_encoded[model_cols]  
        
        #predict 
        predicted_pollutants=model.predict(input_encoded)[0]
        pollutants=['O2',"NO3","NO2","SO4","PO4",'CL'] 
        st.subheader(f"Predicted pollutants for the station '{station_id}' in {year_input}") 
        predicted_values={}
        l=[]
        for p,val in zip(pollutants,predicted_pollutants):
            st.write(f'{p} : {val:.2f}')    
            l.append(round(val,2))
        
        st.session_state.l = l 

            
            # to run  python -m streamlit run app.py

# define l globally to be accessible in both buttons
if 'l' not in st.session_state:
    st.session_state.l = []

if st.button('safe or not'):
    if not st.session_state.l:
        st.warning("Please click on 'Predict' first to get values.")
    else:
        l = st.session_state.l
        s = []

        if l[0] < 6.5 or l[0] > 14:
            s.append(f'O2 limit is 6.5-14 but it is {l[0]}')
        if l[1] > 50:
            s.append(f'NO3 limit is 0-50 but it is {l[1]}')
        if l[2] > 3:
            s.append(f'NO2 limit is 0-3 but it is {l[2]}')
        if l[3] > 250:
            s.append(f'SO4 limit is 0-250 but it is {l[3]}')
        if l[4] > 0.5:
            s.append(f'PO4 limit is 0-0.5 but it is {l[4]}')
        if l[5] > 250:
            s.append(f'CL limit is 0-250 but it is {l[5]}')

        if s:
            s.append("----------------SO IT IS NOT SAFE----------------------- ")
            for i in s:
                st.write(i)
        else:
            st.write("It is SAFE")
