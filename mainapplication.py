# -*- coding: utf-8 -*-
"""mainapplication.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rF0U5spUo5I8nyHla5bGOQpWx-ec8YRk
"""

from os import write
import streamlit as st
import numpy as np
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


header = st.beta_container()
body = st.beta_container()
classify_container = st.beta_container()

def classify(a):
    filename = 'model_pickle'
    model_reloaded = pickle.load(open(filename, 'rb'))
    
    text =[]
    text.append(a)
    ab = model_reloaded.predict_proba(text)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    result = ab.tolist()
    test_res = result[0]
    li_goals = ["No Poverty","Zero Hunger","Good Healthand Well Being","Quality Education"
            ,"Gender Equality","Clean Water and Sanitation","Affordable  and Clean Energy"
            ,"Decent Work and Economic Growth","Industry,Innovation and Infrastructure"
            ,"Reduced Inequalites","Sustainable Cities and Communities",
            "Responsible Consumption and Production","Climate Action","Life Below Water","Life On Land"]
    t =zip(li_goals,test_res)
    df_predic = pd.DataFrame(t,columns=["SDG","Probability"])
    df_predic.index = df_predic.index + 1
    return((df_predic))
    


with header:
    titl, imga = st.beta_columns(2)
    st.title('Sustainable Development Goal Classification') 
     

with body:
    rawtext = st.text_area('Enter Text Here')
  

    uploaded_file = st.file_uploader(
        'Choose your .txt file', type="txt")
    if uploaded_file is not None:
        rawtext = str(uploaded_file.read(), 'utf-8')
    if st.button('Results'):
        with classify_container:
            if rawtext == "":
                st.header('Results')
                st.write('Please enter text or upload the file')
            else:
                result = classify(rawtext)
                st.header('Sustainable development Classification Results')
                st.dataframe(result)
                df = pd.DataFrame(result, columns = ["Probability"])
                st.area_chart(df)