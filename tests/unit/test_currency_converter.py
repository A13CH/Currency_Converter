"""
File: test_currency_converter.py
Author: Alec Hoelscher
Date: 03/06/2024
Description: Test cases for the currency_converter program
"""

from src.data import get_data, get_currency_list
from json import load

def test_get_data() -> None:
    """Testing get_data function"""
    data = get_data()
    with open("./src/data/data.json", "r") as file:
        test_data = load(file)
    assert data == test_data

def test_get_currency_list() -> None:
    """Testing get_currency_list function"""
    currency_list = get_currency_list()
    with open("./src/data/currency_list.json", "r") as file:
        test_currency_data = load(file)
    assert currency_list == test_currency_data

