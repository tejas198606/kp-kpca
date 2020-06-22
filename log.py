import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model1111.pkl","rb") 
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All on Board"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    prediction=classifier.predict([[age,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(prediction)
    return prediction

def main():
    st.title("CANCER")   
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> CANCER APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","")      
    cp = st.text_input("cp","")
    trestbps = st.text_input("trestbps","")
    chol = st.text_input("chol","")      
    fbs = st.text_input("fbs","")
    restecg = st.text_input("restecg","")
    thalach = st.text_input("thalach","")
    exang = st.text_input("exang","")      
    oldpeak = st.text_input("oldpeak","")
    slope = st.text_input("slope","")
    ca = st.text_input("ca","")
    thal = st.text_input("thal","")
    
    
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()