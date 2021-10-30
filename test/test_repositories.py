import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from config.config import Env_Variables
from test.BaseTest import BaseTest

class Test_Repositories(BaseTest):
    
    def test_GetRepositoryInfo(self):
        self.random = homePage(self.driver)        
        # random.load()                     # To be replaced by setup method
        self.random.select_category("repositories")
        ui_repo_dict = self.random.find_repository_records()
        print("="*20)
        print("Elements collection length: ",ui_repo_dict)
        print("="*20)
        
        # random.closeDriver()              # To be replaced by teardown method
