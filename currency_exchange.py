""" Streamlit front-end for api.weather.gov """
import streamlit as st
from requests import get
from time import sleep
import json

#def load_data() -> None:
    #global rate_symbols, data
    #sleep(2) # just to show that requests may take some time
    #data = get("http://api.exchangeratesapi.io/v1/latest?access_key=c3128c5d3ea7324688906d0190169f07", timeout=3).json()
    #rate_symbols = list(data["rates"].keys())
#load_data()

with open("data.json", 'r') as file:
    data = json.load(file)

# Extracting the currency symbols (keys of the "rates" dictionary)
rate_symbols = list(data["rates"].keys())

# Website title
st.title("Currency Converter")

# Selectbox for initial currency
selection_one = st.selectbox("Currency 1", rate_symbols, index=0, key="Select a starting currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

amount_one = st.number_input("Currency 1 Value")

# Create three columns: left, center, and right
col1, col2, col3 = st.columns([1, 2, 1])

# Use the center column to display the image
with col2:
    st.image("exchange.png", width = 300)  # Uncomment if you want it responsive

# Selectbox for currency to convert to 
selection_two = st.selectbox("Currency 2", rate_symbols, index=0, key="Select a ending currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

if selection_one is "EUR":
    step2 = amount_one * data["rates"][selection_two]
else:
    step2 = (amount_one / data["rates"][selection_one]) * data["rates"][selection_two]


st.header("Currency 2 value")
st.subheader(step2)