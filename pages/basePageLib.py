import pytest
from selenium import webdriver
from config.config import Env_Variables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
"""
Things to do:
1. webdriver wait
2. click
3. text
"""
class BasePage:
    # Constructor to set driver instance and define explicit wait
    def __init__(self,driver):
        self.driver = driver
        self.wait_for_element = WebDriverWait(self.driver,7)

    # Explicit wait for element to before every element action
    def wait_for_element_visibility(self, element_to_wait_for):
        return self.wait_for_element.until(EC.visibility_of_element_located((By.XPATH,element_to_wait_for)))
        
    # Click action for web element
    def click_element(self, element_to_click):
        element_presence = self.wait_for_element_visibility(element_to_click)
        element_presence.click()
    
    # Input text for webelement
    def input_text(self, element_for_input, text_to_input):
        element_to_input = self.wait_for_element_visibility(element_for_input)
        element_to_input.send_keys(text_to_input)