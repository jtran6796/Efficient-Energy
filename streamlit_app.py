import streamlit as st
import streamlit_option_menu as option_menu 
import pandas as pd
import geocoding
import solar

st.title('Efficient Energy Calculator')

with st.form("my_form"):


    sq_ft_stat = st.selectbox("Total Square Footage", ("Less than 1,000", "1,000 - 1,499", "1,500 - 1,999", "2,000 - 2,499", "2,500 - 2,999", "3,000 or more")
    ,index = None,placeholder = "Please select an option")

    street = st.text_input("Street Address",max_chars = 50)

    city = st.text_input("City",max_chars=50)

    state = st.text_input("State Initial",max_chars=2)

    appliance = st.multiselect("Select appliances you regularly use", ("Heating and Cooling", "Water Heater",
    "Lighting", "Refrigerator", "Washer and Dryer", "Electric Oven", "Dishwasher", "TV and cable box"))

    submitted = st.form_submit_button("Submit")

    if submitted:
        #need to fix this where all boxes must be filled before anything works
        if (state == "" or city == "" or street == "" or sq_ft_stat is None):
            st.write("Please fill in all the boxes")
        else:
            match sq_ft_stat:
                case "Less than 1,000" : 
                    st.write("The average electricity usage for your home is 6,802 kWh.")
                    average = 6802
                case "1,000 - 1,499":
                    st.write("The average electricity usage for your home is 9,407 kWh.")
                    average = 9407
                case "1,500 - 1,999":
                    st.write("The average electricity usage for your home is 11,009 kWh.")
                    average = 11009
                case "2,000 - 2,499":
                    st.write("The average electricity usage for your home is 12,173 kWh.")
                    average = 12173
                case "2,500 - 2,999":
                    st.write("The average electricity usage for your home is 13,031 kWh.")
                    average = 13031
                case "3,000 or more":
                    st.write("The average electricity usage for your home is 15,489 kWh.")
                    average = 15489
                case None:
                    st.write("Please Select An Option Before Submitting and " + state)

            

            lat_long = geocoding.get_coordinates(street + ", " + city + ", " + state)
            
            solar.solar_api_request(lat_long)

            thing = solar.solar_estimation(lat_long, 13)

            
            # panels count slider somewhere

            st.write(lat_long)
            st.write(thing)
            st.write("Max Panels")
            # st.write(solar.solar_max_panels())

            st.write(solar.solar_finances())




