"""
File: test_currency_converter.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Test cases for the currency_converter program
"""

from requests import get
from src.data import get_data, get_currency_list
from dotenv import load_dotenv
import os
from json import load

load_dotenv()

key = os.getenv("SECRET_KEY")
if not key:
    raise ValueError("SECRET_KEY is not set")

with open("./src/data/currency_list.json", "r") as file:
    test_currency_data = load(file)

with open("./src/data/data.json", "r") as file:
    test_data = load(file)

def test_get_data() -> None:
    """Testing get_data function"""
    data = get_data()
    assert data == test_data

def test_get_currency_list() -> None:
    """Testing get_currency_list function"""
    currency_list = get_currency_list()
    assert currency_list == test_currency_data

