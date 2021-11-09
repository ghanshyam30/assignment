"""
Pytest considers this file as config to run the tests in the whole package it is placed in
"""
import pytest
from selenium import webdriver
from config.config import Env_Variables
import os
import logging

@pytest.fixture(params=Env_Variables.REPO_LIST,scope="class")
def setup(request):
    # Initialize driver instance    
    current_path = os.getcwd()
    driver = webdriver.Firefox(executable_path=current_path + Env_Variables.DRIVER_BIN)
    # Open env URL for UI test
    driver.get(Env_Variables.BASE_URL+"/"+request.param)
    request.cls.driver = driver
    request.cls.repo_to_test = request.param

    # Teardown
    yield
    driver.quit()  
    logging.info("closing the browser")

# To set the custom report title
def pytest_html_report_title(report):
    report.title = "Assignment: test report"