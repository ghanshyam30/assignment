from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Env_Variables
from pages.basePageLib import BasePage
import logging

class repositoriesPage(BasePage):
    
    #Locators
    REPOSITORIES_SECTION_LIST_LOCATOR = "//*[@itemprop='owns']"
    REPOSITORIES_NAME_LOCATOR = "descendant::h3/a"
    REPOSITORIES_DESCRIPTION_LOCATOR = "descendant::p"
    SEARCHBOX_LOCATOR = "//input[@type='search']"
    SEARCH_TYPE_OPTIONS = "//summary[@aria-haspopup='menu']/span[text()='Type']"
    TYPE_OPTIONS_ALL = "//span[@class='text-normal' and text()='All']"
    TYPE_OPTIONS_SOURCES = "//span[@class='text-normal' and text()='Sources']"
    TYPE_OPTIONS_FORKS = "//span[@class='text-normal' and text()='Forks']"
    TYPE_OPTIONS_ARCHIVED = "//span[@class='text-normal' and text()='Archived']"
    TYPE_OPTIONS_MIRRORS = "//span[@class='text-normal' and text()='Mirrors']"
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Search repository from search functionality on UI
    def search_repositories_with_text(self, text_to_search_param):
        text_to_search = text_to_search_param
        self.input_text(self.SEARCHBOX_LOCATOR, text_to_search)

    # To apply type filter for search operation
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
    
    # To open expected repository after search
    def choose_repository(self, repository_name_param):
        self.driver.refresh()
        REPOSITORY_LOCATOR = "//a[@itemprop='name codeRepository' and contains(text(),'" + repository_name_param + "')]"
        self.click_element(REPOSITORY_LOCATOR)

    
    def find_repository_records(self):
        # Wait for the list of elements which has repository records
        self.wait_for_element.until(EC.presence_of_all_elements_located((By.XPATH,self.REPOSITORIES_SECTION_LIST_LOCATOR)))
        repositories_section_list = self.driver.find_elements_by_xpath(self.REPOSITORIES_SECTION_LIST_LOCATOR)
        
        # dictionary to store repoository name,description pairs
        repositories_data_ui = {}

        # For every record find name and description
        for record in repositories_section_list:  

            # Set the name and description to None
            repo_name = repo_description = None          
            
            repo_name = record.find_element_by_xpath(self.REPOSITORIES_NAME_LOCATOR).text
            # print(repo_name)
            try: #Get the repository description
                repo_description = record.find_element_by_xpath(self.REPOSITORIES_DESCRIPTION_LOCATOR).text
                # print(repo_description)
            except Exception: # Exception handling
                logging.warning(f"Repository description not fond for repo name: {repo_name}")

            repositories_data_ui[repo_name]=repo_description
        
        return repositories_data_ui