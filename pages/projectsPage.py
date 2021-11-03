from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Env_Variables
from pages.basePageLib import BasePage

class projectsPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        
    #Locators
    RELEASED_PROJECTS_LOCATOR = "//a[(contains(.,'Projects') and not(contains(@href,'beta'))) and @class='filter-item']"
    PROJECTS_SECTION_LIST_LOCATOR = "//div[@id='projects-results']"
    PROJECTS_NAME_LOCATOR = "descendant::h4/a"
    PROJECTS_DETAILS_LOCATOR = "descendant::p"

    # To chose the projects tab
    def choose_released_projects(self):
        # Refresh the page because sometimes the elements dont reflect and not found
        self.driver.refresh()
        # Navigate to released projects
        self.click_element(self.RELEASED_PROJECTS_LOCATOR)

    # To find the project records
    def find_project_records(self):
        self.wait_for_element.until(EC.presence_of_all_elements_located((By.XPATH,self.PROJECTS_SECTION_LIST_LOCATOR)))
        projects_section_list = self.driver.find_elements_by_xpath(self.PROJECTS_SECTION_LIST_LOCATOR)
        
        # dictionary to store repoository name,description pairs
        projects_data_ui = {}
        for record in projects_section_list:
            projects_name = projects_description = None
            projects_name = record.find_element_by_xpath(self.PROJECTS_NAME_LOCATOR).text
            
            # Handle when project description is empty
            try:
                projects_description = record.find_element_by_xpath(self.PROJECTS_DETAILS_LOCATOR).text
            except Exception:
                print("Project description not fond")

            projects_data_ui[projects_name] = projects_description
        
        return projects_data_ui