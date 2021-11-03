import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from pages.projectsPage import projectsPage
from config.config import Env_Variables
from test.BaseTest import BaseTest
import requests
from lxml import html
from additionalLibraries.additional_features import Additional_Functionalities

class Test_Projects(BaseTest):
    ui_projects_dict ={}
    api_projects_dict ={}

    # UI test to find all projects
    @pytest.mark.ui
    @pytest.mark.regression
    def test_get_projects_info(self):
        self.homePageObj = homePage(self.driver)        
        self.homePageObj.select_category("projects")
        self.projectsPageObj = projectsPage(self.driver)
        self.projectsPageObj.choose_released_projects()
        Test_Projects.ui_projects_dict = self.projectsPageObj.find_project_records()

    # API test to find all projects
    @pytest.mark.regression
    def test_get_projects_api(self):
        # Prepare request
        ENDPOINT = "/orgs/django/projects"
        URL = Env_Variables.BASE_URI + ENDPOINT

        #Execute request
        raw_response = requests.get(URL)

        # Response Validation
        assert raw_response.status_code == 200
        
        dictionary_response_projects = raw_response.json()
        for item in dictionary_response_projects:
            project_name = project_description = ''
            project_name = item['name']
            project_description = item['body']        
            Test_Projects.api_projects_dict[project_name] = project_description

    # Validate both UI and API return same records or not
    @pytest.mark.regression
    def test_ui_api_response_validation(self):
        ui_projects_dict = self.ui_projects_dict
        print(ui_projects_dict)
        api_projects_dict = self.api_projects_dict
        print(api_projects_dict)
        assert ui_projects_dict == api_projects_dict
