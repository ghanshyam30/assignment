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
    @pytest.mark.temp
    def test_get_projects_info(self):
        self.homePageObj = homePage(self.driver)        
        self.homePageObj.select_category("projects")
        self.projectsPageObj = projectsPage(self.driver)
        self.projectsPageObj.choose_released_projects()
        Test_Projects.ui_projects_dict = self.projectsPageObj.find_project_records()
        print(Test_Projects.ui_projects_dict)

    api_projects_dict ={}
    @pytest.mark.temp
    def test_get_projects_api(self):
        
        ENDPOINT = "/orgs/django/projects"
        URL = Env_Variables.BASE_URI + ENDPOINT
        # print(URL)
        raw_response = requests.get(URL)
        assert raw_response.status_code == 200
        api_projects_dict= Additional_Functionalities.convert_projects_html_dict(raw_response.text)
        print(api_projects_dict)     

    @pytest.mark.temp
    def test_ui_api_response_validation(self):
        ui_projects_dict = Test_Projects.ui_projects_dict
        api_projects_dict = Test_Projects.api_projects_dict
        print(len(api_projects_dict))
        print(len(ui_projects_dict))
        if len(ui_projects_dict) == len(api_projects_dict):
            matched_records = Additional_Functionalities.compare_ui_api_responses(ui_projects_dict,api_projects_dict)
            print(matched_records)
            print(len(ui_projects_dict))
            assert matched_records == len(ui_projects_dict)
        else:
            assert False
