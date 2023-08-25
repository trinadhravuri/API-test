import logging

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

    def test_update_booking(self):
        res = requests.put(read_config('urls','mybooking_id'),headers=read_json('headers.json'),json=read_json('updatebooking.json'))
        print(read_config('urls','bookings'))
        print(res.status_code)
        print(res.json())
        #print()