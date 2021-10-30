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
    # api_repo_dict = {}
    def test_GetRepositoryInfo(self):
        self.random = homePage(self.driver)        
        # random.load()                     # To be replaced by setup method
        self.random.select_category("repositories")
        Test_Repositories.ui_repo_dict = self.random.find_repository_records()
        print("="*20)
        print("Elements collection length: ",len(Test_Repositories.ui_repo_dict))
        print("-"*20)

        print(Test_Repositories.ui_repo_dict)
        print("*"*60)
        # random.closeDriver()              # To be replaced by teardown method

class Test_RepositoriesAPI():
    api_repo_dict = {}   
    def test_GetRepositoriesAPI(self):
        self.URL = Env_Variables.BASE_URI + Env_Variables.ENDPOINT
        print(self.URL)
        self.html_page_response = requests.get(self.URL)
        # page = requests.get("https://github.com/orgs/django/repositories")
        traceable_html_response_tree = html.fromstring(self.html_page_response.content)

        #This will create a list of keys which is repository names:    
        repo_name_list = traceable_html_response_tree.xpath('//*[@itemprop="owns"]/following::h3/a/text()')
        # #This will create a list of repo_description_list
        repo_description_list = traceable_html_response_tree.xpath('//*[@itemprop="owns"]/following::p/text()')
        # print('repo_name_list: ', repo_name_list)
        # print('repo_description_list: ', repo_description_list)

        #Dummy xpath test
        # title = tree.xpath("//head/title/text()")

        #To store repository name and its description in a dict record
        # api_repo_dict = {}
        for iter_index in range (0,len(repo_name_list)):
            # format the tab, nextline multispaced string to a concrete one
            new_item_formatted = repo_name_list[iter_index].split()
            repo_name = " ".join(new_item_formatted)

            # format the tab, nextline multispaced string to a concrete one
            new_value_formatted = repo_description_list[iter_index].split()
            repo_description = " ".join(new_value_formatted)

            # Store repository name and descrition against it for better maintenance
            Test_RepositoriesAPI.api_repo_dict[repo_name] = repo_description

        print("API dict length=",len(Test_RepositoriesAPI.api_repo_dict))
        print(Test_RepositoriesAPI.api_repo_dict)

def test_ui_api_response_validation():
    ui_repo_dict = Test_Repositories.ui_repo_dict
    api_repo_dict = Test_RepositoriesAPI.api_repo_dict
    if len(ui_repo_dict) == len(api_repo_dict):
        matched_records = Additional_Functionalities.compare_ui_api_responses(ui_repo_dict,api_repo_dict)
        assert matched_records == len(ui_repo_dict)
    else:
        assert False             
                          
