import pytest
from selenium import webdriver
from selenium.webdriver.common import selenium_manager
from configparser import ConfigParser
import requests
import sys
import json
#import jsonpath


def read_config(locator,value):
    config = ConfigParser()
    config.read("..\config.ini")
    return config.get(locator,value)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def invoke_browser(request):
    browser = request.config.getoption("--browser_name")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


def read_json(file):
    with open(file,'r') as work_file:
        data = json.load(work_file)
        return data



#read_json('..\\DATA\\headers.json')
# read_json('..\\DATA\\auth_data.json')