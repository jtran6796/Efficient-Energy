import streamlit as st
import streamlit_option_menu as option_menu 
import pandas as pd

st.title('Efficient Energy Calculator')

with st.form("my_form"):
    dryer_stat = st.selectbox("How many times do you use your dryer a week?", ("1", "2", "3", "4+"))

    sq_ft_stat = st.selectbox("Total Square Footage", ("Less than 1,000", "1,000 - 1,499", "1,500 - 1,999", "2,000 - 2,499", "2,500 - 2,999", "3,000 or more"))

    fan_stat = st.selectbox("How many hours do you use your fan?", ("1", "2", "3", "4+"))

    fridge_stat = st.selectbox("How many fridges are in your household?", ("1", "2", "3+"))

    st.form_submit_button("Submit")










