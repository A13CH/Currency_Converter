""" Streamlit front-end for api.weather.gov """
import streamlit as st
from requests import get
from time import sleep
import json

#def load_data() -> None:
    #global symbols, data

    #sleep(2) # just to show that requests may take some time

    #data = get("http://api.exchangeratesapi.io/v1/latest?access_key=c3128c5d3ea7324688906d0190169f07", timeout=3).json()

    #currencies = get("https://api.exchangeratesapi.io/v1/symbols?access_key=c3128c5d3ea7324688906d0190169f07", timeout=3).json()
    # List to store the currency symbols
    #symbols = []
    # Loop through the dictionary and populate the list
    #for symbol, name in currencies["symbols"].items():
    #symbols.append(f"{symbol} - {name}")  # Add the symbol-value pair (e.g., "AED - United Arab Emirates Dirham")

#load_data()



#Temporary section to avoid API use, delete after uncommenting previos section

#load_data()
with open("data.json", 'r') as file:
    data = json.load(file)

with open("currencies.json", 'r') as file:
    currencies = json.load(file)

# List to store the symbol-value pair strings
symbols = []

# Loop through the dictionary and populate both lists
for symbol, name in currencies["symbols"].items():
    symbols.append(f"{symbol} - {name}")  # Add the symbol-value pair (e.g., "AED - United Arab Emirates Dirham")



#end temporary section



# Website title
st.title("Currency Converter")

amount_one = st.number_input("Value")
# Selectbox for initial currency
selection_one = st.selectbox("From", symbols, index=0, key="Select a starting currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# Reformatting initial currency selection to get symbol
symbol_one = selection_one.split(' ')[0]

# Create three columns: left, center, and right
col1, col2, col3 = st.columns([1, 2, 1])
# Use the center column to display the image
with col2:
    st.image("images/exchange.png", width = 300)

# Selectbox for currency to convert to 
selection_two = st.selectbox("To", symbols, index=0, key="Select a ending currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# Reformatting second currency selection to get symbol
symbol_two = selection_two.split(' ')[0]

# Conversion logic
if selection_one is "EUR":
    converted_value = amount_one * data["rates"][symbol_two]
else:
    converted_value = (amount_one / data["rates"][symbol_one]) * data["rates"][symbol_two]

# Display converted value
st.subheader(f"{amount_one} {symbol_one} is equal to {round(converted_value, 2)} {symbol_two}")
