from dataclasses import dataclass
import streamlit as st
import datetime as dt
import requests
import pytz

'''
# TaxiFareModel front
'''
st.markdown('''##Taxifare Predictor''')

st.markdown('''
            ## Please insert information about your trip below:
''')

pickup_date = st.date_input("Date")
pickup_time = st.time_input("Time")
pickup_datetime = dt.datetime.combine(pickup_date,pickup_time)
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.slider('Passenger count', 1, 8)

st.markdown('''
            Thank you for inputing your trip details!
''')

url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_latitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count}

response = requests.get(url,params).json()

if st.button('Request prediction'):
    # print is visible in the server output, not in the page
    print('Calculating...')
    st.write('We are predicting your fare...')
    st.write(f'Your fare prediction is {response["fare"]}')
    st.write('Please note: Further clicks are not visible but are executed.')
else:
    st.write('You have not requested a prediction yet...')
