import streamlit as st
import streamlit_option_menu as option_menu 
import pandas as pd

st.title('Efficient Energy Calculator')

dryer_stat = st.selectbox("How many times do you use your dryer a week?", ("1", "2", "3", "4+"))

fan_stat = st.selectbox("How many hours do you use your fan?", ("1", "2", "3", "4+"))

fridge_stat = st.selectbox("How many fridges are in your household?", ("1", "2", "3+"))

state_stat = st.selectbox("What state do you live in?", ("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")
)

state_dict = {
    "northeast" : ["Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Pennsylvania"],
    "midwest" : ["Ohio", "Indiana", "Illinois", "Iowa", "Michigan", "Wisconsin", "Minnesota", "North Dakota", "South Dakota", "Nebraska", "Kansas", "Missouri"],
    "south" : ["Delaware", "Maryland", "Virginia", "West Virginia", "North Carolina", "South Carolina", "Georgia", "Florida", "Alabama", "Mississippi", "Tennessee", "Kentucky", "Arkansas", "Louisiana", "Oklahoma", "Texas"],
    "west" : ["Montana", "Idaho", "Wyoming", "Nevada", "Utah", "Colorado", "New Mexico", "Arizona", "Washington", "Oregon", "California", "Hawaii", "Alaska"]
}

st.button("Submit", on_click)

region = state_dict.get(state_stat)

DATA_URL = ""

async def region_stat(dfs):
    if region == "northeast":
        DATA_URL = "https://www.eia.gov/consumption/residential/data/2020/c&e/xls/ce1.2.xlsx"
    elif region == "midwest":
        DATA_URL = "https://www.eia.gov/consumption/residential/data/2020/c&e/xls/ce1.3.xlsx"
    elif region == "south":
        DATA_URL = "https://www.eia.gov/consumption/residential/data/2020/c&e/xls/ce1.4.xlsx"
    elif region == "west":
        DATA_URL = "https://www.eia.gov/consumption/residential/data/2020/c&e/xls/ce1.5.xlsx"
    await DATA_URL
    dfs = pd.read_excel(DATA_URL, sheet_name=None) #https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython







