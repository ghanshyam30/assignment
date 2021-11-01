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

class Test_SearchRepository(BaseTest):
    
    @pytest.mark.regression
    def test_get_repositories_info(self):
        homePageObj = homePage(self.driver)       
        homePageObj.select_category("repositories")
        repoSearchObj = repositoriesPage(self.driver)
        repoSearchObj.select_type_for_search("Sources")
        repoSearchObj.search_repositories_with_text("developer friendly")
        repoSearchObj.choose_repository("channels")