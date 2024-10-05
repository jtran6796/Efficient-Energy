import streamlit as st
import streamlit_option_menu as option_menu 
import pandas as pd

st.title('Efficient Energy Calculator')

with st.form("my_form"):


    sq_ft_stat = st.selectbox("Total Square Footage", ("Less than 1,000", "1,000 - 1,499", "1,500 - 1,999", "2,000 - 2,499", "2,500 - 2,999", "3,000 or more")
    ,index = None,placeholder = "Please select an Option")


    submitted = st.form_submit_button("Submit")

    if submitted:
        match sq_ft_stat:
            case "Less than 1,000" : 
                st.write("The average electricity usage for your home is 6,802 kWh")
            case "1,000 - 1,499":
                st.write("The average electricity usage for your home is 9,407 kWh")
            case "1,500 - 1,999":
                st.write("The average electricity usage for your home is 11,009 kWh")
            case "2,000 - 2,499":
                st.write("The average electricity usage for your home is 12,173 kWh")
            case "2,500 - 2,999":
                st.write("The average electricity usage for your home is 13,031 kWh")
            case "3,000 or more":
                st.write("The average electricity usage for your home is 15,489 kWh")
            

            case NONE:
                st.write("Please Select An Option Before Submitting")
