"""
File: data.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Program to obtain the current currency exchange rates
"""

from json import dump, load
from requests import get
import streamlit as st

key = st.secrets["API_key"]

DATA_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={key}"
CURRENCY_LIST_URL = f"https://api.exchangeratesapi.io/v1/symbols?access_key={key}"
DATA_FILE = "./app/data/data.json"
CURRENCY_LIST_FILE = "./app/data/currency_list.json"

@st.cache_data(show_spinner="Fetching data from API...", ttl=60*10)
def get_data(data_url: str = DATA_URL, data_file: str = DATA_FILE) -> dict:
    """Get rate data from the API"""
    try:
        exchange_data = get(url=data_url, timeout=3).json()
        if exchange_data:
            # as a backup, save the data in a file
            with open(data_file, "w") as file:
                dump(exchange_data, file)
            return exchange_data
        with open(data_file, "r") as file:
            exchange_data = load(file)
        st.warning("Using cached forecast data", icon="⚠️")
        return exchange_data
    except OSError as err:
        st.error(str(err))
    except TypeError as err:
        st.error(str(err))
    return {}

@st.cache_data(show_spinner="Fetching data from API...", ttl=60*10)
def get_currency_list(currency_list_url: str = CURRENCY_LIST_URL, currency_list_file: str = CURRENCY_LIST_FILE):
    """Get currency list data from the API"""
    try:
        currency_data = get(url=currency_list_url, timeout=3).json()
        if currency_data:
            # as a backup, save the currency_data in a file
            with open(currency_list_file, "w") as file:
                dump(currency_data, file)
            return currency_data
        with open(currency_list_file, "r") as file:
            currency_data = load(file)
        st.warning("Using cached forecast data", icon="⚠️")
        return currency_data
    except OSError as err:
        st.error(str(err))
    except TypeError as err:
        st.error(str(err))
    return {}

if __name__ == '__main__':
    get_data()
    get_currency_list()