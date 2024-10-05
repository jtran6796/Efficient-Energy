import streamlit as st
import pandas as pd
import requests

st.title('Efficient Energy Calculator')

st.form("my_form"):

    tot_kWh = st.number_input("Insert your monthly kW/h")

    sq_ft_stat = st.selectbox("Total Square Footage", ("Less than 1,000", "1,000 - 1,499", "1,500 - 1,999", "2,000 - 2,499", "2,500 - 2,999", "3,000 or more"))

    address = st.text_input("Insert your address")

if(st.form_submit_button("Submit, "))

#geocoding API
#https://developers.google.com/maps/documentation/geocoding/requests-geocoding
url = 'https://solar.googleapis.com/v1/dataLayers:get?'
r_geo = requests.get(url + address)



#solar API datalayers endpoint
#https://developers.google.com/maps/documentation/solar/data-layers
url = 'https://solar.googleapis.com/v1/dataLayers:get?'

r = requests.get(url + r_geo )










