import logging

import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import read_config
from Logging import Loggier


log = Loggier(__name__,logging.INFO)

@pytest.mark.usefixtures("invoke_browser")
class TestBookings:

    def test_get_bookings(self):
        res = requests.get(read_config('urls','bookings'))
        log.logger.info('creating first test with statuscode verification')
        print(res.status_code)
        assert res.status_code == 200
        print(res.text)
        log.logger.info('verified status code')