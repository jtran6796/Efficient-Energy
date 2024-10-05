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


DATE_COLUMN = 'date/time'
DATA_URL = ""

    @st.cache_data
    def load_data(nrows):
        data = pd.read_excel(DATA_URL, nrows=nrows) #https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Done! (using st.cache_data)")

    st.subheader('Raw data')
    st.map(data)








