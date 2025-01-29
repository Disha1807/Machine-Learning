import pickle
import streamlit as st
import pandas as pd


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define Streamlit app

st.set_page_config(
    page_title='Airline Passenger Referral Prediction', 
    # page_icon = im, 
    layout = 'centered', 
    initial_sidebar_state = 'auto'
)
st.title('Airline Passenger Referral Prediction')

st.info('''The project aims to predict whether a passenger referred by an existing customer will book a flight or not.''')


#user input for each feature

seat_comfort = st.slider("Seat Comfort", min_value=0, max_value=5)
cabin_service = st.slider("Cabin Service", min_value=0, max_value=5)
food_bev = st.slider("Food & Beverages", min_value=0, max_value=5)
entertainment = st.slider("Entertainment", min_value=0, max_value=5)
ground_service = st.slider("Ground Service", min_value=0, max_value=5)
value_for_money = st.slider("Value for money", min_value=0, max_value=5)

# Create a dropdown menu with options
traveller_type_options = ['Solo Leisure','Couple Leisure','Family Leisure','Business']
traveller_type = st.selectbox("Traveller Type", traveller_type_options)

label_for_cabin = ['Economy Class','Business Class','Premium Economy','First Class']
cabin = st.selectbox("Cabin", label_for_cabin)


if st.button("Get Recommendation"):   

    input_data = pd.DataFrame({
        'seat_comfort':[seat_comfort],
        'cabin_service':[cabin_service],
        'food_bev':[food_bev],
        'entertainment':[entertainment],
        'ground_service':[ground_service],
        'value_for_money':[value_for_money],
    })    


    # Make prediction using the loaded model
    prediction = model.predict(input_data)  

    if prediction[0] == 1:
        st.success('Recommended: YES')
    else:
        st.info('Recommended: NO')
