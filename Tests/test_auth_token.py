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
class TestAuth:

    def test_auth(self):
        log.logger.info('verifying authentication ')
        res = requests.post(read_config('auth_url','auth'),headers=read_json('..\\DATA\\headers.json'),json=read_json('..\\DATA\\auth_data.json'))
        print(read_config('auth_url','auth'))
        print(res.status_code)
        print(res.json())
        #print()