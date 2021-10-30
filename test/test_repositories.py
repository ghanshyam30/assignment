import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from config.config import Env_Variables
from test.BaseTest import BaseTest
import requests
from lxml import html
from additionalLibraries.additional_features import Additional_Functionalities

class Test_Repositories(BaseTest):
    
    ui_repo_dict = {}
    def test_GetRepositoryInfo(self):
        self.homePageObj = homePage(self.driver)        
        self.homePageObj.select_category("repositories")
        Test_Repositories.ui_repo_dict = self.homePageObj.find_repository_records()

        # print(Test_Repositories.ui_repo_dict)

    api_repo_dict = {}
    def test_GetRepositoriesAPI(self):
        URL = Env_Variables.BASE_URI + Env_Variables.ENDPOINT
        print(URL)
        raw_response = requests.get(URL)
        Test_Repositories.api_repo_dict= Additional_Functionalities.convert_html_dict(raw_response.text)
        # print(Test_Repositories.api_repo_dict)        

# @pytest.mark.skip
def test_ui_api_response_validation():
    ui_repo_dict = Test_Repositories.ui_repo_dict
    api_repo_dict = Test_Repositories.api_repo_dict
    if len(ui_repo_dict) == len(api_repo_dict):
        matched_records = Additional_Functionalities.compare_ui_api_responses(ui_repo_dict,api_repo_dict)
        assert matched_records == len(ui_repo_dict)
    else:
        assert False             
                          
