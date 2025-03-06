""" Streamlit front-end for currency_exchange """
import streamlit as st
from requests import get
from time import sleep
import json
from data import get_data, get_currency_list

st.set_page_config(
    page_title="Currency Coverter",
    page_icon="💰",
)

#simpliy before deploying with data = get_data()
with open("./app/data/data.json", 'r') as file:
    exchange_data = json.load(file)

#simpliy before deploying with data = get_currency_list()
with open("./app/data/currency_list.json", 'r') as file:
    currency_list = json.load(file)

# List to store the symbol-value pair strings
symbols = []

# Loop through the dictionary and populate the list
for symbol, name in currency_list["symbols"].items():
    symbols.append(f"{symbol} - {name}")  # Add the symbol-value pair (e.g., "AED - United Arab Emirates Dirham")

# Website title
st.title("Currency Converter")

amount_one = st.number_input("Value")

# Selectbox for initial currency
selection_one = st.selectbox("From", symbols, index=0, key="Select a starting currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# Reformatting selection_one to get symbol_one
symbol_one = selection_one.split(' ')[0]

# Create three columns: left, center, and right
col1, col2, col3 = st.columns([1, 1, 1])
# Use the center column to display the image
with col2:
    st.image("./images/arrows.svg", width = 200)

# Selectbox for currency to convert to 
selection_two = st.selectbox("To", symbols, index=0, key="Select a ending currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# Reformatting selection_two to get symbol_two
symbol_two = selection_two.split(' ')[0]

# Conversion logic
if selection_one is "EUR":
    converted_value = amount_one * exchange_data["rates"][symbol_two]
else:
    converted_value = (amount_one / exchange_data["rates"][symbol_one]) * exchange_data["rates"][symbol_two]

# Display converted value
st.subheader(f"{amount_one} {symbol_one} is equal to {round(converted_value, 2)} {symbol_two}")