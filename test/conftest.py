"""
Pytest considers this file as config to run the tests in the whole package it is placed in
"""
import pytest
from selenium import webdriver
from config.config import Env_Variables

@pytest.fixture(scope="class")
def setup(request):
    # Initialize driver instance
    driver = webdriver.Firefox(executable_path=Env_Variables.DRIVER_BIN)

    # Open env URL for UI test
    driver.get(Env_Variables.BASE_URL)
    request.cls.driver = driver

    # Teardown
    yield
    driver.close()  # Replace this with quit() later