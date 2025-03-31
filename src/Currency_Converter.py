"""
File: Currency_Converter.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Streamlit front-end for currency_exchange
"""

import streamlit as st
from data import get_data, get_currency_list, CURRENCY_LIST_URL

st.set_page_config(
    page_title="Currency Coverter",
    page_icon="💰",
)

exchange_data = get_data()
currency_list = get_currency_list()

# List to store the symbol-value pair strings
symbols = []

# Loop through the dictionary and populate the list
for symbol, name in currency_list["symbols"].items():
    symbols.append(f"{symbol} - {name}")  # Add the symbol-value pair (e.g., "AED - United Arab Emirates Dirham")

# Website title
st.title("Currency Converter")

# Collect value to convert
amount_one = st.number_input("Value")

# Selectbox for initial currency
selection_one = st.selectbox("From", symbols, index=0, key="Select a starting currency", help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# Reformatting selection_one to get symbol_one
symbol_one = selection_one.split(' ')[0]

# Creating 3 columns for the arrows icon
col1, col2, col3 = st.columns([1, 1, 1])
# Use the center column to display the image
with col2:
    st.image("./app/images/arrows.svg", width = 200)

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