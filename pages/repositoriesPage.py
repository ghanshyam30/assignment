from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Env_Variables
from pages.basePageLib import BasePage

class repositoriesPage(BasePage):
    
    #Locators
    SEARCHBOX_LOCATOR = "//input[@type='search']"
    SEARCH_TYPE_OPTIONS = "//summary[@aria-haspopup='menu']/span[text()='Type']"
    TYPE_OPTIONS_ALL = "//span[@class='text-normal' and text()='All']"
    TYPE_OPTIONS_SOURCES = "//span[@class='text-normal' and text()='Sources']"
    TYPE_OPTIONS_FORKS = "//span[@class='text-normal' and text()='Forks']"
    TYPE_OPTIONS_ARCHIVED = "//span[@class='text-normal' and text()='Archived']"
    TYPE_OPTIONS_MIRRORS = "//span[@class='text-normal' and text()='Mirrors']"
    # SEARCH_SUBMIT = ""
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_for_element = WebDriverWait(self.driver,7)

    def search_repositories_with_text(self, text_to_search_param):
        text_to_search = text_to_search_param
        self.input_text(self.SEARCHBOX_LOCATOR, text_to_search)


    def select_type_for_search(self,type_param):
        self.click_element(self.SEARCH_TYPE_OPTIONS)
        self.type = type_param
        if self.type == "Sources":
            self.click_element(self.TYPE_OPTIONS_SOURCES)
        elif self.type == "Forks":
            self.click_element(self.TYPE_OPTIONS_FORKS)
        elif self.type == "Archived":
            self.click_element(self.TYPE_OPTIONS_ARCHIVED)
        elif self.type == "Mirrors":
            self.click_element(self.TYPE_OPTIONS_MIRRORS)
        else:
            self.click_element(self.TYPE_OPTIONS_ALL)
    
    def choose_repository(self, repository_name_param):
        self.driver.refresh()
        REPOSITORY_LOCATOR = "//a[@itemprop='name codeRepository' and contains(text(),'" + repository_name_param + "')]"
        print("Select repository:",REPOSITORY_LOCATOR)
        self.click_element(REPOSITORY_LOCATOR)