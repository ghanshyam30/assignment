import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from config.config import Env_Variables
from test.BaseTest import BaseTest
import requests
from lxml import html
from additionalLibraries.additional_features import Additional_Functionalities

class Test_Packages(BaseTest):
    
    # Navigate to packages section
    @pytest.mark.regression
    def test_get_packages_info(self):
        self.homePageObj = homePage(self.driver)        
        self.homePageObj.select_category("packages")

    # 
    @pytest.mark.xfail
    def test_get_packages_api(self):
        # Prepare request 
        ENDPOINT = "/orgs/django/packages"
        URL = Env_Variables.BASE_URI + ENDPOINT

        # Execute REST
        raw_response = requests.get(URL)

        # Response Validation
        assert raw_response.status_code == 200