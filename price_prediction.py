# Importing dependencies:

import streamlit as st
import os,pickle
import pandas as pd
from PIL import Image
import numpy as np

# Create a Streamlit app

st.write("""
# MSDE5 : ML Project
## Property Price Prediction App

This app predicts the **Property Price**
""")

st.sidebar.image("https://miro.medium.com/v2/resize:fit:1370/1*yjQ2safdygCd9y4HbA48oA.png", width=300)
st.sidebar.header('User Input Parameters')

# Define input features
def user_input_features():
    OldNew = st.sidebar.slider('Old/New', 0, 1)
    Duration = st.sidebar.slider('Duration', 0, 1)
    Detached = st.sidebar.slider('Detached', 0, 1)
    FlatsMaisonettes = st.sidebar.slider('Flats/Maisonettes', 0, 1)
    OtherType = st.sidebar.slider('Other_Type', 0, 1)
    SemiDetached = st.sidebar.slider('Semi-Detached', 0, 1)
    Terraced = st.sidebar.slider('Terraced', 0, 1)
    StandardPayment = st.sidebar.slider('Standard Payment', 0, 1)
    NonStandardPayment = st.sidebar.slider('Non-Standard Payment', 0, 1)
    CountyCatHigh = st.sidebar.slider('County_Cat_High', 0, 1)
    CountyCatLow = st.sidebar.slider('County_Cat_Low', 0, 1)
    CountyCatMedium = st.sidebar.slider('County_Cat_Medium', 0, 1)
    CountyCatVeryHigh = st.sidebar.slider('County_Cat_Very High', 0, 1)
    data = {'Old/New': OldNew,
            'Duration': Duration,
            'Detached': Detached,
            'Flats/Maisonettes': FlatsMaisonettes,
            'Other_Type': OtherType,
            'Semi-Detached': SemiDetached,
            'Terraced': Terraced,
            'Standard Payment': StandardPayment,
            'Non-Standard Payment': NonStandardPayment,
            'County_Cat_High': CountyCatHigh,
            'County_Cat_Low': CountyCatLow,
            'County_Cat_Medium': CountyCatMedium,
            'County_Cat_Very High': CountyCatVeryHigh}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


# Load your pre-trained model
model = pickle.load(open("property_price_dt.pkl", "rb"))

# Make predictions
if st.sidebar.button('Predict Price'):
    prediction = model.predict(df)
    st.write(f'Predicted Price: {prediction[0]}')
