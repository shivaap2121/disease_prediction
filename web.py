import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
diabetes_model= pickle.load(open(r"C:\Users\shivr\Documents\disease_prediction_project\training_model\diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\shivr\Documents\disease_prediction_project\training_model\heart_disease_model.sav",'rb'))
parkinsons_model= pickle.load(open(r"C:\Users\shivr\Documents\disease_prediction_project\training_model\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)



if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex (0 = Female, 1 = Male)')
    with col3:
        CP = st.text_input('Chest Pain Type')
    with col1:
        Trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        Chol = st.text_input('Cholesterol Level')
    with col3:
        FBS = st.text_input('Fasting Blood Sugar')
    with col1:
        RestECG = st.text_input('Resting ECG Result')
    with col2:
        Thalach = st.text_input('Max Heart Rate Achieved')
    with col3:
        Exang = st.text_input('Exercise Induced Angina')
    with col1:
        Oldpeak = st.text_input('ST Depression Induced')
    with col2:
        Slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        CA = st.text_input('Number of Major Vessels Colored by Flourosopy')
    with col1:
        Thal = st.text_input('Thalassemia')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach, Exang, Oldpeak, Slope, CA, Thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

# Parkinsons Prediction
elif selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo (Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi (Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo (Hz)')
    with col4:
        MDVP_Jitter = st.text_input('MDVP:Jitter (%)')
    with col5:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter (Abs)')
    with col1:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col2:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer (dB)')
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        Spread1 = st.text_input('Spread1')
    with col5:
        Spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    parkinsons_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons disease'
    st.success(parkinsons_diagnosis)
