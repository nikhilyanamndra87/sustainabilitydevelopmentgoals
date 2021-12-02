# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TwnlwVa2ounLX474forzWYz_xWJDUksx
"""

pip install streamlit

import nltk
from os import write
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize 
import numpy as np
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

header = st.beta_container()
body = st.beta_container()
classify_container = st.beta_container()

def classify(textfile):
    model = 'model_pickle'
    model_reloaded = pickle.load(open(model, 'rb'))
    
    text =[]
    text.append(textfile)
    probabs = model_reloaded.predict_proba(text)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    result = probabs.tolist()
    test_res= result[0]
    li_goals = ["No Poverty","Zero Hunger","Good Health and Wellbeing","Quality Education"
            ,"Gender Equality","Clean Water and Sanitation","Affordable and Clean Energy"
            ,"Decent Work and Economic Growth","Industry,Innovation and Infrastructure"
            ,"Reduced Inequalites","Sustainable Cities and Communities",
            "Responsible Consumption and Production","Climate Action","Life Below Water","Life On Land"]
    t =zip(li_goals,test_res)
    df_predic = pd.DataFrame(t,columns=["Sustainable Development Goal","Probability"])
    df_predic.index = df_predic.index + 1
    fi= df_predic.sort_values("Probability", ascending = [False])
    return((fi))
import nltk
nltk.download('stopwords')
stop = stopwords.words('english')
porter = PorterStemmer()

def removestopwords(text):
    text = [word.lower() for word in text.split() if word.lower() not in stop]
    return " ".join(text)

def stem(stem_text):
    stemtext = [porter.stem(word) for word in stemtext.split()]
    return " ".join(stemtext)

with header:
    titl, imga = st.beta_columns(2)
    imga.image('index.png')
    titl.title('Sustainable Development Goals Classifier of un')

with body:
    #Taking text input using one of the 3 ways: entering text, using sample text files or uploading a new text file.
    rawtext = st.text_area('Enter Text Here')
    sample_col, upload_col = st.beta_columns(2)
    sample = sample_col.selectbox('Or select a sample CSR file',  ('None','AsianPaints-csr.txt','AxisBank-csr.txt','tata-csr','techmahindra-csr','zee-csr'))
    if sample != 'None':
        file = open(sample, "r", encoding='utf-8')
        rawtext = file.read()

    uploaded_file = upload_col.file_uploader('Or upload a txt file', type="txt")
    if uploaded_file is not None:
        rawtext = str(uploaded_file.read(), 'utf-8')
    if st.button('Classify'):
        
        #Classification starts
        with classify_container:
            if rawtext == "":
                st.header('Oops! :(')
                st.write('Please enter text or upload a file')
            else:
                #printing the uploaded text on webpage
                expand = st.beta_expander("Expand to see the uploaded text")
                with expand:
                	st.write(rawtext)
                st.text("")
                
                #Removing stop words and stemming words to their root word for better result
                rawtext = removestopwords(rawtext)
                rawtext = stem(rawtext)
                
                #Text is classified and printing results	 
                result = classify(rawtext)
                st.subheader('Result')
                st.dataframe(result)
                data = pd.DataFrame(result, columns = ["Probability"])
                data2 = pd.DataFrame(result)
                st.text("")
                
                #Creating a bar plot for probabilities
                st.subheader("Probability chart result")
                st.line_chart(data)
                st.subheader("Conclusion of it")
                st.write("The uploaded text matches closest to the goal-",data2["Sustainable Development Goal"].iloc[0], ", with probability ", data2["Probability"].iloc[0])
