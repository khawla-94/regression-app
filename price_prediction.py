import streamlit as st
import pickle
import pandas as pd

# Load your pre-trained model
model = pickle.load(open("property_price_lgbm_oct23.pkl", "rb"))

# Create a Streamlit app

st.write("""
# Property Price Prediction App
""")

# Define input features
st.sidebar.header('User Input Parameters')
OldNew = st.sidebar.slider('Old/New', 0, 1)
Duration = st.sidebar.slider('Duration', 0, 1)
Detached = st.sidebar.checkbox('Detached')
SemiDetached = st.sidebar.checkbox('Semi-Detached')
Terraced = st.sidebar.checkbox('Terraced')
FlatsMaisonettes = st.sidebar.checkbox('Flats/Maisonettes')
OtherType = st.sidebar.checkbox('Other_Type')
StandardPayment = st.sidebar.checkbox('Standard Payment')
NonStandardPayment = st.sidebar.checkbox('Non-Standard Payment')
CountyCatHigh = st.sidebar.checkbox('County_Cat_High')
CountyCatLow = st.sidebar.checkbox('County_Cat_Low')
CountyCatMedium = st.sidebar.checkbox('County_Cat_Medium')
CountyCatVeryHigh = st.sidebar.checkbox('County_Cat_Very High')

# Create a feature dictionary
input_data = {
    'Old/New': [OldNew],
    'Duration': [Duration],
    'Detached': [Detached],
    'Semi-Detached': [SemiDetached],
    'Terraced': [Terraced],
    'Flats/Maisonettes': [FlatsMaisonettes],
    'Other_Type': [OtherType],
    'Standard Payment': [StandardPayment],
    'Non-Standard Payment': [NonStandardPayment],
    'County_Cat_High': [CountyCatHigh],
    'County_Cat_Low': [CountyCatLow],
    'County_Cat_Medium': [CountyCatMedium],
    'County_Cat_Very High': [CountyCatVeryHigh]
}

# Convert input data to a DataFrame
input_df = pd.DataFrame(input_data)

# Make predictions
if st.button('Predict Price'):
    prediction = model.predict(input_df)
    st.write(f'Predicted Price: {prediction[0]}')
