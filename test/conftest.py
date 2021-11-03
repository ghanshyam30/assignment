"""
Pytest considers this file as config to run the tests in the whole package it is placed in
"""
import pytest
from selenium import webdriver
from config.config import Env_Variables
import os

@pytest.fixture(scope="class")
def setup(request):
    # Initialize driver instance    
    current_path = os.getcwd()
    driver = webdriver.Firefox(executable_path=current_path + Env_Variables.DRIVER_BIN)

    # Open env URL for UI test
    driver.get(Env_Variables.BASE_URL)
    request.cls.driver = driver

    # Teardown
    yield
    driver.close()  # Replace this with quit() later

# To set the custom report title
def pytest_html_report_title(report):
    report.title = "Assignment: test report"