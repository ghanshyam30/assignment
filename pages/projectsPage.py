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
        self.wait_for_element = WebDriverWait(self.driver,7)
        
    #Locators
    RELEASED_PROJECTS_LOCATOR = "//a[(contains(.,'Projects') and not(contains(@href,'beta'))) and @class='filter-item']"
    PROJECTS_SECTION_LIST_LOCATOR = "//div[@id='projects-results']"
    PROJECTS_NAME_LOCATOR = "descendant::h4/a"
    PROJECTS_DETAILS_LOCATOR = "descendant::p"

    def choose_released_projects(self):
        self.driver.refresh()
        self.click_element(self.RELEASED_PROJECTS_LOCATOR)

    def find_project_records(self):
        # self.wait_for_element()
        self.wait_for_element.until(EC.presence_of_all_elements_located((By.XPATH,self.PROJECTS_SECTION_LIST_LOCATOR)))
        projects_section_list = self.driver.find_elements_by_xpath(self.PROJECTS_SECTION_LIST_LOCATOR)
        # dictionary to store repoository name,description pairs
        projects_data_ui = {}
        for record in projects_section_list:  
            projects_name = projects_description = ""          
            try: #Get the repository name
                projects_name = record.find_element_by_xpath(self.PROJECTS_NAME_LOCATOR).text
                # print(projects_name)
            except Exception as e:
                print("Project name not found")
            try: #Get the repository description
                projects_description = record.find_element_by_xpath(self.PROJECTS_DETAILS_LOCATOR).text
                # print(projects_description)
            except Exception as e: # Exception handling
                print("Project description not fond")

            
            if projects_name and projects_description:
                projects_data_ui[projects_name] = projects_description
            elif  projects_name and not projects_description:
                projects_data_ui[projects_name] = "NA"
        
        return projects_data_ui