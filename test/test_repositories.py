import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from pages.repositoriesPage import repositoriesPage
from config.config import Env_Variables
from test.BaseTest import BaseTest
import requests
from lxml import html
from additionalLibraries.additional_features import Additional_Functionalities
import logging

class Test_Repositories(BaseTest):
    # Class variables - so that they can be accessible throughout the class
    ui_repo_dict = {}
    api_repo_dict = {}
    repositories_url = ""

    # UI test to get repositories records
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_get_repositories_info(self):
        Test_Repositories.ui_repo_dict = {}
        self.homePageObj = homePage(self.driver)        
        self.homePageObj.select_category("repositories")
        self.repositories_url = self.driver.current_url
        self.repositoriesPageObj = repositoriesPage(self.driver)
        Test_Repositories.ui_repo_dict = self.repositoriesPageObj.find_repository_records()
        logging.debug(f"{Test_Repositories.ui_repo_dict}")

    # API test to get repositories records
    @pytest.mark.smoke
    def test_get_repositories_api(self):
        Test_Repositories.api_repo_dict = {}
        # Prepare request 
        if "/orgs/" in self.repositories_url:
            ENDPOINT = "/orgs/"+ self.repo_to_test +"/repos"
            URL = Env_Variables.BASE_URI + ENDPOINT
        else:
            ENDPOINT = "/users/"+ self.repo_to_test +"/repos"
            URL = Env_Variables.BASE_URI + ENDPOINT

        # Execute request
        raw_response = requests.get(URL)
        logging.info(f"URL:{URL}")
        
        # Response validation
        assert raw_response.status_code == 200

        dictionary_response_repos = raw_response.json()
        for item in dictionary_response_repos:
            repo_name = repo_description = ''
            repo_name = item['name']
            repo_description = item['description']        
            Test_Repositories.api_repo_dict[repo_name] = repo_description
        logging.debug(f"{Test_Repositories.api_repo_dict}")        

    @pytest.mark.smoke
    def test_ui_api_response_validation(self):
        ui_repo_dict = Test_Repositories.ui_repo_dict
        api_repo_dict = Test_Repositories.api_repo_dict
        logging.info(f"UI dict: {ui_repo_dict}")
        logging.info(f"API dict: {api_repo_dict}")
        assert ui_repo_dict == api_repo_dict