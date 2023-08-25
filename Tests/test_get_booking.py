import logging
import time

import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import read_config, read_json
from Logging import Loggier


log = Loggier(__name__,logging.INFO)

@pytest.mark.usefixtures("invoke_browser")
class TestCreateBooking:

    def test_auth(self):
        time.sleep(3)
        res = requests.post(read_config('auth_url','auth'),headers=read_json('..\\DATA\\headers.json'),json=read_json('..\\DATA\\auth_data.json'))
        print(read_config('auth_url','auth'))
        print(res.status_code)
        print(res.json())
    def test_create_booking(self):

        res = requests.post(read_config('urls','bookings'),headers=read_json('..\\DATA\\headers.json'),json=read_json('..\\DATA\\createbooking.json'))
        print(read_config('urls','bookings'))
        print(res.status_code)
        print(res.json())

    def test_get_booking(self):
        res = requests.get(read_config('urls','bookings')+'/2148')
        #print(read_config('urls','bookings'))
        print(res.status_code)
        print(res.json())
        #print()

    def test_delete_booking(self):
        res = requests.delete(read_config('urls','bookings')+'2148')
        print(res.status_code)