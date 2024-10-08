import streamlit as st
import pandas as pd
import geocoding
import solar

st.title('Efficient Energy Calculator')

with st.form("my_form"):
    
    # Get the monthly bill cost from user
    monthly_bill = st.number_input("Monthly Bill Amount ($)", min_value = 20, max_value = 500)

    street = st.text_input("Street Address",max_chars = 50)

    city = st.text_input("City",max_chars=50)

    state = st.text_input("State Initial",max_chars=2)

    submitted = st.form_submit_button("Submit")

    if submitted:
        #need to fix this where all boxes must be filled before anything works
        if (state == "" or city == "" or street == ""):
            st.write("Please fill in all the boxes")

try:
    lat_long = geocoding.get_coordinates(street + ", " + city + ", " + state)
    solar.solar_api_request(lat_long)
    solar.lifetime_savings_best_fit()
    m, b = solar.lifetime_savings_best_fit()

    # Display solar panel count
    with st.form('solar_form'):
        num_solar_panels = st.slider('Choose the number of Solar Panels', 4, solar.solar_max_panels(), 15)
        yearly_energy = solar.solar_estimation(lat_long, num_solar_panels)
        
        st.form_submit_button("Solar estimates")
        # panels count slider somewhere
        st.write("The potential amount of energy gained yearly from Solar:☀️", yearly_energy, "kW")
        st.write()


        lifetime_savings = solar.solar_savings(num_solar_panels, m, b)
        lifetime_bill_no_solar = monthly_bill * 12 * 20

        st.write("Your Lifetime Bill without Solar: $", monthly_bill * 12 * 20)
        st.write("Your Lifetime Savings with Bill:💸 $", solar.solar_savings(num_solar_panels, m, b))
        st.write("Your Lifetime Bill with Solar: $", monthly_bill * 12 * 20 - lifetime_savings)
        # st.write(solar.solar_max_panels())
        # st.write(solar.solar_finances())
except:
    pass
            




