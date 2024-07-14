# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:19:17 2024

@author: ASUS
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

credit_model=pickle.load(open("trained_model.sav", "rb"))
wine_model=pickle.load(open("wine_quality.sav", "rb"))

with st.sidebar:
    selected = option_menu("Multiple prediction Web_App with ML",
                           ["Credit Transfer","Wine Quality"],
                           
                           icons=["credit-card","person"],
                           
                           default_index=0)
    

    
if(selected=="Credit Transfer"):
    
    # Title for credit transfer
    st.title("Credit Transfer Web_App by ML")
    
    col1,col2,col3,col4=st.columns(4)
    
    #Getting the input from user
    with col1:
        Time=st.text_input("Enter the time")
    with col2:
        V1=st.text_input("Enter the V1")
    with col3:
        V2=st.text_input("Enter the V2")
    with col4:
        V3=st.text_input("Enter the V3")
    with col1:
        V4=st.text_input("Enter the V4")
    with col2:
        V5=st.text_input("Enter the V5")
    with col3:
        V6=st.text_input("Enter the V6")
    with col4:
        V7=st.text_input("Enter the V7")
    with col1:
        V8=st.text_input("Enter the V8")
    with col2:
        V9=st.text_input("Enter the V9")
    with col3:
        V10=st.text_input("Enter the V10")
    with col4:
        V11=st.text_input("Enter the V11")
    with col1:
        V12=st.text_input("Enter the V12")
    with col2:
        V13=st.text_input("Enter the V13")
    with col3:
        V14=st.text_input("Enter the V14")
    with col4:
        V15=st.text_input("Enter the V15")
    with col1:
        V16=st.text_input("Enter the V16")
    with col2:
        V17=st.text_input("Enter the V17")
    with col3:
        V18=st.text_input("Enter the V18")
    with col4:
        V19=st.text_input("Enter the V19")
    with col1:
        V20=st.text_input("Enter the V20")
    with col2:
        V21=st.text_input("Enter the V21")
    with col3:
        V22=st.text_input("Enter the V22")
    with col4:
        V23=st.text_input("Enter the V23")
    with col1:
        V24=st.text_input("Enter the V24")
    with col2:
        V25=st.text_input("Enter the V25")
    with col3:
        V26=st.text_input("Enter the V26")
    with col4:
        V27=st.text_input("Enter the V27")
    with col1:
        V28=st.text_input("Enter the V28")
    with col2:
        Amount=st.text_input("Enter the Amount")
    
    # Empty variable
    credit_check=""
    if st.button("Transfer Status"):
        credit_pred=credit_model.predict([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10,V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]])
    
        if(credit_pred[0]==0):
            credit_check= "Legit Transfer"
        else:
            credit_check="Fraud Transfer"
            
    st.success(credit_check)
    



if(selected=="Wine Quality"):
    
    # Title for wine quality testing
    st.title("Wine Quality Test Web_App by ML")
    
    col4,col5,col6=st.columns(3)
    
    # Getting input from user
    with col4:
        fixedacidity=st.text_input("F_acidity")
    with col5:
        volatileacidity=st.text_input("V_acidity")
    with col6:
        citricacid=st.text_input("C_acid")
    with col4:
        residualsugar=st.text_input("R_sugar")
    with col5:
        chlorides=st.text_input("clorides")
    with col6:
        freesulfurdioxide=st.text_input("F_S_dioxide")
    with col4:
        totalsulfurdioxide=st.text_input("T_S_dioxide")
    with col5:
        density=st.text_input("Density") 
    with col6:
        pH=st.text_input("PH")
    with col4:
        sulphates=st.text_input("Sulphate")
    with col5:
        alcohol=st.text_input("Alcohol")
    
    # Empty variable
    quality_test=""
    if st.button("Test Quality"):
        quality_pred=wine_model.predict([[fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol]])
        
        if(quality_pred[0]==0):
            quality_test= "Bad Quality"
        else:
            quality_test="Good Quality"
            
    st.success(quality_test)
    
    
        
        
        
        