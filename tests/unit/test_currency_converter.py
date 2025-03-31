"""
File: test_currency_converter.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Test cases for the currency_converter program
"""

import streamlit as st
from requests import get
from src.data import get_data, get_currency_list
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("SECRET_KEY")
if not key:
    raise ValueError("SECRET_KEY is not set")

def test_get_data() -> None:
    """Testing get_data function"""
    data = get_data()
    assert data == get(f"http://api.exchangeratesapi.io/v1/latest?access_key={key}", timeout=3).json()

def test_get_currency_list() -> None:
    """Testing get_currency_list function"""
    currency_list = get_currency_list()
    assert currency_list == get(f"https://api.exchangeratesapi.io/v1/symbols?access_key={key}", timeout=3).json()

