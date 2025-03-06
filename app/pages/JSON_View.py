import streamlit as st
import json
from data import get_data, get_currency_list, DATA_FILE, CURRENCY_LIST_FILE

with open("./app/data/data.json", 'r') as file:
    exchange_data = json.load(file)

with open("./app/data/currency_list.json", 'r') as file:
    currency_list = json.load(file)

st.title("Exchange Rates")
st.json(exchange_data)

st.title("List of Currencies")
st.json(currency_list)

with open(DATA_FILE) as f:
    st.sidebar.download_button("Download Exchange Rates", f, file_name="exchange_rates.json", mime="application/json", type="primary")

with open(CURRENCY_LIST_FILE) as f:
    st.sidebar.download_button("Download Currency List", f, file_name="currency_list.json", mime="application/json", type="primary")
