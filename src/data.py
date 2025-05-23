"""
File: data.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Program to obtain the current currency exchange rates
"""

from json import dump, load
from requests import get
import streamlit as st
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("SECRET_KEY")
if not key:
    raise ValueError("SECRET_KEY is not set")

DATA_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={key}"
CURRENCY_LIST_URL = f"https://api.exchangeratesapi.io/v1/symbols?access_key={key}"
DATA_FILE = "./src/data/data.json"
CURRENCY_LIST_FILE = "./src/data/currency_list.json"

@st.cache_data(show_spinner="Fetching data from API...", ttl=timedelta(days=1))
def get_data(data_url: str = DATA_URL, data_file: str = DATA_FILE) -> dict:
    """Get rate data from the API"""
    try:
        exchange_data = get(url=data_url, timeout=3).json()
        if exchange_data and "error" not in exchange_data:
            # as a backup, save the data in a file
            with open(data_file, "w") as file:
                dump(exchange_data, file)
            return exchange_data
        with open(data_file, "r") as file:
            exchange_data = load(file)
        st.warning("Using cached exchange rate data", icon="⚠️")
        return exchange_data
    except OSError as err:
        st.error(str(err))
    except TypeError as err:
        st.error(str(err))
    return {}

@st.cache_data(show_spinner="Fetching data from API...", ttl=timedelta(days=1))
def get_currency_list(currency_list_url: str = CURRENCY_LIST_URL, currency_list_file: str = CURRENCY_LIST_FILE) -> dict:
    """Get currency list data from the API"""
    try:
        currency_data = get(url=currency_list_url, timeout=3).json()
        if currency_data and "error" not in currency_data:
            # as a backup, save the currency_data in a file
            with open(currency_list_file, "w") as file:
                dump(currency_data, file)
            return currency_data
        with open(currency_list_file, "r") as file:
            currency_data = load(file)
        st.warning("Using cached currency list data", icon="⚠️")
        return currency_data
    except OSError as err:
        st.error(str(err))
    except TypeError as err:
        st.error(str(err))
    return {}

if __name__ == '__main__':
    get_data()
    get_currency_list()